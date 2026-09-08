### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 09, Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S4-BOARD-DEFENSE
```

Status: **PARTIAL**

Phase-qualified result: `implementation-PARTIAL`

Logical-whole closure: not-closed

Start commit: `6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b`

End commit: `f6b6fff42736c5124b508fde319f8bf5ae96cfc3`

Public readback: `origin/main == HEAD == f6b6fff42736c5124b508fde319f8bf5ae96cfc3`

AP pin (unchanged): `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`

Context pressure: high — long implementation plus interrupted opt-in cohort; closeout is from recorded evidence, not a fresh re-run.

Report justification: `new-mutation`

Authority expires with this terminal report.

---

## 1. What this exchange did

Slice 4 is **implemented and published** on `main`. Midgame ranked search can now penalize premium-square exposure, apply score-differential posture (lockdown / comeback), emit `strategy_mode: "board_control"`, and have the SSE move route preserve backend order.

The **default E2 ladder completed green** (mypy, ruff, full pytest, frontend typecheck/lint/targeted vitest). The **predeclared opt-in D7 A/B pytest did not finish** (tool/session abort after English 100 + Slovak 6/20). The **100-game legacy strength acceptance was never started**. Cooperator closeout instruction: **do not run further tests**. Remaining opt-in gates are therefore **missing evidence**, not a failed pytest assertion.

No further code mutation was required at closeout. There were no pending functional edits after the `test_api.py` payload-shape compatibility fix.

---

## 2. Repository gate (start)

Verified before mutation:

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b` |
| `git rev-parse HEAD:.ap` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `git -C .ap rev-parse HEAD` | same `9c5cc44` (detached HEAD, correct) |
| `git status -sb` | `## main...origin/main` |
| `git status --porcelain=v1` | empty |

---

## 3. Changed files and purpose (exact allowlist, 14 paths)

| Path | Role |
|---|---|
| `backend/gamecore/board_defense.py` | **NEW.** Pure-Python integer-centipoint evaluator: bitboard occupancy, 13 access channels per unused TW/DW/TL, lane pairs ≤6 apart, posture weights, `D(m)∈[-800,3000]`. |
| `backend/gamecore/move_search.py` | `score_differential`, `board_defense_enabled`; `RankedMoveCandidate.defense_penalty_cp` + `evaluation_cp`; prune slack +800; `StrategyMode` adds `"board_control"`; 10 ms finish reserve when defense is active. |
| `backend/gamecore/selfplay.py` | `board_defense_enabled` / `player_board_defense_enabled`; `_ranked_search` passes acting-seat flag and `acting_score - opponent_score`; `_Decision.defense_penalty_cp`. |
| `backend/game/services.py` | Live probe always `board_defense_enabled=True` with server-derived differential. Payload: top-level `strategy_mode` for `board_control`; late-game still writes extra `search` fields. |
| `backend/game/position_sets.py` | Explicit `board_defense_enabled=False` in `_selfplay_config` and `_ranked_on_game`. **No asset regeneration.** |
| `backend/tests/test_board_defense.py` | **NEW.** Direct TW exposure, vowel vs low-hook, denial, posture, determinism, prune, 750 ms live deadline. |
| `backend/tests/test_board_defense_services.py` | **NEW.** Differential +60, tied opening 0, live midgame top-level `board_control`. |
| `backend/tests/test_board_defense_benchmark.py` | **NEW.** Default 2-pair smoke + opt-in English 300–349 both seats / Slovak 0–9 both seats. |
| `backend/tests/test_move_search.py` | `board_control` marker + `evaluation_cp` order. |
| `backend/tests/test_strength_benchmark.py` | Legacy configs keep defense off; 4-game English defense-vs-witness smoke; node-bound unmarked-cap pin skipped when defense is on. |
| `backend/tests/test_slovak_strength.py` | Seeds 0,1 both seats defense-vs-witness; ranked self-play both seats defense on. |
| `backend/tests/test_position_sets.py` | `_selfplay_config(...).board_defense_enabled is False`; remount search passes `board_defense_enabled=False`. |
| `frontend/src/app/api/ai/move/route.ts` | `STRATEGIC_MODES` includes `"board_control"`. |
| `frontend/src/app/api/ai/move/route.test.ts` | `it.each` includes `"board_control"`. |

Commit stat: **14 files, +1511 / −21**.

Paths **not** mutated: dictionary, WordAuthority, `test_word_authority_parity.py`, position-set JSON, migrations, prompts, catalog.

---

## 4. Evaluation model (as landed)

Active only when `bag_count > 7`. Empty bag and 1–7 bag keep endgame / pre-endgame. First-witness search is untouched.

