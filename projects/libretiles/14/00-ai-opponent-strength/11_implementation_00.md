You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S5-ANCHORS-AND-STRATEGY — implement structured candidate anchors in frontend/src/lib/prompts.ts with rich hook context (adjacent letters, direction, open spans, reachable premiums), add coordinate mapping guidance to validateMove description, add catalog migration 0014_strategic_seeded_prompts for strategic SEARCH_PROFILE presets, verify CORE_SHA256 and quality gates, conduct live NVIDIA NIM verification, land one commit, push, and read back.
Phase: implementation
Exact baseline: f6b6fff42736c5124b508fde319f8bf5ae96cfc3
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: bounded reversible mutation across prompt formatting, database seeded-prompt migration, and test assertions, verified by unit test gates and live diagnostic probe. No trust boundary crossed, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risk: In Scrabble, LLMs author 0% of moves when presented with flat coordinate lists like `(3,5) (3,6)...` because spatial coordinate mapping on a 15x15 text grid is combinatorially hard for models. Structured anchors provide the model with explicit adjacent board runs, direction, open spans, and reachable premiums, transforming blind search into targeted choice. The implementation must preserve `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) completely byte-identical, preserve user settings in Zustand store without mutation, and execute live NIM verification under the Cooperator's standing API authorization.

## Execution Rules & Environment Invariants

- ⛔ **RF-16 Mandatory Deviation**: Cursor AppImage intercepts `python*`. Always use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`. Never use ambient `python`, `python3`, or `poetry run`.
- ⛔ **Testing Rule**: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use standard `.venv/bin/python`.
- ⛔ **Pytest Warning**: `backend/pyproject.toml` already sets `addopts = "-q"`. Never add a second `-q`.
- ⛔ **Store & UI Boundary**: Do NOT modify `useGameStore.ts`, `settings/page.tsx`, or `AIThinkingOverlay.tsx`. User settings (`aiTimeout`, `aiMaxSteps`) and UI controls remain intact and supported.
- ⛔ **CORE SHA-256 Invariant**: `MOVE_SYSTEM_PROMPT` in `frontend/src/lib/prompts.ts` must remain byte-identical so `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) does not change.

## Cooperator Standing Decision Record

The Cooperator has made an explicit standing decision: real provider API calls (specifically NVIDIA NIM `nvidia/nemotron-3-super-120b-a12b`) are authorized as needed for development until quota limits are hit ("volat real API kym nenarazime na limit"). You are authorized to execute live verification turns via `manage.py diagnose_ai_play` under the Provider Accounting Contract.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:1642-1671      authorized provider calls and single-call-in-flight concurrency
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:423-453 coordinate consistency and Worker Exchange Identity
PROMPT_CONTRACTS.md:1478-1540 Provider Accounting Contract
AP.md:2453-2454      the CLOSED report-justification enum: `new-mutation`.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md                 the project brief ("Making the AI stronger").
frontend/src/lib/prompts.ts                               buildMoveUserPrompt, listAnchorSquares, anchorsFromCells, composeMoveSystemPrompt.
frontend/src/lib/prompts.test.ts                          user prompt tests, CORE_SHA256 pin, anchor tests.
backend/catalog/migrations/0011_playable_seeded_prompts.py SEARCH_PROFILE presets text and hash gating.
backend/catalog/migrations/0013_admin_provider_model_console.py current catalog migration head.
backend/game/management/commands/diagnose_ai_play.py      real AI turn diagnostic harness.
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/10_report_00.md the approved technical design.
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be f6b6fff42736c5124b508fde319f8bf5ae96cfc3
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these 8 paths:
1. `frontend/src/lib/prompts.ts`
2. `frontend/src/lib/prompts.test.ts`
3. `frontend/src/lib/prompts.baseline.fixture.ts` (new, test-only frozen copy of baseline prompts to preserve historical byte-oracle)
4. `frontend/src/lib/atomic-tiles.test.ts`
5. `backend/catalog/migrations/0014_strategic_seeded_prompts.py` (new)
6. `backend/tests/test_strategic_seeded_prompts_migration.py` (new)
7. `backend/game/management/commands/diagnose_ai_play.py`
8. `backend/tests/test_ai_play_turn_diagnostic.py`

⛔ Any mutation outside this allowlist is strictly unauthorized.

## 3. Implementation Specifications

### 3.1 Structured Candidate Anchors (`frontend/src/lib/prompts.ts`)
1. **Extraction & Formatting**:
   In `anchorsFromCells(rows: BoardCell[][])`:
   - Empty board: `(7,7) — CENTER; opening move must cover center (7,7)`.
   - Midgame board:
     For each empty square adjacent to an occupied square:
     * Identify adjacent runs of letters:
       - East: `E:(row,start..end)=[R|A|T|E]`
       - West: `W:(row,start..end)=[...]`
       - North: `N:(start..end,col)=[...]`
       - South: `S:(start..end,col)=[...]`
     * Open spans: Count consecutive empty squares in each orthogonal direction (stopping at board edge or occupied cell).
     * Reachable premiums: Check straight-line reach (within physical rack capacity $\le 7$ tiles) to unused TW, TL, or DW squares (using `PREMIUM_BOARD`).
     * Cross-check indicator: `cross=free` if no perpendicular occupied neighbor at this anchor, or `cross=[N|_|S]` showing the perpendicular run.
   - Deterministic ordering: Sort anchors by (1) reaching TW/TL/DW premiums first, (2) largest open spans, (3) coordinates (row, col).
2. **Compact & Clean Representation**:
   Format each anchor concisely:
   ```text
   (7,4) E:(7,5..8)=[R|A|T|E] | ACROSS W4/E0 cross=free; DOWN N7/S7 cross=[_|R|A|T|E] | reaches DW at (7,7), TL at (5,5)
   ```
3. **Coordinate Mapping Guidance**:
   In `buildMoveUserPrompt`:
   Include concise instructions under `COORDINATE MAPPING & RULES`:
   - `ACROSS: row stays constant, col increases (e.g. (7,4), (7,5), (7,6)...)`
   - `DOWN: col stays constant, row increases (e.g. (4,7), (5,7), (6,7)...)`
   - `REUSE EXISTING TILES: only list NEW tiles in your placements array! Do NOT re-place existing tiles.`
   - `CONTINUOUS LINE: placements must connect to an anchor and form one valid word.`
4. **Preserve System Prompt & CORE**:
   `MOVE_SYSTEM_PROMPT` remains `moveSystemPromptFor(englishMoveSpec)`.
   `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) must remain byte-identical!

