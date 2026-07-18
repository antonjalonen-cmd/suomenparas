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
        # domain op.fi, not pohjola.fi: pohjola.fi 301-redirects into op.fi — OP sells its
        # insurance on the bank's platform, so op.fi IS the site a visitor lands on (same
        # decision as the four product lines below). Changed 18.7.2026 with the JS re-measure.
        dict(slug="pohjola", nimi="Pohjola Vakuutus", domain="op.fi", y_tunnus="1458359-3",
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
    # ---------------------------------------------------------------- batch 2
    # CATEGORY SWAPPED 17.7.2026: the queue asked for "pikavipit". That category no
    # longer describes a real market. The 1.10.2023 rate cap (viitekorko + 15 pp, max
    # 20 %) made the classic short-term pikavippi unviable, and the brands either died
    # or lengthened into ordinary multi-year kulutusluotto. Publishing a "pikavipit"
    # ranking in 2026 would rank a product that no longer exists, so this is
    # `kulutusluotot` instead. It is also cleanly distinct from `lainavertailu`:
    # that page compares BROKERS, this one compares the LENDERS themselves.
    #
    # DEDUPED BY LEGAL ENTITY — brand count wildly overstates lender count here, which
    # is exactly what this site exists to show:
    #   Vippi.fi + Limiitti.fi  = Saldo Bank UAB Suomen sivuliike (3273394-6)
    #
    # RISICUM DROPPED 17.7.2026 — the best catch of this batch, and nearly missed. Its
    # research agent reported it "live, selling Joustolaina at 19.90 %", and risicum.fi
    # still returns HTTP 200 under the marketing title "Laina arkielämään 10 000 euroon
    # asti. Laina tilillesi nyt." But the page body says:
    #   "Uusia nostoja Risicum Joustolainoille ei myönnetä 1.10.2023 alkaen. Laskutus
    #    jatkuu normaalisti, kunnes luotto on loppuun maksettu."
    #   "Risicumin puhelinasiakaspalvelu on päättynyt 30.9.2024."
    # It stopped granting new credit on the exact day the rate cap took effect and is now
    # a run-off servicing page with stale advertising on top. A live domain and a loan
    # headline are not evidence that a company still sells — read the body. (Its owner
    # Aurajoki Nordic Oy 1998514-5 does still exist; the brand's aputoiminimet OK Money,
    # iKassa and Suomen Pienlaina are the same entity and are not sold separately.)
    #
    # EXCLUDED — dead (verified 17.7.2026):
    #   Euroloan (lender Mash Finance Oyj konkurssi 15.3.2021; euroloan.fi is now run by
    #     Holla Online Oy 2672272-2, a PRH-classified ADVERTISING agency with no credit
    #     business line and no "Euroloan" name registered — a zombie brand on the old
    #     lender's domain), Credit24 (site itself says "olemme lopettaneet toimintamme
    #     Suomessa"), Aasa (stopped direct lending 2019, now forwards to Omalaina;
    #     aasa.fi does not resolve), Everyday/OPR-Vakuus/Ostosraha (no new credit since
    #     the 2019 cap), Suomen Viestilaina (domain serves a dangling Azure wildcard
    #     cert; no PRH match), Blue Finance (3105036-9 exists but its own site says
    #     "kuluttajalainat ovat tauolla" — business loans only).
    # EXCLUDED — not a lender: Fixura (2246639-7; own site calls it a marketplace
    #   mediating loans from investors — P2P, not a balance-sheet lender), Halpalaina
    #   and Nordic Finance (brokers → they belong in `lainavertailu`, not here).
    # EXCLUDED — no verifiable Finnish registration (the honest gap, disclosed on the
    #   page): Ferratum (its Finnish entity Multitude SE 1950969-1 DEREGISTERED 30.6.2024
    #   — every name on the PRH record ends that day; the lender of record is now
    #   Multitude Bank p.l.c., Malta), Instabank (2986430-4 returns NOT FOUND from PRH),
    #   Bank Norwegian (2717751-9 NOT FOUND; now a NOBA Bank Group AB brand). All three
    #   demonstrably sell to Finns cross-border under EU passporting — we exclude them
    #   because we could not confirm them from the Finnish trade register, which is the
    #   one standard we apply to everyone. Same rule that already excluded Instabank
    #   from `luottokortit`.
    "kulutusluotot": [
        dict(slug="saldo", nimi="Saldo", domain="saldo.com", y_tunnus="3273394-6",
             omistaja="Saldo Bank UAB (Liettua) — Suomen sivuliike; myös Vippi.fi ja Limiitti.fi",
             valvoja="Liettuan keskuspankki (ECB-järjestelmä)"),
        dict(slug="tfbank", nimi="TF Bank", domain="tfbank.fi", y_tunnus="3529515-2",
             omistaja="TF Bank Nordic AB (Ruotsi) — Suomen sivuliike, rek. 23.4.2025",
             valvoja="Finansinspektionen (Ruotsi)"),
        dict(slug="resursbank", nimi="Resurs Bank", domain="resursbank.fi", y_tunnus="2110471-4",
             omistaja="Resurs Bank AB (Ruotsi) — Suomen sivuliike",
             valvoja="Finansinspektionen (Ruotsi)"),
        dict(slug="northmill", nimi="Northmill", domain="northmill.com", y_tunnus="3166457-1",
             omistaja="Northmill Bank AB (Ruotsi) — Suomen sivuliike; myös Easycredit ja Credigo",
             valvoja="Finansinspektionen (Ruotsi)"),
        dict(slug="svea", nimi="Svea", domain="svea.com", y_tunnus="3237195-7",
             omistaja="Svea Bank AB (Ruotsi) — Suomen sivuliike",
             valvoja="Finansinspektionen (Ruotsi)"),
        dict(slug="santander", nimi="Santander Consumer Finance", domain="santanderconsumer.fi",
             y_tunnus="2076455-0",
             omistaja="Banco Santander (Espanja) — Santander Consumer Finance Oy on suomalainen yhtiö",
             valvoja="Finanssivalvonta (Suomi)"),
    ],
    # ⚠️ NOT BUILT 17.7.2026 — config is complete and correct, but `data/pankit.json` is
    # deliberately not generated, so the category stays dark. Reason: **OP cannot be
    # measured.** op.fi renders everything via JavaScript and blocks every fetch path we
    # have (WebFetch refused, browser pane blocked by policy, curl gets a ~900-character
    # login shell). OP is roughly a third of Finnish retail banking and the first name any
    # reader looks for. Publishing "Suomen paras pankki 2026" while silently omitting it
    # would be a false headline, and publishing OP scored on what our crawler could not
    # see would be a false score. Neither is shippable, so the category waits for a
    # JS-capable fetch path. The other 8 banks verified fine — this is not wasted work.
    # (Same root cause as the Pohjola exclusion below.)
    #
    # CATEGORY RENAMED 17.7.2026: the queue asked for "pankkien asiakaspalvelu". We
    # measure a WEBSITE. Two banks with identical queue times would score differently
    # here purely because one buries its hinnasto deeper — so calling the result
    # "asiakaspalvelu" would promise something the method cannot deliver. The category
    # is `pankit`, scored on fee and contact transparency, and the page says so.
    #
    # PANKKIRYHMÄT, ei yhtiöitä: Säästöpankki and POP Pankki are FEDERATIONS. The
    # Y-tunnus below is the group's central cooperative — NOT a deposit-taking bank.
    # Each member bank is its own company with its OWN hinnasto, which is itself the
    # finding: you cannot get one price list for "Säästöpankki". Labelled on the page.
    #
    # EXCLUDED (verified 17.7.2026): Handelsbanken (retail exited — henkilöasiakkaiden
    #   tili- ja maksupalvelut päättyivät 31.3.2025; retail sold to S-Pankki 1.12.2024,
    #   SME to OmaSp 1.9.2024; no consumer onboarding), Bank Norwegian (2717751-9 NOT
    #   FOUND in PRH; no käyttötili either), Svea (3237195-7 is real but sells only a
    #   säästötili + credit — no everyday account, so not a comparable retail bank; it
    #   is in `kulutusluotot` instead), Revolut + N26 (no Finnish entity in PRH,
    #   cross-border only, no Finnish-language service), Säästöpankkien Keskuspankki
    #   and Bonum Pankki (group central banks — no consumer customers, no public
    #   retail hinnasto).
    "pankit": [
        dict(slug="op", nimi="OP", domain="op.fi", y_tunnus="0242522-1",
             omistaja="OP Osuuskunta — noin 100 osuuspankkia, asiakasomisteinen",
             pankkityyppi="Osuuspankkiryhmä"),
        dict(slug="nordea", nimi="Nordea", domain="nordea.fi", y_tunnus="2858394-9",
             omistaja="Nordea Bank Abp — pörssiyhtiö, pääkonttori Helsingissä",
             pankkityyppi="Liikepankki"),
        dict(slug="danske", nimi="Danske Bank", domain="danskebank.fi", y_tunnus="1078693-2",
             omistaja="Danske Bank A/S (Tanska) — Suomen sivuliike",
             pankkityyppi="Ulkomaisen pankin sivuliike"),
        dict(slug="spankki", nimi="S-Pankki", domain="s-pankki.fi", y_tunnus="2557308-3",
             omistaja="S-ryhmä (SOK ja alueosuuskaupat) — osti Handelsbankenin Suomen "
                      "henkilöasiakkaat 1.12.2024",
             pankkityyppi="Liikepankki"),
        dict(slug="aktia", nimi="Aktia", domain="aktia.fi", y_tunnus="2181702-8",
             omistaja="Aktia Bank Abp — pörssiyhtiö, ei määräysvaltaista omistajaa",
             pankkityyppi="Liikepankki"),
        dict(slug="omasp", nimi="Oma Säästöpankki", domain="omasp.fi", y_tunnus="2231936-2",
             omistaja="Oma Säästöpankki Oyj — pörssiyhtiö; EI sama kuin Säästöpankkiryhmä",
             pankkityyppi="Liikepankki"),
        dict(slug="alandsbanken", nimi="Ålandsbanken", domain="alandsbanken.fi", y_tunnus="0145019-3",
             omistaja="Ålandsbanken Abp — pörssiyhtiö (Ahvenanmaa; konttorit myös mantereella)",
             pankkityyppi="Liikepankki"),
        dict(slug="saastopankki", nimi="Säästöpankki", domain="saastopankki.fi", y_tunnus="0117011-6",
             omistaja="Säästöpankkiliitto osk — keskusyhteisö, EI talletuspankki; "
                      "ryhmässä on itsenäisiä säästöpankkeja omilla Y-tunnuksillaan",
             pankkityyppi="Pankkiryhmä — ei yksi yhtiö"),
        dict(slug="poppankki", nimi="POP Pankki", domain="poppankki.fi", y_tunnus="1090961-3",
             omistaja="POP Pankkikeskus osk — keskusyhteisö, EI talletuspankki; "
                      "ryhmässä on itsenäisiä osuuspankkeja omilla Y-tunnuksillaan",
             pankkityyppi="Pankkiryhmä — ei yksi yhtiö"),
    ],
}

