# Authoritative Worker prompt — Worker session 22, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `22`, exchange `01`. Stored under the
Meta filename mapping as `22_implementation_00.md`, with report destination
`22_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 22
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C4A — canonical release entry, complete marker readers, switching guard
Reasoning recommendation: High
Recommended context capacity: approximately 450k tokens
```

Rationale: `High`. This cut creates the guard that makes a later irreversible cut
safe, completes a compatibility implementation that cut C1 only partly delivered,
and adds reader support for durable identities whose writers change in C5. Getting
any of it subtly wrong can either block a safe cut or silently hide historical data.

This is cut **C4-A** from the accepted completion plan at `17_report_00.md` section
1.5. It must land and be **installed on the NUC before C5**.

## Why this cut exists

Three separate things are incomplete, and all three were found by inspection rather
than assumed.

**First, the installed-unit guard does not exist at all.** The accepted plan assumed
C4 would *add* the guard to the paths that switch the web pointer. Measured: there is
**no reference to `ExecStart` or `ExecStartPre` anywhere in
`deploy/ubuntu/framenest_release.py`**. Nothing today verifies that the binaries the
installed unit names actually exist in the target release. C7 deletes the
`framenest-*` entry points while the host still runs `framenest.service`, which names
`framenest-production`. **Without this guard, that deploy would switch the pointer and
restart onto a release whose executable is absent.** This guard is the mechanism that
makes C7 safe to deploy, and it is being created here for the first time.

**Second, C1's marker compatibility is only half-delivered.** The constants at
`framenest_release.py:43-49` know both spellings:

```python
RELEASE_SHA_MARKER = ".framenest-release-sha"
RELEASE_MANIFEST_MARKER = ".framenest-release-manifest.json"
COMPATIBLE_RELEASE_SHA_MARKER = ".kronika-release-sha"
COMPATIBLE_RELEASE_MANIFEST_MARKER = ".kronika-release-manifest.json"
```

but several call sites **hardcode the former spelling as a literal** instead of using
the constants. Measured instances, at lines **547, 548, 1665 and 1783**. So probing
recognises both marker names while later readers open only the old filename. C5's
precondition is that complete readers are installed; they are not.

**Third, and this one hides data.** `_successful_generic_predicates()` at
`src/kronika/infrastructure/persistence/companion_review_repository.py:789-793` ends
with an equality filter:

```python
media_analysis_runs.c.result_schema_version == RESULT_SCHEMA_VERSION
```

`RESULT_SCHEMA_VERSION` is `"framenest-media-suggestion-result-v1"` at
`domain/media_analysis_runs.py:21`, and there is a **second** one,
`MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` =
`"framenest-movie-identification-result-v1"` at `domain/media_classification.py:114`.
Both are **written into the database**. When C5 switches the writers to the canonical
spelling, this filter matches only new rows and **every historical successful analysis
disappears from the companion inbox**. C4-A must make the readers accept both
spellings before C5 changes any writer.

## Verified current state

