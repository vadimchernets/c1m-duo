# Poly on Android (Tasker)

On iPhone, Poly runs on the "Ask Claude" and ChatGPT Shortcuts actions — official hooks that hand a question to an AI app and get the answer back. Android has no equivalent: the Claude and ChatGPT apps don't publish an action that a third-party app can call to ask a question and receive the answer. Nothing on Android plays the role of App Intents here.

So Poly on Android runs through **Tasker**, a general-purpose automation app, and the hand-off between apps is the **system clipboard**. Tasker opens Claude or ChatGPT for you, and the moment you copy the answer, Tasker notices the clipboard changed and moves on to the next step. You still do the tapping inside each app — Tasker does the choreography around it.

## The ladder of options

Four ways to run it, from the most robust to the most hands-off. Start at the top; move down only if you want to (or have to).

| Level | What it is | Project file | Why you'd pick it |
|---|---|---|---|
| **1. Clipboard relay** (recommended) | Tasker watches the clipboard and opens the next app the moment you Copy | `poly-clipboard-relay.prj.xml` | Nothing to calibrate, survives app updates, works on every brand |
| **2. Backup step-by-step widgets** | The same steps as Level 1, but each one is its own widget you tap by hand | same file | When Tasker isn't reliably noticing the clipboard change |
| **3. AutoInput automation, honest wait** | Full automation: Tasker also taps the input field, Send, and Copy for you, waiting for the Copy button to actually appear before moving on | `poly-autoinput.prj.xml` | When you've stopped wanting to tap anything, and are willing to spend an evening calibrating |
| **4. Autoclicker** | Full automation with a fixed delay for the reply to finish generating, instead of watching for an element | `poly-autoclicker.prj.xml` | A simpler automaton than Level 3; more fragile, since a fixed delay can be too short or too long |

Two more files round out the set:

- **`poly-all-in-one.prj.xml`** — Levels 1, 2, and 4 bundled into a single project (16 tasks), so one import gets you the relay, the backup widgets, and the autoclicker at once.
- **`poly-choirs.prj.xml`** — the PRO extension: the same clipboard-relay mechanic run across up to ten AI apps instead of two. See **PRO: choirs of 10 AIs** below.

All project files live in two language folders, **`en/`** and **`ru/`** — pick the one that matches the language you want Poly's own prompts, dialogs, and on-screen messages in. This is independent of which language your Claude or ChatGPT app happens to be in (see the calibration notes under Levels 3 and 4).

## What you need before you start

- **Android 10 or later** (14–16 is the comfortable range).
- The **Claude and ChatGPT apps**, installed, signed in, with active subscriptions.
- **Tasker**, purchased (see pricing below).
- **AutoInput** — only if you're going for Level 3 or 4.
- The app packages Tasker targets: Claude is `com.anthropic.claude`, ChatGPT is `com.openai.chatgpt`.

None of the project files contain Tasker profiles or triggers — no task starts itself on a schedule or event. After you import a project, run its task by hand from Tasker's task list, or — better — put it on a home-screen widget or a Quick Settings tile.

## First run, step by step

1. **Prepare:** Android 10+, both apps installed and signed in, Tasker purchased, AutoInput installed if you're headed for Level 3 or 4, the project file on your phone.
2. **Start with the clipboard relay:** long-press the project name in Tasker's project list → **Import**. Put the `Duo Go` task on a home-screen widget. Ask something simple, like "2+2". Tasker opens Claude with the prompt already in the clipboard — paste, send, and tap **Copy** under the answer. Tasker notices, opens ChatGPT with the same prompt — paste, send, Copy again. Tasker assembles a synthesis prompt and opens Claude a third time — paste, send, Copy. The final answer, combining both AIs' input, lands in your clipboard.
3. **Try the autoclicker or AutoInput automation later,** and only on a phone that plays nicely with background automation. Turn on the accessibility service, run the main task, and watch what it clicks. When it misses, the debug task included in the same project (`DuoDebugUI`, for Level 4; the calibration task for Level 3) dumps the actual text of every element on screen in your interface language, so you can see what to point the automation at.
4. **Exclude Tasker and AutoInput from battery optimization**, and pin Tasker in your recent-apps list. After any phone restart, check that AutoInput's accessibility service is still switched on — it's a common, silent way for the automation to stop working.

