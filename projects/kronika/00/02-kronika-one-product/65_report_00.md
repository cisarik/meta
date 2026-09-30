### Report for ORCHESTRATOR_CHAT

# S9-R independent acceptance audit — candidate e8f1c04

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 65
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Native planning mode: not-used
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S9-R-AUDIT
Delivery route: manual Cooperator delivery
Evidence posture: required-fresh-independent
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: final-acceptance
Escalation disposition: none
Start commit: e8f1c04b289b7bd694d66edba012d288ee41e610
End commit: e8f1c04b289b7bd694d66edba012d288ee41e610
```

`PARTIAL`. The slice is implemented correctly and the declared focused route is
green, but the audit is not an acceptance: three deviations are recorded as
findings, one of which is the named V11 probe, plus one low response-contract
finding. No security defect, no accounting error and no authorization weakness
was found. This audit never repairs; four findings need a bounded correction
grant before publication.

## 1. Compact core

| Item | Result |
|---|---|
| Candidate identity, containment, AP pin | PASS — V1 |
| Catalog, pricing, refusal of unknown/alias models | PASS — V2 |
| Accounting integrity and durable pricing | PASS — V3 |
| Runtime refresh and enable/disable behavior | PASS in code, coverage gap — V4/F-2 |
| Idempotency and single generation attempt | PASS — V5 |
| Shared configuration CAS | PASS, incomplete contract — V6/F-3 |
| Administrator settings API | PASS, one shape deviation — V7/F-4 |
| Shell section | PASS — V8 |
| Documentation supersession | PASS — V9 |
| Recorded deviations | (b) and (c) acceptable; (a) requires a finding — V10 |
| Named report-attribution probe | Reporting defect **and** coverage gap — V11/F-1 |
| Non-regression re-run | PASS — V12 |
| Repository mutated by this audit | none |

## 2. Acceptance record

```text
Acceptance candidate: e8f1c04b289b7bd694d66edba012d288ee41e610
  tree 1cbf6739083e7459b1d5e5011dbd72fed77e5d69, branch feat/kronika-one-product,
  parent 3bf424586289b500cf45cb0d49676b50d27328fa
Acceptance owner map: delta 3bf4245..e8f1c04, one commit, 37 changed paths
Frozen plan: 62_report_01.md, SHA-256
  971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325 (recomputed,
  matches)
Acceptance allowlist honored: read-only review, declared focused route only
Acceptance independence: required-fresh-independent, satisfied
Automatic corrections used: 0
Named missing-evidence probe: V11 report-attribution discrepancy
Result: PARTIAL — 4 findings, 8 ledger candidates, no correction authority used
```

## 3. Control matrix results

| Control | Observed |
|---|---|
| `git rev-parse HEAD 'HEAD^{tree}' HEAD^` | `e8f1c04…`, `1cbf673…`, `3bf4245…` — exact match |
| `git status --porcelain --untracked-files=all` | empty before and after the audit |
| `git diff --name-status 3bf4245..e8f1c04` | 37 paths; none outside the frozen 44-path allowlist |
| `git show e8f1c04` | `feat(research): add administrator settings and versioned pricing`, 37 files, +3612/−235 |
| `git ls-remote origin main feat/kronika-one-product` | both `3bf4245…` — no push |
| `./.ap/ap project check --baseline e8f1c04…` | `PASS` |
| `./.ap/ap exec --operation test-focus` (15 files) | `373 passed in 21.08s` |
| `node --test` (3 files) | `tests 29 / pass 29 / fail 0` |
| `git diff --check` | clean |

Totals independently reproduced and identical to `64_report_00.md` §4
(373 Python, 29 JS). Seven allowlisted paths were deliberately left unchanged:
`test_openai_responses_adapter.py`, `test_research_registry.py`,
`test_ai_provider_admin_api.py`, `test_research_requests_api.py`,
`test_kronika_access_inventory.py`, `ai_providers_admin_frontend.test.js`,
`kronika_ui.test.js`. The first and the last two matter for V10/V11.

## 4. Per-claim verdicts

### V1 — Candidate identity and containment: PASS

HEAD, tree and parent are exact. The branch is clean including untracked files
before and after the audit. The 37 changed paths are a strict subset of the 44
frozen paths; `comm` between the delta and the allowlist is empty in both the
"outside" and "unexpected-new" directions. The AP gitlink and checkout are both
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`, unchanged. Public `main` and the
public feature ref both still read `3bf4245…`, so no publication occurred.

