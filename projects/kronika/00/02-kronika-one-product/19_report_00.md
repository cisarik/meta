### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 19
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S3-PROFILE-IN-USE-RECOVERY-PLAN

Status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence

Start commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
End commit: e408bb5503f359ec24542304ac1a621c6b9e4ffb
Changed files: none
Tests/builds/interpreters executed: none
Host/browser/network actions: none
Stage/commit/push: none
Delivery: complete Markdown report in this session; no file written
```

# S3 ProcessSingleton refusal: bounded evidence and recovery plan

## 1. Findings and cause boundaries

**Recommend one evidence grant with zero browser starts. Do not select a profile replacement, TMPDIR correction, binary replacement or sandbox change from the current record.**

The evidence establishes a Chromium process that exited before endpoint discovery. It does not establish a live profile holder or the operation that prevented startup. The next step can distinguish several filesystem and configuration prerequisites without opening the profile. It cannot conclusively distinguish stale profile state from Chromium-specific behavior.

`PARTIAL` reflects those unresolved causes and the absence of an evidence-selected correction. The proposed next evidence operation has a fixed scope and stopping rule.

### Verified baseline and evidence classes

Local read-only Git inspection independently confirmed:

```text
Repository: /home/agile/Projects/framenest
Branch: feat/kronika-one-product
HEAD: e408bb5503f359ec24542304ac1a621c6b9e4ffb
Parent: d63d0b725acedf49d1611224c3b5201a90e7ef90
Tree: dadc01726a354c319374832bfd385be0bdffb516
Local main and origin/main: equal to HEAD
AP gitlink and .ap HEAD: 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Index and worktree: clean
```

Public branch state was not directly observed: network use was prohibited. The host state, exit 21, spent diagnostic budget, never-logged-in profile and D3 cleanup are **Orchestrator-relayed classified evidence**, not observations made in this session. [Task evidence, lines 51–105](/home/agile/.codex/attachments/a3d6bf3f-a463-4d48-b43a-7b53a8e3833c/pasted-text.txt:51)

The following distinctions are established statically at the verified baseline:

- Both recognized ProcessSingleton wordings become `profile_in_use`. The parser retains the first recognized classification and discards the text. The existing record cannot reveal which wording occurred, or whether both occurred. [driver.mjs:339–379](/home/agile/Projects/framenest/src/kronika_capture/_assets/extension/src/headless/driver.mjs:339)
- Profile preflight checks existence and canonicalizes the directory. It does not establish permission to create files inside it. Successful creation of the external brake proves access to a sibling location, not to the profile interior. [driver.mjs:292–335](/home/agile/Projects/framenest/src/kronika_capture/_assets/extension/src/headless/driver.mjs:292), [driver.mjs:952–977](/home/agile/Projects/framenest/src/kronika_capture/_assets/extension/src/headless/driver.mjs:952)
- Chromium receives the explicit profile path and loopback debugging arguments. Its environment is inherited. The runner unit permits writes to the state/runtime directories and the X display directory; it does not explicitly permit writes throughout `/tmp`. [driver.mjs:446–464](/home/agile/Projects/framenest/src/kronika_capture/_assets/extension/src/headless/driver.mjs:446), [runner unit:9–33](/home/agile/Projects/framenest/deploy/systemd/kronika-capture-runner.service:9)
- The startup record reports one failed attempt; an active runner can subsequently remain in its unavailable loop without another Chromium start. [runner.mjs:363–408](/home/agile/Projects/framenest/src/kronika_capture/_assets/extension/src/headless/runner.mjs:363)

### Candidate causes

| Candidate | Supporting or limiting evidence | What remains unknown |
|---|---|---|
| Live Chromium holding the profile | Relayed post-cleanup evidence reports no Chromium. This weighs against current live contention. It does not reconstruct process state at the failed start. | Whether any holder existed at that instant. No lock inspection is permitted. |
| Stale singleton state, PID reuse or cross-hostname state | Earlier unsuccessful starts make leftover state plausible. “Never logged in” does not establish an empty or untouched profile. | Whether such artifacts exist and whether this Chromium build would reject them. These are hypotheses, not findings. |
| Profile-directory permission or filesystem restriction | The driver checks existence, not writability. The external brake is outside the profile. | Effective directory ownership, permissions, mount access and profile-specific restrictions. Root-directory metadata can narrow this without reading contents. |
| Temporary-directory failure during singleton creation | The runner’s writable-path allowlist excludes general `/tmp`; the generic singleton wording can conceal the failed operation. | Whether this binary used `/tmp`, which operation failed, and whether the original message was the generic wording. C3 remains unselected. |
| AppArmor or another security restriction | The relayed host has the namespace restriction enabled. | No attempt-correlated denial establishes causality. An interpreter probe does not exercise Chromium’s executable-specific policy or user-namespace startup. |
| Invocation or path difference | The relayed start used the actual unit with an explicit release override. Source requires an explicit executable. | Current effective configuration and binary resolution can be compared without executing Chromium. Historical configuration cannot be reconstructed from current metadata alone. |
| Chromium-build-specific behavior | The configured binary is relayed as Chrome for Testing 154.0.8037.57. | Matching ProcessSingleton source, build-specific exit semantics and behavior are unverified. Exit 21 alone is not assigned a more specific meaning here. |

Sources: [classified host evidence](/home/agile/.codex/attachments/a3d6bf3f-a463-4d48-b43a-7b53a8e3833c/pasted-text.txt:60), [executable configuration and launcher](/home/agile/Projects/framenest/src/kronika_capture/cli.py:263), and the driver/unit locations above. No external Chromium research was performed.

The external brake, spawn failure, endpoint-budget exhaustion and later CDP/navigation failures are not supported as the immediate cause of this recorded attempt. The supplied record reached `endpoint`, reports `process_exited`, and contains neither spawn errno nor endpoint exhaustion. This does not certify those boundaries for future starts. [Recorded outcome](/home/agile/.codex/attachments/a3d6bf3f-a463-4d48-b43a-7b53a8e3833c/pasted-text.txt:67)

## 2. Proposed discriminating probes

**All commands below are proposals. None was executed.**

### P0 — Read-only service and process preflight

Execution owner: a fresh Worker, exclusively through the project SSH gate. Transport values remain in the existing private environment and are never echoed. The gate rejects multiline commands and shell metacharacters; do not transport P1 through an improvised SSH or encoded-command route. [Execution contract:131–175](/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md:131), [gate:229–261](/home/agile/Projects/framenest/scripts/operator/network/framenest_nuc_worker_gate.fish:229)

Run these individually, checking each result before continuing:

```text
scripts/operator/network/framenest_nuc_worker_gate.fish --probe

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'sudo -n true'

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'systemctl show kronika-capture-runner.service -p ActiveState -p SubState -p NRestarts -p User -p Group -p Restart -p NoNewPrivileges -p ProtectSystem -p ProtectHome -p ReadWritePaths -p PrivateTmp -p ProtectControlGroups -p ProtectKernelModules -p ProtectKernelTunables -p RestrictSUIDSGID -p LockPersonality -p CapabilityBoundingSet -p AmbientCapabilities'

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'systemctl show kronika-capture-xvfb.service kronika-capture-bridge.service -p Id -p ActiveState -p SubState'

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'pgrep -c -x chrome'

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'pgrep -c -x chromium'

