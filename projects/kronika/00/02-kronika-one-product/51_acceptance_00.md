# Kronika one product — independent E3/R3 audit of the S4-B and S7-P chains (`74f2a40`)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 51
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S4B-S7P-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — independent audit of two unpublished-by-audit runtime/API chains plus a host-deployment correction, with a strict disposition of autonomy-mode evidence; the Cooperator may override.
Recommended context capacity: as large as the client offers (prefer ~1M tokens if exposed).
Independence required: yes — required-fresh-independent.

## Session and independence declaration

This must be a genuinely fresh session that did not implement, correct or plan
any part of the S4-B, S7-P or systemd/state-directory changes and inherits no
implementation reasoning. Prior plans and reports are evidence, not authority.
You do not correct anything: findings are reported, never fixed. No subagents.
Write-capable client, Plan mode OFF. The runtime research provider remains
disabled by default: do not call any live provider, do not read credentials or
`private/**`, and do not touch the NUC.

The chains under audit were implemented by the Orchestrator under the
Cooperator's 2026-09-28 autonomy directive. Their reports are truthful but
non-independent. This exchange is the independent verification the Cooperator
requested before the successor Orchestrator continues.

## Acceptance candidate and owner map

```text
Acceptance candidate: 74f2a404a4d999407248e07f6ffab325c692722d
  (tree 1715bbdb915ef619d81cf1f12a52c09acaa61d7e, branch feat/kronika-one-product,
   parent c0a528880d0184df9d5b65c1ecbc33fee071ee25)
Base of the audited delta: 89a402981a9eac83646199c77984c3fc21c0744d
  (the gate fix audited independently in 43/01 and 45/01; the S6 chains and the
   earlier gate/systemd history are covered by 35/01, 39/01, 43/01 and 45/01)
Audited commits (10):
  3f5dc5c fix(systemd): request 0700 for the framenest state directory
  df44c2d feat(research): add durable research request storage and accounting
  5417fb8 feat(research): persist research requests, slots and budget holds
  a9ec1f1 feat(research): supervise the research lifecycle in the coordinator
  34cb2f5 feat(research): add the OpenAI Responses adapter
  0a7d3f0 feat(research): wire the research runtime inert by default
  8a277a3 feat(records): add record capabilities and safe document rendering
  f1ec367 feat(research): complete research requests into common records
  c0a5288 feat(research): expose research request submission and history APIs
  74f2a40 feat(records): expose history, timeline, render and approval APIs
Audited delta size: 53 paths, +6127/-73.
Plans and amendments (evidence): 47_planning_00.md + its amendment 1;
  49_planning_00.md + its amendment 1; implementation record 48/50;
  autonomy directive entry in 00_notes.md (2026-09-28).
Published state: public main and feat/kronika-one-product both equal
  74f2a40 (non-force fast-forward from 3f5dc5c and 38e7bee respectively).
Acceptance allowlist: read-only review of the candidate, governing AP and the
  named trace evidence; the declared focused route; direct public-ref readback;
  one declared temporary probe root under /tmp/kronika-one-product-verify-74f2a40
  (mode 0700, synthetic data only).
Acceptance independence: required-fresh-independent.
```

## Starting state (verified read-only at issuance, 2026-09-29)

```text
root     /Users/agile/Projects/framenest       (MacBook)
branch   feat/kronika-one-product
HEAD     74f2a404a4d999407248e07f6ffab325c692722d
tree     1715bbdb915ef619d81cf1f12a52c09aa61d7e
status   empty (git status --porcelain --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
public   main 74f2a40…; feat/kronika-one-product 74f2a40…;
         feat/chatgpt-page-ask-kernel 26d28b16…;
         feat/x-meme-browser-companion 7ff6546f…
NUC      web release 89a4029… (older than main; unit fix host-applied);
         capture 94e605c… parked; do not contact.
```

## Fixed claims

1. **Candidate identity, containment and inert-by-default posture.**
   SHA/tree/parent and the ten commits match; the delta contains no
   `private/**`, credential, token or secret-shaped value; no production code
   path performs network I/O at import, construction or ordinary startup; the
   research runtime is constructed only when the non-secret AI configuration
   enables it; `create_app` remains usable with research disabled and with an
   older catalogue; `.ap`, the managed AGENTS block, `pyproject.toml`,
   `poetry.lock`, migrations `0001..0034` and unrelated files are untouched.
2. **Migration `0035` integrity.** The four tables match the frozen design
   (columns, CHECKs, named indexes, FKs to `kronika_records` and
   `research_requests`, unique `(owner_login_key, client_request_id)`);
   empty upgrade/downgrade/re-upgrade works; a populated downgrade refuses
   atomically with the revision still `0035` and no rows dropped; the
   migration-head ripple is complete (all current-head assertions at `0035`,
   including `REQUIRED_PUBLIC_SCHEMA_REVISION` in
   `public_published_application.py`); historical migration targets are not
   rewritten.
