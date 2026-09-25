### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 16
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-DIAGNOSTICS-REACCEPTANCE
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
Result evidence: declared route plus synthetic probes under one temporary root; no host execution
Logical-whole closure: not-closed
Start commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
End commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
Report justification: final-acceptance

Independence posture: this session did not implement or correct S3. Prior plans and reports were not used as reasoning. Verdicts come from the candidate tree at the commit above, the parent diff against d63d0b725acedf49d1611224c3b5201a90e7ef90, the declared route, and the synthetic probes below.

Changed files: none in the FrameNest candidate. This report is the only new trace file. Product purpose of the candidate, unchanged by this audit: bounded startup diagnostics and fresh-identity activation readiness.
Tests and validation: declared route PASS, recorded below; adversarial probes 37/37 and 92/92 PASS.
Git result: no stage, commit, push, or publication. Public `refs/heads/main` on https://github.com/cisarik/framenest.git is d63d0b725acedf49d1611224c3b5201a90e7ef90. Local `main` and `origin/main` are the same commit. The candidate is not published.
Deviations, risks, or missing evidence: no host or Chromium startup was run; C3 remains unimplemented. See residual risk.
Smallest next step: publish the corrected commit, then run the single bounded host diagnostic.

## Identity observed

```text
checkout: /home/agile/Projects/framenest
branch: feat/kronika-one-product
HEAD: e408bb5503f359ec24542304ac1a621c6b9e4ffb
parent: d63d0b725acedf49d1611224c3b5201a90e7ef90
tree: dadc01726a354c319374832bfd385be0bdffb516
subject: fix(capture): diagnose startup and require fresh activation readiness
worktree: clean
.ap gitlink and detached .ap HEAD: 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

`private/**` was not read. No NUC, SSH, gate, or host command was issued. The transition probe intercepted `ssh` argv inside the process and never executed an SSH client.

## Acceptance and Correction Record

```text
Acceptance candidate: e408bb5503f359ec24542304ac1a621c6b9e4ffb
  (tree dadc01726a354c319374832bfd385be0bdffb516, branch feat/kronika-one-product,
   parent d63d0b725acedf49d1611224c3b5201a90e7ef90)
Acceptance owner map: the S3 slice paths (20 paths, 82a6a598..c975aba); correction
  deltas at c975aba..94e605c (4 paths) and 94e605c..d63d0b7 (3 paths); the accepted
  recovery plan 15_report_00.md; the C1+C2 implementation delta (7 paths,
  d63d0b7..candidate); implementation report 15_report_01.md; the classified host
  evidence in the plan
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused route; synthetic temporary probe state under one declared temporary root
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 3
Automatic corrections used: 3
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none
```

## Per-claim verdicts

### 1. C1 closure — established

`safeStartupDiagnostic` returns only `stage`, `reason`, `spawn_errno`, `exit_code`, `signal`, `endpoint_seen`, `endpoint_budget_exhausted`, `stderr_classification`, and `cleanup_failed`. A probe object carrying the marker `KRONIKA_PROBE_SECRET_MARKER` in message, stderr, path, URL, argv, environment, and profile fields produced a JSON record that did not contain the marker.

Occupied lock, unexpired interval, and unverifiable brake metadata are distinct reasons: `locked`, `interval_unexpired`, and `metadata_unverifiable`. Spawn errno values in the allowlist stay themselves; `EPERM` becomes `OTHER`; null stays null. Signals in the allowlist stay themselves; `SIGUSR1` becomes `OTHER`. Exit codes 0 and 255 are kept; 256 becomes null. Endpoint flags and `cleanup_failed` are strict booleans.

Stderr classes `sandbox_namespace`, `display_authentication`, `temporary_storage_read_only`, and `profile_in_use` matched the fixed failure wording, including a split line, and the marker on those lines did not enter the diagnostics object. A warning, a prefixed non-failure mention, a 4097-character line, and wording outside the four patterns stayed `unclassified`. Feeding exactly 65536 non-endpoint bytes made `endpoint_budget_exhausted` true and discarded a later loopback endpoint and marker. `ws://127.0.0.1` ports 1 and 65535 were accepted. Eight non-loopback or malformed endpoint lines were rejected by both the candidate and the parent parser.

One `runPersistentService` attempt that then looped through four unavailable hellos emitted one `capture_startup` record. A startup failure with `cleanup_failed` plus a later throwing `stop` emitted that startup record and two separate `capture_cleanup` records. The thrown error kept `reason=process_exited` and `exit_code=1`; the cleanup error text was not substituted. Confirmed termination removed the launch lock. Unconfirmed termination left the lock and set `cleanup_failed`. Spawn argv matched `chromiumLaunchArgs` from the parent, including `--remote-debugging-address=127.0.0.1`. The parent runner source has no `capture_startup` emission, and the parent driver does not export `safeStartupDiagnostic`.

### 2. C2 closure — established

The identity script selects only the service singleton record and prints a two-element JSON list. A service row containing the secret marker produced only the two lowercase UUIDs. A corrupt file produced `identity=unverifiable` with the marker absent from stdout and stderr. The local snapshot parser accepted that pair and refused the unverifiable token with exit 15. The message did not contain the marker.

Against the generated gate, with a stub `systemctl` and a synthetic journal, the candidate returned:

```text
old ready, old needs_admin, old browser_unavailable: starting
partially changed identities: starting
absent or invalid identities: starting
uppercase non-canonical identity: unverifiable
fresh ready with ActiveState active: ready
fresh ready with ActiveState activating: starting
fresh needs_admin: needs_admin
fresh browser_unavailable: browser_unavailable
ActiveState failed, journal absent: failed
systemctl exit 1: unverifiable
symlink journal: unverifiable
no previous identity and fresh ready: ready
no service row: starting
```

The parent gate, on the same journals, still returned `ready` for old ready, and returned `needs_admin` or `browser_unavailable` for old terminal rows. That is the causal delta. Fresh ready and fresh terminal states match the parent. The parent constant `CAPTURE_READINESS_DEADLINE_SECONDS` is 30; the candidate constant is 180.

`_verify_capture_readiness` mapped `needs_admin`, `browser_unavailable`, and `failed` to exit 16, and non-`starting` garbage to exit 15, without copying the probe marker into the exception text. While a stub kept returning `readiness=starting`, the real verifier raised exit 17 at a patched monotonic elapsed time of exactly 180 seconds. The poll count was still increasing after 30 seconds.

A stubbed `activate-capture` and `rollback-capture` each performed one capture pointer switch and one `kronika-capture-runner.service` restart, with zero web-service restarts. Readiness failure at exit 16 and restart failure at exit 15 printed `capture_release:` of the candidate SHA and did not issue a second restart. An unverifiable identity snapshot raised exit 15 with zero switches and zero restarts. `CAPTURE_BRIDGE_PROTOCOL` remains `1`. `EXTENSION_CONNECTED_WINDOW_S` remains 90. `src/kronika_capture/bridge/journal.py` is unchanged from the parent, so the journal schema is unchanged.

### 3. Zero-job recovery regression — established

A persisted `browser_unavailable` service row with zero jobs reconstructed as `needs_admin` / `E_AMBIGUOUS_SEND` and job counts `{active: 0, total: 0}`. A wrong intervention id and a non-null job id were both rejected with `E_IDEMPOTENCY_CONFLICT`. A ready hello alone left `needs_admin`. An explicit resume with `job_id` null and the current intervention id returned `readiness_pending`. A hello with a different `resume_id` left the pause. The matching `resume_id` cleared the service to `ready` with zero jobs. The journal inode was unchanged. A secret field injected into the old service row was absent from the reconstructed status and from the committed service record. No separate journal reset or state-directory recreation was used.

### 4. Preserved S3/S2 guarantees — established

Relative to `d63d0b7`, these paths have an empty diff: the five capture units under `deploy/systemd`, `src/kronika_capture/paths.py`, `src/kronika_capture/bridge/auth.py`, `src/kronika_capture/cli.py`, `src/kronika_capture/bridge/jobs.py`, `src/kronika_capture/bridge/journal.py`, `src/kronika_capture/config.py`, `job_engine.mjs`, and `protocol.js`. Inside `framenest_release.py`, the work gate, brake gate, web atomic switch, capture restart command, and bridge-protocol assignment have no changed patch lines. The readiness gate is the deliberate C2 change. Capture failure handling in the stubbed transition did not restart the web service.

### 5. Containment — established

`git diff --name-only d63d0b7..e408bb55` is exactly these seven paths:

```text
deploy/ubuntu/framenest_release.py
docs/UBUNTU_NUC_DEPLOYMENT.md
src/kronika_capture/_assets/extension/src/headless/driver.mjs
src/kronika_capture/_assets/extension/src/headless/runner.mjs
tests/capture_lifecycle.test.js
tests/contract/test_kronika_capture_services.py
tests/unit/chatgpt_page/test_capture_journal.py
```

Numstat total: 746 insertions, 49 deletions. `src/framenest/**`, `.ap`, `AGENTS.md`, `poetry.lock`, and `pyproject.toml` are unchanged. No protocol version, HTTP route, CLI command, or journal schema file changed. `docs/UBUNTU_NUC_DEPLOYMENT.md` describes the stages, the four stderr classes, exits 15, 16, and 17, the 180-second deadline, the null-job resume sequence, and states that synthetic tests do not establish whether Chromium can start on the host.

### 6. Evidence consistency — established

No probe started Chromium and none is reported as host proof. Product added lines contain no `TMPDIR` assignment. C3 is not in this candidate. Parent causality is the observed parent-versus-candidate gate output above, plus the absence of `capture_startup` in the parent runner. No parent red-run was required or performed.

## Control matrix

Positive controls, from `/home/agile/Projects/framenest`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb
  result: ap project check --baseline: PASS
  non-failing tool warning: sanitized inherited environment classes
  LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page -q -p no:cacheprovider
  result: 205 passed in 4.09s

node --test tests/capture_lifecycle.test.js
  result: tests 52, pass 52, fail 0, cancelled 0, skipped 0, todo 0
  duration_ms 1590.278499
```

Negative and adversarial controls:

```text
Temporary root: /tmp/kronika-one-product-s3-diag-reacceptance
Owner: this Worker
Mode: 0700, observed
Contents class: synthetic fixtures only
Cleanup owner: this Worker
Cleanup outcome: removed
```

C1 probe: 37 checks, 0 failed. C2, preservation, and zero-job probe: 92 checks, 0 failed. The secret marker did not appear in startup logs, diagnostic JSON, identity stdout, or readiness stdout.

## Findings

none

## Containment and cleanup

The candidate worktree was clean at start and clean after the probes. The temporary root was removed and a subsequent existence check reported it absent. No product, test, documentation, AP, packaging, or configuration file was edited. No Meta commit was created.

## Residual risk and limitations

The unique host cause of the missing Chromium startup is outside this candidate. C3 stays conditional on the later bounded host diagnostic. The readiness deadline was established with the real verifier and a patched monotonic clock, not a 180-second wall-clock wait. The generated gate was executed by extracting the `python3 -c` body and substituting the synthetic journal path for `/var/lib/kronika-capture/capture-journal.sqlite3`; the production path occurred once in each generated script and was not opened. `systemctl` was a PATH stub. These limits do not leave any fixed claim unverified.

Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: the first direct `.venv` Python start aborted because the AppImage `LD_LIBRARY_PATH` hid the interpreter libraries; the declared `ap exec` route had already sanitized that variable and passed. The C2 probe was rerun with `LD_LIBRARY_PATH` unset. The first C1 interval call acquired the brake twice without releasing the held lock, so the second call correctly reported `locked`; the probe was corrected to release after a successful acquire, and the rerun observed `interval_unexpired`. Neither event changed the candidate.
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
