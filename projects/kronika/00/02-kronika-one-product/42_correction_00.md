# KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT — bounded correction of the NUC worker-gate agent discovery on macOS

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 42
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — security-sensitive operator-gate change with a strict Darwin trust rule and causal contract tests; the Cooperator may override.
Recommended context capacity: approximately 200k tokens
Independence required: no — a separate fresh focused re-audit follows after the corrected commit.

## Context and confirmed defect

Development moved from the office PC (Linux) to a MacBook (macOS). The NUC
routine release update (exchange 41/01, report `41_report_00.md`, status
BLOCKED) stopped at Step 0 before any SSH or deploy: the three
`FRAMENEST_NUC_SSH_*` names were set, but
`scripts/operator/network/framenest_nuc_worker_gate.fish --probe` printed
`ssh-agent: absent` and exited 1.

Orchestrator read-only root cause: `_attach_agent` discovers the agent socket
only through `gpgconf` resolved on the gate's trusted path
`/usr/sbin:/usr/bin:/sbin:/bin`. The MacBook has **no `gpgconf`** anywhere (no
GnuPG installation; a stale `~/.gnupg/S.gpg-agent.ssh` socket exists with no
`gpg-agent` process). The working route is the **native macOS launchd
`ssh-agent`** (`/usr/bin/ssh-agent -l`, one loaded key, exposed through the
ambient `SSH_AUTH_SOCK`); the Cooperator's direct `ssh framenest-nuc true`
succeeds through it. The gate deliberately rebuilds the socket instead of
trusting the ambient value, so it fails closed on macOS even though a usable
agent exists.

## Required outcome

The gate must accept, on macOS only, a strictly validated ambient agent socket
as a fallback when `gpgconf` discovery is unavailable, without weakening any
existing validation or Linux behavior. The `--probe` contract stays
byte-compatible: `ssh-agent: ready` exit 0, or `ssh-agent: absent` exit 1; the
socket path and any agent identities are never printed.

Binding requirements:

R1. Discovery order: try the existing trusted `gpgconf` path first, unchanged.
   Only when `gpgconf` is unavailable (not found in the trusted path), and only
   when the platform is Darwin (`uname -s` resolved through the trusted path is
   exactly `Darwin`), attempt the validated ambient fallback.
R2. Darwin fallback validation (all must hold; any failure returns `absent`):
   `SSH_AUTH_SOCK` is non-empty, absolute, contains no `..` segment, is a Unix
   socket (`test -S`), is owned by the invoking effective user, and its
   resolved physical path lies under `/private/var/run/com.apple.launchd.`
   (accept the `/var/run/...` symlink form by resolving `realpath`).
   Liveness: run `ssh-add -l` with stdout and stderr discarded and treat exit
   status 0 (identities present) or 1 (no identities) as a working agent; any
   other status rejects the socket. Do not require a restrictive socket mode:
   the native launchd socket is observed as `srw-rw-rw-` owned by the user.
R3. On success the gate sets `SSH_AUTH_SOCK` to the validated socket for its
   own process and for the SSH child, exactly as the existing gpgconf path
   does. On Linux the fallback never activates: a missing `gpgconf` still
   yields `ssh-agent: absent`, byte-compatible with today.
R4. No weakening: every other gate validation (target/user/identity/command
   checks, `BatchMode`, `StrictHostKeyChecking=yes`, `IdentitiesOnly=yes`,
   `ClearAllForwardings=yes`, sanitized PATH, loader unsets, no shell
   metacharacters) stays unchanged. No new parallel SSH or agent stack. No
   output of the socket value or key list.
R5. Test hooks: any new hook lives in the existing `FRAMENEST_NETWORK_TEST_*`
   namespace, is active only when `FRAMENEST_NETWORK_TEST_HOOKS=1`, and lets
   the tests simulate the platform, the ambient socket path, and the
   socket/owner/prefix/liveness outcomes deterministically. With hooks enabled
   and no Darwin-fallback hook values, the fallback must be inert so the
   existing `absent` tests stay green on macOS; production code must never
   consult the hook values.
R6. Contract tests in `tests/contract/test_operator_network_scripts.py`:
   - Causal regression first: a new test simulates Darwin + no `gpgconf` + a
     valid validated socket and expects `ssh-agent: ready`; it must fail on the
     unfixed gate and pass after the fix.
   - Negative cases: non-absolute or `..` path, non-socket file, foreign owner,
     path outside `/private/var/run/com.apple.launchd.`, dead agent
     (`ssh-add -l` exit >= 2), empty value — each returns `ssh-agent: absent`
     exit 1.
   - Linux/gpgconf-present behavior unchanged; gpgconf failure on Linux still
     `absent`; the probe never prints the socket path.
   - Ambient-default hardening (bounded secondary objective, the parked debt
     anticipated in `docs/AP_UPGRADE_OBSERVATIONS.md`): make
     `test_ssh_gate_rejects_missing_required_values` (and any equivalent
     parameterized case) isolate the ambient `FRAMENEST_NUC_SSH_*` values by
     clearing them for the invoked gate process, so the missing-value refusal
     is genuinely exercised even when the operator environment exports the
     names. No production behavior change; this is test isolation only.
