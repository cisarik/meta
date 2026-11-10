### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-TCC-ACC-03 — independent E3 acceptance of the complete visibility-aware Timeline chronicle
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
End commit: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Report justification: final-acceptance
Logical-whole closure: not-closed
Result artifact or commit: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Result evidence: fixed candidate, source inspection, and the selected gates below
```

This session started on the acceptance prompt. It did not plan or implement the candidate. Native Plan mode was off. The implementation report was treated as a claim, not proof.

## Acceptance record

```text
Acceptance candidate: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Acceptance owner map: 01_report_02.md section 10 rows C01-C24; ADR-0087; 02_report_01.md section 7
Acceptance allowlist: exactly the 29 changed paths in section 2
Acceptance risk claims: C01-C24, with focus on C01-C14, C16-C21 and C24
Acceptance control matrix: 01_report_02.md section 10, fixed; repeated in section 4
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Repository gate

| Check | Result |
|---|---|
| Checkout | `/Users/agile/Projects/kronika`, branch `main` |
| HEAD | `264a040e104e7495ce649fa583c4f0f3c1241b7c` |
| Parent | `b66ec8f50860ace624f6be1fd3ad63f521edcd33` |
| Public `refs/heads/main` | `b66ec8f50860ace624f6be1fd3ad63f521edcd33` |
| Worktree | Clean before review and after the selected tests |
| Changed paths | Exactly the 29 allowlisted paths |
| `.ap` gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `./.ap/ap doctor` | PASS |
| `ap project check --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33` | PASS |
| Environment warning | Sanitized classes `GIT_CONFIG_VALUE_0`, `SSH_AUTH_SOCK`, `PATH`, `GIT_CONFIG_KEY_0`, `GIT_CONFIG_COUNT`; no values |
| `git diff --check` on the candidate range | Clean |

The candidate remains local and unpushed. No repository file was edited.

## C01–C24