### 3.2 Test Oracle Preservation (`frontend/src/lib/prompts.baseline.fixture.ts` & `prompts.test.ts`)
1. Create `frontend/src/lib/prompts.baseline.fixture.ts` as a test-only frozen copy of baseline `buildMoveUserPrompt` from `f6b6fff` to preserve the historical byte oracle `BASELINE_USER_PROMPT_SHA256`.
2. In `frontend/src/lib/prompts.test.ts`:
   - Verify `BASELINE_USER_PROMPT_SHA256` against the baseline fixture.
   - Add unit tests for the new structured anchors: center opening, horizontal/vertical adjacent runs, open spans, premium detection, coordinate mapping rules.
   - Verify `CORE_SHA256` remains unchanged.
3. In `frontend/src/lib/atomic-tiles.test.ts`:
   - Update anchor format assertions to match the structured format.

### 3.3 Catalog Migration `0014_strategic_seeded_prompts.py`
1. Create `backend/catalog/migrations/0014_strategic_seeded_prompts.py`:
   - Depends on `("catalog", "0013_admin_provider_model_console")`.
   - Imports `_playable_0011 = importlib.import_module("catalog.migrations.0011_playable_seeded_prompts")`.
   - `PRIOR_PROMPTS = _playable_0011.NEW_PROMPTS`.
   - `NEW_PROMPTS`:
     * `Initial`:
       `"SEARCH PROFILE — Initial (balanced):\n"`
       `"Scan order: 1) check anchors adjacent to existing words and premium squares (TW/TL/DW), "`
       `"2) pick direction (ACROSS increases col, DOWN increases row), reuse existing board tiles without re-placing them, "`
       `"3) verify leave quality: keep a balanced mix of vowels and consonants, avoid duplicate tiles, and preserve blanks. "`
       `"With more than 7 bag tiles, play tighter defense when leading (+30); open lanes when trailing (-30). Validate your best candidate promptly."`
     * `Fast Search`:
       `"SEARCH PROFILE — Fast Search (quick points):\n"`
       `"Find a high-scoring anchor quickly: target an anchor with an open span toward a premium square. "`
       `"Form a crisp, solid word using 3 to 5 rack tiles. Keep at least two vowels and two consonants for next turn. "`
       `"Avoid leaving Q, X, or lonely single vowels. Call validateMove immediately once found."`
     * `Short Hooks`:
       `"SEARCH PROFILE — Short Hooks (extensions first):\n"`
       `"Inspect words already on the board: test prepending or appending 1 or 2 tiles to existing words (e.g. adding S, ED, ER, Y or language prefixes). "`
       `"Look for parallel plays that form multiple short cross-words simultaneously. "`
       `"Verify all perpendicular cross-words before playing. Count physical tiles carefully."`
     * `Grandmaster`:
       `"SEARCH PROFILE — Grandmaster (strategic mastery):\n"`
       `"Master board control and leave equity: evaluate both turn score and opponent counter-threats. "`
       `"Leading by 30+ in midgame: close down open Triple Word (TW) lanes and reduce open anchors. "`
       `"Trailing by 30+: open explosive scoring lanes. In endgame (bag <= 7): track unseen tiles. "`
       `"When bag is empty: calculate exact out-play sequences to capture opponent leftover points."`
   - Hash-gated: updates ONLY rows whose current text matches `_text_hash(PRIOR_PROMPTS[name])`. Admin-customized rows are preserved. Reversible.
