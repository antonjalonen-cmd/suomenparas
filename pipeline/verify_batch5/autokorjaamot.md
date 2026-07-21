# autokorjaamot — brändivarmistus (batch 5)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (plain curl; `--js` ei tarvittu yhdellekään
vahvistetulle tai karsitulle brändille — kaikki palauttivat täyden leipätekstin ilman
JS-renderöintiä) + PRH:n YTJ v3 -rajapinta (`avoindata.prh.fi/opendata-ytj-api/v3/companies`)
jokaiselle Y-tunnukselle + kohdennettu websearch omistus-/rakenneväitteille. Rajaus: kuluttajille
valtakunnallisesti auton huoltoa ja korjausta tarjoavat ketjut, joilla on oma verkkosivusto —
ei paikallisia yksittäisiä korjaamoita, ei pelkkää markkinointibrändiä ilman yhtä operoivaa yhtiötä.

**Tämä kategoria osui suoraan QUEUED_CATEGORIES.md:n varoittamaan ansaan kahdesti:** ensin
"onko tämä yksi yritys vai löyhä yhteenliittymä itsenäisiä korjaamoita" (AD/Bosch/Autoasi/Fixus/
Autofit ovat KAIKKI rakenteeltaan tätä samaa "ketjukonsepti + itsenäiset yrittäjäkorjaamot"
-mallia, kuten OpusLex lakifirmat-kategoriassa ja RengasCenter/Motonet rengasliikkeet-kategoriassa),
ja toiseksi "sama omistaja kahtena kilpailevana brändinä" (Fixus ja Mekonomen ovat sama yhtiö).

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | mittaus-URL |
|---|---|---|---|---|---|---|
| `autoasi` | Autoasi | autoasi.fi | 2042810-0 (Örum Oy Ab) — rekisterissä, ei endDate:a, liikevaihto 49,5 M€ / 124 työntekijää (2024) | Örum Oy Ab omistaa Autoasi-ketjukonseptin ja on autoasi.fi:n tietosuojaselosteen mukainen rekisterinpitäjä ("Tämä on Örum Oy Ab:n... tietosuojaseloste"); yksittäiset ~150–250 Autoasi-korjaamoa ovat itsenäisten yrittäjien omistamia (esim. "Autoasi-korjaamo Raisio" on oma Oy:nsä) | Ei — curl palautti 3 402 merkkiä | https://www.autoasi.fi/ |
| `ad-finland` | AD Finland | ad-finland.com | 0554943-0 (AD FIN Oy) — rekisterissä, aktiivinen, rekisteröity 9.2.1984 | AD FIN Oy on ad-finland.com:n tietosuojaselosteen rekisterinpitäjä ja ylläpitää itse kansallisia kuluttajatuotteita (AD-Ajoturva 49 €/v, AD-Lasku, AD-Tili -rahoitus); osa Ranskalais-eurooppalaista AD International -ostoyhteenliittymää; ~150 valtuutettua AD-korjaamoa, monet säilyttävät "AD"-etuliitteen omassa yritysnimessään (esim. "Juhan AD-Autohuolto", "Juuson AD-Autohuolto" — itsenäisiä yrittäjiä) | Ei — curl palautti 2 678 merkkiä | https://ad-finland.com/ |
| `fixus` | Fixus | fixus.fi | 0110111-0 (MEKO Finland Oy, ent. Koivunen Oy vuoteen 2025 asti) — rekisterissä, aktiivinen | MEKO Finland Oy on fixus.fi:n tietosuojaselosteen rekisterinpitäjä ("Rekisterinpitäjä: MEKO Finland Oy"); yhtiö on osa Ruotsin pörssissä listattua MEKO-konsernia (ent. Mekonomen Group); lähes 400 itsenäistä varaosaliike-/korjaamoyrittäjää käyttää Fixus-brändiä | Ei — curl palautti 3 320 merkkiä | https://fixus.fi/ |
| `autofit` | Autofit | autofit.fi | 1630177-2 (Atoy Automotive Finland Oy) — rekisterissä, aktiivinen | Atoy Automotive Finland Oy (perustettu 1955, osa Atoy-perheyritystä) toimii Autofit-ketjun varaosamaahantuojana ja ohjaa/tukee ketjun toimintaa Suomessa (footer: "Autofit-ketju c/o Atoy Automotive Finland Oy"); yksittäiset korjaamot ovat "Autofit-yrittäjiä" | Ei — curl palautti 3 422 merkkiä | https://autofit.fi/ |
| `motonet` | Motonet-korjaamot | motonet.fi | 0699457-9 (Motonet Oy) — sama Y-tunnus kuin rengasliikkeet-kategoriassa | Motonet Oy — suomalainen perheyritys (Broman Group). **Sama yhtiö esiintyy kahdessa kategoriassa** — rengasliikkeet mittaa `/palvelut/motonet-rengaspalvelut` (rengashotellit), tämä mittaa `/palvelut/motonet-korjaamot` (yleinen monimerkkikorjaamoketju, franchise-yrittäjät: "Lähde Motonet-korjaamoyrittäjäksi") | Ei — curl palautti 4 730 merkkiä | https://www.motonet.fi/palvelut/motonet-korjaamot |
| `euromaster` | Euromaster (autohuolto) | euromaster.fi | 0711042-1 (Suomen Euromaster Oy) — sama Y-tunnus kuin rengasliikkeet-kategoriassa | Michelin — valmistajan oma ketju. **Sama yhtiö esiintyy kahdessa kategoriassa** — rengasliikkeet mittaa etusivun/rengaspalvelut, tämä mittaa `/autohuolto`-osiota, joka sisältää aidon yleisen korjaamotarjonnan (jarrut, jousitus, jakopää, määräaikaishuolto, vuosihuolto ja katsastus, kuntotarkastus) rengastyön lisäksi | Ei — curl palautti 8 607 merkkiä | https://www.euromaster.fi/autohuolto |

