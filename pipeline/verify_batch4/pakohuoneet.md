# Brändivarmistus — Pakohuoneet (BATCH 4, ennakkotarkistus)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (curl; ei yhdellekään tarvittu `--js` —
kaikki sivustot palauttivat leipätekstin suoraan) + PRH YTJ v3 -rajapinta
(`avoindata.prh.fi/opendata-ytj-api/v3/companies`, businessId-haku, tradeRegisterStatus
tarkistettu joka yhtiöltä). Lisäksi ristiintarkistus karkaa.fi:n (pakohuoneiden
hakukoneen) aluelistauksella JS-renderöitynä, ettei mitään ilmeistä ketjua puuttunut.

## VASTAUS KRIITTISEEN KYSYMYKSEEN

Suomessa on **karkeasti ~100 itsenäistä pakohuoneyritystä**, mutta aidosti
**monikaupunkisia ketjuja omalla Y-tunnuksella löytyi vain 3**, ja niidenkin lisäksi
2 rajatapausta (täsmälleen 2 kaupunkia). Ala on rakenteellisesti paikallinen — tämä
vahvistaa QUEUED_CATEGORIES.md:n paikallisuusvaroituksen. **Kategoria kannattaa
rakentaa vain pienempänä (3, korkeintaan 5 rivillä rajatapaukset mukaan lukien) tai
jättää rakentamatta tällä kierroksella** — päätös Antonille.

## VAHVISTETUT — aidosti monikaupunkiset (3)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | kaupungit (montako ja mitkä) | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|---|
| `truescape` | Truescape (+ Mysteeri-brändi) | truescape.fi / mysteeri.com | 3016295-9 (Truescape Oy, rek. 2019, elossa, ei companySituations-merkintöjä) | Truescape Oy, Kirkkonummi (Jorvas) | **9**: Helsinki, Espoo, Turku, Vaasa (Truescape-brändi) + Tampere, Jyväskylä, Kuopio, Pori, Mikkeli (Mysteeri-brändi, sama Y-tunnus syyskuusta 2019) | Ei — curl toimii molemmilla domaineilla | https://www.truescape.fi/en |
| `labyrinth-games` | Labyrinth Games Room Escape | lgames.fi | 2659780-2 (Labyrinth Games Room Escape Oy, rek. 2015, elossa) | Itsenäinen, perustajaomistuksessa (yksi Suomen vanhimmista pakohuoneyrityksistä) | **4**: Helsinki, Tampere, Turku, Oulu (Oulun toimipiste avattu n. vuosi sitten — "Labyrinth Oulu turned 1 years old!" -tarjous sivulla heinäkuussa 2026) | Ei | https://lgames.fi/en/ |
| `wayout` | WayOut | wayout.fi | 2781348-2 (WayOut Oy, rek. 2016, elossa) | Itsenäinen, perustajaomistuksessa (Niko Eskelinen) | **3**: Jyväskylä (alkuperäinen, 2015 toiminta alkoi), Tampere, Hyvinkää | Ei | https://wayout.fi/ |

