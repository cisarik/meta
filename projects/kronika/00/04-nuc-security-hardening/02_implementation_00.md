You are a WORKER instance assigned to the WORKER role in the Kronika project. This is one bounded implementation exchange. You implement the approved repository hardening bundle, validate it, and return one terminal report. You do not publish, deploy, contact the host, change dependencies, or close the logical whole.

## Identity and route

Persistent role identity: WORKER
Logical whole identity: nuc-security-hardening
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: NSH-IMPL-05 — repository hardening bundle for the NUC boundary
Delivery route: Cooperator manual selection and paste into a fresh Cursor session. The Orchestrator does not dispatch.
Reasoning recommendation: high. Basis: privileged boundary-recovery helper, security-sensitive systemd directives, and a retention ledger re-pin.
Recommended context capacity: approximately 250k tokens.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 8c58a81234a97fdf5af9d724a3b526f19745d32a
Changed-path allowlist: exactly these 18 paths
  deploy/systemd/kronika.service
  deploy/systemd/kronika-catalog-backup.service
  scripts/operator/security/kronika_nuc_boundary_rollback.sh
  tests/contract/test_nuc_hardening_rollback.py
  tests/contract/test_fedora_systemd_service.py
  tests/contract/test_catalog_backup_timer.py
  tests/contract/test_nuc_release_docs.py
  tests/contract/test_nuc_operator_runbook.py
  tests/contract/test_kronika_identity_retention.py
  docs/NUC_SECURITY_HARDENING.md
  docs/UBUNTU_NUC_DEPLOYMENT.md
  docs/UBUNTU_NUC_CLEAN_INSTALL.md
  docs/OPERATOR_NETWORK.md
  docs/BACKUP_AND_RECOVERY.md
  README.md
  ROADMAP.md
  SECURITY.md
  SERVER.md
Implementation boundaries: repository writes only inside the allowlist; exactly one local commit on `main`; no push, tag, branch, worktree, amend, rebase, or submodule change; no host contact or host command; no dependency, lockfile, AP, ADR, migration, capture/off-device unit, credential-template, release-helper-behavior, or frozen-byte change.
Independence required: no. This is non-independent implementation evidence; a fresh independent candidate review follows as row 05V.

## Accepted decisions

- The Cooperator approved plan 01/02 and row 05 on 2026-10-30.
- Two Orchestrator corrections apply: the retention test is in the allowlist with a measured re-pin; the commit is one local commit on `main`, not a task branch.
- D1–D8 remain deferred to rows 09–12 and do not belong in this task.
- CUPS is already disabled as a snap, capture is already disabled, and Tailscale is 1.104.4 on the host. These are context, not repository work.
- Preserve ADR-0085 frozen objects and hashes, the deferred publication-media path, tailnet-only ingress, disabled Research, and the existing capture/off-device sources.

## Verified starting state

- Repository: `/home/agile/Projects/kronika`, branch `main`, HEAD `8c58a81234a97fdf5af9d724a3b526f19745d32a`, working tree clean, public `origin/main` equal at the same SHA when last observed.
- AP pin and checkout: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `ap doctor` PASS.
- Carried baselines, not re-measured by the Orchestrator: full Python `4765 passed, 8 skipped, 3 warnings, 0 failed`; retention module 15; JS suites 23/41/55/6/12/30; bounded JS glob 216. Re-measure the baselines this task actually exercises and declare every movement.
- Canonical execution route: `./.ap/ap project check --root /home/agile/Projects/kronika --baseline 8c58a81234a97fdf5af9d724a3b526f19745d32a`; `./.ap/ap exec --root /home/agile/Projects/kronika --baseline 8c58a81234a97fdf5af9d724a3b526f19745d32a --operation runtime-info`; `--operation test-focus -- <tests> -q -p no:cacheprovider`; `--operation test` for the full suite.
- Host context, already achieved and not to be changed here: Tailscale 1.104.4, Serve tailnet-only to `unix:/run/kronika/kronika.sock`; CUPS snap disabled; capture runner/bridge/Xvfb disabled; running kernel 6.8.0-146.146 with 147.147 installed and a reboot pending; backup readiness `ready`.

