# -*- coding: utf-8 -*-
"""Svensk spegel: build /sv/ mirror of every generated page.

Approach (26.7.2026): post-process the GENERATED Finnish HTML instead of
refactoring gen_site.py's ~2000 lines of embedded Finnish. Text nodes and
selected attributes are swapped via a persistent fi->sv cache
(pipeline/sv_cache.json). Segments with no cached translation are exported to
pipeline/sv_missing/batch_NNN.json for translation agents; --apply merges the
translated batch files back into the cache. Re-running is idempotent and only
new/changed copy ever needs translating again.

Usage:
  python translate_site.py --extract   # scan pages, write missing batches, report
  python translate_site.py --apply     # merge sv_missing/batch_*.sv.json into cache
  python translate_site.py --build     # write sv/ mirror + language toggles
"""
import json, os, re, shutil, sys
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
CACHE_P = os.path.join(BASE, "pipeline", "sv_cache.json")
MISS_DIR = os.path.join(BASE, "pipeline", "sv_missing")
SV_DIR = os.path.join(BASE, "sv")
BATCH = 400

SKIP_TAGS = {"script", "style", "code", "pre"}
ATTR_TRANSLATE = {"content", "alt", "placeholder", "title", "aria-label"}
# do not translate meta charset/viewport etc: only meta name=description content
NO_TEXT = re.compile(r"^[\s\d\W_]+$", re.UNICODE)  # numbers/punct/whitespace only


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def wants_translation(s):
    t = norm(s)
    if not t or len(t) < 2:
        return False
    if NO_TEXT.match(t):
        return False
    if t.startswith("http") or "@" in t and " " not in t:
        return False
    return True


def load_cache():
    if os.path.exists(CACHE_P):
        return json.load(open(CACHE_P, encoding="utf-8-sig"))
    return {}


def pages():
    out = []
    for root, dirs, files in os.walk(BASE):
        rel = os.path.relpath(root, BASE)
        # kysy-kaverilta = konseptidemo, ei tuotantosivustoa -> ei myoskaan sv-peiliin
        if rel.split(os.sep)[0] in ("sv", "pipeline", "node_modules", ".git", "data", "assets",
                                    "kysy-kaverilta"):
            continue
        for f in files:
            if f == "index.html":
                out.append(os.path.join(root, f))
    return sorted(out)


