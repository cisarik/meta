# FrameNest — Deterministic Companion Acceptance Worker prompt

Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe (read-only deterministic acceptance evidence)
Phase: acceptance (deterministic portion; rendered acceptance remains Cooperator-owned)
Reasoning recommendation: Medium (ordinary bounded evidence work over familiar suites; High not justified — no mutation, no novel architecture)
Task identity: FRAMENEST-COMPANIE-DETACC-01 — deterministic companion acceptance evidence at shared SHA
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

## Mission

You collect the deterministic half of the reopened 03/10 Brave-companion
acceptance backlog at the exact shared release SHA, and produce a sanitized
evidence matrix that maps each backlog scenario group to the suite/test that
owns it deterministically versus the checks that remain Cooperator-rendered.
You change nothing: no product code, no tests, no documentation, no live data,
no NUC, no provider calls, no Git writes.

Exact baseline (= current public `main`, verified equal by ORCHESTRATOR
`git ls-remote` on 2026-08-26):

```text
91410fe063d9907304cff4550f61d403880a2eeb
```

Accepted decisions you operate under (Cooperator, 2026-08-26): companion
03/10 backlog explicitly reopened; Apply acceptance is deterministic-only
(no rendered Apply entry exists; an analyzed click opens hosted Details);
one owner-selected disposable public X item is reserved for a later rendered
scenario, acquisition authorized only then; existing analyzed rows / ordinary
profile are reused or the dependent live case is NOT RUN; allowlist-gate
failure routes to a separate EnvironmentFile/restart task; no synthetic
live-data mutation.

Already-classified preflight evidence you may rely on (do not re-prove, do
not expand): NUC `framenest-release status` returned active release equal to
the baseline, schema `0033`, service active, backup readiness `ready`
(Cooperator transcript, 2026-08-26). You have no NUC authority.

## Mandatory reading

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `.ap/AP.md`, `.ap/AP_WORKER.md` (pinned at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`)
3. `docs/WORKER_EXECUTION_CONTRACT.md` (Cursor boundary, canonical `./.ap/ap` route, Node rule)
4. Backlog: `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/COMPANION_PARKED_BRAVE_TEST_BACKLOG.md`
5. `docs/adr/0073-companion-merged-history-chrome-pending-visibility-x-seed-tag-and-preserving-apply.md`
6. `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
7. `SECURITY.md` — companion paragraphs (extension-origin allowlist, four `companion_mutation` routes, no CORS)
8. `docs/X_COMPANION.md` — read-only; its “fade by position” sentence is known-stale versus the outline contract; do NOT edit it (ledger candidate, not your scope)

## Repository gate (fail-closed, before any execution)

Working directory: `/home/agile/Projects/framenest` (standalone checkout;
canonical checkout used read-only — no isolated worktree is created because
you mutate nothing and baseline equals HEAD equals public `main`).

Verify and record:

- `git rev-parse HEAD` equals `91410fe063d9907304cff4550f61d403880a2eeb`;
- branch is `feat/x-meme-browser-companion`;
- `git status --porcelain=v1` is empty; any difference stops you — classify it
  per RF-12 recovery classes and return evidence, never mutate;
- `.ap` HEAD equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

## Canonical execution route (RF-16 binding)

All Python evidence goes exclusively through the declared `ap.project.conf`
operations with the exact baseline; raw `.venv/bin/python`, `python`,
`python3`, and `poetry run` are prohibited ambient routes:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 91410fe063d9907304cff4550f61d403880a2eeb
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 91410fe063d9907304cff4550f61d403880a2eeb --operation runtime-info
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 91410fe063d9907304cff4550f61d403880a2eeb --operation test-focus -- <selection> -q -p no:cacheprovider
```

An ambient-route violation signature (`Failed to import encodings` /
`No module named 'encodings'`) is classified as ambient violation, rerun once
through the same `ap exec` operation, and briefly reported — never repaired by
rebuilding environments.

Tracked JavaScript contract suites use Node’s built-in runner exactly as
declared by `docs/WORKER_EXECUTION_CONTRACT.md` (“JavaScript Tests”), from the
repository root; installing any JS toolchain is forbidden:

```text
node --test tests/x_companion_extension.test.js
node --test tests/companion_review_extension.test.js
node --test tests/companion_web_bridge.test.js
```

No other operations exist for you. `--operation test` (full suite) is not
authorized; `runtime-info` is for provenance proof only.

## Deterministic test selection (exact, no additions)

Run `./.ap/ap project check` first; then one `test-focus` invocation per batch
below (batches may be split further if output truncates, never widened):

Batch A — configuration, identity, ingress, route policy:

```text
tests/unit/test_configuration.py
tests/unit/test_configuration_ingress.py
tests/unit/test_configuration_env_file.py
tests/unit/test_identity_access.py
tests/contract/test_x_route_policy.py
tests/contract/test_tailscale_ingress_security.py
```

Batch B — companion application, tags, publication sole-writer, workspace:

```text
tests/contract/test_companion_review_api.py
tests/contract/test_adr_0073.py
tests/contract/test_content_publication_api.py
tests/contract/test_content_publication_unpublish.py
tests/contract/test_workspace_media.py
tests/contract/test_team_alias_api.py
tests/contract/test_analysis_proposal.py
tests/contract/test_automatic_analysis_privacy_contract.py
```

Batch C — X companion APIs, public reader posture, migrations:

```text
tests/contract/test_x_companion_api.py
tests/contract/test_x_request_api.py
tests/contract/test_public_published_uds.py
tests/integration/test_persistence_migrations.py
```

Then the three Node suites above.

## What the deterministic net owns (verify present, cite suite/test ids)

Non-v1 analyzed rows appear in listing while apply/detail stay fail-closed on
v1; one undecodable suggestion JSON does not 500 the mixed inbox page;
omitted-category Save yields a pending own-save row; badge equals
`unopened_count` only (pending never increments); opened is not pending;
exactly four `companion_mutation` routes; extension-origin allowlist fails
closed when empty and mutations carrying extension Origin require
allowlist membership plus `X-FrameNest-Request: 1`; no CORS; no
`notifications` permission and minimized manifest permissions; Apply unions
stored keys with submitted mapped AI keys, returns honest 409 on 32-tag
overflow, writes metadata only, and never publishes (administrator PUT is the
sole publication path incl. unpublish); movies excluded from companion
workflows; analyzed click protocol pins `v: "framenest.companion.web.v1"` with
`{ mediaId }` payload to the stored exact origin, never `*`, and has no
review-overlay fallback on handshake miss; hosted `#frame` survival (ADR-0073
S1); ordinary-403 hides history/badge while iframe and Attach remain; Settings
title-bar Connect/Disconnect, `#settings-save` disabled unless dirty; stale-
context recovery copy; auto-analysis flag default-off in tracked files; per-user
hourly proposal limit (six 201 then sanitized 429); public composition uniform
sanitized 404 posture and GET-only allowlist; migration `0033` additive.

