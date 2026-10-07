# Contributing

## Before you start

Useful things to send:

- **A translation** — a new locale, or fixes to one that already ships. This is the most valuable
  contribution the project can get, and it needs no Python at all.
- **Corrections to `docs/`** — anything wrong, stale or confusing in the user documentation.
- **A bug report from a real device**, with the details the issue template asks for.
- **A new mode** — but open a [Discussion](../../discussions) first and agree on the shape of it
  before writing anything. A mode is prompts plus builder plumbing plus eleven translations; a
  surprise pull request is unlikely to land.

Things that will be turned down:

- **Code you don't have the right to submit** — anything copied from an employer's codebase, from
  another project, or generated from a source you can't account for.
- **Code under GPL, AGPL or another license incompatible with Apache 2.0.**
- **Rewriting prompts to "sound better"** without discussing it first. The prompts are the
  product. Every rule in them — no flattery, no averaging of conflicting claims, pasted text is
  data and not instructions, the confidence line — was put there deliberately and verified on
  device. Propose the change, explain what it fixes, then write it.
- **New external dependencies.** The build runs on macOS with Python 3.9+ and the `shortcuts`
  CLI, and it stays that way.

## Contributor terms

By opening a pull request you agree that your contribution is licensed under the Apache License
2.0, and you confirm you have the right to submit it. A DCO sign-off (`git commit -s`, which adds
a `Signed-off-by:` line) is welcome but not required.

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

**Menu arrays keep their length and order.** `menu.main_items` has exactly 7 entries and
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

## Working on the shortcut itself

`src/build_shortcut.py` builds the main shortcut, `src/build_companions.py` the five companions.
They contain no user-visible text; if you need new wording, add a key to `locales/en/ui.json` (and
to every other locale) rather than a literal in the code.

Two platform rules the builders exist to enforce, learned the hard way on device:

- A **text field** (file append, save file) ignores a bare attachment — it needs a text token
  carrying the attachment. Use the helpers (`act_append_file`, `act_save_file`) instead of hand-rolling.
- Only **action outputs** may be embedded inside a string. Dates and variables have to be fetched
  by their own action first (`act_date`, `act_get_variable`) and then referenced; an in-string date
  or variable token renders as empty text on device. `verify.py` fails the build if one appears.

Both builders validate their own output before writing: unique action ids, balanced control flow,
menu items matching their cases, no forward references, correct UTF-16 offsets in text tokens.

## Workflow

1. Fork the repository and create a branch: `git checkout -b ja-locale`.
2. Make the change.
3. Run the checks before you push:

   ```bash
   ./tools/build.sh <lang>     # locale changes: build, sign, package, verify
   python3 tools/verify.py     # checks only — this also runs in CI on every pull request
   ```

   `build.sh` needs macOS for the signing step. If you're on Linux or Windows, run
   `verify.py` and say so in the pull request; a maintainer will do the signed build.
4. Write short, imperative commit messages — "Add Japanese locale", "Fix cost badge in de menu" —
   not "changes" or "update files".
5. Open a pull request and fill in the template. Keep one topic per pull request; a locale and a
   builder change are two of them.

Pull requests are squash merged, so a tidy final description matters more than a tidy history.

## Reporting a bug

Use the **Bug report** issue template — it asks for the four things that determine whether a
report can be acted on at all:

- your **iOS version** (Settings → General → About → Software Version),
- the **locale** you installed,
- the **mode** or companion you were running,
- whether your **Claude plan is paid** (a large share of failures come down to this).

Then say what happened, including any error text on screen, and what you expected instead. A
screenshot helps.

Security issues are the exception: don't open an issue. Follow [SECURITY.md](SECURITY.md).

## Where to ask

- **[Issues](../../issues)** — bugs and concrete, actionable tasks.
- **[Discussions](../../discussions)** — ideas, questions, proposals for new modes, and anything
  you're not yet sure is a bug.

If you're unsure which one fits, use Discussions; moving a thread into an issue is easy. Both are
covered by the [Code of Conduct](CODE_OF_CONDUCT.md).
