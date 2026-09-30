# S9-R Planning Grant — Administrator-managed research provider settings (kronika-one-product, session 62)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 62
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S9-R-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — cross-cutting product slice over the provider boundary, administrator API, shell settings surface and durable documentation supersession
Recommended context capacity: approximately 1M tokens
Independence required: no

## Planning record

```text
Planning cycle: initial
Prior planning report: 25_report_00.md (kronika-one-product 25/01)
Targeted revision basis: none
Changed decision boundary: administrator-managed research provider settings — a Cooperator decision (2026-09-30) that the administrator can set the research model supersedes the accepted "fixed model gpt-5.5-2026-04-23" wording
Preserved unaffected decisions: no client-supplied model/endpoint/tool fields; no automatic fallback; provider/model snapshotted at admission and never changed mid-request; research disabled by default; private/family/administrator access rules; accepted budgets and limits; one generation attempt per request; capture parked; no new framework; testing economy
Automatic targeted revisions used: 0
```

## Plan-to-Execution fields

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded implementation planning for the S9-R administrator research-settings slice
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## Accepted context (do not reopen)

- Cooperator decision (2026-09-30): as administrator of Kronika he must be
  able to set the model. This is server-side administrator configuration, not
  client model selection. The no-client-selection, snapshot-at-admission and
  no-automatic-fallback rules stay. P3 live acceptance first validated the
  whole path with the previously fixed model; S9-R now adds the administrator
  surface.
- Current state (deployed): public `main` and the NUC web release are
  `3bf424586289b500cf45cb0d49676b50d27328fa`; database `0035`; research is
  enabled on the NUC with the credential provisioned through the systemd
  credential boundary and reconciles usage with
  `OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26`; the two P3 acceptance records
  exist; automatic remote cleanup is deployed.
- Accepted sources: `25_report_00.md` sections 2–4 (provider boundary,
  server-controlled selection, configuration v3, typed errors, accounting) and
  section 6 (bounded live acceptance); the S8 shell plan `52_report_00.md`
  sections 4–6 (views, state, accessibility); `58_report_00.md` (price
  schedule wiring); `60_report_00.md`/`61_report_00.md` (cleanup correction).
- The non-secret research configuration already carries a validated
  `model_id` string; `AI_CONFIG_SCHEMA_VERSION` is 3 and the writer preserves
  the research section. What is missing is the administrator surface, a
  model allowlist with matching price schedules, and the documentation
  supersession.

## Goal (one coherent outcome)

Produce the frozen S9-R plan: an administrator-managed research provider
settings slice that lets the authenticated application administrator, through
an administrator-only API and the existing packaged shell, inspect and change
the research settings — enable/disable, the model chosen from a validated
web-search-capable allowlist, and the budget values within accepted bounds —
with a matching usage price schedule per selectable model, fail-closed
validation, snapshot-at-admission semantics, and the durable documentation
update that supersedes the "fixed model" decision in ADR-0083/SPEC/SERVER.

## Required plan contents (decision-complete)

1. **Exact file allowlist** (new and edited paths) with existing-vs-new
   status, verified read-only against the baseline. Expect, at minimum: an
   administrator research-settings API module or extension of
   `src/framenest/adapters/api/ai_admin_api.py`; the route-policy table
   `src/framenest/adapters/api/tailscale_ingress.py`; the shell
   `src/framenest/adapters/api/web/{index.html,app.js,styles.css}`; the
   research configuration module and the OpenAI adapter schedule module for
   the allowlist/price-schedule mapping; Python contract tests and a
   `tests/*.test.js` shell suite; `docs/KRONIKA_ACCESS_INVENTORY.md`
   (regeneration); and the documentation update paths. Justify every path.
2. **Administrator API design**: exact routes, methods, payload shapes and
   validation; capability gating (the existing `provider.operate` capability
   is the natural fit; justify or propose the exact alternative); error codes
   and copy (reuse the stable envelope and existing codes; name any new code);
   conflict/idempotency semantics for concurrent saves; behavior when the
   credential is absent; no secret values in any response; the settings write
   path through the existing validated configuration writer
   (`write_ai_server_config`/`mutate_ai_server_config`), preserving all
   non-research sections byte-compatible.
3. **Model allowlist and pricing**: the exact validation rule for a selectable
   model (web-search-capable, non-empty, bounded); where the allowlist and the
   per-model `UsagePriceSchedule` live; fail-closed behavior for an unknown
   model (refuse the save; never silently account as zero); how the active
   schedule is selected for reconciliation; the revalidation-before-live-use
   requirement; how a model deprecation is handled by the administrator (a
   clear refusal, not a fallback).
4. **Selection semantics**: change applies only to newly admitted requests
   (snapshot at admission); an active request is never affected; the client
   never supplies model/provider/endpoint/tool fields; the UI must not imply
   otherwise. State what happens to pending/failed history on a model change.
5. **Budget fields**: decide the minimal safe scope — the accepted daily and
   monthly budget values and the per-kind reservations — with bounds and
   validation; state explicitly which values are administrator-editable and
   which are fixed limits, and what the API refuses.
6. **Shell surface**: where the research settings live inside the existing
   administrator AI area (find it in `app.js`/`index.html` and reuse its
   patterns); component/state design; capability-gated visibility and
   behavior; loading/saving/error states; confirmation semantics for a model
   change; accessibility consistent with the S8 baseline; no restyle of
   Gallery/Details/player.
7. **Tests**: Python contract tests for the admin API (capability denial,
   anonymous denial, validation failures, unknown model refusal, round-trip
   persistence, preservation of other config sections, inventory accuracy),
   configuration/pricing unit tests (allowlist mapping, schedule selection),
   and a `node --test` shell suite for the settings UI logic and its
   guards; name the causal regression for each important behavior. Keep the
   existing suites green.
