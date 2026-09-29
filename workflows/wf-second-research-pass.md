---
summary: After the first plan, send the agent back to research the codebase's own constraints and ask it to improve the plan; first plans are often the first idea that works, not the smallest change.
tags: [planning, quality]
stage: [planning, review]
effort: low
cost: medium
scale: [feature, large]
links:
  - variant-of: wf-spec-until-quiet
  - mitigates: ap-anchoring-on-first-choice
  - addresses: con-underspecification
---
# Challenge the first plan with more research

sebastiangrill's loop for big changes ([49856721](https://news.ycombinator.com/item?id=49856721)):

1. Ask for a plan for the feature.
2. Ask for "a second round of research with the current project in mind".
3. Ask whether it can improve the plan.
4. Read the plan, note issues, have it correct them.

Why: models "are really lazy and will stop at the first solution without even understanding your
project." One first plan "wanted to add a few thousand lines of code just to support a very minimal
part of a feature"; after the second research round it "recommended a very small change to the
existing codebase that did the same thing."

gattacas_janito makes the same point from before AI: the first idea "has always created a local
minimum", and models turn a bad first idea into code quickly. They spent two days designing a
high-risk feature that the model then built in under two hours
([49856928](https://news.ycombinator.com/item?id=49856928)).

## Prompt

"Before we go further: research how this codebase already handles similar cases and what constraints
it imposes. Then propose the smallest change that achieves the goal, and say what the first plan did
that this one doesn't need."
