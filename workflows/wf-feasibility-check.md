---
summary: Instead of a full plan, ask for a short feasibility verdict and two or three solution options, just enough to confirm the agent's approach matches yours.
tags: [planning, lightweight]
stage: [planning]
effort: low
cost: low
scale: [small, feature]
links:
  - alternative-to: tool-claude-code-plan-mode
  - addresses: con-ai-prose-fatigue
  - variant-of: wf-conversational-planning
---
# Lightweight feasibility check

- skissane made a `feasibility` skill: "evaluate feasibility of this idea and propose solution
  options". It is lighter than plan mode because the skill says not to build a detailed plan, only a
  high-level summary ([49852981](https://news.ycombinator.com/item?id=49852981)).
- socketcluster asks for tradeoffs and a suggested approach on complex features; takes the
  suggestion about half the time, but the constraints listed are reliably good
  ([49851312](https://news.ycombinator.com/item?id=49851312)).
- 6thbit wants a "brainstorming mode": read, run commands, produce reports, discuss — without a plan
  document on every turn ([49850896](https://news.ycombinator.com/item?id=49850896)). zmmmmm similarly
  wants a read-only exploration mode ([49852150](https://news.ycombinator.com/item?id=49852150)).

Skill template: [templates/skills/feasibility/SKILL.md](../templates/skills/feasibility/SKILL.md).
