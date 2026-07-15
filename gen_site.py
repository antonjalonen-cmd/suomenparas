# -*- coding: utf-8 -*-
"""Suomen Paras — static site generator (demo).

Reads scores.json (produced by the scoring engine) and generates the site:
  index.html, lainavertailu/, yritys/<slug>/, kategoriat/, metodologia/

This mirrors the real pipeline: data collection -> scoring -> publish.
Run:  python gen_site.py
"""
import json, os, html

BASE = os.path.dirname(os.path.abspath(__file__))
SCORES = json.load(open(os.path.join(BASE, "scores.json"), encoding="utf-8"))
UPDATED = "15.7.2026"
SCORE_VERSION = "v1.0"

PILLAR_LABELS = {
    "digitaalinen": "Digitaalinen laatu",
    "lapinakyvyys": "Läpinäkyvyys",
    "tavoitettavuus": "Tavoitettavuus",
    "ai_laatu": "AI-laatuarvio",
}
PILLAR_W = {"digitaalinen": 30, "lapinakyvyys": 30, "tavoitettavuus": 20, "ai_laatu": 20}

def esc(s):
    return html.escape(str(s)) if s is not None else ""

# ---------------------------------------------------------------- categories
CATEGORY_GROUPS = [
    ("Talous ja raha", [
        ("Lainavertailu", "lainavertailu", True),
        ("Vakuutukset", None, False), ("Sähkösopimukset", None, False),
        ("Laajakaista", None, False), ("Puhelinliittymät", None, False),
        ("Luottokortit", None, False), ("Sijoitusalustat", None, False),
        ("Pikavipit", None, False), ("Webhotellit", None, False),
        ("VPN-palvelut", None, False), ("Pankkien asiakaspalvelu", None, False),
        ("Autovakuutukset", None, False), ("Kotivakuutukset", None, False),
        ("Matkavakuutukset", None, False), ("Lemmikkivakuutukset", None, False),
    ]),
    ("Koti ja asuminen", [
        ("Lämpöpumppuasentajat", None, False), ("Aurinkopaneeliasentajat", None, False),
        ("Putkiliikkeet", None, False), ("Sähköasentajat", None, False),
        ("Kattoremontit", None, False), ("Muuttopalvelut", None, False),
        ("Siivouspalvelut", None, False), ("Kiinteistönvälittäjät", None, False),
        ("Rakennusliikkeet", None, False), ("Maalausliikkeet", None, False),
        ("Ikkunaremontit", None, False), ("Keittiöremontit", None, False),
    ]),
    ("Auto ja liikenne", [
        ("Autokorjaamot", None, False), ("Autokatsastus", None, False),
        ("Rengasliikkeet", None, False), ("Autopesulat", None, False),
        ("Autokoulut", None, False), ("Autovuokraamot", None, False),
        ("Sähköauton latausasennukset", None, False), ("Autoliikkeet", None, False),
    ]),
    ("Terveys ja hyvinvointi", [
        ("Hammaslääkärit", None, False), ("Yksityislääkärit", None, False),
        ("Fysioterapeutit", None, False), ("Hierojat", None, False),
        ("Optikot", None, False), ("Kuntosalit", None, False),
        ("Eläinlääkärit", None, False), ("Psykoterapeutit", None, False),
        ("Jalkahoitolat", None, False), ("Kauneushoitolat", None, False),
    ]),
    ("Ravintolat ja kahvilat", [
        ("Pizzeriat", None, False), ("Sushiravintolat", None, False),
        ("Hampurilaisravintolat", None, False), ("Lounasravintolat", None, False),
        ("Kahvilat", None, False), ("Kebab-ravintolat", None, False),
        ("Fine dining", None, False), ("Brunssipaikat", None, False),
    ]),
    ("Palvelut yrityksille", [
        ("Tilitoimistot", None, False), ("Mainostoimistot", None, False),
        ("IT-tukipalvelut", None, False), ("Lakitoimistot", None, False),
        ("Käännöstoimistot", None, False), ("Rekrytointipalvelut", None, False),
    ]),
    ("Vapaa-aika ja muut", [
        ("Parturit ja kampaamot", None, False), ("Valokuvaajat", None, False),
        ("Juhlatilat", None, False), ("Catering-palvelut", None, False),
        ("Hääpalvelut", None, False), ("Ohjelmistokoulut lapsille", None, False),
        ("Kielikurssit", None, False), ("Tanssikoulut", None, False),
    ]),
]
TOTAL_CATS = sum(len(cats) for _, cats in CATEGORY_GROUPS)