scripts/operator/network/framenest_nuc_worker_gate.fish --command 'ps -u kronika-capture -o pid=,ppid=,comm='
```

Required interpretation:

- Runner must remain `inactive`; Xvfb and bridge must remain `active`.
- `pgrep` output `0` with exit 1 is the expected no-match result. Exit greater than 1 is a probe failure.
- Process names/PIDs are operational metadata. Never request command lines, environment, open files, browser tabs or socket endpoints.
- Compare unit restrictions with the baseline source. Unexpected activity, configuration drift, another possible browser process, unavailable privilege or incomplete output stops P1.
- No service is stopped or repaired under P0. No product status command is needed: this probe does not access the bridge token or journal.

The process-name check has a stated limit: it cannot prove the absence of every conceivable renamed browser executable. It refreshes the named evidence and detects unexpected capture-account processes.

### P1 — One synthetic filesystem/socket probe under matching restrictions

Execution owner: **Cooperator**, in an already-open NUC Bash session, after accepting the exact block below under the later evidence grant.

Purpose: test directory creation, ordinary file creation, symlink creation and Unix-domain socket binding in three synthetic locations. Inspect only metadata of the profile directory itself.

This is a transient interpreter service with the runner’s declared account and filesystem restrictions. It deliberately has no `LoadCredential`, `StateDirectory`, browser command or product launcher. Consequently, it tests the listed filesystem primitives, **not the complete Chromium sandbox or ProcessSingleton implementation**. The restrictions copied below come from [runner unit:9–33](/home/agile/Projects/framenest/deploy/systemd/kronika-capture-runner.service:9).

Allowed temporary roots:

```text
/tmp/.kronika-s3-singleton-probe
/run/kronika-capture/.kronika-s3-singleton-probe
/var/lib/kronika-capture/.kronika-s3-singleton-probe
```

All must initially be absent, including dangling symlinks. Each successful directory creation uses mode 0700; files use 0600. Only the fixed synthetic children `file`, `link` and `socket` may be created. No target is inside the browser profile.

```bash
# [NUC / bash]
(
set -eu
fail() { printf 'probe_guard=%s\n' "$1"; exit 1; }

sudo -n true || fail privilege

test "$(systemctl show kronika-capture-runner.service \
  -p ActiveState --value)" = inactive || fail runner_state
test "$(systemctl show kronika-capture-xvfb.service \
  -p ActiveState --value)" = active || fail display_state
test "$(systemctl show kronika-capture-bridge.service \
  -p ActiveState --value)" = active || fail bridge_state

for probe_name in chrome chromium; do
  if pgrep -x "$probe_name" >/dev/null; then
    fail browser_present
  else
    probe_status=$?
    test "$probe_status" -eq 1 || fail process_probe
  fi
done

test "$(systemctl show kronika-capture-runner.service \
  -p FragmentPath --value)" = \
  /etc/systemd/system/kronika-capture-runner.service \
  || fail unit_location
test -z "$(systemctl show kronika-capture-runner.service \
  -p DropInPaths --value)" || fail unit_override

sudo -n cmp -s \
  /etc/systemd/system/kronika-capture-runner.service \
  /opt/framenest/releases/e408bb5503f359ec24542304ac1a621c6b9e4ffb/deploy/systemd/kronika-capture-runner.service \
  || fail unit_source_mismatch

test "$(systemctl show kronika-s3-singleton-probe.service \
  -p LoadState --value)" = not-found || fail probe_unit_exists

if sudo -n systemd-run \
  --unit=kronika-s3-singleton-probe.service \
  --quiet --wait --pipe --collect \
  --property=Type=exec \
  --property=User=kronika-capture \
  --property=Group=kronika-capture \
  --property=WorkingDirectory=/opt/framenest/capture-current \
  --property=EnvironmentFile=/etc/kronika-capture/capture.env \
  --setenv=PYTHONUNBUFFERED=1 \
  --setenv=DISPLAY=:99 \
  --setenv=XAUTHORITY=/run/kronika-capture/Xauthority \
  --property=UMask=0077 \
  --property=Restart=no \
  --property=RuntimeMaxSec=30s \
  --property=TimeoutStopSec=5s \
  --property=NoNewPrivileges=yes \
  --property=ProtectSystem=strict \
  --property=ProtectHome=read-only \
  --property=PrivateTmp=no \
  --property='ReadWritePaths=/var/lib/kronika-capture /run/kronika-capture /tmp/.X11-unix' \
  --property=ProtectControlGroups=yes \
  --property=ProtectKernelModules=yes \
  --property=ProtectKernelTunables=yes \
  --property=RestrictSUIDSGID=yes \
  --property=LockPersonality=yes \
  --property=CapabilityBoundingSet= \
  --property=AmbientCapabilities= \
  /usr/bin/python3 -I - 2>/dev/null <<'PY'
import errno
import json
import os
import socket
import stat
import sys

roots = (
    ("tmp", "/tmp/.kronika-s3-singleton-probe"),
    ("runtime", "/run/kronika-capture/.kronika-s3-singleton-probe"),
    ("state", "/var/lib/kronika-capture/.kronika-s3-singleton-probe"),
)
allowed_errors = {
    "EACCES", "EPERM", "EROFS", "ENOSPC", "EDQUOT",
    "EEXIST", "ENOENT", "ENOTDIR", "ELOOP",
    "EOPNOTSUPP", "ENAMETOOLONG",
}

def emit(value):
    print(json.dumps(value, sort_keys=True), flush=True)

def error_class(error):
    name = errno.errorcode.get(getattr(error, "errno", None), "OTHER")
    return name if name in allowed_errors else "OTHER"

try:
    configured = os.environ.get("KRONIKA_CHROMIUM_PATH", "").strip()
    binary_ok = (
        configured == "/usr/bin/chromium"
        and os.path.realpath(configured)
        == "/opt/framenest/tooling/chrome-for-testing/154.0.8037.57/chrome-linux64/chrome"
        and os.access(configured, os.X_OK)
    )
    temp_environment_expected = all(
        os.environ.get(key) in (None, "", "/tmp")
        for key in ("TMPDIR", "TMP", "TEMP")
    )
    profile = "/var/lib/kronika-capture/profile"
    info = os.lstat(profile)
    profile_directory = stat.S_ISDIR(info.st_mode)
    profile_owner = info.st_uid == os.geteuid() and info.st_gid == os.getegid()
    profile_mode = stat.S_IMODE(info.st_mode) == 0o700
    profile_access = os.access(profile, os.W_OK | os.X_OK)
    roots_absent = all(not os.path.lexists(path) for _, path in roots)
    parents_directories = all(
        stat.S_ISDIR(os.lstat(os.path.dirname(path)).st_mode)
        for _, path in roots
    )
    emit({
        "probe": "preflight",
        "binary_expected": binary_ok,
        "temp_environment_expected": temp_environment_expected,
        "profile_directory": profile_directory,
        "profile_owner_expected": profile_owner,
        "profile_mode_0700": profile_mode,
        "profile_write_search_access": profile_access,
        "synthetic_roots_absent": roots_absent,
        "synthetic_parents_directories": parents_directories,
    })
    if not all((
        binary_ok, temp_environment_expected, profile_directory,
        profile_owner, profile_mode, profile_access,
        roots_absent, parents_directories,
    )):
        sys.exit(1)
except SystemExit:
    raise
except Exception as error:
    emit({"probe": "preflight", "error": error_class(error)})
    sys.exit(1)

overall = 0
for label, root in roots:
    created = []
    channel = None
    stage = "mkdir"
    result = {"probe": label, "result": "ok"}
    try:
        os.mkdir(root, 0o700)
        created.append((root, "directory"))

        stage = "file"
        fd = os.open(
            root + "/file",
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
        )
        created.append((root + "/file", "file"))
        try:
            os.write(fd, b"synthetic")
        finally:
            os.close(fd)

        stage = "symlink"
        os.symlink("file", root + "/link")
        created.append((root + "/link", "link"))

        stage = "socket"
        channel = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        channel.bind(root + "/socket")
        created.append((root + "/socket", "socket"))
    except Exception as error:
        result.update(
            result="refused", stage=stage, error=error_class(error)
        )
    finally:
        cleanup_ok = True
        if channel is not None:
            try:
                channel.close()
            except Exception:
                cleanup_ok = False
        for path, kind in reversed(created):
            try:
                if kind == "directory":
                    os.rmdir(path)
                else:
                    os.unlink(path)
            except Exception:
                cleanup_ok = False
        result["cleanup"] = "removed" if cleanup_ok else "retained"
        emit(result)
        if not cleanup_ok:
            overall = 1
    if overall:
        break

sys.exit(overall)
PY
then
  printf 'probe_transport=completed\n'
else
  probe_status=$?
  printf 'probe_transport=failed exit=%s\n' "$probe_status"
  exit "$probe_status"
fi
)
#------------------------------------------------------
```

Operational constraints:

- Run once. Unsupported systemd options, source mismatch or nonstandard configuration stop the probe; do not simplify the sandbox to obtain a result.
- P0’s complete output must be classified before P1. Do not race another operator changing the services.
- A refusal such as `EROFS` is useful probe evidence, not a successful browser diagnosis. `probe_transport=completed` means the script completed.
- Normal cleanup removes only objects created by this invocation, in reverse order, without recursion.
- On timeout, interrupted transport or cleanup failure, stop. Report the exact synthetic root labels potentially retained. Do not use recursive or wildcard deletion. Cooperator-owned recovery must confirm the transient service is stopped and ownership of any leftover exact objects before cleanup.
- P1 never reads the token, Xauthority contents, journal, profile contents or profile-internal locks. It never runs Chromium, including `--version`.

### Decision table after P0/P1

| Result | Established conclusion | Permitted recommendation |
|---|---|---|
| Profile-root ownership/mode/access fails | A necessary profile-root prerequisite is wrong now. | Cooperator-owned root-metadata correction or explicit profile decision; no recursive repair. |
| Synthetic state/runtime operations succeed; `/tmp` returns `EROFS` | Those filesystem primitives work in the approved writable locations; general `/tmp` creation fails under the reproduced restrictions. | Keep temporary storage as a supported candidate. **Do not automatically select C3:** the original Chromium operation/path remains unproven. |
| Symlink or socket operation fails in a writable synthetic root | A corresponding primitive is unavailable in this probe context. | Classify the exact operation and errno; stop before guessing filesystem, mount or policy changes. |
| All primitives succeed | The tested general prerequisites work. | Profile-specific state and Chromium-specific behavior remain unresolved. A profile decision or separately authorized version-specific evidence is required. |
| Configuration/binary comparison differs | Present configuration differs from the proposed baseline. | Stop with boolean mismatch evidence; do not print arbitrary values or repair automatically. |
| Unexpected process or service activity | The stopped-browser precondition is unavailable. | Stop without killing processes or testing locks. |

There is **no permitted read-only agent probe that conclusively identifies stale profile-internal artifacts under the stated boundary**. Do not disguise a profile clone, alternate-profile browser start, `strace` launch or another diagnostic start as a synthetic probe.

## 3. Correction branches and validation

These are conditional routes, not current mutation grants. Exactly one causal correction is selected after evidence reconciliation. A branch whose trigger remains unproven stays closed.

### A. Bounded C1 wording refinement

The source establishes a diagnostic information gap. Refining it is justified if a separately accepted correction will receive a browser start and its failure must distinguish the two wordings. Refinement alone does not justify another start.

Exact change set:

```text
src/kronika_capture/_assets/extension/src/headless/driver.mjs
tests/capture_lifecycle.test.js
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Behavior:

- Preserve `E_BROWSER_UNAVAILABLE`, `stderr_classification=profile_in_use`, existing fields, endpoint handling, cleanup and startup count.
- Add one allowlisted diagnostic field, `profile_singleton_detail`, with:
  `unobserved`, `in_use_wording`, `creation_failed_wording`, `both`.
- Recognize only the two already accepted anchored wordings, using the existing optional ERROR/FATAL prefix handling.
- Track those fixed flags across eligible lines inside the existing 65,536-byte/4,096-character bounds. Earlier generic wording must not hide later in-use wording.
- Treat these values as **wording observations**, never as proof of a live holder, stale locks or an errno.
- Discard all input text. Unknown supplied values become `unobserved`.
- No change to `runner.mjs` is expected: its record already passes through `safeStartupDiagnostic`. No change to public bridge/API schemas.

The baseline’s test covers the in-use wording but does not separately exercise the generic ProcessSingleton wording. Extend the existing fixture and logging tests rather than introducing another suite. [Lifecycle tests:458–579](/home/agile/Projects/framenest/tests/capture_lifecycle.test.js:458)

Required cases:

- Each wording alone, both orders, split chunks, repeated wording.
- ERROR/FATAL prefixes accepted; warnings and embedded mentions rejected.
- Overlong lines and exhausted byte budget cannot manufacture detail.
- Secret markers, fake hostname/PID/path suffixes and arbitrary fields never appear in logs.
- Exit 21 is preserved; one startup record, one spawn, zero offers across unavailable iterations.
- Existing endpoint, termination, brake and exact-argument tests remain valid. [Existing negative and lifecycle coverage:582–720](/home/agile/Projects/framenest/tests/capture_lifecycle.test.js:582)

