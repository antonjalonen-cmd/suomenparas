# Brändivarmistus — Muuttopalvelut (BATCH 4)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py`:llä (curl; ei yhdellekään vahvistetulle
tarvinnut `--js` — kaikki palauttivat luettavaa leipätekstiä ilman JS-renderöintiä) +
PRH:n avoindata-ytj-api v3 -rajapinta (nimihaku → businessId-vahvistus, tradeRegisterStatus
tarkistettu jokaiselle). WebSearch käytetty ehdokkaiden löytämiseen ja toimipisteverkoston
kartoittamiseen; jokainen löydös vahvistettu yhtiön omalta sivulta ja/tai PRH:sta ennen
hyväksymistä.

**Tulos: 4 vahvistettua — ALLE 5–9 TAVOITTEEN.** Sama poikkeus kuin `autokatsastus`
(batch 3, myös 4 vahvistettua): Suomen muuttopalveluala koostuu käytännössä sadoista
paikallisista/alueellisista perheyrityksistä (pääkaupunkiseutu, Uusimaa, Pirkanmaa jne.)
ja vain neljästä yhtiöstä, joilla on aidosti oma, useamman kaupungin kattava
toimipisteverkosto tai valtakunnallinen kuljetuskapasiteetti. Rakentajan/Antonin
päätettävissä: julkaista 4 yhtiön kategoria dokumentoidulla poikkeuksella, vai jättää
`muuttopalvelut` rakentamatta tällä kierroksella.

