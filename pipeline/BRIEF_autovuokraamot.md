# Extraction task — vertical `autovuokraamot`

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

WHAT THIS CATEGORY MEASURES: Finnish car rental companies. Measures the PUBLIC site: can a renter see the total price, deductible/insurance options and rental terms before giving contact details?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/autovuokraamot__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinta_ilman_yhteystietoja": "kylla|osittain|ei",    // Vuokrahinnan näkee ilman yhteystietoja
 "omavastuu_ja_vakuutus": "kylla|osittain|ei",    // Omavastuu ja vakuutusvaihtoehdot kerrottu
 "vuokrausehdot_saatavilla": "kylla|osittain|ei",    // Vuokrausehdot (km-rajat, polttoaine, ikärajat) julkisesti
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",    // Toimipisteet ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "pienin_vuorokausihinta_eur": <number|null>,   // cheapest advertised daily rate for the smallest car class, if publicly stated. null otherwise.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
