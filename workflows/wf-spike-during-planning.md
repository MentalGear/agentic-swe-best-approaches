---
summary: While the plan is still a draft, send subagents to implement it in a scratch directory and report back what they learned; the plan stays yours, the spike stays disposable.
tags: [planning, exploration]
stage: [planning, execution]
effort: medium
cost: high
scale: [feature, large]
links:
  - applies: con-iterative-loop
  - uses: tool-subagents
  - complements: wf-scaffold-then-spike
---
# Throwaway spikes while planning

- Seattle3503: during planning, "spin out sub agents to implement the current draft in a tmp dir and
  bring back lessons." It keeps them grounded in their starting point instead of an implementation
  that "meanders through the agents own discovery process," and makes questions concrete
  ([49852272](https://news.ycombinator.com/item?id=49852272)).
- theptip: for day/week-scale work, "having the agent go off and build a spike can be a quicker way of
  us understanding the design space"; a rough PR stack beats a plan doc for them
  ([49853061](https://news.ycombinator.com/item?id=49853061)).
- biimugan's complaint about Gemini CLI's plan mode shows why: a planner that can't run even a Python
  one-liner is "either blind or relying on its training data" ([49852844](https://news.ycombinator.com/item?id=49852844)).

## Steps

1. Draft plan in the main session.
2. Subagent (or worktree): "Implement this draft in a scratch dir. Don't touch the repo. Report what
   was harder than expected, what the plan got wrong, and what you'd change." Several in parallel for
   competing approaches.
3. Fold lessons into the plan; delete the spike.
