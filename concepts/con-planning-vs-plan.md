---
summary: The thinking before building is valuable; a large generated plan document usually isn't. Keep the activity, shrink the artifact.
tags: [core, planning]
stage: [planning]
links:
  - tension-with: con-ai-prose-fatigue
  - relates-to: con-iterative-loop
---
# Planning is not the plan

The article's central lesson. Nuanced assumed that (a) thinking before implementing is valuable and
(b) preserving that thinking in a big structured spec is also valuable. Users confirmed (a) and
rejected (b).

The thread mostly agreed and compressed it to one line: *"Plans are of little importance, but
planning is essential"* (recroad, quoting Churchill/Eisenhower, [49853332](https://news.ycombinator.com/item?id=49853332)).
gwerbin put the practical version: "you don't 'need' plan mode. But you do still need to do all of
the things you would do with plan mode" ([49852746](https://news.ycombinator.com/item?id=49852746)).

## What survives when the document shrinks

- Establishing domain language and key requirements before tool calls start.
- A question-and-answer pass so ambiguities get decided by the human, not guessed.
- A sanity check that the model's understanding matches yours, stated plainly.
- A point where you can still say "no" before edits start (see [con-blast-radius](con-blast-radius.md)).

## Where people disagree

Several commenters want the plan *as an artifact* anyway: for audit trails (throwaway27448), as
a context-reset boundary ([con-context-boundary](con-context-boundary.md)), or as a handoff to a
cheaper model ([con-model-tiering](con-model-tiering.md)). The disagreement is less about planning
than about who reads the plan: the human, the next agent, or nobody (txhwind writes one mostly for
later forensics, [49852437](https://news.ycombinator.com/item?id=49852437)).

## Use it

Default to planning in conversation. Write a plan file only when something downstream consumes it:
a fresh session, another model, a reviewer, or a future you doing forensics.

Also cited: [49851118](https://news.ycombinator.com/item?id=49851118), [49851176](https://news.ycombinator.com/item?id=49851176), [49852095](https://news.ycombinator.com/item?id=49852095).
