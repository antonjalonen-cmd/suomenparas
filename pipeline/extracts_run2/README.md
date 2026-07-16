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
