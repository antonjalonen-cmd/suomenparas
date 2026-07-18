# Brändivarmistus — Kiinteistönvälittäjät (batch 3)

Mittauspäivä tälle varmistukselle: 18.7.2026. Kaikki haut `pipeline/fetch_page.py`:llä
(curl, ei JS:ää tarvittu). Y-tunnukset vahvistettu PRH:n avoindata-ytj-api v3:sta
nimihaulla + businessId-haulla.

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `kiinteistomaailma` | Kiinteistömaailma | kiinteistomaailma.fi | 0804835-9 (Kiinteistömaailma Oy, Helsinki) | Ei konsernitietoa löydetty tällä haulla | Ei — curl palautti 8 528 merkkiä (n. 600 välittäjää, kymmeniä paikkakuntia A–Y) | https://www.kiinteistomaailma.fi/ |
| `huoneistokeskus` | Huoneistokeskus | huoneistokeskus.fi | 1831315-2 (Huoneistokeskus Oy, Helsinki). **Sisältää nyt entisen SKV:n — ks. KARSITUT.** | Realia-konserni (Huoneistokeskus + entinen SKV yhdistyivät Realia Groupiksi jo 2006; nyk. Retta-brändi mainittu sivustolla "Rettan asiantuntijapalvelut") | Ei — curl palautti 7 577 merkkiä (yli 30 toimistoa) | https://huoneistokeskus.fi/ |
| `opkoti` | OP Koti | op-koti.fi | **Ei yhtä läpäisevää Y-tunnusta.** OP Koti on n. 19 alueellisen "OP Koti X Oy LKV" -yhtiön federaatio, kukin paikallisen osuuspankin omistuksessa, yhteisen OP Ryhmä -brändin ja op-koti.fi-sivuston alla. PRH-vahvistetut esimerkit: OP Koti Uusimaa Oy LKV (0821497-8, Helsinki), OP Koti Itä-Suomi Oy LKV (0595450-8, Kuopio), OP Koti Pohjoinen Oy LKV (3185846-4, Oulu), OP Koti Varsinais-Suomi Oy LKV (0911093-5, Turku) — kaikki status=rekisterissä. | OP Ryhmä (osuuspankkikonserni) | Ei — **op-koti.fi on oma domain, EI sama kuin JS-rajoitteinen op.fi** (huomioitu pankit-kategorian blokkeri ei koske tätä) — curl palautti 4 009 merkkiä täyttä sisältöä | https://op-koti.fi/ (100+ paikkakuntaa, 500 välittäjää) |
| `remax` | RE/MAX | remax.fi | 2019179-9 (REF Real Estate Franchises Oy, Helsinki — suomalainen master-franchisoija, virallinen kotisivu www.remax.fi rekisteröity PRH:n tietoihin) | Kansainvälinen RE/MAX-franchise; sivun oma teksti: "Each office independently owned and operated" — 20 toimistoa ovat itsenäisiä franchise-yrittäjiä | Ei — curl palautti 6 289 merkkiä (20 kaupunkia, 450 välittäjää) | https://remax.fi/ |
| `habita` | Habita | habita.com/fi | 0980183-2 (Habita Finland Oy, Helsinki). **Sama alueellinen rakenne kuin OP Koti**: yksittäiset kaupunkitoimistot ovat erillisiä Oy:itä (esim. Turun Habita Oy, Espoon Habita Oy, Vantaan Habita Oy) saman Habita-brändin alla. | Ei konsernitietoa löydetty (kansainvälinen toimisto­verkosto 30+ maassa mainitaan sivulla) | Ei — curl palautti 7 025 merkkiä (2 094 kohdetta Suomessa + kv-toimistoja) | https://www.habita.com/fi |
| `bolkv` | Bo LKV | bo.fi | 2796763-3 (Bo LKV Oy, alun perin Turku). Kaikki kaupunkitoimistot (Helsinki, Espoo, Vantaa, Tampere, Turku, Pori/Uusikaupunki, Jyväskylä, Mikkeli, Kuopio, Oulu, Levi, Ylläs, Porvoo, Lahti) ovat **saman yhtiön** rekisteröityjä aputoiminimiä — poikkeaa OP Kodista/Habitasta siinä, että tämä on yksi juridinen toimija. | Ei konsernitietoa löydetty | Ei — curl palautti 8 984 merkkiä (10 kasvukeskusta, kattaa Etelä-, Länsi-, Keski-, Itä- ja Pohjois-Suomen) | https://bo.fi/ |

## KARSITUT

