# NUC security hardening — approval-gated implementation plan

## 1. Revised baseline and completed Tailscale outcome

The plan is decision-complete for the recommended choices below. Private account identifiers, the maintenance window and the reviewed package manifest are execution parameters to supply before their respective grants. They do not require another planning revision.

The previous 24-row sequence becomes **ten remaining mutation outcomes**, with separate independent review and acceptance gates. Evidence collection, snapshots, syntax checks and postchecks belong inside the outcome they protect.

### Delta since exchange 01

| Surface | Revised evidence and disposition |
|---|---|
| Tailscale | **Cooperator-observed:** upgraded successfully from `1.102.2` to `1.104.4`; row 02 complete. |
| CUPS | **Cooperator-observed:** OpenPrinting snap `2.4.20-1`, revision 1277; both snap services active/enabled. No dpkg CUPS packages or `cups.*` units. Replace the earlier systemd-package procedure with `snap disable cups`. |
| Kernel | **Cooperator-observed:** running package `6.8.0-146.146`; `6.8.0-147.147` installed; reboot pending. |
| Selected packages | **Cooperator-observed:** systemd `255.4-1ubuntu8.18`, OpenSSH `1:9.6p1-3ubuntu13.20`, and reported zlib/Brotli revisions satisfy the selected prior advisory thresholds. This is not universal vulnerability clearance. |
| AppArmor | **Cooperator-observed:** authoritative profile-file count is 63 enforce / 4 complain. The `1/1` display was a formatting artifact. Installed userspace `.7`, candidate `.9`. |
| Transmission | **Cooperator-observed:** packages and units absent; stale root-owned `/etc/apparmor.d/transmission` remains. Default: document and retain it. |
| Socket/cache | **Cooperator-observed:** runtime `0750`; socket `0600 kronika:kronika`; cache remains `0755`. Socket uncertainty is resolved. |
| Backup | **Cooperator-observed:** timer enabled/active; last success `2026-10-30 03:31:40 UTC`; restore readiness `ready`; 30 automatic and 28 pinned bundles. Off-device remains unconfigured. |
| Toolchain | **Cooperator-observed:** frozen and release Python `3.13.14`; Poetry `2.4.1`. Tooling-security remediation is outside this whole. |
| Application dependencies | Pillow/Pydantic/AnyIO advisory matches remain recorded, outside all host-hardening grants. |

The repository inventory remains unchanged: 16 systemd artifacts, the canonical release-helper pair, associated runtime sources, runbooks and contract tests. Credential templates, capture/off-device units and frozen artifacts remain read-only.

### Row 02 — COMPLETE

Completion is based on **Cooperator-observed host evidence**, not Worker host verification:

- Only `tailscale` upgraded; installation exited zero.
- `tailscaled` active.
- Tailnet-only Serve retains one mount to `/run/kronika/kronika.sock`.
- `RunSSH=false`; Funnel off.
- Application health `ready`; backup timer active.
- Observed HTTPS listener count remains two.

Official-source recheck retrieved 2026-10-30:

