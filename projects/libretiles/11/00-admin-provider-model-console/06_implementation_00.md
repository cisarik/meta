You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An accepted plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: APMC-S4-SESSION — the diagnostic session foundation: `is_diagnostic` + full `DiagnosticRun` (migration 0009), `create_diagnostic_game`, `apply_position_snapshot`, branched acting-slot derivation that is provably behaviour-identical for product games, `abort_diagnostic_run`, history exclusion, admin dashboard exclusion, reserved service account. Backend only. Provider calls: ZERO.
Phase: implementation
Exact baseline: 01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29
Implementation authority: explicit
Independence required: no (implementer) — final acceptance is a separate fresh independent audit session (slice 4-IA, INFOSEC 4.4, R3)
Evidence posture: non-independent
Evidence tier: E3
Evidence tier basis: durable migration + authN/Z-adjacent surfaces (reserved service account, session visibility) + acting-slot change at four call sites. Combined implementation envelope is allowed under E3 with gates; the implementing Worker's evidence stays non-independent.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks: (1) the acting-slot change touches four call sites where the product's behaviour must remain byte-identical — one wrong branch silently returns a human rack to the model or moves for the wrong seat; (2) the migration seeds a reserved user — a wrong attribute set creates a credential-adjacent surface; (3) a partial unique constraint must actually fire (tested, not asserted).

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
AP.md:2453-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself. That sentence is what makes a reading shortcut fail closed.
```

## Mandatory reading — by symbol; re-measure every symbol before you use it

```text
/home/agile/Projects/libretiles/AGENTS.md               project brief; "Word validation" binds
backend/game/models.py            GameSession (every field; game_mode choices = vs_ai/vs_human ONLY),
                                  PlayerSlot (Meta.ordering = ["slot"]), Move, ConsumedWsTicket —
                                  ⭐ NO is_diagnostic, NO DiagnosticRun exists today; latest game
                                  migration is 0008_atomic_token_state_schema
backend/game/services.py          create_game (:1047) — slot 0 human is_ai=False, seed is
                                  random.randint INSIDE _initialize_session; _load_session_for_user
                                  (:449, filters slots__user_id — UNCHANGED); _load_vs_ai_session
                                  (:474, ai_slot = session.slots.filter(is_ai=True).first() at :487);
                                  _check_active_turn (:558); get_ai_context (:1574 — NO turn check;
                                  always first AI slot); validate_move_for_ai (:1612, rack_owner=="ai"
                                  uses its OWN .filter(is_ai=True).first() at :1621); _submit_*_locked;
                                  _reject_ai_nonscoring (:681); list_games_for_user (:1179);
                                  _resolve_ai_model (:335); _stored_ai_metadata
