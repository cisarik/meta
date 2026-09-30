# S8 Fresh Independent Re-Audit — Corrected Candidate ef99203 (kronika-one-product, session 55)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 55
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S8-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — full fresh re-acceptance of a corrected runtime-behavior candidate covering access-sensitive projections, identity echo, submission idempotency and rendering isolation
Recommended context capacity: approximately 1M tokens
Independence required: yes

## Acceptance and Correction Record

```text
Acceptance candidate: ef9920333013f3f70bf5e3443be2e51814f6b9c3
  (tree e4338c2f31e8aff2829351ec107e2d75a165a473, branch feat/kronika-one-product,
   parent 7f7aae9012d35671b062c8731e9009169501d4d0)
Acceptance owner map: delta ade1169b4ba079bb1df540a929572ca58e777d16..ef9920333013f3f70bf5e3443be2e51814f6b9c3
  (two commits, 20 paths, +3410/-50); 52_report_00.md, 53_implementation_00.md,
  53_correction_01.md, 53_report_01.md and 54_report_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused Python route; the
  bounded JavaScript set below; one temporary probe root
  /tmp/kronika-one-product-s8-reaudit (mode 0700, synthetic data only, removed)
Acceptance risk claims: the fixed claims C1–C12 below plus explicit closure of
  finding KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none beyond the controls below
Out-of-scope observations: ledger-candidates
```

This session did not implement, correct, plan or previously audit this slice.
No correction authority is granted; do not edit any repository file.

## Security audit record

```text
Security task class: fresh independent re-audit (R3), with authorization,
  submission-idempotency and rendering specializations
Owned/authorized target: /Users/agile/Projects/framenest at the candidate,
  read-only
Commit under audit: ef9920333013f3f70bf5e3443be2e51814f6b9c3
Scope: the two-commit delta from ade1169b4ba079bb1df540a929572ca58e777d16,
  emphasizing the correction commit 7f7aae9..ef99203 and F01 closure
Exclusions: NUC, SSH, sudo, browser launch, live provider, credentials,
  private/**, broad Python suite, correction
Threat model: as recorded in 54_report_00.md (assets, boundaries, attacker
  inputs, security properties, abuse cases); the correction changes only the
  client-side submission-idempotency path
```

## Candidate and repository gate

```text
Root: /Users/agile/Projects/framenest
Remote: https://github.com/cisarik/framenest.git
Branch: feat/kronika-one-product
Expected HEAD: ef9920333013f3f70bf5e3443be2e51814f6b9c3
Expected tree: e4338c2f31e8aff2829351ec107e2d75a165a473
Expected parent: 7f7aae9012d35671b062c8731e9009169501d4d0
AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Required state: clean index and worktree including untracked files
Public refs (one read-only ls-remote): main and feat/kronika-one-product
remain ade1169b4ba079bb1df540a929572ca58e777d16; the candidate is local-only
```

Independently verify all of it. Classify any difference per RF-12; stop on
unexplained divergence. No Git write of any kind.

## Fixed claims and required verdicts

Re-establish **C1–C12 exactly as defined in `54_acceptance_00.md`** on the
corrected candidate (its claim text is the contract; read it in the trace), and
add:

- **Finding closure — `KRONIKA-ONE-PRODUCT-S8-AUDIT-F01`.** Independently
  reproduce the original failure condition and verify closure on the corrected
  candidate: after a lost POST and a reload with the same login, the same kind,
  the exact same prompt and consent, an explicit resubmit must carry the
  **same** `client_request_id`; a changed prompt, a changed login, a missing or
  empty stored fingerprint, or no `crypto.subtle` must mint a new id; no
  automatic submit occurs; the prompt never appears in session storage. Verdict
  `verified-closed` or `not accepted` with evidence. Do not rely only on the
  candidate's own regression test: run it, and independently reproduce with
  your own two-context synthetic probe.

Correction containment must also be established: the correction commit changes
only `src/framenest/adapters/api/web/app.js` and `tests/kronika_ui.test.js`;
the existing same-page retry test is unchanged; the harness storage/login
options are test-only; no production behavior beyond the fingerprint-match
correction changed; the AP pin is unchanged.

## Required controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}' HEAD^; git status --porcelain --untracked-files=all
git log --oneline -3; git diff --name-status ade1169b4ba079bb1df540a929572ca58e777d16..HEAD; git show 7f7aae9012d35671b062c8731e9009169501d4d0..HEAD
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main refs/heads/feat/kronika-one-product
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline ef9920333013f3f70bf5e3443be2e51814f6b9c3

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline ef9920333013f3f70bf5e3443be2e51814f6b9c3 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_records_api.py tests/contract/test_research_requests_api.py tests/contract/test_local_record_identity.py tests/contract/test_kronika_access_inventory.py tests/contract/test_kronika_record_authorization.py tests/contract/test_kronika_approved_projection.py tests/contract/test_web_package_resources.py::test_web_resources_are_available_from_package_resource_boundary tests/contract/test_public_published_uds.py::test_unlisted_routes_and_methods_are_uniform_404 tests/contract/test_public_published_uds.py::test_workspace_tcp_audience_bootstrap_is_trusted_loopback tests/integration/persistence/test_kronika_record_repository.py tests/unit/application/test_records.py tests/unit/application/test_document_rendering.py -q -p no:cacheprovider

node --test tests/kronika_ui.test.js tests/gallery_loading_states.test.js tests/gallery_filter_controls.test.js tests/gallery_search_tag_filters.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/metadata_form_contract.test.js tests/metadata_alias_edit.test.js tests/catalog_card_ai_quick_action.test.js tests/tailscale_identity_frontend.test.js
```

Dynamic probes only under the declared synthetic root with synthetic data; no
live database, provider, browser or private data. The broad Python suite is not
run; a full JS run only if a named unresolved concern requires it. Do not set
`FRAMENEST_RUN_BROWSER_EVIDENCE`. Rendered browser and NUC acceptance remain
missing evidence for Michal after the NUC serves the exact public main; state
that absence and never convert it to PASS.

## Verdict rules and report contract

All C1–C12 established and F01 `verified-closed` yields
`acceptance-PASS`; otherwise `PARTIAL` or `BLOCKED` with the exact missing
evidence. Findings use the full security finding record; out-of-scope
observations become non-authorizing ledger candidates. The audit never repairs.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 55, 01), and includes the compact core,
the Acceptance and Correction Record, the Security audit record, per-claim
verdicts C1–C12, the explicit F01 closure verdict, correction containment, the
control matrix results, the containment ledger, limitations, residual-risk
summary, critique, and authority expiry. Use
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
Downloadable prompt filename: 55_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 55_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed repository gate, unexplained divergence, any
need to mutate the candidate, unavailable required capability through the
declared routes, or a finding that needs correction authority. Do not audit an
audit or expand into unknown-unknown hunting.

## Completion and report contract

Save the report exactly at the report path if the client permits; read back the
full saved content and verify first line, coordinates and path; otherwise
preserve the complete content in chat and mark the delivery limitation PARTIAL.
Send a short separate completion notice with status, location and SHA-256. No
correction, publication, deployment or further audit is authorized by the
report.

Authority expiry: the terminal report ends this re-audit exchange.