| ID | Verdict | Evidence |
|---|---|---|
| C01 | PASS | Private bound media is visible to the owner and absent for another member in `test_kronika_record_repository.py::test_timeline_titles_stay_on_the_approved_projection` and `test_records_api.py::test_media_list_preview_locator_is_additive_and_path_free`. `test_timeline_repository.py::test_timeline_sql_matches_existing_audience_policy` gives Bob only the unbound published medium. The named API visibility test covers a private question, not media; the media cases above do. |
| C02 | PASS | Administrator current access includes another owner's private question (`test_records_api.py::test_timeline_membership_follows_owner_admin_and_household_visibility`), private media, and an unbound unpublished medium (`test_timeline_count_page_and_locators_share_one_snapshot` reads that row as admin). Administrator current is `media.workflow.read` for media and completed records, and `role == admin` or `records.approve` for unfinished requests, matching `decide_bound_read` and `research_api._is_admin`. The diff adds no capability, route, host, or secret privilege. |
| C03 | PASS | After approval, Bob receives the frozen question text and a search for the later working question returns zero (`test_timeline_household_uses_only_approved_labels_and_status`). For media, Bob stays on `TitleA` / `general` after the working row becomes `TitleB` / `meme`, and the working preview location is absent from Bob's payload (`test_timeline_titles_stay_on_the_approved_projection`, `test_working_only_preview_location_is_not_disclosed_on_timeline`). Approved question text is `json_extract(..., '$.document.question_text')` with no fallback to the current document. |
| C04 | PASS | `test_timeline_denies_anonymous_and_is_absent_from_public_composition`: anonymous `GET /api/timeline` is 401 `IDENTITY_REQUIRED` with `private, no-store`; the public composition returns 404. `create_public_published_app` does not register that route. |
| C05 | PASS | A medium with two locations and no analysis run appears once as `not_requested` (`test_timeline_union_deduplicates_media_and_saved_requests`). `SqliteTimelineReader` issues only `SELECT`, then `ROLLBACK`. No insert, schema change, or synthetic record exists in the reader. |
| C06 | PASS | The media status expression returns `analyzed` when the decision is `approved`, otherwise the latest `automatic_post_catalog` run (`created_at_ms DESC, id DESC`) or `not_requested`. Household selection of the approved decision is executed by the title and category tests. A later pending or failed run was not inserted; the status column is that same decision, not a second audience predicate. |
| C07 | PASS | Failure is a status value on the already-authorized arm. Private media and another member's request are excluded before status is displayed. No selected fixture uses analysis state `failed` or request state `failed`; the inclusion SQL has no failure exception that would widen the set. |
| C08 | PASS | Alice's `admitted` request appears and keeps `question:` identity (`test_timeline_item_identity_survives_binding_and_save`). Her `running` request appears with a null record id, and Bob's total is zero (`test_timeline_request_lifecycle_and_saved_transition`). Admin Ada receives Alice's unfinished request (`test_timeline_sql_matches_existing_audience_policy`). The request arm projects `lifecycle_state` without a state allowlist. `submitting`, `validating`, and `cancel_requested` were not inserted separately. |
| C09 | PASS | A completed record whose request is still `validating` contributes one `question:` item with status `saved`. After the request is marked `saved`, the API total remains 1 and the item id stays `question:op-live`. |
| C10 | PASS | The named preview test does not withdraw or call the preview route. Withdrawal is executed in `test_records_api.py::test_list_preview_locator_round_trip_preserves_record_audience` and `test_withdrawn_preview_is_denied_even_with_a_cached_etag`: Bob loses the Timeline row, a conditional preview GET is 404 `no-store`, and the preview service is not called again. Owner and admin retain the withdrawn row with `publication_state=withdrawn`. |
| C11 | PASS | `test_kronika_approved_projection.py::test_withdrawal_keeps_timeline_position_and_snapshot` keeps `created_at_ms == 5` across approval and withdrawal while `timeline_entered_at_ms` stays 9 on the record detail. Reapproval in the same module also leaves the chronicle timestamp unchanged. |
| C12 | PASS | Bob can read an unbound published medium and loses it after a private binding (`test_timeline_binding_precedes_legacy_publication_and_contributions`). The media decision checks the binding before publication or requester access, matching `ContentAudiencePolicy.read_decision`. The test name mentions contributions, but the fixture does not insert an upload, YouTube, or X claim. |
| C13 | PASS | `_requester_ids` matches the live predicates: upload publication joined to the caller's session; YouTube `cataloged` and `duplicate_resolved`; X asset `cataloged` joined to the caller's post claim. Those are the same sets as `has_live_requester_media_access`. A mere non-success stamp is outside those predicates. No selected Timeline test executes those three sources. |
| C14 | PASS | Two available locations produce one `media:` item. A saved request with its completed record produces one `question:` item, including during the validating-with-record interval. Runs are reduced to rank 1 before the media join. Requester ids use `UNION`, not `UNION ALL`. |
| C15 | PASS | Equal timestamps order by `item_id` ascending, and Python's sort of those ASCII ids matches the returned page (`test_timeline_filters_counts_and_tie_order_use_authorized_projection`). Save and approval do not change the chronicle identity or creation time. |
| C16 | PASS | Kind, text, status, and visibility filters are applied to the authorized projection before `count()` and the page select. Bob's search for Alice's private question returns total 0. Invalid status and a category without `kind=media` return 422 `private, no-store`. An offset past the end is ordinary `LIMIT`/`OFFSET` on that same filtered total; it was not given its own fixture. |
| C17 | PASS | The reader executes `BEGIN` on the sqlite3 connection before the first select and `ROLLBACK` after the page. In WAL mode, a row committed after the count select and before the page select stays out of both the total and the items. |
| C18 | PASS | Instrumented cursor events: empty page 2 selects, question-only page 2, mixed video-plus-still page 3. Still images get a null locator. The statements do not contain `answer_text` or `relative_path`. Limits 1 and 100 were not executed separately; they change only `LIMIT`. |
| C19 | PASS | Owner and admin receive the minimum available current location; a household read stays on the approved location after a new working location appears. Withdrawal denies the old locator before another cache open, including `If-None-Match`. `test_missing_derivative_is_not_generated_by_get_and_error_is_sanitized` still denies generation. The chronicle reuses `kronikaAttachCardPreview` and does not retry after an error. |
| C20 | PASS | The API item key set equals the 14 planned fields. A completed answer sentinel is absent from the response, `owner_login_key` is absent, paths `approved.mp4` and the synthetic cache path are absent, and there is no ETag. Success, 401, 422, and the fixed `500 TIMELINE_UNAVAILABLE` body use `Cache-Control: private, no-store`. |
| C21 | PASS | `test_inventory_matches_both_compositions_and_route_policies` compares the tracked inventory to the rendered route set and does not write it. `write_text` is absent from that test. The Timeline row says verified identity, no added route capability, and caller-specific current, approved, or legacy projection. Ingress `route_policies_match_the_application_route_inventory` passed. The route-policy table was not in the diff. |
| C22 | PASS | The results container is an `ol` of `li` rows. Filter controls have visible labels and 44 px minimum height. Title text is assigned with `textContent`, including a script-like string, and loading performs one list request. Filter changes and search reset the offset to zero and restore focus to the initiating control; pagination clears the opener so focus moves to the Timeline heading. Details opened from a Timeline hash restore that hash and focus the originating title, or the heading if the row is gone. Gallery details still mark Gallery. Rendered keyboard and 320 px acceptance is not claimed. The desktop column header and per-field visually hidden labels from plan §7.1 are absent; see deviations. |
| C23 | PASS | `app.js` hunks are Timeline parsing, chronicle rendering, review-button copy, and the details-return branch. History still renders `.kronika-card`. The CSS card padding and 36 px card slot remain. Node gallery still-image, GIF, playback-handoff, and cover tests passed inside the 48. The local web selection passed 43 tests, including the gallery and details filters. |
| C24 | PASS | `test_timeline_loading_never_calls_research_or_preview_generation` records zero research-runtime calls and no preview URL in the list body. The reader has no provider, filesystem, or generation call. The allowlist contains no secret, host, route-policy, schema, or public-composition path. |

