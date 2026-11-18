### Report for ORCHESTRATOR_CHAT

**Logical whole identity:** `nuc-security-hardening`  
**Worker session ordinal:** `01`  
**Worker exchange ordinal:** `01`  
**Task:** `NSH-PLAN-01`  
**Status:** `PARTIAL`  
**Phase-qualified result:** `not-applicable`  
**Logical-whole closure:** `not-closed`  
**Report justification:** `new-evidence`

**Start and end commit:** `8c58a81234a97fdf5af9d724a3b526f19745d32a`  
**AP pin:** `73e20ef80b88700d5fcbc397cd8edd4fc425869f`

No files were written. No Git mutation, host contact, privileged operation, browser action, provider call, publication, deployment, or acceptance was performed.

The implementation sequence is outlined below, but it is **not execution-ready**. Exact host versions, several operational decisions, and the disposition of newly identified runtime/dependency risks remain unresolved. Issuing a complete implementation specification before resolving those gates would contradict the task’s stopping conditions.

## 1. Executive summary and scope

Prioritize the active boundary: establish installed versions, assess the newly disclosed Tailscale Serve issues, disable unnecessary printing and parked capture services, apply reviewed security updates, and then harden service and SSH/firewall configuration through separate grants.

Three Cooperator choices were obtained during this exchange:

- Gracefully stop and disable parked capture services.
- Disable SSH forwarding.
- Disable CUPS and its activation surfaces while retaining packages.

These are planning decisions, not host execution authority.

Important corrections to the initial findings:

- The repository web and backup units **omit** address-family and syscall filters. The observed `~` values are not erroneous literal directives in those sources.
- Socket `0600` protection already exists in application code. The host socket remains unobserved.
- Routine release refresh deliberately **does not install systemd units**. Changed unit sources require a separate owner-executed installation and restart.
- A successful SSH command can reuse a multiplexed connection. Lockout prevention must prove fresh authentication with multiplexing disabled.
- Ubuntu package updates alone cannot resolve vulnerabilities in bundled Python wheels or the frozen standalone runtime.

Preserve all ADR-0085 frozen objects, the deferred publication-media path, local-first operation, Tailscale-only access, existing catalog backup behavior, and disabled Research. Route-recovery implementation, bespoke Kronika AppArmor policy, provider provisioning, capture activation, private media access, and internet publication remain outside this whole.

No application API, database schema, public type, or migration change is proposed.

## 2. Exact site inventory

Evidence labels: **verified** means repository evidence inspected in this exchange; **Cooperator-observed** means the supplied sanitized host inventory; **inferred** means a conclusion requiring confirmation; **unknown** means not established.

### Repository sites — verified

All **16** artifacts under `deploy/systemd/` were enumerated and read:

| Group | Exact artifact names |
|---|---|
| Web | `kronika.service`, `kronika.env.example` |
| Local backup | `kronika-catalog-backup.service`, `kronika-catalog-backup.timer` |
| Optional off-device backup | `kronika-catalog-offdevice.service`, `kronika-catalog-offdevice.timer` |
| Capture | `kronika-capture-bridge.service`, `kronika-capture-runner.service`, `kronika-capture-xvfb.service`, `kronika-capture-vnc.service`, `kronika-capture-view.service`, `kronika-capture.env.example` |
| Existing AI credential templates | `kronika-ai-credential-nvidia-nim.conf`, `kronika-ai-credential-opencode-go.conf`, `kronika-ai-credential-vercel-ai-gateway.conf` |
| Research credential template | `kronika-research-credential.conf` |

Other material sites:

| Site | Evidence and consequence |
|---|---|
| [Web unit](/home/agile/Projects/kronika/deploy/systemd/kronika.service:22) and [backup unit](/home/agile/Projects/kronika/deploy/systemd/kronika-catalog-backup.service:21) | Existing sandboxing; neither contains an address-family or syscall filter. |
| `deploy/ubuntu/kronika-release`, `deploy/ubuntu/kronika_release.py` | Sole routine release helper; fixed tooling, provenance, backup and public-main gates. |
| [Release remote contracts](/home/agile/Projects/kronika/tests/contract/test_nuc_release_remote_contract.py:1595) | Deploy/rollback must not install units, reload systemd, or start/stop capture. |
| [Socket protection](/home/agile/Projects/kronika/src/kronika/server.py:25) | Service-owned socket, `0600`, fail-closed verification before serving requests. |
| `deploy/ubuntu/production_ai_deploy.py` | Source machinery for `20-ai-credential.conf`; credential provisioning must not run here. |
| `scripts/operator/network/kronika_nuc_worker_gate.fish:450–466` | Canonical future Worker transport; no explicit multiplexing disablement. |
| `src/kronika_capture/cli.py:23–32,279–294` | Node resolved through process PATH; Chromium configured as an absolute executable. Template paths do not prove host provenance. |
| `pyproject.toml`, `poetry.lock` | Seven direct production dependencies; lock contains 31 packages, including 23 main-group entries and eight dev-only entries. Platform markers still govern installation. |
| `src/kronika/infrastructure/media_analysis/still_image.py:69–72` | Unrestricted image opening/loading precedes expected-format comparison. Relevant to Pillow advisory triage. |
| `src/kronika/infrastructure/media_validation/ffprobe.py:198–235` | Upload signature gate narrows accepted inputs before image decoding; do not ignore that control. |

Relevant existing tests:

- `tests/contract/test_fedora_systemd_service.py`
- `tests/contract/test_catalog_backup_timer.py`
- `tests/contract/test_catalog_offdevice_timer.py`
- `tests/contract/test_kronika_capture_services.py`
- `tests/contract/test_nuc_release_docs.py`
- `tests/contract/test_nuc_release_source_contract.py`
- `tests/contract/test_nuc_release_remote_contract.py`
- `tests/contract/test_nuc_operator_runbook.py`
- `tests/contract/test_operator_network_scripts.py`
- `tests/contract/test_tailscale_ingress_security.py`
- `tests/contract/test_kronika_identity_retention.py`
- `tests/unit/infrastructure/runtime/test_production_runtime.py`
- `tests/unit/infrastructure/runtime/test_production_health.py`

