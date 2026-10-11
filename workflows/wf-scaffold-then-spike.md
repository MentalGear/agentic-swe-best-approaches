---
summary: Before real code, require exploration, an explicit list of assumptions, a stub-only scaffold of intent in the codebase, and spikes that validate the risky assumptions.
tags: [planning, quality]
stage: [planning, execution]
effort: medium
cost: medium
scale: [feature, large]
links:
  - addresses: con-underspecification
  - addresses: con-ai-prose-fatigue
  - uses: tool-clops-mcp
  - mitigates: ap-overspecified-plan
---
# Explore, list unknowns, scaffold, spike

SkyPuncher's gate sequence before letting Claude loose ([49852074](https://news.ycombinator.com/item?id=49852074)):

1. **Explore extensively**, including areas it tends to miss (name them).
2. **List what it doesn't know or is assuming.**
3. **Scaffold intentions in code**: comments, classes, method stubs — no bodies. "Very much like a
   spec, but since it's in and alongside other code, it's much easier to identify problems."
4. **Spike and validate key assumptions.** This and step 3 are what stop a "confusion loop" where the
   model mistakes its own rough code for the long-term solution. Keeping code minimal signals it's
   draft.
5. Human review, then implement.

## Why it's good

The plan is expressed in the target language and structure, so review is concrete and the prose
problem ([con-ai-prose-fatigue](../concepts/con-ai-prose-fatigue.md)) disappears. It also forces the
assumptions list that catches [con-underspecification](../concepts/con-underspecification.md).

SkyPuncher runs this as multi-step "micro-skills" via their own MCP server, because plain skills
"were too generic and got lost to context" ([tool-clops-mcp](../tools/tool-clops-mcp.md)).
