# Kronika one product — S4-A: provider-neutral research contracts and configuration v3

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 27
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S4-A-RESEARCH-CONTRACTS
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: extending the shared non-secret AI configuration schema while preserving backward compatibility for existing media provider settings; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository baseline from Step 0 before mutation.
Implementation authority is bounded to the exact allowlist below. The real
research provider stays disabled: no adapter, no network, no credentials
beyond a non-secret credential identifier. No subagents.

## Starting state (verified read-only at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `72009c3b525b6a46e87223cb9a143b5079d89cbf` (parent
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, tree
  `ba4b9290f0c986ac9cec6c3acec49ba747bf9b70`, subject
  `docs(kronika): define modular research and administrator-curated timeline`);
  clean index and worktree; local `main` = `origin/main` =
  `fd277a9…`; the S4-D documentation commit is accepted but not yet published.
- AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- `AI_CONFIG_SCHEMA_VERSION` is currently `2`; the AI configuration storage
  contract test asserts version 2 and currently rejects version 3.
- Accepted inputs: the S4-D documentation (ADR-0083 and updated owners) and
  the accepted modular-provider plan; the architecture, provider IDs, budgets,
  limits and typed outcomes recorded there.
- `private/**` is never read; no token, credential or profile access.

## Goal

Add the pure provider-neutral research contracts, the application ports, the
research provider registry/descriptors, and the non-secret research
configuration under AI configuration schema version 3, with v1/v2 backward
compatibility, disabled by default, and a deterministic fake provider for
tests. No real adapter, no network, no credential material, no API/UI.

## Exact mutation allowlist (baseline `72009c3…`)

```text
src/framenest/domain/research.py
src/framenest/application/ports/research.py
src/framenest/infrastructure/ai/configuration.py
src/framenest/infrastructure/ai/research_configuration.py
src/framenest/infrastructure/ai/research_registry.py
tests/unit/infrastructure/ai/test_ai_configuration_storage.py
tests/unit/infrastructure/ai/test_research_registry.py
tests/contract/test_research_provider_contract.py
```

No other path may change. If an additional path is genuinely required, stop
and report instead of expanding the allowlist.

## Required content

### 1. Domain values — `src/framenest/domain/research.py`

Pure, framework-free values (the existing import-boundary test scans the
domain tree, so no SQLAlchemy/FastAPI/pydantic/capture imports):

- Operation kinds: `search`, `research`.
- Lifecycle states and terminal classes matching the accepted lifecycle
  (`admitted`, `submitting`, `running`, `validating`, `saved`, `refused`,
  `failed`, `incomplete`, `cancel_requested`, `cancelled`, `timeout`,
  `submission_unknown`) plus the separate remote-cleanup and accounting
  states.
- `ProviderDescriptor`: stable provider ID, adapter/configuration version,
  `search`/`research` capabilities, execution location, native-research
  support, cancellation/retrieval/remote-deletion support, retention posture,
  accounting capabilities, submission-idempotency statement (including an
  explicit not-guaranteed value), and availability
  (`disabled`, `parked`, `unconfigured`, `configured`); configuration is not
  proof of live readiness.
- `ProviderRequest`: bounded prompt, operation kind, opaque operation ID,
  server-selected profile, deadline, approved resource limits. It carries no
  owner identity and no client-supplied endpoint/model/tool fields.
- `ProviderObservation`: the outcome classes with a complete result carrying
  full answer text/Markdown, citations, completion evidence, usage and an
  opaque remote handle; no trusted HTML.
- Usage/budget value types suitable for integer micro-USD arithmetic.
- The stable sanitized typed-error codes recorded in the accepted plan
  (`E_DISABLED`, `E_NOT_CONFIGURED`, `E_CAPABILITY_UNAVAILABLE`,
  `E_INVALID_REQUEST`, `E_BUSY`, `E_IDEMPOTENCY_CONFLICT`, `E_AUTH`,
  `E_RATE_LIMIT`, `E_PROVIDER_QUOTA`, `E_PROVIDER_UNAVAILABLE`, `E_REFUSED`,
  `E_INVALID_RESULT`, `E_INCOMPLETE_RESULT`, `E_RESULT_TOO_LARGE`,
  `E_NO_WEB_EVIDENCE`, `E_TIMEOUT`, `E_CANCELLED`, `E_SUBMISSION_UNKNOWN`,
  `E_RESULT_EXPIRED`, `E_ACCOUNTING_UNKNOWN`, `E_BUDGET_EXCEEDED`,
  `E_STORAGE`). No raw provider text is part of any error value.

### 2. Application ports — `src/framenest/application/ports/research.py`

Protocols only, importing only domain values:

- `ResearchProvider` with `describe()`, `submit()`, `poll()`, `cancel()`,
  `release_remote()`.
- Request repository, budget ledger and atomic result-completion ports.

No HTTP, SQLAlchemy, SDK, capture or infrastructure imports (the existing
import-boundary test scans the application tree).

### 3. Research registry and descriptors — `src/framenest/infrastructure/ai/research_registry.py`

- Provider IDs: `openai-responses` (selected first provider; descriptor
  present but `unconfigured`/disabled until a later slice implements its
  adapter), `chatgpt-page` (parked descriptor; unavailable for new
  Search/Research work), and a documented extension point for a future
  self-hosted provider.
- Selection is server-controlled and snapshotted at admission; an active
  request never changes provider or model because configuration changed.
  No dynamic plugin imports; no client-supplied endpoint/model/tool fields;
  no automatic fallback.
