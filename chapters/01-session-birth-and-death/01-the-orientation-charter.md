# Pattern 1: The Orientation Charter

Chapter 1 - Session Birth and Death

A spawned agent starts cold, and a hand-typed opening prompt is different every time. Runs skip the
safety check, forget facts you already wrote down, and drift from what you meant. When one run works
and the next does not, there is no single thing to compare, because the prompt lived in scrollback
and is already gone.

## The rule

**An agent's opening prompt is a build artifact, not a message someone typed.**

If a human types the opening prompt fresh each time, you get a different agent every time. Some runs
skip the safety check, some forget facts you already know, and nobody can say why one run worked and
the next did not, because there is no one thing to compare. The fix is not "be more careful", because
people are not careful at 11pm. Write the prompt once, as a template with blanks, and fill the blanks
by machine. Now every run starts from the same known place, and you can diff two runs. This holds no
matter which agent tool you use.

## How we do it

This is our version. The shape travels; the file names are ours.

1. Classify the ask before anyone writes a word of prompt. (We tag it tech or business and pick a
   persona to match.)
2. Run a preflight before you spawn anything. (Ours checks capacity, grabs a free lane, and sniffs
   for collisions with work already running.)
3. Keep exactly one template per class of agent, checked into source control. (Ours:
   `orientation-template.md`.)
4. Fill the slots with a function, never string pasting and never a shell. A slot looks like
   `{{ask}}`. Pasting lets someone's typed text turn into a command; a fill function cannot. (Ours:
   `render_orientation.py`.)
5. Fail closed if any slot is empty or unknown. Do not ship a half-built prompt and hope. (Ours stops
   with `render failed: unfilled placeholder {{persona}}`.)
6. Pass anything a human typed as a file, never as a command-line argument. Arguments get logged,
   truncated, and interpreted; a file just sits there as data. (Ours: `--ask-file`.)
7. Fix the section order once. (Ours, always: identity, the ask verbatim, preflight verdict, first
   act, scope guardrails, chain of command, persona, shutdown state.)

## Steal this

- Write your opening prompt as a template with named blanks, not a fresh paragraph every time.
- Make an empty blank a hard stop, not a warning you will get to later.
- Pass anything typed by a human through a file, never through a command argument.

## Maturity

Honestly, solid. Tested, fails closed, and two real filled-in renders are saved so you can see what a
finished prompt looks like. The one place I will not oversell it is capacity: we cap it at three
agents running at once, on purpose, because we have not proven it past that yet. That is a scale
question, not a correctness question.

## Crawl, walk, run

- **Crawl:** one text file with blanks and a checklist you fill by hand. Ten minutes.
- **Walk:** a script fills the blanks and refuses to run on an empty one. An afternoon.
- **Run:** preflight, lanes, personas, and a saved render for every spawn. That is the fleet.
