### Report for ORCHESTRATOR_CHAT

# S9-R — Frozen administrator research-settings plan

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 62
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S9-R-REVISION
Delivery route: manual Cooperator delivery
Evidence posture: non-independent planning
Status: PARTIAL — file delivery only; technical plan complete
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Escalation disposition: none
Start commit: 3bf424586289b500cf45cb0d49676b50d27328fa
End commit: 3bf424586289b500cf45cb0d49676b50d27328fa
```

The S9-R plan is frozen. The Cooperator confirmed the recommended four-model allowlist during this exchange. The bounded documentation check resolved the cache-write usage field. No product decision remains unanswered.

This report is delivered as one Markdown artifact in the session. Active client Plan Mode prohibits filesystem writes, so `62_report_01.md` was not created, read back or hashed. `PARTIAL` applies only to that delivery limitation. No implementation is authorized.

## 1. Planning record and verified baseline

### Planning Record — unchanged

```text
Planning cycle: targeted-revision
Prior planning report: 62_report_00.md (kronika-one-product 62/01)
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: the administrator-selectable model allowlist and the
  required UsagePriceSchedule shape (long-context tier and cache-write
  dimensions) grounded by the new external evidence in 63_report_00.md
Preserved unaffected decisions: no client-supplied model/endpoint/tool fields;
  no automatic fallback; provider/model snapshotted at admission and never
  changed mid-request; research disabled by default; private/family/administrator
  access rules; accepted budgets and limits; one generation attempt per request;
  capture parked; no new framework; testing economy
Automatic targeted revisions used: 1
```

### Plan-to-Execution fields — unchanged

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: freeze the S9-R administrator research-settings plan grounded in 62_report_00.md and 63_report_00.md
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

| Gate | Observed result |
|---|---|
| Repository | `/Users/agile/Projects/framenest` |
| Remote | `https://github.com/cisarik/framenest.git` |
| Branch | `feat/kronika-one-product` |
| HEAD | `3bf424586289b500cf45cb0d49676b50d27328fa` |
| Parent | `a3687505eb12359c76f85661e51e36d7e4778fc9` |
| AP gitlink and checkout | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Repository and AP trees | Clean, including untracked files |
| Proposed existing paths | All 39 verified at HEAD |
| Proposed new paths | All five verified absent |
| Intended report destination | Absent at final check |

The nine findings in [62_report_00.md](/Users/agile/meta/projects/kronika/00/02-kronika-one-product/62_report_00.md) remain binding. This plan addresses fixed-model validation, expanded pricing, runtime refresh, request-specific accounting, replay semantics, shared-file concurrency, verified administrator identity, accepted budget ceilings and documentation supersession.

Model and pricing evidence comes from [63_report_00.md](/Users/agile/meta/projects/kronika/00/02-kronika-one-product/63_report_00.md), retrieved on 2026-09-30.

The accepted S8 rendered outcome, completed S9 provider work, cleanup correction acceptance, publication and NUC refresh are supplied trace evidence. This Worker did not independently observe public refs or the NUC. Schema `0035` is the supplied deployed baseline.

## 2. Confirmed model choice and pricing

### Single Cooperator product choice

**Recommended and confirmed:** allow these four exact identifiers, retain `gpt-5.5-2026-04-23` as the default, and offer `gpt-5.6-luna` as the cheapest documented compatible option.

The answer recorded in-session was **“Štyri modely (Recommended)”**.

| Exact identifier | Purpose and pinning |
|---|---|
| `gpt-5.5-2026-04-23` | Default; dated snapshot |
| `gpt-5.6-terra` | Recommended balanced, lower-cost alternative; undated identifier |
| `gpt-5.6-luna` | Lowest-cost option; undated identifier; no claim of equivalent answer quality |
| `gpt-5.6-sol` | Flagship alternative; undated identifier; promotional-price expiry guard |

Use provider ID `openai-responses`. Do not admit aliases such as `gpt-5.5` or `gpt-5.6`, arbitrary model strings, `gpt-5.5-pro`, or the unselected `gpt-5.4` alternative.

Create one immutable catalog in `infrastructure/ai/research_models.py`, consumed by configuration validation, selection, pricing resolution and administrator presentation. Replace all three fixed-model equality checks identified in report 62/01. Preserve identifier syntax validation and then require exact catalog membership.

Unknown models fail before configuration persistence, reservation or provider contact. Provider-side unavailability fails that attempt without fallback. Distinguish model refusal during creation from an expired remote result during polling; a submission 404 must not masquerade as a missing historical response.

Configuration changes never discover models from the network. Historical catalog entries remain available for accounting even if subsequently unavailable for new selection.

### Frozen schedule entries

