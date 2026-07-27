# -*- coding: utf-8 -*-
"""Tunnettuus pass -> pipeline/tunnettuus/<vertical>.json

Informational metric only — NEVER affects the score (build_vertical merges it
as display data). Proxy: average daily fi.wikipedia article page views over the
last 60 days (Wikimedia REST API, public and auditable).

Matching is deliberately conservative: the article title (minus parenthetical
disambiguator) must equal the company name, or the company name plus a
parenthetical. No confident match -> the company simply gets no tunnettuus row
("ei mitattavissa") instead of a wrong article's numbers.

Classes: >=1000 views/day Laaja · >=100 Kohtalainen · <100 Suppea.

Usage: python pipeline/fetch_tunnettuus.py <vertical> [<vertical> ...]
"""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import date, timedelta

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "pipeline"))
from companies import COMPANIES  # noqa: E402

OUT_DIR = os.path.join(BASE, "pipeline", "tunnettuus")
os.makedirs(OUT_DIR, exist_ok=True)
UA = {"User-Agent": "SuomenParasBot/1.0 (suomenparas.antonjalonen.fi; tunnettuus-mittaus)"}


def get_json(url):
    # Wikimedia throttles bursts — pace every call and retry once with backoff.
    # Failures must be VISIBLE: a silent None here turned a rate-limit into
    # "ei osumaa" for 40 verticals on the first run (26.7.2026).
    last = None
    for attempt in (1, 2, 3):
        try:
            time.sleep(0.4)
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as ex:
            last = ex
            print(f"    [retry {attempt}] {type(ex).__name__}: {ex}", flush=True)
            time.sleep(5 * attempt)
    raise last


def norm(s):
    return " ".join(s.lower().split())


# A plain-title match is not enough: "Kaleva" resolves to a disambiguation page
# and "Kide" to the crystal. The article must demonstrably be about an
# organisation/media/product, or carry a qualifying parenthetical.
BUSINESS_WORDS = ("yhtiö", "yritys", "lehti", "sanomalehti", "media", "ketju",
                  "kauppa", "palvelu", "pankki", "vakuutus", "operaattori",
                  "konserni", "verkkokauppa", "sovellus", "apteekki", "sairaala",
                  "yleisradio", "televisio", "uutis", "brändi", "valmistaja",
                  "tavaratalo", "ravintola", "hotelli", "lentoyhtiö", "kanava")
QUALIFIERS = ("yritys", "yhtiö", "sanomalehti", "lehti", "media", "kauppaketju",
              "verkkokauppa", "sovellus", "televisiokanava", "uutistoimisto")


def article_summary(title):
    t = urllib.parse.quote(title.replace(" ", "_"), safe="")
    return get_json(f"https://fi.wikipedia.org/api/rest_v1/page/summary/{t}")


def find_article(name):
    """Return a confidently matching fi.wikipedia title or None."""
    q = urllib.parse.quote(name)
    url = (f"https://fi.wikipedia.org/w/api.php?action=opensearch&search={q}"
           f"&limit=5&namespace=0&format=json")
    try:
        hits = get_json(url)[1]
    except Exception as ex:
        print(f"    haku epaonnistui ({type(ex).__name__}) — ohitetaan", flush=True)
        return None
    want = norm(name)
    for title in hits:
        base = norm(title.split(" (")[0])
        if base != want:
            continue
        paren = title[len(title.split(" (")[0]):].strip(" ()").lower()
        try:
            s = article_summary(title)
        except Exception as ex:
            print(f"    summary epaonnistui ({type(ex).__name__}) — ohitetaan", flush=True)
            continue
        if s.get("type") == "disambiguation":
            continue
        blob = norm((s.get("description") or "") + " " + (s.get("extract") or "")[:300])
        if (paren and any(w in paren for w in QUALIFIERS)) or any(w in blob for w in BUSINESS_WORDS):
            return title
        print(f"    '{title}' ei vaikuta yritykselta/medialta — ohitetaan", flush=True)
    return None


def avg_daily_views(title):
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=59)
    t = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
           f"fi.wikipedia/all-access/user/{t}/daily/"
           f"{start.strftime('%Y%m%d')}/{end.strftime('%Y%m%d')}")
    try:
        items = get_json(url).get("items") or []
    except Exception as ex:
        print(f"    katseludata epaonnistui ({type(ex).__name__}) — ohitetaan", flush=True)
        return None
    if not items:
        return None
    return round(sum(i.get("views", 0) for i in items) / len(items))


def luokka(views):
    # Calibrated 26.7.2026 against the measured distribution: fi.wikipedia
    # daily views run far lower than intuition suggests — Helsingin Sanomat ~79/d,
    # well-known chains 10-50/d, small firms 1-10/d. The first thresholds
    # (1000/100) would have labeled every company in Finland "Suppea".
    if views >= 50:
        return "Laaja"
    if views >= 10:
        return "Kohtalainen"
    return "Suppea"


def run(vertical):
    if vertical not in COMPANIES:
        raise SystemExit(f"unknown vertical: {vertical}")
    out, today = {}, date.today().strftime("%d.%m.%Y")
    for meta in COMPANIES[vertical]:
        name = meta["nimi"]
        title = find_article(name)
        if not title:
            print(f"  {meta['slug']}: ei varmaa fi-wikipedia-osumaa — ohitetaan")
            continue
        views = avg_daily_views(title)
        if views is None:
            print(f"  {meta['slug']}: artikkeli '{title}' loytyi mutta ei katseludataa — ohitetaan")
            continue
        out[meta["slug"]] = {
            "artikkeli": title,
            "paivakatselut_ka": views,
            "luokka": luokka(views),
            "lahde": f"fi.wikipedia-artikkelin '{title}' keskimaaraiset paivittaiset katselut 60 pv (Wikimedia-rajapinta), mitattu {today}",
            "mitattu": today,
        }
        print(f"  {meta['slug']}: '{title}' ~{views}/pv -> {luokka(views)}")
    p = os.path.join(OUT_DIR, f"{vertical}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"wrote {p} ({len(out)} yhtiota)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for v in sys.argv[1:]:
        print(f"== {v}")
        run(v)
