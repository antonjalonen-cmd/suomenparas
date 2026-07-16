# Queued categories — Suomen Paras

Anton asked (16.7.2026) for a chain of batches:
- **batch 1** — 5 categories, built immediately in-session
- **batch 2** — 6 more at ~19:45 (task `suomenparas-batch2`)
- **batch 3** — 6 more at ~22:45 (task `suomenparas-batch3`)
- **batch 4** — 6 more at ~00:45 on 17.7 (task `suomenparas-batch4`)

End state: 4 existing + 23 = **27 live categories**.

> Scheduled tasks only run while the app is open. If it's closed at fire time, the
> batch runs on next launch instead. Each batch spawns ~50 agents — this is a large
> token spend, and it runs unattended.

## BATCH 1 (build immediately) — status: IN PROGRESS 16.7.2026

| slug | nimi | why it works |
|---|---|---|
| `puhelinliittymat` | Puhelinliittymät | same operators as laajakaista, lists already verified |
| `luottokortit` | Luottokortit | real FI issuers, prices are public and comparable |
| `sijoitusalustat` | Sijoitusalustat | Nordnet/OP/Nordea/Danske/Mandatum — fees are published |
| `webhotellit` | Webhotellit | Finnish hosts, prices fully public — should score high |
| `vpn-palvelut` | VPN-palvelut | global brands Finns actually buy; strongest affiliate vertical |

## BATCH 2 (build ~19:45 local, 16.7.2026)

| slug | nimi | note |
|---|---|---|
| `pikavipit` | Pikavipit | **LEGAL CARE** — consumer credit. KSL 7:8 disclosure block required; KKV ruled a site presenting loan offers is a *luotonvälittäjä*. No "halvin/paras" claims without evidence. |
| `pankkien-asiakaspalvelu` | Pankkien asiakaspalvelu | OP, Nordea, Danske, S-Pankki, Aktia, POP, Säästöpankki, Oma Sp, Handelsbanken |
| `autovakuutukset` | Autovakuutukset | same 7 insurers, judged on their auto pages |
| `kotivakuutukset` | Kotivakuutukset | same 7 insurers, koti pages |
| `matkavakuutukset` | Matkavakuutukset | same 7 insurers, matka pages |
| `lemmikkivakuutukset` | Lemmikkivakuutukset | fewer insurers offer it — verify who actually does |

## BATCH 3 (build ~22:45, 16.7.2026)

Batches 1+2 empty the whole "Talous ja raha" group. Batches 3-4 must come from the other
groups — so pick only categories with **genuine national chains**, never local one-offs
(see the warning below).

| slug | nimi | candidate brands to VERIFY (not a final list) |
|---|---|---|
| `autokatsastus` | Autokatsastus | A-Katsastus, K1 Katsastajat, Yksityiset katsastusasemat, Katsastus Plus |
| `autovuokraamot` | Autovuokraamot | Hertz, Avis, Sixt, Europcar, Budget, Scandia Rent, Green Motion |
| `optikot` | Optikot | Specsavers, Instrumentarium, Silmäasema, Nissen, Fenno Optiikka |
| `yksityislaakarit` | Yksityislääkärit | Mehiläinen, Terveystalo, Pihlajalinna, Aava, Diacor? (verify — may be Terveystalo) |
| `kuntosalit` | Kuntosalit | SATS, Fressi, LadyLine, Elixia (verify — may be SATS), Liikku, Motion |
| `kiinteistonvalittajat` | Kiinteistönvälittäjät | Kiinteistömaailma, Huoneistokeskus, OP Koti, RE/MAX, SKV, Habita, Bo LKV |

## BATCH 4 (build ~00:45, 17.7.2026)

| slug | nimi | candidate brands to VERIFY (not a final list) |
|---|---|---|
| `hammaslaakarit` | Hammaslääkärit | Oral, Mehiläinen, Terveystalo, Plusterveys, Hammas Hohde |
| `rengasliikkeet` | Rengasliikkeet | Vianor, Euromaster, Rengasmaailma, Motonet, Teboil? (verify) |
| `elainlaakarit` | Eläinlääkärit | Evidensia, Univet, Anicura (verify FI presence), Omaeläinklinikka |
| `muuttopalvelut` | Muuttopalvelut | Niemi Palvelut, Muuttohaukat, Kotimuutto (verify national reach) |
| `siivouspalvelut` | Siivouspalvelut | SOL, Freska, RTK-Palvelu, ISS, Lassila & Tikanoja (verify consumer offering) |
| `autokoulut` | Autokoulut | verify — may be too local; if no national chain exists, SWAP for `lampopumppuasentajat` or `aurinkopaneeliasentajat` |

