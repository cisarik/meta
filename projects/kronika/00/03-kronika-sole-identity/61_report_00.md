C9-B removal and finalization plan

Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 61
Worker exchange ordinal: 01
Persistent role identity: WORKER
Task identity: KSI-PLAN-C9B
status: PASS
Report justification: new-evidence
Logical-whole closure: not-closed
Start commit: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (clean main, public origin/main equal, .ap 73e20ef80b88700d5fcbc397cd8edd4fc425869f)
ap doctor and ap project check --baseline 5b86d896b3ea03f89fef2c90f7af2c121d0ef915: PASS
Normative source: section 2.19 of the session-25 report. FROZEN_ALEMBIC_SHA256 counted from the dict: revisions 0001-0035 plus versions/__init__.py = 36 keys. Frozen document pins: ADR 0001-0084 (84) plus docs/FEDORA_SERVICE.md and docs/NUC_HOST_BASELINE.md = 86.

No write, commit, host contact, or implementation is authorized by this plan.

1. Former-layout web support

Routine commands have no --layout flag. status, check, deploy, rollback, activate-capture, and rollback-capture all call resolve_host_layout (deploy/ubuntu/kronika_release.py 2077), which probes every member of WEB_LAYOUTS and lets select_web_layout (2003) pick one installed unit. OLD_WEB_LAYOUT (210) is still a legal selection: framenest.service, user/group framenest, /opt/framenest/releases, /opt/framenest/current, /etc/framenest/framenest.env, /var/lib/framenest, /var/cache/framenest, /run/framenest, /run/framenest/framenest.sock. C9-A retired those host objects, so a routine route that can still select them is obsolete.

resolve_capture_pointer (2046) still treats a missing pointer as ("none", OLD_CAPTURE_CURRENT, OLD_WEB_LAYOUT.release_root), which is /opt/framenest/capture-current under /opt/framenest/releases. accepted_release_roots (1354) still returns both release roots, so the on-host _remote-extract and _remote-relocate-venv-shebangs helpers still accept a write under the retired root.

Classification for the implementation:

Retool, do not delete the operation. One canonical WebLayout replaces the pair. Its fields are today's NEW_WEB_LAYOUT (226): kronika.service, user/group kronika, /opt/kronika/releases, /opt/kronika/current, /etc/kronika/kronika.env, /var/lib/kronika, /var/cache/kronika, /run/kronika, /run/kronika/kronika.sock. The only capture pointer is /opt/kronika/capture-current, and its release root is /opt/kronika/releases. An absent pointer stays absent; it does not fall back to the retired path. accepted_release_roots returns only /opt/kronika/releases.

Remove as selectors. OLD_WEB_LAYOUT, WEB_LAYOUTS, OLD_CAPTURE_CURRENT, CAPTURE_POINTERS, and the module constants that are aliases of the retired layout: SERVICE, SERVICE_USER, SERVICE_GROUP, RELEASE_ROOT, CURRENT, CAPTURE_CURRENT, ENV_FILE (lines 70-84). Builder defaults that currently equal OLD_WEB_LAYOUT, SERVICE, RELEASE_ROOT, or CAPTURE_CURRENT are retargeted at the canonical layout in the same change: release_dir, staging_dir, cmd_remote_readlink_current, cmd_remote_df_capacity, cmd_remote_capture_current, service_account_prefix, cmd_remote_db_status, cmd_remote_backup_cli, cmd_remote_backup_status, cmd_remote_production_cli, cmd_remote_check_database_ready, cmd_remote_check_health, cmd_remote_run_scheduled_backup, cmd_remote_atomic_switch, cmd_remote_atomic_switch_capture, the systemctl/journalctl builders at 758-794, read_current_release, read_optional_release_sha, read_backup_readiness, read_db_current_revision, verify_capacity, release_scoped_console_script, verify_unit_executables, _verify_cutover, _wait_ready, _rollback.

Keep the probe shape, shrink the candidate set. parse_web_layout_probe, select_web_layout, WebLayout, WebLayoutReading, HostLayoutState, and cmd_remote_layout_probe stay, but they validate only the canonical unit. A second candidate cannot be added without failing the new test below.

Do not touch while retooling. Marker tables and read_release_markers (section 4). POETRY_BIN and CPYTHON_BIN stay under /opt/framenest/tooling/.... _assert_logs_sanitized (6513) keeps the token /etc/framenest/credentials as a log redaction needle, not as a path the engine writes.