Acceptance class: **full-fresh independent acceptance**, because logging/runtime behavior changes. [.ap/AP.md, Acceptance, Correction, and Escalation:607–631](/home/agile/Projects/framenest/.ap/AP.md:607)

### B. Proven temporary-storage failure

Trigger: evidence identifies a temporary-storage failure relevant to the configured Chromium startup. A synthetic `/tmp` refusal alone does not meet the previously accepted C3 trigger.

If selected, retain the exact accepted C3 change:

```text
deploy/systemd/kronika-capture-runner.service
tests/contract/test_kronika_capture_services.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

```ini
Environment=TMPDIR=/run/kronika-capture/tmp
ExecStartPre=/usr/bin/install -d -m 0700 /var/lib/kronika-capture/profile /var/lib/kronika-capture/staging /run/kronika-capture/tmp
```

Keep every existing sandbox directive and writable-path boundary. Check that the nonsecret environment file does not override the intended value. Do not add general `/tmp` write access or `PrivateTmp` as an unproven substitute.

Extend the existing unit contract to verify the added runtime directory, its mode, TMPDIR and unchanged restrictions. Those source assertions establish configuration, not causality. The synthetic primitive probe and the single corrected Chromium start supply the separate host evidence. [Accepted C3:255–278](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:255), [existing unit tests:184–235](/home/agile/Projects/framenest/tests/contract/test_kronika_capture_services.py:184)

Acceptance class: full-fresh independent acceptance. No deployment-helper or journal change.

### C. Profile-root metadata or profile-specific state

If P1 establishes wrong metadata on the profile directory itself, the smallest prospective correction is a **Cooperator-owned, nonrecursive correction of that directory’s owner/group/mode**, after confirming it is the intended nonsymlink directory and the browser remains stopped.

Expected metadata is `kronika-capture:kronika-capture`, mode 0700. Do not recursively change permissions or ownership, inspect children, or infer that correcting root metadata fixes existing interior objects. [Runner unit:9–22](/home/agile/Projects/framenest/deploy/systemd/kronika-capture-runner.service:9)

If the remaining cause depends on opaque profile state, present these choices to the Cooperator:

| Decision | Consequence |
|---|---|
| Preserve the current profile and stop | Preserves all evidence and consumes no start. Further diagnosis requires an explicitly bounded evidence route. |
| Retain the old profile opaquely and create a fresh profile at the same canonical path | Avoids migrating uncertain profile contents. The old directory is retained; login remains Cooperator-owned. Successful startup would support profile dependence, not identify a particular stale artifact. |
| Cooperator performs an opaque restore from an explicitly selected backup | Preserves the selected historical profile state. It may also preserve the original problem. The exact backup source must be named before authorization. |

For the fresh-profile option, the proposed exact object movement is:

```text
Original:
  /var/lib/kronika-capture/profile

