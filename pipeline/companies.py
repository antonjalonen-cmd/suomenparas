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
    # ---------------------------------------------------------------- batch 1
    # EXCLUDED (verified 16.7.2026): Sonera + Tele Finland (both absorbed into the
    # Telia brand in 2017 — dead), "Vaihtoehto" (no evidence it exists), Lounea and
    # Kaisanet (broadband only, no mobile product).
    "puhelinliittymat": [
        dict(slug="elisa", nimi="Elisa", domain="elisa.fi", y_tunnus="0116510-6",
             omistaja="Pörssiyhtiö (Nasdaq Helsinki) — myös Saunalahti-brändi",
             verkko="Oma verkko"),
        dict(slug="telia", nimi="Telia", domain="telia.fi", y_tunnus="1475607-9",
             omistaja="Telia Company AB (Ruotsi) — myös entinen Sonera ja Tele Finland",
             verkko="Oma verkko"),
        dict(slug="dna", nimi="DNA", domain="dna.fi", y_tunnus="0592509-6",
             omistaja="Telenor ASA (Norja)", verkko="Oma verkko"),
        dict(slug="moi", nimi="Moi Mobiili", domain="moi.fi", y_tunnus="2758687-3",
             omistaja="DNA Oyj — 100 % (ostettu 1/2019)", verkko="DNA:n verkko"),
        dict(slug="gigamobiili", nimi="Giga Mobiili", domain="gigamobiili.fi", y_tunnus="3505729-3",
             omistaja="Gigantti / Elkjøp (Norja) — rekisteröity 1/2025",
             verkko="DNA:n verkko"),
        dict(slug="oomimobiili", nimi="Oomi Mobiili", domain="oomi.fi", y_tunnus="3101315-4",
             omistaja="Yhdeksän kunnallisen energiayhtiön yhteisyritys",
             verkko="Asiakas valitsee: DNA tai Telia"),
        dict(slug="globetel", nimi="Globetel", domain="globetel.fi", y_tunnus="1094711-8",
             omistaja="Itsenäinen, perustajaomisteinen (1997)",
             verkko="Telian verkko (ei vahvistettu Globetelin omilta sivuilta)"),
    ],
    # EXCLUDED (verified 16.7.2026): Handelsbanken (poistui Suomen vähittäispankki-
    # toiminnasta 2026), Diners Club (poistui 2019), St1 (ei uusia; St1 Visa päättyy
    # 30.9.2026), Klarna/N26/Revolut (vain debit, ei luottokorttia), Neste (suljettu
    # ketjukortti), Lidl (ei omaa korttia), Enento (luottotietoyhtiö, ei myöntäjä),
    # "Lunar Credit" (= Creditstar Finland Oy:n joustoluotto ~119,6 % todellinen
    # vuosikorko, EI tanskalainen Lunar eikä luottokortti).
    # Instabank jätettiin pois: Y-tunnusta 2986430-4 ei löydy PRH:n rajapinnasta.
    "luottokortit": [
        dict(slug="op-visa", nimi="OP-Visa", domain="op.fi", y_tunnus="0751699-0",
             omistaja="OP Vähittäisasiakkaat Oyj (OP Ryhmä) — myöntää myös K-Plussa Mastercardin"),
        dict(slug="k-plussa", nimi="K-Plussa Mastercard", domain="plussamaksuaika.fi", y_tunnus="0751699-0",
             omistaja="OP Vähittäisasiakkaat Oyj — Kesko tuo vain Plussa-etuohjelman"),
        dict(slug="nordea-credit", nimi="Nordea Credit", domain="nordea.fi", y_tunnus="2858394-9",
             omistaja="Nordea Bank Abp"),
        dict(slug="danske-mastercard", nimi="Danske Bank Mastercard", domain="danskebank.fi", y_tunnus="1078693-2",
             omistaja="Danske Bank A/S (Tanska) — Suomen sivuliike"),
        dict(slug="s-etukortti", nimi="S-Etukortti Visa", domain="s-pankki.fi", y_tunnus="2557308-3",
             omistaja="S-Pankki Oyj (SOK / S-ryhmä)"),
        dict(slug="aktia-credit", nimi="Aktia Credit", domain="aktia.fi", y_tunnus="2181702-8",
             omistaja="Aktia Bank Abp — myöntää itse"),
        dict(slug="pop-visa", nimi="POP Visa Credit", domain="poppankki.fi", y_tunnus="2192977-5",
             omistaja="Bonum Pankki Oyj — POP Pankki -ryhmän keskuspankki"),
        dict(slug="saastopankki-visa", nimi="Säästöpankki Visa Credit", domain="saastopankki.fi", y_tunnus="2238752-5",
             omistaja="Säästöpankkien Keskuspankki Suomi Oyj — EI sama kuin OmaSp"),
        # Santander DROPPED 16.7.2026: santanderconsumer.fi sells lainat, ajoneuvo-
        # rahoitus, osamaksu ja leasing — EI kuluttajan luottokorttia. /luottokortti
        # palauttaa 200 mutta on soft-404 (sama navigaatiorunko kuin etusivulla, ei
        # korttisisältöä). Tutkimusagentti väitti "Santander Visa Classic" — sitä ei
        # voitu vahvistaa yhtiön omilta sivuilta, joten sitä ei julkaista.
    ],
    # EXCLUDED (verified 16.7.2026): Handelsbanken (poistui Suomen vähittäispankki-
    # toiminnasta; arvopaperipalvelut päättyivät 31.5.2024), Avanza (uusi tili vaatii
    # ruotsalaisen henkilötunnuksen + BankID → suomalainen ei voi avata), Interactive
    # Brokers / Revolut / Lightyear (ei suomenkielistä palvelua), Trading 212 (suomen
    # kieltä ei voitu vahvistaa), "Nordic Fund Market" (ei löytynyt).
    # eQ ja Seligson ovat rahastoyhtiöitä (ei osake-/ETF-kauppaa) → eri kategoria.
    # HUOM: Seligson on 100 % LähiTapiolan omistama.
    "sijoitusalustat": [
        dict(slug="nordnet", nimi="Nordnet", domain="nordnet.fi", y_tunnus="2329589-2",
             omistaja="Nordnet AB (publ), Ruotsi — Suomen sivuliike"),
        dict(slug="op-sijoitus", nimi="OP", domain="op.fi", y_tunnus="0242522-1",
             omistaja="OP Osuuskunta — jäsenten omistama"),
        dict(slug="nordea-sijoitus", nimi="Nordea", domain="nordea.fi", y_tunnus="2858394-9",
             omistaja="Nordea Bank Abp — pääkonttori Helsingissä 2018 alkaen"),
        # S-Pankki DROPPED 16.7.2026: sen sijoitussivuilta löytyy vain RAHASTOJA — ei
        # osakekauppaa eikä arvo-osuustiliä (varmistettu s-pankki.fi/fi/sijoittaminen).
        # Sama sääntö kuin eQ:lla ja Seligsonilla: rahastoyhtiö ei kuulu
        # osakekauppa-alustojen vertailuun. Johdonmukaisuus > listan pituus.
        dict(slug="danske-sijoitus", nimi="Danske Bank", domain="danskebank.fi", y_tunnus="1078693-2",
             omistaja="Danske Bank A/S (Tanska) — Suomen sivuliike"),
        # Alexandria DROPPED 16.7.2026: varainhoitotalo, ei itsepalveluosakekauppaa
        # (varmistettu alexandria.fi — vain varainhoito, rahastot, sijoitusneuvojat;
        # ei osakekauppaa, arvo-osuustiliä eikä kaupankäyntiä). Sama sääntö kuin
        # S-Pankilla, eQ:lla ja Seligsonilla.
        dict(slug="evli", nimi="Evli", domain="evli.com", y_tunnus="3239286-2",
             omistaja="Evli Oyj — itsenäinen (2022 jakautuminen)"),
        dict(slug="mandatum-trader", nimi="Mandatum Trader", domain="mandatumtrader.fi", y_tunnus="0641130-2",
             omistaja="Mandatum Oyj — irtautui Sampo-konsernista 1.10.2023; kaupankäyntiteknologia Saxo Bankilta"),
        # Saxo has a registered Finnish branch (Y-tunnus PRH-verified), which is why it
        # stays while IBKR/Revolut/Lightyear are excluded — those have no Finnish entity
        # at all. But home.saxo/fi-fi 404s: a Finnish branch with no Finnish-language
        # site. That is a real finding, not a reason to drop it.
        dict(slug="saxo", nimi="Saxo Bank", domain="home.saxo", y_tunnus="2927844-4",
             omistaja="Saxo Bank A/S (Tanska) — Suomen sivuliike; ei suomenkielistä sivustoa"),
    ],
    # EXCLUDED (verified 16.7.2026): Atlas VPN (Nord Security LOPETTI 24.4.2024,
    # asiakkaat siirrettiin NordVPN:ään), Zenmate (Kape sulautti CyberGhostiin 2023),
    # TunnelBear (McAfee, ei suomenkielistä sivua), IPVanish + hide.me (suomenkielistä
    # sivua ei voitu vahvistaa), VPN.ac (marginaalinen Suomessa).
    # HUOM: vain F-Secure on suomalainen → Y-tunnus vain sillä; muille kerrotaan
    # lainkäyttöalue ja omistaja Y-tunnuksen sijaan.
    "vpn-palvelut": [
        dict(slug="nordvpn", nimi="NordVPN", domain="nordvpn.com", y_tunnus=None,
             omistaja="Nord Security / Cyberspace B.V. (Alankomaat)", lainkayttoalue="Panama"),
        dict(slug="surfshark", nimi="Surfshark", domain="surfshark.com", y_tunnus=None,
             omistaja="Cyberspace B.V. (Alankomaat) — sama omistaja kuin NordVPN, yhdistyivät 2/2022",
             lainkayttoalue="Alankomaat"),
        dict(slug="expressvpn", nimi="ExpressVPN", domain="expressvpn.com", y_tunnus=None,
             omistaja="Kape Technologies (ostettu 2021)", lainkayttoalue="Brittiläiset Neitsytsaaret"),
        dict(slug="cyberghost", nimi="CyberGhost", domain="cyberghostvpn.com", y_tunnus=None,
             omistaja="Kape Technologies (ostettu 2017)", lainkayttoalue="Romania"),
        dict(slug="pia", nimi="Private Internet Access", domain="privateinternetaccess.com", y_tunnus=None,
             omistaja="Kape Technologies (ostettu 2019)", lainkayttoalue="Yhdysvallat"),
        dict(slug="protonvpn", nimi="Proton VPN", domain="protonvpn.com", y_tunnus=None,
             omistaja="Proton AG — Proton Foundation (voittoa tavoittelematon)", lainkayttoalue="Sveitsi"),
        dict(slug="mullvad", nimi="Mullvad", domain="mullvad.net", y_tunnus=None,
             omistaja="Amagicom AB — perustajaomisteinen, ei pääomasijoittajia", lainkayttoalue="Ruotsi"),
        dict(slug="fsecure", nimi="F-Secure VPN", domain="f-secure.com", y_tunnus="3269349-7",
             omistaja="F-Secure Oyj — suomalainen, Nasdaq Helsinki (ent. Freedome)",
             lainkayttoalue="Suomi"),
        dict(slug="windscribe", nimi="Windscribe", domain="windscribe.com", y_tunnus=None,
             omistaja="Windscribe Limited — itsenäinen", lainkayttoalue="Kanada"),
    ],
    # EXCLUDED (verified 16.7.2026): Nebula, Sigmatic ja Webhotelli.fi — Telia myi koko
    # webhotelli-liiketoimintansa Zonerille 1.8.2024; Nebula on nykyään Telian yritys-
    # ICT-brändi, ei kuluttajan webhotelli. Ficolo (nyk. Verne) = konesali, ei webhotelli.
    # Elisa Yritysweb = B2B-lisäpalvelu. Hostperi ja "Cloud Nine" — ei löydy lainkaan.
    # KRIITTINEN: Planeetta + Domainhotelli + Hostingpalvelu.fi ovat SAMA yhtiö
    # (Planeetta Internet Oy 1753494-9, omistaja team.blue) — vain yksi rivi listalla.
    "webhotellit": [
        dict(slug="zoner", nimi="Zoner", domain="zoner.fi", y_tunnus="1985221-1",
             omistaja="One.com Group AB (Tanska/Ruotsi) — osti Telian webhotellit 1.8.2024"),
        dict(slug="louhi", nimi="Louhi", domain="louhi.fi", y_tunnus="1946409-1",
             omistaja="Louhi Net Oy — itsenäinen suomalainen (Espoo)"),
        dict(slug="planeetta", nimi="Planeetta", domain="planeetta.fi", y_tunnus="1753494-9",
             omistaja="team.blue (Hg Capital) — sama yhtiö kuin Domainhotelli ja Hostingpalvelu.fi"),
        dict(slug="shellit", nimi="Shellit", domain="shellit.org", y_tunnus="2405351-0",
             omistaja="Multim Oy — itsenäinen suomalainen (Merikarvia); myös Tavu Cloud ja VPSfinland"),
        dict(slug="seravo", nimi="Seravo", domain="seravo.com", y_tunnus="2392019-2",
             omistaja="Seravo Oy — itsenäinen suomalainen (Tampere)"),
        # Capnova DROPPED 16.7.2026: capnova.fi (and domainmaailma.fi) now redirect away
        # to glesys.fi — a Swedish host. Lighthouse happily measured glesys.fi and
        # labelled it "capnova", i.e. we would have published another company's website
        # under Capnova's name. The brand no longer sells hosting under its own site.
        dict(slug="kotisivut", nimi="Kotisivut.com", domain="kotisivut.com", y_tunnus="3561966-3",
             omistaja="Mediam Oy — itsenäinen suomalainen"),
        dict(slug="hostaan", nimi="Hostaan", domain="hostaan.fi", y_tunnus="2950656-6",
             omistaja="Hostaan Oy — itsenäinen suomalainen (Kuopio, 2018)"),
    ],
}

if __name__ == "__main__":
    # Slugs must be unique — a collision would overwrite a page.
    # Y-tunnus may legitimately repeat: in `luottokortit` the unit is a CARD, not a
    # company, and OP issues both OP-Visa and K-Plussa Mastercard. That is not an
    # error, it is the ownership story — so report it instead of failing on it.
    total_shared = 0
    for v, cs in COMPANIES.items():
        slugs = [c["slug"] for c in cs]
        assert len(slugs) == len(set(slugs)), f"duplicate slug in {v}"
        by_y = {}
        for c in cs:
            if c["y_tunnus"]:
                by_y.setdefault(c["y_tunnus"], []).append(c["nimi"])
        shared = {y: n for y, n in by_y.items() if len(n) > 1}
        total_shared += len(shared)
        print(f"{v}: {len(cs)}")
        for y, names in shared.items():
            print(f"    shared issuer {y}: {' + '.join(names)}  <- must be disclosed on the page")
    print("total:", sum(len(c) for c in COMPANIES.values()),
          f"| shared-owner groups: {total_shared}")
