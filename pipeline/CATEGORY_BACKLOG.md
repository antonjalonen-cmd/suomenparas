# Kategoriajono — autopilot ottaa ylimmän vapaan `[ ]` rivin

Tilat: `[ ]` vapaa · `[~]` työn alla (varattu, merkitse + committaa HETI) ·
`[x]` julkaistu · `[s]` hylätty (syy riville).

Live-kategoriat (41 kpl, 24.7.2026): lainavertailu, vakuutukset (5 alasivua),
sahkosopimukset, laajakaista, pankit, puhelinliittymat, kulutusluotot,
luottokortit, sijoitusalustat, sahkovertailupalvelut, webhotellit,
vpn-palvelut, salasananhallintapalvelut, pilvitallennuspalvelut,
virustorjuntaohjelmat, suoratoistopalvelut, kiinteistonvalittajat,
muuttopalvelut, siivouspalvelut, autokoulut, autokatsastus, autokorjaamot,
autovuokraamot, rengasliikkeet, kuntosalit, optikot, hammaslaakarit,
yksityislaakarit, lakifirmat, pakohuoneet, hautaustoimistot, tavaransailytys,
matkatoimistot, tilitoimistot, fysioterapia, autopesulat, tapahtumaliput.
ÄLÄ rakenna näitä uudestaan.

## Jono

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
- [~] apteekkien-verkkokaupat — varattu: autopilot-tikki 24.7.2026 — kandidaatit: Yliopiston Apteekki, Apteekki.fi?, Hyvän Mielen Apteekit?, Avainapteekit? (sääntely huomioon)
- [ ] silmasairaalat — kandidaatit: Silmäasema sairaala?, Medilaser?, Terveystalo silmäkirurgia? (KKV-kaupat kesken, tarkista)
- [~] tyonvalityspalvelut — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: Barona, Eezy, StaffPoint, Academic Work, Bolt.Works, VMP?
- [ ] varainhoito-roboneuvojat — kandidaatit: tarkista päällekkäisyys sijoitusalustat-kategorian kanssa ennen aloitusta
- [ ] kotisiivouksen-tilauspalvelut — tarkista päällekkäisyys siivouspalvelut-kategorian kanssa → todennäköisesti [s]
- [ ] aurinkopaneeliasentajat — kandidaatit: Helen aurinko?, Aurinkoenergiaa Suomesta?, Solnet?, Playgreen? (kasvava ala)
- [ ] lämpöpumppuasentajat — kandidaatit: Ilmalämpöpumppuketjut (Iver?, Elfving?), tarkista valtakunnalliset
- [~] kattoremontit — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: Kattotutka, Vesivek, Icopal Katto?, Kerabit Katto?
- [ ] ikkunaremontit — kandidaatit: Pihla, Skaala, Domus, Lammin Ikkuna, HR-Ikkunat?
- [ ] hissiyhtiot — b2b/taloyhtiö-kulma: KONE, Otis, Schindler, TK Elevator → arvioi sopiiko kuluttajasivustolle
- [ ] pesulapalvelut — kandidaatit: SOL Pesulapalvelut, Lindström (b2b?), 24 Pesula, Vistan pesulat?
- [ ] kukkakauppojen-verkkokaupat — kandidaatit: Interflora, Kukkakauppa.fi?, Bloomit?, tarkista ketjut
- [ ] lastenvaatteiden-verkkokaupat — tarkista onko ≥6 suomalaista valtakunnallista, muuten [s]
- [~] urheiluvalineketjut — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: XXL, Intersport, Stadium, Budget Sport, Partioaitta (outdoor), SGN Sportia?
- [~] huonekaluketjut — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: Isku, Asko, Sotka, Masku, Vepsäläinen, JYSK, IKEA Suomi
- [~] rautakaupat — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: K-Rauta, Stark, Bauhaus, Puuilo, Tokmanni (rautaosasto? ei), RTV?
- [~] elektroniikkaketjut — varattu: päätyösessio 24.7.2026 (batch 8) — kandidaatit: Gigantti, Verkkokauppa.com, Power, Jimm's?, Multitronic?
- [ ] optiset-verkkokaupat — tarkista päällekkäisyys optikot-kategorian kanssa → todennäköisesti [s]