2. Create `backend/tests/test_strategic_seeded_prompts_migration.py`:
   - Test forward migration refreshes unmodified rows.
   - Test customized rows are never overwritten.
   - Test backward migration restores 0011 text.

### 3.4 Live NVIDIA NIM Verification
Execute real provider verification under the Provider Accounting Contract:
1. Command:
   ```bash
   LIBRETILES_AI_PLAY_LIVE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play \
     --variant-slug english \
     --provider nvidia-nim \
     --model-id nvidia/nemotron-3-super-120b-a12b \
     --runtime-mode live \
     --queue-mode selected-only \
     --turn-count 1 \
     --output -
   ```
2. Observe and record:
   - Does the model generate a candidate?
   - What is the validation outcome?
   - Record `completion_source` (`provider_candidate` vs `backend_ranked_candidate`).
   - Confirm single call in flight and terminal classification.

## 4. Verification Procedures

Execute and ensure clean exit (0) on:

From `frontend/`:
```bash
npx vitest run src/lib/prompts.test.ts src/lib/atomic-tiles.test.ts
npm run typecheck
npm run lint
```

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strategic_seeded_prompts_migration.py tests/test_playable_seeded_prompts_migration.py tests/test_ai_play_turn_diagnostic.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add frontend/src/lib/prompts.ts \
        frontend/src/lib/prompts.test.ts \
        frontend/src/lib/prompts.baseline.fixture.ts \
        frontend/src/lib/atomic-tiles.test.ts \
        backend/catalog/migrations/0014_strategic_seeded_prompts.py \
        backend/tests/test_strategic_seeded_prompts_migration.py \
        backend/game/management/commands/diagnose_ai_play.py \
        backend/tests/test_ai_play_turn_diagnostic.py

git diff --staged --stat
```

Commit message:
```bash
feat(prompts): implement structured candidate anchors and strategic preset migration
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "f6b6fff42736c5124b508fde319f8bf5ae96cfc3"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- `CORE_SHA256` fails to match the unchanged system prompt core.
- Pre-push verification reveals remote diverged from `f6b6fff42736c5124b508fde319f8bf5ae96cfc3`.

## 7. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 11, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `f6b6fff42736c5124b508fde319f8bf5ae96cfc3`
- End commit: `<exact SHA>`
- Changed files and purpose (explicit paths)
- Live verification results (NVIDIA NIM turn output, tool calls, completion_source)
- Provider Accounting Contract table
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
