# Extraction task — vertical `pilvitallennuspalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- MANY of these sites render prices with JavaScript (placeholders like "--", "%1", "0,00 $"
  in plain fetch): if you see a placeholder, you MUST retry with `--js` before scoring.
  On SPA sites fetch the front page `--raw`, grep hrefs, follow REAL nav links.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Cloud storage services sold to Finns. Measures the PUBLIC site: are EUR prices visible before signup, is renewal pricing stated, is there a Finnish-language site, is the owning company and data jurisdiction disclosed?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/pilvitallennuspalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Tallennustilan hinnat julkisesti esillä
 "uusimishinta_kerrottu": "kylla|osittain|ei",    // Uusimishinta kerrottu (ei vain tarjoushinta)
 "suomenkielinen_palvelu": "kylla|osittain|ei",    // Suomenkielinen sivusto ja hinnat euroissa
 "omistaja_kerrottu": "kylla|osittain|ei",    // Omistava yhtiö kerrottu sivustolla
 "datan_sijainti_kerrottu": "kylla|osittain|ei",    // Datan säilytysmaa tai lainkäyttöalue kerrottu
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "hinta_2tt_kk_eur": <number|null>,   // advertised monthly EUR price of the ~2TB consumer tier (the most comparable tier). null if not stated in EUR.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
