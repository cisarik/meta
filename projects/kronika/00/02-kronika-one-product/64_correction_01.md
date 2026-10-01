# S9-R Bounded Correction — Close audit findings F-1…F-4 (kronika-one-product, session 64, exchange 02)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 64
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S9-R-CORRECTION-AUDIT-FINDINGS
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: adapter usage/error-path coverage, refresh/snapshot contract regressions, media-shell CAS coordination, exact settings response shape
Recommended context capacity: approximately 1M tokens
Independence required: no

## Continuity and authority renewal

```text
Continuity anchor: terminal implementation-PASS report 64_report_00.md and its
  candidate e8f1c04b289b7bd694d66edba012d288ee41e610
Authority renewal: prior implementation authority expired at that terminal
  report; this exchange grants correction-only authority for findings F-1–F-4
  of the independent audit 65_report_00.md
Evidence posture: non-independent; the corrector never certifies its own change
```

Re-gate before editing: branch `feat/kronika-one-product`, HEAD
`e8f1c04b289b7bd694d66edba012d288ee41e610`, clean index and worktree
including untracked files, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Stop on conflict with retained
context.

## Findings to correct (from `65_report_00.md`, all inside the existing allowlist)

**F-1 (medium) — adapter coverage and the report-attribution defect.**
`_parse_usage` and `_submit_status_error_code` in
`src/framenest/infrastructure/ai/openai_responses.py` have zero test
references; the implementation report attributed such tests to an unchanged
file. Add focused causal regressions in
`tests/unit/infrastructure/ai/test_openai_responses_adapter.py`: missing or
invalid `usage` yields `usage is None` (never a zeroed `ResearchUsage`); a
non-dict details block yields `usage is None`; a submit 404 maps to
`PROVIDER_UNAVAILABLE` while a poll 404 still maps to `RESULT_EXPIRED`; and
the reported `cache_write_tokens` path parses into
`cache_write_input_tokens`. Do NOT edit `64_report_00.md` or any other
historical trace artifact; the correction report records the attribution
defect instead.

**F-2 (medium) — refresh and durable-snapshot regressions.** Add contract
regressions in `tests/contract/test_research_provider_contract.py` and/or
`tests/contract/test_research_completion.py`: build the runtime with a real
disposable engine while research is disabled (via the configuration
provider) and assert it exists; enable via a mutable configuration provider;
admit and complete; then change the model and assert the next admission uses
the new model while the first request keeps its persisted model, schedule and
reconciled cost through a simulated restart. Use fake transports only.

**F-3 (low-medium) — complete the media half of the shared configuration
contract.** In `src/framenest/adapters/api/web/app.js`, make the existing
media-provider read/mutation callers send `If-Match` with the media revision
and consume the returned ETag/revision; a successful media save must
invalidate the research settings revision and a successful research save must
invalidate the media revision, so a dirty sibling draft never silently adopts
a new revision. Add the corresponding coverage in
`tests/ai_providers_admin_frontend.test.js` (media/research revision
coordination). Preserve all existing media behavior and tests; if an existing
test intentionally sends no `If-Match`, keep that path valid (absent header
stays permitted server-side).

**F-4 (low) — exact settings response shape.** In
`src/framenest/adapters/api/ai_admin_api.py`, GET must return exactly the
seven planned fields (no `changed` key; use separate response models or
`exclude_none`), while PUT returns the same representation plus
`changed: boolean`. Add a key-set assertion to
`tests/contract/test_research_settings_api.py`.

No behavior beyond these four items; no other refactor.

## Exact allowlist (7 paths; no additions)

```text
src/framenest/adapters/api/ai_admin_api.py
src/framenest/adapters/api/web/app.js
tests/unit/infrastructure/ai/test_openai_responses_adapter.py
tests/contract/test_research_provider_contract.py
tests/contract/test_research_completion.py
tests/contract/test_research_settings_api.py
tests/ai_providers_admin_frontend.test.js
```

Any required change outside this list is a stop: report it and wait for an
amended grant.

## Negative authority

No other source/test/doc file; no dependency, lockfile, schema, migration,
configuration or AP change; no provider call, credential or real
configuration inspection; no NUC/SSH/sudo; no browser run; no publication,
push, merge, rebase, reset, clean, stash or branch change; no `git add .`/`-A`;
no subagents.

## Validation

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610 --operation test-focus -- tests/unit/infrastructure/ai/test_openai_responses_adapter.py tests/contract/test_research_provider_contract.py tests/contract/test_research_completion.py tests/contract/test_research_settings_api.py tests/contract/test_research_requests_api.py tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js
```

F-1 and F-2 add guard regressions for behavior that already exists on the
current candidate: record that they pass against `e8f1c04…` production code
and label them guard regressions (no Red-first is expected, because no
production behavior is reverted). F-3 and F-4 change client and response
behavior: record the before/after assertions with the new tests. No broad
suite; no browser evidence suite.

## Git authority

Stage only the allowlisted paths by exact path after reviewing the full staged
diff. Create exactly one local commit:

```text
fix(research): close the S9-R audit findings
```

No push. Report the commit SHA, tree and parent; the corrected candidate
remains local and needs a fresh independent re-audit.

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
Downloadable prompt filename: 64_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 64_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on baseline drift, out-of-allowlist need, client Plan
mode being active, an un-clearable failing gate, or any proposal that changes
more than the four findings. Do not self-certify closure; the fresh re-audit is
separate.

## Completion and report contract

PASS means: the four findings are corrected inside the allowlist; the focused
route exits 0 with the new regressions present; one local commit with the
exact subject exists; the report is delivered. Implementation evidence is
non-independent.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 64, 02), and carries the compact core
with exact commands and Red/Green evidence, changed files, commit result
(local only), deviations, smallest next step, `Report justification:
new-mutation`, the attribution-defect record for F-1, critique, and authority
expiry. Save the report exactly at `64_report_01.md` if the client permits;
read back the full content; otherwise preserve it in chat and mark delivery
PARTIAL.

Authority expiry: the terminal report ends this correction grant.
