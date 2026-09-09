# Libre Tiles — Notes for logical whole `admin-frontend-console` (Meta 15/00)

Append-only notes ledger for logical whole 15/00.
Maintained by the Agent Orchestrator. Evidence and observation history; not task authority.

---

## §0 Whole 15 Boot and Baseline Record

Whole 15 initialized on 2026-09-08 following the successful closure of `ai-opponent-strength` (14/00).
- Baseline commit: `531a80963115fa7a3ab42f86710f1a2f360df90d`
- Pinned AP commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Standing quality gates:
  * Backend: mypy clean (104 files); ruff clean; fast pytest suites pass in < 15s.
  * Frontend: typecheck clean, lint clean, vitest 37 test files passed (630 tests passed).
- Handout prompt established:
  `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/00_handout.md`
- Core mission:
  1. Build dedicated Admin Frontend Console at `localhost:3000/admin`.
  2. Implement interactive game replay viewer with VCR playback controls (Play/Pause/Step) and scrub slider.
  3. Render dual racks simultaneously (Player 0 & Player 1) with real tile styling.
  4. Deep move inspector: formed words, score calculation, tool calls (`validateMove`, `finishMove`), completion source, latency.
  5. Simulation playground & arena to launch AI vs AI, AI vs CPU, or CPU vs CPU matches directly from the browser.
   6. Model & strategy analytics dashboard for VPS deployment readiness.
   7. Strict isolation: zero regression to regular user gameplay (`/game/[id]`, `/play`, `/settings`).

---

## §1 Slice 1 Planning Launch: Backend Replay Data API & Admin Endpoints

- Baseline check: HEAD `531a80963115fa7a3ab42f86710f1a2f360df90d` aligned with origin/main, porcelain clean, .ap at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- Quality gates verified: mypy clean (104 files), ruff clean, focused pytest clean; frontend typecheck clean, lint clean, vitest 34 tests in ai-fallback clean.
- Session 01 prompt written: `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/01_planning_00.md`.
- `apfieldcheck.py` executed: 0 DEFECTS, 1 WARNING (expected `Native planning mode: required`).
- Scope: Technical design of `GET /api/admin/games/` and `GET /api/admin/games/<id>/replay/`, deterministic dual-rack timeline reconstruction from `bag_seed`, telemetry extraction from `Move.ai_metadata` and `DiagnosticPly`, staff-only DRF gating, and `backend/tests/test_admin_replay_api.py`.

---

## §2 Session 01 Report Acceptance & Cooperator Clean-Slate Decision

- Worker Session 01 submitted `01_report_00.md` with status `PASS`.
- Technical design reviewed across D1-D8:
  * Dedicated admin routing under `api/admin/` with `IsAuthenticated` + `IsAdminUser`.
  * `is_staff` exposed on `UserSerializer` / `GET /api/auth/me/` for frontend authorization.
  * Direct state capture on all new moves (`replay_initial_state`, `replay_before`, `replay_after`, `exchanged_tiles`) rather than relying solely on lossy reverse deduction.
  * Explicit linking between `DiagnosticPly` and `Move`.
- **Cooperator Direction (Clean-Slate Decision)**:
  * Cooperator explicitly instructed: delete existing legacy games in dev DB; no backwards compatibility or migration needed for old games lacking replay state.
  * Purging old games keeps models and replay services 100% clean, lean, and deterministic.
- **Protocol Improvement (Autonomous Worker Report Archiving)**:
  * Future workers will write their terminal report (`02_report_00.md`, etc.) directly to `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/` to eliminate manual copy-pasting courier fatigue for the Cooperator.
  * Updated `/home/agile/meta/AP_DEFECTS.md` with D-17 (Human Courier Trap) and D-18 (Sunk-Cost Dev-Data Preservation).
  * Updated `/home/agile/meta/BRAINSTORMING.md` with Section 5 (Autonomous Worker Report Archiving) and Section 6 (Clean Slate Protocol for Alpha/Prototyping).

---

## §3 Slice 1 Landed: Backend Replay Data API & State Capture

