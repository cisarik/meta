### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-TCC-ACC-05 — full fresh re-acceptance after the rendered Timeline UI polish
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: 5be63b13b45a051ab76ad3c444ad769b11ff89cc
End commit: 65772c6028c07edcab47b6928dbb31e30876c70a
Report justification: final-acceptance
Logical-whole closure: not-closed
Result artifact or commit: 65772c6028c07edcab47b6928dbb31e30876c70a
Result evidence: fixed candidate, source inspection, and the selected gates below
```

This session is a fresh independent audit. It did not plan, implement, correct, or polish the candidate, and it did not participate in a prior acceptance. Native Plan mode was off. Prior reports were treated as claims. The corrected candidate is accepted.

## Acceptance record

```text
Acceptance candidate: 65772c6028c07edcab47b6928dbb31e30876c70a
Acceptance owner map: 01_report_02.md section 10 rows C01-C24; ADR-0087; 02_report_01.md section 7; 02_report_02.md; 03_report_00.md; 04_report_00.md; 02_report_04.md
Acceptance allowlist: exactly the 29 changed paths in section 2
Acceptance risk claims: C01-C24, plus the corrected UI claims in section 4
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
| Checkout | `/Users/agile/Projects/kronika`, standalone, branch `main`, tracking `origin/main` |
| HEAD | `65772c6028c07edcab47b6928dbb31e30876c70a` |
| Parent | `5be63b13b45a051ab76ad3c444ad769b11ff89cc` |
| Public `refs/heads/main` | `5be63b13b45a051ab76ad3c444ad769b11ff89cc` via `git ls-remote` |
| Local tracking | `origin/main...HEAD` is `0 1`; the candidate commit is the one unpushed commit |
| Worktree | Clean before review and after the selected tests |
| Final diff `b66ec8f..65772c6` | Exactly the 29 allowlisted paths, 3249 insertions, 392 deletions |
| Polish delta `5be63b1..65772c6` | Exactly the four UI paths, 502 insertions, 87 deletions |
| `.ap` gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `./.ap/ap doctor` | PASS |
| `ap project check --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc` | PASS, twice |
| Environment warning | Sanitized classes `GIT_CONFIG_VALUE_0`, `SSH_AUTH_SOCK`, `PATH`, `GIT_CONFIG_KEY_0`, `GIT_CONFIG_COUNT`; no values |
| `git diff --check` | Clean |

`b66ec8f` is an ancestor of HEAD. The candidate was not moved. No repository file was edited.

## C01–C24

