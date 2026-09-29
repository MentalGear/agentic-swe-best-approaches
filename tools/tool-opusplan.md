---
summary: Claude Code model alias that uses a stronger model while planning and a cheaper one for execution.
tags: [claude-code, built-in, cost]
origin: built-in
stage: [planning, execution]
effort: low
links:
  - instance-of: con-model-tiering
  - relates-to: tool-claude-code-plan-mode
---
# opusplan model setting

diegof79 used plan mode partly "to execute with another model (i.e., using the barely documented
opusplan feature)" ([49851420](https://news.ycombinator.com/item?id=49851420)). Select it with
`/model` or the model setting. It only helps if you actually use plan mode; the manual alternative
is telling Claude to launch subagents on a different model for the implementation tasks (same
comment). Check the model-configuration docs for which models the alias maps to in your version.

slimebot80 uses it because Opus is better at thinking and Sonnet is cheaper for execution, and asks
whether switching models mid-session costs extra usage; unanswered in the thread ([49866076](https://news.ycombinator.com/item?id=49866076)).
