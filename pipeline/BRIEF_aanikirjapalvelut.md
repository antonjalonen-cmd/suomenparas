# Extraction task — vertical `aanikirjapalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- These sites often render prices with JavaScript: if you see a placeholder or a short shell,
  retry with `--js`. Fetch `--raw`, grep hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Audiobook streaming subscription services available to Finnish
consumers. Measures the PUBLIC site: monthly price visible, free trial and cancellation
terms stated, catalog size (titles or Finnish titles count) stated, tier differences
explained (if multiple tiers exist), parent company/owner disclosed, and whether listening
time limits or download limits are clearly stated. Does NOT measure audio quality, catalog
depth, or app features. Never score inside a logged-in area.

SPECIAL NOTES:
- Storytel: fetch storytel.com/fi and storytel.com/fi/hinnasto (pricing page).
  Storytel has multiple tiers (e.g. Standard, Maxi); note differences if explained.
  Look for Finnish book catalog size if stated.
- BookBeat: fetch bookbeat.com/fi and bookbeat.com/fi/subscription.
  Look for pricing, free trial (typically 30 days), and how many titles are in the catalog.
- Nextory: fetch nextory.com/fi and follow navigation to pricing/subscription pages.
  Look for tier differences and catalog size.
- Kobo: fetch kobo.com/fi/fi and navigate to "Kobo Plus" subscription info.
  Kobo Plus has two tiers: "Kobo Plus Read" (e-books) and "Kobo Plus Listen" (audiobooks).
  Measure the "Kobo Plus Listen" tier specifically. Note whether both tiers are explained.
- Podimo: fetch podimo.com/fi and look for pricing, trial, and audiobook vs podcast
  distinction. Podimo offers both podcasts and audiobooks.
- Spotify: fetch spotify.com/fi/audiobooks/ specifically (this is the audiobooks landing
  page). Also fetch spotify.com/fi/premium/ for pricing context.
  Key thing to measure: is the 15 h/month audiobook listening limit clearly stated on the
  public site? Spotify Premium includes audiobooks up to 15 hours per month; beyond that
  users purchase individually. If this limit is NOT clearly stated, score kuunteluaika_rajoitukset "ei".

Write EXACTLY ONE file: pipeline/extracts/aanikirjapalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",              // Kuukausihinta julkisesti esillä
 "kokeilujakso_kerrottu": "kylla|osittain|ei",      // Ilmaiskokeilun ja irtisanomisen ehdot kerrottu
 "kirjastokoko_kerrottu": "kylla|osittain|ei",      // Kirjaston koko tai suomenkielisten kirjojen määrä kerrottu
 "tasojen_erot_kerrottu": "kylla|osittain|ei",      // Tilaustasojen erot kerrottu (jos tasoja on useita)
 "omistaja_kerrottu": "kylla|osittain|ei",          // Omistava yhtiö kerrottu sivustolla
 "kuunteluaika_rajoitukset": "kylla|osittain|ei",   // Kuunteluajan tai latauksien rajoitukset kerrottu
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "perustaso_kk_hinta_eur": <number|null>,   // cheapest paid monthly EUR price. null if not stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
