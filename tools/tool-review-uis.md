---
summary: Tools for commenting on plans and diffs in place — VS Code extension plan annotation, Codex annotations, tuicr and hunk — instead of copy-pasting into chat.
tags: [review, ux]
origin: third-party
stage: [review]
effort: low
links:
  - addresses: con-ai-prose-fatigue
  - alternative-to: tool-plannotator
---
# Annotation and diff-review UIs

- Claude Code VS Code extension: select and annotate plan text (bartread, [49851028](https://news.ycombinator.com/item?id=49851028)).
- Codex annotations (the author, [49851610](https://news.ycombinator.com/item?id=49851610)).
- `tuicr` and `hunk`: terminal review tools estetlinus recommends; they want a chat where you comment
  on code and get replies inline, "a hard UX problem" ([49854075](https://news.ycombinator.com/item?id=49854075)).

Names as given in the thread; not evaluated.

## Update (refresh 2026-09-26)

- crit.md: GitHub-style review of Markdown with agents replying to comments (tomasztomczyk, author,
  [49857455](https://news.ycombinator.com/item?id=49857455)). They use it less for plans now because models "get it" more often.
- anaqin built their own UI on the pi harness: every agent message renders as annotatable Markdown,
  plus GitHub-style code review, so they don't need a question tool ([49857052](https://news.ycombinator.com/item?id=49857052)).
- estetlinus tried a git-tracked plans folder with Hunk and Tuicr: "awkward" ([49855942](https://news.ycombinator.com/item?id=49855942)).