Kaikki kuusi Y-tunnusta vahvistettu `avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=<y>`:
Örum Oy Ab, AD FIN Oy, MEKO Finland Oy ja Atoy Automotive Finland Oy kaikki `tradeRegisterStatus:"1"`,
`status:"2"` (rekisterissä, aktiivinen), ei endDate:a; Motonet Oy ja Suomen Euromaster Oy
vahvistettu jo rengasliikkeet-kategoriassa (ks. `verify_batch4/rengasliikkeet.md`).

## KARSITUT

- **Bosch Car Service** — **ratkaistu: löyhä brändiverkosto, ei yksi operoiva yhtiö, ei
  yhtenäistä hinnoittelua.** Oma sivu sanoo suoraan: "Bosch Car Service on itsenäisten
  korjaamoiden verkosto" ja lisää ettei kyseessä ole "perinteinen franchising-toiminta".
  Yli 70 suomalaista Bosch Car Service -korjaamoa toimivat täysin erillisillä, historiallisilla
  yritysnimillä jotka eivät edes sisällä sanaa "Bosch" (Tampereen Autosähkö Oy, Auto MAN Oy,
  Loimaan Autohuolto Oy, Hyvinkään Ajoneuvohuolto, Renkomäen Autoexpert Oy) — jokainen julkaisee
  OMAN hinnastonsa omalla erillisellä verkko-osoitteellaan (esim. rexpert.boschcarservice.fi/hinnasto/,
  automan.fi/autohuolto/hinnasto/, Tampereen Autosähkön 99,50 €/h vs. muiden eri tuntihinnat).
  boschcarservice.com/fi/ itse on hakuportaali ("Korjaamohaku") joka ohjaa asiakkaan valitsemalleen
  itsenäiselle korjaamolle — ei tarjoa yhtään valtakunnallista hintaa, tuotetta tai sopimuskumppanuutta
  kuten AD-Tili tai Autoasi Ajoturva. Sama ansa kuin OpusLex lakifirmat-kategoriassa: yhteinen brändi
  ilman yhtä yhtiötä, joka vastaisi kuluttajalle näkyvästä kaupallisesta kokonaisuudesta. Ei ole
  mielekästä pisteyttää "yhtä yritystä", koska sellaista ei ole — pisteet menisivät mielivaltaisesti
  valitulle yksittäiselle jäsenkorjaamolle, joka on juuri se paikallinen yksittäistapaus, jota
  QUEUED_CATEGORIES.md:n ⚠️-varoitus kieltää.
