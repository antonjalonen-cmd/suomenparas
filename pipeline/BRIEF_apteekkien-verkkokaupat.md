# Extraction task — vertical `apteekkien-verkkokaupat`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish online pharmacies (verkkoapteekki) licensed by Fimea.
Measures the PUBLIC site: are OTC product prices visible without login, are delivery costs
stated before checkout, is the prescription medicine process explained? Does NOT measure
drug safety, lääkeneuvonta quality, or prescription prices (which are Kela-regulated).
Never score anything from inside a logged-in area.

Write EXACTLY ONE file: pipeline/extracts/apteekkien-verkkokaupat__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "otc_hinnat_esilla": "kylla|osittain|ei",     // OTC-tuotteiden hinnat esillä ilman kirjautumista
 "toimitusehdot_esilla": "kylla|osittain|ei",  // Toimitusehdot ja -kulut esillä ennen kassaa
 "resepti_prosessi_selitetty": "kylla|osittain|ei", // Reseptilääkkeiden tilausohje kuvattu
 "palautuspolitiikka_kerrottu": "kylla|osittain|ei", // Palautusoikeus ja -ehdot kerrottu
 "y_tunnus_esilla": "kylla|osittain|ei",       // Y-tunnus tai apteekkiluvan haltija esillä
 "riippumaton_arvio": "kylla|osittain|ei",     // Riippumaton arviolähde esillä (Fimea-linkki lasketaan)
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "mobiilisovellus": "kylla|osittain|ei",
 "kk_hinta_alkaen_eur": <number|null>,    // null always (apteekit don't have monthly subscriptions)
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.

NOTES:
- Fimea-rekisteröintilinkki tai FIMEA-logo sivulla = riippumaton_arvio "kylla"
  (it's an independent regulatory body, not a self-generated review).
- OTC = ilman reseptiä myytävät tuotteet (vitamiinit, käsikauppalääkkeet, kosmetiikka).
  Jos tuotteen saa lisättyä koriin ja hinnan näkee ilman kirjautumista = "kylla".
- Reseptiä vaativat lääkkeet: score "resepti_prosessi_selitetty" = "kylla" jos prosessi
  (kanta.fi-linkitys, e-resepti ohje) on selitetty sivulla ilman kirjautumista.
- Apteekin Y-tunnus tai apteekkiluvan haltijan nimi toimitusehdoissa tai footer = "kylla".
- Jos sivusto on botti-estojen takana: merkitse kaikki "osittain", fetched_ok tyhjäksi
  paitsi URL joka vastasi, ja lisää yhteenveto-kohtaan maininta mittausaukosta.
