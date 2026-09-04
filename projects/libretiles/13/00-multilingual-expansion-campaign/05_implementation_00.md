You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Prior logical whole identity: multilingual-expansion
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: MEC-C1a-third — a multi-code-point tile crosses the wire losslessly, on BOTH the placement and the exchange path. Every letter guard in the classified inventory of section 3 is removed. The AI's board view and the dictionary authority are later exchanges.
Phase: Implementation
Implementation authority: explicit
Exact baseline: 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
Changed-path allowlist: backend/game/services.py · backend/game/serializers.py · backend/tests/test_atomic_token_persistence.py · backend/tests/test_api.py · backend/tests/test_slovak_engine.py · frontend/src/lib/types.ts · frontend/src/components/board/Board.tsx · frontend/src/app/game/[id]/page.tsx · frontend/src/app/api/ai/move/route.ts · frontend/src/hooks/useGameStore.ts · frontend/src/hooks/useGameStore.test.ts
Implementation boundaries: change the WIRE PROJECTION of the board and the two letter-shape predicates. NO change to the persisted board_state shape, to any asset, manifest, lexicon or build script, to prompts.ts, to gamecore/, to diagnostics.py, or to any provider surface. ONE commit.
Independence required: no
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Evidence tier: E3
Evidence tier basis: a wire-format change to a shipped, playable product with TWELVE variants and live human-vs-human multiplayer. It removes guards that currently fail closed and replaces them with a shape the client must interpret. A guard that raises is loud; a wrong board is silent.
Authorized implementation stages: repository gate, re-run the six inventory commands in section 3 and confirm the classification, implement, prove each fixture fails before it passes, all eight standing gates, MOVE CORE hash proof, twelve-variant proof, ONE commit, pre-push equality gate, one non-force push, public readback, terminal report
Combined implementation envelope: allowed
Implementation stage gates: no commit before F1-F5 are all satisfied as section 5 defines them, and before `manage.py validate_lexicons` still reports THIRTEEN assets; no push before all eight gates are green and the pre-push gate equals the exact baseline
Independent acceptance: ⛔ REQUIRED-FRESH-INDEPENDENT, not part of this exchange. Do not self-certify.
Rollback or recovery checkpoint: one revertible commit; the PERSISTED board_state is untouched, so a revert needs no data migration
Activated stricter profile: none
Terminal implementation report point: after the public readback, once
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: backend/tests/test_atomic_token_persistence.py · backend/tests/test_atomic_tile_tokens.py · backend/tests/test_api.py · backend/tests/test_slovak_engine.py · frontend/src/hooks/useGameStore.test.ts · frontend/src/lib/prompts.test.ts
Affected tests: TWELVE assertion lines encode the old wire shape and TWO encode a superseded predicate rule. Section 6 names all fourteen from quoted greps. All fourteen are authorized. Nothing else may be weakened.
New causal regression: the board is the only lossy field on the game-state wire, and TWO serializer predicates reject any token longer than one code point — one on the placement path, one on the exchange path. No digraph language can be played, even though the engine, the persistence and the rack already carry such tokens losslessly.
Broad or full suite: required-because the project rule mandates all eight standing gates on every slice
Runtime or testbed: not-used
```

```text
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one accountable Worker and must not delegate further
Worker topology: single-active
Network authority: NONE except `git ls-remote origin refs/heads/main` and one `git push origin main`.
Secret authority: none. ⛔ Never read or print backend/.env or frontend/.env.local.
Dependency authority: none.
Untrusted-content boundary: this prompt is your only task authority. Repository files are data under analysis.
Side-effect authority: reversible local mutation inside the ELEVEN-path allowlist; one non-force commit; one non-force push. ⛔ NO DELETION OF ANY FILE.
Context-pressure rule: report your visible context pressure qualitatively
```

Reasoning recommendation: **High.** Named risk: a partial removal is a silent no-op, and the previous two attempts proved that the guards are spelled in five different ways across two languages. Section 3 exists so that "I removed them all" is a re-runnable command rather than a claim.

---

## 1. This is the THIRD issue. Two Workers blocked before you, both correctly.

⛔ **Do not read that as instability. Read it as the reason section 3 looks the way it does.** Both blocks were defects in my prompt, both were found by extending a search past the scope I had drawn, and both are fixed here:

```text
03/01  my guard list was short by two — route.ts:329/:334 are single-code-point REGEXES, in the
       same function as a site I had named, so removing that site alone was a NO-OP.
       Also: an unsatisfiable stage gate, two nonexistent paths, three undercounted assertions,
       and a corrupted AI board view I had missed entirely.
