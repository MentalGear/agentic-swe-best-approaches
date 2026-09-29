---
summary: The unsolved problem the article ends on; when agents write most of the code, how does the human still understand the system, and how does that scale to many agents?
tags: [core, understanding, open-problem]
stage: [understanding]
links:
  - relates-to: con-ai-prose-fatigue
---
# Keeping the human's mental model current

The article ends here: "We still haven't solved how to help people stay oriented as hundreds of
increasingly capable agents change a system at once."

## The worry

taurath: "I'm actively watching understanding slip away from developers, code review getting paired down to no comment checkmarks" ([49851173](https://news.ycombinator.com/item?id=49851173)).
eddy162: reading diffs doesn't scale anymore; plan mode was how they kept their mental model
([49852822](https://news.ycombinator.com/item?id=49852822)).

## Positions on the fix

| Position | Who | Caveat raised |
|---|---|---|
| Ask the agent to explain; diagrams, sequence charts, tests that prove its claims | frankc [49852511](https://news.ycombinator.com/item?id=49852511), bcherny [49850929](https://news.ycombinator.com/item?id=49850929) | "It's really good at making you feel that you understand things" (jeppester [49853788](https://news.ycombinator.com/item?id=49853788)); generated diagrams focus on the wrong things (abbefaria27 [49852993](https://news.ycombinator.com/item?id=49852993)); it doesn't volunteer what it thinks is irrelevant (spiffytech [49852601](https://news.ycombinator.com/item?id=49852601)). |
| Generate views *deterministically* from the code | teekert [49854001](https://news.ycombinator.com/item?id=49854001) | Only covers what a script can extract. See [wf-deterministic-views](../workflows/wf-deterministic-views.md). |
| Delegate typing, not thinking; keep part of the work yourself | philbo [49853739](https://news.ycombinator.com/item?id=49853739), dsign [49852178](https://news.ycombinator.com/item?id=49852178) | Leaves throughput on the table, knowingly. |
| A system that holds the program's evolving state for the operator | _bobm [49853759](https://news.ycombinator.com/item?id=49853759) | Doesn't exist yet. |
| Model the *solution/problem*, not the code | arendtio [49854680](https://news.ycombinator.com/item?id=49854680) | Reframing, not a tool. |

## Use it

Combine the two that hold up: deterministic views for structure you must not get wrong, and
adversarially-checked explanations ([wf-adversarial-review](../workflows/wf-adversarial-review.md))
for the rest. Treat an unchecked agent explanation as a hypothesis.

## Later in the thread (refresh 2026-09-26)

- aDyslecticCrow: no documentation system transfers institutional knowledge; people do. codethief:
  a company's value is "the mental map the team has built of the problem"
  ([49856300](https://news.ycombinator.com/item?id=49856300), [49858465](https://news.ycombinator.com/item?id=49858465)).
- senordevnyc disagrees for well-documented codebases: an agent can read years of commits, tickets
  and design docs in half an hour and explain the history better than a person
  ([49857547](https://news.ycombinator.com/item?id=49857547)); maccard's experience in a large codebase was that exploring one area filled half
  the context window every time ([49857952](https://news.ycombinator.com/item?id=49857952)).
- hoc is building canvas-based views for independent analysis and visualisation of changes after the
  fact ([49855641](https://news.ycombinator.com/item?id=49855641)).
- nunez: if maintainers lose access to frontier models, they inherit code nobody understands
  ([49858204](https://news.ycombinator.com/item?id=49858204)). fendy3002: knowing what each module does may be enough ([49854943](https://news.ycombinator.com/item?id=49854943)).

aDyslecticCrow: what the code *should* do can itself be institutional knowledge, spread across tools,
databases and other departments' systems you don't have code for; a person knows whom to ask
([49870125](https://news.ycombinator.com/item?id=49870125)). taurath: teams that still care about code understanding keep shipping, while
vibe-coding teams in the same org "flounder after the initial burst of features" ([49860769](https://news.ycombinator.com/item?id=49860769)).

Also cited: [49853201](https://news.ycombinator.com/item?id=49853201).
