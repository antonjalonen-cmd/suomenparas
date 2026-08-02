# Extraction task — vertical `pakettipalvelut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish parcel/courier services available to consumers (private individuals). Measures the PUBLIC site: are domestic package prices visible, are delivery times stated, is pickup point network described, and is the claims process for lost/damaged parcels explained?
It does NOT measure actual delivery speed or service quality. Never score anything from inside a logged-in area.

COMPANY-SPECIFIC NOTES:
- posti: use posti.fi — try /fi/henkiloasiakkaat/paketit/ or similar for parcel pricing; site uses Gatsby (may need --js)
- matkahuolto: use matkahuolto.fi — look for "Lähetä paketti" or hinnasto sections
- postnord: use postnord.fi — look for consumer parcel sending and pricing
- dhl: use dhl.com/fi-fi/ — look for "Yksityishenkilöt" or "Lahetä paketti" sections on the Finnish language version
- gls: use gls-group.com/FI/fi/ — Finnish language section; look for Lahetykset or consumer section
- dsv: use dsv.com/fi-fi/ — look for Kuluttajat section; this is B2B-heavy so consumer pricing may be absent

Write EXACTLY ONE file: pipeline/extracts/pakettipalvelut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnasto_kuluttajalle": "kylla|osittain|ei",    // Kotimaanpakettihinnat kuluttajalle julkisesti esillä (ennen rekisteröintiä)
 "toimitusaika_kerrottu": "kylla|osittain|ei",    // Toimitusaika per palveluluokka (esim. 1–3 vrk) kerrottu julkisesti
 "noutopisteet_tiedot": "kylla|osittain|ei",       // Noutopisteiden määrä tai kartta saatavilla julkisesta sivusta
 "reklamaatiomenettely": "kylla|osittain|ei",      // Korvaus- ja reklamaatiomenettely kadonneelle/vahingoittuneelle paketille kuvattu
 "y_tunnus_esilla": "kylla|osittain|ei",           // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",         // Riippumaton arviolähde esillä (esim. palkinto tai julkinen arvio)
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
