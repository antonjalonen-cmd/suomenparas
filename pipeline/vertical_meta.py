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
}
