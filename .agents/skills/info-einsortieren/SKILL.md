---
name: info-einsortieren
description: Sortiert einzelne Informationen, Dokumente, Notizen, Fotos von Unterlagen, Brain-Dump-Einträge und Agenten-Vorschläge an den richtigen Ort im PersonalOS. Nutzen bei „merk dir das“, „speicher das“, „sortier die Inbox“, „leg das ab“, „hier ein Dokument zum Einarbeiten“. Für Gesprächs-Transkripte stattdessen transkript-einarbeiten.
---

# Info einsortieren

## Ablauf

1. **Was ist es?** Fakt, Regel, Ablaufschritt, Fachwissen, Personeninfo, Aufgabe, Idee.
2. **Gibt es schon einen Ort?** Erst suchen (Dateinamen und Inhalt), dann anlegen. Eine Aussage, ein Ort.
3. **Einsortieren** nach der Tabelle, mit Quelle in Klammern und Datum.
4. **Melden**, wohin es gegangen ist (Pfad als Link), damit {{NAME}} es wiederfindet.

| Art | Ziel |
|---|---|
| Fakt zu einem Kunden oder Auftrag | Kundenakte, „Wissen & Notizen“ |
| Info über eine Person | `03 Bereiche/Personen/<Name>.md` |
| Schreibregel, Wunschformulierung | `00 Kontext/Schreibstil.md` |
| Arbeitsschritt, Werkzeug, Prüfung | `03 Bereiche/Abläufe/<Ablauf>.md` |
| Fachwissen, Vorschrift, Fundstelle | `04 Wissen/<Thema>/` |
| Grundsätzliche Regel („ab jetzt immer“) | Entscheidungsnotiz plus Zeile in der AGENTS.md |
| Aufgabe | Aufgabenort laut AGENTS.md |
| Unklar | bleibt datiert in `01 Inbox/Brain Dump.md`, mit Frage an {{NAME}} |

## Dokumente

Ein Dokument (PDF, Word, Foto) wird gelesen, die Essenz kommt mit Fundstelle ins Vault, das Original bleibt in `01 Inbox/_eingang/` oder im Kundenordner außerhalb des Vaults. Nur Dateien, die in einer Notiz eingebettet werden sollen und nichts Vertrauliches enthalten, wandern nach `07 Anhänge/`.

## Inbox aufräumen

1. `Brain Dump.md`: jeden Eintrag einsortieren oder als „geparkt“ stehen lassen. Einsortierte Einträge mit Verweis auf das Ziel durchstreichen, nicht löschen.
2. `Vorschläge/`: je Vorschlag {{NAME}} fragen (übernehmen, ändern, verwerfen). Übernommene einarbeiten, die Vorschlagsdatei danach nach `06 Archiv/Vorschläge/` verschieben.
3. `_eingang/`: Liegt dort ein Transkript, `transkript-einarbeiten` nutzen.

Zum Schluss `vault_pruefung.py alles --geaendert`.
