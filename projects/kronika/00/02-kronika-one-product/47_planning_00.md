# KRONIKA-ONE-PRODUCT-S4-B-PLAN — frozen implementation plan for the native provider runtime (autonomy mode)

## Identity and route

Persistent role identity: ORCHESTRATOR (planning and execution under the
Cooperator's 2026-09-28 autonomy directive)
Logical whole identity: kronika-one-product
Worker session ordinal: 47
Worker exchange ordinal: 01
Phase: planning (implementation plan freeze)
Task identity: KRONIKA-ONE-PRODUCT-S4-B-PLAN

## Basis

Accepted architecture: `25_report_00.md` (modular research providers and the
administrator-curated Timeline; sections 2–4 own the provider boundary,
lifecycle, runtime, recovery and accounting). Roadmap row S4-B: native
provider runtime — OpenAI adapter, migration `0035`, durable jobs, budgets,
cancellation, cleanup, credential deployment source; fake transport only;
disabled by default. The S4-A surface already exists: `domain/research.py`
(values, lifecycle, budget/completion values, pricing math),
`application/ports/research.py` (provider, request repository, budget ledger,
result completion), `infrastructure/ai/research_registry.py` (descriptors and
server-side selection), `research_configuration.py` (schema v3), the contract
test `tests/contract/test_research_provider_contract.py`.

## Scope of S4-B

In scope: durable request/accounting/slot state (migration `0035`), SQLite
repositories for the ports, the application coordinator (admission,
idempotency, single active slot, submission, polling, cancellation, remote
cleanup, accounting reconciliation, startup recovery), the OpenAI Responses
adapter against an injectable transport (no network in tests), a credential
deployment source, and inert-by-default composition wiring.

Out of scope: HTTP endpoints and forms (S7-P/S8), document rendering (S7-P),
Timeline/approval integration changes (S7-P), live provider calls, real
credentials, capture paths, UI, and any migration beyond `0035`.

## Migration `0035_research_requests_and_accounting.py`

Descends from `0034`; mirrors S6 conventions (bounded names, CHECKs, named
indexes, populated-downgrade refusal before DDL, no backfill).

1. `research_requests` — one row per admitted request:
   `operation_id` PK (bounded token), `owner_login_key`, `client_request_id`,
   `request_fingerprint` (sha256 hex), `kind` in (`search`,`research`),
   `prompt_text`, `prompt_utf8_bytes`, `lifecycle_state` (domain states),
   `provider_id`, `model_id`, `configuration_version`, `reasoning_effort`,
   `max_tool_calls`, `max_output_tokens`, `deadline_seconds`,
   `reservation_micro_usd`, `remote_handle_json`, `checkpoint_json`,
   `checkpoint_sha256`, `record_id` (nullable FK `kronika_records.id`, unique
   when not null), `error_code`, `cancel_requested_at_ms`,
   `cancellation_confirmed_at_ms`, `cleanup_state`, `accounting_state`,
   `admitted_at_ms`, `submitted_at_ms`, `finished_at_ms`, `created_at_ms`,
   `updated_at_ms`; unique `(owner_login_key, client_request_id)`; indexes on
   lifecycle state and updated time.
2. `research_active_slot` — single-row table (`id` PK CHECK `id = 1`),
   `operation_id` nullable, `held_since_ms` nullable; the coordinator owns the
   slot through atomic transactions.
3. `research_operations` — accounting attempts:
   `operation_row_id` PK (uuid), `request_id` FK, `parent_operation_id`
   nullable, `purpose` in (`search`,`research`,`synthetic_acceptance`),
   `operation` in (`create`,`poll`,`cancel`,`delete`), `attempt_number`,
   `started_at_ms`, `finished_at_ms`, `terminal_classification`,
   `remote_handle_reference`, `transport_outcome`, `reserved_usd_micros`,
   `input_tokens`, `cached_input_tokens`, `output_tokens`,
   `reasoning_tokens_as_subset`, `web_tool_calls`,
   `calculated_cost_usd_micros`, `accounting_state` in
   (`reserved`,`reconciled`,`unknown`), `cleanup_state`, `cancellation_state`.
4. `research_budget_holds` — one row per request:
   `operation_id` PK/FK, `day_key` (UTC `YYYY-MM-DD`), `month_key` (UTC
   `YYYY-MM`), `reserved_usd_micros`, `accounted_usd_micros` nullable, `state`
   in (`reserved`,`reconciled`,`unknown`), `created_at_ms`,
   `reconciled_at_ms`; indexes on `(day_key)`, `(month_key)`, `(state)`.
   Daily/monthly consumption derives from holds; a missing usage record is
   never stored as zero.

## Modules and composition

- `src/framenest/application/research.py` — `ResearchCoordinator`: admit
  (validate, fingerprint, reserve, persist, acquire slot, submit outside any
  DB transaction), poll-once/poll-loop, cancel (asynchronous, acknowledged
  before the remote call), reconcile accounting, remote cleanup after local
  completion, startup recovery (persisted handle resumes polling;
  `E_SUBMISSION_UNKNOWN` when a crash precedes a confirmed handle). One
  generation attempt per request; no automatic resubmission; retry only
  polling/cleanup at 1/2/4 s with at most three consecutive failures; kill
  switch blocks admission; `E_BUSY` for a second submission; duplicate client
  submission returns the existing request; a different fingerprint returns
  `E_IDEMPOTENCY_CONFLICT`.
- `src/framenest/infrastructure/persistence/research_request_repository.py` —
  SQLite implementation of the request repository plus atomic admission and
  slot handling (`BEGIN IMMEDIATE`).
- `src/framenest/infrastructure/persistence/research_budget_repository.py` —
  SQLite ledger: reserve/reconcile against daily and monthly thresholds
  atomically; integer micro-USD arithmetic from `domain/research.py`.
- `src/framenest/infrastructure/ai/openai_responses.py` — adapter implementing
  the provider port against an injectable transport protocol; `describe()` is
  network-free; submit/poll/cancel/release map to bounded transport calls;
  parsing enforces the domain byte/token/citation limits; typed error mapping
  only; the concrete HTTPS transport is constructed only when wired.
- `src/framenest/adapters/api/application.py` — lifespan wiring: when the
  research configuration is enabled and selectable, construct repositories,
  ledger, adapter and coordinator; otherwise remain inert. Startup performs no
  network call and never requires a credential; an absent research section
  must not block ordinary startup.
- `src/framenest/infrastructure/persistence/catalog_schema.py` — mirror the
  `0035` tables per convention.
- `deploy/systemd/framenest-research-credential.conf` — credential deployment
  source drop-in:
  `LoadCredential=KRONIKA_RESEARCH_OPENAI_API_KEY:/etc/framenest/credentials/research-openai`;
  documented as provisioned-deployment-only in
  `docs/UBUNTU_NUC_DEPLOYMENT.md`.

## Exact path allowlist

```text
src/framenest/domain/research.py
src/framenest/application/ports/research.py
src/framenest/application/research.py
src/framenest/infrastructure/ai/openai_responses.py
src/framenest/infrastructure/ai/transport.py
src/framenest/infrastructure/ai/research_registry.py
src/framenest/infrastructure/ai/research_configuration.py
src/framenest/infrastructure/ai/credentials.py
src/framenest/infrastructure/persistence/research_request_repository.py
src/framenest/infrastructure/persistence/research_budget_repository.py
src/framenest/infrastructure/persistence/alembic_environment/versions/0035_research_requests_and_accounting.py
src/framenest/infrastructure/persistence/catalog_schema.py
src/framenest/adapters/api/application.py
deploy/systemd/framenest-research-credential.conf
docs/UBUNTU_NUC_DEPLOYMENT.md
tests/unit/application/test_research_coordinator.py
tests/unit/infrastructure/ai/test_openai_responses_adapter.py
tests/integration/persistence/test_research_requests_migration.py
tests/integration/persistence/test_research_request_repository.py
tests/contract/test_research_provider_contract.py
```

No other path may change. A required edit outside this list is a stop; the
plan is amended in the trace before the edit, not silently.

## Test matrix

- Domain/ports: existing `tests/contract/test_research_provider_contract.py`
  stays green; adapter conformance added against the fake transport.
- Coordinator units (fake provider/clock/repositories): admission and
  idempotency; single active slot and `E_BUSY`; budget reserve, reconciliation,
  unknown usage; cancellation acknowledgment and confirmation; cleanup after
  save; recovery from persisted handle; `E_SUBMISSION_UNKNOWN`; no resubmission
  after a create failure.
- Adapter units (fake transport): outcome mapping, bounds enforcement, typed
  errors, network-free `describe()`, disabled/not-configured behavior.
- Persistence integration: `0034` -> `0035` upgrade preserves rows and creates
  no requests; populated downgrade refuses before DDL; repositories admit/save/
  get; concurrent reservations serialize under `BEGIN IMMEDIATE`; budget sums
  per UTC day/month.
- Startup: an absent or disabled research configuration leaves ordinary
  startup unchanged and performs no network I/O.

## Validation and evidence

Targeted only; no full suite (testing economy binding). Declared route with
the current baseline `3f5dc5c469e19802aa3411988aa022b158de2ab6`, focused files
from the matrix above. Implementation evidence tier E2, non-independent under
the autonomy directive; the Cooperator may request a fresh independent audit
of any part later.

## Stops

Out-of-allowlist edit; any live provider call or credential value handling;
any schema change beyond `0035`; weakening of fail-closed or budget rules;
network access at import or startup; unexplained failing gate; client mode
blocking writes.

## Next step

Implement in bounded commits on `feat/kronika-one-product`: (1) migration
`0035` + schema mirror + migration tests; (2) repositories + tests; (3)
coordinator + tests; (4) adapter + tests; (5) composition wiring + credential
source + docs; then targeted validation and the trace report `48_report_00.md`.

## Allowlist amendment 1 (recorded during implementation step 1)

The migration-head ripple to `0035` additionally requires current-head
assertion updates (never historical targets or unrelated canned values) in:

```text
tests/contract/test_persistence_cli.py
tests/integration/persistence/test_analysis_proposal_migration.py
tests/integration/persistence/test_companion_review_migration.py
tests/integration/persistence/test_content_publication_migration.py
tests/integration/persistence/test_device_registry_migration.py
tests/integration/persistence/test_kronika_records_migration.py
tests/integration/persistence/test_library_registry_migration.py
tests/integration/persistence/test_media_catalog_migration.py
tests/integration/persistence/test_media_cover_migration.py
tests/integration/persistence/test_media_metadata_migration.py
tests/integration/persistence/test_media_user_alias_overlay_migration.py
tests/integration/persistence/test_populated_0015_upgrade_to_0017.py
tests/integration/persistence/test_upload_publication_migration.py
tests/integration/persistence/test_upload_session_migration.py
tests/integration/persistence/test_x_requested_category_migration.py
tests/integration/persistence/test_x_requester_acquisition_migration.py
tests/integration/test_persistence_migrations.py
tests/integration/test_process_sigterm_lifecycle.py
tests/unit/infrastructure/backup/test_catalog_backup.py
tests/unit/infrastructure/runtime/test_production_runtime.py
```

Recorded facts from step 1:

- Refused downgrades are atomic: after a populated-downgrade refusal the
  database remains at the starting head `0035`; the S6 test's assertion was
  advanced accordingly (`test_populated_downgrade_refuses_without_dropping_rows`
  keeps its row-retention evidence).
- `test_upload_session_migration`'s post-head expected table union gained the
  four `0035` tables.
- Pre-existing macOS debt observed and not repaired:
  `tests/integration/test_process_sigterm_lifecycle.py` hardcodes
  `/home/agile/Projects/framenest/.venv/bin/python` and fails on the MacBook
  before reaching any assertion (ledger candidate).
- Step 1 result: commit `df44c2d` (23 paths, +1253/-36); targeted affected set
  `198 passed` (the sigterm test excluded as the pre-existing macOS debt).
