# Suomen Paras — yhden kategorian rakentaminen (autopilot-ohjekirja)

Tämä on TÄYDELLINEN resepti yhden uuden vertailukategorian lisäämiseen
suomenparas.antonjalonen.fi-sivustolle. Jarvisin `suomenparas`-tikki seuraa tätä
kirjaimellisesti. Repo: `C:\Users\anton\Downloads\Claude Site\suomenparas`
(oma git-repo, GitHub Pages + Cloudflare Worker -proxy).

**Yksi tikki = yksi kategoria, alusta loppuun, portteineen. Ei oikoteitä.**

## 0. Valinta

Avaa `pipeline/CATEGORY_BACKLOG.md`. Ota ylin rivi jonka tila on `[ ]` (vapaa).
Merkitse se heti `[~]` (työn alla) ja committaa, jotta rinnakkainen sessio ei
ota samaa. Jos jono on tyhjä: tutki webistä 5 uutta elinkelpoista kategoriaa
(kansallisia ketjuja/yhtiöitä ≥6 kpl), lisää ne jonoon kandidaatteineen,
committaa, ja lopeta tikki riviin `SUOMENPARAS BACKLOG: lisätty 5 kategoriaa`.

## 1. Brändien varmistus (webhaku + curl)

Etsi 7–10 suomalaista yhtiötä/ketjua jotka palvelevat kuluttajia
valtakunnallisesti tai monessa kaupungissa, kullakin OMA elävä sivusto.

- Brändit kuolevat hiljaa: tarkista fuusiot, konkurssit ja markkinapoistumiset
  viimeisen 2 vuoden ajalta (webhaku). Esim. Väre→Helen, Lendo poistui Suomesta.
- JOKAINEN domain: `curl -sI --ssl-no-revoke -L -A "Mozilla/5.0" https://domain.fi`
  JA etusivun teksti: elävä domain + otsikko ≠ myy. Jos leipäteksti sanoo
  "ei uusia asiakkaita/nostoja" tms. → HYLKÄÄ ja dokumentoi (Risicum-oppi).
- Viralliset nimet PRH v3:sta: `https://avoindata.prh.fi/opendata-ytj-api/v3/companies?name=<nimi>`
  Y-tunnusta EI KOSKAAN keksitä.
- Saman omistajan brändit merkitään (kerromme omistajuuden sivulla).
- Alle 6 varmistettua yhtiötä = kategoria ei elinkelpoinen → merkitse jonoon
  `[s]` + syy, ota seuraava rivi.

## 2. Konfiguraatio (4 tiedostoa + brief)

1. `pipeline/companies.py` — uusi avain COMPANIES-sanakirjaan. Poissuljetut
   dokumentoidaan kommentteina (kuolleet brändit, duplikaatit, syyt).
2. `pipeline/vertical_meta.py` — otsikko, kuvaus, slug-metat samaan tyyliin
   kuin olemassa olevat.
3. `pipeline/score_rules.py` — TRANSPARENCY-painot kategorialle, summa
   TASAN 100 (assert kaatuu muuten). Globaalit digipalvelut käyttävät
   `omistaja_kerrottu` y_tunnuksen sijaan (vpn-käytäntö).
4. `pipeline/targets.txt` — JUURIDOMAINIT (syvät polut antavat Lighthousessa
   ERRORED_DOCUMENT_REQUEST).
5. `pipeline/BRIEF_<vertical>.md` — ekstraktio-ohje agenteille samalla
   rakenteella kuin muut BRIEF-tiedostot.

## 3. Lighthouse

`python pipeline/run_lighthouse.py <vertical>` — aja lokaalisti (npx).
**PORTTI: laske lokista "OK perf" -rivit — määrän pitää olla = yhtiöiden
määrä. Exit-koodi 0 EI riitä: verkkokatko kaataa ajon hiljaa.** Puuttuvat
ajetaan uudestaan yksitellen.

## 4. Ekstraktio (1 agentti / yhtiö)

Haiku-tason agentti per yhtiö → `pipeline/extracts/<vertical>/<slug>.json`.
Agentin ohjeet (pakolliset):
- Hae sivut `python pipeline/fetch_page.py <url>` (selain-UA), JS-renderöidyt
  sivut `--js`-lipulla (op.fi-tyyppiset). Ei koskaan arvattuja polkuja:
  hae --raw, greppaa hrefit, seuraa OIKEITA navigaatiolinkkejä.
- Jokainen extract sisältää `fetched_ok`-listan oikeasti haetuista URL:eista.
- Botti-esto/evästemuuri = mittausaukko ("ei mitattavissa"), EI "ei ole".
  Muureja EI kierretä.
