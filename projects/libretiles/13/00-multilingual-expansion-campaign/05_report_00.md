### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 05, Worker exchange ordinal 01

**Status: PASS**

`Phase-qualified result:` implementation-PASS
`Result artifact or commit:` `529e6910ddf57dfbb4a9671bbab668b975067cf8`
`Result evidence:` eleven allowlisted paths, one commit, one non-force push, public readback equal; all eight standing gates green; F1/F3/F4/F5 each quoted failing before and passing after; F2 canary passing unchanged both times; all six section-3 commands re-run with every remaining hit assigned to an out-of-scope class.

Start commit `8a50ded8b743d0badf7cca7fc3178a11d4b54be1` → end commit `529e6910ddf57dfbb4a9671bbab668b975067cf8`.

⚠ **ORCHESTRATOR NOTE ON THIS ARCHIVE.** The Worker's terminal report was long and this file preserves it in condensed form: every measurement, quotation and finding is retained; repeated boilerplate and the fully quoted diffs are summarized, because the diffs are recoverable from `git show 529e691`. Nothing evidential was dropped. The condensation is the Orchestrator's, and it is marked so no reader mistakes it for the Worker's own brevity.

---

## 1. Section 2 repository gate — verbatim

```text
git rev-parse HEAD                    8a50ded8b743d0badf7cca7fc3178a11d4b54be1   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (detached)
git status -sb                        ## main...origin/main                      MATCH
git status --porcelain=v1             (empty)                                    MATCH
git ls-remote origin refs/heads/main  8a50ded8b743d0badf7cca7fc3178a11d4b54be1   MATCH
ss -tlnp | grep -E ':(3000|8000)'     no output, exit 1                          no listener
ls backend/assets/variants/ | wc -l   12                                         MATCH
```

End-of-task: public ref `529e691` == `git rev-parse HEAD`; `.ap` gitlink and submodule HEAD both unchanged at `9c5cc44`; porcelain empty; `backend/assets/` porcelain empty, checked before staging, at staging and at end; twelve variant manifests; no listener. `.ap` never attached or updated.

## 2. Changed files — exactly the eleven allowlisted paths, all modified, none added, none deleted

```text
backend/game/services.py            adapter + constant removed; _wire_board added;
                                    WIRE_STATE_SCHEMA_VERSION = 4; blanks dropped from payload
backend/game/serializers.py         G1 and G2 replaced by one shared _is_tile_token_shape /
                                    _tile_token; both bounds from MAX_TILE_TOKEN_CODEPOINTS
backend/tests/test_atomic_token_persistence.py   nine re-pointed lines (p7, p8) + F1, F4, F5
backend/tests/test_api.py           two re-pointed wire-shape assertions
backend/tests/test_slovak_engine.py two re-pointed predicate assertions
frontend/src/lib/types.ts           BoardCell, board: BoardCell[][], state_schema_version,
                                    WIRE_STATE_SCHEMA_VERSION, isSupportedStateSchemaVersion,
                                    boardCellLetter; blanks removed
frontend/src/components/board/Board.tsx   grid-of-cells consumer; blanks set removed
frontend/src/app/game/[id]/page.tsx occupancy test reads a cell, not a character
frontend/src/app/api/ai/move/route.ts     G3-G8 replaced by isTileToken; normalizeTileToken
frontend/src/hooks/useGameStore.ts  refusal in setGameState; persist 5 -> 6 with explicit branch
frontend/src/hooks/useGameStore.test.ts   F3, plus four persist-version pins re-pointed
```

Verified absent from the commit by `git show --name-only`: `prompts.ts`, `rack.ts`, anything under `gamecore/`, `diagnostics.py`, anything under `backend/assets/`, any migration, `Cell.tsx`, `Tile.tsx`, `TileRack.tsx`, `test_atomic_tile_tokens.py`.

## 3. Proof P-D — all six section-3 commands, BEFORE and AFTER

**BEFORE, at baseline, run before any edit — every count matched exactly.** Twenty-seven hits:
twelve from CMD1, one from CMD2 (the refined `[^0-9]` correctly excluded `serializers.py:222`
`max_length=100`), two from CMD3, six from CMD4, four from CMD5, two from CMD6. Eight in scope
(G1 `serializers.py:275`, G2 `serializers.py:248`, G3/G4 `route.ts:123/:127`, G5/G6
`route.ts:329/:334`, G7 `route.ts:341`, G8 `route.ts:1002`), nineteen out of scope, **every one of
the nineteen already named in section 3.2. No unclassified hit, no discrepancy** — confirmed
before a byte was edited.