- Worker Session 02 submitted `02_report_00.md` with status `PASS`, written directly to disk.
- Landed commit: `1a29262795e7e2a79bdf9e70239f180656e8d234` on `main`, pushed to `origin/main`, readback verified.
- Delivered features:
  1. Additive migration `0013_admin_replay_capture.py` applied cleanly.
  2. Transactional state capture in `backend/game/services.py` and `backend/game/replay.py`:
     - Initial state snapshot (`replay_initial_state`) in `_initialize_session()`.
     - Before and after state snapshots (`replay_before`, `replay_after`) and `exchanged_tiles` on all moves (`place`, `exchange`, `pass`, `give_up`).
     - Explicit linking of `DiagnosticPly.move` in `run_diagnostic_match.py`.
  3. Staff permission boundary:
     - Routes `/api/admin/games/` and `/api/admin/games/<game_id>/replay/` protected by `[PasswordAwareJWTAuthentication, SessionAuthentication]` and `[IsAuthenticated, IsAdminUser]`.
     - `is_staff` exposed read-only on `UserSerializer` (`/api/auth/me/`).
  4. Clean-slate purge executed: `manage.py purge_legacy_games --yes` cleanly wiped 31 legacy sessions (242 rows).
  5. Test suite `backend/tests/test_admin_replay_api.py` passes 8/8 tests in < 5s.
- Quality gates verified:
  * Backend: mypy clean (110 source files), ruff clean, makemigrations clean.
  * Frontend: typecheck clean, lint clean.

---

## §4 Slice 2 Planning Launch: Frontend Replay Engine & Playback Controls

- Baseline check: HEAD `1a29262795e7e2a79bdf9e70239f180656e8d234` aligned with origin/main, working tree clean.
- Quality gates verified: mypy clean (110 files), ruff clean; frontend typecheck clean, lint clean.
- Session 03 prompt written: `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/03_planning_00.md`.
- `apfieldcheck.py` executed: 0 DEFECTS, 1 WARNING (expected `Native planning mode: required`).
- Scope: Frontend architecture for `/admin/` games list and `/admin/replay/[id]` replay studio, `useReplayEngine` playback hook (play/pause/step/scrub/speed), simultaneous dual-rack display with gold/black premium tile styling, board reconstruction with placed-tile highlights, staff access check, and Playwright verification.

---

## §5 Session 03 Report Acceptance: Slice 2 Frontend Replay Architecture

- Worker Session 03 submitted `03_report_00.md` with status `PASS`.
- Technical design reviewed across D1-D8:
  * Route architecture: `/admin` (games list), `/admin/replay/[id]` (replay studio), `/admin/login` (admin sign-in with return callback), placeholders for `/admin/playground` and `/admin/analytics`.
  * `AdminAccessGate`: checks fresh `/api/auth/me/` for `is_staff === true`; unauthenticated redirects to `/admin/login?next=...`; authenticated non-staff gets styled 403 screen with return link to `/play`.
  * API client: `api.admin.listGames` and `api.admin.getReplay` added to `frontend/src/lib/api.ts` with complete TypeScript interfaces in `frontend/src/lib/types.ts`.
  * Controller: `admin-replay-engine.ts` + `useReplayEngine.ts` hook with 1000ms base interval, 0.5x/1x/2x speeds, play/pause/step/scrub, auto-pause at N, keyboard shortcuts.
  * Dual-rack visualizer: `DualRackVisualizer.tsx` rendering Player 0 and Player 1 racks simultaneously with tactile gold/black tile styling and turn indicators.
  * Replay board: `ReplayBoard.tsx` with immutable frame precomputation, placement delta highlight rings, and formed words breakdown.
  * VCR controls: `ReplayControls.tsx` with VCR buttons, native range slider timeline scrubber, and speed selector pills.
  * Playwright verification plan: local synthetic verification with ephemeral test fixtures.
  * Path allowlist strictly frontend-only; zero modification to player-facing gameplay routes (`/game/[id]`, `/play`, `/settings`).

---

## §6 Slice 2 Landed & Playwright Verified: Frontend Replay Studio & Dual Racks

