# S9-P3-F01 Bounded Correction — Automatic remote cleanup on research nudges (kronika-one-product, session 60)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 60
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S9-P3-F01-CLEANUP
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: provider-boundary DELETE calls triggered from the API nudge path; no unbounded loops, no response-shape change
Recommended context capacity: approximately 250k tokens
Independence required: no

## Confirmed defect (the only authorized change)

During the P3 live acceptance the two saved requests remained
`cleanup_state: pending`: `ResearchCoordinator.release_remote_pending()` is
implemented and unit-tested but has **no production caller**. The research API
nudge blocks call only `submit_pending()` / `poll_once()`, so provider-side
responses are never deleted after a validated local save, contradicting the
accepted design (“delete the remote response after validated local
persistence”). The two P3 responses were deleted once manually with the
designed method; the defect is the missing automatic call.

## Required correction

1. In `src/framenest/adapters/api/research_api.py`, extend the two existing
   nudge blocks (the successful-admission path in the POST handler and the
   detail GET handler) to also call `runtime.release_remote_pending()`:
   - inside the same `try`/`except Exception: pass` guard used by the existing
     nudge, after `submit_pending()` / `poll_once()`;
   - when the runtime is `None`, behavior is unchanged.
2. No other behavior change: response shapes, status codes, capability checks,
   admission, polling cadence, and cancel semantics stay exactly as today.
   The cleanup loop’s existing bound (`limit=20`) and per-row failure handling
   are unchanged.
3. Add one causal regression in
   `tests/contract/test_research_requests_api.py` that fails on the parent and
   passes after the correction: a terminal `saved` request with a remote
   handle and `cleanup_state` `pending` must transition to `deleted` after a
   normal research API interaction through the nudge path (use the existing
   synthetic app/runtime patterns; assert the fake provider recorded the
   release call exactly once per row and that no release is attempted when the
   runtime is disabled/absent). Record the Red/Green evidence.

## Exact allowlist (2 paths; no additions)

```text
src/framenest/adapters/api/research_api.py
tests/contract/test_research_requests_api.py
```

Any required change outside this list is a stop: report it and wait for an
amended grant.

## Negative authority

No other source or test file; no schema, migration, configuration, dependency,
lockfile, AP or managed-block change; no provider call from tests (fake
transport only); no credentials or secret reads; no NUC/SSH/sudo; no
publication, push, fetch, merge, rebase, reset, clean, stash or branch change;
no `git add .`/`-A`; no subagents. Research stays disabled by default in tests.

## Validation (declared route)

Repository gate: root `/Users/agile/Projects/framenest`, branch
`feat/kronika-one-product`, HEAD `a3687505eb12359c76f85661e51e36d7e4778fc9`,
clean index and worktree, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Stop on unexplained divergence.

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline a3687505eb12359c76f85661e51e36d7e4778fc9

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline a3687505eb12359c76f85661e51e36d7e4778fc9 --operation test-focus -- tests/contract/test_research_requests_api.py tests/contract/test_research_completion.py tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider
```

No broad suite; no JS tests; no live provider calls.

## Git authority

Stage only the two allowlisted paths by exact path after reviewing the full
staged diff. Create exactly one local commit:

```text
fix(research): release remote responses on research API nudges
```

No push. Report the commit SHA and tree; the candidate remains local. A scoped
fresh verification and the deployment are separate later steps.

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
Downloadable prompt filename: 60_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 60_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on baseline drift, out-of-allowlist need, client Plan
mode being active, an un-clearable failing gate, or any proposal that changes
more than the two nudge blocks. Do not self-certify closure of the finding;
the verification is separate.

## Completion and report contract

PASS means: the two nudge blocks call `release_remote_pending()` inside the
existing guards; the causal test is Red on the parent and Green after; the
focused route exits 0; one local commit with the exact subject exists; the
report is delivered. Implementation evidence is non-independent.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 60, 01), and carries the compact core
with exact commands and Red/Green evidence, changed files, commit result
(local only), deviations, smallest next step, `Report justification:
new-mutation`, critique, and authority expiry. Save the report exactly at
`60_report_00.md` if the client permits; read it back fully; otherwise
preserve it in chat and mark delivery PARTIAL.

Authority expiry: the terminal report ends this correction grant.
