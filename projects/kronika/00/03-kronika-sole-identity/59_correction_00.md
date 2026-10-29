# Authoritative Worker prompt — Worker session 59, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `59`, exchange `01`. Stored under the
Meta filename mapping as `59_correction_00.md`, with report destination
`59_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 59
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C8RELOC — parameterize the venv relocation's required console scripts
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The C8-A/H apply reached the shebang-relocation step on the
live host and was refused by a web-only requirement baked into a shared
helper: the relocation demands `kronika-db` and `kronika-backup` in the venv,
which a capture tree cannot provide. The correction must make the required
script set an explicit, validated input — derived per operation — while the
routine web deploy keeps emitting and enforcing exactly what it does today.

## The finding, exactly

Live evidence (PC-side ssh log of the second apply, 2026-10-16 20:51:53):

```text
sudo -n python3 /run/kronika-capture-path-migration/kronika_release.py _remote _remote-relocate-venv-shebangs \
  --staging /opt/kronika/releases/94e605c….staging --final /opt/kronika/releases/94e605c…
---- exit 14 stderr ----
kronika-release: required console script is missing
```

`relocate_venv_shebangs` (`deploy/ubuntu/kronika_release.py`, around line
1394) hardcodes:

```python
venv_bin = venv_root / "bin"
for name in ("kronika-db", "kronika-backup"):
    script = venv_bin / name
    if not script.is_file() or script.is_symlink():
        raise ReleaseError("required console script is missing", EXIT_POETRY)
```

The routine web deploy calls this helper (call site around line 3723) where
those two scripts always exist. The capture-path migration's publish step
(session 58, call site around line 5536) reuses the same helper on a capture
tree whose console scripts are the capture ones (`kronika-capture`; the
venv was rebuilt successfully — the log shows `poetry check --lock`,
`env use` and `install --only main` all passing immediately before this
step). The refusal is deterministic and unrelated to the host state. The
failed applies cleaned up completely and the live capture was never touched.

## Correction specification

1. **Explicit, validated required scripts.** Give
   `relocate_venv_shebangs(staging_path, final_path, required_scripts=…)` a
   required-script sequence parameter whose default preserves today's web
   pair exactly, validate that every requested name is a safe single
   filename (fail closed otherwise), and keep the existing per-script checks
   byte-identical (regular non-symlink file, no `.staging` in the content,
   shebang exactly `#!{final_path}/.venv/bin/python`).
2. **Remote CLI input.** Extend the hidden `_remote-relocate-venv-shebangs`
   handler with a repeatable `--required-script` argument; when absent the
   behavior is exactly today's (the web pair). The web call site must keep
   emitting a command with **no** `--required-script` flag, byte-identical to
   the baseline command.
3. **Capture caller.** The capture publish passes exactly one required
   script, derived from the plan's executable name (the basename of
   `plan.executable`), never a fresh literal. Keep every other relocation
   check unchanged, including the editable-install metadata sweep.
4. **Same-class audit.** Audit the shared helpers the capture publish
   invokes for further web-only hardcoded requirements a capture tree cannot
   satisfy; fix exactly the proven additional hits in the same commit,
   naming each, or report them as findings. Do not widen behavior for the
   web paths.
5. **Tests.** Pin: the web deploy's relocate command carries no
   `--required-script` (byte-identical baseline); the capture publish's
   relocate command carries `--required-script kronika-capture` derived from
   the plan; the function accepts a venv carrying the requested script and
   refuses a venv missing it (non-vacuous); an invalid requested name fails
   closed. Keep every existing relocation test green.
6. **Mutation demonstrations**, each named with its observed failure:
   (a) drop the capture caller's flag → the capture pin fails; (b) empty the
   default required pair → a web relocation test fails; (c) accept an
   invalid requested name → the validation test fails.

