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
import glob, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_rules import TRANSPARENCY, REACH, AI
from companies import COMPANIES

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = missing = ok = 0

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
        if not fetched:
            errs.append("fetched_ok empty — cannot tell what it read")
        elif not any(base in u for u in fetched):
            errs.append(f"never loaded {meta['domain']}: {fetched}")
        # An agent that read a competitor's site names it in fetched_ok. Catch it.
        others = {c["domain"].replace("www.", "").lower()
                  for c in COMPANIES[vert] if c["slug"] != slug}
        for u in fetched:
            for o in others:
                if o in u:
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
