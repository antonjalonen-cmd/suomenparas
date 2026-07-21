# suoratoistopalvelut — brändivarmistus (BATCH 5)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py`:llä (curl ensin; `--js` käytetty kun curl
palautti dynaamisen/tyhjän hintataulukon — merkitty per rivi) + PRH:n YTJ v3 -rajapinta
(`avoindata.prh.fi/opendata-ytj-api/v3/companies`, businessId- tai nimihaulla) suomalaisille
yhtiöille. Kaikki yhdeksän tehtävänannon ehdokasta (Netflix, Disney+, Max/HBO Max, Viaplay,
Ruutu+, MTV Katsomo, Prime Video, Apple TV+, SkyShowtime) löytyivät elossa, suomeksi ja
euromääräisin hinnoin omalta sivultaan — yhtään ei tarvinnut karsia. Tämä on kategorian
tavoitehaarukan (5–9) yläpäässä; ei täytetty listaa, kaikki yhdeksän läpäisivät itsenäisesti.

## VAHVISTETUT (9)

| slug | nimi | domain | y_tunnus | omistaja | JS | mittaus-URL |
|---|---|---|---|---|---|---|
| `netflix` | Netflix | netflix.com/fi | Ei — globaali, ei suomalaista Y-tunnusta | **Netflix International B.V.** (Alankomaat) — vahvistettu suoraan omilta käyttöehdoilta: "Netflix-palvelun tarjoaa Netflix International B.V." Emoyhtiö Netflix, Inc. (Yhdysvallat, pörssiyhtiö). | Ei — curl palautti täyden suomenkielisen leipätekstin (4 309 merkkiä) suoraan, hinnat mukana | https://www.netflix.com/fi/ |
| `disneyplus` | Disney+ | disneyplus.com/fi-fi | Ei — globaali, ei suomalaista Y-tunnusta | **The Walt Disney Company** (Yhdysvallat, pörssiyhtiö). Oma tietosuojasivu: "tietojesi rekisterinpitäjä on jokin Walt Disney -yritysryhmän jäsen" — tarkkaa EU/ETA-laskutusyhtiötä (esim. tietty Disney-tytäryhtiö Isossa-Britanniassa tai Alankomaissa) ei saatu täsmennettyä tällä haulla, ks. HUOMIOT. | Ei — curl palautti täyden suomenkielisen sisällön hintoineen suoraan (8 268 merkkiä) | https://www.disneyplus.com/fi-fi |
| `hbomax` | HBO Max | hbomax.com (huom: max.com/fi/en ohjautuu tänne, ks. HUOMIOT) | Ei — globaali, ei suomalaista Y-tunnusta | **Warner Bros. Discovery, Inc.** (Yhdysvallat, pörssiyhtiö) | Ei — curl palautti täyden suomenkielisen sisällön hintoineen suoraan (15 158 merkkiä osoitteessa /fi/fi) | https://www.hbomax.com/fi/fi |
| `viaplay` | Viaplay | viaplay.fi | Ei — ruotsalainen, ei suomalaista Y-tunnusta | **Viaplay Group AB (publ)** — Nasdaq Tukholma -listattu; Vivendin/Canal+ Groupin (yhdessä PPF:n kanssa) omistusosuus n. 29 % (kasvoi tammikuussa 2024); strategia keskitetty ydinmarkkinoihin (Pohjoismaat + Alankomaat) vuoden 2023 rakenneuudistuksen jälkeen. Ks. HUOMIOT (Suomen nykytila). | Ei — curl palautti täyden suomenkielisen sisällön hintoineen suoraan (8 885 merkkiä) | https://www.viaplay.fi/ |
| `ruutuplus` | Ruutu+ | ruutu.fi | **1515901-4** (Sanoma Media Finland Oy, PRH-vahvistettu — aputoiminimenä rekisteröity mm. "Ruutunelonen") | Sanoma Oyj (pörssiyhtiö, Nasdaq Helsinki) | **Kyllä** — curl palautti vain 74 merkkiä (JS-runko); `--js` palautti täyden sisällön (11 276 merkkiä etusivu, 12 723 merkkiä tilaussivu) | https://www.ruutu.fi/tilaa |
| `mtvkatsomo` | MTV Katsomo+ | mtv.fi | **1093944-1** (MTV Oy, PRH-vahvistettu — aputoiminimenä rekisteröity mm. "MTV Katsomo") | **MTV Oy siirtyi norjalaisen Schibstedin omistukseen (TV4 Median kautta) 1.7.2025** — aiempi omistaja oli ruotsalainen Telia Company AB. Ks. HUOMIOT (kriittinen, ei ollut tehtävänannon ennakko-oletuksissa). | **Kyllä** osalle sivuista — katsomo.fi ohjautuu mtv.fi:hin (1 125 merkkiä ilman JS:ää); /tuotteet-sivu vaati `--js`:n (22 814 merkkiä) hintavertailutaulukon näkemiseksi | https://www.mtv.fi/tuotteet |
| `primevideo` | Prime Video | primevideo.com | Ei — globaali, ei suomalaista Y-tunnusta | **Amazon.com, Inc.** (Yhdysvallat, pörssiyhtiö) | Ei — curl palautti täyden suomenkielisen sisällön hintoineen suoraan (3 382 merkkiä, kielivalikko sisälsi "Suomi") | https://www.primevideo.com/ |
| `appletv` | Apple TV (huom: rebrändätty "Apple TV+":stä pelkäksi "Apple TV":ksi, ks. HUOMIOT) | tv.apple.com/fi, apple.com/fi/apple-tv | Ei — globaali, ei suomalaista Y-tunnusta | **Apple Inc.** (Yhdysvallat, pörssiyhtiö) | Ei — tv.apple.com/fi palautti sisällön suoraan (10 739 merkkiä, tosin sarjakuvaukset englanniksi); apple.com/fi/apple-tv palautti täyden suomenkielisen markkinointisisällön (7 197 merkkiä) | https://www.apple.com/fi/apple-tv/ |
| `skyshowtime` | SkyShowtime | skyshowtime.com/fi | Ei — globaali yhteisyritys, ei suomalaista Y-tunnusta | **SkyShowtime Limited** — Comcast (Sky Limited/Sky-tavaramerkit) ja Paramount Global (Showtime Networks Inc. -tavaramerkit) 50/50-yhteisyritys, per oma copyright-teksti: "© 2022 SkyShowtime Limited. Kaikki SKY- ja SHOWTIME-tavaramerkit... ovat Sky Limitedin ja Showtime Networks Inc:n omaisuutta... Paramount Globalin, NBCUniversalin, Peacockin..." Tarkkaa rekisteröintimaata (Limited-pääte viittaa UK:hon) ei vahvistettu erillisellä yritysrekisterihaulla. | Ei — curl palautti täyden suomenkielisen sisällön hintoineen suoraan (13 423 merkkiä) | https://www.skyshowtime.com/fi |

