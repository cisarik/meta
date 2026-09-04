### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 06, Worker exchange ordinal 01

status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 529e6910ddf57dfbb4a9671bbab668b975067cf8
Result evidence: bounded

```text
Acceptance candidate: commit 529e6910ddf57dfbb4a9671bbab668b975067cf8, parent 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
Acceptance owner map: this session did not design, implement, or author the candidate; it is not the
    session-05 subagent and not the ORCHESTRATOR that re-measured the same claims
Acceptance allowlist: none — read-only audit
Acceptance risk claims: R1 hold (payload + serializer, both paths) · R2 hold in declared scope ·
    R3 hold · R4 hold · R5 hold · R6 hold
Acceptance control matrix: P1–P5 held; N1–N6 failed as required
Acceptance independence: required-fresh-independent — satisfied
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

Changed paths and purpose: **none.** Read-only audit of `529e691`. No tracked byte mutated.
Authorized Git or side-effect result: none. `git ls-remote` and `git fetch --dry-run` only. Test and
build writes were gitignored.

## Section 2 gate (verbatim)

```text
HEAD     529e6910ddf57dfbb4a9671bbab668b975067cf8
HEAD~1   8a50ded8b743d0badf7cca7fc3178a11d4b54be1
HEAD:.ap 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
.ap HEAD 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
status   ## main...origin/main
porcelain (start): empty
ls-remote origin refs/heads/main: 529e6910ddf57dfbb4a9671bbab668b975067cf8
fetch --dry-run: From https://github.com/cisarik/libretiles * branch main -> FETCH_HEAD
ss :(3000|8000): no listeners
venv: backend/.venv/bin/python present
porcelain (END): empty
HEAD after audit: 529e6910ddf57dfbb4a9671bbab668b975067cf8
```

## Verdict per risk claim

**R1 HOLD (payload + ingest).** `_wire_board` returns `list[list[dict[str, Any] | None]]` and
`_build_state` emits `state_schema_version` plus that grid. Pytest
`test_f1_two_multicodepoint_tokens_cross_the_wire_losslessly` asserts `SZ`, `DZS`, and a blank-as-`SZ`
on the wire with `"blanks" not in state`. PlacementSerializer accepts those tokens (N1).
ExchangeSerializer accepts `["SZ"]` and `["?"]` and rejects a 17-code-point child (N2) — **this is the
previously missed HTTP 400 gate**: `CharField(max_length=1)` is gone and the child bound is
`MAX_TILE_TOKEN_CODEPOINTS`. ⚠ **Certification limit: R1 is proven for the game-state wire and for
both ingest predicates, not for pixels (Q2).**

**R2 HOLD in declared scope.** `backend/game/serializers.py` has no `max_length=1` letter child and no
`len(...) == 1` letter test; `_is_tile_token_shape` is length-bounded at 16 and requires at least one
Unicode letter. `route.ts` replaced `z.string().length(1)`, `/^[\p{L}?]$/u`, `/^\p{L}$/u`,
`blankAs.length === 1` and `letter.length === 1` with `isTileToken` / `MAX_TILE_TOKEN_CODEPOINTS`.
Remaining `\p{L}` there is a "contains a letter" lookahead, not a one-code-point anchor. Out-of-scope
guards named in the prompt are still present (N6).

**R3 HOLD.** `list_variant_summaries()` returned 12 rows, every keyset
`{slug, display_name, language_code, readiness}`, every `readiness == "playable"`.
`validate_lexicons`: 13 asset(s) audited, 0 failed.

**R4 HOLD.** `prompts.ts` absent from `8a50ded..529e691`. Vitest: `MOVE_PROMPT_VERSION ===
"pfr-s2-core-1"` and `sha256(MOVE_SYSTEM_PROMPT) === c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`.

**R5 HOLD.** `git diff --name-only 8a50ded..529e691 -- '**/migrations/**'` is empty. `_persist_board`
not in the diff. Persisted cell remains `{token, blank_as}` JSON (`GameSession.board_state`).

**R6 HOLD.** `git diff --name-only 8a50ded..529e691 -- backend/assets/` is empty.

## Positive controls — P1 to P5, all HOLD

```text
mypy                    Success: no issues found in 85 source files     EXIT 0
ruff                    All checks passed!                              EXIT 0
manage.py check         System check identified no issues (0 silenced). EXIT 0
pytest                  745 passed, 4 skipped in 265.46s (0:04:25)      EXIT 0
pytest --collect-only   749 tests collected in 7.27s                    EXIT 0
validate_lexicons       13 asset(s) audited, 0 failed                   EXIT 0
npm run typecheck       EXIT 0
npx vitest run          Tests  454 passed | 3 skipped (457)             EXIT 0
npm run lint            EXIT 0
npm run build           EXIT 0, eleven ƒ lines, footer "ƒ (Dynamic) server-rendered on demand",
                        ZERO ○ static.  ss before build: no :3000/:8000 listeners
