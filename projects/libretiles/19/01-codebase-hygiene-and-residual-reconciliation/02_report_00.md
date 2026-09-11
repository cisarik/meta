### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 02, Worker exchange ordinal: 01
```

```text
status: BLOCKED
Phase-qualified result: implementation-BLOCKED
Result artifact or commit: not-applicable
Result evidence: repository gate matched baseline dd6460583bb9b2d7b15271c1505fe6b73e07e920 / AP pin 9c5cc44f; pre-fix ReplayControls.test.ts failed SZ/12 vs AT/4; allowlisted AT/4 edits applied then reverted; 3 consumer tests outside the allowlist failed; no commit; no push
Logical-whole closure: not-closed
Changed files and purpose: none retained — allowlisted AT/4 edits were applied, validated, then restored to baseline
Commit/push result: not-attempted (stopping condition)
Resolved Execution Issues / Near-Misses: consumer sweep found 7 additional adminReplayFixture importers; DualRackVisualizer / admin-replay tests require the SZ/blank story the table removes; working tree restored by filesystem write (git checkout/reset prohibited)
Pre-Existing Failure Classification: none
Report justification: new-mutation
```

## Repository gate

| Check | Result |
|---|---|
| HEAD | `dd6460583bb9b2d7b15271c1505fe6b73e07e920` |
| `origin/main` (local ref, no fetch) | same SHA |
| branch | `main` |
| porcelain | empty (before and after) |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |

## Pre-fix evidence

`npx vitest run src/components/admin/ReplayControls.test.ts` from `frontend/` failed:

- expected: `Ply 1 of 2: Ada played SZ for 12 points`
- actual markup ticker: `Ply 1 of 2: Ada played AT for 4 points`

## Consumer-file sweep

`rg "adminReplayFixture|admin-replay.fixtures" frontend/src --include='*.ts' --include='*.tsx'` (via workspace search):

| File | Import | Post-edit vitest |
|---|---|---|
| `frontend/src/lib/admin-replay.fixtures.ts` | definition | n/a |
| `frontend/src/components/admin/ReplayControls.test.ts` | `adminReplayFixture` | PASS after AT/4 edit |
| `frontend/src/components/admin/ReplayMoveDetails.test.ts` | `adminReplayFixture` | PASS |
| `frontend/src/components/admin/ReplayScoreBreakdown.test.ts` | `adminReplayFixture` | PASS |
| `frontend/src/components/admin/ReplayMoveInspector.test.ts` | `adminReplayFixture` | PASS |
| `frontend/src/components/admin/ReplayToolTimeline.test.ts` | `adminReplayFixture` | PASS |
| `frontend/src/lib/admin-move-inspection.test.ts` | `adminReplayFixture` | PASS |
| `frontend/src/lib/admin-replay.test.ts` | `adminReplayFixture` | FAIL (2 tests) |
| `frontend/src/components/admin/DualRackVisualizer.test.ts` | `adminReplayFixture` | FAIL (1 test) |
| `frontend/src/components/admin/ReplayBoard.test.ts` | `emptyAdminBoard` only | not a `adminReplayFixture` consumer; not run |

## Why the allowlisted fixture cannot satisfy those consumers

The table requires a blank-free AT/4 physical story. Two out-of-allowlist tests still encode the old SZ/blank story:

1. `admin-replay.test.ts:11` expects `frames[1].board[7][7] === { token: "?", blank_as: "SZ" }`. After the table, that cell is `{ token: "A", blank_as: null }`.
2. `admin-replay.test.ts:18-19` sets `board_delta[0].blank_as = null` and expects `parseAdminReplay` to throw. That mutation is only malformed when `token === "?"`. After the table, `board_delta[0]` is `{ token: "A", blank_as: null }`, so the mutation is a no-op and parse succeeds.
3. `DualRackVisualizer.test.ts:9` expects `Blank tile, zero points` from `initial_racks`. The table sets `[["A", "T"], ["B", "C"]]`.

Those test files are outside the write allowlist. The fixture cannot keep a blank/SZ physical story and also match the mandated AT/4 table.

## Exact `git diff` of the attempted (then reverted) allowlisted change

```diff
diff --git a/frontend/src/components/admin/ReplayControls.test.ts b/frontend/src/components/admin/ReplayControls.test.ts
index 326ee45..1f35152 100644
--- a/frontend/src/components/admin/ReplayControls.test.ts
+++ b/frontend/src/components/admin/ReplayControls.test.ts
@@ -6,5 +6,5 @@ import { adminReplayFixture } from "@/lib/admin-replay.fixtures";
 
 it("renders VCR controls, slider, speeds, and move ticker", () => {
   const data = adminReplayFixture(); const markup = renderToStaticMarkup(createElement(ReplayControls, { currentPlyIndex: 1, totalPlies: 2, isPlaying: false, playbackSpeed: 1, move: data.plies[0], players: data.players, onFirst() {}, onBack() {}, onToggle() {}, onForward() {}, onLast() {}, onSeek() {}, onPause() {}, onSpeed() {} }));
-  expect(markup).toContain("Replay timeline"); expect(markup).toContain("0.5x"); expect(markup).toContain("Ply 1 of 2: Ada played SZ for 12 points"); expect(markup).toContain('aria-label="Step backward"');
+  expect(markup).toContain("Replay timeline"); expect(markup).toContain("0.5x"); expect(markup).toContain("Ply 1 of 2: Ada played AT for 4 points"); expect(markup).toContain('aria-label="Step backward"');
 });
