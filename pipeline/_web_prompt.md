Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule.

Analyse **{DOMAIN}** (brand: {BRAND}) — WEB HOSTING (webhotelli) for Finnish consumers and small businesses. {NOTE}
Judge the shared-hosting/webhotelli pages (webhotelli, hinnasto, palvelut, sopimusehdot, yhteystiedot). Only what a visitor sees WITHOUT logging in.

Work efficiently: ~8 pages max, then WRITE THE FILE. The written file is the only deliverable.
Write to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\webhotellit__{SLUG}.json

Exact JSON (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "fetched_ok": ["<urls you actually loaded successfully>"],
 "hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",
 "uusimishinta_kerrottu": "kylla|osittain|ei",
 "resurssirajat_selkeasti": "kylla|osittain|ei",
 "sopimusehdot_ja_irtisanominen": "kylla|osittain|ei",
 "y_tunnus_esilla": "kylla|ei",
 "y_tunnus": "<string or null>",
 "riippumaton_arvio": "kylla|osittain|ei",
 "asiakasarvio": {"arvosana": <number or null>, "maara": <int or null>, "lahde": "<string or null>"},
 "puhelin_esilla": "kylla|ei", "puhelin": "<string or null>",
 "email_esilla": "kylla|ei", "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei", "ukk_osio": "kylla|ei", "mobiilisovellus": "kylla|ei",
 "halvin_kk_hinta_eur": <number or null>,
 "palvelimet_suomessa": "kylla|ei|ei kerrottu",
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"hinta_esilla_ilman_yhteystietoja": "<observation>", "uusimishinta_kerrottu": "<observation>", "resurssirajat_selkeasti": "<observation>"}
}

Meanings:
- hinta_esilla_ilman_yhteystietoja: is a real monthly or yearly price visible to an anonymous visitor? Hosting companies normally publish prices, so "ei" here would be unusual — check carefully before recording it.
- uusimishinta_kerrottu: KEY DARK-PATTERN CHECK. Hosts advertise a cheap FIRST term (e.g. "1,99 e/kk ensimmäinen vuosi") and then renew far higher. Is the RENEWAL / normal price stated next to the offer? "kylla" = clearly shown, or there is no intro discount and one price applies throughout. "osittain" = only in fine print or a separate terms page. "ei" = not stated at all.
- resurssirajat_selkeasti: are disk space, traffic/bandwidth, number of sites/databases and email accounts stated clearly?
- sopimusehdot_ja_irtisanominen: are contract terms and how to cancel publicly available?
- palvelimet_suomessa: does it state the servers are in Finland? A real selling point in this market — but only "kylla" if actually stated on the site.
- riippumaton_arvio: INDEPENDENT source (Trustpilot etc.). Self-reported = "ei".
- halvin_kk_hinta_eur: cheapest publicly listed webhotelli monthly price. If only an annual price is shown, convert it and say so in evidence. null if not visible. Do NOT guess.

CRITICAL: `fetched_ok` must list only URLs that actually returned real content. If a page 404s or is blocked, you did NOT see it — you may not claim an absence based on a page you could not load. When unsure, use "osittain", not "ei".

After writing, verify the file exists, then reply ONLY: "{SLUG} OK" plus one sentence on anything unusual.
