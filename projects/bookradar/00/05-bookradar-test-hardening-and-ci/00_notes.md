# BookRadar — `bookradar-test-hardening-and-ci` — Notes

Orchestrator-authored. Not task authority.

## 2026-11-13 — Whole restored read-only; handout revalidation

- Stage 2 selection: the COOPERATOR selected `bookradar-test-hardening-and-ci` with full trust, following the predecessor closure recommendation. Objective: one minimal, durable test-and-CI hardening slice that closes the known behavioral test gaps, restores correct workspace-ignore behavior, and runs the existing quality gates reproducibly in a small, secret-free CI workflow. Product semantics, core/store behavior, schema v1, the research wire contract, ADR 0001–0005 and the accepted research ledger remain unchanged. UI, live adapters, NUC, deployment, release and policy selection remain excluded.
- Orchestrator routing: fresh per-whole Orchestrator (direct project checkout), `Orchestrator session scope: logical-whole`. No Worker grant has been issued. The initial Planner is planned for fresh Worker session `01`, exchange `01`, with `Native planning mode: required`; the delivery route (manual Cooperator ferry versus authorized dispatch) is pending the COOPERATOR's selection. No coordinates are consumed until the complete prompt is issued.
- Baseline revalidated read-only on 2026-11-13:
  - Public `refs/heads/main` and symbolic `HEAD` = `d7d49ab6df2d2fd063644700095d5e55a94e4ae1` by direct `git ls-remote`.
  - Local `main`, `HEAD` and `origin/main` equal the same commit; branch is `+0 -0`; worktree clean.
  - Commit subject `fix: update .gitignore to exclude tests target directory`; parent `ed4de54637f22613723bc3df98536a1ac25d0800`; tree `4b8a81d443393ad06eb50b4e97ded598a5bb3931`; date 2026-11-12T21:18:30+01:00.
  - `.ap` gitlink and detached submodule `HEAD` = `d7023cf037f6d17885c3ede5c04812c61640da50`; submodule clean; strict `./.ap/ap doctor` PASS; resolved variant `stable`.
  - Toolchain available: Rust `1.99.1`, cargo `1.99.1`, rustfmt `1.10.0-stable`, clippy `0.1.99`, Apple clang `21.0.0`.
  - `.github` is absent; no `justfile` or local verification script is present. README lists the gates manually.
  - `.gitignore` contains exactly `/tests/target/`; `/target/` is not ignored. `git check-ignore` confirms `tests/target/` and its children are ignored and `target/` is not. No `target/` exists in the worktree.
  - The test inventory is 74 test functions: 17 core, 10 store unit, 6 persistence, 13 history, 2 old CLI, 1 research CLI, 5 research contract, 20 research ingestion. The count is unchanged from the predecessor candidate because `d7d49ab` changes only `.gitignore`. The suite was not re-executed during this read-only restoration, to avoid creating an untracked `target/` before the ignore regression is fixed.
  - Predecessor closure `projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md` SHA-256 `d8c62fb1fef6f1c33d9d9e71e4a6986c90812362e3e0809ae1d9c08fc78d9584`; provisional handout SHA-256 `95e69eb72e4d9b6f8b17c663970f2f2815867c34d6e936a8f50dc8ba581dd3dd`.
- Handout revalidation record:

```text
Handout revalidation: projects/bookradar/00/05-bookradar-test-hardening-and-ci/00_handout.md
Received handout status: provisional
Revalidated against: d7d49ab6df2d2fd063644700095d5e55a94e4ae1; AP d7023cf037f6d17885c3ede5c04812c61640da50; contract revision 1; ADRs 0001–0005; predecessor closure SHA-256 d8c62fb1fef6f1c33d9d9e71e4a6986c90812362e3e0809ae1d9c08fc78d9584
Usable facts: baseline commit/parent/tree; public/local branch equality; clean worktree; AP pin, detached state and doctor PASS; no .github or local verification script; .gitignore regression (/target/ absent, /tests/target/ present); 74-test inventory unchanged from the predecessor candidate; known empty-history/current CLI gaps; accepted contract revision 1 and ADRs 0001–0005
Stale facts and corrections: the handout's Cooperator-requested local alias `00.handout.md` does not exist; the canonical `00_handout.md` is the only handout file -> no content change required; no other material handout fact was contradicted
Not revalidated: 74-test execution (not re-run during read-only restoration; target/ absent and /target/ not ignored); GitHub Actions availability, repository permissions, branch protection and required-check settings (COOPERATOR-owned); active Worker sessions outside this trace (not observable); Meta Git cleanliness (COOPERATOR-owned; the new whole directory and predecessor trace files are untracked/modified and were not touched by Git)
Handout disposition: adopted
```

