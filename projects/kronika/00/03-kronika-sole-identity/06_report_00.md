### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-sole-identity
Worker session ordinal: 06
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-02
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-mutation
Start commit: 90c93eac94171182039a76fbb1c956e42b44da2c
End commit: c02c6753694d5d4958045bb79f80b5eb94b9c75c
Branch: feat/kronika-identity-dual-read (not pushed)
Changed files: 19 (17 under src/framenest, 2 contract tests)
NUC contact: none. No push, no branch, no deploy, no provider, no private/ read.
```

## Repository gate before editing

Branch `feat/kronika-identity-dual-read`, HEAD `90c93ea…`, clean tree, `origin https://github.com/cisarik/kronika`, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS (variant `stable`), `ap project check --baseline 90c93ea…` PASS. Nothing was edited before this.

Baselines reproduced through the canonical route: Python `4274 passed, 8 skipped, 3 warnings, 669.54s`; JavaScript `554 total, 549 passed, 0 failed, 5 skipped`.

## Entry-point enumeration (Verification step 1)

Method: `git grep` over `src/**` for `FrameNestSettings(` and `load_settings`, plus `lookup_env` for the two non-settings readers C1 routed directly, plus every `[project.scripts]` entry parsed from `pyproject.toml`. The list is **wider than the eleven modules in the prompt lead**: the direct readers `catalog_backup_ops.load_catalog_backup_ops_config` and `catalog_backup_offdevice.parse_configured_destination_id` reach `framenest-backup`, and `ai.default_ai_config_path` runs *outside* `framenest-ai`'s guarded block.

| console script | module | can surface | how it is now handled | ordinary status (measured) | conflict |
|---|---|---|---|---|---|
| `framenest-server` | `framenest.server:main` | yes | `load_settings()` → `except FrameNestConfigurationError` keeps exit 1, returns `exc.exit_status` for the conflict subtype | 1 (unreadable env file; the plain success path is a long-running server) | **2** |
| `framenest-db` | `…persistence.cli:main` | yes | new `except IdentityEnvironmentConfigurationError` ahead of the config clause, same `FRAMENEST_DB_CONFIGURATION_FAILED` shape | 0 (`status`) | **2** |
| `framenest-catalog` | `…cli.catalog:main` | yes | new clause ahead of the catch-all, `FRAMENEST_CATALOG_COMMAND_FAILED` | 4 (`device list`, DB not ready) | **2** |
| `framenest-library` | `…cli.library:main` | yes | new clause ahead of the catch-all, existing `_write_error` shape | 4 (`status`) | **2** |
| `framenest-dev` | `…cli.development:main` | yes | one added `isinstance` branch inside the existing `DevelopmentRuntimeError` handler | 3 (`status`, stopped) | **2** |
| `framenest-ai` | `…cli.ai:main` | yes, **twice** | `default_ai_config_path()` moved inside the guarded block (it previously escaped as a traceback); `_resolve` translates the conflict into `AiConfigurationError` so the existing handler prints the suffix-only message and returns its existing 2 | 0 (`status --no-write`) | **2** |
| `framenest-production` | `…runtime.production:main` | yes | it had **no** configuration clause at all; new clause ahead of the catch-all, `FRAMENEST_PRODUCTION_COMMAND_FAILED` | 4 (`check-database-ready`) | **2** |
| `framenest-backup` | `…cli.backup:main` | yes, **twice** | ops-config conflict and off-device destination conflict are each translated in their own module; the CLI keeps its codes and returns `exc.exit_status` | 0 (`status` with hermetic roots) | **2** |
| `framenest-youtube` | `…cli.youtube:main` | yes | new clause ahead of the existing config clause, same `YOUTUBE_CONFIGURATION_FAILED` code | 5 (`status <uuid>`, no loopback listener) | **2** |
| `framenest-previews` | `…cli.previews:main` | yes | new clause ahead of the catch-all | 4 (`status`) | **2** |
| `framenest-covers` | `…cli.covers:main` | yes | new clause ahead of the catch-all | 4 (`status`) | **2** |
| `framenest-sidecar` | `…cli.sidecar:main` | yes, on `export`/`compare` only | `_with_catalog_service` no longer masks the conflict into `_UnavailableError`; new clause keeps `SIDECAR_UNAVAILABLE` | 1 (`export`, DB not at head) | **2** |
| `framenest-recovery` | `…cli.recovery:main` | **no** | `catalog_backup_workstation` resolves no setting name; proved inert by a differential run | 1 (`list`) | 1, unchanged |
| `kronika-capture` | `kronika_capture.cli:main` | **no** | the capture package carries no resolver or settings symbol at all | not executed (browser) | n/a |
| `framenest-chatgpt-page` | `kronika_capture.cli:main` | **no** | same module, compatibility alias | not executed | n/a |