# ---------------------------------------------------------------- shared css
CSS = """
:root{
  --bg:#F4F6F9; --card:#FFFFFF; --ink:#122B4A; --body:#3A4756; --mut:#68778A;
  --line:#E3E8EF; --gold:#B98A1F; --gold-soft:#FBF4DF; --gold-line:#E4C86B;
  --silver:#8C97A3; --silver-soft:#F1F4F7; --bronze:#A96F3D; --bronze-soft:#F8EFE6;
  --navy:#143A66; --navy-hover:#0E2C50; --ok:#2E7D4F; --warn:#B54708;
  --r:14px; --shadow:0 1px 2px rgba(18,43,74,.06),0 4px 16px rgba(18,43,74,.07);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Schibsted Grotesk',system-ui,sans-serif;background:var(--bg);color:var(--body);line-height:1.55;font-size:16px}
.mono{font-family:'IBM Plex Mono',monospace}
a{color:var(--navy);text-decoration:none}
a:hover{text-decoration:underline}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:4px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
/* header */
header.site{background:var(--ink);color:#fff;position:sticky;top:0;z-index:50}
header.site .wrap{display:flex;align-items:center;gap:28px;height:60px}
.brand{display:flex;align-items:baseline;gap:2px;font-weight:800;font-size:1.15rem;color:#fff;letter-spacing:-.02em}
.brand:hover{text-decoration:none}
.brand .tm{color:var(--gold-line);font-weight:800}
nav.main{display:flex;gap:20px;margin-left:auto}
nav.main a{color:#C7D3E2;font-weight:500;font-size:.92rem}
nav.main a:hover{color:#fff;text-decoration:none}
nav.main a.on{color:var(--gold-line)}
.demo-ribbon{background:var(--gold);color:#231A02;text-align:center;font-size:.8rem;font-weight:700;padding:5px 12px;letter-spacing:.02em}
/* hero */
.hero{background:linear-gradient(180deg,var(--ink) 0%,#1A3A63 100%);color:#fff;padding:56px 0 72px}
.hero h1{font-size:clamp(1.9rem,4.4vw,3.1rem);line-height:1.08;letter-spacing:-.03em;color:#fff;font-weight:800;max-width:640px}
.hero h1 em{font-style:normal;color:var(--gold-line)}
.hero p.lead{margin-top:14px;font-size:1.08rem;color:#BFCDDE;max-width:560px}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
@media(max-width:840px){.hero-grid{grid-template-columns:1fr}}
.hero-stats{display:flex;gap:28px;margin-top:28px;flex-wrap:wrap}
.hero-stat b{display:block;font-family:'IBM Plex Mono',monospace;font-size:1.35rem;color:#fff}
.hero-stat span{font-size:.82rem;color:#8FA3BB}
/* live board */
.board{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);color:var(--body);overflow:hidden}
.board-head{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid var(--line)}
.board-head .cat{font-weight:700;color:var(--ink)}
.board-head .live{display:flex;align-items:center;gap:7px;font-size:.75rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.live-dot{width:8px;height:8px;border-radius:50%;background:var(--ok);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
@media(prefers-reduced-motion:reduce){.live-dot{animation:none}}
.board-row{display:flex;align-items:center;gap:12px;padding:11px 18px;border-bottom:1px solid var(--line)}
.board-row:last-child{border-bottom:none}
.board-row .pos{font-family:'IBM Plex Mono',monospace;font-weight:600;width:22px;color:var(--mut)}
.board-row.gold .pos{color:var(--gold)}
.board-row .nm{font-weight:700;color:var(--ink)}
.board-row .sc{margin-left:auto;font-family:'IBM Plex Mono',monospace;font-weight:600;color:var(--ink)}
.board-foot{padding:12px 18px;font-size:.85rem}
.board.upcoming .board-row{opacity:.45;filter:blur(0)}
.board .coming{padding:26px 18px;text-align:center;color:var(--mut);font-size:.9rem}
/* sections */
section.band{padding:56px 0}
h2.sec{font-size:1.5rem;color:var(--ink);letter-spacing:-.02em;font-weight:800;margin-bottom:6px}
p.sec-sub{color:var(--mut);margin-bottom:26px;max-width:620px}
/* score stamp */
.stamp{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:var(--ink);color:#fff;border-radius:12px;padding:9px 13px 7px;min-width:74px}
.stamp .n{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:1.5rem;line-height:1}
.stamp .l{font-size:.56rem;letter-spacing:.14em;color:#8FA3BB;margin-top:4px;font-weight:500}
.stamp.gold{background:linear-gradient(135deg,#8A6614,#B98A1F);color:#fff}
.stamp.gold .l{color:#F3E3B3}
/* ranking cards */
.rank-card{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);padding:22px;display:grid;grid-template-columns:56px 1fr auto;gap:18px;margin-bottom:14px;border:1.5px solid transparent}
.rank-card.m1{border-color:var(--gold-line);background:linear-gradient(0deg,var(--card) 82%,var(--gold-soft) 100%)}
.rank-card.m2{border-color:#C9D2DB}
.rank-card.m3{border-color:#DDBE9C}
.medal{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:1.05rem;background:var(--silver-soft);color:var(--mut);margin-top:2px}
.m1 .medal{background:var(--gold);color:#fff;box-shadow:0 0 0 4px var(--gold-soft)}
.m2 .medal{background:var(--silver);color:#fff;box-shadow:0 0 0 4px var(--silver-soft)}
.m3 .medal{background:var(--bronze);color:#fff;box-shadow:0 0 0 4px var(--bronze-soft)}
.rank-main h3{font-size:1.18rem;color:var(--ink);letter-spacing:-.01em}
.rank-main h3 a{color:inherit}
.rank-meta{font-size:.82rem;color:var(--mut);margin-top:1px}
.badge-yl{display:inline-block;font-size:.68rem;font-weight:700;letter-spacing:.05em;background:var(--gold-soft);color:#7A5A0E;border:1px solid var(--gold-line);border-radius:99px;padding:2px 9px;vertical-align:2px;margin-left:8px}
.pillars{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 22px;margin-top:13px;max-width:520px}
.pillar{display:grid;grid-template-columns:118px 1fr 40px;align-items:center;gap:9px;font-size:.78rem;color:var(--mut)}
.bar{height:6px;border-radius:99px;background:#E9EDF3;overflow:hidden}
.bar i{display:block;height:100%;border-radius:99px;background:var(--navy)}
.m1 .bar i{background:linear-gradient(90deg,var(--navy),var(--gold))}
.pillar .v{font-family:'IBM Plex Mono',monospace;font-size:.75rem;color:var(--ink);text-align:right}
.rank-side{display:flex;flex-direction:column;align-items:flex-end;gap:10px;justify-content:space-between}
.btn{display:inline-block;background:var(--navy);color:#fff;font-weight:700;font-size:.9rem;border-radius:9px;padding:10px 18px;border:none;cursor:pointer}
.btn:hover{background:var(--navy-hover);text-decoration:none}
.btn.ghost{background:transparent;color:var(--navy);border:1.5px solid var(--line);font-weight:600}
.btn.ghost:hover{border-color:var(--navy);background:#F6F9FD}
.rank-strength{font-size:.84rem;color:var(--body);margin-top:11px}
.rank-strength b{color:var(--ok);font-weight:700}
@media(max-width:700px){.rank-card{grid-template-columns:44px 1fr}.rank-side{flex-direction:row;align-items:center;grid-column:1/-1;justify-content:flex-start}.pillars{grid-template-columns:1fr}}
/* toggle chips */
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0 22px}
.chip{font-size:.85rem;font-weight:600;border:1.5px solid var(--line);background:var(--card);color:var(--body);border-radius:99px;padding:7px 15px;cursor:pointer}
.chip:hover{border-color:var(--navy)}
.chip.on{background:var(--ink);border-color:var(--ink);color:#fff}
/* receipt */
.receipt{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);overflow:hidden;margin-bottom:22px}
.receipt-head{display:flex;justify-content:space-between;align-items:center;padding:15px 20px;background:#F8FAFC;border-bottom:1px solid var(--line)}
.receipt-head h3{font-size:1rem;color:var(--ink)}
.receipt-head .w{font-family:'IBM Plex Mono',monospace;font-size:.8rem;color:var(--mut)}
.receipt-head .sub{font-family:'IBM Plex Mono',monospace;font-weight:600;color:var(--ink);font-size:1.05rem}
table.rows{width:100%;border-collapse:collapse;font-size:.88rem}
table.rows th{text-align:left;font-size:.72rem;letter-spacing:.06em;color:var(--mut);font-weight:600;padding:9px 20px;border-bottom:1px solid var(--line);text-transform:uppercase}
table.rows td{padding:10px 20px;border-bottom:1px solid var(--line);vertical-align:top}
table.rows tr:last-child td{border-bottom:none}
td.pts,th.pts{text-align:right;font-family:'IBM Plex Mono',monospace;white-space:nowrap}
td.pts b{color:var(--ink)}
.src{font-size:.72rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.quote{font-size:.8rem;color:var(--mut);font-style:italic;margin-top:3px}
/* profile hero */
.p-hero{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);padding:28px;display:grid;grid-template-columns:1fr auto;gap:24px;margin-bottom:22px;border-top:4px solid var(--ink)}
.p-hero.m1{border-top-color:var(--gold)}
.p-hero.m2{border-top-color:var(--silver)}
.p-hero.m3{border-top-color:var(--bronze)}
.p-hero h1{font-size:1.7rem;color:var(--ink);letter-spacing:-.02em}
.p-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px 26px;margin-top:16px;font-size:.85rem}
.p-facts b{display:block;color:var(--ink);font-weight:700}
.p-facts span{color:var(--mut);font-size:.76rem}
.stamp-big{display:flex;flex-direction:column;align-items:center;gap:8px}
.stamp-big .stamp .n{font-size:2.3rem}
.stamp-big .rank-label{font-size:.8rem;font-weight:700;color:var(--gold);text-align:center}
/* two-col */
.duo{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:22px}
@media(max-width:700px){.duo{grid-template-columns:1fr}.p-hero{grid-template-columns:1fr}}
.panel{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);padding:20px}
.panel h3{font-size:.95rem;color:var(--ink);margin-bottom:11px}
.panel ul{list-style:none}
.panel li{padding:6px 0 6px 24px;position:relative;font-size:.9rem}
.panel li::before{position:absolute;left:0;font-weight:800}
.panel.plus li::before{content:"+";color:var(--ok)}
.panel.minus li::before{content:"–";color:var(--warn)}
.ai-note{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);padding:20px;margin-bottom:22px;border-left:4px solid var(--navy)}
.ai-note .tag{font-size:.68rem;font-weight:700;letter-spacing:.08em;color:var(--navy);font-family:'IBM Plex Mono',monospace}
.ai-note p{margin-top:7px;font-size:.95rem}
/* category dir */
.cat-group{margin-bottom:34px}
.cat-group h3{font-size:1.05rem;color:var(--ink);margin-bottom:13px;padding-bottom:8px;border-bottom:2px solid var(--line)}
.cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.cat-tile{background:var(--card);border-radius:10px;box-shadow:var(--shadow);padding:13px 16px;display:flex;justify-content:space-between;align-items:center;font-weight:600;color:var(--ink);font-size:.9rem}
.cat-tile:hover{text-decoration:none;outline:2px solid var(--navy)}
.cat-tile.off{opacity:.55;font-weight:500;color:var(--mut);pointer-events:none}
.cat-tile .st{font-size:.68rem;font-weight:700;font-family:'IBM Plex Mono',monospace;color:var(--mut)}
.cat-tile.live-cat .st{color:var(--ok)}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:760px){.steps{grid-template-columns:1fr}}
.step{background:var(--card);border-radius:var(--r);box-shadow:var(--shadow);padding:22px}
.step .k{font-family:'IBM Plex Mono',monospace;font-size:.75rem;color:var(--gold);font-weight:600;letter-spacing:.1em}
.step h3{color:var(--ink);font-size:1.02rem;margin:8px 0 7px}
.step p{font-size:.88rem;color:var(--mut)}
/* b2b */
.b2b{background:var(--ink);border-radius:var(--r);color:#fff;padding:30px;margin:26px 0}
.b2b h3{font-size:1.25rem;letter-spacing:-.01em}
.b2b p{color:#BFCDDE;margin:9px 0 16px;max-width:640px;font-size:.93rem}
.b2b .btn{background:var(--gold);color:#231A02}
.b2b .btn:hover{background:#D3A02F}
.b2b small{display:block;margin-top:12px;color:#8FA3BB;font-size:.78rem}
/* misc */
.crumb{font-size:.82rem;color:var(--mut);margin:22px 0 14px}
.crumb a{color:var(--mut)}
.upd{display:inline-flex;align-items:center;gap:7px;font-family:'IBM Plex Mono',monospace;font-size:.76rem;color:var(--mut);background:var(--card);border:1px solid var(--line);border-radius:99px;padding:5px 13px}
.upd::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--ok)}
.note{font-size:.8rem;color:var(--mut);background:#EEF2F7;border-radius:10px;padding:12px 16px;margin:18px 0}
footer.site{background:var(--ink);color:#8FA3BB;padding:36px 0;margin-top:64px;font-size:.82rem}
footer.site .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:32px}
@media(max-width:700px){footer.site .cols{grid-template-columns:1fr}}
footer.site a{color:#C7D3E2}
footer.site h4{color:#fff;font-size:.85rem;margin-bottom:9px}
footer.site .fine{margin-top:26px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);font-size:.75rem;line-height:1.6}
.pageh{padding:40px 0 8px}
.pageh h1{font-size:clamp(1.6rem,3.5vw,2.3rem);color:var(--ink);letter-spacing:-.02em;line-height:1.15}
.pageh p.lead{color:var(--mut);margin-top:10px;max-width:640px;font-size:1rem}
.meta-row{display:flex;gap:12px;align-items:center;margin-top:16px;flex-wrap:wrap}
.count-pill{font-family:'IBM Plex Mono',monospace;font-size:.76rem;color:var(--mut)}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

def page(title, desc, body, root="", active=""):
    def on(k):
        return ' class="on"' if k == active else ""
    return f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{FONTS}
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body>
<div class="demo-ribbon">DEMO — Suomen Paras -konseptin esittelyversio · Lainavertailu-kategoria toimii oikealla datalla</div>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{root}">Suomen&nbsp;Paras<span class="tm">.</span></a>
    <nav class="main">
      <a href="{root}lainavertailu/"{on('laina')}>Lainavertailu</a>
      <a href="{root}kategoriat/"{on('kategoriat')}>Kaikki kategoriat</a>
      <a href="{root}metodologia/"{on('metodologia')}>Näin pisteytämme</a>
    </nav>
  </div>
</header>
{body}
<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>Suomen Paras</h4>
        <p>Suomen läpinäkyvin vertailupalvelu. Pisteytämme yritykset mitattavalla datalla — emme mielipiteillä. Sijoituksia ei voi ostaa.</p>
      </div>
      <div>
        <h4>Palvelu</h4>
        <p><a href="{root}lainavertailu/">Lainavertailu</a><br><a href="{root}kategoriat/">Kaikki kategoriat</a><br><a href="{root}metodologia/">Pisteytysmetodologia</a></p>
      </div>
      <div>
        <h4>Score {SCORE_VERSION}</h4>
        <p class="mono">Päivitetty {UPDATED}<br>{len(SCORES)} palvelua pisteytetty</p>
      </div>
    </div>
    <p class="fine">Tämä on Suomen Paras -palvelun esittelyversio (demo). Pisteet perustuvat julkisiin lähteisiin {UPDATED}: yritysten omat verkkosivut, YTJ/PRH-avoin data ja Lighthouse-mittaukset. AI-arviot on tuottanut Claude Haiku 4.5. Emme anna sijoitus-, laina- tai muuta talousneuvontaa — vertailu on informatiivinen. Sivusto voi tulevaisuudessa sisältää affiliate-linkkejä, jotka eivät koskaan vaikuta sijoituksiin. Virheen huomatessasi: korjaamme datan seuraavassa päivityksessä.</p>
  </div>
</footer>
</body>
</html>"""