```

Counts match the expected set. No finding on counts.

**P2 HOLD.** Exact eleven paths, no twelfth:

```text
backend/game/serializers.py · backend/game/services.py · backend/tests/test_api.py
backend/tests/test_atomic_token_persistence.py · backend/tests/test_slovak_engine.py
frontend/src/app/api/ai/move/route.ts · frontend/src/app/game/[id]/page.tsx
frontend/src/components/board/Board.tsx · frontend/src/hooks/useGameStore.test.ts
frontend/src/hooks/useGameStore.ts · frontend/src/lib/types.ts
```

**P3 HOLD.** `_wire_board(...) -> list[list[dict[str, Any] | None]]`; payload:

```text
"state_schema_version": WIRE_STATE_SCHEMA_VERSION,  # 4
"board": _wire_board(session.board_state),
```

No `"blanks"` key in that dict. ⚠ The identifier `blanks` still appears in `get_ai_context` as
`blanks:{ai_state['blanks']}` — that is the **AI compact prompt**, not the game-state wire.

**P4 HOLD.** `prompts.test.ts` asserts `pfr-s2-core-1` and CORE SHA-256 `c7acc270…`; `prompts.ts`
absent from the diff.

**P5 HOLD.** No migration path in the commit. `backend/assets/` diff empty.

## Negative controls — N1 to N6, all FAILED as required

**N1 FAILED as required (the placement predicate has teeth).** Throwaway Django process,
`MAX_TILE_TOKEN_CODEPOINTS == 16`.

```text
ACCEPT   SZ -> valid, letter SZ        DZS -> valid, letter DZS
         L·L -> valid, letter L·L      Á  -> valid, letter Á
         ? with blank_as=A -> valid, letter ?, blank_as A
         ? bare -> INVALID: "blank_as: This field is required for blank tiles."
REJECT   ""    -> "letter: This field may not be blank."
         a · S Z · 1 · · · 17×A -> "letter: Must be an uppercase tile token."
SHARED   _is_tile_token_shape("?") False · _tile_token("?", allow_blank=True) -> "?"
         _tile_token("?", allow_blank=False) raises
         _is_tile_token_shape("1") False · _is_tile_token_shape("·") False
```

⭐ **A length-test-only drop would have accepted `1` and `·`. It did not.**

**N2 FAILED as required.**

```text
["SZ"]  -> valid, ["SZ"]
["?"]   -> valid, ["?"]
[17×A]  -> INVALID: "letters[0]: Ensure this field has no more than 16 characters."
```

**N3 FAILED as required (the blank branch still exists).**

```text
letter=? + blank_as=A  accepted        letter=? bare          rejected (blank_as required)
letter=A + blank_as=?  rejected        letter=? + blank_as=?  rejected
exchange ["?"]         accepted        _tile_token("?", allow_blank=False)  rejected
```

**N4 FAILED as required (the refusal has teeth).** Focused re-run: 4 passed — schema pin, accept v4,
refuse `5/99/3/undefined/null/"4"/NaN` with `console.error` ×7, and keep an already-accepted state.
Reasoned counterfactual: removing the guard block would fail `expect(gameState).toBeNull()` on each
bogus payload, fail `toHaveBeenCalledTimes(7)`, and fail the survival test because version 99 would
overwrite the accepted state. **It asserts refusal and survival, not existence.**

**N5 FAILED as required (canary green, file unedited).** `test_atomic_tile_tokens.py` absent from the
diff; `test_interpunct_token_loads_places_scores_and_validates` → `1 passed in 0.03s`. Still asserts
`token.isalpha() is False` and `len(token) == 3` for `L·L`.

**N6 FAILED as required (out-of-scope guards remain).**

```text
prompts.ts:190      GRID_ROW = /^[\p{L}.]{15}$/u
rack.ts:1           UNICODE_TILE = /^[\p{L}?]$/u
diagnostics.py:373  len(blank) == 1 and blank.isalpha() and blank in playable
diagnostics.py:374  len(normalized) == 1 and normalized.isalpha()
diagnostics.py:782  len(ch) == 1 and "A" <= ch <= "Z"
diagnostics.py:789  len(folded) == 1 and folded.isalpha() and not _ascii_letter(folded)
```

## Q1 — the re-pointing is honest, with one required inversion that IS the slice

Evidence: `git diff 8a50ded..529e691` on the three test files.

```text
test_api.py       board[7][7:9] == "AT" and board[7][7:10] == "JOE" became CELL EQUALITY on the same
                  coordinates. Same occupancy invariant, new cell shape. Not weakened to "board exists".