| ID | Verdict | Evidence |
|---|---|---|
| C01 | PASS | A private completed question is visible to Alice and Ada and absent for Bob, and the direct record reads are 200/404/200 (`test_timeline_visibility_matches_direct_reads`). The media arm includes a bound row for its owner and excludes it for another member unless the approved-family predicate matches. |
| C02 | PASS | Administrator current access uses `media.workflow.read` for media and completed records, and `role == admin` or `records.approve` for unfinished requests. Ada reads Alice's private question. The snapshot test reads unbound media as admin. The diff adds no capability, route, host, or secret privilege. |
| C03 | PASS | After approval, Bob receives the frozen question "Before save" with `read_decision=approved` and status `saved`. A search for the later working question returns zero; the owner search returns the working text (`test_timeline_household_uses_only_approved_labels_and_status`). Approved question text is `json_extract` of `$.document.question_text`, with an integrity failure instead of a current-text fallback. |
| C04 | PASS | Anonymous `GET /api/timeline` is 401 `IDENTITY_REQUIRED` with `Cache-Control: private, no-store`. The public composition returns 404 (`test_timeline_denies_anonymous_and_is_absent_from_public_composition`). |
| C05 | PASS | A medium with two locations and no analysis run is one `not_requested` item. The reader selects and rolls back; it does not insert a synthetic record (`test_timeline_union_deduplicates_media_and_saved_requests`). |
| C06 | PASS | An approved decision forces media status `analyzed`. A current decision uses the latest `automatic_post_catalog` run ordered by `created_at_ms DESC, id DESC`, or `not_requested`. Household approved questions stay `saved`. The selected tests do not insert a later pending run; inclusion does not depend on that later state. |
| C07 | PASS | Failed and cancelled states are projected only after the audience predicate. They are not an inclusion exception. The selected Timeline fixtures do not insert analysis or request state `failed`; the status group still maps those states, and a private row stays out of another member's set. |
| C08 | PASS | Alice's `running` request is one `question:` item with a null record id. Bob's total is zero (`test_timeline_request_lifecycle_and_saved_transition`). The request arm is owner or request-admin only and always `visibility=private`. |
| C09 | PASS | Completing the document for `op-live` and then marking the request `saved` leaves total 1, status `saved`, and item id `question:op-live`. The request arm excludes a consistent completed record, so the validating-to-saved interval is one question item. |
| C10 | PASS | The owner preview locator matches the bound location and Bob's private page is empty (`test_timeline_preview_locator_round_trip_and_withdrawal`). Withdrawal is executed in `test_timeline_membership_follows_owner_admin_and_household_visibility`: Bob's total becomes 0, and Alice and Ada retain `publication_state=withdrawn`. That preview test does not itself withdraw. |
| C11 | PASS | Chronicle order is `created_at_ms DESC, item_id ASC`. Media uses `logical_media.created_at_ms`. Questions prefer request `admitted_at_ms`. Approval is not the sort key. |
| C12 | PASS | An unbound published medium is readable as `legacy`. A binding is tested before publication or requester access. A private binding removes the other member's row (`test_timeline_binding_precedes_legacy_publication_and_contributions`). |
| C13 | PASS | `_requester_ids` unions the caller's upload publication, YouTube states `cataloged` and `duplicate_resolved`, and a cataloged X asset joined to the caller's post claim. A bound private record is not admitted by a requester stamp. The audience-policy test compares the Timeline set with the existing policy. |
| C14 | PASS | Locations, runs, and requester ids are collapsed before the union. A saved request and its completed record produce one `question:` item. `UNION ALL` is safe because the request arm excludes a consistent completed record. |
| C15 | PASS | Equal timestamps order by `item_id` ascending (`test_timeline_filters_counts_and_tie_order_use_authorized_projection` and `test_timeline_item_identity_survives_binding_and_save`). Save and binding keep the same item id and creation time. |
| C16 | PASS | Kind, category, visibility, publication, status, and escaped `NOCASE` text filters are applied in `_filtered` before count and page. Bob's search for Alice's private text returns total 0. Invalid status and a category without `kind=media` return 422 with `private, no-store`. |
| C17 | PASS | `read_page` issues sqlite3 `BEGIN` before count, page, and the optional locator select, then `ROLLBACK`. In WAL mode, a row committed after the count select stays out of both the total and the items (`test_timeline_count_page_and_locators_share_one_snapshot`). |
| C18 | PASS | An empty page uses 2 data SELECTs. A question page uses 2 and does not select `answer_text` or `relative_path`. A mixed video/image page uses 3. Still images receive a null locator (`test_timeline_page_query_count_is_constant`). Page size does not add further statements. |
| C19 | PASS | Approved locators use the minimum available approved location. Current and legacy locators use the minimum available physical location, and only for `video` and `animated_image`. The UI keeps the kind icon, reveals the image only when ready, and does not request record or request detail while painting the list. Gallery-preview denial remains on the unchanged preview route. |
| C20 | PASS | Timeline items are exactly the 14 chronicle keys. `owner_login_key` is absent. The answer sentinel is absent. Every Timeline response, including 401 and 422, sends `Cache-Control: private, no-store` and no ETag (`test_timeline_contract_is_bounded_sanitized_and_no_store`). |
| C21 | PASS | `GET /api/timeline` stays a verified-identity route with no new capability. The inventory row describes the authorized union and says filters cannot widen it. `test_inventory_matches_both_compositions_and_route_policies` passed inside the 258. The ingress route-policy selection passed 3 tests. |
| C22 | PASS | The results region is an `ol` of `li` rows. The desktop header is `aria-hidden`. Kind keeps a visually hidden label. Status and visibility words are visually hidden and also on `title`. Filter controls are labelled listboxes with 44 px targets. The five C22 presentation rows below pass. Rendered 320/390 px observation was not authorized. |
| C23 | PASS | `app.js` hunks from `b66ec8f` stay in the shell route and Timeline region. Details return still restores the Timeline route and focuses the prior title. Gallery card hover keeps `translateY(-2px)`. The focused shell selection passed 43 tests, and the Gallery, Details, GIF, still-image, and cover Node tests passed inside the 53. |
| C24 | PASS | `GET /api/timeline` with a substituted research runtime leaves `submit_pending`, `poll_once`, and `release_remote_pending` at zero calls and does not mention gallery-preview generation. The reader has no filesystem or provider call. The allowlist contains no provider, capture, generation, or secret path. |

