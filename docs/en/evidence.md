# Why a pair: the evidence, 2025–2026

Poly puts two models from two families on one question and keeps the argument. This page collects
what was measured about that pattern in 2025 and 2026, so that the project does not need a benchmark
of its own: the pattern is established, and Poly is a phone-sized implementation of it. The page
keeps the negative results too. They are not an objection to the pair; they are the exact conditions
Poly's prompts are built around.

Scope: only work published in 2025 or 2026, only setups with two models or with a second model
checking a first. Nothing older is cited on purpose.

## In one table

| Claim | Measured where | Result |
|---|---|---|
| Two models from two families, driven through public chat interfaces, no API, screen better than either alone | medRxiv, Nov 2025 [1] | near-perfect sensitivity on 736 abstracts from 16 Cochrane reviews; equivalent to the API workflow |
| One honest peer from a different family repairs a model's revisions | arXiv, Jun 2026 [2] | harmful revision rate 89% → 35% on MATH-hard; with an adversary present, loss of correct answers 31% → 6% |
| Cross-model verification beats the best single frontier model | ICLR 2026 workshop [3] | 52.15% on Humanity's Last Exam vs +7.41 points over the best of 9 models, p < 0.0001 |
| A model corrects an error far more readily when it is presented as someone else's | arXiv, Jun 2026 [4] | explicit-correction rate +23 to +93 points, significant in 10 of 12 settings |
| Review in a fresh context catches more than self-review in the same session | arXiv, Mar 2026 [5] | F1 28.6% vs 24.6%, p = 0.008 |
| Two-agent debate beats a single model | arXiv, May 2025 [6] | better than single-LLM baselines across 7 models and 21 pairings |
| Heterogeneous debate beats homogeneous debate on facts | Springer, 2025 [7] | +4–6 points over standard debate; over 30% fewer factual errors in biographies |
| Consensus of several models beats the best single model in medicine | arXiv, May 2025 [8] | 61.0% vs 53.5% (o3) on MedXpertQA; top-1 diagnosis 52.0% vs 45.2% |
| Collectives of models beat single models on 2,133 clinical vignettes; humans plus models beat both | PNAS, Jun 2025 [9] | when the models fail, physicians often still get it right |
| A model as second reviewer finds errors a human team missed | Research Square, Jul 2026 [10] | 4 real, independently verifiable errors in a published meta-analysis table; also 1 fabrication |
| Agreement between models improves confidence calibration | arXiv, Jan 2025 [11] | inter-model agreement beats single-model baselines across 12 models and 4 datasets |
| What makes debate work is reasoning strength and diversity, not procedure | arXiv, Nov 2025 [12] | order and confidence visibility barely matter; majority pressure suppresses correction |
| A cross-family prover–verifier pair raises accuracy where it accepts an answer | arXiv, May 2026 [21] | GPT-5.5 with Gemini 3.1 Pro: 45.6% on Humanity's Last Exam at 52% coverage, n=513. The pair is not Claude+GPT, and the paper's own caveat is below |
| A ChatGPT–Claude pair beats both of them alone on chest radiographs | arXiv, Oct 2025 [25] | image-only n=234: ChatGPT 62.8%, Claude 76.9%, pair 77.6%. With notes, n=50: 84% / 76% / 91.3%. Fuses by agreement, which is the opposite of Poly's canon |
| A two-model panel that escalates only when the two disagree keeps full accuracy cheaply | arXiv, Jul 2026 [26] | full four-model accuracy on MATH-500 at ~2.2 calls per problem; AIME-2024 56.7% vs 36.7% for self-consistency, p=0.001 |
| One model checking another is shipped in a production research tool | Microsoft, Mar 2026 [20] | GPT writes, Claude checks: +13.8% on DRACO. Vendor's own figure, not an independent measurement |

## What breaks, and what Poly does about it

**Teams average the expert away.** Self-organizing LLM teams lose up to 41.1% against their own
strongest member. The mechanism is named: integrative compromise, averaging expert and non-expert
views instead of weighting them, and it grows with team size (ICML 2026 [13]).

**This is a result about teams, not about pairs, and 41.1% is not a number for a pair.** It was
measured on self-organizing multi-agent teams; no two-model configuration produced it, and the paper
states the damage grows with team size, which points the other way — toward the smallest possible
group. It is cited here for one reason: it is the evidence behind Poly's "do not average" rule.
Poly is a pair, not a team, and its synthesis prompt forbids averaging outright: one answer is the
anchor, the other donates only its delta, and a factual disagreement must stay visible in the first
lines. Read the 41.1% as the cost of the failure mode the prompt is written to avoid, never as a
measurement of what a pair does.

