---
summary: Containers, VMs, DB replicas and read-only users that bound what an agent can break, independent of prompts or modes.
tags: [safety]
origin: practice
stage: [safety]
effort: medium
links:
  - enables: wf-least-privilege-data
  - addresses: con-blast-radius
---
# Sandboxes and read-only credentials

- Docker's sandbox (`sbx`) or similar VM/containers (diegof79, [49851301](https://news.ycombinator.com/item?id=49851301)).
- Read-only DB user or replica as the only credentials in the agent's env (codesnik, [49852669](https://news.ycombinator.com/item?id=49852669)).
- Work on copies of local databases (sfink, [49854052](https://news.ycombinator.com/item?id=49854052)).
- Claude Code's own sandboxing and permission rules; see the docs.

Feathercrown: "It seems unwise not to implement sandbox measures just because the chance of misuse
has gotten lower" ([49850859](https://news.ycombinator.com/item?id=49850859)).
