# virustorjuntaohjelmat — brändivarmistus (BATCH 5)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py`:llä (curl ensin; `--js` ja `render_page.py`
kokeiltu kun curl palautti tyhjän/dynaamisen sisällön — merkitty per rivi) + PRH:n YTJ v3
-rajapinta suomalaiselle yhtiölle (F-Secure). Kahdeksasta tehtävänannon ehdokkaasta
seitsemän vahvistettiin elossa olevaksi, suomeksi/englanniksi myytäväksi tuotteeksi;
Kaspersky vahvistettiin erikseen aktiiviseksi Suomen myynnin osalta (ei EU-kieltoa).
**McAfee karsittiin — ei brändin kuoleman vaan teknisen esteen takia, ks. KARSITUT.**
Kahdeksan vahvistettua on tavoitehaarukan (5–9) yläpäässä.

## VAHVISTETUT (8)

| slug | nimi | domain | y_tunnus | omistaja | JS | mittaus-URL |
|---|---|---|---|---|---|---|
| `fsecure` | F-Secure (Internet Security / Total) | f-secure.com/fi | **3269349-7** (F-Secure Oyj, PRH-vahvistettu: "Rekisterissä", Julkinen osakeyhtiö, Helsinki — sama Y-tunnus jo käytössä `vpn-palvelut`-kategoriassa F-Secure VPN:lle) | **F-Secure Oyj** — suomalainen pörssiyhtiö, Nasdaq Helsinki | Ei — curl-haulla oikea URL löytyi vasta nav-linkkien kautta (ks. HUOMIOT); lopullinen fi-sivu palautti täyden sisällön ilman JS:ää (12 759 merkkiä) | https://www.f-secure.com/fi |
| `norton` | Norton (360 / AntiVirus Plus) | fi.norton.com | Ei — globaali, ei suomalaista Y-tunnusta | **Gen Digital Inc.** (Yhdysvallat, Nasdaq-pörssiyhtiö) — vahvistettu suoraan omalta sivulta: "Norton on osa Geniä – maailmanlaajuista yritystä, joka omistaa joukon luotettuja brändejä." Copyright: "© 2026 Gen Digital Inc." **KRIITTINEN OMISTUSKESKITTYMÄ, ks. HUOMIOT.** | Ei — fi.norton.com palautti täyden suomenkielisen sisällön hintoineen suoraan (13 994 merkkiä) | https://fi.norton.com/ |
| `bitdefender` | Bitdefender (Total Security) | bitdefender.com | Ei — globaali, ei suomalaista Y-tunnusta | **Bitdefender** — romanialainen yhtiö (perustettu 2001, Bukarest); yksityisesti omistettu, ei pörssiyhtiö. Tarkkaa juridista nimeä/omistuspohjaa ei vahvistettu tällä haulla — merkitty "romanialainen, yksityinen" HUOMIOT-perusteluin. | **Kyllä osittain** — bitdefender.fi ja bitdefender.com/fi-fi eivät ole olemassa (ohjautuvat en-mt/en-us-sivuille); tuotesivu (en-us/consumer/total-security) palautti hinnat suoraan curlilla mutta **USD:ssä, ei EUR:ssa**, ks. HUOMIOT | https://www.bitdefender.com/en-us/consumer/total-security |
| `eset` | ESET (Home Security / NOD32) | eset.com/fi | Ei — globaali, ei suomalaista Y-tunnusta | **ESET, spol. s r.o.** (Slovakia) — konsernin emoyhtiö. Suomen/Pohjoismaiden vähittäismyyntiä hoitaa oma sivu paljastama alueellinen operaattori **ESET Norden ApS** (Korskildelund 6, 2670 Greve, Tanska) — ei siis suomalaista eikä edes pohjoismaista erillisyhtiötä Suomessa, vaan tanskalainen Pohjoismaiden-yksikkö. | Ei — eset.com/fi palautti täyden suomenkielisen sisällön suoraan (28 480 merkkiä); hinnasto-alasivu 404, mutta etusivun tuotekortit ja "Osta nyt" -painikkeet toimivat ilman JS:ää | https://www.eset.com/fi/ |
| `avast` | Avast (One / Premium Security) | avast.com/fi-fi | Ei — globaali, ei suomalaista Y-tunnusta | **Gen Digital Inc.** (Yhdysvallat) — vahvistettu suoraan sivun footerista: "© 2026 Gen Digital Inc. Kaikki oikeudet pidätetään." **Sama omistaja kuin Norton ja AVG, ks. HUOMIOT.** | Ei — avast.com/fi-fi palautti täyden suomenkielisen sisällön suoraan (12 312 merkkiä), maavalikossa "Suomi" mukana | https://www.avast.com/fi-fi/index |
| `avg` | AVG (AntiVirus / Ultimate) | avg.com | Ei — globaali, ei suomalaista Y-tunnusta | **Gen Digital Inc.** (Yhdysvallat) — vahvistettu footerista ("About Gen"). **Sama omistaja kuin Norton ja Avast, ks. HUOMIOT.** | Ei — avg.com/fi-fi/homepage.html ohjautui automaattisesti osoitteeseen /en-eu/homepage (ei suomenkielistä versiota, ks. HUOMIOT); en-eu-sivu palautti sisällön suoraan englanniksi (8 761 merkkiä) | https://www.avg.com/en-eu/homepage |
| `kaspersky` | Kaspersky (Standard / Plus / Premium) | kaspersky.fi | Ei — venäläistaustainen, ei suomalaista Y-tunnusta | **Kaspersky Lab** — perustettu Venäjällä (Moskova), yksityisesti omistettu (perustaja Jevgeni Kasperskin ja johdon omistuksessa, ei pörssiyhtiö). Tarkkaa nykyistä holding-rakennetta (esim. mahdollinen brittiläinen tai sveitsiläinen holdingyhtiö) ei vahvistettu tällä haulla. | Ei — kaspersky.fi ja /standard palauttivat täyden suomenkielisen sisällön suoraan (11 314 ja 12 804 merkkiä) ilman JS:ää, mutta **hinta ei näkynyt kummallakaan**, ks. HUOMIOT | https://www.kaspersky.fi/standard |
| `totalav` | TotalAV (Total Security) | totalav.com | Ei — brittiläis-yhdysvaltalainen, ei suomalaista Y-tunnusta | **Total Security Limited** (Iso-Britannia) / **Total Security US LLC** (250 Northern Avenue, Floor 3, Boston, MA 02210) — molemmat mainittu omalla sivulla, tarkkaa emo-tytär-suhdetta ei eritelty. Ei sama konserni kuin Gen Digital tai muut listan yhtiöt. | Ei — totalav.com palautti täyden sisällön suoraan (6 674 merkkiä), mutta **ei suomeksi**, ks. HUOMIOT | https://www.totalav.com/ |