### V2 — Model catalog and pricing: PASS

`src/framenest/infrastructure/ai/research_models.py:94-175` holds exactly four
entries. Every short/long/cache-write rate equals plan §2, web search is
`10_000_000` micro-USD per thousand for every entry, the threshold is `272_000`,
and Sol carries `valid_until = 2026-11-22T00:00:00Z` (`:43`). The three
fixed-model equality checks are gone: `research_configuration.py:139` and `:434`
now call `is_known_selectable_model`, and `research_registry.py:144` does the
same. `provider_id` remains pinned to `openai-responses`
(`research_configuration.py:138`). The module imports only `dataclasses`,
`datetime` and the domain, so there is no network discovery; the existing
`test_ports_do_not_accept_client_endpoint_model_or_tool_fields` still asserts no
`importlib`/`entry_points` in the registry. Alias and unknown identifiers are
refused in `ResearchConfiguration.__post_init__`, again at `_require_model_id`,
at PUT before any mutation, and at selection — that is, before persistence,
reservation or provider contact.

### V3 — Accounting integrity: PASS

`domain/research.py:414` adds `cache_write_input_tokens: int | None`;
`:437` adds `R + W ≤ I`; reasoning `≤ O` is retained. `ResearchAnswer.usage` is
optional (`:550`). `UsageTokenPrices` and the extended `UsagePriceSchedule` are
present (`:461`, `:485`). `usage_cost_micro_usd` selects the tier from total
input tokens (`:786`) and charges five per-component ceilings; reasoning is never
charged twice. `_int_or_zero` is deleted repo-wide (grep: none).

Unknown accounting is fail-closed at every seam: missing or non-`int` required
values, a non-dict details block, an invalid optional value, or an inconsistent
partition all return `None` rather than zero (`openai_responses.py:447-508`).
Missing GPT-5.6 cache-write is unknown because the write rate differs from the
input rate (`domain/research.py:820-824`); GPT-5.5 stays derivable because the
rates are equal, which charges `I − R` at the ordinary rate without inventing a
count. The fixtures hold and are asserted: Luna short `22_990`, Luna long
`127_000`, `272_000` short and `272_001` long
(`test_research_models.py:82-119`).

Durable pricing is tuple-resolved and append-only
(`research_models.py:255-275`); unknown tuples return `None` and fail closed.
Legacy `"3"` requests keep the 2026-09-26 flat schedule with no long tier, so an
unfinished legacy request above the threshold is unknown
(`test_research_models.py:150-165`). `_schedule_for`
(`application/research.py:551`) resolves from the persisted profile, so restart
never reads the current selection — proven end to end with the real adapter,
real repositories and the real resolver in
`test_production_runtime_reconciles_completed_usage`. Overruns are not clamped:
`research_budget_repository.py:112-127` stores the full calculated cost, and
`BudgetReconciliation` imposes no upper bound against the reservation.
`blocking_accounting_state` (`:163-208`) fails closed on unknown accounting, on
`accounted > reserved`, and on a terminal request whose hold is still reserved.
The reservation is preserved for unknown accounting (`:114-116`).

### V4 — Runtime and enable/disable: PASS in code; finding F-2 on coverage

`build_research_runtime` now builds whenever the engine exists
(`application.py:416-421`), including a disabled start, and construction performs
no credential provisioning and no provider contact. `create_app` passes
`_read_research_configuration` as a live provider (`:1631`), so admission and
capabilities read a fresh validated configuration on every call; saving settings
does not touch the runtime, so the coordinator is never replaced and recovery is
never re-run. Disabling refuses new admissions at
`research_registry.py:139` and refuses new submission claims via
`submission_enabled` (`application/research.py:271-273`); polling, cancellation,
cleanup and history are untouched by that predicate. Re-enabling therefore
activates a process started disabled. Admitted snapshots are immutable because
they are persisted at admission and never re-selected.

The behavior is correct, but plan §8's `Refresh` and `Snapshot` rows have no
causal regression. See F-2.

### V5 — Idempotency and single attempt: PASS

