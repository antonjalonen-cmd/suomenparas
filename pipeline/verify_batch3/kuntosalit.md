# Brändivarmistus — Kuntosalit (batch 3)

Mittauspäivä tälle varmistukselle: 18.7.2026. Kaikki haut `pipeline/fetch_page.py`:llä
(curl, ei JS:ää tarvittu). Y-tunnukset vahvistettu PRH:n avoindata-ytj-api v3:sta
nimihaulla + businessId-haulla.

## VAHVISTETUT (6)

| slug | nimi | domain | y_tunnus (PRH-vahvistettu) | omistaja | JS-vaatimus | ehdotettu mittaus-URL |
|---|---|---|---|---|---|---|
| `elixia` | Elixia (SATS) | elixia.fi | 0459885-5 (SATS Finland Oy, Helsinki). "Elixia" on PRH:ssa rekisteröity aputoiminimi samalle yhtiölle. | SATS ASA (Oslon pörssissä noteerattu pohjoismainen konserni) | Ei — curl palautti 3 534 merkkiä | https://www.elixia.fi/ |
| `fressi` | Fressi | fressi.fi | 2538910-4 (Fysioline Fressi Oy, Tampere) | Ei konsernitietoa löydetty tällä haulla | Ei — curl palautti 31 418 merkkiä (91 keskusta) | https://www.fressi.fi/ |
| `ladyline` | LadyLine | ladyline.fi | 1790020-8 (Ab LL International Oy, Espoo). "Lady Line" rekisteröity aputoiminimi. **HUOM: sama yhtiö kuin EasyFit — ks. HUOMIOT.** | Ab LL International Oy -konserni | Ei — curl palautti 12 602 merkkiä (14 kaupunkia) | https://ladyline.fi/ |
| `easyfit` | EasyFit | easyfit.fi | Sama juridinen omistaja kuin LadyLine: Ab LL International Oy (1790020-8) rekisteröi PRH:ssa myös aputoiminimet "Easy Fit" / "Easy Fitness". **Yksittäiset EasyFit-keskukset ovat kuitenkin erillisiä franchise-yhtiöitä** (esim. EasyFit Raisio = Taitoset Oy 2574843-7, EasyFit Lahti = Hs Well Oy, EasyFit Helsinki-Lauttasaari = MM Sport Club Oy) — ei yhtä läpäisevää Y-tunnusta koko ketjulle. | Ab LL International Oy (brändi/franchisoija) + itsenäiset paikallisyrittäjät | Ei — curl palautti 9 486 merkkiä (n. 30 kaupunkia) | https://www.easyfit.fi/ |
| `fitness24seven` | Fitness24Seven | fitness24seven.com (fi.fitness24seven.com) | 2402161-5 (Fitness24Seven Oy, Helsinki) | Ruotsalainen kansainvälinen ketju (emoyhtiö Ruotsissa, ei tarkistettu tällä ajolla) | Ei — curl palautti 4 912 merkkiä (290+ salia globaalisti) | https://fi.fitness24seven.com/fi |
| `liikku` | Kuntokeskus Liikku | liikku.fi | 2784989-9 (Kuntokeskus Liikku Oy, Oulu) | Ei konsernitietoa löydetty | Ei — curl palautti 4 043 merkkiä (35+ kaupunkia, "yli 50 kuntokeskusta") | https://www.liikku.fi/ |

## KARSITUT

- **GOGO Liikuntakeskus** — elävä (gogo.fi, HTTP 200), mutta **itse brändi on Tampere-paikallinen**:
  sivu kertoo suoraan "3 full-service GOGO Fitness Centers in Tampere" (GOGO Park, City,
  Hervanta) — tamperelainen perheyritys, ei valtakunnallinen ketju. Sisaryhtiö
  **GOGO Express** (gogoexpress.fi) kattaa laajemmin n. 15 kaupunkia (Espoo, Hyvinkää,
  Hämeenlinna, Kajaani, Tampereen seutu, Joensuu, Jyväskylä, Lahti, Lohja, Turku, Pori,
  Porvoo, Seinäjoki), mikä olisi lähempänä valtakunnallista, mutta sen tarkkaa
  yhtiörakennetta/Y-tunnusta ei ehditty vahvistaa PRH:sta tällä ajolla (PRH-nimihaku
  "GOGO Liikuntakeskus" ja "GOGO" ei tuottanut selvää osumaa ilman lisätyötä). **Ei
  julkaista kumpaakaan** — voidaan lisätä myöhemmin, kun GOGO Expressin Y-tunnus on
  varmistettu.
- **Motion** — candidate-listan "Motion" osoittautui virheelliseksi: `motion.fi` ei ole
  kuntosaliketju, vaan täysin eri alan yhtiö (Motion Oy, elokuvatuotantoyhtiö — sivu esittelee
  "Minun mereni" -dokumenttielokuvaa Itämerestä). WebSearch ei myöskään löytänyt mitään
  "Motion"-nimistä valtakunnallista kuntosaliketjua Suomesta. Ehdokas ei ole olemassa
  kuvatussa muodossa — poistettu listalta kokonaan.

## HUOMIOT

- **SATS/Elixia-fuusio** tapahtui Pohjoismaissa 2013–2014 (Kilpailuvirasto hyväksyi
  ehdollisesti, edellyttäen kahden SATS-salin myyntiä kilpailijoille). PRH:n
  "Elixia"-aputoiminimen rekisteröintipäivä (1.1.2016) on hallinnollinen jälkikirjaus,
  ei fuusion todellinen ajankohta — älä käytä sitä fuusiovuotena sivulla.
  `sats.fi` ei enää vastaa (HTTP 000) — koko Suomen liiketoiminta ajetaan **elixia.fi**:n
  kautta, "Elixia" on käytännössä SATS:n suomalainen kuluttajabrändi.
- **EasyFit ja LadyLine ovat saman yhtiön, Ab LL International Oy:n (Espoo), kaksi eri
  kuluttajabrändiä.** Tämä on sama omistuskeskittymän kaava kuin `sahkovertailupalvelut`-
  kategoriassa löydetty Effortia Oy (Sähkövertailu.fi + VertaaEnsin). Pitää avata sivulla
  näkyvästi, jotta LadyLine ja EasyFit eivät näytä kahdelta riippumattomalta kilpailijalta.
  Lisäksi EasyFit-ketjun yksittäiset keskukset ovat vielä oma kerroksensa: ne ovat
  itsenäisiä franchise-yrittäjiä (esim. Taitoset Oy, Hs Well Oy, MM Sport Club Oy, NGL
  Services Oy) — sivun mittaus kohdistuu käytännössä brändin yhteiseen verkkosivustoon
  (easyfit.fi), ei yhteen juridiseen toimijaan. Sama huomio pitää kirjata metodologiaan.
- **Kokoerot:** Fitness24Seven ja Elixia/SATS ovat isoja kansainvälisiä ketjuja;
  Fressi/Liikku/LadyLine kotimaisia, yhden konsernin sisällä toimivia ketjuja; EasyFit
  franchising-malli ilman yhtä keskusyhtiötä. Tämä kannattaa mainita, ei tasapäistää.
- Kaikki 6 löytyivät suoraan curlilla ilman JS-renderöintiä.
