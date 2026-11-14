# BookRadar — First Planner — Test Hardening and CI Slice

Persistent role identity: WORKER
Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BOOKRADAR-TEST-HARDENING-AND-CI-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the plan must reason about a public CI supply chain, exact action pins, secret-free remote execution, and a cross-cutting test/quality policy; this is a named supply-chain and publication-adjacent risk.
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded design of one minimal test-and-CI hardening slice for the current BookRadar baseline, including exact test additions, `.gitignore` correction, one local/CI verification path, one small secret-free GitHub Actions workflow, documentation, evidence tier, and publication boundary.
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

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
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: none

## Authority and delivery posture

You are a fresh WORKER in the Planner profile. This is a read-only planning
exchange. The current prompt is your only task authority. The provisional
handout and the Orchestrator notes are evidence, not authority.

Native Plan Mode is ON and must remain ON for this exchange. Do not implement,
edit repository files, write to the Meta trace, run builds or tests, install
dependencies, fetch into the repository, commit, push, accept, publish, or close
anything. Return the complete terminal planning report in this session. The
COOPERATOR will persist it at the exact report path above. The relay basis is
the COOPERATOR-selected manual ferry and the native Plan Mode write restriction;
`Trace persistence: none` is intentional and grants no Meta write.

The received prompt is persisted at
`/Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_planning_00.md`.
You may read that file to verify identity and compute its SHA-256; do not modify
it. Echo the SHA-256 in your report.

