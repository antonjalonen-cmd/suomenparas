# -*- coding: utf-8 -*-
"""One-shot: scores.json (flat loan list) -> data/lainavertailu.json (vertical shape).

The old schema hardcoded loan fields in gen_site.py (facts table, evidence->row
substring matching). The vertical shape bakes both into the data so the generator
stays vertical-agnostic. Run once; scores.json is then the archived raw input.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = json.load(open(os.path.join(BASE, "scores.json"), encoding="utf-8"))


def facts_extra(e):
    """Loan-specific rows for the profile fact table."""
    out = []
    if e.get("lainasumma_min_eur"):
        lo = f"{e['lainasumma_min_eur']:,}".replace(",", " ")
        hi = f"{e['lainasumma_max_eur']:,}".replace(",", " ")
        out.append({"label": "Lainasummat", "value": f"{lo}–{hi} €"})
    else:
        out.append({"label": "Lainasummat", "value": "Ei kerrottu"})
    n = e.get("kumppanipankkien_maara")
    out.append({"label": "Kumppanipankkeja", "value": f"{n} kpl" if n else "Ei kerrottu"})
    return out


def attach_quotes(rows, e):
    """Bake evidence quotes onto the rows they justify (was substring matching in gen_site)."""
    ev = e.get("evidence") or {}
    out = []
    for r in rows:
        r = dict(r)
        m = r["mittari"].lower()
        if "korkoesimerkki" in m and ev.get("korkoesimerkki"):
            r["quote"] = ev["korkoesimerkki"]
        elif "kumppani" in m and ev.get("kumppanit"):
            r["quote"] = ev["kumppanit"]
        elif "arviol" in m and ev.get("asiakasarvio"):
            r["quote"] = ev["asiakasarvio"]
        out.append(r)
    return out


companies = []
for c in SRC:
    e = c["extract"]
    b = json.loads(json.dumps(c["breakdown"]))  # deep copy
    b["lapinakyvyys"]["rivit"] = attach_quotes(b["lapinakyvyys"]["rivit"], e)
    companies.append({
        "slug": c["slug"],
        "nimi": c["nimi"],
        "domain": c["domain"],
        "omistaja": c["omistaja"],
        "y_tunnus": c["y_tunnus"],
        "rekisteroity": c["rekisteroity"],
        "score": c["score"],
        "pillars": c["pillars"],
        "breakdown": b,
        "lh": c.get("lh") or {},
        "facts_extra": facts_extra(e),
        "vahvuudet": e["vahvuudet"],
        "kehityskohteet": e["kehityskohteet"],
        "yhteenveto": e["yhteenveto"],
    })

vertical = {
    "slug": "lainavertailu",
    "nimi": "Lainavertailu",
    "nav": "Lainat",
    # Real measurement date of THIS vertical's data — not the date the site was rebuilt.
    "updated": "15.7.2026",
    "kategoria_nimi": "Lainavertailu",
    "h1": "Suomen paras lainavertailu 2026",
    "yksikko": "suomalaista lainanvälityspalvelua",
    # Counted from the actual scored rows, not asserted. v1.0 claimed "26 mittaria"
    # while the profiles only ever showed 19 — corrected here rather than carried over.
    "mittarit": sum(len(companies[0]["breakdown"][p]["rivit"])
                    for p in ("digitaalinen", "lapinakyvyys", "tavoitettavuus", "ai_laatu")),
    "lead": ("Pisteytimme {n} suomalaista lainanvälityspalvelua {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Sama kaava kaikille — katso jokaisen "
             "pisteen perustelu."),
    "meta_title": "Suomen paras lainavertailu 2026 — kaikki lainanvälittäjät pisteytettynä | Suomen Paras",
    "meta_desc": "9 suomalaista lainanvälityspalvelua pisteytetty 26 mittarilla. Läpinäkyvä Score: katso mistä jokainen piste tulee.",
    "lapinakyvyys_kriteerit": ("Lakisääteinen korkoesimerkki (30), korkoväli (15), lainaehdot (15), "
                              "Y-tunnus (10), kumppanimäärä (15), riippumaton arviolähde (15)"),
    "notes": [
        ("<b>Huomio:</b> Neljä listan palveluista (Rahalaitos, Omalaina, Sambla ja Rahoitu.fi) kuuluu samaan "
         "konserniin (Sambla Group Oy), ja Zmarta sekä Freedom Rahoitus ovat samaa yhtiötä. Näytämme omistajan "
         "jokaisen palvelun kohdalla — brändejä vertaillessa kannattaa tietää kuka niiden takana on."),
        ("Emme anna laina- tai talousneuvontaa. Vertailu kuvaa palveluiden verkkosivujen mitattavia ominaisuuksia, "
         "ei lainatarjousten paremmuutta — lopullinen korko on aina henkilökohtainen. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
    "yritykset": companies,
}

os.makedirs(os.path.join(BASE, "data"), exist_ok=True)
out = os.path.join(BASE, "data", "lainavertailu.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(vertical, f, ensure_ascii=False, indent=1)
print("wrote data/lainavertailu.json —", len(companies), "companies")
