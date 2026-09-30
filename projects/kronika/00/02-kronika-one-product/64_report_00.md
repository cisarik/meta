### Report for ORCHESTRATOR_CHAT

# S9-R implementation — administrator settings and versioned pricing

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 64
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S9-R-IMPLEMENT
Delivery route: manual Cooperator delivery
Evidence posture: non-independent implementation
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-mutation
Escalation disposition: none
Start commit: 3bf424586289b500cf45cb0d49676b50d27328fa
End commit: e8f1c04b289b7bd694d66edba012d288ee41e610
```

PASS. The frozen S9-R slice is implemented inside the 44-path allowlist, the
focused route exits 0, and one local commit exists. Implementation evidence is
non-independent; a fresh independent audit follows separately.

## 1. Entry gate and baseline

| Gate | Observed result |
|---|---|
| Repository root | `/Users/agile/Projects/framenest` |
| Branch | `feat/kronika-one-product` |
| Baseline / parent | `3bf424586289b500cf45cb0d49676b50d27328fa` |
| AP gitlink checkout | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Plan artifact SHA-256 | `971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325` (matches) |
| Entry worktree | Clean including untracked files |

## 2. Implemented behavior (plan §§2–8)

- **Catalog** — new immutable `research_models.py` with exactly four confirmed
  entries (`gpt-5.5-2026-04-23` default, `gpt-5.6-sol`, `gpt-5.6-terra`,
  `gpt-5.6-luna`), the exact short/long/cache-write rates, threshold `272,000`,
  web search `10,000,000` µ$/thousand for every entry and tier, and Sol
  `valid_until` `2026-11-22T00:00:00Z`. The three fixed-model equality checks
  were replaced; unknown/alias models fail before persistence, reservation or
  provider contact; there is no network model discovery.
- **Accounting** — `ResearchUsage.cache_write_input_tokens`,
  `ResearchAnswer.usage` optional, `UsageTokenPrices` and the extended
  `UsagePriceSchedule` (cache-write rate, long threshold, long tier), per-component
  ceil integer math, `R + W ≤ I` and `reasoning ≤ O` validation. New admissions
  use `configuration_version = "s9r-20260930"` and tuple-resolved append-only
  schedules; legacy `"3"` keeps the 2026-09-26 flat schedule; old checkpoints
  remain readable; unknown accounting and overruns fail closed without clamping.
- **Runtime** — a persistent coordinator is built whenever the catalog engine
  exists (including disabled start); admission and capabilities read a fresh
  validated configuration; configuration selection/admission serialize against
  writes; disabling preserves history, polling, cancellation and cleanup;
  re-enabling needs no restart.
- **Idempotency** — `(owner, client_request_id)` lookup precedes configuration,
  enablement and credential checks; version-2 fingerprint over owner, kind,
  prompt and consent only; identical replay returns the original attempt (202)
  even after model/budget/enablement changes; changed content conflicts; the
  admission receipt distinguishes new admissions; atomic `ADMITTED → SUBMITTING`
  claim with one winner.
- **Shared configuration** — `load_ai_server_config_snapshot` (SHA-256 of
  bounded raw bytes, absent = `"absent"`), per-path process lock plus sibling OS
  advisory lock (`fcntl`/`msvcrt`), compare-and-set, creation-only direct writes,
  `If-Match` HTTP writers with 409 on stale revisions, ETag delivery, and CLI
  saves that capture and honour revisions. Preservation assertion implemented and
  tested.
- **Admin API** — `GET`/`PUT /api/admin/ai/research-settings` with verified
  identity plus `provider.operate`, workspace composition only, explicit ingress
  policies, privileged audit action `ai.research.settings.update`, six required
  PUT fields with the exact bounds, the required GET/PUT response shape, `no-store`,
  the stable error table, no secrets/probes, absent-config refusal, and
  missing-credential disabled edits without enabling.
- **Metadata** — authorized summaries/details gained safe `provider_id`,
  `model_id`, `configuration_version`, `accounting_state`.
- **Shell** — a Research settings section inside the existing administrator AI
  dialog with the exact copy, independent section state, model/budget
  confirmation, stale-revision handling, identity-loss clearing, accessible
  labels/status, and no framework or Gallery/Details restyle.
- **Documentation** — new `docs/adr/0084-...md` (dated 2026-09-30), an ADR-0083
  partial-supersession notice and index entry, and SPEC/SERVER/AGENTS/README/
  PRODUCT/ROADMAP reconciliation.

## 3. Changed files (staged and committed, exactly the allowlist)

Implementation (17): `domain/research.py`, `application/ports/research.py`,
`application/research.py`, `infrastructure/ai/configuration.py`,
`infrastructure/ai/research_configuration.py`,
`infrastructure/ai/research_registry.py`,
`infrastructure/ai/openai_responses.py`,
`infrastructure/persistence/research_request_repository.py`,
`infrastructure/persistence/research_budget_repository.py`,
`adapters/api/ai_admin_api.py`, `adapters/api/application.py`,
`adapters/api/research_api.py`, `adapters/api/tailscale_ingress.py`,
`adapters/cli/ai.py`, `adapters/api/web/{index.html,app.js,styles.css}`.

Tests (7 edited): `test_ai_configuration_storage.py`,
`test_research_coordinator.py`, `test_ai_cli.py`, `test_research_completion.py`,
`test_research_provider_contract.py`, `test_research_request_repository.py`
(new claim test). Documentation (9).

New paths (5): `infrastructure/ai/research_models.py`,
`tests/unit/infrastructure/ai/test_research_models.py`,
`tests/contract/test_research_settings_api.py`,
`tests/research_settings_admin_frontend.test.js`,
`docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md`.

The two compatibility files (`tests/unit/infrastructure/ai/test_registry.py`,
`tests/contract/test_ai_server_composition.py`) were read-only test inputs and
were not edited.

## 4. Validation evidence

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa
=> ap project check --baseline: PASS

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa --operation test-focus -- \
  tests/unit/infrastructure/ai/test_ai_configuration_storage.py \
  tests/unit/infrastructure/ai/test_research_registry.py \
  tests/unit/infrastructure/ai/test_openai_responses_adapter.py \
  tests/unit/infrastructure/ai/test_research_models.py \
  tests/unit/infrastructure/ai/test_registry.py \
  tests/unit/application/test_research_coordinator.py \
  tests/unit/adapters/cli/test_ai_cli.py \
  tests/contract/test_ai_provider_admin_api.py \
  tests/contract/test_ai_server_composition.py \
  tests/contract/test_research_settings_api.py \
  tests/contract/test_research_requests_api.py \
  tests/contract/test_research_provider_contract.py \
  tests/contract/test_research_completion.py \
  tests/contract/test_kronika_access_inventory.py \
  tests/integration/persistence/test_research_request_repository.py \
  -q -p no:cacheprovider
=> 373 passed

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js
=> tests 29 / pass 29 / fail 0

git diff --check
=> clean
```

