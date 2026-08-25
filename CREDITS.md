# Credits and prior art

This system borrows liberally and credits deliberately. This document names the ideas, projects, and
platforms the work drew from, and points you at what to go reuse directly. Where a famous parallel
was tested and no evidence of copying was found, that is said plainly rather than glossed.

The word "pattern language" is used in the Christopher Alexander sense, and the entry shape (name,
forces, consequences, "steal this") follows the Gang of Four. Those two are the lineage of the form
itself.

## Direct borrowings

Ordered by how load-bearing the borrowing is.

1. **Claude Code: Agent Skills, subagents, hooks, and the `CLAUDE.md` memory hierarchy** - Anthropic.
   The whole pattern layer is expressed inside Anthropic's extension primitives: the
   progressive-disclosure skill format, subagent fan-out with per-agent model selection, hooks as
   deterministic gates, and the tiered memory hierarchy. Docs: `code.claude.com/docs/en/skills`,
   `.../sub-agents`, `.../hooks`, `.../memory`.
2. **superpowers** - Jesse Vincent (obra), MIT. The plan-and-execute discipline and the
   spec-then-plan layout. `github.com/obra/superpowers`.
3. **The "Ralph" autonomous loop** - Geoffrey Huntley, 2025. The keep-looping-until-it-converges
   technique. `ghuntley.com/ralph`.
4. **i-have-adhd** - ayghri, MIT. The base of the operator communication contract.
   `github.com/ayghri/i-have-adhd`.
5. **Correction of Error (COE) and 5 Whys** - Amazon; Sakichi Toyoda / Taiichi Ohno. A blocking
   root-cause gate: the COE artifact is a precondition for closing a fix.
6. **Working Backwards / PR-FAQ, tenets, and the Principal Engineer operating model** - Amazon;
   documented by Colin Bryar and Bill Carr, *Working Backwards* (2021).
7. **WSJF** - Don Reinertsen, *The Principles of Product Development Flow* (2009); as framed by SAFe.
8. **The "lethal trifecta" framing** - Simon Willison, 2025. The threat model for any agent with
   private data, tool access, and untrusted input. `simonwillison.net/2025/Jun/16/the-lethal-trifecta/`.
9. **Queue-lease mechanics** - AWS SQS visibility timeout and dead-letter queues; BullMQ
   `lockDuration` / `maxStalledCount`.
10. **The transactional outbox pattern** - Chris Richardson (microservices.io); AWS Prescriptive
    Guidance.
11. **Dead-man switches / heartbeat-absence monitoring** - healthchecks.io (BSD, self-hostable).
12. **Cloudflare's documented D1 to R2 backup workflow** - Cloudflare.
13. **AIMD (additive increase / multiplicative decrease)** - Chiu and Jain (1989); Van Jacobson
    (1988). TCP congestion control, reused to pace an expensive periodic check.
14. **Kubernetes Lease API and the Consul/Serf split** (gossip for detection, one store for
    decisions) - Kubernetes; HashiCorp.
15. **GitOps continuous reconciliation** - Argo CD / Flux. The model was borrowed; the tools were
    deliberately not adopted for a small fleet.
16. **Anthropic Programmatic Tool Calling** - replicated to keep raw web content out of the model's
    context window.
17. **Anthropic's prompt-engineering guidance** - Anthropic.
18. **n8n's deterministic agent template** - the prescript/postscript sandwich around a
    non-deterministic step.
19. **Matt Pocock's engineering skills** ("Skills for Real Engineers"), MIT.
    `github.com/mattpocock/skills`.
20. **The MemGPT / Letta memory-hierarchy line** - evaluated, then deliberately rejected in favor of
    markdown plus git plus an index.

## Platform dependencies

Cloudflare (Workers, D1, R2, Queues, Vectorize, Workers AI, Durable Objects), the Telegram Bot API,
tmux, Tailscale, the `gh` CLI, Doppler, Tavily, n8n, and BGE embeddings (`bge-base-en-v1.5`, BAAI).
These are stood on rather than borrowed from.

## Convergent evolution (arrived at independently, credited anyway)

