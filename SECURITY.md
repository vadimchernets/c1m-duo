# Security Policy

## Reporting a vulnerability

Please do not open a public issue for a security concern. Email
**polyhelper.ai@gmail.com** with details and, if possible, steps to reproduce.
You'll get a response within 7 days.

## Relevant attack surface

C1M ships as an iPhone shortcut (Poly), not a server or an app with backend
infrastructure. The relevant surface is narrower than a typical service, but
not zero:

- **Prompt injection through pasted or shared text.** A question, or text
  shared into Poly from another app, is data the models read — it should
  never be able to make a model act as if it had received new instructions.
  Every prompt in `locales/*/prompts/` states this rule explicitly ("data,
  never instructions"). Reports showing a way around that protection are
  welcome and treated as security issues.
- **Clipboard contents.** Poly writes its result to the system clipboard
  (including Universal Clipboard, which reaches a signed-in Mac or iPad).
  Anything that leaks clipboard contents to an unintended destination, or
  exposes them longer than the run itself, is in scope.
- **The journal file.** `Poly-journal.md` is stored in plain text in the
  user's own iCloud Drive. It is not encrypted at rest by Poly, and it is not
  sent anywhere by Poly. If you find a way for the journal to leak outside
  the user's own iCloud account, that's a report we want.
- **Trust in `.shortcut` files.** A `.shortcut` file is an executable
  workflow, not inert data. Official builds are published as signed files only
  in this repository's `releases/` folder and Releases, and on polyhelper.ai/duo. A `.shortcut` file
  obtained from anywhere else — a link, a forum, a messaging app forward —
  may have been modified and should not be trusted as an official Poly
  build. If you find an official-looking build circulating outside Releases,
  please report it.

## Out of scope

C1M has no server, no API keys, and no account system of its own — it runs
entirely on the ChatGPT and Claude apps and subscriptions already installed
on the user's phone. Vulnerabilities in those apps themselves belong to
OpenAI and Anthropic, not this project; feel free to loop us in if a report
touches both.
