# Authoritative Worker prompt — Worker session 19, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `19`, exchange `01`. Stored under the
Meta filename mapping as `19_implementation_00.md`, with report destination
`19_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 19
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C3B — atomic package, distribution and executable identity move
Reasoning recommendation: High
Recommended context capacity: approximately 500k tokens
```

Rationale: `High`. This is the highest-risk cut in the whole. It moves every Python
module, renames the distribution and its metadata, renames a settings class with over
five hundred live references, changes the AP execution contract so the current
baseline stops being valid, and must relocate an installed package inside a live
virtual environment that a Worker is forbidden to repair. A single missed `include`
path silently ships a wheel with no web shell.

This is cut **C3-B** from the accepted completion plan at `17_report_00.md` section
1.4. **It must be atomic.** Splitting package movement from imports, packaging,
provenance or the migration loader would deliberately create an unusable intermediate
tree. If you cannot complete it, stop and report rather than committing half of it.

## Why this cut exists

The product is functionally Kronika. The identity is not. `src/framenest`, the
`framenest` distribution, thirteen `framenest-*` commands and a `FrameNestSettings`
class still carry the retired spelling, and ADR-0085 names them as the identity that
must change. Everything before this cut was arranged so that this one could be atomic:
C1 made the readers dual so the code could move safely, C3-A made the identity
enforced rather than merely renamed, and C2 sent both mutation headers so the browser
boundary survives a server change.

After this cut there is no `src/framenest` tree and no distribution named `framenest`.
The thirteen `framenest-*` entry points survive as aliases until C7-B, so the
installed `framenest.service` and `relocate_venv_shebangs` keep working.

## Verified current state

Every figure was measured by the Orchestrator at this commit.

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                e1d5ee510b4a1532606dba7d2a098aed71c16225
Remote origin:                https://github.com/cisarik/kronika
Public main:                  e1d5ee510b4a1532606dba7d2a098aed71c16225, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
```

Baselines at this commit:

```text
Python declared test:  4399 passed, 8 skipped, 3 warnings, 0 failed
JavaScript:            583 total, 578 passed, 0 failed, 5 skipped
Retention module:      15 passed
ap project check:      PASS at this baseline
```

**Precondition already satisfied by observation.** The plan requires that no managed
local development server is running under the old launcher before its recorded
launch-module identity changes. `framenest-dev status` on the NUC returned
`Status: stopped` and `Database: uninitialized`. State this in your report; do not
re-run it, because the NUC is out of your reach.

## Verified mutation targets

Re-derive every one of these before editing. Line numbers locate current evidence,
not durable selectors.

```text
pyproject.toml:2                   name = "framenest"                        -> "kronika"
pyproject.toml:30                  packages { include = "framenest" }        -> "kronika"
pyproject.toml:33-38               FIVE explicit include paths, see trap T2
pyproject.toml scripts             13 framenest-* entries get kronika-* siblings
ap.project.conf [runtime cpython]  provenanceModule = framenest                -> kronika
ap.project.conf operation runtime-info argv
                                  "import sys, framenest; ...; framenest.__file__"
                                                                          -> kronika
catalog_backup.py:263              version("framenest")                       -> version("kronika")
migrations.py:24                   DEFAULT_MIGRATION_PACKAGE                 -> kronika.infrastructure.persistence.alembic_environment
migrations.py:121                  ScriptDirectory.from_config               install the shim before this
structured_logging.py:19,20,95,96,101,106,111,113
                                  six framenest* logging namespace identifiers
