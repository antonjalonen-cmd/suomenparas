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
            ("<b>Korjaus 18.7.2026 — Pohjola Vakuutus mitattu uudelleen:</b> alkuperäinen 16.7. mittaus "
             "tehtiin hakumenetelmällä, joka ei suorittanut JavaScriptiä — op.fi:stä näkyi vain "
             "kirjautumiskuori, ja Pohjolan hintalaskuri, ehdot ja omavastuutiedot pisteytettiin "
             "virheellisesti \"kirjautumisen takana\" -tilaan. Se oli mittausvirhe meidän päässämme, ei "
             "löydös Pohjolasta. Pohjolan rivi on mitattu uudelleen 18.7.2026 JavaScriptin renderöivällä "
             "haulla; muiden yhtiöiden tulokset ovat edelleen 16.7.2026 mittauksesta. Alkuperäinen "
             "virheellinen arvio säilyy versiohistoriassa. Täsmennys 21.7.2026 faktantarkistuksessa: "
             "hintalaskuri-kriteeri tarkennettiin tasolle Osittain, koska autovakuutuslaskuri pyytää "
             "henkilötunnuksen ennen hinnan näyttämistä, ja omavastuu-havainnon vakuutuslajimerkintä korjattiin."),
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
            ("<b>Korjaus 18.7.2026, OP-Visa mitattu uudelleen:</b> alkuperäinen 16.7. mittaus ei "
             "suorittanut JavaScriptiä, joten op.fi:stä ei latautunut mitään ja OP-Visa pisteytettiin "
             "sisällöstä, jota mittari ei koskaan nähnyt. Se oli mittausvirhe meidän päässämme. OP-Visan "
             "rivi on mitattu uudelleen 18.7.2026 JavaScriptin renderöivällä haulla; muiden korttien "
             "tulokset ovat edelleen 16.7.2026 mittauksesta. Alkuperäinen arvio säilyy versiohistoriassa."),
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
            ("<b>Korjaus 18.7.2026, OP mitattu uudelleen:</b> alkuperäinen 16.7. mittaus ei suorittanut "
             "JavaScriptiä, joten op.fi:stä näkyi vain kirjautumiskuori ja OP:n sisältöarviot perustuivat "
             "sivuun, jota mittari ei oikeasti nähnyt. Se oli mittausvirhe meidän päässämme. OP:n rivi on "
             "mitattu uudelleen 18.7.2026 JavaScriptin renderöivällä haulla; muiden alustojen tulokset ovat "
             "edelleen 16.7.2026 mittauksesta. Alkuperäinen arvio säilyy versiohistoriassa."),
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

# ---------------------------------------------------------------- batch 3 (18.7.2026)
META["autokatsastus"] = {
    "slug": "autokatsastus",
    "nimi": "Autokatsastus",
    "nav": "Katsastus",
    "h1": "Suomen paras autokatsastus 2026",
    "yksikko": "valtakunnallista katsastusketjua",
    "lead": ("Pisteytimme {n} valtakunnallista katsastusketjua {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatuarvio. Tärkein kysymys: näkyykö katsastuksen "
             "hinta ennen ajanvarausta?"),
    "meta_title": "Suomen paras autokatsastus 2026 | katsastusketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} valtakunnallista katsastusketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi listalla on vain {n} ketjua?</b> Suomessa on satoja katsastusasemia, mutta vain "
         "neljä aidosti valtakunnallista ketjua, joilla on oma verkkosivusto. Alueelliset toimijat "
         "(Katsastajasi, Go-Katsastus) ja helmikuussa 2026 saksalaiselle TÜV SÜDille myyty "
         "Q-Katsastus rajattiin pois. Pienempi oikea joukko on parempi kuin täytetty lista."),
        ("<b>Omistus:</b> A-Katsastus osti K1 Katsastajat joulukuussa 2022, joten listan kaksi "
         "suurinta ovat samaa konsernia (yhteenlaskettu markkinaosuus noin 40 %, minkä Autoliitto "
         "nosti julkisesti esiin). Yhtiöt toimivat omilla Y-tunnuksillaan ja asemillaan, joten ne "
         "mitataan erikseen, mutta omistus näytetään molempien kohdalla."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei katsastuksen "
         "laatua tai hylkäysprosentteja. Katsastushinnat vaihtelevat asemittain; vertailu mittaa "
         "kerrotaanko hinta, ei mikä se on. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta "
         "pisteisiin."),
    ],
}
META["autovuokraamot"] = {
    "slug": "autovuokraamot",
    "nimi": "Autovuokraamot",
    "nav": "Autovuokraus",
    "h1": "Suomen paras autovuokraamo 2026",
    "yksikko": "valtakunnallista autovuokraamoa",
    "lead": ("Pisteytimme {n} valtakunnallista autovuokraamoa {m} mittarilla. Tärkein kysymys: "
             "näkyykö vuokran kokonaishinta omavastuineen ennen kuin annat yhteystietosi?"),
    "meta_title": "Suomen paras autovuokraamo 2026 | vuokraamot pisteytettynä | Suomen Paras",
    "meta_desc": "{n} autovuokraamoa pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi Budget ei ole listalla?</b> Koska se on jo. Avis ja Budget ovat Suomessa saman "
         "yhtiön (Helkama Rent Oy) kaksi brändiä, joten Budgetin listaaminen erikseen laskisi yhden "
         "kilpailijan kahdesti. Scandia Rent on siirtymässä ruotsalaisen Hedin Mobility Groupin "
         "MABI Mobility -brändiin, mutta palvelee yhä scandiarent.fi-osoitteessa."),
        ("Kansainväliset brändit toimivat Suomessa lisenssinhaltijoiden kautta: Hertziä operoi "
         "First Rent A Car Finland, Sixtiä Vehon Transporent ja Green Motionia franchise-yrittäjät. "
         "Näytämme todellisen suomalaisen operaattorin jokaisen brändin kohdalla."),
        ("Vertailu kuvaa vuokraamojen julkisten verkkosivujen mitattavia ominaisuuksia. Todellinen "
         "vuokrahinta riippuu aina ajankohdasta, autoluokasta ja toimipisteestä; vertailu mittaa "
         "kerrotaanko hinta ja ehdot avoimesti, ei mikä hinta on. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}
META["optikot"] = {
    "slug": "optikot",
    "nimi": "Optikot",
    "nav": "Optikot",
    "h1": "Suomen paras optikkoketju 2026",
    "yksikko": "valtakunnallista optikkoketjua",
    "lead": ("Pisteytimme {n} valtakunnallista optikkoketjua {m} mittarilla. Tärkein kysymys: "
             "kerrotaanko silmälasien ja näöntarkastuksen hinnat ennen liikkeeseen astumista?"),
    "meta_title": "Suomen paras optikkoketju 2026 | optikot pisteytettynä | Suomen Paras",
    "meta_desc": "{n} optikkoketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi Nissen ei ole listalla?</b> Koska se on jo. Instrumentarium ja Nissen ovat saman "
         "yhtiön (Instru Optiikka Oy, osa globaalia EssilorLuxottica-konsernia) kaksi brändiä — "
         "erikseen listattuna yksi yhtiö saisi kaksi sijoitusta."),
        ("<b>Silmäasema on kaupan alla:</b> Terveystalo ilmoitti 8.6.2026 ostavansa Silmäaseman, "
         "mutta kauppa ei ollut mittaushetkellä toteutunut. Silmäasema mitattiin itsenäisenä "
         "yhtiönä; omistustilanne tarkistetaan jokaisella päivityskierroksella."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei linssien tai "
         "kehysten laatua. Emme anna terveydenhuollon suosituksia. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}
META["yksityislaakarit"] = {
    "slug": "yksityislaakarit",
    "nimi": "Yksityislääkärit",
    "nav": "Lääkärit",
    "h1": "Suomen paras yksityinen lääkäriketju 2026",
    "yksikko": "valtakunnallista lääkäriketjua",
    "lead": ("Pisteytimme {n} valtakunnallista yksityistä lääkäriketjua {m} mittarilla. Tärkein "
             "kysymys: näkyykö vastaanoton hinta ennen ajanvarausta?"),
    "meta_title": "Suomen paras yksityinen lääkäriketju 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} yksityistä lääkäriketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi listalla on vain {n} ketjua?</b> Suomessa on neljä aidosti valtakunnallista "
         "yksityistä lääkäriketjua. Tarkistimme myös muut ehdokkaat: <b>Diacor</b> sulautui "
         "Terveystaloon jo 2016 (diacor.fi palvelee nykyään täysin eri sivustoa), ja alueelliset "
         "tai yhden erikoisalan toimijat rajattiin pois. Pienempi oikea joukko on parempi kuin "
         "täytetty lista."),
        ("<b>Tämä ei ole hoitosuositus.</b> Vertailu kuvaa ketjujen julkisten verkkosivujen "
         "mitattavia ominaisuuksia: hintojen näkyvyyttä, ajanvarauksen sujuvuutta ja "
         "tavoitettavuutta. Se ei mittaa hoidon laatua, lääkäreiden osaamista eikä jonotusaikoja. "
         "Hätätilanteessa soita 112."),
        ("Vastaanottojen hinnat vaihtelevat toimipisteittäin ja lääkäreittäin; vertailu mittaa "
         "kerrotaanko hinnat avoimesti, ei mikä hinta on. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}
META["kuntosalit"] = {
    "slug": "kuntosalit",
    "nimi": "Kuntosalit",
    "nav": "Kuntosalit",
    "h1": "Suomen paras kuntosaliketju 2026",
    "yksikko": "valtakunnallista kuntosaliketjua",
    "lead": ("Pisteytimme {n} valtakunnallista kuntosaliketjua {m} mittarilla. Tärkein kysymys: "
             "kerrotaanko jäsenyyden hinta ja irtisanomisehdot ennen sopimuksen tekoa?"),
    "meta_title": "Suomen paras kuntosaliketju 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} kuntosaliketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Omistus:</b> LadyLine ja EasyFit ovat saman franchisoijan (Ab LL International Oy) "
         "kaksi brändiä — kaksi listan nimeä on siis samaa järjestelmää, ja yksittäiset salit ovat "
         "itsenäisten yrittäjien yhtiöitä. Elixia on osa pohjoismaista SATS-konsernia. Näytämme "
         "omistajan jokaisen kohdalla."),
        ("<b>Miksi listalla ei ole enempää ketjuja?</b> Tarkistimme myös muut ehdokkaat: GOGO on "
         "Tampereen seudun paikallinen, ja \"Motion\"-ketjua ei ole olemassa. Paikalliset salit "
         "eivät kuulu valtakunnalliseen vertailuun."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei salien "
         "varustelua tai palvelun laatua. Jäsenhinnat vaihtelevat paikkakunnittain; vertailu "
         "mittaa kerrotaanko hinta ja ehdot avoimesti. Demo voi sisältää affiliate-linkkejä; ne "
         "eivät vaikuta pisteisiin."),
    ],
}
META["kiinteistonvalittajat"] = {
    "slug": "kiinteistonvalittajat",
    "nimi": "Kiinteistönvälittäjät",
    "nav": "Kiinteistönvälitys",
    "h1": "Suomen paras kiinteistönvälitysketju 2026",
    "yksikko": "valtakunnallista kiinteistönvälitysketjua",
    "lead": ("Pisteytimme {n} valtakunnallista kiinteistönvälitysketjua {m} mittarilla. Tärkein "
             "kysymys: kerrotaanko välityspalkkio ennen kuin luovutat yhteystietosi?"),
    "meta_title": "Suomen paras kiinteistönvälittäjä 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} kiinteistönvälitysketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Ketju ei aina ole yksi yhtiö.</b> OP Koti on noin 19 alueellisen osuuspankkien "
         "omistaman yhtiön federaatio ilman yhtä Y-tunnusta, ja Habitan kaupunkitoimistot ovat "
         "erillisiä osakeyhtiöitä. RE/MAX- ja Kiinteistömaailma-toimistot ovat itsenäisiä "
         "franchise-yrittäjiä. Bo LKV on poikkeus: yksi yhtiö koko maassa. Rakenne on merkitty "
         "jokaisen kohdalle, koska se vaikuttaa siihen, keneltä palkkiosta voi kysyä."),
        ("<b>Miksi SKV ei ole listalla?</b> Se sulautui Huoneistokeskukseen jo 2020 — skv.fi ohjaa "
         "nykyään Huoneistokeskuksen sivuille. Alueelliset ketjut (Aninkainen, Solid House, Roof "
         "Group) rajattiin pois valtakunnallisuussäännön perusteella."),
        ("Välityspalkkiot ovat aina neuvoteltavissa ja vaihtelevat kohteittain; vertailu mittaa "
         "kerrotaanko palkkiotaso ja palvelun sisältö avoimesti etukäteen, ei mikä palkkio on. "
         "Emme välitä asuntoja emmekä anna sijoitusneuvontaa. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}

# ---------------------------------------------------------------- batch 4a (21.7.2026)
META["lakifirmat"] = {
    "slug": "lakifirmat",
    "nimi": "Lakifirmat",
    "nav": "Lakifirmat",
    "h1": "Suomen paras lakifirma 2026",
    "yksikko": "valtakunnallista lakipalvelua",
    "lead": ("Pisteytimme {n} kuluttajille lakipalveluja tarjoavaa toimijaa {m} mittarilla. "
             "Tärkein kysymys: kerrotaanko hinta ennen kuin otat yhteyttä?"),
    "meta_title": "Suomen paras lakifirma 2026 | lakipalvelut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} valtakunnallista lakipalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Kaksi eri palvelumallia samalla listalla:</b> digitaaliset asiakirjapalvelut (Aatos, "
         "Lakitie, DIY Lakipalvelu) myyvät kiinteähintaisia asiakirjoja verkossa, perinteiset "
         "toimistot (Lindblad, Heikkilä &amp; Co) ja lakipuhelinpalvelu (Minilex) henkilökohtaista "
         "neuvontaa. Vertailu mittaa molemmilta samaa asiaa: kertooko sivusto hinnan ja tekijöiden "
         "pätevyyden etukäteen. <b>Asianajotoimisto</b> on valvottu nimike (Asianajajaliitto); "
         "lakiasiaintoimisto ja lakipalvelu eivät ole — siksi pätevyyden avoimuus on oma mittarinsa."),
        ("<b>Miksi listalla on juuri nämä toimijat?</b> Tarkistimme jokaisen ehdokkaan "
         "kaupparekisteristä 21.7.2026. <b>Lexly</b> (ent. Avtal24) on lakannut 22.12.2025 — "
         "domain ei vastaa, vaikka vanhoja suosituksia näkyy yhä verkossa. <b>Docue ja "
         "Sopimustieto</b> ovat sama yhtiö, joka palvelee nykyään vain yrityksiä. "
         "<b>Eversheds Sutherland</b> on mukana kansainvälisenä asianajotoimistona, vaikka sen "
         "asiakaskunta on pääosin yrityksiä — se mitataan samoilla kuluttajan "
         "läpinäkyvyysmittareilla kuin muutkin. Alueelliset toimistot rajattiin pois "
         "valtakunnallisuussäännöllä."),
        ("<b>Tämä ei ole oikeudellista neuvontaa.</b> Vertailu kuvaa palveluiden julkisten "
         "verkkosivujen mitattavia ominaisuuksia, ei juridisen työn laatua. Monimutkaisessa "
         "asiassa asiakirja-automaatti ei korvaa juristia. Hinnat vaihtelevat toimeksiannon "
         "mukaan; vertailu mittaa kerrotaanko hinnoittelu avoimesti. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}
META["pakohuoneet"] = {
    "slug": "pakohuoneet",
    "nimi": "Pakohuoneet",
    "nav": "Pakohuoneet",
    "h1": "Suomen paras pakohuone 2026",
    "yksikko": "monikaupunkista pakohuoneketjua",
    "lead": ("Pisteytimme {n} usealla paikkakunnalla toimivaa pakohuoneyritystä {m} mittarilla. "
             "Tärkein kysymys: näkyykö pelin hinta ja vapaat ajat ilman yhteydenottoa?"),
    "meta_title": "Suomen paras pakohuone 2026 | pakohuoneketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} monikaupunkista pakohuoneketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Pakohuoneala on rakenteellisesti paikallinen: valtaosa "
         "Suomen pakohuoneista on yhden kaupungin yrityksiä. Listalla ovat kaikki löytämämme "
         "usean paikkakunnan toimijat sekä helsinkiläinen Amazed — jokaisen rivin kattavuus "
         "(montako kaupunkia) on merkitty omistajatietoon, joten yhden ja yhdeksän kaupungin "
         "toimijaa ei sekoiteta keskenään. <b>Room Escape Finland</b> on karsittu: yhtiö "
         "asetettiin konkurssiin 13.2.2026."),
        ("<b>Omistus:</b> Truescape ja Mysteeri ovat saman yhtiön (Truescape Oy) kaksi brändiä — "
         "yhdessä 9 kaupunkia, mitattu yhtenä rivinä. Pakotarinat on myynyt toimipisteensä "
         "(Espoo Truescapelle, Joensuu Huonepakopelille) eikä toimi enää omana ketjunaan, "
         "vaikka nimi näkyy yhä vanhoissa hakemistoissa."),
        ("Vertailu kuvaa yritysten julkisten verkkosivujen mitattavia ominaisuuksia, ei pelien "
         "hauskuutta tai huoneiden laatua. Pelikokemuksesta kertovat asiakasarviot, joiden "
         "näkyvyys sivustolla on yksi mittareistamme. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}

META["hammaslaakarit"] = {
    "slug": "hammaslaakarit",
    "nimi": "Hammaslääkärit",
    "nav": "Hammaslääkärit",
    "h1": "Suomen paras hammaslääkäriketju 2026",
    "yksikko": "valtakunnallista hammaslääkäriketjua",
    "lead": ("Pisteytimme {n} valtakunnallista yksityistä hammaslääkäriketjua {m} mittarilla. "
             "Tärkein kysymys: näkyykö hoidon hinta ennen ajanvarausta?"),
    "meta_title": "Suomen paras hammaslääkäri 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} hammaslääkäriketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Omistus kannattaa tietää:</b> Oral ei ole Mehiläisen omistama, vaan osa sveitsiläisen "
         "Jacobs Holdingin Colosseum Dental Groupia. <b>Terveystalo sopi 23.12.2025 ostavansa "
         "Hammas Hohteen</b> (88 M€) — kilpailuviranomaisen käsittely oli mittaushetkellä kesken. "
         "Jos kauppa toteutuu, kaksi listan kuudesta brändistä on samaa konsernia; tilanne "
         "tarkistetaan jokaisella päivityskierroksella. Coronarian emosijoittajalla (Cor Group) "
         "on omistusta myös Silmäasemassa (optikot-kategoria)."),
        ("<b>Tämä ei ole hoitosuositus.</b> Vertailu kuvaa ketjujen julkisten verkkosivujen "
         "mitattavia ominaisuuksia: hintojen näkyvyyttä, ajanvarauksen sujuvuutta ja "
         "tavoitettavuutta. Se ei mittaa hoidon laatua eikä hammaslääkäreiden osaamista."),
        ("Hinnat vaihtelevat toimipisteittäin ja toimenpiteittäin; vertailu mittaa kerrotaanko "
         "hinnat avoimesti, ei mikä hinta on. Demo voi sisältää affiliate-linkkejä; ne eivät "
         "vaikuta pisteisiin."),
    ],
}
META["rengasliikkeet"] = {
    "slug": "rengasliikkeet",
    "nimi": "Rengasliikkeet",
    "nav": "Rengasliikkeet",
    "h1": "Suomen paras rengasliike 2026",
    "yksikko": "valtakunnallista rengasliikeketjua",
    "lead": ("Pisteytimme {n} valtakunnallista rengasliikeketjua {m} mittarilla. Tärkein kysymys: "
             "näkyvätkö renkaiden ja asennuksen hinnat ennen yhteydenottoa?"),
    "meta_title": "Suomen paras rengasliike 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} rengasliikeketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Kuka ketjun omistaa, vaikuttaa mitä renkaita sinulle suositellaan:</b> neljä kuudesta "
         "ketjusta on rengasvalmistajan omistamia tai tukemia — Vianor (Nokian Renkaat), "
         "Euromaster (Michelin), BestDrive (Continental) ja First Stop (Bridgestone). Motonet ja "
         "RengasCenter ovat valmistajista riippumattomia. Näytämme omistajan jokaisen kohdalla."),
        ("<b>Miksi Rengasmaailma ei ole listalla?</b> Brändi on kuollut kahden uudelleenbrändäyksen "
         "jälkeen: Rengasmaailma → Rengasmarket → BestDrive. Teboil rajattiin pois, koska sillä ei "
         "ole ketjumaista rengaspalvelua."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei renkaiden "
         "tai asennustyön laatua. Hinnat vaihtelevat rengaskoon ja liikkeen mukaan; vertailu "
         "mittaa kerrotaanko ne avoimesti. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta "
         "pisteisiin."),
    ],
}

