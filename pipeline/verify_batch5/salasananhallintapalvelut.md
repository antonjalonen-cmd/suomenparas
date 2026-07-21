# Brändivarmistus — Salasananhallintapalvelut (BATCH 5)

Tarkistettu 21.7.2026 `pipeline/fetch_page.py` (curl-pohjainen; `--js` tarvittiin useimmille,
koska hinnat renderöityvät clientillä React/Next.js-sivuilla — merkitty erikseen jokaiselle) +
PRH:n YTJ v3 -rajapinta (`avoindata.prh.fi/opendata-ytj-api/v3/companies`) nimihaulla jokaiselle
kahdeksalle ehdokkaalle. Kaikki ovat globaaleja, ei-suomalaisia yhtiöitä — sama tilanne kuin
`vpn-palvelut`-kategoriassa (ks. `pipeline/companies.py` rivit ~191–212): `y_tunnus=None`,
`omistaja` + `lainkayttoalue` PRH-vahvistetun Y-tunnuksen sijaan.

**Rajaus:** kuluttajille suunnatut salasananhallintaohjelmistot, joilla on oma julkinen
hinnoittelusivu. Ydinkysymys: kerrotaanko hinta ennen kuin käyttäjä luo tilin ja alkaa syöttää
salasanojaan palveluun?

## KeePass — käsitelty erikseen, EI VAHVISTETTU kategoriaan

KeePass on ilmainen, avoimen lähdekoodin ohjelma jota ylläpitää yhteisö (ei yhtiötä sen takana).
Oma sivusto keepass.info kuvaa itsensä suoraan: *"the official website of KeePass, the free,
open source, light-weight and easy-to-use password manager"* ja *"Is it really free? Yes,
KeePass is really free"* — rahoitus tulee vapaaehtoisista lahjoituksista (Donate-sivu), ei
tilausmaksuista.

**Päätös: KeePass jätetään pois, perusteltuna.** Kategorian läpinäkyvyyskysymys on rakennettu
kaupalliselle transaktiolle: kertooko *yritys* hinnan ennen kuin käyttäjä luovuttaa dataansa
*yritykselle*. KeePassissa ei ole kumpaakaan puolta tästä yhtälöstä — ei yritystä, joka
hinnoittelisi mitään, eikä dataa joka siirtyisi kenellekään ulkopuoliselle (paikallinen
tietokanta, ei pilvitiliä). Sen sijoittaminen samalle pisteytysasteikolle "kerrotaanko hinta"
-kriteerillä antaisi sille automaattisesti täydet pisteet hinta-avoimuudesta (hinta = 0 €,
aina näkyvissä) tavalla, joka ei mittaa mitään todellista — se ei kilpaile samalla
akselilla kuin kahdeksan muuta. Tämä ei ole sama tapaus kuin Lexly/Docue-tyyppinen karsinta
(kuollut yhtiö tai väärä kohderyhmä); KeePass toimii täysin hyvin, se vain ei kuulu tämän
kategorian mittarin piiriin. Jos Anton haluaa avoimen lähdekoodin vaihtoehdon näkyville,
se kannattaisi esitellä sivulla erillisenä huomiolaatikkona ("täysin ilmainen vaihtoehto: KeePass"),
ei rivinä pisteytystaulukossa.

## VAHVISTETUT (7)

