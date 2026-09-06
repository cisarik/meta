### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 05
Worker exchange ordinal: 01
```

**Status:** PASS  
**Phase-qualified result:** not-applicable  
**Logical-whole closure:** not-closed  

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Plan disposition: advisory
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
```

**Start commit:** `01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29`  
**End commit:** `01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29` (zero mutation)

**Changed files:** none. Side-effect class was read-only inspection. Porcelain empty at start; left empty.

**Tests and validation:** not run (planning; gates permitted, not required). Slice-3 F1–F10 and the three standing-gate summaries are not evidence of this exchange. Proposed slice-4 F-table is in §9. Local repository gate:

```text
HEAD          01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29
HEAD:.ap      9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
.ap HEAD      9c5cc44f8b6c92dd56ad2427d13223d7d59c5656  (detached — correct)
git status -sb            ## main...origin/main
git status --porcelain=v1 EMPTY
```

Network authority was NONE, so `git ls-remote` was not executed. Tracking-ref agreement is local, not a public readback.

**Commit and push:** not authorized. Not performed.

**Context pressure:** high — prompt vs AP conflict, INFOSEC, and a multi-file acting-slot proof in one cycle.

---

## 1. Prompt vs AP (honored AP; did not implement)

The prompt identity is plan-only (`Native planning mode: required`, no mutation). §§5–6 then require mypy/ruff/pytest, commit, `git ls-remote`, and push. AP wins (`AP.md:917-932`, `AP.md:2466-2486`, Plan-to-Execution). Those leftover implementation clauses were not followed.

Further prompt claims that are **false at HEAD** and must not be copied into an implementation prompt:

| Prompt claim | Repository at `01ade17` |
|---|---|
| `DiagnosticRun` already exists as GameSession FKs | `backend/game/models.py` ends at `ConsumedWsTicket`. No `DiagnosticRun`, no `is_diagnostic`. |
| ⛔ No migration | Any durable `is_diagnostic` / `DiagnosticRun` / service-user seed needs `game/migrations/0009_*`. Latest game migration is `0008_atomic_token_state_schema`. |
| `create_game(seed, variant_slug)` | Actual signature is `create_game(*, user_id, game_mode="vs_ai", ai_model_id, ai_model_model_id, ai_prompt_id, variant_slug="english")`. Slot 0 is always human `is_ai=False`. Seed is `random.randint` inside `_initialize_session`. |
| Slice 3 shipped an admin-registerable OpenAI-compatible target | Slice 3 shipped `position_sets.py` + generator + fixture `english-f5ae61b4.json`. Catalog still has only `AIModel` / `AIPrompt`. Diagnostic target remains accepted-plan slice 7. |
| Service account sources `process.env[credential_env_name]` | Django `User` has no env. Provider secrets stay on the Next.js process (`CREDENTIAL_ENV_BY_PROVIDER` in `game/diagnostics.py`: `NVIDIA_API_KEY`, `OPENROUTER_API_KEY`). Cooperator R2=A (env-var NAME only). |
| `_check_active_term` | Symbol is `_check_active_turn` (`services.py:558`). |
| Positive allowlist: `position_sets.py` NEW; tests only `test_position_sets.py`; `accounts/**` / migrations / frontend forbidden | Position-set files already exist. Slice 4 needs a new test module, a migration, `User` rows via `AUTH_USER_MODEL` (no `accounts/models.py` edit required), and must **not** touch `frontend/**` in this slice. |
| README diagnostics section | README has AI / catalog / probe / operations. No diagnostics section. |

---

## 2. Architecture — how a persisted two-AI session drives the pipeline

There is still **no in-process Python path** to `/api/ai/move`. The tool-only loop is TypeScript. Slice 4 does not fork it. Slice 4 makes a Django `GameSession` that the existing AI HTTP surface can drive.

**Do not reuse `create_game`.** Add `create_diagnostic_game(...)` in `backend/game/services.py`. Keep `game_mode="vs_ai"` so `_load_vs_ai_session` / `/ai-context/` / `/ai-move/` keep working without `route.ts` edits. Discriminator is `GameSession.is_diagnostic=True`, not a third `MODE_CHOICES` value (still only `vs_ai` / `vs_human`).

Recommended create signature (frozen dataclass return is fine; persist via ORM):

