### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 22
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-C3-REACCEPTANCE
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
Result evidence: read-only candidate inspection, baseline `git show`, declared route, one temporary probe root
Start commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
End commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
Logical-whole closure: not-closed
Report justification: final-acceptance

Independence posture: this session began with the acceptance prompt. It did not implement or correct the C3 change or any earlier S3 candidate, and it did not receive a prompt from another session. Verdicts come from the candidate tree, the baseline object `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, the declared route, and the local `systemd.exec(5)` text. Owner-map reports and `00_notes.md` were not re-opened and were not used as implementation reasoning. Requested reasoning: High. This session does not self-verify a model identity.

Changed files: none in the FrameNest checkout. The only write is this report. Purpose: fresh independent acceptance of the capture-runner temporary-directory correction; no product correction.

Tests and validation: declared route, all exit 0. `ap project check` PASS. `ap exec` test-focus: 131 passed. `node --test tests/capture_lifecycle.test.js`: 52 passed, 0 failed. Details are in the control matrix.

Git result: no stage, commit, or push in either repository. Public `refs/heads/main` remains the parent. The candidate was not published.

Deviations: none. Risks and missing evidence: synthetic tests do not prove host Chromium startup. The installed `/etc/kronika-capture/capture.env` was not read, so an installed `TMPDIR` assignment remains an open deployment-time check.

Smallest next step: publish the accepted candidate `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, then, under a separate grant, deploy it, reinstall the unit, and perform the single corrected bootstrap start.

## Acceptance and Correction Record

```text
Acceptance candidate: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
  (tree 3b9014956a3bc738a209af51034fcac58ef5c498, branch feat/kronika-one-product,
   parent e408bb5503f359ec24542304ac1a621c6b9e4ffb)
Acceptance owner map: the C3 delta (3 paths, e408bb5..candidate); accepted plan
  15_report_00.md §3 C3; 19_report_00.md branch B and decision table; the
  prerequisite probe 20_report_00.md; implementation report 21_report_00.md; the
  classified instrumented-launch evidence in 00_notes.md
Acceptance allowlist: read-only review of the candidate and governing AP; the
  declared focused route; one declared temporary probe root under /tmp
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: completed below with directly observed results
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

Issued record had `Primary fresh acceptances used: 0`. This exchange is that primary fresh acceptance, so the completed count is 1. No out-of-scope observation was recorded.

## Identity observed

Checkout `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`, clean index and worktree before and after the route. `git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'` exited 0:

```text
fd277a9a64a6965df76127dbec5b1735d2fb3cdd
3b9014956a3bc738a209af51034fcac58ef5c498
e408bb5503f359ec24542304ac1a621c6b9e4ffb
```

Subject: `fix(capture): point the capture runner temporary directory at its runtime dir`. Parent is the single commit above. Governing AP gitlink and detached `.ap` HEAD: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. Local `main` and `origin/main`: `e408bb5503f359ec24542304ac1a621c6b9e4ffb`. No upstream is configured for `feat/kronika-one-product`. `private/**` was not read. No NUC, SSH, gate, host service, `sudo`, token, browser profile, or `/etc/kronika-capture/capture.env` access was performed.

## Per-claim verdicts

### 1. Exact and contained unit change — established

The runner unit delta against the baseline is exactly two lines. Added line: `Environment=TMPDIR=/run/kronika-capture/tmp`. Replaced line: `ExecStartPre` still uses `/usr/bin/install -d -m 0700` and now lists `/var/lib/kronika-capture/profile`, `/var/lib/kronika-capture/staging`, and `/run/kronika-capture/tmp`.

`User`, `Group`, `WorkingDirectory`, `Environment=PYTHONUNBUFFERED=1`, `Environment=DISPLAY=:99`, `Environment=XAUTHORITY=/run/kronika-capture/Xauthority`, `EnvironmentFile`, `ExecStart`, `Restart=no`, `LoadCredential`, `StateDirectory`, `StateDirectoryMode`, `UMask`, `NoNewPrivileges=true`, `ProtectSystem=strict`, `ProtectHome=read-only`, `ReadWritePaths`, the `Protect*`/`Restrict*`/`Lock*` and capability directives, `[Unit]`, and `[Install]` are unchanged because they are outside that two-line delta. `ExecStart` is still `kronika-capture --state-dir /var/lib/kronika-capture runner run ...`. No `PrivateTmp=` line was added. `ReadWritePaths` remains `/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix`, so no general `/tmp` path was added.

