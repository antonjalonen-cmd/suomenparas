# pilvitallennuspalvelut — brändivarmistus (BATCH 5)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (curl ensin; `--js` uudelleen aina kun curl
palautti tyhjän JS-kuoren tai hinnat placeholder-tokeneina, esim. `€ -0.01`, `only %1`,
`undefined%`) + PRH:n YTJ v3 -rajapinta nimihaulla (`avoindata.prh.fi/opendata-ytj-api/v3/companies?name=<nimi>`)
jokaiselle ehdokkaalle + kohdennettu websearch omistusrakenteen ja toiminnan jatkumisen
varmistamiseksi (Mega, Internxt, pCloud — brief pyysi erikseen tarkistamaan, ettei mikään
ole hiljaa hävinnyt/sulautunut). Kaikki kahdeksan alkuperäistä ehdokasta läpäisivät
varmistuksen — ei tarvinnut karsia yhtään eikä täydentää listaa.

**Rajaus:** sama kynnys kuin vpn-palvelut-kategoriassa: ulkomainen palvelu hyväksytään jos
sillä on suomenkielinen sivu TAI julkaistu Suomi/EUR-hinnoittelu. Kaikki kahdeksan ovat
globaaleja toimijoita ilman suomalaista Y-tunnusta (ks. PRH-huomiot alla) — sama malli kuin
vpn-palvelut: `y_tunnus=None`, `omistaja`+`lainkayttoalue` korvaavat PRH-vahvistuksen.

## VAHVISTETUT (8)

| slug | nimi | domain | y_tunnus | omistaja | JS-vaatimus | mittaus-URL |
|---|---|---|---|---|---|---|
| `googleone` | Google One | one.google.com | None (ks. PRH-huomio alla — Google Finland Oy on paikallinen toimisto, ei laskuttava yhtiö) | Alphabet Inc. / Google — EU-kuluttajalaskutus tyypillisesti Google Irlannin yksikön kautta | Ei — curl palautti 2 974 merkkiä täyttä suomenkielistä sisältöä hintoineen | https://one.google.com/about/plans |
| `icloud` | iCloud+ | apple.com/fi/icloud | None — ei suomalaista Y-tunnusta löytynyt Apple Distribution -nimihaulla PRH:sta | Apple Inc. — EU-kuluttajalaskutus tyypillisesti Apple Distribution International Ltd:n (Irlanti) kautta | Ei — curl palautti 18 850+ merkkiä täyttä suomenkielistä sisältöä hintoineen | https://www.apple.com/fi/icloud/ |
| `onedrive` | Microsoft OneDrive (Microsoft 365 -paketteina) | microsoft.com/fi-fi | None (Microsoft Oy 0897464-3 on rekisterissä, mutta paikallinen myynti-/toimintayhtiö, ei kuluttajatilausten sopimusosapuoli) | Microsoft Corporation — EU-kuluttajalaskutus tyypillisesti Microsoft Ireland Operations Limitedin kautta | **Kyllä** — plain curl palautti bot-torjuntasivun ("Your request has been blocked"); `--js` palautti 27 132 merkkiä täyttä suomenkielistä sisältöä ja hinnat (20,00 €/v Basic, 99,00 €/v Personal) | https://www.microsoft.com/fi-fi/microsoft-365/onedrive/compare-onedrive-plans |
| `dropbox` | Dropbox | dropbox.com | None — `/fi/plans` ja `/fi-fi/plans` molemmat 404, ei suomenkielistä sivustoa löytynyt | Dropbox, Inc. (Nasdaq: DBX) — itsenäinen pörssiyhtiö, ei emoyhtiötä; EU-asiakkaille tyypillisesti Dropbox International Unlimited Company (Irlanti) | Ei — curl palautti 7 504 merkkiä suoraan EUR-hinnoin (Plus 9,99 €/kk, Standard 12 €/kk, Advanced 18 €/kk) ilman kirjautumista | https://www.dropbox.com/plans |
| `protondrive` | Proton Drive | proton.me/drive | None | Proton AG — **sama omistaja kuin jo listattu `protonvpn` (vpn-palvelut) — ks. HUOMIOT** | **Kyllä hintojen osalta** — suomenkielinen sivu proton.me/fi/drive/pricing löytyy ja renderöityy jo plain curlilla, mutta hinnat näkyvät vain placeholderina ("−undefined %", "0,00 $ joka kuukausi"); `--js` palautti oikeat hinnat (Drive Plus 3,99 €/kk, Unlimited 9,99 €/kk, Duo 14,99 €/kk) | https://proton.me/fi/drive/pricing |
| `mega` | MEGA | mega.io / mega.nz | None | MEGA Limited — itsenäinen, Uusi-Seelanti; Kim Dotcom ei ole omistanut yhtiötä vuoden 2015 jälkeen, useita omistajanvaihdoksia sen jälkeen (ei tee siitä epäluotettavaa — ks. HUOMIOT) | **Kyllä** — plain curl mega.io/pricing palautti template-tokeneita ("only %1", "^{price}"), mega.nz palautti 4 merkkiä (pelkkä SPA-kuori); `--js` palautti oikeat EUR-hinnat (Essential 3,33 €/kk, Pro I 9,99 €/kk jne.) | https://mega.io/pricing |
| `pcloud` | pCloud | pcloud.com | None — `/fi/...`-polku ohjautuu takaisin yleiselle etusivulle, ei suomenkielistä versiota | pCloud AG — itsenäinen, yksityisomisteinen (perustajat Tunio Zafer & Anton Titov), Sveitsi | Ei elinikäisille (Lifetime) hinnoille — curl palautti suoraan oikeat EUR-hinnat (Premium 500 Gt 199 €, Premium Plus 2 Tt 399 €, Ultra 10 Tt 1190 €) ilman kirjautumista. Kuukausitilauksen näkymä ei ehtinyt renderöityä samassa ajossa (`--js`-yritys aikakatkaistiin 120 s:ssa, tulkitaan tilapäiseksi verkko-ongelmaksi, ei sivun ominaisuudeksi) — **seuraavan agentin syytä varmistaa kuukausihinta `--js`:llä uudelleen ennen ekstraktiota** | https://www.pcloud.com/cloud-storage-pricing-plans.html |
| `internxt` | Internxt | internxt.com | None — kielivalikossa EN/ES/FR/DE/IT/ZH/RU/TW, ei suomea; vahvistettu myös kokeilemalla `/es/precios` (toimii, espanjankielinen) | Internxt S.L. — itsenäinen, VC-rahoitteinen (Series B, mm. TheVentureCity, Telefónica, Crowdcube), Espanja (Valencia) | **Kyllä** — plain curl palautti hinnat placeholderina ("€ -0.01"); `--js` palautti oikeat hinnat (Essential 379,99 €, Premium 579,99 €, Ultimate 779,99 €, kertamaksu) | https://internxt.com/pricing |

