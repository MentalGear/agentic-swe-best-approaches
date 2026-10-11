---
summary: Don't let the system that made a change also judge it; record where every claim came from so it can be re-derived, and put deterministic checks outside the agent.
tags: [verification, review]
stage: [review, understanding]
links:
  - tension-with: con-cross-model-review
  - relates-to: ap-trusting-explanations
---
# Check outside the agent

ake2l names the problem: the same system "creates the change, explains why the change is correct, and basically also grades itself", and human review erodes because "After 50 correct looking changes humans start trusting the green output" ([49881912](https://news.ycombinator.com/item?id=49881912)). Their answer is not more review but a different kind of check: deterministic checks, frozen behaviour, architecture constraints, explicit evidence, and "UNKNOWN when I simply cannot prove something". In their words: "Not another smarter agent judging the first agent, but boring independent machinery which does not care how convincing the explanation sounds."

solooperator1 frames it as provenance rather than truth-arbitration: record, per claim, which tool call produced it, what query ran, what source was cited and when, so a human or a simpler check can re-run the chain. "You don't need the AI to know what's true; you need every claim to be re-derivable on demand", and "verification-by-construction scales where human re-checking doesn't" ([49882630](https://news.ycombinator.com/item?id=49882630)).

## In practice

- AlisaYoki took facts out of the model in a small travel app: places are grounded or dropped, and each knowledge card links to its original source. "Chat is just a login, and a product is an object that can be checked" ([49895441](https://news.ycombinator.com/item?id=49895441)).
- Deterministic views of the code ([wf-deterministic-views](../workflows/wf-deterministic-views.md)) and end-to-end tests that carry the plan ([wf-test-harness-as-plan](../workflows/wf-test-harness-as-plan.md)) are this idea applied to structure and behaviour.
- This knowledge base applies it to its own quotations: each one is looked up in the source rather than typed, and checked against the cited comment on every build.

## Counterpoint

empath75: "Claude Code does most of this stuff now already, in terms of verifications and citations, almost to a fault" ([49880708](https://news.ycombinator.com/item?id=49880708)). The disagreement is about who does the checking: the agent itself, or something outside it.
