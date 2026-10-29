# Authoritative Worker prompt — Worker session 42, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `42`, exchange `01`. Stored under the
Meta filename mapping as `42_correction_00.md`, with report destination
`42_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 42
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6COMP — complete the C6 ingress and environment corrections
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The first live C6 identity-migration window surfaced three
independent defects in one subsystem, `deploy/ubuntu/kronika_release.py`: the
Tailscale ingress guard accepts only one of the two spellings its own classifier
treats as the former handler; the replacement target it generates is rejected by
the installed Tailscale; and the canonical environment file is installed without
the ownership/mode parity the operational helper routes require. Each fix must
be exact, must not weaken a fail-closed property, and must be proven by
round-trip and mutation tests.

## The findings, exactly

The live host was already completed manually; the engine was **not** the path
that finished it. The live evidence is recorded here in full so no host contact
is needed. Do not contact the NUC.

**D-1 — Ingress guard accepts only one of the two classified former-handler
spellings.**

`RemoteMigrationHost.replace_tailscale_handler` (`deploy/ubuntu/kronika_release.py`)
guards with:

```python
if targets[index] != tailscale_unix_target(self.plan.old_layout.socket_path):
    raise ReleaseError(
        "existing ingress handler target is unexpected", EXIT_MIGRATION
    )
```

`tailscale_unix_target(socket_path)` returns `unix+http://<socket>`. In contrast,
`parse_tailscale_serve_status` classifies **both** `unix+http://<old-socket>` and
`unix:<old-socket>` as former handlers. On the live host the former handler was
`unix:/run/framenest/framenest.sock`; the preflight classified it correctly as
the single former handler, and the apply then refused at phase
`replace-tailscale-handler` — **after** `start-service`, so post-write — with
`existing ingress handler target is unexpected`. The journal recorded
`outcome: failed`, the durable writes boundary, and completion through
`start-service`.

Required behavior: the guard must accept exactly every spelling the classifier
classifies as the former handler, and nothing else. Exactly-one-former-handler
uniqueness and the zero-handler no-op stay unchanged.

**D-2 — The generated replacement target is rejected by the installed
Tailscale.**

`tailscale_unix_target` always renders `unix+http://<path>`, and
`cmd_remote_tailscale_replace` runs `sudo -n tailscale serve --bg <target>`. The
live retry with that form was rejected by the host's Tailscale:

```text
must be a URL starting with one of the supported schemes: [http https https+insecure unix]
```

(`SERVE_EXIT=1`, handler unchanged.) The host's own spelling is `unix:<path>`,
which the repository deployment guide also uses in its Serve activation step.
The manual replacement `sudo -n tailscale serve --bg
unix:/run/kronika/kronika.sock` succeeded (`SERVE_EXIT=0`), and
`tailscale serve status --json` now reports `Proxy` =
`unix:/run/kronika/kronika.sock`. `verify_ingress` already accepts both new
spellings.

Required behavior: the replacement target must mirror the scheme form of the
observed former handler — `unix:<old>` → `unix:<new>`, and
`unix+http://<old>` → `unix+http://<new>`. One source of truth for the accepted
spellings, shared by classification, the guard and the verifier. Never
`tailscale serve reset`.

**D-3 — The canonical environment file is installed without ownership/mode
parity.**

`RemoteMigrationHost.transform_environment` writes `{destination}.next` through
`cmd_remote_write_file` (`umask 077`), asserts canonical-only assignments on the
staged bytes, then moves the file into place with `sudo -n mv -T`. No ownership
or mode is applied or verified. The live result was
`/etc/kronika/kronika.env` = `0600 root:root`. The former file was directly
observed in the C-DATA-H window as `0640 root:framenest` — readable by the
service account. The operational helper runs service-account routes as the
layout account with `FRAMENEST_ENV_FILE` pointing at that file
(`service_account_prefix`); with the file unreadable by the account,
`framenest-db status` returned

```json
{"operation":"status","state":"error","error_code":"FRAMENEST_DB_CONFIGURATION_FAILED","message":"Kronika configuration could not be loaded."}
```

