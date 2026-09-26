# Kronika one product — S3 Singleton prerequisite evidence probe (P0 Worker, P1 Cooperator)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 20
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S3-SINGLETON-PREREQUISITE-PROBE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: privileged synthetic filesystem evidence must not become profile inspection, sandbox relaxation or another browser launch; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository baseline from Step 0 before acting.
Repository reading is read-only. The only allowed write is the terminal report
at its exact destination when absent. No subagents.

## Accepted plan this grant implements

`19_report_00.md` (Planner report, status PARTIAL, accepted by the
Orchestrator as the basis for this bounded evidence step) proposes exactly one
next grant: P0 (read-only service/process preflight by a fresh Worker through
the project SSH gate) plus P1 (one Cooperator-executed synthetic
filesystem/socket probe under the runner's copied restrictions), both with
zero browser starts. This grant is that evidence grant. It selects and applies
no correction and does not decide between candidate causes.

## Verified starting state (read-only, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (parent
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`); clean; local `main` =
  `origin/main`; AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink
  and `.ap` HEAD).
- Host state after the D3c cleanup (Orchestrator-relayed classified evidence):
  runner `inactive`; Xvfb and bridge `active`; web pointer `e408bb5…`;
  capture pointer `94e605c…`; no Chromium process; no recovery override;
  external brake directory present, `lock` absent, metadata valid, interval
  expired.
- The classified startup record this probe follows up (verbatim):

```text
[headless] capture_startup {"outcome":"failed","code":"E_BROWSER_UNAVAILABLE","stage":"endpoint","reason":"process_exited","spawn_errno":null,"exit_code":21,"signal":null,"endpoint_seen":false,"endpoint_budget_exhausted":false,"stderr_classification":"profile_in_use","cleanup_failed":false}
```

- `private/**` is never read. Never print or read the token value. Never
  inspect browser profile contents or profile-internal locks.

## Goal

Execute P0 and the single Cooperator-executed P1 exactly as specified in
`19_report_00.md` §2, classify their outputs against the plan's decision
table, and report. Zero browser starts. Stop before selecting or applying any
correction.

## Step 0 — preconditions (fail closed)

Check only names, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

If any is unset, stop `BLOCKED` (names only). Then:

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready` and exits 0.
- Repository gate: independently verify the physical root, branch, HEAD,
  parent, tree, clean index and worktree, local `main` = `origin/main` =
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, and the AP pin `7478ddb0…`
  (gitlink and `.ap` HEAD). Classify any divergence with the five RF-12
  recovery classes; stop on unexplained remainder.
- The Cooperator established the NUC privilege timestamp before dispatch,
  outside this Worker. Use `sudo -n` only. Never run `sudo -v` or `sudo -K`;
  never handle or print a password.

## P0 — read-only service and process preflight (Worker, through the gate)

Run these individually and sequentially, classifying each result before the
next. All commands through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`,
one bounded command per invocation, no shell metacharacters.

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
- `pgrep` output `0` with exit 1 is the expected no-match result. Exit greater
  than 1 is a probe failure.
- Process names and PIDs are operational metadata. Never request command
  lines, environment, open files, browser tabs or socket endpoints.
- Compare the unit restrictions with the baseline source
  `deploy/systemd/kronika-capture-runner.service` at `e408bb5…`.
- Unexpected activity, configuration drift, any possible capture browser
  process, unavailable privilege or incomplete output stops P1.
- No service is stopped or repaired under P0. Do not call product status; this
  probe does not access the token or journal.

## P1 — one Cooperator-executed synthetic probe (after P0 passes)

P1 is executed by the Cooperator in his open NUC Bash session, never by you
and never through the gate. After P0 passes, emit the exact block below in the
chat with the Cooperator, in Slovak, preceded by its one-line purpose and
followed by explicit instructions to paste the complete output and to stop if
any marker or `probe_transport=` line is missing. One block in flight; wait
for the complete output before classifying. If the interface collapses or the
paste is detectably corrupted before anything ran, re-emit the block exactly
once; if it partially ran, stop and report.

Purpose for the Cooperator: overí základné filesystem/socket primitívy
(vytvorenie adresára, súboru, symlinku a Unix socketu) pod účtom a
obmedzeniami runnera v troch syntetických umiestneniach; číta iba metadáta
koreňa profilu, nikdy nie jeho obsah ani interné zámky; nespúšťa Chromium.

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

P1 operational constraints (from the accepted plan):

- Run once. Unsupported systemd options, source mismatch or nonstandard
  configuration stop the probe; do not simplify the sandbox to obtain a
  result.
- Do not race another operator changing the services. P0 must be classified
  before P1.
- A refusal such as `EROFS` is useful probe evidence, not a successful
  browser diagnosis. `probe_transport=completed` means the script completed.
- Normal cleanup removes only objects created by this invocation, in reverse
  order, without recursion. Never recursive or wildcard deletion.
- On timeout, interrupted transport or cleanup failure: stop; report the exact
  synthetic root labels potentially retained. Cooperator-owned recovery must
  confirm the transient service is stopped and ownership of any leftover
  exact objects before cleanup.
- P1 never reads the token, Xauthority contents, journal, profile contents or
  profile-internal locks. It never runs Chromium, including `--version`.
- Profile-root metadata (existence, owner/group, mode, access) is the only
  profile-related observation permitted.

## Classification after P0/P1

Apply the accepted plan's decision table (`19_report_00.md` §2):

| Result | Established conclusion | Permitted recommendation |
|---|---|---|
| Profile-root ownership/mode/access fails | A necessary profile-root prerequisite is wrong now. | Cooperator-owned root-metadata correction or explicit profile decision; no recursive repair. |
| Synthetic state/runtime operations succeed; `/tmp` returns `EROFS` | Those filesystem primitives work in the approved writable locations; general `/tmp` creation fails under the reproduced restrictions. | Temporary storage remains a supported candidate. Do not select C3; the original Chromium operation/path remains unproven. |
| Symlink or socket operation fails in a writable synthetic root | A corresponding primitive is unavailable in this probe context. | Classify the exact operation and errno; stop before guessing filesystem, mount or policy changes. |
| All primitives succeed | The tested general prerequisites work. | Profile-specific state and Chromium-specific behavior remain unresolved; a profile decision or separately authorized version-specific evidence is required. |
| Configuration/binary comparison differs | Present configuration differs from the baseline. | Stop with boolean mismatch evidence; do not print arbitrary values or repair automatically. |
| Unexpected process or service activity | The stopped-browser precondition is unavailable. | Stop without killing processes or testing locks. |

There is no permitted read-only agent probe that conclusively identifies stale
profile-internal artifacts under the stated boundary. Do not disguise a
profile clone, alternate-profile browser start, `strace` launch or another
diagnostic start as a synthetic probe.

## Authority and containment

Positive authority: read-only repository inspection for Step 0; P0 through
the named worker gate; emitting the exact P1 block once to the Cooperator and
classifying its complete returned output; the terminal report write at the
exact destination below when absent; full readback of the saved report.

Exact mutation allowlist: none in the repository; the transient service
`kronika-s3-singleton-probe.service`, the three P1 synthetic roots and their
fixed `file`/`link`/`socket` children; P1's exact owned-object cleanup.

Negative authority: no browser executable invocation, including `--version`;
no browser start, restart, alternate profile, login, view or ask; no profile
contents or internal-lock read/test/removal/copy; no token, credential,
Xauthority-content or journal access; no account, AppArmor, namespace, mount,
service or production-unit change; no product release-pointer mutation; no
repository edit, stage, commit, push or publication beyond the report; no
dependency or package-manager change; no `sudo -v` or `sudo -K`; no
`private/**`; no subagents; no raw Chromium stderr, unrestricted logs or
private transport output. Do not print hostnames, private network values,
tokens or sockets.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; a
repository-gate mismatch; unexpected service/process activity; unit or
configuration mismatch; existing probe state; unsupported probe route; any
possible sensitive output; timeout; incomplete output; cleanup failure.
Preserve the first causal failure; do not retry with changed restrictions or
another temporary location; do not simplify the sandbox.

## Validation

Validation ladder: selected.
Inspection and provenance: required — repository gate, unit restrictions
compared against the baseline source, P0 metadata.
Existing focused tests: none — no repository change.
Affected tests: none.
New causal regression: none — evidence probe only; synthetic tests cannot
close the host question.
Broad or full suite: not-used.
Runtime or testbed: the accepted P1 transient service under the runner's
copied restrictions.
Independent acceptance: not-required — evidence only, no candidate.

## Completion and report contract

`PASS` means Step 0 passed, P0 completed with the expected states, the single
P1 invocation completed (`probe_transport=completed`) with all primitives
classified and cleanup reported, and the report is delivered. `PARTIAL` when
useful evidence exists but a material prerequisite, refusal or cleanup detail
remains open. `BLOCKED` when the evidence task cannot proceed. Use
`Phase-qualified result: not-applicable` and
`Logical-whole closure: not-closed`. `Report justification: new-evidence`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; Step 0
results; every P0 result with exact values; the P1 preflight booleans, each
primitive's stage/result/errno and cleanup outcome; `probe_transport` result;
the plan's decision-table classification; deviations, risks and missing
evidence; exact first causal error on any stop; one smallest next step; the
unchanged repository evidence; the authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Do not claim Chromium startup, correction selection or S3 completion. A
refusal inside a synthetic root is probe evidence, not a product failure.
Separate Worker-observed P0 from Cooperator-relayed P1.

The formal report is in English; the short completion notice to the
Cooperator is in Slovak, masculine address. Finalize the report, save it at
the exact destination, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Do not run `sudo -K`; the Cooperator releases
the privilege timestamp manually. Terminal report or cancellation expires
this authority.

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
Downloadable prompt filename: 20_preflight_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 20_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