# ---------------------------------------------------------------- components
def stamp(score, gold=False, label="SP-SCORE"):
    cls = "stamp gold" if gold else "stamp"
    n = f"{score:.1f}".replace(".", ",") if score is not None else "–"
    return f'<div class="{cls}"><span class="n">{n}</span><span class="l">{label}</span></div>'

def pillar_bars(c):
    out = ['<div class="pillars">']
    for key in ["digitaalinen", "lapinakyvyys", "tavoitettavuus", "ai_laatu"]:
        v = c["pillars"][key]
        vv = 0 if v is None else v
        disp = f"{v:.0f}" if v is not None else "–"
        out.append(f'<div class="pillar"><span>{PILLAR_LABELS[key]}</span><span class="bar"><i style="width:{vv}%"></i></span><span class="v">{disp}</span></div>')
    out.append("</div>")
    return "".join(out)

def rank_card(c, pos, root):
    m = f"m{pos}" if pos <= 3 else ""
    top_strength = c["extract"]["vahvuudet"][0] if c["extract"]["vahvuudet"] else ""
    dataattrs = " ".join(
        f'data-{k}="{(c["pillars"][k] if c["pillars"][k] is not None else 0)}"'
        for k in ["digitaalinen", "lapinakyvyys", "tavoitettavuus", "ai_laatu"]
    )
    ylabel = '<span class="badge-yl">SUOMEN PARAS 2026</span>' if pos == 1 else ""
    return f"""
<article class="rank-card {m}" data-score="{c['score'] or 0}" {dataattrs}>
  <div class="medal">{pos}</div>
  <div class="rank-main">
    <h3><a href="{root}yritys/{c['slug']}/">{esc(c['nimi'])}</a>{ylabel}</h3>
    <p class="rank-meta">{esc(c['domain'])} · {esc(c['omistaja'])}</p>
    {pillar_bars(c)}
    <p class="rank-strength"><b>+</b> {esc(top_strength)}</p>
  </div>
  <div class="rank-side">
    {stamp(c['score'], gold=(pos == 1))}
    <div style="display:flex;flex-direction:column;gap:8px;align-items:flex-end">
      <a class="btn" href="https://{c['domain']}" rel="nofollow noopener" target="_blank">Siirry palveluun</a>
      <a class="btn ghost" href="{root}yritys/{c['slug']}/">Näin pisteet syntyvät</a>
    </div>
  </div>
</article>"""

