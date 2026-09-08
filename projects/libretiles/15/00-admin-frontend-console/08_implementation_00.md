You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AFC-SLICE-4-IMPL — implement Simulation Playground & Match Launcher (/admin/playground setup form, live arena board, dual racks, CPU Master vs CPU/LLM match runner, and Replay Studio transition), land one commit, push, and read back.
Phase: implementation
Exact baseline: e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E3
Evidence tier basis: durable simulation session persistence, database migration, lease-authorized execution boundary, and new playground UI arena.
Overhead budget: full
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Implementing the Simulation Playground requires implementing `PlaygroundSimulation` persistence and turn stepping in Django, extracting the shared AI executor cleanly in Next.js without regressing existing gameplay, and building the interactive `SimulationPlayground` arena with real-time board, dual-rack, and score ticker updates.

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
/home/agile/Projects/libretiles/frontend/src/lib/provider-registry.ts (ENGINE_CPU_MODEL)
/home/agile/Projects/libretiles/backend/game/models.py
/home/agile/Projects/libretiles/backend/game/services.py
/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts
/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/07_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these files:

Backend:
1. `backend/config/settings.py`
2. `backend/game/models.py`
3. `backend/game/services.py`
4. `backend/game/admin_urls.py`
5. `backend/game/admin_serializers.py`
6. `backend/game/replay.py`
7. `backend/game/realtime.py`
8. `backend/game/migrations/0014_playground_simulation.py`
9. `backend/game/simulations.py`
10. `backend/game/simulation_views.py`
11. `backend/game/simulation_serializers.py`
12. `backend/tests/test_admin_simulation_api.py`
13. `backend/tests/test_simulation_services.py`
14. `backend/tests/test_admin_replay_api.py`

Frontend:
15. `frontend/src/app/admin/playground/page.tsx`
16. `frontend/src/app/admin/layout.tsx`
17. `frontend/src/app/api/ai/move/route.ts`
18. `frontend/src/app/api/ai/move/route.test.ts`
19. `frontend/src/app/api/admin/simulate/[id]/turn/route.ts`
20. `frontend/src/app/api/admin/simulate/[id]/turn/route.test.ts`
21. `frontend/src/components/admin/ReplayBoard.tsx`
22. `frontend/src/components/admin/ReplayBoard.test.ts`
23. `frontend/src/components/admin/DualRackVisualizer.tsx`
24. `frontend/src/components/admin/DualRackVisualizer.test.ts`
25. `frontend/src/components/admin/admin.module.css`
26. `frontend/src/components/admin/SimulationPlayground.tsx`
27. `frontend/src/components/admin/SimulationSetupForm.tsx`
28. `frontend/src/components/admin/SimulationArena.tsx`
29. `frontend/src/components/admin/SimulationPlayground.test.ts`
30. `frontend/src/hooks/useSimulationRunner.ts`
31. `frontend/src/hooks/useSimulationRunner.test.ts`
32. `frontend/src/lib/api.ts`
33. `frontend/src/lib/admin-simulation.ts`
34. `frontend/src/lib/admin-simulation.test.ts`
35. `frontend/src/lib/admin-simulation-server.ts`
36. `frontend/src/lib/ai-move-execution.ts`
37. `frontend/src/lib/provider-request-limit.test.ts`