All figures below are integer micro-USD per million tokens. The web-search rate is **10,000,000 micro-USD per thousand calls** for every entry and tier.

| Model | Short input | Short cached read | Short cache write | Short output |
|---|---:|---:|---:|---:|
| `gpt-5.5-2026-04-23` | 5,000,000 | 500,000 | 5,000,000 | 30,000,000 |
| `gpt-5.6-sol` | 4,000,000 | 400,000 | 5,000,000 | 20,000,000 |
| `gpt-5.6-terra` | 2,000,000 | 200,000 | 2,500,000 | 12,000,000 |
| `gpt-5.6-luna` | 200,000 | 20,000 | 250,000 | 1,200,000 |

| Model | Long input | Long cached read | Long cache write | Long output |
|---|---:|---:|---:|---:|
| `gpt-5.5-2026-04-23` | 10,000,000 | 1,000,000 | 10,000,000 | 45,000,000 |
| `gpt-5.6-sol` | 8,000,000 | 800,000 | 10,000,000 | 30,000,000 |
| `gpt-5.6-terra` | 4,000,000 | 400,000 | 5,000,000 | 18,000,000 |
| `gpt-5.6-luna` | 400,000 | 40,000 | 500,000 | 1,800,000 |

Short pricing applies through **272,000 input tokens inclusive**. Above that boundary, apply long pricing to the entire request. A GPT-5.5 cache write has the ordinary input rate; the table does not introduce an additional charge.

The pricing basis is standard processing at the existing global endpoint. Regional uplift, Priority/Flex/Batch pricing and negotiated account rates are outside these entries. Confirm the applicable account billing basis before live acceptance.

For Sol, set `valid_until` to `2026-11-22T00:00:00Z`. Refuse new admissions whose deadline could cross that cutoff until a separately reviewed schedule update extends or replaces it. The administrator catalog must explain the restriction. Expiry never rewrites admitted or historical pricing, chooses another model or prevents disabling research.

### Bounded documentation check

Retrieval date: **2026-09-30**.

Successful first-party retrievals:

- [Prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Responses create reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create)

The documented separate field is `usage.input_tokens_details.cache_write_tokens`; cached reads remain `cached_tokens`. Cache-write tokens are excluded from ordinary input and charged at their write rate. The 1.25 multiplier is the total write-token rate, not an additional 1.25 surcharge. [Prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching)

The attempted Python retrieve-reference URL returned an internal retrieval error and supplied no evidence:

`https://developers.openai.com/api/reference/python/resources/responses/methods/retrieve`

No account access, provider request or credential handling occurred.

## 3. Accounting shape, persistence and runtime behavior

### Domain and calculation

Extend the existing pure domain types:

- `ResearchUsage`: add `cache_write_input_tokens: int | None`.
- `ResearchAnswer.usage`: allow `None` when a complete answer lacks trustworthy accounting.
- `UsagePriceSchedule`: retain its four existing fields; add `cache_write_input_micro_usd_per_million`, `long_context_threshold_tokens` and `long_context`.
- `long_context`: an immutable `UsageTokenPrices` value containing input, cached-input, cache-write-input and output rates. Web-search pricing remains on the parent schedule.

The additional schedule fields may be absent only for explicitly supported legacy schedules. New catalog entries contain all dimensions and use threshold `272000`.

Let:

- `I` = total input tokens;
- `R` = cached-read input tokens;
- `W` = cache-write input tokens;
- `O` = total output tokens;
- `T` = validated web-search call count;
- `N = I − R − W`.

Select the tier using `I`, then calculate:

```text
cost_micro_usd =
    ceil(N × input_rate / 1,000,000)
  + ceil(R × cached_read_rate / 1,000,000)
  + ceil(W × cache_write_rate / 1,000,000)
  + ceil(O × output_rate / 1,000,000)
  + ceil(T × web_search_rate / 1,000)
```

Use integer arithmetic and existing per-component ceiling semantics. Reasoning tokens remain a subset of `O` and are never charged again.

Require genuine non-negative integers; reject booleans, negative values and inconsistent counts. Enforce `R + W ≤ I` when `W` is present and `reasoning_tokens ≤ O`.

Remove `_int_or_zero` from usage parsing. Missing or invalid required accounting values produce unknown accounting. Count tools from validated complete provider output; absence of trustworthy evidence is not a zero-call observation.

For GPT-5.6, missing `W` makes accounting unknown. For GPT-5.5, absent `W` is retained as absent, but cost remains derivable by charging `I − R` at the ordinary input rate because write and ordinary rates are equal. This does not fabricate a token count.

Required arithmetic fixtures:

| Case | Expected micro-USD |
|---|---:|
| Luna short: `I=10000, R=2000, W=3000, O=1000, T=2` | 22,990 |
| Luna long: `I=300000, R=100000, W=50000, O=10000, T=2` | 127,000 |
| `I=272000` | Short tier |
| `I=272001` | Long tier |

