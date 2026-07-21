# Extraction task — vertical `rengasliikkeet`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish tyre shop chains. Measures the PUBLIC site: are tyre prices public (webshop/price list), are installation and tyre-hotel prices stated, does online booking work, are stores listed?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/rengasliikkeet__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "renkaiden_hinnat_esilla": "kylla|osittain|ei",    // Renkaiden hinnat julkisesti esillä
 "asennus_ja_sailytys_hinnat": "kylla|osittain|ei",    // Asennuksen ja rengassäilytyksen hinnat kerrottu
 "ajanvaraus_verkossa": "kylla|osittain|ei",    // Ajanvaraus verkossa ilman yhteydenottoa
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",    // Toimipisteet ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "renkaanvaihto_hinta_eur": <number|null>,   // advertised price of a seasonal tyre change (renkaanvaihto/kausivaihto). null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
