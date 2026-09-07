### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 01, Worker exchange ordinal: 01
```

```text
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Baseline verified: `git rev-parse HEAD` = `151e833dd0e78ced075101864cb5f45ee521bebc`, clean working tree. All evidence below is repository-grounded at that commit; every exemplar word was membership-checked against its committed lexicon (NFC casefold, matching `word_authority._nfc_casefold`), every rack and placement letter was checked against the variant tile bag, and every score was computed against `backend/assets/premiums.json` (row 7: `TW . . DL . . . DW . . . DL . . TW` — center (7,7) is DW; (7,5), (7,6), (7,8) and (4,8)/(5,8) are plain).

## D1: Variant & Lexicon Inventory (12 variants)

| Slug | Language (ISO) | Dictionary (entries) | 2-letter entries | Alphabet / tile-set characteristics |
|---|---|---|---|---|
| english | English (—) | collins2019.txt (279,496) | 127 | A–Z, no diacritics. Only variant whose lexicon_id (`collins2019`) differs from its slug. |
| slovak | Slovak (sk) | slovak.txt (3,005,250) | 103 authoritative | Tiles incl. Á Ä Č Ď É Í Ĺ Ľ Ň Ó Ô Ŕ Š Ť Ú Ý Ž. `alphabet_order` lists CH/DZ/DŽ as collation letters but **no multigraph tile exists**; `playable_letters` is tiles only. ONLY variant with `two_tile_words_file` (103 SSS words; main-dict 2-letter count 269 is irrelevant to legality). |
| czech | Czech (cs) | czech.txt (3,930,497) | 350 | Tiles incl. Á Č Ď É Ě Í Ň Ó Ř Š Ť Ú Ů Ý Ž; CH in alphabet_order only, no CH tile. |
| polish | Polish (pl) | polish.txt (3,721,704) | 458 | Tiles incl. Ą Ć Ę Ł Ń Ó Ś Ź Ż; **no Q, V, X tiles**. |
| german | German (de) | german.txt (709,844) | 125 | A–Z plus Ä Ö Ü tiles; no ß tile (lexicon writes `ss`); loanword accents folded. |
| portuguese | Portuguese (pt) | portuguese.txt (4,119,831) | 47 | A–Z plus Ç tile (3 pts); all other diacritics folded. Only variant with **three blanks** (`?=0x3`). |
| icelandic | Icelandic (is) | icelandic.txt (200,182) | 95 | Tiles incl. Ð Þ Æ Ö Á É Í Ó Ú Ý; **no C, Q, W, Z tiles**; no folding applied. |
| italian | Italian (it) | italian.txt (3,128,429) | 121 | 21-letter alphabet; **no J, K, W, X, Y tiles**; diacritics folded. |
| dutch | Dutch (nl) | dutch.txt (1,293,086) | 197 | A–Z; IJ written as I+J tiles; diacritics folded. |
| danish | Danish (da) | danish.txt (317,167) | 367 | A–Z plus Æ Ø Å tiles; **no Q tile**; thorn/eth words dropped. |
| swedish | Swedish (sv) | swedish.txt (822,919) | 258 | A–Z plus Å Ä Ö tiles; **no Q, W tiles**; ü-words dropped. |
| afrikaans | Afrikaans (af) | afrikaans.txt (148,267) | 150 | Plain Latin tiles; **no C, Q, X, Z tiles**; diacritics folded. |

Two-tile routing (`word_authority.py:194-218`): only Slovak has `two_tile_words`; for the other eleven, `load_two_tile_words` returns `None` and 2-tile words route to the main lexicon. All exemplar words below are ≥3 tiles, so no exemplar touches two-tile routing. `lexicon_id` is the dictionary-file stem (`services._lexicon_id`), i.e. equal to the slug for all variants except english→`collins2019`.

## D2: Native Exemplar Construction (12 variants)

Conventions preserved from the shipped English/Slovak specs: Exemplar A places a 4-letter word at (7,5)–(7,8) covering the DW center (score = 2 × letter sum); Exemplar B first places two disconnected tiles at (4,8)/(5,8) using a variant-legal high-point tile, then pivots with ONE tile at (7,6) prepended to an implied stem at (7,7)+ (score = plain letter sum of the whole word). Every exemplar word AND every implied stem is a verified lexicon member; every rack is a legal 7-tile draw containing the Exemplar A letters plus the pivot letter. `firstOutput` is the byte-identical string `{"valid":false,"reason":"Move must connect to existing tiles"}` for all twelve.

**english (reviewed, unchanged):** RATE 8 / STARE 5 — recomputed against premiums and Collins; correct.
**slovak (reviewed, unchanged):** AUTO 12 (A1 U3 T1 O1 ×2) / HRA 6 (H4 R1 A1) — both in slovak.txt; correct.

