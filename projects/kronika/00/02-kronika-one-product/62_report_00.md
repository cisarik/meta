### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 62
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S9-R-PLAN
Delivery route: manual Cooperator delivery
Status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION
Start commit: 3bf424586289b500cf45cb0d49676b50d27328fa
End commit: 3bf424586289b500cf45cb0d49676b50d27328fa

## Outcome

The repository gate passed. Read-only inspection established the principal implementation boundaries and several material differences from the grant’s description of the existing code.

A decision-complete S9-R plan was not frozen. The permitted evidence establishes one research model and one corresponding price schedule. It does not establish a second selectable model with verified support for the required Responses request features and matching accounting rates. A one-model allowlist would not satisfy the required acceptance demonstration that an administrator can change the model.

The grant prohibits network access and requires escalation when a material mapping cannot be grounded. No additional model, alias, capability claim or price was invented. Implementation should not be authorized from this report.

This complete terminal report is delivered as one Markdown artifact in the session, as subsequently requested by the Cooperator.

## Planning Record — unchanged

```text
Planning cycle: initial
Prior planning report: 25_report_00.md (kronika-one-product 25/01)
Targeted revision basis: none
Changed decision boundary: administrator-managed research provider settings — a Cooperator decision (2026-09-30) that the administrator can set the research model supersedes the accepted "fixed model gpt-5.5-2026-04-23" wording
Preserved unaffected decisions: no client-supplied model/endpoint/tool fields; no automatic fallback; provider/model snapshotted at admission and never changed mid-request; research disabled by default; private/family/administrator access rules; accepted budgets and limits; one generation attempt per request; capture parked; no new framework; testing economy
Automatic targeted revisions used: 0
```

## Plan-to-Execution fields — unchanged

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded implementation planning for the S9-R administrator research-settings slice
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## Verified baseline and evidence limits

| Gate | Observed result |
|---|---|
| Repository root | `/Users/agile/Projects/framenest` |
| Remote | `https://github.com/cisarik/framenest.git` |
| Branch | `feat/kronika-one-product` |
| HEAD | `3bf424586289b500cf45cb0d49676b50d27328fa` |
| Parent | `a3687505eb12359c76f85661e51e36d7e4778fc9` |
| Committed AP gitlink | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Working `.ap` HEAD | Matches the gitlink |
| Index and worktree, including untracked files | Clean at initial and terminal checks |
| AP worktree | Clean |
| RF-12 repository divergence | None observed |

Public branch state and the deployed NUC release were not independently observed. Their equality to the baseline is accepted context supplied by the grant and supported by the latest trace entry, not network or host evidence produced by this Worker.

No tests, server, browser, provider, NUC or SSH operation ran. No credential or private-media inspection occurred. No subagents were used.

Changed files: none.
Commit and push result: none; neither was authorized or attempted.

The report destination was absent at the initial check. At the terminal check, `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/62_report_00.md` existed as a zero-byte regular file. This Worker did not create or modify it. No overwrite was attempted. Native Plan Mode prohibited file writes independently; the Cooperator subsequently selected chat delivery.

## Material repository findings

### 1. Model validation is currently fixed, not merely syntactic

`src/framenest/infrastructure/ai/research_configuration.py` contains two fixed-model checks:

- `ResearchConfiguration.__post_init__` rejects a model unequal to `FIXED_OPENAI_RESPONSES_MODEL_ID`.
- `_require_model_id` applies the same restriction after identifier validation.

`src/framenest/infrastructure/ai/research_registry.py::select_research_provider` independently repeats that restriction.

`src/framenest/domain/research.py:39` defines the fixed identifier as `gpt-5.5-2026-04-23`.

Consequently, a settings form and configuration writer alone cannot enable model changes. The configuration and selection boundaries both require deliberate modification.

### 2. The available pricing evidence covers only the original model

`src/framenest/infrastructure/ai/openai_responses.py::_openai_responses_price_schedule_2026_09_26` defines:

| Price component | Stored rate in micro-USD |
|---|---:|
| Input per million tokens | 5,000,000 |
| Cached input per million tokens | 500,000 |
| Output per million tokens | 30,000,000 |
| Web search per thousand calls | 10,000,000 |

Its documented model is `gpt-5.5-2026-04-23`. Its source is accepted report `25_report_00.md`, section 3, with retrieval date 2026-09-26.

`58_report_00.md` confirms the wiring and explicitly states that prices were not revalidated during that implementation task. The later acceptance trace supplies evidence for the original model’s live path; it supplies no second model-and-price mapping.

