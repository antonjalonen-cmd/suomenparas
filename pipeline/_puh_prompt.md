Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule.

Analyse **{DOMAIN}** (brand: {BRAND}) — Finnish CONSUMER MOBILE SUBSCRIPTIONS (puhelinliittymät). Judge only the mobile liittymä offering, not home broadband. WebFetch the site + subpages (liittymät, hinnasto, sopimusehdot, asiakaspalvelu, yhteystiedot). Only what a visitor sees WITHOUT logging in.

Work efficiently: ~8 pages max, then WRITE THE FILE. The written file is the only deliverable.
Write to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\puhelinliittymat__{SLUG}.json

Exact JSON (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "fetched_ok": ["<urls you actually loaded successfully>"],
 "kk_hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",
 "kampanjan_jalkeinen_hinta": "kylla|osittain|ei",
 "sopimusaika_ja_irtisanomisaika": "kylla|osittain|ei",
 "nopeus_ja_datarajat": "kylla|osittain|ei",
 "y_tunnus_esilla": "kylla|ei",
 "y_tunnus": "<string or null>",
 "riippumaton_arvio": "kylla|osittain|ei",
 "asiakasarvio": {"arvosana": <number or null>, "maara": <int or null>, "lahde": "<string or null>"},
 "puhelin_esilla": "kylla|ei", "puhelin": "<string or null>",
 "email_esilla": "kylla|ei", "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei", "ukk_osio": "kylla|ei", "mobiilisovellus": "kylla|ei",
 "halvin_kk_hinta_eur": <number or null>,
 "nopein_mbps": <int or null>,
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"kk_hinta_esilla_ilman_yhteystietoja": "<observation>", "kampanjan_jalkeinen_hinta": "<observation>", "sopimusaika_ja_irtisanomisaika": "<observation>"}
}

Meanings:
- kk_hinta_esilla_ilman_yhteystietoja: real €/kk visible to an anonymous visitor, no name/email/phone? "kylla" only if a number is visible.
- kampanjan_jalkeinen_hinta: KEY DARK-PATTERN CHECK. Operators advertise "0 €/kk 6 kk". Is the price AFTER the campaign stated next to the offer? "kylla" = clearly shown (or no campaign, just one normal price). "osittain" = only in fine print/separate terms page. "ei" = not stated.
- sopimusaika_ja_irtisanomisaika: contract length (määräaikainen/toistaiseksi) AND notice period both public -> kylla; one -> osittain.
- nopeus_ja_datarajat: is the speed cap (e.g. 100M/300M) and any data limit / throttling stated clearly?
- riippumaton_arvio: INDEPENDENT source (EPSI Rating, Trustpilot). Own awards/self-reported = "ei".
- halvin_kk_hinta_eur / nopein_mbps: cheapest publicly listed mobile plan and top advertised speed. null if not visible. Do NOT guess.

CRITICAL: `fetched_ok` must list only URLs that actually returned real content. If a page 404s or is blocked by a cookie wall, you did NOT see it — you may not claim an absence based on a page you could not load. When unsure, use "osittain", not "ei".

After writing, verify the file exists, then reply ONLY: "{SLUG} OK" + one sentence on anything unusual.