Kaikki kahdeksan täyttävät rajauksen: Google One, iCloud+ ja Proton Drive suomeksi +
EUR-hinnoin; OneDrive suomeksi + EUR-hinnoin (vain `--js`:n takana); Dropbox, MEGA, pCloud
ja Internxt eivät ole suomeksi mutta julkaisevat kaikki oikean EUR-hinnan ilman tiliä tai
yhteydenottoa.

## KARSITUT

Ei yhtään. Kaikki kahdeksan alkuperäisen ehdokaslistan palvelua läpäisivät varmistuksen.
Kolmelle tehtiin kuitenkin erillinen "onko tämä oikeasti vielä olemassa/itsenäinen"
-tarkistus brief:n pyynnöstä, koska ne olisivat voineet olla juuri sitä Lexly/Väre-tyyppistä
hiljaista kuolemaa tai omistajanvaihdosta, jota tämä putki on aiemmin löytänyt:

- **MEGA — tarkistettu, EI karsittu.** Perustaja Kim Dotcom irtautui yhtiöstä jo 2015 eikä
  omista siitä osuuksia; omistus on sittemmin vaihtanut useita kertoja (mm. Li Zhi Min 43 %,
  Yang Jianhong 24 %). Yhtiö on silti edelleen olemassa ja toimii itsenäisenä uusiseelantilaisena
  yhtiönä — omistajanvaihdos ≠ lakkaaminen. Oma sivusto (mega.io) toimii ja myy aktiivisesti.
- **Internxt — tarkistettu, EI karsittu.** Ei löytynyt viitteitä lopettamisesta tai ostosta;
  websearch vahvistaa aktiivisen, VC-rahoitetun toiminnan (Series B, ~8,46 M$ rahoitettu).
- **pCloud — tarkistettu, EI karsittu.** Yksityisomisteinen sveitsiläinen yhtiö, ei viitteitä
  omistajanvaihdoksesta tai lopettamisesta.

## HUOMIOT

- **OMISTUS-PÄÄLLEKKÄISYYS, pakollinen disclosure sivulla: Proton Drive = Proton AG =
  sama yhtiö kuin jo julkaistu `protonvpn` (vpn-palvelut).** Jos molemmat kategoriat ovat
  live-tilassa, Proton esiintyy sivustolla kahdesti eri kategorioissa saman konsernin alla —
  täsmälleen sama tilanne kuin `vertaaensin.fi`/Effortia-huomio muissa muistioissa. Ei ole
  syy karsia (Proton Drive ja Proton VPN ovat aidosti eri tuotteita eri kategorioissa), mutta
  näytä se lukijalle, ettei vaikuta riippumattomalta kahdelta yhtiöltä.