def receipt(title, weight, subtotal, rows, has_quote=False):
    trs = []
    for r in rows:
        q = f'<div class="quote">”{esc(r["quote"])}”</div>' if r.get("quote") else ""
        if "pisteet_max" in r:
            pts, maxp = r["pisteet"], r["pisteet_max"]
            disp = str(pts)
        else:
            # weighted 0-100 metric: show contribution toward the pillar
            maxp = r["paino"]
            disp = f'{r["pisteet"] * r["paino"] / 100:.1f}'.replace(".", ",")
        trs.append(
            f'<tr><td>{esc(r["mittari"])}{q}</td>'
            f'<td>{esc(r["arvo"])}</td>'
            f'<td class="src">{esc(r["lahde"])}</td>'
            f'<td class="pts"><b>{disp}</b> / {maxp}</td></tr>'
        )
    sub = f"{subtotal:.1f}".replace(".", ",") if subtotal is not None else "–"
    return f"""
<div class="receipt">
  <div class="receipt-head">
    <h3>{esc(title)} <span class="w">· paino {weight} %</span></h3>
    <span class="sub">{sub} / 100</span>
  </div>
  <table class="rows">
    <thead><tr><th>Mittari</th><th>Mitattu arvo</th><th>Lähde</th><th class="pts">Pisteet</th></tr></thead>
    <tbody>{''.join(trs)}</tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- pages
def build_index():
    top = SCORES[:5]
    rows = []
    for i, c in enumerate(top, 1):
        g = " gold" if i == 1 else ""
        sc = f"{c['score']:.1f}".replace(".", ",")
        rows.append(f'<div class="board-row{g}"><span class="pos">{i}</span><span class="nm">{esc(c["nimi"])}</span><span class="sc">{sc}</span></div>')

    steps = """
