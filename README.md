# Suomen Paras — demo

Suomen läpinäkyvin vertailupalvelu (konseptidemo).

- **Pisteytys:** Suomen Paras Score v1.1 (deterministinen, dokumentoitu metodologia-sivulla)
- **Data:** oikeista julkisista lähteistä (yritysten verkkosivut, YTJ/PRH, Lighthouse, Claude Haiku 4.5)
- **Demo:** https://suomenparas.antonjalonen.fi (noindex)
- **Lokaalisti:** launch.json `suomenparas` → http://localhost:8742

## Kategoriat (live)

| Kategoria | Yrityksiä | Mitattu |
|---|---|---|
| Lainavertailu | 9 | 15.7.2026 |
| Vakuutukset | 7 | 16.7.2026 |
| Sähkösopimukset | 9 | 16.7.2026 |
| Laajakaista | 9 | 16.7.2026 |
| Puhelinliittymät | 7 | 16.7.2026 |
| Luottokortit | 8 | 16.7.2026 |
| Sijoitusalustat | 7 | 16.7.2026 |
| Webhotellit | 7 | 16.7.2026 |
| VPN-palvelut | 9 | 16.7.2026 |
| Kulutusluotot | 6 | 17.7.2026 |
| Autovakuutukset | 6 | 17.7.2026 |
| Kotivakuutukset | 6 | 17.7.2026 |
| Matkavakuutukset | 6 | 17.7.2026 |
| Lemmikkivakuutukset | 6 | 17.7.2026 |
| Sähkövertailupalvelut | 9 | 17.7.2026 |

Measurement dates live in `build_vertical.MEASURED` — per vertical, set when it was actually
measured. Rebuilding an old category must never restamp it with today's date.

## Pipeline

```
pipeline/targets.txt          <vertical>__<slug>=<domain>
pipeline/companies.py         verified metadata (Y-tunnus, omistaja) + why brands were EXCLUDED
pipeline/score_rules.py       Score v1.1 pillars + per-vertical transparency criteria
pipeline/vertical_meta.py     per-vertical page copy (h1, lead, notes)
pipeline/EXTRACTION_BRIEF.md  rules handed to every extraction agent
pipeline/fetch_page.py        fetch a page as a real browser sees it (WebFetch is blocked on some)
pipeline/check_extracts.py    validate extracts BEFORE they can reach a page

python pipeline/run_lighthouse.py --file pipeline/targets.txt   # -> pipeline/lh_cache/
# extraction agents (Claude Haiku 4.5, one per company)         # -> pipeline/extracts/
python pipeline/check_extracts.py <vertical> ...                # MANDATORY gate — see below
python pipeline/build_vertical.py vakuutukset sahkosopimukset laajakaista   # -> data/*.json
python gen_site.py                                              # data/*.json -> static pages
```

**Always run `check_extracts.py` before building.** On 17.7.2026 five separate extraction
agents responded to a failed fetch by inventing a redirect to another company in the same
list ("risicum.fi redirects to saldo.com", "pohjantahti.fi redirects to fennia.fi",
"omasp.fi redirects to Danske Bank" — all false, all HTTP 200). Two of them went on to
describe the competitor's website in the wrong company's file. The checker fails any extract
that never loaded its own domain, that names a competitor's domain, or that leaves a scored
field null. Do not hand-edit a bad extract into passing — re-run it.

Adding a category = add its entry to `companies.py` + `vertical_meta.py` + `score_rules.TRANSPARENCY`,
run the pipeline, done. `gen_site.py` is vertical-agnostic, and a category only shows as LIVE
if its data file actually exists.

## Score v1.1

Four pillars: Digitaalinen laatu 30 % (Lighthouse mobile), Läpinäkyvyys 30 %, Tavoitettavuus 20 %,
AI-laatuarvio 20 %.

v1.0 → v1.1: **Läpinäkyvyys became vertical-specific.** The other three pillars are measured
identically everywhere. Each vertical's transparency pillar leads with the same 30-point question
in its own terms — *does the company tell you the price before you hand over your data?*

## Notes / gotchas

- **Keyless PageSpeed API is dead** (429 even with long backoff). Use local `npx lighthouse`;
  production should use PSI with a key. Lighthouse "Chrome kill" exit≠0 is harmless — the JSON
  still lands. NO_NAVSTART on heavy JS sites → retry with `--max-wait-for-load=60000`.
- **PRH open data:** `opendata-bis-v1` now serves HTML. The live endpoint is
  `https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=<y-tunnus>`.
- **Measurement dates are per-vertical.** Never relabel an old vertical with today's date —
  the methodology page promises results are not rewritten retroactively.
- **Verify the brand list every run.** Real brands die quietly: Väre was absorbed by Helen
  31.5.2026, Säästöpankki stopped selling non-life 3.6.2025, Netplaza closed 31.12.2021,
  Fi-Nergy went bankrupt 2022. See the exclusion lists in `companies.py`.
- Browser-pane screenshots time out on this project; `get_page_text` / `javascript_tool` work.

`scores.json` is the archived v1.0 raw input for lainavertailu; `migrate_to_verticals.py` converted
it into `data/lainavertailu.json`. Neither is needed to rebuild the site.
