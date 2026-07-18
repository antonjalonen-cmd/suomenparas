# -*- coding: utf-8 -*-
"""Fetch a public page WITH JavaScript rendering, and print it as plain text.

This is the "JS-fetch fix" queued in QUEUED_CATEGORIES.md: `fetch_page.py` (curl)
gets HTTP 200 from op.fi but only ~900 chars of login shell, because the page is
built client-side. That single gap cost the `pankit` category (OP unmeasurable)
and excluded Pohjola Vakuutus from all four insurance lines. Whatever renders for
Lighthouse can render for extraction — this tool is that: an ordinary headless
Chromium via Playwright, nothing more.

The boundary (EXTRACTION_BRIEF.md, learned 17.7.2026 — read it before "improving"
this tool):
  - NO bot-protection evasion. Default headless UA, no stealth patches, no CAPTCHA
    solving, no challenge workarounds. If a site keeps automated clients out, the
    answer is "we could not measure it" and the page discloses the gap.
  - NO accepting consent banners. Clicking "accept" consents to tracking on a real
    person's behalf. This tool only ever clicks an explicit DECLINE / "vain
    välttämättömät" control, and if none exists it leaves the banner alone.

Output contract matches fetch_page.py (status line, final URL, char count, text)
so extraction agents can use either interchangeably. If output here is still tiny,
the site is either challenge-walled or empty — report that honestly, score
"osittain", and never invent a reason.

Requires: node + the `playwright` npm package with its Chromium. On the remote
build environments both are preinstalled globally (PLAYWRIGHT_BROWSERS_PATH is
set); locally: `npm i -g playwright && npx playwright install chromium`.

Usage:  python pipeline/render_page.py <url> [--raw] [--max-chars N] [--wait-ms N]
"""
import json
import os
import shutil
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Decline-only consent handling. A control is clicked ONLY if its text matches a
# DECLINE pattern and none of the ACCEPT patterns — never the other way around.
JS = r"""
const { chromium } = require('playwright');

// node -e swallows the `--`; the first real argument lands at argv[1].
const url = process.argv[1];
const waitMs = parseInt(process.argv[2] || '2500', 10);
const wantRaw = process.argv[3] === 'raw';

const DECLINE = [
  /vain\s+v[aä]ltt[aä]m[aä]tt[oö]m[aä]t/i, /hylk[aä][aä]/i, /kiell[aä]/i,
  /en\s+hyv[aä]ksy/i, /reject(\s+all)?/i, /decline/i, /refuse/i,
  /only\s+(strictly\s+)?necessary/i, /necessary\s+only/i, /essential\s+only/i,
  /endast\s+n[oö]dv[aä]ndiga/i, /avvisa/i, /neka/i,
];
const ACCEPT = [
  /hyv[aä]ksy/i, /salli/i, /accept/i, /allow/i, /agree/i, /godk[aä]nn/i,
  /till[aå]t/i, /ok(,|\s|$)/i,
];

async function declineConsent(frame) {
  // Runs inside the page: find a visible decline-only control and click it with
  // an ordinary DOM click. Returns the clicked text, or null.
  return await frame.evaluate(([declineSrc, acceptSrc]) => {
    const decline = declineSrc.map(s => new RegExp(s.source, s.flags || 'i'));
    const accept = acceptSrc.map(s => new RegExp(s.source, s.flags || 'i'));
    const els = document.querySelectorAll('button, [role="button"], a, input[type="button"], input[type="submit"]');
    for (const el of els) {
      const t = (el.innerText || el.value || '').trim();
      if (!t || t.length > 80) continue;
      const st = getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden') continue;
      if (decline.some(r => r.test(t)) && !accept.some(r => r.test(t))) {
        el.click();
        return t;
      }
    }
    return null;
  }, [DECLINE.map(r => ({source: r.source, flags: r.flags})),
      ACCEPT.map(r => ({source: r.source, flags: r.flags}))]).catch(() => null);
}

(async () => {
  const browser = await chromium.launch({args: ['--no-sandbox']});
  const out = {status: null, finalUrl: url, text: '', html: '', banner: null, error: null};
  try {
    const ctx = await browser.newContext({
      locale: 'fi-FI',
      timezoneId: 'Europe/Helsinki',
      viewport: {width: 1280, height: 900},
    });
    const page = await ctx.newPage();
    const resp = await page.goto(url, {waitUntil: 'domcontentloaded', timeout: 45000});
    if (resp) out.status = resp.status();
    await page.waitForLoadState('networkidle', {timeout: 15000}).catch(() => {});
    await page.waitForTimeout(waitMs);
    for (const frame of page.frames()) {
      const clicked = await declineConsent(frame);
      if (clicked) { out.banner = clicked; break; }
    }
    if (out.banner) await page.waitForTimeout(1000);
    out.finalUrl = page.url();
    out.text = await page.evaluate(() => document.body ? document.body.innerText : '');
    if (wantRaw) out.html = await page.content();
  } catch (e) {
    out.error = String(e && e.message || e).slice(0, 500);
  } finally {
    await browser.close();
  }
  process.stdout.write(JSON.stringify(out));
})();
"""


