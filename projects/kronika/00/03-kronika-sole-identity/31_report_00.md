### Report for ORCHESTRATOR_CHAT

Logical whole: `kronika-sole-identity`. Session `31`, exchange `01`. Task identity `KSI-IMPL-CLOCALP`.

| Field | Value |
|---|---|
| Persistent role | `WORKER` |
| Session profile | Fresh Implementation Worker |
| Task identity | `KSI-IMPL-CLOCALP` — explicit development and AI state migration tooling |
| Status | **PASS — bounded implementation candidate, non-independent** |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Evidence tier | Implementation-grade, synthetic fixtures + declared full suite |
| Report justification | `new-mutation` |
| Start commit | `a37be37dd538afa626dbea94b074b676d0b8301c` |
| End commit | `a3977755b6d20a369f1a5c75e39bbcacd88de5c6` |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, untouched |
| Changed files | 7 (listed in section 7) |
| Commit / push / publication / deployment | One local commit; **no push**; `origin/main` remains `a37be37…`; no deployment |
| NUC, provider, browser contact | None |
| Delivery | This session only; Orchestrator stores `31_report_00.md` |

## 1. The interface as implemented

`kronika-dev migrate-identity-paths check|apply [--receipt-dir DIR]` is added to the existing development controller (`src/kronika/adapters/cli/development.py`, dispatch before any `DevelopmentRuntime` construction, so `start`/`stop`/`restart`/`status`/`open`/`logs` behavior is untouched). The engine is the one new module `src/kronika/infrastructure/runtime/local_state_migration.py`.

- `check` is read-only for state. It resolves all 12 owned source/destination classes, refuses while a live or unprovable managed process exists, reports sanitized counts only, and records the complete mapping and counts in a private receipt.
- `apply` performs the copy: sources are copied only to absent destinations, database copies are WAL-safe through the application engine boundary plus the SQLite online backup mechanism and are verified before acceptance, originals are preserved, the managed-process liveness records are excluded, explicit overrides are skipped, and an occupied destination is refused and reported per item. A repeated `apply` with its own receipt is a re-verified no-op, not a second copy.
- Receipts: `identity-paths-check.json` and `identity-paths-apply.json` under a private per-user directory (macOS `~/Library/Application Support/Kronika/local-state-migration`, Linux `${XDG_STATE_HOME:-~/.local/state}/Kronika/local-state-migration`), JSON schema 1, file mode exactly `0600`, directory created `0700`, atomic replace. A receipt directory inside the repository is refused before anything is created. The receipt is never printed; the CLI prints counts and class keys only.
- Exit mapping: `0` success; `2` identity-environment conflict (reuses `IdentityEnvironmentConflictFailure.exit_status`); `5` managed-server refusal and refused destinations; `1` other sanitized failure; `2` usage.

## 2. Resolved mapping and the defaults-unmoved proof

12 classes per platform. macOS: `macos_development_database`, `macos_development_runtime`, `macos_development_logs`, `macos_development_runtime_settings`, `macos_ai_configuration`, `macos_ai_test_state`, `macos_ai_status_snapshot`. Linux/XDG: the same seven with `xdg_` and `$XDG_CONFIG_HOME/framenest/ai` → `.../kronika/ai`. Both platforms: `temporary_development_database`, `temporary_development_runtime_settings`, `temporary_development_gallery_previews`, `temporary_development_covers`, `temporary_development_cover_thumbnails` under `<tempdir>/framenest-development` → `<tempdir>/kronika-development`. The only allowed segment changes are `FrameNest→Kronika`, `framenest→kronika`, `framenest-development→kronika-development`; plan validation fails loudly on duplicate class keys, duplicate sources, duplicate destinations, an unowned class, a non-brand pair, or a depth change, and it cannot express capture/profile/credential/media trees.

