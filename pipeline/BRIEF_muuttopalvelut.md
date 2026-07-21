# Extraction task — vertical `muuttopalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- Suspiciously empty page: retry with `--js`; on SPA sites fetch the front page `--raw`,
  grep hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish national moving companies. Measures the PUBLIC site: are prices/pricing basis stated, can you get a quote online without calling, are insurance and damage liability explained?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/muuttopalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Muuton hinnat tai hinnoitteluperusteet julkisesti esillä
 "tarjouslaskuri_verkossa": "kylla|osittain|ei",    // Hinta-arvion saa verkossa ilman soittoa
 "vakuutus_ja_vastuu_kerrottu": "kylla|osittain|ei",    // Vakuutus ja vastuu vahingoista kerrottu
 "toimialue_ja_yhteystiedot": "kylla|osittain|ei",    // Toimialue ja yhteystiedot kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "tuntihinta_eur": <number|null>,   // advertised hourly rate for a standard move (e.g. 2 movers + van), if stated. null otherwise.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