`application/research.py:178-190` looks up `(owner, client_request_id)` before
the accounting blocker, the selection, enablement and credentials. The version-2
fingerprint (`:65-92`) covers fingerprint version, owner, kind, prompt and
consent only — no provider, model, budget, limit or revision — so an identical
replay returns the original attempt after those change. Legacy `"3"` rows are
compared on persisted owner, kind and prompt without inventing consent
(`:257-282`). Changed content raises `E_IDEMPOTENCY_CONFLICT`
(`test_research_coordinator.py:321`). The receipt
(`ports/research.py:159`) gates the nudge: `research_api.py:290` submits only
when `newly_admitted` and the row is `admitted`. The atomic claim is a
conditional `UPDATE` with a `rowcount != 1` guard inside an immediate
transaction (`research_request_repository.py:311-336`), so only one winner issues
provider creation; `test_claim_submission_has_one_winner` proves the second claim
returns `None`.

### V6 — Shared configuration CAS: PASS; finding F-3 on completeness

`load_ai_server_config_snapshot` (`configuration.py:237-259`) returns the
validated config plus a SHA-256 of the same bounded raw bytes, with
`"absent"` for a missing file, and it re-validates through the existing loader so
the revision cannot drift from the configuration. `_config_file_guard`
(`:594-616`) composes a per-canonical-path process lock with a stable sibling
OS advisory lock; the lock file is created `0o600`, is never removed, and
rejects symlinks and non-regular objects (`:517-556`). The guard is not
re-entered anywhere, so there is no deadlock path.

CAS follows the five-step plan sequence: read snapshot, compare, validate,
bounded mutation, atomic replace. `write_ai_server_config` without an expected
revision is creation-only (`:270-283`). A fresh no-op returns success without
rewriting or advancing the revision, and a real change advances `updated_at_ms`
monotonically (`:293-303`). `_strong_if_match` (`:1105-1120`) rejects empty
values, wildcards, lists, weak tags and unquoted values. A stale revision returns
409 before any write, and `mutate_ai_server_config` re-checks under the guard,
so there is no lost update. Revision and strong ETag are delivered on the
media-provider read and all three mutation responses
(`ai_admin_api.py:389`, `:471-486`, `:527-536`, `:576-586`). All four CLI writers
capture a revision and honour it; the interactive writer captures it before
prompting (`cli/ai.py:309-352`) and a stale save is refused without clobbering
the concurrent write (`test_configure_interactive_refuses_a_stale_save`), which
surfaces as a clean `AI configuration error: AI configuration changed.` with exit
2 through `main`. The preservation assertion holds in both directions on
supported normalized values, not byte-for-byte
(`test_ai_configuration_storage.py:697-730`).

F-3 records that the *media* half of the shared contract is only partially
delivered.

### V7 — Administrator settings API: PASS; finding F-4

Both routes exist in `ai_admin_api.py`. `_research_identity` (`:748-762`) runs
first, before any configuration or credential read, and requires a resolved
`IdentityContext`, a non-empty `login_key` and `provider.operate`; the identity
comes from `SCOPE_IDENTITY`, so loopback capability presentation alone is
insufficient. Both routes are registered only in workspace composition — the
regenerated inventory lists exactly one row each, labelled `workspace`, and the
inventory test asserts `keys == labeled` over the union of both compositions, so
public absence is established. Both have explicit `RoutePolicy` entries with
`CAPABILITY_PROVIDER_OPERATE`, and the PUT carries
`audit_action="ai.research.settings.update"`,
`audit_target_type="research_settings"` (`tailscale_ingress.py:460-471`). The
generic ingress path records the allowed attempt before the mutation and returns
`None` when the audit record cannot be written
(`tailscale_ingress.py:1009-1042`), so an unavailable required audit record
prevents mutation.

`ResearchSettingsBody` is `extra="forbid"` with all six fields required. Bounds
match the plan exactly: daily 1–10,000,000, monthly 1–30,000,000, search
1–500,000, research 1–5,000,000, plus daily ≤ monthly
(`ai_admin_api.py:900-925` against `domain/research.py:27-30`). No provider,
credential, secret, endpoint, tool, reasoning, concurrency or request-limit field
is writable. Missing `If-Match` is a 409 before any work, and a stale revision is
a 409 before any write. Absent configuration refuses PUT with the exact
503 copy, GET reports disabled defaults with `configuration_present: false`
without creating a file, and missing credentials allow disabled edits but refuse
enabling with the exact `E_NOT_CONFIGURED` copy. Successful and error responses
carry `Cache-Control: no-store` through the shared `_json`/`_json_with_etag`
helpers. GET performs no provider probe and exposes `credential_available` as a
boolean only; `test_get_body_contains_no_secret_material` asserts no secret
material. The stable error table is implemented verbatim. F-4 records one
response-shape deviation.