META["muuttopalvelut"] = {
    "slug": "muuttopalvelut",
    "nimi": "Muuttopalvelut",
    "nav": "Muuttopalvelut",
    "h1": "Suomen paras muuttopalvelu 2026",
    "yksikko": "valtakunnallista muuttopalvelua",
    "lead": ("Pisteytimme {n} valtakunnallista muuttopalvelua {m} mittarilla. Tärkein kysymys: "
             "saatko hinta-arvion näkyviin ilman soittoa?"),
    "meta_title": "Suomen paras muuttopalvelu 2026 | muuttofirmat pisteytettynä | Suomen Paras",
    "meta_desc": "{n} valtakunnallista muuttopalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi listalla on vain {n} yritystä?</b> Muuttoala on enimmäkseen paikallisia "
         "perheyrityksiä, joita ei voi asettaa valtakunnalliseen järjestykseen. Listalla ovat "
         "löytämämme aidosti valtakunnalliset toimijat. Karsituista kaksi oli ansoja: "
         "<b>Muuttopalvelu.com</b>-domain mainostaa yhä, vaikka sen yhtiö on lakannut 3.12.2024, "
         "ja <b>Grundell</b> on sulautunut Martela Palveluihin (6/2026) eikä palvele enää "
         "kuluttajamuuttoja."),
        ("Vertailu kuvaa yritysten julkisten verkkosivujen mitattavia ominaisuuksia, ei muuton "
         "laatua tai varovaisuutta. Muuton todellinen hinta riippuu aina kohteesta; vertailu "
         "mittaa kerrotaanko hinnoittelu ja vastuut avoimesti etukäteen. Muista kotitalousvähennys "
         "muuttopalveluista. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}
META["siivouspalvelut"] = {
    "slug": "siivouspalvelut",
    "nimi": "Siivouspalvelut",
    "nav": "Siivous",
    "h1": "Suomen paras kotisiivous 2026",
    "yksikko": "valtakunnallista kotisiivouspalvelua",
    "lead": ("Pisteytimme {n} valtakunnallista kotisiivouspalvelua {m} mittarilla. Tärkein "
             "kysymys: näkyykö siivouksen hinta ja voiko sen tilata verkossa?"),
    "meta_title": "Suomen paras kotisiivous 2026 | siivouspalvelut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} kotisiivouspalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi SOL, ISS, RTK tai L&amp;T eivät ole listalla?</b> Tarkistimme jokaisen omilta "
         "palvelusivuilta: yhdelläkään ei ole kuluttajille suunnattua kotisiivoustuotetta — ne "
         "palvelevat yrityksiä ja julkisia tiloja. Tämä on kotisiivouksen vertailu. "
         "<b>Onni kotisiivous</b> on hoivapalvelukonserni Med Groupin aputoiminimi, mikä on "
         "merkitty sen kohdalle."),
        ("Vertailu kuvaa palveluiden julkisten verkkosivujen mitattavia ominaisuuksia, ei "
         "siivouksen laatua. Kotitalousvähennys pienentää todellista hintaa merkittävästi — "
         "sen avoin kertominen on yksi mittareistamme. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}
META["autokoulut"] = {
    "slug": "autokoulut",
    "nimi": "Autokoulut",
    "nav": "Autokoulut",
    "h1": "Suomen paras autokoulu 2026",
    "yksikko": "valtakunnallista autokouluketjua",
    "lead": ("Pisteytimme {n} valtakunnallista autokouluketjua {m} mittarilla. Tärkein kysymys: "
             "näkyykö ajokortin kokonaishinta ennen ilmoittautumista?"),
    "meta_title": "Suomen paras autokoulu 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} autokouluketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Miksi listalla on vain {n} ketjua?</b> Autokouluala oli pitkään paikallinen, mutta "
         "on ketjuuntunut nopeasti: CAP ja Epic ovat kasvaneet yritysostoilla yli sadan "
         "toimipisteen ketjuiksi (Epicin taustalla pääomasijoittaja Korona Invest, jonka "
         "konserniin kuuluu myös Autokoulu Safiiri). Paikalliset yhden kaupungin autokoulut "
         "eivät kuulu valtakunnalliseen vertailuun."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei opetuksen "
         "laatua tai läpäisyprosentteja. Ajokortin kokonaishinta riippuu tarvittavien ajotuntien "
         "määrästä; vertailu mittaa kerrotaanko hinnoittelu ja kurssin sisältö avoimesti. Demo "
         "voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}

# ---------------------------------------------------------------- batch 5 (21.7.2026)
META["pilvitallennuspalvelut"] = {
    "slug": "pilvitallennuspalvelut",
    "nimi": "Pilvitallennuspalvelut",
    "nav": "Pilvitallennus",
    "h1": "Suomen paras pilvitallennuspalvelu 2026",
    "yksikko": "Suomessa myytävää pilvitallennuspalvelua",
    "lead": ("Pisteytimme {n} suomalaisille myytävää pilvitallennuspalvelua {m} mittarilla. "
             "Tärkein kysymys: näkyykö hinta euroissa ennen tilin luomista, ja kerrotaanko "
             "kuka dataasi säilyttää?"),
    "meta_title": "Suomen paras pilvitallennus 2026 | palvelut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} pilvitallennuspalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Omistus:</b> Proton Drive on saman sveitsiläisen Proton AG:n palvelu kuin listoillamme "
         "jo olevat Proton VPN ja Proton Pass. Suurten yhdysvaltalaisten (Google, Apple, Microsoft, "
         "Dropbox) EU-laskutus kulkee tyypillisesti Irlannin yksiköiden kautta — suomalaista "
         "Y-tunnusta ei sopimuskumppanilla ole, joten mittaamme kerrotaanko omistaja ja "
         "lainkäyttöalue avoimesti."),
        ("<b>Suomenkielisyys on oma mittarinsa:</b> Dropbox, pCloud ja Internxt eivät tarjoa "
         "suomenkielistä sivustoa — kolmen muun kilpailijan hinnat ja ehdot saa suomeksi. "
         "Tämä vaikuttaa läpinäkyvyyspisteisiin, koska ehtojen ymmärtäminen on osa avoimuutta."),
        ("Vertailu kuvaa palveluiden julkisten verkkosivujen mitattavia ominaisuuksia, ei "
         "tallennuksen teknistä laatua tai nopeutta. Hinnat ovat kampanjaherkkiä; vertailu "
         "mittaa kerrotaanko myös normaali uusimishinta. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}
META["salasananhallintapalvelut"] = {
    "slug": "salasananhallintapalvelut",
    "nimi": "Salasananhallintapalvelut",
    "nav": "Salasanat",
    "h1": "Suomen paras salasananhallinta 2026",
    "yksikko": "Suomessa myytävää salasananhallintapalvelua",
    "lead": ("Pisteytimme {n} salasananhallintapalvelua {m} mittarilla. Tärkein kysymys: "
             "näkyykö hinta ennen tilin luomista, ja onko tietoturva auditoitu julkisesti?"),
    "meta_title": "Suomen paras salasananhallinta 2026 | palvelut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} salasananhallintapalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Omistus kannattaa tietää:</b> NordPass on saman Nord Security -konsernin palvelu "
         "kuin NordVPN, ja Proton Pass saman Proton AG:n kuin Proton VPN ja Proton Drive — "
         "tuttu nimi listalla voi siis olla saman yhtiön toinen tuote. LastPass itsenäistyi "
         "GoTo-konsernista 2024 pääomasijoittajien omistukseen."),
        ("<b>Miksi KeePass ei ole listalla?</b> Se on avoimen lähdekoodin yhteisöprojekti ilman "
         "yhtiötä, hinnoittelua tai kuluttajapalvelua — erinomainen työkalu osaajalle, mutta ei "
         "vertailukelpoinen kaupallinen palvelu. Bitwarden on mukana, koska sen takana on yhtiö "
         "ja julkinen hinnoittelu, vaikka koodi on avointa."),
        ("Vertailu kuvaa palveluiden julkisten verkkosivujen mitattavia ominaisuuksia. "
         "Salasanaturvassa auditointien julkisuus on poikkeuksellisen tärkeää — siksi se on "
         "oma 20 pisteen mittarinsa. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta "
         "pisteisiin."),
    ],
}
META["autokorjaamot"] = {
    "slug": "autokorjaamot",
    "nimi": "Autokorjaamot",
    "nav": "Autokorjaamot",
    "h1": "Suomen paras autokorjaamoketju 2026",
    "yksikko": "valtakunnallista korjaamoketjua",
    "lead": ("Pisteytimme {n} valtakunnallista autokorjaamoketjua {m} mittarilla. Tärkein "
             "kysymys: saatko huollon hinnan ja ajan verkosta ilman soittoa?"),
    "meta_title": "Suomen paras autokorjaamo 2026 | ketjut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} autokorjaamoketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Ketju ei ole yksi yhtiö:</b> suomalaiset korjaamoketjut ovat varaosatukkureiden "
         "konsepteja, joissa yksittäiset korjaamot ovat itsenäisiä yrittäjiä — Autoasin takana "
         "on Örum, Fixuksen takana Ruotsin pörssin MEKO-konserni, Autofitin takana Atoy ja "
         "AD Autohuollon takana AD FIN. Motonet-korjaamot ja Euromaster Autohuolto esiintyvät "
         "myös rengasliikkeet-vertailussa: sama yhtiö, eri palvelu ja eri mittaussivu."),
        ("<b>Miksi Bosch Car Service ei ole listalla?</b> Se on löyhä brändiverkosto ilman "
         "suomalaista vastuuyhtiötä, jonka sivustoa voisi mitata — sama syy jolla karsimme "
         "aiemmin OpusLex-verkoston. Mekonomen karsittiin, koska se on samaa MEKO-konsernia "
         "kuin jo listattu Fixus."),
        ("Vertailu kuvaa ketjujen julkisten verkkosivujen mitattavia ominaisuuksia, ei "
         "korjaustyön laatua. Huoltojen hinnat riippuvat automallista; vertailu mittaa "
         "kerrotaanko hinnoittelu avoimesti etukäteen. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}

META["suoratoistopalvelut"] = {
    "slug": "suoratoistopalvelut",
    "nimi": "Suoratoistopalvelut",
    "nav": "Suoratoisto",
    "h1": "Suomen paras suoratoistopalvelu 2026",
    "yksikko": "Suomessa myytävää suoratoistopalvelua",
    "lead": ("Pisteytimme {n} suomalaisille myytävää suoratoistopalvelua {m} mittarilla. "
             "Tärkein kysymys: kerrotaanko kuukausihinta, tasojen erot ja irtisanominen "
             "selkeästi ennen tilaamista?"),
    "meta_title": "Suomen paras suoratoistopalvelu 2026 | palvelut pisteytettynä | Suomen Paras",
    "meta_desc": "{n} suoratoistopalvelua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Omistus liikkuu tällä alalla nopeasti:</b> MTV Katsomo+ siirtyi norjalaisen "
         "Schibstedin omistukseen 1.7.2025 (aiemmin Telia), HBO Max palasi vanhaan nimeensä ja "
         "Apple pudotti plussan Apple TV:stä. Ruutu+ ja MTV Katsomo+ ovat listan ainoat "
         "suomalaisyhtiöiden palvelut. Näytämme omistajan jokaisen kohdalla."),
        ("Vertailu kuvaa palveluiden julkisten verkkosivujen mitattavia ominaisuuksia, ei "
         "sisältökirjaston laatua tai makuasioita. Hinnat ja mainostasot muuttuvat usein; "
         "vertailu mittaa kerrotaanko ne avoimesti ennen tilaamista. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}
META["virustorjuntaohjelmat"] = {
    "slug": "virustorjuntaohjelmat",
    "nimi": "Virustorjuntaohjelmat",
    "nav": "Virustorjunta",
    "h1": "Suomen paras virustorjunta 2026",
    "yksikko": "Suomessa myytävää virustorjuntaohjelmaa",
    "lead": ("Pisteytimme {n} suomalaisille myytävää virustorjuntaohjelmaa {m} mittarilla. "
             "Tärkein kysymys: kerrotaanko ensimmäisen vuoden tarjouksen lisäksi myös "
             "uusimishinta, ja kuka ohjelmiston oikeasti omistaa?"),
    "meta_title": "Suomen paras virustorjunta 2026 | ohjelmat pisteytettynä | Suomen Paras",
    "meta_desc": "{n} virustorjuntaohjelmaa pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Kolme listan kahdeksasta brändistä on samaa yhtiötä:</b> Gen Digital omistaa "
         "Nortonin, Avastin ja AVG:n — \"kilpailevat\" tuotteet voivat siis olla saman talon "
         "eri paketteja. F-Secure on listan ainoa suomalainen (sama pörssiyhtiö kuin F-Secure "
         "VPN vpn-vertailussamme). Kaspersky on venäläistaustainen; se myy edelleen Suomeen, "
         "eikä EU:lla ollut mittaushetkellä kuluttajamyynnin kieltoa."),
        ("<b>Miksi McAfee ei ole listalla?</b> Sen sivusto esti jokaisen hakutapamme (HTTP 403 "
         "myös renderöivällä selaimella), emmekä kierrä bottisuojauksia periaatteesta. Emme "
         "julkaise pisteitä sivustosta, jota mittarimme ei aidosti nähnyt — poissaolo on "
         "mittauksen rajoite, ei arvio McAfeen laadusta."),
        ("Alan tunnetuin kuvio on halpa ensimmäinen vuosi ja hiljaa moninkertaistuva "
         "uusimishinta — siksi uusimishinnan avoimuus on oma 20 pisteen mittarinsa. Vertailu "
         "kuvaa sivustojen läpinäkyvyyttä, ei tunnistustarkkuutta; riippumattomat testilaitokset "
         "(AV-TEST, AV-Comparatives) mittaavat suojaustehoa. Demo voi sisältää "
         "affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}


META["hautaustoimistot"] = {
    "slug": "hautaustoimistot",
    "nimi": "Hautaustoimistot",
    "nav": "Hautaustoimistot",
    "h1": "Suomen paras hautaustoimisto 2026",
    "yksikko": "usealla paikkakunnalla palvelevaa hautaustoimistoa",
    "lead": ("Pisteytimme {n} usealla paikkakunnalla tai verkossa koko maahan palvelevaa "
             "hautaustoimistoa {m} mittarilla. Tärkein kysymys: näkyvätkö hinnat ja pakettien "
             "sisältö ennen yhteydenottoa, vaikeimmalla mahdollisella hetkellä?"),
    "meta_title": "Suomen paras hautaustoimisto 2026 | hautaustoimistot pisteytettyna | Suomen Paras",
    "meta_desc": "{n} monipaikkakuntaista hautaustoimistoa pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Hautausala on rakenteellisesti paikallinen: valtaosa Suomen "
         "hautaustoimistoista palvelee yhtä seutua. Listalla ovat löytämämme usean paikkakunnan "
         "toimijat ja koko maahan verkossa palvelevat yritykset; jokaisen rivin kattavuus on "
         "merkitty omistajatietoon. Memoria on 30+ itsenäisen perheyrityksen verkosto, jonka "
         "yhteistä sivustoa mittaus koskee."),
        ("<b>Miksi hintojen näkyvyys painaa eniten?</b> Hautajaisia järjestetään harvoin ja "
         "kesken surun. Selkeästi julkaistut hinnat ja pakettien sisältö suojaavat ostajaa "
         "tilanteessa, jossa vertailu on raskasta. Siksi hintojen ja pakettien läpinäkyvyys on "
         "puolet kategorian läpinäkyvyyspisteistä."),
        ("<b>Karsitut:</b> ArvoHautaus on vertailuportaali eikä hautaustoimisto. Muistovalkea on "
         "tietopankki. Yhden seudun paikalliset toimistot on rajattu pois, jotta vertailu pysyy "
         "reiluna: paikallinen erikoistuminen ja valtakunnallinen kattavuus ovat eri asioita."),
    ],
}

META["matkatoimistot"] = {
    "slug": "matkatoimistot",
    "nimi": "Matkatoimistot",
    "nav": "Matkatoimistot",
    "h1": "Suomen paras matkatoimisto 2026",
    "yksikko": "valtakunnallista matkatoimistoa",
    "lead": ("Pisteytimme {n} valtakunnallisesti palvelevaa matkatoimistoa ja matkanjärjestäjää "
             "{m} mittarilla. Tärkein kysymys: näkyvätkö matkojen hinnat ja ehdot ennen "
             "varausta, ja onnistuuko varaus verkossa?"),
    "meta_title": "Suomen paras matkatoimisto 2026 | matkatoimistot pisteytettyna | Suomen Paras",
    "meta_desc": "{n} valtakunnallista matkatoimistoa pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Suomessa valmismatkoja ja matkapalveluja myyvät sekä suuret "
         "kansainväliset konsernit (Tjäreborg/Ving, Apollomatkat/DERTOUR) että kotimaiset "
         "yhtiöt (Aurinkomatkat/Finnair, Matkapojat, Lomalinja, Pohjolan Matka, Olympia, "
         "Aventura, IMT). Omistus on merkitty jokaiselle riville."),
        ("<b>Kuolleet brändit karsittu:</b> Detur Finland asetettiin konkurssiin lokakuussa 2022. "
         "Matkavekka-brändi kuoli Primera Travelin romahduksessa, ja domain on nykyään "
         "ulkopuolisen SEO-sivusto, jolla ei ole tekemistä matkatoimiston kanssa. Matka-Agentit "
         "on sama yhtiö kuin Matkapojat, joten se ei ole listalla erikseen."),
        ("<b>TUI ei ole listalla:</b> tui.fi estää automaattisen mittauksen kokonaan "
         "botti-estolla, myös selainpohjaisen haun. Emme pisteytä arvaamalla, joten TUI "
         "jätettiin pois sen sijaan että sille julkaistaisiin epäluotettava pistemäärä. "
         "Lisäämme sen heti, kun mittaus on mahdollinen."),
    ],
}

META["tilitoimistot"] = {
    "slug": "tilitoimistot",
    "nimi": "Tilitoimistot",
    "nav": "Tilitoimistot",
    "h1": "Suomen paras tilitoimisto 2026",
    "yksikko": "valtakunnallista tilitoimistoketjua",
    "lead": ("Pisteytimme {n} valtakunnallista tai monikaupunkista tilitoimistoketjua {m} "
             "mittarilla. Tärkein kysymys: kertooko tilitoimisto hintansa ja palvelunsa "
             "julkisesti, vai vasta tarjouspyynnön jälkeen?"),
    "meta_title": "Suomen paras tilitoimisto 2026 | tilitoimistot pisteytettyna | Suomen Paras",
    "meta_desc": "{n} valtakunnallista tilitoimistoketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Suurimmat valtakunnalliset ja monikaupunkiset ketjut: "
         "pörssiyhtiöt Talenom, Aallon Group ja Administer, pohjoismaiset Aspia ja Azets sekä "
         "kotimaiset Rantalainen, Greenstep, Balanco ja Gallant. Rantalainen on konserni, jolla "
         "on kymmeniä alueyhtiöitä; mittaus koskee yhteistä sivustoa."),
        ("<b>Accountor ei ole listalla</b>, koska sen tilitoimistoliiketoiminta siirtyi "
         "Aspia-konserniin ja brändi poistui käytöstä; vanha osoite ohjaa Aspian sivulle. "
         "Fennoa on taloushallinnon ohjelmisto eikä tilitoimisto, joten sitä ei mitata tässä "
         "kategoriassa."),
        ("<b>Huomio kohdeyleisöstä:</b> tilitoimistopalvelut ostaa tyypillisesti yritys, ei "
         "kuluttaja. Mittaamme silti samaa asiaa kuin muissakin kategorioissa: kertooko "
         "palveluntarjoaja hinnat, sisällön ja ehdot julkisesti ennen yhteydenottoa."),
    ],
}


