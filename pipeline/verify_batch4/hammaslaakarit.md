# hammaslaakarit — brand verification (batch 4)

Mittauspäivä tälle varmistukselle: 21.7.2026. Kaikki haut `pipeline/fetch_page.py`:llä
(curl ensin; `--js` käytetty vain kun curl palautti Next.js/React-skeletonin — merkitty
per rivi alla). Y-tunnukset vahvistettu PRH:n avoindata-ytj-api v3:sta (businessId- tai
name-haulla). Ei yhtään keksittyä Y-tunnusta. Mehiläinen Oy:n ja Terveystalo Oyj:n
Y-tunnukset olivat jo PRH-vahvistettuja `yksityislaakarit`-kategoriassa (batch 3,
18.7.2026) — tässä vain varmistettiin, että sama oikeushenkilö pyörittää edelleen
kansallista, kuluttajalle avointa hammashoitoketjua.

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus | omistaja | JS | mittaus-URL |
|---|---|---|---|---|---|---|
| `oral` | Oral Hammaslääkärit | oral.fi | 2863321-3 (Oral Hammaslääkärit Oy; entinen nimi Colosseum Dental Finland Oy 2017–2022, PRH-vahvistettu) | **Colosseum Dental Group** (Euroopan suurin suunterveyspalveluiden tarjoaja, n. 620 klinikkaa 11 maassa), jonka omistaa sveitsiläinen **Jacobs Holding AG** (Jacobs-säätiön sijoitusyhtiö). **EI Mehiläinen** — ks. HUOMIOT. | Ei — curl palautti 3 479 merkkiä täyttä leipätekstiä ilman JS:ää | https://www.oral.fi/ |
| `mehilainen` | Hammas Mehiläinen | mehilainen.fi/hammas-mehilainen | 1927556-5 (Mehiläinen Oy — jo PRH-vahvistettu batch 3:ssa) | Mehiläinen Oy — pääomasijoittajaomisteinen konserni. Hammashoito on Mehiläinen Oy:n oma palvelulinja ("Hammas Mehiläinen"), ei erillinen tytäryhtiö (sivun copyright: "© Mehiläinen"). | **Kyllä** — curl palautti vain Next.js-skeleton-shellin (n. 594 000 merkkiä minifioitua koodia, 0 hyötysisältöä); `--js` palautti 29 638 merkkiä oikeaa sisältöä hinnastoineen | https://www.mehilainen.fi/hammas-mehilainen |
| `terveystalo` | Suun Terveystalo | terveystalo.com | 2575979-3 (Terveystalo Oyj — jo PRH-vahvistettu batch 3:ssa) | Pörssiyhtiö (Nasdaq Helsinki) | Ei — curl palautti 21 970 merkkiä täyttä sisältöä | https://www.terveystalo.com/fi/Palvelut/Hammashoito |
| `plusterveys` | PlusTerveys | plusterveys.fi | 3265145-7 (PlusTerveys Hammasklinikat Oy, PRH: rekisterissä, toimiala 86230 "Hammaslääkäripalvelut" — täsmää suoraan) | PlusTerveys Ryhmä Oy (emoyhtiö) — sivun oman ilmoituksen mukaan "ammattilaisen omistama": pääomistajina yhtiössä työskentelevät hammaslääketieteen/lääketieteen/hallinnon ammattilaiset; 28.5.2026 uutinen mainitsee kasvustrategian rahoittajina Voland Partners ja Varma | Ei — curl palautti 3 035 merkkiä täyttä sisältöä | https://www.plusterveys.fi/ |
| `hammashohde` | Hammas Hohde | hammashohde.fi | 2339589-3 (Hammas Hohde Oy; entinen nimi Gasellin Hammaslääkärit Oy 2010–2020, PRH-vahvistettu) | Pääomistajana pääomasijoittaja **Sentica Partners** (n. 60 %) ja perustaja, erikoishammaslääkäri Ville Pesonen (n. 20 %). **HUOM — kesken oleva yrityskauppa:** Terveystalo allekirjoitti 23.12.2025 sopimuksen ostaa koko Hohde Group (Hammas Hohde Oy + Loisto Laboratoriot Oy) 88 milj. eurolla; KKV:n kuuleminen päättyi 14.4.2026, lopullista hyväksymispäätöstä ei löytynyt tällä haulla. Ks. HUOMIOT. | Ei — curl palautti 2 776 merkkiä täyttä sisältöä | https://www.hammashohde.fi/ |
| `coronaria` | Coronaria Hammasklinikka | coronaria.fi/hammasklinikka | 2207193-4 (Coronaria Hammasklinikka Oy; entinen nimi Hammasklinikka Dent Oy 2013–2018, PRH: rekisterissä, toimiala 86230) | Coronaria Oy, jonka suurin omistaja on **Cor Group** (n. 82 % yhdessä johdon/avainhenkilöiden kanssa); Mandatum Asset Managementin kasvupääomatuotteet n. 18 %. Cor Groupilla on myös omistusosuus Silmäasemasta (optikot, batch 3) — ei sama yhtiö, mutta sama emo-sijoittaja kahdessa eri kategoriassa. | Ei — curl palautti 11 607 merkkiä täyttä sisältöä | https://www.coronaria.fi/hammasklinikka/ |

