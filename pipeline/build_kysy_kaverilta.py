# -*- coding: utf-8 -*-
"""Kysy kaverilta — konseptidemo (29.7.2026).

Antonin konsepti: yhteisokeskustelu kiinni mittausdatassa. Jokainen kysymys on
oma sivunsa, joka linkittyy yritykseen, kategoriaan, kilpailijoihin, tageihin ja
oppaisiin — eli sama linkkiverkko jota konsepti kuvaa.

Tama skripti tuottaa DEMON, ei tuotantoa:
  * vastaukset ovat KEKSITTYJA esimerkkeja ja merkitty sellaisiksi joka sivulla
  * yritysten nimet, pisteet ja kategoriat tulevat oikeasta mittausdatasta
    (data/*.json), jotta linkkiverkon kytkennat nakyvat aidosti
  * kaikki sivut ovat noindex — tama ei saa paatya hakukoneisiin

Aja: python pipeline/build_kysy_kaverilta.py
Katso: http://localhost:8741/kysy-kaverilta/
"""
import json, os, re, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "kysy-kaverilta")
ASSET_V = "23"


def esc(s):
    return html.escape(str(s), quote=True)


def load(vertical):
    p = os.path.join(BASE, "data", f"{vertical}.json")
    return json.load(open(p, encoding="utf-8-sig"))


def slugify(s):
    s = s.lower()
    for a, b in [("ä", "a"), ("ö", "o"), ("å", "a")]:
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)[:70]


# --- demon sisalto -----------------------------------------------------------
# Vastaukset ovat esimerkkeja konseptin havainnollistamiseen. Ne on kirjoitettu
# geneerisiksi eivatka vaita mitaan tarkistamatonta yhtiosta.
KYSYMYKSET = [
    {
        "slug": "onko-dna-valokuitu-hyva",
        "otsikko": "Onko DNA:n valokuitu hyvä?",
        "yritys": "dna", "vertical": "puhelinliittymat",
        "tagit": ["toimitusaika", "asiakaspalvelu", "hinta", "sopimus"],
        "kysyja": "Mikko H.", "aika": "3 päivää sitten", "katselut": 1284,
        "kysymys": ("Muutimme omakotitaloon ja taloyhtiön sijaan pitää nyt itse valita "
                    "operaattori. Onko kenelläkään kokemusta siitä, miten asennus meni ja "
                    "pitikö luvattu nopeus paikkansa?"),
        "tiivistelma": ("Keskustelussa toistuu kaksi asiaa: asennusaikataulu on vaihdellut "
                        "alueittain, ja hinta nousee kampanjakauden jälkeen. Nopeudesta ei "
                        "ole yhtään valitusta. Tiivistelmä on koottu {n} vastauksesta, "
                        "tuorein {p}."),
        "vastaukset": [
            {"nimi": "Jenni K.", "maine": 340, "aika": "3 päivää sitten", "aanet": 42,
             "paras": True,
             "teksti": ("Meillä asennus tuli sovittuna päivänä ja nopeus on ollut se mitä "
                        "luvattiin. Kannattaa katsoa sopimuksesta se kohta, paljonko hinta "
                        "on kampanjan jälkeen — se yllätti meidät.")},
            {"nimi": "Petri L.", "maine": 88, "aika": "2 päivää sitten", "aanet": 17,
             "teksti": ("Omalla kohdallani asennusta siirrettiin kahdesti. Palvelu toimi "
                        "sen jälkeen moitteetta, mutta odotus oli pitkä. Kysy asennusaika "
                        "kirjallisena ennen kuin allekirjoitat.")},
            {"nimi": "Sanna R.", "maine": 512, "aika": "eilen", "aanet": 9,
             "teksti": ("Vertailin kolmea operaattoria ja päädyin tähän hinnan takia. "
                        "Vinkki: pyydä kaikki tarjoukset sähköpostilla, niin näet "
                        "kokonaishinnan 24 kuukaudelta etkä vain kuukausierää.")},
        ],
        "yritysvastaus": ("Kiitos palautteesta. Asennusaikataulut vaihtelevat alueittain "
                          "verkon rakennustilanteen mukaan, ja arvioitu asennusaika näkyy "
                          "tilausvaiheessa osoitteen perusteella."),
        "jatkokysymykset": [
            ("Mitä DNA:n liittymä maksaa kampanjan jälkeen?", "dna", "mita-dna-liittyma-maksaa-kampanjan-jalkeen"),
            ("Miten irtisanon DNA:n liittymän?", "dna", "miten-irtisanon-dna-liittyman"),
            ("Kannattaako valokuitu vai 5G-liittymä?", "dna", "kannattaako-valokuitu-vai-5g"),
        ],
    },
]

TAGIT_KUVAUS = {
    "toimitusaika": "Toimitus- ja asennusaikoja koskevat keskustelut",
    "asiakaspalvelu": "Asiakaspalvelun tavoitettavuus ja vasteajat",
    "hinta": "Hinnat, kampanjahinnat ja kokonaiskustannus",
    "sopimus": "Sopimusehdot, sitoutuminen ja irtisanominen",
    "laskutus": "Laskutus, laskutuslisat ja maksutavat",
    "reklamaatio": "Reklamaatiot ja hyvitykset",
}

