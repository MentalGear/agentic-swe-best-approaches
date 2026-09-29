---
summary: A finished plan is a natural point to clear context and start a fresh session; people disagree on whether large context windows made that obsolete.
tags: [context, cost]
stage: [context]
links:
  - relates-to: con-model-tiering
---
# The plan as a context boundary

Early Claude Code plan mode could clear the chat and start the implementation from the plan alone.
That option is now off by default. Per nojs, it can be re-enabled with the setting
`"showClearContextOnPlanAccept": true`, and the stated rationale for hiding it was that with a 1M
context window most users no longer need it ([49852890](https://news.ycombinator.com/item?id=49852890);
setting name as reported in the thread, verify against your version).

## For clearing context at the plan

- **Cost.** jmb99 finishes planning at 200–350k tokens; carrying that into implementation "balloons
  the cost" ([49852421](https://news.ycombinator.com/item?id=49852421)).
- **Quality.** cronin101: a fresh session re-checks the plan's assumptions "before context was
  poisoned" and avoids a disastrous mid-implementation compaction
  ([49853717](https://news.ycombinator.com/item?id=49853717)). jonathanlydall reports clearing
  context before execution "vastly improves the quality" ([49854255](https://news.ycombinator.com/item?id=49854255)).
- **Persistence.** jumploops wants one source of truth that survives compaction
  ([49851148](https://news.ycombinator.com/item?id=49851148)).

## Against

- JasonSage found agents did better with the history kept, and stopped having to copy every caveat
  and rejected idea into the plan ([49852284](https://news.ycombinator.com/item?id=49852284)).
- CGamesPlay links a write-up arguing the clear-and-implement step increased cost
  ([stencil.so/blog/prewalk](https://stencil.so/blog/prewalk), [49851395](https://news.ycombinator.com/item?id=49851395));
  not verified here.

## Use it

Clear context when the planning conversation is long, contains dead ends you don't want repeated,
or when implementation will run on a different model. Keep it when the conversation holds many
small decisions that never made it into the plan file.

## Later in the thread (refresh 2026-09-26)

- For: lyjia accepts the plan with a context clear because it's "a really good spot" ([49857634](https://news.ycombinator.com/item?id=49857634)).
- Against: jaapz tried plan files handed to a fresh session and found "too much fiddling … It really
  didn't result in better output" ([49855652](https://news.ycombinator.com/item?id=49855652)); hoc found executing agents with a reduced plan
  filled gaps wrongly ([wf-phased-handoffs](../workflows/wf-phased-handoffs.md), [49855641](https://news.ycombinator.com/item?id=49855641)).
- The underlying limit: "AI, looses its memory every time we press 'new thread'" (aDyslecticCrow,
  [49856300](https://news.ycombinator.com/item?id=49856300)), and in a large codebase just exploring one area can use half the context window
  (maccard, [49857952](https://news.ycombinator.com/item?id=49857952)).

Also cited: [49850744](https://news.ycombinator.com/item?id=49850744), [49851144](https://news.ycombinator.com/item?id=49851144), [49852232](https://news.ycombinator.com/item?id=49852232).
