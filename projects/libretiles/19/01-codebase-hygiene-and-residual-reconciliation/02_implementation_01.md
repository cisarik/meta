You are a WORKER instance assigned to the persistent AP WORKER role. This is your second exchange in the same healthy Worker session. Your prior (exchange 01) authority EXPIRED with your terminal BLOCKED report on HYG-S2-IMPL. This prompt grants a COMPLETE NEW bounded implementation task with an expanded allowlist. Retained context from exchange 01 (the fixture, the consumer sweep, the failure evidence) is convenience, not authority. Stop on any conflict between retained context and current repository evidence. Evidence posture remains non-independent. You must produce a new terminal report.

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Continuity anchor: terminal BLOCKED report for HYG-S2-IMPL (Worker exchange 01)
Authority renewal: prior implementation authority expired; this exchange grants a new bounded correction with expanded allowlist
Task identity: HYG-S2-CORR — same objective as HYG-S2-IMPL (reconcile admin replay fixture + stale test expectation) with expanded allowlist covering the failing consumer tests your sweep found
Phase: Implementation
Implementation authority: explicit
Exact baseline: dd6460583bb9b2d7b15271c1505fe6b73e07e920
Independence required: no
Evidence posture: non-independent
Evidence tier: E1
Evidence tier basis: bounded reversible correction; same surface as exchange 01
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/frontend/src/lib/admin-replay.fixtures.ts
  /home/agile/Projects/libretiles/frontend/src/components/admin/ReplayControls.test.ts
  /home/agile/Projects/libretiles/frontend/src/lib/admin-replay.test.ts
