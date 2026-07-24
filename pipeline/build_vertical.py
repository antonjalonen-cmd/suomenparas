# -*- coding: utf-8 -*-
"""Score a vertical: lh_cache + extracts + companies.py + PRH -> data/<vertical>.json

Deterministic by construction: same inputs -> same output. No randomness, no
hand-tuning. If a number moves, an input moved.

Usage:  python pipeline/build_vertical.py vakuutukset
"""
import json, os, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_rules import PILLAR_W, DIGITAL, REACH, AI, TRANSPARENCY, criteria_text
from companies import COMPANIES
from vertical_meta import META

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LH = json.load(open(os.path.join(BASE, "pipeline", "lh_cache", "_summary.json"), encoding="utf-8"))

# Measurement date is PER VERTICAL and is written once, when that vertical is first
# measured. The methodology page promises results are not rewritten retroactively, so
# rebuilding an old category must never stamp it with today's date. A vertical missing
# from here is a vertical nobody dated — fail instead of guessing.
MEASURED = {
    "hautaustoimistot": "23.7.2026",
    "matkatoimistot": "23.7.2026",
    "tilitoimistot": "23.7.2026",
    "fysioterapia": "23.7.2026",
    "autopesulat": "23.7.2026",
    "lainavertailu": "15.7.2026",
    "vakuutukset": "16.7.2026",
    "sahkosopimukset": "16.7.2026",
    "laajakaista": "16.7.2026",
    "puhelinliittymat": "16.7.2026",
    "luottokortit": "16.7.2026",
    "sijoitusalustat": "16.7.2026",
    "webhotellit": "16.7.2026",
    "vpn-palvelut": "16.7.2026",
    # batch 2
    "kulutusluotot": "17.7.2026",
    # pankit was CONFIGURED 17.7 but not measurable until the JS fetch landed 18.7 —
    # the date below is when the transparency data was actually taken.
    "pankit": "18.7.2026",
    "autovakuutukset": "17.7.2026",
    "kotivakuutukset": "17.7.2026",
    "matkavakuutukset": "17.7.2026",
    "lemmikkivakuutukset": "17.7.2026",
    # Vertailupalvelut meta-group batch
    "sahkovertailupalvelut": "17.7.2026",
    # batch 3
    "autokatsastus": "18.7.2026",
    "autovuokraamot": "18.7.2026",
    "optikot": "18.7.2026",
    "yksityislaakarit": "18.7.2026",
    "kuntosalit": "18.7.2026",
    "kiinteistonvalittajat": "18.7.2026",
    # batch 4
    "lakifirmat": "21.7.2026",
    "pakohuoneet": "21.7.2026",
    "hammaslaakarit": "21.7.2026",
    "rengasliikkeet": "21.7.2026",
    "muuttopalvelut": "21.7.2026",
    "siivouspalvelut": "21.7.2026",
    "autokoulut": "21.7.2026",
    # batch 5
    "pilvitallennuspalvelut": "21.7.2026",
    # batch 6
    "tavaransailytys": "23.7.2026",
    "salasananhallintapalvelut": "21.7.2026",
    "autokorjaamot": "21.7.2026",
    "suoratoistopalvelut": "21.7.2026",
    "virustorjuntaohjelmat": "21.7.2026",
    "hautaustoimistot": "23.7.2026",
}

# Score v1.2 (23.7.2026): certification bonus. Verified certifications, memberships
# and published independent audits found on the company's OWN site (or an official
# registry) add credibility: +1.5 points each, at most two counted (max +3.0), total
# capped at 100. Data lives in pipeline/certs/<vertical>.json ({slug: [{nimi, lahde}]}),
# collected in its own measurement pass — a missing file or empty list means bonus 0,
# never a penalty.
CERT_BONUS_PER = 1.5
CERT_BONUS_MAX = 3.0

def load_certs(vertical):
    p = os.path.join(BASE, "pipeline", "certs", f"{vertical}.json")
    if not os.path.exists(p):
        return {}
    return json.load(open(p, encoding="utf-8-sig"))