Causal regressions added: catalog membership/alias refusal/Sol cutoff and the
arithmetic fixtures (Luna short `22,990`, Luna long `127,000`, threshold
`272,000`/`272,001`) in `test_research_models.py`; strict usage parsing and
submit-404 distinction in `test_openai_responses_adapter.py`; atomic submission
claim in `test_research_request_repository.py`; accounting blocker, admission
guard, disabled submission and content replay in `test_research_coordinator.py`;
CAS/no-op/preservation in `test_ai_configuration_storage.py`; stale interactive
save in `test_ai_cli.py`; the settings API security/concurrency contract in
`test_research_settings_api.py`; and USD conversion/confirmation/stale-revision
shell contracts in the new JS test.

The access inventory was regenerated and inspected;
`docs/KRONIKA_ACCESS_INVENTORY.md` now lists both
`GET`/`PUT /api/admin/ai/research-settings` rows under the existing
provider-administration exclusion.

## 5. Commit result (local only)

```text
commit:  e8f1c04b289b7bd694d66edba012d288ee41e610
tree:    1cbf6739083e7459b1d5e5011dbd72fed77e5d69
parent:  3bf424586289b500cf45cb0d49676b50d27328fa
subject: feat(research): add administrator settings and versioned pricing
```

No push, merge, rebase, reset, branch change, NUC access, provider call or
credential inspection occurred.

## 6. Deviations and residual notes

- **Media-provider `If-Match` is optional, not required.** Revision and strong
  ETag delivery were added to the media-provider read and mutation responses,
  and a stale/`malformed`/wildcard `If-Match` returns 409 without writing.
  Because `tests/contract/test_ai_provider_admin_api.py` is an allowlisted but
  intentionally unchanged compatibility input that sends no `If-Match`, an
  absent header keeps the prior unconditional behavior. The new
  research-settings PUT requires `If-Match`. This is the smallest deviation that
  satisfies both the plan and the compatibility contract.
- **Sol-cutoff guard placement.** Expiry is enforced at admission
  (`admission_guard`, using the injected clock and deadline) and at PUT
  enabling, rather than in `select_research_provider`, to keep the frozen
  selection signature `{config, kind}`.
- **Legacy over-threshold accounting.** The resolved legacy `"3"` schedule keeps
  the 2026-09-26 flat short rates and has no long tier, so an unfinished legacy
  request above `272,000` input tokens resolves to unknown accounting rather than
  a fabricated value, matching plan §3.
- `FIXED_OPENAI_RESPONSES_MODEL_ID` remains defined as the historical default
  identifier for compatibility; production selection now uses the catalog.
- Rendered/browser acceptance was not performed (forbidden). The shell is
  covered by the Node behavior tests only.

## 7. Smallest next step

Issue the fresh independent audit grant against
`e8f1c04b289b7bd694d66edba012d288ee41e610`: one fresh Worker reviews this exact
candidate, re-runs the focused route, and verifies the accounting, replay,
concurrency and authorization claims. Publication, NUC refresh and rendered/live
acceptance are separate authorities.

## 8. Critique

- **MEASURED:** all 44 allowlisted paths are present; no path outside the
  allowlist was touched; the focused route is green after the commit.
- **MEASURED:** the plan's central correctness risks (versioned pricing,
  shared-configuration CAS, atomic claim, replay semantics) have causal
  regressions, not just smoke coverage.
- **LEAD:** the media-provider `If-Match` optionality is the one place where the
  frozen plan and an unchanged compatibility test meet; the fresh audit should
  confirm the chosen resolution is acceptable or request a bounded amendment.

```text
External trace disposition: configured
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Prompt filename: 64_implementation_00.md
Report filename: 64_report_00.md
Destination: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Git publication owner: COOPERATOR
```

**Authority expiry:** this terminal report ends `kronika-one-product` session 64,
exchange 01. Implementation authority expires. Publication, NUC refresh and
rendered/live acceptance remain separate.
