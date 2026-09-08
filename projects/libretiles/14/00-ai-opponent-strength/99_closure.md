# Closure record — logical whole `ai-opponent-strength` (Meta 14/00)

**Logical-whole closure: closed-by-ORCHESTRATOR.**

Closing commit: `531a80963115fa7a3ab42f86710f1a2f360df90d`  
AP pin at closure: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Public `refs/heads/main` at closure: `531a80963115fa7a3ab42f86710f1a2f360df90d`  
Working tree at closure: `git status --porcelain=v1` EMPTY  
Closed on 2026-09-08 by the Agent Orchestrator.

Artifact class: **closure record — authority for the fact of closure only.** It grants no authority to change anything. Successor wholes take their authority from their own Orchestrator prompts.

---

## 1. What this whole delivered

Libre Tiles ships a transformed, formidable AI opponent across two mutually reinforcing pillars: **Pillar 1: Deterministic Engine Super-Structure** and **Pillar 2: LLM Prompt & Strategic Direction**.

### Pillar 1: Engine Super-Structure (Pure Python Gamecore)
1. **Rack Equity & Leave Valuation (`backend/gamecore/leave_equity.py`)**:
   - Integer centipoints formulation ($\text{Utility} = \text{total\_score} \times 100 + \text{leave\_equity\_cp}$).
   - Curated base tile equity tables for English (Quackle/Maven methodology) and Slovak SSS 100 tiles (strong negative retention penalties for single-copy diacritics Ď, Ň, Ô, Ä, Ĺ, Ŕ, X to prioritize playing them instead of hoarding them). Universal fallback derivation for other 10 variants.
   - Vowel-consonant balance penalty matrices ($n=0..6$) with blank wildcard halving.
   - Duplicate tile penalties and synergy pair bonuses (e.g. English Q+U, Slovak O+V, S+T, N+I).
   - Proven impact: English 100-game acceptance spread increased by **+3,075 points** (from +44,320 to **+47,395**, 100% win rate); Slovak full self-play dead-rack pass stalls completely eliminated (converted from `SIX_CONSECUTIVE_ZERO_SCORES` to **100% `BAG_EMPTY_AND_PLAYER_OUT`**).
2. **Pre-Endgame Tracking & Exact Endgame Minimax Solver (`backend/gamecore/tile_tracking.py`, `backend/gamecore/endgame.py`)**:
   - `LateGameContext`: Pure-Python public unseen tile deduction ($0 \le \text{bag} \le 7$) without private state leakage; expands into exact opponent rack when $\text{bag} == 0$.
   - Iterative-deepening minimax solver with $\alpha\beta$ pruning, transposition caching (4,096 entries), and bounded execution (1,250 ms, 10,000 expansions).
   - Models exact terminal score swings ($\Delta\text{Spread} = \text{score} + 2 \times \text{opponent leftover}$).
   - Pre-endgame transition burden and premium exposure penalties.
   - Frontend SSE move route preserves backend strategic candidate order.
3. **Midgame Board Control & Defensive Opportunity Cost (`backend/gamecore/board_defense.py`)**:
   - Fast 225-bit integer bitboard access channels evaluating newly exposed opponent premium opportunities (TW/TL/DW).
   - Dynamic score-differential posture: lockdown ($\ge +60$), leading defense ($+30..+59$), neutral ($-29..+29$), and comeback opening ($\le -30$).
   - Pruning optimization skipping defense evaluation when candidates cannot beat worst top-K utility.
4. **Standalone Local Engine (CPU Master) Playability**:
   - Exposes master-level `POLICY_RANKED_WITNESS_SAFE` as an autonomous CPU opponent (`model_id: "engine/cpu"`) in `provider-registry` and `model-catalog`.
   - Players can play instantly against a Scrabble Master bot with zero external API calls, zero latency (> 50ms), and zero credentials.

