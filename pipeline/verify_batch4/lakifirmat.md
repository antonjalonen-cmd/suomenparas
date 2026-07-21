# Brändivarmistus — Lakifirmat (BATCH 4)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (curl; ei yhdellekään vahvistetulle tarvittu
`--js` — kaikki palauttivat täyden leipätekstin ilman JS-renderöintiä) + PRH:n YTJ v3
-rajapinta (`avoindata.prh.fi/opendata-ytj-api/v3/companies`), ensin nimihaulla, sitten aina
vahvistettu `businessId`-haulla. Kaikki lainaukset leipätekstistä, ei pelkästä otsikosta
(Risicum-opin mukaisesti).

**Rajaus:** kuluttajille valtakunnallisesti lakipalveluja tarjoavat toimijat, joilla on oma
suomenkielinen verkkosivusto — sekä perinteiset monitoimipisteiset asianajo-/lakiasiaintoimistot
että digitaaliset asiakirjapalvelut. Ydinkysymys: kerrotaanko hinta ennen yhteydenottoa?

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `aatos` | Aatos | aatos.app | 2901500-3 (Aatos Legal Technology Oy, ent. 0 Degrees Oy) — rekisterissä, ei endDate:a | Ei konsernitietoa löydetty; itsenäinen | Ei — curl palautti 6 180 merkkiä täyttä sisältöä | https://aatos.app/ |
| `lakitie` | Lakitie | lakitie.com | 3614565-8 (Lakitie Oy) — rekisteröity vasta 17.4.2026, rekisterissä. **Huom: sivuston footer väittää "2023–2026"** — palvelu on ilmeisesti toiminut toiminimenä/muussa muodossa ennen Oy:ksi yhtiöittämistä huhtikuussa 2026; ei vanhempaa Y-tunnusta löydetty samalle toimijalle | Ei konsernitietoa; hyvin nuori osakeyhtiö | Ei — curl palautti 4 858 merkkiä | https://www.lakitie.com/hinnasto |
| `diy-lakipalvelu` | DIY Lakipalvelu | diylakipalvelu.fi | 2835849-3 (DIY Lakipalvelu Oy) — rekisterissä | Pieni, henkilöomisteinen: sisällöstä vastaa varatuomari Tiina Tikka (PRH-osoite "c/o Tiina Tiikka", Tampere) | Ei — curl palautti 5 333 merkkiä | https://www.diylakipalvelu.fi/hinnasto |
| `lindblad` | Asianajotoimisto Lindblad & Co | lindblad.fi | 1608041-2 (Asianajotoimisto Lindblad & Co Oy, ent. Asianajotoimisto Lindblad Oy) — rekisterissä | Itsenäinen suomalainen asianajotoimisto; kansainvälinen ADVOC-referenssiverkosto (ei omistus) | Ei — curl palautti 8 528+ merkkiä eri sivuilta | https://lindblad.fi/ |
| `heikkila-co` | Lakiasiaintoimisto Heikkilä & Co | heikkilaco.fi | 1843393-9 (Lakiasiaintoimisto Heikkilä & Co HCO Oy, ent. **Asianajotoimisto** Heikkilä & Co Oy vuoteen 2024 asti) — rekisterissä | Itsenäinen | Ei — curl palautti 6 434 merkkiä | https://www.heikkilaco.fi/hinnasto/ |
| `minilex` | Minilex | minilex.fi | 2411251-7 (MINILEX OY, ent. Legal Europe Oy) — rekisterissä | Itsenäinen | Ei — curl palautti 20 218 merkkiä | https://www.minilex.fi/ |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Lexly | **Kuollut yhtiö.** PRH: Lexly Oy (Y-tunnus 2868190-1, ent. Frida Family Lawyers Oy/Frida Family Lawyers) on rekisterimerkinnältään "Lakannut" 22.12.2025. lexly.fi ei vastaa lainkaan (curl: HTTP 000, 0 merkkiä — domain ei resolvoi/palvele). Sama ansa kuin Risicum/Väre/Säästöpankki: elävältä näyttävä hakutulos (Trustpilot-arvostelut, vanhat uutiset) ei todista, että yhtiö on olemassa tänään. | PRH businessId=2868190-1: `registeredEntries` sisältää `{"type":"4","description":"Lakannut","registrationDate":"2025-12-22"}`; oma fetch: `HTTP 000` lexly.fi:lle |
| Docue / "Sopimustieto" | **Sama yhtiö, ja nyt puhtaasti B2B — ei kuluttajalle.** sopimustieto.fi ohjautuu automaattisesti osoitteeseen docue.com/fi-fi. PRH vahvistaa: Docue Technologies Oy:n (Y-tunnus 2724469-7) aputoiminimissä on "Suomen Sopimustieto". Docue.com:n leipäteksti on läpikotaisin B2B-sopimushallintaa ("Docueen luottavat jo tuhannet yritykset", asiakastarinat Hesburger/Inderes, "Yritysasiakkaille: support@docue.com") — ei kuluttajalle suunnattua asiakirjapalvelua kuten alkuperäinen ehdokaslista oletti. Kaksi eri karsintaperustetta samassa yhtiössä: (1) tuplabrändi, (2) väärä kohderyhmä. | fetch_page.py: `sopimustieto.fi` → final URL `docue.com/fi-fi`, leipäteksti B2B-sisältöä; websearch vahvisti Y-tunnuksen 2724469-7 aputoiminimen "Suomen Sopimustieto" |
| Fondia | **Ei kuluttajatarjontaa lainkaan.** Fondia.com:n oma teksti: "lakiosastopalvelua (LDaaS)... yritysasiakkaille"; "kaikenkokoisten yritysten... lakikumppani". Ei mainintaa yksityishenkilöistä tai kuluttajapalveluista millään sivulla. | fondia.com/fi/fi-sivuston sisältö (yritys-/startup-/lakiosastopalvelut, ei kuluttajasivua) |
| Asianajotoimisto Facta Oy (Tampere) | Vain 2 toimipistettä (Tampere, Valkeakoski) — ei täytä valtakunnallisuuden rajaa (vrt. autokatsastus-kategorian sääntö, ks. QUEUED_CATEGORIES.md). Liikevaihdolla mitattuna Suomen suurin asianajotoimisto ilman Helsingin-toimistoa, mutta maantieteellisesti Pirkanmaa-keskeinen. | Websearch + ePressi-tiedote: "toimipisteet Tampereella ja Valkeakoskella", ei muita kaupunkeja löytynyt |
| Asianajotoimisto Kontturi & Co Oy | 3 toimipistettä, kaikki Itä-Suomessa (Joensuu, Lappeenranta, Jyväskylä) — alueellinen ketju, ei valtakunnallinen. Lisäksi kuuluu OpusLex-verkostoon, joka on **itsenäisten asianajotoimistojen markkinointiyhteenliittymä**, ei yksi yhtiö — OpusLex-jäsenyyttä ei pidä sekoittaa omaan valtakunnalliseen ketjuun (sama ansa kuin franchise-verkostoissa: jäsentoimistot ovat oikeudellisesti ja taloudellisesti erillisiä). | Websearch: toimipisteet "Joensuu, Lappeenranta, Jyväskylä"; opuslex.fi listaa Kontturin yhtenä monista itsenäisistä jäsentoimistoista |
| Perunkirja.fi | Ei ole lakitoimisto vaan **hautaustoimiston sivutuote**: sivun oma teksti "Perunkirja.fi on Hautaustoimisto Humatin palvelu" (Hautaustoimisto Humat Oy). Yhden asiakirjan (perunkirjoitus, 249 €) niche-tuote, ei vertailukelpoinen laajuudeltaan Aatoksen/Lakitien/DIY Lakipalvelun kanssa, jotka tarjoavat useita asiakirjatyyppejä. Rajatapaus, karsittu kohderyhmän/toimialan epäselvyyden vuoksi. | perunkirja.fi leipäteksti: "Perunkirja.fi on Hautaustoimisto Humatin palvelu — yli 30 vuoden kokemus surutyön arjesta" |