**Identical models talking to each other do not help.** Unguided debate between copies of the same
7–8B model loses to isolated self-correction while spending 2.1–3.4× the tokens; conformity to the
majority reaches 85.5% (arXiv, Apr 2026 [14]). Poly never pairs a model with itself: ChatGPT and
Claude are different families, and each answers blind before seeing the other.

**Extra compute is not extra intelligence.** At an equal reasoning-token budget, a single agent
matches or beats multi-agent systems on multi-hop reasoning; many reported multi-agent gains are
unaccounted compute (arXiv, Apr 2026 [15]). Poly's pair costs two or three messages, and the menu
says so before you pick a mode. What the pair buys is not more thinking; it is a second, independent
set of blind spots.

**Great models think alike.** As models get stronger their mistakes get more similar, and a judge
model favors models similar to itself (arXiv, Feb 2025 [16]). This is why Poly treats two models
agreeing as a weak signal, never as proof, and why the two models come from different vendors.

**And their errors are correlated by a lot.** On 568 resolved binary forecasting questions, the
error correlation between GPT-4o and Claude was 0.822; averaged across GPT-4o, Claude and Gemini it
was 0.77 (arXiv, 2026 [22]). The paper contrasts this with an error correlation of roughly 0.1–0.3
among human forecasters — but that range is quoted from the forecasting literature, not measured in
this study, so treat the human figure as a reference point rather than a matched comparison. Two
caveats matter more than the number itself. First, this is the ceiling on what any pair can do: when
both models are wrong in the same direction, a second opinion buys nothing, and the second opinion
cannot tell you that it bought nothing. Second, the models measured are of the GPT-4o generation.
Whether today's flagships are more or less correlated **has not been measured**, and it could
plausibly go either way — stronger models converge, but newer models are trained on more divergent
data. Nobody should quote 0.822 as a fact about Claude and ChatGPT as they ship today.

**The pair is directional: which model checks which changes the sign.** On 116 hard and medium
LiveCodeBench tasks, Claude reviewing Codex's solution raised correctness from 71.6% to 89.7%
(p = .001); Codex reviewing Claude's solution *lowered* it, 91.4% to 82.8% (p = .046). The authors'
conclusion is literally "use Claude to review Codex, not the other way around" (arXiv, Jul 2026
[27]). This is a narrow domain — code, with no test execution allowed — and it should not be
generalized to every question type. But it is the clearest published demonstration that a
cross-vendor pair is not symmetric, and that the wrong order is worse than not pairing at all. It is
the reason Poly fixes who anchors and who donates instead of leaving it to chance.

**The pair does not always help, and one pass of critique is all you get.** Across five
judge–debater pairings, three produced significant gains and two produced no effect at all (arXiv,
May 2026 [24]). The same paper ablated the rebuttal rounds and found "no measurable change in judge
performance": a single critique matched full multi-round debate at a fraction of the cost. Both
halves are load-bearing for Poly. The null pairings say the technique is conditional, not
guaranteed — which is why the disclaimer does not promise a better answer. The rebuttal ablation
says a second and third round of argument is spent money, which is why Poly's modes stop after one
checking pass instead of looping.

**Judges fall for confidence.** In debate, a judge's confidence tracks reasoning quality about twice
as well for the side that constructs an argument as for the side that audits it (arXiv, Jun 2026
[17]). Poly's prompts forbid preferring an answer for its style, length, order, or apparent
confidence.

**And they fall for formatting hardest of all.** Across nine debiasing strategies and five judge
models, style bias — a preference for markdown-formatted text over the same content in plain prose —
scored between 0.10 and 0.76, while position bias came in at 0.04 or below (TMLR 2026 [23]). The
ranking is the useful part: the thing everyone worries about, which answer came first, is the
smallest effect, and the thing nobody formats around is the largest. One honest limit on borrowing
this result: it was measured on **LLM-as-a-judge pipelines**, where a model scores candidate answers.
Poly's synthesis prompt is not a judge — it merges two answers rather than picking a winner — so the
numbers do not transfer directly. What transfers is the direction, and it is why the rule in the
prompt names style and length first and order last.