### Durable request-specific pricing

Do not add a database migration or price JSON column.

For new admissions, use profile `configuration_version = "s9r-20260930"`. This is independent of AI configuration schema version 3.

Resolve an immutable schedule from the persisted tuple:

```text
(provider_id, model_id, configuration_version)
```

For the four new combinations, that tuple resolves to the model’s `openai-standard-2026-09-30` schedule entry. Existing request columns already persist all three values. The coordinator receives a schedule resolver instead of one shared `_price_schedule`.

The mapping is append-only. Future price changes require a new configuration/profile version; they must not overwrite existing tuples.

Compatibility rules:

- Existing version `"3"` requests on `gpt-5.5-2026-04-23` retain the original 2026-09-26 schedule.
- An unfinished legacy request above 272,000 input tokens has unknown accounting because its original flat schedule does not cover that tier.
- Already reconciled historical charges are not recalculated.
- Unknown tuples fail accounting closed.
- Checkpoint serialization preserves the optional write count and optional usage. Old checkpoints remain readable under their legacy profile.
- Restart resolves pricing from persisted request identity, never the currently selected model.

### Unknown usage and threshold overrun

Keep lifecycle completion separate from accounting completion. A validated complete answer can remain saved while accounting is unknown; retain its owner visibility, record link and cleanup eligibility.

Preserve the reservation for unknown accounting. Preserve the full observed charge when it exceeds the reservation; do not clamp it.

Before further generation, fail closed on:

- unresolved unknown accounting;
- a terminal request whose hold is still reserved, including a crash between terminal persistence and reconciliation;
- a recorded operation cost above its reservation.

Use `E_ACCOUNTING_UNKNOWN` or `E_BUDGET_EXCEEDED` as appropriate. These conditions do not disappear at a day/month rollover. Operator reconciliation requires a separate bounded task; S9-R adds no reset, dismissal or budget-erasure control.

This implements the already accepted accounting rules in report 25. The monetary thresholds remain admission/accounting controls, not an absolute invoice guarantee.

### Runtime refresh and disabling

Build a persistent coordinator whenever the catalog engine is available, including when research starts disabled. Construction performs no credential provisioning or provider contact.

Wire one canonical configuration source into the administrator API, research capabilities and admission selection. Read a fresh validated configuration for each new admission and capabilities request. Do not replace the coordinator or rerun recovery when settings are saved.

Serialize configuration selection and durable admission against configuration writes using the shared configuration guard. Release the guard and database transaction before network I/O.

Disabling:

- prevents new admissions and new submission claims;
- preserves request history, saved answers and reservations;
- leaves polling, cancellation and remote cleanup available;
- leaves unsubmitted admitted requests on their original snapshot until re-enabled, cancelled or expired;
- does not undo a submission already claimed before the disabling save.

Re-enabling can therefore activate a process started disabled without restarting it. Existing requests keep their admitted provider, model, limits and pricing version.

Preserve both automatic cleanup nudge sites from the accepted correction and the existing bounded cleanup loop.

### Idempotency and one generation attempt

Look up `(owner, client_request_id)` before current configuration, enablement or credential checks.

For new requests, fingerprint a canonical version-2 object containing:

```text
fingerprint version, owner, kind, validated prompt, validated consent_version
```

Do not include provider, model, budgets, limits or settings revision. Use the existing prompt validation without introducing new normalization.

For legacy version-3 request rows, compare the persisted owner, kind and prompt. Do not invent a historical consent value that was never persisted.

An identical replay returns the original operation with status 202, including after model changes or disabling. Changed submission content returns `E_IDEMPOTENCY_CONFLICT`.

Return a `ResearchAdmissionReceipt(row, newly_admitted)` from coordinator admission. Only a newly admitted receipt can trigger the submission nudge. Resolve racing inserts using the repository’s existing unique owner/client-ID constraint.

Add an atomic repository claim from `ADMITTED` to `SUBMITTING`. Only its winner may issue provider creation. Concurrent detail nudges cannot submit twice; restart recovery never resubmits an uncertain creation.

## 4. Shared configuration and administrator API

### Shared-file concurrency

Use one concurrency contract for research settings, media-provider HTTP mutations and all four CLI configuration writers.

Add `load_ai_server_config_snapshot`, returning the validated configuration and a revision computed as SHA-256 of the same bounded raw bytes. Represent an absent file by revision `"absent"`.

Implement a per-canonical-path process lock plus a stable sibling OS advisory lock. Use standard-library platform support: `fcntl` on POSIX and a one-byte `msvcrt` lock on Windows. The lock file is private, is not removed after release, and rejects symlinks or non-regular objects. The OS releases its lock on process exit.

