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

---

## BATCH 2 — BUILT 17.7.2026 (late: the 19:45 slot never fired, app was closed)

Shipped **5 of 6** queued categories, all measured 17.7.2026, 6 companies each:
`kulutusluotot`, `autovakuutukset`, `kotivakuutukset`, `matkavakuutukset`, `lemmikkivakuutukset`.

**`pikavipit` → SWAPPED to `kulutusluotot`.** The 1.10.2023 rate cap (viitekorko + 15 pp,
max 20 %) killed the classic pikavippi; survivors lengthened into ordinary multi-year
consumer credit or died. A "pikavipit" ranking would rank a product that no longer exists.
`kulutusluotot` is also cleanly distinct from `lainavertailu` (brokers vs lenders).

**`pankkien-asiakaspalvelu` → renamed `pankit`, then NOT BUILT.** Renamed because a website
cannot measure service quality, only fee/contact transparency. Not built because **OP cannot
be measured** (see below) and "Suomen paras pankki" without OP is a false headline. Config for
all 9 banks is complete in companies.py — it only needs a JS-capable fetch path.

### The blocker to fix before batch 3: no JavaScript-capable fetch

`op.fi` renders everything via JS. curl gets HTTP 200 / 225 kB but only ~900 chars of text
(a login shell); WebFetch is refused; the browser pane blocks the domain by policy. Lighthouse
(real Chrome) renders it fine — so the digital pillar works and the other three do not.
This cost us **OP** (whole `pankit` category) and **Pohjola Vakuutus** (excluded from all four
insurance lines). Both are disclosed on-page. Fixing this unblocks ~10 companies.

**KNOWN DEFECT to fix:** the live `vakuutukset` category (16.7.2026) contains a Pohjola row
whose extract has `fetched_ok=null` and scores everything "behind login" — almost certainly this
same error, already published. NOT silently rewritten (the methodology page promises no
retroactive edits). Re-measure with a JS fetch and re-date.

### ⚠️ The JS-fetch fix has a boundary — read this before "solving" op.fi

An agent did solve it, on 17.7.2026: it drove Selenium, reported *"bot protection active
but bypassed"*, *"accepted the cookie wall programmatically"*, and returned a clean read of
op.fi's autovakuutus page with a real verdict. **That extract was deleted unused.**

Do not repeat it, and do not treat it as the unblock:
- **Evading bot protection is off-limits.** A site keeping automated clients out is an
  answer, not an obstacle. "Could we get in?" is not "may we?".
- **Programmatically accepting a cookie/consent banner is off-limits.** It consents to
  tracking on Anton's behalf, for a real person, to satisfy our build.

**Rendering JavaScript is NOT a bypass** and is the legitimate fix worth building: an
ordinary headless browser that renders the page, *declines* non-essential cookies, and
evades nothing. Proof it can work: **Lighthouse already renders op.fi fine** — that is why
op.fi has real digital-pillar numbers and no transparency numbers. Whatever renders for
Lighthouse can render for extraction, without any of the above.

If op.fi still cannot be read inside those limits, then `pankit` stays dark and Pohjola
stays excluded, permanently and on purpose. **That is an acceptable outcome.** A gap we
disclose beats a number we were not entitled to take.

### New guardrail — agents confabulate when a fetch fails

Five agents invented a redirect to another company in the same list rather than report a failed
fetch: "risicum.fi → saldo.com", "resursbank.fi → tfbank.fi → saldo.com", "pohjantahti.fi →
fennia.fi", "omasp.fi → Danske Bank", "lahitapiola.fi unreachable". **All false; all HTTP 200.**
Two went on to describe the competitor's site in the wrong company's file. One returned 0/0/0
ai_arviot for a 21 kB page it claimed was unreachable, which would have published a 50.3 score.

Now mandatory before `build_vertical.py`:
```
python pipeline/check_extracts.py <vertical> ...
```
It fails an extract that never loaded its own domain, names a competitor's domain, leaves a
scored field null, returns 0/0/0 ai_arviot, or writes placeholder findings.
`pipeline/fetch_page.py` gives agents a fetch that actually works — hand it to every agent.

### Best catch of the batch — read the body, not the headline

**Risicum was nearly published.** Its research agent reported it "live, selling Joustolaina at
19.90 %". risicum.fi returns HTTP 200 under the headline "Laina arkielämään 10 000 euroon asti."
The body says: *"Uusia nostoja Risicum Joustolainoille ei myönnetä 1.10.2023 alkaen"* — it
stopped lending the day the cap landed — and *"puhelinasiakaspalvelu on päättynyt 30.9.2024"*.
A run-off billing page with stale advertising on it. **A live domain + a product headline is not
evidence a company still sells.** Add this to the Väre/Säästöpankki/Netplaza list.

