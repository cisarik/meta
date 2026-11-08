### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ux-refresh-acceptance-and-promotion
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Task identity: UXR-PLAN-02
```

Status: PASS

Phase-qualified result: not-applicable

Logical-whole closure: not-closed

Start commit: `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`

End commit: `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`

Changed files: none in `cisarik/kronika`. This report file is the only write, and it is outside the repository.

Purpose: decision-complete acceptance and promotion plan for `8cbbcad..cb5fa4d`. No implementation, audit, publication, or deployment.

Tests and validation: repository gate re-verified. Claims established by source and test reading. The JavaScript suite and focused pytest were not executed. The NUC helper was invoked and exited before host contact.

Commit and push: not authorized. Not performed.

Report justification: `new-evidence`

Authority expiry: on submission of this report, planning authority expires. Implementation in this session is prohibited. A later execution authority event is an explicit ORCHESTRATOR prompt with `Native planning mode: not-used`.

Deviation: the issued grant forbade every write, including `02_report_00.md`. After the plan was complete, the Cooperator named this exact path and directed the Worker to write the finished report so he can ferry the file. The write is that one file. No repository path, Git operation, NUC command beyond the failed read-only helper, or secret value was written.

## Planning record

```text
Planning cycle: initial
Prior planning report: none
Prior planning note: the 01/01 exchange was a prompt-defect BLOCKED report, not an accepted plan, and its artifacts were withdrawn
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
```

Native planning mode was enabled at the start. This session had no prior conversation about the whole.

## Repository gate

Re-measured before the inventory was trusted.

```text
HEAD: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
branch: main
public main: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
working tree: clean
.ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
8cbbcad is an ancestor of HEAD
ap doctor: PASS (strict pin, clean submodule, managed block, governing variant stable)
ap project check --baseline cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738: PASS
```

`ap project check` also printed its standard sanitized-environment warning. That warning is not a gate failure. Python was CPython 3.13.14 through the declared AP route. Ambient `python`, `python3`, `.venv/bin/python`, and `poetry run` were not used for evidence. The release helper, when invoked, is allowed to call the repository `.venv` internally; this session did not call that interpreter directly.

Chain, oldest to newest: `8cbbcad` Harden NUC service units and add boundary recovery helper; `01dda1f` Make the web shell and companion icon-first and easier to use; `92a537a` Give dialog and cockpit action buttons leading icons; `9318af4` Add YouTube saving, preview backfill and companion upload; polish gallery actions; `cb5fa4d` Send the interactive confirmation with companion YouTube requests.

Alembic head in this tree is revision `0035`. The range adds no migration file.

## Re-measured change inventory

`git diff --shortstat 8cbbcad..cb5fa4d`: 33 files changed, 2903 insertions, 196 deletions. The path set matches the issued prompt. Binary icon deltas are excluded from the line counts, which is why their numstat is blank.

`git diff --shortstat 9318af4..cb5fa4d`: 2 files changed, 6 insertions, 2 deletions.

```text
extension/background/service_worker.js
tests/contract/test_tailscale_ingress_security.py
```

That pair is the whole server-identical tail. `cb5fa4d` adds `confirmation_method: "interactive"` to the companion YouTube POST body and the same field to the ingress fixture. It does not change route policy, the web shell, or the backfill coordinator. The NUC already serves the web shell and server from `9318af4`. The unpacked companion on the workstation may already be `cb5fa4d`. Formal rendered acceptance still requires one accepted SHA on the NUC.

| Path | Change | Surface | Behavioral purpose | Pinning test |
|---|---|---|---|---|
| `docs/UX_AUDIT.md` | A | documentation | Records the UX findings and the resolutions already built | none |
| `extension/background/service_worker.js` | M | companion | `SAVE_YOUTUBE` / `POLL_YOUTUBE`; POST body sends `confirmation_method: "interactive"` | none for the YouTube body |
| `extension/content/x_adapter.js` | M | companion | Save control sits 10 px from the tile corner and 76 px up on video hosts | `tests/x_companion_extension.test.js` (`bottom: 76px` on the video rule) |
| `extension/content/youtube_adapter.js` | A | companion | In-player Save, auto-hide, poll to a terminal label | none |
| `extension/icons/icon16.png` | M | companion | Replaces the placeholder icon | none |
| `extension/icons/icon48.png` | M | companion | Replaces the placeholder icon | none |
| `extension/icons/icon128.png` | M | companion | Replaces the placeholder icon | none |
| `extension/manifest.json` | M | companion | Adds a YouTube content script and mentions YouTube in the description. The public `key` field is unchanged | `tests/x_companion_extension.test.js` still pins `optional_host_permissions` and the absence of `host_permissions`; it does not pin the new matches |
| `extension/shared/messages.js` | M | companion | Adds `acceptYouTubeVideoUrl` and the YouTube message types | none |
| `extension/ui/picker.css` | M | companion | Picker visual pass | existing picker pins, not re-listed here |
| `extension/ui/picker.html` | M | companion | Picker visual pass | existing picker pins |
| `extension/ui/save.css` | M | companion | Save-popup visual pass | existing save pins |
| `extension/ui/save.html` | M | companion | Save-popup visual pass | existing save pins |
| `extension/ui/sidebar.css` | M | companion | Welcome, history sheet, hosted-shell styling | companion UI tests below |
| `extension/ui/sidebar.html` | M | companion | Welcome form, history sheet, title-bar upload, Disconnect copy in Settings | `tests/x_companion_extension.test.js` Disconnect/upload test |
| `extension/ui/sidebar.js` | M | companion | Inline connect, history sheet, `open_upload` after handshake | same test pins `#upload-open` and Disconnect placement, not the handshake guard |
| `src/kronika/adapters/api/application.py` | M | server | Starts `GalleryPreviewBackfillCoordinator` in the lifespan only when the setting is true, and stops it inside the shared shutdown budget | no flag test; coordinator unit tests are separate |
| `src/kronika/adapters/api/tailscale_ingress.py` | M | server | One added field: `companion_mutation=True` on `POST /api/youtube/requests` | `tests/contract/test_x_route_policy.py::test_only_companion_mutations_are_companion_flagged` |
| `src/kronika/adapters/api/web/app.js` | M | web shell | Header menus, navigation, composer dollars, upload drop zone, `data-icon` observer, `open_upload` capability guard | brand and one menu-item pin; no behavioral test of the menus or the observer |
| `src/kronika/adapters/api/web/companion_host.js` | M | web shell | Adds `open_upload` to the pinned-origin parent-window protocol | `tests/companion_web_bridge.test.js` pins the origin constant only |
| `src/kronika/adapters/api/web/index.html` | M | web shell | Icon header, tab bar, heroes, `K` mark | `tests/contract/test_local_web_application.py` brand tests; `tests/kronika_ui.test.js` brand mark |
| `src/kronika/adapters/api/web/styles.css` | M | web shell | Appended experience layer: menus, bottom nav at ≤720 px, card glass, hosted brand hide | no new CSS slice test for the appended layer |
| `src/kronika/application/gallery_preview_backfill.py` | A | server | In-process preview backfill on one worker thread | `tests/unit/test_gallery_preview_backfill.py` |
| `src/kronika/configuration.py` | M | configuration | `gallery_preview_backfill_enabled`, default true, env prefix `KRONIKA_` | none by name |
| `tests/ai_providers_admin_frontend.test.js` | M | test | Header control is a `header-menu__item` with `role="menuitem"` | this file |
| `tests/contract/test_local_web_application.py` | M | test | Visible brand is `K`; `FN` is absent | this file |
| `tests/contract/test_tailscale_ingress_security.py` | M | test | Companion YouTube POST is not `MUTATION_ORIGIN_FORBIDDEN` when the body includes `confirmation_method: "interactive"` | this file |
| `tests/contract/test_x_route_policy.py` | M | test | YouTube submit is the sixth flagged route; the flagged set is exact | this file |
| `tests/gallery_search_tag_filters.test.js` | M | test | Header search prompt icon is `🔎` | this file |
| `tests/kronika_ui.test.js` | M | test | `.brand-mark` text is `K` | this file |
| `tests/unit/test_gallery_preview_backfill.py` | A | test | Pass bound, failure skip, idle catalog, start/shutdown | this file |
| `tests/x_companion_extension.test.js` | M | test | Video save offset, Disconnect in Settings, `#upload-open` in the title bar | this file |
| `tests/youtube_acquisition_cockpit.test.js` | M | test | YouTube menu item is a menuitem whose visible text matches `▶ YouTube` | this file |