and `kronika-release status` exited 20. After the manual remediation
(`chown root:kronika`, `chmod 0640`) the status command is green:
`layout: new`, `service_active: active`, `database_revision: 0035`,
`backup_restore_readiness: ready`, exit 0. So with the engine as it stands, even
a fully “successful” migration leaves the documented operational surface broken
on the new layout. This is a functional defect, not cosmetics: the service
itself reads the file through systemd as root and is unaffected.

Required behavior: the migrated environment file must have parity with the
former file as read by the former account — same owner and mode, with a group
that named the former service account mapped through the identity transition
(live shape `root:framenest:0640` → `root:kronika:0640`). The former file's
owner/group/mode evidence is gathered during the observation and carried as a
bound plan fact, the mapped ownership is applied after the atomic move, and the
installed file is then verified by evidence (owner:group:mode plus content
digest). Absent, unsafe (non-regular/symlink) or `query-failed` evidence, and
any post-install evidence mismatch, fail closed with `EXIT_MIGRATION`.

## Correction specification

1. **D-1.** Introduce one shared accepted-spelling source of truth for the
   former-handler and new-handler target spellings; use it in
   `parse_tailscale_serve_status`, in the `replace_tailscale_handler` guard and
   in `verify_ingress`. The guard accepts exactly the former-handler spellings
   of the plan's old socket and refuses everything else. Keep the existing
   refusal message, `EXIT_MIGRATION`, the uniqueness rule and the zero-handler
   no-op return shape `{"replaced": 0, "handler_count": 0}`.
2. **D-2.** Generate the replacement target by mirroring the observed former
   handler's spelling with the new socket path. Keep `cmd_remote_tailscale_replace`
   and its `:443/` mount guard, keep `--bg`, keep the return shape
   `{"replaced": 1, "handler_count": ...}`, and keep `verify_ingress` accepting
   both new spellings. Recommended: derive the mirroring from the observed
   target string; if you derive a different mechanism, prove the same matrix.
3. **D-3.** Observe the former environment file's owner/group/mode evidence in
   `read_migration_observation` (reuse the existing root-file evidence command
   and its absent/unsafe/query-failed classification); carry it through
   `MigrationObservation`/`MigrationPlan` as a bound fact; after the atomic move
   in `transform_environment`, apply the mapped ownership and mode and verify
   the installed evidence (owner:group:mode and digest) before reporting
   success. Recommended: a small pure mapping helper (owner preserved, former
   account group mapped, mode preserved, anything unmappable fails closed) so
   the transition is unit-testable; derive your own if you can prove the same
   matrix. Keep the canonical-only assertion message and exit code, and keep the
   atomic write-and-move behavior.
4. **No other behavior change.** The apply sequence, phase names, journal and
   receipt shapes, recovery semantics, and all other commands stay as they are.
   No new dependencies. Do not touch docs; if you find a repository document
   that contradicts the corrected behavior, report it instead of editing it.

## Verified starting state, measured by the Orchestrator on 2026-10-11

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                fcde631047650d1ff0a84b84bf185b54d6d11ba5
Public main:                  fcde631047650d1ff0a84b84bf185b54d6d11ba5, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at fcde631:   4901 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     231 passed
Retention module:             15 passed
```

**No host contact.** All work and tests are repository-only with synthetic
fixtures. The live host supplied the failure evidence and was completed
manually; the corrected engine must reproduce the intended end state in tests,
not be re-run on the host.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  three corrections D-1, D-2 and D-3; edit
  `tests/contract/test_kronika_identity_migration.py` for the boundary model,
  tests and mutation demonstrations; edit any other test module you derive as
  directly exercising a changed command, naming it in the report before editing
  it; edit `tests/contract/test_kronika_identity_retention.py` only to re-pin a
  Part C scalar that your own measurement shows this correction moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on `main`.

Negative authority: every other path; any document; any dependency or lockfile
  change; any change to `pyproject.toml`, `ap.project.conf` or the `.ap`
  gitlink; any frozen document or Alembic revision; publication; push; force;
  amend; branch; stash; any NUC contact or SSH; any migration invocation; any
  provider, browser or capture contact; any secret or personal-configuration
  read. If a necessary change falls outside the positive scope, stop and report;
  do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. Read-only Git inspection allowed; exactly one `git add <exact paths>`
  and one `git commit`; no push.

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

1. Reproduce each defect shape before editing, through the real remote-command
   builders and the fake boundary: (a) a single former handler in the `unix:`
   spelling is refused by the guard; (b) the generated replacement command
   carries the `unix+http://` spelling; (c) `transform_environment` installs no
   ownership/mode parity and the live-shaped evidence (`root:framenest:640`)
   has no install or verification step.