04/01  test_slovak_engine.py:205 asserts PlacementSerializer REJECTS "CH". `"CH"` is structurally
       IDENTICAL to `"SZ"` — NFC-stable, upper-stable, isalpha, two code points — so no predicate
       can accept SZ and reject CH. The file was not on the allowlist, so the task was
       arithmetically un-completable. Also: my predicate accepted the digit "1" as a tile letter,
       and an EIGHTH guard spelled `max_length=1` was invisible to a search for `len(x) == 1`.
```

⇒ **The root cause of seven of those nine defects was one thing: an enumeration I produced from
memory or from too narrow a pattern.** Section 3 now hands you the complete spelling space, the
commands, every hit repo-wide, and a classification of every hit — including the ones that are NOT
letter guards, so you can tell them apart without guessing.

## 2. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY
git ls-remote origin refs/heads/main  # MUST be 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
ss -tlnp | grep -E ':(3000|8000)'     # a listener means STOP AND REPORT; never pkill
ls backend/assets/variants/ | wc -l   # MUST be 12
```

Any difference: classify with all five canonical recovery classes — `accepted-continuation`, `unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence `unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation > unpublished-candidate` — and stop. **The repository owner commits to `main` himself.** ⛔ Never attach or update `.ap`.

## 3. ⛔ THE COMPLETE LETTER-GUARD INVENTORY — six spellings, every hit, classified

**Run all six commands and report their output.** They cover the whole spelling space a
single-code-point letter guard can take in this codebase: Python `len`, DRF `max_length`, Zod
`.length()`, TypeScript `.length ===`, a regex anchored around one `\p{L}`, and `charAt(0)`.

```bash
git grep -nE 'len\([a-z_.]+\) == 1'  -- backend/game backend/gamecore frontend/src   # I measured 12
git grep -nE 'max_length=1[^0-9]'    -- backend/game backend/gamecore frontend/src   # I measured 1
git grep -nE '\.length\(1\)'         -- backend/game backend/gamecore frontend/src   # I measured 2
git grep -nE '\.length === 1'        -- backend/game backend/gamecore frontend/src   # I measured 6
git grep -nE '\^\[?\\p\{L\}'         -- backend/game backend/gamecore frontend/src   # I measured 4
git grep -nE 'charAt\(0\)'           -- backend/game backend/gamecore frontend/src   # I measured 2
```

⚠ **Note the `[^0-9]` in the second pattern.** Without it, `max_length=1` also matches
`max_length=100` at `serializers.py:222`, which is a game-id field and not a letter guard. I hit
that false positive myself; the refined pattern gives one hit, not two.

### 3.1 ⛔ IN SCOPE — the EIGHT letter guards you must remove

```text
G1  backend/game/serializers.py:275   len(nfc) == 1 and nfc.isalpha() and nfc == nfc.upper()
                                      the PLACEMENT predicate. Both clauses change — see D-7.
G2  backend/game/serializers.py:248   ExchangeSerializer.letters child=CharField(max_length=1)
                                      the EXCHANGE predicate, used by views.py:304 (human) AND
                                      views.py:475 (AI). ⛔ Leaving this makes G3-G8 a NO-OP for
                                      the exchange path: the route would forward `SZ` and the
                                      backend would answer HTTP 400.
