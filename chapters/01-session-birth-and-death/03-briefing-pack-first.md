# Pattern 3: Briefing Pack First

Chapter 1 - Session Birth and Death

A freshly oriented agent wants to talk about scope right away. So it asks about facts that were
already in the design docs, misses the repo's process gates, duplicates an open issue, or edits a
file that two open pull requests and a live sibling session are already touching. The cheapest way to
avoid all of that is to make the agent gather and read before it may say a word about scope.

## The rule

**Make orientation a gathered artifact, read and reported on before any scope talk.**

The failure here is not ignorance, it is eagerness. The agent has the tools to find out what is
already true; it just skips them and starts talking. So make gathering the mandatory first act, and
make it deterministic: one command that collects the design docs, the repo's rules, the open work,
and the file-level collisions with other agents and pull requests. A source that could not be read
reports "unknown", never "clear", because a gather that failed is not a clean bill of health.

## How we do it

This is our version. The shape travels; the file names are ours.

1. The charter names gathering as the first act, before scope. No exceptions.
2. One deterministic gatherer emits a single pack: design maps scored by overlap with the ask, the
   repo's rules and specs, recent pull requests, open issues, a health pulse, and a collisions block.
3. The collisions block covers three shapes: one file touched by two or more open pull requests; an
   ask path an open pull request already changes; and a live session already on the repo.
4. A degraded source is reported as unknown, never clear.
5. The pack points; it does not summarize. The agent reads what the pack points at, then reports the
   overlaps and collisions with a cost attached, so nothing is folded into the build silently.

## Steal this

- One command gathers the design docs, the rules, the open work, and the file collisions. The agent
  reads and reports before it may discuss scope.
- Score design docs by overlap with the ask so the relevant ones surface first.
- A source that failed to load reports "unknown", never "nothing there".

## Maturity

Solid, with one honest limit. The gatherer is deterministic and tested, but its collision snapshot
goes stale: on a build that runs longer than an hour, you have to re-run it before you spawn the next
worker, because another agent may have started touching the same files while you were not looking.

## Crawl, walk, run

- **Crawl:** a checklist the agent reads first: the design doc, the open issues, the recent PRs. Ten
  minutes.
- **Walk:** a script that dumps those into one file the agent must read before scope. An afternoon.
- **Run:** overlap scoring, a real collisions block across PRs and live sessions, and unknown-not-clear
  on every degraded source.
