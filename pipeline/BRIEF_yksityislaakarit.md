# Extraction task — vertical `yksityislaakarit`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent.
- A BOT-BLOCKED OR COOKIE-WALLED PAGE MUST NOT BE SCORED AS AN OPAQUE PAGE. If a page
  comes back suspiciously empty, retry with `--js` (fetch_page.py renders JavaScript in
  headless Chrome), and if it still fails, SAY SO and use "osittain" — never "ei".
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish private healthcare chains. Measures the PUBLIC site: are appointment prices visible before booking, does booking work without login, is the Kela reimbursement explained? NOT a measure of care quality.
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/yksityislaakarit__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "vastaanottohinnat_esilla": "kylla|osittain|ei",    // Vastaanottojen hinnat julkisesti esillä
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
 "yleislaakari_hinta_eur": <number|null>,   // advertised price of a general practitioner appointment (20-30 min vastaanotto) BEFORE Kela reimbursement. null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
