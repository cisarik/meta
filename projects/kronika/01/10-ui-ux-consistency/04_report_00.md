### Report for ORCHESTRATOR_CHAT

Logical whole identity: ui-ux-consistency
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-UX-ACC-04 — final independent E2 UI acceptance of the corrected application shell
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: bbf776c462e1eb5eccb91eb027a85eee9055d2ec
End commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Report justification: final-acceptance
Logical-whole closure: not-closed
Result artifact or commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Result evidence: read-only inspection of the fixed candidate, the fourteen-path measured diff, the two-path micro-correction, and the exact selected gate and tests below

This session had no prior conversation about this whole. Native Plan mode was off. The candidate was not moved.

```text
Acceptance candidate: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Acceptance owner map: 01_report_01.md sections 6-7; 02_report_01.md; 02_report_02.md; SPEC.md shell requirements; ADR-0088
Acceptance allowlist: exactly the fourteen changed paths in section 2
Acceptance risk claims: header search slot and semantics; Timeline trim; History removal, fold and current marking; Publication-first filter alignment; listbox focused-option activation; no title underline; legacy eye glyph; durable documentation and ADR-0088; preserved closed whole 01/09 behavior; no API, authorization, payload, schema or stored-data change
Acceptance control matrix: 01_report_01.md sections 6-7, fixed; correction scopes 02_correction_01.md and 02_correction_02.md
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

Gate identity, re-established from the checkout and public read-only `git ls-remote`:

- HEAD `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` on `main`; parent `27aa5fd29f259ee27de109f37bb7cf88f255b93f`.
- Public `refs/heads/main` is `bbf776c462e1eb5eccb91eb027a85eee9055d2ec`. Local `main` is ahead 2. Worktree clean before and after the tests.
- `.ap` gitlink and submodule HEAD are `d7023cf037f6d17885c3ede5c04812c61640da50`.
- `./.ap/ap doctor`: PASS. `./.ap/ap project check --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec`: PASS. Both printed the non-failing sanitized-environment warning (`GIT_CONFIG_VALUE_0 SSH_AUTH_SOCK PATH GIT_CONFIG_KEY_0 GIT_CONFIG_COUNT`).

Changed files, relative to `bbf776c`, purpose limited to the shell correction: header search slot, Timeline trim, History removal and fold, Publication-first filters, ADR-0088 and owner-document wording, plus the `8646146` current-marking micro-correction. Measured stat: 14 files changed, 278 insertions, 519 deletions. Micro-correction stat: 2 files changed, 39 insertions, 2 deletions.

## Matrix

### A Header search — PASS

Source contract verified. Painted absence of a layout jump and of page overflow is NOT TESTED; the prompt assigns that to later rendered acceptance.

Both fields are `.header-search` in the header and share `grid-area: search`. Gallery remains the catalog field (`command-search-input`, suggestions, tag rail). Timeline is `form#kronika-timeline-search-form.header-search.kronika-timeline-search`, with the magnifier submit, hidden label, `maxlength="240"`, placeholder `Search timeline`, and the reserved clear slot. `.header-status-group` stays `grid-area: controls`. At `max-width: 900px` the header areas are `"brand controls"` / `"search search"`. `.kronika-timeline-search { margin: 0 }`.

`kronikaShowShell` shows only the Timeline field when `view === "timeline"`, only the Gallery field when the view is gallery and the route is not `details`, and hides both otherwise. The Node test `header search occupies one slot and only the active view is visible` passed for Timeline, Gallery, `#/search`, and `#/details/media-1`. Request and record views are `request` and `record`, so the same branch hides both fields.

Timeline submit still calls `kronikaTimelineRouteFromControls(0)`. That helper trims `q` and copies Kind, Status, Visibility, and Publication from the controls. `kronikaAssignHash` reloads when the hash is unchanged. Clear empties the input, focuses it, records it as the opener, syncs the clear button, and submits offset 0. `kronikaSyncTimelineControls` does not overwrite the input while it is `document.activeElement`. The test `Timeline search edits chrome only until an explicit submit or clear` passed: typing made no request, submit trimmed `q` and preserved the other filters while dropping offset, a second submit reloaded, and a focused draft survived a later load. `catalogLoads` stayed 0. No Gallery search or catalog-controller function appears in the `app.js` diff.

### B Timeline trim — PASS

