# BookRadar — Publication — Minimal Local Read-Only UI Shell

Persistent role identity: WORKER
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: BOOKRADAR-UI-SHELL-PUBLISH
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — deterministic, bounded single-ref publication with exact pre/post identity checks and read-only CI observation; no design or code mutation is authorized.
Recommended context capacity: approximately 250k tokens
Independence required: no

Publication candidate: 2281982f7dae0ef1f582d294592c41281ba11b21
Acceptance PASS reference: `03_report_00.md` SHA-256 `525afe9783b7c2656b0aeb2ec2f60b31d6a5e25b7d6417db892027b659b5c563`; `acceptance-PASS` for this candidate, plus COOPERATOR rendered acceptance sign-off
Publication expected public ref: `refs/heads/main`
Publication expected public parent: `a2182302de73cb345b4b646993a1ad25d602555f`
Publication expected public tree: `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`
Publication mode: normal non-force fast-forward push (`git push --no-follow-tags origin HEAD:refs/heads/main` or `git push origin main`)
Publication authority: explicit

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-ui-shell
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_publication_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Report filename: 04_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: one normal non-force push of `2281982f7dae0ef1f582d294592c41281ba11b21` to `refs/heads/main` at `https://github.com/cisarik/bookradar`; read-only public commit and CI-run observation
Trace persistence: none

## Delivery and authority posture

You are a genuinely fresh WORKER in the `Fresh Publication Worker` profile
(`Worker session ordinal: 04`, `Worker exchange ordinal: 01`, `Worker session
target: fresh-worker-session`, `Native planning mode: not-used`). This is a
bounded publication task, not an independent acceptance; `acceptance-PASS` (`03_report_00.md`,
SHA-256 `525afe9783b7c2656b0aeb2ec2f60b31d6a5e25b7d6417db892027b659b5c563`)
and COOPERATOR rendered acceptance sign-off are already recorded.

Open a fresh Worker session with Native Plan Mode OFF. Do not edit, correct,
rebuild, commit, amend, rebase, force, tag, or change repository settings. If
any pre-push gate fails, stop and report `BLOCKED`. Do not push a second time
after a partial failure. Do not claim logical-whole closure.

Return the complete terminal publication report in this session; the COOPERATOR
will persist it at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/04_report_00.md`.
The received prompt is persisted at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/04_publication_00.md`;
read it to verify identity and echo its SHA-256 in your report. Do not modify
any file in the repository or under `/Users/agile/meta`.

## Repository and pre-push identity gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected local HEAD: `2281982f7dae0ef1f582d294592c41281ba11b21`
Expected parent: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected tree: `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`
Expected subject: `feat: add a local read-only UI shell`
Expected public `refs/heads/main`: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected local state: `main` one commit ahead of `origin/main`; clean worktree (`git status --porcelain` empty; `target/` ignored by `/target/`)
Governing AP: `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`

Before pushing, verify all of the following read-only:

1. Physical root `/Users/agile/Projects/bookradar` and remote `https://github.com/cisarik/bookradar`; active branch `main`.
2. Local `HEAD` is `2281982f7dae0ef1f582d294592c41281ba11b21`; `HEAD^` is `a2182302de73cb345b4b646993a1ad25d602555f`; `HEAD^{tree}` is `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`; commit subject is `feat: add a local read-only UI shell`.
3. `git status --porcelain` is empty.
4. `.ap` is detached at `d7023cf037f6d17885c3ede5c04812c61640da50` and clean; strict `./.ap/ap doctor` PASS.
5. `git diff-tree --no-commit-id --name-status -r HEAD` names exactly the 18 accepted paths:
   - `Cargo.lock` (M)
   - `Cargo.toml` (M)
   - `README.md` (M)
   - `crates/bookradar-store/src/history.rs` (M)
   - `crates/bookradar-store/src/lib.rs` (M)
   - `crates/bookradar-ui/Cargo.toml` (A)
   - `crates/bookradar-ui/src/config.rs` (A)
   - `crates/bookradar-ui/src/http.rs` (A)
   - `crates/bookradar-ui/src/lib.rs` (A)
   - `crates/bookradar-ui/src/main.rs` (A)
   - `crates/bookradar-ui/src/render.rs` (A)
   - `crates/bookradar-ui/src/snapshot.rs` (A)
   - `crates/bookradar-ui/src/style.css` (A)
   - `crates/bookradar-ui/tests/cli.rs` (A)
   - `crates/bookradar-ui/tests/common/mod.rs` (A)
   - `crates/bookradar-ui/tests/http.rs` (A)
   - `crates/bookradar-ui/tests/render.rs` (A)
   - `docs/adr/0007-local-read-only-ui-shell.md` (A)
