# Authoritative Worker prompt — Worker session 02, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `02`, exchange `01`. Stored under the
Meta filename mapping as `02_correction_00.md`, with report destination
`02_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-01 — make the operator-gate Fish contract test hermetic
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: this is a single localized edit at one known function, with an exact
mechanism already verified, a strong focused test that already fails for the
right reason, and trivial rollback. `Low` is sufficient. Escalate only by naming
the concrete evidence you could not obtain at this profile.

This is not plan implementation. Worker session `01` returned `BLOCKED` and its
planning authority expired on submission. This exchange is a bounded prerequisite
correction so that a green E2 baseline exists before planning resumes.

## Goal

Make `tests/contract/test_operator_network_scripts.py` hermetic against the
developer's personal Fish environment, so the Fish-gate contract test result
depends only on the repository, and restore the Python suite to fully green at
this baseline.

## Accepted facts you may rely on

These were measured by the Orchestrator at
`0c850996cd2ef17dae4112733fd17fdc732f4699` and independently reproduced.

- `scripts/operator/network/framenest_nuc_worker_gate.fish` lines 254-257 seed
  `target`, `remote_user` and `identity` from `$FRAMENEST_NUC_SSH_TARGET`,
  `$FRAMENEST_NUC_SSH_USER` and `$FRAMENEST_NUC_SSH_IDENTITY` **before**
  applying CLI flags. Seeding an empty variable yields an empty list, which the
  later presence checks correctly treat as missing.
- The development host carries exactly those three names as **exported Fish
  universal variables** in `~/.config/fish/fish_variables`.
  `FRAMENEST_NUC_SSH_COMMAND` is deliberately not among them.
- `_run_fish` at lines 423-444 removes the four `FRAMENEST_NUC_SSH_*` names from
  the child process environment, but spawns `/usr/bin/fish <script> <args>`
  **without disabling Fish startup configuration**. Fish therefore restores the
  three exported universal variables before the gate script reads them.
- Consequence: the `target`, `user` and `identity` parametrizations return `0`
  instead of `2`. The `command` parametrization still returns `2` because nothing
  supplies `FRAMENEST_NUC_SSH_COMMAND`. Observed result:
  `3 failed, 1 passed, 4148 deselected`.
- `fish --no-config` (`-N`) exists on this host's fish `4.9.3` and was confirmed
  to suppress all four names, including exported universal variables.
- The gate script sources nothing and defines every function it uses, so
  disabling startup configuration cannot break it.
- `_run_fish` has 19 call sites, all inside this one test module.
  `_run_bash` is a separate helper and is unaffected.

## Required change

Change only `_run_fish` in `tests/contract/test_operator_network_scripts.py`
so the spawned Fish does not load personal startup configuration. The
`--no-config` flag placed before the script path is the verified mechanism and
is the expected approach:

```text
["--no-config", str(script), *args]
```

You may choose an equivalent isolated-configuration mechanism instead, for
example redirecting `XDG_CONFIG_HOME` to an empty directory created under
`tmp_path`. If you choose something other than `--no-config`, state the reason
in your report. Do not make both changes; one mechanism is enough.

Do not change the gate script, the gate's behaviour, the `_hook_env` helper,
`_run_bash`, the parametrization, the assertions, or any other file. Do not
change `clear_env` semantics. Do not weaken, skip, xfail or delete any test.

One optional addition is authorised, at your discretion, and must be justified
in the report: a single focused assertion that the Fish invocation is isolated
from personal startup configuration, so that removing the isolation later
cannot silently pass on a host without those variables. The existing three
parametrizations already guard the behaviour on a host that has them; this
assertion guards the mechanism on a host that does not. If you skip it, say so.

## Authority

```text
Positive authority: edit exactly
  tests/contract/test_operator_network_scripts.py, function _run_fish, plus at
  most one new focused test function in the same file; create one local branch
  named fix/operator-gate-test-hermetic from main; stage and commit exactly the
  changed paths of that file; run the declared AP test operations and the
  declared JavaScript test route.

Negative authority: any edit to any other path, including the gate script, other
  tests, deploy/, scripts/, docs/, src/, pyproject.toml, ap.project.conf,
  .gitmodules and .gitignore; any change to the gate's runtime behaviour; any
  dependency install, update or lockfile change; any write outside the
  repository working tree; any Git push, tag, merge, rebase, force operation,
  remote branch creation or history rewrite; any NUC contact, including SSH, the
  NUC worker gate and deploy/ubuntu/framenest-release in every mode; any
  reading or writing of personal Fish configuration, `~/.config/fish/**`,
  `fish_variables`, browser profiles, cookies, tokens, credential stores or
  `.secrets`; any provider or capture-browser contact; any use of
  ~/.config/opencode; any roadmap, ADR or documentation edit.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline <commit>
  --operation <id> -- <argv>`, with operations declared in ap.project.conf.
  Never invoke `.venv/bin/python`, `python`, `python3` or `poetry run` for
  evidence. JavaScript tests use the declared `node --test` route.

Dependency authority: none. The canonical `.venv` is correct; do not reinstall,
  update or relock anything.

Git authority: create the named local branch, stage only the changed file, and
  make exactly one local commit. No push and no publication. Any other Git write
  requires stopping first.

Network authority: none beyond the local routes above. No provider call, no
  capture-browser contact, no other outbound request.

Secret authority: none. Never print, quote or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs or SSH fingerprints. Do not read
  personal Fish configuration even to confirm the cause; the cause is already
  verified and is part of this prompt.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` is authoritative inside its scope. On conflict between retained
  context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only. No
  destructive mutation, no remote effect, no deployment, no credential effect,
  no billing effect.

