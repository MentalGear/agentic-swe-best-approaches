---
id: con-underspecification
type: concept
title: Smarter models still can't read minds
summary: Better models infer more, but intent you never stated (taste, org context, implicit constraints) still has to be elicited; the cheapest place is before code exists.
tags: [core, intent]
stage: [intent]
sources: [49851057, 49852964, 49852428, 49852704, 49854264, 49854413, 49853748, 49851243, 49852866, 49851148, 49854063, 49855710, 49858858, 49856641, 49854895, 49858321, 49857375, 49856922, 49857963, 49860634, 49860819, 49882857, 49880345, 49881067, 49878598, 49878620]
links:
  - relates-to: con-domain-language
---
# Smarter models still can't read minds

The strongest pushback on "the model just gets it". wvenable: "Is Fable going to read my mind?"
([49852964](https://news.ycombinator.com/item?id=49852964)). Marha01: "AI cannot read minds, no
matter how intelligent it is. Hell, often I don't even know exactly what I want before the planning
phase is finished" ([49854294](https://news.ycombinator.com/item?id=49854294)).

## What goes missing

- **Taste and implicit context.** pioneerjeff: the gap was "not capability, but taste" — preferences,
  past decisions, product intuition ([49854264](https://news.ycombinator.com/item?id=49854264)).
  t0mpr1c3's refinement: models "do not elicit feedback well. Where there is ambiguity, they tend to
  pick a solution and call it good" ([49854413](https://news.ycombinator.com/item?id=49854413)).
- **Organisational context.** status_quo69: changes with product-wide impact that no codebase reveals
  ([49851243](https://news.ycombinator.com/item?id=49851243)).
- **Expert defaults.** deprave's example: asked for a short Go TLS client function, several models
  required a private-key *file* instead of accepting a `crypto.Signer` (HSM/KMS-friendly)
  ([49852704](https://news.ycombinator.com/item?id=49852704)).
- **Irrelevant questions, missed real ones.** joegibbs: the model asks "should I use the existing
  system or build a new one in another language?" while silently assuming things that *were*
  ambiguous ([49852866](https://news.ycombinator.com/item?id=49852866)).
- **Doing too much.** jumploops: newer models "do more by default", so you now spend effort saying
  what *not* to do ([49851148](https://news.ycombinator.com/item?id=49851148)).

## Use it

Assume unstated intent will be filled with a plausible default. Either state it, have the model
interview you ([wf-interview-first](../workflows/wf-interview-first.md)), or make choices cheap to
reverse ([wf-prototype-as-clay](../workflows/wf-prototype-as-clay.md)). Ask the model to list its
assumptions explicitly; that is where wrong guesses show up.

## Later in the thread (refresh 2026-09-26)

- thiht: "The best model in the world can't work around misinterpretation because of bad specs"
  ([49855710](https://news.ycombinator.com/item?id=49855710)); burningion: most people aren't precise when first describing a problem, and
  jumping to implementation skips refining it ([49858858](https://news.ycombinator.com/item?id=49858858)). i2km points to Polanyi's tacit
  knowledge (1958) ([49854895](https://news.ycombinator.com/item?id=49854895)).
- everforward: the trouble on large features is "small decisions way down the stack that bubble up,
  or an incoherent data model" — e.g. a state tracker that assumed containers were either running or
  fully removed, leaking storage ([49856641](https://news.ycombinator.com/item?id=49856641)).
- deprave, clarifying their TLS example: they don't expect mind-reading, but models produce lots of
  verbose output and never "here's a simple response to your ask, but have you also considered…"
  ([49858321](https://news.ycombinator.com/item?id=49858321)). fluidcruft's retort: "It can't read your mind that you have an HSM, can it?"
  ([49857375](https://news.ycombinator.com/item?id=49857375)).

## Disputed

samdjstephens found recent models' clarifying questions "generally not useful" — about things the
model would have resolved anyway — and "time-wasting and anxiety inducing". Their fix is on the human
side: understand the code well enough to predict the model's assumptions ([49856922](https://news.ycombinator.com/item?id=49856922)).
whywhywhywhy: Claude Code's plan questions come in pairs of options even when there's no real choice,
so one option is often a downgrade ([49857963](https://news.ycombinator.com/item?id=49857963)).

bfung: a good high-level plan with functional and non-functional requirements costs less and brings
no surprises; "the more right words up front, the less steering you need to do" ([49860634](https://news.ycombinator.com/item?id=49860634)).
mikeocool objects to answering such reports with "are you using the latest model?" ([49860819](https://news.ycombinator.com/item?id=49860819)).

## Second thread (2026-09-28)

- zaxioms asked Fable for a simple class they had "very well scoped in my mind" but only loosely described;
  the result was "laughably over-complicated", and hundreds of lines came down to fewer than 100 with more
  back and forth ([49882857](https://news.ycombinator.com/item?id=49882857)).
- OliveronData: explicit instructions in `AGENTS.md` (no `malloc`, use the arena API, no getters) were broken
  in turn; fixing one violation produced another ("If I let the reins slip just a little bit, everything turns
  into a mush") ([49880345](https://news.ycombinator.com/item?id=49880345)). an0malous: it "doesn't always follow conventions well even if you've documented
  them" ([49881067](https://news.ycombinator.com/item?id=49881067)). vincent-uden calls `AGENTS.md` and skills "just a proxy for what we actually want"
  ([49878598](https://news.ycombinator.com/item?id=49878598)).
- The article lists "you can create a full spec upfront" and "English is the new programming language" as
  fallacies: natural language is vague and conflicting, and the reliable way to find contradictions in your
  instructions is to build what they say ([src-article-coding-not-solved](../sources/src-article-coding-not-solved.md)).
  hanifbbz: "A couple of days building can really save us from a couple of hours of thinking"
  ([49878620](https://news.ycombinator.com/item?id=49878620)).

<!-- graph:links:begin (generated by scripts/build_graph.py; do not edit) -->
## Links

**Outgoing**

- *relates-to* → [Fix the vocabulary first](../concepts/con-domain-language.md) `con-domain-language`

**Backlinks**

- [Implementation details in the plan](../anti-patterns/ap-overspecified-plan.md) `ap-overspecified-plan` *tension-with* this
- [Scale ceremony to blast radius](../concepts/con-blast-radius.md) `con-blast-radius` *relates-to* this
- [Typing code versus owning the software](../concepts/con-coding-vs-engineering.md) `con-coding-vs-engineering` *relates-to* this
- [Never trust a single session](../concepts/con-cross-model-review.md) `con-cross-model-review` *relates-to* this
- [The two jobs of plan mode](../concepts/con-two-jobs-of-plan-mode.md) `con-two-jobs-of-plan-mode` *relates-to* this
- [HN thread: Plan mode is dead](../sources/src-hn-thread.md) `src-hn-thread` *surfaces* this
- [Make the agent interview you](../workflows/wf-interview-first.md) `wf-interview-first` *addresses* this
- [Plan mode as a late checkpoint](../workflows/wf-plan-as-late-checkpoint.md) `wf-plan-as-late-checkpoint` *addresses* this
- [Skip the plan, review the PR](../workflows/wf-review-code-not-plans.md) `wf-review-code-not-plans` *tension-with* this
- [Explore, list unknowns, scaffold, spike](../workflows/wf-scaffold-then-spike.md) `wf-scaffold-then-spike` *addresses* this
- [Challenge the first plan with more research](../workflows/wf-second-research-pass.md) `wf-second-research-pass` *addresses* this
- [Re-plan until the spec stops changing](../workflows/wf-spec-until-quiet.md) `wf-spec-until-quiet` *addresses* this

**Evidence:** [49851057](https://news.ycombinator.com/item?id=49851057), [49852964](https://news.ycombinator.com/item?id=49852964), [49852428](https://news.ycombinator.com/item?id=49852428), [49852704](https://news.ycombinator.com/item?id=49852704), [49854264](https://news.ycombinator.com/item?id=49854264), [49854413](https://news.ycombinator.com/item?id=49854413), [49853748](https://news.ycombinator.com/item?id=49853748), [49851243](https://news.ycombinator.com/item?id=49851243), [49852866](https://news.ycombinator.com/item?id=49852866), [49851148](https://news.ycombinator.com/item?id=49851148), [49854063](https://news.ycombinator.com/item?id=49854063), [49855710](https://news.ycombinator.com/item?id=49855710), [49858858](https://news.ycombinator.com/item?id=49858858), [49856641](https://news.ycombinator.com/item?id=49856641), [49854895](https://news.ycombinator.com/item?id=49854895), [49858321](https://news.ycombinator.com/item?id=49858321), [49857375](https://news.ycombinator.com/item?id=49857375), [49856922](https://news.ycombinator.com/item?id=49856922), [49857963](https://news.ycombinator.com/item?id=49857963), [49860634](https://news.ycombinator.com/item?id=49860634), [49860819](https://news.ycombinator.com/item?id=49860819), [49882857](https://news.ycombinator.com/item?id=49882857), [49880345](https://news.ycombinator.com/item?id=49880345), [49881067](https://news.ycombinator.com/item?id=49881067), [49878598](https://news.ycombinator.com/item?id=49878598), [49878620](https://news.ycombinator.com/item?id=49878620)

<!-- graph:links:end -->
