### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ui-ux-consistency
Worker session ordinal: 01
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRN-UX-PLAN-01R — plan-only — final application-shell UI/UX consistency pass
Status: PARTIAL
Phase-qualified result: not-applicable
Start commit: e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
End commit: e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
Report justification: new-evidence
Planning cycle: initial
Prior planning report: 01_report_00.md
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Post-plan implementation session: fresh-worker-session
Logical-whole closure: not-closed
Report persistence: client-prohibited; complete exact content returned for authorized persistence
```

The implementation plan is complete. `PARTIAL` records missing report-file persistence under active client controls; it does not identify an unresolved technical choice. No implementation or acceptance PASS is claimed.

Intended report destination: `/Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/01_report_01.md`. The file remains absent. No saved-file readback is claimed.

## 1. Summary and verified baseline

Implement one presentation-only shell consistency candidate: separate browsing links from square action links, reuse the Gallery search field treatment, put Publication first, align the remaining filters with the wide Timeline columns, remove chronicle title underlines, and replace the legacy-publication clock with an eye.

During this planning exchange, Michal explicitly selected inclusion of the existing Tab → Enter listbox defect and missing presentation roles. Include that bounded accessibility correction; preserve filter values, query composition and authorization.

Verified before substantive planning and checked again at completion:

- Canonical checkout: `/Users/agile/Projects/kronika`, branch `main`, clean.
- HEAD, `origin/main` and directly observed public `refs/heads/main`: `e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`.
- Recorded `.ap` gitlink, submodule HEAD and observed AP public `main`: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- `./.ap/ap doctor`: PASS; governing variant `stable`.
- Exact baseline-bound `ap project check`: PASS. Its warning lists sanitized inherited environment classes; no environment values were disclosed.
- The supplied attachment matches the archived `01_planning_01.md`.
- The continuity anchor matches this session’s preceding terminal report.

No repository or Meta file changed. No Git write, browser, NUC, provider, secret or private-media action occurred. Product test suites were inspected, not executed: the planning claims were established from source.

NUC release, database and privilege facts remain predecessor-recorded evidence, not observations from this exchange.

## 2. Re-measured current-state map

Web source root below is `src/kronika/adapters/api/web/`.

| Surface | Current implementation and evidence |
|---|---|
| Primary navigation | [index.html:837](/Users/agile/Projects/kronika/src/kronika/adapters/api/web/index.html:837) places all six route anchors inside one `.kronika-nav` under `<main>`. IDs, hashes and `data-kronika-nav` identify each destination. |
| Navigation behavior | [app.js:13918](/Users/agile/Projects/kronika/src/kronika/adapters/api/web/app.js:13918): `kronikaMarkCurrent`, `kronikaSyncReviewNav`, `kronikaShowShell`, `kronikaFocusRoute`; `kronikaBindShell` records link openers. `kronikaStartNavigation` hides the entire nav for the public composition. Review visibility uses `records.approve`. Search and Research retain their existing capability handling inside their views. |
| Navigation CSS | `styles.css:5384` supplies shared control rules; later rules at `5724` make the nav a rounded pill and its links rounded tabs. At `6470`, the entire six-link nav becomes a fixed bottom bar at widths up to 720 px. Later declarations override earlier 44 px sizing with 40 px desktop nav links. |
| Top-right controls | `index.html:41–211`: Add, contributions, administration, health, AI and identity controls. `setupHeaderMenus` at `app.js:15609` handles opening, closing and keyboard behavior. `.app-header` is sticky and uses `backdrop-filter`. These controls and their handlers remain intact. |
| Gallery search | `index.html:20`: `.header-search`, `.header-search__control`, decorative magnifier, `#command-search-input`, inline Clear, active tag rail and suggestions. Placeholder is `Search titles and tags`; accessible name is independent. |
| Gallery search behavior | `app.js:9815–10066`: immediate local query-state update; 200 ms debounce for catalog loading and suggestions; title/tag suggestions; Arrow keys, Enter and Escape; Clear resets existing Gallery search state and returns focus. No part of this controller should be reused to query Timeline. |
| Search CSS | `styles.css:191–279` owns the green border, focus ring, input and Clear styling. Later `.header-search__prompt` at `5532` makes the effective prompt static. Existing tests also inspect older pulse declarations, so first-match source assertions do not describe the complete cascade. The control currently declares 40 px height. |
| Timeline controls | `index.html:855–918`: custom listboxes in Kind, Status, Visibility, Publication order, followed by a separate labelled input and text Search/Clear buttons. [styles.css:6050](/Users/agile/Projects/kronika/src/kronika/adapters/api/web/styles.css:6050) uses a wrapping flex filter bar; triggers have a 9.5 rem minimum width. |
| Timeline query behavior | `kronikaSyncTimelineControls`, `kronikaTimelineRouteFromControls`, `kronikaTimelineExtra` and the form handlers preserve `filter`, `q`, `status`, `visibility`, `publication` and offset. Submit, Clear and menu selection reset offset to zero. Pagination preserves filters. `kronikaAssignHash` deliberately reloads even when the requested hash already matches. |
| Search semantics | `timeline_repository.py:264` applies escaped `NOCASE` substring matching to the authorized projection’s `search_text`; `_columns` derives that from the selected title source. This is not Gallery tag search. |
| Custom listboxes | `kronikaSetupTimelineMenus` at `app.js:15360` supports trigger activation, arrows, Enter/Space, Escape, outside click, selection and focus return. Its stored keyboard index does not follow native Tab focus. Option buttons are wrapped in `<li>` elements without presentation roles. Both findings match whole 09’s final acceptance report. |
| Chronicle rows | `kronikaRenderChronicle` renders Timeline; `kronikaRenderQuestionChronicle` renders History. Both use `.kronika-chronicle__title` anchors. The title rule does not remove the browser’s link underline. Shared hover/focus-within uses a 160 ms green background/inset accent without transforms. |
| Glyphs | Actual helpers are `kronikaStatusGlyph` and `kronikaShareGlyph`, not `kronikaPublicationGlyph`. `kronikaPublicationLabel` supplies retained accessible text. `kronikaChronicleSignal` hides decorative glyphs from assistive technology and preserves words plus a cell title. |
| Responsive layout | Timeline header/rows use five tracks: `4.75rem minmax(0,1fr) 5.5rem 4.5rem 6.25rem`, with 20 px gaps. At 720 px, the header hides and rows become `36px minmax(0,1fr)`. History has a separate four-track layout and becomes one column. Timeline currently uses `overflow-x:hidden` at the narrow breakpoint. Reduced-motion rules disable row transitions and menu animation. |