Risk: a default argument left on the retired constant would make a caller that omits layout operate the deleted tree. The proof is that no routine builder default still names framenest.service, /opt/framenest/current, or /opt/framenest/capture-current. Tests that still parametrize WEB_LAYOUTS or pin the old constant (test_nuc_release_remote_contract.py, test_kronika_capture_services.py, test_kronika_cli_and_release_readers.py, test_nuc_release_source_contract.py) are retooled in the same commit. The module docstring at lines 11-12, which still says deploy moves /opt/framenest/current and framenest.service, is corrected with the code.

2. Temporary migration and recovery

These exist only to perform the one-time host move C9-A already finished. They are remove, including their tests, after a caller check that no routine command calls them.

Identity migration constants, lines 268-434: MIGRATION_DIRECTORY, journal and recovery-manifest paths, MIGRATION_PHASES (15 phases), MIGRATION_UNIT_ARTIFACTS, MIGRATION_OLD_TO_NEW_ROOTS, MIGRATION_SEGMENT_RENAMES, MIGRATION_FROZEN_PATH_PREFIXES, IDENTITY_ENVIRONMENT_PATH_SUFFIXES, IDENTITY_ENVIRONMENT_OPAQUE_SUFFIXES. Callers are the transformer and tests/contract/test_kronika_identity_migration.py only.

Typed transformer, lines 2109-2318: EnvironmentAssignment, EnvironmentTransformation, classify_environment_key, transform_path_value, transform_environment_text. The engine COMPATIBLE_ENVIRONMENT_PREFIX ("FRAMENEST_", line 44) is used here and by the migration grep at 2582. It goes with this block. It is not the application resolver in src/kronika/identity_env.py.

Migration-only remote commands, classes, and orchestration, lines 2489-5147: ObservedUnit, MigrationObservation, MigrationPlan, RemoteMigrationHost, parse_tailscale_serve_status, classify_unit_path_token, transform_unit_dropin_text, transform_sudoers_text, run_migration_apply, read_migration_observation (refuses unless state.web.key == "old"). Private-store handling in that observation (/etc/framenest/credentials at 4948 and 5025) is part of this removal. The sanitizer needle in section 1 is a different site and stays.

Capture-path migration, lines 5148-5817 and the CLI handlers 5770-5816 and 5983-6066: CapturePathUnit, CapturePathPlan, _require_former_capture_pointer, observe_capture_path_plan, CAPTURE_PATH_SCRATCH, CAPTURE_PATH_REMOTE_ENGINE.

CLI surface: migrate-identity {preflight,apply} and migrate-capture-paths {preflight,apply} in _build_parser (5865-5912).

Not transitional. _remote-extract and _remote-relocate-venv-shebangs (6068) are how routine deploy runs the transferred engine. They stay. DeployLockDecision and classify_deploy_lock_owner (2319-2488) are the routine lock. They stay.

Tests: delete tests/contract/test_kronika_identity_migration.py only after confirming every keep in section 4 still has its pin in another file. Marker pins already live in test_kronika_cli_and_release_readers.py. Update test_nuc_release_docs.py and deploy/ubuntu/README.md in the same commit so no living sentence still tells the operator to run a deleted command.

Out of this removal. kronika-dev migrate-identity-paths and src/kronika/infrastructure/runtime/local_state_migration.py are the workstation copy tool. C9-A did not make them obsolete. The refusal safeguard in section 4 calls build_migration_plan. Deleting the module would remove the safeguard.

Risk: deleting a helper that deploy still calls. The grant's first edit step is a caller list for every deleted function; a routine caller stops the cut.

3. Transitional client options

Searched the web shell, companion extension, capture assets, and CLIs. No obsolete client or companion option remains.

Extension tree: ledger file count extension is 0; a search of extension/**/*.js finds no framenest.

Mutation gate: MUTATION_HEADERS in src/kronika/adapters/api/tailscale_ingress.py is only x-kronika-request. The old header is not accepted.

Recovery CLI: tests/contract/test_recovery_cli.py asserts --remote-layout is absent. That flag was removed in C7-B.

src/kronika/identity_env.py lookup_env reads only KRONIKA_. COMPATIBLE_ENVIRONMENT_PREFIX is used to strip a retired spelling from a child environment (drop_identity_environment_spellings) and to name it in an error class. There is no raise IdentityEnvironmentConflictError anywhere under src/. This is a strip safeguard, not a client fallback, and it is not removed.

X-FrameNest-Request still occurs 37 times in 16 files. Those are historical and test strings, not an accepted client header. They stay for the semantic classification; they are not a removal candidate.

