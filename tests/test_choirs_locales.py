"""Every locales/*/choirs.json must carry the same keys as the base (en) locale,
and every .format() template in it must format without error."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES_DIR = ROOT / "locales"

# Keys whose value is a .format() template, with the kwargs a real call site
# passes (see android/generate_choirs.py). Keys not listed here are plain
# strings (or, for "task_names", a dict of plain strings) with no placeholders.
TEMPLATE_KWARGS = {
    "step_flash": {"n": 3, "total": 10, "name": "ChatGPT"},
    "final_flash": {"name": "ChatGPT", "total": 10},
    "done_flash": {"name": "ChatGPT"},
    "answer_from_label": {"i": 3, "name": "ChatGPT"},
    "journal_summary_label": {"name": "ChatGPT"},
}


def flatten_keys(node, prefix=""):
    """Yield dotted key paths for every leaf (and every dict key) in `node`."""
    if isinstance(node, dict):
        for key, value in node.items():
            path = f"{prefix}.{key}" if prefix else key
            yield path
            yield from flatten_keys(value, path)


def load(lang):
    return json.loads((LOCALES_DIR / lang / "choirs.json").read_text(encoding="utf-8"))


def test_choirs_locales_exist_for_en_and_ru():
    assert (LOCALES_DIR / "en" / "choirs.json").is_file()
    assert (LOCALES_DIR / "ru" / "choirs.json").is_file()


def test_every_choirs_locale_has_the_en_key_set():
    base_keys = set(flatten_keys(load("en")))
    checked = 0
    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        choirs_path = locale_dir / "choirs.json"
        if not choirs_path.is_file():
            continue
        checked += 1
        keys = set(flatten_keys(load(locale_dir.name)))
        missing = base_keys - keys
        extra = keys - base_keys
        assert not missing, f"{locale_dir.name}/choirs.json missing keys: {sorted(missing)}"
        assert not extra, f"{locale_dir.name}/choirs.json has unknown keys: {sorted(extra)}"
    # en, ru, es, pt, uk at minimum.
    assert checked >= 5


def test_every_choirs_locale_template_formats_without_error():
    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        choirs_path = locale_dir / "choirs.json"
        if not choirs_path.is_file():
            continue
        tr = load(locale_dir.name)
        for key, kwargs in TEMPLATE_KWARGS.items():
            template = tr[key]
            try:
                template.format(**kwargs)
            except (KeyError, IndexError, ValueError) as error:
                raise AssertionError(
                    f"{locale_dir.name}/choirs.json: {key!r} failed to format: {error}"
                ) from error


def test_task_names_has_four_entries_per_locale():
    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        choirs_path = locale_dir / "choirs.json"
        if not choirs_path.is_file():
            continue
        tr = load(locale_dir.name)
        assert set(tr["task_names"]) == {"all", "west", "east", "east_west"}