<div class="steps">
  <div class="step"><span class="k">01 · KERUU</span><h3>Data kerätään automaattisesti</h3><p>Julkiset lähteet: yrityksen oma verkkosivu, YTJ/PRH-rekisterit ja tekniset mittaukset (Lighthouse). Sama prosessi jokaiselle — kukaan ei täytä lomakkeita.</p></div>
  <div class="step"><span class="k">02 · PISTEYTYS</span><h3>Sama kaava kaikille</h3><p>Suomen Paras Score {v} laskee neljä pilaria dokumentoiduilla painoilla. Kaava on julkinen ja deterministinen: sama data antaa aina saman tuloksen.</p></div>
  <div class="step"><span class="k">03 · KUITTI</span><h3>Jokainen piste perustellaan</h3><p>Jokaisen yrityksen profiililta näet mittari mittarilta, mistä pisteet tulevat — lähteineen ja sitaatteineen. Sijoitusta ei voi ostaa.</p></div>
</div>""".replace("{v}", SCORE_VERSION)

    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Suomen kaikki vertailut.<br>Yksi läpinäkyvä <em>pisteytys</em>.</h1>
      <p class="lead">Vertailemme suomalaiset palvelut mitattavalla datalla, samalla kaavalla ja julkisin perustein. Näet jokaisen pisteen alkuperän.</p>
      <div class="hero-stats">
        <div class="hero-stat"><b>{len(SCORES)}</b><span>palvelua pisteytetty</span></div>
        <div class="hero-stat"><b>{TOTAL_CATS}</b><span>kategoriaa suunnitteilla</span></div>
        <div class="hero-stat"><b>26</b><span>mittaria / yritys</span></div>
      </div>
    </div>
    <div class="board" id="liveboard">
      <div class="board-head"><span class="cat" id="lb-cat">Lainavertailu</span><span class="live"><span class="live-dot"></span><span id="lb-status">TOP 5 · {UPDATED}</span></span></div>
      <div id="lb-body">{''.join(rows)}</div>
      <div class="board-foot" id="lb-foot"><a href="lainavertailu/">Koko vertailu ja pisteiden perustelut →</a></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2 class="sec">Miten Suomen Paras toimii</h2>
    <p class="sec-sub">Perinteiset vertailusivut myyvät sijoituksia. Me myymme vain yhtä asiaa: läpinäkyvää dataa.</p>
    {steps}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <h2 class="sec">Kategoriat</h2>
    <p class="sec-sub">Ensimmäisenä avattu: lainavertailu. Uusia kategorioita avataan kuukausittain — tavoite on kattaa kaikki suomalaiset palvelut.</p>
    <div class="cat-grid">
      <a class="cat-tile live-cat" href="lainavertailu/">Lainavertailu <span class="st">LIVE</span></a>
      <span class="cat-tile off">Sähkösopimukset <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Puhelinliittymät <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Laajakaista <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Vakuutukset <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Luottokortit <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Autokorjaamot <span class="st">TULOSSA</span></span>
      <a class="cat-tile" href="kategoriat/" style="justify-content:center;background:var(--ink);color:#fff">Kaikki {TOTAL_CATS} kategoriaa →</a>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="b2b">
      <h3>Yrittäjä — haluatko nousta listalla?</h3>
      <p>Sijoitusta ei voi ostaa meiltä — eikä keneltäkään. Mutta voit pyytää maksullisen analyysin, joka näyttää täsmälleen mitkä mittarit painavat sijoitustasi alas ja miten korjaat ne. Kun mittarit paranevat, sijoitus nousee seuraavassa päivityksessä — ansaitusti.</p>
      <a class="btn" href="mailto:anton@antonjalonen.fi?subject=Suomen%20Paras%20-analyysi">Pyydä analyysi yrityksellesi</a>
      <small>Analyysi ei koskaan muuta pisteitä suoraan. Premium-näkyvyys ei vaikuta sijoituksiin.</small>
    </div>
  </div>
</section>

"""
    return page("Suomen Paras — Suomen läpinäkyvin vertailupalvelu",
                "Pisteytämme suomalaiset palvelut mitattavalla datalla. Lainavertailu, sähkösopimukset ja sadat muut kategoriat yhdellä läpinäkyvällä Scorella.",
                body, root="", active="")