Browser authority: none.
```

## Verification

Confirm before editing, and stop without editing if any of this fails:

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 0c850996cd2ef17dae4112733fd17fdc732f4699
Expected working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
./.ap/ap doctor
./.ap/ap project check --root /home/agile/Projects/kronika --baseline 0c850996cd2ef17dae4112733fd17fdc732f4699
```

Then:

1. Reproduce the failing baseline once with the focused route, using
   `--operation test-focus -- -k "test_ssh_gate_rejects_missing_required_values"`.
   Expect `3 failed, 1 passed`. Do not skip this; a fix without a reproduced
   before-state has no evidence.
2. Make the change.
3. Re-run the same focused route. Expect `4 passed`.
4. Run the whole affected module:
   `--operation test-focus -- tests/contract/test_operator_network_scripts.py`.
   Expect zero failures and no newly skipped test.
5. Run the full declared `test` operation. Expect zero failures and no new
   skips relative to the Orchestrator-measured `4141 passed, 8 skipped,
   3 warnings, 3 failed`. Report the exact final counts. The suite takes about
   twelve minutes; let it finish once and do not rerun it.
6. Run the declared JavaScript route `node --test tests/*.test.js`. Expect the
   same `554 total, 549 passed, 5 skipped` as the Orchestrator-measured
   baseline. This file is Python-only, so this is a no-change regression guard.
7. Re-run `./.ap/ap project check --root /home/agile/Projects/kronika
   --baseline 0c850996cd2ef17dae4112733fd17fdc732f4699` and
   `git status --porcelain` after the commit, expecting a clean tree.

If step 1 does not reproduce `3 failed, 1 passed`, stop and report; do not
change a test whose failure you could not reproduce.

```text
Evidence tier: E1. Localized known path, strong focused tests, trivial
  rollback, no publication, no remote effect.
```

## Git

One local commit on the new branch. Suggested message subject:

```text
fix(test): isolate the operator gate Fish tests from personal configuration
```

Do not push. Report the branch name and the resulting commit SHA exactly.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the focused route does not reproduce exactly 3 failures and 1 pass;
  if any step would require an edit outside the one authorised file; if the full
  suite shows a failure you cannot attribute and cannot explain with evidence;
  if the change would require a dependency or packaging change; if context
  pressure reaches the point where a bounded rotation is cheaper than a degraded
  fix.

Completion: exactly one commit on the named branch, the failing tests passing,
  the full Python suite green with no new skips, the JavaScript route unchanged,
  and the tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `02_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication and no
  planning is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Worker session 01 outcome: BLOCKED; unchanged by this exchange
Planning status: Worker session 01 planning authority expired; planning has not
  resumed and does not resume under this prompt
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing logical-whole identity `kronika-sole-identity`, Worker session ordinal
`02` and Worker exchange ordinal `01` unchanged. Then: the exact diff; the
mechanism chosen and, if not `--no-config`, why; the before and after focused
results; the full-suite exact counts against the measured baseline; the
JavaScript route result; the branch name and commit SHA; whether the optional
assertion was added and why; confirmation that no other file, no dependency and
no remote resource was touched; deviations, risks and missing evidence; and one
smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

Read only what this bounded change requires:

- `tests/contract/test_operator_network_scripts.py`, especially `_hook_env`,
  `_fish_executable`, `_run_bash`, `_run_fish` and the failing parametrization.
- `scripts/operator/network/framenest_nuc_worker_gate.fish` lines 245-340.
- `docs/WORKER_EXECUTION_CONTRACT.md` sections on the canonical Python route and
  on failure classification.
- `AGENTS.md` Worker Execution section.
- `.ap/AP_WORKER.md` and `.ap/AP.md` §5, §9 and §10.

Do not read personal Fish configuration, `~/.config/opencode`, `private/**`, or
any credential store.

## Communication

Report and code comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

This correction is accepted as a prerequisite slice of `kronika-sole-identity`
only. It is deliberately **not** part of the identity rename, must not be folded
into any rename cut, and grants no roadmap or ADR documentation authority. On
acceptance the Orchestrator will verify the diff and the counts, then decide
separately whether to resume Worker session `01` planning with a fresh grant.
Planning does not restart automatically.