8. **Documentation supersession**: the exact durable update that supersedes
   the fixed-model wording while preserving no-client-selection, no-fallback
   and snapshot semantics — propose the precise ADR-0083 amendment/new-ADR
   shape, the SPEC/SERVER sentences, and any README/ROADMAP status sentence;
   classify what is historical and what is current.
9. **Acceptance route**: focused validation; one fresh independent audit of
   the exact candidate; publication; routine NUC refresh; Cooperator rendered
   acceptance on the deployed release (reusing the existing administrator
   session; the acceptance must show that an administrator can change the
   model, that the change applies to a new request only, and that the refusal
   path works). Name the preconditions.
10. **Recommended first implementation grant**: proposed coordinates and
    profile, `Native planning mode: not-used`, exact baseline `3bf4245…`, the
    exact allowlist, positive and negative authority, validation, and stop
    rules — labelled explicitly as a non-authoritative proposal.

## Binding constraints

- No client-supplied model/provider/endpoint/tool fields anywhere; no
  automatic fallback; no model change mid-request; snapshot at admission.
- Research remains disabled by default for a fresh installation; the
  credential stays outside the UI (never displayed, edited or deletable from
  the shell).
- No new framework, dependency or test toolchain; packaged vanilla assets;
  `node --test` for JS; Python contract tests on the declared AP route.
- Any new HTTP route requires a `ROUTE_POLICIES` entry and an access-inventory
  regeneration.
- Testing economy is binding: targeted validation; no broad suite at every
  step.
- The existing S8 shell behavior (Timeline, history, forms, review,
  document render) and the Gallery/Details/player are unchanged except for
  the new administrator settings surface.

## Mandatory reading

- AP: `.ap/AP.md` (Semantic Authority, RF-03, RF-06, RF-12, RF-18, RF-19,
  Stopping Conditions), `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`
  (Planning Record, Plan-to-Execution Gate, Worker Report Header).
- Project: `AGENTS.md`, `PRODUCT.md`, `SPEC.md`, `SERVER.md`, `ROADMAP.md`,
  `docs/adr/0082-…`, `docs/adr/0083-…`.
- Trace: `25_report_00.md` §2–§4 and §6, `52_report_00.md` §4–§6,
  `58_report_00.md`, `60_report_00.md`, `61_report_00.md`, and the latest
  `00_notes.md` entries.
- Code: `src/framenest/infrastructure/ai/research_configuration.py`,
  `src/framenest/infrastructure/ai/configuration.py` (schema v3, writer),
  `src/framenest/infrastructure/ai/openai_responses.py` (price schedule),
  `src/framenest/infrastructure/ai/research_registry.py` (selection),
  `src/framenest/adapters/api/ai_admin_api.py` (existing admin AI surface),
  `src/framenest/adapters/api/tailscale_ingress.py` (`ROUTE_POLICIES`),
  `src/framenest/adapters/api/application.py` (`build_research_runtime`),
  `src/framenest/domain/identity_access.py` (capabilities),
  `docs/KRONIKA_ACCESS_INVENTORY.md`, and the shell's administrator AI area in
  `src/framenest/adapters/api/web/{index.html,app.js,styles.css}` plus
  `tests/ai_providers_admin_frontend.test.js` and the research API/shell tests.

## Repository gate (read-only)

```text
Root: /Users/agile/Projects/framenest
Remote: https://github.com/cisarik/framenest.git
Branch: feat/kronika-one-product
Expected HEAD: 3bf424586289b500cf45cb0d49676b50d27328fa
Expected parent: a3687505eb12359c76f85661e51e36d7e4778fc9
AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Required state: clean index and worktree including untracked files
```

Independently verify all of it. Classify any difference per RF-12; stop on
unexplained divergence. No Git write; no network; public `main` equals the
baseline (Orchestrator-observed 2026-09-30).

## Positive authority

Bounded read-only inspection of the named repository, trace and AP files:
file reads, `rg`/search, Git read-only commands. In addition, create the
complete terminal report at
`/Users/agile/meta/projects/kronika/00/02-kronika-one-product/62_report_00.md`
if and only if that exact file is absent; read back its full content. The
verified parent directory exists; do not create directories.

## Negative authority

No repository, trace, host or external mutation beyond the single report
write. No product or test edits, no dependency/lockfile/config change, no
schema change, no AP or managed-block change, no Git write, no fetch or
network, no test execution, no server/browser run, no provider calls, no
credential or secret handling, no `private/**`, no NUC/SSH/sudo, no capture
state, no subagents.

## Validation

Planning validation is repository-grounded: cite exact paths and symbols for
every mapping; verify the proposed allowlist read-only against the baseline;
check internal consistency against the preserved decisions and the binding
constraints; identify contradictions (especially the fixed-model wording)
explicitly. Do not run tests. A client-native plan artifact is not the
terminal report.

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed repository gate, missing mandatory
reading, a client restriction that prevents reading or the report, or an
unresolved conflict the Orchestrator must decide. A remaining material
mapping that cannot be grounded returns
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Completion and report contract

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 62, 01), and carries the compact core
with the Planning Record and Plan-to-Execution fields unchanged, the complete
plan, the proposed first implementation grant, open questions, and the
critique. Use `Phase-qualified result: not-applicable`,
`Logical-whole closure: not-closed`, `Report justification: new-evidence`.
If the client's native planning mode prohibits the file write, preserve the
complete plan in chat, report the delivery limitation PARTIAL, and stop.
If the destination exists, stop and report instead of overwriting.

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
Downloadable prompt filename: 62_planning_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 62_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

Authority expiry: the terminal report ends this planning exchange; no
implementation is authorized by it.
