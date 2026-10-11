---
summary: Forcing all thinking into an up-front spec phase so that going back after implementation starts feels like failure.
tags: [process]
stage: [planning]
links:
  - instance-of: con-iterative-loop
  - relates-to: con-planning-vs-plan
---
# Waterfall front-loading

The article's own failure: Nuanced's `chat → disambiguate → spec → review → revise → approve →
implement → review` flow made users "prematurely 'finish thinking'", and "there was no going back up the waterfall" ([article](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html)). Fr0styMatt88: "'front loading' too much is just the wrong approach"
([49852784](https://news.ycombinator.com/item?id=49852784)).

Fix: plan just enough to start, let the first implementation teach you, and keep the plan editable
during the build ([wf-prototype-as-clay](../workflows/wf-prototype-as-clay.md),
[wf-spike-during-planning](../workflows/wf-spike-during-planning.md)).

## Two traps (2026-09-27)

majormajor sees two opposite failures in startup codebases ([49860885](https://news.ycombinator.com/item?id=49860885)):

1. **"Maybe waterfall works now":** plan mode plus fixing every review-bot nit produces over-engineered
   solutions with thorough edge-case tests but little end-to-end coverage of real user flows.
2. **"Maybe code doesn't matter anymore":** asking for things as needed produces several overlapping
   variants of the same feature, so users can't form one mental model of the product.

Both leave verbose comments, slow low-level tests, and "a plethora of new proper nouns" that make the
docs hard to enter (see [con-domain-language](../concepts/con-domain-language.md)).

Also cited: [49854039](https://news.ycombinator.com/item?id=49854039), [49853061](https://news.ycombinator.com/item?id=49853061).