Prompt deltas:

- The path set, the 33-file count, and `+2903/−196` match.
- The extension-only path pair matches. The prompt did not state the `+6/−2` shortstat. That is additional measurement, not a contradiction.
- The prompt says `docs/UX_AUDIT.md` has no declared lifecycle. The file's Status block already names classification, consumers, and retention. It still has no authority, no cleanup owner, and no inbound link.
- This session did not re-verify the NUC. See the transport section.

## Acceptance control matrix

Evidence tier E3 means a fresh independent auditor must accept the claim. E2 means this planning reading plus, where noted, Cooperator rendered acceptance. "Gap" is the smallest pin that would close a missing control. A gap is not by itself a code defect. The auditor decides whether a shared existing control is enough.

| Claim ID | Surface | Exact claim (positive and negative) | Evidence type | Exact test/command/observation | Evidence tier | Acceptance owner | Pass criteria | Current gap |
|---|---|---|---|---|---|---|---|---|
| A1 | Ingress | Positive: `companion_mutation=True` is exactly POST `/api/x/requests`, POST `/api/x/requests/{id}/retry`, POST `/api/companion/review-inbox/{id}/opened`, POST `/api/companion/review-inbox/{id}/apply`, PUT `/api/admin/settings/automatic-analysis`, and POST `/api/youtube/requests`. Negative: every other policy is unflagged, including POST `/api/youtube/requests/{id}/retry` and POST `/api/uploads`. | Contract source pin | `tests/contract/test_x_route_policy.py::test_only_companion_mutations_are_companion_flagged` | E3 | Fresh independent auditor | Set equality holds on the candidate SHA | none for the policy set |
| A2 | Ingress | Positive: a companion origin is allowed only when the matched policy is flagged and the origin is in the allowlist (`_mutation_origin_allowed`). Negative: an unflagged unsafe method returns 403 `MUTATION_ORIGIN_FORBIDDEN`. | Source plus one runtime sample | `tailscale_ingress.py` origin helper; `test_companion_origin_is_accepted_only_on_flagged_companion_routes` samples POST `/api/canonical-tags` | E3 | Fresh independent auditor | Auditor accepts the shared gate, or the sample is extended | Runtime sample is one route. Smallest pin: the same test also POSTs YouTube retry and `/api/uploads` with companion headers and expects `MUTATION_ORIGIN_FORBIDDEN` |
| A3 | Ingress | Positive: YouTube submit requires capability `youtube.request`, writes audit `youtube.request.submit` before the action, and accepts only `confirmation_method: "interactive"`. The companion worker sends that field. Negative: a missing or non-interactive confirmation never reaches `submit`; `yes_flag` is not accepted on the requester API. | Policy pin, model, worker source | Route-policy test asserts the audit action and the flag. `YouTubeRequestCreateBody.confirmation_method: Literal["interactive"]`. `service_worker.js` `saveYouTube`. Ingress test sends the field and asserts only that the error is not `MUTATION_ORIGIN_FORBIDDEN` | E3 | Fresh independent auditor | Audit row `youtube.request.submit` when admitted; omitted confirmation is 422 and creates no submit audit | Ingress test does not assert success, the audit row, or a missing confirmation. Smallest pin: those two assertions, plus a Node assertion that the worker body literal contains `confirmation_method: "interactive"` |
| A4 | Ingress | Positive: after origin and the mutation header, identity is resolved and `has_capability` runs. The flag does not skip it. `ROLE_USER` and `ROLE_ADMIN` both include `youtube.request`. The public audience does not. Negative: the pinned origin does not grant the capability; the retry path is rejected as an unflagged origin before capability is considered. | Source order and role sets | `tailscale_ingress.py` checks around the origin, header, identity, and capability blocks; `identity_access.py` `CAPABILITIES_BY_ROLE` | E3 | Fresh independent auditor | Check order unchanged and no mapped role lacks `youtube.request` | No synthetic role without the capability, because none exists. No code change |
| A5 | Ingress | Positive: origin must equal the configured external origin, or be flagged and allowlisted. `X-Kronika-Request` must be exactly `1`. Negative: the header alone does not authorize; a spoofed or missing origin is 403; an empty allowlist rejects the extension origin; YouTube does not relax any other route. | Existing negative tests on the shared gate | `test_spoofed_or_absent_companion_origin_is_rejected`; `test_empty_companion_allowlist_rejects_extension_origin`; `test_hostile_or_inexact_origin_is_rejected` | E3 | Fresh independent auditor | Those tests stay green and the auditor accepts that YouTube uses the same helper | YouTube POST is not in the spoof or empty-allowlist tests. Same test-only pin as A2 |
| A6 | postMessage | Positive: `open_upload` is handled only when `event.origin` is the pinned extension origin and `event.source` is the parent window. The sidebar posts it only when a stored origin exists, `handshakeSeen` is true, and `acceptKronikaOrigin` accepts it. `handshakeSeen` is set on `WEB_READY` or `HOST_ACK`. The shell opens the dialog only when the upload button exists and is not hidden. Negative: no other origin, no other window, and no capability-hidden button opens the dialog. | Source reading | `companion_host.js` `onMessage`; `sidebar.js` upload click; `app.js` `onOpenUpload`. `tests/companion_web_bridge.test.js` pins `PINNED_EXTENSION_ORIGIN` only | E3 | Fresh independent auditor | A bridge test rejects a foreign origin and a non-parent source, and source assertions pin both guards | No test covers the message. Smallest test: extend `tests/companion_web_bridge.test.js` and pin the two guards |
| A7 | Manifest | Positive: the new content script matches only `https://www.youtube.com/*` and `https://m.youtube.com/*`. `optional_host_permissions` remains `https://*.ts.net/*`. There is no `host_permissions` key. Permissions stay `alarms`, `sidePanel`, `storage`. The `key` field is unchanged and must not be copied into a report. Negative: `music.youtube.com` and `youtu.be` are canonicalized by `acceptYouTubeVideoUrl` but do not receive the content script. | Diff plus existing manifest pins | `git diff 8cbbcad..cb5fa4d -- extension/manifest.json`; `tests/x_companion_extension.test.js` host-permission assertions | E3 | Fresh independent auditor | Match list is exactly those two patterns | No assertion of the new `content_scripts` entry. Smallest pin: one deep equality on that matches array |
| A8 | Secrets | Positive: the changed diff adds no token, cookie, private media filename, host identifier, or private network value. The public video id `jNQXAC9IVRw` in the ingress fixture is the known public test video. Negative: the gitignored companion private key was not read. | Diff inspection | Planning diff of the manifest, ingress, worker, and docs. The manifest `key` line is context, not a change | E3 | Fresh independent auditor | Auditor re-reads the diff and does not print the extension key | none found in this reading |
| B1 | YouTube save | Positive: the button is inside `.html5-video-player`, 14 px from the top and left, hidden unless the player is hovered, not in `ytp-autohide`, busy, done, failed, or focused. Clicks stop propagation. Negative: it is not placed on the bottom control bar. | Source | `extension/content/youtube_adapter.js` style and `playerElement` | E2 | Cooperator rendered acceptance | On a real watch page the control follows auto-hide and does not cover fullscreen or playback | No automated test. Optional source pin of the offsets and `ytp-autohide` selectors |
| B2 | YouTube URL | Positive: `acceptYouTubeVideoUrl` canonicalizes watch, shorts, live, embed, and `youtu.be` to `https://www.youtube.com/watch?v=<11-char id>`. Negative: it rejects non-https, userinfo, a non-443 port, a bad id, and non-video paths. The server re-validates. Raw `/live` and `/embed` URLs remain rejected if submitted directly; the companion does not send those forms. | Source, contrasted with existing server tests | `messages.js` `acceptYouTubeVideoUrl`. Server rejection of raw live/embed is in `tests/unit/domain/test_youtube_acquisition.py` and `tests/youtube_acquisition_cockpit.test.js`, which do not call the companion function | E2 | Fresh audit for the request body; Cooperator for the button | Node cases for the five accepted forms and the rejects | No test calls `acceptYouTubeVideoUrl` |
| B3 | YouTube poll | Positive: the worker maps `completed` and `completed_private` to done, `failed` and `unavailable` to failed, otherwise pending. The button shows `Queued…`, `Downloading…`, `Processing…`, or `Saved to Kronika ✓`. Poll is a GET every 4 seconds for at most 30 minutes. Negative: busy and done do not POST again. A poll transport failure retries the GET, not the POST. After the budget the button returns to idle without a POST. A later click can POST, and the server reuses an still-active request. A failed click may POST again. There is no automatic resend. | Source plus existing reuse test | `youtube_adapter.js` `save`, `poll`, `phaseCopy`; `service_worker.js` `youtubeSnapshot`; `tests/contract/test_youtube_request_api.py::test_same_requester_same_source_active_reuse_skips_admission_limits` | E2 | Cooperator for the visible sequence; auditor for the no-resend reading | Rendered Queued → Downloading → Saved, and a failure stays visible | No Node test of the state machine |
| B4 | YouTube confirmation | Positive: the click is the interactive confirmation and the POST body carries `confirmation_method: "interactive"`. Negative: the content script does not invent `yes_flag`. | Worker source | `saveYouTube` in `service_worker.js` | E3 | Fresh independent auditor | Same pin as A3 | Same gap as A3 |
| B5 | YouTube privacy | Positive: the content script talks only to the extension. The worker fetches the configured Kronika origin. Negative: the flow does not read cookies, sessions, localStorage, profiles, unrelated tabs, or history, and it does not select a model or call a provider. | Source reading | `youtube_adapter.js` and `saveYouTube` contain no cookie, model, or provider call | E3 | Fresh independent auditor | Auditor confirms that reading | No separate test. No code change expected |
| C1 | Backfill lifetime | Positive: the coordinator is constructed and started only when `gallery_preview_backfill_enabled` is true, then registered as `gallery_preview_backfill` and stopped through `shutdown_executor_backed_coordinator` inside `APPLICATION_LIFESPAN_SHUTDOWN_BUDGET_SECONDS` (20). Negative: the flag false leaves `owned_gallery_preview_backfill` unset, so the lifespan does not start it. | Source | `application.py` construction near the preview service and the lifespan `started` list; `in_process_lifecycle.py` constant 20.0; unit test `test_start_and_shutdown_run_a_pass_in_the_background` uses its own short delay | E2 | Auditor reads the flag; rendered acceptance sees previews | Flag false builds no coordinator; shutdown uses the 20-second deadline | No test that the setting false skips construction |
| C2 | Backfill bounds | Positive: defaults are 12 items per pass, 60-second interval, 60-pass failure skip, and a plan window of 500. An unavailable catalog returns without `generate_one`. Negative: a pass does not exceed the item bound, and a failed item is not retried on the next pass. | Unit tests plus constants | `test_pass_generates_missing_previews_up_to_the_per_pass_bound` injects `items_per_pass=2`; `test_failed_items_are_skipped_on_following_passes`; `test_unavailable_catalog_does_no_work`. Defaults live on the class | E2 | Independent reading is enough for the bounds | Tests green and defaults remain 12 / 60 / 60 | The pass test does not assert the default 12. Smallest pin: three asserts on `DEFAULT_ITEMS_PER_PASS`, `DEFAULT_INTERVAL_SECONDS`, and `DEFAULT_FAILURE_RETRY_PASSES` |
| C3 | Preview GET | Positive: GET `/gallery-preview` opens a ready derivative or returns a sanitized error. Negative: a missing derivative is not generated. | Contract test | `tests/contract/test_gallery_preview_api.py::test_missing_derivative_is_not_generated_by_get_and_error_is_sanitized` | E2 | Existing contract; auditor confirms it still binds | Test stays green | none |
| C4 | Preview writes | Positive: `generate_one` publishes only through the preview cache after `_ensure_cache_root_outside_source_roots`. A cache root equal to or inside a library root fails closed. The coordinator does not write the catalog database. Negative: the backfill cannot write `/srv/media` when that path is a library root. | Source | `gallery_preview.py` `generate_one` and `_ensure_cache_root_outside_source_roots`; cache constructed from `gallery_preview_cache_path` | E3 for the filesystem claim | Fresh independent auditor | Auditor accepts the guard | No test names the guard. Smallest pin: one unit test that a cache root inside a library root raises and does not publish |
| C5 | Backfill setting | Positive: `gallery_preview_backfill_enabled` defaults true and the `KRONIKA_` prefix maps `KRONIKA_GALLERY_PREVIEW_BACKFILL_ENABLED`. Negative: no document and no test currently say so. | Settings class | `configuration.py` field and `env_prefix="KRONIKA_"` | E2 | Documentation grant | Env example, SPEC, and DEVELOPMENT state the name, default, and the GET rule | Undocumented and untested by name |
| C6 | Backfill time bound | Positive: frame extraction uses `FFMPEG_FRAME_TIMEOUT_SECONDS` 30 and probe uses `FFPROBE_TIMEOUT_SECONDS` 15, on the one worker thread. Failures skip 60 passes. Negative: one item cannot hold the thread indefinitely. A frame still running can outlast the 20-second shutdown budget and be logged unresolved. The event loop is not blocked by `generate_one`. | Constants and call path | `media_analysis.py` timeouts; `ffmpeg.py` passes the frame timeout; backfill `_run_pass` catches errors and continues | E2 | Acceptance record. Residual is low | Auditor agrees the subprocess timeouts are the bound | No backfill-specific timeout test. No code change unless the auditor disagrees |
| D1 | Header menus | Positive: `setupHeaderMenus` opens, closes, moves with arrows, closes on outside click and Escape, and redirects focus from a hidden item to the trigger. CSS `.header-menu:not(:has(.header-menu__item:not([hidden])))` hides a menu whose items are all hidden. Negative: the information architecture is not redesigned. | Source | `app.js` `KRONIKA_HEADER_MENUS` block; `styles.css` `:has` rule. One admin control is pinned as `header-menu__item` | E2 | Cooperator rendered acceptance | Menus hide when empty; keyboard, outside click, and focus return work | No behavioral test |
| D2 | Navigation | Positive: `.kronika-nav` is the icon tab bar, shown for a non-public audience and fixed to the bottom at `max-width: 720px`, which includes the side panel. `.kronika-pager` hides when every button is disabled or hidden. Kind cards use `data-kronika-kind`. Negative: the public audience keeps the nav hidden. | Source | `kronikaStartNavigation`; styles at the 720 px block; pager `:has` rule | E2 | Cooperator rendered acceptance | Desktop tabs, bottom bar at narrow width and in the side panel, single-page pagers hidden | No new test |
| D3 | Composer | Positive: visible budgets go through `kronikaUsdFromMicros`. The privacy sentence remains in the same copy. Negative: the API still stores micros. Do not change the API to dollars. | Source | `app.js` composer `parts.push` around the reservation copy | E2 | Cooperator rendered acceptance | Dollars on screen, privacy text still present | No pin that the visible string is dollars |
| D4 | Brand and upload | Positive: the mark is `K`, the upload drop zone exists, and a favicon is present. Negative: `FN` is not a visible brand. | Updated contract tests | `test_header_brand_mark_is_circular_branding_not_button`, `test_header_uses_compact_brand_and_accessible_status_labels`, `test_kronika_shell_adds_timeline_without_replacing_gallery`, `tests/kronika_ui.test.js` brand mark | E2 | Tests now; docs still contradict them | Tests green | `README.md` still says the shell keeps the `FN` mark. `GALLERY.md` still says the temporary `FN` mark is sufficient |
| D5 | Labels | Positive: the measured visible-label change is the YouTube menu item, now matching `▶ YouTube`, and its pinning test was updated in the same range. Brand, search-prompt, menu role, X offsets, and Disconnect copy were updated in their pinning tests. Negative: this plan does not claim an unrun suite proved every other label. | Test diffs | `git diff 8cbbcad..cb5fa4d` of the five listed frontend tests | E2 | Documentation must not silently retitle pinned controls | A later `node --test` run is green, or a failure is a deliberate pin update | Suite not re-run in this exchange |
| E1 | `data-icon` | Positive: `KRONIKA_BUTTON_ICONS` maps an exact plain-text label to `data-icon` and does not change `textContent`. The observer does not watch attributes, so `setAttribute` does not retrigger it. Gallery action cells are skipped. Negative: the observer does replace a different `data-icon` on a mapped plain button, and it removes `data-icon` from an unmapped plain button. The issued sentence "does not overwrite an existing data-icon" is restated to this behavior. Do not change the observer. | Source | `app.js` `kronikaDecorateButton` and `setupButtonIcons` | E2 | Cooperator for visible icons; this plan for the restated claim | Labels unchanged; no mutation loop | No test. Optional pin of map, text stability, and no attribute loop |
| E2 | Icon assignment | Positive: only exact label keys receive an icon. `Cancel` and `Cancel upload` are different keys. Negative: an unmapped label does not keep a stale `data-icon`. | Source | The frozen map in `KRONIKA_BUTTON_ICONS` | E2 | Same as E1 | No unrelated label gains an icon | Same optional test |
| F1 | Companion chrome | Positive: welcome connects from an inline form, history is the drop-down sheet, and the icon files are no longer 1×1 placeholders. Negative: this plan does not claim a pixel test. | Source and `docs/UX_AUDIT.md` findings 8 and 9 | Icon blobs changed in `01dda1f`; sidebar welcome form | E2 | Cooperator rendered acceptance | Welcome, real icons, history sheet | none that blocks the plan |
| F2 | Hosted shell | Positive: `.kronika-companion-hosted .brand { display: none }`. The side panel keeps the shell navigation because the iframe is the shell. Negative: ordinary browser tabs do not get that class until the host reports hosted. | Source | `styles.css` hosted block; `syncCompanionHostedClass` | E2 | Cooperator rendered acceptance | Duplicate brand hidden only in the side panel | none beyond rendered acceptance |
| F3 | Disconnect | Positive: Disconnect lives in Settings. The pinning test requires the action below Save and the copy "Disconnect below clears the session". Negative: it is not the title-bar control. | Test | `tests/x_companion_extension.test.js` test "side-panel Settings Save sits under origin; Disconnect lives in Settings and Upload in the title bar" | E2 | Test now; `docs/X_COMPANION.md` is stale | Test green | `docs/X_COMPANION.md` still says the title-bar control is Disconnect when connected |
| F4 | Title-bar upload | Positive: `#upload-open` is in the title bar, above Settings, and posts `open_upload` only after the handshake guard in A6. The shell then applies the capability guard. Negative: the existing test does not prove the handshake or the capability check. | Test plus source | The same companion test pins the element position. Behavior is A6 | E3 for the message; E2 for the button's presence | Auditor for A6; Cooperator for the click | Button visible; dialog opens only with upload capability | A6 |
| F5 | Companion secrets | Positive: side panel, save, and picker do not embed a host identifier or a secret. The welcome field accepts an origin the user types. Negative: repository artifacts must not gain that origin. | Diff reading | No host value added in the companion diff | E2 | Auditor overlaps A8; Cooperator sees the panel | No secret or host value on screen beyond the origin the user typed | none found |
| G1 | JavaScript baseline | Positive: `tests/*.test.js` is 34 files at this SHA. The issued 593 pass / 0 fail / 5 skipped figure was not re-run. Negative: this plan does not treat that count as fresh evidence. | File census | Glob of `tests/*.test.js` returned 34 paths. `node --test` was not required to establish a claim | E2 | A later grant re-runs only if a claim needs it | Command is `node --test tests/*.test.js` | Count of results not re-measured |
| G2 | Python route | Positive: the repository gate passed on the baseline. Focused tests, when a later grant needs them, go through `./.ap/ap exec --root /Users/agile/Projects/kronika --baseline <sha> --operation test-focus`. Negative: this exchange ran no pytest. | Gate | `./.ap/ap project check --baseline cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738` PASS | E2 | Later grants | Gate PASS on the candidate they actually test | Focused tests not executed |
| G3 | Pre-existing failures | Positive: the known macOS failures stay classified and are outside this whole. Negative: nobody "fixes" them here. | Inherited classification | Not re-executed. The list is in Pre-Existing Failure Classification | E2 | Later Workers classify, they do not repair | Those names stay out of this whole's diff | none |
| H1 | `docs/UX_AUDIT.md` | Positive: the record keeps its Status prose and gains authority, a cleanup owner, and one inbound link. Negative: it does not become task authority. | File reading | Status block is present. `git grep` found no inbound link | E2 | Documentation grant | RF-14 block below is present and DEVELOPMENT links to the file | Authority, cleanup owner, and discoverability are missing |
| H2 | Gallery freeze | Positive: card and Details visuals stay frozen. The Cooperator-authorized exception is the 40 px glass card overlay. The visible mark is `K`. Negative: the freeze is not reopened. | `GALLERY.md` plus the card work in `9318af4` | `GALLERY.md` still states the freeze and the `FN` sentence | E2 | Documentation grant | One exception paragraph and the `K` sentence | Exception unrecorded; `FN` sentence false |
| H3 | Durable decision | Positive: one new ADR-0086 records the sixth flagged route, `open_upload`, the title-bar upload control, the backfill coordinator, and the YouTube content-script matches. Negative: historical ADR bodies are not edited. ADR-0079 is not the place for this decision. | ADR index | Highest accepted ADR is 0085. No `0086` file exists. `docs/X_COMPANION.md` and ADR-0079 still say five routes | E2 | Documentation grant | New ADR plus the README index row; living "exactly five" sentences updated | No ADR |
| H4 | Living docs | Positive: README, SPEC, SECURITY, DEVELOPMENT, and the env example each carry only the claim they own. Negative: they do not repeat the whole matrix. | File reading | None of those files name the backfill setting or the YouTube companion route | E2 | Documentation grant | Inventory below | All five silent |
| H5 | Companion guide | Positive: `docs/X_COMPANION.md` is updated because it currently states the route count and the Disconnect placement as operator truth. Negative: it does not become a second SPEC. | File reading | "Exactly five `companion_mutation` routes" and the title-bar Disconnect sentences | E2 | Documentation grant | Six routes, YouTube content script, `open_upload`, Disconnect in Settings | Necessary owner omitted by the prompt's named list; the matrix requires it |
| H6 | Manifest docs | Positive: an operator finds the YouTube content-script matches and the unchanged optional `https://*.ts.net/*` permission in the companion guide and SECURITY. Negative: no broader host permission is documented into existence. | Manifest diff | Matches added; `host_permissions` still absent | E2 | Documentation grant | Those two sentences exist | Undocumented |

