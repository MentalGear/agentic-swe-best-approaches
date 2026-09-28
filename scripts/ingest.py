#!/usr/bin/env python3
"""Capture a source (HN thread or any web page) and extract what's new since the last capture.

The knowledge base is mined from sources. This script does the mechanical half: fetch, snapshot,
and compute the delta. Mining the delta into nodes is done by Claude via the `kb-update` skill
(.claude/skills/kb-update/SKILL.md), or by hand.

Commands:
  ingest.py add <url> [--slug NAME] [--node ID]
                                      register a new source and capture it; --node names the
                                      source node (sources/<ID>.md) that cites it
  ingest.py refresh [SLUG ...]        re-capture registered sources (all if none named)
  ingest.py list                      show registered sources and their last capture

Each capture writes, under .cache/sources/<slug>/ (gitignored, may be deleted any time):
  <stamp>.txt          full flattened text of the source
  delta-<stamp>.txt    only what's new: unseen HN comments, or a unified diff for web pages
and updates sources/manifest.json (committed): url, kind, captures, and for HN the set of comment
ids already seen, so deltas work on a fresh clone without the cache.

Kinds:
  hn   news.ycombinator.com/item?id=N  -> full comment tree via the HN Algolia API
  web  anything else                   -> HTML reduced to readable text

Stdlib only. Behind a TLS-intercepting proxy, point SSL_CERT_FILE at its CA bundle.
"""
import argparse
import datetime as dt
import difflib
import hashlib
import html
import json
import os
import re
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "sources" / "manifest.json"
CACHE = ROOT / ".cache" / "sources"
HN_ITEM = "https://news.ycombinator.com/item?id="
UA = "agentic-swe-kb-ingest/1.0 (+https://github.com/MentalGear/agentic-swe-best-approaches)"


def fetch(url):
    ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE"))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")


def html_to_text(s):
    s = re.sub(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"\2 (\1)", s, flags=re.S)
    s = re.sub(r"<(p|br|li|h[1-6]|pre|tr|div)[^>]*>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def page_text(raw):
    raw = re.sub(r"<(script|style|nav|footer|header|noscript)\b.*?</\1>", "", raw, flags=re.S | re.I)
    m = re.search(r"<(article|main)\b.*?</\1>", raw, re.S | re.I) or re.search(r"<body\b.*</body>", raw, re.S | re.I)
    text = html_to_text(m.group(0) if m else raw)
    lines = [ln.strip() for ln in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def hn_id(url):
    m = re.match(r"https?://news\.ycombinator\.com/item\?id=(\d+)", url)
    return int(m.group(1)) if m else None


def capture_hn(item_id):
    """Return (full_text, comments) where comments maps id -> formatted block."""
    data = json.loads(fetch(f"https://hn.algolia.com/api/v1/items/{item_id}"))
    comments, lines = {}, []
    head = f"# {data.get('title') or ''}\n{HN_ITEM}{item_id}\nurl: {data.get('url') or ''}\n"
    if data.get("text"):
        head += "\n" + html_to_text(data["text"]).strip() + "\n"

    def walk(node, depth, parent):
        if node.get("type") == "comment" and node.get("text"):
            body = html_to_text(node["text"]).strip()
            pad = "  " * depth
            block = f"{pad}[{node['id']}] {node.get('author')} (parent {parent}): " + body.replace("\n", "\n" + pad)
            comments[node["id"]] = block
            lines.append(block)
        for child in node.get("children") or []:
            walk(child, depth + 1, node["id"])

    walk(data, -1, None)
    return head + "\n" + "\n\n".join(lines) + "\n", comments


def load_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"sources": {}}


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n")


def slugify(url):
    if hn_id(url):
        return f"hn-{hn_id(url)}"
    s = re.sub(r"^https?://(www\.)?", "", url)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def capture(slug, entry):
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outdir = CACHE / slug
    outdir.mkdir(parents=True, exist_ok=True)
    previous = sorted(p for p in outdir.glob("2*.txt"))
    if entry["kind"] == "hn":
        text, comments = capture_hn(hn_id(entry["url"]))
        seen = set(entry.get("seen_ids", []))
        new_ids = [i for i in comments if i not in seen]
        delta = f"# New comments since last capture: {len(new_ids)}\n# source: {entry['url']}\n\n"
        delta += "\n\n".join(comments[i] for i in new_ids) + "\n"
        entry["seen_ids"] = sorted(seen | set(comments))
        summary = f"{len(comments)} comments, {len(new_ids)} new"
    else:
        text = page_text(fetch(entry["url"]))
        old = previous[-1].read_text().splitlines(keepends=True) if previous else []
        diff = list(difflib.unified_diff(old, text.splitlines(keepends=True), "previous", "current", n=2))
        delta = "".join(diff) if previous else text
        changed = bool(diff) or not previous
        summary = f"{len(text)} chars, {'changed' if changed else 'unchanged'}"
    (outdir / f"{stamp}.txt").write_text(text)
    delta_path = outdir / f"delta-{stamp}.txt"
    delta_path.write_text(delta)
    entry.setdefault("captures", []).append(
        {"at": stamp, "sha256": hashlib.sha256(text.encode()).hexdigest(), "summary": summary}
    )
    return summary, delta_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("url")
    a.add_argument("--slug")
    a.add_argument("--node", help="id of the source node that cites this source")
    r = sub.add_parser("refresh")
    r.add_argument("slugs", nargs="*")
    sub.add_parser("list")
    args = ap.parse_args()

    m = load_manifest()
    srcs = m["sources"]
    if args.cmd == "list":
        for slug, e in sorted(srcs.items()):
            last = e["captures"][-1] if e.get("captures") else {}
            print(f"{slug:24} {e['kind']:4} {e.get('node') or '-':16} {last.get('at', '-'):17} {last.get('summary', '')}  {e['url']}")
        return
    if args.cmd == "add":
        slug = args.slug or slugify(args.url)
        if slug in srcs:
            sys.exit(f"{slug} already registered; use: ingest.py refresh {slug}")
        srcs[slug] = {"url": args.url, "kind": "hn" if hn_id(args.url) else "web", "node": args.node}
        targets = [slug]
    else:
        targets = args.slugs or sorted(srcs)
        unknown = [t for t in targets if t not in srcs]
        if unknown:
            sys.exit(f"unknown source(s): {', '.join(unknown)}; see: ingest.py list")
    for slug in targets:
        summary, delta = capture(slug, srcs[slug])
        save_manifest(m)
        print(f"{slug}: {summary}\n  delta: {delta.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