G3  frontend/src/app/api/ai/move/route.ts:123    letter: z.string().length(1)
G4  frontend/src/app/api/ai/move/route.ts:127    blank_as: z.string().length(1).optional()
G5  frontend/src/app/api/ai/move/route.ts:329    !/^[\p{L}?]$/u.test(letter)
G6  frontend/src/app/api/ai/move/route.ts:334    !/^\p{L}$/u.test(blankAs)
G7  frontend/src/app/api/ai/move/route.ts:341    blankAs && blankAs.length === 1
G8  frontend/src/app/api/ai/move/route.ts:1002   typeof letter === "string" && letter.length === 1
                                      ⚠ G8 filters playability.exchange_letters — RACK tokens, a
                                      different path from G3-G7, and the one G2 sits downstream of.
```

⛔ **G5 and G6 are the ones that make G7 matter.** Removing G7 while a `^…$`-anchored `\p{L}`
stands is a complete no-op: `normalizePlacementData` still returns `null` for `SZ`.

### 3.2 ⛔ OUT OF SCOPE — every other hit, named so you can recognise it

```text
NOT A LETTER GUARD, leave alone:
  diagnostics.py:958   len(modes) == 1          a mode count
  services.py:667      len(leaders) == 1        a tie test
  board.py:82,:84 · game.py:218 · rules.py:16,:18   row/col/leader counts
  serializers.py:222   max_length=100           a game-id length
  Board.tsx:427,:468,:502   event.touches.length === 1   TOUCH handling
  prompts.ts:316       gridRows.length === 15   a row count
  draw/[id]/page.tsx:24 · game/[id]/page.tsx:133   part.charAt(0).toUpperCase()   title-casing
A LETTER GUARD, but a LATER exchange — ⛔ DO NOT TOUCH:
  diagnostics.py:373,:374,:782,:789   four letter guards -> exchange C1c
  prompts.ts:190       GRID_ROW = /^[\p{L}.]{15}$/u   -> exchange C1b
  frontend/src/lib/rack.ts:1   UNICODE_TILE = /^[\p{L}?]$/u  -> exchange C1b
```

⚠ **`prompts.ts:190` and `rack.ts:1` are real defects and they are deliberately not yours.**
`GRID_ROW` requires exactly fifteen characters, so a digraph row is sixteen and is **silently
dropped** — the model would receive a short board. That is exchange C1b, whose subject is exactly
"the places a letter is still one code point after the wire is fixed". If you fix them here, the
next exchange has nothing to verify and its independent acceptance loses its subject.

### 3.3 The adapter, and what is already lossless

```bash
git grep -nE "_WIRE_ADAPTER_REMOVAL|_legacy_wire_board_and_blanks|len\(token\) > 1|len\(realized\) > 1" -- backend/game/services.py
#   I measured SEVEN: :321 :327 :355 :356 :358 :359 :442
```

```text
ALREADY LOSSLESS — do NOT "fix":
  models.py:31   board_state JSONField, structured cells                    correct already
  services.py:459 "my_rack": list(my_slot.rack) · types.ts:65 my_rack: string[]
  Board.tsx · board/Cell.tsx · tiles/Tile.tsx · tiles/TileRack.tsx   no letter assumption
  consumers.py   forwards get_game_state_for_user verbatim; multiplayer comes along for free
  move history and starting draw   services.py:96-110 and :525-531 pass whole tokens through
```

### 3.4 The board consumers you must update — the complete set

```text
types.ts:48        board: string[]
types.ts:49        blanks: { row: number; col: number }[]
Board.tsx:119      grid = gameState?.board ?? Array(BOARD_SIZE).fill(".".repeat(BOARD_SIZE))
Board.tsx:120-122  blanks = new Set((gameState?.blanks ?? []).map(...))
Board.tsx:556      const boardLetter = grid[row]?.[col];
Board.tsx:597      const boardLetter = grid[row]?.[col] ?? ".";
Board.tsx:615      isBlank={pending ? pending.letter === "?" : blanks.has(key)}
page.tsx:1212      const boardLetter = gameState?.board?.[row]?.[col];
useGameStore.ts:151 setGameState — the SINGLE ingress choke point for every game-state payload,
                   REST and websocket alike. D-3's refusal belongs here, which is why
                   play/page.tsx and waiting/[id]/page.tsx need no edit.
