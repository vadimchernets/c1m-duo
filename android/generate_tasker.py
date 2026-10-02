#!/usr/bin/env python3
"""Generator for the per-language Tasker projects (Android).

English (android/en/*.prj.xml) is the template. Every user-visible string in it
is listed, English → translation, in locales/<lang>/tasker.json; this script
swaps each text node of the English template for its translation and writes
android/<lang>/. The XML structure (tasks, actions, ids, variables) stays
byte-identical to English — only text nodes change. The choir project is then
rebuilt from the generated relay by generate_choirs.py.

Usage:
    python3 generate_tasker.py es           # writes es/ (four projects + choirs)
    python3 generate_tasker.py --all        # every locale that has tasker.json
    python3 generate_tasker.py --check      # exit 1 if any generated file is stale

locales/en/tasker.json is the key list (each English string maps to itself);
a translation must carry exactly the same keys.
"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

SCRIPT_DIR = Path(__file__).resolve().parent
LOCALES_DIR = SCRIPT_DIR.parent / "locales"
PROJECTS = [
    "poly-clipboard-relay.prj.xml",
    "poly-all-in-one.prj.xml",
    "poly-autoinput.prj.xml",
    "poly-autoclicker.prj.xml",
]


def load(lang):
    return json.loads((LOCALES_DIR / lang / "tasker.json").read_text(encoding="utf-8"))["strings"]


def tasker_langs():
    return sorted(p.parent.name for p in LOCALES_DIR.glob("*/tasker.json") if p.parent.name != "en")


def render(lang):
    """Return {filename: xml_text} for the four hand-shaped projects of `lang`."""
    base, tr = load("en"), load(lang)
    missing, extra = set(base) - set(tr), set(tr) - set(base)
    if missing or extra:
        raise SystemExit(f"{lang}/tasker.json: missing {sorted(missing)[:3]} extra {sorted(extra)[:3]}")
    out = {}
    for name in PROJECTS:
        xml = (SCRIPT_DIR / "en" / name).read_text(encoding="utf-8")
        # Longest first, and only whole text nodes (">text<"), so a short string
        # never rewrites part of a longer one.
        for en in sorted(base, key=len, reverse=True):
            xml = xml.replace(">" + escape(en) + "<", ">" + escape(tr[en]) + "<")
        out[name] = xml
    return out


def generate(lang, check=False):
    import generate_choirs
    stale = []
    for name, xml in render(lang).items():
        path = SCRIPT_DIR / lang / name
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != xml:
                stale.append(f"{lang}/{name}")
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(xml, encoding="utf-8")
    if not check:
        generate_choirs.build(lang)
    return stale


def main(argv):
    sys.path.insert(0, str(SCRIPT_DIR))
    if not argv:
        raise SystemExit(__doc__)
    if argv[0] == "--check":
        stale = [s for lang in tasker_langs() for s in generate(lang, check=True)]
        if stale:
            raise SystemExit("stale (rerun generate_tasker.py --all): " + ", ".join(stale))
        print("Tasker projects up to date:", ", ".join(tasker_langs()))
        return
    for lang in tasker_langs() if argv[0] == "--all" else argv:
        generate(lang)
        print("wrote", lang)


if __name__ == "__main__":
    main(sys.argv[1:])
