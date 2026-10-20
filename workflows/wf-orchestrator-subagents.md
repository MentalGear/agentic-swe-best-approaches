---
id: wf-orchestrator-subagents
type: workflow
title: Parent theorizes, children execute
summary: A long-lived parent session holds the plan and the theory; it dispatches narrowly-scoped subagents with only the context they need, and stays available to be quizzed.
tags: [orchestration, context]
stage: [execution, context]
effort: high
cost: high
scale: [large, long-run]
sources: [49853717, 49853101, 49850778, 49840824, 49842589, 49850597, 49863290, 49860129]
links:
  - uses: tool-subagents
  - applies: con-context-boundary
  - tension-with: ap-orchestration-theater
  - uses: tool-artifacts
  - relates-to: con-understanding-problem
  - relates-to: wf-drift-proof-docs
---
# Parent theorizes, children execute

- cronin101: a parent "theorizing about the root cause of issues based on evidence and then
  dispatching targeted child sessions to fix based on theories and concrete telemetry examples."
  Bonus: "a session you can quiz about architecture while one is heads-down working against a spec"
  ([49853717](https://news.ycombinator.com/item?id=49853717)).
- spike021: split the plan into parts, each to a subagent "with fresh, only relevant context"
  ([49853101](https://news.ycombinator.com/item?id=49853101)).
- skybrian: ask what the commits will be, then one subagent per commit
  ([49850778](https://news.ycombinator.com/item?id=49850778)).

## Lessons from a local-model swarm

SillyUsername runs a supervisor, 6–15 small "minion" models and a validator. Up-front preparation
("preflight") took hours instead of minutes. Fix: drop all but basic setup, and before every step
make the supervisor ask "is this a design choice? if not, can this run in parallel? If so, hand it
off *now*." Minions catch and fix incomplete handoffs through their own QA gates; some duplicated
fixes are cheaper than a sequential supervisor ([49840824](https://news.ycombinator.com/item?id=49840824)).
adastra22 and tcdent: tell the planner to plan high-level only — the implementing agent will know more
than the planner did ([49842589](https://news.ycombinator.com/item?id=49842589),
[49850597](https://news.ycombinator.com/item?id=49850597)).

## Caveat

See [ap-orchestration-theater](../anti-patterns/ap-orchestration-theater.md): elaborate pipelines can
burn tokens without output.

## Disputed (2026-09-27)

boorang disables subagents: in microservice-sized repos one agent holds the whole context, and
subagents "waste a lot of unnecessary tokens doing code exploration that the main agent is going to
end up duplicating". They ran the same plan both ways on separate branches and had agents judge the
code; one session per phase won on quality and tokens. Subagents may suit monorepos better
([49863290](https://news.ycombinator.com/item?id=49863290)).

darkwi11ow goes the other way for large changes: one high-level plan, split into N plans by area,
implemented in parallel where possible ([49860129](https://news.ycombinator.com/item?id=49860129)).

## Proposal: reuse idle subagents before spawning new ones (2026-10-20)

Not reported in either thread; suggested by the maintainer of this knowledge base. Before dispatching a task,
the coordinator checks whether a running or idle subagent already holds relevant context (it just worked in
the same area, or it has already explored the repo) and sends the task to it instead of starting a fresh one.
The saving is the exploration tokens a new agent spends re-reading the repository, the cost boorang
describes above ("a lot of unnecessary tokens doing code exploration",
[49863290](https://news.ycombinator.com/item?id=49863290)).

Reuse when:
- the new task builds on what the agent just did (a follow-up fix, the next step in the same module);
- the agent's exploration of the repo is what the new task needs.

Start a fresh agent when:
- the job is review or a second opinion; the reviewer must not inherit the author's context
  ([con-cross-model-review](../concepts/con-cross-model-review.md));
- the agent's context is already large or cluttered with dead ends, so every further turn costs more and
  it may anchor on its earlier choices ([ap-anchoring-on-first-choice](../anti-patterns/ap-anchoring-on-first-choice.md));
- the task is unrelated, where leftover context only adds noise.

A reused agent is not free: its whole context is re-read each turn (cheaper when cached), so the saving
shrinks as it grows. Untested here; compare token use on one real task before adopting it as a rule.

## Proposal: a progress overview for the user, with usage stats (2026-10-20)

Also from the maintainer, not from either thread. Untested.

- **Overview.** The orchestrator keeps one overview page ([tool-artifacts](../tools/tool-artifacts.md)) listing
  each subagent, its task, status (running, idle, finished, blocked), finished tasks and what it is waiting on.
  It aims at the open question in the "Plan mode is dead" article of where human attention is best spent
  ([con-understanding-problem](../concepts/con-understanding-problem.md)).
- **Single writer.** Subagents report status to the orchestrator in their final message, and only the
  orchestrator updates the page. Several agents editing one page would overwrite each other.
- **Usage stats.** Token counts, tool calls and duration per subagent are worth adding if the harness shows
  them to the orchestrator. Cache-hit rates are less likely to be visible to a model; the more reliable source is
  the API's per-request usage fields (cache read and write tokens) collected by a hook or log script. I have not
  checked what any given harness exposes.

## Proposal: a shared repo brief instead of keeping agents alive (2026-10-20)

The maintainer's counter-idea to reusing idle agents: keep a general knowledge cache for new agents. My view:
for a well-documented repository this usually beats reuse, because a new agent reads the README and
architecture notes, then only the paths it needs, without inheriting another agent's context, dead ends or
anchoring. It also suits reviewers, who must start fresh. Order of preference: documented brief first, reuse of
an idle agent for same-area follow-up second, a cold exploration last. The brief has to stay accurate, which is
what [wf-drift-proof-docs](wf-drift-proof-docs.md) is for; an out-of-date brief is worse than none.
Untested; editorial opinion, not a finding.

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *uses* → [Subagents](../tools/tool-subagents.md) `tool-subagents`
- *applies* → [The plan as a context boundary](../concepts/con-context-boundary.md) `con-context-boundary`
- *tension-with* → [Orchestration theater](../anti-patterns/ap-orchestration-theater.md) `ap-orchestration-theater`
- *uses* → [HTML explainers and artifacts](../tools/tool-artifacts.md) `tool-artifacts`
- *relates-to* → [Keeping the human's mental model current](../concepts/con-understanding-problem.md) `con-understanding-problem`
- *relates-to* → [Current-state code and docs that cannot drift (maintainer-supplied)](../workflows/wf-drift-proof-docs.md) `wf-drift-proof-docs`

**Backlinks**

- [Subagents](../tools/tool-subagents.md) `tool-subagents` *enables* this

**Evidence:** [49853717](https://news.ycombinator.com/item?id=49853717), [49853101](https://news.ycombinator.com/item?id=49853101), [49850778](https://news.ycombinator.com/item?id=49850778), [49840824](https://news.ycombinator.com/item?id=49840824), [49842589](https://news.ycombinator.com/item?id=49842589), [49850597](https://news.ycombinator.com/item?id=49850597), [49863290](https://news.ycombinator.com/item?id=49863290), [49860129](https://news.ycombinator.com/item?id=49860129)

<!-- graph:links:end -->