Current test owners:

- `tests/kronika_ui.test.js`: route and capability behavior, list lifecycle, previews, stale-query handling, Timeline controls, custom listboxes, glyphs, responsive source rules and Questions-only History.
- `tests/gallery_search_tag_filters.test.js`: Gallery placeholder/name, inline tag rail, search/tag composition, keyboard behavior, request ownership and reduced-motion source assertions.
- `tests/gallery_filter_controls.test.js`: All-media reset, filters, tag intersection and Details state preservation.
- `tests/contract/test_local_web_application.py`: served document/assets, header, search markup/style, local assets, hidden-state authority and Gallery/Details contracts.
- Existing Gallery still-image, GIF, playback-handoff and cover Node suites protect the frozen media presentation and player.

Corrections to the starting hypotheses and documentary drift:

- The actual History renderer and share-glyph helper have the names above.
- Gallery and Timeline do not have interchangeable search semantics. Reusing the Gallery placeholder verbatim would advertise unsupported Timeline tag search.
- The current mobile nav contains all six entries.
- README, GALLERY and DEVELOPMENT still describe personal-record History preview cards. Current History is Questions-only and makes no preview requests.
- ADR-0087’s creation-date presentation sentence remains the already carried whole-09 finding. The ADR index prohibits editing accepted ADR bodies in place; this plan does not amend it.

