# -*- coding: utf-8 -*-
"""Suomen Paras — static site generator (demo).

Reads data/<vertical>.json (produced by the scoring engine) and generates the site:
  index.html, <vertical>/, yritys/<vertical>/<slug>/, kategoriat/, metodologia/

Each vertical file carries its own config (labels, notes, transparency criteria) so
this generator stays vertical-agnostic — adding a category means adding a data file.

This mirrors the real pipeline: data collection -> scoring -> publish.
Run:  python gen_site.py
"""
import json, os, html, glob

BASE = os.path.dirname(os.path.abspath(__file__))
SCORE_VERSION = "v1.1"
# Site-wide "latest measurement" date. Each vertical carries its own `updated` —
# never relabel a vertical with a date it wasn't measured on (methodology promises
# results are not rewritten retroactively).
UPDATED = "16.7.2026"

# Order matters: first vertical is the site's flagship (shown on the front-page board).
VERTICAL_ORDER = ["lainavertailu", "vakuutukset", "sahkosopimukset", "laajakaista"]


def _load_verticals():
    found = {}
    for p in glob.glob(os.path.join(BASE, "data", "*.json")):
        v = json.load(open(p, encoding="utf-8"))
        v["yritykset"].sort(key=lambda c: -(c["score"] or 0))
        found[v["slug"]] = v
    ordered = [found[s] for s in VERTICAL_ORDER if s in found]
    ordered += [v for s, v in sorted(found.items()) if s not in VERTICAL_ORDER]
    if not ordered:
        raise SystemExit("no data/*.json found — run the scoring engine first")
    return ordered


VERTICALS = _load_verticals()
ALL_COMPANIES = [c for v in VERTICALS for c in v["yritykset"]]

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
    # Meta-flagship: categories that rank comparison services themselves ("vertailemme vertailijat").
    ("Vertailupalvelut", [
        ("Lainavertailupalvelut", "lainavertailu", True),
        ("Sähkövertailupalvelut", "sahkovertailupalvelut", True), ("Vakuutusvertailupalvelut", None, False),
        ("Hintavertailupalvelut", None, False), ("Matka- ja hotellivertailut", None, False),
        ("Lentovertailupalvelut", None, False),
    ]),
    ("Talous ja raha", [
        ("Vakuutukset", "vakuutukset", True), ("Sähkösopimukset", "sahkosopimukset", True),
        ("Laajakaista", "laajakaista", True), ("Puhelinliittymät", "puhelinliittymat", True),
        ("Luottokortit", "luottokortit", True), ("Sijoitusalustat", "sijoitusalustat", True),
        ("Kulutusluotot", "kulutusluotot", True), ("Webhotellit", "webhotellit", True),
        ("VPN-palvelut", "vpn-palvelut", True), ("Pankit", "pankit", True),
        ("Autovakuutukset", "autovakuutukset", True), ("Kotivakuutukset", "kotivakuutukset", True),
        ("Matkavakuutukset", "matkavakuutukset", True), ("Lemmikkivakuutukset", "lemmikkivakuutukset", True),
        ("Pikavipit", None, False), ("Asuntolainat", None, False),
        ("Autorahoitus", None, False), ("Yrityslainat", None, False),
        ("Säästötilit", None, False),
    ]),
    ("Digitaaliset palvelut", [
        ("Suoratoistopalvelut", None, False), ("Pilvitallennuspalvelut", "pilvitallennuspalvelut", True),
        ("Virustorjuntaohjelmat", None, False), ("Salasananhallintapalvelut", "salasananhallintapalvelut", True),
        ("Sähköpostipalvelut", None, False), ("Verkkotunnusvälittäjät", None, False),
        ("Kirjanpito-ohjelmat", None, False), ("Verkkokauppa-alustat", None, False),
    ]),
    ("Koti ja asuminen", [
        ("Lämpöpumppuasentajat", None, False), ("Aurinkopaneeliasentajat", None, False),
        ("Putkiliikkeet", None, False), ("Sähköasentajat", None, False),
        ("Kattoremontit", None, False), ("Muuttopalvelut", "muuttopalvelut", True),
        ("Siivouspalvelut", "siivouspalvelut", True), ("Kiinteistönvälittäjät", "kiinteistonvalittajat", True),
        ("Rakennusliikkeet", None, False), ("Maalausliikkeet", None, False),
        ("Ikkunaremontit", None, False), ("Keittiöremontit", None, False),
        ("Lukkoliikkeet", None, False), ("Kodinkonehuolto", None, False),
        ("Jätehuoltopalvelut", None, False), ("Piha- ja puutarhapalvelut", None, False),
        ("Ilmanvaihtohuollot", None, False),
    ]),
    ("Auto ja liikenne", [
        ("Autokorjaamot", "autokorjaamot", True), ("Autokatsastus", "autokatsastus", True),
        ("Rengasliikkeet", "rengasliikkeet", True), ("Autopesulat", None, False),
        ("Autokoulut", "autokoulut", True), ("Autovuokraamot", "autovuokraamot", True),
        ("Sähköauton latausasennukset", None, False), ("Autoliikkeet", None, False),
        ("Autohinaus", None, False), ("Moottoripyöräkorjaamot", None, False),
        ("Autotarvikeliikkeet", None, False), ("Taksipalvelut", None, False),
    ]),
    ("Terveys ja hyvinvointi", [
        ("Hammaslääkärit", "hammaslaakarit", True), ("Yksityislääkärit", "yksityislaakarit", True),
        ("Fysioterapeutit", None, False), ("Hierojat", None, False),
        ("Optikot", "optikot", True), ("Kuntosalit", "kuntosalit", True),
        ("Eläinlääkärit", None, False), ("Psykoterapeutit", None, False),
        ("Jalkahoitolat", None, False), ("Kauneushoitolat", None, False),
        ("Silmälääkärit", None, False), ("Personal trainerit", None, False),
        ("Joogastudiot", None, False), ("Ravintoterapeutit", None, False),
    ]),
    ("Ravintolat ja kahvilat", [
        ("Pizzeriat", None, False), ("Sushiravintolat", None, False),
        ("Hampurilaisravintolat", None, False), ("Lounasravintolat", None, False),
        ("Kahvilat", None, False), ("Kebab-ravintolat", None, False),
        ("Fine dining", None, False), ("Brunssipaikat", None, False),
        ("Thairavintolat", None, False), ("Konditoriat", None, False),
        ("Vegaaniravintolat", None, False),
    ]),
    ("Palvelut yrityksille", [
        ("Tilitoimistot", None, False), ("Mainostoimistot", None, False),
        ("IT-tukipalvelut", None, False), ("Lakitoimistot", None, False),
        ("Käännöstoimistot", None, False), ("Rekrytointipalvelut", None, False),
        ("Vartiointipalvelut", None, False), ("Maksupäätepalvelut", None, False),
        ("Työterveyspalvelut", None, False), ("Vakuutusmeklarit", None, False),
    ]),
    ("Vapaa-aika ja muut", [
        ("Lakifirmat", "lakifirmat", True), ("Pakohuoneet", "pakohuoneet", True),
        ("Parturit ja kampaamot", None, False), ("Valokuvaajat", None, False),
        ("Juhlatilat", None, False), ("Catering-palvelut", None, False),
        ("Hääpalvelut", None, False), ("Ohjelmistokoulut lapsille", None, False),
        ("Kielikurssit", None, False), ("Tanssikoulut", None, False),
        ("Kukkakaupat", None, False), ("Matkatoimistot", None, False),
        ("Hautaustoimistot", None, False), ("Lemmikkihoitolat", None, False),
    ]),
]
TOTAL_CATS = sum(len(cats) for _, cats in CATEGORY_GROUPS)
# A category is LIVE only if its data file actually exists — never claim a category
# is live from the table above alone.
LIVE_SLUGS = {v["slug"] for v in VERTICALS}
LIVE_COUNT = sum(1 for _, cats in CATEGORY_GROUPS for _, slug, _ in cats if slug in LIVE_SLUGS)