- **SKV Kiinteistönvälitys** — **fuusioitunut Huoneistokeskukseen 1.9.2020** (Realia-konserni;
  uutisoitu mm. Retta/STT-tiedotteella "SKV Kiinteistönvälitys ja Huoneistokeskus yhdistävät
  voimansa", projektiuutiset.fi, Kaleva). Todiste omasta datasta: `www.skv.fi` **uudelleenohjautuu
  suoraan** osoitteeseen `huoneistokeskus.fi` (HTTP 200, sama sisältö kuin Huoneistokeskuksen
  etusivu). PRH vahvistaa: Huoneistokeskus Oy:n (1831315-2) aputoiminimissä on kymmeniä
  entisiä SKV-aluenimiä ("SKV Kiinteistönvälitys", "Helsingin SKV Kiinteistönvälitys",
  "Turun SKV", "Tampereen SKV", "Oulun SKV", "Kuopion SKV Kiinteistönvälitys" jne.),
  kaikki rekisteröity 30.9.2020 — sama juridinen yhtiö, ei enää itsenäinen kilpailija.
  Ei listata erikseen.
- **Roof Group / Roof LKV** — elävä ja kasvava (roof.fi), mutta toimipisteverkosto kattaa
  vain **3 aluetta**: Espoo/pääkaupunkiseutu, Tampere/Pirkanmaa, Oulu/Pohjois-Pohjanmaa.
  Ei toimistoa esim. Turussa, Jyväskylässä, Kuopiossa, Lahdessa. Yhtiön oma markkinointi
  käyttää sanaa "valtakunnallinen verkosto", mutta todellinen kattavuus on kolmen kaupunkiseudun
  ketju — selvästi suppeampi kuin kuusi vahvistettua (Kiinteistömaailman kymmenet paikkakunnat,
  Bo LKV:n kuusi aluetta koko maassa). Rajatapaus, mutta karsittu heikomman maantieteellisen
  kattavuuden perusteella.
- **Aninkaisten Kiinteistönvälitys Oy** — paikallinen Turun yhtiö, ei valtakunnallinen ketju.
  Ei sekoiteta Solid Houseen (eri yhtiö, vaikka molemmat toimivat Turussa).
- **Solid House (Arktium Oy)** — elävä, mutta vain **8 toimistoa**, kaikki
  Lounais-Suomessa/Uudellamaalla/Tampereen seudulla (Helsinki, Vantaa, Tampere, Turku,
  Pori, Salo, Uusikaupunki, Laitila) — ei yhtään toimistoa itäisessä tai pohjoisessa
  Suomessa. Alueellinen läntisen Suomen ketju, ei valtakunnallinen.

## HUOMIOT

- **OP Koti ja Habita jakavat saman rakenteen:** yksi valtakunnallinen brändi ja
  yhtenäinen verkkosivusto, mutta juridisesti hajautettu kymmeniin alueellisiin/paikallisiin
  Oy:ihin. Tämä poikkeaa esim. Bo LKV:sta ja Kiinteistömaailmasta, jotka ovat yksi juridinen
  yhtiö. Pitää avata metodologiasivulla samaan tapaan kuin EasyFit-huomio kuntosalit-kategoriassa
  — muuten lukija olettaa yhden Y-tunnuksen riittävän koko ketjun transparenssin mittariksi.
- **SKV/Huoneistokeskus-fuusio (1.9.2020)** dokumentoitu sekä julkisella uutisoinnilla että
  PRH:n aputoiminimirekisteröinnillä (30.9.2020) — kaksi riippumatonta lähdettä, sama
  ajankohta. Vahva löydös, ei tulkinnanvarainen.
- **RE/MAX** on virallisesti franchise ("Each office independently owned and operated") —
  samantyyppinen huomio kuin EasyFit; mittaus kohdistuu silti yhteen kansalliseen
  master-yhtiöön (REF Real Estate Franchises Oy) ja yhteen sivustoon (remax.fi), joten
  Y-tunnus on tässä tapauksessa yksiselitteinen toisin kuin OP Kodissa/Habitassa.
- **Ei löytynyt viitteitä ristiinomistuksesta** näiden kuuden vahvistetun välillä (toisin
  kuin `sahkovertailupalvelut`-kategoriassa, jossa Effortia Oy omisti kaksi kilpailijaa).
  Kiinteistömaailma, Huoneistokeskus, OP Koti, RE/MAX, Habita ja Bo LKV vaikuttavat aidosti
  toisistaan riippumattomilta — tätä ei kuitenkaan ehditty todistaa tyhjentävästi (esim.
  Kiinteistömaailman mahdollista omistajakonsernia ei jäljitetty PRH:n omistajatiedoista
  asti, koska rajapinta ei tässä ajossa palauttanut omistajarakennetta, vain
  toiminimihistorian).