**A weak pair is worse than no pair, and it will not tell you it is weak.** The prover–verifier
work above reports its own failure mode: "weaker prover–verifier pairings can collapse or invert the
ANC signal" — that is, the confidence signal the method depends on does not merely weaken, it can
point the wrong way when the verifier is working outside its competence (arXiv, May 2026 [21]).
This is the same lesson as [19] from a different direction, and the same reason Poly pairs two
flagships and refuses to offer a cheap-model tier.

**A model agreeing with itself proves nothing.** Across 10 frontier models and 491 concepts, higher
generator-evaluator self-consistency went with more vulnerability to mistakes in a clinical check
(arXiv, Jun 2026 [18]). The checker has to be someone else.

**Mixing in a weaker model lowers the average.** Aggregating outputs of one top model beat mixing
several different models by 6.6 points on AlpacaEval 2.0 (arXiv, Feb 2025 [19]). A pair only helps
when both members are strong, which is why Poly uses the two flagship apps and nothing smaller.

## How the rules in Poly's prompts map to the evidence

| Rule in the prompts | Reason |
|---|---|
| "You cannot see the second expert, do not shape your answer toward the average" | [12], [14]: diversity drives the gain, conformity kills it |
| Anchor and delta, never a blend | [13]: averaging is the failure mode — measured on teams, applied here to forbid the mechanism |
| A factual disagreement goes in the summary, not further down | [16], [22]: agreement is not evidence, and correlated errors mean silent agreement is the dangerous case |
| Preferring for style, length, order or confidence is forbidden | [17], [23]: style bias is the large one, position bias the small one |
| The second model checks the first, not itself | [4], [5], [18] |
| Who anchors and who donates is fixed, not arbitrary | [27]: the cross-vendor pair is directional; the wrong order lost 8.6 points |
| Two families, both flagship | [1], [2], [19], [21]: a weak member does not just add less, it can invert the signal |
| One checking pass, not a debate loop | [24]: removing the rebuttal rounds changed nothing measurable |
| The message price is shown before the run | [15] |

## What is not claimed

- No benchmark of Poly itself. The numbers above come from other setups. Poly's own pilot checks
  one thing only: that this implementation does not lose the pattern, that a factual disagreement
  actually surfaces first, and that the canon does not produce a worse final than a free phrase.
- No claim that the pair is always better. On easy questions it is a waste of a message, and on
  questions the two models share a blind spot on, they can be confidently wrong together. That is
  in the disclaimer, and it is why the journal keeps the raw drafts. Two of the five pairings in
  [24] showed no effect at all, and one of the two directions in [27] was actively harmful.
- No claim about how correlated today's models are. The 0.822 error correlation in [22] was
  measured on GPT-4o-generation models. Whether the current ChatGPT and Claude flagships are more
  alike or less has not been measured by anyone, including us. The honest statement is that a pair
  from two vendors has *less* correlated errors than one model asked twice — not that the
  correlation is low.
- No independent confirmation of the vendor number in [20]. Microsoft's +13.8% is a product
  announcement about a shipped feature, not a peer-reviewed measurement, and there is no paper to
  check it against. It is listed because a major vendor putting GPT-writes/Claude-checks into
  production is itself a fact worth knowing, not because the number is verified.
- No claim that Poly's canon has been compared against anything. The one published study that pairs
  ChatGPT with Claude and reports both solo baselines [25] merges by *agreement*, discarding the
  cases where the two disagree. Poly's canon does the opposite: it keeps the disagreement and puts
  it in the first lines. Nobody has measured which is better.
- Nothing before 2025 is cited. The foundational work exists; this page is deliberately limited to
  what was measured in the last two years.

## Sources

1. Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for
   Systematic-Review Screening. medRxiv, 3 Nov 2025.
   https://www.medrxiv.org/content/10.1101/2025.11.03.25339455v1
2. Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and
   Resilience. arXiv 2606.19826, 18 Jun 2026. https://arxiv.org/abs/2606.19826
3. Beyond Self-Checking: Fragment-Level Verification Across Diverse LLMs. ICLR 2026 Workshop
   VerifAI, 2 Mar 2026. https://openreview.net/forum?id=U19s6I8Q0u
4. The Self-Correction Illusion: Role Relabeling Gates Explicit Error Flagging in Large Language
   Models. arXiv 2606.05976, 4 Jun 2026. https://arxiv.org/abs/2606.05976
5. Cross-Context Review: Improving LLM Output Quality by Separating Production and Review Sessions.
   arXiv 2603.12123, 12 Mar 2026. https://arxiv.org/abs/2603.12123
