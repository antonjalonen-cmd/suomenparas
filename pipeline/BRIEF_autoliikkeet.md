# Extraction task — vertical `autoliikkeet`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs,
  no Nettiauto listings, no news articles.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. A cookie wall or bot block is a
  measurement gap ("ei mitattavissa"), NOT a "no".
- NEVER describe another company's site in this company's file.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish car dealer chains that sell used cars (vaihtoautot)
to consumers. Measured from the BUYER's perspective on the public site, BEFORE any contact
form is filled: are car prices visible, is the used-car warranty (vaihtoautotakuu) content
and duration stated, are financing costs (todellinen vuosikorko, kokonaiskulut) published,
is a return or exchange right stated, are dealerships and opening hours listed?
Does NOT measure car quality, price level or sales service.

Notes for this vertical:
- The car listing search itself usually shows prices — that counts for `hinnat_esilla` only
  if you actually loaded a listing page and saw prices without logging in.
- `rahoituskulut_kerrottu`: a monthly instalment alone is NOT enough. "kylla" requires the
  todellinen vuosikorko (effective annual rate) or a full cost example on a public page.
  A representative example in small print counts as "osittain" if incomplete.
- `palautusehdot_saatavilla`: a stated return right, exchange right or trial period
  (esim. "14 vuorokauden vaihto-oikeus"). Warranty alone is NOT a return right.

Write EXACTLY ONE file: pipeline/extracts/autoliikkeet__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",              // Autojen hinnat verkossa esillä
 "takuu_kerrottu": "kylla|osittain|ei",             // Vaihtoautotakuun sisältö ja kesto kerrottu
 "rahoituskulut_kerrottu": "kylla|osittain|ei",     // Rahoituksen todellinen vuosikorko ja kulut esillä
 "palautusehdot_saatavilla": "kylla|osittain|ei",   // Palautus- tai vaihto-oikeus kerrottu
 "toimipisteet_ja_aukioloajat": "kylla|osittain|ei",// Toimipisteet ja aukioloajat kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",            // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",          // Riippumaton arviolähde esillä
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
Provide `evidence` for at least the seven transparency fields.
