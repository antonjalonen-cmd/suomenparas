# Brändivarmistus — Siivouspalvelut, KULUTTAJASIIVOUS (BATCH 4)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py`:llä (curl; ei yhdellekään vahvistetulle
tarvinnut `--js`) + PRH:n avoindata-ytj-api v3 -rajapinta (nimihaku → businessId-vahvistus).
**Rajaus: nimenomaan kuluttajalle (yksityisasiakkaalle) suunnattu kotisiivous** — B2B-
kiinteistöpalvelujätit (SOL, RTK-Palvelu, ISS, L&T) tarkistettiin erikseen niiden OMILTA
sivuiltaan (ei hakutuloksista) leipätekstitasolla ennen karsimista, Risicum-opin mukaisesti.

## VAHVISTETUT (5)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `freska` | Freska | freska.fi | 3246808-9 (Freska Finland Oy, ent. Freska NewCo Oy) | Ei konsernitietoa löydetty — itsenäinen yhtiö; toimii myös Ruotsissa ja Norjassa | Ei — curl palautti 3 417 merkkiä | https://www.freska.fi/ |
| `kotirinki` | Kotirinki | kotirinki.fi | 1784293-3 (Kotirinki Oy) | Ei konsernitietoa löydetty — itsenäinen yhtiö; franchise-malli (paikalliset Kotirinki-yrittäjät) | Ei — curl palautti 4 249 merkkiä | https://kotirinki.fi/ |
| `keradur` | Keradur | keradur.fi | 2315098-4 (Keradur Oy, ent. Keradur Service Oy — nimenvaihto 17.3.2026) | Ei konsernitietoa löydetty — itsenäinen yhtiö | Ei — curl palautti 5 307 merkkiä | https://www.keradur.fi/ |
| `onni-kotisiivous` | Onni kotisiivous | onnion.fi | 2080120-0 (Med Group Oy) — "ONNI kotisiivous" on Med Group Oy:n rekisteröity aputoiminimi | **Med Group Oy** — laaja koti-/hoivapalvelukonserni, jolla on kymmeniä ONNI-aputoiminimiä (kotihoito, avustajapalvelut, lastenhoito, ONNI kotisiivous jne.); päätoimiala on ikääntyneiden/vammaisten kotihoito, ei siivous | Ei — curl palautti 22 988 merkkiä | https://www.onnion.fi/kotisiivous |
| `koti-puhtaaksi` | Koti Puhtaaksi | kotipuhtaaksi.fi | 2395527-2 (Sahera Koti Puhtaaksi Oy, ent. Porshsivo KY) | Ei konsernitietoa löydetty — itsenäinen yhtiö, perustettu 2011 | Ei — curl palautti 10 596 merkkiä | https://www.kotipuhtaaksi.fi/ |

## KARSITUT