# ---------------------------------------------------------------------------
# The four insurance product lines reuse the SAME seven verified insurers as
# `vakuutukset`, but each is measured on its OWN product page (URLs HTTP-checked
# 17.7.2026, see targets.txt) — that is what makes them four categories and not
# four copies. A consumer shops these products separately, and the transparency
# answer genuinely differs per line: matkavakuutus tends to have a public price,
# kotivakuutus hides behind a calculator.
#
# NOTE — Pohjola Vakuutus: pohjola.fi 301-redirects into op.fi. OP sells its
# insurance on the bank's platform, so op.fi IS Pohjola's site and the domain is
# recorded as op.fi rather than pretending pohjola.fi is a live destination.
_INSURERS = {c["slug"]: c for c in COMPANIES["vakuutukset"]}


def _insurer(slug, **over):
    c = dict(_INSURERS[slug])
    c.update(over)
    return c


# POHJOLA VAKUUTUS EXCLUDED from all four product lines (17.7.2026) — and this is a
# measurement failure on OUR side, not a finding about OP. pohjola.fi redirects into
# op.fi, and op.fi serves its entire product content via JavaScript: curl with a real
# browser User-Agent gets HTTP 200 and 225 kB, but only ~900 characters of text — a
# login/consent shell. WebFetch is refused outright and the browser pane blocks the
# domain by policy. Lighthouse (real Chrome) CAN render it, so the digital pillar was
# measurable, but the transparency and AI pillars were not.
#
# The choice was: publish Pohjola scored on what our crawler could not see, or leave it
# out and say so. EXTRACTION_BRIEF is explicit that penalising a company for blocking a
# crawler rather than for what it shows humans is a measurement error, not a finding —
# so a score built from that would be exactly the falsifiable claim this project already
# had to retract once. It is left out and the omission is stated on each page.
#
# KNOWN DEFECT, flagged for Anton: the already-live `vakuutukset` category (measured
# 16.7.2026) DOES contain a Pohjola row whose extract has fetched_ok=null and records
# everything as "behind login". That looks like this same error, published. It is NOT
# silently rewritten here — the methodology page promises results are not changed
# retroactively — but it should be re-measured with a JS-capable fetch and re-dated.
for _line in ("autovakuutukset", "kotivakuutukset", "matkavakuutukset"):
    COMPANIES[_line] = [
        _insurer("if"), _insurer("lahitapiola"),
        _insurer("fennia"), _insurer("turva"), _insurer("pohjantahti"),
        _insurer("popvakuutus"),
    ]

