---
summary: Built-in mode (shift+tab or /plan) that adds a reminder not to code yet to each message; plus the hidden setting that restores clear-context-on-accept.
tags: [claude-code, built-in]
origin: built-in
stage: [planning]
effort: low
links:
  - instance-of: con-plan-mode-is-a-prompt
  - relates-to: con-context-boundary
---
# Claude Code plan mode

| Fact | Source |
|---|---|
| Enter with shift+tab (cycle modes) or `/plan`, or ask Claude to enter plan mode | bcherny [49851117](https://news.ycombinator.com/item?id=49851117) |
| Implementation: a reminder added to each user message; toolset unchanged (prompt-cache reasons) | bcherny [49850929](https://news.ycombinator.com/item?id=49850929) |
| Not being removed; shift+tab may be remapped by default | bcherny [49851117](https://news.ycombinator.com/item?id=49851117) |
| "Clear context and implement" on plan accept is hidden; re-enable with `"showClearContextOnPlanAccept": true` in settings | nojs [49850744](https://news.ycombinator.com/item?id=49850744), [49852890](https://news.ycombinator.com/item?id=49852890) (as reported; verify) |
| VS Code extension supports selecting and annotating plan text | bartread [49851028](https://news.ycombinator.com/item?id=49851028) |

Docs: <https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode>

## Wishlist from the thread

- Show what changed between plan revisions, so you don't re-review unchanged parts (stephen_cagle,
  [49852117](https://news.ycombinator.com/item?id=49852117)).
- A real read-only mode where mutating tools error out (see [con-plan-mode-is-a-prompt](../concepts/con-plan-mode-is-a-prompt.md)).

pokeapallascat dates the removal of the default clear-before-implementing option to July, and recalls
a period when models kept planning and researching across sessions unless explicitly told to code
([49867762](https://news.ycombinator.com/item?id=49867762)).
