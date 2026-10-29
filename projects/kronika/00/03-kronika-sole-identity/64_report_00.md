### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 64
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B3 — living truth and the semantic classification
status: BLOCKED
Phase-qualified result: not-applicable
Start commit: 9b291e936e93026ebe540b4a23a11b89721747a8
End commit: 9b291e936e93026ebe540b4a23a11b89721747a8
Report justification: new-evidence
Logical-whole closure: not-closed

Gates re-derived before mutation. Local `main` was clean at `9b291e936e93026ebe540b4a23a11b89721747a8`. `git ls-remote origin refs/heads/main` was `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. The containing `.ap` gitlink and submodule `HEAD` were both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap doctor` PASS, governing variant stable. `ap project check --baseline 9b291e936e93026ebe540b4a23a11b89721747a8` PASS. The two-commit lead over public `main` is the unpublished C9-B/1 and C9-B/2 pair. Primary recovery class for that lead: `unpublished-candidate`. No host contact and no browser.

The commit was not made. The classification gate found 808 occurrences with no owning category. The three sentence edits and the measured retention re-pin are in the working tree and are not committed. `FROZEN_DOCUMENT_SHA256` has 86 keys. `FROZEN_ALEMBIC_SHA256` has 36 keys.

## 1. Sentence matrix

The three sentences are edited in the worktree. Nothing else in those documents changed.

**DEVELOPMENT.md.** Truth: `_database_path` in `src/kronika/infrastructure/runtime/development.py` already returns `~/Library/Application Support/Kronika/...` on darwin and `$XDG_DATA_HOME/Kronika/...` otherwise. `DevelopmentRuntime.start` calls `refuse_silent_legacy_state_replacement` before it creates state. `kronika-dev migrate-identity-paths` remains the workstation copy.

Old:

```text
The runtime default locations themselves do not change: until the later
identity switch, launcher-managed state continues at its current locations and
the migration copies it to the canonical destinations. The private migration
receipts are the evidence required before that switch.
```

New:

```text
Launcher defaults are already `~/Library/Application Support/Kronika` on macOS
and `$XDG_DATA_HOME/Kronika` elsewhere. `kronika-dev migrate-identity-paths`
remains the workstation copy tool for a leftover legacy tree, with the
refusal safeguard in front of creating an empty catalog.
```

**ROADMAP.md.** Truth: ADR-0085 is already described there as ordered bounded cuts. The exclusion named by the session-25 plan is the retained `FrameNest*` class residue.

Old:

```text
an ordered sequence of bounded cuts rather than a mass `kronika` rename.
```

New:

```text
an ordered sequence of bounded cuts, and the retained `FrameNest*` class
residue is excluded for this whole.
```

**README.md.** Truth at public `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`: that commit's ROADMAP says S8 is on public `main` and that migration `0034` is accepted and published, and `src/kronika/infrastructure/persistence/alembic_environment/versions/0034_kronika_records.py` exists there. The clause now says that, and only that. Gallery, desktop, Cover Studio, and publication sentences were not edited. No NUC deployment claim was added.

Old:

```text
including private Kronika records and administrator approval as implemented
working-tree evidence that is not yet accepted, deployed, or published,
```

New:

```text
including private Kronika records and administrator approval, which are
accepted and on public `main`,
```

## 2. Sidecar confirmation and pins

Sidecar sentence in README left unchanged. `tests/contract/test_kronika_durable_artifact_readers.py::test_sidecar_store_observes_both_filename_spellings` passed: `COMPATIBLE_SIDECAR_FILENAME_SUFFIX == ".framenest.json"`, and the store observes that historical name after the canonical file is removed.

No test module asserts the three corrected phrases. A search of `tests/` for those phrases found none. The only pin this diff moves is in `tests/contract/test_kronika_identity_retention.py`.

## 3. Semantic classification

Scan command, ledger file excluded, same tracked set the retention counter uses:

```text
git grep -I -o -i framenest -- . ':(exclude)tests/contract/test_kronika_identity_retention.py'
```

That command returns 3375 occurrences. `.ap` was scanned separately with `git -C .ap grep -n -I -i framenest` and is out of scope (16 lines, listed below).

A hit was placed in a category only when one of the granted definitions owns it. Part A paths own every hit in those files. The 61 `class FrameNest…` identifiers, including `FrameNestLogger`, `FrameNestRedactionFilter`, and `FrameNestJsonFormatter`, own uses of those identifiers. The new ROADMAP `FrameNest*` sentence is that class-residue label, so its one occurrence is counted there. One runbook sentence was reclassified by reading it: `docs/UBUNTU_NUC_DEPLOYMENT.md` lines 13–17 name `/opt/framenest/releases/aec2f009…` and say that fact is dated history.

| Category | Occurrences |
|---|---:|
| Excluded class residue | 1812 |
| Frozen document or frozen revision | 673 |
| Durable-reader historical spelling | 20 |
| Frozen state-directory name | 12 |
| Frozen mount | 12 |
| Alembic shim | 12 |
| Frozen tooling | 11 |
| Explicit historical prose | 7 |
| Retained live host identity | 4 |
| Retired-prefix strip | 2 |
| Log sanitizer needle | 1 |
| Parked budget path | 1 |
| Unclassified | 808 |
| Total | 3375 |

Zero unclassified is false. 808 occurrences, 449 aggregated file/token rows, stop the commit. No category was invented for them. They include the historical sidecar suffix, `X-FrameNest-Request`, protocol and storage keys, durable artifact filenames that are not the release-marker pair, environment names outside `identity_env.py`, host paths that are not the tooling prefix or the frozen mount, package docstrings such as `"""FrameNest package."""`, the S10 row's bare `FrameNest`, seven bare `framenest` product-name hits in ADR-0085 (that file is not in `FROZEN_DOCUMENT_SHA256`), and the removed-wrapper names in `AGENTS.md`.

The two large owned sets are not pasted line by line: Excluded class residue is 364 aggregated rows and Frozen document or frozen revision is 320 aggregated rows. Their occurrence totals are in the table above and are part of the 3375 sum. That omission is disclosed. Every other owned row is below. The unclassified table is complete after moving the one runbook occurrence out of it.

Owned rows other than class residue and Part A:

```text
1	AGENTS.md	.framenest-release-manifest.json	Durable-reader historical spelling
1	AGENTS.md	.framenest-release-sha	Durable-reader historical spelling
1	AGENTS.md	/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry	Frozen tooling
1	AGENTS.md	/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13	Frozen tooling
1	PRODUCT.md	/opt/framenest/releases/aec2f0091c10aed2fc2033dac154a0d9651b2b6d	Explicit historical prose
2	README.md	/opt/framenest/releases/aec2f0091c10aed2fc2033dac154a0d9651b2b6d	Explicit historical prose
1	SERVER.md	/opt/framenest/releases/aec2f0091c10aed2fc2033dac154a0d9651b2b6d	Explicit historical prose
1	docs/UBUNTU_NUC_DEPLOYMENT.md	/opt/framenest/releases/aec2f0091c10aed2fc2033dac154a0d9651b2b6d	Explicit historical prose
2	docs/ACCEPTANCE_DUAL_AUDIENCE.md	framenest-public-published-surface-and-tailscale-workspace	Explicit historical prose
1	deploy/systemd/kronika-catalog-offdevice.service	/mnt/framenest-catalog-offdevice	Frozen mount
1	deploy/systemd/kronika-catalog-offdevice.service	/mnt/framenest-catalog-offdevice/bundles	Frozen mount
1	deploy/systemd/kronika.env.example	/mnt/framenest-catalog-offdevice	Frozen mount
1	deploy/ubuntu/kronika_release.py	.framenest-release-manifest.json	Durable-reader historical spelling
1	deploy/ubuntu/kronika_release.py	.framenest-release-sha	Durable-reader historical spelling
1	deploy/ubuntu/kronika_release.py	/etc/framenest/credentials	Log sanitizer needle
1	deploy/ubuntu/kronika_release.py	/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry	Frozen tooling
1	deploy/ubuntu/kronika_release.py	/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13	Frozen tooling
1	deploy/ubuntu/kronika_release.py	framenest_release_sha	Durable-reader historical spelling
2	docs/BACKUP_AND_RECOVERY.md	/mnt/framenest-catalog-offdevice	Frozen mount
3	docs/OPERATOR_NETWORK.md	framenest-nuc	Retained live host identity
1	docs/UBUNTU_NUC_DEPLOYMENT.md	.framenest-release-sha	Durable-reader historical spelling
1	docs/UBUNTU_NUC_DEPLOYMENT.md	/mnt/framenest-catalog-offdevice	Frozen mount
1	docs/UBUNTU_NUC_DEPLOYMENT.md	/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry	Frozen tooling
1	docs/UBUNTU_NUC_DEPLOYMENT.md	/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13	Frozen tooling
1	docs/adr/0085-kronika-sole-identity.md	/mnt/framenest-catalog-offdevice	Frozen mount
1	docs/adr/0085-kronika-sole-identity.md	/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry	Frozen tooling
1	docs/adr/0085-kronika-sole-identity.md	/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13	Frozen tooling
1	docs/adr/0085-kronika-sole-identity.md	framenest-chatgpt-page	Frozen state-directory name
1	docs/adr/0085-kronika-sole-identity.md	framenest.infrastructure.persistence.sqlite_batch_fk	Alembic shim
2	src/kronika/identity_env.py	FRAMENEST_	Retired-prefix strip
1	src/kronika/infrastructure/ai/chatgpt_page/budget.py	/var/lib/framenest/chatgpt-page	Parked budget path
5	src/kronika/infrastructure/persistence/alembic_compat.py	framenest	Alembic shim
2	src/kronika/infrastructure/persistence/alembic_compat.py	framenest.infrastructure	Alembic shim
2	src/kronika/infrastructure/persistence/alembic_compat.py	framenest.infrastructure.persistence	Alembic shim
2	src/kronika/infrastructure/persistence/alembic_compat.py	framenest.infrastructure.persistence.sqlite_batch_fk	Alembic shim
1	src/kronika/infrastructure/persistence/catalog_backup_offdevice.py	/mnt/framenest-catalog-offdevice	Frozen mount
1	src/kronika_capture/_assets/extension/src/headless/bridge_client.mjs	framenest-chatgpt-page	Frozen state-directory name
1	src/kronika_capture/cli.py	framenest-chatgpt-page	Frozen state-directory name
1	src/kronika_capture/config.py	framenest-chatgpt-page	Frozen state-directory name
1	src/kronika_capture/paths.py	/.local/state/framenest-chatgpt-page	Frozen state-directory name
1	src/kronika_capture/paths.py	XDG_STATE_HOME/framenest-chatgpt-page	Frozen state-directory name
1	src/kronika_capture/paths.py	framenest-chatgpt-page	Frozen state-directory name
2	tests/contract/test_catalog_offdevice_timer.py	/mnt/framenest-catalog-offdevice	Frozen mount
1	tests/contract/test_catalog_offdevice_timer.py	/mnt/framenest-catalog-offdevice/bundles	Frozen mount
1	tests/contract/test_chatgpt_page_packaging.py	framenest-chatgpt-page	Frozen state-directory name
1	tests/contract/test_kronika_capture_services.py	framenest_release_sha	Durable-reader historical spelling
2	tests/contract/test_kronika_cli_and_release_readers.py	.framenest-release-manifest.json	Durable-reader historical spelling
7	tests/contract/test_kronika_cli_and_release_readers.py	.framenest-release-sha	Durable-reader historical spelling
3	tests/contract/test_kronika_cli_and_release_readers.py	framenest_release_sha	Durable-reader historical spelling
1	tests/contract/test_local_state_migration.py	/synthetic/framenest-chatgpt-page	Frozen state-directory name
2	tests/contract/test_local_state_migration.py	framenest-chatgpt-page	Frozen state-directory name
1	tests/contract/test_nuc_release_docs.py	.framenest-release-manifest.json	Durable-reader historical spelling
1	tests/contract/test_nuc_release_docs.py	/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry	Frozen tooling
1	tests/contract/test_nuc_release_docs.py	/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13	Frozen tooling
1	tests/contract/test_nuc_release_remote_contract.py	/opt/framenest/tooling	Frozen tooling
1	tests/contract/test_operator_network_scripts.py	framenest-nuc	Retained live host identity
1	tests/unit/chatgpt_page/test_projects.py	framenest-chatgpt-page	Frozen state-directory name
1	tests/unit/infrastructure/backup/test_catalog_backup_offdevice.py	/mnt/framenest-catalog-offdevice	Frozen mount
```

`.ap/` out of scope, 16 lines:

```text
.ap/CHANGELOG.md:72, 92, 111, 122 FrameNest
.ap/README.md:98 ap bundle framenest
.ap/docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md:153, 169 FrameNest
.ap/docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md:61, 62, 100 FrameNest
.ap/docs/adr/0021-followable-spine-and-restatement-conversion.md:75, 77, 114, 150 FrameNest
.ap/docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md:34 FrameNest
.ap/docs/adr/README.md:83 FrameNest
```