## E3 audit package

This planning exchange does not perform the audit and does not claim a result.

```text
Security task class: fresh focused audit, INFOSEC route R3, sections 4.2, 4.4, and 4.5
Candidate: the exact public main SHA at audit start. Today that is cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738. If main has moved, stop.
Independence: a fresh Worker who is not this Planner, not a subagent of this Planner, and not the later implementation Worker
Authority: read-only, plus the bound test route for the named controls only
Correction: the auditor reports findings and does not edit them
```

Owner map and allowlist for the audit reading:

- Route policy and origin gate: `src/kronika/adapters/api/tailscale_ingress.py`, `tests/contract/test_x_route_policy.py`, `tests/contract/test_tailscale_ingress_security.py`
- Request body, capability, reuse: `src/kronika/adapters/api/youtube_request_api.py`, `src/kronika/domain/identity_access.py`, `tests/contract/test_youtube_request_api.py`
- Companion body: `extension/background/service_worker.js`, `extension/shared/messages.js`, `extension/content/youtube_adapter.js`, `extension/manifest.json`
- postMessage: `src/kronika/adapters/api/web/companion_host.js`, `extension/ui/sidebar.js`, `src/kronika/adapters/api/web/app.js`, `tests/companion_web_bridge.test.js`
- Preview writes: `src/kronika/application/gallery_preview_backfill.py`, `src/kronika/application/gallery_preview.py`, `src/kronika/adapters/api/application.py`, `tests/unit/test_gallery_preview_backfill.py`, `tests/contract/test_gallery_preview_api.py`

