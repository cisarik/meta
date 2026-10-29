# Authoritative Worker prompt — Worker session 32, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `32`, exchange `01`. Stored under the
Meta filename mapping as `32_implementation_00.md`, with report destination
`32_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 32
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-COPS — canonical operator-script counterparts
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. These are the last five Part B paths without canonical
counterparts, and they are operator-facing security diagnostics. `C7-B` removes
the old entry points, so the canonical scripts must exist first and must carry
the established dual-prefix variable contract without weakening any check,
refusal or exit code. Mistakes here surface as an operator diagnostic that
silently passes or misreads a security posture.

This is work item **C-OPS** from the accepted closure plan at
`25_report_00.md` section 2.9.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.9 is your specification. Read it in full. Required outcomes:

1. **Five canonical counterparts**, executable (mode `755`), added without
   touching the five existing scripts:

```text
scripts/operator/infosec/kronika_log_triage.sh
scripts/operator/infosec/kronika_public_surface_check.sh
scripts/operator/infosec/kronika_socket_permissions_check.sh
scripts/operator/network/kronika_mullvad_egress.sh
scripts/operator/network/kronika_mullvad_egress.fish
```

2. **Canonical implementations are authoritative; the old entry points remain
   unchanged** until `C7-B` removes them. Part B must still measure **20** after
   this cut. The canonical Fish wrapper must target the canonical Bash
   implementation and keep the AppImage/loader environment sanitization.
3. **Dual-prefix variable contract.** For every operator-facing variable and
   test hook the scripts read, accept `KRONIKA_<SUFFIX>` (canonical, preferred)
   and `FRAMENEST_<SUFFIX>` (retained fallback) under the established contract
   already used by `scripts/operator/network/kronika_nuc_worker_gate.fish`:
   only the old spelling present → use it; only the canonical spelling present →
   use it; both present with different values → **exit 2 naming only the two
   variable names** (never the values); both present and equal → accepted;
   empty-value semantics must be derived from the gate's contract and stated.
   Derive the complete suffix set from the scripts; the known set includes
   `LOG_UNIT`, `LOG_SINCE`, `SPIKE_THRESHOLD`, `JOURNALCTL_BIN`,
   `PUBLIC_BASE_URL`, `CURL_BIN`, `SURFACE_CHECK_TIMEOUT`, `SOCKET_PATHS`,
   `EXPECTED_OWNER_PATTERN`, `STAT_BIN`, `NETWORK_TEST_HOOKS`,
   `NETWORK_TEST_PYTHON`, `NETWORK_TEST_TAILSCALE`, `NETWORK_TEST_CURL`,
   `NETWORK_TEST_MULLVAD`.
4. **Identity updates only.** Canonical defaults for operational values:
   `kronika.service` for the log unit; socket paths
   `/run/kronika/kronika.sock:/run/kronika/kronika-public.sock`; owner pattern
   `^(root|kronika)$`; canonical usage strings and `SCRIPT_NAME` output. The
   external `mullvad.ts.net` DNS suffix and the Mullvad diagnostic URL are
   external facts and must not be renamed. Do not change any check, ordering,
   refusal, timeout or exit code; do not add capabilities; do not add `sudo`;
   do not introduce any frozen residue path.
5. **Operator instructions.** Update `docs/OPERATOR_NETWORK.md`,
   `docs/INFOSEC.md` and `docs/ACCEPTANCE_DUAL_AUDIENCE.md` — state the
   canonical script names where the old ones appear, keeping the old names
   truthful during the compatibility window. Derive every reference from the
   documents; do not rewrite unrelated prose. (If a different but equivalent
   document path is the real one, use it and report the difference.)
6. **Old scripts frozen.** `scripts/operator/infosec/framenest_*.sh` and
   `scripts/operator/network/framenest_mullvad_egress.{sh,fish}` must not be
   modified.

## Verified starting state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                a3977755b6d20a369f1a5c75e39bbcacd88de5c6
Public main:                  a37be37dd538afa626dbea94b074b676d0b8301c
                              (one accepted local commit is unpublished, by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at a397775:   4773 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
```

Anchor map, verified at the baseline (locators, not an inventory — re-derive):

```text
scripts/operator/infosec/framenest_log_triage.sh           120 lines, mode 755
scripts/operator/infosec/framenest_public_surface_check.sh 166 lines, mode 755
scripts/operator/infosec/framenest_socket_permissions_check.sh 125 lines, mode 755
scripts/operator/network/framenest_mullvad_egress.sh        735 lines, mode 755
scripts/operator/network/framenest_mullvad_egress.fish       15 lines, mode 755
scripts/operator/network/kronika_nuc_worker_gate.fish       existing dual-prefix reference
tests/contract/test_operator_network_scripts.py             the hermetic script harness
docs/OPERATOR_NETWORK.md, docs/INFOSEC.md, docs/ACCEPTANCE_DUAL_AUDIENCE.md
                                                            operator instructions
```

The infosec scripts currently have no dedicated contract module; derive the
complete test surface yourself and report any module your derivation names
beyond this prompt's sample before editing it.

**No host execution.** The scripts must be exercised only through hermetic
fake-tool fixtures. No real `journalctl`, `curl`, `tailscale`, `mullvad`,
firewall, network probe, journal access or privilege use.

