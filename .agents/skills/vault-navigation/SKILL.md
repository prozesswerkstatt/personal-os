---
name: vault-navigation
description: Findet Wissen im PersonalOS zuverlässig wieder, indem der Agent sich über Übersichtsnotizen, Dateinamen, Volltext, Wikilinks und Daily Notes durch die Markdown-Dateien bewegt und mit Fundstelle antwortet. Nutzen vor jeder Aufgabe, die Kontext braucht, und bei Fragen wie „was weiß ich über …“, „wie haben wir das damals gelöst“, „gibt es dazu schon was“, „wo steht …“, „wann war …“, „welcher Kunde hatte …“. Nicht zum Ablegen neuer Infos (dafür info-einsortieren) und nicht für Transkripte (transkript-einarbeiten).
---

# Vault-Navigation

Ziel: Die Antwort aus den eigenen Dateien holen, schnell und belegt, statt zu raten oder alles zu lesen. Das Vault ist ein Netz aus kleinen Markdown-Dateien. Man findet etwas, indem man am richtigen Einstieg anfängt und den Links folgt.

## 1. Einstieg wählen

Erst überlegen, welcher Art die Frage ist, dann dort anfangen:

| Frage nach … | Erster Ort | Danach |
|---|---|---|
| einem Kunden, Auftrag, einer Maschine beim Kunden | `02 Projekte/Kunden/_Kunden-Übersicht.md` | Kundenakte: zuerst „Aktueller Stand“, dann „Wissen & Notizen“, dann Änderungs-Log |
| einer Person | `03 Bereiche/Personen/Personen.md` | Personennotiz, verlinkte Kundenakte |
| „Wie mache ich …“, Arbeitsweise | `03 Bereiche/Abläufe/Abläufe.md` | Ablaufnotiz, ggf. passender Skill |
| Fachwissen, Normen, Hersteller, Bauteile | `04 Wissen/Wissen.md` | Themenordner, `Vorschriften & Normen/`, `Referenzen/` |
| einer früheren Lösung oder einem alten Projekt | `04 Wissen/Referenzen/` | verlinkte Kundenakte, Änderungs-Log |
| „Was war am …“, „Wann haben wir …“ | `05 Daily Notes/` (Dateiname = Datum, neueste zuerst) | verlinkte Akten |
| „Warum machen wir das so?“ | `03 Bereiche/Entscheidungen/` | `AGENTS.md`, Abschnitt Entscheidungen |
| Ton, Anrede, Formulierungen | `00 Kontext/Schreibstil.md` | `00 Kontext/Über mich.md` |
| laufenden Vorhaben | `02 Projekte/` | Projektnotiz, „Aktueller Stand“ |

## 2. Suchen, in dieser Reihenfolge

1. **Übersichtsnotiz lesen** (Tabelle oben). Sie verlinkt meist schon direkt auf die richtige Notiz.
2. **Dateinamen suchen.** Dateinamen sind sprechend (`Beschreibender Name.md`), deshalb zuerst nach Namen suchen, etwa alle Dateien mit „Hydraulik“ im Namen.
3. **Volltext suchen**, wenn der Name nichts bringt. Mehrere Schreibweisen probieren: Abkürzung und Langform, Teilenummer mit und ohne Leerzeichen, Firmenname mit und ohne Rechtsform, Begriff mit Umlaut und in alter Umschreibung (ä und ae), Einzahl und Mehrzahl.
4. **Links folgen.** `[[Wikilinks]]` in der gefundenen Notiz zeigen, wo Details stehen. Rückwärts suchen: Wer verlinkt auf diese Notiz? (Volltext nach `[[Notizname`).
5. **Frontmatter nutzen**, um einzugrenzen: `tags` (etwa `kunde`, `person`, `ablauf`, `wissen`), `status` (aktiv, pausiert, abgeschlossen), `date`.
6. **Archiv zuletzt.** `06 Archiv/` nur durchsuchen, wenn aktive Notizen nichts liefern, und das in der Antwort sagen.

Werkzeuge: In Claude Code die eingebauten Such- und Lesewerkzeuge verwenden, sie funktionieren unter Windows und macOS gleich. Notfalls in der Shell: `grep -ril "begriff" .` (macOS, Git Bash) oder `Select-String -Path .\*\*.md -Pattern "begriff"` (PowerShell). Verzeichnisse `.git/`, `.obsidian/` und `01 Inbox/_eingang/` beim Suchen auslassen, außer es geht ausdrücklich um Rohmaterial.

## 3. Sparsam lesen

- Bei Akten zuerst nur „Aktueller Stand“ lesen. Weiter nur, wenn die Frage es braucht.
- Höchstens zwei Link-Sprünge vom Einstieg aus. Reicht das nicht, sagen, was gefunden wurde, und fragen, ob weiter gesucht werden soll.
- Große Dateien abschnittsweise lesen, nicht komplett.

## 4. Was gilt, wenn Stellen sich widersprechen

Reihenfolge der Verlässlichkeit:

1. „Aktueller Stand“ einer Akte und Entscheidungsnotizen
2. Fachnotizen in `04 Wissen/` mit Quelle
3. Änderungs-Log und Daily Notes (zeigen, wie es war, nicht unbedingt, wie es ist)
4. `01 Inbox/` und Agenten-Vorschläge (noch nicht geprüft)

Widersprüche nie still auflösen. Beide Fundstellen nennen und fragen, welche stimmt. Danach die falsche Stelle korrigieren (Regel „eine Aussage, ein Ort“).

## 5. Antworten

- **Mit Fundstelle:** Pfad der Notiz, Abschnitt, und das Datum oder die Quelle, die dort in Klammern steht. Beispiel: „Laut `02 Projekte/Kunden/Muster GmbH/Muster GmbH.md`, Wissen & Notizen (Telefonat 12.03.2027): …“
- **Belegt und abgeleitet getrennt.** Was so in einer Notiz steht, ist belegt. Eigene Schlüsse stehen als „Annahme“ darunter.
- **Nichts gefunden:** Sagen, wo gesucht wurde und mit welchen Begriffen. Nicht raten. Anbieten, die Antwort nach Klärung abzulegen (Skill `info-einsortieren`).

## 6. Das Netz pflegen, damit es auffindbar bleibt

Jede neue Notiz, die bei der Arbeit entsteht:

- bekommt einen sprechenden Dateinamen und Frontmatter,
- wird in der passenden Übersichtsnotiz verlinkt (Kunden-Übersicht, Personen, Abläufe, Wissen),
- verlinkt selbst auf Kunde, Person oder Projekt, zu dem sie gehört.

Findet sich bei der Suche eine Notiz, die in keiner Übersicht steht, den Link dort ergänzen und das kurz erwähnen. Kaputte Links meldet `vault-pruefung`.