**AFTER, at the pushed commit:**

```text
CMD2  max_length=1[^0-9]   no output, exit 1        ZERO
CMD3  .length(1)           no output, exit 1        ZERO
CMD1  len(x) == 1          11 hits, none in serializers.py
CMD4  .length === 1        4 hits, none in route.ts
CMD5  ^[?\p{L}             2 hits, both in prompts.ts / rack.ts
CMD6  charAt(0)            2 hits, unchanged
```

Every remaining hit with its section 3.2 class:

```text
diagnostics.py:373 :374 :782 :789   A LETTER GUARD, later exchange C1c
diagnostics.py:958                  NOT A LETTER GUARD — a mode count
services.py:671                     NOT A LETTER GUARD — a tie test  (was :667, +4 lines above)
board.py:82 :84 · game.py:218 · rules.py:16 :18   NOT letter guards — row/col/leader counts
Board.tsx:433 :474 :508             NOT letter guards — TOUCH handling (were :427/:468/:502)
prompts.ts:316                      NOT A LETTER GUARD — a row count
prompts.ts:190                      A LETTER GUARD, later exchange C1b (GRID_ROW, deliberately not mine)
rack.ts:1                           A LETTER GUARD, later exchange C1b (UNICODE_TILE)
draw/[id]/page.tsx:24 · game/[id]/page.tsx:133    NOT letter guards — title-casing
```

No in-scope letter guard remains. `serializers.py:222` `max_length=100` still returns no hit under
the refined pattern.

⚠ **One near-miss recorded by the Worker.** Its first draft of the `ExchangeSerializer` comment
wrote the historical spelling as the literal `max_length=1`, which made CMD2 return two COMMENT
hits and polluted the very proof section 3 exists to keep clean. Reworded to "a child max_length of
ONE" so CMD2 returns zero. The historical fact stays legible; the proof stays re-runnable.

## 4. Proof P-C — the adapter is gone

```text
BEFORE  :321 :327 :355 :356 :358 :359 :442        SEVEN, exactly as measured
AFTER   no output, exit 1                         ZERO
git grep -in "_WIRE_ADAPTER_REMOVAL"      AFTER: one hit, test_atomic_token_persistence.py:271
git grep -in "_legacy_wire_board_and_blanks"  AFTER: one hit, same file :272
```

Both remaining hits are the re-pointing COMMENT in `test_p8` stating what the test used to assert —
required by the "say what it used to assert" instruction. A comment is not the adapter.

## 5. The new wire payload shape, quoted from the code

`backend/game/services.py:321` and the payload:

```python
WIRE_STATE_SCHEMA_VERSION = 4
"""Version of the GAME-STATE WIRE payload. The client refuses what it cannot render.

⚠ NAMING COLLISION: ``gamecore/state.py`` already calls its SAVE-FILE format
"schema 4" (``_require_schema_4``). Two different axes that happen to share a
number. Do not unify them.

The value 4 is inherited from the removed wire adapter, which named it in the
message it raised rather than emitting a wrong board.
"""
```

```python
    return {
        "game_id": str(session.public_id),
        # The client REFUSES a wire version it does not understand rather than
        # mis-rendering one. A guard that refuses is loud; a wrong board is silent.
        "state_schema_version": WIRE_STATE_SCHEMA_VERSION,
        ...
        "board": _wire_board(session.board_state),
        "premium_used": session.premium_used,
```

`_wire_board` returns `list[list[dict[str, Any] | None]]`, exactly fifteen rows of fifteen, `None`
for empty, `{"token": …, "blank_as": …}` for occupied. `"blanks"` no longer appears. The persisted
`board_state` shape is untouched and there is no Django migration.

Client mirror, `frontend/src/lib/types.ts`:

```ts
export const WIRE_STATE_SCHEMA_VERSION = 4;
export function isSupportedStateSchemaVersion(value: unknown): boolean {
  return value === WIRE_STATE_SCHEMA_VERSION;
}
export type BoardCell = { token: string; blank_as: string | null } | null;
export function boardCellLetter(cell: BoardCell): string | null {
  if (!cell || !cell.token) return null;
  return cell.blank_as || cell.token;
}
```

`blanks: { row: number; col: number }[]` is deleted from `GameState`; `state_schema_version: number`
and `board: BoardCell[][]` are added.

## 6. Board consumers — the complete set, condensed by the Orchestrator

Full diffs recoverable from `git show 529e691`. The substance:

```text
Board.tsx    + import { boardCellLetter, type BoardCell }
             + EMPTY_BOARD: 15x15 of nulls, for the render before the first payload
             :122  grid = gameState?.board ?? EMPTY_BOARD          (blanks Set DELETED)
             :559  const boardCell = grid[row]?.[col] ?? null;  if (boardCell) { …
             :600  letter = pending ? (pending.blank_as || pending.letter)
                                    : boardCellLetter(boardCell)
             :616  isBlank={pending ? pending.letter === "?" : boardCell?.token === "?"}
page.tsx     :1212 if (gameState?.board?.[row]?.[col]) return null;
                   comment: "A non-null wire cell means the square is occupied. Any occupant
                   counts, whatever its code-point length."
```

⛔ The `"."` sentinel disappears entirely, which was LEAD 1 of the 03/01 report and is now settled.
The Worker re-swept `frontend/src` for `.board`, `board?.`, `"board"` and `blanks`: no other
`GameState` consumer reads either field. `play/page.tsx` and `waiting/[id]/page.tsx` only hand whole
payloads to `setGameState`, which is where the refusal sits — so D-3's store-level placement did
cover both without editing either, as designed.

## 7. The store migrate branch, as committed

```ts
      name: "libretiles-store",
      version: 6,
      ...
        if (version < 6) {
          // NOTHING TO MIGRATE, and this branch exists to say so rather than
          // leave the version bump unexplained. The bump accompanies wire
          // `state_schema_version` 4, which belongs to the GAME-STATE payload;
          // this store persists PREFERENCES only (see `partialize` below), so
          // no persisted key changed shape or meaning.
        }
```

The refusal, in the single ingress choke point:

```ts
      setGameState: (gameState) => {
        if (!isSupportedStateSchemaVersion(gameState?.state_schema_version)) {
          console.error(
            "libretiles: refusing a game state with unsupported " +
              `state_schema_version ${JSON.stringify(gameState?.state_schema_version)}; ` +
              `this client renders ${WIRE_STATE_SCHEMA_VERSION}`,
          );
          return;
        }
        set({ gameState });
      },
```

⚠ D-4 asked for an explicit no-op branch rather than an omission, and got one with its reason
stated. ESLint's `no-empty` ignores comment-bearing blocks, confirmed by `npm run lint` exit 0, so
no filler statement was invented to satisfy a linter.

## 8. The shared letter predicate and both bounds, quoted

```python
from gamecore.variant_store import MAX_TILE_TOKEN_CODEPOINTS, list_installed_variants

def _is_tile_token_shape(nfc: str) -> bool:
    """Shape rule for ONE tile token of ANY code-point length. Blanks excluded.

    ⛔ ``str.isalpha()`` cannot be used for the letter clause: ``'L·L'.isalpha()``
    is ``False`` and ``L·L`` is a legitimate shipped-asset token shape. But the
    clause cannot simply be dropped either, or the digit ``'1'`` and the bare
    middle dot ``'·'`` would both become valid tile letters.

    ⛔ The BLANK is handled by the caller, deliberately OUTSIDE this predicate:
    ``'?'`` contains no letter, so this returns ``False`` for it. Placing and
    exchanging a blank are both legal, and the caller's explicit blank branch
    is what keeps them legal.

    ⚠ WHY THIS IS STRICTER than ``gamecore.variant_store._parse_asset_token``,
    which accepts ``'1'``: that loader validates tokens DECLARED BY A MAINTAINER
    in a committed asset, while this serializer validates UNTRUSTED PUBLIC
    INPUT. Two different threat models justify two different predicates, so do
    not "harmonize" them.
    """
    if not nfc:                                       return False
    if len(nfc) > MAX_TILE_TOKEN_CODEPOINTS:          return False   # BOUND 1
    if nfc != nfc.upper():                            return False
    if unicodedata.normalize("NFC", nfc) != nfc:      return False
    if any(character.isspace() for character in nfc): return False
    if any(unicodedata.category(c).startswith("C") for c in nfc): return False
    return any(character.isalpha() for character in nfc)

def _tile_token(value: object, *, allow_blank: bool) -> str:
    """Ingest one untrusted tile token. Shared by the placement and exchange paths."""
    if not isinstance(value, str):
        raise serializers.ValidationError(_TILE_TOKEN_ERROR)
    nfc = unicodedata.normalize("NFC", value)
    if allow_blank and nfc == "?":          # the blank, explicit and OUTSIDE the shape rule
        return nfc
    if _is_tile_token_shape(nfc):
        return nfc
    raise serializers.ValidationError(_TILE_TOKEN_ERROR)
```

