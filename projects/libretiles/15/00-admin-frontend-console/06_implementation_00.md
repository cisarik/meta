You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AFC-SLICE-3-IMPL — implement Deep Move Inspector & Recorded AI Telemetry (detailed mathematical score equations, cross-words, bingo badge, AI tool-call execution viewer, CompletionSourceBadges, provider telemetry chips, and engine/search diagnostics). Land one commit, push, and read back.
Phase: implementation
Exact baseline: 1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: reversible frontend inspector components and backend score/telemetry projection helpers backed by unit tests, typecheck, and lint. No database migration, no external network, no live provider call.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Implementing the Deep Move Inspector requires cleanly capturing letter-by-letter score breakdowns and WordAuthority certification in the backend scoring path, collecting tool-call proposals and completion sources in the frontend AI pipeline without breaking live gameplay, and rendering a tabbed, responsive inspector drawer in the Replay Studio.

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
/home/agile/Projects/libretiles/backend/gamecore/scoring.py
/home/agile/Projects/libretiles/backend/game/services.py
/home/agile/Projects/libretiles/backend/game/replay.py
/home/agile/Projects/libretiles/frontend/src/components/admin/ReplayStudio.tsx
/home/agile/Projects/libretiles/frontend/src/components/admin/ReplayMoveDetails.tsx
/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/05_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these files:

Backend:
1. `backend/gamecore/types.py`
2. `backend/gamecore/scoring.py`
3. `backend/game/services.py`
4. `backend/game/serializers.py`
5. `backend/game/replay.py`
6. `backend/game/inspection.py`
7. `backend/tests/test_move_inspection.py`
8. `backend/tests/test_admin_replay_api.py`

Frontend:
9. `frontend/src/lib/types.ts`
10. `frontend/src/lib/admin-replay.ts`
11. `frontend/src/lib/admin-replay.test.ts`
12. `frontend/src/lib/admin-replay.fixtures.ts`
13. `frontend/src/lib/admin-move-inspection.ts`
14. `frontend/src/lib/admin-move-inspection.test.ts`
15. `frontend/src/lib/ai-inspection-trace.ts`
16. `frontend/src/lib/ai-inspection-trace.test.ts`
17. `frontend/src/lib/ai-fallback.ts`
18. `frontend/src/lib/ai-fallback.test.ts`
19. `frontend/src/lib/ai-move-stream.ts`
20. `frontend/src/lib/ai-move-stream.test.ts`
21. `frontend/src/app/api/ai/move/route.ts`
22. `frontend/src/app/api/ai/move/route.test.ts`
23. `frontend/src/components/admin/ReplayStudio.tsx`
24. `frontend/src/components/admin/ReplayMoveDetails.tsx`
25. `frontend/src/components/admin/ReplayMoveDetails.test.ts`
26. `frontend/src/components/admin/ReplayMoveInspector.tsx`
27. `frontend/src/components/admin/ReplayMoveInspector.test.ts`
28. `frontend/src/components/admin/ReplayScoreBreakdown.tsx`
29. `frontend/src/components/admin/ReplayScoreBreakdown.test.ts`
30. `frontend/src/components/admin/ReplayToolTimeline.tsx`
31. `frontend/src/components/admin/ReplayToolTimeline.test.ts`
32. `frontend/src/components/admin/ReplayEngineDetails.tsx`
33. `frontend/src/components/admin/ReplayEngineDetails.test.ts`
34. `frontend/src/components/admin/CompletionSourceBadge.tsx`
35. `frontend/src/components/admin/CompletionSourceBadge.test.ts`
36. `frontend/src/components/admin/admin.module.css`

