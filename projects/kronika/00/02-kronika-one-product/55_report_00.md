### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 55
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S8-REAUDIT
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: ef9920333013f3f70bf5e3443be2e51814f6b9c3
End commit: ef9920333013f3f70bf5e3443be2e51814f6b9c3
Report justification: final-acceptance
Logical-whole closure: not-closed

Requested reasoning: Extra High. Observed assistant identity: Grok 4.7. Effective reasoning depth is not independently attested. This chat's visible history begins with the re-audit grant. No implementation, correction, or prior audit of this slice was done in this session. That is the independence evidence available here; it is not a separate attestation of process isolation.

Changed files: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/55_report_00.md` only. The FrameNest candidate was not edited.

Validation: repository gate matched the candidate. Focused Python `416 passed in 42.85s`. Bounded JavaScript `149 passed`, `0` failed. The candidate regression test ran inside that JavaScript set. An independent two-context probe closed F01. No browser, NUC, provider, sudo, or Git write.

Commit and push result: not authorized. Public `main` and `feat/kronika-one-product` both remain `ade1169b4ba079bb1df540a929572ca58e777d16`.

Deviations, risks, or missing evidence: none on C1–C12 or F01. Rendered browser and NUC acceptance were not run. That absence is not a PASS. The logical whole stays open.

Smallest next step: the Orchestrator dispositions this acceptance-PASS. Publication, deployment, and rendered acceptance after the NUC serves the exact public main remain separate grants.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

### Acceptance and Correction Record

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

This session did not implement, correct, plan, or previously audit this slice. No repository file was edited.

### Security audit record

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
Findings: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01 verified-closed; no new finding
Containment ledger: recorded below
Limitations: recorded below
Residual-risk summary: recorded below
```

No live provider call was made. No credential, private media path, or private payload was copied into this report.

### Repository gate and RF-12

| Check | Result |
|---|---|
| HEAD | `ef9920333013f3f70bf5e3443be2e51814f6b9c3` |
| Tree | `e4338c2f31e8aff2829351ec107e2d75a165a473` |
| Parent | `7f7aae9012d35671b062c8731e9009169501d4d0` |
| Branch | `feat/kronika-one-product` |
| Remote | `https://github.com/cisarik/framenest.git` |
| AP gitlink and `.ap` HEAD | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| `git status --porcelain --untracked-files=all` | empty at the gate and empty after probe cleanup |
| Two-commit path set | 20 paths; 19 modified and 1 added `tests/kronika_ui.test.js` |
| `git ls-remote` `main` and `feat/kronika-one-product` | both `ade1169b4ba079bb1df540a929572ca58e777d16` |

`git show --stat` of `7f7aae9012d35671b062c8731e9009169501d4d0` is `+3311/-40`. `git show --stat` of `ef9920333013f3f70bf5e3443be2e51814f6b9c3` is `+99/-10`. Those commit stats sum to `+3410/-50`. `git diff --stat ade1169b4ba079bb1df540a929572ca58e777d16..HEAD` is `+3400/-40` because the correction edits lines the first commit added. That arithmetic is explained. It is not a second divergent unit.

Classification unit: local HEAD versus the two public branch tips. All five classes were considered. Primary class: `unpublished-candidate`. The candidate is the expected local-only commit and was not pushed. Secondary: none of `unexplained-divergence`, `unrelated-owner-work`, `stale-clone`, or `accepted-continuation` applies. `./.ap/ap project check --baseline ef9920333013f3f70bf5e3443be2e51814f6b9c3` exited 0. It reported sanitized inherited environment classes `SSH_AUTH_SOCK` and `PATH` and did not print socket values.

Protected paths are absent from the delta: no `.ap` change, no migration, no dependency or lockfile, and no `deploy/` path. `src/framenest/adapters/api/tailscale_ingress.py` is unchanged, so `ROUTE_POLICIES` and the fail-closed fallback are unchanged.

Leak hunt on the added production and documentation lines searched the delta of `src/`, `docs/`, `PRODUCT.md`, `README.md`, `ROADMAP.md`, `SERVER.md`, and `SPEC.md` for credential, secret, password, API-key, private-key, cookie, authorization-header, and private home-path markers. There were no matches.

### Per-claim verdicts

**C1 — established.** Identity, parent, tree, branch, 20-path delta, clean worktree, unchanged AP pin, and unpublished public refs match the gate above. The leak hunt found no secret, credential value, private path, or private payload on the added production and documentation lines.