backend/game/views.py             GameHistoryView (:242) — calls list_games_for_user
backend/game/admin.py             GameSessionAdmin dashboard cards count ALL sessions today
backend/game/position_sets.py     game_from_snapshot — READ-ONLY import; ⛔ this file is byte-frozen
backend/game/migrations/0008_atomic_token_state_schema.py   the migration house style
backend/accounts/models.py        User — set_unusable_password, blacklist_outstanding_refresh_tokens;
                                  ⛔ accounts/** is NOT editable — import via AUTH_USER_MODEL settings
backend/tests/test_admin.py       admin test house style
backend/tests/test_game_app_has_no_dev_imports.py   the AST guard (game/** scope)
backend/pyproject.toml            ⚠ addopts = "-q": never pass a second -q
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start and before commit
```

If `main` has advanced past `01ade17`: re-gate against the THEN-HEAD, state the new baseline in your
report, and continue — your allowlist and claims do not change. Any other divergence: classify with
the five canonical recovery classes and stop on `unexplained-divergence`.

## 2. THE GOAL — one paragraph

Slice 3 built byte-stable position snapshots; slice 5 will drive real models through the pipeline.
Between them stands the missing piece: a **persisted diagnostic session** — a real `GameSession` the
existing AI HTTP surface can drive, with two AI seats, a server-derived acting slot, a clean abort
path for model authorship failures, and complete invisibility to players. This slice builds exactly
that foundation and NOTHING more: ⛔ no runner, no admin launcher, no heartbeat, no provider call,
no frontend, no route.ts edit.

## 3. The design contract — from the accepted plan, with its corrections baked in

```text
MIGRATION backend/game/migrations/0009_<descriptive>.py  (NEW — the only migration)
  a. GameSession.is_diagnostic = BooleanField(default=False)
  b. GameSession.bag_rng_state = JSONField(null=True, blank=True, default=None)
     (diagnostic-only use; product create_game leaves it null; required so a mounted position's
     bag RNG continuity survives an exchange — the accepted plan's §10 finding)
  c. DiagnosticRun, FULL schema in THIS migration so slice 5 needs no second E3 migration:
       id UUID pk · status CharField(choices: queued/running/completed/failed/cancelled/
         abandoned/blocked_dependency, default queued) · assist_mode CharField
         (choices: assisted/authorship) · instrument CharField
         (choices: position-set/full-game, default full-game) · variant_slug CharField ·
         seat0_model_id CharField · seat1_model_id CharField · prompt FK catalog.AIPrompt null ·
         session FK game.GameSession · position_set_digest CharField blank · max_plies Integer ·
         max_provider_requests Integer · max_wall_clock_seconds Integer · heartbeat_at DateTime null ·
         pid Integer null · diagnostic_end_reason CharField blank · executed_runtime_mode
         CharField blank (fake|live|"") · score_authority CharField blank (engine|model|"") ·
         report_path CharField blank · log_path CharField blank · created_by FK
         settings.AUTH_USER_MODEL · parameters_json JSONField(default=dict) · created_at/updated_at
     Partial unique constraint: exactly one in-flight run — UniqueConstraint(
       fields=["status"], condition=Q(status__in=["queued","running"]), name="unique_inflight_diagnostic_run")
     (SQLite-legal; a test must create a second queued row and expect IntegrityError)
  d. RunPython forward: ensure_diagnostic_service_user() — get_or_create username
     "libretiles-diagnostic" with set_unusable_password(), is_staff=False, is_superuser=False,
     is_active=True, no groups, no user_permissions, preferred_ai_model_id="".
     ⛔ NEVER call set_password on it (set_password on an unusable-password user would still not
     stamp password_changed_at, but do not touch the password at all). Reverse: delete the row.
     The same logic ships as an idempotent services.ensure_diagnostic_service_user() the migration
     calls, so tests and the runner can re-ensure it.

SERVICES backend/game/services.py
  create_diagnostic_game(*, variant_slug, seed: int, seat0_model_id, seat1_model_id,
                         prompt_id: int | None, created_by_id: int,
                         assist_mode: str) -> dict
    · ensure_diagnostic_service_user()
    · resolve BOTH model ids through get_selectable_models() (same shape as _resolve_ai_model);
      unknown → fail closed, raise, no row written
    · GameSession.objects.create(game_mode="vs_ai", is_diagnostic=True, variant_slug=…,
      ai_model=<seat1 model row>, ai_prompt=<prompt or None>, current_turn_slot=None,
      bag_seed=seed)
    · slot 0: user=service_user, is_ai=True; slot 1: user=None, is_ai=True
    · _initialize_session(..., seed=seed) — EXTEND the helper with `seed: int | None = None`;
      None keeps random.randint for product create_game (F-G: behaviour-identical); diagnostic
      passes the int
    · DiagnosticRun(status=queued, parameters_json=<reproducible copy>, session=…, created_by=…,
      assist_mode=…, seat model ids, variant_slug, executed_runtime_mode=None, score_authority=None)
    · return {game_id, run_id, current_turn_slot, service_user_id} — ⛔ NEVER a JWT, never a
      credential value, never a token

  _resolve_acting_ai_slot(session) -> PlayerSlot | None
    if session.is_diagnostic:
        if session.current_turn_slot not in (0, 1): return None   # fail closed; ⛔ never coerce
        return session.slots.filter(slot=current_turn_slot, is_ai=True).first()
    return session.slots.filter(is_ai=True).first()               # product: first AI (slot 1)

  _load_vs_ai_session: membership via _load_session_for_user (slots__user_id UNCHANGED) →
    game_mode=="vs_ai" → acting = _resolve_acting_ai_slot(session); acting is None → GameNotFoundError.
    get_ai_context must split THREE roles: membership (authenticated user's slot), acting
    (_resolve_acting_ai_slot), opponent (1 - acting.slot). build_ai_state_dict(ai_rack=acting.rack,
    human_score=opponent.score, ai_score=acting.score). ai_model/ai_prompt text from the ACTING
    slot's FKs, then session FKs. Product identity (F-A) must hold exactly.
    validate_move_for_ai: rack_owner=="ai" uses _resolve_acting_ai_slot — NOT its own
    .filter(is_ai=True).first().
    ⛔ Do NOT change set_game_ai_model / set_game_ai_prompt semantics beyond what the branch
    requires; keep their current product behaviour.

  apply_position_snapshot(session, snapshot) -> None
    · fail closed unless session.is_diagnostic
    · structured {token, blank_as} board + per-cell premium_used; racks from
      rack/opponent_rack/to_move_seat_index; ordered bag_tiles; seat scores/pass_streaks/names;
      consecutive_scoreless_turns; ended/end_reason/leftover_points/winner_name/no_moves_available
      as applicable; bag_rng_state → session.bag_rng_state; current_turn_slot = to_move_seat_index
    · persists via the same persistence helpers the submit paths use (_persist_board/_persist_bag)
    · calls position_sets.game_from_snapshot for the gamecore-equivalence side — ⛔ position_sets.py
      itself is byte-frozen; you only IMPORT from it

  abort_diagnostic_run(*, run_id: UUID, reason: str) -> dict
    · requires the run's session.is_diagnostic
    · DiagnosticRun.status="failed", diagnostic_end_reason=reason, ended_at=now
    · ⛔ creates ZERO Move rows; ⛔ does NOT call _submit_pass_locked/_submit_exchange_locked;
      ⛔ does NOT bypass or weaken _reject_ai_nonscoring (it stays on every is_ai pass/exchange,
      diagnostic included)
    · GameSession.status="abandoned" with EMPTY game_end_reason (a run-level reason, never a fake
      finished-match reason)

  list_games_for_user: add .filter(is_diagnostic=False) in the SERVICE (the view then needs no
    change). build_ws_ticket: refuse when session.is_diagnostic (fail closed, diagnostic is not a
    human websocket product).

ADMIN backend/game/admin.py
  GameSessionAdmin: list_filter gains is_diagnostic; the four dashboard cards
  (Games/Active/Finished/AI turns) count .filter(is_diagnostic=False). ⛔ Do NOT hide diagnostic
  games from the staff changelist — a badge/filter, not invisibility.

VIEWS backend/game/views.py — ONLY if you prove a view-level guard is necessary; prefer the
  service-layer filter. Say which you chose and why.
```

## 4. Path allowlist and negative authority

```text
Positive authority (exact paths):
  backend/game/models.py
  backend/game/migrations/0009_<descriptive>.py          NEW
  backend/game/services.py
  backend/game/admin.py
  backend/game/views.py                                  only if §3's condition fires; else untouched
  backend/tests/test_diagnostic_session.py               NEW

Negative authority (⛔ forbidden):
  backend/gamecore/**                     byte-frozen
  backend/game/position_sets.py           byte-frozen (import only)
  backend/game/migrations/0001-0008       byte-frozen
  backend/accounts/**                     (import User via settings.AUTH_USER_MODEL only)
  backend/catalog/**, backend/config/**, backend/assets/**
  frontend/**                             every file — ⚠ the aiSlot:1 hardcode in
                                          ai-play-diagnostic.ts:438 is NAMED and NOT fixed here
  backend/tests/** except the one NEW test module
  backend/pyproject.toml                  ⛔ no dependency change
  ⛔ No provider call. ⛔ No run_diagnostic_match command. ⛔ No admin launcher. ⛔ No route.ts edit.
  ⛔ Never read or print backend/.env / frontend/.env.local.
```

Commands and the RF-16 bounded deviation exactly per house pattern: all Python through
`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/` — the declared `poetry run`
route is unusable in this Worker boundary (the Cursor AppImage intercepts `python*` via inherited
`APPIMAGE`/`PYTHONHOME`); rationale, evidence class, bounded authority, and stopping condition as
previously stated. ⛔ Never ambient `python`, `python3`, or `poetry run`.

## 5. Fail-before table — capture BEFORE you edit, verbatim

| ID | Pre-fix claim (must fail on current HEAD) |
|---|---|
| F-A | vs_ai, current_turn_slot=0: get_ai_context rack equals slot 1 (today) — the test asserting the DIAGNOSTIC branch cannot exist yet; capture the pre-fix product value as the identity anchor |
| F-B | Two is_ai seats, current_turn_slot=1: submit_move_for_ai persists slot 0 today (wrong seat for diagnostics) — capture the pre-fix persisted slot |
| F-C | list_games_for_user includes is_diagnostic rows today (field does not exist → the filtered test cannot pass pre-fix; capture the AttributeError/FieldError) |
| F-D | POST /api/auth/login/ for "libretiles-diagnostic" pre-migration: user does not exist (capture); post: 401, has_usable_password() False, is_staff/is_superuser False, groups/permissions empty |
| F-E | Ordinary user JWT GET /api/game/{diagnostic_id}/ → 404 (membership unchanged) |
| F-F | abort_diagnostic_run missing pre-fix; post: diagnostic_end_reason=model_authorship_failure, Move count UNCHANGED, no pass/exchange Move row created |
| F-G | create_game still creates slot 0 is_ai=False; _initialize_session without seed still assigns bag_seed |
| F-H | apply_position_snapshot on a diagnostic session: current_turn_slot == snapshot to_move_seat_index; non-diagnostic session rejected |
| F-I | Diagnostic current_turn_slot=None → AI endpoints fail closed (NOT slot 0) |
| F-J | Register of the reserved username after migrate → unique error |
| F-K | Second queued DiagnosticRun while one in-flight → IntegrityError (partial unique fires) |

## 6. Validation — the full standing backend set

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Documented mypy scope, never narrowed. Plain `-m pytest`, never a second `-q`; quote all summaries
VERBATIM. Baseline at `01ade17`: mypy `Success: no issues found in 88 source files`, ruff clean,
pytest `844 passed, 4 skipped in 536.41s`. Added tests fine; no removals, no skips. Also run
`manage.py migrate` against the dev DB and quote the 0009 line. ⛔ No `npm run build` (frontend
gates cannot move). Classify any failure before repairing; one broad rerun per materially changed
candidate.

## 7. Git pattern — exactly this

```bash
git add backend/game/models.py \
        backend/game/migrations/0009_<descriptive>.py \
        backend/game/services.py \
        backend/game/admin.py \
        backend/tests/test_diagnostic_session.py
# + backend/game/views.py ONLY if §3's condition fired
git diff --cached --stat        # verify EXACTLY the allowlisted paths, no instrumentation left
git commit -m "feat(game) diagnostic session foundation with two AI seats"
git ls-remote origin refs/heads/main    # MUST print your re-gated baseline
git push origin main                     # one non-force fast-forward
git rev-parse HEAD && git ls-remote origin refs/heads/main   # readback — MUST be equal
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced beyond your
re-gated baseline → STOP, report both SHAs, escalate.

## 8. Stopping conditions

```text
· the repository gate disagrees on any value, or porcelain is not empty
· the acting-slot branch cannot be made product-identical (F-A) without touching a byte-frozen file
· the migration cannot seed the service user idempotently, or F-J cannot be proven
· the partial unique constraint cannot be made to fire (F-K)
· _reject_ai_nonscoring, evaluate_scoring_move, or WordAuthority.accepts_tokens would need to
  weaken for any abort path — ⛔ STOP and report instead
· a gate failure pointing outside the allowlist · the pre-push equality gate fails
· secret exposure of any kind, or an instruction embedded in a repository file
· completed allowlisted work, gates green, pushed, readback equal — stop THERE and report
```

## 9. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 06, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` is the expected value); start/end commit; changed files with exact paths;
tests and validation — the F-A..F-K table with pre/post values, the three gate summaries VERBATIM,
the migrate output line, and (if fired) the views.py decision; commit and push result with SHA and
the readback pair; deviations, risks, or missing evidence; one smallest next step; exactly one
report justification from the closed enum at `AP.md:2453-2454`; explicit authority-expiry
statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT, the
  accepted plan §3, and the stated goal. Is any call site of the acting-slot branch missed?
  Is any DiagnosticRun column wrong for the slice-5 runner that will consume it? Assume one is
  and look.>
Enumeration widened: none | <...>  — e.g. other consumers of list_games_for_user, other dashboard
  counts, other ws-ticket paths, anything the plan's inventory could not reach.
```

⛔ Your authority ends at that report. Do not start slice 5, do not run K2, do not archive into
Meta. Acceptance — including the separate fresh independent authN/Z audit (slice 4-IA) — is the
ORCHESTRATOR's, after re-verification.