## Tests and validation

Commands, each once, from `/Users/agile/Projects/kronika`, with worktree HEAD `264a040e104e7495ce649fa583c4f0f3c1241b7c`:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33
```

PASS.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/integration/persistence/test_timeline_repository.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_timeline_api.py tests/contract/test_records_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_kronika_access_inventory.py tests/contract/test_gallery_preview_api.py tests/contract/test_content_audience_policy.py tests/contract/test_research_requests_api.py tests/contract/test_workspace_media.py tests/contract/test_public_published_uds.py tests/unit/application/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_content_audience_requester_private.py -q -p no:cacheprovider
```

258 passed in 35.06s.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
```

43 passed, 164 deselected in 6.14s.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/contract/test_tailscale_ingress_security.py -k 'route_policies_match_the_application_route_inventory or requester_private_media_detail_reaches_application_through_ingress or missing_identity_login_is_rejected' -q -p no:cacheprovider
```

3 passed, 83 deselected in 2.14s.

```text
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
```

48 passed, 0 failed, 0 skipped, 0 cancelled.

```text
git diff --check
git status --short
```

`git diff --check` on `b66ec8f..264a040` was clean. `git status --short` was empty. These counts were produced by this run. They match the implementation report's counts and do not rely on it.

## Source and security

The three arms are disjoint: `media:<logical_media.id>`, `question:<final_operation_id>` for a completed search or research record, and `question:<operation_id>` for a request that is not a consistent completed record. A contradictory `record_id`, or `saved` without that record, sets an integrity flag and the whole authorized read becomes `TimelineUnavailableError` before a page is returned. Media requires `gallery.read`. Completed records follow `decide_bound_read`. Unfinished requests require `research.run` plus owner or the existing request administrator. Binding wins over publication and requester access. Household approved media forces status `analyzed` and approved title, category, and location columns. No new endpoint, capability, migration, or client-side union was added.

## API and payload

`GET /api/timeline` keeps its URL. Limit and offset keep the existing clamp. Kind, category, trimmed 240-code-point search, status group, visibility, and publication are validated server-side. The response is the page envelope plus the fixed item object. SQLAlchemy errors and integrity failures use the fixed 500 message. The reader does not put answers, paths, filenames, cache state, provider errors, or login keys into the item.

