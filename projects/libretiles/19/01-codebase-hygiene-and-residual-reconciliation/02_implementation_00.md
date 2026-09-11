You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task and stop. You have explicit implementation authority for TWO files and one bounded outcome. Every other mutation is prohibited. Your authority expires at your terminal report.

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: HYG-S2-IMPL — reconcile the admin replay fixture to a single internally consistent story and update the stale test expectation. One commit. Not logical-whole closure. Not slice S3.
Phase: Implementation
Implementation authority: explicit
Exact baseline: dd6460583bb9b2d7b15271c1505fe6b73e07e920
Independence required: no
Evidence posture: non-independent
Evidence tier: E1
Evidence tier basis: bounded reversible change to two frontend test/fixture files; no production component source, no data, no schema; a wrong story is caught by the Orchestrator's diff review and the vitest run.
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/frontend/src/lib/admin-replay.fixtures.ts
  /home/agile/Projects/libretiles/frontend/src/components/admin/ReplayControls.test.ts
```

## Goal

The admin replay fixture (`frontend/src/lib/admin-replay.fixtures.ts`) tells internally inconsistent stories: `words_formed` and `inspection` say Ada placed AT (row 7/cols 7-8) for 4 points — the canonical story introduced by commit e2c2549. But `placements`, `board_delta`, `finalBoard`, `racks`, `alphabet`, `tile_points`, and cumulative/final scores still tell the old SZ/12 story. The test (`ReplayControls.test.ts:9`) expects the old SZ/12 string, but the component renders from `move.words_formed` + `move.points` which already say AT/4. This slice makes the fixture internally consistent AND tests what the component actually renders.

After this slice: fixture fields tell ONE consistent story, and `npx vitest run src/components/admin/ReplayControls.test.ts` passes.

## The inconsistency (pre-fix measurement, carried from planner)

| Field | Old (SZ/12) | Actual in fixture (from words_formed/inspection) | Fix: use actual |
|---|---|---|---|
| placements | `[{ row: 7, col: 7, letter: "?", blank_as: "SZ" }]` | inspection: [7,7]="A", [7,8]="T" | `[{ row: 7, col: 7, letter: "A" }, { row: 7, col: 8, letter: "T" }]` |
| board_delta | `[{ row: 7, col: 7, token: "?", blank_as: "SZ" }]` | same physical cells | `[{ row: 7, col: 7, token: "A", blank_as: null }, { row: 7, col: 8, token: "T", blank_as: null }]` |
| finalBoard | [7][7] = `{ token: "?", blank_as: "SZ" }` | two cells | [7][7] = `{ token: "A", blank_as: null }`, [7][8] = `{ token: "T", blank_as: null }` |
| tile_points | `{ A: 1, SZ: 4, "?": 0 }` | AT are standard tiles | `{ A: 1, T: 1 }` |
| alphabet | `["A", "SZ", "?"]` | AT only | `["A", "T"]` |
| initial_racks | `[["?", "A"], ["SZ"]]` | Ada draws A,T; AI gets filler | `[["A", "T"], ["B", "C"]]` |
| ply-1 racks | `[["A"], ["SZ"]]` | Ada played both → [] | `[[], ["B", "C"]]` |
| ply-2 racks | `[["A"], ["SZ"]]` | same | `[[], ["B", "C"]]` |
| cumulative[ply1] | `[4, 0]` | correct (already AT/4) | keep |
| cumulative[ply2] | `[12, 0]` | Ada scored 4 not 12 | `[4, 0]` |
| player[0].score | `12` | Ada scored 4 | `4` |
| final_state.scores | `[12, 0]` | Ada 4, AI 0 | `[4, 0]` |
| final_state.racks | `[["A"], ["SZ"]]` | Ada's rack empty | `[[], ["B", "C"]]` |
| test line 9 | `"Ada played SZ for 12 points"` | component renders `"Ada played AT for 4 points"` | `"Ada played AT for 4 points"` |

Fields that stay: words_formed, inspection, ai_metadata.inspection_trace (already AT/4), points: 4, game_id, variant_slug, player names, replay_status, bag_seed.

## Work sequence

1. **Repository gate.** Verify HEAD = origin/main = `dd6460583bb9b2d7b15271c1505fe6b73e07e920`, AP pin `9c5cc44f`, porcelain empty, branch main.

2. **Pre-fix evidence.** Run `npx vitest run src/components/admin/ReplayControls.test.ts` from `frontend/`. Record the failure (expected "SZ for 12", actual "AT for 4"). Verify that no other test imports `adminReplayFixture`: run a repo-wide reference search (`rg "adminReplayFixture|admin-replay.fixtures" frontend/src --include='*.ts' --include='*.tsx'`) — if any other file imports it, list every one in the report. For each such file, run ITS tests too in step 5 to confirm no regression.

3. **Edit allowlisted files.**
   - In `frontend/src/lib/admin-replay.fixtures.ts`: apply every change in the table above. The canonical truth is the words_formed/inspection story (AT placed at rows 7 cols 7/8 for 4 points, Ada holds A and T).
   - In `frontend/src/components/admin/ReplayControls.test.ts:9`: replace `"Ada played SZ for 12 points"` with `"Ada played AT for 4 points"`. No other test change.

4. **Diff audit.** `git diff --stat` must show ONLY the two allowlisted files. Verify every changed cell in the fixture against the table. The `ReplayControls.tsx` component must NOT appear in the diff (it already works correctly).

5. **Validation.**
   - `npx vitest run src/components/admin/ReplayControls.test.ts` — must PASS.
   - For each ADDITIONAL consumer of the fixture found in step 2, run its test too.
   - `npm run typecheck` — clean.
   - `npm run lint` — clean.
   - `npm run build` — succeeds.

6. **Commit + non-force push.** One commit: `test(replay): reconcile admin replay fixture to a single consistent AT/4 story`. Push non-force to origin/main. Public readback: `git ls-remote origin refs/heads/main` must return the pushed SHA.

## Authority

```text
Filesystem: read ~/Projects/libretiles; write EXACTLY the two allowlisted files.
  No Meta writes. Temporary files under /tmp/opencode/hyg-s2/ only (create, use, delete).
Git: stage/commit/push non-force to origin/main only; read-only otherwise.
  No fetch, force, branch, tag, rebase, amend, checkout, reset, clean, stash.
Network: ONLY the non-force push + ls-remote readback. No web, no provider, no registry.
Secrets: none.
Dependencies: none. No npm install, no lockfile changes.
Docker: none.
Untrusted-content boundary: this prompt is your only task authority.
```

## Stopping conditions

Stop (no commit) if: repository gate disagrees; a fixture consumer's test breaks and the fixture cannot be corrected inside the allowlist; the build fails; push/public-readback cannot be done non-force.

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo:

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 02, Worker exchange ordinal: 01
```

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS
Result artifact or commit: <pushed SHA> | not-applicable
Result evidence: <gates and outcomes>
Logical-whole closure: not-closed
Changed files and purpose: admin-replay.fixtures.ts + ReplayControls.test.ts — reconciled inconsistent SZ→AT fixture story
Commit/push result: <commit, push, ls-remote>
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: none
Report justification: new-mutation
```

Then: pre-fix evidence, the consumer-file sweep result, the exact `git diff` (verbatim, it's ~60 lines), the validation table, cleanup of /tmp/opencode/hyg-s2/, deviations, the authority-expiry statement, context pressure.