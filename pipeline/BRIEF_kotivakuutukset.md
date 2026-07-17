# Extraction task — one INSURANCE PRODUCT LINE page

Read pipeline/EXTRACTION_BRIEF.md FIRST and obey it. It is binding. Key points repeated:
- Only the insurer's OWN public website counts. No comparison sites (vakuutusopas.fi etc.), no blogs.
- "kylla" = fully publicly visible / "osittain" = partial, conditional, or you could not
  positively confirm / "ei" = genuinely absent.
- A BOT-BLOCKED OR COOKIE-WALLED PAGE MUST NOT BE SCORED AS AN OPAQUE PAGE. op.fi and agria.fi are
  known to be bot-protected. If you are challenged, or a page comes back as only a cookie/consent
  shell, SAY SO EXPLICITLY and use "osittain" for anything you cannot positively confirm — never "ei".
- NEVER claim an absence from a page you could not load. Absence claims are the unstable ones.
- Never guess a number. If you did not see it, it is null.
- All output text is FINNISH — it is published verbatim.

SCOPE: score THIS PRODUCT LINE'S OWN PAGE (and the pages it links to: ehdot, tuoteseloste, hinta,
UKK, yhteystiedot). Do NOT score the insurer's front page or a different product line. The whole
point of this category is that the product page is measured, not the company in general.

"Hinta-arvio ilman yhteystietoja" is the key question and means: can a visitor reach a real price
estimate WITHOUT handing over henkilötunnus, name, email or phone? A calculator that asks only for
non-identifying facts (car reg-free details, postcode, apartment size, pet breed/age) counts as
"kylla". One that demands henkilötunnus or contact details before showing any figure is "ei".
"Pyydä tarjous" / "jätä yhteydenottopyyntö" with no instant figure is "ei". If a calculator exists
but you cannot get through it to verify, that is "osittain" — say so.

Write EXACTLY ONE file at the path given in your task. Nothing else.

## JSON shape — pipeline/extracts/kotivakuutukset__<slug>.json
{
 "slug": "<slug>",
 "fetched_ok": ["<every URL you actually loaded and read>"],
 "hintalaskuri_ilman_yhteystietoja": "kylla|osittain|ei",
 "vakuutusehdot_saatavilla": "kylla|osittain|ei",
 "omavastuu_selkeasti": "kylla|osittain|ei",
 "korvausrajat_kerrottu": "kylla|osittain|ei",  // payout caps / limits / ikävähennykset stated publicly
 "y_tunnus_esilla": "kylla|osittain|ei",
 "riippumaton_arvio": "kylla|osittain|ei",
 "omavastuu_min_eur": <number|null>,
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