# ---------------------------------------------------------------- shared css
CSS = """
:root{
  --bg:#FDF0F6; --card:#FFFFFF; --ink:#43112B; --body:#5C2743; --mut:#9A6480;
  --blue:#D6336C; --blue-deep:#A61E4D; --blue-soft:#FBDCE8;
  --line:#F2C4D8; --gold:#F7B500; --gold-deep:#D89B00; --gold-soft:#FFF3CE; --gold-line:#FFC61A;
  --silver:#B48EA0; --silver-soft:#F9EEF4; --bronze:#C08447; --bronze-soft:#F9EFE2;
  --ok:#1F9D55; --warn:#C2410C; --cream:#FFF6FB;
  --r:20px;
  --shadow:0 2px 0 rgba(67,17,43,.06),0 8px 20px rgba(166,30,77,.12);
  --pop:0 4px 0 rgba(67,17,43,.16);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Nunito',system-ui,sans-serif;background:var(--bg);color:var(--body);line-height:1.6;font-size:16.5px}
h1,h2,h3,h4,.brand{font-family:'Baloo 2',sans-serif}
.mono{font-family:'IBM Plex Mono',monospace}
a{color:var(--blue-deep);text-decoration:none}
a:hover{text-decoration:underline}
:focus-visible{outline:3px solid var(--gold);outline-offset:2px;border-radius:6px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
/* header — graphite/silver to match the logo */
header.site{background:linear-gradient(180deg,#B03068 0%,#8A1F4E 100%);color:#fff;position:sticky;top:0;z-index:50;border-bottom:3px solid #4A0E2C}
header.site .wrap{display:flex;align-items:center;gap:24px;height:66px}
.brand{display:flex;align-items:center;gap:12px;font-weight:700;font-size:1.28rem;color:#fff;letter-spacing:.01em}
.brand:hover{text-decoration:none}
.brand img{width:58px;height:58px;filter:drop-shadow(0 2px 3px rgba(0,0,0,.35));transition:transform .25s cubic-bezier(.3,1.6,.4,1)}
.brand:hover img{transform:rotate(-8deg) scale(1.08)}
.brand .tm{color:var(--gold-line)}
.brand .btxt{display:flex;flex-direction:column;line-height:1.1}
.brand .oy{font-family:'IBM Plex Mono',monospace;font-size:.6rem;font-weight:500;letter-spacing:.22em;color:#9DABC2;text-transform:uppercase;margin-top:3px}
nav.main{display:flex;gap:22px;margin-left:auto;align-items:center}
nav.main a{color:#DCE8FC;font-weight:800;font-size:.95rem}
nav.main a:hover{color:#fff;text-decoration:none}
nav.main a.on{color:var(--gold-line)}
/* Category dropdown — a flat nav stopped fitting at 5+ categories (roadmap is 67). */
.navdd{position:relative}
.navdd-btn{background:none;border:0;padding:0;cursor:pointer;color:#DCE8FC;font-family:inherit;font-weight:800;font-size:.95rem;display:flex;align-items:center;gap:5px}
.navdd-btn:hover,.navdd.open .navdd-btn{color:#fff}
.navdd.on-cat .navdd-btn{color:var(--gold-line)}
.navdd-btn .car{font-size:.62rem;transition:transform .18s}
.navdd.open .navdd-btn .car{transform:rotate(180deg)}
.navdd-panel{display:none;position:absolute;top:calc(100% + 12px);right:0;min-width:250px;background:var(--card);border:2.5px solid var(--ink);border-radius:10px;box-shadow:5px 6px 0 rgba(20,33,63,.22);padding:7px;z-index:60}
.navdd.open .navdd-panel{display:block}
.navdd-panel a{display:flex;justify-content:space-between;align-items:center;gap:12px;color:var(--ink);font-size:.9rem;font-weight:700;padding:8px 10px;border-radius:6px}
.navdd-panel a:hover{background:var(--blue-soft);text-decoration:none}
.navdd-panel a.on{background:var(--gold-soft)}
.navdd-panel .n{font-family:'IBM Plex Mono',monospace;font-size:.72rem;font-weight:600;color:var(--mut)}
.navdd-panel hr{border:0;border-top:1.5px solid var(--line);margin:6px 4px}
.navdd-panel .all{color:var(--blue-deep)}
.demo-ribbon{background:var(--ink);color:var(--gold-line);text-align:center;font-size:.8rem;font-weight:800;padding:6px 12px;letter-spacing:.03em}
/* hero */
.hero{background:linear-gradient(170deg,#C2417A 0%,#96285C 62%,#5E1638 100%);color:#fff;padding:58px 0 74px;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;width:1700px;height:1700px;left:50%;top:-560px;transform:translateX(-50%);background:repeating-conic-gradient(rgba(255,255,255,.55) 0 9deg,transparent 9deg 18deg);border-radius:50%;pointer-events:none;opacity:.045;animation:spin 140s linear infinite;-webkit-mask-image:radial-gradient(closest-side at 50% 42%,#000 34%,transparent 74%);mask-image:radial-gradient(closest-side at 50% 42%,#000 34%,transparent 74%)}
.hero .wrap{position:relative}
.kicker{font-family:'IBM Plex Mono',monospace;font-size:.7rem;letter-spacing:.16em;color:var(--gold-line);margin-bottom:16px;font-weight:600}
.hero h1{font-size:clamp(2.1rem,4.8vw,3.4rem);line-height:1.08;letter-spacing:.01em;color:#fff;font-weight:800;max-width:660px}
.hero h1 em{font-style:normal;color:var(--gold-line)}
.hero p.lead{margin-top:16px;font-size:1.1rem;color:#F8DCE9;max-width:560px;font-weight:600}
.hero-logo{width:240px;height:240px;margin-bottom:18px;filter:drop-shadow(0 10px 24px rgba(0,0,0,.45));animation:bounceIn .8s cubic-bezier(.3,1.5,.4,1) both,logoPulse 3.2s ease-in-out .9s infinite}
@keyframes logoPulse{0%,100%{transform:scale(1);filter:drop-shadow(0 10px 24px rgba(0,0,0,.45))}50%{transform:scale(1.05);filter:drop-shadow(0 14px 34px rgba(255,198,26,.28))}}
@media(prefers-reduced-motion:reduce){.hero-logo{animation:none}}
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
.hero-stat b{display:block;font-family:'Baloo 2',sans-serif;font-size:1.5rem;color:var(--gold-line);font-weight:600}
.hero-stat span{font-size:.84rem;color:#EBBCD3;font-weight:600}
/* live board */
.board{background:var(--card);border-radius:var(--r);border:3px solid var(--ink);box-shadow:0 6px 0 rgba(74,14,44,.35);color:var(--body);overflow:hidden}
.board-head{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:2px solid var(--line);background:var(--cream)}
.board-head .cat{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink);font-size:1.05rem}
.board-head .live{display:flex;align-items:center;gap:7px;font-size:.72rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.live-dot{width:9px;height:9px;border-radius:50%;background:var(--ok);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
@media(prefers-reduced-motion:reduce){.live-dot{animation:none}}
.board-row{display:flex;align-items:center;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line)}
.board-row:last-child{border-bottom:none}
.board-row .pos{font-family:'Baloo 2',sans-serif;font-weight:600;width:24px;color:var(--mut)}
.board-row.gold{background:var(--gold-soft)}
.board-row.gold .pos{color:var(--gold-deep)}
.board-row .nm{font-weight:800;color:var(--ink)}
.board-row .dots{flex:1;border-bottom:2px dotted #EFC6DA;height:2px;margin:0 6px;transform:translateY(5px)}
.board-row .sc{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink)}
.board-foot{padding:12px 18px;font-size:.88rem;font-weight:700}
.board{transition:opacity .26s ease}
.board.lb-fade{opacity:0}
/* front-page top-3 boards */
.top-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.top-board{display:block;background:var(--card);border-radius:var(--r);border:2.5px solid var(--line);box-shadow:var(--shadow);overflow:hidden;color:var(--body);transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}
.top-board:hover{transform:translateY(-3px);border-color:var(--blue);text-decoration:none;box-shadow:0 10px 22px rgba(10,25,60,.14)}
.tb-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px;padding:12px 16px;background:var(--cream);border-bottom:2px solid var(--line);font-family:'Baloo 2',sans-serif;font-weight:700;color:var(--ink);font-size:1.02rem}
.tb-head .tb-n{font-family:'IBM Plex Mono',monospace;font-size:.68rem;color:var(--mut);font-weight:500;white-space:nowrap}
.tb-row{display:flex;align-items:center;gap:10px;padding:9px 16px;border-bottom:1px solid var(--line);font-size:.92rem}
.tb-row .pos{font-family:'Baloo 2',sans-serif;font-weight:600;width:20px;color:var(--mut)}
.tb-row.gold{background:var(--gold-soft)}
.tb-row.gold .pos{color:var(--gold-deep)}
.tb-row .nm{font-weight:800;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tb-row .dots{flex:1;border-bottom:2px dotted #EFC6DA;height:2px;margin:0 4px;transform:translateY(5px);min-width:14px}
.tb-row .sc{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink)}
.tb-foot{padding:10px 16px;font-size:.84rem;font-weight:800;color:var(--blue)}
/* front-page search */
.sp-search{position:relative;margin:0 0 24px;max-width:600px}
.sp-search input{width:100%;padding:16px 96px 16px 52px;border-radius:999px;border:3px solid var(--ink);font-family:inherit;font-size:1.02rem;font-weight:700;background:#fff;color:var(--ink);box-shadow:0 5px 0 rgba(74,14,44,.25);appearance:none;-webkit-appearance:none}
.sp-ico{position:absolute;left:18px;top:50%;transform:translateY(-50%);width:22px;height:22px;color:var(--blue-deep);pointer-events:none;z-index:2}
.sp-btn{position:absolute;right:7px;top:50%;transform:translateY(-50%);background:linear-gradient(165deg,var(--blue) 0%,var(--blue-deep) 100%);color:#fff;border:2.5px solid var(--ink);border-radius:999px;padding:9px 20px;font-family:'Baloo 2',sans-serif;font-weight:700;font-size:.95rem;cursor:pointer;z-index:2}
.sp-btn:hover{filter:brightness(1.08)}
.sp-search input::-webkit-search-cancel-button{display:none}
.sp-search input::placeholder{color:var(--mut);font-weight:600}
.sp-search input:focus{outline:3px solid var(--gold);outline-offset:1px}
.sp-results{position:absolute;top:calc(100% + 10px);left:0;right:0;background:var(--card);border:2.5px solid var(--ink);border-radius:18px;box-shadow:5px 6px 0 rgba(74,14,44,.25);z-index:70;overflow:hidden;max-height:340px;overflow-y:auto}
.sp-row{display:flex;align-items:center;gap:10px;padding:11px 14px;border-bottom:1px solid var(--line);color:var(--ink);font-weight:700;font-size:.95rem}
.sp-row:hover{background:var(--blue-soft);text-decoration:none}
.sp-row:last-child{border-bottom:none}
.sp-tag{font-family:'IBM Plex Mono',monospace;font-size:.6rem;background:var(--blue-soft);color:var(--blue-deep);padding:2px 7px;border-radius:6px;font-weight:600;white-space:nowrap;letter-spacing:.05em}
.sp-tag.y{background:var(--gold-soft);color:#7A5A0E}
.sp-nm{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sp-nm small{color:var(--mut);font-weight:600}
.sp-sc{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--blue-deep)}
.sp-go{color:var(--mut)}
.sp-empty{padding:14px;color:var(--mut);font-weight:600;font-size:.92rem}
/* footer bottom bar */
.foot-bottom{display:flex;justify-content:space-between;align-items:center;gap:14px;margin-top:24px;border-top:1px solid rgba(255,255,255,.14);padding-top:18px;flex-wrap:wrap}
.foot-bottom .oy{font-family:'IBM Plex Mono',monospace;font-size:.7rem;letter-spacing:.16em;text-transform:uppercase}
.foot-bottom .btn{background:var(--gold);color:var(--ink);padding:9px 20px;border-radius:10px;font-weight:800;border:2.5px solid var(--ink)}
.foot-bottom .btn:hover{text-decoration:none;transform:translateY(-1px)}
/* category guide */
.opas-intro{margin-top:14px;color:var(--body);font-weight:600;max-width:720px}
.opas{margin:40px 0 8px;background:var(--card);border:2.5px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:28px}
.opas h3{color:var(--ink);font-size:1.12rem;margin:20px 0 8px}
.opas h3:first-of-type{margin-top:12px}
.opas ul{margin:0 0 6px 22px}
.opas li{margin:6px 0;font-weight:600;color:var(--body);font-size:.95rem}
.opas p{color:var(--body);font-weight:600;font-size:.95rem;max-width:720px}
details.ukk{border:2px solid var(--line);border-radius:12px;margin:8px 0;background:var(--cream)}
details.ukk summary{cursor:pointer;padding:12px 16px;font-weight:800;color:var(--ink);list-style:none;position:relative;padding-right:38px}
details.ukk summary::after{content:"+";position:absolute;right:16px;top:50%;transform:translateY(-50%);font-family:'Baloo 2',sans-serif;font-size:1.3rem;color:var(--blue-deep)}
details.ukk[open] summary::after{content:"−"}
details.ukk p{padding:0 16px 14px;margin:0}
/* analyysi form */
.aform{max-width:640px;margin-bottom:22px}
.aform label{display:block;font-weight:800;color:var(--ink);font-size:.92rem;margin:14px 0 0}
.aform input,.aform select,.aform textarea{display:block;width:100%;margin-top:6px;padding:11px 12px;border:2.5px solid var(--line);border-radius:10px;background:var(--card);color:var(--body);font-family:inherit;font-size:.95rem;font-weight:600}
.aform input:focus,.aform select:focus,.aform textarea:focus{outline:none;border-color:var(--blue)}
.aform textarea{resize:vertical;line-height:1.5}
.aform .btn{margin-top:18px}
.aform small{display:block;margin-top:10px;color:var(--mut);font-weight:600}
.aform-note{color:var(--mut);font-weight:600;margin-bottom:4px}
/* sections */
section.band{padding:56px 0}
h2.sec{font-size:1.65rem;color:var(--ink);font-weight:700;margin-bottom:6px}
h2.sec::before{content:"";display:inline-block;width:22px;height:5px;border-radius:3px;background:linear-gradient(90deg,var(--gold),var(--gold-line));margin-right:11px;vertical-align:.2em}
p.sec-sub{color:var(--mut);margin-bottom:26px;max-width:640px;font-weight:600}
/* score stamp */
.stamp{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:var(--blue-deep);color:#fff;border-radius:16px;border:2.5px solid var(--ink);box-shadow:var(--pop);padding:9px 14px 7px;min-width:80px}
.stamp .n{font-family:'Baloo 2',sans-serif;font-weight:600;font-size:1.6rem;line-height:1}
.stamp .l{font-size:.56rem;letter-spacing:.13em;color:#F0C4D9;margin-top:4px;font-weight:700;font-family:'IBM Plex Mono',monospace}
.stamp.gold{background:linear-gradient(160deg,var(--gold-line),var(--gold));color:var(--ink)}
.stamp.gold .l{color:#7A5A0E}
/* ranking cards */
.rank-card{background:var(--card);border-radius:var(--r);border:2.5px solid var(--line);box-shadow:var(--shadow);padding:22px;display:grid;grid-template-columns:56px 1fr auto;gap:18px;margin-bottom:16px}
.rank-card.m1{border-color:var(--gold);box-shadow:0 5px 0 rgba(216,155,0,.25),0 10px 26px rgba(30,79,168,.12);background:linear-gradient(0deg,var(--card) 84%,var(--gold-soft) 100%)}
.rank-card.m2{border-color:var(--silver)}
.rank-card.m3{border-color:var(--bronze)}
.medal{width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Baloo 2',sans-serif;font-weight:600;font-size:1.15rem;background:var(--silver-soft);color:var(--mut);margin-top:2px;border:2px solid transparent;position:relative}
.m1 .medal{background:var(--gold-line);color:var(--ink);border-color:var(--ink);box-shadow:0 0 0 4px var(--gold-soft)}
.m1 .medal::after{content:"👑";position:absolute;top:-17px;left:50%;transform:translateX(-50%) rotate(8deg);font-size:.95rem}
.m2 .medal{background:var(--silver);color:#fff;box-shadow:0 0 0 4px var(--silver-soft)}
.m3 .medal{background:var(--bronze);color:#fff;box-shadow:0 0 0 4px var(--bronze-soft)}
.rank-main h3{font-size:1.32rem;color:var(--ink);font-weight:700}
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
.receipt-head .sub{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink);font-size:1.15rem}
table.rows{width:100%;border-collapse:collapse;font-size:.9rem}
table.rows th{text-align:left;font-size:.7rem;letter-spacing:.07em;color:var(--mut);font-weight:800;padding:9px 20px;border-bottom:1px solid var(--line);text-transform:uppercase;font-family:'Nunito',sans-serif}
table.rows td{padding:11px 20px;border-bottom:1px solid var(--line);vertical-align:top}
table.rows tr:last-child td{border-bottom:none}
td.pts,th.pts{text-align:right;font-family:'IBM Plex Mono',monospace;white-space:nowrap}
td.pts b{color:var(--ink)}
.src{font-size:.72rem;color:var(--mut);font-family:'IBM Plex Mono',monospace}
.quote{font-size:.8rem;color:var(--mut);font-style:italic;margin-top:4px;font-weight:400}
.qlab{display:inline-block;font-family:'IBM Plex Mono',monospace;font-style:normal;font-size:.58rem;font-weight:600;letter-spacing:.08em;color:var(--ink);background:var(--gold-soft);border:1.5px solid var(--ink);border-radius:3px;padding:0 5px;margin-right:6px;vertical-align:1px}
/* profile hero */
.p-hero{background:var(--card);border-radius:var(--r);border:2.5px solid var(--line);box-shadow:var(--shadow);padding:28px;display:grid;grid-template-columns:1fr auto;gap:24px;margin-bottom:22px;border-top:6px solid var(--blue)}
.p-hero.m1{border-top-color:var(--gold);border-color:var(--gold)}
.p-hero.m2{border-top-color:var(--silver)}
.p-hero.m3{border-top-color:var(--bronze)}
.p-hero h1{font-size:1.9rem;color:var(--ink);font-weight:800}
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
.b2b{background:linear-gradient(165deg,var(--blue) 0%,var(--blue-deep) 100%);border-radius:var(--r);border:3px solid var(--ink);box-shadow:0 5px 0 rgba(74,14,44,.3);color:#fff;padding:30px;margin:26px 0}
.b2b h3{font-size:1.4rem;font-weight:700}
.b2b p{color:#F8DCE9;margin:9px 0 16px;max-width:640px;font-size:.95rem;font-weight:600}
.b2b small{display:block;margin-top:12px;color:#EBBCD3;font-size:.78rem;font-weight:600}
.b2b.light{background:var(--card);color:var(--ink)}
.b2b.light h3{color:var(--ink)}
.b2b.light p{color:var(--body)}
.b2b.light small{color:var(--mut)}
/* misc */
.crumb{font-size:.84rem;color:var(--mut);margin:22px 0 14px;font-weight:700}
.crumb a{color:var(--mut)}
.upd{display:inline-flex;align-items:center;gap:7px;font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--ink);background:var(--card);border:2px solid var(--line);border-radius:99px;padding:5px 13px;font-weight:600}
.upd::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--ok)}
.note{font-size:.82rem;color:var(--mut);background:var(--blue-soft);border:1.5px solid var(--line);border-radius:14px;padding:12px 16px;margin:18px 0;font-weight:600}
footer.site{background:var(--ink);color:#D9A8C1;padding:36px 0;margin-top:64px;font-size:.84rem}
footer.site .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:32px}
@media(max-width:700px){footer.site .cols{grid-template-columns:1fr}}
footer.site a{color:#F3CFE0;font-weight:700}
footer.site h4{color:var(--gold-line);font-size:.95rem;margin-bottom:9px;font-weight:600}
footer.site .fine{margin-top:26px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);font-size:.75rem;line-height:1.6}
.pageh{padding:40px 0 8px}
.pageh h1{font-size:clamp(1.7rem,3.6vw,2.4rem);color:var(--ink);line-height:1.14;font-weight:800}
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
/* ---------- palaute: Anna oma arvio (questionnaire, stored via api) ---------- */
#palaute{margin-top:42px}
.comm-sub b{color:var(--ink)}
.arvio-form{background:var(--card);border:2px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:20px;margin-bottom:20px}
.q-label{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink);font-size:1.02rem;margin:14px 0 9px}
.q-label:first-child{margin-top:0}
.q-label .opt{font-family:'Nunito',sans-serif;font-size:.78rem;color:var(--mut);font-weight:700}
.feel-row{display:flex;gap:8px;flex-wrap:wrap}
.feel{display:flex;flex-direction:column;align-items:center;gap:3px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:9px 12px;cursor:pointer;font-family:'Nunito',sans-serif;font-weight:800;font-size:.74rem;color:var(--mut);min-width:86px;transition:transform .15s cubic-bezier(.3,1.5,.4,1),border-color .15s,background .15s}
.feel .fe{font-size:1.5rem;line-height:1;filter:grayscale(.55);transition:filter .15s,transform .2s cubic-bezier(.3,1.6,.4,1)}
.feel:hover{border-color:var(--blue);transform:translateY(-2px)}
.feel.on{background:var(--gold-soft);border-color:var(--ink);color:var(--ink);box-shadow:0 2px 0 var(--ink)}
.feel.on .fe{filter:none;transform:scale(1.22) rotate(-6deg)}
.claim-row{display:flex;gap:9px;flex-wrap:wrap}
.claim{font-family:'Nunito',sans-serif;font-size:.88rem;font-weight:800;border:2px solid var(--line);background:#fff;color:var(--body);border-radius:999px;padding:8px 16px;cursor:pointer;transition:border-color .15s,background .15s,transform .15s}
.claim:hover{border-color:var(--blue)}
.claim:active{transform:scale(.94)}
.claim.on{background:var(--blue);border-color:var(--ink);color:#fff;box-shadow:0 2px 0 var(--ink)}
.claim.on::before{content:"✓ "}
.arvio-form input,.arvio-form textarea{width:100%;border:2px solid var(--line);border-radius:12px;padding:11px 13px;font-family:'Nunito',sans-serif;font-size:.95rem;font-weight:600;color:var(--ink);background:#fff}
.arvio-form input{margin-top:16px}
.arvio-form input::placeholder,.arvio-form textarea::placeholder{color:#9DAAC5}
.arvio-form input:focus,.arvio-form textarea:focus{outline:none;border-color:var(--blue)}
.arvio-form textarea{margin-top:10px;min-height:94px;resize:vertical;line-height:1.5}
.cf-actions{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:12px;flex-wrap:wrap}
.cf-note{font-size:.76rem;color:var(--mut);font-weight:600;max-width:340px}
.a-err{display:none;background:#FDECEA;border:2px solid var(--warn);color:var(--warn);border-radius:12px;padding:10px 14px;font-weight:700;font-size:.88rem;margin-top:12px}
.a-thanks{background:var(--card);border:2px solid var(--ok);border-radius:var(--r);box-shadow:var(--shadow);padding:20px;margin-bottom:20px;font-weight:700;color:var(--ink)}
.a-thanks .big{font-size:1.6rem;margin-right:8px;vertical-align:-3px}
/* aggregate summary */
.agg{background:var(--card);border:2px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:18px 20px;margin-bottom:16px;display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.agg .a-emo{font-size:2.4rem;line-height:1}
.agg .a-num{font-family:'Baloo 2',sans-serif;font-weight:600;color:var(--ink);font-size:1.5rem}
.agg .a-num small{font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--mut);display:block;font-weight:500}
.agg-claims{display:flex;gap:8px;flex-wrap:wrap}
.agg-claims span{font-size:.78rem;font-weight:800;background:var(--blue-soft);border:1.5px solid var(--line);border-radius:99px;padding:4px 12px;color:var(--ink)}
/* review list */
.comment-list{display:flex;flex-direction:column;gap:12px}
.comment{background:var(--card);border:2px solid var(--line);border-radius:14px;padding:14px 16px;animation:fadeUp .4s cubic-bezier(.2,.7,.2,1) both}
.c-head{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:5px}
.c-name{font-weight:800;color:var(--ink)}
.c-name .c-emo{font-size:1.05rem;margin-right:6px;vertical-align:-2px}
.c-date{font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--mut);white-space:nowrap}
.c-text{font-size:.94rem;font-weight:600;white-space:pre-wrap;word-break:break-word}
.c-empty{color:var(--mut);font-weight:700;padding:18px;text-align:center;background:var(--blue-soft);border-radius:12px}
/* ranking-card button group (all same size, 2-up grid) */
.rank-btns{display:grid;grid-template-columns:1fr 1fr;gap:8px;width:100%;min-width:250px;max-width:310px}
.rank-btns .btn{text-align:center;padding:10px 8px;font-size:.82rem;white-space:nowrap}
.rank-btns .wide{grid-column:1/-1}
.cbtn .cc{font-family:'IBM Plex Mono',monospace;font-size:.72rem;color:var(--mut);font-weight:600}
.cbtn .cc:not(:empty)::before{content:"("}
.cbtn .cc:not(:empty)::after{content:")"}
@media(max-width:700px){.rank-btns{max-width:none}}
/* ---------- mobile ---------- */
@media(max-width:720px){
  .wrap{padding:0 16px}
  header.site .wrap{flex-wrap:wrap;height:auto;padding:9px 16px 8px;gap:5px 16px}
  .brand{font-size:1.1rem}
  .brand img{width:46px;height:46px}
  /* No overflow-x here: it would clip the category dropdown panel. The nav wraps to
     a second line on narrow screens instead of clipping the last link. */
  nav.main{margin-left:0;width:100%;gap:6px 14px;font-size:.86rem;flex-wrap:wrap}
  nav.main a,.navdd-btn{white-space:nowrap;padding:2px 0}
  .navdd-panel{right:auto;left:0;min-width:min(250px,calc(100vw - 32px))}
  .demo-ribbon{font-size:.7rem;padding:5px 10px}
  .hero{padding:34px 0 44px}
  .hero-logo{width:min(250px,64vw);height:auto;margin:0 auto 16px;display:block}
  .hero h1{text-align:center}
  .hero p.lead{text-align:center;margin-left:auto;margin-right:auto}
  .hero-stats{justify-content:center}
  .sp-search{max-width:none}
  header.site .wrap{flex-wrap:wrap;height:auto;min-height:60px;padding-top:8px;padding-bottom:8px;gap:8px 16px}
  nav.main{gap:6px 14px;flex-wrap:wrap;font-size:.88rem}
  .top-grid{grid-template-columns:1fr}
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

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Nunito:wght@400;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

APP_JS = r"""
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Category dropdown. Click to toggle (works on touch); closes on outside click or Esc.
  var dd = document.getElementById('navdd');
  if (dd) {
    var btn = dd.querySelector('.navdd-btn');
    var setOpen = function(open){
      dd.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    btn.addEventListener('click', function(e){
      e.stopPropagation();
      setOpen(!dd.classList.contains('open'));
    });
    document.addEventListener('click', function(e){
      if (!dd.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape') setOpen(false);
    });
  }

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

  // ---- Palaute: "Anna oma arvio" — questionnaire stored via the palaute-API (D1)
  var API = (location.hostname === 'suomenparas.antonjalonen.fi')
    ? '/api'
    : 'https://suomenparas-palaute.anton-jalonen.workers.dev/api';
  var FEEL_EMO = {1:'😠',2:'🙁',3:'😐',4:'🙂',5:'😀'};
  var FEEL_TXT = {1:'En käyttäisi enää',2:'Huono',3:'Ok',4:'Hyvä',5:'Erinomainen'};
  function esc(s){ return String(s).replace(/[&<>"]/g, function(m){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]; }); }

  var pal = document.getElementById('palaute');
  if (pal) {
    var vertical = pal.dataset.vertical, slug = pal.dataset.slug;
    var DONE_KEY = 'sp_arvio_' + vertical + '_' + slug;
    var form = document.getElementById('aform');
    var fiilis = 0, claims = {};

    pal.querySelectorAll('.feel').forEach(function(b){
      b.addEventListener('click', function(){
        fiilis = parseInt(b.dataset.v, 10);
        pal.querySelectorAll('.feel').forEach(function(x){
          x.classList.toggle('on', x === b);
          x.setAttribute('aria-checked', x === b ? 'true' : 'false');
        });
      });
    });
    pal.querySelectorAll('.claim').forEach(function(b){
      b.addEventListener('click', function(){
        var on = !b.classList.contains('on');
        b.classList.toggle('on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        claims[b.dataset.k] = on;
      });
    });

    function showThanks(msg){
      form.outerHTML = '<div class="a-thanks"><span class="big">🙏</span>' + esc(msg) + '</div>';
    }
    function showErr(msg){
      var el = document.getElementById('aerr');
      el.textContent = msg;
      el.style.display = 'block';
    }
    if (localStorage.getItem(DONE_KEY) === '1') {
      showThanks('Kiitos — olet jo arvioinut tämän yrityksen tällä laitteella.');
    } else {
      form.addEventListener('submit', function(e){
        e.preventDefault();
        if (!fiilis) { showErr('Valitse ensin, millainen kokemuksesi oli.'); return; }
        var payload = {
          vertical: vertical, slug: slug, fiilis: fiilis,
          luotettava: !!claims.luotettava, hintansa: !!claims.hintansa,
          suosittelisin: !!claims.suosittelisin, uudelleen: !!claims.uudelleen,
          nimi: document.getElementById('animi').value.trim().slice(0,40),
          teksti: document.getElementById('ateksti').value.trim().slice(0,600)
        };
        var btn = form.querySelector('button[type=submit]');
        btn.disabled = true;
        fetch(API + '/arvio', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)})
          .then(function(r){ return r.json().then(function(d){ return {ok: r.ok, status: r.status, d: d}; }); })
          .then(function(res){
            if (res.ok || res.status === 409) {
              localStorage.setItem(DONE_KEY, '1');
              showThanks(res.d.message || 'Kiitos! Arviosi näkyy sivulla tarkistuksen jälkeen.');
            } else {
              btn.disabled = false;
              showErr('Lähetys epäonnistui — yritä hetken päästä uudelleen.');
            }
          })
          .catch(function(){
            btn.disabled = false;
            showErr('Lähetys epäonnistui — tarkista verkkoyhteys ja yritä uudelleen.');
          });
      });
    }

    // load approved aggregates + reviews
    fetch(API + '/arvio?vertical=' + vertical + '&slug=' + slug)
      .then(function(r){ return r.json(); })
      .then(function(d){
        var list = document.getElementById('alist');
        if (d.n > 0) {
          var emo = FEEL_EMO[Math.round(d.fiilis_avg)] || '😐';
          var chips = [
            ['luotettava','Luotettava'], ['hintansa','Hintansa arvoinen'],
            ['suosittelisin','Suosittelisin'], ['uudelleen','Käyttäisin uudelleen']
          ].map(function(c){ return '<span>' + c[1] + ' · ' + d.vaitteet[c[0]] + '/' + d.n + '</span>'; }).join('');
          document.getElementById('agg').innerHTML =
            '<span class="a-emo">' + emo + '</span>' +
            '<span class="a-num">' + String(d.fiilis_avg).replace('.', ',') + ' / 5' +
            '<small>' + d.n + (d.n === 1 ? ' arvio' : ' arviota') + '</small></span>' +
            '<span class="agg-claims">' + chips + '</span>';
          document.getElementById('agg').hidden = false;
        }
        if (d.arviot && d.arviot.length) {
          list.innerHTML = d.arviot.map(function(c){
            return '<div class="comment"><div class="c-head"><span class="c-name"><span class="c-emo">' +
              (FEEL_EMO[c.fiilis] || '') + '</span>' + esc(c.nimi || 'Nimetön') +
              '</span><span class="c-date">' + esc(c.pvm ? c.pvm.split('-').reverse().join('.') : '') + '</span></div>' +
              '<p class="c-text">' + esc(c.teksti) + '</p></div>';
          }).join('');
        } else {
          list.innerHTML = '<div class="c-empty">Ei vielä julkaistuja arvioita — ole ensimmäinen ja jaa kokemuksesi.</div>';
        }
      })
      .catch(function(){ /* api unreachable — the form still explains itself */ });
  }

  // Ranking pages: fill review counts into the 💬 icons
  var ranking = document.getElementById('ranking');
  if (ranking && ranking.dataset.vertical) {
    fetch(API + '/counts?vertical=' + ranking.dataset.vertical)
      .then(function(r){ return r.json(); })
      .then(function(counts){
        ranking.querySelectorAll('.cbtn').forEach(function(a){
          var n = counts[a.dataset.slug];
          if (n) a.querySelector('.cc').textContent = n;
        });
      })
      .catch(function(){});
  }
})();
"""

def page(title, desc, body, root="", active=""):
    def on(k):
        return ' class="on"' if k == active else ""
    # The front page shows the big pulsing hero logo, so its header is text-only —
    # one logo per page. Subpages keep the small header logo.
    brand_img = "" if root == "" else (
        f'<img src="{root}assets/logo-200.png?v=3" alt="Suomen Paras -logo" width="58" height="58">')
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
<link rel="stylesheet" href="{root}assets/style.css?v=20">
<script src="{root}assets/app.js?v=20" defer></script>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{root}">{brand_img}<span>SuomenParas<span class="tm">.com</span></span></a>
    <nav class="main">
      <a href="{root}"{on('etusivu')}>Etusivu</a>
      <a href="{root}kategoriat/"{on('kategoriat')}>Kaikki kategoriat</a>
      <a href="{root}metodologia/"{on('metodologia')}>Näin pisteytämme</a>
      <a href="{root}sertifikaatti/"{on('sertifikaatti')}>Sertifikaatti</a>
      <a href="{root}yhteiso/"{on('yhteiso')}>Liity mukaan</a>
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
        <p>{"".join(f'<a href="{root}{v["slug"]}/">{esc(v["nimi"])}</a><br>' for v in VERTICALS)}<a href="{root}kategoriat/">Kaikki kategoriat</a><br><a href="{root}metodologia/">Pisteytysmetodologia</a></p>
      </div>
      <div>
        <h4>Score {SCORE_VERSION}</h4>
        <p class="mono">Päivitetty {UPDATED}<br>{len(ALL_COMPANIES)} palvelua pisteytetty<br>{len(VERTICALS)} kategoriaa live</p>
      </div>
    </div>
    <p class="fine">Tämä on Suomen Paras -palvelun esittelyversio (demo). Pisteet perustuvat julkisiin lähteisiin {UPDATED}: yritysten omat verkkosivut, viralliset rekisterit ja tekniset mittaukset. Emme anna sijoitus-, laina- tai muuta talousneuvontaa, vaan vertailu on informatiivinen. Sivusto voi tulevaisuudessa sisältää affiliate-linkkejä, jotka eivät koskaan vaikuta sijoituksiin. Virheen huomatessasi: korjaamme datan seuraavassa päivityksessä.</p>
    <div class="foot-bottom">
      <a class="btn" href="{root}meista/">Meistä</a>
      <span class="oy">© Suomen Paras Oy 2026</span>
    </div>
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

def rank_card(c, pos, root, vslug):
    m = f"m{pos}" if pos <= 3 else ""
    top_strength = c["vahvuudet"][0] if c["vahvuudet"] else ""
    dataattrs = " ".join(
        f'data-{k}="{(c["pillars"][k] if c["pillars"][k] is not None else 0)}"'
        for k in ["digitaalinen", "lapinakyvyys", "tavoitettavuus", "ai_laatu"]
    )
    ylabel = '<span class="badge-yl">SUOMEN PARAS 2026</span>' if pos == 1 else ""
    return f"""
<article class="rank-card {m}" data-score="{c['score'] or 0}" {dataattrs}>
  <div class="medal">{pos}</div>
  <div class="rank-main">
    <h3><a href="{root}yritys/{vslug}/{c['slug']}/">{esc(c['nimi'])}</a>{ylabel}</h3>
    <p class="rank-meta">{esc(c['domain'])} · {esc(c['omistaja'])}</p>
    {pillar_bars(c)}
    <p class="rank-strength"><b>+</b> {esc(top_strength)}</p>
  </div>
  <div class="rank-side">
    {stamp(c['score'], gold=(pos == 1))}
    <div class="rank-btns">
      <a class="btn" href="https://{c['domain']}" rel="nofollow noopener" target="_blank">Siirry palveluun</a>
      <a class="btn ghost cbtn" data-slug="{c['slug']}" href="{root}yritys/{vslug}/{c['slug']}/#palaute" title="Lue arviot ja anna palautetta">💬 Anna palautetta <span class="cc"></span></a>
      <a class="btn ghost wide" href="{root}yritys/{vslug}/{c['slug']}/">Näin pisteet syntyvät</a>
    </div>
  </div>
</article>"""

def receipt(title, weight, subtotal, rows, has_quote=False):
    trs = []
    for r in rows:
        # Evidence is rendered as a labelled OBSERVATION, not a quotation. Some
        # strings are verbatim page text, but others summarise what a visitor sees
        # — or record an absence, which cannot be quoted at all. Wrapping those in
        # quote marks would attribute our words to the company.
        q = f'<div class="quote"><span class="qlab">HAVAINTO</span>{esc(r["quote"])}</div>' if r.get("quote") else ""
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
    flagship = VERTICALS[0]
    top = flagship["yritykset"][:5]
    rows = []
    for i, c in enumerate(top, 1):
        g = " gold" if i == 1 else ""
        sc = f"{c['score']:.1f}".replace(".", ",")
        rows.append(f'<div class="board-row{g}"><span class="pos">{i}</span><span class="nm">{esc(c["nimi"])}</span><span class="dots"></span><span class="sc">{sc}</span></div>')

    # The hero board was always meant to showcase more than the flagship (its
    # lb-* ids exist for live updates) — feed it every live vertical and rotate.
    lb_data = json.dumps([
        {"n": v["nimi"], "s": v["slug"], "u": v["updated"],
         "top": [[c["nimi"], round(c["score"], 1)] for c in v["yritykset"][:5]]}
        for v in VERTICALS
    ], ensure_ascii=False)

    # Search index: every category and every scored company. A company owner must be
    # able to find their own row (name + score + link) straight from the front page.
    search_index = json.dumps(
        [{"t": "k", "n": v["nimi"], "u": f"{v['slug']}/"} for v in VERTICALS] +
        [{"t": "y", "n": c["nimi"], "k": v["nimi"], "sc": round(c["score"], 1),
          "u": f"yritys/{v['slug']}/{c['slug']}/"}
         for v in VERTICALS for c in v["yritykset"]],
        ensure_ascii=False)

    def mini_board(v):
        rws = ""
        for i, c in enumerate(v["yritykset"][:3], 1):
            sc = f"{c['score']:.1f}".replace(".", ",")
            g = " gold" if i == 1 else ""
            rws += (f'<div class="tb-row{g}"><span class="pos">{i}</span>'
                    f'<span class="nm">{esc(c["nimi"])}</span><span class="dots"></span>'
                    f'<span class="sc">{sc}</span></div>')
        return (f'<a class="top-board" href="{v["slug"]}/">'
                f'<div class="tb-head">{esc(v["nimi"])}<span class="tb-n">{len(v["yritykset"])} vertailtua</span></div>'
                f'{rws}<div class="tb-foot">Koko vertailu →</div></a>')

    # Front page shows only the most-searched categories' podiums — the full list
    # lives behind Kaikki kategoriat and the search box covers everything else.
    HAETUIMMAT = ["lainavertailu", "vakuutukset", "sahkosopimukset",
                  "laajakaista", "pankit", "puhelinliittymat"]
    by_slug = {v["slug"]: v for v in VERTICALS}
    top_boards = "".join(mini_board(by_slug[s]) for s in HAETUIMMAT if s in by_slug)

    steps = """
<div class="steps">
  <div class="step"><span class="k">01 · KERUU</span><h3>Data kerätään automaattisesti</h3><p>Julkiset lähteet: yrityksen oma verkkosivu, viralliset rekisterit ja tekniset mittaukset. Sama prosessi jokaiselle, kukaan ei täytä lomakkeita.</p></div>
  <div class="step"><span class="k">02 · PISTEYTYS</span><h3>Sama kaava kaikille</h3><p>Suomen Paras Score {v} laskee neljä pilaria dokumentoiduilla painoilla. Kaava on julkinen ja deterministinen: sama data antaa aina saman tuloksen.</p></div>
  <div class="step"><span class="k">03 · KUITTI</span><h3>Jokainen piste perustellaan</h3><p>Jokaisen yrityksen profiililta näet mittari mittarilta, mistä pisteet tulevat — lähteineen ja havaintoineen. Sijoitusta ei voi ostaa.</p></div>
</div>""".replace("{v}", SCORE_VERSION)

    live_tiles = "".join(
        f'<a class="cat-tile live-cat" href="{v["slug"]}/">{esc(v["nimi"])} <span class="st">LIVE</span></a>'
        for v in VERTICALS
    )

    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <img class="hero-logo" src="assets/logo-480.png?v=3" alt="Suomen Paras" width="184" height="184">
      <h1>Löydä luotettavin, <em>vertaa läpinäkyvästi</em></h1>
      <p class="lead">Hyvä diili ei ole sattumaa: pisteytämme suomalaiset palvelut mitattavalla datalla, samalla kaavalla ja julkisin perustein. Näet jokaisen pisteen alkuperän.</p>
      <div class="hero-stats">
        <div class="hero-stat"><b>{len(ALL_COMPANIES)}</b><span>palvelua pisteytetty</span></div>
        <div class="hero-stat"><b>{LIVE_COUNT}</b><span>kategoriaa live</span></div>
        <div class="hero-stat"><b>{TOTAL_CATS}</b><span>kategoriaa suunnitteilla</span></div>
      </div>
    </div>
    <div class="board-wrap">
      <div class="board" id="liveboard">
        <div class="board-head"><span class="cat" id="lb-cat">{esc(flagship['nimi'])}</span><span class="live"><span class="live-dot"></span><span id="lb-status">TOP 5 · {flagship['updated']}</span></span></div>
        <div id="lb-body">{''.join(rows)}</div>
        <div class="board-foot" id="lb-foot"><a href="{flagship['slug']}/">Koko vertailu ja pisteiden perustelut →</a></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2 class="sec">Haetuimpien kategorioiden kärjet</h2>
    <p class="sec-sub">Hae mitä tahansa kategoriaa tai yritystä, tai selaa kuutta haetuinta alta. Loput {LIVE_COUNT} kategoriaa löydät <a href="kategoriat/">kategoriasivulta</a>.</p>
    <div class="sp-search" id="sp-search">
      <svg class="sp-ico" width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true" style="max-width:22px;max-height:22px"><circle cx="10.5" cy="10.5" r="6.5" stroke="currentColor" stroke-width="2.6"/><line x1="15.6" y1="15.6" x2="21" y2="21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>
      <input type="search" id="sp-q" placeholder="Mitä haluat vertailla?" autocomplete="off" aria-label="Hae kategoriaa tai yritystä">
      <button type="button" class="sp-btn" id="sp-go">Hae</button>
      <div class="sp-results" id="sp-results" hidden></div>
    </div>
    <div class="top-grid">{top_boards}</div>
  </div>
</section>

<script>
(function(){{
  var IX = {search_index};
  var q = document.getElementById('sp-q'), box = document.getElementById('sp-results');
  if (!q) return;
  function norm(t){{ return t.toLowerCase().replace(/[äå]/g,'a').replace(/ö/g,'o'); }}
  function fmt(n){{ return n.toFixed(1).replace('.',','); }}
  function render(list){{
    if (!list.length) {{ box.innerHTML = '<div class="sp-empty">Ei osumia. Puuttuuko yrityksesi? <a href="analyysi/">Ota yhteyttä</a>.</div>'; box.hidden = false; return; }}
    box.innerHTML = list.map(function(r){{
      if (r.t === 'k') return '<a class="sp-row" href="' + r.u + '"><span class="sp-tag">Kategoria</span><span class="sp-nm">' + r.n + '</span><span class="sp-go">→</span></a>';
      return '<a class="sp-row" href="' + r.u + '"><span class="sp-tag y">Yritys</span><span class="sp-nm">' + r.n + '<small> · ' + r.k + '</small></span><span class="sp-sc">' + fmt(r.sc) + '</span></a>';
    }}).join('');
    box.hidden = false;
  }}
  q.addEventListener('input', function(){{
    var t = norm(q.value.trim());
    if (t.length < 2) {{ box.hidden = true; return; }}
    var hits = IX.filter(function(r){{ return norm(r.n + ' ' + (r.k || '')).indexOf(t) !== -1; }});
    hits.sort(function(a, b){{
      var an = norm(a.n).indexOf(t) === 0 ? 0 : 1, bn = norm(b.n).indexOf(t) === 0 ? 0 : 1;
      if (an !== bn) return an - bn;
      if (a.t !== b.t) return a.t === 'k' ? -1 : 1;
      return 0;
    }});
    render(hits.slice(0, 8));
  }});
  function go(){{
    var first = box.querySelector('a.sp-row');
    if (first && !box.hidden) location.href = first.getAttribute('href');
    else q.focus();
  }}
  q.addEventListener('keydown', function(e){{
    if (e.key === 'Enter') go();
    if (e.key === 'Escape') box.hidden = true;
  }});
  document.getElementById('sp-go').addEventListener('click', go);
  document.addEventListener('click', function(e){{
    if (!document.getElementById('sp-search').contains(e.target)) box.hidden = true;
  }});
}})();
</script>

<script>
(function(){{
  var DATA = {lb_data};
  if (!DATA.length) return;
  var cat=document.getElementById('lb-cat'), st=document.getElementById('lb-status'),
      bd=document.getElementById('lb-body'), ft=document.getElementById('lb-foot'),
      board=document.getElementById('liveboard');
  if(!cat||!bd) return;
  var i=0;
  function fmt(n){{return n.toFixed(1).replace('.',',');}}
  function show(k){{
    var v=DATA[k];
    cat.textContent=v.n;
    st.textContent='TOP '+v.top.length+' · '+v.u;
    var h='';
    for(var j=0;j<v.top.length;j++){{
      h+='<div class="board-row'+(j===0?' gold':'')+'"><span class="pos">'+(j+1)+'</span><span class="nm">'+v.top[j][0]+'</span><span class="dots"></span><span class="sc">'+fmt(v.top[j][1])+'</span></div>';
    }}
    bd.innerHTML=h;
    if(ft) ft.innerHTML='<a href="'+v.s+'/">Koko vertailu ja pisteiden perustelut →</a>';
  }}
  setInterval(function(){{
    i=(i+1)%DATA.length;
    board.classList.add('lb-fade');
    setTimeout(function(){{ show(i); board.classList.remove('lb-fade'); }}, 260);
  }}, 6500);
}})();
</script>

<section class="band">
  <div class="wrap">
    <h2 class="sec">Miten Suomen Paras toimii</h2>
    <p class="sec-sub">Perinteiset vertailusivut myyvät sijoituksia. Me tarjoamme vain yhtä asiaa: läpinäkyvää dataa.</p>
    {steps}
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <h2 class="sec">Kategoriat</h2>
    <p class="sec-sub">{LIVE_COUNT} kategoriaa on avattu oikealla datalla. Uusia avataan kuukausittain — tavoite on kattaa kaikki suomalaiset palvelut.</p>
    <div class="cat-grid">
      {live_tiles}
      <span class="cat-tile off">Autokorjaamot <span class="st">TULOSSA</span></span>
      <span class="cat-tile off">Autopesulat <span class="st">TULOSSA</span></span>
      <a class="cat-tile" href="kategoriat/" style="justify-content:center;background:var(--ink);color:#fff">Kaikki {TOTAL_CATS} kategoriaa →</a>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="b2b light">
      <h3>Liity Suomen Paras -perheeseen</h3>
      <p>Suomen Paras rakentuu lukijoiden kanssa: ehdota seuraavia kategorioita, bongaa virheitä ja kerro mikä toimii. Jokainen palaute luetaan, ja parhaat ehdotukset näkyvät suoraan seuraavissa päivityksissä.</p>
      <a class="btn" href="yhteiso/">Liity mukaan ja anna palautetta</a>
      <small>Palaute ei koskaan vaikuta yritysten pisteisiin.</small>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="b2b">
      <h3>Yrittäjä: haluatko nousta listalla?</h3>
      <p>Sijoitusta ei voi ostaa meiltä — eikä keneltäkään. Mutta voit pyytää analyysin, joka näyttää täsmälleen mitkä mittarit painavat sijoitustasi alas ja miten korjaat ne. Kun mittarit paranevat, sijoitus nousee seuraavassa päivityksessä — ansaitusti. Analyysi on avausvaiheessa maksuton.</p>
      <p>Eikö yrityksesi löydy listalta, vaikka sen pitäisi olla siellä? Ota yhteyttä, niin otamme yrityksesi mukaan seuraavaan mittauskierrokseen.</p>
      <a class="btn" href="analyysi/">Pyydä maksuton analyysi</a>
      <small>Analyysi ei koskaan muuta pisteitä suoraan. Premium-näkyvyys ei vaikuta sijoituksiin.</small>
    </div>
  </div>
</section>

"""
    return page("Suomen Paras | Suomen läpinäkyvin vertailupalvelu",
                "Pisteytämme suomalaiset palvelut mitattavalla datalla. Lainavertailu, sähkösopimukset ja sadat muut kategoriat yhdellä läpinäkyvällä Scorella.",
                body, root="", active="")

def build_vertical(v):
    cs = v["yritykset"]
    cards = "".join(rank_card(c, i, "../", v["slug"]) for i, c in enumerate(cs, 1))
    lead = v["lead"].replace("{n}", str(len(cs))).replace("{m}", str(v["mittarit"]))
    notes = "".join(f'<p class="note">{n}</p>' for n in v["notes"])

    # Category guide (dad's structure 21.7.2026): short intro ABOVE the table so the
    # ranking stays the hook; the deep guide + expert tips + FAQ (with FAQPage
    # schema for search engines) BELOW it.
    opas = v.get("opas") or {}
    opas_intro = f'<p class="opas-intro">{opas["johdanto"]}</p>' if opas.get("johdanto") else ""
    opas_body = ""
    if opas:
        import json as _json
        parts = ['<section class="opas" id="opas"><h2 class="sec">Vertailuopas</h2>']
        if opas.get("huomioita"):
            parts.append('<h3>Mitä vertailussa kannattaa huomioida</h3><ul>')
            parts += [f"<li>{h}</li>" for h in opas["huomioita"]]
            parts.append("</ul>")
        parts.append('<h3>Miten Suomen Paras arvioi ja pisteyttää</h3>'
                     '<p>Jokainen yritys mitataan samalla julkisella kaavalla neljästä pilarista: '
                     'tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Sijoitusta ei '
                     'voi ostaa, ja jokaisen pisteen alkuperän näet yrityksen profiilista. '
                     '<a href="../metodologia/">Lue koko metodologia →</a></p>')
        if opas.get("vinkit"):
            parts.append('<h3>Asiantuntijan vinkit</h3><ul>')
            parts += [f"<li>{h}</li>" for h in opas["vinkit"]]
            parts.append("</ul>")
        if opas.get("ukk"):
            parts.append('<h3>Usein kysytyt kysymykset</h3>')
            for qa in opas["ukk"]:
                parts.append(f'<details class="ukk"><summary>{qa["q"]}</summary><p>{qa["a"]}</p></details>')
            faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
                      "mainEntity": [{"@type": "Question", "name": qa["q"],
                                      "acceptedAnswer": {"@type": "Answer", "text": qa["a"]}}
                                     for qa in opas["ukk"]]}
            parts.append('<script type="application/ld+json">' +
                         _json.dumps(faq_ld, ensure_ascii=False) + "</script>")
        parts.append("</section>")
        opas_body = "".join(parts)
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>{esc(v['nimi'])}</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>{esc(v['h1'])}</h1>
    <p class="lead">{lead}</p>
    <div class="meta-row">
      <span class="upd">Mitattu {v['updated']} · Score {SCORE_VERSION}</span>
      <a class="count-pill" href="../metodologia/">Miten pisteet lasketaan →</a>
    </div>
    {opas_intro}
  </div>

  <div class="chips" role="tablist" aria-label="Järjestä ranking">
    <button class="chip on" data-key="score">Paras kokonaisuus</button>
    <button class="chip" data-key="lapinakyvyys">Läpinäkyvin</button>
    <button class="chip" data-key="digitaalinen">Paras digitaalinen laatu</button>
    <button class="chip" data-key="tavoitettavuus">Paras tavoitettavuus</button>
  </div>

  <div id="ranking" data-vertical="{v['slug']}">{cards}</div>

  <p class="note"><b>Lue pisteet oikein:</b> tämän demon AI-ekstraktio ei ole täysin toistettava — mittasimme kolme yritystä kahdesti ja ero oli jopa ±15 pistettä (<a href="../metodologia/">selitys metodologiassa</a>). Käytä pisteitä suuruusluokkana, älä tarkkana paremmuusjärjestyksenä: muutaman pisteen ero on kohinaa, mutta iso ero (esim. hinta julkisesti vs. kirjautumisen takana) on todellinen.</p>
  {notes}
  {opas_body}

  <div class="b2b">
    <h3>Oletko listalla ja haluaisit korkeammalle?</h3>
    <p>Jokainen menetetty piste on dokumentoitu profiilissasi. Analyysimme priorisoi korjaukset vaikutuksen mukaan: mitkä toimet nostavat pisteitäsi eniten seuraavaan päivitykseen mennessä. Analyysi on avausvaiheessa maksuton.</p>
    <p>Eikö yrityksesi löydy listalta, vaikka sen pitäisi olla siellä? Ota yhteyttä, niin otamme yrityksesi mukaan seuraavaan mittauskierrokseen.</p>
    <a class="btn" href="../analyysi/">Pyydä maksuton analyysi</a>
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
    return page(v["meta_title"], v["meta_desc"], body, root="../", active=v["slug"])

def build_profile(c, pos, v):
    n_total = len(v["yritykset"])
    m = f"m{pos}" if pos <= 3 else ""
    rank_label = {1: "👑 Sija 1 — Suomen Paras 2026", 2: f"🥈 Sija 2 / {n_total}", 3: f"🥉 Sija 3 / {n_total}"}.get(pos, f"Sija {pos} / {n_total}")

    # evidence quotes are baked onto the rows by the scoring engine
    b = c["breakdown"]
    lap_rows = b["lapinakyvyys"]["rivit"]
    dig_rows = b["digitaalinen"]["rivit"]
    receipts = ""
    if dig_rows:
        receipts += receipt("Digitaalinen laatu", 30, c["pillars"]["digitaalinen"], dig_rows)
    else:
        receipts += '<div class="note">Tekninen mittaus ajetaan seuraavassa päivityksessä.</div>'
    receipts += receipt("Läpinäkyvyys", 30, c["pillars"]["lapinakyvyys"], lap_rows)
    receipts += receipt("Tavoitettavuus", 20, c["pillars"]["tavoitettavuus"], b["tavoitettavuus"]["rivit"])
    receipts += receipt("AI-laatuarvio", 20, c["pillars"]["ai_laatu"], b["ai_laatu"]["rivit"])

    vah = "".join(f"<li>{esc(x)}</li>" for x in c["vahvuudet"])
    keh = "".join(f"<li>{esc(x)}</li>" for x in c["kehityskohteet"])

    lh = c.get("lh") or {}
    lcp = f'{lh["lcp_ms"]/1000:.1f} s'.replace(".", ",") if lh.get("lcp_ms") else "–"

    extra = "".join(
        f'<div><span>{esc(f["label"])}</span><b>{esc(f["value"])}</b></div>'
        for f in c.get("facts_extra", [])
    )
    # Most VPNs are foreign and have no Finnish Y-tunnus. Rendering an empty
    # "Y-tunnus –" row would imply they are hiding it; they simply don't have one.
    if c.get("y_tunnus"):
        reg = f"<div><span>Rekisteröity Suomessa (PRH)</span><b>{esc(c['rekisteroity'] or '–')}</b></div>"
        idrows = f'<div><span>Y-tunnus</span><b class="mono">{esc(c["y_tunnus"])}</b></div>{reg}'
    else:
        idrows = '<div><span>Y-tunnus</span><b>Ei suomalaista Y-tunnusta</b></div>'
    facts = f"""
    <div class="p-facts">
      <div><span>Verkkosivu</span><b>{esc(c['domain'])}</b></div>
      <div><span>Omistaja</span><b>{esc(c['omistaja'])}</b></div>
      {idrows}
      {extra}
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
  <p class="crumb"><a href="../../../">Etusivu</a> › <a href="../../../{v['slug']}/">{esc(v['nimi'])}</a> › <b>{esc(c['nimi'])}</b></p>

  <div class="p-hero {m}">
    <div>
      <h1>{esc(c['nimi'])}</h1>
      <p class="rank-meta" style="margin-top:4px">{esc(rank_label)} · {esc(v['nimi'])} · Mitattu {v['updated']}</p>
      {facts}
    </div>
    <div class="stamp-big">
      {stamp(c['score'], gold=(pos == 1))}
      <a class="btn" href="https://{c['domain']}" rel="nofollow noopener" target="_blank">Siirry palveluun</a>
    </div>
  </div>

  <div class="ai-note">
    <span class="tag">AI-YHTEENVETO · CLAUDE HAIKU 4.5 · {v['updated']}</span>
    <p>{esc(c['yhteenveto'])}</p>
  </div>

  <div class="duo">
    <div class="panel plus"><h3>Vahvuudet</h3><ul>{vah}</ul></div>
    <div class="panel minus"><h3>Kehityskohteet</h3><ul>{keh}</ul></div>
  </div>

  <h2 class="sec" style="margin-top:36px">Näin pisteet lasketaan</h2>
  <p class="sec-sub">Jokainen rivi on mitattu {v['updated']} julkisista lähteistä. Sama kaava kaikille — <a href="../../../metodologia/">lue koko metodologia</a>.</p>
  {total_formula}
  {receipts}

  <section id="palaute" data-vertical="{v['slug']}" data-slug="{c['slug']}">
    <h2 class="sec" style="margin-top:36px">Anna palautetta</h2>
    <p class="sec-sub comm-sub">Oletko {esc(c['nimi'])}-palvelun asiakas? Kerro kokemuksesi. <b>Ei vaikuta Suomen Paras Scoreen</b> — pisteet perustuvat vain mitattavaan dataan.</p>
    <div id="agg" class="agg" hidden></div>
    <form class="arvio-form" id="aform">
      <p class="q-label">Millainen kokemuksesi oli?</p>
      <div class="feel-row" role="radiogroup" aria-label="Millainen kokemuksesi oli?">
        <button type="button" class="feel" data-v="5" role="radio" aria-checked="false"><span class="fe">😀</span>Erinomainen</button>
        <button type="button" class="feel" data-v="4" role="radio" aria-checked="false"><span class="fe">🙂</span>Hyvä</button>
        <button type="button" class="feel" data-v="3" role="radio" aria-checked="false"><span class="fe">😐</span>Ok</button>
        <button type="button" class="feel" data-v="2" role="radio" aria-checked="false"><span class="fe">🙁</span>Huono</button>
        <button type="button" class="feel" data-v="1" role="radio" aria-checked="false"><span class="fe">😠</span>En käyttäisi enää</button>
      </div>
      <p class="q-label">Mitkä väittämät pitävät paikkansa? <span class="opt">valitse sopivat</span></p>
      <div class="claim-row">
        <button type="button" class="claim" data-k="luotettava" aria-pressed="false">Luotettava</button>
        <button type="button" class="claim" data-k="hintansa" aria-pressed="false">Hintansa arvoinen</button>
        <button type="button" class="claim" data-k="suosittelisin" aria-pressed="false">Suosittelisin</button>
        <button type="button" class="claim" data-k="uudelleen" aria-pressed="false">Käyttäisin uudelleen</button>
      </div>
      <input type="text" id="animi" maxlength="40" placeholder="Nimesi (valinnainen)" autocomplete="off">
      <textarea id="ateksti" maxlength="600" placeholder="Kerro omin sanoin kokemuksesi {esc(c['nimi'])}-palvelusta… (valinnainen)"></textarea>
      <div class="a-err" id="aerr"></div>
      <div class="cf-actions">
        <span class="cf-note">Arviot tarkistetaan ennen julkaisua. Yksi arvio per yritys. Asiaton sisältö poistetaan.</span>
        <button type="submit" class="btn">Lähetä arvio</button>
      </div>
    </form>
    <div id="alist" class="comment-list"></div>
  </section>

  <div class="b2b">
    <h3>Onko tämä sinun yrityksesi?</h3>
    <p>Yllä näkyy täsmälleen mistä pisteesi tulevat — ja mihin niitä jää saamatta. Analyysimme priorisoi korjaukset: mitkä toimenpiteet nostavat Scorea eniten, ja miten ne toteutetaan. Kun data paranee, sijoitus nousee seuraavassa päivityksessä. Analyysi on avausvaiheessa maksuton.</p>
    <a class="btn" href="../../../analyysi/?yritys={esc(c['nimi'])}">Pyydä maksuton analyysi: {esc(c['nimi'])}</a>
    <small>Analyysi ei muuta pisteitä. Vain mittareiden parantaminen muuttaa.</small>
  </div>
</div>"""
    sc = f"{c['score']:.1f}".replace(".", ",") if c["score"] else "–"
    return page(f"{c['nimi']} — Suomen Paras Score {sc}/100 | {v['nimi']}",
                f"{c['nimi']}: pisteet, vahvuudet ja kehityskohteet. Katso mistä jokainen piste tulee — mittari mittarilta.",
                body, root="../../../", active=v["slug"])

def build_kategoriat():
    groups = []
    for gname, cats in CATEGORY_GROUPS:
        tiles = []
        for cname, slug, _ in cats:
            if slug in LIVE_SLUGS:
                tiles.append(f'<a class="cat-tile live-cat" href="../{slug}/">{esc(cname)} <span class="st">LIVE</span></a>')
            else:
                tiles.append(f'<span class="cat-tile off">{esc(cname)} <span class="st">TULOSSA</span></span>')
        groups.append(f'<div class="cat-group"><h3>{esc(gname)}</h3><div class="cat-grid">{"".join(tiles)}</div></div>')
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Kategoriat</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Kaikki kategoriat</h1>
    <p class="lead">{TOTAL_CATS} kategoriaa suunnitteilla — jokainen pisteytetään samalla julkisella Suomen Paras Score -kaavalla. Avattu tähän mennessä: {esc(", ".join(v["nimi"].lower() for v in VERTICALS))}. Uusia avataan kuukausittain.</p>
    <div class="meta-row"><span class="upd">{LIVE_COUNT} kategoriaa live · {TOTAL_CATS - LIVE_COUNT} tulossa</span></div>
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
        <tr><td><b>Digitaalinen laatu</b></td><td>Suorituskyky (40), saavutettavuus (30), SEO (15), tekniset käytännöt (15) — mobiili</td><td class="src">Tekninen mittaus (mobiili)</td><td class="pts"><b>30 %</b></td></tr>
        <tr><td><b>Läpinäkyvyys</b></td><td>Kategoriakohtaiset kriteerit — sama painoarvo, eri mittarit. Ks. taulukko alla.</td><td class="src">Verkkosivu + AI-ekstraktio</td><td class="pts"><b>30 %</b></td></tr>
        <tr><td><b>Tavoitettavuus</b></td><td>Puhelin (30), sähköposti (15), chat (15), aukioloajat (15), UKK (15), mobiilisovellus (10)</td><td class="src">Verkkosivu + AI-ekstraktio</td><td class="pts"><b>20 %</b></td></tr>
        <tr><td><b>AI-laatuarvio</b></td><td>Tietojen selkeys, hintatietojen löydettävyys, sisällön kattavuus (0–100)</td><td class="src">AI-analyysi</td><td class="pts"><b>20 %</b></td></tr>
      </tbody>
    </table>
  </div>

  <div class="receipt" style="margin-top:26px">
    <div class="receipt-head"><h3>Läpinäkyvyys — kategoriakohtaiset kriteerit <span class="w">· paino 30 %</span></h3><span class="sub">{len(VERTICALS)} kategoriaa</span></div>
    <table class="rows">
      <thead><tr><th>Kategoria</th><th>Mitä läpinäkyvyys tarkoittaa tässä kategoriassa</th><th class="pts">Yhteensä</th></tr></thead>
      <tbody>
        {"".join(f'<tr><td><b>{esc(v["nimi"])}</b></td><td>{esc(v["lapinakyvyys_kriteerit"])}</td><td class="pts"><b>100</b></td></tr>' for v in VERTICALS)}
      </tbody>
    </table>
  </div>
  <p class="note">Kolme muuta pilaria (digitaalinen laatu, tavoitettavuus, AI-laatuarvio) mitataan täsmälleen samoilla mittareilla kategoriasta riippumatta. Vain läpinäkyvyys on kategoriakohtainen — lainanvälittäjän korkoesimerkki ja sähköyhtiön hinnasto eivät ole sama asia, mutta molemmat vastaavat samaan kysymykseen: <b>kertooko yritys hinnan ennen kuin annat tietojasi?</b></p>

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
      <li style="padding-left:0"><b>Jokainen yritys mitataan samalla tavalla.</b> Sama automaattinen prosessi ja sama ohjeistus jokaiselle yritykselle samassa päivityksessä, kukaan ei saa erikoiskohtelua.</li>
      <li style="padding-left:0"><b>Mutta AI-ekstraktio ei ole täysin toistettava — ja se on rehellisyyden vuoksi kerrottava.</b> Mittasimme 16.7.2026 kolme yritystä vahingossa kahdesti samalla mallilla ja samalla ohjeistuksella. Tulokset erosivat: 4–6 mitattua kohtaa per yritys, ja kokonaispisteissä jopa <b>±15 pistettä</b>. Syy: mallin näkemä sivu vaihtelee (evästemuurit, JS-sisältö, 404-sivut, eri alasivut), ja &rdquo;en löytänyt&rdquo; ei ole sama asia kuin &rdquo;ei ole olemassa&rdquo;. Kaava on deterministinen, mutta sen syöte ei vielä ole.</li>
      <li style="padding-left:0"><b>Mitä tämä tarkoittaa lukijalle:</b> pieniä pistemeroja ei pidä lukea paremmuusjärjestyksenä. Alle noin 15 pisteen ero on tässä demossa kohinaa, ei tulosta. Suuret erot (esim. hinta julkisesti vs. kirjautumisen takana) ovat luotettavia. Tuotantoversio vaatii moniajovarmistuksen: sama sivu mitataan useasti ja vain yhtenevä tulos julkaistaan.</li>
      <li style="padding-left:0"><b>”Havainto” on meidän huomiomme, ei yrityksen lainaus.</b> Pisterivien alla näkyvä havainto kertoo, mitä sivustolla oli nähtävissä mittaushetkellä. Se voi olla suora lainaus sivulta tai tiivistys siitä mitä kävijä näkee — usein se kuvaa nimenomaan jonkin tiedon <em>puuttumista</em>, jota ei voi lainata. Emme siksi esitä havaintoja yrityksen omina sanoina.</li>
      <li style="padding-left:0"><b>Virheet korjataan.</b> Jos yritys osoittaa mittausvirheen, korjaamme datan seuraavassa päivityksessä ja merkitsemme korjauksen.</li>
    </ul>
  </div>

  <div class="note" style="margin-top:26px"><b>Demo-huomautus:</b> Tämä on konseptin esittelyversio. Jokaisen kategorian data on kerätty oikeista julkisista lähteistä sen omana mittauspäivänä ({esc(", ".join(f"{v['nimi'].lower()} {v['updated']}" for v in VERTICALS))}), mutta mittaristo on suppeampi kuin tuotantoversiossa (~26 / ~200 mittaria) ja kattaa vain palveluiden julkiset verkkosivut — ei esimerkiksi todellisia lainatarjouksia, vakuutusmaksuja tai pörssisähkön hintakehitystä.</div>
</div>"""
    return page("Näin Suomen Paras Score lasketaan | Suomen Paras",
                "Suomen Paras Score on julkinen ja deterministinen: pilarit, painot, lähteet ja riippumattomuusperiaatteet.",
                body, root="../", active="metodologia")

def build_analyysi():
    opts = "".join(f'<option value="{esc(v["nimi"])}">{esc(v["nimi"])}</option>' for v in VERTICALS)
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Maksuton analyysi</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Pyydä maksuton analyysi</h1>
    <p class="lead">Analyysi näyttää mittari mittarilta, mitkä asiat painavat yrityksesi sijoitusta alas ja miten korjaat ne. Kun mittarit paranevat, sijoitus nousee seuraavassa päivityksessä. Analyysi on avausvaiheessa maksuton.</p>
  </div>

  <div class="panel aform">
    <p class="aform-note">Viesti on valmiiksi kirjoitettu, joten täydennä vain yrityksen tiedot ja lähetä. Lähetä-nappi avaa sähköpostiohjelmasi.</p>
    <label>Yrityksen nimi<input type="text" id="af-yritys" placeholder="Esim. Yritys Oy"></label>
    <label>Kategoria<select id="af-kategoria"><option value="">Valitse kategoria</option>{opts}<option value="Muu">Muu / ei vielä listalla</option></select></label>
    <label>Viesti<textarea id="af-viesti" rows="9"></textarea></label>
    <a class="btn" id="af-send" href="#">Lähetä analyysipyyntö</a>
    <small>Jos nappi ei avaa sähköpostiohjelmaa, lähetä viesti suoraan osoitteeseen <a href="mailto:anton@antonjalonen.fi">anton@antonjalonen.fi</a>.</small>
  </div>

  <div class="b2b">
    <h3>Mitä analyysi sisältää?</h3>
    <p>Käymme läpi yrityksesi julkisen verkkosivun samoilla mittareilla, joilla koko kategoria on pisteytetty: hintojen näkyvyys, sopimusehtojen saatavuus, tavoitettavuus ja tekninen laatu. Saat listan konkreettisia korjauksia vaikutusjärjestyksessä.</p>
    <small>Analyysi ei koskaan muuta pisteitä suoraan. Sijoitusta ei voi ostaa, se ansaitaan.</small>
  </div>
</div>

<script>
(function(){{
  var params = new URLSearchParams(location.search);
  var y = document.getElementById('af-yritys'),
      k = document.getElementById('af-kategoria'),
      m = document.getElementById('af-viesti'),
      s = document.getElementById('af-send');
  if (params.get('yritys')) y.value = params.get('yritys');
  function pohja(){{
    return 'Hei,\\n\\npyydän maksuttoman Suomen Paras -analyysin yrityksellemme.\\n\\n'
      + 'Yritys: ' + (y.value || '') + '\\n'
      + 'Kategoria: ' + (k.value || '') + '\\n\\n'
      + 'Haluamme tietää, mitkä mittarit painavat sijoitustamme alas ja miten korjaamme ne.\\n\\nTerveisin\\n';
  }}
  var muokattu = false;
  m.value = pohja();
  m.addEventListener('input', function(){{ muokattu = true; }});
  function refresh(){{ if (!muokattu) m.value = pohja(); }}
  y.addEventListener('input', refresh);
  k.addEventListener('change', refresh);
  s.addEventListener('click', function(e){{
    e.preventDefault();
    var subject = 'Suomen Paras -analyysi' + (y.value ? ': ' + y.value : '');
    location.href = 'mailto:anton@antonjalonen.fi?subject=' + encodeURIComponent(subject)
      + '&body=' + encodeURIComponent(m.value);
  }});
}})();
</script>"""
    return page("Pyydä maksuton analyysi | Suomen Paras",
                "Pyydä maksuton analyysi: näet mitkä mittarit painavat yrityksesi sijoitusta alas ja miten korjaat ne.",
                body, root="../", active="analyysi")

def build_sertifikaatti():
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Sertifikaatti</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Suomen Paras -sertifikaatti</h1>
    <p class="lead">Merkki, jonka yritys voi ansaita, mutta ei ostaa. Sertifikaatti on tulossa.</p>
    <div class="meta-row"><span class="upd">TULOSSA</span></div>
  </div>

  <div class="steps">
    <div class="step"><span class="k">MIKÄ SE ON</span><h3>Todiste läpinäkyvyydestä</h3><p>Suomen Paras -sertifikaatti myönnetään yritykselle, jonka mitattu Score ylittää kategoriansa vaatimustason. Merkin voi näyttää omalla sivustolla, ja jokainen merkki linkittyy yrityksen julkiseen pisteprofiiliin, josta kuka tahansa voi tarkistaa mihin se perustuu.</p></div>
    <div class="step"><span class="k">MITEN SEN SAA</span><h3>Mittaamalla, ei maksamalla</h3><p>Sertifikaattia ei voi ostaa. Se ansaitaan samalla julkisella pisteytyksellä, jolla koko kategoria on mitattu, ja se päivittyy jokaisen mittauskierroksen mukana. Jos mittarit heikkenevät, merkki poistuu.</p></div>
    <div class="step"><span class="k">MILLOIN</span><h3>Tulossa</h3><p>Sertifikaatti julkaistaan, kun kategorioiden mittaus on vakiintunut. Jos haluat yrityksesi ensimmäisten joukkoon, pyydä maksuton analyysi niin näet jo nyt, missä mittarisi ovat.</p></div>
  </div>

  <div class="b2b">
    <h3>Haluatko olla mukana ensimmäisten joukossa?</h3>
    <p>Pyydä maksuton analyysi, niin näet jo ennen sertifikaatin julkaisua, mitkä mittarit ovat kunnossa ja mitkä vaativat korjausta.</p>
    <a class="btn" href="../analyysi/">Pyydä maksuton analyysi</a>
    <small>Sertifikaattia ei voi ostaa. Sijoitusta ei voi ostaa. Molemmat ansaitaan.</small>
  </div>
</div>"""
    return page("Suomen Paras -sertifikaatti (tulossa) | Suomen Paras",
                "Suomen Paras -sertifikaatti: merkki jonka yritys voi ansaita, mutta ei ostaa. Tulossa.",
                body, root="../", active="sertifikaatti")

def build_yhteiso():
    # Reuses the company-review widget (app.js #palaute) against a reserved
    # vertical/slug pair, so site feedback lands in the same D1 + admin moderation.
    # The claim keys MUST stay luotettava/hintansa/suosittelisin/uudelleen — they are
    # DB columns — only the visible labels differ.
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Liity mukaan</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Liity Suomen Paras -perheeseen</h1>
    <p class="lead">Suomen Paras rakentuu avoimesti ja lukijoiden kanssa. Kerro mitä kategorioita haluat seuraavaksi, mikä sivustossa toimii ja mikä ei. Jokainen palaute luetaan, ja parhaat ehdotukset näkyvät suoraan seuraavissa päivityksissä.</p>
  </div>

  <div class="steps">
    <div class="step"><span class="k">EHDOTA</span><h3>Uudet kategoriat</h3><p>109 kategoriaa on suunnitteilla, ja järjestyksen ratkaisee kysyntä. Kerro mikä vertailu auttaisi juuri sinua, niin nostamme sitä jonossa.</p></div>
    <div class="step"><span class="k">KORJAA</span><h3>Bongasitko virheen?</h3><p>Jos jokin tieto on vanhentunut tai väärin, kerro se. Korjaamme datan seuraavassa päivityksessä ja merkitsemme korjauksen avoimesti sivulle.</p></div>
    <div class="step"><span class="k">VAIKUTA</span><h3>Kehitä palvelua</h3><p>Mikä sivustossa on hyvää, mikä huonoa? Suorat ehdotukset menevät suoraan tekijälle, eivät tikettijonoon.</p></div>
  </div>

  <section id="palaute" data-vertical="suomenparas" data-slug="sivusto">
    <h2 class="sec" style="margin-top:36px">Kerro mitä mieltä olet</h2>
    <p class="sec-sub comm-sub">Palaute koskee Suomen Paras -palvelua itseään, ei mitään listattua yritystä. Julkaistut palautteet näkyvät alla.</p>
    <div id="agg" class="agg" hidden></div>
    <form class="arvio-form" id="aform">
      <p class="q-label">Millainen kokemuksesi sivustosta oli?</p>
      <div class="feel-row" role="radiogroup" aria-label="Millainen kokemuksesi sivustosta oli?">
        <button type="button" class="feel" data-v="5" role="radio" aria-checked="false"><span class="fe">😀</span>Erinomainen</button>
        <button type="button" class="feel" data-v="4" role="radio" aria-checked="false"><span class="fe">🙂</span>Hyvä</button>
        <button type="button" class="feel" data-v="3" role="radio" aria-checked="false"><span class="fe">😐</span>Ok</button>
        <button type="button" class="feel" data-v="2" role="radio" aria-checked="false"><span class="fe">🙁</span>Huono</button>
        <button type="button" class="feel" data-v="1" role="radio" aria-checked="false"><span class="fe">😠</span>En palaisi</button>
      </div>
      <p class="q-label">Mitkä väittämät pitävät paikkansa? <span class="opt">valitse sopivat</span></p>
      <div class="claim-row">
        <button type="button" class="claim" data-k="luotettava" aria-pressed="false">Luotan pisteytykseen</button>
        <button type="button" class="claim" data-k="hintansa" aria-pressed="false">Tiedoista oli hyötyä</button>
        <button type="button" class="claim" data-k="suosittelisin" aria-pressed="false">Suosittelisin kaverille</button>
        <button type="button" class="claim" data-k="uudelleen" aria-pressed="false">Palaan uudelleen</button>
      </div>
      <input type="text" id="animi" maxlength="40" placeholder="Nimesi (valinnainen)" autocomplete="off">
      <textarea id="ateksti" maxlength="600" placeholder="Mitä kategorioita haluaisit seuraavaksi? Mikä toimii, mikä ei? Kerro omin sanoin… (valinnainen)"></textarea>
      <div class="a-err" id="aerr"></div>
      <div class="cf-actions">
        <span class="cf-note">Palautteet tarkistetaan ennen julkaisua. Asiaton sisältö poistetaan.</span>
        <button type="submit" class="btn">Lähetä palaute</button>
      </div>
    </form>
    <div id="alist" class="comment-list"></div>
  </section>

  <div class="b2b">
    <h3>Oletko yrittäjä?</h3>
    <p>Yrityksille perheeseen liittyminen alkaa maksuttomalla analyysilla: näet mittari mittarilta missä sivustosi on nyt ja miten sijoitus nousee. Tulossa oleva Suomen Paras -sertifikaatti myönnetään samalla julkisella datalla.</p>
    <a class="btn" href="../analyysi/">Pyydä maksuton analyysi</a>
    <small>Sijoitusta ei voi ostaa. Palaute ei vaikuta pisteisiin.</small>
  </div>
</div>"""
    return page("Liity Suomen Paras -perheeseen | Suomen Paras",
                "Kerro mitä kategorioita haluat seuraavaksi ja anna palautetta palvelusta. Suomen Paras rakentuu avoimesti.",
                body, root="../", active="yhteiso")

def build_meista():
    body = f"""
<div class="wrap">
  <p class="crumb"><a href="../">Etusivu</a> › <b>Meistä</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>Tarinamme</h1>
    <p class="lead">Suomen Paras syntyi yksinkertaisesta havainnosta: suomalaiset vertailusivut myyvät sijoituksia, eivät totuutta. Me päätimme rakentaa vertailun, jossa jokainen piste voidaan perustella.</p>
  </div>

  <div class="steps">
    <div class="step"><span class="k">MIKSI</span><h3>Hyvä diili ei ole sattumaa</h3><p>Kun etsit lainaa, vakuutusta tai vaikka pakohuonetta, joku on yleensä maksanut siitä, mitä näet ensimmäisenä. Meillä sijoitusta ei voi ostaa: jokainen sijoitus lasketaan julkisella kaavalla julkisesta datasta, ja jokaisen pisteen alkuperän voi tarkistaa yrityksen profiilista.</p></div>
    <div class="step"><span class="k">MITEN</span><h3>Mittaamme, emme mielipiteile</h3><p>Keräämme datan yritysten omilta verkkosivuilta, virallisista rekistereistä ja teknisillä mittauksilla, samalla prosessilla jokaiselle. Tärkein kysymyksemme on aina sama: kerrotaanko hinta ennen kuin luovutat tietosi? Kun löydämme virheen, korjaamme sen ja kerromme siitä avoimesti sivulla.</p></div>
    <div class="step"><span class="k">KUKA</span><h3>Suomen Paras Oy</h3><p>Olemme suomalainen yhtiö, joka rakentaa Suomen läpinäkyvintä vertailupalvelua kategoria kerrallaan. Tavoitteena on kattaa yli sata kategoriaa, ja jokainen niistä avataan oikealla, tarkistetulla datalla, ei koskaan täytelistoilla.</p></div>
  </div>

  <div class="b2b">
    <h3>Haluatko mukaan matkalle?</h3>
    <p>Lukijana voit ehdottaa uusia kategorioita ja antaa palautetta yhteisösivulla. Yrittäjänä pääset alkuun maksuttomalla analyysilla, ja tulossa oleva Suomen Paras -sertifikaatti myönnetään samalla julkisella datalla, jolla kaikki muukin täällä mitataan.</p>
    <a class="btn" href="../yhteiso/">Liity mukaan</a>
    <a class="btn" href="../analyysi/" style="margin-left:10px">Pyydä maksuton analyysi</a>
    <small>Sijoitusta ei voi ostaa. Sitä ei ole koskaan voinut, eikä koskaan voi.</small>
  </div>
</div>"""
    return page("Meistä | Suomen Paras",
                "Suomen Paras Oy:n tarina: vertailu jossa sijoitusta ei voi ostaa, vaan jokainen piste perustellaan julkisella datalla.",
                body, root="../", active="meista")

# ---------------------------------------------------------------- write
def strip_em_dashes(html_text):
    # Site-wide copy rule (18.7.2026, Anton): no em dashes anywhere in published pages.
    # Spaced em dashes read naturally as a comma in Finnish; bare ones become hyphens.
    return html_text.replace(" — ", ", ").replace(" —", ",").replace("— ", "").replace("—", "-")

def w(path, content):
    if path.endswith(".html"):
        content = strip_em_dashes(content)
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

def main():
    w("assets/style.css", CSS)
    w("assets/app.js", APP_JS)
    w("index.html", build_index())
    w("kategoriat/index.html", build_kategoriat())
    w("metodologia/index.html", build_metodologia())
    w("analyysi/index.html", build_analyysi())
    w("sertifikaatti/index.html", build_sertifikaatti())
    w("yhteiso/index.html", build_yhteiso())
    w("meista/index.html", build_meista())
    n = 3
    for v in VERTICALS:
        w(f"{v['slug']}/index.html", build_vertical(v))
        n += 1
        for i, c in enumerate(v["yritykset"], 1):
            w(f"yritys/{v['slug']}/{c['slug']}/index.html", build_profile(c, i, v))
            n += 1
    print(f"OK — {n} pages, {len(VERTICALS)} verticals, {len(ALL_COMPANIES)} companies")

if __name__ == "__main__":
    main()