Governing documentation inspected across this Worker run: deployment and clean-install runbooks, backup/recovery, operator network, frozen NUC baseline, Worker execution contract, ROADMAP, SECURITY, SERVER, and ADRs 0032, 0052, 0058, 0075 and 0085.

The retention ledger actually protects **86 documents**—ADRs through 0084 and the two historical host documents—and **36 Alembic files**. All recorded hashes matched. ADR-0085 is additionally protected by the task’s explicit prohibition.

### Host sites

| Surface | Classification and supplied state |
|---|---|
| UFW and interfaces | **Cooperator-observed:** active deny-incoming policy; one stale wired-only LAN SSH allowance; wired interface down; Wi-Fi in use. Complete effective netfilter interaction remains **unknown**. |
| OpenSSH | **Cooperator-observed:** wildcard port 22; key-only/root-denied effective policy; local forwarding permitted; no user/group allowlist. |
| SSH drop-ins | **Cooperator-observed:** `00-kronika-hardening.conf` and `50-cloud-init.conf`; latter contains an overridden password-authentication allowance. |
| Web/backup units | **Cooperator-observed:** application active, backup timer active; effective protections and missing settings as supplied. Exact installed fragment/drop-in paths require readback. |
| Web drop-ins | **Cooperator-observed:** `20-ai-credential.conf`, `30-publication-write-path.conf`, `40-runtime-directory-mode.conf`, `kronika-research-credential.conf`. No checked-in source was found for the exact `30-` and `40-` filenames. |
| Capture | **Cooperator-observed:** bridge, runner and Xvfb active/enabled; view/VNC inactive/static. Profile and browser state are excluded. |
| CUPS | **Cooperator-observed:** wildcard TCP 631. Actual peer reachability is **inferred**, not measured. |
| Accounts | **Cooperator-observed:** service accounts nologin and non-sudo; root alone has UID zero. Complete authorized interactive-account set is **unknown**. |
| Application modes | **Cooperator-observed:** env `0640`; credentials directory `0700`, files `0600`; application state `0700`; cache `0755`; runtime `0750`; source-media parent `2750`. |
| Unix socket | **Unknown:** privileged metadata was not obtained. Failed unprivileged traversal does not establish absence. |
| Tailscale | **Cooperator-observed:** tailnet-only HTTPS Serve to the canonical Unix socket; no Funnel, selected exit node, or table-52 default route. Installed version, embedded SSH setting and configuration privileges are **unknown**. |
| AppArmor | **Cooperator-observed:** enabled; 63 enforcing and four Transmission complain profiles. Package ownership, executable presence and current profile attachment are **unknown**. |
| Patch state | **Cooperator-observed:** 59 upgradable packages, reboot marker, kernel ABI `6.8.0-146-generic`, unattended upgrades enabled. Exact package revisions and current candidates are **unknown**. |
| Off-device backup | **Cooperator-observed:** not installed. This optional layer is unprovisioned, not broken. |

## 3. Findings classification

These are planning classifications, not independent audit certification or exploit findings.

| ID | Classification | Evidence, affected site and disposition |
|---|---|---|
| F1 | **Gap / latent policy defect** | Stale wired LAN SSH allowance. Remove its exact privately identified rule; preserve Tailscale behavior and UFW defaults. |
| F2 | **Cooperator decision** | SSH allowlist and limits are policy choices. Forwarding prohibition is now selected; operator allowlist remains unresolved. |
| F3 | **Latent configuration defect** | `50-cloud-init.conf` permits password authentication if the earlier protection disappears. Neutralize fallback and verify effective `Match` contexts. |
| F4 | **Gap** | Repository units omit real filters. Do not claim a malformed source directive exists. |
| F5 | **Gap** | Additional sandbox protections need workload-specific compatibility proof. A lower exposure score is insufficient acceptance. |
| F6 | **Exposure gap** | Unnecessary wildcard CUPS listener. Selected disposition: disable service and activation surfaces; retain packages. |
| F7 | **Decision resolved for planning** | Selected disposition: gracefully stop/disable parked capture. Preserve all profile/state data; no activation rollback without renewed authority. |
| F8 | **Cache confidentiality gap; socket unknown** | Tighten cache parent mode. Observe socket before diagnosing it; application already enforces `0600`. |
| F9 | **Cooperator decision** | Four complain profiles alone do not prove an exposed application. Establish package/use/attachment before removal or enforcement. |
| F10 | **Maintenance gap** | Pending updates/reboot warrant review. Neither package count nor ABI alone proves vulnerability. |
| F11 | **Acceptable current ingress; separate recovery objective** | Preserve Serve-to-UDS boundary. Existing docs already explain ADR-0058’s limited recovery behavior. Route-repair implementation stays separate. |
| F12 | **Accepted exception requiring verification** | Preserve the deliberate publication write path. Verify effective sandbox paths without writing real media. |
| F13 | **Acceptable** | Optional off-device backup remains unprovisioned. |
| F14 | **Acceptable baseline to preserve** | Key-only SSH, root denial, service-account restrictions and existing secret/state/source-media modes. |

New advisory-driven concerns are recorded in section 8. No host vulnerability is classified as confirmed.

## 4. Ordered bounded grants and authority matrix

**One grant executes one row.** The following are proposed future boundaries; none is authorized by this report.

Proposed repository implementation allowlist:

- Existing web/backup units and their directly relevant contract tests.
- New `scripts/operator/security/kronika_nuc_boundary_rollback.sh`.
- New `tests/contract/test_nuc_hardening_rollback.py`.
- New `docs/NUC_SECURITY_HARDENING.md`.
- Relevant living deployment, network and status documentation, explicitly enumerated by the eventual grant.

Frozen documents, migrations, capture units, credential templates, release-helper behavior, `pyproject.toml` and `poetry.lock` are excluded from that implementation grant.