Defaults are proven unmoved by direct assertions in `test_plan_sources_still_equal_the_public_default_functions`: every dev source equals `resolve_development_paths(...)`, every AI source equals `default_ai_config_path`/`default_ai_test_state_path`/`default_ai_status_snapshot_path`, and the temporary-root sources equal `KronikaSettings` defaults under a patched `gettempdir`; every destination differs from its source. The pre-existing pins (`DEVELOPMENT_DATABASE_DIRECTORY == "framenest-development"`, the macOS/XDG runtime unit tests) are unchanged and green.

## 3. Synthetic fixture matrix and invariant assertions

All fixtures are synthetic under pytest temporary directories; no real local state was read. Exercised: macOS, XDG and temporary-root layouts; source present; source absent; destination absent; destination occupied; populated WAL database; explicit override; interrupted copy; failed copy retry; AI test-state and status-snapshot adjacency; gallery previews, covers and thumbnails; receipts. Key assertions: a WAL source with an open writer copies to a destination containing every row with `PRAGMA integrity_check = ok` and identical per-table evidence; originals keep their bytes and modes; a repeated apply keeps destination inode/mtime/size unchanged; the managed liveness records (`server-state.json`, `operation.lock`) never travel, while a nested same-named file does; an absent source creates no destination at all; capture-state, browser-profile, credential and media trees keep byte-identical digests and share no path with any source/destination; receipts are `0600` JSON carrying the mapping; CLI output never contains a synthetic private path.

## 4. Refusal demonstrations (mutation, then observed failure)

- **Managed-server-running refusal.** Mutation: the `running`/`unhealthy` raise in `_assert_managed_server_stopped` disabled. Observed: `Failed: DID NOT RAISE ManagedDevelopmentServerActiveError` for both parametrizations; the separate `conflict` branch stayed live and still passed, proving both branches are independently load-bearing.
- **Conflicting-destination refusal.** Mutation: the destination-absence check in `_apply_entry` and the finalization re-check in `_apply_database_entry` disabled. Observed: the occupied destination was overwritten and the outcome became `copied-verified` instead of `destination-occupied-refused`; the test failed. Performed twice, before and after the boundary rework, with the same observation.
- **Legacy-state empty-replacement refusal.** Mutation: `if offenders:` → `if False:`. Observed: `Failed: DID NOT RAISE LegacyStateReplacementRefusal`. The detector clears when the canonical destination exists, when the source is absent, and when the class is explicitly overridden.
- **No-capture/no-profile/no-credential boundary.** Mutation: the owned-class key-set validation disabled. Observed: a plan carrying a `capture_state` class passed validation and the assertion `outside the owned` no longer raised.
- Every mutation was reverted; the module was re-verified byte-identical (`sha256sum -c` OK) before continuing.
- Input-absence proofs: unset XDG falls back to home-relative defaults; absent overrides leave normal statuses; absent source creates nothing; absent destination yields `copy-ready`; the real `DevelopmentRuntime` with no state file proceeds (stopped), an invalid port yields a sanitized failure with the raw value absent from the message; an absent receipt directory is created `0700`.

## 5. Documentation note

Added `## Identity-Path Migration` to the repository's development guide between “Runtime Locations” and “Local `.env` …”. It names `kronika-dev migrate-identity-paths check|apply`, the read-only check, the private receipt, the absent-destination/never-overwrite/no-liveness-record/override rules, the managed-server refusal, and states that the runtime defaults themselves do not change until the later identity switch. The prompt's locator `docs/DEVELOPMENT.md` does not exist; the actual and AGENTS.md-linked surface is the root `DEVELOPMENT.md`, which was edited (disclosed in section 9).

## 6. Counts and elapsed time

| Run (declared AP route, baseline `a37be37…`) | Result | Elapsed |
|---|---|---|
| Focused set: migration, development CLI, product agreement, retention, reader routing, CLI/release readers, dev runtime, configuration, persistence boundaries | **267 passed, 0 failed** | 23.29 s |
| Full suite (`--operation test`) | **4773 passed, 8 skipped, 3 warnings, 0 failed** | 688.63 s (11 m 28.7 s wall) |
| Retention module (before staging, after staging, after commit) | **15 passed** each | 0.35 s / 0.34 s |

