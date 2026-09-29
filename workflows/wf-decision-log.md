---
summary: Have the agent write a short design note before each non-trivial change and record deviations afterward; you rarely read it, but it's there for forensics.
tags: [persistence, audit]
stage: [understanding, context]
effort: low
cost: low
scale: [feature, large]
links:
  - applies: con-planning-vs-plan
  - addresses: con-understanding-problem
---
# Agent-written decision log

txhwind: one line in `AGENTS.md` makes the agent write a document before implementing. "Usually I
won't read that document, because I don't want to micromanage agents." It works like an ADR, to find
later "what agents missed, made mistakes on or misaligned on"
([49852437](https://news.ycombinator.com/item?id=49852437)).

OtomotO makes it write deviations and rename the plan once done
([49854204](https://news.ycombinator.com/item?id=49854204)); jmb99 has agents update `docs/API.md` on
every PR ([49852496](https://news.ycombinator.com/item?id=49852496)).

## Format

`decisions/NNNN-title.md`: context · decision · alternatives rejected · consequences · deviations
(filled after). Keep it under a screen; see [con-ai-prose-fatigue](../concepts/con-ai-prose-fatigue.md).

## Later in the thread (refresh 2026-09-26)

Huppie has the agent keep docs plus a worklog of what/why/decisions, and finds it slightly better than
beads so far ([49856954](https://news.ycombinator.com/item?id=49856954)). mgr86 keeps decisions in org-mode files that both Claude and they read
([49856713](https://news.ycombinator.com/item?id=49856713)).

notjackiechan: capture the *motivation* behind a plan and its expected and observed results, not the
plan itself, because real work is full of "nah, screw that decision" ([49863948](https://news.ycombinator.com/item?id=49863948)). real-hacker
recommends the early-release book *Regenerative Software* on externalising knowledge about software
from the code ([49863413](https://news.ycombinator.com/item?id=49863413); not reviewed here).

Also cited: [49850846](https://news.ycombinator.com/item?id=49850846).