### V8 — Shell: PASS

`index.html:535-581` places a **Research settings** section inside the existing
administrator AI dialog. The three required copy paragraphs are present verbatim
(`:537-539`). The identity predicate
(`app.js:12874-12879`) is strictly stronger than the legacy media predicate:
resolved identity, availability, workspace audience and `provider.operate`.
`researchSettingsParseUsd` (`app.js:12893-12902`) converts with `BigInt` integer
arithmetic under a strict `/^[0-9]+(\.[0-9]{0,6})?$/` and rejects anything that
would need float rounding or exceed `Number.MAX_SAFE_INTEGER`;
`researchSettingsFormatUsd` is integer-only. Model or budget changes arm an
explicit confirmation showing the previous and next model and the resulting
budgets; cancelling sends no PUT; and any later edit clears `confirmArmed` and
`pendingDraft` (`app.js:13250-13270`). A 409 sets the conflict copy and marks
the draft dirty without rebasing or resending. A network failure retains the
draft and instructs a reload. `clearResearchSettingsProtectedState` plus a
`responseGeneration` counter mean a stale response cannot reopen or repopulate the
section, and focus is restored on close. Labels are associated, status uses
`role="status" aria-live="polite"`, and the JS suite passes 29/29. `styles.css`
adds 34 scoped lines under `research-settings`; the Gallery and Details surfaces
are untouched. Two plan §5 details are softer than specified and are recorded as
ledger candidates L-3 and L-4.

### V9 — Documentation: PASS

ADR-0084 exists, `Accepted`, dated 2026-09-30, and records the confirmed
four-model choice with the unchanged default, the exact schedule tables identical
to plan §2, the Sol expiry policy, the immutable-pricing rules, the runtime
refresh and disabling rules, the idempotency rule, the shared CAS contract and the
fail-closed accounting rules. ADR-0083 carries a partial-supersession notice that
names exactly what is superseded and keeps the original fixed-model wording as
historical text; `docs/adr/README.md` gains both the narrative note and the index
row. SPEC promotes all six required normative statements; SERVER documents
dynamic reads, disabled-start activation, durable schedule derivation, shared CAS
and continued settlement; AGENTS changes only project-owned text outside the
managed AP block. README, PRODUCT and ROADMAP state that S9-R is a candidate
awaiting its own audit, publication, NUC refresh and rendered acceptance, and
claim no acceptance and no NUC observation.

### V10 — Recorded deviations: (b) and (c) acceptable; (a) requires a finding

**(a) Media-provider `If-Match` optional — finding F-3.** As an HTTP-compatibility
choice this is defensible: absent header keeps prior unconditional behavior, a
supplied stale/malformed/wildcard value is a 409 without writing, and the
unchanged `test_ai_provider_admin_api.py` still passes. But the deviation is
larger than `64_report_00.md` §6 states. Plan §4 also required updating the media
shell callers, and no media caller sends `If-Match` or consumes the new ETag
(`app.js` has exactly one `If-Match`, the research PUT at `:13174`). Plan §5
required that a successful media save invalidate the research revision and vice
versa; `researchSettingsState.revision` is written only from a research response
(`app.js:12985`). And the plan's own test path for "Media/research revision
coordination", `tests/ai_providers_admin_frontend.test.js`, is unchanged, so that
coordination has no coverage. The net effect is fail-safe — media mutations keep
their prior semantics and research saves are CAS-protected, so a stale research
save after a media save is a 409 rather than a lost update — but the declared
single concurrency contract is only partially delivered and the deviation record
understates it.