**C2 — established.** `_question_display_title` collapses whitespace and keeps at most 240 Unicode code points, with the ellipsis inside that limit. Media titles on the Timeline come from `kronika_approved_media`; other lists use `media_metadata`. Non-strings and empty strings stay null. Invalid categories stay null. Document labels replace a row label from `question_text` only, and repository writes of that column are inserts. `_summary_payload` adds `display_title` and `content_category` and does not add answer text, citations, filenames, or location paths. `kronikaRenderCards` assigns the title with `textContent`. `test_summaries_keep_hostile_titles_and_omit_answers` is in the focused set that passed.

**C3 — established.** `list_timeline` sets `timeline_only`, which requires family visibility, a non-null approved projection, and a Timeline timestamp. Every Timeline row is labeled `READ_APPROVED`. Timeline category filters read `kronika_approved_media`, not working metadata. `test_timeline_membership_is_approved_for_every_caller` and `test_timeline_titles_stay_on_the_approved_projection` are in the focused set that passed. Detail and Gallery authorization stay on the non-timeline read path.

**C4 — established.** `_query` accepts only the closed kind set, accepts a content category only with media, and accepts visibility only from the closed visibility set. `/api/timeline` and `/api/my/records` call `_list_filters` with `administrator=False`, so a visibility parameter raises `RecordValueError` and returns 422 `INVALID_REQUEST` with the fixed message `The list request is invalid.` Administrator inventory still requires `may_approve` and is the only list that passes visibility through. Own history still passes `identity.login_key`. The id filter is counted before the page query. Default limit 24 and maximum 100 remain. Ordering remains timestamp descending, then id ascending.

**C5 — established.** On the non-Tailscale branch, `/api/audience/me` echoes login, display name, role, provenance, and sorted capabilities only when `SCOPE_IDENTITY` holds an `IdentityContext` with `login_key`. Otherwise it keeps the previous null-identity trusted-loopback body. `LocalIdentityMiddleware` attaches the configured owner for a loopback client and does not read an identity from request headers. `test_configured_loopback_echoes_mapped_identity` sends `X-Forwarded-User` and `Tailscale-User-Login` and is in the focused set that passed, as is `test_missing_local_owner_keeps_null_identity`. The Tailscale return remains the branch above the echo. Public published mode returns from `create_public_published_app` before the workspace records router is installed.

**C6 — established.** An empty hash parses as `/timeline`. `kronikaStartNavigation` is the workspace startup path. The public-audience branch does not open the Kronika sections. Gallery remains `#/gallery`. `#/details/{id}` still reaches `openDetailsDialog`. List reads carry `kronikaIdentityGeneration` and a per-list generation; a stale result returns before `kronikaAcceptList` writes items. Timeline loading fetches `/api/timeline` only. `kronikaNoteIdentity` clears private lists and stops polling when the audience or login changes. The node shell tests for landing, details, administrator Timeline isolation, and identity loss are in the JavaScript set that passed. The CSS delta adds `.brand-wordmark`, `#main` focus rules, and `.kronika-*` rules. It deletes no existing rule.

**C7 — established.** `kronikaSubmitQuestion` checks a non-empty prompt, the 16,384-byte `TextEncoder` bound, and the consent checkbox before `kronikaFreezeAttempt`. The consent version sent after that check is `kronika-research-v1`. The question form says acknowledgement is not stored as a separate setting. `kronikaAttempt.submitting` blocks an overlapping post. A thrown POST is retried by `kronikaRetrySubmission` with the same in-memory object. The input listener clears the in-memory id when the text changes, and a changed prompt no longer matches the stored fingerprint, so the next submit mints a new id. The node test `submission retries keep the attempt id until the question changes` is unchanged and passed: three posts, one id, then a new id after the question changed. The reload path now reuses that id when the fingerprint matches. See F01.

**C8 — established.** Active states are exactly `admitted`, `submitting`, `running`, `validating`, and `cancel_requested`. Terminal states are exactly `saved`, `refused`, `failed`, `incomplete`, `cancelled`, `timeout`, and `submission_unknown`. `kronikaPollOnce` returns while a poll is in flight, uses GET on the operation, and arms the next 5,000 ms timeout only after settle. `visibilitychange` and `pagehide` clear the timer. Identity change calls `kronikaStopPoll`. An unknown state sets `Status is unavailable.` and does not stay in the active set. Three transport failures set `pollPaused` and reveal Resume. That pause copy is not the terminal `Failed.` label. `cancel_requested` stays active. The open-answer link runs only when `saved` has `record_id`. That path does not assign a hash and does not clear `kronikaLists.timeline`. The polling node test passed.