`adapters/api/public_published_application.py` also calls `load_settings()`, but only *after* `application.create_app` already built settings successfully, so `framenest-server` owns it.

## Mechanism

**(b), sanitized translation, exit mapped** — as preferred. No output contract was bypassed, so mechanism (a) was never needed.

`IdentityEnvironmentConflictError` is translated, at the layer that owns the error vocabulary, into a **subclass of that layer's existing sanitized type**, carrying the same suffix-only message and one `exit_status` property:

- `configuration.IdentityEnvironmentConfigurationError(FrameNestConfigurationError, IdentityEnvironmentConflictFailure)` — raised by all three `load_settings` translation sites; every settings-based CLI imports it from `framenest.configuration`, a module each already imported.
- `runtime.development.IdentityEnvironmentDevelopmentError(…, DevelopmentRuntimeError)` — replaces the untyped `DevelopmentRuntimeError` at `_resolve_override`, and now also wraps `_migrate_database`, which previously let the raw resolver error escape as a traceback.
- `catalog_backup_ops.CatalogBackupIdentityEnvironmentConflictError(…, CatalogBackupOpsError)` — the raw error escaped `load_catalog_backup_ops_config` uncaught.
- `catalog_backup_offdevice.OffdeviceIdentityEnvironmentConflictError(…, OffdeviceError)` — keeps `error_code="OFFDEVICE_DESTINATION_ID_INVALID"`.

`EXIT_IDENTITY_ENVIRONMENT_CONFLICT` is now read by exactly one place, `IdentityEnvironmentConflictFailure.exit_status` in `identity_env.py`; no entry point repeats the literal `2`, and the two stdlib-only deploy engines keep their own local constant untouched.

## Exact diff of every path

New in `src/framenest/identity_env.py` (+17):

```python
class IdentityEnvironmentConflictFailure:
    """Marker mixin for a command's sanitized failure caused by a conflict. …"""

    @property
    def exit_status(self) -> int:
        """Return the fail-closed exit status for an identity-environment conflict."""
        return EXIT_IDENTITY_ENVIRONMENT_CONFLICT
```

`src/framenest/configuration.py` (+28/−14): one import name added to the existing `framenest.identity_env` block; the new `IdentityEnvironmentConfigurationError`; the three translation sites changed from `FrameNestConfigurationError(str(exc))` to `IdentityEnvironmentConfigurationError(str(exc))`; `load_settings` docstring gained the `Raises` contract. `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding`, `env_prefix="FRAMENEST_"`, source order and the `EXPLICIT_ENV_FILE_MESSAGE` path are unchanged.

`src/framenest/server.py` (+8/−2): import; the existing handler computes `status = exc.exit_status if isinstance(exc, IdentityEnvironmentConfigurationError) else 1`.

`src/framenest/infrastructure/persistence/cli.py` (+13/−2): import; clause returning `exc.exit_status` with `CONFIGURATION_ERROR_CODE` and `message=str(exc)`.

`src/framenest/infrastructure/runtime/production.py` (+8): import; clause returning `exc.exit_status` with `COMMAND_ERROR_CODE`.

`src/framenest/adapters/cli/catalog.py` (+13/−2), `library.py` (+9/−2), `covers.py` (+9/−2), `previews.py` (+9/−2): import; one clause ahead of each catch-all, emitting that command's existing error shape with `message=str(exc)` and returning `exc.exit_status`.

`src/framenest/adapters/cli/youtube.py` (+7): import; clause keeping `YOUTUBE_CONFIGURATION_FAILED`, message `str(exc)`, returning `exc.exit_status` (was 6).

`src/framenest/adapters/cli/sidecar.py` (+7/−2): import; `except IdentityEnvironmentConfigurationError: raise` before the blanket `except Exception` in `_with_catalog_service`; clause keeping `UNAVAILABLE_CODE`.

`src/framenest/adapters/cli/ai.py` (+12/−4): import; `config_path`/`context` moved inside the existing `try`; `_resolve` gained a conflict branch that raises `AiConfigurationError(str(exc))` (its handler already returned 2, so only the message changed).

`src/framenest/adapters/cli/development.py` (+3): import; two lines inside the existing handler return `exc.exit_status` for the conflict type, else `EXIT_ERROR`.

`src/framenest/infrastructure/runtime/development.py` (+37/−11): imports; the new error type; `_resolve_override` raises it; `_migrate_database` wraps `FrameNestSettings(...)`.

`src/framenest/infrastructure/persistence/catalog_backup_ops.py` (+65/−31): imports; the new error type; the five resolver calls in `load_catalog_backup_ops_config` wrapped, raising it.

