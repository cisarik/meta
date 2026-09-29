### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 51
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S4B-S7P-REAUDIT
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 74f2a404a4d999407248e07f6ffab325c692722d
Result evidence: candidate SHA, tree, parent and the ten commits match; public main and feat/kronika-one-product both equal that SHA; focused suite 340 passed, exit 0; synthetic probe plus systemd contract 30 passed, exit 0; one open low non-blocking finding (unbounded quote recursion)
Logical-whole closure: not-closed
Start commit: 74f2a404a4d999407248e07f6ffab325c692722d
End commit: 74f2a404a4d999407248e07f6ffab325c692722d
Changed files: none in FrameNest; this report only
Tests and validation: `ap project check` exit 0; declared `test-focus` 340 passed, exit 0; probe plus `tests/contract/test_fedora_systemd_service.py` 30 passed, exit 0; probe root removed
Commit and push result: not authorized by this audit; not performed
Deviations, risks, or missing evidence: the prompt's starting-state tree string is 38 hex characters and does not match `HEAD^{tree}`; the candidate-block tree does match. Living README, PRODUCT, SPEC, ROADMAP and SECURITY sentences still say schema head `0034`, and the tests that lock those sentences were outside this delta. Production `build_research_runtime` does not inject a price schedule, so a saved request is reconciled as unknown and consumes the reservation. The broad suite and the four parked failures were not run. One open low finding remains.
Smallest next step: the successor Orchestrator reconciles the handout, dispositions F01 (accept as residual or authorize one bounded correction), then continues with S8
Report justification: final-acceptance
Authority expiry: this terminal report ends the independent-audit exchange

## Acceptance record

```text
Acceptance candidate: 74f2a404a4d999407248e07f6ffab325c692722d
  (tree 1715bbdb915ef619d81cf1f12a52c09acaa61d7e, branch feat/kronika-one-product,
   parent c0a528880d0184df9d5b65c1ecbc33fee071ee25)
Acceptance owner map: delta 89a402981a9eac83646199c77984c3fc21c0744d..74f2a404a4d999407248e07f6ffab325c692722d
  (10 commits, 53 paths, +6127/-73); plans 47 and 49 are evidence only
Acceptance allowlist: read-only review; declared focused route; public-ref readback;
  one temporary probe root /tmp/kronika-one-product-verify-74f2a40
  (mode 0700, synthetic data only, removed)
Acceptance risk claims: the eleven fixed claims
Acceptance control matrix: declared git and focused-route controls, plus the
  negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none required beyond the controls that were run
Out-of-scope observations: living product sentences still name schema head 0034;
  production composition reconciles successful usage as unknown
```

This session did not implement, correct or plan the audited chains. Prior plans and reports were not treated as authority.

## Security audit record

```text
Security task class: focused defensive audit (R3), with authN/Z, file and provider-boundary specializations
Owned/authorized target: /Users/agile/Projects/framenest at 74f2a404a4d999407248e07f6ffab325c692722d, read-only
Commit under audit: 74f2a404a4d999407248e07f6ffab325c692722d
Scope: the ten-commit delta from 89a402981a9eac83646199c77984c3fc21c0744d
Exclusions: NUC, SSH, sudo, browser, live provider, credentials, private/**, broad suite, correction
Threat model: fields below
Source records: no external standard was re-fetched; CWE and ASVS mappings are none
Findings: F01 open low; attribute-injection hypothesis rejected below
Containment ledger: probe root created mode 0700 and removed
Limitations: section below
Residual-risk summary: F01 is open and non-blocking; Orchestrator disposition is still required
```

```text
Assets: research prompts and answers, owner identity, budget ledger, private catalog, provider credential
Trust boundaries: caller to research and records HTTP; untrusted model text to the HTML renderer; server-selected profile to the provider adapter; catalog migration 0035
Attacker-controlled inputs: authenticated request JSON, client request ids, Markdown stored as question or answer text, provider response bodies parsed by the adapter
Security properties: inert-by-default runtime, no client model or tool selection, owner isolation, administrator-only approval, escaped rendering, atomic completion, reservation accounting that does not store unknown usage as zero
Abuse cases: cross-owner read, unapproved household read, raw HTML or javascript links, credential or provider-body leakage, double-spend of a client key, slot bypass, completion of a cancelled request, downgrade that drops rows
```

## Identity gate