`#kronika-timeline` now starts with `<h1 id="kronika-timeline-heading" class="visually-hidden" tabindex="-1">Timeline</h1>`, then `#kronika-timeline-filters`, then status, chronicle header, list, and pager. The visible hero, lede, and `Household sharing does not publish to the internet.` note are absent from `index.html`. `.visually-hidden` clips the heading without `display: none`, so `kronikaFocusRoute` can still focus `route.headingId` (`kronika-timeline-heading` for Timeline and for the History fold). `.kronika-hero` and `.kronika-lede` remain because Search, request, and Review still use them. No `.kronika-note` rule remains.

### C History removal — PASS

Browse contains only `#kronika-nav-timeline` and `#kronika-nav-gallery`. Actions remain Search, Research, and hidden Review. The `#kronika-history` section, its heading, status, list, pager, and retry control are gone. The question composer's former `#/history` link is `#/timeline`. `git grep` of the web shell finds no History nav, section, loader, or list state. Remaining `history` hits are the fold itself and an unrelated analysis-count string.

`kronikaParseRoute` maps `/history` and `/history/records` to the Timeline route with offset 0, empty filters, and `headingId` `kronika-timeline-heading`. `kronikaFollowHash` then replaces a `#/history...` address with `#/timeline` through `kronikaSetHashSuppressed` and loads Timeline. The test `removed History addresses fold to the Timeline and do not fetch the old list` passed: `#/history/records?offset=24` became `#/timeline`, offset parsed as 0, Timeline rows rendered, and no call URL contained `/api/research-requests`.

`kronikaLoadHistory`, `kronikaRenderQuestionChronicle`, `historyMode`, and the `questions` / `records` list, controller, and preview buckets are deleted. Clear, page-hide, and approval only reset the lists that remain. Question and record routes, `#/requests/...` and `#/records/...` links, and `/api/timeline` loading remain. No second list was added. No API module is in the diff.

### D Current marking — PASS

`kronikaMarkCurrent` maps `details` to `gallery`, `request` and `record` to `timeline`, and `review-shared` / `review-requests` to `review`; every other route name is used directly. The selector writes `aria-current="page"` only on the matching `data-kronika-nav` link and removes it from the others. The micro-diff is only that `request` / `record` mapping. The test `question detail routes keep Timeline current` passed for `#/requests/op-1`, `#/records/11111111-1111-4111-8111-111111111111`, `#/details/media-1`, and `#/review/shared`, and asserted that no History link or `history` current value exists.

### E Filters — PASS

Source contract verified. Painted alignment, popup visibility, and horizontal clipping are NOT TESTED.

DOM order inside `#kronika-timeline-filters` is Publication, Kind, Status, Visibility. Search is not in that form. `#kronika-timeline-publication.kronika-menu__trigger` uses `border-color: var(--accent-border)` and the soft-green background; expanded and focus-visible states use the stronger accent border.

The base toolbar is one column. From 721 px it is three equal columns and Publication spans `1 / -1`, so Kind, Status, and Visibility form the next row. From 1100 px the toolbar, chronicle header, and rows share `4.75rem minmax(0, 1fr) 9.5rem 9.5rem 10.5rem` with a 20 px gap, and Publication spans `1 / 3` (preview and title). Below 1100 px the compact row tracks `4.75rem minmax(0, 1fr) 5.5rem 4.5rem 6.25rem` remain. At `max-width: 720px` the toolbar stays one column, the chronicle header is hidden, and panels are full width. Status and Visibility panels are right-aligned from 721 px. Panels use `min(22rem, 60vh)` and vertical scrolling. The toolbar sets `overflow: visible`. Reduced motion disables chronicle, menu, nav, and search-prompt animation. The History `overflow-x: hidden` rule was removed with the History section.

### F Preserved shell behavior — PASS

Source contract verified. Touch behavior and assistive-technology output are NOT TESTED.

One `nav.kronika-nav` sits after `header.app-header` and before `main#main`. Browse holds Timeline and Gallery. Actions hold Search, Research, and Review. IDs, hashes, labels, `data-kronika-nav`, Review's initial `hidden`, opener assignment on nav click, and `kronikaFocusRoute` are intact. Action links use `border-radius: 0` and `margin-inline-start: auto`. Browse and action links have a 44 px minimum; the browsing bar at `max-width: 720px` is fixed to the bottom with 54 px targets, while actions stay in the header row at 44 px with `border-radius: 0`. Focus-visible outlines remain on nav links and title links.

