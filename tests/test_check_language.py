"""The language check: Cyrillic only in language places. Controls plant it and expect red."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check_language", ROOT / "tools" / "check_language.py")
check_language = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_language)

RU_WORD = "\u043f\u0440\u0438\u0432\u0435\u0442"  # a Russian word, written as escapes on purpose


def test_repository_is_clean():
    assert check_language.violations(ROOT, check_language.git_files(ROOT)) == []


def _plant(tmp_path, name, text):
    path = tmp_path / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return name


def test_control_comment_in_code_is_red(tmp_path):
    name = _plant(tmp_path, "scripts/tool.py", f"x = 1  # {RU_WORD}\n")
    assert check_language.violations(tmp_path, [name])
    _plant(tmp_path, "scripts/tool.py", "x = 1  # hello\n")
    assert check_language.violations(tmp_path, [name]) == []


def test_control_file_name_is_red(tmp_path):
    name = _plant(tmp_path, f"notes/{RU_WORD}.txt", "hello\n")
    assert check_language.violations(tmp_path, [name])
    clean = _plant(tmp_path, "notes/hello.txt", "hello\n")
    assert check_language.violations(tmp_path, [clean]) == []


def test_control_json_key_is_red(tmp_path):
    name = _plant(tmp_path, "data/table.json", json.dumps({RU_WORD: 1}, ensure_ascii=False))
    assert check_language.violations(tmp_path, [name])
    _plant(tmp_path, "data/table.json", json.dumps({"hello": 1}))
    assert check_language.violations(tmp_path, [name]) == []


def test_control_markdown_is_red(tmp_path):
    name = _plant(tmp_path, "README.md", f"# {RU_WORD}\n")
    assert check_language.violations(tmp_path, [name])
    _plant(tmp_path, "README.md", "# hello\n")
    assert check_language.violations(tmp_path, [name]) == []


def test_language_places_are_allowed(tmp_path):
    names = [
        _plant(tmp_path, "README.ru.md", f"{RU_WORD}\n"),
        _plant(tmp_path, "lang/ru.json", json.dumps({"w": RU_WORD}, ensure_ascii=False)),
        _plant(tmp_path, "lang/uk.json", json.dumps({"w": RU_WORD}, ensure_ascii=False)),
        _plant(tmp_path, "tests/fixtures/ru/case.txt", f"{RU_WORD}\n"),
        _plant(tmp_path, "tests/behavior/uk/case.txt", f"{RU_WORD}\n"),
    ]
    assert check_language.violations(tmp_path, names) == []


def test_other_language_files_may_not_hold_cyrillic(tmp_path):
    name = _plant(tmp_path, "lang/es.json", json.dumps({"w": RU_WORD}, ensure_ascii=False))
    assert check_language.violations(tmp_path, [name])


def test_self_names_in_a_language_list_are_allowed(tmp_path):
    line = "English · Español · Português · " + " · ".join(check_language.SELF_NAMES)
    name = _plant(tmp_path, "README.md", line + "\n")
    assert check_language.violations(tmp_path, [name]) == []


def test_control_legacy_encoding_is_red(tmp_path):
    path = tmp_path / "scripts" / "legacy.py"
    path.parent.mkdir(parents=True)
    path.write_bytes(("# " + RU_WORD + "\n").encode("cp1251"))
    assert check_language.violations(tmp_path, ["scripts/legacy.py"])