| Row | Dependency and exact boundary | Executor / privilege / interruption | Verification, rollback and independence |
|---|---|---|---|
| **00** | **First:** bounded version/effective-state inventory; commands in section 6. No changes. | Cooperator; privileged reads separately granted; no restart. | Sanitize evidence, reconcile installed versions and advisory applicability. Stop affected planning on missing facts. |
| 01 | Dispose outstanding decisions in section 10; resolve exact operator identity, maintenance window and residual risks. | Cooperator/Orchestrator; no mutation. | Written dispositions; no implied implementation authority. |
| 02 | Conditional Tailscale security update if row 00 establishes an affected version. Exact package/version and restart scope must be granted. | Cooperator/root; possible tailnet/Serve interruption; physical console required. | Restore connectivity/configuration continuity; no automatic downgrade to a vulnerable version. Independently recheck boundary. |
| 03 | Disable/mask only the installed CUPS service/socket/path activation surfaces identified in row 00. Retain packages. | Cooperator/root; printing interruption only. | No 631 listener or peer connection. Preserve previous enable/mask states for explicit restoration. |
| 04 | Gracefully stop/disable capture runner, bridge and Xvfb; keep view/VNC inactive. | Cooperator/root; capture interruption. | Inactive after reboot, no capture listener; no profile inspection. Restarting capture requires separate authority. |
| 05 | Reviewed Ubuntu security-package transaction; exact approved package/version list. Exclude frozen tooling, release upgrades and autoremove. | Cooperator/root; package scripts may restart daemons. | Review simulation first; preserve previous kernel and package transaction record. No blanket package downgrade rollback. |
| 06 | Explicit reboot after row 05 and completed backup checkpoint. | Cooperator/root; downtime and console recovery. | Running kernel, Wi-Fi, tailnet, SSH, Serve, application and timer checks. Boot retained kernel if needed. |
| 07 | Repository sandbox/recovery-tool/runbook implementation; selected settings in section 5. Exact branch and one local commit require explicit authority. | Worker; repository writes only; no host. | Baseline-bound tests and synthetic rollback tests. Preserve frozen bytes. Candidate evidence is non-independent. |
| 08 | Fresh independent review of row 07, including rollback safety and sandbox workload proof. | Fresh independent Worker; read-only. | Findings only. Corrections require a separate bounded grant and subsequent independent verification. |
| 09 | Publish the accepted exact candidate SHA to public `main`. | Separately authorized publisher; Git writes only. | Verify public SHA/content; no force push or deployment. |
| 10 | Canonical release-helper `status` and `check` for the authorized public SHA. | Authorized operator; host reads and helper’s local temporary artifacts. | Require all gates, including backup readiness. A check never authorizes deployment. |
| 11 | Routine immutable refresh through `deploy/ubuntu/kronika-release`. | Cooperator under explicit release authority; application restart. | Canonical health/provenance/backup checks and canonical rollback. No unit installation assumed. |
| 12 | Install approved web/backup unit material; preserve existing credential/publication drop-ins; set persistent cache/runtime modes; reload and restart only granted units. | Cooperator/root; bounded application interruption. | Validate units before activation, then service/synthetic workload checks. Restore exact previous unit bytes/modes and restart if needed. |
| 13 | Observe an **actual existing timer-triggered** backup pipeline after row 12. | Read-only verifier; normal scheduler performs existing work. | Backup, verification, disposable restore, semantic readback, readiness `ready`, no pending cleanup. Manual oneshot is insufficient. |
| 14 | Install the reviewed recovery helper as a physical root-owned file and prepare root-only recovery storage. | Cooperator/root; no network-policy change. | Verify ownership, hashes, symlink refusal and timer execution using harmless synthetic state. Remove only exact temporary test objects. |
| 15 | Remove the exact stale UFW wired rule; change no Tailscale netfilter mode or interface state. | Cooperator/root; own dead-man rollback. | Fresh tailnet SSH positive and Wi-Fi LAN SSH negative; restore exact UFW snapshot on failure. |
| 16 | SSH fallback correction, selected forwarding prohibition, approved allowlist and agreed limits. | Cooperator/root; validate then reload, not blind restart; own dead-man rollback. | Fresh authentication and effective `Match` policy; restore exact touched files on failure. |
| 17 | Conditional Transmission/AppArmor disposition after package/use/attachment evidence and owner decision. No bespoke Kronika profile. | Cooperator/root if mutation selected. | Validate only affected profiles/packages. Preserve exact profile bytes/modes; no global AppArmor disablement. |
| 18 | Fresh independent read-only host-boundary verification and advisory reconciliation. | Independent verifier under separately bounded host-read authority. | Per-finding verdicts; no corrections or acceptance on the corrector’s own evidence. |
| 19 | Reconcile living documentation with verified outcomes and explicit residual risks. | Worker; exact documentation allowlist and one commit. | No frozen-document edits or unsupported completion claims. |
| 20 | Publish accepted documentation commit. | Separately authorized publisher. | Public-main verification; no host action. |
| 21 | Canonical `status`/`check` for final public main. | Authorized operator. | Read-only gates; no automatic refresh. |
| 22 | Refresh NUC to that exact final public SHA. | Cooperator under explicit release authority. | Canonical helper and health/backup/provenance gates. |
| 23 | Cooperator rendered UI/companion acceptance and final post-refresh boundary observation. Synthetic fixtures only, separately authorized. | Cooperator; bounded application test effects; no provider calls. | Current public main must already be on NUC. Clean up exact synthetic objects; preserve Gallery/Details behavior. |

Rows 02–06 are independent of repository implementation once their own evidence and decisions pass. Firewall and SSH remain separate from each other, package maintenance, reboot and capture actions.

Dependency/runtime corrections discovered by the annex are **not silently added to row 07**. They need separate accepted-finding or tooling authority.

## 5. Proposed configuration and interfaces

These are bounded candidates for approval after row 00, not settings certified compatible with the host.

**Web and local backup:**

- Add `PrivateDevices=true`, `ProtectHostname=true`, `ProtectClock=true`, `ProtectKernelLogs=true`, `RestrictNamespaces=true`, `RestrictRealtime=true`, and `SystemCallArchitectures=native`.
- Set web `CacheDirectoryMode=0700` and `RuntimeDirectoryMode=0750`.
- Web address families: `AF_UNIX AF_INET AF_INET6`, preserving loopback and existing outbound capability.
- Backup candidate: `AF_UNIX`, `IPAddressDeny=any`, and inaccessible source media, subject to complete synthetic backup/restore proof.
- Stage a real syscall denylist separately within compatibility testing: `~@clock @module @mount @raw-io @reboot @swap`, with `SystemCallErrorNumber=EPERM`.

