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
