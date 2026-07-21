# Faktantarkistus A — neljä kategoriavoittajaa

Tarkistuspäivä: 2026-07-21
Menetelmä: `python pipeline/fetch_page.py "<url>" [--js] --max-chars N` jokaiselle lähdesivulle (ei evästeklikkauksia, ei bot-suojauksen ohitusta); Danske Bankin PDF ladattu erikseen `curl`illa ja luettu `pypdf`illä sivumäärän ja sisällön varmistamiseksi. Ei muokattu data/- tai pipeline/extracts/-tiedostoja.

---

## 1. Danske Bank — data/pankit.json (voittaja, score 83,4)

Lähteet uudelleenhaettu: `danskebank.fi/sinulle/paivittaispalvelut/tilit/danske-tili` (HTTP 200) ja `danskebank.fi/-/media/pdf/danske-bank/fi/fi/tuotteet/palveluhinnasto.pdf` (HTTP 200, ladattu ja luettu tekstinä).

**VAHVISTETTU:**
- "Julkinen 10-sivuinen palveluhinnasto-PDF" — PDF on yhä julkisesti ladattavissa ilman kirjautumista, HTTP 200, `pypdf` vahvistaa täsmälleen **10 sivua**. Ensimmäisellä sivulla lukee "Voimassa 23.6.2026 alkaen" ja "Y-tunnus 1078693-2" — täsmää julkaistuun sitaattiin.
- Käyttötilin kk-maksu 2,50 €: sivutekstissä yhä sanatarkasti "Paketin ulkopuolisista tai peruspankkipalveluun kuuluvasta tilistä veloitetaan 2,50 euroa kuukaudessa"; PDF:n sisällä tekstihaku löytää "Danske-tilin kuukausimaksu 2,50" ja "Debit kortti, Mastercard Debit kortin kuukausimaksu 3,30" — molemmat luvut täsmäävät julkaistuun dataan pilkulleen.
- "Hinnat ja ehdot" -osiossa sivulla on yhä linkit "Etuohjelman hinnasto", "Palveluhinnasto", "Tili- ja maksupalveluehdot", "Maksuja koskeva tietoasiakirja" — täsmää.
- Ei riippumatonta arviolähdettä, ei julkista sähköpostia (vain kirjautuneena) — molemmat yhä paikkansapitäviä havaintoja sivulla.

**POIKKEAMAT:** Ei löytynyt yhtään. Kaikki tarkistetut väitteet (10-sivuinen PDF, 2,50 €/kk, 3,30 €/kk kortti, Y-tunnus, voimassaolopäivä) pitivät paikkansa sanatarkasti.

Arvio: ei pisteitä muuttavaa poikkeamaa.

---

## 2. Amazed — data/pakohuoneet.json (voittaja, score 81,7, lisätty tänään)

Lähteet uudelleenhaettu (`--js` koska sivu on kevyt JS-render): `amazed.fi/hinnasto`, `amazed.fi/varaa`, `amazed.fi/pakohuoneet`.

**VAHVISTETTU:**
- Hintataulukko: 2 pelaajaa 105 €/ryhmä … 6 pelaajaa 165 €/ryhmä — täsmää julkaistuun "105–165 €" -väitteeseen täsmälleen.
- Alennukset: alle 10-vuotiaat lapset ilmaiseksi, opiskelijat 100 € (Kampin toimipiste, ma–to tietyt kellonajat) — molemmat yhä sivulla sanatarkasti.
- Maksutavat listattu (kortit, käteinen, MobilePay, laskutus +10 €, lahjakortti) — täsmää.
- Varauskalenteri: "Voit varata pelin seuraavalle päivälle klo 22.00 asti" — sanatarkka täsmäys julkaistuun väitteeseen.
- Kuusi peliä vaikeustasoineen: ALCHEMIA 4/5, TEETH 3.5/5, VOYAGE 3/5, MISSION 3.5/5, KGB 4/5, PELASTAKAA BENNY 4/5 — kaikki kuusi täsmäävät järjestyksessä ja vaikeustasoissa.
- TripAdvisor "488 reviews" — täsmää julkaistuun "488 arvostelua".
- Osoite Köydenpunojankatu 4a, 00180 Helsinki; aukiolo "Mon-Sat 11:00-17:00" — täsmää.
- Y-tunnus/VAT FI27164662 — täsmää.

**POIKKEAMAT:** Ei löytynyt yhtään.

Arvio: ei pisteitä muuttavaa poikkeamaa.

---

## 3. Koti Puhtaaksi — data/siivouspalvelut.json (voittaja, score 88,4 — koko sivuston ennätys)

Lähteet uudelleenhaettu: `kotipuhtaaksi.fi/hinnasto/`, `kotipuhtaaksi.fi/yhteystiedot/`, `kotipuhtaaksi.fi/`.

