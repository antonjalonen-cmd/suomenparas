# -*- coding: utf-8 -*-
"""Validate batch extracts BEFORE they can reach a page.

Written 17.7.2026 after three separate Haiku agents invented redirect chains
("risicum.fi redirects to saldo.com", "resursbank.fi redirects to tfbank.fi",
"lahitapiola.fi is not accessible") for sites that in fact return HTTP 200. Two of
those would have published a competitor's website under the wrong company's name.
build_vertical.py already refuses such an extract; this reports them all at once
instead of dying on the first.

Usage: python pipeline/check_extracts.py <vertical> [<vertical> ...]
"""
import glob
import re, json, os, sys
import urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_rules import TRANSPARENCY, REACH, AI
from companies import COMPANIES

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = missing = ok = 0

# fetched_ok-URLien statustarkistus (4.8.2026). Portti tarkisti aiemmin VAIN etta
# URL sisaltaa oikean domainin — ei sita, ETTA SIVU ON OLEMASSA. 4.8.2026 tikki
# kirjoitti autotarvikkeet-verkossa-kategoriaan 28 fetched_ok-URLia, joista 9 ei
# palauta 200: keksittyja suomalaisilta kuulostavia polkuja (/toimitusehdot/,
# /asiakaspalvelu/, /yhteystiedot) joista oli silti siteerattu tarkkoja
# euromaaria ("333,32 EUR", "ILMAINEN yli 80.00 EUR"). Mukana seka kategorian
# ykkonen etta viimeinen. 404 = sivua ei ole = evidenssi on keksitty, ja se on
# hard fail. 403/429 on todennakoinen bottiesto, joten se on vain varoitus:
# oikea sivu voi hyvin torjua urllibin mutta paastaa selaimen lapi.
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}
SKIP_URL_CHECK = "--no-url-check" in sys.argv


def url_status(u):
    try:
        return urllib.request.urlopen(
            urllib.request.Request(u, headers=UA), timeout=25).getcode()
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR {type(e).__name__}"

