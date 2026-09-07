You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S1-PROMPT-SPECS — implement native MovePromptSpec and JudgePromptSpec for all 12 shipped variants (fixing H1), fix the hardcoded English candidate description in validateMove, verify CORE_SHA256 preservation and comprehensive test coverage, land one commit, push, and read back.
Phase: implementation
Exact baseline: 151e833dd0e78ced075101864cb5f45ee521bebc
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E1
Evidence tier basis: bounded reversible mutation across three frontend files backed by focused unit test assertions, CORE hash preservation, and TypeScript type checking. No trust boundary, no network beyond authorized Git push, no provider call, no migration, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risk: H1 prompt specs govern model instructions across all non-English gameplay. Every exemplar word and score must strictly match the variant's committed lexicon and `premiums.json`. Furthermore, `MOVE_SYSTEM_PROMPT` for English must remain byte-identical so that the pinned `CORE_SHA256` digest is preserved.

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
/home/agile/Projects/libretiles/frontend/AGENTS.md        Next.js rules.
frontend/src/lib/prompts.ts                               the prompt definitions and dispatch functions
frontend/src/lib/prompts.test.ts                          the prompt test suite with CORE_SHA256 pin
frontend/src/app/api/ai/move/route.ts                     lines 1370-1410 (system prompt composition & validateMove tool)
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/01_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 151e833dd0e78ced075101864cb5f45ee521bebc
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify **ONLY** these three files:
1. `frontend/src/lib/prompts.ts`
2. `frontend/src/lib/prompts.test.ts`
3. `frontend/src/app/api/ai/move/route.ts`

⛔ Any mutation to any file outside this allowlist is unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `01_report_00.md`:

### 3.1 `frontend/src/lib/prompts.ts`

1. **Union type extension**:
   Define:
   ```typescript
   export type PromptLexiconId =
     | "collins2019"
     | "slovak"
     | "czech"
     | "polish"
     | "german"
     | "portuguese"
     | "icelandic"
     | "italian"
     | "dutch"
     | "danish"
     | "swedish"
     | "afrikaans";

   export type MovePromptLexiconId = PromptLexiconId;
   export type JudgePromptLexiconId = PromptLexiconId;
   ```
   (Update `MovePromptSpec` and `JudgePromptSpec` to use `PromptLexiconId` for `lexiconId`).

2. **Existing specs**:
   Keep `englishMoveSpec`, `slovakMoveSpec`, `englishJudgeSpec`, `slovakJudgeSpec` completely intact.