# Avoimet keskustelut: naissa ei ole viela vastauksia. Ne nayttavat demossa sen
# tilan, jossa AI on luonut sivun toistuvasta kysymyksesta mutta yhteiso ei ole
# viela ehtinyt vastata — sama URL, sama linkkiverkko, tyhja sisalto.
AVOIMET = [
    ("Mitä DNA:n liittymä maksaa kampanjan jälkeen?", "dna", "mita-dna-liittyma-maksaa-kampanjan-jalkeen",
     ["hinta", "sopimus"], "puhelinliittymat"),
    ("Miten irtisanon DNA:n liittymän?", "dna", "miten-irtisanon-dna-liittyman",
     ["sopimus", "asiakaspalvelu"], "puhelinliittymat"),
    ("Kannattaako valokuitu vai 5G-liittymä?", "dna", "kannattaako-valokuitu-vai-5g",
     ["hinta", "toimitusaika"], "puhelinliittymat"),
    ("Miten Telian chat toimii iltaisin?", "telia", "miten-telian-chat-toimii-iltaisin",
     ["asiakaspalvelu"], "puhelinliittymat"),
    ("Saako Elisan asiakaspalvelun kiinni puhelimella?", "elisa", "saako-elisan-asiakaspalvelun-kiinni",
     ["asiakaspalvelu"], "puhelinliittymat"),
    ("Vastaako Moi Mobiili sähköposteihin?", "moi", "vastaako-moi-mobiili-sahkoposteihin",
     ["asiakaspalvelu", "laskutus"], "puhelinliittymat"),
    ("Miksi laskussa on laskutuslisä?", "telia", "miksi-laskussa-on-laskutuslisa",
     ["laskutus", "hinta"], "puhelinliittymat"),
    ("Miten teen reklamaation liittymästä?", "elisa", "miten-teen-reklamaation-liittymasta",
     ["reklamaatio", "asiakaspalvelu"], "puhelinliittymat"),
]


def kaikki_kysymykset():
    """(otsikko, yritys, slug, tagit, vertical, vastauksia, katselut)"""
    out = [(q["otsikko"], q["yritys"], q["slug"], q["tagit"], q["vertical"],
            len(q["vastaukset"]), q["katselut"]) for q in KYSYMYKSET]
    out += [(t, y, s, tg, v, 0, 0) for t, y, s, tg, v in AVOIMET]
    return out


def header(root, active=""):
    def a(href, label, key):
        on = ' class="on"' if key == active else ""
        return f'<a href="{root}{href}"{on}>{label}</a>'
    return f"""<header class="site">
  <div class="wrap">
    <a class="brand" href="{root}../"><img src="{root}../assets/logo-200.png?v=3" alt="Suomen Paras -logo" width="58" height="58"><span>SuomenParas<span class="tm">.com</span></span></a>
    <nav class="main">
      <a href="{root}../">Etusivu</a>
      <a href="{root}../kategoriat/">Kaikki kategoriat</a>
      <a href="{root}../uutishuone/">Uutishuone</a>
      {a("", "Kysy kaverilta", "kysy")}
      <a href="{root}../luottamus/">Näin pisteytämme</a>
      <a href="{root}../sertifikaatti/">Sertifikaatti</a>
      <a href="{root}../yhteiso/">Liity mukaan</a>
    </nav>
  </div>
</header>"""


def page(title, desc, body, depth, active="kysy", jsonld=None, root_to_site="../"):
    """depth = kuinka monta tasoa kysy-kaverilta-juuresta alaspain."""
    up = "../" * depth              # takaisin kysy-kaverilta-juureen
    site = up + root_to_site        # sivuston juureen
    ld = f'\n<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="article">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Nunito:wght@400;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="{site}assets/favicon.png">
<link rel="stylesheet" href="{site}assets/style.css?v={ASSET_V}">
<link rel="stylesheet" href="{up}demo.css?v=1">{ld}
</head>
<body>
{header(up, active)}
<div class="demobar"><b>Konseptidemo.</b> Yritysten nimet, pisteet ja kategoriat ovat oikeaa mittausdataa — <b>vastaukset ja äänimäärät ovat keksittyjä esimerkkejä</b>, eivät oikeita käyttäjäkokemuksia. Mitään ei ole julkaistu.</div>
{body}
<script src="{up}demo.js?v=1" defer></script>
</body>
</html>"""


# --- osat --------------------------------------------------------------------
def linkkiverkko(yritys, vert, kilpailijat, tagit, up):
    """Konseptin ydin: yksi keskustelu tuottaa kymmeniä sisäisiä linkkejä."""
    site = up + "../"
    rivit = [
        ("Yritys", [(yritys["nimi"], f'{site}yritys/{vert["slug"]}/{yritys["slug"]}/')]),
        ("Kategoria", [(vert["nimi"], f'{site}{vert["slug"]}/')]),
        ("Pisteet", [(f'{yritys["nimi"]} {str(yritys["score"]).replace(".", ",")} / 100',
                      f'{site}yritys/{vert["slug"]}/{yritys["slug"]}/')]),
        ("Kilpailijat", [(c["nimi"], f'{site}yritys/{vert["slug"]}/{c["slug"]}/') for c in kilpailijat]),
        ("Opas", [(f'{vert["nimi"]} — ostajan opas', f'{site}{vert["slug"]}/#opas')]),
        ("Menetelmä", [("Näin pisteytämme", f"{site}luottamus/")]),
        ("Aiheet", [("#" + t, f"{up}aihe/{t}/") for t in tagit]),
    ]
    out = []
    for otsikko, linkit in rivit:
        ls = " ".join(f'<a href="{esc(h)}">{esc(n)}</a>' for n, h in linkit)
        out.append(f'<div class="lv-row"><span class="lv-k">{esc(otsikko)}</span><span class="lv-v">{ls}</span></div>')
    return f"""<aside class="panel lv">
  <h3>Linkkiverkko</h3>
  <p class="lv-lead">Yksi kysymys kytkeytyy automaattisesti mittausdataan. Nämä linkit syntyvät ilman käsityötä.</p>
  {''.join(out)}