engine.py:72,73,76                 the framenest_umask connection.info key
script.py.mako:19                  the generated downgrade message
src/kronika_capture/config.py:7    APP_NAME                                   -> "kronika-capture"
src/kronika_capture/config.py:8    STATE_DIR_NAME                             UNCHANGED, see trap T4
framenest (root launcher, 7687 bytes)  becomes a thin wrapper around a new ./kronika
```

**Measured class-name distribution.** `FrameNestSettings` occurs **504** times across
`src` and `tests` and **5** times in `docs/adr/`. Those five are inside frozen ADR
bodies. See trap T3.

**Console entry arithmetic.** `[project.scripts]` currently holds fifteen entries:
thirteen `framenest-*` application commands, plus `kronika-capture`, plus
`framenest-chatgpt-page`. After this cut it holds **twenty-eight**: the thirteen
canonical `kronika-*` commands, the thirteen retained `framenest-*` aliases,
`kronika-capture`, and `framenest-chatgpt-page`. The retained-alias count named by the
ledger, `CONSOLE_SCRIPT_ENTRY_COUNT`, counts `framenest-*` names and therefore stays
**14**. A change to that pin is a defect, not an expected movement.

## Traps — each one is a specific way this cut fails

**T1. A test that must be inverted, not updated.** `tests/contract/test_chatgpt_page_packaging.py:99`
currently reads:

```python
assert not any(name.startswith(("kronika/", "vendor/")) for name in names)
```

It **forbids** `kronika/` in the wheel. The moment the package is renamed, this
assertion fails. It must be **inverted**: require the canonical application package to
be present and forbid an installed `framenest/` package instead. Do not simply delete
the assertion. Report the final form.

**T2. Five include paths that silently gut the wheel.** `pyproject.toml` lists these
explicitly, and each must be repathed:

```text
src/framenest/infrastructure/persistence/alembic_environment/script.py.mako
src/framenest/adapters/api/web/index.html
src/framenest/adapters/api/web/styles.css
src/framenest/adapters/api/web/app.js
src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png
```

Miss one and the wheel builds cleanly while losing the web shell, the stylesheet, the
application script, the Alembic template or the AI vision fixture. **A green test
suite is not proof these survived**; prove them by building or inspecting the wheel and
listing its contents.

**T3. A repository-wide replace corrupts Part A.** These files reference `src/framenest`
and are **frozen**, hash-locked by `FROZEN_DOCUMENT_SHA256`:

```text
docs/adr/0004-repository-layout.md
docs/adr/0008-asgi-runtime.md
docs/adr/0009-structured-logging-approach.md
docs/adr/0011-stable-domain-identities.md
docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md
```

`docs/adr/0085-kronika-sole-identity.md` also references it and is **not** frozen. A
mechanical whole-repository substitution of `framenest` will change frozen bytes and
break the ledger. Scope every substitution explicitly. **Part A and Part B must not
move.**

**T4. Two adjacent lines, one identical literal, opposite destinations.** In
`src/kronika_capture/config.py`:

```python
APP_NAME = "framenest-chatgpt-page"       line 7  ->  "kronika-capture"
STATE_DIR_NAME = "framenest-chatgpt-page" line 8  ->  UNCHANGED, permanently
```

Both lines hold the same string today and they go opposite ways. `STATE_DIR_NAME` is a
named ADR-0085 frozen residue and identifies the capture state directory, which must
never move. **Change line 7 and leave line 8.** A substitution scoped to that file
rather than to the token gets this exactly backwards.

**T5. Eleven frozen revisions import a module that will no longer exist.** These import
`framenest.infrastructure.persistence.sqlite_batch_fk`:

```text
0016  0017  0018  0023  0024  0025  0026  0027  0028  0030  0031
```

Each imports it once, at line 8. Their bytes are frozen and must not change. The only
mechanism that lets them load is the process-local shim below.

**T6. `framenest_umask` is a coupled internal attribute.** `engine.py` reads, writes
and pops `connection.info["framenest_umask"]` at lines 72, 73 and 76. It is
self-contained in that one file, so the rename is low risk, but leaving a `framenest_`
prefixed key inside a module that now lives under `src/kronika/` contradicts this
cut's purpose. The plan's instruction to rename coupled internal attributes together
covers it. Change all three occurrences together or none.

**T7. The AP baseline becomes invalid the moment `ap.project.conf` changes.** The
current SHA stops being a valid `--baseline` for this worktree, because worktree and
baseline drift of the AP contract forbids execution. This is expected and is why the
re-gate below is ordered the way it is. Do not try to run the suite against the old
SHA after editing the contract.

**T8. One JavaScript test references the old path.** `tests/admin_batch_actions_frontend.test.js`
references `src/framenest`. It is a path, not prose, so C2d never touched it and C3-A
did not either. It must be repathed. Since this cut may touch JavaScript after all,
the JavaScript count need not stay identical — but **every change must be reported
individually** and justified.

## The Alembic compatibility shim

Implement it exactly as specified. This is the mechanism on which eleven frozen
revisions depend, and it is the only sanctioned way they will ever load.

```text
Expose exactly four module names, and nothing else:
  framenest                                        empty package parent
  framenest.infrastructure                         empty package parent
  framenest.infrastructure.persistence             empty package parent
  framenest.infrastructure.persistence.sqlite_batch_fk
                                                   binds kronika.infrastructure.persistence.sqlite_batch_fk