Ten new specs (rack | A: word, validateOutput score | B: disconnected letters, pivot word, score; stems in parentheses are the verified implied board words):

- **czech** — rack `A U T O H R D` | A: AUTO, `{"valid":true,"words":[{"word":"AUTO","valid":true}],"total_score":10}` | B: X,A at (4,8)/(5,8); pivot H at (7,6) → HRAD 5 (stem RAD)
- **polish** — rack `W O D A L A S` | A: WODA, 10 | B: Ź,A; pivot L → LAS 4 (stem AS)
- **german** — rack `H A U S M E N` | A: HAUS, 10 | B: Q,I; pivot M → MAUS 6 (stem AUS)
- **portuguese** — rack `C A S A M R O` | A: CASA, 10 | B: X,A; pivot M → MAR 3 (stem AR)
- **icelandic** — rack `S A G A R Ó N` | A: SAGA, 10 | B: X,A; pivot R → RÓS 8 (stem ÓS)
- **italian** — rack `C A S A M R E` | A: CASA, 12 | B: Q,I; pivot M → MARE 7 (stem ARE)
- **dutch** — rack `H U I S B O M` | A: HUIS, 22 | B: Q,I; pivot B → BOOM 8 (stem OOM)
- **danish** — rack `G A D E B O R` | A: GADE, 14 | B: X,E (no Q tile); pivot B → BORD 8 (stem ORD)
- **swedish** — rack `S T O L J R E` | A: STOL, 10 | B: Z,A (no Q tile); pivot J → JORD 11 (stem ORD)
- **afrikaans** — rack `M E L K A A S` | A: MELK, 20 | B: J,A (no Q/X/Z tiles); pivot K → KAAS 6 (stem AAS)

Exact JSON strings follow the shipped template mechanically; e.g. czech:

```json
validateInput:  {"placements":[{"row":7,"col":5,"letter":"A"},{"row":7,"col":6,"letter":"U"},{"row":7,"col":7,"letter":"T"},{"row":7,"col":8,"letter":"O"}]}
validateOutput: {"valid":true,"words":[{"word":"AUTO","valid":true}],"total_score":10}
firstInput:     {"placements":[{"row":4,"col":8,"letter":"X"},{"row":5,"col":8,"letter":"A"}]}
firstOutput:    {"valid":false,"reason":"Move must connect to existing tiles"}
pivotInput:     {"placements":[{"row":7,"col":6,"letter":"H"}]}
pivotOutput:    {"valid":true,"words":[{"word":"HRAD","valid":true}],"total_score":5}
```

Each other variant substitutes its Exemplar A letters at cols 5–8, its two firstInput letters, its pivot letter, and the scores listed above. Verified sums (plain / doubled): AUTO 5/10, WODA 5/10, HAUS 5/10, CASA-pt 5/10, SAGA 5/10, CASA-it 6/12, HUIS 11/22, GADE 7/14, STOL 5/10, MELK 10/20; pivots HRAD 5, LAS 4, MAUS 6, MAR 3, RÓS 8, MARE 7, BOOM 8, BORD 8, JORD 11, KAAS 6.

