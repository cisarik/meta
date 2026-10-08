All gates pass and the tree is clean. Terminating with the required report.

### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 23 · **Exchange:** 01
**Task identity:** KSI-IMPL-C4B
**Report justification:** `new-mutation`
**Commit:** `ed5bcb481749f5a732170fd967efc5a2f940cae2` on local `main`, parent `b16ea2c719f46e167c579c34ddd87a915b70cb00`. One commit, no amend, not pushed. Public `main` is still `6e89328640fe5477e08f17f4c31c9fc4bf261238`; local `main` is 2 ahead. Tree clean, submodule unmoved at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
**Client disclosure:** none; this client emitted no prose above the header.
**Evidence tier:** E2. Repository implementation with simulated-host tests only. No host was contacted.

---

## 1. Derivation

All four derivations were done by parsing the live tree, never from the issued sample. Measurement probes: the retention module's own helpers, a Part C measurement probe, and an AST probe for untested sites, each run through `./.ap/ap exec --operation test-focus`.

### 1.1 Derivation A — canonical artifact mapping

Rule applied to each live Part B basename: replace `framenest_`/`framenest` with the canonical component; the canonical file must exist. The 20 Part B paths split exactly three ways.

**Created by this cut (11 web-side artifacts):**

| Retired path | Canonical counterpart | Action |
|---|---|---|
| `deploy/systemd/framenest.service` | `deploy/systemd/kronika.service` | created |
| `deploy/systemd/framenest-catalog-backup.service` | `deploy/systemd/kronika-catalog-backup.service` | created |
| `deploy/systemd/framenest-catalog-backup.timer` | `deploy/systemd/kronika-catalog-backup.timer` | created |
| `deploy/systemd/framenest-catalog-offdevice.service` | `deploy/systemd/kronika-catalog-offdevice.service` | created |
| `deploy/systemd/framenest-catalog-offdevice.timer` | `deploy/systemd/kronika-catalog-offdevice.timer` | created |
| `deploy/systemd/framenest.env.example` | `deploy/systemd/kronika.env.example` | created |
| `deploy/systemd/framenest-ai-credential-nvidia-nim.conf` | `deploy/systemd/kronika-ai-credential-nvidia-nim.conf` | created |
| `deploy/systemd/framenest-ai-credential-opencode-go.conf` | `deploy/systemd/kronika-ai-credential-opencode-go.conf` | created |
| `deploy/systemd/framenest-ai-credential-vercel-ai-gateway.conf` | `deploy/systemd/kronika-ai-credential-vercel-ai-gateway.conf` | created |
| `deploy/systemd/framenest-research-credential.conf` | `deploy/systemd/kronika-research-credential.conf` | created |
| `deploy/ubuntu/framenest-catalog-export-v1` | `deploy/ubuntu/kronika-catalog-export-v1` | created (mode 100755) |

**Already existing from earlier cuts (4):** `framenest-release` → `kronika-release`; `framenest_release.py` → `kronika_release.py`; root `framenest` → `kronika`; `scripts/operator/network/framenest_nuc_worker_gate.fish` → `kronika_nuc_worker_gate.fish`.

**Ambiguous under the rule, deliberately not created (5):** `scripts/operator/infosec/framenest_{log_triage,public_surface_check,socket_permissions_check}.sh`, `scripts/operator/network/framenest_mullvad_egress.{fish,sh}`. These are workstation operator diagnostics, not web host layout artifacts; the prompt's §3 scope and the issued artifact sample cover only the `deploy/` web-side set. Creating silent duplicates would be provisioning-by-copy. Their canonical identity belongs to the cut that owns the workstation operator surface (C6/C7-B window). This is the only rule ambiguity, and it is reported rather than resolved by guessing.

### 1.2 Derivation B — environment keys, path versus opaque

Derived from the settings model (`KronikaSettings` fields with `Path` annotations), the env template, and the code that consumes keys outside the model (catalog backup roots in the backup CLI, `AI_CONFIG_PATH` in AI configuration storage, `ENV_FILE` in `load_settings`).

