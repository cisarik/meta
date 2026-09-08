You are a WORKER instance assigned to the persistent AP WORKER role. This is the COMPREHENSIVE INDEPENDENT CODE QUALITY, ARCHITECTURE, AND GAMEPLAY AUDIT session for logical whole `ai-opponent-strength` (Meta 14/00) at baseline commit `128116210a2a9e9394b0e57d3ef037acdd940ccf`. Perform exactly this bounded READ-ONLY audit task and stop. ⛔ You have NO implementation authority, NO correction authority, and NO mutation authority of any kind.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Code Quality and Architecture Audit Worker
Task identity: AIOS-WHOLE-14-COMPREHENSIVE-AUDIT — comprehensive independent architecture, code quality, and gameplay audit across all code landed in Whole 14 (Slices 1 through 5 at commit 128116210a2a9e9394b0e57d3ef037acdd940ccf). Read-only. Provider calls: ZERO.
Phase: audit
Exact baseline: 128116210a2a9e9394b0e57d3ef037acdd940ccf
Independence required: yes
Evidence posture: independent
Evidence tier: E0
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High (1M Context Window Recommended).** The Cooperator explicitly requested a deep, independent, end-to-end audit of all code generated across Whole 14 (Slices 1–5). You must independently inspect the codebase, verify that no spaghetti code, architectural drift, or hidden regressions were introduced, evaluate the pure-CPU gameplay potential, inspect the LLM prompt and anchor quality, and assess test suite hygiene.

## Execution Rules & Invariants

- ⛔ **Read-Only**: Zero mutation. No files created, modified, or deleted in the repository.
- ⛔ **Zero Provider Calls**: Provider calls during this audit are strictly ZERO.
- ⛔ **Command Execution**:
  * Use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`.
  * Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use standard `.venv/bin/python`.
  * `backend/pyproject.toml` already sets `addopts = "-q"`. Never add a second `-q`.
  * ⛔ **Do NOT run heavy multi-seed 100-game benchmark commands** (`LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1` or `LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1`) that take 1–3 hours. Only run fast focused unit test commands (< 30s) if needed for verification.
- ⛔ **Secret Authority**: Never read, print, hash, or measure `backend/.env` or `frontend/.env.local`. Report credential state only as `present: yes|no` plus variable name.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1773-1810      the Defensive-Security Task Anchor
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and coordinate fields you echo
PROMPT_CONTRACTS.md:423-453 coordinate consistency and Worker Exchange Identity
PROMPT_CONTRACTS.md:203     phase-qualified result (`not-applicable` for audit)
AP.md:2453-2454      the CLOSED report-justification enum: `new-evidence`.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — Scope of Whole 14

```text
/home/agile/Projects/libretiles/AGENTS.md
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/00_handout.md
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/00_notes.md
```

Then inspect by symbol and module all new/modified files from Whole 14:
1. **Slice 1 (Variant Prompts & H1 Fix)**:
   `frontend/src/lib/prompts.ts` (12 variant specs, dispatch maps)
   `frontend/src/lib/prompts.test.ts`
   `frontend/src/app/api/ai/move/route.ts` (tool description)
2. **Slice 2 (Rack Equity & Leave Valuation)**:
   `backend/gamecore/leave_equity.py` (integer centipoints, profiles, V/C balance, duplicates, synergy)
   `backend/gamecore/move_search.py` (utility ranking, `leave_equity_cp`)
   `backend/tests/test_leave_equity.py`
   `backend/tests/test_slovak_strength.py`
3. **Slice 3 (Pre-Endgame Tracking & Exact Endgame Minimax Solver)**:
   `backend/gamecore/tile_tracking.py` (`LateGameContext`, unseen pool subtraction)
   `backend/gamecore/endgame.py` (minimax solver, alpha-beta pruning, terminal swing valuation)
   `backend/game/services.py` (`_probe_ai_ranked_candidates`)
   `frontend/src/app/api/ai/move/route.ts` (`mergeCandidateRecommendations` strategic order preservation)
   `backend/tests/test_tile_tracking.py`, `backend/tests/test_endgame.py`, `backend/tests/test_pre_endgame.py`
4. **Slice 4 (Board Control & Defensive Opportunity Cost)**:
   `backend/gamecore/board_defense.py` (premium exposure bitboards, posture thresholds, access channels)
   `backend/gamecore/move_search.py` (`evaluation_cp`, `defense_penalty_cp`, `StrategyMode.board_control`)
   `backend/gamecore/selfplay.py` (`player_board_defense_enabled`)
   `backend/tests/test_board_defense.py`, `backend/tests/test_board_defense_services.py`
5. **Slice 5 (Structured Candidate Anchors & Strategic Presets)**:
   `frontend/src/lib/prompts.ts` (rich structured anchors in `anchorsFromCells`, coordinate mapping guidance)
   `frontend/src/lib/prompts.baseline.fixture.ts` (test-only frozen byte oracle)
   `backend/catalog/migrations/0014_strategic_seeded_prompts.py` (hash-gated preset upgrade)
   `backend/tests/test_strategic_seeded_prompts_migration.py`

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 128116210a2a9e9394b0e57d3ef037acdd940ccf
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Deliverables Required

Provide a comprehensive, evidence-dense audit report addressing the following 6 core areas:

### D1: Code Hygiene, Architectural Layering, and "Spaghetti" Analysis
- **Layering Integrity**: Does `backend/gamecore/` remain completely pure Python with ZERO imports from `backend/game/` or Django?
- **Modularity & Separation of Concerns**: Are the newly introduced modules (`leave_equity.py`, `tile_tracking.py`, `endgame.py`, `board_defense.py`) clean, decoupled, and well-structured?
- **Data Integrity & Determinism**: Are all calculations deterministic? (Verify: integer centipoints, fixed-point math, no non-deterministic floats, canonical placement key tie-breaking).
- **Dead Code or Drift**: Are there any abandoned functions, redundant helpers, or dead code remnants?

### D2: Game Invariants and Formed-Word Legality
- **The ONE Formed-Word Authority**: Confirm that `WordAuthority.accepts_tokens` remains the sole legality certifier and that no scoring path or heuristic bypasses it.
- **Parity Oracle**: Confirm that sections 1–4 of `backend/tests/test_word_authority_parity.py` remain untouched and green.
- **Variant Invariants**: Confirm that SSS 100 Slovak tiles, 12 variant definitions, multigraph token handoffs, and blank assignments score zero points as required.

### D3: Engine / CPU Standalone Playability Analysis
The Cooperator asked: *"Dokazal by Libre Tiles hrat proti userovi aj bez API volani? ... v Settings mat moznost nastavit hru proti CPU"*.
Analyze:
- Can the newly enhanced gamecore engine play directly as a standalone "CPU opponent" without external LLM API calls?
- Which policy (`POLICY_RANKED_WITNESS_SAFE` or `POLICY_RANKED_BEST`) provides this capability?
- What would be the exact technical seam to expose a "CPU / Pure Engine" opponent in Django `PlayerSlot` or frontend game settings? (Describe how straightforward this is, e.g. slot with `is_ai=True, ai_model=None` resolving to engine ranked search).
- What strength level does this pure engine currently exhibit? (Cite the 100-game spread +47,395, 100% win rate against first-witness baseline, and 100% `BAG_EMPTY_AND_PLAYER_OUT` completion).

### D4: LLM Integration, Prompt Engineering, and Anchor Quality
- **Structured Anchors Evaluation**: Inspect `frontend/src/lib/prompts.ts`. How effective is the new structured anchor output compared to the old flat coordinate list?
- **Coordinate Mapping Guidance**: Does `buildMoveUserPrompt` give models sufficient guidance on row/col increments and reusing existing tiles?
- **System Prompt Preservation**: Verify that `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) is byte-identical and uncompromised.
- **Strategic Presets**: Verify migration `0014_strategic_seeded_prompts.py` text and hash-gating.