Every figure was measured by the Orchestrator at this commit.

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                6e89328640fe5477e08f17f4c31c9fc4bf261238
Remote origin:                https://github.com/cisarik/kronika
Public main:                  6e89328640fe5477e08f17f4c31c9fc4bf261238, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
```

Baselines at this commit, all executed by the Orchestrator:

```text
Python declared test:  4399 passed, 8 skipped, 3 warnings, 0 failed
JavaScript:            583 total, 578 passed, 0 failed, 5 skipped
Retention module:      15 passed
```

NUC state, for context only. **You have no NUC authority and must not attempt any.**

```text
active web release:  6e89328640fe5477e08f17f4c31c9fc4bf261238
capture release:    94e605c17b881461fad3e22fd8c7fca32cb93976
database revision:  0035, equal to head
installed unit:     framenest.service, User=framenest, ExecStart=.../framenest-production
installed layout:   /opt/framenest, /etc/framenest, /var/lib/framenest
```

## In scope

### 1. The canonical release entry

Move the engine to `deploy/ubuntu/kronika_release.py`, add the Fish entry
`deploy/ubuntu/kronika-release`, and keep `deploy/ubuntu/framenest-release` as a
wrapper that execs the new engine with identical arguments.

**No commit may lack both names.** Measure the existing wrapper first:
`deploy/ubuntu/framenest-release` is a Fish script that resolves
`$script_dir/framenest_release.py`, hardcodes that filename, and prints
`FrameNest release engine is unavailable.` when the engine is absent. That message is
user-visible operator output and falls inside this cut's prose scope.

Routine constants **stay on the old layout by design**: the service name, release
root, current pointer, capture pointer and env-file path are C6's business. Derive the
filename mapping from the retention ledger's own Part B set rather than from prose.

### 2. The NUC worker gate

Rename `scripts/operator/network/framenest_nuc_worker_gate.fish` to
`kronika_nuc_worker_gate.fish`, and keep the old path as a wrapper that execs the new
file. **The old path must keep working throughout**, because the Orchestrator and the
Cooperator both use it and it is the only sanctioned NUC route.

The new file reads `KRONIKA_NUC_SSH_TARGET`, `KRONIKA_NUC_SSH_USER`,
`KRONIKA_NUC_SSH_IDENTITY` and `KRONIKA_NUC_SSH_COMMAND`, and **falls back to the
`FRAMENEST_NUC_SSH_*` names when the canonical name is unset**. Both set and different
exits 2 and names **suffixes only, never values**. CLI flags still override.
Missing-value exit stays 2. Probe behaviour stays identical.

Today the gate reads the old names **directly at lines 254-257**, with no prefix
resolution at all, so the fallback logic is new.

Test hooks follow the same prefix fallback. **The Fish tests must be hermetic:**
`fish --no-config`, synthetic environment, and no read of `~/.config/fish/**` or
`fish_variables` by the Worker. Note that the Orchestrator's own fish one-liner in this
area failed earlier because `and`/`or` after a line continuation were absorbed as
operands; write the tests, do not rely on ad-hoc shell one-liners.

### 3. Complete the marker readers

Centralise marker selection and validation so that **every** reader resolves either
spelling through the constants rather than a literal, and so that disagreement is a
failure rather than a silent preference. The readers that must be covered:

```text
current-release status
optional capture pointers          read_optional_release_sha, called at 1249, 1535, 1687
manual rollback
automatic rollback
capture activation and rollback
release-manifest identity checks
```

If both spellings exist, validate that their identities agree and fail on
disagreement. Historical release artefacts written by pre-C4 releases must remain
readable **after C7 removes the canonical names**, so the resolution must be data-driven
and not depend on the old constant surviving.

### 4. The installed-unit executable guard — create it

This does not exist. Create it, and apply it to **every** path that can switch the web
pointer, **including automatic rollback**.

```text
Determine the effective unit configuration, including drop-ins.
Extract the EXECUTABLE fields of effective ExecStart and ExecStartPre only.
  Not every argument basename. A path argument, a flag or an interpreter path is not
  the thing being guarded.
Require each named executable to exist in the target release's .venv/bin as a
  regular, executable, NON-SYMLINK file with a valid target path.
An unknown effective execution form must FAIL before switching, not be skipped.
```

Move rollback readiness and executable validation **ahead of** the rollback symlink
switch, so a rollback cannot move the pointer onto a release that cannot start.

Add a test asserting the guard applies to automatic rollback and to effective drop-ins,
not only to the explicit deploy path.

### 5. Reclaimable deploy locking — a new finding

The Orchestrator observed `existing remote lock or recovery state` during the last
deploy and traced it to this mechanism:

```text
line  363  cmd_remote_mkdir_deploy_dir() = sudo -n mkdir -m 0700 {REMOTE_DEPLOY_DIR}
line 1346  the gate: ssh(... mkdir ...) inside try, raising
           "existing remote lock or recovery state", EXIT_EXISTS on failure
line 1526  except-branch cleanup: ssh(... rmdir ...)
line 1683  finally cleanup:        ssh(... rmdir ...)
```

`mkdir` has **no `-p`**, so a directory left behind by an interrupted deploy makes every
later deploy fail at `EXIT_EXISTS`, and the abort happens **before** the `finally` is
established, so there is **no self-healing path and no recovery command**.

Make the gate able to distinguish an interrupted prior run from a genuinely concurrent
one, and able to reclaim **its own** prior lock safely. Requirements:

- A lock carrying the live run's own identity may be reclaimed; a lock belonging to a
  different live run may not.
- Reclamation must be safe against a run that is actually in progress. Prefer
  ownership plus liveness over a blanket "if it exists, delete it".
- If you cannot establish ownership, refuse and say so. **Refusing is an acceptable
  outcome; silently deleting a live lock is not.**
- Report the reclaim decision in the operation output.

### 6. Durable analysis-identity readers

Make every reader of a stored analysis identity accept **both** the current and the
canonical spelling, without changing any writer. This covers at least:

```text
result-schema filters
stored-result validation
prompt-version aliases
```

The equality filter at `companion_review_repository.py:791` is the known instance.
**Derive the full set yourself** rather than fixing only that line: search for every
comparison against a `*_RESULT_SCHEMA_VERSION` or prompt-version constant, in both
persistence and application layers.

Two constants are involved, not one:

```text
domain/media_analysis_runs.py:21        "framenest-media-suggestion-result-v1"
domain/media_classification.py:114       "framenest-movie-identification-result-v1"
```

Prove the equivalence is **symmetric and explicit**, and that a row written under either
spelling is returned by the same query. Add a test that a historical row stored under
the former spelling still satisfies the predicate after C5's writer change is
simulated.

### 7. Documentation

`AGENTS.md` and `docs/WORKER_EXECUTION_CONTRACT.md` name `kronika-release` and
`kronika_nuc_worker_gate.fish` as canonical, and state that the old paths and the old
SSH variable names still work until C7-B.

**Both are living prose under the retention ledger's Part C and the question-12
denylist.** Frozen ADR bodies are not living prose and must not be edited.

## How you must find the sites — derivation, not a list

**Do not work from the site list above.** It is a confirmed sample and a specification
of causes, not of locations.

Sessions 14, 15, 16, 19 and 21 of this whole each found omissions when the Orchestrator
issued a hand-built site list, and in one case that left **four import-boundary guards
passing vacuously**. Issue yourself the derivation rule instead:

```text
A. Parse deploy/ubuntu/framenest_release.py and every file under scripts/operator/ and
   collect, by parsing:
     - every occurrence of a marker filename, whether via constant or literal
     - every comparison against a RESULT_SCHEMA_VERSION or prompt-version constant
     - every ssh(...) call site that can switch or read a pointer
   Classify each as: in-scope-this-cut / C4-B / C6 / C7-B / a frozen residue.
B. Report the per-category totals and reconcile them against the sample above BEFORE
   editing. Explain any difference.
C. Report every site you found that no currently failing or passing test exercises.
```

**Derivation rule 8 has failed three times in this whole and the corrected value is
known.** `FROZEN_ALEMBIC_SHA256` contains **36** keys, revisions `0001` through `0035`
plus `__init__.py`. Measure it. Two Workers reported 38 by transcribing a remembered
figure.

## Scope boundaries

```text
Do NOT change any routine host constant. The service name, /opt/framenest/releases,
  /opt/framenest/current, /opt/framenest/capture-current, /etc/framenest/framenest.env,
  the Unix account and the unit names all stay exactly as they are. That is C6.
Do NOT change any environment prefix fallback. lookup_env's FRAMENEST_ fallback stays.
  That is C7-B.
Do NOT delete any alias, wrapper or fallback this cut adds. C4-A ADDS canonical names
  and KEEPS the old ones. C7-B removes them.
Do NOT change any durable writer identity. No backup, sidecar, marker or manifest name
  is written with the new spelling in this cut. That is C5.
Do NOT change the mutation header, either companion protocol string, any CSS, DOM or
  port identifier, or the deliberately dual-spelled message at
  adapters/api/tailscale_ingress.py:869. That is C7-A.
Do NOT rename or move any capture state directory. STATE_DIR_NAME stays
  "framenest-chatgpt-page". Do NOT touch capture APP_NAME.
Do NOT edit the 36 Alembic revision files or docs/adr/0001 through docs/adr/0084.
Do NOT rename the FrameNest* class-name hierarchy, FrameNestJsonFormatter,
  FrameNestRedactionFilter, FrameNestLogger or FrameNestConfigurationError. That
  residue is deferred by decision and is roughly 1,423 occurrences across about 95
  classes. Renaming them here is out of scope.
Do NOT add a migration. Head stays 0035.
Do NOT change poetry.lock, and do NOT move RESTORATION_REFERENCE in
  tests/contract/test_kronika_settings_parity.py.
No NUC contact of any kind, including SSH, the worker gate in any mode, and
  deploy/ubuntu/framenest-release or kronika-release in any mode. No provider contact.
  No browser or capture-browser contact. No environment repair, no dependency change.
No branch, push, tag, merge, rebase or history rewrite.
```

## The ten discipline rules, binding on this cut

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration.
2. Resolve every cited line to its literal text BEFORE classifying it.
3. A literal in a test fixture is NOT a pin. Require assertion context.
4. Pin and verify each occurrence independently. Never per file, never per function.
5. Reject any display pin that is a whole-file or whole-function regex where the
   literal occurs more than once.
6. Never truncate an inventory. If output is truncated, disclose it and reprocess.
7. Verify every mechanical probe against a known-impossible number.
8. Regenerate every verification table at report time. Never transcribe one.
9. Open and classify every grep hit. Distinguish production presence, historical
   compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

Rule 3 has two live applications here. **The retention ledger's provenance comments
under `tests/contract/test_kronika_identity_retention.py`, and any comment in the helper
or the gate that narrates what an earlier cut did, must keep the historical spelling.**
So must the comment in `tests/contract/test_kronika_settings_parity.py`. None of those
is an in-scope site.

Rule 9 has a live application too: the **new wrapper for the old gate path** and the
**old wrapper for the new engine path** both must exist, and a test that asserts the old
name is absent would be a false positive to delete rather than a finding.

## Authority

```text
Positive authority: move the engine and add the canonical entry; add and keep both gate
  paths; centralise marker resolution across every reader; create the installed-unit
  executable guard and apply it to every pointer-switching path including automatic
  rollback; make the deploy lock reclaimable by its owner; complete the durable
  analysis-identity readers; update AGENTS.md and docs/WORKER_EXECUTION_CONTRACT.md; add
  or extend tests including a hermetic Fish test; create ONE commit on local main; run
  the declared AP and JavaScript routes; run read-only Git inspection.

Negative authority: any change outside the scope boundaries above; a second commit; any
  invocation of .venv/bin/python, python, python3 or poetry run for evidence; any NUC
  contact; any provider or capture-browser contact; any execution of a kronika-capture
  command; any dependency install, update or lockfile change; any reading of private/**,
  personal Fish configuration, ~/.config/opencode, browser profiles, cookies, tokens,
  credential stores or .secrets; any write to /home/agile/meta.

Commands: Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
   6e89328640fe5477e08f17f4c31c9fc4bf261238 --operation test-focus -- <argv>`,
  `./.ap/ap exec ... --operation test`, and
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <baseline>`.
  **The baseline must be a full 40-character lowercase commit object ID.** After your
  commit the baseline becomes your commit SHA for the same operations.
  JavaScript evidence goes only through `node --test tests/*.test.js` and focused
  `node --test <path>`. Fish evidence goes only through `fish --no-config` invocations
  with a synthetic environment. Read-only Git inspection is allowed (`git status`,
  `git rev-parse`, `git log`, `git show`, `git diff`, `git ls-files`, `git grep`,
  `git ls-remote`, `git submodule status`, `git merge-base`, `git mv`); no other Git
  command. Throwaway probe files under /tmp only. Any other command must be stated in
  the report with its purpose and a confirmation that it mutated nothing.

Dependency authority: none. No lockfile change.

Git authority: exactly one commit on local main, without amend. No push.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch files
  under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `main`, HEAD `6e89328640fe5477e08f17f4c31c9fc4bf261238`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS, and
   `ap project check --baseline 6e89328...` PASS. **Stop without editing if any fails.**
2. Reproduce both baselines before editing: Python `4399 passed, 8 skipped, 3 warnings`
   and JavaScript `578 passed, 0 failed, 5 skipped`. The Python suite takes about twelve
   minutes; let it finish once. **Do not edit while a suite is running.**
3. Perform the derivation and reconcile against the sample before editing. Report
   per-category totals and every site no test exercises.
4. Prove the guard exists and works, by demonstration rather than assertion:
   - a target release **lacking** the executable the installed unit names refuses,
     **without switching the pointer and without restarting**;
   - the same for **automatic rollback**, not only explicit deploy;
   - the same when the executable comes from an **effective drop-in**;
   - a symlink in place of a regular file is **rejected**;
   - an unknown effective execution form **fails before switching**.
5. Prove the marker matrix across **every** reader: old-only, new-only, both-and-equal,
   and both-and-disagreeing. The disagreeing case must fail everywhere.
6. Prove a historical analysis row stored under the former schema spelling still
   satisfies the predicate, for **both** schema constants, with a simulated C5 writer.
7. Prove the lock behaviour: an owner-less stale lock is reclaimed or refused with a
   stated reason, and a lock owned by a live run is **not** reclaimed. Report which
   outcome you implemented and why it is safe.
8. Prove both entry points and both gate paths work: `kronika-release`, `framenest-release`,
   `kronika_nuc_worker_gate.fish`, `framenest_nuc_worker_gate.fish`. The old paths must
   still work.
9. Run the hermetic Fish test with only the new variable names, then with only the old,
   then with a conflict. Report all three.
10. Prove routine `deploy`, `rollback`, `activate-capture` and `rollback-capture` never
    invoke identity migration, install units or restart capture.
11. Run the full declared `test` operation once and `node --test tests/*.test.js` once.
    Report exact counts for both. **The JavaScript count should be unchanged unless a
    test genuinely required it; if it moves, justify each change.**
12. Run the retention module. **Part A and Part B must not move.** Report every Part C
    movement with your own measurement and its cause. The filename ledger legitimately
    changes here because paths are renamed; re-pin only what you measured.
13. Confirm `git diff --stat` touches only reported paths, and report explicitly whether
    any file under `src/kronika/**` appears and why.
14. Commit once, then run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <your commit SHA>` and `./.ap/ap exec --baseline <your commit SHA>
    --operation runtime-info`, and confirm both resolve `src/kronika/__init__.py`.

```text
Evidence tier: E2. Repository implementation with hermetic tests only. The NUC is not
  contacted, and this cut's completion does not prove the guard on a live host.
```

## Git

One commit on local `main`, parent `6e89328640fe5477e08f17f4c31c9fc4bf261238`.
Suggested subject:

```text
refactor(deploy): add the canonical release entry and complete the marker readers
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  either baseline does not reproduce; if your derivation and the sample cannot be
  reconciled before editing; if the guard cannot distinguish a stale lock from a live
  one, because an unsafe reclaim is worse than a refusal; if making a durable-identity
  reader accept both spellings would appear to require changing a writer; if any routine
  host constant, environment fallback or FrameNest* class name would have to change; if
  Part A or Part B of the ledger would move; if the JavaScript count moves without a
  stated justification; if you would need a second commit; if any step would need NUC,
  provider, browser or capture authority; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded commit.

Completion: one commit; canonical and legacy entry points both working; canonical and
  legacy gate paths both working; the marker matrix passing across every reader
  including the disagreement case; the executable guard demonstrated on explicit deploy,
  automatic rollback and drop-ins; the lock reclaiming safely or refusing with a reason;
  historical analysis rows visible under both schema spellings; no routine host constant
  changed; no FrameNest* class renamed; Part A and Part B unmoved; tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `22_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this prompt
  expires. No further implementation, no second commit, no push, no publication, no NUC
  contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `22` and exchange `01` unchanged. Then:

1. Your derivation with per-category totals, the reconciliation against the sample, and
   every site no test exercises.
2. `git diff --stat`, the commit SHA, and an explicit statement of whether any
   `src/kronika/**` file appears and why.
3. The marker matrix results for every reader, including the disagreement case.
4. The guard: its real implementation shape, and the five demonstrations from
   Verification 4, each with actual output.
5. The lock: what you implemented, why it is safe, and the demonstration from
   Verification 7.
6. The durable-analysis-identity equivalence: both constants, every reader you found by
   derivation, and the historical-row demonstration.
7. Both entry points and both gate paths working, plus the three-variable-name Fish
   matrix.
8. Documentation changes with exact paths.
9. Full Python and JavaScript counts, with per-test-file attribution for any new or
   removed test.
10. Ledger movements with your own measurement and cause; explicit confirmation that
    Part A and Part B did not move and your own `FROZEN_ALEMBIC_SHA256` key count.
11. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header, disclose
it on the first line of the report body.

## Mandatory reading

- `docs/adr/0085-kronika-sole-identity.md` in full, especially "Named frozen residues".
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`,
  section 1.5 in full, its Corrections table, and the additional-findings table entry
  about release-marker probing and the analysis filter.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/21_report_00.md`,
  sections 1 and 2, for the derivation discipline and the vacuous-guard finding.
- `deploy/ubuntu/framenest_release.py` in full. It is the primary subject.
- `deploy/ubuntu/framenest-release`, the existing wrapper, in full.
- `scripts/operator/network/framenest_nuc_worker_gate.fish` in full.
- `tests/contract/test_nuc_release_remote_contract.py` and
  `tests/contract/test_kronika_cli_and_release_readers.py`, which already exercise the
  helper and must be repointed rather than duplicated.
- `src/kronika/infrastructure/persistence/companion_review_repository.py` around lines
  780-800, and the two schema-version constants.
- `tests/contract/test_kronika_identity_retention.py`, the Part B path set and the
  Part C measurement helpers.
- `docs/WORKER_EXECUTION_CONTRACT.md` and the `AGENTS.md` Worker Execution section.
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, for the routine deployment contract this cut must not
  change.
- `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify that the guard exists and
refuses without switching, that the old engine and gate paths still work, that the
lock cannot be silently stolen from a live run, that Part A and Part B did not move, and
that no routine host constant changed.

**Publication and the routine NUC refresh are separate grants, and this cut must be
installed before C5 is attempted.** The plan's deployment gate is explicit: C1 ancestry
alone is not sufficient evidence of a safe rollback floor, because C1's marker readers
were incomplete and this cut is what completes them. **If the Cooperator later needs to
roll back past this release, the old marker filenames must still resolve.**

**One consequence to flag to the Cooperator when this cut lands:** the canonical gate
name becomes `kronika_nuc_worker_gate.fish`, and the Cooperator's Fish universals
(`KRONIKA_NUC_SSH_*`) are not yet set. The old path keeps working and the old variables
keep being read, so **nothing breaks on the day this cut is published** — the universal
migration belongs to the C7-B window and must use guarded `set -Ux` semantics, not blind
copying.