Install it idempotently, before every ScriptDirectory.from_config path, and at the
start of Alembic env.py.

Prohibited: a filesystem package alias, a broad import hook, sys.path forwarding, or
general delegation from framenest.* to kronika.*.

Required: fail closed if any of the four names is already bound to something unexpected.
```

**The alias is process-local state installed when migration status loads. It is not a
shipped `framenest` distribution, and there must be no `src/framenest` tree and no
importable general `framenest` package afterwards.** Prove both halves.

`script.py.mako` currently contains **no** `framenest` import. The accepted plan's
description of it is inaccurate on that point. Its present required edit is the
generated downgrade message. **Do not invent an import in the template** to satisfy the
plan's wording, and do not use the template to regenerate any applied revision file.

## Ordered re-gate — this sequence is mandatory

```text
1. Edit the package, tests and AP contract under this grant.
2. ./.ap/ap project check --root /home/agile/Projects/kronika --candidate
   must print exactly:  PASS (non-authorizing)
3. Commit the coherent candidate ONCE, without amend.
4. ROOT INSTALLATION REFRESH — Cooperator maintenance action, NOT a Worker action.
   Refresh only the root project installation in the existing canonical .venv.
   Preserve that environment and all of its dependencies. Remove only the obsolete
   root-distribution metadata and scripts before reinstalling the renamed project.
   Report the exact commands the Orchestrator must give the Cooperator, and stop
   there. Do not run them. Never invoke .venv/bin/python for any purpose.
