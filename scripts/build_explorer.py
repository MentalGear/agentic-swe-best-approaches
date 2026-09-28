#!/usr/bin/env python3
"""Render the knowledge graph as one self-contained interactive HTML page.

build_graph.py calls render() on every build and writes explorer/index.html, so the page always
matches the notes. Run this script directly to write the page somewhere else:

  python3 scripts/build_explorer.py OUT.html [--fragment]

--fragment omits <!doctype>/<html>/<head>/<body>, for hosts that wrap the page themselves
(Claude artifacts do). Reads graph/graph.json and the node files, so run build_graph.py first.
"""
import json
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_BLOB = "https://github.com/MentalGear/agentic-swe-best-approaches/blob/main/"
BEGIN = "<!-- graph:links:begin"
README_SECTIONS = ["Playbook", "Which workflow when", "Updating from this or other sources", "Caveats"]


def rewrite_links(md, base_dir, ids):
    """Point links at in-page anchors for nodes, and at GitHub for every other repo file."""

    def fix(m):
        text, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(base_dir, path)) if path else ""
        stem = posixpath.splitext(posixpath.basename(resolved))[0]
        if resolved.endswith(".md") and stem in ids:
            return f"[{text}](#{stem})"
        if resolved == "README.md":
            return f"[{text}](#playbook)"
        return f"[{text}]({REPO_BLOB}{resolved}{'#' + anchor if anchor else ''})"

    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", fix, md)


def node_body(text):
    text = text.split(BEGIN)[0]
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    return re.sub(r"^\s*# [^\n]*\n", "", text, count=1).strip()


