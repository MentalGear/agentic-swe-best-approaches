---
summary: Better models infer more, but intent you never stated (taste, org context, implicit constraints) still has to be elicited; the cheapest place is before code exists.
tags: [core, intent]
stage: [intent]
links:
  - relates-to: con-domain-language
---
# Smarter models still can't read minds

The strongest pushback on the idea that the model just gets it. wvenable: "Is Fable going to read my mind?"
([49852964](https://news.ycombinator.com/item?id=49852964)). Marha01: "AI cannot read minds, no
matter how intelligent it is. Hell, often I don't even know exactly what I want before the planning
phase is finished" ([49854294](https://news.ycombinator.com/item?id=49854294)).

## What goes missing

- **Taste and implicit context.** pioneerjeff: the biggest issue "wasn't capability, but taste" — preferences,
  past decisions, product intuition ([49854264](https://news.ycombinator.com/item?id=49854264)).
  t0mpr1c3's refinement: models "do not elicit feedback well. Where there is ambiguity, they tend to
  pick a solution and call it good" ([49854413](https://news.ycombinator.com/item?id=49854413)).
- **Organisational context.** status_quo69: changes with product-wide impact that no codebase reveals
  ([49851243](https://news.ycombinator.com/item?id=49851243)).
- **Expert defaults.** deprave's example: asked for a short Go TLS client function, several models
  required a private-key *file* instead of accepting a `crypto.Signer` (HSM/KMS-friendly)
  ([49852704](https://news.ycombinator.com/item?id=49852704)).
- **Irrelevant questions, missed real ones.** joegibbs: the model asks "Should I use the existing system or create a whole new one in a different language?" while silently assuming things that *were*
  ambiguous ([49852866](https://news.ycombinator.com/item?id=49852866)).
- **No one-shot products.** Razengan: "You're not gonna one-shot a full, actual product"; each element still has to be designed on its own ([49880852](https://news.ycombinator.com/item?id=49880852)). idle_zealot sees two kinds of users: those with a vision they lack the time or skill to build, and those who want the computer to supply the intent and then react to what they get; "It seems the latter cohort is much larger" ([49881013](https://news.ycombinator.com/item?id=49881013)).
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

Also cited: [49851057](https://news.ycombinator.com/item?id=49851057), [49852428](https://news.ycombinator.com/item?id=49852428), [49853748](https://news.ycombinator.com/item?id=49853748), [49854063](https://news.ycombinator.com/item?id=49854063).
