# Extraction task — vertical `salasananhallintapalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- MANY of these sites render prices with JavaScript (placeholders like "--", "%1", "0,00 $"
  in plain fetch): if you see a placeholder, you MUST retry with `--js` before scoring.
  On SPA sites fetch the front page `--raw`, grep hrefs, follow REAL nav links.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Password manager services sold to Finns. Measures the PUBLIC site: are prices visible before signup, are free-tier limits clear, are independent security audits published, is the owner disclosed?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/salasananhallintapalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Hinnat julkisesti esillä
 "ilmainen_versio_kerrottu": "kylla|osittain|ei",    // Ilmaisversion rajoitukset kerrottu selkeästi
 "turvallisuusauditoinnit": "kylla|osittain|ei",    // Riippumattomat tietoturva-auditoinnit julkaistu
 "omistaja_kerrottu": "kylla|osittain|ei",    // Omistava yhtiö kerrottu sivustolla
 "uusimishinta_kerrottu": "kylla|osittain|ei",    // Uusimishinta kerrottu (ei vain tarjoushinta)
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "premium_kk_hinta_eur": <number|null>,   // advertised monthly price of the individual premium tier in EUR (if only USD shown, put null and note the USD price in evidence).
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
