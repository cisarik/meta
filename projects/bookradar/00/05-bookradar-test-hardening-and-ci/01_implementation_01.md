# BookRadar — Implementation — Test Hardening and CI Slice

Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 01
Worker exchange ordinal: 02
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BOOKRADAR-TEST-HARDENING-AND-CI-IMPLEMENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — the plan is decision-complete; implementation is bounded to exact test, ignore, script, workflow, documentation and one-commit changes, with a named supply-chain pin already resolved.
Recommended context capacity: approximately 250k tokens
Independence required: no

Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `073955776ff0750059a6f9d3560c801d1adfb58744a802eeb74a26c1c3747ef2`) for task `BOOKRADAR-TEST-HARDENING-AND-CI-PLAN`, produced in this exact Worker session.
Authority renewal: prior planning authority expired at that terminal report; this exchange grants a new complete implementation grant.
Evidence posture: non-independent. The required fresh independent acceptance is a separate later Worker session and is not performed or self-certified here.
Current-session reuse: the accepted plan is repository-grounded, the session is healthy, the assumptions are unchanged, and retained context reduces implementation error. Retained context is convenience, not authority. Stop if retained context conflicts with current repository evidence.

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
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exact allowlist paths below; ignored build outputs under `target/` and `tests/target/`; temporary `verify-dirty-probe.tmp` created and removed only for the negative probe
Host/remote mutation: none
Trace persistence: none

## Authority and delivery posture

This prompt is your only current task authority. The accepted plan is
`01_report_00.md` (SHA-256 above); this grant binds that plan and records the
COOPERATOR's approval of the plan and decision table on 2026-11-13. If this
grant and the plan differ, this grant controls; stop if a difference is
material and unresolved.

Native Plan Mode must be OFF for this exchange. This prompt must be pasted into
the exact current Planner session that produced `01_report_00.md`, not a new or
different session. If that session is unavailable, do not paste this prompt;
return for a fresh-session `02/01` implementation grant instead.

The COOPERATOR approved:

- GitHub Actions; one `ubuntu-24.04` job; no macOS job.
- `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1) with
  `submodules: recursive`, `persist-credentials: false`, `fetch-depth: 1`.
- No cache; no third-party Rust action; runner rustup plus
  `rust-toolchain.toml`.
- `bash scripts/verify.sh` as the single local/CI gate; the workflow calls it
  and does not restate the cargo list.
- The three named process tests plus `common::TempDir` in the existing research
  CLI test; the 74 existing tests stay.
- `docs/adr/0006-verification-gate-and-ci.md` as Accepted with date
  2026-11-13; decision owner COOPERATOR. Do not edit the domain contract or
  ADRs 0001–0005.
- E2 evidence and a fresh independent acceptance before publication.
- No status badge in this slice.
- One local commit; publication is a separate later grant and is prohibited
  here.

## Repository and baseline gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected parent: `ed4de54637f22613723bc3df98536a1ac25d0800`
Expected tree: `4b8a81d443393ad06eb50b4e97ded598a5bb3931`
Expected subject: `fix: update .gitignore to exclude tests target directory`
Expected worktree: clean; `target/` may be absent initially
Governing AP: `.ap` gitlink and detached checkout
`d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1
Accepted ADRs: `docs/adr/0001`–`0005`

Before any edit, independently verify the root, remote, branch, HEAD, parent,
tree, clean worktree, `.ap` pin and cleanliness, strict `./.ap/ap doctor` PASS,
Rust `1.99.1` and C compiler availability. If the baseline differs, or the
worktree is dirty, stop and report; do not repair, reset, clean, stash or
switch branch.

## Accepted plan and binding implementation decisions

The full plan is the terminal report `01_report_00.md`; read it as accepted
design context. The binding decisions are restated here.

### 1. `.gitignore`

Replace the file content with exactly these two lines, including the final
newline:

```text
/target/
/tests/target/
```

Do not use `.git/info/exclude`, a global ignore, `git clean`, or manual
cleanup. After writing it and before any build, verify all three:

- `git check-ignore -v -- target/debug/ignored` names pattern `/target/`;
- `git check-ignore -v -- tests/target/ignored` names pattern `/tests/target/`;
- `git check-ignore -q -- README.md` is non-matching.