3. **Ten new MovePromptSpec constants**:
   Export:
   - `czechMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"czech"`
     * `productLine`: `"Czech Scrabble (shipped Czech lexicon)"`
     * `shedTiles`: `"X / Ď / Ó / Ť / Ň"`
     * `exemplarA`: rack `"A U T O H R D"`, validateInput: placements A(7,5), U(7,6), T(7,7), O(7,8); validateOutput: `'{"valid":true,"words":[{"word":"AUTO","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements X(4,8), A(5,8); firstOutput: `'{"valid":false,"reason":"Move must connect to existing tiles"}'`; pivotInput: placement H(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"HRAD","valid":true}],"total_score":5}'`
   - `polishMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"polish"`
     * `productLine`: `"Polish Scrabble (shipped Polish lexicon)"`
     * `shedTiles`: `"Ź / Ń / Ć / Ą / Ę"`
     * `exemplarA`: rack `"W O D A L A S"`, validateInput: placements W(7,5), O(7,6), D(7,7), A(7,8); validateOutput: `'{"valid":true,"words":[{"word":"WODA","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements Ź(4,8), A(5,8); firstOutput: standard; pivotInput: placement L(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"LAS","valid":true}],"total_score":4}'`
   - `germanMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"german"`
     * `productLine`: `"German Scrabble (shipped German lexicon)"`
     * `shedTiles`: `"Q / Y / Ö / X"`
     * `exemplarA`: rack `"H A U S M E N"`, validateInput: placements H(7,5), A(7,6), U(7,7), S(7,8); validateOutput: `'{"valid":true,"words":[{"word":"HAUS","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements Q(4,8), I(5,8); firstOutput: standard; pivotInput: placement M(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"MAUS","valid":true}],"total_score":6}'`
   - `portugueseMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"portuguese"`
     * `productLine`: `"Portuguese Scrabble (shipped Portuguese lexicon)"`
     * `shedTiles`: `"X / Z / Q / J"`
     * `exemplarA`: rack `"C A S A M R O"`, validateInput: placements C(7,5), A(7,6), S(7,7), A(7,8); validateOutput: `'{"valid":true,"words":[{"word":"CASA","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements X(4,8), A(5,8); firstOutput: standard; pivotInput: placement M(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"MAR","valid":true}],"total_score":3}'`
   - `icelandicMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"icelandic"`
     * `productLine`: `"Icelandic Scrabble (shipped Icelandic lexicon)"`
     * `shedTiles`: `"X / Ý / É / Ú / Ö"`
     * `exemplarA`: rack `"S A G A R Ó N"`, validateInput: placements S(7,5), A(7,6), G(7,7), A(7,8); validateOutput: `'{"valid":true,"words":[{"word":"SAGA","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements X(4,8), A(5,8); firstOutput: standard; pivotInput: placement R(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"RÓS","valid":true}],"total_score":8}'`
   - `italianMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"italian"`
     * `productLine`: `"Italian Scrabble (shipped Italian lexicon)"`
     * `shedTiles`: `"Q / G / H / Z"`
     * `exemplarA`: rack `"C A S A M R E"`, validateInput: placements C(7,5), A(7,6), S(7,7), A(7,8); validateOutput: `'{"valid":true,"words":[{"word":"CASA","valid":true}],"total_score":12}'`
     * `exemplarB`: firstInput: placements Q(4,8), I(5,8); firstOutput: standard; pivotInput: placement M(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"MARE","valid":true}],"total_score":7}'`
   - `dutchMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"dutch"`
     * `productLine`: `"Dutch Scrabble (shipped Dutch lexicon)"`
     * `shedTiles`: `"Q / X / Y"`
     * `exemplarA`: rack `"H U I S B O M"`, validateInput: placements H(7,5), U(7,6), I(7,7), S(7,8); validateOutput: `'{"valid":true,"words":[{"word":"HUIS","valid":true}],"total_score":22}'`
     * `exemplarB`: firstInput: placements Q(4,8), I(5,8); firstOutput: standard; pivotInput: placement B(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"BOOM","valid":true}],"total_score":8}'`
   - `danishMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"danish"`
     * `productLine`: `"Danish Scrabble (shipped Danish lexicon)"`
     * `shedTiles`: `"C / W / X / Z"`
     * `exemplarA`: rack `"G A D E B O R"`, validateInput: placements G(7,5), A(7,6), D(7,7), E(7,8); validateOutput: `'{"valid":true,"words":[{"word":"GADE","valid":true}],"total_score":14}'`
     * `exemplarB`: firstInput: placements X(4,8), E(5,8); firstOutput: standard; pivotInput: placement B(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"BORD","valid":true}],"total_score":8}'`
   - `swedishMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"swedish"`
     * `productLine`: `"Swedish Scrabble (shipped Swedish lexicon)"`
     * `shedTiles`: `"Z / C / X / J / Y"`
     * `exemplarA`: rack `"S T O L J R E"`, validateInput: placements S(7,5), T(7,6), O(7,7), L(7,8); validateOutput: `'{"valid":true,"words":[{"word":"STOL","valid":true}],"total_score":10}'`
     * `exemplarB`: firstInput: placements Z(4,8), A(5,8); firstOutput: standard; pivotInput: placement J(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"JORD","valid":true}],"total_score":11}'`
   - `afrikaansMoveSpec: MovePromptSpec`:
     * `lexiconId`: `"afrikaans"`
     * `productLine`: `"Afrikaans Scrabble (shipped Afrikaans lexicon)"`
     * `shedTiles`: `"J / B / F"`
     * `exemplarA`: rack `"M E L K A A S"`, validateInput: placements M(7,5), E(7,6), L(7,7), K(7,8); validateOutput: `'{"valid":true,"words":[{"word":"MELK","valid":true}],"total_score":20}'`
     * `exemplarB`: firstInput: placements J(4,8), A(5,8); firstOutput: standard; pivotInput: placement K(7,6); pivotOutput: `'{"valid":true,"words":[{"word":"KAAS","valid":true}],"total_score":6}'`

