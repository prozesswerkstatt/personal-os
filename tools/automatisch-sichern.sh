#!/usr/bin/env bash
# Richtet eine automatische Sicherung um 07:30 und 18:00 ein.
# Aufruf: tools/automatisch-sichern.sh an | aus
#
# macOS: LaunchAgent. Liegt das Vault unter ~/Desktop oder ~/Documents, braucht /bin/bash
#   Festplattenvollzugriff (Systemeinstellungen > Datenschutz & Sicherheit), sonst scheitert
#   der Lauf ohne sichtbare Meldung. Protokoll: ~/Library/Logs/personalos-sichern.log
# Windows (in Git Bash ausführen): zwei Aufgaben in der Windows-Aufgabenplanung.
#   Läuft nur, solange der Benutzer angemeldet ist. Protokoll: tools/sichern.log
#   Prüfen: schtasks /Query /TN "PersonalOS Sicherung 0730"
set -euo pipefail
vault="$(cd "$(dirname "$0")/.." && pwd)"

windows_an() {
  local bash_exe vault_win ziel
  bash_exe="$(cygpath -w "$(command -v bash)")"
  vault_win="$(cygpath -w "$vault")"
  ziel="\"$bash_exe\" -lc \"cd '$vault' && tools/sichern.sh >> tools/sichern.log 2>&1\""
  for zeit in 07:30 18:00; do
    MSYS_NO_PATHCONV=1 schtasks /Create /F /SC DAILY /ST "$zeit" \
      /TN "PersonalOS Sicherung ${zeit/:/}" /TR "$ziel" >/dev/null
  done
  echo "Automatische Sicherung an (07:30 und 18:00, Aufgabenplanung). Vault: $vault_win"
  echo "Protokoll: tools/sichern.log"
}

windows_aus() {
  for zeit in 0730 1800; do
    MSYS_NO_PATHCONV=1 schtasks /Delete /F /TN "PersonalOS Sicherung $zeit" >/dev/null 2>&1 || true
  done
  echo "Automatische Sicherung aus."
}

mac_an() {
  local label="de.prozesswerkstatt.personalos.sichern"
  local plist="$HOME/Library/LaunchAgents/$label.plist"
  local log="$HOME/Library/Logs/personalos-sichern.log"
  cat > "$plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$label</string>
  <key>ProgramArguments</key>
  <array><string>/bin/bash</string><string>$vault/tools/sichern.sh</string></array>
  <key>StartCalendarInterval</key>
  <array>
    <dict><key>Hour</key><integer>7</integer><key>Minute</key><integer>30</integer></dict>
    <dict><key>Hour</key><integer>18</integer><key>Minute</key><integer>0</integer></dict>
  </array>
  <key>StandardOutPath</key><string>$log</string>
  <key>StandardErrorPath</key><string>$log</string>
</dict>
</plist>
PLIST
  launchctl unload "$plist" 2>/dev/null || true
  launchctl load "$plist"
  echo "Automatische Sicherung an (07:30 und 18:00). Protokoll: $log"
}

mac_aus() {
  local plist="$HOME/Library/LaunchAgents/de.prozesswerkstatt.personalos.sichern.plist"
  launchctl unload "$plist" 2>/dev/null || true
  rm -f "$plist"
  echo "Automatische Sicherung aus."
}

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) system=windows ;;
  Darwin) system=mac ;;
  *) echo "Nur macOS und Windows werden unterstützt. Unter Linux einen cron-Eintrag für tools/sichern.sh anlegen." >&2; exit 1 ;;
esac

case "${1:-}" in
  an)  "${system}_an" ;;
  aus) "${system}_aus" ;;
  *)   echo "Aufruf: $0 an | aus" >&2; exit 1 ;;
esac