diff --git a/frontend/src/lib/admin-replay.fixtures.ts b/frontend/src/lib/admin-replay.fixtures.ts
index 839f87e..5f5aacf 100644
--- a/frontend/src/lib/admin-replay.fixtures.ts
+++ b/frontend/src/lib/admin-replay.fixtures.ts
@@ -5,20 +5,21 @@ export const emptyAdminBoard = (): BoardCell[][] => Array.from({ length: 15 }, (
 export function adminReplayFixture(): AdminReplayPayload {
   const board = emptyAdminBoard();
   const finalBoard = emptyAdminBoard();
-  finalBoard[7][7] = { token: "?", blank_as: "SZ" };
+  finalBoard[7][7] = { token: "A", blank_as: null };
+  finalBoard[7][8] = { token: "T", blank_as: null };
   return {
     replay_schema_version: 1, game_id: "123e4567-e89b-42d3-a456-426614174000", variant_slug: "english", game_mode: "vs_ai",
     status: "finished", winner_slot: 0, game_end_reason: "bag_empty", created_at: "2026-09-08T10:00:00Z", finished_at: "2026-09-08T10:10:00Z",
-    tile_points: { A: 1, SZ: 4, "?": 0 }, alphabet: ["A", "SZ", "?"],
+    tile_points: { A: 1, T: 1 }, alphabet: ["A", "T"],
     players: [
-      { slot: 0, username: "Ada", score: 12, is_ai: false, model_id: null, model_display_name: null },
+      { slot: 0, username: "Ada", score: 4, is_ai: false, model_id: null, model_display_name: null },
       { slot: 1, username: null, score: 0, is_ai: true, model_id: "bot/model", model_display_name: "Bot Model" },
     ],
-    initial_state: { initial_board: board, initial_racks: [["?", "A"], ["SZ"]], initial_scores: [0, 0], starting_turn_slot: 0, bag_seed: 12 },
+    initial_state: { initial_board: board, initial_racks: [["A", "T"], ["B", "C"]], initial_scores: [0, 0], starting_turn_slot: 0, bag_seed: 12 },
     plies: [
-      { seq: 1, player_slot: 0, kind: "place", created_at: "2026-09-08T10:01:00Z", placements: [{ row: 7, col: 7, letter: "?", blank_as: "SZ" }], words_formed: [{ word: "AT", score: 4, multiplier: 2, coords: [{ row: 7, col: 7 }, { row: 7, col: 8 }], inspection: { version: 1, physical_cells: [{ row: 7, col: 7, token: "A", blank_as: null, base_points: 1, is_new: true, premium: "DW", premium_applied: true, letter_multiplier: 1 }, { row: 7, col: 8, token: "T", blank_as: null, base_points: 1, is_new: true, premium: null, premium_applied: false, letter_multiplier: 1 }], base_points: 2, letter_bonus_points: 0, word_multiplier: 2, word_total: 4, authority: { name: "WordAuthority", valid: true, physical_tile_count: 2, route: "main", main_lexicon_id: "collins2019", two_tile_lexicon_id: null, lexicon_source: "Collins Scrabble Words (2019)" } } }], points: 4, tiles_exchanged: 0, exchanged_tiles: null, cumulative_scores: [4, 0], racks: [["A"], ["SZ"]], board_delta: [{ row: 7, col: 7, token: "?", blank_as: "SZ" }], ai_metadata: { completion_source: "provider_candidate", inspection_trace: { version: 1, attempts: [{ attempt_index: 0, provider: "openrouter", model_id: "bot/model", latency_ms: 210, provider_requests_used: 2, outcome: "done", events: [{ ordinal: 0, elapsed_ms: 100, phase: "search", tool: "validateMove", placements: [{ row: 7, col: 7, letter: "A" }, { row: 7, col: 8, letter: "T" }], words: ["AT"], valid: true, score: 4 }, { ordinal: 1, elapsed_ms: 200, phase: "finishMove", tool: "finishMove", ready: true }] }] } }, diagnostic_ply: null },
-      { seq: 2, player_slot: 1, kind: "pass", created_at: "2026-09-08T10:02:00Z", placements: [], words_formed: [], points: 0, tiles_exchanged: 0, exchanged_tiles: null, cumulative_scores: [12, 0], racks: [["A"], ["SZ"]], board_delta: [], ai_metadata: {}, diagnostic_ply: null },
+      { seq: 1, player_slot: 0, kind: "place", created_at: "2026-09-08T10:01:00Z", placements: [{ row: 7, col: 7, letter: "A" }, { row: 7, col: 8, letter: "T" }], words_formed: [{ word: "AT", score: 4, multiplier: 2, coords: [{ row: 7, col: 7 }, { row: 7, col: 8 }], inspection: { version: 1, physical_cells: [{ row: 7, col: 7, token: "A", blank_as: null, base_points: 1, is_new: true, premium: "DW", premium_applied: true, letter_multiplier: 1 }, { row: 7, col: 8, token: "T", blank_as: null, base_points: 1, is_new: true, premium: null, premium_applied: false, letter_multiplier: 1 }], base_points: 2, letter_bonus_points: 0, word_multiplier: 2, word_total: 4, authority: { name: "WordAuthority", valid: true, physical_tile_count: 2, route: "main", main_lexicon_id: "collins2019", two_tile_lexicon_id: null, lexicon_source: "Collins Scrabble Words (2019)" } } }], points: 4, tiles_exchanged: 0, exchanged_tiles: null, cumulative_scores: [4, 0], racks: [[], ["B", "C"]], board_delta: [{ row: 7, col: 7, token: "A", blank_as: null }, { row: 7, col: 8, token: "T", blank_as: null }], ai_metadata: { completion_source: "provider_candidate", inspection_trace: { version: 1, attempts: [{ attempt_index: 0, provider: "openrouter", model_id: "bot/model", latency_ms: 210, provider_requests_used: 2, outcome: "done", events: [{ ordinal: 0, elapsed_ms: 100, phase: "search", tool: "validateMove", placements: [{ row: 7, col: 7, letter: "A" }, { row: 7, col: 8, letter: "T" }], words: ["AT"], valid: true, score: 4 }, { ordinal: 1, elapsed_ms: 200, phase: "finishMove", tool: "finishMove", ready: true }] }] } }, diagnostic_ply: null },
+      { seq: 2, player_slot: 1, kind: "pass", created_at: "2026-09-08T10:02:00Z", placements: [], words_formed: [], points: 0, tiles_exchanged: 0, exchanged_tiles: null, cumulative_scores: [4, 0], racks: [[], ["B", "C"]], board_delta: [], ai_metadata: {}, diagnostic_ply: null },
     ],
-    final_state: { board: finalBoard, racks: [["A"], ["SZ"]], scores: [12, 0] }, replay_status: "complete",
+    final_state: { board: finalBoard, racks: [[], ["B", "C"]], scores: [4, 0] }, replay_status: "complete",
   };
 }
```

`git diff --stat` of that attempted mutation showed only the two allowlisted files. `ReplayControls.tsx` was not in the diff. After the stopping condition, both files were restored; porcelain is empty again at the baseline SHA.

## Validation table

| Gate | Outcome |
|---|---|
| `ReplayControls.test.ts` after AT/4 edit | PASS |
| other `adminReplayFixture` consumers | 12 passed / 3 failed (see above) |
| `npm run typecheck` | not run (stopped) |
| `npm run lint` | not run (stopped) |
| `npm run build` | not run (stopped) |
| commit / non-force push / `ls-remote` | not attempted |

## Cleanup

`/tmp/opencode/hyg-s2/` created then removed. Path absent after cleanup.

## Deviations

- Did not commit or push.
- Restored the two allowlisted files by rewriting baseline contents (git checkout/reset/clean/stash are prohibited).
- Did not run typecheck/lint/build after consumer failure.

## Authority expiry

This Worker exchange's implementation authority expires at this terminal report. No further mutation, commit, or push is authorized.

Context pressure: moderate.