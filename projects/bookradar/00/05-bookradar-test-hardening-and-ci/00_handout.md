# BookRadar — Opening Handout: `bookradar-test-hardening-and-ci`

**Artifact:** `projects/bookradar/00/05-bookradar-test-hardening-and-ci/00_handout.md` (canonical trace spelling; the Cooperator-requested local alias is `00.handout.md`).
**Kind:** provisional opening continuity, domain-dependency and decision-context handout for a fresh per-whole Orchestrator. **Not** a Worker prompt, permission grant, implementation plan, acceptance, publication or closure.
**Authored by:** outgoing per-whole ORCHESTRATOR (direct project checkout), 2026-11-13, under explicit COOPERATOR instruction and full trust. This is not a Master handoff and grants no authority.
**Predecessor:** `projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md` (`closed-by-ORCHESTRATOR`; acceptance PASS; publication PASS), SHA-256 `d8c62fb1fef6f1c33d9d9e71e4a6986c90812362e3e0809ae1d9c08fc78d9584`.
**Current public maintenance baseline:** `d7d49ab6df2d2fd063644700095d5e55a94e4ae1` (`fix: update .gitignore to exclude tests target directory`), parent `ed4de54637f22613723bc3df98536a1ac25d0800`, tree `4b8a81d443393ad06eb50b4e97ded598a5bb3931`. This post-closure commit is a follow-up maintenance fix, not a reopened predecessor whole. It changes `.gitignore` only and contains the regression described in §2.
**Earlier closed wholes:** `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`; `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md`; `projects/bookradar/00/02-bookradar-rust-foundation/01_closure.md`; `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_closure.md`.
**Logical-whole candidate identity:** `bookradar-test-hardening-and-ci`.
**Handout status:** provisional until the fresh per-whole Orchestrator reconciles the current repository, Cooperator selection and activated Meta trace. Do not modify this frozen handout in place after opening; material changes use a successor handout under the AP/Meta handoff sequence.
**Intended successor capability profile:** `Orchestrator` (direct project checkout), with `Orchestrator session scope: logical-whole`.
**Upstream author access profile/scope:** `Orchestrator` / `logical-whole` (outgoing session).
**Restoration classification:** PASS for read-only preparation of the first Planner on the observed baseline; current public `main`, local checkout, tool availability and Meta trace **must** be independently revalidated before any Worker grant. Not implementation readiness.
**Authority:** zero. Neither this handout nor the predecessor closure grants Git, filesystem, SSH, host, dependency installation, implementation, acceptance, publication or Meta mutation.

## 0. Selection rationale and one bounded objective

The Cooperator selected `bookradar-test-hardening-and-ci` with full trust after the predecessor closure recommended it as the lowest-risk follow-up. The research-ingestion trust boundary is now public and accepted:

- `bookradar-core` remains dependency-free and evaluates one supplied observation and explicit context.
- `bookradar-store` owns schema v1 observation history and the separate research ledger with strict JSON v1, replay/quarantine, candidate projection and no auto-verification.
- 74 tests passed at the predecessor candidate; the last public commit is `d7d49ab…`; the AP pin is unchanged; the domain contract remains revision 1.

The next risk is not another product feature. It is **evidence durability and automation**: known test gaps, a `.gitignore` regression introduced by the post-closure maintenance commit, no CI, and manual-only gates. These make every later whole more expensive and let trace/report-delivery friction recur.

**Single objective proposed for this whole:** establish one minimal, durable **test-and-CI hardening slice** that closes the known behavioral test gaps, restores correct workspace-ignore behavior, and runs the existing quality gates reproducibly in a small, secret-free CI workflow. It must not change product semantics, the accepted core/store behavior, schema v1, the research ledger contract, or add a product feature.

The first Planner must choose the smallest useful vertical or horizontal slice. Do not attempt a broad test-suite rewrite, coverage-percentage program, release pipeline, deployment workflow, UI, live research adapter, full NUC setup or policy selection in this whole.

