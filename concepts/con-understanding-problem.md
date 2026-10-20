---
id: con-understanding-problem
type: concept
title: Keeping the human's mental model current
summary: The unsolved problem the article ends on; when agents write most of the code, how does the human still understand the system, and how does that scale to many agents?
tags: [core, understanding, open-problem]
stage: [understanding]
sources: [49851173, 49852511, 49853788, 49852993, 49852601, 49853739, 49853759, 49854680, 49852822, 49852178, 49853201, 49856300, 49858465, 49857547, 49857952, 49855641, 49858204, 49854943, 49870125, 49860769, 49879305, 49878532, 49879353, 49880788, 49880395, 49881373, 49880796, 49882719, 49879747]
links:
  - relates-to: con-ai-prose-fatigue
---
# Keeping the human's mental model current

The article ends here: "We still haven't solved how to help people stay oriented as hundreds of
increasingly capable agents change a system at once."

## The worry

taurath: "I'm actively watching understanding slip away from developers, code review getting pared
down to no-comment checkmarks" ([49851173](https://news.ycombinator.com/item?id=49851173)).
eddy162: reading diffs doesn't scale anymore; plan mode was how they kept their mental model
([49852822](https://news.ycombinator.com/item?id=49852822)).

## Positions on the fix

| Position | Who | Caveat raised |
|---|---|---|
| Ask the agent to explain; diagrams, sequence charts, tests that prove its claims | frankc [49852511](https://news.ycombinator.com/item?id=49852511), bcherny [49850929](https://news.ycombinator.com/item?id=49850929) | "It's really good at making you feel that you understand things" (jeppester [49853788](https://news.ycombinator.com/item?id=49853788)); generated diagrams focus on the wrong things (abbefaria27 [49852993](https://news.ycombinator.com/item?id=49852993)); it doesn't volunteer what it thinks is irrelevant (spiffytech [49852601](https://news.ycombinator.com/item?id=49852601)). |
| Generate views *deterministically* from the code | teekert [49854001](https://news.ycombinator.com/item?id=49854001) | Only covers what a script can extract. See [wf-deterministic-views](../workflows/wf-deterministic-views.md). |
| Delegate typing, not thinking; keep part of the work yourself | philbo [49853739](https://news.ycombinator.com/item?id=49853739), dsign [49852178](https://news.ycombinator.com/item?id=49852178) | Leaves throughput on the table, knowingly. |
| A system that holds the program's evolving state for the operator | _bobm [49853759](https://news.ycombinator.com/item?id=49853759) | Doesn't exist yet. |
| Model the *solution/problem*, not the code | arendtio [49854680](https://news.ycombinator.com/item?id=49854680) | Reframing, not a tool. |

## Use it

Combine the two that hold up: deterministic views for structure you must not get wrong, and
adversarially-checked explanations ([wf-adversarial-review](../workflows/wf-adversarial-review.md))
for the rest. Treat an unchecked agent explanation as a hypothesis.

## Later in the thread (refresh 2026-09-26)

- aDyslecticCrow: no documentation system transfers institutional knowledge; people do. codethief:
  a company's value is "the mental map the team has built of the problem"
  ([49856300](https://news.ycombinator.com/item?id=49856300), [49858465](https://news.ycombinator.com/item?id=49858465)).
- senordevnyc disagrees for well-documented codebases: an agent can read years of commits, tickets
  and design docs in half an hour and explain the history better than a person
  ([49857547](https://news.ycombinator.com/item?id=49857547)); maccard's experience in a large codebase was that exploring one area filled half
  the context window every time ([49857952](https://news.ycombinator.com/item?id=49857952)).
- hoc is building canvas-based views for independent analysis and visualisation of changes after the
  fact ([49855641](https://news.ycombinator.com/item?id=49855641)).
- nunez: if maintainers lose access to frontier models, they inherit code nobody understands
  ([49858204](https://news.ycombinator.com/item?id=49858204)). fendy3002: knowing what each module does may be enough ([49854943](https://news.ycombinator.com/item?id=49854943)).

aDyslecticCrow: what the code *should* do can itself be institutional knowledge, spread across tools,
databases and other departments' systems you don't have code for; a person knows whom to ask
([49870125](https://news.ycombinator.com/item?id=49870125)). taurath: teams that still care about code understanding keep shipping, while
vibe-coding teams in the same org "flounder after the initial burst of features" ([49860769](https://news.ycombinator.com/item?id=49860769)).

## Second thread (2026-09-28)

- **Do some of it by hand.** josephmtummon (about two years' experience): building without an LLM takes longer,
  but "my own context of problem is so much better", and they then review with an LLM. They worry newer
  developers plateau if they never put the tools down and have set up separate skills that make them build
  understanding as they go ([49879305](https://news.ycombinator.com/item?id=49879305)). The article's version: keep an AI-free hobby project.
- **Is reading code understanding?** efficax: "Reading the code does not mean you understand the code"
  ([49878532](https://news.ycombinator.com/item?id=49878532)); jdkoeck: believing you can understand behaviour without at least reading the high-level code
  "is truly silly" ([49879353](https://news.ycombinator.com/item?id=49879353)). layer8: modularise with succinct interfaces so you can reason locally, and
  make sure for every part that someone reasoned through it with rigour ([49880788](https://news.ycombinator.com/item?id=49880788)). ModernMech asks why
  reasoning has to happen at source level and says a codebase is "only as good as what you can prove"
  ([49880395](https://news.ycombinator.com/item?id=49880395)); discreteevent answers that unreviewed AI code was never reasoned about by anyone
  ([49881373](https://news.ycombinator.com/item?id=49881373)).
- **Trust comes from field use.** misterderpie and skydhash accept libraries because thousands of users have
  exercised them, and say code written in-house or by an AI five minutes ago has no such record
  ([49880796](https://news.ycombinator.com/item?id=49880796), [49882719](https://news.ycombinator.com/item?id=49882719)).
- **Measure, don't guess.** slifin laments that reverse debuggers were never operationalised, citing Bret
  Victor's "Seeing Spaces" on seeing inside what you build ([49879747](https://news.ycombinator.com/item?id=49879747)).

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *relates-to* → [Generated prose is hard to review](../concepts/con-ai-prose-fatigue.md) `con-ai-prose-fatigue`

**Backlinks**

- [Trusting the agent's account of its code](../anti-patterns/ap-trusting-explanations.md) `ap-trusting-explanations` *instance-of* this
- [Whoever ships the code owns it](../concepts/con-accountability.md) `con-accountability` *relates-to* this
- [Generated prose is hard to review](../concepts/con-ai-prose-fatigue.md) `con-ai-prose-fatigue` *relates-to* this
- [Typing code versus owning the software](../concepts/con-coding-vs-engineering.md) `con-coding-vs-engineering` *relates-to* this
- [Review capacity is the limit on agent output](../concepts/con-review-capacity.md) `con-review-capacity` *relates-to* this
- [The two jobs of plan mode](../concepts/con-two-jobs-of-plan-mode.md) `con-two-jobs-of-plan-mode` *relates-to* this
- [Article: Plan mode is dead](../sources/src-article.md) `src-article` *argues* this
- [Adversarial review by a second session](../workflows/wf-adversarial-review.md) `wf-adversarial-review` *addresses* this
- [Agent-written decision log](../workflows/wf-decision-log.md) `wf-decision-log` *addresses* this
- [Scripts that draw the system from code](../workflows/wf-deterministic-views.md) `wf-deterministic-views` *addresses* this
- [Current-state code and docs that cannot drift (maintainer-supplied)](../workflows/wf-drift-proof-docs.md) `wf-drift-proof-docs` *relates-to* this
- [Explainer artifacts attached to PRs](../workflows/wf-explainer-artifacts.md) `wf-explainer-artifacts` *addresses* this
- [You write the spec, the agent asks](../workflows/wf-human-authored-spec.md) `wf-human-authored-spec` *addresses* this
- [Living spec directory and TODO.md](../workflows/wf-living-spec-dir.md) `wf-living-spec-dir` *addresses* this
- [Parent theorizes, children execute](../workflows/wf-orchestrator-subagents.md) `wf-orchestrator-subagents` *relates-to* this
- [Refactor to make the change easy](../workflows/wf-refactor-before-feature.md) `wf-refactor-before-feature` *addresses* this

**Evidence:** [49851173](https://news.ycombinator.com/item?id=49851173), [49852511](https://news.ycombinator.com/item?id=49852511), [49853788](https://news.ycombinator.com/item?id=49853788), [49852993](https://news.ycombinator.com/item?id=49852993), [49852601](https://news.ycombinator.com/item?id=49852601), [49853739](https://news.ycombinator.com/item?id=49853739), [49853759](https://news.ycombinator.com/item?id=49853759), [49854680](https://news.ycombinator.com/item?id=49854680), [49852822](https://news.ycombinator.com/item?id=49852822), [49852178](https://news.ycombinator.com/item?id=49852178), [49853201](https://news.ycombinator.com/item?id=49853201), [49856300](https://news.ycombinator.com/item?id=49856300), [49858465](https://news.ycombinator.com/item?id=49858465), [49857547](https://news.ycombinator.com/item?id=49857547), [49857952](https://news.ycombinator.com/item?id=49857952), [49855641](https://news.ycombinator.com/item?id=49855641), [49858204](https://news.ycombinator.com/item?id=49858204), [49854943](https://news.ycombinator.com/item?id=49854943), [49870125](https://news.ycombinator.com/item?id=49870125), [49860769](https://news.ycombinator.com/item?id=49860769), [49879305](https://news.ycombinator.com/item?id=49879305), [49878532](https://news.ycombinator.com/item?id=49878532), [49879353](https://news.ycombinator.com/item?id=49879353), [49880788](https://news.ycombinator.com/item?id=49880788), [49880395](https://news.ycombinator.com/item?id=49880395), [49881373](https://news.ycombinator.com/item?id=49881373), [49880796](https://news.ycombinator.com/item?id=49880796), [49882719](https://news.ycombinator.com/item?id=49882719), [49879747](https://news.ycombinator.com/item?id=49879747)

<!-- graph:links:end -->