Retained opaque original:
  /var/lib/kronika-capture/profile.s3-pre-recovery

Fresh directory:
  /var/lib/kronika-capture/profile
  owner/group kronika-capture:kronika-capture; mode 0700

Rollback retention for the failed replacement:
  /var/lib/kronika-capture/profile.s3-failed-candidate
```

All destinations must be absent, including symlinks. **Only the Cooperator performs the whole-directory rename/create/restore operations.** No agent copies, lists or reads either profile. The external `profile.capture-launch` directory and timestamp remain at their original path, so changing the profile does not manufacture a new launch budget. The state root, journal, staging, account and token are not recreated.

Rollback, with the browser stopped: retain the replacement under the exact failed-candidate name and restore the original whole directory. Do not delete either profile or automatically restart.

The accepted owner explicitly controls opaque profile backup/restore and decisions about a problematic profile. A fresh-profile choice requires his explicit prospective decision; never treat “never logged in” as authorization. [Accepted plan:218–229](/home/agile/meta/projects/kronika/00/02-kronika-one-product/01_plan_sk.md:218), [AGENTS.md:254–265](/home/agile/Projects/framenest/AGENTS.md:254)

No runtime source change is required for this branch. Any durable runbook update belongs only in `docs/UBUNTU_NUC_DEPLOYMENT.md`. Synthetic tests cannot certify the opaque operation; retain the existing lifecycle, brake and journal tests and require the separately authorized host result.

### D. Invocation/configuration drift

For drift from the already accepted configuration, restore only the established mismatching object through a separate exact-object host grant:

- Runner unit: install the exact accepted release’s unit source; reload systemd without starting it.
- Executable configuration: restore only the verified `KRONIKA_CHROMIUM_PATH` entry to the accepted absolute path, provided that binary’s identity and provenance remain established.

Do not change the profile path, token delivery, working directory, account or launch arguments opportunistically. If the accepted binary target is itself missing or different, stop; do not replace the executable or retarget its symlink from this plan.

Repository changes are unnecessary when restoring host drift to the accepted source. A source-level launcher defect would require a concrete finding before authorizing changes to `src/kronika_capture/cli.py` or the driver. Existing launcher tests already cover explicit executable configuration and argument construction. [cli.py:263–324](/home/agile/Projects/framenest/src/kronika_capture/cli.py:263), [service contract tests:247](/home/agile/Projects/framenest/tests/contract/test_kronika_capture_services.py:247)

### E. Security-policy, filesystem-specific or binary-specific failure

No safe exact patch is selected by the current evidence.

- A synthetic permission failure is not proof that AppArmor caused Chromium’s refusal.
- A distro userns profile being present does not prove it covers this executable.
- A generic ProcessSingleton message does not establish a Chromium regression.

The next correction grant for one of these causes must first bind the failed operation, relevant policy or filesystem evidence, and—where necessary—the matching Chromium source/build provenance. No guessed AppArmor policy, mount change, downgrade, upgrade, binary substitution, `--no-sandbox` or namespace disabling is included.

This is a deliberate stop branch. Inventing an exact patch here would exceed the evidence.

### Declared validation route for a selected repository correction

A later implementation grant must bind the baseline literally. From the repository root:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/unit/chatgpt_page/test_capture_journal.py -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

Run release source/docs/remote contracts additionally when the selected change affects their contract. No new test toolchain, ambient Python route or broad suite by default. [Declared execution owner](/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md:44), [JavaScript route](/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md:307)

The existing zero-job recovery test already demonstrates that readiness alone cannot clear the pause: matching null-job resume and fresh acknowledgement are required. Preserve and rerun it; do not add a duplicate or change journal behavior. [test_capture_journal.py:276–310](/home/agile/Projects/framenest/tests/unit/chatgpt_page/test_capture_journal.py:276)

## 4. Acceptance, publication and ordered host recovery

### Acceptance and publication

Freeze the selected candidate commit, tree and changed-path list. Runtime changes require full-fresh independent acceptance, including privacy, startup count, brake, cleanup, journal recovery and fresh activation identities. The implementer cannot self-certify that acceptance.

The inspected evidence establishes two separate publication surfaces:

1. **Git publication:** a separate explicit grant, fast-forward of accepted `main`, one non-force `refs/heads/main:refs/heads/main` push, and direct public readback. This is the recorded established route. [17_report_00.md:59–100](/home/agile/meta/projects/kronika/00/02-kronika-one-product/17_report_00.md:59)
2. **Immutable release publication/deployment:** exclusively `deploy/ubuntu/framenest-release`. [AGENTS.md:68–104](/home/agile/Projects/framenest/AGENTS.md:68)

No separate Git-publication helper was identified in the inspected repository sources. Therefore this report does not invent one. If “publication through the canonical helper” means a distinct Git helper, its exact identity remains missing and must be bound before the publication grant. The release helper is not a substitute for Git publication.

For a selected, accepted and publicly verified correction SHA, the deployment grant must substitute its literal value for `<CORRECTION_SHA>`:

```text
deploy/ubuntu/framenest-release status
deploy/ubuntu/framenest-release check --release <CORRECTION_SHA>
deploy/ubuntu/framenest-release deploy --release <CORRECTION_SHA> --yes
```

A check does not authorize deploy. Do not patch installed release contents. A unit change additionally needs explicitly authorized installation of the unit from that immutable release and `daemon-reload`; web deployment alone does not establish the installed capture-unit version. [Deployment contract:455–519](/home/agile/Projects/framenest/docs/UBUNTU_NUC_DEPLOYMENT.md:455)

### Ordered host sequence after a selected correction

1. **Refresh preconditions.** Require the accepted/public/deployed SHA and manifest, runner stopped, no browser, unchanged intended Xvfb/bridge state, no recovery override and no active competing operation. Use supported authenticated status under the later host grant to require zero active/total jobs and `active_job=null`; never inspect the token value.

2. **Apply only the selected correction.** Install the accepted unit/configuration correction or receive the Cooperator’s completed opaque profile operation. Record its exact disposition. Do not combine speculative TMPDIR, profile and binary changes in one attempt.

3. **Check the external brake.** Use the accepted metadata-only D2 procedure. Require valid metadata, expired 300-second interval and no external launch lock. An unexpected lock stops this grant; no inherited permission to remove it. Never test profile-internal locks. [Accepted D2 and brake boundary](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:384)

4. **One corrected bootstrap start.** Under a new explicit budget, use the accepted D3 mechanism: the exact temporary `90-s3-recovery.conf` changes only `ExecStart` to the accepted release, retaining the unit account, credential wiring, display and sandbox. Start the actual runner exactly once. The new grant must bind the selected correction and literal SHA. [D3 command and cleanup](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:477)

5. **Classify within 180 seconds.** Observe only bounded C1 records, operational process metadata, loopback-listener classification and supported authenticated status. A startup failure ends the attempt. No raw stderr, second diagnostic launch or alternative-profile launch follows.

6. **Cooperator login and view.** On successful startup, retain that browser. The Cooperator alone opens the existing loopback view/tunnel, handles login/challenges and closes the view. Agents do not observe or operate the login screen. [View boundary](/home/agile/Projects/framenest/docs/UBUNTU_NUC_DEPLOYMENT.md:180)

7. **Explicit null-job recovery.** Read the current intervention identity; issue one supported `bridge resume --intervention-id <CURRENT_ID>` without `--job-id`. Require `readiness_pending`, followed within the accepted bounded wait by matching fresh readiness and cleared intervention. Do not reset the journal or repeat resume to force progress. [Accepted H3](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:601)

8. **One planned activation restart.** After the brake expires, remove only the bootstrap override and reload systemd while retaining the browser until activation. Then:

   ```text
   deploy/ubuntu/framenest-release status
   deploy/ubuntu/framenest-release check --release <CORRECTION_SHA>
   deploy/ubuntu/framenest-release activate-capture --release <CORRECTION_SHA> --yes
   ```

   Preserve manifest, work and brake gates. Require both fresh runner and browser-session identities. Terminal readiness or timeout stops without another restart. The helper retains the actual pointer outcome on failure. [Activation implementation:1694–1776](/home/agile/Projects/framenest/deploy/ubuntu/framenest_release.py:1694), [fresh-identity tests:536–612](/home/agile/Projects/framenest/tests/contract/test_kronika_capture_services.py:536)

9. **Verify stability, then one synthetic ask.** Require one browser root, fresh connected readiness, expected release identities, no override, loopback-only capture/CDP, closed view ports and unchanged privacy metadata. Repeat readiness/process identity after 30 seconds. Execute the accepted H6 ask once; require successful terminal submission without resend or browser replacement. [Accepted H5–H6](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:658)

The budgets are distinct:

```text
Original diagnostic start: already spent; remaining 0
P0/P1 evidence grant: browser starts 0
Selected corrected bootstrap: maximum 1, separately authorized
Later successful-recovery activation: maximum 1 planned restart
Synthetic ask: maximum 1, separately authorized
Automatic retry or rollback launch: 0
```

### Failure and rollback

Before capture activation, failure cleanup stops the runner, confirms browser termination, removes only the recovery override and reloads systemd. Preserve the profile, external brake timestamp, journal, credentials and release pointers.

For a unit correction, restore only the previously verified unit source if rollback is authorized; do not start it. Retain a newly created runtime temporary directory if its contents cannot lawfully be classified—never recursively clean Chromium-created state.

For a profile correction, rollback is the Cooperator’s stopped-browser whole-directory operation described above.

After activation has moved the capture pointer, preserve and report the actual result. `rollback-capture` itself restarts the runner; it requires its own grant, gates and launch budget. Do not use it automatically as cleanup. [Deployment failure behavior](/home/agile/Projects/framenest/docs/UBUNTU_NUC_DEPLOYMENT.md:187)

No branch resets the journal, edits SQL, recreates the state root, changes model/reasoning behavior, weakens Host/Origin/token checks, disables sandboxing or introduces automatic restart.

## 5. Exactly one recommended next grant

**Recommend a fresh bounded evidence grant implementing P0 and the Cooperator-executed P1 only.** A profile decision is not yet required to obtain that evidence. The report from that grant must stop before selecting or applying a correction.

```text
Proposed identity and route:
Persistent role: WORKER
Logical whole: inherited from this report's header
Next session/exchange: 20 / 01, subject to Orchestrator allocation verification
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S3-SINGLETON-PREREQUISITE-PROBE
Delivery route: manual Cooperator delivery
Independence required: no
Reasoning recommendation: High
Named risk: privileged synthetic filesystem evidence must not become
profile inspection, sandbox relaxation or another browser launch.