The pattern token check must distinguish `/target/` from `/tests/target/`; a
substring search is insufficient.

### 2. Tests

Add these exact process tests and keep every existing assertion:

- `empty_history_exits_zero_with_count_zero` in
  `crates/bookradar-store/tests/cli.rs`, using the existing `run` helper and
  `common::TempDir`. `init <temp>/store.sqlite` then
  `history <temp>/store.sqlite`; expect exit 0, stdout
  `synthetic=true offer=1/1 count=0\n`, stderr empty.
- `empty_current_exits_zero_with_status_empty` in the same file and harness.
  `init <temp>/store.sqlite` then
  `current <temp>/store.sqlite 1793548800`; expect exit 0, stdout
  `synthetic=true offer=1/1 target=10 status=empty\n`, stderr empty.
- `empty_research_current_exits_zero_without_candidates` in
  `crates/bookradar-store/tests/research_cli.rs`; add `mod common;` and use
  `common::TempDir`. `init <temp>/empty.sqlite` then
  `current <temp>/empty.sqlite synthetic:producer synthetic:source OFFER-A
  generation-1 10 1793548800`; expect exit 0, stdout
  `candidates=0 conflict=clear recheck=clear verification=not-eligible\n`,
  stderr empty.

In the existing `research_cli_transcript_and_exits_are_stable`, replace the
pid-based temporary directory and end-of-function cleanup with
`common::TempDir`; keep every current assertion. Do not refactor
`crates/bookradar-store/tests/research_ingestion.rs`. Do not add coverage,
fuzzing, benchmarks or a new harness.

If a new test's actual output differs from the expected transcript, stop and
report it. Do not edit product source, schema, renderers, Cargo files or
toolchain to force a pass.

### 3. `scripts/verify.sh`

Create `scripts/verify.sh`, shebang `#!/usr/bin/env bash`, invoked as
`bash scripts/verify.sh` locally and in CI. It must use `set -euo pipefail`,
`cd` to the repository root from the script directory, and fail closed in this
order:

1. If `git status --porcelain` is non-empty, print it to stderr and exit 2
   before PATH changes, ignore checks or cargo. Do not stash, reset or clean.
2. Prepend `$HOME/.cargo/bin` when that directory exists.
3. Require `rustc --version` to start with `rustc 1.99.1` and
   `cargo +1.99.1 --version` to succeed.
4. Require the exact `git check-ignore` pattern checks above and require
   `README.md` to be unignored.
5. `cargo +1.99.1 fetch --locked`.
6. `cargo +1.99.1 build --workspace --all-targets --locked --offline`.
7. `cargo +1.99.1 test --workspace --locked --offline`.
8. `cargo +1.99.1 fmt --all --check`.
9. `cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D
   warnings`.
10. Capture `cargo +1.99.1 tree --locked --offline -p bookradar-core`; require
    exactly one line whose prefix is `bookradar-core v0.1.0 (`.
11. `git diff --check`.
12. `./.ap/ap doctor` with no `--candidate` (strict mode).
13. Require `git status --porcelain` to be empty. A build must leave `target/`
    ignored; a missing `/target/` pattern must fail here.

Fail fast; no `continue-on-error`. Do not add a cache, a second command list or
a release/deployment step.

### 4. `.github/workflows/verify.yml`

Create exactly this workflow shape, with the pinned SHA and no secrets:

```yaml
name: verify

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: verify-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

jobs:
  verify:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          submodules: recursive
          persist-credentials: false
          fetch-depth: 1
      - name: Verify
        env:
          GITHUB_TOKEN: ""
        run: bash scripts/verify.sh
```

The workflow name and filename are `verify` and `verify.yml`; no `main.yml` is
required. Do not add `pull_request_target`, `schedule`, deployment, release,
environment, cache, third-party Rust action, `secrets` context or write
permission. Do not change repository settings; Actions is already enabled and
the default workflow token is read-only.

### 5. README and ADR

Update `README.md`:

- State that `bash scripts/verify.sh` is the only local and CI gate; describe
  what it proves; do not paste a second cargo flag list.
