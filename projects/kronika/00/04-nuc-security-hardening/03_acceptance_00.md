You are a WORKER instance assigned to the WORKER role in the Kronika project. This is one bounded independent acceptance review. You review the exact candidate read-only and return one terminal report. You do not correct, commit, push, publish, deploy, contact the host, or close the logical whole.

## Identity and route

Persistent role identity: WORKER
Logical whole identity: nuc-security-hardening
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Task identity: NSH-REVIEW-05 — independent acceptance of the row 05 hardening candidate
Delivery route: Cooperator manual selection and paste into a fresh Cursor session. The Orchestrator does not dispatch.
Reasoning recommendation: high. Basis: security-sensitive unit directives, a privileged recovery helper, and a retention ledger re-pin.
Recommended context capacity: approximately 250k tokens.

Independence declaration required: you did not participate in the implementation, you have no session 02 context, and you are a genuinely fresh session. State this explicitly. If you have any prior participation in this candidate, stop and report the conflict instead of reviewing.

## Acceptance record

Acceptance candidate: 8cbbcad947964d711ebc2001e1c80976c4f82e24
Acceptance owner map: the approved plan 01/02 row 05 selected settings and helper interface, the 18-path allowlist, and repository truth at the candidate.
Acceptance allowlist: exactly the 18 paths listed below.
Acceptance risk claims: unit-directive correctness and preservation; helper security, refusal behavior and exact restoration; meaningful test coverage; retention arithmetic; documentation truth and scope; no host impact; one local commit with unchanged AP pin.
Acceptance control matrix: the commands and expected results in this prompt.
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

## Candidate and starting state

- Repository: `/home/agile/Projects/kronika`, branch `main`, HEAD `8cbbcad947964d711ebc2001e1c80976c4f82e24`.
- Parent and expected baseline: `8c58a81234a97fdf5af9d724a3b526f19745d32a`.
- Local `main` is one commit ahead of the last observed public `main`; public `main` must still be `8c58a81…` when you check it read-only.
- AP pin and checkout: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- Allowlist, exactly:
  README.md
  ROADMAP.md
  SECURITY.md
  SERVER.md
  deploy/systemd/kronika-catalog-backup.service
  deploy/systemd/kronika.service
  docs/BACKUP_AND_RECOVERY.md
  docs/NUC_SECURITY_HARDENING.md
  docs/OPERATOR_NETWORK.md
  docs/UBUNTU_NUC_CLEAN_INSTALL.md
  docs/UBUNTU_NUC_DEPLOYMENT.md
  scripts/operator/security/kronika_nuc_boundary_rollback.sh
  tests/contract/test_catalog_backup_timer.py
  tests/contract/test_fedora_systemd_service.py
  tests/contract/test_kronika_identity_retention.py
  tests/contract/test_nuc_hardening_rollback.py
  tests/contract/test_nuc_operator_runbook.py
  tests/contract/test_nuc_release_docs.py
- Carried baselines before the candidate: full Python `4765 passed, 8 skipped, 3 warnings, 0 failed`; retention 15; JS `23/41/55/6/12/30`; bounded JS glob 216. The implementer claims `4822/8/3/0`, retention 15, helper 54, focused 151. Verify independently.

## Fixed claims to verify

C1. The candidate is exactly one local commit on `main`, parent `8c58a81…`, 18 changed paths equal to the allowlist, AP pin unchanged, worktree clean, no push, and public `main` still `8c58a81…`.
C2. `deploy/systemd/kronika.service` adds exactly `PrivateDevices=true`, `ProtectHostname=true`, `ProtectClock=true`, `ProtectKernelLogs=true`, `RestrictNamespaces=true`, `RestrictRealtime=true`, `SystemCallArchitectures=native`, `CacheDirectoryMode=0700`, `RuntimeDirectoryMode=0750`, `RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6`, `SystemCallFilter=~@clock @module @mount @raw-io @reboot @swap`, `SystemCallErrorNumber=EPERM`; preserves every pre-existing line; adds no excluded directive and no repo-level publication write path.
C3. `deploy/systemd/kronika-catalog-backup.service` adds the common directives plus `RestrictAddressFamilies=AF_UNIX`, `IPAddressDeny=any`, `InaccessiblePaths=/srv/media`; preserves every pre-existing line; adds no excluded directive.
C4. Capture units, off-device units, release-helper behavior, credential templates, `pyproject.toml`, `poetry.lock`, AP, ADRs, migrations, and frozen documents are untouched.
C5. `scripts/operator/security/kronika_nuc_boundary_rollback.sh` implements exactly `snapshot|verify|restore` for `ufw|sshd`, fixed surface paths, root-only default state, exact byte/mode/owner/group/SHA-256 recording, symlink/hardlink/unsafe-path refusal, non-blocking lock, incomplete/conflicting state refusal, preflight-before-restore, exact restoration, and one causal error message. The test-only root override must not weaken the installed default.
C6. The 54 helper tests actually exercise those behaviors; foreign-owner and copy-failure branches are honestly labelled fixtures, not host proof.
C7. The retention re-pin is measured: Part A byte-unmoved, Part B empty, Part C values match the independent counts and the new doc is the sole content-path addition; no frozen hash changed.
C8. The unit/runbook/release/retention contract tests are meaningfully updated; the new documentation is classified, scoped, linked, and does not claim host acceptance or whole completion; the ROADMAP edit does not fix the unrelated `kronika-sole-identity` table; SECURITY/SERVER state residual risk without overclaim.
C9. The reported validation counts are reproducible: focused 151, helper 54, retention 15, full Python 4822/8/3/0; no JS changed.
C10. The candidate has no host impact and no out-of-allowlist effect.

## Control matrix

