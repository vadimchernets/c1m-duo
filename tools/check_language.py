#!/usr/bin/env python3
"""Fail if Cyrillic appears anywhere outside a language place.

The project language is English. Russian and Ukrainian live only in their own places, on par with
every other language:

  * a path part named after the language: `ru/`, `uk/` (localizations, `tests/fixtures/ru/`,
    `tests/behavior/ru/`, `locales/ru/`, ...);
  * a file named for the language: `README.ru.md`, `lang/ru.json`, `lang/uk.json`;
  * the self-names of the two languages in a list where every language is named in its own way
    (`English · Español · Português · <Russian> · <Ukrainian>`, each in its own script).

Every file git knows about (tracked, or new and not ignored) is checked: each part of its path, and
its text. There are no in-file exemption markers - the list above is the whole list.

    python3 tools/check_language.py          # prints offenders, exits 1 if any
"""
import re
import subprocess
import sys
from pathlib import Path

CYRILLIC = re.compile("[\u0400-\u04ff]")
# Self-names of the two Cyrillic-script languages (Russian, Ukrainian).
SELF_NAMES = ("\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
              "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430")
LANGUAGE_CODES = ("ru", "uk")
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".shortcut",
                   ".plist", ".wav", ".mp3", ".mp4", ".woff", ".woff2", ".ttf", ".otf", ".pyc"}


def is_language_place(path):
    """True when `path` (a posix relative path) belongs to the Russian or Ukrainian place."""
    parts = path.split("/")
    if any(part in LANGUAGE_CODES for part in parts[:-1]):
        return True
    name = parts[-1]
    for code in LANGUAGE_CODES:
        if re.fullmatch(rf"[^/]*\.{code}\.[^/]+", name):
            return True
        if len(parts) >= 2 and parts[-2] == "lang" and name == f"{code}.json":
            return True
    return False


def offending_lines(text):
    """Line numbers that hold Cyrillic once the allowed self-names are removed."""
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        for name in SELF_NAMES:
            line = line.replace(name, "")
        if CYRILLIC.search(line):
            found.append(number)
    return found


def violations(root, paths):
    """List of "path: why" strings for `paths` (relative, posix) under `root`."""
    out = []
    root = Path(root)
    for path in sorted(set(paths)):
        if is_language_place(path):
            continue
        if CYRILLIC.search(path):
            out.append(f"{path}: Cyrillic in the file name")
        full = root / path
        if not full.is_file() or full.suffix.lower() in BINARY_SUFFIXES:
            continue
        try:
            data = full.read_bytes()
        except OSError as error:
            out.append(f"{path}: cannot be read ({error.strerror})")
            continue
        if b"\0" in data:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            # Not UTF-8: a legacy single-byte Cyrillic encoding would otherwise slip through.
            text = data.decode("cp1251", errors="replace")
        lines = offending_lines(text)
        if lines:
            shown = ", ".join(str(n) for n in lines[:10]) + (" ..." if len(lines) > 10 else "")
            out.append(f"{path}: Cyrillic on line(s) {shown}")
    return out


def git_files(root):
    result = subprocess.run(
        ["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=root, capture_output=True, check=True)
    return [p for p in result.stdout.decode("utf-8", errors="surrogateescape").split("\0") if p]


def main():
    root = Path(__file__).resolve().parent.parent
    found = violations(root, git_files(root))
    for line in found:
        print(line)
    print(f"check_language: {len(found)} file(s) with Cyrillic outside a language place")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
