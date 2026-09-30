### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 54
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S8-AUDIT
status: PARTIAL
Phase-qualified result: not-applicable
Start commit: 7f7aae9012d35671b062c8731e9009169501d4d0
End commit: 7f7aae9012d35671b062c8731e9009169501d4d0
Report justification: final-acceptance
Logical-whole closure: not-closed

Requested reasoning: Extra High. Observed assistant identity: Grok 4.7. Effective reasoning depth is not independently attested. This chat's visible history begins with the acceptance grant. No implementation edit was made. That is the independence evidence available here; it is not a separate attestation of process isolation.

Changed files: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/54_report_00.md` only. The FrameNest candidate was not edited.

Validation: repository gate matched the candidate; focused Python `416 passed`; bounded JavaScript `148 passed`, `0` failed. One synthetic reload probe reproduced finding F01. No browser, NUC, provider, sudo, or Git write.

Commit and push result: not authorized. Public `main` and `feat/kronika-one-product` both remain `ade1169b4ba079bb1df540a929572ca58e777d16`.

Deviations, risks, or missing evidence: C7 is partial. Finding F01 is open. Rendered browser and NUC acceptance was not run and is not treated as PASS.

Smallest next step: the Orchestrator dispositions F01. A correction needs a new grant. This audit does not repair the candidate.

Resolved Execution Issues / Near-Misses: the first probe script asked for form elements before `getElementById` created them. The script was corrected inside `/tmp/kronika-one-product-s8-audit` and then removed. The candidate was untouched.

Pre-Existing Failure Classification: none

### Acceptance and Correction Record

```text
Acceptance candidate: 7f7aae9012d35671b062c8731e9009169501d4d0
  (tree 17a559dff621882ac561a9901d20fe5b824508c4, branch feat/kronika-one-product,
   parent ade1169b4ba079bb1df540a929572ca58e777d16)
Acceptance owner map: delta ade1169b4ba079bb1df540a929572ca58e777d16..7f7aae9012d35671b062c8731e9009169501d4d0
  (one commit, 20 paths, +3311/-40); the frozen plan 52_report_00.md and the
  implementation prompt 53_implementation_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused Python route; the
  bounded JavaScript set below; one temporary probe root
  /tmp/kronika-one-product-s8-audit (mode 0700, synthetic data only, removed)
Acceptance risk claims: the fixed claims C1–C12 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none beyond the controls below
Out-of-scope observations: ledger-candidates
```

Ledger candidates: none. F01 is in scope for C7.

### Security audit record

```text
Security task class: focused defensive audit (R3), with authorization and
  rendering specializations; the provider-boundary specialization is limited to
  the no-live-call posture because S8 makes no provider calls
Owned/authorized target: /Users/agile/Projects/framenest at the candidate,
  read-only