```

## 4. The design — eight decisions plus two corrections. Implement; do not re-decide.

```text
D-1  board: BoardCell[][] — exactly 15 rows of 15. BoardCell = { token: string; blank_as: string |
     null } | null. `null` for empty, because services.py:341-344 already treats a non-dict
     persisted cell as empty. A GRID, because both consumers index by coordinate.
D-2  `blanks` is REMOVED from the payload — a second source of truth for a fact the cell carries.
D-3  `state_schema_version: 4` is a NEW field. It exists nowhere today but the adapter's comment
     text and one test assertion, so you INTRODUCE it. The value 4 is INHERITED from that text.
     The client REFUSES a version it does not understand rather than mis-rendering one, and the
     refusal lives in setGameState.
     ⚠ NAMING COLLISION: gamecore/state.py:79 already calls its SAVE-FILE format "schema 4"
     (`_require_schema_4`). Two different axes that share a number. Do not unify them.
D-4  the client store goes 5 -> 6 with an explicit `version < 6` branch. The store persists
     PREFERENCES, not game state, so the branch may have nothing to do — and if so it must SAY so
     in a comment rather than be omitted.
D-5  the AI's board view and the dictionary authority are LATER exchanges.
D-6  the PERSISTED board_state shape does not change; NO Django migration.
D-7  ⛔ THE PLACEMENT PREDICATE, and it has FOUR clauses, not three. `serializers.py:275` currently
     reads `len(nfc) == 1 and nfc.isalpha() and nfc == nfc.upper()`. The replacement must accept a
     token that is:
        (a) non-empty
        (b) NFC-stable
        (c) equal to its own uppercase form
        (d) free of whitespace and of control characters
        (e) ⛔ CONTAINING AT LEAST ONE UNICODE LETTER
     ⛔ CLAUSE (e) IS NOT OPTIONAL AND IT IS WHY `.isalpha()` CANNOT SIMPLY STAY. Measured:
        'L·L'.isalpha() is False   -> so `.isalpha()` must GO, or the canary is rejected
        '1'  has no letter at all  -> so without (e), a DIGIT becomes a valid tile letter
        '·'  has no letter at all  -> without (e), a bare middle dot becomes valid
     Verified: with (e), `SZ` `DZS` `L·L` `Á` all pass and `1` `·` `` `a` `S Z` all fail.
     ⚠ AND RECORD WHY THIS DEVIATES from gamecore/variant_store.py's `_parse_asset_token`, which
     accepts `"1"`: that loader validates tokens DECLARED BY A MAINTAINER in a committed asset,
     while this serializer validates UNTRUSTED PUBLIC INPUT. Different threat models justify a
     stricter predicate. Say so in a comment, so nobody later "harmonizes" them.
D-8  ⛔ BOUND THE LENGTH, on BOTH predicates. `gamecore/variant_store.py:22` declares
     MAX_TILE_TOKEN_CODEPOINTS = 16 for exactly this reason. Bound G1 and G2 at that same value and
     name the shared constant in a comment rather than writing a bare 16.
     ⚠ G2 is a DRF `CharField(max_length=…)`; that is the natural place for its bound.
D-9  ⛔ NEW. G2's replacement must accept the same token vocabulary as G1. An exchange letter and a
     placement letter are the same kind of thing, so two different predicates for them would be a
     defect waiting to happen. Factor the shared predicate rather than writing it twice.
     ⛔ AND THE BLANK IS THE TRAP IN THAT REFACTOR. I verified: the five clauses above REJECT `"?"`,
     because a question mark contains no letter. Today that is harmless — `serializers.py:273-274`
     early-returns on `allow_blank and nfc == "?"` BEFORE the predicate runs. But a shared
     predicate factored carelessly would move or lose that early return, and then:
        the placement path would reject every blank placement
        the EXCHANGE path would reject exchanging a blank — which is a legal move, and
        `CharField(max_length=1)` accepts `"?"` today, so it is live behaviour you would break
     ⇒ Keep the blank handling explicit and OUTSIDE the shared shape predicate, or give the shared
       predicate its own `allow_blank` parameter. Either is fine; silently dropping it is not.
       F4 and F5 both assert `"?"` for exactly this reason.
