# Authoritative Worker prompt — Worker session 31, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `31`, exchange `01`. Stored under the
Meta filename mapping as `31_implementation_00.md`, with report destination
`31_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 31
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-CLOCALP — explicit development and AI state migration tooling
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This cut creates the only repository tooling that will copy
the Cooperator's local development catalogs, AI configuration and derived state
to canonical destinations before `C7-B` changes the defaults. A mistake here
does not produce a red test; it loses or orphans local state. The tooling must
never overwrite, never guess which database is authoritative and never silently
create an empty replacement catalog.

This is work item **C-LOCAL-P** from the accepted closure plan at
`25_report_00.md` sections 2.7 and 1.8.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
sections 2.7 and 1.8 are your specification. Read both in full. Required
outcomes:

1. **One bounded interface.** Add `kronika-dev migrate-identity-paths` with
   `check` and `apply`, alongside the existing `start`/`stop`/`restart`/`status`/
   `open`/`logs` commands, without changing any existing command behavior. It is
   not a general filesystem tool and is not reachable from ordinary start/stop.
2. **Canonical mapping in the owned defaults only.** Replace the brand component
   in exactly these classes: `FrameNest` → `Kronika`, lowercase `framenest` →
   `kronika`, and `framenest-development` → `kronika-development`. Applies to:
   - the macOS development database, runtime and log directories
     (`~/Library/Application Support/FrameNest/...`, `~/Library/Logs/FrameNest/...`);
   - the Linux/XDG development data, state and log directories
     (`$XDG_DATA_HOME/FrameNest/...`, `$XDG_STATE_HOME/FrameNest/...`);
   - the default temporary development root
     (`<tempdir>/framenest-development/...`) including the development database,
     runtime settings, gallery previews, accepted cover storage and cover
     thumbnails;
   - the macOS AI configuration (`.../Application Support/FrameNest/ai/config.json`)
     and the lowercase Linux/XDG AI directory (`.../framenest/ai/config.json`);
   - the adjacent owned AI test-state and status-snapshot paths.
3. **Defaults do not change in this cut.** The current default path functions
   keep returning the legacy locations; `C7-B` switches them after `C-LOCAL`
   receipts exist. `check` and `apply` compute the canonical destinations
   independently from the same platform/XDG/temp-root rules and the migration
   receipt records the verified source/destination mapping.
4. **`check` is read-only for state.** It resolves each owned source/destination
   pair, reports sanitized counts (how many sources exist, how many destinations
   are absent/occupied), and records the mapping in a private receipt. It never
   prints private paths, media names, identifiers or file contents. It refuses
   to run while the managed development server is running.
5. **`apply` copies only to absent destinations.** It preserves originals, never
   overwrites a conflicting destination (refuse and report that item), copies
   consistent databases (WAL-safe through the application engine or the SQLite
   backup mechanism, verified after the copy), and leaves every explicitly
   overridden path unchanged. It must not copy live PID/runtime liveness records
   (do not revive a dead process), and must not touch the frozen capture state
   directory, browser profiles, credentials or source media — prove that by
   refusal and by test.
6. **Legacy-state refusal safeguard.** Implement a callable detector that, when
   a canonical destination is absent while matching legacy state exists, refuses
   to silently create an empty replacement. `C7-B` will retain it when the
   defaults switch; test it directly now.
7. **Receipts and idempotence.** Receipts are private (mode `0600`), outside the
   repository, and identify the verified source/destination mapping and
   integrity evidence. A repeated `apply` with receipts is a verified no-op, not
   a second copy.
8. **Documentation.** Add a short note to `docs/DEVELOPMENT.md` describing the
   `migrate-identity-paths check|apply` operation and that the defaults remain
   the legacy locations until `C7-B`. Keep it consistent with the document's
   style.

## Verified starting state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                a37be37dd538afa626dbea94b074b676d0b8301c
Public main:                  a37be37dd538afa626dbea94b074b676d0b8301c, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at a37be37:   4737 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
```

Anchor map, verified at `a37be37` (locators, not an inventory — re-derive):

```text
configuration.py:47          DEVELOPMENT_DATABASE_DIRECTORY = "framenest-development"
configuration.py:48-51       database filename, runtime settings filename,
                             gallery preview / covers / cover thumbnails directories
configuration.py:102-131      _default_database_path, _default_gallery_preview_cache_path,
                             _default_cover_storage_root, _default_cover_thumbnail_cache_path
                             (all under Path(tempfile.gettempdir()))
infrastructure/runtime/development.py:711,732,753
                             _database_path, _runtime_dir, _log_path with the macOS
                             Application Support / Library Logs and XDG components
infrastructure/ai/configuration.py:152,182,187
                             default_ai_config_path (macOS FrameNest/ai, Linux
                             framenest/ai), default_ai_test_state_path,
                             default_ai_status_snapshot_path
adapters/cli/development.py:37-55
                             the dev parser (start/stop/restart/status/open/logs)
```

Known test surfaces to derive and reconcile (locators): `tests/unit/test_configuration.py`,
`tests/unit/infrastructure/runtime/test_development_runtime.py`,
`tests/contract/test_development_cli.py`,
`tests/contract/test_kronika_direct_reader_routing.py`,
`tests/contract/test_kronika_cli_and_release_readers.py`,
`tests/contract/test_ai_server_composition.py`, and the retention ledger.

**No host contact and no personal-state inspection.** All fixtures are synthetic:
macOS, XDG and temporary-root layouts built under test-owned directories. Never
read the Cooperator's real development state, AI configuration, capture state,
profiles or credentials.