```text
HEAD:        74f2a404a4d999407248e07f6ffab325c692722d
HEAD^{tree}: 1715bbdb915ef619d81cf1f12a52c09acaa61d7e
HEAD^:       c0a528880d0184df9d5b65c1ecbc33fee071ee25
branch:      feat/kronika-one-product
status:      empty porcelain, including untracked files, before and after the audit
.ap gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
public main: 74f2a404a4d999407248e07f6ffab325c692722d
public feat/kronika-one-product: 74f2a404a4d999407248e07f6ffab325c692722d
public feat/chatgpt-page-ask-kernel: 26d28b16c08a5e7e0179a32c16646bfdc1009c81
public feat/x-meme-browser-companion: 7ff6546f345827d6df20bd5b13d5e57cb4bc90db
```

`git log --oneline -11` shows the ten audited commits in the prompt's order, with parent `89a4029`. `git diff --shortstat 89a4029..HEAD` is `53 files changed, 6127 insertions(+), 73 deletions(-)`. The path list contains no `private/**`, no `.ap`, no `pyproject.toml`, no `poetry.lock`, and no migration file other than `0035_research_requests_and_accounting.py`.

The prompt's starting-state block prints a 38-character tree (`…c09aa61d7e`). The candidate block and `HEAD^{tree}` are the 40-character tree above. SHA, parent, branch, clean status and public refs match, so this is a prompt transcription defect, not a candidate mismatch. NUC was not contacted.

## Control matrix

| Control | Result |
|---|---|
| `git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'` | exit 0; values above |
| `git log --oneline -11` | exit 0; ten audited subjects match |
| `git diff --name-status 89a4029..HEAD` | exit 0; 53 paths |
| `git status --porcelain --untracked-files=all` | exit 0; empty |
| `GIT_TERMINAL_PROMPT=0 git ls-remote` of the four named refs | exit 0; main and feature head equal the candidate |
| `ap project check --baseline 74f2a40…` | exit 0; PASS; CPython 3.13 |
| declared `ap exec test-focus` (19 files) | exit 0; `340 passed in 45.83s` |
| probe file plus `tests/contract/test_fedora_systemd_service.py` | exit 0; `30 passed in 1.62s` (10 probe, 20 systemd) |
| leak hunt on added production lines | two identifier hits, no secret value; see claim 1 |
| probe-root cleanup | removed; absence checked |

The first probe invocation exited 1 on one probe assertion that treated an HTML-escaped `onclick` sequence inside an href as attribute breakout. The rendered value was `&quot;onclick=&quot;`. The assertion was corrected and the same route re-ran green. That failure was the probe, not the product.

## Per-claim verdicts

1. Candidate identity, containment and inert-by-default posture — established. SHA, tree, parent, ten commits, 53-path delta and clean worktree match. Added production lines contain `LoadCredential=KRONIKA_RESEARCH_OPENAI_API_KEY:/etc/framenest/credentials/research-openai` and `api_key = self._api_key_supplier()`, which are names and a supplier call, not a secret value. `build_research_runtime` returns `None` when configuration is missing or `enabled` is false (`application.py` lines 421–422); `test_research_runtime_wiring_is_inert_when_disabled` passed inside the 340. Construction of `HttpsJsonTransport` stores timeout and size only. `urlopen` is reached only from `_execute`. `create_app` catches runtime construction failure and still returns the app. `.ap`, packaging, lockfile and migrations `0001..0034` are absent from the name-status list.

2. Migration `0035` integrity — established. `0035_research_requests_and_accounting.py` creates `research_requests`, `research_operations`, `research_budget_holds` and `research_active_slot`, with the named CHECKs, the unique `(owner_login_key, client_request_id)`, the unique `record_id`, and foreign keys to `kronika_records` and `research_requests`. `test_populated_downgrade_refuses_without_dropping_rows` asserts the exception text contains `refused`, revision stays `0035`, and all three populated counts stay 1. `test_request_constraints_reject_malformed_rows` raises `IntegrityError` for a short fingerprint, a byte-count mismatch and lifecycle state `paused`. Executable head checks in the delta assert `0035`, including `REQUIRED_PUBLIC_SCHEMA_REVISION`. Downgrade targets such as `0034` and `0033` remain historical. Living product sentences that still say `0034` are outside this delta; see limitations.