class Segmenter(HTMLParser):
    """Collect translatable segments from one page."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.segs = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        d = dict(attrs)
        if tag == "meta" and d.get("name") == "description" and d.get("content"):
            self.segs.append(d["content"])
        else:
            for k, v in attrs:
                if k in ("alt", "placeholder", "title", "aria-label") and v:
                    self.segs.append(v)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if self.stack and self.stack[-1] in SKIP_TAGS:
            return
        if wants_translation(data):
            self.segs.append(norm(data))


def collect():
    segs = {}
    for p in pages():
        html = open(p, encoding="utf-8").read()
        s = Segmenter()
        s.feed(html)
        # <title> is data inside title tag — captured by handle_data
        for seg in s.segs:
            t = norm(seg)
            if wants_translation(t):
                segs.setdefault(t, 0)
                segs[t] += 1
    return segs


def cmd_extract():
    cache = load_cache()
    segs = collect()
    missing = sorted(t for t in segs if t not in cache)
    os.makedirs(MISS_DIR, exist_ok=True)
    for f in os.listdir(MISS_DIR):
        if f.endswith(".json") and not f.endswith(".sv.json"):
            os.remove(os.path.join(MISS_DIR, f))
    for i in range(0, len(missing), BATCH):
        p = os.path.join(MISS_DIR, f"batch_{i // BATCH:03d}.json")
        json.dump(missing[i:i + BATCH], open(p, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=0)
    print(f"segments total: {len(segs)} | cached: {len(segs) - len(missing)} | "
          f"missing: {len(missing)} -> {(len(missing) + BATCH - 1) // BATCH} batch files in pipeline/sv_missing/")


def cmd_apply():
    cache = load_cache()
    added = 0
    for f in sorted(os.listdir(MISS_DIR)):
        if not f.endswith(".sv.json"):
            continue
        src = os.path.join(MISS_DIR, f.replace(".sv.json", ".json"))
        if not os.path.exists(src):
            continue
        fi = json.load(open(src, encoding="utf-8-sig"))
        sv = json.load(open(os.path.join(MISS_DIR, f), encoding="utf-8-sig"))
        if len(fi) != len(sv):
            print(f"SKIP {f}: length mismatch {len(fi)} vs {len(sv)}")
            continue
        for a, b in zip(fi, sv):
            if isinstance(b, str) and b.strip():
                cache[norm(a)] = b.strip()
                added += 1
    json.dump(cache, open(CACHE_P, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"cache now {len(cache)} entries (+{added})")


# Lippukytkin (28.7.2026): fi-sivulla Ruotsin lippu, sv-sivulla Suomen lippu.
# Inline-SVG, koska sivusto on staattinen eika kaannoskerros saa koskea siihen.
FLAG_SE = ('<svg class="flagsvg" viewBox="0 0 16 10" width="26" height="17" aria-hidden="true">'
           '<rect width="16" height="10" fill="#005293"/>'
           '<rect x="5" width="2" height="10" fill="#FECB00"/>'
           '<rect y="4" width="16" height="2" fill="#FECB00"/></svg>')
FLAG_FI = ('<svg class="flagsvg" viewBox="0 0 16 10" width="26" height="17" aria-hidden="true">'
           '<rect width="16" height="10" fill="#fff"/>'
           '<rect x="5" width="2.4" height="10" fill="#003580"/>'
           '<rect y="4" width="16" height="2.4" fill="#003580"/></svg>')


def toggle_html(href, flag, label, lang):
    """Lippulinkki. Teksti jaa ruudunlukijalle, visuaalisesti nakyy lippu."""
    return (f'<a class="langsw" href="{href}" lang="{lang}" title="{label}" '
            f'aria-label="{label}">{flag}<span class="sr">{label}</span></a>')

# Lippu sijoitetaan navin VIIMEISEKSI (oikea ylakulma), ei ensimmaiseksi.
NAV_END_RE = re.compile(r'(<nav class="main">.*?)(</nav>)', re.S)
# --build kirjoittaa kytkimen myos fi-sivulle levylle, joten pelkka uusinta-ajo
# ilman gen_site.py:ta kasaisi nappeja paallekkain. Vanhat siivotaan aina ensin.
LANGSW_RE = re.compile(r'<a class="langsw".*?</a>', re.S)


def set_toggle(html, toggle):
    """Poista mahdolliset vanhat kielikytkimet ja lisaa tasan yksi navin loppuun."""
    html = LANGSW_RE.sub("", html)
    return NAV_END_RE.sub(lambda m: m.group(1) + toggle + m.group(2), html, count=1)


def translate_html(html, cache):
    out = []
    pos = 0
    # Walk with a tolerant regex over tags; translate the text between them.
    # (The generator emits well-formed HTML, so tag-boundary splitting is safe.)
    parts = re.split(r"(<[^>]+>)", html)
    in_skip = None
    for part in parts:
        if part.startswith("<"):
            m = re.match(r"<\s*(/?)([a-zA-Z0-9]+)", part)
            if m:
                closing, tag = m.group(1), m.group(2).lower()
                if tag in SKIP_TAGS:
                    in_skip = None if closing else tag
            # attribute translation
            def attr_sub(am):
                k, q, v = am.group(1), am.group(2), am.group(3)
                t = norm(v)
                if k in ("alt", "placeholder", "title", "aria-label", "content") and t in cache:
                    if k == "content" and 'name="description"' not in part and "name='description'" not in part:
                        return am.group(0)
                    return f"{k}={q}{cache[t]}{q}"
                return am.group(0)
            part = re.sub(r"([a-zA-Z-]+)=([\"'])([^\"']*)\2",
                          lambda am: attr_sub(am), part)
            out.append(part)
        else:
            if in_skip:
                out.append(part)
                continue
            # HTMLParser (poiminta) katkaisee tekstisolmun entiteetin kohdalta,
            # joten valimuistin avaimet ovat entiteettien valisia paloja. Sama
            # jako on tehtava tassa, muuten esim. "... mittausdatasta &mdash; emme
            # kirjoita ..." ei osu mihinkaan avaimeen ja jaa kokonaan suomeksi.
            for piece in re.split(r"(&[a-zA-Z]+;|&#\d+;)", part):
                t = norm(piece)
                if t and not piece.startswith("&") and t in cache:
                    lead = piece[:len(piece) - len(piece.lstrip())]
                    tail = piece[len(piece.rstrip()):]
                    out.append(lead + cache[t] + tail)
                else:
                    out.append(piece)
    return "".join(out)


def cmd_build():
    cache = load_cache()
    if os.path.isdir(SV_DIR):
        shutil.rmtree(SV_DIR)
    n = 0
    for p in pages():
        rel = os.path.relpath(p, BASE).replace(os.sep, "/")
        html = open(p, encoding="utf-8").read()
        depth = rel.count("/")
        root = "../" * depth  # original page's root prefix

        # 1) fi page gets an SV toggle
        fi_toggle = toggle_html(f'{root}sv/{rel.rsplit("/", 1)[0] + "/" if depth else ""}',
                                FLAG_SE, "Svenska", "sv")
        fi_html = set_toggle(html, fi_toggle)
        open(p, "w", encoding="utf-8").write(fi_html)

        # 2) sv mirror (same relative structure inside sv/ so page links stay sv)
        sv = translate_html(html, cache)
        sv = sv.replace('<html lang="fi">', '<html lang="sv">')
        # Kysy kaverilta on toistaiseksi vain suomeksi -> linkki pois sv-navista,
        # muuten se osoittaisi sv-puun sisalle sivulle jota ei ole.
        sv = re.sub(r'<a href="[^"]*kysy-kaverilta/"[^>]*>[^<]*</a>\s*', "", sv)
        sv_root_to_fi = "../" * (depth + 1)
        sv_toggle = toggle_html(f'{sv_root_to_fi}{rel.rsplit("/", 1)[0] + "/" if depth else ""}',
                                FLAG_FI, "Suomeksi", "fi")
        sv = set_toggle(sv, sv_toggle)
        dest = os.path.join(SV_DIR, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(sv)
        n += 1
    # assets duplicated so sv pages' relative asset paths resolve
    shutil.copytree(os.path.join(BASE, "assets"), os.path.join(SV_DIR, "assets"))
    if os.path.isdir(os.path.join(BASE, "data")):
        shutil.copytree(os.path.join(BASE, "data"), os.path.join(SV_DIR, "data"))
    print(f"sv mirror: {n} pages + assets")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--extract":
        cmd_extract()
    elif arg == "--apply":
        cmd_apply()
    elif arg == "--build":
        cmd_build()
    else:
        raise SystemExit(__doc__)
