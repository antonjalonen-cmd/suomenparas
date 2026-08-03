# Extraction task — vertical `lentoyhtiöt`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source.
- "kylla" = fully publicly visible / "osittain" = partial or unconfirmable / "ei" = genuinely absent — ONLY from a page you actually loaded.
- Empty shell → retry --js; find real subpages via front page --raw + href grep; never guess deep paths.
- All output text is FINNISH — published verbatim.

WHAT THIS CATEGORY MEASURES: Airlines (lentoyhtiöt) flying regularly FROM Finland, from the
CONSUMER's perspective on the public site: are add-on fees (bags, seat selection, priority
boarding) shown DURING booking before you've committed? Is the total price (taxes and fees
included) visible before payment? Are cancellation/change terms easily findable? Is the loyalty
program's content and tiers explained before you join?

NOTE: Finnair (finnair.com) is Finnish — check for Y-tunnus. All others are global companies —
check for omistaja/rekisteröintimaa disclosed on the site instead of Y-tunnus.

NOTE: These sites are often bot-protected. Use --js flag (headless Chrome) for sites that
return HTTP 000 or thin shells with plain fetch. For SAS (flysas.com) and airBaltic
(airbaltic.com), the Finnish-market pages are in English — that is expected and fine.

Write EXACTLY ONE file: pipeline/extracts/lentoyhtiöt__<slug>.json — nothing else.

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded>"],
 "lisamaksut_nakyy_varauksessa": "kylla|osittain|ei",   // Lisämaksujen (matkatavarat, istumapaikka) hinnat näkyvät varauksen aikana
 "kokonaishinta_ennen_maksua": "kylla|osittain|ei",     // Kokonaishinta verot ja maksut mukaan lukien näytetään ennen maksua
 "peruutus_ja_muutosehdot": "kylla|osittain|ei",        // Peruutus- ja muutosehdot julkisesti saatavilla
 "lojaaliohjelma_kerrottu": "kylla|osittain|ei",        // Lojaaliohjelma, etujen sisältö ja tasot kerrottu
 "omistaja_tai_rekisterointimaa": "kylla|osittain|ei",  // Omistava yhtiö tai rekisteröintimaa kerrottu
 "riippumaton_arvio": "kylla|osittain|ei",
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
Provide `evidence` for at least the six transparency fields.