META["fysioterapia"] = {
    "slug": "fysioterapia",
    "nimi": "Fysioterapia",
    "nav": "Fysioterapia",
    "h1": "Suomen paras fysioterapiaketju 2026",
    "yksikko": "monikaupunkista fysioterapiaketjua",
    "lead": ("Pisteytimme {n} usealla paikkakunnalla toimivaa fysioterapiaketjua {m} mittarilla. "
             "Tärkein kysymys: näkyvätkö käyntihinnat ja terapeuttien pätevyydet ilman "
             "puhelinsoittoa, ja onnistuuko ajanvaraus verkossa?"),
    "meta_title": "Suomen paras fysioterapiaketju 2026 | fysioterapia pisteytettyna | Suomen Paras",
    "meta_desc": "{n} monikaupunkista fysioterapiaketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Fysioterapiaan erikoistuneet ketjut (Coronaria Fysioterapia, "
         "Kotifysio) sekä terveysjätit, joiden lääkärikeskuksissa fysioterapia on osa palvelua "
         "(Mehiläinen, Terveystalo, Pihlajalinna, Aava) ja kuntokeskusketju Fressi. Suurten "
         "terveystalojen rivit mittaavat koko sivustoa, jolta fysioterapiatiedot löytyvät."),
        ("<b>Fysios ei ole oma rivinsä</b>, koska Fysios Mehiläinen Oy sulautui Mehiläinen "
         "Oy:hyn huhtikuussa 2026 ja fysios.fi ohjaa Mehiläisen sivulle. Auron-brändi sulautui "
         "Fysiokseen jo 2020. Kela-korvaus yksityisestä fysioterapiasta palasi 1.5.2025: "
         "korvaus on 15 euroa käynniltä enintään neljästä käynnistä vuodessa, eikä lääkärin "
         "lähetettä tarvita. Loppuosa maksetaan itse, joten hintojen läpinäkyvyys ratkaisee."),
        ("<b>Mittausrajoite:</b> mehilainen.fi rajoittaa automaattista hakua, joten se "
         "mitattiin selainpohjaisella haulla. Vahvistamatta jäänyt mittari merkitään "
         "puuttuvana tietona eikä puutteena."),
    ],
}