Why this precedes UI / live Hermes / NUC work:

- 74 tests exist, but the old `bookradar-poc` empty-history and empty-current outputs are not automatically asserted, and the research CLI empty-current output is probed manually but not automated.
- The current `.gitignore` contains only `/tests/target/`; the post-closure commit replaced `/target/` instead of adding `/tests/target/`. The worktree is clean only because `target/` is currently absent; a normal build creates untracked `target/`.
- All gates are manual; there is no `.github` workflow and no single local verification script. A small CI slice makes the existing evidence repeatable.
- The predecessor whole's process/trace friction (missing implementation report, foreign BLOCKED reports, recovered notes) is a separate Meta concern, but it reinforces the value of deterministic, single-path evidence.

Alternative next wholes considered but deferred: `bookradar-ui-shell` (visual learning can use the accepted store/research ledger) and a live Hermes/Playwright adapter (requires separate security, network, real-data and host boundaries). Selection should be revisited only for fresh material evidence or COOPERATOR redirection.

## 1. Baseline and source precedence

**Canonical repository:** `https://github.com/cisarik/bookradar`
**Public branch:** `main`
**Current public/local commit:** `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
**Subject:** `fix: update .gitignore to exclude tests target directory`
**Parent:** `ed4de54637f22613723bc3df98536a1ac25d0800`
**Tree:** `4b8a81d443393ad06eb50b4e97ded598a5bb3931`
**Commit date:** 2026-11-12T21:18:30+01:00
**Predecessor closure baseline:** `ed4de54637f22613723bc3df98536a1ac25d0800`
**Pinned AP:** `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` (immutable; detached expected checkout)
**Accepted product contract:** `docs/domain-contract.md`, revision 1, accepted 2026-11-10
**Accepted ADRs:** `docs/adr/0001`–`0005`; ADR 0005 accepted 2026-11-12

Read in precedence order:

1. Project root `AGENTS.md` and the immutable AP at the gitlink: `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, and later `.ap/PROMPT_CONTRACTS.md`, `.ap/AP_WORKER.md` as routed.
2. Current public `main` and the actual local checkout; verify refs, ancestry, tree, cleanliness, submodule and toolchain independently.
3. Accepted domain contract and ADRs 0001–0005.
4. Predecessor closure and accepted planning/implementation/acceptance/publication records as historical evidence.
5. This handout as provisional, non-authorizing context.

The post-closure commit `d7d49ab…` is part of the current baseline. It is a maintenance fix, not a reopened predecessor whole; do not rewrite it or treat it as authority for changing product semantics. Its `.gitignore` change is relevant evidence for this whole.

At authoring, the outgoing Orchestrator observed public `refs/heads/main` and symbolic `HEAD` at `d7d49ab…`, local `main`/`HEAD`/`origin/main` at the same commit, a clean worktree, `.ap` detached and clean at `d7023cf…`, and strict `ap doctor` PASS. The successor must revalidate these facts before any grant; do not infer them from this handout.

## 2. Accepted state and the test/CI gap

Current repository state at authoring:

- `bookradar-core` is dependency-free with 17 tests; it evaluates one supplied observation and explicit assessment context.
- `bookradar-store` owns schema v1 observation history plus the separate research ledger: strict JSON v1, canonical-byte replay, quarantine, partial-run accounting, candidate projection as unreviewed/disputed and no auto-verification.
- 74 tests pass at the predecessor implementation candidate: 17 core, 10 store unit, 6 persistence, 13 history, 2 old CLI, 1 research CLI, 5 research contract and 20 research ingestion.
- `docs/research-input-v1.md` and ADR 0005 are accepted; the README documents the research proof.
- No `.github` directory or CI workflow exists. No single local verification script or `justfile` exists; the README lists the gate commands manually.
- The current `.gitignore` contains exactly `/tests/target/`. The post-closure commit `d7d49ab…` changed the previous `/target/` pattern to `/tests/target/` instead of adding the latter. This is a concrete regression: a normal `cargo build` creates an untracked `target/`, even though the current worktree is clean because `target/` is absent.
- The old `bookradar-poc` CLI test runs `history` only on a populated store; it does not assert empty history or empty current output. The research CLI test asserts empty `inspect` but not empty `current`.
- The predecessor acceptance noted the empty-history assertion as a residual test-coverage gap; the research CLI empty-current path was manually probed but is not automated.
- The predecessor closure records a missing implementation report and foreign predecessor BLOCKED reports in the Meta trace. Those are process/trace defects, not code defects; they are outside this whole's code scope and must not be "fixed" by changing tests or product code.

