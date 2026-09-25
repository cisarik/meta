### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product  
Worker session ordinal: 15  
Worker exchange ordinal: 01

# S3 host recovery: bounded diagnosis and completion plan

```text
Persistent role identity: WORKER
Task identity: KRONIKA-ONE-PRODUCT-S3-RECOVERY-PLAN
Native planning mode: required
Phase: planning
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Evidence tier: E0
Validation ladder: not-used
Independent acceptance: not-required
Report justification: new-evidence
Delivery: one Markdown artifact in this session
Changed files: none
Commit/push result: not authorized; not performed
```

PASS applies to the planning deliverable. It does not establish the host launch cause, deployment acceptance or S3 completion.

The Cooperator’s current instruction replaces the report-file write, filesystem readback and file-receipt requirements. No report was written, and no file hash or persistence receipt is claimed.

## 1. Verified baseline and principal findings

Start and end commit:

```text
d63d0b725acedf49d1611224c3b5201a90e7ef90
```

Verified locally:

| Gate | Result |
|---|---|
| Physical checkout | `/home/agile/Projects/framenest` |
| Branch | `feat/kronika-one-product` |
| HEAD tree | `95862a1e012256829ada49ed780ad665cd2aea18` |
| Local `main`, `origin/main` | Both equal HEAD |
| Index and worktree | Clean at start and end |
| Recorded AP gitlink and detached AP HEAD | Both `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` |
| Public branch | Supplied verified evidence; not independently refreshed in this exchange |
| Execution | Read-only inspection only; no tests, host, gate, SSH, browser or network calls |

The required historical reports, governing Worker/AP contracts and relevant implementation paths were inspected. The classified host attempts were treated as input, not repeated.

The plan has three conclusions:

1. **The missing Chromium process has no uniquely established host cause yet.** The code deliberately hides the startup exception, so the empty application journal does not distinguish lock, brake, executable, filesystem, display or sandbox failures.
2. **The zero-job journal state has a designed recovery path.** A working browser, explicit resume with `job_id=None`, and the runner’s subsequent readiness acknowledgement suffice. Deleting or editing the journal is unnecessary.
3. **Capture activation has a separate verification defect.** Its readiness check can accept the previous runner’s persisted `ready` state. Correct this before relying on activation as completion evidence.

## 2. Repository-grounded diagnosis

### Browser launch and the silent runner

The actual service path is:

```text
systemd runner unit
  -> Python CLI build_runner_argv()
  -> node <packaged runner.mjs> run ...
  -> modeRun()
  -> runPersistentService()
  -> ChromiumDriver.start()
  -> spawnProcess(configured executable, chromiumLaunchArgs(), ...)
```

There is no `startBrowser` function in the current capture implementation.

Relevant source evidence:

| Source | Established behavior |
|---|---|
| `cli.py:281–324` | Node receives the systemd credential directory as `--state-dir`, but receives the explicit browser profile separately. |
| `runner.mjs:159–171,383–392` | That Node state directory supplies the bridge token; the explicit profile determines browser storage. |
| `driver.mjs:884–917` | Checks executable/profile accessibility, acquires the launch brake, spawns once, discovers the endpoint and connects CDP. |
| `driver.mjs:936–944` | Endpoint discovery has a 20-second deadline and detects spawn errors or child termination. |
| `runner.mjs:363–380` | Catches startup/open/navigation failure without logging the exception, then continues reporting `browser_unavailable`. |
| `runner.mjs:306–359` | A connected job loop can remain alive without a functioning browser. |

Consequently, `active`, `Result=success` and `client_connected=true` do not prove browser startup. Report `10_report_05.md` is consistent with this exact failure path.

The launcher’s credential-directory argument is intentional. With the unit’s explicit:

```text
--profile /var/lib/kronika-capture/profile
--port 8765
```

it does not move the browser profile or its launch metadata into the read-only credential directory. Authentication already succeeding also makes a missing Node token an unsupported explanation for the classified attempt.

### Launch lock and brake

`driver.mjs:250–291` implements an exclusive directory lock and persisted start timestamp outside the browser profile:

