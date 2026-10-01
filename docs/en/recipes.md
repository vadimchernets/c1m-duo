# Poly recipes — what to ask, and which mode to use

Poly is a generalist: any task boils down to the right phrasing plus the right mode. Below is a tested library of recipes. The fastest path for existing text: **select the text → Share → Poly** — it drops straight into the question box, so you just add the instruction in front of it.

| Task | What to write in the question | Mode |
|---|---|---|
| Proofread an email before sending | "Check and improve this email, keep a warm professional tone: [text]" | ⚖️ Critique · 2✉ (already final and shouldn't be rewritten? Use 🩺 Advisor instead — see below) |
| Reply to a difficult or unpleasant message | "Here's an incoming message. Break down the tone and intent, and suggest 3 replies in different tones: [text]" | ⚖️ Critique · 2✉ |
| Write code and get it reviewed | "Write [what you need]. Requirements: …" | ⚖️ Critique · 2✉ (🥊 Debate · 4✉ only for critical code, when you specifically want someone hunting for holes) |
| Review existing code | "Find bugs, risks, and what to improve: [code]" | 👀 Side by side · 2✉ |
| Make a decision (buy / switch / launch?) | "Should I [idea/decision]? Context: …" | ⚔️ Decision · 3✉ |
| Assess risk in a project or deal | "What are the risks in [thing] and how do I close them off?" | ⚔️ Decision · 3✉ |
| Fact-check a text or news article | "Check these claims for factual errors: [text]" | 🔀 Synthesis · 3✉ |
| High-stakes question (medical / legal / financial) | Ask it as-is | 🔀 Synthesis · 3✉ (🥊 Debate is not a substitute — it's for when you specifically want the conclusion stress-tested) |
| Quickly understand a new topic | "Explain this for a non-specialist, no fluff: [topic]" | ⚖️ Critique · 2✉ |
| Learn something with self-testing | "Explain [topic] and give me 3 self-check questions with answers" | ⚖️ Critique · 2✉ |
| Prepare for a meeting or negotiation | "Meeting about [topic] with [who]. What questions should I ask, and what objections should I expect, with answers?" | ⚔️ Decision · 3✉ |
| Names, taglines, creative options | "Give me 10 variations of [thing] in different styles, then pick your top 3 with reasoning" | 👀 Side by side · 2✉ |
| Summarize an article | select the article → Share → "Summarize: the main points and the takeaway" | ⚖️ Critique · 2✉ |
| Plan your day / prioritize tasks | "Here are my tasks: […]. Prioritize them and suggest an order" | ⚔️ Decision · 3✉ |
| Translate and polish | "Translate into [language] and polish the style: [text]" | ⚖️ Critique · 2✉ |
| Brainstorm | "Suggest 5 non-obvious solutions to this problem: […], then rate which ones are realistic" | ⚖️ Critique · 2✉ (this is "generate and filter," not "stress-test" — Debate isn't needed) |
| Long explanation → short summary | "Explain […] in detail, then compress it into 3 one-sentence points at the end" | ⚖️ Critique · 2✉ |
| Awkward message → draft reply | select the conversation → Share → "Break down the tone and suggest a reply" | ⚔️ Decision · 3✉ |
| Check YOUR OWN text without a rewrite | select your draft → Share → (don't add anything) | 🩺 Advisor · 1✉ |
| Contested topic — what's actually true? | ask it as-is — you'll get a map of agreements and disagreements with no forced conclusion | 🗺 Dispute map · 3✉ |
| Vague question, not sure what you actually want | ask it as-is — you'll get follow-up questions first | ❓ Clarify · 2✉ |
| Logo, diagram, greeting card, illustration | "Draw [what, in what style]" — two vector sketches to choose from | 🎨 Image · 2–3✉ |
| Photo of a document, sign, or menu | Share the photo → Poly Photo (OCR handles the rest) | Poly Photo companion |
| Small screen / on the move | ask by voice — the answer is read aloud, and the text lands in your clipboard | Poly Voice companion |
| Not sure which mode to pick | ask it as-is — don't choose a mode yourself | 🧭 Auto · +1✉ (ChatGPT recommends one; Poly restarts with the same question) |
| Message budget is tight, but you still want two takes | ask it as-is | ➕ Delta · 2✉ (a cheaper alternative to 🔀 Synthesis: Claude's anchor + ChatGPT's list of improvements — 2 messages instead of 3) |

## Technique notes

- **Debate is a rare tool, not a default.** Save it for when you specifically need someone to try to break the conclusion: critical code, decisions where a mistake is expensive. Everyday writing goes through Critique or Advisor; high-stakes questions go through Synthesis.
- **The microphone key** on the keyboard in the question box gives you voice input with no setup.
- **Modifier words** at the end of a question work: "answer concisely," "in detail," "in bullet points only" — the models follow them.
- For a recipe you use often, you can build a **small dedicated shortcut**: a block of text with the task already written, followed by "Run Shortcut" pointing at Poly (the task becomes the pre-filled question).
- Every run's result is already in your **clipboard** — paste it straight into an email or chat — and it's also saved in the **journal**, `Poly-journal.md`.