Positive controls are A1, A3's existing policy pin, A4's check order, A5's existing negative tests, C3, and C6's timeouts. Negative controls the auditor must judge are A2, A3's missing audit and confirmation assertions, A5's YouTube samples, A6, A7's match list, and C4.

Threat-model points:

- Origin trust: the companion origin is an allowlisted exception on flagged unsafe methods only. It is not proof of the extension process; it is the same Origin header model already used for X.
- Capability gate: origin is checked before identity and capability. The flag does not add `youtube.request`.
- Audit trail: `youtube.request.submit` is the policy action and is recorded before the handler. The handler then records `youtube.request.submit.new` or `youtube.request.submit.reuse`.
- Confirmation binding: the requester model allows only `interactive`. The worker hard-codes that value. The click is the confirmation.
- Replay and duplicate submission: `create_or_get_active` returns the active claim for the same requester and source. The content script suppresses a second POST while busy or done. A POST after the 30-minute UI budget relies on that server reuse.
- Cross-origin postMessage: `open_upload` requires the pinned origin and the parent window. The dialog also requires the upload control to be visible.
- Manifest permissions: two YouTube host patterns, optional `https://*.ts.net/*`, no `host_permissions`.
- Secret and host-value leakage: the diff must not gain any. The extension `key` field is pre-existing and is not copied into the audit report.
- Filesystem: preview generation writes the cache and refuses a cache root inside a library root. GET does not generate.

