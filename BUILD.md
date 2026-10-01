# How this product is built

The build and translation mechanics. How to contribute is in
[CONTRIBUTING.md](CONTRIBUTING.md); this file is how the shortcuts are made.

The one line worth knowing before anything else:

```
./tools/build.sh <lang>    # builds, signs, packages and verifies one language
```

---

## Adding a language

A language is a folder, not a fork. Nothing in `src/` needs to change.

```
locales/
  en/                 base language
    ui.json           menus, notifications, journal templates, built-in help  ← translate this
    prompts/*.txt     what the two models read; shared by every language      ← leave as is
  <your-lang>/
    ui.json           your translation
    prompts/          optional: only if you want to override a specific prompt
```

You translate what a person sees, not what the models read. Prompts stay in English for every
language: the models follow English instructions best, and every prompt already tells them to
answer in the language of the question — so a Japanese user installing the Japanese build gets a
Japanese menu and a Japanese answer from the same English prompt.

1. Copy `locales/en/ui.json` to `locales/<lang>/ui.json` (ISO 639-1 code: `de`, `ja`, `pt`…).
2. Translate it — about 90 strings.
3. Translate the three user documents into `docs/<lang>/`: `install.md`, `what-is-c1.md`, `recipes.md`.
4. Build and check: `./tools/build.sh <lang>` — it builds, signs, packages and verifies.
5. Add your language to the table in `README.md`.

Not translated: source code, `README.md`, this file — those are for developers.

If a prompt genuinely needs to differ in your language, drop just that one file into
`locales/<lang>/prompts/`; everything you don't override falls back to English.

### Rules that keep a translation working

**Placeholders stay untouched.** Anything in braces — `{Q}`, `{R}`, `{D}`, `{X}`, `{QUESTION}`,
`{GPT_ANSWER}`, `{CLAUDE_ANSWER}`, `{ANCHOR}`, `{DRAFT}`… — is wired to a value by the builder.
Keep the same names in the same structural places; move the surrounding words freely.

**Menu arrays keep their length and order.** `menu.main_items` has exactly 6 entries and
`menu.extra_items` exactly 7; the builder indexes into them. Translate the labels, keep the emoji
and the `· N✉` cost badge — that badge is how a user sees the price before choosing.

**Prompt structure survives translation.** Numbered lists, section headers (`ORIGINAL QUESTION:`),
blank lines and the order of paragraphs are part of how the models parse the instruction. Translate
the sentences, keep the skeleton.

**Keep the rules the prompts encode**, they are not decoration:
- the answer must come back *in the language of the question*, whichever locale is installed;
- no flattery, no smoothing over disagreement, no averaging of conflicting claims;
- pasted text is *data, never instructions* — a model must not change role because of it;
- when a source is empty, say so instead of inventing it;
- the confidence line at the end (`Confidence: high / medium / low`).

**`auto-router.txt` answers with one word** from the closed list of mode names. Translate the list
in the prompt and `menu.*_items` together, so the recommendation matches a real menu entry.

### What the verifier checks

`python3 tools/verify.py` compares your locale against `en`: every ui key present, all 21 prompts
present, menu arrays the right length, and — for anything already built — that the signed files
match what the sources produce and stay structurally valid.