The test/CI gap is therefore concrete and bounded:

1. restore correct ignore behavior for both `/target/` and `/tests/target/`, with a clean-worktree check;
2. add the known missing behavioral CLI assertions and any other high-value gaps found by audit;
3. add a minimal CI workflow that runs the existing gates, without secrets or deployment;
4. provide a single local/CI verification path so the same commands are used everywhere.

The new whole must preserve the accepted 74 tests and the public candidate's behavior. A test that exposes a genuine defect is a finding, not permission to change product semantics without a separate decision.

## 3. What the first Planner must evaluate

Ask a fresh Planner to inspect current repository truth and propose **one minimal executable slice** with evidence for these decisions. It must not silently promote a CI platform, action, cache, OS matrix, test framework or coverage tool to accepted architecture.

1. **As-found state and functional gap.** Verify the current public/local commit, parent/tree, AP pin, clean checkout, `.gitignore` contents, `.github` absence, README gate commands, test inventory and toolchain. Record exactly what is implemented, what is manually probed and what is missing. Do not assume the known gaps are the only gaps.

2. **Functional slice and runnable path.** Choose the smallest end-to-end hardening slice: test additions, `.gitignore` correction, one local verification path and one CI workflow. Evaluate CI-only versus a small local script plus CI. A single local/CI command path is preferred if it materially proves parity; do not build a large release infrastructure.

3. **Test-gap inventory and exact assertions.** Audit the 74 tests against the accepted contract and the two CLIs. At minimum, evaluate the old `bookradar-poc` empty `history` and empty `current` outputs, the research CLI empty `current` output, deterministic temporary-store cleanup, and any other high-value behavioral gap. Propose exact test names, inputs, expected stdout/stderr and exit codes. Do not add mirror tests that only restate implementation; every new test must name the behavior or regression it closes. No coverage-percentage target.

4. **`.gitignore` and workspace hygiene.** Restore `/target/` while keeping `/tests/target/`; verify with `git check-ignore` and a real build. Add a clean-worktree check to the local/CI gate so a future ignore regression fails. Do not rely on `.git/info/exclude`, global ignores or manual cleanup. Do not delete unrelated owner files.

5. **CI platform, triggers and permissions.** Prefer GitHub Actions because the canonical repository is on GitHub; evaluate any alternative only if materially justified. Specify exact triggers (push to `main`, pull requests to `main`, optional manual dispatch), minimal `contents: read` permissions, concurrency, and no `pull_request_target`, secrets, deployment, release or scheduled production job. One accountable workflow is preferred.

6. **CI steps and local/CI parity.** Propose the exact step order: checkout with pinned submodules; install/select Rust `1.99.1`; fetch the pinned dependency graph; build, test, fmt and clippy with `--locked --offline`; assert the core tree contains only `bookradar-core`; run `git diff --check` and strict `ap doctor`; verify `git status --porcelain` is clean after the gates. Fail fast, no `continue-on-error`. Compare duplicating commands in YAML versus a single local script invoked by CI; choose one source of truth.