## 3. Exact proposed design

### Navigation structure and behavior

Move the existing `.kronika-nav` from `<main>` to immediately after `.app-header`, as a body-level sibling. Keep one hidden-by-default `nav` landmark and all six existing anchors.

Its two child groups are:

```html
<nav class="kronika-nav" aria-label="Primary" hidden>
  <div class="kronika-nav__browse" role="group" aria-label="Browse">
    <!-- Existing Timeline, Gallery and History anchors -->
  </div>
  <div class="kronika-nav__actions" role="group" aria-label="Actions">
    <!-- Existing Search, Research and Review anchors -->
  </div>
</nav>
```

Preserve IDs, hashes, labels, glyphs, `data-kronika-nav`, Review’s initial `hidden`, click-opener handling and `aria-current` logic. The action entries remain native anchors because they open existing routes. Do not introduce button emulation, a tablist, a second router or new capability rules.

CSS decisions:

- The outer nav is a full-width, unfiltered flex container with wrapping, `align-items:center`, a 16 px group gap and `padding:12px 20px 0`.
- Match its horizontal padding to the existing header: 14 px at the 900 px breakpoint and 10 px at 360 px. This aligns the action group’s right edge with the top-right controls.
- Put the rounded container and browsing-tab treatment on `.kronika-nav__browse`.
- Put Search, Research and Review in the right group using `margin-inline-start:auto`, a 6 px gap, fixed 1 px borders and `border-radius:0`.
- All desktop links have at least 44 × 44 px targets. Retain green current/hover treatment and add explicit visible keyboard focus to both groups.
- At 720 px and below, only the browsing group becomes the existing fixed bottom bar. Keep its 54 px link targets, safe-area padding and existing body bottom allowance. Actions remain in the normal row below the header.
- Narrow action links keep both icons and text, using 0.75 rem text, 6 px horizontal padding and a 4 px gap. They remain at least 44 px tall.
- Retarget every pill-specific and mobile-positioning selector to the browsing group. Keep the outer nav’s overflow visible and preserve authoritative `[hidden]` behavior.

Keeping this nav outside the filtered header avoids making the mobile fixed bar depend on the header’s containing-block behavior. Header-menu markup and JavaScript remain unchanged.

### Shared search presentation

Use the existing `.header-search__control`, `__prompt`, `__input` and `__clear` styles as the single presentation owner.

Keep Gallery’s controller, IDs, placeholder, accessible name, suggestion panel and tag rail. Add a fixed-width `.header-search__clear-slot` around its existing Clear button so showing Clear does not change neighboring widths.

Timeline receives:

- A `.kronika-timeline-search` wrapper with `role="search"` and `aria-label="Search timeline"`.
- A visually hidden input label.
- The shared control/input/Clear classes.
- Existing input ID, `type="search"`, `maxlength="240"` and `autocomplete="off"`.
- Placeholder `Search timeline`; accessible name `Search timeline titles and questions`.
- The existing submit button ID, presented as a leading magnifier button with accessible name `Search timeline`.
- The existing Clear ID, presented as an inline × inside the reserved Clear slot, hidden when the draft input is empty.

Do not add `.header-search` to the Timeline wrapper: existing shell code uses that root selector to hide Gallery search.

Normalize the shared search chrome to accessible target sizes: 44 px minimum input/button height, 44 px Clear slot, automatic control height and `min-width:0` on the flexible input. The bordered field will normally be 46 px tall. This is the explicit shared-search exception to the Gallery freeze; cards, Details and playback remain untouched.

Timeline interaction remains explicit submission:

- Typing updates only Clear visibility; it starts no query, debounce or suggestions.
- Enter and magnifier activation use the existing form submit handler and route builder.
- Clear empties only `q`, preserves other filters, resets offset and uses the existing route path.
- Clear returns focus to the input and records that connected input as the opener before hiding Clear.
- Preserve submit-opener behavior for the retained submit ID.
- Add one small `kronikaSyncTimelineSearchChrome` helper, called from input handling, route/control synchronization and Clear.
- Preserve existing focused-input draft protection and same-hash reload behavior.
- Suppress the native search cancel decoration only on the Timeline input to avoid a duplicate Clear control.

No Gallery query state, tag state or request controller is shared with Timeline.

### Filter layout and responsive behavior

Reorder the actual DOM, not merely CSS order:

1. Publication.
2. Timeline search.
3. Kind.
4. Status.
5. Visibility.

Publication and search share a `.kronika-timeline-filters__primary` wrapper. Keep every existing filter value, ID, label, listbox association and option.

| Width | Layout |
|---|---|
| At least 1100 px | One shared five-track grid for Timeline toolbar, header and rows: `4.75rem minmax(0,1fr) 9.5rem 9.5rem 10.5rem`, 20 px column gaps and 8 px horizontal content padding. The primary wrapper spans tracks 1–2; Kind, Status and Visibility occupy tracks 3–5. |
| 721–1099 px | Toolbar has a full-width Publication/search row, followed by three equal filter columns. Preserve the existing compact table tracks. |
| Up to 720 px | Toolbar is one column in DOM order. Preserve the existing narrow Timeline row layout and History layout. |

The primary wrapper uses `11.5rem minmax(0,1fr)` on wider layouts and stacks Publication/search at 720 px. Wider signal tracks apply only to Timeline; History retains its current title space.

Additional rules:

- Publication’s trigger always uses `var(--accent-border)` and the existing soft-green language. Expanded/focused state remains distinguishable.
- Triggers have fixed minimum target height, `min-width:0`, bounded text with ellipsis and full accessible text.
- Use an inset toolbar border so toolbar/header/row grid content starts align.
- Right-align Status and Visibility popup panels to their triggers on wider layouts.
- Narrow panels use full available width, `min-width:0`, bounded height `min(22rem,60vh)` and vertical scrolling.
- Remove Timeline’s narrow `overflow-x:hidden`; prevent overflow through sizing and wrapping instead of clipping menus or focus indicators.
- Popups remain absolutely positioned and cannot shift rows.
- Preserve current row hover timing; disable new transitions under reduced motion. Keep the search magnifier static, matching the effective current Gallery treatment.

### Listbox correction selected by Michal

Inside `kronikaSetupTimelineMenus`, register a focus listener on each option that updates `panel._kronikaIndex` to that option’s index. Keep native Tab navigation and the existing selection path.

Add `role="presentation"` to each option-wrapper `<li>`.

Enter and Space must commit the focused option after Tab or arrow navigation. Preserve one-open-menu behavior, arrows, Escape, outside click, focus return, selected labels, offset reset and single route dispatch. Do not add unrelated typeahead or replace the custom dropdown implementation.

### Title links and glyphs

Add explicit `text-decoration:none` for `.kronika-chronicle__title` in idle, hover and focus states. Keep anchor names, destinations, two-line clamp, row hover/focus-within and visible focus outline. Do not make whole rows clickable.

Change only the legacy-publication glyph branch and matching menu option to `👁️`.

| Condition, in existing precedence order | Glyph | Accessible text |
|---|---|---|
| Withdrawn | ↩ | Existing visibility/publication label |
| Legacy publication | 👁️ | Existing `Private` or `Household · Legacy publication` label |
| Approved, or family visibility | 🏠 | Existing label |
| Private/default | 🔒 | Existing label |
| History item without publication fields | 🔒 | `Private` |

Publication menu: Any ✨, Unpublished 🔒, Approved 🏠, Withdrawn ↩, Legacy publication 👁️. Visibility menu remains Any ✨, Private 🔒, Household 🏠.

Status mapping remains: unanalysed 💤; in-progress states ⏳; analyzed/saved ✅; cancelled 🚫; failure/refusal/incomplete/timeout/unknown-submission states ⚠️; unknown fallback •.