| Advisory | Published | Fixed threshold | Disposition |
|---|---|---|---|
| [TS-2026-014 — SSH Unix forwarding](https://tailscale.com/security-bulletins#ts-2026-014) | 2026-10-26 | `1.104.4` | Closed by observed version; embedded SSH is also disabled. |
| [TS-2026-016 — privileged Unix backends](https://tailscale.com/security-bulletins#ts-2026-016) | 2026-10-26 | `1.104.4` | Closed by observed version; preserve the protected backend. |
| [TS-2026-017 — capabilities across Serve mounts](https://tailscale.com/security-bulletins#ts-2026-017) | 2026-10-26 | `1.104.4` | Closed by observed version; the multiple-mount prerequisite is also absent. |
| [TS-2026-008 — Serve/Funnel CPU denial of service](https://tailscale.com/security-bulletins#ts-2026-008) | 2026-07-13 | `1.98.9` | Already fixed before this upgrade. |

The first three bulletins do not establish the earliest affected release. Do not claim every earlier version was vulnerable. `1.104.2` is below their fixed threshold and is not a rollback target. Separate update dates were not exposed.

**Further action: none for these advisories.** Preserve the cosmetic `sd_notify` observations without restarting services to silence them.

## 2. Consolidated grants and authority

One grant executes one row. All host mutations are Cooperator-executed. Each grant must name its exact paths, version/SHA parameters, commands, checkpoints, rollback and stop conditions.

| Row | Outcome and authority | Dependencies, proof and recovery |
|---|---|---|
| **01 — evidence reconciled** | Accept the supplied version/configuration observations and verified repository baseline. No new full inventory cycle. | Remaining narrowly scoped observations are preconditions of the affected cut. No host action occurred in this exchange. |
| **02 — complete** | Tailscale `1.104.4` update and selected advisory closure. | Preserve current healthy state; no downgrade or cosmetic restart. |
| **03 — CUPS snap disabled** | Cooperator/root: exact `snap disable cups`; retain snap, revision history and data. | Verify both snap services disabled/inactive and port 631 absent. Exact rollback: `snap enable cups`. Reprove after reboot. |
| **04 — capture operationally parked** | Cooperator/root: gracefully stop/disable runner, bridge and Xvfb; keep view/VNC inactive. | Owner confirms no work needs continuation. Preserve profile/state without inspection. Re-activation is not automatic rollback and requires separate authority. |
| **05 — repository hardening bundle** | Fresh implementation Worker: exact allowlist in section 5; tests and one local commit on task branch `nuc-security-hardening`. | Remeasure relevant baseline first. No publication, host access, dependency change or frozen edits. Failures outside the allowlist stop the cut. |
| **05V — independent candidate review** | Fresh independent Worker; source-read-only review of the exact candidate, recovery design and validation evidence. | Must precede publication. Corrections require a separate bounded corrective grant; the implementer cannot certify independence. |
| **06 — publication** | Separately authorized publisher: accepted exact candidate to public `main`, with public SHA/content verification. | Stop if public main advanced incompatibly; no force push, silent rebase or deployment. |
| **07 — routine immutable refresh** | Cooperator under explicit release authority: canonical status/check and separately initiated deployment of the approved SHA. | Preserve canonical backup, provenance, health and rollback gates. A successful check does not itself authorize deployment. This row does not install units. |
| **08 — activate reviewed local hardening** | Cooperator/root: install approved web/backup units and reviewed recovery helper; set cache/runtime modes; daemon reload and bounded application restart. | Preserve credential/publication drop-ins. Verify synthetic workloads and an actual scheduled backup success. Restore exact previous unit bytes/modes on failure. |
| **09 — UFW rule correction** | Cooperator/root: remove only the approved stale wired LAN rule. | Row 08 helper installed; physical console, exact snapshot and independent ten-minute rollback. Fresh tailnet SSH positive and Wi-Fi LAN negative before cancellation. |
| **10 — SSH policy correction** | Cooperator/root: approved operator allowlist, forwarding prohibition, fallback correction and selected limits. | Separate snapshot/timer from row 09. Syntax/effective-policy checks before reload; newly authenticated SSH proof afterward. Restore exact touched files on failure. |
| **11 — reviewed package transaction** | Cooperator/root: install the exact approved security-relevant package/version manifest. | Review current simulation first. Exclude frozen tooling/application dependencies and further Tailscale work. No removals, autoremove, release upgrade or isolated Wi-Fi restart. |
| **12 — reboot and persistence proof** | Cooperator/root: explicit console-attended reboot in the approved window. | All transactions completed and rollback timers canceled. Boot installed kernel 147; verify the complete postboot matrix below. Retain previous kernel for console recovery. |
| **13 — independent acceptance** | Fresh independent read-only verifier plus explicitly authorized Cooperator rendered/companion acceptance. | Exact public main already on NUC. Verify host boundary, actual scheduled backup success and residual decisions. Synthetic fixtures only; no provider call or capture activation. |

Rows 03–04 can proceed independently after their own grants. Package/reboot work may be scheduled earlier if necessary, but remains separate from repository, capture and network-policy cuts. Any earlier reboot must repeat persistence checks for configuration changed afterward.

Read-only preflight produces the literal package manifest before row 11 is granted. It is transaction preparation, not another planning revision.

Documentation in row 05 records the implementation contract and distinguishes source availability from host acceptance. It must not prematurely claim whole completion. Final host evidence belongs in the terminal reports and operator trace; subsequent closure-document changes need their own authority.

## 3. Implementation, proof and recovery contracts

### CUPS snap cut

Exact mutation: **`snap disable cups` only**.

Preconditions:

- Confirm installed snap identity, channel and current revision.
- `snap services cups` shows the two expected services.
- Record current snap enabled state and port-631 baseline.
- Confirm no conflicting snap change is running.

Expected post-state:

- `cups.cupsd` and `cups.cups-browsed`: disabled/inactive.
- `snap.cups.cupsd.service`: inactive.
- No TCP4 or TCP6 listener on 631.
- Authorized tailnet peer cannot connect to 631.
- Application/Serve and backup timer remain healthy.

Future command specifications, not commands issued in this planning exchange:

| Purpose | Command |
|---|---|
| Snap identity | `snap list cups` |
| Service state | `snap services cups` |
| Change in progress | `snap changes` |
| Listener proof | `ss -H -lnt '( sport = :631 )'` |
| Parser positive control | `ss -H -lnt '( sport = :22 )'` |
| Unit state | `systemctl is-active snap.cups.cupsd.service` |
| Granted mutation | `sudo -n snap disable cups` |
| Granted rollback | `sudo -n snap enable cups` |

An inactive-unit exit status is an expected negative result, not an execution failure.

Retain the snap. Do not change channel, refresh scheduling, hold state or revision, and do not run refresh/remove/revert in this cut. Do not assume retained disabled contents remain security-updated. Later snap maintenance must reprove that CUPS remains disabled and 631 absent; unexpected reactivation stops that maintenance outcome. Re-enabling outside explicit rollback requires a fresh security review.

### Capture cut

Gracefully stop the runner before its bridge/display dependencies; preserve inactive view/VNC state. Disable automatic startup of the three previously enabled services.

Proof is inactive/disabled state, absent capture/view listeners, continued application health and persistence after reboot. No profile, browser session, credentials or pending prompt content may be inspected. No automatic restart is authorized as recovery.

### Service hardening

Preserve these exact candidates from exchange 01:

| Target | Selected settings |
|---|---|
| Web and local backup | `PrivateDevices=true`, `ProtectHostname=true`, `ProtectClock=true`, `ProtectKernelLogs=true`, `RestrictNamespaces=true`, `RestrictRealtime=true`, `SystemCallArchitectures=native` |
| Web | `CacheDirectoryMode=0700`, `RuntimeDirectoryMode=0750`, `RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6` |
| Local backup | `RestrictAddressFamilies=AF_UNIX`, `IPAddressDeny=any`, `InaccessiblePaths=/srv/media` |
| Separately validated filter stage | `SystemCallFilter=~@clock @module @mount @raw-io @reboot @swap`, `SystemCallErrorNumber=EPERM` |

Validate the common/address-family settings and syscall-filter stage separately within row 08. Failure restores the failed stage and stops acceptance; it does not authorize ad hoc weakening.

Continue to defer web MDWE, `PrivateUsers`, `RemoveIPC` and `ProcSubset=pid`. Preserve capture/X11 unit differences and the intentional publication write exception.

Required proof:

- Unit syntax valid on the actual systemd version.
- Effective settings and bounded writable paths match the accepted source.
- Socket remains service-owned `0600`, runtime `0750`, cache parent `0700`.
- Healthy application over the canonical Unix socket.
- Synthetic SQLite, generated-media ffmpeg/ffprobe, preview/cache and backup/restore workloads pass.
- Web outbound compatibility uses local stubs; backup network isolation is verified.
- Actual scheduled backup success completes after activation, with readiness `ready` and no pending cleanup.
- No recursive chmod or source-media write attempt.

The existing contract explicitly separates routine deployment from unit installation. Release rollback alone does not restore installed unit changes; row 08 needs its own unit/mode snapshot.

### Recovery helper and network order

Preserve the helper interface:

- Fixed operations: `snapshot`, `verify`, `restore`.
- Enumerated surfaces: `ufw` or `sshd`.
- Installed physical executable: `/usr/local/libexec/kronika/nsh-boundary-rollback`.
- Root-only recovery state: `/var/lib/kronika-host-hardening`.
- Reject arbitrary paths, symlinks, unsafe ownership/modes, stale state and conflicting operations.
- Restore only the exact touched UFW files or SSH drop-ins; never host keys, profiles or unrelated configuration.

Each network cut follows this order:

1. Working physical console and existing tailnet session.
2. Fresh authenticated SSH baseline.
3. Exact root-controlled snapshot; verify helper and snapshot.
4. Arm and verify an independent root ten-minute rollback timer.
5. Apply only that cut; run `sshd -t` before SSH reload.
6. Prove new authentication, expected LAN denial and service continuity.
7. Cancel rollback only after every gate passes.

The timer must work without SSH, DNS, tailnet connectivity or a sudo timestamp. No reboot while armed. If it fires, classify the cut as rolled back and stop.

Fresh Cooperator SSH proof explicitly disables multiplexing:

```text
# [MacBook / fish]
ssh -S none -o ControlMaster=no -o ControlPath=none -o BatchMode=yes -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -i "$KRONIKA_NUC_SSH_IDENTITY" "$KRONIKA_NUC_SSH_USER@$KRONIKA_NUC_SSH_TARGET" true
#------------------------------------------------------
```

The Worker gate alone does not establish a fresh authentication session.

LAN negative testing uses the privately verified Wi-Fi address from a functioning LAN peer, with an independent positive connectivity control. Wired empirical testing remains **not tested** while the wired interface is down; verify exact rule removal without enabling it.

SSH settings:

- Preserve key-only authentication, root denial and existing agent/X11 restrictions.
- `DisableForwarding yes`.
- `MaxAuthTries 3`, `LoginGraceTime 30`.
- `ClientAliveInterval 300`, `ClientAliveCountMax 2`.
- `AllowUsers` contains only the explicitly approved operator identities.
- Neutralize the password allowance in `50-cloud-init.conf`; verify effective relevant `Match` contexts and retain the earlier hardening drop-in.

Client-alive probes are liveness detection, not an idle logout guarantee.

### Package and reboot proof

Before row 11:

- Classify the current remaining candidate list; do not reuse a stale count as the manifest.
- Review exact package versions, origins, dependencies, removals and restart implications.
- Assess AppArmor candidate `.9`; install only when included in the approved classified manifest.
- Preserve current Tailscale `1.104.4`; no downgrade.
- Confirm healthy backup and retained bootable kernel.
- Require an approved maintenance window and physical console.

After the transaction, record installed versions and actual results, not just simulation output. A package failure stops the row; no improvised downgrade.

Resolve deferred `dbus`, `systemd-logind`, `unattended-upgrades` and `wpa_supplicant` restart state through the explicit reboot. **Do not restart `wpa_supplicant` alone.**

Postboot acceptance:

- Running kernel corresponds to installed `6.8.0-147.147`.
- Wi-Fi operational; wired interface remains down.
- Fresh key-only tailnet SSH succeeds.
- Tailscale active; `RunSSH=false`; one tailnet-only UDS Serve mount; Funnel off.
- Application health ready; socket ownership/mode preserved.
- Backup timer enabled/active; readiness valid.
- Capture disabled/inactive, without unintended relaunch.
- CUPS snap disabled/inactive; no 631 listener.
- AppArmor active; no new unexplained application confinement failure.
- Reboot-required and deferred-restart state reconciled with actual running processes.

If boot fails, use the physical console and retained prior kernel. Do not remove older kernels or run broad cleanup in this whole.

### Acceptance and command handling

Independent acceptance must include an actual timer-triggered backup pipeline. The existing successful run is the pre-change checkpoint, not proof of post-hardening scheduling.

Rendered Gallery/Details and companion checks belong to Michal, after public main is refreshed onto the NUC. Preserve accepted behavior; use separately authorized synthetic records/media and exact cleanup.

Owner execution uses one command block at a time with complete output and exit status. No privileged script is pasted through chat. The Cooperator establishes privilege; terminal handling uses project-required `sudo -K`. Lost-session privilege release is recorded as unknown, never fabricated.

## 4. Decisions and residual risks

Approval can adopt all recommendations in one pass. Silence does not select an option or grant execution.

| Decision | Recommendation | Alternative and effect |
|---|---|---|
| **D1 — wired UFW rule** | Remove only the stale wired LAN allowance. | Retain while disconnected only with explicit residual acceptance; skip row 09 mutation and do not claim the latent wired exposure closed. New LAN access is outside this plan. |
| **D2 — SSH allowlist** | Only the privately verified current operator. | Additional approved identities must be named and freshly authenticated before row 10. No account/key changes are implied. |
| **D3 — maintenance/reboot** | Named console-attended window; retain previous kernel. | Deferral blocks rows 11–12 and leaves kernel/deferred-restart residuals explicit. The date is a scheduling parameter. |
| **D4 — stale Transmission profile** | Retain the stale file/profiles as documented inactive residue; packages/units are absent. | Unload/quarantine requires a separate AppArmor-only grant after exact ownership and loaded-profile membership preflight. No package removal or blind enforcement. |
| **D5 — frozen CPython** | Route confirmed `3.13.14` concerns to a separate tooling-security decision; record residual here. | Any tooling change needs its own accepted compatibility/path decision and grant. Never replace bytes under the frozen version path. |
| **D6 — Pillow/Pydantic/AnyIO** | Record and route separately; no dependency edits in this whole. | A compatibility/relock correction needs its own bounded grant, tests, publication and refresh. |
| **D7 — pending packages** | Exact classified security-relevant set and necessary dependencies. | A full classified remaining-package transaction expands row 11’s manifest and rollback assessment. The unclassified 60-package set is not approved wholesale. |
| **D8 — ADR-0058 recovery** | Preserve the documented limitation; route implementation separately. | Routing changes require separate exact diagnostic/recovery authority and cannot enter a firewall/SSH cut implicitly. |

The first three earlier choices—capture stop/disable, SSH forwarding prohibition and CUPS disable with retention—remain settled.

### Updated risk register

| Risk | Severity / likelihood | Mitigation and residual disposition |
|---|---|---|
| Selected Tailscale advisories | **Closed by version**, based on Cooperator evidence | Retain `1.104.4`; independent final observation confirms continuity. No universal vulnerability-clearance claim. |
| Active CUPS snap exposure | Medium / present listener | Row 03 disables the snap; repeat negative proof after reboot and later maintenance. |
| Installed kernel 147 not running | Medium / confirmed pending state | Explicit reboot; retain 146 for console recovery. |
| Deferred Wi-Fi/service restarts | High availability consequence / uncertain | Console-attended reboot; no isolated `wpa_supplicant` restart. |
| Frozen CPython residual | Potential high / reachability-dependent | Separate tooling-security disposition; explicit Cooperator residual decision before closure. |
| Pillow/Pydantic/AnyIO residuals | Potential high / host-path dependent | Separate triage/correction authority; no host-hardening closure claim for them. |
| SSH/firewall lockout | High / medium | Separate transactions, console, root rollback timer and fresh authentication. |
| Sandbox regression | Medium / medium | Staged synthetic workloads, exact unit rollback and scheduled backup proof. |
| Stale Transmission profiles | Low / low under supplied absent-package/unit state | Document retained residue; investigate unexpected attachment rather than claim all profiles enforce. |
| Unclassified pending updates | Unknown until classification | Literal reviewed manifest; no “60 vulnerabilities” inference or blanket upgrade. |

Medium-or-higher residual risks require explicit Cooperator disposition. The plan does not silently accept them.

## 5. Exact repository scope, validation and readiness

### Row 05 mutation allowlist

Only these 17 paths may change:

```text
deploy/systemd/kronika.service
deploy/systemd/kronika-catalog-backup.service
scripts/operator/security/kronika_nuc_boundary_rollback.sh
tests/contract/test_nuc_hardening_rollback.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_catalog_backup_timer.py
tests/contract/test_nuc_release_docs.py
tests/contract/test_nuc_operator_runbook.py
docs/NUC_SECURITY_HARDENING.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/UBUNTU_NUC_CLEAN_INSTALL.md
docs/OPERATOR_NETWORK.md
docs/BACKUP_AND_RECOVERY.md
README.md
ROADMAP.md
SECURITY.md
SERVER.md
```

The helper, helper test and hardening document are new. Other paths already exist.

No changes to AP, release-helper behavior, credential templates, capture/off-device sources, dependency manifests, retention expectations, ADRs or frozen documents/migrations. Preserve the publication-media path and disabled Research. New documentation should link to existing frozen-residue explanations rather than duplicate frozen-name inventories.

No application API/type/schema change is required. The helper adds only the bounded operator interface specified above.

### Baseline remeasurement

Before row 05 mutation:

1. Run canonical AP project check and `runtime-info` against baseline `8c58a81234a97fdf5af9d724a3b526f19745d32a`.
2. Remeasure the existing web/backup/runbook/release/retention contracts used by the change.
3. Run production runtime/health tests where the candidate relies on their behavior.

Use `./.ap/ap exec` with the exact authorized baseline and `--operation test-focus -- … -q -p no:cacheprovider`. Do not reconstruct the environment.

After implementation:

- Run the new helper tests, strengthened unit/runbook tests and relevant unchanged release/capture/off-device/ingress/retention contracts.
- Test UFW and SSH restoration separately with synthetic state and controlled command responses.
- Cover absent/present files, unsafe paths/owners/modes, symlinks, stale/conflicting snapshots, exact restoration and first-failure preservation.
- Run `bash -n` on the helper.
- Validate unit syntax in an authorized compatible systemd environment.
- Run actual host workload and scheduled-backup proofs in row 08.
- Preserve frozen hashes and exact membership.

The new helper test has no before-change execution because the file does not exist yet. Do not manufacture one. Historical full Python/JavaScript counts remain historical; no unrelated JavaScript rerun is required.

### Evidence regenerated in this revision

| Check | Result |
|---|---|
| HEAD and AP pin | Match declared baseline |
| Initial/final worktree state | Clean |
| Baseline-bound AP project check | PASS |
| Frozen documents | 86; zero hash mismatches |
| Frozen migrations | 36; zero hash mismatches |
| Frozen membership | Exact |
| Systemd artifacts | 16 |
| Lock inventory | 31 packages; 23 main-group entries |
| Impossible-member control | PASS |
| Host verification by this Worker | Not performed |
| Tests beyond read-only/static checks | Not run |
| File/Git/host mutations | None |

### Plan-to-execution readiness

**Decision-complete: yes, for the recommended choices.** Approval must explicitly adopt those choices or select their bounded alternatives.

Choices that change execution boundaries are D1, D2, D4 and D7:

- D1 can remove or skip the UFW mutation.
- D2 changes private allowlist membership.
- D4 cleanup adds a separate AppArmor-only cut.
- D7 expands the literal package transaction.

D3 supplies timing and recovery availability. D5, D6 and D8 remain outside this whole. None requires another Planner revision; affected execution grants must carry the selected boundary and verified parameters.

Before rendered acceptance, verify exact public-main/deployed provenance. Before Orchestrator closure, require independent technical acceptance, Michal’s acceptance, actual scheduled backup proof and explicit residual-risk dispositions.

This `PASS` certifies the revised plan’s readiness for approval, not host hardening completion.

Internal delegation covered repository scope, runbook/recovery constraints and the named Tailscale recheck. It was research within one accountable Worker run, not independent acceptance. No unresolved delegate conflict remains.

Resolved execution issues: none material. Searches with no matches were treated as absence evidence only; no host demonstration was manufactured. Pre-existing failure classification: none established.

The report is delivered in chat only. Planning authority expires at this terminal report. Implementation requires a complete new grant targeting a fresh Worker session with `Native planning mode: not-used`.