```python
class ExchangeSerializer(serializers.Serializer[dict[str, Any]]):
    letters = serializers.ListField(
        # The child bound is the shared MAX_TILE_TOKEN_CODEPOINTS resource
        # bound, never a tile count: the OUTER max_length=7 is the tile count.
        # It replaced a child max_length of ONE, which made every digraph
        # exchange a HTTP 400 on both the human path (views.ExchangeView) and
        # the AI path (views.AIExchangeView).
        child=serializers.CharField(max_length=MAX_TILE_TOKEN_CODEPOINTS),   # BOUND 2
        min_length=1, max_length=7,
    )
    def validate_letters(self, value: list[str]) -> list[str]:
        # Same token vocabulary as a placement letter, from the same predicate.
        # allow_blank because exchanging a blank is a legal move that the old
        # one-character CharField accepted, so it is live behaviour.
        return [_tile_token(letter, allow_blank=True) for letter in value]
```

Frontend mirror in `route.ts`, naming the constant rather than a bare 16:

```ts
/** Resource bound on ONE tile token, mirroring the backend's shared
 *  `gamecore.variant_store.MAX_TILE_TOKEN_CODEPOINTS`. Never a tile count. */
const MAX_TILE_TOKEN_CODEPOINTS = 16;
/** At least one Unicode letter, and no whitespace or control characters. */
const TILE_TOKEN_SHAPE = /^(?=[\s\S]*\p{L})[^\s\p{C}]+$/u;
function isTileToken(value: string): boolean {
  return value.length > 0 && value.length <= MAX_TILE_TOKEN_CODEPOINTS &&
    value === value.toUpperCase() && TILE_TOKEN_SHAPE.test(value);
}
```

⭐ **D-9's blank trap was avoided exactly as the prompt asked**: the blank stays outside the shared
shape predicate, both call sites pass `allow_blank=True`, and F4/F5 assert `"?"` on both paths.

## 9. Test table — F1 to F5, with class B failures quoted

| Fixture | Host | Before | After |
|---|---|---|---|
| F1 two multi-code-point tokens + one blank, end to end | `test_atomic_token_persistence.py::test_f1_…` | FAIL | PASS |
| F2 the `L·L` canary, unmodified file | `test_atomic_tile_tokens.py:243` | PASS | PASS |
| F3 unknown `state_schema_version` refused | `useGameStore.test.ts` | FAIL (4 of 4 red) | PASS |
| F4 the placement predicate | `test_atomic_token_persistence.py::test_f4_…` | FAIL | PASS |
| F5 the exchange predicate | `test_atomic_token_persistence.py::test_f5_…` | FAIL | PASS |

**F2 before and after, identical, and the file is provably untouched**
(`git status --porcelain=v1 -- backend/tests/test_atomic_tile_tokens.py` empty):

```text
tests/test_atomic_tile_tokens.py .                                       [100%]
============================== 1 passed in 0.03s ===============================
```

**Class B for F1/F4/F5.** As committed, the fixtures fail at COLLECTION against unmodified
production code, which masks the causal failures:

```text
collected 0 items / 1 error
E   ImportError: cannot import name 'WIRE_STATE_SCHEMA_VERSION' from 'game.services'
```

⚠ **So the Worker ran a read-only probe** from `/tmp/opencode/mec-c1a3/` (deleted afterwards)
carrying exactly the F1/F4/F5 assertions against baseline production code:

```text
=== F1 pre-fix: the wire adapter RAISES on a multi-code-point token ===
ValueError: temporary wire adapter cannot represent a multi-code-point token; this adapter is
deleted when the wire format moves to state_schema_version 4

=== F1 pre-fix: no state_schema_version anywhere on the wire ===
hasattr(game.services, 'WIRE_STATE_SCHEMA_VERSION') -> False

=== F4 pre-fix: serializers.py:275 `nfc.isalpha()` rejects the L-interpunct-L canary ===
'L\u00b7L'.isalpha() -> False
  letter='SZ'   is_valid=False  'Must be a single uppercase letter.'
  letter='DZS'  is_valid=False  'Must be a single uppercase letter.'
  letter='L·L'  is_valid=False  'Must be a single uppercase letter.'
  letter='Á'    is_valid=True
  letter='1'    is_valid=False
  letter='·'    is_valid=False

=== F5 pre-fix: serializers.py:248 `CharField(max_length=1)` rejects SZ ===
  letters=['SZ','A']  is_valid=False  'Ensure this field has no more than 1 characters.'
  letters=['?']       is_valid=True   <== blank exchange is LIVE behaviour, not a new allowance
  letters=['A'*17]    is_valid=False  'Ensure this field has no more than 1 characters.'
```

