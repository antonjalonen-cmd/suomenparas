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
  --bg:#EAF2FE; --card:#FFFFFF; --ink:#14213F; --body:#2C3A5C; --mut:#5D6E92;
  --blue:#2E6BD6; --blue-deep:#1E4FA8; --blue-soft:#D9E7FC;
  --line:#C9D9F2; --gold:#F7B500; --gold-deep:#D89B00; --gold-soft:#FFF3CE; --gold-line:#FFC61A;
  --silver:#93A2BC; --silver-soft:#EEF3FA; --bronze:#C08447; --bronze-soft:#F9EFE2;
  --ok:#1F9D55; --warn:#C2410C; --cream:#FFF9EC;
  --r:20px;
  --shadow:0 2px 0 rgba(20,33,63,.06),0 8px 20px rgba(30,79,168,.10);
  --pop:0 4px 0 rgba(20,33,63,.16);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Nunito',system-ui,sans-serif;background:var(--bg);color:var(--body);line-height:1.6;font-size:16.5px}
h1,h2,h3,h4,.brand{font-family:'Fredoka',sans-serif}
.mono{font-family:'IBM Plex Mono',monospace}
a{color:var(--blue-deep);text-decoration:none}
a:hover{text-decoration:underline}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:6px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
/* header */
header.site{background:linear-gradient(180deg,var(--blue) 0%,var(--blue-deep) 100%);color:#fff;position:sticky;top:0;z-index:50;border-bottom:3px solid var(--ink)}
header.site .wrap{display:flex;align-items:center;gap:24px;height:66px}
.brand{display:flex;align-items:center;gap:11px;font-weight:600;font-size:1.28rem;color:#fff;letter-spacing:.01em}
.brand:hover{text-decoration:none}
.brand img{width:46px;height:46px;filter:drop-shadow(0 2px 3px rgba(0,0,0,.25));transition:transform .25s cubic-bezier(.3,1.6,.4,1)}
.brand:hover img{transform:rotate(-8deg) scale(1.08)}
.brand .tm{color:var(--gold-line)}
nav.main{display:flex;gap:22px;margin-left:auto}
nav.main a{color:#DCE8FC;font-weight:800;font-size:.95rem}
nav.main a:hover{color:#fff;text-decoration:none}
nav.main a.on{color:var(--gold-line)}
.demo-ribbon{background:var(--ink);color:var(--gold-line);text-align:center;font-size:.8rem;font-weight:800;padding:6px 12px;letter-spacing:.03em}
/* hero */
.hero{background:linear-gradient(170deg,var(--blue) 0%,var(--blue-deep) 78%,#173F87 100%);color:#fff;padding:58px 0 74px;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;width:1700px;height:1700px;left:50%;top:-560px;transform:translateX(-50%);background:repeating-conic-gradient(rgba(255,255,255,.55) 0 9deg,transparent 9deg 18deg);border-radius:50%;pointer-events:none;opacity:.1;animation:spin 140s linear infinite;-webkit-mask-image:radial-gradient(closest-side at 50% 42%,#000 34%,transparent 74%);mask-image:radial-gradient(closest-side at 50% 42%,#000 34%,transparent 74%)}
.hero .wrap{position:relative}
.kicker{font-family:'IBM Plex Mono',monospace;font-size:.7rem;letter-spacing:.16em;color:var(--gold-line);margin-bottom:16px;font-weight:600}
.hero h1{font-size:clamp(2.1rem,4.8vw,3.4rem);line-height:1.06;letter-spacing:.005em;color:#fff;font-weight:600;max-width:660px}
.hero h1 em{font-style:normal;color:var(--gold-line)}
.hero p.lead{margin-top:16px;font-size:1.1rem;color:#D6E4FB;max-width:560px;font-weight:600}
.hero-logo{width:132px;height:132px;margin-bottom:18px;filter:drop-shadow(0 8px 18px rgba(10,25,60,.4));animation:bounceIn .8s cubic-bezier(.3,1.5,.4,1) both}
@keyframes bounceIn{from{opacity:0;transform:scale(.5) rotate(-12deg)}to{opacity:1;transform:none}}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes spin{to{transform:translateX(-50%) rotate(360deg)}}
.hero .kicker{animation:fadeUp .65s cubic-bezier(.2,.7,.2,1) .1s both}
.hero h1{animation:fadeUp .65s cubic-bezier(.2,.7,.2,1) .17s both}
.hero p.lead{animation:fadeUp .65s cubic-bezier(.2,.7,.2,1) .25s both}
.hero .hero-stats{animation:fadeUp .65s cubic-bezier(.2,.7,.2,1) .33s both}
.board-wrap{position:relative;animation:fadeUp .7s cubic-bezier(.2,.7,.2,1) .4s both}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
@media(max-width:840px){.hero-grid{grid-template-columns:1fr}}
.hero-stats{display:flex;gap:26px;margin-top:26px;flex-wrap:wrap}
.hero-stat b{display:block;font-family:'Fredoka',sans-serif;font-size:1.5rem;color:var(--gold-line);font-weight:600}
.hero-stat span{font-size:.84rem;color:#AFC6EC;font-weight:600}
/* live board */
.board{background:var(--card);border-radius:var(--r);border:3px solid var(--ink);box-shadow:0 6px 0 rgba(10,22,50,.35);color:var(--body);overflow:hidden}
.board-head{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:2px solid var(--line);background:var(--cream)}
.board-head .cat{font-family:'Fredoka',sans-serif;font-weight:600;color:var(--ink);font-size:1.05rem}
.board-head .live{display:flex;align-items:center;gap:7px;font-size:.72rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.live-dot{width:9px;height:9px;border-radius:50%;background:var(--ok);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
@media(prefers-reduced-motion:reduce){.live-dot{animation:none}}
.board-row{display:flex;align-items:center;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line)}
.board-row:last-child{border-bottom:none}
.board-row .pos{font-family:'Fredoka',sans-serif;font-weight:600;width:24px;color:var(--mut)}
.board-row.gold{background:var(--gold-soft)}
.board-row.gold .pos{color:var(--gold-deep)}
.board-row .nm{font-weight:800;color:var(--ink)}
.board-row .dots{flex:1;border-bottom:2px dotted #BFD1EC;height:2px;margin:0 6px;transform:translateY(5px)}
.board-row .sc{font-family:'Fredoka',sans-serif;font-weight:600;color:var(--ink)}
.board-foot{padding:12px 18px;font-size:.88rem;font-weight:700}
/* sections */
section.band{padding:56px 0}
h2.sec{font-size:1.65rem;color:var(--ink);font-weight:600;margin-bottom:6px}
h2.sec::before{content:"";display:inline-block;width:22px;height:5px;border-radius:3px;background:linear-gradient(90deg,var(--gold),var(--gold-line));margin-right:11px;vertical-align:.2em}
p.sec-sub{color:var(--mut);margin-bottom:26px;max-width:640px;font-weight:600}
/* score stamp */
.stamp{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:var(--blue-deep);color:#fff;border-radius:16px;border:2.5px solid var(--ink);box-shadow:var(--pop);padding:9px 14px 7px;min-width:80px}
.stamp .n{font-family:'Fredoka',sans-serif;font-weight:600;font-size:1.6rem;line-height:1}
.stamp .l{font-size:.56rem;letter-spacing:.13em;color:#B9CFF3;margin-top:4px;font-weight:700;font-family:'IBM Plex Mono',monospace}
.stamp.gold{background:linear-gradient(160deg,var(--gold-line),var(--gold));color:var(--ink)}
.stamp.gold .l{color:#7A5A0E}
/* ranking cards */
.rank-card{background:var(--card);border-radius:var(--r);border:2.5px solid var(--line);box-shadow:var(--shadow);padding:22px;display:grid;grid-template-columns:56px 1fr auto;gap:18px;margin-bottom:16px}
.rank-card.m1{border-color:var(--gold);box-shadow:0 5px 0 rgba(216,155,0,.25),0 10px 26px rgba(30,79,168,.12);background:linear-gradient(0deg,var(--card) 84%,var(--gold-soft) 100%)}
.rank-card.m2{border-color:var(--silver)}
.rank-card.m3{border-color:var(--bronze)}
.medal{width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fredoka',sans-serif;font-weight:600;font-size:1.15rem;background:var(--silver-soft);color:var(--mut);margin-top:2px;border:2px solid transparent;position:relative}
.m1 .medal{background:var(--gold-line);color:var(--ink);border-color:var(--ink);box-shadow:0 0 0 4px var(--gold-soft)}
.m1 .medal::after{content:"👑";position:absolute;top:-17px;left:50%;transform:translateX(-50%) rotate(8deg);font-size:.95rem}
.m2 .medal{background:var(--silver);color:#fff;box-shadow:0 0 0 4px var(--silver-soft)}
.m3 .medal{background:var(--bronze);color:#fff;box-shadow:0 0 0 4px var(--bronze-soft)}
.rank-main h3{font-size:1.3rem;color:var(--ink);font-weight:600}
.rank-main h3 a{color:inherit}
.rank-meta{font-size:.84rem;color:var(--mut);margin-top:1px;font-weight:600}
.badge-yl{display:inline-block;font-family:'Nunito',sans-serif;font-size:.68rem;font-weight:900;letter-spacing:.05em;background:var(--gold-line);color:var(--ink);border:2px solid var(--ink);border-radius:99px;padding:2px 10px;vertical-align:3px;margin-left:8px;box-shadow:0 2px 0 rgba(20,33,63,.2)}
.pillars{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 22px;margin-top:13px;max-width:520px}
.pillar{display:grid;grid-template-columns:118px 1fr 40px;align-items:center;gap:9px;font-size:.78rem;color:var(--mut);font-weight:700}
.bar{height:9px;border-radius:99px;background:var(--blue-soft);overflow:hidden;border:1px solid rgba(20,33,63,.12)}
.bar i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--blue),var(--blue-deep))}
.m1 .bar i{background:linear-gradient(90deg,var(--blue),var(--gold))}
.pillar .v{font-family:'IBM Plex Mono',monospace;font-size:.76rem;color:var(--ink);text-align:right;font-weight:600}
.rank-side{display:flex;flex-direction:column;align-items:flex-end;gap:10px;justify-content:space-between}
.btn{display:inline-block;background:var(--gold-line);color:var(--ink);font-weight:900;font-family:'Nunito',sans-serif;font-size:.92rem;border-radius:999px;padding:11px 20px;border:2.5px solid var(--ink);cursor:pointer;box-shadow:0 3px 0 var(--ink)}
.btn:hover{background:#FFD34D;text-decoration:none}
.btn.ghost{background:#fff;color:var(--blue-deep);border-color:var(--blue-deep);box-shadow:0 3px 0 var(--blue-deep);font-weight:800}
.btn.ghost:hover{background:var(--blue-soft)}
.rank-strength{font-size:.86rem;color:var(--body);margin-top:11px;font-weight:600}
.rank-strength b{color:var(--ok);font-weight:900}
@media(max-width:700px){.rank-card{grid-template-columns:44px 1fr}.rank-side{flex-direction:row;align-items:center;grid-column:1/-1;justify-content:flex-start}.pillars{grid-template-columns:1fr}}
/* toggle chips */
.chips{display:flex;gap:9px;flex-wrap:wrap;margin:20px 0 22px}
.chip{font-family:'Nunito',sans-serif;font-size:.88rem;font-weight:800;border:2px solid var(--line);background:var(--card);color:var(--body);border-radius:999px;padding:8px 16px;cursor:pointer}
.chip:hover{border-color:var(--blue)}
.chip.on{background:var(--blue);border-color:var(--ink);color:#fff;box-shadow:0 2px 0 var(--ink)}
/* receipt — serrated bottom edge like a printed receipt */
.receipt{background:var(--card);border-radius:var(--r) var(--r) 0 0;border:2px solid var(--line);border-bottom:none;box-shadow:var(--shadow);overflow:visible;margin-bottom:34px;position:relative}
.receipt::after{content:"";position:absolute;left:0;right:0;bottom:-9px;height:9px;background-image:linear-gradient(45deg,var(--card) 5px,transparent 5px),linear-gradient(-45deg,var(--card) 5px,transparent 5px);background-size:14px 9px;background-repeat:repeat-x;filter:drop-shadow(0 3px 3px rgba(20,33,63,.06))}
.receipt-head{display:flex;justify-content:space-between;align-items:center;padding:15px 20px;background:var(--cream);border-bottom:2px dashed var(--line);border-radius:18px 18px 0 0}
.receipt-head h3{font-size:1.08rem;color:var(--ink);font-weight:600}
.receipt-head .w{font-family:'IBM Plex Mono',monospace;font-size:.78rem;color:var(--mut);font-weight:500}
.receipt-head .sub{font-family:'Fredoka',sans-serif;font-weight:600;color:var(--ink);font-size:1.15rem}
table.rows{width:100%;border-collapse:collapse;font-size:.9rem}
table.rows th{text-align:left;font-size:.7rem;letter-spacing:.07em;color:var(--mut);font-weight:800;padding:9px 20px;border-bottom:1px solid var(--line);text-transform:uppercase;font-family:'Nunito',sans-serif}
table.rows td{padding:11px 20px;border-bottom:1px solid var(--line);vertical-align:top}
table.rows tr:last-child td{border-bottom:none}
td.pts,th.pts{text-align:right;font-family:'IBM Plex Mono',monospace;white-space:nowrap}
td.pts b{color:var(--ink)}
.src{font-size:.72rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.quote{font-size:.8rem;color:var(--mut);font-style:italic;margin-top:3px;font-weight:400}
/* profile hero */
.p-hero{background:var(--card);border-radius:var(--r);border:2.5px solid var(--line);box-shadow:var(--shadow);padding:28px;display:grid;grid-template-columns:1fr auto;gap:24px;margin-bottom:22px;border-top:6px solid var(--blue)}
.p-hero.m1{border-top-color:var(--gold);border-color:var(--gold)}
.p-hero.m2{border-top-color:var(--silver)}
.p-hero.m3{border-top-color:var(--bronze)}
.p-hero h1{font-size:1.85rem;color:var(--ink);font-weight:600}
.p-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px 26px;margin-top:16px;font-size:.88rem}
.p-facts b{display:block;color:var(--ink);font-weight:800}
.p-facts span{color:var(--mut);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.stamp-big{display:flex;flex-direction:column;align-items:center;gap:10px}
.stamp-big .stamp .n{font-size:2.4rem}
/* two-col */
.duo{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:22px}
@media(max-width:700px){.duo{grid-template-columns:1fr}.p-hero{grid-template-columns:1fr}}
.panel{background:var(--card);border-radius:var(--r);border:2px solid var(--line);box-shadow:var(--shadow);padding:20px}
.panel h3{font-size:1.05rem;color:var(--ink);margin-bottom:11px;font-weight:600}
.panel ul{list-style:none}
.panel li{padding:6px 0 6px 26px;position:relative;font-size:.92rem;font-weight:600}
.panel li::before{position:absolute;left:0;font-weight:900;font-size:1rem}
.panel.plus li::before{content:"✓";color:var(--ok)}
.panel.minus li::before{content:"!";color:var(--warn);left:4px}
.ai-note{background:var(--card);border-radius:var(--r);border:2px solid var(--line);box-shadow:var(--shadow);padding:20px;margin-bottom:22px;border-left:6px solid var(--blue)}
.ai-note .tag{font-size:.66rem;font-weight:700;letter-spacing:.08em;color:var(--blue-deep);font-family:'IBM Plex Mono',monospace}
.ai-note p{margin-top:7px;font-size:.97rem;font-weight:600}
/* category dir */
.cat-group{margin-bottom:34px}
.cat-group h3{font-size:1.15rem;color:var(--ink);margin-bottom:13px;padding-bottom:8px;border-bottom:3px solid var(--blue-soft);font-weight:600}
.cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:11px}
.cat-tile{background:var(--card);border-radius:14px;border:2px solid var(--line);box-shadow:0 2px 0 rgba(20,33,63,.07);padding:13px 16px;display:flex;justify-content:space-between;align-items:center;font-weight:800;color:var(--ink);font-size:.92rem}
.cat-tile:hover{text-decoration:none;border-color:var(--blue)}
.cat-tile.off{opacity:.5;font-weight:700;color:var(--mut);pointer-events:none}
.cat-tile .st{font-size:.66rem;font-weight:700;font-family:'IBM Plex Mono',monospace;color:var(--mut)}
.cat-tile.live-cat{border-color:var(--ok)}
.cat-tile.live-cat .st{color:var(--ok)}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:760px){.steps{grid-template-columns:1fr}}
.step{background:var(--card);border-radius:var(--r);border:2px solid var(--line);box-shadow:var(--shadow);padding:22px}
.step .k{font-family:'IBM Plex Mono',monospace;font-size:.72rem;color:var(--gold-deep);font-weight:600;letter-spacing:.1em}
.step h3{color:var(--ink);font-size:1.12rem;margin:8px 0 7px;font-weight:600}
.step p{font-size:.9rem;color:var(--mut);font-weight:600}
/* b2b */
.b2b{background:linear-gradient(165deg,var(--blue) 0%,var(--blue-deep) 100%);border-radius:var(--r);border:3px solid var(--ink);box-shadow:0 5px 0 rgba(20,33,63,.3);color:#fff;padding:30px;margin:26px 0}
.b2b h3{font-size:1.4rem;font-weight:600}
.b2b p{color:#D6E4FB;margin:9px 0 16px;max-width:640px;font-size:.95rem;font-weight:600}
.b2b small{display:block;margin-top:12px;color:#AFC6EC;font-size:.78rem;font-weight:600}
/* misc */
.crumb{font-size:.84rem;color:var(--mut);margin:22px 0 14px;font-weight:700}
.crumb a{color:var(--mut)}
.upd{display:inline-flex;align-items:center;gap:7px;font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--ink);background:var(--card);border:2px solid var(--line);border-radius:99px;padding:5px 13px;font-weight:600}
.upd::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--ok)}
.note{font-size:.82rem;color:var(--mut);background:var(--blue-soft);border:1.5px solid var(--line);border-radius:14px;padding:12px 16px;margin:18px 0;font-weight:600}
footer.site{background:var(--ink);color:#93A2BC;padding:36px 0;margin-top:64px;font-size:.84rem}
footer.site .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:32px}
@media(max-width:700px){footer.site .cols{grid-template-columns:1fr}}
footer.site a{color:#C8D6EE;font-weight:700}
footer.site h4{color:var(--gold-line);font-size:.95rem;margin-bottom:9px;font-weight:600}
footer.site .fine{margin-top:26px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);font-size:.75rem;line-height:1.6}
.pageh{padding:40px 0 8px}
.pageh h1{font-size:clamp(1.7rem,3.6vw,2.4rem);color:var(--ink);line-height:1.12;font-weight:600}
.pageh p.lead{color:var(--mut);margin-top:10px;max-width:640px;font-size:1.02rem;font-weight:600}
.meta-row{display:flex;gap:12px;align-items:center;margin-top:16px;flex-wrap:wrap}
.count-pill{font-family:'IBM Plex Mono',monospace;font-size:.76rem;color:var(--mut);font-weight:600}
/* ---------- motion & micro-interactions ---------- */
.rv{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
.bar i{transition:width .9s cubic-bezier(.2,.7,.2,1)}
.rank-card{transition:transform .22s cubic-bezier(.3,1.4,.4,1),box-shadow .22s ease,border-color .22s ease}
.rank-card:hover{transform:translateY(-3px) rotate(-.3deg);box-shadow:0 6px 0 rgba(20,33,63,.1),0 16px 34px rgba(30,79,168,.16)}
.cat-tile{transition:transform .18s cubic-bezier(.3,1.4,.4,1),box-shadow .18s ease,border-color .18s ease}
.cat-tile:not(.off):hover{transform:translateY(-2px) rotate(-.4deg);box-shadow:0 4px 0 rgba(20,33,63,.12)}
.btn{transition:transform .15s cubic-bezier(.3,1.5,.4,1),background .15s ease,box-shadow .15s ease}
.btn:hover{transform:translateY(-2px)}
.btn:active{transform:translateY(1px);box-shadow:0 1px 0 var(--ink)}
.step{transition:transform .2s cubic-bezier(.3,1.4,.4,1)}
.step:hover{transform:translateY(-2px) rotate(.3deg)}
.chip{transition:border-color .15s ease,background .15s ease,color .15s ease,transform .15s ease}
.chip:active{transform:scale(.94)}
.stamp{transition:transform .22s cubic-bezier(.3,1.6,.4,1)}
.rank-card:hover .stamp{transform:scale(1.06) rotate(2deg)}
@keyframes sortIn{from{opacity:.25;transform:translateY(10px) scale(.99)}to{opacity:1;transform:none}}
.sort-in{animation:sortIn .4s cubic-bezier(.2,.7,.2,1)}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  .rv{opacity:1;transform:none}
}
/* ---------- mobile ---------- */
@media(max-width:720px){
  .wrap{padding:0 16px}
  header.site .wrap{flex-wrap:wrap;height:auto;padding:9px 16px 8px;gap:5px 16px}
  .brand{font-size:1.1rem}
  .brand img{width:38px;height:38px}
  nav.main{margin-left:0;width:100%;gap:18px;overflow-x:auto;font-size:.86rem;-webkit-overflow-scrolling:touch;scrollbar-width:none}
  nav.main::-webkit-scrollbar{display:none}
  nav.main a{white-space:nowrap;padding:2px 0}
  .demo-ribbon{font-size:.7rem;padding:5px 10px}
  .hero{padding:34px 0 44px}
  .hero-logo{width:96px;height:96px;margin-bottom:14px}
  .hero-stats{gap:20px}
  section.band{padding:40px 0}
}
@media(max-width:640px){
  table.rows th:nth-child(3):not(:last-child),table.rows td:nth-child(3):not(:last-child){display:none}
  table.rows th,table.rows td{padding:9px 14px;font-size:.83rem}
  .receipt-head{padding:12px 14px}
  .receipt-head h3 .w{display:block;margin-top:2px}
  .rank-card{padding:16px}
  .rank-side{flex-wrap:wrap;gap:8px}
  .rank-side>div{flex-direction:row!important;flex-wrap:wrap;align-items:center!important}
  .btn{padding:9px 15px;font-size:.86rem}
  .p-hero{padding:20px}
  .stamp-big{flex-direction:row;align-items:center;justify-content:flex-start;gap:14px}
  .b2b{padding:22px 18px}
  .quote{word-break:break-word}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

APP_JS = r"""
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Pillar bars: remember target width, start from zero, animate when visible
  var bars = document.querySelectorAll('.bar i');
  bars.forEach(function(b){ b.dataset.w = b.style.width; if (!reduce) b.style.width = '0%'; });
  function fillBars(scope){ (scope || document).querySelectorAll('.bar i').forEach(function(b){ b.style.width = b.dataset.w; }); }

  // Scroll reveal (plain scroll check — reliable everywhere)
  var targets = Array.prototype.slice.call(
    document.querySelectorAll('.rank-card,.receipt,.step,.panel,.ai-note,.b2b,.cat-group,.p-hero,.note,.cat-tile')
  );
  if (reduce) {
    targets.forEach(function(el){ el.classList.add('in'); });
    fillBars();
  } else {
    targets.forEach(function(el, i){
      el.classList.add('rv');
      el.style.transitionDelay = Math.min((i % 5) * 55, 220) + 'ms';
    });
    var pending = targets.slice();
    function check(){
      if (!pending.length) return;
      var limit = window.innerHeight * 0.94;
      pending = pending.filter(function(el){
        if (el.getBoundingClientRect().top < limit) {
          el.classList.add('in');
          fillBars(el);
          return false;
        }
        return true;
      });
    }
    addEventListener('scroll', check, {passive: true});
    addEventListener('resize', check);
    check();
    setTimeout(check, 250);
    // safety net: if nothing revealed (broken env), show everything
    setTimeout(function(){
      if (pending.length === targets.length) {
        pending.forEach(function(el){ el.classList.add('in'); fillBars(el); el.style.transitionDelay = '0ms'; });
        pending = [];
      }
    }, 1500);
  }

  // Leaderboard rows stagger on load
  document.querySelectorAll('.board-row').forEach(function(r, i){
    if (reduce) return;
    r.classList.add('rv');
    setTimeout(function(){ r.classList.add('in'); }, 450 + i * 100);
  });

  // Count-up on profile score stamp
  var n = document.querySelector('.stamp-big .stamp .n');
  if (n && !reduce) {
    var target = parseFloat(n.textContent.replace(',', '.'));
    if (!isNaN(target)) {
      var t0 = null;
      var step = function(ts){
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / 950, 1);
        p = 1 - Math.pow(1 - p, 3);
        n.textContent = (target * p).toFixed(1).replace('.', ',');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  }
})();
"""

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
<link rel="icon" type="image/png" href="{root}assets/favicon.png">
<link rel="stylesheet" href="{root}assets/style.css?v=7">
<script src="{root}assets/app.js?v=7" defer></script>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{root}"><img src="{root}assets/logo-200.png" alt="Suomen Paras -logo" width="46" height="46">Suomen&nbsp;Paras<span class="tm">.com</span></a>
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
        rows.append(f'<div class="board-row{g}"><span class="pos">{i}</span><span class="nm">{esc(c["nimi"])}</span><span class="dots"></span><span class="sc">{sc}</span></div>')

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
      <img class="hero-logo" src="assets/logo-480.png" alt="Suomen Paras" width="132" height="132">
      <h1>Suomen kaikki vertailut.<br>Yksi läpinäkyvä <em>pisteytys</em>.</h1>
      <p class="lead">Vertailemme suomalaiset palvelut mitattavalla datalla, samalla kaavalla ja julkisin perustein. Näet jokaisen pisteen alkuperän.</p>
      <div class="hero-stats">
        <div class="hero-stat"><b>{len(SCORES)}</b><span>palvelua pisteytetty</span></div>
        <div class="hero-stat"><b>{TOTAL_CATS}</b><span>kategoriaa suunnitteilla</span></div>
        <div class="hero-stat"><b>26</b><span>mittaria / yritys</span></div>
      </div>
    </div>
    <div class="board-wrap">
      <div class="board" id="liveboard">
        <div class="board-head"><span class="cat" id="lb-cat">Lainavertailu</span><span class="live"><span class="live-dot"></span><span id="lb-status">TOP 5 · {UPDATED}</span></span></div>
        <div id="lb-body">{''.join(rows)}</div>
        <div class="board-foot" id="lb-foot"><a href="lainavertailu/">Koko vertailu ja pisteiden perustelut →</a></div>
      </div>
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
        card.classList.remove('sort-in');
        wrap.appendChild(card);
        void card.offsetWidth;
        card.classList.add('sort-in');
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
    rank_label = {1: "👑 Sija 1 — Suomen Paras 2026", 2: "🥈 Sija 2 / " + str(len(SCORES)), 3: "🥉 Sija 3 / " + str(len(SCORES))}.get(pos, f"Sija {pos} / {len(SCORES)}")

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
    w("assets/app.js", APP_JS)
    w("index.html", build_index())
    w("lainavertailu/index.html", build_lainavertailu())
    w("kategoriat/index.html", build_kategoriat())
    w("metodologia/index.html", build_metodologia())
    for i, c in enumerate(SCORES, 1):
        w(f"yritys/{c['slug']}/index.html", build_profile(c, i))
    print("OK —", 4 + len(SCORES), "pages")

if __name__ == "__main__":
    main()
