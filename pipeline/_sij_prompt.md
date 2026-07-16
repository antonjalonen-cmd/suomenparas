Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule.

Analyse **{DOMAIN}** (brand: {BRAND}) — INVESTMENT PLATFORM for Finnish retail investors (sijoitusalusta / osakekauppa). {NOTE}
Judge the investing/share-trading pages (osakkeet, kaupankäynti, hinnasto, arvo-osuustili). Only what a visitor sees WITHOUT logging in.

Work efficiently: ~8 pages max, then WRITE THE FILE. The written file is the only deliverable.
Write to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\sijoitusalustat__{SLUG}.json

Exact JSON (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "fetched_ok": ["<urls you actually loaded successfully>"],
 "kaupankayntikulut_ilman_kirjautumista": "kylla|osittain|ei",
 "sailytyspalkkio_kerrottu": "kylla|osittain|ei",
 "valuutanvaihtokulu_kerrottu": "kylla|osittain|ei",
 "hinnasto_ladattavissa": "kylla|osittain|ei",
 "y_tunnus_esilla": "kylla|ei",
 "y_tunnus": "<string or null>",
 "riippumaton_arvio": "kylla|osittain|ei",
 "asiakasarvio": {"arvosana": <number or null>, "maara": <int or null>, "lahde": "<string or null>"},
 "puhelin_esilla": "kylla|ei", "puhelin": "<string or null>",
 "email_esilla": "kylla|ei", "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei", "ukk_osio": "kylla|ei", "mobiilisovellus": "kylla|ei",
 "halvin_osakekauppa_eur": <number or null>,
 "markkinat": ["helsinki","tukholma","usa"],
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"kaupankayntikulut_ilman_kirjautumista": "<observation>", "sailytyspalkkio_kerrottu": "<observation>", "valuutanvaihtokulu_kerrottu": "<observation>"}
}

Meanings:
- kaupankayntikulut_ilman_kirjautumista: can an anonymous visitor see what a Helsinki share trade actually costs (euros or %), WITHOUT logging into online banking? IMPORTANT: for the banks (OP, Nordea, S-Pankki, Danske) pricing is often behind a bank login — if so that is "ei" (or "osittain" if a public price list exists elsewhere on the site).
- sailytyspalkkio_kerrottu: is the custody/account fee (säilytyspalkkio) stated publicly, including "0 euroa" if genuinely free?
- valuutanvaihtokulu_kerrottu: is the FX conversion cost for foreign trades stated (e.g. 0,25 %)?
- hinnasto_ladattavissa: is a full price list (hinnasto) publicly available/downloadable without login?
- riippumaton_arvio: INDEPENDENT source (EPSI, Trustpilot, an award from a named external body). Self-reported = "ei".
- halvin_osakekauppa_eur: cheapest publicly stated commission for a Finnish share trade. null if not visible. Do NOT guess.

NOTE: this compares WEBSITE TRANSPARENCY, not investment quality. Do not evaluate whether the platform is a good investment choice — only whether it tells you the costs before you sign up. This is not investment advice.

CRITICAL: `fetched_ok` must list only URLs that actually returned real content. If a page 404s or is blocked by a login/cookie wall, you did NOT see it — you may not claim an absence based on a page you could not load. When unsure, use "osittain", not "ei".

After writing, verify the file exists, then reply ONLY: "{SLUG} OK" plus one sentence on anything unusual.