## Authority

```text
Positive authority: edit `src/kronika/configuration.py` ONLY if a shared
  canonical constant is required and WITHOUT changing any current default;
  edit `src/kronika/infrastructure/runtime/development.py`; add exactly one new
  module `src/kronika/infrastructure/runtime/local_state_migration.py`; edit
  `src/kronika/infrastructure/ai/configuration.py`; edit
  `src/kronika/adapters/cli/development.py`; edit `docs/DEVELOPMENT.md`;
  edit `tests/unit/test_configuration.py`,
  `tests/unit/infrastructure/runtime/test_development_runtime.py`,
  `tests/contract/test_development_cli.py`,
  `tests/contract/test_kronika_direct_reader_routing.py`,
  `tests/contract/test_kronika_cli_and_release_readers.py`,
  `tests/contract/test_ai_server_composition.py`; add
  `tests/contract/test_local_state_migration.py`; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this cut moved, with the arithmetic
  cause stated. Any further test module directly affected must be named in the
  report before editing it.

Negative authority: every other path; `deploy/ubuntu/kronika_release.py` and
  `src/kronika/infrastructure/persistence/engine.py` are frozen; any change to
  the current default locations or their behavior; any dependency or lockfile
  change; any change to `pyproject.toml`, `ap.project.conf` or the `.ap`
  gitlink; any frozen document or Alembic revision; publication; push; force;
  amend; branch; stash; any NUC contact or SSH; any real local-state, catalog,
  AI-configuration, capture-state, profile or credential access; any provider,
  browser or capture contact. If a necessary change falls outside the positive
  scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline a37be37dd538afa626dbea94b074b676d0b8301c --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `sqlite3`, including as a text
  editor.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only. No host,
  service, database, provider, browser or account side effect.
Browser authority: none.
```

## Verification

1. **Synthetic layout matrix.** Build macOS, XDG and temporary-root fixtures
   under test-owned directories and exercise: source present; source absent;
   destination absent; destination occupied (refuse, leave untouched); populated
   WAL database copied consistently and verified; explicit override left
   unchanged; interrupted copy recovered without corruption; adjacent AI
   test-state and status-snapshot paths; gallery previews, covers and thumbnails
   under the temporary root; receipt private and idempotent second apply.
2. **Refusals with teeth.** The managed-development-server-running refusal, the
   conflicting-destination refusal, the legacy-state empty-replacement refusal,
   and the no-capture/no-profile/no-credential boundary must each fail when
   their protection is removed, named with the mutation and the observed
   failure. Whenever a guard reads a path or an environment value, prove what
   happens when the input is absent.
3. **The defaults did not move.** Prove with direct assertions that the current
   default path functions still return the legacy locations, so the migration
   tooling cannot be mistaken for the `C7-B` switch.
4. Run, through the declared route: the focused modules, then the declared full
   Python suite, then the retention module. Report every count, elapsed time and
   any difference from the `4737/8/3/0` baseline.
5. Report **every moved or removed site that no test exercises**, and every
   caller your derivation found that this prompt's sample did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and per-file
   cause for any Part C movement (the new code must reference the legacy names to
   migrate them, so `src` movement is expected — re-pin from the tree, never
   from memory).

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

**Collapsing pairs.** For every mapping or acceptance set this cut touches, name
whether a collapse raises or fails silently; the source/destination mapping must
fail loudly on ambiguity or duplication.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a necessary change would move a current default (that belongs to
  C7-B); if a required change falls outside the positive scope; if a real local
  state or personal file would have to be read; if a frozen hash, Part A or
  Part B moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if context pressure reaches the point where a bounded rotation
  is cheaper than a degraded result.

Completion: the bounded interface implemented and tested with synthetic
  fixtures; refusals demonstrated with named mutations; defaults proven
  unmoved; documentation note added; focused modules, full declared Python
  suite and retention module green through the declared route; one local commit;
  report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `31_report_00.md` in
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
echoing `kronika-sole-identity`, session `31` and exchange `01` unchanged. Then:

1. The interface as implemented: commands, receipt format and privacy mode.
2. The resolved source/destination mapping across macOS, XDG and temporary-root
   classes, with the defaults-unmoved proof.
3. The synthetic fixture matrix and the invariant/privacy assertions.
4. Refusal demonstrations, each with its named mutation.
5. The documentation note and its location.
6. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
7. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and Part C
   movement with cause.
8. Every site no test exercises.
9. Deviations, risks, missing evidence, and one smallest next step.

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
  sections 2.7 and 1.8 in full.
- `src/kronika/configuration.py` — the development defaults and the temporary
  root functions.
- `src/kronika/infrastructure/runtime/development.py` — the launcher path
  functions and the managed-process state.
- `src/kronika/infrastructure/ai/configuration.py` — the AI path functions.
- `src/kronika/adapters/cli/development.py` — the command surface you extend.
- The test modules named in the anchor map.
- `docs/DEVELOPMENT.md` — the documentation surface.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, any real local state under the
Cooperator's home or temporary directories.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the defaults are
unmoved; the migration copies only to absent destinations and refuses conflicts;
the legacy-state safeguard exists and is tested; no real personal state was
read; the full suite is green at the reported commit; and Part A and Part B are
unmoved. `C-LOCAL-H` (the Cooperator-identified local installations) remains a
separate later grant, and the default switch remains `C7-B`.
