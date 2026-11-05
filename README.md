# PersonalOS Vorlage

Vorlage der ProzessWerkstatt für ein persönliches Wissenssystem (PersonalOS, Second Brain). Wissen, Abläufe, Kunden und Entscheidungen einer Person liegen als verknüpfte Markdown-Dateien lokal auf ihrem Rechner, gesichert in einem eigenen GitHub-Repository. Jeder KI-Agent (Claude Code, Codex, Gemini, lokale Modelle über Ollama) arbeitet mit denselben Dateien. Das Wissen gehört der Person, nicht dem Anbieter.

Die Vorlage startet fast leer und wächst mit der Arbeit: Jedes Transkript, jeder Beobachtungstermin und jede Korrektur macht Akten, Abläufe und Skills genauer.

## Aufbau

```text
AGENTS.md            einzige Regeldatei für alle Agenten (CLAUDE.md verweist nur darauf)
00 Kontext/          wer die Person ist, Angebot, Schreibstil
01 Inbox/            Brain Dump, Vorschläge von Agenten, _eingang/ für Rohmaterial (nicht in Git)
02 Projekte/         Vorhaben und Kundenakten (Kunden/<Kunde>/<Kunde>.md)
03 Bereiche/         Abläufe, Entscheidungen, Personen
04 Wissen/           Vorschriften und Normen, Referenzen, Fachthemen
05 Daily Notes/      Tageslogbuch YYYY-MM-DD.md
06 Archiv/           Abgeschlossenes
07 Anhänge/          eingebettete Bilder und PDFs
_vorlagen/           Daily Note, Kundenakte, Person, Entscheidung, Ablauf, Wissensnotiz, Transkript-Auswertung
.agents/skills/      erststart, transkript-einarbeiten, info-einsortieren, tagesabschluss, ablauf-zu-skill, vault-pruefung
tools/               einrichten.sh, sichern.sh, automatisch-sichern.sh
```

## So wächst das System

```text
Gespräch / Ortstermin / Bildschirmbegleitung
        │  Aufnahme (z. B. Plaud) → Transkript nach 01 Inbox/_eingang/
        ▼
transkript-einarbeiten ──► Kundenakte · Personen · Abläufe · Wissen · Entscheidungen
        │                     (nur die Essenz, mit Quelle und Zeitstempel)
        ▼
Ablauf zweimal gleich gelaufen ──► ablauf-zu-skill ──► Skill führt den Ablauf aus
        │
        ▼
Korrektur durch die Person ──► landet im Skill, im Schreibstil oder als Entscheidung
```

Die drei Grundregeln dahinter: eine Aussage an genau einem Ort, Eingang ist noch keine Wahrheit (erst die geprüfte Essenz wird übernommen), Prüfpunkte mit Außenwirkung bleiben beim Menschen.

## Selbst einrichten (Windows oder Mac)

**Voraussetzungen**

