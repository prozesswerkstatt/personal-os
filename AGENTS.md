# PersonalOS von {{NAME}}

Dieses Vault ist das Zweite Gehirn von {{NAME}} ({{TAETIGKEIT}}). Es hält Abläufe, Fachwissen, Kunden, Entscheidungen und den Tagesverlauf als verknüpfte Markdown-Dateien fest. Die Dateien gehören {{NAME}}. Jeder KI-Agent (Claude Code, Codex, Gemini, ein lokales Modell) arbeitet mit denselben Dateien, deshalb lässt sich der Anbieter jederzeit wechseln.

**Eine Regeldatei für alle Agenten.** Diese `AGENTS.md` gilt für jeden Agenten. Die `CLAUDE.md` lädt sie nur per `@AGENTS.md`. Regeln werden ausschließlich hier gepflegt.

> Stehen in dieser Datei noch Platzhalter in doppelten geschweiften Klammern, ist der Erststart nicht abgeschlossen. Dann zuerst den Skill `erststart` ausführen.

## Bevor du arbeitest

1. Lies `00 Kontext/Über mich.md` (wer, was, wie) und bei Texten zusätzlich `00 Kontext/Schreibstil.md`.
2. Suche den Ort, an dem die Antwort schon steht, bevor du rätst. Erst lesen, dann antworten.
3. Gibt es für die Aufgabe einen Skill (Liste unten), nutze ihn statt frei zu arbeiten.

## Grundregeln

1. **Eine Aussage, ein Ort.** Jede aktuelle Information steht an genau einer Stelle. Andere Notizen verlinken mit `[[Wikilinks]]` dorthin, statt zu kopieren.
2. **Quelle in Klammern.** Neue Aussagen aus Gesprächen, Mails oder Dokumenten bekommen ihre Herkunft, zum Beispiel „(Telefonat Müller 12.03.2027)“.
3. **Belegt statt geschätzt.** Als Tatsache gilt nur, was eine Quelle trägt. Abgeleitetes steht getrennt darunter als „Annahme“. Lässt sich etwas nicht klären, sag das offen und nenne, wie man es prüfen kann.
4. **Eingang ist noch keine Wahrheit.** Transkripte, Notizen und Dokumente sind zuerst nur Quellen. Erst die geprüfte Kernaussage wandert in die zuständige Notiz.
5. **Aktueller Stand oben, Verlauf unten.** Kundenakten und Projekte haben oben den Abschnitt „Aktueller Stand“ (höchstens fünf Sätze, wird neu geschrieben, nicht ergänzt). Darunter wächst ein datiertes Änderungs-Log, aus dem nichts gelöscht wird.
6. **Nichts nach außen ohne Freigabe.** Mails, Nachrichten, Veröffentlichungen, Zahlungen und Kalendereinträge bei anderen bereitest du als Entwurf vor. Abgeschickt wird erst nach ausdrücklichem Okay von {{NAME}} zu genau diesem Text.
7. **Prüfpunkte bleiben beim Menschen.** Arbeitsergebnisse mit Außenwirkung (Gutachten, Angebote, Berichte) legst du {{NAME}} vor der Freigabe zur Kontrolle vor und sagst, was du geprüft hast und was nicht.
8. **Nicht löschen, nicht überschreiben ohne Rückfrage.** Verschieben und Archivieren nur auf Ansage.
9. **Keine Geheimnisse im Vault.** Passwörter, API-Schlüssel und Zugangsdaten gehören nicht in Notizen und nie in den Chat. Wo sie liegen, darf notiert werden.
10. **Rohdaten bleiben draußen.** Roh-Transkripte, Mietverträge, Ausweise und ähnliche Unterlagen landen nur in `01 Inbox/_eingang/` (von Git ausgeschlossen) oder im Kundenordner außerhalb des Vaults. Ins Vault kommt die destillierte Essenz mit Quellenangabe.

## Ordner