7. **Toolchain, dependencies, network and caching.** Pin every third-party action by full commit SHA, not a floating tag. Compare using `actions/checkout` plus `rustup`/`rust-toolchain.toml` against a third-party Rust action. Evaluate Ubuntu-only versus macOS+Ubuntu; bundled SQLite requires a C compiler. Compare no cache, `actions/cache`, and a pinned third-party cache action. Allow network only for checkout, toolchain installation and the dependency fetch; tests remain offline. No secrets.

8. **Test infrastructure and determinism.** Ensure tests use owned temporary directories, injected times and no wall clock, network, credentials or real data. Keep process-level CLI tests isolated; avoid shared global paths and flaky concurrency. State cleanup behavior and how a failure preserves its first causal error. Do not refactor the 982-line research ingestion test file merely for style.

9. **Documentation and ADR.** Update README with the local verification command, CI status/limits and the `.gitignore` rationale. Add a status badge only if it reflects a real workflow and does not become placeholder theater. Add one implementation ADR only if a meaningful durable CI/quality policy is accepted; do not modify the domain contract or ADRs 0001–0005. No license, contribution, privacy, security-response, support or release policy.

10. **Evidence tier, acceptance and CI-run verification.** Propose E1/E2 with a rationale. Test additions and `.gitignore` may be E1; a new CI workflow with remote execution and public status may warrant E2 and fresh independent acceptance. The actual workflow run after publication is separate evidence and must be observed directly (workflow run URL/status or Cooperator-observed GitHub evidence); do not claim CI is active from the file alone. No deployment.

11. **Git and publication boundary.** Propose exact paths, one reviewable local commit, and a normal non-force push only under a separate publication grant. No force, rebase, history rewrite, tags or extra refs. The CI workflow becomes active only after the push; a post-push workflow run is a separate evidence surface.

12. **Implementation path and rollback.** Propose exact paths, ordered stages, rollback, a small local demonstration and the Git/publication boundary. If a test exposes a real product defect, stop and report it; do not silently change product semantics. If CI requires a third-party action or a repository setting that cannot be verified, surface the decision; do not guess.

## 4. Nonnegotiable boundaries

This whole does **not** authorize:

- changing product semantics, `bookradar-core` behavior, schema v1, the research wire contract, ADR 0001–0005 or the separate research ledger's accepted behavior;
- a new product feature, UI, live Hermes/Playwright adapter, scraping, external API, MCP, real retail data, screenshots, personal data, accounts, authentication, NUC, SSH, sudo, services, deployment or production;
- a release, deployment, publish, scheduled production or secret-bearing workflow; GitHub Actions must remain read-only and secret-free;
- a broad test-suite rewrite, coverage-percentage program, new heavy test framework, benchmark suite, fuzzing program or toolchain upgrade without a separate justified decision;
- force push, rebased/rewritten published history, undocumented dependency installation, unsafe cleanup or privilege inference;
- updates to `.ap`, the AP gitlink, other projects or Meta Git from a Worker;
- a new license, contribution, privacy, security-response, support or release policy without Cooperator decision.

The positive authority in a later Worker grant must name exact paths, operations, workflow file, action pins, commands, network boundaries and Git/publication authority. If the Planner proposes wider scope, hand material options to the Cooperator instead of treating them as approved.

## 5. Operating model for the fresh Orchestrator

**Stage 1 — read-only restoration.** Read the current root `AGENTS.md` and pinned AP, verify the public/local commit `d7d49ab…`, parent/tree, `.gitignore`, test inventory, `.github` absence, `.ap` pin, clean state and toolchain. Compare the predecessor closure at `ed4de54…` and the post-closure `.gitignore` commit against current evidence. Record the handout revalidation in the new whole's `00_notes.md` when the activated trace permits. Do not infer current branch, worktree or Worker state from this handout.

**Stage 2 — reconcile one bounded objective with the COOPERATOR.** Present the restored state, the test/CI gap, material uncertainty and one evidence-backed recommendation. Preserve Cooperator ownership of CI platform/OS matrix, action pinning/caching, local script versus CI duplication, test scope, evidence tier, publication and any GitHub repository setting.

