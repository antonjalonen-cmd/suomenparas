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

# APTEEKKIEN-VERKKOKAUPAT (verified 24.7.2026)
#
# Finnish online pharmacies licensed by Fimea (Lääkealan turvallisuus- ja
# kehittämiskeskus). All seven appear on Fimea's legal online pharmacy register.
# Finnish pharmacy licences are issued to individual pharmacists (proviisorin
# apteekkilupa), not always to a limited company — so some Y-tunnukset belong to the
# e-commerce operating company (Oy), others are listed as None because the licensee
# is a natural person whose personal Y-tunnus is not published.
#
# EXCLUDED: apteekkituotteet.fi (redirects to single Länsi-Keskuksen Apteekki
# local page — not a national service), DocMorris (EU crossborder, no Finnish Oy).
# pilleriainen.fi: domain did not respond at measurement time (curl no response).
COMPANIES["apteekkien-verkkokaupat"] = [
    dict(slug="yliopiston-apteekki", nimi="Yliopiston Apteekki", domain="yliopistonapteekki.fi",
         y_tunnus="1846816-2",
         omistaja="Yliopiston Apteekki Oy — Suomen suurin apteekkiketju, yli 30 toimipistettä"),
    dict(slug="olo-apteekki", nimi="Olo-apteekki", domain="oloapteekki.fi",
         y_tunnus="2862688-1",
         omistaja="Olo-apteekki Oy (ent. Yleisavain Oy) — Suomen nopeimmin kasvava verkkoapteekki, EAEP-jäsen"),
    dict(slug="apteekki-360", nimi="Apteekki 360", domain="apteekki360.fi",
         y_tunnus="2279092-0",
         omistaja="Vaidia Oy — Hakaniemen Ympyrätalo, Helsinki; automaattinen hinnanvertailu"),
    dict(slug="nettiterveysapteekki", nimi="Nettiterveysapteekki", domain="nettiterveysapteekki.fi",
         y_tunnus=None,
         omistaja="Hansa Apteekki, Oulu (Limingantullin Prisma) — apteekkilupa Fimea, valtakunnallinen toimitus"),
    dict(slug="bonusapteekki", nimi="Bonusapteekki", domain="bonusapteekki.fi",
         y_tunnus=None,
         omistaja="Bonusapteekki, Ylöjärvi (Kauppakeskus Elo); ei-lääkkeelliset: Balogi Oy (3334061-8)"),
    dict(slug="nettiapteekki", nimi="Nettiapteekki", domain="nettiapteekki.fi",
         y_tunnus=None,
         omistaja="Seitsemän Veljeksen Apteekki — OIVA-hyväksytty, valtakunnallinen toimitus"),
    dict(slug="verkkoapteekki", nimi="Verkkoapteekki", domain="verkkoapteekki.fi",
         y_tunnus=None,
         omistaja="Järvenpään Lähiapteekki — laillinen verkkoapteekki, toimitus Posti/PostNord"),
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


# ---------------------------------------------------------------------------
# BATCH 3 (verified 18.7.2026, full verification notes in pipeline/verify_batch3/*.md)
#
# AUTOKATSASTUS — only 4 genuine national chains exist; that is the honest set, not
# padding (rule: a smaller correct set beats a padded one). EXCLUDED: Katsastus Plus
# (= Plus Katsastus, wrong name), "Yksityiset katsastusasemat" (not a company),
# Suomen Autokatsastus (folded into A-Katsastus), Katsastajasi + Go-Katsastus +
# Q-Katsastus (regional; Q sold to TÜV SÜD 2/2026). OWNERSHIP: A-Katsastus bought
# K1 Katsastajat 12/2022 (~40 % combined share, flagged by Autoliitto) — disclosed.
COMPANIES["autokatsastus"] = [
    dict(slug="a-katsastus", nimi="A-Katsastus", domain="a-katsastus.fi", y_tunnus="1959705-4",
         omistaja="Tradeka — suomalainen osuuskuntataustainen konserni; omistaa myös K1 Katsastajat"),
    dict(slug="k1-katsastajat", nimi="K1 Katsastajat", domain="k1katsastus.fi", y_tunnus="2046583-3",
         omistaja="A-Katsastus-konsernin tytäryhtiö 12/2022 alkaen — sama konserni kuin A-Katsastus"),
    dict(slug="plus-katsastus", nimi="Plus Katsastus", domain="plus.fi", y_tunnus="2307508-0",
         omistaja="Suomalaisten yrittäjien omistama, riippumaton A-Katsastus-konsernista"),
    dict(slug="dekra-katsastus", nimi="DEKRA Katsastus", domain="dekra-katsastus.fi", y_tunnus="2467455-2",
         omistaja="Saksalainen DEKRA-konserni"),
]

# AUTOVUOKRAAMOT — EXCLUDED: Budget (SAME company as Avis: Helkama Rent Oy, one
# Y-tunnus — would double-count one competitor as two). Scandia Rent quietly
# rebranded MABI Mobility (Hedin Mobility Group) but still trades at scandiarent.fi.
# hertz.fi and avis.fi are JS-rendered — extraction MUST use fetch_page.py --js.
COMPANIES["autovuokraamot"] = [
    dict(slug="hertz", nimi="Hertz", domain="hertz.fi", y_tunnus="0744711-2",
         omistaja="First Rent A Car Finland Oy Ab — Suomen Hertz-lisenssinhaltija"),
    dict(slug="avis", nimi="Avis", domain="avis.fi", y_tunnus="2346469-2",
         omistaja="Helkama Rent Oy — sama yhtiö operoi myös Budget-brändiä Suomessa"),
    dict(slug="sixt", nimi="Sixt", domain="sixt.fi", y_tunnus="2275518-0",
         omistaja="Transporent Oy (Veho-konserni) — Suomen Sixt-lisenssinhaltija"),
    dict(slug="europcar", nimi="Europcar", domain="europcar.fi", y_tunnus="0109269-9",
         omistaja="Interrent Oy — osa Europcar Mobility Groupia"),
    dict(slug="scandia-rent", nimi="Scandia Rent", domain="scandiarent.fi", y_tunnus="2509794-5",
         omistaja="Mabi Mobility Oy — ruotsalainen Hedin Mobility Group; brändi vaihtumassa MABI Mobilityksi"),
    # domain greenmotion.com, not .fi: greenmotion.fi redirects to greenmotion.com/fi —
    # the .com site IS where a Finnish visitor lands (same decision as pohjola.fi→op.fi).
    dict(slug="green-motion", nimi="Green Motion", domain="greenmotion.com", y_tunnus="1837195-0",
         omistaja="Green Motion International -franchise, suomalaiset franchise-yrittäjät"),
]

# OPTIKOT — EXCLUDED: Nissen (SAME company as Instrumentarium: Instru Optiikka Oy /
# EssilorLuxottica). Silmäasema is MID-ACQUISITION: Terveystalo signed 8.6.2026,
# not closed — disclosed on-page, re-check every run.
COMPANIES["optikot"] = [
    dict(slug="specsavers", nimi="Specsavers", domain="specsavers.fi", y_tunnus="2006084-4",
         omistaja="Kansainvälinen Specsavers-franchisejärjestelmä"),
    dict(slug="instrumentarium", nimi="Instrumentarium", domain="instru.fi", y_tunnus="1789727-2",
         omistaja="Instru Optiikka Oy / EssilorLuxottica — sama yhtiö omistaa myös Nissen-brändin"),
    dict(slug="silmaasema", nimi="Silmäasema", domain="silmaasema.fi", y_tunnus="2627773-7",
         omistaja="Coronaria; Terveystalo ilmoitti ostavansa 8.6.2026 — kauppa ei vielä toteutunut"),
    dict(slug="fenno-optiikka", nimi="Fenno Optiikka", domain="fennooptiikka.fi", y_tunnus="2205389-1",
         omistaja="Suomalainen franchise-yrittäjävetoinen ketju"),
    dict(slug="synsam", nimi="Synsam", domain="synsam.fi", y_tunnus="2446347-2",
         omistaja="Ruotsalainen Synsam Group — pörssiyhtiö"),
]

# YKSITYISLÄÄKÄRIT — 4 genuine national chains; Lysna (rekisteröity 9/2024, yksi
# kaupunki) EXCLUDED as not national — a startup padded in would be indefensible.
# Diacor is DEAD (merged into Terveystalo 2016; diacor.fi now serves an unrelated
# diet site). Coronaria = eri segmentti, Lähilääkärit = pääkaupunkiseutu.
COMPANIES["yksityislaakarit"] = [
    dict(slug="mehilainen", nimi="Mehiläinen", domain="mehilainen.fi", y_tunnus="1927556-5",
         omistaja="Mehiläinen Oy — pääomasijoittajaomisteinen konserni"),
    dict(slug="terveystalo", nimi="Terveystalo", domain="terveystalo.com", y_tunnus="2575979-3",
         omistaja="Terveystalo Oyj — pörssiyhtiö (Nasdaq Helsinki)"),
    dict(slug="pihlajalinna", nimi="Pihlajalinna", domain="pihlajalinna.fi", y_tunnus="2617455-1",
         omistaja="Pihlajalinna Oyj — pörssiyhtiö (Nasdaq Helsinki)"),
    dict(slug="aava", nimi="Aava", domain="aava.fi", y_tunnus="2311119-2",
         omistaja="Aava ja Pikkujätti Oy (nimi 3.6.2025 asti Lääkärikeskus Aava Oy) — suomalainen perheyritys"),
]

# KUNTOSALIT — OWNERSHIP: LadyLine ja EasyFit ovat saman franchisoijan (Ab LL
# International Oy 1790020-8) kaksi brändiä — disclosed on-page (Effortia-oppi).
# EXCLUDED: GOGO (Tampere-paikallinen), "Motion" (ei ole olemassa — domain kuuluu
# elokuvayhtiölle), SATS erillisenä (Suomessa brändi on Elixia, sama yhtiö).
COMPANIES["kuntosalit"] = [
    dict(slug="elixia", nimi="Elixia", domain="elixia.fi", y_tunnus="0459885-5",
         omistaja="SATS Finland Oy / SATS ASA — Oslon pörssissä noteerattu konserni"),
    dict(slug="fressi", nimi="Fressi", domain="fressi.fi", y_tunnus="2538910-4",
         omistaja="Fysioline Fressi Oy — suomalainen, Tampere"),
    dict(slug="ladyline", nimi="LadyLine", domain="ladyline.fi", y_tunnus="1790020-8",
         omistaja="Ab LL International Oy — sama franchisoija kuin EasyFitillä"),
    dict(slug="easyfit", nimi="EasyFit", domain="easyfit.fi", y_tunnus="1790020-8",
         omistaja="Ab LL International Oy (franchisoija, sama kuin LadyLine); yksittäiset salit itsenäisiä yrittäjiä"),
    dict(slug="fitness24seven", nimi="Fitness24Seven", domain="fi.fitness24seven.com", y_tunnus="2402161-5",
         omistaja="Fitness24Seven Oy — ruotsalainen kansainvälinen ketju"),
    dict(slug="liikku", nimi="Kuntokeskus Liikku", domain="liikku.fi", y_tunnus="2784989-9",
         omistaja="Kuntokeskus Liikku Oy — suomalainen, Oulu"),
]

# KIINTEISTÖNVÄLITTÄJÄT — EXCLUDED: SKV (sulautui Huoneistokeskukseen — skv.fi
# ohjaa sinne), Roof Group/Aninkainen/Solid House (alueellisia). OP Koti on ~19
# alueellisen "OP Koti X Oy LKV" -yhtiön federaatio ilman yhtä Y-tunnusta — sama
# rakenne kuin Säästöpankki/POP pankit-kategoriassa; y_tunnus=None, labelled.
COMPANIES["kiinteistonvalittajat"] = [
    dict(slug="kiinteistomaailma", nimi="Kiinteistömaailma", domain="kiinteistomaailma.fi", y_tunnus="0804835-9",
         omistaja="Kiinteistömaailma Oy — franchise-ketju"),
    dict(slug="huoneistokeskus", nimi="Huoneistokeskus", domain="huoneistokeskus.fi", y_tunnus="1831315-2",
         omistaja="Realia/Retta-konserni — sisältää entisen SKV:n (sulautui 2020)"),
    dict(slug="opkoti", nimi="OP Koti", domain="op-koti.fi", y_tunnus=None,
         omistaja="OP Ryhmä — noin 19 alueellista OP Koti Oy LKV -yhtiötä, ei yhtä Y-tunnusta"),
    dict(slug="remax", nimi="RE/MAX", domain="remax.fi", y_tunnus="2019179-9",
         omistaja="REF Real Estate Franchises Oy — kansainvälisen RE/MAX-ketjun master-franchisoija; toimistot itsenäisiä"),
    dict(slug="habita", nimi="Habita", domain="habita.com", y_tunnus="0980183-2",
         omistaja="Habita Finland Oy; kaupunkitoimistot erillisiä osakeyhtiöitä saman brändin alla"),
    dict(slug="bolkv", nimi="Bo LKV", domain="bo.fi", y_tunnus="2796763-3",
         omistaja="Bo LKV Oy — yksi yhtiö, kaupunkitoimistot aputoiminimiä"),
]

# LAKIFIRMAT (verified 21.7.2026, pipeline/verify_batch4/lakifirmat.md) — consumer legal
# services with national reach: digital document services + multi-office firms.
# EXCLUDED: Lexly (company LAKKANNUT 22.12.2025 per PRH — dead brand caught before
# publishing), Docue/Sopimustieto (same company, pure B2B now), Fondia (B2B only),
# Facta (2 cities), Kontturi & Co (regional, 3 offices), Perunkirja.fi (funeral-home
# side product). NOTE: "asianajotoimisto" is a regulated title (Asianajajaliitto
# supervision) — juristin pätevyys is a scored transparency criterion here.
COMPANIES["lakifirmat"] = [
    dict(slug="aatos", nimi="Aatos", domain="aatos.app", y_tunnus="2901500-3",
         omistaja="Aatos Legal Technology Oy — itsenäinen suomalainen legal tech -yhtiö"),
    dict(slug="lakitie", nimi="Lakitie", domain="lakitie.com", y_tunnus="3614565-8",
         omistaja="Lakitie Oy — nuori yhtiö (Oy rekisteröity 4/2026; palvelu toiminut vuodesta 2023)"),
    dict(slug="diy-lakipalvelu", nimi="DIY Lakipalvelu", domain="diylakipalvelu.fi", y_tunnus="2835849-3",
         omistaja="DIY Lakipalvelu Oy — henkilöomisteinen, sisällöstä vastaa varatuomari"),
    dict(slug="lindblad", nimi="Asianajotoimisto Lindblad & Co", domain="lindblad.fi", y_tunnus="1608041-2",
         omistaja="Itsenäinen suomalainen asianajotoimisto — Asianajajaliiton valvoma"),
    dict(slug="heikkila-co", nimi="Lakiasiaintoimisto Heikkilä & Co", domain="heikkilaco.fi", y_tunnus="1843393-9",
         omistaja="Itsenäinen; vuoteen 2024 asti asianajotoimisto, nykyään lakiasiaintoimisto"),
    dict(slug="minilex", nimi="Minilex", domain="minilex.fi", y_tunnus="2411251-7",
         omistaja="Minilex Oy — itsenäinen; lakipuhelin + juristiverkosto"),
    # Added 21.7.2026 by owner request. International network's Finnish member firm;
    # serves mainly businesses and private wealth — no public prices, which the
    # transparency pillar scores as found.
    dict(slug="eversheds", nimi="Eversheds Sutherland", domain="eversheds-sutherland.com", y_tunnus="2556202-6",
         omistaja="Eversheds Asianajotoimisto Oy — kansainvälisen Eversheds Sutherland -verkoston itsenäinen suomalainen jäsen"),
]

# PAKOHUONEET (verified 21.7.2026, pipeline/verify_batch4/pakohuoneet.md) — the industry
# is STRUCTURALLY LOCAL: only 3 genuinely multi-city chains exist in Finland, plus two
# two-city operators included with their reach labelled. Disclosed on-page.
# OWNERSHIP: Truescape and Mysteeri are the SAME company (Truescape Oy, one Y-tunnus) —
# measured as one row. EXCLUDED: Room Escape Finland (KONKURSSI 13.2.2026), Claustrophobia
# (Tallinn only), Pakotarinat (sold both sites — Espoo→Truescape, Joensuu→Huonepakopeli),
# and 8 single-city operators. Truescape's Seinäjoki site is "toistaiseksi suljettu" —
# not counted in its 9 cities.
COMPANIES["pakohuoneet"] = [
    dict(slug="truescape", nimi="Truescape", domain="truescape.fi", y_tunnus="3016295-9",
         omistaja="Truescape Oy — omistaa myös Mysteeri-brändin (sama yhtiö); yhteensä 9 kaupunkia"),
    dict(slug="labyrinth-games", nimi="Labyrinth Games", domain="lgames.fi", y_tunnus="2659780-2",
         omistaja="Labyrinth Games Room Escape Oy — perustajaomisteinen, 4 kaupunkia"),
    dict(slug="wayout", nimi="WayOut", domain="wayout.fi", y_tunnus="2781348-2",
         omistaja="WayOut Oy — perustajaomisteinen, 3 kaupunkia"),
    dict(slug="huonepakopeli", nimi="Huonepakopeli", domain="huonepakopeli.fi", y_tunnus="2996282-8",
         omistaja="MooseFabric Oy — 2 kaupunkia (Joensuu, Kuopio)"),
    dict(slug="the-great-escape", nimi="The Great Escape", domain="thegreatescape.fi", y_tunnus="2978448-6",
         omistaja="Gr8 Escape Oy — 2 paikkakuntaa (Kajaani, Vuokatti)"),
    # Added 21.7.2026 by owner request. SINGLE-CITY operator (Helsinki/Kamppi) — the
    # category is otherwise multi-city; its coverage is labelled on the row and the
    # category note was reworded so the published claim stays true.
    dict(slug="amazed", nimi="Amazed", domain="amazed.fi", y_tunnus="2716466-2",
         omistaja="Amazed Oy — 1 kaupunki (Helsinki)"),
]

# HAMMASLÄÄKÄRIT (verified 21.7.2026, pipeline/verify_batch4/hammaslaakarit.md).
# Oral is NOT Mehiläinen (Colosseum Dental Group / Jacobs Holding AG — the assumed
# link was false). PENDING DEAL: Terveystalo signed 23.12.2025 to buy Hohde Group
# (88 M€), KKV review pending at measurement time — if it closes, Terveystalo owns
# 2/6 brands; disclosed on-page, re-check every run. Cor Group owns Coronaria AND a
# stake in Silmäasema (optikot) — same parent investor across two categories.
# mehilainen.fi is a Next.js shell — extraction MUST use --js.
COMPANIES["hammaslaakarit"] = [
    dict(slug="oral", nimi="Oral Hammaslääkärit", domain="oral.fi", y_tunnus="2863321-3",
         omistaja="Colosseum Dental Group / Jacobs Holding AG (Sveitsi) — EI Mehiläinen"),
    dict(slug="mehilainen", nimi="Hammas Mehiläinen", domain="mehilainen.fi", y_tunnus="1927556-5",
         omistaja="Mehiläinen Oy — hammashoito on konsernin oma palvelulinja"),
    dict(slug="terveystalo", nimi="Suun Terveystalo", domain="terveystalo.com", y_tunnus="2575979-3",
         omistaja="Terveystalo Oyj — pörssiyhtiö; ostamassa Hammas Hohdetta (KKV-käsittely kesken)"),
    dict(slug="plusterveys", nimi="PlusTerveys", domain="plusterveys.fi", y_tunnus="3265145-7",
         omistaja="PlusTerveys Ryhmä Oy — ammattilaisomisteinen"),
    dict(slug="hammashohde", nimi="Hammas Hohde", domain="hammashohde.fi", y_tunnus="2339589-3",
         omistaja="Sentica Partners (~60 %); Terveystalo sopi ostosta 23.12.2025 — kauppa ei vielä toteutunut"),
    dict(slug="coronaria", nimi="Coronaria Hammasklinikka", domain="coronaria.fi", y_tunnus="2207193-4",
         omistaja="Coronaria Oy / Cor Group — samalla emosijoittajalla omistusta myös Silmäasemassa"),
]

# RENGASLIIKKEET (verified 21.7.2026, pipeline/verify_batch4/rengasliikkeet.md).
# OWNERSHIP CONCENTRATION: 4 of 6 chains are tyre-manufacturer-owned (Vianor=Nokian
# Renkaat, Euromaster=Michelin, BestDrive=Continental, First Stop=Bridgestone) — a
# manufacturer-owned chain has an incentive to recommend its own brand; disclosed.
# DEAD BRAND: Rengasmaailma → Rengasmarket → BestDrive (two rebrands) — replaced by
# BestDrive. Teboil excluded (no chain-wide tyre service).
COMPANIES["rengasliikkeet"] = [
    dict(slug="vianor", nimi="Vianor", domain="vianor.fi", y_tunnus="1463013-4",
         omistaja="Nokian Renkaat — valmistajan oma ketju"),
    dict(slug="euromaster", nimi="Euromaster", domain="euromaster.fi", y_tunnus="0711042-1",
         omistaja="Michelin — valmistajan oma ketju"),
    dict(slug="bestdrive", nimi="BestDrive", domain="bestdrive.fi", y_tunnus="1095378-8",
         omistaja="Continental-tuettu ketju (ent. Rengasmaailma/Rengasmarket)"),
    dict(slug="motonet", nimi="Motonet Rengaspalvelut", domain="motonet.fi", y_tunnus="0699457-9",
         omistaja="Motonet Oy — suomalainen perheyritys (Broman Group)"),
    dict(slug="rengascenter", nimi="RengasCenter", domain="rengascenter.fi", y_tunnus="0782719-0",
         omistaja="Yrittäjäomisteinen ketju (60+ liikettä) — ei valmistajan omistama"),
    dict(slug="firststop", nimi="First Stop", domain="firststop.fi", y_tunnus="1806488-9",
         omistaja="Bridgestone Europe NV/SA, Suomen sivuliike — valmistajan oma ketju"),
]

# MUUTTOPALVELUT (verified 21.7.2026, pipeline/verify_batch4/muuttopalvelut.md) — only 4
# genuine national operators; the sector is mostly local family movers (disclosed, same
# precedent as autokatsastus). DEAD CATCHES: Muuttopalvelu.com (MLP Moving Oy lakannut
# 3.12.2024, domain still advertises), Grundell (renamed Martela Palvelut 2.6.2026,
# B2B office relocation now, grundell.fi dead).
COMPANIES["muuttopalvelut"] = [
    dict(slug="niemi-palvelut", nimi="Niemi Palvelut", domain="niemi.fi", y_tunnus="1944860-6",
         omistaja="Niemi Palvelut Oy — itsenäinen suomalainen yhtiö"),
    dict(slug="muuttohaukat", nimi="Muuttohaukat", domain="muuttohaukat.com", y_tunnus="0887272-7",
         omistaja="Muuttohaukat Oy — itsenäinen"),
    dict(slug="suomen-muuttofirma", nimi="Suomen Muuttofirma", domain="muuttofirma.fi", y_tunnus="2292440-7",
         omistaja="Suomen Muuttofirma Oy — itsenäinen"),
    dict(slug="victor-ek", nimi="Victor Ek", domain="victorek.fi", y_tunnus="0215408-9",
         omistaja="Oy Victor Ek Ab — perheomisteinen vuodesta 1885"),
]

# SIIVOUSPALVELUT (verified 21.7.2026) — CONSUMER home cleaning only. SOL, RTK, ISS ja
# L&T EXCLUDED: none has a consumer home-cleaning product (verified from each company's
# own service pages, not search results). Onni kotisiivous is a Med Group Oy trade name
# (care-services group) — labelled.
COMPANIES["siivouspalvelut"] = [
    dict(slug="freska", nimi="Freska", domain="freska.fi", y_tunnus="3246808-9",
         omistaja="Freska Finland Oy — toimii myös Ruotsissa ja Norjassa"),
    dict(slug="kotirinki", nimi="Kotirinki", domain="kotirinki.fi", y_tunnus="1784293-3",
         omistaja="Kotirinki Oy — franchise-malli, paikalliset yrittäjät"),
    dict(slug="keradur", nimi="Keradur", domain="keradur.fi", y_tunnus="2315098-4",
         omistaja="Keradur Oy — itsenäinen"),
    dict(slug="onni-kotisiivous", nimi="Onni kotisiivous", domain="onnion.fi", y_tunnus="2080120-0",
         omistaja="Med Group Oy — hoivapalvelukonserni; kotisiivous on yksi ONNI-aputoiminimistä"),
    dict(slug="koti-puhtaaksi", nimi="Koti Puhtaaksi", domain="kotipuhtaaksi.fi", y_tunnus="2395527-2",
         omistaja="Sahera Koti Puhtaaksi Oy — itsenäinen, perustettu 2011"),
]

# AUTOKOULUT (verified 21.7.2026) — the sector HAS consolidated into national chains
# (contrary to the queue's caution): CAP and Epic are PE-backed roll-ups with 100+
# locations. 4 confirmed (autokatsastus precedent, disclosed).
COMPANIES["autokoulut"] = [
    dict(slug="cap-autokoulu", nimi="CAP-Autokoulu", domain="cap.fi", y_tunnus="0841716-9",
         omistaja="CAP-Group Oy — osin sopimusyrittäjämalli"),
    dict(slug="epic-autokoulu", nimi="Epic Autokoulu", domain="epicautokoulu.fi", y_tunnus="2551291-8",
         omistaja="Korona Invest -pääomasijoittaja; konserniin kuuluu myös Autokoulu Safiiri"),
    dict(slug="antin-autokoulu", nimi="Antin Autokoulu", domain="antinautokoulu.fi", y_tunnus="2763674-6",
         omistaja="Antin Autokoulu Oy — itsenäinen, kotipaikka Raahe"),
    dict(slug="ajokorttiverkosta", nimi="Ajokortti Verkosta", domain="ajokorttiverkosta.fi", y_tunnus="1440949-9",
         omistaja="RG Driving Consulting Oy — verkkopainotteinen autokoulu"),
]

# ---------------------------------------------------------------------------
# BATCH 5 (verified 21.7.2026, pipeline/verify_batch5/*.md)
#
# PILVITALLENNUSPALVELUT — global services, vpn-palvelut convention (y_tunnus=None,
# owner disclosure is the criterion). Proton Drive = same Proton AG as published
# Proton VPN — disclosed. Suomenkielisyys on oma mittari (Dropbox/pCloud/Internxt ei).
COMPANIES["pilvitallennuspalvelut"] = [
    dict(slug="googleone", nimi="Google One", domain="one.google.com", y_tunnus=None,
         omistaja="Alphabet Inc. / Google (Yhdysvallat) — EU-laskutus Irlannin yksikön kautta"),
    dict(slug="icloud", nimi="iCloud+", domain="apple.com", y_tunnus=None,
         omistaja="Apple Inc. (Yhdysvallat) — EU-laskutus Apple Distribution International (Irlanti)"),
    dict(slug="onedrive", nimi="Microsoft OneDrive", domain="microsoft.com", y_tunnus=None,
         omistaja="Microsoft Corporation (Yhdysvallat) — EU-laskutus Microsoft Ireland Operations"),
    dict(slug="dropbox", nimi="Dropbox", domain="dropbox.com", y_tunnus=None,
         omistaja="Dropbox, Inc. — pörssiyhtiö (Nasdaq); ei suomenkielistä sivustoa"),
    dict(slug="protondrive", nimi="Proton Drive", domain="proton.me", y_tunnus=None,
         omistaja="Proton AG (Sveitsi) — sama yhtiö kuin Proton VPN ja Proton Pass"),
    dict(slug="mega", nimi="MEGA", domain="mega.io", y_tunnus=None,
         omistaja="MEGA Limited (Uusi-Seelanti)"),
    dict(slug="pcloud", nimi="pCloud", domain="pcloud.com", y_tunnus=None,
         omistaja="pCloud AG (Sveitsi) — perustajaomisteinen; ei suomenkielistä sivustoa"),
    dict(slug="internxt", nimi="Internxt", domain="internxt.com", y_tunnus=None,
         omistaja="Internxt S.L. (Espanja) — VC-rahoitteinen; ei suomenkielistä sivustoa"),
]

# SALASANANHALLINTAPALVELUT — OWNERSHIP: NordPass = Nord Security (sama kuin NordVPN),
# Proton Pass = Proton AG (sama kuin Proton VPN + Drive) — molemmat disclosed.
# KeePass excluded (open source -projekti, ei yhtiötä eikä hinnoittelua).
COMPANIES["salasananhallintapalvelut"] = [
    dict(slug="1password", nimi="1Password", domain="1password.com", y_tunnus=None,
         omistaja="1Password Inc. (Kanada)"),
    dict(slug="bitwarden", nimi="Bitwarden", domain="bitwarden.com", y_tunnus=None,
         omistaja="Bitwarden Inc. (Yhdysvallat) — avoin lähdekoodi, pääomasijoittajarahoitteinen"),
    dict(slug="dashlane", nimi="Dashlane", domain="dashlane.com", y_tunnus=None,
         omistaja="Dashlane SAS/Inc. (Ranska/Yhdysvallat)"),
    dict(slug="nordpass", nimi="NordPass", domain="nordpass.com", y_tunnus=None,
         omistaja="Nord Security (Liettua) — sama konserni kuin NordVPN"),
    dict(slug="lastpass", nimi="LastPass", domain="lastpass.com", y_tunnus=None,
         omistaja="LastPass US LP — Francisco Partners & Elliott Management (itsenäistyi GoTo:sta 2024)"),
    dict(slug="keeper", nimi="Keeper", domain="keepersecurity.com", y_tunnus=None,
         omistaja="Keeper Security, Inc. (Yhdysvallat)"),
    dict(slug="proton-pass", nimi="Proton Pass", domain="proton.me", y_tunnus=None,
         omistaja="Proton AG (Sveitsi) — sama yhtiö kuin Proton VPN ja Proton Drive"),
]

# AUTOKORJAAMOT — ketjut ovat varaosatukkureiden/valmistajien konsepteja, joissa
# yksittäiset korjaamot ovat itsenäisiä yrittäjiä; ketjuyhtiö kirjattu omistajaksi.
# Motonet ja Euromaster esiintyvät myös rengasliikkeet-kategoriassa ERI sivuilla
# mitattuna — disclosed. EXCLUDED: Bosch Car Service (löyhä verkosto ilman
# vastuuyhtiötä), Mekonomen (sama MEKO kuin Fixus), Autoklinikka (kolarikorjaus, 3 kpl).
COMPANIES["autokorjaamot"] = [
    dict(slug="autoasi", nimi="Autoasi", domain="autoasi.fi", y_tunnus="2042810-0",
         omistaja="Örum Oy Ab — ketjukonsepti; korjaamot itsenäisiä yrittäjiä"),
    dict(slug="ad-finland", nimi="AD Autohuolto", domain="ad-finland.com", y_tunnus="0554943-0",
         omistaja="AD FIN Oy — osa AD International -yhteenliittymää; korjaamot itsenäisiä"),
    dict(slug="fixus", nimi="Fixus", domain="fixus.fi", y_tunnus="0110111-0",
         omistaja="MEKO Finland Oy (ent. Koivunen) — Ruotsin pörssin MEKO-konserni"),
    dict(slug="autofit", nimi="Autofit", domain="autofit.fi", y_tunnus="1630177-2",
         omistaja="Atoy Automotive Finland Oy — perheyritys; korjaamot Autofit-yrittäjiä"),
    dict(slug="motonet", nimi="Motonet-korjaamot", domain="motonet.fi", y_tunnus="0699457-9",
         omistaja="Motonet Oy (Broman Group) — sama yhtiö myös rengasliikkeet-kategoriassa, eri palvelu"),
    dict(slug="euromaster", nimi="Euromaster Autohuolto", domain="euromaster.fi", y_tunnus="0711042-1",
         omistaja="Michelin — sama yhtiö myös rengasliikkeet-kategoriassa, eri palvelu"),
]

# SUORATOISTOPALVELUT (verified 21.7.2026, pipeline/verify_batch5/suoratoistopalvelut.md)
# Global services, vpn convention. MTV Oy moved Telia -> Schibsted 1.7.2025. HBO Max
# kept its name in FI; Apple dropped the "+" from Apple TV.
COMPANIES["suoratoistopalvelut"] = [
    dict(slug="netflix", nimi="Netflix", domain="netflix.com", y_tunnus=None,
         omistaja="Netflix International B.V. (Alankomaat) / Netflix, Inc."),
    dict(slug="disneyplus", nimi="Disney+", domain="disneyplus.com", y_tunnus=None,
         omistaja="The Walt Disney Company (Yhdysvallat)"),
    dict(slug="hbomax", nimi="HBO Max", domain="hbomax.com", y_tunnus=None,
         omistaja="Warner Bros. Discovery, Inc. (Yhdysvallat)"),
    dict(slug="viaplay", nimi="Viaplay", domain="viaplay.fi", y_tunnus=None,
         omistaja="Viaplay Group AB (Ruotsi) — Canal+/PPF suurimpina omistajina"),
    dict(slug="ruutuplus", nimi="Ruutu+", domain="ruutu.fi", y_tunnus="1515901-4",
         omistaja="Sanoma Media Finland Oy / Sanoma Oyj"),
    dict(slug="mtvkatsomo", nimi="MTV Katsomo+", domain="mtv.fi", y_tunnus="1093944-1",
         omistaja="MTV Oy — siirtyi Schibstedin (Norja) omistukseen 1.7.2025 (aiemmin Telia)"),
    dict(slug="primevideo", nimi="Prime Video", domain="primevideo.com", y_tunnus=None,
         omistaja="Amazon.com, Inc. (Yhdysvallat)"),
    dict(slug="appletv", nimi="Apple TV", domain="tv.apple.com", y_tunnus=None,
         omistaja="Apple Inc. (Yhdysvallat) — palvelu tunnettiin aiemmin nimellä Apple TV+"),
    dict(slug="skyshowtime", nimi="SkyShowtime", domain="skyshowtime.com", y_tunnus=None,
         omistaja="Comcast (Sky) ja Paramount Global 50/50 -yhteisyritys"),
]

# VIRUSTORJUNTAOHJELMAT (verified 21.7.2026) — OWNERSHIP: Gen Digital owns Norton,
# Avast AND AVG (3/8 rows) — disclosed. McAfee EXCLUDED: site serves HTTP 403 to every
# fetch path incl. rendering browsers; bot-protection is not bypassed, so it cannot be
# measured (documented, not a finding about McAfee's quality). Kaspersky still sells in
# Finland (no EU consumer ban as of measurement).
COMPANIES["virustorjuntaohjelmat"] = [
    dict(slug="fsecure", nimi="F-Secure", domain="f-secure.com", y_tunnus="3269349-7",
         omistaja="F-Secure Oyj — suomalainen pörssiyhtiö (sama yhtiö kuin F-Secure VPN vpn-listalla)"),
    dict(slug="norton", nimi="Norton", domain="norton.com", y_tunnus=None,
         omistaja="Gen Digital Inc. (Yhdysvallat) — omistaa myös Avastin ja AVG:n"),
    dict(slug="bitdefender", nimi="Bitdefender", domain="bitdefender.com", y_tunnus=None,
         omistaja="Bitdefender (Romania) — yksityisomisteinen"),
    dict(slug="eset", nimi="ESET", domain="eset.com", y_tunnus=None,
         omistaja="ESET, spol. s r.o. (Slovakia)"),
    dict(slug="avast", nimi="Avast", domain="avast.com", y_tunnus=None,
         omistaja="Gen Digital Inc. — sama omistaja kuin Norton ja AVG"),
    dict(slug="avg", nimi="AVG", domain="avg.com", y_tunnus=None,
         omistaja="Gen Digital Inc. — sama omistaja kuin Norton ja Avast; ei suomenkielistä sivustoa"),
    dict(slug="kaspersky", nimi="Kaspersky", domain="kaspersky.fi", y_tunnus=None,
         omistaja="Kaspersky Lab — venäläistaustainen, perustajan ja johdon omistuksessa"),
    dict(slug="totalav", nimi="TotalAV", domain="totalav.com", y_tunnus=None,
         omistaja="Total Security Limited (Iso-Britannia) / Total Security US LLC"),
]


# HAUTAUSTOIMISTOT (verified 23.7.2026, agent + PRH). Multi-city / nationwide-online
# operators only; the field is structurally local so coverage is written on each row.
# EXCLUDED: Muistovalkea (tietopankki, ei hautaustoimisto), ArvoHautaus (vertailuportaali
# eli kilpaileva palvelu), Lund/Kaarna/Tähtinen (yhden seudun paikallisia), Pietas +
# hyvastit.fi + fenixhautaus.fi (domainit kuolleet), Hautaustoimistojen Liitto (yhdistys).
COMPANIES["hautaustoimistot"] = [
    dict(slug="memoria", nimi="Memoria", domain="memoria.fi", y_tunnus="0875310-3",
         omistaja="Memoria Oy — 30+ itsenäisen perhehautaustoimiston verkosto, palvelua koko maassa"),
    dict(slug="humat", nimi="Humat", domain="humat.fi", y_tunnus="3370342-3",
         omistaja="Hautaustoimisto Humat Oy — Helsinki, Espoo, Vantaa, Tampere, Turku"),
    dict(slug="toro", nimi="Hautaustoimisto Toro", domain="hautaustoimistotoro.fi", y_tunnus="2740478-5",
         omistaja="Torowit Oy — Uusimaa, Varsinais-Suomi ja useita kaupunkeja (Tampere, Jyväskylä, Lahti, Kuopio, Vaasa, Oulu)"),
    dict(slug="hok-elannon-hautauspalvelu", nimi="HOK-Elannon Hautauspalvelu", domain="hok-elannonhautauspalvelu.fi", y_tunnus="1837957-3",
         omistaja="HOK-Elanto Liiketoiminta Oy — S-ryhmän osuuskauppa, 12 toimistoa pääkaupunkiseudulla"),
    dict(slug="lohtu", nimi="Lohtu", domain="lohtu.fi", y_tunnus="3340382-6",
         omistaja="Lohtu Oy — verkkohautaustoimisto, palvelee lähes koko Suomessa"),
    dict(slug="hautauspalvelusi", nimi="Hautauspalvelusi.fi", domain="hautauspalvelusi.fi", y_tunnus="3518496-2",
         omistaja="Hautauspalvelusi Oy — perheyritys, verkkopalvelu Etelä-, Keski- ja Länsi-Suomessa"),
    dict(slug="pietet", nimi="Pietét", domain="pietet.fi", y_tunnus="1010277-2",
         omistaja="Hautauspalvelu Pietét Oy — Helsinki ja Espoo, useita toimipisteitä (suppein kattavuus listalla)"),
]

# MATKATOIMISTOT (verified 23.7.2026, agent + PRH). TUI PUDOTETTU 23.7.2026:
# Akamai-botti-esto palauttaa 403 myos headless-Chromelle -> koko lapinakyvyys-
# mittaus mahdoton, ei pisteyteta arvaamalla (McAfee-precedentti). EXCLUDED: Detur (Detur Finland Oy
# konkurssi 10/2022, domain ohjaa nykyään aventours.fi:hin), Matkavekka (brändi kuoli
# Primera Travel -romahduksessa, domain on nyt geneerinen SEO-blogi = kaapattu),
# Matka-Agentit (sama yhtiö kuin Matkapojat, domain pelkkä redirect). tui.fi:ssä
# botti-esto (Akamai) — mitattava fetch_page.py --js:llä.
COMPANIES["matkatoimistot"] = [
    dict(slug="aurinkomatkat", nimi="Aurinkomatkat", domain="aurinkomatkat.fi", y_tunnus="0200991-4",
         omistaja="Oy Aurinkomatkat - Suntours Ltd Ab — Finnair-konserni, valmismatkojen markkinajohtaja"),
    dict(slug="tjareborg", nimi="Tjäreborg", domain="tjareborg.fi", y_tunnus="0114101-6",
         omistaja="Oy Tjäreborg Ab — osa Nordic Leisure Travel Groupia (Ving)"),
    dict(slug="apollomatkat", nimi="Apollomatkat", domain="apollomatkat.fi", y_tunnus="2322685-4",
         omistaja="DERTOUR Nordic AB, filial i Finland — sivuliike, REWE-konserni (DERTOUR)"),
    dict(slug="matkapojat", nimi="Matkapojat", domain="matkapojat.fi", y_tunnus="0975148-4",
         omistaja="Matkapojat Oy — omistaa myös Matka-Agentit-brändin; risteilyt ja lähialuematkat"),
    dict(slug="lomalinja", nimi="Lomalinja", domain="lomalinja.fi", y_tunnus="0205870-8",
         omistaja="Lomalinja Oy Holiday Tours Ltd — kierto- ja ryhmämatkat valtakunnallisesti"),
    dict(slug="pohjolan-matka", nimi="Pohjolan Matka", domain="pohjolanmatka.fi", y_tunnus="0179285-5",
         omistaja="Pohjolan Turistiauto Oy — 12 toimipaikkaa eri puolilla Suomea"),
    dict(slug="olympia", nimi="Olympia Kaukomatkat", domain="olympia.fi", y_tunnus="2150319-2",
         omistaja="Oy Lentomatkatoimisto Olympia Flygresebyrå Ab — kaukomatkat, yli 70 vuotta alalla"),
    dict(slug="kilroy", nimi="KILROY", domain="kilroy.fi", y_tunnus="0115306-8",
         omistaja="OY KILROY Finland AB — osa tanskalaista KILROY Internationalia"),
    dict(slug="aventura", nimi="Aventura", domain="aventura.fi", y_tunnus="1654907-3",
         omistaja="Matkatoimisto Aventura Oy — räätälöidyt kauko- ja kiertomatkat"),
    dict(slug="imt", nimi="IMT (Ikaalisten Matkatoimisto)", domain="imt.fi", y_tunnus="0838997-0",
         omistaja="Ikaalisten Matkatoimisto Oy — brändi nykyään IMT, valtakunnallinen verkkomyynti"),
]

# TILITOIMISTOT (verified 23.7.2026, agent + PRH). EXCLUDED: Accountor (tilitoimisto-
# liiketoiminta siirtyi Aspiaan 2024-2026, accountor.com/fi ohjaa aspia.fi:hin — brändi
# poistui), Fennoa (ohjelmisto, ei tilitoimisto), Tietotili (sulautunut HLB Finlandiin),
# Premium Group (domain ei vastaa). Rantalainen listataan konsernin ydinyhtiöllä
# (Tilipalvelu Rantalainen Oy) — konserniin kuuluu kymmeniä alueyhtiöitä.
# aallongroup.fi renderöityy JS:llä — asiakassivusto on aallon.fi, sitä mitataan.
COMPANIES["tilitoimistot"] = [
    dict(slug="aspia", nimi="Aspia", domain="aspia.fi", y_tunnus="0932167-9",
         omistaja="Aspia Oy (ent. Accountor Services Oy) — osa pohjoismaista Aspia-konsernia"),
    dict(slug="rantalainen", nimi="Rantalainen", domain="rantalainen.fi", y_tunnus="0362167-0",
         omistaja="Tilipalvelu Rantalainen Oy — Rantalainen-konserni, Suomen suurin tilitoimistoketju, toimistoja koko maassa"),
    dict(slug="talenom", nimi="Talenom", domain="talenom.com", y_tunnus="2551454-2",
         omistaja="Talenom Oyj — pörssiyhtiö, valtakunnallinen"),
    dict(slug="azets", nimi="Azets", domain="azets.com", y_tunnus="0220227-1",
         omistaja="Azets Insight Oy — osa kansainvälistä Azets-konsernia"),
    dict(slug="greenstep", nimi="Greenstep", domain="greenstep.fi", y_tunnus="2306461-3",
         omistaja="Greenstep Oy — kotimainen, toimistoja useissa kaupungeissa ja Pohjoismaissa"),
    dict(slug="aallon-group", nimi="Aallon Group", domain="aallon.fi", y_tunnus="2931805-5",
         omistaja="Aallon Group Oyj — pörssiyhtiö, toimistoja useissa kaupungeissa"),
    dict(slug="administer", nimi="Administer", domain="administer.fi", y_tunnus="0593027-4",
         omistaja="Administer Oyj — pörssilistattu Administer Group, johon kuuluvat myös Silta ja Econia"),
    dict(slug="balanco", nimi="Balanco", domain="balanco.fi", y_tunnus="0964752-1",
         omistaja="Balanco Oy — kasvava ketju, useita toimipisteitä"),
    dict(slug="gallant", nimi="Gallant", domain="gallant.fi", y_tunnus="2994701-1",
         omistaja="Gallant Group Oy — monikaupunkiketju (alueyhtiöitä mm. Espoossa ja Lahdessa)"),
    # Lisätty 26.7.2026 lukijaehdotuksesta. Mitataan samalla kaavalla kuin ketjut.
    dict(slug="smart-office", nimi="Tilitoimisto Smart Office", domain="smartoffice.fi", y_tunnus="1454110-7",
         omistaja="Tilitoimisto Smart Office Oy — helsinkiläinen tilitoimisto (Vallila)"),
]


# FYSIOTERAPIA (verified 23.7.2026, agent + PRH). Fysios Mehiläinen Oy sulautui
# Mehiläinen Oy:hyn 30.4.2026 ja fysios.fi ohjaa mehilainen.fi:hin — siksi Fysios ei ole
# oma rivi. Auron sulautui Fysiokseen 2020 (auron.fi ohjaa nykyään hieronta.fi:hin).
# Debora ostettu Mehiläiselle. Verve ei kuluttajafysioterapiaa. Kunnonpaikka yhden
# paikkakunnan. Lääkärikeskus Aava Oy nimenmuutos 3.6.2025 -> Aava ja Pikkujätti Oy.
# mehilainen.fi vaatii --js-haun (botti-rajoitus curlille).
COMPANIES["fysioterapia"] = [
    dict(slug="coronaria", nimi="Coronaria Fysioterapia", domain="coronaria.fi", y_tunnus="0530530-5",
         omistaja="Coronaria Fysioterapia Oy — osa Coronaria-konsernia, klinikoita kymmenilla paikkakunnilla"),
    dict(slug="kotifysio", nimi="Kotifysio", domain="kotifysio.fi", y_tunnus="2643758-5",
         omistaja="Three E. Champs Oy Ab — kotikäyntifysioterapia, toimintaa useissa kaupungeissa"),
    dict(slug="mehilainen", nimi="Mehiläinen (Fysios)", domain="mehilainen.fi", y_tunnus="1927556-5",
         omistaja="Mehiläinen Oy — Fysios Mehiläinen sulautui emoyhtiöön 4/2026, Suomen suurin fysioterapiaketju"),
    dict(slug="terveystalo", nimi="Terveystalo", domain="terveystalo.com", y_tunnus="1093863-3",
         omistaja="Suomen Terveystalo Oy — valtakunnallinen verkosto, fysioterapiaa lääkärikeskuksissa"),
    dict(slug="pihlajalinna", nimi="Pihlajalinna", domain="pihlajalinna.fi", y_tunnus="2617455-1",
         omistaja="Pihlajalinna Oyj — pörssiyhtiö, fysioterapiaa lääkärikeskuksissa useissa kaupungeissa"),
    dict(slug="aava", nimi="Lääkärikeskus Aava", domain="aava.fi", y_tunnus="2311119-2",
         omistaja="Aava ja Pikkujätti Oy (ent. Lääkärikeskus Aava Oy) — perheomisteinen, pääkaupunkiseutu ja Etelä-Suomi"),
    dict(slug="fressi", nimi="Fressi", domain="fressi.fi", y_tunnus="2538910-4",
         omistaja="Fysioline Fressi Oy — kuntokeskusketju, fysioterapiapalvelut keskuksissa useissa kaupungeissa"),
]

# AUTOPESULAT (verified 23.7.2026, agent + PRH). Hesburger/Hese-Pesu PUDOTETTU
# 23.7.2026: hesburger.fi:lla EI ole autopesusisaltoa lainkaan (tarkistettu kasin:
# ei pesu-linkkeja, /hese-pesu 404, hesepesu.fi ei vastaa) — fyysisia pesulinjoja
# voi olla, mutta kategoria mittaa julkista verkkosisaltoa. EXCLUDED: Teboil (Lukoil-pakotteet
# 11/2025 alkaen, asemaverkosto romahtamassa, Carlyle-kauppa kesken — liian epavakaa
# pisteytettavaksi), Prowash (myy pesukoneita b2b, ei kuluttajaketju), CleanCar/
# Pesuparoni/Pesukunkku (yhden kaupungin), Hurja Pesu + PesuExpress + Uudenmaan
# Pikapesu (domainit kuolleet), Shell-pesut = St1 Suomi Oy operoi (sama omistaja,
# ei omaa rivia). St1 Oy (2082259-7) on rahoitusyhtiö — asemaoperaattori on St1 Suomi Oy.
COMPANIES["autopesulat"] = [
    dict(slug="abc-carwash", nimi="ABC CarWash", domain="abcasemat.fi", y_tunnus="0116323-1",
         omistaja="SOK — pesulat alueosuuskauppojen operoimia, Suomen laajin pesuverkosto"),
    dict(slug="neste", nimi="Neste", domain="neste.fi", y_tunnus="1626490-8",
         omistaja="Neste Markkinointi Oy — pesut asemilla valtakunnallisesti"),
    dict(slug="st1", nimi="St1", domain="autopesu.st1.fi", y_tunnus="0201124-8",
         omistaja="St1 Suomi Oy — yli 60 pesupaikkaa, operoi myös Shell-asemien pesut Suomessa"),
    dict(slug="carwash", nimi="Carwash", domain="carwash.fi", y_tunnus="1859137-1",
         omistaja="DD Group Oy — franchise-ketju, 16 toimipistettä pääkaupunkiseudulla ja Tampereella"),
    dict(slug="gowash", nimi="GoWash", domain="gowash.fi", y_tunnus="2654393-5",
         omistaja="M. Jordan Oy — usean yhtiön franchise-ketju (mm. GoWash Länsi-Suomi Oy), useita kaupunkeja"),
    dict(slug="korrek-pro-center", nimi="KORREK Pro Center", domain="korrekprocenter.fi", y_tunnus="0107011-5",
         omistaja="Berner Oy:n KORREK-konsepti — yrittäjävetoiset pesukeskukset, 9 toimipistettä"),
    dict(slug="carstation", nimi="CarStation", domain="carstation.fi", y_tunnus="2605487-5",
         omistaja="Nura Autopesu Oy — pesukeskuksia Espoossa, Helsingissä ja Turussa"),
]

# TAVARANSAILYTYS (6 consumer self-storage operators; verified 23.7.2026 against PRH v3 + live domains).
# Bot-protection note: cityvarasto.fi returns 404 to a plain curl UA but serves full HTML with a
# browser UA (Cookiebot script visible) — this is a WAF/bot-gate, not a dead site. Lighthouse
# (real Chrome) can render it. Warasto Finland Oy (warasto.fi, Y 2130922-6) excluded: B2B
# logistics/warehousing company, no consumer self-storage product. 24varasto.fi excluded: 403
# to all fetch paths, not bypassable. Tokkovarasto.fi 301-redirects to www.tokkovarasto.fi.
# Kotivarasto.fi 301-redirects to www.kotivarasto.fi. Flexistore.fi 301-redirects to www.
COMPANIES["tavaransailytys"] = [
    dict(slug="cityvarasto", nimi="Cityvarasto", domain="cityvarasto.fi", y_tunnus="1561027-4",
         omistaja="Cityvarasto Oyj — julkinen osakeyhtiö, Vantaa; Suomen suurin pienvarastoketju, 58+ toimipistettä 15+ kaupungissa"),
    dict(slug="pelican", nimi="Pelican Self Storage", domain="pelican.fi", y_tunnus="3224338-1",
         omistaja="Pelican Finland OpCo 2 Oy — Pohjoismaiden johtava self-storage-yhtiö, 14 toimipistettä Helsingissä, Espoossa, Vantaalla ja Turussa"),
    dict(slug="tokkovarasto", nimi="Tokko Vuokravarasto", domain="tokkovarasto.fi", y_tunnus="3108947-4",
         omistaja="Tokko Group Oy, Helsinki — automatisoidut varasto Helsingissä (Hakaniemi, Lauttasaari, Punavuori, Toolo) ja Espoossa"),
    dict(slug="m2selfstorage", nimi="M2 Self Storage", domain="m2selfstorage.fi", y_tunnus="2778522-3",
         omistaja="Helsinki Varastot Oy — toimipisteet Helsingissä (Vuorimiehenkatu) ja Raumalla"),
    dict(slug="kotivarasto", nimi="Kotivarasto", domain="kotivarasto.fi", y_tunnus="1708316-4",
         omistaja="Helsingin Kotivarasto Oy (per. 1993) — toimipisteet Helsingissä (Valuraudantie) ja Oulussa"),
    dict(slug="flexistore", nimi="Flexistore", domain="flexistore.fi", y_tunnus="3380916-4",
         omistaja="Flexistore Finland Oy Ab, Siuntio — sovellusohjattu avainkoodi-varasto, toimintaa Helsingissä ja Siuntiossa"),
]

# ---------------------------------------------------------------- BATCH 7 (24.7.2026)
# TAPAHTUMALIPUT (6 lipunmyyntipalvelua; kodinkonehuolto+catering hylätty viabiliteettitarkistuksessa)
# Lippu.fi botti-esto Akamai-CDN:llä (HTTP-yhteys avautuu, sivu ei vastaa koskaan) —
# kirjattu mittausaukoksi, ei pisteeksi. Kide.app (Treanglo Oy) on opiskelija/yhteisö-
# painotteinen mutta toimii yli 20 kaupungissa ja 170 000+ käyttäjällä — mukana.
# EXCLUDED: fanSALE.fi = Lippupiste Oy:n oma jälleenmyyntialusta (SAME_COMPANY lippu.fi).
COMPANIES["tapahtumaliput"] = [
    dict(slug="ticketmaster", nimi="Ticketmaster", domain="ticketmaster.fi",
         y_tunnus="0110928-6",
         omistaja="Live Nation Entertainment Inc. (Yhdysvallat) — Suomessa Ticketmaster Suomi Oy (ent. Lippupalvelu Oy, perustettu 1945)"),
    dict(slug="lippu", nimi="Lippu.fi", domain="lippu.fi",
         y_tunnus="1789232-4",
         omistaja="CTS Eventim SE & Co. KGaA (Saksa) — Suomessa Lippupiste Oy (rek. 1997); myös Liigalippu-brändi; botti-esto CDN:llä, ei mitattavissa digitaalisesti"),
    dict(slug="tiketti", nimi="Tiketti", domain="tiketti.fi",
         y_tunnus="0116189-3",
         omistaja="Tiketti Oy — Suomen suurin suomalainen lipunvälittäjä (per. 1975); liput saatavilla kaikista R-kioskeista"),
    dict(slug="netticket", nimi="NetTicket", domain="netticket.fi",
         y_tunnus="1028658-3",
         omistaja="Oy NetTicket Finland Ab — suomalainen (Vaasa, per. 1989); teatteri- ja tapahtumalippujen erikoisalusta"),
    dict(slug="kide", nimi="Kide.app", domain="kide.app",
         y_tunnus="2623329-1",
         omistaja="Treanglo Oy — suomalainen startup; pääfokus opiskelijatapahtumat, yli 500 yhteisöä 20+ kaupungissa"),
    dict(slug="eventbrite", nimi="Eventbrite", domain="eventbrite.fi",
         y_tunnus=None,
         omistaja="Eventbrite Inc. (Yhdysvallat) — ei suomalaista rekisteröintiä; toimii Suomessa eventbrite.fi-osoitteessa"),
]


# RAUTAKAUPAT (verified 24.7.2026, agent + PRH). EXCLUDED: RTV (RTV-Yhtymä Oy konkurssi
# 8.1.2025, rtv.fi ohjaa laattapiste.fi:hin), Kodin Terra (brandi lakkautettu 2022 →
# Prisma Rauta ilman omaa domainia), Hartman Rauta (domain kuollut, alueellinen).
# bauhaus.fi antaa curlille 429 → mittaa fetch_page.py --js:lla. ikh.fi vaatii selain-UA:n.
COMPANIES["rautakaupat"] = [
    dict(slug="k-rauta", nimi="K-Rauta", domain="k-rauta.fi", y_tunnus="0109862-8",
         omistaja="Kesko Oyj — noin 130 myymälää valtakunnallisesti, markkinajohtaja"),
    dict(slug="stark", nimi="Stark", domain="stark-suomi.fi", y_tunnus="2043575-7",
         omistaja="Stark Suomi Oy — osa tanskalaista STARK Groupia, kymmeniä myymälöitä"),
    dict(slug="bauhaus", nimi="Bauhaus", domain="bauhaus.fi", y_tunnus="1580679-5",
         omistaja="Bauhaus & Co. Ky — osa saksalaista Bauhaus-konsernia, myymälät useissa kaupungeissa"),
    dict(slug="puuilo", nimi="Puuilo", domain="puuilo.fi", y_tunnus="2726573-8",
         omistaja="Puuilo Oyj — pörssiyhtiö, yli 40 myymälää; kauppaa operoi tytäryhtiö Puuilo Tavaratalot Oy (2431081-2), jonka Y-tunnus näkyy sivustolla"),
    dict(slug="taloon", nimi="Taloon.com", domain="taloon.com", y_tunnus="1870108-3",
         omistaja="Bygghemma Finland Oy — verkkokauppa, osa ruotsalaista BHG Groupia"),
    dict(slug="byggmax", nimi="Byggmax", domain="byggmax.fi", y_tunnus="2132241-2",
         omistaja="Byggmax AB:n Suomen sivuliike — myymälät useissa kaupungeissa ja verkkokauppa"),
]
# EXCLUDED 26.7.2026: IKH (ikh.fi) — Cloudflare-botti-esto palauttaa 403 seka curlille
# etta headless Chromelle; koko sivusto mittauskelvoton (sama linja kuin McAfee 403,
# TUI ja Hesburger). Ei julkaista yhtiota jonka lapinakyvyytta ei voida mitata.

# KATTOREMONTIT (verified 24.7.2026, agent + PRH). EXCLUDED: Laaturemontti (sulautui
# Vesivekiin, domain ohjaa vesivek.fi:hin), Kattomaailma (vain Pirkanmaa), Icopal Katto
# (domain kuollut, toiminta b2b BMI-konsernin sivuilla). Kerabit-domain on jaettu
# valmistajabrandin kanssa; Ruukki Katot on valmistajan (SSAB) remonttipalvelu.
COMPANIES["kattoremontit"] = [
    dict(slug="kattotutka", nimi="Kattotutka", domain="kattotutka.fi", y_tunnus="0904784-1",
         omistaja="Kattotutka Oy — valtakunnallinen, 5 alueellista kattoremonttiyksikköä"),
    dict(slug="vesivek", nimi="Vesivek", domain="vesivek.fi", y_tunnus="0951383-0",
         omistaja="Vesivek Oy — perheomisteinen, omat tehtaat Pirkkalassa ja Orimattilassa, asennus koko maassa"),
    dict(slug="kattokeskus", nimi="Kattokeskus", domain="kattokeskus.fi", y_tunnus="3188733-7",
         omistaja="Kattokeskus Suomi Oy — alueyhtiörakenne, toimintaa useissa maakunnissa"),
    dict(slug="kattocenter", nimi="Suomen KattoCenter", domain="kattocenter.fi", y_tunnus="3146636-4",
         omistaja="Suomen KattoCenter Oy — useita maakuntia Etelä-Suomessa, sisaryhtiö Pirkanmaalla"),
    dict(slug="kattomestarit", nimi="Kattomestarit", domain="kattomestarit.fi", y_tunnus="2177663-3",
         omistaja="Suomen Kattomestarit Oy — kiertävä asennusverkosto useissa kaupungeissa, yli 40 vuotta alalla"),
    dict(slug="kerabit", nimi="Kerabit", domain="kerabit.fi", y_tunnus="2432892-4",
         omistaja="KerabitPro Oy — osa Nordic Waterproofing -konsernia, urakointi ja kattohuolto valtakunnallisesti"),
    dict(slug="ruukki-katot", nimi="Ruukki Katot", domain="ruukkikatot.fi", y_tunnus="2389450-2",
         omistaja="Ruukki Construction Oy — valmistajan (SSAB) kattoremonttipalvelu kuluttajille"),
]

# TYONVALITYSPALVELUT (verified 24.7.2026, agent + PRH). Kuluttajakulma = tyonhakija.
# EXCLUDED: VMP ja Smile Henkilostopalvelut (sulautuivat Eezyyn 2019), Go On (brandi
# vaihtui Bondataksi — listattu Bondatana). Adeccolla ei omaa fi-juuridomainia
# (adecco.com/fi-fi); Bondatan juuri on subdomain henkilostopalvelut.bondata.fi.
COMPANIES["tyonvalityspalvelut"] = [
    dict(slug="barona", nimi="Barona", domain="barona.fi", y_tunnus="2808477-9",
         omistaja="Barona Oy — osa Bravedo-konsernia, Suomen suurin henkilöstöpalveluyhtiö"),
    dict(slug="eezy", nimi="Eezy", domain="eezy.fi", y_tunnus="2854570-7",
         omistaja="Eezy Oyj — pörssiyhtiö, syntyi VMP:n ja Smilen fuusiosta 2019, noin 60 toimipistettä"),
    dict(slug="staffpoint", nimi="StaffPoint", domain="staffpoint.fi", y_tunnus="2492090-1",
         omistaja="StaffPoint Oy — osa StaffPoint Holdingia, valtakunnallinen"),
    dict(slug="academic-work", nimi="Academic Work", domain="academicwork.fi", y_tunnus="2756351-6",
         omistaja="Academic Work Finland Oy — ruotsalainen konserni, nuorten ammattilaisten välitys"),
    dict(slug="bolt-works", nimi="Bolt.Works", domain="bolt.works", y_tunnus="2041555-3",
         omistaja="Bolt.Works Oy — suomalainen, rakennus-, teollisuus- ja logistiikka-alat"),
    dict(slug="manpower", nimi="Manpower", domain="manpower.fi", y_tunnus="1091032-3",
         omistaja="ManpowerGroup Oy — osa yhdysvaltalaista ManpowerGroupia"),
    dict(slug="bondata", nimi="Bondata Henkilöstöpalvelut", domain="henkilostopalvelut.bondata.fi", y_tunnus="3293589-8",
         omistaja="Bondata Group Oy (ent. Go On Group) — Korona Invest -omisteinen alueyhtiöverkosto"),
    dict(slug="adecco", nimi="Adecco", domain="adecco.com", y_tunnus="1042464-0",
         omistaja="Adecco Finland Oy — osa sveitsiläistä Adecco Groupia; suomenkielinen palvelu adecco.com/fi-fi"),
]

# ---------------------------------------------------------------- BATCH 8 / autopilot-tikki (24.7.2026)
# SILMASAIRAALAT (6 yksityistä silmäkirurgian tarjoajaa; verified 24.7.2026, agent + PRH).
# Medilaser sulautui Silmäasemaan 2020 — ei erillinen rivi.
# ÖGA (Tampere), Turun Silmälaser, Laser-Porus (Oulu), Eiran Sairaala (Helsinki) rajattu
# ulkopuolelle: yksittäiset kaupungit, ei valtakunnallinen ketju.
# Haukansilm Oy: mikrofirma, ei kuluttajasivustoa.
# Terveystalo ostaa Silmäaseman Coronarialta; kauppa KKV-käsittelyssä — yhtiöt ovat
# toistaiseksi erilliset (mittaus tehty 24.7.2026 ennen sulkeutumista).
COMPANIES["silmasairaalat"] = [
    dict(slug="silmaasema", nimi="Silmäasema", domain="silmaasema.fi", y_tunnus="2627773-7",
         omistaja="Silmäasema Oy (ent. Silmäasema Oyj) — Coronaria Oy:n omistama; 18 yksityistä silmäsairaalaa ja noin 150 optikkoliikettä valtakunnallisesti; Terveystalo ostaa, kauppa vireillä"),
    dict(slug="pilke", nimi="Silmäsairaala Pilke", domain="silmasairaalapilke.fi", y_tunnus="3215906-7",
         omistaja="Silmäsairaala Pilke Oy — 6 toimipistettä: Espoo, Helsinki, Jyvaskyla, Tampere, Turku, Vaasa; perustettu silmäkirurgien toimesta"),
    dict(slug="valo", nimi="Silmäsairaala Valo", domain="silmasairaalavalo.fi", y_tunnus="2767513-9",
         omistaja="Silmäsairaala Valo Oy (ent. Silmäsairaala Lux Oy) — toimipisteet Helsingissä ja Kouvolassa; yhteistyö Instrumentariumin ja Mehilaisen kanssa"),
    dict(slug="terveystalo", nimi="Terveystalo (silmäkirurgia)", domain="terveystalo.com", y_tunnus="1093863-3",
         omistaja="Suomen Terveystalo Oy — valtakunnallinen, silmäkirurgiaa useilla paikkakunnilla; ostaa Silmäaseman, kauppa vireillä"),
    dict(slug="mehilainen", nimi="Mehiläinen (silmäkirurgia)", domain="mehilainen.fi", y_tunnus="1927556-5",
         omistaja="Mehiläinen Oy — valtakunnallinen, silmäkirurgiaa Helsingissä, Jyvaskylass, Kuopiossa, Tampereella, Vaasassa ja Oulussa"),
    dict(slug="pihlajalinna", nimi="Pihlajalinna (Pohjola Sairaala)", domain="pihlajalinna.fi", y_tunnus="2617455-1",
         omistaja="Pihlajalinna Oyj — pörssilistattu; silmäkirurgia Pohjola Sairaalan kautta Helsingissä ja muilla paikkakunnilla"),
]

# --- uutismediat (26.7.2026, Antonin pyyntö: mediavertailu) -------------------
# Yksiköt ovat YKSITTÄISIÄ MEDIOITA (lehti/uutispalvelu), eivät konserneja —
# siksi sama julkaisija voi esiintyä kahdesti (Sanoma: HS+IS, Alma: IL+KL).
# Omistus näytetään avoimesti omistaja-kentässä. Y-tunnukset PRH v3 26.7.2026.
# MTV: Telia myi Schibsted Medialle, kauppa toteutui 1.7.2025.
# Kaleva: Kaleva Media ja Ilkka-yhtymä yhdistivät medialiiketoimintansa
# yhteisyhtiöön 1.1.2026 (Kaleva 65 %, Ilkka 35 %).
COMPANIES["uutismediat"] = [
    dict(slug="helsingin-sanomat", nimi="Helsingin Sanomat", domain="hs.fi", y_tunnus="1515901-4",
         omistaja="Sanoma Media Finland Oy (Sanoma Oyj) — Suomen suurin tilattava sanomalehti (per. 1889)"),
    dict(slug="ilta-sanomat", nimi="Ilta-Sanomat", domain="is.fi", y_tunnus="1515901-4",
         omistaja="Sanoma Media Finland Oy (Sanoma Oyj) — sama julkaisija kuin Helsingin Sanomilla"),
    dict(slug="iltalehti", nimi="Iltalehti", domain="iltalehti.fi", y_tunnus="0869288-1",
         omistaja="Alma Media Finland Oy (Alma Media Oyj) — sama konserni kuin Kauppalehdella"),
    dict(slug="kauppalehti", nimi="Kauppalehti", domain="kauppalehti.fi", y_tunnus="0869288-1",
         omistaja="Alma Media Finland Oy (Alma Media Oyj) — talousmedia (per. 1898); sama konserni kuin Iltalehdella"),
    dict(slug="yle-uutiset", nimi="Yle Uutiset", domain="yle.fi", y_tunnus="0215438-8",
         omistaja="Yleisradio Oy — julkisen palvelun media, rahoitus Yle-verolla, eduskunnan valvonnassa"),
    dict(slug="mtv-uutiset", nimi="MTV Uutiset", domain="mtvuutiset.fi", y_tunnus="1093944-1",
         omistaja="MTV Oy — Schibsted Media (Norja) osti Telialta, kauppa toteutui 1.7.2025"),
    dict(slug="turun-sanomat", nimi="Turun Sanomat", domain="ts.fi", y_tunnus="0141911-0",
         omistaja="TS-Yhtymä Oy — perheomisteinen (Ketonen), Suomen vanhin edelleen ilmestyvä päivälehti (per. 1904)"),
    dict(slug="kaleva", nimi="Kaleva", domain="kaleva.fi", y_tunnus="2715049-8",
         omistaja="Kaleva Media Oy — Kaleva Media ja Ilkka-yhtymä yhdistivät medialiiketoimintansa 1.1.2026 (Kaleva 65 %, Ilkka 35 %)"),
]

# --- aikakauslehdet (26.7.2026, Antonin pyyntö — jatko uutismedioille) --------
# Yksiköt ovat YKSITTÄISIÄ LEHTIÄ, eivät kustantajia. Otavamedia julkaisee 4/8 —
# markkina on keskittynyt ja se kerrotaan avoimesti omistaja-kentässä.
# Y-tunnukset PRH v3 26.7.2026: A-lehdet Oy 1708790-7, Otavamedia Oy 0196807-2,
# Aller Media Oy 0872238-2, Sanoma Media Finland Oy 1515901-4.
COMPANIES["aikakauslehdet"] = [
    dict(slug="apu", nimi="Apu", domain="apu.fi", y_tunnus="1708790-7",
         omistaja="A-lehdet Oy — perheomisteinen (Aatos Erkko -suvusta erillinen A-lehdet-suku), per. 1933"),
    dict(slug="seura", nimi="Seura", domain="seura.fi", y_tunnus="0196807-2",
         omistaja="Otavamedia Oy (Otava-konserni) — sama kustantaja kuin SK:lla, TM:llä ja Kotiliedellä"),
    dict(slug="suomen-kuvalehti", nimi="Suomen Kuvalehti", domain="suomenkuvalehti.fi", y_tunnus="0196807-2",
         omistaja="Otavamedia Oy (Otava-konserni) — yhteiskunnallinen viikkolehti (per. 1916)"),
    dict(slug="tekniikan-maailma", nimi="Tekniikan Maailma", domain="tekniikanmaailma.fi", y_tunnus="0196807-2",
         omistaja="Otavamedia Oy (Otava-konserni) — tekniikan ja autoilun erikoislehti (per. 1953)"),
    dict(slug="kotiliesi", nimi="Kotiliesi", domain="kotiliesi.fi", y_tunnus="0196807-2",
         omistaja="Otavamedia Oy (Otava-konserni) — Suomen vanhimpia aikakauslehtiä (per. 1922)"),
    dict(slug="et-lehti", nimi="ET-lehti", domain="etlehti.fi", y_tunnus="1515901-4",
         omistaja="Sanoma Media Finland Oy (Sanoma Oyj) — sama kustantaja kuin Tiede-lehdella"),
    dict(slug="seiska", nimi="Seiska", domain="seiska.fi", y_tunnus="0872238-2",
         omistaja="Aller Media Oy (Aller-konserni, Tanska) — viihdelehti"),
]
# EXCLUDED 26.7.2026: Tiede — tiede.fi ohjautuu hs.fi/tiede-osioon, lehdella ei ole
# enaa itsenaista verkkosivustoa jota voisi mitata erillaan Helsingin Sanomista
# (lehti itsessaan elaa tilaa.sanoma.fi-katalogissa). Ei mitata toisen median
# sivustoa taman nimissa.

# --- huonekaluketjut (26.7.2026, Antonin pyyntö) ------------------------------
# Y-tunnukset: PRH v3 + Asiakastieto/Proff 26.7.2026.
# EXCLUDED: Asko ja Sotka — Indoor Group Oy meni konkurssiin helmikuussa 2026,
# myymälät suljettiin ja Toivo Sukari (Maskun omistaja) osti pelkät brändit
# konkurssipesältä maalis-huhtikuussa 2026 (Yle 74-20211430). sotka.fi ohjautuu
# jo masku.comiin. Kuolleita ketjuja ei pisteytetä.
COMPANIES["huonekaluketjut"] = [
    dict(slug="ikea", nimi="IKEA", domain="ikea.com", y_tunnus="2149172-6",
         omistaja="IKEA Oy — Ingka Group (Alankomaat/Ruotsi); Suomessa myymälät ja verkkokauppa ikea.com/fi"),
    dict(slug="jysk", nimi="JYSK", domain="jysk.fi", y_tunnus="1000514-7",
         omistaja="JYSK OY — Lars Larsen Group (Tanska)"),
    dict(slug="isku", nimi="Isku", domain="isku.fi", y_tunnus="0148884-5",
         omistaja="Isku-Yhtymä Oy — perheomisteinen suomalainen (Lahti, per. 1928)"),
    dict(slug="masku", nimi="Masku", domain="masku.com", y_tunnus="0583816-0",
         omistaja="Maskun Kalustetalo Oy (Toivo Sukari) — osti Asko- ja Sotka-brändit Indoor Groupin konkurssipesältä keväällä 2026"),
    dict(slug="vepsalainen", nimi="Vepsäläinen", domain="vepsalainen.com", y_tunnus="2111755-8",
         omistaja="Vepsäläinen Oy — suomalainen design-huonekalujen ketju (per. 1926)"),
    dict(slug="stemma", nimi="Stemma", domain="stemma.fi", y_tunnus="0250671-8",
         omistaja="Stemma Oy — itsenäisten kauppiaiden suomalainen ketju"),
]

# --- elektroniikkaketjut (26.7.2026, Antonin pyyntö) --------------------------
# Y-tunnukset: PRH v3 + Asiakastieto 26.7.2026. Jimm's: Lounea ja tj myivät koko
# osakekannan saksalaiselle Casekingille 2018 (muropaketti.com). Proshop toimii
# Suomessa Tanskasta käsin ilman suomalaista Y-tunnusta.
COMPANIES["elektroniikkaketjut"] = [
    dict(slug="gigantti", nimi="Gigantti", domain="gigantti.fi", y_tunnus="1523846-8",
         omistaja="Gigantti Oy Ab — Elkjøp Nordic / Currys plc (Iso-Britannia)"),
    dict(slug="verkkokauppa", nimi="Verkkokauppa.com", domain="verkkokauppa.com", y_tunnus="1456344-5",
         omistaja="Verkkokauppa.com Oyj — suomalainen pörssiyhtiö (Helsinki)"),
    dict(slug="power", nimi="Power", domain="power.fi", y_tunnus="0993774-8",
         omistaja="Power Finland Oy — Power International AS (Norja)"),
    dict(slug="jimms", nimi="Jimm's PC-Store", domain="jimms.fi", y_tunnus="0885951-4",
         omistaja="Jimm's PC-store Oy — Caseking GmbH (Saksa) osti 2018; PC-komponenttien erikoisliike (Turku)"),
    dict(slug="multitronic", nimi="Multitronic", domain="multitronic.fi", y_tunnus="1008670-9",
         omistaja="Multitronic Oy — suomalainen (Vaasa, per. 1994)"),
    dict(slug="proshop", nimi="Proshop", domain="proshop.fi", y_tunnus=None,
         omistaja="Proshop A/S (Tanska) — palvelee Suomea proshop.fi-verkkokaupalla ilman myymälöitä"),
]

# --- urheiluvalineketjut (26.7.2026, Antonin pyyntö) --------------------------
# Intersport ja Budget Sport ovat molemmat Keskon Intersport Finland Oy:n
# konsepteja — listataan erikseen, omistus kerrotaan (HS/IS-linja).
# Sportia jätetty pois: ei näyttöä elävästä valtakunnallisesta ketjusta.
# XXL jatkaa Suomessa (sulkenut yksittäisiä myymälöitä 2026, ketju toimii).
# Y-tunnukset PRH v3 + Asiakastieto 26.7.2026.
COMPANIES["urheiluvalineketjut"] = [
    dict(slug="xxl", nimi="XXL", domain="xxl.fi", y_tunnus="2541215-9",
         omistaja="XXL Sports & Outdoor Oy — XXL ASA (Norja); karsinut myymäläverkkoaan Suomessa 2026"),
    dict(slug="intersport", nimi="Intersport", domain="intersport.fi", y_tunnus="1648871-7",
         omistaja="Intersport Finland Oy (Kesko Oyj) — sama yhtiö operoi myös Budget Sportia"),
    dict(slug="budget-sport", nimi="Budget Sport", domain="budgetsport.fi", y_tunnus="1648871-7",
         omistaja="Intersport Finland Oy (Kesko Oyj) — sama yhtiö operoi myös Intersportia"),
    dict(slug="stadium", nimi="Stadium", domain="stadium.fi", y_tunnus="1515574-2",
         omistaja="Stadium Oy — ruotsalainen perheomisteinen Stadium AB"),
    dict(slug="partioaitta", nimi="Partioaitta", domain="partioaitta.fi", y_tunnus="0201830-0",
         omistaja="Partioaitta Oy — Fenix Outdoor International AG (Ruotsi/Sveitsi)"),
    dict(slug="varuste", nimi="Varuste.net", domain="varuste.net", y_tunnus="1702286-3",
         omistaja="Aalto Group Oy — suomalainen (Helsinki), ulkoilun ja urheilun verkkokauppa"),
    dict(slug="scandinavian-outdoor", nimi="Scandinavian Outdoor", domain="scandinavianoutdoor.fi", y_tunnus="2066059-1",
         omistaja="Scandinavian Outdoor Oy — suomalainen ulkoiluvarusteketju"),
]

# --- ikkunaremontit (27.7.2026, Antonin pyyntö, 5 kategorian erä; tutkimusagentti + PRH) ---
# Pihla ja Tiivi ovat saman Inwido AB:n (Pihla Group Oy) brandeja - kerrotaan avoimesti.
COMPANIES["ikkunaremontit"] = [
    dict(slug="pihla", nimi="Pihla", domain="pihla.fi", y_tunnus="1882624-9",
         omistaja="Pihla Group Oy (ent. Inwido Finland Oy) on osa Tukholman pörssiin listattua ruotsalaista Inwido AB -konsernia, joka omistaa myös Tiivi-brändin."),
    dict(slug="tiivi", nimi="Tiivi", domain="tiivi.fi", y_tunnus="1882624-9",
         omistaja="Tiivi on Pihla Group Oy:n brändi (Tiivituote Oy sulautui 1.1.2015) eli sama Inwido AB -konserni kuin Pihlalla — huomioi vertailussa yhteinen omistaja ja Y-tunnus."),
    dict(slug="skaala", nimi="Skaala", domain="skaala.com", y_tunnus="2656258-9",
         omistaja="Skaala IFN Oy (Kauhava/Ylihärmä) on kuulunut itävaltalaiseen IFN Holding -konserniin vuodesta 2017 (ei Dovista, kuten joskus luullaan)."),
    dict(slug="lammin-ikkuna", nimi="Lammin Ikkunat ja Ovet", domain="lammin.fi", y_tunnus="1454666-1",
         omistaja="Lammin Ikkuna Oy (Hämeenlinnan Lammi, per. 1972) on kokonaan suomalaisomisteinen itsenäinen yhtiö, toimitusjohtajana Hannu Saarinen."),
    dict(slug="alavus-ikkunat", nimi="Alavus Ikkunat ja Ovet", domain="alavusikkunat.fi", y_tunnus="1796128-9",
         omistaja="Alavus Ikkunat Oy (per. 2003) on yksityinen kotimainen yhtiö, jonka omistavat mm. Kimmo ja Erno Hautamäki, Tarmo Peltoniemi, Arto Paalanen (tj.) ja Juha Äijänaho; toimipisteitä Alavuden lisäksi Vantaalla, Tampereella ja Turussa."),
    dict(slug="hr-ikkunat", nimi="HR-Ikkunat", domain="hrikkunat.fi", y_tunnus="1910924-1",
         omistaja="HR-Ikkunat Oy (ent. HR-Ikkunat Ruhkala Oy, Kalajoen Tynkä) on Ruhkalan suvun kolmannen polven perheyritys, omistajina serkukset Kari ja Ari Ruhkala."),
    dict(slug="piklas", nimi="Piklas", domain="piklas.fi", y_tunnus="0189227-4",
         omistaja="Piklas Oy on osa perhetaustaista PRT-Forest-ryhmää: vanha Piklas Oy (1999174-8) sulautui emoyhtiöönsä 28.2.2025 ja emo PRT-Forest Oy otti nimen Piklas Oy (kotipaikka Pyhäntä)."),
]

# --- lampopumppuasentajat (27.7.2026, Antonin pyyntö, 5 kategorian erä; tutkimusagentti + PRH) ---
# Renoa asentaa vain ilma-vesilampopumppuja (ei maalampoa) - todettu omistaja-kentassa.
COMPANIES["lampopumppuasentajat"] = [
    dict(slug="tomallensenera", nimi="Tom Allen Senera", domain="tomallensenera.fi", y_tunnus="1016410-5",
         omistaja="Tom Allen Senera Oy (per. 1995, Vantaa) on osa pohjoismaista Assemblin Caverion Group -konsernia (Seneran konserni siirtyi Assemblinille 2021, Assemblin ja Caverion yhdistyivät 2024)."),
    dict(slug="lampoykkonen", nimi="LämpöYkkönen", domain="lampoykkonen.fi", y_tunnus="2155807-0",
         omistaja="LämpöYkkönen Oy (per. 2007, kotipaikka Jyväskylä) on suomalainen lämpöpumppuasentaja, jonka vähemmistöomistajaksi (30 %) tuli saksalainen lämmityslaitevalmistaja Viessmann; yhtiöllä on lisäksi Helenin kanssa maalämpöön keskittyvä yhteisyritys."),
    dict(slug="lampopartio", nimi="Lämpöpartio", domain="lampopartio.fi", y_tunnus="2436191-9",
         omistaja="Lämpöpartio Oy (per. 2011, kotipaikka Kokkola) on 100-prosenttisesti suomalaisomisteinen perheyhtiö, toimitusjohtaja Vesa Malmberg."),
    dict(slug="renoa", nimi="Renoa", domain="renoa.fi", y_tunnus="2612804-5",
         omistaja="Renoa Group Oy on entinen KotiSun-konserni (palvelut yhdistettiin Renoa-nimen alle 2021); CapMan myi yhtiön joulukuussa 2024 toimivalle johdolle, rahoittajina Korpi Capital ja Marko Malmivaaran sijoitusyhtiö."),
    dict(slug="lampokumppanit", nimi="Lämpökumppanit", domain="lampokumppanit.fi", y_tunnus="3332404-4",
         omistaja="Lämpökumppanit Oy on nuori (per. n. 2023) yksityisomisteinen suomalainen lämpöpumppuyhtiö, jolla toimipisteet Helsingissä, Tampereella ja Oulussa."),
    dict(slug="zatap", nimi="Zatap", domain="zatap.fi", y_tunnus="3149597-4",
         omistaja="Zatap Oy on itsenäinen suomalainen energiaremonttiyhtiö (lämpöpumput ja aurinkosähkö), ei tunnettua emoyhtiötä."),
    dict(slug="lampovalli", nimi="Lämpö-Valli", domain="lampovalli.fi", y_tunnus="2432031-6",
         omistaja="Lämpö-Valli Oy on yksityisomisteinen jyväskyläläinen putkiliike, joka toimii kolmella paikkakunnalla (Jyväskylä, Kuopio, Tampere)."),
    dict(slug="ilpurakointi", nimi="ILP Urakointi", domain="ilpurakointi.fi", y_tunnus="3169601-2",
         omistaja="ILP Urakointi Oy (aputoiminimi ILP Sähkö) on yksityisomisteinen turkulainen ilmalämpöpumppuasentaja, joka toimii Varsinais-Suomessa ja Uudellamaalla."),
]

# --- aurinkopaneeliasentajat (27.7.2026, Antonin pyyntö; tutkimusagentti + PRH) ---
# Helen jätetty pois: kuluttaja-aurinkomyynnin hoitaa listattu kumppani Aurinkotekniikka.
# Seron: kuluttaja-asiamiehen puuttuminen ovimyyntiin 2025 mainittu omistajarivillä.
COMPANIES["aurinkopaneeliasentajat"] = [
    dict(slug="energio", nimi="Energio", domain="energio.fi", y_tunnus="3228147-6",
         omistaja="Energio Finland Oy on vuonna 2021 perustettu itsenäinen kotimainen yhtiö (tj Jarno Kautto, Raisio/Helsinki), jonka omat asennustiimit toimivat Uudellamaalla, Varsinais-Suomessa, Pirkanmaalla ja Savossa ja toiminta kattaa koko Manner-Suomen."),
    dict(slug="solarum", nimi="Solarum", domain="solarum.fi", y_tunnus="2984708-8",
         omistaja="Solarum Suomi Oy on vuonna 2019 perustettu itsenäinen kotimainen sähköurakointiyhtiö (tj Antti Tahkola, kotipaikka Liminka/Oulunsalo) ilman tiedossa olevaa emoyhtiötä; asentaa avaimet käteen -toimituksena koko Suomeen."),
    dict(slug="1komma5-suomi", nimi="1KOMMA5° Suomi", domain="1komma5.com", y_tunnus="2778665-6",
         omistaja="1KOMMA5° Suomi on juridisesti Solar Age Oy (perustettu 2016, Kaarina/Turku), jonka enemmistön saksalainen 1KOMMA5° GmbH osti lokakuussa 2022; perustajat Ricardo Pacheco sekä Pasi ja Petri Seppälä; toimialueet Varsinais-Suomi, Uusimaa ja Pirkanmaa."),
    dict(slug="seron", nimi="Seron", domain="seron.fi", y_tunnus="3332016-6",
         omistaja="Seron Oy:n (Tampere) omistaa ja sitä johtaa Lauri Vepsäläinen; toimittaa ja asentaa aurinkopaneeleita koko Suomessa — HUOM: kuluttaja-asiamies puuttui 2025 yhtiön painostavaan kotimyyntiin iäkkäille (Yle 74-20171581), huomioitava luotettavuusarvioinnissa."),
    dict(slug="aurinkotekniikka", nimi="Aurinkotekniikka", domain="aurinkotekniikka.fi", y_tunnus="3428090-1",
         omistaja="Aurinkotekniikka-brändin myynnistä vastaa Aurinkotekniikka Myynti Oy (3428090-1) ja asennuksista sisaryhtiö AurinkoPro Oy (2758891-6, ent. Suomen Aurinkotekniikka Oy, nimenmuutos 30.10.2025); kotimainen kokonaisuus, yli 5000 asennettua järjestelmää ja Helenin kuluttaja-aurinkovoimaloiden myynti- ja asennuskumppani — RISKI: AurinkoPron liikevaihto putosi 2024 n. 80 % (1,3 M€, tulos -233 t€), taloustilanne syytä arvioida."),
    dict(slug="lampopartio", nimi="Lämpöpartio", domain="lampopartio.fi", y_tunnus="2436191-9",
         omistaja="Lämpöpartio Oy on vuonna 2011 perustettu itsenäinen kotimainen energiaremonttiyhtiö (tj Vesa Malmberg), kotipaikka Kokkola ja toimipisteet Helsingissä, Jyväskylässä ja Oulussa; yli 12 500 energiaremonttia."),
    dict(slug="at-aurinkopaneelit", nimi="AT Aurinkopaneelit", domain="ataurinkopaneelit.fi", y_tunnus="3006802-2",
         omistaja="At Aurinkopaneelit Oy on itsenäinen kotimainen aurinkosähköasentaja (PRH: aktiivinen, rinnakkaistoiminimi Kattokeisari), ei tiedossa olevaa emoyhtiötä; palvelee valtakunnallisesti."),
    dict(slug="kotisi-energia", nimi="Kotisi Energia", domain="kotisienergia.fi", y_tunnus="2787210-8",
         omistaja="Kotisi Energia Nordic Oy (PRH: aktiivinen, aiempi nimi Kotisi LVI Oy) on itsenäinen kotimainen aurinkopaneelien myynti- ja asennusyhtiö ilman tiedossa olevaa emoyhtiötä."),
]

# --- kukkakauppojen-verkkokaupat (28.7.2026, Antonin pyyntö; tutkimusagentti + PRH) ---
# Kukka Express jätetty pois: operaattoria ei voitu todentaa (anonyymi ulkomainen
# verkosto) — emme julkaise yhtiötä jonka omistajaa ei voi nimetä.
COMPANIES["kukkakauppojen-verkkokaupat"] = [
    dict(slug="interflora", nimi="Interflora", domain="interflora.fi", y_tunnus="0109243-7",
         omistaja="Interflora.fi-verkkokauppaa pyörittää Interflora-Myynti Oy (PRH: aktiivinen), joka kuuluu suomalaisten kukkakauppiaiden omistamaan Interflora-Suomi ry:hyn; kukkavälitys kattaa lähes koko Suomen jäsenkauppojen kautta."),
    dict(slug="ekukka", nimi="eKukka.fi", domain="ekukka.fi", y_tunnus="2485800-1",
         omistaja="eKukka.fi-tilausalustaa ylläpitää oululainen Floweb Oy (PRH: aktiivinen), floristimestari Pasi Kivilompolon ja hänen veljensä perustama kotimainen yhtiö; verkostossa yli 500 kukkakauppaa yli 200 paikkakunnalla."),
    dict(slug="verkkokukka", nimi="Verkkokukka.fi", domain="verkkokukka.fi", y_tunnus="0686978-6",
         omistaja="Verkkokukka.fi on Oy Kukkien Datavälitys DF Ltd:n (DataFlora-välitysketju, PRH: aktiivinen) ja sen yli 60 kumppanikukkakaupan yhteinen verkkokauppa, joka toimittaa kukat oman ilmoituksensa mukaan kaikkialle Suomeen."),
    dict(slug="lahetakukkia", nimi="Lähetäkukkia.fi", domain="lahetakukkia.fi", y_tunnus="0815227-9",
         omistaja="Lähetäkukkia.fi:tä ylläpitää kokkolalainen Järvelä Invest Oy (markkinointinimi Vakkurin Kukka, PRH: aktiivinen), joka toimittaa oman alueensa itse ja muun Suomen eKukka-, DataFlora- ja Interflora-ketjujen kautta."),
    dict(slug="kukka-garden", nimi="Kukka Garden", domain="kukkagarden.fi", y_tunnus="3015820-4",
         omistaja="Kukka Garden on Hallin Luomupuoti Oy:n (PRH: aktiivinen) kukkakauppa Helsingin Vuosaaren Columbuksessa; verkkokaupan kukkalähetykset toimitetaan ilmaiseksi Helsinkiin ja Vantaalle sekä 15 euron lisämaksusta muualle Suomeen."),
    dict(slug="piilola", nimi="Kukkakauppa Piilola", domain="piilola.fi", y_tunnus="1895827-6",
         omistaja="Piilola.fi on Kukkamyynti Piilola Oy:n (PRH: aktiivinen, kolme myymälää Helsingissä, toiminut Etelä-Haagassa 1970-luvulta) verkkokauppa; oma toimitus kattaa pääkaupunkiseudun ja muut paikkakunnat hoidetaan Interflora-kukkavälityksen kautta."),
]

# --- lastenvaatteiden-verkkokaupat (28.7.2026, Antonin pyyntö, erä 2; tutkimusagentti + PRH) ---
# Papu Design konkurssi 10/2025, Vimma+Mainio lopettaneet lastenvaatteet - karsittu.
# Polarn O. Pyret karsittu 28.7.2026: SPA + Cloudflare, alasivujen URL:t eivat
# nay HTML:ssa edes --js:lla -> sivustoa ei voi mitata rehellisesti.
COMPANIES["lastenvaatteiden-verkkokaupat"] = [
    dict(slug="reima", nimi="Reima", domain="reima.com", y_tunnus="2204295-7",
         omistaja="Reima Europe Oy (Reima Group), enemmistön omistavat hallituksen puheenjohtaja Elina Björklund sekä ruotsalaiset Anders Ullstrand ja Jonas Meerits, rahoittajana ruotsalainen P Capital Partners."),
    dict(slug="gugguu", nimi="Gugguu", domain="gugguu.com", y_tunnus="2508855-5",
         omistaja="Gugguu Oy:n pääomistajat ovat perustajasisarukset Miia Riekki (tj) ja Anne Valli; sijoitusyhtiö Panostaja osti 43 prosentin vähemmistöosuuden."),
    dict(slug="metsola", nimi="Metsola", domain="metsola.fi", y_tunnus="2245002-9",
         omistaja="Metsola Lifestyle Oy, josta suomalainen perheyhtiö SGN Group osti 75 % vuonna 2021; perustajat Riina ja Heikki Pulkkinen jatkavat 25 prosentin osuudella."),
    dict(slug="kaiko", nimi="KAIKO", domain="kaikoshop.com", y_tunnus="2878739-4",
         omistaja="Kaiko Clothing Company Oy on perustajiensa omistama helsinkiläinen vastuullisuusbrändi (naisten- ja lastenvaatteet), joka ohjaa 7 % tuotteen tuotosta nepalilaisten naisten koulutukseen."),
    dict(slug="melli-ecodesign", nimi="Melli EcoDesign", domain="melli.fi", y_tunnus="2845286-9",
         omistaja="Melli EcoDesign Oy on perustajiensa omistama jyväskyläläinen yritys, jonka lasten- ja naistenvaatteet valmistetaan Jyväskylässä."),
    dict(slug="ruskovilla", nimi="Ruskovilla", domain="ruskovilla.fi", y_tunnus="3488506-2",
         omistaja="Ruskovilla Oy on artjärveläinen perheyritys, joka valmistaa luonnonkuituvaatteet (luomuvilla, silkki) Suomessa; liiketoiminta siirtyi uudelle Ruskovilla Oy:lle (3488506-2) vanhan yhtiön (0432769-2) rekisteröinnin päätyttyä 31.3.2025 — järjestely, ei konkurssia (2024 liikevaihto 2,5 M€, liikevoitto 352 t€)."),
    dict(slug="pikkuotus", nimi="pikkuOtus", domain="pikkuotus.fi", y_tunnus="2479277-8",
         omistaja="pikkuOtus Oy on ylöjärveläinen yrittäjävetoinen monimerkkiverkkokauppa, joka myy kotimaisia lastenvaatemerkkejä (mm. Metsola, Kaiko, Mainio)."),
]

# --- lemmikkitarvikkeiden-verkkokaupat (28.7.2026, Antonin pyyntö, erä 2; tutkimusagentti + PRH) ---
# Faunatar karsittu: palvelin ei vastaa; affiliate-aggregaattorit hylatty.
COMPANIES["lemmikkitarvikkeiden-verkkokaupat"] = [
    dict(slug="musti-ja-mirri", nimi="Musti ja Mirri", domain="mustijamirri.fi", y_tunnus="1083808-5",
         omistaja="Musti ja Mirri Oy kuuluu Musti Group -konserniin, jonka osti pörssistä vuonna 2024 Flybird Holding Oy:n kautta portugalilaisen Sonaen sekä Jeffrey Davidin, Johan Dettelin ja toimitusjohtaja David Rönnbergin konsortio."),
    dict(slug="zooplus", nimi="Zooplus", domain="zooplus.fi", y_tunnus=None,
         omistaja="Zooplus.fi:tä operoi saksalainen zooplus SE (München), jonka pääomasijoittajat Hellman & Friedman ja EQT ostivat pois pörssistä vuonna 2021; ei suomalaista Y-tunnusta."),
    dict(slug="peten-koiratarvike", nimi="Peten Koiratarvike", domain="petenkoiratarvike.com", y_tunnus="1917875-7",
         omistaja="Peten Koiratarvike Oy on itsenäinen, vuonna 2004 perustettu suomalainen yksityisomisteinen yhtiö (Helsinki, liikevaihto n. 68 M€ 2025), ei osa mitään ketjukonsernia."),
    dict(slug="murren-murkina", nimi="Murren Murkina", domain="murrenmurkina.com", y_tunnus="2010183-7",
         omistaja="Eläintarvike Murren Murkina Oy on 100 % kotimainen yksityinen eläintarvikeliikeketju, joka on erikoistunut koirien ja kissojen luonnonmukaiseen ruokintaan."),
    dict(slug="tassukauppa", nimi="Tassukauppa.fi", domain="tassukauppa.fi", y_tunnus="2263845-1",
         omistaja="Tassukauppa.fi on sastamalalaisen yksityisen elinkeinonharjoittajan Koira- ja kissatarvikeliike Xenaranin (per. 2009) aputoiminimi — suomalainen, ketjuihin kuulumaton kauppa."),
    dict(slug="muotitassu", nimi="Muotitassu", domain="muotitassu.fi", y_tunnus="3299486-3",
         omistaja="Muotitassua pyörittää suomalainen LILALO Oy; design-painotteinen koirien ja kissojen tarvikkeiden verkkokauppa, joka korostaa vastuullisuutta ja hiilineutraaleja toimituksia."),
    dict(slug="koiranurkka", nimi="Koiranurkka", domain="koiranurkka.fi", y_tunnus="1093193-3",
         omistaja="Koiranurkka on Etelä-Savon Polttoainepalvelu Oy:n rekisteröity aputoiminimi (PRH type 3, voimassa) — suomalainen koiraharrastajien verkkokauppa."),
]

# --- hotelliketjut (28.7.2026, Antonin pyyntö, erä 2; tutkimusagentti + PRH) ---
# Radisson+Best Western karsittu (botti-esto 403); Finlandia Hotels karsittu (itsenaisten markkinointiketju).
COMPANIES["hotelliketjut"] = [
    dict(slug="scandic", nimi="Scandic Hotels", domain="scandichotels.com", y_tunnus="1447914-7",
         omistaja="Suomen Scandic-hotelleja operoi Scandic Hotels Oy, jonka omistaa Tukholman pörssissä listattu ruotsalainen Scandic Hotels Group AB."),
    dict(slug="sokos-hotels", nimi="Sokos Hotels", domain="sokoshotels.fi", y_tunnus="0212329-0",
         omistaja="Sokos Hotels on SOK:n ketjubrändi, jonka hotelleja operoivat SOK:n tytäryhtiö Sokotel Oy (Y 0212329-0) ja alueelliset osuuskaupat."),
    dict(slug="lapland-hotels", nimi="Lapland Hotels", domain="laplandhotels.com", y_tunnus="3439760-8",
         omistaja="Suomen suurin yksityinen hotelliketju, joka kuuluu Pertti Yliniemen perheen North European Invest -konserniin (emoyhtiö Lapland Hotels Group Oy; operatiiviset yhtiöt mm. Lapland Hotels Lappi Oy 2199747-9 ja Lapland Hotels City Oy 3432129-1)."),
    dict(slug="omena-hotels", nimi="Omena Hotels", domain="omenahotels.com", y_tunnus="1579157-0",
         omistaja="Omena Hotellit Oy on vaasalaisen Rabbe Grönblomin (Kotipizzan perustaja) perheen omistama itsepalveluhotelliketju, toimitusjohtajana Erno Launo."),
    dict(slug="greenstar-hotels", nimi="GreenStar Hotels", domain="greenstar.fi", y_tunnus="2190146-5",
         omistaja="Greenstar Hotels Oy:n omistavat perustaja-toimitusjohtaja Kristian Ikonen, pääomasijoittaja Nordia Rahasto Oy sekä Bolt.Worksin johtajakolmikko Hakkarainen, Herva ja Hämäläinen."),
    dict(slug="holiday-club", nimi="Holiday Club", domain="holidayclubresorts.com", y_tunnus="2033337-1",
         omistaja="Holiday Club Resorts Oy on kylpylähotelli- ja viikko-osakeyhtiö, jonka enemmistön (noin 92 %) omistaa intialainen Mahindra Holidays & Resorts India Ltd (Mahindra-konserni)."),
]

# --- taksipalvelut (28.7.2026, Antonin pyyntö, erä 2; tutkimusagentti + PRH) ---
# Kovanen karsittu (rikkinainen SSL, Cabonline-brandi jonka FixuTaxi kattaa).
COMPANIES["taksipalvelut"] = [
    dict(slug="taksi-helsinki", nimi="Taksi Helsinki", domain="taksihelsinki.fi", y_tunnus="0838031-9",
         omistaja="Noin 800 helsinkiläisen taksiyrittäjän ja Helsingin Taksiautoilijat ry:n omistama kotimainen yhtiö."),
    dict(slug="meneva", nimi="Menevä", domain="meneva.fi", y_tunnus="0711979-2",
         omistaja="Halmisen perheen omistama kotimainen perheyhtiö (Helsingin Taksipalvelu -tausta), toimitusjohtajana Tuomo Halminen."),
    dict(slug="lahitaksi", nimi="Lähitaksi", domain="lahitaksi.fi", y_tunnus="0220285-3",
         omistaja="Pääkaupunkiseudun taksiyrittäjien omistama tilausvälitysyhtiö, perustettu 1978 (vuoteen 2010 Helsingin Ympäristön Taksikeskus Oy)."),
    dict(slug="02-taksi", nimi="02 Taksi", domain="02taksi.fi", y_tunnus="3217978-9",
         omistaja="02 Taksi on kotimaisen Konnektio Oy:n valtakunnallinen brändi; Konnektio syntyi 020202 Palvelut Oy:n, 02 Taksi Oy:n ja Valopilkku Oy:n fuusiossa 12/2024 ja on suomalaisten taksitoimijoiden omistama."),
    dict(slug="fixutaxi", nimi="FixuTaxi", domain="fixutaxi.fi", y_tunnus="2788104-7",
         omistaja="FixuTaxi on Cabonline Finland Oy:n brändi, osa ruotsalaista Cabonline Groupia (samaan konserniin kuuluu myös Kovanen-brändi)."),
    dict(slug="uber", nimi="Uber", domain="uber.com", y_tunnus="2636362-7",
         omistaja="Yhdysvaltalaisen Uber Technologies Inc:n paikallisyhtiö Uber Finland Oy — ulkomainen kyytisovellusoperaattori, kaupunkeina mm. Helsinki, Tampere ja Turku."),
    dict(slug="bolt", nimi="Bolt", domain="bolt.eu", y_tunnus="3279109-7",
         omistaja="Virolaisen Bolt Technology OÜ:n suomalainen tytäryhtiö Bolt Services FI Oy — ulkomainen kyytisovellusoperaattori useissa Suomen kaupungeissa."),
    dict(slug="kajon", nimi="Kajon", domain="kajon.fi", y_tunnus="1701534-8",
         omistaja="Espoolainen perhetaustainen taksiyhtiö (perustaja Jorma Palomäki); huom. sisaryhtiö Kajon Group ajautui konkurssiin 2020, mutta Kajon Oy (rek. 2001) on PRH:ssa aktiivinen ja jatkaa toimintaa pääkaupunkiseudulla."),
]

# --- kirjakauppojen-verkkokaupat (28.7.2026, Antonin pyyntö, erä 2; tutkimusagentti + PRH) ---
# Kirja.fi (WSOY) karsittu: kustantajan oma kauppa, ei yleiskirjakauppa. Adlibris osti Akateemisen 1.1.2026 (molemmat Bonnier).
COMPANIES["kirjakauppojen-verkkokaupat"] = [
    dict(slug="suomalainen-kirjakauppa", nimi="Suomalainen Kirjakauppa", domain="suomalainen.com", y_tunnus="0205361-6",
         omistaja="Otava-konsernin (Reenpään suvun perheyhtiö) omistama Suomen suurin kirjakauppaketju, jolla on noin 55 myymälää ja Suomalainen.com-verkkokauppa."),
    dict(slug="adlibris", nimi="Adlibris", domain="adlibris.com", y_tunnus="0195663-7",
         omistaja="Ruotsalaisen Bonnier-konsernin Adlibris-ketjun Suomen-yhtiö AdLibris Finland Oy; Pohjoismaiden suurin verkkokirjakauppa, joka osti Akateemisen Kirjakaupan 1.1.2026 alkaen."),
    dict(slug="akateeminen-kirjakauppa", nimi="Akateeminen Kirjakauppa", domain="akateeminen.com", y_tunnus="2699781-4",
         omistaja="1.1.2026 alkaen ruotsalaisen Adlibriksen omistama (saman Bonnier-konsernin sisäinen kauppa marraskuussa 2025; Stockmann myi Bonnierille 2015), oma verkkokauppa ja nimi säilyvät."),
    dict(slug="booky", nimi="Booky.fi", domain="booky.fi", y_tunnus="2131125-4",
         omistaja="Kotimainen perheyhtiö Booky.fi Oy (perustettu 2005/2007), jonka konserniin kuuluvat myös Porvoon Kirjakeskus, Suomen Kirjastopalvelu ja nuottikauppa Ostinato."),
    dict(slug="rosebud", nimi="Rosebud Books", domain="rosebud.fi", y_tunnus="0679141-3",
         omistaja="Itsenäinen helsinkiläinen Rosebud Books Oy (rekisterissä aiemmin nimellä Oy Like Kustannus Ltd), jolla on kivijalkakauppoja ja oma verkkokirjakauppa."),
    dict(slug="karkkainen", nimi="Kärkkäinen", domain="karkkainen.com", y_tunnus="0865108-6",
         omistaja="Perheomisteisen ylivieskalaisen tavarataloyhtiö Kärkkäinen Oy:n (aputoiminimi J. Kärkkäinen) verkkokauppa, jossa kirjat ovat oma yli tuhannen nimikkeen osastonsa — tavaratalo, ei puhdas kirjakauppa."),
]

# --- autoliikkeet (29.7.2026, Antonin pyyntö; PRH v3 + domain-tarkistus) ------
# Delta Auto jätetty pois: deltaauto.fi ei enää vastaa — Delta Auto Oy on
# sulautunut Hedin Automotive Retail Oy:hyn, eli sama omistaja kuin Laakkosella.
# Vaihtoplus (Vehon vaihtoautoketju) jätetty pois: ei omaa elävää sivustoa,
# vaihtoplus.fi ei vastaa — Vehon vaihtoautot mitataan veho.fi:n kautta.
COMPANIES["autoliikkeet"] = [
    dict(slug="kamux", nimi="Kamux", domain="kamux.fi", y_tunnus="2442327-8",
         omistaja="Kamux Oyj (PRH: aktiivinen) on Helsingin pörssiin listattu käytettyjen autojen ketju, joka toimii Suomen lisäksi Ruotsissa ja Saksassa; Suomen liiketoiminnasta vastaa Kamux Suomi Oy."),
    dict(slug="rinta-jouppi", nimi="J. Rinta-Jouppi", domain="rintajouppi.fi", y_tunnus="2045608-0",
         omistaja="J. Rinta-Jouppi on Jarmo Rinta-Jouppi Oy:n (PRH: aktiivinen) aputoiminimi; seinäjokelainen perheyhtiö vuodesta 1987, konserniin kuuluvat myös Rinta-Jouppi Caravan ja Autojouppi."),
    dict(slug="hedin-automotive", nimi="Hedin Automotive", domain="hedinautomotive.fi", y_tunnus="2081088-7",
         omistaja="Hedin Automotive Finland Oy (PRH: aktiivinen, aiempi nimi Veljekset Laakkonen Oy) kuuluu ruotsalaiseen Hedin Mobility Groupiin; samalle omistajalle kuuluu Suomessa myös Delta Auto (Hedin Automotive Retail Oy). Laakkonen-nimi jäi autokaupasta pois: laakkonen.fi on nykyään Laakkonen Kiinteistöt Oy:n sivusto."),
    dict(slug="veho", nimi="Veho", domain="veho.fi", y_tunnus="0115761-6",
         omistaja="Veho Oy Ab (PRH: aktiivinen) on suomalainen autokaupan konserni vuodelta 1939, omistajina Vehon perheomistajat; vaihtoautoja myydään sekä Vehon omilla kauppapaikoilla että Vaihtoplus-konseptilla."),
    dict(slug="saka", nimi="SAKA", domain="saka.fi", y_tunnus="3205932-2",
         omistaja="SAKA Finland Oy (PRH: aktiivinen, aputoiminimet Suomen Autokauppa ja Saka Finland) on kotimainen käytettyjen autojen ketju, joka keskittyy vaihtoautokauppaan ilman merkkiedustuksia."),
    dict(slug="wetteri", nimi="Wetteri", domain="wetteri.fi", y_tunnus="0548170-4",
         omistaja="Wetteri Oyj (PRH: aktiivinen) on Helsingin pörssiin listattu pohjoissuomalainen autotalokonserni, joka myy sekä uusia että käytettyjä autoja usealla paikkakunnalla."),
    dict(slug="autokeskus", nimi="Autokeskus", domain="autokeskus.fi", y_tunnus="1093812-3",
         omistaja="Autokeskus Oy (PRH: aktiivinen, aputoiminimi AK-Outlet) on pääkaupunkiseudulla, Tampereella ja Turussa toimiva autotaloketju, joka myy uusia ja vaihtoautoja sekä ylläpitää AK-Outlet-vaihtoautomyymälöitä."),
    # hartikainen KARSITTU 2.8.2026: E. Hartikainen Oy myi koko autokauppaliiketoimintansa
    # Wetteri Oyj:lle 8.3.2023 (34,4 M€). hartikainen.com on nyt maarakennusyhtiön sivusto —
    # autokauppa poistunut kokonaan; /vaihtoautot 404. Wetteri on jo listassa.
]

# --- pikaruokaketjut (29.7.2026, Antonin pyyntö; PRH v3 + domain-tarkistus) ---
# Subway jätetty pois: subway.fi ohjaa subway.com/fi-fi-sivulle, joka ei vastaa
# mittaukseen (yhteys katkeaa) — mittausaukko, ei väite puuttuvasta tiedosta.
# Pancho Villa ja Pizza Hut jätetty pois: panchovilla.fi vastaa 403 (botti-esto)
# eikä Pizza Hutin Suomen operaattoria voitu varmistaa PRH:sta.
COMPANIES["pikaruokaketjut"] = [
    dict(slug="hesburger", nimi="Hesburger", domain="hesburger.fi", y_tunnus="0845504-2",
         omistaja="Hesburger on Burger-In Oy:n (PRH: aktiivinen) ketju; salolainen Harri ja Kirsti Ljungqvistin perheyhtiö vuodesta 1980, Suomen laajin pikaruokaketju."),
    dict(slug="mcdonalds", nimi="McDonald's", domain="mcdonalds.fi", y_tunnus="2779836-6",
         omistaja="McDonald's-ravintoloista Suomessa vastaa Food Folk Suomi Oy (PRH: aktiivinen), joka osti Pohjoismaiden McDonald's-liiketoiminnan vuonna 2017; brändi on yhdysvaltalaisen McDonald's Corporationin."),
    dict(slug="kotipizza", nimi="Kotipizza", domain="kotipizza.fi", y_tunnus="0548483-3",
         omistaja="Kotipizza Oyj (PRH: aktiivinen) on Suomen suurin pizzaketju; omistaja on norjalainen Orkla ASA, ja ravintolat toimivat yrittäjävetoisina franchising-ravintoloina."),
    dict(slug="burger-king", nimi="Burger King", domain="burgerking.fi", y_tunnus="2538302-8",
         omistaja="Burger Kingin Suomen ravintoloista vastaa Restel Fast Food Oy (PRH: aktiivinen), joka kuuluu Osuuskunta Tradekan omistamaan Resteliin; sama yhtiö operoi myös Taco Bellia Suomessa."),
    dict(slug="taco-bell", nimi="Taco Bell", domain="tacobell.fi", y_tunnus="2538302-8",
         omistaja="Taco Bellin Suomen ravintoloista vastaa Restel Fast Food Oy (PRH: aktiivinen) eli sama Tradekan omistama yhtiö kuin Burger Kingin; osa ravintoloista toimii yhteisravintoloina Burger Kingin kanssa."),
    dict(slug="rax", nimi="Golden Rax", domain="rax.fi", y_tunnus="1572598-7",
         omistaja="Golden Rax Pizzabuffet on Rax Ravintolat Oy:n (PRH: aktiivinen) ketju, joka kuuluu Osuuskunta Tradekan omistamaan Restel-konserniin — sama omistaja kuin Burger Kingillä ja Taco Bellilla."),
    dict(slug="fafas", nimi="Fafa's", domain="fafas.fi", y_tunnus="2442719-9",
         omistaja="Fafa's on Fafa's Plats Oy:n (PRH: aktiivinen) kotimainen pitaketju vuodelta 2011; ravintolat toimivat pääosin franchising-periaatteella."),
    dict(slug="sibylla", nimi="Sibylla", domain="sibylla.fi", y_tunnus="1731965-9",
         omistaja="Sibylla-konseptista Suomessa vastaa Atria Concept Oy (PRH: aktiivinen, aputoiminimi Sibylla), joka kuuluu suomalaiseen Atria Oyj:hyn; ravintolat toimivat huoltoasemien ja kauppojen yhteydessä."),
]

# PAKETTIPALVELUT (2.8.2026) — kuluttajan kotimaiset ja kansainväliset pakettipalvelut.
# POISSULJETUT: UPS (pääosin B2B Suomessa; kuluttajapalvelu epäselvä); FedEx (kansainv.
# pikarahti, ei kuluttajan kotimaanlähetyksiä); Instabox/Budbee (Suomen toiminta
# epäselvä 8/2026). DSV (ent. DB Schenker): dbschenker.com ohjaa nyt dsv.com/fi-fi/;
# DSV osti DB Schenkerin Deutsche Bahn AG:lta 30.4.2025 (14,3 Mrd EUR); Schenker Oy
# (Y: 0124239-4) on edelleen Finnish entity DSV:n tytäryhtiönä; brändi = DSV.
COMPANIES["pakettipalvelut"] = [
    dict(slug="posti", nimi="Posti", domain="posti.fi", y_tunnus="0109357-9",
         omistaja="Posti Jakelu Oy — Suomen valtio omistaa Posti Group Oyj:n (100 %); Suomen postipalveluiden pääoperaattori"),
    dict(slug="matkahuolto", nimi="Matkahuolto", domain="matkahuolto.fi", y_tunnus="0111393-9",
         omistaja="Oy Matkahuolto Ab — suomalaisten linja-autoyritysten omistama, perustettu 1933; pakettipalvelut toimivat linja-autoasema- ja sopimusverkostossa"),
    dict(slug="postnord", nimi="PostNord", domain="postnord.fi", y_tunnus="1056251-7",
         omistaja="PostNord Oy — PostNord AB:n (Tanska 40 %, Ruotsi 60 %) suomalainen tytäryhtiö"),
    dict(slug="dhl", nimi="DHL", domain="dhl.com", y_tunnus="2717767-4",
         omistaja="DHL Express (Finland) Oy — osa Deutsche Post DHL -konsernia (Saksa); Suomen verkkosivusto dhl.com/fi-fi on yritysasiakkaille suunnattu — kotimaan kuluttajareklamaatiot ohjataan Postin sivuille"),
    dict(slug="gls", nimi="GLS", domain="gls-group.com", y_tunnus="1739617-9",
         omistaja="General Logistics Systems Finland Oy — osa GLS Group -konsernia; omistaja International Distributions Services plc (UK, ent. Royal Mail Group)"),
    # DSV HUOM: db Schenkerin kuluttajasivu ohjautuu nyt dsv.com/fi-fi/. DSV on B2B-painotteinen
    # mutta tarjoaa myös kuluttajapalvelun (Kuluttajat-osio dsv.com/fi-fi/). Mittaus julkisesta
    # sivusta on mahdollinen; tulos todennäköisesti heikko kuluttajaläpinäkyvyydessä.
    dict(slug="dsv", nimi="DSV", domain="dsv.com", y_tunnus="0124239-4",
         omistaja="Schenker Oy — DSV A/S:n (Tanska) tytäryhtiö; Deutsche Bahn myi DB Schenkerin DSV:lle 30.4.2025; domain vaihtunut dbschenker.com -> dsv.com"),
]

# MUSIIKKIPALVELUT (3.8.2026) — musiikin kuuntelun tilauspalvelut Suomessa.
# Globaalit toimijat, vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen.
# POISSULJETUT:
#   Tidal (tidal.com): koko domain palauttaa 403 myos JS-renderoinnilla (kuten McAfee/IKH).
#   Napster: on pivotoitunut AI-agenttiyhtioksi, ei enaa musiikkistriimausta.
#   SoundCloud Go+: soundcloud.com/go palauttaa HTTP 000; suomi-sivu ei tavoitettavissa.
#   Amazon Music: music.amazon.fi ei ole olemassa; music.amazon.com on sisäänkirjautumisportti
#     ilman julkista hinnoittelua — ei mitattavissa kuluttajalle suunnatun hintatiedon osalta.
COMPANIES["musiikkipalvelut"] = [
    dict(slug="spotify", nimi="Spotify", domain="spotify.com", y_tunnus=None,
         omistaja="Spotify AB (Ruotsi) — porssiyhtion NYSE: SPOT; maailman suurin musiikkistriimaamo"),
    dict(slug="apple-music", nimi="Apple Music", domain="music.apple.com", y_tunnus=None,
         omistaja="Apple Inc. (Yhdysvallat) — tilaussivu apple.com/fi/apple-music/; music.apple.com on web-soitin"),
    dict(slug="youtube-music", nimi="YouTube Music", domain="music.youtube.com", y_tunnus=None,
         omistaja="Alphabet Inc. / Google LLC (Yhdysvallat) — sisaltyy YouTube Premium -tilaukseen"),
    dict(slug="deezer", nimi="Deezer", domain="deezer.com", y_tunnus=None,
         omistaja="Deezer SA (Ranska) — porssiyhtion Euronext: DEEZR; suomenkielinen palvelu deezer.com/fi"),
    dict(slug="qobuz", nimi="Qobuz", domain="qobuz.com", y_tunnus=None,
         omistaja="Xandrie SA (Ranska) — yksityisomisteinen; erikoistunut hi-res/lossless-aanentoistoon; palvelu Suomessa qobuz.com/fi-en"),
    dict(slug="amazon-music", nimi="Amazon Music", domain="music.amazon.com", y_tunnus=None,
         omistaja="Amazon.com, Inc. (Yhdysvallat); Amazon Music Unlimited saatavilla Suomessa amazon.de-kautta; music.amazon.com on web-soitin"),
]

# --- kauneustuotteet-verkkokaupat (3.8.2026, autopilot-tikki; PRH v3 + domain-tarkistus) ---
# Notino.fi KARSITTU: Cloudflare 403 myos selain-UA:lla — ei mitattavissa.
# Lookfantastic.fi KARSITTU: ohjautuu eu.lookfantastic.com (englanti, ei suomalaista sisaltoa).
# Douglas.fi KARSITTU: domain vastaa 200:lla mutta palauttaa 0 tavua — sivusto tyhja/kuollut.
# Parfym Sverige AB:n kaksi Suomi-branssia: parfym.fi (kaikki kategoriat) ja hajuvesi.fi
#   (vain tuoksut) — SAME_COMPANY, sisarsivustoja; mitataan vain parfym.fi.
# NordicFeel: eleven.fi on virallinen fi-domain joka ohjaa nordicfeel.com/fi-sivulle.
# Cocopanda: kaksi PRH-entriaa (Cocopanda.fi Oy Ab 2718362-8 ja norjalaisen Blivakker &
#   Cocopanda Retail AS Suomen Sivuliike 3515859-6) — yhtio myytaneen tai yhtiokookiratkaisut;
#   verkkosivusta vastaa Cocopanda.fi Oy Ab.
COMPANIES["kauneustuotteet-verkkokaupat"] = [
    dict(slug="lyko", nimi="Lyko", domain="lyko.com", y_tunnus=None,
         omistaja="Lyko Group AB (Ruotsi, per. 1974) operoi lyko.com/fi-suomenkielista verkkokauppaa; ei suomalaista Y-tunnusta. Ruotsalainen porssilistaamaton perheyhtiö (Kungsbacka)."),
    dict(slug="bangerhead", nimi="Bangerhead", domain="bangerhead.fi", y_tunnus="2607224-8",
         omistaja="Bangerhead AB filial i Finland (PRH: aktiivinen) on ruotsalaisen Bangerhead AB:n Suomen sivuliike; Bangerhead AB perustettiin 2009 Tukholmassa."),
    dict(slug="cocopanda", nimi="Cocopanda", domain="cocopanda.fi", y_tunnus="2718362-8",
         omistaja="Cocopanda.fi Oy Ab (PRH: aktiivinen, per. 2015) on Suomessa rekisteroity verkkokauppayhtion; liittyy myos norjalaiseen Blivakker & Cocopanda Retail AS:aan, jonka Suomen Sivuliike (Y: 3515859-6) on myos rekisteroity."),
    dict(slug="kicks", nimi="KICKS", domain="kicks.fi", y_tunnus="2061510-9",
         omistaja="Kicks Kosmetikkedjan Oy (PRH: aktiivinen, per. 2006) on ruotsalaisen KICKS-ketjun Suomen tytäryhtiö; KICKS on Scandinavian Beauty Group AB:n brändi."),
    dict(slug="parfymfi", nimi="Parfym.fi", domain="parfym.fi", y_tunnus=None,
         omistaja="Parfym.fi:ta operoi ruotsalainen Parfym Sverige AB (org.nr 556705-2799); sisarsivusto hajuvesi.fi on sama kauppa eri domainilla; ei suomalaista Y-tunnusta."),
    dict(slug="nordicfeel", nimi="NordicFeel", domain="eleven.fi", y_tunnus=None,
         omistaja="NordicFeel AB (Ruotsi) operoi eleven.fi-suomalaisdomain kautta nordicfeel.com/fi-sivustoa; Pohjoismainen kauneusverkkokauppa, yli 3 milj. asiakasta; ei suomalaista Y-tunnusta."),
]

# --- pelitilauspalvelut (3.8.2026; autopilot-tikki) ---
# Kaikki globaaleja toimijoita, vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen.
# POISSULJETUT:
#   PC Game Pass / Xbox Game Pass PC: sama tilaus kuin Xbox Game Pass (nyk. Game Pass Standard/Ultimate),
#     ei erillinen tuote — mitataan yhden Xbox-merkinnän alla.
#   GeForce Now (nvidia.com): pilvistriimaamo ei pelitilauspalvelu — ei sisallyta.
#   Amazon Luna: ei saatavilla Suomessa (EU-julkaisu tapahtumaton elokuuhun 2026 mennessa).
COMPANIES["pelitilauspalvelut"] = [
    dict(slug="xbox-game-pass", nimi="Xbox Game Pass", domain="xbox.com", y_tunnus=None,
         omistaja="Microsoft Corporation (Yhdysvallat, NASDAQ: MSFT) — pelitilauspalvelu saatavilla xbox.com/fi-fi; taso-vaihtoehdot Game Pass Standard ja Game Pass Ultimate (sis. EA Play)"),
    dict(slug="playstation-plus", nimi="PlayStation Plus", domain="playstation.com", y_tunnus=None,
         omistaja="Sony Interactive Entertainment LLC (Yhdysvallat) — tytäryhtiö Sony Group Corporation (Japani, TSE: 6758); Suomi-sivu store.playstation.com/fi-fi"),
    dict(slug="nintendo-switch-online", nimi="Nintendo Switch Online", domain="nintendo.fi", y_tunnus=None,
         omistaja="Nintendo Co., Ltd. (Japani, TSE: 7974) — ainoa listattu pelitilauspalvelu, jolla on suomenkielinen verkkotunnus (nintendo.fi); tilaussivu nintendo.fi/nintendo-switch-perhe/nintendo-switch-online"),
    dict(slug="ea-play", nimi="EA Play", domain="ea.com", y_tunnus=None,
         omistaja="Electronic Arts Inc. (Yhdysvallat, NASDAQ: EA) — Suomi-sivu ea.com/fi-fi; EA Play on EA:n oma tilauspalvelu, sisaltyy myos Xbox Game Pass Ultimate -tilaukseen"),
    dict(slug="ubisoft-plus", nimi="Ubisoft+", domain="ubisoft.com", y_tunnus=None,
         omistaja="Ubisoft Entertainment SA (Ranska, Euronext: UBI) — Suomi-sivu ubisoft.com/fi-fi; Ubisoft+ Classic ja Ubisoft+ Premium kaksi tasoa"),
    dict(slug="apple-arcade", nimi="Apple Arcade", domain="apple.com", y_tunnus=None,
         omistaja="Apple Inc. (Yhdysvallat, NASDAQ: AAPL) — Suomi-sivu apple.com/fi/apple-arcade; yksi kiintea kuukausihinta, ei tasoja"),
]

# --- aanikirjapalvelut (3.8.2026; autopilot-tikki) ---
# Kaikki globaaleja toimijoita, vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen.
# POISSULJETUT:
#   Audible (audible.fi / audible.com): ei suomenkielistä markkinaa — Amazonia ei ole
#     avannut Suomea omana alueena; audible.fi ei vastaa (HTTP 000). Lähimmät EU-sivustot
#     (audible.co.uk, audible.de) ovat englanti-/saksankielisiä eikä niillä ole
#     suomenkielistä sisältöä tai hinnoittelua.
#   Elisa Kirja (kirja.elisa.fi): domain ei vastaa (HTTP 000) — palvelu lakkautettu.
#   Fabel (fabel.fi): domain ei vastaa (HTTP 000) — palvelu poistunut Suomen markkinalta.
#   Scribd (scribd.com): kansainvalinen palvelu ilman suomenkielistä sivustoa tai
#     hinnoittelua euroissa — ei vertailukelpoinensuomalaiselle kuluttajalle.
#   Blinkist (blinkist.com): kirjojen lyhennelmät, ei kokonaiset äänikirjat — eri kategoria.
# HUOM Spotify: Spotify on mitattu myos musiikkipalvelut-kategoriassa. Tassa kategoriassa
#   mitataan Spotifyn aanikritjapalvelu-ominaisuus erikseen: Premium-tilaukseen kuuluva
#   15 h/kk aanikuunteluaika, yli 150 000 äänikirjaa, erillinen osta-kapasiteettirajoituksen
#   ylitys. spotify.com/fi/audiobooks/ on Spotifyn oma suomenkielinen äänikirjasivu.
COMPANIES["aanikirjapalvelut"] = [
    dict(slug="storytel", nimi="Storytel", domain="storytel.com", y_tunnus=None,
         omistaja="Storytel AB (Ruotsi) — pörssilistattu Nasdaq Stockholm: STORY A/STORY B; maailman suurimpia äänikirjapalveluja yli miljoonalla nimikkeellä; Suomi-sivu storytel.com/fi"),
    dict(slug="bookbeat", nimi="BookBeat", domain="bookbeat.com", y_tunnus=None,
         omistaja="BookBeat AB (Ruotsi) — Bonnier Books AB:n kokonaan omistama tytäryhtiö; Bonnier on ruotsalainen yksityinen mediakonserni; Suomi-sivu bookbeat.com/fi"),
    dict(slug="nextory", nimi="Nextory", domain="nextory.com", y_tunnus=None,
         omistaja="Nextory AB (Ruotsi) — yksityisomisteinen pohjoismainen äänikirja- ja e-kirjapalvelu, perustettu 2019 Tukholmassa; Suomi-sivu nextory.com/fi"),
    dict(slug="kobo", nimi="Kobo", domain="kobo.com", y_tunnus=None,
         omistaja="Rakuten Kobo Inc. (Kanada) — japanilaisen Rakuten Group, Inc.:n (Tokyo Stock Exchange: 4755) tytäryhtiö; Kobo Plus Listen -tilaus sisältää äänikirjoja; Suomi-sivu kobo.com/fi/fi"),
    dict(slug="podimo", nimi="Podimo", domain="podimo.com", y_tunnus=None,
         omistaja="Podimo ApS (Tanska) — yksityisomisteinen, perustettu 2019 Kööpenhaminassa; tarjoaa sekä podcasteja että äänikirjoja; Suomi-sivu podimo.com/fi"),
    dict(slug="spotify-audiobooks", nimi="Spotify", domain="spotify.com", y_tunnus=None,
         omistaja="Spotify AB (Ruotsi) — pörssilistattu NYSE: SPOT; Premium-tilaukseen kuuluu 15 h/kk äänikirjakuuntelua; Suomi-sivu spotify.com/fi/audiobooks/"),
]

# ---------------------------------------------------------------------------
# KYLPYLÄT — 6 suomalaista kylpylää/vesipuistoa, tarkistettu 3.8.2026.
# Kaikki tarjoavat päivälipun tai vastaavan kuluttajapääsyn, toimivat vähintään
# kahdella paikkakunnalla tai ovat valtakunnallisesti tunnettuja.
# EXCLUDED: HaVen Ylläs (Holiday Club Resorts Oy:n kohde — SAME_COMPANY Holiday
#   Clubin kanssa); Virkistyshotelli Yyteri (toimii, mutta 6 riittää edustamaan
#   markkinaa); Imatran Kylpylä, Peurunka kylpylähotelli, Rauhalahti jne. (Suomalaiset
#   Kylpylät ry:n listalla, mutta alla on jo 6 hyvää kohdetta).
# OMISTUS: Serena = Puuharyhmä Oyj (espanjalainen Aspro Ocio S.A. omistaa);
#   Naantalin Kylpylä = Naantalin Kylpylänranta Oy, Sunborn Hotels & Restaurants.
COMPANIES["kylpylat"] = [
    dict(slug="holiday-club", nimi="Holiday Club Resorts", domain="holidayclubresorts.com",
         y_tunnus="2033337-1",
         omistaja="Holiday Club Resorts Oy — Suomen suurin kylpyläketju; kohteet mm. Saimaa, Caribia (Turku), Kuusamon Tropiikki, Ylläs, Saariselkä, Tampereen Kehräämö"),
    dict(slug="serena", nimi="Serena", domain="serena.fi",
         y_tunnus="0564528-9",
         omistaja="Puuharyhmä Oyj — espanjalaisen Aspro Ocio S.A.:n omistama; Suomen ja Pohjoismaiden suurin vesipuisto, Espoo"),
    dict(slug="flamingo-spa", nimi="Flamingo Spa", domain="flamingospa.fi",
         y_tunnus="2029086-9",
         omistaja="Flamingospa Oy — Vantaa, kauppakeskus Jumbon yhteydessä; yksi Pohjoismaiden suurimmista sisäkylpylöistä"),
    dict(slug="ikaalinen-spa", nimi="Ikaalinen Spa & Resort", domain="ikaalinenspa.fi",
         y_tunnus="3186123-3",
         omistaja="Ikaalinen Spa Oy — Ikaalisissa Kyrösjärven rannalla; uusi paikallisomisteinen operaattori vuodesta 2021"),
    dict(slug="naantali-spa", nimi="Naantalin Kylpylä", domain="naantalispa.fi",
         y_tunnus="1711966-5",
         omistaja="Naantalin Kylpylänranta Oy (Sunborn Hotels & Restaurants) — Naantali; ei kuulu Holiday Club -ketjuun"),
    dict(slug="peurunka", nimi="Peurunka", domain="peurunka.fi",
         y_tunnus="0176471-5",
         omistaja="Peurunka Oy — Laukaassa Peurunkajärven rannalla, noin 30 km Jyväskylästä; Suomalaiset Kylpylät ry:n jäsen"),
]

# ---------------------------------------------------------------------------
# LENTOYHTIÖT — 6 Suomesta säännöllisesti lentävää yhtiötä, tarkistettu 3.8.2026.
# Kaikki globaaleja toimijoita, vpn-palvelut-konventio: omistaja_kerrottu korvaa y_tunnuksen.
# Finnair on ainoa suomalainen, Y-tunnus 0108023-3 (Finnair Oyj, PRH-tarkistettu 3.8.2026).
# POISSULJETUT:
#   easyJet (easyjet.com/fi/): 404 — ei suomalaista sivustoa; lentää SUOMEEN ei SUOMESTA
#     säännöllisesti; Helsinki on saapumiskohde, ei lähtöasema easyJetin reittiverkostossa.
#   Lufthansa (lufthansa.com/fi): Cloudflare-esto; B2B-painotus eikä suomenkielistä sivustoa.
#   KLM (klm.com): Cloudflare 403 myös --js:llä; ei suomenkielistä sivustoa.
#   Turkish Airlines (turkishairlines.com/fi-fi/): HTTP 000 kaikilla hakumetodeilla — ei
#     mitattavissa.
#   British Airways: ei suomenkielistä sivua eikä suoria lentoja Suomesta.
#   Wizz Air vaihtoehto: LENTÄÄ Turusta (Turku–Vilnius, Turku–Bukarest, Turku–Gdańsk)
#     vaikka wizzair.com/fi-FI → 404; globaali .com toimii, riittää mittaukseen.
# SAS HUOM: flysas.com/fi-fi --raw hakeminen ohjaa fi-en (englanninkielinen FI-versio);
#   data-country="FI" vahvistaa Suomen markkinan; ei suomenkielistä käyttöliittymää.
# airBaltic HUOM: airbaltic.com/en-fi/ — englanninkielinen mutta Suomen lentoasemapainotus;
#   lentää 6 suomalaiselta lentoasemalta (Helsinki, Tampere, Turku, Oulu, Kittilä, Kuusamo).
COMPANIES["lentoyhtiot"] = [
    dict(slug="finnair", nimi="Finnair", domain="finnair.com",
         y_tunnus="0108023-3",
         omistaja="Finnair Oyj — Suomen valtio omistaa noin 56 % osakkeista; Helsinki-Vantaalta yli 80 kohteeseen; pörssilistattu Nasdaq Helsinki: FIA1S"),
    dict(slug="norwegian", nimi="Norwegian", domain="norwegian.com", y_tunnus=None,
         omistaja="Norwegian Air Shuttle ASA (Norja) — pörssilistattu Oslo Børs: NAS; lentää usealta suomalaiselta lentoasemalta; Suomi-sivu norwegian.com/fi/"),
    dict(slug="ryanair", nimi="Ryanair", domain="ryanair.com", y_tunnus=None,
         omistaja="Ryanair DAC (Irlanti) — pörssilistattu Nasdaq Dublin / London Stock Exchange: RYA; Euroopan matkustajamääriltään suurin lentoyhtiö; lentää mm. Helsingistä ja Rovaniemeltä; Suomi-sivu ryanair.com/fi/fi"),
    dict(slug="flysas", nimi="SAS", domain="flysas.com", y_tunnus=None,
         omistaja="SAS AB (Ruotsi/Tanska/Norja) — uudelleenjärjestelty 2024; Castlelake L.P. ja Air France-KLM suurimpia omistajia; Suomen sivu flysas.com/fi-fi (englanninkielinen FI-versio)"),
    dict(slug="airbaltic", nimi="airBaltic", domain="airbaltic.com", y_tunnus=None,
         omistaja="airBaltic Corporation AS (Latvia) — pörssilistattu Nasdaq Riga: BTC1R; Latvian valtio suurin omistaja; lentää 6 suomalaiselta lentoasemalta (Helsinki, Tampere, Turku, Oulu, Kittilä, Kuusamo); Suomi-sivu airbaltic.com/en-fi/"),
    dict(slug="wizzair", nimi="Wizz Air", domain="wizzair.com", y_tunnus=None,
         omistaja="Wizz Air Holdings Plc (Unkari) — pörssilistattu London Stock Exchange: WIZZ; lentää Turun lentoasemalta (Vilna, Bukarest, Gdańsk); globaali sivu wizzair.com"),
]

# ---------------------------------------------------------------------------
# KIRJANPITO-OHJELMISTOT — 6 pk-yrityksille suunnattua taloushallinto-ohjelmistoa,
# tarkistettu 4.8.2026. Kaikki suomalaisrekisteröityjä yhtiöitä (Y-tunnus tiedossa).
# Netvisorilla norjalainen Visma-omistus; Holvilla espanjalainen BBVA-omistus —
# omistajuus kerrotaan sivulla avoimesti.
# POISSULJETUT:
#   Passeli Merit (passeli.fi): meritaktiva.fi ohjautuu /passelimerit-sivulle — yhtiön
#     y-tunnusta ei löydetty PRH:sta nimellä "Passeli Oy"; jätetään pois.
#   Tikon (tikon.fi): Accountor Group -tuote, sama konserni kuin Procountor —
#     SAME_COMPANY-este, ei voida mitata erikseen.
#   Fivaldi (fivaldi.fi): Visma Solutions Oy:n tuote, sama yhtiö kuin Netvisor —
#     SAME_COMPANY-este.
#   Heeros (heeros.com): suunnattu tilitoimistoille, ei yrittäjän itsensä valittavaksi.
COMPANIES["kirjanpito-ohjelmistot"] = [
    dict(slug="procountor", nimi="Procountor", domain="procountor.fi",
         y_tunnus="0836922-4",
         omistaja="Finago Oy (ent. Accountor Finago Oy, nimi muuttui 19.11.2025) — Accountor Group -konsernin omistama; pilvipalvelu kirjanpitoon, palkanlaskentaan ja laskutukseen"),
    dict(slug="netvisor", nimi="Netvisor", domain="netvisor.fi",
         y_tunnus="1967543-8",
         omistaja="Visma Solutions Oy (ent. Netvisor Oy) — norjalainen Visma Group -konserni omistaa; pilvipohjainen ERP- ja taloushallinto-ohjelmisto"),
    dict(slug="fennoa", nimi="Fennoa", domain="fennoa.com",
         y_tunnus="2593931-3",
         omistaja="Fennoa Oy (ent. BIS Network Oy) — suomalainen; pilvikirjanpito-ohjelmisto erityisesti pienyrityksille ja yrittäjille"),
    dict(slug="holvi", nimi="Holvi", domain="holvi.com",
         y_tunnus="2193756-4",
         omistaja="Holvi Payment Services Oy — BBVA S.A. (Espanja) omistaa; yritystili ja valmisteleva kirjanpito yksinyrittäjille ja pk-yrityksille; holvi.com/fi/"),
    dict(slug="kitsas", nimi="Kitsas", domain="kitsas.fi",
         y_tunnus="3093902-7",
         omistaja="Kitsas Oy — suomalainen avoimen lähdekoodin kirjanpito-ohjelmisto; ilmaisversio + maksullinen pilvipalvelu"),
    dict(slug="lemonsoft", nimi="Lemonsoft", domain="lemonsoft.fi",
         y_tunnus="2017863-1",
         omistaja="Lemonsoft Oyj — suomalainen, pörssilistattu Nasdaq First North (2021); ERP + taloushallinto pk-yrityksille; tuotenimiä: WorkIn, Käyttösofta"),
]

# ---------------------------------------------------------------------------
# KAHVILAKETJUT — 6 valtakunnallista kahvila- tai pikapalveluketjua,
# tarkistettu 4.8.2026.
# POISSULJETUT:
#   Wayne's Coffee: poistui Suomesta 2012.
#   Starbucks: starbucks.fi ei ole olemassa (HTTP 000); kansainvälinen
#     starbucks.com ei suomenkielinen eikä fi-kotisivu; BFI ilmoitti 2024
#     laajentavansa Pohjoismaihin, mutta Suomessa ei toistaiseksi omia toimipisteitä.
#   Coffee House: coffeehouse.fi ohjautuu raflaamo.fi-alustalle (S-Group);
#     ei omaa erillistä verkkosivua — karsittu domainongelman vuoksi.
COMPANIES["kahvilaketjut"] = [
    dict(slug="espresso-house", nimi="Espresso House", domain="espressohouse.com",
         y_tunnus="2663296-2",
         omistaja="Espresso House Finland Oy — ruotsalaisen Espresso House AB:n omistama; 65+ toimipaikkaa Suomessa; fi-sivu fi.espressohouse.com"),
    dict(slug="roberts-coffee", nimi="Robert's Coffee", domain="robertscoffee.com",
         y_tunnus=None,
         omistaja="Gilvaria Oy (Robert's Coffee Suomessa; franchise-ketju; pääkonttori Sienikuja 6, 00760 Helsinki; Y-tunnus ei löytynyt suoraan sivustolta)"),
    dict(slug="arnolds", nimi="Arnolds", domain="arnolds.fi",
         y_tunnus="0864440-9",
         omistaja="Hermen Oy — brändin ja konseptin omistaja; franchise-pohjainen ketju; perustettu 1991; 30+ toimipaikkaa"),
    dict(slug="fazer-cafe", nimi="Fazer Café", domain="fazer.fi",
         y_tunnus="0202669-3",
         omistaja="Oy Karl Fazer Ab — suomalainen perheyhtiö; Fazer Café on Fazer Foodservices -yksikön ketju; 24+ toimipaikkaa pääkaupunkiseudulla, Turussa ja Tampereella; lippulaiva Karl Fazer Café avattu 1891"),
    dict(slug="picnic", nimi="Picnic", domain="picnic.fi",
         y_tunnus="0789907-1",
         omistaja="Picnic Finland Oy — suomalainen; perustettu 1991; noin 40 ravintolaa yli 15 kaupungissa; patonki-, uuniperunat- ja salaattiketju, jossa kahvi on keskeinen tuote"),
    dict(slug="coffee-house", nimi="Coffee House", domain="coffeehouse.fi",
         y_tunnus=None,
         omistaja="Restamax Oyj / Eateria Oy (ketju-omistaja ei vahvistettavissa PRH:sta suoraan; aiemmin S-Group, nyt Restamax-konsernin alla); 15 toimipaikkaa; coffeehouse.fi ohjautuu raflaamo.fi-alustalle"),
]

# --- era 17 (4.8.2026): muotikaupat (aikuisten vaatteiden verkkokaupat) -----
# Vertailtavat: kansainväliset ja pohjoismaiset muotiverkkokaupat, jotka palvelevat
# suomalaisia kuluttajia omilla fi-sivustoillaan tai fi-kielisillä sivuillaan.
# KARSITUT:
# Lindex (lindex.com/fi): Akamai-estetty täysin — kaikki polut 403. Yli 3 kokonaan
#   estettyjä yhtiöitä samassa kategoriassa heikentäisi vertailun luotettavuutta.
# Nelly (nelly.com/fi): elossa ja toimiva, mutta ei yhtä iso fi-markkina-asema
#   kuin Zalando tai H&M; karsittu 6:n yhtiön rajoituksella.
# Vero Moda (veromoda.com/fi-fi): naisten muotiin erikoistunut; mukana Boozt-valikoimassa;
#   Bestseller Group omistaa myös Jack & Jones, ONLY, Pieces — laske vain yksi.
# Zara (zara.com/fi): 0 tavua — täysin JS-renderöity, ei mitattavissa selain-UA:lla.
# Mango (mango.com/fi/fi): ohjautuu UK-sivustolle, ei suomenkielistä sisältöä.
# H&M Group omistaa H&M + COS + Monki + Weekday — lasketaan vain H&M (suurin fi-toimija).
# Inditex omistaa Zara + Mango + Massimo Dutti — lasketaan vain Zara, joka on kuitenkin
#   täysin estetty boteille, joten ei sisällytetä.
COMPANIES["muotikaupat"] = [
    dict(slug="zalando", nimi="Zalando", domain="zalando.fi",
         y_tunnus="2697196-4",
         omistaja="Zalando Finland Oy (PRH 2697196-4) on saksalaisen Zalando SE:n (Frankfurt: ZAL) Suomen tytäryhtiö; Euroopan suurin muodin verkkokauppa; yli 2 miljoonaa tuotetta; zalando.fi on suomenkielinen domain"),
    dict(slug="hm", nimi="H&M", domain="www2.hm.com",
         y_tunnus="1080854-8",
         omistaja="H & M Hennes & Mauritz Oy (PRH 1080854-8) on ruotsalaisen H & M Hennes & Mauritz AB:n (Nasdaq Stockholm: HM B) Suomen tytäryhtiö; H&M Group omistaa myös COS, Monki, Weekday — vain H&M mitataan; fi-sivu www2.hm.com/fi_fi/"),
    dict(slug="boozt", nimi="Boozt", domain="boozt.com",
         y_tunnus=None,
         omistaja="Boozt AB (Ruotsi, Nasdaq Stockholm: BOOZT) — ei suomalaista tytäryhtiötä PRH:ssa; pohjoismainen muodin verkkokauppa, perustettu 2007 Malmössa; suomenkielinen palvelu boozt.com/fi/fi"),
    dict(slug="kappahl", nimi="KappAhl", domain="kappahl.com",
         y_tunnus="0758506-4",
         omistaja="KappAhl Oy (PRH 0758506-4) on ruotsalaisen KappAhl AB:n (Nasdaq Stockholm: KAHL) Suomen tytäryhtiö; perustettu 1953 Göteborgissa; myymälöitä ja verkkokauppa Suomessa; fi-sivu kappahl.com/fi-fi/"),
    dict(slug="cubus", nimi="Cubus", domain="cubus.com",
         y_tunnus="2379502-9",
         omistaja="Cubus Finland Oy Ab (PRH 2379502-9) on norjalaisen Varner AS:n (Varner-konserni) omistaman Cubus AS:n Suomen tytäryhtiö; Varner omistaa myös Dressmann, Bik Bok, Volt — vain Cubus mitataan; fi-sivu cubus.com/fi/"),
    dict(slug="ellos", nimi="Ellos", domain="ellos.fi",
         y_tunnus="1442131-6",
         omistaja="Ellos Finland Oy (PRH 1442131-6) on ruotsalaisen Ellos Group AB:n Suomen tytäryhtiö; postimyyntiyhtiönä perustettu 1947, nykyisin monialainen muoti- ja lifestyleverkkokauppa; liikevaihto 35,2 M€ (2024)"),
]

# SÄHKÖAUTOJEN LATAUS (4.8.2026) — sähköauton julkiset latauspalvelut Suomessa.
# POISSULJETUT:
# Virta (virta.fi): B2B-latausalusta (SaaS yrityksille latauspisteverkostojen hallintaan);
#   kuluttajasivu ohjaa yritysmyyntiin ja B2B-tukeen — ei kuluttajan latauspalvelu.
# Plugit (plugit.fi → plugit.com): "Turnkey EV charging solutions" B2B-yrityksille;
#   englanninkielinen sivusto, ei suomenkielistä kuluttajapalvelua.
# St1 (st1.fi): kumppanina K-Latauksen verkostossa, mutta ei omaa kuluttajasuuntaista
#   latausverkkosivustoa — st1.fi/sahkolataus 404.
COMPANIES["sahkoautojen-lataus"] = [
    dict(slug="k-lataus", nimi="K-Lataus", domain="k-lataus.fi",
         y_tunnus="0154578-2",
         omistaja="K Auto Oy (PRH 0154578-2, Tikkurilantie 123 Vantaa) on Kesko Oyj:n autoalan tytäryhtiö; K-Lataus on K-Auton sähköautojen latausverkosto, joka on yhteistyössä St1:n ja Rechargen kanssa; kuuluu K-Auto Oy:hyn"),
    dict(slug="abc-lataus", nimi="ABC Lataus", domain="abcasemat.fi",
         y_tunnus="0116323-1",
         omistaja="Suomen Osuuskauppojen Keskuskunta SOK (PRH 0116323-1) omistaa ABC-ketjun; ABC-lataus on S-ryhmän sähköautojen latausverkosto ABC-asemilla, S-ruokakaupoilla ja hotelleilla; Suomen suurin teholatausverkosto"),
    dict(slug="ionity", nimi="IONITY", domain="ionity.eu",
         y_tunnus=None,
         omistaja="IONITY GmbH (Saksa) on BMW Groupin, Mercedes-Benzin, Volkswagen Groupin (Audi, Porsche), Hyundai-konsernin ja Ford Motorsin yhteisyritys; eurooppalainen suurteholatausverkosto moottoriteiden varsilla; fi-sivu ionity.eu/fi"),
    dict(slug="fortum-charge-drive", nimi="Fortum Charge & Drive", domain="chargedrive.com",
         y_tunnus="1463611-4",
         omistaja="Fortum Oyj (PRH 1463611-4, Helsinki; Suomen valtio enemmistöomistajana) operoi Charge & Drive -latauspalvelua suomalaisille sähköautoilijoille; chargedrive.com ohjaa fi-FI-sivulle automaattisesti"),
    dict(slug="recharge", nimi="Recharge", domain="rechargeinfra.com",
         y_tunnus=None,
         omistaja="Recharge AS (Norja) on pohjoismainen julkinen pikalatausverkko; Infracapital osti enemmistön Fortum Charge & Drive -infrastruktuurista ja rebrändäsi sen Recharge-nimellä; fi-sivu rechargeinfra.com/fi/"),
    # Helen Lataus mitattiin 4.8.2026 tähän kategoriaan ensin omana yhtiönään. Helen
    # myi koko julkisen latausliiketoimintansa Plugitille heinäkuussa 2026 (199 asemaa,
    # 798 latauspistettä, 55 000 käyttäjää siirtyi Plugitin sovellukseen), joten se
    # verkko on nyt Plugitin. helen.fi vastasi yhä 200, mikä ei riittänyt paljastamaan
    # omistajanvaihdosta — sama ansa kuin Väre→Helen 31.5.2026.
    dict(slug="plugit", nimi="Plugit", domain="plugit.com",
         y_tunnus="2513960-7",
         omistaja="Plugit Finland Oy (PRH 2513960-7) on suomalainen latausoperaattori; osti Helenin julkisen latausliiketoiminnan heinäkuussa 2026 (199 latausasemaa ja 798 latauspistettä sekä 55 000 käyttäjää) ja nousi pääkaupunkiseudun suurimmaksi julkiseksi latausoperaattoriksi; plugit.fi ohjaa osoitteeseen plugit.com"),
]

# LOMAMÖKKIVUOKRAUS (4.8.2026; 6 mökkivuokrauksen verkkoalustaa)
# Karsinnat:
#   Cottages.fi — domain ei vastannut (connection refused)
#   Loma-Hytti.fi — domain ei vastannut (connection refused)
#   Lomaviikko.fi — ajoittain toimiva mutta ei täysiverinen kansallinen alusta
# Kaikki 6 valittua ovat kansallisesti toimivia alustoja, joilla suomalaiset
# kuluttajat voivat etsiä ja varata lomamökkejä Suomesta.
COMPANIES["lomamokkivuokraus"] = [
    dict(slug="lomarengas", nimi="Lomarengas", domain="lomarengas.fi",
         y_tunnus="0980172-8",
         omistaja="Oy Lomarengas Ab, Ltd (PRH 0980172-8, Helsinki; perustettu 1994) on Suomen suurin mökkivuokrauksen välittäjä; yli 4 400 kohdetta Suomessa; If Peruutusturva sisältyy kaikkiin varauksiin; Siltasaarenkatu 8–10, Helsinki"),
    dict(slug="nettimokki", nimi="Nettimökki", domain="nettimokki.com",
         y_tunnus="0869288-1",
         omistaja="Alma Media Finland Oy (PRH 0869288-1) operoi Nettimökki-palvelua; Alma Media on suomalainen mediayhtiö, jonka palveluihin kuuluu useita verkkomarkkinapaikkoja; nettimokki.com"),
    dict(slug="airbnb", nimi="Airbnb", domain="airbnb.fi",
         y_tunnus=None,
         omistaja="Airbnb Ireland UC (Irlanti) — Airbnb, Inc.:n (NASDAQ: ABNB, San Francisco) eurooppalainen toimipiste; airbnb.fi ohjaa suomenkieliselle sivustolle"),
    dict(slug="booking-com", nimi="Booking.com", domain="booking.com",
         y_tunnus=None,
         omistaja="Booking.com B.V. (Alankomaat) on Booking Holdings Inc.:n (NASDAQ: BKNG) tytäryhtiö; yksi maailman suurimmista majoituksen varaustalustoista; toimii myös Suomessa mökkivuokrauksessa osoitteessa booking.com/fi"),
    dict(slug="huvilanet", nimi="Huvila.net", domain="huvila.net",
         y_tunnus="2202714-0",
         omistaja="Huvilanet Oy (PRH 2202714-0, Oulu; perustettu 2008) — mökkivuokrauksen välityspalvelu vuodesta 1999; suomalainen pienoperaattori"),
    dict(slug="mokkivuokra", nimi="Mökkivuokra.fi", domain="mokkivuokra.fi",
         y_tunnus="3364418-7",
         omistaja="Mökkivuokra Marketing Oy (PRH 3364418-7, Helsinki) on osa Villada Group Oy -konsernia; erikoistunut premium- ja luksusmajoituskohteiden välitykseen; toimii myös CottageFinland.fi-nimellä ulkomaisille asiakkaille"),
]

# --- AUTOTARVIKKEET-VERKOSSA (4.8.2026): autovaraosien ja -tarvikkeiden verkkokaupat ---
# Vertailtavat: kansalliset ja kansainväliset autovaraosa- ja autotarvikeverkkokaupat,
# jotka palvelevat suomalaisia kuluttajia omilla fi-sivustoillaan tai fi-kielisillä sivuillaan.
# KARSITUT:
#   Nettivaraosa (nettivaraosa.com): Alma Median ilmoitusmarkkinapaikka (C2C-classified),
#     ei suoramyyntiverkkokauppa — eri liiketoimintamalli kuin muut.
#   Bilema (bilema.fi): domain on Astra WordPress -teemapohja, ei autovaraosatoimijaa.
#   Mekonomen (mekonomen.fi): korjaamoketju, ei kuluttajalle myyvä varaosaverkkokauppa.
#   Trodo (trodo.fi): Cloudflare 403 -botti-esto; mittausaukko — ei hylkäysperuste.
#   Fixusnet (fixusnet.fi): Fixus-korjaamojen B2B-tavarantoimittaja; edellyttää myymälä-
#     tunnuksia ennen hintojen näyttämistä — ei kuluttajaverkkokauppa.
COMPANIES["autotarvikkeet-verkossa"] = [
    dict(slug="motonet", nimi="Motonet", domain="motonet.fi",
         y_tunnus="0699457-9",
         omistaja="Motonet Oy (PRH 0699457-9, Turku) on suomalaisen Broman Group Oy:n tytäryhtiö; perustettu 1975; Suomen johtava autotarvikeketju, jolla on yli 41 tavarataloa Suomessa; myy varaosia, työkaluja, vapaa-ajan tuotteita ja kodintuotteita myymälöissä ja verkossa"),
    dict(slug="biltema", nimi="Biltema", domain="biltema.fi",
         y_tunnus=None,
         omistaja="Biltema Nordic Retail AB (Ruotsi) — pohjoismainen vähittäiskauppaketju; perustettu 1963 Ruotsissa; yli 20 tavarataloa Suomessa; myy autoilu-, MP-, veneily-, koti- ja vapaa-ajan tuotteita; biltema.fi on suomenkielinen verkkokauppa, toimitusmaksu alkaen 4,85 €; ei suomalaista Y-tunnusta"),
    dict(slug="autodoc", nimi="Autodoc", domain="autodoc.fi",
         y_tunnus=None,
         omistaja="Autodoc SE (Berliini, Saksa) — eurooppalainen autovaraosaverkkokauppa, perustettu 2008; yli 6,7 miljoonaa tuotetta 27 maassa; palvelee yli 9 miljoonaa asiakasta vuodessa; autodoc.fi on suomenkielinen sivusto, ei suomalaista Y-tunnusta"),
    dict(slug="motointegrator", nimi="Motointegrator", domain="motointegrator.fi",
         y_tunnus=None,
         # 4.8.2026: tikki kirjoitti tähän "Auto Partner SA (Puola, Varsova)" sivulta
         # jota se ei ollut hakenut (kaikki kolme sen fetched_ok-polkua olivat 404).
         # motointegrator.fi:n yleiset sopimusehdot nimeävät myyjäksi saksalaisen
         # CLEVERLOG-AUTOTEILE GmbH:n. Kirjataan se mitä sivustolla lukee.
         omistaja="CLEVERLOG-AUTOTEILE GmbH (Saksa) on motointegrator.fi:n yleisissä sopimusehdoissa nimetty myyjä ja sopimusosapuoli; Motointegrator on suomenkielinen kuluttajaverkkokauppa, jossa lähes 5 miljoonaa varaosaa; suomenkielinen puhelinpalvelu 0800 413 714 (ma-pe 8-21); Trusted Shops -arvosana 4,76/5,00; ei suomalaista Y-tunnusta"),
    dict(slug="alvadi", nimi="ALVADI", domain="alvadi.fi",
         y_tunnus=None,
         omistaja="ALVADI (viro) — virolainen autovaraosaverkkokauppa, joka palvelee useita Euroopan maita suomalainen asiakaskunta mukaan lukien; fi-sivu alvadi.fi; suomalainen asiakaspalvelunumero +358 9315 888 39; pääkonttori Majaka 10, Tallinn; ilmainen toimitus yli 80 €:n tilauksille"),
    # EU Varaosat (euvaraosat.fi) karsittu 4.8.2026: SAMA YHTIÖ kuin Autodoc.
    # euvaraosat.fi:n omat toimitusehdot nimeävät sopimusosapuoleksi "AUTODOC SE,
    # Josef-Orlopp-Straße 55, 10365 Berliini, Arvonlisäverotunniste: DE260634589,
    # Kaupparekisteri: HRB 247677 B" ja jopa ilmoittavat verkkosivuksi
    # www.autodoc.fi — samat tunnisteet kuin autodoc-extraktissa. Kaksi saman
    # yhtiön kauppapaikkaa samassa kategoriassa kasvattaisi kentän keinotekoisesti
    # ja antaisi AUTODOC SE:lle kaksi sijaa. Sama linja kuin coffeehouse.fi →
    # raflaamo.fi ja fortum.fi → fortum.com. Tikki oli pisteyttänyt sen erikseen
    # viimeiseksi (58,7).
]

# VAKUUTUSVERTAILUPALVELUT (5.8.2026) — "vertailemme vertailijat" toisena versiona
# sähkövertailupalvelut-kaavasta. Mitataan vertailu-/kilpailutuspalvelun OMAA
# läpinäkyvyyttä (näkyvätkö tarjoukset ilman henkilötietoja, ansaintamalli,
# kattavuus, vakuutusyhtiöpaneeli, Y-tunnus, riippumaton arvio) — ei vakuutusten
# omia hintoja. Insured.fi karsittu: sivu ilmoittaa itse "avaa ovensa mahdollisim-
# man pian" — ei ole vielä toiminnassa oleva palvelu, vain liittymälomake.
COMPANIES["vakuutusvertailupalvelut"] = [
    dict(slug="valitsevakuutus", nimi="Valitse Vakuutus", domain="valitsevakuutus.fi",
         y_tunnus=None,
         omistaja="Sonodo (sivuston oma ilmoitus: \"Sonodo-toiminimen ylläpitämä\"); PRH:n haku nimellä \"Sonodo\" löytää Sonodo Oy:n (2887416-4), mutta yhteyttä ei ole vahvistettu — sivustolla itsellään ei näy Y-tunnusta"),
    dict(slug="vakuutustenvertailu", nimi="Vakuutustenvertailu.fi", domain="vakuutustenvertailu.fi",
         y_tunnus="2261132-0",
         omistaja="Effortia Oy (sama omistaja kuin Sähkövertailu.fi ja VertaaEnsin sähkövertailupalvelut-kategoriassa, eri tuote/vertikaali); käyttää Little Buck Oy:n Vakuutuslaskuri.fi-kilpailutussovellusta"),
    dict(slug="vakuutus-fi", nimi="Vakuutus.fi", domain="vakuutus.fi",
         y_tunnus=None,
         omistaja="Tumes Media Ltd (Valley Towers, Suite 5, Valley Road, Malta) — sivun oma tietosuojaseloste nimeää rekisterinpitäjäksi; ei suomalaista Y-tunnusta eikä maltalaista rekisterinumeroa näkyvillä"),
    dict(slug="vakuutusinfo", nimi="Vakuutusinfo.fi", domain="vakuutusinfo.fi",
         y_tunnus=None,
         omistaja="Omistavaa yhtiötä ei löydy sivustolta: ei Y-tunnusta, ei Oy-nimeä millään ladatulla sivulla; sisarsivustoina linkitetty joustoluottoja.fi ja rahoituslaitos.fi"),
    dict(slug="fiksuraha", nimi="FiksuRaha.fi", domain="fiksuraha.fi",
         y_tunnus=None,
         omistaja="Omistavaa yhtiötä ei löydy sivustolta: \"Tietoa meistä\" -sivulla vain \"Kotipaikka: Helsinki, Suomi\" ja sähköposti, ei Y-tunnusta eikä yhtiön nimeä; sivusto ilmoittaa joka sivulla \"Sivustomme voi sisältää affiliate-linkkejä\""),
]

# LENTOVERTAILUPALVELUT (5.8.2026). Skyscanner haetaan --raw-tilassa: --js-tila
# palauttaa botti-esto-haasteen ("Are you a person or a robot?").
COMPANIES["lentovertailupalvelut"] = [
    dict(slug="skyscanner", nimi="Skyscanner", domain="skyscanner.fi",
         y_tunnus=None,
         omistaja="Skyscanner Limited, yksityinen osakeyhtiö, rekisteröity Englannissa ja Walesissa yritysnumerolla 04217916 (sivun oma \"Ehdot\"-sivu); perustettu 2003; Ctrip (nyk. Trip.com Group) osti yrityksen 2016 1,4 miljardilla punnalla (sivun oma \"Tietoa meistä\" -sivu); ei suomalaista Y-tunnusta"),
    dict(slug="momondo", nimi="momondo", domain="momondo.fi",
         y_tunnus=None,
         omistaja="momondo.com A/S (Tanska); sivun omassa JSON-konfiguraatiossa affiliate-tunniste \"momondo-kyk-wl\" (kyk = Kayak) paljastaa Kayak-yhteyden; Kayak ja momondo kuuluvat molemmat Booking Holdings -konserniin; ei suomalaista Y-tunnusta"),
    dict(slug="travellink", nimi="Travellink", domain="travellink.fi",
         y_tunnus="1728205-9",
         omistaja="Travellink AB, filial i Finland (PRH 1728205-9) — ruotsalaisen Travellink AB:n Suomen sivuliike; kuuluu espanjalaiseen Opodo/eDreams ODIGEO -konserniin"),
    dict(slug="lentovertailu", nimi="Lentovertailu.fi", domain="lentovertailu.fi",
         y_tunnus=None,
         omistaja="Sivun oma yhteystietosivu: sivuston tekniikasta ja ylläpidosta vastaa \"espoolainen Silky Sand Media\"; avattu 2007; PRH-haku nimellä \"Silky Sand Media\" ei löydä yhtiötä; ei Y-tunnusta sivustolla"),
    dict(slug="lentohakukone", nimi="Lentohakukone.fi", domain="lentohakukone.fi",
         y_tunnus=None,
         omistaja="Omistavaa yhtiötä ei löydy sivustolta lainkaan: ei Y-tunnusta, ei Oy-nimeä, ei tietosuoja- tai käyttöehtosivua linkitettynä etusivulta"),
]

# MATKA- JA HOTELLIVERTAILUT (5.8.2026). kuumat.com/hotellit karsittu:
# sivu on pelkkä käsin koottu affiliate-linkkilista muihin palveluihin
# (Hotels.com, Trivago, Momondo, Kayak, Trip.com) — ei tee omaa vertailua.
COMPANIES["matka-ja-hotellivertailut"] = [
    dict(slug="trivago", nimi="trivago", domain="trivago.fi",
         y_tunnus=None,
         omistaja="trivago N.V. (Alankomaat) ja sen tytäryhtiöt (sivun oma tietosuojailmoitus); julkisesti noteerattu (Nasdaq: TRVG), enemmistöomistaja Expedia Group; ei suomalaista Y-tunnusta"),
    dict(slug="hotellit-fi", nimi="hotellit.fi", domain="hotellit.fi",
         y_tunnus=None,
         omistaja="Osoite Bulevardi 54, 00120 Helsinki (sivun oma käyttöehtosivu); ei Y-tunnusta, puhelinta, sähköpostia eikä chattia sivustolla; etusivulla paikoin täyttämätöntä placeholder-tekstiä (\"This is paragraph 1 text\")"),
    dict(slug="hotellitvertailu", nimi="Hotellitvertailu.fi", domain="hotellitvertailu.fi",
         y_tunnus=None,
         omistaja="Ei Y-tunnusta tai yhtiön nimeä yhteystietosivulla; sähköposti info@hotellitvertailu.fi; sivusto ilmoittaa avoimesti oman affiliate-ansaintamallinsa erillisellä sivulla ja selittää arviointimenetelmänsä"),
    dict(slug="matkailijat-net", nimi="Matkailijat.net (hotellivertailu)", domain="matkailijat.net",
         y_tunnus=None,
         omistaja="Matkailijat.net on suomalainen matkafoorumi; hotellien \"hintavertailu\"-toiminto on sivun oman ilmoituksen mukaan toteutettu yhteistyössä yhden kumppanin, Booking.comin, kanssa — ei siis vertaa useita varaussivustoja keskenään; ei Y-tunnusta sivulla"),
]