**C9 — established.** `index.html` gives `#kronika-document-frame` `sandbox=""` and `referrerpolicy="no-referrer"`. `kronikaLoadRecord` writes the question first, fetches render HTML, and only then assigns `srcdoc` from `kronikaSrcdoc`. That wrapper carries `default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'`. The render route sends the same policy and `X-Content-Type-Options: nosniff`. A failed render clears `srcdoc`, leaves the question, and reveals retry. Citations are created with `createElement`. `kronikaSafeCitationUrl` allows only `http`, `https`, and `mailto`. Links set `rel` to `noopener noreferrer`. Production `app.js` has no `innerHTML` assignment. `tests/unit/application/test_document_rendering.py` is in the focused set that passed.

**C10 — established.** The review markup offers Approve and Withdraw and no Reject control. Both actions post `action` and the `expected_version` taken from the displayed payload version. `changed: false` is accepted with `The record is already in that state.` A 409 sets `needsReload`, shows the conflict copy, and `kronikaSyncReviewActions` disables the stale actions until Reload. There is no automatic resubmit and no version substitution. Approve stays disabled when `completed_at_ms` is null. The server accepts only `approve` and `withdraw`; any other action returns 422 `UNSUPPORTED_ACTION`. `test_unready_media_cannot_be_approved` and `test_stale_version_conflicts_and_users_cannot_approve` are in the focused set that passed. The node approval test passed.

**C11 — established.** The route-policy module is outside the delta. The inventory row for `GET /api/timeline` says `approved projection for every caller, including owner and administrator`. A search of `docs/KRONIKA_ACCESS_INVENTORY.md` found no `TODO`, `TBD`, `FIXME`, or `placeholder`. `create_public_published_app` includes `create_public_published_api_router` only. `test_inventory_matches_both_compositions_and_route_policies`, `test_unlisted_routes_and_methods_are_uniform_404`, and `test_workspace_tcp_audience_bootstrap_is_trusted_loopback` are in the focused set that passed. `find_route_policy` still returns `_UNCLASSIFIED_FALLBACK_POLICY` when no explicit policy matches.

**C12 — established.** The declared Python command exited 0 with `416 passed in 42.85s`. The declared node command exited 0 with `149` passed and `0` failed. The CSS delta does not change existing Gallery, Details, or player selectors. The new `tests/kronika_ui.test.js` slices `/* KRONIKA_SHELL_START */` through `/* KRONIKA_SHELL_END */` from production `app.js` and runs that slice with `vm.runInContext`. The correction adds one regression test and does not delete or rewrite the previous shell tests.

### Finding closure — KRONIKA-ONE-PRODUCT-S8-AUDIT-F01

Verdict: `verified-closed`.

```text
Finding ID: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Title: Reload recovery replaces the frozen research request id
Status: verified-closed
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: ef9920333013f3f70bf5e3443be2e51814f6b9c3
Affected component and exact location: src/framenest/adapters/api/web/app.js kronikaFreezeAttempt, kronikaReadStoredAttempt, kronikaPersistAttempt
Security property: one client_request_id per deliberate attempt, reused by a transport-failure retry
Asset at risk: research submission identity and idempotency
Trust boundary: browser to provider-boundary form
Attacker-controlled input or local actor: the signed-in caller after a lost POST response
Reachability: workspace shell, research form, sessionStorage key kronika.research.attempt.v1
Preconditions: the POST throws before an operation id is stored; the page is reloaded; the caller re-enters the same question, checks consent, and submits
Required privileges: ordinary user
Observed or potential impact: closed on the corrected candidate; the explicit resubmit carries the original client_request_id
C/I/A effect: the one-attempt guarantee holds for the named reload path; no cross-owner disclosure observed
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: the candidate test "reload recovery reuses the request id only when the fingerprint matches" passed inside the bounded JavaScript run. Independently, under /tmp/kronika-one-product-s8-reaudit, a synthetic probe loaded the production shell slice in fresh vm contexts that shared one sessionStorage map. The first context submitted a synthetic prompt and the POST threw. The stored object had keys id, fingerprint, and operationId, a 64-character fingerprint, an empty operation id, and no prompt. A second context called kronikaShowQuestion and issued no POST. After the same login, search kind, exact prompt, and consent, the explicit resubmit used the same client_request_id and consent_version kronika-research-v1. A changed prompt, a changed login, research instead of search, an empty stored fingerprint, a missing stored fingerprint, and a context whose crypto object had no subtle each minted a new id. Unchecked consent issued no POST. No provider was contacted.
Static evidence: kronikaPersistAttempt writes id, fingerprint, and operationId only. kronikaFreezeAttempt recomputes the SHA-256 fingerprint from login, kind, exact prompt, and KRONIKA_CONSENT_VERSION, and reuses the stored id only when the fingerprint is non-empty and equal. Otherwise it mints a new id. kronikaFingerprint returns an empty string when crypto.subtle.digest is absent, and an empty fingerprint fails the match. kronikaOfferRecovery sets status text and does not call submit.
Synthetic containment: /tmp/kronika-one-product-s8-reaudit, created by this re-audit, mode 0700, synthetic script and synthetic question only, removed
False-positive analysis: closure would be false if any named mismatch reused the original id, if the same tuple minted a new id, if show-question posted by itself, or if the prompt appeared in the stored JSON. None of those occurred.
Exploitability conclusion: the named reload replacement is closed
Smallest safe correction direction: none; the correction is present and was re-checked
Regression-test requirement: met by the candidate's two-context node test; the empty fingerprint, missing fingerprint, and absent crypto.subtle cases were additionally reproduced by this probe
Residual risk: none for this finding; rendered browser behavior remains separate missing evidence
Acceptance-blocking decision: not blocking
Redaction requirements: none; the probe used a synthetic question and no provider credential
```