def readme_sections(readme, ids):
    out = []
    for name in README_SECTIONS:
        m = re.search(rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", readme, re.S | re.M)
        if m:
            out.append({"title": name, "body": rewrite_links(m.group(1).strip(), "", ids)})
    return out


def render(graph, texts, readme, relations, facets=None, fragment=False):
    """graph: the graph.json dict; texts: {node id: raw file text}; relations: {rel: meaning}."""
    ids = {n["id"] for n in graph["nodes"]}
    nodes = []
    for n in graph["nodes"]:
        base = posixpath.dirname(n["path"])
        nodes.append({**n, "body": rewrite_links(node_body(texts[n["id"]]), base, ids)})
    data = {
        "nodes": nodes,
        "edges": graph["edges"],
        "relations": relations,
        "facets": facets or {},
        "readme": readme_sections(readme, ids),
        "repo": REPO_BLOB,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.replace("__DATA__", payload)
    if fragment:
        return page
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + page + "</body>\n</html>\n"
    )


PAGE = r"""<title>Coding Agents Best Practices</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root {
  --bg: #f3f6f5; --surface: #ffffff; --sunk: #e9eeec; --ink: #15201c; --muted: #58685f; --line: #d5ddd9;
  --accent: #0e6f64; --focus: #0e6f64;
  --t-source: #5f6f7f; --t-concept: #4a54c9; --t-workflow: #1d8455; --t-tool: #a86d12; --t-anti-pattern: #bf3b33;
  --display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --read: "Source Serif 4", Georgia, "Times New Roman", serif;
  --mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  --ui: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0e1412; --surface: #151d1a; --sunk: #1b2521; --ink: #e3ebe7; --muted: #97a8a0; --line: #2a3632;
    --accent: #46c4b2; --focus: #46c4b2;
    --t-source: #9aa9b8; --t-concept: #8e96f2; --t-workflow: #53c68e; --t-tool: #e2aa4a; --t-anti-pattern: #f07068;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #0e1412; --surface: #151d1a; --sunk: #1b2521; --ink: #e3ebe7; --muted: #97a8a0; --line: #2a3632;
  --accent: #46c4b2; --focus: #46c4b2;
  --t-source: #9aa9b8; --t-concept: #8e96f2; --t-workflow: #53c68e; --t-tool: #e2aa4a; --t-anti-pattern: #f07068;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.5 var(--ui); padding-inline: 16px; }
.wrap { max-width: 1320px; margin: 0 auto; padding-block: 20px 48px; display: grid; gap: 16px; }
a { color: var(--accent); }
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 4px; }

header.top { display: flex; flex-wrap: wrap; align-items: end; justify-content: space-between; gap: 12px 24px; }
h1 { font: 700 clamp(26px, 4vw, 38px)/1.05 var(--display); letter-spacing: -0.02em; margin: 0; text-wrap: balance; }
.lede { margin: 6px 0 0; color: var(--muted); max-width: 62ch; }
.lede a { color: inherit; }
nav.tabs { display: flex; gap: 4px; background: var(--sunk); padding: 4px; border-radius: 10px; }
nav.tabs button { font: 500 14px var(--ui); color: var(--muted); background: none; border: 0; padding: 7px 14px; border-radius: 7px; cursor: pointer; }
nav.tabs button[aria-selected="true"] { background: var(--surface); color: var(--ink); box-shadow: 0 1px 2px rgb(0 0 0 / .08); }

.explore { display: grid; grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr); gap: 16px; align-items: start; }
@media (max-width: 900px) { .explore { grid-template-columns: 1fr; } }
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; }
.graph-panel { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 12px); display: grid; grid-template-rows: auto 1fr auto; overflow: hidden; }
@media (max-width: 900px) { .graph-panel { position: static; } svg.graph { height: auto; min-height: 0; aspect-ratio: 1000 / 720; } }
.controls { display: flex; flex-wrap: wrap; gap: 8px; padding: 12px; border-bottom: 1px solid var(--line); align-items: center; }
.search { position: relative; flex: 1 1 200px; }
.search input { width: 100%; font: 14px var(--ui); color: var(--ink); background: var(--sunk); border: 1px solid transparent; border-radius: 8px; padding: 8px 10px; }
.search input:focus { border-color: var(--focus); outline: none; }
.results { position: absolute; z-index: 5; left: 0; right: 0; top: calc(100% + 4px); background: var(--surface); border: 1px solid var(--line); border-radius: 8px; margin: 0; padding: 4px; list-style: none; box-shadow: 0 8px 24px rgb(0 0 0 / .12); max-height: 320px; overflow: auto; }
.results li button { display: grid; grid-template-columns: 10px 1fr; gap: 8px; align-items: baseline; width: 100%; text-align: left; background: none; border: 0; padding: 6px 8px; border-radius: 6px; cursor: pointer; color: var(--ink); font: 14px var(--ui); }
.results li button:hover, .results li button.active { background: var(--sunk); }
.results small { display: block; color: var(--muted); font-size: 12px; }
.dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; background: var(--c); flex: none; }
.filters { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { display: inline-flex; align-items: center; gap: 6px; font: 500 12px var(--ui); letter-spacing: .02em; color: var(--ink); background: var(--sunk); border: 1px solid var(--line); border-radius: 999px; padding: 4px 10px; cursor: pointer; }
.chip[aria-pressed="false"] { opacity: .45; }
.chip[aria-pressed="false"] .dot { background: transparent; box-shadow: inset 0 0 0 1.5px var(--c); }
svg.graph { width: 100%; height: min(68vh, 640px); min-height: 380px; display: block; cursor: grab; touch-action: none; }
svg.graph:active { cursor: grabbing; }
.graph .edge { stroke: var(--line); stroke-width: 1; fill: none; }
.graph .edge.hot { stroke: var(--muted); stroke-width: 1.6; }
.graph .node circle { stroke: var(--surface); stroke-width: 1.5; cursor: pointer; }
.graph .node.sel circle { stroke: var(--ink); stroke-width: 2.5; }
.graph .node text { font: 500 11px var(--ui); fill: var(--ink); paint-order: stroke; stroke: var(--surface); stroke-width: 3px; pointer-events: none; }
.graph .elabel { font: 10px var(--mono); fill: var(--muted); paint-order: stroke; stroke: var(--surface); stroke-width: 3px; pointer-events: none; }
.graph .dim { opacity: .3; }
.graph .edge.dim { opacity: .45; }
.hint { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 4px 12px; font-size: 12px; color: var(--muted); padding: 8px 12px; border-top: 1px solid var(--line); }
.hint button { font: inherit; color: var(--accent); background: none; border: 0; padding: 0; cursor: pointer; text-decoration: underline; }

.detail { padding: 20px 22px 24px; min-width: 0; }
.kind { display: inline-flex; align-items: center; gap: 6px; font: 600 11px var(--ui); text-transform: uppercase; letter-spacing: .08em; color: var(--c); }
.detail h2 { font: 700 26px/1.15 var(--display); letter-spacing: -0.01em; margin: 6px 0 6px; text-wrap: balance; }
.detail .summary { font: 17px/1.5 var(--read); color: var(--ink); margin: 0 0 10px; }
.meta { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; font-size: 12px; color: var(--muted); margin-bottom: 14px; }
.meta code { font: 12px var(--mono); background: var(--sunk); padding: 2px 6px; border-radius: 4px; color: var(--ink); }
.tag { font: 12px var(--ui); color: var(--muted); }
.md { font: 16px/1.6 var(--read); max-width: 68ch; overflow-wrap: anywhere; }
.md h1, .md h2, .md h3 { font: 700 18px/1.3 var(--display); margin: 1.4em 0 .4em; }
.md p, .md ul, .md ol, .md blockquote, .md table, .md pre { margin: 0 0 .9em; }
.md ul, .md ol { padding-left: 1.3em; }
.md li { margin: .2em 0; }
.md blockquote { border-left: 3px solid var(--line); padding: .1em 0 .1em 1em; color: var(--muted); }
.md code { font: .86em var(--mono); background: var(--sunk); padding: .1em .35em; border-radius: 4px; }
.md pre { background: var(--sunk); padding: 12px; border-radius: 8px; overflow-x: auto; }
.md pre code { background: none; padding: 0; }
.md .tbl { overflow-x: auto; margin: 0 0 1em; }
.md table { border-collapse: collapse; font: 14px/1.45 var(--ui); width: 100%; }
.md th, .md td { text-align: left; vertical-align: top; padding: 6px 10px 6px 0; border-bottom: 1px solid var(--line); }
.md th { font-weight: 600; color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .05em; }
.md a[href^="#"] { text-decoration-style: dotted; text-underline-offset: 3px; }
.links { margin-top: 22px; border-top: 1px solid var(--line); padding-top: 14px; display: grid; gap: 14px; }
.links h3 { font: 600 11px var(--ui); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin: 0 0 6px; }
.linklist { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; }
.linklist li { display: grid; grid-template-columns: 7.5em 10px 1fr; gap: 8px; align-items: baseline; font-size: 14px; }
.linklist .rel { font: 12px var(--mono); color: var(--muted); text-align: right; }
.linklist a { color: var(--ink); text-decoration: none; }
.linklist a:hover { text-decoration: underline; color: var(--accent); }
.evidence { display: flex; flex-wrap: wrap; gap: 6px; }
.evidence a { font: 12px var(--mono); color: var(--muted); background: var(--sunk); border-radius: 4px; padding: 2px 7px; text-decoration: none; }
.evidence a:hover { color: var(--accent); }

.page { padding: 24px clamp(16px, 4vw, 40px) 32px; }
.page section + section { margin-top: 28px; padding-top: 24px; border-top: 1px solid var(--line); }
.page h2 { font: 700 22px/1.2 var(--display); margin: 0 0 12px; }
.stats { display: flex; flex-wrap: wrap; gap: 8px 20px; margin: 0 0 4px; padding: 0; list-style: none; font-size: 14px; color: var(--muted); }
.stats b { font: 600 15px var(--ui); color: var(--ink); font-variant-numeric: tabular-nums; }
.filterbar { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; align-items: center; }
.filterbar input { flex: 1 1 240px; font: 14px var(--ui); color: var(--ink); background: var(--sunk); border: 1px solid transparent; border-radius: 8px; padding: 8px 10px; }
.filterbar input:focus { border-color: var(--focus); outline: none; }
.catalog { display: grid; gap: 24px; }
.catalog h3 { display: flex; align-items: center; gap: 8px; font: 600 12px var(--ui); text-transform: uppercase; letter-spacing: .08em; color: var(--c); margin: 0 0 8px; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 8px; }
.card { display: grid; gap: 4px; text-align: left; font: inherit; color: var(--ink); background: var(--sunk); border: 1px solid transparent; border-radius: 10px; padding: 12px 14px; cursor: pointer; }
.card:hover { border-color: var(--c); }
.card b { font: 600 15px/1.3 var(--display); }
.card span { font-size: 13px; color: var(--muted); }
.card small { font: 11px var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.empty { color: var(--muted); font-style: italic; }
footer { font-size: 12px; color: var(--muted); }

.cmp { display: grid; gap: 14px; }
.cmp-head { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.cmp-head input { flex: 1 1 240px; font: 14px var(--ui); color: var(--ink); background: var(--sunk); border: 1px solid transparent; border-radius: 8px; padding: 8px 10px; }
.cmp-head input:focus { border-color: var(--focus); outline: none; }
.seg { display: flex; flex-wrap: wrap; gap: 4px; background: var(--sunk); padding: 4px; border-radius: 10px; }
.seg button { font: 500 13px var(--ui); color: var(--muted); background: none; border: 0; padding: 6px 12px; border-radius: 7px; cursor: pointer; display: inline-flex; gap: 6px; align-items: center; }
.seg button[aria-checked="true"] { background: var(--surface); color: var(--ink); box-shadow: 0 1px 2px rgb(0 0 0 / .08); }
.seg small { font: 11px var(--mono); color: var(--muted); }
.facets { display: grid; gap: 8px; }
.fgroup { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.fgroup > span { font: 600 11px var(--ui); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); min-width: 6.5em; }
.fchip { font: 500 12px var(--ui); color: var(--ink); background: var(--surface); border: 1px solid var(--line); border-radius: 999px; padding: 3px 10px; cursor: pointer; }
.fchip[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: var(--surface); }
.fchip small { font: 11px var(--mono); opacity: .7; margin-left: 4px; }
.cmp-bar { display: flex; flex-wrap: wrap; gap: 8px 18px; align-items: center; font-size: 13px; color: var(--muted); }
.cmp-bar .only { display: inline-flex; gap: 6px; align-items: center; cursor: pointer; }
.linkbtn { font: inherit; color: var(--accent); background: none; border: 0; padding: 0; cursor: pointer; text-decoration: underline; }
.tablewrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 10px; }
.cmp-table { border-collapse: collapse; width: 100%; min-width: 880px; font-size: 13px; }
.cmp-table th, .cmp-table td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--line); }
.cmp-table tbody tr:last-child td { border-bottom: 0; }
.cmp-table thead th { position: sticky; top: 0; background: var(--sunk); font: 600 11px var(--ui); text-transform: uppercase; letter-spacing: .06em; color: var(--muted); white-space: nowrap; }
.cmp-table th button { font: inherit; color: inherit; text-transform: inherit; letter-spacing: inherit; background: none; border: 0; padding: 0; cursor: pointer; display: inline-flex; gap: 4px; align-items: center; }
.cmp-table th button[data-dir]::after { content: attr(data-dir); color: var(--accent); }
.cmp-table tbody tr:hover { background: color-mix(in srgb, var(--sunk) 60%, transparent); }
.cmp-table tr.checked { background: color-mix(in srgb, var(--accent) 9%, transparent); }
.cmp-table .name { min-width: 230px; max-width: 340px; }
.cmp-table .name a { font: 600 14px/1.3 var(--display); color: var(--ink); text-decoration: none; display: inline-flex; gap: 7px; align-items: baseline; }
.cmp-table .name a:hover { color: var(--accent); }
.cmp-table .name p { margin: 3px 0 0 17px; color: var(--muted); font-size: 12.5px; line-height: 1.4; }
.pill { display: inline-block; font: 11px var(--ui); color: var(--ink); background: var(--sunk); border-radius: 4px; padding: 1px 6px; margin: 0 3px 3px 0; white-space: nowrap; }
.level { display: inline-flex; gap: 2px; vertical-align: middle; margin-right: 6px; }
.level i { width: 7px; height: 12px; border-radius: 2px; background: var(--line); }
.level i.on { background: var(--c, var(--accent)); }
.lvl { white-space: nowrap; }
.rels { min-width: 180px; max-width: 280px; }
.rels a { color: var(--ink); text-decoration: none; border-bottom: 1px dotted var(--muted); }
.rels a:hover { color: var(--accent); }
.num { font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap; }
.bar { display: inline-block; height: 6px; border-radius: 3px; background: var(--accent); opacity: .55; vertical-align: middle; margin-left: 6px; }
.dash { color: var(--muted); }
.note { font-size: 12px; color: var(--muted); margin: 0; }
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
</style>

<div class="wrap">
  <header class="top">
    <div>
      <h1>Coding Agents Best Practices</h1>
      <p class="lede">How practitioners plan with coding agents now: workflows, tools and pitfalls mined from
        <a href="https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html">“Plan mode is dead”</a>
        and <a href="https://news.ycombinator.com/item?id=49840054">its Hacker News thread</a>, linked as a graph. Every claim cites its comment.</p>
    </div>
    <nav class="tabs" role="tablist" aria-label="Views">
      <button role="tab" id="tab-explore" aria-controls="view-explore">Explore</button>
      <button role="tab" id="tab-compare" aria-controls="view-compare">Compare</button>
      <button role="tab" id="tab-playbook" aria-controls="view-playbook">Playbook</button>
      <button role="tab" id="tab-nodes" aria-controls="view-nodes">All notes</button>
    </nav>
  </header>

  <main>
    <div id="view-explore" role="tabpanel" aria-labelledby="tab-explore" class="explore">
      <div class="panel graph-panel">
        <div class="controls">
          <div class="search">
            <input id="q" type="search" placeholder="Search notes…" autocomplete="off" aria-label="Search notes" aria-controls="results">
            <ul id="results" class="results" hidden></ul>
          </div>
          <div class="filters" id="filters" aria-label="Show note types"></div>
        </div>
        <svg class="graph" id="graph" role="img" aria-label="Knowledge graph. Select a node to read it."></svg>
        <div class="hint"><span>Click a node to read it. Drag to pan, scroll or pinch to zoom.</span><button id="reset" type="button">Reset view</button></div>
      </div>
      <article class="panel detail" id="detail" aria-live="polite"></article>
    </div>

    <div id="view-compare" role="tabpanel" aria-labelledby="tab-compare" class="panel page cmp" hidden>
      <div class="cmp-head">
        <div class="seg" id="cmp-type" role="radiogroup" aria-label="What to compare"></div>
        <input id="cq" type="search" placeholder="Search names, summaries, tags" aria-label="Search the table">
      </div>
      <div class="facets" id="cmp-facets"></div>
      <div class="cmp-bar">
        <span id="cmp-count" aria-live="polite"></span>
        <label class="only"><input type="checkbox" id="cmp-only"> Show only checked rows</label>
        <button type="button" class="linkbtn" id="cmp-clear">Clear filters</button>
      </div>
      <div class="tablewrap"><table class="cmp-table" id="cmp-table"></table></div>
      <p class="note">Stage, task size, effort and token cost are editorial ratings drawn from the thread, not measurements. Evidence counts the comments and pages each note cites.</p>
    </div>

    <div id="view-playbook" role="tabpanel" aria-labelledby="tab-playbook" class="panel page" hidden></div>

    <div id="view-nodes" role="tabpanel" aria-labelledby="tab-nodes" class="panel page" hidden>
      <div class="filterbar">
        <input id="nq" type="search" placeholder="Filter by title, summary or tag" aria-label="Filter notes">
        <ul class="stats" id="stats"></ul>
      </div>
      <div class="catalog" id="catalog"></div>
    </div>
  </main>

  <footer>Generated from the repository by <code>scripts/build_graph.py</code>. Source notes:
    <a href="https://github.com/MentalGear/agentic-swe-best-approaches">MentalGear/agentic-swe-best-approaches</a>.</footer>
</div>

<script type="application/json" id="kb-data">__DATA__</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
(() => {
  const DATA = JSON.parse(document.getElementById("kb-data").textContent);
  const TYPES = [
    ["source", "Sources"], ["concept", "Concepts"], ["workflow", "Workflows"],
    ["tool", "Tools"], ["anti-pattern", "Anti-patterns"],
  ];
  const TYPE_LABEL = Object.fromEntries(TYPES);
  const SINGULAR = { source: "Source", concept: "Concept", workflow: "Workflow", tool: "Tool", "anti-pattern": "Anti-pattern" };
  const color = t => `var(--t-${t})`;
  const byId = new Map(DATA.nodes.map(n => [n.id, n]));
  const out = new Map(), inc = new Map();
  for (const n of DATA.nodes) { out.set(n.id, []); inc.set(n.id, []); }
  for (const e of DATA.edges) { out.get(e.from).push(e); inc.get(e.to).push(e); }
  const degree = id => out.get(id).length + inc.get(id).length;
  const DEFAULT = byId.has("con-plan-mode-is-a-prompt") ? "con-plan-mode-is-a-prompt" : DATA.nodes[0].id;
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const md = src => {
    const html = window.marked ? marked.parse(src, { mangle: false, headerIds: false }) : `<pre>${esc(src)}</pre>`;
    const box = document.createElement("div");
    box.innerHTML = html;
    box.querySelectorAll("table").forEach(t => { const w = document.createElement("div"); w.className = "tbl"; t.replaceWith(w); w.appendChild(t); });
    box.querySelectorAll('a[href^="http"]').forEach(a => { a.target = "_blank"; a.rel = "noopener"; });
    return box.innerHTML;
  };

  // ---------- tabs & routing ----------
  const views = { explore: "view-explore", compare: "view-compare", playbook: "view-playbook", nodes: "view-nodes" };
  let current = DEFAULT;
  function showTab(name) {
    for (const [k, id] of Object.entries(views)) {
      document.getElementById(id).hidden = k !== name;
      document.getElementById("tab-" + k).setAttribute("aria-selected", String(k === name));
    }
  }
  function route() {
    const h = decodeURIComponent(location.hash.slice(1));
    if (h === "playbook" || h === "nodes" || h === "compare") { showTab(h); return; }
    showTab("explore");
    select(byId.has(h) ? h : current, false);
  }
  for (const k of Object.keys(views)) {
    document.getElementById("tab-" + k).addEventListener("click", () => {
      if (k === "explore") location.hash = current; else location.hash = k;
    });
  }

  // ---------- detail ----------
  const detail = document.getElementById("detail");
  function linkItem(e, otherId, dir) {
    const o = byId.get(otherId);
    const rel = dir === "out" ? e.rel : e.rel;
    return `<li style="--c:${color(o.type)}"><span class="rel" title="${esc(DATA.relations[e.rel] || "")}">${esc(rel)}</span><span class="dot"></span><a href="#${o.id}">${esc(o.title)}</a></li>`;
  }
  function renderDetail(id) {
    const n = byId.get(id);
    const o = out.get(id), i = inc.get(id);
    const ev = (n.sources || []).map(u => {
      const m = u.match(/item\?id=(\d+)/);
      const label = m ? "HN " + m[1] : u.replace(/^https?:\/\/(www\.)?/, "").slice(0, 40);
      return `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(label)}</a>`;
    }).join("");
    detail.style.setProperty("--c", color(n.type));
    detail.innerHTML = `
      <span class="kind"><span class="dot"></span>${SINGULAR[n.type]}</span>
      <h2>${esc(n.title)}</h2>
      <p class="summary">${esc(n.summary)}</p>
      <div class="meta"><code>${esc(n.id)}</code>${(n.tags || []).map(t => `<span class="tag">#${esc(t)}</span>`).join("")}
        <a href="${esc(DATA.repo + n.path)}" target="_blank" rel="noopener">Source file</a></div>
      <div class="md">${md(n.body)}</div>
      <div class="links">
        ${o.length ? `<div><h3>Links out</h3><ul class="linklist">${o.map(e => linkItem(e, e.to, "out")).join("")}</ul></div>` : ""}
        ${i.length ? `<div><h3>Linked from</h3><ul class="linklist">${i.map(e => linkItem(e, e.from, "in")).join("")}</ul></div>` : ""}
        ${ev ? `<div><h3>Evidence</h3><div class="evidence">${ev}</div></div>` : ""}
      </div>`;
  }

  // ---------- graph (optional: everything else works without d3) ----------
  let edgeSel = null, elabelSel = null, nodeSel = null, labelSel = null, fit = () => {};
  if (window.d3) {
    const svg = d3.select("#graph");
    const W = 1000, H = 720;
    svg.attr("viewBox", `0 0 ${W} ${H}`).attr("preserveAspectRatio", "xMidYMid meet");
    const root = svg.append("g");
    const col = { source: 0.1, concept: 0.36, workflow: 0.58, tool: 0.82, "anti-pattern": 0.4 };
    const row = { source: 0.5, concept: 0.42, workflow: 0.5, tool: 0.5, "anti-pattern": 0.86 };
    const nodes = DATA.nodes.map(n => ({ id: n.id, type: n.type, title: n.title, r: 5 + Math.sqrt(degree(n.id)) * 2.4 }));
    const links = DATA.edges.map(e => ({ source: e.from, target: e.to, rel: e.rel }));
    const sim = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(70).strength(0.25))
      .force("charge", d3.forceManyBody().strength(-260))
      .force("x", d3.forceX(d => col[d.type] * W).strength(0.12))
      .force("y", d3.forceY(d => row[d.type] * H).strength(0.08))
      .force("collide", d3.forceCollide(d => d.r + 6))
      .stop();
    for (let k = 0; k < 400; k++) sim.tick();

    edgeSel = root.append("g").selectAll("line").data(links).join("line").attr("class", "edge")
      .attr("x1", d => d.source.x).attr("y1", d => d.source.y).attr("x2", d => d.target.x).attr("y2", d => d.target.y);
    elabelSel = root.append("g").selectAll("text").data(links).join("text").attr("class", "elabel").attr("text-anchor", "middle")
      .attr("x", d => (d.source.x + d.target.x) / 2).attr("y", d => (d.source.y + d.target.y) / 2 - 3).text(d => d.rel).attr("display", "none");
    nodeSel = root.append("g").selectAll("g").data(nodes).join("g").attr("class", "node")
      .attr("transform", d => `translate(${d.x},${d.y})`)
      .attr("tabindex", 0).attr("role", "button").attr("aria-label", d => `${SINGULAR[d.type]}: ${d.title}`)
      .on("click", (ev, d) => { location.hash = d.id; })
      .on("keydown", (ev, d) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); location.hash = d.id; } })
      .on("mouseenter", (ev, d) => highlight(d.id, true))
      .on("mouseleave", () => highlight(current, false));
    nodeSel.append("circle").attr("r", d => d.r).style("fill", d => color(d.type));
    nodeSel.append("title").text(d => d.title);
    const short = t => t.length > 30 ? t.slice(0, 28) + "…" : t;
    labelSel = nodeSel.append("text").attr("dy", d => -d.r - 4).attr("text-anchor", "middle").text(d => short(d.title));

    const zoom = d3.zoom().scaleExtent([0.4, 4]).on("zoom", ev => root.attr("transform", ev.transform));
    svg.call(zoom);
    fit = function () {
      const xs = nodes.map(n => n.x), ys = nodes.map(n => n.y), pad = 30;
      const x0 = Math.min(...xs) - pad, x1 = Math.max(...xs) + pad, y0 = Math.min(...ys) - pad, y1 = Math.max(...ys) + pad;
      const s = Math.min(W / (x1 - x0), H / (y1 - y0), 2.2);
      svg.call(zoom.transform, d3.zoomIdentity.translate(W / 2 - s * (x0 + x1) / 2, H / 2 - s * (y0 + y1) / 2).scale(s));
    };
  } else {
    document.getElementById("graph").outerHTML = '<p class="empty" style="padding:24px">The map needs the d3 library, which could not load. Search, notes, Compare and the other tabs still work.</p>';
  }
  document.getElementById("reset").addEventListener("click", () => fit());

  let hiddenTypes = new Set(), searchHits = null;
  function highlight(id, hover) {
    if (!nodeSel) return;
    const nb = new Set([id]);
    for (const e of out.get(id)) nb.add(e.to);
    for (const e of inc.get(id)) nb.add(e.from);
    const touches = l => l.source.id === id || l.target.id === id;
    nodeSel.classed("sel", d => d.id === current)
      .classed("dim", d => searchHits ? !searchHits.has(d.id) : !nb.has(d.id))
      .attr("display", d => hiddenTypes.has(d.type) ? "none" : null);
    labelSel.attr("display", d => (nb.has(d.id) || degree(d.id) >= 9 || (searchHits && searchHits.has(d.id))) ? null : "none");
    edgeSel.classed("hot", touches).classed("dim", l => searchHits ? true : !touches(l))
      .attr("display", l => hiddenTypes.has(l.source.type) || hiddenTypes.has(l.target.type) ? "none" : null);
    elabelSel.attr("display", l => touches(l) && !hiddenTypes.has(l.source.type) && !hiddenTypes.has(l.target.type) && !searchHits ? null : "none");
  }
  function select(id, push = true) {
    if (!byId.has(id)) return;
    current = id;
    if (hiddenTypes.has(byId.get(id).type)) { hiddenTypes.delete(byId.get(id).type); syncFilters(); }
    renderDetail(id);
    highlight(id, false);
    if (push && location.hash.slice(1) !== id) location.hash = id;
  }

  // ---------- filters ----------
  const filters = document.getElementById("filters");
  filters.innerHTML = TYPES.map(([t, label]) =>
    `<button type="button" class="chip" data-type="${t}" aria-pressed="true" style="--c:${color(t)}"><span class="dot"></span>${label}</button>`).join("");
  function syncFilters() { filters.querySelectorAll(".chip").forEach(b => b.setAttribute("aria-pressed", String(!hiddenTypes.has(b.dataset.type)))); }
  filters.addEventListener("click", ev => {
    const b = ev.target.closest(".chip"); if (!b) return;
    const t = b.dataset.type;
    hiddenTypes.has(t) ? hiddenTypes.delete(t) : hiddenTypes.add(t);
    syncFilters(); highlight(current, false);
  });

  // ---------- search ----------
  const q = document.getElementById("q"), results = document.getElementById("results");
  const hay = n => (n.title + " " + n.summary + " " + (n.tags || []).join(" ") + " " + n.id + " " + n.body).toLowerCase();
  const index = DATA.nodes.map(n => [n, hay(n)]);
  function find(term) {
    const words = term.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return index.filter(([, h]) => words.every(w => h.includes(w)))
      .map(([n]) => n)
      .sort((a, b) => (b.title.toLowerCase().includes(words[0]) - a.title.toLowerCase().includes(words[0])) || degree(b.id) - degree(a.id));
  }
  let active = 0, hits = [];
  function drawResults() {
    if (!hits.length) { results.innerHTML = q.value.trim() ? `<li class="empty" style="padding:6px 8px">No notes match “${esc(q.value.trim())}”.</li>` : ""; results.hidden = !q.value.trim(); return; }
    results.hidden = false;
    results.innerHTML = hits.slice(0, 10).map((n, k) =>
      `<li><button type="button" data-id="${n.id}" class="${k === active ? "active" : ""}" style="--c:${color(n.type)}"><span class="dot"></span><span>${esc(n.title)}<small>${esc(SINGULAR[n.type])} · ${esc(n.summary.slice(0, 90))}${n.summary.length > 90 ? "…" : ""}</small></span></button></li>`).join("");
  }
  q.addEventListener("input", () => {
    hits = find(q.value); active = 0;
    searchHits = q.value.trim() ? new Set(hits.map(n => n.id)) : null;
    drawResults(); highlight(current, false);
  });
  q.addEventListener("keydown", ev => {
    if (ev.key === "ArrowDown") { active = Math.min(active + 1, Math.min(hits.length, 10) - 1); drawResults(); ev.preventDefault(); }
    else if (ev.key === "ArrowUp") { active = Math.max(active - 1, 0); drawResults(); ev.preventDefault(); }
    else if (ev.key === "Enter" && hits[active]) { pick(hits[active].id); }
    else if (ev.key === "Escape") { clearSearch(); }
  });
  results.addEventListener("click", ev => { const b = ev.target.closest("button[data-id]"); if (b) pick(b.dataset.id); });
  function clearSearch() { q.value = ""; hits = []; searchHits = null; results.hidden = true; highlight(current, false); }
  function pick(id) { clearSearch(); location.hash = id; }
  document.addEventListener("click", ev => { if (!ev.target.closest(".search")) results.hidden = true; });

  // ---------- playbook ----------
  const counts = Object.fromEntries(TYPES.map(([t]) => [t, DATA.nodes.filter(n => n.type === t).length]));
  document.getElementById("view-playbook").innerHTML = DATA.readme.map(s =>
    `<section><h2>${esc(s.title)}</h2><div class="md">${md(s.body)}</div></section>`).join("");

  // ---------- catalog ----------
  const stats = document.getElementById("stats");
  stats.innerHTML = TYPES.map(([t, l]) => `<li><b>${counts[t]}</b> ${l.toLowerCase()}</li>`).join("") + `<li><b>${DATA.edges.length}</b> links</li>`;
  const catalog = document.getElementById("catalog"), nq = document.getElementById("nq");
  function drawCatalog() {
    const term = nq.value.trim();
    const allowed = term ? new Set(find(term).map(n => n.id)) : null;
    const html = TYPES.map(([t, label]) => {
      const list = DATA.nodes.filter(n => n.type === t && (!allowed || allowed.has(n.id))).sort((a, b) => a.title.localeCompare(b.title));
      if (!list.length) return "";
      return `<section style="--c:${color(t)}"><h3><span class="dot"></span>${label} <span style="color:var(--muted)">${list.length}</span></h3><div class="cards">${
        list.map(n => `<button type="button" class="card" data-id="${n.id}"><b>${esc(n.title)}</b><span>${esc(n.summary)}</span><small>${out.get(n.id).length} out · ${inc.get(n.id).length} in · ${(n.sources || []).length} citations</small></button>`).join("")
      }</div></section>`;
    }).join("");
    catalog.innerHTML = html || `<p class="empty">No notes match “${esc(term)}”.</p>`;
  }
  nq.addEventListener("input", drawCatalog);
  catalog.addEventListener("click", ev => { const b = ev.target.closest(".card"); if (b) location.hash = b.dataset.id; });
  drawCatalog();

  // ---------- compare ----------
  const FAC = DATA.facets;
  const LEVEL = { low: 1, medium: 2, high: 3 };
  const CMP_TYPES = [
    ["workflow", "Workflows", ["stage", "scale", "effort", "cost"], "Addresses", ["addresses", "applies", "mitigates"], ["concept", "anti-pattern"]],
    ["tool", "Tools", ["origin", "stage", "effort"], "Supports", ["enables", "instance-of", "addresses", "alternative-to"], ["workflow", "concept", "tool"]],
    ["anti-pattern", "Anti-patterns", ["stage"], "Fixed by", null, null],
    ["concept", "Concepts", ["stage"], "Put into practice by", null, null],
  ];
  const cmp = { type: "workflow", q: "", only: false, checked: new Set(), filters: {}, sort: { key: "name", dir: 1 } };
  const vals = (n, k) => { const v = n[k]; return v == null ? [] : Array.isArray(v) ? v : [v]; };
  function related(n, spec) {
    const [t, , , , rels, types] = spec;
    if (t === "anti-pattern") return inc.get(n.id).filter(e => e.rel === "mitigates").map(e => e.from);
    if (t === "concept") return inc.get(n.id).filter(e => ["applies", "addresses"].includes(e.rel) && byId.get(e.from).type === "workflow").map(e => e.from);
    return out.get(n.id).filter(e => rels.includes(e.rel) && types.includes(byId.get(e.to).type)).map(e => e.to);
  }
  const toolsUsed = n => out.get(n.id).filter(e => e.rel === "uses").map(e => e.to)
    .concat(inc.get(n.id).filter(e => e.rel === "enables" && byId.get(e.from).type === "tool").map(e => e.from))
    .filter((v, i, a) => a.indexOf(v) === i);
  const spec = () => CMP_TYPES.find(c => c[0] === cmp.type);

  const seg = document.getElementById("cmp-type");
  seg.innerHTML = CMP_TYPES.map(([t, label]) =>
    `<button type="button" role="radio" data-t="${t}" style="--c:${color(t)}"><span class="dot"></span>${label} <small>${counts[t]}</small></button>`).join("");
  seg.addEventListener("click", ev => {
    const b = ev.target.closest("button[data-t]"); if (!b) return;
    cmp.type = b.dataset.t; cmp.filters = {}; cmp.checked.clear(); cmp.only = false;
    cmp.sort = { key: "name", dir: 1 }; drawCompare();
  });
  const facetBox = document.getElementById("cmp-facets");
  facetBox.addEventListener("click", ev => {
    const b = ev.target.closest(".fchip"); if (!b) return;
    const set = cmp.filters[b.dataset.k] || (cmp.filters[b.dataset.k] = new Set());
    set.has(b.dataset.v) ? set.delete(b.dataset.v) : set.add(b.dataset.v);
    drawCompare();
  });
  const cq = document.getElementById("cq");
  cq.addEventListener("input", () => { cmp.q = cq.value; drawCompare(); });
  const onlyBox = document.getElementById("cmp-only");
  onlyBox.addEventListener("change", () => { cmp.only = onlyBox.checked; drawCompare(); });
  document.getElementById("cmp-clear").addEventListener("click", () => {
    cmp.filters = {}; cmp.q = ""; cq.value = ""; cmp.only = false; drawCompare();
  });
  const table = document.getElementById("cmp-table");
  table.addEventListener("click", ev => {
    const h = ev.target.closest("th button[data-sort]");
    if (h) { const k = h.dataset.sort; cmp.sort = { key: k, dir: cmp.sort.key === k ? -cmp.sort.dir : (k === "name" ? 1 : -1) }; drawCompare(); }
  });
  table.addEventListener("change", ev => {
    const c = ev.target.closest("input[data-id]"); if (!c) return;
    c.checked ? cmp.checked.add(c.dataset.id) : cmp.checked.delete(c.dataset.id);
    drawCompare();
  });

  const level = (v, t) => v ? `<span class="lvl"><span class="level" aria-hidden="true">${[1, 2, 3].map(k => `<i class="${k <= LEVEL[v] ? "on" : ""}"></i>`).join("")}</span>${v}</span>` : `<span class="dash">—</span>`;
  const pills = arr => arr.length ? arr.map(v => `<span class="pill">${esc(v)}</span>`).join("") : `<span class="dash">—</span>`;
  const refs = ids => ids.length ? ids.map(id => `<a href="#${id}">${esc(byId.get(id).title)}</a>`).join(", ") : `<span class="dash">—</span>`;

  function drawCompare() {
    const sp = spec(), [t, , keys, relLabel] = sp;
    seg.querySelectorAll("button").forEach(b => b.setAttribute("aria-checked", String(b.dataset.t === t)));
    onlyBox.checked = cmp.only;
    const pool = DATA.nodes.filter(n => n.type === t);
    const words = cmp.q.toLowerCase().split(/\s+/).filter(Boolean);
    const passes = (n, skip) => {
      if (words.length && !words.every(w => (n.title + " " + n.summary + " " + (n.tags || []).join(" ")).toLowerCase().includes(w))) return false;
      if (cmp.only && !cmp.checked.has(n.id)) return false;
      for (const [k, set] of Object.entries(cmp.filters)) {
        if (k === skip || !set.size) continue;
        if (!vals(n, k).some(v => set.has(v))) return false;
      }
      return true;
    };
    // facet chips with live counts (count ignores the group's own selection)
    facetBox.innerHTML = keys.filter(k => pool.some(n => vals(n, k).length)).map(k => {
      const f = FAC[k], sel = cmp.filters[k] || new Set();
      const chips = f.values.map(v => {
        const c = pool.filter(n => passes(n, k) && vals(n, k).includes(v)).length;
        return `<button type="button" class="fchip" data-k="${k}" data-v="${v}" aria-pressed="${sel.has(v)}" title="${esc(f.help)}">${esc(v)}<small>${c}</small></button>`;
      }).join("");
      return `<div class="fgroup"><span title="${esc(f.help)}">${esc(f.label)}</span>${chips}</div>`;
    }).join("");

    const rows = pool.filter(n => passes(n)).map(n => ({ n, rel: related(n, sp), tools: t === "workflow" ? toolsUsed(n) : [], ev: (n.sources || []).length, links: degree(n.id) }));
    const { key, dir } = cmp.sort;
    const sv = r => key === "name" ? r.n.title.toLowerCase() : key === "ev" ? r.ev : key === "links" ? r.links : LEVEL[r.n[key]] || 0;
    rows.sort((a, b) => (sv(a) < sv(b) ? -1 : sv(a) > sv(b) ? 1 : 0) * dir || a.n.title.localeCompare(b.n.title));
    const maxEv = Math.max(1, ...pool.map(n => (n.sources || []).length));
    const sortBtn = (k, label) => `<button type="button" data-sort="${k}"${cmp.sort.key === k ? ` data-dir="${cmp.sort.dir > 0 ? "↑" : "↓"}"` : ""}>${label}</button>`;
    const head = `<thead><tr><th><span class="sr" hidden>Compare</span></th><th>${sortBtn("name", "Name")}</th>${
      keys.map(k => `<th>${LEVEL[FAC[k].values[0]] ? sortBtn(k, FAC[k].label) : FAC[k].label}</th>`).join("")
    }<th>${relLabel}</th>${t === "workflow" ? "<th>Tools</th>" : ""}<th class="num">${sortBtn("ev", "Evidence")}</th><th class="num">${sortBtn("links", "Links")}</th></tr></thead>`;
    const body = rows.map(({ n, rel, tools, ev, links }) => `<tr class="${cmp.checked.has(n.id) ? "checked" : ""}" style="--c:${color(n.type)}">
      <td><input type="checkbox" id="chk-${n.id}" data-id="${n.id}" ${cmp.checked.has(n.id) ? "checked" : ""} aria-label="Mark ${esc(n.title)} for comparison"></td>
      <td class="name"><a href="#${n.id}"><span class="dot"></span>${esc(n.title)}</a><p>${esc(n.summary)}</p></td>
      ${keys.map(k => `<td>${FAC[k].list ? pills(vals(n, k)) : LEVEL[n[k]] ? level(n[k]) : pills(vals(n, k))}</td>`).join("")}
      <td class="rels">${refs(rel)}</td>
      ${t === "workflow" ? `<td class="rels">${refs(tools)}</td>` : ""}
      <td class="num">${ev}<span class="bar" style="width:${Math.round(ev / maxEv * 40)}px"></span></td>
      <td class="num">${links}</td></tr>`).join("");
    const cols = 5 + keys.length + (t === "workflow" ? 1 : 0);
    table.innerHTML = head + `<tbody>${body || `<tr><td colspan="${cols}" class="empty">No ${spec()[1].toLowerCase()} match these filters.</td></tr>`}</tbody>`;
    const active = Object.values(cmp.filters).reduce((a, s) => a + s.size, 0) + (words.length ? 1 : 0) + (cmp.only ? 1 : 0);
    document.getElementById("cmp-count").textContent = `Showing ${rows.length} of ${pool.length} ${spec()[1].toLowerCase()}` +
      (cmp.checked.size ? ` · ${cmp.checked.size} checked` : "") + (active ? "" : " · no filters");
  }
  drawCompare();

  window.addEventListener("hashchange", route);
  fit();
  route();
})();
</script>
"""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_graph import FACETS, RELATIONS

    graph = json.loads((ROOT / "graph" / "graph.json").read_text())
    texts = {n["id"]: (ROOT / n["path"]).read_text() for n in graph["nodes"]}
    html = render(graph, texts, (ROOT / "README.md").read_text(), RELATIONS, FACETS, fragment="--fragment" in sys.argv)
    Path(args[0]).write_text(html)
    print(f"wrote {args[0]} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