- Worker Session 04 landed commit `a7f9960243542ffdf5a90b870be211f68c7cdbd3` across 30 allowlisted frontend files.
- Refinement commit: `1d57ee2` (guarded `AdminAccessGate` against hydration promise deadlock on client navigation).
- Live Playwright verification executed in real browser:
  1. Unauthenticated request to `/admin` successfully prompted admin sign in (`/admin/login`).
  2. Staff login with `adminstaff` authenticated cleanly and restored navigation to `/admin`.
  3. Games list rendered with full filter toolbar (Mode, Variant, Status, Search) and loaded sample game (`81959d773468`).
  4. Clicking `[View Replay]` navigated to `/admin/replay/81959d77-3468-4e0a-b3e5-0f934d69f9d9`.
  5. Dual-rack visualizer rendered both Player 0 (`adminstaff`, 10 pts) and Player 1 (`Gemma 4 31B IT`, 0 pts) racks simultaneously with gold/black tile styling.
  6. Replay board reconstructed Ply 1 with golden highlights on placed tiles (`L`, `E`, `A`, `D`) and formed word breakdown (`LEAD · 10 points`).
  7. Step backward `<` returned board to initial empty position, reset racks and score to 0, and disabled backward buttons.
- All quality gates clean: mypy clean (110 source files), ruff clean, frontend typecheck clean, lint clean, vitest 25 tests passed.

---

## §7 Slice 3 Planning Launch: Deep Move Inspector & Telemetry Drawer

- Baseline check: HEAD `1d57ee2eb0760fa0d6556e4c767425110eb2ad1d` aligned with origin/main, working tree clean.
- Session 05 prompt written: `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/05_planning_00.md`.
- `apfieldcheck.py` executed: 0 DEFECTS, 1 WARNING (expected `Native planning mode: required`).
- Scope: Deep Move Inspector architecture: mathematical score breakdown (letters, multipliers, bingo, cross-words), AI tool-call execution viewer (`validateMove` candidate proposals, accepted vs rejected words, `finishMove`), `completion_source` badges, provider requests & latency telemetry, lexicon authority inspection, and `DiagnosticPly` metrics integration.

---

## §8 Session 05 Report Acceptance: Slice 3 Deep Move Inspector Architecture

- Worker Session 05 submitted `05_report_00.md` with status `PASS`.
- Technical design reviewed across D1-D8:
  * Layout: `ReplayMoveInspector` with three tabs: `[Score & Words]`, `[AI Telemetry & Tool Calls]`, `[Engine & Search]`. Document flow layout, capped scroll at 32rem, board and dual racks remain 100% visible.
  * Score breakdown: mathematical equation capture (`[L(1) + E(1) + A(1) + D(2)] × 2 DW = 10`), physical cells, letter/word multipliers, 50-point bingo badge, and cross-word separation.
  * AI Tool-Call telemetry: `inspection_trace` capturing `validateMove` proposals (valid and rejected candidates), `finishMove` parameters, and repair phase transitions.
  * Badges & chips: `CompletionSourceBadge` (`provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_pass/exchange`), latency chips, attempt counts, provider request tracking.
  * Word authority & lexicon inspection: explicit `WordAuthority` certification and lexicon source naming.
  * Diagnostic ply integration: `model_authored`, `first_validate_valid`, `model_legal_score` vs `ranked_best_score`, and playability metrics.
  * Explicit allowlist covering backend scoring inspection helpers and frontend inspector components.

---

## §9 Slice 3 Landed & Playwright Verified: Deep Move Inspector & Recorded AI Telemetry

- Worker Session 06 landed commit `e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4` across 34 allowlisted files.
- Delivered features:
  1. Backend opt-in mathematical scoring details in `scoring.py` and `inspection.py`.
  2. Frontend telemetry trace capture in `ai-inspection-trace.ts` and SSE move route.
  3. `ReplayMoveInspector` component in `ReplayStudio.tsx` with 3 accessible tabs:
     - `[Score & Words]`: Formed words, letter-by-letter math, multipliers, bingo, and WordAuthority certification.
     - `[AI Telemetry & Tool Calls]`: Tool execution list (`validateMove`, `finishMove`), `CompletionSourceBadge`, latency, and request counts.
     - `[Engine & Search]`: `DiagnosticPly` metrics (`model_authored`, `first_validate_valid`, `valid_candidate_count`, scores, playability).