### 2. Causal regression — established

`test_runner_temporary_directory_stays_inside_the_runtime_boundary` asserts the exact new `Environment=` and `ExecStartPre` lines, the unchanged `ReadWritePaths` line, no bare `/tmp` element in that path list, absence of `PrivateTmp=true` from the runner and Xvfb unit text, `ProtectSystem=strict`, `NoNewPrivileges=true`, and no `TMPDIR` assignment in `kronika-capture.env.example`. The test-file diff has 29 insertions and 0 deletions, so existing assertions were preserved.

Applied to baseline unit text from `git show e408bb5503f359ec24542304ac1a621c6b9e4ffb:deploy/systemd/kronika-capture-runner.service`, the two new exact lines are absent and the old `ExecStartPre` without `/run/kronika-capture/tmp` is present. Both new lines are present on the candidate. The preserved `ReadWritePaths`, `ProtectSystem=strict`, and `NoNewPrivileges=true` lines are present on both. The regression fails on the baseline text and holds on the candidate.

### 3. Documentation — established

`docs/UBUNTU_NUC_DEPLOYMENT.md` now attributes the `/tmp` write to the Xvfb unit, records `TMPDIR=/run/kronika-capture/tmp` and the mode `0700` directory, and states that general `/tmp` write access for the runner and `PrivateTmp` remain prohibited. The deleted wording is only `the unit keeps /tmp writable`; `the rest of the filesystem stays read-only` and `The cookie is generated when Xvfb starts.` remain. The change does not say that synthetic tests prove host startup. The unchanged following paragraph still says synthetic tests alone do not establish whether Chromium can start on the host. Sandbox, loopback, credential, and journal paragraphs are outside the hunk. The Xvfb unit still has `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture` and is byte-identical to the baseline, so the Xvfb `/tmp` statement stays distinct from the runner.

### 4. Containment — established

`git diff --name-status e408bb5503f359ec24542304ac1a621c6b9e4ffb HEAD` exited 0 and listed only:

```text
M	deploy/systemd/kronika-capture-runner.service
M	docs/UBUNTU_NUC_DEPLOYMENT.md
M	tests/contract/test_kronika_capture_services.py
```

Numstat: service `2 1`, docs `8 2`, tests `29 0`. `git diff-tree --no-commit-id --name-only -r HEAD` lists the same three paths. No capture Python or JavaScript asset, protocol, HTTP endpoint, CLI command, journal schema, other unit, `framenest.service`, AP file, managed block, upgrade ledger, `poetry.lock`, `pyproject.toml`, `AGENTS.md`, or Meta artifact is in the commit. `kronika-capture.env.example` is identical to the baseline. Public `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` exited 0 and returned `e408bb5503f359ec24542304ac1a621c6b9e4ffb`. The same command for `refs/heads/feat/kronika-one-product` returned no ref. No remote-tracking branch contains HEAD. `git merge-base --is-ancestor HEAD main` exited 1. Nothing was pushed.

### 5. Preserved boundaries — established

The three-path diff does not touch loopback binding, token or Host/Origin checks, credential loading, browser lifecycle, durable submission, automatic resend, or journal recovery. `ExecStart`, `LoadCredential`, and `EnvironmentFile` are unchanged. The lifecycle suite covering one persistent browser, durable send, no automatic resend, and loopback endpoint parsing passed unchanged; that file is not in the diff.

### 6. Evidence honesty and residual risk — established

The new test reads committed unit and template text. The lifecycle suite is synthetic. Neither starts host Chromium. The documentation change does not claim that they do. `/etc/kronika-capture/capture.env` was not read. Local `systemd.exec(5)` states that settings from `EnvironmentFile=` override settings made with `Environment=`, and its precedence list places `EnvironmentFile=` after `Environment=`. The unit sets `Environment=TMPDIR=...` and then `EnvironmentFile=/etc/kronika-capture/capture.env`. The committed template's only assignment is `KRONIKA_CHROMIUM_PATH=/usr/bin/chromium`. A host file that matches that template does not assign `TMPDIR`. Whether the installed file matches the template is not established.

