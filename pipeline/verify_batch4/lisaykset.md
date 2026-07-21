# Lisäysten varmistus — 2 nimeltä pyydettyä yritystä (BATCH 4)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (curl; ei kummallekaan tarvittu `--js` —
molemmat palauttivat täyden leipätekstin suoraan) + PRH:n YTJ v3 -rajapinta
(`avoindata.prh.fi/opendata-ytj-api/v3/companies`, aina `businessId`-haulla vahvistettu).

## 1. Amazed (amazed.fi) → ehdotettu kategoria `pakohuoneet`

| kenttä | tieto |
|---|---|
| nimi | aMazed Games |
| domain | amazed.fi (→ www.amazed.fi) |
| y_tunnus (PRH-vahvistettu) | **2716466-2** — "aMazed Games Oy", rekisteröity 2015-10-15, `tradeRegisterStatus: "1"` (rekisterissä), `companySituations: []` (ei konkurssia/selvitystilaa) — **elää**. VAT-tunnus sivun footerissa (FI27164662) täsmää tähän Y-tunnukseen. |
| omistaja | Itsenäinen, perustajaomisteinen (aMazed Games Oy). Aputoiminimiä PRH:ssa: Prison Dinner, Haunted Dinner, aMazed Escape Room Helsinki, aMazed Escapes, Alternate Reality Lab — kaikki saman Y-tunnuksen alla, ei erillisiä yhtiöitä. |
| **kaupunkimäärä** | **1 — VAIN Helsinki (Kamppi).** Yrityksen oma etusivu: *"Kaikki pelit yhdessä toimipisteessä Kampissa Helsingin keskustassa, helppo tulla."* FAQ vahvistaa saman: *"Kampin toimipisteessä on sesongista riippuen 5–6 peliä."* Osoite: Köydenpunojankatu 4 A, 00180 Helsinki. **EI löytynyt mainintaa toisesta kaupungista millään sivulla (etusivu, hinnasto, FAQ, ehdot).** |
| JS-vaatimus | **Ei.** curl palautti täyden leipätekstin suoraan (etusivu 2 332 merkkiä, FAQ 7 915 merkkiä, hinnasto 2 287 merkkiä, ehdot 3 326 merkkiä) — ei tarvinnut `--js`-renderöintiä. |
| hinta alkaen | 27,50 €/hlö (6 hengen ryhmä) — 52,50 €/hlö (2 hengen ryhmä), sis. 13,5 % alv. Sunnuntaisin 2–3 hlö 140 €/ryhmä. |
| muuta | Alle 10-vuotiaat ilmaiseksi aikuisen seurassa (min. veloitus 95 €). Opiskelija-alennus (100 €/3–6 hlö, ma–to tiettyihin aikoihin). Varauskalenteri verkossa ("BOOK NOW" → suora varaus). Laaja FAQ, englanniksi ja suomeksi. |
| ehdotettu mittaus-URL | https://www.amazed.fi/ |

**HUOMIO — ristiriita kategorian rajaukseen:** `pakohuoneet`-kategoria (ks.
`pipeline/verify_batch4/pakohuoneet.md` ja `data/pakohuoneet.json`) on nimenomaisesti
rajattu **monikaupunkisiin** pakohuoneketjuihin — kategorian oma lead-teksti sanoo
"Pisteytimme {n} usealla paikkakunnalla toimivaa pakohuoneyritystä" ja huomautus selittää
miksi yhden kaupungin toimijat (mm. **Amazed Games** nimeltä mainittuna) on jo karsittu
listalta juuri tästä syystä: *"EXITE, Amazed Games, Pakomielle, Huone Escapes, Escape Room
Helsinki / Pakohuone Tarina — Kaikki yhden kaupungin (Helsinki tai Espoo) toimijoita — ei
monikaupunkisia."*

Amazed elää, Y-tunnus vahvistettu, sivusto toimii hienosti ilman JS:ää — mutta se on
todistettavasti **yhden toimipisteen yritys**, ei ketju. Jos se lisätään nykyiseen
kategoriaan sellaisenaan, kategorian oma rajaus (ja sen selittävä teksti) pitää kirjoittaa
uusiksi, tai Amazed pitää merkitä poikkeukseksi omalla perusteellaan. **Päätös Antonille:**
(a) laajenna kategorian rajaus kattamaan myös vahvat yhden kaupungin toimijat ja päivitä
lead/notes-teksti vastaavasti, TAI (b) pidä kategoria monikaupunkisena ja jätä Amazed pois
tästä listasta huolimatta omistajan pyynnöstä. En lisännyt sitä `data/pakohuoneet.json`:iin
odottaessani tätä päätöstä.

---

## 2. Eversheds Sutherland Helsinki → ehdotettu kategoria `lakifirmat`

