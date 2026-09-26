### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 21
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-C3-RUNNER-TEMPDIR
status: PASS
Phase-qualified result: implementation-PASS
Start commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
End commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
Report justification: new-mutation
Logical-whole closure: not-closed

The capture runner unit now sets `TMPDIR` to `/run/kronika-capture/tmp` and creates that directory at mode 0700 before start. The new contract test failed on the baseline unit and passes on the committed tree. No host contact, push, or independent acceptance was performed. No subagents were used.

Changed files:

- `deploy/systemd/kronika-capture-runner.service` — writable temporary directory inside the existing runtime path
- `tests/contract/test_kronika_capture_services.py` — regression that the baseline unit fails
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the same correction, with Xvfb's `/tmp` write kept distinct from the runner

## Step 0

Physical root `/home/agile/Projects/framenest` (not a symlink), branch `feat/kronika-one-product`:

- HEAD `e408bb5503f359ec24542304ac1a621c6b9e4ffb`
- parent `d63d0b725acedf49d1611224c3b5201a90e7ef90`
- tree `dadc01726a354c319374832bfd385be0bdffb516`
- subject `fix(capture): diagnose startup and require fresh activation readiness`
- index clean; worktree clean; no index or HEAD lock
- local `main` = `origin/main` = `e408bb5503f359ec24542304ac1a621c6b9e4ffb`
- public `refs/heads/main` via `git ls-remote origin` = `e408bb5503f359ec24542304ac1a621c6b9e4ffb`
- AP gitlink and `.ap` HEAD = `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`

No divergence from the issued gate, so no RF-12 recovery class was applied. Report destination `21_report_00.md` was absent.

## Unit lines

```ini
Environment=TMPDIR=/run/kronika-capture/tmp
ExecStartPre=/usr/bin/install -d -m 0700 /var/lib/kronika-capture/profile /var/lib/kronika-capture/staging /run/kronika-capture/tmp
```

`ReadWritePaths` remains `/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix`. `PrivateTmp` was not added. No other unit directive changed.

## Test assertions

`test_runner_temporary_directory_stays_inside_the_runtime_boundary` asserts, as exact lines:

- `Environment=TMPDIR=/run/kronika-capture/tmp`
- `ExecStartPre=/usr/bin/install -d -m 0700 /var/lib/kronika-capture/profile /var/lib/kronika-capture/staging /run/kronika-capture/tmp`
- `ReadWritePaths=/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix`, and that the path list does not contain a bare `/tmp`
- `PrivateTmp=true` absent from the runner and Xvfb units
- `ProtectSystem=strict` and `NoNewPrivileges=true` still present on the runner
- no active `TMPDIR` assignment in `deploy/systemd/kronika-capture.env.example`

Existing tests in that file were left in place.

## Routes

`./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb` exited 0: `ap project check --baseline: PASS`.

`./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py -q -p no:cacheprovider`

- Before the unit change, with only the new test present: exit 1; `1 failed, 130 passed`. The only failure was `test_runner_temporary_directory_stays_inside_the_runtime_boundary`, on the missing `Environment=TMPDIR=/run/kronika-capture/tmp` line.
- After the unit, test, and final documentation wording, on the tree that was then committed: exit 0; `131 passed`.

Each route also printed `WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH` and `OK environment policy: sanitized-v1`.

## Git

Commit `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`
Parent `e408bb5503f359ec24542304ac1a621c6b9e4ffb`
Tree `3b9014956a3bc738a209af51034fcac58ef5c498`
Subject `fix(capture): point the capture runner temporary directory at its runtime dir`

`git diff --name-status` against the baseline is exactly the three allowlisted paths. `git diff --check` was empty. Post-commit `git status --porcelain` is empty on `feat/kronika-one-product`. No push, fetch, tag, or other ref update. Meta artifacts were not committed.

Deviations: none.
Risks and missing evidence: these tests do not start Chromium or the host unit. The installed `/etc/kronika-capture/capture.env` was not read. `EnvironmentFile=` follows the new `Environment=` line, so an installed assignment of `TMPDIR` would replace the unit value. Independent acceptance is not claimed.
Smallest next step: full-fresh independent acceptance of `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, including the separately authorized corrected start.
Orchestration critique:
MEASURED: none
LEAD: the installed `/etc/kronika-capture/capture.env` may assign `TMPDIR` and override the unit; cheapest useful check is a read-only test for an active `TMPDIR` assignment in that file during the authorized acceptance, without printing other values
Resolved Execution Issues / Near-Misses: the first documentation draft stated that `capture.env` does not set `TMPDIR` as if the installed file had been inspected; corrected before commit so the sentence covers the committed template and a host copy that matches it; residual risk is the unread installed file
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
