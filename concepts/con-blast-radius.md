---
summary: Skip planning for small reversible changes; require an explicit plan and a human stop for auth, payments, shared schemas, data migrations and prod.
tags: [safety, risk]
stage: [safety]
links:
  - relates-to: con-underspecification
---
# Scale ceremony to blast radius

Most commenters who dropped plan mode still plan when the change is risky. theholygrail:

> For a one-file change I don't bother. For anything that touches auth, payments, or a shared schema
> I still want the plan written down first — not because the model can't figure it out, but because
> I need a moment where I can still say "no" before it starts editing.
> ([49852093](https://news.ycombinator.com/item?id=49852093))

## Signals that justify a plan step

- Touches auth, payments, shared schemas, migrations, infra/devops (theholygrail, anarticle [49853054](https://news.ycombinator.com/item?id=49853054)).
- Destructive data operations. anarticle: the agent concluded "we copied it all over so I can delete
  it from source" after a failed copy. 0xfaded caught an agent proposing to run an unfinished
  backfill against prod ([49852392](https://news.ycombinator.com/item?id=49852392)).
- More than 2–3 files (altern8, [49854423](https://news.ycombinator.com/item?id=49854423)).
- Work that needs human validation between stages, such as manual playtesting in games (bentt,
  [49852531](https://news.ycombinator.com/item?id=49852531)).
- You're unfamiliar with the domain and need its unwritten rules explained (omsta, [49854769](https://news.ycombinator.com/item?id=49854769)).

## Use it

Encode the list in `CLAUDE.md` so the agent proposes a plan by itself when a change crosses the
line, instead of you remembering to switch modes (the article's "meta-question" problem; see
[con-mode-switch-cost](con-mode-switch-cost.md)). Template: [templates/CLAUDE.planning.md](../templates/CLAUDE.planning.md).

## Later in the thread (refresh 2026-09-26)

- parf02, on long-horizon scientific work with expensive compute: users want the harness "to stop and
  confirm the cost (and plan) before it goes ahead" ([49858959](https://news.ycombinator.com/item?id=49858959)). Cost is blast radius too.
- eurekin: plan first when the work depends on proprietary libraries and services the model can't
  know ([49859806](https://news.ycombinator.com/item?id=49859806)); z3ratul163071: in complex existing codebases, "plan, then implement is much
  better and, more importantly, much safer" ([49855156](https://news.ycombinator.com/item?id=49855156)).
- early_exit: a hallucination on the surface is fine; on a "load-bearing" component the agent then
  builds on it ([49856764](https://news.ycombinator.com/item?id=49856764)).

Also cited: [49852668](https://news.ycombinator.com/item?id=49852668), [49859499](https://news.ycombinator.com/item?id=49859499).