Unclassified rows, count then file then token. The runbook release-path row is absent here because it is Explicit historical prose. Column sums of this list are 808.

```text
2	.gitignore	/.framenest/
1	AGENTS.md	deploy/ubuntu/framenest-release
1	AGENTS.md	deploy/ubuntu/framenest_release.py
1	README.md	.framenest.json
1	ROADMAP.md	FrameNest
1	docs/BACKUP_AND_RECOVERY.md	.framenest-catalog-offdevice.json
1	docs/OPERATOR_NETWORK.md	FRAMENEST_
1	docs/OPERATOR_NETWORK.md	framenest_nuc_worker_gate.fish
7	docs/adr/0085-kronika-sole-identity.md	framenest
1	docs/adr/0085-kronika-sole-identity.md	src/framenest
3	docs/adr/README.md	framenest
1	docs/provenance/kronika-capture.json	//github.com/cisarik/framenest.git
25	docs/provenance/kronika-capture.json	FrameNest
1	docs/provenance/kronika-capture.json	framenest_baseline
32	docs/provenance/kronika-capture.json	framenest_origin
1	src/kronika/__init__.py	FrameNest
1	src/kronika/adapters/api/application.py	FrameNest
1	src/kronika/adapters/api/tailscale_ingress.py	FrameNest
1	src/kronika/adapters/api/upload_api.py	FrameNest
1	src/kronika/adapters/api/web/__init__.py	FrameNest
3	src/kronika/adapters/api/web/app.js	...framenestRevisionHeader
1	src/kronika/adapters/api/web/app.js	X-FrameNest-Request
3	src/kronika/adapters/api/web/app.js	element.__framenestCleanup
2	src/kronika/adapters/api/web/app.js	element.__framenestGifImage
1	src/kronika/adapters/api/web/app.js	element.__framenestGifImage.onerror
1	src/kronika/adapters/api/web/app.js	element.__framenestGifImage.onload
1	src/kronika/adapters/api/web/app.js	element.__framenestGifImage.removeAttribute
1	src/kronika/adapters/api/web/app.js	framenest.catalog.pageSize
1	src/kronika/adapters/api/web/app.js	framenest.upload.recovery.v1
1	src/kronika/adapters/api/web/app.js	framenest.youtube.currentClaim.v1
8	src/kronika/adapters/api/web/app.js	framenestJSONHeaders
33	src/kronika/adapters/api/web/app.js	framenestMutationHeaders
3	src/kronika/adapters/api/web/app.js	framenestResponseRevision
1	src/kronika/adapters/api/web/app.js	framenestRevisionHeader
1	src/kronika/adapters/cli/backup.py	FrameNest
1	src/kronika/adapters/cli/catalog.py	FrameNest
1	src/kronika/adapters/cli/development.py	FrameNest
1	src/kronika/adapters/cli/recovery.py	FrameNest
1	src/kronika/application/__init__.py	FrameNest
1	src/kronika/application/media_analysis_coordinator.py	framenest-media-analysis
1	src/kronika/application/media_analysis_coordinator.py	framenest-media-analysis-coordinator
1	src/kronika/application/media_analysis_lifecycle.py	FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED
1	src/kronika/application/media_suggestion.py	framenest-media-suggestion-v4
1	src/kronika/application/ports/media_sidecar_store.py	.framenest.json
1	src/kronika/application/upload_catalog_coordinator.py	framenest-upload-catalog
1	src/kronika/application/upload_catalog_coordinator.py	framenest-upload-catalog-coordinator
1	src/kronika/application/upload_publication_coordinator.py	framenest-upload-publication
1	src/kronika/application/upload_publication_coordinator.py	framenest-upload-publication-coordinator
1	src/kronika/application/upload_validation_coordinator.py	FrameNest
1	src/kronika/application/upload_validation_coordinator.py	framenest-upload-validation
1	src/kronika/application/upload_validation_coordinator.py	framenest-upload-validation-coordinator
1	src/kronika/application/x_acquisition.py	FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED.
1	src/kronika/application/x_acquisition.py	framenest-x-acquisition
1	src/kronika/application/youtube_acquisition.py	framenest-youtube-acquisition-coordinator
2	src/kronika/configuration.py	/run/framenest/framenest-public.sock
2	src/kronika/configuration.py	/run/framenest/framenest.sock
1	src/kronika/configuration.py	FrameNest
1	src/kronika/domain/__init__.py	FrameNest
1	src/kronika/domain/devices.py	FrameNest.
3	src/kronika/domain/identities.py	FrameNest
1	src/kronika/domain/media_analysis_runs.py	framenest-media-suggestion-result-v1
1	src/kronika/domain/media_classification.py	framenest-movie-identification-prompt-v2
1	src/kronika/domain/media_classification.py	framenest-movie-identification-result-v1
1	src/kronika/domain/media_sidecar.py	framenest-media-sidecar
1	src/kronika/infrastructure/__init__.py	FrameNest
1	src/kronika/infrastructure/ai/configuration.py	FrameNest
1	src/kronika/infrastructure/ai/configuration.py	framenest
1	src/kronika/infrastructure/ai/nvidia_nim.py	FrameNest
1	src/kronika/infrastructure/media_analysis/contact_sheet.py	framenest-contact-
1	src/kronika/infrastructure/media_analysis/process.py	FrameNest-owned
1	src/kronika/infrastructure/media_analysis/process.py	framenest-media-analysis-stderr-reader
1	src/kronika/infrastructure/media_analysis/process.py	framenest-media-analysis-stdout-reader
1	src/kronika/infrastructure/persistence/__init__.py	FrameNest-owned
1	src/kronika/infrastructure/persistence/alembic_compat.py	framenest.
1	src/kronika/infrastructure/persistence/alembic_environment/__init__.py	FrameNest
1	src/kronika/infrastructure/persistence/catalog_backup.py	.framenest-backup-
1	src/kronika/infrastructure/persistence/catalog_backup.py	framenest
1	src/kronika/infrastructure/persistence/catalog_backup_offdevice.py	.framenest-catalog-offdevice.json
1	src/kronika/infrastructure/persistence/catalog_backup_offdevice.py	.framenest-offdevice-stage-
1	src/kronika/infrastructure/persistence/catalog_backup_offdevice.py	FrameNest-owned
1	src/kronika/infrastructure/persistence/catalog_backup_offdevice.py	framenest-catalog-offdevice
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	.framenest-pull-stage-
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	.framenest-workstation-snapshot-store.json
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	framenest-catalog-backup-export
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	framenest-ssh-stderr-drain
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	framenest-workstation-catalog-snapshot
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py	framenest-workstation-snapshot-store
1	src/kronika/infrastructure/persistence/catalog_schema.py	FrameNest
1	src/kronika/infrastructure/persistence/cli.py	FrameNest
1	src/kronika/infrastructure/persistence/errors.py	FrameNest.
2	src/kronika/infrastructure/persistence/identity_labels.py	FrameNest
1	src/kronika/infrastructure/runtime/__init__.py	FrameNest
1	src/kronika/infrastructure/runtime/development.py	FrameNest.
1	src/kronika/infrastructure/runtime/local_state_migration.py	FrameNest
1	src/kronika/infrastructure/runtime/local_state_migration.py	framenest
1	src/kronika/infrastructure/runtime/local_state_migration.py	framenest-development
1	src/kronika/server.py	FrameNest.
1	src/kronika/structured_logging.py	FrameNest
1	src/kronika/structured_logging.py	FrameNest-owned
1	src/kronika_capture/__init__.py	FrameNest
1	src/kronika_capture/__init__.py	FrameNest-owned
2	tests/admin_batch_actions_frontend.test.js	/framenestMutationHeaders/
2	tests/admin_batch_actions_frontend.test.js	X-FrameNest-Request
1	tests/admin_batch_actions_frontend.test.js	framenestMutationHeaders
2	tests/admin_content_publication_frontend.test.js	/framenestMutationHeaders/
1	tests/ai_providers_admin_frontend.test.js	X-FrameNest-Request
4	tests/ai_providers_admin_frontend.test.js	framenestMutationHeaders
1	tests/ai_providers_admin_frontend.test.js	framenestResponseRevision
1	tests/ai_providers_admin_frontend.test.js	framenestRevisionHeader
2	tests/browser/x_browser_server.py	FrameNest
1	tests/browser_catalog_removal_evidence.test.js	framenest-removal-
1	tests/browser_companion_evidence.test.js	framenest-companion-
1	tests/browser_cover_evidence.test.js	FrameNest
1	tests/browser_cover_evidence.test.js	framenest-browser-
1	tests/browser_movie_identification_evidence.test.js	framenest-movie-browser-
1	tests/browser_movie_identification_evidence.test.js	framenest-movie-identification-prompt-v2
1	tests/browser_movie_identification_evidence.test.js	framenest-movie-identification-result-v1
1	tests/browser_movie_identification_evidence.test.js	window.__framenestConsoleErrors
1	tests/catalog_card_ai_quick_action.test.js	/framenestMutationHeaders
6	tests/catalog_card_ai_quick_action.test.js	X-FrameNest-Request
1	tests/catalog_card_ai_quick_action.test.js	context.framenestMutationHeaders
3	tests/catalog_card_ai_quick_action.test.js	framenestMutationHeaders
1	tests/catalog_card_ai_quick_action.test.js	framenestMutationHeaders/g
1	tests/companion_review_extension.test.js	/FrameNest/
1	tests/companion_review_extension.test.js	/FrameNest/i
1	tests/companion_review_extension.test.js	/frameNestOrigin
1	tests/companion_review_extension.test.js	/framenest
1	tests/companion_review_extension.test.js	FrameNest
2	tests/companion_review_extension.test.js	X-FrameNest-Request
1	tests/companion_review_extension.test.js	X-FrameNest/
1	tests/companion_review_extension.test.js	both.state.storage.frameNestOrigin
6	tests/companion_review_extension.test.js	frameNestOrigin
3	tests/companion_review_extension.test.js	framenest
1	tests/companion_review_extension.test.js	framenest-companion.v1
1	tests/companion_review_extension.test.js	framenest-companion.v2
1	tests/companion_review_extension.test.js	framenest.companion.review.v1
1	tests/companion_review_extension.test.js	framenest.companion.web.v1
1	tests/companion_review_extension.test.js	framenest.companion.web.v2
2	tests/companion_review_extension.test.js	framenest.review-inbox
1	tests/companion_review_extension.test.js	retiredOnly.state.storage.frameNestOrigin
2	tests/companion_review_extension.test.js	worker.state.storage.frameNestOrigin
1	tests/companion_settings_automatic_analysis.test.js	X-FrameNest-Request
1	tests/companion_web_bridge.test.js	/framenest
1	tests/companion_web_bridge.test.js	FRAMENEST.COMPANION.WEB.V1
1	tests/companion_web_bridge.test.js	framenest.companion.review.v1
1	tests/companion_web_bridge.test.js	framenest.companion.v1
1	tests/companion_web_bridge.test.js	framenest.companion.web
3	tests/companion_web_bridge.test.js	framenest.companion.web.v1
1	tests/companion_web_bridge.test.js	framenest.companion.web.v2
1	tests/contract/test_ai_provider_admin_api.py	framenest.sock
2	tests/contract/test_ai_server_composition.py	FRAMENEST_AI_CONFIG_PATH
1	tests/contract/test_analysis_proposal.py	FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS
1	tests/contract/test_analysis_proposal.py	framenest.sock
2	tests/contract/test_ap_integration.py	FrameNest
1	tests/contract/test_ap_project_contract.py	FrameNest
1	tests/contract/test_automatic_analysis_privacy_contract.py	FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED
1	tests/contract/test_automatic_analysis_settings_api.py	framenest.sock
1	tests/contract/test_backup_cli.py	FrameNest
1	tests/contract/test_catalog_cli.py	FrameNest
2	tests/contract/test_catalog_cli.py	framenest-media-suggestion-v1
1	tests/contract/test_catalog_identity_labels.py	FrameNest
2	tests/contract/test_catalog_identity_labels.py	framenest
1	tests/contract/test_catalog_identity_labels.py	framenest-development
2	tests/contract/test_chatgpt_page_packaging.py	framenest
1	tests/contract/test_chatgpt_page_packaging.py	framenest-
1	tests/contract/test_chatgpt_page_packaging.py	framenest.
1	tests/contract/test_chatgpt_page_packaging.py	framenest/
1	tests/contract/test_chatgpt_page_packaging.py	framenest_baseline
1	tests/contract/test_chatgpt_page_packaging.py	framenest_origin
1	tests/contract/test_companion_review_api.py	framenest-media-suggestion-result-v1
1	tests/contract/test_companion_review_api.py	framenest-media-suggestion-v4
2	tests/contract/test_companion_review_api.py	framenest.sock
1	tests/contract/test_content_publication_unpublish.py	framenest.sock
1	tests/contract/test_cover_ingress.py	framenest.sock
1	tests/contract/test_fedora_systemd_service.py	./framenest
2	tests/contract/test_fedora_systemd_service.py	/etc/framenest/framenest.env
2	tests/contract/test_fedora_systemd_service.py	/opt/framenest/current
1	tests/contract/test_fedora_systemd_service.py	/opt/framenest/current/.venv
6	tests/contract/test_fedora_systemd_service.py	/opt/framenest/current/.venv/bin/framenest-production
1	tests/contract/test_fedora_systemd_service.py	/run/framenest
1	tests/contract/test_fedora_systemd_service.py	/var/cache/framenest/gallery-previews
2	tests/contract/test_fedora_systemd_service.py	/var/lib/framenest/ai/config.json
1	tests/contract/test_fedora_systemd_service.py	/var/lib/framenest/catalog.sqlite3
1	tests/contract/test_fedora_systemd_service.py	framenest-
1	tests/contract/test_fedora_systemd_service.py	framenest/.venv
1	tests/contract/test_fedora_systemd_service.py	framenest/ai/config.json
1	tests/contract/test_gallery_preview_api.py	/tmp/framenest-gallery-preview-api.sqlite3
1	tests/contract/test_gallery_preview_api.py	/tmp/framenest-gallery-preview-cache
2	tests/contract/test_health_api.py	FRAMENEST_ENV_VARS
1	tests/contract/test_health_api.py	isolate_framenest_env
2	tests/contract/test_kronika_approved_projection.py	framenest-media-suggestion-result-v1
1	tests/contract/test_kronika_capture_services.py	framenest
1	tests/contract/test_kronika_capture_services.py	framenest.service
2	tests/contract/test_kronika_capture_services.py	framenest_release_capture
2	tests/contract/test_kronika_cli_and_release_readers.py	FRAMENEST_
1	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_
2	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_AI_CONFIG_PATH
3	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_CATALOG_BACKUP_ROOT
2	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_CATALOG_OFFDEVICE_DESTINATION_ID
1	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_DATABASE_PATH
1	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_DEVELOPMENT_RUNTIME_DIR
2	tests/contract/test_kronika_direct_reader_routing.py	FRAMENEST_PORT
1	tests/contract/test_kronika_durable_analysis_identity_readers.py	framenest
1	tests/contract/test_kronika_durable_analysis_identity_readers.py	framenest-media-suggestion-v3
6	tests/contract/test_kronika_durable_artifact_readers.py	.framenest-catalog-offdevice.json
3	tests/contract/test_kronika_durable_artifact_readers.py	.framenest-workstation-snapshot-store.json
1	tests/contract/test_kronika_durable_artifact_readers.py	.framenest.json
1	tests/contract/test_kronika_durable_artifact_readers.py	framenest
3	tests/contract/test_kronika_durable_artifact_readers.py	framenest-catalog-offdevice
1	tests/contract/test_kronika_durable_artifact_readers.py	framenest-media-sidecar
1	tests/contract/test_kronika_durable_artifact_readers.py	framenest-workstation-catalog-snapshot
2	tests/contract/test_kronika_durable_artifact_readers.py	framenest-workstation-snapshot-store
1	tests/contract/test_kronika_durable_artifact_readers.py	framenest_backups
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-backup-
3	tests/contract/test_kronika_durable_writer_identities.py	.framenest-backup-old.deadbeef
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-catalog-offdevice.json
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-offdevice-stage-
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-offdevice-stage-deadbeef
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-pull-stage-
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-pull-stage-deadbeef
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest-workstation-snapshot-store.json
1	tests/contract/test_kronika_durable_writer_identities.py	.framenest.json
2	tests/contract/test_kronika_durable_writer_identities.py	framenest
2	tests/contract/test_kronika_durable_writer_identities.py	framenest-catalog-backup-export
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-catalog-offdevice
3	tests/contract/test_kronika_durable_writer_identities.py	framenest-media-sidecar
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-media-suggestion-result-v1
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-media-suggestion-v4
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-movie-identification-prompt-v2
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-movie-identification-result-v1
2	tests/contract/test_kronika_durable_writer_identities.py	framenest-workstation-catalog-snapshot
1	tests/contract/test_kronika_durable_writer_identities.py	framenest-workstation-snapshot-store
2	tests/contract/test_kronika_identity_dual_read.py	FRAMENEST_
10	tests/contract/test_kronika_identity_dual_read.py	framenest.env
1	tests/contract/test_kronika_identity_dual_read.py	test_framenest_env_file_is_ignored
1	tests/contract/test_kronika_identity_dual_read.py	test_framenest_prefix_alone_is_ignored
4	tests/contract/test_kronika_mutation_header.py	X-FrameNest-Request
1	tests/contract/test_kronika_mutation_header.py	framenest.sock
1	tests/contract/test_kronika_mutation_header.py	x-framenest-request
1	tests/contract/test_kronika_product_string_agreement.py	framenest_alembic_environment_under_test
1	tests/contract/test_kronika_settings_parity.py	/srv/framenest/parity-value
1	tests/contract/test_kronika_settings_parity.py	FRAMENEST_
2	tests/contract/test_kronika_settings_parity.py	FRAMENEST_PORT
1	tests/contract/test_kronika_settings_parity.py	Framenest_Port
1	tests/contract/test_kronika_settings_parity.py	fRaMeNeSt_pOrT
2	tests/contract/test_kronika_settings_parity.py	framenest.env
5	tests/contract/test_kronika_settings_parity.py	framenest_port
2	tests/contract/test_local_state_migration.py	FRAMENEST_DATABASE_PATH
17	tests/contract/test_local_state_migration.py	FrameNest
5	tests/contract/test_local_state_migration.py	framenest
1	tests/contract/test_local_state_migration.py	framenest-browser-profile
3	tests/contract/test_local_state_migration.py	framenest-development
1	tests/contract/test_local_web_application.py	/Users/example/framenest
1	tests/contract/test_local_web_application.py	/Users/example/framenest/catalog.sqlite3
8	tests/contract/test_local_web_application.py	FrameNest
2	tests/contract/test_local_web_application.py	X-FrameNest-Request
3	tests/contract/test_local_web_application.py	framenest.catalog.pageSize
2	tests/contract/test_local_web_application.py	framenest.upload.recovery.v1
6	tests/contract/test_local_web_application.py	framenest.youtube.currentClaim.v1
2	tests/contract/test_local_web_application.py	framenestMutationHeaders
1	tests/contract/test_local_web_application.py	test_root_serves_framenest_application_document
1	tests/contract/test_media_analysis_api.py	/tmp/framenest-contract.sqlite3
1	tests/contract/test_media_analysis_lifecycle_api.py	/tmp/framenest-analysis-lifecycle-api-manual.sqlite3
1	tests/contract/test_media_analysis_lifecycle_api.py	/tmp/framenest-analysis-lifecycle-api-rerun.sqlite3
1	tests/contract/test_media_analysis_lifecycle_api.py	/tmp/framenest-analysis-lifecycle-api-side-effect.sqlite3
1	tests/contract/test_media_analysis_lifecycle_api.py	/tmp/framenest-analysis-lifecycle-api.sqlite3
1	tests/contract/test_media_analysis_lifecycle_api.py	/tmp/framenest-analysis-lifecycle-capability.sqlite3
5	tests/contract/test_media_analysis_lifecycle_api.py	framenest-media-suggestion-v3
1	tests/contract/test_media_catalog_api.py	/tmp/framenest-media-catalog-api.sqlite3
1	tests/contract/test_media_content_api.py	/tmp/framenest-media-content-api.sqlite3
1	tests/contract/test_media_content_api.py	framenest
1	tests/contract/test_media_import_api.py	/tmp/framenest-media-import-api.sqlite3
1	tests/contract/test_media_metadata_api.py	/tmp/framenest-media-metadata-api.sqlite3
2	tests/contract/test_media_metadata_repository.py	framenest-media-suggestion-result-v1
2	tests/contract/test_media_metadata_repository.py	framenest-media-suggestion-v4
1	tests/contract/test_media_suggestion_api.py	/tmp/framenest-media-suggestion-api.sqlite3
1	tests/contract/test_metadata_field_contract_parity.py	FrameNest
2	tests/contract/test_nuc_operator_runbook.py	./framenest
1	tests/contract/test_nuc_operator_runbook.py	/opt/framenest/current
1	tests/contract/test_nuc_operator_runbook.py	FRAMENEST_ENV_FILE
1	tests/contract/test_nuc_release_docs.py	FRAMENEST_
1	tests/contract/test_nuc_release_docs.py	FRAMENEST_ENV_FILE
2	tests/contract/test_nuc_release_docs.py	deploy/ubuntu/framenest-release
1	tests/contract/test_nuc_release_docs.py	deploy/ubuntu/framenest_release.py
1	tests/contract/test_nuc_release_docs.py	framenest
1	tests/contract/test_nuc_release_docs.py	framenest-db
4	tests/contract/test_nuc_release_docs.py	framenest-release
1	tests/contract/test_nuc_release_docs.py	framenest_nuc_worker_gate.fish
2	tests/contract/test_nuc_release_docs.py	framenest_release.py
2	tests/contract/test_nuc_release_remote_contract.py	/etc/framenest/framenest.env
3	tests/contract/test_nuc_release_remote_contract.py	/opt/framenest/capture-current
1	tests/contract/test_nuc_release_remote_contract.py	/opt/framenest/current
1	tests/contract/test_nuc_release_remote_contract.py	/opt/framenest/releases
1	tests/contract/test_nuc_release_remote_contract.py	/opt/framenest/releases/abc
1	tests/contract/test_nuc_release_remote_contract.py	/run/framenest
1	tests/contract/test_nuc_release_remote_contract.py	/var/cache/framenest
1	tests/contract/test_nuc_release_remote_contract.py	/var/lib/framenest
1	tests/contract/test_nuc_release_remote_contract.py	framenest
1	tests/contract/test_nuc_release_remote_contract.py	framenest.service
1	tests/contract/test_nuc_release_source_contract.py	framenest-0.1.0.dist-info
1	tests/contract/test_nuc_release_source_contract.py	framenest.pth
2	tests/contract/test_operator_infosec_scripts.py	FRAMENEST_
1	tests/contract/test_operator_infosec_scripts.py	FRAMENEST_LOG_SINCE
2	tests/contract/test_operator_infosec_scripts.py	FRAMENEST_LOG_UNIT
2	tests/contract/test_operator_infosec_scripts.py	FRAMENEST_PUBLIC_BASE_URL
2	tests/contract/test_operator_infosec_scripts.py	FRAMENEST_SOCKET_PATHS
2	tests/contract/test_operator_infosec_scripts.py	framenest
1	tests/contract/test_operator_infosec_scripts.py	framenest_log_triage.sh
1	tests/contract/test_operator_infosec_scripts.py	framenest_public_surface_check.sh
1	tests/contract/test_operator_infosec_scripts.py	framenest_socket_permissions_check.sh
4	tests/contract/test_operator_network_scripts.py	FRAMENEST_
1	tests/contract/test_operator_network_scripts.py	FRAMENEST_NETWORK_TEST_CURL
1	tests/contract/test_operator_network_scripts.py	FRAMENEST_NETWORK_TEST_MULLVAD
1	tests/contract/test_operator_network_scripts.py	FRAMENEST_NETWORK_TEST_SSH
4	tests/contract/test_operator_network_scripts.py	FRAMENEST_NETWORK_TEST_TAILSCALE
2	tests/contract/test_operator_network_scripts.py	FRAMENEST_NUC_SSH_COMMAND
2	tests/contract/test_operator_network_scripts.py	FRAMENEST_NUC_SSH_IDENTITY
2	tests/contract/test_operator_network_scripts.py	FRAMENEST_NUC_SSH_TARGET
2	tests/contract/test_operator_network_scripts.py	FRAMENEST_NUC_SSH_USER
4	tests/contract/test_operator_network_scripts.py	framenest_mullvad_egress.sh
1	tests/contract/test_ordinary_upload_ownership_boundary.py	framenest.sock
1	tests/contract/test_persistence_cli.py	FrameNest
1	tests/contract/test_persistence_cli.py	test_framenest_db_failure_output_is_sanitized_and_stable
1	tests/contract/test_persistence_cli.py	test_framenest_db_migrate_upgrades_to_head_with_deterministic_output
1	tests/contract/test_persistence_cli.py	test_framenest_db_status_dispatch_does_not_bind_socket
1	tests/contract/test_persistence_cli.py	test_framenest_db_status_reports_uninitialized_without_creating_database
1	tests/contract/test_persistence_cli.py	test_framenest_db_status_starts_no_listener_or_child_process
1	tests/contract/test_persistence_cli.py	test_framenest_server_startup_does_not_apply_migrations
1	tests/contract/test_persistence_package_resources.py	FrameNest
1	tests/contract/test_previews_console_script.py	FrameNest
1	tests/contract/test_public_published_uds.py	/tmp/framenest-public-audience-tcp.sqlite3
2	tests/contract/test_requester_private_youtube_details.py	FrameNest
1	tests/contract/test_research_provider_contract.py	framenest.
1	tests/contract/test_server_process_output.py	FrameNest
2	tests/contract/test_sidecar_cli.py	clip.mp4.framenest.json
1	tests/contract/test_tailscale_ingress_security.py	FrameNest
4	tests/contract/test_tailscale_ingress_security.py	framenest.sock
1	tests/contract/test_team_alias_api.py	framenest.sock
1	tests/contract/test_uvicorn_logging.py	test_config_uses_framenest_formatter_and_redaction_filter
1	tests/contract/test_uvicorn_logging.py	test_create_server_passes_framenest_log_config
1	tests/contract/test_uvicorn_runtime.py	framenest
2	tests/contract/test_uvicorn_runtime.py	framenest.sock
1	tests/contract/test_web_package_resources.py	FrameNest
2	tests/contract/test_worker_execution_contract.py	framenest_nuc_worker_gate.fish
1	tests/contract/test_x_companion_api.py	framenest.sock
1	tests/gallery_filter_controls.test.js	FrameNest-owned
3	tests/gallery_filter_controls.test.js	framenest.catalog.pageSize
1	tests/integration/persistence/test_analysis_run_history_migration.py	framenest-media-suggestion-result-v1
2	tests/integration/persistence/test_analysis_run_history_migration.py	framenest-media-suggestion-v3
2	tests/integration/persistence/test_companion_review_migration.py	framenest-media-suggestion-result-v1
2	tests/integration/persistence/test_companion_review_migration.py	framenest-media-suggestion-v3
1	tests/integration/persistence/test_kronika_record_repository.py	framenest-media-suggestion-result-v1
1	tests/integration/persistence/test_populated_0015_upgrade_to_0017.py	framenest-media-suggestion-result-v1
1	tests/integration/persistence/test_populated_0015_upgrade_to_0017.py	framenest-media-suggestion-v3
1	tests/integration/test_development_launcher.py	FrameNest
1	tests/integration/test_local_web_media_metadata.py	framenest-media-suggestion-result-v1
1	tests/integration/test_local_web_media_metadata.py	framenest-media-suggestion-v3
1	tests/integration/test_local_web_media_playback.py	framenest
1	tests/integration/test_persistence_migrations.py	broken_framenest_migrations
1	tests/integration/test_persistence_migrations.py	missing_framenest_migrations
1	tests/integration/test_still_image_vertical_slice.py	FrameNest
2	tests/kronika_ui.test.js	X-FrameNest-Request
1	tests/kronika_ui.test.js	framenestJSONHeaders
1	tests/kronika_ui.test.js	framenestMutationHeaders
1	tests/research_settings_admin_frontend.test.js	framenestMutationHeaders
1	tests/support/metadata_field_contract_cases.json	FrameNest
1	tests/support/x_fake_demo.py	FrameNest
1	tests/support/youtube_fake_demo.py	framenest-youtube-demo-loopback
1	tests/support/youtube_fake_demo.py	framenest-youtube-fake-demo-
1	tests/tailscale_identity_frontend.test.js	FrameNest
9	tests/tailscale_identity_frontend.test.js	X-FrameNest-Request
6	tests/tailscale_identity_frontend.test.js	framenestMutationHeaders
1	tests/unit/application/test_media_analysis_lifecycle.py	framenest-media-suggestion-result-v1
2	tests/unit/application/test_media_analysis_lifecycle.py	framenest-media-suggestion-v3
1	tests/unit/application/test_media_content_application.py	framenest
2	tests/unit/application/test_media_sidecar.py	/tmp/clip.mp4.framenest.json
2	tests/unit/application/test_upload_validation_coordinator.py	framenest-upload-validation
1	tests/unit/chatgpt_page/test_bridge_security.py	//chatgpt.com/g/g-p-framenest-analysis
2	tests/unit/chatgpt_page/test_projects.py	/var/lib/framenest/chatgpt-page
1	tests/unit/chatgpt_page/test_projects.py	test_development_default_uses_framenest_state_name
1	tests/unit/domain/__init__.py	FrameNest
4	tests/unit/domain/test_identities.py	framenest.example
1	tests/unit/domain/test_identities.py	test_validation_error_is_sanitized_and_framenest_owned
1	tests/unit/domain/test_media_sidecar.py	framenest-media-sidecar
1	tests/unit/infrastructure/ai/chatgpt_page/test_budget.py	/var/lib/framenest/chatgpt-page/budget.json
1	tests/unit/infrastructure/ai/test_credentials.py	FRAMENEST_AI_GATEWAY_API_KEY
3	tests/unit/infrastructure/backup/test_catalog_backup.py	.framenest-backup-
3	tests/unit/infrastructure/backup/test_catalog_backup_offdevice.py	framenest-catalog-offdevice
1	tests/unit/infrastructure/backup/test_catalog_backup_workstation.py	framenest_backups
2	tests/unit/infrastructure/filesystem/test_media_sidecar_store.py	.framenest-sidecar.
1	tests/unit/infrastructure/filesystem/test_media_sidecar_store.py	.framenest-sidecar.deadbeefdeadbeef.tmp
1	tests/unit/infrastructure/filesystem/test_media_sidecar_store.py	clip.mp4.framenest.json
2	tests/unit/infrastructure/media_analysis/test_movie_contact_sheet_selection.py	framenest-contact-
1	tests/unit/infrastructure/media_analysis/test_process.py	/nonexistent/framenest-media-tool
1	tests/unit/infrastructure/media_analysis/test_process.py	/nonexistent/framenest-tool
1	tests/unit/infrastructure/persistence/test_companion_review_repository.py	framenest-media-suggestion-result-v1
1	tests/unit/infrastructure/persistence/test_companion_review_repository.py	framenest-media-suggestion-v3
4	tests/unit/infrastructure/persistence/test_companion_review_repository.py	framenest-media-suggestion-v4
1	tests/unit/infrastructure/persistence/test_companion_review_repository.py	framenest-movie-identification-prompt-v2
3	tests/unit/infrastructure/persistence/test_media_analysis_run_repository.py	framenest-media-suggestion-result-v1
5	tests/unit/infrastructure/persistence/test_media_analysis_run_repository.py	framenest-media-suggestion-v3
1	tests/unit/infrastructure/runtime/test_development_runtime.py	FRAMENEST_PORT
1	tests/unit/infrastructure/runtime/test_production_health.py	framenest.sock
2	tests/unit/test_configuration.py	FRAMENEST_ENV_VARS
2	tests/unit/test_configuration.py	FrameNest
1	tests/unit/test_configuration.py	isolate_framenest_env
2	tests/unit/test_configuration_env_file.py	FRAMENEST_ENV_VARS
1	tests/unit/test_configuration_env_file.py	FrameNest
1	tests/unit/test_configuration_env_file.py	isolate_framenest_env
2	tests/unit/test_configuration_ingress.py	/run/framenest/framenest-public.sock
14	tests/unit/test_configuration_ingress.py	/run/framenest/framenest.sock
1	tests/unit/test_configuration_ingress.py	framenest.sock
1	tests/unit/test_configuration_ingress.py	relative/framenest.sock
1	tests/unit/test_gallery_preview.py	/tmp/framenest-test.sqlite3
1	tests/unit/test_identity_env.py	FRAMENEST_
1	tests/unit/test_identity_env.py	FRAMENEST_PORT
1	tests/unit/test_identity_env.py	Framenest_Port
4	tests/unit/test_identity_env.py	framenest_port
1	tests/unit/test_import_boundaries.py	FrameNest
1	tests/unit/test_persistence_boundaries.py	test_framenest_persistence_error_strings_are_sanitized
1	tests/unit/test_persistence_engine.py	FrameNest
1	tests/unit/test_previews_cli.py	/tmp/framenest-cli-previews
1	tests/unit/test_previews_cli.py	/tmp/framenest-cli.sqlite3
1	tests/unit/test_runtime_settings_store.py	FRAMENEST_RUNTIME_SETTINGS_PATH
1	tests/unit/test_server_runtime.py	framenest.sock
1	tests/unit/test_server_runtime.py	test_create_server_passes_framenest_log_config_and_disables_access_log
1	tests/unit/test_server_runtime.py	test_framenest_host_and_port_overrides_propagate
1	tests/unit/test_server_runtime.py	test_uvicorn_host_and_port_env_vars_do_not_override_framenest_settings
1	tests/unit/test_structured_logging.py	FrameNest
2	tests/unit/test_structured_logging.py	framenest.test
1	tests/unit/test_structured_logging.py	framenest_sanitized_payload
1	tests/unit/test_structured_logging.py	framenest_structured_payload
1	tests/unit/test_structured_logging.py	test_complete_framenest_settings_objects_are_not_traversed_or_exposed
1	tests/upload_cockpit_async_ownership.test.js	framenest-test
1	tests/upload_cockpit_async_ownership.test.js	framenest.upload.recovery.v1
1	tests/workspace_media_frontend.test.js	/framenestMutationHeaders/
2	tests/x_companion_extension.test.js	.frameNestOrigin/
1	tests/x_companion_extension.test.js	/FrameNest/
3	tests/x_companion_extension.test.js	/FrameNest/i
1	tests/x_companion_extension.test.js	/framenest-save-live/
6	tests/x_companion_extension.test.js	FrameNest
1	tests/x_companion_extension.test.js	FrameNest/
1	tests/x_companion_extension.test.js	data-framenest-
7	tests/x_companion_extension.test.js	frameNestOrigin
3	tests/x_companion_extension.test.js	framenest-media.bin
1	tests/youtube_acquisition_cockpit.test.js	X-FrameNest-Request
1	tests/youtube_acquisition_cockpit.test.js	framenest.youtube.currentClaim.v1
2	tests/youtube_acquisition_cockpit.test.js	framenestMutationHeaders
1	tests/youtube_request_cockpit.test.js	framenestMutationHeaders
```

