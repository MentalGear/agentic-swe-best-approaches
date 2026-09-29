---
summary: Shell commands the harness runs on events such as before a tool call; can deny edits while a read-only flag is set, which gives plan mode the teeth it lacks.
tags: [claude-code, built-in, safety]
origin: built-in
stage: [safety]
effort: medium
links:
  - addresses: con-plan-mode-is-a-prompt
  - enables: wf-least-privilege-data
  - enables: wf-conversational-planning
---
# Claude Code hooks

Hooks are configured in `.claude/settings.json` and run deterministically on harness events, so they
enforce what a prompt can only request. Docs: <https://code.claude.com/docs/en/hooks>.

## Uses from the thread

- ChicagoDave hooked the start of planning and replaced the built-in planner with their own
  ([49851180](https://news.ycombinator.com/item?id=49851180)).
- The idea of making mutating tools error in plan mode (bionhoward, jstanley) is implementable as a
  `PreToolUse` hook that denies file-editing tools while a flag is set. The template below blocks
  `Edit`/`Write`/`MultiEdit`/`NotebookEdit` only; `Bash` can still write files, so pair it with
  permission deny rules for mutating commands if you need a hard guarantee.

## Template

[templates/hooks/readonly-guard.sh](../templates/hooks/readonly-guard.sh) with settings snippet
[templates/hooks/settings.readonly.json](../templates/hooks/settings.readonly.json): `touch .claude/READONLY`
to make the session discussion-only; remove it to allow edits. It's a switch you control, not the
model.

Also cited: [49852457](https://news.ycombinator.com/item?id=49852457), [49853894](https://news.ycombinator.com/item?id=49853894).
