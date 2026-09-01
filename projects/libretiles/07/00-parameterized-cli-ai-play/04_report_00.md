### Report for ORCHESTRATOR_CHAT

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 04
Worker exchange ordinal: 01

**Status:** implementation-PASS; publication-PASS.

**Phase-qualified result:** Slice T (`implement-slice-t-provider-free-turn-cli`) is implemented, validated, committed, and published on `origin/main`. Fake-mode CLI drives the real Next.js `POST /api/ai/move` handler, `orchestrateFallbackTurn`, `consumeAIStream`, and an ephemeral pytest-django `live_server` while only `getLanguageRuntime` / `generateText` are injected. Live mode is implemented and hard-refused without `LIBRETILES_AI_PLAY_LIVE=1`. The logical whole is not closed.

**Start commit:** `7b8fd1ec66270e7dd0f50d0fa09b7c517dc7c201` (`fix(engine): score Slovak endgame with variant tile points`)
**End commit:** `93d665d2c25f0923fdbcdedb0df98e460175f641` (`feat(diagnostics): add provider-free AI turn CLI`)
**.ap gitlink (unchanged):** `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`

**Changed files (purpose):**
- `AGENTS.md` — one-sentence `completion_source` vocabulary correction (`backend_ranked_candidate`)
- `backend/game/diagnostics.py` — turn sample types, NFC/two-letter classification, report merge, live sentinel, handoff constants
- `backend/assets/diagnostics/ai_play_report_v1.schema.json` — turn branch (`oneOf` engine/turn sample)
- `backend/assets/diagnostics/ai_play_scenarios_v1.json` — `slovak-turn-diacritic-blank`, `english-turn-dead-qqq`, `turn_scripts`
- `backend/game/management/commands/diagnose_ai_play.py` — CLI; spawns pytest node; no dev-group import
- `backend/tests/diagnostics/__init__.py`, `backend/tests/diagnostics/test_turn_probe.py` — pytest-django live-server testbed + named integration tests
- `backend/tests/test_ai_play_turn_diagnostic.py` — command-level axes, exit 2, redaction, classifiers
- `backend/tests/test_game_app_has_no_dev_imports.py` — AST guard for correction 1
- `frontend/src/lib/ai-play-diagnostic.ts` — queue, fetch guard, observation serialization, `runDiagnosticTurn`
- `frontend/src/lib/ai-play-diagnostic.test.ts` / `.worker.test.ts` / `.live.worker.test.ts` — unit, BACKEND_URL import-order, live sentinel refusal

**Implementation Authority Record:** explicit implementation; independence required: no; material phase gate: yes; changed material axis: mutation-authority-or-side-effect-class; combined implementation envelope: allowed; Git: stage allowlisted paths only; exactly one commit with the required subject; pre-push `git ls-remote origin refs/heads/main` must equal the baseline; then one non-force `git push origin main`; no force/amend/rebase/merge; do not close the logical whole.

**Capability handshake (abbreviated, material rows):**
- Cursor AppImage Python intercept — **requested / directly observed:** every Python/ruff/mypy/pytest invocation used `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` (or `.venv/bin/ruff`) from `backend/`
- Vitest / npm — **directly observed** from `frontend/`
- Provider credentials / `.env` / `.env.local` — **unknown-not-observably-exposed** (not read); fake `generateText` mock; live sentinel unset
- Network — **directly observed:** loopback ephemeral Django (`http://127.0.0.1:<port>`) plus Git remote gate/push; **inferred:** no foreign origin (fetch guard + `foreign_origins: []`)
- Dev-group import into `backend/game/**` — **directly observed absent** (AST guard green)
- JWT — **directly observed minted** inside the pytest test DB via SimpleJWT; **never printed**, never written into the v1 report

**BACKEND_URL import-ordering seam:** `BACKEND_URL` is module-scope in `route.ts`. The worker sets `process.env.BACKEND_URL` to the ephemeral origin, then `await import("@/app/api/ai/move/route")` (no top-level static import). Standalone Vitest asserts every `fetch` URL starts with `http://127.0.0.1:59999` and none contain `localhost:8000`. Runtime CLI reports recorded `backend_origins` such as `http://127.0.0.1:53017` / `http://127.0.0.1:51009` (command spawn uses `--liveserver=127.0.0.1`). `installFetchGuard` rejects any other origin.

