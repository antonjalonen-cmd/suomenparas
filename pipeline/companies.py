# -*- coding: utf-8 -*-
"""Verified company metadata per vertical (research pass 16.7.2026).

Every Y-tunnus here was confirmed against PRH/YTJ open data, not guessed.
`omistaja` is the real parent — the site publishes ownership because several
consumer brands share one owner, which is not obvious from the brand alone.

Excluded on purpose (verified dead/duplicate — do not re-add without re-checking):
  vakuutukset:     A-Vakuutus (old name of Pohjola 1458359-3), Folksam (merged into
                   Fennia 2019), Nordea Vahinkovakuutus (resells If), Säästöpankki
                   (non-life sales ended 3.6.2025), Aktia (life only), Hedvig (never
                   launched in FI), Moi Vakuutus (does not exist)
  sahkosopimukset: Väre (absorbed by Helen 31.5.2026), Savon Voima + Tampereen
                   Energia (retail sold to Väre), Lumme + Loiste (absorbed by Oomi
                   1.1.2026), Fi-Nergy Voima (bankrupt 21.7.2022), Kymppivoima
                   (procurement consortium, no consumer sales), Seiverkot (grid, not
                   a retailer), Herrfors (regional only)
  laajakaista:     Saunalahti (= Elisa), Moi (= DNA sub-brand, mobile only), Adola
                   (= Valoo), Netplaza (ceased 31.12.2021), PPO (merged into Elisa
                   2013), VLP (now Loihde, exited telecom), SSP (now Finda, holding
                   co), Karjalan Kaista + Telemore (could not verify they exist)
"""

