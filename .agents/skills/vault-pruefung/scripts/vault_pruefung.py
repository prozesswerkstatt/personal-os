#!/usr/bin/env python3
"""Vault-Prüfung für ein PersonalOS (Vorlage der ProzessWerkstatt).

Nur lesend. Ändert keine Datei im Vault.

Befehle:
  text <datei|->            Schreibregeln für Copy-Texte prüfen (Umlaut-Ersatz,
                            Gedankenstriche, harte Umbrüche im Absatz).
                            Exit-Code 1 bei Treffern.
  links                     Kaputte [[Wikilinks]] finden.
  frontmatter               Notizen ohne YAML-Frontmatter finden.
  checkboxen                Offene "- [ ]" in Daily Notes zählen.
  platzhalter               Nicht ausgefüllte {{PLATZHALTER}} finden (Erststart offen?).
  alles                     links + frontmatter + checkboxen + platzhalter als Übersicht.

Optionen:
  --geaendert               Nur Dateien, die laut git geändert oder neu sind.
  --liste                   Einzelne Treffer statt nur Zahlen ausgeben.
  --bericht <datei.md>      Ergebnis zusätzlich als Markdown speichern
                            (Pfad außerhalb des Vaults empfohlen, z. B. Scratchpad).
"""

import argparse
import collections
import os
import unicodedata
import re
import subprocess
import sys

# Windows: Konsole und Pipes nutzen sonst oft cp1252, Umlaute würden falsch gelesen oder ausgegeben.
for _strom in (sys.stdin, sys.stdout, sys.stderr):
    try:
        _strom.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

# Ordner, die keine gepflegten Notizen enthalten (Roh- und Ausgabedateien, Technik).
AUSGESCHLOSSEN = {".git", ".obsidian", ".trash", ".claude", ".claudian", "node_modules",
                  "tmp", "_input", "_output", "_work", "_eingang", "_vorlagen", "venv", ".venv",
                  "__pycache__"}

UMLAUT = re.compile(r"[äöüÄÖÜß]")
WORT = re.compile(r"[A-Za-zÄÖÜäöüß]+")
CODEBLOCK = re.compile(r"```.*?```", re.S)
INLINECODE = re.compile(r"`[^`\n]*`")
WIKILINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")

# Häufige Ersatzschreibungen, die auch dann gemeldet werden, wenn das Vault-Wörterbuch
# das Wort (noch) nicht kennt.
KERNLISTE = {
    "fuer", "ueber", "koennen", "koennte", "moeglich", "moeglichkeit", "naechste", "naechsten",
    "spaeter", "waere", "waeren", "haette", "muessen", "muesste", "wuerde", "wuerden",
    "aenderung", "aenderungen", "uebersicht", "rueckmeldung", "gruesse", "gruessen",
    "persoenlich", "schoen", "loesung", "gross", "grosse", "grossen", "heisst", "strasse",
    "massnahme", "massnahmen", "gemaess", "fruehestens", "zurueck", "natuerlich", "tatsaechlich",
    "erklaervideo", "gefuellt", "bestaetigt", "koennt", "moechte", "moechten", "fuehren",
    "pruefen", "geprueft", "pruefung", "oeffnen", "aehnlich", "ausfuehrlich", "ueberarbeitet",
}


