# Extraction task — vertical `pikaruokaketjut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs,
  no Wolt/Foodora listings, no news articles.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. A cookie wall or bot block is a
  measurement gap ("ei mitattavissa"), NOT a "no".
- NEVER describe another company's site in this company's file.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: fast food chains operating in Finland. Measured from the
CUSTOMER's perspective on the public site: are product prices visible online, are allergen
and nutrition details available per product, is the ORIGIN of the meat and other main
ingredients stated, are restaurants and their opening hours listed?
Does NOT measure taste, food quality or restaurant cleanliness.

Notes for this vertical:
- `hinnat_esilla`: prices shown in the chain's own online ordering flow or menu count.
  If prices appear only after choosing a restaurant, that is still "kylla" as long as no
  login is required. If the site shows no prices anywhere without an app, that is "ei".
- `allergeenit_esilla`: "kylla" requires per-product allergen or nutrition data on the
  public site (an interactive table, a product page, or a downloadable list). A general
  sentence "kysy henkilökunnalta" alone is "ei".
- `alkupera_kerrottu`: origin of meat or main raw materials (esim. "naudanliha Suomesta").
  A vague "käytämme laadukkaita raaka-aineita" is "ei".
- Many of these chains are heavily JS-driven — use `--js` and follow real nav links.

Write EXACTLY ONE file: pipeline/extracts/pikaruokaketjut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",               // Tuotteiden hinnat verkossa esillä
 "allergeenit_esilla": "kylla|osittain|ei",          // Allergeeni- ja ravintosisältötiedot tuotekohtaisesti
 "alkupera_kerrottu": "kylla|osittain|ei",           // Raaka-aineiden alkuperä kerrottu
 "ravintolat_ja_aukioloajat": "kylla|osittain|ei",   // Ravintolat ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",             // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",           // Riippumaton arviolähde esillä
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
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
