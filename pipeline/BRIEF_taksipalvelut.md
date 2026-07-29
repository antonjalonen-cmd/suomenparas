# Extraction task — vertical `taksipalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: taxi services in Finland, from the RIDER's perspective on
the public site: are prices or price examples public (starting fee, per-km, price
calculator, or app fare estimate described), are ordering channels described (app,
phone, street), are cancellation/waiting/extra fees stated, is the service area clear?

Write EXACTLY ONE file: pipeline/extracts/taksipalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "hinnat_esilla": "kylla|osittain|ei",            // Hinnat tai hintaesimerkit julkisesti esillä
 "tilaustavat_kuvattu": "kylla|osittain|ei",      // Tilaustavat (sovellus, puhelin, katu) kuvattu
 "peruutus_ja_lisamaksut": "kylla|osittain|ei",   // Peruutus-, odotus- ja lisämaksukäytännöt kerrottu
 "toiminta_alue_kerrottu": "kylla|osittain|ei",   // Toiminta-alue kerrottu
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