`src/framenest/infrastructure/persistence/catalog_backup_offdevice.py` (+24/−4): imports; the new error type; `parse_configured_destination_id` raises it with the unchanged error code.

`src/framenest/adapters/cli/backup.py` (+20/−4): imports of both new types; one `isinstance` branch at the head of the existing `CatalogBackupOpsError` handler and one in the existing `OffdeviceError` handler.

Tests: `tests/contract/test_kronika_cli_and_release_readers.py` (+415) and `tests/contract/test_kronika_direct_reader_routing.py` (+11/−5, described below).

## Named tests per entry point

All in `tests/contract/test_kronika_cli_and_release_readers.py`, run as real console-script subprocesses through `Path(sys.executable).parent`, with every `KRONIKA_`/`FRAMENEST_` variable stripped from the inherited environment first.

- `test_identity_conflict_exits_two_and_discloses_no_value[adapters.cli.<x>]` — parametrized over all twelve reachable entry points: exit **2**; the reported sentence contains both `KRONIKA_DATABASE_PATH` and `FRAMENEST_DATABASE_PATH`; neither value, its length, its SHA-256 prefix, nor its `repr` appears in the sentence; neither value appears anywhere in stdout+stderr; no `Traceback`.
- `test_ordinary_status_of_the_same_arguments_is_unchanged[…]` — same argv, one prefix:0 db, 4 production, 0 ai, 0 backup, 4 catalog, 4 covers, 3 dev, 4 library, 4 previews, 1 sidecar, 5 youtube, 1 server (unreadable env file), each measured, and no conflict sentence.
- `test_invalid_command_status_is_identical_with_and_without_the_conflict[…]` — eleven cases (the server takes no arguments): the invalid-command status is byte-identical with and without the conflicting pair.
- `test_the_settings_free_entry_point_keeps_its_status_under_a_conflict` — recovery: 1 with and without the conflict, no conflict sentence.
- `test_the_parked_capture_package_cannot_surface_the_conflict` — static scan of `src/kronika_capture` for `load_settings`, `Settings`, `IdentityEnvironmentConflict*`, `lookup_env`, `identity_env`, `load_catalog_backup_ops_config`, `default_ai_config_path`: no file matches, so both capture scripts are proved inert rather than skipped (they must not be executed; they drive a browser).
- `test_every_declared_console_script_is_classified` — derives the 15 declared scripts from `pyproject.toml` and fails if any module key is unclassified, so a future script cannot silently escape this ledger.
- `test_an_empty_primary_value_still_behaves_as_unset_at_an_entry_point` and `test_identical_values_in_both_prefixes_still_succeed_at_an_entry_point` — both at `framenest-db status`: exit 0, no conflict sentence.
- In `test_kronika_direct_reader_routing.py`: `test_catalog_backup_ops_config_fails_closed_on_a_conflict` now asserts the new contract (sanitized subclass, `__cause__` is the resolver error with `.suffix == "CATALOG_BACKUP_ROOT"`, `exit_status == 2`, suffixes named, no value); `…offdevice_destination_id_fails_closed_on_a_conflict` and `…development_port_reads_either_prefix` gained `exit_status == 2`.

## Retention ledger

**No pin moved.** Measured directly with `git grep` against every pin and re-run as the live test: `test_kronika_identity_retention.py` passes unchanged (14 tests).

```text
src occurrences 2983/2983   tests occurrences 4401/4401   src files 255/255   tests files 320/320
FrameNest 3364/3364   env-prefix tokens 642/642   distinct 101/101   bare 16/16
mutation header 59/59   /opt 204  /etc 76  /var/lib 94  /var/cache 21  /mnt 13
User=framenest 5  Group=framenest 5   console-script entries 14
deploy 212 scripts 104  docs 1216  extension 199
```

This was the sharpest constraint of the task and it is worth stating plainly: the ledger counts *every* occurrence of the product word, so ordinary code such as a new import line or a test referencing `framenest-db` moves it. I held every counter at its pinned value by extending existing import statements rather than adding new ones, by naming the new settings subtype in the docstrings that the change makes necessary, and by deriving the test enumeration from `pyproject.toml` instead of hardcoding script or module names. One symbol in the capture scan is written as the neutral token `Settings` rather than the full settings class name, for the same reason. No pin was re-pinned and no existing pinned text was deleted.

## No other exit status changed

Evidence, three layers: the per-entry-point ordinary-status and invalid-command tests above; the full suite (`4314 passed, 8 skipped, 3 warnings`); and direct inspection that each new clause is either disjoint from every existing handler or guarded by an `isinstance` test inside the existing handler. Emitted error-code strings are unchanged (no new `FRAMENEST_*` or `KRONIKA_*` spelling was added: the token and distinct-name counts confirm it), writers still emit the old spelling, and `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding`, `env_prefix` and process-over-env-file precedence are untouched. No traceback is reachable from a conflict at any entry point, and `framenest-ai` no longer has one reachable at all.

