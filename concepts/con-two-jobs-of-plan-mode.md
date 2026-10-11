---
summary: Plan mode did two jobs, making instructions precise for the agent and building human understanding; the first is fading, the second is growing.
tags: [core, planning]
stage: [planning, understanding]
links:
  - relates-to: con-understanding-problem
  - relates-to: con-underspecification
  - relates-to: con-plan-mode-is-a-prompt
---
# The two jobs of plan mode

The author's framing ([49851044](https://news.ycombinator.com/item?id=49851044)):

1. **Agent precision.** Give the agent instructions precise enough to execute. Fading, because
   models explore the repo and make reasonable assumptions on their own.
2. **Human understanding.** Help the human see what is about to be built. Growing, because each
   agent turn now covers more ground.

Commenters named further jobs plan mode was quietly doing for them:

| Job | Who | Notes |
|---|---|---|
| Force context gathering before writing | loveparade [49852489](https://news.ycombinator.com/item?id=49852489) | "I usually barely read [the plan]"; the value is the model reading enough code first. |
| A last "no" before risky edits | theholygrail [49852093](https://news.ycombinator.com/item?id=49852093) | "It was about making the human stop and look." |
| Emotional safety to grant more permissions | early_exit [49851942](https://news.ycombinator.com/item?id=49851942) | Better served by real guardrails; see [wf-least-privilege-data](../workflows/wf-least-privilege-data.md). |
| Parallel read-only exploration | loveparade [49852489](https://news.ycombinator.com/item?id=49852489) | Several agents can plan at once without worktree conflicts. |
| Escaping a dead end | rglover [49852420](https://news.ycombinator.com/item?id=49852420) | See [wf-plan-to-escape-spiral](../workflows/wf-plan-to-escape-spiral.md). |
| A known rhythm for walking away | trashface [49851295](https://news.ycombinator.com/item?id=49851295) | crunch → questions → plan → do. |

## Use it

Before reaching for plan mode, name which job you need done. Each one has a lighter or stronger
tool in this graph: follow this node's links.

Also cited: [49851212](https://news.ycombinator.com/item?id=49851212).
