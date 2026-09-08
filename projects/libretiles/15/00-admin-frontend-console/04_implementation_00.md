You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AFC-SLICE-2-IMPL — implement Frontend Replay Engine & Playback Controls (/admin games list, /admin/replay/[id] studio with VCR controls, dual-rack visualizer, and placed-tile highlights), write tests, land one commit, push, and read back.
Phase: implementation
Exact baseline: 1a29262795e7e2a79bdf9e70239f180656e8d234
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: reversible frontend integration across routing, API consumption, playback controller, and UI rendering backed by Vitest unit tests, typecheck, lint, and browser verification. Zero backend or schema mutation.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Implementing the frontend replay studio requires ensuring strict isolation from standard player routes (`/game/[id]`, `/play`), robust state reconstruction across plies 0..N, tactile gold/black dual-rack visualization, and smooth VCR playback controls without regressions.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:423-453 coordinate consistency and Worker Exchange Identity
AP.md:2453-2454      the CLOSED report-justification enum: `new-mutation`.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md                 the project brief.
/home/agile/Projects/libretiles/frontend/AGENTS.md        Next.js rules.
/home/agile/Projects/libretiles/frontend/src/lib/types.ts
/home/agile/Projects/libretiles/frontend/src/lib/api.ts
/home/agile/Projects/libretiles/frontend/src/components/board/Board.tsx
/home/agile/Projects/libretiles/frontend/src/components/tiles/Tile.tsx
/home/agile/Projects/libretiles/frontend/src/lib/premiumSurface.ts
/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/03_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 1a29262795e7e2a79bdf9e70239f180656e8d234
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these files:

Existing files:
1. `frontend/src/lib/types.ts`
2. `frontend/src/lib/api.ts`

New admin routes:
3. `frontend/src/app/admin/layout.tsx`
4. `frontend/src/app/admin/page.tsx`
5. `frontend/src/app/admin/login/page.tsx`
6. `frontend/src/app/admin/playground/page.tsx`
7. `frontend/src/app/admin/analytics/page.tsx`
8. `frontend/src/app/admin/replay/[id]/page.tsx`

New admin components & helpers:
9. `frontend/src/components/admin/AdminAccessGate.tsx`
10. `frontend/src/components/admin/AdminGamesList.tsx`
11. `frontend/src/components/admin/ReplayStudio.tsx`
12. `frontend/src/components/admin/ReplayBoard.tsx`
13. `frontend/src/components/admin/DualRackVisualizer.tsx`
14. `frontend/src/components/admin/ReplayControls.tsx`
15. `frontend/src/components/admin/ReplayMoveDetails.tsx`
16. `frontend/src/components/admin/admin.module.css`
17. `frontend/src/hooks/useReplayEngine.ts`
18. `frontend/src/lib/admin-access.ts`
19. `frontend/src/lib/admin-replay.ts`
20. `frontend/src/lib/admin-replay-engine.ts`

New test files:
21. `frontend/src/lib/admin-api.test.ts`
22. `frontend/src/lib/admin-access.test.ts`
23. `frontend/src/lib/admin-replay.test.ts`
24. `frontend/src/lib/admin-replay.fixtures.ts`
25. `frontend/src/hooks/useReplayEngine.test.ts`
26. `frontend/src/components/admin/AdminGamesList.test.ts`
27. `frontend/src/components/admin/ReplayBoard.test.ts`
28. `frontend/src/components/admin/DualRackVisualizer.test.ts`
29. `frontend/src/components/admin/ReplayControls.test.ts`
30. `frontend/src/components/admin/ReplayMoveDetails.test.ts`

