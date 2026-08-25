# The pattern index

All 111 patterns, in 14 chapters. Each line gives the pattern, its one-line essence, an honest maturity verdict, and whether it is published yet.

Maturity is verbatim-honest: `solid` (tested, holds up), `works-but-founder-scale` (works today, would strain at 10x), `fragile` (known to break, kept with eyes open), `mixed` (solid in one part, softer in another), `designed-not-built` (specified, not yet running). A `cross-reference` entry points to the full pattern in another chapter.

Status is `published` (the full entry is in this repo now) or `coming` (essence and maturity here; the full entry lands on the weekly cadence in [NEXT.md](NEXT.md)).

## Chapter 1 - Session Birth and Death

See [chapters/01-session-birth-and-death/README.md](chapters/01-session-birth-and-death/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | [The Orientation Charter](chapters/01-session-birth-and-death/01-the-orientation-charter.md) | Treat the opening prompt as a versioned build artifact, not a message someone types. | solid | published |
| 2 | [Proof-of-Delivery Paste](chapters/01-session-birth-and-death/02-proof-of-delivery-paste.md) | Never treat "the command exited 0" as proof a brief was delivered or submitted. | works-but-founder-scale | published |
| 3 | [Briefing Pack First](chapters/01-session-birth-and-death/03-briefing-pack-first.md) | Make orientation a gathered artifact, read and reported on before any scope talk. | solid | published |
| 4 | [Zero-Token Hooks](chapters/01-session-birth-and-death/04-zero-token-hooks.md) | What the opening of a session must guarantee belongs in a process hook, not in the instructions. | works-but-founder-scale | published |
| 5 | The Two-Phase Exit | Split an irreversible close: a read-only phase mints a short-lived token, the irreversible step refuses without it. | solid | coming |
| 6 | Backstop at Birth | Pair every model-driven close-out with a deterministic zero-token backstop wired in at launch. | solid | coming |
| 7 | Ask It to Die | To end a session you do not own, inject the close command so its own model runs the close-out. | fragile | coming |
| 8 | Successor Before Corpse | The predecessor's death is the last step, gated on proof the successor is alive and oriented. | works-but-founder-scale | coming |
| 9 | The Close Record | Emit a machine record and a human record on the transaction that closes the session. | solid | coming |
| 10 | The Policy-Gated Sweep | Drive agent self-cleanup from a declarative policy with three authority levels and proof of ownership. | fragile | coming |

## Chapter 2 - Fleet Memory

See [chapters/02-fleet-memory/README.md](chapters/02-fleet-memory/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | One Fact, One File | Make every durable fact its own small file with machine-readable frontmatter, and make the index a router of one-line hooks rather than a summary. | works-but-founder-scale | coming |
| 2 | Supersede, Never Delete | Treat obsolescence as a first-class field on the record and enforce it in the retrieval path, not in the reader's attention span. | solid | coming |
| 3 | Recall Before You Assert | Put the knowledge base behind a two-verb retrieval API instead of in the prompt, keeping the files authoritative and the index strictly derived. | works-but-founder-scale | coming |
| 4 | The Memory Cascade | Give shared agent memory tiers with explicit precedence, a written cap per tier, and a validating writer that refuses rather than half-writes. | works-but-founder-scale | coming |
| 5 | The Compaction Survival Kit | Separate what the agent controls (writing irreplaceable state down as it happens) from what it does not (when the context is reclaimed), then re-inject a tailored digest. | solid | coming |
| 6 | The Append-Only Ledger | For a log a formatting hook, another agent, or a crash could touch, ship a purpose-built appender and forbid the general-purpose edit path outright. | solid | coming |
| 7 | Leaderless Sync | For append-mostly shared state written by many uncoordinated writers, prefer partitioning and staggering over locking, then resolve the remainder additively. | works-but-founder-scale | coming |
| 8 | The Pinned Reconciler | Any job that can mass-delete derived state needs a trust anchor outside its blast radius, preconditions that fail closed, and separate overrides per failure class. | fragile | coming |

## Chapter 3 - Watching the Fleet

See [chapters/03-watching-the-fleet/README.md](chapters/03-watching-the-fleet/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | The Poll Is the Pulse | Make liveness a byproduct of the work-fetch path, so the signal cannot outlive the thing it measures. | solid | coming |
| 2 | Named Failure Classes | Split "unhealthy" into named classes whose boundaries are provability boundaries, not severity boundaries. | solid | coming |
| 3 | Ride the Live Wire | Ship new detection into an already-plumbed alert channel, and pay for it with a strict row contract. | works-but-founder-scale | coming |
| 4 | One Verdict Authority | When N stores hold partial truth about one entity, build one arbiter that ranks evidence by directness of observation and fence its writes with an epoch. | solid | coming |
| 5 | Census First | One deterministic gather returns a typed envelope, the pass/fail rule rides inside it as an exit code, and the agent triages only from the envelope. | solid | coming |
| 6 | Armed Watchers | Every watcher must speak on failure, emit deltas, and be registered in durable storage a fresh context can read. | works-but-founder-scale | coming |
| 7 | The Diagnostic Ladder | Severity-inverted diagnosis tiers, one shared envelope, read-only at every level, with the model tier's limits enforced by the harness. | solid | coming |
| 8 | Two-Ledger Escalation | Automatic escalation needs two counters with different lifetimes: an episode ledger recovery clears, and an attempts ledger recovery does not. | solid | coming |
| 9 | The Hourly Mirror | One declarative desired-state manifest, one audit per node per hour, one JSON report, with other periodic reconciliation piggybacked on the same beat. | solid | coming |
| 10 | Velocity Rungs | A threshold alert needs a freshness gate on the measurement itself, a rate rung with a clamped interval, and an ack that kills the page but not the row. | solid | coming |
| 11 | Name Your Blind Spots | Enumerate in writing the failure modes your monitoring shape cannot express, because a system that does not list its blind spots reports green over them. | mixed | coming |

## Chapter 4 - Structured Payloads

See [chapters/04-structured-payloads/README.md](chapters/04-structured-payloads/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Ask as Untrusted File | Text destined for another process crosses the boundary as a file path, never as an inline argument. | solid | coming |
| 2 | Degraded Means Unknown | Give each failure-prone source its own ok and error inside one schema-versioned document. | solid | coming |
| 3 | The Hand-off Ladder | Rank inter-agent channels by verifiability; never let the cheapest one carry something alone. | solid | coming |
| 4 | The Close Report Shape | A report to someone who was not watching needs a fixed, restated-from-scratch shape behind an evidence gate. | solid | coming |
| 5 | The AuDHD Brief | One reply-shape contract governs every output; channel rendering is a separate layer. | mixed | coming |

## Chapter 5 - Grading the Models

See [chapters/05-grading-the-models/README.md](chapters/05-grading-the-models/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | The Grading Table | Grade work by whether it needs judgment or only execution against a fixed rubric, and route the model tier from that. | solid | coming |
| 2 | Explicit Model or Bust | Never let a child agent inherit its parent's model; every fan-out call site names its own tier. | works-but-founder-scale | coming |
| 3 | The Standdown Lever | Default the scarce frontier tier off for autonomous use, and lift it only by a written, build-scoped owner mandate. | designed-not-built | coming |
| 4 | Difficulty-Split Extraction | Route batch items to tiers using a cheap structural signal available before the expensive call. | works-but-founder-scale | coming |
| 5 | Haiku on the Heartbeat | A probe whose output is pass or fail should be pinned to the cheapest model, by a named constant, with its argv locked by a test. | solid | coming |

## Chapter 6 - The Quota Pool

See [chapters/06-the-quota-pool/README.md](chapters/06-the-quota-pool/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Pooled Identities | Multiply a hard per-subscription ceiling by pooling several real identities, each isolated in its own credential directory. | solid | coming |
| 2 | Refuse, Don't Redirect | When a request would breach a hard threshold or an active operator override, return a typed refusal instead of quietly substituting another resource. | solid | coming |
| 3 | Headroom-First Placement | Rank identities by remaining headroom on the fastest-draining meter first, then have the allocator write its choice back onto the request. | works-but-founder-scale | coming |
| 4 | The Cordon | Keep a governance override channel beside the numeric gate, but an override that never reaches the allocator's code path is not governance. | fragile | coming |
| 5 | The Honest Inert Reserve | Ship policy logic ahead of the data feed that activates it, with an explicit commented seam, so the gap is legible instead of silent. | designed-not-built | coming |
| 6 | Presence Is Not Validity | A "logged in" flag is not proof a credential works; prove it with a bounded round-trip, classify the failure, and cache by verdict. | solid | coming |

## Chapter 7 - Handling Hosts

See [chapters/07-handling-hosts/README.md](chapters/07-handling-hosts/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Host Roles | Encode machine roles as a fixed enum and make placement a pure function of that enum plus live load, with auto-placement seeing only the fungible tier. | solid | coming |
| 2 | Node Descriptors | One machine-readable descriptor per host, parsed identically by every consumer, and only as trustworthy as its provenance. | fragile | coming |
| 3 | The Encrypted Tier | When key material exists on only some hosts, enforce the affinity at the call site, and give that work's record its own content tier. | works-but-founder-scale | coming |
| 4 | Health on the Heartbeat | Ride an existing cheap beat with bounded probes that degrade to null, and carry one prior sample forward to turn a snapshot into a rate. | solid | coming |
| 5 | Platform Asymmetry Is a Constraint | A script proven in an interactive shell is not proven under a daemon's stripped PATH or a non-interactive ssh session. | solid | coming |
| 6 | Stray Hunting | A registry sweep cannot find what the registry never learned about, so enumerate the OS's ground truth and cross-reference. | solid | coming |

## Chapter 8 - Counting the Tokens

See [chapters/08-counting-the-tokens/README.md](chapters/08-counting-the-tokens/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Cost at Close-Out | Force a structured cost document out of every unit of agentic work at its end of life, and make unknown cost null rather than an average. | works-but-founder-scale | coming |
| 2 | Quota-Routed Placement | Treat quota consumption as a live routing input, not an after-the-fact report. | solid | coming |
| 3 | The Escalating Healer | Escalate model tier and spend allowance together, and bound the loop with several independent circuit breakers rather than one retry count. | mixed | coming |
| 4 | Write Down What It Cost | When a pipeline has a real per-run cost, record the observed number next to its own documentation, tied to the input size that produced it. | works-but-founder-scale | coming |
| 5 | Context Is Money | Bound what loads automatically, push expensive reading into subagents, and give a long-running session a self-preservation threshold. | mixed | coming |
| 6 | Secrets Are the Agent's Job | Credential lifecycle work belongs entirely to the agent, never round-tripped through a human. | designed-not-built | coming |

## Chapter 9 - The Supervisor Chain

See [chapters/09-the-supervisor-chain/README.md](chapters/09-the-supervisor-chain/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | One Build, One Supervisor, One Death Date | Give each unit of autonomous work one manager, born for that work and destroyed with it. | solid | coming |
| 2 | Preflight Before Spawn | Run a bounded admission check against live resource state, then hand its verdict to the agent you spawn. | solid | coming |
| 3 | The Scope Line | Make scope a posted three-field artifact with an explicit lock event and a cheap deflection channel. | works-but-founder-scale | coming |
| 4 | Silence Is Not Success | Treat quiet as an unproven state: arm something that speaks on failure before the wait begins. | solid | coming |
| 5 | Verified Delivery Everywhere | Rank channels by measured delivery rate and require an independent probe at every process boundary. | solid | coming |
| 6 | The Reviewer Merges | Separate approval authority from the context that produced the work, then give the approver the terminal action. | solid | coming |
| 7 | Single Actor | Every shared operation that cancels or supersedes gets one named owner; everyone else observes and requests. | solid | coming |
| 8 | Receipts or It Didn't Happen | Done means a third party can point at an artifact, and which artifacts count is declared before work starts. | works-but-founder-scale | coming |
| 9 | Status Is a Script | Answer the most-asked question with a deterministic renderer over the agent's own durable log. | solid | coming |
| 10 | The Triage Ladder | Agents get stuck in their interface, not just their reasoning: observe, classify, one recipe per class. | works-but-founder-scale | coming |

## Chapter 10 - Review and Quality

See [chapters/10-review-and-quality/README.md](chapters/10-review-and-quality/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | The Clean-Context Panel | Get diversity from N context-isolated reviewers, then merge their findings with deterministic code. | solid | coming |
| 2 | The Convergence Loop | Put the stopping rule, the completeness gate, and the give-up condition in code the agents cannot argue with. | works-but-founder-scale | coming |
| 3 | The Review Ledger | A loop of stateless reviewers needs an external append-only memory or it oscillates instead of converging. | designed-not-built | coming |
| 4 | Budget the Rounds | Convergence is a property of small artifacts, so on a large one set the round budget before you start. | works-but-founder-scale | coming |
| 5 | Fresh-Eyes Verification | Ask whether the artifact meets its criteria and whether its claims are true, in an agent that never saw the loop. | solid | coming |
| 6 | The Adversarial Council | For artifacts with no oracle, manufacture disagreement structurally instead of hoping for it. | solid | coming |
| 7 | The Independent Gate | Generate the reviewer's brief rather than improvising it, and back its authority with a guard that refuses anything red. | solid | coming |
| 8 | Converge Before You Publish | While one process is still improving an artifact, keep it out of the shipping process's field of view. | fragile | coming |
| 9 | The Judgment Ladder | Split delegated judgment into three instruments, and let the automated gate veto but never authorize. | works-but-founder-scale | coming |
| 10 | TDD Vertical Slices | One behavior, one test, one implementation, each cycle informed by what the last one taught. | works-but-founder-scale | coming |
| 11 | The Advisory Bell | Surface standing review requirements in the tool loop, and go advisory when the trigger is a heuristic. | solid | coming |

## Chapter 11 - Operating the Machine

See [chapters/11-operating-the-machine/README.md](chapters/11-operating-the-machine/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Pull Convergence with Receipts | Make each node pull itself to the declared tip on a short timer, and treat the node's own posted receipt, not the operator's exit code, as the evidence of liveness. | solid | coming |
| 2 | Content-Addressed Bundles | Separate assembling a content-addressed artifact set from installing one, and forbid the installer from knowing how the payload arrived. | solid | coming |
| 3 | Migration-Guarded Deploys | When a deploy has a second mandatory step, make the two one command and make every "cannot verify" a refusal. | solid | coming |
| 4 | The Merge Gate | When the actors are agents, put the policy check at the tool-call boundary and match on the command about to run. | works-but-founder-scale | coming |
| 5 | THE GATE | Encode "every component must carry capability X" as a data-driven registry plus one pure rule engine, and make touching an unregistered component the trigger. | works-but-founder-scale | coming |
| 6 | Desired-State Parity | Write desired state as data with an explicit class per element, separate observing drift from fixing it, and gate fixing behind a closed allowlist. | works-but-founder-scale | coming |
| 7 | The Project Manifest Standard | Split a project's self-description into a machine-owned layer, a model-written layer, and a human-pinned layer, with a hook that can invalidate but never certify the second. | works-but-founder-scale | coming |
| 8 | The Sudo Broker | Replace a broad privilege grant with one root-owned, non-editable broker exposing a closed set of verbs, each validating its arguments before any privileged call. | solid | coming |
| 9 | The Ownership Map | When more than one delivery mechanism exists, make "which one owns this path" a checked-in, exhaustive, non-overlapping map, and make an unmatched path a build error. | solid | coming |

## Chapter 12 - Sidecars and Leases

See [chapters/12-sidecars-and-leases/README.md](chapters/12-sidecars-and-leases/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | The Sidecar in the Next Pane | To give an interactive process a remote channel without owning its code, run a companion inside the same OS-level lifecycle container and read the artifact it already writes. | solid | coming |
| 2 | The Lane Lease | Model exclusive ownership of a singleton resource as a leased row keyed by the resource, and make takeover unconditional and audited rather than consensual. | solid | coming |
| 3 | Liveness Is Not the Lease | A heartbeat proves the heartbeater is alive; demand instead the cheapest signal the real work cannot avoid producing. | solid | coming |
| 4 | Dead Sidecars Stay Dead | A process may not be its own supervisor; put restart authority in something longer-lived, and make the decision cause-agnostic. | works-but-founder-scale | coming |
| 5 | The Authority/Transport Split | When a control-plane endpoint is too expensive to poll, separate the two jobs it was doing, carrying data and proving liveness, and move only the data. | works-but-founder-scale | coming |
| 6 | The Verified Inject | Treat "I sent it" and "it was accepted" as different claims, and decide ambiguous cases by asking which error is recoverable. | works-but-founder-scale | coming |
| 7 | Watch the Webhook | Monitor the edge you do not own, and design the alert rule around the provider's real data semantics. | solid | coming |
| 8 | Leases per Kind | Give every queued unit a lease with a TTL sized to silence rather than duration, and cap retries per work type by whether replaying that type is safe. | solid | coming |

## Chapter 13 - The Operator Experience

See [chapters/13-the-operator-experience/README.md](chapters/13-the-operator-experience/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | The Command Seat | One high-trust operator seat that reaches every actuator directly, builds nothing itself, and changes its verbosity depending on which screen is reading it. | solid | coming |
| 2 | Persona Is Voice, Never Process | A persona is a bounded skin over one invariant message structure; it may add a declared process step, never restyle the information architecture. | mixed | coming |
| 3 | One Lane per Workstream | A fixed pool of named identities, each leased 1:1 to one live workstream, with wrong claimants refused before any resource is committed. | solid | coming |
| 4 | The Phone-First Brief | Treat screen size, interruption rate, and the transport's real formatting support as inputs to a rendering contract implemented as pure functions plus a linter. | solid | coming |
| 5 | Quiet Cadence | Prove liveness with a cheap, bounded, self-decaying transport signal; report progress under a separate, explicitly budgeted content policy. | solid | coming |
| 6 | Slash Commands Everywhere | Reuse one command surface across a rich terminal and a constrained chat client by making dispatch identical, and invalidate anything that caches the command set. | works-but-founder-scale | coming |
| 7 | The LCARS Board | A live operator console is a thin, read-mostly rendering layer over independent polls, with every write routed through the queue the CLI uses. | solid | coming |
| 8 | Fleet Eyes | Fetch the health payload exactly once, then synthesize it into a fixed-shape triage brief where every item lands in exactly one priority bucket. | solid | coming |

## Chapter 14 - Trust Boundaries

See [chapters/14-trust-boundaries/README.md](chapters/14-trust-boundaries/README.md) for the chapter diagram and intro.

| # | Pattern | Essence | Maturity | Status |
|---|---------|---------|----------|--------|
| 1 | Everything Inbound Is Data | Name every inbound channel as untrusted at one authored rule, and have every consumer point back to that rule instead of restating it. | solid | coming |
| 2 | Draft-Only Outbound | Split "produce the artifact" from "make it irreversible," and make the second step demand a fresh, non-inferred human trigger captured at the tool boundary. | solid | coming |
| 3 | Read-Only by Default | Default every autonomous write to "ask a human," then open exactly as many auto-approved exceptions as carry a machine-checkable safety proof. | works-but-founder-scale | coming |
| 4 | The Sanitizer Chain | Chain narrow, independent defenses across the trust boundary: normalize, score, allowlist, latch, and funnel every send through one path. | solid | coming |
| 5 | Secrets to the Vault | One store is the only place a secret is read from, the agent owns getting it there and purging every other copy, and verification happens by comparison, never by printing. | solid | coming |
| 6 | The Sudo Broker | See Chapter 11, pattern 8: one root-owned, operator-unwritable broker with a hardcoded verb list, argv-not-shell argument passing, and a reset PATH is the trust boundary for every privileged operation named in this chapter. | cross-reference | coming |
| 7 | Deny Wins | A prefix-glob allowlist is not a verb-scoped grant; where the allow side cannot express the narrower intent, add the missing precision on the deny side. | fragile | coming |
| 8 | Contract-Governed Agents | Give every autonomous unit a machine-checked capability declaration validated before it runs, and pair the static contract with runtime leak detection. | works-but-founder-scale | coming |

---

Published: 4 of 111. The rest arrive one pattern a week, newest at the top of [NEXT.md](NEXT.md).
