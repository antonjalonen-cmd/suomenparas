Read C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\EXTRACTION_BRIEF.md FIRST and follow every rule.

Analyse **{DOMAIN}** (brand: {BRAND}) — VPN service, as a Finnish consumer would see it. {NOTE}
Prefer the Finnish-language pages if they exist (e.g. /fi/). Judge the pricing, privacy and company/about pages. Only what a visitor sees WITHOUT an account.

Work efficiently: ~8 pages max, then WRITE THE FILE. The written file is the only deliverable.
Write to: C:\Users\anton\Downloads\Claude Site\suomenparas\pipeline\extracts\vpn-palvelut__{SLUG}.json

Exact JSON (no extra keys, no markdown fence):
{
 "slug": "{SLUG}",
 "fetched_ok": ["<urls you actually loaded successfully>"],
 "hinta_esilla_ilman_yhteystietoja": "kylla|osittain|ei",
 "uusimishinta_kerrottu": "kylla|osittain|ei",
 "omistaja_kerrottu": "kylla|osittain|ei",
 "lainkayttoalue_kerrottu": "kylla|osittain|ei",
 "lokikaytanto_kerrottu": "kylla|osittain|ei",
 "riippumaton_auditointi": "kylla|osittain|ei",
 "suomenkielinen_sivu": "kylla|ei",
 "puhelin_esilla": "kylla|ei", "puhelin": "<string or null>",
 "email_esilla": "kylla|ei", "chat_mainittu": "kylla|ei",
 "aukioloajat_esilla": "kylla|ei", "ukk_osio": "kylla|ei", "mobiilisovellus": "kylla|ei",
 "halvin_kk_hinta_eur": <number or null>,
 "ai_arviot": {"selkeys": 0-100, "hintojen_loydettavyys": 0-100, "sisallon_kattavuus": 0-100},
 "vahvuudet": ["...","...","..."],
 "kehityskohteet": ["...","...","..."],
 "yhteenveto": "...",
 "evidence": {"omistaja_kerrottu": "<observation>", "uusimishinta_kerrottu": "<observation>", "lokikaytanto_kerrottu": "<observation>"}
}

Meanings:
- hinta_esilla_ilman_yhteystietoja: is a real price visible without creating an account or giving an email?
- uusimishinta_kerrottu: KEY DARK-PATTERN CHECK. VPNs advertise a low long-term price (e.g. "2,99 e/kk") that renews far higher. Is the RENEWAL price stated next to the offer? "kylla" = clearly shown. "osittain" = fine print or a separate terms page only. "ei" = not stated.
- omistaja_kerrottu: **THE KEY CRITERION FOR THIS CATEGORY.** Does the site say which company OWNS it? Several major VPNs share a parent: Kape Technologies owns ExpressVPN, CyberGhost and Private Internet Access; Nord Security and Surfshark share the Cyberspace B.V. holding. A product sold on privacy that will not name its parent should lose points for that. "kylla" = the parent/owning company is named plainly somewhere on the site (an about/company page counts). "osittain" = only the operating entity is named, not the ultimate owner. "ei" = no ownership information at all.
- lainkayttoalue_kerrottu: is the legal jurisdiction stated (e.g. Panama, Switzerland, BVI)? Relevant to 5/9/14-Eyes.
- lokikaytanto_kerrottu: is the no-logs / logging policy described concretely, not just as the slogan "no logs"?
- riippumaton_auditointi: is an INDEPENDENT third-party audit named (e.g. Deloitte, Cure53, PwC), ideally with a date? A self-declared "audited" with no auditor named = "osittain".
- suomenkielinen_sivu: does a genuine Finnish-language version exist?
- halvin_kk_hinta_eur: cheapest publicly stated monthly price. Note in evidence if it requires a long commitment. null if not visible. Do NOT guess.

CRITICAL: `fetched_ok` must list only URLs that actually returned real content. Some VPN sites block bots (Cloudflare 403). If you get blocked, leave that URL out of `fetched_ok` and DO NOT record absences for pages you could not load — use "osittain" and explain in evidence. **A blocked fetch is not evidence of absence.**

After writing, verify the file exists, then reply ONLY: "{SLUG} OK" plus one sentence on anything unusual.