**Path-classified (14 suffixes):** `DATABASE_PATH`, `GALLERY_PREVIEW_CACHE_PATH`, `COVER_STORAGE_ROOT`, `COVER_THUMBNAIL_CACHE_PATH`, `AI_CONFIG_PATH`, `CATALOG_BACKUP_ROOT`, `CATALOG_RESTORE_VERIFY_ROOT`, `CATALOG_BACKUP_OPS_ROOT`, `YOUTUBE_ACQUISITION_ROOT`, `X_ACQUISITION_ROOT`, `UPLOAD_QUARANTINE_ROOT`, `RUNTIME_SETTINGS_PATH`, `UDS_PATH`, `ENV_FILE`. Reason: each holds a filesystem location; prefix-only rename would leave the object on the former path.

**Opaque (31 suffixes):** `HOST`, `PORT`, `API_KEY`, `UPLOAD_PUBLICATION_LIBRARY_ID`, `UPLOAD_MAX_*` (3), `UPLOAD_MIN_FREE_SPACE_RESERVE_BYTES`, `YOUTUBE_ACQUISITION_MAX_STAGING_BYTES`, `YOUTUBE_REQUEST_MAX_*` (6), `X_ACQUISITION_MAX_STAGING_BYTES`, `X_REQUEST_MAX_*` (4), `AI_PROVIDER_ID`, `AI_MODEL_ID`, `INGRESS_MODE`, `EXTERNAL_ORIGIN`, `COMPANION_EXTENSION_ORIGINS`, `IDENTITY_MAP`, `LOCAL_OWNER_LOGIN`, `AUTOMATIC_MEDIA_ANALYSIS_ENABLED`, `AUTOMATIC_MEDIA_ANALYSIS_MAX_ATTEMPTS`, `CATALOG_BACKUP_KEEP_AUTO`, `CATALOG_OFFDEVICE_DESTINATION_ID`. Reason: counts, flags, identifiers, an origin, a JSON map/list, or a 32-hex pin; rewriting any of them would corrupt semantics. An unknown identity suffix fails the transformation (`EXIT_MIGRATION`) rather than being renamed untyped. A key under neither prefix is foreign and preserved verbatim. The classification test asserts every current `KronikaSettings` field suffix is in the union, so a future setting fails the guard until classified.

### 1.3 Derivation C — old-layout assumptions and their owner

| Site | Classification |
|---|---|
| `status`, `check`, `deploy`, `rollback`, `activate-capture`, `rollback-capture` web targets | in-scope-this-cut: now selected from validated effective service configuration |
| installed-unit guard, release-scoped console-script mapping, capacity probe, service-account prefix, production CLI, `current` readlink, atomic switch, capture-pointer read/switch | in-scope-this-cut: layout- and pointer-parameterised |
| transferred `_remote` extract/relocate path validation | in-scope-this-cut: now accepts both accepted release roots (this was a C6 blocker; see §1.5) |
| `SERVICE`, `SERVICE_USER`, `SERVICE_GROUP`, `RELEASE_ROOT`, `CURRENT`, `CAPTURE_CURRENT`, `ENV_FILE`, `REMOTE_DEPLOY_DIR`, both tooling paths | **C6 owns the values.** Unchanged by this cut and bound as `OLD_WEB_LAYOUT` data |
| `FRAMENEST_ENV_FILE` variable name passed to service-account commands; `REMOTE_DEPLOY_DIR/framenest_release.py` transferred artifact name | **C7-B window.** The artifact name is published by the runbook and pinned by a test |
| capture pointer location (`/opt/framenest/capture-current` → new) | **C8-A** |
| tooling paths, `/mnt/framenest-catalog-offdevice`, capture state directory | **named frozen residues.** Never renamed |

### 1.4 Derivation D — new sites no test exercises

Directly tested production-host methods: `copy_state`, `transform_environment`, `prepare_release_environment`, `rename_account`, `install_units`, `replace_tailscale_handler`, `recover_pre_write`, `recover_post_write`, plus `read_migration_observation`, `build_migration_plan`, the layout probes, the typed transformation, and the tailscale parser.

