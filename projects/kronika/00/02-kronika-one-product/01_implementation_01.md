# Kronika one product — S0 record one-product architecture

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S0
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — bounded documentation and one ADR against an exact allowlist, reversible, no code, no host, no named risk; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS report `01_report_00.md` for task
`KRONIKA-ONE-PRODUCT-PLAN`, Worker session 01, exchange 01.
Authority renewal: that planning authority expired at its terminal report. This
exchange grants complete new bounded implementation authority for S0 only.
Reuse rationale: the same healthy session produced the repository-grounded plan;
retained understanding of the allowlist and the locked direction reduces error.
No independence is required for documentation alignment.
Repository and environment re-gating: required before mutation; re-establish
every gate below from current evidence, never from memory.
Retained context: convenience only, never authority. On any conflict between
retained context and current repository evidence, stop and report.
Evidence posture: non-independent.
New terminal report: required (`01_report_01.md`).

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/chatgpt-page-ask-kernel`, HEAD
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`, parent
  `0fd21b989814b7c0b78d517996812750a823ff10`, tree
  `f554863f18238e04203e4f22d5e20770e180045d`, subject
  `feat: add chatgpt-page probe tooling and budget contract`; clean index and
  worktree; local `main` = `origin/main` = `26d28b16c08a5e7e0179a32c16646bfdc1009c81`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Kronika source checkout `/home/agile/Tools/cli_chatgpt` at
  `66c40d43c577276b0ad304a494fbbb1ffb6fc933`, clean; read-only source.
- All S0 target files exist except the new ADR
  `docs/adr/0082-kronika-one-product-and-private-records.md`, which does not
  exist yet; the latest existing ADR is `0081`.
- Latest catalog revision is `0033_media_analysis_proposals.py`.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `26d28b16c08a5e7e0179a32c16646bfdc1009c81`
Changed-path allowlist:

```text
AGENTS.md
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SERVER.md
SECURITY.md
DEVELOPMENT.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/adr/README.md
docs/adr/0082-kronika-one-product-and-private-records.md
```

Implementation boundaries: the positive and negative authority below.
Independence required: no

## Goal

Record the accepted one-product Kronika architecture in current FrameNest
documentation and one new ADR, clearly distinguishing the accepted future
architecture from implemented behavior, so later slices can execute without
re-deciding product direction. Documentation only: no code, packaging, test,
host, database, or behavior change.

## Governing decisions (accepted; do not reopen)

- One product: the existing FrameNest repository becomes Kronika; the closed
  `cli_chatgpt`/Kronika code supplies the ChatGPT capture module; no new
  repository.
- Application and capture are separate processes; the web application and the
  capture module communicate over the loopback bridge.
- Timeline is the main page; the existing design and Gallery are preserved.
- New record kinds Search and Research; media enters the timeline only after a
  successful validated analysis.
- Every new record starts private; family sharing is explicit; family sharing
  is never mapped onto public publication, which stays off.
- Old databases of both projects hold unwanted test data; no import is
  implemented; the accepted transition is an authorized empty-database reset.
- Owner comes from verified identity; the administrator role is not a private
  content read override.
- Capture: one persistent browser, admin intervention via `needs_admin`, no
  automatic resend, one bounded ZIP attachment, per-install token, loopback
  only.
- Slice order S0–S10; one Worker grant executes one row; S0 is documentation
  and ADR only.

## Branch topology

Create `feat/kronika-one-product` from the verified baseline and work there:

```text
git switch -c feat/kronika-one-product
```

The existing `feat/chatgpt-page-ask-kernel` branch and its history stay intact.
One local commit on the new branch. No push, no force, no remote change, no
rebase, no amend, no tag, no config write.

## Exact content changes

- `docs/adr/0082-kronika-one-product-and-private-records.md` (new): record one
  repository/product, application/capture ownership, the process boundary,
  selective transfer, the common catalog, private defaults, explicit sharing
  and the empty-database transition.
- `PRODUCT.md`, `SPEC.md`: record Timeline, Search/Research, entry rules and
  scope exclusions.
- `SERVER.md`, `SECURITY.md`: record trusted identity, administrator limits,
  public exclusion, capture token/browser boundaries and safe rendering.
