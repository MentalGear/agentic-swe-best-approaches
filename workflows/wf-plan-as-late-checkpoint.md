---
summary: Explore and decide in normal conversation first; switch to plan mode only at the end to consolidate one reviewable plan, catch remaining gaps, and clear context before building.
tags: [planning, context]
stage: [planning, context]
effort: low
cost: low
scale: [feature, large]
links:
  - variant-of: wf-conversational-planning
  - uses: tool-claude-code-plan-mode
  - applies: con-context-boundary
  - addresses: con-underspecification
---
# Plan mode as a late checkpoint

Several people who kept plan mode moved it *later*: it's the step between deciding and building,
not the first thing you do.

## Shapes reported

- **lyjia**, per ticket, written into their user `CLAUDE.md`
  ([49857634](https://news.ycombinator.com/item?id=49857634)):
  1. Scoping discussion: research and pick an approach (auto mode).
  2. Planning: turn the scoping into a concrete plan for review (plan mode).
  3. Implementation (auto mode).

  Plan mode "forces the model to double-check its plans (I find even with Opus 5.5 it still discovers
  gaps), and it gives me an opportunity to clear context at a really good spot." ([49857634](https://news.ycombinator.com/item?id=49857634))
- **jonmagic** (works at GitHub, on Copilot's plan mode): it didn't stick "until very recently, when I
  used it the way you describe. I was just putting it too early in the process." They explore on
  their own first, then use plan mode to be interviewed on "the last few things it needs before
  implementation" ([49857763](https://news.ycombinator.com/item?id=49857763)).
- **rnvannatta**: chat through the fiddly bits, then `/plan` "to get everything in one document", then
  review and amend it. "Two phases: hammer out key design decisions then write and amend the
  document" ([49856513](https://news.ycombinator.com/item?id=49856513)).
- **user3939382**: plan mode as "a phase transition to let the agent decide when discovery is
  sufficient" ([49855997](https://news.ycombinator.com/item?id=49855997)).
- **radley**: critical early in a project when long-tail decisions are unresolved; less needed as
  skills and memory fill in; still used for big features "to confirm that I've asked for what I want
  in the right way" ([49859777](https://news.ycombinator.com/item?id=49859777)).

## Steps

1. Discuss and explore without a mode ([wf-conversational-planning](wf-conversational-planning.md)).
2. When the decisions feel settled, enter plan mode and ask for one consolidated plan plus any gaps it
   still sees.
3. Review, amend, then accept with a context clear if the discussion was long
   ([con-context-boundary](../concepts/con-context-boundary.md)).
