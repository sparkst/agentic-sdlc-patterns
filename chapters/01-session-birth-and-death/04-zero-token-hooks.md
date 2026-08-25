# Pattern 4: Zero-Token Hooks

Chapter 1 - Session Birth and Death

Some guarantees are too important to leave to the model, because a model under context pressure skips
them and it costs tokens to do at all. And some facts are only knowable at the very start: once an
agent has been working for an hour, a plain status check cannot tell work this session did from work
that was already sitting uncommitted when it opened. Both problems want the same answer.

## The rule

**What the opening of a session must guarantee belongs in a process hook, not in the instructions.**

If a guarantee lives in the prompt, it is optional, because the model can always decide it has more
important things to spend attention on. Move it into a deterministic hook that runs on its own, costs
no tokens, and exits cleanly even when its backing service is down. Put the things that must be true
at t=0 there: identity, draining the inbox, and any baseline you can only measure before the model
touches anything. Then make absence safe: if the hook did not run, the feature that depended on it
asks a human rather than guessing.

## How we do it

This is our version. The shape travels; the file names are ours.

1. Two independent start hooks, both deterministic and both spending zero model tokens.
2. One registers the session: it derives a stable id, freezes it into the session's environment
   file, renames the multiplexer session to match, and drains any waiting inbox.
3. The other snapshots scope: the repo head, the branch, and the exact paths already dirty before the
   model touched anything, capped at a fixed number with a truncation flag, on a short time budget.
4. Every hook exits zero even when its daemon is down, so a hook can never wedge a session at birth.
5. Absence is safe by construction: with no snapshot, every close-out decision that depends on scope
   asks a human instead of guessing.

## Steal this

- Put identity, inbox drain, and any t=0-only baseline into hooks with a hard time budget that exit
  zero on every path.
- Make a hook that could not run degrade the dependent feature to "ask a human", never to a wrong
  answer.
- Measure "what was already dirty when I opened" at the start, because you cannot reconstruct it later.

## Maturity

Works, at founder scale. The mechanism is sound and fail-safe, but the thing that reads it has burned
real work on shared checkouts, where "already dirty at start" is a poor stand-in for "not mine". A
session that registered without its hooks in place once caused a redelivery storm. The hook layer is
right; the close-out logic that consumes it still needs a real ownership signal, not a proxy.

## Crawl, walk, run

- **Crawl:** a start script that prints the session id and the current dirty files. Ten minutes.
- **Walk:** hooks that register identity and snapshot the dirty set, and exit zero no matter what. An
  afternoon.
- **Run:** two independent zero-token hooks, a capped snapshot with a truncation flag, and every
  scope-dependent decision degrading to "ask a human" when the snapshot is missing.
