# -*- coding: utf-8 -*-
"""Uutishuone: some-tyyliset postaukset MITATUSTA datasta (28.7.2026).

Idea (Antonin pyynto): sivustolla on oma uutishuone, joka julkaisee viikoittain
lyhyita some-postauksen mittaisia nostoja: uudet vertailut, viikon ykkoset,
nousijat ja laskijat, lapinakyvyysaukot, yllattajat.

Rautainen saanto: JOKAINEN postaus johdetaan data/<vertical>.json -tiedostoista.
Mitaan ei keksita, ei kirjoiteta kasin eika vahvisteta markkinointipuheella.
Jos vaite ei ole laskettavissa datasta, sita ei julkaista.

Tila sailytetaan pipeline/uutishuone/:
  snapshot.json  edellisen ajon pisteet (nousijoiden laskemiseen)
  posts.json     julkaistut postaukset (uudet lisataan karkeen)

Usage:  python pipeline/build_uutishuone.py            # luo viikon postaukset
        python pipeline/build_uutishuone.py --dry      # nayta luomatta
"""
import json, os, sys, glob
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "pipeline", "uutishuone")
os.makedirs(OUT, exist_ok=True)
SNAP_P = os.path.join(OUT, "snapshot.json")
POSTS_P = os.path.join(OUT, "posts.json")


def load_json(p, default):
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8-sig"))
    return default


def load_verticals():
    out = []
    for p in sorted(glob.glob(os.path.join(BASE, "data", "*.json"))):
        d = json.load(open(p, encoding="utf-8-sig"))
        if d.get("yritykset"):
            out.append(d)
    return out


def fmt(x):
    return f"{x:.1f}".replace(".", ",")