def load_opas(vertical):
    """Category guide content (dad's structure): johdanto/huomioita/vinkit/ukk.
    Authored as JSON in pipeline/opas/ so content agents never touch Python source."""
    p = os.path.join(BASE, "pipeline", "opas", f"{vertical}.json")
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding="utf-8-sig"))

TERNARY = {"kylla": 1.0, "osittain": 0.5, "ei": 0.0}
TERNARY_LABEL = {"kylla": "Kyllä", "osittain": "Osittain", "ei": "Ei"}
PRH_CACHE = os.path.join(BASE, "pipeline", "prh_cache.json")


def prh_registered(y_tunnus):
    """PRH registration year for this Y-tunnus. Cached; None if unavailable.

    NB this is the registration date of the ENTITY BEHIND THE BRAND — for a
    foreign company's Finnish branch (If, Nordic Green) that is when the branch
    was registered here, not when the group was founded. Labelled accordingly.
    The old opendata-bis-v1 endpoint now serves HTML; v3 is the live one.
    """
    # Foreign companies (most VPNs) have no Finnish Y-tunnus at all — that is the
    # correct answer, not a lookup failure. Don't ask PRH about None.
    if not y_tunnus:
        return None
    cache = json.load(open(PRH_CACHE, encoding="utf-8")) if os.path.exists(PRH_CACHE) else {}
    if y_tunnus in cache:
        return cache[y_tunnus]
    url = f"https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId={y_tunnus}"
    year = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "suomenparas-demo/1.1"})
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)
            comps = d.get("companies") or []
            if comps:
                rd = (comps[0].get("businessId") or {}).get("registrationDate")
                if rd:
                    year = int(rd[:4])
            break
        except urllib.error.HTTPError as ex:
            if ex.code == 429 and attempt < 3:
                wait = 5 * (attempt + 1)
                print(f"  PRH 429 for {y_tunnus}, retrying in {wait}s")
                time.sleep(wait)
                continue
            print(f"  PRH lookup failed for {y_tunnus}: {ex}")
            break
        except Exception as ex:
            print(f"  PRH lookup failed for {y_tunnus}: {ex}")
            break
    # Only cache a real answer — caching a rate-limited None would make the gap permanent.
    if year is not None:
        cache[y_tunnus] = year
        with open(PRH_CACHE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=1)
    return year


def score_digital(lh):
    rows, total = [], 0.0
    for key, label, w in DIGITAL:
        v = lh[key]
        total += v * w / 100
        rows.append({"mittari": label, "arvo": f"{v}/100", "paino": w, "pisteet": v,
                     "lahde": "Tekninen mittaus"})
    return round(total, 1), rows


def score_ternary(spec, e, source):
    rows, total = [], 0.0
    for key, label, w in spec:
        raw = e.get(key)
        if isinstance(raw, bool):
            raw = "kylla" if raw else "ei"
        raw = raw if raw in TERNARY else "ei"
        pts = round(TERNARY[raw] * w, 1)
        total += pts
        row = {"mittari": label, "arvo": TERNARY_LABEL[raw], "paino": w,
               "pisteet_max": w, "pisteet": pts, "lahde": source}
        q = (e.get("evidence") or {}).get(key)
        if q:
            row["quote"] = q
        rows.append(row)
    return round(total, 1), rows


def score_ai(e):
    rows, total = [], 0.0
    a = e["ai_arviot"]
    missing = [k for k, _, _ in AI if k not in a]
    if missing:
        # Fail loudly with the slug — a silent default here would invent a score.
        raise SystemExit(f"{e['slug']}: ai_arviot missing {missing}; got {list(a)}")
    for key, label, w in AI:
        v = a[key]
        total += v * w / 100
        rows.append({"mittari": label, "arvo": f"{v}/100", "paino": w, "pisteet": v,
                     "lahde": "AI-analyysi"})
    return round(total, 1), rows