test_p7_*         renamed. 15-char strings + sidecar `blanks` became a 15x15 cell grid,
                  `"blanks" not in state`, and blank identity inside {token:"?", blank_as:"A"}.
                  Same lossless English blank board, new mechanism.
test_p8_*         renamed from "adapter raises on multicodepoint" to "wire carries a multicodepoint
                  token". ⚠ The WRITTEN assertion inverted (raise -> carry). The CLAIMED invariant is
                  "never silently mangled". The old raise was the temporary adapter's SUBSTITUTE for
                  losslessness; the new test asserts board[0][0] == {token: SZ, blank_as: None} plus
                  state_schema_version. A mechanism replacement, not a quiet soften-to-exists.
                  New F1/F4/F5 add teeth the old file did not have.
test_slovak_engine.py:205   ⛔ THIS DID INVERT, and the auditor judged it correct.
                  The old assert passed because of a ONE-CODE-POINT SHAPE RULE, not because CH is
                  unplayable in Slovak. PlacementSerializer has no variant in scope, so any shape
                  rule that accepts SZ must accept CH. The replacement asserts the serializer accepts
                  CH **and** `"CH" not in load_variant("slovak").playable_letters`, also pinned at
                  test_atomic_tile_tokens.py:237. Engine membership is what evaluate_scoring_move uses.
```

## Q2 — ⛔ R1 IS NOT CERTIFIED FOR THE HUMAN-VISIBLE BOARD

```text
glob **/*Board*.test.*                                       -> 0 files
frontend/src/components/**/*.{test,spec}.{ts,tsx}            -> no Board / Cell / Tile test
the only renderLabeledBoard hits are AI prompt helpers in prompts.test.ts, not Board.tsx
```

`Board.tsx` does consume the new shape — `boardCellLetter`, `boardCell?.token === "?"`,
`grid[row][col]` as `BoardCell`. ⚠ **That is a COMPILE-TIME contract (typecheck, lint, build all
held), not a render test.**

⇒ **This acceptance certifies the wire payload and the ingest predicates. It does not certify pixels.**

## Q3 — the deploy coupling is real, and version skew is USER-SILENT

```text
WIRE_STATE_SCHEMA_VERSION = 4 in backend/game/services.py AND frontend/src/lib/types.ts
isSupportedStateSchemaVersion is EXACT EQUALITY; the backend always emits 4; no dual-accept window
⇒ frontend and backend of this commit MUST SHIP TOGETHER.
new client + old/missing version   setGameState console.error(...) and return; gameState stays null
                                   or keeps the last accepted state; Board falls back to EMPTY_BOARD
                                   ⛔ NO toast, NO banner, NO dedicated copy. A user can sit on an
                                   empty board with only a console line.
old client + new backend           NO refusal at all — the guard is introduced in this commit, which
                                   is why simultaneous ship is mandatory.
```

The decided posture in the code comments is *"refuse rather than mis-render"*, and it **holds**. ⚠ It
is **not** a user-facing error screen.

## Deviations, risks, missing evidence

```text
no count deviation.
MISSING FOR CERTIFICATION   no Board render test; no separate HTTP view-level exchange of SZ beyond
                            the serializer plus the suite (⭐ and the previously missed gate WAS the
                            serializer, so that is the one that mattered).
RESIDUAL RISK               version skew is user-silent; the remaining one-code-point assumptions
                            below will block Hungarian on later surfaces even though this wire slice
                            holds.
```

`Resolved Execution Issues / Near-Misses:` the pytest summary was invisible for ~280 s because the
command was piped to `tail -40`; cause `-q` plus tail buffering until the suite ends; resolution
waited; residual none. N1's bare `?` is serializer-invalid without `blank_as`; resolution tested `?`
both bare and with `blank_as=A`, plus N3; residual none.

`Pre-Existing Failure Classification:` none

---

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

```text
· get_ai_context still interpolates joined 15-character `grid` rows plus blanks:{ai_state['blanks']}.
  build_ai_state_dict does "".join(row_chars) and ai_rack="".join(ai_rack). A cell letter SZ makes a
  row longer than 15; GRID_ROW then DROPS it. The AI compact state is still a one-code-point joined
  string. ⚠ AND test_atomic_tile_tokens.py:532 still asserts len(row) == 15 on that grid.
