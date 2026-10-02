"""Android Tasker projects: every locale's tasker.json mirrors the English key set, keeps the
Tasker variables, and android/<lang>/ is exactly what generate_tasker.py makes from it."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "android"))
import generate_tasker  # noqa: E402

LANGS = ["en", "es", "pt", "ru", "uk"]
VAR = re.compile(r"%[A-Za-z_][A-Za-z0-9_]*")


def strings(lang):
    return json.loads((ROOT / "locales" / lang / "tasker.json").read_text(encoding="utf-8"))["strings"]


def test_all_five_languages_have_tasker_projects():
    base = sorted(p.name for p in (ROOT / "android" / "en").glob("*.prj.xml"))
    assert len(base) == 5
    for lang in LANGS:
        assert sorted(p.name for p in (ROOT / "android" / lang).glob("*.prj.xml")) == base, lang
        for name in base:
            ET.parse(ROOT / "android" / lang / name)


def test_same_keys_and_variables_as_english():
    base = strings("en")
    assert all(k == v for k, v in base.items())
    for lang in LANGS[1:]:
        tr = strings(lang)
        assert set(tr) == set(base), lang
        for en, value in tr.items():
            assert set(VAR.findall(en)) <= set(VAR.findall(value)), (lang, en[:40])


def test_selectors_compile():
    for lang in LANGS:
        for en, value in strings(lang).items():
            if en.startswith("(?i)"):
                re.compile(value)


def test_generated_projects_are_up_to_date():
    for lang in generate_tasker.tasker_langs():
        assert generate_tasker.generate(lang, check=True) == [], lang


def test_translated_projects_keep_english_structure():
    """Same element tree as English, only text differs."""
    for lang in LANGS[1:]:
        for name in generate_tasker.PROJECTS:
            a = list(ET.parse(ROOT / "android" / "en" / name).getroot().iter())
            b = list(ET.parse(ROOT / "android" / lang / name).getroot().iter())
            assert [(x.tag, x.attrib) for x in a] == [(y.tag, y.attrib) for y in b], (lang, name)
