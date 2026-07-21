# Extraction task — vertical `lakifirmat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish consumer legal services (digital document services + multi-office law firms). Measures the PUBLIC site: are prices (hourly or fixed) stated before contact, is the lawyers' qualification (asianajaja/varatuomari/lakimies) disclosed, are engagement terms public? NOT a measure of legal quality.
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/lakifirmat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Hinnat (tuntihinta tai kiinteä hinta) julkisesti esillä
 "palvelun_sisalto_kuvattu": "kylla|osittain|ei",    // Palvelun sisältö (mitä hintaan kuuluu) kuvattu
 "patevyys_kerrottu": "kylla|osittain|ei",    // Juristien pätevyys (asianajaja/varatuomari/lakimies) kerrottu
 "sopimusehdot_saatavilla": "kylla|osittain|ei",    // Toimeksiannon ehdot julkisesti saatavilla
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "esimerkkihinta_eur": <number|null>,   // cheapest clearly advertised consumer price (a fixed-price document or stated hourly rate). null if no price is publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
