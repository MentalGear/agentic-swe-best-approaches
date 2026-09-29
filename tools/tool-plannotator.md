---
summary: Web UI for reviewing and annotating agent plans inline, then sending the annotations back; the most-recommended third-party tool in the thread.
tags: [third-party, review]
origin: third-party
stage: [planning, review]
effort: low
links:
  - enables: wf-plan-file-fresh-session
  - addresses: con-ai-prose-fatigue
  - alternative-to: tool-superpowers
---
# Plannotator

<https://plannotator.ai/>

Recommended by esafak, stingraycharles and soleveloper
([49850915](https://news.ycombinator.com/item?id=49850915), [49852329](https://news.ycombinator.com/item?id=49852329),
[49853982](https://news.ycombinator.com/item?id=49853982)). stingraycharles prefers it to heavier
skill packs: "It solves this one problem better, where superpowers tries to do way too much, poorly"
([49852821](https://news.ycombinator.com/item?id=49852821)).

It answers the article's cut-and-paste complaint: you comment on plan lines instead of copying
fragments into new messages.

## Open questions from users

- How to review an arbitrary Markdown file rather than the Claude Code plan file (c_s_guy,
  [49853555](https://news.ycombinator.com/item?id=49853555)) — unanswered in the thread.
- Wanted: change tracking across revisions, persistent comment history, blame across generations
  (soleveloper).

Not evaluated for this knowledge base.

## Update (refresh 2026-09-26)

- Reviewing an arbitrary Markdown file: pass it as a CLI argument, per the
  [quickstart](https://docs.plannotator.ai/open-source/start/quickstart) (itintheory, [49856936](https://news.ycombinator.com/item?id=49856936)).
- Why not just commit plans to git? soleveloper: you'd lose the comments themselves and their link to
  a specific section; they want comments that work like GitHub pull request reviews combined with Google Docs suggestions ([49859686](https://news.ycombinator.com/item?id=49859686)).

Also cited: [49856914](https://news.ycombinator.com/item?id=49856914).
