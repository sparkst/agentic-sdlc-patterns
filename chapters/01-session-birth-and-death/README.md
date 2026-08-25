# Chapter 1 - Session Birth and Death

An agent session is a process with no supervisor, no signal handler, and state that only its own
pane can see. Those three facts make both ends dangerous: a session born wrong drifts silently, and
one that dies wrong takes uncommitted work and open bookkeeping with it.

This chapter is the clearest expression of **Evidence over Exit Codes** (Sparkry Ten #2): readiness
proven by pane content, delivery by composer content, close by re-collected blockers. It also
carries **Deterministic Mechanisms over Good Intentions** (#1) in the rendered charter and the
zero-token hooks, **Per-Build Lifetime** (#8) in respawn-over-resume, and **Scars Become Constants**
(#9) in nearly every timeout below, each one tracing back to a dated incident that created it.

## The system in one page

```mermaid
flowchart TD
    subgraph BIRTH [Birth]
      A[Spawn request] --> B[Deterministic preflight]
      B --> C["#1 Orientation Charter<br/>rendered from a template"]
      C --> D["#2 Proof-of-Delivery Paste<br/>evidence-gated deliver + submit"]
      D --> E["#3 Briefing Pack First<br/>gather before scope talk"]
      A -.-> F["#4 Zero-Token Hooks<br/>register + scope snapshot at t=0"]
    end
    E --> W[Session working]
    F -.-> W
    W --> G{How does it end?}
    subgraph DEATH [Death]
      G -- planned --> H["#5 Two-Phase Exit<br/>check mints token, finish refuses without it"]
      G -- crash / kill / context-out --> I["#6 Backstop at Birth<br/>deterministic close baked in at spawn"]
      G -- someone else ends it --> J["#7 Ask It to Die<br/>inject the close command, observe liveness"]
      G -- move to new host/context --> K["#8 Successor Before Corpse<br/>verify successor, then close"]
      H --> L["#9 The Close Record<br/>machine metrics + human report"]
      I --> L
      J --> L
      K --> L
      H --> M["#10 Policy-Gated Sweep<br/>auto-clean only proven-owned blockers"]
    end
    L --> Z[Pane closes, work order closed]
    M --> Z
```

## Patterns in this chapter

| # | Pattern | Maturity | Status |
|---|---------|----------|--------|
| 1 | [The Orientation Charter](01-the-orientation-charter.md) | solid | published |
| 2 | [Proof-of-Delivery Paste](02-proof-of-delivery-paste.md) | works-but-founder-scale | published |
| 3 | [Briefing Pack First](03-briefing-pack-first.md) | solid | published |
| 4 | [Zero-Token Hooks](04-zero-token-hooks.md) | works-but-founder-scale | published |
| 5 | The Two-Phase Exit | solid | coming |
| 6 | Backstop at Birth | solid | coming |
| 7 | Ask It to Die | fragile | coming |
| 8 | Successor Before Corpse | works-but-founder-scale | coming |
| 9 | The Close Record | solid | coming |
| 10 | The Policy-Gated Sweep | fragile | coming |

See the full [pattern index](../../INDEX.md) for every chapter.
