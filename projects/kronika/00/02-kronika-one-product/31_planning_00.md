# Kronika one product — S6 execution plan: records, access and approval

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 31
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S6-EXECUTION-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: a bounded execution plan for the fail-closed authorization slice whose seam change can ripple across every app-constructing contract test; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: expand the accepted S6 row (common records, owner/admin/household policy, approval service, private-history foundations) into an exact implementation plan: file allowlist, migration 0034 design, centralized policy and fail-closed seam migration, complete affected-test inventory, access inventory artifact, E3/R3 acceptance route and the exact next implementation grant
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: 25_report_00.md (accepted modular-provider plan, §5 records/access/approval and §7 revised sequence)
Targeted revision basis: none
Changed decision boundary: the S6 execution mapping — exact files, migration design, fail-closed access-seam strategy and affected-test inventory
Preserved unaffected decisions: the S6 outcome and checks, the access-policy matrix, the record invariants, the S4-A contracts and schema v3, the parked capture work, all earlier accepted decisions
Automatic targeted revisions used: 0
```

Planning authority expires at the terminal planning report. This grant does
not authorize implementation, repository mutation, acceptance, publication,
deployment, host contact or closure.

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository evidence below before reasoning.
Repository reading is read-only. The only write this grant allows is the
terminal report at its exact destination when absent. No subagents, no host,
no provider, no credentials. `private/**` is never read.

## Starting state (verified at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`; clean; local `main` =
  `origin/main` = public `refs/heads/main` = `40e51cb2…`; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- S4-D documentation (ADR-0083), S4-A research contracts and configuration v3
  are accepted and published. Next active row: S6.
- Current migration head: `0033`; next revision: `0034`.
- Existing audience seam: `content_audience_allows(...)` with
  `policy: ContentAudiencePolicy | None` and a permissive `policy is None`
  branch; many app-constructing contract tests rely on that seam. The
  accepted plan requires missing policy/identity context to fail closed.
- Capture host parked; no host action.

## Planning question

Produce an approval-gated, decision-complete S6 execution plan that:

1. **Defines the exact file allowlist** against the `40e51cb2…` baseline:
   every new file (domain record values, application port, application
   service, persistence repository, migration `0034_kronika_records.py`,
   test files) and every modified existing file (centralized policy, seam,
   affected tests). Name each path exactly. State any path the plan
   deliberately excludes and why.
2. **Designs migration `0034`**: tables, columns, constraints, foreign keys
   (including the existing `logical_media` binding), indexes, downgrade, and
   the record invariants from the accepted plan (UUID identity, kinds,
   server-derived owner, private default, creation/completion/timeline
   timestamps, approval actor/time/version, unique bindings). Ground every
   column type and constraint in the existing `0033`/`catalog_schema`
   conventions.
3. **Designs the centralized access policy**: the owner/admin/household
   matrix as code placement in the existing domain/application layers; how
   the existing media paths are covered; the fail-closed change to the
   `policy is None` seam; and the complete inventory of affected tests with
   each test's required update (fail-closed injection vs permitted seam).
   Verify the inventory by reading the tests, not by guessing.
4. **Designs the approval service and history foundations**: approval/
   withdrawal/version-conflict semantics, timeline-entry rules, reanalysis
   preservation, and what is deliberately deferred to S7-P (record APIs,
   atomic Q/A save, rendering) and S8 (UI).
5. **Produces an access inventory artifact design**: a test or documented
   inventory listing each route/path and the policy source that guards it,
   suitable as the S6 "all-route authorization" evidence.
6. **Specifies the test matrix and acceptance route** for E3/R3: migration
   tests, authorization positive/negative tests, approval conflict tests,
   public-exclusion tests, synthetic disposable databases, and the fresh
   independent authorization review that follows.
7. **Recommends exactly one next bounded implementation grant** in the
   project's grant shape (identity/route, baseline, allowlist, authority,
   declared route, staging/commit, stops, report contract, trace record).
8. **States limits**: no implementation here; no claim that any code exists;
   the capture module and parked work are untouched.

## Mandatory reading

- Governing WORKER spine, `RF-19`, AP validation/planning/stopping owners,
  and the `.ap/INFOSEC.md` R3 authorization-review material as applicable.
- `25_report_00.md` §5 (records/access/approval) and §7 (S6 row);
  `ADR-0083`; the S4-A accepted contracts (`domain/research.py`,
  `application/ports/research.py`, `infrastructure/ai/configuration.py`,
  `research_registry.py`) as adjacent conventions.
- `src/framenest/domain/content_publication.py`,
  `src/framenest/application/content_publication.py`,
  `src/framenest/adapters/api/content_audience_api.py`,
  `src/framenest/application/ports/content_publication_repository.py`,
  `src/framenest/infrastructure/persistence/content_publication_repository.py`,
  `src/framenest/infrastructure/persistence/engine.py`,
  `src/framenest/infrastructure/persistence/migrations.py`,
  `src/framenest/infrastructure/persistence/catalog_schema.py`,
  the `0033` migration and the migration test conventions.
- `src/framenest/application/media_catalog.py` and the media insertion/
  ownership path as the eventual record-binding site, with the boundary to
  S7-P stated.
- The relevant tests, read in full where the policy seam appears:
  `tests/contract/test_content_audience_policy.py`,
  `tests/unit/application/test_content_audience_requester_private.py`,
  `tests/integration/test_persistence_migrations.py`, and the app-building
  contract tests whose behavior the fail-closed seam can change.

Citation rule: every material claim cites its exact source location at the
baseline; line numbers are locators. Do not run tests or produce code.

## Authority and containment

Positive authority: read-only inspection of the named repository and trace
files; the terminal report write at the exact destination below when absent;
full readback of the saved report.

Negative authority: no repository mutation; no test, build, interpreter or
package-manager execution; no host, SSH, gate, sudo, service, browser,
provider or credential action; no `private/**`; no subagents; no network; no
second planning cycle. Do not print hostnames, private network values, tokens
or secrets.

## Completion and report contract

Status: `PASS` when the execution plan is decision-complete for issuance;
`PARTIAL` when a material mapping remains open and is stated; `BLOCKED` when
the question cannot be answered inside the boundaries. Use
`Phase-qualified result: not-applicable`, `Logical-whole closure: not-closed`,
`Report justification: new-evidence`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the exact
allowlist; the migration design; the policy and seam design with the
affected-test inventory; the approval/history design and deferred boundaries;
the access inventory artifact design; the test matrix and E3/R3 acceptance
route; the recommended next implementation grant; deviations and missing
evidence; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; a short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination, read it back in full, verify its first line, coordinates,
content and path, then send the separate short completion notice with status,
path and SHA-256. Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 31_planning_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 31_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
