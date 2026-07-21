# Extraction task — vertical `hammaslaakarit`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish private dental chains. Measures the PUBLIC site: are treatment prices visible before booking, does online booking work without login, is the Kela reimbursement explained? NOT a measure of care quality.
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/hammaslaakarit__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "vastaanottohinnat_esilla": "kylla|osittain|ei",    // Hammashoidon hinnat julkisesti esillä
 "ajanvaraus_ilman_kirjautumista": "kylla|osittain|ei",    // Ajanvaraus verkossa ilman kirjautumista
 "kela_korvaus_kerrottu": "kylla|osittain|ei",    // Kela-korvaus ja todellinen omavastuu kerrottu
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",    // Toimipisteet ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "tarkastus_hinta_eur": <number|null>,   // advertised price of a dentist examination (hammaslaakarin tutkimus/tarkastus) BEFORE Kela reimbursement. null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