```text
create_diagnostic_game(
  *, variant_slug, seed, seat0_model_id, seat1_model_id,
  prompt_id: int | None, created_by_id: int, assist_mode: "assisted"|"authorship"
) -> DiagnosticGame
```

Creation steps:

1. `ensure_diagnostic_service_user()` (see §6).
2. Resolve both model ids through `get_selectable_models()` (same as `_resolve_ai_model`). Unknown → fail closed, no row.
3. `GameSession.objects.create(game_mode="vs_ai", is_diagnostic=True, variant_slug=..., ai_model=seat1_or_seat0, ai_prompt=..., current_turn_slot=None, bag_seed=seed)`.
4. Slot 0: `user=service_user`, `is_ai=True`, nullable `ai_model`/`ai_prompt` for seat 0.
5. Slot 1: `user=None`, `is_ai=True`, nullable FKs for seat 1.
6. `_initialize_session(..., seed=seed)` — extend today’s helper with `seed: int | None = None`; `None` keeps `random.randint(0, 2**31)` for product `create_game` (behaviour-identical). Diagnostic always passes the int seed into `TileBag(seed=seed, ...)`.
7. Insert `DiagnosticRun` `status=queued` with `parameters_json` (reproducible copy), `session` FK, `created_by`, `assist_mode`, seat model ids, `variant_slug`, `executed_runtime_mode=None`, `score_authority=None`.
8. Return `{game_id, run_id, current_turn_slot, service_user_id}` — **never** a JWT, never a credential value.

**`DiagnosticRun` does not exist. Put the full D7 schema in this slice’s migration** so slice 5 does not need a second E3 migration. Slice 4 **uses** create + abort + history. Slice 4 does **not** implement `run_diagnostic_match`, admin launcher, heartbeat, or provider spend. Nullable runner fields (`pid`, `heartbeat_at`, `report_path`, `log_path`) stay null.

`DiagnosticRun` minimum columns (from accepted plan D7, still valid): UUID `id`; `status` `{queued,running,completed,failed,cancelled,abandoned,blocked_dependency}`; `assist_mode`; `instrument` `{position-set,full-game}` (slice 4 may default `full-game` or leave blank until apply-snapshot); `variant_slug`; `seat0_model_id` / `seat1_model_id` CharFields; prompt FKs; `session` FK to `GameSession`; `position_set_digest`; caps; `heartbeat_at`; `pid`; `diagnostic_end_reason`; `executed_runtime_mode`; `score_authority`; `report_path`; `log_path`; `created_by` FK `User`; timestamps; `parameters_json`. Partial unique constraint on in-flight (`queued`|`running`) is SQLite-legal via `UniqueConstraint(condition=...)` and should land with the table.

**Connecting slice 3:** `game_from_snapshot` rebuilds `gamecore.Game` only (no Django). Add `apply_position_snapshot(session, snapshot)` in `services.py` (not in `position_sets.py`, which must stay Django-free): structured `{token, blank_as}` board, `premium_used`, both racks from `rack`/`opponent_rack`/`to_move_seat_index`, `bag_tiles`, `bag_rng_state` if the session bag needs RNG continuity, seat scores/pass_streaks, `consecutive_scoreless_turns`, `current_turn_slot = to_move_seat_index`. Fail closed if `session.is_diagnostic` is false. This is the mount path for 3b; empty seeded games remain valid for full-game instrument.

**Frontend blocker named, not fixed here:** `frontend/src/lib/ai-play-diagnostic.ts:438` hardcodes `aiSlot: 1`. Reconciliation `current_turn_slot !== anchor.aiSlot` cannot drive seat 0. `route.ts` POST still has no `api-auth` header path; token is JSON-body. Slice 4 stays backend-only. Slice 5 / K2 worker **must** pass `aiSlot: session.current_turn_slot` (server-derived on Django; client copies it). Product `ai-fallback.ts` may keep `aiSlot: 1` for non-diagnostic games.

---

## 3. Acting-slot derivation — product identity is **not** automatic

Today `_load_vs_ai_session` does `session.slots.filter(is_ai=True).first()`. `PlayerSlot.Meta.ordering = ["slot"]`, so first AI is the **lowest slot number**.

Product `create_game`: slot 0 human `is_ai=False`, slot 1 AI `is_ai=True` → first AI is **always slot 1**, independent of `current_turn_slot`.

Call sites that use that first-AI slot:

| Symbol | Uses first `is_ai`? | Calls `_check_active_turn`? |
|---|---|---|
| `submit_move_for_ai` / `_exchange` / `_pass` | yes, via `_load_vs_ai_session` | yes, on that AI slot |
| `get_ai_playability` / `get_ai_candidates` | yes | yes |
| `get_ai_context` | yes | **no** |
| `validate_move_for_ai` | yes, `rack_owner=="ai"` at `:1621` | no |
| `set_game_ai_model` / `set_game_ai_prompt` | loads vs_ai session | n/a |

`_check_active_turn`: `current_turn_slot is None or != player_slot.slot` → `"Not your turn"`.

**Unconditional `acting_slot = current_turn_slot` is not product-identical.** Counterexample: vs_ai, human’s turn (`current_turn_slot=0`). Today `get_ai_context` still returns **slot 1’s rack** (the AI). Using `current_turn_slot` would return the **human rack**. Playability/submit currently 409/conflict on human’s turn because they check the AI slot against turn 0; `get_ai_context` does not.

**Required branch** (prompt sketch is the right shape; it is incomplete):

```text
_resolve_acting_ai_slot(session) -> PlayerSlot | None
  if session.is_diagnostic:
      if session.current_turn_slot not in {0, 1}:
          return None          # fail closed; do not coerce None → 0
      slot = session.slots.filter(slot=current_turn_slot, is_ai=True).first()
      return slot              # None if that seat is not AI
  else:
      return session.slots.filter(is_ai=True).first()   # product: slot 1
```

`_load_vs_ai_session` still: membership via `_load_session_for_user` (`slots__user_id` **unchanged**); `game_mode=="vs_ai"`; then `acting = _resolve_acting_ai_slot`; if `acting is None` → `GameNotFoundError`.

`get_ai_context` must split three roles:

- **membership** = authenticated user’s slot (service user → slot 0)
- **acting** = `_resolve_acting_ai_slot`
- **opponent** = the other slot (`1 - acting.slot`)

`build_ai_state_dict(ai_rack=acting.rack, human_score=opponent.score, ai_score=acting.score)`. Prompt text / `ai_model_id` from **acting** slot FKs, then session FKs. Product: acting=slot1, opponent=slot0=membership → same scores and rack as today.

`validate_move_for_ai`: `rack_owner=="ai"` uses `_resolve_acting_ai_slot`, not `.filter(is_ai=True).first()`.

Diagnostic `current_turn_slot is None`: acting is None → 404, not slot 0.

---

## 4. Authorship abort — outside `_reject_ai_nonscoring`

Do **not** force pass/exchange and do **not** bypass `_reject_ai_nonscoring`. `evaluate_scoring_move` / `WordAuthority.accepts_tokens` stay the only placement certifiers. `GameEndReason` stays a gamecore end-of-game enum.

New service, diagnostic-only:

```text
abort_diagnostic_run(*, run_id or game_id, reason: Literal["model_authorship_failure", ...])
```

- Requires `session.is_diagnostic`.
- Writes `DiagnosticRun.status=failed`, `diagnostic_end_reason=model_authorship_failure`, `ended_at`.
- Creates **zero** `Move` rows. Does not call `_submit_pass_locked` / `_submit_exchange_locked`.
- May set `GameSession.status=abandoned` without stuffing a fake `game_end_reason` that looks like a finished match. Prefer empty `game_end_reason` plus run-level reason.

**Who detects failure:** the slice-5 runner, from the **in-memory SSE observation** (`completion_source` not in `{provider_candidate, repair_candidate}` when `assist_mode=authorship`; or no backend-valid model placement). `valid_candidate_count` is overlay telemetry and is **not** a persisted Django field (slice-2 LEAD). Slice 4 only supplies the abort writer. Django must not infer authorship from a missing move.

`assisted` mode never calls this abort for engine rescue. `_reject_ai_nonscoring` stays on every `is_ai` pass/exchange, diagnostic included.

---

## 5. History exclusion

Player list is `list_games_for_user` (`services.py:1179`), invoked by `GameHistoryView` (`views.py:248`). Filter belongs in the **service**, not only the view:

```text
GameSession.objects.filter(slots__user_id=user_id, is_diagnostic=False)
```

Position-set / run scoring reads `DiagnosticRun` / ply rows, never `/api/game/history/`.