Under that guard:

1. Read the current snapshot.
2. Compare the expected revision.
3. Validate preconditions against that snapshot.
4. Apply the bounded mutation.
5. Write through the existing private atomic replacement path.

All production read-modify-write callers supply their observed revision. Direct `write_ai_server_config` calls without an expected revision are creation-only; replacing an existing file requires a revision.

A fresh no-op returns success without rewriting or advancing the revision. A stale request conflicts even if its proposed values happen to match. A real change advances `updated_at_ms` monotonically.

**Preservation assertion:** a research-only save preserves every supported, normalized non-research configuration value; a media-only save preserves the research subtree. JSON formatting, key order and `updated_at_ms` are not preserved byte-for-byte. Existing schema normalization and schema-1/2-to-3 serialization remain explicit compatibility behavior.

HTTP writers use one strong `If-Match` value. Reject missing/malformed values, wildcards and lists. A stale revision returns 409 without writing or automatically retrying.

Add revision and ETag delivery to the existing media-provider reads and mutation responses; update its shell callers. Interactive CLI configuration captures a revision before prompting and refuses a stale save after confirmation.

### Exact research routes

| Method and route | Behavior |
|---|---|
| `GET /api/admin/ai/research-settings` | Safe settings, catalog, bounds and revision; no provider probe |
| `PUT /api/admin/ai/research-settings` | Validate and atomically save the six accepted settings |

Both routes require a verified `IdentityContext` with a non-empty login and `provider.operate`. Loopback capability presentation alone is insufficient. Authorize before configuration or credential inspection.

Register both routes in workspace composition and the explicit ingress policy table. Keep them absent from public composition. PUT uses existing Origin and `X-FrameNest-Request` protection and a privileged audit action `ai.research.settings.update`, target type `research_settings`. An unavailable required audit record prevents mutation.

All successful and error responses use `Cache-Control: no-store`. Preserve the established sanitized error envelope.

### PUT body

All six fields are required; extra fields are forbidden:

```json
{
  "enabled": false,
  "model_id": "gpt-5.5-2026-04-23",
  "daily_budget_usd_micros": 10000000,
  "monthly_budget_usd_micros": 30000000,
  "search_budget_reservation_usd_micros": 500000,
  "research_budget_reservation_usd_micros": 5000000
}
```

| Field | Validation |
|---|---|
| `enabled` | Strict boolean |
| `model_id` | Valid identifier and exact selectable catalog entry |
| Daily budget | Strict integer, 1–10,000,000 |
| Monthly budget | Strict integer, 1–30,000,000 |
| Search reservation | Strict integer, 1–500,000 |
| Research reservation | Strict integer, 1–5,000,000 |

Daily budget must not exceed monthly budget. Preserve the current rule allowing a reservation above a configured remaining/daily budget; subsequent admission is then refused. Lowering budgets does not erase accumulated spending or modify existing reservations.

No provider, credential reference, secret, endpoint, tool, reasoning, concurrency or request-limit field is writable here.

A recognized expired model may remain in an unchanged selection while disabling research. It cannot be newly selected or enabled for new work.

### GET and successful PUT response

GET returns exactly these top-level fields:

- `revision`: unquoted revision value; response also supplies its strong `ETag`.
- `configuration_present`: whether the server AI configuration exists.
- `provider_id`: `openai-responses`.
- `settings`: the six-field object above.
- `credential_available`: boolean only.
- `models`: catalog entries containing `model_id`, `display_name`, `pinning`, `selectable`, `price_schedule_version`, `valid_until` and `pricing`.
- `limits`: minimum budget `1`, the four budget maxima, and the fixed operation limits.

`pinning` is `dated_snapshot` or `undated_identifier`. `valid_until` is the Sol cutoff or `null`. `pricing` serializes the extended schedule fields from section 3.

The fixed limits remain:

| Limit | Search | Research |
|---|---:|---:|
| Web tools | 3 | 20 |
| Output tokens | 4,096 | 32,768 |
| Deadline seconds | 180 | 1,800 |

Common limits remain prompt 16,384 bytes, provider response 8,388,608 bytes, answer 2,097,152 bytes and 200 citations. Concurrency remains one generation slot.

Successful PUT returns the same representation plus `changed: boolean`. It neither probes nor generates.

If the whole AI configuration is absent, GET returns disabled defaults with `configuration_present: false` without creating a file. PUT refuses until existing server AI configuration is set up. This avoids silently selecting a media provider as an incidental research-settings operation.

An existing media configuration without a research section can receive that section normally. Missing credentials permit disabled-settings edits but prevent enabling.

### Stable settings errors

