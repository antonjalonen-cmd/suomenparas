# Brändivarmistus — Optikot (BATCH 3)

Tarkistettu 18.7.2026 `pipeline/fetch_page.py` (curl, ei --js tarvittu yhdellekään — kaikki
palauttivat aidon leipätekstin ilman JS-renderöintiä) + PRH YTJ v3 -rajapinta.

## VAHVISTETUT (5)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `specsavers` | Specsavers | specsavers.fi | 2006084-4 (Specsavers Finland Oy, ent. Tähti Optikko Group Oy) | Kansainvälinen Specsavers-franchisejärjestelmä (brittiläis-tanskalainen alkuperä) | Ei | https://www.specsavers.fi |
| `instrumentarium` | Instrumentarium | instrumentarium.fi (→ instru.fi) | 1789727-2 (Instru Optiikka Oy) | EssilorLuxottica (globaali optiikkajätti, osti GrandVisionin 2021) | Ei | https://www.instru.fi |
| `silmaasema` | Silmäasema | silmaasema.fi | 2627773-7 (Silmäasema Oy / Silmäasema Oyj) | Coronaria (omistanut 2020 alkaen) — **KAUPAN ALLA**, ks. HUOMIOT | Ei | https://www.silmaasema.fi |
| `fenno-optiikka` | Fenno Optiikka | fennooptiikka.fi | 2205389-1 (Fenno Optical Oy) | Suomalainen, franchise-yrittäjävetoinen ketju (Rodenstock-tuotekumppanuus, ei omistus) | Ei | https://fennooptiikka.fi |
| `synsam` | Synsam | synsam.fi | 2446347-2 (Synsam Group Finland Oy) | Ruotsalainen Synsam Group (pörssiyhtiö) | Ei | https://www.synsam.fi |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| Nissen | **SAMA YHTIÖ kuin Instrumentarium** — molemmat ovat Instru Optiikka Oy:n (Y-tunnus 1789727-2) brändejä Suomessa (kolmas on Keops). Kahden pistoon listaaminen tuplaisi saman EssilorLuxottica-omisteisen ketjun kahdeksi kilpailijaksi | Fi.Wikipedia + instruoptiikka.fi/tietoa-meista: "Instru Optiikka Oy... toimii Suomessa Instrumentarium-, Nissen- ja Keops-myymäläbrändeillä"; nissen.fi ja instru.fi jakavat identtisen verkkokauppa-alustan ja navigaatiorakenteen |

## HUOMIOT

- **Tärkein löydös — Instrumentarium = Nissen (= Keops).** Instru Optiikka Oy pyörittää
  kaikkia kolmea kuluttajabrändiä yhden Y-tunnuksen alla, osana EssilorLuxotticaa (osti
  GrandVisionin 2021, joka syntyi Pearle Europen ja GrandVisionin fuusiosta 2010 — ketju
  jonka nimi "Instrumentarium" vapautui kun alkuperäinen pörssiyhtiö Instrumentarium Oyj
  lakkasi 2004 General Electricin ostettua sen). Vain Instrumentarium mukaan (suurempi,
  historiallisesti tunnetumpi brändi Suomessa); Nissen jätetty pois tuplauksena samaan
  tapaan kuin Avis/Budget autovuokraamot-kategoriassa.
- **Silmäasema on kaupan kesken heinäkuussa 2026 — merkittävä ajoitusriski.**
  Terveystalo allekirjoitti 8.6.2026 sopimuksen ostaakseen Silmäaseman koko osakekannan
  (~574 M€, josta 275 M€ käteisellä + loput 36,5 M osakkeella). Nykyinen omistaja Coronaria
  (omistanut 2020 alkaen) muuttuu kaupan toteutuessa Terveystalon suurimmaksi
  osakkeenomistajaksi (~15,1 %). Kauppa nostaisi Terveystalon silmäterveyden
  markkinajohtajaksi. **Tätä ei ole vielä toteutettu** (viittaus "kaupan toteutuessa") —
  todennäköisesti odottaa vielä kilpailuviranomaisen hyväksyntää. Jos `optikot` rakennetaan
  ennen kaupan sulkeutumista, sivulle on merkittävä "Silmäasema on ostettavana Terveystalolle
  (sopimus 8.6.2026, ei vielä toteutunut)" — muuten julkaistava tieto vanhenee saman tien.
  Tämä on täsmälleen sama ansa kuin Väre/Helen ja Diacor/Terveystalo aiemmin: brändi näyttää
  itsenäiseltä mutta omistus on jo muuttumassa.
  HUOM myös: Terveystalo esiintyy queued-listalla ehdokkaana `yksityislaakarit`- ja
  `hammaslaakarit`-kategorioissa (BATCH 3/4) — jos molemmat rakennetaan, ristiinomistus
  Terveystalo↔Silmäasema pitää disclosuroida kaikilla sivuilla.
- **Synsam-Mehiläinen-yhteistyö ei ole omistussuhde.** Hakutulos mainitsi "Most Synsam
  stores also offer eye doctor services through Mehiläinen" — tämä on palvelukumppanuus
  (silmälääkärin vastaanotto samassa tilassa), ei omistusta. Ei vaadi poistoa, mutta syytä
  mainita transparenssikohdassa jos silmälääkäripalvelun tarjoaja on relevantti kriteeri.
- **Fenno Optiikka** vaikuttaa aidosti riippumattomalta suomalaiselta ketjulta
  (franchise-yrittäjämalli, "Haemme yrittäjiä" -sivu), tuotekumppanuus saksalaisen
  Rodenstockin kanssa on vain linssitoimittajasuhde, ei omistus.
- Kaikki 5 vahvistettua yhtiötä ovat aidosti valtakunnallisia (kymmeniä–yli 70 myymälää),
  kategoria täyttää 5–9 tavoitteen juuri ja juuri alarajalla. Jos Nissen olisi laskettu
  erikseen, näyttäisi virheellisesti 6 yhtiöltä.
