---
summary: Adversarial review sessions can always find something; without a severity bar or a pass limit they never converge.
tags: [review, cost]
stage: [review]
links:
  - relates-to: con-cross-model-review
---
# Review loops with no stop rule

sdevonoes, on int_19h's "Never trust a single session" ([49854550](https://news.ycombinator.com/item?id=49854550)): "Problem is where to stop. Open a 3rd session? … Let's
try a fifth now…" ([49855213](https://news.ycombinator.com/item?id=49855213)).

sdiupIGPWEfh ran 20–30 adversarial sessions a few times: for some tasks they "never converge on
anything that yet another session won't find fault with, recommending an alternative already ruled
out by another session", even with the earlier reasoning documented
([49856983](https://news.ycombinator.com/item?id=49856983)).

## Stop rules

- Stop when a pass finds nothing at the blocking level, not when it finds nothing.
- Cap passes (two or three).
- Give the reviewer the decisions already made and tell it not to reopen them unless they're wrong
  on the facts.
