/**
 * Suomen Paras — palaute-API ("Anna oma arvio")
 *
 * Endpoints (mounted at suomenparas.antonjalonen.fi/api/* and *.workers.dev/api/*):
 *   POST /api/arvio                       submit one questionnaire answer (stored unapproved)
 *   GET  /api/arvio?vertical=&slug=       approved aggregates + review texts for one company
 *   GET  /api/counts?vertical=            approved review count per company slug in a vertical
 *   GET  /api/admin?key=ADMIN_KEY         moderation page (approve / delete pending reviews)
 *   POST /api/admin/paatos                {key, id, action: "approve"|"delete"}
 *
 * Data lives in D1 (SQLite) — table `arviot`, see schema.sql.
 * Nothing is shown publicly until approved=1 (moderation via /api/admin).
 */

const SLUG_RE = /^[a-z0-9-]{1,60}$/;
const CLAIMS = ["luotettava", "hintansa", "suosittelisin", "uudelleen"];

const ALLOWED_ORIGINS = [
  "https://suomenparas.antonjalonen.fi",
  "https://antonjalonen-cmd.github.io",
];

function corsHeaders(req) {
  const origin = req.headers.get("Origin") || "";
  const ok =
    ALLOWED_ORIGINS.includes(origin) ||
    /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
  return {
    "Access-Control-Allow-Origin": ok ? origin : ALLOWED_ORIGINS[0],
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
  };
}

function json(data, req, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", ...corsHeaders(req) },
  });
}

