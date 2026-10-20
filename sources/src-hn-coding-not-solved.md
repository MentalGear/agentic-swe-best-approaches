---
id: src-hn-coding-not-solved
type: source
title: "HN thread: Coding Is Not Solved"
summary: 359-comment Hacker News discussion (item 49877988) on whether "coding is solved", heavy on review capacity, accountability and what tests can and cannot prove.
tags: [primary-source]
sources: [49877988]
links:
  - surfaces: con-coding-vs-engineering
  - surfaces: con-accountability
  - surfaces: con-review-capacity
  - surfaces: ap-green-tests-drift
  - surfaces: wf-port-with-oracle
  - surfaces: wf-executable-quality-rules
  - disputes: con-cross-model-review
  - surfaces: ap-unsupervised-autonomy
---
# HN thread: Coding Is Not Solved

- **URL:** <https://news.ycombinator.com/item?id=49877988>
- **Article:** [Article: Coding is NOT solved](src-article-coding-not-solved.md)
- **Captured:** 359 comments on 2026-09-28 (first capture; see `sources/manifest.json`), via the HN
  Algolia items API. Points and submitter were not recorded by the capture script.

## Shape of the discussion

A different debate from the plan-mode thread: little about planning, a lot about what happens after
code is generated. Camps, roughly:

| Camp | Position | Representative comments |
|---|---|---|
| **Solved in practice with the newest models** | "If you've used Opus 5.5, it's clear that coding is solved in the practical sense"; the article is outdated. | Rover222 [49879425](https://news.ycombinator.com/item?id=49879425), extr [49879510](https://news.ycombinator.com/item?id=49879510), keel-control [49879757](https://news.ycombinator.com/item?id=49879757), temp00345 [49879660](https://news.ycombinator.com/item?id=49879660), throwawayffffas [49881029](https://news.ycombinator.com/item?id=49881029) |
| **Typing is solved; engineering isn't** | The article's conclusion is right, its reasons are weak; the useful distinction is code versus decisions. | federicobrancas [49878318](https://news.ycombinator.com/item?id=49878318), jasongi [49879300](https://news.ycombinator.com/item?id=49879300), lordnacho [49878717](https://news.ycombinator.com/item?id=49878717), bluegatty [49879718](https://news.ycombinator.com/item?id=49879718) |
| **Not solved even as coding** | Design of types and APIs, architecture, long-run maintainability and non-JS domains still fail. | vmg12 [49878528](https://news.ycombinator.com/item?id=49878528), an0malous [49881067](https://news.ycombinator.com/item?id=49881067), OliveronData [49880345](https://news.ycombinator.com/item?id=49880345), jayd16 [49880481](https://news.ycombinator.com/item?id=49880481) |
| **The verification problem** | Tests, fuzzers and AI review may be enough (or may not); what humans must still read is the fight. | efficax [49878532](https://news.ycombinator.com/item?id=49878532) vs layer8 [49879394](https://news.ycombinator.com/item?id=49879394), whatever1 [49878472](https://news.ycombinator.com/item?id=49878472), nemo44x [49879469](https://news.ycombinator.com/item?id=49879469) |

## What this thread added to the graph

- **New concepts:** [con-coding-vs-engineering](../concepts/con-coding-vs-engineering.md),
  [con-accountability](../concepts/con-accountability.md),
  [con-review-capacity](../concepts/con-review-capacity.md).
- **New workflows:** [wf-port-with-oracle](../workflows/wf-port-with-oracle.md),
  [wf-executable-quality-rules](../workflows/wf-executable-quality-rules.md).
- **New pitfall:** [ap-green-tests-drift](../anti-patterns/ap-green-tests-drift.md).
- **Extended:** unsupervised autonomy (a dispute over six months of no-review coding), cross-model
  review (a dispute over AI reviewing AI), endless review, test harnesses, underspecification,
  the understanding problem, blast radius, trusting explanations, prototype-as-clay, and the
  unvetted-tools table.

## Numbers reported (none verified)

- antonmks: GitHub Copilot's runtime was ported from TypeScript to Rust by agents, about $120,000 in
  tokens plus three weeks of a developer's time, over 135 releases in 14.5 weeks, 430,000 lines to
  800,000 ([49878374](https://news.ycombinator.com/item?id=49878374)). No source was linked.
- Powdering7082: GitHub git pushes were 320M in Q1 this year against 80M in Q1 2020, citing GitHub's
  Innovation Graph ([49881032](https://news.ycombinator.com/item?id=49881032)); replies note more
  churn is not more or better software.
- necovek, passing on someone else's summary of GitHub's status history: about 10 incidents per month
  over ten years, about 22 per month over the last six ([49882855](https://news.ycombinator.com/item?id=49882855)).
- Tade0: Opus 5.5 resolved a large merge conflict in 1h16m for about $60
  ([49880277](https://news.ycombinator.com/item?id=49880277)).
- rfgplk: repos doing "~100k to ~250k loc changes per week" ([49878599](https://news.ycombinator.com/item?id=49878599));
  pretendscholar asked what applications need that and got no answer ([49882840](https://news.ycombinator.com/item?id=49882840)).

## Reading notes

- Model names (Opus 5.5, Fable, Astra 6 / "GPT 6 Astra", Luna, Kimi K3, GLM 5.2, DeepSeek 4.1) are as
  commenters wrote them. The refrain "try the latest model" drew its own pushback: lnkl
  ([49880323](https://news.ycombinator.com/item?id=49880323)), CoolestBeans
  ([49881773](https://news.ycombinator.com/item?id=49881773)) and lbrito
  ([49881111](https://news.ycombinator.com/item?id=49881111)) say they keep hearing it: lnkl "each year since 2023", lbrito "more or less every day for years",
  CoolestBeans a new "inflection point" each month.
- Skipped as noise: jokes, insults, the article's numbered-list "gotcha", a long side-argument
  about whether human and LLM errors are both "non-deterministic" (IshKebab, ben_w, InsideOutSanta
  and others), GitHub-versus-Azure blame, salary comparisons, licensing and ethics objections, and
  career-anxiety comments. The determinism argument's one practical residue, that agents don't learn
  between sessions and `AGENTS.md`/skills are "a proxy", is by vincent-uden
  ([49878598](https://news.ycombinator.com/item?id=49878598)).
- Several commenters describe their own products or repos; those are in
  [tool-mentioned-unvetted](../tools/tool-mentioned-unvetted.md) and were not evaluated.
- This records what commenters reported. echelon's "I haven't written a single line of code since February"
  ([49879369](https://news.ycombinator.com/item?id=49879369)) and nemo44x's "100% more PRs than a year ago and code
  quality is as high" ([49879469](https://news.ycombinator.com/item?id=49879469)) are self-reports.

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *surfaces* → [Typing code versus owning the software](../concepts/con-coding-vs-engineering.md) `con-coding-vs-engineering`
- *surfaces* → [Whoever ships the code owns it](../concepts/con-accountability.md) `con-accountability`
- *surfaces* → [Review capacity is the limit on agent output](../concepts/con-review-capacity.md) `con-review-capacity`
- *surfaces* → [Green tests, drifted behaviour](../anti-patterns/ap-green-tests-drift.md) `ap-green-tests-drift`
- *surfaces* → [Port against an oracle, or have the agent write the converter](../workflows/wf-port-with-oracle.md) `wf-port-with-oracle`
- *surfaces* → [Turn "what good looks like" into checks the agent runs](../workflows/wf-executable-quality-rules.md) `wf-executable-quality-rules`
- *disputes* → [Never trust a single session](../concepts/con-cross-model-review.md) `con-cross-model-review`
- *surfaces* → [Unbounded "looks good, go"](../anti-patterns/ap-unsupervised-autonomy.md) `ap-unsupervised-autonomy`

**Backlinks**

- [Article: Coding is NOT solved](../sources/src-article-coding-not-solved.md) `src-article-coding-not-solved` *discussed-in* this
- [Other tools mentioned (unvetted)](../tools/tool-mentioned-unvetted.md) `tool-mentioned-unvetted` *relates-to* this

**Evidence:** [49877988](https://news.ycombinator.com/item?id=49877988)

<!-- graph:links:end -->