## RAJATAPAUKSET — täsmälleen 2 kaupunkia (2)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | kaupungit | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|---|
| `huonepakopeli` | Huonepakopeli | huonepakopeli.fi | 2996282-8 (MooseFabric Oy, rek. 2019, elossa; kotisivu PRH:ssa musapekka.fi — vanha nimi/toinen liiketoiminta samalla Y-tunnuksella) | Itsenäinen (yhteyshenkilö Olli Hirvikangas, sama nimi kuin sivuston blogikirjoittaja) | **2**: Joensuu (2 toimipistettä: Koulukatu + Teollisuuskatu), Kuopio. Jyväskylä mainittu joissain alasivujen otsikoissa/breadcrumpeissa, mutta oma Jyväskylä-sivu 404, ei toimipistettä oikeasti auki — **EI laskettu mukaan** | Ei | https://huonepakopeli.fi/ |
| `the-great-escape` | The Great Escape | thegreatescape.fi | 2978448-6 (Gr8 Escape Oy, rek. 2019, elossa) | Itsenäinen (alun perin Kajaanin AMK:n opiskelijaprojekti 2016) | **2**: Kajaani ja Vuokatti (Sotkamo) — n. 30 km päässä toisistaan, samaa Kainuun seutua | Ei | https://www.thegreatescape.fi/home/ |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Room Escape Finland (roomescape.fi) | **KONKURSSI** — PRH: Room Escape Finland Oy (Y-tunnus 2695664-1, aputoiminimet Room Escape Helsinki/Lahti/Naantali/Oulu/Turku) companySituations = "KONK", rekisteröity 13.2.2026. Domain roomescape.fi palauttaa vain paljaan hakemistolistauksen ("Name Last Modified Size Directory valvonta-wp"), ei toimivaa sivustoa | PRH YTJ v3 -haku businessId=2695664-1; `fetch_page.py roomescape.fi` |
| Claustrophobia | Toimii Tallinnassa (Virossa), ei Suomessa — alkuperäinen ehdokaslistan oletus vääriä | Web-haku: kaikki Claustrophobia-osumat viittaavat Tallinnan sijaintiin, ei yhtään suomalaista toimipistettä löytynyt |
| Exit Room Helsinki (exitroomhelsinki.com) | Yksi kaupunki (Helsinki, Mäkelänkatu) — ei monikaupunkinen | exitroomhelsinki.com sivusto, yhteystiedot vain Helsingissä |
| Live Exit Games | Kaksi toimipistettä, mutta molemmat SAMASSA kaupungissa (Turku: Kakolanmäki + keskusta) — ei täytä monikaupunki-sääntöä | liveexitgames.fi; Y-tunnus 2723684-9 |
| Pakotarinat | Yhtiö lakannut toimimasta pakohuoneoperaattorina omalla brändillä: myi Espoon toimipisteen Truescapelle ja Joensuun toimipisteen Huonepakopelille (MooseFabric Oy:lle) — pelit jatkuvat samoissa tiloissa mutta eri omistajan/brändin alla. Karkaa.fi-hakemistossa näkyy silti vanhentuneena kahdessa maakunnassa — elävä hakemistomerkintä ei tarkoita elossa olevaa yhtiötä | pakotarinat.fi/en/our-story/: "sold its Espoo location to Truescape and its Joensuu location to Huonepakopeli" |
| EXITE, Amazed Games, Pakomielle, Huone Escapes, Escape Room Helsinki / Pakohuone Tarina | Kaikki yhden kaupungin (Helsinki tai Espoo) toimijoita — ei monikaupunkisia | Kunkin oman sivuston yhteystiedot; Huone Escapes avautui vasta syksyllä 2025 Espoon Tapiolaan, ei laajennusta muualle |
| Pako.fi | Domain vastaa (HTTP 200) mutta on täysin tyhjä sekä curlilla että `--js`-renderöinnillä (0 merkkiä) — ei tunnistettavaa pakohuoneyritystä tämän domainin takana | `fetch_page.py pako.fi` ja `fetch_page.py pako.fi --js` |
| Pakohuone.fi | Domain ei vastaa lainkaan (HTTP 000 / yhteysvirhe) | `fetch_page.py pakohuone.fi` |
| "Time Trap" | Ehdokaslistan nimi ei vastaa mitään löydettyä suomalaista pakohuoneketjua — hauilla löytyi vain yksittäisiä huoneita nimeltä ajankohtaan liittyen eri yrityksissä (esim. WayOutin "Back in Time" Tampereella), ei omaa ketjua nimellä Time Trap | Ei yhtään osumaa yritysrekisterissä tai hausssa nimelle "Time Trap" -pakohuoneketju |
| Cluedo-tyyppiset toimijat | Ei löytynyt yhtään suomalaista pakohuoneketjua tällä nimellä/konseptilla — Cluedo on lautapelibrändi, ei tunnistettu pakohuoneoperaattoriksi Suomessa | Ei osumia |
| M Room | Löytyi hausta "franchising"-hakusanalla, mutta on parturiliikeketju, ei pakohuoneyritys — väärä osuma alkuperäisessä laajassa haussa | franchising.fi/jasenet/m-room/, mroom.com |

## HUOMIOT

- **Tärkein löydös — Truescape ja Mysteeri ovat SAMA yhtiö.** Mysteeri (6 kaupunkia:
  Tampere, Turku, Jyväskylä, Kuopio, Pori, Mikkeli) liittyi Truescape Oy:n
  "pakohuonepeliperheeseen" syyskuussa 2019 — sama Y-tunnus 3016295-9, sama
  copyright-rivi ("Truescape Oy 2026 ©") molempien sivustojen alatunnisteessa, ja
  mysteeri.com:n oman sivun metatiedot/otsikko viittaavat suoraan Truescapeen.
  Tämä on sama tilanne kuin Effortia Oy sähkövertailussa: yksi yhtiö, kaksi
  kuluttajabrändiä. **Jos rakennetaan, listataan YHTENÄ rivinä (Truescape Oy), ei
  kahtena kilpailijana** — muuten tuplaisimme saman yhtiön kahdeksi riviksi
  (sama ansa kuin Saunalahti=Elisa). Yhdistettynä tämä on selvästi Suomen suurin
  pakohuoneketju kaupunkimäärällä mitattuna (9 kaupunkia).