Also exclude diagnostic sessions from **player-facing** totals. Staff admin may list them with a badge. `GameSessionAdmin` dashboard cards (`Games` / `Active` / `Finished` / `AI turns` at `admin.py:239-246`) currently count **all** sessions; leaving that unfiltered contaminates the operator picture. Slice 4 allowlist should include `backend/game/admin.py` for `is_diagnostic` list filter + dashboard `filter(is_diagnostic=False)`. Do not hide diagnostic games from staff changelist.

Ordinary user: `_load_session_for_user` 404s (no slot). Service JWT cannot load a product game it does not own. Product player JWT cannot load a diagnostic game.

Refuse `build_ws_ticket` when `is_diagnostic` (diagnostic is not a human websocket product). Cheap; prevents a second join path.

---

## 6. Service account — JWT identity, not provider secrets

Two different secrets:

| Secret | Process | Slice 4 |
|---|---|---|
| Provider API keys | Next.js `process.env` via `credential_env_name_for_provider` | **out of scope**. Do not store on `User`. Do not log. R2=A already decided. |
| Diagnostic Django JWT | minted in the **runner subprocess** with `RefreshToken.for_user(service_user)` (precedent: `test_turn_probe.mint_token`) | identity only |

`accounts.User` is already `AUTH_USER_MODEL`. **Do not edit `accounts/models.py`.** Create the row from `game` (migration `RunPython` + `ensure_diagnostic_service_user`).

Fixed username (example): `libretiles-diagnostic`. Create at migrate so `POST /api/auth/register/` cannot take it (unique username). Attributes:

- `set_unusable_password()`
- `is_staff=False`, `is_superuser=False`, `is_active=True` (JWT user must be active)
- no groups, no user_permissions
- `preferred_ai_model_id=""`

Login: `POST /api/auth/login/` (`ScopedTokenObtainPairView`) uses Django `authenticate` → unusable password fails. Minting via `RefreshToken.for_user` does **not** need a password (P3 surface). Controls: token never rendered in admin HTML; 2h access lifetime (`SIMPLE_JWT`); runner-only mint; tests in §9.

`User.set_password` sets `password_changed_at` only when changing an **existing usable** password. Unusable → `password_changed_at` stays null → password-change JWT gate does not bite minted tokens. Do not call `set_password` on this user.

Player-facing “user count”: there is no public user list. `/api/auth/me/` is self. Admin `User.objects.count()` will be +1 — accept as residual **info**, or exclude this username in the dashboard only. Do not put the service user in `/api/game/history/`.

---

## 7. Independent acceptance (this Worker does not certify)

E3: combined implementation envelope is allowed; **final acceptance is a fresh Worker that did not implement**. Implementing Worker’s own tests are non-independent (R1/R2).

```text
Acceptance independence: required-fresh-independent
Security task class: focused defensive audit — authentication and authorization specialization (INFOSEC 4.4)
Primary route: R3 (authN/Z)
Trigger row: "Authentication, authorization, session, token, role, or permission-check touch"
Not in slice 4: INFOSEC 4.6 live provider-boundary (no provider call, no new base_url)
Correction authority on the acceptor: none
```

Acceptor allowlist = the landed slice-4 paths only. Claims to prove: service user cannot login; ordinary JWT cannot see diagnostic games; history filter; acting-slot product identity; abort creates no Move and does not call `_reject_ai_nonscoring`; no secret in responses. Fail closed if any claim needs a live provider call.

---

## 8. INFOSEC — proportionate threat model

**Primary route: R3** (authN/Z audit). **R1** inside the implementation session (non-independent). Provider-boundary R3 for **this slice** is not triggered (no egress, no `base_url`, network NONE on the planner; implementation must keep provider calls at zero). Mintable service JWT is an escalation **within** R3, not a jump to R4.

### Threat-Model Fields

```text
Assets: Django session/admin; diagnostic GameSession / DiagnosticRun rows; service-user JWT; player game history integrity; formed-word / scoring integrity; provider credentials and quota (not stored here, but a leaked JWT can drive /api/ai/move spend); catalog is_active/sort_order (not written in this slice).
Trust boundaries: admin/created_by → create_diagnostic_game; service JWT → DRF AI endpoints; ordinary player JWT → same endpoints; Node worker (later) → Django with that JWT; history serializer → browser.
Attacker-controlled inputs: none from the public internet that this slice newly accepts. Local-actor assumption for tests. Later runner/admin forms are slice 5/6. Model text is not rendered here.
Security properties: object-level auth remains slots__user_id; server-derived acting slot; unusable password; is_diagnostic exclusion from player history; abort does not weaken WordAuthority; no secret in DiagnosticRun.parameters_json or logs; Redis still unused for AI-only boot.
Abuse cases: (1) product get_ai_context returns human rack if acting-slot is unbranched; (2) diagnostic games appear in /api/game/history/; (3) stolen staff session is out of slice 4, stolen minted service JWT can call AI endpoints and cause Next.js provider spend; (4) register race on service username if not seeded in migration; (5) service user listed as a player; (6) abort implemented as forced pass, hiding authorship failure; (7) two in-flight DiagnosticRun rows without partial unique.
```

