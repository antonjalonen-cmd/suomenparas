# Brändivarmistus — Autokatsastus (BATCH 3)

Tarkistettu 18.7.2026 `pipeline/fetch_page.py` (curl, ei --js tarvittu yhdellekään) +
PRH YTJ v3 -rajapinta (`avoindata.prh.fi/opendata-ytj-api/v3/companies`). Kaikki Y-tunnukset
haettu ensin PRH:n nimihaulla, sitten vahvistettu `businessId`-hakulla (tradeRegisterStatus=1,
ei endDate = elossa).

## VAHVISTETUT (4 — ALLE 5–9 TAVOITTEEN, katso HUOMIOT)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `a-katsastus` | A-Katsastus | a-katsastus.fi | 1959705-4 (A-Katsastus Oy) | Tradeka (suomalainen monialakonserni) | Ei — curl toimii, 8700+ merkkiä | https://www.a-katsastus.fi |
| `k1-katsastajat` | K1 Katsastajat | k1katsastus.fi | 2046583-3 (K1 Katsastajat Oy) | **A-Katsastus-konsernin tytäryhtiö 12/2022 alkaen** (ostettu espanjalaiselta Applus-pörssiyhtiöltä) — jatkaa nimellään ja henkilöstöllään omana yhtiönä | Ei | https://www.k1katsastus.fi |
| `plus-katsastus` | Plus Katsastus | plus.fi | 2307508-0 (Plus Katsastus Oy) | 100 % suomalaisten yrittäjien omistama, riippumaton A-Katsastus/K1:stä | Ei | https://plus.fi |
| `dekra-katsastus` | DEKRA Katsastus | dekra-katsastus.fi | 2467455-2 (DEKRA Katsastus Oy, ent. Tähti Katsastus Oy) | Saksalainen DEKRA-konserni (26 maata, ~30M katsastusta/v maailmanlaajuisesti) | Ei | https://dekra-katsastus.fi |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Katsastus Plus | ei löytynyt tällä nimellä — sama yhtiö kuin "Plus Katsastus" (domain katsastusplus.fi ei enää vastaa, oikea domain plus.fi) | ehdokaslistan nimi oli epätarkka; PRH ja plus.fi vahvistavat yhtiön oikean nimen |
| Yksityiset katsastusasemat | ei ole yksittäinen yritys/ketju vaan yleisnimitys itsenäisille yksittäisasemille — ei täytä "oma valtakunnallinen ketju" -sääntöä | — |
| Suomen Autokatsastus | historiallinen nimi, nyt Ajovarma Oy:n (Y-tunnus 1033613-0) aputoiminimi — Ajovarma on itse A-Katsastus-konsernin sisaryhtiö (yhteinen portaali "A-Katsastus ja Ajovarma"), ei erillinen kilpailija | PRH: 1033613-0 "Ajovarma Oy" / "Suomen Autokatsastus Oy" aputoiminimenä; a-katsastus.fi otsikko "A-Katsastus ja Ajovarma" |
| Katsastajasi | alueellinen (Itä-Suomi + 2 asemaa pks:lla), 16 asemaa — ei valtakunnallinen kattavuus | katsastajasi.fi 404-sivun footer: "Katsastajasi.fi-katsastusasemat sijaitsevat pääasiassa Itä-Suomessa" |
| Suomen Katsastusasemat (Q-Katsastus, Katsastus Kovalainen, Koillismaan Autokatsastus) | 11 toimipistettä, syntyjään joensuulainen — omistaja vaihtui vasta 4.2.2026 saksalaiselle TÜV SÜD:lle; liian pieni + omistus juuri muuttunut | katsastusasemat.fi (Y-tunnus 3160745-4, SKA Holding Oy); Yle 4.2.2026: "Joensuulainen Suomen Katsastusasemat myytiin Saksaan – 11 asemaa" |
| Go-Katsastus | 7 asemaa keskittyneenä pääasiassa Uudellemaalle/Kanta-Hämeeseen + 1 Oulussa — ei valtakunnallinen kattavuus verrattuna A-Katsastuksen/K1:n/Plussan/DEKRAn kymmeniin toimipisteisiin | go-katsastus.fi: "Espoo, Helsinki, Riihimäki, Hyvinkää, Hämeenlinna, Vantaa, Oulu" |