D-10 ⛔ NEW. test_slovak_engine.py:205 and :207 are re-pointed, and section 6 says how and why.
```

## 5. Fixtures — FIVE

```text
F1  TWO DIFFERENT MULTI-CHARACTER TOKENS end to end through the wire projection.
    ⛔ NOT only `SZ`. Use `SZ` and one of `DZS` or `LJ`. Include one placed as a blank
    (token "?", blank_as "SZ"). Host: test_atomic_token_persistence.py.
    ⚠ SYNTHETIC TOKENS ARE CORRECT: no shipped variant has a digraph tile, which is exactly why
    twelve could ship before this change. Hungarian is the first real consumer and lands later.
F2  THE L·L CANARY still passes, unmodified. test_atomic_tile_tokens.py:243-284 owns it and that
    file is OFF the allowlist. Run it, quote before and after.
F3  A PAYLOAD WITH AN UNKNOWN state_schema_version IS REFUSED BY THE CLIENT.
    Host: frontend/src/hooks/useGameStore.test.ts. Assert the REFUSAL, not the absence of a crash.
F4  THE PLACEMENT PREDICATE. PlacementSerializer ACCEPTS `SZ`, `DZS`, `L·L`, `Á`, and `?`;
    REJECTS ``, `a`, `S Z`, `1`, `·`, and a 17-code-point token. Host:
    test_atomic_token_persistence.py.
    ⚠ `1` and `·` are the D-7 clause-(e) cases and `L·L` is the one F2 cannot reach.
    ⛔ `?` IS IN THE ACCEPT LIST DELIBERATELY — see D-9. The five clauses reject it, and only the
    explicit blank branch saves it, so a careless shared-predicate refactor breaks blank placement
    and this case is what catches it.
F5  ⛔ NEW. THE EXCHANGE PREDICATE. ExchangeSerializer accepts a `letters` list containing `SZ`,
    accepts a list containing `?` — exchanging a blank is a legal move and works today — and
    rejects a 17-code-point entry. Host: test_atomic_token_persistence.py.
    ⚠ Without F5, G2 could be left in place and every other change would still look green.
```

Pre-fix capture:

```text
CLASS B  F1, F3, F4 and F5 must each be shown to FAIL against the unmodified code, with the
         failure text quoted. F1 fails because the adapter RAISES — quote it. F3 fails because no
         version field exists. F4's `L·L` case fails on `.isalpha()`; quote that specific line,
         because it is the defect D-7 clause (e) exists to fix. F5 fails on `max_length=1`.
         F2 must PASS both before and after. A canary that changes state is not a canary.
```

## 6. The FOURTEEN authorized assertion re-pointings

Derived from two commands, not from memory:

```bash
git grep -nE 'state\["board"\]|state\["blanks"\]|\["state"\]\["board"\]|_WIRE_ADAPTER_REMOVAL|_legacy_wire_board_and_blanks' \
  -- backend/tests/test_atomic_token_persistence.py backend/tests/test_api.py     # I measured 12
git grep -nE 'letter": "CH"|letter": "1"' -- backend/tests/test_slovak_engine.py  # I measured 2
```

```text
TWELVE old-wire-shape lines:
  test_atomic_token_persistence.py:12,16   the two adapter imports
  test_atomic_token_persistence.py:247,248,249,250,251,253   the fifteen-string board AND
      :251 `state["blanks"] == [{"row": 7, "col": 7}]` — ⚠ my previous issue's pattern did not
      search `state["blanks"]` and therefore missed this one. That is why the count moved from
      eleven to twelve.
  test_atomic_token_persistence.py:264,266   the raise-message equality and the direct call
  test_api.py:1078   data["state"]["board"][7][7:9] == "AT"
  test_api.py:1324   data["state"]["board"][7][7:10] == "JOE"