def build_lainavertailu():
    cards = "".join(rank_card(c, i, "../") for i, c in enumerate(SCORES, 1))
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Lainavertailu</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Suomen paras lainavertailu 2026</h1>
    <p class="lead">Pisteytimme {len(SCORES)} suomalaista lainanvälityspalvelua 26 mittarilla: tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Sama kaava kaikille — katso jokaisen pisteen perustelu.</p>
    <div class="meta-row">
      <span class="upd">Päivitetty {UPDATED} · Score {SCORE_VERSION}</span>
      <a class="count-pill" href="../metodologia/">Miten pisteet lasketaan →</a>
    </div>
  </div>

  <div class="chips" role="tablist" aria-label="Järjestä ranking">
    <button class="chip on" data-key="score">Paras kokonaisuus</button>
    <button class="chip" data-key="lapinakyvyys">Läpinäkyvin</button>
    <button class="chip" data-key="digitaalinen">Paras digitaalinen laatu</button>
    <button class="chip" data-key="tavoitettavuus">Paras tavoitettavuus</button>
  </div>

  <div id="ranking">{cards}</div>

  <p class="note"><b>Huomio:</b> Neljä listan palveluista (Rahalaitos, Omalaina, Sambla ja Rahoitu.fi) kuuluu samaan konserniin (Sambla Group Oy), ja Zmarta sekä Freedom Rahoitus ovat samaa yhtiötä. Näytämme omistajan jokaisen palvelun kohdalla — brändejä vertaillessa kannattaa tietää kuka niiden takana on.</p>
  <p class="note">Emme anna laina- tai talousneuvontaa. Vertailu kuvaa palveluiden verkkosivujen mitattavia ominaisuuksia, ei lainatarjousten paremmuutta — lopullinen korko on aina henkilökohtainen. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin.</p>

  <div class="b2b">
    <h3>Oletko listalla — ja haluaisit korkeammalle?</h3>
    <p>Jokainen menetetty piste on dokumentoitu profiilissasi. Maksullinen analyysimme priorisoi korjaukset vaikutuksen mukaan: mitkä toimet nostavat pisteitäsi eniten seuraavaan päivitykseen mennessä.</p>
    <a class="btn" href="mailto:anton@antonjalonen.fi?subject=Suomen%20Paras%20-analyysi">Pyydä analyysi</a>
    <small>Sijoitusta ei voi ostaa. Analyysi kertoo miten se ansaitaan.</small>
  </div>
</div>