4. Keeps

Each of these was found at a definition. Removal in sections 1-2 must not edit them.

Durable marker readers, deploy/ubuntu/kronika_release.py 46-67 and 1492-1617. ACCEPTED_RELEASE_SHA_MARKERS is (".framenest-release-sha", ".kronika-release-sha"). ACCEPTED_RELEASE_MANIFEST_MARKERS is the matching pair of manifest filenames. ACCEPTED_RELEASE_SHA_MANIFEST_KEYS is ("framenest_release_sha", "kronika_release_sha"). manifest_release_sha, parse_release_marker_presence, read_release_markers, and ResolvedReleaseMarkers resolve every spelling and fail on disagreement. Writers still emit only the canonical names (RELEASE_SHA_MARKER, RELEASE_MANIFEST_MARKER, RELEASE_SHA_MANIFEST_KEY, and make_manifest). Pins: test_every_reader_resolves_through_the_accepted_marker_tables and test_release_marker_presence_probes_every_accepted_spelling in tests/contract/test_kronika_cli_and_release_readers.py. Why: rollback still reads release trees written before the marker rename. Layout removal changes which directory is current; it does not change how a tree's identity is read.

Alembic shim, src/kronika/infrastructure/persistence/alembic_compat.py install_alembic_package_alias (79), names ALIASED_NAMES, called from src/kronika/infrastructure/persistence/migrations.py line 127. Why: eleven frozen revisions import framenest.infrastructure.persistence.sqlite_batch_fk. Part A forbids editing those bytes. No migration deletion touches this module or the versions/ directory.

Local-state refusal, refuse_silent_legacy_state_replacement at src/kronika/infrastructure/runtime/local_state_migration.py 1365, invoked from src/kronika/infrastructure/runtime/development.py around 221 before a launcher creates canonical state. Pins: test_legacy_state_detector_refuses_and_clears and test_launcher_refuses_legacy_state_before_creating_canonical_state in tests/contract/test_local_state_migration.py. Why: a legacy database with no canonical copy must not be replaced by an empty catalog. Defaults are already under Kronika (development.py 727-745).

Also untouched. POETRY_BIN, CPYTHON_BIN. Frozen mount /mnt/framenest-catalog-offdevice in deploy/systemd/kronika-catalog-offdevice.service and deploy/systemd/kronika.env.example. STATE_DIR_NAME = "framenest-chatgpt-page" in src/kronika_capture/config.py. FrameNest* class residue, excluded for the life of this whole by the session-25 plan section 4. Part A files.

DEPLOYMENT_STATE_DIR = "/var/lib/framenest/chatgpt-page" in src/kronika/infrastructure/ai/chatgpt_page/budget.py 18 has no other caller. It is not a layout selector and not one of the three named keeps. Leave it; classify it in section 6 as a parked path. Do not retarget it inside C9-B.

5. Living-document finalization

Frozen, do not edit: every file in FROZEN_DOCUMENT_SHA256 (ADRs 0001-0084, docs/FEDORA_SERVICE.md, docs/NUC_HOST_BASELINE.md), the 36 Alembic revision files, and ADR-0085 (no ADR amendment). docs/adr/README.md stays an index of those decisions.

Correct, because the sentence is now false or would invoke a deleted command:

docs/UBUNTU_NUC_DEPLOYMENT.md "Capture Path Migration" (273-326) and "Identity Migration" (1137 onward), including the copy-paste migrate-capture-paths and migrate-identity commands and the former-pointer restoration steps. Replace each procedure with one explicit historical sentence: the cut ran, the commands are gone, routine status/check/deploy/rollback address only the canonical layout and do not migrate. Keep the marker-reader sentence at 1059-1061 and the frozen tooling paths at 609-610.

deploy/ubuntu/README.md line 58, which still instructs migrate-capture-paths. Same historical sentence. The docs contract currently requires that sentence (test_nuc_release_docs.py around 440); update the pin in the same commit.

DEVELOPMENT.md 157-160. It says launcher state stays put "until the later identity switch". The launcher defaults are already ~/Library/Application Support/Kronika and $XDG_DATA_HOME/Kronika. Say that, and say migrate-identity-paths remains the workstation copy for a leftover legacy tree, with the refusal in front of an empty catalog.

ROADMAP.md 79-80. "mass kronika rename" does not name the actual exclusion. Say ADR-0085 is implemented as bounded cuts, and the retained FrameNest* class residue is excluded for this whole.