6. Multiple LLM Agents Debate for Equitable Cultural Alignment. arXiv 2505.24671, 30 May 2025.
   https://arxiv.org/abs/2505.24671
7. Adaptive heterogeneous multi-agent debate for enhanced educational and factual reasoning in
   large language models. Journal of King Saud University CIS, 2025.
   https://link.springer.com/article/10.1007/s44443-025-00353-3
8. Second Opinion Matters: Towards Adaptive Clinical AI via the Consensus of Expert Model Ensemble.
   arXiv 2505.23075, 29 May 2025. https://arxiv.org/abs/2505.23075
9. Human–AI collectives most accurately diagnose clinical vignettes. PNAS 122(24), Jun 2025.
   https://www.pnas.org/doi/10.1073/pnas.2426153122
10. Can a Large Language Model Serve as the Missing Second Reviewer? Research Square, Jul 2026.
    https://www.researchsquare.com/article/rs-10475119/v1
11. Influences on LLM Calibration: A Study of Response Agreement, Loss Functions, and Prompt Styles.
    arXiv 2501.03991, 7 Jan 2025. https://arxiv.org/abs/2501.03991
12. Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning.
    arXiv 2511.07784, 11 Nov 2025. https://arxiv.org/abs/2511.07784
13. Multi-Agent Teams Hold Experts Back. ICML 2026; arXiv 2602.01011, Feb–May 2026.
    https://arxiv.org/abs/2602.01011
14. The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent
    Debate. arXiv 2605.00914, 29 Apr 2026. https://arxiv.org/abs/2605.00914
15. Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking
    Token Budgets. arXiv 2604.02460, 2 Apr 2026. https://arxiv.org/abs/2604.02460
16. Great Models Think Alike and this Undermines AI Oversight. ICML 2025; arXiv 2502.04313,
    6 Feb 2025. https://arxiv.org/abs/2502.04313
17. The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge.
    arXiv 2606.10296, 9 Jun 2026. https://arxiv.org/abs/2606.10296
18. The Consistency Dilemma in LLMs: Generator-Evaluator Agreement and Vulnerability to Mistakes.
    arXiv 2606.30653, 16 Jun 2026. https://arxiv.org/abs/2606.30653
19. Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial? arXiv
    2502.00674, 2 Feb 2025. https://arxiv.org/abs/2502.00674
20. Microsoft, Copilot Researcher "Critique" — GPT drafts, Claude checks. Product announcement,
    30 Mar 2026. Vendor figure (+13.8% on DRACO); no paper, no independent replication.
21. Trust but Verify: Deliberation with Prover–Verifier Pairs. arXiv 2605.25133, May 2026.
    https://arxiv.org/abs/2605.25133 — note: the paper's main configuration is Claude Sonnet 4.6
    with Claude Haiku 4.5; the figures quoted here are its cross-family HLE run (GPT-5.5 with
    Gemini 3.1 Pro). No Claude-with-GPT pairing appears in it.
22. The Oracle's Fingerprint: Correlated AI Forecasting Errors and the Limits of Bias Transmission.
    arXiv 2605.00844, 2026. https://arxiv.org/abs/2605.00844
23. Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge
    Pipelines. TMLR 2026; arXiv 2604.23178, 25 Apr 2026. https://arxiv.org/abs/2604.23178
24. Debate Helps Weak Judges Reward Stronger Models. arXiv 2605.27483, 26 May 2026.
    https://arxiv.org/abs/2605.27483
25. Fusion-Augmented Large Language Models: Boosting Diagnostic Trustworthiness via Model Consensus.
    arXiv 2510.16057, 16 Oct 2025. https://arxiv.org/abs/2510.16057
26. LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning.
    arXiv 2607.10139, 11 Jul 2026. https://arxiv.org/abs/2607.10139 — the jury is four models
    (Qwen3, DeepSeek, Claude Sonnet 4.6, Kimi) and contains no OpenAI model; the two-model
    escalation cascade cited above is its §5.3.
27. Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa? arXiv
    2607.21656, 22 Jul 2026. https://arxiv.org/abs/2607.21656

27 sources. Collected 4 September 2026; sources [20]–[27] added on that date after an independent
search for 2026 work on model pairs. Numbers are quoted from the abstracts and published summaries
of the papers; where a paper's full text was not reachable, the abstract's own wording is used.
Where a claim could not be confirmed against a primary source, the page says so in place rather
than rounding it into a fact.