## Hard boundaries

- Read-only against repository, durable state, live catalog, NUC, providers.
- No SSH, no sudo, no `deploy/ubuntu/*` execution, no EnvironmentFile reads,
  no provider keys, no browser launch, no GUI apps, no push, no commits,
  no stash/reset/clean, no dependency or toolchain changes.
- If any selected test FAILS or ERRORs: do not repair code, tests, or
  environment; capture the bounded failure signature and stop that batch;
  classify per the failure table (candidate / harness / ambient-route /
  environment / pre-existing-with-full-record) and continue only with
  independent remaining batches if safe.
- Preserve the first causal error: the earliest failing assertion/output is
  primary evidence; later cleanup noise never replaces it.

## Validation ladder record

Validation ladder: selected
Inspection and provenance: required (gate above plus `runtime-info` proving source resolves under the canonical checkout)
Existing focused tests: the exact batches listed above
Affected tests: identical (this is an evidence task; nothing changed)
New causal regression: none
Broad or full suite: not-used (logical-whole-scoped selection; full suite is not a Worker tax)
Runtime or testbed: not-used
Independent acceptance: not-required

Evidence tier: E1
Evidence tier basis: bounded reversible local read/test-only execution; no durable, security, production, or trust-boundary mutation triggers.
Combined implementation envelope: prohibited (no implementation stages authorized)
Independent acceptance: not-required
Rollback or recovery checkpoint: not-applicable (no mutation)
Activated stricter profile: none
Terminal report point: one terminal report after gate, all batches, and matrix are complete

## Output

Write exactly one file:

```text
/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/01_report_00.md
```

Professional English, beginning exactly:

### Report for ORCHESTRATOR_CHAT

Required content:

1. Coordinate echo: logical-whole identity, session `01`, exchange `01`.
2. Status: PASS, PARTIAL, or BLOCKED; phase-qualified result
   `acceptance-PASS` only when the gate holds AND every selected suite passes;
   otherwise PARTIAL/BLOCKED with sanitized failure classes.
3. Gate evidence: HEAD, branch, clean-status, AP pin, `ap project check`
   result, `runtime-info` provenance line.
4. Per-batch and per-Node-suite outcomes with invocation lines and pass/fail
   counts; full output only for failures.
5. The evidence-ownership matrix: backlog scenario groups (Chrome/history;
   Listing/badge; Click path; Connect/origin; Save/Apply/Settings; product
   facts) mapped to owning deterministic suite/test ids, and an explicit
   NOT-RUN-here list of Cooperator-rendered checks (rendered chrome UX,
   Settings flow on real origin, real Save/pending row, hosted Details click,
   Attach continuity, stale-context copy, disconnect clearing).
6. Invariant confirmation list (each invariant: upheld-by <suite/test>).
7. Sanitization compliance: no hostnames, tailnet identifiers, allowlist or
   extension-origin values, X URLs, titles, UUIDs of live items, cookies,
   headers, identity-map entries, private filenames, or raw journals.
8. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>.
   Pre-Existing Failure Classification: none | <complete record>; any claimed
   pre-existing failure needs the full contract record (baseline here is the
   tested main itself, so most failures will be findings against the release,
   not pre-existing debt).
9. Deviations, risks, missing evidence; one smallest next step.
10. Report justification: new-evidence.
11. Authority-expiry statement: this report terminates your authority; no
    follow-on action is authorized.

Abbreviated capability handshake in the report: client/surface observed,
model requested-vs-observed class, native planning mode observed off,
permission mode, qualitative context pressure. Capability never expands
authority.

## Stopping rule

Stop and report after the terminal report. Stop earlier — as BLOCKED — when a
gate fails, a required capability is unavailable, evidence would require
unauthorized access (live data, NUC, providers, secrets), or a batch fails in
a way you cannot classify inside your authority.

## Transition owner

ORCHESTRATOR classifies your matrix, sequences the Cooperator rendered pass,
and owns any INFOSEC finding routing, remediation slicing, publication, and
NUC refresh. You have no follow-on authority.