- Live Playwright verification in real browser confirmed:
  * Replay studio loaded `/admin/replay/81959d77-3468-4e0a-b3e5-0f934d69f9d9`.
  * Deep move inspector drawer opened on Ply 1 with toggle button.
  * All 3 tabs (`Score & Words`, `AI Telemetry & Tool Calls`, `Engine & Search`) switch cleanly and render their respective data.
- Quality gates clean: mypy clean (111 source files), ruff clean, 13 backend tests passed in 5.51s, frontend typecheck/lint clean, vitest 146 tests passed.

---

## §10 Slice 4 Planning Launch: Simulation Playground & Match Launcher

- Baseline check: HEAD `e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4` aligned with origin/main, working tree clean.
- Session 07 prompt written: `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/07_planning_00.md`.
- `apfieldcheck.py` executed: 0 DEFECTS, 1 WARNING (expected `Native planning mode: required`).
- Scope: Simulation Playground architecture under `/admin/playground/`: configuring Slot 0 vs Slot 1 across LLM models, CPU Master (`engine/cpu`), 4 strategic prompt presets, and 12 language variants. Live turn-by-turn board execution, real-time dual-rack and score updates, victory banner, and direct link to Replay Studio.

---

## §11 Session 07 Report Acceptance: Slice 4 Simulation Playground Architecture

- Worker Session 07 submitted `07_report_00.md` with status `PASS`.
- Technical design reviewed across D1-D8:
  * `PlaygroundSimulation` model linking 1-to-1 with `GameSession` storing configuration snapshot, creator, and turn lease.
  * `POST /api/admin/simulate/`: creates two-AI match session transactionally with `is_ai=True` for both slots.
  * Turn execution: CPU turns executed directly by backend engine search (`POLICY_RANKED_WITNESS_SAFE`), LLM turns executed via `/api/admin/simulate/[id]/turn/` with lease validation.
  * UI: `SimulationPlayground.tsx` with setup form (`SimulationSetupForm.tsx`) and live arena (`SimulationArena.tsx`) showing live 15x15 board, placement animation, dual racks, score ticker, and victory banner.
  * Direct transition to Replay Studio: `[Open in Replay Studio →]` linking to `/admin/replay/[id]`.
  * Evidence tier: E3 for full implementation.

---

## §12 Slice 4 Landed & Playwright Verified: Simulation Playground & Live Arena

- Worker Session 08 landed commit `8a978daed9c003155bd12535a3879fded32a5385` across 35 allowlisted files.
- Refinement commit `f040a64` (allowed optional seed and default timeouts in `create_playground_simulation`).
- Migration `0014_playground_simulation.py` applied cleanly.
- Live Playwright verification in real browser confirmed:
  1. Opened `/admin/playground`: setup form rendered with Slot 0, Slot 1, Category (AI Model vs CPU Master), 12 Variants with flags, Seed, and Quick Presets.
  2. Started "CPU Master vs CPU Master" match: live arena mounted immediately.
  3. Watched turns execute live in real time:
     - Opening move #1: `CORSETS` for 72 points on center.
     - Move #2: `CHIRK` for 28 points.
     - Followed by moves #3 through #16 (`TASE, TE, AR, ED`, etc.).
     - Live dual racks updated with drawn tiles, live score differential updated.
  4. Tested `[Pause]` button: successfully paused at move #15.
  5. Tested `[Step One Turn]`: cleanly advanced one turn to move #16.
  6. Tested `[Stop Simulation]`: stopped cleanly, displayed terminal banner with final scores and spread.
  7. Clicked `[Open in Replay Studio →]`: seamlessly opened the complete 16-ply game in `/admin/replay/[id]` for deep turn-by-turn analysis.
- Standing quality gates 100% green: mypy clean (115 files), ruff clean, makemigrations clean, 17 backend tests passed in 8.48s, frontend typecheck/lint clean, vitest 83 tests passed.

---

## §13 Slice 5 Planning Launch: Model Analytics Dashboard & VPS Deployment Recommendation

