# Extraction task — vertical `kukkakauppojen-verkkokaupat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish online flower shops. Measured from the BUYER's
perspective on the public site: are product prices visible online, are delivery methods
and COSTS (rahti, kantopalvelu, vanhan poisvienti) stated before checkout, are return
and warranty terms publicly available, are stores and opening hours listed? Does NOT
measure product quality or selection.

Write EXACTLY ONE file: pipeline/extracts/kukkakauppojen-verkkokaupat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",             // Tuotehinnat verkossa esillä
 "toimitus_kerrottu": "kylla|osittain|ei",         // Toimitustavat ja -kulut kerrottu ennen kassaa
 "palautusehdot_saatavilla": "kylla|osittain|ei",  // Palautus- ja takuuehdot julkisesti saatavilla
 "myymalat_ja_aukioloajat": "kylla|osittain|ei",   // Myymälät ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",           // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",         // Riippumaton arviolähde esillä
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
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