Keep decorative glyphs `aria-hidden`, existing hidden text and cell titles. Keep the Timeline navigation/hero clock: it still means chronology. Do not introduce a `public` visibility value or suggest internet publication.

Rejected alternatives:

- Reusing the Gallery search controller would change query semantics and request behavior.
- Copying `Search titles and tags` into Timeline would misdescribe its search capability.
- Putting the fixed mobile browsing bar inside the filtered header risks incorrect positioning.
- Separate navigation roots would require broader hiding/current/focus selector changes.
- Button-based route actions would replace native link behavior unnecessarily.
- Keeping narrow row tracks while placing full filter controls over them would cause overflow or severe truncation.
- Native selects, another component framework, global link-decoration changes and clipping-based responsive fixes are outside this bounded pass.

## 4. Exact implementation changed-path allowlist

These are proposed future changes, not current mutation authority.

| Repository path | Purpose |
|---|---|
| `src/kronika/adapters/api/web/index.html` | Navigation groups/placement, shared search markup, Publication-first controls, eye option and presentation roles. |
| `src/kronika/adapters/api/web/app.js` | Timeline search chrome/focus, option-focus index synchronization and legacy glyph. |
| `src/kronika/adapters/api/web/styles.css` | Grouped navigation, shared search targets, aligned responsive filters, popup bounds, underline removal and reduced motion. |
| `tests/kronika_ui.test.js` | Causal shell/search/listbox/glyph regressions and deliberate layout-pin updates. |
| `tests/gallery_search_tag_filters.test.js` | Preserve Gallery behavior; update shared-search presentation and effective-motion expectations. |
| `tests/contract/test_local_web_application.py` | Served DOM hierarchy/order, target/style contracts and updated search pins. |
| `SPEC.md` | Sole normative owner of the changed shell presentation and focused-option activation requirement. |
| `DEVELOPMENT.md` | Correct History description and document the focused validation route. |
| `GALLERY.md` | Correct the obsolete History preview-card reference and retain the SPEC ownership link. |
| `README.md` | Correct the same shipped-UI summary and briefly describe the shell grouping. |

No new file, dependency or generated artifact is needed.

Negative allowlist: every other repository path, especially `.ap`, its gitlink, AGENTS, project execution configuration, manifests/lockfiles, migrations, API/domain/application/persistence code, authorization and route-policy tables, providers, capture, companion sources, deployment and host scripts.

Within `app.js`, exclude Gallery search/controller logic, Gallery/Details renderers, player code, route parsing/hash serialization, capability predicates, list request ownership, previews, polling, approval and mutation payloads.

No public HTTP API, payload, schema, persisted type, storage key or route contract changes.

## 5. Durable-document changes

`SPEC.md`, under “Timeline, Personal History and Completion”, owns the new requirements. Add:

> The application shell MUST separate Timeline, Gallery and History browsing links from right-aligned Search, Research and capability-gated Review action links below the header. Action links MUST use unrounded styling and preserve their existing routes. Timeline search MUST reuse Gallery’s icon-led green field treatment while retaining its Timeline-local query and explicit submit and clear behavior. Publication MUST be the first Timeline filter and use a green accent border; on wide layouts, Kind, Status and Visibility MUST align with their corresponding list columns. Timeline and History title links MUST have no underline and MUST retain visible keyboard focus. Legacy publication MUST use an eye glyph without changing visibility or publication labels. Changed shell controls MUST provide at least 44 px targets and remain usable at 320 px and 390 px. Timeline listbox keyboard activation MUST commit the focused option, including after Tab navigation.

Use SPEC links elsewhere instead of creating another normative owner.

Exact documentary corrections:

- README’s paragraph beginning “The Timeline and personal Records cards reuse ready media previews…” becomes:  
  “Timeline media rows reuse ready previews, retaining the kind icon while loading and after every failure. Personal History is a Questions-only chronicle without media previews; [SPEC.md](SPEC.md) owns the bounded behavior.”  
  Follow with one factual shell-grouping sentence linked to SPEC.
- GALLERY’s sentence assigning “Timeline-row and personal-record History card reuse” to SPEC becomes:  
  “[SPEC.md](SPEC.md) owns Timeline-row reuse of the same ready previews, including icon retention while loading and after every failure. Personal History shows the caller’s questions without media previews.”
- DEVELOPMENT’s sentences saying History reuses media previews and “keeps its card layout” become:  
  “Timeline media rows reuse ready Gallery previews, with the kind icon retained while loading and after every failure. Personal History is the Questions-only chronicle and makes no media-preview requests. [SPEC.md](SPEC.md) owns these presentation requirements.”  
  Extend the existing focused validation block with the shell/search tests below.

PRODUCT, SERVER and SECURITY need no change for this presentation candidate. Preserve their architecture, access and provider contracts. Do not amend accepted ADR bodies or repair unrelated transition-status prose.

## 6. Test plan and evidence limits

Extend existing suites; do not add a new toolchain.

| Claim | Required evidence |
|---|---|
| Navigation grouping | Served-HTML parser verifies one nav, two groups, correct membership, unchanged IDs/hashes, initial hidden states and placement outside the header/main. Node checks current-route marking, opener focus and capability/public hiding across the grouped fixture. |
| Explicit Timeline search | Drive typing, submit and Clear. Typing changes chrome only; submission uses the existing route path; trim `q`, reset offset and preserve all non-text filters. Clear hides its button, returns input focus and preserves filters. Preserve same-hash reload behavior. |
| Search separation | Timeline interactions do not mutate Gallery query/tags or call Gallery loaders. Existing Gallery suggestion, Enter, tag-AND, reset and stale-response tests remain authoritative. |
| Listbox defect | Add a regression that opens a menu, focuses another option through the Tab-equivalent focus event, then activates Enter and Space. The focused option must be committed. Cover subsequent arrows, Escape, outside click, another menu opening and focus return. |
| Layout | Served DOM verifies Publication/search/Kind/Status/Visibility order. CSS contracts verify the shared wide grid, common padding/gaps, narrow stacking, popup bounds, reserved Clear slots and 44 px targets. These are structural claims, not pixel measurements. |
| Links | Preserve actual Timeline and History destinations and names; verify explicit no-underline selectors and retained focus/row-hover rules. |
| Glyphs | Update the legacy expectation; cover the complete precedence matrix, menu glyph, unchanged labels, hidden decorative icons and History’s private fallback. |
| Closed behavior | Preserve stale-query Retry, identity clearing, cancelled dirty navigation, pagehide versus visibilitychange, preview limits and History’s Questions-only endpoint/legacy-address fold. |

Required test maintenance:

- Model the two navigation groups in the Node fixture.
- Make fixture focus dispatch registered focus listeners and track active focus sufficiently to exercise the real listbox correction.
- Replace obsolete fake kind-chip fixtures only where needed to represent current controls.
- Update the existing legacy-clock expectation.
- Update the local-web search assertions that currently require 40 px height and an 80 px input minimum.
- Update the old pulse-oriented tests to inspect the effective static prompt and explicit reduced-motion fallback, rather than treating an earlier overridden declaration as final behavior.
- Preserve all unrelated expectations and Gallery tag-rail containment.

Demonstrate the Tab/focus regression failing against the previous implementation with the corrected fixture, then passing after the bounded fix.

