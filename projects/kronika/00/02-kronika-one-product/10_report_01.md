### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST-CORRECTION
status: PASS
Phase-qualified result: correction committed, non-independent
Start commit: c975aba14840b97944aecc655907e3abc370341d
End commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
Report justification: new-mutation
Logical-whole closure: not-closed

Continuity anchor matched exchange 01: terminal BLOCKED report `10_report_00.md`, repository HEAD `c975aba14840b97944aecc655907e3abc370341d` before this commit. That exchange's authority had expired. This correction does not self-certify.

## Step 0

Names only: TARGET-set, USER-set, IDENTITY-set.
Probe printed `ssh-agent: ready` and exited 0. Remote `sudo -n true` exited 0.
Branch `feat/kronika-one-product` was clean. Local `main`, `origin/main`, and public `refs/heads/main` were the baseline. AP pin was `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.

## Host cleanup

Through the gate, in order, each exit 0:

- `systemctl stop` bridge, runner, then xvfb.
- `systemctl disable` of the three units removed the three `multi-user.target.wants` symlinks.
- `systemctl reset-failed` of the three units.

Read-only result for each of the three: `is-active` `inactive` (exit 3), `NRestarts=0`, `ActiveState=inactive`, `SubState=dead`, `UnitFileState=disabled`. `pgrep -c -x chrome` and `pgrep -c -x Xvfb` were 0. Ports 8765, 5900, and 6080 had no listeners. Account, paths, token files, installed unit files, and the release pointer were not removed.

`/usr/bin/Xvfb -help` exited 0. The help text contains `-nolock` with the description `disable the locking mechanism`. Nothing was started. Chosen strategy: `-nolock`, keeping `-nolisten tcp` and `-auth`. The `/tmp` `ReadWritePaths` fallback was not used. Xvfb and the runner do not set `PrivateTmp=true`.

`sudo -K` exited 0. A following `sudo -n true` exited 1 with a password-required result.

## Corrected unit lines

```text
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge run --port 8765
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed
ExecStart=/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -nolock -auth /run/kronika-capture/Xauthority
```

`tests/unit/chatgpt_page/test_systemd_credentials.py` already parses `--state-dir` before `runner` and does not encode the unit command line. It was not edited. `docs/UBUNTU_NUC_DEPLOYMENT.md` and `deploy/ubuntu/README.md` do not state these command lines or the lock-file behavior. They were not edited.

## Regression and route

`test_cli_execstart_parses_and_rejects_the_old_option_order` extracts each bridge and runner `ExecStart`, strips the executable, and parses the remainder with `kronika_capture.cli.build_parser()`. The corrected argument lists parse. The previous order, with `--state-dir` after `bridge run` and `runner run`, raises `SystemExit` code 2. `test_xvfb_lock_strategy_uses_nolock` asserts the exact Xvfb `ExecStart` above and that `ReadWritePaths` stays `/tmp/.X11-unix /run/kronika-capture`. Existing directive assertions, including `PrivateTmp=true` absent from Xvfb and the runner, remain.

`./.ap/ap project check --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d` exited 0 (`ap project check --baseline: PASS`).
The declared `test-focus` route exited 0: `157 passed in 4.37s`.

## Git

Changed files, all inside the allowlist:

```text
M	deploy/systemd/kronika-capture-bridge.service
M	deploy/systemd/kronika-capture-runner.service
M	deploy/systemd/kronika-capture-xvfb.service
M	tests/contract/test_kronika_capture_services.py
```

Commit `94e605c17b881461fad3e22fd8c7fca32cb93976` on `feat/kronika-one-product`. Parent `c975aba14840b97944aecc655907e3abc370341d`. Tree `4667f47c24e84d80574beb66b71aca533393d994`. Worktree clean. One commit above the baseline. No push.

AP pin remains `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. No diff from the baseline for `.gitmodules`, `ap.project.conf`, `poetry.lock`, `pyproject.toml`, `AGENTS.md`, or `src/framenest`. Local `main`, `origin/main`, and public `refs/heads/main` remain `c975aba14840b97944aecc655907e3abc370341d`.

Deviations: none.
Risks: this session is non-independent. `-nolock` was chosen from `Xvfb -help`; this grant did not start Xvfb.
Missing evidence: a live Xvfb process under the corrected unit. The host retry is the check.
Smallest next step: fresh acceptance of this correction.

Orchestration critique:
MEASURED: none
LEAD: `-nolock` is advertised by the installed `Xvfb -help` and is now the unit text, but this grant did not start the server; the later host retry is the cheapest check that the display stays up.
Resolved Execution Issues / Near-Misses: none
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