`kronikaSetupTimelineMenus` sets `panel._kronikaIndex` from each option's focus listener. Enter and Space commit `options[index]`. Arrows, Escape, outside click, one-open behavior, and focus return to the trigger remain. Every Timeline option wrapper in `index.html` is `<li role="presentation">`. The test `Timeline listbox Enter and Space commit the option focused by Tab` passed, including a later arrow, a second menu opening, and Escape.

`.kronika-chronicle__title` sets `text-decoration: none` for the element, `:hover`, `:focus`, and `:focus-visible`, and `:focus-visible` keeps a 2 px accent outline. The underline at `styles.css` around the admin title button is a different control.

`kronikaShareGlyph` returns `↩` for withdrawn, `👁️` for `legacy_published`, `🏠` for approved or family, and `🔒` otherwise. `kronikaPublicationLabel` still returns `Private` or `Household` plus the publication label, including `Legacy publication`. The publication menu's legacy option is `data-glyph="👁️"` and `data-label="Legacy publication"`. The Timeline nav icon remains `🕰️`. The glyph test passed, including `👁️` / `Household · Legacy publication`. This diff does not modify `kronikaShareGlyph`; the eye branch is present at the candidate and was already at the baseline.

### G Documentation and ADR — PASS

`docs/adr/0088-timeline-as-single-overview.md` is new, status `Accepted`, dated 2026-11-10. It records Timeline as the single overview, removes the History link and page, folds both History addresses to Timeline, keeps Search, Research, and Review as actions, keeps Gallery separate, and keeps question and answer records, APIs, and authorization. It supersedes only the separate-History-view statements in ADR-0083 and ADR-0087. `docs/adr/README.md` indexes ADR-0088 and marks those two supersessions. `git diff --name-only bbf776c..8646146` includes no ADR-0082 through ADR-0087 body.

`SPEC.md` under `Timeline, Personal History and Completion` is the normative MUST owner: no separate History view, both folds, header-slot search, hidden heading without hero/lede/note, Publication-first green filter, column alignment, no title underline, eye glyph, 44 px targets, and focused-option activation. README, GALLERY, DEVELOPMENT, PRODUCT, ROADMAP, and AGENTS no longer say a separate History view exists; they say it does not, and the presentation sentences point at SPEC. The AGENTS diff is only that History-view paragraph. `SECURITY.md` and `SERVER.md` are unchanged. Their surviving `history` uses are dated operational history, Git or retention history, browser-history prohibition, companion own-history routes, or the still-existing preview-locator payload section `Timeline And History Preview Locators`. That section describes `preview_location_id` on list items, not the removed page.

The SPEC heading still contains the words `Personal History`. The paragraph under it denies the separate view, so this is residual wording, not a second semantic owner and not a claim that the view remains.

### H Closed behavior and non-UI scope — PASS

The `app.js` hunks are list-state removal, History route fold, shell visibility, current marking, History loader deletion, recovery and error copy that now say Timeline, and the search listeners moving to the header form. They do not edit Gallery search, Gallery or Details renderers, the player, capability predicates, polling, approval payloads, or Timeline preview rendering. The preview-runtime edit removes the deleted History `records` bucket and leaves the Timeline bucket. Timeline still loads `/api/timeline`. Question rows still link to request or record routes and the existing question-preview tests passed (`Timeline question rows never request previews`).

`git diff --name-only bbf776c..8646146` contains no API, domain, application, persistence, authorization, capability, route-policy, schema, migration, provider, capture, companion, dependency, or deployment path. `git diff --check` was clean.

### I Validation and allowlist — PASS

Measured commands and counts:

- `./.ap/ap doctor`: PASS
- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec`: PASS
- `./.ap/ap exec --root /Users/agile/Projects/kronika --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider`: 208 passed, 0 failed, 26.28s
- `node --test tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/gallery_filter_controls.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js`: 85 passed, 0 failed, 0 skipped, 0 cancelled
- `git diff --check`: clean
- `git status --short` after those runs: empty
- HEAD remained `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`

`git diff --name-only 27aa5fd..8646146` is exactly `src/kronika/adapters/api/web/app.js` and `tests/kronika_ui.test.js`.

`git diff --name-only bbf776c..8646146` is exactly these fourteen paths:

```text
AGENTS.md
DEVELOPMENT.md
GALLERY.md
PRODUCT.md
README.md
ROADMAP.md
SPEC.md
docs/adr/0088-timeline-as-single-overview.md
docs/adr/README.md
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/contract/test_local_web_application.py
tests/kronika_ui.test.js
```

No other path changed. `tests/gallery_search_tag_filters.test.js` is named in the prompt's section 2 list and has an empty diff against `bbf776c`; `git log bbf776c..8646146 -- tests/gallery_search_tag_filters.test.js` is empty. It was executed and passed. The correction grant said to leave a listed file unchanged when it needed no edit. The measured change set matches the stated count of fourteen and contains no path outside the enumerated names. See deviations.

No full Python suite was run. No browser, screenshot, or rendered-geometry claim is made.

## Source and security findings

None. The diff does not touch authorization, payloads, schema, secrets, or provider code. Error-copy edits are user-facing strings that point at the Timeline.

## UI and frozen-view findings

None in the source contract. Gallery and Details renderers and the player are outside the diff. Gallery search, tag, filter, still-image, GIF, playback-handoff, and cover tests passed. Painted alignment, contrast, 320/390 px geometry, layout jump, popup visibility, touch, and assistive-technology output were not tested.

## Documentation findings

None that fail the matrix. ADR-0088 and the updated owners agree that the separate History view is gone and that SPEC owns the shell requirements. Accepted ADR bodies 0082–0087 are unedited.

## Allowlist review

Negative allowlist holds: the measured diff is confined to the fourteen paths above. The two-path micro-correction matches exactly. Within `app.js`, the changes are the History removal, header-search visibility and binding, current marking, and the copy that names the Timeline. Route parsing changes only the History fold.

## Deviations and near-misses

The acceptance prompt's section 2 says "fourteen" and then enumerates fifteen paths, including `tests/gallery_search_tag_filters.test.js`. That file is unchanged from `bbf776c`. The candidate's measured whole diff is the fourteen paths listed under claim I, with stat 14 files, 278 insertions, 519 deletions. This is a prompt-list surplus, not a candidate scope escape and not a missing required edit. The file remains a required regression test and passed.

Resolved Execution Issues / Near-Misses: the section 2 enumeration is one name longer than the measured fourteen-path diff. Cause: `tests/gallery_search_tag_filters.test.js` was carried in the changed-path list although this candidate does not modify it. Resolution: compared `git diff --name-only` with the enumerated names, confirmed the surplus path's empty diff and empty log, confirmed every measured path is inside the enumerated names, and continued the audit. Residual risk: a later reader who treats the fifteen-name list as a required mutation set will misclassify this candidate.

Pre-Existing Failure Classification: none

## Residual risks and missing evidence

Rendered header stability, column alignment, contrast, 320/390 px geometry, popup visibility, touch behavior, and assistive-technology output remain the Cooperator's later rendered acceptance. They were not claimed from Node or CSS.

`SPEC.md` still titles the section `Timeline, Personal History and Completion`. The normative paragraph denies a separate History view. `SECURITY.md` still headings `Timeline And History Preview Locators`; the body is the unchanged preview-locator payload contract.

Out-of-scope observations: ledger-candidates. No ledger entry was written.

## Smallest next step

Orchestrator records this acceptance-PASS for `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`. Publication, NUC refresh, rendered acceptance, and closure each need a new grant. Drop `tests/gallery_search_tag_filters.test.js` from the changed-path enumeration if that prompt text is reused; keep it in the test command.

Git result: read-only inspection only. No add, commit, push, or other Git write. The Kronika worktree is clean and still at the candidate.

Authority expiry: this terminal report ends the grant. No correction, publication, deployment, production, or closure authority remains.

Orchestration critique:
MEASURED: section 2 of `04_acceptance_00.md` says the candidate changes exactly fourteen paths and then lists fifteen, including `tests/gallery_search_tag_filters.test.js`; `git diff --name-only bbf776c..8646146` and `git log bbf776c..8646146 -- tests/gallery_search_tag_filters.test.js` show that file unchanged, while the other fourteen names match the diff exactly (278 insertions, 519 deletions). Effect: a literal stop on set inequality would have blocked a candidate that matches the fourteen-path measured set and the two-path micro-correction. Smallest correction: remove that unchanged test path from the changed-path list and leave it in the test command.
LEAD: none
