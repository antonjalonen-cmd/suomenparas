# Brändivarmistus — Autokoulut (BATCH 4)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py`:llä (curl; ei yhdellekään vahvistetulle
tarvinnut `--js`) + PRH:n avoindata-ytj-api v3 -rajapinta (nimihaku → businessId-vahvistus,
kaikki aputoiminimet luetteloitu omistuskeskittymän arvioimiseksi).

**Tulos: 4 vahvistettua — RAKENNETTAVISSA poikkeuksella, ei EI RAKENNETTAVISSA.**
Toisin kuin QUEUED_CATEGORIES.md:n varovainen ennakko-oletus ("verify — may be too
local"), Suomessa on itse asiassa neljä aidosti valtakunnallista, satoja toimipisteitä
kattavaa autokouluketjua — ala on viime vuosina konsolidoitunut voimakkaasti
pääomasijoittajavetoisten "roll-up"-ostojen kautta (Epic/Korona Invest, CAP). Neljä
vahvistettua on sama määrä kuin `autokatsastus`-kategoriassa (batch 3), joka silti
rakennettiin dokumentoidulla poikkeuksella — sama ratkaisu kelpaa tässä.

## VAHVISTETUT (4)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `cap-autokoulu` | CAP-Autokoulu | cap.fi | 0841716-9 (CAP-Group Oy, ent. CAP-Koulutus Oy) | Ei konsernitietoa löydetty — itsenäinen yhtiö; toimii osin sopimusyrittäjyys-mallilla ("CAP-Sopimusyrittäjyys") | Ei — curl palautti 14 647 merkkiä | https://cap.fi/ |
| `epic-autokoulu` | Epic Autokoulu | epicautokoulu.fi | 2551291-8 (Epic Autokoulu Oy) | **Korona Invest** (suomalainen pääomasijoitusrahasto) suurin omistaja 28.2.2020 alkaen; konserniin kuuluu myös Autokoulu Safiiri Oy ja Liikenneterveys Oy | Ei — curl palautti 10 032 merkkiä | https://www.epicautokoulu.fi/ |
| `antin-autokoulu` | Antin Autokoulu | antinautokoulu.fi | 2763674-6 (Antin Autokoulu Oy, rek. 2016 — kolmas saman nimen yhtiö PRH:ssa, kaksi edeltäjää lakannut/nimenvaihdettu, katso HUOMIOT) | Ei konsernitietoa löydetty — itsenäinen yhtiö, kotipaikka Raahe | Ei — curl palautti 4 939 merkkiä | https://antinautokoulu.fi/ |
| `ajokorttiverkosta` | Ajokortti Verkosta (NetDriving) | ajokorttiverkosta.fi | 1440949-9 (RG Driving Consulting Oy) — "NetDriving!" ja "DRIVING AJOKORTTIVERKOSTA" ovat rekisteröityjä aputoiminimiä | Ei konsernitietoa löydetty — itsenäinen yhtiö; ks. HUOMIOT pienestä henkilöstömäärästä suhteessa laajaan toimialueeseen | Ei — curl palautti 14 804 merkkiä | https://ajokorttiverkosta.fi/ |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Drivers' Club | Yksi ainoa toimipiste Porvoossa — ei ketju, ei valtakunnallinen kattavuus | WebSearch: "Drivers' Club operates as a single location in Porvoo only... The search results do not indicate additional branch locations elsewhere in Finland"; PRH nimi "Autokoulu Drivers' Club Oy" |
| Liikenneopisto (yleisnimi) | Ei ole yksi yhtiö/ketju vaan yleisnimitys, jota käyttävät useat toisistaan riippumattomat paikalliset yhtiöt (Porin Liikenneopisto Ky, Euran Liikenneopisto, Nakkilan Liikenneopisto, Pirkanmaan Liikenneopisto jne.) — sama ansa kuin "Yksityiset katsastusasemat" batch 3:ssa | WebSearch: "Liikenneopisto refers to several affiliated driving schools operating in different cities... a network of driving schools" — ei yhtä yhteistä Y-tunnusta |
| Kissanmaan Autokoulu | Yhden kaupungin (Tampere) toimija — "Tampereen suurin ja suosituin autokoulu", ei valtakunnallinen | WebSearch: "Kissanmaan Autokoulu is Tampere's largest and most popular driving school" |
| Autokoulu Ajokortti Ky | Yhden toimipisteen yhtiö Lahdessa | WebSearch/PRH-viitteet: toimii vain Lahdessa |
| Autokoulu Safiiri | Osa Epic Autokoulu Oy:n konsernia (sama omistaja, Korona Invest) — tuplalaskisi saman ketjun kahdesti | WebSearch: "Konserniimme kuuluu myös Autokoulu Safiiri Oy sekä Liikenneterveys Oy" (Epic Autokoulun oma sivu) |

## HUOMIOT

- **Ala on konsolidoitunut pääomasijoittajavetoisesti.** Epic Autokoulu Oy on ostanut
  lukuisia paikallisia autokouluja viime vuosina ja jatkaa niitä alkuperäisillä
  paikallisnimillä aputoiminimenä (mm. Siilin Ajo-Opisto, Porvoon Auto-opisto, Nummelan
  Autokoulu, Salon Autokoulu, Vieremän Liikennekoulu, Jalasjärven Autokoulu, Varkauden
  Ajo-Opisto, Muhoksen Autokoulu, sekä 2018 ostettu kuusamolainen Tornbergin liikennekoulu
  ja 2024 ostettu turkulainen Liikennekoulu P. Mikola / Naantalin ja Maskun toimipisteet).
  Turun Sanomat (viitattu hakutuloksissa): "Kaksi isointa toimijaa [Epic ja CAP] hallitsee
  jo noin puolta alan markkinoista." Tämä kannattaa näyttää sivulla — moni paikkakunnan
  "oma" autokoulu on jo osa Epic- tai CAP-ketjua.
- **CAP-Group Oy:llä samanlainen rakenne**: kymmeniä paikallisia aputoiminimiä
  (Jyväskylän Autokoulu, Haagan Autokoulu jne.) saman Y-tunnuksen alla, 135 toimipistettä
  cap.fi:n oman toimipistesivun mukaan.
- **Antin Autokoulu -nimi on PRH:ssa kolmas kertaa käytössä.** Kaksi aiempaa
  "Antin Autokoulu Oy" -yhtiötä (0911169-8, lakannut 2005; 1921319-6, lakannut 2016)
  ovat päättyneet/muuttaneet nimeä ennen nykyistä, edelleen toiminnassa olevaa yhtiötä
  (2763674-6, rekisteröity 2016, website antinautokoulu.fi, tradeRegisterStatus
  "1" = rekisterissä). Tavallista nimikierrätystä yritysjärjestelyjen yhteydessä, ei
  punainen lippu — mutta tarkistettu erikseen, ettei nykyinen sivu viittaa lakanneeseen
  yhtiöön (ei viittaa: domain ja Y-tunnus 2763674-6 täsmäävät).
- **Ajokorttiverkosta/NetDriving on pieni yhtiö suhteessa ilmoitettuun kattavuuteen.**
  RG Driving Consulting Oy:llä oli vain 3 työntekijää (2024 tilinpäätös) ja 297 000 €
  liikevaihto, mutta sivusto listaa toimipaikkoja yhdeksällä eri alueella (Etelä-Pohjanmaa,
  Kanta-Häme, Keski-Suomi, Pirkanmaa, Pohjanmaa, Pohjois-Karjala, Pohjois-Pohjanmaa,
  Pohjois-Savo, Uusimaa) kymmenissä kunnissa. Malli muistuttaa opetuslupa-/
  sopimusyrittäjyysverkostoa (samantyyppinen kuin CAP:n oma "sopimusyrittäjyys") — pieni
  keskusyhtiö + verkosto paikallisia opettajia/yrittäjiä samalla brändillä. Ei ole
  peruste karsimiselle, mutta avoimuuspisteytyksessä kannattaa huomioida: muodollinen
  yhtiö on ohut suhteessa markkinoituun laajuuteen. Samalla Y-tunnuksella on myös
  toisenlaisia sivutoiminimiä ("RG Heppakauppa" hevoskauppa, "Autopesu Wash Me!"
  autopesu) — pieni monialayritys, mutta rekisteröity päätoimiala on oikein
  "Kuljettajakoulutus", toisin kuin muuttopalvelut-kategorian LogoTex-tapauksessa.
- Ei yhtään yhtiötä tarvinnut `--js`-renderöintiä.