3. Repositories and budget ledger — established. `SqliteResearchRequestRepository.admit` runs in `run_in_immediate_transaction`. An exact client-key replay returns the existing row; a different fingerprint raises `IDEMPOTENCY_CONFLICT` before insert; a held slot raises `BUSY`; `reserve_hold` runs after the request insert so a budget refusal rolls the request, hold and slot back. `save` clears the slot when the lifecycle is terminal and the slot operation id matches. `reconcile_hold` stores the calculated cost for `reconciled` and the reservation itself for `unknown`. `test_reconcile_unknown_consumes_the_reservation` and `test_budget_exceeded_rolls_back_admission` passed. `_consumed_micros` adds `accounted` for every non-reserved row, and the shape CHECK forbids a reconciled or unknown row with a null accounted amount.

4. Coordinator lifecycle — established. `submit_pending` saves `SUBMITTING` before `provider.submit`. The probe's raising provider observed that stored state, then a `RuntimeError`, and the row finished `submission_unknown` with unknown accounting, a released slot, and no second submit (`provider.calls == ["submit"]`). `ProviderObservationKind.UNCERTAIN` is covered by `test_submit_uncertain_becomes_submission_unknown`. `recover` on a persisted `SUBMITTING` row is covered by `test_recover_submitting_becomes_submission_unknown`. The deadline path calls cancel and finishes `timeout` (`test_deadline_timeout_finishes_timeout`). A cancel that stays `RUNNING` followed by `COMPLETE` finishes `cancelled` with `record_id is None` and zero completion calls (probe). A completion exception leaves `validating` and a later poll reaches `saved` (`test_completion_failure_keeps_validating_and_retries`). Adapter `HttpsTransportError` is mapped to a stable code and returned as `FAILED`, so it does not re-enter the coordinator's exception path; an exception that does escape the provider port is the path the probe ran.

5. Adapter boundary — established. `_submit_body` copies `model`, tools, limits and reasoning from `request.profile` only. `test_submit_builds_a_bounded_server_selected_body` asserts the fixed model, `web_search`, and the absence of an `endpoint` or `tool` field, and the byte cap `16384 + 4096`. A missing supplier result returns `NOT_CONFIGURED` with `transport.posts == []`. Poll accepts `COMPLETE` only after `completion_error` is absent; a completed payload without a web-search call is `NO_WEB_EVIDENCE`. Status and transport 404 map to `RESULT_EXPIRED`. `release_remote` treats that code and HTTP 404 as `DELETED`. Observations carry codes, not bodies. The probe built `urllib.request.Request` for hostile handles (`https://evil.example/...`, `//evil.example/...`, `@evil.example`, `resp-1/../../v1/models`); `request.host` stayed `api.openai.com`. No socket was opened.

6. Atomic completion and record binding — established. `SqliteResearchResultCompletion.complete` inserts the document, the record with `owner_login_key` taken from the stored request, and the `record_id` update inside one immediate transaction. An existing `record_id` returns the saved receipt without a second insert (`test_exact_replay_returns_existing_binding` asserts document and record counts stay `(1, 1)`). `test_coordinator_with_real_completion_binds_the_record` asserts the reloaded row's `record_id` equals the `kronika_records.id` and the owner is `alice@example.com`. `record_id` is mutable on later saves; the coordinator reloads before the terminal save, and that test is the dynamic check that the binding survives.

7. Authorized HTTP surfaces — established for the composed routes exercised by the focused suite. Research handlers return 401 without an identity, 403 on capability denial, and the same 404 body for a missing row and a foreign owner (`research_api.py` lines 277–280 and 299–303). Duplicate submit is 202 with the same operation id; conflicting reuse is 409 `E_IDEMPOTENCY_CONFLICT`; a null runtime is 503 `E_DISABLED` while `GET /api/research/capabilities` still returns `enabled: false`. Administrator inventory is `CAPABILITY_RECORDS_APPROVE` at the route policy and the handler. Records: `/api/my/records` lists `identity.login_key`; `/api/timeline` uses `timeline_only`; detail uses `decide_bound_read`, and deny is `RecordNotFoundError` mapped to the same 404 helper as a missing id. Render uses that same read, then escaped HTML with `nosniff` and `default-src 'none'`. Approval requires the administrator capability; expected version 999 is 409; `reject` is 422. These are `test_anonymous_is_refused`, `test_submission_progress_and_owner_separation`, `test_household_member_sees_only_the_approved_projection`, `test_stale_version_conflicts_and_users_cannot_approve`, and the inventory denial parametrization, all inside the 340. Remote ingress still requires a Tailscale login before the handler, including for capabilities, whose route policy has no extra capability.