No finding records: this is planning, not an audit. No containment ledger (no temp roots). Residual risk for Orchestrator: service JWT is a real credential-adjacent surface; slice 5 must treat mint as privileged and never echo the token.

### Source Version Record (planning citations only)

```text
Title: Application Security Verification Standard
Owner: OWASP
Version: 5.0
Status: final
Retrieval date: 2026-09-06
AP concept supported: authN/Z properties for the slice-4-IA audit mapping
Refresh: recheck before the independent audit

Title: Common Weakness Enumeration
Owner: MITRE
Version: 4.16 (taxonomy)
Status: taxonomy
Retrieval date: 2026-09-06
AP concept supported: CWE-287 (login), CWE-639 (session IDOR), CWE-200 (history disclosure)
Refresh: recheck before the independent audit
```

Provider accounting for **this** exchange: inactive (zero calls; network NONE). Slice 4 implementation: same. Slice 5/3b activates the annex with a numerical cap and reason.

---

## 9. Slice sequence (decision-complete enough to issue prompts)

Whole sequence already accepted: 1–3a done at `01ade17`. Do not reopen them.

### Slice 4 — diagnostic session foundation (next mutating prompt)

```text
Evidence tier: E3
Independence required: no (implementer). Acceptance: separate session.
Network: NONE. Provider calls: 0.
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 01ade17f8f0b6786b7a5921a3eaf6ac6c8573d29  (re-gate; if main moved, use then-HEAD)
```

Positive allowlist:

```text
backend/game/models.py
backend/game/migrations/0009_<descriptive>.py          NEW
backend/game/services.py
backend/game/views.py                                 only if a view-level guard is proven necessary; prefer service filter
backend/game/admin.py                                 list_filter + dashboard exclude is_diagnostic
backend/tests/test_diagnostic_session.py              NEW
```

Negative: `backend/gamecore/**` byte-frozen; `frontend/**`; `catalog/**`; `accounts/**` (import `User` only); `config/**`; `position_sets.py` (call `game_from_snapshot`, do not edit); no `run_diagnostic_match`; no admin launcher; no `route.ts`; no `pyproject.toml`; ⛔ no provider call; ⛔ do not print `.env`.

Fail-before (must fail on current HEAD, pass after):

| ID | Claim |
|---|---|
| F-A | vs_ai, `current_turn_slot=0`, `get_ai_context` rack equals **slot 1**, not slot 0 (product identity). |
| F-B | Two `is_ai` seats, `current_turn_slot=1`, `submit_move_for_ai` persists **slot 1** (today: slot 0). |
| F-C | `list_games_for_user` for the service user (or created_by if mistakenly slotted) does not include `is_diagnostic=True`. Ordinary player history unchanged. |
| F-D | `POST /api/auth/login/` for the service username returns 401; `has_usable_password()` is false; `is_staff`/`is_superuser` false; groups/permissions empty. |
| F-E | Ordinary user JWT GET `/api/game/{diagnostic_id}/` is 404. |
| F-F | `abort_diagnostic_run` → `diagnostic_end_reason=model_authorship_failure`, `Move` count unchanged, `_reject_ai_nonscoring` not used (spy/AST or no pass/exchange row). |
| F-G | `create_game` still creates slot 0 `is_ai=False`; `_initialize_session` without seed still assigns `bag_seed`. |
| F-H | `apply_position_snapshot` on a diagnostic session: `current_turn_slot` matches snapshot `to_move_seat_index`; non-diagnostic session rejected. |
| F-I | Diagnostic `current_turn_slot=None` → AI endpoints fail closed (not slot 0). |
| F-J | Register of reserved username after migrate → unique error. |