Expected evidence: the named tests read, and executed only through the bound route if the auditor cannot close a claim by reading. Stop if the candidate SHA moves, the tree is dirty, the audit would need a secret, a browser profile, the NUC environment file, a provider call, or a live acquisition. A missing YouTube-specific sample is a finding only if the auditor rejects the shared gate. Test-only pins are INFOSEC R0. A code change on the origin, capability, or audit path is a security-boundary correction and requires a later full fresh re-acceptance by a Worker who neither audited nor patched. The auditor must not self-certify a correction.

## Documentation-promotion inventory

One new ADR. Do not amend ADR-0079 in place. ADR-0079 is the fifth-route automatic-analysis decision; its own text already left older "exactly four" bodies frozen and updated living sentences instead. The same pattern fits here. The next free number is 0086. Suggested path: `docs/adr/0086-companion-youtube-save-upload-message-and-preview-backfill.md`, plus one index row in `docs/adr/README.md`.

ADR-0086 claims:

- `POST /api/youtube/requests` is the sixth `companion_mutation` route. Capability `youtube.request`, audit action `youtube.request.submit`, body confirmation `interactive`. YouTube retry stays unflagged.
- `open_upload` is accepted only from the pinned extension origin and the parent window, and the shell opens the upload dialog only when the upload control is visible.
- The title-bar upload control posts that message only after the sidebar handshake. Disconnect stays in Settings.
- `GalleryPreviewBackfillCoordinator` runs in-process on one thread when `gallery_preview_backfill_enabled` is true, at most 12 items per pass, failures skipped for 60 passes, inside the 20-second shutdown budget. GET `/gallery-preview` never generates.
- The extension content script matches `https://www.youtube.com/*` and `https://m.youtube.com/*` only. Optional host permission stays `https://*.ts.net/*`. There is no `host_permissions` key.
- This ADR supersedes the living "exactly five routes" sentences. It does not edit ADR-0064, ADR-0072, ADR-0073, ADR-0076, ADR-0079, or ADR-0080.

