# Extraction brief — Suomen Paras Score v1.1

Shared instructions handed to every extraction agent. One agent per company.
The agent reads only the company's own public website and writes one JSON file.

## Hard rules

1. **Only the company's own public website counts** as a source for the scored
   fields. No third-party comparison sites, no marketing blogs.
2. **Never guess.** If you cannot find a thing, mark it `"ei"`. If it exists but
   is incomplete, hidden behind a login, or requires contact details, mark it
   `"osittain"`. Do not reward intent — reward what a visitor can actually see.
3. **The JS trap.** Some sites render prices/values with JavaScript, so the
   static HTML shows an empty placeholder. If the value only appears in a real
   browser, that still counts as visible — but if you cannot confirm it renders,
   mark `"osittain"` and say so in the evidence. (Verified real case 15.7.2026:
   Omalaina/Sambla korkoesimerkki values are empty in static HTML.)
4. **Evidence** is published under a "HAVAINTO" (observation) label, NOT as a
   quotation — because in practice much of it records what is *missing*, and an
   absence cannot be quoted. Write it as a short factual observation of what a
   visitor sees. Prefer verbatim page text where it exists.
   > Known gap (16.7.2026): the first run asked for verbatim quotes, but ~2/3 of
   > returned strings were paraphrase. Rendering them in quote marks would have
   > attributed our words to the company, so the site now labels them HAVAINTO.
   > If verbatim quoting is wanted as a feature, the pipeline needs a verification
   > step that re-fetches the page and confirms the substring actually occurs —
   > do not trust a model's claim that a string is verbatim.
5. **Be honest, not generous.** These scores are published with sources next to
   them. A wrong "kylla" is worse than a harsh "ei".
6. `"kylla"` = fully and publicly visible. `"osittain"` = partial/conditional.
   `"ei"` = absent.

## Values

- Ternary fields: exactly `"kylla"` | `"osittain"` | `"ei"`.
- `ai_arviot`: integers 0-100, your own judgement of the site as a consumer sees it.
  - `selkeys` — is the information clearly organised and readable?
  - `hintojen_loydettavyys` — how many clicks/forms until a real price?
  - `sisallon_kattavuus` — does it answer the questions a buyer actually has?
- `vahvuudet` / `kehityskohteet`: exactly 3 each, short Finnish, concrete and
  specific to THIS site (not generic filler).
- `yhteenveto`: 2-3 sentences of neutral Finnish prose. State what the company is
  and what the site does well/badly. No marketing tone.

All output text is **Finnish** — it is published verbatim on a Finnish site.
