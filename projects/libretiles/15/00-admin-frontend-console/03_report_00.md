# AFC Slice 2 — Frontend Replay Engine and Playback Controls

Build a staff-only replay console using the existing Django replay APIs. Keep replay data and playback state local to the admin interface; reuse existing tile styling without mounting the live-game board or changing player routes.

## D1 — Route Architecture and Staff Access Gate

**Routes**

- `/admin`: games list.
- `/admin/replay/[id]`: replay studio.
- `/admin/login?next=…`: admin sign-in with return navigation.
- `/admin/playground` and `/admin/analytics`: protected availability placeholders supporting the requested navigation links; no playground or analytics functionality.

`admin/layout.tsx` supplies an admin shell through `AdminAccessGate`, with navigation to Games, Playground, Analytics, and `/play`. Wrap URL-dependent client content in Suspense. The replay client reads its identifier with `useParams<{ id: string }>()`, consistent with the installed Next.js documentation.

**Authentication**

The current sign-in form lives at `/`, always navigates to `/play`, and has no callback support. Add an admin-only sign-in page to preserve player authentication behavior.

- Wait for client mount and Zustand persistence hydration before deciding that authentication is absent.
- Verify the current token using `api.me(token)`. There is no stored profile to trust.
- Mount protected page content only after a fresh response contains `is_staff === true`. Missing `is_staff` also denies access.
- Recheck on token or admin pathname changes. Associate each result with its request identity; ignore obsolete responses and immediately hide content when the identity changes.
- Missing authentication redirects with `router.replace` to `/admin/login?next=<encoded-current-admin-path>`.
- The login page alone bypasses the staff gate. Use existing `api.login`, `setToken`, `setRefreshToken`, and `api.me`; do not reset game state, change model preferences, or load a provider catalog.
- Accept callbacks only to `/admin`, the two named placeholder routes, or `/admin/replay/<UUID>`. Reject external URLs, protocol-relative URLs, backslashes, and login loops; default to `/admin`.
- Authenticated non-staff users see a styled “403 — Staff access required” screen with a `/play` link.
- Let the existing API client perform its single refresh/retry. An eventual 401 returns to sign-in; 403 unmounts protected content; transport/5xx failures show Retry.
- Protected pages report authorization failures to the gate so an already-mounted replay is cleared.

This is frontend access presentation. Django’s existing `IsAuthenticated` plus `IsAdminUser` remains the data authorization boundary. No server-side token transport, middleware, cookie migration, or backend permission change is proposed.

## D2 — API Client and Types

Add `is_staff?: boolean` to `UserProfile`. Preserve existing callers and request behavior.

Add these client methods:

```ts
api.admin.listGames(
  token: string,
  params?: AdminGameListParams,
): Promise<AdminGameListResponse>

api.admin.getReplay(
  token: string,
  gameId: string,
): Promise<AdminReplayPayload>
```

Use the existing private `request` helper, including `cache: "no-store"`, bearer authentication, refresh handling, and `ApiError`. Encode the game identifier and construct queries with `URLSearchParams`.

**List contract**

`AdminGameListParams` supports:

- `page`, `page_size`;
- `game_mode`: `all | vs_ai | vs_human`;
- `status`: `all | waiting | active | finished | abandoned`;
- `variant_slug`, `search`;
- `is_diagnostic`: `all | true | false`, supported by the client without adding an extra UI filter.

`AdminGameListResponse` contains exactly `count`, `page`, `total_pages`, `page_size`, and `results`.

`AdminGameSummary` mirrors `admin_serializers.py`: game identity, mode, variant, status, diagnostic flag, timestamps, move count, winner/end reason, `slots`, nullable `diagnostic`, and `diagnostic_run_count`.

Share an `AdminReplayPlayer` type between summary slots and replay players: `slot`, nullable username/model identifiers/model display name, score, and `is_ai`. Diagnostic summary contains run ID, status, assist mode, instrument, and model IDs.

**Replay contract**

| Type | Fields and important nullability |
|---|---|
| `AdminReplayPayload` | Literal `replay_schema_version: 1`; game ID, variant, mode, status, nullable winner, end reason, timestamps, tile points, alphabet, players, initial state, plies, final state, and `replay_status: "complete" \| "partial"` |
| `AdminReplayInitialState` | `initial_board: BoardCell[][] \| null`; two-element nullable rack and score tuples; nullable `starting_turn_slot`; numeric `bag_seed` |
| `AdminReplayPly` | `seq`, player slot, move kind, timestamp, placements, `words_formed: WordResult[]`, points, exchange count, nullable exchanged tiles, nullable score/rack tuples, board delta, AI metadata, nullable diagnostic ply |
| `AdminReplayFinalState` | Board grid, two rack arrays, and two scores |
| `AdminReplayBoardDelta` | Row, column, token, nullable blank assignment |