| HTTP | Code | Copy |
|---:|---|---|
| 401 | `IDENTITY_REQUIRED` | “A verified identity is required.” |
| 403 | `CAPABILITY_DENIED` | “You do not have permission to manage research settings.” |
| 422 | `VALIDATION_FAILED` | “Request validation failed.” |
| 422 | `E_CAPABILITY_UNAVAILABLE` | “Choose a supported research model from the list.” |
| 409 | `AI_CONFIG_CONFLICT` | “AI settings changed. Reload and review before saving again.” |
| 409 | `AI_PROVIDER_BUSY` | “Another AI provider operation is already running.” |
| 503 | `AI_CONFIG_UNAVAILABLE` | “The AI provider configuration could not be read or saved.” |
| 503 | `AI_CONFIG_UNAVAILABLE` — absent file | “Set up the server AI configuration first, then reload Research settings.” |
| 503 | `E_NOT_CONFIGURED` — credential absent | “Research credentials are not configured on the server.” |
| 503 | `E_NOT_CONFIGURED` — expired pricing | “This model’s pricing must be reviewed before research can be enabled.” |

Existing ingress, mutation-protection and audit-failure errors remain unchanged. Never include configuration paths, credential identifiers, secrets or raw provider errors.

Add safe `provider_id`, `model_id`, `configuration_version` and `accounting_state` fields to authorized request summaries/details. They describe the admitted attempt and are not submission controls.

## 5. Shell behavior

Place a **Research settings** section inside the existing administrator AI dialog. Retain its dialog, focus, mutation-header and error conventions. Add no framework or Gallery/Details redesign.

The new section uses a stricter identity predicate than legacy media-provider administration: resolved verified identity, non-empty login, workspace audience and `provider.operate`. Public, anonymous and capability-only loopback contexts must not fetch it.

Provide the enable switch, four-model selector and four monetary inputs. Display USD with at most six fractional digits and convert decimal strings to integer micro-USD without floating-point rounding. Show model pricing, pinning and credential presence as read-only information.

Required copy:

> These server settings apply to new Search and Research requests. People submitting questions cannot choose a model, endpoint or tools.

Also explain:

> Changing the model does not change requests already admitted. Disabling pauses new generation; existing requests can still be checked or cancelled.

State that credentials are managed on the server and that configuration does not prove account access.

Maintain separate server snapshot, draft, revision, dirty, loading, saving, confirmation, error and response-generation state. Load media and research sections independently; one section’s failure must not erase the other’s draft.

A model change requires explicit confirmation showing the previous and next model and the resulting budgets. Cancelling confirmation sends no PUT. Editing after confirmation invalidates it.

During save, disable duplicate actions and expose busy/status feedback. On failure retain the draft. On 409 require explicit reload and review; do not silently rebase or resend. After an uncertain network outcome, read the server state before allowing another explicit save.

A successful media save invalidates the research revision and vice versa. A dirty sibling draft must not silently adopt a new revision.

On identity loss or dialog closure, abort or invalidate pending responses and clear protected state. Stale responses cannot reopen or repopulate the section. Confirm discarding a dirty draft; restore focus using existing dialog behavior. Use associated labels, keyboard operation, visible focus, accessible status/errors and existing minimum target sizes.

After a successful settings save, refresh capabilities and new-submission controls. Continue polling an existing request when research is disabled. Show its admitted model and any accounting warning while preserving the saved-answer link.

## 6. Exact implementation allowlist

Paths are relative to `/Users/agile/Projects/framenest`. **39 existing paths and five new paths; 44 total.** No other repository mutation is proposed.

### Existing implementation paths

| Path | Authorized purpose |
|---|---|
| `src/framenest/domain/research.py` | Usage, schedules, profile version and exact cost calculation |
| `src/framenest/application/ports/research.py` | Admission receipt and atomic submission-claim contract |
| `src/framenest/application/research.py` | Replay, dynamic admission, request pricing and fail-closed accounting |
| `src/framenest/infrastructure/ai/configuration.py` | Snapshot revisions, shared guard, CAS and atomic preservation |
| `src/framenest/infrastructure/ai/research_configuration.py` | Catalog validation and accepted settings bounds |
| `src/framenest/infrastructure/ai/research_registry.py` | Allowlisted immutable selection |
| `src/framenest/infrastructure/ai/openai_responses.py` | Strict usage parsing and contextual provider-error mapping |
| `src/framenest/infrastructure/persistence/research_request_repository.py` | Atomic claim and replay race handling |
| `src/framenest/infrastructure/persistence/research_budget_repository.py` | Unknown/overrun admission guards and retained true accounting |
| `src/framenest/adapters/api/ai_admin_api.py` | Settings routes, safe responses and shared writer revisions |
| `src/framenest/adapters/api/application.py` | Persistent runtime and canonical dynamic configuration wiring |
| `src/framenest/adapters/api/research_api.py` | Capabilities, consent forwarding, receipt handling and request metadata |
| `src/framenest/adapters/api/tailscale_ingress.py` | Explicit settings policies and privileged audit action |
| `src/framenest/adapters/cli/ai.py` | Shared CAS for configuration writers |
| `src/framenest/adapters/api/web/index.html` | Research settings controls and confirmation |
| `src/framenest/adapters/api/web/app.js` | Protected UI state, revisions, save flow and request presentation |
| `src/framenest/adapters/api/web/styles.css` | Scoped settings layout, errors and accessibility |