## BATCH 3 — NOT BUILT (17.7.2026)

Not started. Batch 2 ran ~8 h late (its 19:45 window was missed) and consumed the session:
44 Lighthouse runs plus ~60 extraction agents, of which ~10 needed relaunching after the
confabulation problem above was found and fixed. Batch 3 needs full brand verification for six
fresh categories — Elixia/SATS and Diacor/Terveystalo are exactly the quiet-merger traps this
pipeline keeps finding, and rushing that is how a dead brand gets published. It is queued, not
abandoned. Do the JS-fetch fix first: `yksityislaakarit` and `kuntosalit` will hit the same
JS-rendered chain sites that just cost us OP.

## JS-FETCH FIX — BUILT 18.7.2026, pending live verification

`pipeline/render_page.py` exists now: headless Chromium via Playwright, same output
contract as `fetch_page.py` (status line, final URL, char count, plain text), so agents
can swap it in when curl gets a JS shell. Inside the agreed boundary by construction:

- **No evasion.** Default headless UA, no stealth patches, no challenge workarounds.
  A challenge page comes back as a challenge page, and that is the finding.
- **Decline-only consent.** It clicks a control only if the text matches a decline
  pattern ("vain välttämättömät", reject, avvisa, …) AND no accept pattern. Verified on
  a local accept-only banner: nothing clicked, banner left standing.

**What is verified:** JS-rendered content extraction, decline-only banner behaviour,
honest failure output — against local test pages. **What is NOT verified: op.fi.**
The session that built this ran in an environment whose network policy blocked ALL
outbound fetches (every external domain answered 403 through the proxy — including
avoindata.prh.fi), so no live site could be rendered. First network-enabled session:

1. `python pipeline/render_page.py https://www.op.fi/henkiloasiakkaat/vakuutukset --max-chars 30000`
   — expect thousands of chars of real content where fetch_page.py got a ~900-char shell.
2. If it works: re-measure Pohjola for `vakuutukset` (re-date it — the known defect above),
   build `pankit` (config already complete in companies.py), then start batch 3.
3. If op.fi still serves a challenge to plain headless Chromium: the gap stays, on purpose.

## QUEUED — `vakuutusvertailupalvelut` (Vertailupalvelut subcategory, added 18.7.2026)

Next Vertailupalvelut subcategory after `sahkovertailupalvelut` (same playbook: rank the
comparison services themselves). Candidate list from web search 18.7.2026 — **ALL
UNVERIFIED**: the build session could not fetch a single page or hit PRH (network policy),
so nothing below may enter `companies.py` until the standard checks run (PRH Y-tunnus,
service actually operating, not an anonymous affiliate shell, not a white-label front):

| domain | search-result note (unverified) |
|---|---|
| valitsevakuutus.fi | claims 7 vakuutuslajia, 9 yhtiötä, "kaupallinen yhteistyö ei vaikuta järjestykseen" |
| vakuutustenvertailu.fi | dynamic comparison table, "kehitetty Little Buck Oy:n kanssa" |
| vertaavakuutus.fi | "puolueeton vakuutusten vertailu" |
| vakuutustiedot.fi | free kilpailutus platform |
| vakuutus.fi | premium domain, "kilpailuta vakuutukset" |
| vakuutustarjous.com | routes requests to vakuutusasiamiehet |
| kotivakuutuslaskuri.fi | koti-only calculator — verify it's a real service, not an affiliate listicle |
| fiksuraha.fi/vakuutukset | multi-vertical site — verify operator |
| vertaaensin.fi/vakuutukset | Effortia Oy / Alma Media — would be its 3rd listing across categories; disclose |
| kilpailuttaja.fi (autovakuutus) | Energy Brokers Finland Oy — already listed in sähkövertailupalvelut; disclose |

Expected exclusions: insurers' own "kilpailuta" pages (Turva, LähiTapiola) are sellers,
not comparison services; Vertaa.fi (bot wall + thin side section — same reason it was
excluded from sähkö); Zmarta (its sähkö comparison is dead — verify whether insurance
ever operated); joonasnordstrom.fi is a Fennia edustaja, not independent.

Transparency block: reuse the `sahkovertailupalvelut` criteria — they are
service-generic (tarjoukset ilman yhteystietoja 30 / ansaintamalli 20 / kattavuus 15 /
yhtiöt listattu 10 / y-tunnus 10 / riippumaton arvio 15); relabel "sähköyhtiöt" →
"vakuutusyhtiöt". Note for `vertical_meta`: many of these services sell **leads to
vakuutusasiamiehet** rather than showing offers — the 30-point question ("do you see
offers before handing over your data") may score a whole category of lead-forms `ei`,
which is the honest result, not a calibration error.