## HUOMIOT

- **Asianajaja vs. lakimies -ero, tärkeä lukijalle:** "Asianajotoimisto" on suojattu nimitys —
  sen osakkaat/vetäjät ovat Suomen Asianajajaliiton valvomia asianajajia (asianajaja-tutkinto,
  kurinpitovalvonta, pakollinen vastuuvakuutus). "Lakiasiaintoimisto"/"lakipalvelu" voi tarjota
  identtisiä palveluita **lakimiehillä/juristeilla**, joilla on oikeustieteen tutkinto muttei
  asianajajan auktorisointia eikä Asianajajaliiton valvontaa. Tässä kategoriassa: Lindblad on
  aidosti "Asianajotoimisto" (bar-jäseniä). Heikkilä & Co **vaihtoi nimensä "Asianajotoimisto
  Heikkilä & Co Oy":stä "Lakiasiaintoimisto Heikkilä & Co HCO Oy":ksi 28.1.2024** (PRH-data) —
  muutos kertoo todennäköisesti valvontastatuksen/profiilin muutoksesta, ei pelkästä
  markkinointinimen vaihdosta. Aatos, Lakitie, DIY Lakipalvelu ja Minilex ovat kaikki
  lakimies-/teknologiayhtiöitä, eivät asianajotoimistoja. Tämä ero kannattaa näyttää sivulla
  omana sarakkeenaan, ei vain nimien perässä — kuluttaja ei muuten tiedä eroa.
