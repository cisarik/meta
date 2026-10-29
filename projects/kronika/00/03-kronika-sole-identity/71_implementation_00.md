# Authoritative Worker prompt — Worker session 71, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `71`, exchange `01`. Stored under the
Meta filename mapping as `71_implementation_00.md`, with report destination
`71_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C-INSTALL-DOC**: the clean-install / recovery runbook the Cooperator
requested, reframed under his decision that the live host keeps its current
identity (no live reinstall is planned). Documentation only.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 71
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-CINSTALL — the clean-install / recovery runbook
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The document must reconcile the final units, the release
helper, the settings contract, the frozen ADR-0085 exceptions and the
Cooperator's recorded decisions — without values, without scripts, and without
presenting instructions as a completed installation.

## Specification

Session-25 plan section 2.20 is the normative source, reframed by the
Cooperator's decision A (the host identity is retained; the runbook serves a
fresh or replacement host). Create exactly one new document,
`docs/UBUNTU_NUC_CLEAN_INSTALL.md`, and link it from the existing deployment
runbook and from the README Documentation Map. Documentation and
documentation-contract tests only.

The document must describe, professionally and without any secret or
host-specific values:

1. **From-scratch host**: Ubuntu NUC preparation, bootstrap toolchain versus
   routine updates (the frozen `/opt/framenest/tooling` Poetry 2.4.1 and
   CPython 3.13.14 paths are bootstrap and routine-tooling authority, and no
   routine update invokes `uv`), the canonical product account `kronika` and
   the canonical directory layout (`/opt/kronika`, `/etc/kronika`,
   `/var/lib/kronika`, `/var/cache/kronika`, `/run/kronika`), and the
   canonical host/tailnet naming for a fresh setup.
2. **Frozen exceptions, exact**: the encrypted protocol magic `FNCBE01`; the
   mount name `/mnt/framenest-catalog-offdevice`; the tooling paths above;
   the capture state-directory name `framenest-chatgpt-page` with no
   executable alias of that name. State that the live host retains its
   existing identity by the Cooperator's decision, and that a fresh setup
   chooses canonical naming.
3. **Units and install order**: the canonical units from
   `deploy/systemd/` (web, capture bridge/runner/xvfb/vnc/view, catalog backup
   and off-device timers), the credential drop-ins, the environment file, the
   ingress modes and the loopback-first posture; SSH reachable over the
   tailnet rather than a wired-only boundary (the recorded Wi-Fi decision).
4. **Read-only original media** under `/srv/media` and the distinct
   quarantine/publication/staging boundaries; never grant broad service write
   access to source media.
5. **Canonical web installation** through the sole release helper
   `deploy/ubuntu/kronika-release` (`status`, `check --release`, `deploy
   --release --yes`, `rollback --release --yes`, `activate-capture` only for
   capture code changes), including the same-schema boundary and the
   `migration-required` continuation.
6. **Backup scheduling and restore verification**: the catalog timers, the
   operator-state roots, retention, and the restore-readiness proof; the
   scheduled success is the requirement.
7. **Optional parked capture provisioning** without login or activation by
   default: the units, the credential source name, the frozen state name, and
   the explicit statement that capture stays parked.
8. **The two operator notes, without values**: the Cooperator's existing SSH
   identity filename still contains the retired spelling, and a fresh setup
   chooses an explicitly chosen canonical filename; the transport variables
   currently come from an exported user-dotfile configuration — do not claim
   universal-variable storage and do not prescribe two competing sources.
9. **Verification checkpoints and recovery references**: what to verify after
   each phase, and where the recovery instructions live; include the operator
   finding that ADR-0058's `recover` did not clear a stale Tailscale
   policy-table default route on the live host (the exact route was cleared
   separately) as a recovery caution — clearly historical.
10. **Documented versus completed**: the document states plainly that it is
    instructions for a future installation, not a receipt that an installation
    was performed.

Forbidden content: secret values, credentials, private media filenames,
host-specific identifiers or addresses, any installer script or generated
file, any provider activation or credential provisioning, any claim that
contradicts the frozen ADRs or the living documents. Review the result against
the final units, the helper and the settings; every command form must match
them; every link must resolve inside the repository.

## Verified starting state, measured by the Orchestrator on 2026-10-29

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                f6859362f64cf4b5d5ec7529785d53e1ad483969
Public main:                  f6859362f64cf4b5d5ec7529785d53e1ad483969 (published; NUC serves it)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4759 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 216
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no external calls.

## Authority

```text
Positive authority: create `docs/UBUNTU_NUC_CLEAN_INSTALL.md`; edit the
  deployment runbook and the README Documentation Map for the two links;
  create or extend documentation-contract test coverage for the new document
  (its presence, its links, its required sections), naming the module before
  editing; edit `tests/contract/test_kronika_identity_retention.py` to re-pin
  the scalars your own measured retention failure shows this document moved,
  with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; every frozen document; the ADRs;
  installer scripts or any executable artifact; any secret, credential,
  host-specific identifier or address; any provider activation; any settings,
  unit or helper change; any dependency or lockfile change; the `.ap`
  gitlink; any Alembic revision; any `.venv` operation; publication; push;
  force; amend; branch; stash; any host or browser action. If a necessary
  change falls outside the positive scope, stop and report; do not widen
  scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline f6859362f64cf4b5d5ec7529785d53e1ad483969 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed;
  exactly one `git add <exact paths>` and one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none.