| kenttä | tieto |
|---|---|
| nimi | Eversheds Sutherland (Suomen toimisto) |
| domain | eversheds-sutherland.com/fi/finland (huom: **eversheds-sutherland.fi ei vastaa, HTTP 000** — väärä domain-oletus alkuperäisessä pyynnössä); sähköposti käyttää yhä vanhaa `eversheds.fi`-domainia |
| y_tunnus (PRH-vahvistettu) | **2556202-6** — "Eversheds Asianajotoimisto Oy" (ent. Asianajotoimisto JB Eversheds Oy / Asianajotoimisto Bützow), rekisteröity 2013-07-04, `tradeRegisterStatus: "1"`, `companySituations: []` — **elää**. Osoite PRH:ssa (Fabianinkatu 29 B, 00100 Helsinki) täsmää tarkalleen toimiston omalla sivulla ilmoitettuun osoitteeseen. |
| omistus/verkostorakenne | **Kansainvälinen ketju, ei yksi globaali yhtiö.** Sivuston oma juridinen huomautus: *"Eversheds Sutherland is the name and brand under which the members of Eversheds Sutherland Limited (...) and their respective controlled, managed and affiliated firms (...) provide legal (...) services (...). The use of the name Eversheds Sutherland (...) does not imply that the Eversheds Sutherland Entities are in a partnership or are part of a global LLP."* Suomen toimisto (Eversheds Asianajotoimisto Oy, Y-tunnus 2556202-6) on siis **oikeudellisesti ja taloudellisesti itsenäinen suomalainen osakeyhtiö**, joka toimii kansainvälisen Eversheds Sutherland -brändiverkoston jäsenenä — sama rakenne kuin esim. OpusLex-jäsentoimistoilla `lakifirmat.md`:n karsinnassa (Kontturi & Co), mutta huomattavasti suurempi ja tunnetumpi kansainvälinen brändi. Nimike **"Asianajotoimisto"** = Asianajajaliiton valvoma, sama kategoria kuin Lindblad nykyisellä listalla. |
| toimipisteet | **Vain 1 Suomessa: Helsinki** (Fabianinkatu 29 B). Ei muita Suomen-toimipisteitä sivustolla mainittu. |
| kuluttajat vai vain yritykset | **Palvelee molempia, mutta painotus on selvästi yritys-/varakkaat yksityisasiakkaat, ei tavallinen kuluttaja.** Palveluluettelossa on oma kohta **"Yksityishenkilöjuridiikka" (Private Client)** — leipäteksti: *"Whether you're a family business or a high net worth individual, we can provide you with dedicated lawyers (...) family law and tax to inheritance and succession matters (...) With many years' experience advising **wealthy private clients** (...)"* — eli testamentit, avioehdot, perinnönjako, mutta kohderyhmänä nimenomaisesti perheyritykset ja varakkaat yksityishenkilöt, ei massakuluttaja. Etusivun oma CTA on suunnattu yrityksille: *"Hanki **yrityksesi** tarvitsemaa juridista tukea."* **Ei mitään julkista hinnastoa, ei kiinteitä dokumenttihintoja, ei itsepalvelua** — täysin toimeksianto-/tarjouspyyntöpohjainen malli, päinvastainen ääripää verrattuna esim. Lakitieen tai Aatokseen listalla. |
| JS-vaatimus | **Ei.** curl palautti täyden leipätekstin sekä englanniksi että suomeksi (esim. `/fi/finland` 5 990 merkkiä, `/en/finland/capabilities/services/private-client` 5 138 merkkiä) suoraan — mutta **sisänavigaatio (linkkien href-polut) on rakennettu clientside-reitityksellä**, eivät näy raa'assa HTML:ssä ilman `--js`-renderöintiä. Itse sisältösivujen leipäteksti ei vaadi JS:ää, ainoastaan oikeiden alasivupolkujen löytäminen vaati `--js --raw` -renderöinnin kertaalleen navigaatiorakenteen selvittämiseksi. |
| ehdotettu mittaus-URL | https://www.eversheds-sutherland.com/fi/finland (suomenkielinen etusivu; toimistosivu https://www.eversheds-sutherland.com/en/finland/offices/helsinki) |

**HUOMIO — mittarikelpoisuus:** kategorian omat mittarit (hinnat julkisesti esillä,
esimerkkihinta €) tuottavat Eversheds Sutherlandille todennäköisesti hyvin matalan
läpinäkyvyyspisteen — ei julkaistuja hintoja, ei UKK-osiota, ei chat-tukea, ei
mobiilisovellusta löytynyt. Tämä ei ole mittausvirhe vaan aito ero: kyseessä on
kansainvälinen Big Law -toimisto, jonka liiketoimintamalli (räätälöity toimeksianto,
tuntilaskutus sopimuksen mukaan) on rakenteellisesti erilainen kuin listan nykyisillä
kuudella toimijalla. Sopii silti kategoriaan sisällöllisesti (suomalainen, kuluttajille
osittain palveleva asianajotoimisto), mutta tulos kannattaa kehystää sivulla samalla
tavalla kuin Minilexin liidipohjainen malli on jo kehystetty (`lakifirmat.md`:n HUOMIOT).

---

## Yhteenveto molemmista

- **Amazed**: elää, Y-tunnus 2716466-2 vahvistettu, ei JS-vaadetta — mutta on todistettavasti
  yhden kaupungin (Helsinki/Kamppi) yritys, mikä on ristiriidassa `pakohuoneet`-kategorian
  nykyisen monikaupunki-rajauksen kanssa (jossa Amazed on jo kerran nimeltä karsittu tästä
  samasta syystä). Ei lisätty `data/pakohuoneet.json`:iin — odottaa Antonin päätöstä
  rajauksen laajentamisesta.
- **Eversheds Sutherland**: elää, Y-tunnus 2556202-6 (Eversheds Asianajotoimisto Oy)
  vahvistettu, yksi toimipiste Helsingissä, kansainvälisen ketjun itsenäinen suomalainen
  jäsenyhtiö, palvelee sekä yrityksiä että varakkaita yksityisasiakkaita (Private Client
  -palvelu) mutta ei tavallista kuluttajaa massamielessä; ei julkista hinnoittelua. Sopii
  kategoriaan, mutta pisteytyy todennäköisesti heikosti läpinäkyvyysmittareilla — kehystä
  sivulla kuten Minilex.