def node_env():
    env = dict(os.environ)
    # The playwright npm package is installed globally on the build environments;
    # NODE_PATH lets a bare `node -e` script require() it from anywhere.
    if "NODE_PATH" not in env:
        try:
            root = subprocess.run(["npm", "root", "-g"], capture_output=True,
                                  text=True, timeout=30).stdout.strip()
            if root:
                env["NODE_PATH"] = root
        except Exception:
            pass
    return env


def render(url, wait_ms=2500, raw=False):
    if not shutil.which("node"):
        raise SystemExit("node not found — render_page.py needs node + the "
                         "playwright package (see module docstring).")
    r = subprocess.run(["node", "-e", JS, "--", url, str(wait_ms),
                        "raw" if raw else "text"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=180, env=node_env())
    if not r.stdout.strip():
        return None, r.stderr.strip()
    try:
        return json.loads(r.stdout), r.stderr.strip()
    except json.JSONDecodeError:
        return None, (r.stdout[:300] + " / " + r.stderr.strip()[:300])


def main():
    args = list(sys.argv[1:])
    raw = "--raw" in args
    if raw:
        args.remove("--raw")
    max_chars = 40000
    if "--max-chars" in args:
        i = args.index("--max-chars")
        max_chars = int(args[i + 1])
        del args[i:i + 2]
    wait_ms = 2500
    if "--wait-ms" in args:
        i = args.index("--wait-ms")
        wait_ms = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        raise SystemExit(__doc__)
    url = args[0]

    out, err = render(url, wait_ms=wait_ms, raw=raw)
    if out is None or (out.get("error") and not out.get("text")):
        detail = (out or {}).get("error") or err
        print(f"FETCH FAILED for {url}\ndetail: {str(detail)[:500]}")
        print("Do NOT invent a reason for this. Report the failure and score 'osittain'.")
        return

    body = out["html"] if raw else out["text"]
    status = f"HTTP {out['status']}  final URL: {out['finalUrl']}" if out["status"] else \
             f"no response object  final URL: {out['finalUrl']}"
    print(f"=== {url}\n=== {status}\n=== {len(body)} chars (JS-rendered)")
    if out.get("banner"):
        print(f"=== consent banner: clicked decline-only control \"{out['banner']}\"")
    print()
    print(body[:max_chars])
    if len(body) > max_chars:
        print(f"\n[...truncated, {len(body) - max_chars} more chars. "
              f"Re-run with --max-chars to see more.]")
    if len(body) < 1500 and not raw:
        print("\n[NOTE: very little text even after JS rendering — likely a "
              "challenge/consent wall or an empty page. This is 'could not "
              "measure', not 'the site hides things'. Score 'osittain'.]")


if __name__ == "__main__":
    main()