META["autopesulat"] = {
    "slug": "autopesulat",
    "nimi": "Autopesulat",
    "nav": "Autopesulat",
    "h1": "Suomen paras autopesuketju 2026",
    "yksikko": "valtakunnallista tai monikaupunkista autopesuketjua",
    "lead": ("Pisteytimme {n} usealla paikkakunnalla toimivaa autopesuketjua {m} mittarilla. "
             "Tärkein kysymys: näkyvätkö pesujen hinnat ja ohjelmien sisältö verkossa, vai "
             "selviävätkö ne vasta pesukadulla?"),
    "meta_title": "Suomen paras autopesuketju 2026 | autopesulat pisteytettyna | Suomen Paras",
    "meta_desc": "{n} autopesuketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Asemaketjujen pesuverkostot (ABC CarWash, Neste, St1) ja "
         "pesuun erikoistuneet ketjut (Carwash, GoWash, KORREK Pro Center, CarStation). "
         "St1 Suomi Oy operoi myös Shell-asemien pesut, joten Shell ei ole listalla erikseen. "
         "Hesburgerin pesulinjat rajattiin pois, koska yhtiön sivustolla ei ole lainkaan "
         "autopesua koskevaa sisältöä, jota voisi mitata. Osa riveistä mittaa koko ketjun "
         "sivustoa, jonka osa autopesu on."),
        ("<b>Teboil ei ole listalla:</b> Lukoilin omistama Teboil on ollut marraskuusta 2025 "
         "alkaen pakotteiden kohteena, kymmeniä asemia on suljettu ja yrityskauppa on kesken. "
         "Tilanne on liian epävakaa reiluun pisteytykseen; palaamme asiaan kun omistus on "
         "selvinnyt."),
        ("<b>Karsitut:</b> Prowash myy pesulaitteita yrityksille eikä ole kuluttajaketju. "
         "Yhden kaupungin pesulat (mm. CleanCar Kuopio, Pesuparoni Lahti) on rajattu pois, "
         "jotta vertailu pysyy reiluna."),
    ],
}

