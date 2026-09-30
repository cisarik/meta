# S9-R Independent Audit — Exact Candidate e8f1c04 (kronika-one-product, session 65)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 65
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S9-R-AUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — independent acceptance of a large accounting-, concurrency- and authorization-bearing slice
Recommended context capacity: approximately 1M tokens
Independence required: yes

## Acceptance and Correction Record

```text
Acceptance candidate: e8f1c04b289b7bd694d66edba012d288ee41e610
  (tree 1cbf6739083e7459b1d5e5011dbd72fed77e5d69, branch feat/kronika-one-product,
   parent 3bf424586289b500cf45cb0d49676b50d27328fa)
Acceptance owner map: delta 3bf424586289b500cf45cb0d49676b50d27328fa..e8f1c04b289b7bd694d66edba012d288ee41e610
  (one commit, 37 changed paths); the frozen plan 62_report_01.md (SHA-256
  971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325),
  the model evidence 63_report_00.md and the implementation report
  64_report_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused route; no
  temporary root is required and none is granted; no mutation
Acceptance risk claims: V1–V12 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: the report-attribution discrepancy in V11
Out-of-scope observations: ledger-candidates
```

This session did not implement, plan or correct the slice. Reports are claims;
verify them. No correction authority is granted.

## Security audit record

```text
Security task class: focused defensive audit (R3), with authorization,
  accounting-integrity and shared-configuration specializations
Owned/authorized target: /Users/agile/Projects/framenest at the candidate,
  read-only
Commit under audit: e8f1c04b289b7bd694d66edba012d288ee41e610
Scope: the one-commit delta from 3bf424586289b500cf45cb0d49676b50d27328fa,
  against the frozen plan 62_report_01.md sections 2–8
Exclusions: NUC, SSH, sudo, browser launch, live provider, credentials, real
  configuration inspection, private/**, broad Python suite, correction
```

Threat model: assets are the administrator settings boundary, versioned
pricing/accounting correctness, admission idempotency and the shared
non-secret AI configuration file. Attacker-controlled inputs: authenticated
admin JSON, settings revisions/If-Match, client request ids, stored usage
values from provider responses, concurrent writers. Security properties:
verified-identity authorization, fail-closed unknown accounting, no client
model selection, immutable admitted pricing, single generation claim, CAS
without lost updates, no secret exposure.

## Claims and required verdicts

**V1 — Candidate identity and containment.** HEAD/tree/parent exact; branch
clean including untracked; the 37 changed paths are a subset of the frozen
44-path allowlist; no path outside it; no push (public refs still `3bf4245…`);
AP pin `73e20ef8…` unchanged.

**V2 — Model catalog and pricing.** `research_models.py` holds exactly the
four confirmed entries with the plan §2 rates (short/long/cache-write, web
search 10,000,000/thousand), threshold 272,000, Sol `valid_until`
2026-11-22T00:00:00Z; the three fixed-model equality checks are replaced;
unknown/alias/arbitrary models are refused before persistence, reservation or
provider contact; no network discovery.

**V3 — Accounting integrity.** Extend `ResearchUsage`/schedule/`UsageTokenPrices`
as planned; per-component ceil integer math; `R + W ≤ I` and `reasoning ≤ O`
validation; no `_int_or_zero` zero-filling; missing/invalid usage is unknown
(never zero); missing GPT-5.6 cache-write is unknown; GPT-5.5 stays derivable
without fabricating a count; the arithmetic fixtures (Luna short 22,990, Luna
long 127,000, boundaries 272,000/272,001) hold; legacy `"3"` requests keep the
2026-09-26 flat schedule with unknown long-tier accounting; restarts resolve
pricing from the persisted identity, not the current selection; unknown/overrun
states block further generation without clamping or losing output.

**V4 — Runtime and enable/disable.** A persistent coordinator is built when the
catalog engine exists (including disabled start); admission and capabilities
read a fresh validated configuration; saving settings does not replace the
coordinator or rerun recovery; disabling stops new admissions/submission claims
but preserves history, polling, cancellation and cleanup; re-enabling needs no
restart; admitted snapshots are unchanged.

**V5 — Idempotency and single attempt.** `(owner, client_request_id)` lookup
precedes configuration/enablement/credential checks; version-2 fingerprint
over owner, kind, prompt, consent only; identical replay returns the original
attempt after model/budget/enablement changes; changed content conflicts; the
admission receipt gates the submission nudge; the atomic `ADMITTED →
SUBMITTING` claim admits exactly one provider creation.

