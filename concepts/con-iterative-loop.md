---
summary: The article's replacement for plan→approve→execute; planning happens inside a tight loop rather than as a gate in front of it.
tags: [core, process]
stage: [execution, planning]
links:
  - tension-with: con-blast-radius
---
# Understand → act → inspect → adjust

Old loop (when a wrong direction was expensive): `plan → approve → execute`.
New loop (article): `understand → act → inspect → clarify → adjust → act again`.

Eupolemos points out this is essentially the OODA loop (observe, orient, decide, act) — the method
for when you're "in it" rather than planning from a distance
([49853602](https://news.ycombinator.com/item?id=49853602)). lowbloodsugar's summary: "Waterfall is
dead. Agile iteration is the future. That's the amazing realization?"
([49854039](https://news.ycombinator.com/item?id=49854039)).

## Why it works now

- Agents test their own work and revise after inspecting results, so a wrong first step is cheap.
- theptip: for day/week-scale tasks, a quick spike maps the design space faster than a plan, and a
  rough PR stack teaches more than a plan doc ([49853061](https://news.ycombinator.com/item?id=49853061)).
- ed_mercer: "usually faster to correct the agent later, once the initial implementation is in
  place" — less cognitively demanding than front-loading ([49852617](https://news.ycombinator.com/item?id=49852617)).

## Where it breaks

When the "act" step is irreversible (data, prod, money) or the inspect step needs a human
(manual QA). Then fall back to a gate: see [con-blast-radius](con-blast-radius.md).

## Later in the thread (refresh 2026-09-26)

- bob1029: "Planning largely doesn't work because it's extrapolation." The complex successes they've
  seen came from the model probing live data, rerunning the compiler, and retrying shell commands
  until it worked ([49858402](https://news.ycombinator.com/item?id=49858402)).
- astrostl: plan mode pushes toward "zero/one-shot big bangs over iterative features/bugfixes"
  ([49858230](https://news.ycombinator.com/item?id=49858230)).
- jchook wants a steering mode: the agent narrates its direction and you interject any time without a
  hard interrupt ([49858449](https://news.ycombinator.com/item?id=49858449)).
- nchmy notices the tension in "a waterfall approach with well defined milestones" when you don't yet know how to build it
  ([49855137](https://news.ycombinator.com/item?id=49855137)).

Also cited: [49852784](https://news.ycombinator.com/item?id=49852784).