## 4. Measured retention re-pin

Before the pin edit, `tests/contract/test_kronika_identity_retention.py` was 1 failed, 14 passed. The only failure was `test_capitalized_framenest_occurrence_counts_match`: `assert 2328 == 2327`. File counts, content paths, per-tree occurrences, environment tokens, the mutation header, host paths, unit accounts, console scripts, Part A, and Part B did not fail.

Independent count of `FrameNest`, ledger excluded: HEAD 2327, worktree 2328. The only added spelling outside the ledger is the new ROADMAP class-residue sentence. `ROADMAP.md` already contained one capitalized spelling, so the file count stays 343. Arithmetic: 2327+1=2328. The worktree pin is `CAPITALIZED_OCCURRENCE_COUNT = 2328`. After that edit the retention module passed, 15 passed in the combined 47-pass run below.

## 5. Suites

Focused run through `ap exec --operation test-focus` against baseline `9b291e936e93026ebe540b4a23a11b89721747a8`: 47 passed in 1.53s. That run was the retention module, `tests/contract/test_nuc_release_docs.py`, `tests/contract/test_adr_0073.py::test_current_schema_head_is_0035`, `tests/contract/test_team_alias_api.py::test_schema_head_sentences_are_0035`, and the sidecar reader test. No baseline difference inside that set.