5. ./.ap/ap project check --root /home/agile/Projects/kronika --baseline <new SHA>
6. ./.ap/ap exec --root /home/agile/Projects/kronika --baseline <new SHA> --operation test
   and --operation test-focus, then: node --test tests/*.test.js
7. Any correction is a NEW commit, and ITS SHA is the new baseline. --candidate never
   substitutes for step 6.
```

**Stop after step 3 and report.** Steps 5 and 6 cannot run until the Cooperator has
performed step 4, because the environment still holds the old distribution. The
Orchestrator will arrange step 4 and then commission the verification. Do not attempt
to work around the missing installation.

No dependency update and no lockfile rewrite is included in this grant.

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

Rule 3 is live here. The C3-A agreement guards deliberately reference retired class
names, because those names are correct until this cut renames them. **Those are
fixtures and inventory entries, not retired prose.** Do not "fix" them as if they were
display text, and do not count them as failures. After you rename the class, they must
be repointed, and that repointing is part of this cut.

Rule 8 has failed twice at the same value in this whole. `FROZEN_ALEMBIC_SHA256`
contains **36** keys, being revisions `0001` through `0035` plus `__init__.py`. Two
Implementation Workers reported 38. **Measure it yourself** rather than carrying any
figure from this prompt.

## Scope boundaries

Do not change any of the following. Each has a different owner in the plan.

```text
No default data location. The dev launcher paths, the AI config path, the log path and
  every default stay on the old spelling: that is C4-B and C-LOCAL.
No durable writer identifier. Backup application name, sidecar format and suffix,
  marker purposes and filenames, and the release-manifest identity key stay old:
  that is C5.
No mutation header, companion protocol, API version, CSS, DOM or port identifier:
  that is C7-A.
No Unix account, systemd unit, /opt, /etc, /var or socket change: that is C6.
No deletion of any alias, wrapper or fallback. C3-B ADDS the canonical names and
  KEEPS the old ones. C7-B removes them.
Do NOT touch capture state identity. STATE_DIR_NAME stays. Do not move or rename any
  capture state directory, profile or token path.
Do NOT edit the 36 Alembic revision files. They move; their bytes do not change.
Do NOT edit docs/adr/0001 through docs/adr/0084. See trap T3.
Do NOT edit deploy/** or scripts/**. The release helper and the NUC gate are C4-A.
Do NOT edit extension/**.
Do NOT add a migration. Head stays 0035.
No NUC contact, no provider contact, no browser or capture-browser contact.
```

## Authority

```text
Positive authority: move src/framenest to src/kronika with Git rename detection and
  edit every in-scope file listed under "Verified mutation targets" plus any file your
  own derivation shows must change, each reported explicitly; create ONE commit on
  local main; run `project check --candidate`; run read-only Git inspection; STOP after
  the commit and report the exact Cooperator commands needed for step 4.

Negative authority: any second commit in this cut; any change to any item under "Scope
  boundaries"; any edit to the 36 Alembic revision files or to docs/adr/0001 through
  docs/adr/0084; any change to any of the four excluded metadata defaults; any NUC
  contact, including SSH, the NUC worker gate, and deploy/ubuntu/framenest-release in
  every mode; any invocation of .venv/bin/python, python, python3 or poetry run for any
  purpose including as an editor; any root installation refresh; any dependency
  install, update or lockfile change; any provider or capture-browser contact; any
  execution of a kronika-capture command; any new branch, push, tag, merge, rebase or
  history rewrite; any reading of private/**, personal Fish configuration, browser
  profiles, cookies, tokens, credential stores, .secrets or ~/.config/opencode; any
  write to /home/agile/meta.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap project check --root /home/agile/Projects/kronika --candidate` before the
  commit, and after the Cooperator's step 4 through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline <new SHA> --operation <id> -- <argv>`
  and `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <new SHA>`.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`, `git mv`); no other Git command.
  Throwaway probe files under /tmp only. Any other command must be stated in the report
  with its purpose and a confirmation that it mutated nothing.

Dependency authority: none. No lockfile change.

Git authority: exactly one commit on local main, without amend. No push.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch files
  under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `main`, HEAD `e1d5ee510b4a1532606dba7d2a098aed71c16225`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS, and
   `ap project check --baseline` PASS at the current SHA. **Stop without editing if any
   fails.**
2. **Re-derive the target inventory by parsing** and reconcile against "Verified
   mutation targets" before editing. Report your count, the Orchestrator's, and every
   difference. Specifically confirm: the count of `src/framenest` modules, the count of
   `framenest-*` console entries, the number of explicit `src/framenest` include paths,
   the number of `FrameNestSettings` occurrences in `src` and `tests` separately from
   `docs/adr`, and the number of Alembic revisions importing `sqlite_batch_fk`.
3. Make the move and every in-scope edit.
4. **Prove the wheel survives.** Build or inspect the distribution and list its contents.
   Confirm all five previously-repathed resources are present: `script.py.mako`,
   `index.html`, `styles.css`, `app.js`, and the vision fixture. Confirm `kronika/` is
   present and `framenest/` is absent. **A green suite is not this proof.**
5. Confirm there is no `src/framenest` tree and that an ordinary `import framenest`
   fails, while the shim makes `framenest.infrastructure.persistence.sqlite_batch_fk`
   importable and bound to the `kronika` module.
6. Confirm a **fresh** temporary database migrates to `0035`, and that a populated
   fixture already at `0035` remains there with its `alembic_version` row unchanged.
7. **Prove the shim's alarm still works.** Construct a synthetic revision that imports
   an unrelated `framenest` module and show it **fails**. Do not add that synthetic
   revision to the repository.
8. Confirm every one of the thirteen canonical and thirteen alias entry points resolves
   to the same callable, and that the total entry count is twenty-eight with
   `framenest-*` names still fourteen.
9. Confirm `kronika_capture` is importable and its `STATE_DIR_NAME` still equals
   `framenest-chatgpt-page`, while its `APP_NAME` is now `kronika-capture`.
10. Run `./.ap/ap project check --root /home/agile/Projects/kronika --candidate` and
    confirm it prints exactly `PASS (non-authorizing)`.
11. Commit once. Confirm `git diff --stat` shows renames rather than delete-and-add for
    the moved modules, and that `docs/adr/0001` through `docs/adr/0084` appear nowhere
    in the diff.
12. Run the retention module against the new tree. **Part A and Part B must not move.**
    Report every Part C movement with its cause. In particular
    `CONSOLE_SCRIPT_ENTRY_COUNT` should remain 14, the per-tree file counts should move
    by exactly the expected path renames, and `EXPECTED_FRAMENEST_CONTENT_PATHS` should
    lose only paths that genuinely lost their last occurrence.
13. **Stop and report.** Do not attempt steps 5 and 6 of the re-gate.

```text
Evidence tier: E2 for the commit, by repository suites and package inspection. The
  post-installation suite run is commissioned separately by the Orchestrator after the
  Cooperator's maintenance action.
```

## Git

One commit on local `main`, parent `e1d5ee510b4a1532606dba7d2a098aed71c16225`.
Suggested subject:

```text
refactor(package): move the application package and distribution to kronika
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  `project check --candidate` does not print `PASS (non-authorizing)`; if your derived
  inventory cannot be reconciled with the issued targets before editing; if the wheel
  cannot be inspected or built; if any frozen ADR body or any of the 36 revision files
  would have to change; if any of the four excluded metadata defaults would have to
  change; if you would need a second commit; if you would need to repair the installed
  environment yourself; if any step would need NUC, provider, browser or capture
  authority; if context pressure reaches the point where a bounded rotation is cheaper
  than a degraded commit.

Completion: one commit; no `src/framenest` tree; no importable general `framenest`
  package; the shim present, idempotent, fail-closed, and proven to alarm on an
  unrelated import; a fresh database reaching 0035 and a populated fixture unchanged;
  all five include paths re-pathed and proven present in the wheel; twenty-eight entry
  points with `framenest-*` still fourteen; capture `STATE_DIR_NAME` unchanged;
  `candidate` PASS; Part A and Part B unmoved; frozen ADRs absent from the diff.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `19_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this prompt
  expires. No further implementation, no second commit, no push, no publication, no NUC
  contact, no environment repair and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `19` and exchange `01` unchanged. Then:

1. Your derived inventory and its reconciliation against the issued targets, naming
   every difference, including the separately counted `FrameNestSettings` figures in
   `src`/`tests` versus `docs/adr` and the measured `FROZEN_ALEMBIC_SHA256` key count.
2. `git diff --stat` with rename detection, and explicit confirmation that
   `docs/adr/0001` through `docs/adr/0084` and all 36 revision files are absent from it.
3. The final `pyproject.toml` script table and the twenty-eight entry-point count, with
   the `framenest-*` count shown to be fourteen.
4. The full wheel or sdist content listing, with all five previously-repathed resources
   explicitly confirmed present and `framenest/` confirmed absent.
5. The final form of the inverted packaging assertion from trap T1.
6. The shim implementation: the four exposed names, the install points, the
   fail-closed behaviour, and the synthetic-alarm demonstration.
7. Fresh-migration and populated-fixture evidence, with the unchanged
   `alembic_version` row.
8. The `ap.project.conf` before and after, verbatim.
9. The exact `project check --candidate` output line.
10. **The precise commands the Cooperator must run for re-gate step 4**, written so
    they can be executed without interpretation, plus a plain statement of what they
    preserve and what they remove. Do not run them.
11. Ledger movements with causes, and explicit confirmation that Part A and Part B did
    not move and that `CONSOLE_SCRIPT_ENTRY_COUNT` is unchanged.
12. Every JavaScript change, individually justified, with before and after counts.
13. The commit SHA; deviations, risks and missing evidence; and one smallest next step.

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

- `docs/adr/0085-kronika-sole-identity.md` in full, especially "Named frozen residues"
  and the decision text naming the package, distribution, provenance module and scripts.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`,
  section 1.4 in full, plus its Corrections table and the capture finding.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/18_report_00.md`,
  sections 4, 5 and 6, for the identity-derivation helper you must repoint and the
  distinction between retired prose and fixtures.
- `pyproject.toml` and `ap.project.conf` in full.
- `src/framenest/infrastructure/persistence/migrations.py` in full.
- `src/framenest/infrastructure/persistence/alembic_environment/env.py` and
  `script.py.mako`.
- `src/framenest/infrastructure/persistence/engine.py` around lines 55-80.
- `src/framenest/structured_logging.py` in full.
- `src/kronika_capture/config.py` in full.
- `tests/contract/test_chatgpt_page_packaging.py` in full.
- `tests/support/kronika_identity.py` and `tests/contract/test_kronika_product_string_agreement.py`.
- `tests/contract/test_kronika_identity_retention.py`, the ledger sections and the
  path-name and content-path helpers.
- The root launcher `framenest` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify that no `src/framenest` tree
remains, that the wheel still contains all five re-pathed resources, that the 36 frozen
revisions and the frozen ADR bodies are byte-identical, that `capture`'s
`STATE_DIR_NAME` is untouched, and that the entry-point arithmetic holds. Then the
Orchestrator will commission the Cooperator's step-4 maintenance action and the
post-installation suite, which this prompt deliberately does not authorise the Worker
to perform.