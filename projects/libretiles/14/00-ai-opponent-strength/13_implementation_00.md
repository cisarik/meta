You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S6-CPU-OPPONENT-AND-TEST-HYGIENE — implement the "Local Engine (CPU Master)" opponent option in catalog/selection and frontend move route (allowing instant zero-API play), cap structured anchors in prompts.ts to top 20, and gate slow multi-minute benchmark simulation tests in backend/tests/ behind LIBRETILES_RUN_BENCHMARKS to restore fast standard pytest execution (< 30s), land one commit, push, and read back.
Phase: implementation
Exact baseline: 128116210a2a9e9394b0e57d3ef037acdd940ccf
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: bounded reversible mutation across catalog selection, provider registry, frontend move route, anchor formatting, and test gating. No external network beyond authorized Git push, no provider spend, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named task: Following the comprehensive audit in Session 12, this polish slice implements two high-value deliverables: (1) exposes the master-level gamecore engine as a standalone "Local Engine (CPU Master)" opponent (`model_id: "engine/cpu"`), allowing players to play against a master bot instantly with zero external API calls or keys; (2) gates the heavy multi-minute simulation benchmark tests behind `LIBRETILES_RUN_BENCHMARKS=1` and `@pytest.mark.slow`, so standard development `pytest` runs in under 30 seconds; (3) caps `anchorsFromCells` to the top 20 prioritized anchors to conserve LLM context window tokens on dense boards.

## Execution Rules & Environment Invariants

- ⛔ **RF-16 Mandatory Deviation**: Cursor AppImage intercepts `python*`. Always use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`. Never use ambient `python`, `python3`, or `poetry run`.
- ⛔ **Testing Rule**: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use standard `.venv/bin/python`.
- ⛔ **Pytest Warning**: `backend/pyproject.toml` already sets `addopts = "-q"`. Never add a second `-q`.
- ⛔ **Word Authority Invariant**: Formed-word legality is determined solely by `WordAuthority.accepts_tokens`. Sections 1–4 of `test_word_authority_parity.py` are the untouchable test oracle.
- ⛔ **CORE SHA-256 Invariant**: `MOVE_SYSTEM_PROMPT` in `frontend/src/lib/prompts.ts` must remain byte-identical so `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) does not change.

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
backend/catalog/selection.py                             select_models_from_rows, get_selectable_models, is_selectable_model.
frontend/src/lib/provider-registry.ts                    EXACT_PROVIDER_METADATA, isValidRuntimePair.
frontend/src/app/api/ai/move/route.ts                    handling of move execution and candidates.
frontend/src/lib/prompts.ts                              anchorsFromCells (top anchor formatting).
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/12_report_00.md comprehensive audit report (D3, D5, D6).
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 128116210a2a9e9394b0e57d3ef037acdd940ccf
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these 13 paths:
1. `backend/catalog/migrations/0015_add_engine_cpu_model.py` (new migration seeding engine/cpu model)
2. `backend/catalog/selection.py`
3. `backend/tests/test_engine_cpu_model_migration.py` (new test suite)
4. `frontend/src/lib/provider-registry.ts`
5. `frontend/src/lib/provider-registry.test.ts`
6. `frontend/src/app/api/ai/move/route.ts`
7. `frontend/src/app/api/ai/move/route.test.ts`
8. `frontend/src/lib/prompts.ts`
9. `frontend/src/lib/prompts.test.ts`
10. `backend/tests/test_board_defense_benchmark.py`
11. `backend/tests/test_endgame_benchmark.py`
12. `backend/tests/test_slovak_strength.py`
13. `backend/tests/test_strength_benchmark.py`

⛔ Any mutation outside this allowlist is strictly unauthorized.

## 3. Implementation Specifications

### 3.1 Catalog Migration & Selection for "Local Engine (CPU Master)"
1. **Migration `0015_add_engine_cpu_model.py`**:
   - Depends on `("catalog", "0014_strategic_seeded_prompts")`.
   - Forward: Creates an `AIModel` row:
     * `provider`: `"engine"`
     * `model_id`: `"engine/cpu"`
     * `display_name`: `"Local Engine (CPU Master)"`
     * `description`: `"Autonomous deterministic game engine with rack equity, endgame solver, and board defense. Zero API keys required."`
     * `model_type`: `"language"`
     * `is_active`: `True`
     * `sort_order`: `0`
     * `tags`: `["tools"]`
   - Reverse: Deletes the created row.
2. **`backend/catalog/selection.py`**:
   - In `select_models_from_rows`:
     Include active `engine` provider models in the returned list:
     ```python
     engine_models = [
         model for (provider, _), model in active.items() if provider == "engine"
     ]
     return _without_duplicate_pairs([*engine_models, *direct, *compatibility])
     ```
   - This ensures `get_selectable_models()` returns the engine model at the top, and `is_selectable_model("engine/cpu")` returns `True`.
3. **`backend/tests/test_engine_cpu_model_migration.py`**:
   - Test forward migration creates the model, `is_selectable_model("engine/cpu")` is True, reverse removes it.

### 3.2 Provider Registry & Route Handling (`frontend/`)
1. **`frontend/src/lib/provider-registry.ts`**:
   - Export:
     ```typescript
     export const ENGINE_PROVIDER = "engine" as const;
     export const ENGINE_CPU_MODEL_ID = "engine/cpu" as const;
     ```
   - In `EXACT_PROVIDER_METADATA`:
     Add entry:
     ```typescript
     {
       provider: ENGINE_PROVIDER,
       model_id: ENGINE_CPU_MODEL_ID,
       provider_label: "Local Engine",
       model_label: "CPU Master",
       catalog_tier: "direct",
       runtime_kind: "openai-compatible",
     },
     ```
   - Update `provider-registry.test.ts` to assert `isValidRuntimePair("engine", "engine/cpu") === true`.
