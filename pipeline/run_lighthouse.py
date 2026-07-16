# -*- coding: utf-8 -*-
"""Lighthouse mobile runs -> pipeline/lh_cache/<slug>.json

Why local npx and not the PageSpeed Insights API: the keyless PSI endpoint is
rate-limited into uselessness (429 even with 180s backoff, verified 15.7.2026).
Production should use PSI with an API key; local Lighthouse is the demo stand-in.

Known quirks handled here:
  - "Chrome kill" / non-zero exit is harmless — the JSON is still written.
  - NO_NAVSTART trace errors hit heavy JS sites intermittently; retry with
    longer waits before giving up.

Usage:  python pipeline/run_lighthouse.py <slug>=<domain> [<slug>=<domain> ...]
        python pipeline/run_lighthouse.py --file pipeline/targets.txt
"""
import json, os, subprocess, sys, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(BASE, "pipeline", "lh_cache")
os.makedirs(CACHE, exist_ok=True)

FLAGS = [
    "--only-categories=performance,accessibility,seo,best-practices",
    "--form-factor=mobile",
    "--screenEmulation.mobile",
    "--throttling-method=simulate",
    "--output=json",
    "--quiet",
    "--chrome-flags=--headless=new --no-sandbox --disable-gpu",
]
RETRY_FLAGS = ["--max-wait-for-load=60000", "--pause-after-fcp-ms=2000"]


def run(slug, domain, attempt=1):
    out = os.path.join(CACHE, f"{slug}.json")
    url = f"https://{domain}"
    cmd = ["npx", "--yes", "lighthouse", url, *FLAGS, f"--output-path={out}"]
    if attempt > 1:
        cmd += RETRY_FLAGS
    print(f"[{slug}] attempt {attempt}: {url}", flush=True)
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=300, shell=True)
    except subprocess.TimeoutExpired:
        print(f"[{slug}] TIMEOUT", flush=True)

    # Exit code is unreliable (Chrome kill); trust the artifact.
    if not os.path.exists(out):
        return None
    try:
        d = json.load(open(out, encoding="utf-8"))
    except Exception as ex:
        print(f"[{slug}] unreadable json: {ex}", flush=True)
        return None
    if d.get("runtimeError"):
        code = d["runtimeError"].get("code")
        print(f"[{slug}] runtimeError {code}", flush=True)
        os.remove(out)
        return None
    cats = d.get("categories", {})
    if cats.get("performance", {}).get("score") is None:
        print(f"[{slug}] no performance score", flush=True)
        os.remove(out)
        return None
    return {
        "performance": round(cats["performance"]["score"] * 100),
        "accessibility": round(cats["accessibility"]["score"] * 100),
        "seo": round(cats["seo"]["score"] * 100),
        "best_practices": round(cats["best-practices"]["score"] * 100),
        "lcp_ms": d["audits"]["largest-contentful-paint"]["numericValue"],
        "cls": d["audits"]["cumulative-layout-shift"]["numericValue"],
        "tbt_ms": d["audits"]["total-blocking-time"]["numericValue"],
        "lh_version": d.get("lighthouseVersion"),
        "fetched_url": d.get("finalDisplayedUrl") or d.get("finalUrl"),
    }


def main():
    args = sys.argv[1:]
    targets = []
    if args and args[0] == "--file":
        for line in open(args[1], encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                s, d = line.split("=", 1)
                targets.append((s.strip(), d.strip()))
    else:
        for a in args:
            s, d = a.split("=", 1)
            targets.append((s, d))

    summary = {}
    sum_path = os.path.join(CACHE, "_summary.json")
    if os.path.exists(sum_path):
        summary = json.load(open(sum_path, encoding="utf-8"))

    for slug, domain in targets:
        if slug in summary:
            print(f"[{slug}] cached, skipping", flush=True)
            continue
        res = None
        for attempt in (1, 2):
            res = run(slug, domain, attempt)
            if res:
                break
            time.sleep(3)
        if res:
            res["domain"] = domain
            summary[slug] = res
            print(f"[{slug}] OK perf={res['performance']} a11y={res['accessibility']} "
                  f"seo={res['seo']} bp={res['best_practices']}", flush=True)
        else:
            print(f"[{slug}] FAILED after retries", flush=True)
        with open(sum_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=1)

    print(f"\ndone — {len(summary)} measured, summary at pipeline/lh_cache/_summary.json")


if __name__ == "__main__":
    main()
