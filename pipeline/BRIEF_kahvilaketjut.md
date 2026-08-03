# Ekstraktio-ohje: kahvilaketjut

Vertical: `kahvilaketjut`. Tarkista joka yhtiölle alla olevat 7 kriteeriä.

## Yhtiöt ja URL:t

| slug | nimi | pääsivu |
|---|---|---|
| espresso-house | Espresso House | https://espressohouse.com/ |
| roberts-coffee | Robert's Coffee | https://robertscoffee.com/ |
| arnolds | Arnolds | https://arnolds.fi/ |
| fazer-cafe | Fazer Café | https://fazer.fi/fazer-cafe/ |
| picnic | Picnic | https://picnic.fi/ |
| coffee-house | Coffee House | https://coffeehouse.fi/ |

## Kriteerit (score_rules.py-avaimet)

1. **hinnat_esilla** (25 p) — Onko kahvila-/ruokatuotteiden hinnat esillä verkkosivustolla? "kyllä" jos hintalista löytyy ilman kirjautumista, sovellusta tai ravintolaan menemistä. Hakemisto + hinta riittää.

2. **allergeenit_esilla** (20 p) — Löytyykö allergeeni- ja/tai ravintosisältötiedot tuotekohtaisesti verkkosivustolla? Ei riitä pelkkä yleinen maininta allergeeneistä — tarvitaan tuotekohtaiset listat tai "näytä lisätiedot" -toiminto sivustolla.

3. **kahvin_alkupera** (15 p) — Kerrotaanko kahvin alkuperä (maa/alue/viljelijät) tai onko ketjulla Reilu kauppa -sertifiointi, UTZ, Rainforest Alliance tai muu vastaava sitoumus mainittu verkkosivustolla?

4. **ravintolat_ja_aukioloajat** (15 p) — Löytyykö toimipisteet ja aukioloajat helposti verkkosivustolta ilman kirjautumista? Kartta tai lista riittää; tarkista myös yksittäisen toimipisteen sivu.

5. **y_tunnus_esilla** (10 p) — Näkyykö Y-tunnus tai vastaava yritystunnus (esim. org.nr.) selvästi jollain sivuston sivulla (footer, yhteystiedot, tietosuojaseloste)?

6. **riippumaton_arvio** (10 p) — Onko sivustolla linkki tai maininta riippumattomaan arvioivaan lähteeseen (esim. Tripadvisor-pistemäärä, lehtiarvostelu, Oiva-raportti linkitettynä)? Oiva-raportti-linkki lasketaan.

7. **kanta_asiakasohjelma_kerrottu** (5 p) — Onko sivustolla kuvaus kanta-asiakasohjelmasta tai mobiilisovelluksesta (edut, miten liittyä)?

## Erityishuomiot

- **Fazer Café** (fazer.fi): Sivusto on evästemuuri. Merkitse kriteerit, joihin et pääse evästesuostumuksen vuoksi, arvoksi "ei mitattavissa" (ÄLÄ merkitse "ei"). Yritä silti saada Oiva-raportit, aukioloajat ja perusinfo jos ne löytyvät staattisesta HTML:sta.
- **Coffee House** (coffeehouse.fi): Ohjautuu raflaamo.fi-alustalle. Mittaa sen, mitä löydät coffeehouse.fi:n kautta. Jos raflaamo-sivu näyttää Coffee Housen tiedot, ne lasketaan.
- **Espresso House**: pääsivu on fi.espressohouse.com (ei /fi/ -polku). Käytä fi.espressohouse.com:ia.
- **Y-tunnus**: Arnolds = 0864440-9 (Hermen Oy), Espresso House FI = 2663296-2, Picnic = 0789907-1, Fazer = 0202669-3. Robert's Coffee ja Coffee House: etsi sivustolta, merkitse "ei löydetty" jos ei näy.
- Botti-esto tai evästemuuri = "ei mitattavissa", EI "ei ole". Älä keksi tietoja.
- Oiva-raportti-linkki = riippumaton_arvio kyllä.

## Extract JSON -rakenne

```json
{
  "slug": "espresso-house",
  "nimi": "Espresso House",
  "domain": "espressohouse.com",
  "fetched_ok": ["https://fi.espressohouse.com/", "https://fi.espressohouse.com/menu/"],
  "hinnat_esilla": "kyllä",
  "hinnat_esilla_lähde": "HAVAINTO: Menu-sivulla listattu tuotteet hinnoilla, esim. 'Caramel Latte 3,90 €'",
  "allergeenit_esilla": "ei",
  "allergeenit_esilla_lähde": "Allergeeni-sivulla yleinen ohje mutta ei tuotekohtaisia listoja",
  "kahvin_alkupera": "kyllä",
  "kahvin_alkupera_lähde": "Vastuullisuus-sivulla: 'Kaikki kahvimme ovat Rainforest Alliance -sertifioituja'",
  "ravintolat_ja_aukioloajat": "kyllä",
  "ravintolat_ja_aukioloajat_lähde": "HAVAINTO: 'Löydä lähin kahvila' -kartta löydettävissä etusivulta",
  "y_tunnus_esilla": "kyllä",
  "y_tunnus_esilla_lähde": "Tietosuojaseloste: 'Espresso House Finland Oy, Y-tunnus 2663296-2'",
  "riippumaton_arvio": "kyllä",
  "riippumaton_arvio_lähde": "HAVAINTO: Oiva-raportti linkitettynä etusivulla",
  "kanta_asiakasohjelma_kerrottu": "kyllä",
  "kanta_asiakasohjelma_kerrottu_lähde": "HAVAINTO: 'Fika Club' -sovellus kuvattu etusivulla eduilla ja liittymisohjeella"
}
```