## KARSITUT

- **McAfee — ei karsittu brändin kuoleman vuoksi, vaan koska sivustoa ei saatu luettua
  millään sallitulla menetelmällä.** mcafee.com palautti johdonmukaisesti
  `HTTP 403 Access Denied` (Akamai-reunapalvelin) jokaisella kokeillulla polulla
  (`/en-fi/antivirus.html`, `/fi-fi/index.html`, paljas juuri `/`) sekä plain curlilla
  että `--js`-headless Chromella (joka sai `ERR_HTTP2_PROTOCOL_ERROR`), ja myös
  `pipeline/render_page.py` (Playwright) epäonnistui samalla virheellä ja tulosti
  eksplisiittisesti: *"Do NOT invent a reason for this. Report the failure and score
  'osittain'."* McAfee on tunnetusti edelleen elossa oleva, laajasti myyty brändi
  (osa McAfee Corp:ia, yksityistetty konsortion — mm. Advent Internationalin —
  toimesta 2022) — kyse ei ole kuolleesta yhtiöstä, vaan siitä että heidän
  reunaverkkonsa torjuu tämän pipelinen automatisoidut hakuyritykset johdonmukaisesti
  kolmella eri polulla ja kahdella eri renderöintimoottorilla. QUEUED_CATEGORIES.md:n
  rajan mukaan **sivuston bottisuojauksen kiertäminen on rajan ulkopuolella** — tätä ei
  yritetty (ei User-Agent-kiertoa, ei proxya, ei uudelleenyrityksiä viiveellä). Tulos:
  McAfee jätetään pois tästä varmistuksesta. Jos Anton haluaa sen mukaan, se vaatisi
  joko manuaalisen selainhaun (ihmisen tekemänä) tai sallitun kolmannen fetch-reitin,
  ei tämän pipelinen automaatiota.

## HUOMIOT

