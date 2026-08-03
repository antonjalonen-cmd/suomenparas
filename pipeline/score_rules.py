# -*- coding: utf-8 -*-
"""Suomen Paras Score v1.1 — pillar weights and per-vertical transparency criteria.

v1.0 -> v1.1: the Läpinäkyvyys pillar became vertical-specific. Three pillars
(digitaalinen, tavoitettavuus, ai_laatu) are measured identically in every
category. Only Läpinäkyvyys changes, because "did they publish the price before
asking for your data" looks different for a loan broker, an insurer, an
electricity retailer and an ISP — but it is the same question.

Each criterion: (key, label, weight, source). Weights must total 100 per vertical.
Extraction values are "kylla" | "osittain" | "ei" -> full / half / zero points,
or a number for the 0-100 AI metrics.
"""

PILLAR_W = {"digitaalinen": 30, "lapinakyvyys": 30, "tavoitettavuus": 20, "ai_laatu": 20}

# Lighthouse sub-weights (identical in every vertical)
DIGITAL = [
    ("performance", "Suorituskyky (mobiili)", 40),
    ("accessibility", "Saavutettavuus", 30),
    ("seo", "Löydettävyys (SEO)", 15),
    ("best_practices", "Tekniset käytännöt", 15),
]

# Reachability (identical in every vertical)
REACH = [
    ("puhelin_esilla", "Puhelinnumero esillä", 30),
    ("email_esilla", "Sähköposti esillä", 15),
    ("chat_mainittu", "Chat-tuki", 15),
    ("aukioloajat_esilla", "Aukioloajat esillä", 15),
    ("ukk_osio", "UKK-osio", 15),
    ("mobiilisovellus", "Mobiilisovellus", 10),
]

# AI quality (identical in every vertical)
AI = [
    ("selkeys", "Tietojen selkeys", 34),
    ("hintojen_loydettavyys", "Hintatietojen löydettävyys", 33),
    ("sisallon_kattavuus", "Sisällön kattavuus", 33),
]