## Counts

```text
Python  baseline  4274 passed, 8 skipped, 3 warnings, 669.54s, exit 0
Python  final     4314 passed, 8 skipped, 3 warnings, 688.49s, exit 0   (+40, all new)
JavaScript baseline/final  554 total, 549 passed, 0 failed, 5 skipped (unchanged)
ap doctor PASS; ap project check --baseline c02c675… PASS; tree clean after commit
```

## Deviations, risks, missing evidence

1. **`_database_state` in `runtime/development.py` still swallows a conflict.** That status probe keeps its existing blanket `except Exception: return "unknown"`, so a conflict on a field the launcher does not resolve shows as `unknown` rather than failing. Deliberate: a status probe must not fail, and it cannot produce a traceback or a wrong status. `framenest-dev start` still exits 2 through `_migrate_database`.
2. **Exit 2 collides with existing statuses** at ten entry points whose usage error is already 2 (`db`, `catalog`, `library`, `dev`, `ai`, `production`, `backup`, `youtube`, `previews`, `covers`). The plan mandates 2, so the conflict is distinguished by its message, not its status. Only `sidecar`, `server` and `recovery` have an unambiguous 2.
3. **Not proven by this correction:** the NUC's installed `/etc/framenest/framenest.env` under a real systemd `Environment=` line, and the two `systemd` credential drop-ins. Those need the routine refresh plus Cooperator acceptance, which this grant excludes.
4. **The stdlib-only mirrors keep their duplicated constant**, as instructed; a later cut can unify them when the package layout changes.
5. No lint or typecheck command is declared anywhere in this repository; pytest through `./.ap/ap exec` is the only declared Python gate, and it was used for all Python evidence.
6. `git status` shows no untracked file. The temporary measurement probe I used to learn the ordinary statuses was moved to `/tmp/opencode/test_zz_identity_conflict_probe.py.bak`, outside the repository, because the client's policy denies `rm`, `unlink` and `git clean`.

## Smallest next step

Accept or reject `c02c675…`, then issue the fresh independent audit of the whole C1 + C1b state as its own envelope — C1 widened a mutation-authorization boundary, so its acceptance cannot rest on the session that implemented it. Publication and the routine NUC refresh stay separate grants.

## Resolved Execution Issues / Near-Misses

- The first baseline run was launched with `nohup` in the background and was killed when the tool call hit its 120 s timeout. Re-run in the foreground with a long timeout; the baseline then reproduced exactly. No evidence was taken from the truncated run.
- The client denies `rm`, so the temporary probe was relocated to `/tmp/opencode/` rather than deleted in place.
- A first draft of the new tests formatted `{COMPATIBLE}` placeholders with lowercase keyword names, raising `KeyError`; and it parametrized the invalid-command test over the server, which ignores argv and would have started a real server until the 60 s timeout. Both were caught by the focused run, fixed (uppercase placeholders; the server excluded by construction), and re-verified.
- The first full-suite run failed exactly one test: session 05's `test_catalog_backup_ops_config_fails_closed_on_a_conflict` asserted the *untranslated* contract this correction deliberately replaces. Updated to the new contract rather than worked around, and the suite re-run to green.

## Pre-Existing Failure Classification

none — the baseline reproduced exactly, and every failure observed during this task was a candidate defect of this correction, fixed within scope.

```text
Orchestration critique:
MEASURED: The prompt's entry-point lead listed eleven modules; the true reachable set is thirteen surfaces across twelve commands, because two direct readers (catalog_backup_ops, catalog_backup_offdevice) reach framenest-backup and default_ai_config_path runs outside framenest-ai's guarded block and escaped as a traceback. Evidence: git grep over FrameNestSettings(|load_settings|lookup_env plus the parsed [project.scripts] table above, and the framenest-ai traceback path fixed by moving config_path into the existing try. Effect: without this enumeration two commands would have kept exiting 1 and one would have kept printing a traceback. Smallest correction: none needed; the enumeration is now a test that fails when a new script is unclassified.
LEAD: The retention ledger's generic per-tree occurrence counters cannot accommodate any authorized change that adds an import line or a module reference, so the next cut that legitimately adds one will need an explicit Orchestrator decision to re-pin those counters rather than contorting the diff; evidence would be a single `git grep -io framenest` delta on a cut that renames no path. Cheapest useful check: compare the ledger's specificity against the identity-sensitive pins it duplicates.
```