Baseline was 4737/8/3/0. Difference: exactly **+36 passed** (29 new migration-contract tests + 7 new development-CLI tests); skips, warnings and failures unchanged. The product-string agreement inventory moved 55→57 occurrences (in-scope 53→55; duplicate literal `"Kronika"` now 2) for the two new canonical runtime strings.

## 7. Commit data and Part A/B/C

Commit `a3977755b6d20a369f1a5c75e39bbcacd88de5c6`, subject `feat(runtime): add bounded local identity-path migration`; `git diff --stat a37be37..HEAD`:

```text
 DEVELOPMENT.md                                     |   17 +
 src/kronika/adapters/cli/development.py            |   71 +
 .../runtime/local_state_migration.py               | 1387 ++++++++++++++++++++
 tests/contract/test_development_cli.py             |  206 +++
 tests/contract/test_kronika_identity_retention.py  |   77 +-
 .../test_kronika_product_string_agreement.py       |   10 +-
 tests/contract/test_local_state_migration.py       | 1134 ++++++++++++++++
 7 files changed, 2893 insertions(+), 9 deletions(-)
```

Part A is byte-unmoved (retention Part A green; no frozen document or Alembic revision in the diff). **Part B still measures 20.** Part C movement, measured from the tree by the retention failures before re-pinning and by a scratch counting probe over the tracked set plus the two new files before commit, then confirmed by the ledger after commit:

| Part C pin | Movement | Cause |
|---|---|---|
| `src` file count | 185 → 186 | one new module containing the legacy component constants |
| `tests` file count | 184 → 185 | one new contract test containing legacy layouts |
| `src` occurrences | 1703 → 1706 | `FrameNest`, `framenest`, `framenest-development` constants in the new module |
| `tests` occurrences | 2178 → 2214 | new test: 17 `FrameNest` fixtures/assertions, 12 lowercase spellings, 7 `FRAMENEST_` override inputs |
| content paths | +2 | `src/kronika/infrastructure/runtime/local_state_migration.py`, `tests/contract/test_local_state_migration.py` |
| env prefix tokens | 688 → 695 | `FRAMENEST_DATABASE_PATH` ×4, `FRAMENEST_DEVELOPMENT_RUNTIME_DIR` ×1, `FRAMENEST_PORT` ×2 in the new test |
| distinct env names / bare spellings | unmoved (112 / 29) | all three names already exist elsewhere |
| `FrameNest` occurrences / files | 2754 → 2772 / 396 → 398 | +1 in the new module, +17 in the new test; both files enter the count |
| host paths, unit accounts, mutation header, console entries | unmoved | no host literal is touched by this cut |

## 8. Sites no test exercises

Derived from the final tree: `default_receipt_directory` (all tests inject `--receipt-dir`; the platform default is computed but never asserted); the symlinked receipt-directory refusal; the `_repository_root` `Path.cwd()` `OSError` branch; `MigrationPlan.by_key` missing-key `KeyError`; `LocalStateMigration.receipt_directory` property; the source-symlink and nested-symlink refusal statuses (`source-symlink-refused`); the database-copy failure refusal after the boundary rework (file/directory copy failure is tested); the `_destination_matches_evidence` directory-refusal catch and the malformed-prior-evidence branches of `_prior_evidence`; the post-`os.replace` digest-mismatch self-removal path. The `kronika` Fish wrapper does not route `migrate-identity-paths` (reachable through `kronika-dev` only); wrapper routing and the stale `framenest-dev` argparse prog name are C7-B/documentation surfaces, not this cut.

## 9. Deviations, risks, missing evidence, smallest next step

