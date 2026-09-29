---
summary: Iterate on plan.md with the agent, then start a new session that reads only the plan and implements it; the file is audit trail, handoff and context reset in one.
tags: [planning, context, handoff]
stage: [planning, context]
effort: medium
cost: medium
scale: [feature, large]
links:
  - applies: con-context-boundary
  - applies: con-model-tiering
  - complements: wf-adversarial-review
  - variant-of: wf-conversational-planning
  - uses: tool-plannotator
---
# Plan file, then a fresh session

## When

Big changes, long planning conversations, or when a different (cheaper) model will implement.
brokencode and pseudosavant: "Small plans you can just ask for, and big plans you work through
building a plan.md file" ([49851138](https://news.ycombinator.com/item?id=49851138),
[49851248](https://news.ycombinator.com/item?id=49851248)).

## Steps

1. "Propose a plan for change X and write to file Y", with `plans/X.md` as the file and no code changes
   (throwaway27448, [49850846](https://news.ycombinator.com/item?id=49850846))
2. Review and iterate on the file. Annotate in place if you have a tool for it
   ([tool-plannotator](../tools/tool-plannotator.md)); a file stops the agent "repeatedly asking if I’m ready to implement the plan" (brokencode, [49851138](https://news.ycombinator.com/item?id=49851138)).
3. Optional: adversarial pass by a fresh session ([wf-adversarial-review](wf-adversarial-review.md)).
4. New session: `Read plans/X.md. List ambiguities, friction points and oversights first; resolve them with me; then implement.` (after stingraycharles, [49852329](https://news.ycombinator.com/item?id=49852329))
5. For long plans, execute in slices: "Execute steps M-N from file Y" (throwaway27448, [49850846](https://news.ycombinator.com/item?id=49850846))
6. When done, record deviations in the plan and rename it (e.g. `X.done.md`) so the directory shows
   what was built versus planned (OtomotO, [49854204](https://news.ycombinator.com/item?id=49854204)).

## Why

- Survives compaction and context clears; jumploops wants "one source of “truth” that sits across context windows" ([49851148](https://news.ycombinator.com/item?id=49851148)).
- The fresh session re-checks assumptions without the planning conversation's bias
  ([con-context-boundary](../concepts/con-context-boundary.md)).
- Leaves an audit trail of decisions in git.

Template: [templates/plan.md](../templates/plan.md).

drutaTushar keeps plans as a baseline to point a drifting agent back to, and batches instructions when
running many agents ([49864373](https://news.ycombinator.com/item?id=49864373)).

Also cited: [49852750](https://news.ycombinator.com/item?id=49852750), [49854255](https://news.ycombinator.com/item?id=49854255), [49852221](https://news.ycombinator.com/item?id=49852221).
