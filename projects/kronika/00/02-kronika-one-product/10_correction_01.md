# Kronika one product — S3 host defect correction

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: stop a looping host service and correct two runtime defects in installed unit sources with a regression that proves the exact command lines parse; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal BLOCKED report `10_report_00.md` for task
`KRONIKA-ONE-PRODUCT-S3-HOST`, Worker session 10, exchange 01, ending at
repository HEAD `c975aba14840b97944aecc655907e3abc370341d`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded correction authority for the two
defects below, plus the immediate host cleanup, for this session only. The
correction may not self-certify; a fresh acceptance follows, then publication
and the host retry.
Reuse rationale: this session holds the exact host evidence, the installed
state and the journal causes. Repository and environment re-gating is required
before mutation; retained context is convenience only.
Evidence posture: non-independent.
New terminal report: required (`10_report_01.md`).

## Confirmed findings (from the host run; do not reopen)

**F-HOST-01 — wrong `--state-dir` position.** The bridge and runner units place
`--state-dir` after the subcommand
(`kronika-capture bridge run --state-dir …`,
`kronika-capture runner run --state-dir …`). The CLI parent parser accepts
`--state-dir` only before the subcommand, so both services exited 2 with
`unrecognized arguments`. The same mistake was in the granted status command.

**F-HOST-02 — Xvfb cannot create its lock file.** The Xvfb unit runs under
`ProtectSystem=strict` with `ReadWritePaths=/tmp/.X11-unix /run/kronika-capture`.
Xvfb needs to create `/tmp/.X99-lock` (journal showed `/tmp/.tX99-lock`) and
exited 1, so the runner's required display never came up and activation
reported `readiness=failed` instead of `needs_admin`.