The full Python suite, the JavaScript suites, and the bounded glob were not run. The unclassified gate stopped the commit before that proof.

## 6. Diff, commit, Part A, Part B, Part C

No commit. `git diff --stat`:

```text
 DEVELOPMENT.md                                    | 8 ++++----
 README.md                                         | 4 ++--
 ROADMAP.md                                        | 3 ++-
 tests/contract/test_kronika_identity_retention.py | 7 ++++++-
 4 files changed, 14 insertions(+), 8 deletions(-)
```

Part A is byte-unmoved: the retention module's frozen-hash tests passed and none of those paths are in the diff. Part B is still empty: the basename test passed. Part C movement in the worktree is the capitalized occurrence scalar only, 2327 to 2328, caused by the one new `FrameNest` in `ROADMAP.md`.

## 7. Sites no test exercises

No test asserts the new DEVELOPMENT launcher-default paragraph, the README public-main clause, or the ROADMAP exclusion wording. The retention counter notices the extra capitalized spelling and does not check the sentence. The sidecar reader test exercises the suffix, not the README sentence.

## 8. Deviations, risks, missing evidence, smallest next step

Deviation: the authorized commit was not created because an unclassified hit stops it. The worktree is dirty on the four paths above. This grant does not include `git restore` or `git checkout`, so the edits were left in place.

Risk: the granted categories do not own the sidecar suffix, the mutation header, durable non-marker artifact names, or ADR-0085's product-name sentences. Committing a "complete classification" would require a category this prompt does not give.

Missing evidence: full Python suite and the JavaScript suites.

Smallest next step: decide whether to extend the category list so the 808 hits have an owner, then authorize one commit of these four paths, or authorize restoring the worktree.

Resolved Execution Issues / Near-Misses

One forbidden `python3` process was started and only printed a skip line. It did not import the project, run tests, or change files. Later evidence used `git grep`, Perl, and `./.ap/ap exec`.

Pre-Existing Failure Classification

none

Orchestration critique:
MEASURED: the granted category list leaves 808 case-insensitive hits unclassified, including the sidecar suffix the same prompt says to keep; evidence is the scan total 3375 against the owned-category sum; effect is that this commit is stopped; smallest correction is one Orchestrator decision that names the missing owners.
LEAD: none