In addition, you have WRITE AUTHORITY to output your complete terminal report file to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/06_report_00.md`

⛔ Any mutation to any file outside this allowlist is strictly unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `05_report_00.md`:

### 3.1 Backend: Detailed Score Breakdown & Certification Capture (`scoring.py`, `inspection.py`, `services.py`, `replay.py`)

1. In `backend/gamecore/scoring.py` and `types.py`:
   - Extend `ScoreBreakdown` (or add an opt-in inspection helper) with detailed per-letter tile math:
     * `physical_cells`: `[{row, col, token, blank_as, base_points, is_new, premium_applied, letter_multiplier}]`
     * `word_multiplier`: integer (e.g. 2 for DW, 3 for TW, 4 for DW+DW)
     * `word_total`: calculated points
   - Capture this before premiums are consumed, so the exact premium contribution is recorded.
2. In `backend/game/inspection.py`:
   - Build `capture_word_inspection(...)`: captures authority name (`WordAuthority`), lexicon identifier, route, and tile breakdown.
   - Build `capture_move_inspection(...)`: formats the inspection object saved inside `Move.words_formed`.
3. In `backend/game/replay.py`:
   - Include the captured inspection object in `plies[k].words_formed` if available.
   - Backward-compatible: if inspection data is absent, keep existing `word`, `score`, `multiplier`, `coords`.
4. In `backend/game/serializers.py`:
   - Allow optional `inspection_trace` inside `ai_metadata`. Validate bounds (max 64 events per attempt, max 96 KiB total).

### 3.2 Frontend: AI Tool-Call Telemetry & Trace Capture (`ai-inspection-trace.ts`, `route.ts`, `ai-fallback.ts`)

1. In `frontend/src/lib/ai-inspection-trace.ts`:
   - Bounded in-memory event collector during AI move execution:
     * Records `validateMove` invocations: candidate placements, words returned, validity (`valid: true/false`), rejection code.
     * Records phase transitions: `search` -> `repair` -> `finishMove`.
     * Records `finishMove` invocation: `{ready: true}`.
   - Serializes sanitized `inspection_trace` into the move request body before committing the move.
2. In `frontend/src/app/api/ai/move/route.ts`:
   - Attach tool events to the attempt trace.
   - Forwards trace in SSE done event and save-move payload.
3. In `frontend/src/lib/ai-fallback.ts`:
   - Carry forward earlier attempt traces into subsequent attempts so multi-attempt fallbacks are preserved in the final trace.

### 3.3 Frontend: Replay Move Inspector (`ReplayMoveInspector.tsx`, `ReplayStudio.tsx`)

1. In `frontend/src/components/admin/ReplayStudio.tsx`:
   - Integrate `ReplayMoveInspector` below the dual racks in the right column on desktop (≥1024px), preserving board and rack visibility.
   - On mobile/tablet, render as an inline collapsible accordion.
   - Opening inspector pauses replay playback.
2. In `frontend/src/components/admin/ReplayMoveInspector.tsx`:
   - Tabbed container with 3 tabs:
     * Tab 1: **Score & Words**
     * Tab 2: **AI Telemetry & Tool Calls**
     * Tab 3: **Engine & Search**
   - Accessible tabs (`role="tablist"`, `aria-selected`, arrow-key navigation).
3. Tab 1: `ReplayScoreBreakdown.tsx`:
   - Renders exact mathematical equation: `[L(1) + E(1) + A(1) + D(2)] × 2 DW = 10`.
   - Distinguishes primary word from secondary cross-words.
   - Shows **Bingo +50** badge when all 7 tiles were placed.
   - Displays WordAuthority certification and lexicon source.
4. Tab 2: `ReplayToolTimeline.tsx`:
   - Shows chronological list of tool calls in that turn:
     * `validateMove`: proposed coordinates, words formed, validity pill (Green `Valid` / Red `Rejected`), rejection reason.
     * `finishMove`: confirmation.
   - Shows `CompletionSourceBadge`:
     * Emerald: `Provider candidate`
     * Amber: `Backend ranked candidate`
     * Indigo: `Repair candidate`
     * Blue: `Backend legal rescue`
     * Stone: `No legal move (pass/exchange)`
   - Telemetry chips: `latency_ms` (time to submission), `provider_requests_used`, attempt index/model name.
5. Tab 3: `ReplayEngineDetails.tsx`:
   - Shows `DiagnosticPly` metrics if linked to a `DiagnosticRun`:
     * `model_authored`: Yes/No
     * `first_validate_valid`: Yes/No
     * `valid_candidate_count`: count
     * `model_legal_score` vs `ranked_best_score`
     * `ranked_search_complete`: boolean
     * `playability_status`: status string
   - If no diagnostic ply attached: display "No diagnostic run linked to this move".

## 4. Verification Commands

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_move_inspection.py tests/test_admin_replay_api.py -v
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-move-inspection.test.ts src/lib/ai-inspection-trace.test.ts src/components/admin/ReplayMoveInspector.test.ts src/components/admin/ReplayScoreBreakdown.test.ts src/components/admin/ReplayToolTimeline.test.ts src/components/admin/ReplayEngineDetails.test.ts src/components/admin/CompletionSourceBadge.test.ts
```

⛔ Do NOT run package installers (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY allowlisted files by explicit paths:
```bash
git add backend/gamecore/types.py backend/gamecore/scoring.py backend/game/services.py backend/game/serializers.py backend/game/replay.py backend/game/inspection.py backend/tests/test_move_inspection.py backend/tests/test_admin_replay_api.py frontend/src/lib/types.ts frontend/src/lib/admin-replay.ts frontend/src/lib/admin-replay.test.ts frontend/src/lib/admin-replay.fixtures.ts frontend/src/lib/admin-move-inspection.ts frontend/src/lib/admin-move-inspection.test.ts frontend/src/lib/ai-inspection-trace.ts frontend/src/lib/ai-inspection-trace.test.ts frontend/src/lib/ai-fallback.ts frontend/src/lib/ai-fallback.test.ts frontend/src/lib/ai-move-stream.ts frontend/src/lib/ai-move-stream.test.ts frontend/src/app/api/ai/move/route.ts frontend/src/app/api/ai/move/route.test.ts frontend/src/components/admin/ReplayStudio.tsx frontend/src/components/admin/ReplayMoveDetails.tsx frontend/src/components/admin/ReplayMoveDetails.test.ts frontend/src/components/admin/ReplayMoveInspector.tsx frontend/src/components/admin/ReplayMoveInspector.test.ts frontend/src/components/admin/ReplayScoreBreakdown.tsx frontend/src/components/admin/ReplayScoreBreakdown.test.ts frontend/src/components/admin/ReplayToolTimeline.tsx frontend/src/components/admin/ReplayToolTimeline.test.ts frontend/src/components/admin/ReplayEngineDetails.tsx frontend/src/components/admin/ReplayEngineDetails.test.ts frontend/src/components/admin/CompletionSourceBadge.tsx frontend/src/components/admin/CompletionSourceBadge.test.ts frontend/src/components/admin/admin.module.css
git diff --staged --stat
```

Commit with message:
```bash
git commit -m "feat(admin): implement deep move inspector, score breakdown math, and AI telemetry drawer"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a"
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
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/06_report_00.md`

The report content must begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 06, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a`
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

In your final chat message, emit a concise 3-line notification confirming that the report has been written to disk at `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/06_report_00.md`.