8. Rendering and capabilities safety — established for the XSS claims, with F01 open on recursion. `render_inline` escapes every non-match span and every code, label and emphasis group. Links are emitted only when the stripped URL starts with `http://`, `https://` or `mailto:`; the href uses `escape(..., quote=True)`. The probe's `<script>`, `javascript:`, `JavaScript:` and `data:text/html` inputs produced no raw script element and no `javascript:` href. The quote-injection case stayed inside one href as `&quot;onclick=&quot;`. Capabilities omit the supplier result; disabled configuration returns `enabled: false` and does not call the transport. F01 is the remaining renderer limit and is not an HTML-passthrough failure.

9. Route-policy and inventory completeness — established. The new research and records templates are explicit `ROUTE_POLICIES` entries (`tailscale_ingress.py` lines 675–717), so they do not depend on the fallback. `test_inventory_matches_both_compositions_and_route_policies` passed. The inventory header states schema head `0035` and names a positive and a negative test id on the new content rows that were inspected (`/api/my/records`, `/api/timeline`, `/api/research-requests`, `/api/admin/research-requests`).

10. Systemd and state-directory correction — established. The service diff adds only `StateDirectoryMode=0700`. `NoNewPrivileges`, `ProtectSystem=strict`, `UMask=0077`, `PrivateTmp`, `ProtectHome=read-only` and the empty capability sets remain. `test_systemd_service_directory_boundaries_are_mutable_state_cache_runtime_only` asserts `StateDirectoryMode == 0700`. The optional credential drop-in is a separate unit fragment; the deployment note says to install it only for an explicitly provisioned deployment. The combined probe run included the 20 tests in `test_fedora_systemd_service.py` and exited 0.

11. Non-regression and classification — established for the authorized gate. The focused subset exited 0 with no failures. `tests/integration/test_process_sigterm_lifecycle.py` changes only the expected Alembic revision from `0034` to `0035`; `CANONICAL_PYTHON = Path("/home/agile/Projects/framenest/.venv/bin/python")` is still present and was not repaired. The broad suite was not run, so the four parked failures were not re-observed and were not edited by this delta.

## Findings

```text
Finding ID: KRONIKA-ONE-PRODUCT-S4B-S7P-REAUDIT-F01
Title: unbounded blockquote recursion crashes document rendering
Status: open
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 74f2a404a4d999407248e07f6ffab325c692722d
Affected component and exact location: src/framenest/application/document_rendering.py:90-94 (flush_quote calls render_markdown); reached from src/framenest/adapters/api/records_api.py:203-206
Security property: bounded handling of untrusted document text
Asset at risk: availability of the render request
Trust boundary: stored question and answer text, including untrusted model output, into the HTML renderer
Attacker-controlled input or local actor: Markdown in a completed document; a nested line of the form "> " repeated 1200 times plus a leaf token
Reachability: GET /api/records/{record_id}/render after read_detail returns a document; the handler does not catch RecursionError
Preconditions: the caller can read that document (owner, administrator, or household member after approval); the text fits the answer byte CHECK (2097152)
Required privileges: ordinary user
Observed or potential impact: render_markdown raises RecursionError. A 50-level nest returns HTML containing the leaf. A 1200-level nest does not return.
C/I/A effect: no confidentiality or integrity change observed; one render call fails
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: probe test_unbounded_quote_nesting_raises_recursion_error, synthetic source ("> " * 1200) + "leaf", pytest.raises(RecursionError), second run exit 0 inside the 30 passed
Static evidence: flush_quote strips one "> " prefix and calls render_markdown on the remainder; no depth counter
Synthetic containment: /tmp/kronika-one-product-verify-74f2a40 mode 0700; removed after the run
False-positive analysis: a successful return of escaped HTML for that 1200-prefix input would disprove it. The 50-level case did return, so the failure is depth, not the quote syntax itself. An outer ASGI conversion to HTTP 500 was not issued.
Exploitability conclusion: demonstrated
Smallest safe correction direction: render quotes iteratively, or stop at a fixed depth and escape the remainder as text; add a regression test inside the answer byte bound
Regression-test requirement: a document whose answer is ("> " * 1200) + "leaf" must return escaped HTML or a sanitized refusal, and must not raise RecursionError
Residual risk: after that bound, a hostile document can still cost CPU up to the cap; it must not exhaust the call stack
Acceptance-blocking decision: non-blocking; the demonstrated effect is a failed render, not a cross-owner read, script execution, or ledger corruption
Redaction requirements: none; the input was synthetic
```

