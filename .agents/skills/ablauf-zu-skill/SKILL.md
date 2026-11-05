---
name: ablauf-zu-skill
description: Macht aus einem beschriebenen, wiederkehrenden Ablauf einen Skill, den ein Agent ausführen kann, oder verbessert einen bestehenden Skill nach einer Korrektur. Nutzen bei „mach daraus einen Skill“, „das machen wir jetzt immer so“, „der Ablauf soll automatisch laufen“, oder wenn eine Ablaufnotiz den Status stabil erreicht.
---

# Ablauf zu Skill

Ein Skill ist die ausführbare Fassung einer Ablaufnotiz. Die Ablaufnotiz unter `03 Bereiche/Abläufe/` bleibt die Beschreibung für Menschen, der Skill unter `.agents/skills/<name>/SKILL.md` die Arbeitsanweisung für den Agenten. Beide verlinken aufeinander.

## Wann ein Ablauf reif ist

- Er kam mindestens zweimal gleich vor.
- Ziel, Eingangsdaten und das, was am Ende drinstehen muss, sind beschrieben.
- Die Prüfpunkte sind klar: wo {{NAME}} draufschaut, bevor es weitergeht.

Fehlt etwas davon, zuerst die Lücken als Fragen an {{NAME}} stellen oder im nächsten Beobachtungstermin klären.

## Bauen

1. Ordnername in Kleinbuchstaben mit Bindestrichen, ohne Umlaute (`verkehrswert-gutachten`).
2. Aufbau nach `references/master-skill-muster.md`: Ziel, Auslöser, Eingangsdaten mit Nachfrage bei Lücken, Schritte, Prüfpunkte, Qualitätsprüfung gegen das Ziel, Ablage, Grenzen.
3. Große Abläufe als Master-Skill mit Unterschritten. Ein Unterschritt wird erst dann ein eigener Skill, wenn er auch allein gebraucht wird.
4. Die `description` im Kopf nennt die Formulierungen, mit denen {{NAME}} den Ablauf anstößt. Danach wählt der Agent den Skill aus.
5. Eintragen: Zeile in der Skill-Tabelle der AGENTS.md, Feld `skill:` und Tabelle in `03 Bereiche/Abläufe/Abläufe.md`.
6. `tools/einrichten.sh` erneut laufen lassen, damit Claude Code den neuen Skill findet.

## Testen

An einem echten, abgeschlossenen Fall durchspielen und das Ergebnis mit dem Original vergleichen. Abweichungen in den Skill zurückschreiben. Erst danach an neuen Fällen einsetzen, mit Prüfpunkten.

## Verbessern nach Korrektur

Korrigiert {{NAME}} ein Ergebnis, kommt die Korrektur direkt in den Skill (und in die Ablaufnotiz), datiert im Abschnitt „Verlauf“. So lernt das System im Tun.
