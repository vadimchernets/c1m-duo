# Installing Poly — 2 minutes, no tech skills required

Poly is a "shortcut" for iPhone: ask one question, and it's handled by two AIs at once — ChatGPT and Claude — in one of eleven modes. The answer lands on your screen and in your clipboard.

## Before you install (one-time)

1. **An iPhone with iOS 18 or later.** That's the official minimum for the "Ask Claude" action Poly is built on (Anthropic's own docs say "iOS 18 and later"). Separately, under iOS 26, Apple lists iPhone 11 and later, SE 2nd generation and later, as supported devices. Poly itself does not require Apple Intelligence — only iOS 18+. iPad is expected to work on iPadOS 18+/26 but hasn't been tested in the wild. The **Poly Compress** companion needs Apple Intelligence hardware specifically: an A17 Pro / M-series chip or newer (iPhone 15 Pro/Pro Max, any 16/16e and later, iPad with M1+ or the A17 Pro mini).
2. **The ChatGPT and Claude apps**, installed from the App Store and signed in on both. Free accounts are enough: free Claude runs Sonnet 5.5, the same model as the paid plan, and the Ask Claude action uses the model chosen in the Claude app.

## Installing (one tap)

### Easiest — the iCloud link (one tap)

On your iPhone, tap the link → the Shortcuts app opens → **Add**. On the first run the shortcut asks for permission 4–6 times — tap **Always Allow** each time.

- **Duo:** https://www.icloud.com/shortcuts/80a91be31b2644af828076a50ad96f00
- **Trio** (the third voice, see below): https://www.icloud.com/shortcuts/4006167cb55b4cf2bf36868389318ed2

### Backup — the file

