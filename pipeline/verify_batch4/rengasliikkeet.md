# rengasliikkeet — brand verification (batch 4)

Verified 21.7.2026 via `pipeline/fetch_page.py` (plain fetch, no `--js` needed for any
confirmed brand) + PRH opendata-ytj-api v3 + targeted web search for ownership claims.

## VAHVISTETUT

| slug | nimi | domain | y_tunnus | omistaja | JS | mittaus-URL |
|---|---|---|---|---|---|---|
| `vianor` | Vianor | vianor.fi | 1463013-4 (Vianor Oy) | Nokian Renkaat (Nokian Tyres) — confirmed via yritys.nokianrenkaat.fi listing Vianor as one of its own liiketoimintayksiköt | ei | https://www.vianor.fi/ |
| `euromaster` | Euromaster | euromaster.fi | 0711042-1 (Suomen Euromaster Oy) | Michelin — Euromaster is Michelin's own European tire-service subsidiary (est. Finland 1988 as Oy Distra Ab, ~61 own + 20+ partner points) | ei | https://www.euromaster.fi/ |
| `bestdrive` | BestDrive | bestdrive.fi | 1095378-8 (BestDrive Finland Oy) | Continental — page states outright: "BestDrive on kansainvälisesti tunnettu Continentalin tukema rengasliikeketju"; ~30 stores nationally | ei | https://bestdrive.fi/ |
| `motonet` | Motonet | motonet.fi | 0699457-9 (Motonet Oy) | Independent (suomalainen perheyritys) — primarily a retail hypermarket, but runs a genuine franchised national service network: "Motonet-korjaamot" (monimerkkikorjaamoketju, franchise entrepreneurs) + "Motonet Rengaspalvelut" incl. rengashotellit in multiple towns | ei | https://www.motonet.fi/palvelut/motonet-rengaspalvelut |
| `rengascenter` | RengasCenter | rengascenter.fi | 0782719-0 (Rengascenter Oy) | Independent, entrepreneur-owned — "Suomen suurin yrittäjäomisteinen rengasliikeketju", 60+ franchised stores; member of the TEN (Tyre European Network) European buying/marketing cooperative, not manufacturer-owned | ei | https://rengascenter.fi/ |
| `firststop` | First Stop | firststop.fi | 1806488-9 (Bridgestone Europe NV/SA, Suomen sivuliike) | Bridgestone — legally registered in Finland as a Bridgestone branch; own tietosuojaseloste names "First Stop Suomi / Bridgestone Europe NV/SA, Suomen sivuliike" directly | ei | https://www.firststop.fi/ |

All six Y-tunnus values confirmed live/registered against
`avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=<y>` (Vianor Oy, Suomen
Euromaster Oy and Rengascenter Oy: `status:"2"`, `tradeRegisterStatus:"1"`, i.e. active;
BestDrive Finland Oy and Motonet Oy: registered, active; Bridgestone's Finnish branch:
registered as a "Sivuliike" company form, active).

## KARSITUT

- **Rengasmaailma** — the candidate domain `www.rengasmaailma.fi` returns
  `DNS_PROBE_FINISHED_NXDOMAIN` (confirmed both via plain fetch and `--js` rendering — the
  domain does not resolve at all, it is not a bot-protection or JS-shell issue). Web search
  shows Rengasmaailma Oy was later rebranded **Rengasmarket**; fetching
  `rengasmarket.fi` itself resolves but redirects to `bestdrive.fi/wp-signup.php?new=…`
  (a decommissioned WordPress-multisite subdomain), and bestdrive.fi's own homepage banner
  states outright: *"Rengasmarket on nyt BestDrive"*. So the chain is not dead — it went
  through **two quiet rebrands** (Rengasmaailma → Rengasmarket → BestDrive) and now trades
  under BestDrive, which is listed above as its own confirmed brand. Publishing
  "Rengasmaailma" today would rank a name nobody can find; BestDrive replaces it.
