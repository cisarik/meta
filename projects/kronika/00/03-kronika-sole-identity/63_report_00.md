### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 63
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B2 — canonical layout only
status: PASS
Phase-qualified result: not-applicable
Start commit: f2c4624ded775e3446bfafef4a5a413253a03136
End commit: 9b291e936e93026ebe540b4a23a11b89721747a8
Report justification: new-mutation
Logical-whole closure: not-closed

Gates re-derived before mutation. Local `main` was clean at `f2c4624`, parent of this commit. `origin/main` and `git ls-remote origin refs/heads/main` were both `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. The containing `.ap` gitlink and submodule `HEAD` were both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap doctor` PASS, governing variant stable. `ap project check --baseline f2c4624ded775e3446bfafef4a5a413253a03136` PASS. The one-commit lead over public `main` is the unpublished C9-B/1 candidate. No host contact and no browser.

## 1. Retool matrix

One canonical layout replaces the pair. `CANONICAL_WEB_LAYOUT` has the former `NEW_WEB_LAYOUT` fields: `kronika.service`, user and group `kronika`, `/opt/kronika/releases`, `/opt/kronika/current`, `/etc/kronika/kronika.env`, `/var/lib/kronika`, `/var/cache/kronika`, `/run/kronika`, `/run/kronika/kronika.sock`. `WEB_LAYOUT_CANDIDATES` is that one object. `resolve_host_layout` iterates that name. The only capture pointer is `CANONICAL_CAPTURE_CURRENT` = `/opt/kronika/capture-current`.

Removed as module assignments, confirmed by an AST scan of the committed engine: `OLD_WEB_LAYOUT`, `WEB_LAYOUTS`, `OLD_CAPTURE_CURRENT`, `CAPTURE_POINTERS`, `SERVICE`, `SERVICE_USER`, `SERVICE_GROUP`, `RELEASE_ROOT`, `CURRENT`, `CAPTURE_CURRENT`, `ENV_FILE`.

Every listed builder default now binds `CANONICAL_WEB_LAYOUT`, `CANONICAL_WEB_LAYOUT.service`, `CANONICAL_WEB_LAYOUT.release_root`, or `CANONICAL_CAPTURE_CURRENT`. That covers `release_dir`, `staging_dir`, `cmd_remote_readlink_current`, `cmd_remote_df_capacity`, `cmd_remote_capture_current`, `service_account_prefix`, `cmd_remote_db_status`, `cmd_remote_backup_cli`, `cmd_remote_backup_status`, `cmd_remote_production_cli`, `cmd_remote_check_database_ready`, `cmd_remote_check_health`, `cmd_remote_run_scheduled_backup`, `cmd_remote_atomic_switch`, `cmd_remote_atomic_switch_capture`, the eight systemctl/journalctl builders, `read_current_release`, `read_optional_release_sha`, `read_backup_readiness`, `read_db_current_revision`, `verify_capacity`, `release_scoped_console_script`, `verify_unit_executables`, `_verify_cutover`, `_wait_ready`, and `_rollback`. The same AST walk finds no function default whose string contains `framenest.service`, `/opt/framenest/current`, `/opt/framenest/capture-current`, `/opt/framenest/releases`, `/etc/framenest/framenest.env`, `/var/lib/framenest`, `/var/cache/framenest`, or `/run/framenest`.

Probe shape kept: `WebLayout`, `WebLayoutReading`, `HostLayoutState`, `parse_web_layout_probe`, `select_web_layout`, `cmd_remote_layout_probe`. Selection still fail-closes on the readings it is given. The routine candidate set has one member.

Absent pointer: `resolve_capture_pointer` reads only `/opt/kronika/capture-current`. A missing pointer returns `("none", "/opt/kronika/capture-current", "/opt/kronika/releases")`. A live pointer returns `("canonical",` that same path, that same root`)`. There is no retired-path fallback.

One root: `accepted_release_roots()` returns `("/opt/kronika/releases",)`. `remote_extract` and `relocate_venv_shebangs` both call it. A path under `/opt/framenest/releases` is refused.

The module docstring now says deploy and rollback move `/opt/kronika/current` and `kronika.service`.

