---
name: vorlage-aktualisieren
description: Holt neue oder verbesserte Skills, Werkzeuge und Notizvorlagen aus der PersonalOS-Vorlage in ein eingerichtetes Vault, ohne persönliche Inhalte anzufassen. Nutzen bei „aktualisiere die Vorlage“, „gibt es neue Skills“, „zieh die Skills nach“, „Update der Vorlage“. Nicht für eigene neue Skills (dafür ablauf-zu-skill).
---

# Vorlage aktualisieren

Ein eingerichtetes Vault besteht aus zwei Arten von Dateien:

- **Systemdateien** (kommen aus der Vorlage, dürfen aktualisiert werden): `.agents/skills/`, `tools/`, `_vorlagen/`, `.gitattributes`, `VORLAGE-VERSION`, `CHANGELOG.md`, `LIZENZEN/`.
- **Inhalte** (gehören der Person, werden nie überschrieben): alles andere, insbesondere `00 Kontext/` bis `07 Anhänge/` und `AGENTS.md`.

## Ablauf

1. **Quelle prüfen.** `git remote -v` muss einen Remote `vorlage` zeigen. Fehlt er:
   `git remote add vorlage https://github.com/prozesswerkstatt/personal-os.git`
   Niemals nach `vorlage` pushen.
2. **Stand holen:** `git fetch vorlage`
3. **Vergleichen.** Eigene Version in `VORLAGE-VERSION` gegen `git show vorlage/main:VORLAGE-VERSION`. Gleich: fertig, melden. Sonst die neuen Einträge aus `git show vorlage/main:CHANGELOG.md` zeigen.
4. **Was sich ändert:** `git diff --stat HEAD vorlage/main -- .agents/skills tools _vorlagen .gitattributes`
   Eigene Skills (die es in der Vorlage nicht gibt) bleiben unberührt. Hat die Person einen Vorlagen-Skill selbst angepasst (im Diff zu sehen), diesen Skill nicht überschreiben, sondern die Unterschiede zeigen und fragen.
5. **Freigabe holen.** Liste zeigen: neu, geändert, selbst angepasst. Erst nach Okay weiter.
6. **Übernehmen**, nur die freigegebenen Pfade:
   `git checkout vorlage/main -- <pfad> [<pfad> …]`
   dazu `VORLAGE-VERSION` und `CHANGELOG.md`. Übernommene Dateien enthalten wieder die Platzhalter der Vorlage (Großbuchstaben in doppelten geschweiften Klammern, etwa NAME). Diese sofort mit den Werten ersetzen, die beim Erststart gewählt wurden: Name und Tätigkeit stehen oben in `AGENTS.md`, der Aufgabenort im Abschnitt „Aufgaben“. Kontrolle: `vault_pruefung.py platzhalter --liste` meldet 0.
7. **AGENTS.md** nie komplett ersetzen, sie enthält persönliche Regeln. Bringt die neue Version Änderungen an Regelabschnitten oder neue Zeilen in der Skill-Tabelle, diese gezielt einfügen und vorher zeigen.
8. **Skills sichtbar machen:** `tools/einrichten.sh` ausführen (Windows: `bash tools/einrichten.sh` in Git Bash). Unter Windows ist das Pflicht, weil die Skills dort als Kopie unter `.claude/skills/` liegen.
9. **Prüfen:** `python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles` (Windows `py`).
10. **Festhalten:** Commit „Vorlage auf X.Y.Z aktualisiert“, Eintrag in der Daily Note, danach `tools/sichern.sh`.

Claude Code im Vault-Ordner danach neu starten, damit neue Skills geladen werden.