- Keep the `$HOME/.cargo/bin` PATH note.
- Replace the false "ignored `target/`" claim with the two-line rationale:
  `/target/` is the workspace build directory; `/tests/target/` remains for a
  nested `tests/` cargo output. Current workspace tests compile into `target/`.
- Name the workflow `verify`, its triggers, `ubuntu-24.04`, `contents: read`,
  the checkout SHA, no cache/secrets/deployment/schedule, and the 20-minute
  timeout.
- Do not claim a green public run. Do not add a status badge in this commit.
- Leave the synthetic examples and all policy gaps unchanged.

Create `docs/adr/0006-verification-gate-and-ci.md` following the shape of ADR
0004. Record status `Accepted`, date 2026-11-13, decision owner COOPERATOR. It
must record: one bash script is the gate; GitHub Actions on `ubuntu-24.04`;
`actions/checkout` pinned to
`3d3c42e5aac5ba805825da76410c181273ba90b1`; `contents: read`; no cache; no
third-party Rust action; strict `ap doctor`; clean porcelain after the gates.
Record the rejected alternatives: `ubuntu-latest`, a macOS job,
`dtolnay/rust-toolchain`, `actions/cache`, `Swatinem/rust-cache`, and
duplicating commands in YAML. Link the ADR from the README. Do not edit
ADRs 0001–0005 or the domain contract.

## Changed-path allowlist

Exactly these paths may change or be created:

- `.gitignore`
- `scripts/verify.sh`
- `.github/workflows/verify.yml`
- `crates/bookradar-store/tests/cli.rs`
- `crates/bookradar-store/tests/research_cli.rs`
- `README.md`
- `docs/adr/0006-verification-gate-and-ci.md`

No other path. `crates/bookradar-store/tests/common/mod.rs` is reused and not
modified. Directory creation for `scripts/` and `.github/workflows/` is
authorized only for these exact files. The temporary `verify-dirty-probe.tmp`
is authorized for the negative probe only and must be absent at completion.

## Implementation stages and gates

1. Baseline gate: verify the declared state. Stop on any difference or dirty
   worktree.
2. `.gitignore`: write the two-line file; run the three ignore checks. Do not
   build yet.
3. Tests: add the three tests and the `TempDir` replacement; run
   `cargo +1.99.1 test --locked --offline -p bookradar-store --test cli --test
   research_cli`. This creates `target/`; `git status --porcelain` must not
   list it. If a new test fails on output, stop; do not edit product code.
4. Script, workflow, README and ADR: create or update the exact paths.
5. Review: inspect `git diff` and `git diff --cached --check`; stage only the
   seven allowlist paths; make one local commit with subject
   `fix: restore target ignore and run the gates in CI`. No amend, rebase,
   tag, extra ref, force, reset or push.
6. Negative probe: create an untracked `verify-dirty-probe.tmp` at the
   repository root; run `bash scripts/verify.sh`; expect exit 2 before cargo;
   delete the file; confirm `git status --porcelain` is empty.
7. Full gate: run `bash scripts/verify.sh` on the clean post-commit tree;
   expect exit 0, a clean porcelain, and `target/` present and ignored.
8. Report: write the terminal implementation report in the session; do not
   write it to Meta or push.