Keeps still in the engine, and nowhere else as a `framenest` hit: the two marker filenames, `framenest_release_sha`, `POETRY_BIN`, `CPYTHON_BIN`, and the `/etc/framenest/credentials` sanitizer needle. `FROZEN_ALEMBIC_SHA256` still has 36 keys (revisions `0001`–`0035` plus `versions/__init__.py`). The retention Part A tests passed.

Further module identified from the parse before it was edited: `tests/contract/test_nuc_release_docs.py`. Its post-switch failure fixture matched `journalctl -u framenest.service`, which is the removed service default. Only that match was changed, to `kronika.service`.

## 2. Retooled tests and the three proofs

Retooled because they parametrized `WEB_LAYOUTS` or pinned a removed constant, or because their fake host answered the removed default:

- `tests/contract/test_nuc_release_remote_contract.py`
- `tests/contract/test_kronika_capture_services.py`
- `tests/contract/test_kronika_cli_and_release_readers.py`
- `tests/contract/test_nuc_release_source_contract.py`
- `tests/contract/test_nuc_release_docs.py` (the one further module)

`RELEASE_ROOT` monkeypatches now replace `CANONICAL_WEB_LAYOUT.release_root`, which `accepted_release_roots` reads at call time. Marker-reader assertions, the Alembic shim, the local-state refusal tests, and the packaging tests were not edited. Those last two were in the 299-pass run below.

New proofs, all in the remote-contract module:

- `test_selection_consumes_exactly_the_canonical_layout` — the consumed tuple is exactly the canonical layout, the removed names are absent, and no builder default names a former-layout path.
- `test_absent_capture_pointer_stays_on_the_canonical_path` — absence is `none` on the canonical pointer; a live pointer is read there too.
- `test_accepted_release_roots_is_the_canonical_root_only` — one root, and both remote helpers call it.

## 3. Measured retention re-pin

The retention module was run before any pin edit: 3 failed, 12 passed, 0.38s. The failures were the occurrence, host-path, and unit-account scalars. File counts, content-path membership, Part A, Part B, environment tokens, the mutation header, capitalized `FrameNest`, and console scripts did not fail. After values were taken from that failure and from a per-file `git grep` of the same worktree, then written into the ledger.

| Scalar | Before | After | Cause |
|---|---:|---:|---|
| tests occurrences | 1101 | 999 | −102 |
| deploy occurrences | 25 | 9 | −16, all in `kronika_release.py` (22 → 6) |
| `/opt/framenest` | 122 | 64 | −58 |
| `/etc/framenest` | 18 | 17 | −1 |
| `User=framenest` | 2 | 0 | −2 |
| `Group=framenest` | 3 | 1 | −2 |

Tests −102 by file: remote contract −76 (90 → 14), capture services −18 (23 → 5), readers −5 (19 → 14), source contract −2 (4 → 2), docs −1 (18 → 17). No test file lost its last occurrence.

Deploy’s six remaining hits are the two marker filenames, the historical manifest key, the two tooling paths, and the sanitizer needle. The offdevice unit and the env-example mount comment are the other three of the nine.

`/opt` −58: engine −5 (7 → 2), capture services −10, readers −2, remote contract −39 (46 → 7), source contract −2. `/etc` −1: engine −1 and readers −1, offset by +1 where the single-layout test names the former env path as a forbidden default. `/var/lib/framenest` and `/var/cache/framenest` are unmoved for the same reason: the engine lost one former root each, and that test names each root once. The frozen mount is unmoved.

`User=` −2 and `Group=` −2 are the two former layout-probe fixtures. The capture unit-file absence check keeps the remaining `Group=framenest` line.

After the re-pin: 15 passed in 0.34s.

## 4. Mutation demonstrations

Both probes were restored before the full suite. After restoration, `test_selection_consumes_exactly_the_canonical_layout` passed in the same process as the capture-pointer failure.

(a) A second `WebLayout` (`key="extra"`) was added to `WEB_LAYOUT_CANDIDATES`. `test_selection_consumes_exactly_the_canonical_layout` failed at `test_nuc_release_remote_contract.py:1646`: `assert engine.WEB_LAYOUT_CANDIDATES == (layout,)`, left side one item longer, the extra layout.

(b) The absent branch was changed to return `/opt/framenest/capture-current`. `test_absent_capture_pointer_stays_on_the_canonical_path` failed at line 1713: index 1 `'/opt/framenest/capture-current' != '/opt/kronika/capture-current'`.

## 5. Suites

