### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 15, Worker exchange ordinal: 01
```

**1. Status:** PASS. **2. Phase-qualified result:** `implementation-PASS`. **3. Start/end commit:** start `f17a8ba0dc0e0d97da770e2ed2238190b6e432b1` (gate verified: HEAD, `.ap` gitlink `9c5cc44`, detached `.ap` HEAD, `## main...origin/main`, porcelain empty) → end `a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20`.

**4. Changed files (exactly the allowlist; 14 paths, 2569 insertions):**
- `backend/game/models.py` — `DiagnosticPly` only (lawful shape **B**: one nullable-where-Optional column per `PlyMetricRecord` field + `run` FK `related_name="plies"`, `ply_index`, nullable `position_index`, `UniqueConstraint(run, ply_index)`; no column name contains any `SECRET_KEY_FRAGMENTS` substring; no `DiagnosticRun` change)
- `backend/game/migrations/0011_diagnostic_ply.py` — NEW, reversible CreateModel on `0010_diagnostic_service_account`; `makemigrations --check` clean
- `backend/game/services.py` — `configure_diagnostic_run` (cap range-checks 1..200/1000/21600, digest iff position-set, `subcaps_provisional`, rejects `SECRET_KEY_FRAGMENTS` keys and JWT-shaped values), `cancel_diagnostic_run` (cancelled, never failed, no Moves), `mint_diagnostic_access_token` (AccessToken only), `abandon_stale_diagnostic_runs` (threshold `max(300, 2*max_wall_clock_seconds)` → `stale_heartbeat`); `abort_diagnostic_run` untouched
- `backend/game/admin.py` — `DiagnosticRunAdmin` (launch view with `has_change_permission` guard, stale flip → IntegrityError→form-message → `create_diagnostic_game` → `configure` → `Popen([sys.executable, manage.py, run_diagnostic_match, --run-id, <uuid>], cwd=backend, start_new_session=True, stdin=DEVNULL)` env minus APPIMAGE/ARGV0/APPDIR, no JWT, no `call_command`; cancel as admin POST action; heartbeat age + in-flight badge; diagnostics stay visible)
- `backend/game/management/commands/run_diagnostic_match.py` — NEW: `--run-id` sole argument; refuses on LIVE_SENTINEL; claims queued row (running+pid+heartbeat); mint after start; one long-lived Node worker per run over length-capped JSONL IPC (no token field); per-ply heartbeat/30s-or-5-plies, cancel poll, wall-clock check + SIGALRM +60s grace (main thread only); reconciles latest persisted Move; `PlyMetricRecord` → `DiagnosticPly` + redacted JSONL log; unobservable metrics persist as None; assisted continues, authorship writes ply **then** `abort_diagnostic_run("model_authorship_failure")`; caps → completed/`truncated`/score_authority `""`; natural ends: **`full_game_over`** and **`position_set_exhausted`** (quoted per contract); Node death mid-ply → ply from persisted state, fresh worker; position-set loads committed asset by 64-hex digest from `default_position_set_dir()` (24 positions, no generation); ai-match report under `backend/var/diagnostics/` via frozen `build_ai_match_report`/`write_report_atomically`
- `backend/game/templates/admin/game/diagnosticrun/change_list.html`, `launch.html` — NEW (house style)
- `backend/tests/test_diagnostic_runner.py` + `backend/tests/fixtures/diagnostic_stub_worker.mjs` — NEW: 24 tests covering F01–F09 via stub worker (pytest never imports Next)
- `frontend/src/lib/ai-play-diagnostic.ts` — `aiSlot?: number`, anchor uses `opts.aiSlot ?? 1` (the one existing-line product change)
- `frontend/src/lib/ai-play-diagnostic.test.ts` — aiSlot default-1 / explicit-0 anchor tests + token no-echo test
- `frontend/scripts/diagnostic-resolve-hooks.mjs`, `diagnostic-worker.mjs` — NEW K2 machinery: `registerHooks` (`@/`→src, .ts/.tsx/.js/index retries, no `--experimental-transform-types`, no package.json change); long-lived stdin/stdout worker, dies on EOF, fetch-guard fake mode, JWT from env only, scrubbed error messages
- `.gitignore` — `backend/var/` only

**5. Tests and validation (VERBATIM):**
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog` → `Success: no issues found in 93 source files`
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .` → `All checks passed!`
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest` → `898 passed, 4 skipped in 554.30s (0:09:14)` (baseline 874 passed, 4 skipped; no removals/skips added; F08 AST guard included)
- `migrate` → `Applying game.0011_diagnostic_ply... OK`
- `npm run typecheck` → exit 0, no errors. `npm run lint` → 0 problems (one unused `NextRequest` import removed during the run). `npx vitest run src/lib/ai-play-diagnostic.test.ts` → `Test Files  1 passed (1)`, `Tests  12 passed (12)`. No `npm run build`.
- K2 plain-Node proof (committed real worker, `generic_unchanged`, closed `BACKEND_URL=http://127.0.0.1:9`, `env -i` zero provider env): **exit=0**; redacted one-liner: `{"seq":1,"status":"done","terminal_kind":"generic_error","completion_source":null,"turn_provider_requests_used":0,"external_provider_invocations":0,"foreign_origins":[],"sentinel_present":false}`; token string absent from output.