⭐ `'L·L'.isalpha() -> False` is the measured `.isalpha()` failure, and it holds INDEPENDENTLY of
the length clause — which is why `.isalpha()` had to go rather than merely be relaxed. That is
defect C-5 made visible, exactly as the prompt demanded.

Post-fix verification over the exact F4 sets:

```text
ACCEPT 'SZ' 'DZS' 'L·L' 'Á' '?'             all accepted
REJECT '' 'a' 'S Z' '1' '·' 17-codepoints   all rejected
NFD 'Á' -> 'Á'                              still normalized; test_slovak_engine.py:200-203 unchanged
'?' with allow_blank=False                  rejected; blank_as still cannot be a blank
```

**Class B for F3, verbatim:**

```text
 ❯ src/hooks/useGameStore.test.ts (23 tests | 4 failed) 19ms
 FAIL … > introduces wire schema version 4
AssertionError: expected undefined to be 4          :294  expect(WIRE_STATE_SCHEMA_VERSION).toBe(4)
 FAIL … > REFUSES a newer, older, or absent version rather than mis-rendering it
AssertionError: expected { …(19) } to be null       :312  expect(…gameState).toBeNull()
 FAIL … > keeps an already-accepted state when a refused payload arrives
-   "state_schema_version": undefined,
+   "state_schema_version": 99,
 FAIL … > keeps selectedModelId in partialize and round-trips a stored id
AssertionError: expected 5 to be 6                  :275  expect(…version).toBe(6)
 Tests  4 failed | 19 passed (23)
```

F3 asserts the refusal — state stays `null`, an already-accepted state survives a refused payload,
`console.error` called once per refusal — not the absence of a crash. Its one pre-existing pass,
"accepts the supported version", is the positive control; the three refusal assertions are the teeth.

## 10. The re-pointed assertion lines, each with its restated invariant

```text
test_atomic_token_persistence.py:12,16   the two adapter imports
    -> WIRE_STATE_SCHEMA_VERSION replaces _WIRE_ADAPTER_REMOVAL;
       _legacy_wire_board_and_blanks dropped. Same intent: the module imports whatever
       names the wire contract.

test_p7  renamed test_p7_adapter_is_lossless… -> test_p7_wire_projection_is_lossless…
    comment: "Was `test_p7_adapter_is_lossless_for_english_blank_board`, which asserted the
    joined-string wire: 15 strings of 15 characters, plus a sidecar
    state["blanks"] == [{"row": 7, "col": 7}]. SAME INVARIANT, new mechanism: an English blank
    board crosses the wire losslessly. The realized letter and the blank identity now live in
    ONE cell instead of a string plus a coordinate list."
    :251 state["blanks"] == [...]  became  assert "blanks" not in state

test_p8  renamed test_p8_adapter_raises… -> test_p8_wire_projection_carries_a_multicodepoint_token
    comment: "Was `test_p8_adapter_raises_on_multicodepoint_token`, which asserted that
    `_build_state` RAISED `_WIRE_ADAPTER_REMOVAL` and that a direct
    `_legacy_wire_board_and_blanks` call mentioned "state_schema_version 4". SAME INVARIANT,
    new mechanism: a multi-code-point token is never silently mangled on the wire. The temporary
    adapter had to raise because a 15-character row cannot represent `SZ`; the structured
    projection carries it, so the loud failure becomes a correct payload."

test_api.py:1078  "Was data["state"]["board"][7][7:9] == "AT" — a slice of a joined
    fifteen-character row. SAME INVARIANT, new mechanism: the two tiles the human just played
    are on the wire at (7,7) and (7,8), now as atomic cells that a multi-code-point token
    also fits."
test_api.py:1324  same shape, for the AI's "JOE" at (7,7)-(7,9).

test_slovak_engine.py:205   D-10, shape-valid / engine-rejected
    comment: "Was `assert not PlacementSerializer(letter="CH").is_valid()`, and it was passing
    for the WRONG REASON. "CH" is structurally identical to "SZ" on every dimension a serializer
    can see — NFC-stable, uppercase-stable, two code points — so no shape predicate that accepts
    SZ can reject CH. PlacementSerializer has NO VARIANT IN SCOPE and cannot know whether CH is
    a tile in the game being played. SAME INVARIANT, split where it belongs: shape is the
    serializer's job, playability is the engine's. Both halves are asserted here, and the engine
    half is also pinned in tests/test_atomic_tile_tokens.py:237."
    Now asserts: is_valid() True, validated_data["letter"] == "CH", AND
    "CH" not in load_variant("slovak").playable_letters

test_slovak_engine.py:207   "`1` is still rejected, now for a better reason than a length limit:
    a tile token must contain at least one Unicode letter, and a digit has none."
```