```

## Verification

1. **Content matrix.** Each of the ten specification areas present; the
   frozen exceptions exact; no forbidden content anywhere in the document.
2. **Links.** Both links exist and resolve; no relative link is broken.
3. **Command forms.** Every command in the document matches the final helper,
   unit and settings sources; name any source you reconciled against.
4. **Contract tests.** The new document's presence, links and required
   sections are pinned; the docs-contract modules stay green; name the module.
5. **Measured retention re-pin.** The new document moves `docs` file and
   occurrence counts and any host-path or token scalars it legitimately names
   (frozen exceptions are allowed); measure the failure, re-pin with the
   arithmetic cause, and state the exact movement. Do not add counted tokens
   outside the documented frozen exceptions.
6. Run, through the declared routes: the docs-contract modules and the
   documentation-pin modules (named), the full declared Python suite against
   `4759/8/3/0`, the retention module, and the JS suites plus bounded glob as
   unaffected sanity.
7. Report every statement that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive every unit, command, path and setting by PARSING the sources, not
    from this prompt's prose.
 2. Resolve every cited path to its literal source BEFORE documenting it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each link independently.
 5. Never include a value the specification forbids. Redact by omission.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse bootstrap tooling with routine tooling;
do not collapse the frozen exceptions with retired spellings that must not
appear; do not collapse documented instructions with a completed installation.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a command or path cannot be reconciled against its source; if the
  document would need a value the specification forbids; if a frozen hash or
  Part A moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if context pressure reaches the point where a bounded rotation
  is cheaper than a degraded result.

Completion: the runbook with its ten areas, the two links, the contract pin,
the measured retention re-pin, and one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `71_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `71` and exchange `01` unchanged.
Then:

1. The content matrix (the ten areas) with the source reconciliation for each.
2. The link addition and the contract test pin, each named.
3. The measured retention re-pin with the arithmetic cause and the exact
   movement.
4. Suites: docs-contract modules, full Python, retention, JS sanity — counts,
   elapsed time, baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
6. Every statement no test exercises.
7. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `docs/UBUNTU_NUC_DEPLOYMENT.md` (the living runbook and its structure),
  `README.md` (the Documentation Map), `PRODUCT.md`, `SPEC.md`, `SERVER.md`,
  `SECURITY.md`, `DEVELOPMENT.md`.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  sections 2.20, 2.21 and 5 (the closure table).
- `deploy/ubuntu/kronika-release`, `deploy/ubuntu/kronika_release.py` (the
  helper and its command forms), `deploy/systemd/*`, `docs/BACKUP_AND_RECOVERY.md`,
  `docs/OPERATOR_NETWORK.md`.
- The frozen ADR list and `docs/adr/README.md`; ADR-0085, ADR-0075, ADR-0058,
  ADR-0084.
- The docs-contract test modules (derive by parse).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the document, the links, the contract
pin and the retention arithmetic at the reported commit, then arranges the
final publication, the routine refresh of the NUC to the resulting SHA, and
the read-only CLOSE reconciliation.
