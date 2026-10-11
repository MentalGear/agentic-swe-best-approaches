---
summary: Before building a feature, have the agent remove the cruft the feature would build on, and fold that cleanup into the feature's work.
tags: [code-quality, process]
stage: [execution]
effort: medium
cost: medium
scale: [feature, large]
links:
  - addresses: con-understanding-problem
  - complements: wf-decomment-pass
  - applies: con-iterative-loop
---
# Refactor to make the change easy

the_other got "rigorous about making the agent refactor old code" before building on it
([49855004](https://news.ycombinator.com/item?id=49855004)). Their example: two client-side caches of
related server state, kept in sync by extra code long after one API call started returning everything.
Consumers disagreed about which cache was the fallback, which hid that one was redundant.

What they do:

- Tell the agent to "refactor to make the change easier" before the feature.
- Roll the debt payback into feature tasks, because standalone cleanup never gets prioritised.
- Caveat: on a limited model budget (they mostly use a cheaper model), they've never seen the model
  *propose* such a refactor unprompted, so the human has to spot it.

literallyroy asks whether anyone runs scheduled agent automations for regular cleanup
([49856017](https://news.ycombinator.com/item?id=49856017)); no answers yet.
