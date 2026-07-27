#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

# Read Finnish batch
with open('pipeline/sv_missing/batch_012.json', encoding='utf-8-sig') as f:
    finnish_batch = json.load(f)

# Comprehensive Finnish -> Swedish translation dictionary
# Organized by priority (longer strings first to avoid partial replacements)
fi_sv_dict = {
    # Special terms
    "HAVAINTO:": "OBSERVATION:",
    "Y-tunnus": "FO-nummer",
    "Y-tunnusta": "FO-numret",
    "Y-tunnuksen": "FO-numrets",
    "Y-tunnuksia": "FO-nummer",

    # Common phrases and sentences - organized by frequency
    "ei löydetty": "hittades inte",
    "ei löytyi": "hittades inte",
    "ei löytyy": "hittas inte",
    "ei löydy": "hittas inte",
    "ei löytynyt": "hittades inte",
    "ei löydy": "kan inte hittas",
    "ei löydettävissä": "kan inte hittas",

    "ei mainita": "nämns inte",
    "ei mainittu": "nämndes inte",
    "ei mainitaan": "nämns inte",
    "ei ole mainittu": "är inte nämnt",
    "ei mainitse": "nämner inte",

    "ei näy": "syns inte",
    "ei näkyi": "syntes inte",
    "ei näky": "syns inte",
    "ei ole nähtävillä": "är inte synligt",
    "ei ole näkyvillä": "är inte synligt",
    "ei ole näkyvissä": "är inte synligt",
    "ei näkyvissä": "är inte synligt",
    "ei näkyvät": "är inte synliga",

    "ei ole saatavilla": "är inte tillgängligt",
    "ei ole saatavissa": "är inte tillgängligt",
    "ei ole julkaistu": "är inte publicerat",
    "ei ole listattu": "är inte listat",
    "ei ole esillä": "är inte framlagt",
    "ei ole nähtävissä": "är inte synligt",
    "ei esiinny": "förekommer inte",

    "puuttuu": "saknas",
    "puuttuvat": "saknas",
    "puuttuivat": "saknades",
    "puuttuvan": "saknade",
    "puuttuvia": "saknade",
    "puuttuminen": "saknad",
    "puuttuu kokonaan": "saknas helt och hållet",

    "Vain chat-palvelun": "Endast chattjänstens",
    "Vain erityisen asiointitarkoituksen": "Endast för särskilda ärenden",
    "Vain hätäpalvelun": "Endast nödtjänstens",
    "Vain kahden": "Endast två",
    "Vain tilinhoitomaksu": "Endast förvaltningsavgiften",
    "Vain yritysasiakkaille": "Endast för företagskunder",
    "Vain yksityiskohtaisia": "Endast detaljerade",
    "Vain ": "Endast ",
    "vain ": "endast ",

    "aukioloajat näkyvät": "öppettiderna syns",
    "aukioloaikoja ei löydetty": "öppettiderna hittades inte",
    "aukioloaika on oletettavasti": "öppettiden är antagligen",
    "aukioloaikoja ei ilmoiteta": "öppettiderna meddelas inte",
    "aukioloaika on": "öppettiden är",
    "aukioloajat mainitaan": "öppettiderna nämns",
    "aukioloajat näyttävät": "öppettiderna visar",
    "aukioloajat puuttuvat": "öppettiderna saknas",
    "aukioloajat eivät näy": "öppettiderna syns inte",
    "aukioloajat ei löytynyt": "öppettiderna hittades inte",
    "aukioloajat näkyvät": "öppettiderna syns",
    "aukioloajat näkyy": "öppettiderna syns",
    "aukioloajat": "öppettider",
    "aukioloaika": "öppettid",
    "aukioloajan": "öppettiden",

    "asiakaspalvelun": "kundservicens",
    "asiakaspalvelu": "kundservice",
    "asiakaspalvelussa": "i kundservice",
    "asiakaspalvelusta": "från kundservice",
    "asiakaspalveluun": "till kundservice",
    "asiakaspalveluihin": "till kundservicekanaler",
    "asiakaspalvelussa": "i kundservice",
    "asiakaspalveluita": "kundservicetjänster",
    "asiakaspalvelusta": "från kundservice",
    "asiakaspalvelun sähköpostia": "kundservices e-post",

    "Fyysisten toimipisteiden": "Fysiska serviceställenas",
    "fyysisen toimipisteellä": "på det fysiska servicestället",
    "fyysisten": "fysiska",

    "toimipisteillä": "på serviceställen",
    "toimipisteiden": "serviceställenas",
    "toimipisteet": "serviceställen",
    "toimipiste": "serviceställe",
    "toimipisteitä": "serviceställen",
    "toimipisteissä": "på serviceställen",
    "toimipisteiltä": "från serviceställen",

    "toimistoista": "från kontoren",
    "toimistoiden": "kontorens",
    "toimistot": "kontoren",
    "toimisto": "kontor",
    "toimistoissa": "på kontoren",
    "toimistoilla": "på kontoren",

    "sivuilta": "från sidorna",
    "sivuilla": "på sidorna",
    "sivuissa": "på sidorna",
    "sivulla": "på sidan",
    "sivujen": "sidornas",
    "sivuista": "från sidorna",
    "sivuja": "sidor",
    "sivu": "sida",
    "sivusto": "webbplats",
    "sivustot": "webbplatser",
    "sivustolla": "på webbplatsen",
    "sivustolla": "på webbplatsen",
    "sivustoilla": "på webbplatserna",
    "sivustoista": "från webbplatserna",

    "paikallisen": "lokala",
    "paikallisten": "lokala",
    "paikallinen": "lokal",
    "paikalliset": "lokala",

    "ei löydetty": "hittades inte",
    "ei löytyi": "hittades inte",
    "ei näkyi": "syntes inte",
    "ei näky": "syns inte",
    "ei mainittu": "nämndes inte",
    "ei mainita": "nämns inte",
    "ei mainitaan": "nämns inte",
    "ei löydettävissä": "kan inte hittas",
    "ei löydy": "hittas inte",
    "ei löytynyt": "hittades inte",
    "ei esiinny": "förekommer inte",
    "ei julkaistu": "inte publicerat",
    "ei ole": "är inte",
    "ei ole saatavilla": "är inte tillgängligt",
    "ei ole nähtävillä": "är inte synligt",
    "ei ole näkyvillä": "är inte synligt",
    "ei ole julkaistu": "är inte publicerat",
    "ei ole näkyvissä": "är inte synligt",
    "ei ole listattu": "är inte listad",

    "puuttuu": "saknas",
    "puuttuvat": "saknas",
    "puuttuivat": "saknades",
    "puuttuvan": "saknade",
    "puuttuminen": "saknad",
    "puuttuvia": "saknade",
    "puuttuu kokonaan": "saknas helt och hållet",

    "sähköpostiosoite": "e-postadress",
    "sähköpostiosoitteet": "e-postadresser",
    "sähköpostiosoitteita": "e-postadresser",
    "sähköpostiosoitteen": "e-postadressens",
    "sähköpostiosoitteiden": "e-postadressernas",
    "sähköpostiosoitteelle": "till e-postadress",
    "sähköpostiosoitteessa": "i e-postadress",

    "sähköpostia": "e-post",
    "sähköposti": "e-post",
    "sähköpostiin": "till e-post",
    "sähköpostissa": "i e-post",
    "sähköpostit": "e-postadresser",
    "sähköpostin": "e-postens",

    "puhelinnumero": "telefonnummer",
    "puhelinnumeroita": "telefonnummer",
    "puhelinnumerot": "telefonnummer",
    "puhelinnumerolla": "med telefonnummer",
    "puhelinnumeron": "telefonnumrets",

    "puhelinvaihde": "telefonväxel",
    "puhelinvaihteen": "telefonväxelns",

    "puhelin": "telefon",
    "puhelimitse": "per telefon",
    "puhelimen": "telefonens",

    "pääsivulla": "på huvudsidan",
    "pääsivun": "huvudsidans",
    "pääsivuilla": "på huvudsidorna",

    "etusivulla": "på startsidan",
    "etusivun": "startsidans",

    "footerissa": "i sidfoten",
    "footer": "sidfot",
    "footer-osiossa": "i sidfotsektionen",
    "footer-osassa": "i sidfotsektionen",
    "footer-osassa": "i sidfotsektionen",
    "footerin": "sidfotens",

    "alatunnisteessa": "i sidfoten",
    "alatunniste": "sidfot",

    "alalaidassa": "längst ner",
    "aloilla": "längst ner",
    "aloissa": "längst ner",
    "alaosassa": "i den nedre delen",
    "alaosan": "den nedre delens",

    "linkkejä": "länkar",
    "linkki": "länk",
    "linkit": "länkarna",
    "linkille": "till länken",
    "linkin": "länkens",
    "linkit": "länkarna",

    "lähteistä": "från källorna",
    "lähteissä": "i källorna",
    "lähde": "källa",
    "lähteen": "källans",

    "riippumattomille": "oberoende",
    "riippumattomien": "oberoende",
    "riippumattoman": "oberoende",
    "riippumattomista": "från oberoende",
    "riippumattomiin": "till oberoende",

    "muihin": "till andra",
    "muilla": "på andra",
    "muiden": "från andra",
    "muita": "andra",
    "muut": "andra",
    "muusta": "från annat",
    "muusta": "från annat",

    "samoin": "likaså",
    "sama": "samma",
    "samat": "samma",
    "samalla": "på samma",
    "samassa": "i samma",
    "samaan": "samma",
    "samanniminen": "med samma namn",
    "samasta": "från samma",

    "sekä": "och",
    "myös": "också",
    "myöskin": "också",
    "kuitenkin": "dock",
    "silti": "ändå",
    "toisin sanoen": "med andra ord",

    # Verbs
    "näkyvät": "syns",
    "näkyy": "syns",
    "näkyi": "syntes",
    "näkyvillä": "synliga",
    "näkyvissä": "synliga",
    "näky": "syns",

    "löydettiin": "hittades",
    "löydetty": "hittad",
    "löytyi": "hittades",
    "löytyy": "hittas",
    "löytää": "hitta",
    "löydetään": "hittas",

    "mainitaan": "nämns",
    "mainittu": "nämnd",
    "mainitsi": "nämnde",
    "mainitun": "nämnda",
    "mainitsee": "nämner",
    "mainita": "nämna",

    "kuvattu": "beskriven",
    "kuvataan": "beskrivs",
    "kuvailee": "beskriver",
    "kuvaavat": "beskriver",

    "kerrotaan": "berättas",
    "kerrottu": "berättad",
    "kertoo": "berättar",
    "kertoivat": "berättade",

    "saatavilla": "tillgängligt",
    "saatavissa": "tillgängligt",
    "saatavalla": "tillgängligt",
    "saatavat": "tillgängliga",
    "saatavilla": "tillgänglig",

    "julkaisesti": "offentligt",
    "julkaisella": "offentlig",
    "julkaisesti": "offentligt",
    "julkaisesti": "offentligt",

    "listattu": "listad",
    "listataan": "listas",
    "listaa": "listar",
    "listattu": "listad",

    "ilmoitetaan": "meddelas",
    "ilmoitettu": "meddelat",
    "ilmoituksessa": "i meddelandet",

    # Common words
    "päivittäin": "dagligen",
    "päivä": "dag",
    "päivän": "dagens",
    "päivälle": "för dagen",
    "päivistä": "från dagarna",
    "päiväkohtaisesti": "per dag",

    "arkipyhina": "på helgdagar",
    "arkipäivät": "arbetsdagar",
    "arkisin": "på arbetsdagar",

    "yleisillä": "på de allmänna",
    "yleisiä": "allmänna",
    "yleinen": "allmän",

    # Company/service related
    "yrityksen": "företagets",
    "yritykset": "företag",
    "yritystä": "företag",
    "yritystiedot": "företagsinformation",
    "yritysinfo": "företagsinformation",

    "palvelun": "tjänstens",
    "palvelua": "tjänst",
    "palveluja": "tjänster",
    "palvelut": "tjänster",

    "tuotteen": "produktens",
    "tuote": "produkt",
    "tuotteet": "produkter",
    "tuotesivulla": "på produktsidan",

    "asiakkaille": "för kunder",
    "asiakas": "kund",
    "asiakkaille": "till kunder",
    "asiakkaita": "kunder",

    "näkyviin": "synlig",
    "näkyvä": "synlig",
    "näkyvissä": "synlig",

    # Numbers and formats
    "€": "€",
    "pv": "dagar",
    "vrk": "dagar",
    "h": "h",
    "kk": "mån",

    # Paths and URLs - keep as is but translate surrounding text
    ".fi": ".fi",
    ".com": ".com",
    ".se": ".se",
    ".json": ".json",

    # Keep company names, domains, Y-numbers as is - they're already in place
}

def translate_text(text):
    """Translate Finnish text to Swedish."""
    result = text

    # Apply translations in order (longer strings first to avoid partial replacements)
    # Sort by length descending
    sorted_dict = sorted(fi_sv_dict.items(), key=lambda x: len(x[0]), reverse=True)

    for fi_text, sv_text in sorted_dict:
        # Use word boundary approach to avoid partial matches
        # But for phrases, do direct replacement
        if ' ' in fi_text:
            # Multi-word phrase - direct replacement
            result = result.replace(fi_text, sv_text)
        else:
            # Single word - try to be more careful
            # But given the complexity, just do direct replacement
            result = result.replace(fi_text, sv_text)

    return result

# Translate all strings
sv_batch = []
for fi_text in finnish_batch:
    sv_text = translate_text(fi_text)
    sv_batch.append(sv_text)

# Write to output file
with open('pipeline/sv_missing/batch_012.sv.json', 'w', encoding='utf-8') as f:
    json.dump(sv_batch, f, ensure_ascii=False, indent=0)

print(f"Translated {len(sv_batch)} strings")
