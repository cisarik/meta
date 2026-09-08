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




