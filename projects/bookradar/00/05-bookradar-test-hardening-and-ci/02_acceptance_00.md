# BookRadar — Fresh Independent Acceptance — Test Hardening and CI Slice

Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: BOOKRADAR-TEST-HARDENING-AND-CI-ACCEPT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — independent acceptance of a public CI supply-chain pin, workflow permissions, exact CLI transcripts, a fail-closed gate, and a local candidate; this is a named supply-chain and publication-adjacent risk.
Recommended context capacity: approximately 250k tokens
Independence required: yes

Acceptance candidate: a2182302de73cb345b4b646993a1ad25d602555f
Acceptance owner map: BookRadar verification-gate slice — domain contract revision 1 and ADRs 0001–0006; accepted plan `01_report_00.md` SHA-256 `073955776ff0750059a6f9d3560c801d1adfb58744a802eeb74a26c1c3747ef2`; implementation report `01_report_01.md` SHA-256 `2eac95688e02ec6e0144048a7e4e9f3fa13a736fd8161288a7616436bf3026d8`; candidate `a2182302de73cb345b4b646993a1ad25d602555f`
Acceptance allowlist: `.gitignore`; `scripts/verify.sh`; `.github/workflows/verify.yml`; `crates/bookradar-store/tests/cli.rs`; `crates/bookradar-store/tests/research_cli.rs`; `README.md`; `docs/adr/0006-verification-gate-and-ci.md`
Acceptance risk claims: the candidate is bounded to seven non-product paths; `/target/` and `/tests/target/` are ignored; three new CLI tests assert exact empty outputs; the preserved suite plus new tests is 77; `scripts/verify.sh` is fail-closed and offline after the locked fetch; the workflow is read-only, pinned, cache-free, secret-free and deployment-free; no push or public run is claimed; the AP pin, domain contract and ADRs 0001–0005 are unchanged.
Acceptance control matrix: fixed controls C1–C12 below, including positive and negative controls.
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-test-hardening-and-ci
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_acceptance_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci
Report filename: 02_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none to tracked source; ignored build outputs under `target/` may be created by the permitted gate
Host/remote mutation: none
Trace persistence: none

## Independence and delivery posture

You are a genuinely fresh WORKER in the Fresh Independent Audit profile. This
is a read-only acceptance of the exact local candidate. You did not plan or
implement it and must not inherit the Planner/Implementation conversation.
The COOPERATOR must open a new session with no prior project conversation,
confirm Native Plan Mode is OFF, and paste this prompt there. Do not use the
Planner or Implementation session, a reused transcript, or an internal
delegate. If the session is not genuinely fresh, stop and report the routing
mismatch.

The current prompt is your only task authority. The accepted plan and
implementation report are evidence, not authority. Do not correct, edit,
commit, push, publish, or close anything. If you find a defect or missing
evidence, report it; the Orchestrator decides whether one smallest correction
is authorized. This acceptance is not publication and not logical-whole
closure.

The received prompt is persisted at
`/Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci/02_acceptance_00.md`.
You may read it to verify identity and compute its SHA-256; do not modify it.
Echo the SHA-256 in your report.

## Repository and candidate gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected candidate HEAD: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected candidate parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected candidate tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Expected subject: `fix: restore target ignore and run the gates in CI`
Expected public `refs/heads/main`: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1` (not published)
Expected local state: `main` one commit ahead of `origin/main`; clean worktree
Governing AP: `.ap` gitlink and detached checkout
`d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1
Accepted ADRs: `docs/adr/0001`–`0005`; ADR 0006 is the new verification policy

Before acceptance, independently verify the root, remote, branch, candidate
HEAD, parent, tree, clean worktree, `.ap` pin and cleanliness, strict
`./.ap/ap doctor` PASS, Rust `1.99.1` and C compiler availability, and public
`main` by direct `git ls-remote`. If the candidate or public state differs,
stop and report; do not repair or push.

## Goal

Independently accept or reject the exact candidate `a218230…` for the bounded
test-and-CI hardening slice. Verify the implementation claims against the
repository, the accepted plan, the workflow, the tests, the script, the README
and the ADR. Do not rely on the implementation report as proof; use it only as
a claim to compare against direct evidence. Do not correct anything.

## Mandatory reading

Read the WORKER minimum-reading spine and the task-relevant anchors:

- `.ap/AP.md`: Semantic Authority and Artifact Relationships; RF-03, RF-05,
  RF-06, RF-07, RF-12, RF-18; §8; §12 Validation; §18 Stopping Conditions;
  Acceptance, Correction, and Escalation; Phase-Qualified Results and Closure.
- `.ap/AP_WORKER.md`: Worker Session Target; Worker Exchange Coordinates and
  Trace Boundary; Before Mutation; Validation; Reporting; Stopping Conditions.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Acceptance and Correction
  Record; Phase Result and Closure Record; Worker Exchange Identity and
  External Trace Contract; Validation Ladder Record.
- Project root `AGENTS.md`.
- The accepted plan `01_report_00.md` (SHA-256 `073955…`), the implementation
  report `01_report_01.md` (SHA-256 `2eac956…`), the provisional handout and the
  Orchestrator notes as historical evidence.