## C22 presentation claims

| Claim | Verdict | Evidence |
|---|---|---|
| C22-Dropdowns | PASS | `index.html` replaces the four Timeline `<select>` elements with labelled buttons. Each trigger has `aria-haspopup="listbox"`, `aria-expanded`, `aria-controls`, and `aria-labelledby`. Each panel is `role="listbox"`; each option is `role="option"` with `aria-selected`. `kronikaSetupTimelineMenus` opens on click, ArrowDown, Enter, and Space; moves with ArrowUp and ArrowDown; selects with Enter, Space, and click; closes on Escape and restores focus; closes on an outside click. Choosing a value writes the trigger value and assigns the route at offset 0. Search submit and clear still call `kronikaTimelineRouteFromControls(0)`. The Node test drives click, ArrowDown, Enter, Escape, outside click, and clear. Filter buttons inherit `min-height: 44px`. |
| C22-NoDate | PASS | The header is Preview, Item, Kind, Status, Visibility. Row rendering appends preview, title, kind, status, and visibility, and no `<time>`. The desktop grid is `4.75rem minmax(0, 1fr) 5.5rem 4.5rem 6.25rem`, so the title receives the flexible column. At `max-width: 720px` the header is hidden, the row becomes `36px minmax(0, 1fr)`, and kind, status, and visibility wrap into column 2. `#kronika-timeline` sets `overflow-x: hidden`. No `.kronika-chronicle__added` rule exists. |
| C22-Emoji | PASS | Status glyphs cover `not_requested`, the in-progress states, `analyzed`/`saved`, `cancelled`, and the failure states, with "Unknown" and `•` as the leftover pair. Publication glyphs cover withdrawn, legacy publication, approved or household, and private. The glyph node is `aria-hidden`; the words are visually hidden and copied to `title`. The five-row Node fixture checks Unanalysed, Analysing, Analysed, Analysis failed, and Cancelled, with the matching publication words. Meaning is carried by the glyph plus text. |
| C22-Motion | PASS | Row hover and focus-within change only background and an inset accent shadow, over `160ms ease`. The open panel uses one `140ms` `header-menu-in` animation. `prefers-reduced-motion: reduce` sets `animation: none` and `transition: none` on the row and the panel. Chronicle rows do not use the Gallery card `translateY(-2px)` rule. |
| C22-Polish | PASS | The filter bar, uppercase labels, row separators, and green accent tokens stay in the existing dark palette. Rows remain a list with a 36 px preview, not Gallery cards. The new menu rules are scoped to `.kronika-menu` and `.kronika-chronicle`. |

## Tests and validation

Commands were run from `/Users/agile/Projects/kronika` with baseline `5be63b13b45a051ab76ad3c444ad769b11ff89cc`. HEAD stayed `65772c6028c07edcab47b6928dbb31e30876c70a`.

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc
```

PASS. The same sanitized-environment warning as the gate. No values.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc --operation test-focus -- tests/integration/persistence/test_timeline_repository.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_timeline_api.py tests/contract/test_records_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_kronika_access_inventory.py tests/contract/test_gallery_preview_api.py tests/contract/test_content_audience_policy.py tests/contract/test_research_requests_api.py tests/contract/test_workspace_media.py tests/contract/test_public_published_uds.py tests/unit/application/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_content_audience_requester_private.py -q -p no:cacheprovider
```

258 passed in 38.70s. Exit 0.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
```

43 passed, 164 deselected, in 6.34s. Exit 0.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc --operation test-focus -- tests/contract/test_tailscale_ingress_security.py -k 'route_policies_match_the_application_route_inventory or requester_private_media_detail_reaches_application_through_ingress or missing_identity_login_is_rejected' -q -p no:cacheprovider
```

3 passed, 83 deselected, in 1.97s. Exit 0.

```text
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
```

53 passed, 0 failed, in 194.48ms. The files contribute 30, 2, 5, 8, and 8 tests. Exit 0.

`git diff --check` was clean. `git status --short` was empty. `git rev-parse HEAD` remained the candidate.

Changed files: none in the repository. This report is the only write.

Git result: read-only inspection and one public `git ls-remote`. No fetch, stage, commit, or push.

## Source and security findings