## VAHVISTETUT (4)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `niemi-palvelut` | Niemi Palvelut (Muuttopalvelu Niemi) | niemi.fi | 1944860-6 (Niemi Palvelut Oy, ent. Muuttopalvelu Niemi Oy) | Ei konsernitietoa löydetty — itsenäinen yhtiö | Ei — curl palautti 17 282 merkkiä | https://niemi.fi/ |
| `muuttohaukat` | Muuttohaukat | muuttohaukat.com | 0887272-7 (Muuttohaukat Oy, ent. Muuttohaukat Ky) | Ei konsernitietoa löydetty — itsenäinen yhtiö | Ei — curl palautti 13 831 merkkiä | https://muuttohaukat.com/ |
| `suomen-muuttofirma` | Suomen Muuttofirma | muuttofirma.fi | 2292440-7 (Suomen Muuttofirma Oy) | Ei konsernitietoa löydetty — itsenäinen yhtiö | Ei — curl palautti 8 063 merkkiä | https://muuttofirma.fi/ |
| `victor-ek` | Victor Ek | victorek.fi | 0215408-9 (Oy Victor Ek Ab) | Perheomisteinen vuodesta 1885/1955 lähtien (yhtiön oma historia-artikkeli: "remains under family ownership") | Ei — curl palautti 7 203 merkkiä (en-sivu) | https://www.victorek.fi/ |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Kotimuutto | Ei ole itsenäinen yhtiö — `kotimuutto.fi` uudelleenohjautuu osoitteeseen `muuttovelhot.fi/kotimuutot/`, joka on vain yksi palvelusivu Muuttovelhot Oy:n sivustolla. Muuttovelhot Oy:n oma etusivun otsikko on "Muuttopalvelu **pääkaupunkiseudulla**" — pelkästään pääkaupunkiseutu, ei valtakunnallinen. | fetch_page.py: `kotimuutto.fi` → HTTP 200, final URL `muuttovelhot.fi/kotimuutot/`; `www.muuttovelhot.fi` etusivun koko sisältö = "Muuttopalvelu pääkaupunkiseudulla \| MuuttoVelhot" (48 merkkiä); PRH 0721408-7 Muuttovelhot Oy (ent. Laatikkovuokraamo Boxi Oy) |
| Muuttopalvelu Grundell | **Hiljainen fuusio + nimenvaihto 2.6.2026**: PRH:n mukaan Y-tunnus 1087288-1 on nykyään "Martela Palvelut Oy" — "Muuttopalvelu Grundell Oy" -nimi päättyi 2.6.2026. Rekisteröity toimiala vaihtui muuttopalveluista ("Muuttopalvelut") koneiden/laitteiden vuokraukseen, ja PRH:n rekisteröity verkko-osoite on nyt martela.com, ei enää grundell.fi. `grundell.fi` ei enää vastaa (HTTP 000). Martelan oma "Muutot ja muutostyöt" -sivu on puhtaasti B2B-toimistokalustepalvelu (tilalaskelma, työympäristösuunnittelu, kalusteiden hallinta) — ei kuluttajan kotimuuttoa. | PRH businessId=1087288-1: nimet-listassa "Martela Palvelut Oy" (rekisteröity 2026-06-02), "Muuttopalvelu Grundell Oy" endDate 2026-06-02; website-kenttä "martela.com"; `www.grundell.fi` HTTP 000; `martela.com/fi/palvelut/toteutuspalvelut/muuttopalvelut` sisältö puhtaasti kalustekonsernin B2B-palveluista |
| Muuttopalvelu.com (MLP Moving Oy) | **Kuollut yhtiö, elävä domain** — täsmälleen Risicum-tyyppinen tapaus. PRH: businessId 3315942-1, tradeRegisterStatus "4" (Lakannut), endDate 2024-12-03, ALV-velvollisuus päättyi jo 2024-07-08. Silti muuttopalvelu.com on elossa ja sivun footerissa lukee "© 2026 MLP Moving Oy" — mainostaa yhtiötä, joka on lakannut yli puolitoista vuotta sitten. | PRH businessId=3315942-1: `"tradeRegisterStatus":"4"`, `"status":"2"`, `"endDate":"2024-12-03"`; muuttopalvelu.com footer "© 2026 MLP Moving Oy" |
| Pakumuutto.com (LogoTex Oy) | Omistava yhtiö LogoTex Oy:n **rekisteröity päätoimiala on "Muu tekstiilien tukkukauppa"**, ei muuttopalvelut. Sama yhtiö pyörittää samanaikaisesti useita ohuita markkinointibrändi-sivustoja (pakumuutto.com, kodinsiivous.fi, muuttohinta.fi, t-paitoja.com) yhden pienen toiminimen alla — ei osoita omaa, riippumatonta muuttoyritystä vaan liidinvälitysmallia. | PRH nimihaku "Logotex": mainBusinessLine "46412 Muu tekstiilien tukkukauppa"; aputoiminimet "LogoTex/pakumuutto.com", "LogoTex/kodinsiivous.fi", "LogoTex/t-paitoja.com", "www.muuttohinta.fi" kaikki saman Y-tunnuksen (1929259-2) alla |
| HRS | Ehdokaslistan "HRS" ei vastannut mitään löydettävissä olevaa muuttopalveluyritystä — PRH-nimihaku (51 osumaa) ei tuottanut yhtään muuttoalan yhtiötä, eikä hakukaan löytänyt vastaavaa brändiä. Todennäköisesti ehdokaslistan virheellinen/vanhentunut nimi. | PRH-nimihaku "HRS": ei muuttopalvelu-toimialan osumia; WebSearch ei tuottanut muuttoyritystä nimeltä HRS |
| Muuttoapu.fi | Uudelleenohjautuu osoitteeseen pakukuljetus.fi ("Suomen Pakukuljetus") — pieni pakettiauto+kuljettaja-palvelu, joka toimii Helsingin, Tampereen ja Turun alueilla yhdellä puhelinnumerolla per kaupunki. Ei omaa toimipisteverkostoa eikä osoita valtakunnallista laajuutta samalla tavalla kuin vahvistetut neljä. | fetch_page.py: `muuttoapu.fi` → HTTP 200, final URL `pakukuljetus.fi`; sivun sisältö kuvaa yhden pakettiauton palvelua kolmella alueella |
| Muuttopojat | Aluetoimija Keski-/Etelä-/Pohjois-Pohjanmaalla (Kokkola, Pietarsaari, Vaasa, Ylivieska, Oulu, Raahe, Haapajärvi) — tekee muuttoja "tarvittaessa koko Suomen alueella", mutta toimipisteverkosto on selkeästi yhden maakuntaryhmän kokoinen, ei valtakunnallinen kuten Niemi/Muuttohaukat | WebSearch: "Päätoimialueena on Etelä-, Pohjois- ja Keski-Pohjanmaa" |
| Muuttokarhut | Toimii vain Helsingissä, Espoossa ja Vantaalla (perustettu Porvoossa 1997) — pääkaupunkiseudun yhtiö, ei valtakunnallinen | WebSearch: "operate in the greater Helsinki area... Helsinki, Espoo, and Vantaa" |
| Muuttomiehet (K Niskanen Oy) | Toimii Espoossa, Kauniaisissa, Helsingissä, Vantaalla, Kirkkonummella, Porvoossa, Nummelassa ja muualla Uudellamaalla — Uusimaa-alueen yhtiö, ei valtakunnallinen toimipisteverkosto | WebSearch: "Espoo, Kauniainen, Helsinki, Vantaa, Kirkkonummi, Porvoo, Nummela and other parts of Uusimaa" |
| Suomimuutto Oy | Toimii pääasiassa Helsingin, Espoon, Vantaan ja muun eteläisen Suomen alueella "sekä laajemmin sopimuksen mukaan" — Etelä-Suomi-painotteinen, ei erillistä toimipisteverkostoa muualla maassa | WebSearch: "primarily operates in the Helsinki, Espoo, Vantaa and greater capital region areas, as well as all of southern Finland" |
| Muuttopalvelu Pietilä Ky | Paikallinen Oulun alueen yhtiö (Ii, Haukipudas, Kello, Kiiminki, Ylikiiminki, Oulunsalo, Hailuoto, Kempele, Liminka, Tyrnävä, Muhos, Utajärvi) — tekee pitkän matkan kuljetuksia koko Suomeen, mutta ilman omaa toimipisteverkostoa muualla; yksi Ky ilman sisaryhtiöitä | WebSearch: paikallinen toimialue rajattu Oulun ympäristökuntiin |
| Santa Fe Relocation / Crown Relocations | Kansainvälisiä yritys-/expat-muuttoja hoitavia relokaatioyhtiöitä (B2B/expatriaatti-asiakkuudet, yritysten kautta), ei suomalaiselle kuluttajalle suunnattu oma-aloitteinen kotimuuttopalvelu samalla tavalla kuin vahvistetut neljä | WebSearch: "Global Mobility company", "60 years of experience and a global network spanning 38 countries" — ei viitteitä suoraan kuluttajamarkkinointiin Suomessa |