for vert in sys.argv[1:]:
    for meta in COMPANIES[vert]:
        slug = meta["slug"]
        p = os.path.join(BASE, "pipeline", "extracts", f"{vert}__{slug}.json")
        if not os.path.exists(p):
            print(f"MISSING  {vert}__{slug}")
            missing += 1
            continue
        try:
            e = json.load(open(p, encoding="utf-8-sig"))
        except Exception as ex:
            print(f"BADJSON  {vert}__{slug}: {ex}")
            bad += 1
            continue
        errs = []
        base = meta["domain"].replace("www.", "").lower()
        fetched = [str(u).lower() for u in (e.get("fetched_ok") or [])]
        # Verticals measured 15.–16.7.2026 predate this gate; their extracts never had a
        # fetched_ok field, and that absence is not retroactive evidence of a bad fetch.
        # The requirement is absolute for everything measured after the gate existed.
        legacy = "fetched_ok" not in e and vert in (
            "lainavertailu", "vakuutukset", "sahkosopimukset", "laajakaista",
            "puhelinliittymat", "luottokortit", "sijoitusalustat", "webhotellit",
            "vpn-palvelut")
        if not fetched:
            if not legacy:
                errs.append("fetched_ok empty — cannot tell what it read")
        elif not any(base in u for u in fetched):
            errs.append(f"never loaded {meta['domain']}: {fetched}")
        if fetched and not SKIP_URL_CHECK:
            for u in (e.get("fetched_ok") or []):
                st = url_status(str(u))
                if st in (404, 410):
                    errs.append(f"fetched_ok-URL {u} palauttaa {st} — sivua EI OLE "
                                f"olemassa, joten siita siteerattu evidenssi on "
                                f"keksitty. Hae oikeat polut sivuston hrefeista.")
                elif st != 200:
                    print(f"         (varoitus) {vert}__{slug}: {u} -> {st} "
                          f"(mahdollinen bottiesto, tarkista kasin)")
        # An agent that read a competitor's site names it in fetched_ok. Catch it.
        # Exception: a URL on another listed company's domain whose PATH names this
        # product is the product's OWN page on a shared issuer platform, not competitor
        # data (K-Plussa Maksuaika lives at op.fi/.../k-plussa-maksuaika because OP
        # issues the card — reading it is required, not a mixup).
        others = {c["domain"].replace("www.", "").lower()
                  for c in COMPANIES[vert] if c["slug"] != slug}
        own_tokens = [t for t in slug.lower().split("-") if len(t) > 2]
        for u in fetched:
            for o in others:
                if o in u and not any(t in u for t in own_tokens):
                    errs.append(f"fetched a COMPETITOR's site ({o}) — would publish "
                                f"the wrong company's data")
        for k, _, _ in TRANSPARENCY[vert] + REACH:
            v = e.get(k)
            if v not in ("kylla", "osittain", "ei"):
                errs.append(f"{k}={v!r} not a ternary value")
        a = e.get("ai_arviot") or {}
        for k, _, _ in AI:
            if not isinstance(a.get(k), (int, float)):
                errs.append(f"ai_arviot.{k} missing/not a number (got {list(a)})")
        # An all-zero ai_arviot is never a real judgement of a live page — it is what an
        # agent writes when it saw nothing and scored the nothing. Fennia's autovakuutus
        # page (21 000 chars, loads fine) came back 0/0/0 on 17.7.2026 from an agent that
        # claimed the content was unreachable. Zero is a valid number, so the type check
        # let it through to a published 50.3 score. It is not valid data.
        if a and all(a.get(k) == 0 for k, _, _ in AI):
            errs.append("ai_arviot is 0/0/0 — the agent scored a page it never read")
        if any((e.get(k) or "").startswith("Ei voida arvioida") for k in ("vahvuudet",)
               for k in []):
            pass
        filler = [x for x in (e.get("vahvuudet") or []) + (e.get("kehityskohteet") or [])
                  if "ei voida arvioida" in str(x).lower() or "ei saatavilla" == str(x).lower()]
        if filler:
            errs.append(f"placeholder text instead of findings: {filler[:1]}")
        for k in ("vahvuudet", "kehityskohteet"):
            if len(e.get(k) or []) != 3:
                errs.append(f"{k} has {len(e.get(k) or [])} items, need 3")
        if not (e.get("yhteenveto") or "").strip():
            errs.append("yhteenveto empty")
        # Umlautit ASCII-korvikkeina (3.-4.8.2026). Tikit ovat kirjoittaneet
        # julkaistavaa suomea muodossa "poerssilistattu", "Koopenhamminassa",
        # "aaanikirjoja", "tytaryhtion", "paakaupunkiseudulla" ja "sisaan" — kaikki
        # menivat liveen, koska pelkka kehotus promptissa ei pida. Portti on ainoa
        # tapa pysayttaa ne. Sanalista, ei heuristiikka: vaarat positiiviset
        # (esim. vieraskieliset nimet) maksaisivat enemman kuin hyoty.
        # Skannataan VAIN nakyvat arvomerkkijonot. Avaimet ovat tunnisteita
        # (bonusjarjestelma_kerrottu, lisamaksut_nakyy_varauksessa) ja URLit
        # ovat URLeja — kumpikaan ei saa laueta.
        # Kaksi listaa: harvinaiset turmeltumat osamerkkijonoina (eivat voi osua
        # vaarin), tavalliset sanat sanarajoilla — muuten "korvauksetta" laukaisee
        # "etta"-osuman (117 vaaraa positiivista ensimmaisessa versiossa).
        ASCII_SUB = ["aaanikirj", "poerss", "koopenhamm", "tytaryhtio",
                     "paakaupunki", "jarjestelma", "kayttaja", "tyontekij"]
        ASCII_WORD = ["etta", "seka", "myos", "nakyy", "sisaan", "loydy", "loydat",
                      "selkeasti", "esilla", "sahkoposti", "kaannos", "paivays"]
        TERNARY_VALUES = {"kylla", "osittain", "ei"}
        SKIP_VALUE_KEYS = {"slug", "domain", "y_tunnus", "fetched_ok", "url", "updated"}

        def _strings(node, key=""):
            if isinstance(node, dict):
                for k, v in node.items():
                    yield from _strings(v, k)
            elif isinstance(node, list):
                for v in node:
                    yield from _strings(v, key)
            elif isinstance(node, str) and key not in SKIP_VALUE_KEYS:
                if node.strip().lower() not in TERNARY_VALUES and "://" not in node:
                    yield node

        blob = " ".join(_strings(e)).lower()
        hits = sorted({w for w in ASCII_SUB if w in blob}
                      | {w for w in ASCII_WORD
                         if re.search(r"(?<![a-zäö])" + w + r"(?![a-zäö])", blob)})
        if hits:
            errs.append(f"ASCII-korvikeumlautteja suomenkielisessa tekstissa: {hits} "
                        f"— kirjoita a-umlaut ja o-umlaut oikein")
        if errs:
            bad += 1
            print(f"FAIL     {vert}__{slug}")
            for x in errs:
                print(f"           - {x}")
        else:
            ok += 1

# Orphans: an extract for a company the vertical no longer lists. Harmless today, because
# build_vertical only reads COMPANIES — but it is a loaded gun. On 17.7.2026 a stalled
# agent woke up two hours late and wrote an extract for Pohjola, who had been excluded in
# the meantime for being unreadable; two more orphans were already committed. Every one of
# them recorded a blocked read as though it were an absence. Re-add the company later and
# build_vertical would silently score it from that garbage — exactly the error the
# exclusion existed to prevent. Report them so the choice is deliberate.
orphans = []
for vert in sys.argv[1:]:
    listed = {c["slug"] for c in COMPANIES.get(vert, [])}
    for f in glob.glob(os.path.join(BASE, "pipeline", "extracts", f"{vert}__*.json")):
        slug = os.path.basename(f)[len(vert) + 2:-5]
        if slug not in listed:
            orphans.append(f"{vert}__{slug}")
if orphans:
    print("\nORPHAN extracts (company is not in COMPANIES[vertical]) — delete them, or "
          "re-add the company deliberately. Do not leave them to be picked up later:")
    for o in orphans:
        print(f"  {o}")

print(f"\n{ok} ok | {bad} bad | {missing} missing | {len(orphans)} orphan")
sys.exit(1 if (bad or missing) else 0)