- Material findings for the Planner: the `.gitignore` regression is real and currently makes README's "ignored `target/` directory" statement inaccurate; the old `bookradar-poc` CLI does not assert empty `history` or empty `current` output; the research CLI asserts empty `inspect` but not empty `current`; the research CLI test uses a pid-based temporary directory with cleanup only at normal test end, unlike the guarded `TempDir` used by the old CLI tests. These are candidates for the bounded slice, not accepted plan decisions.
- Trace: only the provisional handout and this notes file are present in the whole directory. No prompt or report has been issued. The proposed first prompt and report destinations are `01_planning_00.md` and `01_report_00.md`, contingent on the COOPERATOR's delivery-route selection. Meta Git remains COOPERATOR-owned; no Meta Git operation was performed.
- Authority: zero beyond read-only restoration. No implementation, dependency, Git, publication, acceptance, closure or Meta Git authority is granted.
- Active mutation: none.

## 2026-11-13 — Delivery route selected; first Planner prompt prepared

- COOPERATOR routing decision: manual Cooperator ferry for the first Planner. The Orchestrator prepared the complete prompt; no dispatch is used. This preserves the actual Native Plan Mode requirement and the prior whole's delivery pattern.
- Prompt `01_planning_00.md` authored at the whole directory; SHA-256 `abf46bdffbddc0a3fac727a66e1e2488b6e4d5a23bbbf73aced511b8424a6b3b`; 403 lines. Coordinates: logical whole `bookradar-test-hardening-and-ci`, Worker session `01`, exchange `01`; `fresh-worker-session`; `Native planning mode: required`; profile `Planner`; reasoning High; approximately 250k context; plan disposition approval-gated; initial planning cycle; no targeted revision used.
- Delivery record: prompt persistence owner ORCHESTRATOR; report persistence owner COOPERATOR; Git publication owner COOPERATOR; archival wait-for-report. The Worker has `Trace persistence: none` and returns the complete report in-session; the COOPERATOR persists it at `01_report_00.md`. No Meta Git operation is authorized.
- The prompt remains read-only and forbids builds/tests, repository writes, Meta writes, fetch, dependency changes, commit, push, acceptance, publication and closure. It requires the Planner to audit the 74-test inventory, the known empty CLI outputs, the research CLI temp cleanup, the `.gitignore` regression, local/CI parity, action pins, OS matrix, caching, evidence tier and publication boundary, and to surface every material Cooperator decision.
- Delivery is pending. The prompt is prepared, not yet confirmed delivered; coordinates are consumed when it is issued to the concrete Planner session. If that session is unavailable, the next route is a genuinely fresh session `02/01`, not a reused `01/01`.
- Active mutation: none.

## 2026-11-13 — Planner report received; plan reconciliation