The signed `Duo.shortcut` and `Trio.shortcut` files are on [polyhelper.ai/duo/en/](https://polyhelper.ai/duo/en/) and in the [GitHub release](https://github.com/vadimchernets/c1m-duo/releases/tag/v1.0.0). Or:

1. Get the **`Poly.shortcut`** file any way you like: AirDrop, WhatsApp/Telegram, email, a USB drive — it doesn't matter.
2. Tap the file. The Shortcuts app opens with a "Poly" card — tap **Add**. Done, Poly is installed.
   - If the file arrived in a messaging app, tap it there first, choose Share/"Open in…", then pick Shortcuts.
3. **First run:** the shortcut asks for permissions — "Allow ChatGPT actions?" → Allow; "…send text to Claude?" → **Always Allow**; "…copy to clipboard?" → **Always Allow**. This only happens once.

## Home Screen icon (30 seconds, optional)

1. Open Shortcuts → long-press the Poly tile → if no menu appears, tap "···" on the tile → tap the name **Poly ⌄** at the top → **"Add to Home Screen."**
2. Want the branded icon? Tap the thumbnail → the "Image" tab → "Choose Photo/File" → pick `Poly.jpg` (send it to your phone along with the shortcut).
3. Tap **Add**. The Poly icon appears on your Home Screen — one tap to launch. By voice: "Hey Siri, Poly."

## How to use it

Tap the icon → "Question for Poly?" → type your question → "Done" → pick a mode. The menu has two levels: five common modes up top, everything else tucked into **📂 More…** (nothing is removed — a rare mode just costs one extra tap). More… also holds **ℹ️ What is Poly** — a free, on-device explainer for every mode. Lost at the mode picker? Open it — it doesn't spend a single message.

**Main menu (common modes):**

| Mode | What happens | Cost |
|---|---|---|
| **⚖️ Critique · 2✉** | ChatGPT answers, Claude checks it and delivers an improved final version. Your everyday driver. | 2 messages |
| **🩺 Advisor · 1✉** | Claude reviews YOUR finished text without rewriting it: a one-line verdict, the strongest objection first, what to double-check. The cheapest mode. | 1 message |
| **👀 Side by side · 2✉** | Both answer independently; the answers sit next to each other. | 2 messages |
| **🔀 Synthesis · 3✉** | Both answer blind, then get merged into an "anchor + delta" result. You'll be asked who anchors: Claude (facts/structure) or ChatGPT (tone/creativity). For anything that matters. | 3 messages |
| **🧭 Auto · +1✉** | Not sure which mode to use? ChatGPT picks one for you (+1 message), then Poly restarts with the same question so you can choose the recommended mode. | 1 message + the mode |

**📂 More… (occasional modes + free help):**

| Mode | What happens | Cost |
|---|---|---|
| **⚔️ Decision · 3✉** | A quick take (ChatGPT) meets a cautious one (Claude), then a referee lays out first steps and risks. For decisions. | 3 messages |
| **🗺 Dispute map · 3✉** | Both answer blind, then get mapped: where they agree, where they diverge, blind spots, what to verify. No forced conclusion — you decide. | 3 messages |
| **🥊 Debate · 4✉** | A draft, an opponent hunting for weaknesses, a revision, then a judge's verdict. For the hardest problems. | 4 messages |
| **❓ Clarify · 2✉** | ChatGPT asks what's missing first → you answer in a window that pops up → Claude gives a precise answer. For vague questions. The only mode where you're expected to touch the screen mid-run — but only in its own dialog, nothing else. | 2 messages |
| **➕ Delta · 2✉** | Claude writes the anchor answer → ChatGPT returns ONLY a bullet list of improvements, no full rewrite. A cheaper alternative to Synthesis when you're watching your message budget. | 2 messages |
| **🎨 Image · 2–3✉** | Describe what to draw → both AI artists sketch it blind (vector SVG, each in a clean session — no peeking at the other) → a page opens with two sketches side by side, ◆ CLAUDE and ◆ CHATGPT — pick one (you'll be asked: sketches only · 2✉ or + a comparison judge's verdict · 3✉ — the judge compares the sketch code; you can already see the renders yourself). The image is saved (Files → iCloud Drive → Shortcuts → `Poly-image.html`), and the SVG code lands in your clipboard: paste it into any converter or site to get an image file at any size. | 2–3 messages |
| **ℹ️ What is Poly** | An on-screen explainer of what Poly is and which mode to use when — no AI calls involved. From there, "🔁 Another mode" takes you back to mode selection with the same question. | 0 messages |

**A shortcut into the menu itself** (optional): keep the **Poly Quiet** companion nearby — it's a ready-made Critique run in one tap, no mode picker at all (the result goes straight to the clipboard and the journal, no screens), or **Poly Voice** — the same thing by voice, with the result read aloud. Either one's icon can go on your Home Screen just like Poly, giving you a "quick button" next to the full menu.

Pricing is shown right in the menu (the ✉ icon). Progress notifications arrive as the run goes — "[step 2/4]…". The journal logs both the mode and the raw intermediate answers, so if the final result gets cut off, the drafts aren't lost. The final answer opens full-screen with a Share button (Quick Look).

**Two tiers.** Tier 1 is the core: the Poly pair and the companions below, which run on their own once you tap them — start here, this is the heart of it. Tier 2 is **🎼 Poly Multi**: the same pair plus any other AIs you have, brought in semi-manually — Poly writes the prompt, leads you through the apps one at a time and merges everything into one document, while you paste, send and copy. About half the work of polling them by hand. It ships alongside the core; pick it up once the pair feels natural.

**Automatic Poly companions** (included): **Poly Voice** — tap, dictate, the Critique pipeline runs, the answer is read aloud (good for walking or cooking); **Poly Photo** — share a photo or PDF, on-device OCR reads the text (free, no network) and feeds it straight into Poly; **Poly Quiet** — the same pipeline as Critique but with no notifications and no final screen: the result goes only to the clipboard and the journal (for quick runs in the background); **Poly Compress** (Apple Intelligence devices only: iPhone 15 Pro and later, the full 16/16e/17 lineup) — select a wall of text → Share → Compress: Apple's free on-device model shrinks it and launches Poly automatically (protection against timeouts on long text).

Right after you pick a mode, a **status notification** arrives ("what's happening and how long to wait"). Then it's roughly 1–2 minutes until the answer shows up on screen and in your clipboard. Ready-made phrasings for 20+ common tasks live in `recipes.md`. The final answer always opens with the gist in one line, and ends with "Confidence: high/medium/low." **While the shortcut is running, leave your phone alone** — touching the screen cancels it (if it seems to silently die, just run it again). The exception is **❓ Clarify**: by design, it opens a second window and asks you to answer follow-up questions (or tap "skip") — that's not a glitch, it's part of the flow. Answer, and the shortcut continues on its own.

## Superpowers

- **From any app:** select text → Share → Poly — your question box already has the text in it; add "translate/check/explain" and run.
- **Journal:** every run appends itself to `Poly-journal.md` (Files → iCloud Drive → Shortcuts). Your whole history of questions and verdicts lives in one place; on the first run, allow file access with **Always Allow**.
- **Hands-free launch:** Settings → Action Button → "Run Shortcut" → Poly. Or a double-tap on the back of the phone: Settings → Accessibility → Touch → Back Tap → Poly. By voice: "Hey Siri, Poly."
- **More entry points:** a widget on your Home Screen or Lock Screen (long-press the Home Screen → + → Shortcuts → Poly); Control Center (Settings → Control Center → add "Shortcuts"); an NFC tag on your desk or in your car (Shortcuts → Automation → NFC → run Poly).
- **Photos into the duet:** the main path is the **Poly Photo** companion (share a photo/PDF → OCR → it launches Poly for you). For a *visual* read of an image (not the text on it), use Claude's camera widget → analysis → Copy → share the text into Poly.
- **Check your own writing:** select your draft anywhere → Share → Poly → **🩺 Advisor** mode — it reviews without rewriting (and never turns into a co-author).
- **On iPhone 15 Pro and later:** Shortcuts has an "Use Model" action (Apple Intelligence, free, no internet) that can extend Poly — for example, auto-picking a mode. On iPhone 14 and earlier the action isn't available; Poly works fine without it.
- **Start listening immediately (optional):** in the shortcut editor, expand the first "Ask" action and enable the "dictate immediately" toggle — then tapping the icon starts listening for your question right away. Off by default, since that's more convenient for both typed text and the share sheet.

## Trio — the third voice (free key)

`Trio.shortcut` adds a third AI to the pair: it reads the question, ChatGPT's answer and Claude's
final answer, and names only what both missed. It runs on **any free key — or several**, asked once.

**Free keys — a minute each, no card** (one is enough; more keys = Trio almost never goes quiet):
- **aistudio.google.com/apikey** → Create API key (Gemini, starts with `AIza`);
- **openrouter.ai/keys** → Create key (dozens of free models from different companies, starts with `sk-or-`);
- **console.groq.com/keys** → Create API Key (starts with `gsk_`).

Run Trio and paste the key(s) when it asks — several keys, each on a new line. They are saved in
iCloud Drive → Shortcuts → `poly-key.txt`, not inside the shortcut. On the first run iPhone asks for
permission 4–5 times — tap **Allow** each time, right away (an unanswered prompt closes and the
shortcut then says it can't access).

Trio tries every key with every free model until one answers: an overloaded model or a spent daily
limit moves on to the next model, a key with no money left or an invalid key is skipped. Only if all
of them fail does it list what each one answered (no money, limit, overloaded, invalid key) and what
to do. To add a key later, paste it on a new line in `poly-key.txt` (Files → iCloud Drive →
Shortcuts), or delete the file and run Trio again.

## About iCloud — no paid plan needed

Poly does not require paid iCloud. The core flow (question → both AIs → answer on screen and in the clipboard) never touches iCloud at all. Only two optional conveniences use it: the run journal and the image file — both measured in kilobytes, and the free 5 GB on any Apple ID covers decades of that. If iCloud Drive is off or full, the answer still lands on your screen and in your clipboard (this is guaranteed by design) — only the journal entry is skipped. Don't want a journal at all? See Privacy below.

## Privacy

`Poly-journal.md` stores every question and answer in plain text in iCloud Drive. Don't want the history? Delete the journal action in the shortcut editor. To erase what's already there, delete the `Poly-journal.md` file in Files. If the journal grows too large, just rename the file (e.g. to `Poly-journal-august.md`) — a fresh one is created automatically on the next run.

## If something's wrong

- **ChatGPT says "You are logged out"** (while you're clearly logged in) — open the ChatGPT app, close it, run Poly again. A known glitch that always clears up this way.
- **Claude says "This model isn't available right now"** — you've hit the free daily limit, or the model chosen in the Claude app isn't on your plan. Pick Sonnet in the Claude app or wait for the limit to reset; meanwhile Trio checks with a free AI on a key.
- **Claude goes silent / an empty answer on a long question** — the Claude action has a timeout: it can hand control back before Claude finishes, while Claude keeps writing the answer inside its own app. Open Claude, the answer is there — copy it with the app's own button. For next time: a shorter question returns more reliably. If it just failed outright, swipe Shortcuts away from Recents and run it again.
- **Sharing Poly with someone:** send `Poly.shortcut` as a standalone file, not zipped (a zip on a phone means extra steps). In Telegram: long-press the file → Share/Save to Files, not a single tap.
- **Don't rename the Poly shortcut.** The Photo and Compress companions, and the "🔁 Another mode" button, all call it by the exact name "Poly." Rename it (or re-import it and end up with "Poly 1") and those three paths silently stop working. If you get a duplicate on reinstall, delete the old shortcut and keep exactly one named "Poly."
- **Answers weaker than expected** — the action uses whatever model is set as default in the Claude app: open Claude, switch the model, close it, run Poly again. Good habit: check the model in Claude's header before an important run.
- **A share brought over a bare link and nothing happened** — the actions don't fetch web pages themselves: open the page, select some of the text, and share that text instead.
- **Bonus:** the final answer also goes into the shared clipboard (Universal Clipboard) — on a Mac or iPad you can paste it with Cmd+V without touching your phone.
- **After a major iOS update** (say, to iOS 27), run one test Critique. A big Shortcuts update can re-ask for permissions or show an extra "Done" card — one run will surface and clear that.
- Message cost comes out of your **subscriptions** for each service (not an API), sharing the same limits as your normal chats. The model used is whatever's set as default in each app.

## What comes after the final answer

Below the final screen, Poly asks: **"✅ Done"** or **"🔁 Another mode — same question."** The second option restarts Poly with your question already filled in (you can edit it) and lets you pick a different mode. Handy for running Critique, then immediately running Dispute map on the same question without retyping it.