R7. Documentation: a short, accurate note in `docs/OPERATOR_NETWORK.md` (and,
   only if needed for truthfulness, a one-line clarification in
   `docs/WORKER_EXECUTION_CONTRACT.md` and
   `scripts/operator/network/README.md`) describing the discovery order and
   the Darwin validation. No new semantics.

## Exact path allowlist

Edit only these paths, and only as far as needed:

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
scripts/operator/network/README.md
tests/contract/test_operator_network_scripts.py
docs/OPERATOR_NETWORK.md
docs/WORKER_EXECUTION_CONTRACT.md
```

The gate and the test file are expected to carry the change. Any needed edit
outside this list is a stop with the exact path and reason.

## Starting state (verified read-only at issuance, 2026-09-28)

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     0d0d8c88bf88bf8454751a0205bc8652374796c2
parent   5843486ddeae13ec5b331f102c5cb595bfa6e386
tree     96adead05beb58f2e282ff77b9e6d29bff2c8298
subject  fix(kronika): serve approved projections on household reads
status   empty (git status --porcelain --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
main     local branch 40e51cb2d061ead96850c9c94aa59de54d5e1310; public main 0d0d8c8…; public feature branch 38e7bee…
```

Baseline for every declared AP command in this exchange:
`0d0d8c88bf88bf8454751a0205bc8652374796c2`.

Report destination: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/42_report_00.md` (absent at issuance).

Environment facts for the implementation (observed read-only by the
Orchestrator; verify before relying on them): no `gpgconf` exists on this host;
`pgrep -x gpg-agent` finds no process; the ambient `SSH_AUTH_SOCK` is a Unix
socket under `/var/run/com.apple.launchd.<id>/Listeners`, owner uid 501, mode
`srw-rw-rw-`; `/usr/bin/ssh-agent -l` is running and holds one identity. Never
print the socket value or identity details in evidence; describe them as above.

## Validation (targeted only; testing economy directive is binding)

1. `./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2` — exit 0 before editing and before the commit.
2. Red first: with the new/updated tests written, run
   `tests/contract/test_operator_network_scripts.py` through the declared
   route and record the new causal test failing on the unfixed gate.
3. Implement the correction inside the allowlist.
4. Green: same single `test-focus` invocation of
   `tests/contract/test_operator_network_scripts.py` exits 0, including the
   hardened ambient-default isolation.
5. Do not run the broad suite. Do not re-run an unchanged gate. Do not touch
   the `framenest_mullvad_egress` scripts or their tests.

Declared route:

```text
./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2 --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider
```

## Git

If and only if all gates hold: stage exactly the changed allowlisted paths
(never `git add .` or `git add -A`), inspect `git diff --cached --check` and
`--stat`, and create exactly one local commit:

```text
fix(operator): discover the macOS launchd ssh agent in the worker gate
```

Report SHA, parent (`0d0d8c88bf88bf8454751a0205bc8652374796c2`), tree, subject,
changed-path list, and post-commit `git status --porcelain=v1
--untracked-files=all` (must be empty). No push, fetch, tag, merge, rebase,
reset, restore, checkout, switch, stash, clean or config write.

## Stop conditions

Stop with preserved first-causal evidence on: an edit needed outside the
allowlist; any weakening of the gate's trust rules, sanitization, or SSH
options; a fallback that activates on Linux or with `gpgconf` available; any
printing of the socket path, key list or other private value; a test-isolation
change that alters production behavior; an unexplained failing gate; the client
mode blocking required writes; or any instruction conflict.

## Evidence envelope

```text
Evidence tier: E2
Evidence tier basis: repository-local operator-tooling correction with causal contract tests; no host contact
Authorized implementation stages: regression-first (Red), correction implementation, targeted contract tests, diff review, one local commit
Independent acceptance: required-separate-fresh-worker after this exchange (focused re-audit of the corrected exact SHA; not this session)
Rollback checkpoint: parent 0d0d8c8… remains intact
Terminal implementation report point: the single local commit above
```

## Completion and report contract

`PASS` means: the new causal Darwin-fallback test failed on the unfixed gate
and passes after the fix; the targeted gate test file exits 0 including the
ambient-default isolation; only allowlisted paths changed; one local commit
exists with a clean post-commit worktree and no push. Use
`Phase-qualified result: implementation-PASS` only for that result; otherwise
`not-applicable` and a truthful `PARTIAL`/`BLOCKED`. `Logical-whole closure:
not-closed`. `Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 42, exchange 01) exactly once. Include: the
re-gate values; the Red/Green evidence with exact counts; the discovery-order
and validation summary actually implemented; the test list and results; the
changed-path list; the commit SHA/parent/tree/subject and post-commit status;
the parked-failure classification for the MacBook ambient names (explain that
the hardening removes the ambient-default interference for this file); one
smallest next step (the separate fresh focused re-audit of the corrected exact
SHA, then publication, then the renewed NUC deployment grant); the compact
critique block; and the authority-expiry statement.

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
Downloadable prompt filename: 42_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 42_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
