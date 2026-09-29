---
summary: Long AI-written plans and comments bury the decisions that matter; reviewers glaze over, so constrain length and shape of anything a human must read.
tags: [review, writing]
stage: [review, understanding]
links:
  - relates-to: con-understanding-problem
---
# Generated prose is hard to review

Article: "The spec contained more information without creating more clarity … My eyes kept glazing over." ([article](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html)) The author in the thread: the plan "can be detailed and technically correct, but still be
hard to review because the important bits are buried" and it contains "decisions I didn't
explicitly make" ([49850837](https://news.ycombinator.com/item?id=49850837)).

## The same problem in code comments

- wtallis: comments become "a dumping grounds for Claude's stream of consciousness" — history and
  context that is true but doesn't explain *why the code is this way*
  ([49853029](https://news.ycombinator.com/item?id=49853029)).
- meowface does "a big decommenting pass before every PR" ([49854105](https://news.ycombinator.com/item?id=49854105)).
- stingraycharles: once the codebase is cleaned up, new generated code follows the cleaner pattern
  ([49853035](https://news.ycombinator.com/item?id=49853035)).

## Use it

- Ask for decisions and open questions, not narrative. A plan that fits on a screen gets read.
- Ask for the plan as a list of commits or a scaffold in code ([wf-scaffold-then-spike](../workflows/wf-scaffold-then-spike.md)) instead of prose.
- Annotate instead of rewriting: [tool-plannotator](../tools/tool-plannotator.md).
- See [ap-comment-dumping](../anti-patterns/ap-comment-dumping.md).

hdjrudni doesn't read the full generated spec: "the agent is smart enough to highlight the important
tidbits and assumptions. I read those." They care most about architecture and which libraries it
picks ([49860759](https://news.ycombinator.com/item?id=49860759)). Asking for that highlight section is cheap.

Also cited: [49854387](https://news.ycombinator.com/item?id=49854387), [49852894](https://news.ycombinator.com/item?id=49852894), [49854769](https://news.ycombinator.com/item?id=49854769).