### Existing test paths

| Path | Coverage |
|---|---|
| `tests/unit/infrastructure/ai/test_ai_configuration_storage.py` | Lock/CAS, normalization and preservation |
| `tests/unit/infrastructure/ai/test_research_registry.py` | Exact model selection and immutable profiles |
| `tests/unit/infrastructure/ai/test_openai_responses_adapter.py` | Usage parsing and model refusal |
| `tests/unit/application/test_research_coordinator.py` | Refresh, restart, replay, accounting and generation claims |
| `tests/unit/adapters/cli/test_ai_cli.py` | CLI concurrency and stale interactive saves |
| `tests/contract/test_ai_provider_admin_api.py` | Existing media writer revision contract |
| `tests/contract/test_research_requests_api.py` | Replay, disable/re-enable and preserved cleanup |
| `tests/contract/test_research_provider_contract.py` | Model/request/accounting compatibility |
| `tests/contract/test_research_completion.py` | Saved output with unknown accounting and restart |
| `tests/contract/test_kronika_access_inventory.py` | New route policies, composition and inventory regeneration |
| `tests/integration/persistence/test_research_request_repository.py` | Durable snapshots, atomic claims and budget guards |
| `tests/ai_providers_admin_frontend.test.js` | Media/research revision coordination |
| `tests/kronika_ui.test.js` | Existing request polling and history behavior |

### Existing documentation paths

| Path | Purpose |
|---|---|
| `AGENTS.md` | Current model-selection boundary outside managed AP content |
| `README.md` | Shipped status and administrator settings overview |
| `PRODUCT.md` | Administrator-controlled server selection |
| `SPEC.md` | Normative API, bounds, pricing and immutable admission rules |
| `SERVER.md` | Refresh, persistence, writer concurrency and credential boundaries |
| `ROADMAP.md` | S8/S9 evidence and S9-R acceptance state |
| `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md` | Partial-supersession notice retaining historical decision |
| `docs/adr/README.md` | ADR-0084 index entry |
| `docs/KRONIKA_ACCESS_INVENTORY.md` | Regenerated route inventory |

### New paths

| Path | Purpose |
|---|---|
| `src/framenest/infrastructure/ai/research_models.py` | Immutable selectable/historical model and price catalog |
| `tests/unit/infrastructure/ai/test_research_models.py` | Catalog, tier, cache-write, expiry and legacy pricing |
| `tests/contract/test_research_settings_api.py` | Complete settings API/security/concurrency contract |
| `tests/research_settings_admin_frontend.test.js` | New settings state and accessibility contracts |
| `docs/adr/0084-administrator-managed-research-settings-and-versioned-pricing.md` | Accepted bounded supersession |

No dependency, lockfile, database schema, migration, AP file, capture module or operational deployment script change is required. AI configuration stays schema version 3; database schema stays `0035`.

## 7. Documentation supersession

Create ADR-0084 dated 2026-09-30. Record the confirmed four-model choice, unchanged default, undated-model limitation, exact schedule tables, Sol expiry policy, administrator controls and immutable request pricing.

ADR-0084 supersedes only ADR-0083’s fixed-model decision and the interpretation that every bounded administrator adjustment requires another architecture decision. It preserves the provider boundary, no fallback, submission restrictions, privacy/publication rules, capture parking, default-disabled behavior and accepted limits.

Add a partial-supersession notice and ADR-0084 link to ADR-0083. Keep its original fixed-model wording as historical decision text.

Promote these normative requirements into SPEC:

- Verified application administrators select a model only through server settings and the approved catalog.
- Search/Research submissions cannot select a provider, model, endpoint or tools.
- Admission persists an immutable provider/model/profile identity that determines later pricing.
- Configuration changes cannot reprice or regenerate an existing attempt.
- Fresh configuration is disabled; accepted monetary defaults are also upper bounds.
- Unknown accounting and threshold overruns block further generation pending reconciliation.

SERVER documents dynamic reads, disabled-start activation, durable schedule derivation, shared CAS and continued settlement/cleanup. AGENTS changes only project-owned text outside the managed AP block.