Other files:

| File | Current gap | Exact claim to add | Section | Validation | Owner |
|---|---|---|---|---|---|
| `README.md` | Says the shell keeps the `FN` mark. Silent on companion YouTube save and in-process previews | The visible mark is `K`. The companion can save a YouTube video from the player. Missing gallery previews are filled in-process. | Accepted Transition, the sentence that still names `FN` | Brand tests already reject `FN` | current product status |
| `SPEC.md` | §§14, 16, and 19 do not normatively state the new route, bounds, or message | One flagged YouTube route with capability, audit action, and interactive confirmation. Backfill bounds and "GET does not generate". `open_upload` origin and capability rule | §§14, 16, 19 | Route-policy test and preview GET test | normative requirements |
| `SECURITY.md` | Privacy section does not name the sixth route or the YouTube content script | Six-route set, capability/audit/confirmation chain, the two YouTube matches, optional `https://*.ts.net/*` only, no secrets to ordinary clients | Accepted Kronika Privacy and Research Boundary | Ingress tests | security boundary |
| `GALLERY.md` | Freeze is stated. The glass-overlay exception is absent. The `FN` sentence is false | Freeze remains. Exception: the Cooperator asked for the 40 px glass card overlay. The visible mark is `K` | The freeze paragraph | Card work stays inside that exception | gallery contract |
| `DEVELOPMENT.md` | Launcher doc does not say how to load the companion or disable backfill | Point at the unpacked-load steps in `docs/X_COMPANION.md`. Name `KRONIKA_GALLERY_PREVIEW_BACKFILL_ENABLED`, default true. Link `docs/UX_AUDIT.md` | New short section after Tests | The link is the discoverability pin | contributors |
| `docs/X_COMPANION.md` | States exactly five routes and title-bar Disconnect | Six routes, YouTube content script, `open_upload`, Disconnect in Settings | The route paragraph and the title-bar paragraph | Companion Disconnect test | operators |
| `deploy/systemd/kronika.env.example` | No backfill variable | Commented `KRONIKA_GALLERY_PREVIEW_BACKFILL_ENABLED=true`, default true, GET never generates | Next to `KRONIKA_GALLERY_PREVIEW_CACHE_PATH` | Settings field default | operators |
| `docs/adr/README.md` | Index ends at 0085 | One 0086 row, status Accepted when the documentation grant lands | Index table | File exists | ADR catalog |