No test file was deleted. Two tests were renamed inside their own file, each carrying its former
name in its own comment so a rename is distinguishable from a loss; the `p7`/`p8` identity prefixes
are unchanged.

## 11. Proofs P-A and P-B

**P-A.** `prompts.test.ts` not on the allowlist and unmodified; `prompts.ts` not in the commit.

```ts
  it("exports MOVE_PROMPT_VERSION and pins the CORE snapshot hash", () => {
    expect(MOVE_PROMPT_VERSION).toBe("pfr-s2-core-1");
    expect(createHash("sha256").update(MOVE_SYSTEM_PROMPT).digest("hex")).toBe(CORE_SHA256);
  });
```

with `CORE_SHA256 = "c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60"`, and:

```text
 ✓ src/lib/prompts.test.ts > MOVE_SYSTEM_PROMPT > exports MOVE_PROMPT_VERSION and pins the CORE snapshot hash 0ms
 Test Files  1 passed (1)   Tests  29 passed (29)
```

`GRID_ROW` at `prompts.ts:190` and `UNICODE_TILE` at `rack.ts:1` untouched — real defects, C1b's.

**P-B.**

```text
validate_lexicons: 13 asset(s) audited, 0 failed          exit 0
ls backend/assets/variants/ | wc -l                       12
git status --porcelain=v1 -- backend/assets/               (empty)
tests/test_czech_polish_variants.py   14 passed in 15.39s  (unmodified, off the allowlist)
tests/test_slovak_variant.py + test_variant_invariants.py + test_slovak_engine.py   all pass
```

`state_schema_version` is a game-state payload field only; no variant row, manifest or catalog
surface carries it.

## 12. The eight standing gates

```text
1 mypy       Success: no issues found in 85 source files          exit 0
2 ruff       All checks passed!                                   exit 0
3 check      System check identified no issues (0 silenced).       exit 0
4 pytest     745 passed, 4 skipped in 273.33s     --collect-only  749 tests collected
5 lexicons   validate_lexicons: 13 asset(s) audited, 0 failed     exit 0
6 typecheck  exit 0
7 vitest     Test Files 31 passed | 1 skipped (32) · Tests 454 passed | 3 skipped (457)
8 lint       exit 0        build   exit 0 — ELEVEN dynamic routes, ZERO static
```

Delta accounted for:

```text
pytest   742 -> 745 (+3): test_f1_…, test_f4_…, test_f5_…   4 skipped unchanged
         re-pointed with no count change: test_p7 (renamed), test_p8 (renamed),
         test_api.py:1078, :1324, test_slovak_engine.py:205, :207
collect  746 -> 749 (+3, the same three)
vitest   450 -> 454 (+4): the four in the new "F3 setGameState refuses an unknown
         state_schema_version" describe.  3 skipped unchanged.
         re-pointed with no count change: four persist-version pins 5 -> 6
mypy     85 files, unchanged, full documented scope
build    eleven dynamic, zero static, unchanged
```

Two separate frontend claims: **the code type-checks** (`npm run typecheck`, `tsc --noEmit
--incremental false`, exit 0) and **the build passed** (`npm run build` exit 0, TypeScript re-run
clean inside the build, eleven dynamic routes, zero static). No second `-q`; ports checked free
before the build; nothing pkilled; RF-16 route used as declared with no `-m` on `manage.py check`.

## 13. Git sequence

```text
git add <eleven paths, named individually>       (no -A, no .)
git status --porcelain=v1                        11 lines, all "M ", all inside the allowlist
git status --porcelain=v1 -- backend/assets/     (empty)
git diff --cached --stat                         11 files changed, 483 insertions(+), 99 deletions(-)
git commit                                       [main 529e691]
PRE-PUSH  git ls-remote origin refs/heads/main   8a50ded8…   EQUALS BASELINE
git push origin main                             8a50ded..529e691  main -> main   non-force, ff
READBACK  git ls-remote origin refs/heads/main   529e6910…  == git rev-parse HEAD
```

No force, amend, rebase, reset, clean, stash, branch or tag. One commit, one push. Network limited
to `git ls-remote` and one `git push`. No secret read or printed.

