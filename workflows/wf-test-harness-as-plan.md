---
summary: Encode the plan as an end-to-end test harness whose failure messages quote the relevant part of the plan, so long unattended runs stay on track.
tags: [testing, long-running, verification]
stage: [execution, review]
effort: high
cost: high
scale: [long-run]
links:
  - applies: con-iterative-loop
  - uses: tool-artifacts
  - complements: wf-explainer-artifacts
  - mitigates: ap-unsupervised-autonomy
---
# End-to-end tests that carry the plan

orisho's workflow for large changes ([49854300](https://news.ycombinator.com/item?id=49854300)):

1. Have the model write an **HTML explainer** of what will be built, with code snippets. It serves as
   the source of truth; models "have no issue using that HTML artifact".
2. Before execution, **interactively build an end-to-end test** that includes pieces of the plan.
   *When a test fails, the relevant part of the plan is in the error message.*
3. Let it run. They report 12h routinely and up to 48h unattended (11h of API time) "with good
   results" — one person's anecdote.
4. At each check-in, have it append current state to the HTML, blog-style (append-only), then
   iterate on the tests and their messages.

## Why it works

The plan lives where the agent looks when it's lost: the failing test. Related practices:
Fr0styMatt88 locks down liked behaviour with tests while prototyping
([49852784](https://news.ycombinator.com/item?id=49852784)); wildzzz builds a test suite at each
milestone ([49852661](https://news.ycombinator.com/item?id=49852661)); frankc: make systems
verifiable and deterministic so agents can write strong property-based tests
([49852511](https://news.ycombinator.com/item?id=49852511)).

## Steps to adopt

- Write assertions with messages like `"Plan §3.2: orders over the limit must be rejected with 422"`.
- Keep the plan sections numbered so messages can cite them.
