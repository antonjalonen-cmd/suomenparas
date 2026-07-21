# Extraction task — vertical `autokoulut`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely
  absent — and ONLY from a page you actually loaded.
- Suspiciously empty page: retry with `--js`; on SPA sites fetch the front page `--raw`,
  grep hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load. Never guess a number.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish national driving school chains. Measures the PUBLIC site: are course prices stated, does online enrollment work, is course content (driving lessons, theory, installments) described?
It does NOT measure service quality. Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/autokoulut__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "kurssihinnat_esilla": "kylla|osittain|ei",    // Kurssien hinnat julkisesti esillä
 "ilmoittautuminen_verkossa": "kylla|osittain|ei",    // Ilmoittautuminen onnistuu verkossa
 "kurssisisalto_kuvattu": "kylla|osittain|ei",    // Kurssin sisältö (ajotunnit, teoria, maksuerät) kuvattu
 "toimipisteet_ja_yhteystiedot": "kylla|osittain|ei",    // Toimipisteet ja yhteystiedot kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "b_kortti_hinta_eur": <number|null>,   // advertised total price of a B-license course (peruspaketti). null if not stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields.
