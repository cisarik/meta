# BookRadar — Publication — Test Hardening and CI Slice

Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: BOOKRADAR-TEST-HARDENING-AND-CI-PUBLISH
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — deterministic, bounded single-ref publication with exact pre/post identity checks and read-only CI observation; no design or correction is authorized.
Recommended context capacity: approximately 250k tokens
Independence required: no

Publication candidate: a2182302de73cb345b4b646993a1ad25d602555f
Acceptance PASS reference: `02_report_00.md` SHA-256 `4fca20d8b87db34ba8e38d2db1985d23791fed27fd5e3deb50a658cb34087193`; `acceptance-PASS` for this candidate
Publication expected public ref: `refs/heads/main`
Publication expected public parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Publication expected public tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Publication mode: normal non-force fast-forward push
Publication authority: explicit

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
Downloadable prompt filename: 03_publication_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: one normal non-force `git push origin main` to `https://github.com/cisarik/bookradar`; read-only public commit and CI-run observation
Trace persistence: none

## Delivery and independence posture

You are a genuinely fresh WORKER in the Fresh Publication Worker profile. This
is a bounded publication task, not an independent acceptance. The COOPERATOR
authorized one normal non-force push of the already accepted candidate. The
COOPERATOR must open a fresh session with Native Plan Mode OFF and paste this
prompt there. Do not use the Planner, Implementation, or Acceptance session.
Freshness separates publication context; it is not an independence claim, and
the acceptance PASS is already recorded.

The current prompt is your only task authority. Do not edit, correct, rebuild,
commit, amend, rebase, force, tag, or change repository settings. If a check
fails, stop and report. Do not push a second time after a partial failure. Do
not claim logical-whole closure.

The received prompt is persisted at
`/Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci/03_publication_00.md`.
You may read it to verify identity and compute its SHA-256; do not modify it.
Echo the SHA-256 in your report.

## Repository and pre-push identity gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected local HEAD: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Expected subject: `fix: restore target ignore and run the gates in CI`
Expected public `refs/heads/main`: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected local state: `main` one commit ahead of the public parent; clean worktree
Governing AP: `.ap` gitlink and detached checkout
`d7023cf037f6d17885c3ede5c04812c61640da50`

Before the push, verify all of the following read-only:

- root and remote are the canonical repository; branch is `main`;
- local HEAD is the candidate; `HEAD^` is the expected parent; `HEAD^{tree}` is
  the expected tree; subject matches;
- `git status --porcelain` is empty; `target/` may exist and is ignored;
- `.ap` is detached at the pin, clean; strict `./.ap/ap doctor` PASS;
- `git diff-tree --no-commit-id --name-status -r HEAD` names exactly the seven
  accepted paths: `.github/workflows/verify.yml`, `.gitignore`, `README.md`,
  `crates/bookradar-store/tests/cli.rs`,
  `crates/bookradar-store/tests/research_cli.rs`,
  `docs/adr/0006-verification-gate-and-ci.md`, `scripts/verify.sh`;
- direct `git ls-remote origin refs/heads/main` equals the expected public
  parent `d7d49ab…`.

If any check differs, stop and report `BLOCKED`; do not repair, force, fetch,
rebase or push. If public `main` has advanced, stop; a new publication decision
is required.

## Publication action

The only authorized remote mutation is exactly:

```sh
git push origin main
```

This must be a normal non-force fast-forward push. Do not use `--force`,
`--force-with-lease`, `+refs`, a tag, an alternate ref, `--mirror`, or any
remote configuration change. Do not create a commit. If the push is rejected
or is not a fast-forward, stop and report the exact output; do not retry with
force.

## Post-push verification

After a successful push, verify directly:

- `git ls-remote origin refs/heads/main` equals
  `a2182302de73cb345b4b646993a1ad25d602555f`;
- `git ls-remote --symref origin HEAD` reports `ref: refs/heads/main HEAD` and
  the candidate;
- local HEAD remains the candidate and `git status --porcelain` remains empty;
- read-only public commit metadata, through `gh api` or the public API, shows
  the candidate SHA, parent `d7d49ab…`, tree `9a922bf…`, and the expected
  subject. Do not use a write token or change settings.

Then observe the `verify` workflow run for the pushed commit, read-only:

```sh
gh run list --repo cisarik/bookradar --workflow verify.yml --branch main --limit 5 \
  --json databaseId,headSha,status,conclusion,url,createdAt
```