6. `03_report_00.md` exists at `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/03_report_00.md` with SHA-256 `525afe9783b7c2656b0aeb2ec2f60b31d6a5e25b7d6417db892027b659b5c563`.
7. Direct `git ls-remote origin refs/heads/main` equals the expected public parent `a2182302de73cb345b4b646993a1ad25d602555f`.

If any check differs, stop and report `BLOCKED`; do not repair, force, fetch,
rebase, or push.

## Publication action

The only authorized remote mutation is one normal non-force fast-forward push:

```sh
git push --no-follow-tags origin HEAD:refs/heads/main
```

Do not use `--force`, `--force-with-lease`, `+refs`, tags, alternate refs, or
any remote configuration change. If the push is rejected or is not a
fast-forward, stop and report the exact output; do not retry with force.

## Post-push verification and CI observation

After the push succeeds, verify directly:

1. `git ls-remote origin refs/heads/main` equals `2281982f7dae0ef1f582d294592c41281ba11b21`.
2. `git ls-remote --symref origin HEAD` reports `ref: refs/heads/main	HEAD` and `2281982f7dae0ef1f582d294592c41281ba11b21`.
3. Local `HEAD` remains `2281982f7dae0ef1f582d294592c41281ba11b21` and `git status --porcelain` remains empty.
4. Read-only public commit metadata via `gh api repos/cisarik/bookradar/commits/2281982f7dae0ef1f582d294592c41281ba11b21` shows `sha` `2281982f7dae0ef1f582d294592c41281ba11b21`, parent `a2182302de73cb345b4b646993a1ad25d602555f`, tree `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`, and subject `feat: add a local read-only UI shell`.
5. Observe the `verify` GitHub Actions workflow run for `headSha` `2281982f7dae0ef1f582d294592c41281ba11b21` read-only:
   ```sh
   gh run list --repo cisarik/bookradar --workflow verify.yml --branch main --limit 5 \
     --json databaseId,headSha,status,conclusion,url,createdAt
   ```
   Wait for the run with `headSha == 2281982f7dae0ef1f582d294592c41281ba11b21` to complete (bounded wait up to 20 minutes):
   ```sh
   gh run watch <run-id> --repo cisarik/bookradar --exit-status
   ```
   Record the exact run ID, URL, `headSha`, `status`, and `conclusion`.

## Positive and negative authority

- **Positive authority:** Read-only local Git and repository inspection; one
  normal non-force `git push --no-follow-tags origin HEAD:refs/heads/main`;
  `git ls-remote`; read-only public commit and CI-run queries via `gh api` /
  `gh run`; `shasum -a 256` for artifact identity. No local build or test run
  is needed (already verified in `03_report_00.md`).
- **Negative authority:** No file edits, no commits, no amend/rebase/reset/clean/stash/tag/fetch/force,
  no second push, no GitHub settings changes, no secrets inspection, no
  deployment or release, no Meta writes, and no closure signal.

## Report contract

Return the complete terminal publication report in this session; the COOPERATOR
will save it at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/04_report_00.md`.
Do not append an informal post-report footer inside the report body. Begin
exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinates once at the top of the report metadata:

```text
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 04
Worker exchange ordinal: 01
```

Include the compact core:
- `status: PASS | PARTIAL | BLOCKED` (`PASS` with `publication-PASS` when public `refs/heads/main` and symbolic `HEAD` equal `2281982f7dae0ef1f582d294592c41281ba11b21`, commit metadata matches, and the `verify` CI run reaches `conclusion: success`; `PARTIAL` with `publication-PASS` if public ref matches but CI run failed or was not observed; `BLOCKED` with `not-applicable` if pre-push gate or push failed)
- `Phase-qualified result: publication-PASS | not-applicable`
- `Result artifact or commit: 2281982f7dae0ef1f582d294592c41281ba11b21`
- `Result evidence: <direct git ls-remote, gh api commit metadata, and gh run verify evidence>`
- `Start commit: 2281982f7dae0ef1f582d294592c41281ba11b21`
- `End commit: 2281982f7dae0ef1f582d294592c41281ba11b21`
- `Changed files: none`
- `Tests and validation: acceptance reference 03_report_00.md (SHA-256 525afe9783b7c2656b0aeb2ec2f60b31d6a5e25b7d6417db892027b659b5c563) and observed public verify CI run <id>`
- `Git result: one normal non-force fast-forward push a218230..2281982 main -> main; direct public readback`
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: ORCHESTRATOR reconciles publication-PASS and CI evidence and evaluates logical-whole closure`
- `Report justification: changed-external-state`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the publication grant; no autonomous continuation.`
- Echo the SHA-256 of `04_publication_00.md` and include:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>
Pre-Existing Failure Classification: none | <complete classification per the contract>
```