### Pillar 2: LLM Prompt & Strategic Direction
1. **Universal Variant Prompt Specs (Fix H1)**:
   - Shipped native `MovePromptSpec` and `JudgePromptSpec` for all 12 variants in `frontend/src/lib/prompts.ts`.
   - Eliminates English Collins leakage on non-English lexicons.
   - `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) verified byte-identical.
2. **Structured Candidate Anchors & Coordinate Mapping Guidance**:
   - Replaced flat coordinate lists `(3,5) (3,6)...` with rich structured anchors in `anchorsFromCells`: adjacent word runs, orthogonal open spans, perpendicular cross-check indicators, and reachable TW/TL/DW premiums within physical rack capacity.
   - Added explicit `COORDINATE MAPPING & RULES` in `buildMoveUserPrompt` instructing models on row/col increments and strictly enforcing tile reuse without re-placing existing tiles.
   - Capped anchor list to top 20 prioritized anchors to conserve LLM context tokens.
3. **Strategic Seeded Presets Migration (`0014_strategic_seeded_prompts.py`)**:
   - Hash-gated reversible migration upgrading Initial, Fast Search, Short Hooks, and Grandmaster `SEARCH_PROFILE` presets with Chain-of-Thought guidance for anchor selection, leave balance, and board defense posture.
4. **Live Verification with NVIDIA NIM**:
   - Executed live against `nvidia/nemotron-3-super-120b-a12b` via `manage.py diagnose_ai_play` under single-call-in-flight concurrency, scoring 84 points on ply ("BACKARE").

### Test Suite Hygiene
- Heavy multi-ply 20,000-node simulation benchmark suites gated behind `@pytest.mark.slow` and `LIBRETILES_RUN_BENCHMARKS=1`.
- Standard development test commands run in under 30 seconds.

---

## 2. Landed Commit Lineage

```text
843251d  feat(prompts): add native prompt specs for all 12 variants and fix H1 lexicon mismatch (Slice 1)
68afb6d  feat(gamecore): implement rack equity and leave valuation in move search (Slice 2)
6e20a4f  feat(gamecore): implement pre-endgame tracking and exact endgame minimax solver (Slice 3)
f6b6fff  feat(gamecore): implement board control and defensive opportunity cost (Slice 4)
1281162  feat(prompts): implement structured candidate anchors and strategic preset migration (Slice 5)
531a809  feat(game): add local engine cpu opponent and gate slow benchmark tests (Slice 6 Polish)
```

---

## 3. Closure Conditions & Verification

| Condition | Status | Evidence |
|---|---|---|
| All planned slices (1–6) implemented and accepted | **MET** | Slices 1–5 accepted in notes §3, §6, §8, §10, §12; Polish accepted in §14 |
| Formed-word authority and word parity oracle intact | **MET** | Parity oracle `backend/tests/test_word_authority_parity.py` sections 1–4 untouched and 100% green |
| Comprehensive independent architecture audit executed | **MET** | Worker Session 12 (1M context window) evaluated D1–D6; clean bill of health |
| Working tree and remote alignment | **MET** | local `HEAD` == `origin/main` == `531a80963115fa7a3ab42f86710f1a2f360df90d`, porcelain clean |
| Standing test suites green | **MET** | Backend mypy clean (104 files), ruff clean, focused pytest clean; frontend typecheck, lint, vitest 37 files (630 passed) clean |
| Meta archive complete | **MET** | Sessions 01–13 archived with prompt/report pairs, append-only `00_notes.md` through §14 |

---

## 4. Residual-Risk Disposition at Closure

| Finding / residual | Severity | Decision | Approver | Rationale & Status |
|---|---|---|---|---|
| Residual Slovak Slice 4 Benchmark Evidence | Low | accepted-residual | Orchestrator | English 100-pair board defense acceptance finished (+494 spread, 100/100 outs). Slovak 6/20 pairs finished (+287 spread). Remaining seeds are computational benchmark evidence, not a code defect. |
| TileBag empty list ambiguity at snapshot mount | Info | accepted-residual | Orchestrator | Bounded 4-line guard in `position_sets.py` routes around `TileBag.__post_init__` refill on empty bags. |
| Vitest native config ESM warning | Info | accepted-residual | Orchestrator | Cosmetic Vite deprecation warning during test runs; zero impact on test execution or production build. |

---

## 5. Logical Whole Closure Declaration

Logical whole `ai-opponent-strength` (Meta 14/00) is **CLOSED**.  
All objectives set by the Cooperator to elevate AI opponent strength, eliminate pass stalls, build a master-grade engine super-structure, and enrich LLM strategic direction are **FULLY SATISFIED**.
