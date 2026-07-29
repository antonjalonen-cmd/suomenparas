# Extraction task — vertical `hotelliketjut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: hotel chains operating in Finland, from the GUEST's
perspective on the public site: are room prices visible without logging in (search a
sample date if the site offers a date picker in plain HTML — otherwise judge from
visible price examples), are cancellation terms stated before booking, are breakfast
and extras priced openly, are the hotels/locations/contacts listed?

Write EXACTLY ONE file: pipeline/extracts/hotelliketjut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "hinnat_esilla": "kylla|osittain|ei",            // Huonehinnat nähtävissä ilman kirjautumista
 "peruutusehdot_esilla": "kylla|osittain|ei",     // Peruutusehdot kerrottu ennen varausta
 "lisapalvelut_hinnoiteltu": "kylla|osittain|ei", // Aamiaisen ja lisäpalvelujen hinnat kerrottu
 "hotellit_ja_sijainnit": "kylla|osittain|ei",    // Hotellit, sijainnit ja yhteystiedot kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",
 "riippumaton_arvio": "kylla|osittain|ei",
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
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
