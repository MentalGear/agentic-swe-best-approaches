---
summary: Ayman Nadeem's post-mortem of Nuanced, a plan-first coding app, and why she thinks plan modes are the wrong abstraction.
url: https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html
tags: [primary-source]
links:
  - argues: con-planning-vs-plan
  - argues: con-two-jobs-of-plan-mode
  - argues: con-iterative-loop
  - argues: con-understanding-problem
  - argues: con-ai-prose-fatigue
  - argues: con-mode-switch-cost
  - discussed-in: src-hn-thread
---
# Article: Plan mode is dead

- **Author:** Ayman Nadeem (HN: `aymandfire`), formerly GitHub, founder of Nuanced.
- **Published:** 2026-09-24
- **URL:** <https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html>

## What she built

Nuanced was a desktop coding app built around planning as a first-class primitive. You chatted in a
thread, the system surfaced ambiguities and asked you to decide them, it produced a persistent spec,
and then it implemented the spec and checked the code against it:

> chat → disambiguate by answering questions → generate spec → review spec → revise spec → approve → implement → review code
> ([article](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html))

She built it to answer one question: *how do humans keep a coherent mental model of a system while
machines change it faster than humans can inspect the changes?*

## Why it failed, in her words

1. **She conflated planning with a plan.** Thinking before building was valuable. The large
   structured artifact that recorded it was not; early users had little appetite for it.
2. **Models got good.** Each decision the model can reliably make alone is one fewer decision to
   surface to the human. Better models competed directly with a better planning interface.
3. **AI-generated text is painful to read.** Specs were long and "contained more information without
   creating more clarity". The fix they tried, a "Spec Tour" that summarised the spec, only added
   another layer of text.
4. **Planning and building were split in a way that felt like waterfall.** Real work interleaves them:
   the first attempt teaches you something that changes the plan. Once implementation began, going
   back to the planning chat felt like moving backwards.
5. **Separate plan and build modes made the user answer a meta-question** ("does this task deserve a
   plan?") that the tool could have answered from context.

## What she concludes

- The old loop was `plan → approve → execute`, because going the wrong way was expensive.
- The new loop is `understand → act → inspect → clarify → adjust → act again`. Planning still
  happens inside it; it just doesn't have to be a document called "the plan".
- Her biggest mistake: "turning the plan into an artifact instead of designing a process for improved
  human understanding."
- **Unsolved:** keeping human understanding current as the number of agents grows from five to
  hundreds. Agents should find "the fewest places where human attention can have the greatest
  impact" and surface enough context there.

## Clarification she added in the thread

Plan modes did two jobs: (1) make instructions precise enough for the agent and (2) help the human
understand what is being built. Job 1 is fading as models improve. Job 2 matters *more* as agents do
more, but a long generated document is the wrong interface for it
([49851044](https://news.ycombinator.com/item?id=49851044),
[49851212](https://news.ycombinator.com/item?id=49851212)).

Also cited: [49840054](https://news.ycombinator.com/item?id=49840054).