**Initial Planner.** Assign a fresh Worker session `01`, exchange `01`, with **native Plan Mode required**, read-only repository inspection and a bounded implementation-planning report. The first exchange is not an implementation grant. Do not start a second implementation worker; one accountable workstream only.

**Later implementation.** After plan reconciliation and Cooperator decisions, issue a new self-contained grant with exact baseline, allowlist, workflow/action decisions, tests, and separately named Git/publication authority. If the work introduces a remote CI workflow or changes public repository settings, use the risk-appropriate acceptance and publication route. The actual CI run after publication is separate from the local implementation evidence.

**Meta trace.** Preferred new directory: `projects/bookradar/00/05-bookradar-test-hardening-and-ci/`, with `00_notes.md` on opening and this provisional handout. Worker exchange `01/01` is stored, when activated, as `01_planning_00.md` + `01_report_00.md`; later implementation/acceptance/publication coordinates follow the actual route. Preserve the predecessor process/trace residual: do not reuse foreign `02_report_00.md`/`03_report_00.md` BLOCKED reports, do not duplicate a report under the same coordinates, and keep Meta Git Cooperator-owned.

## 6. Quality standard for the test/CI slice

A credible first slice should aspire to:

- one readable local verification path and one CI workflow using the same commands, with no silent drift;
- exact behavioral tests for the known CLI gaps, not coverage-number theater;
- `.gitignore` correctness for both `/target/` and `/tests/target/`, proven by a real build and a clean `git status`;
- pinned third-party actions, minimal permissions, no secrets, no deployment or release;
- deterministic tests with no network, wall clock, credentials or real data;
- a CI workflow that checks out the pinned `.ap` submodule, selects Rust `1.99.1`, fetches only the locked dependency graph, then runs locked/offline gates;
- a fail-closed clean-worktree check after the gates;
- README and CI status that describe what is actually implemented and verified;
- a reviewable diff with no product-code changes, no unrelated refactors and no host/AP/UI/NUC side effects;
- no unsupported claim that CI is active before a public workflow run is observed.

## 7. Suggested acceptance matrix and negative evidence

| Risk/feature | Bounded evidence the Planner should require |
|---|---|
| Builds on current baseline | Local `d7d49ab…`; exact parent/tree; 74-test baseline reproduced or revalidated; AP pin and `ap doctor` PASS |
| `.gitignore` | `/target/` and `/tests/target/` both ignored; `cargo build` leaves `git status --porcelain` clean; regression test or CI check |
| Empty CLI outputs | Automated assertions for old `history`/`current` and research `current`; exact stdout and exit codes |
| Test gap closure | Each new test names a behavior/regression, not implementation mirroring; existing 74 tests preserved |
| Local/CI parity | One command path or exact equivalence between local script and workflow; no duplicated stale command lists |
| CI workflow | Pinned actions by SHA; minimal permissions; submodule checkout; Rust 1.99.1; fetch + locked/offline gates; fmt/clippy/core tree/ap doctor/clean status |
| CI safety | No secrets, deployment, release, production, scheduled job or `pull_request_target`; only necessary network |
| Public CI evidence | Actual workflow run observed after publication; no claim from the YAML alone |
| Product integrity | No core/store/schema/wire-contract/ADR changes; no feature expansion; exact diff |
| Repository integrity | Normal non-force push, direct public ref readback, unchanged AP pin and accepted contract |
| Scope fidelity | No UI, live adapter, NUC, deployment, screenshots, personal data, license/policy or release infrastructure |

For E1/E2 classification, independence and correction budgets, use the pinned AP. Do not assume test/CI work is automatically E1; a remote CI workflow and a public status surface may justify E2 and fresh acceptance.

## 8. Residual risks and decisions to surface