- **Teboil** — confirmed to be a fuel-station chain first: "Huolto" is one of four listed
  station services (Autopesu, Huolto, Sähköauton lataus, Vuokraus) alongside food service.
  Its own huolto page does list "renkaanvaihdot" among huoltoasemien palvelut, but it is
  bundled as one line item inside general car maintenance (öljynvaihdot,
  ilmastointihuollot, määräaikaishuollot) at whichever franchised stations happen to offer
  huolto — the site itself says only some Teboil-asemat are "huoltoja tarjoavia" and nearly
  all stations are independently run by kauppiaat. There is no dedicated tire product line,
  no rengashotelli/tire-storage offering, and no tire e-commerce comparable to the six
  brands above. This is a fuel/convenience retailer with incidental tire-change service at
  some locations, not a national tire-service chain — cut per the brief's explicit
  instruction to verify this distinction.

## HUOMIOT

- **Manufacturer-ownership pattern, disclose prominently on-page**: of the six confirmed
  brands, four are owned outright by a tire manufacturer and compete against each other
  under different names while ultimately funding the same parent: Vianor = Nokian Renkaat,
  Euromaster = Michelin, BestDrive = Continental, First Stop = Bridgestone. Only Motonet
  (independent retailer/franchise) and RengasCenter (independent, entrepreneur-owned,
  TEN buying-cooperative member) are not manufacturer-owned. This mirrors the
  Budget=Avis / Nissen=Instrumentarium pattern already flagged in earlier batches — a
  reader comparing "5 competing chains" should know 4 of them are funded by tire makers
  competing for retail shelf space, not independent businesses.
- **No Nokian Renkaat duplicate found**: Nokian Renkaat (the manufacturer) does not run a
  separate consumer-facing service chain of its own beyond Vianor — confirmed via its
  corporate site (yritys.nokianrenkaat.fi), which lists Vianor as its retail/service
  business unit, alongside "Henkilöauton renkaat" and "Raskaat renkaat" (its own
  manufacturing lines, not competing retail brands). No double-count risk here.
- **First Stop's Nordic-only assumption was wrong** — the brief asked to verify whether
  First Stop even operates in Finland (vs. Sweden/Norway only). It does: firststop.fi is
  live, states Finnish operations began in 1998, and lists 60+ Finnish franchise stores.
  Do not cut it on that assumption.
- **Motonet is a genuine borderline case, included with a caveat** — its core business is
  retail (car parts/tools hypermarket), but it runs a real, separately branded national
  service network ("Motonet-korjaamot" + "Motonet Rengaspalvelut", including rengashotellit
  in multiple towns, run by franchise entrepreneurs — "Lähde Motonet-korjaamoyrittäjäksi").
  This clears the bar the brief set (a genuine tire-fitting/rengashotelli service chain,
  not just a shelf of tires for sale), but when scoring, measure the
  `motonet-rengaspalvelut` page specifically, not the general retail storefront, or the
  transparency criteria will effectively grade a hypermarket rather than a tire-service
  chain.
- **JS fetch was not needed for any of the six** — every confirmed brand's own site,
  yhteystiedot/sopimusehdot page, and Y-tunnus were readable with a plain
  `fetch_page.py` call (no `--js`). Flag this for the extraction agents so nobody wastes a
  render pass here.
- **SPA nav gotcha repeated**: vianor.fi, euromaster.fi and rengascenter.fi all 404 on
  guessed deep paths (e.g. `/yhteystiedot` on vianor.fi 404s; the real path is
  `/vianor/yhteystiedot/`). The fix that worked every time: fetch the front page with
  `--raw --max-chars 200000+` (their footers are far down the DOM and get silently cut off
  at lower max-chars) and grep real `href=` values, then follow those — never guess a path.
- **Six confirmed is within the 5–9 target**; no swap-in category needed.