- **KRIITTINEN — OMISTUSKESKITTYMÄ: Norton + Avast + AVG = Gen Digital Inc, 3/8
  vahvistetusta rivistä sama omistaja.** Tehtävänanto pyysi tämän kirjattavaksi
  erikseen, ja kaikki kolme vahvistettiin **suoraan omilta sivuiltaan**, ei
  kolmannen osapuolen lähteestä: Norton-sivun footer "Norton on osa Geniä", Avastin
  footer "© 2026 Gen Digital Inc.", AVG:n footer "About Gen" -linkki. Tämä on suurin
  yksittäinen omistuskeskittymä, joka tässä pipelinessä on toistaiseksi löydetty yhden
  kategorian sisällä (kahdeksasta rivistä kolme). Julkaisusivulla tämä täytyy näkyä
  näkyvästi, ei vain pienenä alaviitteenä — muuten lukija luulee vertailevansa kolmea
  riippumatonta tuotetta, kun todellisuudessa kyse on yhdestä konsernista kolmella
  eri hintapisteellä/brändillä samalle ydinteknologialle (Avast osti AVG:n 2016;
  NortonLifeLock ja Avast yhdistyivät 2022 muodostaen Gen Digitalin).
- **Kaspersky: ei EU-tason kuluttajakieltoa toukokuussa 2026, mutta poliittinen paine
  jatkuu — tehtävänannon erikseen pyytämä tarkistus.** Web-haku: Euroopan parlamentti
  hyväksyi ei-sitovan päätöslauselman (476 puolesta, 151 vastaan), joka kuvaa
  Kasperskyn ohjelmistoa "haitalliseksi", mutta **tämä ei ole EU:n laajuinen
  myyntikielto**. Yksittäiset maat ovat toimineet vaihtelevasti: Saksan BSI antoi
  vuonna 2022 suosituksen vaihtoehtoisista tuotteista kansallisen turvallisuuden
  perusteella (ei myyntikieltoa), Italia ja Alankomaat ovat merkinneet Kasperskyn
  vain julkisten hankintojen osalta ongelmalliseksi. **Suomen Kyberturvallisuuskeskusta
  (Traficom) koskevaa erillistä suositusta tai kieltoa ei löytynyt tällä haulla.**
  kaspersky.fi on aidosti olemassa, suomenkielinen ja toimiva, maavalikossa "Suomi"
  Länsi-Euroopan alla — myynti Suomeen jatkuu normaalisti heinäkuussa 2026.
  Julkaisusivulla on silti syytä mainita geopoliittinen konteksti (Yhdysvallat kielsi
  Kasperskyn myynnin kokonaan syyskuussa 2024) läpinäkyvyyden vuoksi, vaikka se ei ole
  karsintaperuste Suomen markkinalle.