The accepted planning report also mentions long-context pricing changes and search-content token charges. An additional model must be checked for compatibility with the existing four-rate `UsagePriceSchedule`, not merely assigned four plausible numbers.

### 3. Runtime configuration is captured at application construction

`src/framenest/adapters/api/application.py::build_research_runtime`:

- Returns `None` for absent or disabled configuration.
- Captures its `configuration` argument in the selection closure.
- Passes one fixed price schedule to `ResearchCoordinator`.

`create_app` loads research configuration once and passes the resulting objects into `ResearchApiDependencies`.

`src/framenest/adapters/api/research_api.py::ResearchApiDependencies` is frozen; the capabilities handler reads its stored configuration.

A durable settings save therefore would not affect the running application by itself. The eventual plan must explicitly connect current configuration to new admission and capabilities reads while retaining access to existing requests for polling, cancellation and cleanup. It must also cover enabling a process that started with research disabled.

### 4. Accounting must follow the admitted request’s model

`src/framenest/application/research.py::ResearchCoordinator.__init__` stores one `_price_schedule`.

`ResearchCoordinator._complete_from_checkpoint` reconciles using that object, rather than selecting a schedule from the request’s persisted profile.

Changing that shared schedule when an administrator saves a model would risk pricing an older request using the newer model’s rates. The implementation must resolve accounting from the admitted model and preserve fail-closed handling when no applicable schedule exists, including after restart.

### 5. Configuration changes interact with submission idempotency

`src/framenest/application/research.py::research_request_fingerprint` includes provider, model, configuration version, reasoning, limits and reservation.

`ResearchCoordinator.admit` selects current configuration and computes this fingerprint before looking up an existing client request ID.

After a model or reservation change, replaying an otherwise identical submission can therefore produce `E_IDEMPOTENCY_CONFLICT`. Disabling research can also prevent that replay before the existing request is found.

The final plan must distinguish retrieval of an existing attempt from admission of a new attempt. A settings change must not silently replace, regenerate or rewrite existing history.

### 6. Atomic replacement does not establish concurrent-save correctness

`src/framenest/infrastructure/ai/configuration.py::mutate_ai_server_config` performs load, mutation, timestamp refresh and write without a surrounding concurrency guard.

`write_ai_server_config` uses an atomic JSON-file replacement. That prevents a partially written file but does not prevent two successful read-modify-write operations from losing each other’s changes.

The final API design must specify conflict detection and coordinate with other configuration writers. Guarding only the new research endpoint would not prove preservation during a concurrent media-provider save.

The writer also serializes the complete document and refreshes `updated_at_ms`. It does not preserve arbitrary original JSON formatting byte-for-byte. The final plan must state the precise non-research preservation assertion rather than claim literal whole-file byte preservation.

### 7. Existing administrator and shell integration points are available

The natural capability is `provider.operate`, already administrator-only in `src/framenest/domain/identity_access.py`.

Existing integration points are:

- `src/framenest/adapters/api/ai_admin_api.py::create_ai_admin_api_router`, its sanitized error envelope and `no-store` responses.
- `src/framenest/adapters/api/tailscale_ingress.py::ROUTE_POLICIES`.
- `src/framenest/adapters/api/web/index.html` — existing `ai-providers-dialog`.
- `src/framenest/adapters/api/web/app.js` — `identityAllowsProviderAdministration`, `openAiProvidersDialog`, `closeAiProvidersDialog`, mutation headers and existing provider state.
- `tests/ai_providers_admin_frontend.test.js` — the established Node/VM testing pattern.
- `tests/contract/test_kronika_access_inventory.py` — inventory generation and composition comparison.

The new surface must require a verified identity as well as the capability. Legacy loopback capability presentation must not substitute for authenticated application-administrator authority.

The accepted “no client selection” rule should remain explicit for Search/Research submissions. The requested administrator configuration API is the separately authorized server-settings surface, not a per-question model selector.

### 8. Existing budget ceilings are already concrete

`src/framenest/domain/research.py` and `ResearchConfiguration` establish these upper bounds:

| Field | Maximum micro-USD |
|---|---:|
| Search reservation | 500,000 |
| Research reservation | 5,000,000 |
| Daily budget | 10,000,000 |
| Monthly budget | 30,000,000 |

Current validation requires positive integers and daily budget no greater than monthly budget.

