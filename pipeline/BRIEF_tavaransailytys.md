# Extraction task — vertical `tavaransailytys`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- Suspiciously empty page: retry with `--js`; on SPA sites fetch the front page `--raw`,
  grep hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish consumer self-storage (tavaransailytys / vuokravarasto)
companies. Measures the PUBLIC site: are storage unit prices shown, can you rent online without
calling, are contract terms (cancellation, minimum period) explained, and is insurance or liability
for stored goods mentioned?
It does NOT measure the physical storage quality or safety. Never score anything from inside a
logged-in area.

NOTE: cityvarasto.fi returns 404 to a simple curl user-agent but works fine with a browser UA.
Use `python pipeline/fetch_page.py <url> --js` for this site. If the site is still bot-blocked,
record all fields as "osittain" with evidence "HAVAINTO: Sivusto esti automaattisen haun" — not
"ei", because a bot-blocked site may well have the information a human visitor can see.

Write EXACTLY ONE file: pipeline/extracts/tavaransailytys__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",    // Varastotilan hinta julkisesti esillä ilman yhteystietoja
 "varaus_verkossa": "kylla|osittain|ei",                     // Varauksen tai sopimuksen voi tehdä verkossa
 "sopimusehdot_kerrottu": "kylla|osittain|ei",               // Sopimusehdot (irtisanominen, sitoutumisaika) kerrottu
 "vakuutus_ja_vastuu_kerrottu": "kylla|osittain|ei",         // Vakuutusturva tai vastuu tavaroiden osalta kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",                     // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",                   // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "nelio_hinta_eur": <number|null>,   // cheapest published price per month for smallest unit (e.g. 1-2 m²), if stated. null otherwise.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation OR direct quote from site." }
}
Provide `evidence` for at least the six transparency fields.
