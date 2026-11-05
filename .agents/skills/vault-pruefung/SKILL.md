---
name: vault-pruefung
description: Prüft Texte und das Vault mechanisch statt nach Gefühl. (1) Jeder Text nach außen wird vor der Ausgabe geprüft auf Umlaut-Ersatz, Gedankenstriche und harte Umbrüche im Absatz. (2) Nach Änderungen meldet die Prüfung kaputte Wikilinks, fehlendes Frontmatter und offene Platzhalter. Nutzen vor jedem Copy-Paste-Text, am Ende jeder Session mit Änderungen, bei „prüf den Vault“, „sind Links kaputt“. Ändert nie eine Datei.
---

# Vault-Prüfung

Nur lesend. Braucht nur Python 3 ohne Zusatzpakete.

## Texte prüfen (vor jeder Ausgabe)

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py text <datei>
printf '%s' "$TEXT" | python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py text -
```

`OK` heißt: Text darf raus. Bei Treffern korrigieren und erneut prüfen. Das Umlaut-Wörterbuch lernt aus dem Vault selbst, deshalb bleiben `dass`, `neue`, `Quelle` erlaubt.

## Vault prüfen (nach Änderungen)

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles --geaendert
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py platzhalter --liste
```

| Prüfung | Meldet |
|---|---|
| `links` | `[[Wikilinks]]` ohne Zieldatei |
| `frontmatter` | gepflegte Notizen ohne YAML-Kopf |
| `checkboxen` | offene Checkboxen in Daily Notes (Aufgaben gehören an den Aufgabenort) |
| `platzhalter` | nicht ausgefüllte Platzhalter, also offener Erststart |

Nicht geprüft werden `_eingang/`, `_vorlagen/`, `_input/`, `_output/`, `tmp/`, `.obsidian/`, `.claude/`.

Herkunft: Prüfskript aus dem Second Brain der ProzessWerkstatt, Idee aus der PersonalOS-Boilerplate von Vincent Mumme (MIT).

Unter Windows heißt der Aufruf meist `py` statt `python3` (Python von python.org). Die Befehle oben gelten dann mit `py` am Anfang.
