---
name: erststart
description: Richtet ein frisch aus der PersonalOS-Vorlage erzeugtes Vault für seine Person ein. Führt ein kurzes Interview, ersetzt alle Platzhalter in doppelten geschweiften Klammern, füllt 00 Kontext, legt die erste Daily Note an und prüft das Ergebnis. Nutzen, wenn das Vault neu ist, die AGENTS.md noch Platzhalter enthält oder jemand sagt „richte mein PersonalOS ein“, „Erststart“, „wir fangen an“. Nicht für die laufende Arbeit.
---

# Erststart

Die Platzhalter heißen im Vault so wie unten in Großbuchstaben, eingefasst in doppelte geschweifte Klammern. Hier stehen sie ohne Klammern, damit dieser Skill sich beim Ersetzen nicht selbst verändert.

Ziel: Nach rund 20 Minuten ist das Vault auf die Person zugeschnitten, ohne einen einzigen offenen Platzhalter, und der erste echte Inhalt ist drin.

## Vorab prüfen

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py platzhalter --liste
```

Gibt es keine offenen Platzhalter, ist der Erststart schon erledigt. Dann nicht erneut ausführen, sondern fragen, was ergänzt werden soll.

Liegt schon Material vor (Transkript eines Erstgesprächs, Website, Unterlagen in `01 Inbox/_eingang/`), lies es zuerst und fülle damit vor. Frag dann nur noch, was fehlt oder unsicher ist.

## Interview

Frag einzeln, warte jeweils auf die Antwort. Fasse am Ende jeder Antwort kurz zusammen, was du verstanden hast.

1. Name, Tätigkeit, Firma. → `NAME`, `TAETIGKEIT`, `KURZPROFIL`
2. Was genau machst du, welche Leistungen, welche Arten von Aufträgen? → `TAETIGKEIT_AUSFUEHRLICH`, `LEISTUNG` (eine Tabellenzeile je Leistung)
3. Wer sind deine Kunden, wie kommen sie zu dir? → `KUNDEN`
4. Mit welchen Werkzeugen arbeitest du (Software, Ablage, Mail, Kalender, Rechnungen)? Was willst du selbst behalten, was darf die KI übernehmen? → `ARBEITSWEISE`
5. Was ist dir gegenüber Kunden wichtig? → `WERTE`
6. Wie soll die KI mit dir arbeiten: knapp oder ausführlich, wann nachfragen, was nie ohne dich? → `KI_ZUSAMMENARBEIT`
7. Duzt oder siezt du deine Kunden? Wie klingst du? Ein, zwei Beispielmails helfen. → `ANREDE`, `TON`, Beispiele in `Schreibstil.md`
8. Wo führst du Aufgaben (Papier, App, Kalender, eine Notiz im Vault)? → `AUFGABEN_ORT`. Ohne eigenes Werkzeug: `die Notiz [[Aufgaben]] im Vault` und die Notiz `01 Inbox/Aufgaben.md` anlegen.

`DATUM` ist das heutige Datum im Format `YYYY-MM-DD`.

## Einsetzen

1. Platzhalter in allen Dateien ersetzen, auch in `_vorlagen/`, README und Skills. Ersetzt werden alle Großbuchstaben-Platzhalter in doppelten geschweiften Klammern. Nur die Obsidian-Variablen in Kleinbuchstaben (date, title und date mit Format) in `_vorlagen/` bleiben stehen, die füllt Obsidian beim Anlegen.
2. Fehlt eine Antwort, statt Platzhalter „noch offen (Erststart TT.MM.JJJJ)“ eintragen. Nichts erfinden.
3. Erste Daily Note `05 Daily Notes/YYYY-MM-DD.md` aus der Vorlage anlegen: „PersonalOS eingerichtet“.
4. Werden im Gespräch schon Kunden, Personen oder Abläufe genannt, je eine Notiz aus der passenden Vorlage anlegen und verlinken.

## Abschluss

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles
```

Erwartung: 0 kaputte Links, 0 offene Platzhalter. Danach `tools/einrichten.sh` (falls noch nicht geschehen) und `tools/sichern.sh`.

Zum Schluss der Person in drei Sätzen sagen, wie es weitergeht: Rohmaterial nach `01 Inbox/_eingang/`, dann „arbeite das Transkript ein“; Abläufe beschreiben lassen; am Tagesende „Tagesabschluss“.
