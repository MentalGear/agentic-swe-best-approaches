---
summary: Have the agent write scripts that generate diagrams and tables directly from code or config, so your view of the system can't drift or be hallucinated.
tags: [understanding, verification]
stage: [understanding]
effort: medium
cost: low
scale: [large, long-run]
links:
  - addresses: con-understanding-problem
  - mitigates: ap-trusting-explanations
---
# Scripts that draw the system from code

teekert, after the article convinced them to "double down": find "clarifying abstractions that have a
deterministic relation to the code" ([49854001](https://news.ycombinator.com/item?id=49854001)).
Their examples in a Django project:

- A script that renders the data model to SVG: tables, relations encoded in line ends (1:1, many:1,
  many:many), `on_delete` behaviour as colours. Used in the README and with stakeholders.
- RBAC declared in a TOML file that seeds the DB, plus a script turning it into a Markdown table
  (roles as columns, permissions as rows), also in the README.

biimugan uses the same idea for agent self-checks: after generating an SVG with D2, the agent parses
the XML in Python to check sizes and coordinates before a human looks
([49852844](https://news.ycombinator.com/item?id=49852844)).

avereveard goes further: a frontend records every user message, commit and PR into a graph, and the
agent gets tools to search the *real* reasons behind changes instead of "sloppy self written justifications" ([49854258](https://news.ycombinator.com/item?id=49854258)).

## Steps

1. Pick the structure you most need to trust (schema, permissions, routes, module deps, state machine).
2. Ask the agent for a script, not a diagram. Commit the script; regenerate in CI.
3. Put the output in the README or PR.

This knowledge base does the same for itself: [information-miner](https://github.com/MentalGear/information-miner)
derives the index, backlinks, graph and site from the notes, and checks every quotation against its source.
