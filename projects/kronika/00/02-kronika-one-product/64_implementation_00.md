# S9-R Implementation Grant — Administrator-managed research settings and versioned pricing (kronika-one-product, session 64)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 64
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S9-R-IMPLEMENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: versioned pricing/accounting math, shared configuration CAS across writers, atomic submission claim, replay/idempotency semantics
Recommended context capacity: approximately 1M tokens
Independence required: no

## Implementation authority record

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 3bf424586289b500cf45cb0d49676b50d27328fa
Changed-path allowlist: the exact 44 paths in "Exact allowlist" below
Implementation boundaries: the positive and negative authority in this grant
Independence required: no
```

## Frozen authoritative specification

Implement frozen sections 2–8 of
`/Users/agile/meta/projects/kronika/00/02-kronika-one-product/62_report_01.md`
(SHA-256 `971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325`;
status PARTIAL applied only to its original file delivery — the Cooperator
persisted the complete report and the plan is frozen; the Cooperator confirmed
the four-model allowlist in-session). Read the full plan before editing. Its
section 10 proposal is superseded by this grant, which is the sole execution
authority.

## Binding highlights (the plan owns the detail)

- **Catalog**: new immutable model/price catalog in
  `src/framenest/infrastructure/ai/research_models.py` with exactly the four
  confirmed entries (`gpt-5.5-2026-04-23` default, `gpt-5.6-sol`,
  `gpt-5.6-terra`, `gpt-5.6-luna`), the exact short/long/cache-write rates from
  plan §2, threshold `272,000` input tokens, web search `10,000,000` µ$ per
  thousand for every entry and tier, and Sol `valid_until`
  `2026-11-22T00:00:00Z` with a new-admission cutoff guard. Replace the three
  fixed-model equality checks; unknown/alias models fail before persistence,
  reservation or provider contact; no network model discovery.
- **Accounting**: extend the domain values exactly as plan §3 (usage
  cache-write tokens, optional usage, extended schedule with long-context
  value, per-component ceil integer math, validation `R + W ≤ I` and
  `reasoning ≤ O`); new admissions use `configuration_version = "s9r-20260930"`
  with tuple-resolved append-only schedules; legacy `"3"` requests keep the
  2026-09-26 flat schedule; old checkpoints stay readable; restart resolves
  pricing from the persisted request identity; unknown accounting and
  reservation overruns fail closed without clamping or erasing output.
- **Runtime**: build the persistent coordinator whenever the catalog engine
  exists (including disabled start); read fresh validated configuration per
  admission and capabilities request; serialize configuration selection and
  durable admission against configuration writes; disabling preserves
  history, polling, cancellation and cleanup; re-enabling needs no restart.
- **Idempotency**: lookup `(owner, client_request_id)` before configuration,
  enablement and credential checks; version-2 fingerprint over owner, kind,
  prompt and consent only; identical replay returns the original attempt (202)
  even after model/budget/enablement changes; changed content conflicts; the
  admission receipt distinguishes new admissions; add the atomic
  `ADMITTED -> SUBMITTING` claim so only one winner issues provider creation.
- **Shared configuration**: snapshot revisions (SHA-256 of bounded raw bytes;
  absent = `"absent"`), per-path process lock plus sibling OS advisory lock
  (POSIX `fcntl`; Windows `msvcrt`), compare-and-set semantics, creation-only
  direct writes, `If-Match`-based HTTP writers with 409 on stale revisions,
  revision/ETag delivery to existing media-provider read/mutation surfaces and
  their shell callers, CLI interactive saves capture and honour revisions.
  Preservation assertion exactly as plan §4 (normalized non-research values
  survive research saves and vice versa; not byte-for-byte formatting).
- **Admin API**: exact routes
  `GET/PUT /api/admin/ai/research-settings`; verified identity plus
  `provider.operate`; workspace composition only; explicit policies plus
  privileged audit action `ai.research.settings.update`; six required PUT
  fields with the exact validation bounds from plan §4; GET/PUT response
  shapes (revision, `configuration_present`, settings, `credential_available`,
  catalog with pricing/pinning/`valid_until`, limits); `no-store`; the exact
  stable error table; no secrets, provider contact or probe; absent server AI
  configuration refuses PUT; missing credentials allow disabled edits but not
  enabling.
- **API metadata**: authorized request summaries/details gain safe
  `provider_id`, `model_id`, `configuration_version`, `accounting_state`.
- **Shell**: a Research settings section inside the existing administrator AI
  dialog with the exact copy, independent media/research section state,
  confirmation for model/budget changes, stale-revision and uncertain-save
  handling, identity-loss clearing, accessible labels/status and the existing
  dialog conventions; no framework, no Gallery/Details/player restyle.
- **Documentation**: new
  `docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md`
  (dated 2026-09-30), an ADR-0083 partial-supersession notice and index entry,
  the SPEC/SERVER/AGENTS deltas and the README/PRODUCT/ROADMAP reconciliation
  from plan §7; keep historical wording historical; do not claim NUC or
  publication facts the plan does not supply.
- **Tests**: implement the causal regressions of plan §8 in the allowlisted
  test files, including the arithmetic fixtures (Luna short `22,990`, Luna
  long `127,000`, threshold 272,000/272,001) and the 16 proof areas; use fake
  providers, fake credentials and temporary fixtures only.

## Exact allowlist (44 paths; no additions or wildcards)

Existing implementation paths (17):

```text
src/framenest/domain/research.py
src/framenest/application/ports/research.py
src/framenest/application/research.py
src/framenest/infrastructure/ai/configuration.py
src/framenest/infrastructure/ai/research_configuration.py
src/framenest/infrastructure/ai/research_registry.py
src/framenest/infrastructure/ai/openai_responses.py
src/framenest/infrastructure/persistence/research_request_repository.py
src/framenest/infrastructure/persistence/research_budget_repository.py
src/framenest/adapters/api/ai_admin_api.py
src/framenest/adapters/api/application.py
src/framenest/adapters/api/research_api.py
src/framenest/adapters/api/tailscale_ingress.py
src/framenest/adapters/cli/ai.py
src/framenest/adapters/api/web/index.html
src/framenest/adapters/api/web/app.js
src/framenest/adapters/api/web/styles.css
```

Existing test paths (13):

```text
tests/unit/infrastructure/ai/test_ai_configuration_storage.py
tests/unit/infrastructure/ai/test_research_registry.py
tests/unit/infrastructure/ai/test_openai_responses_adapter.py
tests/unit/application/test_research_coordinator.py
tests/unit/adapters/cli/test_ai_cli.py
tests/contract/test_ai_provider_admin_api.py
tests/contract/test_research_requests_api.py
tests/contract/test_research_provider_contract.py
tests/contract/test_research_completion.py
tests/contract/test_kronika_access_inventory.py
tests/integration/persistence/test_research_request_repository.py
tests/ai_providers_admin_frontend.test.js
tests/kronika_ui.test.js
```

Existing documentation paths (9):

```text
AGENTS.md
README.md
PRODUCT.md
SPEC.md
SERVER.md
ROADMAP.md
docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md
docs/adr/README.md
docs/KRONIKA_ACCESS_INVENTORY.md
```

New paths (5; the only new files):

```text
src/framenest/infrastructure/ai/research_models.py
tests/unit/infrastructure/ai/test_research_models.py
tests/contract/test_research_settings_api.py
tests/research_settings_admin_frontend.test.js
docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md
```

No dependency, lockfile, database schema, migration, AP, capture or
deployment-script change. AI configuration stays schema version 3; the
database stays `0035`. Any required change outside this list is a stop: report
it and wait for an amended grant.

## Positive authority

Edit exactly the allowlisted paths; create only the five new files; use fake
providers/credentials and temporary test fixtures; run the validation route
below; regenerate and inspect the allowlisted access inventory; inspect
diffs; explicitly stage accepted allowlisted paths; create one local commit.

## Negative authority

No push/publication, merge, rebase, reset, clean, stash, force operation or
branch change; no `git add .`/`-A`; no NUC/SSH/sudo; no provider call or real
credential/configuration inspection; no browser run; no private media; no
dependencies, migrations, AP or managed-block changes; no capture work; no
subagents; no unrelated cleanup.

## Validation (focused route; run once at closeout, narrower reruns only)

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa --operation test-focus -- tests/unit/infrastructure/ai/test_ai_configuration_storage.py tests/unit/infrastructure/ai/test_research_registry.py tests/unit/infrastructure/ai/test_openai_responses_adapter.py tests/unit/infrastructure/ai/test_research_models.py tests/unit/infrastructure/ai/test_registry.py tests/unit/application/test_research_coordinator.py tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_ai_server_composition.py tests/contract/test_research_settings_api.py tests/contract/test_research_requests_api.py tests/contract/test_research_provider_contract.py tests/contract/test_research_completion.py tests/contract/test_kronika_access_inventory.py tests/integration/persistence/test_research_request_repository.py -q -p no:cacheprovider

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js

git diff --check
```

