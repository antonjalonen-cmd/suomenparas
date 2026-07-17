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
    # ------------------------------------------------------------------ batch 2
    "kulutusluotot": {
        "slug": "kulutusluotot",
        "nimi": "Kulutusluotot",
        "nav": "Kulutusluotot",
        "h1": "Suomen paras kulutusluotto 2026",
        "yksikko": "kuluttajaluoton myöntäjää",
        "lead": ("Pisteytimme {n} Suomessa toimivaa kuluttajaluoton myöntäjää {m} mittarilla. "
                 "Tärkein kysymys: näkyykö todellinen vuosikorko julkisesti ennen hakemusta — "
                 "ja kerrotaanko, kuka luoton oikeasti myöntää?"),
        "meta_title": "Suomen paras kulutusluotto 2026 — luotonantajat pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} kuluttajaluoton myöntäjää pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Etsitkö pikavippejä?</b> Sellaista tuotetta ei käytännössä enää ole. "
             "Kuluttajaluoton korkokatto (viitekorko + 15 prosenttiyksikköä, enintään 20 %) astui "
             "voimaan 1.10.2023 ja teki lyhyestä, pienestä ja kalliista pikavipistä kannattamattoman. "
             "Brändit joko lopettivat tai venyttivät tuotteensa tavalliseksi monivuotiseksi "
             "kulutusluotoksi. Siksi tämä sivu vertailee kulutusluottoja — emme julkaise "
             "&rdquo;parhaat pikavipit&rdquo; -listaa tuotteesta, jota ei enää myydä."),
            ("<b>Brändejä on enemmän kuin luotonantajia.</b> <b>Vippi.fi ja Limiitti.fi ovat sama "
             "yhtiö kuin Saldo</b> — Saldo Bank UAB Suomen sivuliike, Y-tunnus 3273394-6. Laskemme "
             "jokaisen yhtiön kerran, emme jokaista brändiä: brändilistalta markkina näyttäisi "
             "selvästi kilpaillummalta kuin se on."),
            ("<b>Miksi Risicum puuttuu? Koska se ei enää myönnä lainaa — vaikka sivu näyttää siltä "
             "että myöntää.</b> risicum.fi on pystyssä ja sen otsikko lupaa yhä &rdquo;Laina "
             "arkielämään 10 000 euroon asti. Laina tilillesi nyt.&rdquo; Saman sivun leipätekstissä "
             "lukee kuitenkin: <i>&rdquo;Uusia nostoja Risicum Joustolainoille ei myönnetä 1.10.2023 "
             "alkaen&rdquo;</i> — eli täsmälleen siitä päivästä, jona korkokatto tuli voimaan — ja "
             "<i>&rdquo;Risicumin puhelinasiakaspalvelu on päättynyt 30.9.2024&rdquo;</i>. Kyseessä "
             "on vanhojen luottojen laskutussivu, jonka päällä on yhä vanha mainos. Elävä verkko-"
             "osoite ja lainaotsikko eivät ole todiste siitä, että yhtiö myy. Sama koskee sen "
             "aputoiminimiä <b>OK Money</b>, <b>iKassa</b> ja <b>Suomen Pienlaina</b> — kaikki ovat "
             "samaa Aurajoki Nordic Oy:tä (1998514-5)."),
            ("<b>Miksi Ferratum, Instabank ja Bank Norwegian puuttuvat?</b> Emme pystyneet "
             "vahvistamaan niitä Suomen kaupparekisteristä. <b>Ferratumin suomalainen yhtiö "
             "(Multitude SE) poistui rekisteristä 30.6.2024</b> ja luoton myöntää nykyään "
             "maltalainen Multitude Bank p.l.c.; Instabankin ja Bank Norwegianin Y-tunnuksia ei "
             "löydy PRH:n rajapinnasta lainkaan. Ne myyvät suomalaisille EU-passin turvin — mutta "
             "sovellamme samaa vaatimusta kaikkiin. <b>Euroloan</b> on kuollut brändi: luotonantaja "
             "Mash Finance meni konkurssiin 2021, ja euroloan.fi:tä pyörittää nykyään mainostoimisto "
             "(Holla Online Oy) ilman luotonantotoimintaa. <b>Credit24</b> kertoo itse lopettaneensa "
             "Suomessa, <b>Aasa</b> ei enää myönnä itse, ja <b>Blue Financen</b> kuluttajalainat "
             "ovat tauolla. <b>Fixura</b> on vertaislaina-markkinapaikka, ei luotonantaja."),
            ("<b>Emme anna talousneuvontaa emmekä suosittele luoton ottamista.</b> Vertailu kuvaa "
             "luotonantajien julkisten verkkosivujen mitattavia ominaisuuksia — ei sitä, kannattaako "
             "luottoa ottaa, eikä sitä kuka on halvin. Todellinen korko ja luottoraja ovat aina "
             "henkilökohtaisia ja riippuvat luottokelpoisuudestasi. Tämä sivu ei välitä "
             "luottohakemuksia. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
    "pankit": {
        "slug": "pankit",
        "nimi": "Pankit",
        "nav": "Pankit",
        "h1": "Suomen paras pankki 2026",
        "yksikko": "suomalaista vähittäispankkia",
        "lead": ("Pisteytimme {n} suomalaista vähittäispankkia {m} mittarilla. Tärkein kysymys: "
                 "saatko palveluhinnaston auki ilman kirjautumista — vai vasta kun olet jo asiakas?"),
        "meta_title": "Suomen paras pankki 2026 — vähittäispankit pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} suomalaista vähittäispankkia pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Tämä ei mittaa asiakaspalvelun laatua.</b> Emme tiedä kuinka kauan jonotat, kuinka "
             "hyvin sinua autetaan tai kuinka nopeasti reklamaatio ratkeaa — verkkosivulta sitä ei "
             "voi mitata, eikä tämä sivu väitä mittaavansa sitä. Pisteet kertovat, kuinka "
             "läpinäkyvästi pankki julkaisee hintansa, ehtonsa ja yhteystietonsa <i>ennen kuin</i> "
             "sinusta tulee asiakas. Se on eri asia kuin hyvä palvelu — mutta se on asia, jonka voi "
             "tarkistaa."),
            ("<b>Säästöpankki ja POP Pankki eivät ole yhtiöitä vaan pankkiryhmiä.</b> Kummankin "
             "kohdalla Y-tunnus on ryhmän keskusyhteisö (Säästöpankkiliitto osk, POP Pankkikeskus "
             "osk) — ei talletuspankki. Jokainen jäsenpankki on itsenäinen yhtiö omalla "
             "Y-tunnuksellaan ja <b>omalla palveluhinnastollaan</b>: yhtä &rdquo;Säästöpankin "
             "hinnastoa&rdquo; ei ole olemassa. Mittaamme ryhmän yhteisen sivuston. <b>Oma "
             "Säästöpankki on kokonaan eri yhtiö</b> (2231936-2) kuin Säästöpankkiryhmä, vaikka "
             "nimet muistuttavat toisiaan."),
            ("<b>Miksi listalla ei ole Handelsbankenia?</b> Se ei enää palvele suomalaisia "
             "henkilöasiakkaita: tili- ja maksupalvelut päättyivät 31.3.2025, henkilöasiakkaat "
             "siirtyivät <b>S-Pankkiin</b> 1.12.2024 ja pk-yritysasiakkaita <b>Oma Säästöpankkiin</b> "
             "1.9.2024. <b>Revolut ja N26</b> palvelevat suomalaisia, mutta niillä ei ole suomalaista "
             "Y-tunnusta eikä suomenkielistä palvelua. <b>Bank Norwegianin</b> Y-tunnusta ei löydy "
             "PRH:sta, ja <b>Svea</b> tarjoaa vain säästötilin ja luottoa — ei käyttötiliä, joten se "
             "on kulutusluotto-vertailussa. <b>Säästöpankkien Keskuspankki</b> ja <b>Bonum Pankki</b> "
             "ovat ryhmiensä keskuspankkeja, joilla ei ole kuluttaja-asiakkaita."),
        ],
    },
    "autovakuutukset": {
        "slug": "autovakuutukset",
        "nimi": "Autovakuutukset",
        "nav": "Autovakuutus",
        "h1": "Suomen paras autovakuutus 2026",
        "yksikko": "vahinkovakuutusyhtiötä",
        "lead": ("Pisteytimme {n} vakuutusyhtiön autovakuutussivut {m} mittarilla. Tärkein kysymys: "
                 "saatko hinta-arvion ennen kuin luovutat henkilötunnuksesi?"),
        "meta_title": "Suomen paras autovakuutus 2026 — vakuutusyhtiöt pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} vakuutusyhtiön autovakuutussivut pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Pohjola Vakuutus puuttuu listalta — emme onnistuneet mittaamaan sitä.</b> Tämä on meidän mittausongelmamme, ei havainto OP:sta. pohjola.fi ohjaa op.fi:hin, ja op.fi rakentaa sisältönsä JavaScriptillä: sivu vastaa HTTP 200, mutta automaattinen lukijamme saa siitä vain kirjautumiskuoren — ihminen näkee sivun normaalisti. <b>Bottisuojauksesta tai JavaScriptistä ei kuulu rangaista yhtiötä</b>, ja pisteiden antaminen sillä perusteella mitä emme nähneet olisi juuri sellainen väite, jota emme voi puolustaa. Siksi jätimme Pohjolan kokonaan pois sen sijaan että arvaisimme. Yleisemmässä <a href=\"/vakuutukset/\">Vakuutukset</a>-vertailussa (mitattu 16.7.2026) Pohjola on mukana — myös sen kohdalla lukema on epävarma samasta syystä."),
            ("<b>Mittaamme autovakuutussivun, emme yhtiötä.</b> Jokainen yhtiö on pisteytetty sen "
             "omalla autovakuutussivulla — ei etusivulla. Siksi saman yhtiön pisteet voivat poiketa "
             "koti-, matka- ja lemmikkivakuutusvertailuista: sivut ovat oikeasti erilaisia. "
             "Yleisempi vertailu on <a href=\"/vakuutukset/\">Vakuutukset</a>-sivulla."),
            ("<b>Liikennevakuutus on pakollinen, kasko ei.</b> Emme vertaile vakuutusmaksuja emmekä "
             "kerro mikä kaskotaso sinulle riittää — todellinen maksu riippuu autosta, "
             "ajokokemuksesta, bonuksista ja asuinpaikasta, eikä sitä voi lukea verkkosivulta. "
             "Mittaamme sen, kertooko yhtiö hinnan ja ehdot julkisesti ennen kuin annat tietosi."),
            ("<b>Omistus:</b> POP Vakuutus (Suomen Vahinkovakuutus Oy) on 70-prosenttisesti "
             "LähiTapiolan omistama, ja neljä yhtiötä (LähiTapiola, Fennia, Turva, Pohjantähti) on "
             "keskinäisiä eli asiakkaidensa omistamia. Demo voi sisältää affiliate-linkkejä; ne "
             "eivät vaikuta pisteisiin."),
        ],
    },
    "kotivakuutukset": {
        "slug": "kotivakuutukset",
        "nimi": "Kotivakuutukset",
        "nav": "Kotivakuutus",
        "h1": "Suomen paras kotivakuutus 2026",
        "yksikko": "vahinkovakuutusyhtiötä",
        "lead": ("Pisteytimme {n} vakuutusyhtiön kotivakuutussivut {m} mittarilla. Tärkein kysymys: "
                 "saatko hinta-arvion ennen kuin luovutat henkilötunnuksesi?"),
        "meta_title": "Suomen paras kotivakuutus 2026 — vakuutusyhtiöt pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} vakuutusyhtiön kotivakuutussivut pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Pohjola Vakuutus puuttuu listalta — emme onnistuneet mittaamaan sitä.</b> Tämä on meidän mittausongelmamme, ei havainto OP:sta. pohjola.fi ohjaa op.fi:hin, ja op.fi rakentaa sisältönsä JavaScriptillä: sivu vastaa HTTP 200, mutta automaattinen lukijamme saa siitä vain kirjautumiskuoren — ihminen näkee sivun normaalisti. <b>Bottisuojauksesta tai JavaScriptistä ei kuulu rangaista yhtiötä</b>, ja pisteiden antaminen sillä perusteella mitä emme nähneet olisi juuri sellainen väite, jota emme voi puolustaa. Siksi jätimme Pohjolan kokonaan pois sen sijaan että arvaisimme. Yleisemmässä <a href=\"/vakuutukset/\">Vakuutukset</a>-vertailussa (mitattu 16.7.2026) Pohjola on mukana — myös sen kohdalla lukema on epävarma samasta syystä."),
            ("<b>Mittaamme kotivakuutussivun, emme yhtiötä.</b> Jokainen yhtiö on pisteytetty sen "
             "omalla kotivakuutussivulla — ei etusivulla. Siksi saman yhtiön pisteet voivat poiketa "
             "auto-, matka- ja lemmikkivakuutusvertailuista. Yleisempi vertailu on "
             "<a href=\"/vakuutukset/\">Vakuutukset</a>-sivulla."),
            ("<b>Kotivakuutuksen hinta on aina henkilökohtainen</b> — se riippuu asunnon tyypistä, "
             "koosta, sijainnista, rakennusvuodesta ja valitusta turvatasosta. Emme vertaile "
             "maksuja emmekä kerro mikä turvataso sinulle riittää. Korvauskatot ja rajoitukset "
             "(esim. vuotovahingon ikävähennykset) ovat käytännössä se kohta, jossa yhtiöt eroavat "
             "eniten — siksi mittaamme erikseen, kerrotaanko ne julkisesti."),
            ("<b>Omistus:</b> POP Vakuutus on 70-prosenttisesti LähiTapiolan omistama; LähiTapiola, "
             "Fennia, Turva ja Pohjantähti ovat keskinäisiä eli asiakkaidensa omistamia. Demo voi sisältää "
             "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
    "matkavakuutukset": {
        "slug": "matkavakuutukset",
        "nimi": "Matkavakuutukset",
        "nav": "Matkavakuutus",
        "h1": "Suomen paras matkavakuutus 2026",
        "yksikko": "vahinkovakuutusyhtiötä",
        "lead": ("Pisteytimme {n} vakuutusyhtiön matkavakuutussivut {m} mittarilla. Tärkein kysymys: "
                 "näkyykö hinta ennen kuin luovutat tietosi?"),
        "meta_title": "Suomen paras matkavakuutus 2026 — vakuutusyhtiöt pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} vakuutusyhtiön matkavakuutussivut pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Pohjola Vakuutus puuttuu listalta — emme onnistuneet mittaamaan sitä.</b> Tämä on meidän mittausongelmamme, ei havainto OP:sta. pohjola.fi ohjaa op.fi:hin, ja op.fi rakentaa sisältönsä JavaScriptillä: sivu vastaa HTTP 200, mutta automaattinen lukijamme saa siitä vain kirjautumiskuoren — ihminen näkee sivun normaalisti. <b>Bottisuojauksesta tai JavaScriptistä ei kuulu rangaista yhtiötä</b>, ja pisteiden antaminen sillä perusteella mitä emme nähneet olisi juuri sellainen väite, jota emme voi puolustaa. Siksi jätimme Pohjolan kokonaan pois sen sijaan että arvaisimme. Yleisemmässä <a href=\"/vakuutukset/\">Vakuutukset</a>-vertailussa (mitattu 16.7.2026) Pohjola on mukana — myös sen kohdalla lukema on epävarma samasta syystä."),
            ("<b>Mittaamme matkavakuutussivun, emme yhtiötä.</b> Jokainen yhtiö on pisteytetty sen "
             "omalla matkavakuutussivulla — ei etusivulla. Siksi saman yhtiön pisteet voivat poiketa "
             "auto-, koti- ja lemmikkivakuutusvertailuista. Yleisempi vertailu on "
             "<a href=\"/vakuutukset/\">Vakuutukset</a>-sivulla."),
            ("<b>Rajoitukset ratkaisevat matkavakuutuksessa.</b> Urheilulajien rajaukset, ikärajat, "
             "riskimaat ja jo olemassa olevat sairaudet ovat juuri ne kohdat, joista korvauskiistat "
             "syntyvät — ja ne löytyvät vain ehdoista. Siksi mittaamme erikseen, kerrotaanko "
             "korvauskatot ja rajoitukset julkisesti. <b>Emme kerro riittääkö eurooppalainen "
             "sairaanhoitokortti</b> matkallesi; tarkista turva aina ehdoista ennen matkaa."),
            ("<b>Omistus:</b> POP Vakuutus on 70-prosenttisesti LähiTapiolan omistama; LähiTapiola, "
             "Fennia, Turva ja Pohjantähti ovat keskinäisiä. Demo voi sisältää affiliate-linkkejä; ne eivät "
             "vaikuta pisteisiin."),
        ],
    },
    "lemmikkivakuutukset": {
        "slug": "lemmikkivakuutukset",
        "nimi": "Lemmikkivakuutukset",
        "nav": "Lemmikkivakuutus",
        "h1": "Suomen paras lemmikkivakuutus 2026",
        "yksikko": "lemmikkivakuutuksen myyjää",
        "lead": ("Pisteytimme {n} lemmikkivakuutuksen myyjän sivut {m} mittarilla. Tärkein kysymys: "
                 "saatko hinta-arvion — ja kerrotaanko vuosittainen korvauskatto — ennen kuin annat "
                 "tietosi?"),
        "meta_title": "Suomen paras lemmikkivakuutus 2026 — vakuutukset pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} lemmikkivakuutuksen myyjää pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Pohjola Vakuutus puuttuu listalta — emme onnistuneet mittaamaan sitä.</b> Tämä on meidän mittausongelmamme, ei havainto OP:sta. pohjola.fi ohjaa op.fi:hin, ja op.fi rakentaa sisältönsä JavaScriptillä: sivu vastaa HTTP 200, mutta automaattinen lukijamme saa siitä vain kirjautumiskuoren — ihminen näkee sivun normaalisti. <b>Bottisuojauksesta tai JavaScriptistä ei kuulu rangaista yhtiötä</b>, ja pisteiden antaminen sillä perusteella mitä emme nähneet olisi juuri sellainen väite, jota emme voi puolustaa. Siksi jätimme Pohjolan kokonaan pois sen sijaan että arvaisimme. Yleisemmässä <a href=\"/vakuutukset/\">Vakuutukset</a>-vertailussa (mitattu 16.7.2026) Pohjola on mukana — myös sen kohdalla lukema on epävarma samasta syystä."),
            ("<b>Korvauskatto on tämän tuotteen tärkein luku.</b> Lemmikkivakuutuksessa on lähes "
             "aina vuosittainen enimmäiskorvaus, ja rotukohtaiset sekä ikään perustuvat rajoitukset "
             "ovat yleisiä — moni koirarotu on rajattu osittain ulos perinnöllisten sairauksien "
             "vuoksi. Siksi mittaamme erikseen, kerrotaanko korvauskatto ja rajoitukset julkisesti. "
             "<b>Emme vertaile vakuutusmaksuja</b>: hinta riippuu rodusta, iästä ja asuinpaikasta."),
            ("<b>POP Vakuutus puuttuu listalta, koska se ei myy lemmikkivakuutusta lainkaan</b> — "
             "tarkistimme sen tuotevalikoiman ja sivuston 17.7.2026. Kyseessä on todellinen "
             "puuttuva tuote, ei mittausvirhe. <b>Agria</b> on listan ainoa erikoistunut "
             "eläinvakuuttaja (Länsförsäkringar-ryhmä, Suomen sivuliike rek. 5.2.2016, Y-tunnus "
             "2744611-7). <b>Barkibu</b> myy Suomeen saksalaisen sivuliikkeen kautta ilman "
             "suomalaista rekisteröintiä, joten se ei ole mukana."),
            ("<b>Huomio Agrian pisteisiin:</b> agria.fi on bottisuojattu (CAPTCHA), joten "
             "ekstraktioagenttimme ei päässyt sivulle kuten ihminen pääsee. Sen kohdalla &rdquo;ei "
             "löytynyt&rdquo; ei tarkoita &rdquo;ei ole&rdquo;, ja epävarmat kohdat on pisteytetty "
             "varovaisesti &rdquo;osittain&rdquo;. Bottisuojauksesta ei kuulu rangaista yhtiötä — "
             "mutta emme myöskään voi väittää nähneemme sitä mitä emme nähneet. Demo voi sisältää "
             "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
    "sahkovertailupalvelut": {
        "slug": "sahkovertailupalvelut",
        "nimi": "Sähkövertailupalvelut",
        "nav": "Sähkövertailu",
        "h1": "Suomen paras sähkövertailupalvelu 2026",
        "yksikko": "sähkön kilpailutus- ja vertailupalvelua",
        "lead": ("Kilpailutuspalvelut vertailevat sähköyhtiöitä — me vertailemme kilpailuttajat. "
                 "Pisteytimme {n} suomalaista sähkövertailupalvelua {m} mittarilla. Tärkein kysymys: "
                 "näetkö tarjoukset ennen kuin annat yhteystietosi — ja kerrotaanko, kuka palvelun "
                 "takana on ja miten se tienaa?"),
        "meta_title": "Suomen paras sähkövertailupalvelu 2026 — kilpailuttajat pisteytettynä | Suomen Paras",
        "meta_desc": ("{n} suomalaista sähkön kilpailutuspalvelua pisteytetty läpinäkyvällä kaavalla. "
                      "Katso mistä jokainen piste tulee."),
        "notes": [
            ("<b>Omistus:</b> kaksi listan brändiä on sama yhtiö. <b>Sähkövertailu.fi ja VertaaEnsin "
             "ovat molemmat Effortia Oy:tä</b> (2261132-0), joka kertoo itse olevansa osa Alma Mediaa "
             "— sama kuvio kuin lainavertailussa, jossa Sambla Group omistaa useita \"kilpailevia\" "
             "brändejä. Mukana on myös yksi ei-kaupallinen palvelu: <b>Sahkonhinta.fi on "
             "Energiaviraston eli valtion valvontaviranomaisen ylläpitämä</b> — se toimii vertailun "
             "puolueettomana mittatikkuna."),
            ("<b>Miksi listalla on vain {n} palvelua?</b> Tarkistimme 17.7.2026 kaikkiaan 20 "
             "hakutuloksissa näkyvää \"sähkövertailua\". Yli puolet karsiutui: <b>Zmarta</b> lopetti "
             "sähkövertailunsa (sivu itse kertoo: \"ei ole tällä hetkellä toiminnassa\", päivitetty "
             "viimeksi 15.9.2023), <b>Kilpailuta-sahkosopimus.fi</b> ja <b>Sahkon-hintavertailu.fi</b> "
             "ovat saman oikean palvelun valkotarrakuoria, ja mm. <b>Halpasahko.com</b>, "
             "<b>Sähkötarjouksia.fi</b> ja <b>Vertaa-hintaa.fi</b> ovat nimettömiä affiliate-sivustoja, "
             "joilta ei löydy ylläpitäjän nimeä eikä Y-tunnusta — yksi mainosti heinäkuussa yhä Black "
             "Friday -etuja ja Väre-brändiä, joka sulautui Heleniin 31.5.2026. "
             "<b>Vertaa-kilpailuttajat.fi</b> jäi pois, koska se kertoo järjestyksensä perustuvan "
             "osin sponsorointiin eikä sen ilmoittamaa Y-tunnusta löydy kaupparekisteristä."),
            ("Kilpailutuspalvelu elää komissioista: sähköyhtiö maksaa palvelulle välitetystä "
             "sopimuksesta. Se ei tee palvelusta huonoa — mutta se tekee läpinäkyvyydestä "
             "tärkeää, ja siksi mittaamme erikseen, kerrotaanko ansaintamalli ja vertailun "
             "kattavuus avoimesti. Emme vertaile sähkön hintoja emmekä suosittele sopimuksia. "
             "Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
        ],
    },
}
