# Extraction task — vertical `musiikkipalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- These sites often render prices with JavaScript (placeholders in plain fetch): if you see
  a placeholder or a ~74-char shell, retry with `--js`. On SPA sites fetch `--raw`, grep
  hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Music streaming subscription services sold to Finnish consumers.
Measures the PUBLIC site: monthly prices visible, tier differences (audio quality, device
limits, offline playback, ad-supported vs paid) explained, cancellation/free trial terms
stated, owner company disclosed, Finnish-language site with euro pricing available?
It does NOT measure music library size, sound quality, or app features. Never score inside a
logged-in area.

SPECIAL NOTES:
- Spotify: pricing is at spotify.com/fi/premium/ (fetch this URL specifically)
- Apple Music: web player is music.apple.com (web app, login required) — the subscription
  and pricing page is at apple.com/fi/apple-music/ — fetch THAT URL for pricing data.
- YouTube Music: pricing at music.youtube.com/premium or youtube.com/premium — fetch both.
- Deezer: Finnish locale at deezer.com/fi/ — check the subscription/offers page.
- Qobuz: Finnish locale at qobuz.com/fi-en/ — fetch pricing/plans pages.
- Amazon Music: music.amazon.com is a login-gated web player. Pricing info for Finnish
  users exists on amazon.de/music/unlimited (German UI). If no Finnish-language pricing
  found, mark suomenkielinen_palvelu as "ei" and hinnat_esilla as "osittain" if at least
  the general amazon.com/music/unlimited page shows prices.

Write EXACTLY ONE file: pipeline/extracts/musiikkipalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",          // Kuukausihinnat julkisesti esillä
 "tasojen_erot_kerrottu": "kylla|osittain|ei",  // Tilaustasojen erot (laatu, laitteet, offline) kerrottu
 "irtisanominen_kerrottu": "kylla|osittain|ei", // Irtisanominen ja ilmaiskokeilun ehdot kerrottu
 "omistaja_kerrottu": "kylla|osittain|ei",      // Omistava yhtiö kerrottu sivustolla
 "suomenkielinen_palvelu": "kylla|osittain|ei", // Suomenkielinen sivusto ja hinnat euroissa
 "riippumaton_arvio": "kylla|osittain|ei",      // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "perustaso_kk_hinta_eur": <number|null>,   // advertised monthly EUR price of cheapest paid tier. null if not stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