<script>
(function(){{
  var chips = document.querySelectorAll('.chip');
  var wrap = document.getElementById('ranking');
  chips.forEach(function(ch){{
    ch.addEventListener('click', function(){{
      chips.forEach(function(c){{ c.classList.remove('on'); }});
      ch.classList.add('on');
      var key = ch.dataset.key;
      var cards = Array.prototype.slice.call(wrap.children);
      cards.sort(function(a, b){{ return parseFloat(b.dataset[key]) - parseFloat(a.dataset[key]); }});
      cards.forEach(function(card, idx){{
        var pos = idx + 1;
        card.className = 'rank-card' + (pos <= 3 ? ' m' + pos : '');
        card.querySelector('.medal').textContent = pos;
        var badge = card.querySelector('.badge-yl');
        if (badge) badge.remove();
        if (pos === 1 && key === 'score') {{
          card.querySelector('h3').insertAdjacentHTML('beforeend', '<span class="badge-yl">SUOMEN PARAS 2026</span>');
        }}
        wrap.appendChild(card);
      }});
    }});
  }});
}})();
</script>"""
    return page("Suomen paras lainavertailu 2026 — kaikki lainanvälittäjät pisteytettynä | Suomen Paras",
                "9 suomalaista lainanvälityspalvelua pisteytetty 26 mittarilla. Läpinäkyvä Score: katso mistä jokainen piste tulee.",
                body, root="../", active="laina")

def build_profile(c, pos):
    e = c["extract"]
    m = f"m{pos}" if pos <= 3 else ""
    rank_label = {1: "🏆 Sija 1 — Suomen Paras 2026", 2: "Sija 2 / " + str(len(SCORES)), 3: "Sija 3 / " + str(len(SCORES))}.get(pos, f"Sija {pos} / {len(SCORES)}")

    # receipts with evidence quotes attached to relevant rows
    b = c["breakdown"]
    lap_rows = []
    for r in b["lapinakyvyys"]["rivit"]:
        r = dict(r)
        if "korkoesimerkki" in r["mittari"].lower() and e["evidence"].get("korkoesimerkki"):
            r["quote"] = e["evidence"]["korkoesimerkki"]
        if "kumppani" in r["mittari"].lower() and e["evidence"].get("kumppanit"):
            r["quote"] = e["evidence"]["kumppanit"]
        if "arviol" in r["mittari"].lower() and e["evidence"].get("asiakasarvio"):
            r["quote"] = e["evidence"]["asiakasarvio"]
        lap_rows.append(r)

    dig_rows = b["digitaalinen"]["rivit"]
    receipts = ""
    if dig_rows:
        receipts += receipt("Digitaalinen laatu", 30, c["pillars"]["digitaalinen"], dig_rows)
    else:
        receipts += '<div class="note">Tekninen mittaus (Lighthouse) ajetaan seuraavassa päivityksessä.</div>'
    receipts += receipt("Läpinäkyvyys", 30, c["pillars"]["lapinakyvyys"], lap_rows)
    receipts += receipt("Tavoitettavuus", 20, c["pillars"]["tavoitettavuus"], b["tavoitettavuus"]["rivit"])
    receipts += receipt("AI-laatuarvio", 20, c["pillars"]["ai_laatu"], b["ai_laatu"]["rivit"])

    vah = "".join(f"<li>{esc(v)}</li>" for v in e["vahvuudet"])
    keh = "".join(f"<li>{esc(v)}</li>" for v in e["kehityskohteet"])

    lh = c.get("lh") or {}
    lcp = f'{lh["lcp_ms"]/1000:.1f} s'.replace(".", ",") if lh.get("lcp_ms") else "–"

    facts = f"""
    <div class="p-facts">
      <div><span>Verkkosivu</span><b>{esc(c['domain'])}</b></div>
      <div><span>Omistaja (YTJ)</span><b>{esc(c['omistaja'])}</b></div>
      <div><span>Y-tunnus</span><b class="mono">{esc(c['y_tunnus'])}</b></div>
      <div><span>Yhtiö rekisteröity</span><b>{esc(c['rekisteroity'] or '–')}</b></div>
      <div><span>Lainasummat</span><b>{esc((f"{e['lainasumma_min_eur']:,}".replace(',', ' ') + '–' + f"{e['lainasumma_max_eur']:,}".replace(',', ' ') + ' €') if e.get('lainasumma_min_eur') else 'Ei kerrottu')}</b></div>
      <div><span>Kumppanipankkeja</span><b>{esc((str(e['kumppanipankkien_maara']) + ' kpl') if e.get('kumppanipankkien_maara') else 'Ei kerrottu')}</b></div>
      <div><span>LCP (mobiili)</span><b class="mono">{lcp}</b></div>
    </div>"""

    total_formula = ""
    if c["score"] is not None:
        p = c["pillars"]
        total_formula = f"""
  <div class="receipt">
    <div class="receipt-head"><h3>Kokonaispisteet <span class="w">· painotettu summa</span></h3><span class="sub">{f"{c['score']:.1f}".replace('.', ',')} / 100</span></div>
    <table class="rows"><tbody>
      <tr><td>Digitaalinen laatu</td><td class="src">30 % × {str(p['digitaalinen']).replace('.', ',')}</td><td class="pts"><b>{f"{0.30*p['digitaalinen']:.1f}".replace('.', ',')}</b></td></tr>
      <tr><td>Läpinäkyvyys</td><td class="src">30 % × {str(p['lapinakyvyys']).replace('.', ',')}</td><td class="pts"><b>{f"{0.30*p['lapinakyvyys']:.1f}".replace('.', ',')}</b></td></tr>
      <tr><td>Tavoitettavuus</td><td class="src">20 % × {str(p['tavoitettavuus']).replace('.', ',')}</td><td class="pts"><b>{f"{0.20*p['tavoitettavuus']:.1f}".replace('.', ',')}</b></td></tr>
      <tr><td>AI-laatuarvio</td><td class="src">20 % × {str(p['ai_laatu']).replace('.', ',')}</td><td class="pts"><b>{f"{0.20*p['ai_laatu']:.1f}".replace('.', ',')}</b></td></tr>
    </tbody></table>
  </div>"""

    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../../">Etusivu</a> › <a href="../../lainavertailu/">Lainavertailu</a> › <b>{esc(c['nimi'])}</b></p>

  <div class="p-hero {m}">
    <div>
      <h1>{esc(c['nimi'])}</h1>
      <p class="rank-meta" style="margin-top:4px">{esc(rank_label)} · Lainavertailu · Päivitetty {UPDATED}</p>
      {facts}
    </div>
    <div class="stamp-big">
      {stamp(c['score'], gold=(pos == 1))}
      <a class="btn" href="https://{c['domain']}" rel="nofollow noopener" target="_blank">Siirry palveluun</a>
    </div>
  </div>

  <div class="ai-note">
    <span class="tag">AI-YHTEENVETO · CLAUDE HAIKU 4.5 · {UPDATED}</span>
    <p>{esc(e['yhteenveto'])}</p>
  </div>

  <div class="duo">
    <div class="panel plus"><h3>Vahvuudet</h3><ul>{vah}</ul></div>
    <div class="panel minus"><h3>Kehityskohteet</h3><ul>{keh}</ul></div>
  </div>

  <h2 class="sec" style="margin-top:36px">Näin pisteet lasketaan</h2>
  <p class="sec-sub">Jokainen rivi on mitattu {UPDATED} julkisista lähteistä. Sama kaava kaikille — <a href="../../metodologia/">lue koko metodologia</a>.</p>
  {total_formula}
  {receipts}

  <div class="b2b">
    <h3>Onko tämä sinun yrityksesi?</h3>
    <p>Yllä näkyy täsmälleen mistä pisteesi tulevat — ja mihin niitä jää saamatta. Maksullinen analyysimme priorisoi korjaukset: mitkä toimenpiteet nostavat Scorea eniten, ja miten ne toteutetaan. Kun data paranee, sijoitus nousee seuraavassa päivityksessä.</p>
    <a class="btn" href="mailto:anton@antonjalonen.fi?subject=Suomen%20Paras%20-analyysi%20({esc(c['nimi'])})">Pyydä analyysi — {esc(c['nimi'])}</a>
    <small>Analyysi ei muuta pisteitä. Vain mittareiden parantaminen muuttaa.</small>
  </div>
</div>"""
    return page(f"{c['nimi']} — Suomen Paras Score {f'{c['score']:.1f}'.replace('.', ',') if c['score'] else '–'}/100 | Lainavertailu",
                f"{c['nimi']}: pisteet, vahvuudet ja kehityskohteet. Katso mistä jokainen piste tulee — mittari mittarilta.",
                body, root="../../", active="laina")

def build_kategoriat():
    groups = []
    for gname, cats in CATEGORY_GROUPS:
        tiles = []
        for cname, slug, live in cats:
            if live:
                tiles.append(f'<a class="cat-tile live-cat" href="../{slug}/">{esc(cname)} <span class="st">LIVE</span></a>')
            else:
                tiles.append(f'<span class="cat-tile off">{esc(cname)} <span class="st">TULOSSA</span></span>')
        groups.append(f'<div class="cat-group"><h3>{esc(gname)}</h3><div class="cat-grid">{"".join(tiles)}</div></div>')
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Kategoriat</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Kaikki kategoriat</h1>
    <p class="lead">{TOTAL_CATS} kategoriaa suunnitteilla — jokainen pisteytetään samalla julkisella Suomen Paras Score -kaavalla. Ensimmäisenä avattu lainavertailu; uusia avataan kuukausittain.</p>
    <div class="meta-row"><span class="upd">1 kategoria live · {TOTAL_CATS - 1} tulossa</span></div>
  </div>
  {''.join(groups)}
