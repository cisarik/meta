### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `05`
Worker exchange ordinal: `01`
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C1 — dual-read identity resolver, both mutation header spellings, both durable artifact spellings, old writers unchanged
Phase-qualified result: `not-applicable`
Logical-whole closure: `not-closed`
Report justification: `new-mutation`
Branch: `feat/kronika-identity-dual-read`
Commit: `90c93eac94171182039a76fbb1c956e42b44da2c`, parent `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`
Changed files: 21 (14 source, 6 new test, 1 pin update), `+2562 / −78`
NUC contact: none, by design

## Repository gate

Re-verified before editing and again after the commit: branch `main` at `18c357c…`, clean tree, `origin` `https://github.com/cisarik/kronika`, public `refs/heads/main` and `refs/heads/docs/adr-0085-kronika-sole-identity` both `18c357c…`, `.ap` gitlink and submodule HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `./.ap/ap doctor` PASS (governing variant `stable`), `./.ap/ap project check --root … --baseline 18c357c…` PASS. `ap.project.conf` `projectId` `cisarik/kronika`, `provenanceModule` `framenest`. Python evidence used only `./.ap/ap exec --root /home/agile/Projects/kronika --baseline 18c357c… --operation {test,test-focus,runtime-info}`; JavaScript used `node --test tests/*.test.js`. No interpreter was invoked directly.

## Exact diff of every path

```
deploy/ubuntu/framenest_release.py                 | 108 +++-
deploy/ubuntu/production_ai_deploy.py              |  54 +-
src/framenest/adapters/api/tailscale_ingress.py    |  32 +-
src/framenest/application/ports/media_sidecar_store.py |  16 +
src/framenest/configuration.py                     | 137 ++++-
src/framenest/domain/media_sidecar.py              |  10 +-
src/framenest/identity_env.py                      | 122 +++++  (new)
src/framenest/infrastructure/ai/configuration.py   |  14 +-
src/framenest/infrastructure/filesystem/media_sidecar.py | 20 +-
src/framenest/infrastructure/persistence/catalog_backup.py | 17 +-
src/framenest/infrastructure/persistence/catalog_backup_offdevice.py | 32 +-
src/framenest/infrastructure/persistence/catalog_backup_ops.py | 11 +-
src/framenest/infrastructure/persistence/catalog_backup_workstation.py | 33 +-
src/framenest/infrastructure/runtime/development.py | 28 +-
tests/contract/test_kronika_cli_and_release_readers.py    | 296 +++++++++++ (new)
tests/contract/test_kronika_direct_reader_routing.py     | 224 +++++++  (new)
tests/contract/test_kronika_durable_artifact_readers.py  | 553 +++++++ (new)
tests/contract/test_kronika_identity_dual_read.py        | 510 +++++++ (new)
tests/contract/test_kronika_mutation_header.py           | 257 ++++++  (new)
tests/unit/test_identity_env.py                          | 134 ++++   (new)
tests/contract/test_kronika_identity_retention.py        |  32 +-
```

No `docs/**`, no ADR, no `AGENTS.md`, no `pyproject.toml`, no `ap.project.conf`, no `deploy/systemd/**`, no Alembic file, no `src/kronika_capture/**`. Verified with `git diff --cached --stat` over exactly those paths: empty.

## Reader files touched and the `FRAMENEST_` occurrences routed

