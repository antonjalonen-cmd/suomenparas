# -*- coding: utf-8 -*-
"""Score a vertical: lh_cache + extracts + companies.py + PRH -> data/<vertical>.json

Deterministic by construction: same inputs -> same output. No randomness, no
hand-tuning. If a number moves, an input moved.

Usage:  python pipeline/build_vertical.py vakuutukset
"""
import json, os, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_rules import PILLAR_W, DIGITAL, REACH, AI, TRANSPARENCY, criteria_text
from companies import COMPANIES
from vertical_meta import META

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LH = json.load(open(os.path.join(BASE, "pipeline", "lh_cache", "_summary.json"), encoding="utf-8"))
UPDATED = "16.7.2026"

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
    cache = json.load(open(PRH_CACHE, encoding="utf-8")) if os.path.exists(PRH_CACHE) else {}
    if y_tunnus in cache:
        return cache[y_tunnus]
    url = f"https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId={y_tunnus}"
    year = None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "suomenparas-demo/1.1"})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        comps = d.get("companies") or []
        if comps:
            rd = (comps[0].get("businessId") or {}).get("registrationDate")
            if rd:
                year = int(rd[:4])
    except Exception as ex:
        print(f"  PRH lookup failed for {y_tunnus}: {ex}")
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
                     "lahde": f"Lighthouse {lh.get('lh_version', '13').split('.')[0]}"})
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
                     "lahde": "Claude Haiku 4.5"})
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
        out.append({"label": label, "value": f"{h} snt/kWh".replace(".", ",") if h else "Ei julkisesti esillä"})
        p = e.get("perusmaksu_eur_kk")
        out.append({"label": "Perusmaksu", "value": f"{p} €/kk".replace(".", ",") if p else "Ei julkisesti esillä"})
    elif vertical == "laajakaista":
        out.append({"label": "Saatavuus", "value": meta.get("saatavuus", "–")})
        out.append({"label": "Tekniikat", "value": pretty_list(e.get("tekniikat")) or "Ei kerrottu"})
        h = e.get("halvin_kk_hinta_eur")
        out.append({"label": "Halvin kk-hinta", "value": f"{h} €/kk".replace(".", ",") if h else "Ei julkisesti esillä"})
        s = e.get("nopein_mbps")
        out.append({"label": "Nopein liittymä", "value": f"{s} Mbit/s" if s else "Ei kerrottu"})
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
        e = json.load(open(ext_path, encoding="utf-8"))
        lh = LH.get(f"{vertical}__{slug}")
        if not lh:
            print(f"  SKIP {slug}: no lighthouse")
            continue

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

    out.sort(key=lambda c: -c["score"])
    v = dict(META[vertical])
    v["yritykset"] = out
    v["updated"] = UPDATED
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
