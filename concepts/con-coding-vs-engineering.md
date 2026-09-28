---
id: con-coding-vs-engineering
type: concept
title: Typing code versus owning the software
summary: Most of the second thread concedes that generating code is largely solved and argues about whether the decisions, requirements and long-run judgement around it are; the disagreement is mostly about the word "solved".
tags: [core, judgement]
stage: [intent, understanding]
sources: [49878318, 49879300, 49878597, 49879718, 49878444, 49878717, 49880892, 49878528, 49879868, 49879425, 49879660, 49880323, 49881773, 49878620, 49878506, 49879874, 49879546, 49880358, 49879641, 49878407, 49878826, 49881052]
links:
  - relates-to: con-understanding-problem
  - relates-to: con-underspecification
  - relates-to: con-planning-vs-plan
---
# Typing code versus owning the software

The article's title is answered differently depending on what "coding" means. The pattern across the
thread:

| Position | Who | Caveat raised |
|---|---|---|
| Coding is solved; software engineering isn't | federicobrancas "coding is solved, software engineering not" [49878318](https://news.ycombinator.com/item?id=49878318); jasongi [49879300](https://news.ycombinator.com/item?id=49879300); ben_w: LLMs can write all the code they were paid for in 20 years but not yet the "project planning and self-QA" they did in their first six months on the job, so "Code Monkey" is a dead role but coding and engineering differ [49878597](https://news.ycombinator.com/item?id=49878597); bluegatty: the LLM is "a writer's assistant, who has perfect prose and grammar, but doesn't really write 'stories'" [49879718](https://news.ycombinator.com/item?id=49879718) | flohofwoe: the two are "different words for the same thing", since a spec that removed all engineering decisions would have to be as detailed as the code ([49878444](https://news.ycombinator.com/item?id=49878444)) |
| "Coding in the small" is solved | lordnacho: small, well-understood edits are; "coding in the larger sense is never solved" because decisions keep changing, though the friction of changing them is lower ([49878717](https://news.ycombinator.com/item?id=49878717)) | Models take default decisions for you, and "you might not even realize what it decided" |
| The claim is a motte-and-bailey | argee: the defensible claim is that programmers rarely need to type code by hand, not that design is solved ([49880892](https://news.ycombinator.com/item?id=49880892)) | — |
| Not solved even as coding | vmg12: types and APIs are designed for the immediate goal, not for how the system will evolve ([49878528](https://news.ycombinator.com/item?id=49878528)); bigstrat2003 "LLMs write code worse than humans do" ([49879868](https://news.ycombinator.com/item?id=49879868)) | Contested by the next row |
| Solved in practice since the latest models | Rover222 [49879425](https://news.ycombinator.com/item?id=49879425), temp00345 [49879660](https://news.ycombinator.com/item?id=49879660) | lnkl: "Feels like I read comment similar to this one each year since 2023" ([49880323](https://news.ycombinator.com/item?id=49880323)); CoolestBeans asks whether limitations are being surpassed or just pushed further out ([49881773](https://news.ycombinator.com/item?id=49881773)) |

## Code as a by-product of thinking

hanifbbz: "Code is just a side-effect of reaching clarity" ([49878620](https://news.ycombinator.com/item?id=49878620));
gradus_ad: writing code "is the process of clarifying your own thought and being forced to answer
questions that may not have been obvious before", so an AI's silent assumptions become bugs
([49878506](https://news.ycombinator.com/item?id=49878506)). clickety_clack: coding is like writing; vibe
coding is fast but "I'm not getting the same opportunity to think through the problem"
([49879874](https://news.ycombinator.com/item?id=49879874)). strange_quark: their employer's AI writing
policy is "basically: don't", on the grounds that "writing is thinking"
([49879546](https://news.ycombinator.com/item?id=49879546)). This is the same worry as
[con-planning-vs-plan](con-planning-vs-plan.md) from the other side.

## What the work becomes

- roncesvalles: it is "the art of setting up the program into a shape from which the LLM can reliably
  and efficiently fill up the rest of it", and you "need to be as good of a software engineer as you
  were before" ([49880358](https://news.ycombinator.com/item?id=49880358)).
- ketzo: the new skill is steering agents at the speed they allow "while still keeping enough
  context/understanding to step in when it matters" ([49879641](https://news.ycombinator.com/item?id=49879641)).
- bushido: what is nearer to solved is product development, since fast-and-wrong engineers used to
  iterate to a product people would pay for faster than precise seniors; but the 18-month polish
  phase became 1-4 months, not days ([49878407](https://news.ycombinator.com/item?id=49878407),
  [49878826](https://news.ycombinator.com/item?id=49878826)).
- mstaoru: "it's just a new baseline"; the job becomes combining and instructing tools to produce ever
  more complex outputs, judging the tradeoffs and guiding them, "not that different from pre-AI coding"
  ([49881052](https://news.ycombinator.com/item?id=49881052)).
- jasongi worries about deskilling: the moat moved from "can speak computer" to reading, writing,
  comprehension and judgement ([49879300](https://news.ycombinator.com/item?id=49879300)).

## Use it

When someone says "coding is solved", ask which part: generating a change you can fully specify (widely
reported as working), or deciding what to change and living with it (not reported as solved by anyone
who ships to users long-term). Spend human effort on the second, and on
[keeping your own mental model current](con-understanding-problem.md).

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *relates-to* → [Keeping the human's mental model current](../concepts/con-understanding-problem.md) `con-understanding-problem`
- *relates-to* → [Smarter models still can't read minds](../concepts/con-underspecification.md) `con-underspecification`
- *relates-to* → [Planning is not the plan](../concepts/con-planning-vs-plan.md) `con-planning-vs-plan`

**Backlinks**

- [Article: Coding is NOT solved](../sources/src-article-coding-not-solved.md) `src-article-coding-not-solved` *argues* this
- [HN thread: Coding Is Not Solved](../sources/src-hn-coding-not-solved.md) `src-hn-coding-not-solved` *surfaces* this

**Evidence:** [49878318](https://news.ycombinator.com/item?id=49878318), [49879300](https://news.ycombinator.com/item?id=49879300), [49878597](https://news.ycombinator.com/item?id=49878597), [49879718](https://news.ycombinator.com/item?id=49879718), [49878444](https://news.ycombinator.com/item?id=49878444), [49878717](https://news.ycombinator.com/item?id=49878717), [49880892](https://news.ycombinator.com/item?id=49880892), [49878528](https://news.ycombinator.com/item?id=49878528), [49879868](https://news.ycombinator.com/item?id=49879868), [49879425](https://news.ycombinator.com/item?id=49879425), [49879660](https://news.ycombinator.com/item?id=49879660), [49880323](https://news.ycombinator.com/item?id=49880323), [49881773](https://news.ycombinator.com/item?id=49881773), [49878620](https://news.ycombinator.com/item?id=49878620), [49878506](https://news.ycombinator.com/item?id=49878506), [49879874](https://news.ycombinator.com/item?id=49879874), [49879546](https://news.ycombinator.com/item?id=49879546), [49880358](https://news.ycombinator.com/item?id=49880358), [49879641](https://news.ycombinator.com/item?id=49879641), [49878407](https://news.ycombinator.com/item?id=49878407), [49878826](https://news.ycombinator.com/item?id=49878826), [49881052](https://news.ycombinator.com/item?id=49881052)

<!-- graph:links:end -->
