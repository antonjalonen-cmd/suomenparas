# Extraction task — vertical `aikakauslehdet`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the outlet's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: individual Finnish magazines (aikakauslehdet), NOT their
publishers. Measured from the SUBSCRIBER's perspective on the public site: are
subscription prices (kestotilaus AND määräaikainen) clearly stated before you give your
details, is it clearly explained how to END a continuous subscription (peruutus/
irtisanominen — the industry's known pain point), is the editor-in-chief named with
newsroom contacts, and is commercial content (kaupallinen yhteistyö, mainokset) clearly
separated from journalism? Does NOT measure content quality.

Useful real pages: tilaa/tilaus (pricing — may live on the publisher's order subdomain
like tilaa.sanoma.fi, otavamedia.fi or a-lehdet.fi order pages, IF the magazine's own
site links there — note this in evidence), asiakaspalvelu (cancellation instructions),
yhteystiedot/toimitus, tilausehdot, mediatiedot. JSN membership counts for
riippumaton_arvio.

Write EXACTLY ONE file: pipeline/extracts/aikakauslehdet__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "tilaushinta_esilla": "kylla|osittain|ei",    // Tilaushinnat (kesto + määräaikainen) selkeästi ennen tietojen antamista
 "tilauksen_peruutus_kerrottu": "kylla|osittain|ei",  // Tilauksen päättäminen ja peruutusehdot kerrottu julkisesti
 "paatoimittaja_esilla": "kylla|osittain|ei",  // Päätoimittaja nimetty ja toimituksen yhteystiedot esillä
 "mainonta_eroteltu": "kylla|osittain|ei",     // Kaupallinen sisältö merkitty ja erottelu kuvattu
 "y_tunnus_esilla": "kylla|osittain|ei",       // Y-tunnus esillä (tai kustantaja selkeästi kerrottu)
 "riippumaton_arvio": "kylla|osittain|ei",     // Riippumaton arviolähde esillä (esim. JSN-jäsenyys, levikintarkastus)
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "kestotilaus_eur_12kk": <number|null>,        // cheapest stated CONTINUOUS subscription price for 12 months in EUR (compute 12 x monthly if quoted monthly); null if not publicly stated
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
