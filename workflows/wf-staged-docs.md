---
summary: For big features, iterate a high-level strategy doc, then a technical sprint doc, then implementation and e2e scenarios, with a human resolving "founder questions" and another model reviewing each stage.
tags: [spec, process, milestones]
stage: [planning, review]
effort: high
cost: high
scale: [large]
links:
  - applies: con-cross-model-review
  - refines: wf-plan-file-fresh-session
  - tension-with: con-iterative-loop
---
# Strategy doc, then sprint doc, then build

smnscu ([49852909](https://news.ycombinator.com/item?id=49852909)):

1. Strategy document.
2. "Sprint" document with the technical implementation.
3. Implementation.
4. Update end-to-end test scenarios.

Each stage is iterated with Claude, with the human setting direction and answering "founder
questions", and a different model (usually Codex, sometimes Gemini) reviewing.

## Related shapes

- wildzzz: plan everything wanted up front, then milestones: proof of concept → test suite → features
  in layers ([49852661](https://news.ycombinator.com/item?id=49852661)).
- dmix: several agents work on Markdown files the human "manually perfects", split per feature/PR,
  plus design handoff docs with screenshots and wireframes ([49852408](https://news.ycombinator.com/item?id=49852408)).
- spacedcowboy: for months-long projects, an hour or two iterating a living plan, until they have "talked it down from wherever it first wanted to go", before starting ([49841767](https://news.ycombinator.com/item?id=49841767)).

## When

Serious, long-lived features where the heavier upfront cost pays back. This is the opposite end from
[wf-prototype-as-clay](wf-prototype-as-clay.md); pick by [con-blast-radius](../concepts/con-blast-radius.md).
