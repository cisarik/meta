### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-TCC-ACC-04 — full fresh re-acceptance after the two UI corrections
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: 264a040e104e7495ce649fa583c4f0f3c1241b7c
End commit: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Report justification: final-acceptance
Logical-whole closure: not-closed
Result artifact or commit: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Result evidence: fixed candidate, source inspection, and the selected gates below
```

This session is a fresh independent audit. It did not plan, implement, or correct the candidate, and it did not participate in the first acceptance. Native Plan mode was off. Prior reports were treated as claims. The corrected candidate is accepted.

## Acceptance record

```text
Acceptance candidate: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Acceptance owner map: 01_report_02.md section 10 rows C01-C24; ADR-0087; 02_report_01.md section 7; 02_report_02.md; 03_report_00.md
Acceptance allowlist: exactly the 29 changed paths in section 2
Acceptance risk claims: C01-C24, plus the two corrected UI claims in section 4
Acceptance control matrix: 01_report_02.md section 10, fixed
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Repository gate

| Check | Result |
|---|---|
| Checkout | `/Users/agile/Projects/kronika`, standalone, branch `main`, tracking `origin/main` ahead 2 |
| HEAD | `1bc10a364ddf3fba15fad62e9036183ab75e1a46` |
| Parent | `264a040e104e7495ce649fa583c4f0f3c1241b7c` |
| Public `refs/heads/main` | `b66ec8f50860ace624f6be1fd3ad63f521edcd33` via `git ls-remote` |
| Worktree | Clean before review and after the selected tests |
| Final diff | Exactly the 29 allowlisted paths, 2830 insertions, 389 deletions |
| Correction delta `264a040..1bc10a3` | Exactly the four UI paths, 181 insertions, 17 deletions |
| `.ap` gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `./.ap/ap doctor` | PASS |
| `ap project check --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c` | PASS, twice |
| Environment warning | Sanitized classes `GIT_CONFIG_VALUE_0`, `SSH_AUTH_SOCK`, `PATH`, `GIT_CONFIG_KEY_0`, `GIT_CONFIG_COUNT`; no values |
| `git diff --check` | Clean, including `b66ec8f..HEAD` |

The candidate remains local and unpushed. No repository file was edited.

## C01–C24

