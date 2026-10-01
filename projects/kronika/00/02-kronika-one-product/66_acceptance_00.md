# S9-R Fresh Independent Re-Audit — Corrected Candidate 2af8edd (kronika-one-product, session 66)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 66
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S9-R-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — full fresh re-acceptance of the corrected accounting-, concurrency- and authorization-bearing slice
Recommended context capacity: approximately 1M tokens
Independence required: yes

## Acceptance and Correction Record

```text
Acceptance candidate: 2af8edde5faf8967777a68b0a72685cc580c45ea
  (tree 3f6367cf2da9224eebefb7659ca0efb8ae7d54e0, branch feat/kronika-one-product,
   parent e8f1c04b289b7bd694d66edba012d288ee41e610)
Acceptance owner map: delta 3bf424586289b500cf45cb0d49676b50d27328fa..2af8edde5faf8967777a68b0a72685cc580c45ea
  (two commits, 37+6 changed paths); the frozen plan 62_report_01.md
  (SHA-256 971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325),
  the model evidence 63_report_00.md, the audit 65_report_00.md and the
  correction 64_report_01.md are evidence only
Acceptance allowlist: read-only review; the declared focused route; no
  temporary root is required and none is granted; no mutation
Acceptance risk claims: R1–R7 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none beyond the claims below
Out-of-scope observations: ledger-candidates
```

This session did not implement, audit or correct this slice. Reports are
claims; verify them. No correction authority is granted.

## Claims and required verdicts

**R1 — Candidate identity and containment.** HEAD/tree/parent exact; clean
including untracked; the second commit touches exactly six of the seven
allowlisted paths (`ai_admin_api.py`, `app.js`,
`test_openai_responses_adapter.py`, `test_research_provider_contract.py`,
`test_research_settings_api.py`, `ai_providers_admin_frontend.test.js`;
`test_research_completion.py` untouched is permitted by the grant's
“and/or”); the full delta stays inside the frozen 44-path allowlist; no push
(public refs still `3bf4245…`); AP pin unchanged.

**R2 — F-1 corrected.** New regressions in
`test_openai_responses_adapter.py` actually exercise `_parse_usage` and
`_submit_status_error_code`: reported `cache_write_tokens` parses; absent
write detail stays `None`; missing/invalid `usage` yields `usage is None`
(never a zeroed value; non-dict details, negative counts, booleans,
`R > I`, `R + W > I`); submit 404 maps to `PROVIDER_UNAVAILABLE` while poll
404 maps to `RESULT_EXPIRED`. Verify the tests call the real adapter with a
fake transport and that no production behavior changed in this commit for
these paths. Verify the attribution defect is recorded in
`64_report_01.md` and that `64_report_00.md` was not rewritten.

**R3 — F-2 corrected.** The new contract regression builds the runtime with a
real disposable migrated engine while research is disabled, enables through a
mutable configuration provider without restart, admits and completes, changes
the model, and asserts the next admission uses the new model while the first
request keeps its persisted model, schedule and reconciled cost after a
simulated restart. Verify the test genuinely exercises the production
`configuration_provider` composition path and fake transports only.

**R4 — F-3 corrected.** In `app.js`, the media provider list read captures the
revision; `saveAiProviderRecord`, `deleteAiProvider` and `activateAiProvider`
send `If-Match` only when a revision was captured, consume the returned ETag,
and invalidate the research revision on success; a research save invalidates
the media revision and refuses to send `If-Match: ""`; the non-mutating ping
path is unchanged. **Read the four mutation functions and the ping closely
for mis-targeted edits of the kind the correction report records as a
near-miss** (a corrupted ping body/copy; an `activateAiProvider` identifier
error). Verify the new JS coverage actually asserts the headers and both
invalidation directions. Server-side optional `If-Match` for media remains
permitted.

**R5 — F-4 corrected.** GET research-settings returns exactly the seven planned
top-level fields (no `changed`); PUT returns those plus `changed: boolean`;
the key-set assertions exist and cover the six writable settings keys.

**R6 — Non-regression.** Independently re-run the declared focused route on the
exact corrected candidate and reproduce the totals; `git diff --check`; no
broad suite.

**R7 — Residual disposition.** State whether ledger candidates L-1…L-4 from
`65_report_00.md` (cached-tokens-missing semantics; disabled PUT storing an
expired model; dirty-draft discard/uncertain-save advisory text; confirmation
not listing reservations) remain acceptable non-authorizing observations or
require a finding; state whether the correction's own deviations (untouched
`test_research_completion.py`) are acceptable. No expansion beyond these.

## Controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}' HEAD^; git status --porcelain --untracked-files=all
git diff --name-status 3bf424586289b500cf45cb0d49676b50d27328fa..HEAD; git show 2af8edde5faf8967777a68b0a72685cc580c45ea
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main refs/heads/feat/kronika-one-product
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 2af8edde5faf8967777a68b0a72685cc580c45ea

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 2af8edde5faf8967777a68b0a72685cc580c45ea --operation test-focus -- tests/unit/infrastructure/ai/test_ai_configuration_storage.py tests/unit/infrastructure/ai/test_research_registry.py tests/unit/infrastructure/ai/test_openai_responses_adapter.py tests/unit/infrastructure/ai/test_research_models.py tests/unit/infrastructure/ai/test_registry.py tests/unit/application/test_research_coordinator.py tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_ai_server_composition.py tests/contract/test_research_settings_api.py tests/contract/test_research_requests_api.py tests/contract/test_research_provider_contract.py tests/contract/test_research_completion.py tests/contract/test_kronika_access_inventory.py tests/integration/persistence/test_research_request_repository.py -q -p no:cacheprovider

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js
```

Fake transports only; no provider/credential/NUC actions; no repository
mutation; no temporary probe root granted.

## Verdict rules and report contract

All R1–R7 established (with R7 dispositions recorded) yields
`acceptance-PASS`; otherwise `PARTIAL` or `BLOCKED` with the exact missing
evidence. Findings use the full finding record; out-of-scope observations
become non-authorizing ledger candidates. This re-audit never repairs.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 66, 01), and includes the compact core,
the Acceptance record, per-claim verdicts with evidence, control-matrix
results, limitations, residual risk, critique and authority expiry. Use
`Phase-qualified result: acceptance-PASS | not-applicable`,
`Logical-whole closure: not-closed`, `Report justification: final-acceptance`.

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
Downloadable prompt filename: 66_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 66_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed gate, unexplained divergence, any need to
mutate the repository, a required read that would expose secrets or real
configuration, or a finding requiring correction authority.

Authority expiry: the terminal report ends this re-audit exchange.
