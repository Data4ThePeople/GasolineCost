#!/bin/zsh
# Unattended weekly update of the gas cost tool, run by launchd (Tuesday and
# Wednesday at 11:00). EIA posts the weekly pump price Monday afternoon, or
# Tuesday after a Monday holiday; Wednesday is the backup run.
#   1. EIA weekly regular gasoline and BLS CPI-U (fetch_prices.py --weekly).
#   2. If either changed: model.py, then build.py (which checks the page in
#      Chrome against model.py before writing dist/ and docs/).
#   3. Commit and push. GitHub Pages then serves the new price, on the
#      standalone tool and inside the Prismic embed.
# The post's own numbers and charts stay as published.
# Success posts a macOS notification with the new price. A failure posts one too, undoes any partial change, and leaves
# details in logs/weekly.log.
set -u
ROOT="${0:A:h:h}"
PY="$ROOT/.venv/bin/python"
LOG="$ROOT/logs/weekly.log"
mkdir -p "$ROOT/logs"
exec >>"$LOG" 2>&1
cd "$ROOT" || exit 1
echo "\n=== $(date '+%Y-%m-%d %H:%M %Z') ==="

TRACKED=(data/raw/eia_gasoline_regular_weekly.json data/raw/bls_cpi_u_nsa.json data/processed/model.json dist docs)

fail() {
  echo "FAILED: $1"
  git checkout -q -- $TRACKED 2>/dev/null
  osascript -e "display notification \"$1\" with title \"Gas cost weekly update failed\"" 2>/dev/null
  exit 1
}

git pull -q --rebase || fail "git pull"
"$PY" src/fetch_prices.py --weekly || fail "EIA or BLS fetch"

if git diff --quiet -- data/raw/eia_gasoline_regular_weekly.json data/raw/bls_cpi_u_nsa.json; then
  echo "no new data"; exit 0
fi

"$PY" src/model.py || fail "model.py"
"$PY" src/build.py || fail "build.py"

week=$("$PY" -c "import json;m=json.load(open('data/processed/model.json'));print(m['price_date'], '\$%.2f' % m['price'])")
git add $TRACKED
git commit -q -m "gas-cost tool: automatic weekly update, price for the week of $week" || fail "git commit"
git push -q || fail "git push"
echo "pushed: week of $week"
osascript -e "display notification \"Now showing ${week#* } for the week of ${week%% *}. Live on GitHub Pages in a minute or two.\" with title \"Gas cost tool updated\" sound name \"Glass\"" 2>/dev/null
