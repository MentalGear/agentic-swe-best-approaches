---
summary: A planner that hasn't done the deep dive writes code-level detail that the better-informed implementing agent then has to follow or fight.
tags: [planning]
stage: [planning]
links:
  - instance-of: con-ai-prose-fatigue
  - tension-with: con-underspecification
---
# Implementation details in the plan

adastra22: "Tell the planner to not do all that. Just plan out the high level. No code. No
implementation details" ([49842589](https://news.ycombinator.com/item?id=49842589)). tcdent's reason:
the zero-shot that writes the ticket "is much less informed than the agent doing the work will be"
([49850597](https://news.ycombinator.com/item?id=49850597)). plaguuuuuu found detailed plans raise the
model's cognitive load and worsen code organisation ([49853088](https://news.ycombinator.com/item?id=49853088)).

The balance: specify *decisions and constraints* (what, why, what not), leave *how* to the
implementer, and validate the risky "how" with a spike ([wf-scaffold-then-spike](../workflows/wf-scaffold-then-spike.md)).

Also cited: [49852894](https://news.ycombinator.com/item?id=49852894).
