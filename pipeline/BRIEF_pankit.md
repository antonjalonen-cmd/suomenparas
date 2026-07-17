# Extraction task — vertical `pankit` (Finnish retail banks)

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the bank's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent.
- A BOT-BLOCKED OR COOKIE-WALLED PAGE MUST NOT BE SCORED AS AN OPAQUE PAGE. Finnish bank sites
  are heavily protected and several force a cookie wall before showing anything. If you are
  challenged or a page comes back suspiciously empty, SAY SO and use "osittain" — never "ei".
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: the transparency of the PUBLIC, LOGGED-OUT site — can a person who
is not yet a customer find the price list, the terms, and a way to make contact? It does NOT
measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/pankit__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "palveluhinnasto_julkinen": "kylla|osittain|ei",   // full palveluhinnasto reachable WITHOUT logging in (a public PDF counts as "kylla")
 "tilin_ja_kortin_maksut_esilla": "kylla|osittain|ei", // the actual €/kk or €/v for a käyttötili and a debit card, publicly stated
 "sopimusehdot_saatavilla": "kylla|osittain|ei",    // yleiset sopimusehdot publicly downloadable
 "konttorit_ja_aukioloajat": "kylla|osittain|ei",   // branch list AND opening hours public
 "y_tunnus_esilla": "kylla|osittain|ei",
 "riippumaton_arvio": "kylla|osittain|ei",
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "kayttotili_kk_maksu_eur": <number|null>,   // monthly fee of the basic personal current account (käyttötili/päivittäispalvelut). 0 is a valid answer if they state it is free. null if you did not see it.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