## Validation ladder

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: crates/bookradar-store/tests/cli.rs and crates/bookradar-store/tests/research_cli.rs
Affected tests: the same focused tests plus the workspace suite
New causal regression: three named process tests and the TempDir cleanup close the empty-history, empty-current and research-empty-current evidence gaps
Broad or full suite: required-because the accepted plan makes scripts/verify.sh the project gate
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker
```

Expected final test count: 77 tests (74 preserved plus 3 new). The
implementation report must state the actual count and the exact new commit SHA,
tree and changed paths. Implementation PASS is non-independent; it is not
acceptance, publication or closure.

## Evidence and acceptance envelope

```text
Evidence tier: E2
Evidence tier basis: bounded reversible source/test/docs/CI-file changes plus a public CI workflow and supply-chain pin; no secret, production host, privilege change or durable migration
Authorized implementation stages: baseline gate; .gitignore; tests; script/workflow/README/ADR; one local commit; dirty-file negative probe; full script; terminal report
Combined implementation envelope: allowed
Implementation stage gates: each stage must pass before the next; no product-code edit; no push
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: baseline d7d49ab6df2d2fd063644700095d5e55a94e4ae1; before commit stop and report; after commit do not reset, amend or force
Activated stricter profile: none
Terminal implementation report point: after the one local commit and the full scripts/verify.sh pass
```

The fresh independent acceptance is a separate grant and a separate fresh
session. This grant does not authorize it, and the implementing Worker must not
self-certify it. Publication is a later grant: prove public `main` is still
`d7d49ab6df2d2fd063644700095d5e55a94e4ae1`, then one non-force push and a
directly observed CI run. None of that is authorized here.

## Network, dependencies, secrets, and Git

Network authority: only `cargo +1.99.1 fetch --locked` for the already locked
dependency graph, plus the ordinary checkout/toolchain network that CI will use
after publication. No new dependency, no version change, no `Cargo.toml`,
`Cargo.lock` or `rust-toolchain.toml` edit. No GitHub API or settings change.
No `git fetch`.

Secret authority: none. Do not inspect, print, commit or transmit credentials.
Do not use the GitHub token; the workflow sets `GITHUB_TOKEN` empty on the
verify step.

Git authority: read-only inspection; stage only the seven allowlist paths;
exactly one local commit with the stated subject. No `git add .` or `git add
-A`; no fetch, push, merge, rebase, amend, tag, branch, remote/config change,
reset, restore, stash or clean. No publication.

Host/remote mutation: none. No SSH, services, sudo, deployment, release,
account or production action.

## Positive and negative authority

Positive authority: read/write only the seven allowlist paths; create and
remove only `verify-dirty-probe.tmp`; create ignored build outputs under
`target/` and `tests/target/`; run the focused tests, the full
`bash scripts/verify.sh`, read-only Git inspection, `cargo fetch --locked`, and
the exact local commit. Read the accepted plan, handout, notes and AP as
evidence.

Negative authority: all other writes, paths, dependencies, toolchain changes,
product-source edits, schema or contract edits, ADR 0001–0005 edits, Meta
writes, Git push/remote changes, GitHub settings, secrets, host/remote
mutation, deployment, release, acceptance, publication and closure are
prohibited. Do not use `git clean`, reset, stash or force to recover.

## Report contract

Return the terminal implementation report in this session; the COOPERATOR
persists it at `01_report_01.md`. Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

```text
Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 01
Worker exchange ordinal: 02
```

Include the compact core: `status`; `Phase-qualified result:
implementation-PASS` only if the candidate and validation are complete; start
commit `d7d49ab…`; end commit (the new local commit); changed files and
purposes; tests and validation (focused and full, 77 expected); Git result
(one local commit, no push); deviations, risks or missing evidence; the one
smallest next step (fresh independent acceptance); report justification
`new-mutation`; authority-expiry statement; and:

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
the prompt SHA-256 after reading `01_implementation_01.md`, and the report's
own SHA-256 in the separate completion notice. Do not write the report to the
repository or Meta; do not push.

## Stopping conditions

Stop and report without improvisation if:

- the baseline, branch, HEAD, parent, tree, cleanliness, `.ap` pin or
  `ap doctor` differs from the declared state;
- the exact current Planner session is unavailable or the prompt cannot be
  delivered there;
- a new test's actual output differs from the expected transcript;
- a required change would touch a path outside the allowlist, product source,
  schema, contract, ADR 0001–0005, Cargo files or toolchain;
- `scripts/verify.sh` fails on a product defect or an unrepaired regression;
- a Git commit fails, or recovery would require reset, amend, force, clean or
  another destructive operation;
- a dependency, network, secret, host, GitHub setting, publication or
  acceptance action becomes necessary;
- the candidate would require a fresh session or evidence that is not in this
  grant.

Preserve the first causal error and exact evidence. Return the report in the
session even for `PARTIAL` or `BLOCKED`, unless delivery is impossible; then
preserve the complete available content and disclose the missing delivery.
This terminal report ends the implementation grant. No autonomous
continuation.
