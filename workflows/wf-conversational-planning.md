---
summary: Say "discuss first, no code yet" (or set a standing phrasing rule) and plan in the normal session; act only on an explicit go.
tags: [planning, default]
stage: [planning, intent]
effort: low
cost: low
scale: [small, feature]
links:
  - applies: con-planning-vs-plan
  - addresses: con-mode-switch-cost
  - relies-on: con-plan-mode-is-a-prompt
  - complements: wf-interview-first
  - alternative-to: tool-claude-code-plan-mode
---
# Plan in conversation, no mode

The most common replacement for plan mode in the thread. Since plan mode is only a prompt
([con-plan-mode-is-a-prompt](../concepts/con-plan-mode-is-a-prompt.md)), a sentence does the same
job and is easier to undo mid-conversation.

## When

Default for anything that isn't a trivial edit. Escalate to a plan file
([wf-plan-file-fresh-session](wf-plan-file-fresh-session.md)) when the conversation gets long or
another session/model will execute.

## Steps

1. Open with an explicit no-edit instruction. Phrasings from the thread:
   - "This is discussion; no code changes yet." (topspin, [49852430](https://news.ycombinator.com/item?id=49852430))
   - "Let's brainstorm, don't implement anything yet." … then "now do that." (int_19h, [49854521](https://news.ycombinator.com/item?id=49854521))
   - "Discuss your plan with me before implementing anything." (b0rtb0rt, [49852317](https://news.ycombinator.com/item?id=49852317))
   - Append "evaluate", "investigate" or "report only" when you just want to see what it would do (geraneum, [49852668](https://news.ycombinator.com/item?id=49852668)).
2. Ask what the commits will be. skybrian: "a conversation can be the plan. It helps if you ask it
   what the commits will be and then tell it to use subagents to implement them"
   ([49850778](https://news.ycombinator.com/item?id=49850778)).
3. Iterate until the decisions are yours, then give an explicit go.

Other harnesses ship without a mode at all: cavoirom has used Amp Code since late 2025 with "just
conversation" ([49854848](https://news.ycombinator.com/item?id=49854848)).

## Make it a standing rule

Put the trigger in `CLAUDE.md` so you don't have to repeat it:

- solarkraft: "I want to…" / "Let's…" → plan; "Do X" → act; questions are answered, never treated as
  instructions ([49851108](https://news.ycombinator.com/item?id=49851108)).
- skybrian added instructions "to not edit any checked-in files if the prompt contains a question"
  ([49850778](https://news.ycombinator.com/item?id=49850778)).

Ready-made block: [templates/CLAUDE.planning.md](../templates/CLAUDE.planning.md).

## Caveats

Several people still find newer models "trigger happy" and edit after a plain question
(ivanjermakov [49854456](https://news.ycombinator.com/item?id=49854456), coolgoose
[49854704](https://news.ycombinator.com/item?id=49854704)). If that matters, back the sentence with a
hook ([tool-claude-code-hooks](../tools/tool-claude-code-hooks.md)).

## Later in the thread (refresh 2026-09-26)

- More phrasings: "what's your thoughts?" / "feel free to pushback" (OzzyB, [49856115](https://news.ycombinator.com/item?id=49856115)); "please do
  not do anything yet, just tell me what you would do" and "please feel free to ask if anything is
  unclear" at forks in the road (captainmuon, [49857316](https://news.ycombinator.com/item?id=49857316)).
- Put it in default rules: nunez has int_19h's brainstorm-then-"now do that" pattern ([49854521](https://news.ycombinator.com/item?id=49854521)) in rules that load
  every session ([49858145](https://news.ycombinator.com/item?id=49858145)); robertlagrant "basically just reimplemented plan mode via AGENTS.md"
  to stop a model burning a subscription's 5-hour allowance on tool calls before a quick conversation
  ([49855393](https://news.ycombinator.com/item?id=49855393)).
- jstummbillig's reading of the Claude Code team's point: you don't need `/plan` to get planning, you
  can say "Let's plan this out" ([49857099](https://news.ycombinator.com/item?id=49857099)). jaapz talks a few turns, then says go, and only for
  complex work ([49855652](https://news.ycombinator.com/item?id=49855652)).
- **Caveat that got stronger:** Iolaum adds "Stop once you['ve] written the plan" to every planning
  request because models go ahead otherwise ([49859323](https://news.ycombinator.com/item?id=49859323)). Name the stop condition explicitly.

Also cited: [49850621](https://news.ycombinator.com/item?id=49850621), [49852510](https://news.ycombinator.com/item?id=49852510), [49854342](https://news.ycombinator.com/item?id=49854342), [49852221](https://news.ycombinator.com/item?id=49852221).