## Goal

Implement the approved repository hardening bundle: harden the web and local-backup unit sources, add the reviewed boundary-recovery helper and its synthetic contract test, update the affected contract tests and living documentation, re-pin the measured retention counts, and produce exactly one local commit on `main`.

## Required unit changes

Preserve every existing directive and behavior unless a change below requires otherwise. Add to the `[Service]` section of `deploy/systemd/kronika.service`:

- `PrivateDevices=true`
- `ProtectHostname=true`
- `ProtectClock=true`
- `ProtectKernelLogs=true`
- `RestrictNamespaces=true`
- `RestrictRealtime=true`
- `SystemCallArchitectures=native`
- `CacheDirectoryMode=0700`
- `RuntimeDirectoryMode=0750`
- `RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6`
- `SystemCallFilter=~@clock @module @mount @raw-io @reboot @swap`
- `SystemCallErrorNumber=EPERM`

Add to the `[Service]` section of `deploy/systemd/kronika-catalog-backup.service`:

- `PrivateDevices=true`
- `ProtectHostname=true`
- `ProtectClock=true`
- `ProtectKernelLogs=true`
- `RestrictNamespaces=true`
- `RestrictRealtime=true`
- `SystemCallArchitectures=native`
- `RestrictAddressFamilies=AF_UNIX`
- `IPAddressDeny=any`
- `InaccessiblePaths=/srv/media`
- `SystemCallFilter=~@clock @module @mount @raw-io @reboot @swap`
- `SystemCallErrorNumber=EPERM`

Do not add web `MemoryDenyWriteExecute`, `PrivateUsers`, `RemoveIPC`, or `ProcSubset`. Do not add a repo-level publication write path; the host drop-in `30-publication-write-path.conf` remains the deliberate exception. Do not change capture or off-device units. Do not change the release helper or its behavior.

The unit syntax must be valid for the systemd version expected on Ubuntu 24.04 (`255.x`). Validate with `systemd-analyze verify` in the local environment when available; if unavailable or if it reports only missing-executable warnings caused by the workstation, record the limitation and rely on the contract test plus row 08 host validation. Do not invent a host validation.

## Required recovery helper

Create `scripts/operator/security/kronika_nuc_boundary_rollback.sh` with this fixed operator interface:

- Operations: `snapshot`, `verify`, `restore`.
- Surfaces: `ufw` or `sshd`.
- Installed runtime target: `/usr/local/libexec/kronika/nsh-boundary-rollback`.
- Default root-only recovery state: `/var/lib/kronika-host-hardening`.
- UFW surface files: the exact persistent user-rule files the UFW cut modifies, `/etc/ufw/user.rules` and `/etc/ufw/user6.rules`.
- SSH surface files: the exact drop-ins the SSH cut will modify, `/etc/ssh/sshd_config.d/00-kronika-hardening.conf` and `/etc/ssh/sshd_config.d/50-cloud-init.conf`.
- The helper may not accept arbitrary file paths, snapshot host keys, profiles, credentials, or unrelated configuration.

Required behavior:

- Bash, `set -euo pipefail`, private umask.
- Refuse symlinks, non-regular files, unexpected owners or modes, missing surfaces, stale or conflicting snapshots, and concurrent operations; fail closed with a nonzero exit and one first causal message.
- Snapshot exact bytes, mode, owner, group, and SHA-256 into root-only state, preserving the relative surface path.
- Verify the snapshot against the recorded metadata without modifying live files.
- Restore only the exact recorded surface files, with exact bytes and metadata; never recursive chmod, wildcard deletion, or path expansion.
- Use a non-blocking lock under the state root; a held lock is a conflict, not a retry loop.
- A test-only surface-root override is permitted so the contract test can exercise synthetic files without touching `/etc`; the installed default must be `/`, and the override must be rejected when it is not an existing private directory with safe ownership and mode.
- No network, no `sudo`, no service restart, no reboot, no package command.
- The helper is installed only in row 08; this task writes and tests the source.