</aside>"""


def kysymyssivu(q):
    vert = load(q["vertical"])
    yritys = next(c for c in vert["yritykset"] if c["slug"] == q["yritys"])
    kilpailijat = [c for c in vert["yritykset"] if c["slug"] != q["yritys"]][:3]
    up = "../../"
    site = up + "../"
    n = len(q["vastaukset"])

    vastaukset = []
    for i, v in enumerate(q["vastaukset"]):
        paras = '<span class="chip ok">Hyödyllisin</span>' if v.get("paras") else ""
        vastaukset.append(f"""
      <article class="ans{' best' if v.get('paras') else ''}" data-id="{i}">
        <div class="votebox">
          <button class="vote" data-id="{i}" aria-label="Merkitse hyödylliseksi">▲</button>
          <span class="votes" data-votes="{v['aanet']}">{v['aanet']}</span>
        </div>
        <div class="ansbody">
          <div class="ansmeta"><b>{esc(v['nimi'])}</b> <span class="chip demo">Esimerkki</span> <span class="rep" title="Mainepisteet">{v['maine']} p</span> <span class="dot">·</span> {esc(v['aika'])} {paras}</div>
          <p>{esc(v['teksti'])}</p>
        </div>
      </article>""")

    jatko = "".join(
        f'<li><a href="{up}{y}/{s}/">{esc(t)}</a></li>' for t, y, s in q["jatkokysymykset"])
    tagit = " ".join(f'<a class="tag" href="{up}aihe/{t}/">#{t}</a>' for t in q["tagit"])

    jsonld = {
        "@context": "https://schema.org", "@type": "QAPage",
        "mainEntity": {
            "@type": "Question", "name": q["otsikko"], "text": q["kysymys"],
            "answerCount": n, "upvoteCount": q["vastaukset"][0]["aanet"],
            "acceptedAnswer": {"@type": "Answer", "text": q["vastaukset"][0]["teksti"],
                               "upvoteCount": q["vastaukset"][0]["aanet"]},
            "suggestedAnswer": [{"@type": "Answer", "text": v["teksti"], "upvoteCount": v["aanet"]}
                                for v in q["vastaukset"][1:]],
        },
    }

    tiivis = q["tiivistelma"].format(n=n, p=q["vastaukset"][-1]["aika"])
    body = f"""
<div class="wrap kk">
  <p class="crumb"><a href="{site}">Etusivu</a> &rsaquo; <a href="{up}">Kysy kaverilta</a> &rsaquo;
     <a href="{up}{q['yritys']}/">{esc(yritys['nimi'])}</a> &rsaquo; <b>{esc(q['otsikko'])}</b></p>

  <div class="kkgrid">
   <main>
    <div class="qhead">
      <h1>{esc(q['otsikko'])}</h1>
      <div class="qmeta">Kysyi <b>{esc(q['kysyja'])}</b> <span class="dot">·</span> {esc(q['aika'])}
        <span class="dot">·</span> {n} vastausta <span class="dot">·</span> {q['katselut']} katselua</div>
      <p class="qtext">{esc(q['kysymys'])}</p>
      <div class="tags">{tagit}</div>
    </div>

    <section class="aisum">
      <div class="aisum-h"><span class="chip ai">AI-yhteenveto</span> <span class="mut">päivittyy automaattisesti uusien vastausten myötä</span></div>
      <p>{esc(tiivis)}</p>
      <p class="aisum-src">Yhteenveto perustuu vain tämän sivun vastauksiin. Se ei ole kannanotto yhtiön palvelun laadusta.</p>
    </section>

    <h2 class="secth">{n} vastausta</h2>
    {''.join(vastaukset)}

    <article class="ans official">
      <div class="votebox"><span class="shield" aria-hidden="true">✓</span></div>
      <div class="ansbody">
        <div class="ansmeta"><b>Yrityksen vahvistettu vastaus</b> <span class="chip ver">Paikka varattu</span></div>
        <p class="mut">Tähän tulisi yhtiön oma vastaus, jos sillä on vahvistettu yritystili.
           {esc(yritys["nimi"])} ei ole vastannut, eikä tähän kirjoiteta mitään yhtiön puolesta.</p>
      </div>
    </article>

    <section class="panel writer">
      <h3>Vastaa kysymykseen</h3>
      <textarea id="answer" rows="3" placeholder="Kerro oma kokemuksesi. Pysy asiassa — mielipide on sallittu, keksitty väite ei."></textarea>
      <div class="wrow"><button class="btn" id="postAnswer">Lähetä vastaus</button>
        <span class="mut small">Demo: vastaus tallentuu vain tähän selaimeen.</span></div>
    </section>

    <section class="panel">
      <h3>Samankaltaiset kysymykset</h3>
      <ul class="qlist">{jatko}</ul>
      <p class="mut small">AI ehdottaa näitä, kun samaa aihetta kysytään toistuvasti — jokaisesta syntyy oma sivunsa.</p>
    </section>
   </main>

   <div class="side">
    {linkkiverkko(yritys, vert, kilpailijat, q['tagit'], up)}

    <aside class="panel scorecard">
      <h3>Mitä mittasimme</h3>
      <p class="sc-num">{str(yritys['score']).replace('.', ',')}<span>/100</span></p>
      <p class="mut small">{esc(yritys['nimi'])} · {esc(vert['nimi'])} · mitattu {esc(vert['updated'])}</p>
      <a class="btn ghost" href="{site}yritys/{vert['slug']}/{q['yritys']}/">Katso mistä pisteet tulevat</a>
      <p class="mut small">Keskustelu ei vaikuta pisteisiin. Pisteet tulevat mittauksesta, mielipiteet keskustelusta — ne pidetään erillään.</p>
    </aside>

    <aside class="panel seo">
      <h3>SEO-näkymä <button class="mini" id="seoToggle">näytä</button></h3>
      <p class="mut small">Mitä hakukone näkee tästä sivusta.</p>
      <pre id="seoBox" hidden>{esc(json.dumps(jsonld, ensure_ascii=False, indent=1))}</pre>
    </aside>
   </div>
  </div>