```text
/var/lib/kronika-capture/profile.capture-launch/lock
/var/lib/kronika-capture/profile.capture-launch/last-start.json
```

The driver canonicalizes the profile directory itself without enumerating its contents.

Lifecycle:

- The lock is acquired before checking/writing the timestamp.
- The timestamp is committed before spawning Chromium. A failed spawn therefore consumes the 300-second interval.
- The lock remains held while the browser is owned.
- Confirmed shutdown releases the lock and preserves `last-start.json`.
- Unconfirmed termination deliberately retains the lock.
- Abrupt process termination can leave an orphaned lock.
- A pre-existing directory with missing, malformed, oversized or future metadata fails closed.
- Waiting 300 seconds does not remove a lock or repair unverifiable metadata.
- The runner does not retry startup after any of these failures.

The release helper’s brake gate checks the timestamp, **not the exclusive lock**. Thus `brake=ok` alone cannot establish that the driver can acquire its lock.

Manual recovery may remove only an empty orphaned `lock` directory, after the runner is stopped and absence of all capture browser processes is established. Preserve the timestamp. Never delete the launch-state directory to manufacture a first launch, and never inspect or remove Chromium’s profile-internal locks.

### Display, temporary files and sandbox

The runner unit establishes:

```text
User=kronika-capture
DISPLAY=:99
XAUTHORITY=/run/kronika-capture/Xauthority
ProtectSystem=strict
NoNewPrivileges=true
RestrictSUIDSGID=true
CapabilityBoundingSet=
ReadWritePaths=/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix
```

Xvfb and the runner share the display socket and Xauthority path without private `/tmp` namespaces. The Node child inherits the service environment.

The corrected Xvfb unit permits writes throughout `/tmp`; the runner unit does not. This is a concrete configuration difference and a plausible Chromium temporary-file failure, **not yet a proven launch cause**.

Historical acceptance records say `/usr/bin/chromium` resolves to Chrome for Testing, user-namespace restriction is enabled, and an AppArmor userns profile exists. They explicitly did not prove that the configured executable can launch under this service’s sandbox.

The diagnostic must distinguish:

- executable access/spawn failure;
- launch lock or timestamp refusal;
- read-only temporary storage;
- display/Xauthority failure;
- sandbox/userns denial;
- profile-in-use refusal reported by Chromium;
- endpoint parsing exhaustion/timeout;
- CDP or subsequent page/navigation failure.

No branch permits `--no-sandbox`, disabling AppArmor/userns restrictions, enabling stealth, adding `-ac`, or replacing the profile.

### Version-parser claim

`parseChromiumMajorVersion()` is called only by `readChromiumMajorVersion()` in the capture source. There is no call to that reader from the current startup path.

Furthermore, `ChromiumDriver.start()` rejects stealth, and the runner parser rejects `--stealth`.

The precise conclusion is therefore stronger than “stealth-path-only”: **the current capture startup does not execute the version parser at all**. The earlier CfT version-parsing problem is not the cause of this startup failure.

### Endpoint parsing and observability

`driver.mjs:294–312` accepts only a complete:

```text
DevTools listening on ws://127.0.0.1:<port>/devtools/browser/<id>
```

line, within a 65,536-byte input budget and 4,096-character line limit. Unrelated stderr is discarded. Large startup noise or an unrecognized endpoint can produce an indistinguishable generic failure.

Preserve these limits and the prohibition on raw browser stderr logging. Add fixed diagnostic classifications, not browser-log passthrough.

## 3. Source corrections and acceptance

Implement the two established corrections together against the verified baseline. They do not claim to fix the unknown host launch cause.

### C1. Preserve safe startup diagnostics

Files:

```text
src/kronika_capture/_assets/extension/src/headless/driver.mjs
src/kronika_capture/_assets/extension/src/headless/runner.mjs
tests/capture_lifecycle.test.js
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Required behavior:

- Preserve public error code `E_BROWSER_UNAVAILABLE`.
- Attach internal, allowlisted diagnostic fields for the failed stage: executable preflight, profile-directory preflight, lock, brake metadata, spawn, endpoint, CDP connection, page opening or navigation.
- Distinguish an occupied launch lock, an unexpired interval and unverifiable timestamp metadata.
- Preserve a bounded spawn errno, numeric child exit code, allowlisted signal, endpoint-seen flag and endpoint-budget-exhausted flag.
- Within the existing bounded stderr processing, recognize fixed classifications for sandbox/namespace refusal, X display/authentication failure, read-only temporary storage and profile-in-use refusal. Emit only the classification; discard the input text.
- Unknown messages remain `unclassified`. Do not infer a cause from an unrelated warning.
- Log one sanitized startup outcome from the runner. Never interpolate raw exceptions, stderr, URLs, argv, environment values, profile paths, DOM or credentials.
- Preserve the first startup failure if shutdown also fails; report cleanup failure separately.
- Preserve exactly one startup attempt, existing cleanup, the launch brake and the unavailable service loop.

Required causal tests:

- Each launch stage produces the expected safe classification.
- Startup failure emits one record and makes one start attempt across multiple job-loop iterations.
- Synthetic secret markers in stderr, exception messages and paths never reach logs.
- Oversized/split stderr remains bounded; non-loopback endpoints remain rejected.
- Confirmed termination releases the lock; unconfirmed termination retains it.
- Diagnostics do not change spawn arguments, submission behavior or retry counts.

### C2. Require fresh readiness after activation

Files:

```text
deploy/ubuntu/framenest_release.py
tests/contract/test_kronika_capture_services.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Established defect:

- `cmd_remote_capture_readiness_gate()` accepts `service.state == ready` plus an active unit.
- Restarting the runner does not clear the bridge’s previous service record.
- `JobManager.hello()` can reject the new runner with `E_BUSY` while the previous hello remains inside the 90-second connected window.
- The helper currently has a 30-second readiness deadline.

Required behavior:

1. After work and brake checks, snapshot the journal’s previous runner and browser-session identities, using only service metadata.
2. Switch the pointer and restart exactly once.
3. Treat readiness belonging to that previous identity as `starting`, including stale terminal readiness.
4. Accept `ready` only after both valid runner and browser-session identities have changed and the runner unit is active.
5. A failed unit is immediately terminal. A fresh runner’s `needs_admin` or `browser_unavailable` remains terminal.
6. Use a bounded 180-second capture readiness deadline, accommodating the existing 90-second connection fence and reconnect backoff.
7. On timeout or failure, retain the new pointer and report failure without another restart.

Do not change the bridge’s connection fence or reset the journal to accelerate activation.

Required causal tests:

- Old `ready` survives restart: activation must not return success.
- Old `browser_unavailable` survives restart: it must not cause premature terminal failure before the new identity arrives.
- Fresh identity plus `ready`: success after one restart.
- Fresh identity plus blocked readiness: exit 16, no retry.
- No fresh identity: exit 17 at the deadline, no retry.
- A failed unit remains immediately terminal.
- Existing work refusal, brake refusal, manifest validation and web/capture separation still pass.

### C3. Conditional temporary-directory correction

Apply only if the bounded host diagnostic establishes Chromium temporary-file failure against the runner’s read-only temporary location.

Files:

```text
deploy/systemd/kronika-capture-runner.service
tests/contract/test_kronika_capture_services.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Exact change:

```ini
Environment=TMPDIR=/run/kronika-capture/tmp
ExecStartPre=/usr/bin/install -d -m 0700 /var/lib/kronika-capture/profile /var/lib/kronika-capture/staging /run/kronika-capture/tmp
```

Keep the existing writable-path allowlist, display sharing and sandbox directives. The runtime directory is already writable; this does not require making all of `/tmp` writable for the runner.

Acceptance must prove the selected temporary directory is writable by the service account under the unit’s restrictions. The subsequent single corrected browser start must prove the configured Chromium actually uses the correction successfully. A source assertion alone does not close the host defect.

A sandbox denial, profile-in-use failure or unclassified failure does **not** select C3. Those outcomes stop for an exact evidence-based grant. No speculative AppArmor policy, binary replacement or profile reset belongs to this plan.

### Acceptance and publication route

C1, C2 and any selected C3 change runtime behavior. Under AP’s “Acceptance, Correction, and Escalation” rule, their re-acceptance class is **full-fresh**, not scoped.

Required acceptance evidence:

- Frozen candidate commit, tree and exact changed-path list.
- Independent positive/negative results for the corrections.
- Preserved credential, Host/Origin, journal, single-browser and no-resend boundaries.
- Synthetic logging leak controls.
- No claim that synthetic tests establish host Chromium startup.

Planned validation commands, with the exact authorized baseline substituted:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <AUTHORIZED_BASELINE>

./.ap/ap exec --root /home/agile/Projects/framenest --baseline <AUTHORIZED_BASELINE> --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

Also add the zero-job restart/resume scenario described below to `tests/unit/chatgpt_page/test_capture_journal.py`.

Publication and deployment need separate explicit authority. The accepted correction must be public and deployed before the host executes it. Do not patch installed release files.

There are no new public CLI commands, HTTP endpoints, protocol versions or journal schemas. The diagnostic fields are operational log fields; the freshness snapshot is internal to the release helper.

## 4. Journal recovery and activation contract

`JobManager.__init__()` at `jobs.py:148–178` converts a previous `needs_admin` **or** `browser_unavailable` service state into a new blocked service state with reason `E_AMBIGUOUS_SEND`, even when there are no jobs.

This explains how the classified empty journal can legitimately hold that reason. It does not prove an actual send occurred.

`hello()` can subsequently change its visible state to `browser_unavailable` while retaining the intervention ID. This matches the transition between reports `10_report_04.md` and `10_report_05.md`.

The correct zero-job recovery is:

1. Establish a functioning, logged-in browser on the runner-owned page.
2. Read current authenticated status and require `jobs.active=0`, `jobs.total=0`, `active_job=null`.
3. Use the **current** intervention ID; do not reuse the historical ID.
4. Run `bridge resume --intervention-id …`, omitting `--job-id`.
5. The CLI sends `job_id=None`. `resume()` verifies that identity and persists a `resume_id`.
6. The response is `status=readiness_pending`, not proof of readiness.
7. The runner receives that resume ID through hello and echoes it in a subsequent hello containing freshly observed `ready`.
8. `hello()` commits `ready` and clears the intervention, reason and pending resume fields.

A ready browser alone does not clear the persisted pause. A resume request alone does not clear it either. Both are required.

Add a causal recovery test that starts with zero jobs and persisted `browser_unavailable`, reconstructs the manager, observes `needs_admin/E_AMBIGUOUS_SEND`, rejects wrong intervention/job identities, and clears only after explicit null-job resume plus matching fresh readiness acknowledgement.

**No transient-journal reset is required.** Direct SQL updates, deleting the database or recreating the state directory would bypass fencing and recovery guarantees. They are excluded.

Activation order in the accepted helper is:

```text
validate requested release and --yes
verify installed SHA, manifest and capture runtime identity
verify web identity and capture protocol compatibility
drain queued work
refuse live or paused work
enforce persisted 300-second brake
atomically switch capture-current
restart runner once
verify readiness
report both pointers
```

Work-gate classifications:

| State | Result |
|---|---|
| Offered/running job | `blocked=live` |
| `needs_admin` job or service | `blocked=paused` |
| Queued job | `blocked=queued`; bounded drain |
| No blocking job and service `browser_unavailable` | Can produce `blocked=none` |
| Unverifiable journal | Refusal |

Thus `blocked=none` is not a browser readiness check. Keep the work gate intact; complete explicit recovery before final activation.

## 5. Single bounded host diagnostic

All commands below are **future execution instructions**, not actions taken in this exchange.

### Ownership and prerequisites

- Worker commands use `scripts/operator/network/framenest_nuc_worker_gate.fish`.
- Complex shell blocks, runtime drop-in creation and interactive view/login are Cooperator-executed.
- The gate rejects shell metacharacters and multiline commands. Do not bypass it with another Worker SSH route.
- Workers never execute `sudo -v` or `sudo -K`. The Cooperator establishes and releases privilege manually.
- Freeze all capture submissions until the single final synthetic ask.
- Let `S3_RELEASE` denote the exact accepted, published and deployed correction SHA. Future grants must bind its literal value.
- Keep both existing releases and all profile, credential and journal state.

First prepare, independently accept and publish C1+C2. Then use the canonical helper, with its configured private transport values kept out of reports:

```text
deploy/ubuntu/framenest-release status
deploy/ubuntu/framenest-release check --release <S3_RELEASE>
deploy/ubuntu/framenest-release deploy --release <S3_RELEASE> --yes
```

Stop on any failed gate. A successful check does not itself authorize deployment.

### D1. Inspect current state without launching

Through the Worker gate, use these individual bounded remote commands:

```text
sudo -n true
sudo -n systemctl show kronika-capture-runner.service -p ActiveState -p SubState -p Result -p NRestarts -p User -p Group -p ProtectSystem -p NoNewPrivileges -p ReadWritePaths
sudo -n systemctl show kronika-capture-xvfb.service -p ActiveState -p Result -p NRestarts
sudo -n systemctl show kronika-capture-bridge.service -p ActiveState -p Result
sudo -n readlink /opt/framenest/current
sudo -n readlink /opt/framenest/capture-current
sudo -n -u kronika-capture /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
sudo -n -u kronika-capture test -r /run/kronika-capture/Xauthority
sudo -n test -S /tmp/.X11-unix/X99
sudo -n readlink -e /usr/bin/chromium
sudo -n sysctl -n kernel.apparmor_restrict_unprivileged_userns
```

Check installed configuration against the accepted sources using selected non-secret fields. Do not dump environments, credentials, Xauthority contents or browser command lines.

Require zero jobs and no competing capture browser. Count **browser roots**, distinguishing Chromium child processes by their process type; a raw `pgrep -c chrome` count is not a one-browser invariant.

If current evidence already shows a healthy browser, preserve it and stop the launch diagnostic for Orchestrator reconciliation.

### D2. Stop the unavailable runner and classify launch state

Stop only the runner:

```text
sudo -n systemctl stop kronika-capture-runner.service
```

Confirm it is inactive and that its browser process tree is gone. Preserve the running bridge and Xvfb.

The Cooperator inspects only the external brake metadata:

```bash
# [NUC / bash]
sudo -n -u kronika-capture python3 - <<'PY'
import json, math, os, stat, time
from pathlib import Path

