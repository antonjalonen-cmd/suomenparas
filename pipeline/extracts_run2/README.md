# extracts_run2 — accidental second measurement (16.7.2026)

**This is the most useful data in the repo. Do not delete it.**

Three extraction agents appeared to hang, so they were re-launched. The originals
were not dead — they finished ~33 minutes later and overwrote their files. That
accident produced something the pipeline never otherwise gets: **the same company,
same model (Claude Haiku 4.5), same prompt, measured twice.**

The two runs disagree.

| Company | run1 (published) | run2 | Δ score | scored fields differing |
|---|---|---|---|---|
| BLC | 79,4 | 64,8 | **−14,6** | 6 |
| Turva | 49,9 | 62,8 | **+12,9** | 5 |
| Elisa | 64,4 | 61,1 | −3,3 | 4 |

Examples of direct contradictions:
- BLC `kampanjan_jalkeinen_hinta`: `kylla` vs `ei` (worth 20 points)
- Turva `korvausprosessi_kuvattu`: `ei` vs `kylla`
- Turva `riippumaton_arvio`: `ei` vs `kylla` (EPSI)
- Elisa `mobiilisovellus`: `ei` vs `kylla`

## Why it happens

The model does not see a stable page. Verified by hand on turva.fi (16.7.2026):
- `turva.fi/asiakaspalvelu` is a **404** — an agent fetching it records "not found"
- the real nav sits behind a **cookie-consent wall**, so an unrendered fetch sees almost nothing
- `TaskuTurva` demonstrably exists on the front page, yet run1 recorded `mobiilisovellus: osittain`

So **"I could not find it" was scored as "it does not exist"**. Absence claims are
where the variance lives; existence claims (a price, a quoted figure) are far more stable.

## Consequence

The Score *formula* is deterministic — same inputs, same output. Its *inputs* are not.
Differences under ~15 points are noise, not ranking. Turku Energia beating Omavoima
78,7 vs 78,6 is meaningless at this precision. Large, structural gaps (If 76,2 vs
Pohjola 28,2 — pricing public vs behind a bank login) survive the noise and are real.

This limitation is disclosed on the live metodologia page rather than hidden.

## Fix before this is a product

1. **Multi-run consensus** — measure each company N=3 times, take the per-field majority,
   and flag disagreement instead of averaging it away. Cheapest real fix.
2. **Render the page properly** — headless browser with consent dismissal, not a raw
   fetch. Confirm HTTP 200 before recording any absence.
3. **Never score an absence from a single run.** Require a second confirmation for any
   `ei`, or downgrade it to "ei varmistettu".
4. **Verify verbatim quotes** by re-fetching and substring-matching (see EXTRACTION_BRIEF).
5. Publish a confidence band per score, not a false-precision decimal.

---

## Second accidental replication (17.7.2026) — the effect is not a one-off

It happened again, the same way, during the batch-2 build. Two agents were re-launched
after appearing to hang; both originals woke up **~35 minutes and ~2 hours later** and
overwrote their files *after the site had already been built and pushed*. One of them,
`kotivakuutukset__lahitapiola`, gave a second independent reading of the same page.

**6 of 12 scored fields disagreed** (same model, same prompt, same URL, same day):