def reach_value(e, key):
    """Reachability fields are booleans/ternary in the extracts."""
    v = e.get(key)
    if isinstance(v, bool):
        return "kylla" if v else "ei"
    return v if v in TERNARY else "ei"


# Extracts use ASCII slugs (agents avoid ä/ö in keys); the site is Finnish, so
# render them properly rather than printing "porssisahko" at a reader.
PRETTY = {
    "porssisahko": "Pörssisähkö", "kiintea": "Kiinteä", "maaraaikainen": "Määräaikainen",
    "toistaiseksi": "Toistaiseksi voimassa", "hybridi": "Hybridi", "opiskelijasahko": "Opiskelijasähkö",
    "muutto": "Muutto", "yosahko": "Yösähkö", "kausisahko": "Kausisähkö",
    "kuitu": "Kuitu", "kaapeli": "Kaapeli", "5g": "5G", "4g": "4G", "adsl": "ADSL", "dsl": "DSL",
    "koti": "Koti", "auto": "Auto", "matka": "Matka", "lemmikki": "Lemmikki", "henkilo": "Henkilö",
    "vene": "Vene", "metsa": "Metsä", "tapaturma": "Tapaturma", "sairaus": "Sairaus",
    "mokki": "Mökki", "elain": "Eläin", "urheilu": "Urheilu", "oikeusturva": "Oikeusturva",
}


def pretty_list(items):
    if not items:
        return None
    return ", ".join(PRETTY.get(str(i).lower().strip(), str(i).capitalize()) for i in items)


def num(v):
    """5.0 -> '5', 1.99 -> '1,99'. Avoids publishing '1,0 €/kk'."""
    if v is None:
        return None
    f = float(v)
    s = str(int(f)) if f == int(f) else f"{f:g}"
    return s.replace(".", ",")