The denylist is an intentionally limited first cut, not an exhaustive syscall sandbox. The selected systemd version must support and resolve every group. Upstream documentation explains filter semantics and recommends combining filesystem protection with mount-syscall restrictions. [systemd 255 execution documentation](https://www.freedesktop.org/software/systemd/man/255/systemd.exec.html)

Defer web `MemoryDenyWriteExecute`, `PrivateUsers`, `RemoveIPC` and `ProcSubset=pid`. They need additional native-runtime, subprocess, shared-UID and `/proc` compatibility evidence. Do not apply global hardening to parked Chromium/X11 units.

**SSH candidate:**

- Preserve existing key-only authentication and root-login denial.
- Set `DisableForwarding yes`, consistent with the Cooperator’s selected policy.
- Neutralize the cloud-init password fallback without assuming that removing one drop-in controls future provisioning.
- Proposed limits: `MaxAuthTries 3`, `LoginGraceTime 30`, `ClientAliveInterval 300`, `ClientAliveCountMax 2`.
- `AllowUsers` requires the privately approved operator-account set.

Client-alive settings detect unresponsive clients; they must not be described as an inactivity logout policy.

**Recovery helper interface:**

The proposed helper exposes only fixed operations: snapshot, verify and restore for the enumerated `ufw` or `sshd` surface. It must reject arbitrary paths, symlinks, unexpected owners, stale cases and concurrent conflicting operations. Installation target:

`/usr/local/libexec/kronika/nsh-boundary-rollback`

Recovery state:

`/var/lib/kronika-host-hardening`

Both are root-controlled; recovery data is outside application-owned state. Privileged helper source must be reviewed and installed from accepted repository bytes, not pasted as a privileged chat script.

## 6. Proof design and exact command specifications

These commands specify **future grants**. They were not run against the NUC. The Orchestrator must issue owner commands one block at a time, with preconditions, complete returned output, exit status and sanitization. Private identities, network values and configuration output stay on the operator console.

### Row 00: first version inventory

```text
# [NUC / bash]
/usr/bin/cat /etc/os-release
/usr/bin/uname -r
/usr/bin/dpkg-query -W -f='${binary:Package}\t${Version}\t${db:Status-Abbrev}\n' systemd systemd-resolved openssh-server openssh-client cups cups-daemon cups-browsed apparmor apparmor-utils tailscale nodejs chromium-browser snapd unattended-upgrades libbrotli1 zlib1g
/usr/bin/dpkg-query -W -f='${binary:Package}\t${Version}\t${db:Status-Abbrev}\n' 'linux-image-*' 'linux-modules-*'
tailscale version
snap list chromium
/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13 --version
/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry --version
#------------------------------------------------------
```

Missing packages or commands must be recorded individually; they are not version zero or proof of safety. Do not install tools to finish this inventory.

Additional exact read-only probes, issued separately:

| Probe | Expected evidence |
|---|---|
| `dpkg-query -W nsh-impossible-package-837269` | Nonzero absence control; never hide it with `|| true`. |
| `readlink /opt/kronika/current` | Canonical immutable release target, privately verified against provenance marker. |
| `awk '/^(Name|Version): / { print }' /opt/kronika/current/.venv/lib/python3.13/site-packages/*.dist-info/METADATA` | Distribution metadata only, no imports. Validate canonical layout, nonempty membership and duplicates first; fail closed on denied access or unexpected layout. |
| `sudo -n /usr/sbin/sshd -t` | Exit zero before any SSH cut. |
| `sudo -n /usr/sbin/sshd -T` | Owner-local effective policy; return sanitized selected directives only. Repeat with privately supplied relevant `-C` contexts. |
| `sudo -n /usr/sbin/ufw status verbose` and `status numbered` | Exact stale rule and default policy established privately. |
| `sudo -n /usr/bin/stat -c '%a %U:%G %F' /run/kronika /run/kronika/kronika.sock /var/cache/kronika` | Runtime `0750`; service-owned socket `0600`; cache pre-state established. |
| `systemctl show kronika.service -p FragmentPath -p DropInPaths -p ReadWritePaths -p ReadOnlyPaths -p RuntimeDirectoryMode -p CacheDirectoryMode` | Actual unit provenance and bounded mutable paths; no environment dump. |
| `systemctl show cups.service cups.socket cups.path cups-browsed.service -p LoadState -p ActiveState -p UnitFileState -p Triggers -p TriggeredBy` | Installed printing activation surfaces identified before targeting them. |
| `sudo -n /usr/sbin/aa-status` | Current profile state, followed by narrowly scoped package/profile ownership evidence. |
| `systemctl show kronika-catalog-backup.timer -p ActiveState -p UnitFileState -p LastTriggerUSec -p NextElapseUSecRealtime` | Timer enabled/active with scheduling evidence. |
| `sudo -n -l -U kronika` and corresponding capture-account query | Expected sudo denial, classified as an intentional negative result. |
| `tailscale serve status --json`, `tailscale funnel status` | Owner-local inspection only; return canonical backend/mount-count/Funnel assertions, not raw private JSON. |

Embedded Tailscale SSH, operator capabilities and advertised/accepted routes require a narrowly selected, sanitized readback. Do not dump all preferences or personal configuration.

Actual capture Node/Chromium provenance remains a separate metadata gap. Do not launch Chromium or inspect browser process arguments, environment, profile or session data to resolve it.

### Network controls

Fresh Cooperator-owned SSH proof must explicitly disable connection reuse:

```text
# [MacBook / fish]
ssh -S none -o ControlMaster=no -o ControlPath=none -o BatchMode=yes -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -i "$KRONIKA_NUC_SSH_IDENTITY" "$KRONIKA_NUC_SSH_USER@$KRONIKA_NUC_SSH_TARGET" true
#------------------------------------------------------
```

Expected: a newly authenticated key-only connection exits zero. A pre-existing session or multiplexed command is insufficient.

For the negative LAN proof, use the privately verified **Wi-Fi LAN address**, not MagicDNS or a tailnet address:

`nc -G 5 -z <private-Wi-Fi-address> 22`

Expected: connection fails from a LAN peer whose ability to reach the intended LAN has been independently established. A timeout without a functioning positive control proves little.

Wired empirical testing cannot exist while the wired interface remains down. Record exact rule-removal evidence and mark wired reachability **not tested**; do not activate the interface to manufacture a result.

CUPS controls:

- `ss -H -lntu '( sport = :631 )'` must return no listener.
- The equivalent port-22 inspection must return the known SSH listener as a parser control.
- A targeted port-631 connection from an authorized tailnet peer must fail.
- Repeat after package maintenance and reboot.

### Application, backup and sandbox controls

- `systemd-analyze verify /etc/systemd/system/kronika.service /etc/systemd/system/kronika-catalog-backup.service`: no invalid or unsupported directives.
- `systemctl is-active kronika.service kronika-catalog-backup.timer`: both active.
- `sudo -n /usr/bin/curl --fail --silent --show-error --unix-socket /run/kronika/kronika.sock http://localhost/health`: healthy HTTP response.
- Generated-media ffmpeg/ffprobe, preview/cache writes, SQLite transactions and complete backup/restore pipeline must pass under the proposed sandbox.
- Use local stubs for outbound compatibility; no provider or acquisition call.
- Capture acceptance is now **inactive/disabled**, with ports 8765/5900/6080 absent and no unintended restart after reboot.
- Verify publication/source-media protection inside the service mount namespace or an equivalent synthetic sandbox. A host-shell `test -w` does not prove `ProtectSystem`.
- A privileged operation already denied by missing capabilities cannot demonstrate that a new syscall filter caused the denial. Label such evidence static; do not manufacture a dynamic proof.

Backup acceptance must correlate an actual timer activation with completed verification, disposable restore, semantic readback, readiness `ready`, and no pending cleanup. Preserve the existing `03:17 UTC` schedule and randomized delay.

### Release gates

```text
# [MacBook / fish]
deploy/ubuntu/kronika-release status
deploy/ubuntu/kronika-release check --release <exact-authorized-public-main-40-hex-SHA>
#------------------------------------------------------
```

These precede a separately authorized refresh. `check` creates local temporary archives and therefore was not permissible in this exchange’s no-writes envelope.

## 7. Rollback and lockout-prevention order

Each firewall and SSH grant needs its **own** recovery case:

1. Cooperator confirms working physical console and local recovery login.
2. Keep the existing tailnet session open.
3. Establish fresh key-only SSH before changing policy.
4. Snapshot exactly the files that the row will modify, preserving ownership/modes in root-only recovery storage.
5. Verify the installed rollback helper and snapshot. Exercise its logic against synthetic fixtures beforehand.
6. Arm a root systemd rollback timer for ten minutes; verify its active state, future expiry and exact restore command.
7. Apply only the granted change. SSH syntax validation must pass before reload.
8. Prove fresh independent tailnet authentication, LAN denial and application/backup continuity.
9. Cancel rollback only after all gates pass. Otherwise allow local restoration and stop.

The timer and restore executable must operate without SSH, DNS, Tailscale, a workstation connection or a retained sudo timestamp. No reboot may occur while either network rollback timer is armed.

Snapshots:

- UFW: exact affected persistent user-rule files and relevant configuration.
- SSH: exact modified drop-ins and any explicitly approved provisioning-policy file.
- Unit activation: prior physical unit/drop-in bytes, modes and enabled states.
- Cache mode: exact prior parent mode; no recursive chmod.
- CUPS: prior unit enable/mask states.
- AppArmor: only affected profile bytes and modes.

Package rollback is not an automatic downgrade. Retain a previously bootable kernel and use console recovery where necessary. Application release rollback remains the canonical helper’s responsibility.

Capture restart is not automatic rollback: it would reactivate a parked module and requires separate explicit authority.

ADR-0058’s exit-node rollback is unsuitable for firewall/SSH recovery and must not be reused as though it restores those surfaces.

## 8. Vulnerability annex

**Coverage cutoff:** 2026-10-29.  
**Retrieval date for every source below:** 2026-10-30.  
**Coverage:** selected official notices and upstream advisories, not “all vulnerabilities.” Unless stated otherwise, a distinct update date was not exposed by the retrieved source.

Ubuntu revisions must be compared using Debian package-version semantics. Upstream version numbers alone do not establish whether Ubuntu backports are present.

### Host and runtime advisory selection

| Official source/title; publication/update | Affected range → fixed version | Applicability, confidence and evidence |
|---|---|---|
| [USN-8903-1 — Linux kernel vulnerabilities](https://ubuntu.com/security/notices/USN-8903-1), 2026-10-08 | Affected Noble kernel revisions; per-CVE lower bounds differ → generic `6.8.0-146.146` | **unknown; medium.** Observed ABI matches the fixed ABI, but full package provenance is missing. |
| [CVE-2026-23268 / CrackArmor](https://ubuntu.com/security/CVE-2026-23268), published 2026-03-18, updated 2026-10-12 | Affected Noble kernel revisions → `6.8.0-106.106` | **unknown; medium.** Observed ABI suggests the kernel correction is already present. Userspace mitigation/version remains unobserved. |
| [USN-8402-1 — systemd vulnerabilities, official mailing-list notice](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-June/010717.html), 2026-06-08 | Affected Noble systemd revisions → `255.4-1ubuntu8.16` | **unknown; low.** Exact package and nspawn use missing. The resolved DNSSEC issue in this notice concerns 22.04, so that specific issue is **not-applicable** to the documented 24.04 host. |
| [USN-8928-1 — OpenSSH vulnerabilities](https://ubuntu.com/security/notices/USN-8928-1), 2026-10-14 | Affected Noble client/server revisions → `1:9.6p1-3ubuntu13.20` | **unknown; medium.** sshd is active, but exact package revision and individual prerequisites are missing. |
| [USN-8405-1 — CUPS vulnerabilities, official mailing-list notice](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-June/010720.html), 2026-06-08 | Affected Noble CUPS revisions → `2.4.7-1.2ubuntu7.13` | **unknown; medium.** Wildcard listener observed; queue/job/local-user prerequisites differ. This June fix does not establish closure of later CUPS issues. |
| [TS-2026-016 — Serve Unix backends reaching privileged sockets](https://tailscale.com/security-bulletins#ts-2026-016), 2026-10-26 | Earliest affected version unspecified → `1.104.4` | **unknown; medium.** Unix backend is configured; installed version and local configuration/backend-write privileges are missing. High-priority inventory item. |
| [TS-2026-017 — HTTP/2 Serve capabilities crossing mounts](https://tailscale.com/security-bulletins#ts-2026-017), 2026-10-26 | Earliest affected version unspecified → `1.104.4` | **unknown; low.** Requires differently authorized mounts; only one mount is reported. |
| [TS-2026-014 — Tailscale SSH Unix forwarding](https://tailscale.com/security-bulletins#ts-2026-014), 2026-10-26 | Earliest affected version unspecified → `1.104.4` | **unknown; low.** Embedded Tailscale SSH is unobserved. Ordinary OpenSSH over tailnet is distinct. |
| [Node — October 21, 2026 Security Releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases), 2026-10-21 | Affected supported 22/24/26 release lines before fixes → `22.23.4`, `24.22.1`, `26.12.1` | **unknown; low.** Actual capture runtime/provenance is missing; prerequisites vary. |
| [Chrome — Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), 2026-10-27 | Individual lower bounds unspecified → Linux Chrome `156.0.8078.73` | **unknown; low.** Upstream reference only; it is not automatically the correct snap/distro Chromium target. |
| [USN-8956-1 — Brotli vulnerability](https://ubuntu.com/security/notices/USN-8956-1), 2026-10-26 | Affected Noble packages → `1.1.0-2ubuntu0.1` | **unknown; low.** Package presence and decoder reachability missing; does not repair bundled copies. |
| [USN-8954-1 — zlib vulnerability](https://ubuntu.com/security/notices/USN-8954-1), 2026-10-22 | Affected Noble packages → `1:1.3.dfsg-3.1ubuntu2.3` | **unknown; low.** Runtime linkage and vulnerable operation use missing. |
| [CPython — compromised intermediate-certificate distrust](https://mail.python.org/archives/list/security-announce%40python.org/message/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/), 2026-10-24; [fixed release](https://www.python.org/downloads/release/python-31318/), 2026-10-25 | Earlier 3.13 builds lack this correction; earliest affected unspecified → `3.13.18` | **likely missing correction; medium.** Frozen contract expects `3.13.14`; confirm actual binary. TLS exposure depends on trust/runtime use. |
| [CPython — tar-filter traversal bypass](https://mail.python.org/archives/list/security-announce%40python.org/thread/43JOWPRAV5DI3VZ4FUEUAZOHCATXXOCK/), 2026-10-22; [fixed release](https://www.python.org/downloads/release/python-31318/), 2026-10-25 | Affected earlier 3.13 builds, lower bound unspecified → `3.13.18` | **unknown; medium.** Requires affected tar filtering. Release extraction uses `filter="data"` and independent member validation; do not misclassify that path as the advisory’s `tar_filter` case. |
| [Poetry — wheel path traversal](https://github.com/python-poetry/poetry/security/advisories/GHSA-2599-h6xx-hpxp), 2026-03-31 | `>=1.4.0,<=2.3.2` → `2.3.3` | **not-applicable if expected 2.4.1 confirmed; high** range confidence. |
| [Poetry — tar extraction traversal](https://github.com/python-poetry/poetry/security/advisories/GHSA-73h3-mf4w-8647), 2026-04-18 | Poetry `<=2.3.3` on specified older Python environments → `2.3.4` | **not-applicable if frozen versions confirmed; high.** Both expected Poetry and Python exceed the stated prerequisites. |

The CPython correction cannot be hidden inside Ubuntu package maintenance or installed under a misleading frozen version path. It requires a separate tooling/security decision or explicit residual-risk acceptance.

### Application dependency coverage

Verified direct production lock versions:

| Dependency | Version | Research result |
|---|---:|---|
| pydantic-settings | 2.14.2 | Selected nested-secret advisory fixed at this version. |
| FastAPI | 0.138.0 | Official advisory index reviewed; selected historical issue predates this version. |
| Uvicorn | 0.49.0 | Official index reviewed; no published advisory identified there. |
| SQLAlchemy | 2.0.51 | Official index reviewed; no published advisory identified there. |
| Alembic | 1.18.4 | Official index reviewed; no published advisory identified there. |
| Pillow | 12.2.0 | Matches current advisory ranges below. |
| yt-dlp | 2026.7.4 | Selected shortcut-injection correction included at this version; bundled-executable notices must not be applied wholesale to this pip installation. |

Named high-risk transitives reviewed: Starlette `1.3.1`, AnyIO `4.14.0`, Pydantic `2.13.4`, pydantic-core `2.46.4`, h11 `0.16.0`, idna `3.18`, Mako `1.3.12`, MarkupSafe `3.0.3`, python-dotenv `1.2.2`.

“No advisory identified” describes source coverage, not safety certification. Official indices include [Uvicorn](https://github.com/Kludex/uvicorn/security/advisories), [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy/security/advisories) and [Alembic](https://github.com/sqlalchemy/alembic/security/advisories).

### Current lock-version matches

For every entry below: publication date is shown; update date was not separately exposed; retrieval date is 2026-10-30. **Host applicability is unknown pending row 00.** Confidence is high in the published range and lock comparison; exploit reachability is not established.

| Official advisory/title | Published | Affected → fixed | Repository evidence and limitations |
|---|---|---|---|
| [Pillow JPEG draft-scaling heap overflow](https://github.com/python-pillow/Pillow/security/advisories/GHSA-8g5g-8vmr-9782) | 2026-10-17 | `<=12.3.0` → `13.0.0` | Lock matches. Requires relevant libjpeg-turbo build and draft/thumbnail path; matching application use was not found. |
| [Pillow bundled OpenJPEG heap write](https://github.com/python-pillow/Pillow/security/advisories/GHSA-78g4-xqwv-q3g8) | 2026-10-17 | Affected wheels `11.1.0–12.3.0` → `13.0.0` | Lock matches; installed wheel/codec and JPEG2000 input reachability missing. |
| [Pillow XBM open-phase ReDoS](https://github.com/python-pillow/Pillow/security/advisories/GHSA-xgh8-jp6q-p5x8) | 2026-10-17 | `<=12.3.0` → `13.0.0` | Lock matches. Some unrestricted `Image.open()` paths precede format checks; upload signature gate narrows one path. |
| [Pillow GIF-comment DoS](https://github.com/python-pillow/Pillow/security/advisories/GHSA-74r2-7ff9-mjj2) | 2026-10-17 | `5.4.0–12.3.0` → `13.0.0` | Lock matches; assess accepted image routes before exploitability conclusions. |
| [Pillow Ghostscript filename injection](https://github.com/python-pillow/Pillow/security/advisories/GHSA-w889-685w-c8fh) | 2026-10-17 | `2.6.0–12.3.0` → `13.0.0` | Lock matches; attacker-controlled filename/EPS/Ghostscript prerequisites not established for reviewed BytesIO paths. |
| [Pydantic extra JSON-key validation bypass](https://github.com/pydantic/pydantic/security/advisories/GHSA-qpmf-fgh3-ff25) | 2026-10-29 | `>=2.13.0,<2.14.2` → `2.14.2` | Lock matches; required typed extra-key configuration not found in production-source searches. |
| [Pydantic aliased TypedDict/dataclass bypass](https://github.com/pydantic/pydantic/security/advisories/GHSA-3r8g-cqwr-jr29) | 2026-10-29 | `>=2.0,<2.14.2` → `2.14.2` | Lock matches; required usage not found; ordinary BaseModel alone does not establish reachability. |
| [AnyIO TLS IDNA certificate spoofing](https://github.com/agronholm/anyio/security/advisories/GHSA-82r6-8w77-94w6) | 2026-07-07 | `<=4.14.1` → `4.14.2` | Lock matches; requires affected TLS API, non-ASCII hostname and connection hijacking. |
| [AnyIO process-pool stderr hang](https://github.com/agronholm/anyio/security/advisories/GHSA-5p39-cfhj-2xmp) | 2026-07-07 | `<=4.14.1` → `4.14.2` | Lock matches; no production `to_process` use found. |
| [AnyIO supplementary-group retention](https://github.com/agronholm/anyio/security/advisories/GHSA-3w57-8xmc-8v26) | 2026-07-07 | Exactly `4.14.0` → `4.14.2` | Exact lock match; no matching process privilege-drop calls found. |

Pillow is constrained to `<13` in `pyproject.toml`. Moving to the advisory’s fixed version requires an explicit compatibility and dependency-bound decision, relocking, regression tests, publication and refresh. It is not an incidental host patch.

Selected fixed comparisons:

| Advisory | Publication | Affected → fixed | Applicability |
|---|---|---|---|
| [Starlette form-limits DoS](https://github.com/Kludex/starlette/security/advisories/GHSA-82w8-qh3p-5jfq) | 2026-06-12 | `>=0.4.1,<1.3.1` → `1.3.1` | Lock fixed; host **unknown**; high range confidence. |
| [h11 malformed chunk bodies](https://github.com/python-hyper/h11/security/advisories/GHSA-vqfr-h8mv-ghfj) | 2025-04-24 | `<=0.15.0` → `0.16.0` | Lock fixed; host **unknown**; high confidence. |
| [pydantic-settings nested-secret symlinks](https://github.com/pydantic/pydantic-settings/security/advisories/GHSA-4xgf-cpjx-pc3j) | 2026-06-19 | `>=2.12.0,<2.14.2` → `2.14.2` | Lock fixed; host **unknown**; high confidence. |
| [yt-dlp shortcut command injection](https://github.com/yt-dlp/yt-dlp/security/advisories/GHSA-6v4j-43gg-vj32) | 2026-07-04 | `<2026.7.4` → `2026.7.4` | Lock fixed; host **unknown**; high confidence. |

`httpx2` and `httpcore2` `2.4.0` are dev-only. The canonical release installs `--only main`; do not label their advisories as production exposure without contrary installed metadata. The lock has no package blocks for cryptography, certifi, Brotli, requests, urllib3 or python-multipart; extras text is not installation evidence.

### Priority and limitations

Prioritize by actual exposure and prerequisites:

1. Tailscale version and Unix-backend boundary.
2. Unnecessary CUPS exposure and applicable daemon/security updates.
3. Pillow input-path and installed-wheel triage.
4. Frozen runtime correction/residual-risk decision.
5. Lower-reachability Pydantic/AnyIO matches and parked capture runtimes.

No scanner, PoC, exploit, hostile media or provider call was used.

Source gaps:

- Canonical USN-8402-1 timed out; the official Ubuntu mailing-list copy was available.
- [CUPS CVE-2026-87875](https://ubuntu.com/security/CVE-2026-87875) surfaced with publication 2026-09-09, but the tracker detail repeatedly timed out. Noble affected/fixed ranges remain **unknown**; the June CUPS notice cannot close it.
- AppArmor userspace and systemd-resolved coverage are bounded, not exhaustive.
- Bundled OpenSSL, Expat and image-codec provenance remains unobserved.
- Mutable tracker content retrieved on October 30 does not prove every displayed update existed by the October 29 cutoff.

## 9. Risk register

| Risk | Severity / likelihood | Owner | Mitigation and residual |
|---|---|---|---|
| SSH/firewall lockout | High / medium | Cooperator | Physical console, separate changes, root timer, fresh authentication. Residual requires explicit acceptance. |
| Vulnerable active Tailscale Serve | Potential high / unknown | Cooperator | Version-first assessment; fixed-release update if applicable. No confirmed host finding yet. |
| Sandbox breaks media/backup | Medium / medium | Implementer + independent verifier | Synthetic workloads, staged directives, exact unit rollback. |
| Frozen CPython lacks newer corrections | Potential high / unknown reachability | Cooperator | Separate tooling decision or explicit residual disposition; preserve frozen contract meanwhile. |
| Pillow lock matches current advisories | Potential high / unknown host reachability | Orchestrator/Cooperator | Installed-build and input-path triage; separate dependency correction authority. |
| Package/reboot loses access | High / low–medium | Cooperator | Console window, retained kernel, pre/post backup and network proof. |
| CUPS reactivated by socket/package behavior | Medium / medium | Cooperator | Cover installed activation surfaces; repeat negative checks after update/reboot. |
| Capture stop interrupts pending work | Medium / unknown | Cooperator | Owner confirms no work requiring continuation; graceful stop; no agent browser inspection. |
| Shared-UID sandbox side effects | Medium / medium | Implementer | Defer `RemoveIPC`/user namespaces; test web and backup together. |
| False assurance from stale/versionless evidence | Medium / high | Orchestrator | Label evidence, remeasure versions, separate static and dynamic controls. |

Medium-or-higher residual risks require explicit Cooperator disposition; none is silently accepted here.

## 10. Cooperator decisions

| Decision | Options and recommendation | Current disposition |
|---|---|---|
| Capture lifecycle | **Recommend stop/disable**; alternative retain running with stated need/risk. | **Selected: stop/disable.** |
| SSH forwarding | **Recommend prohibit**; alternative retain narrowly documented local forwarding. | **Selected: prohibit.** |
| Printing | **Recommend disable all installed activation surfaces and retain packages**; alternatives reviewed package removal or retained printing with access policy. | **Selected: disable, retain packages.** |
| SSH operator allowlist | **Recommend explicitly approved operator accounts only**; alternative retain unrestricted account eligibility with residual acceptance. | Pending private account selection. |
| Transmission/AppArmor | **Recommend remove confirmed-unused installed application packages**; otherwise validate enforcement for used profiles, or document inactive profiles/residual. | Pending package/use evidence. |
| Maintenance window | **Recommend named console-attended package/reboot window**; alternative defer with exposure recorded. | Pending date/window and console confirmation. |
| Frozen runtime | **Recommend separate tooling-security decision**; alternative bounded residual-risk acceptance. Do not replace bytes under a misleading frozen version path. | Pending Orchestrator/Cooperator disposition. |
| Dependency matches | **Recommend separate compatibility/relock correction grant**; alternative evidence-backed nonreachability/residual disposition. | Pending; outside host-unit grant. |
| ADR-0058 recovery | **Recommend preserve documented limitation and keep implementation separate**; alternative explicit scope expansion under its own grant. | Recommendation only. |
| AppArmor expansion | **Recommend existing-profile/package disposition only**; alternative separately planned bespoke Kronika policy. | Recommendation only. |

## 11. Verification, acceptance and closure conditions

Repository implementation must remeasure the baselines it relies on through the exact authorized AP route. Relevant existing tests include unit/runbook/release/capture/retention contracts and production runtime/health tests. Add meaningful rollback tests for path escape, symlink rejection, stale state, exact restoration and failure handling.

The reported historical Python and JavaScript counts were **not rerun** here.

Acceptance requires:

- Exact public-main and deployed provenance.
- Preserved frozen hashes and migration membership.
- Fresh tailnet SSH success and controlled Wi-Fi LAN SSH denial.
- No CUPS listener/reachability; parked capture inactive.
- Effective service/account/secret/cache/socket boundaries.
- Healthy application, synthetic media workflow and actual scheduled backup success.
- Applicable security fixes verified by installed revision and running state.
- Explicit disposition of unresolved runtime/dependency risks.
- Independent read-only verification.
- Michal’s rendered UI and companion acceptance **after final public main is refreshed onto the NUC**.

UI checks must preserve the accepted Gallery/Details behavior and use separately authorized synthetic records/media. No private media, capture login, Research activation or provider contact is implied.

Only the Orchestrator may decide logical-whole closure after these conditions and living-document reconciliation. This Worker does not close it.

## 12. Open evidence gaps and smallest next step

The smallest next step is a **new, explicit row-00 Cooperator-executed read-only inventory grant**, not an implementation grant.

Its required outputs are:

1. Exact installed/candidate versions, package provenance and running kernel.
2. Actual release distribution metadata and frozen executable versions.
3. Privileged socket metadata.
4. Effective unit/drop-in paths and complete bounded writable-path assertions.
5. Relevant SSH `Match` contexts and privately approved account set.
6. Tailscale version, embedded-SSH setting, Serve mounts and configuration/backend ownership facts.
7. CUPS activation membership and controlled reachability.
8. Transmission package/profile ownership and attachment.
9. Backup readiness and last actual scheduled success.
10. Console recovery capability and maintenance-window decision.

Until those outputs exist, exact patch targets, host advisory applicability, final AppArmor action and some sandbox compatibility decisions cannot be completed honestly. The unavailable later CUPS advisory and frozen-runtime/dependency disposition also prevent a complete security closeout specification.

## 13. Validation, deviations and terminal disposition

Completed evidence:

- HEAD, local `origin/main`, AP gitlink and AP checkout matched the declared SHAs.
- Initial and final worktrees were clean.
- Baseline-bound `ap project check` passed through the canonical sanitized route.
- Read-only hash comparison found **zero mismatches across 86 frozen documents and 36 migrations**; membership checks and impossible-member control passed.
- Parsed lock inventory was nonempty and unique: **31 packages**, including **23 main-group entries**.
- Enumerated **16 systemd artifacts**.
- No application tests or host checks were executed.

**Resolved Execution Issues / Near-Misses:** Broad initial outputs were truncated and relevant passages were reread in bounded slices. A Node probe spawning Git failed with `EPERM`; a filesystem-only hash/membership probe subsequently passed. This is static evidence, not a substitute claim that pytest ran.

**Pre-Existing Failure Classification:** None established. Unknown host facts remain evidence gaps.

**Internal delegation:** Three internal research tasks covered units/release contracts, runbooks/recovery, and host advisories; dependency research followed. Their purpose was parallel evidence gathering. Key repository conclusions were checked against literal sources. Delegates were not independent auditors. No conflicting conclusion was left unresolved except the explicitly recorded evidence and source-availability gaps.

**Commit/push result:** Not authorized; not performed.  
**Changed files:** None.  
**Terminal disposition:** `PARTIAL`; planning authority expires with this report. Implementation requires a fresh Worker session and a complete new prompt with `Native planning mode: not-used`.

Orchestration critique:  
MEASURED: Routine deploy/rollback contracts prohibit systemd installation and daemon reload; changed unit sources therefore require a separate owner-executed activation grant.  
LEAD: Installed Tailscale may predate 1.104.4 while Serve uses a Unix backend; the cheapest useful check is the first-row version and bounded configuration inventory.