- The candidate diff, `.gitignore`, `scripts/verify.sh`,
  `.github/workflows/verify.yml`, `crates/bookradar-store/tests/cli.rs`,
  `crates/bookradar-store/tests/research_cli.rs`,
  `crates/bookradar-store/tests/common/mod.rs`, `README.md`, and
  `docs/adr/0006-verification-gate-and-ci.md`.
- `docs/domain-contract.md` and ADRs 0001–0005 as the unchanged boundary.

## Acceptance controls

### C1 — Candidate identity and scope

Verify the commit, parent, tree and subject above. Verify exactly seven changed
paths and no others:

- `.github/workflows/verify.yml` (added)
- `.gitignore` (modified)
- `README.md` (modified)
- `crates/bookradar-store/tests/cli.rs` (modified)
- `crates/bookradar-store/tests/research_cli.rs` (modified)
- `docs/adr/0006-verification-gate-and-ci.md` (added)
- `scripts/verify.sh` (added)

Verify no change under `src/` or `crates/bookradar-store/src/`, and no change
to `Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`, `.ap`,
`docs/domain-contract.md`, ADRs 0001–0005,
`crates/bookradar-store/tests/research_ingestion.rs`, or
`crates/bookradar-store/tests/common/mod.rs`.

### C2 — `.gitignore` and workspace hygiene

Verify `.gitignore` is exactly `/target/` then `/tests/target/` with a final
newline. Verify `git check-ignore -v` names pattern `/target/` for
`target/debug/ignored` and `/tests/target/` for `tests/target/ignored`, and
that `README.md` is not ignored. After the permitted gate, verify `target/`
exists and is ignored and `git status --porcelain` is empty. A missing
`/target/` pattern must make the gate fail; inspect the script's pattern check
for the exact-token comparison, not a substring.

### C3 — Tests

Verify the workspace suite has 77 tests: 17 core, 10 store unit, 4 old CLI, 13
history, 6 persistence, 2 research CLI, 5 research contract, and 20 research
ingestion; doc-tests and binary unit tests may add zero. Verify the preserved
74 tests are still present and the three new tests are exactly:

- `empty_history_exits_zero_with_count_zero` in
  `crates/bookradar-store/tests/cli.rs`, expecting exit 0 and stdout
  `synthetic=true offer=1/1 count=0\n`, stderr empty;
- `empty_current_exits_zero_with_status_empty` in the same file, expecting exit
  0 and stdout `synthetic=true offer=1/1 target=10 status=empty\n`, stderr
  empty;
- `empty_research_current_exits_zero_without_candidates` in
  `crates/bookradar-store/tests/research_cli.rs`, expecting exit 0 and stdout
  `candidates=0 conflict=clear recheck=clear verification=not-eligible\n`,
  stderr empty.

Verify the existing `research_cli_transcript_and_exits_are_stable` uses
`common::TempDir` and retains every prior assertion. Verify no test was
removed or weakened and `research_ingestion.rs` was not refactored.

### C4 — `scripts/verify.sh`

Inspect the script for `#!/usr/bin/env bash`, `set -euo pipefail`, repository
root `cd`, the fail-closed dirty-worktree check (exit 2 before PATH/ignore/
cargo), `$HOME/.cargo/bin` handling, the exact `rustc 1.99.1` check, the exact
`git check-ignore` checks, `cargo +1.99.1 fetch --locked`, locked/offline
build/test/clippy, `cargo +1.99.1 fmt --all --check`, the one-line
`bookradar-core` tree check, `git diff --check`, strict `./.ap/ap doctor`, and
the final empty `git status --porcelain`. Verify no `continue-on-error`, no
cache, no secret, and no second command list. Verify the implementation
report's negative dirty-probe evidence is consistent with the script; do not
recreate the probe in this read-only audit.

### C5 — Workflow

Verify `.github/workflows/verify.yml` has name `verify`; push to `main`,
pull request to `main`, and `workflow_dispatch`; workflow-level
`permissions: contents: read`; the stated concurrency; `ubuntu-24.04`; a
20-minute timeout; one checkout step pinned to the full 40-hex SHA
`3d3c42e5aac5ba805825da76410c181273ba90b1` with `submodules: recursive`,
`persist-credentials: false`, `fetch-depth: 1`; and one verify step running
`bash scripts/verify.sh` with `GITHUB_TOKEN` empty. Verify no
`pull_request_target`, `schedule`, environment, deployment, release, `secrets`
context, cache action, third-party Rust action, or write permission. Verify
the pin independently via read-only `git ls-remote`/public metadata if
available; if public metadata is unavailable, state the limitation rather than
guessing.

### C6 — README

Verify the README names `bash scripts/verify.sh` as the only local and CI
gate, keeps the PATH note, states the two-line ignore rationale, describes
the workflow triggers, `ubuntu-24.04`, `contents: read`, checkout SHA, no
cache/secrets/deployment/schedule and 20-minute timeout, links ADR 0006, does
not claim a green public run, and adds no status badge. Verify the synthetic
examples and policy gaps are otherwise unchanged.

