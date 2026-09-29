# S8 Planning Grant — Unified Kronika UI/UX (kronika-one-product, session 52)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 52
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S8-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — cross-cutting UI/UX planning over a large existing vanilla-JS shell, several views, and binding access rules; directed as exceptional by the restoration handout
Recommended context capacity: approximately 1M tokens
Independence required: no

## Planning record

```text
Planning cycle: initial
Prior planning report: 25_report_00.md (kronika-one-product 25/01)
Targeted revision basis: none
Changed decision boundary: the S8 unified UI/UX design (shared Timeline landing, personal history, Search and Research forms, administrator review) inside the existing packaged shell over the published S7-P APIs
Preserved unaffected decisions: ADR-0082 and ADR-0083 product decisions (private/family/administrator rules, administrator approval for the shared Timeline, separate personal history, Gallery as a separate working view, research disabled by default, no new framework); the published baseline ade1169…; capture parked; the S9/S10 sequence; testing economy; frozen Gallery/Details behavior
Automatic targeted revisions used: 0
```

## Plan-to-Execution fields

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded implementation planning for the S8 unified Kronika UI/UX inside the existing packaged web shell
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## External trace and delivery record

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
Downloadable prompt filename: 52_planning_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 52_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Accepted context (do not reopen)

- One Kronika on the existing FrameNest base (ADR-0082). Under ADR-0083 the
  Timeline is the main page and contains only administrator-approved records;
  personal history is a separate view; the Gallery remains a separate working
  view with its existing design and player.
- Media enters the shared Timeline only after successful validated analysis and
  administrator approval. Search and Research become personal history when
  their complete results are saved; that completion does not enter the
  Timeline.
- Private by default; verified identity determines ownership; an authenticated
  application administrator can read all product records; ordinary household
  members cannot read another owner's private or unfinished records. Internet
  publication stays disabled.
- Research stays disabled by default; no live provider calls are part of S8;
  generated output remains untrusted.
- Everything through S7-P is implemented, independently audited (`51/01` PASS;
  F01 fixed in `8e5c374`), consolidated, published and deployed. The local
  baseline, public `main` and the NUC web release all equal
  `ade1169b4ba079bb1df540a929572ca58e777d16`; the NUC database is at revision
  `0035`.
- The parked capture module and the parked S3/S5/S7-C work stay untouched.

## Goal (one coherent outcome)

Produce the frozen **S8 unified Kronika UI/UX** implementation plan on the
published `ade1169…` baseline: the shared Timeline landing
(administrator-approved records only), the separate personal-history view,
Search and Research forms, and the administrator review queue, inside the
existing packaged web shell (`src/framenest/adapters/api/web/`), with **no new
framework**, the Gallery kept as a separate working view with the frozen
Gallery/Details behavior, and the existing design language reused.

## Required plan contents (decision-complete)

1. **Exact file allowlist** (new and edited paths), verified read-only against
   the baseline with existing-vs-new status. Keep it minimal; every path must
   be inside the shell, the owning API/application/tailscale modules, targeted
   tests, or named docs — justify any other path explicitly.
2. **Page/route and API mapping** over the existing endpoints listed below.
   State explicitly whether any new HTTP route is needed. If one is, name the
   required `ROUTE_POLICIES` entry in `src/framenest/adapters/api/tailscale_ingress.py`
   (the fallback is fail-closed) and the access-inventory regeneration.
3. **Component and state design** for: the Timeline landing; personal history
   (including unfinished work: pending, failed and cancelled research
   requests); Search and Research submission forms; and the administrator
   review queue (approve/withdraw with `expected_version`). Describe how the
   Timeline becomes the default landing view client-side while the Gallery
   stays reachable and existing deep links keep working, and how loading,
   empty, partial and error states are represented.
4. **Disabled and error UX**: the capability-disabled state rendered from
   `GET /api/research/capabilities` without assuming provider readiness, and
   friendly copy mapped from the stable error codes `E_DISABLED`,
   `E_NOT_CONFIGURED`, `E_BUSY`, `E_IDEMPOTENCY_CONFLICT`, `E_BUDGET_EXCEEDED`,
   `IDENTITY_REQUIRED`, `CAPABILITY_DENIED`, `RECORD_CONFLICT`, `NOT_FOUND`
   (envelope `{"error": {"code": ..., "message": ...}}`).
5. **Accessibility and responsive baseline** consistent with the existing shell
   (skip link, ARIA roles, focus behavior, palette, reduced motion where
   present), without changing the frozen Gallery/Details visuals.
6. **Test matrix** in the existing repository style: Python contract tests for
   route/page and access assertions, plus `node --test tests/*.test.js` for JS
   logic (the tests read the shell sources and execute production functions in
   a `vm` context with stubs). Schedule the thin UI regression harness covering
   at least: Timeline approved-only listing for every caller; personal-history
   separation from the Timeline; research submission idempotency and active
   polling; render embedding; and the approval flow with a stale version. Name
   causal tests, not a broad suite.