- Evidenssi: suora sitaatti sivulta, tai HAVAINTO:-etuliite jos rakenteellinen
  havainto ilman sitaattia.
- ÄLÄ KOSKAAN kuvaa toisen yhtiön sivua väärän yhtiön tiedostoon (agentit ovat
  keksineet "uudelleenohjauksia" kilpailijalle kun haku epäonnistui — portti
  nappaa tämän).

## 5. PORTTI: check_extracts

`python pipeline/check_extracts.py <vertical>` — PAKOLLINEN, nollavirhettä.
Tyypilliset korjaukset: typotetut avaimet nimetään uudelleen arvot säilyttäen;
ohut ryömintä (2 URL:ää + pelkkiä "ei") = epäilyttävä → uusi ryömintä oikeilla
navigaatiolinkeillä.

## 6. Sertifioinnit

`pipeline/certs/<vertical>.json` = `{"slug": [{"nimi": "...", "lahde": "..."}]}`.
Karsintalinja (EI poikkeuksia):
- ✓ LASKETAAN: ISO-sertifioinnit, SOC 2, nimetyt julkaistut auditoinnit,
  WWF Green Office, Ekokompassi, EKOenergia, Avainlippu/Design from Finland,
  Luotettava Kumppani, alan liittojen jäsenyydet, asianajotoimisto-nimike,
  AV-TEST-tyyppiset sertifiointiohjelmat.
- ✗ EI: lakisääteiset toimiluvat (Fiva/Traficom/Valvira/LKV), allekirjoitus-
  sitoumukset (UN PRI, Global Compact, SBTi), ESG-luokitukset (EcoVadis/CDP/
  MSCI), asiakastyytyväisyysmerkit, markkinointipalkinnot, "standardin
  mukainen" (≠ sertifioitu), vuokranantajan kiinteistösertifikaatit,
  alkuperätakuut, oma vastuullisuusraportti.

## 7. Opas

`pipeline/opas/<vertical>.json` = `{johdanto, huomioita[], vinkit[], ukk[{q,a}]}`.
Faktat notes/extract-datasta — EI keksittyjä tilastoja. Suomeksi, ei
ajatusviivoja, ei malli-/työkalunimiä.

## 8. Build

`pipeline/build_vertical.py`:
- Lisää uusi vertical `MEASURED`-sanakirjaan TÄMÄN PÄIVÄN päivämäärällä.
  Vanhoja päivämääriä EI muuteta koskaan.
- Aja `python pipeline/build_vertical.py <vertical>` ja **varmista että lokissa
  on "wrote data/<vertical>.json" — domain-vahti kaataa buildin hiljaa** (jos
  kaksi yhtiötä jakaa domainin oikeasti, lisää SAME_COMPANY-poikkeus).

## 9. Sivusto + julkaisu

1. `python gen_site.py` — sivumäärän pitää kasvaa. Uusi kategoria tulee
   automaattisesti Kaikki kategoriat -sivulle ja hakuindeksiin.
   **HAETUIMMAT-listaan (etusivun 6 kärkeä) EI kosketa** (Antonin päätös).
2. `git add -A && git commit` (suomenkielinen viesti) `&& git pull --rebase && git push`
3. Varmista live: `curl -s --ssl-no-revoke https://suomenparas.antonjalonen.fi/<vertical>/`
   palauttaa sivun jossa yhtiöiden nimet näkyvät.
4. Merkitse backlog-rivi `[x] ... — julkaistu <pvm>` ja committaa.

## 10. Raportointi

Tikin yhteenvetorivi TÄSMÄLLEEN:
`SUOMENPARAS KATEGORIA: <vertical> https://suomenparas.antonjalonen.fi/<vertical>/`

Jos jokin portti ei mene läpi eikä korjaannu tämän tikin sisällä: älä julkaise
mitään puolivalmista — jätä työpuu puhtaaksi (git checkout/clean uudet
konfiguraatiorivit saa jättää committoituna vain jos build meni läpi) ja
raportoi `SUOMENPARAS BLOKATTU: <syy>`. Seuraava tikki yrittää uudelleen.

## Kovat säännöt (kaikissa vaiheissa)

- Julkinen copy: suomeksi, ei ajatusviivoja (generaattori riisuu ne, mutta älä
  kirjoita niitä), ei AI-malli- tai työkalunimiä ("data" riittää).
- Y-tunnuksia ei keksitä. Sitaatteja ei keksitä. "En löytänyt" ≠ "ei ole".
- Sijoitusta ei voi ostaa -periaate näkyy joka sivulla automaattisesti.
- Ei koskaan rahankäyttöä, ei uusia työkaluja/palveluita joihin pitäisi
  rekisteröityä.