def facts_extra(vertical, e, meta):
    out = []
    if vertical == "vakuutukset":
        out.append({"label": "Vakuutuslajit", "value": pretty_list(e.get("vakuutuslajit")) or "Ei kerrottu"})
    elif vertical == "sahkosopimukset":
        out.append({"label": "Sopimustyypit", "value": pretty_list(e.get("sopimustyypit")) or "Ei kerrottu"})
        h = e.get("hinta_snt_kwh")
        # For a pörssisähkö contract this figure is the seller's margin, not the
        # delivered price — label it so, instead of implying it is what you pay.
        types = [str(t).lower() for t in (e.get("sopimustyypit") or [])]
        label = "Hinta / marginaali (esillä)" if "porssisahko" in types else "Hinta (esillä)"
        out.append({"label": label, "value": f"{num(h)} snt/kWh" if h else "Ei julkisesti esillä"})
        p = e.get("perusmaksu_eur_kk")
        out.append({"label": "Perusmaksu", "value": f"{num(p)} €/kk" if p else "Ei julkisesti esillä"})
    elif vertical == "laajakaista":
        out.append({"label": "Saatavuus", "value": meta.get("saatavuus", "–")})
        out.append({"label": "Tekniikat", "value": pretty_list(e.get("tekniikat")) or "Ei kerrottu"})
        h = e.get("halvin_kk_hinta_eur")
        out.append({"label": "Halvin kk-hinta", "value": f"{num(h)} €/kk" if h else "Ei julkisesti esillä"})
        s = e.get("nopein_mbps")
        out.append({"label": "Nopein liittymä", "value": f"{s} Mbit/s" if s else "Ei kerrottu"})
    elif vertical == "puhelinliittymat":
        # Which network a brand rides on is the point: the cheapest MVNO may use
        # exactly the same masts as the most expensive operator.
        out.append({"label": "Verkko", "value": meta.get("verkko", "–")})
        h = e.get("halvin_kk_hinta_eur")
        out.append({"label": "Halvin kk-hinta", "value": f"{num(h)} €/kk" if h else "Ei julkisesti esillä"})
        s = e.get("nopein_mbps")
        out.append({"label": "Nopein liittymä", "value": f"{s} Mbit/s" if s else "Ei kerrottu"})
    elif vertical == "luottokortit":
        t = e.get("korttityyppi")
        out.append({"label": "Korttityyppi",
                    "value": "Maksuaikakortti" if t == "maksuaikakortti" else "Luottokortti"})
        k = e.get("todellinen_vuosikorko_pct")
        out.append({"label": "Todellinen vuosikorko",
                    "value": f"{num(k)} %" if k else "Ei julkisesti esillä"})
        v = e.get("vuosimaksu_eur")
        out.append({"label": "Vuosimaksu",
                    "value": (f"{num(v)} €") if v is not None else "Ei julkisesti esillä"})
    elif vertical == "sijoitusalustat":
        # No numeric fee fact here on purpose. Brokers price differently — Evli quotes
        # 0,05 % per trade, Nordnet a 3 € minimum — and the extracts mixed percentages
        # and euros into one field. Rather than print a number that may be the wrong
        # unit, state whether the cost is public and let the receipt rows carry the
        # actual quoted figures.
        pub = {"kylla": "Julkisesti esillä", "osittain": "Osittain esillä",
               "ei": "Vain kirjautuneille"}.get(e.get("kaupankayntikulut_ilman_kirjautumista"), "Ei tiedossa")
        out.append({"label": "Kaupankäyntikulut", "value": pub})
        out.append({"label": "Markkinat", "value": pretty_list(e.get("markkinat")) or "Ei kerrottu"})
    elif vertical == "webhotellit":
        h = e.get("halvin_kk_hinta_eur")
        out.append({"label": "Halvin kk-hinta", "value": f"{num(h)} €/kk" if h else "Ei julkisesti esillä"})
        p = e.get("palvelimet_suomessa")
        out.append({"label": "Palvelimet Suomessa",
                    "value": {"kylla": "Kyllä", "ei": "Ei"}.get(p, "Ei kerrottu")})
    elif vertical == "vpn-palvelut":
        # No Y-tunnus for foreign services, so jurisdiction stands in its place —
        # for a VPN it is arguably the more meaningful fact anyway.
        out.append({"label": "Lainkäyttöalue", "value": meta.get("lainkayttoalue", "–")})
        h = e.get("halvin_kk_hinta_eur")
        out.append({"label": "Halvin kk-hinta", "value": f"{num(h)} €/kk" if h else "Ei julkisesti esillä"})
        s = e.get("suomenkielinen_sivu")
        out.append({"label": "Suomenkielinen sivusto",
                    "value": {"kylla": "Kyllä", "ei": "Ei"}.get(s, "Ei kerrottu")})
    elif vertical == "kulutusluotot":
        # Who supervises the lender is the fact a Finnish borrower cannot look up from
        # the brand: most of these are Swedish or Lithuanian banks passporting in, and
        # a complaint goes to that country's regulator, not Finanssivalvonta.
        out.append({"label": "Valvoja", "value": meta.get("valvoja", "–")})
        k = e.get("todellinen_vuosikorko_pct")
        out.append({"label": "Todellinen vuosikorko (esimerkki)",
                    "value": f"{num(k)} %" if k else "Ei julkisesti esillä"})
        s = e.get("luottosumma_max_eur")
        out.append({"label": "Suurin luottosumma", "value": f"{num(s)} €" if s else "Ei kerrottu"})
    elif vertical == "pankit":
        out.append({"label": "Pankkityyppi", "value": meta.get("pankkityyppi", "–")})
        p = e.get("palveluhinnasto_julkinen")
        out.append({"label": "Palveluhinnasto",
                    "value": {"kylla": "Julkisesti auki", "osittain": "Osittain julkinen",
                              "ei": "Vain kirjautuneille"}.get(p, "Ei tiedossa")})
        h = e.get("kayttotili_kk_maksu_eur")
        # 0 €/kk is a real and meaningful answer here — don't let falsiness hide it.
        out.append({"label": "Käyttötilin kk-maksu",
                    "value": f"{num(h)} €/kk" if h is not None else "Ei julkisesti esillä"})
    elif vertical in ("autovakuutukset", "kotivakuutukset", "matkavakuutukset",
                      "lemmikkivakuutukset"):
        laskuri = e.get("hintalaskuri_ilman_yhteystietoja") or e.get("hinta_esilla_ilman_yhteystietoja")
        out.append({"label": "Hinta-arvio ilman yhteystietoja",
                    "value": {"kylla": "Kyllä", "osittain": "Osittain",
                              "ei": "Ei"}.get(laskuri, "Ei tiedossa")})
        if vertical == "autovakuutukset":
            out.append({"label": "Kaskotasot", "value": pretty_list(e.get("kaskotasot")) or "Ei kerrottu"})
        elif vertical == "lemmikkivakuutukset":
            out.append({"label": "Vakuutettavat eläimet",
                        "value": pretty_list(e.get("elaimet")) or "Ei kerrottu"})
            k = e.get("korvauskatto_eur_vuosi")
            out.append({"label": "Vuosittainen korvauskatto",
                        "value": f"{num(k)} €/v" if k else "Ei julkisesti esillä"})
        else:
            o = e.get("omavastuu_min_eur")
            out.append({"label": "Pienin omavastuu (esillä)",
                        "value": f"{num(o)} €" if o else "Ei julkisesti esillä"})
    return out