In addition, you have WRITE AUTHORITY to output your complete terminal report file to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/04_report_00.md`

⛔ Any mutation to any file outside this allowlist is strictly unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `03_report_00.md`:

### 3.1 Types & API Client (`types.ts`, `api.ts`, `admin-access.ts`)

1. In `frontend/src/lib/types.ts`:
   - Add `is_staff?: boolean;` to `UserProfile`.
   - Add `AdminGameSummary`, `AdminGameListResponse`, `AdminGameListParams`.
   - Add `AdminReplayPayload`, `AdminReplayInitialState`, `AdminReplayPly`, `AdminReplayFinalState`, `AdminReplayPlayer`.
2. In `frontend/src/lib/api.ts`:
   - Add `api.admin.listGames(token, params)` calling `/api/admin/games/`.
   - Add `api.admin.getReplay(token, gameId)` calling `/api/admin/games/${gameId}/replay/`.
3. In `frontend/src/lib/admin-access.ts`:
   - Callback URL validation: only allow relative admin paths (`/admin`, `/admin/replay/...`, `/admin/playground`, `/admin/analytics`). Reject external URLs, backslashes, login loops.

### 3.2 Staff Access Gate & Route Layout (`AdminAccessGate.tsx`, `layout.tsx`, `login/page.tsx`)

1. `frontend/src/app/admin/layout.tsx`:
   - Provides admin navigation bar with links:
     * `[Games List]` (`/admin`)
     * `[Replay Studio]`
     * `[Playground (Preview)]` (`/admin/playground`)
     * `[Analytics (Preview)]` (`/admin/analytics`)
     * `[← Back to Game]` (`/play`)
   - Uses `AdminAccessGate` to verify staff authentication.
2. `AdminAccessGate`:
   - Checks `api.me(token)`.
   - If unauthenticated: redirects via `router.replace` to `/admin/login?next=...`.
   - If authenticated but `is_staff !== true`: displays styled 403 Access Denied screen with link back to `/play`.
   - If staff: renders children.
3. `frontend/src/app/admin/login/page.tsx`:
   - Dedicated admin sign-in form preserving return navigation callback.
4. Navigation placeholders for `/admin/playground/page.tsx` and `/admin/analytics/page.tsx`:
   - Friendly status notice indicating upcoming feature in Meta whole 15 Slices 4 and 5.

### 3.3 Games List Dashboard (`admin/page.tsx`, `AdminGamesList.tsx`)

1. Renders table/cards of recent games:
   - Creation time, Game ID (shortened hex prefix), Mode, Variant, Status badge, Players with scores, Move count, Diagnostic badge, and `[View Replay]` button.
2. Filter bar:
   - Game Mode (`all`, `vs_ai`, `vs_human`).
   - Variant picker.
   - Status (`all`, `active`, `finished`, `abandoned`).
   - Search input (by game ID prefix or player username) with Enter/Submit button.
3. Pagination controls (Previous / Next / Page N of Total).
4. Loading, Empty, and Error with Retry states.

### 3.4 Replay State Engine (`admin-replay-engine.ts`, `useReplayEngine.ts`)

1. `admin-replay-engine.ts`:
   - Pure state controller with `currentPlyIndex` (0..totalPlies), `isPlaying`, `playbackSpeed` (0.5, 1, 2).
   - Actions: `play`, `pause`, `togglePlay`, `stepForward`, `stepBackward`, `goToPly(index)`, `setSpeed(speed)`.
   - 1000ms base interval per ply (2000ms at 0.5x, 500ms at 2x).
   - Auto-pause when reaching the last ply (N).
2. `useReplayEngine.ts`:
   - React hook wrapping the controller.
   - Keyboard shortcuts: `Space` (play/pause), `ArrowLeft` (step back), `ArrowRight` (step forward), `Home` (start), `End` (last ply).

### 3.5 Dual-Rack Visualizer (`DualRackVisualizer.tsx`)

1. Renders both Player 0 and Player 1 racks simultaneously:
   - Separate panels for Player 0 and Player 1.
   - Highlights the acting player for the current ply ("Starting Player" at ply 0, "Played this ply" after a move).
   - Displays player name/model, cumulative score, and rack tile count.
   - Renders individual tiles using the existing `Tile` component with `size="rack"` and gold/black styling from `premiumSurface.ts`.
   - Shows blank tiles with `?` and zero points.

### 3.6 Replay Board & Move Details (`ReplayBoard.tsx`, `ReplayMoveDetails.tsx`)

1. `ReplayBoard.tsx`:
   - Renders 15x15 Scrabble grid using `Tile` components and board premiums (`BOARD_SIZE`, `PREMIUM_BOARD`, `PREMIUM_LABELS`).
   - Reconstructs board state at `currentPlyIndex` from precomputed frame array.
   - Highlights tiles placed in the *current active ply* with a distinct golden ring and subtle glow.
2. `ReplayMoveDetails.tsx`:
   - Move summary: kind (`place`, `exchange`, `pass`, `give_up`), player, points gained.
   - Words formed: word text, score breakdown, word multiplier, coordinates.
   - For exchange moves: shows exchanged tile count and letters if recorded.

### 3.7 VCR Controls & Scrubber (`ReplayControls.tsx`)

1. VCR Buttons: First (`<<`), Step Back (`<`), Play/Pause, Step Forward (`>`), Last (`>>`).
2. Interactive native range slider (`<input type="range" min={0} max={totalPlies} value={currentPlyIndex} />`) for smooth scrubbing.
3. Speed selector pills: `0.5x`, `1x`, `2x`.
4. Informative turn ticker (e.g. "Ply 14 of 28: Player 1 played 'PRASKO' for 42 pts").

## 4. Verification Commands

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-api.test.ts src/lib/admin-access.test.ts src/lib/admin-replay.test.ts src/hooks/useReplayEngine.test.ts
```

Backend check (confirming zero regression):
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_admin_replay_api.py -v
```

⛔ Do NOT run package installers (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add frontend/src/lib/types.ts frontend/src/lib/api.ts frontend/src/app/admin/ frontend/src/components/admin/ frontend/src/hooks/useReplayEngine.ts frontend/src/lib/admin-access.ts frontend/src/lib/admin-replay.ts frontend/src/lib/admin-replay-engine.ts frontend/src/lib/admin-*.test.ts frontend/src/lib/admin-replay.fixtures.ts frontend/src/hooks/useReplayEngine.test.ts frontend/src/components/admin/*.test.ts
git diff --staged --stat
```

Commit with message:
```bash
git commit -m "feat(admin): implement frontend replay engine, dual racks, and VCR playback controls"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "1a29262795e7e2a79bdf9e70239f180656e8d234"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Any test or gate failure cannot be resolved within the allowlisted files.
- Pre-push verification reveals that `origin/main` has diverged from the baseline.

## 7. Report Contract

IMPORTANT: Write your complete terminal report directly to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/04_report_00.md`

The report content must begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 04, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `1a29262795e7e2a79bdf9e70239f180656e8d234`
- End commit: `<exact SHA>`
- Changed files and purpose
- Tests and validation summaries (verbatim tool outputs)
- Commit and push result (SHA and readback check)
- Deviations, risks, or missing evidence: none | <details>
- One smallest next step
- Report justification: `new-mutation`
- Explicit authority-expiry statement

Plus the two analytical fields:
```text
Orchestration critique: none | <findings> (labelled MEASURED and LEAD)
Enumeration widened: none | <surfaces not reached>
```

In your final chat message, emit a concise 3-line notification confirming that the report has been written to disk at `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/04_report_00.md`.
