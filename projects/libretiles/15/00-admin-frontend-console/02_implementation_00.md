You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AFC-SLICE-1-IMPL — implement Backend Replay Data API & Admin Endpoints (GET /api/admin/games/ and GET /api/admin/games/<id>/replay/), state capture in session transactions, staff authorization boundary, purge legacy games command, and comprehensive test suite. Land one commit, push, and read back.
Phase: implementation
Exact baseline: 531a80963115fa7a3ab42f86710f1a2f360df90d
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E3
Evidence tier basis: changes to database schema (migration), game session transactional state capture, staff authorization boundary, and new admin-facing replay API.
Overhead budget: full
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Implementing the Replay API requires ensuring that replay state capture occurs cleanly inside existing game transactions (`services.py`) without affecting move evaluation, timer budgets, or scoring. Furthermore, staff permissions (`IsAdminUser`) must strictly reject non-staff users, `UserSerializer` must expose `is_staff` read-only, and old games must be cleanly purgable.

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
/home/agile/Projects/libretiles/backend/config/urls.py
/home/agile/Projects/libretiles/backend/game/models.py
/home/agile/Projects/libretiles/backend/game/services.py (_initialize_session, submit_move_transactional, submit_exchange_for_user, submit_pass_for_user, give_up_for_user)
/home/agile/Projects/libretiles/backend/accounts/serializers.py (UserSerializer)
/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/01_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 531a80963115fa7a3ab42f86710f1a2f360df90d
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these files:
1. `backend/accounts/serializers.py`
2. `backend/config/urls.py`
3. `backend/game/models.py`
4. `backend/game/services.py`
5. `backend/game/admin_urls.py`
6. `backend/game/admin_views.py`
7. `backend/game/admin_serializers.py`
8. `backend/game/replay.py`
9. `backend/game/migrations/0013_admin_replay_capture.py`
10. `backend/game/management/commands/purge_legacy_games.py`
11. `backend/game/management/commands/run_diagnostic_match.py`
12. `backend/tests/test_admin_replay_api.py`

