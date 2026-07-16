Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule.

Analyse **{DOMAIN}** for the CREDIT CARD "{BRAND}" (Finnish consumer luottokortti). {NOTE}
Judge THAT CARD's public pages (kortit, luottokortti, hinnasto, ehdot, asiakaspalvelu). Only what a visitor sees WITHOUT logging in.

Work efficiently: ~8 pages max, then WRITE THE FILE. The written file is the only deliverable.
Write to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\luottokortit__{SLUG}.json

Exact JSON (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "fetched_ok": ["<urls you actually loaded successfully>"],
 "korko_ja_vuosikorko_esilla": "kylla|osittain|ei",
 "vuosimaksu_esilla": "kylla|osittain|ei",
 "muut_kulut_esilla": "kylla|osittain|ei",
 "luotonmyontaja_kerrottu": "kylla|osittain|ei",
 "y_tunnus_esilla": "kylla|ei",
 "y_tunnus": "<string or null>",
 "riippumaton_arvio": "kylla|osittain|ei",
 "asiakasarvio": {"arvosana": <number or null>, "maara": <int or null>, "lahde": "<string or null>"},
 "puhelin_esilla": "kylla|ei", "puhelin": "<string or null>",
 "email_esilla": "kylla|ei", "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei", "ukk_osio": "kylla|ei", "mobiilisovellus": "kylla|ei",
 "todellinen_vuosikorko_pct": <number or null>,
 "vuosimaksu_eur": <number or null>,
 "korttityyppi": "luottokortti|maksuaikakortti",
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"korko_ja_vuosikorko_esilla": "<observation>", "vuosimaksu_esilla": "<observation>", "luotonmyontaja_kerrottu": "<observation>"}
}

Meanings:
- korko_ja_vuosikorko_esilla: is the nominal interest AND todellinen vuosikorko (APR) publicly visible without applying/logging in? Finnish law (Kuluttajansuojalaki 7:8) requires this disclosure — so this measures whether they meet their own legal duty in public. "kylla" only if a real number appears.
- vuosimaksu_esilla: annual fee in euros publicly stated (including "0 €" if genuinely free)?
- muut_kulut_esilla: other costs — käteisnostopalkkio, valuutanvaihtolisä, viivästyskorko — publicly stated?
- luotonmyontaja_kerrottu: does the page say WHO actually grants the credit? Co-branded cards are often issued by a different bank than the brand on the card. "kylla" = the issuing entity is named plainly.
- korttityyppi: "maksuaikakortti" = charge card, balance due in full monthly (e.g. Amex) — the interest-cap framing does not apply the same way. Otherwise "luottokortti".
- riippumaton_arvio: INDEPENDENT source (EPSI, Trustpilot). Self-reported = "ei".
- todellinen_vuosikorko_pct / vuosimaksu_eur: the publicly stated figures. null if not visible. Do NOT guess.

CRITICAL: `fetched_ok` must list only URLs that actually returned real content. If a page 404s or is blocked by a login/cookie wall, you did NOT see it — you may not claim an absence based on a page you could not load. When unsure, use "osittain", not "ei".

After writing, verify the file exists, then reply ONLY: "{SLUG} OK" + one sentence on anything unusual.