Find the run whose `headSha` equals the candidate. If it is not listed yet,
retry a bounded number of times for up to five minutes; do not poll
indefinitely. Then observe that run to a terminal state with a total bounded
wait of no more than 25 minutes:

```sh
gh run watch <run-id> --repo cisarik/bookradar --exit-status
```

or equivalent repeated read-only `gh run view <run-id> --json
status,conclusion,headSha,url` calls. Report the run id, URL, head SHA, status
and conclusion exactly.

If `gh` is unavailable, use the public GitHub API through `curl` or `webfetch`
read-only. If the run cannot be observed within the bound, report it as
`not observed` with the current status; do not guess, re-run, or change
settings.

A successful publication is established by the public ref readback. A CI run
conclusion is separate evidence. Do not claim a green public run from the
workflow file, and do not treat a missing run as a publication failure.

## Positive and negative authority

Positive authority: read-only local Git and repository inspection; one exact
`git push origin main`; `git ls-remote`; read-only public commit and CI-run
queries through `gh api`/`gh run`/`curl`/`webfetch`; `shasum` for identity.
No build or test suite is required; the acceptance already ran the gate.

Negative authority: no source, test, script, workflow, README, ADR, Cargo,
toolchain, `.ap`, domain-contract or ADR 0001–0005 edits; no new commit,
amend, rebase, reset, clean, stash, tag, branch, extra ref, fetch into the
repository or force; no second push after a partial failure; no GitHub
settings, secret, token printing, deployment, release, production mutation,
Meta write, acceptance, publication retry, or closure. Do not use the
Planner/Implementation/Acceptance session.

## Network, secrets, and side effects

Network authority: the single push, read-only `git ls-remote`, and read-only
public commit/CI metadata. No other network. Secret authority: none; do not
print or inspect credentials or tokens. The push may use the environment's
existing Git credential helper; that is transport, not a new secret grant.
Host/remote mutation: exactly the one normal non-force `refs/heads/main` push
and read-only public observation. No SSH, service, sudo, deployment or release.

## Report contract

Return the terminal publication report in this session; the COOPERATOR
persists it at `03_report_00.md`. Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

```text
Logical whole identity: bookradar-test-hardening-and-ci
Worker session ordinal: 03
Worker exchange ordinal: 01
```

Include the compact core: status; `Phase-qualified result: publication-PASS`
only when the expected candidate is the public `refs/heads/main` and direct
readback matches; start and end commit `a218230…`; changed files none; tests
and validation (acceptance reference and the observed CI run); Git result (one
normal non-force push, public readback); deviations, risks or missing evidence;
the one smallest next step; report justification `changed-external-state`;
authority-expiry statement; and:

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

and `Logical-whole closure: not-closed`. Do not emit a closure signal.

Status semantics:

- `PASS` with `publication-PASS` only if the push succeeded, public
  `refs/heads/main` equals the candidate, the expected tree/parent/subject are
  read back, and the `verify` run reached `success`.
- `PARTIAL` with `publication-PASS` if the public ref matches but the CI run
  failed, was cancelled/timed out, or could not be observed within the bound.
  State the exact run URL, head SHA, status and conclusion or `not observed`.
- `BLOCKED` with `Phase-qualified result: not-applicable` if the pre-push gate
  failed, the push was rejected/non-fast-forward, or public readback did not
  match. Do not force or retry.

Include the prompt SHA-256 after reading `03_publication_00.md`, and the
report's own SHA-256 in the separate completion notice. Do not write the
report to the repository or Meta. Do not push a second time.

## Stopping conditions

Stop and report without improvisation if:

- the local candidate, parent, tree, subject, branch, clean worktree, `.ap`
  pin or `ap doctor` state differs from the declared state;
- public `refs/heads/main` is not the expected parent;
- the changed-path set is not exactly the seven accepted paths;
- the push is rejected, non-fast-forward, or fails;
- public readback does not equal the candidate;
- the CI run fails, is cancelled/timed out, or cannot be observed within the
  bound;
- a check would require a source edit, correction, second commit, force,
  settings change, secret, deployment, release, Meta write or closure;
- the session is not the fresh publication session selected by the
  COOPERATOR.

Preserve the first causal error and exact evidence. Return the report in the
session even for `PARTIAL` or `BLOCKED`, unless delivery is impossible; then
preserve the complete available content and disclose the missing delivery.
This terminal report ends the publication grant. No autonomous continuation.