No source or security defect fails a matrix row. The three arms stay disjoint. Household rows require family visibility, an approval projection, and completion. Unfinished requests stay private to the owner or the existing request administrator. Timeline responses do not carry owner keys, answers, paths, or provider errors. No new route capability, public composition route, or secret appears in the diff.

## API and payload findings

`GET /api/timeline` still requires a verified login inside the adapter and serializes the 14-field chronicle item. Other record payloads are unchanged: personal history can still include `preview_location_id`, and administrator inventory does not. Invalid filters return 422. Anonymous callers receive 401. The public app does not install the route. Count, page, and locator selection share one sqlite3 read transaction.

## UI and frozen-view findings

The polish is confined to the four UI paths. Route parsing, hash building, offset reset, search, clear, Retry, pagination, preview attachment, and the Timeline return focus are still present. Gallery and Details renderer bodies are outside the `app.js` hunks. The Node gallery and playback tests passed.

One keyboard near-miss does not fail C22-Dropdowns. `Enter` and `Space` inside an open panel call `chooseMenu` with `panel._kronikaIndex`. That index advances on ArrowUp and ArrowDown, and on option click. The option buttons remain tabbable while the panel is open, and Tab does not update the index. A Tab followed by Enter can therefore commit a different option than the focused one. The required arrow, Escape, outside-click, and focus-return path is implemented and covered by `tests/kronika_ui.test.js`.

The listbox options are buttons inside `li` elements. The panel has `role="listbox"` and the buttons have `role="option"`, but the `li` is an intervening element without `role="presentation"`. This audit had no browser or assistive-technology session.

## Documentation and inventory findings

`SERVER.md` lines 85–88 now say that another household member does not see a completed record until administrator approval, and that the owner and an application administrator see their authorized work in the chronicle. Lines 115–121 state the same authorized union. `SPEC.md` requires the compact semantic list and does not require a visible Added column. The inventory row for `GET /api/timeline` matches the implemented predicate. The inventory equality test passed.

ADR-0087 lines 47–48 still say the compact Timeline list shows kind, title, creation date, lifecycle status, and visibility or publication state. The polished header and row renderer show no creation date. Ordering still uses creation or admission time. The sentence is presentation drift. It was outside the four-path polish delta, so this candidate could not amend it. It does not change authorization.

## Allowlist and latest-delta review

The final diff and the polish delta match section 2 exactly. No `.ap` gitlink change, dependency file, schema file, migration, audience-policy file, preview route, public composition, identity definition, ingress table, extension, deploy script, or Gallery player body is in either diff. The polish delta is `app.js`, `index.html`, `styles.css`, and `tests/kronika_ui.test.js`. The new Node tests add the listbox, glyph, grid, and reduced-motion assertions. They do not remove the inert-text, route, Retry, preview, or pagination expectations.

## Deviations and near-misses

The Tab-versus-arrow index near-miss and the intervening `li` are recorded above. Neither fails the stated keyboard contract, and neither was corrected.

Rendered horizontal scrolling at 320 px and 390 px was not observed. The source evidence is the 720 px wrapping grid and `overflow-x: hidden` on `#kronika-timeline`.

## Residual risks and missing evidence

Browser, assistive-technology, NUC, provider, secret, and private-media evidence were not authorized and were not collected. Cooperator-rendered acceptance of this polish remains outside this report. Offset pages can still move between separate HTTP requests. The mixed-source order and literal search may scan; no new index was added.

Failed analysis and failed request rows were not inserted by the selected Timeline fixtures. Their sharing behavior follows the same audience predicate as the executed private and running rows.

## Smallest next step

The Orchestrator decides whether to publish `65772c6028c07edcab47b6928dbb31e30876c70a`. Updating the one ADR-0087 presentation sentence is a separate documentation decision. This report grants no publication, deployment, or closure.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

```text
Orchestration critique:
MEASURED: ADR-0087 lines 47–48 still say the compact list shows the creation date; the polished header and `kronikaRenderChronicle` render no Added column or `<time>`; effect is a stale presentation sentence while ordering still uses creation time; smallest correction is to remove "creation date" from that one sentence.
LEAD: Enter inside an open Timeline listbox uses `panel._kronikaIndex`, which Tab does not update; cheapest useful check is one Tab-then-Enter pass on a Timeline filter after the menu is open.
```

Authority expiry: this terminal report ends the grant. No further correction, publication, deployment, production, or closure authority remains.