7. **Acceptance route**: one fresh independent audit of the exact candidate,
   then Cooperator rendered acceptance on the NUC refreshed to the exact public
   `main` through `deploy/ubuntu/framenest-release` (routine release update).
   State the preconditions for each step.
8. **Recommended first implementation grant**: proposed coordinates and
   profile, `Native planning mode: not-used`, exact baseline `ade1169…`, the
   exact allowlist, positive and negative authority, validation, and stop
   rules. Label this explicitly as a non-authoritative proposal; only a later
   complete Orchestrator grant authorizes execution.
9. **Open Cooperator decisions**: UI copy language (English as today, or
   Slovak) and any branding treatment ("Kronika") in the shell. Present them as
   open decisions with a recommended default, and keep the plan implementable
   under either choice.

## Binding constraints (treat as fixed)

- Private/family/administrator rules per ADR-0083; the Timeline is
  approved-only for every caller, including administrators.
- Approval is `approve`/`withdraw` only and version-checked; a stale
  `expected_version` is a 409 `RECORD_CONFLICT`; never offer `reject` (no
  schema state exists).
- Answer text appears only in record detail and render; list payloads stay
  summary-only as implemented.
- Research is disabled by default; render the capability-disabled state from
  `/api/research/capabilities`; no live provider calls.
- `client_request_id` is generated per form attempt so retries cannot
  double-charge; a 409 `E_IDEMPOTENCY_CONFLICT` means the id was reused with
  different content.
- `consent_version` is required and bounded but not stored; present it as an
  explicit consent acknowledgement.
- Research progress is nudged synchronously by API calls; there is no
  background poller; poll `GET /api/research-requests/{id}` while a request is
  active (a few seconds apart).
- The render response is escaped HTML with `nosniff` and CSP
  `default-src 'none'; style-src 'unsafe-inline'; img-src data:`; embed it in a
  sandboxed iframe, or inject it knowing it is escaped and script-free. Never
  insert untrusted HTML into the main DOM and never auto-fetch cited URLs.
- Any new HTTP route requires a `ROUTE_POLICIES` entry and an access-inventory
  regeneration (`tests/contract/test_kronika_access_inventory.py` rewrites
  `docs/KRONIKA_ACCESS_INVENTORY.md`; the regenerated file is committed).
  Prefer no new route if the existing endpoints suffice.
- No new framework, no new dependency, no test-toolchain change; packaged
  vanilla HTML/CSS/JS assets; `node --test` for JS; Python contract tests on
  the declared AP route; no mass `framenest` → `kronika` rename.
- Gallery/Details MVP visual behavior and the player are frozen unless a
  concrete defect is identified and reported.
- Testing economy is binding: targeted validation; no broad-suite runs at
  every step.

## Available APIs (implemented in S7-P; verify shapes against the code)

```text
GET  /api/research/capabilities            enabled, provider/model, limits, retention notice
POST /api/research-requests                {kind, prompt, client_request_id, consent_version} -> 202 summary
GET  /api/research-requests?limit&offset   own history: items[operation_id, kind, state,
                                           error_code, prompt, created/admitted/submitted/
                                           finished/updated_at_ms, record_id], total
GET  /api/research-requests/{id}           owner/admin; same summary
POST /api/research-requests/{id}/cancel    owner/admin; returns summary
GET  /api/admin/research-requests          administrator inventory
GET  /api/my/records                       own record summaries (record_id, kind, owner,
                                           visibility, timestamps, version, media_id, read_decision)
GET  /api/timeline                         approved records only, same summary shape
GET  /api/records/{id}                     {record, version, document{operation_id, kind,
                                           question_text, citations, timestamps}}
GET  /api/records/{id}/render              escaped HTML, nosniff, restrictive CSP
GET  /api/admin/records                    administrator inventory
POST /api/admin/records/{id}/approval      {action: approve|withdraw, expected_version}
                                           -> {record_id, version, changed}
```

## Mandatory reading

- AP Worker spine: `.ap/AP.md` (Semantic Authority, RF-03, RF-06, RF-12,
  RF-18, RF-19, Stopping Conditions), `.ap/AP_WORKER.md` (Worker Session
  Target, Reporting), `.ap/PROMPT_CONTRACTS.md` (Planning Record,
  Plan-to-Execution Gate, Worker Report Header, Common Worker Task Fields).
- Project: `AGENTS.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md` (Active Kronika
  Sequence, S8 row), `docs/adr/0082-kronika-one-product-and-private-records.md`,
  `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`.
