---
summary: Child agents with their own fresh context, used for isolated review, parallel spikes and per-slice implementation.
tags: [claude-code, built-in, orchestration]
origin: built-in
stage: [review, execution, context]
effort: low
links:
  - enables: wf-adversarial-review
  - enables: wf-orchestrator-subagents
  - enables: wf-spike-during-planning
  - applies: con-cross-model-review
---
# Subagents

The mechanism behind most multi-session workflows in the thread: a subagent starts without the
parent's conversation, which is exactly what an unbiased reviewer or a focused implementer needs.
Define reusable ones in `.claude/agents/*.md` with their own tools and model. Git worktrees keep
parallel implementers from colliding.

Evidence: skybrian (subagent per commit, [49850778](https://news.ycombinator.com/item?id=49850778)),
spike021 (per plan part, [49853101](https://news.ycombinator.com/item?id=49853101)), Seattle3503
(spikes in tmp dirs, [49852272](https://news.ycombinator.com/item?id=49852272)), cronin101
(child sessions per theory, [49853717](https://news.ycombinator.com/item?id=49853717)).