No broad suite; no browser evidence suite; no live service. The two
compatibility files (`test_registry.py`, `test_ai_server_composition.py`) are
read-only test inputs, not edit targets.

## Git authority

Stage only the allowlisted paths by exact path after reviewing the full staged
diff. Create exactly one local commit:

```text
feat(research): add administrator settings and versioned pricing
```

No push. Report the commit SHA, tree and parent.

## Delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 64_implementation_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 64_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on baseline drift, out-of-allowlist need, client Plan
mode being active, a gate conflict, unresolved accounting/model mapping, or a
required failure exceeding the allowlist. Do not waive failing required checks
or invent fallback behavior. Report the exact blocker and smallest next
decision.

## Completion and report contract

PASS means: the frozen slice is implemented inside the allowlist; the focused
route exits 0 with the required causal regressions Red-then-Green where
applicable; the regenerated inventory is included; one local commit with the
exact subject exists; the report is delivered. Implementation evidence is
non-independent; a fresh independent audit follows separately.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 64, 01), and carries the compact core
with exact commands and evidence, changed files, commit result (local only),
deviations, smallest next step, `Report justification: new-mutation`,
critique, and authority expiry. Save the report exactly at
`64_report_00.md` if the client permits; read back the full content;
otherwise preserve it in chat and mark delivery PARTIAL.

Authority expiry: the terminal report, cancellation or supersession ends this
grant; publication, NUC refresh and rendered/live acceptance remain separate.