| Ordner | Was hinein gehört |
|---|---|
| `00 Kontext/` | Wer {{NAME}} ist, Angebot, Schreibstil. Pflichtlektüre bei Texten und Kundenkontakt. |
| `01 Inbox/` | Schnelle Gedanken (`Brain Dump.md`), Vorschläge von Agenten (`Vorschläge/`), Rohmaterial zum Einarbeiten (`_eingang/`, nicht in Git). |
| `02 Projekte/` | Vorhaben mit Ziel und Ende. Eine Datei je Projekt, ein Unterordner nur bei vielen Dateien. Kundenakten unter `02 Projekte/Kunden/<Kunde>/<Kunde>.md`. |
| `03 Bereiche/` | Laufende Verantwortung ohne Enddatum. Darin `Abläufe/` (wie {{NAME}} arbeitet, Schritt für Schritt), `Entscheidungen/` (eine Notiz je festgelegter Regel) und `Personen/` (eine Notiz je Person). |
| `04 Wissen/` | Fachwissen mit Quelle: Vorschriften und Normen, Referenzen (ausgewertete frühere Arbeiten), Werkzeuge. Je Thema ein Ordner. |
| `05 Daily Notes/` | Tageslogbuch `YYYY-MM-DD.md`. Was passiert ist, Zeiterfassung, offene Punkte als Verweis. |
| `06 Archiv/` | Abgeschlossenes, nur auf Ansage verschieben. |
| `07 Anhänge/` | Bilder und PDFs, die in Notizen eingebettet sind. |
| `_vorlagen/` | Vorlagen für neue Notizen. Immer von dort ausgehen. |

## Dateien und Schreibweise

- Dateinamen in normaler Schreibweise mit Leerzeichen: `Beschreibender Name.md`. Daily Notes als `YYYY-MM-DD.md`, Entscheidungen als `YYYY-MM-DD Kurzer Satz.md`.
- Jede gepflegte Notiz beginnt mit YAML-Frontmatter (`tags`, `status`, `date`).
- Notizen atomar halten: eine Sache pro Notiz. Ausnahme: Daily Notes fassen einen Tag zusammen.
- Echte Umlaute (ä, ö, ü, ß), nie ae, oe, ue, ss als Ersatz. ASCII nur, wo Technik es erzwingt (Dateinamen von Skripten, IDs).
- Weitere Schreibregeln für Texte nach außen stehen in `00 Kontext/Schreibstil.md`.

## Aufgaben

Aufgaben leben an genau einem Ort: {{AUFGABEN_ORT}}. Daily Notes und Akten verlinken nur dorthin, sie führen keine eigenen Checkbox-Listen.

## Skills

Skills liegen unter `.agents/skills/<name>/SKILL.md`. Der spezifischste passende Skill gewinnt.

| Wenn … | Skill |
|---|---|
| das Vault neu ist oder noch Platzhalter enthält | `erststart` |
| ein Transkript (Call, Termin, Sprachnachricht, Ortstermin) eingearbeitet werden soll | `transkript-einarbeiten` |
| ein Dokument, eine Notiz oder Infos einsortiert werden sollen, oder die Inbox aufgeräumt wird | `info-einsortieren` |
| ein Arbeitstag oder eine Session endet | `tagesabschluss` |
| ein Ablauf sich wiederholt und als Skill festgehalten werden soll | `ablauf-zu-skill` |
| ein Text nach außen geht oder das Vault nach Änderungen geprüft wird | `vault-pruefung` |

Neue Skills entstehen mit `ablauf-zu-skill` aus einer Notiz unter `03 Bereiche/Abläufe/`. Ein Skill führt einen Ablauf aus, die Regeln stehen hier.

## Lernen aus Korrekturen

Korrigiert {{NAME}} ein Ergebnis („so nicht, sondern so“), hältst du die Korrektur am richtigen Ort fest, damit sie nicht wieder passiert: Schreibregeln in `00 Kontext/Schreibstil.md`, Arbeitsschritte im Ablauf oder Skill, eine grundsätzliche Regel als Entscheidungsnotiz unter `03 Bereiche/Entscheidungen/` plus eine Zeile hier. Sag in der Antwort, wo du es festgehalten hast.

## Nach jeder Arbeit im Vault

1. Prüfen: `python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles --geaendert` (unter Windows `py` statt `python3`). Eine Session hinterlässt keine neuen kaputten Links.
2. Daily Note ergänzen (Skill `tagesabschluss`).
3. Sichern: `tools/sichern.sh` (holt den Stand, committet und pusht nach GitHub). Unter Windows in Git Bash ausführen.

## Antworten an {{NAME}}

Ergebnis zuerst, Technik zuletzt. Bei längeren Antworten diese Gliederung, leere Abschnitte weglassen:

```text
Erledigt              (höchstens fünf Punkte)
Kurzfassung           (drei bis fünf Sätze)
Offene Entscheidungen (nur wo {{NAME}} entscheiden muss)
Nächste Schritte
Technische Details    (optional)
```

## Entscheidungen

Festgelegte Arbeitsregeln stehen einzeln unter `03 Bereiche/Entscheidungen/` mit Anlass und Begründung. Neue Regel: Entscheidungsnotiz aus `_vorlagen/Entscheidung.md` anlegen und hier unter der passenden Überschrift eine Zeile mit Link ergänzen.

- [[Wie dieses PersonalOS entstanden ist]]