- **Turun päällekkäisyys.** Sekä Truescape/Mysteeri (Turku, kaksi osoitetta:
  Aurakatu ja Aninkainen) että Labyrinth Games (Turku, Yliopistonkatu) että Live Exit
  Games (Turku, Kakolanmäki + keskusta) toimivat samassa kaupungissa. Tämä ei ole
  ongelma sinänsä — useampi ketju voi kilpailla samalla paikkakunnalla — mutta
  kertoo, että Turku on pakohuonealan toiseksi tihein kaupunki Helsingin jälkeen.
- **Seinäjoki — elävä osoite, suljettu toiminta (Risicum-tyyppinen löydös).**
  Truescape.fi:n sivupohjassa esiintyy edelleen Seinäjoen toimipisteen yhteystiedot
  (Kauppakatu 25) osana jaettua "yhteystiedot"-komponenttia, mutta erillinen haku
  paljasti sivun otsikon: "Pakohuonepeli Seinäjoki (**toistaiseksi suljettu**)".
  Seinäjokea EI laskettu mukaan Truescapen 9 kaupungin joukkoon — sivustolla näkyvä
  osoite ei tarkoita auki olevaa toimipistettä. Tämä on täsmälleen sama virhetyyppi
  kuin Risicum-tapaus (elävä domain + vanha tieto ≠ elossa oleva palvelu), vain
  yhden kaupungin tasolla koko ketjun sisällä.
- **Karkaa.fi-hakemisto (aluelistaus, JS-renderöity) ei paljastanut yhtään
  ylimääräistä monikaupunkista ketjua** WAYOUTin (esiintyy 3 kertaa: Keski-Suomi,
  Pirkanmaa, Uusimaa — täsmää Jyväskylä/Tampere/Hyvinkää) lisäksi. Kaikki muut
  hakemiston ~50 nimeä esiintyivät vain kerran (yksi kaupunki/maakunta). Truescape,
  Mysteeri ja Labyrinth Games eivät edes ole karkaa.fi:n listalla — hakemisto ei ole
  kattava, joten sitä käytettiin vain ristiintarkistukseen, ei ainoana lähteenä.
- **MooseFabric Oy:n PRH-rekisteröity kotisivu on musapekka.fi, ei huonepakopeli.fi.**
  Y-tunnus täsmää silti yhteyshenkilön nimen (Olli Hirvikangas) kautta sekä
  huonepakopeli.fi:n blogikirjoittajaan että toimipisteiden Joensuu-osoitteisiin.
  Jos `huonepakopeli` rakennetaan, tämä ristiriita (rekisteröity domain ≠ käytössä
  oleva kuluttajadomain) kannattaa mainita sivulla läpinäkyvyyden vuoksi.
- **Kokoluokka kaikilla pieni.** Yhdenkään vahvistetun tai rajatapauksen liikevaihto
  ei ylitä muutamaa miljoonaa euroa (Mysteerin oma "About us" -sivu ilmoittaa koko
  Mysteeri-brändin liikevaihdoksi 1,5 milj. €, 50 työntekijää, 27 huonetta — tämä on
  vain osa Truescape Oy:n kokonaisuudesta). Tämä ei ole karsintaperuste, mutta
  asettaa odotukset: pakohuoneet on rakenteellisesti pienten toimijoiden ala, ei
  suurten pörssiyhtiöiden ala kuten esim. autovuokraamot tai katsastus.
- **Suositus:** rakenna `pakohuoneet` 3 vahvistetulla rivillä (Truescape/Mysteeri,
  Labyrinth Games, WayOut) ja harkitse 2 rajatapauksen (Huonepakopeli, The Great
  Escape) lisäämistä 5 riviksi asti — sama poikkeuskäytäntö kuin `autokatsastus`
  (4 vahvistettua, dokumentoitu syy alle 5–9 tavoitteen). Jos Anton haluaa tiukemman
  rajan (esim. vähintään 3 kaupunkia), pudota molemmat rajatapaukset ja jää 3 riviin.
