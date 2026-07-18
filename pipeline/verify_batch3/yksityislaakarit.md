# Brändivarmistus — Yksityislääkärit (batch 3)

Mittauspäivä tälle varmistukselle: 18.7.2026. Kaikki haut tehty `pipeline/fetch_page.py`:llä
(curl, ei JS-renderöintiä tarvittu yhdellekään näistä viidestä — kaikki palauttivat täyden
leipätekstin ilman `--js`-lippua). Y-tunnukset vahvistettu PRH:n avoindata-ytj-api v3:sta
nimihaulla + businessId-haulla (ei yhtään keksittyä Y-tunnusta).

## VAHVISTETUT (5)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `mehilainen` | Mehiläinen | mehilainen.fi | 1927556-5 (Mehiläinen Oy, Helsinki, rekisteröity 2004, tradeRegisterStatus=rekisterissä) | Ei tarkistettu tarkemmin tällä ajolla (tiedetään yleisesti pääomasijoittajaomisteinen; ei vahvistettu PRH:n omistajatiedoista) | Ei — curl palautti 4 816 merkkiä täyttä sisältöä | https://www.mehilainen.fi/ |
| `terveystalo` | Terveystalo | terveystalo.com | 2575979-3 (Terveystalo Oyj, Helsinki, julkinen osakeyhtiö/pörssiyhtiö) | Pörssiyhtiö (Nasdaq Helsinki) | Ei — curl palautti 9 516+ merkkiä | https://www.terveystalo.com/ |
| `pihlajalinna` | Pihlajalinna | pihlajalinna.fi | 2617455-1 (Pihlajalinna Oyj, Tampere, julkinen osakeyhtiö/pörssiyhtiö) | Pörssiyhtiö (Nasdaq Helsinki) | Ei — curl palautti 5 498 merkkiä | https://www.pihlajalinna.fi/ |
| `aava` | Aava (ent. Lääkärikeskus Aava) | aava.fi | 2311119-2 — **HUOM: virallinen nimi vaihtui 3.6.2025** "Lääkärikeskus Aava Oy" → "Aava ja Pikkujätti Oy" (PRH: names[].endDate=2025-06-03 vanhalle nimelle). Sivusto käyttää edelleen pelkkää "Aava"-brändiä, mutta mainitsee itse "Aava ja Pikkujätti Oy:n hallitukseen" uutisissaan — ristiriidaton löydös. | Suomalainen perheyritys ("Omistus pysyy perheellä" — sivun oma väite) | Ei — curl palautti 6 216+ merkkiä | https://www.aava.fi/ |
| `lysna` | Lysna | lysna.fi | 3474612-6 (Lysna Oy, Tampere, rekisteröity 10.9.2024, toimiala 86220 "Lääkäriasemat, yksityislääkärit ja vastaavat erikoislääkäripalvelut" — täsmää suoraan kategoriaan) | Ei konsernitietoa löydetty — vaikuttaa itsenäiseltä, äskettäin perustetulta yhtiöltä | Ei — curl palautti 7 191 merkkiä | https://lysna.fi/ |

**HUOM kokoerosta:** Mehiläinen/Terveystalo/Pihlajalinna/Aava ovat satojen toimipisteiden
valtakunnallisia ketjuja (Terveystalolla itsellään 225 toimipistettä). Lysna on vasta 2024
perustettu, 5 toimipisteen ketju (Helsinki, Turku, Tampere, Kempele, Pyhäntä — kattaa etelän,
lännen ja pohjoisen, joten täyttää "valtakunnallinen" kriteerin maantieteellisesti, vaikka
on kooltaan murto-osa muista). Tämä kokoero pitää näkyä sivulla, ei piilottaa.

## KARSITUT