Attribute-injection hypothesis, rejected:

```text
Finding ID: KRONIKA-ONE-PRODUCT-S4B-S7P-REAUDIT-F02
Title: quote inside a Markdown link breaks out of the href attribute
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 74f2a404a4d999407248e07f6ffab325c692722d
Affected component and exact location: src/framenest/application/document_rendering.py:50-52
Security property: attribute containment of untrusted URLs
Asset at risk: browser execution of rendered HTML
Trust boundary: document text to HTML
Attacker-controlled input or local actor: [here](http://example.invalid/"onclick="alert(1))
Reachability: the same render path as F01
Preconditions: a readable document containing that link
Required privileges: ordinary user
Observed or potential impact: none; the quote is encoded
C/I/A effect: none observed
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: probe rendered that source to an href containing &quot;onclick=&quot; and no onclick=" attribute
Static evidence: escape(url, quote=True) on the href
Synthetic containment: same probe root; removed
False-positive analysis: this record is the rejection. A raw onclick=" in the output would have reopened it.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none
Regression-test requirement: the existing test_link_attribute_injection_is_escaped already covers the escaped quote
Residual risk: none from this hypothesis
Acceptance-blocking decision: non-blocking; rejected
Redaction requirements: none
```

## Containment ledger

```text
Temporary root: /tmp/kronika-one-product-verify-74f2a40
Owner: this audit session
Mode: 0700
Contents class: one synthetic pytest module and pytest temp databases under tmp_path
Cleanup owner: this audit session
Cleanup outcome: removed; absence verified
```

No NUC, SSH, sudo, browser, provider, credential or `private/**` action was taken. FrameNest `git status` was empty after cleanup.

## Limitations

Living README, PRODUCT, SPEC, ROADMAP and SECURITY still contain schema-head `0034` sentences. `tests/contract/test_team_alias_api.py::test_schema_head_sentences_are_0034` and `tests/contract/test_adr_0073.py::test_current_schema_head_is_0034` lock that prose and were not part of the 53-path delta. Executable Alembic head assertions in the delta are `0035`.

`build_research_runtime` does not pass `price_schedule`. A saved production request therefore takes the unknown reconciliation path and consumes the reservation. The reconciled-cost path is implemented and covered when a schedule is injected. That is fail-closed for the ledger, not an under-count.

Older-catalogue startup was not booted. The code returns `None` from `recover` on any exception, and returns `None` before `recover` when research is disabled. History routes are still mounted and would query `0035` tables on request.

The HTTP layer was not driven with the 1200-quote document. F01 is demonstrated at `render_markdown`, which the render route calls with the stored text and without a handler guard.

The broad suite was not run.

## Residual risk

F01 stays open. It is low and non-blocking. This audit does not accept it as residual; that decision belongs to the Orchestrator. No medium or higher finding was established. F02 is rejected.

## Orchestration critique

```text
Orchestration critique:
MEASURED: F01 unbounded blockquote recursion; probe RecursionError at 1200 nested "> " prefixes; effect is a failed render; smallest correction is an iterative or depth-capped renderer plus a regression test inside the answer byte bound
LEAD: one synthetic HTTP render of that document, to confirm the ASGI stack returns a bounded 500 rather than killing the worker
```

Resolved Execution Issues / Near-Misses: the first probe assertion treated `&quot;onclick=` inside an href as attribute breakout. The bytes were escaped. The assertion was corrected and the probe re-ran, 30 passed, exit 0. No product file was edited.
Pre-Existing Failure Classification: `tests/integration/test_process_sigterm_lifecycle.py` still hardcodes `/home/agile/Projects/framenest/.venv/bin/python`; this delta changes only its expected revision to `0035`. The four parked broad-suite failures were not re-run and were not modified.

## Authority expiry

This terminal report ends the independent-audit exchange. No correction, publication, deployment or further audit action is authorized by it.
