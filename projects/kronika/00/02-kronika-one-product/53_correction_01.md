# S8 Bounded Correction Grant — F01 reload recovery (kronika-one-product, session 53, exchange 02)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 53
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S8-CORRECTION-F01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: submission idempotency across reload recovery; small surface but a billing-adjacent guarantee
Recommended context capacity: approximately 250k tokens
Independence required: no

## Continuity and authority renewal

```text
Continuity anchor: terminal implementation-PASS report 53_report_00.md for
  task KRONIKA-ONE-PRODUCT-S8-IMPLEMENTATION (commit
  7f7aae9012d35671b062c8731e9009169501d4d0)
Authority renewal: prior implementation authority expired at that terminal
  report; this exchange grants correction-only authority for accepted finding
  KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Evidence posture: non-independent; the corrector never certifies its own change
```

Re-gate the repository and environment before editing: branch
`feat/kronika-one-product`, HEAD `7f7aae9012d35671b062c8731e9009169501d4d0`,
tree `17a559dff621882ac561a9901d20fe5b824508c4`, clean index and worktree
including untracked files, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Stop on conflict between retained
context and the current repository. Retained context is convenience, not
authority.

## Accepted finding (the only authorized defect)

`KRONIKA-ONE-PRODUCT-S8-AUDIT-F01` (medium, reproduced-dynamic, blocking for
C7): after a lost POST response and a page reload, the shell's recovery path
restores the stored `client_request_id` into memory, but the next submit
recomputes nothing against the stored SHA-256 fingerprint; `kronikaFreezeAttempt`
sees no matching in-memory prompt and mints a new id. Re-entering the same
question, checking consent and submitting therefore POSTs a different
`client_request_id`, defeating server idempotency and risking a second provider
admission and budget use. Full record: `54_report_00.md`, section "Finding".

**Smallest safe correction direction (binding):** on submit after recovery,
recompute the fingerprint over the current login, kind, exact prompt and consent
version; reuse the stored id only when the stored fingerprint is non-empty and
equals the recomputed one; otherwise mint a new id. Keep the prompt out of
storage. Do not auto-submit.

## Required behavior

1. Recovery still restores the stored id into the in-memory attempt and keeps
   the current user-facing recovery copy.
2. On submit (both the same-page path and the post-reload path), the frozen
   attempt id is reused only when a fresh fingerprint over
   `kronikaLogin()`, kind, exact prompt and `KRONIKA_CONSENT_VERSION` equals the
   stored non-empty fingerprint from `kronika.research.attempt.v1`.
3. When the recomputed fingerprint differs, when the stored fingerprint is
   missing or empty, or when no fingerprint can be computed (no
   `crypto.subtle`), mint a new id as today (fail-closed).
4. Preserve every existing guarantee: no prompt or answer text in storage; no
   automatic submit or replay; consent still required on every submit; the
   same-page retry (`kronikaRetrySubmission`) still reuses the frozen attempt;
   a changed question on the same page still mints a new id; a stored
   `operationId` still routes the user to History without a retry offer; the
   persisted record still carries only id, fingerprint and operationId.
5. No other behavior change in the shell, the API adapters, the record
   projections or the docs.

## Exact allowlist (2 paths; no additions)

```text
src/framenest/adapters/api/web/app.js
tests/kronika_ui.test.js
```

Any required change outside this list is a stop: report it and wait for an
amended grant.

## Required causal regression (Red first)

Add to `tests/kronika_ui.test.js` one new `node:test` case that fails on the
current candidate (Red) and passes after the fix (Green), following the
existing harness style (production shell slice via `vm`, stubbed fetch, shared
session storage across two fresh contexts):

- Context A: submit a synthetic question; the POST throws (lost response).
  Storage holds `{id, fingerprint, operationId: ""}` with no prompt text.
- Context B: a fresh context over the same storage map; `kronikaLogin` returns
  the same identity; open the form (recovery offer runs), re-enter the exact
  same question, check consent, submit with an observable POST.
- Assert: the second POST carries the **same** `client_request_id` as the
  first, and the same prompt/consent body; no automatic submit occurred.
- Negative in the same case or a second case: a changed question in context B
  mints a new id; a different login in context B mints a new id.
- Support the shared-storage requirement with an explicit harness option (test
  code only); do not change production code to make the test pass.

The existing `submission retries keep the attempt id until the question
changes` test must stay green unchanged.

## Validation

Repository gate as above, then:

```text
node --test tests/kronika_ui.test.js
```

Red on the parent commit (record the exact failing assertion), Green on the
corrected candidate. Then one bounded run:

```text
node --test tests/kronika_ui.test.js tests/gallery_details_playback_handoff.test.js tests/tailscale_identity_frontend.test.js tests/metadata_form_contract.test.js
```

Repository route (once, for provenance):

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 7f7aae9012d35671b062c8731e9009169501d4d0
```

No Python test run is required (no Python file changes). No broad suite. No
browser launch, no NUC, no sudo, no provider.

## Git authority

Stage only the two allowlisted paths by exact path after reviewing the full
staged diff. Create exactly one local commit:

```text
fix(kronika): reuse the frozen request id across reload recovery
```

No fetch, push, merge, rebase, reset, clean, stash, force operation or branch
change. Report the commit SHA and tree; the corrected candidate remains local.

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
Downloadable prompt filename: 53_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 53_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on baseline drift, out-of-allowlist need, a change in
scope beyond F01, an un-clearable failing gate, client Plan mode being active
(write capability is required), or a second equivalent blocker. Do not weaken
or delete existing tests; do not fix unrelated pre-existing issues.

## Completion and report contract

PASS means: the correction is implemented inside the allowlist; the new
regression is Red on the parent and Green on the corrected candidate; the
bounded JS run exits 0; one local commit with the exact subject exists; and the
terminal report is delivered. Implementation evidence is non-independent.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 53, 02), and carries the compact core:
status; `Phase-qualified result: implementation-PASS | not-applicable`; start
commit `7f7aae9…` and end commit (the correction commit); changed files; tests
with exact commands, Red and Green evidence; commit result (local only);
deviations and missing evidence; smallest next step; `Report justification:
new-mutation`; critique; issues or none; `Logical-whole closure: not-closed`;
authority expiry. Also state explicitly that F01 closure is not self-certified
and that a fresh independent re-audit follows.

Save the report exactly at `53_report_01.md` if the client permits; read back
the full content and verify first line, coordinates and path; otherwise
preserve the complete content in chat and mark the delivery limitation PARTIAL.
Send a short separate completion notice with status, location and SHA-256.

Authority expiry: the terminal report ends this correction grant; a fresh
independent re-audit of the corrected candidate is required next (runtime
behavior changed); no publication or deployment is authorized here.