## Verified starting state, measured by the Orchestrator on 2026-10-16

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                90766ca04358af876a7fb154c44fb005612d34ad
Public main:                  c0f456656c9930810e11d13e1d4684efdb3ee4ff
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4999 passed, 8 skipped, 3 warnings, 0 failed
Focused capture/release modules: 609 passed (nine modules, per session 58)
Focused six-module set:       462 passed
Retention module:             15 passed
JS baselines (unaffected sanity): 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
Host state (Orchestrator evidence): the capture-path preflight plan digest
              b8c68cb5ce246e7b4a792f9ea31e98b0a7e73fe269b87a2cdaca04fffa2d61ad
              remains valid (the failed applies changed nothing); the live
              capture runs from the former pointer, services untouched.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no capture action.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  relocation parameterization, the remote CLI argument and the capture
  caller; edit every test module your parse shows pinning a changed surface,
  naming each non-obvious module in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this correction moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; the routine web deploy's emitted
  command and behavior; the capture software, units, state, token, profile
  and bridge protocol; any document; any dependency or lockfile change; the
  `.ap` gitlink; any Alembic revision; any `.venv` operation; publication;
  push; force; amend; branch; stash; any NUC contact or SSH; any migration,
  deployment or capture invocation. If a necessary change falls outside the
  positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 90766ca04358af876a7fb154c44fb005612d34ad --operation <id> [-- <argv>]
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

1. **Reproduce the defect shape.** Before editing, show the hardcoded pair
   and the two call sites; demonstrate with a synthetic venv that a
   capture-shaped tree (carrying only the capture script) is refused today
   with the exact message, while a web-shaped tree passes.
2. **Post-fix matrix.** Web call site: byte-identical command, no flag;
   capture call site: exactly one flag derived from the plan executable;
   function: requested-script acceptance, missing-script refusal,
   invalid-name refusal; every other relocation check unchanged.
3. **Mutation demonstrations**, the three named.
4. Run, through the declared routes: the focused capture/release/migration
   modules, the full declared Python suite against `4999/8/3/0`, the
   retention module and the JS suites plus bounded glob as unaffected
   sanity.
5. Report every moved or removed site that no test exercises, and every
   consumer your derivation found that this prompt did not name.
6. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved,
   Part B still empty, and any Part C movement with cause.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's anchors are
    locators, not an inventory.
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

**Collapsing pairs.** Do not collapse the web default with the capture
requirement: the web command must stay byte-identical while the capture path
carries its own script. Do not collapse an absent flag with an empty script
list. Do not collapse a validation refusal with a missing-script refusal.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would alter the web deploy's emitted command or any
  other web behavior; if a capture object (software, unit, state, token,
  profile, protocol) would change; if a frozen hash or Part A moves; if a
  Part C re-pin cannot be reproduced from your own measurement; if a `.venv`
  operation or any host action would be required; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded
  result.

Completion: the required-script parameterization with its default preserved,
  the remote argument, the capture caller's derived flag, the same-class
  audit result, the matrix and the three mutation demonstrations; focused
  modules, full Python suite, retention and JS sanity green through the
  declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `59_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push,
  no publication, no refresh, no capture action, no host contact and no later
  grant is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `59` and exchange `01` unchanged. Then:

1. The reproduced defect shape and the post-fix matrix.
2. The same-class audit result.
3. The mutation demonstrations, each with its named mutation.
4. Suites: focused, full Python, retention, JS sanity — counts, elapsed time,
   baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
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

- `deploy/ubuntu/kronika_release.py` — `relocate_venv_shebangs`,
  `remote_relocate_venv_shebangs`, `cmd_remote_relocate_venv_shebangs`, the
  `_remote` handler, the routine deploy's call site and the capture
  publish's call site.
- The capture/release contract test modules named in the starting state.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrix and suites at the reported
commit, then re-runs the capture-path apply with the same preflight digest
(the host state is unchanged), followed by the host verification block. No
push, refresh, capture action or host contact is authorized inside this
prompt.
