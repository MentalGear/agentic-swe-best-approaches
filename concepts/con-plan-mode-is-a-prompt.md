---
id: con-plan-mode-is-a-prompt
type: concept
title: Plan mode is only a prompt
summary: Per the Claude Code team, plan mode is a reminder appended to each message, not a sandbox or tool restriction; treat it as convention, not safety.
tags: [claude-code, safety, facts]
stage: [safety, planning]
sources: [49850929, 49851117, 49852369, 49852457, 49853894, 49850876, 49852215, 49854835, 49852163, 49857523, 49858198, 49855658, 49855427, 49857316, 49859323, 49859853, 49855037, 49862882, 49860370, 49860218, 49867762, 49860673]
links:
  - relates-to: con-blast-radius
---
# Plan mode is only a prompt

bcherny ([49850929](https://news.ycombinator.com/item?id=49850929)), who works on Claude Code:

> all plan mode does is add a little reminder to every user message along the lines of "you're in
> plan mode, please don't code yet" … plan mode has always been a prompt — it has never changed the
> toolset because doing so would break the prompt cache.

Follow-ups from the same person: plan mode isn't being removed; `/plan` or asking Claude to enter
plan mode still works; shift+tab may be remapped by default
([49851117](https://news.ycombinator.com/item?id=49851117)).

## Disputed

dbbk, replying later in the thread, says the opposite: plan mode "has harness level behaviour - it's
restricted to readonly tools, and it re-reads its plan into context after compaction"
([49854835](https://news.ycombinator.com/item?id=49854835)). TechSquidTV had asked whether plan
state survives compaction ([49852163](https://news.ycombinator.com/item?id=49852163)). The two
statements may describe different versions, or the difference between the *toolset offered to the
model* (unchanged, per bcherny) and *what the permission layer allows* (restricted, per dbbk and the
docs). Until verified against the current docs, don't rely on plan mode as your only guard.

## Consequences

- **It is not a sandbox.** monster_truck: "Plan was never a sandbox or a permissions system"
  ([49850876](https://news.ycombinator.com/item?id=49850876)). fy20 recalls an earlier version
  where the permission system prompted before non-read-only actions even in YOLO mode
  ([49852369](https://news.ycombinator.com/item?id=49852369)); the current docs describe
  permission behaviour for plan mode separately, so check them for your version
  ([docs](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)).
- **Suggested improvement** (bionhoward, jstanley): keep the tool list identical for caching but
  make mutating tools return an error while in plan mode
  ([49852457](https://news.ycombinator.com/item?id=49852457), [49853894](https://news.ycombinator.com/item?id=49853894)).
  Hooks can approximate this today; see [tool-claude-code-hooks](../tools/tool-claude-code-hooks.md).
- **Any sentence works as well.** "Don't write any code yet" in a normal session produces the same
  effect; see [wf-conversational-planning](../workflows/wf-conversational-planning.md).

## Use it

For real protection use permissions, hooks, read-only credentials or a container. Use plan mode,
or a sentence, for intent.

## Later in the thread (refresh 2026-09-26)

- **More reports that plan mode doesn't block edits**, which supports bcherny's description over
  dbbk's: losvedir learned it was a prompt "when Claude Code edited a file despite being in plan mode"
  ([49857523](https://news.ycombinator.com/item?id=49857523)); collingreen had a model "go off and read other repos and make changes just
  yesterday while in 'plan mode'" ([49858198](https://news.ycombinator.com/item?id=49858198)).
- **Other harnesses do restrict tools.** bulder: GitHub Copilot for VS Code configures Plan mode "to
  disable everything except reading, asking the user questions, and writing into the memory
  scratchpad" ([49855658](https://news.ycombinator.com/item?id=49855658)). weird-eye-issue repeats the fix: have the tool reject the call in plan
  mode without touching the tool schema or cache ([49855427](https://news.ycombinator.com/item?id=49855427)).
- **Newer models overrun "plan only".** Iolaum now adds "Stop once you've written the plan", because
  otherwise there's roughly a 35% chance (their estimate) the model implements it too; plan mode is
  "a useful shortcut when I want to have an agent do read-only work without having to worry about
  giving it appropriate stop conditions" ([49859323](https://news.ycombinator.com/item?id=49859323)). viccis reports the same trend
  ([49859853](https://news.ycombinator.com/item?id=49859853)); captainmuon wants "a dry run mode that just disables all external commands"
  ([49857316](https://news.ycombinator.com/item?id=49857316)).
- Plan modes predate Claude Code: Aider and Cline had them (GodelNumbering, [49855037](https://news.ycombinator.com/item?id=49855037)).

## Second refresh (2026-09-27)

- thaeli: in GitHub Copilot, plan mode "has teeth": the agent may only write to a temp directory and
  the plan document, tool calls are restricted, and a separate read-only "ask" mode exists. "I've seen
  the model 'forget' and try to start coding - it bounces off a hard permissions failure and that
  'reminds' it that it's in plan mode" ([49862882](https://news.ycombinator.com/item?id=49862882)).
- thejosh: Claude Code in plan mode "does destructive operations, requiring a hook to tell it not to"
  ([49860370](https://news.ycombinator.com/item?id=49860370)); adamsb6 could coax partial execution without leaving plan mode ([49860218](https://news.ycombinator.com/item?id=49860218)).
- almostroot: telling it not to make changes "feels an awful lot like 'Make no mistakes'"
  ([49860673](https://news.ycombinator.com/item?id=49860673)).
- pokeapallascat: plan mode was "unusable" for them after the clear-before-implementing option was
  removed in July ([49867762](https://news.ycombinator.com/item?id=49867762)); see [tool-claude-code-plan-mode](../tools/tool-claude-code-plan-mode.md).

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *relates-to* → [Scale ceremony to blast radius](../concepts/con-blast-radius.md) `con-blast-radius`

**Backlinks**

- [Cargo-cult mega-prompts](../anti-patterns/ap-cargo-cult-prompts.md) `ap-cargo-cult-prompts` *relates-to* this
- [Modes make you answer a meta-question](../concepts/con-mode-switch-cost.md) `con-mode-switch-cost` *relates-to* this
- [The two jobs of plan mode](../concepts/con-two-jobs-of-plan-mode.md) `con-two-jobs-of-plan-mode` *relates-to* this
- [HN thread: Plan mode is dead](../sources/src-hn-thread.md) `src-hn-thread` *contains-statement* this
- [Claude Code hooks](../tools/tool-claude-code-hooks.md) `tool-claude-code-hooks` *addresses* this
- [Claude Code plan mode](../tools/tool-claude-code-plan-mode.md) `tool-claude-code-plan-mode` *instance-of* this
- [Plan in conversation, no mode](../workflows/wf-conversational-planning.md) `wf-conversational-planning` *relies-on* this
- [Read-only credentials instead of trust](../workflows/wf-least-privilege-data.md) `wf-least-privilege-data` *relies-on* this

**Evidence:** [49850929](https://news.ycombinator.com/item?id=49850929), [49851117](https://news.ycombinator.com/item?id=49851117), [49852369](https://news.ycombinator.com/item?id=49852369), [49852457](https://news.ycombinator.com/item?id=49852457), [49853894](https://news.ycombinator.com/item?id=49853894), [49850876](https://news.ycombinator.com/item?id=49850876), [49852215](https://news.ycombinator.com/item?id=49852215), [49854835](https://news.ycombinator.com/item?id=49854835), [49852163](https://news.ycombinator.com/item?id=49852163), [49857523](https://news.ycombinator.com/item?id=49857523), [49858198](https://news.ycombinator.com/item?id=49858198), [49855658](https://news.ycombinator.com/item?id=49855658), [49855427](https://news.ycombinator.com/item?id=49855427), [49857316](https://news.ycombinator.com/item?id=49857316), [49859323](https://news.ycombinator.com/item?id=49859323), [49859853](https://news.ycombinator.com/item?id=49859853), [49855037](https://news.ycombinator.com/item?id=49855037), [49862882](https://news.ycombinator.com/item?id=49862882), [49860370](https://news.ycombinator.com/item?id=49860370), [49860218](https://news.ycombinator.com/item?id=49860218), [49867762](https://news.ycombinator.com/item?id=49867762), [49860673](https://news.ycombinator.com/item?id=49860673)

<!-- graph:links:end -->
