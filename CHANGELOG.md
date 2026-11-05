# Änderungen an der Vorlage

Nur Änderungen an der Vorlage selbst. Was in einem eingerichteten PersonalOS passiert, steht dort in den Daily Notes.

## 0.3.0 · 2026-11-05

- Neuer Skill `vault-navigation`: Einstiegspunkte je Fragetyp, Suchreihenfolge (Übersicht, Dateiname, Volltext, Links, Frontmatter), Verlässlichkeit bei Widersprüchen, Antwort mit Fundstelle, Pflege der Übersichtsnotizen.
- Neuer Skill `vorlage-aktualisieren`: Skills, Werkzeuge und Vorlagen aus dem Remote `vorlage` übernehmen, ohne persönliche Inhalte und ohne AGENTS.md zu überschreiben.
- README: Abschnitt „Trainieren“ für die ersten Wochen, Installationsprompt prüft die Skills und macht eine Probe-Suche.

## 0.2.0 · 2026-11-05

- Öffentlich unter `prozesswerkstatt/personal-os`, neue Historie ohne personenbezogene Daten.
- Installationsprompt im README für die Einrichtung ohne Begleitung.
- Windows: `tools/einrichten.sh` kopiert die Skills statt zu verknüpfen, `tools/automatisch-sichern.sh` legt Aufgaben in der Windows-Aufgabenplanung an, `.gitattributes` erzwingt LF für Skripte, Prüfskript liest und schreibt UTF-8 auch unter Windows, Hinweise auf `py` und Git Bash in AGENTS.md und Skills.
- **Unter Windows noch nicht auf einem echten Rechner getestet** (Aufgabenplanung, Kopien der Skills). Erster Einsatz bei einem Kunden mit Windows-PC.

## 0.1.1 · 2026-11-03

- Leere Ordner (Daily Notes, Archiv, Anhänge, Referenzen, Vorschriften) tragen eine `.gitkeep`, sonst fehlen sie in Repos, die aus der Vorlage erzeugt werden. Gefunden beim ersten Einsatz.

## 0.1.0 · 2026-11-03

- Erste Fassung: Ordnerstruktur nach PARA, AGENTS.md als einzige Regeldatei, Kontext-, Übersichts- und Entscheidungsnotizen, sieben Notizvorlagen, sechs Skills (erststart, transkript-einarbeiten, info-einsortieren, tagesabschluss, ablauf-zu-skill, vault-pruefung), Werkzeuge zum Einrichten und Sichern, Obsidian-Grundeinstellungen.
- Abgeleitet aus dem Second Brain der ProzessWerkstatt (im Einsatz seit Juni 2026) und Ideen aus der PersonalOS-Boilerplate von Vincent Mumme (MIT, siehe LIZENZEN/).
