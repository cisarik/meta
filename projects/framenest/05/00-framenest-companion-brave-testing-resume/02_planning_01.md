# FrameNest — Planner continuation prompt (companion history correction, amendment R3′)

Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: on (Plan Mode; no filesystem writes anywhere)
Worker session profile: Fresh Planner (bounded continuation of your healthy session)
Phase: planning
Reasoning recommendation: High (per-identity open-state persistence is a durable-data design decision)
Task identity: FRAMENEST-COMPANIE-HISTPLAN-02
Continuity anchor: your terminal planning output for FRAMENEST-COMPANIE-HISTPLAN-01, archived verbatim by ORCHESTRATOR as `/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/02_report_00.md`
Authority renewal: that output terminated your prior authority. This exchange renews PLANNING-only authority to the exact same healthy session to fold one Cooperator amendment into your plan. Retained context is convenience, not authority. Re-gate repository facts you rely on. Stop on conflict between retained context and current repository evidence.
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report (return full updated plan in chat; ORCHESTRator archives it as 02_report_01.md)
Trace self-granted status: none

## The amendment (authoritative Cooperator decision, 2026-08-26)

R3 is amended to **R3′**. Verbatim intent: the ordinary user gets their own
history too — it is NOT the analyzed-only history like admin has, but their
own saves — and they get badge and highlighting ONLY when an item passes
analysis.

Concretely:

1. Ordinary own-history still lists ALL own saves (any analysis state),
   requester-private, movie-excluded — unchanged from your plan.
2. Analyzed items inside ordinary own-history NOW participate in the
   unopened/badge/accent lifecycle: unopened analyzed row → `--unopened`
   accent + counts toward the toolbar badge; single click opens iframe and
   clears that row’s unopened state and decrements the badge. Pending rows
   stay plain, never counted, never POST `opened`.
3. This supersedes your prior table rows “`unopened` always false;
   `unopened_count` always 0 | never” for the ordinary audience.

## What you must now design (the deep part — think it through fully)

A. **Per-identity open-state persistence.** Today `companion_review_open_states`
(migration 0031) persists opened per `analysis_run_id`. Under R3′ both admin
(global pool) and each ordinary user (their own items) track opened
independently: Alice opening an item must NOT clear Bob’s accent/badge, and
admin opening must not clear an ordinary user’s. Inspect the 0031 table shape
and decide exactly: extend with a login-key/identity dimension, separate
table, or another bounded mechanism. If a schema migration is required,
design migration **0034** (additive, reversible downgrade, consistent with
the repository’s migration discipline) — migrations are now IN scope for
this slice. State the exact DDL-level intent, upgrade/downgrade behavior,
and which existing rows must be preserved/backfilled (existing admin open
states map to the admin identity; no ordinary backfill exists).

B. **Badge sources.** Admin badge remains `unopened_count` over the global
analyzed pool filtered to admin’s own open-state view. Ordinary badge =
`unopened_count` over OWN cataloged analyzed items under THEIR open-state
view. Specify payload changes for `/api/companion/review-inbox` and the new
`GET /api/companion/own-history` (`unopened`, `unopened_count`, row accent
inputs), plus extension routing/badge refresh updates for the ordinary path.

C. **Capability gate for `opened` POST from ordinary users.** Today opened
is admin-gated. Under R3′ an ordinary user must be able to mark THEIR OWN
item opened. Decide: widen the existing route by ownership check (requester
owns the media AND the analysis run belongs to it) vs a second route.
Preserve: four `companion_mutation` routes exactly (if opened gains ordinary
callers it stays the SAME route), allowlist + header rules unchanged for it,
cross-user 403/404 sanitized posture, and admin inbox/opened/apply still
403 for ordinary EXCEPT own-item opened under the narrow ownership rule.

D. **State machine + tests update.** Update the mermaid machine for both
audiences; update the test matrix: per-identity isolation negatives
(Alice/Bob/admin triple), migration 0034 unit tests mirroring the 0033
additive pattern, ordinary opened-own-item positive + cross-user negative,
accent/badge rendering for ordinary analyzed rows, retention of all
previously named suites.

E. **ADR-0076 outline** must now cover per-user unopened semantics and the
0034 migration rationale while superseding ADR-0073 statements without
editing its body.

## Rendered-pass context (classify into parked observations, do not redesign)

Items 7–9 PASS (attach continuity after one transient `composer_unbound`
cold start — park “auto-rebind polish” as an observation; stale-context
reload PASS; disconnect PASS). Item 6 pending-click is superseded by R2
(admin sees no pending). Item 10 is superseded by R3′ itself.

## Output (chat text, not a file)

Return the COMPLETE updated plan — not a diff — in the same structure as
your prior plan (front-matter todos included), beginning exactly:

### Report for ORCHESTRATOR_CHAT

Add a short “Changes from exchange 01” section at top listing exactly what
moved. Keep the Parked list, add: auto-rebind polish; anything new you
parked. Report justification: changed-external-state. Sanitization identical
to exchange 01. End with the authority-expiry statement.

## Stopping rule

Unchanged from exchange 01: stop and return PARTIAL/BLOCKED with the exact
contradiction if repository evidence conflicts with any accepted decision,
including R3′.

## Transition owner

ORCHESTRATOR archives your updated plan, then issues the implementation
prompt. You have no follow-on authority.
