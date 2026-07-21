# Extraction task — vertical `pakohuoneet`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish multi-city escape room companies. Measures the PUBLIC site: are game prices visible, does online booking work without contacting, are rooms/difficulty/player counts described, are locations and hours listed?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/pakohuoneet__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Pelien hinnat julkisesti esillä
 "varaus_verkossa": "kylla|osittain|ei",    // Varauskalenteri toimii verkossa ilman yhteydenottoa
 "pelit_kuvattu": "kylla|osittain|ei",    // Huoneet, vaikeustasot ja pelaajamäärät kuvattu
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",    // Toimipisteet ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "pelin_hinta_alkaen_eur": <number|null>,   // cheapest advertised price for one game (per group or per person - state which in evidence). null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