TWO superseded-predicate lines, and ⛔ THIS IS DECISION D-10:
  test_slovak_engine.py:205  assert not PlacementSerializer(letter="CH").is_valid()
  test_slovak_engine.py:207  assert not PlacementSerializer(letter="1").is_valid()
```

⛔ **Why `:205` must change, and it is not a concession.** `"CH"` is structurally identical to
`"SZ"` on every dimension a serializer can see, so no predicate satisfying F4 can reject it. But
the deeper point is that **the assertion was passing for the wrong reason**: `PlacementSerializer`
has **no variant in scope** — it cannot know whether `CH` is a tile in the game being played.
Shape is the serializer's job; playability is the engine's, and **the same file already asserts the
playability half at `:237`** (`"CH" not in variant.playable_letters`).

⇒ Re-point `:205` to assert **shape-valid, engine-rejected**, and in the comment say that the
playability half lives thirty lines below at `:237`. **`:207` is restored by D-7 clause (e)** — a
digit contains no letter — so its assertion survives once the predicate is right, and the comment
should say that it now holds for a better reason than a length limit.

⛔ **Do not delete any test.** Each of the fourteen encodes an invariant that still holds; only the
mechanism changes. **In each test's own comment, say what it used to assert and why the replacement
is the same invariant.** A deleted test is indistinguishable from a lost one.

## 7. Required proofs

```text
P-A  MOVE CORE UNCHANGED. prompts.test.ts pins sha256(MOVE_SYSTEM_PROMPT) ==
     c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60 and pfr-s2-core-1.
     prompts.ts is NOT on the allowlist. Quote the passing assertion.
P-B  TWELVE VARIANTS STILL PLAYABLE. validate_lexicons still THIRTEEN assets, 0 failed, and
     test_czech_polish_variants.py — OFF the allowlist, needing no change — still passes.
     ⛔ state_schema_version belongs to the GAME-STATE payload, never to a variant row.
P-C  THE ADAPTER IS GONE. Re-run the section 3.3 command and report its output, plus
     `git grep -in "_WIRE_ADAPTER_REMOVAL"`. Report BOTH cases.
P-D  ⛔ NO LETTER GUARD REMAINS IN SCOPE. Prove it by RE-RUNNING ALL SIX section-3 commands and
     reporting their output, then stating for every remaining hit which out-of-scope class in 3.2
     it belongs to. **Do not report a count.** Two previous issues of this prompt failed exactly
     there: a count from a list is not a proof, and a count from ONE pattern is not a proof either.
```

## 8. What must not change

```text
⛔ NO change to the persisted board_state shape, and NO Django migration.
⛔ NO byte under backend/assets/ may change. `git status --porcelain=v1 -- backend/assets/` MUST
   be EMPTY at every point.
⛔ NO change to frontend/src/lib/prompts.ts — including GRID_ROW at :190, which IS a real defect
   and belongs to exchange C1b. P-A is the proof you did not touch it.
⛔ NO change to frontend/src/lib/rack.ts — UNICODE_TILE at :1 is also C1b's.
⛔ NO change to anything under backend/gamecore/. You may READ variant_store.py for D-7 and D-8;
   reading is not changing.