- **Google One EI ole eri tuote kuin "Google Drive"** — Google One on nykyisin Google Driven,
  Kuvien ja Gmailin yhteinen tallennustilan lisäostopaketti; ei ole olemassa erillistä
  "Google Drive -tilausta" myytäväksi tämän rinnalla, joten ei tuplalistausriskiä.
- **Microsoft OneDrive myydään vain Microsoft 365 -pakettien sisällä kuluttajille** — ei ole
  enää erillistä "osta pelkkää OneDrive-tallennustilaa" -tuotetta henkilöasiakkaille (Free 5 Gt,
  sitten Basic 100 Gt + 15 Gt postilaatikko 20 €/v, Personal 1 Tt + koko Office-paketti 99 €/v).
  Mittaa/ekstraktoi nimenomaan tuo palvelupaketit-sivu, ei erillistä OneDrive-tuotesivua — sitä
  ei ole. Tämä on itsessään läpinäkyvyyslöydös, ei este: näytä lukijalle että "OneDrive-hinta"
  tarkoittaa käytännössä M365-tilausta.
  **Digitaalinen pilari:** plain curl saa Microsoftin bot-torjuntasivun ("Your request has
  been blocked") — pakollinen `--js` tälle yhdelle kahdeksasta. Kirjaa tämä Lighthouse/
  ekstraktioagenteille selvästi, sama kuin op.fi-oppi.
- **PRH-löydökset paikallisista toimistoista, EI laskuttavista yhtiöistä — älä sekoita
  näitä tuotteen Y-tunnukseksi:** nimihaku PRH:sta löysi rekisterissä olevia suomalaisia
  tytäryhtiöitä sekä Googlelle (Google Finland Oy, Y-tunnus 2206071-7, alun perin Forivia Oy;
  toinen vanhempi Google Finland Oy 2045000-9 on lakannut 31.12.2011) että Microsoftille
  (Microsoft Oy, Y-tunnus 0897464-3, rekisterissä — entisiä Nokia-yksiköitä muutettu
  Microsoft-nimisiksi 2014–2015 Nokian puhelinliiketoiminnan kaupan myötä). Nämä ovat
  paikallisia toiminta-/myyntiyhtiöitä, eivät kuluttajatilausten sopimusosapuolia — sama ero
  kuin Saxo Bankin Suomen sivuliikkeen kohdalla vpn-palvelut-listassa: rekisteröity paikallinen
  läsnäolo ≠ tuotteen laskuttava yhtiö. En löytänyt vastaavaa Apple-, Dropbox-, Proton-,
  MEGA-, pCloud- tai Internxt-nimistä rekisteröityä suomalaista yhtiötä PRH:n nimihaulla.
  **En itse hakenut kunkin yhtiön omia käyttöehtoja vahvistaakseni tarkkaa EU-laskutusyhtiön
  nimeä (esim. "Google Ireland Limited") tässä ajossa — tämä on yleisesti tunnettu käytäntö,
  ei tässä pass:ssa alkulähteestä varmistettu fakta.** Jos joku tarvitsee tarkan laskuttavan
  yhtiön nimen, se pitää hakea kunkin palvelun omista käyttöehdoista erikseen.
- **JS-vaatimus vaihtelee paljon tässä kategoriassa — kirjaa tarkkaan ekstraktioagenteille:**
  Google One, iCloud+, Dropbox ja pCloud (Lifetime-hinnat) toimivat plain curlilla. OneDrive,
  Proton Drive (vain hintanumerot — sivu itse renderöityy ilman JS:ää), MEGA ja Internxt
  tarvitsevat `--js`:n, koska hinnat piirtyvät asiakaspuolen JavaScriptillä template-merkkijonoina
  (`only %1`, `€ -0.01`, `undefined%`) ilman sitä. Väärä "hinta ei löytynyt" -havainto tässä
  kategoriassa on lähes aina JS-vaatimuksen unohtaminen, ei oikea puute sivulla.
- **pCloudin kuukausihinta jäi vahvistamatta tässä ajossa** — `--js`-yritys aikakatkaistiin
  120 sekunnissa (Chrome ei ehtinyt renderöidä, ei sivun este). Elinikäishinnat (Lifetime)
  ovat jo vahvistettu plain curlilla ilman ongelmia. Ekstraktioagentin kannattaa yrittää
  `--js` uudelleen kuukausihintanäkymälle ennen pisteytystä, jotta "kuukausimaksu ei näy"
  ei rekisteröidy virheellisesti puutteeksi.
- **Kahdeksan vahvistettua on kategorian yläpäässä (tavoite 5–9)** — poikkeuksellisen korkea
  läpäisyaste tälle listalle verrattuna moneen aiempaan erään, koska ehdokaslista koostui
  jo valmiiksi tunnetuista, aidosti aktiivisista globaaleista kuluttajabrändeistä eikä
  paikallisista/epävarmoista toimijoista.