**No direct test (stated, not hidden):** production `read_journal`, `write_journal`/`write_recovery_manifest`/`_write_root_file`, `acquire_lock`/`release_lock`, `quiesce`/`stop_writers`/`assert_no_legacy_writers`, `capture_snapshot`/`verify_capture_untouched`, `create_checkpoint`, `preserve_ancillary`, `verify_effective_units`, `start_service`, `verify_local_readiness`, `record_tailscale_state`, `verify_ingress`, `resume_writers`. Their sequencing, recovery branch and invariants are proven through the host-agnostic orchestration with the simulated host; their exact remote command sequences are not exercised. **Three builders are dead code:** `cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state`, `migration_unit_required` (no caller, no test).

### 1.5 A C6 blocker found and fixed by derivation

The transferred `_remote _remote-extract` and `_remote-relocate-venv-shebangs` helpers validated every path against the single former release root. After C6, routine deploy prepares `/opt/kronika/releases/<sha>`; the helpers would have refused it on the host with no layout to select from. Fixed: `accepted_release_roots()` returns the active `RELEASE_ROOT` plus the canonical target root, read at call time, so C6's constant change needs no second edit.

## 2. Reconciliation against the artifact sample

**No differences from the sample.** The sample's 11 paths are exactly the 11 created. The reconciliation extends it: `framenest-release`, `framenest_release.py`, root `framenest` and `framenest_nuc_worker_gate.fish` already have canonical counterparts, and the five operator-script paths are named in §1.1 as the ambiguity. Diff of derivation vs sample: **0 artifacts missing, 0 extra creations**.

## 3. Three transition states, signals, and fail-closed proof

Signals, all from `systemctl show` on both candidate units: `LoadState` (installed), `ActiveState` (serving), `UnitFileState` (enabled), `User`, `Group`, `WorkingDirectory`, and the `path=` field of each effective `ExecStart`. A candidate whose effective identity does not name its own user, group, working directory and a `.venv/bin` console script is **unrecognised**. Capture pointer axis: existence/absence of each accepted pointer.

| State | Selected signals |
|---|---|
| 1. old web, old capture pointer | old unit active (or enabled), new not-found; old pointer present |
| 2. new web, old capture pointer | new unit active/valid, old pointer still present → web resolves new, capture root stays former |
| 3. new web, new capture pointer | new unit active, new pointer present |

Fail-closed demonstrations (`test_select_web_layout_fails_closed_on_ambiguity_and_absence`, `test_resolve_host_layout_selects_each_state_and_fails_closed`): both candidates active → `EXIT_LAYOUT`; both not-found → `EXIT_LAYOUT`; both enabled-inactive → `EXIT_LAYOUT`; a loaded candidate with foreign effective identity → `EXIT_LAYOUT`; both capture pointers present → `EXIT_LAYOUT`. A wrong signal cannot silently select: identity is validated from effective configuration, never from a service name or a preference.

## 4. Typed transformation

Synthetic environment, before → after (all values verified in `test_typed_transformation_moves_every_path_class`):

```text
FRAMENEST_DATABASE_PATH=/var/lib/framenest/catalog.sqlite3        -> KRONIKA_DATABASE_PATH=/var/lib/kronika/catalog.sqlite3
FRAMENEST_GALLERY_PREVIEW_CACHE_PATH=/var/cache/framenest/...     -> KRONIKA_GALLERY_PREVIEW_CACHE_PATH=/var/cache/kronika/...
FRAMENEST_COVER_STORAGE_ROOT=/var/lib/framenest/covers            -> KRONIKA_COVER_STORAGE_ROOT=/var/lib/kronika/covers
FRAMENEST_COVER_THUMBNAIL_CACHE_PATH=/var/cache/framenest/...     -> KRONIKA_COVER_THUMBNAIL_CACHE_PATH=/var/cache/kronika/...
FRAMENEST_AI_CONFIG_PATH=/var/lib/framenest/ai/config.json        -> KRONIKA_AI_CONFIG_PATH=/var/lib/kronika/ai/config.json
FRAMENEST_CATALOG_BACKUP_ROOT=/var/lib/framenest/catalog-backups  -> KRONIKA_CATALOG_BACKUP_ROOT=/var/lib/kronika/catalog-backups
FRAMENEST_CATALOG_RESTORE_VERIFY_ROOT=...                         -> KRONIKA_CATALOG_RESTORE_VERIFY_ROOT=/var/lib/kronika/...
FRAMENEST_CATALOG_BACKUP_OPS_ROOT=...                             -> KRONIKA_CATALOG_BACKUP_OPS_ROOT=/var/lib/kronika/...
FRAMENEST_YOUTUBE_ACQUISITION_ROOT=...                            -> KRONIKA_YOUTUBE_ACQUISITION_ROOT=/var/lib/kronika/...
FRAMENEST_UDS_PATH=/run/framenest/framenest.sock                  -> KRONIKA_UDS_PATH=/run/kronika/kronika.sock
```