**VAHVISTETTU (kaikki läpinäkyvyyspilarin 100/100-väitteet):**
- Alueellinen tuntihinnasto: Uusimaa 67,80 €/h (säänn.) ja 72,00 €/h (kerta); Tampere/Turku-alue 62,80 €/h ja 68,00 €/h; Oulu/Jyväskylä-alue 58,80 €/h ja 64,00 €/h — täsmää julkaistuun "67,80–72,00 / 62,80–68,00 / 58,80–64,00 €/h" -väitteeseen euron sentilleen.
- Kotitalousvähennys: sivu sanoo sanatarkasti "kotitalousvähennyskelpoinen (35%, vuonna 2026)" ja "Asiakkaanamme voit antaa meille suostumuksen, jonka jälkeen ilmoitamme kotitalousvähennykset puolestasi" — molemmat sanatarkkoja täsmäyksiä.
- Verkkotilaus: "Tilaa tästä ›" -painikkeet jokaisella hintarivillä + "Tai tilaa suoraan verkkokaupasta" -linkki — täsmää.
- Toimialueiden kaupunkimäärät täsmäävät **tarkalleen** julkaistuihin lukuihin: Uusimaa 11 kaupunkia (Helsinki, Espoo, Vantaa, Kauniainen, Kirkkonummi, Kerava, Tuusula, Järvenpää, Hyvinkää, Nurmijärvi, Sipoo), Tampereen seutu 7 (+Hämeenkyrö), Turun seutu 8, Oulun seutu 6, Jyväskylän seutu 3 — kaikki viisi lukua pitivät paikkansa yksi yhteen.
- Toimistojen aukioloajat: Tampere ja Helsinki 8–15 (ma–pe), muut sovitusti — täsmää.
- Riippumaton arviolähde: etusivulla sanatarkasti "Yli 1800 asiakasarvion jälkeen asiakastyytyväisyytemme keskiarvo on 4,8/5." — sanatarkka täsmäys.
- Y-tunnus 2395527-2, puhelin 050 1209 (ma-pe 7-13), Live Chat (ma-pe 7-17) — täsmäävät footerissa.

**POIKKEAMAT:** Ei löytynyt yhtään sisällöllistä poikkeamaa. (Sivulla itsellään pieni sisäinen epäjohdonmukaisuus: footerissa esiintyy kahdessa eri kohdassa hieman eri chat-/puhelinaikoja, esim. "Live Chat (ma-pe 7-17:30)" vs. "(ma-pe 7-17)" ja "050 1209 (MA-PE 7-16)" vs. "(ma-pe 7-13)" — tämä on sivuston oma epäjohdonmukaisuus, ei ekstraktiovirhe, eikä vaikuta pisteytykseen koska mittari on kyllä/ei-tyyppinen "aukioloajat esillä".)

Arvio: ei pisteitä muuttavaa poikkeamaa. Tämä oli tarkistetuista neljästä perusteellisin täsmäys — jokainen numero (hinnat, %-osuus, kaupunkimäärät) piti paikkansa.

---

## 4. Aatos — data/lakifirmat.json (voittaja, score 83,1)

Lähteet uudelleenhaettu: `aatos.app/`, `aatos.app/kayttoehdot/`, `aatos.app/testamentti/`.

**VAHVISTETTU:**
- Hinnat: Aatos Huoleton 79 €/vuosi, perunkirjoitus 399 €, avioero 199 €, yksittäinen asiakirja 99 € — kaikki neljä täsmäävät sanatarkasti etusivulla.
- Arvosana "4.4 /5.0" näkyy yhä ylätunnisteessa — täsmää.
- "Vahvistettu"-leimatut asiakasarviot ★-symbolein — useita löytyy edelleen etusivulta, täsmää.
- Y-tunnus 2901500-3 footerissa — täsmää.
- Yhteystiedot/käyttöehdot: "Aatos.app-verkkopalveluun voi olla yhteydessä sähköpostin tai chatin välityksellä... Puhelinnumero on +358 45 2709 010" — sanatarkka täsmäys käyttöehtojen kohdasta 8; puhelinnumero ei ole esillä etusivulla (vain käyttöehdoissa) — täsmää julkaistun mittarin sanamuotoon.
- Chat-maininta "Lakitiimin tuki heti chatissa tai sähköpostitse" — löytyy yhä etusivun ylätunnisteesta sanatarkasti.
- Pätevyys: testamentti-sivulla yhä "Perintöoikeuden asiantuntijoiden laatima ja tarkastama palvelu... (OTM Tatu Mäenpää ja Sophie Pöllänen)" — sanatarkka täsmäys; edelleen vain OTM-tutkinto mainittu, ei asianajaja/varatuomari-nimikettä — täsmää "Osittain"-arvion perusteluun.
- 30 päivän tyytyväisyystakuu käyttöehdoissa — täsmää.

**POIKKEAMAT:** Ei löytynyt yhtään.

Arvio: ei pisteitä muuttavaa poikkeamaa.

---

## Yhteenveto

Tarkistettiin 4 kategoriavoittajaa, yhteensä n. 35 yksittäistä väitettä (hinnat, prosenttiosuudet, sivumäärät, kaupunkilistat, sitaatit, arvosanat). **Poikkeamia löytyi 0.** Kaikki neljä voittajan dataa piti paikkansa nykyisillä live-sivuilla, mukaan lukien tarkat eurosummat, PDF:n sivumäärä ja voimassaolopäivä, kaupunkien lukumäärät toimialueittain, ja sanatarkat asiakaspalautesitaatit. Yhtään havaintoa ei tarvinnut korjata tai merkitä epäluotettavaksi.
