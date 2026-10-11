---
summary: When the full test suite takes hours, index which tests touch which code and have an agent pick the relevant tests for each change, with full runs and automatic bisecting on a schedule.
tags: [testing, ci, verification]
stage: [review, execution]
effort: high
cost: medium
scale: [large, long-run]
links:
  - applies: con-iterative-loop
  - complements: wf-test-harness-as-plan
---
# Agent-picked tests for slow CI

Context: 01100011 works on widely used software with an 8-hour CI run, which makes splitting changes
into small reviewable pieces impractical ([49853537](https://news.ycombinator.com/item?id=49853537));
t-writescode argues getting CI to ~20 minutes would pay off as much as the AI tooling
([49854493](https://news.ycombinator.com/item?id=49854493)).

gravypod's proposal, a "fast agentic CI" ([49867612](https://news.ycombinator.com/item?id=49867612)):

1. Record code coverage for every test in the full runs.
2. Index it: test name → methods touched.
3. On each commit, an agent reads the diff, predicts which tests exercise the edited code, and runs
   those (or a random subset if there are too many).
4. Every 8 hours, build all submitted patches together and run everything.
5. When a test starts failing, bisect the history automatically and notify the author.

A Bazel-style build that caches test results for unchanged binaries gets some of the same benefit
without an agent.

This is a proposal from the thread, not a reported deployment.
