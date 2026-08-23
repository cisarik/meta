[Archival note by ORCHESTRATOR, not part of the Worker report: Native Plan Mode
was active in the Worker client during exchange 01 and prohibits filesystem
mutation, so the Worker could not write this file itself. The Worker delivered
its complete terminal report in chat; the Cooperator relayed it to the
ORCHESTRATOR on 2026-08-23. This file is a verbatim transcription of that
chat-delivered terminal report for Worker session 01 / exchange 01. Nothing
below this note was added, removed, or edited.]

### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-companion-review-inbox-ux-history-mvp  
Worker session ordinal: 01  
Worker exchange ordinal: 01

Status: BLOCKED

Phase-qualified result: not-applicable

## Baseline and capability evidence

- Canonical root: `/home/agile/Projects/framenest`
- Branch: `feat/x-meme-browser-companion`
- HEAD and local `origin/main`: `6e20fc12f145286e474294b79cbd120df6e38e56`
- Worktree: clean
- `.ap` gitlink and checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native planning mode: directly observed active.
- Reasoning: extra-high requested; effective setting is not observably exposed.
- Context pressure: moderate but healthy; no evidence loss.
- Internal delegation: not used, as required.
- Baseline test: `node --test tests/companion_review_extension.test.js` passed all 15 tests.

Planning is decision-complete. The blocking condition is report delivery: active native Plan Mode prohibits filesystem mutation, so `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/01_report_00.md` was not created.

## Recon evidence

- Current chrome places `#shell-status`, a visible “Review inbox” toggle, empty copy, list, and then `#frame`: `extension/ui/sidebar.html:9-65`.
- Existing flex layout already makes fixed-height chrome precede a surviving flexible iframe: `extension/ui/sidebar.css:142-153`, `274-284`.
- Sidebar currently renders every returned item and toggles the inbox itself: `extension/ui/sidebar.js:315-360`; “Connected” is emitted at lines 452, 579, and 654.
- The API returns `media_id`, `title`, `analysis_run_id`, `completed_at_ms`, `unopened`, `unopened_count`, and `next_cursor`: `src/framenest/adapters/api/companion_review_api.py:82-98`, `378-393`.
- Results are latest-successful-generic-per-media, ordered by completion time then run ID descending: `src/framenest/infrastructure/persistence/companion_review_repository.py:90-142`, `517-564`.
- `unopened` and `unopened_count` derive from the actor-scoped opened row versus the latest run: `src/framenest/infrastructure/persistence/companion_review_repository.py:567-629`.
- Mark-opened is monotonic and reusable: `src/framenest/infrastructure/persistence/companion_review_repository.py:270-325`.
- The endpoint is paginated—25 by default, 100 maximum—and pagination beyond 25 is already tested: `src/framenest/application/companion_review.py:34-35`, `tests/unit/infrastructure/persistence/test_companion_review_repository.py:348-378`.
- The service worker currently drops `next_cursor`, so it exposes only the first page to the sidebar: `extension/background/service_worker.js:590-619`.
- The review overlay marks the selected run opened after detail load and when changing run, while Save currently only applies and requests a refresh: `extension/ui/review.js:115-174`, `195-253`.
- Direct stale-context sites exist in `x_adapter.js` at lines 252-255, 840, 934, 1638, 1926, and 1948. An unused `markStale` foundation already exists at lines 235-248.
- ADR-0063 preserves the hosted iframe (`docs/adr/0063-companion-side-panel-web-host.md:28-79`); ADR-0067 owns durable actor-scoped opened state (`docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md:18-33`); ADR-0071 owns the rejected collapsible-inbox chrome while preserving iframe and badge posture (`docs/adr/0071-native-side-panel-review-inbox-chrome.md:18-37`).
- Stale living descriptions are at `SPEC.md:7` and `924-939`, `PRODUCT.md:30` and `394`, `ROADMAP.md:286-289`, and `docs/X_COMPANION.md:36-58`.

## Frozen implementation plan

### 1. Sidebar DOM and layout

- Replace `#review-inbox-toggle`, its heading bar, hint, and empty-copy node with:
  - an absolute full-bar `<button id="review-history-toggle">` inside `.title-bar`, labelled “Analysis history”, with `aria-expanded="false"` and `aria-controls="review-history`;
  - `<section id="review-history">` immediately after the green title bar, containing `<ol id="review-history-list" aria-label="Analysis history">`;
  - the existing `#review-inbox` below history, containing only `<ol id="review-inbox-list" aria-label="Unread analyses">`;
  - the retained `#shell-status` and unchanged `#frame`.