Read-only Git and source checks:

- `git rev-parse HEAD`, `git log --oneline -3`, `git status --porcelain=v1 --branch`.
- `git diff --name-status 8c58a81…..HEAD` and `git diff --stat`; compare with the allowlist and the report's 18 paths and 1089/7.
- `git ls-tree HEAD .ap` and `git submodule status`; expect `73e20ef8…`.
- `git show HEAD:deploy/systemd/kronika.service` and the backup unit; `git grep` for excluded directives.
- `git diff 8c58a81…..HEAD -- tests/contract/test_kronika_identity_retention.py`; inspect every Part C change and the absence of Part A edits.
- `git diff 8c58a81…..HEAD -- docs/ README.md ROADMAP.md SECURITY.md SERVER.md`; review scope, links, and claims.
- `git show HEAD:scripts/operator/security/kronika_nuc_boundary_rollback.sh`; read the whole script, not only the test.
- `bash -n scripts/operator/security/kronika_nuc_boundary_rollback.sh`.
- `git ls-remote --heads origin main` (read-only; no fetch).
- `systemd-analyze verify` on the two candidate units in the local environment; record that the host is Ubuntu systemd 255 and this is only local syntax evidence.

Canonical execution route (exact baseline `8c58a81…`; the worktree is the candidate):

- `./.ap/ap project check --root /home/agile/Projects/kronika --baseline 8c58a81…`.
- `./.ap/ap exec --root /home/agile/Projects/kronika --baseline 8c58a81… --operation runtime-info`.
- Focused six modules: `test_fedora_systemd_service.py`, `test_catalog_backup_timer.py`, `test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_nuc_hardening_rollback.py`, `test_kronika_identity_retention.py`, each `-q -p no:cacheprovider`.
- Full suite: `--operation test`.
- Independent retention counts using the repository's declared methods; do not trust the report's table.

Security review of the helper:

- Trace every shell path expansion, `stat`, `realpath`, `stat -c`, `find`, `sha256sum`, lock, and restore operation.
- Confirm no arbitrary path enters from the operator, no surface outside the fixed lists, no wildcard deletion, no recursive chmod, no symlink follow, no hard-link acceptance, no uncontrolled temporary file.
- Confirm the test-root override is bounded to a private synthetic root and cannot silently become a production surface.
- Assess the reported residual limitations: privileged pathname races, partial multi-file restoration, transient rollback-timer loss on reboot, and the publication write exception. Classify each as acceptable residual, minor finding, or blocking.

## Findings format

For each finding:

Finding ID:
Severity: blocking | major | minor | observation
Claim or surface:
Evidence: exact path, line, command, or output
Effect:
Smallest correction: what the Orchestrator could authorize; do not apply it yourself

Out-of-scope observations become ledger candidates and must not expand the audit.

## Authority

Positive: read-only repository inspection; the canonical AP Python route; the named tests and full suite; `bash -n`; `systemd-analyze verify`; read-only `git ls-remote`; reading the candidate and its evidence.

Negative: no Git writes, commit, push, branch, tag, or worktree change; no file writes; no correction; no host contact, SSH, sudo, probe, service action, or reboot; no dependency, environment, AP, ADR, migration, or frozen-byte change; no provider, credential, browser, capture, media, or personal-configuration access; no Meta write; no acceptance or closure signal by the reviewer.

## Mandatory reading

- `AGENTS.md`.
- `.ap/AP.md`: RF-05, RF-07, §12, §18, Acceptance/Correction/Escalation, Phase-Qualified Results.
- `.ap/AP_WORKER.md`: Reporting.
- `.ap/PROMPT_CONTRACTS.md`: Acceptance and Correction Record; Worker Report Header; Security Finding and Audit Contracts.
- `docs/WORKER_EXECUTION_CONTRACT.md`.
- The exact candidate diff and the whole helper source.
- The two unit sources, the five contract modules, the new hardening contract, and the four runbooks.
- `ROADMAP.md`, `SECURITY.md`, `SERVER.md`, ADRs 0032, 0052, 0058, 0075, 0085.

## Derivation discipline

Apply the ten derivation and verification rules: parse artifacts, resolve literal lines, treat fixtures as fixtures, verify independently, avoid broad regex pins, disclose truncation, use impossible-member controls, regenerate tables at report time, classify hits, and state when a demonstration cannot exist.

## Stopping conditions

Stop and report without correcting when:

- the candidate, parent, allowlist, AP pin, or public main does not match;
- an out-of-allowlist or frozen change appears;
- a test fails or a reported count does not reproduce;
- the helper has a blocking security defect;
- a documentation claim is unsupported or overclaims host acceptance;
- the local environment cannot support a required check — record the limitation rather than manufacturing evidence;
- any instruction would cross the negative authority.

## Report contract

Start exactly:

### Report for ORCHESTRATOR_CHAT

Echo `nuc-security-hardening`, session `03`, exchange `01`. State status (`PASS`, `PARTIAL`, or `BLOCKED`), phase-qualified result (`acceptance-PASS` only if PASS, otherwise `not-applicable`), logical-whole closure `not-closed`, report justification `new-evidence`, and the independence declaration. Include:

- candidate identity and one-commit/allowlist verification;
- each fixed claim C1–C10 with verified/contradicted/unverifiable and evidence;
- helper security review and residual classification;
- retention arithmetic and independent counts;
- exact validation results with counts and any movement;
- findings in the required format;
- verdict and the smallest next step;
- `Orchestration critique:` with `MEASURED:` and `LEAD:` lines.

Deliver the report in chat only; write no files. Your authority expires at this terminal report. The Orchestrator reconciles the verdict; the reviewer does not accept, publish, deploy, or close the whole.