4. **Ten new JudgePromptSpec constants**:
   Export:
   - `czechJudgeSpec: JudgePromptSpec` { lexiconId: "czech", language: "Czech", authorityName: "The shipped Czech lexicon", entryName: "the shipped Czech lexicon", recallNoun: "a shipped Czech lexicon entry" }
   - `polishJudgeSpec: JudgePromptSpec` { lexiconId: "polish", language: "Polish", authorityName: "The shipped Polish lexicon", entryName: "the shipped Polish lexicon", recallNoun: "a shipped Polish lexicon entry" }
   - `germanJudgeSpec: JudgePromptSpec` { lexiconId: "german", language: "German", authorityName: "The shipped German lexicon", entryName: "the shipped German lexicon", recallNoun: "a shipped German lexicon entry" }
   - `portugueseJudgeSpec: JudgePromptSpec` { lexiconId: "portuguese", language: "Portuguese", authorityName: "The shipped Portuguese lexicon", entryName: "the shipped Portuguese lexicon", recallNoun: "a shipped Portuguese lexicon entry" }
   - `icelandicJudgeSpec: JudgePromptSpec` { lexiconId: "icelandic", language: "Icelandic", authorityName: "The shipped Icelandic lexicon", entryName: "the shipped Icelandic lexicon", recallNoun: "a shipped Icelandic lexicon entry" }
   - `italianJudgeSpec: JudgePromptSpec` { lexiconId: "italian", language: "Italian", authorityName: "The shipped Italian lexicon", entryName: "the shipped Italian lexicon", recallNoun: "a shipped Italian lexicon entry" }
   - `dutchJudgeSpec: JudgePromptSpec` { lexiconId: "dutch", language: "Dutch", authorityName: "The shipped Dutch lexicon", entryName: "the shipped Dutch lexicon", recallNoun: "a shipped Dutch lexicon entry" }
   - `danishJudgeSpec: JudgePromptSpec` { lexiconId: "danish", language: "Danish", authorityName: "The shipped Danish lexicon", entryName: "the shipped Danish lexicon", recallNoun: "a shipped Danish lexicon entry" }
   - `swedishJudgeSpec: JudgePromptSpec` { lexiconId: "swedish", language: "Swedish", authorityName: "The shipped Swedish lexicon", entryName: "the shipped Swedish lexicon", recallNoun: "a shipped Swedish lexicon entry" }
   - `afrikaansJudgeSpec: JudgePromptSpec` { lexiconId: "afrikaans", language: "Afrikaans", authorityName: "The shipped Afrikaans lexicon", entryName: "the shipped Afrikaans lexicon", recallNoun: "a shipped Afrikaans lexicon entry" }

5. **Dispatch Maps and Lookup Functions**:
   Build:
   ```typescript
   const MOVE_SPECS_BY_KEY = new Map<string, MovePromptSpec>([
     ["english", englishMoveSpec],
     ["collins2019", englishMoveSpec],
     ["slovak", slovakMoveSpec],
     ["czech", czechMoveSpec],
     ["polish", polishMoveSpec],
     ["german", germanMoveSpec],
     ["portuguese", portugueseMoveSpec],
     ["icelandic", icelandicMoveSpec],
     ["italian", italianMoveSpec],
     ["dutch", dutchMoveSpec],
     ["danish", danishMoveSpec],
     ["swedish", swedishMoveSpec],
     ["afrikaans", afrikaansMoveSpec],
   ]);

   const JUDGE_SPECS_BY_KEY = new Map<string, JudgePromptSpec>([
     ["english", englishJudgeSpec],
     ["collins2019", englishJudgeSpec],
     ["slovak", slovakJudgeSpec],
     ["czech", czechJudgeSpec],
     ["polish", polishJudgeSpec],
     ["german", germanJudgeSpec],
     ["portuguese", portugueseJudgeSpec],
     ["icelandic", icelandicJudgeSpec],
     ["italian", italianJudgeSpec],
     ["dutch", dutchJudgeSpec],
     ["danish", danishJudgeSpec],
     ["swedish", swedishJudgeSpec],
     ["afrikaans", afrikaansJudgeSpec],
   ]);

   export function movePromptSpecFromContext(context: {
     lexicon_id?: unknown;
     variant?: unknown;
   }): MovePromptSpec {
     if (typeof context.lexicon_id === "string") {
       const spec = MOVE_SPECS_BY_KEY.get(context.lexicon_id);
       if (spec) return spec;
     }
     if (typeof context.variant === "string") {
       const spec = MOVE_SPECS_BY_KEY.get(context.variant);
       if (spec) return spec;
     }
     return englishMoveSpec;
   }

   export function judgePromptSpecFromBody(body: {
     lexicon_id?: unknown;
     variant?: unknown;
   }): JudgePromptSpec {
     if (typeof body.lexicon_id === "string") {
       const spec = JUDGE_SPECS_BY_KEY.get(body.lexicon_id);
       if (spec) return spec;
     }
     if (typeof body.variant === "string") {
       const spec = JUDGE_SPECS_BY_KEY.get(body.variant);
       if (spec) return spec;
     }
     return englishJudgeSpec;
   }
   ```
   Note: `moveSystemPromptFor` and `composeMoveSystemPrompt` must remain structurally unchanged.