- `ROADMAP.md`: record S0–S10 and their gates.
- `README.md`: explain the accepted transition without claiming that new
  features are implemented.
- `DEVELOPMENT.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`: describe the intended
  single release route and the later host gates.
- `AGENTS.md`: change only project-specific product/security guidance outside
  the managed AP block; the managed block stays byte-identical.
- `docs/adr/README.md`: register ADR-0082 consistently with the existing index.
- Preserve old ADRs and host baseline facts as history; link the superseding
  decision rather than rewriting past observations.
- Do not claim unverified host behavior anywhere. Host facts stay
  historical/preflight claims.

## Positive authority

Create the branch above; edit exactly the allowlisted files; stage exactly those
paths; create one commit. Read-only checks are allowed.

Commands: the repository integration gate
`./.ap/ap project check --root /home/agile/Projects/framenest --baseline 26d28b16c08a5e7e0179a32c16646bfdc1009c81`
(before and after the commit; non-mutating); read-only Git identity, status,
diff, log, show and ref queries; `rg`/`rg --files` with private-value-safe
output; the native file writer for allowlisted files only; explicit
`git add <exact paths>`; one `git commit`.

The declared FrameNest Python route (`./.ap/ap exec`) and the JavaScript
`node --test` route are binding for later slices but are not used in S0: no
test execution is authorized or required for documentation-only work.

## Negative authority

- No test execution (no pytest, no `node --test`, no `./.ap/ap exec` test
  operations); no `poetry`, `uv`, `pip`, setup or environment change; no
  dependency or lockfile change.
- No product code, packaging, assets, contracts, migrations, deploy/systemd
  files, AP files, `.ap` content, managed AP block, or upgrade-ledger changes.
- No host, SSH, NUC, browser, database, network, provider, credential, or
  secret access. Do not read `private/**`.
- No push, publication, GitHub rename, remote change, force, amend, rebase,
  reset, clean, stash, `git add -A`, `git add .`, `--no-verify`,
  `--no-gpg-sign`, or config write.
- No new files beyond the allowlist; no adjacent refactoring; no branding
  sweep; no mass `framenest` rename.
- Do not reopen a locked decision. If the allowlist cannot express a required
  change, stop and report.

## Validation

1. Final `git diff --name-status <baseline>..HEAD` equals the allowlist exactly
   (modified files plus the one added ADR).
2. `git status --porcelain` is clean after the commit; branch, HEAD and commit
   SHA are read back.
3. AP pin unchanged in gitlink and `.ap` HEAD; the managed AP block is
   byte-identical; `.gitmodules` and `docs/AP_UPGRADE_OBSERVATIONS.md`
   unchanged.
4. Contradiction checklist, reported by file with the resolution (updated or
   preserved as history): live two-product claims; Gallery-versus-landing
   wording; old database/import claims; administrator private-content access
   claims; public publication claims; any claim that new features already
   exist.
5. Referenced relative links/paths in changed documents resolve; ADR index
   registration is consistent.
6. `./.ap/ap project check` passes on the final baseline.

S0 evidence for the next slice: the accepted documentation commit, the
contradiction checklist, and the unchanged pin.

## Stopping conditions

Stop and report on: baseline, cleanliness, branch, AP-pin, or managed-block
mismatch; an unexpected pre-existing change in an allowlisted file; a needed
change outside the allowlist; a need to reopen a locked decision; a needed
claim about unverified host behavior; a required test or route operation this
grant does not authorize; missing capability; or any instruction conflict.
Preserve the first causal failure; do not improvise a workaround.

## Completion and report contract

`PASS` means S0 documentation and ADR changes are complete within the
allowlist, the single commit exists on `feat/kronika-one-product`, and all
validation above passed. Use `PARTIAL` or `BLOCKED` honestly otherwise. No push
occurred.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core: status;
`Phase-qualified result: implementation-PASS` (or `not-applicable` on failure);
start and end commit; changed files and purpose; validation results; commit
result with `no push`; deviations/risks/missing evidence; one smallest next
step; `Report justification: new-mutation`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report, cancellation or supersession expires this authority. Do not continue
autonomously after the report.

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
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
