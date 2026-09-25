### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 15
Worker exchange ordinal: 02

Persistent role identity: WORKER
Task identity: KRONIKA-ONE-PRODUCT-S3-DIAGNOSTICS-CORRECTION
Worker session profile: Implementation Worker
Phase: implementation
Native planning mode: not-used
Evidence posture: non-independent
Status: PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation

C1 startup diagnostics, C2 fresh-identity activation, and the zero-job recovery
regression are implemented and validated within the seven-path allowlist.
One local commit was created; no push. Acceptance and host recovery are not
claimed.

Start commit: d63d0b725acedf49d1611224c3b5201a90e7ef90
Start tree: 95862a1e012256829ada49ed780ad665cd2aea18
End commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
End tree: dadc01726a354c319374832bfd385be0bdffb516
End parent: d63d0b725acedf49d1611224c3b5201a90e7ef90
Branch: feat/kronika-one-product
Result artifact or commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
Commit subject: fix(capture): diagnose startup and require fresh activation readiness
Result evidence: 205 Python tests and 52 Node tests passed; one commit above the
authorized baseline; clean source index and worktree; exact changed-path match.

#### C1 correction evidence

Locations are relative to the source repository at the end commit.

- src/kronika_capture/_assets/extension/src/headless/driver.mjs:270 defines the
  allowlisted diagnostic projection; :292 distinguishes launch lock, unexpired
  interval, and unverifiable brake metadata; :339 classifies fixed stderr
  failure wording; :354 preserves the bounded loopback endpoint parser; :952
  records the startup stage and snapshots child failure fields before cleanup.
- src/kronika_capture/_assets/extension/src/headless/runner.mjs:363 records page
  opening and navigation failures, preserves E_BROWSER_UNAVAILABLE, and keeps
  the unavailable loop. Exactly one capture_startup record is emitted.
  capture_cleanup records at :391 and :401 separately identify failed startup
  cleanup or final shutdown. Cleanup cannot replace the first startup failure.
  Page/navigation failures snapshot the child's current exit code and signal.
- Spawn errno and signal are fixed enums or OTHER; exit code is an integer
  from 0 through 255 or null. Endpoint flags and cleanup status are booleans.
  No raw exception, stderr, endpoint URL, argv, environment value, profile
  path, DOM, or credential enters the new startup record.
- Stderr still has a 65,536-byte budget and a 4,096-character line limit.
  Classes are sandbox_namespace, display_authentication,
  temporary_storage_read_only, profile_in_use, or unclassified. Unrelated
  warning lines cannot manufacture a diagnosis. Byte accounting now counts
  consumed input bytes directly, including invalid UTF-8.
- tests/capture_lifecycle.test.js:517 exercises executable/profile preflight,
  occupied lock, unexpired interval, malformed/missing/future metadata and
  failed metadata writes through the real driver. :541 tests synchronous and
  asynchronous spawn errors. :558 tests all four stderr classes. :582 tests
  warnings, split/oversized input, exact byte exhaustion and rejected endpoint
  hosts. :606, :619 and :627 cover endpoint timeout, signal exit and CDP failure.
  :639 covers page opening, afterOpen and navigation failures.
- The failure harness drives three unavailable-loop iterations and asserts one
  start, one startup record, zero offers and no synthetic secret marker in
  logs. :656 proves unconfirmed termination retains the real brake lock,
  preserves the original CDP failure, and releases the lock only after
  confirmed termination. :673 tests a secondary shutdown exception; :684
  tests rejection of arbitrary diagnostic fields; :695 checks successful
  startup, one record, lock lifetime and the exact unchanged spawn argv.
- Observed result: all 52 Node tests passed, including the existing send
  barrier, ambiguous-send, delivery retry, reconnection and lifecycle tests.
  Documentation: docs/UBUNTU_NUC_DEPLOYMENT.md:133.

#### C2 correction evidence

- deploy/ubuntu/framenest_release.py:657 reads only journal service metadata.
  :690 creates the previous runner/browser-session snapshot. :1650 validates
  its bounded response, allowing absent identities for first activation and
  refusing an unverifiable snapshot before the pointer switch.
- :1758 places the snapshot after work and brake checks and before the existing
  pointer switch and single runner restart. :703 requires both valid
  identities to change before interpreting journal readiness. Old ready and
  old terminal readiness are starting. A failed unit remains immediately
  terminal; fresh needs_admin/browser_unavailable remain exit 16. Ready also
  requires an active runner unit.
- The deadline at :46 is 180 seconds; :1667 polls without another restart.
  Timeout remains exit 17. Failure after the switch retains and reports the
  new capture pointer. The connection fence and journal schema are unchanged.
- tests/contract/test_kronika_capture_services.py:536 executes the actual
  generated gate against a synthetic SQLite service record and a stubbed
  systemctl response. Each stale state first yields starting, then fresh ready
  succeeds after one restart. :547 proves fresh blocked states return exit 16
  without retry. :558 proves unchanged ready times out at simulated second
  180 with one switch and one restart. :569 proves failed-unit termination.