| Field | run1 (published) | run2 (late agent) |
|---|---|---|
| `omavastuu_selkeasti` | `osittain` | `kylla` |
| `korvausrajat_kerrottu` | `osittain` | `kylla` |
| `y_tunnus_esilla` | **`ei`** | **`osittain`** |
| `aukioloajat_esilla` | `osittain` | `ei` |
| `mobiilisovellus` | **`kylla`** | **`ei`** |
| `hintalaskuri_ilman_yhteystietoja` | `osittain` | *(agent typo'd the key)* |

Same signature as 16.7: the disagreements are concentrated in **absence claims**, and
they swing in *both* directions — run2 was more generous on the insurance terms and
harsher on reachability. `mobiilisovellus` flipped `kylla`→`ei` for a company that
plainly has an app, which is the 16.7 Elisa failure repeating exactly.

run1 (the published version) is kept in `kotivakuutukset__lahitapiola.RUN1-PUBLISHED.json`.
run2's body was not preserved — it was reverted before being copied, and the field-level
diff above is the verified record. Do not reconstruct it from memory; that would be
inventing a measurement.

### What this strengthens

The 16.7 conclusion was drawn from **3** companies. This is a 4th, from a different
category, with the same result — so the ±15-point figure on the methodology page is not
an artefact of one bad afternoon. It is the method's actual precision.

### Operational lesson (cost real damage this time)

A "stalled" agent is often **not dead**. Twice now the original has woken up late and
silently overwritten a re-run — and on 17.7 it did so *after commit and push*, so a
clean `git status` at build time proved nothing. It also wrote a typo'd key and a BOM,
which `check_extracts.py` would have caught, but only if someone re-ran it.

**Always `git diff` the extracts again after the build, not just before.**

### Third replication, same day: `autovakuutukset__lahitapiola`

A third late agent overwrote its file too. Here only **1 of 12** fields disagreed — but it
was the one that matters most:

| Field | run1 (published) | run2 (late agent) |
|---|---|---|
| `hintalaskuri_ilman_yhteystietoja` | **`ei`** | **`osittain`** |

That is the category's **30-point** criterion — the whole question the site is built on —
so a single flip is a **15-point** swing, and it moves LähiTapiola's rank. Both runs read
the same page on the same day. run1 concluded the calculator demands henkilötunnus; run2
concluded it could not verify the form's requirements without interacting with it.

**run2 is arguably the more honest answer**, and that is the uncomfortable part: the
disagreement is not random noise here, it is two defensible readings of a JS calculator
that neither run could actually operate. The published `ei` asserts an absence the agent
did not prove. Do not "fix" this by hand-picking the nicer answer — the real fix is a
fetch that can drive the calculator, and until then this field is soft in every insurance
category.

**Pattern across all three 17.7 replications: the variance is entirely in absence claims.**
Nothing that quotes a real figure ever moved.

### Fourth replication: `lemmikkivakuutukset__if` — the cleanest evidence in the file

A fourth late agent overwrote its file. This one is the most useful of all, because the
same JSON contains both halves of the thesis at once:

**The quoted figure did not move:**

| Field | run1 | run2 |
|---|---|---|
| `korvauskatto_eur_vuosi` | **4000** | **4000** |

**Every disagreement was an absence claim — 4 of 12:**

| Field | run1 (published) | run2 (late agent) |
|---|---|---|
| `y_tunnus_esilla` | `ei` | `osittain` |
| `riippumaton_arvio` | `osittain` | `ei` |
| `puhelin_esilla` | **`ei`** | `osittain` |
| `aukioloajat_esilla` | `osittain` | `kylla` |

`puhelin_esilla: ei` for **If** — one of the largest insurers in Finland, which obviously
publishes a phone number — is simply wrong in the published run. Same shape as the 16.7
NordVPN and Elisa errors. Nothing that quoted a real number ever moved; everything that
claimed a thing was *missing* did.

**New finding: `ai_arviot` is not stable either, and nobody had measured that.**

| | selkeys | hintojen_loydettavyys | sisallon_kattavuus |
|---|---|---|---|
| run1 | 78 | **62** | 76 |
| run2 | 85 | **90** | 85 |

That is a 28-point swing on one sub-metric. Weighted, the AI pillar moves **72,1 → 86,7
(+14,6)**, and since it is 20 % of the Score, **+2,9 points on the published total** from
subjective judgement alone — before any ternary field is counted. Prior replication work
only ever compared the ternary fields, so this component of the noise was invisible.

**Consolidated view of the four 17.7 replications:** absence claims and subjective 0-100
ratings are both unstable; quoted figures are stable. That is an argument for shifting the
Score's weight toward things a page literally states, and away from "we could not find it".
