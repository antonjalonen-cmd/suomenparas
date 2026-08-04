# Extraction task — vertical `sahkoautojen-lataus`

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the company's OWN public website counts as a source. No comparison sites, no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent — and ONLY from a page you actually loaded.
- If a page comes back suspiciously empty, retry with `--js`; on SPA sites fetch the front
  page with `--raw`, grep the hrefs and follow REAL nav links — never guess deep paths.
- NEVER claim an absence from a page you could not load.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

WHAT THIS CATEGORY MEASURES: Finnish public EV charging services available to consumers.
Measures the PUBLIC site: is pricing (€/kWh or €/min) publicly visible before starting a
charge? Is the charging network size stated? Is there a free mobile app? Is Finnish customer
service described? Can you charge without mandatory registration or subscription? Never score
anything from inside a logged-in area or app.

COMPANY-SPECIFIC NOTES:
- k-lataus: domain is k-lataus.fi which redirects to www.k-auto.fi/k-lataus/ — use the
  redirected URL. Check /k-lataus/hinnoittelu or /k-lataus/asiakaspalvelu subpages.
  Pricing section mentions AC/DC pricing visible to registered and unregistered users.
- abc-lataus: use abcasemat.fi/sahkoauton-lataus/ — check also
  abcasemat.fi/sahkoauton-lataus/hintatiedot-ja-bonus/ for pricing transparency.
  Note: pricing varies by ABC station (regional cooperatives set prices independently).
- ionity: use ionity.eu/fi/ — this is the Finnish-language page. Look for pricing
  (Tilaukset/subscriptions section), map of stations, customer service/support links.
  IONITY is a European fast-charging network, so Finnish may be partial.
- fortum-charge-drive: use chargedrive.com (auto-redirects to /fi-FI). Look for
  subscription options (Fortum Latauspaketti), pricing per kWh for fast charging,
  customer service contact, and Latauskartta (charging map).
- recharge: use rechargeinfra.com/fi/ — Finnish language page. Look for Hinnat ja
  maksu, Latausohjeet, Recharge app, and customer service info.
- helen-lataus: use helen.fi — navigate to Sähköauton lataus section. Look for
  helen.fi/sahkoauton-lataus/rekisteroidy-helen-latauksen-asiakkaaksi and linked pages.
  Helen has 800+ charging points; pricing should be in Oma Helen section or public page.

Write EXACTLY ONE file per company: pipeline/extracts/sahkoautojen-lataus__<slug>.json

JSON shape (all keys required):
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hinnoittelu_esilla": "kylla|osittain|ei",      // Latausten hinnoittelu (€/kWh tai €/min) julkisesti esillä ilman kirjautumista
 "latausverkosto_koko": "kylla|osittain|ei",      // Latausasemien tai -pisteiden määrä Suomessa kerrottu
 "mobiilisovellus": "kylla|osittain|ei",          // Mobiilisovellus saatavilla ilmaiseksi (iOS/Android)
 "asiakaspalvelu_suomi": "kylla|osittain|ei",     // Suomenkielinen asiakaspalvelu kuvattu (aukioloajat, puhelin tai chat)
 "kaytto_ilman_rekisteroitymista": "kylla|osittain|ei",  // Lataus mahdollista ilman pakollista tiliä tai sopimusta
 "omistaja_kerrottu": "kylla|osittain|ei",        // Omistava yhtiö tai Y-tunnus esillä sivustolla
 "puhelin_esilla": "kylla|osittain|ei",
 "email_esilla": "kylla|osittain|ei",
 "chat_mainittu": "kylla|osittain|ei",
 "aukioloajat_esilla": "kylla|osittain|ei",
 "ukk_osio": "kylla|osittain|ei",
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["", "", ""],
 "kehityskohteet": ["", "", ""],
 "yhteenveto": "2-3 neutral Finnish sentences",
 "evidence": { "<field_key>": "HAVAINTO: short factual Finnish observation of what a visitor sees." }
}
Provide `evidence` for at least the six transparency fields.
