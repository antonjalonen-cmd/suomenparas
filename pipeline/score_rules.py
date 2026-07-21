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