**(b) Sol cutoff at admission and PUT enabling — acceptable.** Plan §2's
operative requirement is "Refuse new admissions whose deadline could cross that
cutoff", and plan §2 also requires that expiry never prevents disabling research.
`application.py:441-452` enforces both: `admission_guard` refuses an expired model
and a deadline that would cross the cutoff, and the PUT refuses enabling an
expired model. The narrow residual — a *disabled* save may newly store an expired
selection — is recorded as L-2; it cannot reach a generation because admission and
re-enabling both fail closed. Keeping the frozen `select(config, kind)` signature
is a legitimate reason.

**(c) Legacy over-threshold unknown accounting — acceptable and exactly as
planned.** Plan §3 states that an unfinished legacy request above 272,000 input
tokens has unknown accounting because its original flat schedule does not cover
that tier. `legacy_2026_09_26_schedule` sets a threshold with no long tier, and
`select_token_prices` returns `None`, which `usage_cost_micro_usd_or_none`
turns into unknown rather than a value.

### V11 — Named report-attribution probe: reporting defect **and** coverage gap (F-1)

`64_report_00.md` §4 states that "strict usage parsing and submit-404 distinction"
tests were added to `tests/unit/infrastructure/ai/test_openai_responses_adapter.py`.
That file is byte-identical between `3bf4245` and `e8f1c04`
(`git diff --stat` on it is empty), and it contains neither.

**What the file actually contains.** The only `submit` tests are
`test_submit_builds_a_bounded_server_selected_body` (HTTP 200) and
`test_missing_credential_is_not_configured_without_network` (no key, no network).
No test drives `submit` with any HTTP error status. The only usage assertion is
`test_poll_completed_parses_answer_evidence_and_usage:207-211`, against a fully
populated valid `usage` block. The 404 assertions at `:231` and `:261` are
pre-existing and concern polling and remote release, not creation.

**Where the required coverage actually lives — for one half only.** The
adapter file is the only test file in the repository that constructs
`OpenAIResponsesAdapter`; every other research test uses a fake provider, so
nothing else can reach these seams. Consequences:

- `_parse_usage` (`openai_responses.py:447-508`), the entire replacement for
  `_int_or_zero`, has **zero** references in any test. Plan §8's
  `Missing evidence` row, "missing/invalid usage never becomes zero", is proven
  only at the *domain* seam (`test_research_models.py:122`, missing GPT-5.6
  cache-write) and by the coordinator's blocker. The adapter step that decides
  `answer.usage is None` rather than a zeroed `ResearchUsage` is unproven.
- `_submit_status_error_code` (`openai_responses.py:132-140`), added by this
  commit and the whole point of plan §2's "a submission 404 must not masquerade
  as a missing historical response", has **zero** references in any test. The
  polling half is proven by the pre-existing
  `test_poll_missing_response_and_transport_failure_map_to_codes:231-232`
  (`RESULT_EXPIRED`); the creation half is unproven. The change is real and
  correct by inspection — before it, a submit 404 became `RESULT_EXPIRED` and
  would have finalized the request as a released remote — but nothing guards it.

**Disposition: both.** It is a reporting defect, because §4 attributes coverage
to a file that was not touched. It is also a coverage gap, because two new
behavior-changing functions in a defensive, accounting-bearing slice have no
causal regression, and the focused route is the only evidence that will exist
before publication and NUC deployment. The report's claim is the more serious half:
it states as established evidence something the repository does not contain.

## 5. Findings

**F-1 — Report attribution defect plus two untested adapter behaviors (V11).**
Severity: medium. `64_report_00.md` §4 attributes "strict usage parsing and
submit-404 distinction" to `tests/unit/infrastructure/ai/test_openai_responses_adapter.py`,
which is unchanged in the delta. In reality `_parse_usage` and
`_submit_status_error_code` — both introduced by this commit — have no test
references anywhere in the repository. Plan §2's submit-404 distinction and
plan §8's "missing/invalid usage never becomes zero" are therefore unproven.
Correction: correct the §4 attribution, and add focused causal regressions in
`test_openai_responses_adapter.py` for missing/invalid `usage` yielding
`usage is None`, for a non-dict details block, for a submit 404 mapping to
`PROVIDER_UNAVAILABLE` while a poll 404 still maps to `RESULT_EXPIRED`, and
optionally for the reported `cache_write_tokens` path. That file is already
inside the frozen allowlist, so no scope change is required.