## UI and frozen views

The Timeline list is a compact chronicle, not a Gallery grid. Links encode media, record, and request ids. Preview slots reuse the existing lazy image and icon fallback. History cards and the Gallery player path were not rewritten. Two static gaps remain and do not change the authorization result: chronicle rows have no column header or per-field visually hidden label, and a same-query transport failure marks the page stale while hiding the Retry button. Plan §7.2 asks for that Retry control. Rendered 320 px behavior was not tested; this grant forbids browser acceptance.

## Documentation and inventory

ADR-0087 is Accepted, dated 2026-11-09, and matches the Cooperator acceptance in `00_notes.md`: complete authorized read projection, creation order, owner and administrator current access, household approved or legacy access, no migration, and no synthetic records. The ADR index records only the approved-only membership sentence as superseded. ADR-0082 through ADR-0086 bodies are unchanged. `AGENTS.md`, `SPEC.md`, and `SECURITY.md` state the new membership and keep administrator access as application content. The inventory test is an exact read-only comparison.

## Allowlist and negative allowlist

`git diff --name-only b66ec8f..264a040` is exactly the 29 paths in the prompt. The stat is 29 files, 2665 insertions, 388 deletions. No `.ap` path, gitlink, dependency, schema, migration, audience-policy, preview route, public composition, ingress table, extension, deploy, or Gallery player body changed. `record_access.py` only deletes unused `timeline_includes`. `records.py` changes only the Timeline port method.

## Deviations and near-misses

`test_timeline_preview_locator_round_trip_and_withdrawal` checks a private owner locator and Bob's empty page. It does not withdraw or round-trip a preview GET. Those assertions live in the records API tests.

`test_timeline_binding_precedes_legacy_publication_and_contributions` does not insert a contribution. `test_timeline_sql_matches_existing_audience_policy` does not call `ContentAudiencePolicy`.

The planned UI test that restores Details focus was not added. The function `kronikaFocusTimelineReturn` is present and the Gallery branch remains.

`kronikaAcceptList` clears `error` on a same-query failure and sets `stale`. `kronikaLoadTimeline` then hides `#kronika-timeline-retry`. A first-load failure still shows Retry.

`kronikaRenderChronicle` does not add the planned aria-hidden column header or visually hidden field names. Narrow CSS wraps the values and does not add visible field names.

None of these change a visibility predicate, payload key, or route.

## Residual risks and missing evidence

Rendered Timeline acceptance at 320 px and with the keyboard remains Michal's, after a later publication and NUC refresh. This audit made no browser, NUC, provider, or secret contact.

Upload, YouTube, and X success and non-success rows were compared in source and not executed through the Timeline reader. A private reanalysis run after household approval was not inserted. `EXPLAIN QUERY PLAN` timings were not part of the authorized commands and were not recorded here. Offset pagination can still move between separate HTTP requests, as ADR-0087 already says. The mixed-source sort and literal search may scan.

## Smallest next step

Decide whether to publish `264a040e104e7495ce649fa583c4f0f3c1241b7c` as accepted, or first apply one bounded UI correction for the stale Retry control and the missing chronicle field labels. This acceptance grants neither publication, deployment, nor closure.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

Changed files: none in the Kronika repository. This report is the only write.

Git result: read-only inspection. No add, commit, push, or other Git write.

Authority expiry: submission of this terminal acceptance report ends the grant. No correction, publication, deployment, production, or closure authority remains.

Orchestration critique:
MEASURED: same-query Timeline refresh failure hides Retry, and chronicle rows omit the planned field labels; evidence is `kronikaAcceptList` / `kronikaLoadTimeline` and `kronikaRenderChronicle` against plan §7.1–§7.2; effect is a recovery-control and labelling gap, not an authorization change; smallest correction is one UI-only change to those two functions and their tests.
LEAD: Timeline fixtures never execute upload, YouTube, X, or a post-approval reanalysis run; cheapest useful check is one repository test that compares those states with `ContentAudiencePolicy` and asserts the household status stays `analyzed`.
