---
id: wf-drift-proof-docs
type: workflow
title: Current-state code and docs that cannot drift (maintainer-supplied)
summary: Keep code and docs describing only the present, generate every restatable fact from code, and let CI flag prose whose subject changed; history goes to an archive and git.
tags: [docs, verification, maintenance]
stage: [understanding, review]
effort: high
cost: low
scale: [large, long-run]
sources: []
links:
  - relates-to: wf-deterministic-views
  - relates-to: con-understanding-problem
  - relates-to: ap-comment-dumping
  - relates-to: wf-decomment-pass
  - complements: wf-living-spec-dir
  - applies: con-model-tiering
---
# Current-state code and docs that cannot drift

Provenance: supplied by the maintainer of this knowledge base. It is not from either Hacker News thread, has
no commenter evidence, and I have not seen it run on a real project. It is written for a TypeScript-style
codebase (`as const`, `satisfies`, an API extractor); the ideas carry over, the tooling names don't.

## Principles

1. Code and docs describe the present. History lives in an archive and in git, reachable through stable IDs,
   never inline.
2. Every fact has one source. If a doc states it, it exists as a value in code and the doc is rendered from it.
3. Values first, types derived from them. Registries are `as const` data; types come from `typeof` and
   `satisfies`. Generators import the values, so they need no compiler API.
4. Guards before migrations. Add the checks first, then move and rewrite under them. Ratchets make progress
   irreversible.
5. Prose stays human, and change detection catches it going stale.

## Four layers, each linking to the one below

| Layer | Contents | Kept current by |
|---|---|---|
| Code | strong types, API doc comments, short "why now" comments with an ID | the compiler, a history ratchet |
| Reference | public API, config, limits, error codes, protocols, state machines | generation: an API extractor plus doc regions |
| Current docs | README, ARCHITECTURE, threat model, decision records (current text) | handwritten prose with generated regions and markers |
| Archive | reviews, finished research, closed tickets, superseded decisions | moved, never deleted; git is the last archive |

## Mechanisms

- **Public-API report** (api-extractor style), committed. CI fails on any unreviewed change, which also
  enforces naming approval.
- **Generated regions.** `<!-- generated:begin X -->` ... `<!-- generated:end -->` is rewritten from code. CI
  regenerates the regions and fails on any difference, so every structural change shows in the PR's diff.
- **Staleness markers.** A handwritten section declares what it describes: `<!-- describes: id sig:hash -->`.
  The hash covers the semantic signature only. CI flags exactly the sections whose subject changed; `--accept`
  clears a flag after review.
- **ID registry and link check.** Every finding, decision and ticket has an anchor. The check fails on a dead
  link or an unknown ID.
- **History ratchet.** Count history-style comment lines per file (SHAs, dates, "before", "used to"). A file's
  count may only go down.
- **Structural tests.** Each invariant gets a scan that enumerates its domain, for example "only builders
  create frames" or "every frame type is in the table".

## Rollout, one PR per step, merged when green

1. Measure: doc-comment coverage, hand copies of code in the docs, history in comments, broken links, what is
   already data. Report and agree the plan.
2. Guards: the API gate, a conventions doc, the ID registry, the link check and the ratchet.
3. Registries as data; then the generator and its extractors; then `ARCHITECTURE.md` built from them.
4. Archive: move the old material, keeping in place anything tests depend on.
5. Decision records: each states its current text; the amendment trail is archived.
6. Comments, file by file, largest first: each becomes the current reason plus an ID, and the history moves to
   the archive.
7. API doc comments everywhere, then generate the reference from them.
8. Clean-up, then an independent review of the current state.

## Delegation

- Mechanical work (moves, renames, link fixes, counting): the cheapest capable model.
- Implementation and rewrites: a mid-tier model.
- The top model: only for judgement on risky behaviour and security-relevant review.
- The coordinator merges and reports. See [con-model-tiering](../concepts/con-model-tiering.md) and
  [wf-orchestrator-subagents](wf-orchestrator-subagents.md).

## How it fits this knowledge base

It is the docs-side counterpart of [wf-deterministic-views](wf-deterministic-views.md) (generate the picture
from code) and of the generated `Links` sections in this repository, whose `--check` fails on drift. The
history ratchet targets the same clutter as [ap-comment-dumping](../anti-patterns/ap-comment-dumping.md). It
also gives a cheap, trustworthy repo brief for agents that start cold (see the subagent proposals in
[wf-orchestrator-subagents](wf-orchestrator-subagents.md)).

## Limits to weigh

Staleness hashes and the API gate add upkeep and can train people to run `--accept` without reading. The full
programme pays off on large, long-lived codebases; on a small one, start with generated regions and the link
check.

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *relates-to* → [Scripts that draw the system from code](../workflows/wf-deterministic-views.md) `wf-deterministic-views`
- *relates-to* → [Keeping the human's mental model current](../concepts/con-understanding-problem.md) `con-understanding-problem`
- *relates-to* → [Comments as the agent's scratchpad](../anti-patterns/ap-comment-dumping.md) `ap-comment-dumping`
- *relates-to* → [Decommenting pass before PR](../workflows/wf-decomment-pass.md) `wf-decomment-pass`
- *complements* → [Living spec directory and TODO.md](../workflows/wf-living-spec-dir.md) `wf-living-spec-dir`
- *applies* → [Plan with a strong model, build with a cheaper one](../concepts/con-model-tiering.md) `con-model-tiering`

**Backlinks**

- [Parent theorizes, children execute](../workflows/wf-orchestrator-subagents.md) `wf-orchestrator-subagents` *relates-to* this

<!-- graph:links:end -->