def build_posts(verts, snap, today):
    """Jokainen postaus: {tyyppi, otsikko, teksti, linkki, tagit}."""
    posts = []
    prev = snap.get("scores", {})

    # 1) Uudet vertailut: kategoriat joita ei ollut edellisessa snapshotissa.
    # Ensimmaisella ajolla snapshottia ei ole, joten "uusi" = tuoreimmalla
    # mittauspaivalla mitatut kategoriat — muuten nostaisimme sattumanvaraisesti
    # aakkosjarjestyksen ensimmaiset.
    prev_verts = set(snap.get("verticals", []))
    if prev_verts:
        uudet = [v for v in verts if v["slug"] not in prev_verts]
    else:
        tuorein = max((v.get("updated") or "") for v in verts)
        uudet = [v for v in verts if v.get("updated") == tuorein]
    if uudet and prev_verts:  # ensimmaisella ajolla ei julkaista "N uutta" -nostoa
        nimet = ", ".join(v["nimi"] for v in uudet[:6])
        n_yht = sum(len(v["yritykset"]) for v in uudet)
        posts.append({
            "tyyppi": "uutta",
            "otsikko": f"{len(uudet)} uutta vertailua julkaistu",
            "teksti": (f"Mittasimme {n_yht} uutta yritystä ja avasimme kategoriat: {nimet}. "
                       f"Jokaisen yrityksen sivulla näkyy mittari mittarilta, mistä pisteet tulevat."),
            "linkki": "kategoriat/",
            "linkki_teksti": "Katso kaikki kategoriat",
            "tagit": ["uusi"],
        })

    # 2) Viikon ykkoset uusissa kategorioissa
    for v in uudet[:5]:
        y = v["yritykset"][0]
        hanta = v["yritykset"][-1]
        ero = y["score"] - hanta["score"]
        posts.append({
            "tyyppi": "ykkonen",
            "otsikko": f"{y['nimi']} on {v['nimi'].lower()} -vertailun kärjessä",
            "teksti": (f"{y['nimi']} sai {fmt(y['score'])} pistettä sadasta. "
                       f"Kategorian viimeinen {hanta['nimi']} jäi {fmt(hanta['score'])} pisteeseen, "
                       f"eli kärjen ja hännän ero on {fmt(ero)} pistettä."),
            "linkki": f"{v['slug']}/",
            "linkki_teksti": f"Avaa {v['nimi'].lower()}",
            "tagit": ["ykkonen", v["slug"]],
        })

    # 3) Nousijat ja laskijat (vaatii edellisen snapshotin)
    muutokset = []
    for v in verts:
        for c in v["yritykset"]:
            key = f"{v['slug']}/{c['slug']}"
            if key in prev and c.get("score") is not None:
                d = round(c["score"] - prev[key], 1)
                if abs(d) >= 1.0:
                    muutokset.append((d, v, c))
    muutokset.sort(key=lambda t: -t[0])
    for d, v, c in muutokset[:3]:
        if d > 0:
            posts.append({
                "tyyppi": "nousija",
                "otsikko": f"{c['nimi']} nousi {fmt(d)} pistettä",
                "teksti": (f"{c['nimi']} ({v['nimi'].lower()}) on nyt {fmt(c['score'])} pistettä. "
                           f"Nousu tarkoittaa, että sivustolta löytyi mittaushetkellä enemmän "
                           f"julkista tietoa kuin edellisellä kierroksella."),
                "linkki": f"yritys/{v['slug']}/{c['slug']}/",
                "linkki_teksti": "Katso mistä pisteet tulevat",
                "tagit": ["nousija", v["slug"]],
            })
    for d, v, c in muutokset[-2:]:
        if d < 0:
            posts.append({
                "tyyppi": "laskija",
                "otsikko": f"{c['nimi']} laski {fmt(abs(d))} pistettä",
                "teksti": (f"{c['nimi']} ({v['nimi'].lower()}) on nyt {fmt(c['score'])} pistettä. "
                           f"Lasku tarkoittaa, että aiemmin näkynyttä tietoa ei löytynyt "
                           f"tällä kierroksella tai sivuston tekniset mittarit heikkenivät."),
                "linkki": f"yritys/{v['slug']}/{c['slug']}/",
                "linkki_teksti": "Katso mikä muuttui",
                "tagit": ["laskija", v["slug"]],
            })

    # 4) Yllattaja: pieni tunnettuus, korkea sijoitus
    yllattajat = []
    for v in verts:
        for i, c in enumerate(v["yritykset"][:3], 1):
            t = (c.get("tunnettuus") or {}).get("luokka")
            if t == "Suppea" and c.get("score", 0) >= 75:
                yllattajat.append((c["score"], i, v, c))
    yllattajat.sort(key=lambda t: -t[0])
    if yllattajat:
        _, sija, v, c = yllattajat[0]
        posts.append({
            "tyyppi": "yllattaja",
            "otsikko": f"Tuntematon nimi kärjessä: {c['nimi']}",
            "teksti": (f"{c['nimi']} on {v['nimi'].lower()} -vertailun sija {sija} "
                       f"({fmt(c['score'])} p), vaikka sen tunnettuus on mittarillamme suppea. "
                       f"Läpinäkyvyys ei ole kokokysymys: pieni yritys voi kertoa hinnat ja "
                       f"ehdot avoimemmin kuin markkinajohtaja."),
            "linkki": f"yritys/{v['slug']}/{c['slug']}/",
            "linkki_teksti": "Katso pisteet",
            "tagit": ["yllattaja", v["slug"]],
        })

    # 5) Lapinakyvyysaukko: yleisin nollamittari koko sivustolla
    puutteet = {}
    for v in verts:
        for c in v["yritykset"]:
            for pilari in (c.get("breakdown") or {}).values():
                for r in pilari.get("rivit", []):
                    if r.get("arvo") == "Ei":
                        puutteet[r["mittari"]] = puutteet.get(r["mittari"], 0) + 1
    if puutteet:
        mittari, kpl = max(puutteet.items(), key=lambda kv: kv[1])
        kaikki = sum(len(v["yritykset"]) for v in verts)
        osuus = round(100 * kpl / kaikki)
        posts.append({
            "tyyppi": "aukko",
            "otsikko": f"Yleisin puute: {mittari.lower()}",
            "teksti": (f"{kpl} mitatusta {kaikki} yrityksestä ({osuus} %) ei kerro tätä "
                       f"julkisilla sivuillaan. Se on koko sivuston yleisin yksittäinen "
                       f"läpinäkyvyysaukko juuri nyt."),
            "linkki": "metodologia/",
            "linkki_teksti": "Näin mittaamme",
            "tagit": ["aukko"],
        })

    # 6) Viikon numero: kuinka moni julkaisee Y-tunnuksen
    y_on = y_kaikki = 0
    for v in verts:
        for c in v["yritykset"]:
            for pilari in (c.get("breakdown") or {}).values():
                for r in pilari.get("rivit", []):
                    if "Y-tunnus" in r.get("mittari", ""):
                        y_kaikki += 1
                        if r.get("arvo") == "Kyllä":
                            y_on += 1
    if y_kaikki:
        osuus = round(100 * y_on / y_kaikki)
        posts.append({
            "tyyppi": "numero",
            "otsikko": f"{osuus} % yrityksistä kertoo Y-tunnuksensa",
            "teksti": (f"Mittasimme {y_kaikki} yritystä: {y_on} kertoo Y-tunnuksensa "
                       f"julkisilla sivuillaan. Y-tunnus on nopein tapa tarkistaa, kenen "
                       f"kanssa oikeasti asioit."),
            "linkki": "luottamus/",
            "linkki_teksti": "Luottamus ja tietoturva",
            "tagit": ["numero"],
        })

    # 7) Koko sivuston karki
    kaikki_yr = [(c["score"], v, c) for v in verts for c in v["yritykset"] if c.get("score")]
    kaikki_yr.sort(key=lambda t: -t[0])
    if kaikki_yr:
        top = kaikki_yr[:3]
        lista = ", ".join(f"{c['nimi']} {fmt(s)}" for s, v, c in top)
        posts.append({
            "tyyppi": "karki",
            "otsikko": "Koko sivuston läpinäkyvimmät juuri nyt",
            "teksti": (f"Korkeimmat pisteet kaikista {len(kaikki_yr)} mitatusta yrityksestä: "
                       f"{lista}. Pisteet mittaavat verkkosivun avoimuutta, eivät palvelun laatua."),
            "linkki": "kategoriat/",
            "linkki_teksti": "Selaa kategorioita",
            "tagit": ["karki"],
        })

    for p in posts:
        p["pvm"] = today
    return posts


def main():
    dry = "--dry" in sys.argv
    today = date.today().strftime("%d.%m.%Y")
    verts = load_verticals()
    snap = load_json(SNAP_P, {})
    posts_old = load_json(POSTS_P, [])

    new_posts = build_posts(verts, snap, today)
    if dry:
        for p in new_posts:
            print(f"[{p['tyyppi']}] {p['otsikko']}\n   {p['teksti'][:120]}...")
        print(f"\n{len(new_posts)} postausta (dry run)")
        return

    # uudet karkeen, sailyta enintaan 60 viimeista
    posts = new_posts + [p for p in posts_old if p.get("pvm") != today]
    json.dump(posts[:60], open(POSTS_P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    scores = {f"{v['slug']}/{c['slug']}": c["score"]
              for v in verts for c in v["yritykset"] if c.get("score") is not None}
    json.dump({"paiva": today, "verticals": [v["slug"] for v in verts], "scores": scores},
              open(SNAP_P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"uutishuone: {len(new_posts)} uutta postausta, {len(posts[:60])} yhteensa")


if __name__ == "__main__":
    main()
