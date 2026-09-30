# S9-P1 Implementation Grant — Price-schedule reconciliation wiring (kronika-one-product, session 58)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 58
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S9-P1-PRICE-WIRING
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: monetary accounting correctness at the provider boundary; small surface
Recommended context capacity: approximately 250k tokens
Independence required: no

## Implementation authority record

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 5eddb81bd164207a86f23b3f236e36b66192930b
Changed-path allowlist: the four exact paths in "Exact allowlist" below
Implementation boundaries: the positive and negative authority in this grant
Independence required: no
```

## Goal (one coherent outcome)

Wire the documented, accepted usage price schedule into the production
research composition so that a completed provider result reconciles to a
calculated cost (`accounting_state: reconciled`) instead of today's
fail-closed `unknown`. This is the known S4-B deferral: `build_research_runtime`
constructs `ResearchCoordinator` without `price_schedule`, and
`ResearchCoordinator._reconcile` stores the reservation as `unknown` when no
schedule is present.

Accepted sources: `25_report_00.md` section 3 (rates retrieved 2026-09-26) and
section 4 (reconciliation rules: never count cache twice, never add reasoning
twice, never treat missing usage as zero, never cap recorded cost); the
documented model is `gpt-5.5-2026-04-23`. Documented rates: input USD 5 per
million tokens, cached input USD 0.50 per million, output USD 30 per million,
web search USD 10 per 1,000 calls. Prices must be revalidated before live
activation (that revalidation belongs to the later live-acceptance step, not to
this grant).

## Required implementation

1. Add one named module-level `UsagePriceSchedule` constant in
   `src/framenest/infrastructure/ai/openai_responses.py` (the OpenAI
   Responses adapter module) carrying the four rates as integer micro-USD:
   input `5_000_000`, cached input `500_000`, output `30_000_000`, web search
   per thousand `10_000_000`. Use a date-qualified name
   (`OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26`) and a docstring naming the
   source, the retrieval date and the revalidation-before-live-use
   requirement. No configuration plumbing, no env key, no new file.
2. Pass that schedule in `build_research_runtime` when constructing
   `ResearchCoordinator` (keyword `price_schedule`). Construction stays
   inert-by-default, network-free, and credential-free; disabled or
   unconfigured research is unchanged.
3. Tests:
   - Pin the four rates of the constant (exact integer values).
   - One causal reconciliation test through the production composition:
     construct the runtime via `build_research_runtime` over a disposable
     synthetic SQLite engine with a fake transport (reuse the existing
     fake-transport and repository patterns), drive one bounded synthetic
     request to a completed result with usage, and assert the budget hold
     reconciles with `usage_cost_micro_usd(usage, schedule)` and
     `accounting_state: reconciled` (no cache double count, no reasoning
     add-on). This test must fail on the parent commit (where the state is
     `unknown`) and pass after the wiring; record the Red/Green evidence.
   - Keep existing assertions that disabled research stays inert and that no
     network call occurs.
4. No behavioral change beyond the schedule wiring; no change to admission,
   budgets, deadlines, cancellation, cleanup or the migration.

## Exact allowlist (4 paths; no additions)

```text
src/framenest/infrastructure/ai/openai_responses.py
src/framenest/adapters/api/application.py
tests/contract/test_research_provider_contract.py
tests/unit/infrastructure/ai/test_openai_responses_adapter.py
```

Any required change outside this list is a stop: report it and wait for an
amended grant. The rate-pinning test belongs in one of the two allowlisted
test files; the causal composition test belongs in
`tests/contract/test_research_provider_contract.py`.

## Negative authority

No dependencies, lockfiles, migrations, configuration or environment changes,
AP pin or managed-block changes; no other source file; no live provider call,
network call in tests, credential handling or secret read; no NUC/SSH/sudo;
no browser/server launch; no publication, push, fetch, merge, rebase, reset,
clean, stash or branch change; no `git add .`/`-A`; no subagents. Research
remains disabled by default; do not enable anything.

## Validation (declared route; testing economy binding)

Repository gate: root `/Users/agile/Projects/framenest`, branch
`feat/kronika-one-product`, HEAD `5eddb81bd164207a86f23b3f236e36b66192930b`,
clean index and worktree, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Stop on unexplained divergence.

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 5eddb81bd164207a86f23b3f236e36b66192930b

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 5eddb81bd164207a86f23b3f236e36b66192930b --operation test-focus -- tests/contract/test_research_provider_contract.py tests/unit/application/test_research_coordinator.py tests/unit/infrastructure/ai/test_openai_responses_adapter.py tests/integration/persistence/test_research_request_repository.py -q -p no:cacheprovider
```

Red first on the parent for the new causal test (record the exact failing
assertion), then Green after the wiring. No broad suite; no JS tests; no live
service.

## Git authority

Stage only the allowlisted paths by exact path after reviewing the full staged
diff. Create exactly one local commit:

```text
feat(research): reconcile usage with the documented price schedule
```

No push. Report the commit SHA and tree; the candidate remains local.

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
Downloadable prompt filename: 58_implementation_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 58_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on baseline drift, out-of-allowlist need, client Plan
mode being active (write capability required), an un-clearable failing gate,
or a finding that the schedule cannot be wired without a design change. Do not
enable research; do not touch credentials.

## Completion and report contract

PASS means: the schedule constant exists with the exact rates; the production
composition passes it; the rate pin and the causal reconciliation test are
Red-then-Green; the focused route exits 0; one local commit with the exact
subject exists; the report is delivered. Implementation evidence is
non-independent.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 58, 01), and carries the compact core
with exact commands and Red/Green evidence, changed files, commit result
(local only), deviations, smallest next step, `Report justification:
new-mutation`, critique, and authority expiry. Save the report exactly at
`58_report_00.md` if the client permits; read it back fully; otherwise
preserve it in chat and mark delivery PARTIAL.

Authority expiry: the terminal report, cancellation or supersession ends this
grant. Publication and live activation are separate grants.