</div>"""
    return page("Kaikki kategoriat | Suomen Paras",
                f"{TOTAL_CATS} palvelukategoriaa yhdellä läpinäkyvällä pisteytyksellä.",
                body, root="../", active="kategoriat")

def build_metodologia():
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Metodologia</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Näin Suomen Paras Score lasketaan</h1>
    <p class="lead">Score {SCORE_VERSION} on deterministinen: sama julkinen data tuottaa aina saman tuloksen. Tällä sivulla on koko kaava — koska läpinäkyvyys ei ole markkinointisana, se on tuote.</p>
    <div class="meta-row"><span class="upd">Score {SCORE_VERSION} · voimassa {UPDATED} alkaen</span></div>
  </div>

  <div class="receipt">
    <div class="receipt-head"><h3>Pilarit ja painot</h3><span class="sub">100 %</span></div>
    <table class="rows">
      <thead><tr><th>Pilari</th><th>Mitä mittaa</th><th>Lähde</th><th class="pts">Paino</th></tr></thead>
      <tbody>
        <tr><td><b>Digitaalinen laatu</b></td><td>Suorituskyky (40), saavutettavuus (30), SEO (15), tekniset käytännöt (15) — mobiili</td><td class="src">Lighthouse 12</td><td class="pts"><b>30 %</b></td></tr>
        <tr><td><b>Läpinäkyvyys</b></td><td>Lakisääteinen korkoesimerkki (30), korkoväli (15), lainaehdot (15), Y-tunnus (10), kumppanimäärä (15), riippumaton arviolähde (15)</td><td class="src">Verkkosivu + AI-ekstraktio</td><td class="pts"><b>30 %</b></td></tr>
        <tr><td><b>Tavoitettavuus</b></td><td>Puhelin (30), sähköposti (15), chat (15), aukioloajat (15), UKK (15), mobiilisovellus (10)</td><td class="src">Verkkosivu + AI-ekstraktio</td><td class="pts"><b>20 %</b></td></tr>
        <tr><td><b>AI-laatuarvio</b></td><td>Tietojen selkeys, hintatietojen löydettävyys, sisällön kattavuus (0–100)</td><td class="src">Claude Haiku 4.5</td><td class="pts"><b>20 %</b></td></tr>
      </tbody>
    </table>
  </div>

  <div class="steps" style="margin-top:26px">
    <div class="step"><span class="k">DATALÄHTEET</span><h3>Vain julkista dataa</h3><p>Yrityksen oma verkkosivu, YTJ/PRH-avoin data ja tekniset mittaukset. Emme käytä ostettuja arvosteluja emmekä yritysten itse toimittamia lukuja.</p></div>
    <div class="step"><span class="k">PÄIVITYSSYKLI</span><h3>Rullaava uudelleenmittaus</h3><p>Tekniset mittarit ja sivusisältö mitataan uudelleen kuukausittain, rekisteritiedot neljännesvuosittain. Jokaisella sivulla lukee milloin data on mitattu.</p></div>
    <div class="step"><span class="k">VERSIOINTI</span><h3>Kaava on versioitu</h3><p>Kun painoja tai mittareita muutetaan, versionumero kasvaa ja muutos dokumentoidaan. Vanhoja tuloksia ei muokata takautuvasti.</p></div>
  </div>

  <h2 class="sec" style="margin-top:44px">Riippumattomuus</h2>
  <div class="panel" style="margin-top:12px">
    <ul style="list-style:disc;padding-left:20px">
      <li style="padding-left:0"><b>Sijoitusta ei voi ostaa.</b> Mikään maksu ei muuta pisteitä tai järjestystä — ei mainonta, ei kumppanuus, ei analyysipalvelu.</li>
      <li style="padding-left:0"><b>Affiliate-linkit eivät vaikuta pisteisiin.</b> Voimme saada komission, kun siirryt palveluun linkistämme. Komissio ei ole mittari.</li>
      <li style="padding-left:0"><b>Analyysipalvelu neuvoo, ei nosta.</b> Yritys voi ostaa analyysin siitä, mitkä mittarit painavat sen sijoitusta — pisteet nousevat vasta kun mittarit oikeasti paranevat.</li>
      <li style="padding-left:0"><b>AI-arviot ovat toistettavia.</b> Sama malli (Claude Haiku 4.5), sama ohjeistus ja sama data jokaiselle yritykselle samassa päivityksessä.</li>
      <li style="padding-left:0"><b>Virheet korjataan.</b> Jos yritys osoittaa mittausvirheen, korjaamme datan seuraavassa päivityksessä ja merkitsemme korjauksen.</li>
    </ul>
  </div>

  <div class="note" style="margin-top:26px"><b>Demo-huomautus:</b> Tämä on konseptin esittelyversio. Lainavertailun data on kerätty oikeista julkisista lähteistä {UPDATED}, mutta mittaristo on suppeampi kuin tuotantoversiossa (26 / ~200 mittaria) ja kattaa vain palveluiden julkiset verkkosivut — ei esimerkiksi todellisia lainatarjouksia.</div>
</div>"""
    return page("Metodologia — näin Suomen Paras Score lasketaan | Suomen Paras",
                "Suomen Paras Score on julkinen ja deterministinen: pilarit, painot, lähteet ja riippumattomuusperiaatteet.",
                body, root="../", active="metodologia")

# ---------------------------------------------------------------- write
def w(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

def main():
    w("assets/style.css", CSS)
    w("index.html", build_index())
    w("lainavertailu/index.html", build_lainavertailu())
    w("kategoriat/index.html", build_kategoriat())
    w("metodologia/index.html", build_metodologia())
    for i, c in enumerate(SCORES, 1):
        w(f"yritys/{c['slug']}/index.html", build_profile(c, i))
    print("OK —", 4 + len(SCORES), "pages")

if __name__ == "__main__":
    main()
