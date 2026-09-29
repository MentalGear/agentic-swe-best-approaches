---
summary: Agree on names for the things in your system before building, so you and the agent mean the same thing and the agent doesn't invent its own terms.
tags: [intent, communication]
stage: [intent]
links:
  - relates-to: con-planning-vs-plan
---
# Fix the vocabulary first

- gwerbin: establish domain language early, "especially with Claude models which otherwise will
  invent their own, and it will be inscrutable" ([49852746](https://news.ycombinator.com/item?id=49852746)).
- Fr0styMatt88, second step of their process: "Figure out the language of your app (what terms you
  want to use for things, what your UI design language will be, etc) and spec that, so you can use words
  consistently with the agent" ([49852784](https://news.ycombinator.com/item?id=49852784)).

This is the Domain-Driven Design "ubiquitous language" idea applied to agent sessions. It's one of
the few pieces of up-front planning that nearly every camp in the thread keeps.

## Use it

Keep a short glossary in `CLAUDE.md` or `docs/glossary.md`: term, one-line meaning, and the names
*not* to use. Update it when the agent invents a synonym. Template section in
[templates/CLAUDE.planning.md](../templates/CLAUDE.planning.md).

majormajor lists "a plethora of new proper nouns all over the place that make the documentation an
ouroboros without a good entry point" among the costs of unguided agent work ([49860885](https://news.ycombinator.com/item?id=49860885)).
