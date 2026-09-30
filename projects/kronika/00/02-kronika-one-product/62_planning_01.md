# S9-R Targeted Planning Revision — Administrator research settings (kronika-one-product, session 62, exchange 02)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 62
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S9-R-REVISION
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — freezing a billing-adjacent, cross-cutting administrator slice on new external evidence
Recommended context capacity: approximately 1M tokens
Independence required: no

## Continuity and authority renewal

```text
Continuity anchor: terminal PARTIAL planning report 62_report_00.md (session 62
  / exchange 01), including its nine repository findings and its escalation
Prior authority expired at that terminal report; this exchange grants only the
  single authorized targeted revision of the same planning question
Evidence posture: non-independent planning; no implementation authority
```

Re-gate the repository before planning: root `/Users/agile/Projects/framenest`,
branch `feat/kronika-one-product`, HEAD
`3bf424586289b500cf45cb0d49676b50d27328fa`, clean index and worktree including
untracked files, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Stop on conflict between retained
context and current repository truth.

## Planning record (targeted revision)

```text
Planning cycle: targeted-revision
Prior planning report: 62_report_00.md (kronika-one-product 62/01)
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: the administrator-selectable model allowlist and the
  required UsagePriceSchedule shape (long-context tier and cache-write
  dimensions) grounded by the new external evidence in 63_report_00.md
Preserved unaffected decisions: no client-supplied model/endpoint/tool fields;
  no automatic fallback; provider/model snapshotted at admission and never
  changed mid-request; research disabled by default; private/family/administrator
  access rules; accepted budgets and limits; one generation attempt per request;
  capture parked; no new framework; testing economy
Automatic targeted revisions used: 1
```

## Plan-to-Execution fields

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: freeze the S9-R administrator research-settings plan grounded in 62_report_00.md and 63_report_00.md
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## New external evidence (binding input)

`63_report_00.md` (WebSearcher, 63/01, PASS; retrieval date 2026-09-30)
establishes the first-party matrix:

- `gpt-5.5-2026-04-23` — input 5,000,000 / cached 500,000 / output 30,000,000
  / web search per thousand 10,000,000 micro-USD; no separate cache-write
  charge.
- `gpt-5.6-sol` — 4,000,000 / 400,000 / 20,000,000 / 10,000,000; cache writes
  at 1.25x uncached input; promotional pricing through at least 2026-11-21.
- `gpt-5.6-terra` — 2,000,000 / 200,000 / 12,000,000 / 10,000,000; cache
  writes at 1.25x.
- `gpt-5.6-luna` — 200,000 / 20,000 / 1,200,000 / 10,000,000; cache writes at
  1.25x.
- All four support the Responses API, the hosted `web_search` tool, both
  `low` and `high` reasoning effort, and 128,000 max output tokens; none is in
  the deprecation register.
- Long-context tier (>272K input tokens) applies 2x input and 1.5x output for
  all four; the current four-rate `UsagePriceSchedule` cannot represent it.
- GPT-5.6 snapshot stability is weaker (no dated snapshot); a dated snapshot
  exists only for `gpt-5.5-2026-04-23`; `gpt-5.5-pro` lacks `low` effort and is
  excluded; `gpt-5.4` is a valid same-family alternative without a
  cache-write charge.
- Unknowns: account-specific access, whether >272K input is reachable in
  practice, whether cache writes occur and how usage reports them, and
  non-first-party price discrepancies.

Bounded resolution allowance: you may perform a small number of read-only
first-party documentation retrievals (no account, no API call, no credential)
solely to resolve the cache-write usage-field question raised as the evidence
report's LEAD (whether provider usage exposes a separate cache-write token
count; the adapter currently reads `cached_tokens`). Record exact URLs and the
retrieval date for anything so fetched; if unresolved, design fail-safe.

## Required revision outcome (decision-complete)

Produce the frozen S9-R plan, incorporating the nine findings in
`62_report_00.md` as binding constraints and deciding explicitly:

1. **Exact file allowlist** (existing/new, verified read-only) for the whole
   slice, including any `UsagePriceSchedule`/accounting extension, the
   configuration/selection changes, the admin API, route policies and the
   access-inventory regeneration, the shell settings surface, tests and the
   documentation update.
2. **Allowlist decision** — the exact set of administrator-selectable models
   and their schedule entries; the default model; per-model snapshot/pinning
   notes; the unknown-model refusal; the recommendation from `63_report_00.md`
   is input, not a decision. Present this as the one Cooperator-confirmable
   product choice with your recommendation (including the cheapest sensible
   option).
3. **Schedule-shape decision** — whether to extend `UsagePriceSchedule` with a
   long-context tier and a cache-write rate (with exact math), or to constrain
   the allowlist/prompt so the four-rate shape suffices; use the permitted
   bounded documentation check; keep accounting fail-closed for every unknown
   and never zero-fill.
4. **Per-request pricing and restart persistence** — accounting resolves from
   the admitted request's model (not one shared schedule), including after a
   restart; state the exact storage/derivation.
5. **Runtime refresh path** — how a saved settings change reaches new
   admissions and capabilities reads without a restart (and how a
   process started with research disabled can become enabled), while
   preserving polling, cancellation and cleanup for existing requests.
6. **Idempotency and history** — replay after a settings change returns the
   original attempt without another generation; disabling must not destroy
   history; the fingerprint semantics are stated explicitly.
7. **Concurrent-save contract** — conflict detection across research and
   media-provider writers that share the configuration file, with the
   preservation assertion stated precisely (not whole-file byte identity).
8. **Admin API contract** — exact routes, methods, payloads, validation,
   `provider.operate` gating plus verified identity, error codes and copy,
   no-store behavior, and the exact budget fields within their bounds.
9. **Shell surface** — the settings UI inside the existing administrator AI
   dialog patterns, states, confirmation semantics, accessibility, and the
   explicit no-client-selection copy.
10. **Tests** — the causal regressions named in `62_report_00.md` plus
    schedule/tier/cache-write math tests; Python contract tests and a
    `node --test` suite; the exact focused route.
11. **Documentation supersession** — the exact new ADR (ADR-0083's Revisit
    Conditions require it for a changed model/budget decision) plus the
    minimal AGENTS/README/PRODUCT/SPEC/SERVER/ROADMAP deltas, separating
    historical wording from current status and using the supplied S8/S9
    evidence.
12. **Acceptance route and first implementation grant** — focused validation,
    one fresh independent audit, publication, routine NUC refresh, Cooperator
    rendered acceptance, and the recommended first implementation grant
    (labelled non-authoritative).

## Boundaries

Read-only planning; the only permitted writes are the report file and trace
output. Small bounded first-party documentation retrievals as authorized
above. No repository mutation, no tests, no server/browser run, no provider
call, no credential handling, no NUC/SSH/sudo, no subagents. Research stays
disabled by default; nothing is enabled by this grant.

## Report contract

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 62, 02), carries the Planning Record
and Plan-to-Execution fields, the complete frozen plan, the single
Cooperator-confirmable allowlist choice with your recommendation, the
proposed first implementation grant, open questions, and the critique. Use
`Phase-qualified result: not-applicable`, `Logical-whole closure: not-closed`,
`Report justification: new-evidence`. Save the report exactly at
`62_report_01.md` if the client permits; read back the full content;
otherwise preserve it in chat and mark the delivery limitation PARTIAL.

## Delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 62_planning_01.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 62_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

A remaining material mapping that cannot be grounded returns
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` (no second revision
exists). Client restrictions that block reading or the report stop for a
completion route.

Authority expiry: the terminal report ends this planning exchange; planning
authority expires; no implementation is authorized.