Exact baseline:
Root /home/agile/Projects/framenest
Branch feat/kronika-one-product
HEAD e408bb5503f359ec24542304ac1a621c6b9e4ffb
Parent d63d0b725acedf49d1611224c3b5201a90e7ef90
Tree dadc01726a354c319374832bfd385be0bdffb516
AP pin 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Clean index and worktree; local main and origin/main equal HEAD.
No claim of fresh public-ref observation is required for this probe.

Positive authority:
- Read the governing Worker/AP/project instructions and this accepted report.
- Verify the exact local baseline using read-only Git commands.
- Execute P0, individually and sequentially, through the named SSH gate.
- Receive and classify the Cooperator's one P1 execution.
- Inspect only the explicitly named service/process metadata and P1 targets.
- Create synthetic state only through the Cooperator's exact P1 block.
- Perform P1's exact owned-object cleanup.
- Release Worker remote privilege through the gate with sudo -K.
- Deliver one complete terminal report in the current session.

Exact mutation allowlist:
- Transient service kronika-s3-singleton-probe.service.
- The three P1 synthetic roots and their fixed file/link/socket children.
- No repository or product-state mutation.

Negative authority:
No browser executable invocation, including --version.
No browser start, restart, alternate profile, login, view or real ask.
No profile contents or internal-lock read/test/removal/copy.
No token, credential, Xauthority-content or journal access.
No account, AppArmor, namespace, mount or production-unit changes.
No product release-pointer mutation.
No repository edit, stage, commit, push, fetch or publication.
No package manager, environment repair, new dependencies or subagents.
No raw Chromium stderr, unrestricted logs or private transport output.

