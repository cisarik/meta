# Kronika one product — S3 C3: a writable temporary directory for the capture runner

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 21
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-C3-RUNNER-TEMPDIR
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: a capture service unit and its sandbox/temporary-storage boundary change, with runtime behavior and a full-fresh acceptance requirement; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository baseline from Step 0 before mutation.
The evidence below is Orchestrator-classified and cited; verify the named
sources yourself before changing anything. Implementation authority is
explicit and bounded to the exact allowlist. You may not self-certify; a
separate full-fresh acceptance follows.

## Starting state (verified read-only at issuance, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (parent
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`, subject
  `fix(capture): diagnose startup and require fresh activation readiness`);
  clean index and worktree; local `main` = `origin/main` = public
  `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Established evidence for the C3 trigger (accepted plan `15_report_00.md`
  §3 C3; probe `20_report_00.md`; instrumented launch classification
  recorded in `00_notes.md`): Chromium's Linux process singleton creates its
  socket directory with `ScopedTempDir::CreateUniqueTempDir()` in the
  temporary directory (`$TMPDIR`, else `/tmp`). The runner unit runs with
  `ProtectSystem=strict` and a writable-path allowlist of
  `/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix`, so general
  `/tmp` is read-only. The instrumented launch failed with
  `process_singleton_posix.cc:1043 Failed to create socket directory.` and
  exit 21; the P1 probe independently showed `/tmp` mkdir `EROFS`. The
  capture profile is not the cause.
- Do not contact the host. `private/**` is never read; never print or read the
  token value; never inspect the browser profile or its locks.

## Goal

Implement exactly the accepted C3 correction so the capture runner has a
writable temporary directory inside its existing sandbox boundary, with a
contract regression that would fail on the current tree, and the deployment
documentation note. One commit. No push. No host contact.

## Exact change set (allowlist)

```text
deploy/systemd/kronika-capture-runner.service
tests/contract/test_kronika_capture_services.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

### Required unit change

In `deploy/systemd/kronika-capture-runner.service`:

- Add exactly:

```ini
Environment=TMPDIR=/run/kronika-capture/tmp
```

- Extend the existing `ExecStartPre` to also create the runtime temporary
  directory at mode 0700, exactly:

```ini
ExecStartPre=/usr/bin/install -d -m 0700 /var/lib/kronika-capture/profile /var/lib/kronika-capture/staging /run/kronika-capture/tmp
```

- Keep every existing directive unchanged: `User`, `Group`,
  `WorkingDirectory`, the other `Environment=` lines, `EnvironmentFile`,
  `ExecStart`, `Restart=no`, `LoadCredential`, `StateDirectory`,
  `StateDirectoryMode`, `UMask`, `NoNewPrivileges=true`,
  `ProtectSystem=strict`, `ProtectHome=read-only`, `ReadWritePaths`, the
  `Protect*`/`Restrict*`/`Lock*`/capability directives, `[Unit]` and
  `[Install]`. Do not add general `/tmp` write access, `PrivateTmp`, or any
  new writable path. `/run/kronika-capture` already exists (the Xvfb unit's
  `RuntimeDirectory`) and is writable by the capture account.

### Required contract regression

Extend the existing capture-service contract test
(`tests/contract/test_kronika_capture_services.py`) so it fails on the
baseline tree and passes after the correction. At minimum assert:

- the exact `Environment=TMPDIR=/run/kronika-capture/tmp` line in the runner
  unit;
- the exact `ExecStartPre` line above, including `-m 0700` and all three
  paths;
- the runner's `ReadWritePaths` is unchanged and does not add a bare `/tmp`;
- `PrivateTmp=true` is still absent from the runner and Xvfb units;
- the existing sandbox assertions remain in force;
- `/etc/kronika-capture/capture.env` (the committed
  `kronika-capture.env.example`) does not define `TMPDIR`, so it cannot
  override the intended value.

Keep the existing tests intact; extend rather than replace. Do not weaken any
security assertion.

### Required documentation

In `docs/UBUNTU_NUC_DEPLOYMENT.md`, document the correction: Chromium's Linux
process singleton creates its socket directory under the temporary directory,
so the runner sets `TMPDIR` to the already-writable runtime directory; the
`ExecStartPre` creates it at mode 0700; general `/tmp` write access and
`PrivateTmp` remain prohibited. Keep the existing capture diagnostics and
activation documentation consistent.

## Step 0 — repository preconditions (fail closed)

- Confirm the physical root, branch, HEAD, parent, tree, clean index and
  worktree, local `main` = `origin/main` = `e408bb5…`, the public
  `refs/heads/main` via `git ls-remote`, and the AP pin `7478ddb0…` (gitlink
  and `.ap` HEAD). Classify any divergence with the five RF-12 recovery
  classes; stop on unexplained remainder.
- Confirm the consumer-declared route below is usable. No host, SSH, gate,
  sudo, service or browser action is authorized.

## Declared execution route

Run from the repository root with the exact baseline:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py -q -p no:cacheprovider
```