META["tavaransailytys"] = {
    "slug": "tavaransailytys",
    "nimi": "Tavaransailytys",
    "nav": "Tavaransailytys",
    "h1": "Suomen paras tavaransailytys 2026",
    "yksikko": "suomalaista tavaransailytyspalvelua",
    "lead": ("Pisteytimme {n} suomalaista itsepalveluvarastoyhtiota {m} mittarilla: tekninen laatu, "
             "lapinakyvyys, tavoitettavuus ja AI-laatuarvio. Tarkein kysymys: nakyvatko "
             "varastotilan hinta ja sopimusehdot ennen kuin annat yhteystietosi?"),
    "meta_title": "Suomen paras tavaransailytys 2026 | vuokravarastot pisteytettyna | Suomen Paras",
    "meta_desc": ("{n} suomalaista tavaransailytyspalvelua pisteytetty lapinakyvalla kaavalla. "
                  "Katso mista jokainen piste tulee."),
    "notes": [
        ("<b>Cityvarasto on Suomen suurin:</b> Cityvarasto Oyj (per. 1999) on julkinen "
         "osakeyhtiö, jolla on yli 58 toimipistettä yli 15 kaupungissa. Pelican Self Storage "
         "on Pohjoismainen ketju, jolla on 14 toimipistettä paakaupunkiseudulla ja Turussa. "
         "Muut listalla olevat palvelevat useammalla kuin yhdella paikkakunnalla."),
        ("<b>Miksi listalla on vain {n} yhtiota?</b> Etsimme kansallisesti tai useassa "
         "kaupungissa toimivia kuluttajapalveluita, joilla on oma verkkosivusto. 24varasto.fi "
         "palvelee Joensuussa ja Pirkkalassa mutta sivusto oli botti-estojen takana eika "
         "ollut mitattavissa. Warasto Finland (warasto.fi) on B2B-logistiikkayhtiö ilman "
         "kuluttajatuotetta. Yhden kaupungin toimijat rajattiin pois."),
        ("Vertailu kuvaa yhtiöiden julkisten verkkosivujen mitattavia ominaisuuksia, ei "
         "varastojen fyysistä kuntoa, turvallisuuslaitteita tai kulkuyhteyksistä. Todellinen "
         "varastotilan hinta riippuu koosta, sijainnista ja sopimuksen kestosta; vertailu "
         "mittaa kerrotaanko hinta, ei mika se on. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}

META["tapahtumaliput"] = {
    "slug": "tapahtumaliput",
    "nimi": "Tapahtumaliput",
    "nav": "Tapahtumaliput",
    "h1": "Suomen paras lipunmyyntipalvelu 2026",
    "yksikko": "Suomessa toimivaa tapahtumien lipunmyyntipalvelua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa tapahtumien lipunmyyntipalvelua {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "näetkö kokonaishinnan palvelumaksuineen ennen kuin sitoudut ostoon?"),
    "meta_title": "Suomen paras lipunmyyntipalvelu 2026 | tapahtumaliput pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} tapahtumien lipunmyyntipalvelua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Miksi listalla on vain {n} palvelua?</b> Etsimme palveluita, joista suomalaiset "
         "kuluttajat oikeasti ostavat tapahtumaliput. Kolme suurinta (Ticketmaster, Lippu.fi, "
         "Tiketti) kattavat ylivoimaisen enemmistön konsertti-, festivaali-, teatteri- ja "
         "urheilulipuista. NetTicket on pienempien tapahtumajärjestäjien suosittu alusta, "
         "Kide.app palvelee opiskelijajärjestöjen tapahtumia yli 20 kaupungissa, ja Eventbrite "
         "on kansainvälinen alusta, jota kautta myydään myös suomalaisia tapahtumia."),
        ("<b>Lippu.fi ei ollut digitaalisesti mitattavissa.</b> Lippupiste Oy:n lippu.fi on "
         "Akamai-CDN:n suojaama niin, että automaattinen mittaus ei saa vastausta lainkaan. "
         "Tämä on mittausaukko meidan puoleltamme, ei havainto palvelusta. Läpinäkyvyys-, "
         "tavoitettavuus- ja AI-pillarit mitataan sivuston julkisesta sisällöstä; ne ovat "
         "mitattavissa, mutta Lighthouse-suorituskyky merkitään 'ei mitattavissa'."),
        ("<b>Omistus:</b> Ticketmaster Suomi Oy on yhdysvaltalaisen Live Nation Entertainmentin "
         "omistama (ent. Lippupalvelu Oy, perustettu 1945). Lippu.fi on saksalaisen CTS Eventiamin "
         "omistaman Lippupiste Oy:n palvelu. Tiketti Oy on Suomen suurin suomalainen lipunvälittäjä "
         "ja sen liput saa kaikista R-kioskeista. NetTicket on vaasalainen Oy NetTicket Finland Ab. "
         "Kide.app on tamperelaisen Treanglo Oy:n alusta. Eventbrite on yhdysvaltalainen eika silla "
         "ole suomalaista rekisteröintia."),
        ("Vertailu kuvaa lipunmyyntipalvelujen julkisten verkkosivujen mitattavia ominaisuuksia, "
         "ei tapahtumavalikoimaa, jonotusaikoja tai asiakaspalvelun nopeutta. Palvelumaksut "
         "vaihtelevat tapahtumittain ja ovat palvelun asettamia; vertailu mittaa kerrotaanko "
         "ne avoimesti. Demo voi sisältää affiliate-linkkejä; ne eivät vaikuta pisteisiin."),
    ],
}


META["rautakaupat"] = {
    "slug": "rautakaupat",
    "nimi": "Rautakaupat",
    "nav": "Rautakaupat",
    "h1": "Suomen paras rautakauppa 2026",
    "yksikko": "valtakunnallista rautakauppaketjua",
    "lead": ("Pisteytimme {n} valtakunnallista rautakauppaketjua {m} mittarilla. Tärkein "
             "kysymys: näkyvätkö hinnat, toimituskulut ja palautusehdot ennen kassaa?"),
    "meta_title": "Suomen paras rautakauppa 2026 | rautakaupat pisteytettyna | Suomen Paras",
    "meta_desc": "{n} rautakauppaketjua pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Suuret myymäläketjut (K-Rauta, Stark, Bauhaus, Puuilo, "
         "Byggmax, IKH) ja verkkokauppa Taloon.com. Omistus on merkitty jokaiselle riville: "
         "mukana on suomalaisia pörssiyhtiöitä ja pohjoismaisten sekä saksalaisen konsernin "
         "ketjuja."),
        ("<b>RTV ei ole listalla</b>, koska RTV-Yhtymä asetettiin konkurssiin tammikuussa "
         "2025 ja myymälät on suljettu. Kodin Terra -brändi lakkautettiin jo 2022. Kuolleiden "
         "brändien karsinta on osa jokaista mittauskierrosta."),
        ("<b>Mittausrajoite:</b> bauhaus.fi rajoittaa automaattista hakua, joten se mitattiin "
         "selainpohjaisella haulla. Vahvistamatta jäänyt mittari merkitään puuttuvana tietona "
         "eikä puutteena."),
    ],
}

META["kattoremontit"] = {
    "slug": "kattoremontit",
    "nimi": "Kattoremontit",
    "nav": "Kattoremontit",
    "h1": "Suomen paras kattoremonttiyritys 2026",
    "yksikko": "valtakunnallista tai monimaakunnallista kattoremonttiyritystä",
    "lead": ("Pisteytimme {n} usean maakunnan alueella toimivaa kattoremonttiyritystä {m} "
             "mittarilla. Tärkein kysymys: saako remontin hinnasta, vaiheista ja takuista "
             "selvän kuvan ennen myyjän soittoa?"),
    "meta_title": "Suomen paras kattoremonttiyritys 2026 | kattoremontit pisteytettyna | Suomen Paras",
    "meta_desc": "{n} kattoremonttiyritystä pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Usean maakunnan alueella toimivat kattoremonttiketjut: "
         "Kattotutka, Vesivek, Kattokeskus, Suomen KattoCenter, Kattomestarit, KerabitPro ja "
         "Ruukki Katot. Ruukki on samalla materiaalivalmistaja (SSAB-konserni) ja Kerabitin "
         "sivusto on jaettu valmistajabrändin kanssa, mikä on merkitty riveille."),
        ("<b>Laaturemontti ei ole listalla erikseen</b>, koska brändi on sulautunut "
         "Vesivekiin ja sen osoite ohjaa Vesivekin sivulle. Alueelliset yhden maakunnan "
         "toimijat (esim. Kattomaailma Pirkanmaalla) on rajattu pois."),
        ("<b>Miksi hintatieto painaa eniten?</b> Kattoremontti on tuhansien eurojen hankinta, "
         "joka myydään usein kotikäynnillä. Yritys, joka kertoo hintahaarukat, vaiheet ja "
         "takuut jo verkossa, antaa ostajalle mahdollisuuden vertailla rauhassa."),
    ],
}

META["tyonvalityspalvelut"] = {
    "slug": "tyonvalityspalvelut",
    "nimi": "Työnvälityspalvelut",
    "nav": "Työnvälitys",
    "h1": "Suomen paras henkilöstöpalveluyhtiö 2026",
    "yksikko": "valtakunnallista henkilöstöpalveluyhtiötä",
    "lead": ("Pisteytimme {n} valtakunnallista henkilöstöpalveluyhtiötä työnhakijan "
             "näkökulmasta {m} mittarilla. Tärkein kysymys: voiko avoimia paikkoja selata ja "
             "hakuprosessin ymmärtää ilman kirjautumista, ja kerrotaanko palkka?"),
    "meta_title": "Suomen paras henkilostopalveluyhtio 2026 | tyonvalitys pisteytettyna | Suomen Paras",
    "meta_desc": "{n} henkilostopalveluyhtiota pisteytetty tyonhakijan nakokulmasta. Katso mista jokainen piste tulee.",
    "notes": [
        ("<b>Keitä listalla on?</b> Suurimmat valtakunnalliset henkilöstöpalveluyhtiöt: "
         "Barona, Eezy, StaffPoint, Academic Work, Bolt.Works, Manpower, Bondata ja Adecco. "
         "Mittaus on tehty työnhakijan näkökulmasta: yrityksille myytäviä palveluita ei "
         "pisteytetä."),
        ("<b>Kuolleet brändit:</b> VMP ja Smile Henkilöstöpalvelut sulautuivat Eezyksi jo "
         "2019, ja Go On -ketju toimii nykyään nimellä Bondata. Vanhat nimet eivät siksi ole "
         "listalla erikseen."),
        ("<b>Huomio palkkatiedosta:</b> palkan tai palkkahaarukan kertominen ilmoituksessa on "
         "mittareistamme se, jossa ala on läpinäkymättömimmillään. Mittari palkitsee yhtiöt, "
         "jotka kertovat palkan jo ilmoituksessa."),
    ],
}

META["apteekkien-verkkokaupat"] = {
    "slug": "apteekkien-verkkokaupat",
    "nimi": "Apteekkien verkkokaupat",
    "nav": "Nettiapteekit",
    "h1": "Suomen paras nettiapteekki 2026",
    "yksikko": "suomalaista verkkoapteekkia",
    "lead": ("Pisteytimme {n} suomalaista verkkoapteekkia {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: näkyvätkö OTC-tuotteiden "
             "hinnat ja toimitusehdot ennen kuin luovutat tietosi?"),
    "meta_title": "Suomen paras nettiaapteekki 2026 | verkkoapteekit pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} suomalaista verkkoapteekkia pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Kaikki listatut apteekit ovat Fimean rekisteröimiä:</b> jokainen Suomessa laillisesti "
         "toimiva apteekki verkkopalvelu on Lääkealan turvallisuus- ja kehittämiskeskuksen (Fimea) "
         "hyväksymä. Luettelo laillisista verkkoapteekkipalveluista löytyy Fimean sivustolta. "
         "Pisteytyksemme ei mittaa lääketurvallisuutta — se kuvaa sivuston läpinäkyvyyttä."),
        ("<b>Omistus:</b> Yliopiston Apteekki Oy (1846816-2) on Suomen suurin apteekkiketju. "
         "Olo-apteekki Oy (2862688-1) on nopeimmin kasvava verkkoapteekki ja Euroopan "
         "verkkoapteekkiyhdistyksen (EAEP) jäsen. Apteekki 360 on Vaidia Oy:n (2279092-0) "
         "hallinnoima, Hakaniemen Ympyrätalo. Muut listatut ovat yksittäisten proviisorien "
         "apteekkeja, joilla on valtakunnallinen toimituspalvelu."),
        ("<b>Miksi listalla ei ole kaikkia apteekkeja?</b> Fimean rekisterissä on yli 200 "
         "verkkoapteekkipalvelua — valtaosa on yksittäisiä kivijalkoja joiden verkkokauppa "
         "toimii alueellisesti tai vain kanta-asiakkaille. Listalla ovat apteekit, jotka "
         "markkinoivat itseään aktiivisesti valtakunnallisena palveluna ja joiden sivusto on "
         "mitattavissa. apteekkituotteet.fi ohjaa yksittäiselle paikalliselle apteekille eika "
         "ole valtakunnallinen."),
        ("Vertailu kuvaa apteekkien verkkokauppojen julkisten sivujen mitattavia ominaisuuksia, "
         "ei lääkkeiden hintoja eikä lääkeneuvonnan laatua. Reseptilääkkeiden hinnat ovat "
         "Suomessa Kelan korvausjärjestelmän kautta lakisääteisiä — hintaero syntyy "
         "ilman reseptiä ostettavissa OTC-tuotteissa. Demo voi sisältää affiliate-linkkejä; "
         "ne eivät vaikuta pisteisiin."),
    ],
}

# ---------------------------------------------------------------- batch 8 / autopilot-tikki (24.7.2026)
META["silmasairaalat"] = {
    "slug": "silmasairaalat",
    "nimi": "Silmäsairaalat",
    "nav": "Silmasairaalat",
    "h1": "Suomen paras silmäklinikka 2026",
    "yksikko": "yksityistä silmäkirurgian tarjoajaa",
    "lead": ("Pisteytimme {n} yksityistä silmäkirurgian tarjoajaa {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: saatko silmäleikkauksen "
             "hinnan tietää ennen kuin luovutat yhteystietosi?"),
    "meta_title": "Suomen paras silmaklinikka 2026 | silmakirurgia pisteytettyna | Suomen Paras",
    "meta_desc": ("{n} yksityistä silmäkirurgian tarjoajaa pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Tärkeä muutos tulossa:</b> Terveystalo on solminut sopimuksen Silmäaseman "
         "ostamisesta Coronarialta noin 574 miljoonan euron kauppahinnalla. Kaupan odotetaan "
         "sulkeutuvan vuoden 2026 lopussa tai vuoden 2027 alussa, edellyttäen kilpailuviranomaisen "
         "hyväksyntää. Tämä mittaus on tehty 24.7.2026 ennen kaupan sulkeutumista: Silmäasema ja "
         "Terveystalo ovat mittaushetkellä erilliset yhtiöt. Tuloksia päivitetään tarvittaessa. "
         "Medilaser sulautui Silmäasemaan 2020 eikä ole enää erillinen yhtiö."),
        ("<b>Miksi listalla on vain {n} palveluntarjoajaa?</b> Rajasimme listan niihin, joilla on "
         "useita toimipisteitä ympäri Suomea ja jotka tarjoavat silmäkirurgisia palveluja "
         "verkkosivujensa kautta. Yksittäisissä kaupungeissa toimivat klinikat (OGA Tampere, "
         "Turun Silmalaser, Laser-Porus Oulu, Eiran Sairaala Helsinki) on rajattu ulkopuolelle. "
         "Listalla on sekä erikoistuneita silmasairaalaketjuja etta suuria terveyskonserneja, "
         "joiden silmakirurgiayksikko on kuluttajalle yhtä lailla vaihtoehto."),
        ("Emme anna laakarineuvontaa emmeka suosittele toimenpidetta. Vertailu kuvaa "
         "yritysten julkisten verkkosivujen mitattavia ominaisuuksia. Silmaleikkauksen "
         "sopivuus arvioidaan aina ensin lausunnossa. "
         "Demo voi sisaltaa affiliate-linkkeja; ne eivat vaikuta pisteisiin."),
    ],
}

