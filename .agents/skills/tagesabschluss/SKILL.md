---
name: tagesabschluss
description: Schließt eine Arbeitssession oder einen Tag sauber ab. Schreibt die Daily Note mit Ergebnissen und Zeiterfassung, zieht Akten und Abläufe nach, prüft das Vault und sichert es nach GitHub. Nutzen bei „Tagesabschluss“, „Feierabend“, „schreib die Daily Note“, „sicher alles“, oder wenn eine Session mit Änderungen im Vault endet. Ohne Rückfrage ausführen.
---

# Tagesabschluss

1. **Daily Note** `05 Daily Notes/YYYY-MM-DD.md` anlegen (aus `_vorlagen/Daily Note.md`) oder ergänzen:
   - „Was heute gelaufen ist“: je Kunde oder Projekt ein Punkt mit Wikilink und Ergebnis.
   - „Offen / Morgen“: nur Verweise auf den Aufgabenort, keine Checkboxen.
   - „Zeiterfassung“: Tätigkeit, Dauer, `[M]` für Zeit von {{NAME}} selbst (Termine, Vor-Ort, eigene Arbeit), `[KI]` für Arbeit, die ein Agent ausgeführt hat.
2. **Nachziehen**, falls in der Session noch nicht geschehen: „Aktueller Stand“ und Änderungs-Log der betroffenen Akten, neue Entscheidungen, Korrekturen in Schreibstil oder Abläufen.
3. **Prüfen:** `python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles --geaendert`. Neue kaputte Links beheben.
4. **Sichern:** `tools/sichern.sh "Tagesabschluss YYYY-MM-DD"`. Meldet das Skript einen Konflikt, nichts erzwingen, sondern {{NAME}} Bescheid geben.
5. **Kurz melden:** was erledigt ist, was morgen ansteht, ob die Sicherung durchgelaufen ist.