### C7 — ADR 0006

Verify `docs/adr/0006-verification-gate-and-ci.md` is `Accepted 2026-11-13`
with decision owner COOPERATOR, records the script/GitHub Actions/Ubuntu
decision and the rejected alternatives, states the consequences and
limitations, and does not modify the domain contract or ADRs 0001–0005.

### C8 — Product integrity

Verify no product source, schema, research contract, domain contract, ADR
0001–0005, dependency, lockfile, toolchain, `.ap` gitlink or unrelated path
changed. Verify `bookradar-core` remains dependency-free as the tree check
proves.

### C9 — Repository and public state

Verify local `main` is one commit ahead of `origin/main`, public
`refs/heads/main` is still `d7d49ab…`, no push occurred, the worktree is clean,
the AP pin is `d7023cf…`, `.ap` is detached and clean, and strict `ap doctor`
PASS. Verify `target/` is ignored and not listed in porcelain.

### C10 — Implementation report consistency

Compare `01_report_01.md` with direct evidence. Verify the prompt SHA-256,
candidate commit/tree/parent, seven paths, 77 tests, one local commit, no push,
non-independent implementation posture, and the explicit statement that the
workflow file is not a public-run claim. A discrepancy is a finding, not
permission to repair.

### C11 — CI safety

Verify the workflow is read-only and secret-free: `contents: read` only, no
secrets, no deployment, no release, no scheduled production job, no
`pull_request_target`, no write token, no cache, no third-party Rust action,
and no settings change. The checkout action is pinned by full SHA. A missing
public run is not evidence of failure; it is separate post-publication
evidence.

### C12 — Evidence boundary

Verify the acceptance itself is read-only. Confirm the implementation report
does not claim acceptance, publication, deployment, production acceptance, a
public CI run, or closure. The actual CI run after publication is a separate
surface and cannot be inferred from the YAML.

## Positive and negative authority

Positive authority: read-only inspection of the repository, candidate diff,
tests, script, workflow, README, ADR, AP, plan, implementation report, handout
and notes; read-only Git inspection; `bash scripts/verify.sh` (which may create
ignored `target/` outputs); focused tests if needed; strict `./.ap/ap doctor`;
`git ls-remote` and read-only public action metadata; `shasum` for report and
artifact identity. The script's locked `cargo fetch` network is permitted.

Negative authority: no edits to source, tests, workflow, script, README, ADR,
Cargo files, toolchain, `.ap`, domain contract, ADRs 0001–0005 or Meta; no
correction; no commit, amend, reset, clean, stash, rebase, tag, fetch into the
repository or push; no GitHub settings or token use; no secrets, host/remote
mutation, deployment, release, publication, acceptance of product changes, or
closure. Do not create a dirty probe; inspect the script and the implementation
report's existing negative-probe evidence instead.

## Validation and completion

Run the full gate `bash scripts/verify.sh` on the clean candidate. Capture the
complete output. If it fails, stop and report the first causal error; do not
repair. Confirm the final porcelain is empty and `target/` is ignored. Confirm
no push occurred and public `main` is unchanged. Confirm the candidate tree and
test count.

Use `status: PASS` and `Phase-qualified result: acceptance-PASS` only when
every control C1–C12 is satisfied and the gate passes. Use `PARTIAL` when
useful acceptance evidence exists but a material claim remains unverified. Use
`BLOCKED` when a prerequisite prevents the audit. Do not self-correct. Do not
claim publication or closure.

Report header must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

```text
Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Include the compact core: status; phase-qualified result; start and end commit
`a218230…`; changed files none; tests and validation; Git result none; any
deviations, findings, risks or missing evidence; the one smallest next step
(publication decision or one correction); report justification
`final-acceptance`; authority-expiry statement; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

Also include:

```text
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
Pre-Existing Failure Classification: none | <complete classification per the contract below>
```

and `Logical-whole closure: not-closed`. Do not emit a closure signal. Include
the prompt SHA-256 after reading `02_acceptance_00.md`, and the report's own
SHA-256 in the separate completion notice. Do not write the report to the
repository or Meta; return it in this session for COOPERATOR persistence at
`02_report_00.md`. The COOPERATOR will save it, then the Orchestrator will
reconcile it.

## Stopping conditions

Stop and report without improvisation if:

- the candidate HEAD, parent, tree, branch, cleanliness, `.ap` pin, `ap doctor`
  state or public `main` differs from the declared state;
- the session is not genuinely fresh or has inherited Planner/Implementation
  context;
- a required read-only capability is unavailable;
- the gate fails or a test output differs from the expected transcript;
- a material claim is unverified and the audit would have to guess;
- the audit would require a correction, source write, commit, push, Meta write,
  secret, host/remote mutation, GitHub setting, publication or closure;
- the work expands beyond the fixed control matrix.

Preserve the first causal error and exact evidence. Return the report in the
session even for `PARTIAL` or `BLOCKED`, unless delivery is impossible; then
preserve the complete available content and disclose the missing delivery. This
terminal report ends the acceptance grant. No autonomous continuation.
