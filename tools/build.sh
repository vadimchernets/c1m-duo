#!/bin/bash
# Build, sign and package C1 for every locale (or the ones named on the command line).
#
#   ./tools/build.sh            # all locales in locales/
#   ./tools/build.sh en ru      # only these
#
# Signing uses the macOS `shortcuts` CLI in "anyone" mode, so the resulting files
# install on any device and any Apple ID.
set -u
cd "$(dirname "$0")/.."

LANGS=${@:-$(ls locales)}

for lang in $LANGS; do
  echo "== $lang =="
  python3 src/build_shortcut.py "$lang"   || exit 1
  python3 src/build_companions.py "$lang" || exit 1
  python3 src/build_trio.py "$lang"       || exit 1   # skipped where locales/<lang>/trio.json is absent

  # sign every shortcut in place
  for file in "dist/$lang"/*.shortcut; do
    [ -f "$file" ] || continue
    case "$file" in *.signed.shortcut) continue;; esac
    tmp="$(mktemp -d)/$(basename "$file")"
    # signing contacts Apple; retry a few times so a transient network error
    # does not abandon a half-signed release
    signed=0
    for attempt in 1 2 3 4 5; do
      if shortcuts sign -i "$file" -o "$tmp" --mode anyone 2>/dev/null; then signed=1; break; fi
      sleep 3
    done
    [ "$signed" = 1 ] || { echo "cannot sign $file (network?)"; exit 1; }
    mv "$tmp" "$file"
  done

  # kit archive: the shortcut, the icon and the docs a newcomer needs
  python3 - "$lang" <<'PYZIP'
import json, sys, zipfile
from pathlib import Path

lang = sys.argv[1]
root = Path.cwd()
ui = json.loads((root / 'locales' / lang / 'ui.json').read_text(encoding='utf-8'))
names = ui['shortcut_names']
dist = root / 'dist' / lang
docs = root / 'docs' / lang

entries = [(dist / f"{names['main']}.shortcut", f"{names['main']}.shortcut"),
           (root / 'assets' / 'poly.jpg', 'poly.jpg')]
for doc in ('install.md', 'what-is-c1.md'):
    if (docs / doc).exists():
        entries.append((docs / doc, doc))
for key in ('voice', 'photo', 'quiet', 'compress'):
    path = dist / f'{names[key]}.shortcut'
    if path.exists():
        entries.append((path, path.name))

archive = dist / 'poly-kit.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for source, arcname in entries:
        z.write(source, arcname)          # zipfile flags non-ASCII names as UTF-8
print(f'{lang}: {archive.relative_to(root)} — {len(entries)} entries')
PYZIP
done

echo "== verify =="
python3 tools/verify.py