JavaScript tests: not-used — no asset or JavaScript change in this slice.
Do not use an ambient Python or substitute route. Contract tests are the
causal evidence for the unit change; the host behavior is proven by the later
separately authorized corrected start, not by these tests.

Validation ladder: selected.
Inspection and provenance: required.
Existing focused tests: `tests/contract/test_kronika_capture_services.py`.
Affected tests: the Python selection above.
New causal regression: the unit contract extension — the baseline asserts no
TMPDIR/socket-directory guarantee and must fail the new assertions.
Broad or full suite: not-used.
Runtime or testbed: not-used for this repository slice.
Independent acceptance: required-separate-fresh-worker (full-fresh, runtime
change); the implementation Worker must not claim it.

## Git and commit rules

One commit on `feat/kronika-one-product` above the exact baseline, staging
only the allowlist. Suggested subject (use exactly):

```text
fix(capture): point the capture runner temporary directory at its runtime dir
```

Before committing, show `git diff --name-status` against the baseline and
confirm exactly the three allowed paths; run `git diff --check`; after the
commit confirm the worktree is clean and no other path changed. Do not push,
fetch, tag, or touch any other ref. Do not commit Meta artifacts.

## Authority and containment

Positive authority: read-only repository inspection; edits to exactly the
three allowed paths; the two declared route commands; one local commit; the
terminal report write at the exact destination below when absent; full
readback of the saved report.

Negative authority: no host, SSH, worker gate, sudo, service, account,
systemd, AppArmor, mount or browser action; no `activate-capture`; no release
helper; no profile, token, journal or credential access; no `private/**`; no
dependency, lockfile, packaging, AP or migration change; no file outside the
allowlist; no push/publication; no subagents; no ambient execution route.

## Stopping conditions

Stop and report on: any repository-gate mismatch; an unusable declared route;
a required change outside the allowlist; a failing test that cannot be fixed
inside the allowlist; a need for host, credential or network action; or any
instruction conflict. Preserve the first causal failure; do not improvise.

## Completion and report contract

`PASS` means the three-path change is committed with the contract regression
passing through the declared routes and the worktree clean. `PARTIAL` when
useful work exists but a gate or evidence is incomplete. `BLOCKED` when the
slice cannot proceed inside the boundaries. Use
`Phase-qualified result: implementation-PASS` for PASS, otherwise
`not-applicable`, and `Logical-whole closure: not-closed`. `Report
justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the exact
changed paths; the exact new unit lines and test assertions; the route
commands with their exit results and pass counts; the commit SHA, parent,
tree and subject; post-commit status; deviations, risks and missing evidence;
the smallest next step (full-fresh independent acceptance of the new
candidate); authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; the short completion notice to the
Cooperator is in Slovak, masculine address. Finalize the report, save it at
the exact destination, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Do not run `sudo -K` or `sudo -v`; this grant
uses no privilege. Terminal report or cancellation expires this authority.

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
Downloadable prompt filename: 21_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 21_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