</div>"""
    return page(f"{q['otsikko']} | Kysy kaverilta | Suomen Paras",
                f"{q['otsikko']} — {n} kokemusta ja AI-yhteenveto. Suomen Paras, Kysy kaverilta.",
                body, depth=2, jsonld=jsonld)


def avoin_kysymys(otsikko, yritys_slug, slug, tagit, vertical):
    """Kysymys jolla ei viela ole vastauksia — demon tyhja tila."""
    vert = load(vertical)
    yritys = next(c for c in vert["yritykset"] if c["slug"] == yritys_slug)
    kilpailijat = [c for c in vert["yritykset"] if c["slug"] != yritys_slug][:3]
    up = "../../"
    site = up + "../"
    nimi = yritys["nimi"]
    score = str(yritys["score"]).replace(".", ",")
    tagl = " ".join('<a class="tag" href="%saihe/%s/">#%s</a>' % (up, t, t) for t in tagit)
    muut = [(t, y, sl) for t, y, sl, _tg, _v, _n, _k in kaikki_kysymykset() if sl != slug][:4]
    lista = "".join('<li><a href="%s%s/%s/">%s</a></li>' % (up, y, sl, esc(t)) for t, y, sl in muut)
    jsonld = {"@context": "https://schema.org", "@type": "QAPage",
              "mainEntity": {"@type": "Question", "name": otsikko, "answerCount": 0}}
    body = f"""
<div class="wrap kk">
  <p class="crumb"><a href="{site}">Etusivu</a> &rsaquo; <a href="{up}">Kysy kaverilta</a> &rsaquo;
     <a href="{up}{yritys_slug}/">{esc(nimi)}</a> &rsaquo; <b>{esc(otsikko)}</b></p>
  <div class="kkgrid">
   <main>
    <div class="qhead">
      <h1>{esc(otsikko)}</h1>
      <div class="qmeta"><span class="chip ai">AI loi keskustelun</span>
        <span class="dot">·</span> ei vielä vastauksia</div>
      <p class="qtext">Tämä kysymys toistui haussa ja muissa keskusteluissa, joten siitä syntyi
         automaattisesti oma sivunsa. Sivu on olemassa, linkitetty ja indeksoitavissa jo ennen
         ensimmäistä vastausta.</p>
      <div class="tags">{tagl}</div>
    </div>

    <section class="empty">
      <p class="e-big">Ei vielä yhtään vastausta.</p>
      <p class="mut">Ensimmäinen vastaus näkyy heti sivulla ja käynnistää AI-yhteenvedon.</p>
    </section>

    <section class="panel writer">
      <h3>Ole ensimmäinen</h3>
      <textarea id="answer" rows="3" placeholder="Kerro oma kokemuksesi."></textarea>
      <div class="wrow"><button class="btn" id="postAnswer">Lähetä vastaus</button>
        <span class="mut small">Demo: vastaus tallentuu vain tähän selaimeen.</span></div>
    </section>

    <section class="panel"><h3>Muita keskusteluja</h3><ul class="qlist">{lista}</ul></section>
   </main>
   <div class="side">
    {linkkiverkko(yritys, vert, kilpailijat, tagit, up)}
    <aside class="panel scorecard">
      <h3>Mitä mittasimme</h3>
      <p class="sc-num">{score}<span>/100</span></p>
      <p class="mut small">{esc(nimi)} · {esc(vert["nimi"])} · mitattu {esc(vert["updated"])}</p>
      <a class="btn ghost" href="{site}yritys/{vert["slug"]}/{yritys_slug}/">Katso mistä pisteet tulevat</a>
    </aside>
   </div>
  </div>
</div>"""
    return page(otsikko + " | Kysy kaverilta | Suomen Paras",
                otsikko + " — kysy ja vastaa. Suomen Paras, Kysy kaverilta.",
                body, depth=2, jsonld=jsonld)


def yrityssivu(yritys_slug, vertical):
    vert = load(vertical)
    yritys = next(c for c in vert["yritykset"] if c["slug"] == yritys_slug)
    up = "../"
    site = up + "../"
    nimi = yritys["nimi"]
    score = str(yritys["score"]).replace(".", ",")
    valilehdet = ["keskustelu", "kysymykset", "kokemukset", "arvostelut", "vertailut",
                  "uutiset", "oppaat", "reklamaatiot", "asiakaspalvelu"]
    tabs = "".join('<span class="tab%s">%s</span>' % (" on" if t == "keskustelu" else "", t)
                   for t in valilehdet)
    omat = [(t, sl, n, k) for t, y, sl, _tg, _v, n, k in kaikki_kysymykset() if y == yritys_slug]
    rivit = "".join(
        '<li><a href="%s%s/%s/">%s</a><span class="mut small">%s</span></li>'
        % (up, yritys_slug, sl, esc(t),
           ("%d vastausta · %d katselua" % (n, k)) if n else "AI ehdotti — ei vielä vastauksia")
        for t, sl, n, k in omat)
    tagit = sorted({t for _o, y, _s, tg, _v, _n, _k in kaikki_kysymykset()
                    if y == yritys_slug for t in tg})
    kilpa = " ".join('<a href="%syritys/%s/%s/">%s</a>' % (site, vert["slug"], c["slug"], esc(c["nimi"]))
                     for c in vert["yritykset"] if c["slug"] != yritys_slug)
    tagl = " ".join('<a href="%saihe/%s/">#%s</a>' % (up, t, t) for t in tagit)
    body = f"""