- **Hinta-avoimuuden kirjo on kategorian ydin ja se vaihtelee valtavasti jo tässä kuudessa:**
  Lakitie näyttää kiinteät hinnat (38–89 €) suoraan etusivulla ilman minkäänlaista yhteydenottoa;
  DIY Lakipalvelu samoin (avaimet käteen 200 €); Aatos näyttää hinnat suoraan (79 €/v, 99 €/asiakirja,
  199–499 € erikoispalvelut); **Lindblad julkaisee kiinteät tuotehinnat** vastaavista asiakirjoista
  (esim. testamentti 600 € sis. alv, avioehto 600 €+87 € kulu) suoraan "Tuotepaketit"-sivuillaan,
  mutta CTA on silti "Ota yhteyttä ja kysy lisää"; **Heikkilä & Co julkaisee tuntihinnan haarukan**
  kuluttaja-asiakkaille (299–350 €/h sis. alv) hinnasto-sivullaan, muttei kiinteää kokonaishintaa;
  **Minilex** toimii osin liidipohjaisesti ("Pyydä tarjous" / "Juristiverkosto" -malli, ks. sama
  ansa kuin vakuutusvertailupalvelut-muistiossa) ja osin puhelinpalveluna (0600 12 450 —
  maksullinen numero, minuuttihinta yleensä pientä printtiä). Tämä antaa kategorialle aidon
  pisteytysjakauman ääripäästä toiseen ilman, että yhtään dataa tarvitsee vääristää.
- **Nuori Y-tunnus, ei syytä epäillä:** Lakitie Oy on rekisteröity osakeyhtiönä vasta 17.4.2026
  (kolme kuukautta ennen tätä varmistusta). Sivusto ja asiakasarvostelut ulottuvat vuoteen 2023
  asti, joten palvelu on todennäköisesti toiminut aiemmin toisessa yhtiömuodossa (esim.
  toiminimi) ennen Oy:ksi yhtiöittämistä — tämä ei ole PRH:n mukaan sama tapaus kuin "Lakiasiaintoimisto
  Lakitie Oy" (Y-tunnus 2375691-9), joka lakkasi jo 6.4.2020 ja on eri, irrallinen yhtiö samalla
  yleisnimellä. Rakentajan syytä mainita ikä sivulla läpinäkyvyyden vuoksi, mutta se ei ole peruste
  karsia.
- **Lindblad ei ole franchise:** lindblad.fi:n nav-valikossa on artikkeli "Franchising-sopimus",
  joka herätti epäilyn omasta franchise-rakenteesta. Sisältö osoittautui yleiseksi
  lakitietoartikkeliksi franchising-sopimuksista asiakkaille (SEO-sisältöä), ei kuvaukseksi
  Lindbladin omasta toimintamallista. Kaikki kuusi toimipistettä (Helsinki, Lappeenranta,
  Tampere, Mikkeli, Joensuu, Imatra) kuuluvat samaan Y-tunnukseen 1608041-2.
- **Kategoria jää tavoitteen (5–9) sisään mutta juuri ja juuri kuudessa** kahden todella
  vahvan ehdokkaan (Lexly, Docue-kuluttajatuote) kuollessa/paljastuessa vääräksi kohderyhmäksi
  tarkastuksessa — kannattaa merkitä sivulla, ettei "digitaaliset lakipalvelut" ollut yhtä
  runsas alaryhmä kuin ehdokaslista antoi olettaa.
- Ei yhtään yhteistä omistajaa/konsernia löytynyt näiden kuuden väliltä (toisin kuin
  esim. autokatsastus- tai pankit-kategorioissa) — kaikki kuusi ovat toisistaan riippumattomia
  yhtiöitä. Ei siis tarvita Effortia/A-Katsastus-tyyppistä omistusdisclaimeria tälle kuudelle.
