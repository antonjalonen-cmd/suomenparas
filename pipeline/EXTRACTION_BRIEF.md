# Extraction brief — Suomen Paras Score v1.1

Shared instructions handed to every extraction agent. One agent per company.
The agent reads only the company's own public website and writes one JSON file.

## ⚠️ `fetched_ok` is necessary but NOT sufficient (learned 16.7.2026)

The NordVPN agent listed `nordvpn.com/fi/features/no-log-vpn/` in `fetched_ok` and then
recorded "no jurisdiction stated" and "no independent audit". That page plainly says
*"NordVPN toimii Panamasta käsin"* and names **Deloitte** across six audits. Cloudflare
had served the agent a degraded version of a page it believed it had read. Three fields
were wrong — **40 transparency points** — and it would have ranked the biggest VPN in the
category near the bottom for hiding things it publishes prominently.

**A bot-blocked site must not be scored as an opaque site.** If a page looks suspiciously
empty, or the site is known to use bot protection (Cloudflare, Akamai, PerimeterX):
1. say so explicitly in your reply, and
2. use `"osittain"` for anything you cannot positively confirm — never `"ei"`.

Penalising a company for blocking a crawler, rather than for what it shows humans, is a
measurement error, not a finding.

## ⚠️ A blocked fetch makes agents INVENT redirects (learned 17.7.2026)

The single biggest failure of the batch-2 run. When their fetch tool returned nothing
useful, agents did not report the failure — they confabulated a tidy explanation, and
the explanation was always "this site now redirects to a company you already mentioned":

| The claim | The truth |
|---|---|
| "risicum.fi redirects to saldo.com" | risicum.fi = HTTP 200, own content. The agent then described **Saldo's** site inside Risicum's file. |
| "resursbank.fi redirects to tfbank.fi → saldo.com" | Three unrelated competitors. All three load fine. |
| "pohjantahti.fi redirects to fennia.fi" | HTTP 200, own content. |
| "omasp.fi redirects to Danske Bank" | HTTP 200, own content. |
| "lahitapiola.fi is not accessible" | HTTP 200, own content. |

Two of these would have **published one company's website under a competitor's name** —
the worst error this project can make. `pipeline/check_extracts.py` now fails any extract
whose `fetched_ok` names a competitor in the same vertical, or omits its own domain.

**If a page will not load, say so and score `"osittain"`. Never explain why.** You do not
know why. A redirect you did not personally follow is not an observation, it is a story.

## Use `fetch_page.py` — WebFetch is blocked on several of these sites

    python pipeline/fetch_page.py "<url>" --max-chars 30000

curl with a real browser User-Agent; prints the page as plain text. WebFetch gets a
consent/challenge shell from op.fi and agria.fi and returns near-nothing, which is what
triggers the confabulation above. `fetch_page.py` prints the real HTTP status and final
URL, so a redirect is something you can *see* rather than guess.

Its limit: it does not run JavaScript. If it returns HTTP 200 but only a few hundred
characters of text (op.fi does exactly this), the page is JS-rendered and you have NOT
read it. In that case use the JS-rendering fetch (added 18.7.2026):

    python pipeline/render_page.py "<url>" --max-chars 30000

It renders the page in an ordinary headless Chromium (no stealth, no UA spoofing) and
interacts with consent banners **decline-only** — it clicks "vain välttämättömät"/reject
if such a control exists and otherwise leaves the banner alone. If render_page.py ALSO
returns very little text, the site is challenge-walled for automated clients: that is
`"osittain"` plus an honest note — never `"ei"`, and never a guessed explanation.

## 🚫 Do NOT defeat bot protection, and do NOT click "accept cookies"

Learned 17.7.2026: an agent told to measure op.fi reported that it had driven Selenium,
*"bot protection active but bypassed"*, and *"accepted the cookie wall programmatically"*.
It got the data. **The extract was deleted unused, and so will any other obtained this way.**

Two separate lines, both firm:

1. **No evading bot detection.** If a site takes measures to keep automated clients out,
   that answer is "we could not measure it" — not a puzzle to solve. Whether our crawler
   *can* get in is not the same question as whether it *may*.
2. **No accepting consent on the user's behalf.** A cookie/consent banner is a legal
   agreement. Clicking "accept" programmatically consents to tracking for a real person
   who never asked for it. Decline non-essential if you interact with a banner at all.

**Rendering JavaScript is fine and is not a bypass** — an ordinary browser does it. What is
forbidden is *evasion* (spoofing to defeat a challenge, solving CAPTCHAs, working around a
block that is deliberately aimed at clients like us). Lighthouse renders op.fi perfectly
well without evading anything, which is exactly why op.fi's digital pillar has real numbers
while its transparency pillar does not.

If a site cannot be read within these limits, that is a **published gap**, not a failure.
Say so, score `"osittain"`, and let the page disclose it. A comparison built on data we
were not allowed to take is worth less than an honest hole.

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