COMPANIES = {
    "vakuutukset": [
        dict(slug="if", nimi="If", domain="if.fi", y_tunnus="1602149-8",
             omistaja="Sampo Oyj (If Vahinkovakuutus Oyj, Suomen sivuliike)"),
        dict(slug="lahitapiola", nimi="LähiTapiola", domain="lahitapiola.fi", y_tunnus="0211034-2",
             omistaja="Keskinäinen yhtiö — asiakkaiden omistama"),
        dict(slug="pohjola", nimi="Pohjola Vakuutus", domain="pohjola.fi", y_tunnus="1458359-3",
             omistaja="OP Osuuskunta (OP Ryhmä)"),
        dict(slug="fennia", nimi="Fennia", domain="fennia.fi", y_tunnus="0196826-7",
             omistaja="Keskinäinen yhtiö — asiakkaiden omistama"),
        dict(slug="turva", nimi="Turva", domain="turva.fi", y_tunnus="0211695-5",
             omistaja="Keskinäinen yhtiö — asiakkaiden omistama"),
        dict(slug="pohjantahti", nimi="Pohjantähti", domain="pohjantahti.fi", y_tunnus="0146905-4",
             omistaja="Keskinäinen yhtiö — asiakkaiden omistama"),
        dict(slug="popvakuutus", nimi="POP Vakuutus", domain="popvakuutus.fi", y_tunnus="2432824-6",
             omistaja="LähiTapiola 70 % / POP Pankki -ryhmä 30 % (Suomen Vahinkovakuutus Oy)"),
    ],
    "sahkosopimukset": [
        dict(slug="fortum", nimi="Fortum", domain="fortum.fi", y_tunnus="1852328-0",
             omistaja="Fortum Oyj — Suomen valtio enemmistöomistajana (Fortum Markets Oy)"),
        dict(slug="helen", nimi="Helen", domain="helen.fi", y_tunnus="2630573-4",
             omistaja="Helsingin kaupunki — sulautti Väre-brändin 31.5.2026"),
        dict(slug="oomi", nimi="Oomi", domain="oomi.fi", y_tunnus="1703296-5",
             omistaja="Seitsemän kunnallisen energiayhtiön yhteisyritys (Oomi Palvelut Oy)"),
        dict(slug="vattenfall", nimi="Vattenfall", domain="vattenfall.fi", y_tunnus="1842073-2",
             omistaja="Vattenfall AB — Ruotsin valtio"),
        dict(slug="vaasansahko", nimi="Vaasan Sähkö", domain="vaasansahko.fi", y_tunnus="3484498-1",
             omistaja="Vaasan kaupunki (99,9 %)"),
        dict(slug="turkuenergia", nimi="Turku Energia", domain="turkuenergia.fi", y_tunnus="0984944-9",
             omistaja="Turun kaupunki (100 %)"),
        dict(slug="pks", nimi="PKS", domain="pks.fi", y_tunnus="0214732-1",
             omistaja="Pohjois-Karjalan kunnat (Pohjois-Karjalan Sähkö Oy)"),
        dict(slug="omavoima", nimi="Omavoima", domain="omavoima.fi", y_tunnus="2209312-1",
             omistaja="Rauman Energia, Vakka-Suomen Voima, Leppäkosken Group, Valkeakosken Energia"),
        dict(slug="nordicgreen", nimi="Nordic Green Energy", domain="nordicgreen.fi", y_tunnus="2220675-5",
             omistaja="Switch Nordic Green AB (Ruotsi) — Suomen sivuliike"),
    ],
    "laajakaista": [
        dict(slug="elisa", nimi="Elisa", domain="elisa.fi", y_tunnus="0116510-6",
             omistaja="Pörssiyhtiö (Nasdaq Helsinki) — myös Saunalahti-brändi",
             saatavuus="Valtakunnallinen"),
        dict(slug="telia", nimi="Telia", domain="telia.fi", y_tunnus="1475607-9",
             omistaja="Telia Company AB (Ruotsi)", saatavuus="Valtakunnallinen"),
        dict(slug="dna", nimi="DNA", domain="dna.fi", y_tunnus="0592509-6",
             omistaja="Telenor ASA (Norja) — myös Moi Mobiili -brändi",
             saatavuus="Valtakunnallinen"),
        dict(slug="valoo", nimi="Valoo", domain="valoo.fi", y_tunnus="2925233-2",
             omistaja="Infrastruktuurisijoittajien omistama (ent. Adola)",
             saatavuus="Alueellinen — 50+ kuntaa"),
        # Lounea's own site markets nationwide reach; its owned fibre footprint is
        # concentrated in Southwest Finland. We could not verify a clean national
        # availability claim, so we state both rather than pick one.
        dict(slug="lounea", nimi="Lounea", domain="lounea.fi", y_tunnus="0139471-8",
             omistaja="Noin 16 000 yksityistä osakkeenomistajaa",
             saatavuus="Ydinverkko Varsinais-Suomessa; markkinoi valtakunnallisesti"),
        dict(slug="mpy", nimi="MPY", domain="mpy.fi", y_tunnus="3363506-1",
             omistaja="Infranode (pohjoismainen infrastruktuurisijoittaja)",
             saatavuus="Alueellinen — Itä-Suomi"),
        dict(slug="kaisanet", nimi="Kaisanet", domain="kaisanet.fi", y_tunnus="2366937-2",
             omistaja="Kainuun Puhelinosuuskunta 66 % + Puhelinosuuskunta IPY",
             saatavuus="Alueellinen — Kainuu ja Ylä-Savo"),
        dict(slug="lennu", nimi="Lennu", domain="lennu.fi", y_tunnus="0133011-6",
             omistaja="LennuNet Oy — itsenäinen alueoperaattori (ent. IPP)",
             saatavuus="Alueellinen — Pirkanmaa ja Satakunta"),
        dict(slug="blc", nimi="BLC", domain="blc.fi", y_tunnus="3262182-1",
             omistaja="Savonlinnan BLC-osuuskunta (BLC Telecom Oy)",
             saatavuus="Alueellinen — Etelä-Savo"),
    ],
}

if __name__ == "__main__":
    for v, cs in COMPANIES.items():
        print(f"{v}: {len(cs)}")
        seen = set()
        for c in cs:
            assert c["y_tunnus"] not in seen, f"duplicate Y-tunnus in {v}: {c['y_tunnus']}"
            seen.add(c["y_tunnus"])
    print("total:", sum(len(c) for c in COMPANIES.values()))
