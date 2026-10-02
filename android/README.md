# Poly on Android — experimental

**Status: built, never run on a real device.** Everything here is complete and structurally
verified, and no human has yet used it on an Android phone. If you have one, you are the person
this folder is waiting for — see [how to help](#how-to-help) at the bottom.

## Why this is different from the iPhone side

On iPhone, Poly runs on official Shortcuts actions: the ChatGPT and Claude apps publish "ask this"
hooks that another app may call. **Android has no equivalent** — neither app exposes anything a
third-party automation can invoke to ask a question and get the answer back.

So Poly on Android works through **Tasker** and the system clipboard. Tasker prepares the prompt,
opens the right app at the right moment and waits; the moment you copy an answer, it notices the
clipboard changed and moves on. You still tap inside each app — Tasker does the choreography
around it. Semi-manual by design, not by omission.

## What's here

| File | What it is |
|---|---|
| `en/poly-clipboard-relay.prj.xml` | **Start here.** The clipboard relay: paste, send, copy — Tasker leads you through both AIs and merges the result. Nothing to calibrate. |
| `en/poly-all-in-one.prj.xml` | All tasks in one import: the relay, the backup step-widgets and the automation attempts. |
| `en/poly-autoinput.prj.xml` | Automation via AutoInput with honest waiting — it watches for the Copy button rather than guessing with timers. Needs calibration. |
| `en/poly-autoclicker.prj.xml` | An older automation approach, kept for reference. |
| `en/poly-choirs.prj.xml` | The ten-AI choirs: West, East, and an East–West merge. |
| `generate_choirs.py` | Regenerates the choir file — `python3 generate_choirs.py <lang>` (strings in `locales/<lang>/choirs.json`). Edit the AI list inside if yours differ. |
| `generate_tasker.py` | Makes `<lang>/` from the English projects and `locales/<lang>/tasker.json` (English text → translation), then the choirs — `python3 generate_tasker.py --all`; `--check` fails if a folder is stale. |
| `es/` `pt/` `ru/` `uk/` | The same five projects in Spanish, Portuguese, Russian and Ukrainian — generated, never edited by hand. |

Guides: [English](../docs/en/android.md) · [Русский](../docs/ru/android.md)

## What you need

Tasker (a one-time purchase of about $4 on Google Play, with a 7-day trial from the developer's
site; included in Play Pass). AutoInput as a separate plugin only if you go past the relay. The
ChatGPT and Claude apps installed and signed in — free accounts are enough.

## Honest limitations

- **Nobody has run this on a phone.** The XML is valid and the structure is verified; behaviour is
  not. Expect to fix something.
- **Button labels must be calibrated to your interface language** for anything beyond the relay.
- **Tasker's Wait Until has no timeout** — if a step seems stuck, it means the clipboard never
  changed, i.e. you haven't copied the answer yet.
- **No profiles or triggers are included**: tasks are started by hand or from a widget you place.
- Android tightens what background apps may do with every release; automation that works today can
  break on an update. Nothing safety-critical should depend on it.

## Scale and scope

This is built for one person's own accounts, at human speed: you tap, you copy, the relay waits
for you. Anything that turns it into bulk automation — running many accounts, feeding someone
else's questions through your subscription, or driving the apps faster than a person would — is
outside what this is for and outside what the apps' own terms allow.

The automation levels here differ in kind, and it is worth knowing which you are using. The
clipboard relay only watches your clipboard; it never touches another app's interface. The
AutoInput levels drive the apps' UI through Android's accessibility service — that is a powerful
permission that can see whatever is on screen, so keep it off while you handle passwords or
banking, and turn it on only for the runs you want.

## How to help

The single most useful thing: **run the clipboard relay once and tell us what happened.** Import
`en/poly-clipboard-relay.prj.xml`, put `Duo Go` on your home screen, ask it `2+2`, and follow the
prompts. Then open an issue (write to info@polyhelper.ai) or a discussion (write to info@polyhelper.ai) with your
phone model, Android version, and where it went wrong — or that it simply worked.

That one report turns this folder from "experimental" into a real second half of the product.
