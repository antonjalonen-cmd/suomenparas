# Extraction task — vertical `virustorjuntaohjelmat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- These sites often render prices with JavaScript (placeholders in plain fetch): if you see
  a placeholder or a ~74-char shell, retry with `--js`. On SPA sites fetch `--raw`, grep
  hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Antivirus products sold to Finns. Measures the PUBLIC site: prices visible, RENEWAL price stated (the industry's dark pattern is a cheap first year), owner disclosed (Gen Digital owns 3 brands), independent test results shown, Finnish site?
It does NOT measure content/protection quality. Never score inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/virustorjuntaohjelmat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Hinnat julkisesti esillä
 "uusimishinta_kerrottu": "kylla|osittain|ei",    // Uusimishinta kerrottu (ei vain tarjoushinta)
 "omistaja_kerrottu": "kylla|osittain|ei",    // Omistava yhtiö kerrottu sivustolla
 "testitulokset_kerrottu": "kylla|osittain|ei",    // Riippumattomat testitulokset (AV-TEST tms.) esillä
 "suomenkielinen_palvelu": "kylla|osittain|ei",    // Suomenkielinen sivusto ja hinnat euroissa
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "uusimishinta_vuosi_eur": <number|null>,   // the stated RENEWAL yearly price of the basic product in EUR (not the first-year offer). null if renewal price is not stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
