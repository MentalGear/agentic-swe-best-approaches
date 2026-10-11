---
summary: A long-lived parent session holds the plan and the theory; it dispatches narrowly-scoped subagents with only the context they need, and stays available to be quizzed.
tags: [orchestration, context]
stage: [execution, context]
effort: high
cost: high
scale: [large, long-run]
links:
  - uses: tool-subagents
  - applies: con-context-boundary
  - tension-with: ap-orchestration-theater
---
# Parent theorizes, children execute

- cronin101: a parent "theorizing about the root cause of issues based on evidence and then
  dispatching targeted child sessions to fixed [sic] based on theories and concrete telemetry examples."
  Bonus: "a session you can quiz about architecture while one is heads-down working against a spec"
  ([49853717](https://news.ycombinator.com/item?id=49853717)).
- spike021: split the plan into parts, each to a subagent "with fresh, only relevant context"
  ([49853101](https://news.ycombinator.com/item?id=49853101)).
- skybrian: ask what the commits will be, then one subagent per commit
  ([49850778](https://news.ycombinator.com/item?id=49850778)).

## Lessons from a local-model swarm

SillyUsername runs a supervisor, 6–15 small "minion" models and a validator. Up-front preparation
("preflight") took hours instead of minutes. Fix: drop all but basic setup, and before every step
make the supervisor ask "if this is not the design choices, can this be run in parallel? If so, hand it off NOW." Minions catch and fix incomplete handoffs through their own QA gates; some duplicated
fixes are cheaper than a sequential supervisor ([49840824](https://news.ycombinator.com/item?id=49840824)).
adastra22 and tcdent: tell the planner to plan high-level only — the implementing agent will know more
than the planner did ([49842589](https://news.ycombinator.com/item?id=49842589),
[49850597](https://news.ycombinator.com/item?id=49850597)).

## Caveat

See [ap-orchestration-theater](../anti-patterns/ap-orchestration-theater.md): elaborate pipelines can
burn tokens without output.

## Disputed (2026-09-27)

boorang disables subagents: in microservice-sized repos one agent holds the whole context, and
subagents "waste alot of unnecessary tokens doing code exploration that the main agent is going to
end up duplicating". They ran the same plan both ways on separate branches and had agents judge the
code; one session per phase won on quality and tokens. Subagents may suit monorepos better
([49863290](https://news.ycombinator.com/item?id=49863290)).

darkwi11ow goes the other way for large changes: one high-level plan, split into N plans by area,
implemented in parallel where possible ([49860129](https://news.ycombinator.com/item?id=49860129)).