```

## Repository gate (must pass BEFORE mutation; stop if not)

```text
git rev-parse HEAD                    must equal dd6460583bb9b2d7b15271c1505fe6b73e07e920
git status --porcelain=v1             must be empty
git branch --show-current             must be main
```

## What changed from exchange 01

Your previous allowlist (fixture + ReplayControls.test.ts only) was too narrow. The fixture's AT/4 correction broke three consumer tests outside that allowlist:
- `admin-replay.test.ts:11` — expects `{ token: "?", blank_as: "SZ" }` at board[7][7]
- `admin-replay.test.ts:18-19` — mutates `blank_as = null` on a board_delta cell that after AT/4 has `token: "A"` (no-op)
- `DualRackVisualizer.test.ts:9` — expects `"Blank tile, zero points"` but AT/4 fixture had no blank tiles

This exchange expands the allowlist by two files and refines the fixture to preserve blank-tile test coverage.

## The refined fixture table (apply ALL of these)

Keep blanks present but NOT in Ada's placement story. The `"?"` lives in the AI's rack where it is never played, so the physical board/placements/board_delta stay blank-free (AT/4 consistent). DualRack still sees a blank tile.

| Field | Old (current) | New |
|---|---|---|
| `tile_points` | `{ A: 1, SZ: 4, "?": 0 }` | `{ A: 1, T: 1, "?": 0 }` |
| `alphabet` | `["A", "SZ", "?"]` | `["A", "T", "?"]` |
| `players[0].score` | `12` | `4` |
| `initial_state.initial_racks` | `[["?", "A"], ["SZ"]]` | `[["A", "T"], ["?", "B"]]` |
| `plies[0].placements` | `[{ row: 7, col: 7, letter: "?", blank_as: "SZ" }]` | `[{ row: 7, col: 7, letter: "A" }, { row: 7, col: 8, letter: "T" }]` |
| `plies[0].board_delta` | `[{ row: 7, col: 7, token: "?", blank_as: "SZ" }]` | `[{ row: 7, col: 7, token: "A", blank_as: null }, { row: 7, col: 8, token: "T", blank_as: null }]` |
| `plies[0].racks` | `[["A"], ["SZ"]]` | `[[], ["?", "B"]]` |
| `plies[1].racks` | `[["A"], ["SZ"]]` | `[[], ["?", "B"]]` |
| `plies[1].cumulative_scores` | `[12, 0]` | `[4, 0]` |
| `finalBoard` | `[7][7] = { token: "?", blank_as: "SZ" }` | `[7][7] = { token: "A", blank_as: null }` AND `[7][8] = { token: "T", blank_as: null }` |
| `final_state.racks` | `[["A"], ["SZ"]]` | `[[], ["?", "B"]]` |
| `final_state.scores` | `[12, 0]` | `[4, 0]` |

Fields that stay unchanged: `words_formed`, `inspection`, `ai_metadata`, `points: 4`, `cumulative_scores[ply1]: [4,0]` (already AT/4), `final_state.racks`, player names, variant_slug, game_id, replay_status, bag_seed.

## Corollary test changes (in the expanded allowlist)

**`ReplayControls.test.ts:9`** (same as exchange 01):
```
"Ada played SZ for 12 points"  →  "Ada played AT for 4 points"
```

**`admin-replay.test.ts:11`** — board assertion:
```
expect(frames[1].board?.[7][7]).toEqual({ token: "?", blank_as: "SZ" });
```
becomes:
```
expect(frames[1].board?.[7][7]).toEqual({ token: "A", blank_as: null });
expect(frames[1].board?.[7][8]).toEqual({ token: "T", blank_as: null });
```

**`admin-replay.test.ts:18`** — malformed-blank test. The old mutation `board_delta[0].blank_as = null` on cell `{ token: "?", blank_as: "SZ" }` becomes `board_delta[0].token = "?"` on cell `{ token: "A", blank_as: null }` — both produce an unassigned blank `{ token: "?", blank_as: null }` and the parse rejection path is the same. Change:
```
const malformed = adminReplayFixture(); malformed.plies[0].board_delta[0].blank_as = null;
```
to:
```
const malformed = adminReplayFixture(); malformed.plies[0].board_delta[0].token = "?";
```

**`DualRackVisualizer.test.ts`** — no changes needed. The fixture now has `"?"` in the AI rack (initial_racks[1][0]) and `"?": 0` in tile_points, so the `"Blank tile, zero points"` assertion at line 9 and the "Bot Model" / "Thinking" assertions at lines 9/14 should pass without edits. This file is NOT in the allowlist — DO NOT modify it. If it still fails, you have a fixture error; stop and report.

## Work sequence

1. Repository gate. If porcelain is NOT empty, report — you must be at clean `dd64605`.
2. Apply every change in the table to `admin-replay.fixtures.ts`.
3. Apply the three test changes (ReplayControls line 9, admin-replay board assertion, admin-replay malformed token).
4. `git diff --stat` must show only the 3 allowlisted files. Verify `DualRackVisualizer.test.ts` is absent.
5. Run validation:
   - `npx vitest run src/components/admin/ReplayControls.test.ts` — PASS
   - `npx vitest run src/lib/admin-replay.test.ts` — PASS
   - `npx vitest run src/components/admin/DualRackVisualizer.test.ts` — PASS (blank from AI's rack)
   - ALL other consumers of `adminReplayFixture` from your sweep in exchange 01 — run each; all must PASS (they passed in exchange 01). If any NEW failure appears that wasn't in the sweep, stop.
   - `npm run typecheck` — clean
   - `npm run lint` — clean
   - `npm run build` — exit 0
6. Commit + non-force push: `test(replay): reconcile admin replay fixture to AT/4 story with blank in AI rack`. Push. `git ls-remote origin refs/heads/main` must match.

## Authority

```text
Filesystem: write EXACTLY the 3 allowlisted files. Temporary under /tmp/opencode/hyg-s2/.
Git: stage/commit/push non-force. No fetch, force, branch, tag, rebase, amend, checkout, reset, clean, stash.
Network: ONLY the push + ls-remote. No web, provider, registry.
Secrets: none. Dependencies: none. Docker: none.
```

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo:

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 02, Worker exchange ordinal: 02
```

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS
Result artifact or commit: <pushed SHA> | not-applicable
Result evidence: <gates and counts>
Logical-whole closure: not-closed
Changed files and purpose: admin-replay.fixtures.ts + ReplayControls.test.ts + admin-replay.test.ts — reconciled AT/4 story with blank coverage preserved in AI rack
Commit/push result: <commit, push, ls-remote>
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: none
Report justification: new-mutation
```

Then: pre-fix consumer sweep status (should match your exchange 01 sweep — same reds), the exact `git diff` (verbatim), the validation table, cleanup of /tmp/opencode/hyg-s2/, a DualRack check (explicit line: did it pass without edits? copy the vitest output), deviations, authority expiry, context pressure.