2. **`frontend/src/app/api/ai/move/route.ts`**:
   - In `executeStream()`:
     Detect when `runtimePair.provider === "engine"`:
     * Emit thinking event:
       ```typescript
       emit({
         type: "thinking",
         model: "engine/cpu",
         runtime_model: "engine/cpu",
         status: "searching",
         message: "Calculating optimal master move...",
         provider_path: "engine",
       });
       ```
     * Directly fetch backend candidates:
       `const candidatesResult = await fetchAiCandidates(game_id, token);`
     * If candidate placement exists:
       Commit the top candidate placement:
       `const commitResult = await commitMove(game_id, candidatesResult.candidates[0].placements, token);`
       Emit finishMove and terminal event:
       ```typescript
       emit({
         type: "finishMove",
         ready: true,
         completion_source: "backend_ranked_candidate",
         score: candidatesResult.candidates[0].total_score,
         words: candidatesResult.candidates[0].words,
       });
       emit({
         type: "terminal",
         completion_source: "backend_ranked_candidate",
         turn_provider_requests_used: 0,
         score: candidatesResult.candidates[0].total_score,
       });
       ```
     * If no legal moves available (pass/exchange needed):
       Execute playability check / exchange / pass.
     * Close stream! Total execution time: ~20-50ms. Zero LLM calls, zero API keys needed!
   - In `frontend/src/app/api/ai/move/route.test.ts`:
     Add unit test for `engine/cpu` move turn verifying direct candidate fetch and commitment.

### 3.3 Anchor Cardinality Cap (`frontend/src/lib/prompts.ts`)
1. In `anchorsFromCells(rows: BoardCell[][])`:
   Cap the formatted anchors to the top 20 prioritized entries:
   ```typescript
   return candidates.slice(0, 20).map(formatAnchor).join("\n");
   ```
   (This addresses audit finding m1, preventing token bloat on dense boards while retaining the best hook and premium opportunities).
2. Ensure `prompts.test.ts` tests continue to pass and `CORE_SHA256` remains byte-identical.

### 3.4 Test Suite Hygiene: Gating Slow Benchmarks
In `backend/tests/`:
1. In `test_board_defense_benchmark.py`:
   Add `@pytest.mark.slow` and `@pytest.mark.skipif(os.environ.get("LIBRETILES_RUN_BENCHMARKS") != "1", reason="set LIBRETILES_RUN_BENCHMARKS=1 to run full game simulation benchmarks")` to:
   - `test_default_paired_benchmark_terminates_and_engages_board_control`
2. In `test_endgame_benchmark.py`:
   Add `@pytest.mark.slow` and `@pytest.mark.skipif(os.environ.get("LIBRETILES_RUN_BENCHMARKS") != "1", reason="set LIBRETILES_RUN_BENCHMARKS=1 to run full game simulation benchmarks")` to:
   - `test_default_paired_endgame_benchmark_terminates_and_reaches_player_out`
3. In `test_slovak_strength.py`:
   Add `@pytest.mark.slow` and `@pytest.mark.skipif(os.environ.get("LIBRETILES_RUN_BENCHMARKS") != "1", reason="set LIBRETILES_RUN_BENCHMARKS=1 to run full game simulation benchmarks")` to:
   - `test_slovak_ranked_strategy_beats_witness_on_default_seeds`
   - `test_slovak_ranked_selfplay_terminates_with_tile_conservation`
4. In `test_strength_benchmark.py`:
   Add `@pytest.mark.slow` and `@pytest.mark.skipif(os.environ.get("LIBRETILES_RUN_BENCHMARKS") != "1", reason="set LIBRETILES_RUN_BENCHMARKS=1 to run full game simulation benchmarks")` to:
   - `test_ranked_strategy_beats_first_witness_on_default_balanced_seeds`
   - `test_node_bound_strength_regression_tuples`
5. Verify that a bare `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest` runs all standard unit and service tests in under **30 seconds**!

## 4. Verification Procedures

Execute and ensure clean exit (0) on:

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```
(Confirm `pytest` exits 0 cleanly in under 30 seconds!)

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/provider-registry.test.ts src/lib/prompts.test.ts src/app/api/ai/move/route.test.ts
```

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add backend/catalog/migrations/0015_add_engine_cpu_model.py \
        backend/catalog/selection.py \
        backend/tests/test_engine_cpu_model_migration.py \
        frontend/src/lib/provider-registry.ts \
        frontend/src/lib/provider-registry.test.ts \
        frontend/src/app/api/ai/move/route.ts \
        frontend/src/app/api/ai/move/route.test.ts \
        frontend/src/lib/prompts.ts \
        frontend/src/lib/prompts.test.ts \
        backend/tests/test_board_defense_benchmark.py \
        backend/tests/test_endgame_benchmark.py \
        backend/tests/test_slovak_strength.py \
        backend/tests/test_strength_benchmark.py

git diff --staged --stat
```

Commit message:
```bash
feat(catalog): add local engine cpu opponent and gate slow benchmark tests
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "128116210a2a9e9394b0e57d3ef037acdd940ccf"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Standard `pytest` fails or takes longer than 60 seconds without `LIBRETILES_RUN_BENCHMARKS`.
- `CORE_SHA256` fails to match the unchanged system prompt core.
- Pre-push verification reveals remote diverged from `128116210a2a9e9394b0e57d3ef037acdd940ccf`.

## 7. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 13, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf`
- End commit: `<exact SHA>`
- Changed files and purpose (explicit paths)
- Verification that standard `pytest` runtime is now < 30s
- Gate summaries (mypy, ruff, full pytest, vitest)
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