⛔ NO change to backend/game/diagnostics.py — its four letter guards are exchange C1c's.
⛔ NO change to backend/tests/test_atomic_tile_tokens.py — it owns the canary, to be OBSERVED.
⛔ NO change to components/board/Cell.tsx, components/tiles/Tile.tsx, components/tiles/TileRack.tsx.
⛔ NO deletion of any test file. Section 6's fourteen lines are the authorized re-pointing.
NO provider list, provider constant, model tuple, provider tier or provider documentation, ANYWHERE.
NO new dependency, no lockfile edit, no mypy scope change.
NO reading backend/.env or frontend/.env.local.
NO `git add -A`, no `git add .`, no force, amend, rebase, reset, clean, stash, branch, tag.
NO writing under /home/agile/meta/ and no temporary file outside /tmp/opencode/mec-c1a3/.
```

✅ **Cross-check performed when this prompt was written, over BOTH obligations and test hosts.**
Sections 4-7 require edits to: `services.py` (projection), `serializers.py` (G1, G2, the shared
predicate, both bounds), `test_atomic_token_persistence.py` (nine lines plus F1, F4, F5),
`test_api.py` (two lines), `test_slovak_engine.py` (two lines per D-10), `types.ts`, `Board.tsx`,
`page.tsx`, `route.ts` (G3-G8), `useGameStore.ts` (refusal, migrate) and `useGameStore.test.ts`
(F3). **That is exactly the eleven allowlisted paths, and every one of F1-F5 has a host on the
list.** Section 8 forbids only paths no section asks you to edit, and it permits READING
`variant_store.py`, which D-7 and D-8 require. If you find a genuine contradiction, stop and report
it rather than choosing an interpretation — two Workers have now done exactly that, correctly.

## 9. Validation

RF-16 route binding, bounded to this task:

```text
Declared route that could not be used: `poetry run <tool>`, as documented in AGENTS.md
Exact alternate, canonical for this task, from backend/ :
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons
Rationale: the client environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
Evidence class: reproduced-dynamic.  Bounded authority: this task only.
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP AND REPORT.
```

⛔ `manage.py check` takes no `-m`. Then from `frontend/`: `npm run typecheck`, `npx vitest run`, `npm run lint`, `npm run build`.

Baseline at `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`, independently re-measured by two Workers and agreeing to the digit:

```text
mypy      Success: no issues found in 85 source files
ruff      All checks passed!
check     System check identified no issues (0 silenced).
pytest    742 passed, 4 skipped        --collect-only  746 tests collected
lexicons  13 asset(s) audited, 0 failed, exit 0
typecheck exit 0        vitest  450 passed | 3 skipped (31 files | 1 skipped)
lint      exit 0        build   exit 0, ELEVEN dynamic routes, ZERO static
```

⚠ Counts WILL move: you are adding F1, F3, F4 and F5 and re-pointing fourteen assertion lines. Report the new numbers and **account for the delta** — which tests you added, which you re-pointed. Wall-clock times are machine noise.

The four standing traps: a second `-q` silently suppresses the pytest summary; mypy on the FULL documented scope; check `ss -tlnp | grep :3000` before `npm run build` and never pkill; and "the build passed" and "the code type-checks" are TWO SEPARATE CLAIMS.

## 10. Git authority — one commit

```bash
cd /home/agile/Projects/libretiles
git add <the paths you actually changed, named individually>
git status --porcelain=v1                       # MUST be a subset of the ELEVEN-path allowlist
git status --porcelain=v1 -- backend/assets/    # MUST be EMPTY
git diff --cached --stat
git commit -m "feat(wire): a multi-code-point tile crosses the wire losslessly"
git ls-remote origin refs/heads/main            # MUST still be 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
git push origin main                            # one non-force fast-forward push
git ls-remote origin refs/heads/main            # MUST equal `git rev-parse HEAD`
git rev-parse HEAD
```

If the remote advanced between the gate and the push, **stop and escalate**. Never force, amend, rebase, reset, clean, stash, branch, or tag.

## 11. Stopping conditions

```text
the section 2 gate does not match, or backend/assets/variants/ does not hold 12 files
any of the six section-3 commands, or the 3.3 command, returns a different set than I state —
    report both and stop. That is the correction of this issue and it is not a formality.
any hit appears that section 3.2 does not classify — report it and stop rather than deciding
    whether it is in scope