Erlang/OTP supervision trees and "let it crash" (Joe Armstrong; Ericsson); crash-only software
(Candea and Fox); the Contract Net Protocol (Reid Smith, 1980); leases for cache consistency (Gray
and Cheriton, 1989); event sourcing and CQRS (Fowler; Greg Young); Google SRE practice (error
budgets, blameless postmortems, the four golden signals, toil, SLO/SLI); the Toyota andon cord and
kanban; blackboard architectures (Hearsay-II); and the circuit breaker (Michael Nygard, *Release
It!*). None of these show internal evidence of copying; several were reached empirically and have
decades of theory the system does not.

## Reuse pointers

What an outside team should grab, and from where. Most point upstream, which is the right answer
anyway: go get the original.

| If you want | Grab | From |
|---|---|---|
| Plan-and-execute discipline for agent work | **superpowers** (MIT) | `github.com/obra/superpowers` |
| The autonomous converge-until-done loop | **the Ralph loop** (it is one line of bash) | `ghuntley.com/ralph` |
| Issue-tracker-as-agent-substrate and Socratic pre-spec interviewing | **Matt Pocock's "Skills for Real Engineers"** (MIT) | `github.com/mattpocock/skills` |
| A multi-reviewer convergence loop you can run today | **`ai-review-toolkit`** (qreview / qloop / qpipeline) | `github.com/sparkst/sparkry-claude-skills` |
| A communication contract readable for an ADHD/AuDHD operator | **`ayghri/i-have-adhd`** for the base rules | `github.com/ayghri/i-have-adhd` |
| The threat model for any agent with data, tools, and untrusted input | **the lethal-trifecta framing** | `simonwillison.net/2025/Jun/16/the-lethal-trifecta/` |
| Queue-lease mechanics without adopting a broker | **SQS visibility timeout + DLQ**, **BullMQ** stalled-job docs | AWS SQS docs; `docs.bullmq.io` |
| Guaranteed delivery on a free-tier budget | **the transactional outbox pattern** | microservices.io / AWS Prescriptive Guidance |
| Alerting on jobs that never ran | **healthchecks.io** (BSD, self-hostable) | `healthchecks.io` |
| Backing up Cloudflare D1 to R2 | **Cloudflare's own documented workflow** | `developers.cloudflare.com/workflows/examples/backup-d1` |
| Pacing an expensive periodic check | **AIMD** (additive increase, multiplicative decrease) | Chiu and Jain 1989 / Jacobson 1988 |
| A liveness/lease object decoupled from status reporting | **Kubernetes `coordination.k8s.io` Lease API** + KEP-589 | `kubernetes.io/docs/concepts/architecture/leases` |
| Continuous reconciliation without Kubernetes | **the Argo CD / Flux model** | Argo CD / Flux docs |
| Keeping raw web content out of an agent's context window | **Anthropic's Programmatic Tool Calling** | `platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling` |
| Agent memory at personal/team scale | **markdown + git + an index**; read Letta's own filesystem benchmark first | `letta.com/blog/benchmarking-ai-agent-memory/`; `github.com/basicmachines-co/basic-memory` |
| A blocking root-cause gate | **COE + 5 Whys** as a precondition for closing a fix | Amazon COE guidance; Toyota 5 Whys |
| Deterministic wrappers around non-deterministic steps | **n8n's agent template** (validate-in, validate-out) | `n8n.io` |

## Sources

All URLs verified 2026-08-20. Books and pre-web papers are cited rather than linked.

### Platform and tooling

| Source | Author / org | URL | License |
|---|---|---|---|
| Claude Code: Skills, subagents, hooks, MCP, permissions, memory | Anthropic | `code.claude.com/docs/en/skills` and sibling pages | proprietary product |
| Programmatic Tool Calling | Anthropic | `platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling` | proprietary |
| Model Context Protocol | Anthropic (David Soria Parra, Justin Spahr-Summers) | `modelcontextprotocol.io` | MIT |
| Official Claude Code plugin marketplace | Anthropic | `github.com/anthropics/claude-plugins-official` | Apache-2.0 |
| superpowers | Jesse Vincent (obra) | `github.com/obra/superpowers` | MIT |
| Matt Pocock's skills | Matt Pocock | `github.com/mattpocock/skills` | MIT |
| i-have-adhd | ayghri | `github.com/ayghri/i-have-adhd` | MIT |
| Cloudflare Workers / D1 / R2 / Queues / Vectorize / Workers AI / Durable Objects | Cloudflare | `developers.cloudflare.com` | proprietary platform |
| D1 to R2 backup workflow example | Cloudflare | `developers.cloudflare.com/workflows/examples/backup-d1` | docs |
| BGE embeddings (`bge-base-en-v1.5`) | BAAI | `huggingface.co/BAAI/bge-base-en-v1.5` | MIT |
| Tavily | Tavily | `tavily.com` | commercial API |
| Doppler | Doppler | `doppler.com` | commercial |
| n8n | n8n GmbH | `n8n.io` | Sustainable Use License (fair-code; not OSI open source) |
| tmux | Nicholas Marriott | `github.com/tmux/tmux` | ISC |
| Tailscale | Tailscale Inc. | `tailscale.com` | client BSD-3-Clause; backend proprietary |
| healthchecks.io | Pēteris Caune | `healthchecks.io/about` | BSD (self-hostable) |
| Telegram Bot API | Telegram | `core.telegram.org/bots/api` | platform API |
| `gh` CLI | GitHub | `cli.github.com` | MIT |