META["uutismediat"] = {
    "slug": "uutismediat",
    "nimi": "Uutismediat",
    "nav": "Uutismediat",
    "h1": "Suomen paras uutismedia 2026",
    "yksikko": "suomalaista uutismediaa",
    "lead": ("Pisteytimme {n} suomalaista uutismediaa {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: kerrotaanko "
             "lukijalle avoimesti, mitä sisältö maksaa, kuka siitä vastaa ja miten "
             "virheet korjataan?"),
    "meta_title": "Suomen paras uutismedia 2026 | uutismediat pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} suomalaista uutismediaa pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Vertailemme yksittäisiä medioita, emme konserneja.</b> Siksi listalla on "
         "esimerkiksi sekä Helsingin Sanomat että Ilta-Sanomat, vaikka molempia "
         "julkaisee Sanoma Media Finland Oy, ja sekä Iltalehti että Kauppalehti "
         "(Alma Media). Julkaisija ja omistaja kerrotaan jokaisen median sivulla."),
        ("<b>Emme arvioi journalismin laatua tai linjaa.</b> Mittaamme median "
         "verkkosivuston läpinäkyvyyttä lukijan silmin: näkyykö tilaushinta ennen "
         "tietojen antamista, onko vastaava päätoimittaja ja toimituksen yhteystiedot "
         "esillä, kuvataanko virheiden korjauskäytäntö ja erotellaanko kaupallinen "
         "sisältö journalismista. Emme ota kantaa sisältöön."),
        ("<b>Yle on mukana eri rahoitusmallilla.</b> Yle Uutiset on Yle-verolla "
         "rahoitettu julkisen palvelun media ilman tilausmaksua — sen kohdalla "
         "tilaushintakriteeri mittaa, kerrotaanko maksuttomuus ja rahoitusmalli "
         "selkeästi."),
    ],
}

META["aikakauslehdet"] = {
    "slug": "aikakauslehdet",
    "nimi": "Aikakauslehdet",
    "nav": "Aikakauslehdet",
    "h1": "Suomen paras aikakauslehti 2026",
    "yksikko": "suomalaista aikakauslehteä",
    "lead": ("Pisteytimme {n} suomalaista aikakauslehteä {m} mittarilla: tekninen laatu, "
             "läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: kerrotaanko "
             "tilaajalle avoimesti, mitä kestotilaus maksaa ja miten sen saa loppumaan?"),
    "meta_title": "Suomen paras aikakauslehti 2026 | aikakauslehdet pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} suomalaista aikakauslehteä pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Vertailemme yksittäisiä lehtiä, emme kustantajia.</b> Otavamedia julkaisee "
         "neljää listan lehdistä (Seura, Suomen Kuvalehti, Tekniikan Maailma, Kotiliesi), "
         "Sanoma kahta (ET, Tiede) — markkina on keskittynyt, ja siksi kustantaja ja "
         "omistaja kerrotaan jokaisen lehden sivulla."),
        ("<b>Tilauksen päättäminen on alan kipupiste.</b> Kestotilaus jatkuu, kunnes sen "
         "erikseen päättää, ja peruutusohjeiden löydettävyys vaihtelee. Siksi tilauksen "
         "päättämisen avoimuus on tässä kategoriassa oma painava kriteerinsä ja kytkeytyy "
         "myös sitoutumisindeksiin."),
        ("<b>Emme arvioi lehtien sisältöä tai laatua.</b> Mittaamme verkkosivuston "
         "läpinäkyvyyttä tilaajan silmin: hinnat, peruutusehdot, vastuuhenkilöt ja "
         "kaupallisen sisällön erottelu."),
    ],
}

META["huonekaluketjut"] = {
    "slug": "huonekaluketjut",
    "nimi": "Huonekaluketjut",
    "nav": "Huonekaluketjut",
    "h1": "Suomen paras huonekaluketju 2026",
    "yksikko": "Suomessa toimivaa huonekaluketjua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa huonekaluketjua {m} mittarilla: tekninen "
             "laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: näetkö "
             "hinnat, toimituskulut ja palautusehdot ennen kuin annat tietosi?"),
    "meta_title": "Suomen paras huonekaluketju 2026 | huonekaluketjut pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} huonekaluketjua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Miksi Asko ja Sotka eivät ole listalla?</b> Niiden omistaja Indoor Group Oy "
         "meni konkurssiin helmikuussa 2026 ja myymälät suljettiin. Maskun omistaja osti "
         "konkurssipesältä pelkät brändit keväällä 2026, ja sotka.fi ohjaa nykyään Maskun "
         "verkkokauppaan. Emme pisteytä ketjua, jota ei enää ole."),
        ("<b>Huonekaluissa toimitus ratkaisee.</b> Ison tavaran rahti, kantopalvelu ja "
         "vanhan kalusteen poisvienti voivat maksaa kymmeniä euroja, ja niiden hintojen "
         "avoimuus ennen kassaa on tässä kategoriassa painava kriteeri."),
        ("<b>IKEA mitataan ikea.com/fi-sivustolta.</b> IKEAlla ei ole erillistä .fi-domainia, "
         "vaan suomenkielinen kauppa toimii globaalin sivuston alla."),
    ],
}

META["elektroniikkaketjut"] = {
    "slug": "elektroniikkaketjut",
    "nimi": "Elektroniikkaketjut",
    "nav": "Elektroniikkaketjut",
    "h1": "Suomen paras elektroniikkaketju 2026",
    "yksikko": "Suomessa toimivaa elektroniikkaketjua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa kodintekniikan ja elektroniikan ketjua {m} "
             "mittarilla: tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein "
             "kysymys: näetkö kokonaishinnan toimituskuluineen ja palautusehdot ennen ostoa?"),
    "meta_title": "Suomen paras elektroniikkaketju 2026 | elektroniikkaketjut pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} elektroniikkaketjua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Ketjujen taustat vaihtelevat.</b> Gigantti kuuluu brittiläiseen Currys-konserniin, "
         "Power norjalaiseen Power Internationaliin, Jimm's saksalaiseen Casekingiin ja "
         "Proshop palvelee Suomea Tanskasta — Verkkokauppa.com ja Multitronic ovat "
         "suomalaisia. Omistus kerrotaan jokaisen ketjun sivulla."),
        ("<b>Proshopilla ei ole suomalaista Y-tunnusta.</b> Se myy Suomeen tanskalaisena "
         "verkkokauppana, mikä on laillista mutta tarkoittaa, että kuluttajansuoja-asiat "
         "hoidetaan tanskalaisen yhtiön kanssa."),
        ("<b>Emme vertaile tuotehintoja.</b> Mittaamme sivuston läpinäkyvyyttä: näkyvätkö "
         "hinnat, toimituskulut ja palautusehdot ennen sitoutumista — emme sitä, kummalta "
         "telkkarin saa halvemmalla."),
    ],
}

META["urheiluvalineketjut"] = {
    "slug": "urheiluvalineketjut",
    "nimi": "Urheiluvälineketjut",
    "nav": "Urheiluvälineketjut",
    "h1": "Suomen paras urheiluvälineketju 2026",
    "yksikko": "Suomessa toimivaa urheilu- ja ulkoiluvälineketjua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa urheilu- ja ulkoiluvälineketjua {m} "
             "mittarilla: tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. "
             "Tärkein kysymys: näetkö hinnat, toimituskulut ja palautusehdot ennen ostoa?"),
    "meta_title": "Suomen paras urheiluvälineketju 2026 | urheiluvälineketjut pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} urheiluvälineketjua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Intersport ja Budget Sport ovat sama yhtiö.</b> Molempia operoi Keskon "
         "Intersport Finland Oy, mutta konseptit palvelevat eri asiakasryhmiä eri "
         "hinnoilla, joten vertailemme ne erikseen — omistus kerrotaan avoimesti."),
        ("<b>Ala elää murrosta.</b> XXL on karsinut myymäläverkkoaan Suomessa vuonna "
         "2026, ja Sportia-ketju on jätetty vertailusta pois, koska näyttöä elävästä "
         "valtakunnallisesta ketjusta ei mittaushetkellä ollut."),
        ("<b>Mukana on myös verkkopainotteisia toimijoita.</b> Varuste.net ja "
         "Scandinavian Outdoor palvelevat pääosin verkossa, ja niiden myymäläkriteeri "
         "mitataan noutopisteiden ja toimitustietojen avoimuutena."),
    ],
}

META["ikkunaremontit"] = {
    "slug": "ikkunaremontit",
    "nimi": "Ikkunaremontit",
    "nav": "Ikkunaremontit",
    "h1": "Suomen paras ikkunaremontti 2026",
    "yksikko": "Suomessa toimivaa ikkunaremonttiyritystä",
    "lead": ("Pisteytimme {n} Suomessa toimivaa ikkunaremonttiyritystä {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "saatko hintatiedon ja takuuehdot ennen kuin annat yhteystietosi?"),
    "meta_title": "Suomen paras ikkunaremontti 2026 | ikkunaremontit pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} ikkunaremonttiyritystä pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Pihla ja Tiivi ovat saman konsernin brändejä.</b> Molemmat kuuluvat "
         "ruotsalaiselle Inwido AB:lle (Pihla Group Oy), mutta toimivat eri brändeinä "
         "eri hinnoilla — vertailemme ne erikseen ja kerromme omistuksen avoimesti."),
        ("<b>Ala on käynyt läpi konkurssiaallon.</b> Fenestra kaatui jo 2016 ja Domus "
         "2019 — vertailussa ovat vain yritykset, joiden toiminta on varmistettu "
         "mittaushetkellä heinäkuussa 2026."),
        ("<b>Kotitalousvähennys koskee asennustyötä.</b> Ikkunaremontin työn osuudesta "
         "voi saada kotitalousvähennyksen, ja hyvät toimijat erittelevät työn ja "
         "materiaalin osuuden tarjouksessa."),
    ],
}

META["lampopumppuasentajat"] = {
    "slug": "lampopumppuasentajat",
    "nimi": "Lämpöpumppuasentajat",
    "nav": "Lämpöpumppuasentajat",
    "h1": "Suomen paras lämpöpumppuasentaja 2026",
    "yksikko": "Suomessa toimivaa lämpöpumppuasentajaa",
    "lead": ("Pisteytimme {n} Suomessa toimivaa lämpöpumppuasentajaa {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "kerrotaanko hinnat ja takuut ennen kuin joudut jättämään yhteystietosi?"),
    "meta_title": "Suomen paras lämpöpumppuasentaja 2026 | lämpöpumppuasentajat pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} lämpöpumppuasentajaa pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Kolme pumpputyyppiä, eri hintaluokat.</b> Ilmalämpöpumppu maksaa satoja "
         "tai tuhansia, ilma-vesilämpöpumppu ja maalämpö kymmeniä tuhansia euroja. "
         "Kaikki listan yritykset eivät asenna kaikkia tyyppejä — esimerkiksi Renoa "
         "keskittyy ilma-vesilämpöpumppuihin."),
        ("<b>Omistuspohjat vaihtelevat.</b> Markkinajohtaja Tom Allen Senera kuuluu "
         "pohjoismaiseen Assemblin Caverion Groupiin ja LämpöYkkösestä 30 % omistaa "
         "laitevalmistaja Viessmann — laitemerkkisidonnaisuus kannattaa tiedostaa "
         "tarjouksia vertaillessa."),
        ("<b>Mittaamme sivuston läpinäkyvyyttä, emme asennuslaatua.</b> Pisteet "
         "kertovat, miten avoimesti yritys kertoo hinnoista, prosessista ja takuista "
         "verkossa — eivät sitä, kenen poraus onnistuu parhaiten."),
    ],
}

