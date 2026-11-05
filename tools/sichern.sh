#!/usr/bin/env bash
# Sichert das Vault nach GitHub: erst den Stand holen, dann committen und pushen.
# Aufruf: tools/sichern.sh ["Commit-Nachricht"]
set -uo pipefail
cd "$(dirname "$0")/.."

nachricht=${1:-"Sicherung $(date '+%Y-%m-%d %H:%M')"}

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "FEHLER: kein Git-Repository. Siehe README, Abschnitt Sicherung." >&2
  exit 1
fi

git add -A
if ! git diff --cached --quiet; then
  git commit -q -m "$nachricht" && echo "committet: $nachricht"
else
  echo "keine Änderungen"
fi

if git remote get-url origin >/dev/null 2>&1; then
  if ! git pull --rebase -q; then
    git rebase --abort 2>/dev/null
    echo "KONFLIKT: Der Stand auf GitHub weicht ab. Nichts überschrieben, bitte von Hand klären." >&2
    exit 2
  fi
  git push -q && echo "nach GitHub gesichert"
else
  echo "Hinweis: kein GitHub-Ziel (origin) eingerichtet, nur lokal committet."
fi
