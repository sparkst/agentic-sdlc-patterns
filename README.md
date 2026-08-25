# The Sparkry Pattern Language for Agentic SDLC

Design patterns from a real, running fleet: how one operator ships production software with a
supervised fleet of AI coding agents, and what any team can reuse.

This is a pattern language in the Alexander and Gang-of-Four sense: named, composable solutions to
recurring problems, each stating its forces and its consequences. There are 111 patterns in 14
chapters. Every pattern carries an honest maturity verdict, and where a mechanism has open holes,
the holes are named. This catalog treats scars as part of the product.

## Who this is for

Engineers building agentic software development systems, especially inside regulated enterprises
where "the agent did it" is not an acceptable audit answer. If you run more than one AI coding agent
and you have felt the specific pain of a session that drifted, a memory that went stale, a close-out
that lost work, or a review that passed something wrong, these patterns are the shapes that survived
those failures.

## The three ways to use this

1. **The repo (free).** Read the patterns. Steal the generic forms. Every entry ends with a
   "steal this" section: the reusable shape an outside team can adopt without any Sparkry code.
2. **The book (paid).** The long-form treatment, with the full incident histories and the reasoning
   behind each guard. Separate from this repo.
3. **The engagement (the operator).** When you want the system built and run rather than read about,
   that is the work Sparkry does.

## Start here

- **[The Sparkry Ten](THE-TEN.md)** - ten principles that recur through every chapter. The
  compressed form of the whole catalog. Read this first.
- **[The pattern index](INDEX.md)** - all 111 patterns, one line each, with an honest maturity
  verdict and whether the full entry is published yet.
- **[NEXT.md](NEXT.md)** - the publishing queue. One new pattern lands each week.
- **[CREDITS.md](CREDITS.md)** - the ideas, projects, and people this system borrowed from, and
  where to go get the originals.

## How the patterns are published

The full entries land on a weekly cadence, newest at the top of [NEXT.md](NEXT.md). Chapter 1's
first four patterns are published now; the rest show their essence and maturity in the index and
fill in over time. Each chapter folder has a one-page diagram of that chapter's system and a short
intro.

## How to read a pattern entry

Each published entry gives: the branded name; one line stating the reusable essence; the problem;
the mechanism, as a technique you can reproduce; a diagram; an honest maturity verdict (solid,
works-but-founder-scale, fragile, mixed, or designed-not-built); and "steal this", the generic form
an outside team can adopt. Maturity verdicts are honest by policy: a pattern that would break at 10x
says so, and known open defects are named.

## License

MIT. See [LICENSE](LICENSE).