<div class="wrap kk">
  <p class="crumb"><a href="{site}">Etusivu</a> &rsaquo; <a href="{up}">Kysy kaverilta</a> &rsaquo; <b>{esc(nimi)}</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>{esc(nimi)} — kysy kaverilta</h1>
    <p class="lead">Kaikki {esc(nimi)}-keskustelut yhdessä paikassa, kiinni mittausdatassa.
       Yhtiö sai {score} / 100 kategoriassa {esc(vert["nimi"].lower())}.</p>
  </div>
  <div class="tabs">{tabs}<span class="mut small tabs-note">konseptin URL-rakenne: /kysy-kaverilta/{esc(yritys_slug)}/…</span></div>
  <div class="kkgrid">
    <main>
      <section class="panel"><h3>Kysymykset</h3><ul class="qlist big">{rivit}</ul></section>
      <section class="panel">
        <h3>Kysy uutta</h3>
        <input id="askq" type="text" placeholder="Esim. Paljonko liittymä maksaa kampanjan jälkeen?">
        <div class="wrow"><button class="btn" id="askBtn">Luo keskustelu</button></div>
        <p class="mut small">Demo näyttää, millainen osoite kysymyksestä syntyisi:</p>
        <p class="urlout mono" id="urlOut">/kysy-kaverilta/{esc(yritys_slug)}/…</p>
      </section>
    </main>
    <div class="side">
      <aside class="panel scorecard">
        <h3>Mittaustulos</h3>
        <p class="sc-num">{score}<span>/100</span></p>
        <p class="mut small">{esc(vert["nimi"])} · mitattu {esc(vert["updated"])}</p>
        <a class="btn ghost" href="{site}yritys/{vert["slug"]}/{yritys_slug}/">Yrityksen sivu</a>
      </aside>
      <aside class="panel lv">
        <h3>Kytkennät</h3>
        <div class="lv-row"><span class="lv-k">Kategoria</span><span class="lv-v"><a href="{site}{vert["slug"]}/">{esc(vert["nimi"])}</a></span></div>
        <div class="lv-row"><span class="lv-k">Kilpailijat</span><span class="lv-v">{kilpa}</span></div>
        <div class="lv-row"><span class="lv-k">Aiheet</span><span class="lv-v">{tagl}</span></div>
      </aside>
    </div>
  </div>
</div>"""
    return page(nimi + " — Kysy kaverilta | Suomen Paras",
                nimi + "-keskustelut, kysymykset ja kokemukset yhdessä paikassa.",
                body, depth=1)


def tagisivu(tag):
    up = "../../"
    site = up + "../"
    virta = [(t, y, sl, n, k) for t, y, sl, tg, _v, n, k in kaikki_kysymykset() if tag in tg]
    virta.sort(key=lambda r: -r[3])
    if virta:
        rivit = "".join(
            '<li><a href="%s%s/%s/">%s</a><span class="mut small">%s</span></li>'
            % (up, y, sl, esc(t),
               ("%d vastausta · %d katselua" % (n, k)) if n else "ei vielä vastauksia")
            for t, y, sl, n, k in virta)
        sisalto = '<ul class="qlist big">%s</ul>' % rivit
    else:
        sisalto = '<p class="mut">Tästä aiheesta ei ole vielä keskusteluja.</p>'
    muut = " ".join('<a class="tag" href="%saihe/%s/">#%s</a>' % (up, t, t)
                    for t in TAGIT_KUVAUS if t != tag)
    body = f"""
<div class="wrap kk">
  <p class="crumb"><a href="{site}">Etusivu</a> &rsaquo; <a href="{up}">Kysy kaverilta</a> &rsaquo; <b>#{esc(tag)}</b></p>
  <div class="pageh" style="padding-top:0">
    <h1>#{esc(tag)}</h1>
    <p class="lead">{esc(TAGIT_KUVAUS[tag])}. Tagi syntyy automaattisesti keskustelun sisällöstä — sivu
       kokoaa saman aiheen kysymykset yhtiöstä riippumatta.</p>
  </div>
  <div class="kkgrid">
    <main><section class="panel"><h3>Keskustelut</h3>{sisalto}</section></main>
    <div class="side">
      <aside class="panel"><h3>Muut aiheet</h3><div class="tags">{muut}</div></aside>
      <aside class="panel"><h3>Miksi tagisivu</h3>
        <p class="mut small">Sama ongelma toistuu eri yhtiöillä. Tagisivu tekee siitä oman
        laskeutumissivunsa ja kytkee keskustelut ristiin ilman että kukaan luokittelee niitä käsin.</p></aside>
    </div>
  </div>