## Required tests and contract updates

- New `tests/contract/test_nuc_hardening_rollback.py`: exercise snapshot, verify, and restore against synthetic files in a temporary root. Cover absent and present files, unsafe paths, symlinks, unexpected owner/mode, stale or conflicting state, exact restoration, lock conflict, and first-failure preservation. Do not require root and do not touch `/etc`.
- Update `tests/contract/test_fedora_systemd_service.py` and `tests/contract/test_catalog_backup_timer.py` for the new directives and preserved existing ones.
- Update `tests/contract/test_nuc_release_docs.py` and `tests/contract/test_nuc_operator_runbook.py` for the new documentation and any exact command/link assertions.
- Update `tests/contract/test_kronika_identity_retention.py` only by a measured Part C re-pin. Part A must remain byte-unmoved; Part B must remain empty; re-pin only from the measured failure with its arithmetic cause. Never pre-write expected counts and never edit a frozen hash.

## Required documentation

Create `docs/NUC_SECURITY_HARDENING.md` with classification, consumers, retention, and update owner, and cover:

- Scope and non-goals: host boundary hardening; no dependency/relock work, no frozen-runtime replacement, no capture activation, no provider or media access.
- The selected unit settings and why they are staged separately from host activation.
- The recovery helper interface, installed path, state root, refusal rules, and operator flow: console and session baseline, snapshot, verify, arm the independent rollback timer, apply one cut, prove fresh authentication and denial, cancel only after every gate.
- Proof design: unit syntax, effective settings, socket `0600`, runtime `0750`, cache `0700`, synthetic SQLite/media/preview workloads, local stubs for outbound compatibility, backup network isolation, actual scheduled backup success, post-boot matrix.
- Rollback and lockout prevention, including the rule that the timer must work without SSH, DNS, Tailscale, or a sudo timestamp.
- Residual risks and the deferred decisions D1–D8.
- A clear distinction between repository source and host acceptance; do not claim host hardening is complete.
- Links to the deployment, clean-install, backup, and operator-network runbooks; link to existing frozen-residue explanations instead of duplicating frozen-name inventories.

Update `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/UBUNTU_NUC_CLEAN_INSTALL.md`, `docs/OPERATOR_NETWORK.md`, and `docs/BACKUP_AND_RECOVERY.md` only where the new unit settings, helper, or host-activation boundary changes their truth. Update `README.md` with the documentation-map link. Update `ROADMAP.md`, `SECURITY.md`, and `SERVER.md` only for the NUC hardening status and residual risks. Do not fix the unrelated `kronika-sole-identity` closed-whole table omission in `ROADMAP.md`; that is a separate finding.

## Validation and baseline discipline

Use only the canonical AP Python route; never `python`, `python3`, `.venv/bin/python`, or `poetry run`. Do not install, upgrade, relock, or reconstruct any environment.

Required sequence:

1. `ap project check` and `runtime-info` against the exact baseline.
2. Focused runs while implementing: the two unit contract modules, the two release/runbook modules, the new helper test, and the retention module.
3. The retention module must show the measured failure caused by the new or changed documentation; re-pin Part C with the arithmetic cause. Part A must remain byte-unmoved; Part B empty.
4. The full Python suite through `--operation test`. Declare the exact new counts and explain every movement from `4765/8/3/0`.
5. JavaScript: no JS file is in the allowlist. State the carried JS baselines and that they were not rerun because no JS changed. If you nevertheless run the declared glob, report the exact counts.
6. `bash -n` on the helper; `systemd-analyze verify` where available with the limitation stated.
7. Final `git status`, `git show --stat`, parent, one-commit range, changed-path list, and unchanged AP pin.

## Git

