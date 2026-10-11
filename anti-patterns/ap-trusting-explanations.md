---
summary: Agent explanations feel complete but omit what the model deemed irrelevant and can be confidently wrong; a feeling of understanding isn't understanding.
tags: [understanding, review]
stage: [understanding, review]
links:
  - instance-of: con-understanding-problem
---
# Trusting the agent's account of its code

- jeppester: "it's really good at making you feel that you understand things. Then when you actually
  dig into the code, there are many things that are not like you'd expect." Example: an SSO simulator
  that remembered the last login in a variable instead of a cookie; later agents then built test
  helpers to work around that statefulness ([49853788](https://news.ycombinator.com/item?id=49853788)).
- abbefaria27: generated architecture docs look great unless you know the code; then they focus on
  the wrong things and miss the mental model ([49852993](https://news.ycombinator.com/item?id=49852993)).
- spiffytech: you get caught off guard by what the model didn't volunteer
  ([49852601](https://news.ycombinator.com/item?id=49852601)).

Fixes: [wf-adversarial-review](../workflows/wf-adversarial-review.md) on explanations too (int_19h,
[49854550](https://news.ycombinator.com/item?id=49854550)), and
[wf-deterministic-views](../workflows/wf-deterministic-views.md) for structure.