| slug | nimi | domain | y_tunnus | omistaja | JS-vaatimus | mittaus-URL |
|---|---|---|---|---|---|---|
| `1password` | 1Password | 1password.com | Ei — PRH-haku "1Password" antoi 0 tulosta | 1Password Inc. (Kanada) — oma footer: "4711 Yonge St, 10th Floor, Toronto, Ontario, M2N 6K8, Canada" | Ei — plain fetch palautti hinnat suoraan (Individual $2.99/kk) | https://1password.com/pricing |
| `bitwarden` | Bitwarden | bitwarden.com | Ei — PRH-haku "Bitwarden" antoi 0 tulosta | Bitwarden Inc. (Yhdysvallat, Santa Barbara, CA) — itsenäinen, pääomasijoittaja-rahoitteinen | Ei — plain fetch palautti hinnat suoraan (Premium $1.65/kk, Families $3.99/kk) | https://bitwarden.com/pricing/ |
| `dashlane` | Dashlane | dashlane.com | Ei — PRH-haku "Dashlane" antoi 0 tulosta | Dashlane Inc. / Dashlane SAS (oma footer: "trademarks of Dashlane SAS, registered in the U.S. and other countries") — itsenäinen, ei julkisesti listattu, pääomasijoittajaomisteinen | Kyllä — plain fetch palautti hinnat "--" (placeholder); `--js` palautti oikeat EUR-hinnat (Premium 3,87 €/kk) | https://www.dashlane.com/personal-pricing |
| `nordpass` | NordPass | nordpass.com | Ei — PRH-haku "NordPass" antoi vain irrelevantin osuman (ks. HUOMIOT) | Nord Security — sama konserni kuin jo julkaistu NordVPN (ks. HUOMIOT, kriittinen disclosure) | Kyllä — plain fetch /plans-sivulle palautti hinnat "Loading"-placeholderina; `--js` palautti oikeat EUR-hinnat (Premium 1,49 €/kk kampanjahintana) | https://nordpass.com/plans |
| `lastpass` | LastPass | lastpass.com | Ei — PRH-haku "LastPass" antoi 0 tulosta | LastPass US LP, hallinnoi LMI Parent, L.P. -holdingyhtiö; omistajat Francisco Partners ja Elliott Management (irtaantui GoTo:sta/LogMeIn:sta toukokuussa 2024, on itsenäinen yhtiö) | Kyllä — plain fetch näytti suunnitelmien nimet mutta ei euromääriä; `--js` palautti hinnat (Premium 2,90 €/kk, Families 3,90 €/kk) | https://www.lastpass.com/pricing |
| `keeper` | Keeper | keepersecurity.com | Ei — PRH-haku "Keeper Security" antoi 0 tulosta | Keeper Security, Inc. — rekisteröity Delawaressa, pääkonttori Chicago, Illinois, USA; yksityisesti omistettu | Kyllä — plain fetch /pricing/personal-and-family.html palautti hinnat tyhjinä/"XXX"-placeholdereina; `--js` palautti oikeat USD-hinnat (Personal $4.50/kk) | https://www.keepersecurity.com/pricing/personal-and-family.html |
| `proton-pass` | Proton Pass | proton.me/pass | Ei — PRH-haku "Proton AG" antoi 0 tulosta | Proton AG — sama omistaja kuin jo julkaistu Proton VPN (ks. HUOMIOT, kriittinen disclosure). Oma ToS: *"The Services are operated by Proton AG ('the Company', 'We'), domiciled at Route de la Galaise 32, 1228 Plan-les-Ouates, Geneva, Switzerland"* | Kyllä — plain fetch näytti "/month" ilman numeroa; `--js` palautti oikeat EUR-hinnat (Free 0 €, Pass Plus 2,99 €/kk kampanjahintana) | https://proton.me/pass/pricing |

Kaikki seitsemän PRH-haku suoritettu businessId-hakua vastaavalla nimihaulla
(`?name=<yritys>`); kuudelle (Bitwarden, Dashlane, LastPass, Keeper Security, Proton AG,
1Password) tulos oli tyhjä (`totalResults:0`) — ei suomalaista rekisteröityä yhtiötä millään
näistä nimistä. NordPass-haku EI ollut tyhjä, mutta osuma on irrelevantti — ks. HUOMIOT.

## KARSITUT

- **KeePass** — ei kaupallinen tuote, ei yhtiötä, ei hintaa, ei datan luovutusta. Käsitelty
  omana lukunaan yllä, ei rivinä VAHVISTETUT-taulukossa. Ei sama asia kuin muut karsinnat
  (ei kuollut yhtiö, ei väärä kohderyhmä) — tietoinen rajausvalinta kategorian mittarin takia.

Kaikki kahdeksasta alkuperäisestä ehdokkaasta paitsi KeePass läpäisivät varmistuksen — mikään
ei osoittautunut kuolleeksi brändiksi, tuplabrändiksi tai väärän kohderyhmän tuotteeksi.

## HUOMIOT