## HUOMIOT

- **Omistuskeskittymä, tärkein löydös:** A-Katsastus osti K1 Katsastuksen joulukuussa 2022
  espanjalaiselta Applus-pörssiyhtiöltä. Traficomin mukaan näiden kahden yhteinen
  valtakunnallinen markkinaosuus oli 2019 ~40 %; kaupan jälkeen ne ovat Suomen kaksi
  suurinta katsastustoimijaa SAMAN omistajan alla. Autoliiton toimitusjohtaja kommentoi
  julkisesti huolensa kilpailun vähenemisestä (MTV Uutiset 25.12.2022, Autoliitto 22.12.2022).
  **Päätös tässä:** K1 Katsastajat pidetty listalla omana rivinä, koska sillä on oma Y-tunnus,
  oma henkilöstö ja oma asemaverkosto (ei sama operatiivinen yhtiö kuin A-Katsastus — toisin
  kuin esim. Avis/Budget-tapaus autovuokraamot-kategoriassa, jossa kyse on kirjaimellisesti
  samasta Y-tunnuksesta). Jos kategoria rakennetaan, omistussuhde ON pakko näyttää sivulla
  yhtä näkyvästi kuin Effortia/sähkövertailu-tapauksessa.
- **Hiljainen fuusio #2:** HelppoKatsastus osti… tarkemmin PLUS KATSASTUS OSTI HelppoKatsastuksen
  2025 ("Vuonna 2025 tapahtui luonnollinen seuraava askel, kun Plus Katsastus osti
  HelppoKatsastuksen"). Kaikki entiset HelppoKatsastus-asemat toimivat nyt Plus Katsastus
  -nimellä. HelppoKatsastus Oy (Y-tunnus 2184450-1) on siis elossa PRH:ssa mutta ei enää
  itsenäinen kilpailija.
- **Hiljainen fuusio #3:** DEKRA Katsastus Oy:n aputoiminimi PRH:ssa on "Tähti Katsastus Oy" —
  DEKRA on siis ostanut/nimennyt uudelleen suomalaisen Tähti Katsastus -ketjun. DEKRA myös
  laajentaa aktiivisesti: "DEKRA Katsastus laajenee Veteliin ja Seinäjoelle" -uutinen kertoo
  vasta ostaneensa Perhonjokilaakson Katsastus Oy:n ja Etelä-Pohjanmaan Katsastus Oy:n
  liiketoiminnan — ala konsolidoituu koko ajan lisää.
- **Kategoria jää alle 5–9 tavoitteen (4 vahvistettua).** Traficomin katsastusalan
  tilannekatsauksen mukaan toimipaikkoja on 561 (2024 lop.), mutta suurin osa on joko
  A-Katsastus/K1/Plus/DEKRA-verkoston asemia tai selkeästi alueellisia pienketjuja/yksittäisiä
  asemia jotka eivät täytä "aidosti valtakunnallinen" -sääntöä. Anton/rakentaja päättää:
  rakennetaanko 4 yhtiön kategoria (poikkeus 5–9 säännöstä, dokumentoitu syy) vai jätetäänkö
  `autokatsastus` rakentamatta tällä kierroksella.
- Katsastushintojen keskiarvo kevät 2026: 50,06 € ilman ennakkovarausta, päästömittaus
  78,15 € (Traficom, tilannekatsaus 2025/2026-uutinen) — hyödyllinen konteksti hinta-avoimuuden
  pisteytykseen jos kategoria rakennetaan.
