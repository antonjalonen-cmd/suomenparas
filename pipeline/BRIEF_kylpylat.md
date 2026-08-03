# Extraction task — vertical `kylpylat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish spas and water parks (kylpylät), from the VISITOR's
perspective on the public site: is the day-pass price visible without logging in or giving
contact details? Can you buy a ticket online? Are the spa/sauna/pool facilities described?
Are opening hours and location clearly stated?

Write EXACTLY ONE file: pipeline/extracts/kylpylat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "paivylipun_hinta_esilla": "kylla|osittain|ei",   // Päivälipun hinta nähtävissä sivustolla ilman kirjautumista
 "varaus_verkossa": "kylla|osittain|ei",            // Lipun tai kylpyläpäivän voi ostaa tai varata verkossa
 "palvelut_kuvattu": "kylla|osittain|ei",           // Kylpylä-, sauna- ja vesipuistopalvelut kuvattu
 "sijainti_ja_aukioloajat": "kylla|osittain|ei",    // Sijainti ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",
 "riippumaton_arvio": "kylla|osittain|ei",
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
