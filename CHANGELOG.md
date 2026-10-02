# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added (2026-10-02, version check)
- **Duo and Trio look for a newer version at most once in 7 days.** At the very end of a run they
  read `releases/version.json` (GitHub raw, then `polyhelper.ai/duo/version.json`); if its number
  is higher than the one built in, one line asks «A new version of Duo is out — install it?» and
  «Install» opens that language's iCloud link from the same file. The day of the last check is the
  modification date of `Duo-version-check.txt` / `Trio-version-check.txt` next to `poly-key.txt`
  (iCloud Drive → Shortcuts). Strings `update.*` in every `locales/<lang>/ui.json`; code in
  `src/build_shortcut.py` (`version_check`), used by `src/build_trio.py`; test
  `tests/test_version_check.py`. This build is **duo 2, trio 2**. Signed en/es/pt/ru/uk Duo and
  Trio rebuilt — their iCloud links must be re-created.

### Fixed (2026-10-02)
- «🔁 Another mode — same question» in Duo called the shortcut «Poly», but the release installs
  as «Duo» (file name and iCloud record): it now calls «Duo».

### Changed (2026-10-02)
- Spanish speaks «usted» everywhere, like Poly A1 (pt «você», uk and ru formal «you»):
  `locales/es/ui.json` and `trio.json` (menus, notifications, help, key
  prompts), `docs/es/*`. Signed **es Duo and Trio rebuilt** — their iCloud links
  must be re-created. Russian docs (`docs/ru/*`) and the Russian Tasker flashes
  and choir steps moved from the informal to the formal «you» as well; Russian/Ukrainian/Portuguese
  shortcut strings were already formal and are unchanged.

### Added (2026-10-02)
- Android Tasker projects in all five languages (en, es, pt, ru, uk): new
  `android/generate_tasker.py` builds `android/<lang>/` from the English
  projects and `locales/<lang>/tasker.json`; ru is now generated the same way
  (its old hand-made files are reproduced byte for byte). `generate_choirs.py`
  takes any language with `locales/<lang>/choirs.json`. `tools/verify.py` checks
  that every language has the five projects and that they are up to date;
  `tests/test_tasker_locales.py`.

### Changed
- Project language is English: the Russian duplicates in README.md and
  .zenodo.json were removed (English copies already present) and the BUILD.md
  note on iCloud links translated. Russian stays only in its localization places
  (locales/ru, docs/ru, android/ru), on par with the other languages. No shortcut
  was rebuilt or re-signed; iCloud links are unchanged.

### Added
- **Trio** (`Trio.shortcut`, en/es/pt/ru/uk): ChatGPT answers, Claude checks
  (the Critique pair, prompt `critique.txt`), then a third AI from a third
  company — Gemini Flash (`gemini-3.8-flash`) on a free Google AI Studio key —
  names only the errors and gaps both missed (new prompt `trio.txt`; ru has its
  own). Its words come as a separate block under Claude's answer, into the
  clipboard and on screen. Built by `src/build_trio.py`, words in
  `locales/<lang>/trio.json`; `tools/build.sh` and `tools/verify.py` build and
  check it.
- Keys never live in the shortcut: asked once (Gemini, then an optional Groq
  key), saved in iCloud Drive → Shortcuts → `poly-key.txt`, picked out by
  their shape (`gsk_…` is Groq). With both keys, Qwen on Groq
  (`qwen/qwen3.8-27b`) stands in when Gemini's free quota is spent or it is
  still overloaded after one automatic retry.
- Plain-words errors: daily/minute limit, wrong key, overloaded provider,
  renamed model, anything else with the provider's own reply.
- Ukrainian locale `locales/uk/ui.json` — the main shortcut and companions
  now build in uk too.
- Install docs (en, es, pt, ru): how to get the free key in three steps.
- `tools/check_language.py` — a gate that fails if Cyrillic appears anywhere
  outside a language place (a `ru/`/`uk/` path part, a `*.ru.*`/`*.uk.*` file,
  or a language's own self-name in a list where every language is named in
  its own script). Covered by `tests/test_check_language.py`; wired into
  `tools/verify.py`, which CI already runs on every push.
- `android/generate_choirs.py` now loads its per-language strings from
  `locales/<lang>/choirs.json` instead of an inline Python dict (en and ru
  carry the exact same text as before — the generated `android/en` and
  `android/ru` `poly-choirs.prj.xml` are byte-identical to what shipped
  previously). `locales/es/choirs.json`, `locales/pt/choirs.json` and
  `locales/uk/choirs.json` were added alongside, translated to match the
  wording already used in each locale's `ui.json`/`trio.json`; the Android
  generator itself still only builds en/ru (there is no `android/es`,
  `android/pt` or `android/uk` donor project yet to clone from), but the
  tables are ready for when one exists. Covered by
  `tests/test_choirs_locales.py` — every `locales/*/choirs.json` carries the
  same key set as the English base and every `.format()` template in it
  formats without error.

### Checked
- On a Mac (not on a phone), 01.10.2026: the third-voice block — the same
  actions `build_trio.py` ships — ran in macOS Shortcuts against both
  providers: Gemini 3.8 Flash and Qwen on Groq answered through
  `choices[0].message.content`; Gemini found a planted error both models
  missed; a fake key gave the «key did not work» message; a Gemini 503 gave
  the «overloaded» message. The ChatGPT/Claude steps, the key-file steps and
  the Groq stand-in were not run on a device.


## [1.1.0] — 2026-09-18

### Added
- Built-in help «What is Poly» (all ten languages) now says, in one
  paragraph, that PolyHelper on a laptop or PC does more — folders, agents,
  channels, schedules, a council of several AIs — and that Poly on the phone
  is the light version without the PC features. Prompts and the shortcut's
  logic are unchanged. Not yet run on a physical phone.
- A one-time notice (all ten languages): on the very first run, before the
  question, Poly shows once that PolyHelper on a laptop or PC does more and
  that Poly on the phone is the light version. A marker file next to the
  journal (iCloud Drive → Shortcuts → `Poly-pc-notice.txt`) keeps it from
  coming back. Prompts and the modes are unchanged. Not yet run on a physical
  phone.
- `android/` — the Tasker path, marked experimental: five projects in two
  languages, the choir generator and guides. Built and verified, never run
  on a physical device.
- `DISCLAIMER.md` — what Poly is for and what it is not.
- Language switcher in the README; every doc exists in all ten languages.

### Changed
- README leads with the economics of orchestration rather than the mechanics.
- `Verified` now states its exact coverage: one phone, two of ten languages.


## [1.0.0] — 2026-09-01

- 11 modes in a two-level menu: five everyday modes up top, the rest one tap
  away under More….
- 5 companions: Voice, Photo, Quiet, Compress, Multi.
- 10 languages via `locales/`, each a folder — no fork of the code.
- Signed, verified builds per locale, packaged as a ready-to-share kit.
- Plain-text journal, delivery to the clipboard (including Universal
  Clipboard), and an in-run "What is Poly" help screen that costs nothing.