**V6 — Shared configuration CAS.** `load_ai_server_config_snapshot` revision
semantics (SHA-256 of bounded raw bytes; absent = `"absent"`); process + OS
advisory locks; CAS with creation-only direct writes; stale `If-Match`/wildcard
409 without writing; research-settings PUT requires `If-Match`; revision/ETag
delivered on the media-provider read/mutation surfaces and honoured by CLI
saves; the preservation assertion holds for supported normalized values in both
directions (not byte-for-byte formatting).

**V7 — Admin API.** `GET`/`PUT /api/admin/ai/research-settings` exist with
verified identity plus `provider.operate`; workspace composition only; explicit
ingress policies and the `ai.research.settings.update` audit action with
audit-failure refusal; six required PUT fields and the exact bounds; the
required GET/PUT response shapes; `no-store`; the stable error table; no
probe/generation/secret; absent-config refusal; missing-credential disabled
edits without enabling; the regenerated inventory lists both routes.

**V8 — Shell.** The Research settings section exists inside the administrator
AI dialog with the required copy, confirmation for model/budget changes,
stale-revision and uncertain-save handling, identity-loss clearing, accessible
labels/status, strict USD-to-micro-USD conversion without float rounding, and
no Gallery/Details restyle; the new JS suite covers these.

**V9 — Documentation.** ADR-0084 exists with the confirmed decision, schedule
tables, Sol expiry policy and immutable-pricing rules; ADR-0083 carries the
partial-supersession notice; SPEC/SERVER/AGENTS deltas are consistent; README/
PRODUCT/ROADMAP reconciliation does not claim unperformed acceptance or NUC
observations.

**V10 — Recorded deviations.** Assess the three deviations in
`64_report_00.md` §6 against the frozen plan: (a) media-provider `If-Match`
optional (absent header keeps prior behavior) while research PUT requires it;
(b) Sol cutoff enforced at admission and PUT enabling, not in selection; (c)
legacy over-threshold unknown accounting. State whether each is acceptable
within the plan or requires a finding.

**V11 — Report attribution check (named missing-evidence probe).**
`64_report_00.md` §4 states that “strict usage parsing and submit-404
distinction” tests were added to
`tests/unit/infrastructure/ai/test_openai_responses_adapter.py`, but that file
is unchanged in the delta. Determine where the required causal coverage for
“missing/invalid usage never becomes zero” and “model refusal during creation
vs expired remote result during polling” actually lives, or whether it is
missing; record the exact evidence and whether the report’s attribution is a
reporting defect, a coverage gap, or both. This is a named probe, not an
expansion: do not audit beyond it.

**V12 — Non-regression.** Independently re-run the declared focused route on
the exact candidate (15 Python files; the three JS files; totals) and
`git diff --check`; inspect the regenerated inventory diff; no broad suite.

## Controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}' HEAD^; git status --porcelain --untracked-files=all
git diff --name-status 3bf424586289b500cf45cb0d49676b50d27328fa..HEAD; git show e8f1c04b289b7bd694d66edba012d288ee41e610
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main refs/heads/feat/kronika-one-product
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610 --operation test-focus -- tests/unit/infrastructure/ai/test_ai_configuration_storage.py tests/unit/infrastructure/ai/test_research_registry.py tests/unit/infrastructure/ai/test_openai_responses_adapter.py tests/unit/infrastructure/ai/test_research_models.py tests/unit/infrastructure/ai/test_registry.py tests/unit/application/test_research_coordinator.py tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_ai_server_composition.py tests/contract/test_research_settings_api.py tests/contract/test_research_requests_api.py tests/contract/test_research_provider_contract.py tests/contract/test_research_completion.py tests/contract/test_kronika_access_inventory.py tests/integration/persistence/test_research_request_repository.py -q -p no:cacheprovider

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js
```

Use the exact full SHAs where the prompt shows abbreviating ellipses outside
command lines. Fake transports only; no provider/credential/NUC actions; no
repository mutation; no temporary probe root is granted (none is needed for a
read-only code and test audit).

## Verdict rules and report contract

All V1–V12 established (or V10/V11 dispositions recorded with findings where
required) yields `acceptance-PASS`; otherwise `PARTIAL` or `BLOCKED` with the
exact missing evidence. Findings use the full finding record; out-of-scope
observations become non-authorizing ledger candidates. This audit never
repairs.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 65, 01), and includes the compact core,
the Acceptance record, per-claim verdicts with evidence, the control matrix
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
Downloadable prompt filename: 65_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 65_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed gate, unexplained divergence, any need to
mutate the repository, a required read that would expose secrets or real
configuration, or a finding requiring correction authority.

Authority expiry: the terminal report ends this audit exchange.