README.md 89-91. Schema head 0035 is on this public commit, while the sentence still says the private-record evidence "is not yet accepted, deployed, or published". Reconcile that clause with the ROADMAP statement that S8/S9 are on public main. Do not reopen Gallery, desktop, Cover Studio, or publication scope.

Engine module docstring, lines 11-12, with the layout retool.

Already explicitly historical; leave the dated fact, do not present it as the live tree:

README 75-78 and 393-397, PRODUCT 185-189, SERVER 189-193: commit aec2f009... at /opt/framenest/releases/... with schema 0028, each already labeled dated history.

Keep and label as retained, not as debt:

Frozen tooling paths in AGENTS.md and the runbook.

Frozen mount in docs/BACKUP_AND_RECOVERY.md 136, 146, 522.

Live host identity framenest-nuc in docs/OPERATOR_NETWORK.md. The Cooperator kept that identity.

Historical acceptance title in docs/ACCEPTANCE_DUAL_AUDIENCE.md. It names a completed run.

Sidecar spelling {media_filename}.framenest.json in README 578, as a historical filename readers still recognize. Confirm the reader test before any wording change; do not drop the historical name if the reader still accepts it.

Do not create docs/UBUNTU_NUC_CLEAN_INSTALL.md. That file is C-INSTALL-DOC, after C9-B. SPEC.md has no retired-package claim to correct (importable package name MUST be kronika at 1115). SECURITY.md has no framenest hit.

6. Semantic classification

After each implementation commit, every remaining case-insensitive framenest hit outside the ledger file is placed in exactly one category by the definition that owns it:

Frozen document or frozen revision. Path is in Part A. Rule: do not edit. Movement 0.

Durable-reader historical spelling. The accepted marker filenames, the manifest keys, and the functions that read them. Rule: keep.

Frozen tooling. Path prefix /opt/framenest/tooling/. Rule: keep POETRY_BIN and CPYTHON_BIN.

Frozen mount. /mnt/framenest-catalog-offdevice. Rule: keep the unit, the env template, and the backup runbook.

Frozen state-directory name. framenest-chatgpt-page. Rule: keep STATE_DIR_NAME and its resolution tests.

Retained live host identity. framenest-nuc in operator docs. Rule: keep.

Alembic shim. The four aliased module names in alembic_compat.py. Rule: keep.

Excluded class residue. A FrameNest identifier that is a class, exception, logger, or formatter. Rule: do not rename.

Log sanitizer needle. The credentials path inside _assert_logs_sanitized only. Rule: keep.

Retired-prefix strip. identity_env.COMPATIBLE_ENVIRONMENT_PREFIX and drop_identity_environment_spellings. Rule: keep; it is not a value source.

Parked budget path. DEPLOYMENT_STATE_DIR only. Rule: leave for a later capture decision.

Explicit historical prose. A living document sentence that names a past release path or a completed acceptance and says it is history. Rule: may stay; it must not read as a current command.

Ledger self-reference. tests/contract/test_kronika_identity_retention.py is excluded by _SELF_RELATIVE_PATH. Comments that restate arithmetic go there, not into counted files.

Unclassified. Stop the commit. Do not invent a category.

A former-layout or migration hit is not a remaining category. After the commit it is absent.

Ledger arithmetic, measured the way the tests measure it:

Part A: byte hashes. This plan edits none of the 86 documents or 36 revisions. Delta 0.

Part B: basenames containing framenest. The set is empty and CANONICAL_REPLACEMENT_PATHS has 20 members. No renamed basename is introduced. Delta 0.

Part C: per-tree file counts and text.lower().count("framenest"), plus content-path membership, host-path keys, User=/Group=, FRAMENEST_[A-Z0-9_]+, bare FRAMENEST_, X-FrameNest-Request, capitalized FrameNest, and framenest-[a-z0-9-]+. The before pins are src files 183 / occ 1604, tests 174 / 1386, deploy 3 / 72, scripts 0 / 0, docs 84 / 751, extension 0 / 0; /opt/framenest 145, /etc/framenest 30, /var/lib/framenest 64, /var/cache/framenest 19, mount 23; User=framenest 4, Group=framenest 5; env tokens 116, distinct 44, bare 22; header 37 / 16 files; capitalized 2327 / 343; console scripts 0.