- History starts collapsed on every panel load and is not persisted. Ignore legacy collapse/seen preferences for rendering, while retaining their reset cleanup.
- Empty history and empty unread render no copy and consume no height. Remove the awaiting-analysis hint from visible chrome to honor C2.
- Keep `#shell-status`; replace only the three “Connected” writes with an empty value and add `:empty { display: none; }`. Preserve errors, configuration guidance, “Cleared”, and the Attach confirmation “Attached”.

Rationale: this directly implements confirmed C1–C3 without changing the hosted iframe or server state.

### 2. Exact title-bar hit target

- Make `.title-bar` positioned and place the transparent history button at `inset: 0`.
- Keep wordmark text pointer-transparent.
- Stack Settings and Connect/Disconnect above the history button with a higher `z-index`; they remain sibling buttons, so their clicks never reach the toggle.
- Use the native button’s Enter/Space behavior rather than custom keyboard emulation.
- Disable the history toggle while disconnected and after ordinary-identity 403; force `aria-expanded="false"` and hide both lists.

Rationale: sibling stacking makes the complete green bar clickable except the two existing controls, satisfying C4 without nested interactive elements.

### 3. History and unread data flow

- Extend the service worker’s existing `REVIEW_INBOX` operation to fetch sequential pages with `limit=100`, following server-returned `next_cursor` through `URLSearchParams`.
- Preserve page and row order exactly. Detect repeated cursors and treat any later-page error as a complete list failure: clear the badge and return no partial titles.
- History predicate: every sanitized row from the fully aggregated list.
- Unread predicate: `item.unopened === true`.
- A history row represents the latest successful generic run for one media item; all earlier successful runs remain in the existing review-overlay dropdown.
- Do not re-sort client-side: the server’s `(completed_at_ms DESC, analysis_run_id DESC)` order is authoritative.

Rationale: client pagination is necessary to make “all history” true beyond the current 25-row default while retaining the existing HTTP contract.

### 4. Row opening, Save, and no-Alembic decision

- Both lists use the same safe text-content renderer and the same media-ID click handler to open `ui/review.html#media=<uuid>`.
- Do not remove unread optimistically. Remove it after the existing durable mark-opened succeeds and the overlay sends `INBOX_REFRESH`.
- Track successfully opened run IDs inside the review controller.
- Before Apply, Save calls `ensureOpened()`:
  - if the selected run was already marked successfully, proceed without another audited POST;
  - otherwise retry the existing opened route;
  - if that retry fails, retain selections, show a specific error, and do not Apply;
  - after opened success, run the unchanged Apply path.
- Apply receipts remain canonical-field provenance and are not added to unread queries.

No Alembic 0032, new table, server route, schema, or server repository change is needed. The existing actor/media opened table, opened endpoint, and monotonic semantics provide the smallest durable rule.

### 5. Badge and identity behavior

- Continue deriving badge text solely from server `unopened_count`, using the existing `1`…`99`/`99+` formatter.
- Never derive badge text from rendered lengths or titles.
- Update it after the fully successful list refresh and through the existing one-minute alarm.
- Any 403 or list failure clears the badge and hides unread/history. Failed analyses remain excluded by the existing server predicates.
- Do not add `notifications` permission.

Rationale: this preserves C6 and the already-passing ordinary-identity privacy contract.

### 6. Iframe survival and push mechanics

- Keep history as non-growing header chrome and unread as a `flex: 0 0 auto` main child before `#frame`.
- Give each list a bounded scroll height; expanding history grows the header and pushes `.sidebar-main`/`#frame` down. Collapsing removes only history’s layout height.
- History/unread render and toggle functions must never call `clearFrame`, alter `frame.src`, set `frame.hidden`, replace the iframe node, or move the review overlay inside it.
- Existing disconnect/invalid-origin behavior remains the only path that clears the hosted frame.

Rationale: the stable iframe node and source preserve ADR-0063/ADR-0071 Attach survival.

### 7. Accessibility

- `#review-history-toggle`: native button, meaningful label, `aria-expanded`, and `aria-controls`.
- Both lists: native ordered-list semantics with distinct `aria-label` values.
- Every row remains a native text-labelled button.
- `#shell-status` retains `role="status"`.
- No hover or focus event marks an item opened.

