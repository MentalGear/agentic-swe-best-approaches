---
name: kb-update
description: Update this knowledge base from a source. Use when the user gives a URL (HN thread, blog post, docs page) to mine, or asks to refresh / re-check existing sources for new comments or changes.
---

This repo is a graph of Markdown nodes (see README.md, "How the graph works"). Updating it has a
mechanical half (scripts) and a judgment half (you).

## 1. Capture

- New source: `python3 scripts/ingest.py add <url> [--slug short-name]`
- Existing sources: `python3 scripts/ingest.py refresh [slug ...]` (all when none given)
- `python3 scripts/ingest.py list` shows what's registered.

If TLS fails behind a proxy, set `SSL_CERT_FILE` to the proxy's CA bundle and retry.
The script prints a `delta:` path under `.cache/sources/`. Read that file: for HN it's only the
comments not seen before; for a web page it's a diff (or the full text on first capture).
If the delta is empty, report that and stop.

## 2. Mine the delta

Read all of it before writing anything. For each comment or passage, decide:

- **New workflow, tool, concept or anti-pattern** → new node. Only if it's concrete enough that
  someone could act on it; opinions without a method go into an existing concept's "positions" or
  get skipped.
- **Evidence for an existing node** → add the citation to that node's `sources:` and, if it adds
  something (a step, a caveat, a counter-example), a sentence in the body.
- **Contradiction** → add a "Disputed" section to the node with both sides cited. Never silently
  overwrite an earlier claim.
- **Noise** (jokes, flame, flagged, pure self-promotion) → skip. Product links go in
  `tools/tool-mentioned-unvetted.md` marked "(author)" when the poster built it.

Search existing nodes first (`grep -ril <term> concepts workflows tools anti-patterns`) so you extend
rather than duplicate.

## 3. Write

- First capture of a new source: create `sources/src-<slug>.md` (type `source`) summarising it, and
  set `"node": "src-<slug>"` for that entry in `sources/manifest.json`.
- Node format: copy the frontmatter shape of any existing node. `id` = filename without `.md`; prefix
  `con-`, `wf-`, `tool-`, `ap-`, `src-`. `sources:` takes HN item ids or full URLs.
- Comparison attributes: give new workflows `stage`, `scale`, `effort`, `cost`; new tools `origin`,
  `stage`, `effort`; concepts and anti-patterns `stage`. Allowed values are in `FACETS` in
  `scripts/build_graph.py`. Base ratings on what the source says; they feed the Compare table.
- Links: `  - <relation>: <target-id>` using only relations listed in `INDEX.md` → "Edge vocabulary".
  Give every new node at least one edge, and link it from the source node.
- Attribute every claim to its commenter by username with a link. Quote sparingly and exactly.
- Keep claims as claims: "X reports…", not "X is true". Flag anything you couldn't verify.
- Don't edit anything between the `graph:links` markers; it's generated.

## 4. Rebuild and verify

```
python3 scripts/build_graph.py          # regenerates INDEX.md, graph/, explorer/index.html, Links sections
python3 scripts/build_graph.py --check  # must print ok
```

Fix any dangling link, unknown relation, orphan or manifest error it reports.

## 5. Report

Tell the user: how many new items the delta had, which nodes you created, which you extended, any
disputes you recorded, and what you skipped and why (one line each). Commit with a message naming the
source.
