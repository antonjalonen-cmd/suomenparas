# Brändivarmistus — Autovuokraamot (BATCH 3)

Tarkistettu 18.7.2026 `pipeline/fetch_page.py` (curl; Hertz ja Avis/Budget vaativat --js,
muut eivät) + PRH YTJ v3 -rajapinta. Kansainväliset merkit toimivat Suomessa paikallisen
lisenssinhaltijan/franchise-yhtiön kautta — Y-tunnus on aina paikallisen operaattorin, ei
ulkomaisen emoyhtiön.

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja/operaattori | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `hertz` | Hertz | hertz.fi | 0744711-2 (First Rent A Car Finland Oy Ab, ent. Polarpoint Oy Ab) | Suomen Hertz-lisenssinhaltija | **Kyllä** — curl saa vain 77 merkkiä (evästekuori), --js antaa 21 000+ merkkiä | https://www.hertz.fi |
| `avis` | Avis | avis.fi | 2346469-2 (Helkama Rent Oy) | Suomen Avis/Budget/Payless-lisenssinhaltija | **Kyllä** — curl palauttaa tavaamattoman/pakatun sisällön, --js toimii | https://www.avis.fi |
| `sixt` | Sixt | sixt.fi | 2275518-0 (Transporent Oy, ent. Veho Rent Oy Ab) | Suomen Sixt-lisenssinhaltija (Veho-konsernin autovuokrausyhtiö) | Ei | https://www.sixt.fi |
| `europcar` | Europcar | europcar.fi | 0109269-9 (Interrent Oy, ent. VW-Rent Oy) | Osa kansainvälistä Europcar Mobility Group -konsernia (osti Interrentin 2019) | Ei | https://www.europcar.fi |
| `scandia-rent` | Scandia Rent (MABI Mobility) | scandiarent.fi | 2509794-5 (Mabi Mobility Oy, ent. Scredo Oy) | Ruotsalainen MABI Mobility AB / Hedin Mobility Group | Ei | https://scandiarent.fi |
| `green-motion` | Green Motion | greenmotion.fi (→ greenmotion.com/fi) | 1837195-0 (Silver Cars Rental Oy, ent. Rentella Oy — Rovaniemen toimipisteen operaattori, vahvistettu Finder.fi:n kautta) | Kansainvälinen Green Motion International -franchisejärjestelmä, Suomen franchise-yrittäjät | Ei | https://greenmotion.fi |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Budget | **SAMA YHTIÖ kuin Avis** — molemmat ovat Helkama Rent Oy:n (Y-tunnus 2346469-2) lisensoimia brändejä. Kahden pistoon listaaminen tuplaisi saman yhtiön kahdeksi kilpailijaksi (sama ansa kuin Saunalahti=Elisa, Moi=DNA) | LinkedIn: "Helkama Rent Oy / Avis and Budget Rent a Car lic."; sähköpostiosoite reservations@avisbudget.fi; useat yritysrekisterit (Fonecta, Finder, Asiakastieto) vahvistavat saman Y-tunnuksen molemmille brändeille |

## HUOMIOT

- **Tärkein löydös — Avis = Budget Suomessa.** Helkama Rent Oy operoi Suomessa kolmea
  kansainvälistä brändiä (Avis, Budget, Payless) samalla Y-tunnuksella, samalla
  varausjärjestelmällä (yhteinen sähköpostidomain avisbudget.fi) ja osittain samalla
  kalustolla. Tämä ei ole sama tilanne kuin autokatsastus-kategorian A-Katsastus/K1
  (eri Y-tunnukset, eri asemaverkosto) — tässä on kirjaimellisesti yksi yhtiö kahden
  ikkunalasin takana. Vain Avis otettu mukaan (tunnetumpi globaali brändi); Budget
  jätetty pois tuplauksena, ei hiljaisena poistona — merkitään HUOMIOna sivulle jos
  rakennetaan.
- **Scandia Rent -> MABI Mobility -nimenmuutos.** scandiarent.fi:n otsikko on nyt
  "MABI Mobility", ei enää "Scandia Rent". Yli 70 vuotta vanha suomalainen ketju
  (perustettu Seinäjoella) on ruotsalaisen Hedin Mobility Groupin omistama MABI Mobility
  AB:n Suomen yksikkö. Domain ja asiakaskunnan tuttu nimi ("Scandia Rent") säilyy
  toistaiseksi sivustolla rinnakkain, joten mittaus-URL toimii, mutta rakentajan
  kannattaa käyttää nimeä "Scandia Rent (MABI Mobility)" ettei asiakas hämmenny.
- **Europcar Finland = Interrent Oy** (ent. VW-Rent Oy) — Europcar Mobility Group osti
  paikallisen lisenssinhaltijan Interrentin vuonna 2019. Ei enää itsenäinen suomalainen
  yritys, mutta ei kaksoislaskentaa (Europcar ei esiinny muuna candidaattina listalla).
- **Green Motion pienin toimija:** vain 5 pistettä (Helsinki-Vantaa, Helsinki Hotel Valo,
  Oulu, Rovaniemi, Kittilä, Ivalo) — painottuu lentokentille/Lappiin. Rajatapaus
  "aidosti valtakunnallinen" -säännön suhteen, mutta hyväksytty koska palvelee kaikkia
  suurimpia lentoasemia ja on globaalisti tunnettu franchise-brändi jota suomalaiset
  aidosti käyttävät (ei paikallinen yksittäisyritys). Y-tunnus varmistettu vain
  Rovaniemen toimipisteen operaattorille (Silver Cars Rental Oy / Rentella Oy) kolmannen
  osapuolen rekisterin (Finder.fi) kautta — PRH-nimihaku "Green Motion" ei löytänyt
  suoraa osumaa koska yhtiö toimii suomenkielisellä nimellä. Rakentajan syytä varmistaa
  vielä greenmotion.fi:n footerista sama Y-tunnus ennen julkaisua.
- Kaikki kuusi toimivat yleisesti tunnetuilla kansainvälisillä hinnoilla/ehdoilla — hyvä
  kategoria hinta-avoimuuden pisteytykseen (esim. näkyykö hinta ennen tietojen antamista,
  peruutusehdot, piilokulut).