### 3.2 `frontend/src/lib/prompts.test.ts`

1. Retain all existing tests verifying `MOVE_SYSTEM_PROMPT`, `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`), `MOVE_PROMPT_VERSION` (`pfr-s2-core-1`), Slovak Move core, `composeMoveSystemPrompt`, and `JUDGE_SYSTEM_PROMPT`.
2. Add comprehensive tests for the 10 new move specs and 10 new judge specs:
   - Check that `moveSystemPromptFor(spec)` for every new spec:
     * Contains all seven `PRIORITY_SECTIONS` in order
     * Contains `Shed ${spec.shedTiles}`
     * Contains `"ready":true`
     * Does NOT contain `/Collins/i`
     * For no-Q variants (`polish`, `icelandic`, `danish`, `swedish`, `afrikaans`, and `czech`), does not contain `/"letter":"Q"/`
   - Test `movePromptSpecFromContext`:
     * Resolves correctly for all 12 variant slugs (e.g. `{ variant: "czech" } -> czechMoveSpec`)
     * Resolves correctly for all 12 lexicon IDs (e.g. `{ lexicon_id: "collins2019" } -> englishMoveSpec`)
     * Falls back to `englishMoveSpec` on unknown variant (`{ variant: "unknown" }`), missing context (`{}`), or hostile keys (`{ variant: "__proto__" }`, `{ lexicon_id: "constructor" }`).
   - Test `judgeSystemPromptFor(spec)` for all new judge specs:
     * Contains `spec.language`
     * Contains `shipped ${spec.language} lexicon`
     * Does NOT contain `/Collins/i`
     * Conservative and strict JSON format assertions
   - Test `judgePromptSpecFromBody` resolution across all 12 variants and fallback.

### 3.3 `frontend/src/app/api/ai/move/route.ts`

In `validateMove` tool definition (around lines 1401-1406):
Change:
```typescript
description:
  "Validates a candidate tile placement before playing it. Call this " +
  "with your plausible English candidates before deciding your move. " +
  "Returns whether the move is legal, all formed words, and total score.",
```
To:
```typescript
description:
  "Validates a candidate tile placement before playing it. Call this " +
  "with your plausible candidates for this game's lexicon before deciding your move. " +
  "Returns whether the move is legal, all formed words, and total score.",
```

## 4. Verification Procedures

Execute and ensure clean exit (0) on:

From `frontend/`:
```bash
npx vitest run src/lib/prompts.test.ts
npx vitest run src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts
npx vitest run src/lib/ai-turn-simulation.test.ts
npm run typecheck
npm run lint
```

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strength_benchmark.py tests/test_slovak_full_game.py
```

⛔ Do NOT run `npm run build` (writes to `.next/`).
⛔ Do NOT run any package installer (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY the three allowlisted files by explicit paths:
```bash
git add frontend/src/lib/prompts.ts frontend/src/lib/prompts.test.ts frontend/src/app/api/ai/move/route.ts
git diff --staged --stat
```
Verify that `git diff --staged --name-only` outputs EXACTLY those three files.

Commit with message:
```bash
git commit -m "feat(prompts): add native prompt specs for all 12 variants and fix H1 lexicon mismatch"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "151e833dd0e78ced075101864cb5f45ee521bebc"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Any test or gate failure cannot be resolved within the 3 allowlisted files.
- `CORE_SHA256` in `prompts.test.ts` fails to match the unchanged English core.
- Pre-push verification reveals that `origin/main` has diverged from the baseline.

## 7. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 02, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `151e833dd0e78ced075101864cb5f45ee521bebc`
- End commit: `<exact SHA>`
- Changed files and purpose (listing exactly the three allowlisted paths)
- Tests and validation summaries (verbatim tool outputs from vitest, typecheck, lint, and backend gates)
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