- **`/mnt/framenest-catalog-offdevice` unchanged** — checked before any root mapping; `test_typed_transformation_preserves_custom_and_frozen_paths` and `test_canonical_offdevice_artifacts_keep_the_frozen_mount`.
- `/opt/framenest/tooling/...` unchanged (frozen); a custom root `/srv/media/framenest-quarantine` unchanged; already-canonical values unchanged; opaque values containing the token unchanged (`FRAMENEST_EXTERNAL_ORIGIN=https://framenest.example`, a destination id).
- **Idempotence:** `transform_environment_text(once.text).text == once.text` and `environment_transformation_is_idempotent(once)`.
- A value under a moved root that still carries the token after component renaming is **refused** (`EXIT_MIGRATION`), not left on an unmigrated path. Comments are preserved byte-for-byte.

## 5. Migration machinery, capability by capability

| Capability | Implementation | Simulated test |
|---|---|---|
| Phase journal | root-controlled `/var/lib/kronika/identity-migration/journal.json` (0755 parents, 0700 dir, umask 077) written before the first mutation and after every phase | `test_journal_is_written_before_the_first_mutation_and_after_every_phase` |
| Recovery manifest | exact-object manifest: plan digest, layouts, account uid/gid/home, copy moves, drop-ins, credential sources, export/sudo instances, capture pointer | same test |
| Exclusive lock | `/run/kronika-identity-migration` + sibling owner record; reuses C4-A `classify_deploy_lock_owner` reclaim semantics | simulated host lock assertions across 42 runs |
| Copy-and-verify | `cp -a` under a moved root, source and destination full manifests compared before continuing; existing destination refuses | `test_production_copy_state_*` (2) |
| New-path environment | copy retained release to `<new>.staging`, drop copied `.venv`, frozen Poetry + committed lock, relocate shebangs/search paths, chown/chmod, markers, atomic rename, final verify | `test_production_prepare_release_environment_builds_at_the_new_path`, `test_relocated_environment_resolves_and_leaves_the_old_release_alone` |
| Account rename | preflight refuses an existing `kronika`/second account; `groupmod` then `usermod`, assert uid/gid and old-name absence; never `useradd`/`groupadd` | `test_production_rename_account_keeps_uid_and_gid` |
| Effective units/drop-ins | canonical repo units written by hash; only discovered drop-ins migrated with typed path tokens; `daemon-reload`; effective probe of `kronika.service` | `test_production_install_units_installs_only_discovered_artifacts` |
| Tailscale handler | status JSON recorded first; exactly one old-socket handler located; targeted `tailscale serve --bg` replacement; `reset` never emitted; non-default mount fails closed | `test_production_replacement_records_first_replaces_one_and_never_resets`, `test_tailscale_replacement_command_never_resets`, refusal test |
| Preflight ancillary | discovers installed drop-in names, credential source filenames, export executable and sudo-rule candidates; migrates only existing instances; filenames/existence only | `test_preflight_is_read_only_and_reports_existence_only`, `test_preflight_never_reads_a_credential_value` |

## 6. Failure injection after every phase

Machine-run matrix: **14 phases × 3 capture-pointer states = 42 injected failures**, all passing (`test_failure_injection_after_every_phase`). Failure of phase *k* leaves `completed_phases == MIGRATION_PHASES[:k]` in the journal and selects:

| # | Phase whose start failed | Last completed | Recovery branch |
|---|---|---|---|
| 0 | quiesce | — | pre-write |
| 1 | verify-capture | quiesce | pre-write |
| 2 | checkpoint | …verify-capture | pre-write |
| 3 | copy-state | …checkpoint | pre-write |
| 4 | transform-environment | …copy-state | pre-write |
| 5 | preserve-ancillary | …transform-environment | pre-write |
| 6 | prepare-release-environment | …preserve-ancillary | pre-write |
| 7 | rename-account | …prepare-release | pre-write |
| 8 | install-units | …rename-account | pre-write |
| 9 | verify-effective-units | …install-units | pre-write |
| 10 | start-service | …verify-effective-units | pre-write (start not completed) |
| 11 | replace-tailscale-handler | …**start-service** | **post-write** |
| 12 | verify-ingress | …replace-handler | **post-write** |
| 13 | resume-writers | …verify-ingress | **post-write** |

Every injected run asserted: correct branch; journal identifies the last completed phase; UID and GID 1001 preserved; exactly one account and `useradd_calls == 0`; **`capture_restarts == 0`**; lock released on every path.

## 7. Pre-write versus post-write recovery

The cutover boundary is the completed `start-service` phase: from then on the new application may admit writes. Pre-write (`recover_pre_write`): stop/disable the new unit, reverse the account rename only when it completed, start the former service, re-enable/start the former timers; no state is copied back because none changed. Post-write (`recover_post_write`): guard only — it never copies state back, never renames the account back, never touches capture, and records that forward recovery is required. Tests: `test_pre_write_recovery_restores_the_former_layout`, `test_post_write_recovery_never_restores_stale_copied_state`, `test_production_pre_write_recovery_restores_the_old_layout_and_writers`, `test_production_post_write_recovery_never_restores_stale_state`.

## 8. New-path environment and retained-release protection

`test_relocated_environment_resolves_and_leaves_the_old_release_alone`: a synthetic `.venv` built at `<new>.staging` gets shebangs rewritten to `<new>/.venv/bin/python`; `.pth` and `direct_url.json` search paths resolve to the final path; a separate retained release tree is byte-identical before and after (sha256 compared). The production sequence rebuilds the environment at the **final** path from the copied staging tree and verifies it after the atomic rename.

## 9. `migrate-identity` invocation-freedom

`test_routine_commands_never_reach_identity_migration` monkeypatches `_cmd_migrate_identity`, `read_migration_observation`, `run_migration_apply` and `RemoteMigrationHost` to explode, then runs `deploy`, `rollback`, `activate-capture` and `rollback-capture` through the real CLI with the existing fakes: all return `EXIT_OK`, and no transcript contains `migrate`. `test_engine_and_routine_builders_never_emit_migrate_identity` pins the routine builders. **`apply` was never executed in any mode**: refusal tests call `_cmd_migrate_apply` directly with fakes (`--yes` missing → `EXIT_USAGE` with zero runner calls; digest mismatch → `EXIT_MIGRATION`, no mutating command), and no test drives apply through `main`.

## 10. Diff, commit, Part A and Part B

`git show --stat HEAD` (tree clean, `git diff` empty):

```text
 deploy/systemd/kronika-ai-credential-nvidia-nim.conf      |   2 +
 deploy/systemd/kronika-ai-credential-opencode-go.conf     |   2 +
 deploy/systemd/kronika-ai-credential-vercel-ai-gateway.conf | 2 +
 deploy/systemd/kronika-catalog-backup.service             |  37 +
 deploy/systemd/kronika-catalog-backup.timer               |  14 +
 deploy/systemd/kronika-catalog-offdevice.service          |  49 +
 deploy/systemd/kronika-catalog-offdevice.timer            |  14 +
 deploy/systemd/kronika-research-credential.conf           |   9 +
 deploy/systemd/kronika.env.example                        |  62 +
 deploy/systemd/kronika.service                            |  40 +
 deploy/ubuntu/kronika-catalog-export-v1                   |  60 +
 deploy/ubuntu/kronika_release.py                          | 2753 +++++++++++--
 tests/contract/test_kronika_capture_services.py           |  26 +
 tests/contract/test_kronika_identity_migration.py         | 1473 +++++++++++
 tests/contract/test_kronika_identity_retention.py         |  85 +-
 tests/contract/test_nuc_release_remote_contract.py        |  37 +
 16 files changed, 4478 insertions(+), 187 deletions(-)
```