**Kokoerot toimipistemäärissä (leipätekstistä poimittu, ei ulkoista lähdettä):** Oral 65
hammaslääkäriasemaa + 5 hammaslaboratoriota lähes 40 paikkakunnalla; Hammas Hohde 33
hammaslääkäriasemaa 24 paikkakunnalla (Ivalosta Turkuun — aidosti valtakunnallinen);
PlusTerveys n. 80 hammasklinikkaa n. 60 paikkakunnalla; Coronaria Hammasklinikka 180
suun terveyden asiantuntijaa (ei ilmoitettu toimipistemäärää etusivulla); Mehiläinen ja
Terveystalo eivät ilmoittaneet hammashoidon toimipistemäärää erikseen tällä haulla.

## KARSITUT

- **Aava** — ei tarjoa hammashoitoa lainkaan. Etusivun palveluluettelo (Korva-, nenä- ja
  kurkkutaudit, Lasten terveys, Leikkaukset ja sairaala, Naisen terveys, Rokotukset,
  Tuki- ja liikuntaelimet, Vatsa ja suolisto, Yleislääkäri- ja päivystyspalvelut) ei
  sisällä hammashoitoa, eikä koko etusivun raakateksti (grep) sisältänyt sanaa "hammas"
  missään muodossa. Aava on `yksityislaakarit`-kategoriassa (batch 3) mutta ei kuulu
  tähän kategoriaan.
- **Pihlajalinna** — samasta syystä ei tarjoa hammashoitoa: etusivun raakatekstissä ei
  yhtään "hammas"-osumaa. Pihlajalinna keskittyy yleis-/erikoislääkäripalveluihin,
  ortopediaan, kuntoutukseen — ei suun terveyteen. Tarkistettu, koska on
  `yksityislaakarit`-kategorian jäsen ja aiemmin ehdotettu tähän kategoriaan.

## HUOMIOT

- **Väärä ennakko-oletus korjattu: Oral EI ole Mehiläisen omistuksessa.** Tehtävänannossa
  pyydettiin varmistamaan väite "Oral Hammaslääkärit acquired by Mehiläinen" — tämä on
  **virheellinen**. PRH:n mukaan Oral Hammaslääkärit Oy:n edellinen nimi oli "Colosseum
  Dental Finland Oy" (2017–2022), ja CapMan Buyout myi omistuksensa Oralista Colosseum
  Dental Groupille 2017 (CapManin oma tiedote). Colosseum Dental Groupin omistaa
  sveitsiläinen Jacobs Holding AG. Oral ja Mehiläinen ovat siis kaksi täysin
  **riippumatonta** kilpailijaa eri omistajilla — ei sama konserni, ei disclaimeria
  tarvita niiden välillä. Tämä on täsmälleen se konfabulaatioriski, josta
  QUEUED_CATEGORIES.md varoittaa: ennakko-oletusta ei saa hyväksyä ilman todistetta,
  ja tässä tapauksessa todiste (PRH nimihistoria + CapMan/Colosseum-lehdistötiedotteet)
  osoitti ennakko-oletuksen vääräksi.
