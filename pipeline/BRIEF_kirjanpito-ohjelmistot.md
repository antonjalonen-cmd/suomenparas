# Extraction task — vertical `kirjanpito-ohjelmistot`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish SMB accounting/bookkeeping software (kirjanpito-ohjelmistot),
from the BUYER'S perspective on the public site: is the monthly price visible without signing up
or entering company data? Is there a free trial? Are integrations (bank, invoicing, payroll)
described? Is Finnish-language customer support available?

Write EXACTLY ONE file: pipeline/extracts/kirjanpito-ohjelmistot__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "hinta_esilla": "kylla|osittain|ei",            // Kuukausihinta tai hinnoittelu julkisesti näkyvissä ilman rekisteröitymistä
 "ilmainen_kokeilu": "kylla|osittain|ei",         // Ilmainen kokeilujakso tai freemium tarjolla
 "integraatiot_kuvattu": "kylla|osittain|ei",     // Pankki-, laskutus- tai palkkaintegraatiot kuvattu sivustolla
 "tuki_suomeksi": "kylla|osittain|ei",            // Suomenkielinen asiakastuki (puhelin, sähköposti, chat) mainittu
 "y_tunnus_esilla": "kylla|osittain|ei",          // Y-tunnus tai omistava yhtiö esillä sivustolla
 "ukk_ja_ohjeet": "kylla|osittain|ei",            // Ohjekeskus, oppaat tai UKK saatavilla
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
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation." }
}
Provide `evidence` for at least the six transparency fields (hinta_esilla, ilmainen_kokeilu,
integraatiot_kuvattu, tuki_suomeksi, y_tunnus_esilla, ukk_ja_ohjeet).

IMPORTANT: For Holvi (holvi.com), the Finnish site is at holvi.com/fi/ — use that as the starting
URL. For Procountor, use procountor.fi. For Netvisor, use netvisor.fi.