| ID | Verdict | Evidence |
|---|---|---|
| C01 | PASS | Private bound media is visible to the owner and absent for another member. `test_timeline_sql_matches_existing_audience_policy` gives Bob only the unbound published medium. `test_timeline_titles_stay_on_the_approved_projection` keeps the approved media projection. The named API visibility test covers a private question: Alice and Ada total 1, Bob total 0, and the direct record reads are 200/404/200. |
| C02 | PASS | Administrator current access includes another owner's private question, private media, and unbound media. Media and completed records use `media.workflow.read`; unfinished requests use `role == admin` or `records.approve`, matching `decide_bound_read` and `research_api._is_admin`. Both ordinary roles already include `gallery.read` and `research.run`. The diff adds no capability, route, host, or secret privilege. `test_timeline_count_page_and_locators_share_one_snapshot` reads an unbound medium as admin. |
| C03 | PASS | After approval, Bob receives the frozen question and a search for the later working question returns zero (`test_timeline_household_uses_only_approved_labels_and_status`). Approved question text is `json_extract` of `$.document.question_text` with an integrity failure instead of a current-text fallback. Media household reads use the approved title, category, and location. |
| C04 | PASS | `test_timeline_denies_anonymous_and_is_absent_from_public_composition`: anonymous `GET /api/timeline` is 401 `IDENTITY_REQUIRED` with `private, no-store`; the public composition returns 404. |
| C05 | PASS | A medium with two locations and no analysis run appears once as `not_requested` with the untitled fallback (`test_timeline_union_deduplicates_media_and_saved_requests`). The reader issues `SELECT`, then `ROLLBACK`. It does not insert a synthetic record. |
| C06 | PASS | Approved media status is forced to `analyzed`. A current read uses the latest `automatic_post_catalog` run ordered by `created_at_ms DESC, id DESC`, or `not_requested`. Household selection of the approved decision is executed. A later pending or failed run was not inserted; status is that same decision, not a second audience predicate. |
| C07 | PASS | Failure is a status on the already-authorized arm. Private media and another member's request are excluded before status is shown. No selected fixture uses analysis or request state `failed`. The inclusion SQL has no failure exception that widens the set. |
| C08 | PASS | Alice's unfinished request keeps `question:` identity. Her `running` request is visible with a null record id, and Bob's total is zero. Ada receives Alice's unfinished request. The request arm projects `lifecycle_state`. `submitting`, `validating`, and `cancel_requested` were not inserted separately. |
| C09 | PASS | A completed record whose request is still `validating` contributes one `question:` item with status `saved`. After the request is marked `saved`, the API total remains 1 and the item id stays `question:op-live`. |
| C10 | PASS | The named preview test checks the owner locator and Bob's empty private page. It does not withdraw. Withdrawal is executed in `test_timeline_membership_follows_owner_admin_and_household_visibility`: Bob's total becomes 0, and Alice and Ada retain `publication_state=withdrawn`. `test_withdrawn_preview_is_denied_even_with_a_cached_etag` returns 404 `no-store` on `If-None-Match` and does not call the preview service again. Preview authorization in `gallery_preview_api.py` runs before the 304 branch. That route file is outside the diff. |
| C11 | PASS | `test_withdrawal_keeps_timeline_position_and_snapshot` keeps `created_at_ms == 5` across approval and withdrawal. Chronicle order uses `logical_media.created_at_ms` or request `admitted_at_ms`, not approval time. |
| C12 | PASS | Bob can read an unbound published medium and loses it after a private binding. The media decision checks the binding before publication or requester access, matching `ContentAudiencePolicy.read_decision`. The contribution fixture is not inserted in that test. |
| C13 | PASS | `_requester_ids` matches the live predicates: upload publication joined to the caller's session with no extra success filter; YouTube `cataloged` and `duplicate_resolved`; X asset `cataloged` joined to the caller's post claim. A bound private record stays excluded even when a requester stamp exists. No selected Timeline test executes those three sources. |
| C14 | PASS | Two locations produce one `media:` item. A saved request and its completed record produce one `question:` item, including while the request is still `validating`. Runs are reduced to rank 1. Requester ids use `UNION`. `media_id` is unique on records, approved media, metadata, and publication. |
| C15 | PASS | Equal timestamps order by `item_id` ascending. The tie-order test matches Python's sort of those ids. Save does not change chronicle identity or `created_at_ms`. |
| C16 | PASS | Kind, text, status, and visibility filters are applied inside `_filtered` before count and page. Bob's search for Alice's private text returns total 0. Invalid status and a category without `kind=media` return 422 `private, no-store`. The UI sends category choices as `kind=media` plus `content_category`. |
| C17 | PASS | The reader executes `BEGIN` on the sqlite3 connection before the selects and `ROLLBACK` after them. In WAL mode, a row committed after the count select stays out of both the total and the items. |
| C18 | PASS | Instrumented cursor events: empty page 2 selects, question-only page 2, mixed video-plus-still page 3. Still images get a null locator. The statements do not contain `answer_text` or `relative_path`. Limits 1 and 100 change only `LIMIT`. |
| C19 | PASS | Approved household locators use `min(location_id)` among available approved locations. Current and legacy reads use the minimum available physical location. A working-only location is absent from Bob's payload and present for Alice and Ada. The image is `alt=""` and `aria-hidden`, with no generation call from `GET /api/timeline`. |
| C20 | PASS | `test_timeline_contract_is_bounded_sanitized_and_no_store` locks the item keys, excludes `SECRET-ANSWER` and `owner_login_key`, and requires `private, no-store` without an ETag. The timeline serializer has no path, filename, cache, or provider field. |
| C21 | PASS | The inventory row for `GET /api/timeline` is verified identity, no added route capability, and the caller-specific projection. `test_inventory_matches_both_compositions_and_route_policies` is inside the 258 passing tests. The ingress selection passed 3 tests: route-policy equality, requester private detail, and missing-identity login rejection. |
| C22 | PASS | The list is an `<ol>` of `<li>` rows. Filter controls are labelled. Title links encode media, record, and request ids through text nodes. The two corrected claims below close the previous Retry and label gaps. Rendered 320/390 px and keyboard acceptance remain Michal's. |
| C23 | PASS | Gallery and Details player bodies are outside the diff. Details return special-cases only a Timeline origin and still marks every other return as Gallery. The selected shell, details, preview, gallery, still-image, GIF, playback, and cover tests passed. |
| C24 | PASS | `test_timeline_loading_never_calls_research_or_preview_generation` records zero research-runtime calls and no `gallery-preview` text. The reader has no filesystem or provider call. The allowlist adds no secret or host surface. |