### ⚠️ Design problem batches 3-4 will hit — read before building

The 67-category roadmap contains many **inherently local** categories (pizzeriat, parturit,
putkiliikkeet, hierojat). Those **cannot be ranked nationally** — there are thousands per city
and "Suomen paras pizzeria" from a website score would be indefensible. The Score measures a
*website*, which is fine for a national chain but meaningless for comparing a Tampere plumber
to a Turku plumber.

**Rule: only build a category if it has genuine national chains with their own websites.**
If a category on the list is local-only, say so in the summary and swap it — do not pad the
count with a comparison that cannot be defended. A smaller correct set beats a padded one.
Local categories need a city dimension (`/pizzeriat/tampere/`) which does not exist yet;
that is a product decision for Anton, not something to improvise at 00:45.

Also note: several batch 3-4 chains overlap owners (e.g. Mehiläinen and Terveystalo appear in
both `yksityislaakarit` and `hammaslaakarit`). That is fine — but measure the category-specific
page, and keep the ownership disclosure honest.

## How to build a category (do NOT skip steps)

1. **Verify the brand list first.** Real brands die quietly — this pipeline has already
   caught Väre (absorbed by Helen 31.5.2026), Säästöpankki non-life (ended 3.6.2025),
   Netplaza (closed 2021), Fi-Nergy (bankrupt 2022), and duplicates that would double-count
   one company as two (Saunalahti=Elisa, Moi=DNA, Adola=Valoo). Confirm every Y-tunnus
   against PRH: `https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=<y>`
   Never invent a Y-tunnus. If a brand can't be verified to exist, DO NOT PUBLISH IT.
2. Add the companies to `pipeline/companies.py`, page copy to `pipeline/vertical_meta.py`,
   and a transparency criteria block to `score_rules.TRANSPARENCY` (weights MUST total 100;
   it is asserted in code). Lead with the same 30-point question in that category's terms:
   *does the company tell you the price before you hand over your data?*
3. Add targets to `pipeline/targets.txt`, run `python pipeline/run_lighthouse.py --file pipeline/targets.txt`
4. One extraction agent per company (Claude Haiku 4.5), each writing ONE json to
   `pipeline/extracts/<vertical>__<slug>.json`. Give them `pipeline/EXTRACTION_BRIEF.md`.
5. `python pipeline/build_vertical.py <slug>` then `python gen_site.py`
6. Verify in the browser (screenshots time out — use `get_page_text` / `javascript_tool`),
   crawl all pages for HTTP 200 + broken links, then commit and push.
7. Add a DESIGN-LOG.md row in the project root.

## KNOWN LIMITATION — read before adding more categories

The AI extraction is **not reproducible**. Measuring 3 companies twice with the same model
and prompt moved scores by up to **±15 points** and reordered the ranking
(see `pipeline/extracts_run2/README.md`). Root cause: the model does not see a stable page
(cookie walls, JS content, 404s), so **"I couldn't find it" gets scored as "it doesn't exist."**

Mitigation now baked into the brief: agents must record which URLs they actually fetched and
must not claim an absence from a page they could not load. **Absence claims are the unstable
ones; existence claims (a price, a quoted figure) are stable.**

Adding categories multiplies this. The real fix before this is a product, not a demo:
multi-run consensus (N=3, per-field majority, flag disagreement).

## ⚠️ BATCHES MUST NOT OVERLAP

Batch 1 ran in-session while batch 2 was scheduled 2h later. If a batch is still
building when the next one fires, they collide:
- `pipeline/lh_cache/_summary.json` is read-modify-write → concurrent runners silently
  lose measurements. `run_lighthouse.py` now takes `lh_cache/.lighthouse.lock` and
  refuses to start if another run holds it (<1h old). **Do not delete that lock to
  "get past" the error** — wait, or you corrupt both runs' data.
- `gen_site.py` + `git commit/push` from two sessions at once will conflict. If a push
  is rejected, `git pull --rebase` first; never force-push.

**Before starting a batch: check `git log` and the lock.** If the previous batch is
still running, wait for it rather than racing it. Finishing one batch correctly beats
starting two badly.

## Gotchas
- Nav holds ~4 categories. Beyond that it needs the dropdown (added 16.7.2026 for batch 1).
- Category shows LIVE only if `data/<slug>.json` exists — never fake a LIVE tile.
- Measurement date is per-vertical. Never relabel an old category with today's date.
- Agents can stall silently: detect by MISSING FILES, not by waiting for a notification.
  If one stalls, relaunch — but the original may wake later and overwrite; check `git diff`.