One local commit on `main`, exactly the allowlisted paths, no other files. Suggested subject: `Harden NUC service units and add boundary recovery helper`. Do not amend, rebase, push, tag, create a branch, or touch the `.ap` submodule. Verify the commit's parent is the exact baseline, the range is one commit, the changed paths equal the allowlist subset you actually needed, the worktree is clean afterward, and the AP pin is unchanged. If a required change falls outside the allowlist, stop and report instead of widening the commit.

## Authority

Positive: read and write only the 18 allowlisted repository paths; run the canonical AP Python route; run `node --test` only if a JS file were changed (none is expected); make one local commit on `main`.

Negative: no other repository path; no host contact, SSH, sudo, service action, probe, reboot, or firewall/sshd change; no push, publication, deployment, or refresh; no dependency, lockfile, `pyproject.toml`, `uv`, Poetry, or `.venv` change; no AP, ADR, migration, frozen-document, credential-template, capture/off-device unit, or release-helper-behavior change; no provider call, credential use, browser, capture, media, or personal configuration access; no Meta trace write; no acceptance or closure claim.

## Mandatory reading

- `AGENTS.md`.
- `.ap/AP.md`: RF-03, RF-06, RF-12, RF-16, RF-18; §8; §12; §18.
- `.ap/AP_WORKER.md`: Worker Session Target; Reporting.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Common Worker Task Fields; Implementation Authority Record; Owner-Executed Command Contract.
- `docs/WORKER_EXECUTION_CONTRACT.md`.
- `deploy/systemd/kronika.service`, `deploy/systemd/kronika-catalog-backup.service`, and the other unit sources for context.
- `deploy/ubuntu/kronika-release`, `deploy/ubuntu/kronika_release.py`, and the release contract tests that define what routine deployment may not do.
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/UBUNTU_NUC_CLEAN_INSTALL.md`, `docs/BACKUP_AND_RECOVERY.md`, `docs/OPERATOR_NETWORK.md`, `docs/NUC_HOST_BASELINE.md`.
- The five named contract-test modules and the retention module.
- `ROADMAP.md`, `SECURITY.md`, `SERVER.md`, and ADRs 0032, 0052, 0058, 0075, 0085.

## Derivation and verification discipline

Apply the ten derivation and verification rules from the approved plan wherever the task touches inventories, pins, counts, or evidence tables: parse artifacts rather than prose; resolve cited lines; treat fixtures as fixtures; verify occurrences independently; reject broad regex pins; disclose truncation; use impossible-member controls; regenerate tables at report time; classify hits; and state when a demonstration cannot exist.

## Stopping conditions

Stop and report without improvisation when:

- a required change falls outside the allowlist;
- the exact baseline, clean tree, AP pin, or public identity does not match;
- the retention Part A hash or Part B state moves;
- a test failure is caused by the candidate and cannot be fixed inside the allowlist;
- the selected systemd directives are unsupported or unverifiable in the available environment;
- the helper cannot meet the interface without a host action or an out-of-allowlist file;
- an environment defect requires reconstruction;
- any instruction would cross the negative authority.

## Report contract

Start exactly:

### Report for ORCHESTRATOR_CHAT

Echo `nuc-security-hardening`, session `02`, exchange `01`. State status (`PASS`, `PARTIAL`, or `BLOCKED`), phase-qualified result `not-applicable`, logical-whole closure `not-closed`, report justification `new-mutation`. Include:

- summary and exact commit identity;
- changed paths and one-commit range;
- exact unit directives added and preserved;
- helper interface, refusal design, and test coverage;
- documentation changes and links;
- retention Part A/B/C before/after with the arithmetic cause;
- focused, full-suite, retention, and JS validation counts with movements explained;
- host impact: none; row 08 activation and rows 09–10 network cuts remain future;
- deviations, risks, missing evidence, and pre-existing failure classification;
- smallest next step (fresh independent candidate review, row 05V);
- `Orchestration critique:` with `MEASURED:` and `LEAD:` lines.

Deliver the report in chat only; write no files outside the allowlisted repository changes. Your authority expires at this terminal report. The Orchestrator archives the prompt/report pair and reconciles the candidate; the commit is not accepted or published by this task.