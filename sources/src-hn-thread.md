---
summary: 291-comment Hacker News discussion (item 49840054, 315 points) where practitioners describe the planning workflows and tools they actually use.
url: https://news.ycombinator.com/item?id=49840054
tags: [primary-source]
links:
  - contains-statement: con-plan-mode-is-a-prompt
  - disputes: con-planning-vs-plan
  - surfaces: con-underspecification
  - surfaces: con-blast-radius
  - surfaces: con-context-boundary
  - surfaces: con-cross-model-review
  - surfaces: wf-plan-as-late-checkpoint
  - surfaces: wf-review-code-not-plans
  - surfaces: wf-second-research-pass
  - surfaces: wf-refactor-before-feature
  - surfaces: ap-anchoring-on-first-choice
  - surfaces: ap-endless-review
  - surfaces: wf-agentic-test-selection
---
# HN thread: Plan mode is dead

- **URL:** <https://news.ycombinator.com/item?id=49840054>
- **Submitted:** 2026-09-24 by `jmvldz` · 315 points at first capture. Comments: 294 at first capture, 446 at the refresh on 2026-09-26, 492 on 2026-09-27 (capture log in `.miner/state.json`).
- **Captured via:** the HN Algolia items API (`https://hn.algolia.com/api/v1/items/49840054`).

## Shape of the discussion

The thread split roughly three ways:

| Camp | Position | Representative comments |
|---|---|---|
| **Mode is dead, planning isn't** | You don't need a *mode*; tell the agent to discuss first and write no code yet, or have it write `plan.md`. The model now respects that. | tcdent [49850621](https://news.ycombinator.com/item?id=49850621), brokencode [49851138](https://news.ycombinator.com/item?id=49851138), topspin [49852430](https://news.ycombinator.com/item?id=49852430), Mond_ [49852510](https://news.ycombinator.com/item?id=49852510) |
| **Keep plan mode** | Models still guess intent wrong; a plan is the cheapest point to catch it; it keeps the human in the loop and reviewing a plan is easier than reviewing code. | dbbk [49841243](https://news.ycombinator.com/item?id=49841243), akersten [49851057](https://news.ycombinator.com/item?id=49851057), wvenable [49852964](https://news.ycombinator.com/item?id=49852964), jonathanlydall [49854255](https://news.ycombinator.com/item?id=49854255), Marha01 [49854294](https://news.ycombinator.com/item?id=49854294) |
| **Plan mode is too weak** | Built-in plan mode is insufficient; they run heavier processes: plan files reviewed by other models, annotation tools, spec directories, phased hand-offs, test harnesses. | stingraycharles [49852329](https://news.ycombinator.com/item?id=49852329), dmix [49852408](https://news.ycombinator.com/item?id=49852408), SkyPuncher [49852074](https://news.ycombinator.com/item?id=49852074), orisho [49854300](https://news.ycombinator.com/item?id=49854300) |

## The key statement from Claude Code

`bcherny` (works on Claude Code) wrote that plan mode "has always been a prompt": a reminder added to
each user message, never a change of toolset, because changing tools would break the prompt cache
([49850929](https://news.ycombinator.com/item?id=49850929)). He said plan mode is not going away
(`/plan` still works) but shift+tab may be remapped
([49851117](https://news.ycombinator.com/item?id=49851117)). See
[con-plan-mode-is-a-prompt](../concepts/con-plan-mode-is-a-prompt.md).

## What the refresh added (152 comments, 2026-09-26)

- More users report plan mode didn't stop edits, which supports the "only a prompt" description; other
  harnesses (GitHub Copilot) do restrict tools.
- Newer models overrun "plan only" requests more often; people now name an explicit stop condition.
- New methods: plan mode as a *late* checkpoint, reviewing PRs instead of plans, a second research
  pass against the first plan, refactoring before features.
- New pitfalls: anchoring on the first choice, and adversarial review that never converges.
- Disputes: prose handoffs between phase agents lose information; clarifying questions can be
  low-value; some no longer care about comment noise.

## What the second refresh added (49 comments, 2026-09-27)

- More reports that Claude Code's plan mode doesn't block edits; GitHub Copilot's plan and ask modes
  enforce restrictions through permissions.
- Disputes on multi-agent setups: one head-to-head test favoured one session per phase over subagents;
  multi-agent design review found mostly nits.
- New: agent-picked tests for slow CI; two opposite traps (waterfall revival versus feature sprawl).
- About half the new comments were flame, a vibe-coding definition debate, or hiring arguments; skipped.

## Reading notes

- Model names in the thread (Fable 5.1, Opus 5.5, Astra, GPT 5.6 Sol, Qwen, Gemma, Kimi) are as
  commenters wrote them. Experiences differ sharply by model, budget and codebase size; several
  commenters point out that heavy token use is affordable for some and not others
  ([49854226](https://news.ycombinator.com/item?id=49854226)).
- A few comments were flagged, deleted or were jokes; they were skipped.
- Links to people's own products are recorded in [tool-mentioned-unvetted](../tools/tool-mentioned-unvetted.md)
  and were not evaluated.
- This knowledge base records what commenters *reported*. Claims like 12–48h unattended runs are
  single-person anecdotes, not measurements.