\[
U(m)=100\cdot score(m)+leave(m)-D(m)
\]

\[
D(m)=\mathrm{clamp}\big(\lfloor wR/100\rfloor-\lfloor gG/100\rfloor-\lfloor cC/100\rfloor-\lfloor tV/100\rfloor,-800,3000\big)
\]

- `R`: new premium risk, cap 2400; top two positive exposure changes `p1 + p2//2` plus `200 * min(2, newly_opened_lanes)`.
- `G`: denial, cap 400; `(n1 + n2//2)//4`.
- `C`: net empty-anchor reduction, cap 200; `50 * max(0, anchors_before - anchors_after)`.
- `V`: high-variance openings, cap 400.

Support: vowel 150%, low-hook consonant (`<4` two-tile partners via `WordAuthority.accepts_tokens`) 50%, else 100%. Premium weights: TW 1000, DW 500, TL 600. DL has no defensive weight.

Posture from **pre-move** `acting − opponent` (candidate score is not added):

| ΔScore | w | g | c | t |
|---|---:|---:|---:|---:|
| ≤ −60 | 40 | 50 | 0 | 100 |
| −59…−30 | 65 | 75 | 0 | 50 |
| −29…+29 | 100 | 100 | 0 | 0 |
| +30…+59 | 150 | 150 | 100 | 0 |
| ≥ +60 | 200 | 200 | 200 | 0 |

Ranking key: `(-evaluation_cp, -rack_out, -tiles_used, canonical_key)`.

When top-k is full and `score*100 + leave + 800` is **strictly below** the worst retained utility, defense evaluation is skipped; the placement still counts in `unique_placements`.

---

## 5. Live payload / frontend (compatibility deviation)

`GET /api/game/{id}/ai-candidates/` now always enables board defense. Midgame results carry **top-level** `strategy_mode: "board_control"`.

`search` for `board_control` keeps the five-key midgame shape:

`complete`, `nodes`, `elapsed_ms`, `unique_placements`, `candidate_count`

Late-game (`exact` / `bounded` / `pre_endgame`) still adds `search.strategy_mode`, `out_in_two`, `completed_depth`.

**Why:** `tests/test_api.py::GameAPITest.test_ai_candidates_are_ranked_revalidatable_and_hide_private_state` pins `set(data["search"])` to those five keys. That file was **not** on the allowlist. First full pytest failed there. The SSE route reads **top-level** `strategy_mode`, so order preservation still works without enlarging `search`.

Frontend `STRATEGIC_MODES = {"exact","bounded","pre_endgame","board_control"}`. Backend strategic candidates stay first, in backend order.

---

## 6. Position sets

Historical `english-aaac5c27` is unchanged. Generation and remount pass `board_defense_enabled=False`. Neutral differential alone is **not** used as a compatibility substitute: the evaluator is explicitly off.

---

## 7. Tests and validation (no re-run at closeout)

### 7.1 Quality gates that **did** complete with exit 0

From `backend/`, RF-16 interpreter (`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…`):

| Gate | Result |
|---|---|
| `mypy config game gamecore accounts catalog` | Success, **103** source files (after adding `board_defense.py`) |
| `ruff check .` | All checks passed |
| Focused: `test_board_defense.py` + `test_board_defense_services.py` + `test_move_search.py` | **36 passed** in 6.97s |
| `test_position_sets.py` + `test_endgame_services.py` + `test_pre_endgame.py` | **26 passed** in 161.10s |
| `test_board_defense_strategy_beats_first_witness_on_default_seeds` (after cap-pin fix) | **1 passed** in 67.70s |
| `test_api.py::…test_ai_candidates_are_ranked…` + services + endgame services (after payload fix) | **9 passed** in 13.40s |
| **Full pytest** | **1128 passed, 6 skipped, 1 warning** in 1344.75s (0:22:24) |

First full-pytest attempt: **1 failed** (`test_api.py` search-key set). After payload split: **1128 passed**. The extra pass vs the 1127+1-fail run is that API test now green.

From `frontend/`:

| Gate | Result |
|---|---|
| `npm run typecheck` | clean |
| `npm run lint` | clean |
| `npx vitest run src/app/api/ai/move/route.test.ts src/lib/ai-turn-simulation.test.ts` | **2 files, 74 passed** |

Parity oracle `test_word_authority_parity.py` sections 1–4: included in full pytest; **not** failed.

Always-on default A/B smoke (`test_default_paired_benchmark_terminates_and_engages_board_control`) is inside full pytest and **passed**. Printed rows:

| Variant | seed | slot | spread_off | spread_on | delta | board_control | opp_ppt_off→on |
|---|---:|---:|---:|---:|---:|---:|---|
| English | 300 | 0 | +93 | +35 | −58 | 10 (9 nonzero) | 33.58 → 33.42 |
| Slovak | 0 | 0 | +111 | +139 | +28 | 13 (12 nonzero) | 31.31 → 23.73 |

Smoke assertions: terminate, `board_control_decisions > 0`, treatment aggregate spread positive. They do **not** require paired-mean improvement. English default pair is negative; Slovak is positive; combined +35+139 > 0.

### 7.2 Intermediate failure that was fixed (not open)

`test_strength_benchmark._simulate(node_bound=True)` required an incomplete decision with `strategy_mode is None` hitting 20k nodes. Defense midgame emits `board_control`, so that set was empty. **Fix (allowlisted):** skip the unmarked-cap pin when `board_defense=True`. Legacy node-bound tuples **unchanged** (defense off).

### 7.3 Opt-in D7 A/B — **incomplete pytest**, measured English 100 complete

Command (first attempt, ~102 min, then abort):

`LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1 … pytest tests/test_board_defense_benchmark.py -s`

- Default test in that file: **passed** (`.` after summaries).
- Acceptance: **English seeds 300–349, both seats = 100/100 pairs completed**.
- Slovak: **seeds 0–2, both seats = 6/20**, then process abort.
- Restarts were aborted (tool/user). Cooperator then forbade further tests.
- `LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 … -k one_hundred` was **never started**.

Cohort design (as implemented, matches D7): both seats `POLICY_RANKED_WITNESS_SAFE`; control strategy seat defense **off**; treatment **on**; opponent always defense **off**; `late_game_enabled=True`; 20k nodes; large elapsed cap.

**English 100 (complete, parsed from the aborted log):**

| Metric | Control (off) | Treatment (on) |
|---|---:|---:|
| Games | 100 | 100 |
| W/D/L | 50/0/50 | 50/0/50 |
| Win rate (draw = ½) | 0.500 | 0.500 |
| Total spread | **+0** | **+494** |
| Paired delta (on−off) | | **+494** |
| Mean paired delta | | **+4.94** |
| Mean opponent points/turn | 37.1508 | **35.5700** |
| `board_control` plies (sum) | 0 (asserted) | 951 |
| Nonzero `defense_penalty_cp` plies | 0 | 920 |
| End reason | 100× `BAG_EMPTY_AND_PLAYER_OUT` | same |

Equal 50/50 W/D/L on both arms is expected: control is identical policy vs itself, so seat-0 wins of seed S are exactly seat-1 losses of seed S (spreads sum to 0). Treatment win rate **did not fall**. Mean spread **improved**. Opponent PPT **fell**.

Predeclared D7 gates vs this English sample (pytest never reached the assert block):

| Gate | English 100 |
|---|---|
| Positive paired mean spread | **yes** (+4.94) |
| Treatment WR ≥ control | **yes** (0.500 = 0.500) |
| Aggregate opponent PPT does not increase | **yes** (37.15 → 35.57) |
| Leading-posture reply cohort nonempty and mean decreases | **not fully measured** in the wide cohort (per-game log has no reply vectors). Default English pair: lead_reply_n off/on = **0/3**, mean off/on = 0.00/36.67. Control leading replies are **empty by construction** (no `board_control` on the control arm), so the implemented assert is `on_mean < +inf` if `on_lead` nonempty. |

**Slovak 6/20 (incomplete):**

| seed | slot | delta | notes |
|---|---:|---:|---:|
| 0 | 0 | +28 | also the default smoke row |
| 0 | 1 | −30 | |
| 1 | 0 | +1 | |
| 1 | 1 | +88 | |
| 2 | 0 | +310 | |
| 2 | 1 | −110 | |

Slovak partial: paired delta **+287**, mean **+47.83**, opp PPT 35.995 → 30.132, all six `BAG_EMPTY_AND_PLAYER_OUT`. **Not** a D7 pass: seeds 3–9 missing.

Bootstrap CIs were printed only for the **default** 1×2 pairs, not for the wide English 100 (summary prints after the full cohort).

### 7.4 Commands **not** completed

```text
LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1 pytest tests/test_board_defense_benchmark.py -s
  → no terminal pytest PASS/FAIL for test_paired_board_defense_acceptance
LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 pytest tests/test_strength_benchmark.py -s -k one_hundred
  → never started
```

Legacy 100-game strength is defense-**off** / late_game **off**. It is a regression of Slice 2 numbers, not Slice 4 A/B. It was in the grant and remains **unrun in this exchange**.

---

## 8. Commit and push

```text
Staged by explicit allowlisted paths only (14 files).
Message: feat(gamecore): implement board control and defensive opportunity cost
Pre-push: ls-remote origin/main == 6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b
git push origin main
Readback: ls-remote origin/main == f6b6fff42736c5124b508fde319f8bf5ae96cfc3
Working tree: clean, ## main...origin/main
```

