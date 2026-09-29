---
summary: Run the planning pass over your spec repeatedly, fixing the spec each time, and only implement once a pass finds nothing new.
tags: [spec, quality]
stage: [planning, review]
effort: medium
cost: high
scale: [large]
links:
  - variant-of: wf-adversarial-review
  - addresses: con-underspecification
---
# Re-plan until the spec stops changing

OutOfHere, on Codex: "I keep rerunning plan mode over my updated spec until it stops finding issues.
It is only then that I execute the spec" ([49851367](https://news.ycombinator.com/item?id=49851367)).
LeoPanthera does the same: "If it's asking a lot of questions your spec isn't specified enough"
([49852255](https://news.ycombinator.com/item?id=49852255)).

## Steps

1. Write or update `spec.md`.
2. Fresh session: `Read spec.md. Don't implement. List every ambiguity, contradiction, missing edge case and question, most costly first.`
3. Fix the spec yourself (jacobobryant keeps the spec hand-written and lets the agent only ask
   questions, [49852208](https://news.ycombinator.com/item?id=49852208)).
4. Repeat with a *new* session until the list is empty or trivial.
5. Implement; verify the implementation against the spec (chickensong: drift "can feed back into
   process improvements for future specs", [49854198](https://news.ycombinator.com/item?id=49854198)).

## Cost

Each pass is a full read of the spec and relevant code. Cap it (e.g. three passes) on a budget.