- **Kaspersky Standard -sivu ei näyttänyt hintaa lainkaan — ainoa tällä haulla löydetty
  tapaus koko kategoriassa.** Sekä plain curl että `--js`-renderöinti kaspersky.fi/
  standard-sivulle palauttivat täyden suomenkielisen ominaisuuskuvauksen (tietoturva-,
  yksityisyys- ja suorituskykyominaisuudet, palkinnot, "30 päivän rahat takaisin
  -takuu") mutta **ei yhtään euromäärää** — hinta ladataan ilmeisesti erillisen
  ostoskori-/kassa-API:n kautta vasta "Osta nyt" -painikkeen jälkeen, ei
  markkinointisivulla. Tämä eroaa selvästi F-Securesta, Nortonista, Avastista ja
  Bitdefenderista, jotka kaikki näyttivät euro-/dollarihinnan suoraan
  markkinointisivullaan. Pisteytysagenteille tärkeä ero: älä merkitse Kasperskyn
  hinta-avoimuutta samaksi kuin muiden pelkän "sivu latautui" perusteella — hinnan
  puuttuminen tällä nimenomaisella sivulla on todellinen löydös, ei mittausvirhe
  (sivu selvästi latautui, sisältö täydellistä, hinta vain puuttuu).
- **Bitdefenderilla ja AVG:llä ei ole omaa suomenkielistä sivua — kahdella eri
  tavalla.** Bitdefender.fi ja bitdefender.com/fi-fi eivät ole olemassa; molemmat
  ohjautuvat geneeriselle englanninkieliselle sivulle (ensin en-mt/Malta, sitten
  tuotesivuilla en-us) ja **hinta näytettiin USD:ssä** tällä haulla — epäselvää, olisiko
  todellinen suomalainen kävijä (oikea IP-geolokaatio) nähnyt EUR-hinnan; tätä ei voitu
  vahvistaa tällä fetch-menetelmällä, koska emme voi jäljitellä suomalaista
  IP-osoitetta ilman kiertämistä. AVG:n tapaus on vielä selvempi: sen oma maavalikko
  (Länsi-Eurooppa/Pohjoismaat-osiossa) listaa Ruotsin ja Tanskan mutta **ei sisällä
  Suomea lainkaan** — ei siis edes kielivalintaa tarjolla, toisin kuin sisaryhtiö Avast
  (sama Gen Digital -konserni), jonka maavalikossa Suomi on mukana ja koko sivu on
  suomeksi. Tämä ero saman konsernin kahden brändin välillä on syytä näyttää
  julkaisusivulla omana huomiona.
- **TotalAV ei tarjoa suomea — ainoa täysin kielivahvistettu poissulkeva löydös.**
  Kielivalikko listaa: Dansk, Deutsch, Français, English, Español, Italiano,
  Nederlands, **Norsk**, Polski, Português, **Svenska**, Česky, Türkçe — Suomi puuttuu
  kokonaan, vaikka naapurimaiden kielet (norja, ruotsi, tanska) ovat mukana. Ei
  karsintaperuste sinänsä (VPN-palvelut/salasananhallinta-kategorioissa on jo
  julkaistu brändejä ilman suomenkielisyyttä, esim. Windscribe, Keeper), mutta
  ansaitsee oman sarakkeen/huomion sivulla: TotalAV on ainoa kategorian brändeistä,
  joka ei edes yritä tavoittaa suomalaista kuluttajaa millään kielellä.
- **F-Secure vaati nav-linkkien seuraamista, ei suoraa URL-arvausta — sama SPA-ansa
  kuin batch 3:ssa (Hertz, Synsam, Habita).** Suorat arvaukset (`/fi_fi`, `/fi_fi/home`,
  `/fi_fi/home/products/total`) palauttivat kaikki HTTP 404 saman staattisen
  JS-sovelluskuoren kanssa, vaikka maavalikko listasi "Suomi". Toimiva polku
  (`/fi`) löytyi vasta hakemalla englanninkielisen sivun (`/en/home`) raaka HTML ja
  poimimalla oikea `href`-linkki maavalikosta `--js --raw`-tilassa. Tämä on
  täsmälleen se korjaus, jonka batch 3:n laatunotet suosittelivat: "fetch front page
  --js --raw, grep hrefs, follow REAL nav links" — toimi tälläkin kertaa.
  F-Secure Internet Security 49,99 €/vuosi, F-Secure Total 69,99 €/vuosi
  (löydöt lopullisen `/fi`-sivun sisällöstä).
- **ESET:n Pohjoismaiden-operaattori on tanskalainen, ei suomalainen eikä edes
  yleispohjoismainen erillisyhtiö.** ESET-sivun oma 404-sivun footeri (löytyi
  hinnasto-alasivun kokeilussa) paljasti yhteystiedoksi "ESET Norden ApS,
  Korskildelund 6, 2670 Greve, Danmark" — tämä on vastuuyksikkö koko Pohjolan
  vähittäismyynnille, Suomi mukaan lukien. Ei siis suomalaista Y-tunnusta haettavaksi
  edes epäsuorasti; y_tunnus=None on oikea merkintä, kotimaa "Slovakia (emo) /
  Tanska (aluevastuu)".
- **Kaikki kahdeksan ovat aidosti elossa myyviä tuotteita — ei yhtään kuollutta
  brändiä tai fuusiota löytynyt tällä haulla.** Toisin kuin monissa aiemmissa
  kategorioissa (Väre, Säästöpankki, Risicum, Lexly), virustorjuntamarkkina
  vaikuttaa tässä otoksessa vakaalta: kaikki kahdeksan yhtiötä toimivat itsenäisinä,
  tunnistettavina brändeinä omalla verkkotunnuksellaan. Ainoa rakenteellinen
  yllätys on omistuskeskittymä (Gen Digital), ei brändien kuolema.
- **Ei tarkistettu tyhjentävästi:** Windows Defenderia/Microsoft Defenderia (esiasennettu,
  ei erillinen ostotuote — ei sovi kategorian "kerrotaanko hinta" -mittariin samalla
  tavalla kuin KeePass jätettiin pois salasananhallinta-kategoriasta) eikä pienempiä
  nichetuotteita (esim. Malwarebytes, joka on enemmän täydentävä kuin
  perusvirustorjunta) ei käyty läpi — tehtävänanto rajasi kahdeksaan nimettyyn
  ehdokkaaseen, ja se rajaus riitti tavoitehaarukkaan.