### Correction containment

The correction commit `7f7aae9012d35671b062c8731e9009169501d4d0..ef9920333013f3f70bf5e3443be2e51814f6b9c3` changes only `src/framenest/adapters/api/web/app.js` and `tests/kronika_ui.test.js` (`+99/-10`). The existing test `submission retries keep the attempt id until the question changes` is outside those hunks and passed. `options.storage` and `options.login` exist only in the test harness. Production behavior changed in `kronikaFreezeAttempt`: it now reads the stored fingerprint and reuses the stored id only on a match, and `kronikaSubmitQuestion` awaits that function. `kronikaPersistAttempt`, `kronikaOfferRecovery`, and `kronikaRetrySubmission` are outside the correction hunks. The AP pin is unchanged at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.

### Control matrix results

| Control | Result |
|---|---|
| `git rev-parse HEAD`, `HEAD^{tree}`, `HEAD^` | match the candidate, tree, and parent |
| `git status --porcelain --untracked-files=all` | empty at the gate and after probe cleanup |
| `git log --oneline -3` and `git diff --name-status` | parent subject `feat(kronika): add unified timeline history and review UI`; HEAD subject `fix(kronika): reuse the frozen request id across reload recovery`; 20 paths across the owner map |
| `git show 7f7aae9012d35671b062c8731e9009169501d4d0..HEAD` | two paths, `app.js` and `tests/kronika_ui.test.js` |
| `GIT_TERMINAL_PROMPT=0 git ls-remote` for `main` and `feat/kronika-one-product` | both `ade1169b4ba079bb1df540a929572ca58e777d16` |
| `./.ap/ap project check --root /Users/agile/Projects/framenest --baseline ef9920333013f3f70bf5e3443be2e51814f6b9c3` | exit 0, `ap project check --baseline: PASS` |
| `./.ap/ap exec ... --operation test-focus --` the declared Python files | exit 0, `416 passed in 42.85s` |
| `node --test` the declared JavaScript files | exit 0, `149` passed, `0` failed |

`FRAMENEST_RUN_BROWSER_EVIDENCE` was not set. The broad Python suite was not run. A full JavaScript run was not required.

### Containment ledger

```text
Temporary root: /tmp/kronika-one-product-s8-reaudit
Owner: this re-audit
Mode: 0700
Contents class: synthetic fixtures only
Cleanup owner: this re-audit
Cleanup outcome: removed
```

The probe script was deleted with the directory. A following existence check reported `probe-root-removed`. No live database and no private data were used. The FrameNest worktree was empty afterward.

### Limitations

Rendered browser behavior and NUC acceptance were not run. That missing evidence is stated here and is not converted to PASS. The broad Python suite and a full JavaScript run were not required and were not run. No live provider call was made. The pinned `.ap` checkout has no `INFOSEC.md`; this report uses the structural security-audit contract from the grant and from `54_report_00.md`.

### Residual-risk summary

```text
Finding ID: KRONIKA-ONE-PRODUCT-S8-AUDIT-F01
Decision: verified-closed
Severity: medium
Approver: this re-audit, for the named closure only
Regression test: present and passed; independent probe also passed
Rationale: the lost-POST reload path now reuses the frozen id only for the same login, kind, prompt, and consent fingerprint
Recorded in: this report
```

No new finding was opened. C1–C12 have no separate residual finding. Rendered browser and NUC acceptance remain outside this result.

### Ledger candidates

none

### Compact critique

```text
Orchestration critique:
MEASURED: none
LEAD: none
```

Authority expiry: this terminal report ends the re-audit exchange. No correction, publication, deployment, or further audit is authorized.