Use `Placement` and `WordResult`; retain the replay wire name `words_formed`, which differs from existing history’s `words`.

Define `AdminDiagnosticPly` from every field emitted by `_diagnostic_ply_payload`, preserving model-field nullability. Explicitly type identifiers, metrics, strings, and nullable booleans; use a recursive JSON value type for `ai_trace` and `earlier_attempt_failures`. Mirror `sanitize_ai_metadata` for optional AI metadata fields rather than reusing transient overlay types.

Validate replay ingress in the new replay helper using the installed Zod dependency: schema version, board dimensions/cell identities, tuple structure, supported move kinds, slot/coordinate bounds, and increasing sequence order. Reject malformed occupied blanks and structurally inconsistent deltas. Optional unavailable historical values remain nullable.

**Games list behavior**

- Default to page 1, page size 20, all modes/statuses/variants, empty search; preserve backend newest-created ordering.
- Provide the four requested filters. Obtain variant options through existing `api.getVariants`; retain slug text entry if that request fails.
- Search submits explicitly with Enter or Search and has a 150-character limit. Filter changes reset pagination.
- Store filters and pagination in the admin URL; use Suspense for search-parameter consumers.
- Show creation time, game ID, players, mode, variant, status, current scores, move count, diagnostic badge, and Replay action.
- Use returned pagination values, including backend page clamping. Ignore stale responses after filter changes.
- Provide loading, empty, error/Retry, and previous/next states.

## D3 — `useReplayEngine`

Implement a dependency-free controller in `admin-replay-engine.ts`, wrapped by `useReplayEngine.ts` using `useSyncExternalStore`. This permits genuine timer/state tests in the existing Node Vitest environment.

**State and interface**

- `currentPlyIndex`: count of applied plies, from 0 through N.
- `isPlaying`: initially false.
- `playbackSpeed`: `0.5 | 1 | 2`, initially 1.
- Actions: `play`, `pause`, `togglePlay`, `stepForward`, `stepBackward`, `goToPly`, `setSpeed`.
- Derived output: current frame, current move or null, total plies, boundary flags, and acting slot.

Use one self-rescheduling timeout, with a base duration of **1,000 ms per ply**: 2,000/1,000/500 ms at the supported speeds.

- Play advances after one full interval; Play at N restarts from 0.
- Reaching N pauses automatically; N=0 cannot play.
- Steps, First/Last, and scrubbing pause before changing position.
- Seeking clamps finite integers to 0..N; non-finite input is ignored.
- Changing speed while playing restarts the interval at the new duration.
- Pause, unmount, payload replacement, and document hiding cancel the pending timeout. Returning to a visible tab remains paused.
- Use generation checks to prevent obsolete callbacks from advancing a replaced or paused controller.
- Mount the studio keyed to the loaded replay instance so a newly loaded game resets playback.

The hook returns a keyboard handler attached to the focusable replay region. Space toggles playback; Left/Right step; Home/End seek. Ignore modified/repeated keystrokes and events from inputs, selects, buttons, links, or editable elements. Native range-slider keyboard behavior remains intact.

## D4 — Dual-Rack Visualizer

`DualRackVisualizer` receives players, current rack/score tuples, acting slot, tile points, and premium preference.

- Always render separate Player 0 and Player 1 panels. Stack below the large-screen breakpoint; show side by side when room permits.
- Human identity uses username, then “Player 0/1.” AI identity uses model display name, then model ID, then “CPU bot.”
- Display frame scores rather than the player record’s current/final score.
- Preserve rack order and duplicate physical tiles. Render each token using the existing `Tile`, `size="rack"`, `hoverable={false}`, and explicit replay tile points.
- Blank racks use `letter="?"` and `isBlank`; accessible labels explicitly identify blanks and zero points.
- Use existing gold tiles against black panels with `PREMIUM_PANEL_STYLE`, gold borders, and `handlePremiumSurfacePointer`. With Premium Look off, use flat dark panels and amber borders.
- A scoped wrapper removes the inherited pointer cursor from noninteractive tiles.
- `null` rack means “Rack unavailable,” with an unknown count; `[]` means an empty rack and zero count.
- Label the highlighted seat “Starting player” at index 0 and “Played this ply” after a move. Use the move’s actual `player_slot`; do not infer actors by alternating indices.

Pass a normalized points map covering every displayed token, with explicit zero for unavailable values, to prevent `Tile` falling back to another live game’s points.

## D5 — Board Reconstruction and Move Details

Create a prop-driven `ReplayBoard`. Do not mount `Board` or `Cell`: the former reads and mutates live-game state, while the latter registers drag-and-drop behavior.

Reuse `Tile`, `BOARD_SIZE`, `PREMIUM_BOARD`, `PREMIUM_LABELS`, and existing board CSS classes. Add scoped admin CSS for read-only cursors, responsive token sizing, and highlights. Read visual preferences only.

