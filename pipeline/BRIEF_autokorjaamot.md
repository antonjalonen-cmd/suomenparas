# Extraction task — vertical `autokorjaamot`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- MANY of these sites render prices with JavaScript (placeholders like "--", "%1", "0,00 $"
  in plain fetch): if you see a placeholder, you MUST retry with `--js` before scoring.
  On SPA sites fetch the front page `--raw`, grep hrefs, follow REAL nav links.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish car repair chains. Measures the PUBLIC site: are service prices or pricing basis public, does online booking work, are services described, are shops listed?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/autokorjaamot__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Huoltojen hinnat tai hinnoitteluperusteet julkisesti
 "ajanvaraus_verkossa": "kylla|osittain|ei",    // Ajanvaraus verkossa ilman yhteydenottoa
 "huoltopalvelut_kuvattu": "kylla|osittain|ei",    // Palveluvalikoima kuvattu selkeästi
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",    // Korjaamot ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "oljynvaihto_hinta_eur": <number|null>,   // advertised price of an oil change or basic service if any fixed price is public. null otherwise.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