- **KRIITTINEN — NordPass jakaa omistajan jo julkaistun NordVPN:n kanssa.** NordPass on Nord
  Securityn tuote, sama konserni jonka omistus on jo dokumentoitu `vpn-palvelut`-kategoriassa
  (`nordvpn`: "Nord Security / Cyberspace B.V. (Alankomaat)"). Konkreettinen todiste omalta
  sivustolta: nordpass.com:n kirjautumisvalikossa lukee suoraan *"Subscription management —
  View, upgrade or cancel my Nord Security subscriptions"* (NordPass-tilaus ON Nord
  Security-tilaus), ja saman sivun footerissa "Discover: Nord Security / NordVPN / NordLayer
  / NordLocker / NordStellar / Coveron / Saily" listaa NordPassin sisarbrändien joukossa.
  **Suoraa oikeushenkilötason vahvistusta (nordvpn.com:n tai my.nordaccount.com:n omasta
  käyttöehto-/tietosuojasivusta, samalla tavalla kuin Cyberspace B.V. vahvistettiin
  vpn-palvelut-kategoriassa 16.7.2026) ei tällä kertaa saatu** — molemmat domainit
  palauttivat Cloudflare-bottitarkistuksen sekä plain fetchillä (HTTP 403) että `--js`:llä
  ("Turvatarkistuksen suorittaminen... Ray ID..."), eikä sitä yritetty kiertää (rajan
  ylitys, ks. QUEUED_CATEGORIES.md). Tämä on itsessään merkittävä löydös: Nord Securityn
  omat käyttöehtosivut olivat avoimesti luettavissa 16.7.2026 mutta eivät enää 21.7.2026 —
  syytä mainita julkaisusivulla, ei vain omistusdisclaimeria vaan myös tätä läpinäkyvyyden
  heikkenemistä. Julkaisusivulla NordPass ja NordVPN on merkittävä saman omistajan tuotteiksi
  — lukija joka näkee molemmat "riippumattomina" vaihtoehtoina eri kategorioissa ei muuten
  tiedä rahoittavansa samaa konsernia kahdesti.
- **KRIITTINEN — Proton Pass jakaa omistajan jo julkaistun Proton VPN:n kanssa.** Vahvistettu
  suoraan Protonin omasta yleisestä Privacy Policy -sivusta (kattaa kaikki Proton-tuotteet,
  myös Passin): *"The Services are operated by Proton AG ('the Company', 'We'), domiciled at
  Route de la Galaise 32, 1228 Plan-les-Ouates, Geneva, Switzerland."* Sama Proton AG kuin
  `vpn-palvelut`-kategoriassa julkaistu `protonvpn` ("Proton AG — Proton Foundation"). Jos
  sisarprojektin `pilvitallennuspalvelut`-varmistus vahvistaa myös Proton Driven, Proton AG
  esiintyisi kolmessa kategoriassa — merkitse tämä julkaisusivulla riippumatta siitä, mitä
  sisarprojekti päättää, koska Pass↔VPN-yhteys on jo kahden kategorian tason toistuvuus
  yksinään.
- **NordPass-nimihaku PRH:sta ei ollut tyhjä, mutta osuma on harhaanjohtava — ei pidä
  sekoittaa.** `avoindata.prh.fi`-haku nimellä "NordPass" löysi yhtiön "Nordpass Oy"
  (Y-tunnus 2835469-5), mutta se on rekisteröity 29.5.2017 ja **lakannut 14.7.2021**,
  toimialana kiinteistöjen vuokraus ("Letting of other real estate") — täysin sattumanvarainen
  nimiosuma, ei mitenkään yhteydessä salasananhallintaohjelmisto NordPassiin tai Nord
  Securityyn. Ei julkaista, ei käytetä Y-tunnuksena. Sama Risicum-tyyppinen varoitus: pelkkä
  osuma nimihaussa ei todista yhteyttä, tarvitaan sisällöllinen vahvistus.
- **JS-vaatimus koskee lähes kaikkia paitsi kahta.** 1Password ja Bitwarden ovat
  poikkeuksellisia: niiden hinnat tulevat suoraan plain-curl-fetchin mukana ilman
  `--js`-renderöintiä. Loput viisi (Dashlane, NordPass, LastPass, Keeper, Proton Pass)
  näyttivät plain-fetchillä joko tyhjän/placeholder-hinnan ("--", "XXX", "Loading",
  pelkkä "/month" ilman numeroa) tai puuttuvan hinnan kokonaan — vasta `--js` paljasti
  todelliset luvut. Tämä on tärkeä huomio pisteytysagenteille: älä merkitse "hintaa ei
  kerrota" plain-fetchin perusteella tässä kategoriassa, sivut LÄHES KAIKKI vaativat
  JS-renderöinnin ennen kuin voi arvioida hinta-avoimuutta rehellisesti.
