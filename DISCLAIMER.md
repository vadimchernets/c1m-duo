# Disclaimer

## What Poly is for

Poly is a personal tool: it asks two AI assistants the same question, has them check each other,
and hands you one result to read and judge. It is meant for one person's own work — a decision,
a document, a draft, a second opinion.

## What Poly is not

**Not professional advice.** Poly is not a doctor, a lawyer, an accountant or a financial adviser,
and neither are the models behind it. When the recipes suggest using it for medical, legal or
financial questions, that means *preparing yourself for a conversation with a professional* — what
to ask, what to check, where two sources disagree — not replacing that conversation. Decisions with
real consequences belong to a qualified human being.

**Not fact-checking.** Two models agreeing is a weak signal, not evidence: they read much of the
same internet and can be confidently wrong together. Poly is built to *surface* disagreement, not
to certify truth. Anything that matters still needs a primary source.

**Not enterprise orchestration.** If you need server-side scale, guaranteed execution, retries,
audit logs, compliance or an SLA, use the providers' APIs or a platform built for that. Poly runs
one question at a time, in the foreground, on one phone, at human pace.

**Not browser automation, and not a grey area.** This is worth stating plainly, because anyone
arriving from the desktop versions will ask. Poly on iPhone drives nothing and opens no windows: it
calls the Shortcuts actions that the ChatGPT and Claude apps **publish for exactly this purpose**,
through Apple's own Shortcuts app, with your accounts, on your phone. That is a supported
integration point offered by the vendors, not an automated route into a consumer interface — so the
"automated access" question that applies to browser-driving tools does not arise here at all.

**Not a way around anyone's pricing or limits.** Poly uses the Shortcuts actions the ChatGPT and
Claude apps publish, with your own accounts, and every run spends messages from your own plan
exactly as asking by hand would. It is not built for bulk automation, for reselling access, or for
running someone else's questions through your subscription.

## Accuracy and responsibility

The models can be wrong, incomplete or out of date, and Poly cannot tell when they are. You remain
responsible for what you do with the output. The software is provided without warranty of any kind, and liability is limited,
on the terms set out in [LICENSE](LICENSE).

## Independence

Poly is an independent product, not affiliated with, endorsed by or sponsored by Apple,
OpenAI or Anthropic. It depends on their apps continuing to publish the actions it uses; if they
change, Poly may stop working until it is updated.