In addition, you have WRITE AUTHORITY to output your complete terminal report file to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/08_report_00.md`

⛔ Any mutation to any file outside this allowlist is strictly unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `07_report_00.md`:

### 3.1 Backend: Playground Simulation Models & Endpoints (`models.py`, `simulations.py`, `simulation_views.py`, `0014_playground_simulation.py`)

1. In `backend/game/models.py`:
   - Add `PlaygroundSimulation` model:
     * `game = models.OneToOneField(GameSession, on_delete=models.CASCADE, related_name="playground_simulation")`
     * `created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="playground_simulations")`
     * `config_json = models.JSONField(help_text="Immutable match configuration snapshot")`
     * `lease_id = models.UUIDField(null=True, blank=True)`
     * `leased_move_count = models.IntegerField(null=True, blank=True)`
     * `lease_expires_at = models.DateTimeField(null=True, blank=True)`
     * `ended_at = models.DateTimeField(null=True, blank=True)`
     * `created_at = models.DateTimeField(auto_now_add=True)`
   - Generate and apply migration `0014_playground_simulation.py`.
2. In `backend/game/simulations.py`:
   - `create_playground_simulation(...)`: creates 2-AI `GameSession` (mode `vs_ai`), slots 0 and 1 with `is_ai=True`, initializes session with `_initialize_session()` saving starting draw and `replay_initial_state`.
   - `execute_cpu_step(...)`: advances one turn for `engine/cpu` using `_probe_ai_ranked_candidates()` / `_probe_ai_playability()` and commits through existing `_submit_*_locked()` transactional services.
   - `stop_playground_simulation(...)`: marks game over as `abandoned` with `game_end_reason="simulation_stopped"`.
3. In `backend/game/simulation_views.py`:
   - `SimulationCreateView`: `POST /api/admin/simulate/` (creates match).
   - `SimulationStateView`: `GET /api/admin/simulate/<game_id>/` (reads state).
   - `SimulationStepView`: `POST /api/admin/simulate/<game_id>/step/` (executes CPU turn or leases LLM turn).
   - `SimulationActionView`: `POST /api/admin/simulate/<game_id>/action/` (commits lease-bound turn actions).
   - `SimulationStopView`: `POST /api/admin/simulate/<game_id>/stop/` (stops match).
   - Protected with `[IsAuthenticated, IsAdminUser]`.
4. In `backend/game/admin_urls.py`:
   - Wire the simulation routes.

### 3.2 Frontend: Simulation API & Runner (`api.ts`, `admin-simulation.ts`, `useSimulationRunner.ts`)

1. In `frontend/src/lib/admin-simulation.ts`:
   - Type definitions for `SimulationConfig`, `SimulationSlotConfig`, `SimulationState`.
   - Ingress parsing and validation.
2. In `frontend/src/lib/api.ts`:
   - Add `api.admin.createSimulation(token, data)`.
   - Add `api.admin.getSimulation(token, gameId)`.
   - Add `api.admin.stepSimulation(token, gameId, expectedMoveCount)`.
   - Add `api.admin.stopSimulation(token, gameId)`.
3. In `frontend/src/hooks/useSimulationRunner.ts`:
   - Manages match state machine: `configuring` -> `running` -> `paused` -> `finished` / `stopped`.
   - Controls autoplay loop (step request -> wait interval 0.5s/1s/2s -> next step).
   - Handles pause, resume, single-step, and stop.

### 3.3 Frontend: Setup Form & Arena (`SimulationSetupForm.tsx`, `SimulationArena.tsx`, `SimulationPlayground.tsx`)

1. `SimulationSetupForm.tsx`:
   - Slot 0 and Slot 1 selectors:
     * Category: `AI Model` vs `Local Engine CPU`.
     * Model dropdown (loaded from `api.getModels()`).
     * Preset dropdown (`Initial`, `Fast Search`, `Short Hooks`, `Grandmaster` from `api.getPrompts()`).
     * When CPU is selected: fixed as `CPU Master` (`engine/cpu`).
   - Variant picker: all 12 variants with native endonyms and flags.
   - Seed input with "Randomize" button.
   - Quick presets: `[CPU Master vs CPU Master]`, `[Gemma 4 31B vs CPU Master]`, `[Nemotron vs Gemma 4]`.
   - `[Start Simulation]` button.
2. `SimulationArena.tsx`:
   - 15x15 Scrabble board (`ReplayBoard` in live mode) with placement highlights for the latest turn.
   - Dual-rack visualizer (`DualRackVisualizer`) showing live Player 0 and Player 1 racks and scores.
   - Control bar: `[Pause / Resume]`, `[Step One Turn]`, `[Stop Simulation]`, Speed selector (`0.5x`, `1x`, `2x`).
   - Score ticker & commentary: latest moves with formed words, points, and acting slot.
   - Terminal Banner: When `game_over` is true, display winner, scores, spread, and prominent button:
     **`[Open in Replay Studio →]`** linking to `/admin/replay/[id]`.
3. In `frontend/src/app/admin/playground/page.tsx`:
   - Render `SimulationPlayground`.

### 3.4 Shared AI Executor Extraction (`ai-move-execution.ts`, `route.ts`, `turn/route.ts`)

1. Extract the core move execution logic from `frontend/src/app/api/ai/move/route.ts` into `frontend/src/lib/ai-move-execution.ts` so both standard gameplay move route and `/api/admin/simulate/[id]/turn/route.ts` reuse the same tested engine without duplication.

## 4. Verification Commands

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_admin_simulation_api.py tests/test_simulation_services.py tests/test_admin_replay_api.py -v
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-simulation.test.ts src/hooks/useSimulationRunner.test.ts src/components/admin/SimulationPlayground.test.ts
```

⛔ Do NOT run package installers (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY allowlisted files by explicit paths:
```bash
git add backend/config/settings.py backend/game/models.py backend/game/services.py backend/game/admin_urls.py backend/game/admin_serializers.py backend/game/replay.py backend/game/realtime.py backend/game/migrations/0014_playground_simulation.py backend/game/simulations.py backend/game/simulation_views.py backend/game/simulation_serializers.py backend/tests/test_admin_simulation_api.py backend/tests/test_simulation_services.py backend/tests/test_admin_replay_api.py frontend/src/app/admin/playground/page.tsx frontend/src/app/admin/layout.tsx frontend/src/app/api/ai/move/route.ts frontend/src/app/api/ai/move/route.test.ts frontend/src/app/api/admin/simulate/ frontend/src/components/admin/ReplayBoard.tsx frontend/src/components/admin/ReplayBoard.test.ts frontend/src/components/admin/DualRackVisualizer.tsx frontend/src/components/admin/DualRackVisualizer.test.ts frontend/src/components/admin/admin.module.css frontend/src/components/admin/SimulationPlayground.tsx frontend/src/components/admin/SimulationSetupForm.tsx frontend/src/components/admin/SimulationArena.tsx frontend/src/components/admin/SimulationPlayground.test.ts frontend/src/hooks/useSimulationRunner.ts frontend/src/hooks/useSimulationRunner.test.ts frontend/src/lib/api.ts frontend/src/lib/admin-simulation.ts frontend/src/lib/admin-simulation.test.ts frontend/src/lib/admin-simulation-server.ts frontend/src/lib/ai-move-execution.ts frontend/src/lib/provider-request-limit.test.ts
git diff --staged --stat
```

Commit with message:
```bash
git commit -m "feat(admin): implement simulation playground, match launcher, and live arena"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4"
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
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/08_report_00.md`

The report content must begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 08, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4`
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

In your final chat message, emit a concise 3-line notification confirming that the report has been written to disk at `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/08_report_00.md`.