Reconcile README, PRODUCT and ROADMAP with the supplied S8/S9 evidence: accepted S8 shell, completed provider path, and verified/published cleanup correction. Identify S9-R implementation as awaiting its own audit, publication, NUC refresh and rendered acceptance until those occur. S10 follows; parked work remains parked.

Do not turn this documentation update into a general runbook cleanup or claim new NUC observations.

## 8. Focused validation

No tests were run in this planning exchange.

The implementation must establish these causal regressions:

| Area | Required proof |
|---|---|
| Catalog | Exactly four selectable IDs, pinned default, alias/unknown refusal and Sol cutoff |
| Arithmetic | Every rate entry, threshold boundary, cache partition, component rounding and no reasoning double count |
| Missing evidence | Missing/invalid usage never becomes zero; missing GPT-5.6 writes fail accounting closed |
| Refresh | A disabled-start process can enable; a saved model reaches the next admission without restart |
| Snapshot | A uses its admitted model and schedule after changing settings to B, including after restart |
| Replay | Same ID returns the original attempt after model, budget or enablement changes; changed content conflicts |
| Single attempt | Concurrent nudges produce exactly one atomic claim and one provider creation |
| Disable | No new submission claim; polling, cancellation, history and cleanup remain available |
| Accounting | Unknown, overrun and terminal/reserved crash-gap states block further generation without losing output |
| Concurrency | Research/research, research/media and research/CLI races cannot lose successful changes |
| Preservation | Supported non-research values survive research saves and vice versa |
| Authorization | Anonymous, ordinary-member and legacy loopback-only contexts cannot read/write settings |
| API | Strict fields/types/bounds, no secret exposure, no provider contact on GET/PUT, stable errors and ETags |
| UI | Confirmation, stale revisions/responses, identity loss, uncertain saves and exact USD conversion |
| Access inventory | Both routes have explicit policies, workspace-only registration and regenerated entries |
| Compatibility | Existing media configuration and accepted cleanup continue to work |

Use fake transports, fake credentials and temporary test configuration files. Do not inspect real configuration or secrets.

The access-inventory test writes the approved inventory document; inspect the generated diff rather than treating regeneration as proof of authorization correctness.

Run this exact aggregate route once at closeout, with narrower reruns only for changed or failing areas. The two additional compatibility files are read-only test inputs, not additions to the edit allowlist.

```fish
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa

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

node --test \
    tests/ai_providers_admin_frontend.test.js \
    tests/research_settings_admin_frontend.test.js \
    tests/kronika_ui.test.js

git diff --check
#------------------------------------------------------
```

Python execution remains through AP with the exact authorized baseline. No raw Python, environment reconstruction, browser suite or automatic broad-suite expansion is proposed.

## 9. Acceptance route

1. **Implementation validation:** pass the focused route, inspect containment and produce one local candidate commit.
2. **Fresh independent audit:** one fresh Worker reviews that exact candidate, verifies the claims above and runs the focused evidence route. Implementation reports remain claims until checked.
3. **Publication:** separate authority publishes the accepted candidate to public `main` and verifies the exact public SHA.
4. **Routine NUC refresh:** separate bounded authority uses only `deploy/ubuntu/framenest-release`; run `status`, then `check --release <published-40-hex-SHA>`, then the separately authorized deployment and post-update status/health checks. A check never implies deployment permission.
5. **Rendered acceptance:** Michal tests only after the NUC serves that exact published release. Verify the administrator dialog, confirmation, conflict behavior and ordinary-user boundary.
6. **Bounded live proof:** a separate grant permits at most two new generation attempts as described below.

Before live proof, verify model access and applicable standard-tier billing, revalidate price evidence if stale, confirm the accepted provider monthly control, sufficient remaining budgets and no unresolved accounting. Public documentation alone does not establish account access.

Use expressly submitted synthetic public-information questions:

- Research A on `gpt-5.5-2026-04-23`: “Using official Python documentation, explain how asyncio.TaskGroup handles task failures, cancellation, and ExceptionGroup. Include source links.”
- While A is active, change the administrator setting to `gpt-5.6-luna`.
- After A reaches a terminal state, Search B: “What does the official Python documentation say that asyncio.TaskGroup does? Include a source link.”

A must retain its admitted model and pricing; B must use Luna. Total admission reservations cannot exceed USD 5.50, and current lower configured limits still apply. No automatic retries, extra quality comparisons or additional model calls are included.

If A finishes before the setting change, report the live overlap claim as unproven; do not add another generation without authority. The deterministic fake-provider test still supplies causal coverage.

Verify private saved records, complete output, accounting and automatic remote cleanup. Exercise unknown-model refusal without generation and stale-save conflict without overwriting. Restore pre-acceptance settings afterward unless a later explicit choice changes them.