</div>"""
    return page("#" + tag + " | Kysy kaverilta | Suomen Paras",
                "Kaikki #" + tag + "-aiheiset keskustelut Suomen Parhaassa.", body, depth=2)


def etusivu():
    vert = load(KYSYMYKSET[0]["vertical"])
    kaikki = kaikki_kysymykset()
    kortit = "".join(
        '<a class="qcard" href="%s/%s/"><span class="qc-t">%s</span><span class="qc-m">%s</span></a>'
        % (y, sl, esc(t), ("%d vastausta · %d katselua" % (n, k)) if n else "AI ehdotti — uusi")
        for t, y, sl, _tg, _v, n, k in kaikki[:6])
    tagit = " ".join('<a class="tag" href="aihe/%s/">#%s</a>' % (t, t) for t in TAGIT_KUVAUS)
    vaiheet = [
        ("1", "Kysymys", "Käyttäjä kysyy. Kysymys saa oman osoitteen, otsikon ja metakuvauksen."),
        ("2", "Tunnistus", "AI tunnistaa yhtiön, kategorian ja aiheen tekstistä ja luo linkit."),
        ("3", "Vastaukset", "Yhteisö vastaa, äänestää ja nostaa hyödyllisimmän ylös."),
        ("4", "Yhteenveto", "AI tiivistää keskustelun ja päivittää sen uusien vastausten myötä."),
        ("5", "Verkosto", "Sivu linkittyy yritykseen, kilpailijoihin, oppaisiin ja tageihin."),
    ]
    steps = "".join('<div class="step"><span class="k">%s</span><h3>%s</h3><p>%s</p></div>'
                    % (k, esc(n), esc(t)) for k, n, t in vaiheet)
    yr = sorted({r[1] for r in kaikki})
    nimet = {c["slug"]: c["nimi"] for c in vert["yritykset"]}
    hubit = " ".join('<a class="tag" href="%s/">%s</a>' % (y, esc(nimet.get(y, y))) for y in yr)
    ykk = vert["yritykset"][0]
    body = f"""
<div class="wrap kk">
  <p class="crumb"><a href="../">Etusivu</a> &rsaquo; <b>Kysy kaverilta</b></p>
  <div class="pageh hero" style="padding-top:0">
    <h1>Kysy kaverilta</h1>
    <p class="lead">Mittaus kertoo, mitä yritys lupaa julkisesti. Keskustelu kertoo, miten se meni.
       Kysy kaverilta kokoaa kokemukset samaan paikkaan mittausdatan kanssa — jokainen kysymys
       omalle sivulleen, kiinni siinä yhtiössä ja kategoriassa jota se koskee.</p>
    <div class="askbig">
      <input id="askq" type="text" placeholder="Kysy jotain, esim. Onko DNA:n valokuitu hyvä?">
      <button class="btn" id="askBtn">Kysy</button>
    </div>
    <p class="urlout mono" id="urlOut">Kysymyksesi osoite näkyy tässä</p>
  </div>

  <h2 class="secth">Keskustelut juuri nyt</h2>
  <div class="qcards">{kortit}</div>

  <h2 class="secth">Yritykset</h2>
  <div class="tags big">{hubit}</div>

  <h2 class="secth">Aiheet</h2>
  <div class="tags big">{tagit}</div>

  <h2 class="secth">Miten yhdestä kysymyksestä tulee sivu</h2>
  <div class="steps">{steps}</div>

  <div class="panel note-why">
    <h3>Miksi tämä sopii juuri Suomen Parhaalle</h3>
    <p>Keskustelupalstoja on jo. Mikään niistä ei tiedä, että {esc(ykk["nimi"])} sai
    {str(ykk["score"]).replace(".", ",")} pistettä läpinäkyvyydestä, eikä osaa linkittää keskustelua
    siihen mittaukseen. Tässä keskustelu ja mittaus ovat samassa paikassa, ja ne pidetään silti
    erillään: <b>keskustelu ei koskaan vaikuta pisteisiin</b>. Se on koko palvelun uskottavuuden ehto.</p>
  </div>
</div>"""
    return page("Kysy kaverilta | Suomen Paras",
                "Kysy ja vastaa yrityksistä. Jokainen kysymys saa oman sivunsa, kiinni mittausdatassa.",
                body, depth=0)


CSS = """/* Kysy kaverilta -demo. Kayttaa sivuston omia muuttujia (assets/style.css). */
.demobar{background:var(--gold-soft);border-bottom:2px solid var(--gold-line);color:var(--ink);
  padding:9px 20px;font-size:.86rem;text-align:center}
.kk{padding:22px 20px 60px}
.kkgrid{display:grid;grid-template-columns:1fr 340px;gap:26px;align-items:start}
@media(max-width:900px){.kkgrid{grid-template-columns:1fr}}
.kk main{min-width:0}
.side{display:flex;flex-direction:column;gap:16px;position:sticky;top:86px}
@media(max-width:900px){.side{position:static}}
.panel{background:var(--card);border:1.5px solid var(--line);border-radius:var(--r);padding:18px 20px;
  box-shadow:var(--shadow);margin-bottom:18px}
.panel h3{font-size:1.02rem;color:var(--ink);margin-bottom:8px}
.secth{font-size:1.25rem;color:var(--ink);margin:26px 0 12px}
.mut{color:var(--mut)}.small{font-size:.83rem}.dot{color:var(--line);margin:0 4px}
.mono{font-family:'IBM Plex Mono',monospace}

.qhead{background:var(--card);border:1.5px solid var(--line);border-radius:var(--r);padding:22px 24px;
  box-shadow:var(--shadow)}