3. **Repositories and budget ledger.** Admission is atomic under
   `BEGIN IMMEDIATE`: an exact duplicate client key returns the existing row;
   a different fingerprint raises `E_IDEMPOTENCY_CONFLICT`; a held slot
   raises `E_BUSY`; a refusal leaves no request, no hold and no slot change;
   `save` releases the slot on terminal states; daily/monthly consumption is
   summed per UTC key, retired reservations are replaced by reconciled usage,
   unknown usage consumes the reservation (never zero).
4. **Coordinator lifecycle.** A durable `SUBMITTING` marker precedes the
   provider call; an uncertain outcome or a transport exception, and a
   recovery over a persisted `SUBMITTING` row, produce terminal
   `submission_unknown` with the hold reconciled as unknown and the slot
   released; there is no automatic resubmission; polling maps outcomes and a
   deadline produces terminal `timeout` with a best-effort remote cancel;
   a cancellation committed before result-save prevents finalization;
   a failed completion keeps the request `validating` with its normalized
   checkpoint and a later retry can still reach `saved`; remote cleanup runs
   for terminal rows with a handle.
5. **Adapter boundary.** The OpenAI Responses adapter builds its request body
   only from the server-selected profile (no client endpoint, model or tool
   fields; bounded by the approved prompt limit); a missing credential
   returns `E_NOT_CONFIGURED` with no network call; provider responses are
   parsed within the domain bounds and mapped to stable codes only; a
   completed result is accepted only when `completion_error` is absent; a
   missing remote response maps to `E_RESULT_EXPIRED` and release treats it
   as already deleted; no provider body, credential or reasoning text enters
   errors, logs or responses.
6. **Atomic completion and record binding.** One immediate transaction creates
   the immutable `kronika_documents` row, the `kronika_records` row with the
   server-derived owner of the stored request, and the
   `research_requests.record_id` binding; an exact replay returns the existing
   binding without a second document or record; the coordinator's terminal
   save cannot clobber the binding.
7. **Authorized HTTP surfaces.** Research routes: missing identity 401,
   capability denial 403, foreign and nonexistent indistinguishable 404,
   duplicate submission idempotent, conflicting reuse 409, budget refusal 429,
   a disabled runtime refuses admission with `E_DISABLED` while history reads
   remain available; the administrator inventory requires the administrator
   capability. Records routes: `/api/my/records` is the caller's own history;
   `/api/timeline` contains approved records only; detail serves the current
   state to the owner and administrator and the approved projection to other
   household members; an unapproved private record is the unknown-record body;
   `/render` follows the same authorization and returns escaped HTML with
   `nosniff` and a restrictive CSP; approval is administrator-only, version
   checked (stale version 409) and supports `approve`/`withdraw` (`reject`
   is refused 422 because no rejected state exists).
8. **Rendering and capabilities safety.** The renderer converts only the
   bounded Markdown subset; raw HTML is escaped and never passed through;
   links are emitted only for `http`, `https` and `mailto`; attribute
   injection cannot terminate an attribute; capabilities expose no secret,
   perform no live probe, and report disabled safely.
9. **Route-policy and inventory completeness.** Every new route has a
   matching `ROUTE_POLICIES` entry (no fallback-only route); the regenerated
   `docs/KRONIKA_ACCESS_INVENTORY.md` matches both compositions, names a
   specific positive and negative behavioral test per content route, and its
   header states schema head `0035`; the inventory contract test passes.
10. **Systemd/state-directory correction.** `deploy/systemd/framenest.service`
    carries `StateDirectoryMode=0700` with a contract assertion, consistent
    with the accepted private-catalog rule and the host change recorded in
    `46_report_00.md`; no other unit hardening was weakened.
11. **Non-regression and classification.** A focused security subset is green;
    no unexplained failing gate remains; the pre-existing macOS debt
    (`tests/integration/test_process_sigterm_lifecycle.py` hardcoded
    `/home/agile/...` interpreter path) and the four parked PC-era failures
    are classified, not silently repaired; the broad suite is deliberately
    not run (testing economy directive).

## Fixed controls

Positive controls, from the repository root with the declared route bound to
the candidate:

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git log --oneline -11
git diff --name-status 89a402981a9eac83646199c77984c3fc21c0744d HEAD
git status --porcelain --untracked-files=all
GIT_TERMINAL_PROMPT=0 git ls-remote https://github.com/cisarik/framenest.git