def transliteriere(wort):
    return (wort.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
                .replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue").replace("ß", "ss"))


def md_dateien(nur=None):
    if nur is not None:
        return [p for p in nur if p.endswith(".md") and os.path.isfile(os.path.join(VAULT, p))]
    ergebnis = []
    for wurzel, ordner, dateien in os.walk(VAULT):
        ordner[:] = [o for o in ordner if o not in AUSGESCHLOSSEN]
        for d in dateien:
            if d.endswith(".md"):
                ergebnis.append(os.path.relpath(os.path.join(wurzel, d), VAULT))
    return sorted(ergebnis)


def alle_dateinamen():
    """Alle Dateien im Vault (auch Anhänge), für die Link-Auflösung wie in Obsidian."""
    namen, pfade = set(), set()
    for wurzel, ordner, dateien in os.walk(VAULT):
        ordner[:] = [o for o in ordner if o not in {".git", ".trash", "node_modules"}]
        for d in dateien:
            # macOS liefert Dateinamen oft in NFD (ü = u + Pünktchen), Links stehen in NFC.
            # Obsidian gleicht das aus, also hier beides auf NFC bringen.
            d = unicodedata.normalize("NFC", d)
            rel = unicodedata.normalize("NFC", os.path.relpath(os.path.join(wurzel, d), VAULT))
            pfade.add(rel.lower())
            namen.add(d.lower())
            if d.lower().endswith(".md"):
                namen.add(d[:-3].lower())
                pfade.add(rel[:-3].lower())
    return namen, pfade


def lesen(pfad):
    with open(os.path.join(VAULT, pfad), encoding="utf-8", errors="replace") as f:
        return f.read()


def ohne_code(text):
    text = CODEBLOCK.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return INLINECODE.sub("", text)


def geaenderte_dateien():
    aus = subprocess.run(["git", "-C", VAULT, "status", "--porcelain", "-uall", "-z"],
                         capture_output=True, text=True).stdout
    ergebnis = []
    for eintrag in aus.split("\0"):
        if len(eintrag) > 3 and not eintrag.startswith("D"):
            ergebnis.append(eintrag[3:])
    return ergebnis


# ---------------------------------------------------------------- Schreibregeln

def woerterbuch():
    """Lernt aus dem Vault, welche Wörter mit Umlaut geschrieben werden.

    Ein Wort gilt als Ersatzschreibung, wenn seine Umlaut-Form im Vault deutlich
    häufiger vorkommt als die ASCII-Form (so bleibt z. B. "dass" erlaubt).
    """
    mit_umlaut = collections.Counter()
    ohne_umlaut = collections.Counter()
    for pfad in md_dateien():
        if pfad.startswith(".agents"):
            continue
        for w in WORT.findall(ohne_code(lesen(pfad))):
            w = w.lower()
            if UMLAUT.search(w):
                mit_umlaut[transliteriere(w)] += 1
            else:
                ohne_umlaut[w] += 1
    verdaechtig = {w for w, n in mit_umlaut.items() if n >= 2 and n >= 3 * ohne_umlaut.get(w, 0)}
    return verdaechtig | KERNLISTE


def pruefe_text(text, verdaechtig):
    treffer = []
    zeilen = text.split("\n")
    in_code = False
    in_frontmatter = zeilen[:1] == ["---"]
    vorige_absatzzeile = None
    for nr, zeile in enumerate(zeilen, 1):
        if in_frontmatter:
            if nr > 1 and zeile.strip() == "---":
                in_frontmatter = False
            continue
        if zeile.strip().startswith("```"):
            in_code = not in_code
            vorige_absatzzeile = None
            continue
        if in_code:
            continue
        sichtbar = INLINECODE.sub("", zeile)
        for zeichen, name in (("—", "Gedankenstrich (—)"), ("–", "Gedankenstrich (–)")):
            if zeichen in sichtbar:
                treffer.append((nr, name, zeile.strip()))
        for w in WORT.findall(sichtbar):
            if not UMLAUT.search(w) and w.lower() in verdaechtig:
                treffer.append((nr, f"Umlaut-Ersatz: {w}", zeile.strip()))
        # Harte Umbrüche: zwei direkt aufeinanderfolgende Fließtext-Zeilen. Kurze Vorzeilen
        # (Grußformel, Anrede, Betreff) sind erlaubt, z. B. "Viele Grüße" + "Max".
        fliesstext = bool(zeile.strip()) and not re.match(r"\s*([-*+>|#]|\d+[.)]\s|!\[|\[\[)", zeile) \
            and not zeile.startswith(("    ", "\t"))
        if fliesstext and vorige_absatzzeile is not None:
            vorzeile = zeilen[vorige_absatzzeile - 1].rstrip()
            if len(vorzeile) >= 40 and not vorzeile.endswith(":"):
                treffer.append((nr, "Harter Umbruch im Absatz", zeile.strip()))
        vorige_absatzzeile = nr if fliesstext else None
    return treffer


def befehl_text(args):
    text = sys.stdin.read() if args.datei == "-" else open(args.datei, encoding="utf-8").read()
    treffer = pruefe_text(text, woerterbuch())
    if not treffer:
        print("OK: keine Verstöße gegen die Schreibregeln gefunden.")
        return 0
    print(f"{len(treffer)} Treffer:")
    for nr, art, zeile in treffer:
        print(f"  Zeile {nr}: {art}  |  {zeile[:100]}")
    return 1


# ---------------------------------------------------------------- Vault-Checks

def pruefe_links(dateien):
    namen, pfade = alle_dateinamen()
    kaputt = []
    for pfad in dateien:
        text = ohne_code(lesen(pfad))
        for nr, zeile in enumerate(text.split("\n"), 1):
            for _, ziel in WIKILINK.findall(zeile):
                ziel = ziel.split("|")[0].split("#")[0].split("^")[0].strip()
                if not ziel or ziel.startswith(("http", ":")):
                    continue
                if ziel.replace("\\", "").strip() == "":
                    continue
                z = unicodedata.normalize("NFC", ziel.replace("\\", "")).lower()
                basis = os.path.basename(z)
                if z in pfade or basis in namen or z.removesuffix(".md") in pfade:
                    continue
                kaputt.append((pfad, nr, ziel))
    return kaputt


# Systemdateien ohne Notizcharakter brauchen kein Frontmatter.
OHNE_FRONTMATTER_OK = {"AGENTS.md", "CLAUDE.md", "README.md", "CHANGELOG.md"}


def pruefe_frontmatter(dateien):
    return [p for p in dateien if p not in OHNE_FRONTMATTER_OK
            and not p.startswith(".agents" + os.sep)
            and not lesen(p).startswith("---")]


def pruefe_checkboxen():
    ordner = os.path.join(VAULT, "05 Daily Notes")
    je_monat = collections.Counter()
    eintraege = []
    for d in sorted(os.listdir(ordner)):
        if not d.endswith(".md"):
            continue
        for zeile in lesen(os.path.join("05 Daily Notes", d)).split("\n"):
            if re.match(r"\s*- \[ \]", zeile):
                je_monat[d[:7]] += 1
                eintraege.append((d[:-3], zeile.strip()[6:]))
    return je_monat, eintraege


PLATZHALTER = re.compile(r"\{\{[A-ZÄÖÜ_]+\}\}")


def pruefe_platzhalter(dateien):
    treffer = []
    for pfad in dateien:
        for nr, zeile in enumerate(lesen(pfad).split("\n"), 1):
            for m in PLATZHALTER.findall(zeile):
                treffer.append((pfad, nr, m))
    return treffer


def befehl_vault(args, welche):
    dateien = md_dateien(geaenderte_dateien() if args.geaendert else None)
    zeilen = [f"# Vault-Prüfung", "", f"Geprüfte Notizen: {len(dateien)}"
              + (" (nur geänderte)" if args.geaendert else ""), ""]
    fehler = 0
    if "links" in welche:
        kaputt = pruefe_links(dateien)
        fehler += len(kaputt)
        zeilen.append(f"## Kaputte Links: {len(kaputt)}")
        zaehler = collections.Counter(z for _, _, z in kaputt)
        for ziel, n in zaehler.most_common(None if args.liste else 15):
            zeilen.append(f"- [[{ziel}]] ({n}x)")
        if args.liste:
            zeilen.append("")
            for pfad, nr, ziel in kaputt:
                zeilen.append(f"- {pfad}:{nr} → {ziel}")
        zeilen.append("")
    if "frontmatter" in welche:
        ohne = pruefe_frontmatter(dateien)
        zeilen.append(f"## Ohne Frontmatter: {len(ohne)}")
        je_ordner = collections.Counter(p.split(os.sep)[0] for p in ohne)
        for o, n in je_ordner.most_common():
            zeilen.append(f"- {o}: {n}")
        if args.liste:
            zeilen += [f"  - {p}" for p in ohne]
        zeilen.append("")
    if "platzhalter" in welche:
        offen = pruefe_platzhalter(dateien)
        zeilen.append(f"## Offene Platzhalter: {len(offen)}")
        if offen:
            zeilen.append("Der Erststart ist noch nicht abgeschlossen (Skill erststart).")
        je_datei = collections.Counter(p for p, _, _ in offen)
        for pfad, n in je_datei.most_common():
            zeilen.append(f"- {pfad}: {n}")
        if args.liste:
            zeilen += [f"  - {p}:{nr} {m}" for p, nr, m in offen]
        zeilen.append("")
    if "checkboxen" in welche and not args.geaendert:
        je_monat, eintraege = pruefe_checkboxen()
        zeilen.append(f"## Offene Checkboxen in Daily Notes: {sum(je_monat.values())}")
        zeilen.append("Aufgaben gehören in die Aufgabenliste aus der AGENTS.md. Daily Notes verlinken nur.")
        for m, n in sorted(je_monat.items()):
            zeilen.append(f"- {m}: {n}")
        if args.liste:
            zeilen += [f"  - {d}: {t}" for d, t in eintraege]
        zeilen.append("")
    ausgabe = "\n".join(zeilen)
    print(ausgabe)
    if args.bericht:
        with open(args.bericht, "w", encoding="utf-8") as f:
            f.write(ausgabe + "\n")
    return 1 if fehler else 0


def main():
    p = argparse.ArgumentParser(description="Vault-Prüfung (nur lesend)")
    p.add_argument("befehl", choices=["text", "links", "frontmatter", "checkboxen", "platzhalter", "alles"])
    p.add_argument("datei", nargs="?", help="bei 'text': Datei oder - für stdin")
    p.add_argument("--geaendert", action="store_true")
    p.add_argument("--liste", action="store_true")
    p.add_argument("--bericht")
    args = p.parse_args()
    if args.befehl == "text":
        if not args.datei:
            p.error("text braucht eine Datei oder -")
        return befehl_text(args)
    welche = {"alles": {"links", "frontmatter", "checkboxen", "platzhalter"}}.get(args.befehl, {args.befehl})
    return befehl_vault(args, welche)


if __name__ == "__main__":
    sys.exit(main())
