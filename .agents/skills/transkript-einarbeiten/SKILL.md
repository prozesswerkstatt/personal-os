---
name: transkript-einarbeiten
description: Arbeitet ein Transkript (Kundentermin, Telefonat, Ortstermin, Sprachnachricht, Diktat, Beobachtungstermin) nachvollziehbar ins PersonalOS ein. Trennt Belegtes von Annahmen, schreibt nur die Essenz mit Zeitstempel in die zuständigen Notizen, hält Zusagen fest und kopiert nie das Rohtranskript ins Vault. Nutzen bei „arbeite das Transkript ein“, „hier die Aufnahme“, „Gespräch auswerten“, „was haben wir besprochen“, oder wenn eine neue Datei in 01 Inbox/_eingang/ liegt.
---

# Transkript einarbeiten

Transkripte sind der wichtigste Weg, auf dem das PersonalOS wächst. Jedes Gespräch macht Akten, Abläufe und Wissen ein Stück genauer. Dafür muss die Übernahme sauber sein: Eingang ist noch keine Wahrheit.

## 1. Quelle lesen, vollständig

- Lies das ganze Transkript, nicht nur den Anfang. Lange Dateien in Abschnitten.
- Notiere Art, Datum, Dauer, Teilnehmer und Ablageort der Rohdatei.
- Sprecherzuordnung ist oft fehlerhaft. Ordne Sprecher über den Inhalt zu und markiere Unsicheres.
- Automatische Transkripte verhören Namen, Fachbegriffe und Software. Unsichere Schreibweisen als „unsicher“ markieren und nicht nach außen verwenden, bis sie schriftlich bestätigt sind.

## 2. Zuordnen

Zu welchem Kunden, Projekt oder Ablauf gehört das Gespräch? Bei Zweifel kurz fragen. Gibt es den Kunden noch nicht, Akte aus `_vorlagen/Kundenakte.md` anlegen und in `02 Projekte/Kunden/_Kunden-Übersicht.md` eintragen.

## 3. Bestand lesen, bevor du schreibst

Lies die betroffenen Notizen ganz. Kläre:

- Was gilt schon?
- Was ist wirklich neu oder anders?
- Welche Aussage ersetzt einen alten Stand?
- Was bleibt offen?

## 4. Einarbeiten

| Was im Gespräch steckt | Wohin |
|---|---|
| Fakten zum Kunden, Auftrag, Objekt | Kundenakte, Abschnitt „Wissen & Notizen“ |
| Neues über eine Person | ihre Notiz unter `03 Bereiche/Personen/` |
| Wie {{NAME}} arbeitet (Schritte, Werkzeuge, Prüfungen) | passende Notiz unter `03 Bereiche/Abläufe/` |
| Fachwissen, Vorschriften, Argumentationen | `04 Wissen/` |
| Festgelegte Regel („ab jetzt immer …“) | Entscheidungsnotiz plus Zeile in der AGENTS.md |
| Zusagen und Aufgaben | Aufgabenort laut AGENTS.md, in der Daily Note nur als Verweis |

Regeln dafür:

- Jede übernommene Aussage bekommt Quelle und Zeitstempel, zum Beispiel „(Telefonat 12.03.2027, 14:20)“.
- Vermutungen und eigene Schlüsse stehen als „Annahme“ getrennt.
- Keine erfundenen Teilnehmer, Fristen, Preise oder Zusagen. Was nicht klar gesagt wurde, bleibt offene Frage.
- Das Rohtranskript wird nicht ins Vault kopiert. Bei sehr ergiebigen Gesprächen eine Auswertung aus `_vorlagen/Transkript-Auswertung.md` anlegen.
- Danach den „Aktuellen Stand“ der Akte neu schreiben (höchstens fünf Sätze) und eine Zeile ins Änderungs-Log.

## 5. Beobachtungstermine (Ablauf aufnehmen)

Wurde {{NAME}} beim Arbeiten begleitet (Bildschirm, Ortstermin), ist das wichtigste Ergebnis die Ablaufnotiz:

- jeden Schritt in Reihenfolge, mit Werkzeug und Ergebnis,
- welche Angaben woher kommen,
- wo {{NAME}} prüft oder entscheidet (Prüfpunkte),
- was am Ende zwingend drinstehen muss,
- Sonderfälle, die nebenbei erwähnt wurden.

Lücken als offene Fragen an den Schluss der Ablaufnotiz, damit sie im nächsten Termin geklärt werden.

## 6. Prüfen und berichten

```bash
python3 .agents/skills/vault-pruefung/scripts/vault_pruefung.py alles --geaendert
```

Bericht an {{NAME}}: welche Quelle verarbeitet wurde, welche Notizen sich geändert haben, welche Zusagen entstanden sind, was unsicher oder offen bleibt. Nichts wird verschickt, Mails nur als Entwurf.