# POP Vakuutus EXCLUDED from pet: verified 17.7.2026 that it sells no animal line at
# all — not on the product listing, and a site-restricted search for lemmikki-/koira-/
# kissa-/eläinvakuutus on popvakuutus.fi returns nothing. A real absence, not a gap.
# Agria ADDED: the category's specialist, PRH-verified Finnish branch. NB agria.fi is
# CAPTCHA-gated — per EXTRACTION_BRIEF a bot-blocked site must be scored "osittain",
# never "ei". Barkibu excluded: sells into Finland via a German branch, no Finnish
# registration. "Sneiku" and "Dogsdorf" excluded: no evidence either exists.
COMPANIES["lemmikkivakuutukset"] = [
    _insurer("if"), _insurer("lahitapiola"),
    _insurer("fennia"), _insurer("turva"), _insurer("pohjantahti"),
    dict(slug="agria", nimi="Agria", domain="agria.fi", y_tunnus="2744611-7",
         omistaja="Försäkringsaktiebolaget Agria (publ) — Länsförsäkringar-ryhmä (Ruotsi), "
                  "Suomen sivuliike rek. 5.2.2016"),
]

# SÄHKÖVERTAILUPALVELUT (verified 17.7.2026, 4 parallel research agents, every
# operator checked against PRH v3 where a Y-tunnus exists).
#
# First vertical of the Vertailupalvelut meta-group: this ranks the services that
# compare electricity contracts — the same move lainavertailu made on loan brokers.
#
# OWNERSHIP CATCH: Sähkövertailu.fi and VertaaEnsin ovat SAMA yhtiö — Effortia Oy
# (2261132-0), joka kertoo itse olevansa osa Alma Mediaa. Two "competing" brands,
# one owner — the Sambla pattern again. Disclosed in notes.
#
# Energiavirasto's sahkonhinta.fi is included deliberately: the regulator's own
# comparison is the neutral yardstick the commercial services get measured against.
# State agency → no Y-tunnus in YTJ; that is the correct value, not a gap.
#
# EXCLUDED — discontinued/not a comparison service (verified 17.7.2026):
#   Zmarta (own page: "Zmartan sähkövertailu ei ole tällä hetkellä toiminnassa",
#     page last updated 15.9.2023 — loans only now), Liukuri.fi (spot-price
#     visualizer, hobby project by a private developer, no kilpailutus),
#     Vertaa.fi (product price-comparison portal; electricity is a thin side
#     section of ~6 offers, not a kilpailutus service; bot wall on headless),
#     Liittymätarjoukset.fi (phone-plan site with a side sähkö table; operator is
#     a toiminimi that PRH v3 API cannot verify).
# EXCLUDED — anonymous affiliate shells (no legal identity anywhere on the site):
#   Sähkötarjouksia.fi (also still ran a Black Friday banner and promoted the dead
#     Väre brand in July 2026), Halpasahko.com (SEO article farm, no comparison
#     tool, Adtraction links straight to sellers), Vertaa-hintaa.fi (affiliate
#     listicle site, pseudonymous authors).
# EXCLUDED — white-label fronts: Kilpailuta-sahkosopimus.fi and
#   Sahkon-hintavertailu.fi both funnel to halvinsähkösopimus.fi's flow (same
#   hssprewidget campaign) — listing them separately would count one service thrice.
# EXCLUDED — unverifiable operator: Vertaa-kilpailuttajat.fi ranks comparison
#   sites partly by sponsorship ("järjestys perustuu sponsorointiin...") and its
#   claimed Y-tunnus 3419623-2 returns nothing from PRH — cannot be listed.
COMPANIES["sahkovertailupalvelut"] = [
    dict(slug="sahkovertailu", nimi="Sähkövertailu.fi", domain="sahkovertailu.fi",
         y_tunnus="2261132-0",
         omistaja="Effortia Oy — osa Alma Mediaa (yhtiön oma ilmoitus); sama omistaja kuin VertaaEnsin"),
    dict(slug="vertaaensin", nimi="VertaaEnsin (sähkö)", domain="vertaaensin.fi",
         y_tunnus="2261132-0",
         omistaja="Effortia Oy — osa Alma Mediaa (yhtiön oma ilmoitus); sama omistaja kuin Sähkövertailu.fi"),
    dict(slug="kilpailuttaja", nimi="Kilpailuttaja.fi", domain="kilpailuttaja.fi",
         y_tunnus="1811203-5",
         omistaja="Energy Brokers Finland Oy (per. 2003)"),
    dict(slug="valovirta", nimi="Valovirta", domain="valovirta.fi",
         y_tunnus="3358519-9",
         omistaja="EnCoHub Oy, Jyväskylä"),
    dict(slug="sahkon-kilpailutus", nimi="Sähkön-kilpailutus.fi", domain="sahkon-kilpailutus.fi",
         y_tunnus="2933035-3",
         omistaja="Comperion Oy (aik. DZR eCommerce Oy)"),
    dict(slug="sahkonhinta", nimi="Sahkonhinta.fi (Energiavirasto)", domain="sahkonhinta.fi",
         y_tunnus=None,
         omistaja="Energiavirasto — valtion viranomainen, sähkömarkkinoiden valvoja"),
    dict(slug="halvinsahkosopimus", nimi="Halvinsähkösopimus.fi",
         domain="xn--halvinshksopimus-1nb04a.fi",
         y_tunnus="3337062-2",
         omistaja="Optolead Oy"),
    dict(slug="sahkonkilpailutus-com", nimi="Sähkön-kilpailutus.com",
         domain="xn--shkn-kilpailutus-vnb04a.com",
         y_tunnus="2658911-6",
         omistaja="WebCube Oy, Alavus (myös VertaaLainaa.fi ja VertaaLiittymät.fi)"),
    dict(slug="valitseparas", nimi="ValitseParas.fi", domain="valitseparas.fi",
         y_tunnus="3251768-8",
         omistaja="Valo Sales Oy (rek. 2021)"),
]

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
