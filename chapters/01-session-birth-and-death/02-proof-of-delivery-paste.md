# Pattern 2: Proof-of-Delivery Paste

Chapter 1 - Session Birth and Death

Handing a brief to a terminal agent over a shared multiplexer is the most fragile hop in the whole
system. A sleep followed by a keystroke fails on a booting pane, on a modal that eats the paste, on a
same-breath submit that lands as a newline, and on a slow render that hides a paste that actually
landed. "The command exited 0" tells you nothing about whether the agent got the message.

## The rule

**Never treat "the command exited 0" as proof a brief was delivered or submitted.**

Delivery over a terminal is not a function call; it is a keystroke landing in a UI that may not be
ready. So do not trust the send. Prove the surface is ready before you type, prove the text landed
after you type, and prove the turn actually started before you call it submitted. Every step is
gated on something you can see, not on the exit code of the tool that did the typing. And every
retry is single-shot and evidence-gated, because a blind retry is how you send the same brief twice.

## How we do it

This is our version. The shape travels; the file names are ours.

1. Poll for readiness, do not sleep. Ready means a specific rendered marker or a live composer line,
   and any numbered-option line forces not-ready, because a menu wants a different kind of input.
2. Verify the paste landed by reading the composer back for the prompt's own text, normalized at a
   minimum length so a short coincidence cannot pass. The verdict is one of three: landed,
   positively absent, or unverifiable.
3. Send the submit as a separate key event, then walk a ladder: look for the turn to start, then a
   plain submit, then a guarded clear-and-retype.
4. Allow exactly one re-paste, and only when two captures both show the text missing, a minimum wait
   has passed, and there is budget left to verify the result.
5. Write the delivery verdict as a first-class field (`delivered`, `failed`, `timed_out`, `n/a`) and
   page on it, so a silent non-delivery becomes a visible failure.

## Steal this

- Gate the send on evidence the surface accepts input; gate the submit on evidence the input landed.
- Make every retry single-shot and evidence-gated, never "just send it again".
- Publish the delivery result as a field you can alert on, not a log line nobody reads.

## Maturity

Works, at founder scale, and openly fragile. The comments record several live incidents, two of them
caused by the fix for the one before: a re-paste wait that was too short doubled the brief, a longer
one still doubled it, and the current value is an honest guess. There is a known worst-case timing
that runs close to the liveness gate. The technique is sound; the constants are not settled, and I
will tell you that to your face.

## Crawl, walk, run

- **Crawl:** after you paste, read the screen back once and eyeball that your text is there before
  you hit enter. Two minutes.
- **Walk:** a script polls for readiness, checks the composer for your text, and submits as a
  separate step. A morning.
- **Run:** three-state verdicts, a single evidence-gated re-paste, and a delivery field you page on.