**F-2 — Dynamic refresh and durable-snapshot behavior have no causal regression
(V4, plan §8 `Refresh` and `Snapshot` rows).** Severity: medium. No test builds
the runtime with a real engine while research is disabled
(`test_research_runtime_wiring_is_inert_when_disabled` only passes `engine=None`
and asserts `None`); no test exercises disable-then-re-enable on a persistent
coordinator; no test shows a saved model reaching the next admission without a
restart; no test shows request A keeping its admitted model and schedule after
settings change to B, including after a restart. `build_research_runtime` is
exercised only with a static `configuration`, so the new
`configuration_provider` path is untested at composition level. The
implementation is correct by inspection and by construction, but the two most
important runtime guarantees of this slice rest on code reading alone.
Correction: add contract regressions in
`tests/contract/test_research_provider_contract.py` and/or
`tests/contract/test_research_completion.py` that build the runtime with a real
engine and a mutable configuration provider, assert it exists while disabled,
admit after enabling, change the model, and assert the next admission uses the new
model while the first request keeps its persisted model, schedule and reconciled
cost after a simulated restart.

**F-3 — The media half of the shared configuration contract is partial and
under-reported (V6, V10a).** Severity: low-medium. Server-side optional
`If-Match` is acceptable, but plan §4's "update its shell callers" and plan §5's
"a successful media save invalidates the research revision and vice versa" are
not implemented: no media shell caller sends `If-Match` or reads the new ETag,
`researchSettingsState.revision` is written only from research responses, and the
plan-listed `tests/ai_providers_admin_frontend.test.js` ("Media/research revision
coordination") is unchanged. The behavior is fail-safe, so this is not a
security finding; it is an under-scoped contract and a mis-stated deviation
record. Correction: either complete the shell coordination with the corresponding
JS coverage, or record the omission as an explicit accepted deviation.

**F-4 — The GET research-settings response carries `changed: null` (V7).**
Severity: low. Plan §4 specifies that GET returns *exactly* seven top-level
fields and that PUT returns the same representation *plus* `changed: boolean`.
`ResearchSettingsResponse.changed` is `bool | None = None` and `_json_with_etag`
uses `model_dump()` without `exclude_none`, so GET emits an eighth key with a
null value. No secret, capability or authorization impact; the shell reads
`body.changed` only on PUT. Correction: emit the GET and PUT shapes from
separate models, or use `response_model_exclude_none`, and add a key-set
assertion to `test_research_settings_api.py`.

## 6. Ledger candidates (non-authorizing, out of scope for this audit)

- **L-1** — A missing `usage.input_tokens_details.cached_tokens` is parsed as `0`,
  not as unknown. The plan carves out only `W`, and `0` is the conservative
  (higher-cost) reading and preserves prior behavior, but "missing required
  accounting values produce unknown accounting" is ambiguous for `R`. If `R` were
  treated as unknown, virtually every real response would become unknown
  accounting, since OpenAI omits the field when nothing is cached. Worth an
  explicit decision.
- **L-2** — A disabled PUT may newly store an expired model, and the shell renders
  non-selectable models as enabled `<option>`s marked "(unavailable)" rather than
  `disabled`. No generation can result, because admission and re-enabling both
  fail closed.
- **L-3** — Plan §5's "confirm discarding a dirty draft" is not implemented; the
  research section tracks `dirty` but never prompts, and the legacy media section
  has no dirty-draft convention to inherit. Likewise, "after an uncertain network
  outcome, read the server state before allowing another explicit save" is
  advisory text rather than a block on the Save button. CAS makes both fail-safe.
- **L-4** — The confirmation note shows the daily and monthly budgets but not the
  two reservation values, which also trigger confirmation.
- **L-5** — No test binds the two new `RoutePolicy` entries to their routes. The
  inventory test skips paths under the provider-administration exclusion, so a
  stale or mistyped policy would go undetected. The entries were verified by
  direct reading.
- **L-6** — Plan §3's "serialize configuration selection and durable admission
  against configuration writes using the shared configuration guard" is
  implemented on the write side only; the read side is a plain read of a file
  replaced atomically. No lost update and no torn read is possible, and a read
  failure refuses admission, but the plan wording is broader than the code.
- **L-7** — `ai_admin_api.py:479` and `:1044` use `assert` for narrowing; under
  `python -O` a delete-between-check-and-write race would surface as a 500
  instead of a sanitized 503.
- **L-8** — "Replay returns the original attempt after model, budget or
  enablement changes" is guaranteed by construction, since the lookup precedes
  `select`, but no test changes those inputs between the two calls.

## 7. Limitations

- The audit is a read-only code and focused-test review. It performed no rendered
  or browser acceptance, no provider call, no credential handling, no NUC access
  and no real configuration inspection, all of which are excluded by the grant.
- `V12` re-ran the declared focused route only. The broad suite was not run, so a
  regression outside those 15 Python and 3 JavaScript files is not excluded. Two
  of them (`test_registry.py`, `test_ai_server_composition.py`) are read-only
  compatibility inputs, as the plan intended.
- The access inventory was regenerated by its own test and inspected as a diff.
  Per plan §8, that is not treated as proof of authorization correctness; the
  authorization evidence here is the route code, the `RoutePolicy` entries and
  the ingress audit path.
- Windows advisory locking is `pragma: no cover` and was not executed; only the
  POSIX `fcntl` path was exercised.
- Conclusions about model access, applicable billing tier and real
  `cache_write_tokens` field behavior remain later live gates.

## 8. Residual risk

If published as-is, the slice's behavior is sound, but three runtime and adapter
guarantees — the submit-404 distinction, the never-zero usage parse, and the
dynamic disabled-start refresh — would reach the NUC with no regression guarding
them. The first two are accounting- and lifecycle-adjacent: a future refactor
could silently restore `RESULT_EXPIRED` on a creation 404, which would finalize
an attempt as a released remote and lose a reservation, or reintroduce
zero-filling that hides missing accounting. Both are cheap to guard and both are
inside the existing allowlist. The refresh gap is the largest single exposure,
because the coordinator lifecycle is the most structurally changed part of the
slice and its distinguishing behavior is the least tested. Nothing observed here
is a security weakness: verified-identity authorization, fail-closed accounting,
immutable admitted pricing, single-claim submission, no client model selection
and no secret exposure all hold at the code level.

## 9. Critique

- **MEASURED** — Containment, catalog rates, arithmetic fixtures, CAS ordering,
  the atomic claim, fingerprint scope, error tables, copy and documentation
  supersession were all established by direct reading and by re-running the
  focused route. Every rate in the catalog and in ADR-0084 matches plan §2
  exactly.
- **MEASURED** — The implementation is of good quality. Fail-closed paths are
  consistent, unknown accounting is never coerced to zero, the no-op path does
  not advance the revision, and the guard is not re-entered. The defects found
  are in evidence and in two narrow contract details, not in the core logic.
- **MEASURED** — The report's §4 evidence paragraph overstated coverage. This is
  the second time in this logical whole's history that an implementation report
  has attributed coverage to a file the delta did not touch; the Orchestrator
  should treat §4 "causal regressions added" lists as claims requiring a
  file-level diff, not as evidence.
- **LEAD** — Do not publish or refresh the NUC from this candidate. A single
  bounded correction grant covering F-1 through F-4, all inside the existing
  44-path allowlist and requiring no migration, dependency or AP change, would
  close the slice. F-1 and F-2 are the substantive ones; F-3 and F-4 are cheap.
- **LEAD** — The plan's §8 evidence table is a good contract, and the two rows
  that failed here (`Refresh`, `Snapshot`) plus the two adapter behaviors are
  exactly the rows a mechanical test-count review would have missed. Future
  implementation grants should require the report to name, per §8 row, the exact
  test function that discharges it.

## 10. Authority expiry

This terminal report ends `kronika-one-product` session 65, exchange 01.
Acceptance authority expires with it. This audit never repaired anything and no
correction authority was granted or used. The repository is unchanged and clean
at `e8f1c04b289b7bd694d66edba012d288ee41e610`. Publication, NUC refresh,
rendered acceptance and bounded live proof remain separate authorities and none
is recommended until F-1 through F-4 are closed and re-audited.

```text
External trace disposition: configured
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 65_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 65_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (written to the configured destination)
Git publication owner: COOPERATOR
Archival: wait-for-report
Changed files: none in the repository; this report only
Actions not performed: implementation, correction, tests beyond the declared
  focused route, builds, server or browser runs, provider calls, credential
  handling, NUC or SSH access, Git writes, private media, subagent work
```
