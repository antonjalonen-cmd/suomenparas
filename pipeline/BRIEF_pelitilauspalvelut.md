# Extraction task — vertical `pelitilauspalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- These sites often render prices with JavaScript: if you see a placeholder or a short shell,
  retry with `--js`. Fetch `--raw`, grep hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Gaming subscription services sold to Finnish consumers.
Measures the PUBLIC site: monthly prices per tier visible, tier differences (game library,
devices, extra perks) explained, cancellation/free trial terms stated, owner company
disclosed, game library browsable before subscribing? It does NOT measure library size,
game quality, latency, or hardware. Never score inside a logged-in area.

SPECIAL NOTES:
- Xbox Game Pass: main page xbox.com/fi-fi/xbox-game-pass — fetch this specifically.
  Tiers to look for: Game Pass Standard, Game Pass Ultimate (2026 naming); note if PC/console
  split is explained. EA Play is included in Ultimate.
- PlayStation Plus: store.playstation.com/fi-fi is the Finnish store. Main subscription
  info at www.playstation.com/fi-fi/ps-plus/ — fetch that URL. Three tiers: Essential,
  Extra, Premium.
- Nintendo Switch Online: nintendo.fi is the Finnish-language site. Subscription info at
  nintendo.fi/nintendo-switch-perhe/nintendo-switch-online — fetch that URL.
  Tiers: Individual / Family and with/without Expansion Pack.
- EA Play: ea.com/fi-fi/ea-play — fetch this URL. Note EA Play vs EA Play Pro.
- Ubisoft+: ubisoft.com/fi-fi/ubisoftplus — fetch this URL (or follow nav links).
  Tiers: Ubisoft+ Classic, Ubisoft+ Premium.
- Apple Arcade: apple.com/fi/apple-arcade/ — fetch this URL. One tier, one price.

Write EXACTLY ONE file: pipeline/extracts/pelitilauspalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",          // Kuukausihinta per taso julkisesti esillä
 "tasojen_erot_kerrottu": "kylla|osittain|ei",  // Tilaustasojen erot (pelikirjasto, laitteet, hinta) selitetty
 "pelikirjasto_kuvaus": "kylla|osittain|ei",    // Pelikirjaston kuvaus tai lista ennen tilaamista
 "irtisanominen_kerrottu": "kylla|osittain|ei", // Irtisanominen ja ilmaiskokeilun ehdot kerrottu
 "omistaja_kerrottu": "kylla|osittain|ei",      // Omistava yhtiö kerrottu sivustolla
 "riippumaton_arvio": "kylla|osittain|ei",      // Riippumaton arviolähde esillä
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