directory = Path("/var/lib/kronika-capture/profile.capture-launch")
out = {"directory": "absent", "lock": "absent", "metadata": "absent"}
try:
    ds = directory.lstat()
    if not stat.S_ISDIR(ds.st_mode):
        raise ValueError()
    out["directory"] = "directory"
    try:
        ls = (directory / "lock").lstat()
        out["lock"] = "directory" if stat.S_ISDIR(ls.st_mode) else "invalid"
    except FileNotFoundError:
        pass
    fd = os.open(directory / "last-start.json", os.O_RDONLY | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_size > 256:
            raise ValueError()
        raw = os.read(fd, 257)
    finally:
        os.close(fd)
    value = json.loads(raw)["started_ms"]
    now = time.time() * 1000
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError()
    if not math.isfinite(value) or value < 0 or value > now:
        raise ValueError()
    out["metadata"] = "valid"
    out["remaining_ms"] = max(0, math.ceil(value + 300000 - now))
except FileNotFoundError:
    if out["directory"] != "absent":
        out["metadata"] = "unverifiable"
except (OSError, ValueError, TypeError, KeyError):
    out["metadata"] = "unverifiable"
print(json.dumps(out, sort_keys=True))
PY
#------------------------------------------------------
```

Interpretation:

- Absent directory: first-use acquisition is possible.
- Valid timestamp and remaining interval: wait for expiry; do not edit it.
- Invalid lock or unverifiable metadata: stop.
- Empty orphaned lock, with stopped runner and independently confirmed zero capture browser processes: the later grant may authorize exactly:

```text
sudo -n -u kronika-capture rmdir /var/lib/kronika-capture/profile.capture-launch/lock
```

A non-empty directory, race or removal failure stops recovery. This does not authorize recursive removal.

### D3. Run the accepted diagnostic code under the actual unit

The capture pointer is still on the earlier release. To obtain C1 diagnostics without weakening the paused-work activation gate, use one explicitly authorized temporary `ExecStart` override pointing to the accepted correction release.

This is a recovery bootstrap, not completed capture activation. Record the effective runner SHA separately from the capture pointer.

Preconditions: zero jobs, no browser, valid expired brake, working display, exact installed release provenance, no conflicting recovery override.

The Cooperator executes:

```bash
# [NUC / bash]
(
set -eu
: "${S3_RELEASE:?Exact accepted release SHA required}"
[[ "$S3_RELEASE" =~ ^[0-9a-f]{40}$ ]]
test "$(cat "/opt/framenest/releases/$S3_RELEASE/.framenest-release-sha")" = "$S3_RELEASE"
test ! -e /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf
test ! -L /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf

sudo -n install -d -m 0755 /run/systemd/system/kronika-capture-runner.service.d
printf '%s\n' \
  '[Service]' \
  'ExecStart=' \
  "ExecStart=/opt/framenest/releases/$S3_RELEASE/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed" \
  | sudo -n tee /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf >/dev/null
sudo -n systemctl daemon-reload
sudo -n systemctl start kronika-capture-runner.service
)
#------------------------------------------------------
```

This preserves the actual unit’s account, credentials, display, mount restrictions and sandbox. It avoids diagnosing a different unsandboxed shell launch.

Observe for at most 180 seconds, using short polling intervals. Read only C1’s allowlisted startup records, authenticated status, process identity and listener metadata. Do not print raw browser stderr or unrestricted journals.

Expected classification:

| Result | Interpretation and next action |
|---|---|
| Lock/brake refusal; no spawn | Follow D2 only; never launch around the brake. |
| Spawn errno | Exact executable/permission/runtime prerequisite failure; stop. |
| Display/authentication failure | Verify display socket and Xauthority accessibility; no Xauthority dump or `-ac`; stop for correction. |
| Temporary-filesystem failure | Select C3 only with matching mount/configuration evidence. |
| Sandbox/userns failure | Correlate with bounded kernel denial metadata for the attempted process and actual executable; stop for a separately specified policy correction. |
| Profile-in-use | Stop; no profile inspection or lock deletion. |
| Endpoint timeout/exhaustion | Record the bounded parser outcome and child disposition; no raw-stderr escalation or alternate endpoint discovery. |
| CDP/page/navigation failure | Record the exact stage; do not relabel it as login readiness. |
| Successful startup; structural login blocker | Keep this browser alive and continue to owner login. |
| Unclassified failure | Stop with the preserved classification; no second diagnostic launch. |

AppArmor correlation must report only whether a relevant denial was established, its operation class and the matched process identity. Absence of a matching audit event is not proof that sandbox policy is correct.

### Diagnostic cleanup and attempt budget

On failure:

1. Stop the runner and verify browser termination.
2. Remove only `90-s3-recovery.conf`.
3. Reload systemd without starting the runner.
4. Preserve launch timestamp, journal, profile, tokens and release pointers.
5. Leave pre-existing bridge/Xvfb state recorded.
6. The Cooperator releases privilege.

On success, retain the browser through login and resume. Remove the override before final activation; `daemon-reload` alone does not restart the running browser.

Budget:

- At most one diagnostic browser spawn.
- If C3 is causally selected, one separately accepted corrected start after the brake.
- One later planned activation restart.
- No repeated failed launch, automatic rollback launch or synthetic-ask retry.

## 6. Ordered host completion

### H1. Complete any evidence-selected correction

If D3 succeeds, continue with that running browser.

If C3 is selected, stop and clean up as above. Implement C3, obtain full-fresh acceptance, publish and deploy the resulting exact SHA, install its runner unit, and perform one explicitly authorized corrected bootstrap start. Do not repeat unrelated setup or reinstall the token.

Any other failed diagnostic exits this completion sequence. The next grant must name the evidenced correction; this plan does not grant an improvised repair.

### H2. Cooperator view and login

Require one running capture browser, active Xvfb, functioning CDP and a structural login/intervention state.

The Cooperator starts the temporary view:

```bash
# [NUC / bash]
sudo -n systemctl start kronika-capture-vnc.service
sudo -n systemctl start kronika-capture-view.service
#------------------------------------------------------
```

Confirm that the view listeners are loopback-only and retain their 1,800-second runtime limits.

The Cooperator opens the tunnel from his MacBook:

```fish
# [MacBook / fish]
ssh -N -o ExitOnForwardFailure=yes \
  -L 127.0.0.1:6080:127.0.0.1:6080 \
  -i "$FRAMENEST_NUC_SSH_IDENTITY" \
  "$FRAMENEST_NUC_SSH_USER@$FRAMENEST_NUC_SSH_TARGET"
#------------------------------------------------------
```

He opens `http://127.0.0.1:6080/vnc.html`, selects the runner-owned ChatGPT page if necessary, and completes login/challenges himself. Agents neither view the authentication screen nor handle credentials.

Do not invoke `kronika-capture login`; it launches a separate browser path.

After login, the Cooperator stops the view and closes the SSH tunnel:

```bash
# [NUC / bash]
sudo -n systemctl stop kronika-capture-view.service
sudo -n systemctl stop kronika-capture-vnc.service
#------------------------------------------------------
```

Verify ports 5900 and 6080 are closed. Login success is an owner observation; operational readiness still requires the next step.

### H3. Explicit zero-job resume

Read authenticated status using the accepted bootstrap release CLI:

```text
sudo -n -u kronika-capture /opt/framenest/releases/<S3_RELEASE>/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
```

Require zero jobs and a current intervention ID. Then execute once:

```text
sudo -n -u kronika-capture /opt/framenest/releases/<S3_RELEASE>/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge resume --intervention-id <CURRENT_INTERVENTION_ID>
```

Expected immediate response: `readiness_pending`.

Poll authenticated status for at most 30 seconds. Require:

```text
readiness = ready
reason = null
intervention_id = null
client.connected = true
jobs.active = 0
jobs.total = 0
active_job = null
```

A pending response, browser absence, persistent login blocker or identity conflict stops the sequence. Do not issue repeated resume requests to clear an unexplained failure.

### H4. Wait for the brake, remove the bootstrap override, activate

Record the bootstrap browser PID/start identity and `browser_session`. Recheck the external timestamp and wait until at least 300 seconds have elapsed since its recorded start.

Remove only the temporary override:

```bash
# [NUC / bash]
sudo -n rm /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf
sudo -n systemctl daemon-reload
#------------------------------------------------------
```

Verify the effective `ExecStart` again resolves through `capture-current`. The running browser is retained until activation.

From the repository root, through the canonical release route:

```text
deploy/ubuntu/framenest-release status
deploy/ubuntu/framenest-release check --release <S3_RELEASE>
deploy/ubuntu/framenest-release activate-capture --release <S3_RELEASE> --yes
```

Require exit 0 and C2’s fresh identity evidence. Do not accept an old persisted `ready`.

Any exit 16, 17, 22, 23 or transport/source failure stops. Preserve the actual pointer outcome; never automatically repeat activation or roll back.

### H5. Verify the final service before submitting anything

Require all of the following:

- Web and capture pointers both identify `S3_RELEASE`.
- Installed release manifests match the accepted commit and runtime/unit identities.
- No recovery override remains.
- Runner uses its normal `capture-current` command.
- Xvfb, bridge and runner are active; runner/Xvfb automatic restart counts have not increased.
- Exactly one capture browser root exists. Chromium renderer, GPU and utility children are allowed.
- Browser PID/start identity and `browser_session` are new relative to the bootstrap.
- Authenticated status is freshly `ready`, connected and without an intervention.
- Bridge port 8765 and the browser CDP listener bind only to `127.0.0.1`.
- View ports 5900/6080 and Xvfb TCP port 6099 are closed.
- State/profile/staging privacy remains 0700 and journal/token privacy remains 0600, verified from metadata only.

Repeat process identity and authenticated readiness after a 30-second stability interval. A process appearing momentarily is insufficient.

### H6. One synthetic ask as the capture user

Through the Worker gate, execute exactly once:

```text
sudo -n -u kronika-capture /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture ask --quiet --timeout 120 "Reply with exactly KRONIKA_S3_OK."
```

Expected:

```text
exit status: 0
stdout: KRONIKA_S3_OK.
```

Treat the requested punctuation consistently with the actual answer when recording the synthetic result; a nonempty completed synthetic answer establishes the basic ask path, while an instruction-following difference is recorded separately.

Do not retry a failed or ambiguous ask.

Afterward, require:

- One terminal successful synthetic job and no active job.
- `submission=send_confirmed`.
- One durable send-intent transition and one send-confirmed transition.
- Service still `ready`.
- Same browser PID/start identity and `browser_session` as immediately before the ask.
- View still stopped.
- No new browser launch or runner restart.

Report only synthetic answer evidence and operational metadata. Omit conversation URLs and unrelated content.

## 7. S3 acceptance, limits and closeout

S3 may be declared complete by the Orchestrator only after receiving:

1. Full-fresh acceptance for the exact corrections used.
2. Publication evidence tying the accepted SHA to public `main`.
3. Exact deployed manifest and both final pointer identities.
4. A classified successful browser launch under the installed service account and sandbox.
5. Cooperator confirmation of login and view closure.
6. Null-job resume acknowledgement followed by fresh authenticated `ready`.
7. Successful activation with a new runner/browser identity and exactly one planned restart.
8. Stable one-browser, loopback-listener and private-state evidence.
9. One successful synthetic ask without resend, browser replacement or output-file creation.
10. Removal of the temporary override, no outstanding host mutation, and Cooperator privilege-release disposition.

The present exchange establishes none of those live results.

Remaining host uncertainties are the actual lock/timestamp state, configured executable and effective policy, temporary-directory behavior, display access and current ChatGPT structural readiness. They are resolved by the bounded diagnostic and completion evidence, not by additional repository speculation.

A source-only review cannot guarantee that Chromium starts on this NUC. The plan’s deterministic failure outcome is a classified stop with preserved evidence. It never substitutes a sandbox bypass, state deletion or another blind launch.

S4 remains the accepted Search/Research slice: mode support, complete-output handling, provenance and its separate acceptance. This recovery does not implement S4 or reopen S0–S2 and S4–S10 product decisions.

```text
Tests and validation:
Read-only source, contract, historical-evidence and Git inspection.
No tests, builds, host probes or runtime checks executed.

Deviations:
Session-only report delivery replaces the original file-delivery instructions
under the Cooperator's current explicit directive.
Public branch state was not directly observed because network use was forbidden.

Orchestration critique:
MEASURED: The runner suppresses startup failure detail, while activation reads
persisted readiness without requiring a new runner identity. This permits
uninformative launch failures and premature readiness success. Smallest
correction: bounded safe startup diagnostics plus fresh-identity activation
verification, followed by one classified host diagnostic.

LEAD: The runner's read-only temporary location or executable-specific
AppArmor/userns policy may prevent Chromium startup. Neither is established
as the cause. Cheapest useful check: the single instrumented start under the
actual service unit.

Resolved Execution Issues / Near-Misses:
Oversized read output was replaced by targeted source excerpts. A test-file
lookup used a nonexistent name and was corrected using the discovered
test_capture_journal.py path. No execution or mutation followed those reads.

Pre-existing Failure Classification:
Earlier CLI/Xvfb failures are supplied classified historical evidence.
Silent startup failure and stale activation-readiness acceptance are
established-static findings at the verified baseline.
The host Chromium launch cause remains hypothesis-unverified.

Smallest next step:
ORCHESTRATOR accepts or rejects this plan, then issues a complete bounded
implementation grant for C1+C2 and their causal tests. Independent acceptance,
publication and the single host diagnostic remain separately authorized.

Authority expiry:
Submission of this terminal report expires the current planning authority.
No implementation, host action, publication or autonomous continuation follows.
```