META["aurinkopaneeliasentajat"] = {
    "slug": "aurinkopaneeliasentajat",
    "nimi": "Aurinkopaneeliasentajat",
    "nav": "Aurinkopaneeliasentajat",
    "h1": "Suomen paras aurinkopaneeliasentaja 2026",
    "yksikko": "Suomessa toimivaa aurinkopaneeliasentajaa",
    "lead": ("Pisteytimme {n} Suomessa toimivaa aurinkopaneeliasentajaa {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "kerrotaanko järjestelmän hinta ja takuut ennen kuin annat yhteystietosi?"),
    "meta_title": "Suomen paras aurinkopaneeliasentaja 2026 | pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} aurinkopaneeliasentajaa pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Ala on myllerryksessä.</b> Moni tunnettu nimi on poistunut kuluttajamarkkinalta: "
         "Fortum ja Vattenfall lopettivat kuluttaja-aurinkopalvelunsa, Naps ajautui "
         "järjestelyihin ja Otovo vetäytyi Suomesta. Vertailussa ovat vain toimijat, joiden "
         "aktiivinen asennusmyynti varmistettiin heinäkuussa 2026."),
        ("<b>Helen ei ole listalla erikseen</b>, koska sen kuluttaja-aurinkomyynnin hoitaa "
         "kumppanina toimiva Aurinkotekniikka, joka on vertailussa mukana."),
        ("<b>Ovimyyntiin liittyy alalla riskejä.</b> Kuluttaja-asiamies on puuttunut yhden "
         "listatun yhtiön aggressiiviseen ovimyyntiin vuonna 2025 — kerromme tämän avoimesti "
         "yhtiön sivulla. Vertaa aina kirjalliset tarjoukset rauhassa."),
    ],
}

META["kukkakauppojen-verkkokaupat"] = {
    "slug": "kukkakauppojen-verkkokaupat",
    "nimi": "Kukkakauppojen verkkokaupat",
    "nav": "Kukkien verkkokaupat",
    "h1": "Suomen paras kukkien verkkokauppa 2026",
    "yksikko": "Suomeen toimittavaa kukkien verkkokauppaa",
    "lead": ("Pisteytimme {n} Suomeen toimittavaa kukkien verkkokauppaa {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "näetkö kimpun hinnan toimitusmaksuineen ja korvauskäytännön ennen tilausta?"),
    "meta_title": "Suomen paras kukkien verkkokauppa 2026 | pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} kukkien verkkokauppaa pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Ala on täynnä välittäjiä ja affiliate-sivustoja.</b> Moni 'kukkakauppa' on "
         "pelkkä välityssivu, joka ohjaa tilauksen toiselle toimijalle provisiota vastaan. "
         "Vertailussa ovat vain palvelut, joiden operoija on tunnistettavissa — yksi "
         "kandidaatti hylättiin, koska sen taustayhtiötä ei voitu todentaa."),
        ("<b>Toimitus ratkaisee kukkakaupassa.</b> Saman päivän toimitus, toimitusalue ja "
         "toimitusmaksu vaihtelevat rajusti — ja pilalle mennyt kimppu vaatii selkeän "
         "korvauskäytännön. Nämä ovat vertailun painavimmat kriteerit."),
        ("<b>Verkostomallit eroavat.</b> Interflora ja DataFlora välittävät tilaukset "
         "paikallisille kukkakaupoille, osa taas lähettää kimput keskusvarastolta. "
         "Kumpikin toimii — kerromme mallin jokaisen palvelun sivulla."),
    ],
}

def _meta2(slug, nimi, nav, h1, yksikko, kysymys, notes):
    META[slug] = {
        "slug": slug, "nimi": nimi, "nav": nav, "h1": h1, "yksikko": yksikko,
        "lead": ("Pisteytimme {n} " + yksikko + " {m} mittarilla: tekninen laatu, "
                 "läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: " + kysymys),
        "meta_title": h1 + " | pisteytettynä | Suomen Paras",
        "meta_desc": "{n} " + yksikko + " pisteytetty läpinäkyvällä kaavalla. Katso mistä jokainen piste tulee.",
        "notes": notes,
    }

_meta2("lastenvaatteiden-verkkokaupat", "Lastenvaatteiden verkkokaupat", "Lastenvaatteet",
    "Suomen paras lastenvaatteiden verkkokauppa 2026", "lastenvaatteiden verkkokauppaa",
    "näetkö hinnat, toimituskulut ja palautusehdot ennen tilausta?",
    [("<b>Polarn O. Pyret puuttuu</b>, koska sen verkkokauppa ei ole automaattisesti mitattavissa: sivusto on JavaScript-sovellus Cloudflaren takana eivatka alasivujen osoitteet nay lahdekoodissa. Emme arvaa pisteita mittaamattomasta sivustosta."),
     ("<b>Ala on käynyt läpi rajun karsinnan.</b> Papu Design ajautui konkurssiin lokakuussa "
      "2025, Vimma lopetti lastenvaatteet ja Mainio ajaa lastenlinjaansa alas — vertailussa "
      "ovat vain heinäkuussa 2026 aktiivisiksi varmistetut kaupat."),
     ("<b>Mukana on eri kokoluokkia.</b> Reima on kansainvälinen suuryritys ja osa kaupoista "
      "pieniä kotimaisia perheyrityksiä — pisteet mittaavat verkkokaupan läpinäkyvyyttä, "
      "eivät yrityksen kokoa tai vaatteiden laatua.")])

_meta2("lemmikkitarvikkeiden-verkkokaupat", "Lemmikkitarvikkeiden verkkokaupat", "Lemmikkitarvikkeet",
    "Suomen paras lemmikkitarvikkeiden verkkokauppa 2026", "lemmikkitarvikkeiden verkkokauppaa",
    "näetkö hinnat, toimituskulut ja palautusehdot ennen tilausta?",
    [("<b>Markkinajohtaja vaihtoi omistajaa.</b> Musti Group ostettiin pois pörssistä 2024 — "
      "omistus kerrotaan avoimesti yhtiön sivulla, kuten myös Zooplusin pääomasijoittajatausta."),
     ("<b>Affiliate-aggregaattorit on karsittu.</b> Osa 'lemmikkikaupoista' on pelkkiä "
      "ohjaussivustoja ilman omaa kauppaa — vertailussa ovat vain oikeat verkkokaupat.")])

_meta2("hotelliketjut", "Hotelliketjut", "Hotelliketjut",
    "Suomen paras hotelliketju 2026", "Suomessa toimivaa hotelliketjua",
    "näetkö huonehinnan ja peruutusehdot ennen varausta ja kirjautumista?",
    [("<b>Radisson ja Best Western puuttuvat</b>, koska niiden sivustot estävät automaattisen "
      "mittauksen kokonaan (HTTP 403) — emme arvaa pisteitä, joten mittauskelvottomat jäävät "
      "pois. Finlandia Hotels jäi pois itsenäisten hotellien markkinointiketjuna."),
     ("<b>Peruutusehdot ovat hotellivarauksen tärkein pieni teksti.</b> Joustava ja "
      "ei-palautettava hinta voivat erota kymmeniä euroja — mittaamme, kerrotaanko ehdot "
      "selkeästi ennen varausta, ja avoimuus tuo myös sitoutumisindeksibonuksen.")])

_meta2("taksipalvelut", "Taksipalvelut", "Taksipalvelut",
    "Suomen paras taksipalvelu 2026", "Suomessa toimivaa taksipalvelua",
    "kerrotaanko hinnat tai hintaesimerkit ennen kyytiä?",
    [("<b>Mukana ovat myös Uber ja Bolt</b> ulkomaisina sovelluspalveluina — omistus ja "
      "toiminta-alueet kerrotaan jokaisen palvelun sivulla. Kajonin sisaryhtiön vuoden 2020 "
      "konkurssi on kerrottu avoimesti riskitietona."),
     ("<b>Taksiuudistuksen jälkeen hinnat vaihtelevat rajusti.</b> Sama matka voi maksaa "
      "tuplasti eri yhtiöllä — siksi hintojen ja lisämaksujen avoimuus ennen tilausta on "
      "vertailun painavin kriteeri.")])

_meta2("kirjakauppojen-verkkokaupat", "Kirjakauppojen verkkokaupat", "Kirjakaupat",
    "Suomen paras kirjakauppojen verkkokauppa 2026", "Suomeen myyvää kirjojen verkkokauppaa",
    "näetkö hinnat, toimituskulut ja palautusehdot ennen tilausta?",
    [("<b>Ala keskittyi vuodenvaihteessa:</b> Adlibris (Bonnier) osti Akateemisen "
      "Kirjakaupan 1.1.2026 — molemmat verkkokaupat jatkavat erikseen ja molemmat ovat "
      "vertailussa, omistus avoimesti kerrottuna. Suomalainen Kirjakauppa kuuluu Otavalle."),
     ("<b>Äänikirjapalvelut eivät ole tässä vertailussa.</b> BookBeat, Storytel ja Nextory "
      "ovat tilauspalveluita, eivät kirjakauppoja — ne ansaitsevat oman kategoriansa.")])

META["autoliikkeet"] = {
    "slug": "autoliikkeet",
    "nimi": "Autoliikkeet",
    "nav": "Autoliikkeet",
    "h1": "Suomen paras autoliike 2026",
    "yksikko": "Suomessa toimivaa autoliikeketjua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa autoliikeketjua {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "näetkö auton hinnan, takuun sisällön ja rahoituksen kulut ennen kuin "
             "jätät yhteystietosi?"),
    "meta_title": "Suomen paras autoliike 2026 | pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} autoliikeketjua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Vaihtoautokauppa on keskittynyt.</b> Laakkosen autotalot ovat nykyään "
         "ruotsalaisen Hedin Mobility Groupin omistuksessa (Hedin Automotive Finland Oy, "
         "aiemmin Veljekset Laakkonen Oy), ja samalle omistajalle kuuluu Suomessa myös "
         "Delta Auto. Kerromme omistajan jokaisen yhtiön sivulla, koska kahden ketjun "
         "vertailu ei ole vertailua, jos omistaja on sama."),
        ("<b>Mitä tämä vertailu ei mittaa.</b> Emme arvioi autojen kuntoa, hintatasoa "
         "emmekä kauppojen palvelua. Mittaamme sen, mitä ostaja näkee julkisilta sivuilta "
         "ennen yhteydenottoa: hinnat, vaihtoautotakuun sisällön, rahoituksen kulut ja "
         "palautus- tai vaihto-oikeuden."),
        ("<b>Rahoituksen kulut ovat alan vaikein kohta.</b> Kuukausierä näkyy usein "
         "isolla, mutta todellinen vuosikorko ja kokonaiskulut vasta pienellä tai "
         "erillisessä liitteessä. Pisteytämme sen, löytyykö todellinen vuosikorko "
         "julkiselta sivulta ilman lomakkeen täyttöä."),
    ],
}