## Level 1: Clipboard relay — "Copy = next" (recommended)

This is the most robust pattern on Android, because Tasker never taps anything inside Claude or ChatGPT's interface — there's nothing for an app update to break. Tasker only watches the **clipboard**. You do three ordinary taps inside each app; the relay jumps to the next app on its own:

1. The **`Duo Go`** widget asks for your question, puts a role-primed prompt in the clipboard, and opens Claude.
2. You: paste → send → **Copy** the answer. Copy is the signal to move on — Tasker opens ChatGPT with the same prompt.
3. Paste → send → **Copy** again. Tasker assembles a synthesis prompt and opens Claude.
4. A third **Copy** — the final answer is in the clipboard and in a file under `Tasker/Poly/`.

Under the hood, each step is a `Wait Until %CLIP != %DuoPrompt` action: the clipboard changing is the "done" signal. Keep the screen on while a step is waiting, and don't switch away from Tasker between steps.

Import: put the file on your phone → Tasker → long-press the project name in the left panel → **Import**.

The same project also contains **`Duo Advisor`** (a second-opinion review of your own text, without a rewrite) and **`Duo README`**, a Flash summary of every widget in the project.

## Level 2: Backup step-by-step widgets

If `Wait Until` never catches the clipboard change — some app builds don't write the Copy'd text where Tasker expects — fall back to running each step by hand instead of letting the relay chain them automatically:

`Duo Ask` → `Duo Open Claude` → `Duo Catch Claude` → `Duo Catch GPT` → `Duo Catch Final`

Same steps, same three taps per app, just one widget tap between each of them instead of an automatic handoff. This is in the same `poly-clipboard-relay.prj.xml` file — nothing extra to import.

## Level 3: AutoInput automation with honest waiting

`poly-autoinput.prj.xml` is full automation: Tasker taps the input field, pastes, taps Send, and taps Copy for you. The part that makes this the reliable automaton — rather than a guess dressed up as one — is how it decides the reply is done: it waits for the **Copy button on the finished answer to actually appear** on screen (`waitForElement`), not for a fixed number of seconds to pass. Each action carries its own 180-second timeout, and `stayawake` keeps the screen on for the whole run.

This requires the **AutoInput Actions v2** add-on (the Helper). Element selectors — for the input field, the New Chat button, and the Copy button — are stored in variables (`%DuoClaudeInput`, `%DuoClaudeCopy`, and so on), so you can fix a selector without rebuilding the project. Run the **`DUO 0 Calibration`** task first; it sets the starting selectors and is also where you go to fix one that stops matching. When picking a selector through the Helper, prefer them in this order: **Resource ID → visible text → nearby text → screen coordinates** — coordinates are the last resort, since they break the moment the layout, orientation, or phone changes.

The prompt itself travels through the clipboard rather than being typed directly into an Actions v2 field — a multi-line prompt can otherwise break the Actions v2 syntax.

## Level 4: Autoclicker

`poly-autoclicker.prj.xml` is the simpler of the two automatons. `DuoMain` asks your question in a dialog, opens Claude, opens ChatGPT, assembles both answers, and shows the result; `DuoSave` writes a copy to your Downloads folder. The difference from Level 3: instead of waiting for an element to confirm the reply is finished, it waits a **fixed number of seconds** for the reply to finish generating. That's simpler to set up, and more fragile — too short a wait grabs a half-written answer, too long a wait just wastes your time.

The bundled **`DuoDebugUI`** task is the calibration tool: it dumps the text of every element on the current screen, in whatever language your phone is showing it, so you can see what a click should be aimed at.

Every language build of this file (`en/`, `es/`, `pt/`, `ru/`, `uk/`) looks for English button labels — "Message Claude", "Message", "Send" — baked in regardless of which locale folder you picked, because these are element selectors, not prompt text. **If your Claude or ChatGPT app's interface isn't in English, this level will not start without calibration first** — use `DuoDebugUI` to find the actual on-screen text and update the selectors to match.