| nimi | syy | todiste |
|---|---|---|
| SOL Palvelut | **Ei kuluttajatuotetta.** SOL Yhtiöiden oman `/palvelut/`-sivun navigaatiossa siivouspalvelujen alakohdat ovat: desinfiointisiivous, tehostettu siivous, elintarviketeollisuuden tuotantotilat, rakennussiivous, sairaalasiivous, hotellisiivous — kaikki B2B/laitos. Ei kotisiivous-nimikettä missään. | fetch_page.py `sol.fi/palvelut/`: siivouspalvelut-alavalikko sisältää vain institutionaalisia kohteita, ei kuluttajaa |
| RTK-Palvelu | **Ei kuluttajatuotetta.** `rtkpalvelu.fi/palvelut/siivouspalvelut/` listaa kohteet: liikekiinteistöt/toimistot, hotellit, liikennevälineet, koulut/päiväkodit, terveydenhuolto, urheilu-/vapaa-ajan kohteet, kaupat, teollisuus/logistiikka, "asuinkiinteistöt ja taloyhtiöt" (=taloyhtiöiden yhteistilat, ei yksityisasunto) | fetch_page.py `rtkpalvelu.fi/palvelut/siivouspalvelut/`: täysi kohdelista, ei yksityisasiakas/kuluttaja-nimikettä |
| ISS Palvelut | **Ei kuluttajatuotetta.** `fi.issworld.com/palvelut/siivouspalvelut` jakaa toimialat kolmeen: toimistot, teollisuus, julkinen sektori. Ei kuluttaja-/kotitalousosiota. | fetch_page.py `fi.issworld.com/palvelut/siivouspalvelut`: toimialat = Toimistot / Teollisuus / Julkinen sektori |
| Lassila & Tikanoja (L&T) | **Ei kuluttajatuotetta siivouksessa.** `/kotisiivous`-polku palauttaa 404. L&T:n oma "Kotitalouksien palvelut" -valikko sisältää vain: kodin jätehuolto, lajitteluohjeet, kodin viemärin avaus, lokakaivon tyhjennys — jätehuolto- ja viemäripalveluja, ei siivousta. | fetch_page.py `lt.fi/kotisiivous` → HTTP 404; `lt.fi`-navigaation "Kotitalouksien palvelut" -alavalikko ei sisällä siivousta |
| Topakat & Kätevät Oy | Vuoden 2024 kotityöpalveluyritys, mutta **pääkaupunkiseudun/Uudenmaan liiketoiminta siirtyi Kotirinki Oy:lle 1.5.2026** — perustaja palasi yksinyrittäjäksi. Ei enää itsenäinen ketju; osa on jo vahvistetun Kotirinki-rivin sisällä. | WebSearch: "Kotirinki Oy has acquired Topakat & Kätevät Oy's business operations in the capital region and Uusimaa... founder returned to operating as a sole entrepreneur in spring 2026" |
| Moppi / Moppi.com | Sovelluspohjainen siivoojan varauspalvelu, toiminta keskittyy pääasiassa Helsinkiin — ei todistettua monen kaupungin toimipisteverkostoa samassa mittakaavassa kuin viisi vahvistettua | WebSearch: "Moppi is a home cleaning service... operates in areas like Helsinki" |
| Clean Club / WE-Company / IsoJoo | Kaikki toimivat vain pääkaupunkiseudulla (Helsinki, Espoo, Vantaa, Kauniainen) — alueellisia toimijoita, ei valtakunnallisia | WebSearch: Clean Club "Helsinki, Vantaa, Espoo, Kauniainen"; WE-Company "Espoo, Helsinki, Kauniainen, Vantaa"; IsoJoo "Helsinki, Espoo, Vantaa" |
| Clean Home (cleanhome.fi) | Toimii Pohjanmaan alueella — alueellinen, ei valtakunnallinen | WebSearch: "Clean Home... operate in the Pohjanmaa (Ostrobothnia) region" |
| GLOW-Siivous | Toimii Jyväskylässä, Äänekoskella ja lähikunnissa — yhden seutukunnan toimija | WebSearch: "GLOW-Siivous provides home cleaning services in Jyväskylä, Ääneskoski and surrounding municipalities" |

## HUOMIOT

- **Ala on hyvin pirstaloitunut kuluttajapuolella.** Toisin kuin monissa aiemmissa
  kategorioissa, tässä isoimmat/tunnetuimmat brändit (SOL, ISS, RTK-Palvelu, L&T) ovat
  KAIKKI kiinteistöpalvelujättejä, joilla ei ole minkäänlaista kuluttajasiivous-tuotetta —
  tämä piti todeta jokaisen yhtiön omalta sivulta erikseen (ei hakutuloksesta), koska
  hakutulokset yksin eivät riittäneet varmistamaan poissaoloa (sama "en löytänyt ≠ ei ole"
  -riski kuin muissa kategorioissa).
- **Onni kotisiivous on aputoiminimi, ei erillinen yhtiö.** Med Group Oy on iso
  koti-/hoivapalvelukonserni (kymmeniä ONNI-brändejä: kotihoito, avustajapalvelut,
  lastenhoito jne.). Kuluttajasiivous on yksi liiketoimintalinja monen joukossa, ja osa
  sen asiakkuudesta tulee kuntien palveluseteleiden kautta (ei suoraa kuluttajamarkkinaa
  kuten Freska/Kotirinki). Tämä pitää näyttää sivulla samalla tavalla kuin OP Koti /
  Habita -federaatiorakenteet näytettiin batch 3:ssa.
- **Keradur-nimisekaannus, tärkeä löydös:** PRH:n suora nimihaku "Keradur" löytää
  ENSIN kuolleen, täysin eri alan yhtiön (Keradur Oy 0975595-2, lakannut 2014, jonka
  aputoiminimi oli "Hammaslääkäriasema Kerdent" — hammaslääkäriasema, ei siivous).
  Oikea, elossa oleva yhtiö on Keradur Oy 2315098-4 (ent. Keradur Service Oy,
  nimenvaihto 17.3.2026), löytyi vasta yhtiön oman sivun footerista Y-tunnuksen kautta.
  Muistutus: nimihaun ensimmäinen osuma ei aina ole oikea yhtiö — tarkista aina
  mainBusinessLine ja tradeRegisterStatus.
- **Kotirinki laajenee aktiivisesti** (osti Topakat & Kätevät Oy:n pääkaupunkiseudun/
  Uudenmaan liiketoiminnan 1.5.2026) — ~60 paikkakuntaa, 65+ palvelupistettä,
  franchise-malli ("yhdistää pienyrittäjän henkilökohtaisen palvelun, valtakunnallisen
  ketjun turvan"). Vahvin kandidaatti kategorian laajimmalle kattavuudelle.
- Ei yhtään yhtiötä tarvinnut `--js`-renderöintiä.
