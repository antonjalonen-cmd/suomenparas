Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule in it.

Analyse the public website **{DOMAIN}** (brand: {BRAND}, Finnish consumer electricity retailer / sähkön myyjä). Use WebFetch on {DOMAIN} and its relevant subpages (sähkösopimukset, hinnasto, sopimusehdot, asiakaspalvelu, yhteystiedot). Judge only what a visitor can actually see without logging in.

Write your result to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\sahkosopimukset__{SLUG}.json

Exact JSON shape (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",
 "perusmaksu_esilla": "kylla|osittain|ei",
 "sopimusehdot_selkeasti": "kylla|osittain|ei",
 "alkupera_kerrottu": "kylla|osittain|ei",
 "y_tunnus_esilla": "kylla|ei",
 "y_tunnus": "<string or null>",
 "riippumaton_arvio": "kylla|osittain|ei",
 "asiakasarvio": {"arvosana": <number or null>, "maara": <int or null>, "lahde": "<string or null>"},
 "puhelin_esilla": "kylla|ei",
 "puhelin": "<string or null>",
 "email_esilla": "kylla|ei",
 "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei",
 "ukk_osio": "kylla|ei",
 "mobiilisovellus": "kylla|ei",
 "sopimustyypit": ["porssisahko","kiintea","maaraaikainen", ...],
 "hinta_snt_kwh": <number or null>,
 "perusmaksu_eur_kk": <number or null>,
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"hinta_esilla_ilman_yhteystietoja": "<verbatim quote>", "perusmaksu_esilla": "<verbatim quote>", "alkupera_kerrottu": "<verbatim quote>"}
}

Field meanings:
- hinta_esilla_ilman_yhteystietoja: is an actual price in snt/kWh (or the pörssisähkö margin) shown to an anonymous visitor WITHOUT giving name/email/phone? "kylla" only if a real number is visible. "osittain" if it needs only a postcode, or if only a marginal/vague figure is shown. If you must start a signup flow or give contact details -> "ei".
- perusmaksu_esilla: is the fixed monthly fee (perusmaksu, €/kk) publicly stated?
- sopimusehdot_selkeasti: are contract length (määräaikainen/toistaiseksi) and notice/termination terms clearly stated publicly?
- alkupera_kerrottu: is the electricity's origin stated (uusiutuva, alkuperätakuu, ydinvoima, fossiiliton)?
- riippumaton_arvio: does the site show an INDEPENDENT rating source (EPSI Rating, Trustpilot, etc.)? Self-reported satisfaction with no external source = "ei".
- hinta_snt_kwh / perusmaksu_eur_kk: record the cheapest/most prominent publicly listed figure, or null if none is visible. Do NOT guess.

Create the extracts directory if needed. After writing the file, reply with ONLY: "{SLUG} OK" plus one sentence on anything unusual. Do not paste the JSON back.