### 8. Stale extension-context guard

- Add one shared exact classifier and recovery copy: `FrameNest was reloaded. Refresh X and reopen the side panel.`
- Classify only:
  - a falsy/missing `chrome.runtime.id`; or
  - an exception/`lastError.message` containing the exact `Extension context invalidated` signature.
- In `x_adapter.js`, route every runtime URL, message, and listener-registration operation through targeted helpers:
  - invalidation invokes an idempotent `markStale`, closes partial picker/Save hosts, disables existing controls, stops further scans, and creates one fixed `role="alert"` recovery notice;
  - Save/picker URL failure returns before appending a partial host;
  - unrelated thrown runtime errors propagate; unrelated callback `lastError` keeps the existing ordinary unavailable result.
- Apply equivalent synchronous-throw and callback guards in Save, picker, sidebar, and review request paths. Their existing status regions display the same recovery copy and disable the affected action.
- Do not change `background/service_worker.js` for Slice B: an MV3 service worker is terminated and recreated on extension reload; its startup `getURL`/listener registration executes only in the new context. Its bootstrap failure must remain loud rather than be swallowed.
- MiniDom/VM can emulate falsy runtime IDs and the exact thrown/`lastError` signature, but it cannot prove Chromium’s real reload lifecycle. Cooperator UX step 16 remains the required real-browser evidence.

### 9. Successor ADR and documentation

Create exactly:

`ADR-0072: Native Side-Panel Unread Inbox and Title-Bar History Chrome`

Outline:

1. Status and decision date.
2. Context: live Cooperator rejection of Connected/heading/empty/collapsible-inbox chrome.
3. Decision: default unread filter, full paginated history, title-bar target/exclusions, shared overlay, opened-on-click/Save, hidden success status, ordinary-identity hiding.
4. Preserved contracts: hosted iframe, badge/no-notifications posture, overlay sibling files, four mutation routes, G2, v4 tags, movie exclusion.
5. Superseded statements: only ADR-0071/X_COMPANION statements about the collapsible inbox toggle, “Review inbox” heading, and empty copy.
6. Consequences and references to ADR-0063, ADR-0067, ADR-0071, and X_COMPANION.

Do not edit ADR-0071 itself. Add ADR-0072 to the ADR index and mark only the named ADR-0071 chrome statements as succeeded.

Update:

- `docs/X_COMPANION.md`: unread/history behavior, title-bar control, blank success status, unchanged iframe/badge/permission posture, and stale-context recovery.
- `SPEC.md`: summary and companion API paragraph with unread/history chrome semantics.
- `PRODUCT.md`: companion surface described as an unread attention queue plus all-item history.
- `ROADMAP.md`: replace “native S1 review inbox” with the accepted successor chrome and ADR-0072.

Public interface impact: no HTTP route, JSON field, database schema, manifest permission, or companion message type changes. Internal DOM IDs add `review-history-toggle`, `review-history`, and `review-history-list`; the existing `REVIEW_INBOX` response shape is retained but its `items` become fully page-aggregated.

### 10. Test plan

Slice A extends `tests/companion_review_extension.test.js` with:

- new DOM order, absence of visible heading/empty/hint copy, retained status and iframe;
- whole-bar toggle structure, control exclusions, keyboard semantics, and ARIA;
- history-all versus unread-only filtering with preserved order and accepted duplication;
- multi-page aggregation, encoded cursor, repeated-cursor guard, and no partial results;
- same overlay from both lists and no hover/focus opened mutation;
- opened-success refresh removing unread while retaining history;
- Save retrying opened only after an earlier failure and blocking Apply if retry fails;
- status success hiding with errors/Cleared/Attached retained;
- ordinary 403 hiding both lists and badge;
- iframe identity/src unchanged across expand, collapse, empty, and forbidden states.

Slice B extends:

- `tests/x_companion_extension.test.js` for exact invalidation throws, falsy runtime ID, one recovery notice, disabled controls, no partial iframe host, valid-context behavior, and unrelated-error propagation;
- `tests/companion_review_extension.test.js` for sidebar/review recovery and shared classifier behavior.

Exact commands:

```text
node --test tests/companion_review_extension.test.js
node --test tests/x_companion_extension.test.js
git diff --check
git status --short
```

