---
summary: The agent treats its first decision as fixed, refusing "breaking" changes to uncommitted code or wrapping the old path in defensive code and comments instead of replacing it.
tags: [planning, code-quality]
stage: [planning, execution]
links:
  - tension-with: con-iterative-loop
  - relates-to: ap-comment-dumping
---
# Anchoring on the first choice

Reply to "it makes plausible choices and you can retroactively ask it to change them":

- matsemann: "It gets so hung up in its initial decision. Like, it won't make changes because they're
  'breaking', for something never even committed. Or it will litter the code base with defensive code
  and comments about the path not chosen" ([49855100](https://news.ycombinator.com/item?id=49855100)).
- qvq: "Changing the initial decision is a hassle so I just start over most of the time"
  ([49859368](https://news.ycombinator.com/item?id=49859368)).
- loeg hasn't seen the refusal, but has seen the defensive code and comments
  ([49858752](https://news.ycombinator.com/item?id=49858752)).
- everforward: a small early data-model decision leaves the agent where every fix except a rewrite
  has bad outcomes, and it won't launch the rewrite on its own
  ([49856641](https://news.ycombinator.com/item?id=49856641)).

## Fixes

- Say explicitly that nothing is shipped and breaking changes are fine.
- Restart from a corrected prompt rather than steering a long session (qvq).
- Catch it before code: [wf-second-research-pass](../workflows/wf-second-research-pass.md).

Also cited: [49856721](https://news.ycombinator.com/item?id=49856721).
