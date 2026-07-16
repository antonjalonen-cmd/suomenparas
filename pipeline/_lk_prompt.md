Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule in it.

Analyse the public website **{DOMAIN}** (brand: {BRAND}, Finnish consumer home broadband provider / laajakaista). Use WebFetch on {DOMAIN} and its relevant subpages (laajakaista, kotinetti, hinnasto, saatavuus, sopimusehdot, asiakaspalvelu, yhteystiedot). Judge only what a visitor can actually see without logging in. Focus on HOME BROADBAND (fixed fibre/cable or 5G kotinetti) — not mobile phone plans.

Write your result to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\laajakaista__{SLUG}.json

Exact JSON shape (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "kk_hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",
 "kampanjan_jalkeinen_hinta": "kylla|osittain|ei",
 "sopimusaika_ja_avausmaksu": "kylla|osittain|ei",
 "saatavuustarkistus_ilman_yhteystietoja": "kylla|osittain|ei",
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
 "tekniikat": ["kuitu","kaapeli","5g", ...],
 "halvin_kk_hinta_eur": <number or null>,
 "nopein_mbps": <int or null>,
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"kk_hinta_esilla_ilman_yhteystietoja": "<verbatim quote>", "kampanjan_jalkeinen_hinta": "<verbatim quote>", "sopimusaika_ja_avausmaksu": "<verbatim quote>"}
}

Field meanings:
- kk_hinta_esilla_ilman_yhteystietoja: is a real monthly price in euros shown to an anonymous visitor WITHOUT giving name/email/phone? "kylla" only if a number is visible. "osittain" if it requires entering an address/postcode first (common for fibre) but no personal contact details.
- kampanjan_jalkeinen_hinta: THIS IS THE KEY DARK-PATTERN CHECK. Many ISPs advertise "0 €/kk ensimmäiset 6 kk" or "19,90 €/kk 12 kk ajan". Is the price AFTER the campaign period clearly stated next to the offer? "kylla" = normal price clearly shown. "osittain" = only in fine print / a separate terms page / must be calculated. "ei" = not stated at all. If the provider runs NO campaign pricing and simply lists one normal price, that counts as "kylla".
- sopimusaika_ja_avausmaksu: are contract length (määräaikainen 12/24kk vs toistaiseksi) AND the opening/activation fee (avausmaksu/toimitusmaksu) both publicly stated? Both -> "kylla", one -> "osittain".
- saatavuustarkistus_ilman_yhteystietoja: can you check whether the connection is available at an address WITHOUT giving contact details? Address/postcode alone is fine -> "kylla". Requires name/email/phone -> "ei".
- riippumaton_arvio: does the site show an INDEPENDENT rating source (EPSI Rating, Trustpilot, etc.)? Self-reported figures or own award claims with no external source = "ei".
- halvin_kk_hinta_eur / nopein_mbps: cheapest publicly listed home-broadband monthly price and highest advertised speed. null if not visible. Do NOT guess.

Create the extracts directory if needed. After writing the file, reply with ONLY: "{SLUG} OK" plus one sentence on anything unusual. Do not paste the JSON back.
