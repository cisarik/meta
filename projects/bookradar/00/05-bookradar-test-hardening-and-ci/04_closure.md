# BookRadar — Closure: `bookradar-test-hardening-and-ci`

**Artifact:** `projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_closure.md`
**Kind:** closing continuity and handoff artifact for a completed logical whole. Not a Worker prompt, task authority, implementation plan, acceptance report, publication report, or grant.
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-13.
**Target:** the upstream Master ChatOrchestrator and the next logical-whole selection.
**Capability profile: Orchestrator**
**Orchestrator session scope: logical-whole**
**Closure status:** `closed-by-ORCHESTRATOR`
**Restoration classification:** PASS for selecting and preparing the next logical whole, conditional on the successor revalidating mutable facts. This grants no mutation authority.
**Filename basis:** Meta handoff/closure sequence; next prefix after the opening `00` position, independent of Worker exchange suffixes.

## 1. Closure record

```text
Phase-qualified result: publication-PASS
Result artifact or commit: a2182302de73cb345b4b646993a1ad25d602555f
Result evidence: exact public ref and symbolic HEAD equality; public commit parent/tree/subject; CI run 43438422059 success; implementation-PASS and acceptance-PASS; 77 tests; strict ap doctor PASS; clean worktree
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

`publication-PASS` is the final phase result; `acceptance-PASS` and
`implementation-PASS` preceded it. No deployment or production acceptance
applies. No upgrade ledger is activated; `Upgrade-ledger reconciliation:
complete` records that there was nothing to reconcile.

## 2. Verified result

Canonical repository: `https://github.com/cisarik/bookradar`
Published branch: `main`
Public commit: `a2182302de73cb345b4b646993a1ad25d602555f`
Public commit URL: <https://github.com/cisarik/bookradar/commit/a2182302de73cb345b4b646993a1ad25d602555f>
Commit subject: `fix: restore target ignore and run the gates in CI`
Parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Commit date: 2026-11-13T14:17:54+01:00

The commit changes exactly seven paths, adding 265 lines and removing 22:

| Path | Purpose |
|---|---|
| `.gitignore` | Restores `/target/` and keeps `/tests/target/` |
| `scripts/verify.sh` | Single fail-closed local and CI gate |
| `.github/workflows/verify.yml` | Read-only, pinned GitHub Actions verification workflow |
| `crates/bookradar-store/tests/cli.rs` | Empty-history and empty-current process tests |
| `crates/bookradar-store/tests/research_cli.rs` | Empty research-current test and guarded `TempDir` reuse |
| `README.md` | Names the gate, corrects the ignore rationale, states CI limits, links ADR 0006 |
| `docs/adr/0006-verification-gate-and-ci.md` | Accepted verification-gate policy |

The core sources, store sources, schema, research wire contract, domain
contract, ADRs 0001–0005, `Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`,
`.ap` gitlink, `research_ingestion.rs` and `tests/common/mod.rs` are unchanged.
The two existing CLI test files were extended without removing any prior
assertion.

Direct public readback:

```text
ref: refs/heads/main    HEAD
a2182302de73cb345b4b646993a1ad25d602555f    HEAD
a2182302de73cb345b4b646993a1ad25d602555f    refs/heads/main
```

Local `main` equals `origin/main` and `HEAD`; the branch is `+0 -0`; the
worktree is clean apart from ignored `target/`. The push was one normal
non-force fast-forward `d7d49ab..a218230 main -> main`. Public commit metadata
shows the expected parent, tree and subject.

CI evidence, independently observed by the Orchestrator:

```text
Workflow: verify
Run: 43438422059
URL: https://github.com/cisarik/bookradar/actions/runs/43438422059
Event: push
Head SHA: a2182302de73cb345b4b646993a1ad25d602555f
Status: completed
Conclusion: success
Created: 2026-11-13T13:58:52Z
Updated: 2026-11-13T13:59:22Z
```

AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`; `.ap` remains detached and
clean. Strict `./.ap/ap doctor` PASS. The domain contract remains revision 1.
ADR 0006 is accepted; ADRs 0001–0005 are unchanged.

## 3. Scope completed

- Restored correct workspace-ignore behavior: `/target/` is the workspace
  build directory and `/tests/target/` remains for a nested cargo output.
- Added three exact behavioral CLI tests:
  `empty_history_exits_zero_with_count_zero`,
  `empty_current_exits_zero_with_status_empty`, and
  `empty_research_current_exits_zero_without_candidates`.
- Reused the guarded `common::TempDir` in the existing research CLI transcript
  test, preserving all prior assertions and removing the pid-based cleanup
  leak on assertion failure.
- Added `scripts/verify.sh` as the single local and CI gate: fail-closed dirty
  worktree check, Rust `1.99.1` check, exact ignore-pattern checks, locked
  dependency fetch, locked/offline build, test, formatting, clippy, one-line
  core-tree check, `git diff --check`, strict `ap doctor`, and a final clean
  worktree check.
- Added `.github/workflows/verify.yml`: GitHub Actions on `ubuntu-24.04`, push
  to `main`, pull requests to `main`, manual dispatch, `contents: read`,
  bounded concurrency, 20-minute timeout, and `actions/checkout` pinned to
  `3d3c42e5aac5ba805825da76410c181273ba90b1` with submodules, no persisted
  credentials and fetch depth 1.
- Added README gate/CI documentation and accepted ADR 0006.
- Published the accepted candidate and observed a successful public CI run.

No product semantics, schema v1, research ledger contract, research wire
contract, domain contract, ADR 0001–0005, dependency, lockfile, toolchain or AP
pin changed. The core remains dependency-free.

## 4. Evidence

- 77 tests pass: 17 core, 10 store unit, 4 old CLI, 13 history, 6 persistence,
  2 research CLI, 5 research contract and 20 research ingestion. Doc-tests and
  binary unit targets add zero. The preserved 74 tests and the three new tests
  all passed in the public CI run and in the Orchestrator's local gate.
- Planning report `01_report_00.md`, SHA-256
  `073955776ff0750059a6f9d3560c801d1adfb58744a802eeb74a26c1c3747ef2`.
- Implementation report `01_report_01.md`, SHA-256
  `2eac95688e02ec6e0144048a7e4e9f3fa13a736fd8161288a7616436bf3026d8`;
  `implementation-PASS` for `a218230…`.
- Acceptance report `02_report_00.md`, SHA-256
  `4fca20d8b87db34ba8e38d2db1985d23791fed27fd5e3deb50a658cb34087193`;
  `acceptance-PASS` for `a218230…`; fresh independent session `02/01`; all
  controls C1–C12 passed; no correction.
- Publication report `03_report_00.md`, file SHA-256
  `35b875a0b250e545cb71f154212328f0f105aa79d165eeca1764103b5fbc69af`;
  formal report core SHA-256
  `72749a97bb0ff10a095e1f69771bbcf11b7d8630aefa2022734d32bf839ba0d0`;
  `publication-PASS`.
- Prompt hashes: planning `abf46bdffbddc0a3fac727a66e1e2488b6e4d5a23bbbf73aced511b8424a6b3b`;
  implementation `d1fabc66b850c04b053ed7c5344238e4569e1c5fee741b25453bc90cf7e9f1e7`;
  acceptance `e091f8db7b8fb083fe3ed1dfe8d3b3d2f0d36e2a5911ee18ecdc56501926a087`;
  publication `813366a19720cdd49be207d00cbf219e16302e7e94947c41fec035793236a7bf`.
- Public CI run `43438422059`, conclusion `success`, head SHA `a218230…`,
  observed directly after publication.
- Direct public readback and public commit metadata match the accepted
  candidate. `ap doctor` PASS; AP pin unchanged.

## 5. Non-achievements and deferrals

- No user interface, live Hermes/Playwright ingestion, scraping, external API,
  MCP, real retail data, screenshots, personal data, accounts, authentication,
  NUC, SSH, sudo, services, deployment, release, production job or secret-bearing
  workflow.
- No macOS CI, dependency cache, third-party Rust action, status badge,
  scheduled workflow, branch protection or required-check configuration.
- No change to product semantics, schema v1, the research ledger or wire
  contract, the domain contract or ADRs 0001–0005.
- No new dependency, lockfile update, toolchain change or AP update.
- No license, contribution, privacy, security-response, support or release
  policy.
- No claim that the CI workflow proves future commits or production behavior.

## 6. Residual risks and process/trace defects

- `ubuntu-24.04` is a hosted runner label that can change inside its image. The
  script's exact Rust `1.99.1` check and the full-suite gate fail closed if the
  image drifts. The `actions/checkout` pin is an exact full SHA; future action
  updates require a separate reviewed change.
- Future CI runs depend on GitHub Actions availability and repository settings.
  Actions is confirmed enabled with an all-actions allowlist and read-only
  default workflow permissions. No branch protection or required-check setting
  was configured; those remain COOPERATOR-owned and were not needed for this
  slice.
- No cache was selected. Runs recompile bundled SQLite on a cold runner; the
  20-minute timeout bounds the cost. A later cache decision requires a separate
  supply-chain and cold-run review.
- No status badge was added. The README does not claim a green run; this closure
  records the observed run separately.
- The saved `03_report_00.md` includes the publication Worker's informal
  localized completion notice after the formal report core. The core hash
  `72749a97…` is valid; the file hash `35b875a0…` includes the notice. No rewrite
  was performed, and Meta Git remains COOPERATOR-owned. This is a minor
  trace-persistence deviation, not a code or acceptance defect.
- The planning exchange created `/tmp/bookradar-fmt-help.txt` and
  `/tmp/br-actions.json` while reading help/API output and left them because no
  cleanup authority was granted. They are non-secret, outside the repository,
  and do not affect the result.
- The predecessor whole's missing implementation report and duplicate foreign
  BLOCKED reports are historical trace defects. This whole produced its
  planning, implementation, acceptance and publication reports; no foreign
  report was reused.
- Meta Git remains COOPERATOR-owned. The whole directory is untracked in Meta;
  no Meta Git operation was performed. The COOPERATOR decides whether and when
  to commit the trace.
- The local `target/` directory contains ignored build artifacts. It is not
  tracked; no cleanup was performed.

## 7. Pins and durable owners

- Public BookRadar commit: `a2182302de73cb345b4b646993a1ad25d602555f`.
- Public CI run: `43438422059`, `verify`, conclusion `success`, head SHA
  `a2182302de73cb345b4b646993a1ad25d602555f`.
- AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Product contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10.
- ADRs 0001–0005 accepted and unchanged; ADR 0006 accepted 2026-11-13.
- Verification owners: `scripts/verify.sh`, `.github/workflows/verify.yml`,
  `README.md`, ADR 0006.
- No active upgrade ledger.

## 8. Recommended next logical whole(s)

Recommended next whole: `bookradar-ui-shell` — a small synthetic/store-backed
view of the accepted history and research ledger. It can build on the accepted
store and research contract without a live adapter. UI acceptance will need its
own browser/Cooperator evidence and security boundaries.

A later candidate: a live Hermes/Playwright research adapter, which requires
separate network, real-data, security, host and operational boundaries.
Deployment, NUC operation, release automation and policy selection remain later
separately authorized wholes.

Neither recommendation selects or grants a successor whole.

## 9. Artifact lifecycle and return edge

- **Class:** retained closing continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP
  and the accepted domain contract.
- **Consumer:** upstream Master ChatOrchestrator, the next per-whole
  Orchestrator, and later reviewers.
- **Discoverability:** exact Meta location, public commit URL, CI run URL, AP
  pin, contract revision, ADR 0006, and the four Worker exchange reports.
- **Retention:** retain through the next selection and archive after closure;
  material correction after closure is a separately named successor artifact.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup
  decision.
- **Expected return to Master:** this truthful closure with exact public commit,
  CI workflow/run evidence, completed scope, explicit non-achievements, current
  contract/AP pin, residual risks, recommended next logical wholes, and no
  implied successor grant.

**Closure signal:** `closed-by-ORCHESTRATOR`

**Final invariant:** Evidence durability now matches product truth: one minimal
fail-closed gate, one observed green public run, 77 tests, correct workspace
ignore behavior, no product-semantics change, no secrets, and no deployment.