**Reconstruction**

Precompute immutable frames once per payload:

1. Frame 0 clones `initial_board` and initial rack/score tuples.
2. Frame k applies `plies[k - 1].board_delta` to the previous board.
3. Its racks and scores come directly from that ply, preserving nulls.
4. Non-placement moves retain the preceding board and have no highlighted cells.

Use structural sharing for unchanged rows; clone changed rows/cells. Seek and step-back select existing frames without reversing moves or recalculating scores. Never split multigraph tokens into characters or regenerate racks from `bag_seed`.

Preserve endgame adjustments in recorded cumulative scores. Show the difference between the final mover’s placement points and any recorded final score adjustments separately.

**Partial histories**

- When an initial board exists, reconstruct available board history; missing rack/score snapshots remain visibly unavailable.
- When it is absent, do not assume an empty board. Show an incomplete-history notice and the separately labelled `final_state` snapshot; historical board playback is disabled.
- A zero-ply replay renders its available initial state with disabled controls.
- `final_state` is the latest snapshot at retrieval, including for active games. Compare it with the reconstructed endpoint and report a discrepancy without overwriting historical frames.
- Replay is a fixed snapshot. No polling, websocket connection, move validation, or AI request occurs.

**Highlights and scoring**

Highlight exactly the current placement delta with a static gold ring plus a 250 ms glow animation. Re-entering a ply retriggers the glow; reduced motion retains only the ring. Supply row/column, token, blank status, points, and “placed this ply” in accessible cell labels.

Display stored formed words, word scores, word multipliers, and total move points. The payload lacks stored per-letter breakdowns:

- Derive an explicitly labelled explanation from word coordinates, physical tokens, tile points, and newly used premium squares.
- Blanks contribute zero; old tiles do not reactivate premiums.
- Show a detailed equation only when inputs are available and it reconciles with the stored word score.
- Otherwise retain the stored score and say the detailed calculation is unavailable.
- Identify a 50-point bingo only when seven placements and the recorded score difference agree; label other differences as recorded adjustments.

Diagnostic data remains typed and available to the studio, but raw trace rendering and analytics are outside this slice.

## D6 — Controls and Timeline

`ReplayControls` is presentational, receiving state and action callbacks from the hook.

- Buttons: First, Step Back, Play/Pause, Step Forward, Last.
- Disable backward controls at 0 and forward controls at N. At N, Play remains available as “Replay from start” when N>0.
- Use a labelled native range input, `min=0`, `max=N`, `step=1`. Pointer-down pauses; changes seek immediately and remain paused.
- Provide speed buttons with `aria-pressed` for 0.5x, 1x, and 2x.
- Display “Ply k of N,” independently of stored `seq`; show stored sequence in move details.
- Summaries distinguish initial position, placement, pass, exchange count, and give-up. Example: “Ply 14 of 28: Player 1 played PRASKO for 42 points.”
- Use visible focus rings, full accessible button names, wrapping controls, and a polite status announcement while paused. Avoid continuous live-region announcements during autoplay.

## D7 — Playwright Browser Verification

Browser MCP capability is present in this session’s tool inventory. No browser action has been taken.

The implementation grant must explicitly authorize local servers, synthetic accounts/data, temporary files, browser access, and verification artifacts. Use a disposable verification tree under `/tmp/libretiles-afc-slice2-verification`, containing the candidate code and assets, with existing dependency directories linked in. Exclude secret env files and existing databases.

Within that isolated tree:

1. Supply an ephemeral Django secret and explicit local settings; migrate its disposable SQLite database.
2. Seed synthetic staff/non-staff users and deterministic replay fixtures using a temporary fixture script. Include complete placement/exchange/pass/give-up histories, blanks/multigraphs, endgame adjustments, zero plies, partial history, and a diagnostic link.
3. Run Django with `manage.py runserver 127.0.0.1:8000 --noreload` and Next with `npm run dev -- --hostname 127.0.0.1 --port 3000`. Use `http://localhost:3000` in the browser. No Redis, provider credentials, catalog synchronization, or provider calls are needed.
4. Keep browser traffic local. Use a fresh browser context; do not inspect an existing account’s tokens or browser storage.

**Acceptance workflow**