- Baseline check: HEAD `f040a649ae5430bbd743a68d0ee54e7d975a6c1e` aligned with origin/main, working tree clean.
- Session 09 prompt written: `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/09_planning_00.md`.
- `apfieldcheck.py` executed: 0 DEFECTS, 1 WARNING (expected `Native planning mode: required`).
- Scope: Model Analytics Dashboard architecture under `/admin/analytics/`: backend aggregation endpoint `GET /api/admin/analytics/` (win rates, spreads, average scores, % provider authorship, pass streaks, latencies), strategy preset comparison, VPS deployment recommendation card, navigation polish, and closure audit.

---

## §14 Session 09 Report Acceptance & Cooperator Brainstorming: Difficulty Sliders & AI Judge Selection

- Worker Session 09 submitted `09_report_00.md` with status `PASS`.
- Technical design reviewed across D1-D8:
  * Model Analytics Dashboard under `/admin/analytics/`: backend aggregation endpoint `GET /api/admin/analytics/` computing games played, win rate %, average score, spread differential, % provider authorship (`provider_candidate`), and latencies across models and prompt presets.
  * VPS deployment recommendation card: primary flagship, high-throughput rival, and offline CPU Master.
  * Navigation polish in `admin/layout.tsx`.
- **Cooperator Direction & Interactive Enhancements**:
  1. Difficulty / strength slider under Player 0 and Player 1 in `SimulationSetupForm.tsx` (mapping to the 4 prompt presets: `1: Initial`, `2: Fast Search`, `3: Short Hooks`, `4: Grandmaster`).
  2. Prompt preview: Ability to click and preview the strategic prompt configured for that AI player.
  3. Game Judge selection: Option to choose Dictionary (`WordAuthority`) vs AI Judge (`/api/ai/judge`) with model selector.
  4. In Replay Studio / Move Inspector: Display judge emoji button (⚖️) with popup showing how the AI Judge reasoned and explained the formed words.
- All included in the Slice 5 implementation scope!

---

## §15 Slice 5 Landed & Playwright Verified: Model Analytics & Interactive Polish

- Worker Session 10 landed commit `a892f740f194af2492c3865a9a1ea6dcf18ed1a7` across 29 allowlisted files.
- Delivered features:
  1. Backend analytics aggregation endpoint `GET /api/admin/analytics/` in `backend/game/analytics.py` and `analytics_views.py` with strict staff authentication and private no-store headers.
  2. Model Performance comparison table (`ModelAnalyticsTable.tsx`) with sortable metrics (win rate %, average score, spread, provider authorship %, latency, requests/turn).
  3. Preset Comparison cards (`PresetAnalyticsCards.tsx`) for `Initial`, `Fast Search`, `Short Hooks`, `Grandmaster`.
  4. VPS Deployment Recommendation banner (`DeploymentRecommendationCard.tsx`) highlighting primary flagship, high-throughput rival, and offline CPU Master.
  5. Interactive difficulty/strength sliders under Player 0 and Player 1 in `SimulationSetupForm.tsx` (levels 1–4) with live preset selection.
  6. Strategic Prompt Preview modal (`PromptPreviewModal.tsx`) allowing full text inspection of the selected AI preset instructions.
  7. Game Judge selector in simulation setup (Dictionary `WordAuthority` vs AI Judge) and judge verdict explanation modal (`JudgeExplanationModal.tsx`) with ⚖️ badge.
  8. Unified Admin Navigation (`AdminNavigation.tsx`) linking Games List, Simulation Playground, Model Analytics, Replay Studio, and Back to Game.
- Live Playwright verification in real browser confirmed:
  * `/admin/analytics`: Model performance matrix rendered, summary stat cards loaded, preset cards and VPS deployment recommendation displayed.
  * `/admin/playground`: Difficulty/strength slider on Seat 0 successfully changed levels, clicked `[👁 Preview Prompt]` which opened the modal showing the complete `Initial` prompt text, and Game Judge selector toggled cleanly.
- Quality gates clean: mypy clean (119 source files), ruff clean, 16 backend tests passed in 7.93s, frontend typecheck/lint clean, vitest passed.