`docs/UX_AUDIT.md` RF-14 completion, keeping the existing Status prose:

```text
Relationship: historical product record of one UX round. Not task authority.
Authority: Cooperator observations from that round, already implemented in 01dda1f..cb5fa4d. The documentation grant may add this metadata and must not treat the file as a new product grant.
Consumer: Cooperator, Orchestrator, and Workers touching the web shell or the companion.
Discoverability: one inbound link from DEVELOPMENT.md.
Retention: remains while later UX work uses the findings. Git history is the archive.
Cleanup trigger: closure of ux-refresh-acceptance-and-promotion, or a later UX whole that supersedes the findings.
Cleanup owner: ORCHESTRATOR, by leaving the file as frozen history rather than deleting it.
```

No other product document is in scope. `PRODUCT.md` does not currently state the `FN` mark.

## NUC refresh and rendered acceptance

Planning evidence is the Orchestrator's read-only observation on 2026-11-08, not a fresh helper result from this session:

```text
kronika-release status:
  layout: canonical
  active_release: 9318af471c51c24dbcd8244ab83bcbafb5c7f5c9
  web_release: 9318af471c51c24dbcd8244ab83bcbafb5c7f5c9
  capture_release: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915
  service_active: active
  database_revision: 0035
  backup_restore_readiness: ready

kronika-release check --release cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738:
  PASS
  layout: canonical
  ap_gitlink: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
  public_main: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
  backup_restore_readiness: ready
  capture_bridge_protocol: 1
```

This session ran `deploy/ubuntu/kronika-release status` and `check --release cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`. Both exited 2 with `SSH target is required`, before any host contact. The helper reads `KRONIKA_NUC_SSH_TARGET`, `KRONIKA_NUC_SSH_USER`, and `KRONIKA_NUC_SSH_IDENTITY`. The identity value is the filesystem path passed to `ssh -i`. Unprefixed `NUC_SSH_*` names do not satisfy it. A public-key line is not an identity path. This report does not record target, user, or key material. The deployment grant must start in a shell where the three `KRONIKA_` names are already set, then re-run `status` and `check`. It must not source the operator env file from the Worker.

Preconditions for that later grant: the accepted SHA is public `main`; the local `.ap` HEAD equals that release's gitlink; the checkout is clean; the Cooperator has run `sudo -v` outside the Worker; backup readiness is `ready`; no other mutation is active; transport uses the three canonical names. Expected schema result is same-revision `0035`, because this range adds no migration and the observed catalog is already `0035`. If a later correction adds a migration, compare again. Do not assume `0035` after an unseen commit.

Order:

1. `kronika-release status`
2. `kronika-release check --release <40-hex-sha>`
3. Stop. A check never deploys. The deploy needs its own explicit grant.
4. `kronika-release deploy --release <40-hex-sha> --yes`

Exit 0 is a same-schema update. Exit 13 is `migration-required` and continues only through the annex "Schema-jump continuation after `migration-required` (exit 13)" in `docs/UBUNTU_NUC_DEPLOYMENT.md`. Any other nonzero exit stops the run. Do not improvise a migration.

After deploy, `status` must show `active_release` and `web_release` equal to the deployed SHA, `service_active` active, `database_revision` equal to the packaged head, and `backup_restore_readiness` ready. Provenance is `.kronika-release-sha` and `.kronika-release-manifest.json` on the release tree. The deployed tree has no `.git` metadata. The helper's own cutover verification is the health readback. Do not add a second probe that prints a host name.

Automatic rollback of a failed cutover is the helper restoring the previous release it captured. A deliberate rollback is a separate grant: `kronika-release rollback --release <previous-sha> --yes`. The previous SHA is the `active_release` read before deploy, not a SHA hardcoded by this plan. The capture release stays on its current SHA. The deploy grant states its own terminal `sudo -K` rule. This planning exchange must not run `sudo -K`.

Rendered acceptance belongs to the Cooperator, on the refreshed NUC, in the companion he actually uses. Checklist:

- Header menus open, and a menu whose items are all capability-hidden is absent.
- Icon tab bar on a wide window; bottom tab bar at a narrow width and in the side panel.
- Gallery card buttons readable on light media and on dark media.
- Previews present for items that previously said "Preview unavailable."
- Companion welcome connects inline.
- Title-bar upload opens the upload dialog only when the upload capability is present.
- Disconnect is in Settings.
- History sheet drops down.
- On a real logged-in X post, the save button does not cover fullscreen.
- A YouTube save runs through Queued, Downloading, and "Saved to Kronika ✓", or a failure stays visible and is not silently resent.

## Verification side effect

The acquired item is the public 19-second video `jNQXAC9IVRw`, stored as a requester-private download for the Cooperator's identity. Removal is the administrator catalog-removal workflow: preview `GET /api/admin/media/{media_id}/catalog-removal`, then `POST /api/admin/media/{media_id}/catalog-removal`, capability `media.catalog.remove`, audit `media.catalog_remove`. The shell label is "Remove from catalog". Nobody deletes a file under `/srv/media`.

Recommendation: leave the item in place until rendered acceptance, because that checklist includes a completed YouTube save, then remove it through the workflow above. Keep it only if the Cooperator wants a documented requester-private fixture. An administrator can read it either way. The Cooperator decides. This plan does not remove it.

