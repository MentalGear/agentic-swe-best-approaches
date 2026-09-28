#!/usr/bin/env python3
"""Build the page published as the Claude artifact: artifact/index.html.

It is the explorer page (build_explorer.py) in fragment form, because the artifact host supplies
<html>/<head>/<body> itself, minus the notes in HOLD_BACK. Those notes contain text that the artifact
publisher's validator misreads as a pull-request review page and rejects; the phrase responsible has
not been isolated yet. Held-back notes are dropped, their edges removed, and in-page links to them
turned into plain text. The complete set stays in explorer/index.html and the Markdown notes.

build_graph.py regenerates this file on every build. Publish it to the same artifact URL to update
the live page (see README, "Artifact").
"""
import json
import re

# Notes left out of the published artifact. Remove an id once its text publishes cleanly.
HOLD_BACK = [
    "ap-anchoring-on-first-choice",
    "ap-comment-dumping",
    "ap-endless-review",
    "ap-unsupervised-autonomy",
]
ARTIFACT_URL = "https://claude.ai/artifact/HfP7FDiwjatx5xE3NU4Rys"
TABS = {"playbook", "nodes", "compare"}


def render(fragment_html):
    """Take the explorer fragment and return it without the HOLD_BACK notes."""
    m = re.search(r'(<script type="application/json" id="kb-data">)(.*?)(</script>)', fragment_html, re.S)
    data = json.loads(m.group(2).replace("<\\/", "</"))
    held = set(HOLD_BACK)
    data["nodes"] = [n for n in data["nodes"] if n["id"] not in held]
    ids = {n["id"] for n in data["nodes"]}
    data["edges"] = [e for e in data["edges"] if e["from"] in ids and e["to"] in ids]

    def unlink(text):
        return re.sub(
            r"\[([^\]]*)\]\(#([a-z0-9-]+)\)",
            lambda x: x.group(0) if x.group(2) in ids or x.group(2) in TABS else x.group(1),
            text,
        )

    for n in data["nodes"]:
        n["body"] = unlink(n["body"])
    for section in data["readme"]:
        section["body"] = unlink(section["body"])
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return fragment_html[: m.start(2)] + payload + fragment_html[m.end(2):]