No Timeline publication follows automatically from completion. No second rendered acceptance of unchanged Gallery/Details is required.

Rollback requires a separate bounded operational grant: disable new generation, settle or reconcile outstanding work, restore an older-code-compatible research configuration, then use the routine release mechanism. Preserve records and accounting. There is no schema rollback.

## 10. Proposed first implementation grant — non-authoritative

The following is a recommendation for the Orchestrator’s next complete grant. It grants no authority in this session.

```text
Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 64
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S9-R-IMPLEMENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High
Independence required: no

Authoritative implementation specification:
  Frozen sections 2–8 of 62_report_01.md.

Repository:
  /Users/agile/Projects/framenest
Branch:
  feat/kronika-one-product
Baseline:
  3bf424586289b500cf45cb0d49676b50d27328fa
AP gitlink and checkout:
  73e20ef80b88700d5fcbc397cd8edd4fc425869f

Entry gate:
  Verify root, remote, branch, exact baseline, clean index/worktree
  including untracked files, and clean exact AP checkout.
  Stop on mismatch.

Mutation authority:
  Exactly the 44 paths in section 6.
  Implement one coherent S9-R slice.
  Use only fake providers/credentials and temporary test fixtures.
  Regenerate and review the allowlisted access inventory.
  Run the exact focused route in section 8.

Local Git authority:
  Stage only the exact allowlisted changes.
  Create one local candidate commit:
  feat(research): add administrator settings and versioned pricing
  Report commit, tree, parent, containment and verification evidence.

Excluded:
  Push/publication, merge, deployment, NUC/SSH/sudo, provider calls,
  real credential/configuration inspection, private media, browser runs,
  dependency changes, migrations, AP changes, capture work, subagents,
  additional worktrees and unrelated cleanup.

Stop:
  Scope expansion, unresolved accounting/model mapping, gate conflict,
  or a required failure whose resolution exceeds the allowlist.
  Do not waive failing required checks or invent fallback behavior.

Report:
  64_report_00.md in the configured private trace destination,
  with full chat fallback if file delivery is unavailable.

Terminal boundary:
  Candidate is ready for a separate fresh independent audit only.
  No publication, NUC refresh or rendered/live acceptance follows
  automatically from implementation completion.
```

The Orchestrator must issue that grant afresh with its complete authority and delivery fields. Approval of this plan alone does not activate it.

## 11. Open questions, critique and delivery

**Open product or implementation decisions:** none.

Remaining acceptance facts are account-specific model access, applicable billing tier, actual usage-field behavior in authorized live calls and current deployed candidate identity. They are explicit later gates, not unresolved mappings in this plan.

**Residual limitations:** GPT-5.6 identifiers are undated; provider behavior and prices can change. Reservations cannot guarantee an opaque native run’s final invoice. Unknown accounting and overrun recovery require operator reconciliation rather than an S9-R UI reset.

**Resolved Execution Issues / Near-Misses:**

- The first Responses reference retrieval failed; the official create reference and caching guide resolved the field question.
- Larger combined reads were truncated; relevant conclusions were checked through narrower reads.
- Atomic replacement alone was not mistaken for concurrency protection.
- Configuration schema version and persisted request profile version are explicitly separated.

**Pre-Existing Failure Classification:** no executable gate ran. Static implementation gaps are not reported as observed test failures.

**Orchestration critique:**

- **MEASURED:** the new evidence and bounded retrieval resolved the original model/pricing blocker. The single Cooperator choice was presented and confirmed.
- **MEASURED:** the slice necessarily reaches shared media/CLI configuration writers, runtime composition and accounting. Limiting implementation to a settings form and new endpoint would leave known correctness defects.
- **LEAD:** no additional planning cycle is recommended. Use the focused tests and fresh audit to test this frozen design.

**Changed files:** none, inside or outside the repository.

**Actions not performed:** implementation, tests, builds, server/browser runs, provider calls, credential handling, NUC access, Git writes, trace writes and subagent work.

```text
External trace disposition: configured
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Trace archival owner: COOPERATOR
Delivery route: manual Cooperator delivery
Prompt filename: 62_planning_01.md
Report filename: 62_report_01.md
Destination:
  /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Actual delivery: complete Markdown report in this session
File persistence: not performed; prohibited by active client Plan Mode
Saved-file readback and SHA-256: unavailable
Report persistence owner under fallback: COOPERATOR
Git publication owner: COOPERATOR
```

**Next action:** persist this artifact, reconcile the frozen plan, then issue the fresh implementation grant. No further planning revision is required.

**Authority expiry:** this terminal report ends `kronika-one-product` session 62, exchange 02. Planning authority expires. No implementation is authorized.