1. **Current `.gitignore` regression:** `d7d49ab…` replaced `/target/` instead of adding `/tests/target/`; a normal build will create untracked `target/`. Fix and verify in this whole; do not rewrite the public commit.
2. **CI platform and action supply chain:** GitHub Actions is the natural platform, but exact action pins, caching, Rust setup and permissions remain decisions; floating tags are not acceptable.
3. **OS matrix and cost:** Ubuntu-only is smallest; macOS coverage may catch native differences but doubles cost. Surface the trade-off.
4. **Local script versus CI duplication:** a single `scripts/verify.sh` or equivalent may reduce drift; adding a script is a repo path and must be justified.
5. **Test-gap scope:** empty-history/current are known; the Planner must audit for others without turning this into a suite rewrite or coverage program.
6. **CI run evidence:** the workflow file is not proof of a passing public run. Publication and post-push observation require separate authority.
7. **GitHub settings:** Actions availability, branch protection, required checks and repository permissions are Cooperator-owned; do not infer or change them.
8. **Publication boundary:** one normal non-force push only after acceptance; no deployment/release, tags or extra refs.
9. **Predecessor trace residual:** missing implementation report, foreign BLOCKED reports, recovered notes and untracked Meta files. Treat as a separate Meta/process concern; do not let it expand the code/test scope.
10. **Policy deferrals:** license, contribution, privacy, security-response, support and release policy remain undecided; do not add them as a CI convenience.

## 9. Readiness review and exact next action

| Review area | Status |
|---|---|
| Predecessor closure | PASS as recorded; `closed-by-ORCHESTRATOR` at `ed4de54…`, acceptance and publication PASS |
| Current public `main` / local checkout | Observed at `d7d49ab…` during handout authoring; **must be independently revalidated** |
| Post-closure maintenance | `d7d49ab…` changes `.gitignore` only; public/local equal; `.gitignore` regression identified |
| Accepted contract/ADRs/AP | PASS at revision 1 and ADRs 0001–0005; AP pin `d7023cf…` |
| Test/CI state | 74 tests pass at the predecessor candidate; no CI; known empty-history/current and `.gitignore` gaps |
| Cooperator's next whole intent | `bookradar-test-hardening-and-ci` selected with full trust; material CI/platform decisions remain Cooperator-owned |
| Active mutation / Worker sessions | None observed at authoring; successor must recheck |
| Security/host/provider boundaries | PASS for no live host, network, secret or deployment work planned |
| First Planner readiness | PASS **after** current-state revalidation and objective reconciliation |
| Implementation readiness | NOT GRANTED; requires Planner report, decision gate and complete mutation/publication grant |

**Next action for the per-whole Orchestrator:** open this exact handout, read the pinned AP and current repository, verify public/local state read-only, record the handout revalidation in the new `00_notes.md` when the trace permits, reconcile the bounded test/CI objective with the COOPERATOR, and issue the **first native Plan Mode Worker prompt** solely for designing the minimal test-hardening-and-CI slice. Do not ask the outgoing Orchestrator to write implementation instructions or accept the Worker result.

## 10. Artifact lifecycle and return edge

- **Class:** retained opening continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP and the accepted domain contract.
- **Consumer:** fresh per-whole Orchestrator, its initial Planner, and the upstream Master upon closure.
- **Discoverability:** exact Meta location, predecessor closure, public commit URL, AP pin and contract revision above.
- **Retention:** retain through this whole and archive after closure; material correction after opening is a separately named successor handout with predecessor/supersession links.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup decision.
- **Expected return to Master:** a truthful `xx_closure.md` with exact public commit, CI workflow/run evidence, completed scope, explicit non-achievements, current contract/AP pin, residual risks, recommended next logical whole(s), and no implied successor grant.

**Final invariant:** Harden the evidence before widening the product. One minimal CI/test slice, one accountable Orchestrator, fresh bounded Worker grants, deterministic local and public evidence, no product-semantics change, no secrets, no deployment, and no cross-project or host side effects.