## Repository and baseline

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected parent: `ed4de54637f22613723bc3df98536a1ac25d0800`
Expected tree: `4b8a81d443393ad06eb50b4e97ded598a5bb3931`
Expected subject: `fix: update .gitignore to exclude tests target directory`
Expected worktree: clean; no `target/` present
Governing AP: `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10
Accepted ADRs: `docs/adr/0001`–`0005`; ADR 0005 accepted 2026-11-12

Independently verify before planning: physical root and remote; branch and HEAD;
parent and tree; cleanliness; absence of `target/`; `.ap` detached at the
gitlink and clean; strict `./.ap/ap doctor` PASS; Rust `1.99.1` and C compiler
availability; `.gitignore` content; absence of `.github`, `justfile`, and any
local verification script; README gate commands; and the 74-test inventory
(17 core, 10 store unit, 6 persistence, 13 history, 2 old CLI, 1 research CLI,
5 research contract, 20 research ingestion). Public `refs/heads/main` may be
checked read-only with `git ls-remote`. If repository state differs, classify
the difference under RF-12 and stop; do not repair it.

The predecessor closure is
`/Users/agile/meta/projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md`
(SHA-256 `d8c62fb1fef6f1c33d9d9e71e4a6986c90812362e3e0809ae1d9c08fc78d9584`).
The provisional handout is
`/Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci/00_handout.md`
(SHA-256 `95e69eb72e4d9b6f8b17c663970f2f2815867c34d6e936a8f50dc8ba581dd3dd`).
Read them as historical evidence. Do not treat either as a current grant.

## Mandatory reading

Read the WORKER minimum-reading spine and the task-relevant anchors:

- `.ap/AP.md`: Semantic Authority and Artifact Relationships; RF-03, RF-06,
  RF-12, RF-18; §3 Worker Session Target and Orchestration Planning and
  Implementation Planning; Plan-to-Execution Gate; Planning Budget and Expiry;
  §8; §12 Validation; §18 Stopping Conditions.
- `.ap/AP_WORKER.md`: Worker Session Target; Worker Exchange Coordinates and
  Trace Boundary; Before Mutation; Validation; Reporting; Stopping Conditions.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Planning Record;
  Plan-to-Execution Gate; Worker Exchange Identity and External Trace Contract;
  Validation Ladder Record.
- Project root `AGENTS.md`.
- `README.md`, `.gitignore`, `Cargo.toml`, `rust-toolchain.toml`, `Cargo.lock`.
- `crates/bookradar-store/tests/cli.rs`,
  `crates/bookradar-store/tests/research_cli.rs`,
  `crates/bookradar-store/tests/common/mod.rs`, and the two CLI binaries
  `crates/bookradar-store/src/bin/bookradar-poc.rs` and
  `crates/bookradar-store/src/bin/bookradar-research.rs`.
- The test inventory and names in `tests/verification.rs`,
  `crates/bookradar-store/tests/persistence.rs`,
  `crates/bookradar-store/tests/history.rs`,
  `crates/bookradar-store/tests/research_contract.rs`, and
  `crates/bookradar-store/tests/research_ingestion.rs`. Inspect enough to audit
  coverage; do not refactor the 982-line research ingestion test file merely
  for style.
- `docs/domain-contract.md` and the accepted ADRs 0001–0005 as read-only
  context for the no-product-semantics-change boundary.

## Goal

Produce one implementation-ready plan for the smallest durable
test-and-CI hardening slice on this baseline. The plan must be executable from
the repository evidence, must preserve the accepted 74 tests and all product
semantics, and must leave every material CI/platform/quality policy choice
visible to the COOPERATOR. This is a plan, not implementation and not
acceptance.

Accepted boundaries:

- No change to `bookradar-core` behavior, `bookradar-store` product behavior,
  schema v1, the research ledger contract, the research wire contract, the
  domain contract, or ADRs 0001–0005.
- No new product feature, UI, live Hermes/Playwright adapter, scraping,
  external API, MCP, real retail data, screenshots, personal data, accounts,
  authentication, NUC, SSH, sudo, services, deployment, release, scheduled
  production job, or secret-bearing workflow.
- No broad test-suite rewrite, coverage-percentage program, new heavy test
  framework, benchmarks, fuzzing, or toolchain upgrade.
- No force push, rebase, history rewrite, tags, extra refs, or undocumented
  dependency installation.
- No Meta Git operation and no AP update. Meta Git remains COOPERATOR-owned.

## Required planning work

### 1. As-found audit

Record exactly what exists versus what is missing. Confirm the baseline,
`.gitignore` contents, `.github` absence, README gate commands, test inventory,
test infrastructure, toolchain, and the two CLIs. Do not assume the known gaps
are the only gaps. State what you inspected and what you could not inspect.

### 2. Test-gap inventory and exact assertions

Audit the 74 tests against the accepted contract and the two CLIs. At minimum,
evaluate:

- old `bookradar-poc` empty `history` output and exit code;
- old `bookradar-poc` empty `current` output and exit code;
- research CLI empty `current` output and exit code;
- deterministic temporary-store cleanup in the research CLI test, including
  behavior on assertion failure;
- any other high-value behavioral gap you can justify from the accepted
  contract, without turning this into a suite rewrite or coverage program.

For every proposed test, state: exact file, exact test function name, input
setup, expected stdout and stderr, expected exit code, the behavior or
regression it closes, the existing evidence gap, and why the test is a causal
regression rather than an implementation mirror. Do not refactor the 982-line
research ingestion test file merely for style.

### 3. `.gitignore` correction and workspace hygiene

The current `.gitignore` contains only `/tests/target/`; the post-closure
commit replaced `/target/` instead of adding `/tests/target/`. Specify the
exact corrected file content that restores `/target/` while preserving
`/tests/target/`. Specify how the implementation will prove it with
`git check-ignore` and a real build, and how the verification path will fail
closed on a future ignore regression. Do not use `.git/info/exclude`, global
ignores, or manual cleanup. Note that README currently calls `target/` ignored;
the documentation must become true.

### 4. Local verification path versus CI duplication

Evaluate CI-only versus one small local verification script invoked by CI.
Recommend one source of truth. If you propose a script, state its exact path,
interpreter, fail-fast behavior, command order, expected output checks, and
clean-worktree semantics, including how it handles a pre-existing dirty
worktree. The path must prove the same gates locally and in CI without a
duplicated stale command list. Do not build a large release infrastructure.

### 5. CI platform, triggers, permissions, and cost

GitHub Actions is the expected candidate because the canonical repository is
on GitHub; evaluate another platform only if materially justified. Specify:

- exact triggers: push to `main`, pull requests to `main`, and optional
  `workflow_dispatch`;
- workflow-level `permissions: contents: read`;
- concurrency group and cancellation behavior;
- a bounded job timeout;
- no `pull_request_target`, secrets, deployment, release, scheduled production
  job, or write permission;
- Ubuntu-only versus Ubuntu plus macOS, with the cost and native-difference
  trade-off;
- the exact runner label, including whether to pin a numbered Ubuntu image or
  use `ubuntu-latest`.

### 6. Action pins, Rust setup, dependencies, and caching

Pin every third-party action by full commit SHA, not a floating tag. Provide
the exact full SHA and the source evidence used to resolve it. Compare
`actions/checkout` plus `rustup`/`rust-toolchain.toml` against a third-party
Rust action; compare no cache, `actions/cache`, and a pinned third-party cache
action. State the exact checkout inputs, including submodule initialization and
whether credentials are persisted. Allow network only for checkout, toolchain
installation, and the locked dependency fetch; tests remain offline. Do not
guess a SHA. If network access is unavailable, state the exact verification
command and mark the pin as a required pre-implementation decision.

### 7. CI steps and local/CI parity

Propose the exact step order, consistent with the chosen local path:

- checkout with the pinned `.ap` submodule;
- select Rust `1.99.1`;
- fetch only the locked dependency graph;
- build, test, fmt, and clippy with `--locked --offline`;
- assert `cargo tree -p bookradar-core` contains only `bookradar-core`;
- run `git diff --check`;
- run strict `./.ap/ap doctor`;
- assert `git status --porcelain` is clean after the gates.

Fail fast, no `continue-on-error`. State exactly how the core-tree assertion is
implemented and how the clean-worktree assertion catches the known
`.gitignore` regression. Compare duplicating commands in YAML versus a single
local script invoked by CI; choose one source of truth.

### 8. Test infrastructure and determinism

Confirm the proposed tests use owned temporary directories, injected times, no
wall clock, no network, no credentials, and no real data. Keep process-level
CLI tests isolated. State cleanup behavior and how a failure preserves its
first causal error. If the research CLI test should adopt the existing guarded
`TempDir` pattern, specify the smallest change and why.

### 9. Documentation and ADR

Update README with the local verification command, CI status and limits, and
the `.gitignore` rationale. Add a status badge only if it reflects the real
workflow and does not become placeholder theater. Add one implementation ADR
only if a meaningful durable CI/quality policy is accepted; do not modify the
domain contract or ADRs 0001–0005. No license, contribution, privacy,
security-response, support, or release policy.

### 10. Evidence tier, acceptance, and CI-run verification

Propose E1 or E2 with a rationale. Test additions and `.gitignore` may be E1; a
new CI workflow with remote execution and public status may warrant E2 and
fresh independent acceptance. The actual workflow run after publication is
separate evidence and must be observed directly; do not claim CI is active from
the YAML file alone. No deployment. State the exact acceptance matrix,
including negative controls and the independence requirement.

### 11. Git and publication boundary

Propose exact changed paths, one reviewable local commit, and a normal
non-force push only under a separate publication grant. No force, rebase,
history rewrite, tags, or extra refs. The CI workflow becomes active only after
the push; a post-push workflow run is a separate evidence surface. State the
proposed commit subject and the rollback path.

### 12. Implementation path and rollback

Propose the exact path allowlist, ordered implementation stages, stage gates,
rollback, a small local demonstration, and the Git/publication boundary. If a
test exposes a real product defect, stop and report it; do not silently change
product semantics. If CI requires a third-party action or repository setting
that cannot be verified, surface the decision; do not guess. Do not propose
changes outside the bounded slice.

## Required plan output

Return a terminal planning report with these sections:

1. As-found audit and baseline evidence.
2. Test-gap inventory with exact proposed assertions and a statement that the
   existing 74 tests are preserved.
3. `.gitignore` and workspace-hygiene plan.
4. Local verification path and CI-parity decision.
5. CI platform, OS matrix, action pins, Rust setup, dependency fetch, caching,
   triggers, permissions, concurrency, and timeout.
6. Exact CI step order and local script outline.
7. Test-infrastructure and determinism review.
8. Documentation and ADR proposal.
9. Evidence tier, acceptance matrix, and post-publication CI-run evidence plan.
10. Exact changed-path allowlist, ordered implementation stages, rollback, and
    proposed commit subject.
11. Decision table: for each material choice (platform, OS matrix, action pins,
    caching, local script versus YAML, test scope, ADR, evidence tier,
    publication, badge), give the recommendation, alternatives, evidence,
    cost/risk, and the exact COOPERATOR decision required.
12. Residual risks, open questions, and the one smallest next step.

Do not implement any item. Do not create test files, workflow files, scripts,
ADRs, or README edits. Do not run `cargo build`, `cargo test`, `cargo fetch`, or
any command that could create `target/` or other repository artifacts. Static
inspection, read-only Git reads, `./.ap/ap doctor`, and public action metadata
reads are permitted. If a needed read-only check would write, stop and report
the limitation.

## Validation and completion

For this planning exchange, `cargo` builds/tests are intentionally not run; the
planning evidence is the current repository inspection and the predecessor's
74-test evidence. The implementation grant will reproduce the full suite and
gates on the corrected baseline.

Use `status: PASS` when the plan is complete and decision-ready. Use `PARTIAL`
when useful plan content exists but a material evidence gap or missing
capability remains. Use `BLOCKED` when a prerequisite prevents planning. Do not
claim a product defect without evidence.

Report header must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

```text
Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 01
Worker exchange ordinal: 01
```

Include the compact core: status; `Phase-qualified result: not-applicable`;
start and end commit `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`; changed files
none; tests and validation (read-only inspection only); Git result none;
deviations, risks, or missing evidence; the one smallest next step; report
justification `new-evidence`; authority-expiry statement; and:

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

and `Logical-whole closure: not-closed`. Do not emit a project closure signal.
Do not write the report to the repository or Meta; return it in this session
for COOPERATOR persistence at `01_report_00.md`. The COOPERATOR will save it,
then the Orchestrator will reconcile it. A terminal report ends this planning
grant; it grants no implementation, acceptance, publication, or closure
authority.

## Stopping conditions

Stop and report without improvisation if:

- the repository root, remote, branch, HEAD, parent, tree, cleanliness, `.ap`
  pin, or `ap doctor` state differs from the declared baseline;
- a required read-only capability (Git, shell, public action metadata, or
  `./.ap/ap doctor`) is unavailable;
- the only way to answer a material question would require a repository or
  Meta write, a build/test, a dependency change, a fetch into the repository,
  a secret, a host/remote mutation, or a publication action;
- a test or inspection exposes a genuine product defect whose repair would
  change product semantics;
- a material CI platform, action pin, runner, repository setting, or publication
  decision cannot be verified and would have to be guessed;
- the plan would require paths or scope outside the bounded slice.

Preserve the first causal error and the exact evidence. Return the report in
the session even when the outcome is `PARTIAL` or `BLOCKED`, unless delivery is
itself impossible; then preserve the complete available content and disclose
the missing delivery.