**Part A byte-unmoved; Part B exactly 20; no former-spelling artifact left the tree.** Retention module **15 passed** post-commit. `git diff --diff-filter=D b16ea2c..HEAD` is empty. No Part B path was removed or renamed; every creation was additive.

## 11. Full counts and per-file attribution

**Python, declared `test`:** `4587 passed, 8 skipped, 3 warnings in 734.55s`. Baseline reproduced pre-edit: `4493 passed, 8 skipped, 3 warnings`. **+94 net**, all 94 collected tests in the new `tests/contract/test_kronika_identity_migration.py` (51 `def test_`, parametrisation expands to 94). No test removed; the two existing test files gained fake-host probe answers only.
**JavaScript, `node --test tests/*.test.js`:** `583 tests, 578 pass, 0 fail, 5 skipped` — unchanged; no JavaScript was touched.
**Retention module:** 15 passed.

## 12. Ledger movements and `FROZEN_ALEMBIC_SHA256`

All values regenerated at report time from the committed tree.

| Pin | Before | After | Cause |
|---|---:|---:|---|
| `src` files / occurrences | 186 / 1695 | 186 / 1695 | unmoved |
| `tests` files / occurrences | 184 / 1871 | **185 / 2006** | +1 file: the new migration test; +135 occurrences = new file 120 + remote-contract 8 + capture 7 |
| `deploy` files / occurrences | 20 / 201 | **22 / 246** | +2 files (`kronika-catalog-offdevice.service` 2, `kronika.env.example` 1 = frozen mount only); +42 in the engine migration section |
| `scripts` files / occurrences | 7 / 86 | 7 / 86 | unmoved |
| `docs` / `extension` | 88 / 1216, 8 / 145 | unchanged | unmoved |
| Content-path membership | 508 | **511** | +3: offdevice service, canonical env template, new test file; 0 removed |
| `ENV_PREFIX_TOKEN / DISTINCT / BARE` | 628 / 101 / 26 | **655 / 103 / 29** | all +27/+2/+3 from the new test file's sample environment and prefix checks |
| `MUTATION_HEADER` | 73 / 30 | 73 / 30 | unmoved |
| `/opt`, `/etc`, `/var/lib`, `/var/cache`, `/mnt/framenest-…` | 210 / 76 / 94 / 21 / 13 | **223 / 83 / 109 / 29 / 23** | additive: engine migration constants/builders, two fake probe answers, new test fixtures |
| `User=framenest`, `Group=framenest` | 5 / 5 | **8 / 8** | two probe answers + one negative assertion |
| Capitalized `FrameNest` occurrences / files | 2748 / 394 | 2748 / 394 | unmoved; no `FrameNest*` class or message touched |
| Console-script retired entries | 14 | 14 | `pyproject.toml` untouched |

**`FROZEN_ALEMBIC_SHA256` key count: 36** = 35 numbered revisions `0001`–`0035` plus `__init__.py`; bytes and set equality both pass.

## 13. Deviations, risks, missing evidence, smallest next step

**Deviations.**
1. `apply` confirmation is `--yes` **plus** `--preflight-digest <sha256>` (argparse-required) binding apply to the exact validated plan; the C6 grant names its confirmation flag, and `--yes` follows the existing deploy convention.
2. Five operator-script paths deliberately have no canonical counterpart here (§1.1); creating them would exceed web-side scope.
3. The narrow sudo rule content is not in the repository, so the migration copies the installed rule to the canonical candidate path with typed path tokens and validates it with `visudo -cf`; the export launcher is installed from the canonical repository artifact.
4. Three builders are dead code (`cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state`, `migration_unit_required`); removal was not possible inside a single non-amended commit.
5. The engine module docstring (line 16) still describes the former single-layout deploy; it was left exact to avoid a second commit.