Commit under audit: 7f7aae9012d35671b062c8731e9009169501d4d0
Scope: the one-commit delta from ade1169b4ba079bb1df540a929572ca58e777d16
Exclusions: NUC, SSH, sudo, browser launch, live provider, credentials,
  private/**, broad Python suite, correction
Threat model:
  Assets: record summaries and titles, private/family visibility decisions,
    owner identity, the local identity context, research submission identity and
    idempotency, rendered question/answer documents, the frozen Gallery/Details UX
  Trust boundaries: caller to records HTTP list/detail/render; authenticated
    local loopback identity to audience response; browser to provider-boundary
    forms (no call); untrusted render HTML into a sandboxed frame; administrator
    approval mutation
  Attacker-controlled inputs: query filters (kind, content_category, visibility,
    limit, offset), record ids, stored question/answer text and titles, provider
    output later rendered, forged identity headers
  Security properties: Timeline approved-only for every caller; approved
    projection titles/categories for every caller; no answer text or documents in
    list payloads; owner isolation for own history; administrator inventory gated;
    local identity echo only from an attached verified IdentityContext; one
    client_request_id per deliberate attempt; render HTML only inside a sandboxed
    frame with effective CSP; versioned approve/withdraw; fail-closed routes
  Abuse cases: cross-owner title/count leak; private record on the Timeline;
    working metadata leaking through the approved projection; answer text via
    lists; fabricated local identity; double-charging via a replaced request id;
    script execution via render; stale approval overwrite; administrator routes
    reachable without capability
Source records: none
Findings: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Containment ledger: recorded below
Limitations: recorded below
Residual-risk summary: recorded below
```

No live provider call was made. No credential, private media path, or private payload was copied into this report.

### Repository gate and RF-12

| Check | Result |
|---|---|
| HEAD | `7f7aae9012d35671b062c8731e9009169501d4d0` |
| Tree | `17a559dff621882ac561a9901d20fe5b824508c4` |
| Parent | `ade1169b4ba079bb1df540a929572ca58e777d16` |
| Branch | `feat/kronika-one-product` |
| AP gitlink and `.ap` HEAD | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Remote | `https://github.com/cisarik/framenest.git` |
| `git status --porcelain --untracked-files=all` | empty before tests and empty after probe cleanup |
| Delta | 20 paths, 19 modified, 1 added `tests/kronika_ui.test.js`, `+3311/-40` |
| `git ls-remote` `main` and `feat/kronika-one-product` | both `ade1169b4ba079bb1df540a929572ca58e777d16` |

Classification unit: local commit versus the two public branch tips. All five classes were considered. Primary class: `unpublished-candidate`. The candidate is the expected local-only commit; it was not pushed. Secondary: none of `unexplained-divergence`, `unrelated-owner-work`, `stale-clone`, or `accepted-continuation` applies to that unit. The worktree matches the expected candidate, so there is no second divergent unit. `./.ap/ap project check --baseline 7f7aae9012d35671b062c8731e9009169501d4d0` exited 0. It reported sanitized inherited environment classes `SSH_AUTH_SOCK` and `PATH` and did not print socket values.

Protected paths are absent from the delta: no `.ap` change, no migration, no dependency or lockfile, no `deploy/` path. `src/framenest/adapters/api/tailscale_ingress.py` is unchanged, so `ROUTE_POLICIES` and the fail-closed fallback are unchanged.

Leak hunt on the added production and documentation lines searched the delta of `src/`, `docs/`, `PRODUCT.md`, `README.md`, `ROADMAP.md`, `SERVER.md`, and `SPEC.md` for credential, secret, password, API-key, private-key, cookie, authorization-header, and private home-path markers. There were no matches.

### Per-claim verdicts

**C1 — established.** Identity, parent, tree, branch, 20-path delta, clean worktree, and unpublished public refs match the gate above. The leak hunt found no secret, credential value, private path, or private payload on the added production and documentation lines.

**C2 — established.** `SqliteRecordRepository._question_display_title` collapses whitespace and keeps at most 240 Unicode code points, with the ellipsis inside that limit. Media titles come from `kronika_approved_media` on the Timeline and from `media_metadata` elsewhere; empty or non-string values stay null. Invalid categories stay null. `ck_kronika_records_shape` keeps media rows and document rows apart, so a document title does not replace a media title. `_summary_payload` adds `display_title` and `content_category` and does not add answer text, citations, filenames, or location paths. `test_summaries_keep_hostile_titles_and_omit_answers` observed a title containing `<script>` and the absence of the answer string. `test_list_filters_apply_before_count_and_keep_order` in `tests/integration/persistence/test_kronika_record_repository.py` observed a 240-code-point title ending in `…`, collapsed hostile question text, and no `SECRET-ANSWER-TEXT` in titles. Card rendering assigns titles with `textContent`.

**C3 — established.** `list_timeline` sets `timeline_only`, which requires family visibility, a non-null approved projection, and a Timeline timestamp. Every Timeline row is labeled `READ_APPROVED`. Withdrawal sets visibility back to private, so the row leaves the Timeline for every caller. `test_timeline_membership_is_approved_for_every_caller` covered owner, household member, and administrator, including withdrawal. `test_timeline_titles_stay_on_the_approved_projection` changed working metadata from `TitleA` / `general` to `TitleB` / `meme` and observed the Timeline title, category, and category filter stay on the approved values for all three callers, while own history showed the working values. Search and Research titles are read from `question_text`. Repository writes of that column are inserts, not updates.

**C4 — established.** `_query` accepts only `media`, `search`, and `research`, accepts a content category only together with `kind=media`, and accepts visibility only from the closed private/family set. Non-administrator callers, including on `/api/my/records` and `/api/timeline`, receive 422 `INVALID_REQUEST` when `visibility` is present. The message is the fixed string `The list request is invalid.` Administrator inventory still requires `may_approve`. Own history still passes `identity.login_key`. Filters are applied to the id query before the count and the page. Default limit 24 and maximum 100 remain in `_page` and `_page_params`. Ordering remains `timeline_entered_at_ms` or `created_at_ms` descending, then id ascending. The repository test observed a 25-row search history page of 24 and an administrator own-history total of 1 against an inventory total of 27.

**C5 — established.** On the non-Tailscale branch, `/api/audience/me` echoes `login`, `display_name`, `role`, `provenance`, and the sorted capabilities only when `SCOPE_IDENTITY` holds an `IdentityContext` with `login_key`. `LocalIdentityMiddleware` attaches the configured owner for a loopback client and does not read an identity from request headers. `test_configured_loopback_echoes_mapped_identity` sent `X-Forwarded-User: ada` and `Tailscale-User-Login: ada@example.com` and observed login `alice`, role `user`, provenance `local-config`, and no `records.approve`. The same test observed an administrator echo with `records.approve`, and a non-loopback client with `identity: null`. `test_missing_local_owner_keeps_null_identity` observed the previous null-identity trusted-loopback body. The Tailscale return remains the branch above the new echo. Public published mode returns from `create_public_published_app` before the workspace records router.

**C6 — established.** An empty hash parses as `/timeline`. `kronikaStartNavigation` is the workspace startup path and follows that hash. The public-audience branch still calls `loadCatalogTags` and `loadCatalog` and does not open the Kronika sections. Gallery remains `#/gallery`, shows `#catalog-browser`, and loads the catalog once. `#/details/{id}` calls the existing `openDetailsDialog`. The companion `onOpenDetails` hook still calls `openDetailsDialog({ media_id: mediaId }, detailsCloseButton)`. List reads carry `kronikaIdentityGeneration` and a per-list generation; a stale result returns before `kronikaAcceptList` writes items. Timeline loading fetches `/api/timeline` only. `kronikaNoteIdentity` clears private lists, the frame, and polling when the audience or login changes. `tests/kronika_ui.test.js` covers the empty-hash landing, the details handoff, administrator Timeline isolation, history rows staying off the Timeline, a failed refresh keeping the previous page, and identity loss clearing the frame and question. The open and close details hooks only add the hash helpers. Playback functions are outside those hunks.

**C7 — partial.** The same-page controls match the claim. `kronikaSubmitQuestion` checks consent and the 16,384-byte `TextEncoder` bound, then `kronikaFreezeAttempt` assigns one id before `kronikaPostAttempt`. A thrown POST is retried through `kronikaRetrySubmission` with the same object. Editing clears the id. `submitting` blocks overlap. `consent_version` is `kronika-research-v1` and is sent only after the checkbox. The question form says acknowledgement is not stored as a separate setting. The node test `submission retries keep the attempt id until the question changes` observed three posts, one id, and a new id after the question changed. The durable recovery path does not keep that id. See F01.

**C8 — established.** Active states are `admitted`, `submitting`, `running`, `validating`, and `cancel_requested`. Terminal states are `saved`, `refused`, `failed`, `incomplete`, `cancelled`, `timeout`, and `submission_unknown`. `kronikaPollOnce` returns while `pollInFlight` is set, uses GET on `/api/research-requests/{operation_id}`, and arms the next five-second timeout only after the request settles and only when the document is visible. Hide and `pagehide` clear the timer. Identity change calls `kronikaStopPoll`. An unknown state sets `Status is unavailable.` and does not arm another poll. Three transport failures set `pollPaused` and reveal Resume. The status text for those failures is the pause copy. `cancel_requested` stays in the active set. The open-answer link and the history-cache clear run only when `saved` has `record_id`. That path does not assign a hash and does not clear `kronikaLists.timeline`. The polling test observed one in-flight GET, a 5,000 ms follow-up, cancellation copy that is not the terminal `Cancelled.` label, and pause copy that does not contain `Failed.`

**C9 — established.** `index.html` gives `#kronika-document-frame` `sandbox=""` and `referrerpolicy="no-referrer"`. `kronikaLoadRecord` writes the question first, then fetches render HTML, then assigns `srcdoc` from `kronikaSrcdoc`. That wrapper carries `default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'`. A failed render clears `srcdoc`, leaves the question in place, and reveals retry. Citations are created with `createElement`; `kronikaSafeCitationUrl` allows only `http`, `https`, and `mailto`; links set `rel` to `noopener noreferrer`. The render test observed the CSP and answer inside `srcdoc`, the question in the page, and no fetch of the citation host. Production `app.js` has no `innerHTML` assignment.

**C10 — established.** The review detail offers Approve and Withdraw. Both post `action` and the `expected_version` taken from the displayed payload version. `changed: false` is accepted with `The record is already in that state.` A 409 sets `needsReload`, shows the conflict copy, and `kronikaSyncReviewActions` disables the stale actions until Reload. There is no automatic resubmit and no version substitution. No Reject control exists. Approve stays disabled when `completed_at_ms` is null. `test_unready_media_cannot_be_approved` observed 409 `RECORD_CONFLICT`. `test_stale_version_conflicts_and_users_cannot_approve` observed 409 for a stale version and 422 for `reject`. The node approval test observed a second click sending no post, then a post of the reloaded version after Reload.

**C11 — established.** The route-policy module is outside the delta. The regenerated inventory row for `GET /api/timeline` says `approved projection for every caller, including owner and administrator`. A search of `docs/KRONIKA_ACCESS_INVENTORY.md` found no `TODO`, `TBD`, `FIXME`, or `placeholder`. `create_app` returns `create_public_published_app` for public published ingress before the workspace records and research routers are installed. `create_public_published_app` includes `create_public_published_api_router` only. `test_inventory_matches_both_compositions_and_route_policies` passed, as did `test_unlisted_routes_and_methods_are_uniform_404` and `test_workspace_tcp_audience_bootstrap_is_trusted_loopback`. `find_route_policy` still returns `_UNCLASSIFIED_FALLBACK_POLICY` when no explicit policy matches.

**C12 — established.** The declared Python command exited 0 with `416 passed in 42.06s`. The declared node command exited 0 with `148` passed and `0` failed. The CSS delta adds `.brand-wordmark`, `#main` focus rules, and `.kronika-*` rules. It does not change existing Gallery, Details, or player selectors. The only removed test line moves `/api/timeline` from the older projection sentence into the stricter approved-for-every-caller sentence. `tests/kronika_ui.test.js` slices `/* KRONIKA_SHELL_START */` through `/* KRONIKA_SHELL_END */` from production `app.js` and runs that slice with `vm.runInContext`.

### Control matrix results

| Control | Result |
|---|---|
| `git rev-parse HEAD`, `HEAD^{tree}`, `HEAD^` | match the candidate, tree, and parent |
| `git status --porcelain --untracked-files=all` | empty at gate and after probe cleanup |
| `git log --oneline -3` and `git diff --name-status` | one subject `feat(kronika): add unified timeline history and review UI`; 20 paths |
| `git show -s HEAD` | parent `ade1169b4ba079bb1df540a929572ca58e777d16` |
| `GIT_TERMINAL_PROMPT=0 git ls-remote` for `main` and `feat/kronika-one-product` | both `ade1169b4ba079bb1df540a929572ca58e777d16` |
| `./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 7f7aae9012d35671b062c8731e9009169501d4d0` | exit 0, `ap project check --baseline: PASS` |
| `./.ap/ap exec ... --operation test-focus --` the declared Python files | exit 0, `416 passed in 42.06s` |
| `node --test` the declared JavaScript files | exit 0, `148` passed, `0` failed |

`FRAMENEST_RUN_BROWSER_EVIDENCE` was not set. The broad Python suite was not run.

### Finding

```text
Finding ID: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Title: Reload recovery replaces the frozen research request id
Status: open
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7f7aae9012d35671b062c8731e9009169501d4d0
Affected component and exact location: src/framenest/adapters/api/web/app.js kronikaOfferRecovery, kronikaFreezeAttempt, kronikaPersistAttempt
Security property: one client_request_id per deliberate attempt, reused by a transport-failure retry
Asset at risk: research submission identity and idempotency
Trust boundary: browser to provider-boundary form
Attacker-controlled input or local actor: the signed-in caller after a lost POST response
Reachability: workspace shell, research form, sessionStorage key kronika.research.attempt.v1
Preconditions: the POST throws before an operation id is stored; the page is reloaded; the caller re-enters the same question, checks consent, and submits
Required privileges: ordinary user
Observed or potential impact: the second POST carries a new client_request_id, so server idempotency on the first id does not cover it
C/I/A effect: integrity of the one-attempt guarantee; possible second provider admission and budget use; no cross-owner disclosure observed
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: under /tmp/kronika-one-product-s8-audit, a synthetic probe loaded the production shell slice in two fresh contexts that shared one sessionStorage map. The first context submitted "Synthetic question" and the POST threw. The stored value had keys id, fingerprint, and operationId, and no prompt. The second context called kronikaShowQuestion, re-entered the same question, checked consent, and submitted. The two client_request_id values differed. No provider was contacted.
Static evidence: kronikaPersistAttempt writes the fingerprint; kronikaOfferRecovery restores id and does not read the fingerprint or prompt; kronikaFreezeAttempt mints a new id when the in-memory prompt does not match
Synthetic containment: /tmp/kronika-one-product-s8-audit, created by this audit, mode 0700, synthetic script and synthetic question only, removed
False-positive analysis: this would be disproved if the second context reused the stored id, or if C7 treated every reload as a mandatory new attempt. The recovery copy says "Re-enter the same question before retrying this submission", and the same-page retry does reuse the id. The reload path is the one that drops it.
Exploitability conclusion: probable
Smallest safe correction direction: on submit after recovery, recompute the fingerprint for the current login, kind, exact prompt, and consent; reuse the stored id only when it matches; otherwise mint a new id. Keep the prompt out of storage. Do not auto-submit.
Regression-test requirement: a node harness that uses two fresh production-shell contexts, one shared sessionStorage, a thrown first POST, and a same-question resubmit that must keep the same client_request_id
Residual risk: until corrected, a lost response plus reload and resubmit can admit a second request
Acceptance-blocking decision: blocking, because C7's transport-failure retry does not reuse the frozen id across the shell's own recovery path
Redaction requirements: none; the probe used a synthetic question and no provider credential
```

### Containment ledger

```text
Temporary root: /tmp/kronika-one-product-s8-audit
Owner: this audit
Mode: 0700
Contents class: synthetic fixtures only
Cleanup owner: this audit
Cleanup outcome: removed
```

The probe script was deleted and the directory was removed with `rmdir`. A following existence check reported `probe-root-removed`. No live database and no private data were used.

### Limitations

Rendered browser behavior and NUC acceptance were not run. That missing evidence is stated here and is not converted to PASS. The broad Python suite and a full JavaScript run were not required and were not run. No live provider call was made. The pinned `.ap` checkout has no `INFOSEC.md`; this report uses the structural security-audit contract. The same-page retry in C7 remains established by the node test. F01 is the reload path.

### Residual-risk summary

```text
Finding ID: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Decision: correction-required
Severity: medium
Approver: Cooperator
Regression test: not present; the required harness is described on F01
Rationale: a medium finding on the named double-charge abuse case is not accepted by this audit
Recorded in: this report
```

C1–C6 and C8–C12 have no separate residual finding.

### Compact critique

```text
Orchestration critique:
MEASURED: reload recovery writes a SHA-256 fingerprint and then ignores it; the synthetic two-context probe showed a new client_request_id; effect is a second admission after a lost POST; smallest correction is fingerprint match before minting a new id
LEAD: none
```

Authority expiry: this terminal report ends the audit exchange. No correction, publication, deployment, or further audit is authorized.