**6. Commit and push:** `a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20` pushed `main -> main` (non-force fast-forward from `f17a8ba`); pre-push remote gate printed baseline `f17a8ba…`; readback pair: local `a17cdf4f…` == origin `a17cdf4f…`; porcelain clean.

**7. Fail-before F01–F10:** all captured pre-fix by construction and pinned post-fix by the named tests (F01 ply persistence; F02 cancel ≠ abort + runner exits 0; F03 ply/provider ceilings independent → truncated/`""`; F04 minted JWT absent from argv-shaped spawn, log, ply blob, parameters_json, IPC dump, report, OutstandingToken count unchanged, AccessToken-no-BlacklistMixin verified in installed simplejwt source; F05 sentinel refusal; F06 ply-then-abort `model_authorship_failure`; F07 second launch 302+message, never 500; F08 suite-green; F09 whitelist env dump: DJANGO_SECRET_KEY/DATABASE_URL/SECRET_KEY/NVIDIA_API_KEY/OPENROUTER_API_KEY/APPIMAGE/ARGV0/APPDIR/LIBRETILES_AI_PLAY_LIVE absent, JWT present only as `LIBRETILES_AI_PLAY_JWT`; F10 vitest anchor assertions).

**8. Deviations, risks, missing evidence:**
- RF-16 bounded deviation as declared: all Python via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`; never ambient `python`/`poetry run`.
- `LIBRETILES_DIAGNOSTIC_WORKER` override (test-only) plus, solely under that override, forwarding of `STUB_*` names into the Node whitelist; production default worker never hits this branch.
- Resolve-hook fallback: on bare-specifier failure it retries `node_modules/<spec>` with the ".js" retry — needed because Next 16.3.4's exports map has no `./server` while `node_modules/next/server.js` exists (the contract's ".js is required for next/server" note anticipated this).
- Runner turn constants quoted: `timeout_seconds=60`, `max_steps=10` (inert under `generic_unchanged`).
- Risks: none known. Missing evidence: none within E3; live NIM (K1), 4.4/4.6 certification, and slice 5-IA acceptance deliberately not attempted.

**9. One smallest next step:** Orchestrator-ordered slice 5-IA fresh audit of the mint/echo surface and launcher lifecycle.

**10. Report justification:** `new-mutation`.

**11. Authority expiry:** This prompt's authority expires with this report; no K1, slice 6, 3b, or Meta archival was started.

```text
Resolved Execution Issues / Near-Misses:
  - TransactionTestCase teardown in this suite does not flush between tests: first full run
    hit UNIQUE(catalog_ai_model.model_id); repaired with the house idempotent get-or-create
    seeding pattern (turn_probe.seed_catalog precedent). Near-miss: silent cross-test coupling.
  - Worker-death test was initially non-deterministic (stub died after answering; runner's
    EPIPE-retry correctly masked it): added STUB_DIE_BEFORE_TURN to exercise the real EOF path.
  - Stub knobs were blocked by the env whitelist by design; sanctioned STUB_* forwarding only
    under the test override (named above). AiMatchSample required-fields TypeError was caught
    by the report's fail-open guard and fixed.
Pre-Existing Failure Classification: none
Orchestration critique (scope: THIS PROMPT):
  - MEASURED: no JWT echo path survived — the token exists only inside the whitelisted child
    env (proven by the stub env dump) and is structurally absent from argv, IPC schema, logs,
    ply rows, parameters_json, and the report; tests grep for the minted string.
  - MEASURED: cancel does not call abort — separate `cancel_diagnostic_run`; abort semantics
    byte-untouched; F02/F06 pin both directions.
  - LEAD: design contract §3.2 contains a truncated sentence ("Do not generate new assees,
    or steps_consumed."); resolved by reading the frozen source as authority — future prompts
    should regenerate corrupted contract lines.
  - LEAD: the TransactionTestCase non-flush assumption is implicit in this suite; documenting
    it in AGENTS.md would spare future workers the same full-suite discovery cycle.
Enumeration widened: backend/game/templates/admin/game/diagnosticrun/launch.html and
  change_list.html (section-7 example realized); the STUB_* forwarding branch and the
  next/server node_modules fallback live inside already-allowlisted files (no new paths).
Context pressure: moderate — roughly two-thirds consumed, no truncation observed.
```