- **Claude Code** mit einem Claude-Abo (oder ein anderer Agent mit Dateizugriff, etwa Codex). Läuft unter macOS 13 und neuer sowie nativ unter Windows 10 (ab Version 1809) und Windows 11. Installation laut offizieller Anleitung: <https://code.claude.com/docs/de/setup>
- **Git**. Windows: [Git für Windows](https://git-scm.com/download/win), bringt Git Bash mit, das die Skripte in `tools/` brauchen. Anthropic empfiehlt es für Claude Code unter Windows ohnehin. Mac: Beim ersten Aufruf von `git` im Terminal bietet macOS die Installation selbst an.
- **Python 3** für das Prüfskript. Windows: <https://www.python.org/downloads/>, beim Installieren „Add python.exe to PATH“ anhaken, Aufruf dann `py`. Mac: meist schon vorhanden (`python3`).
- **Obsidian** als Oberfläche, optional: <https://obsidian.md/download>

Der Installationsprompt prüft das selbst und sagt, was fehlt.

**Installationsprompt.** Claude Code in einem beliebigen Ordner öffnen und diesen Text einfügen:

```text
Richte mir ein PersonalOS aus der Vorlage https://github.com/prozesswerkstatt/personal-os ein. Arbeite Schritt für Schritt, sag kurz, was du tust, und warte bei jeder Entscheidung auf meine Antwort. Frag mich nie nach Passwörtern und schreib keine Zugangsdaten in Dateien.

1. Stell fest, ob ich unter Windows oder macOS arbeite, und richte alle Befehle und Pfade danach aus. Unter Windows führst du Shell-Skripte mit Git Bash aus.
2. Prüfe Git (git --version) und Python 3 (Windows: py --version, Mac: python3 --version). Fehlt etwas, nenn mir den offiziellen Download für mein System und warte, bis ich fertig bin.
3. Schlag mir einen Speicherort vor: einen Ordner PersonalOS direkt in meinem Benutzerordner (Windows C:\Users\<Name>\PersonalOS, Mac ~/PersonalOS). Nicht unter Desktop oder Dokumente und nicht in einem Ordner, den OneDrive, iCloud oder Dropbox synchronisiert. Warte auf meine Bestätigung.
4. Klone die Vorlage dorthin und benenne den Remote origin in vorlage um (git remote rename origin vorlage), damit meine Notizen nie in das öffentliche Vorlagen-Repository gelangen.
5. Führe im neuen Ordner tools/einrichten.sh aus (Windows: bash tools/einrichten.sh in Git Bash).
6. Lies AGENTS.md und .agents/skills/erststart/SKILL.md vollständig und führe mit mir den Erststart durch. Stell die Fragen einzeln. Prüfe am Ende mit dem Prüfskript, dass keine Platzhalter offen sind.
7. Prüfe, ob Obsidian installiert ist, nenne sonst den Download, und sag mir, wie ich den Ordner als Vault öffne.
8. Mach einen ersten Commit. Biete mir an, für die Sicherung ein eigenes, privates GitHub-Repository als origin einzurichten, und zeig mir dafür die Schritte im Browser. Pushe nichts ohne meine Zustimmung. Wenn ich möchte, schalte danach die automatische Sicherung ein (tools/automatisch-sichern.sh an) und prüfe sofort, ob sie eingerichtet ist (Windows: schtasks /Query /TN "PersonalOS Sicherung 0730", Mac: launchctl list | grep personalos).
9. Gib mir zum Schluss eine kurze Übersicht, was angelegt ist, und sag mir, dass ich künftige Sitzungen direkt im Ordner PersonalOS starte, damit die Regeln aus AGENTS.md automatisch geladen werden.
```

## Mit Begleitung einrichten

Für Teams und Betriebe richtet die ProzessWerkstatt das PersonalOS gemeinsam ein: Repository aus dieser Vorlage erzeugen („Use this template“, immer **privat**), Erstgespräch aufnehmen und damit vorbefüllen, danach Übergabe ins eigene GitHub-Konto („Transfer ownership“). Ab dann gehört das Wissen vollständig dem Kunden.

Prüfen, ob alles ausgefüllt ist (Windows `py` statt `python3`):

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles
```

Erwartung nach dem Erststart: 0 kaputte Links, 0 offene Platzhalter.

## Windows und Mac

Die Inhalte sind auf beiden Systemen gleich. Unterschiede:

| | Mac | Windows |
|---|---|---|
| Skripte in `tools/` | Terminal | Git Bash |
| Skills für Claude Code (`tools/einrichten.sh`) | Verknüpfungen, Änderungen wirken sofort | Kopien, nach Änderungen an `.agents/skills/` das Skript erneut ausführen |
| Automatische Sicherung | LaunchAgent | Windows-Aufgabenplanung, läuft nur bei angemeldetem Benutzer |
| Prüfskript | `python3` | `py` |

`.gitattributes` hält die Zeilenenden auf beiden Systemen gleich. Ohne das würden die Shell-Skripte unter Windows nicht starten.

## Täglicher Gebrauch

| Situation | Satz an den Agenten |
|---|---|
| Aufnahme liegt in `_eingang/` | „Arbeite das Transkript ein.“ |
| Dokument, Info, Merkposten | „Merk dir das“ oder „sortier die Inbox“ |
| Ablauf soll automatisch laufen | „Mach daraus einen Skill.“ |
| Feierabend | „Tagesabschluss.“ |

## Lokales Modell statt Cloud

Das Wissen steckt in den Dateien, deshalb lässt sich das Modell tauschen. Für lokale Modelle (Ollama) gilt aus der Praxis: Das Modell muss mehrstufig suchen und Werkzeuge sauber aufrufen können. Ab 32 GB Arbeitsspeicher brauchbar, darunter nur für einfache Fragen. Kontextfenster mindestens 64k. Je schlanker AGENTS.md und Skill-Liste, desto schneller.

## Vorlage weiterentwickeln

Diese Vorlage lebt in `prozesswerkstatt/personal-os`. Änderungen hier betreffen nur neue PersonalOS. Bestehende Kunden-Vaults werden nicht automatisch aktualisiert.

- **Systemdateien** (übertragbar): `.agents/skills/`, `tools/`, `_vorlagen/`, Regelabschnitte der `AGENTS.md`.
- **Inhalte** (gehören dem Kunden, nie überschreiben): alles andere.

Update in einem Kunden-Vault: Systemdateien einzeln vergleichen und übernehmen, `VORLAGE-VERSION` hochsetzen, Änderung in der Daily Note vermerken. Jede Änderung an der Vorlage kommt in `CHANGELOG.md` mit neuer Versionsnummer.

## Herkunft und Lizenz

Abgeleitet aus dem Second Brain der ProzessWerkstatt, im täglichen Einsatz seit Juni 2026. Die Vorlage enthält keine Inhalte und keine personenbezogenen Daten. Einzelne Ideen (Wahrheit mit genau einem Owner, Trennung von Quelle und übernommener Wahrheit, Call-Auswertung, Prüfung nach jeder Änderung, Skill-Routing) stammen aus der [PersonalOS-Boilerplate](https://github.com/vincentmumme/personalos-boilerplate) von Vincent Mumme, veröffentlicht unter MIT-Lizenz (Text in `LIZENZEN/personalos-boilerplate-MIT.txt`).