Gates: documented mypy scope `config game gamecore accounts catalog`; ruff; plain `-m pytest`; RF-16 interpreter `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`. Quote summaries verbatim. Do not run `npm run build`. Baseline at planner time: mypy 88 files / ruff clean / pytest `844 passed, 4 skipped` at `01ade17` (slice-3 closeout). Re-measure after the slice.

Git: explicit paths only; one commit; pre-push `git ls-remote` vs exact baseline; one non-force push. ⛔ Network only for that authorized Git class.

### Slice 4-IA — fresh independent authN/Z audit

Read-only. INFOSEC 4.4. Threat model = §8. No correction. Verdict per claim: verified-closed | not accepted.

### K2 — Node POST-handler probe (already required before slice 5)

Unchanged from accepted plan. Slice 5 must not be written until a plain Node import of the move `POST` is proven or refuted.

### Slice 5 — DiagnosticRun runner + admin launcher (catalog pairs)

Uses the table slice 4 already migrated. argv = `--run-id` only. Live caps: run 200 (Cooperator R4) with instrument subcaps still provisional (K1). Frontend: diagnostic worker `aiSlot` from server `current_turn_slot`. Independent acceptance yes (R3, now including provider-boundary if live).

### Slice 3b — LLM scorer of the committed position set

Depends on slice 4 mount + slice 5 runner. Cap 24 positions with independent request ceiling (K1). Fake default; live only under explicit grant.

Slices 6–8 remain as in accepted D11 (UI, diagnostic target/SSRF, probe history). Do not pull D8 `base_url` into slice 4.

---

## 10. Deviations / risks / missing evidence

- Prompt leftover implementation/Git sections vs plan-only grant — followed AP.
- No public `ls-remote` (forbidden).
- Live authorship rate not re-measured (network NONE); prior whole claim (~zero authored placements) is inherited, not this session’s evidence.
- Whether a partial unique constraint on SQLite test DB plus later PostgreSQL production needs an extra check: Django supports it; implementation tests must create a second queued run and expect IntegrityError.
- `apply_position_snapshot` bag RNG: `game_from_snapshot` restores `_rng` on `TileBag`; Django session stores `bag_tiles` + `bag_seed` but not RNG state today. Mount must persist enough that a later exchange matches F9. If `bag_rng_state` cannot be stored without a GameSession field, **that is a slice-4 migration field** (`bag_rng_state` JSONField, nullable, diagnostic-only use) — add it in 0009 rather than a follow-up gap. Product `create_game` leaves it null.

**Smallest next step:** Orchestrator accepts this plan (or one targeted revision), then issues a **fresh** implementation prompt for slice 4 with `Native planning mode: not-used`, the allowlist in §9, migration **required**, provider calls **0**, and the F-A–F-J fail-before table. Do not start slice 5 or K2 from this report.

**Report justification:** new-evidence

**Authority expiry:** Planning authority expired at this terminal report. This session must not implement, commit, push, archive Meta, or start slice 5. Acceptance of the plan is the Orchestrator’s.

```text
Resolved Execution Issues / Near-Misses: prompt §§5–6 (gates/commit/push) contradicted plan-only identity and Network: NONE. Classified as prompt-vs-AP conflict; AP followed; no mutation.
Pre-Existing Failure Classification: none
```

Orchestration critique:  
MEASURED — Unconditional `acting_slot = current_turn_slot` is **not** behaviour-identical for `is_diagnostic=False`. Product `get_ai_context` ignores turn and always uses first `is_ai` (slot 1). `current_turn_slot` is nullable (`_check_active_turn` already treats `None` as not-your-turn; `get_ai_context` does not). Fourth first-AI site: `validate_move_for_ai`. `_load_vs_ai_session` must keep membership ≠ acting ≠ opponent. Prompt “DiagnosticRun already exists” / “no migration” / `create_game(seed, …)` are false at `01ade17`. Service-user “credential env” conflates Django JWT with Next.js provider env.  
LEAD — Put full `DiagnosticRun` schema + `bag_rng_state` (if required for F9 mount) in slice-4 migration; keep the runner out. Treat service JWT mint as slice-5 privileged I/O, never as a User-stored provider key.

```text
Enumeration widened: first-is_ai sites include validate_move_for_ai and set_game_ai_*; get_ai_context has no _check_active_turn; ai-play-diagnostic.ts aiSlot hardcoded 1; GameSessionAdmin dashboard counts all games; no DiagnosticRun/is_diagnostic symbols in backend/game/models.py; README has no diagnostics section.
```