- Trace (read-only, outside the repository):
  `25_report_00.md` sections 5–7 (records, approval, rendering; security and
  required automated evidence; the S8 row), `50_report_00.md` (S7-P result),
  `51_report_00.md` (independent audit, F01), and `33_report_00.md` for the
  expected planning-report form.
- Current shell: `src/framenest/adapters/api/web/index.html`, `styles.css`,
  `app.js` (large; read the navigation, Gallery, Details and admin patterns
  needed to map the new views, selectively).
- APIs and policies: `src/framenest/adapters/api/research_api.py`,
  `records_api.py`, `application.py` (`_read_web_resource`, router
  registration, `build_research_runtime`), `tailscale_ingress.py`
  (`ROUTE_POLICIES`), `docs/KRONIKA_ACCESS_INVENTORY.md`.
- Test style: `tests/contract/test_records_api.py`,
  `tests/contract/test_research_requests_api.py`,
  `tests/contract/test_kronika_access_inventory.py`, and representative JS
  tests `tests/gallery_loading_states.test.js` and
  `tests/metadata_form_contract.test.js`.

## Repository gate (read-only)

```text
Root: /Users/agile/Projects/framenest
Remote: https://github.com/cisarik/framenest.git
Branch: feat/kronika-one-product
Expected HEAD: ade1169b4ba079bb1df540a929572ca58e777d16
Expected tree: f266df7205ddea5b83de7e6cd8313512ce70bcb1
Expected parent: 7be040eb99901d0ae0b1327bb42de614e9192f17
AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Required state: clean index/worktree including untracked files
```

Independently verify all of it before planning. Classify any difference with
the five RF-12 recovery classes; stop on unexplained divergence; preserve owner
work; no fetch, checkout, reset, clean, stash or any Git write. Public `main`
equals the baseline (Orchestrator-observed 2026-09-29 via `git ls-remote`); no
public re-verification is required for planning and no network is authorized.

## Positive authority

Bounded read-only inspection of the named repository, trace and AP files: file
and path reads, `rg`/search, and Git read-only commands (`status`, `log`,
`show`, `diff`, `rev-parse`). In addition, create the complete terminal report
at `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/52_report_00.md`
if and only if that exact file is absent; read back its full content. This
exact file write is the sole exception to read-only planning and is permitted
for PASS, PARTIAL and BLOCKED outcomes when the client permits it. The verified
parent directory already exists; do not create directories.

## Negative authority

No repository, trace, host or external mutation beyond the single report
write. No product or test edits, no new files, no dependency or lockfile
changes, no schema changes, no AP or managed-block changes, no Git writes (no
stage/commit/push), no fetch or network, no test execution, no server or
browser run, no provider calls, no credential or secret handling, no
`private/**`, no NUC/SSH/sudo, no capture state. No subagents.

## Validation

Planning validation is repository-grounded: cite exact file paths and symbols
for every mapping relied on; verify the proposed allowlist read-only against
the baseline (existing vs new); check internal consistency against ADR-0082,
ADR-0083 and the binding constraints; identify contradictions explicitly. Do
not run tests or builds. A client-native plan artifact is not the terminal
Worker report; the report below is.

## Stopping conditions

Stop and report honestly (PARTIAL/BLOCKED) at a failed repository gate, missing
mandatory reading, a client restriction that prevents the required reading or
the report, or an unresolved conflict between the accepted decisions and the
current code that the Orchestrator must decide. Present Cooperator-owned
product questions (copy language, branding) as open questions with recommended
defaults; they authorize no scope change. A remaining material mapping that
cannot be grounded returns `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Completion and report contract

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 52, 01), and carries the compact core:
status; `Phase-qualified result: not-applicable`; start and end commit
`ade1169…` (unchanged); changed files (none in FrameNest; the report file
only); tests (none run); Git result (none); deviations, risks and missing
evidence; smallest next step; `Report justification: new-evidence`; compact
critique; `Resolved Execution Issues / Near-Misses` and `Pre-Existing Failure
Classification` (or none); authority expiry. Include the Planning Record and
Plan-to-Execution fields unchanged, the complete plan, the proposed first
implementation grant, and the open Cooperator questions. Report requested
versus observed native planning mode and any client restrictions truthfully.
Use `Logical-whole closure: not-closed`.

If the client's native planning mode prohibits the file write, preserve the
complete plan in the chat output, report the file-delivery limitation as
PARTIAL, and stop; the Cooperator will persist the report; do not bypass the
control with another tool. If the destination exists (collision), stop and
report instead of overwriting.

Finish: finalize the content, save exactly, read back the full saved content,
verify the first line, coordinates and path, then send a short separate
completion notice with status, location and SHA-256. The Cooperator archives
the exact prompt/report pair after the report exists; this grant gives no Git
authority.

Authority expiry: this terminal report ends the planning exchange; planning
authority expires; no implementation is authorized by it.