### Practice, patterns, and papers

| Source | Originator / year | Reference |
|---|---|---|
| The Ralph loop | Geoffrey Huntley, 2025 | `ghuntley.com/ralph` |
| Lethal trifecta | Simon Willison, 2025 | `simonwillison.net/2025/Jun/16/the-lethal-trifecta/` |
| Correction of Error (COE) | Amazon / AWS | `aws.amazon.com/blogs/mt/creating-a-correction-of-errors-document` |
| 5 Whys | Sakichi Toyoda / Taiichi Ohno | Ohno, *Toyota Production System*, 1988 |
| Working Backwards / PR-FAQ | Amazon; Bryar and Carr | *Working Backwards*, 2021 · `workingbackwards.com` |
| WSJF | Don Reinertsen, 2009 | `framework.scaledagile.com/wsjf` |
| Google SRE (error budgets, postmortems, golden signals, toil, SLO/SLI) | Google SRE | `sre.google` |
| Erlang/OTP supervision, "let it crash" | Ericsson; Joe Armstrong (PhD thesis, 2003) | `erlang.org/doc/system/design_principles.html` |
| Crash-only software | Candea and Fox, 2003 | `usenix.org/events/hotos03/tech/candea.html` |
| Actor model | Hewitt, Bishop, Steiger, 1973 | IJCAI'73, pp. 235-245 |
| Event sourcing; CQRS | Martin Fowler; Greg Young | `martinfowler.com/eaaDev/EventSourcing.html`; `martinfowler.com/bliki/CQRS.html` |
| Transactional outbox | Chris Richardson | `microservices.io/patterns/data/transactional-outbox.html` |
| AIMD | Chiu and Jain, 1989; Van Jacobson, 1988 | *Computer Networks and ISDN Systems* 17(1); ACM SIGCOMM '88 |
| Contract Net Protocol | Reid G. Smith, 1980 | *IEEE Transactions on Computers* C-29(12) |
| Leases (cache consistency) | Gray and Cheriton, 1989 | 12th ACM SOSP |
| Kubernetes Lease API; KEP-589 | Kubernetes | `kubernetes.io/docs/concepts/architecture/leases` |
| GitOps | Alexis Richardson, Weaveworks, 2017 | `fluxcd.io/flux/concepts`; `argo-cd.readthedocs.io` |
| SQS visibility timeout + DLQ | AWS | AWS SQS docs |
| BullMQ stalled jobs | Taskforce.sh | `docs.bullmq.io` |
| Circuit breaker | Michael T. Nygard, *Release It!*, 2007 | `martinfowler.com/bliki/CircuitBreaker.html` |
| MemGPT | Packer et al., 2023 | `arxiv.org/abs/2310.08560` |
| Letta filesystem-memory benchmark | Letta | `letta.com/blog/benchmarking-ai-agent-memory/` |
| basic-memory | Basic Machines | `github.com/basicmachines-co/basic-memory` |
| OWASP Top 10 | OWASP Foundation | `owasp.org/www-project-top-ten/` |

### Sparkry's own public artifact

`github.com/sparkst/sparkry-claude-skills` is the public plugin bundle, including `ai-review-toolkit`
(qreview / qloop / qpipeline), `qralph`, `coe-workflow`, `dev-workflow`, `research-workflow`,
`writing-workflow`, and `strategy-workflow`.