| File | Occurrences routed through the resolver | Reader sites |
|---|---|---|
| `src/framenest/configuration.py` | 2 (`FRAMENEST_` prefix in `env_prefix`, `FRAMENEST_ENV_FILE` literal) | all 43 model fields via `_DualPrefixEnvSettingsSource`/`_DualPrefixDotEnvSettingsSource`; env-file bootstrap via `lookup_env("ENV_FILE")` |
| `src/framenest/infrastructure/persistence/catalog_backup_ops.py` | 5 | `FRAMENEST_DATABASE_PATH`, `_CATALOG_BACKUP_ROOT`, `_CATALOG_RESTORE_VERIFY_ROOT`, `_CATALOG_BACKUP_OPS_ROOT`, `_CATALOG_BACKUP_KEEP_AUTO` |
| `src/framenest/infrastructure/persistence/catalog_backup_offdevice.py` | 1 | `FRAMENEST_CATALOG_OFFDEVICE_DESTINATION_ID` |
| `src/framenest/infrastructure/ai/configuration.py` | 1 | `FRAMENEST_AI_CONFIG_PATH` |
| `src/framenest/infrastructure/runtime/development.py` | 4 read (9 occurrences, 5 kept as writer constants) | `FRAMENEST_DATABASE_PATH`, `_PORT`, `_DEVELOPMENT_RUNTIME_DIR`, `_DEVELOPMENT_LOG_DIR` read; the same four literals at lines 468–470 stay as the spawned-child writer names |
| `deploy/ubuntu/production_ai_deploy.py` | 1 | `FRAMENEST_PRODUCTION_SSH_TARGET` |
| `deploy/ubuntu/framenest_release.py` | 3 (missed readers, see below) | `FRAMENEST_NUC_SSH_TARGET`, `_NUC_SSH_USER`, `_NUC_SSH_IDENTITY` |
| `src/framenest/configuration.py` (writer path) | kept | `env FRAMENEST_ENV_FILE=` injection and `ENV_FILE` constant value unchanged |

## Readers the plan and this prompt both missed

Three, all in `deploy/ubuntu/framenest_release.py:1117-1119`: `FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER`, `FRAMENEST_NUC_SSH_IDENTITY`. The accepted plan's C1 list names only "the release helper's injected env-file name" and assigns the `*_NUC_SSH_*` dual read to C4's new Fish gate; the release engine's own three reads were not assigned to any cut. They are inside this cut's authorized file and are the identical pattern, so I routed them and report them here. C4 remains free to add the hermetic `--no-config` Fish test; it is unaffected.

Deliberately **not** routed, with reasons: `deploy/ubuntu/framenest-catalog-export-v1` *exports* (writes) `FRAMENEST_DATABASE_PATH` and friends — a writer; `scripts/operator/infosec/*.sh` and `scripts/operator/network/framenest_mullvad_egress.sh` read operator-tool variables (`FRAMENEST_LOG_UNIT`, `FRAMENEST_CURL_BIN`, `FRAMENEST_NETWORK_TEST_*`), not application settings, and are outside this cut's edit surface; `scripts/operator/network/framenest_nuc_worker_gate.fish` is C4's declared cut; `deploy/systemd/framenest.env.example` and `framenest-research-credential.conf` are templates; `src/framenest/adapters/cli/*.py` and `infrastructure/runtime/production.py` hold emitted `FRAMENEST_*` error-code strings that must stay on the old prefix until C7; `x_acquisition.py` and `media_analysis_lifecycle.py` occurrences are prose.

## The dual-prefix settings source, and how it was verified against the installed API