Future authorized execution uses:

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
node --test tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/gallery_filter_controls.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
#------------------------------------------------------
```

The later grant must bind the actual candidate and confirm the unchanged trusted execution-contract baseline. Run affected checks once per candidate; diagnose failures narrowly before repeating them.

No full Python suite, gated browser suite or old authorization-wide matrix is required for this UI-only candidate. A boundary deviation changes that selection.

Evidence tier: **E2**, supplemented by Cooperator-rendered acceptance. Node and served-asset tests do not prove painted alignment, contrast, 320/390 px geometry, popup visibility, touch behavior or assistive-technology output.

## 7. Acceptance, execution sequence and budgets

Select one bounded fresh E2 UI acceptance after implementation. The concrete benefit is separate verification of the previously independently identified focus defect, moved DOM ancestry and shared Gallery CSS, which the hand-built harness cannot establish alone. This is not a reopening of whole 09’s data/security audit.

| Stage | Route and gate |
|---|---|
| Plan disposition | Orchestrator reconciles this report, records Michal’s listbox decision and obtains approval of the complete plan. Persistence completion stores this exact content without replanning. |
| Implementation | Fresh Worker session 02, native planning off, one complete grant for the ten paths. Recommend Medium reasoning: design choices are resolved; the remaining work is bounded UI implementation. Use the canonical checkout, re-gate the exact baseline and produce one local commit without push. |
| Verification | Same implementation session: causal regression, selected suites, exact diff/path review and documentation checks. Evidence remains non-independent. |
| E2 acceptance | Fresh session 03, native planning off, Medium reasoning, read-only fixed-candidate UI review. Verify this plan’s matrix and selected evidence; no browser, provider or host access is implied. |
| Correction | At most one bounded correction for the same finding in the healthy implementation session under renewed authority. Runtime UI correction receives fresh re-acceptance; a documentation-only correction can receive scoped reconciliation. |
| Publication | After acceptance, a complete publication grant may reuse the healthy implementation session. Permit only normal push of the accepted commit and verify public `main` equality. |
| NUC preflight | Separately authorize the canonical helper’s `status` and `check --release <accepted-40-hex-SHA>`. Check never automatically grants deployment. |
| NUC refresh | After the preflight is reconciled, separately authorize `deploy --release <accepted-40-hex-SHA> --yes` through `deploy/ubuntu/kronika-release`, followed by status/readiness verification and terminal privilege release. Healthy session reuse is lawful with a complete renewed grant. |
| Rendered acceptance | Michal tests only after the accepted SHA is public and NUC `active_release`/`web_release` match it. Orchestrator classifies his observations and owns closure. |

Deployment constraints:

- Use the existing release helper, declared transport names and accepted Poetry/CPython paths.
- Record the actual previous active release as the recovery target.
- Expect schema `0035` unchanged; verify service, health and backup restore readiness.
- A schema discrepancy or `migration-required` result stops this UI deployment path and goes to the documented separately authorized continuation.
- Use the helper’s supported rollback to the recorded complete previous release if separately required and authorized; no manual pointer reconstruction.
- The Cooperator establishes sudo readiness outside the Worker. The Worker never runs `sudo -v` and ends privileged work with `sudo -K`.
- Do not restart capture, change host configuration or provision credentials.

Rendered checklist, each answered PASS/FAIL/NOT TESTED:

1. Browsing links and square actions are clearly separated; actions align beneath the top-right controls.
2. Timeline’s field matches Gallery’s treatment; Enter/magnifier and Clear preserve filters and paging behavior.
3. Publication is first and green-bordered; wide controls align with their columns.
4. At 320 and 390 px, labels/actions remain usable, menus are reachable, and no horizontal page overflow or clipped focus appears.
5. Tab → Enter/Space commits the focused option; arrow, Escape and focus-return behavior remain correct.
6. Timeline/History links have no underline; focus, destinations, glyph labels, previews and reduced motion behave correctly.
7. History remains Questions-only; Gallery tags, cards, Details and playback retain their accepted behavior.

Budgets: one initial planning cycle; one coherent implementation candidate; one primary fresh E2 acceptance; at most one correction/re-acceptance cycle for the same finding. No automatic audit-of-audit or repeated broad gates. New authority is required for every later phase.

Any change to authorization, route interpretation, capabilities, payloads, query composition, persisted state or runtime data behavior stops this allowlist. Re-scope before implementation/publication and require fresh independent acceptance of the affected boundary, raising the evidence tier when its consequences require E3 or higher.

## 8. Decisions, risks and protocol friction

No unresolved technical choice remains. Plan approval, subsequent action grants and rendered judgment remain with their designated owners.

Defaults fixed by this plan:

- Native links with square action styling.
- Body-level navigation sibling, rather than nesting under the filtered header.
- `Search timeline` copy and existing explicit submission semantics.
- Shared search target-size normalization as the bounded Gallery-shell exception.
- Exact wide alignment begins at 1100 px; narrower layouts prioritize readable controls.
- Michal’s selected listbox correction is included.
- No accepted ADR is edited in place.

The prompt provides no numbered “risks below” list. This table maps measured risks and relevant predecessor risks:

| Risk | Control / disposition |
|---|---|
| Monolithic shell and misleading test fixtures | Three bounded production files; real served-DOM assertions; focused fixture updates; fresh E2 review. |
| Moved actions lose current/focus/capability behavior | Preserve common nav root, selectors, IDs and anchors; test each group and public/Review hiding. |
| Shared search changes semantics | Share presentation only; Gallery controller unchanged; Timeline remains on its existing route/query path. |
| Filter alignment harms title space or narrow layout | Wider tracks only on wide Timeline; preserve History; stack controls at narrow widths; owner checks exact geometry. |
| Menus or focus clipped | Bound popup width/height, align right-edge panels and remove Timeline’s clipping workaround. |
| Existing Tab/index defect | Explicit Cooperator decision, smallest focus synchronization, causal regression and separate acceptance. |
| Eye glyph implies internet publication | Change only legacy presentation; retain labels and household/private values; add no public state or action. |
| Documentation repeats closed History behavior | Correct only the three obsolete UI summaries; SPEC remains the normative owner. |
| Gallery/Details freeze | Shared field chrome is the only Gallery exception; preserve media renderer/player code and regression suites. |
| Rendered evidence missing | Do not claim pixels or subjective acceptance from Node/CSS; publish and refresh NUC before Michal’s checklist. |

Predecessor private-access, query-budget, deduplication and preview-lifecycle boundaries remain preserved. Upload-flow-polish, pre-identity upload observations, live external-button checks and retained private verification-item disposition remain outside this work.

AP protocol friction, measured:

- The preceding P4 defect is corrected by this grant’s explicit exact-content completion route. Client write prohibition now limits delivery, not planning.
- The prompt’s display title still says exchange 01; its explicit coordinate block, continuity and filename mapping identify exchange 02. This report follows those explicit coordinates. Correct future prompt titles prospectively.

## 9. Closeout and smallest next step

Changed files: none. Commit/push result: none; read-only Git only. No product tests ran, and historical test counts are not promoted into current evidence.

Resolved Execution Issues / Near-Misses: two initially guessed ADR filenames were unavailable; the tracked ADR index/file listing supplied the correct names before their contents were used. Large inspection outputs were sometimes truncated; material design decisions were checked through bounded follow-up excerpts. No mutation or acceptance claim resulted from those inspection issues.

Pre-Existing Failure Classification: none. The carried listbox and documentary findings are source-observed findings, not newly executed test failures.

Smallest next step: persist this exact report through the authorized completion route, then have the Orchestrator reconcile and approve the plan before issuing the fresh Implementation Worker grant. Missing file delivery requires persistence recovery, not another planning cycle.

Authority expiry: submission of this terminal report ends this exchange’s authority. Implementation in this session remains prohibited. The plan grants no implementation, acceptance, publication, deployment or closure authority.

Orchestration critique:  
MEASURED: P4 is now satisfied, permitting a complete plan despite the client write restriction; preserve the exact returned content through authorized persistence. The renewed prompt’s display title retains exchange 01 while its structural coordinates correctly specify exchange 02; align future titles before delivery.  
LEAD: none