## KARSITUT

Ei yhtään — kaikki yhdeksän tehtävänannon ehdokasta läpäisivät varmistuksen. Yksi
harkittu lisäys hylättiin rajaussyystä:

- **Yle Areena** — ei sisällytetty, vaikka on Suomen käytetyin suoratoistopalvelu.
  Yle Areena on Yleisradion (julkinen, lupamaksurahoitteinen) maksuton palvelu ilman
  tilausmaksua tai kaupallista hinnoittelua. Kategorian läpinäkyvyysmittari ("kerrotaanko
  hinta ennen kuin käyttäjä luovuttaa tietonsa") ei sovellu palveluun, jolla ei ole
  hintaa eikä kaupallista tilaussuhdetta — sama rajausperuste kuin KeePassin poisjättö
  `salasananhallintapalvelut`-kategoriasta (ks. sisarprojektin muistiinpanot). Editorial-
  huomio Antonille: jos julkisrahoitteinen vaihtoehto halutaan näkyville, se sopisi
  erilliseen huomiolaatikkoon, ei pisteytystaulukkoon.
- **Paramount+** — ei ole itsenäinen kuluttajatuote Suomessa; Paramount Globalin
  sisältö jaetaan Suomessa SkyShowtimen kautta (yhteisyritys Comcastin kanssa), ei
  erillisen Paramount+-sovelluksen/tilin kautta. Ei siis oma kilpailija tässä
  kategoriassa, sisältyy jo `skyshowtime`-riviin.

## HUOMIOT

- **KRIITTINEN — MTV Katsomo+:n omistaja vaihtui, ei ollut tehtävänannon
  ennakko-oletuksissa.** Tehtävänanto ei maininnut omistajaa, mutta yleistieto (myös
  tämän pipelinen aiemmat muistiinpanot) olettaisi Telia Companyn (Ruotsi). Web-haku
  vahvisti: **MTV Oy:n koko määräysvalta siirtyi norjalaiselle Schibstedille (TV4 Median
  kautta) 1.7.2025** — kauppa siis jo toteutunut, ei vireillä. Tämä on täsmälleen se
  hiljainen omistajanvaihdos, jota tämä pipeline on aiemmin löytänyt (Väre/Helen,
  Säästöpankki, nyt MTV/Schibsted) — PRH-Y-tunnus (1093944-1) pysyy samana omistajan
  vaihtuessa, koska kyse on osakekaupasta eikä yhtiön purkamisesta, joten pelkkä
  Y-tunnuksen pysyvyys ei riitä; omistus piti tarkistaa erikseen webistä. Julkaisusivulla
  MTV Katsomo+:n omistajaksi on merkittävä Schibsted, ei Telia.
- **HBO Max on brändätty Suomessa "HBO Max":ksi, ei "Max":ksi — max.com uudelleenohjaa.**
  Tehtävänannon ehdokaslistalla lukee "Max (HBO)", ja globaali domain on max.com, mutta
  `https://www.max.com/fi/en` ohjautui suoraan osoitteeseen `hbomax.com/fi/en`, ja sivun
  oma otsikko/sisältö käyttää läpensä nimeä "HBO Max" (ei koskaan pelkkää "Max"). Tämä
  vastaa Warner Bros. Discoveryn tunnettua päätöstä palauttaa Max-brändi takaisin
  "HBO Max" -nimeen useilla markkinoilla; Suomen sivusto vahvistaa tämän omalta
  sivultaan. Julkaisusivulla kannattaa käyttää nimeä "HBO Max", ei "Max", koska se on
  mitä yhtiö itse näyttää suomalaiselle kuluttajalle.
- **Apple TV+ on rebrändätty pelkäksi "Apple TV":ksi.** Sekä tv.apple.com/fi että
  apple.com/fi/apple-tv käyttävät johdonmukaisesti nimeä "Apple TV" — "+"-merkki on
  pudotettu koko sivustolta englanninkielisiä juridisia tekstejä lukuun ottamatta.
  Hinta 9,99 €/kk on sama kummallakin sivulla. tv.apple.com/fi-sivun ohjelmakuvaukset
  ja -nimet ovat pääosin englanniksi (esim. "New Episode Every Friday"), kun taas
  apple.com/fi/apple-tv-markkinointisivu on kokonaan suomeksi — kaksi eri astetta
  suomenkielisyyttä samalle tuotteelle riippuen mitatusta URL:sta. Mittaus-URL:ksi
  valittu jälkimmäinen, koska se on aidosti suomenkielinen.
- **Viaplayn nykytila Suomessa (tehtävänannon erikseen pyytämä tarkistus): elossa ja
  toimiva, ei kriisissä enää.** Oma sivusto (viaplay.fi) palautti täyden, toimivan
  tilaussivun neljällä pakettitasolla (8,99–37,99 €/kk perushinnat, urheilupaketti
  Total 37,99–45,99 €/kk). Web-haku vahvisti taustan: Viaplay Group kärsi vakavista
  taloudellisista vaikeuksista 2022–2023 (SEK 4 mrd pääomankorotus + SEK 14,6 mrd
  velkajärjestely marraskuussa 2023), veti liiketoimintansa pois useista markkinoista
  (mm. Baltiasta, Isosta-Britanniasta, Yhdysvalloista) ja keskittyi uudelleen
  ydinmarkkinoihinsa: Ruotsi, Norja, Tanska, **Suomi**, Islanti ja Alankomaat. Canal+
  (Vivendi) osti yhdessä PPF:n kanssa n. 29 % omistusosuuden 2023–2024. Vuoden 2026
  Q1/Q2-raportit kuvaavat yhtiön olevan "on track" vuoden 2026 taloustavoitteidensa
  suhteen. Suomi on siis edelleen aktiivinen, ei karsittu ydinmarkkina — tämä oli
  tarpeen vahvistaa nimenomaan koska tehtävänanto epäili tilannetta erikseen.
- **Disney+:n tarkkaa EU/ETA-laskutusyhtiötä ei saatu vahvistettua omalta sivulta.**
  Tilaussopimus-sivu (subscriber-agreement) latasi oletuksena tietosuojakäytännön eikä
  itse tilausehtoja, eikä toisella yrityksellä (haku "Star Entertainment" / "Walt Disney
  Company Limited") löytynyt suoraa vahvistusta. Merkitty omistajaksi konsernitasolla
  "The Walt Disney Company" — tarkempi EU-laskutusyhtiö jää auki tulevaa varmistusta
  varten, samaan tapaan kuin `salasananhallintapalvelut`-sisarprojektissa NordVPN/
  NordPass-yhteyden tarkka oikeushenkilö jäi Cloudflare-bottitarkistuksen taakse.
- **SkyShowtimen tarkkaa rekisteröintimaata ei vahvistettu erikseen.** Oma copyright-
  teksti nimeää oikeushenkilön "SkyShowtime Limited" (Limited-pääte viittaa
  todennäköisesti Isoon-Britanniaan, koska Sky on brittiläinen Comcast-tytäryhtiö),
  mutta virallista yritysrekisterihakua (esim. Companies House) ei tehty tässä
  varmistuksessa — julkaisusivulla riittää mainita "Comcast (Sky) / Paramount Global
  50/50-yhteisyritys", ei tarvitse väittää tarkkaa kotimaata ilman rekisterivahvistusta.
- **JS-vaatimus koskee kahta yhdeksästä.** Ruutu.fi ja MTV:n /tuotteet-sivu ovat
  molemmat client-side-renderöityjä (Sanoma/MTV Oy molemmat, kiintoisa yhteinen piirre
  suomalaisilla mediataloilla); loput seitsemän (Netflix, Disney+, HBO Max, Viaplay,
  Prime Video, Apple TV, SkyShowtime) palauttivat täyden sisällön hintoineen suoraan
  plain-curl-fetchillä.
- **Kaikki yhdeksän näyttävät hinnan suomeksi ja euroissa ilman tiliä tai maksutapaa.**
  Tämä on poikkeuksellisen vahva tulos kategorian 30 pisteen ydinkysymykselle ("kerrotaanko
  hinta ennen kuin käyttäjä luovuttaa tietonsa") — yhtään ei tarvinnut merkitä "osittain"
  tai "ei" pelkän hinnan näkyvyyden osalta tällä haulla. Muut läpinäkyvyyskriteerit
  (peruutusehdot, sitovat jaksot, kampanjahintojen jälkeinen normaalihinta) vaihtelevat
  selvästi — esim. Viaplayn 12 kk sitova tilaus ja Disney+:n/Apple TV:n kampanjahinnan
  jälkeinen korotus ovat pisteytysagenteille tärkeitä yksityiskohtia.
- **Omistuskeskittymä tässä kategoriassa on vähäisempi kuin virustorjuntaohjelmat-
  kategoriassa.** Yhdeksästä palvelusta kahdeksalla on eri, toisistaan riippumaton
  omistaja (Netflix, Disney, Warner Bros. Discovery, Viaplay Group, Sanoma, Schibsted,
  Amazon, Apple); vain SkyShowtime on kahden ison konsernin (Comcast/Paramount)
  yhteisyritys, joka on jo rakenteellisesti läpinäkyvä kahden brändin (Sky+Showtime)
  yhdistelmänä nimessään. Ei siis samanlaista "sama omistaja kolmessa rivissä"
  -tilannetta kuin Gen Digital tuottaa virustorjuntaohjelmat-kategoriassa.
