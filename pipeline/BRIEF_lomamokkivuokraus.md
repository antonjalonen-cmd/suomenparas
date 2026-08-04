# Extraction task — vertical `lomamokkivuokraus`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish holiday cottage rental platforms (lomamökkivuokraus), from the CONSUMER's
perspective on the public site: can you see the price per night or week in search results without registering?
Are cancellation policies stated clearly? Can you book and pay fully online? How many Finnish cottages/properties
does the platform have?

Write EXACTLY ONE file: pipeline/extracts/lomamokkivuokraus__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "hinnat_esilla": "kylla|osittain|ei",            // Vuorokausi- tai viikkohinta nähtävissä hakutuloksissa ilman rekisteröitymistä
 "peruutusehdot_kerrottu": "kylla|osittain|ei",   // Peruutus- tai varausehdot kerrottu selkeästi
 "varaus_verkossa": "kylla|osittain|ei",           // Mökin voi varata ja maksaa kokonaan verkossa
 "kohteiden_maara_fi": "kylla|osittain|ei",        // Suomessa olevien mökkien tai loma-asuntojen lukumäärä kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",           // Y-tunnus tai omistava yhtiö esillä sivustolla
 "asiakaspalvelu_suomeksi": "kylla|osittain|ei",   // Suomenkielinen asiakaspalvelu saatavilla
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
