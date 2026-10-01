# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
