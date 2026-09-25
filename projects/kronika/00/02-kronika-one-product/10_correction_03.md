# Kronika one product — S3 Xvfb lock correction (documented fallback)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S3-XVFB-LOCK-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: correct the Xvfb lock strategy with the pre-authorized fallback after real host evidence, and stop the currently active capture services; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal BLOCKED report `10_report_02.md` for task
`KRONIKA-ONE-PRODUCT-S3-HOST-RETRY`, Worker session 10, exchange 03, ending at
accepted commit `94e605c17b881461fad3e22fd8c7fca32cb93976`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded correction authority for the Xvfb
lock strategy and the host cleanup below, for this session only.
Reuse rationale: this session holds the exact host evidence and installed
state. Repository and environment re-gating is required before mutation.
Retained context is convenience only. Evidence posture: non-independent. New
terminal report: required (`10_report_03.md`).

## New material evidence justifying this second correction

The host run (`10_report_02.md`) proved that the first-correction assumption
was wrong: Xvfb logs `Warning: the -nolock option can only be used by root`,
ignores the option for the unprivileged service user, still needs
`/tmp/.tX99-lock`, and exits 1; readiness stayed `browser_unavailable`. The
first correction grant already named the fallback for exactly this case: if
`-nolock` is not usable, add `/tmp` to the unit's `ReadWritePaths` and record
the broader grant. That fallback is now selected.

Host residue to clean: bridge and runner are active (runner reports
`browser_unavailable`), Xvfb is failed, the three units are enabled. Account,
directories, token files, both release pointers at `94e605c` and the installed
corrected units remain.

## Step 0 — preconditions

- The three `FRAMENEST_NUC_SSH_*` names are present (names only); otherwise
  stop `BLOCKED`.
- Gate `--probe` prints `ssh-agent: ready`; remote `sudo -n true` exits 0. Use
  `sudo -n` only, never `sudo -v`.

## Correction A — host cleanup first

Through the gate, in order:

```text
sudo -n systemctl stop kronika-capture-bridge.service
sudo -n systemctl stop kronika-capture-runner.service
sudo -n systemctl stop kronika-capture-xvfb.service
sudo -n systemctl disable kronika-capture-xvfb.service kronika-capture-bridge.service kronika-capture-runner.service
sudo -n systemctl reset-failed kronika-capture-bridge.service kronika-capture-runner.service kronika-capture-xvfb.service
```

Verify read-only: the three are `inactive` or `failed` with `NRestarts=0`, no
chrome/Xvfb processes, no listeners on 8765/5900/6080. Do not remove the
account, paths, tokens, units or release pointers.

## Correction B — Xvfb lock strategy (documented fallback)

Replace the ineffective `-nolock` with the writable-lock path:

```text
ExecStart=/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -auth /run/kronika-capture/Xauthority

ProtectSystem=strict
ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture
```

Keep `-auth`, `-nolisten tcp`, `RuntimeDirectory=kronika-capture`,
`RuntimeDirectoryMode=0700`, `UMask=0077`, `Restart=no` and the rest of the
unit unchanged. `/tmp` is the minimal shared path that lets the unprivileged
Xvfb create its display lock; the socket directory and runtime directory
remain explicit. Do not use `PrivateTmp` on Xvfb, the runner or VNC.

Update `tests/contract/test_kronika_capture_services.py`:

- Remove the `-nolock` assertion.
- Assert the Xvfb `ExecStart` keeps `-nolisten tcp` and `-auth`, does not
  contain `-nolock` and does not contain `-ac`.
- Assert `ReadWritePaths` includes `/tmp`, `/tmp/.X11-unix` and
  `/run/kronika-capture`, and that Xvfb and the runner still do not set
  `PrivateTmp`.
- Keep every other directive assertion, including the CLI-parse regression.

Update `docs/UBUNTU_NUC_DEPLOYMENT.md` with one sentence stating that Xvfb
writes its display lock under `/tmp`, so the unit keeps `/tmp` writable while
the rest of the filesystem stays read-only. Do not change the sentence about
access control: the unit still uses `-auth` and not `-ac`.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `94e605c17b881461fad3e22fd8c7fca32cb93976`
Changed-path allowlist:

```text
deploy/systemd/kronika-capture-xvfb.service
tests/contract/test_kronika_capture_services.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Implementation boundaries: the lock-strategy correction, the test update and
the one documentation sentence; nothing else.
Independence required: no

## Positive authority

The gate cleanup commands; the allowlisted repository edits; the declared
route; one local commit; the report write.

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

No ambient Python, `poetry run` or substitute route.

## Negative authority

- Host: only the stop/disable/reset-failed commands above; no install, start,
  enable, deploy, activate, login, view, resume or ask; no token read; no
  account/path/token/release removal.
- Repository: no other unit, helper, capture source, packaging, AP or doc
  change; no push or publication (separate grant follows).
- No `sudo -v`, no `private/**`, no subagents, no Meta commit.

## Validation

1. Host after cleanup: three units inactive/failed with `NRestarts=0`, no
   chrome/Xvfb processes, no listeners; account and pointers untouched.
2. The corrected Xvfb unit contains no `-nolock`, keeps `-nolisten tcp` and
   `-auth`, and `ReadWritePaths` includes `/tmp`; no `PrivateTmp` on Xvfb or
   the runner.
3. The updated contract test passes; the CLI-parse regression still passes and
   still rejects the old option order.
4. The declared route passes; `git diff --name-status <baseline>..HEAD` equals
   the allowlist; clean worktree; one commit above the baseline; branch, HEAD,
   parent and tree read back.
5. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `src/framenest/**` and `AGENTS.md`
   unchanged; local `main` and public `main` still at the baseline until the
   publication grant.
6. Terminal remote `sudo -K`; confirm with a failing `sudo -n true`.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; an
unexpected host result; a needed change outside the allowlist; a route failure
that cannot be corrected inside the allowlist; or any conflict with the host
evidence. Preserve the first causal failure; do not improvise.

## Completion and report contract

`PASS` means the host cleanup is verified, the lock strategy is corrected and
tested, the documentation sentence is added, the declared route passed and one
commit exists. `PARTIAL`/`BLOCKED` otherwise. No push. A fresh acceptance,
publication and host retry follow.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include: the compact core; the host
cleanup result; the exact corrected unit fragment; the test changes and route
results; changed files; commit result with `no push`; deviations/risks/missing
evidence; one smallest next step (fresh acceptance); `Report justification:
new-mutation`; authority expiry; and:

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
report or cancellation expires this authority.

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
Downloadable prompt filename: 10_correction_03.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 10_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
