# Kategoriajono — TUNTIAUTOMAATIO PÄÄLLÄ (Anton 2.8.2026)
#
# Anton pyysi 2.8.2026: yksi uusi kategoria tunnissa. Autopilotin
# suomenparas-tikki ajaa AUTOPILOT_PLAYBOOK.md:n reseptin kerran tunnissa
# (autopilot_suomenparas_every_hours=1, autopilot_suomenparas_only=true —
# mikään muu automaatio EI ole päällä). Tikki ottaa ylimmän [ ]-rivin;
# kun jono tyhjenee, tikki tutkii 5 uutta elinkelpoista kategoriaa jonoon.

Tilat: `[ ]` vapaa · `[~]` työn alla (varattu, merkitse + committaa HETI) ·
`[x]` julkaistu · `[s]` hylätty (syy riville).

Live-kategoriat (60 kpl, 28.7.2026): lainavertailu, vakuutukset (5 alasivua),
sahkosopimukset, laajakaista, pankit, puhelinliittymat, kulutusluotot,
luottokortit, sijoitusalustat, sahkovertailupalvelut, webhotellit,
vpn-palvelut, salasananhallintapalvelut, pilvitallennuspalvelut,
virustorjuntaohjelmat, suoratoistopalvelut, kiinteistonvalittajat,
muuttopalvelut, siivouspalvelut, autokoulut, autokatsastus, autokorjaamot,
autovuokraamot, rengasliikkeet, kuntosalit, optikot, hammaslaakarit,
yksityislaakarit, lakifirmat, pakohuoneet, hautaustoimistot, tavaransailytys,
matkatoimistot, tilitoimistot, fysioterapia, autopesulat, tapahtumaliput,
apteekkien-verkkokaupat, rautakaupat, kattoremontit, tyonvalityspalvelut,
silmasairaalat, uutismediat, aikakauslehdet, huonekaluketjut, elektroniikkaketjut,
urheiluvalineketjut (+ tilitoimistoihin lisätty Smart Office).
ÄLÄ rakenna näitä uudestaan.