async function ipHash(req, env) {
  const ip = req.headers.get("CF-Connecting-IP") || "0.0.0.0";
  const data = new TextEncoder().encode(ip + "|" + (env.ADMIN_KEY || "salt"));
  const digest = await crypto.subtle.digest("SHA-256", data);
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function submitArvio(req, env) {
  let body;
  try {
    body = await req.json();
  } catch {
    return json({ error: "invalid json" }, req, 400);
  }
  const vertical = String(body.vertical || "");
  const slug = String(body.slug || "");
  const fiilis = Number(body.fiilis);
  if (!SLUG_RE.test(vertical) || !SLUG_RE.test(slug)) return json({ error: "bad company" }, req, 400);
  if (!Number.isInteger(fiilis) || fiilis < 1 || fiilis > 5) return json({ error: "bad fiilis" }, req, 400);

  const claims = {};
  for (const c of CLAIMS) claims[c] = body[c] ? 1 : 0;
  const nimi = String(body.nimi || "").trim().slice(0, 40) || null;
  const teksti = String(body.teksti || "").trim().slice(0, 600) || null;
  const hash = await ipHash(req, env);

  // one review per visitor per company (soft guard — same network shares an IP)
  const dup = await env.DB.prepare(
    "SELECT id FROM arviot WHERE vertical=?1 AND slug=?2 AND ip_hash=?3 LIMIT 1"
  ).bind(vertical, slug, hash).first();
  if (dup) return json({ error: "already", message: "Olet jo arvioinut tämän yrityksen." }, req, 409);

  await env.DB.prepare(
    `INSERT INTO arviot (vertical, slug, fiilis, luotettava, hintansa, suosittelisin, uudelleen,
                         nimi, teksti, ip_hash, created_at, approved)
     VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,0)`
  ).bind(
    vertical, slug, fiilis,
    claims.luotettava, claims.hintansa, claims.suosittelisin, claims.uudelleen,
    nimi, teksti, hash, new Date().toISOString()
  ).run();

  return json({ ok: true, message: "Kiitos! Arviosi näkyy sivulla tarkistuksen jälkeen." }, req, 201);
}

async function getArvio(req, env, url) {
  const vertical = url.searchParams.get("vertical") || "";
  const slug = url.searchParams.get("slug") || "";
  if (!SLUG_RE.test(vertical) || !SLUG_RE.test(slug)) return json({ error: "bad company" }, req, 400);

  const agg = await env.DB.prepare(
    `SELECT COUNT(*) n, AVG(fiilis) fiilis_avg,
            SUM(luotettava) luotettava, SUM(hintansa) hintansa,
            SUM(suosittelisin) suosittelisin, SUM(uudelleen) uudelleen
     FROM arviot WHERE vertical=?1 AND slug=?2 AND approved=1`
  ).bind(vertical, slug).first();

  const rows = await env.DB.prepare(
    `SELECT fiilis, nimi, teksti, created_at FROM arviot
     WHERE vertical=?1 AND slug=?2 AND approved=1 AND teksti IS NOT NULL
     ORDER BY id DESC LIMIT 50`
  ).bind(vertical, slug).all();

  return json({
    n: agg.n || 0,
    fiilis_avg: agg.n ? Math.round(agg.fiilis_avg * 10) / 10 : null,
    vaitteet: {
      luotettava: agg.luotettava || 0,
      hintansa: agg.hintansa || 0,
      suosittelisin: agg.suosittelisin || 0,
      uudelleen: agg.uudelleen || 0,
    },
    arviot: rows.results.map((r) => ({
      fiilis: r.fiilis, nimi: r.nimi, teksti: r.teksti, pvm: r.created_at.slice(0, 10),
    })),
  }, req);
}

async function getCounts(req, env, url) {
  const vertical = url.searchParams.get("vertical") || "";
  if (!SLUG_RE.test(vertical)) return json({ error: "bad vertical" }, req, 400);
  const rows = await env.DB.prepare(
    "SELECT slug, COUNT(*) n FROM arviot WHERE vertical=?1 AND approved=1 GROUP BY slug"
  ).bind(vertical).all();
  const out = {};
  for (const r of rows.results) out[r.slug] = r.n;
  return json(out, req);
}

// ---------------------------------------------------------------- moderation
const FEEL = { 1: "😠 En käyttäisi enää", 2: "🙁 Huono", 3: "😐 Ok", 4: "🙂 Hyvä", 5: "😀 Erinomainen" };

function escHtml(s) {
  return String(s ?? "").replace(/[&<>"']/g, (m) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));
}

async function adminPage(req, env, url) {
  const key = url.searchParams.get("key") || "";
  if (!env.ADMIN_KEY || key !== env.ADMIN_KEY) return new Response("Ei pääsyä.", { status: 403 });

  const pend = await env.DB.prepare(
    "SELECT * FROM arviot WHERE approved=0 ORDER BY id DESC LIMIT 200").all();
  const done = await env.DB.prepare(
    "SELECT * FROM arviot WHERE approved=1 ORDER BY id DESC LIMIT 50").all();

  const card = (r, pending) => `
    <div class="c" id="r${r.id}">
      <div class="h"><b>${escHtml(r.vertical)} / ${escHtml(r.slug)}</b>
        <span>${FEEL[r.fiilis] || r.fiilis}</span>
        <span class="d">${escHtml(r.created_at.slice(0, 16).replace("T", " "))}</span></div>
      <div class="t">${["luotettava","hintansa","suosittelisin","uudelleen"]
        .filter((k) => r[k]).map((k) => `<span class="tag">${k}</span>`).join("") || '<span class="d">ei väittämiä</span>'}</div>
      ${r.nimi ? `<div><b>${escHtml(r.nimi)}</b></div>` : ""}
      ${r.teksti ? `<p>${escHtml(r.teksti)}</p>` : '<p class="d">(ei tekstiä)</p>'}
      <div class="b">
        ${pending ? `<button onclick="act(${r.id},'approve')">✅ Julkaise</button>` : ""}
        <button class="del" onclick="act(${r.id},'delete')">🗑 Poista</button>
      </div>
    </div>`;

  const html = `<!DOCTYPE html><html lang="fi"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Suomen Paras — palautteen moderointi</title>
<style>
body{font-family:system-ui,sans-serif;background:#EAF2FE;color:#14213F;max-width:760px;margin:0 auto;padding:20px}
h1{font-size:1.3rem}h2{font-size:1.05rem;margin-top:28px}
.c{background:#fff;border:2px solid #C9D9F2;border-radius:12px;padding:14px;margin:10px 0}
.h{display:flex;gap:12px;flex-wrap:wrap;align-items:baseline}
.d{color:#5D6E92;font-size:.85rem}
.tag{display:inline-block;background:#D9E7FC;border-radius:99px;padding:1px 10px;font-size:.78rem;margin-right:6px}
p{margin:8px 0;white-space:pre-wrap}
.b{margin-top:8px}
button{border:2px solid #14213F;border-radius:99px;padding:7px 16px;font-weight:700;cursor:pointer;background:#FFC61A;margin-right:8px}
button.del{background:#fff}
.empty{color:#5D6E92;padding:20px;text-align:center}
</style>
<h1>Palautteen moderointi</h1>
<p class="d">Odottaa: ${pend.results.length} · Julkaistu (viimeiset 50): ${done.results.length}</p>
<h2>Odottaa tarkistusta</h2>
${pend.results.map((r) => card(r, true)).join("") || '<div class="empty">Ei odottavia arvioita 🎉</div>'}
<h2>Julkaistut</h2>
${done.results.map((r) => card(r, false)).join("") || '<div class="empty">Ei julkaistuja arvioita vielä.</div>'}
<script>
async function act(id, action){
  const res = await fetch('/api/admin/paatos', {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({key: ${JSON.stringify(key)}, id, action})});
  if (res.ok) document.getElementById('r'+id).remove(); else alert('Virhe: ' + res.status);
}
</script></html>`;
  return new Response(html, { headers: { "Content-Type": "text/html; charset=utf-8" } });
}

async function adminAction(req, env) {
  let body;
  try { body = await req.json(); } catch { return json({ error: "invalid json" }, req, 400); }
  if (!env.ADMIN_KEY || body.key !== env.ADMIN_KEY) return json({ error: "forbidden" }, req, 403);
  const id = Number(body.id);
  if (!Number.isInteger(id)) return json({ error: "bad id" }, req, 400);
  if (body.action === "approve") {
    await env.DB.prepare("UPDATE arviot SET approved=1 WHERE id=?1").bind(id).run();
  } else if (body.action === "delete") {
    await env.DB.prepare("DELETE FROM arviot WHERE id=?1").bind(id).run();
  } else {
    return json({ error: "bad action" }, req, 400);
  }
  return json({ ok: true }, req);
}


const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

async function submitPaneli(req, env) {
  let body;
  try { body = await req.json(); } catch { return json({ error: "invalid json" }, req, 400); }
  const email = String(body.email || "").trim().toLowerCase().slice(0, 120);
  const nimi = String(body.nimi || "").trim().slice(0, 60) || null;
  if (!EMAIL_RE.test(email)) return json({ error: "bad email", message: "Tarkista sähköpostiosoite." }, req, 400);
  const hash = await ipHash(req, env);
  const dup = await env.DB.prepare("SELECT id FROM paneli WHERE email=?1 LIMIT 1").bind(email).first();
  if (dup) return json({ ok: true, message: "Olet jo paneelissa — kiitos!" }, req);
  await env.DB.prepare(
    "INSERT INTO paneli (email, nimi, ip_hash, created_at) VALUES (?1, ?2, ?3, ?4)"
  ).bind(email, nimi, hash, new Date().toISOString()).run();
  return json({ ok: true, message: "Tervetuloa paneeliin!" }, req);
}

async function adminPaneli(req, env, url) {
  if (url.searchParams.get("key") !== env.ADMIN_KEY) return json({ error: "forbidden" }, req, 403);
  const rows = (await env.DB.prepare("SELECT email, nimi, created_at FROM paneli ORDER BY id DESC").all()).results || [];
  const esc = (t) => String(t || "").replace(/[<>&]/g, (c) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c]));
  const list = rows.map((r) => `<tr><td>${esc(r.email)}</td><td>${esc(r.nimi)}</td><td>${esc(r.created_at)}</td></tr>`).join("");
  const html = `<!doctype html><meta charset="utf-8"><title>Paneeli (${rows.length})</title>
<style>body{font-family:system-ui;margin:24px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px 10px;font-size:14px}</style>
<h1>Tutkimuspaneeli — ${rows.length} jäsentä</h1>
<p><a download="paneeli.csv" href="data:text/csv;charset=utf-8,${encodeURIComponent("email;nimi;liittyi\n" + rows.map((r) => [r.email, r.nimi || "", r.created_at].join(";")).join("\n"))}">Lataa CSV</a></p>
<table><tr><th>Email</th><th>Nimi</th><th>Liittyi</th></tr>${list}</table>`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", ...corsHeaders(req) } });
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const path = url.pathname.replace(/\/+$/, "");

    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders(req) });

    if (path === "/api/arvio" && req.method === "POST") return submitArvio(req, env);
    if (path === "/api/arvio" && req.method === "GET") return getArvio(req, env, url);
    if (path === "/api/counts" && req.method === "GET") return getCounts(req, env, url);
    if (path === "/api/paneli" && req.method === "POST") return submitPaneli(req, env);
    if (path === "/api/paneli-admin" && req.method === "GET") return adminPaneli(req, env, url);
    if (path === "/api/admin" && req.method === "GET") return adminPage(req, env, url);
    if (path === "/api/admin/paatos" && req.method === "POST") return adminAction(req, env);

    return json({ error: "not found" }, req, 404);
  },
};
