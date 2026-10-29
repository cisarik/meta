# Authoritative Worker prompt — Worker session 58, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `58`, exchange `01`. Stored under the
Meta filename mapping as `58_implementation_00.md`, with report destination
`58_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C8-A/P**, the preparation half of the capture-path migration. C7-B
is committed, published, served (`c0f4566`) and rendered-accepted. Capture is
deliberately still on the former pointer: this grant builds and tests the
explicit bounded operation that later (C8-A/H) moves the installed capture
release to the canonical pointer without changing its software, units,
account, state, token, profile or bridge protocol.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 58
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C8AP — prepare the unchanged-release capture path migration
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This operation moves a live browser-backed capture release:
it must preserve the same source identity and build environment, stage and
switch exactly the pointer and the two path lines in the capture units, keep
every name, account, state path, token and protocol byte-unchanged, respect
the existing drain and brake gates, and touch nothing else — no capture
software change (that is C8-B), no web action, no Xvfb action. The routine web
deploy and rollback must remain structurally unable to reach it.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
sections 2.14 and 2.15 are your specification. Required outcomes:

1. **One explicit command.** Add `migrate-capture-paths` to the release
   helper (`deploy/ubuntu/kronika_release.py`) with the engine's established
   two-phase safety: a read-only `preflight` that observes the installed
   capture release and produces a plan digest, and an `apply` that refuses
   without that digest and `--yes`. It must be **unreachable from the routine
   web deploy, rollback, check and status code paths** — no routine path may
   emit or call it — and a test pins that separation.
2. **Prepare (the apply phase, same bounded operation).** Against the freshly
   observed installed capture release, resolved through the existing capture
   pointer/identity machinery:
   - copy the installed capture release to `/opt/kronika/releases/<sha>`
     preserving the exact same source identity and the release markers the
     capture tree carries (derive what identity the capture release uses);
   - rebuild and verify its virtual environment from that release's committed
     lock using the frozen tooling executables the engine already uses (never
     `uv` on this path);
   - stage and switch the canonical pointer `/opt/kronika/capture-current`;
   - stage and install the canonicalized capture units — the **same unit
     names, account, state directory, token, profile, journal, ports and
     bridge protocol**, with only the two `/opt/framenest/capture-current`
     paths (`WorkingDirectory=`, `ExecStart=`) becoming
     `/opt/kronika/capture-current` in all five capture units;
   - refuse conflicting pointer states (canonical pointer already present,
     both pointers present, none present) and any installed unit whose
     contract differs beyond those path lines;
   - enforce the existing gates: the capture work/drain gate
     (`EXIT_CAPTURE_BUSY`), the five-minute brake gate (`EXIT_CAPTURE_BRAKE`)
     and the capture identity/readiness preservation the engine already
     implements;
   - perform **exactly** the bounded bridge and runner stop/start cycle once;
     keep Xvfb, the view and VNC units, and the web service untouched.
3. **Repository path sources.** Update the six capture artifacts
   (`deploy/systemd/kronika-capture.env.example` and the five units) so their
   path lines name the canonical pointer, and note that the captured
   `capture_unit_contract_sha256` therefore recomputes (no literal pin may
   block it). Nothing else in those artifacts changes; the parked capture
   software (`src/kronika_capture/**`) is untouched.
4. **Runbook.** Add the bounded procedure and its restoration path to the
   deployment runbook in the established style: the explicit command, the
   preflight→digest→apply flow, the drain/brake conditions, the one-cycle
   bridge/runner restart, and the prior-pointer/unit restoration, including
   the rule that any recovery browser start needs fresh authority and the
   brake.
5. **Tests, offline.** Same-release source/manifest preservation; final
   executable paths; each conflicting-pointer refusal; the drain and brake
   gate exits; exactly-bounded actions (only the specific systemctl verbs; no
   web, Xvfb, view or VNC actions); the unit transformation is exactly the
   pointer substitution (a six-artifact before/after diff shows only the
   documented lines); the command is unreachable from routine paths.

## Anchors, as locators, not an inventory

- `deploy/ubuntu/kronika_release.py` — `CAPTURE_CURRENT`/`NEW_CAPTURE_CURRENT`
  and `CAPTURE_POINTERS`, `CAPTURE_CONTRACT_PATHS`, `CAPTURE_RUNTIME_CONTRACT`,
  the capture constants and exit codes, `resolve_capture_pointer`,
  `cmd_remote_capture_current`, `cmd_remote_atomic_switch_capture`,
  `cmd_remote_restart_capture_runner`, `cmd_remote_capture_work_gate`,
  `cmd_remote_capture_brake_gate`, `cmd_remote_capture_identity`,
  `cmd_remote_capture_readiness_gate`, `capture_runtime_identity`,
  `_drain_capture_work`, `_enforce_capture_brake`,
  `_snapshot_capture_identity`, `_verify_capture_readiness`,
  `_cmd_capture_transition`, the subcommand parser and the routine
  deploy/rollback paths.
- `deploy/systemd/kronika-capture-*.{service,env.example}` — the six
  artifacts.
- `tests/contract/test_kronika_capture_services.py`,
  `tests/contract/test_chatgpt_page_packaging.py`,
  `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_nuc_release_source_contract.py` — the pin homes.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the capture runbook section to extend.

## Verified starting state, measured by the Orchestrator on 2026-10-16

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                c0f456656c9930810e11d13e1d4684efdb3ee4ff
Public main:                  c0f456656c9930810e11d13e1d4684efdb3ee4ff
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4981 passed, 8 skipped, 3 warnings, 0 failed
Focused capture/release modules: 429 passed
Retention module:             15 passed
JS baselines (unaffected sanity): 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
Host state (Orchestrator evidence): the NUC serves `c0f4566`; capture is
              still on `/opt/framenest/capture-current` (release identity
              `94e605c…`, units `kronika-capture-*`, account
              `kronika-capture`, state `/var/lib/kronika-capture`, token
              `/etc/kronika-capture/credentials/kronika-bridge-token`,
              bridge protocol `1`); C8-A/H will execute the operation this
              grant builds.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no capture action.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  new command and its bounded operations, reusing the existing capture
  primitives; edit the six `deploy/systemd/kronika-capture-*` artifacts for
  exactly the pointer path lines; edit the capture tests and any further test
  module your parse shows pinning a changed surface, naming it in the report
  before editing it; add the runbook procedure section to
  `docs/UBUNTU_NUC_DEPLOYMENT.md`; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this grant moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; `src/kronika_capture/**` and every
  capture software file (C8-B owns software identity); the parked profile,
  state, token and journal objects; the routine deploy/rollback/check/status
  behavior; any document outside the runbook section; any dependency or
  lockfile change; the `.ap` gitlink; any Alembic revision; any `.venv`
  operation; any capture unit installation, pointer switch, service
  restart, browser launch or host mutation (C8-A/H owns execution);
  publication; push; force; amend; branch; stash; any NUC contact or SSH; any
  provider, browser or capture contact. If a necessary change falls outside
  the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline c0f456656c9930810e11d13e1d4684efdb3ee4ff --operation <id> [-- <argv>]
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
Side-effect authority: reversible local repository mutation only. No host,
  service, pointer, unit or browser side effect.
Browser authority: none.
```

## Verification

1. **Command and plan.** The preflight's observed plan, the digest binding and
   the apply's refusal without digest/`--yes`; the accepted-operation
   refusals; the two-phase shape shown as literal command strings.
2. **Preservation matrix.** Same-release source identity and markers; the venv
   rebuilt from the committed lock with the frozen tooling; the pointer
   switch exactly one step; the six-artifact diff exactly the pointer path
   lines; names, account, state, token, profile, journal, ports and protocol
   byte-unchanged.
3. **Gate matrix.** Work/drain gate exit, brake gate exit, identity/readiness
   gates, each conflicting-pointer refusal, each wrong-unit refusal.
4. **Bounded actions.** The exact systemctl verbs for bridge and runner, once
   each, and the absence of any web, Xvfb, view or VNC action; the routine
   paths cannot emit the command.
5. **Mutation demonstrations**, each named with its observed failure: widen
   the unit transformation beyond the pointer lines → the six-artifact diff
   test fails; drop the digest binding → the apply-refusal test fails; drop
   the work gate → the busy-refusal test fails.
6. Run, through the declared routes: the focused capture/release modules
   (baseline 429), the full declared Python suite (baseline `4981/8/3/0`),
   the retention module (15) and the JS suites plus bounded glob as unaffected
   sanity.
7. Report every moved or removed site that no test exercises, and every
   consumer your derivation found that this prompt did not name.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and your own measurement for any Part C movement.

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

**Collapsing pairs.** Do not collapse the capture path move with a capture
software change; do not collapse "staged" with "switched"; do not collapse a
work-gate refusal with a transport failure; do not collapse the six-artifact
path substitution with any other unit edit.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would touch capture software, the routine web paths, a
  parked object or a document beyond the runbook section; if a name, account,
  state, token, profile or protocol would change; if a frozen hash or Part A
  moves; if a Part C re-pin cannot be reproduced from your own measurement;
  if a `.venv` operation or any host action would be required; if context
  pressure reaches the point where a bounded rotation is cheaper than a
  degraded result.

Completion: the explicit command with its two-phase safety, preservation and
  gate matrices, the repo artifact updates and the runbook section; focused
  modules, full Python suite, retention and JS sanity green through the
  declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `58_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push,
  no publication, no refresh, no capture action, no host contact and no later
  cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `58` and exchange `01` unchanged. Then:

1. The command, plan and two-phase shape as implemented.
2. The preservation, gate and bounded-action matrices.
3. The six-artifact before/after diff and the recomputed contract hash.
4. The mutation demonstrations, each with its named mutation.
5. Suites: focused, full Python, retention, JS sanity — counts, elapsed time,
   baseline differences.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
7. Every site no test exercises.
8. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  sections 2.14 and 2.15 in full.
- `deploy/ubuntu/kronika_release.py` — the capture constants, primitives and
  command parser named in the anchors.
- The six capture artifacts and the capture tests.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the capture runbook context.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the command matrix, the artifacts and
the suites at the reported commit, then issues **C8-A/H** — the separate
Cooperator host grant that executes the prepared operation on the NUC
(pointer switch, unit path install, one bounded bridge/runner cycle, Xvfb
kept), with the drain/brake gates and the restoration path. No push, refresh,
capture action or host contact is authorized inside this prompt.