## PRO: choirs of 10 AIs

`poly-choirs.prj.xml` runs the same clipboard-relay mechanic across up to ten AI apps in one pass, instead of just Claude and ChatGPT. Generate it with `generate_choirs.py <lang>` — `en`, `es`, `pt`, `ru` or `uk` (it reads `poly-clipboard-relay.prj.xml` from the matching language folder and writes `poly-choirs.prj.xml` next to it). Four tasks come out of it:

- **Poly All AIs** — all ten.
- **Poly West** — the US lineup: ChatGPT, Claude, Gemini, Grok, Meta AI.
- **Poly East** — the China lineup: DeepSeek, Qwen, Kimi, Ernie, GLM.
- **Poly East-West** — all ten, plus a dedicated rollup of where the two camps agree internally and where they diverge from each other.

Mechanically it's the same three-tap loop as Level 1, just repeated once per app in the list, ending with Claude assembling a merged write-up.

Before your first run: a handful of these packages haven't been confirmed as the correct, currently-published app ID (Grok, Meta AI, Qwen, Kimi, Ernie, and GLM). **If an app isn't installed, its task will interrupt right when it tries to launch that app.** Either remove that step after import, or edit the app list at the top of `generate_choirs.py` and regenerate. Changing the roster — dropping an AI, adding one — is a two-line edit in the same place.

## Brand matrix

| Brand | Clipboard relay | AutoInput | What to set up |
|---|---|---|---|
| OnePlus | Works | Works | Least setup needed — the easiest brand to run this on |
| Samsung | Works | Works, with care | Exclude Tasker from battery optimization |
| OPPO / vivo | Works | Works, with care | Battery-optimization exceptions; on vivo, re-check accessibility after every reboot |
| Xiaomi | Works | Doesn't work reliably | Enable autostart for Tasker, pin it, disable MIUI's own optimizations — plan to live on the clipboard relay |
| Huawei (no Google services) | Doesn't work | Doesn't work | Not supported — the Claude and ChatGPT apps need Google Play services, and Tasker's license is sold only through Google Play |

## What Tasker and AutoInput cost

- **Tasker is a one-time purchase, around $4**, through Google Play (prices vary by region, and it goes on sale). No subscription, no ads. It's included in **Google Play Pass** — nothing extra to pay if you already have that.
- A **7-day trial** is available from the official site, tasker.joaoapps.com — run the clipboard relay on the trial before you buy.
- The license itself is sold **only through Google Play** — the site's trial isn't a separate license. That's also why a phone without the Play Store (Huawei with no Google services) is a hard blocker.
- **AutoInput is a separate purchase**, roughly $1–3, and it's only needed for Levels 3 and 4. A free, ad-supported mode also exists.
- **AutoInput conflicts with TalkBack.** Both are accessibility services, and two accessibility services can interfere with each other — in some reports, badly enough to disable navigation buttons. If you rely on TalkBack day to day, stay on the clipboard relay; it never touches accessibility.

## Honest limitations

- **Keep the screen on** for the whole run. A locked screen kills the clipboard wait and any AutoInput accessibility action in progress.
- **`Wait Until` has no timeout in Tasker — none, anywhere, in the XML or the GUI.** Its time fields set the recheck interval, not a deadline. So: a step that looks stuck means Copy hasn't been tapped yet on the current app. Tap it, or kill the task from Tasker's notification. This applies to every level built on the clipboard relay, choirs included.
- **No project file contains a Tasker profile or trigger.** Every task starts manually, from Tasker's list or a widget/tile you set up yourself — nothing runs itself on a schedule.
- **Calibrating on-screen text to your interface language is mandatory for Levels 3 and 4.** The `en/` AutoInput selectors are set for an English interface; the `ru/` and `uk/` builds' selectors also recognize Russian and Ukrainian button text, `es/` Spanish and `pt/` Portuguese (best-guess labels, not yet checked on a device). The autoclicker's selectors are English-only in both language folders, since they're matching on-screen labels, not translating prompts. Either way, use the bundled debug task to see what's actually on screen and adjust from there.