· prompts.ts:250  formatRackMultiset uses trimmed.split("").join(" ")
· prompts.ts:267  rows[row][col] indexes a string as one column per UTF-16 unit
· ai-turn-simulation.test.ts:119  board.map((row) => row.split(""))
· AIThinkingOverlay.tsx:72  word.toUpperCase().split("")
· BlankPicker.tsx:8  "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("") as the fallback when gameState.alphabet
  is absent
· constants.ts  TILE_POINTS is A-Z plus "?" only (session tile_points is preferred when present)
· move_search.py:33  _BLANK_LETTERS = string.ascii_uppercase  default blank alphabet
· legality.py:28  LETTERS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ") default; and :143 the error copy
  still says "Letter must be A-Z or '?'" even though the check is set membership
· gamecore/state.py  AIState still types grid: list[str] + blanks
· test_slovak_ranked_search.py:67-76  encodes /^[\p{L}?]$/u as len(...) == 1 and .isalpha()
· test_slovak_full_game.py:106,111  assert len(blank_nfc) == 1 / assert len(letter_nfc) == 1
· test_czech_polish_variants.py:89  assert all(len(token) == 1 for token in tiles)
· services.py  _word_passes_dictionary: `if not w.isalpha()` — 'L·LA'.isalpha() is False, so
  dictionary ingest still REJECTS interpunct words
· version-skew UX: empty EMPTY_BOARD, console.error only
```

**LEAD**

```text
· JS value.length in isTileToken counts UTF-16 UNITS; Python len counts CODE POINTS. BMP Hungarian
  matches; a SUPPLEMENTARY-PLANE tile would disagree. Not exercised.
· Tile.tsx will paint SZ as one string in a fixed-size square; overflow and layout are untested (Q2).
· isPlausibleRack without `alphabet` still uses UNICODE_TILE. Live _build_state DOES send
  alphabet: list(variant.playable_letters), so the fallback is the live hazard only if a payload
  omits it.
```

**⭐ REQUIRED FIELD — the remaining one-code-point inventory, any spelling, including out of scope**

```text
 1  prompts.ts:190           GRID_ROW = /^[\p{L}.]{15}$/u
 2  prompts.ts:250           split("") on a rack string
 3  prompts.ts:267-274       rows[row][col] / === "."
 4  rack.ts:1                UNICODE_TILE = /^[\p{L}?]$/u
 5  diagnostics.py:373,374,782,789   four len == 1 letter guards
 6  gamecore/state.py:44,49  joined AI grid and joined ai_rack
 7  move_search.py:33        string.ascii_uppercase blank letters
 8  legality.py:28           default LETTERS A-Z
 9  BlankPicker.tsx:8        "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")
10  AIThinkingOverlay.tsx:72 word.split("")
11  ai-turn-simulation.test.ts:111-123   15-dot rows and split("")
12  constants.ts             TILE_POINTS A-Z keys
13  rack.test.ts:4           English split("")
14  test_slovak_ranked_search.py:75-76,93
15  test_slovak_full_game.py:106,111
16  test_czech_polish_variants.py:89
17  test_atomic_tile_tokens.py:532   AI grid len(row) == 15
18  services.py:218          _word_passes_dictionary w.isalpha() — rejects L·L as a word
19  legality.py:143          error string "A-Z" (the check itself is set membership; the COPY is not)
```

⇒ **Declared-scope files `serializers.py` and `route.ts` retain no one-code-point letter guard.**

---

Smallest next step: ORCHESTRATOR opens C1b; **do not treat this PASS as closure of
multilingual-expansion-campaign.**

`Report justification:` final-acceptance
`Logical-whole closure: not-closed`

Authority-expiry statement: this Worker's authority expires at this terminal report. No further
mutation, re-audit, or archival is authorized from this grant.

**Context pressure: HIGH.** Full backend suite, full frontend suite, production build, serializer
interpreter controls, and a multi-pattern remaining-guard search all sat in one exchange. ⚠ *"The
remaining-guard inventory is the part most at risk of an unseen spelling; it is a search, not a proof
of absence."*