## HUOMIOT

- **Kategoria jää 4:ään, ei 5–9:ään.** Sama tilanne kuin `autokatsastus`-kategoriassa
  (batch 3): laajan haun jälkeen (PRH-nimihaut, WebSearch, yhtiöiden omat sivut) löytyi
  vain neljä yhtiötä, joilla on aidosti oma, useamman kaupungin toimipisteverkosto TAI
  todistetusti valtakunnallinen palvelukapasiteetti. Kymmeniä muita "muuttopalvelu"-nimisiä
  sivustoja löytyi, mutta jokainen niistä osoittautui joko yhden kaupungin/maakunnan
  toimijaksi, saman yhtiön toiseksi domainiksi tai (kahdessa tapauksessa) lakanneeksi
  yhtiöksi jonka domain on jäänyt elämään.
- **Kaksi erillistä "kuollut yhtiö, elävä domain" -löydöstä samassa kategoriassa**
  (Muuttopalvelu.com/MLP Moving Oy ja osittain Muuttopalvelu Grundell/Martela) —
  poikkeuksellisen paljon tälle yhdelle kategorialle. Kumpikin vahvistettu PRH:n
  `tradeRegisterStatus`/`endDate`-kentistä, ei pelkästä domain-käyttäytymisestä.
- **Victor Ek** on kategorian vanhin yhtiö (yhtiön oma historia-artikkeli mainitsee
  "over the years" ja perheomistuksen; PRH-rekisteröinti 1978, mutta yhtiön oma markkinointi
  väittää 140 vuoden/vuoden 1885 historian — todennäköisesti yhtiön toiminta on alkanut
  ennen nykyistä yhtiömuotoa). Rekisteröity päätoimiala PRH:ssa on edelleen
  "Meri- ja rannikkovesiliikenteen tavarankuljetus" (merikuljetus), ei muuttopalvelut —
  yhtiö on historiallisesti laajentunut satamahuolinnasta muuttopalveluun ja tarjoaa
  edelleen molempia. Tämä kannattaa näyttää sivulla avoimesti (ei ole ongelma, mutta
  yllättävä yksityiskohta).
- **Niemi Palvelut** on ainoa ehdokas, jolla on selkeä 9 kaupungin toimipisteverkosto
  (Helsinki, Tampere, Turku, Oulu, Jyväskylä, Lahti, Kuopio, Vaasa, Rovaniemi) — vahvin
  kandidaatti kategorian "valtakunnallisin" -otsikolle jos kategoria rakennetaan.
- **Suomen Muuttofirma**: vain 2 fyysistä toimipistettä (Joensuu, Kuopio), mutta 100+
  muuton ammattilaista, 25+ muuttoautoa, 4500+ muuttoa/vuosi ja valtakunnallinen
  palvelunumero — hyväksytty samalla logiikalla kuin Green Motion autovuokraamot-
  kategoriassa (batch 3): pieni toimipisteverkosto mutta todistetusti laaja, aidosti
  koko-Suomen kattava operatiivinen kapasiteetti.
- Ei yhtään yhtiötä tarvinnut `--js`-renderöintiä — kaikki kuusi vahvistus-hakua
  onnistuivat tavallisella curl-hausta (fetch_page.py oletusasetuksin).
