# FAQ

**Do I need an API key?**
No. Poly runs on the ChatGPT and Claude apps already installed and signed
in on your phone — there's no key to generate or paste anywhere.

**Does it spend my plan limits?**
Yes. Each run costs 1 to 4 messages against your ChatGPT and Claude
subscriptions, the same as chatting in those apps directly. The ✉ badge in
the menu shows the price before you pick a mode.

**Is it safe to install a shortcut from the internet?**
Official builds are published as signed files in this repository's
the folder you were given only. You can also open the shortcut in the
Shortcuts app and read every step before running it — nothing is hidden.

**Does it work with free ChatGPT / free Claude?**
ChatGPT — yes, subject to its own free-tier limits. Claude — no, a paid
Claude plan is required; on a free account the Claude action can fail with
"model isn't available."

**Where does the journal live and how do I delete it?**
`Poly-journal.md` is a plain-text file in your own iCloud Drive (Files →
iCloud Drive → Shortcuts). Delete the file to erase the history, or remove
the journal action from the shortcut to stop new entries.

**Do I need paid iCloud?**
No. The core flow — question in, answer on screen and in the clipboard —
never touches iCloud. The free 5 GB on any Apple ID covers the journal for
years.

**Android or iPad?**
Poly is iPhone-first. iPad is expected to work but hasn't been verified.
Android has an experimental path: Tasker plus the clipboard, because neither app publishes a callable action there. The files and the guide are in [android/](../../android/) — built and verified, but never run on a real device. If you have an Android phone, trying it and reporting back is the most useful contribution available right now.

**Are you affiliated with OpenAI or Anthropic?**
No. See [TRADEMARKS.md](../../TRADEMARKS.md).

**One of the apps returned nothing — what now?**
Two known cases: ChatGPT shows "you are logged out" while you're clearly
logged in — open the ChatGPT app, close it, and run Poly again. Claude goes
quiet on a long question because its action times out — the answer is still
being written inside the Claude app itself; open Claude to read it.

**How do I remove Poly completely?**
Delete the Poly shortcut (and any companions you installed) from the
Shortcuts app, and delete `Poly-journal.md` from Files if you kept a
journal.
