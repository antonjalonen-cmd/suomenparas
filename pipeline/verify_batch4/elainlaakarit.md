# elainlaakarit — brand verification (batch 4)

## VAHVISTETUT
| slug | nimi | domain | y_tunnus | omistaja | JS | mittaus-URL |
|---|---|---|---|---|---|---|
| evidensia | Evidensia Eläinlääkäriasemat | evidensia.fi | 2494136-6 (Evidensia Eläinlääkäripalvelut Oy) | IVC Evidensia (kansainvälinen roll-up; oma sivu mainitsee "Osa IVC Evidensiaa") | ei tarvittu (curl toimi, 11 075 merkkiä) | https://evidensia.fi/ + https://evidensia.fi/yritys/laskutustiedot/ |
| vireä | Vireä Group | vireagroup.fi | 3224401-8 (Vireä Group Oy, ent. Ax VI VET FI Holding Oy) | Kansainvälinen Vetopia-konserni ("osa kansainvälistä Vetopia-konsernia, joka tarjoaa... palveluita seitsemässä maassa" — sivun oma teksti) | ei tarvittu (curl toimi) | https://www.vireagroup.fi/ + https://www.vireagroup.fi/klinikat |

Molemmat PRH-vahvistettu (avoindata.prh.fi, businessId-haku, HTTP 200, tiedot täsmäävät).

**HUOM Vireä-rekisteröinnistä:** PRH:n mainBusinessLine = "Holdingyhtiöiden toiminta" (holding-yhtiö,
TOIMI4-koodi 64210). Vireä Group Oy on siis emo-/holdingyhtiö klinikoiden verkostolle, ei
välttämättä jokaisen yksittäisen klinikan operatiivinen y-tunnus. Tämä ei ole karsintaperuste
(Evidensiankin taustalla toimii sama roll-up-logiikka aputoiminimillä), mutta on syytä mainita
build-vaiheessa hinnasto-/sopimusehtosivuja etsittäessä — yksittäisen klinikan laskutustiedoissa
saattaa olla eri y-tunnus kuin Vireä Group Oy:n.

## KARSITUT
- **Univet** — univet.fi (ja www.univet.fi) tekee HTTP 200 -uudelleenohjauksen suoraan
  evidensia.fi:hin (final URL = evidensia.fi molemmilla). PRH-haku Evidensian y-tunnuksella
  (2494136-6) listaa "UniVet Eläinlääkäriasema Tampere" ja "UniVet Raisio" rekisteröityinä
  aputoiminimiksi (type "3") saman y-tunnuksen alle vuodesta 2015 lähtien. Univet ei siis ole
  enää itsenäinen brändi vaan sama yhtiö kuin Evidensia — karsittu duplikaattina, ei erillisenä
  kilpailijana.
- **Omaeläinklinikka** — omaelainklinikka.fi (www ja ilman) tekee saman HTTP 200 -uudelleenohjauksen
  evidensia.fi:hin. PRH vahvistaa: "Omaeläinklinikka" on Evidensian (2494136-6) aputoiminimi,
  rekisteröity 2022-09-30. Taustalla (Cision-tiedote, ei yrityksen oma sivu, ei käytetty
  vahvistuslähteenä mutta kontekstiksi): Omaeläinklinikka syntyi Suomen Pieneläinklinikat +
  Tuhatjalka -yhdistymisestä n. 2019-2021 tavoitteena kasvaa valtakunnalliseksi ketjuksi, ja
  IVC Evidensia osti tämän kokonaisuuden myöhemmin — sama aputoiminimi-rekisteröintipäivä
  (30.9.2022) kuin usealla muullakin Evidensian aputoiminimellä tukee tätä. Karsittu
  duplikaattina.
- **Mevet** (Eläinsairaala Mevet) — mevet.fi tekee saman HTTP 200 -uudelleenohjauksen
  evidensia.fi:hin, ja "Eläinsairaala Mevet" esiintyy Evidensian omalla etusivulla yhtenä sen
  24h-eläinsairaaloista (Helsinki). Karsittu duplikaattina — sama yhtiö kuin Evidensia.
