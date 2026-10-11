---
summary: Built-in tool that lets Claude ask you structured multiple-choice questions in any mode, not only plan mode.
tags: [claude-code, built-in, intent]
origin: built-in
stage: [intent]
effort: low
links:
  - enables: wf-interview-first
---
# Claude Code question tool

miki123211: "I keep forgetting that CC has access to the 'question' tool, even outside plan mode,
which is mostly why I still use it sometimes" ([49854758](https://news.ycombinator.com/item?id=49854758)).
diegof79 forked an interviewing skill to use it because the UI is faster than typing answers
([49851420](https://news.ycombinator.com/item?id=49851420)).

Ask for it explicitly: "Use the question tool, one question at a time, with your recommended option
first."

Jimmc414 values it as plan mode's main benefit ([49856208](https://news.ycombinator.com/item?id=49856208)). whywhywhywhy's complaint: questions
often come as two options even when no real choice exists ([49857963](https://news.ycombinator.com/item?id=49857963)). Tell it to skip questions
with an obvious answer.