.qhead h1{font-size:1.72rem;color:var(--ink);line-height:1.25}
.qmeta{font-size:.85rem;color:var(--mut);margin:6px 0 12px}
.qtext{color:var(--body)}
.tags{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
.tags.big{margin:0 0 8px}
.tag{background:var(--blue-soft);color:var(--blue-deep);border:1px solid var(--line);border-radius:999px;
  padding:4px 11px;font-size:.82rem;font-weight:800}
.tag:hover{background:var(--blue);color:#fff;text-decoration:none}

.aisum{background:linear-gradient(180deg,var(--cream),var(--card));border:1.5px solid var(--line);
  border-left:5px solid var(--blue);border-radius:var(--r);padding:18px 20px;margin:18px 0;box-shadow:var(--shadow)}
.aisum-h{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;font-size:.84rem}
.aisum-src{color:var(--mut);font-size:.8rem;margin-top:8px}
.chip{display:inline-block;border-radius:999px;padding:3px 10px;font-size:.74rem;font-weight:900;
  letter-spacing:.03em;text-transform:uppercase}
.chip.ai{background:var(--blue);color:#fff}
.chip.ok{background:var(--gold-soft);color:var(--gold-deep);border:1px solid var(--gold-line)}
.chip.ver{background:#E6F6EC;color:var(--ok);border:1px solid #B7E3C6}
.chip.demo{background:var(--silver-soft);color:var(--mut);border:1px solid var(--line)}

.ans{display:flex;gap:14px;background:var(--card);border:1.5px solid var(--line);border-radius:var(--r);
  padding:16px 18px;margin-bottom:12px;box-shadow:var(--shadow)}
.ans.best{border-color:var(--gold-line);background:linear-gradient(180deg,#FFFCF2,var(--card))}
.ans.official{border-color:#B7E3C6;background:linear-gradient(180deg,#F4FBF6,var(--card))}
.votebox{display:flex;flex-direction:column;align-items:center;gap:2px;min-width:44px}
.vote{background:var(--blue-soft);border:1.5px solid var(--line);color:var(--blue-deep);border-radius:10px;
  width:38px;height:32px;font-size:.9rem;cursor:pointer;font-weight:900}
.vote:hover{background:var(--blue);color:#fff}
.vote.done{background:var(--blue);color:#fff;cursor:default}
.votes{font-weight:900;color:var(--ink);font-size:.95rem}
.shield{width:38px;height:38px;border-radius:50%;background:#E6F6EC;color:var(--ok);display:grid;
  place-items:center;font-weight:900;border:1.5px solid #B7E3C6}
.ansbody{flex:1;min-width:0}
.ansmeta{font-size:.85rem;color:var(--mut);margin-bottom:6px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.ansmeta b{color:var(--ink)}
.rep{background:var(--silver-soft);border:1px solid var(--line);border-radius:999px;padding:1px 8px;font-size:.74rem;font-weight:800}

.writer textarea,input[type=text]{width:100%;font-family:inherit;font-size:.95rem;color:var(--body);
  border:1.5px solid var(--line);border-radius:12px;padding:11px 13px;background:var(--cream)}
.writer textarea:focus,input[type=text]:focus{outline:3px solid var(--gold);outline-offset:1px}
.wrow{display:flex;align-items:center;gap:12px;margin-top:10px;flex-wrap:wrap}
.btn{background:var(--blue);color:#fff;border:0;border-radius:999px;padding:10px 20px;font-family:inherit;
  font-weight:900;font-size:.9rem;cursor:pointer;box-shadow:var(--pop)}
.btn:hover{background:var(--blue-deep);text-decoration:none;color:#fff}
.btn.ghost{background:var(--card);color:var(--blue-deep);border:1.5px solid var(--line);box-shadow:none;
  display:inline-block;margin:6px 0}
.mini{background:var(--blue-soft);border:1px solid var(--line);border-radius:999px;padding:2px 10px;
  font-family:inherit;font-size:.75rem;font-weight:800;color:var(--blue-deep);cursor:pointer;float:right}

.qlist{list-style:none;display:flex;flex-direction:column;gap:2px}
.qlist li{padding:9px 0;border-bottom:1px dashed var(--line)}
.qlist li:last-child{border-bottom:0}
.qlist.big li{display:flex;flex-direction:column;gap:2px}
.qlist a{font-weight:800}

.qcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.qcard{display:flex;flex-direction:column;gap:6px;background:var(--card);border:1.5px solid var(--line);
  border-radius:var(--r);padding:16px 18px;box-shadow:var(--shadow)}
.qcard:hover{border-color:var(--blue);text-decoration:none;transform:translateY(-2px)}
.qc-t{font-family:'Baloo 2',sans-serif;font-weight:700;color:var(--ink);font-size:1.02rem;line-height:1.3}
.qc-m{font-size:.8rem;color:var(--mut)}

.lv-lead{font-size:.83rem;color:var(--mut);margin-bottom:10px}
.lv-row{display:flex;gap:10px;padding:7px 0;border-bottom:1px dashed var(--line);font-size:.86rem}
.lv-row:last-child{border-bottom:0}
.lv-k{min-width:82px;color:var(--mut);font-weight:800;font-size:.78rem;text-transform:uppercase;letter-spacing:.03em}
.lv-v{display:flex;flex-wrap:wrap;gap:6px}
.lv-v a{font-weight:700}

.scorecard .sc-num{font-family:'Baloo 2',sans-serif;font-size:2.4rem;font-weight:800;color:var(--blue-deep);line-height:1}
.scorecard .sc-num span{font-size:1rem;color:var(--mut)}
.seo pre{background:#2B0A1C;color:#FFD9E8;border-radius:12px;padding:12px;font-size:.72rem;overflow:auto;
  max-height:280px;font-family:'IBM Plex Mono',monospace;margin-top:8px}

.tabs{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin:6px 0 18px}
.tab{background:var(--silver-soft);border:1px solid var(--line);border-radius:999px;padding:5px 13px;
  font-size:.82rem;font-weight:800;color:var(--mut)}
.tab.on{background:var(--blue);color:#fff;border-color:var(--blue)}
.tabs-note{margin-left:auto}

.hero .lead{max-width:760px}
.askbig{display:flex;gap:10px;margin-top:16px;max-width:680px}
.askbig input{flex:1}
.urlout{margin-top:8px;font-size:.84rem;color:var(--blue-deep);background:var(--blue-soft);
  border:1px dashed var(--line);border-radius:10px;padding:8px 12px;display:inline-block}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px}
.step{background:var(--card);border:1.5px solid var(--line);border-radius:var(--r);padding:16px 18px;box-shadow:var(--shadow)}
.step .k{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--blue);
  color:#fff;font-weight:900;margin-bottom:8px}
.step h3{font-size:1rem;margin-bottom:4px}
.step p{font-size:.86rem;color:var(--body)}
.note-why{margin-top:26px;border-left:5px solid var(--gold)}
.empty{background:var(--cream);border:1.5px dashed var(--line);border-radius:var(--r);padding:26px 22px;text-align:center;margin:18px 0}
.e-big{font-family:'Baloo 2',sans-serif;font-size:1.15rem;color:var(--ink);font-weight:700}
"""

JS = """/* Kysy kaverilta -demo: aanestys, vastaus ja osoitteen muodostus. Vain selaimessa. */
(function () {
  var KEY = 'sp-kk-demo';
  var store = JSON.parse(localStorage.getItem(KEY) || '{}');
  function save() { localStorage.setItem(KEY, JSON.stringify(store)); }

  // aanestys
  document.querySelectorAll('.vote').forEach(function (b) {
    var id = b.dataset.id, box = b.parentNode.querySelector('.votes');
    if (store['v' + id]) { b.classList.add('done'); box.textContent = +box.dataset.votes + 1; }
    b.addEventListener('click', function () {
      if (store['v' + id]) return;
      store['v' + id] = 1; save();
      b.classList.add('done'); box.textContent = +box.dataset.votes + 1;
    });
  });

  // oma vastaus
  var post = document.getElementById('postAnswer');
  if (post) {
    var ta = document.getElementById('answer');
    function render(txt) {
      var el = document.createElement('article');
      el.className = 'ans';
      el.innerHTML = '<div class="votebox"><span class="votes">1</span></div>' +
        '<div class="ansbody"><div class="ansmeta"><b>Sinä</b> ' +
        '<span class="chip ok">Oma vastaus</span> <span class="dot">·</span> juuri nyt</div><p></p></div>';
      el.querySelector('p').textContent = txt;
      post.closest('.writer').insertAdjacentElement('beforebegin', el);
    }
    (store.answers || []).forEach(render);
    post.addEventListener('click', function () {
      var t = (ta.value || '').trim();
      if (t.length < 5) { ta.focus(); return; }
      store.answers = (store.answers || []).concat([t]); save();
      render(t); ta.value = '';
    });
  }

  // kysymyksesta osoitteeksi
  var ask = document.getElementById('askq'), out = document.getElementById('urlOut'),
      btn = document.getElementById('askBtn');
  if (ask && out) {
    function slug(s) {
      return s.toLowerCase().replace(/[äå]/g, 'a').replace(/ö/g, 'o')
        .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
    }
    function firma(s) {
      var t = s.toLowerCase(), names = ['dna', 'elisa', 'telia', 'moi', 'oomi', 'globetel'];
      for (var i = 0; i < names.length; i++) if (t.indexOf(names[i]) > -1) return names[i];
      return 'yleinen';
    }
    function upd() {
      var v = ask.value.trim();
      out.textContent = v ? '/kysy-kaverilta/' + firma(v) + '/' + slug(v) + '/'
                          : 'Kysymyksesi osoite näkyy tässä';
    }
    ask.addEventListener('input', upd);
    if (btn) btn.addEventListener('click', function () {
      upd();
      out.textContent += '  ← demo pysähtyy tähän';
    });
  }

  // SEO-paneeli
  var t = document.getElementById('seoToggle'), box = document.getElementById('seoBox');
  if (t && box) t.addEventListener('click', function () {
    box.hidden = !box.hidden; t.textContent = box.hidden ? 'näytä' : 'piilota';
  });
})();
"""


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)
    print("wrote", os.path.relpath(path, BASE).replace(os.sep, "/"))


def main():
    write(os.path.join(OUT, "demo.css"), CSS)
    write(os.path.join(OUT, "demo.js"), JS)
    write(os.path.join(OUT, "index.html"), etusivu())
    for q in KYSYMYKSET:
        write(os.path.join(OUT, q["yritys"], q["slug"], "index.html"), kysymyssivu(q))
    for otsikko, y, slug, tagit, vertical in AVOIMET:
        write(os.path.join(OUT, y, slug, "index.html"),
              avoin_kysymys(otsikko, y, slug, tagit, vertical))
    kaikki = kaikki_kysymykset()
    for y in sorted({r[1] for r in kaikki}):
        vertical = next(r[4] for r in kaikki if r[1] == y)
        write(os.path.join(OUT, y, "index.html"), yrityssivu(y, vertical))
    for tag in TAGIT_KUVAUS:
        write(os.path.join(OUT, "aihe", tag, "index.html"), tagisivu(tag))
    print("\nKysy kaverilta -demo valmis: http://localhost:8741/kysy-kaverilta/")


if __name__ == "__main__":
    main()