I read the installed library rather than assuming a signature:
`~/.venv/lib/python3.13/site-packages/pydantic_settings/main.py` (`_settings_init_sources` builds `init, env, dotenv, file_secret` then calls `settings_customise_sources`; `_settings_build_values` does `state = deep_update(source_state, state)`, so **earlier sources win**), `sources/base.py` (`PydanticBaseEnvSettingsSource`, `PydanticBaseEnvSettingsSource._extract_field_info` — which applies `_apply_case_sensitive` to `env_prefix + field_name`, `sources/providers/env.py` (`EnvSettingsSource.__init__` ends with `self.env_vars = self._load_env_vars()`), and `sources/providers/dotenv.py` (`DotEnvSettingsSource._read_env_files`, and the `__call__` extras loop that depends on `env_prefix` and on the raw lower-cased file keys).

Mechanism: two subclasses of the library's own sources, sharing one field walk, installed through the documented `settings_customise_sources` hook.
- `_IdentityResolverFieldMixin._identity_suffix` converts the internal environment key back to a setting-name suffix and returns `None` for any key outside the internal prefix, refusing to guess.
- `_DualPrefixEnvSettingsSource._load_env_vars()` returns `resolver` values keyed by the library's internal `framenest_<field>` name, so complex decoding, strict coercion, case-insensitive mapping and the `__call__` contract are inherited unchanged.
- `_DualPrefixDotEnvSettingsSource._load_env_vars()` keeps the file keys the library already read and adds the resolver's per-field values, so `env_file_encoding` and the `env_prefix` extras handling are untouched. It resolves through `canonical_identity_environment`, because the library lower-cases file keys and `lookup_env` is deliberately case-exact.
- `settings_customise_sources` returns `(init, dual-env, dual-dotenv, file_secret)` — the library default order.

No API limitation blocked this; nothing had to be degraded. The pinned API guard is `test_dual_prefix_sources_hook_the_installed_pydantic_settings_api` (asserts `VERSION.startswith("2.14.")` and the four seams) plus `test_configured_source_order_keeps_process_environment_over_env_file`.

**Deliberate deviation, stated plainly:** the prompt asked to *replace* `env_prefix="FRAMENEST_"`; I kept it, as the internal key spelling only. `env_prefix=""` would have made `_extract_field_info` produce bare field names, so any ambient `PORT`, `HOST` or `HOSTNAME` in the process environment would silently become application configuration. Retaining the prefix keeps the accepted name set exactly as it is. `test_bare_unprefixed_process_variables_are_not_read` proves no widening. `ENV_PREFIX_BARE_SPELLING_COUNT` therefore still counts the `env_prefix` literal, which is why that pin moved only from new-file prose.

## Preserved behaviours

- `hide_input_in_errors=True`, `env_file_encoding="utf-8"`, `extra="ignore"`, `env_prefix` — unchanged in `model_config`; asserted directly by `test_hide_input_in_errors_is_preserved`, `test_env_file_encoding_is_preserved`, `test_extra_ignore_is_preserved`.
- Process environment overrides environment-file values — unchanged source order, asserted by `test_configured_source_order_keeps_process_environment_over_env_file` and behaviourally by `test_process_environment_still_overrides_environment_file_values` and `test_environment_file_still_applies_without_a_process_override`.
- The `KRONIKA_` prefix does not weaken secret containment. The resolver's own error is translated at each boundary into that boundary's existing sanitized error type, so no command boundary regressed to a traceback.

## Named test for each Verification step 6 item

All in `tests/unit/test_identity_env.py` (14), `tests/contract/test_kronika_identity_dual_read.py` (29), `tests/contract/test_kronika_mutation_header.py` (16), `tests/contract/test_kronika_durable_artifact_readers.py` (21), `tests/contract/test_kronika_cli_and_release_readers.py` (21), `tests/contract/test_kronika_direct_reader_routing.py` (14). Total new 115.

| Required proof | Test |
|---|---|
| `KRONIKA_` alone works for a settings field | `test_kronika_prefix_alone_configures_a_settings_field` |
| `FRAMENEST_` alone still works for the same field | `test_framenest_prefix_alone_still_configures_the_same_field` |
| the installed `/etc/framenest/framenest.env` shape | `test_installed_environment_file_shape_keeps_working_unchanged`, `test_every_uncommented_key_in_the_installed_shape_is_still_accepted`, `test_the_same_shape_with_the_new_prefix_also_works` (the first two read the real `deploy/systemd/framenest.env.example`) |
| identical values in both prefixes accepted | `test_identical_values_in_both_prefixes_are_accepted`, `test_identical_env_file_selection_in_both_prefixes_are_accepted` |
| conflict fails closed, no value in message or log | `test_conflicting_field_values_fail_closed_without_revealing_a_value` (asserts `caplog.records == []`), `test_conflicting_env_file_selection_fails_closed_before_the_file_opens`, `test_secret_field_conflict_never_appears_in_a_validation_error` |
| exit 2 for a CLI path | `test_ai_deploy_helper_conflict_exits_two` (exit 2, suffixes only, on stdout and stderr), `test_release_helper_conflict_fails_closed_with_status_two`, `test_release_helper_transport_conflict_is_reported_not_raised_as_traceback` |
| empty string behaves as unset | `test_empty_value_behaves_as_unset`, `test_empty_env_file_selection_behaves_as_unset`, `test_empty_value_counts_as_unset_for_the_primary_prefix` / `…_compatible_prefix`, `test_both_empty_counts_as_unset`, `test_catalog_backup_ops_config_treats_an_empty_value_as_unset` |
| unknown extra `KRONIKA_` variable does not raise | `test_unknown_extra_primary_prefix_variable_does_not_raise` |
| `SecretStr` value never leaks under either prefix | `test_secret_field_value_never_appears_in_a_validation_error[KRONIKA_|FRAMENEST_]`, `test_secret_field_resolves_under_both_prefixes[…]` |
| both header spellings authorize | `test_either_spelling_authorizes_a_real_mutation[…]` (end-to-end, both names), `test_both_spellings_together_authorize_a_real_mutation`, `test_either_spelling_alone_authorizes`, `test_both_present_and_correct_authorizes` |
| `x-kronika-request` with a wrong value rejected | `test_new_spelling_with_a_wrong_value_is_rejected`, `test_wrong_value_on_the_new_spelling_is_rejected` |
| `x-framenest-request` with a wrong value still rejected | `test_old_spelling_with_a_wrong_value_is_still_rejected`, `test_wrong_value_on_the_old_spelling_is_rejected` |
| both present with one wrong value rejected | `test_both_spellings_with_one_wrong_value_is_rejected`, `test_both_present_with_one_wrong_value_is_rejected` |
| old-name backup manifest still verifies | `test_old_name_backup_manifest_still_verifies` |
| new-name manifest also verifies | `test_new_name_backup_manifest_also_verifies` |
| sidecar reader both spellings | `test_sidecar_reader_accepts_both_format_spellings[…]`, `test_sidecar_store_observes_both_filename_spellings`, `test_sidecar_reader_still_rejects_an_unknown_format`, `test_sidecar_store_reports_missing_when_no_accepted_name_exists` |
| off-device marker both spellings | `test_offdevice_marker_reader_accepts_both_spellings[…]`, `test_offdevice_marker_reader_still_rejects_an_unknown_purpose`, `test_offdevice_marker_reader_fails_closed_on_an_unsafe_accepted_name` |
| workstation marker both spellings | `test_workstation_marker_reader_accepts_both_spellings[…]`, `test_workstation_store_init_accepts_a_marker_under_the_new_spelling`, `test_workstation_marker_reader_still_rejects_an_unknown_purpose` |
| release-manifest key and release-marker filename both spellings | `test_manifest_release_sha_is_read_under_both_keys[…]`, `test_release_marker_probe_accepts_both_spellings`, `test_release_marker_probe_prefers_manifest_over_sha`, `test_manifest_release_sha_absent_key_returns_none` |
| no writer emits a `KRONIKA_` spelling | `test_backup_manifest_writer_keeps_the_former_application_name`, `test_sidecar_writer_keeps_the_former_format_and_suffix`, `test_offdevice_marker_writer_keeps_the_former_spelling`, `test_workstation_marker_writer_keeps_the_former_spelling`, `test_release_markers_and_manifest_keys_keep_their_writer_spelling`, `test_release_read_commands_keep_the_writer_marker_names`, `test_release_helper_still_injects_the_old_env_file_name`, `test_protocol_magic_and_version_reads_are_unchanged`, `test_development_database_directory_is_unchanged`, `test_emitted_cli_error_codes_stay_on_the_former_prefix`, `test_catalog_cli_error_codes_stay_on_the_former_prefix`, `test_development_spawned_child_environment_keeps_the_old_names`, `test_ai_config_environment_name_constant_is_unchanged`, `test_env_file_environment_variable_constant_is_unchanged` |

`FNCBE01`, `version("framenest")`, `DEVELOPMENT_DATABASE_DIRECTORY`, the emitted `FRAMENEST_*` code strings, the injected `env FRAMENEST_ENV_FILE=`, `ENV_FILE`, `RELEASE_ROOT` and `SERVICE` are all asserted unchanged. The `.kronika-*` spellings added in this cut are, exhaustively: the resolver's two accepted prefixes and their two variable names; the second accepted header name; the read-only constants `COMPATIBLE_*`/`ACCEPTED_*` in the six reader modules; and the two stdlib-only mirrors in the deploy engines. No newly written durable artifact, error code, or sent header uses them.

## Retention test pin changes and their causes

`tests/contract/test_kronika_identity_retention.py`, all measured, all caused by this cut:

| Pin | Was | Now | Cause |
|---|---|---|---|
| `PER_TREE_FRAMENEST_FILE_COUNT["src"]` | 254 | 255 | new `src/framenest/identity_env.py` |
| `["tests"]` | 314 | 320 | six new test modules |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2975 | 2983 | the new module plus the accepted-spelling constants in six reader modules |
| `["tests"]` | 4223 | 4401 | the six new test modules |
| `["deploy"]` | 218 | **212** | the four `FRAMENEST_*` operator-variable literals in the two stdlib-only engines are now composed from the prefix constant, so they no longer appear as literals |
| `ENV_PREFIX_TOKEN_COUNT` | 637 | 642 | new reader/writer-constant and test mentions |
| `ENV_PREFIX_DISTINCT_NAME_COUNT` | 102 | **101** | `FRAMENEST_PRODUCTION_SSH_TARGET` is no longer a literal anywhere, being composed as prefix + suffix |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 2 | 16 | the two new prefix literals in `identity_env.py` and in each stdlib-only mirror |
| `MUTATION_HEADER_OCCURRENCE_COUNT` | 53 | 59 | the new header test module |
| `MUTATION_HEADER_FILE_COUNT` | 28 | 29 | the new header test module |
| `HOST_PATH_OCCURRENCE_COUNT` `/opt/framenest` | 200 | 204 | new test module quoting the routine paths |
| `/etc/framenest` | 73 | 76 | new test module quoting the installed env-file path |
| `/var/lib/framenest` | 91 | 94 | new test module quoting the installed env-file values |
| `/var/cache/framenest` | 20 | 21 | new test module quoting the installed env-file values |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3335 | 3364 | new test module prose |
| `CAPITALIZED_FILE_COUNT` | 478 | 481 | three new test modules |

`EXPECTED_FRAMENEST_BASENAME_PATHS`, `/mnt/framenest-catalog-offdevice`, `User=framenest`, `Group=framenest` and `CONSOLE_SCRIPT_ENTRY_COUNT` are unchanged; the ledger was not weakened, only re-pinned to measured values. The `deploy` occurrence *decrease* is worth your attention at acceptance: it is a real consequence of composing prefix plus suffix in the two stdlib-only engines rather than keeping the literal names, and it is why `FRAMENEST_PRODUCTION_SSH_TARGET` no longer appears verbatim anywhere in the repository.

## Baseline and final counts

| Route | Baseline `18c357c…` | Final `90c93ea…` |
|---|---|---|
| `--operation test` | `4159 passed, 8 skipped, 3 warnings, 0 failed` in 662.87 s | `4274 passed, 8 skipped, 3 warnings, 0 failed` in 671.00 s |
| `node --test tests/*.test.js` | `554 total, 549 passed, 0 failed, 5 skipped` | `554 total, 549 passed, 0 failed, 5 skipped` |

Python delta is exactly `+115`, the new tests, with skips and warnings unchanged. JavaScript delta is exactly zero, which is the expected result: C1 changes only the header reader, and no JavaScript expectation moved.

The clean baseline was reproduced with the implementation removed from the worktree (modified files restored from `git show HEAD:<path>`, new files moved to `/tmp/opencode`) so that no edit could be observed by a running suite, then reapplied byte-for-byte. Two earlier runs were contaminated by my own mid-run edits and are discarded, not reported as evidence.

## Deviations, risks, missing evidence

1. **In-package CLI exit status is not 2.** The prompt requires exit 2 for CLI entry points. It is proven for the two CLI entry points inside this cut's authorized surface (`production_ai_deploy.py`, `framenest_release.py`). For `framenest-db`, `framenest-ai`, `framenest-youtube`, `framenest-production` and the server, the conflict is translated into each boundary's existing `FrameNestConfigurationError` / `AiConfigurationError` handling, so it fails closed with that command's existing sanitized code and existing exit status (1 or 6) and never a traceback — but not 2. Those adapters are outside the authority this prompt granted, so I did not touch them. Smallest correction: one bounded follow-up adding a dedicated conflict handler ahead of the existing `except` clauses in those five modules.
2. **Two stdlib-only mirrors of the resolver** exist in `framenest_release.py` and `production_ai_deploy.py`. They cannot import the application package by design. Duplication is real; both copies are asserted to expose the same prefix pair and the same rule, and `production_ai_deploy.py`'s copy is also asserted to resolve each prefix alone. C7 should delete all three copies together.
3. **The env-file source is dual-prefix too**, which the prompt left implicit. Without it, an explicit `load_settings(env_file=…)` of a `KRONIKA_`-named file — the shape C6 will install — would silently read nothing. This is an additive read.
4. **`env_prefix` retained**, as explained above; the only structural deviation from the literal instruction.
5. **Not verified here:** any runtime behaviour on the NUC. The routine refresh remains a separate E2 grant. The fresh independent audit before C2 is still recommended; the mutation gate is a trust boundary and this cut widened it.
6. The C5/C6 preconditions are unchanged: C1's readers accept both spellings, C1's writers still emit only the former, and the installed `/etc/framenest/framenest.env` shape is proven to keep working.

## Resolved Execution Issues / Near-Misses

- **Two contaminated long runs, self-inflicted.** I began editing while a baseline suite was running; the run spanned 18 %–80 % of my first write window, which includes `test_nuc_release_remote_contract.py` (24 %) and `test_production_ai_deployment.py` (28 %), both of which I later edited. That run reported 5 failures and 8 errors and is discarded. A second run was killed by the shell timeout taking its process group. Fixed by removing the implementation from the worktree before the clean baseline, and by launching the final run with `setsid`.
- **`env_prefix` case mismatch.** My first `_identity_suffix` compared the lower-cased internal key against the upper-cased prefix and returned `None` for every field, silently disabling all environment reads. Caught by the pre-existing settings tests immediately, found by reading `_extract_field_info` in the installed `base.py`, and fixed with `self._apply_case_sensitive(self.env_prefix)`. `test_settings_source_resolves_each_field_through_the_resolver` now pins the exact internal key mapping.
- **`env_file` is not in scope inside `settings_customise_sources`.** The env-file source is now built with `env_file=dotenv_settings.env_file`, reusing the value the library already resolved, which preserves the `ENV_FILE_SENTINEL` semantics exactly.
- **Dead local variable** `marker = store / MARKER_NAME` in `init_workstation_store` was removed once `children` became the marker test.
- **`IdentityEnvironmentConflictError` placement.** Defining it as a subclass of `FrameNestConfigurationError` would create an import cycle, so each reader translates it into its own module's sanitized error type, reusing the suffix-only message text. One dedicated type, no traceback path, no dynamic classes.

## Pre-Existing Failure Classification

none. The clean baseline at `18c357c…` is `4159 passed, 8 skipped, 3 warnings, 0 failed`, reproduced from a pristine worktree. No pre-existing failure was observed or repaired.

Smallest next step: a fresh independent audit of this commit against the mutation gate and the fail-closed resolver, before C2 is granted.

```text
Orchestration critique:
MEASURED: retention ledger `deploy` occurrence count fell 218 -> 212 and the
distinct `FRAMENEST_` name count fell 102 -> 101, because the two standard
library-only deploy engines now compose `FRAMENEST_` from a prefix constant
instead of spelling it literally; evidence: `git show --stat HEAD` plus the
measured ledger deltas reproduced from the pristine-worktree baseline run and
the final run; effect: `FRAMENEST_PRODUCTION_SSH_TARGET` is no longer greppable
verbatim anywhere, which costs operator and reviewer grep-ability for four
variable names; smallest correction: if you want the literals back, have each
engine declare its accepted names as an explicit tuple
(`("KRONIKA_NUC_SSH_TARGET", "FRAMENEST_NUC_SSH_TARGET")`) and have the mirror
resolve names rather than suffixes.
LEAD: none.
```