- :585 checks each partially changed identity, absent/invalid identities, and
  the active-unit requirement. :592 checks metadata-only snapshot output and
  first launch without creating an absent journal. :605 checks malformed
  snapshots refuse before switch/restart.
- Observed result: all 205 tests in the declared Python selection passed,
  including existing work/brake refusal, manifest validation, capture rollback
  and web/capture separation contracts. No generated sudo, SSH or systemctl
  command was executed against a host. Documentation:
  docs/UBUNTU_NUC_DEPLOYMENT.md:200.

#### Zero-job recovery regression

tests/unit/chatgpt_page/test_capture_journal.py:276 starts with zero jobs and
persists browser_unavailable through the manager API. Manager reconstruction
produces needs_admin/E_AMBIGUOUS_SEND. Wrong intervention and job identities
are rejected. Fresh ready alone and an incorrect resume acknowledgement leave
the pause intact. Explicit null-job resume followed by the matching ready
acknowledgement clears it, preserving zero jobs and persisted ready state.
No journal reset, SQL surgery or state-directory recreation is used in this
recovery scenario. This regression passed in the 205-test Python selection.
Documentation: docs/UBUNTU_NUC_DEPLOYMENT.md:209.

#### Declared validation route

Repository root: /home/agile/Projects/framenest

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90

./.ap/ap exec --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

Project check passed before mutation. The final Python run exited 0 with
205 passed in 4.09s. The final Node run exited 0 with 52 passed, 0 failed,
0 skipped, 0 cancelled, and 0 todo. AP used the trusted baseline contract and
CPython 3.13 under its sanitized execution envelope. No ambient Python or
substitute execution route was used. No test failure was observed.

Parent causality is supported by the reviewed baseline diff: the parent
discarded startup errors and emitted no startup diagnostic, while its gate
accepted persisted ready plus an active unit without an identity check.
The new assertions exercise those differences. No separate parent test run
was performed; no observed parent red-run result is claimed.

#### Changed paths and repository readback

The complete baseline-to-HEAD name-status result is:

```text
M deploy/ubuntu/framenest_release.py
M docs/UBUNTU_NUC_DEPLOYMENT.md
M src/kronika_capture/_assets/extension/src/headless/driver.mjs
M src/kronika_capture/_assets/extension/src/headless/runner.mjs
M tests/capture_lifecycle.test.js
M tests/contract/test_kronika_capture_services.py
M tests/unit/chatgpt_page/test_capture_journal.py
```

Exactly these seven files were staged and committed. git diff --check passed.
The end commit has exactly the authorized baseline as its parent, and the
baseline-to-HEAD commit count is 1. Post-commit git status --porcelain was empty.

AP gitlink and AP checkout HEAD both remain
7478ddb07d2c3911f79e1aa1441f0115a31c45d8; the AP checkout is clean.
The baseline comparison is empty for .ap, AGENTS.md including its managed
block, .gitmodules, ap.project.conf, docs/AP_UPGRADE_OBSERVATIONS.md,
poetry.lock, pyproject.toml, src/framenest and all deploy/systemd sources.
Local main and origin/main remain at the baseline. Direct public
git ls-remote --exit-code origin refs/heads/main readback after the commit also
returned d63d0b725acedf49d1611224c3b5201a90e7ef90.
Commit result: one local commit; no push; no publication; no Meta commit.

#### Limits and next step

No scope deviation. No host, NUC, SSH, worker gate, service, account, privilege,
browser, credential, external-provider or subagent action occurred. private/**
was not read. C3/TMPDIR was not implemented. Units, sandbox configuration,
spawn arguments, submission semantics, retry counts, token handling,
connection fence and journal schema remain unchanged.

The tests are synthetic and do not establish Chromium startup or a unique
cause of the missing host browser. Fixed stderr wording intentionally leaves
unrecognized output unclassified. Full-fresh independent acceptance,
publication and the bounded host diagnostic remain separate grants.

Smallest next step: full-fresh acceptance of
e408bb5503f359ec24542304ac1a621c6b9e4ffb against this correction contract.

Orchestration critique:
MEASURED: none
LEAD: none

Resolved Execution Issues / Near-Misses: final review found that page-opening
and navigation failures needed current child exit/signal fields rather than
the successful-start snapshot. The runner now snapshots those fields at the
failure, the causal assertions cover both exit and signal, and the final
declared tests pass. No unresolved execution issue remains.

Pre-existing Failure Classification: none

Report destination:
/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_01.md
External trace authority: historical-evidence-only.
Trace archival owner: COOPERATOR; wait-for-report.
Delivery: manual Cooperator delivery; save and complete readback before the
separate completion notice. No trace artifact grants follow-up authority.

Authority expiry: this terminal report ends the implementation grant.
No autonomous acceptance, publication, deployment or host continuation.