# ---------------------------------------------------------------- transparency
# The 30-point "price before your data" criterion is deliberately the heaviest in
# every vertical — it is the site's core question, expressed in each domain's terms.
TRANSPARENCY = {
    "rautakaupat": [
        ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
        ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
        ("palautusehdot_saatavilla", "Palautus- ja takuuehdot julkisesti saatavilla", 20),
        ("myymalat_ja_aukioloajat", "Myymälät ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "kattoremontit": [
        ("hinta_indikaatio", "Hintatietoa tai hintalaskuri julkisesti esillä", 25),
        ("prosessi_kuvattu", "Remontin eteneminen kuvattu vaiheittain", 20),
        ("takuut_kerrottu", "Takuut ja niiden ehdot kerrottu", 20),
        ("materiaalit_kuvattu", "Kattomateriaalit ja vaihtoehdot kuvattu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "tyonvalityspalvelut": [
        ("tyopaikat_esilla", "Avoimet työpaikat selattavissa ilman kirjautumista", 25),
        ("hakuprosessi_kuvattu", "Hakuprosessi ja sen vaiheet kuvattu", 20),
        ("palkkatieto_ilmoituksissa", "Palkka tai palkkahaarukka kerrottu ilmoituksissa", 20),
        ("tyosuhteen_ehdot", "Työsuhteen muodot ja ehdot selitetty", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],

    "fysioterapia": [
        ("hinnat_esilla", "Fysioterapiakäyntien hinnat julkisesti esillä", 30),
        ("varaus_verkossa", "Ajanvaraus toimii verkossa ilman puhelua", 20),
        ("palvelut_kuvattu", "Palvelut ja erikoisalat kuvattu", 15),
        ("terapeutit_esitelty", "Terapeutit ja pätevyydet esitelty", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "autopesulat": [
        ("hinnat_esilla", "Pesujen hinnat julkisesti esillä", 30),
        ("pesuohjelmat_kuvattu", "Pesuohjelmien sisältö kuvattu", 20),
        ("toimipisteet_ja_aukioloajat", "Pesupaikat ja aukioloajat kerrottu", 20),
        ("osto_verkossa", "Pesun voi ostaa tai varata verkossa", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],

    "hautaustoimistot": [
        ("hinnat_esilla", "Hautauspalvelujen hinnat julkisesti esillä", 30),
        ("paketit_kuvattu", "Palvelupakettien sisältö kuvattu", 20),
        ("prosessi_kuvattu", "Hautausjärjestelyjen eteneminen kuvattu", 15),
        ("toimialue_kerrottu", "Toimialue ja toimipisteet kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "matkatoimistot": [
        ("hinnat_esilla", "Matkojen hinnat julkisesti esillä", 25),
        ("varaus_verkossa", "Matkan voi varata verkossa ilman yhteydenottoa", 20),
        ("ehdot_saatavilla", "Matkapaketti- ja peruutusehdot julkisesti saatavilla", 20),
        ("vakuus_kerrottu", "Matkanjärjestäjän vakuus tai rekisteröinti kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "tilitoimistot": [
        ("hinnat_esilla", "Hinnoittelu (kuukausipaketit tai tuntihinnat) julkisesti esillä", 30),
        ("palvelut_kuvattu", "Palvelujen sisältö kuvattu", 20),
        ("ohjelmistot_kerrottu", "Käytetyt ohjelmistot ja integraatiot kerrottu", 15),
        ("auktorisointi_kerrottu", "Auktorisointi tai KLT-pätevyydet kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "tavaransailytys": [
        # Core question: can you see the price for a storage unit without handing over your data?
        ("hinta_esilla_ilman_yhteystietoja", "Varastotilan hinta julkisesti esillä ilman yhteystietoja", 30),
        ("varaus_verkossa", "Varauksen tai sopimuksen voi tehdä verkossa", 20),
        ("sopimusehdot_kerrottu", "Sopimusehdot (irtisanominen, sitoutumisaika) kerrottu", 15),
        ("vakuutus_ja_vastuu_kerrottu", "Vakuutusturva tai vastuu tavaroiden osalta kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "tapahtumaliput": [
        # Core question: can you see the TOTAL price including all service/booking fees
        # BEFORE you have to commit to a purchase or create an account?
        ("palvelumaksut_esilla", "Palvelumaksut (lisät) esillä ennen maksuprosessia", 30),
        ("kokonaishinta_ilman_ostoa", "Kokonaishinnan (lippu + maksut) saa tietää ilman ostoprosessia", 20),
        ("peruutusehdot_esilla", "Peruutus- ja vaihtoehtokäytäntö julkisesti esillä", 20),
        ("ostaa_ilman_rekisteroitymista", "Liput voi tilata ilman rekisteröitymistä", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä (tai omistava yhtiö selkeästi kerrottu)", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],

    "apteekkien-verkkokaupat": [
        # Core question: can you see OTC product prices and delivery costs BEFORE
        # handing over your details or creating an account?
        ("otc_hinnat_esilla", "OTC-tuotteiden hinnat esillä ilman kirjautumista", 30),
        ("toimitusehdot_esilla", "Toimitusehdot ja -kulut esillä ennen kassaa", 20),
        ("resepti_prosessi_selitetty", "Reseptilääkkeiden tilausohje kuvattu", 20),
        ("palautuspolitiikka_kerrottu", "Palautusoikeus ja -ehdot kerrottu", 10),
        ("y_tunnus_esilla", "Y-tunnus tai apteekkiluvan haltija esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "vakuutukset": [
        ("hintalaskuri_ilman_yhteystietoja", "Hinta-arvio ilman yhteystietoja", 30),
        ("vakuutusehdot_saatavilla", "Vakuutusehdot/tuoteseloste julkisesti saatavilla", 20),
        ("omavastuu_selkeasti", "Omavastuu kerrottu selkeästi", 15),
        ("korvausprosessi_kuvattu", "Korvausprosessi ja -ajat kuvattu", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 15),
    ],
    "sahkosopimukset": [
        ("hinta_esilla_ilman_yhteystietoja", "Hinta (c/kWh) esillä ilman yhteystietoja", 30),
        ("perusmaksu_esilla", "Perusmaksu (€/kk) esillä", 15),
        ("sopimusehdot_selkeasti", "Sopimusaika ja irtisanomisehdot selkeästi", 15),
        ("alkupera_kerrottu", "Sähkön alkuperä kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 15),
    ],
    "laajakaista": [
        ("kk_hinta_esilla_ilman_yhteystietoja", "Kuukausihinta esillä ilman yhteystietoja", 30),
        ("kampanjan_jalkeinen_hinta", "Kampanjan jälkeinen normaalihinta kerrottu", 20),
        ("sopimusaika_ja_avausmaksu", "Sopimusaika ja avausmaksu kerrottu", 15),
        ("saatavuustarkistus_ilman_yhteystietoja", "Saatavuuden voi tarkistaa ilman yhteystietoja", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "puhelinliittymat": [
        ("kk_hinta_esilla_ilman_yhteystietoja", "Kuukausihinta esillä ilman yhteystietoja", 30),
        ("kampanjan_jalkeinen_hinta", "Kampanjan jälkeinen normaalihinta kerrottu", 20),
        ("sopimusaika_ja_irtisanomisaika", "Sopimusaika ja irtisanomisaika kerrottu", 15),
        ("nopeus_ja_datarajat", "Nopeus ja datarajat kerrottu selkeästi", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "luottokortit": [
        # Consumer-credit cost disclosure is legally required (KSL 7:8) — so this
        # measures whether they meet their own obligation in public, before you apply.
        ("korko_ja_vuosikorko_esilla", "Korko ja todellinen vuosikorko esillä", 30),
        ("vuosimaksu_esilla", "Vuosimaksu esillä", 20),
        ("muut_kulut_esilla", "Muut kulut (nosto, valuutanvaihto) esillä", 15),
        ("luotonmyontaja_kerrottu", "Luoton todellinen myöntäjä kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "sijoitusalustat": [
        ("kaupankayntikulut_ilman_kirjautumista", "Kaupankäyntikulut esillä ilman kirjautumista", 30),
        ("sailytyspalkkio_kerrottu", "Säilytyspalkkio kerrottu", 15),
        ("valuutanvaihtokulu_kerrottu", "Valuutanvaihtokulu kerrottu", 15),
        ("hinnasto_ladattavissa", "Täysi hinnasto julkisesti saatavilla", 15),
        ("y_tunnus_esilla", "Y-tunnus tai valvoja kerrottu", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 15),
    ],
    "webhotellit": [
        ("hinta_esilla_ilman_yhteystietoja", "Hinta esillä ilman yhteystietoja", 30),
        # The hosting dark pattern: cheap first term, silently expensive renewal.
        ("uusimishinta_kerrottu", "Uusimishinta kerrottu (ei vain tarjoushinta)", 20),
        ("resurssirajat_selkeasti", "Levytila- ja liikennerajat kerrottu selkeästi", 15),
        ("sopimusehdot_ja_irtisanominen", "Sopimusehdot ja irtisanominen kerrottu", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 15),
    ],
    "vpn-palvelut": [
        ("hinta_esilla_ilman_yhteystietoja", "Hinta esillä ilman yhteystietoja", 30),
        ("uusimishinta_kerrottu", "Uusimishinta kerrottu (ei vain tarjoushinta)", 20),
        # Most VPNs are foreign, so Y-tunnus is meaningless here. The equivalent
        # question — and the one this whole category turns on — is whether the
        # service tells you WHO OWNS IT. Three of the biggest share one owner.
        ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
        ("lainkayttoalue_kerrottu", "Lainkäyttöalue kerrottu", 10),
        ("lokikaytanto_kerrottu", "Lokikäytäntö kerrottu", 15),
        ("riippumaton_auditointi", "Riippumaton auditointi esillä", 10),
    ],
    # ------------------------------------------------------------------ batch 2
    "kulutusluotot": [
        # KSL 7:8-9 REQUIRES the effective rate and a representative example to be
        # given before the consumer commits. So this measures whether a lender meets
        # its own legal duty in public — not whether its rate is low.
        ("todellinen_vuosikorko_esilla", "Todellinen vuosikorko esillä ilman hakemusta", 30),
        ("esimerkkilaskelma_esilla", "Lakisääteinen esimerkkilaskelma esillä", 20),
        ("kulut_eriteltyna", "Kaikki kulut eriteltynä (tilinhoito, nosto, viivästys)", 15),
        # The point of the whole category: the brand on the ad is very often not the
        # company lending you the money.
        ("luotonantaja_ja_valvoja_kerrottu", "Todellinen luotonantaja ja valvoja kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "pankit": [
        ("palveluhinnasto_julkinen", "Palveluhinnasto julkisesti saatavilla ilman kirjautumista", 30),
        ("tilin_ja_kortin_maksut_esilla", "Tilin- ja kortinhoitomaksut esillä", 20),
        ("sopimusehdot_saatavilla", "Yleiset sopimusehdot julkisesti saatavilla", 15),
        ("konttorit_ja_aukioloajat", "Konttorit ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "autovakuutukset": [
        ("hintalaskuri_ilman_yhteystietoja", "Hinta-arvio ilman yhteystietoja", 30),
        ("vakuutusehdot_saatavilla", "Vakuutusehdot/tuoteseloste julkisesti saatavilla", 20),
        ("omavastuu_selkeasti", "Omavastuu kerrottu selkeästi", 15),
        ("bonusjarjestelma_kerrottu", "Bonusjärjestelmä kerrottu", 15),
        ("kaskotasot_vertailtavissa", "Kaskotasojen erot vertailtavissa", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ],
    "kotivakuutukset": [
        ("hintalaskuri_ilman_yhteystietoja", "Hinta-arvio ilman yhteystietoja", 30),
        ("vakuutusehdot_saatavilla", "Vakuutusehdot/tuoteseloste julkisesti saatavilla", 20),
        ("omavastuu_selkeasti", "Omavastuu kerrottu selkeästi", 15),
        ("korvausrajat_kerrottu", "Korvauskatot ja rajoitukset kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "matkavakuutukset": [
        ("hinta_esilla_ilman_yhteystietoja", "Hinta esillä ilman yhteystietoja", 30),
        ("vakuutusehdot_saatavilla", "Vakuutusehdot/tuoteseloste julkisesti saatavilla", 20),
        ("korvauskatot_kerrottu", "Korvauskatot (sairaus, matkatavara) kerrottu", 15),
        ("rajoitukset_kerrottu", "Rajoitukset (urheilulajit, ikä, riskimaat) kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "lemmikkivakuutukset": [
        ("hintalaskuri_ilman_yhteystietoja", "Hinta-arvio ilman yhteystietoja", 30),
        ("vakuutusehdot_saatavilla", "Vakuutusehdot/tuoteseloste julkisesti saatavilla", 20),
        ("korvauskatto_kerrottu", "Vuosittainen korvauskatto kerrottu", 15),
        ("rotu_ja_ikarajat_kerrottu", "Rotu- ja ikärajoitukset kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    # Comparison services live on commissions, so the vertical-specific questions
    # are about the SERVICE's own transparency: offers visible before your data,
    # who runs it, how it earns, and whether it admits its coverage limits.
    "sahkovertailupalvelut": [
        ("tarjoukset_ilman_yhteystietoja", "Tarjoukset ja hinnat näkyvät ilman yhteystietoja", 30),
        ("ansaintamalli_kerrottu", "Ansaintamalli (komissiot) kerrottu avoimesti", 20),
        ("kattavuus_kerrottu", "Vertailun kattavuus ja rajaukset kerrottu", 15),
        ("yhtiot_listattu", "Vertailussa mukana olevat sähköyhtiöt listattu", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 15),
    ],
    # ---------------- batch 3 (18.7.2026) — always lead with the 30-point question:
    # does the company tell you the price before you hand over your data?
    "autokatsastus": [
        ("katsastushinta_esilla", "Määräaikaiskatsastuksen hinta julkisesti esillä", 30),
        ("ajanvaraus_hinnalla", "Nettiajanvaraus näyttää hinnan ennen yhteystietoja", 20),
        ("asemat_ja_aukioloajat", "Asemat ja aukioloajat kerrottu", 15),
        ("palveluvalikoima_kuvattu", "Katsastuslajit ja lisäpalvelut hintoineen kuvattu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "autovuokraamot": [
        ("hinta_ilman_yhteystietoja", "Vuokrahinnan näkee ilman yhteystietoja", 30),
        ("omavastuu_ja_vakuutus", "Omavastuu ja vakuutusvaihtoehdot kerrottu", 20),
        ("vuokrausehdot_saatavilla", "Vuokrausehdot (km-rajat, polttoaine, ikärajat) julkisesti", 15),
        ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "optikot": [
        ("silmalasien_hinnat_esilla", "Silmälasien/linssien hintatietoja julkisesti esillä", 30),
        ("nakotarkastuksen_hinta", "Näöntarkastuksen hinta kerrottu", 20),
        ("ajanvaraus_verkossa", "Ajanvaraus verkossa ilman kirjautumista", 15),
        ("liikkeet_ja_aukioloajat", "Liikkeet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "yksityislaakarit": [
        ("vastaanottohinnat_esilla", "Vastaanottojen hinnat julkisesti esillä", 30),
        ("ajanvaraus_ilman_kirjautumista", "Ajanvaraus verkossa ilman kirjautumista", 20),
        ("kela_korvaus_kerrottu", "Kela-korvaus ja todellinen omavastuu kerrottu", 15),
        ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "kuntosalit": [
        ("jasenyyden_hinta_esilla", "Jäsenyyden hinta julkisesti esillä", 30),
        ("sopimusehdot_saatavilla", "Sopimusehdot (sitoutumisaika, irtisanominen) julkisesti", 20),
        ("liittymismaksut_kerrottu", "Liittymis- ja muut kertamaksut kerrottu", 15),
        ("salit_ja_aukioloajat", "Salit ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    # ---------------- batch 5 (21.7.2026) — global digital services follow the
    # vpn-palvelut convention: owner disclosure replaces Y-tunnus as the criterion.
    "suoratoistopalvelut": [
        ("hinnat_esilla", "Kuukausihinnat julkisesti esillä", 30),
        ("tasojen_erot_kerrottu", "Tilaustasojen erot (mainokset, laatu, laitteet) kerrottu", 20),
        ("irtisanominen_kerrottu", "Irtisanominen ja sitoutumisaika kerrottu", 15),
        ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
        ("suomenkielinen_palvelu", "Suomenkielinen sivusto ja hinnat euroissa", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "virustorjuntaohjelmat": [
        ("hinnat_esilla", "Hinnat julkisesti esillä", 30),
        ("uusimishinta_kerrottu", "Uusimishinta kerrottu (ei vain tarjoushinta)", 20),
        ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
        ("testitulokset_kerrottu", "Riippumattomat testitulokset (AV-TEST tms.) esillä", 15),
        ("suomenkielinen_palvelu", "Suomenkielinen sivusto ja hinnat euroissa", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "pilvitallennuspalvelut": [
        ("hinnat_esilla", "Tallennustilan hinnat julkisesti esillä", 30),
        ("uusimishinta_kerrottu", "Uusimishinta kerrottu (ei vain tarjoushinta)", 15),
        ("suomenkielinen_palvelu", "Suomenkielinen sivusto ja hinnat euroissa", 20),
        ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
        ("datan_sijainti_kerrottu", "Datan säilytysmaa tai lainkäyttöalue kerrottu", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "salasananhallintapalvelut": [
        ("hinnat_esilla", "Hinnat julkisesti esillä", 30),
        ("ilmainen_versio_kerrottu", "Ilmaisversion rajoitukset kerrottu selkeästi", 15),
        ("turvallisuusauditoinnit", "Riippumattomat tietoturva-auditoinnit julkaistu", 20),
        ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
        ("uusimishinta_kerrottu", "Uusimishinta kerrottu (ei vain tarjoushinta)", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "autokorjaamot": [
        ("hinnat_esilla", "Huoltojen hinnat tai hinnoitteluperusteet julkisesti", 30),
        ("ajanvaraus_verkossa", "Ajanvaraus verkossa ilman yhteydenottoa", 20),
        ("huoltopalvelut_kuvattu", "Palveluvalikoima kuvattu selkeästi", 15),
        ("toimipisteet_ja_aukioloajat", "Korjaamot ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    # ---------------- batch 4 (21.7.2026)
    "muuttopalvelut": [
        ("hinnat_esilla", "Muuton hinnat tai hinnoitteluperusteet julkisesti esillä", 30),
        ("tarjouslaskuri_verkossa", "Hinta-arvion saa verkossa ilman soittoa", 20),
        ("vakuutus_ja_vastuu_kerrottu", "Vakuutus ja vastuu vahingoista kerrottu", 15),
        ("toimialue_ja_yhteystiedot", "Toimialue ja yhteystiedot kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "siivouspalvelut": [
        ("hinnat_esilla", "Siivouksen hinnat julkisesti esillä", 30),
        ("varaus_verkossa", "Tilaus tai varaus onnistuu verkossa", 20),
        ("kotitalousvahennys_kerrottu", "Kotitalousvähennys ja sen vaikutus hintaan kerrottu", 15),
        ("toimialue_ja_yhteystiedot", "Toimialue ja yhteystiedot kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "autokoulut": [
        ("kurssihinnat_esilla", "Kurssien hinnat julkisesti esillä", 30),
        ("ilmoittautuminen_verkossa", "Ilmoittautuminen onnistuu verkossa", 20),
        ("kurssisisalto_kuvattu", "Kurssin sisältö (ajotunnit, teoria, maksuerät) kuvattu", 15),
        ("toimipisteet_ja_yhteystiedot", "Toimipisteet ja yhteystiedot kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "hammaslaakarit": [
        ("vastaanottohinnat_esilla", "Hammashoidon hinnat julkisesti esillä", 30),
        ("ajanvaraus_ilman_kirjautumista", "Ajanvaraus verkossa ilman kirjautumista", 20),
        ("kela_korvaus_kerrottu", "Kela-korvaus ja todellinen omavastuu kerrottu", 15),
        ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "rengasliikkeet": [
        ("renkaiden_hinnat_esilla", "Renkaiden hinnat julkisesti esillä", 30),
        ("asennus_ja_sailytys_hinnat", "Asennuksen ja rengassäilytyksen hinnat kerrottu", 20),
        ("ajanvaraus_verkossa", "Ajanvaraus verkossa ilman yhteydenottoa", 15),
        ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "pakohuoneet": [
        ("hinnat_esilla", "Pelien hinnat julkisesti esillä", 30),
        ("varaus_verkossa", "Varauskalenteri toimii verkossa ilman yhteydenottoa", 20),
        ("pelit_kuvattu", "Huoneet, vaikeustasot ja pelaajamäärät kuvattu", 15),
        ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "lakifirmat": [
        ("hinnat_esilla", "Hinnat (tuntihinta tai kiinteä hinta) julkisesti esillä", 30),
        ("palvelun_sisalto_kuvattu", "Palvelun sisältö (mitä hintaan kuuluu) kuvattu", 20),
        ("patevyys_kerrottu", "Juristien pätevyys (asianajaja/varatuomari/lakimies) kerrottu", 15),
        ("sopimusehdot_saatavilla", "Toimeksiannon ehdot julkisesti saatavilla", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "kiinteistonvalittajat": [
        ("valityspalkkio_esilla", "Välityspalkkio tai hinnasto julkisesti esillä", 30),
        ("palvelun_sisalto_kuvattu", "Palvelun sisältö (mitä palkkiolla saa) kuvattu", 20),
        ("sopimusehdot_saatavilla", "Toimeksiantosopimuksen ehdot julkisesti", 15),
        ("toimistot_ja_yhteystiedot", "Toimistot ja yhteystiedot kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
    "silmasairaalat": [
        # Core question: can you find out the price of laser eye surgery or cataract surgery
        # BEFORE you have to call or hand over your contact details?
        ("hinnat_esilla", "Leikkauksen hintatieto julkisesti esillä ilman yhteystietoja", 30),
        ("menetelmat_kuvattu", "Leikkausmenetelmät kuvattu (LASIK, PRK, SMILE, kaihileikkaus)", 20),
        ("varaus_verkossa", "Ajanvaraus tai arviokäynti tilattavissa verkossa", 20),
        ("takuu_tai_jalkitarkastus", "Takuu tai jälkitarkastukset kuvattu", 10),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ],
}

# Human-readable criteria string rendered on the methodology page.
def criteria_text(vertical):
    rows = TRANSPARENCY[vertical]
    parts = []
    for i, (_, label, w) in enumerate(rows):
        # Sentence case: keep the first criterion capitalised, lowercase the rest,
        # but never lowercase an acronym like "Y-tunnus".
        text = label if i == 0 or label.startswith("Y-") else label[0].lower() + label[1:]
        parts.append(f"{text} ({w})")
    return ", ".join(parts)


for _v, _rows in TRANSPARENCY.items():
    _t = sum(w for _, _, w in _rows)
    assert _t == 100, f"{_v} transparency weights total {_t}, must be 100"
assert sum(PILLAR_W.values()) == 100

# --- uutismediat (26.7.2026) --------------------------------------------------
# Median "hinta ennen dataa" -kysymys: mitä lukeminen maksaa ja kuka sisällöstä
# vastaa. Journalistinen läpinäkyvyys mitataan kuluttajan silmin sivustolta.
TRANSPARENCY["uutismediat"] = [
    ("tilaushinta_esilla", "Tilaushinta ja maksullisuus kerrottu selkeästi ennen tietojen antamista", 25),
    ("paatoimittaja_esilla", "Vastaava päätoimittaja ja toimituksen yhteystiedot esillä", 20),
    ("oikaisukaytanto_kuvattu", "Virheiden korjaus- ja oikaisukäytäntö kuvattu julkisesti", 20),
    ("mainonta_eroteltu", "Kaupallinen sisältö merkitty ja erottelu journalismista kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- aikakauslehdet (26.7.2026) -----------------------------------------------
# Aikakauslehden "hinta ennen dataa": mitä kestotilaus oikeasti maksaa ja miten
# sen saa loppumaan. Tilauksen päättämisen avoimuus on alan tunnettu kipupiste,
# ja se syöttää myös sitoutumisindeksiä (peruutus-avain).
TRANSPARENCY["aikakauslehdet"] = [
    ("tilaushinta_esilla", "Tilaushinnat (kesto- ja määräaikaistilaus) kerrottu selkeästi ennen tietojen antamista", 25),
    ("tilauksen_peruutus_kerrottu", "Tilauksen päättäminen ja peruutusehdot kerrottu julkisesti", 20),
    ("paatoimittaja_esilla", "Päätoimittaja ja toimituksen yhteystiedot esillä", 20),
    ("mainonta_eroteltu", "Kaupallinen sisältö merkitty ja erottelu journalismista kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- huonekaluketjut + elektroniikkaketjut (26.7.2026) ------------------------
# Sama vähittäiskaupan mittaristo kuin rautakaupoissa: hinta ennen dataa,
# toimituskulut ennen kassaa, palautusehdot julkisesti (syöttää sitoutumisindeksiä).
TRANSPARENCY["huonekaluketjut"] = [
    ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
    ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
    ("palautusehdot_saatavilla", "Palautus- ja takuuehdot julkisesti saatavilla", 20),
    ("myymalat_ja_aukioloajat", "Myymälät ja aukioloajat kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]
TRANSPARENCY["elektroniikkaketjut"] = [
    ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
    ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
    ("palautusehdot_saatavilla", "Palautus- ja takuuehdot julkisesti saatavilla", 20),
    ("myymalat_ja_aukioloajat", "Myymälät ja aukioloajat kerrottu (verkkokaupalla: noutopisteet)", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- urheiluvalineketjut (26.7.2026) ------------------------------------------
# Sama vähittäiskaupan mittaristo kuin rautakaupoissa ja huonekaluissa.
TRANSPARENCY["urheiluvalineketjut"] = [
    ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
    ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
    ("palautusehdot_saatavilla", "Palautus- ja takuuehdot julkisesti saatavilla", 20),
    ("myymalat_ja_aukioloajat", "Myymälät ja aukioloajat kerrottu (verkkokaupalla: noutopisteet)", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- ikkunaremontit + lampopumppuasentajat (27.7.2026) ------------------------
# Remonttipalvelun mittaristo kattoremonttien malliin: hintaindikaatio ennen
# yhteydenottoa, prosessi, takuut, vaihtoehdot.
TRANSPARENCY["ikkunaremontit"] = [
    ("hinta_indikaatio", "Hintatietoa tai hintalaskuri julkisesti esillä", 25),
    ("prosessi_kuvattu", "Remontin eteneminen kuvattu vaiheittain", 20),
    ("takuut_kerrottu", "Takuut ja niiden ehdot kerrottu", 20),
    ("materiaalit_kuvattu", "Ikkunavaihtoehdot ja energiatehokkuus kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]
TRANSPARENCY["lampopumppuasentajat"] = [
    ("hinta_indikaatio", "Hintatietoa tai hintalaskuri julkisesti esillä", 25),
    ("prosessi_kuvattu", "Asennuksen eteneminen kuvattu vaiheittain", 20),
    ("takuut_kerrottu", "Takuut ja niiden ehdot kerrottu", 20),
    ("materiaalit_kuvattu", "Laitevaihtoehdot ja merkit kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- aurinkopaneeliasentajat (27.7.2026) --------------------------------------
TRANSPARENCY["aurinkopaneeliasentajat"] = [
    ("hinta_indikaatio", "Hintatietoa tai hintalaskuri julkisesti esillä", 25),
    ("prosessi_kuvattu", "Asennuksen eteneminen kuvattu vaiheittain", 20),
    ("takuut_kerrottu", "Takuut ja niiden ehdot kerrottu", 20),
    ("materiaalit_kuvattu", "Paneeli- ja invertterivaihtoehdot kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- kukkakauppojen-verkkokaupat (28.7.2026) ----------------------------------
TRANSPARENCY["kukkakauppojen-verkkokaupat"] = [
    ("hinnat_esilla", "Kimppujen hinnat ja toimitusmaksu verkossa esillä", 25),
    ("toimitus_kerrottu", "Toimituspäivät, -alueet ja -kulut kerrottu ennen kassaa", 20),
    ("palautusehdot_saatavilla", "Korvaus- ja reklamaatiokäytäntö julkisesti saatavilla", 20),
    ("myymalat_ja_aukioloajat", "Välitysverkosto tai omat myymälät kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- erä 2 (28.7.2026): 5 kategoriaa ------------------------------------------
for _v in ("lastenvaatteiden-verkkokaupat", "lemmikkitarvikkeiden-verkkokaupat",
           "kirjakauppojen-verkkokaupat"):
    TRANSPARENCY[_v] = [
        ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
        ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
        ("palautusehdot_saatavilla", "Palautusehdot julkisesti saatavilla", 20),
        ("myymalat_ja_aukioloajat", "Myymälät tai noutopisteet ja palveluajat kerrottu", 15),
        ("y_tunnus_esilla", "Y-tunnus esillä", 10),
        ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ]
TRANSPARENCY["hotelliketjut"] = [
    ("hinnat_esilla", "Huonehinnat nähtävissä ilman kirjautumista", 25),
    ("peruutusehdot_esilla", "Peruutusehdot kerrottu ennen varausta", 20),
    ("lisapalvelut_hinnoiteltu", "Aamiaisen ja lisäpalvelujen hinnat kerrottu", 20),
    ("hotellit_ja_sijainnit", "Hotellit, sijainnit ja yhteystiedot kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]
TRANSPARENCY["taksipalvelut"] = [
    ("hinnat_esilla", "Hinnat tai hintaesimerkit julkisesti esillä", 25),
    ("tilaustavat_kuvattu", "Tilaustavat (sovellus, puhelin, katu) kuvattu", 20),
    ("peruutus_ja_lisamaksut", "Peruutus-, odotus- ja lisämaksukäytännöt kerrottu", 20),
    ("toiminta_alue_kerrottu", "Toiminta-alue kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- erä 9 (29.7.2026): autoliikkeet + pikaruokaketjut -----------------------
TRANSPARENCY["autoliikkeet"] = [
    ("hinnat_esilla", "Autojen hinnat verkossa esillä", 25),
    ("takuu_kerrottu", "Vaihtoautotakuun sisältö ja kesto kerrottu", 20),
    ("rahoituskulut_kerrottu", "Rahoituksen todellinen vuosikorko ja kulut esillä", 15),
    ("palautusehdot_saatavilla", "Palautus- tai vaihto-oikeus kerrottu", 15),
    ("toimipisteet_ja_aukioloajat", "Toimipisteet ja aukioloajat kerrottu", 10),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 5),
]

TRANSPARENCY["pikaruokaketjut"] = [
    ("hinnat_esilla", "Tuotteiden hinnat verkossa esillä", 25),
    ("allergeenit_esilla", "Allergeeni- ja ravintosisältötiedot tuotekohtaisesti", 25),
    ("alkupera_kerrottu", "Raaka-aineiden alkuperä kerrottu", 15),
    ("ravintolat_ja_aukioloajat", "Ravintolat ja aukioloajat kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

TRANSPARENCY["pakettipalvelut"] = [
    ("hinnasto_kuluttajalle", "Kotimaanpakettihinnat kuluttajalle julkisesti esillä", 30),
    ("toimitusaika_kerrottu", "Toimitusaika per palveluluokka kerrottu", 20),
    ("noutopisteet_tiedot", "Noutopisteiden määrä tai kartta saatavilla", 20),
    ("reklamaatiomenettely", "Korvaus- ja reklamaatiomenettely kuvattu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 5),
]

# --- era 11 (3.8.2026): musiikkipalvelut ---------------------------------------
# vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen (globaalit palvelut).
TRANSPARENCY["musiikkipalvelut"] = [
    ("hinnat_esilla", "Kuukausihinnat julkisesti esillä", 30),
    ("tasojen_erot_kerrottu", "Tilaustasojen erot (laatu, laitteet, offline) kerrottu", 20),
    ("irtisanominen_kerrottu", "Irtisanominen ja ilmaiskokeilun ehdot kerrottu", 15),
    ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 15),
    ("suomenkielinen_palvelu", "Suomenkielinen sivusto ja hinnat euroissa", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- era 12 (3.8.2026): pelitilauspalvelut --------------------------------------
# vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen (globaalit palvelut).
TRANSPARENCY["pelitilauspalvelut"] = [
    ("hinnat_esilla", "Kuukausihinta per taso julkisesti esillä", 30),
    ("tasojen_erot_kerrottu", "Tilaustasojen erot (pelikirjasto, laitteet, hinta) selitetty", 20),
    ("pelikirjasto_kuvaus", "Pelikirjaston kuvaus tai lista ennen tilaamista", 15),
    ("irtisanominen_kerrottu", "Irtisanominen ja ilmaiskokeilun ehdot kerrottu", 15),
    ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- era 10 (3.8.2026): kauneustuotteet-verkkokaupat ---------------------------
TRANSPARENCY["kauneustuotteet-verkkokaupat"] = [
    ("hinnat_esilla", "Tuotehinnat verkossa esillä", 25),
    ("toimitus_kerrottu", "Toimitustavat ja -kulut kerrottu ennen kassaa", 20),
    ("palautusehdot_saatavilla", "Palautusehdot julkisesti saatavilla", 20),
    ("ainesosaluettelo_saatavilla", "Tuotteiden ainesosaluettelot (INCI) löydettävissä", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- era 13 (3.8.2026): aanikirjapalvelut ----------------------------------------
# vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen (kaikki globaaleja palveluja).
TRANSPARENCY["aanikirjapalvelut"] = [
    ("hinnat_esilla", "Kuukausihinta julkisesti esillä", 30),
    ("kokeilujakso_kerrottu", "Ilmaiskokeilun ja irtisanomisen ehdot kerrottu", 20),
    ("kirjastokoko_kerrottu", "Kirjaston koko tai suomenkielisten kirjojen määrä kerrottu", 15),
    ("tasojen_erot_kerrottu", "Tilaustasojen erot kerrottu (jos tasoja on useita)", 15),
    ("omistaja_kerrottu", "Omistava yhtiö kerrottu sivustolla", 10),
    ("kuunteluaika_rajoitukset", "Kuunteluajan tai latauksien rajoitukset kerrottu selkeästi", 10),
]

# --- era 14 (3.8.2026): kylpylat ------------------------------------------------
# Core question: can you see the day-pass price before handing over your data?
TRANSPARENCY["kylpylat"] = [
    ("paivylipun_hinta_esilla", "Päivälipun hinta julkisesti esillä", 30),
    ("varaus_verkossa", "Lipun tai kylpyläpäivän voi ostaa tai varata verkossa", 20),
    ("palvelut_kuvattu", "Kylpylä-, sauna- ja vesipuistopalvelut kuvattu", 15),
    ("sijainti_ja_aukioloajat", "Sijainti ja aukioloajat kerrottu", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
]

# --- era 16 (4.8.2026): kirjanpito-ohjelmistot -----------------------------------
# SaaS-ohjelmistot pk-yrityksille. Tärkein kysymys: näkyykö kuukausihinta
# ennen kuin syötät yritystietosi tai rekisteröidyt kokeilujaksoon?
# Kaikki 6 yhtiötä ovat suomalaisrekisteröityjä (y_tunnus saatavilla).
# Weights: 30+20+20+15+10+5 = 100
TRANSPARENCY["kirjanpito-ohjelmistot"] = [
    # Korkein paino: SaaS-palvelun ostopäätöksen peruste on kuukausihinta —
    # jos se on piilossa rekisterin takana, kuluttaja ei voi vertailla.
    ("hinta_esilla", "Kuukausihinta tai hinnoittelu julkisesti esillä", 30),
    # Ilmainen kokeilu madaltaa kynnystä testata ohjelmistoa ennen sitoutumista.
    ("ilmainen_kokeilu", "Ilmainen kokeilujakso tai freemium tarjolla", 20),
    # Kirjanpito-ohjelma on arvoton ilman pankkiyhteyksiä ja laskutusintegraatioita.
    ("integraatiot_kuvattu", "Integraatiot (pankit, laskutus, palkka) kuvattu", 20),
    # Yrittäjälle suomenkielinen tuki on usein ratkaiseva käytettävyyskriteeri.
    ("tuki_suomeksi", "Suomenkielinen asiakastuki mainittu", 15),
    # Kertoo kuka vastaa datasta ja missä sitä käsitellään.
    ("y_tunnus_esilla", "Y-tunnus tai omistava yhtiö esillä", 10),
    # Ohjekeskus tai UKK vähentää tukipyyntöjä ja osoittaa palvelun kypsyyden.
    ("ukk_ja_ohjeet", "Ohjekeskus, oppaat tai UKK saatavilla", 5),
]

# --- era 15 (3.8.2026): lentoyhtiöt ----------------------------------------------
# Kaikki paitsi Finnair ovat globaaleja yhtiöitä — vpn-palvelut-konventio:
# omistaja_kerrottu korvaa y_tunnuksen. Tärkein kysymys: näkyykö kokonaishinta
# (sis. lisämaksut) ennen kuin olet jo syöttänyt matkustajatietosi?
# Weights: 30+20+20+15+10+5 = 100
TRANSPARENCY["lentoyhtiot"] = [
    # Halpalentoyhtiöillä matkatavara-, paikkavalinta- ja prioriteettipalvelumaksut
    # voivat moninkertaistaa perushinnan. Tärkein mittari on näytetäänkö ne ENNEN kassaa.
    ("lisamaksut_nakyy_varauksessa", "Lisämaksujen (matkatavarat, istumapaikka) hinnat näkyvät varauksen aikana", 30),
    # Lopullinen kokonaishinta veroineen on oltava näkyvissä ennen maksua EU-lainsäädännön
    # (EU 1008/2008) nojalla — mittaamme onko se selvästi näkyvissä ENNEN checkout-nappia.
    ("kokonaishinta_ennen_maksua", "Kokonaishinta verot ja maksut mukaan lukien näytetään ennen maksua", 20),
    # Muutokset ja peruutukset ovat keskeinen kuluttajariski lennoissa — pitäisi olla
    # helposti löydettävissä ilman asiakaspalveluyhteydenottoa.
    ("peruutus_ja_muutosehdot", "Peruutus- ja muutosehdot julkisesti saatavilla", 20),
    # Kanta-asiakasohjelmat ohjaavat paljon matkustuspäätöksiä — näkyykö etujen sisältö
    # ja tasovaatimukset selkeästi ennen liittymistä?
    ("lojaaliohjelma_kerrottu", "Lojaaliohjelma, etujen sisältö ja tasot kerrottu", 15),
    # Kaikki paitsi Finnair ovat ulkomaisia yhtiöitä — kertoo kuluttajalle kenen sääntelyn
    # piirissä yhtiö toimii ja mistä pitää reklamoida.
    ("omistaja_tai_rekisterointimaa", "Omistava yhtiö tai rekisteröintimaa kerrottu", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 5),
]

# --- era 13 (4.8.2026): kahvilaketjut -----------------------------------------
TRANSPARENCY["kahvilaketjut"] = [
    ("hinnat_esilla", "Tuotteiden hinnat verkossa esillä", 25),
    ("allergeenit_esilla", "Allergeeni- ja ravintosisältötiedot tuotekohtaisesti", 20),
    ("kahvin_alkupera", "Kahvin alkuperä tai reilu kauppa -sitoumus kerrottu", 15),
    ("ravintolat_ja_aukioloajat", "Toimipisteet ja aukioloajat helposti löydettävissä", 15),
    ("y_tunnus_esilla", "Y-tunnus esillä", 10),
    ("riippumaton_arvio", "Riippumaton arviolähde esillä", 10),
    ("kanta_asiakasohjelma_kerrottu", "Kanta-asiakasohjelma tai sovellus kuvattu sivustolla", 5),
]