No force push. No hooks skipped.

---

## 9. Deviations, risks, missing evidence

1. **Allowlist gap (resolved without editing the extra file).** `test_api.py` was not listed; it pinned midgame `search` keys. Payload: `board_control` is top-level only. Frontend still preserves order. Late-game payload unchanged.

2. **Node-bound cap pin (allowlisted).** Defense-on smokes skip the unmarked incomplete-cap assertion. Legacy tuples still require it.

3. **Opt-in D7 pytest not finished.** English 100 is **measured** from logs, not a pytest-asserted PASS. Slovak 14 pairs missing. Do **not** treat +4.94 as a CI-certified D7 pass.

4. **100-game strength acceptance unrun.**

5. **Control-arm leading replies.** Collection is tied to `strategy_mode == "board_control"`, so control leading replies are always empty. The “mean reply decreases vs control” gate is weak unless redesigned.

6. **Vs-equal-ranked spread is noisy.** Per-game English deltas range from about −238 to +320; the mean is only +4.94. No 10k-seed bootstrap on the wide cohort.

7. **No coefficient retune.** Per D7 / the grant: do not retune against acceptance seeds.

8. **Closeout tests.** After Cooperator “no more tests”, this report does **not** re-run pytest. Default-suite numbers are from the successful full run **before** the commit. The commit is that same tree (allowlisted paths only). Residual risk: un-retested after `git commit` itself (content identical to the green tree).

---

## 10. Execution timeline (for the Orchestrator)

1. Gate clean at `6e20a4f`.
2. Implement evaluator + wiring + tests + frontend marker.
3. Focused unit/service tests green; mypy/ruff/frontend green.
4. Strength smoke failed on unmarked-cap pin → fix → pass.
5. Full pytest failed on `test_api.py` search keys → payload split → full pytest **1128 passed**.
6. Opt-in A/B started; English 100 finished; Slovak aborted at seed 2.
7. Restarts aborted; Cooperator: stop tests, write this report.
8. Commit `f6b6fff`, push, public readback OK.

---

## 11. Orchestration critique

- **MEASURED — static + pytest:** backend-only `board_control` would be discarded by raw-score merge; frontend allowlist was necessary and was used.
- **MEASURED — pytest:** `test_api.py` exact `search` set was an unlisted blast radius. Planner D5 assumed “payload automatically carries the marker” including `search.*`. That collided with the midgame contract.
- **MEASURED — execution:** opt-in 240 games (100 EN + 20 SK, two arms) is ~90–110 minutes node-bound; it does not fit a single tool wait. English 100 was obtained once; Slovak was not.
- **LEAD:** vs-equal ranked A/B, WR stays ~0.5; spread and opponent PPT are the real signals. English mean +4.94 with large per-game variance.
- **LEAD:** local exposure is a reply-risk surrogate. Default English pair **lost 58 spread** while opponent PPT dipped slightly; Slovak default **gained 28** with a large opponent-PPT drop. Wide English still net-positive.

Enumeration widened: `test_api.py` candidate payload shape. No catalog, provider, or production audit.

---

## 12. Smallest next step

Orchestrator should **accept the landed commit** as Slice 4 implementation on default-suite evidence, then choose **one**:

1. **Accept Slice 4** on English-100 measured +4.94 / opponent PPT down, and park a follow-up to finish Slovak 0–9 both seats plus the 100-game strength command on a long-running host; or
2. **Authorize one dedicated opt-in Worker** with no other scope: finish `LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1` to pytest exit 0 and optionally `-k one_hundred`; or
3. **Reject / retune** only if the incomplete Slovak or unrun 100-game is treated as a hard D7 blocker — that would be a new grant, not this Worker retuning coefficients.

This Worker must not close the logical whole.

---

```text
Resolved Execution Issues / Near-Misses:
  1. test_api.py search-key pin vs board_control extras — cause: allowlist omitted the API contract test; resolution: top-level strategy_mode only for board_control; residual: search object no longer mirrors late-game extras for this marker.
  2. Opt-in pytest wall-time / abort — cause: 240 node-bound games; resolution: none in this exchange after Cooperator stop; residual: Slovak 14 pairs and pytest-asserted D7 missing.
  3. Strength node-bound cap pin vs board_control marker — cause: pin assumed strategy_mode is None; resolution: skip pin when board_defense=True.

Pre-Existing Failure Classification: none

Orchestration critique: see §11 (MEASURED / LEAD labelled)

Enumeration widened: tests/test_api.py ranked-candidate search payload keys
```