- A deterministic fake provider used only by tests (define it in the contract
  test file or the new research-registry test; no production fake).

### 4. Configuration schema v3 — `configuration.py` + `research_configuration.py`

- `AI_CONFIG_SCHEMA_VERSION = 3`; accepted versions `{1, 2, 3}`. Reading
  version 1 or 2 files must remain unchanged and lossless; saving writes
  version 3 and preserves existing media provider selection and provider
  records exactly.
- Optional `research` section, absent meaning disabled. Non-secret fields
  only: `enabled` (default false), provider ID, fixed model identifier,
  reasoning effort, tool allowlist, `max_tool_calls`, `max_output_tokens`,
  background flag, deadlines, per-operation budget reservations, daily and
  monthly budget thresholds, prompt/response/answer/citation bounds, timeout
  and poll values, and the credential identifier name only. No secret value
  may be stored; validation rejects unknown or malformed fields and
  out-of-range values.
- Future unknown schema versions remain rejected.

### 5. Tests

- `tests/unit/infrastructure/ai/test_ai_configuration_storage.py`: update the
  current version-2 assumptions to version 3; keep and extend v1/v2 read
  compatibility; v3 round-trip; absent `research` = disabled; malformed and
  unknown-version rejection (including 999); saving preserves media settings.
- `tests/unit/infrastructure/ai/test_research_registry.py`: descriptor and
  capability mapping; parked provider unavailable; unknown provider rejected;
  selection snapshot is stable across a configuration change; no fallback.
- `tests/contract/test_research_provider_contract.py`: the fake provider
  exercises every port method and outcome class; typed error codes are stable;
  the port/registry surface exposes no endpoint/model/tool input from
  clients; domain/ports import boundaries hold.
- Do not weaken or delete existing assertions; extend them.

## Step 0 — preconditions (fail closed)

- Verify physical root, branch, HEAD, parent, tree, clean index and worktree,
  local `main` = `origin/main` = `fd277a9…`, public `refs/heads/main` via
  `git ls-remote`, and the AP pin `7478ddb0…` (gitlink and `.ap` HEAD).
- Confirm `AI_CONFIG_SCHEMA_VERSION == 2` and that no research module exists
  yet. Classify divergence with RF-12; stop on unexplained remainder.

## Declared execution route

From the repository root with the exact baseline:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 72009c3b525b6a46e87223cb9a143b5079d89cbf

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 72009c3b525b6a46e87223cb9a143b5079d89cbf --operation test-focus -- tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py tests/contract/test_ai_server_composition.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_research_provider_contract.py -q -p no:cacheprovider
```

JavaScript tests: not-used — no JavaScript change. No ambient Python or
substitute route.

Validation ladder: selected.
Inspection and provenance: required.
Existing focused tests: `tests/unit/infrastructure/ai/test_ai_configuration_storage.py`, `tests/unit/infrastructure/ai/test_registry.py`.
Affected tests: the declared selection above.
New causal regression: the new contract and registry tests — the baseline has
no research contracts, no registry and no schema v3, so they fail before the
change.
Broad or full suite: not-used.
Runtime or testbed: not-used.
Independent acceptance: not-required for this implementation; a separate
focused acceptance follows because a shared configuration schema changes.

## Git and commit rules

Stage only the eight allowlisted paths after reviewing the complete diff and
`git diff --cached --check`. Verify the complete baseline-to-HEAD diff is
exactly those paths. Create exactly one local commit:

```text
feat(kronika): add provider-neutral research contracts and configuration
```

Do not push, fetch, tag, merge or rebase. Do not touch `.ap`, the managed
block, `docs/AP_UPGRADE_OBSERVATIONS.md`, `pyproject.toml`, `poetry.lock` or
any migration. Do not commit Meta artifacts.

## Authority and containment

Positive authority: read-only repository inspection; edits to exactly the
eight allowed paths; the declared route commands; one local commit; the
terminal report write at the exact destination below when absent; full
readback of the saved report.

Negative authority: no real provider adapter, provider call, network use,
credential material, account action or endpoint configuration beyond the
non-secret schema; no API/UI/endpoint implementation; no schema migration,
database, dependency, packaging or configuration-state change; no host, SSH,
gate, sudo, service or browser action; no `private/**`; no push,
publication or deployment; no subagents; no ambient execution route.

## Stopping conditions

Stop and report on: baseline or topology drift; an unexpected extra required
path; an unusable declared route; a failing test that cannot be fixed inside
the allowlist; an existing research module or schema-v3 artifact; a need for
network, credentials or host action; or any instruction conflict. Preserve
the first causal failure; do not improvise.

## Completion and report contract

`PASS` means the eight-path change is committed with the declared route
passing, v1/v2 compatibility preserved, research disabled by default, and the
worktree clean. `PARTIAL`/`BLOCKED` otherwise. Use
`Phase-qualified result: implementation-PASS` for PASS, otherwise
`not-applicable`, and `Logical-whole closure: not-closed`. `Report
justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the exact
changed paths; the domain/port/registry/config contents; the compatibility
evidence for v1/v2; the route results with counts; the commit SHA, parent,
tree and subject; post-commit status; unchanged AP pin, managed block and
ledger; deviations, risks and missing evidence; one smallest next step (a
focused independent acceptance of the contracts and configuration, then S6);
authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; the short completion notice to the
Cooperator is in Slovak, masculine address. Finalize the report, save it at
the exact destination, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion
notice with status, path and SHA-256. Do not run `sudo -v` or `sudo -K`.
Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 27_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 27_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