In addition, you have WRITE AUTHORITY to output your complete terminal report file to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/02_report_00.md`

⛔ Any mutation to any file outside this allowlist is strictly unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `01_report_00.md` with the **Cooperator's explicit Clean Slate decision**:
Existing development games in the database have no replay state and do NOT need complex reverse-deduction or lossy heuristic backwards-compatibility. We start with a clean slate for all new games and provide a clean purge command!

### 3.1 Database Models & Migration (`backend/game/models.py`)

Add the replay capture fields to `GameSession`, `Move`, and `DiagnosticPly`:
1. `GameSession`:
   - `replay_initial_state = models.JSONField(null=True, blank=True, editable=False, help_text="Initial state snapshot {board, premium_used, racks, bag_remaining, scores, turn_slot}")`
2. `Move`:
   - `replay_before = models.JSONField(null=True, blank=True, editable=False, help_text="State snapshot before move")`
   - `replay_after = models.JSONField(null=True, blank=True, editable=False, help_text="State snapshot after move")`
   - `exchanged_tiles = models.JSONField(null=True, blank=True, editable=False, help_text="Exact list of tile tokens exchanged")`
3. `DiagnosticPly`:
   - `move = models.ForeignKey("Move", null=True, blank=True, on_delete=models.SET_NULL, related_name="diagnostic_plies", editable=False)`
   - `replay_before = models.JSONField(null=True, blank=True, editable=False)`
   - `replay_after = models.JSONField(null=True, blank=True, editable=False)`
   - `ai_trace = models.JSONField(null=True, blank=True, editable=False)`
4. Generate migration `backend/game/migrations/0013_admin_replay_capture.py` and verify with `python manage.py makemigrations --check --dry-run`.

### 3.2 Expose `is_staff` on `UserSerializer` (`backend/accounts/serializers.py`)

1. In `UserSerializer`:
   - Add `"is_staff"` to `fields = ("id", "username", "email", "preferred_ai_model_id", "date_joined", "is_staff")`.
   - Add `"is_staff"` to `read_only_fields = ("id", "date_joined", "is_staff")`.
   - Ensure `is_staff` cannot be modified via registration or update payloads.

### 3.3 Replay Capture & Services (`backend/game/replay.py` and `backend/game/services.py`)

1. In `backend/game/replay.py`:
   - `build_snapshot(session: GameSession) -> dict[str, Any]`:
     Captures `{board, premium_used, racks: [slot0.rack, slot1.rack], scores: [slot0.score, slot1.score], bag_remaining: len(session.bag_tiles), current_turn_slot: session.current_turn_slot}`.
   - `build_replay_payload(session: GameSession) -> dict[str, Any]`:
     Assembles the complete replay payload:
     * `game_id`, `variant_slug`, `game_mode`, `status`, `winner_slot`, `game_end_reason`, `created_at`, `finished_at`.
     * `tile_points`, `alphabet`.
     * `players`: list of slot info (`slot`, `username`, `score`, `is_ai`, `model_display_name`).
     * `initial_state`: `initial_board` (15x15 empty grid), `initial_racks`, `initial_scores: [0, 0]`, `starting_turn_slot`, `bag_seed`.
     * `plies`: array of plies (seq 1..N):
       - `seq`, `player_slot`, `kind`, `created_at`.
       - `placements`: list of `{row, col, letter, blank_as}`.
       - `words_formed`: list of `{word, score, multiplier, coords}`.
       - `points`, `tiles_exchanged`, `exchanged_tiles`.
       - `cumulative_scores`: `[score_0, score_1]` after this ply.
       - `racks`: `[rack_0, rack_1]` after this ply.
       - `board_delta`: `{row, col, token, blank_as}` placed in this turn.
       - `ai_metadata`: sanitized metadata from `Move.ai_metadata`.
       - `diagnostic_ply`: linked `DiagnosticPly` metrics if present.
     * `final_state`: current board, racks, scores.
     * `replay_status`: `"complete"` if initial state and plies have snapshots, `"partial"` if unrecorded historical data.
2. In `backend/game/services.py`:
   - In `_initialize_session()`: save `replay_initial_state = build_snapshot(session)` after initial racks are drawn.
   - In `submit_move_transactional()`, `submit_exchange_for_user()`, `submit_pass_for_user()`, `give_up_for_user()`:
     * Capture `before = build_snapshot(session)`.
     * Apply move, end game checks, and bag updates.
     * Capture `after = build_snapshot(session)`.
     * Save `move.replay_before = before`, `move.replay_after = after`, `move.exchanged_tiles = letters_exchanged` (for exchange moves).
3. In `backend/game/management/commands/run_diagnostic_match.py`:
   - When creating `DiagnosticPly`, link `move=last_created_move` if a move was created during that ply.

### 3.4 Admin Endpoints & Views (`backend/config/urls.py`, `backend/game/admin_urls.py`, `backend/game/admin_views.py`, `backend/game/admin_serializers.py`)

1. In `backend/config/urls.py`:
   - Mount `path("api/admin/", include("game.admin_urls"))`.
2. In `backend/game/admin_urls.py`:
   - `path("games/", AdminGameListView.as_view(), name="admin-game-list")`
   - `path("games/<str:game_id>/replay/", AdminGameReplayView.as_view(), name="admin-game-replay")`
3. In `backend/game/admin_views.py`:
   - Both views require:
     ```python
     authentication_classes = [PasswordAwareJWTAuthentication, SessionAuthentication]
     permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
     ```
   - `AdminGameListView`:
     * Query params: `page` (default 1), `page_size` (default 20, max 100), `game_mode`, `variant_slug`, `status`, `is_diagnostic`, `search`.
     * Search checks UUID prefix or player usernames.
     * Uses `select_related("ai_model")` and `prefetch_related("slots__user", "slots__ai_model", "diagnostic_runs")` for efficient querying.
     * Returns `{count, page, total_pages, page_size, results: [...]}`.
   - `AdminGameReplayView`:
     * Takes `<str:game_id>` (UUID or string), fetches `GameSession` (returns 404 if not found).
     * Returns `build_replay_payload(session)`.
4. In `backend/game/management/commands/purge_legacy_games.py`:
   - Implement `manage.py purge_legacy_games` to purge old `GameSession` records (with confirmation or `--yes` flag).
   - Execute it once to clean slate existing unneeded dev games as requested by the Cooperator.

### 3.5 Test Suite (`backend/tests/test_admin_replay_api.py`)

Implement thorough test coverage:
1. `test_admin_games_list_requires_staff`: anonymous -> 401, non-staff -> 403, staff -> 200.
2. `test_admin_games_list_filtering`: verifies filters for mode, variant, status, and search.
3. `test_admin_game_replay_requires_staff`: anonymous -> 401, non-staff -> 403, staff -> 200.
4. `test_admin_game_replay_structure`: creates a game, plays placement, exchange, pass moves, verifies dual racks, cumulative scores, and board deltas.
5. `test_admin_game_replay_diagnostic_integration`: verifies `DiagnosticPly` is attached to replay moves.
6. `test_user_serializer_exposes_is_staff`: `/api/auth/me/` returns `is_staff: true/false`.

## 4. Verification Commands

Always run backend commands from `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_admin_replay_api.py -v
```

From `frontend/` (read-only verification):
```bash
npm run typecheck
npm run lint
```

⛔ Do NOT run `npm run build` (writes to `.next/`).
⛔ Do NOT run package installers (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add backend/accounts/serializers.py backend/config/urls.py backend/game/models.py backend/game/services.py backend/game/admin_urls.py backend/game/admin_views.py backend/game/admin_serializers.py backend/game/replay.py backend/game/migrations/0013_admin_replay_capture.py backend/game/management/commands/purge_legacy_games.py backend/game/management/commands/run_diagnostic_match.py backend/tests/test_admin_replay_api.py
git diff --staged --stat
```

Commit with message:
```bash
git commit -m "feat(game): implement admin replay API, state capture, and staff permission boundary"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "531a80963115fa7a3ab42f86710f1a2f360df90d"
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
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/02_report_00.md`

The report content must begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 02, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `531a80963115fa7a3ab42f86710f1a2f360df90d`
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

In your final chat message, emit a concise 3-line notification confirming that the report has been written to disk at `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/02_report_00.md`.
