# Faktantarkistus B — 4 julkaistua yhtiötä

Tarkastuspäivä: 21.7.2026
Menetelmä: `python pipeline/fetch_page.py <url> [--js]` jokaiselle yhtiölle, verrattuna data/*.json-tiedostojen julkaistuihin quote-kenttiin. Ei muokattu data/- tai pipeline/extracts/-tiedostoja.

---

## 1. Suomen Muuttofirma (data/muuttopalvelut.json, voittaja 86,0, läpinäkyvyys 100/100)

Sivut haettu: muuttofirma.fi (etusivu, /muuttopalvelun-hinta/, /kotimuutot/, /ukk/, /muuton-vakuuttaminen/, /yhteystiedot/), easymoving.fi (--js).

### VAHVISTETTU
- **Hintaesimerkit**: 249 €, 589 €, 1 599 € — kaikki kolme löytyvät sanasta sanaan /muuttopalvelun-hinta/-sivulta samoine kuvauksineen (Kuopio-opiskelijamuutto, Joensuu–Kuopio-kaksio, Helsinki–Kuopio-omakotitalo).
- **"Yleiset kotimuuton hinnat ovat muuttotyön osalta 200–500 €"** — sanatarkka lainaus löytyy /ukk/-sivulta kohdasta "Mitä muutto maksaa?".
- **Easy Move / easymoving.fi**: sovellus mainittu etusivulla ("EASY MOVE… Kuvaa muutettavat tavarat, Valitse tarvitsemasi palvelut, Hinta heti"), ja easymoving.fi toimii todellisuudessa selainpohjaisena kirjautumis/tilausjärjestelmänä (Kirjaudu/Rekisteröidy, iOS/Android) — vahvistaa "toimii myös verkkoselaimen kautta" -väitteen.
- **Vakuutus/vastuu**: "erittäin rajattu" tiekuljetusvastuu ja perintömaljakko-esimerkki (1000 €:n maljakko, ~10 € korvaus) löytyvät sanasta sanaan /muuton-vakuuttaminen/-sivulta.
- **Toimipisteet/yhteystiedot**: Joensuu (Pilkontie 5) puh. 010 209 8400, Kuopio (Kumpusaarentie 52) puh. 010 209 8401 — täsmää.
- **Y-tunnus 2292440-7** — vahvistettu /yhteystiedot/-sivulta.
- **Google-arviot 9.6/10**: vahvistettu, ja etusivulla oli fetkauspäivänä jopa kuusi nimettyä arvostelua (Marjut L, Momo Porri, Tontza, Meri Kinnunen, Tiina Tikkanen, Urpo Holopainen — kotimuutto-sivulla vielä kaksi lisää), eli enemmän kuin julkaistun datan "neljä".

### POIKKEAMA
Ei löytynyt merkittäviä poikkeamia. Yksi sivuston sisäinen pieni epäjohdonmukaisuus (ei koske julkaistua dataamme): Kuopion postinumero on /muuttopalvelun-hinta/-sivulla "70760" mutta /yhteystiedot/-sivulla "70620" — meidän lainauksemme (70760) täsmää ainakin toisen sivun kanssa, joten tätä ei lasketa poikkeamaksi.

**Arvio pistevaikutuksesta: 0.** Kaikki läpinäkyvyys-kuitin väitteet pitävät paikkansa tai ovat vahvempia kuin julkaistu teksti antaa ymmärtää.

---

## 2. Antin Autokoulu (data/autokoulut.json, voittaja 86,3, läpinäkyvyys 100/100)

Sivut haettu: antinautokoulu.fi (etusivu, /hinnasto/, /hinnasto/oulu/ eli /autokoulu/oulu/, /tietosuojaseloste/, /asiakaspalvelu/), --js ja --raw molemmat testattu.

### VAHVISTETTU
- **"Ilmoittaudu Antin Autokouluun" -nappula** — löytyy etusivulta sanatarkasti.
- **33 toimipistettä** — hinnasto-sivun toimipaikkavalikossa täsmälleen 33 kaupunkia listattuna.
- **Y-tunnus 2763674-6 ja osoite Isokatu 11 C 14, 90100 Oulu** — vahvistettu /tietosuojaseloste/-sivulta sanatarkasti.
- **Puhelin 044 022 1265 ja info@antinautokoulu.fi** — vahvistettu useilla sivuilla.
- **Chat-tuki**: /asiakaspalvelu/-sivulta löytyy sanatarkka lause "Voit olla meihin yhteydessä myös sivun alanurkassa olevan chatin kautta aukioloaikojen puitteissa: ma-to 10.00-18.00, pe 10.00-15.00" — täsmää julkaistuun quoteen sanasta sanaan.
- **Aukioloajat ma-to 10-18, pe 10-15** — vahvistettu.

### POIKKEAMA / EI-VARMISTETTAVISSA
1. **"1 tunti 99 €" -hintarivi** (perusteena 30/30 pisteelle "Kurssien hinnat julkisesti esillä"): hinnasto-sivun toimipaikkavalinta on JS-pohjainen pudotusvalikko, joka on `disabled`-tilassa ennen valintaa ja lataa hintataulukon todennäköisesti erillisellä AJAX-kutsulla käyttäjän valinnan jälkeen. Sekä curl- että --js-renderöinti (myös yksittäisen toimipisteen alasivulta, esim. /hinnasto/oulu/) palauttivat sivun ilman yhtään näkyvää euromäärää ajotunneille. **En pystynyt toistamaan alkuperäistä havaintoa** — tämä voi johtua työkalun rajoituksesta (ei pudotusvalikon interaktiota, mikä on rajapyyntöjen ulkopuolella) eikä välttämättä tarkoita että hinta olisi poistettu. Suositus: tarkista manuaalisesti tai selaimen kautta.
2. **Uusi havainto (ei alkuperäisessä datassa)**: Oulun toimipiste-sivun `<title>`-tagi on "Antin Autokoulu Oulu | Ajokortti alkaen 979 €" — eli kokonaispakettihinta *on* jossain muodossa julkinen (hakukonetulosten/välilehden otsikossa), vaikka sivun näkyvässä leipätekstissä sitä ei toistaiseksi näy. Tämä on julkaistua dataa myönteisempi löydös, ei negatiivinen poikkeama, mutta kannattaa huomioida jos kriteeriä "kokonaiskurssin hinta puuttuu" käytetään miinuksena.
3. **"19 Google-arvostelua" etusivulla** (peruste 10/10 pisteelle "Riippumaton arviolähde esillä"): en löytänyt mitään arvostelulaatikkoa tai tähtiarviota nykyiseltä etusivulta (ei raakana eikä --js-renderöitynä). Löysin sen sijaan toimipistesivulta (esim. Oulu) lauseen "jota jopa 98 % asiakkaista suosittelee" — eri luku, eri sivu, eikä siinä näy arvostelumäärää eikä ulkopuolista lähdettä (esim. Google-widgetiä). **Tätä ei pystytty vahvistamaan nykyisellä sivustolla** — joko arvostelu-widget on poistettu etusivulta extraktion jälkeen, tai se ei renderöidy fetch-työkalulla. Suositus: tarkista selaimella onko Google-arvostelut yhä näkyvissä jossain kohtaa etusivua.

**Arvio pistevaikutuksesta: pieni-kohtalainen riski 10-20 pisteeseen (30 max) läpinäkyvyys-pilarin sisällä**, koska sekä hintarivi (30 p) että arviolähde (10 p) -väitteitä ei pystytty toistamaan suoraan — molemmat saattavat silti olla oikein (interaktion tai renderöintiajan takia), mutta niitä ei voi kutsua VAHVISTETUKSI tällä ajolla. Kokonaispistevaikutus todennäköisesti pieni, koska kummallekin löytyi todennäköinen selitys (JS-vuorovaikutus / sivun muutos) eikä selvää valheellisuutta.

---

## 3. Pohjola Vakuutus (data/vakuutukset.json, 18.7. korjattu riville score 63,7)

Sivut haettu **kaikki --js:llä** (pakollinen op.fi:lle): /henkiloasiakkaat/vakuutukset/vakuutuslaskuri, /henkiloasiakkaat/vakuutukset/ajoneuvovakuutus/autovakuutus-henkiloautolle/autovakuutuslaskuri, /henkiloasiakkaat/vakuutukset/kotivakuutus/omakotitalo, /henkiloasiakkaat/vakuutukset/henkilovakuutus/matkavakuutus, /henkiloasiakkaat/vakuutukset/elainvakuutus/koiravakuutus.

### VAHVISTETTU
- **Hintalaskurit olemassa julkisesti** kaikille pääryhmille (auto, koti, matka, koira, vene, henkilö) ilman kirjautumista sivulle pääsyä varten.
- **Ehdot/tuoteopas PDF:t**: kotivakuutuksen sivulla "Kodin ja tavaroiden vakuutukset, tuoteopas (pdf)", "…ehdot (pdf)", "Omakoti-vakuutus, vakuutustietoasiakirja (pdf)" — vahvistettu.
- **Matkavakuutuksen omavastuu 0 €** sairaus/tapaturma- ja matkatavaraosalta (0 € tai valinnan mukaan 100 €) — sivu vahvistaa yleisen rakenteen, joskin ei julkaistun luvun mukaisesti (ks. poikkeama alla).
- **Koiravakuutus 70 € omavastuu + 30 %** ensimmäisestä vahingosta kalenterivuonna — sanatarkka esimerkki (Leo-koira, hampaan murtuma, 600 €:n lasku, 70 €:n omavastuu + 30 % jäljelle jäävästä) löytyy koiravakuutus-sivulta.
- **OP-mobiilisovellus** vakuutusasiointiin mainittu.

### POIKKEAMA
1. **"Hinta-arvio ilman yhteystietoja" = Kyllä, 30/30 pistettä — TÄMÄ ON VIRHEELLINEN vähintään ajoneuvovakuutusten osalta.** Autovakuutuslaskuri-sivu toteaa suoraan: *"Pääset aloittamaan autovakuutuslaskurin käytön, kun annat autosi rekisterinumeron. Laskuri kysyy tämän jälkeen henkilötunnuksesi sekä autoasi koskevia kysymyksiä. Tarvitsemme henkilötunnuksesi, jotta voimme laskea tarkan hinnan autovakuutuksellesi…"* — eli auton/moottoripyörän vakuutuslaskuri **vaatii henkilötunnuksen** ennen tarkan hinnan näyttämistä. Tämä on suoraan ristiriidassa kriteerin nimen ("ilman yhteystietoja") ja täysien pisteiden kanssa. Sama huomio on jo tehty tässä datatiedostossa POP Vakuutuksen kohdalla ("Haittapuolia ovat henkilötunnuksen vaatiminen hintalaskurissa") — Pohjolan rivi ei mainitse samaa ongelmaa, vaikka ilmiö toistuu sen omalla ajoneuvovakuutuslaskurilla.
2. **"€70+30 % matkavakuutuksella" -omavastuuväite on todennäköisesti VÄÄRÄ / sekoittunut koiravakuutuksen kanssa.** Julkaistu yhteenveto sanoo: *"…autovakuutuksella €200 omavastuut kaskoissa ja €70+30% matkavakuutuksella, koiravakuutuksella €70 vakuutuskaudella ja 30-40% lisäkuluista."* Nykyinen matkavakuutus-sivu (koko sisältö luettu, 28 559 merkkiä) ei sisällä lainkaan lukuja "70 €" tai "30 %" minkään matkavakuutusturvan omavastuuna — matkustajavakuutuksen omavastuu on 0 €, matkatavaravakuutuksen 0 € tai 100 €, matkavastuuvakuutuksen 150 €, matkaoikeusturvan 15 % (väh. 200 €). Sen sijaan **koiravakuutuksen** sivulla esiintyy juuri luku "70 euron omavastuu... maksat omavastuuta 30 %" — tarkalleen sama luku kuin julkaistussa tekstissä on liitetty sekä matka- että koiravakuutukseen. Vaikuttaa siltä, että alkuperäinen ekstraktio kopioi koiravakuutuksen luvun myös matkavakuutus-riville.

**Arvio pistevaikutuksesta: kohtalainen-suuri.** Kohta 1 koskee 30 pisteen kriteeriä pillarissa, jonka paino on 30 % kokonaispisteistä — jos "auto/moottoripyörä vaatii henkilötunnuksen" lasketaan osittaiseksi täyttymykseksi eikä täydeksi, 30 pisteestä voisi pudota esim. 15-20 pisteeseen, mikä laskisi läpinäkyvyys-pilaria n. 3-4 pistettä ja kokonaispistemäärää n. 1 pisteen. Kohta 2 on lähinnä tekstivirhe (yhteenvedossa/vahvuudet-kentässä, ei suoraan pisteytetyssä kriteeririvissä), mutta koska sama virhe (18.7. korjattu rivi) toistuu, suosittelen korjaamaan tekstin joka tapauksessa faktavirheenä riippumatta pistevaikutuksesta.

---

## 4. Hammas Mehiläinen (data/hammaslaakarit.json, voittaja 84,3)

Sivut haettu **--js:llä** (pakollinen mehilainen.fi:lle): /hammashoito (koko hinnasto), /ajanvaraus?service=hammashoito, /toimipisteet (ei toiminut suoraan, ks. alla).

### VAHVISTETTU
- **Hammastarkastus 56,00 € (Kela-korvauksen jälkeen) / 86,00 € (ilman)** — sanatarkka täsmäys hinnasto-taulukosta.
- **Hampaan paikkaus 97,00–216,00 €**, **hammaskiven poisto 122,00–169,00 €**, **kruunu 627,00–812,00 €** — kaikki täsmäävät tarkalleen julkaistuun dataan.
- **Röntgenkuva: "Hinta lääkärin lähetteellä Kela-korvauksen jälkeen 80 €"** — sanatarkka lainaus vahvistettu.
- **Poliklinikkamaksu vapautuu viiden käynnin jälkeen kalenterivuoden loppuosaksi** — vahvistettu sanatarkasti ("Viidennen maksun jälkeen poliklinikkamaksu on 0 € lopun kalenterivuoden käyntien ajan").
- **Ajanvaraus ilman kirjautumista**: /ajanvaraus-sivu latasi ajanvaraustyökalun (päivämäärävalinta, "Valitse maksaja tai palvelu") ilman että kirjautuminen vaadittiin ensin.
- **Asiakaspalvelu/ajanvaraus 010 273 8000** — vahvistettu.
- **Y-tunnus ei näkyvissä** — vahvistettu (ei löytynyt hakusanoilla "Y-tunnus" tai "1927556" koko sivulta).
- **Riippumaton arviolähde puuttuu** (vain "Asiakkaamme suosittelevat Mehiläistä" -oma mittari ilman ulkopuolista linkkiä) — vahvistettu sanasta sanaan.
- **Digiklinikka/OmaMehiläinen mainittu** navigaatiossa ja palveluluettelossa.

### POIKKEAMA
- **Toimipisteiden tarkkaa listaa (Nokia, Mikkeli, Hyvinkää, Lohja, Espoo Iso Omena, Joensuu) ei pystytty toistamaan** — /toimipisteet-haku on interaktiivinen hakukomponentti eikä palauttanut listaa suoralla URL-kutsulla (404 tai tyhjä tulos). Tämä on työkalurajoitus, ei vahvistettu ristiriita: en löytänyt näyttöä siitä että lista olisi väärä, mutta en myöskään pystynyt varmistamaan sitä uudelleen. Huomionarvoista: julkaistu quote sanoo "Seitsemän nimettyä… klinikkaa" mutta listaa vain kuusi paikkakuntaa — tämä ristiriita on jo alkuperäisessä datassa (lukumäärä vs. nimetty lista), ei minun löytämäni uusi virhe, mutta suosittelen korjaamaan sen selkeyden vuoksi.
- **Uusi havainto (ei vaikuta pisteytykseen, informatiivinen)**: sivustolla mainitaan 1.1.2026 alkaen käyttöön otettu erillinen "Kanta-maksu (4 €)" jokaisella käynnillä, jota ei ole julkaistussa datassa. Ei ole ristiriita (datassa ei väitetä sen puuttuvan), mutta ajantasaisuuden kannalta relevantti muutos hinnastossa.

**Arvio pistevaikutuksesta: hyvin pieni.** Kaikki pisteytykseen suoraan liittyvät kriteerit vahvistuivat. Ainoa avoin kohta (toimipisteiden nimilista, "seitsemän" vs. kuusi nimeä) on alkuperäisen datan sisäinen epätarkkuus, ei tässä ajossa löydetty uusi ristiriita, ja koskee vain "Toimipisteet ja aukioloajat kerrottu" -kriteerin sanamuotoa, ei pistemäärää (15/15 annettiin jo, ja toimipisteitä todella on useita nimettyinä).

---

## Yhteenveto

| Yhtiö | Vahvistettuja väitteitä | Poikkeamia/ei-varmistettavissa | Suurin löydös |
|---|---|---|---|
| Suomen Muuttofirma | 7/7 | 0 | — |
| Antin Autokoulu | 5/5 tarkistettua | 2 (ei-toistettavissa: hintarivi 99€, Google-arviot 19 kpl) | Ei suoraa virhettä löytynyt, mutta kaksi läpinäkyvyys-pisteperustetta ei toistunut fetch-työkalulla |
| Pohjola Vakuutus | 5/5 muuta | 2 (henkilötunnus-vaatimus autolaskurissa vastoin "ilman yhteystietoja"-väitettä; matka- vs. koiravakuutuksen omavastuulukujen sekoittuminen) | **Autovakuutuslaskuri vaatii henkilötunnuksen ennen tarkkaa hintaa — ristiriidassa 30/30-pisteytyksen kanssa** |
| Hammas Mehiläinen | 9/9 | 1 (toimipistelistaa ei pystytty toistamaan hakutyökalulla, ei osoitettu vääräksi) | — |

**Yhteensä 5 poikkeama/ei-varmistettavissa-havaintoa 4 yhtiön yli**, joista **kaksi on todennäköisiä tosiasiallisia virheitä julkaistussa datassa** (molemmat Pohjola Vakuutuksen rivillä: henkilötunnus-vaatimus autolaskurissa, ja matka/koira-omavastuulukujen sekaannus) ja **kolme on työkalurajoitteita** (Antin Autokoulun hintarivi ja Google-arviot, Hammas Mehiläisen toimipistelista) joita ei pystytty toistamaan mutta joita ei myöskään osoitettu vääriksi.
