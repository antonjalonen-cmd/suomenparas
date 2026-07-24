# Extraction task — vertical `tapahtumaliput`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish and Finland-operating online event ticket sales platforms.
Measures the PUBLIC site: are service/booking fees visible before you commit to a purchase,
can you see the total cost (ticket + fees) without completing checkout, what is the refund/
exchange policy, and can you buy without registering? Does NOT measure event selection, queue
times, or customer service quality — only what a visitor can read on the public website.

SPECIAL NOTE for lippu.fi: Akamai CDN blocks automated fetches entirely (HTTP timeout).
If fetch_page.py returns 0 chars or HTTP 000, mark all fields as "osittain" (measurement
gap, not an absence) and set fetched_ok to []. Note the blocker in the evidence field.

Write EXACTLY ONE file: pipeline/extracts/tapahtumaliput__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "palvelumaksut_esilla": "kylla|osittain|ei",    // Palvelumaksut (lisät) esillä ennen maksuprosessia
 "kokonaishinta_ilman_ostoa": "kylla|osittain|ei",    // Kokonaishinnan (lippu + maksut) saa tietää ilman ostoprosessia
 "peruutusehdot_esilla": "kylla|osittain|ei",    // Peruutus- ja vaihtoehtokäytäntö julkisesti esillä
 "ostaa_ilman_rekisteroitymista": "kylla|osittain|ei",    // Liput voi tilata ilman rekisteröitymistä
 "y_tunnus_esilla": "kylla|osittain|ei",    // Y-tunnus esillä (tai omistava yhtiö selkeästi kerrottu)
 "riippumaton_arvio": "kylla|osittain|ei",    // Riippumaton arviolähde esillä
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "palvelumaksu_eur_per_lippu": <number|null>,   // stated service/booking fee per ticket in EUR. null if not publicly stated.
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