**No dev-group import under `backend/game/**`:** `test_game_app_modules_do_not_import_dev_group_packages` AST-walks every `backend/game/**/*.py` for `pytest` / `pytest_django` / `_pytest` / `ruff` / `mypy`. The command only names `pytest` as a `sys.executable -m pytest` argv token.

**Validation results:**

Fake Slovak CLI (exit 0):
`slovak turn slovak-turn-diacritic-blank action=place source=backend_ranked_candidate score=82 words=SČÍTALO persisted=1 verdict=pass`

Per-sample: `completion_source=backend_ranked_candidate`; placements include regular `Č` and blank `?` with `blank_as=Í`; `playability.status=found`; `persistence.move_id=1`, `move_count_delta=1`; `reason_code=ok` (not `stale_witness`); `turn_provider_requests_used=0`; `external_provider_invocations=0`; `foreign_origins=[]`.

Fake English CLI (exit 0):
`english turn english-empty-autolin action=place source=backend_ranked_candidate score=66 words=OUTLAIN persisted=1 verdict=pass`

Same request accounting: provider HTTP used = 0; external invocations = 0 (distinct from unknown).

Live without sentinel: `CommandError: --runtime-mode live requires LIBRETILES_AI_PLAY_LIVE=1`, **exit 2**, no pytest/worker spawn.

Named tests: `test_found_probe_never_accepts_pass_or_exchange`, `test_none_probe_with_full_bag_exchanges_instead_of_passing` (`genuine_no_move_exchange` on `QQQQQQQ`), `test_generic_unchanged_turn_is_mechanical_failure`, `test_persist_then_lost_terminal_is_pass_with_telemetry`, selected-only / catalog-fallback / foreign-origin guards — all green. Stay-green backend and frontend suites green. `npm run lint` / `npm run build` green.

**Exact mypy count:** 12 errors in 6 files; none in new files (`diagnose_ai_play.py`, `diagnostics.py` clean). Pre-existing parked debt unchanged.

**Commit subject and SHA:** `feat(diagnostics): add provider-free AI turn CLI` / `93d665d2c25f0923fdbcdedb0df98e460175f641`
**Pre-push remote gate:** `7b8fd1ec66270e7dd0f50d0fa09b7c517dc7c201`
**Push result:** fast-forward `7b8fd1e..93d665d  main -> main` (non-force)
**Public readback SHA:** `93d665d2c25f0923fdbcdedb0df98e460175f641` (equals local HEAD)
**Final `git status --porcelain`:** empty
**Temp cleanup:** CLI `mktemp` dir `/tmp/tmp.Z347eOmgkH` removed; command `finally` `rmtree` of pytest handoff dirs

**Deviations / risks / missing evidence:**
- `seed_catalog` upserts `FREE_RIVAL_PAIRS` rather than skipping when any `AIModel` exists: migration `0012` inserts inactive prepared rivals, so `exists()` is true on a fresh test DB.
- Command-level `subprocess.run` mock forwards non-pytest calls (`git rev-parse` inside `observe_source_revision`).
- Fake `generateText` is a noop; the persisted scoring move is the real ranked/witness path (`backend_ranked_candidate`). That is the accepted fake-mode composition, not a production behavior change.
- No live provider call was made.

**Smallest next step:** keep the whole open; the next authorized slice is live-mode under an explicit provider grant (`LIBRETILES_AI_PLAY_LIVE=1`), not a source change to this CLI.

Report justification: new-mutation
Logical-whole closure: not-closed
Authority expiry: this exchange’s authority expires with this terminal report, cancellation, or supersession. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** (1) catalog `exists()` short-circuit vs migration-prepared inactive rivals; (2) test mock intercepting `git rev-parse`; (3) Vitest default 5s timeout vs real route + ranked search — worker tests now use 60s/180s; (4) mypy on a mixed `dict[str, str | int | None]` request — resolved with `TurnCliRequest` TypedDict.

**Pre-Existing Failure Classification (parked mypy debt):** 12 errors in 6 files (`config/settings.py`, `game/models.py`, `game/realtime.py`, `gamecore/scoring.py`, `gamecore/game.py`, `game/services.py`). Class: pre-existing / out of slice authority; not introduced or enlarged by this commit.