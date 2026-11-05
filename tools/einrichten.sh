#!/usr/bin/env bash
# Einmal je Rechner (und nach jedem Vorlagen-Update): macht die Skills für Claude Code sichtbar.
# .claude/ ist von Git ausgeschlossen.
# macOS und Linux: Verknüpfungen, Änderungen an .agents/skills/ wirken sofort.
# Windows (Git Bash): Kopien, weil Verknüpfungen dort Sonderrechte brauchen.
#   Nach Änderungen an .agents/skills/ dieses Skript erneut ausführen.
set -euo pipefail
cd "$(dirname "$0")/.."

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) modus=kopie ;;
  *) modus=link ;;
esac

mkdir -p .claude/skills
for s in .agents/skills/*/; do
  name=$(basename "$s")
  ziel=".claude/skills/$name"
  if [ "$modus" = kopie ]; then
    rm -rf "$ziel"
    cp -R ".agents/skills/$name" "$ziel"
    echo "kopiert: $name"
  elif [ ! -e "$ziel" ]; then
    ln -s "../../.agents/skills/$name" "$ziel"
    echo "verknüpft: $name"
  fi
done

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Hinweis: Dieser Ordner ist noch kein Git-Repository. Siehe README, Abschnitt Sicherung."
fi
echo "Fertig. Claude Code im Vault-Ordner neu starten."