- **Diacor** — domain **kuollut**: `https://www.diacor.fi` palautti HTTP 000 (ei yhteyttä).
  `https://diacor.fi` (ilman www) uudelleenohjautuu osoitteeseen **dieetti.fi** — täysin
  irrallinen laihdutus/ruokavalio-sivusto, ei terveyspalveluihin liittyvä. Domain on siis
  luovutettu/myyty eteenpäin. Todiste: brändi sulautui Terveystaloon jo v. 2016 — Yle
  ("Terveystalo ja Diacor yhdistyvät"), Lääkärilehti ja Keskisuomalainen uutisoivat
  fuusiosta; Helsingin Diakonissalaitos (Diacorin omistaja) tuli tuolloin Terveystalon
  merkittäväksi omistajaksi. QUEUED_CATEGORIES.md:n epäilys ("Diacor? — verify, may be
  Terveystalo") vahvistui oikeaksi.
- **Coronaria** — elävä ja aidosti valtakunnallinen yhtiö (coronaria.fi, HTTP 200, 7 499+
  merkkiä), mutta palveluvalikoima on **Kela-kuntoutus, työterveys ja hyvinvointialueiden
  julkinen kumppanuus** (Kelan ammatillinen kuntoutus, kuntoutuskurssit, fysioterapia,
  psykiatria jne.) — ei tarjoa itsemaksullista yleislääkärin vastaanottoa valtakunnallisesti
  samalla tavalla kuin nelikko. Ainoa löydetty suoraan kuluttajalle myyty "lääkäri"-tuote oli
  ajokorttitodistus, ja senkin vain kahdessa toimipisteessä (Oulu, Kuusamo). Ei
  vertailukelpoinen tuote tässä kategoriassa — eri segmentti.
- **Lähilääkärit** (Suomen Lähilääkärit Oy, lahilaakarit.fi) — elävä, kasvava, nimestä
  ("Suomen Lähilääkärit") huolimatta **kaikki 5 toimipistettä sijaitsevat
  pääkaupunkiseudulla**: Kalasatama, Itäkeskus (Helsinki), Soukka, Leppävaara (Espoo),
  Tikkurila (Vantaa). Ei valtakunnallinen — puhtaasti pääkaupunkiseudun ketju. Karsittu
  maantieteellisen kattavuuden perusteella (sama sääntö kuin Roof Groupille
  kiinteistönvälittäjät-kategoriassa).

## HUOMIOT

- **Vain 5 vahvistettua** — juuri kategoriasäännön alarajalla (5–9). Yksityislääkärimarkkina
  on aidosti konsolidoitunut nelikoksi (Mehiläinen/Terveystalo/Pihlajalinna/Aava) plus yksi
  pieni, äskettäin syntynyt haastaja (Lysna). Muita elävää, valtakunnallista, itsemaksullista
  yleislääkäripalvelua tarjoavaa ketjua ei löytynyt tällä haulla (Terwe, Jokiklinikka,
  Medipulssi, Lääkärisatama vaikuttivat kaikki yhden kaupungin/kaupunginosan toimijoilta —
  ei tarkistettu yksitellen PRH:sta ajan säästämiseksi, koska maantieteellinen rajaus näkyi
  jo niiden omilta sivuilta hakutuloksissa).
- **Aava-nimenvaihto (3.6.2025):** sivusto ei vielä (18.7.2026) käytä uutta virallista nimeä
  "Aava ja Pikkujätti Oy" markkinointinimenä — brändi on edelleen pelkkä "Aava". Kannattaa
  käyttää Y-tunnusta 2311119-2 ja mainita virallinen nimi pienellä sivulla, ei otsikossa.
- **Ristikkäisomistus muihin batch 4 -kategorioihin:** Mehiläinen, Terveystalo ja
  Pihlajalinna toimivat myös hammaslääkäri- ja optikkoaloilla (batch 4:n
  `hammaslaakarit`, ja huomionarvoisesti Terveystalo osti Silmäaseman v. 2026 — mainittu
  sen omalla etusivullaan "Terveystalo & Silmäasema – vahvempaa kasvua silmäterveyden
  markkinoilla"). Tämä pitää avata omistuskeskittymänä kun `hammaslaakarit`/`optikot`
  rakennetaan, jotta samaa konsernia ei lasketa toisistaan riippumattomiksi kilpailijoiksi
  eri kategorioissa ilman disclaimeria.
- Kaikki 5 löytyivät suoraan curlilla ilman JS-renderöintiä — tälle kategorialle
  `render_page.py`/`--js` ei ole tarpeen.
