---
summary: For complex or core changes, ask for diagrams or an interactive demo explaining the change and the alternatives considered, and attach it to the PR for reviewers and future agents.
tags: [understanding, review]
stage: [understanding, review]
effort: low
cost: medium
scale: [feature, large]
links:
  - addresses: con-understanding-problem
  - uses: tool-artifacts
  - complements: wf-deterministic-views
  - critiqued-by: ap-trusting-explanations
---
# Explainer artifacts attached to PRs

bcherny's replacement for plan mode's understanding job
([49850929](https://news.ycombinator.com/item?id=49850929)):

> For complex diffs to core parts of the system, I will often ask it to make diagrams or even
> interactive demos so I can better understand the change and alternatives considered … I ask Claude
> to attach these artifacts to its PRs also, so others can understand and future Claudes have the
> context.

zobzu wants the harness to do it unprompted: "ok here's our overall current state in a simple
diagram" ([49853296](https://news.ycombinator.com/item?id=49853296)).

## Prompt

"Make a one-page HTML explainer of this change: the before/after data flow as a diagram, the two
alternatives you rejected and why, and the riskiest assumption. Link it from the PR description."

## Caveat

An explainer is the model's account of its own work. Verify the load-bearing claims
([ap-trusting-explanations](../anti-patterns/ap-trusting-explanations.md)) or generate the structural
parts deterministically ([wf-deterministic-views](wf-deterministic-views.md)).

aqme28 is considering a local "artifact mode" as a better way to see proposed changes
([49856728](https://news.ycombinator.com/item?id=49856728)).

## Second refresh (2026-09-27)

- rickye26 has agents write designs in HTML instead of Markdown for richer layout and interactivity,
  especially for UI work, and used to upload them as Claude artifacts for review ([49860141](https://news.ycombinator.com/item?id=49860141)).
- VadimPR has Claude make before/after videos of features and fixes; the skill is public in the Mudlet
  repo (`docs/demo-videos.md`) ([49860289](https://news.ycombinator.com/item?id=49860289)). jgalt212: "you must have tokens to burn"
  ([49860679](https://news.ycombinator.com/item?id=49860679)).

Also cited: [49854300](https://news.ycombinator.com/item?id=49854300), [49852511](https://news.ycombinator.com/item?id=49852511).