Consequence of removal: the item leaves the owner's gallery; the claim becomes `catalog_removed`; the receipt and audit row remain. Consequence of keeping it: it stays private to that owner and visible to an administrator, and it must be described as a verification item so it is not mistaken for household material.

## Execution sequence and budgets

1. Fresh independent E3 audit of this matrix. One exchange. Reasoning High. About 250k tokens is enough. Read-only. Named tests only if reading cannot close a claim. No full Python suite. No browser. No NUC deploy. The auditor does not correct.
2. At most one correction, and only for a concrete finding. Test-only pins may share the documentation session. A change to the origin, capability, or audit path is its own session, and a different session then does full fresh re-acceptance. The corrector does not self-certify. If the same finding survives that one correction, the result is `PARTIAL` or `BLOCKED` with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`. No second correction. No audit of the audit.
3. Documentation implementation on the allowlist in the promotion inventory, only after the acceptance result is PASS. One session. Reasoning Medium. If step 2 was a security-boundary code change, documentation waits for the re-acceptance PASS and does not share that correction session.
4. Publication of the accepted SHA. Separate grant. The Cooperator owns Git publication.
5. NUC refresh to that exact SHA. Separate grant. Re-run `status` and `check` in that session. Deploy only after the grant says `deploy --yes`.
6. Cooperator rendered acceptance on that NUC. Not a Worker browser session.
7. ORCHESTRATOR closure.

Session sharing: the audit shares a session with nobody. A security-boundary correction shares a session with nobody. Test-only pins may share the documentation session. Publication, NUC refresh, and rendered acceptance are separate. This Planner session implements nothing.

Do not run the full Python suite in any of these steps. Known macOS failures stay classified. JavaScript, when needed, is `node --test tests/*.test.js`. Python is `./.ap/ap exec --root /Users/agile/Projects/kronika --baseline <sha> --operation test-focus -- <pytest-args>`.

## Open decisions

1. The Cooperator decides whether `jNQXAC9IVRw` is removed after rendered acceptance or kept as a documented requester-private fixture. This plan recommends removal after acceptance.
2. Any audit finding at medium or higher is a later Cooperator residual-risk decision. None is open now.
3. No product decision is open. ADR-0086 as one new ADR, the restated `data-icon` claim, and the inclusion of `docs/X_COMPANION.md` are plan decisions.

## Risks

| ID | Disposition | Residual owner |
|---|---|---|
| R1 | Open until the E3 audit accepts the ingress change. This matrix reduces it to named controls. | Cooperator if the residual is medium or higher |
| R2 | Open until the NUC runs the accepted SHA. The current gap is one extension-only commit plus any later documentation commits. | Routine refresh under ADR-0075 |
| R3 | Reduced to ADR-0086. Open until that file exists. | Documentation grant |
| R4 | Reduced to one GALLERY exception paragraph. Open until written. | Documentation grant |
| R5 | Reduced to the living-doc inventory, including `docs/X_COMPANION.md`. Open until written. | Documentation grant |
| R6 | Reduced. The audit file already has classification, consumers, and retention. Authority, cleanup owner, and an inbound link remain. | Documentation grant |
| R7 | Open. X-button clearance is still a screenshot measurement until a real post is checked. | Cooperator |
| R8 | Reduced to low. Subprocess timeouts bound one item. Shutdown may log an unresolved executor if a frame outlasts 20 seconds. | Acceptance record |
| R9 | Open and outside this whole. `app.js` stays a monolith. | A future planning whole |
| R10 | Open. Recommendation recorded. | Cooperator |

## AP protocol friction observed

- The selected delivery route is a human ferry. Measured: the grant names manual copy-paste, and the Cooperator then directed this file to be written so he can send the file. Effect: one ferry remains. Smallest correction is none in this exchange; the route was explicitly selected. This is not an AP change request.
- The issued prompt says `docs/UX_AUDIT.md` has no declared lifecycle. The file's Status block already declares classification, consumers, and retention. Measured at lines 3–11 of that file. Effect: the documentation grant completes the missing RF-14 fields instead of replacing a blank lifecycle. Smallest correction is that grant, not a prompt repair.

## Test baseline evidence actually used

- `./.ap/ap doctor`: PASS.
- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`: PASS.
- Glob of `tests/*.test.js`: 34 files. The issued 593 pass / 0 fail / 5 skipped result was not re-run.
- No `./.ap/ap exec --operation test-focus` invocation. No `node --test` invocation.
- NUC helper: `status` and `check --release cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738` both exited 2, `SSH target is required`, with no host contact.

## E2 test evidence

The E2 claims above were closed by reading the cited tests and the cited source. They were not closed by a fresh execution. The E3 rows are inputs to the audit, not results.

## Resolved Execution Issues / Near-Misses

The NUC helper exited 2 because this shell had no `KRONIKA_NUC_SSH_TARGET`. The Cooperator's interactive shell has the unprefixed name set, and a later message offered three unprefixed exports whose identity value was a public-key line. This session did not export those values, did not pass them to `ssh -i`, did not source the operator env file, and does not record them. Planning used the Orchestrator's same-day status and check. Residual risk: the deployment grant must re-check in a shell that already has the three canonical names, with the identity set to a private-key path.

## Pre-Existing Failure Classification

Not re-executed in this exchange. Inherited from the issued grant as environment-caused macOS failures, outside this whole, and not to be fixed here:

- `test_nuc_hardening_rollback.py` (38)
- `test_operator_network_scripts.py` (4)
- `test_uvicorn_runtime.py` (4)
- `tests/unit/test_server_runtime.py` (4)
- `test_development_runtime.py` (2)
- `test_kronika_direct_reader_routing.py` (2, `/private/var` symlink)
- `test_kronika_identity_dual_read.py` (1, same symlink)
- `test_youtube_fake_demo.py` (1)
- one collection error in `test_production_health.py`

## One smallest next step

Issue the fresh independent E3 audit prompt for candidate `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`, using the package in this report. Do not deploy. Do not start the documentation grant before that audit returns.

```text
Orchestration critique:
MEASURED: the issued prompt says docs/UX_AUDIT.md has no declared lifecycle; the file's Status block already names classification, consumers, and retention (lines 3–11). Effect: the promotion gap is authority, cleanup owner, and an inbound link. Smallest correction: the documentation grant adds those fields and does not replace the existing Status block.
LEAD: none
```