- **Ei suomenkielistä sisältöä millään seitsemällä paitsi Proton Pass.** 1password.com/fi
  palauttaa HTTP 404; bitwarden.com/fi/ 404; nordpass.com/fi ohjautuu takaisin englanninkieliselle
  etusivulle; keepersecurity.com/fi/ 404 (kielivalikossa 13 kieltä, suomi ei niiden joukossa);
  lastpass.com/fi ohjautuu englanninkieliselle etusivulle; dashlane.com/fi palauttaa HTTP 200
  mutta sisältö on pelkkä englanninkielinen "claim your free 6 months"-kampanjalanding page,
  ei aito suomennos (kielivalitsin sivulla näyttää vain "English") — **ei laske
  suomenkieliseksi sisällöksi**. Proton Pass on ainoa aidosti suomennettu: proton.me/fi
  näyttää täyden suomenkielisen navigaation ja tuotenimet ("Salasanaholvi",
  "Henkilökohtaiset tilaukset", "Tietomurto-observatorio"). Tämä ero kannattaa näkyä
  sivulla omana sarakkeenaan tai huomiona — kategoria mittaa nimenomaan suomalaisen
  kuluttajan kokemusta, ja kuusi seitsemästä tarjoaa sen vain englanniksi (hinnat silti
  usein EUR:ssa).
- **LastPassin 2022 tietomurto — ei karsintaperuste, mutta pakollinen HUOMIO
  läpinäkyvyyssivulle.** LastPass ilmoitti elokuussa 2022 tunkeutumisesta kehitysympäristöön;
  marraskuussa 2022 yhtiö vahvisti vakavamman tapauksen, jossa hyökkääjä sai haltuunsa
  varmuuskopioidun tietokannan ja asiakkaiden salasanaholvien kopioita — sisältäen sekä
  salaamattomia kenttiä (mm. joitain verkko-osoitteita) että salattuja kenttiä (käyttäjätunnukset,
  salasanat). Yhtiön oma viestintä tapahtumasta oli laajasti kritisoitu hitaaksi ja epäselväksi
  (mm. Krebs on Security, Sophos, The Hacker News, ICO:n oma arvio). LastPass on tästä huolimatta
  edelleen toimiva, itsenäinen yhtiö (ks. seuraava kohta) — tämä ei ole peruste karsia sitä,
  mutta se on olennainen luottamustieto lukijalle juuri tällä sivulla, jonka koko teema on
  "kerrotaanko käyttäjälle rehellisesti, mitä hänen datalleen tapahtuu". Editorial-päätös
  (nostetaanko esiin kriittisesti vai vain mainitaan) jätetään Antonille.
- **LastPassin omistusrakenne vahvistettu itsenäiseksi.** LastPass erosi virallisesti
  GoTo:sta (ent. LogMeIn) toukokuussa 2024 ja toimii nyt itsenäisenä yhtiönä holdingyhtiön
  LMI Parent, L.P. alla, omistajina pääomasijoittajat Francisco Partners ja Elliott
  Management — ei ole sulautunut tai kadonnut, tuote on aidosti elossa ja aktiivisesti
  kehitetty (oma pricing-sivu listaa uusia ominaisuuksia, mm. "SaaS Protect", "Mobile Smart
  Scanner").
- **Dashlane ja Keeper vahvistettu edelleen itsenäisiksi, ei kuollutta brändiä.** Dashlane on
  yksityinen, pääomasijoittajaomisteinen (Sequoia, Bessemer ym.), ei myyty; markkina-analyysit
  spekuloivat mahdollisella exitillä 2026–2027 mutta ei toteutunutta kauppaa heinäkuuhun 2026
  mennessä. Keeper Security, Inc. on rekisteröity Delawaressa, pääkonttori Chicago — ei
  osoitusta omistajanvaihdoksesta tai sulautumisesta.
- **Ei yhteisiä omistajia paitsi Nord- ja Proton-parit.** 1Password (Kanada), Bitwarden
  (USA), Dashlane (USA/Ranska), LastPass (USA, PE-omisteinen) ja Keeper (USA) ovat kaikki
  toisistaan riippumattomia. Kategoriassa on siis kaksi selvää omistuskeskittymä-paria
  (NordPass↔NordVPN, Proton Pass↔Proton VPN) viiden muun itsenäisen toimijan joukossa.
- **Seitsemän vahvistettua on tavoitteen (5–9) sisällä, ei tarvinnut karsia lisää eikä
  etsiä täytettä.** KeePassin tietoinen poisjättö on ainoa rajaus tässä kategoriassa —
  ei yhtään kuollutta brändiä, ei tuplabrändiä (Nord- ja Proton-parit ovat läpinäkyvästi
  disclosoituja duplikaatteja, ei virheellisiä tuplia), ei väärää kohderyhmää.