Declared execution route:
Worker host commands: scripts/operator/network/framenest_nuc_worker_gate.fish.
Owner synthetic probe: exact # [NUC / bash] P1 block.
The owner block is not an alternate Worker Python/SSH route.
Local Python, if separately required later: baseline-bound
./.ap/ap project check and ./.ap/ap exec.
JavaScript tests, if separately required later: node --test.
This evidence grant selects no local product tests or builds.

Staging and commit rules:
None authorized. No report file write or Meta Git operation.

Budget:
One P0 sequence, one P1 invocation, zero browser starts.
No retry with changed restrictions or another temporary location.

Stop conditions:
Baseline mismatch; failed capability/privilege; unexpected activity;
unit/configuration mismatch; existing probe state; unsupported probe route;
possible sensitive output; timeout; incomplete output; cleanup failure.
After a stop, only independently authorized cleanup, privilege release
and reporting remain. No correction follows.

Report contract:
Begin with the standard Worker report header and assigned coordinates.
Report PASS/PARTIAL/BLOCKED for the actual evidence task.
Phase-qualified result: not-applicable.
Logical-whole closure: not-closed.
Report justification: new-evidence.
Separate Worker-observed P0 from Cooperator-relayed P1.
Include every primitive's stage/result/errno classification, preflight
booleans, first failure, cleanup outcome, privilege-release outcome,
unchanged repository evidence and remaining causal limits.
Do not claim Chromium startup or S3 completion.
Terminal report expires the grant.