The eventual settings contract should expose only the accepted monetary fields and enable/model controls. Tool choices, reasoning, concurrency, response limits, deadlines, endpoint, provider selection and credentials must not become incidental editable settings.

### 9. Documentation supersession reaches beyond SPEC and SERVER

Current fixed-model wording occurs in:

- `AGENTS.md`, outside the managed AP block.
- `README.md`.
- `PRODUCT.md`.
- `SPEC.md`.
- `SERVER.md`.
- `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`.

ADR-0083’s “Revisit Conditions” expressly requires a superseding ADR for a changed model or budget decision. The final documentation design must address that clause and preserve the historical initial configuration.

README, PRODUCT, SPEC, SERVER and ROADMAP also contain status language predating the accepted S8/S9 deployment evidence. Those statements need bounded reconciliation using the supplied acceptance evidence, without claiming this Worker independently verified the NUC.

## Planning completeness and validation needs

These findings are implementation-planning evidence, not a frozen specification or an authorized path allowlist.

The following required deliverables remain unfinished at the stop:

- Exhaustive, verified existing/new path allowlist.
- Exact API routes, payloads, error table and concurrent-save contract.
- Complete selectable-model and price-schedule mapping.
- Complete runtime refresh, recovery and idempotency design.
- Detailed shell state, confirmation and accessibility contract.
- Exact documentation patch shape and first implementation grant.

Causal regressions identified for that later frozen plan include:

1. New admission observes a saved model without server restart.
2. An already admitted request retains its model, limits and matching accounting schedule.
3. Restart preserves the same accounting choice for persisted work.
4. A same-ID replay after a settings change returns the original attempt without another generation.
5. Conflicting saves cannot silently overwrite another administrator’s change or a media-provider update.
6. Unknown or unsupported models fail before persistence or provider contact.
7. Missing credentials, anonymous callers and ordinary users cannot trigger generation or unauthorized settings changes.
8. Identity loss and stale asynchronous UI responses cannot restore protected settings.
9. Both new routes appear in the policy table and regenerated access inventory.
10. Existing automatic remote cleanup remains reachable after settings changes.

No test result is claimed. Existing suites and test patterns were inspected as evidence only.

## Smallest next step

The Orchestrator should supply or authorize one bounded public-documentation evidence task establishing at least one additional exact model identifier alongside the existing default.

The required output is a source-backed model matrix covering:

- Current availability and deprecation status.
- Responses API and `web_search` support.
- Compatibility with the existing background, storage, reasoning, tool-choice and token-limit request.
- Input, cached-input, output and web-search pricing, including applicable tiers or special accounting rules.
- Compatibility with the existing `UsagePriceSchedule`.
- Source URLs and retrieval date.

This needs no provider generation, account access, credential handling or NUC operation. Public documentation does not prove account-specific access; that remains a later live-acceptance precondition.

The new external evidence can support the single justified targeted revision of this planning question. This report does not consume that revision.

## First implementation grant disposition

Non-authoritative recommendation: do not issue the S9-R implementation grant yet.

The requested exact implementation allowlist and executable grant cannot responsibly be presented as complete while the model-and-pricing mapping remains unresolved. The eventual grant must retain the exact baseline unless independently updated, use a fresh implementation session with `Native planning mode: not-used`, and separately bound implementation, independent audit, publication, NUC refresh and live/rendered acceptance.

No implementation, publication or deployment authority is created by this report.

## Issues and critique

Resolved Execution Issues / Near-Misses:

- Some large reads were truncated; important conclusions were checked through narrower reads.
- One guessed coordinator path and one unmatched shell glob failed during discovery. The actual coordinator path was located through `rg --files`; no execution or environment repair followed.
- The report destination changed from absent to an existing empty file during the exchange. It was preserved without mutation.

Pre-Existing Failure Classification: no executable gate was run; the findings above are static implementation gaps, not claimed test failures.

Orchestration critique:

MEASURED: The grant requires a demonstrable model change and matching per-model pricing, but its permitted sources substantiate only the original model and it prohibits network access. This prevents a grounded selectable-model set. Smallest correction: provide the missing source-backed model matrix or authorize its bounded retrieval.

MEASURED: The grant describes the existing `model_id` as a validated string, but configuration and registry code enforce equality with the fixed model. Runtime refresh, request-specific pricing and replay semantics also need explicit inclusion in the eventual implementation boundary.

LEAD: none.

Authority expiry: this terminal PARTIAL report ends exchange kronika-one-product 62/01. No further planning or implementation proceeds without a new complete authoritative prompt.