**Risks.**
1. Every production remote command sequence is unexecuted. The transferred `_remote` both-roots validation change (§1.5) is proven by parse/string tests only.
2. The `systemctl show` parse now feeds both the C4-A guard and the layout selector; neither has seen live output. The outstanding C4-A read-only probe precondition is now more important, not less.
3. Tailscale JSON shape and replacement syntax are documented-shape only; non-default mounts fail closed.
4. Copy verification hashes whole state/cache trees; on the real host this trades time for correctness.
5. `ps -u framenest` in the writer assertion runs unprivileged; it is read-only and best-effort, and it fails the abort only on a nonzero count.

**Missing evidence.** No host contact, no live systemd/Tailscale/account output, no apply execution, no copy-performance measurement, and the engine has not been executed under Ubuntu system Python 3.12. Rule 10 applies: I cannot demonstrate the migration against a real host, and nothing here proves the machinery on a live system.

**Smallest next step.** Keep the two outstanding C4-A host-side preconditions (stale lock removal; one read-only `systemctl show --property=ExecStart --property=ExecStartPre framenest.service`) as the first items of the C6 preparation window, and add the layout probe properties to that same read so the selector parse is confirmed against observed output before anything depends on it.

## Resolved Execution Issues / Near-Misses

- **A C6 blocker caught during derivation, not after commit.** The transferred `_remote` helpers validated only the former release root; the first draft would have refused canonical release paths on the host. Found by classifying every remaining old-layout literal, fixed with `accepted_release_roots()` and covered by the existing parse tests.
- **Retention re-pin done three times, each time from a fresh measurement.** The pins moved after the staged artifacts became tracked, then again after the production-host tests were added; a transcribed figure was never used.
- **Fake-runner ordering hazard.** The layout probe initially collided with the existing `systemctl show --property=ExecStart` fake branch; the probe orders `LoadState` first and the fakes dispatch on it, so the guard branch and the layout branch cannot cross.
- **A wrong test expectation, corrected.** The first canonical-artifact regression test asserted that routine deploy never names `kronika.service` at all; the layout probe legitimately names the candidate unit. The test now pins the mutating forms (`cat > /etc/systemd/system/kronika…`, `groupmod`, `usermod`, `tailscale serve --bg`).
- **A fake returned `present` for the env read.** The preflight read-only fake matched a generic existence branch before the env-file branch; reordered, no production code changed.

## Pre-Existing Failure Classification

**none.** Both baselines were reproduced exactly before any edit (Python `4493 passed, 8 skipped, 3 warnings`; JavaScript `583 / 578 / 0 / 5`), and every failure encountered during implementation was caused by this cut's own edits and resolved before the full run. No test failed for a reason outside this change.

```text
Orchestration critique:
MEASURED: The issued §3 sample (11 deploy/ web-side artifacts) and completion-plan §1.6 ("and affected operator scripts") disagree about scope, because the live Part B set also holds five `scripts/operator/` paths whose canonical counterparts this cut deliberately does not create. A future acceptance check that mechanically applies the replacement rule to all 20 Part B paths would fail this cut for doing exactly what its own sample lists. Evidence: §1.1; `EXPECTED_FRAMENEST_BASENAME_PATHS` contains 20 paths, 11 in the sample, 5 operator scripts uncreated, 4 pre-existing. Effect: acceptance ambiguity, not a product defect. Smallest correction: state in the next grant whether operator-script canonical counterparts belong to C6/C7-B or to a dedicated operator-surface cut.
MEASURED: This cut added three dead builders (`cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state`, `migration_unit_required`) that no caller or test references. Evidence: AST probe over the committed engine (131 new sites, these three with zero test references and no production caller). Effect: harmless residue in the engine. Smallest correction: delete them in the next cut that touches `kronika_release.py`.
LEAD: The new layout selector consumes `systemctl show` output shapes (`UnitFileState`, `LoadState`, multi-line `ExecStart`) that have never been observed on the NUC; a value such as `enabled-runtime` or a systemd output dialect could make a valid layout look unrecognised, and the selector fails closed, so the effect would be a refused routine operation rather than a wrong tree. Cheapest useful check: one read-only Cooperator `systemctl show --property=LoadState --property=ActiveState --property=UnitFileState --property=User --property=Group --property=WorkingDirectory --property=ExecStart framenest.service` on the NUC before C5/C6.
```