## 14. Deviations, risks, missing evidence

**Deviations — seven, all named, none silent**

```text
1  useGameStore.test.ts's four persist-version pins re-pointed 5 -> 6. Not in the fourteen. D-4
   mandates the bump; the file is allowlisted and is F3's host; the assertion stays an exact
   equality on the current declared version, so nothing is weakened. A consistent execution
   exists — unlike 04/01's CH/SZ — so the Worker proceeded rather than blocking, and flagged it.
2  test_atomic_token_persistence.py:267 re-pointed. `assert "state_schema_version 4" in
   str(raised_direct.exception)` sits inside the same assertRaises block as :264/:266 and cannot
   survive the adapter's removal. The section-6 grep could not see it: the string is
   `state_schema_version 4`, not one of the five patterns.
3  Two test renames, each carrying its former name in its own comment. Keeping "adapter raises"
   as a name after deleting the adapter would be a fresh documentation defect.
4  normalizeTileToken adds a second .normalize("NFC") after .toUpperCase() in route.ts. Without
   it the new predicate would accept an upper-but-decomposed token that the backend then rejects
   with 400 — a failure mode the old ^\p{L}$ could not produce, because a decomposed Á is two
   code points. variant_store.canonicalize_tile_token documents the same reason.
5  G3/G4's zod bounds became .min(1).max(MAX_TILE_TOKEN_CODEPOINTS) rather than being dropped.
   A bound was mandated only for G1/G2; leaving the model's tool schema unbounded is strictly
   worse than mirroring the backend, and the constant is named.
6  G8's replacement accepts "?" explicitly. letter.length === 1 accepted a rack blank, so
   dropping it silently would have removed blanks from exchange_letters — live behaviour.
7  Prompt-internal labels (D-1, D-2, D-7, D-9, G2) were removed from committed comments after
   first being written in. They reference a document that is not in the repository. F1/F4/F5
   labels are retained because they name tests inside this slice.
```

**Risks**

```text
· The refusal in setGameState is a hard fail-closed: a backend serving a wire version this client
  does not know leaves the board blank with a console.error and no user-visible message. That is
  the decided posture (loud, not silent), but a version-skew deploy shows an empty board rather
  than an explanation. Rollback needs no data migration; board_state is untouched.
· state_schema_version is 4 on both sides simultaneously, so frontend and backend of this commit
  must deploy TOGETHER. No negotiation, no dual-accept window.
· AIThinkingOverlay.tsx:72 still splits a candidate word per character, so a digraph word renders
  one tile too many. Off-allowlist — see MEASURED 2.
```

**Missing evidence, named**

```text
· No end-to-end HTTP round trip of a digraph placement. F4/F5 prove the serializer, F1 the wire
  projection, test_api.py:1078/:1324 the composite HTTP path for single-code-point tokens. One
  test doing all three needs an installed variant with a digraph tile, and no shipped variant has
  one — which is exactly why twelve could ship before this change. Hungarian is the first.
· No browser or running-product evidence. Board.tsx and page.tsx are verified by typecheck, lint,
  build and the existing suite only; no test renders the board from a BoardCell[][] payload, and
  there is no board-component test in the repository to extend.
· No exercise of the changed route.ts paths against a live provider. ai-turn-simulation.test.ts
  (off-allowlist, unmodified) drives the real POST handler with mocked generation and passes; it
  uses single-code-point tokens throughout.
```

`Resolved Execution Issues / Near-Misses:`

```text
1  The ExchangeSerializer comment first spelled the historical bound as the literal max_length=1,
   which made CMD2 return two comment hits and would have polluted the re-runnable proof for the
   next exchange. Reworded to "a child max_length of ONE"; CMD2 now returns zero.
2  F1/F4/F5 as committed fail at COLLECTION against unmodified code (ImportError), which masks the
   causal failures. Resolved by a read-only probe carrying the same assertions against baseline
   production code; both the collection error and the causal failures are quoted in section 9.
   Probe deleted; /tmp/opencode/mec-c1a3/ empty.
3  The `version < 6` migrate branch contains only a comment. ESLint's no-empty ignores
   comment-bearing blocks, confirmed by lint exit 0, so no filler statement was invented.
```

`Pre-Existing Failure Classification:` none. Every gate green at baseline and green at the commit;
no pre-existing failure inherited, masked or repaired.

---

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