## Jono
- [x] autoliikkeet — julkaistu 2.8.2026 (autopilot-tikki; 7 yhtiötä, check_extracts 7/7 OK; Kamux #1 82,6, Veho viimeinen 64,2; Hartikainen karsittu: myi autokaupan Wetterille 8.3.2023, hartikainen.com nyt maarakennusyhtiö; Autokeskus: ISO 9001/14001 + Suomalaisen Työn Liitto sertit)
- [x] pikaruokaketjut — julkaistu 2.8.2026 (tikki #3 + käsiviimeistely session limitin jälkeen; 8 ketjua, check_extracts 8/8 OK; Hesburger #1 75,3, Sibylla viimeinen 36,0; 0/8 kertoo Y-tunnuksen — mittaushistorian heikoin tulos; McDonald's poistanut hinnat verkosta sovellukseen; Subway/Pancho Villa/Pizza Hut karsittu)
- [x] lastenvaatteiden-verkkokaupat — julkaistu 28.7.2026 (7 kauppaa; Reima #1 74,5; Papu konkurssi 10/2025, Polarn O. Pyret karsittu SPA+Cloudflare)
- [x] lemmikkitarvikkeiden-verkkokaupat — julkaistu 28.7.2026 (7 kauppaa; Koiranurkka #1 83,3; Faunatar ei vastaa, affiliate-aggregaattorit karsittu)
- [x] hotelliketjut — julkaistu 28.7.2026 (6 ketjua; Omena #1 78,8, Scandic viimeinen 61,0; Radisson+Best Western karsittu 403-esto)
- [x] taksipalvelut — julkaistu 28.7.2026 (8 palvelua; Lähitaksi #1 84,6, Bolt viimeinen 57,4; Kovanen karsittu rikki-SSL)
- [x] kirjakauppojen-verkkokaupat — julkaistu 28.7.2026 (6 kauppaa; Akateeminen #1 83,5; Adlibris osti Akateemisen 1.1.2026 = 2 Bonnier-kauppaa; Kirja.fi karsittu kustantajakauppana)


- [x] hautaustoimistot — julkaistu 23.7.2026 (autopilot-tikki; 7 yhtiota, check_extracts OK, LH 7/7)
- [x] matkatoimistot — julkaistu 24.7.2026 (autopilot-tikki; 10 yhtiota, check_extracts 10/10 OK, LH 10/10; Olympia #1 86.7 p)
- [x] tilitoimistot — julkaistu 24.7.2026 (paatyosessio batch 6; portit OK)
- [x] fysioterapia — julkaistu 24.7.2026 (paatyosessio batch 6; portit OK)
- [x] autopesulat — julkaistu 24.7.2026 (paatyosessio batch 6; portit OK)
- [s] kielikoulut — hylätty 23.7.2026: alle 6 vertailukelpoista yksityistä yhtiötä (markkina on kansalais/työväenopistoja; Berlitz ilman omaa fi-sivustoa, EF myy kielimatkoja, Galimatias b2b, Alfa International kuollut domain)
- [x] tavaransailytys — julkaistu 24.7.2026 (autopilot-tikki; 6 yhtiota, check_extracts 6/6 OK, LH 6/6; Kotivarasto #1 75.3 p)
- [s] kodinkonehuolto — hylätty 24.7.2026: alle 6 valtakunnallista kuluttajapalvelua — vain Hakonen ja Huoltolux ovat aidosti kansallisia; loput ovat paikallisia tai valmistajan yksimerkkisiä huoltopalveluita, joita ei voi mielekkäasti vertailla keskenaan
- [s] catering-palvelut — hylätty 24.7.2026: markkina on b2b-painotteinen (Fazer Food + Compass = sama konserni, Sodexo); kuluttajatapahtumapalvelut ovat paikallisia, ei valtakunnallisia ketjuja
- [x] festivaalit-lipunmyynti — julkaistu 24.7.2026 (slug: tapahtumaliput; 6 yhtiota, check_extracts 6/6 OK, LH 6/6; Tiketti #1 78.9, NetTicket #2 78.2, Ticketmaster viimeinen 39.3; Lippu.fi Akamai CDN mittausaukko)
- [s] ruokakassipalvelut — hylätty 24.7.2026: alle 6 valtakunnallista yhtiötä — vain Ruokaboksi ja Venner elossa; Sannan Ruokakassi ja Anton & Anton lopettivat; HelloFresh ei toimi Suomessa; Fiksuruoka/Matsmart ovat hävikkiruokapalveluita, eri kategoria
- [s] ruoan-kotiinkuljetus — hylätty 24.7.2026: alle 6 itsenäistä valtakunnallista palvelua — konsolidoitunut: Wolt (ravintola+kauppa), Foodora (ravintola), K-Ruoka verkkokauppa, S-kaupat/Foodie.fi; Oda ja Gorillas poistuneet Suomesta; K-Ruoka käyttää Wolt-toimitusta → ei riittävästi erillisiä palveluntarjoajia
- [x] apteekkien-verkkokaupat — julkaistu 24.7.2026 (autopilot-tikki; 7 yhtiota, check_extracts 7/7 OK; Nettiapteekki #1 86.3 p, Yliopiston Apteekki #2 85.0 p)
- [x] silmasairaalat — julkaistu 26.7.2026 (päätyösessio, Antonin pyyntö; 6 yhtiötä, check_extracts 6/6 OK; Mehiläinen #1 75,8; Terveystalo vaati /fi/-polut, Imperva-esto ohitettu oikeilla linkeillä ei kiertämällä)
- [x] tyonvalityspalvelut — julkaistu 26.7.2026 (päätyösessio; 8 yhtiötä, check_extracts 8/8 OK; Barona #1 68,0; palkkatieto puuttuu lähes koko alalta)
- [ ] varainhoito-roboneuvojat — kandidaatit: tarkista päällekkäisyys sijoitusalustat-kategorian kanssa ennen aloitusta
- [ ] kotisiivouksen-tilauspalvelut — tarkista päällekkäisyys siivouspalvelut-kategorian kanssa → todennäköisesti [s]
- [x] aurinkopaneeliasentajat — julkaistu 28.7.2026 (8 yhtiötä; Solarum+1KOMMA5° jaettu #1 78,5; Fortum/Vattenfall/Otovo/Naps poistuneet markkinalta; Seronin ovimyyntihuomautus kerrottu avoimesti)
- [x] lämpöpumppuasentajat — julkaistu 27.7.2026 (8 yhtiötä; Zatap #1 82,0; markkinajohtaja Tom Allen Senera vasta 59,9 — tavoitettavuus 15)
- [x] kattoremontit — julkaistu 26.7.2026 (päätyösessio; 7 yhtiötä, check_extracts 7/7 OK; Vesivek #1 77,8 täydet läpinäkyvyyspisteet + 5 serttiä; ruukkikatot.fi->ruukki.com SAME_COMPANY-poikkeus)
- [x] ikkunaremontit — julkaistu 27.7.2026 (7 yhtiötä; Pihla #1 80,5; Pihla+Tiivi=Inwido kerrottu; Fenestra/Domus kuolleet)
- [ ] hissiyhtiot — b2b/taloyhtiö-kulma: KONE, Otis, Schindler, TK Elevator → arvioi sopiiko kuluttajasivustolle
- [s] pesulapalvelut — hylätty 27.7.2026: vain 2 aidosti valtakunnallista kuluttajatoimijaa (SOL, 24 Pesula) — loput ovat 1-2 kaupungin paikallisia; sama linja kuin kodinkonehuollon hylkäys. HUOM tutkimuksesta: lorella.fi on kaapattu kasinospämmidomain, Vistan Pesula on SOL:n omistama
- [x] kukkakauppojen-verkkokaupat — julkaistu 28.7.2026 (6 yhtiötä; Lähetäkukkia.fi #1 76,5; Kukka Express hylätty anonyymi operaattori; kukkia.fi/tilaakukat.fi = affiliate-sivustoja)
- [ ] lastenvaatteiden-verkkokaupat — tarkista onko ≥6 suomalaista valtakunnallista, muuten [s]
- [x] urheiluvalineketjut — julkaistu 27.7.2026 (päätyösessio; 7 ketjua, portit OK; Partioaitta #1 78,2; Stadium 57,2 sisältösivut HTTP 500; 3 ohutta uusittu; Sportia pois)
- [x] huonekaluketjut — julkaistu 26.7.2026 (päätyösessio; 6 ketjua, portit OK; Masku #1 81,5; Asko+Sotka KARSITTU: Indoor Group konkurssi 2/2026, Sukari/Masku osti brändit, sotka.fi ohjaa masku.comiin)
- [x] rautakaupat — julkaistu 26.7.2026 (päätyösessio; 6 yhtiötä, check_extracts 6/6 OK; Puuilo #1 79,0; IKH karsittu: Cloudflare 403 myös headless-Chromelle)
- [x] elektroniikkaketjut — julkaistu 26.7.2026 (päätyösessio; 6 ketjua + Proshop ilman fi-Y-tunnusta; Jimm's #1 81,6, Verkkokauppa.com vasta 58,8 tavoitettavuus 22,5)
- [x] uutismediat — julkaistu 26.7.2026 (päätyösessio; 8 mediaa, portit OK; Yle #1 81,2; yksiköt yksittäisiä medioita ei konserneja; HS/IS=Sanoma ja IL/KL=Alma avoimesti; uutissivustojen mobiiliperf. surkea, HS 5/100)
- [x] aikakauslehdet — julkaistu 26.7.2026 (päätyösessio; 7 lehteä, portit OK; Tekniikan Maailma #1 78,4; Tiede KARSITTU: tiede.fi ohjautuu hs.fi/tiede-osioon eli ei itsenäistä sivustoa; normaalihinnan piilottelu alan selkein läpinäkyvyyspuute)
- [ ] optiset-verkkokaupat — tarkista päällekkäisyys optikot-kategorian kanssa → todennäköisesti [s]