## Control matrix

Positive controls, from `/home/agile/Projects/framenest`:

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
  exit 0
  fd277a9a64a6965df76127dbec5b1735d2fb3cdd
  3b9014956a3bc738a209af51034fcac58ef5c498
  e408bb5503f359ec24542304ac1a621c6b9e4ffb

git diff --name-status e408bb5503f359ec24542304ac1a621c6b9e4ffb HEAD
  exit 0
  3 modified paths, listed in claim 4

git show e408bb5503f359ec24542304ac1a621c6b9e4ffb:deploy/systemd/kronika-capture-runner.service
  exit 0
  baseline unit has no TMPDIR line and the old ExecStartPre without /run/kronika-capture/tmp

./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb
  exit 0
  final line: ap project check --baseline: PASS
  observed WARN before PASS: sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py -q -p no:cacheprovider
  exit 0
  131 passed in 0.84s
  same inherited-environment WARN, then operation test-focus OK

node --test tests/capture_lifecycle.test.js
  exit 0
  tests 52, pass 52, fail 0, cancelled 0, skipped 0, todo 0
  duration_ms 1586.360675
```

Negative and adversarial controls, probe root `/tmp/kronika-one-product-s3-c3-reacceptance`, mode `0700`, no files stored, removed after use:

- Leak hunt over the full three-path diff: no `--no-sandbox`, no `stealth`, no `User=` or `Group=` change, no `LoadCredential` change, no `--state-dir` or `ExecStart` change, no `framenest.service`, `AGENTS.md`, `poetry.lock`, `pyproject.toml`, `00_notes`, or `meta/` text. `PrivateTmp` occurs only in the new prohibition sentence and in the new negative assertions `PrivateTmp=true` not in the runner or Xvfb. The runner and Xvfb units have no `PrivateTmp=` directive on either side of the delta. `ReadWritePaths` is not changed in the unit. Xvfb, bridge, view, and VNC units are not in the diff. `XAUTHORITY` appears only as unchanged documentation context, not as a changed directive.
- Causality: baseline lacks both asserted new lines; the candidate has both. Observed flags: `BASE_HAS_NEW_ENV False`, `CAND_HAS_NEW_ENV True`, `BASE_HAS_NEW_PRE False`, `CAND_HAS_NEW_PRE True`.
- Candidate `ReadWritePaths` elements are `/var/lib/kronika-capture`, `/run/kronika-capture`, and `/tmp/.X11-unix`. Bare `/tmp` is absent. `ExecStartPre` uses `-m 0700`.
- The documentation change does not claim that synthetic tests prove host startup and does not grant the runner general `/tmp` access.
- The commit contains only the three allowlisted paths and no Meta artifact.

Unverified controls: none of the required controls above. Host Chromium startup and the installed `capture.env` contents were outside the grant and are residual risk, not unverified stand-ins for these controls.

## Findings

none

## Containment and cleanup

```text
Temporary root: /tmp/kronika-one-product-s3-c3-reacceptance
Owner: this Worker session
Mode: 0700
Contents class: empty; comparisons were computed in memory from git show
Cleanup owner: this Worker session
Cleanup outcome: removed
```

Product, test, documentation, AP, packaging, and configuration files were not edited. The FrameNest worktree was clean after the route. No subagent was used. No Meta commit was created.

## Residual risk and limitations

Synthetic contract and lifecycle tests do not establish that Chromium creates its singleton socket under `/run/kronika-capture/tmp` on the NUC. That proof remains the later separately authorized corrected start.

The installed `/etc/kronika-capture/capture.env` was not read. Because `EnvironmentFile=` overrides `Environment=`, an installed `TMPDIR` assignment would replace `TMPDIR=/run/kronika-capture/tmp`. The committed template does not assign `TMPDIR`. The deployment-time comparison of the installed file with that template remains open and is not assumed.

The local man page establishes the override rule. This session did not observe the NUC systemd version.

Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: the first local man extraction matched an earlier `EnvironmentFile=` cross-reference and did not show the override sentence; the directive body in `/usr/share/man/man5/systemd.exec.5.gz` was then read and states that `EnvironmentFile=` overrides `Environment=`; residual risk of that mis-read is none, and the installed capture.env remains unread by authority
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