- **Mekonomen** — **sama omistaja kuin Fixus, karsittu tuplabrändinä (kuten Nissen=Instrumentarium
  optikot-kategoriassa).** mekonomen.fi:n omat yhteystiedot nimeävät hallinnoksi suoraan
  "MEKO Finland Oy, Malminkaari 12, 00700 Helsinki" — sama Y-tunnus 0110111-0 joka on Fixuksen
  rekisterinpitäjä samalla osoitteella. MEKO-konserni (Ruotsin pörssissä, ent. Mekonomen Group)
  osti Koivunen Oy:n 2022 ja nimesi sen MEKO Finland Oy:ksi 21.1.2025 — sama yhtiö pyörittää nyt
  KAHTA kilpailevana esitettyä ketjua Suomessa (Fixus ~400 toimipistettä, Mekonomen ~70
  paikkakuntaa). Fixus valittu säilytettäväksi suuremman Suomen-toimipistemäärän ja
  vakiintuneemman kotimaisen aseman vuoksi ("Suomen suurin autokorjaamo- ja
  varaosaliikeketju"); Mekonomen karsittu tuplauksena, ei väärän kohderyhmän vuoksi.
- **Autoklinikka** — **ei kuulu tähän kategoriaan; eri palvelu (kolarikorjaus/vahinkokorjaus),
  ei aito valtakunnallinen yleishuoltoketju.** Autoklinikka-yhtiöt Oy (Y-tunnus 2225675-2,
  liikevaihto 123,5 M€, 50+ toimipaikkaa) markkinoi itseään "Suomen johtava
  autokorjaamoketju" -sloganilla, mutta oman navigaationsa mukaan ydinliiketoiminta on
  Kolarikorjaus (peltikorjaus, PDR, raekuurovauriot, automaalaus) ja Tuulilasit — ei yleinen
  huolto/korjaus. "Merkkihuolto"-palvelu (määräaikaishuollot, joita tämä kategoria mittaisi)
  on rajattu vain kolmeen pääkaupunkiseudun toimipisteeseen (Helsinki Alppila, Pitäjänmäki,
  Konala) — ei valtakunnallinen samalla tavalla kuin Autoasi/Fixus/AD/Autofit/Motonet-korjaamot/
  Euromaster-autohuolto. Rajatapaus lähempänä omaa kategoriaansa (vahinkokorjaamot/tuulilasiliikkeet)
  kuin tätä; ei pakattu mukaan väärällä perusteella.

## HUOMIOT

- **Kategorian ydinlöytö: "ketjukonsepti + itsenäiset yrittäjäkorjaamot" -rakenne on tässä
  kategoriassa NORMI, ei poikkeus — ja se on eri asia kuin OpusLex-ansa.** Kaikki kuusi
  vahvistettua ovat rakenteeltaan franchise-tyyppisiä: yksi keskusyhtiö omistaa/lisensoi
  brändin ja pyörittää kansallista verkkosivua, mutta suuri osa (tai kaikki) yksittäisistä
  korjaamoista ovat itsenäisten yrittäjien omistamia erillisillä Y-tunnuksilla. Tämä hyväksyttiin
  jo rengasliikkeet-kategoriassa (Motonet, RengasCenter). Ratkaiseva testi ei ole "omistetaanko
  jokainen toimipiste keskitetysti" vaan **"on olemassa YKSI rekisteröity yhtiö, joka omistaa
  brändin, operoi kansallista verkkosivua (tietosuojaselosteen rekisterinpitäjänä) ja tarjoaa
  ainakin joitain valtakunnallisia kuluttajatuotteita (esim. AD-Tili, Autoasi Ajoturva,
  Mekonomen Rahoitus)."** OpusLex ja nyt Bosch Car Service epäonnistuvat juuri tässä: kumpikaan
  ei ole yksi yhtiö vaan pelkkä yhteinen brändi/markkinointiverkosto ilman keskitettyä
  kaupallista vastuuta tai yhtenäistä hinnoittelua — jäsenet pysyvät täysin erillisinä sekä
  oikeudellisesti että kaupallisesti.
- **AD Finland on rajatapaus, mutta läpäisi testin — dokumentoitu tarkasti koska tämä oli
  brief:n nimeämä epäilyttävin tapaus Bosch Car Servicen ohella.** AD FIN Oy on pieni
  (liikevaihto 2,2 M€, 5 työntekijää 2024) verrattuna Örumiin (49,5 M€) tai MEKO Finlandiin
  (115,9 M€) — se on todennäköisesti vain kansallinen koordinaatio-/markkinointitoimisto AD
  Internationalin (kansainvälinen varaosien ostoallianssi) alaisuudessa, ei suuri operoiva
  yhtiö. Erotti sen Boschista kuitenkin kaksi konkreettista löydöstä: (1) AD FIN Oy on
  nimenomaisesti ad-finland.com:n tietosuojaselosteen rekisterinpitäjä osoitteella ja
  puhelinnumerolla, ei pelkkä globaali brändinhaltija; (2) AD FIN Oy hallinnoi suoraan
  nimettyjä kansallisia kuluttajatuotteita (AD-Ajoturva 49 €/v tiepalvelu, AD-Lasku, AD-Tili
  -rahoitus) — ei vain reititä hakuja itsenäisille korjaamoille kuten Bosch. Jos jatkokehitys
  löytää näytön siitä, että AD-Tili/AD-Ajoturva ovatkin kolmannen osapuolen (esim. rahoitusyhtiön)
  tuotteita AD:n brändillä, tämä pitäisi arvioida uudelleen.
- **Domainien epäjohdonmukaisuus:** AD Finlandin verkko-osoite on ad-finland.com (ei .fi) —
  poikkeuksellista valtakunnalliselle suomalaiselle ketjulle, mutta ei itsessään peruste karsia;
  sivu on täysin suomenkielinen ja kohdistettu Suomen markkinalle (kieli fi, osoite Hyvinkäällä).
- **Ristikkäiskategoria-disclosure (kuten Mehiläinen/Terveystalo yksityislaakarit+hammaslaakarit-
  kategorioissa):** Motonet (0699457-9) ja Suomen Euromaster Oy (0711042-1) esiintyvät MOLEMMAT
  jo rengasliikkeet-kategoriassa (batch 4) JA tässä autokorjaamot-kategoriassa — sama slug/domain/
  y_tunnus/omistaja on tarkoituksella toistettu tässä tiedostossa konsistenssin vuoksi, mutta
  kumpikin mitataan eri sivulta: rengasliikkeet mittaa rengaspalvelut/rengashotellit, tämä
  kategoria mittaa yleistä monimerkkikorjaamo-/autohuoltotarjontaa. Rakentajan pitää
  varmistaa, ettei sama laskurikone/sivulataus mene molempiin kategorioihin — eri URL, eri
  ekstraktio.
- **Hinta-avoimuuden kirjo antaa kategorialle aidon pisteytyshajonnan:** Fixus ja Autofit
  näyttävät hinnan SUORAAN rekisterinumeron syöttämisen jälkeen ennen yhteystietoja
  ("Anna autosi rekisterinumero ja näet huollon hinnan" / "Hinnan ja vapaat ajat näet
  täytettyäsi auton tiedot") — vahvin läpinäkyvyystaso. Euromasterin autohuolto-osiolla on
  navigaatiossa erillinen "Palveluhinnasto"-sivu. Autoasi ja AD Finland toimivat sen sijaan
  tarjouspyyntö-/yhteydenottomallilla ("Pyydä Huoltotarjous", korjaamohaku ilman kiinteää
  hintaa) — heikompi mutta ei olematon läpinäkyvyys. Tämä ero kannattaa näyttää sivulla
  pisteytyksen selittäjänä, ei vain lopputuloksena.
- **JS-renderöintiä ei tarvittu yhdellekään** kuudesta vahvistetusta eikä kummallekaan
  karsitusta (Bosch, Mekonomen, Autoklinikka) — kaikki palauttivat täyden leipätekstin
  tavallisella curl-haulla. Merkitään ekstraktioagenteille, ettei renderöintiajoa tarvita
  tässä kategoriassa.
- **Kategoria jää tavoitteen (5–9) sisään kuudella vahvistetulla** — kahden aidosti
  vahvan ehdokkaan (Bosch Car Service, Mekonomen) karsiutuessa perustellusti rakenteellisista
  syistä eikä siksi, ettei yhtiötä olisi löytynyt. Ei tarvetta swapata kategoriaa toiseen;
  autokorjaamot osoittautui QUEUED_CATEGORIES.md:n varoituksesta huolimatta riittävän
  valtakunnalliseksi, samaan tapaan kuin autokoulut batch 4:ssä.