Host residue to clean: `kronika-capture-bridge.service` is still
auto-restarting; runner and Xvfb are failed; the three units are enabled; no
browser process exists.

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `c975aba14840b97944aecc655907e3abc370341d`, clean index and worktree; local
  `main` = `origin/main` = public `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Host capture state from exchange 01 remains: account `kronika-capture`
  (uid 996), capture directories, two matching 0600 token files (never read),
  five installed units, `capture.env`, `capture-current` at the accepted
  release, three enabled units, and the looping bridge.
- `private/**` is never read. Never print or read the token value.

## Step 0 — preconditions

- The three `FRAMENEST_NUC_SSH_*` names are present (names only); if unset,
  stop `BLOCKED`.
- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready`; remote `sudo -n true` exits 0. The Cooperator established
  the timestamp outside this Worker; use `sudo -n` only, never `sudo -v`.

## Correction A — host cleanup first (bounded, reversible)

Through the worker gate, in this order:

```text
sudo -n systemctl stop kronika-capture-bridge.service
sudo -n systemctl stop kronika-capture-runner.service
sudo -n systemctl stop kronika-capture-xvfb.service
sudo -n systemctl disable kronika-capture-xvfb.service kronika-capture-bridge.service kronika-capture-runner.service
sudo -n systemctl reset-failed kronika-capture-bridge.service kronika-capture-runner.service kronika-capture-xvfb.service
```

Verify read-only: `systemctl is-active` for the three is `inactive` or
`failed` with `NRestarts=0`; `pgrep -c -x chrome` and `pgrep -c -x Xvfb` are
`0`; ports 8765/5900/6080 have no listeners. Do not uninstall units, do not
remove the account, paths, token or release; the later retry reuses them.

Read-only probe for Correction B:

```text
/usr/bin/Xvfb -help
```

Inspect the output for `-nolock` and report whether the installed Xvfb supports
it. Do not start anything.

## Correction B — repository unit fixes

1. Bridge unit: move `--state-dir` before the subcommand:

```text
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge run --port 8765
```

2. Runner unit: same move, keeping the explicit profile, port and headed mode:

```text
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed
```

3. Xvfb unit: prefer the least-privilege lock fix. If the probe shows
   `-nolock` is supported, add it while keeping `-nolisten tcp` and `-auth`:

```text
ExecStart=/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -nolock -auth /run/kronika-capture/Xauthority
```

   If `-nolock` is not supported, add `/tmp` to the unit's
   `ReadWritePaths` (keeping `/tmp/.X11-unix` and `/run/kronika-capture`) and
   record that broader grant as the documented fallback. Do not use
   `PrivateTmp` for Xvfb or the runner.

4. Strengthen `tests/contract/test_kronika_capture_services.py`:

   - Replace the weak substring assertion with a causal regression that
     extracts each CLI `ExecStart` from the bridge and runner units, strips the
     executable, and proves the remaining arguments parse with the candidate
     CLI parser (`kronika_capture.cli.build_parser()`), so a wrong option
     position or an unknown option fails the test.
   - Assert the chosen Xvfb lock strategy: `-nolock` present, or the fallback
     `ReadWritePaths` including `/tmp`, consistent with the actual unit text.
   - Keep every existing directive assertion intact.

5. Update `tests/unit/chatgpt_page/test_systemd_credentials.py` only if its
   expected launcher argv encodes the wrong CLI order; read before editing.
6. Update `docs/UBUNTU_NUC_DEPLOYMENT.md` and `deploy/ubuntu/README.md` only if
   they state the corrected command lines or the lock behavior.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `c975aba14840b97944aecc655907e3abc370341d`
Changed-path allowlist:

```text
deploy/systemd/kronika-capture-xvfb.service
deploy/systemd/kronika-capture-bridge.service
deploy/systemd/kronika-capture-runner.service
tests/contract/test_kronika_capture_services.py
tests/unit/chatgpt_page/test_systemd_credentials.py
docs/UBUNTU_NUC_DEPLOYMENT.md
deploy/ubuntu/README.md
```

Implementation boundaries: the two corrections, the lock strategy and the
regression tests above; nothing else.
Independence required: no

## Positive authority

The gate commands above; the read-only `Xvfb -help` probe; the allowlisted
repository edits; the declared route; one local commit; the report write.

Declared route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d

./.ap/ap exec --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

No ambient Python, `poetry run` or substitute route. No Node suite change is
expected.

## Negative authority

- Host: only the stop/disable/reset-failed commands above; no install, start,
  enable, deploy, activate, login, view, resume or ask; no token read or
  regeneration; no account/path removal.
- Repository: no other unit, helper, capture source, packaging, AP or
  documentation change; no push or publication (a separate grant follows).
- No `sudo -v`, no `private/**`, no subagents, no Meta commit.

## Validation

1. Host after cleanup: three units inactive/failed with `NRestarts=0`, no
   chrome/Xvfb processes, no listeners on the three ports, units disabled.
2. The Xvfb probe result is reported and the chosen lock strategy matches the
   actual unit text.
3. The new regression test fails against the old command order and passes
   against the corrected units; every existing directive assertion still
   passes. Demonstrate this by running the focused test against the corrected
   tree (and, if practical, show the parser rejecting the old order).
4. The declared route passes; `git diff --name-status <baseline>..HEAD` equals
   the allowlist; clean worktree; one commit above the baseline; branch, HEAD,
   parent and tree read back.
5. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `src/framenest/**` and `AGENTS.md`
   unchanged; local `main` and public `main` still at the baseline until the
   publication grant.
6. A terminal remote `sudo -K` releases the timestamp; confirm with a failing
   `sudo -n true`.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; a
host command whose result is unexpected; a repository change needed outside
the allowlist; a route failure that cannot be corrected inside the allowlist;
or any conflict with the host evidence. Preserve the first causal failure and
do not improvise host commands.

## Completion and report contract

`PASS` means both corrections and the regression are committed within the
allowlist, the host cleanup is verified, the declared route passed, and the
Xvfb lock strategy is chosen from the probe. `PARTIAL`/`BLOCKED` otherwise. No
push. The fresh acceptance, publication and host retry follow as separate
grants.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include: the compact core; the host
cleanup result; the `Xvfb -help` `-nolock` finding; the exact corrected unit
lines; the regression evidence (old order failing, new order passing); the
route results; changed files; commit result with `no push`; deviations/risks/
missing evidence; one smallest next step (fresh acceptance of the correction);
`Report justification: new-mutation`; authority expiry; and:

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
Downloadable prompt filename: 10_correction_01.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 10_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
