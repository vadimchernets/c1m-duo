# What is Poly?

C1M is the project; **Poly** is what you actually get on your phone. This page explains it in plain language.

## What it actually is

Poly is a button on your iPhone with two AIs behind it. You ask one question, and ChatGPT and Claude handle it as a pair: one answers, the other checks and improves it — or both answer independently and their answers get merged, depending on the mode you pick. The result lands on your screen, in your clipboard, and in a journal.

The point is compression. The old sequence — open ChatGPT, ask, copy, open Claude, paste, ask it to check, copy the final version — collapses into one tap and about a minute and a half of waiting. And it's not just faster, it's better: a second AI genuinely catches the first one's mistakes. That's the whole reason a pair beats a single model.

It isn't an App Store app. It's a **shortcut** for Apple's built-in Shortcuts app — which is why it installs with one tap on a file and sits on your Home Screen like an ordinary icon.

## What it costs

- **Poly itself is free.** It's a file, not a service — no subscription to Poly, no ads, no data collection.
- **The cost comes out of your ChatGPT and Claude subscriptions.** Each run spends 1 to 4 messages (the price is shown right in the menu with a ✉ icon). It shares the same limits as your regular chats in those apps.
- **A Claude subscription is required** — on a free account the action can respond with "model isn't available." ChatGPT works either way, subject to its own limits.
- **No paid iCloud needed:** the journal is a few kilobytes; the free 5 GB covers decades of it. Turn iCloud off and the answer still arrives — only the journal entry is skipped.

## What you need before installing

An iPhone on iOS 18 or later, with the ChatGPT and Claude apps installed and signed in. That's it. Installation is one tap on the `Poly.shortcut` file — the step-by-step guide for non-technical users is in `install.md`.

## Where Poly earns its keep

- **Writing:** proofread before you hit send, decode an unpleasant incoming message, translate and polish.
- **Decisions:** "should I buy this," "should I switch," "should I launch this" — a quick take against a cautious one, then a plan and the risks.
- **High-stakes questions** (medical, legal, financial): two independent opinions and an honest map of where they disagree, instead of one confident voice.
- **Your own writing, unchanged:** Advisor mode reviews without turning into a co-author.
- **On the go:** the Voice companion — dictate the question, hear the answer read back.
- **Images:** two vector sketches from two different AI artists to choose from.

Ready-made phrasings for 20+ tasks are in `recipes.md`.

## The honest downsides

- **While Poly is running, leave your phone alone** (about 1–2 minutes) — touching the screen cancels the run. That's a limit of Apple's platform, not of Poly. The exception is Clarify mode, which opens a window on its own and asks you to answer.
- **It's not background magic.** The phone has to be unlocked, apps come to the foreground one at a time, in strict order. Poly is a button you press and wait on, not a robot on a schedule.
- **The ChatGPT action can glitch:** it sometimes claims "you are logged out" while you're clearly logged in. Always fixable: open the ChatGPT app, close it, run Poly again.
- **Long questions are risky:** the Claude action has a timeout — on a very long question the final result can come back empty, and you have to retrieve the full answer from inside the Claude app itself. Shorter questions return more reliably.
- **The model isn't selectable from inside Poly:** it uses whatever's set as default in each app. Check the model in Claude before a run that matters.
- **A major iOS update may call for one test run** — a big update can re-ask for permissions.

## Lost at the mode picker?

In the Poly menu, open **📂 More…** → **ℹ️ What is Poly** — a short explainer for every mode, right there on your phone, for free. Afterward Poly offers to take you back to the mode picker with the same question.

## And the other AIs — half the work is already off your hands

Everything above is about the pair, because that pair is what runs by itself. But you probably have
more AIs than two on your phone: Gemini, Grok, DeepSeek, Qwen, Copilot, whichever you like. Poly
can bring them in as well — semi-manually, and it is worth knowing exactly what that means.

Until now, asking five AIs the same question meant doing all of it by hand: writing the question
five times, keeping five answers straight, and then merging them yourself. **Poly Multi takes
roughly half of that off you.** It writes the prompt, puts it in your clipboard, walks you through
the apps one at a time, collects every answer as you copy it, and hands the whole pile to Claude to
merge into one document with the disagreements kept. What stays with you is the part only you can
do: open your app, paste, send, copy the answer, come back.

So it is not "Poly drives your other apps" — nothing here automates software you didn't write.
It is your own three taps per AI, with the thinking, the ordering and the merge done for you.
If you have been doing this by hand, it is about twice as fast, and the result is a document
instead of five tabs.

This is where the project is heading: more of the chorus, less of the manual part, as the apps
open up. For now the pair is automatic and the rest is semi-manual — and we would rather say that
plainly than promise otherwise. Poly Multi ships alongside the main shortcut; pick it up once the
pair feels natural.

## In one sentence

A free button that puts two of your paid subscriptions to work together, checking each other: one price — 1 to 4 messages per run — and one habit — tap, then leave your phone alone for a minute and a half.