2. Post-fix matrix for D-1 and D-2: former handler `unix:<old>` → exactly one
   `tailscale serve --bg unix:<new>` and result `{"replaced": 1, ...}`; former
   handler `unix+http://<old>` → exactly one `tailscale serve --bg
   unix+http://<new>`; a foreign target → fail closed; two former handlers →
   fail closed; zero handlers → no-op; never `reset`. Verify the classifier, the
   guard and `verify_ingress` agree on the accepted spelling sets.
3. Post-fix matrix for D-3: live shape `root:framenest:640` → install applies
   `root:kronika` + `640` and verifies evidence; a non-account group shape (for
   example `root:root:640`) is preserved exactly and never widened; absent,
   unsafe and `query-failed` former-file evidence → fail closed; a post-install
   evidence mismatch → fail closed. State exactly which evidence bytes the plan
   is bound to and how the digest of the staged content is verified.
4. Mutation demonstrations, each named with its observed failure:
   (a) restore the old `unix+http://`-only guard comparison → the `unix:`
   former-handler test fails with the spurious refusal; (b) restore the fixed
   `unix+http://` replacement target → the mirroring test fails; (c) remove the
   ownership/mode application or its verification → the D-3 parity test fails.
5. Run, through the declared route: the focused migration module, then the
   declared full Python suite, then the retention module. Report every count,
   elapsed time and any difference from the `4901/8/3/0`, `231` and `15`
   baseline.
6. Report **every moved or removed site that no test exercises**, and every
   caller or boundary branch your derivation found that this prompt did not
   name.
7. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until a suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the affected callers and boundary branches by PARSING the engine and
    its tests. Locators are not an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** The accepted spellings must not collapse in either
direction: a `unix:` former handler must never read as foreign, and a foreign
target must never read as an accepted former handler. The environment-file
classification must not collapse: absent, unsafe and `query-failed` evidence
must each stay distinguishable from a valid evidence value, and the mapped
ownership must never silently widen access.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a correction would weaken any fail-closed property; if the
  classifier, guard and verifier can disagree on an accepted spelling; if a
  frozen hash, Part A or Part B moves; if a Part C re-pin cannot be reproduced
  from your own measurement; if a necessary change falls outside the positive
  scope.

Completion: the three corrected behaviors with their matrices and mutation
  demonstrations; focused module, full declared Python suite and retention
  module green through the declared route; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `42_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `42` and exchange `01` unchanged. Then:

1. The three reproduced baseline misfires and the corrected outcomes.
2. The changed function texts as implemented, with the guard/target spelling
   matrix and the environment parity matrix.
3. Mutation demonstrations, each with its named mutation and observed failure.
4. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and
   Part C movement with cause.
6. Every site no test exercises.
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

- `deploy/ubuntu/kronika_release.py` —
  `parse_tailscale_serve_status`, `tailscale_unix_target`,
  `cmd_remote_tailscale_replace`, `RemoteMigrationHost.replace_tailscale_handler`,
  `verify_ingress`, `read_migration_observation`, `build_migration_plan`,
  `transform_environment`, `cmd_remote_write_file`, `cmd_remote_root_file_evidence`,
  `service_account_prefix`.
- `tests/contract/test_kronika_identity_migration.py` — the fake boundary and
  the ingress/environment tests.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the Serve activation section, reading only.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md`
  tail — the live failure evidence and host state.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the three matrices;
the unchanged fail-closed semantics for genuine failures; agreement of the
classifier, guard and verifier on accepted spellings; the environment-file
parity including non-widening; the full suite green at the reported commit; and
Part A and Part B unmoved. **A fresh independent re-audit follows**; the live
host already reflects the intended end state achieved manually, and only after
the re-audit's PASS may the failed C6 journal be archived.
