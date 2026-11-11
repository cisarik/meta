# BookRadar Persistence and History — Targeted Planning Revision

Persistent role identity: WORKER
Logical whole identity: bookradar-persistence-and-history-slice
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BOOKRADAR-PERSISTENCE-HISTORY-REVISION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the revision must correct a material conflict-scope ambiguity and a false Cooperator-decision claim without reopening the accepted storage or schema direction.
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal planning report `01_report_00.md` for this logical whole, produced in this same Worker session.

Authority renewal: prior planning authority expired at `01_report_00.md`; this exchange grants read-only targeted-revision authority only. It does not accept the prior plan, grant implementation, or authorize a new planning question.

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: one targeted revision of the persistence/history plan, limited to the conflict-scope semantics, exact negative current/CLI outputs, and correction of the report's unselected conflict-lifetime claim; preserve the storage, schema, workspace, CLI command shape, allowlist and E2 evidence direction unless a minimal change is strictly required by the corrected conflict rule.
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal revised planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1
Planning cycle: targeted-revision
Prior planning report: 01_report_00.md
Targeted revision basis: newly-identified-material-risk
Changed decision boundary: exact equal-time conflict scope and negative current/CLI labels; correction of the report's unselected conflict-lifetime claim
Preserved unaffected decisions: bundled SQLite with the proposed `rusqlite = 0.37.0` pin; root core plus dependent `bookradar-store` crate and `bookradar-poc` binary; schema v1 and append-only observation/review model; four-command synthetic CLI shape; fifteen-path implementation allowlist; deferred dependency provisioning; E2 implementation evidence with one focused fresh acceptance; no UI, network ingestion, Hermes, NUC or deployment
Automatic targeted revisions used: 1

## 1. Reason for revision

`01_report_00.md` is received and is not accepted unchanged. The ORCHESTRATOR identified one material defect and one material ambiguity:

1. **False Cooperator-selection claim.** §11 says the conflict lifetime was “Selected by COOPERATOR during this exchange.” The COOPERATOR has not selected that rule. The report must present it as a proposed recommendation requiring an explicit decision; it must not claim a decision that did not occur.
2. **Conflict scope is ambiguous.** §5 step 7 correctly limits conflict detection to each exact observed-time group, but step 8 says “any incompatible pair among non-rejected claims … applies across retained history.” It must be explicit whether different-time availability or stock changes are normal temporal changes or conflicts. They are normal temporal changes under the accepted contract; only equal-time incompatible claims, intrinsic conflicting subject/language assertions, or an active disputed review should block a positive interpretation. A newer unavailable observation must not create an artificial conflict with an older available observation. A retained equal-time conflict may remain active until explicit assessment.

The revision must also define the exact user-facing `current`/CLI output for explicit unavailable, reserved, unknown, removed, conflict, failed-recheck and unorderable states, or a precise mapping from `CurrentView` to the accepted contract’s labels. The prior examples cover positive, failed and recovered states only.

This is the sole targeted revision. Do not widen it to a new storage comparison, a new application, or a new implementation scope.

## 2. Delivery, trace and authority record

External trace disposition: configured
Trace discovery: `cisarik/meta`, `projects/bookradar/00/03-bookradar-persistence-and-history-slice/`
Trace project key: `bookradar`
Trace logical-whole projection identity: `03-bookradar-persistence-and-history-slice`
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_planning_01.md`
Destination path: `cisarik/meta` @ `projects/bookradar/00/03-bookradar-persistence-and-history-slice/`
Report filename: `01_report_01.md`
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Relay basis: the COOPERATOR selected manual delivery. The Orchestrator prepared this revision prompt in Meta; the Worker has no Meta write or Meta Git authority. Return the complete revised report in this session; the COOPERATOR persists it as `01_report_01.md`. The prompt and report are first Git-added to Meta together only after the report exists.

Repository mutation: none
Host/remote mutation: none
Trace persistence: none

## 3. Preserved plan

Preserve unless a minimal correction is strictly necessary and explicitly identified:

- bundled SQLite through `rusqlite` with the proposed fixed pin; no dependency is installed in this exchange;
- root `bookradar-core` remains dependency-free and unchanged;
- workspace plus `crates/bookradar-store` and `bookradar-poc`;
- schema v1, append-only observations/reviews, exact IDs/time encoding and fail-closed version policy;
- four-command synthetic CLI and its general exit behavior;
- the fifteen-path allowlist, E2 evidence direction, fresh acceptance and deferred CI;
- all no-UI/no-network/no-NUC/no-Hermes/no-policy boundaries.

If the corrected conflict rule changes a schema field, API result, CLI transcript or test expectation, name that exact change and why it is necessary. Do not silently re-plan the storage architecture.

## 4. Required revision output

Return a complete terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinate fields from the metadata above exactly once. Use status `PASS`, `PARTIAL` or `BLOCKED`; `Phase-qualified result: not-applicable`; start/end `bookradar bd23b08…` and AP `d7023cf…`; changed files none; no build/test/dependency installation; Git result read-only; persistence none; report justification `new-material-risk`; logical-whole closure `not-closed`; authority expiry; critique, resolved execution issues, pre-existing failure classification and capability handshake.

The report should contain:

1. **Correction record** — exactly what was wrong, what the Cooperator has not decided, and what is now stated.
2. **Revised conflict rules** — exact equal-time scope, temporal-change treatment, conflict lifetime, review/rejection behavior, and how a newer negative or older import affects the current candidate.
3. **Negative current/CLI mapping** — exact text/structured output for explicit unavailable, reserved, unknown, removed, conflict, failed-recheck and unorderable states, with exit behavior.
4. **Test additions** — at least one explicit available-then-unavailable temporal-change test and one negative `current`/CLI case; exact expected results. A fifth fixture is allowed only if it is the smallest way to demonstrate the negative state.
5. **Preserved decisions** — a compact list confirming the unaffected storage, schema, workspace, allowlist and E2 decisions.
6. **Decision status** — the conflict-lifetime recommendation remains a Cooperator decision; do not mark it selected.
7. **Why no other change is required** — a short boundary statement.

Do not repeat the entire prior report. The prior report plus this revision is the plan. Do not modify `01_report_00.md`.

## 5. Authority and constraints

Read-only inspection of the BookRadar checkout at the verified baseline, current `bookradar-core` source/tests, the accepted contract and ADRs, Meta history, and the prior report. No repository, host, Meta or trace writes. No network beyond the existing public-ref read if you need to recheck it; no crates.io, dependency resolution or installation. No `ap` subcommand. No implementation, scaffolding, file creation, stage, commit or push.

If the current session is not the same Planner session that produced `01_report_00.md`, or native Plan Mode is not actually enabled, stop and report the routing defect; do not pretend continuity. If the prior report is unavailable, stop and report the exact gap.

The anomaly that would make this revision incomplete is a remaining ambiguity about whether different-time availability changes are conflicts, or a remaining claim that the Cooperator selected a rule that was not selected. If the corrected rule requires a material change beyond the preserved decisions, stop and name the smallest decision rather than expanding scope.

## 6. Authority expiry

This grant authorizes one read-only targeted planning revision. It expires at the terminal report, cancellation or supersession. It does not authorize implementation, a second revision, repository or host mutation, dependency installation, Meta writes, publication, acceptance or closure.