F1, F3, F4 or F5 PASSES before the change — the fixture has no teeth
F2 does not pass BEFORE the change, or stops passing AFTER — do NOT weaken the canary
`git status --porcelain=v1 -- backend/assets/` is non-empty at ANY point
`manage.py validate_lexicons` no longer reports 13 assets, 0 failed
the MOVE CORE hash assertion fails
completing the work would require a path outside the ELEVEN-path allowlist
you would need a Django migration
`git ls-remote` no longer equals the exact baseline at the pre-push gate
```

Stop normally — success — when all six section-3 commands show no in-scope letter guard remaining, the 3.3 command shows the adapter gone, the wire carries `board: BoardCell[][]` and `state_schema_version: 4`, `blanks` is gone from payload and consumer, the store is at version 6 with an explicit branch, F1/F3/F4/F5 are proven to fail before and pass after, F2 passes unchanged both times, the fourteen assertion lines are re-pointed with their invariant restated in a comment, twelve variants remain playable, the MOVE CORE hash is proved unchanged, all eight gates are green, one commit is pushed non-force, and the public readback equals `git rev-parse HEAD`.

## 12. Report contract

The FIRST CHARACTER of your reply must be `#`, so it begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then, in this order: the coordinate line reading `logical whole multilingual-expansion-campaign, Worker session ordinal 05, Worker exchange ordinal 01`; status; `Phase-qualified result:` one value from the closed enum at `PROMPT_CONTRACTS.md:206`; `Result artifact or commit:`; `Result evidence:`; start and end commit; the section 2 gate values verbatim plus an end-of-task porcelain re-confirmation **including `git status --porcelain=v1 -- backend/assets/` shown empty**; changed files and purpose; **the output of ALL SIX section-3 commands and the 3.3 command, BEFORE and AFTER, verbatim, with every remaining hit assigned to an out-of-scope class** — that is proofs P-C and P-D and it replaces any counted claim; **the new wire payload shape quoted from the code including `state_schema_version`**; **the exact diff of every board consumer**; **the store migrate branch as committed**; **the shared letter predicate and both length bounds, quoted, with the shared constant named and the threat-model comment shown**; the test table with F1-F5 and every class B failure quoted verbatim — including F4's `L·L` `.isalpha()` failure and F5's `max_length=1` failure; **the fourteen re-pointed lines, each with its restated invariant comment**; **proof P-A quoted**; **proof P-B**; all eight gates each with its own quoted line, the pytest summary verbatim, the `--collect-only` count with the delta accounted for, and the mypy file count; both separate frontend claims; the Git sequence with the pre-push value, the commit SHA, the push result and the readback equality; deviations, risks, missing evidence; `Resolved Execution Issues / Near-Misses:`; `Pre-Existing Failure Classification:`; then:

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
   Two separate labelled lists: MEASURED and LEAD.
   MEASURED means you ran something and it produced that result. LEAD means you suspect it and
   have not proved it. Do not merge them and do not leave an item unlabelled.
   The two previous attempts at this exact task used this section to catch nine defects in my
   prompts before a single byte changed, including a guard count short by two, a forced logical
   contradiction, a predicate that accepted digits as tiles, and a corrupted AI board view.
   It is the highest-value part of your report and I read it first.
   In particular: if you can see a SEVENTH spelling of a single-code-point letter guard that
   section 3's six commands cannot reach, name it with its file:line. That specific gap has now
   cost two exchanges.
```

then one smallest next step; exactly one report justification from `new-mutation | new-evidence | new-material-risk | changed-external-state | final-acceptance | explicit-closure`; `Logical-whole closure: not-closed`; an authority-expiry statement; and your qualitative context pressure.

⛔ **Your PASS is an implementation PASS and nothing more.** This slice requires fresh independent acceptance from a session that is not a subagent of the Orchestrator, and that is not you.

One value per field. No visible mid-sentence self-corrections. Summarize command output; full output only for failures, unexpected state, or safety-critical evidence.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/
Archival: wait-for-report
```

You do not archive this pair. Your authority expires at your terminal report, and no `PASS` you report closes anything.
