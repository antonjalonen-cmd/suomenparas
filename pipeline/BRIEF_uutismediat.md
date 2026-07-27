# Extraction task — vertical `uutismediat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: individual Finnish news media outlets (NOT their parent
companies). Measured from the READER's perspective on the public site: is it clearly
stated what content costs (subscription price and what is behind the paywall — or that
the service is free and how it is funded), is the responsible editor-in-chief (vastaava
päätoimittaja) named with newsroom contact details, is there a public corrections policy
(virheiden korjaus / oikaisut), and is commercial content clearly separated from
journalism (mainokset, kaupallinen yhteistyö merkitty)? Does NOT measure journalistic
quality, political line, or content — only website transparency.

Useful real pages on news sites: tilaa/tilaukset (pricing), footer links like
"yhteystiedot", "toimitus", "vastaava päätoimittaja", "käyttöehdot", "periaatteet",
"oikaisut" / "virheen korjaus", "mediatiedot" (advertising info). JSN (Julkisen sanan
neuvosto) membership counts as an independent oversight mention for riippumaton_arvio.

Write EXACTLY ONE file: pipeline/extracts/uutismediat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "tilaushinta_esilla": "kylla|osittain|ei",    // Tilaushinta ja maksullisuus kerrottu selkeästi ennen tietojen antamista (ilmaismedialla: maksuttomuus ja rahoitusmalli kerrottu)
 "paatoimittaja_esilla": "kylla|osittain|ei",  // Vastaava päätoimittaja nimetty ja toimituksen yhteystiedot esillä
 "oikaisukaytanto_kuvattu": "kylla|osittain|ei",  // Virheiden korjaus- ja oikaisukäytäntö kuvattu julkisesti
 "mainonta_eroteltu": "kylla|osittain|ei",     // Kaupallinen sisältö merkitty ja erottelu journalismista kuvattu
 "y_tunnus_esilla": "kylla|osittain|ei",       // Y-tunnus esillä (tai julkaisijayhtiö selkeästi kerrottu)
 "riippumaton_arvio": "kylla|osittain|ei",     // Riippumaton arviolähde esillä (esim. JSN-jäsenyys, levikintarkastus, ulkoinen tutkimus)
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "tilaushinta_eur_kk": <number|null>,          // cheapest stated digital subscription EUR/month; 0 if the outlet is free; null if not publicly stated
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