./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 74f2a404a4d999407248e07f6ffab325c692722d

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 74f2a404a4d999407248e07f6ffab325c692722d --operation test-focus -- \
  tests/unit/application/test_research_coordinator.py \
  tests/unit/application/test_document_rendering.py \
  tests/unit/infrastructure/ai/test_openai_responses_adapter.py \
  tests/unit/infrastructure/ai/test_research_registry.py \
  tests/unit/test_identity_access.py \
  tests/contract/test_research_provider_contract.py \
  tests/contract/test_research_completion.py \
  tests/contract/test_research_requests_api.py \
  tests/contract/test_records_api.py \
  tests/contract/test_kronika_record_authorization.py \
  tests/contract/test_kronika_approved_projection.py \
  tests/contract/test_kronika_access_inventory.py \
  tests/contract/test_public_published_uds.py \
  tests/integration/persistence/test_research_requests_migration.py \
  tests/integration/persistence/test_research_request_repository.py \
  tests/integration/persistence/test_kronika_records_migration.py \
  tests/unit/infrastructure/backup/test_catalog_backup.py \
  tests/unit/infrastructure/runtime/test_production_runtime.py \
  tests/contract/test_persistence_cli.py \
  -q -p no:cacheprovider
```

Negative and adversarial controls: synthetic fixtures and one declared
temporary probe root (`/tmp/kronika-one-product-verify-74f2a40`, mode 0700,
removed after use). Cover at least:

- Migration: populated-downgrade refusal retains rows and revision `0035`;
  malformed rows are rejected by the named CHECKs.
- Store: a second admission while the slot is held returns `E_BUSY`; a
  conflicting client key returns `E_IDEMPOTENCY_CONFLICT`; a budget refusal
  rolls everything back; unknown reconciliation consumes the reservation.
- Coordinator: with fakes, `SUBMITTING` persists before the provider call;
  an exception during submit yields `submission_unknown`, not a retry; a
  late completion cannot finalize a cancelled request; deadline yields
  `timeout`.
- Adapter: no body field can introduce a client endpoint/model/tool; a
  missing credential cannot call the fake transport; an oversized or
  malformed completion cannot reach `COMPLETE`.
- HTTP: anonymous denial on every new route; cross-owner denial is the same
  body as unknown; a household member cannot read an unapproved private
  document; the rendered HTML never contains raw `<script>` or a
  `javascript:` href; approval with a stale version conflicts.
- Leak hunt over the 53-path delta: no credential, token, secret-shaped
  value, raw provider payload, document text in errors, host address or
  private path.

State every observed result with exact evidence; unverified controls are
never PASS. Findings use the full INFOSEC finding structure (evidence class,
reachability, preconditions, privilege, impact, containment, residual risk).

## Authority and containment

Positive authority: read-only inspection of the candidate, governing `.ap`
and the named trace evidence; the declared focused route; direct public-ref
readback; one declared temporary synthetic probe root; the terminal report
write at the exact destination.

Negative authority: no product/test/doc/config/AP/packaging edit; no
correction; no NUC contact, SSH, sudo, service, browser, provider or
credential action; no live provider call; no push; no new dependency; no
subagent; no `private/**`; no Meta commit.

## Stopping conditions

Stop with `PARTIAL`/`BLOCKED` on identity or git-state mismatch, an unusable
route, a probe exceeding authorized effects, sensitive output, or a control
that cannot be established without a forbidden mutation. Preserve the first
causal failure; missing evidence is never PASS.

## Evidence selection

```text
Evidence tier: E3
Evidence tier basis: security/trust boundaries (research runtime, records HTTP authorization, safe rendering, private catalog) plus durable migration 0035
Activated stricter profile: INFOSEC.md — R3 route (fresh focused audit)
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the selected subset above
Affected tests: the 53-path audited delta
New causal regression: none — this is acceptance
Broad or full suite: not-used — do not run (testing economy; the Cooperator may order otherwise)
Runtime or testbed: declared route plus the declared synthetic probe root; no NUC
Independent acceptance: required-separate-fresh-worker (this exchange)
```

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a
PASS; otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: final-acceptance`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 51, exchange 01) exactly once. Include the
compact core; the completed acceptance record; per-claim verdicts with exact
evidence; the control matrix with counts and exit codes; findings with the
full structure; containment and cleanup; residual risk and limitations; one
smallest next step (the successor Orchestrator's handout reconciliation and
S8); the critique block; and the authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. If the report write is blocked by the client,
preserve the complete content in the client output and report the missing
delivery truthfully. Terminal report or cancellation expires this authority.

## Trace and delivery record

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
Downloadable prompt filename: 51_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 51_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