- **Path deviation:** the prompt's `docs/DEVELOPMENT.md` locator does not exist; the documentation surface is the root `DEVELOPMENT.md`.
- **Further directly-affected test module edited:** `tests/contract/test_kronika_product_string_agreement.py` (named here). Two occurrence rows added and the counts re-pinned; the added strings are canonical and no legacy spelling moved there.
- **Boundary defect caught by the suite (candidate defect, fixed within authority):** the first implementation imported `sqlite3` outside the persistence package and `tests/unit/test_persistence_boundaries.py::test_sqlalchemy_and_alembic_imports_are_confined_to_persistence_package` failed (`local_state_migration.py: ['sqlite3']`). Fixed by routing the copy and evidence through the application engine boundary (`create_sqlite_readonly_engine`/`create_sqlite_engine` plus the SQLite online backup); that boundary test was **not** edited. The intermediate `catalog_backup` route was probed and rejected on evidence: the product's bundle verifier refuses a WAL snapshot's `-wal`/`-shm` siblings (product catalogs are journal-mode DELETE).
- **Git mechanics:** exactly one `git add` of the seven exact paths; the post-staging repair meant the index held earlier blobs, so the single `git commit` was given the same explicit pathspecs; all seven committed blobs were verified byte-identical to the working tree (`sha256sum` equality).
- **Risks / limitations:** the engine boundary requires the application's private modes on a source catalog (directory `0700`, file `0600`); a non-private legacy catalog is refused fail-loud rather than opened. A WAL source whose `-shm` is missing with no writer is untested. Receipts accumulate (one check plus one merged apply receipt per directory by design).
- **Scratch artifacts:** probe scripts and a pristine copy remain under `/tmp/opencode` (outside the repository); the session permission layer denied their deletion. They affect no repository state.
- **Missing evidence:** no macOS execution; darwin correctness rests on synthetic fixtures plus equality with the public default functions. No real installation was touched.
- **Smallest next step:** acceptance of this candidate, then issue **C-LOCAL-H** for the Cooperator-identified installations; `C7-B` must retain `refuse_silent_legacy_state_replacement` when the defaults switch.

### Resolved Execution Issues / Near-Misses

- The anchor map did not name `tests/unit/test_persistence_boundaries.py`; a green focused set was not sufficient and the first full-suite candidate was red exactly there. Fixed within scope; no test amended to hide it.
- `Connection.driver_connection` does not exist in the installed SQLAlchemy; the documented `connection.connection.driver_connection` was used and both journal modes were probed before re-running.
- Mutation demonstrations used temporary source edits with byte-hash verification because `git checkout`/`restore` is not authorized.
- The `catalog_backup` route was abandoned on measured evidence (WAL snapshot siblings inside the bundle) rather than patched, because that module is outside this cut's authority.

### Pre-Existing Failure Classification

None. The declared baseline route was green at `a37be37…` (4737/8/3/0; retention 15 passed re-verified in this session), the single observed failure was a candidate defect introduced by this cut and fixed within authority, and the final suite is green at the reported commit. No failure is parked or attributed to pre-existing debt.

Orchestration critique:  
**MEASURED:** The prompt's anchor map omits architecture-boundary test modules of the touched package. Evidence: the first full candidate failed only `tests/unit/test_persistence_boundaries.py` with `local_state_migration.py: ['sqlite3']`, while every listed focused module was green. Effect: the listed surfaces alone cannot certify a new in-package module. Smallest correction: include the touched package's boundary/agreement modules in the anchor map or say that directly affected modules may be edited by disclosure, as was done here.  
**LEAD:** The retained `kronika` Fish wrapper cannot reach `migrate-identity-paths`, so C-LOCAL-H must run through `kronika-dev` (or a later wrapper/documentation cut adds routing). Cheapest useful check: decide that invocation path when issuing the C-LOCAL-H grant.

All authority under this Worker prompt expires on submission of this report.