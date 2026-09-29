---
summary: Approving a plan and letting the agent run overnight without verification gates, budgets or permission limits.
tags: [safety, cost]
stage: [safety, execution]
links:
  - relates-to: con-blast-radius
  - tension-with: con-iterative-loop
---
# Unbounded "looks good, go"

bfung sees a good plan turning a project into "a 'looks good, go' and run overnight thing"
([49850860](https://news.ycombinator.com/item?id=49850860)). t-writescode asks what that costs per month,
and what happens without "please don't run scary commands on random directories"
([49853314](https://news.ycombinator.com/item?id=49853314)). Small real failures: the agent leaves dev
servers holding port 3000 (the_lonely_phon, [49852598](https://news.ycombinator.com/item?id=49852598));
proposes running unfinished scripts against prod (0xfaded, [49852392](https://news.ycombinator.com/item?id=49852392));
deletes the source after a copy it didn't verify (anarticle, [49853054](https://news.ycombinator.com/item?id=49853054)).

Long runs can work: they need tests that carry the plan ([wf-test-harness-as-plan](../workflows/wf-test-harness-as-plan.md)),
least-privilege credentials ([wf-least-privilege-data](../workflows/wf-least-privilege-data.md)) and a spend cap.

## Later in the thread (refresh 2026-09-26)

hibikir: summaries that don't say when the agent changed direction until much later, bad calls about
where to fix bugs, and acting on questions ([49854923](https://news.ycombinator.com/item?id=49854923)). Ntrails keeps hitting ctrl+c as the model
"flies off doing deep first principles analysis" to find something they already know
([49855453](https://news.ycombinator.com/item?id=49855453)).