| Run | Result | Time |
|---|---|---|
| Touched modules plus packaging and local-state refusal | 299 passed, 0 failed | 20.21s |
| Retention before re-pin | 3 failed, 12 passed | 0.38s |
| Retention after re-pin | 15 passed | 0.34s |
| Full Python, `ap exec --operation test` | 4713 passed, 8 skipped, 3 warnings, 0 failed | 716.39s |
| JS companion_web_bridge | 23 passed | |
| JS companion_review_extension | 41 passed | |
| JS x_companion_extension | 55 passed | |
| JS companion_settings_automatic_analysis | 6 passed | |
| JS kronika_ui | 12 passed | |
| JS catalog_card_ai_quick_action | 30 passed | |
| JS `tests/*_frontend.test.js` `tests/*_cockpit.test.js` `tests/gallery_*.test.js` | 212 passed | |

The six JS files plus the glob were also run together: 379 passed, 0 failed, 10.1s. The per-file recount above matches that total.

Baseline at `f2c4624` was 4714 passed, 8 skipped, 3 warnings, 0 failed. This commit is −1 passed. The backup-cli parametrize shrank from 8 cases on two layouts to 4 cases on one (−4), and the three new proofs add +3. Skips are unchanged: five real-tool cover cases, two real-tool media-analysis cases, one NVIDIA smoke case. Warnings are the same three `PydanticJsonSchemaWarning`s. No new failure.

## 6. Commit, Part A, Part B, Part C

`git diff --stat` for `9b291e936e93026ebe540b4a23a11b89721747a8` against parent `f2c4624ded775e3446bfafef4a5a413253a03136`:

```text
 deploy/ubuntu/kronika_release.py                   | 199 +++++-------
 tests/contract/test_kronika_capture_services.py    |  46 ++-
 .../test_kronika_cli_and_release_readers.py        |  13 +-
 tests/contract/test_kronika_identity_retention.py  |  39 ++-
 tests/contract/test_nuc_release_docs.py            |   2 +-
 tests/contract/test_nuc_release_remote_contract.py | 333 +++++++++++++++------
 tests/contract/test_nuc_release_source_contract.py |  50 +++-
 7 files changed, 419 insertions(+), 263 deletions(-)
```

Working tree clean. Not pushed. Local `main` is now two commits ahead of public `5b86d896`.

Part A byte-unmoved: none of those paths are in the diff, and the frozen-document and frozen-Alembic retention tests passed, including the 36-key set. Part B still empty: the basename ledger test passed and no basename was added. Part C movement is the table in section 3.

## 7. Sites no test executes

- `cmd_remote_service_fragment_path` has no caller. Its default is covered only by the default-argument parse, not by a call.
- `select_web_layout` still refuses two active or two enabled readings, and an unrecognised installed unit. No test builds two readings. The routine probe never produces them. The new test fails if a second candidate is added to the set that `resolve_host_layout` consumes.
- Status and check print `layout: canonical`. No assertion reads that line. The layout object’s `key` is asserted.
- The corrected module docstring is not asserted. `test_engine_documents_never_uv_or_migrate` still checks that the engine does not invoke `uv` or `framenest-db migrate`.
- `state_root`, `cache_root`, `runtime_root`, and `socket_path` are equality-pinned and have no reader in the engine.

## 8. Deviations, risks, missing evidence

No scope deviation. The candidate tuple is `WEB_LAYOUT_CANDIDATES` because `WEB_LAYOUTS` was a required removal. A present capture pointer is keyed `canonical`. The `/var/lib` and `/var/cache` host-path scalars did not drop, because the new proof names those former roots; the engine itself no longer contains them.

Missing evidence: none of the required suites. This result is non-independent. No publication, refresh, or host contact was done.

Smallest next step: accept this commit, then issue C9-B/3 (living truth) against `9b291e936e93026ebe540b4a23a11b89721747a8`.

```text
Orchestration critique:
MEASURED: none
LEAD: cmd_remote_service_fragment_path has no caller; a repo-wide name search finds only its definition. A later cut can delete it. This grant only retargeted the default.
```

Resolved Execution Issues / Near-Misses: one `python3 -c 'print("skip")'` was invoked while collecting git evidence. It printed `skip` and was not used as product evidence or as a mutation. The contract route for Python evidence remained `./.ap/ap exec`. No residual product effect.

Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the grant; no autonomous continuation.