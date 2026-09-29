---
summary: Strip agent stream-of-consciousness comments before each PR, keeping only comments that explain why; a clean codebase makes future generations cleaner.
tags: [code-quality, review]
stage: [review]
effort: low
cost: low
scale: [small, feature]
links:
  - mitigates: ap-comment-dumping
---
# Decommenting pass before PR

meowface: "I now make sure to do a big decommenting pass before every PR"
([49854105](https://news.ycombinator.com/item?id=49854105)). stingraycharles: typical review notes are "you explain only what but not why", "this is way too much prose", "these comments don’t belong here" and "this is completely redundant as it’s already obvious from the code" — and once the codebase is clean, new generated code follows suit
([49853035](https://news.ycombinator.com/item?id=49853035)).

## Prompt

"Review the comments in this diff. Delete any that restate the code, narrate the change history or
our conversation, or describe what was changed. Keep only comments explaining a non-obvious why.
Don't touch code."

Also put the comment policy in `CLAUDE.md` so it's prevented, not cleaned up. The built-in `/simplify`
skill covers some of this.

Also cited: [49853029](https://news.ycombinator.com/item?id=49853029).
