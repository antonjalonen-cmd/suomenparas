# Extraction task — vertical `muotikaupat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- BOT-BLOCKED SITES: Zalando (zalando.fi) and H&M (hm.com/fi_fi/) are protected by
  bot-blocking (Zalando: custom, H&M: Akamai). If pages return 403 or <300 chars:
  use "osittain" for criteria you cannot positively confirm — NEVER "ei" for blocked content.
  Document the blocking clearly in evidence.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Online fashion retailers selling adult clothing in Finland.
Measured from the BUYER's perspective: can you browse prices without logging in, is delivery
cost shown before checkout, are return terms clearly accessible, is a size guide available?

COMPANY DETAILS:
- zalando: zalando.fi — Zalando Finland Oy (Y-tunnus 2697196-4). Bot-blocked: return 403.
  Use "osittain" for blocked criteria. Document blocking in evidence.
- hm: hm.com/fi_fi/ — H & M Hennes & Mauritz Oy (Y-tunnus 1080854-8). Akamai-estetty.
  Use "osittain" for blocked criteria. Document blocking in evidence.
- boozt: boozt.com/fi/fi — Swedish Boozt AB, no Finnish Y-tunnus. Accessible.
- kappahl: kappahl.com/fi-fi/ — KappAhl Oy (Y-tunnus 0758506-4). Accessible.
- cubus: cubus.com/fi/ — Cubus Finland Oy Ab (Y-tunnus 2379502-9), Varner-konserni.
  Accessible.
- ellos: ellos.fi — Ellos Finland Oy (Y-tunnus 1442131-6). Accessible.

Write EXACTLY ONE file: pipeline/extracts/muotikaupat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnat_esilla": "kylla|osittain|ei",           // Tuotehinnat esillä ilman kirjautumista
 "toimitus_kerrottu": "kylla|osittain|ei",        // Toimitustavat ja -kulut kerrottu ennen kassaa
 "palautusehdot_saatavilla": "kylla|osittain|ei", // Palautusehdot julkisesti saatavilla
 "koko_opas": "kylla|osittain|ei",               // Koko-opas tai sovitusohje saatavilla
 "y_tunnus_esilla": "kylla|osittain|ei",          // Y-tunnus tai omistava yhtiö esillä
 "riippumaton_arvio": "kylla|osittain|ei",         // Riippumaton arviolähde esillä
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
