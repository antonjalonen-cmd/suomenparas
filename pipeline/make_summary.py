#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Populate lh_cache/_summary.json from existing individual lh_cache/*.json files."""
import json, os, glob, sys

vertical = sys.argv[1] if len(sys.argv) > 1 else None

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(BASE, "pipeline", "lh_cache")
sum_path = os.path.join(CACHE, "_summary.json")

try:
    summary = json.load(open(sum_path, encoding="utf-8"))
except Exception:
    summary = {}

print(f"Existing summary keys: {len(summary)}")

# Read targets.txt for slug->domain mapping
targets = {}
for line in open(os.path.join(BASE, "pipeline", "targets.txt"), encoding="utf-8"):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        s, d = line.split("=", 1)
        targets[s.strip()] = d.strip()

pattern = os.path.join(CACHE, f"{vertical}__*.json" if vertical else "*.json")
added = 0
for f in sorted(glob.glob(pattern)):
    slug = os.path.basename(f).replace(".json", "")
    if slug == "_summary":
        continue
    if slug in summary:
        print(f"  ALREADY: {slug}")
        continue
    try:
        d = json.load(open(f, encoding="utf-8-sig"))
    except Exception as ex:
        print(f"  BAD JSON {slug}: {ex}")
        continue
    if d.get("runtimeError"):
        code = d["runtimeError"].get("code", "?")
        print(f"  RUNTIME ERROR {slug}: {code}")
        continue
    cats = d.get("categories", {})
    if cats.get("performance", {}).get("score") is None:
        print(f"  NO PERF SCORE {slug}")
        continue
    rec = {
        "performance": round(cats["performance"]["score"] * 100),
        "accessibility": round(cats["accessibility"]["score"] * 100),
        "seo": round(cats["seo"]["score"] * 100),
        "best_practices": round(cats["best-practices"]["score"] * 100),
        "lcp_ms": d["audits"]["largest-contentful-paint"]["numericValue"],
        "cls": d["audits"]["cumulative-layout-shift"]["numericValue"],
        "tbt_ms": d["audits"]["total-blocking-time"]["numericValue"],
        "lh_version": d.get("lighthouseVersion"),
        "fetched_url": d.get("finalDisplayedUrl") or d.get("finalUrl"),
        "domain": targets.get(slug, ""),
    }
    summary[slug] = rec
    print(f"  OK {slug}: perf={rec['performance']} seo={rec['seo']}")
    added += 1

if added > 0:
    with open(sum_path, "w", encoding="utf-8") as fp:
        json.dump(summary, fp, ensure_ascii=False, indent=1)
    print(f"Wrote {sum_path} ({len(summary)} total entries, +{added} new)")
else:
    print("Nothing new to add")