### D5: Test Suite Hygiene & Runtime Performance
- **Heavy vs Fast Tests**: The Cooperator observed tests running for hours when `LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1` was invoked. Audit the test suite structure:
  * Fast unit tests (< 15 seconds) vs opt-in acceptance matrices.
  * Confirm that standard developer commands (`pytest`) only run fast tests and that long-running multi-seed benchmarks require explicit opt-in env vars (`LIBRETILES_RUN_*`).
- **Search Latency**: Confirm that midgame search and live probe execution remain well within the 750 ms / 1,250 ms live limits.

### D6: Findings, Technical Debt, and Recommendations
- List any identified defects, near-misses, code smells, or technical debt across Whole 14, classified by severity:
  * Critical / Blocker (0 expected)
  * Medium / Material
  * Minor / Clean-up
- Provide actionable, concrete recommendations for follow-up polishing.

## 3. Verification Commands (Read-Only)

Run fast verification gates only (do NOT run multi-hour opt-in benchmarks):

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strategic_seeded_prompts_migration.py tests/test_tile_tracking.py tests/test_endgame.py tests/test_leave_equity.py tests/test_board_defense.py
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/prompts.test.ts src/lib/atomic-tiles.test.ts
```

## 4. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 12, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `not-applicable`
- Start commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf`
- End commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf` (zero mutation)
- Changed files and purpose: `none — this exchange mutates nothing`
- Commit/push result: `not-applicable`
- Resolved Execution Issues / Near-Misses: `none`
- Pre-Existing Failure Classification: `none`

Then provide deliverables **D1 through D6, labelled, in that order.**

Include the two analytical fields:
```text
Orchestration critique: none | <findings> (labelled MEASURED and LEAD)
Enumeration widened: none | <surfaces not reached>
```

Conclude with:
- Exactly one `Report justification`: `new-evidence`
- One authority-expiry statement.
- One smallest next step.