- **Toinen Terveystalo-konsolidaatiotapaus, sama kaava kuin Silmäasema/optikot
  (batch 3).** Terveystalo allekirjoitti 23.12.2025 sopimuksen ostaa koko Hohde Group
  (Hammas Hohde Oy + Loisto Laboratoriot Oy) 88 milj. eurolla. KKV:n kuuleminen päättyi
  14.4.2026 (diaarinumero KKV/433/14.00.10/2026); tällä haulla ei löytynyt vahvistettua
  lopullista hyväksymispäätöstä, eikä hammashohde.fi ole (21.7.2026) vaihtanut brändiä —
  sivusto toimii yhä itsenäisenä "Hammas Hohde Oy" -brändinä omalla Y-tunnuksellaan.
  Julkaistaan siis kahtena erillisenä, itsenäisenä kilpailijana, mutta **kesken oleva
  omistajanvaihdos on pakko avata sivulla** — jos kauppa toteutuu, Terveystalo omistaisi
  2/6 tämän kategorian brändeistä (itsensä + Hohteen), mikä pitää päivittää heti kun
  KKV-päätös vahvistuu. Tarkista uudelleen jokaisella ajolla ennen batch 5:tä.
- **Cor Group -ristikkäisomistus kategorioiden välillä.** Coronaria Hammasklinikan
  emoyhtiö Coronaria Oy:n suurin omistaja on Cor Group, jolla on myös omistusosuus
  Silmäasemasta (`optikot`, batch 3, joka itse on parhaillaan Terveystalon ostettavana —
  ks. batch 3:n muistiinpanot). Ei sama yhtiö kuin Coronaria Hammasklinikka, mutta sama
  sijoittajaperhe esiintyy kahdessa eri Suomen Paras -kategoriassa. Ei vaadi karsintaa,
  mutta kannattaa mainita sivun "omistus"-osiossa läpinäkyvyyden vuoksi.
- **Mehiläinen vaatii JS-renderöinnin.** `mehilainen.fi` on Next.js-sovellus; curl näki
  vain latausanimaatioiden skeleton-CSS:n ilman hyötysisältöä. `--js`-tila
  (headless Chrome, ei evästeklikkauksia, ei bot-kiertoa) toimi suoraan ja palautti
  täyden hinnaston. Muut viisi brändiä (Oral, Terveystalo, PlusTerveys, Hammas Hohde,
  Coronaria) palauttivat täyden leipätekstin pelkällä curlilla.
- **6 vahvistettua, alarajan 5–9 sisällä.** Hammaslääkärimarkkina on kilpailluin
  batch 3/4:n kategorioista tähän mennessä — kansallisia, aidosti kuluttajalle avoimia
  ketjuja löytyi kuusi kappaletta ilman että jouduttiin venyttämään "kansallinen"-
  määritelmää (Hammas Hohdekin kattaa Ivalosta Turkuun, ei vain pääkaupunkiseutua).
  Ei tarvinnut swapata muita kategorioita listalle.
- **Ei tarkistettu tyhjentävästi:** pienempiä alueellisia hammaslääkäriketjuja (esim.
  yksittäisten kaupunkien "Hammaslääkärikeskus X" -brändit, joita PRH:n nimihaut Oralin
  ja Hohteen alla paljastivat kymmenittäin toimipistetasolla) ei käyty läpi yksitellen,
  koska ne ovat jo osa jotain kuudesta ketjusta eivätkä itsenäisiä kilpailijoita.