META["pakettipalvelut"] = {
    "slug": "pakettipalvelut",
    "nimi": "Pakettipalvelut",
    "nav": "Pakettipalvelut",
    "h1": "Suomen paras pakettipalvelu 2026",
    "yksikko": "pakettipalveluntarjoajaa",
    "lead": ("Pisteytimme {n} Suomessa toimivaa pakettipalvelua {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "saatko hinnan tietää ennen kuin rekisteröit pakettisi?"),
    "meta_title": "Suomen paras pakettipalvelu 2026 — Posti, DHL, Matkahuolto, PostNord, GLS, DSV pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} suomalaista pakettipalvelua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>DB Schenker on nyt DSV.</b> Deutsche Bahn myi koko DB Schenker -liiketoiminnan "
         "tanskalaiselle DSV A/S:lle 30.4.2025 (14,3 miljardia euroa). Suomessa Schenker Oy "
         "jatkaa toimintaansa DSV:n tytäryhtiönä ja dbschenker.com ohjaa nyt dsv.com/fi-fi/ "
         "-sivulle. Mittauksessa on siis DSV, ei DB Schenker."),
        ("<b>Vertailemme kuluttajapalvelua.</b> Kaikki kuusi yhtiötä tarjoavat pakettien "
         "lähetyspalvelun myös yksityishenkilöille, mutta B2B-paino vaihtelee merkittävästi: "
         "Posti ja Matkahuolto ovat selvästi kuluttajapainotteisia, DHL ja GLS kuluttaja- ja "
         "yrityspalvelua rinnakkain, DSV painottuu vahvasti yritysasiakkaisiin. "
         "Tämä näkyy hintaviestinnän selkeydessä ja noutopisteinformaatiossa."),
        ("<b>Noutopisteet, ei kotiinkuljetus.</b> Suurin osa suomalaisesta pakettikuljetuksesta "
         "kulkee noutopisteverkoston kautta. Mittaamme onko noutopisteiden määrä tai kartta "
         "julkisella sivulla, koska se on kuluttajalle yksi tärkeimmistä valintatekijöistä."),
        ("Emme vertaile lähetysnopeutta tai paketin perille saapumista käytännössä. "
         "Mittaamme sivuston julkista tietoa: hinnasto, aikataulut, noutopisteet ja "
         "reklamaatiomenettely."),
    ],
}

META["kauneustuotteet-verkkokaupat"] = {
    "slug": "kauneustuotteet-verkkokaupat",
    "nimi": "Kauneustuotteet-verkkokaupat",
    "nav": "Kauneustuotteet",
    "h1": "Suomen paras kauneustuotteiden verkkokauppa 2026",
    "yksikko": "kosmetiikan ja kauneustuotteiden verkkokauppaa",
    "lead": ("Pisteytimme {n} Suomessa toimivaa kosmetiikan ja kauneustuotteiden verkkokauppaa "
             "{m} mittarilla: tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. "
             "Tärkein kysymys: naatko hinnat, toimituskulut ja ainesosaluettelot ilman "
             "kirjautumista?"),
    "meta_title": "Suomen paras kauneustuotteiden verkkokauppa 2026 — Lyko, Bangerhead, Cocopanda, KICKS, Parfym.fi, NordicFeel pisteytettyna | Suomen Paras",
    "meta_desc": ("{n} kosmetiikan verkkokauppaa pisteytetty lapinakyvallakaavalla. "
                  "Katso mista jokainen piste tulee."),
    "notes": [
        ("<b>Kolme yhtiota ei suomalaista Y-tunnusta.</b> Lyko (ruotsalainen Lyko Group AB), "
         "Parfym.fi (ruotsalainen Parfym Sverige AB) ja NordicFeel (ruotsalainen NordicFeel AB) "
         "operoivat Suomessa ulkomaisena yhtiönä ilman suomalaista tytaryhtiota. Omanikki "
         "kerrotaan jokaisen yhtion kohdalla."),
        ("<b>Parfym.fi ja Hajuvesi.fi ovat sama kauppa.</b> Molemmat domainit kuuluvat "
         "ruotsalaiselle Parfym Sverige AB:lle ja toimittavat samoista varastoista. "
         "Mittauksessa on vain parfym.fi, jolla on laajempi valikoima."),
        ("<b>Emme vertaile tuotevalikoimaa tai hintatasoa.</b> Kaikki kuusi kauppaa myyvat "
         "useita tuhansia tuotteita. Mittaamme sen, mita kauppa kertoo julkisesti: hinnat, "
         "toimituskulut, palautusehdot ja ainesosaluettelot ennen kuin asiakas kirjautuu tai "
         "lisaa tuotteen koriin."),
        ("<b>Ainesosaluettelot ovat kosmetiikka-asetuksen vaatimus.</b> EU-kosmetiikka-asetus "
         "edellyttaa INCI-luettelon tuotteen pakkauksessa, mutta ei verkkokaupan sivulla. "
         "Pisteytamme sen, tarjoaako kauppa ainesosatiedot tuotekohtaisesti myos verkossa, "
         "mika on erityisen tarkeaa allergisoituville asiakkaille."),
    ],
}

META["musiikkipalvelut"] = {
    "slug": "musiikkipalvelut",
    "nimi": "Musiikkipalvelut",
    "nav": "Musiikki",
    "h1": "Suomen paras musiikkipalvelu 2026",
    "yksikko": "Suomessa myytavaa musiikkipalvelua",
    "lead": ("Pisteytimme {n} Suomessa myytavaa musiikkipalvelua {m} mittarilla. "
             "Tairkein kysymys: kerrotaanko kuukausihinta, tilaustasojen erot ja "
             "irtisanominen selkeasti ennen tilaamista?"),
    "meta_title": "Suomen paras musiikkipalvelu 2026 | palvelut pisteytettyina | Suomen Paras",
    "meta_desc": "{n} musiikkipalvelua pisteytetty lapinakyvalla kaavalla. Katso mista jokainen piste tulee.",
    "notes": [
        ("<b>Kaikki kuusi palvelua ovat kansainvalisia yhtiota.</b> Spotify on ruotsalainen, "
         "Deezer ja Qobuz ranskalaisia, loput yhdysvaltalaisten teknologiajattien palveluita. "
         "Yksikaan ei ole suomalainen. Naytamme omistajan jokaisen kohdalla."),
        ("<b>Qobuz on listan ainoa hi-res-erikoispalvelu.</b> Se on ainoa joka markkinoi "
         "lossless- ja hi-res-aania ensisijaisena ominaisuutenaan. Muut palvelut tarjoavat "
         "korkealaatuista aanta lisatason ominaisuutena tai ei lainkaan."),
        ("<b>Emme arvioi musiikin maaraa tai soittolistoja.</b> Vertailu mittaa julkisten "
         "verkkosivujen mitattavia ominaisuuksia: hinnat, tilaustasojen erot, irtisanominen "
         "ja omistajan lapinakyyvys ennen tilaamista."),
    ],
}

META["pelitilauspalvelut"] = {
    "slug": "pelitilauspalvelut",
    "nimi": "Pelitilauspalvelut",
    "nav": "Pelipalvelut",
    "h1": "Suomen paras pelitilauspalvelu 2026",
    "yksikko": "Suomessa myytavaa pelitilauspalvelua",
    "lead": ("Pisteytimme {n} Suomessa myytavaa pelitilauspalvelua {m} mittarilla. "
             "Tairkein kysymys: nakyvatko kuukausihinnat per taso, pelikirjaston kuvaus "
             "ja irtisanomisoikeus selkeasti ennen tilauksen tekemista?"),
    "meta_title": "Suomen paras pelitilauspalvelu 2026 | Xbox, PlayStation, Nintendo | Suomen Paras",
    "meta_desc": ("{n} pelitilauspalvelua pisteytetty lapinakyvalla kaavalla. "
                  "Katso mista jokainen piste tulee: Xbox Game Pass, PlayStation Plus, Nintendo Switch Online ja muut."),
    "notes": [
        ("<b>Kaikki kuusi palvelua ovat kansainvalisten yritysten tuotteita.</b> "
         "Microsoft, Sony ja Nintendo ovat suuria julkisesti listattuja yrityksita. "
         "EA ja Ubisoft ovat eurooppalaisen peliteollisuuden jatteja. "
         "Apple on maailman arvokkain teknologiayritys. Yksikaan ei ole suomalainen."),
        ("<b>Nintendo Switch Online on ainoa palvelu, jolla on suomenkielinen verkkotunnus (nintendo.fi).</b> "
         "Muut toimijat palvelevat Suomea kansainvalisten tai skandinaavisten sivustojensa kautta. "
         "Suomenkielinen palvelu pisteyttaa 'kylla' suomenkielinen_palvelu-mittarilla, "
         "pelkka euro-hinnoittelu pisteyttaa 'osittain'."),
        ("<b>Emme arvioi pelikirjaston kokoa, teknista suorituskykyia tai laitteistoa.</b> "
         "Vertailu mittaa julkisten verkkosivujen lapinakyvyytta: kerrotaanko hinnat, "
         "tasojen erot, kirjaston sisalto ja irtisanominen ennen tilaamista?"),
    ],
}

META["pikaruokaketjut"] = {
    "slug": "pikaruokaketjut",
    "nimi": "Pikaruokaketjut",
    "nav": "Pikaruokaketjut",
    "h1": "Suomen paras pikaruokaketju 2026",
    "yksikko": "Suomessa toimivaa pikaruokaketjua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa pikaruokaketjua {m} mittarilla: "
             "tekninen laatu, läpinäkyvyys, tavoitettavuus ja AI-laatu. Tärkein kysymys: "
             "näetkö hinnat, allergeenit ja raaka-aineiden alkuperän ennen kuin "
             "menet ravintolaan?"),
    "meta_title": "Suomen paras pikaruokaketju 2026 | pisteytettynä | Suomen Paras",
    "meta_desc": ("{n} pikaruokaketjua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee."),
    "notes": [
        ("<b>Kolme ketjua, yksi operaattori.</b> Burger King, Taco Bell ja Golden Rax "
         "kuuluvat kaikki Osuuskunta Tradekan omistamaan Restel-konserniin. Ketjut ovat "
         "vertailussa erikseen, koska niillä on omat sivustot ja oma hinnoittelu, mutta "
         "omistaja kerrotaan jokaisen kohdalla."),
        ("<b>Emme arvioi ruokaa.</b> Maku, laatu ja ravintoloiden siisteys eivät ole "
         "mitattavissa verkkosivulta. Mittaamme sen, mitä ketju kertoo julkisesti: "
         "hinnat, allergeeni- ja ravintosisältötiedot, raaka-aineiden alkuperän sekä "
         "ravintoloiden aukioloajat."),
        ("<b>Allergeenitiedot ovat lain vaatimus, mutta esitystapa ei.</b> Tieto voi olla "
         "selattavassa taulukossa, latautuvassa PDF:ssä tai vain ravintolassa kysyttäessä. "
         "Pisteytämme sen, löytyykö tieto julkiselta sivulta tuotekohtaisesti."),
    ],
}

META["aanikirjapalvelut"] = {
    "slug": "aanikirjapalvelut",
    "nimi": "Äänikirjapalvelut",
    "nav": "Äänikirjat",
    "h1": "Suomen paras äänikirjapalvelu 2026",
    "yksikko": "Suomessa toimivaa äänikirjapalvelua",
    "lead": ("Pisteytimme {n} Suomessa toimivaa äänikirjapalvelua {m} mittarilla. "
             "Tärkein kysymys: kerrotaanko kuukausihinta, kirjaston koko ja "
             "irtisanominen selkeästi ennen tilauksen tekemistä?"),
    "meta_title": "Suomen paras äänikirjapalvelu 2026 | Storytel, BookBeat, Nextory | Suomen Paras",
    "meta_desc": ("{n} äänikirjapalvelua pisteytetty läpinäkyvällä kaavalla. "
                  "Katso mistä jokainen piste tulee: Storytel, BookBeat, Nextory, Kobo, Podimo ja Spotify."),
    "notes": [
        ("<b>Kaikki kuusi palvelua ovat pohjoismaisia tai kansainvälisiä yhtiöitä.</b> "
         "Storytel, BookBeat ja Nextory ovat ruotsalaisia, Podimo tanskalainen, Kobo "
         "kanadalainen ja Spotify ruotsalainen. Yksikään ei ole suomalainen. "
         "Näytämme omistajan jokaisen palvelun kohdalla."),
        ("<b>Spotify on ensisijaisesti musiikkipalvelu.</b> Sen Premium-tilaus sisältää "
         "15 tuntia kuukaudessa äänikirjakuuntelua, minkä jälkeen kirjoja voi ostaa "
         "erikseen. Muut viisi palvelua ovat rakennettu ensisijaisesti äänikirjoja varten. "
         "Vertailu mittaa jokaisen palvelun äänikirjaominaisuuksia, ei musiikkia."),
        ("<b>Emme arvioi kirjaston kokoa tai äänenlaatua.</b> Mittaamme julkisten "
         "verkkosivujen läpinäkyvyyttä: näkyykö kuukausihinta, kirjaston kuvaus, "
         "tilaustasojen erot, irtisanomisen ehdot ja kuunteluajan rajoitukset ennen "
         "tilaamista?"),
    ],
}