Deploy's 72 is the whole deploy tree: 68 case-sensitive hits in the engine, plus the FRAMENEST_ prefix constant, plus one mount comment in the env example, plus two mount paths in the offdevice unit. The last three stay. The engine drops every hit that is not a marker, a tooling path, or the sanitizer needle. A file leaves the content set only when its last hit leaves. The implementation records the delta from the retention failure before the re-pin. It does not pre-write the after integers in the grant, and it does not add the substring in a counted comment.

7. Proof and mutations

Each implementation commit, through ./.ap/ap exec --baseline <that commit's parent> --operation test and node --test from the worktree root:

Full Python suite. Orchestrator baseline at the start commit: 5016 passed, 8 skipped, 3 warnings, 0 failed. Skips stay the five real-tool cover cases, two real-tool media-analysis cases, and one NVIDIA smoke case.

The contract modules this cut touches, named in the grant, rather than an unnamed subset.

JavaScript: companion_web_bridge 23, companion_review_extension 41, x_companion_extension 55, companion_settings_automatic_analysis 6, kronika_ui 12, catalog_card_ai_quick_action 30, bounded frontend/cockpit/gallery glob 212. These should not move; a movement stops the cut.

Retention module: 15 passed, including Part A hashes and the 36-key Alembic set.

Wheel and resources: the existing tests/contract/test_chatgpt_page_packaging.py cases test_importlib_resources_resolve_packaged_assets and test_wheel_contains_kernel_assets_and_entry_point. No new packaging command.

Canonical executables: pyproject.toml [project.scripts] stays the fourteen kronika-* entries including kronika-capture. deploy/ubuntu/kronika-release remains the only release entry. Parser subcommands after the migration deletion are exactly status, check, deploy, rollback, activate-capture, rollback-capture, and hidden _remote (_remote-extract, _remote-relocate-venv-shebangs).

Mutations, each restored before the suite:

Re-add migrate-identity to the parser. The new parser-surface test fails.

Put OLD_WEB_LAYOUT back into the candidate tuple passed to selection. The new single-layout test fails.

Make resolve_capture_pointer return /opt/framenest/capture-current when no pointer exists. The capture-pointer test fails.

Delete .framenest-release-sha from ACCEPTED_RELEASE_SHA_MARKERS. test_every_reader_resolves_through_the_accepted_marker_tables fails.

Remove install_alembic_package_alias() from the migration loader. The existing Alembic alias test fails.

Make refuse_silent_legacy_state_replacement return immediately. test_launcher_refuses_legacy_state_before_creating_canonical_state fails.

Public-main equality is git rev-parse HEAD against git ls-remote origin refs/heads/main after the separately authorized publication. It is not a step inside an implementation commit.

8. Sub-grant split

Three commits, in order. Precedent is C7-B/1...B/3: one behavior each, one proof each, no publication inside the commit.

C9-B/1 - Delete the one-time commands. Sections 2 and the runbook/README sentences that name those commands, plus the migration test file and the docs pin. Routine dual-layout selection still exists at the end of this commit, so the "cannot select a deleted layout" proof is not claimed here. Proof: parser test, caller check, both suites, retention re-pin, mutation of the parser.

C9-B/2 - Canonical layout only. Section 1. Proof: single-layout test, capture-pointer test, accepted_release_roots has one root, both suites, retention re-pin, the two layout mutations. Marker, tooling, shim, and refusal tests stay green without being edited except where a fixture literally built OLD_WEB_LAYOUT.

C9-B/3 - Living truth. Section 5 sentences that are not the deleted-command procedures (those moved with B/1), plus the section 6 classification written into the implementation report. Proof: docs contract, retention, classification has no unclassified hit, both suites. No new runbook file.

After B/3, and not inside any of the three: publication of the resulting SHA, routine NUC refresh to that SHA through deploy/ubuntu/kronika-release, then rendered acceptance. C-INSTALL-DOC follows C9-B and is not folded into B/3. CLOSE is a later read-only acceptance.

Open questions

None that block the split. The parked budget path and the unraised identity-conflict class are classified above and left in place.

Smallest next step: accept this plan, then issue C9-B/1 against 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 with the migration-only deletion list and the parser mutation named.

Resolved Execution Issues / Near-Misses

git status at conversation start showed a dirty tree; a fresh read-only inspection showed a clean tree at the expected SHA. The snapshot was stale. No file was written.

Pre-Existing Failure Classification

none

Orchestration critique:
MEASURED: none
LEAD: DEPLOYMENT_STATE_DIR is a single unused-by-callers parked path under the retired state root; cheapest check is whether any host unit still points at /var/lib/framenest/chatgpt-page, and that check is host contact, so it stays outside this plan.