## Authority

```text
Positive authority: add the five canonical scripts named above; edit
  `tests/contract/test_operator_network_scripts.py`; add
  `tests/contract/test_operator_infosec_scripts.py`; edit
  `docs/OPERATOR_NETWORK.md`, `docs/INFOSEC.md` and
  `docs/ACCEPTANCE_DUAL_AUDIENCE.md` for the canonical references; edit any
  further directly affected contract module you name in the report before
  editing it; edit `tests/contract/test_kronika_identity_retention.py` only to
  re-pin a Part C scalar that your own measurement shows this cut moved, with
  the arithmetic cause stated; create exactly one local commit on `main`.

Negative authority: the five existing `framenest_*` operator scripts (frozen);
every other path; any dependency or lockfile change; any change to
`pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen document
or Alembic revision; publication; push; force; amend; branch; stash; any NUC
contact or SSH; any real tool, journal, socket, network, firewall, Tailscale or
Mullvad invocation; any provider, browser or capture contact; any secret or
personal-configuration read. If a necessary change falls outside the positive
scope, stop and report; do not widen scope.

Commands: shell syntax checks (`bash -n`, the fish syntax-check form you derive)
and the hermetic test harness only. Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline a3977755b6d20a369f1a5c75e39bbcacd88de5c6 --operation <id> [-- <argv>]
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
Side-effect authority: reversible local repository mutation only. No host,
  service, network, journal, firewall or account side effect.
Browser authority: none.
```

## Verification

1. **Syntax.** `bash -n` for every Bash script (old and new); the fish
   syntax-check form for every Fish script. Report the exact command form.
2. **Hermetic matrix per script family**, using fake binaries on `PATH` and
   `fish --no-config` for Fish, including: canonical-only variable, old-only
   variable, equal dual, conflicting dual (exit 2; message names both variable
   names and contains no value), empty-value cases, missing required variable,
   missing tool, and preserved exit codes for success and each refusal.
3. **Wrapper identity.** The canonical Fish wrapper reaches the canonical Bash
   implementation and preserves the environment sanitization; prove it with the
   fake harness rather than by reading the file alone.
4. **Old family regression.** The existing old-script tests stay green and the
   old files are byte-identical (report their hashes).
5. **Security-posture preservation.** Diff the canonical logic against the old
   logic line by line; report every difference and show that each is either the
   identity change or the dual-prefix resolution. No check, refusal or ordering
   may weaken.
6. Demonstrate that each new guard fails when its protection is removed, naming
   the mutation and the observed failure. Whenever a guard reads a path, a name
   or an environment value, prove what happens when the input is absent.
7. Run, through the declared route: the focused script modules, then the
   declared full Python suite, then the retention module. Report every count and
   any difference from the `4773/8/3/0` baseline.
8. Report **every moved or removed site that no test exercises**, and every
   reference your derivation found that this prompt's sample did not name.
9. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement (new scripts contain `FRAMENEST_*` fallbacks, so token and
   membership movement is expected — re-pin from the tree, never from memory).

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

**Collapsing pairs.** The dual-prefix resolution must fail loudly on a
conflicting pair and must never silently pick one value; name its empty-value
semantics.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a necessary change would edit an old `framenest_*` script; if a
  check or exit code cannot be preserved under the dual-prefix contract; if a
  real tool, host or network would have to be invoked; if a frozen hash, Part A
  or Part B moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if context pressure reaches the point where a bounded rotation
  is cheaper than a degraded result.

Completion: the five canonical counterparts added and executable; the
  dual-prefix contract implemented and tested for every variable; old scripts
  untouched and green; operator instructions updated; focused modules, full
  declared Python suite and retention module green through the declared route;
  one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `32_report_00.md` in
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
echoing `kronika-sole-identity`, session `32` and exchange `01` unchanged. Then:

1. The five canonical scripts and their mode; the old-script hashes proving they
   are untouched.
2. The derived variable suffix set and the dual-prefix semantics.
3. The line-by-line logic diff classification (identity change versus
   dual-prefix resolution).
4. The hermetic matrix results per family, including conflict and refusal cases.
5. Wrapper identity and environment-sanitization evidence.
6. Mutation demonstrations, each with its named mutation.
7. Operator-document references updated, with any derivation difference.
8. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
9. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and Part C
   movement with cause.
10. Every site no test exercises.
11. Deviations, risks, missing evidence, and one smallest next step.

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
  section 2.9 in full.
- The five old scripts in full.
- `scripts/operator/network/kronika_nuc_worker_gate.fish` — the established
  dual-prefix conflict contract to follow.
- `tests/contract/test_operator_network_scripts.py` in full — the hermetic
  harness and fake-tool patterns.
- `docs/OPERATOR_NETWORK.md`, `docs/INFOSEC.md`,
  `docs/ACCEPTANCE_DUAL_AUDIENCE.md` — the operator instructions.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, any real journal.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the five old scripts
are byte-untouched; the canonical counterparts are executable and reachable;
the dual-prefix conflict exits 2 naming only variable names; every preserved
check and exit code is unchanged; Part B still measures 20; and the full suite
is green at the reported commit. After acceptance, publication of `a397775` +
this cut and then the `C6-H` window remain the next steps.