`productLine` strings: `"<Language> Scrabble (shipped <Language> lexicon)"` for the ten new variants (mirrors Slovak's no-Collins claim; never names an official tournament list, honoring the "Not an official tournament list" lexicon headers).

## D3: Shed Tiles per Variant

From `letters` points×counts (all listed tiles are count 1 unless noted):

- english: `Q/J` (unchanged); slovak: `X / Ĺ / Ŕ / Ä / Ó` (unchanged, all 10 pts)
- czech: `X / Ď / Ó / Ť / Ň` (10, 8, 7, 7, 6)
- polish: `Ź / Ń / Ć / Ą / Ę` (9, 7, 6, 5, 5; F/Ó/Ś/Ż also 5×1 — diacritic cluster chosen for lower combinability)
- german: `Q / Y / Ö / X` (10, 10, 8, 8)
- portuguese: `X / Z / Q / J` (8, 8, 6, 5×2)
- icelandic: `X / Ý / É / Ú / Ö` (10, 9, 8, 8, 8)
- italian: `Q / G / H / Z` (10; 8×2 each)
- dutch: `Q / X / Y` (10, 8, 8)
- danish: `C / W / X / Z` (8×2, 8, 8, 8)
- swedish: `Z / C / X / J / Y` (10, 8, 8, 7, 7)
- afrikaans: `J / B / F` (10, 8, 8)

## D4: JudgePromptSpec (12 variants)

english and slovak unchanged. The ten new specs follow the Slovak pattern exactly (must never claim Collins; the authority is the shipped lexicon, which is what `WordAuthority` actually consults):

| lexiconId | language | authorityName | entryName | recallNoun |
|---|---|---|---|---|
| czech | Czech | The shipped Czech lexicon | the shipped Czech lexicon | a shipped Czech lexicon entry |
| polish | Polish | The shipped Polish lexicon | the shipped Polish lexicon | a shipped Polish lexicon entry |
| german | German | The shipped German lexicon | the shipped German lexicon | a shipped German lexicon entry |
| portuguese | Portuguese | The shipped Portuguese lexicon | the shipped Portuguese lexicon | a shipped Portuguese lexicon entry |
| icelandic | Icelandic | The shipped Icelandic lexicon | the shipped Icelandic lexicon | a shipped Icelandic lexicon entry |
| italian | Italian | The shipped Italian lexicon | the shipped Italian lexicon | a shipped Italian lexicon entry |
| dutch | Dutch | The shipped Dutch lexicon | the shipped Dutch lexicon | a shipped Dutch lexicon entry |
| danish | Danish | The shipped Danish lexicon | the shipped Danish lexicon | a shipped Danish lexicon entry |
| swedish | Swedish | The shipped Swedish lexicon | the shipped Swedish lexicon | a shipped Swedish lexicon entry |
| afrikaans | Afrikaans | The shipped Afrikaans lexicon | the shipped Afrikaans lexicon | a shipped Afrikaans lexicon entry |

## D5: Prompt Dispatch Architecture

In `frontend/src/lib/prompts.ts`:

1. Widen the id unions to one shared 12-member union: `type PromptLexiconId = "collins2019" | "slovak" | "czech" | "polish" | "german" | "portuguese" | "icelandic" | "italian" | "dutch" | "danish" | "swedish" | "afrikaans"`, with `MovePromptLexiconId` and `JudgePromptLexiconId` kept as exported aliases (type-only; erased at runtime).
2. Two `ReadonlyMap<string, Spec>` lookups keyed by BOTH variant slug and lexicon id — `["english", englishMoveSpec], ["collins2019", englishMoveSpec], ["slovak", slovakMoveSpec], ["czech", czechMoveSpec], …` (slug equals lexicon stem for all non-English variants, so each contributes one key). `Map.get` is deliberate: a `Record` lookup with a hostile backend key such as `"__proto__"` or `"constructor"` would hit the prototype chain.
3. Resolution order in both `movePromptSpecFromContext` and `judgePromptSpecFromBody`: string `lexicon_id` lookup first, then string `variant`, then the English spec. This is a strict superset of the current `=== "slovak"` OR-check (backend always sends both fields consistently: `services.get_ai_context` returns `variant` and `**_variant_snapshot_fields` with `lexicon_id`), and unknown/missing/13th-variant inputs fail safe to English exactly as today.
4. `composeMoveSystemPrompt` needs no change: its `spec.lexiconId === "collins2019"` branch keeps reusing the frozen `MOVE_SYSTEM_PROMPT` constant; every other spec flows through `moveSystemPromptFor(spec)`.

## D6: CORE Template & Hash Digestion

- `moveSystemPromptFor` needs **no structural change**: `${spec.productLine}`, `${spec.shedTiles}`, and the four exemplar interpolations already accommodate all twelve specs (Slovak proves the factory pattern).
- `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) **does not change**: `MOVE_SYSTEM_PROMPT = moveSystemPromptFor(englishMoveSpec)`, and Slice 1 leaves both the template literal and `englishMoveSpec` byte-identical; added constants and widened type unions have no runtime bytes. `MOVE_PROMPT_VERSION` stays `pfr-s2-core-1`. hash pinning.
- New assertions in `prompts.test.ts`:
  1. Existing `CORE_SHA256`, byte-oracle, English, and Slovak blocks stay verbatim (regression proof the CORE is unchanged).
  2. A parameterized block over the ten new move specs: seven `PRIORITY_SECTIONS` in order; contains `Shed <spec.shedTiles>`; contains both exemplar words and `"ready":true`; does NOT match `/Collins/i`; for the no-Q variants (polish, icelandic, danish, swedish, afrikaans, and czech which never uses Q) does not match `/"letter":"Q"/`.
  3. Dispatch completeness: a hard-coded 12-slug list asserting `movePromptSpecFromContext({variant})` and `({lexicon_id})` return the exact spec object (`toBe`) for every slug and every lexicon id; unknown slug, missing fields, and hostile keys (`"__proto__"`, `"constructor"`) → `englishMoveSpec`.
  4. A parameterized judge block over the ten new judge specs mirroring the existing "slovak JUDGE CORE" assertions (names the language, `shipped <Language> lexicon`, no Collins, conservative + strict-JSON schema), plus the mirrored `judgePromptSpecFromBody` dispatch test.

## D7: Downstream Impact & Compatibility

- **Backend context (MEASURED)**: `get_ai_context` already returns `"variant": session.variant_slug` and `lexicon_id` via `_variant_snapshot_fields` (`backend/game/services.py:163-169, 2201, 2213`) for every variant. No backend change, no model change, no migration: `lexicon_id` is derived at runtime from the dictionary file stem.
- **Move route**: sole consumption point is `movePromptSpecFromContext(context)` → `composeMoveSystemPrompt` (`route.ts:1373-1377`); works unchanged. **MEASURED adjacent defect**: the `validateMove` tool description hardcodes "plausible **English** candidates" (`frontend/src/app/api/ai/move/route.ts:1401-1406`) and is sent to providers on every variant; no test or digest pins those bytes (single occurrence in the repository). Bounded one-string fix included in D8.
- **Judge route**: `judgePromptSpecFromBody(body)` at line 266 and the user prompt already interpolates `judgeSpec.language` (line 322). **MEASURED**: no in-repo production caller posts to `/api/ai/judge` (only `route.test.ts`), so H1 item 3 is currently reachable only by direct API callers; the fix remains correct and future-proof, and callers omitting the fields fail safe to English.
- **`ai-turn-simulation.test.ts`**: turn builders already model per-turn `variant`/`lexicon_id` (lines 78-79, 426-429, 1016-1017); nothing breaks; no change required.
- No i18n, overlay, catalog, or seeded-prompt-migration impact (SEARCH_PROFILE presets are advisory blocks composed around whichever CORE the spec selects; migrations 0010/0011 hash-gate DB rows, not the TypeScript CORE).

## D8: Slice 1 Implementation Plan

Ordered steps:
1. `frontend/src/lib/prompts.ts` — add ten `MovePromptSpec` and ten `JudgePromptSpec` constants with the exact D2/D3/D4 values; widen the lexicon-id unions; replace both dispatch functions with the Map-backed lookup (D5).
2. `frontend/src/lib/prompts.test.ts` — add the D6 assertions; leave all pinned hashes and existing blocks byte-identical.
3. `frontend/src/app/api/ai/move/route.ts` — single string edit: "plausible English candidates" → "plausible candidates for this game's lexicon".

Path allowlist (exactly three files): `frontend/src/lib/prompts.ts`, `frontend/src/lib/prompts.test.ts`, `frontend/src/app/api/ai/move/route.ts`.

Focused verification (from `frontend/`): `npx vitest run src/lib/prompts.test.ts`, `npx vitest run src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts`, `npx vitest run src/lib/ai-turn-simulation.test.ts`, `npm run typecheck`, `npm run lint`. No `npm run build`; no backend gates (no backend path touched).

Proposed Evidence Tier: **E1 — bounded reversible**: localized known path in one frontend module plus one string literal; strong focused tests including pinned CORE/user-prompt hashes that mechanically prove English-path non-regression; trivial rollback; no network, secret, dependency, or migration surface.

```text
Orchestration critique:
  MEASURED — route.ts:1401-1406 hardcodes "plausible English candidates" in the validateMove tool
    description sent to providers for every variant; outside the task's named dispatch files, so it
    is surfaced here and folded into D8 as a bounded one-string change for the grant to confirm.
  MEASURED — /api/ai/judge has no in-repo production caller (route.test.ts only); H1's judge-facing
    harm is latent today and the body-driven dispatch fix is forward-correct.
  LEAD — czech/slovak alphabet_order carries collation multigraphs (CH, DZ, DŽ) that are not tiles;
    playable_letters excludes them, so the packed board format holds for all twelve variants and
    Slice 1 needs no multigraph handling.
  LEAD — the eight newest lexicons are machine-authored without second-opinion review (AGENTS.md);
    exemplars were deliberately chosen as high-frequency everyday nouns to minimize exposure.
Enumeration widened: none — all consumers of the dispatch functions were enumerated (move route,
  judge route, prompts.test.ts, ai-turn-simulation.test.ts); no other importer exists.
```

Context pressure: comfortable — well under half of the window consumed, no truncation pressure.

Report justification: new-evidence
Authority expiry: this Worker exchange's authority ends with the submission of this report; no implementation, mutation, or follow-on authority survives it.
Smallest next step: ORCHESTRATOR reviews this design and, if accepted, issues the Slice 1 implementation prompt (`Native planning mode: not-used`, fresh Worker session, the three-file path allowlist above, tier E1).
