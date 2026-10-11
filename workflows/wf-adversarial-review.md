---
summary: Have a fresh session (ideally another model family) attack the plan, explanation or diff before you accept it.
tags: [review, quality]
stage: [review]
effort: medium
cost: high
scale: [feature, large, long-run]
links:
  - critiqued-by: ap-endless-review
  - applies: con-cross-model-review
  - addresses: con-understanding-problem
  - uses: tool-subagents
  - mitigates: ap-trusting-explanations
---
# Adversarial review by a second session

## Variants seen in the thread

| Variant | Who |
|---|---|
| Plan written by one model, reviewed by another model *and* another instance of the same model | senderista [49852685](https://news.ycombinator.com/item?id=49852685) |
| Converse with the default model to aim the plan, then loop with a smarter reviewer "until the plan file is converged" | esafak [49850915](https://news.ycombinator.com/item?id=49850915) |
| Session A (chat) writes a spec + "cover letter"; session B plans; A ratifies or amends; B executes | aaroninsf [49852597](https://news.ycombinator.com/item?id=49852597) |
| Fresh subagent without planning context validates edge cases | spike021 [49853101](https://news.ycombinator.com/item?id=49853101) |
| Different vendor's model for code review | smnscu [49852909](https://news.ycombinator.com/item?id=49852909) |

## Steps

1. Give the reviewer the artifact (plan, diff, explanation) and the project rules — **not** the
   author's conversation.
2. Ask for findings ranked by severity. Nursie gets results as good as elaborate review skills
   "just by asking Claude to review a PR and spit out results in order of severity"
   ([49852894](https://news.ycombinator.com/item?id=49852894)).
3. Feed findings back to the author session or fix yourself; repeat until quiet
   ([wf-spec-until-quiet](wf-spec-until-quiet.md)).

In Claude Code: spawn a subagent for the review so it starts with clean context
([tool-subagents](../tools/tool-subagents.md)); the built-in `/code-review` covers diffs.
Prompt: [templates/prompts/adversarial-review.md](../templates/prompts/adversarial-review.md).

## Cost

aaroninsf: "Lots of tokens!" — but the corrections are consistent enough that they won't skip it.

## Caveat (refresh 2026-09-26)

Reviews don't always converge; one person ran 20–30 sessions that kept finding new faults. Set a stop
rule: see [ap-endless-review](../anti-patterns/ap-endless-review.md).

Also cited: [49854550](https://news.ycombinator.com/item?id=49854550), [49852329](https://news.ycombinator.com/item?id=49852329), [49852532](https://news.ycombinator.com/item?id=49852532), [49855213](https://news.ycombinator.com/item?id=49855213), [49856983](https://news.ycombinator.com/item?id=49856983).