- Navigate unauthenticated to a replay URL; verify admin login and exact callback restoration after staff sign-in.
- Verify non-staff 403 and direct backend 401/403 responses. Confirm protected data is absent while role verification is pending.
- Verify list rows, all four filters, search, pagination, empty results, Retry, and stale-response handling.
- Open a replay. Check index 0, both racks, scores, board contents, and player identity.
- Exercise Play/Pause, both steps, First/Last, slider pointer/keyboard input, all speeds, final auto-pause, restart, and keyboard shortcuts.
- Check backward reconstruction, blank scoring, multigraph display, pass/exchange highlight clearing, terminal score adjustments, and partial-history messaging.
- Verify pause stability over more than one playback interval and cleanup after navigation.
- Capture accessibility snapshots and screenshots at 1440×1000 and 390×844, including highlighted placements and both rack panels. Repeat with reduced motion and Premium Look off.
- Smoke-test `/play`, `/settings`, and `/game/[id]`; verify their UI and game state remain unaffected by replay navigation.
- Record console errors and request destinations/statuses without capturing authorization headers. Replay navigation/playback must not call move, validation, websocket, or AI endpoints.

Store screenshots and snapshots under the declared temporary root. The verification Worker owns server shutdown, temporary account/database disposal, browser cleanup, and exact-root cleanup after evidence review. Report retained evidence explicitly.

## D8 — Implementation Order, Allowlist, and Evidence Tier

**Ordered implementation**

1. Add wire types, API methods, runtime replay checks, and synthetic fixtures.
2. Implement immutable reconstruction and the timer controller; validate them before UI integration.
3. Add the admin gate, callback-safe sign-in, navigation, and games list.
4. Add replay board, dual racks, details, controls, and route integration.
5. Run focused Vitest tests, frontend typecheck/lint/build, then the declared Playwright matrix.
6. Review changed paths and rollback readiness; submit implementation evidence. Git publication and deployment require their own explicit grant.

**Exact proposed frontend allowlist**

Existing files:

```text
frontend/src/lib/types.ts
frontend/src/lib/api.ts
```

New routes:

```text
frontend/src/app/admin/layout.tsx
frontend/src/app/admin/page.tsx
frontend/src/app/admin/login/page.tsx
frontend/src/app/admin/playground/page.tsx
frontend/src/app/admin/analytics/page.tsx
frontend/src/app/admin/replay/[id]/page.tsx
```

New implementation files:

```text
frontend/src/components/admin/AdminAccessGate.tsx
frontend/src/components/admin/AdminGamesList.tsx
frontend/src/components/admin/ReplayStudio.tsx
frontend/src/components/admin/ReplayBoard.tsx
frontend/src/components/admin/DualRackVisualizer.tsx
frontend/src/components/admin/ReplayControls.tsx
frontend/src/components/admin/ReplayMoveDetails.tsx
frontend/src/components/admin/admin.module.css
frontend/src/hooks/useReplayEngine.ts
frontend/src/lib/admin-access.ts
frontend/src/lib/admin-replay.ts
frontend/src/lib/admin-replay-engine.ts
```

New test files:

```text
frontend/src/lib/admin-api.test.ts
frontend/src/lib/admin-access.test.ts
frontend/src/lib/admin-replay.test.ts
frontend/src/lib/admin-replay.fixtures.ts
frontend/src/hooks/useReplayEngine.test.ts
frontend/src/components/admin/AdminGamesList.test.ts
frontend/src/components/admin/ReplayBoard.test.ts
frontend/src/components/admin/DualRackVisualizer.test.ts
frontend/src/components/admin/ReplayControls.test.ts
frontend/src/components/admin/ReplayMoveDetails.test.ts
```

No changes to backend files, dependencies/lockfiles, Zustand, shared board/tile components, global CSS, locale catalogs, or player routes.

**Tests**

- API: query encoding, exact endpoints, token transport, no-store behavior, refresh and 401/403/404 handling.
- Access: callback allowlist, missing/false staff role, and obsolete authorization responses.
- Reconstruction: every move kind; initial nonempty board; backward/random seeks; immutable input; blanks/multigraphs; null versus empty racks; terminal scoring; partial history; malformed/version-mismatched payloads.
- Controller: fake timers at all speeds; pause/resume; bounds; restart; no duplicate timers; disposal; stale callbacks; zero plies.
- Components: existing `renderToStaticMarkup` pattern for rack identities/counts, controls, accessibility attributes, highlights, and score explanations.
- Real hook lifecycle, hydration, focus, interaction, animation, and visual behavior: Playwright, rather than mocked React hooks.

Use existing Node Vitest and React server rendering; add no DOM testing dependency. Run existing API/auth, game-store, history-panel, and premium-surface regressions alongside the new tests. Build is proposed for the separately authorized implementation session only.

**Tier, defaults, and rollback**

Propose **E2**: this is reversible frontend integration across routing, API consumption, and rendering. Django’s existing authorization boundary remains unchanged. Any proposed server authorization, credential storage, or privilege change requires Orchestrator reassessment.

Defaults: English admin copy; 1-second plies; paused startup; no live refresh; navigation placeholders only for Playground/Analytics. Existing visual preferences remain readable and unchanged.

Rollback consists of reverting the frontend slice. There are no migrations or new persisted replay preferences. Production rollout and publication are outside this plan.