## C22-Retry

Verdict: PASS.

`kronikaAcceptList` keeps the previous items only when `queryKey` matches and the page already has rows, then sets `stale` and clears `error`. A different query, including a changed filter, clears the rows and sets the error. `queryKey` includes offset, the route's kind, category, text, status, visibility, publication, and login.

`kronikaLoadTimeline` shows `#kronika-timeline-retry` on the error path and returns without rendering the failed query. On the stale path it sets `retry.hidden = !list.stale`, so Retry stays visible, and it renders the retained items with "Showing the last loaded page. It was not refreshed." A successful load hides Retry.

The click handler calls `kronikaLoadTimeline` with `kronikaParseRoute` of the current hash. It does not call `focus` and does not schedule a timer. The correction diff adds no automatic retry.

`tests/kronika_ui.test.js` covers the same-query case, including one extra request for the same URL and unchanged `activeElement`; the changed-query case, which removes the previous title and does not use the stale copy; and the existing failed-refresh test, which now also requires Retry to be visible. The first-load failure uses the existing error branch because there are no retained rows.

## C22-Labels

Verdict: PASS.

`index.html` places `div.kronika-chronicle-header` with `aria-hidden="true"` immediately before `<ol id="kronika-timeline-results">`. The six header cells are Preview, Item, Kind, Added, Status, and Visibility. The header is not inside the list.

Each row appends Kind, Status, and Visibility through `kronikaChronicleLabeled`, and Added through a `<time datetime>` whose first child is a visually hidden "Added" label. The title link's text is only the title. The preview image remains empty-alt, aria-hidden, and `pointer-events: none`.

Desktop header and row grids both use `36px minmax(0, 1fr) auto auto auto auto`. At `max-width: 720px` the header is `display: none`, the row becomes `36px minmax(0, 1fr)`, and the four fields move to column 2, so the list stays one item per row. The same query overrides `.visually-hidden` on `#kronika-timeline .kronika-chronicle__label` with equal or higher specificity and `!important`, which makes those labels visible. `#kronika-timeline { overflow-x: hidden }` is in that same breakpoint, so 320 px is included. Title links, rows, filter controls, and the header keep `min-height: 44px`. The correction does not change `.kronika-action`, whose shared `min-height` remains 40 px for pager and Retry.

The header test checks the source order, the 720 px rules, and the four row labels. Existing status, visibility, and kind assertions now read the value child and still require "Saved", "Private · Unpublished", and "General". No expectation was removed.

Rendered pixel measurement was not performed. This grant forbids browser acceptance.

## Tests

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c
```

PASS. The same command had already passed before the test block. Both runs reported the sanitized-environment warning and exit 0.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/integration/persistence/test_timeline_repository.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_timeline_api.py tests/contract/test_records_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_kronika_access_inventory.py tests/contract/test_gallery_preview_api.py tests/contract/test_content_audience_policy.py tests/contract/test_research_requests_api.py tests/contract/test_workspace_media.py tests/contract/test_public_published_uds.py tests/unit/application/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_content_audience_requester_private.py -q -p no:cacheprovider
```

258 passed in 35.27s. Exit 0.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
```

43 passed, 164 deselected in 6.45s. Exit 0.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/contract/test_tailscale_ingress_security.py -k 'route_policies_match_the_application_route_inventory or requester_private_media_detail_reaches_application_through_ingress or missing_identity_login_is_rejected' -q -p no:cacheprovider
```

3 passed, 83 deselected in 2.06s. Exit 0.

```text
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
```

51 passed, 0 failed, 0 skipped, 0 cancelled. Exit 0.

```text
git diff --check
git status --short
```

`git diff --check` was clean for the worktree and for `b66ec8f..HEAD`. `git status --short` was empty.

## Source and security

The three arms stay disjoint. Media requires `gallery.read` and then the bound, approved-family, legacy-publication, or live-requester decision. Completed questions follow the same bound decision. Unfinished requests require `research.run` plus the owner or the existing request administrator, and a consistent completed record suppresses the request row. A contradictory `record_id`, or `saved` without that record, raises `TimelineUnavailableError` before a page is returned. The fixed 500 message is "The Timeline is unavailable."

The four-path correction does not change a predicate, payload key, query parameter, stored row, preview route, or Gallery player. Search remains a bound `LIKE` over the authorized title or question text, with `%`, `_`, and backslash escaped. Display truncation to 240 code points happens after the query.

