# KRONIKA-ONE-PRODUCT-WORKER-GATE-F01-CORRECTION — bounded correction of re-audit finding F01

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 44
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-WORKER-GATE-F01-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — small security-adjacent operator-gate correction with a causal regression; the Cooperator may override.
Recommended context capacity: approximately 150k tokens
Independence required: no — a separate fresh scoped re-audit follows after the corrected commit.

## Context and finding

The focused independent re-audit `43_report_00.md` (status PASS,
acceptance-PASS) established all six claims for worker-gate candidate
`665a565bc1279690ce8dacade37103fa3e0aaddc` and verified-closed the exchange-41
`ssh-agent: absent` failure. It left one open low-severity finding:

```text
Finding ID: KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT-REAUDIT-F01
Title: Final-symlink ownership check lags test -S
Status: open
Severity: low
Decision: correction-required (approver: Orchestrator)
Affected component: scripts/operator/network/framenest_nuc_worker_gate.fish:_attach_darwin_ambient_from_system
Detail: the Darwin ownership comparison uses stat -f %u, which does not follow a final symlink, while test -S does follow it. A presented SSH_AUTH_SOCK whose final component is a symlink can satisfy the socket check on a different inode than the ownership check.
Smallest safe correction direction: compare ownership with stat -L so the uid is the socket inode's.
Regression-test requirement: a case whose presented path is a symlink to a socket and whose ownership result follows the target.
```

The live socket's final component is not a symlink, so the accepted claims
hold; this exchange is the pre-publication cleanup of that gap.

## Required outcome

R1. The Darwin ownership comparison follows the final symlink and compares the
   uid of the socket inode the path actually denotes (for example
   `stat -L -f %u`, or an equivalent that resolves the final component before
   the ownership comparison). The compared value must be the target socket's
   owner, not the link's.
R2. Every other check and behavior is unchanged: gpgconf-first order, the
   Darwin-only activation, nonempty/absolute/no-`..`, `test -S`, the launchd
   prefix check on `realpath`, the `ssh-add -l` liveness rule, no mode check,
   the `--probe` output contract (`ssh-agent: ready` exit 0 or
   `ssh-agent: absent` exit 1), no socket or key-list printing, no weakening of
   the SSH options, loader unsets, sanitized PATH, no parallel stack. Linux and
   gpgconf-present paths stay byte-compatible.
R3. Regression: add a case that fails on the parent `665a565…` and passes after
   the fix, demonstrating that the ownership check follows the final symlink to
   the socket inode. Choose the mechanism inside the existing
   `FRAMENEST_NETWORK_TEST_*` hooks convention; a behavior-or-shape assertion is
   acceptable if a purely dynamic same-user case cannot distinguish link and
   target ownership. Keep the existing Darwin positive/negative cases green.

## Exact path allowlist

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
tests/contract/test_operator_network_scripts.py
```

No other path may change. A required edit outside this list is a stop. Do not
change the docs in this exchange (their description stays truthful).

## Starting state (verified read-only at issuance, 2026-09-28)

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     665a565bc1279690ce8dacade37103fa3e0aaddc
parent   0d0d8c88bf88bf8454751a0205bc8652374796c2
tree     043b811cf82b54cff05026a90b3b15ee46609475
subject  fix(operator): discover the macOS launchd ssh agent in the worker gate
status   empty (git status --porcelain --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
public   main 0d0d8c8…; feature branch 38e7bee…
```

Baseline for every declared AP command:
`665a565bc1279690ce8dacade37103fa3e0aaddc`.

Report destination: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/44_report_00.md` (absent at issuance).

## Validation (targeted only; testing economy directive is binding)

1. `./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 665a565bc1279690ce8dacade37103fa3e0aaddc` — exit 0 before editing and before the commit.
2. Red first: with the new regression written, run the declared route and
   record it failing on the unfixed gate.
3. Implement the correction.
4. Green: same single `test-focus` invocation exits 0 with the full file green
   (`60+` passed). Do not run the broad suite; do not re-run an unchanged gate.

```text
./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 665a565bc1279690ce8dacade37103fa3e0aaddc --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider
```

## Git

If and only if all gates hold: stage exactly the two allowlisted paths (never
`git add .` or `git add -A`), inspect `git diff --cached --check` and `--stat`,
and create exactly one local commit:

```text
fix(operator): follow symlinks in the gate agent ownership check
```

Report SHA, parent (`665a565bc1279690ce8dacade37103fa3e0aaddc`), tree, subject,
changed-path list, and post-commit `git status --porcelain=v1
--untracked-files=all` (must be empty). No push, fetch, tag, merge, rebase,
reset, restore, checkout, switch, stash, clean or config write.

## Stop conditions

Stop with preserved first-causal evidence on: an edit needed outside the
allowlist; any change beyond the ownership comparison; any weakening of the
gate's trust rules, sanitization or SSH options; a regression that cannot be
made to fail first or to pass after; any printing of the socket path, key list
or other private value; an unexplained failing gate; the client mode blocking
required writes; or any instruction conflict.

## Evidence envelope

```text
Evidence tier: E2
Evidence tier basis: repository-local operator-tooling correction with a causal regression; no host contact
Authorized implementation stages: regression-first (Red), correction implementation, targeted contract tests, diff review, one local commit
Independent acceptance: required-separate-fresh-worker after this exchange (scoped re-audit of the corrected exact SHA; not this session)
Rollback checkpoint: parent 665a565… remains intact
Terminal implementation report point: the single local commit above
```

## Completion and report contract

`PASS` means: the new regression failed on the unfixed gate and passes after
the fix; the targeted file exits 0 fully green; only the two allowlisted paths
changed; one local commit exists with a clean post-commit worktree and no push.
Use `Phase-qualified result: implementation-PASS` only for that result;
otherwise `not-applicable` and a truthful `PARTIAL`/`BLOCKED`.
`Logical-whole closure: not-closed`. `Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 44, exchange 01) exactly once. Include: the
re-gate values; the Red/Green evidence with exact counts; the exact ownership
check change; the regression mechanism and why it distinguishes the parent; the
changed-path list; the commit SHA/parent/tree/subject and post-commit status;
the confirmation that no other behavior changed; one smallest next step (the
separate fresh scoped re-audit of the corrected exact SHA, then publication,
then the renewed NUC deployment grant); the compact critique block; and the
authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. If the report write is blocked by the client,
preserve the complete content in the client output and report the missing
delivery truthfully. Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 44_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 44_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