- **AniCura** — anicura.fi ja www.anicura.fi eivät vastaa mitään (HTTP 000, 0 tavua molemmilla
  yrityksillä — rehellinen fetch-epäonnistuminen, ei keksitty selitystä). anicura.com on TÄYSIN
  ERI yritys (yhdysvaltalainen lemmikkien ihonhoitotuotteita myyvä verkkokauppa, ei eläinlääkäri-
  ketju — nimikkeistön sattuma). Oikean, Mars Inc:n omistaman eläinlääkäriketjun virallinen
  ryhmäsivu anicuragroup.com listaa toimintamaansa: Itävalta, Belgia, Tanska, Ranska, Saksa,
  Italia, Norja, Portugali, Espanja, Ruotsi, Sveitsi, Alankomaat, Puola — 13 maata, EI Suomea.
  AniCura ei siis toimi Suomessa lainkaan. Karsittu: ei läsnäoloa Suomen markkinoilla.

## HUOMIOT

**Tämä kategoria ei täytä 5-9 brändin tavoitetta — vain 2 aitoa, erillistä valtakunnallista
ketjua löytyi, eikä kolmatta ole olemassa.** Alkuperäisestä 5 kandidaatin listasta (Evidensia,
Univet, AniCura, Omaeläinklinikka, Mevet) kolme (Univet, Omaeläinklinikka, Mevet) osoittautuivat
saman yhtiön (Evidensia) eri brändinimiksi/aputoiminimiksi — verkkotunnukset ohjaavat kaikki
suoraan evidensia.fi:hin ja PRH vahvistaa saman y-tunnuksen. AniCura ei toimi Suomessa lainkaan.
Jäljelle jää siis vain Evidensia + yksi lisälöytö (Vireä Group), jonka löysin web-hausta koska
alkuperäinen kandidaattilista ei sisältänyt sitä.

Web-haku (ei yrityksen oma sivu — vain suunnannäyttäjänä, ei vahvistuslähteenä) toistuvasti
kuvaa Suomen lemmikkieläinlääkärimarkkinaa nimenomaan **kahden ulkomaisen pääomasijoittajan
omistaman ketjun duopolina**: Evidensia (IVC Evidensia, n. 40-50 % markkinaosuus pieneläin-
palveluista) ja Vireä Group (Vetopia-konserni, n. 10-20 % markkinaosuus, tullut markkinoille
2021). Kaikki muut löydetyt nimet (Vet112, VETEK, Kaarinan Eläinlääkäriasema, Eläinsairaala
Aisti, Suomen eläinlääkärit -hakemistosivusto jne.) ovat joko yksittäisiä paikallisia klinikoita
tai hakemistoja/vertailusivustoja, eivät valtakunnallisia ketjuja — samaa "vain paikallinen"
-ongelmaa jota QUEUED_CATEGORIES.md varoittaa muissakin kategorioissa (esim. autokoulut).

Huomionarvoinen löydös samalla hausta: **Eläinsairaala Aisti** (aisti.info, Vantaan Myyrmäki)
markkinoi itseään omalla sivullaan "Suomen suurin itsenäinen yksityinen eläinsairaala"
(= väitetysti riippumaton), mutta esiintyy Vireä Groupin omalla /klinikat-sivulla yhtenä sen
klinikoista. Tätä ei tarvinnut ratkaista tämän kategorian kannalta (Aisti ei ollut oma
kandidaattinsa, vain yksi Vireän 26 klinikasta), mutta jos Aisti nousisi joskus omaksi
kandidaatikseen jossain toisessa kategoriassa, "itsenäinen"-väite kaipaisi tarkistusta —
sama ilmiö kuin Väre/Risicum-tapauksissa: markkinointiteksti ei päivity omistajanvaihdoksen
mukana.

**Suositus Antonille:** kategoria "Eläinlääkärit" ei tällä hetkellä täytä pipelinen
"aidot valtakunnalliset ketjut" -kynnystä riittävän monella toimijalla ollakseen mielekäs
vertailu (2 ketjua = ei oikeasti "vertailu", lähempänä duopoli-esittelyä). Vaihtoehdot:
(a) älä julkaise `elainlaakarit` tässä batchissa, käytä varakategoriaa kuten
`lampopumppuasentajat`/`aurinkopaneeliasentajat` (jo mainittu autokoulut-varasuunnitelmassa),
tai (b) julkaise vain 2 riviä ja otsikoi sivu rehellisesti duopolina, ei "9 ketjun vertailuna" —
Anton päättää, ei tätä improvisoida rakennusvaiheessa.

Ei bottisuojausta, ei consent-bannereita kohdattu millään sivustolla tämän tutkimuksen aikana.
Kaikki fetchit tehty pipeline/fetch_page.py:llä, ei WebFetchillä (ei estoja kohdattu, --js ei
tarvittu kertaakaan — kaikki sivut olivat curl-yhteensopivia).