## API and payload

`GET /api/timeline` keeps its URL, the 24/100 clamp, and server-side filter validation. Every timeline response, including 401, 422, and 500, uses `Cache-Control: private, no-store`. The item object matches the planned key set, including `read_decision` and one nullable `preview_location_id`. History and administrator record payloads still use their previous summary shape.

## UI and frozen views

The chronicle is a compact list. History remains cards. Closing Details from a Timeline hash reloads that route and focuses the originating title, or the Timeline heading if the row is gone. Closing Details from any other hash still marks Gallery. Retry does not move focus. No timeline row contains playback, approval, download, or provider controls.

## Documentation and inventory

ADR-0087 is Accepted, dated 2026-11-09, and matches the Cooperator acceptance in `00_notes.md`: complete authorized read projection, creation or admission order, owner and administrator current access, household approved or legacy access, no migration, and no synthetic records. The ADR index supersedes only ADR-0083's approved-only membership sentence. ADR-0082 through ADR-0086 bodies are unchanged. `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `README.md`, `PRODUCT.md`, and `ROADMAP.md` state the new membership. The inventory row matches the implementation and is enforced by the passing inventory test.

`SERVER.md` lines 115–121 state the authorized union. Lines 85–87, in the research paragraph, still say: "The shared Timeline does not receive a card until an administrator approves the completed record." That sentence was not in the correction delta and remains from the public baseline. It contradicts the boundary paragraph in the same file. It does not change runtime authorization.

## Allowlist and correction-delta review

`git diff --name-only b66ec8f..1bc10a3` is exactly the 29 paths in the prompt. `git diff --name-only 264a040..1bc10a3` is exactly `app.js`, `index.html`, `styles.css`, and `tests/kronika_ui.test.js`.

No `.ap` path, gitlink, dependency, schema, migration, `ContentAudiencePolicy`, preview or download route, public composition, ingress table, identity definition, extension, deploy script, or Gallery player body changed. `record_access.py` only deletes unused `timeline_includes`. `record_repository.list_timeline` delegates to `SqliteTimelineReader` and does not write. The `app.js` hunks outside the correction are route parsing, chronicle rendering, timeline loading, filter binding, and the Timeline return glue.

## Deviations and near-misses

The named timeline preview test does not withdraw or call the preview route. Those assertions are in the records API tests, which passed.

The binding test does not insert an upload, YouTube, or X claim. The audience-policy test does not call `ContentAudiencePolicy`. The predicates were compared in source.

Upload, YouTube, X, and a post-approval reanalysis run were not executed as Timeline fixtures. Limits 1 and 100 were not separate fixtures.

Pager and Retry buttons still use `.kronika-action` at `min-height: 40px`. Chronicle title links and filter controls are 44 px. The correction did not reduce those 44 px rules.

None of these change a visibility predicate, payload key, or route.

## Residual risks and missing evidence

Rendered Timeline acceptance at 320 px and with the keyboard remains Michal's, after publication and a NUC refresh. This audit made no browser, NUC, provider, or secret contact.

`EXPLAIN QUERY PLAN` was not part of the authorized commands. Offset pages can still move between separate HTTP requests, as ADR-0087 says. The mixed-source sort and literal search may scan.

The stale `SERVER.md` research sentence can mislead a later reader. The runtime union is the boundary paragraph and the tested reader.

## Smallest next step

Publish is an Orchestrator decision. The runtime candidate `1bc10a364ddf3fba15fad62e9036183ab75e1a46` meets C01–C24 and both corrected UI claims. One documentation sentence in `SERVER.md` still equates shared Timeline entry with approval; correcting it is optional before publication and is not authorized by this report. This acceptance grants neither publication, deployment, nor closure.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

Changed files: none in the Kronika repository. This report is the only write.

Git result: read-only inspection. No add, commit, push, fetch, or other Git write.

Authority expiry: submission of this terminal re-acceptance report ends the grant. No further correction, publication, deployment, production, or closure authority remains.

Orchestration critique:
MEASURED: `SERVER.md` lines 85–87 still say the shared Timeline receives no card until administrator approval; the sentence is unchanged from `b66ec8f` while lines 115–121 state the authorized union; effect is a contradictory current sentence, not a runtime or authorization defect; smallest correction is to replace that one sentence with the household-approval wording already used in the boundary paragraph.
LEAD: none
