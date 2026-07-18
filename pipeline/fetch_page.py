# -*- coding: utf-8 -*-
"""Fetch a public page as a real browser sees it, and print it as plain text.

Why this exists (17.7.2026): the extraction agents' built-in WebFetch is blocked or
degraded by several of the sites we measure — op.fi and agria.fi return only a
consent/challenge shell to it. Agents then recorded "not stated" for things the page
states prominently, which is a MEASUREMENT ERROR, not a finding (the NordVPN lesson in
EXTRACTION_BRIEF.md, repeated). curl with an ordinary browser User-Agent gets the real
page: op.fi returns 225 kB of genuine content this way.

Worse, several agents responded to a blocked fetch by INVENTING an explanation
("risicum.fi redirects to saldo.com", "pohjantahti.fi redirects to fennia.fi",
"omasp.fi redirects to Danske Bank") — all false, all would have published one
company's data under a competitor's name. A fetch path that actually works removes the
pressure to confabulate.

This reads the company's OWN public website exactly as the brief requires. It is not a
third-party source.

--js mode (18.7.2026): some sites (op.fi, several healthcare/gym chains) ship an empty
HTML shell and render everything client-side, so curl sees ~900 chars of a 225 kB page.
--js renders the page in headless Chrome exactly the way Lighthouse already does for the
digital pillar, then dumps the resulting DOM. Boundaries, per QUEUED_CATEGORIES.md:
it does NOT click cookie banners (declining = not interacting; banner text may appear in
the output — ignore it), and it does NOT evade bot protection. If a site still serves a
challenge page to a rendering browser, that IS the finding: report it, don't work around
it. Rendering JavaScript is not a bypass; interacting with consent or challenges is.

Usage:  python pipeline/fetch_page.py <url> [--js] [--raw] [--max-chars N]
"""
import html as _html
import os
import re
import subprocess
import sys

# Finnish pages are full of characters cp1252 cannot encode; without this the whole
# fetch dies on a stray bullet and an agent is left with nothing but a traceback.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]


def fetch_js(url):
    """Render the page in headless Chrome (like Lighthouse does) and return the DOM.

    No interaction happens: no cookie clicks, no scrolling, no input. virtual-time-budget
    fast-forwards timers so client-side rendering settles before the dump.
    """
    chrome = next((p for p in CHROME_CANDIDATES if os.path.exists(p)), None)
    if not chrome:
        return "", "Chrome not found in standard locations"
    cmd = [chrome, "--headless=new", "--dump-dom", "--disable-gpu",
           "--no-first-run", "--mute-audio",
           "--accept-lang=fi-FI,fi",
           "--virtual-time-budget=15000",
           "--timeout=45000",
           url]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=120)
    return r.stdout or "", r.stderr or ""


def fetch(url):
    cmd = ["curl", "-sS", "-L", "--max-time", "45", "--ssl-no-revoke",
           "-A", UA,
           "-H", "Accept-Language: fi-FI,fi;q=0.9,en;q=0.8",
           "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-w", "\n<<<HTTP_STATUS:%{http_code} FINAL_URL:%{url_effective}>>>",
           url]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=90)
    return r.stdout or "", r.stderr or ""


def to_text(doc):
    doc = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", doc)
    doc = re.sub(r"(?is)<!--.*?-->", " ", doc)
    doc = re.sub(r"(?i)<(br|/p|/div|/li|/h[1-6]|/tr)[^>]*>", "\n", doc)
    doc = re.sub(r"(?s)<[^>]+>", " ", doc)
    doc = _html.unescape(doc)
    doc = re.sub(r"[ \t ]+", " ", doc)
    doc = re.sub(r"\n\s*\n+", "\n", doc)
    return doc.strip()


def main():
    args = [a for a in sys.argv[1:]]
    raw = "--raw" in args
    if raw:
        args.remove("--raw")
    use_js = "--js" in args
    if use_js:
        args.remove("--js")
    max_chars = 40000
    if "--max-chars" in args:
        i = args.index("--max-chars")
        max_chars = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        raise SystemExit(__doc__)
    url = args[0]
    if use_js:
        out, err = fetch_js(url)
    else:
        out, err = fetch(url)
    if not out.strip():
        print(f"FETCH FAILED for {url}\nstderr: {err.strip()[:500]}")
        print("Do NOT invent a reason for this. Report the failure and score 'osittain'.")
        if not use_js:
            print("If this site may be JS-rendered, retry with --js before concluding anything.")
        return
    status = "rendered in headless Chrome (JS executed)" if use_js else ""
    m = re.search(r"<<<HTTP_STATUS:(\d+) FINAL_URL:([^>]*)>>>", out)
    if m:
        status = f"HTTP {m.group(1)}  final URL: {m.group(2)}"
        out = out[:m.start()]
    body = out if raw else to_text(out)
    print(f"=== {url}\n=== {status}\n=== {len(body)} chars\n")
    print(body[:max_chars])
    if len(body) > max_chars:
        print(f"\n[...truncated, {len(body) - max_chars} more chars. "
              f"Re-run with --max-chars to see more.]")


if __name__ == "__main__":
    main()