1. ⛔ **A SEVENTH SPELLING the six commands cannot reach, and it is a real placement-path letter
   guard: `frontend/src/components/game/BlankPicker.tsx:8`.**
   ```ts
   const ENGLISH_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
   ```
   This is the UI that chooses what a blank represents. A hardcoded twenty-six-entry
   single-code-point English alphabet, so **a blank can never be assigned `SZ` from the product**
   no matter how correct the wire, the serializer and the engine are. The spelling is
   `"…".split("")` — no `len`, no `.length`, no `max_length`, no `\p{L}`, no `charAt`. Section 3.2
   does not name it, so it is neither in scope nor classified out of scope; it is invisible to the
   inventory. `GameState.alphabet` already exists on the wire, so the fix has a source of truth
   available. **This is the gap that has now cost three exchanges' worth of enumeration.**

2. **An EIGHTH spelling, same shape, display side: `AIThinkingOverlay.tsx:72`** —
   `const letters = word.toUpperCase().split("");`. A digraph word renders one tile per code point,
   so `SZA` shows three tiles for two tiles played. Also unreachable by all six commands.

3. **The section-6 enumeration was short by FIVE, all inside allowlisted files.**
   `useGameStore.test.ts:155,:167,:222,:249` pin `persist.getOptions().version).toBe(5)` and are
   forced red by D-4's mandated bump; `test_atomic_token_persistence.py:267` pins
   `"state_schema_version 4" in str(...)`. Same root cause as 03/01 and 04/01: an enumeration from
   a pattern narrower than the change. ⇒ **Cheap prophylactic for the next issue: before publishing
   a fixed assertion count, run the full gate suite against the DECIDED production change and let
   the red output produce the list.**

4. **The prompt attributed `:237` to the wrong file.** "the same file already asserts the
   playability half at `:237` … thirty lines below" — measured, `"CH" not in
   variant.playable_letters` is at `backend/tests/test_atomic_tile_tokens.py:237`, the canary's
   off-allowlist host, **not** `test_slovak_engine.py`, which is only 208 lines long. The
   substantive claim is true and D-10 stands; only the attribution is wrong. The committed comment
   points at the correct path. ⚠ **Had the fix depended on editing that line, D-10 would have been
   un-completable in the same way 04/01 was.**

5. `backend/gamecore/state.py:153,157` is a third independent "schema 4"-adjacent 15×15 validator
   (`len(grid) != 15`, and it explicitly rejects `isinstance(row, str)`). D-3 warned about the NAME
   collision; the measured fact is that the save-file validator also fails closed on a joined-string
   row, so it AGREES with the new wire rather than conflicting. No action needed.

6. `backend/game/services.py:216-218` — `if len(w) < 2` and `if not w.isalpha()` in
   `_word_passes_dictionary`. A WORD-level guard, not a tile-token guard, and `not w.isalpha()` will
   reject any word containing an interpunct or apostrophe — **`L·LA` cannot pass the dictionary
   today.** Same `.isalpha()` defect class D-7 clause (e) exists to fix, on the dictionary-authority
   axis. `backend/gamecore/lexicon_health.py:95` has the identical `not token.isalpha()`.

**LEAD**

1. `prompts.ts:250` (`trimmed.split("").join(" ")`) and `:254` (`rows.length !== 15`) are suspected
   additional C1b sites beyond `GRID_ROW` at `:190`, and fixing `GRID_ROW` alone would leave the
   model receiving per-code-point rack rendering. Call graph not verified.
2. Suspected that fixing `GRID_ROW` to accept a sixteen-character digraph row is not sufficient,
   because a labeled board row built from `BoardCell` tokens has no fixed character width at all —
   so the row format may need a SEPARATOR rather than a widened count. Row builder not read.
3. Suspected no test anywhere renders `Board.tsx`, which is why a `BoardCell[][]` regression on the
   visual path would be caught only by typecheck. One `find` would settle it; not run.

---

**Smallest next step:** commission the required fresh independent acceptance of
`529e6910ddf57dfbb4a9671bbab668b975067cf8` from a session that did not implement it, and give it the
two unclassified seventh/eighth spellings above (`BlankPicker.tsx:8`, `AIThinkingOverlay.tsx:72`) so
C1b's scope is complete before it is issued.

`Report justification:` new-mutation

`Logical-whole closure: not-closed`

My PASS is an implementation PASS and nothing more: it is non-independent, it self-certifies nothing,
and it closes nothing. This slice still requires fresh independent acceptance from a session that is
not a subagent of the Orchestrator and is not me. My authority expires with this terminal report.

**Context pressure:** moderate. Roughly half the window consumed, dominated by two full backend
suite runs and the diff reviews; no step was abbreviated for budget.