- `01_report_00.md` received and read: SHA-256 `073955776ff0750059a6f9d3560c801d1adfb58744a802eeb74a26c1c3747ef2`; 298 lines; coordinates `01/01`; header exact; `status: PASS`; `Phase-qualified result: not-applicable`; start/end commit `d7d49ab…`; changed files none; report justification `new-evidence`; `Logical-whole closure: not-closed`. It echoes the prompt SHA-256 `abf46bdf…`, handout `95e69eb7…` and predecessor closure `d8c62fb1…` correctly. It is a plan artifact, not acceptance.
- Plan summary: three exact process tests (`empty_history_exits_zero_with_count_zero`, `empty_current_exits_zero_with_status_empty`, `empty_research_current_exits_zero_without_candidates`) plus adoption of the guarded `common::TempDir` in the existing research CLI test; `.gitignore` restored to `/target/` and `/tests/target/`; one `bash scripts/verify.sh` source of truth; one `.github/workflows/verify.yml` using GitHub Actions, `ubuntu-24.04`, `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1) with `submodules: recursive`, `persist-credentials: false`, `fetch-depth: 1`, `contents: read`, no cache, no third-party Rust action, 20-minute timeout, no secrets/deployment/release/schedule; README update; proposed ADR 0006; E2 with fresh independent acceptance recommended before publication; one local commit `fix: restore target ignore and run the gates in CI`; publication separate and non-force.
- Orchestrator checks: the action pin was independently confirmed by `git ls-remote` (`refs/tags/v7.0.1` = `3d3c42e5aac5ba805825da76410c181273ba90b1`, `refs/tags/v7` same; `v4` = `11d5960a…`); `action.yml` at that SHA confirms `persist-credentials`, `submodules`, and `fetch-depth`; `synthetic_target()` is edition `10`, matching the proposed empty-current transcript; project worktree remains clean and `target/` absent.
- Material open item: the Planner's unauthenticated `GET /repos/cisarik/bookradar/actions/permissions` returned HTTP 401, so GitHub Actions enablement and branch protection remain unverified and COOPERATOR-owned. The report correctly recommends an authenticated check before a publication grant, not before plan acceptance.
- Report near-miss: the Planner created `/tmp/bookradar-fmt-help.txt` and `/tmp/br-actions.json` while reading help/API output and left them in place because no cleanup authority was granted. They are outside the repository, non-secret, and do not affect the plan; no cleanup mutation was performed by the Orchestrator.
- Plan disposition: pending COOPERATOR approval of the decision table (platform, OS, action pin, Rust setup, cache, local script, test scope, ADR, E2/independence, publication, badge, Actions enablement). No implementation grant has been issued.
- No implementation, acceptance, publication or closure authority is granted.
- Active mutation: none.

## 2026-11-13 — Authenticated Actions settings check

- The COOPERATOR asked for help enabling GitHub Actions and asked whether a `main.yml` workflow file is required.
- Authenticated read-only `gh api` checks (account `cisarik`; no settings mutation) returned: `actions/permissions` = `{enabled: true, allowed_actions: all, sha_pinning_required: false}`; `actions/permissions/workflow` = `{default_workflow_permissions: read, can_approve_pull_request_reviews: false}`. Actions is already enabled; the default workflow token is read-only. No repository setting change is required for the planned workflow.
- Workflow filename: no `main.yml` is required. GitHub discovers any `.github/workflows/*.yml` or `*.yaml`; the plan uses `.github/workflows/verify.yml` with display name `verify`. The filename and workflow name are independent. No `.github` directory exists yet; it will be created only in a separately authorized implementation grant.
- The Planner's earlier unauthenticated 401 was an authentication limitation, not evidence that Actions is disabled. The remaining settings question is resolved.
- Active mutation: none.

## 2026-11-13 — Plan approved; implementation grant prepared

- COOPERATOR decision: the initial plan `01_report_00.md` is approved, including all recommended rows: GitHub Actions; `ubuntu-24.04` only; `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` with `submodules: recursive`, `persist-credentials: false`, `fetch-depth: 1`; no cache; no third-party Rust action; `bash scripts/verify.sh` as the single local/CI gate; three exact CLI tests plus `common::TempDir` in the existing research CLI test; ADR 0006; E2 with fresh independent acceptance before publication; no badge; one local commit; publication in a separate grant.
- GitHub Actions is confirmed enabled through authenticated read-only API evidence; no repository setting change is required. The workflow file is `.github/workflows/verify.yml`; no `main.yml` is required.
- Implementation grant `01_implementation_01.md` prepared for the exact current Planner session: session `01`, exchange `02`, `current-worker-session`, `Native planning mode: not-used`, profile `Implementation Worker`, reasoning Medium, approximately 250k context. It carries the accepted plan, seven-path allowlist, one local commit subject `fix: restore target ignore and run the gates in CI`, no push, and a non-independent implementation evidence posture.
- Implementation prompt SHA-256: `d1fabc66b850c04b053ed7c5344238e4569e1c5fee741b25453bc90cf7e9f1e7`; 434 lines.
- Delivery: manual COOPERATOR ferry to the exact Planner session that produced `01_report_00.md`. The report returns in-session as `01_report_01.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner: COOPERATOR. Archival: wait-for-report.
- If the exact Planner session is unavailable, this current-session grant must not be pasted into a different session; a fresh-session `02/01` implementation grant is required instead.
- Implementation PASS, fresh independent acceptance, publication and closure remain separate. No push, acceptance, publication or closure authority is granted here.
- Active mutation: none until the Worker begins; local build/ignored outputs and one local commit only; no push.

## 2026-11-13 — Implementation report received; implementation-PASS; acceptance prepared

- `01_report_01.md` received and read: SHA-256 `2eac95688e02ec6e0144048a7e4e9f3fa13a736fd8161288a7616436bf3026d8`; 50 lines; coordinates `01/02`; prompt SHA-256 `d1fabc66…` matches; `status: PASS`; `Phase-qualified result: implementation-PASS`; start `d7d49ab…`; end `a2182302de73cb345b4b646993a1ad25d602555f`; tree `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`; parent `d7d49ab…`; seven allowlist paths; 77 tests; one local commit; no push; non-independent.
- Orchestrator direct verification of candidate `a218230…`: commit/parent/tree match; exactly seven changed paths (`.github/workflows/verify.yml`, `.gitignore`, `README.md`, `crates/bookradar-store/tests/cli.rs`, `crates/bookradar-store/tests/research_cli.rs`, `docs/adr/0006-verification-gate-and-ci.md`, `scripts/verify.sh`); no product source, schema, Cargo, toolchain, `.ap`, domain contract or ADR 0001–0005 changes; worktree clean; local `main` ahead 1; public `refs/heads/main` still `d7d49ab…`; `.ap` detached and clean at `d7023cf…`; strict `ap doctor` PASS; `target/` present and ignored by `/target/`; `git check-ignore` names `/target/` and `/tests/target/`; `README.md` not ignored.
- Orchestrator executed `bash scripts/verify.sh` on the clean candidate: exit 0; 77 tests passed (17 core, 10 store unit, 4 old CLI, 13 history, 6 persistence, 2 research CLI, 5 research contract, 20 research ingestion; 0 doc/bin tests); fmt, clippy, locked/offline build, core-tree one-line check, `git diff --check` and strict `ap doctor` all passed; final porcelain empty.
- Implementation PASS is accepted for the non-independent candidate. It is not acceptance, publication or closure. The plan's E2 route requires a fresh independent acceptance before publication.
- Next route: fresh Worker session `02`, exchange `01`, `fresh-worker-session`, `Native planning mode: not-used`, profile `Fresh Independent Audit`, read-only acceptance of `a218230…`; prompt `02_acceptance_00.md`; report `02_report_00.md`; prompt persistence ORCHESTRATOR; report persistence COOPERATOR; no publication.
- Acceptance prompt SHA-256: `e091f8db7b8fb083fe3ed1dfe8d3b3d2f0d36e2a5911ee18ecdc56501926a087`; 352 lines. Delivery: genuinely fresh manual session, Native Plan Mode OFF; no inherited Planner/Implementation conversation; report returns in-session and is persisted by the COOPERATOR at `02_report_00.md`.
- Active mutation: local candidate only; no push.

## 2026-11-13 — Acceptance report received; acceptance-PASS; publication decision

- `02_report_00.md` received and read: SHA-256 `4fca20d8b87db34ba8e38d2db1985d23791fed27fd5e3deb50a658cb34087193`; 80 lines; coordinates `02/01`; prompt SHA-256 `e091f8…` matches; `status: PASS`; `Phase-qualified result: acceptance-PASS`; candidate `a2182302de73cb345b4b646993a1ad25d602555f`; changed files none; no Git write; independence stated; report justification `final-acceptance`; `Logical-whole closure: not-closed`.
- The acceptance reports C1–C12 PASS: exact seven-path candidate, two-line `.gitignore` with exact pattern checks, 77 tests including the three new exact CLI tests and `TempDir` cleanup, fail-closed `scripts/verify.sh`, pinned/read-only workflow, README/ADR consistency, no product or dependency changes, public `main` still `d7d49ab…`, no push, and no public-run claim. It ran `bash scripts/verify.sh` exit 0 and strict `ap doctor` PASS.
- Orchestrator reconciliation: the acceptance report's candidate, prompt, scope, test count and gate claims match the Orchestrator's own direct verification. Acceptance PASS is accepted for candidate `a218230…`. No correction is indicated.
- Next decision: a separate COOPERATOR authorization for one normal non-force publication push to `origin/main` and read-only observation of the `verify` workflow run. No push, publication grant or CI-run claim exists yet.
- Active mutation: local candidate only; no push.

## 2026-11-13 — Publication authorized; publication grant prepared

- COOPERATOR decision: authorize one normal non-force publication push of the accepted candidate `a2182302de73cb345b4b646993a1ad25d602555f` to `origin/main`, followed by direct public readback and read-only observation of the `verify` workflow run. No force, tags, rebase, settings change, deployment or release.
- Publication grant `03_publication_00.md` prepared for a genuinely fresh publication session: session `03`, exchange `01`, `fresh-worker-session`, `Native planning mode: not-used`, profile `Fresh Publication Worker`, independence not required (this is publication separation, not an independent acceptance). It carries the accepted candidate, expected public parent `d7d49ab…`, expected tree `9a922bf…`, one normal non-force `git push origin main`, direct readback, and bounded read-only CI observation.
- Delivery: manual COOPERATOR ferry to a fresh session, Native Plan Mode OFF. The report returns in-session as `03_report_00.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner for Meta: COOPERATOR. Archival: wait-for-report.
- If the public `main` is no longer `d7d49ab…`, the local candidate or AP pin differs, or the push is rejected/non-fast-forward, the Worker stops; no force. If the CI run fails or is not observed, the Worker reports it; no correction or settings change is authorized in this grant.
- Publication prompt SHA-256: `813366a19720cdd49be207d00cbf219e16302e7e94947c41fec035793236a7bf`; 257 lines. Delivery: fresh manual session, Native Plan Mode OFF; report returns in-session and is persisted by the COOPERATOR at `03_report_00.md`.
- Publication PASS, CI-run evidence and logical-whole closure remain separate. Closure is not authorized here.
- Active mutation: local candidate only until the Worker pushes; then one public fast-forward ref update.

## 2026-11-13 — Publication PASS; CI run success; closure conditions satisfied

- `03_report_00.md` received and read: file SHA-256 `35b875a0b250e545cb71f154212328f0f105aa79d165eeca1764103b5fbc69af`; 42 lines; formal report core SHA-256 `72749a97bb0ff10a095e1f69771bbcf11b7d8630aefa2022734d32bf839ba0d0`; coordinates `03/01`; prompt SHA-256 `813366…` matches; `status: PASS`; `Phase-qualified result: publication-PASS`; candidate `a218230…`; changed files none; report justification `changed-external-state`; `Logical-whole closure: not-closed`.
- Publication result: one normal non-force fast-forward push `d7d49ab..a218230 main -> main`; direct public readback `refs/heads/main` and symbolic `HEAD` equal `a2182302de73cb345b4b646993a1ad25d602555f`; local `main` is `+0 -0`; worktree clean; public commit metadata shows parent `d7d49ab…`, tree `9a922bf…`, subject `fix: restore target ignore and run the gates in CI`; `.ap` pin unchanged and clean; strict `ap doctor` PASS.
- CI evidence independently verified by the Orchestrator: workflow `verify`, run `43438422059`, URL `https://github.com/cisarik/bookradar/actions/runs/43438422059`, event `push`, head SHA `a2182302de73cb345b4b646993a1ad25d602555f`, status `completed`, conclusion `success`, created `2026-11-13T13:58:52Z`, updated `2026-11-13T13:59:22Z`.
- Publication PASS is accepted for the exact candidate. All closure prerequisites are satisfied: implementation-PASS, acceptance-PASS, publication-PASS, CI success, Cooperator decisions, no residual material risk requiring a new decision, no active mutation. The Orchestrator is authoring `01_closure.md`.
- Trace note: the saved `03_report_00.md` includes the Worker's informal localized completion notice after the formal report core. The core hash `72749a97…` matches the Worker's notice; the file hash `35b875a0…` includes the notice. The core report is valid; no rewrite was performed, and Meta Git remains COOPERATOR-owned.
- Active mutation: none.

## 2026-11-13 — Closure authored; notes frozen

- Closure `01_closure.md` authored at the whole directory; SHA-256 `9c157d4935020e56056eacbb9251905ee31284fad72444654ed5d7d672ae4b2b`; 248 lines; `closed-by-ORCHESTRATOR`.
- Closure record: `publication-PASS` for `a2182302de73cb345b4b646993a1ad25d602555f`; required preceding results satisfied; Cooperator-owned decisions satisfied; residual-risk disposition satisfied; upgrade-ledger reconciliation complete; active mutation none; closure actor ORCHESTRATOR.
- Final verified state: public `refs/heads/main` and symbolic `HEAD` = `a218230…`; local `main` `+0 -0`; clean worktree; AP pin `d7023cf…` unchanged; strict `ap doctor` PASS; CI run `43438422059` conclusion `success`.
- Recommended next whole: `bookradar-ui-shell`; live Hermes/Playwright, NUC and deployment remain later separately authorized wholes. No successor grant is implied.
- Meta Git remains COOPERATOR-owned; the whole directory is untracked and no Meta Git operation was performed. Notes are frozen at closure; no further entries.








