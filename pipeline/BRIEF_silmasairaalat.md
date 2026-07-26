# Extraction task — vertical `silmasairaalat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish private eye surgery clinics and healthcare chains
offering ophthalmological surgery. Measures the PUBLIC site: are laser/cataract surgery
prices visible before you have to call or give contact details, are surgery methods
explained, can you book online?
NOTE: For large health companies (Terveystalo, Mehiläinen, Pihlajalinna) measure the
EYE SURGERY content specifically — navigate to their silmäkirurgia/silmäleikkaukset section.
Mehiläinen uses bot-protection on curl — use fetch_page.py --js for all pages.
It does NOT measure care quality or surgeon skill. Never score anything from inside a
logged-in area.

Write EXACTLY ONE file: pipeline/extracts/silmasairaalat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",    // Leikkauksen hintatieto julkisesti esillä ilman yhteystietoja
 "menetelmat_kuvattu": "kylla|osittain|ei",    // Leikkausmenetelmät kuvattu (LASIK, PRK, SMILE, kaihileikkaus)
 "varaus_verkossa": "kylla|osittain|ei",    // Ajanvaraus tai arviokäynti tilattavissa verkossa
 "takuu_tai_jalkitarkastus": "kylla|osittain|ei",    // Takuu tai jälkitarkastukset kuvattu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "laserleikkaus_hinta_alkaen_eur": <number|null>,   // cheapest advertised laser eye surgery price (one eye or both) in EUR. null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
