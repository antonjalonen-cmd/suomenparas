# -*- coding: utf-8 -*-
"""Per-vertical page copy. Merged into data/<vertical>.json by build_vertical.py.

The `notes` blocks are load-bearing, not filler: they publish the ownership
clusters and — deliberately — which brands were LEFT OUT and why. A comparison
site that silently drops a dead brand looks identical to one that never checked.
"""

META = {
    "vakuutukset": {
        "slug": "vakuutukset",
        "nimi": "Vakuutukset",
        "nav": "Vakuutukset",
        "h1": "Suomen paras vakuutusyhtiö 2026",
        "yksikko": "suomalaista vahinkovakuutusyhtiötä",
        "lead": ("Pisteytimme {n} suomalaista vahinkovakuutusyhtiötä {m} mittarilla: tekninen laatu, "
                 "läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Tärkein kysymys: saatko hinnan "
                 "tietää ennen kuin luovutat tietosi?"),
        "meta_title": "Suomen paras vakuutusyhtiö 2026 — vahinkovakuuttajat pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} suomalaista vahinkovakuutusyhtiötä pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Omistus:</b> POP Vakuutus (Suomen Vahinkovakuutus Oy) on 70-prosenttisesti LähiTapiolan "
             "omistama — kaksi listan brändiä on siis samassa konsernissa. Neljä yhtiötä (LähiTapiola, "
             "Fennia, Turva, Pohjantähti) on keskinäisiä eli asiakkaidensa omistamia. Näytämme omistajan "
             "jokaisen kohdalla."),
            ("<b>Miksi listalla on vain {n} yhtiötä?</b> Tarkistimme jokaisen brändin olemassaolon "
             "kaupparekisteristä 16.7.2026. Listalta puuttuvat: <b>Säästöpankki</b> (vahinkovakuutusten "
             "myynti loppui 3.6.2025, siirtymä valmis 2.1.2026), <b>Folksam</b> (sulautui Fenniaan 2019), "
             "<b>A-Vakuutus</b> (Pohjola Vakuutuksen vanha nimi), <b>Nordea</b> (myy If:n vakuutuksia omalla "
             "kanavallaan, ei oma vahinkovakuuttaja) ja <b>Aktia</b> (vain henkivakuutus). Alandia "
             "(meri/vene) ja Ålands Försäkringar (vain Ahvenanmaa) rajattiin pois, koska ne eivät myy "
             "valtakunnallista koti-/auto-/matkavakuutusta."),
            ("Emme anna vakuutusneuvontaa emmekä vertaile vakuutusmaksuja. Vertailu kuvaa yhtiöiden "
             "julkisten verkkosivujen mitattavia ominaisuuksia — todellinen vakuutusmaksu on aina "
             "henkilökohtainen ja riippuu kohteesta. Demo voi sisältää affiliate-linkkejä; ne eivät "
             "vaikuta pisteisiin."),
        ],
    },
    "sahkosopimukset": {
        "slug": "sahkosopimukset",
        "nimi": "Sähkösopimukset",
        "nav": "Sähkö",
        "h1": "Suomen paras sähköyhtiö 2026",
        "yksikko": "suomalaista sähkönmyyjää",
        "lead": ("Pisteytimme {n} valtakunnallista sähkönmyyjää {m} mittarilla: tekninen laatu, "
                 "läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Tärkein kysymys: näkyykö hinta "
                 "snt/kWh ennen kuin annat yhteystietosi?"),
        "meta_title": "Suomen paras sähköyhtiö 2026 — sähkönmyyjät pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} suomalaista sähkönmyyjää pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Omistus:</b> sähkömarkkina on keskittynyt nopeasti. <b>Helen sulautti Väre-brändin "
             "31.5.2026</b> — ja Väre oli jo sitä ennen ostanut Savon Voiman (2019), Tampereen Energian "
             "(2024) ja Kymenlaakson Sähkön (2024) vähittäismyynnit. <b>Oomi osti Lumme Energian "
             "1.1.2026</b>, ja Lumme oli aiemmin sulauttanut Loiste Sähkönmyynnin. Käytännössä moni "
             "aiemmin itsenäinen paikallisbrändi on tänään joko Helen tai Oomi."),
            ("<b>Miksi listalla ei ole Värettä?</b> Koska sitä ei enää ole — Helen sulautti sen 31.5.2026 "
             "(kaupparekisteri). Listalta puuttuvat myös <b>Fi-Nergy Voima</b> (konkurssi 21.7.2022), "
             "<b>Savon Voima</b> ja <b>Tampereen Energia</b> (myivät vähittäismyyntinsä Väreelle), "
             "<b>Lumme</b> ja <b>Loiste</b> (nyt Oomia), <b>Kymppivoima</b> (hankintayhtiö, ei myy "
             "kuluttajille) ja <b>Seiverkot</b> (sähkönsiirto, ei myyjä). Herrfors myy vain alueellisesti."),
            ("Sähkön hinta muuttuu jatkuvasti. Emme vertaile hintoja emmekä ennusta pörssisähkön "
             "kehitystä — mittaamme sen, kertooko yhtiö hintansa julkisesti ja ymmärrettävästi. Tarkista "
             "ajantasainen hinta aina yhtiön omilta sivuilta. Demo voi sisältää affiliate-linkkejä; ne "
             "eivät vaikuta pisteisiin."),
        ],
    },
    "laajakaista": {
        "slug": "laajakaista",
        "nimi": "Laajakaista",
        "nav": "Laajakaista",
        "h1": "Suomen paras laajakaistaoperaattori 2026",
        "yksikko": "suomalaista laajakaistaoperaattoria",
        "lead": ("Pisteytimme {n} suomalaista laajakaistaoperaattoria {m} mittarilla: tekninen laatu, "
                 "läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Tärkein kysymys: kertooko operaattori "
                 "kampanjan jälkeisen normaalihinnan — vai vain sen ensimmäisen kuukauden?"),
        "meta_title": "Suomen paras laajakaista 2026 — operaattorit pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} suomalaista laajakaistaoperaattoria pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Saatavuus:</b> vain Elisa, Telia ja DNA myyvät valtakunnallisesti. Loput ovat "
             "alueellisia kuituoperaattoreita — ne voivat olla erinomaisia, mutta liittymää ei voi ostaa "
             "mistä tahansa Suomesta. Saatavuusalue näkyy jokaisen kohdalla. Pisteet mittaavat "
             "verkkosivun laatua ja läpinäkyvyyttä, eivät verkon kattavuutta."),
            ("<b>Omistus:</b> <b>Saunalahti on Elisan oma brändi</b> (sulautettu 2011) ja <b>Moi Mobiili "
             "on DNA:n omistama</b> (2019 alkaen) — siksi kumpaakaan ei listata erikseen, se olisi saman "
             "yhtiön laskemista kahdesti. Valoo on entinen Adola (sama Y-tunnus). Alueellista kuituverkkoa "
             "ostavat infrastruktuurisijoittajat: MPY:n omistaa Infranode."),
            ("<b>Miksi listalla ei ole kaikkia?</b> <b>Netplaza</b> lopetti toimintansa 31.12.2021, "
             "<b>PPO</b> sulautui Elisaan 2013, <b>VLP</b> (nyk. Loihde) ja <b>SSP</b> (nyk. Finda) "
             "poistuivat teleliiketoiminnasta kokonaan. Emme myöskään listaa brändejä, joiden "
             "olemassaoloa emme pystyneet vahvistamaan kaupparekisteristä."),
        ],
    },
    "puhelinliittymat": {
        "slug": "puhelinliittymat",
        "nimi": "Puhelinliittymät",
        "nav": "Liittymät",
        "h1": "Suomen paras puhelinliittymä 2026",
        "yksikko": "suomalaista liittymäbrändiä",
        "lead": ("Pisteytimme {n} suomalaista puhelinliittymäbrändiä {m} mittarilla. Tärkein kysymys: "
                 "kertooko operaattori kampanjan jälkeisen normaalihinnan — vai vain sen ensimmäisen "
                 "kuukauden?"),
        "meta_title": "Suomen paras puhelinliittymä 2026 — operaattorit pisteytettynä | Suomen Paras",
        "meta_desc": "{n} suomalaista liittymäbrändiä pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
        "notes": [
            ("<b>Omistus:</b> vain <b>Elisalla, Telialla ja DNA:lla on oma verkko</b> — kaikki muut "
             "vuokraavat sen joltakin näistä kolmesta. <b>Moi Mobiili on DNA:n omistama</b> (2019 alkaen) "
             "ja <b>Giga Mobiili on Gigantin</b> (Elkjøp) — molemmat toimivat DNA:n verkossa. Oomi Mobiilin "
             "asiakas valitsee itse DNA:n tai Telian verkon. Kerromme jokaisen kohdalla sekä omistajan "
             "että verkon: halvin brändi voi käyttää täsmälleen samaa verkkoa kuin kallein."),
            ("<b>Saunalahti puuttuu listalta tarkoituksella:</b> se ei ole oma yhtiö vaan Elisan brändi "
             "(sulautettu 2011, sama Y-tunnus). Sen listaaminen erikseen laskisi saman yhtiön kahdesti. "
             "Samasta syystä <b>Sonera</b> ja <b>Tele Finland</b> puuttuvat — molemmat sulautuivat Telian "
             "brändiin 2017 eivätkä ole enää olemassa."),
            ("Vertailu kuvaa operaattoreiden verkkosivujen mitattavia ominaisuuksia, ei verkon kuuluvuutta "
             "tai nopeutta omalla kotiosoitteellasi. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta "
             "pisteisiin."),
        ],
    },
    "luottokortit": {
        "slug": "luottokortit",
        "nimi": "Luottokortit",
        "nav": "Luottokortit",
        "h1": "Suomen paras luottokortti 2026",
        "yksikko": "suomalaista luottokorttia",
        "lead": ("Pisteytimme {n} suomalaista luottokorttia {m} mittarilla. Tärkein kysymys: näkyykö "
                 "todellinen vuosikorko julkisesti ennen hakemista — ja kerrotaanko, kuka luoton "
                 "oikeasti myöntää?"),
        "meta_title": "Suomen paras luottokortti 2026 — kortit pisteytettynä | Suomen Paras",
        "meta_desc": "{n} suomalaista luottokorttia pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
        "notes": [
            ("<b>Kuka luoton oikeasti myöntää?</b> Kortin logo ei kerro sitä. <b>OP-Visan ja K-Plussa "
             "Mastercardin myöntää sama yhtiö</b> — OP Vähittäisasiakkaat Oyj (Y-tunnus 0751699-0); Kesko "
             "tuo vain Plussa-etuohjelman. POP Visan myöntää Bonum Pankki, ei paikallinen POP Pankki. "
             "Säästöpankki Visan myöntää Säästöpankkien Keskuspankki — <b>eri yhtiö kuin Oma Säästöpankki</b>, "
             "vaikka nimet muistuttavat toisiaan. Siksi mittaamme erikseen, kerrotaanko todellinen myöntäjä."),
            ("<b>Miksi listalla on vain {n} korttia?</b> <b>Handelsbanken</b> poistui Suomen "
             "vähittäispankkitoiminnasta 2026 ja <b>Diners Club</b> jo 2019. <b>St1:n</b> kortteja ei enää "
             "myönnetä uusille (St1 Visa päättyy 30.9.2026). <b>Klarna, N26 ja Revolut</b> tarjoavat "
             "Suomessa vain debit-kortteja — ei luottokorttia. <b>Lidlillä</b> ei ole omaa korttia ja "
             "<b>Enento</b> on luottotietoyhtiö, ei myöntäjä."),
            ("<b>Emme anna talousneuvontaa emmekä suosittele luoton ottamista.</b> Vertailu kuvaa korttien "
             "julkisten verkkosivujen mitattavia ominaisuuksia, ei sitä kannattaako luottoa ottaa. "
             "Todellinen korko ja luottoraja ovat aina henkilökohtaisia. Kuluttajaluoton koron yläraja on "
             "viitekorko + 15 prosenttiyksikköä, enintään 20 %. Maksuaikakortti (esim. charge card) ei ole "
             "sama asia kuin jatkuva luotto. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
    "sijoitusalustat": {
        "slug": "sijoitusalustat",
        "nimi": "Sijoitusalustat",
        "nav": "Sijoittaminen",
        "h1": "Suomen paras sijoitusalusta 2026",
        "yksikko": "sijoitusalustaa",
        "lead": ("Pisteytimme {n} suomalaisille sijoittajille tarkoitettua alustaa {m} mittarilla. Tärkein "
                 "kysymys: näkeekö osakekaupan hinnan ilman kirjautumista — vai vasta kun olet jo asiakas?"),
        "meta_title": "Suomen paras sijoitusalusta 2026 — alustat pisteytettynä | Suomen Paras",
        "meta_desc": "{n} sijoitusalustaa pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
        "notes": [
            ("<b>Pankki vai välittäjä?</b> Pankkien (OP, Nordea, S-Pankki, Danske) sijoituspalvelu on osa "
             "verkkopankkia, ja hinnasto jää usein kirjautumisen taakse. Välittäjillä (Nordnet, Saxo) hinnat "
             "ovat tyypillisesti julkisia. Tämä ero näkyy suoraan läpinäkyvyyspisteissä — se ei kerro kumpi "
             "on halvempi, vaan kumpi kertoo hintansa etukäteen."),
            ("<b>Mitä tähän kategoriaan kuuluu:</b> alustat, joilla voit <b>itse ostaa ja myydä osakkeita "
             "tai ETF:iä</b>. Pelkkä rahastosäästäminen tai varainhoito ei riitä — muuten vertailisimme "
             "eri tuotteita keskenään. Siksi listalta puuttuvat <b>S-Pankki</b> ja <b>Alexandria</b> "
             "(tarkistimme: vain rahastot ja varainhoito, ei osakekauppaa) sekä <b>Seligson</b> ja "
             "<b>eQ</b> (rahastoyhtiöitä; Seligson on 100 % LähiTapiolan omistama). Ne voivat olla "
             "erinomaisia — ne eivät vain ole tämän kategorian tuotteita."),
            ("<b>Miksi listalla ei ole Avanzaa?</b> Uuden tilin avaaminen vaatii ruotsalaisen henkilötunnuksen "
             "ja BankID:n — suomalainen ei käytännössä voi avata tiliä. <b>Handelsbanken</b> lopetti Suomen "
             "arvopaperipalvelut 31.5.2024 ja poistui vähittäispankkitoiminnasta. <b>Interactive Brokers, "
             "Revolut ja Lightyear</b> palvelevat suomalaisia, mutta ilman suomenkielistä palvelua."),
            ("<b>Tämä ei ole sijoitusneuvontaa.</b> Emme suosittele mitään alustaa emmekä sijoituskohdetta. "
             "Vertailu kuvaa vain alustojen verkkosivujen läpinäkyvyyttä ja teknistä laatua. Sijoittamiseen "
             "liittyy aina riski: sijoituksen arvo voi laskea. Ulkomaisten palveluntarjoajien "
             "sijoittajansuoja määräytyy niiden kotimaan järjestelmän mukaan, ei Suomen. Demo voi sisältää "
             "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
    "webhotellit": {
        "slug": "webhotellit",
        "nimi": "Webhotellit",
        "nav": "Webhotellit",
        "h1": "Suomen paras webhotelli 2026",
        "yksikko": "webhotellipalvelua",
        "lead": ("Pisteytimme {n} webhotellipalvelua {m} mittarilla. Tärkein kysymys: kerrotaanko "
                 "uusimishinta — vai vain se halpa ensimmäinen vuosi?"),
        "meta_title": "Suomen paras webhotelli 2026 — palvelut pisteytettynä | Suomen Paras",
        "meta_desc": "{n} webhotellipalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
        "notes": [
            ("<b>Omistus:</b> suomalainen webhotellimarkkina on keskittynyt rajusti. <b>Planeetta, "
             "Domainhotelli ja Hostingpalvelu.fi ovat sama yhtiö</b> (Planeetta Internet Oy, Y-tunnus "
             "1753494-9) ja omistaja on brittiläisen pääomasijoittajan taustoittama <b>team.blue</b> — "
             "siksi listalla on niistä vain yksi rivi. <b>Zonerin omistaa tanskalais-ruotsalainen One.com</b>, "
             "ja Zoner osti Telian koko suomalaisen webhotelliliiketoiminnan 1.8.2024. Aidosti itsenäisiä "
             "suomalaisia ovat Louhi, Shellit (Multim), Seravo, Capnova (Moment Digital), Kotisivut.com "
             "(Mediam) ja Hostaan."),
            ("<b>Miksi listalla ei ole Nebulaa tai Sigmaticia?</b> Ne eivät enää myy webhotelleja. "
             "Nebula sulautui Teliaan, ja Telia myi koko webhotelliliiketoimintansa (myös Sigmatic- ja "
             "Webhotelli.fi-brändit) Zonerille 1.8.2024. Nebula on nykyään Telian yritys-ICT-brändi. "
             "<b>Ficolo</b> (nyk. Verne) on konesalitoimija, ei kuluttajan webhotelli."),
            ("Vertailu kuvaa palveluiden verkkosivujen läpinäkyvyyttä ja teknistä laatua — ei palvelimien "
             "todellista nopeutta, käytettävyyttä tai tukea. Demo voi sisältää affiliate-linkkejä; ne eivät "
             "vaikuta pisteisiin."),
        ],
    },
    "vpn-palvelut": {
        "slug": "vpn-palvelut",
        "nimi": "VPN-palvelut",
        "nav": "VPN",
        "h1": "Suomen paras VPN 2026",
        "yksikko": "VPN-palvelua",
        "lead": ("Pisteytimme {n} VPN-palvelua {m} mittarilla. Tärkein kysymys yksityisyyttä myyvälle "
                 "palvelulle: kertooko se kuka sen omistaa?"),
        "meta_title": "Suomen paras VPN 2026 — palvelut pisteytettynä | Suomen Paras",
        "meta_desc": "{n} VPN-palvelua pisteytetty läpinäkyvällä kaavalla. Kuka omistaa VPN:si? Katso mistä jokainen piste tulee.",
        "notes": [
            ("<b>Viisi yhdeksästä on kahden omistajan hallussa.</b> <b>Kape Technologies omistaa "
             "ExpressVPN:n, CyberGhostin ja Private Internet Accessin</b> — kolme &rdquo;kilpailijaa&rdquo;, "
             "yksi omistaja. <b>NordVPN ja Surfshark</b> kuuluvat samaan hollantilaiseen Cyberspace B.V. "
             "-holdingiin (yhdistyivät 2/2022), joskin ne toimivat erillisinä. Yksityisyyttä myyvän "
             "palvelun kohdalla omistus ei ole sivuseikka — siksi mittaamme erikseen, kertooko palvelu itse "
             "kuka sen omistaa."),
            ("<b>Nämä eivät ole suomalaisia yrityksiä</b> — poikkeuksena <b>F-Secure</b> (Y-tunnus "
             "3269349-7, Nasdaq Helsinki), joka on listan ainoa suomalainen. Siksi Y-tunnuksen sijaan "
             "mittaamme lainkäyttöalueen ja omistajan. Lainkäyttöalue on VPN:ssä olennainen: esim. PIA "
             "toimii Yhdysvalloista ja Windscribe Kanadasta (5 Eyes -maat), Proton Sveitsistä ja "
             "Mullvad Ruotsista."),
            ("<b>Miksi Atlas VPN puuttuu?</b> Sitä ei ole enää: Nord Security lopetti palvelun 24.4.2024 ja "
             "siirsi asiakkaat NordVPN:ään. <b>Zenmate</b> sulautettiin CyberGhostiin 2023. F-Securen "
             "<b>Freedome</b> päättyi toukokuussa 2024 ja on nyt osa F-Secure-sovellusta."),
            ("Vertailu kuvaa palveluiden verkkosivujen läpinäkyvyyttä ja teknistä laatua — <b>emme testaa "
             "VPN-yhteyden nopeutta emmekä pysty todentamaan lokikäytäntöjä</b>. Riippumaton auditointi on "
             "mittari juuri siksi: se on ainoa julkinen tapa tarkistaa lupaus. Demo voi sisältää "
             "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
}
