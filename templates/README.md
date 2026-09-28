# Templates

Copy-ready files distilled from the workflows in this knowledge base. Each one names the workflow
node it implements. None are active in this repo; copy them into a project to use them.

| File | Copy to | Implements |
|---|---|---|
| [CLAUDE.planning.md](CLAUDE.planning.md) | append to your `CLAUDE.md` | [wf-conversational-planning](../workflows/wf-conversational-planning.md), [con-blast-radius](../concepts/con-blast-radius.md), [con-domain-language](../concepts/con-domain-language.md) |
| [plan.md](plan.md) | `plans/<name>.md` | [wf-plan-file-fresh-session](../workflows/wf-plan-file-fresh-session.md) |
| [handoff.md](handoff.md) | `plans/<name>.handoff-N.md` | [wf-phased-handoffs](../workflows/wf-phased-handoffs.md) |
| [prompts/adversarial-review.md](prompts/adversarial-review.md) | paste, or make a subagent | [wf-adversarial-review](../workflows/wf-adversarial-review.md) |
| [skills/interview/SKILL.md](skills/interview/SKILL.md) | `.claude/skills/interview/SKILL.md` | [wf-interview-first](../workflows/wf-interview-first.md) |
| [skills/feasibility/SKILL.md](skills/feasibility/SKILL.md) | `.claude/skills/feasibility/SKILL.md` | [wf-feasibility-check](../workflows/wf-feasibility-check.md) |
| [hooks/readonly-guard.sh](hooks/readonly-guard.sh) + [hooks/settings.readonly.json](hooks/settings.readonly.json) | `.claude/hooks/` + merge into `.claude/settings.json` | [tool-claude-code-hooks](../tools/tool-claude-code-hooks.md) |