Trace and delivery:
External trace: configured, private, historical-evidence-only.
Project key: kronika.
Logical-whole projection: 02-kronika-one-product.
Existing trace destination:
  /home/agile/meta/projects/kronika/00/02-kronika-one-product
Proposed archival names:
  20_preflight_00.md
  20_report_00.md
Prompt author: ORCHESTRATOR.
Report author: assigned WORKER.
Delivery: complete session Markdown; no Worker persistence.
Optional later persistence and Meta Git archival: COOPERATOR.
Archival: wait-for-report.
Trace self-granted authority: none.
```

The proposed ordinal must be checked against actual allocation; it is not permission to reuse an occupied coordinate. The trace remains evidence rather than authority. [.ap/AP.md, RF-19:393–469](/home/agile/Projects/framenest/.ap/AP.md:393)

### Limits, deviations and terminal record

- This session verified source and local Git state only. It executed no tests, interpreter, host probe, browser or network request.
- Current user direction supersedes the attachment’s file-delivery instructions. No report file, readback receipt or file SHA-256 is claimed.
- Targeted publication-trace inspection was used to resolve the established Git route; it supplies historical evidence only.
- The original wording, failing syscall/path, attempt-correlated policy evidence, profile-internal state and matching Chromium implementation remain unknown.
- Synthetic success does not establish host Chromium startup. No S3 completion, acceptance, publication, deployment or logical-whole closure is claimed. The accepted S3 completion requirements remain outstanding. [Accepted closeout:707–726](/home/agile/meta/projects/kronika/00/02-kronika-one-product/15_report_00.md:707)

```text
Orchestration critique:
MEASURED: At the verified baseline, two materially different startup
wordings map to profile_in_use, and only the first recognized class survives.
Evidence: driver.mjs:339-379.
Effect: the recorded class cannot select a live-holder, stale-profile or
singleton-creation correction.
Smallest correction: preserve bounded wording detail if a separately
accepted correction receives an explicitly budgeted browser start.

LEAD: General temporary storage may be unavailable under the runner's
filesystem restrictions.
Evidence: runner unit:23-26; original Chromium operation remains unknown.
Cheapest useful check: P0/P1, with zero browser starts and no profile entry.

Resolved Execution Issues / Near-Misses:
Oversized read output was narrowed to targeted excerpts.
Unsuccessful optional documentation lookups were resolved through existing
repository and trace locations.
A broader operator-document excerpt included repository-documented host
labels; those labels are omitted from this report. No host contact followed.

Pre-existing Failure Classification:
Orchestrator-relayed host Chromium startup failure:
E_BROWSER_UNAVAILABLE, endpoint/process_exited, exit 21,
profile_in_use, no endpoint, no cleanup failure.
Established-static diagnostic conflation at the verified baseline.
Underlying host cause: unresolved.

Authority expiry:
Submission of this terminal report expires this planning authority.
No implementation, host action, additional planning cycle or autonomous
continuation follows. Execution requires a new complete Orchestrator grant.
```