def build(vertical):
    metas = COMPANIES[vertical]
    out = []
    for meta in metas:
        slug = meta["slug"]
        ext_path = os.path.join(BASE, "pipeline", "extracts", f"{vertical}__{slug}.json")
        if not os.path.exists(ext_path):
            print(f"  SKIP {slug}: no extract")
            continue
        e = json.load(open(ext_path, encoding="utf-8-sig"))
        lh = LH.get(f"{vertical}__{slug}")
        if not lh:
            print(f"  SKIP {slug}: no lighthouse")
            continue

        # Did we actually measure THIS company? Two real failures on 16.7.2026:
        #  - capnova.fi silently redirected to glesys.fi (a different company), and
        #    Lighthouse scored glesys.fi under the name "Capnova".
        #  - the Hostaan agent read shellit.org and filed it as Hostaan.
        # Publishing one company's data under another's name is the worst thing this
        # site could do, so both inputs are checked against the declared domain.
        base = meta["domain"].replace("www.", "").lower()
        got = (lh.get("fetched_url") or "").lower()
        host = got.split("//")[-1].split("/")[0].replace("www.", "")
        # VERIFIED same-company redirects (23.7.2026): fortum.fi is Fortum Oyj's own
        # Finnish domain and 301-redirects to the group's global fortum.com/fi/sahkoa.
        # Same owner, not a sold brand — allowed explicitly instead of loosening the guard.
        SAME_COMPANY = {("fortum.fi", "fortum.com")}
        if (base, host) in SAME_COMPANY:
            pass
        elif host and base not in host and host not in base:
            raise SystemExit(
                f"{vertical}/{slug}: lighthouse measured {got} but the declared domain is "
                f"{meta['domain']}. The brand may have been sold/redirected. Verify before "
                f"publishing — do NOT score another company's site under this name."
            )
        fetched = [u.lower() for u in (e.get("fetched_ok") or [])]
        if fetched and not any(base in u for u in fetched):
            raise SystemExit(
                f"{vertical}/{slug}: the extraction agent never loaded {meta['domain']} "
                f"(fetched_ok={fetched}). Re-run this extract — it describes a different site."
            )

        dig, dig_rows = score_digital(lh)
        lap, lap_rows = score_ternary(TRANSPARENCY[vertical], e, "Verkkosivu + AI-ekstraktio")
        reach_e = {k: reach_value(e, k) for k, _, _ in REACH}
        reach_e["evidence"] = e.get("evidence") or {}
        rea, rea_rows = score_ternary(REACH, reach_e, "Verkkosivu + AI-ekstraktio")
        ai, ai_rows = score_ai(e)

        score = round(0.30 * dig + 0.30 * lap + 0.20 * rea + 0.20 * ai, 1)

        out.append({
            "slug": slug,
            "nimi": meta["nimi"],
            "domain": meta["domain"],
            "omistaja": meta["omistaja"],
            "y_tunnus": meta["y_tunnus"],
            "rekisteroity": prh_registered(meta["y_tunnus"]),
            "score": score,
            "pillars": {"digitaalinen": dig, "lapinakyvyys": lap, "tavoitettavuus": rea, "ai_laatu": ai},
            "breakdown": {
                "digitaalinen": {"paino_kokonaisuudesta": PILLAR_W["digitaalinen"], "rivit": dig_rows},
                "lapinakyvyys": {"paino_kokonaisuudesta": PILLAR_W["lapinakyvyys"], "rivit": lap_rows},
                "tavoitettavuus": {"paino_kokonaisuudesta": PILLAR_W["tavoitettavuus"], "rivit": rea_rows},
                "ai_laatu": {"paino_kokonaisuudesta": PILLAR_W["ai_laatu"], "rivit": ai_rows},
            },
            "lh": {k: lh[k] for k in ("performance", "accessibility", "seo", "best_practices",
                                      "lcp_ms", "cls", "tbt_ms") if k in lh},
            "facts_extra": facts_extra(vertical, e, meta),
            "vahvuudet": e["vahvuudet"],
            "kehityskohteet": e["kehityskohteet"],
            "yhteenveto": e["yhteenveto"],
        })

    certs_all = load_certs(vertical)
    for c in out:
        certs = certs_all.get(c["slug"]) or []
        if not certs:
            continue
        bonus = round(min(CERT_BONUS_MAX, CERT_BONUS_PER * min(2, len(certs))), 1)
        c["sertifikaatti_bonus"] = bonus
        c["score"] = round(min(100.0, c["score"] + bonus), 1)
        c["sertifikaatit"] = [
            {"mittari": s.get("nimi", "?"),
             "arvo": "Vahvistettu" + ("" if i < 2 else " (ei laskettu, max 2)"),
             "pisteet": (CERT_BONUS_PER if i < 2 else 0),
             "lahde": s.get("lahde", "Yrityksen oma sivusto")}
            for i, s in enumerate(certs)]
    out.sort(key=lambda c: -c["score"])
    v = dict(META[vertical])
    v["yritykset"] = out
    if vertical not in MEASURED:
        raise SystemExit(f"{vertical}: add it to MEASURED with the date it was actually "
                         f"measured — never inherit today's date by accident.")
    v["updated"] = MEASURED[vertical]
    opas = load_opas(vertical)
    if opas:
        v["opas"] = opas
    v["mittarit"] = len(DIGITAL) + len(TRANSPARENCY[vertical]) + len(REACH) + len(AI)
    v["lapinakyvyys_kriteerit"] = criteria_text(vertical)
    # Any {n} in copy resolves to the real company count, so the prose can never
    # contradict the table next to it.
    v["meta_desc"] = v["meta_desc"].replace("{n}", str(len(out)))
    v["notes"] = [n.replace("{n}", str(len(out))) for n in v["notes"]]

    path = os.path.join(BASE, "data", f"{vertical}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(v, f, ensure_ascii=False, indent=1)
    print(f"wrote data/{vertical}.json — {len(out)} companies, {v['mittarit']} mittaria")
    for c in out:
        print(f"  {c['score']:5.1f}  {c['nimi']:<22} dig={c['pillars']['digitaalinen']:5.1f} "
              f"lap={c['pillars']['lapinakyvyys']:5.1f} tav={c['pillars']['tavoitettavuus']:5.1f} "
              f"ai={c['pillars']['ai_laatu']:5.1f}")


if __name__ == "__main__":
    for vert in sys.argv[1:]:
        build(vert)
