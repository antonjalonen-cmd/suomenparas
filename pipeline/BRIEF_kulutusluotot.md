# Extraction task — vertical `kulutusluotot` (Finnish consumer credit lenders)

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent.
- A BOT-BLOCKED OR COOKIE-WALLED PAGE MUST NOT BE SCORED AS AN OPAQUE PAGE. If a page looks
  suspiciously empty or you are challenged, say so and use "osittain" — never "ei".
- NEVER claim an absence from a page you could not load. Absence claims are the unstable ones.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

Write EXACTLY ONE file: pipeline/extracts/kulutusluotot__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "todellinen_vuosikorko_esilla": "kylla|osittain|ei",   // effective APR (todellinen vuosikorko) visible publicly WITHOUT submitting an application
 "esimerkkilaskelma_esilla": "kylla|osittain|ei",       // the statutory representative example (KSL 7:9): "esim. 5000 € 3 v, tod. vuosikorko X %, takaisin yhteensä Y €"
 "kulut_eriteltyna": "kylla|osittain|ei",               // account/handling/withdrawal/late fees itemised
 "luotonantaja_ja_valvoja_kerrottu": "kylla|osittain|ei", // does the site say WHICH legal entity lends and WHO supervises it (e.g. "Saldo Bank UAB, valvoja Liettuan keskuspankki")
 "y_tunnus_esilla": "kylla|osittain|ei",
 "riippumaton_arvio": "kylla|osittain|ei",              // an independent rating source shown (Trustpilot etc.)
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "todellinen_vuosikorko_pct": <number|null>,            // the APR from THEIR OWN representative example. If a range, the LOWEST. Only if you literally saw it.
 "luottosumma_max_eur": <number|null>,                  // largest advertised credit amount
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],        // exactly 3, short Finnish, specific to THIS site
 "kehityskohteet": ["", "", ""],   // exactly 3
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees. Prefer verbatim page text where it exists." }
}
Provide `evidence` for at least the six transparency fields.