No Python evidence is required because no server or persistence code changes.

### 11. Slice allowlists and commits

Slice A — chrome:

- `extension/ui/sidebar.html`
- `extension/ui/sidebar.js`
- `extension/ui/sidebar.css`
- `extension/ui/review.js`
- `extension/background/service_worker.js`
- `tests/companion_review_extension.test.js`
- `docs/adr/0072-native-side-panel-unread-inbox-and-title-bar-history-chrome.md`
- `docs/adr/README.md`
- `docs/X_COMPANION.md`
- `SPEC.md`
- `PRODUCT.md`
- `ROADMAP.md`

Commit: `feat: add companion unread inbox and title-bar history`

Validation ladder: exact baseline/clean-tree re-gate → focused companion suite → existing X companion suite → documentation/ADR link and semantic review → `git diff --check` → exact changed-path and staged-diff review. Stop on iframe mutation, ordinary title exposure, server/schema need, or any non-zero gate. No NUC deployment.

Slice B — stale context:

- `extension/shared/messages.js`
- `extension/content/x_adapter.js`
- `extension/ui/save.js`
- `extension/ui/picker.js`
- `extension/ui/sidebar.js`
- `extension/ui/review.js`
- `tests/x_companion_extension.test.js`
- `tests/companion_review_extension.test.js`
- `docs/X_COMPANION.md`

Commit: `fix: guard invalidated companion extension contexts`

Validation ladder: re-gate at accepted Slice A HEAD → exact-signature positive/negative MiniDom tests → both focused Node suites → direct search confirming every `x_adapter.js` runtime use is guarded → `git diff --check` → exact changed-path/staged-diff review. Stop if unrelated runtime errors are swallowed or valid-context Save/picker behavior changes.

Slice C — Cooperator UX walk:

- Proposed changed-path allowlist: none.
- Commit: none.
- A concrete failure stops the walk and requires a separately authorized smallest correction and scoped retest.

### 12. Ordering and acceptance

Execute A → B → C only.

Slice C uses the fixed 16-step order, one step at a time:

1. Admin empty chrome.
2. Ordinary identity privacy and Attach.
3. Website Analyze creates unread row and badge.
4. Unread click opens overlay and clears attention.
5. Title-bar history lists all rows and pushes iframe.
6. History row reopens overlay without restoring unread.
7. Collapse restores iframe space and Attach.
8. Frozen ingest Save.
9. X Save does not create unread before analysis.
10. Overlay field/tag gates.
11. Title-only apply remains `not_ready`.
12. Description/tags complete publication.
13. Tags replace rather than union.
14. Error retention and ordinary 403 hiding.
15. Close preserves iframe/Attach; no notification, movie, or NIM publication regression.
16. Reload unpacked without refreshing X: picker/Save show recovery without throwing; after tab refresh, normal behavior returns.

Michal owns visual/UX PASS. No code is authorized during C unless a concrete failure receives a new correction grant. Publication, living-document remainder, NUC update, and deployment remain separate grants.

## Deviations, risks, and open questions

Deviations:

- The required report file was not written because native Plan Mode prohibits filesystem mutation. No repository or Meta file was changed.
- No other deviation.

Risks:

- Fully aggregating history makes each 15-second sidebar refresh proportional to catalog history size; 100-row pages and sequential local requests bound each request, while cursor-cycle detection prevents infinite loops.
- New analyses committed between pages may be absent until the next poll; keyset pagination and the next 15-second refresh provide eventual correction.
- Full-bar CSS stacking could intercept Settings/Connect if implemented incorrectly; structural/MiniDom tests and UX steps 1, 5, and 7 are mandatory.
- MiniDom can reproduce the exact invalidation error class but not Chromium’s lifecycle; UX step 16 remains necessary.

Open questions: none. C1–C7 are confirmed Cooperator intent, and no Section 8 fork remains blocking.

## Smallest next step

ORCHESTRATOR issues a report-rendering-only exchange with `Native planning mode: not-used` to place this frozen plan in `01_report_00.md`, then reviews it with Michal and, after approval, issues Slice A implementation authority.

Report justification: new-evidence

Planning authority expired at this submission. No implementation, Git write, publication, deployment, or further action is authorized without a new ORCHESTRATOR prompt.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none; the only executed baseline suite passed 15/15 at the exact baseline.
