# C1 design decision record — multi-code-point tiles end to end

Artifact class: **Orchestrator design decision record. Evidence and decisions, not authority.**
Owned by the Orchestrator of `13/00 multilingual-expansion-campaign`.
Measured 2026-09-03 at `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`. Read-only.

⛔ Every `file:line` below was measured in this session. **The campaign handout's C1 line numbers
and several of its scope claims are stale** — the corrections are named in section 5.

---

## 1. Why this record exists instead of a planner Worker

`12/00/91_orchestrator-handout.md` and `13/00/00_handout.md` both prescribe a **PLANNER WORKER
first, copy-paste delivery, "you stop at the file"** for C1. That was written before the
Cooperator's routing decision of 2026-09-03 (`00_notes.md` section 13), which reserves Workers
for genuinely large slices and calls out round-trips that produce no product value.

Reconciling the two honestly:

```text
WHAT A PLANNER WOULD ADD    repository reconnaissance, plus a second pair of eyes on the design
WHAT I ALREADY HAVE         the reconnaissance, done read-only in this session and recorded below
WHAT CANNOT BE DELEGATED    fresh independent ACCEPTANCE, from a session that did not implement
                            and that is NOT my subagent (AP.md:1395-1405). E3, non-negotiable,
                            untouched by any efficiency or autonomy grant.
```

⇒ **Decision D13-11.** The Orchestrator resolves the C1 design here, in writing, because AP
assigns objective, risk, routing and sequencing to the Orchestrator and the wire shape is an
architectural decision rather than a material product decision. One implementation Worker
follows. **The one thing handed to the Cooperator is the independent acceptance prompt** — which
is precisely the thing the planner route was protecting, and the only part of C1 that a subagent
cannot lawfully perform.

⚠ If any decision in section 4 turns out to be materially wrong during implementation, that is a
route-assumption change and the correct response is to stop and re-decide here, not to improvise
inside the implementation.

---

## 2. Measured surface — the seven guards, with real coordinates

```text
1  backend/game/services.py:321-324     _WIRE_ADAPTER_REMOVAL, a named constant whose text says
                                        "this adapter is deleted when the wire format moves to
                                        state_schema_version 4"
2  backend/game/services.py:327-364     _legacy_wire_board_and_blanks(): structured grid -> 15
                                        joined strings + blank coords. RAISES at :356 and :359
                                        rather than truncating. ONE call site: :442.
3  backend/game/serializers.py:269      _nfc_uppercase_letter(value, *, allow_blank)
4  backend/game/serializers.py:286-290  PlacementSerializer.validate_letter / validate_blank_as
5  frontend/src/app/api/ai/move/route.ts:123   Zod .length(1)
6  frontend/src/app/api/ai/move/route.ts:127   Zod .length(1)
7  frontend/src/app/api/ai/move/route.ts:341   blankAs.length === 1
   frontend/src/app/api/ai/move/route.ts:1002  letter.length === 1
```

⚠ **That is SEVEN items but EIGHT checks** — the handout's items 5-7 cover four distinct code
sites. Any "all seven removed" claim must enumerate all eight.

Test coverage that pins the current behaviour and must be re-pointed rather than deleted:

```text
backend/tests/test_atomic_token_persistence.py:12,16,264,266   imports the constant AND the
    adapter by name, and asserts the raised message equals _WIRE_ADAPTER_REMOVAL and contains
    "state_schema_version 4".
```

## 3. Measured surface — what is ALREADY token-safe

This is the half the handout understates, and it shrinks C1 substantially.

```text
PERSISTENCE   backend/game/models.py:31  board_state = JSONField holding list[list[dict]] with
              cells shaped {"token": str, "blank_as": str|None}. Already structured, already
              token-safe. F1/F2b landed this.
THE RACK      backend/game/services.py:459  "my_rack": list(my_slot.rack)
              frontend/src/lib/types.ts:65  my_rack: string[]
              ⇒ ALREADY LOSSLESS. A multi-code-point token in a rack crosses the wire untouched.
RENDERING     frontend/src/components/board/Board.tsx, game/Tile.tsx, game/TileRack.tsx contain
              NO single-character assumption. Every `.length === 1` and `[0]` in Board.tsx is
              touch-event handling (:421-:503), not letters. MEASURED by grep of all three.
AUTHORITY     backend/gamecore/legality.py:104,112  evaluate_scoring_move already accepts
              `authority: WordAuthority | None = None`. The parameter EXISTS; the work is to
              PASS one at the call sites, not to add plumbing.
```

⇒ **`board` is the only lossy field on the wire.** Everything else already carries tokens.

## 4. The decisions

### D-1 · The wire cell shape

`board: string[]` becomes a structured grid. Chosen shape:

```text
board: BoardCell[][]        15 rows x 15 cells
BoardCell = { token: string; blank_as: string | null } | null
```

```text
WHY THIS AND NOT A FLAT LIST OF PLACED CELLS: the frontend indexes by coordinate today —
    frontend/src/app/game/[id]/page.tsx:1212 does gameState?.board?.[row]?.[col] — and a grid
    keeps that access pattern working with a one-line change from a char to a field read. A
    sparse list would force every consumer to build an index first.
WHY `null` FOR AN EMPTY CELL AND NOT `{token: ""}`: the persisted representation already uses a
    non-dict for empty (services.py:341-344 treats any non-dict cell as empty), so `null` is the
    honest wire spelling of what storage already means. An empty-string token would create two
    ways to say "empty" and a test would eventually assert the wrong one.
```

### D-2 · `blanks` is REMOVED from the wire, not kept alongside

```text
Today   blanks: {row,col}[]  is a SECOND source of truth for the same fact, derived at
        services.py:361 by testing `token == "?"`.
After   the cell carries `token` and `blank_as`, so blankness is intrinsic. Keeping the
        coordinate list would leave two representations that can disagree.
⛔ CONSUMER TO UPDATE: frontend/src/components/board/Board.tsx:120-121 builds a Set of
   "row-col" keys from gameState.blanks and reads it at :615 via `blanks.has(key)`. That becomes
   a direct cell test.
```

### D-3 · A wire schema version IS introduced, and it is a NEW field

⛔ **MEASURED: `state_schema_version` does not exist anywhere in the code.** It appears only
inside the adapter's comment text at `services.py:323` and `:332`, and in the test at
`test_atomic_token_persistence.py:267`. There is no version field on the wire, on the model, or
in the payload's ~25 keys.

```text
⇒ "moving to state_schema_version 4" means INTRODUCING the field, not incrementing one.
DECISION: add `state_schema_version: 4` to the game-state payload, and have the frontend REFUSE
    a payload whose version it does not understand rather than mis-render one.
WHY 4 AND NOT 1: the value is fixed by the existing constant text and by the test that asserts
    it. Renumbering would make the adapter's own farewell message wrong and would silently
    invalidate an assertion that already ships. The number is inherited, not chosen.
```

### D-4 · The client store bumps to version 6, not 4

⛔ **MEASURED: the persisted store is ALREADY at version 5.** `frontend/src/hooks/useGameStore.ts`
`name: "libretiles-store"`, `version: 5`, with a migrate chain covering `< 1` through `< 5` at
`:273-296`.

```text
⇒ The handout's "localStorage v4" is STALE. C1 bumps 5 -> 6 and appends a `version < 6` branch.
WHAT THE MIGRATION MUST DO: nothing to the board. The store persists PREFERENCES (token, locale,
    selectedVariantSlug, aiTimeout, aiMaxSteps…), not game state — measured from its own shape.
    So the v6 branch exists to invalidate any cached field the new wire makes meaningless, and if
    there is none it must say so rather than be omitted, because a silent gap in a migrate chain
    is how a stale preference survives a schema change.
```

### D-5 · `_word_passes_dictionary` deletion is a SEPARATE, ORDERED step

```text
CALL SITES MEASURED   backend/game/services.py:131 (inside a closure) and :209 (the definition)
                      backend/game/diagnostics.py:136 and :352
TEST REFERENCES       backend/tests/test_ai_play_engine_diagnostic.py:25,299
                      backend/tests/test_czech_polish_variants.py:16
AUTHORITY CALL SITES  evaluate_scoring_move is called at services.py:862, services.py:1649,
                      diagnostics.py:476, move_search.py:373 and move_search.py:585 — FIVE
                      places, all of which must pass a WordAuthority once the predicate is gone.
```

⛔ **This is not the same change as the wire format** and must not be bundled into one commit
with it. They fail for different reasons, and the wire change is what the seven guards are about.
Order: wire first, authority second, both inside the same slice but as separate commits, so a
revert can take one without the other.

### D-6 · What C1 must NOT touch

```text
⛔ NO change to the PERSISTED board_state shape. It is already correct; only its projection onto
   the wire changes. A migration of stored rows is NOT part of C1 and would be a far higher tier.
⛔ NO change to any lexicon, manifest, build script or variant asset. Twelve languages ship and
   standing condition 1 requires their behaviour byte-unchanged.
⛔ NO change to prompts.ts. The MOVE CORE SHA-256
   c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60 and version pfr-s2-core-1
   must be PROVED unchanged.
⛔ NO provider surface. LOCK 11 holds.
```

## 5. ⛔ Where the handouts are stale about C1

```text
S1  "localStorage v4"            the store is already at version 5. C1 goes to 6.
S2  "state_schema_version 4"     the field does not exist; C1 introduces it. Nothing is bumped.
S3  "board/rack/blank/draw
     rendering"                  the RACK is already lossless on the wire, and the three
                                 rendering components carry no single-char assumption. Only
                                 `board` and the `blanks` list change.
S4  "seven guards"               seven items, EIGHT code sites. route.ts contributes four.
S5  "evaluate_scoring_move
     re-pointed at WordAuthority" the parameter already exists at legality.py:112. The work is to
                                 pass one at FIVE call sites, not to add the seam.
S6  planner Worker first         superseded by decision D13-11 above, for a named reason.
```

⚠ Five of six are the same defect class as `-m manage.py check` and the stale
`variant_store.py` line numbers: **a value carried forward in prose and never re-measured.** Rule
R-G exists for exactly this and it applies to my own successors reading THIS file too.

## 6. Inherited conditions this slice must satisfy

From `12/00/98_supersession.md`, carried forward and still open:

```text
 8  all seven F2b guards removed TOGETHER with the wire schema change; _word_passes_dictionary
    deleted and evaluate_scoring_move re-pointed
 9  the fixture passes with at least TWO DIFFERENT multi-character tokens, not only SZ
10  the L·L SYNTHETIC CANARY still passes — proving the implementation did not generalize only
    to `len(token) <= 2 && isalpha()`
14  FRESH INDEPENDENT ACCEPTANCE by a session that did not implement it, and that session
    CANNOT be my subagent
```

⚠ Condition 9 is now cheap to satisfy honestly: **twelve shipped languages give real
multi-code-point candidates only if a digraph variant exists, and none does yet.** So the fixture
must use SYNTHETIC tokens — `SZ` plus one of `DZS` or `LJ` — and the L·L canary. Hungarian is the
first real consumer and it lands AFTER C1, not with it.

## 7. Sequencing

```text
STEP 1  implementation Worker, subagent, bounded, NON-INDEPENDENT
          commit A  wire: BoardCell[][], state_schema_version 4 introduced, blanks removed,
                    adapter and its constant deleted, four route.ts guards and the two
                    serializer guards removed, store 5 -> 6, frontend consumers updated
          commit B  authority: evaluate_scoring_move given a WordAuthority at all five call
                    sites, _word_passes_dictionary deleted, its three test references re-pointed
          fixtures  two different multi-character tokens + the L·L canary
          gates     all eight, plus the MOVE CORE hash proof, plus twelve variants still playable
STEP 2  ⛔ FRESH INDEPENDENT ACCEPTANCE — copy-paste, delivered by the Cooperator to a session
          that is NOT my subagent. This is the only part of C1 I cannot execute or delegate.
STEP 3  B1 Hungarian, then B4 Croatian/Spanish, then B6 Greek/Bulgarian/Russian — six languages
          unlocked by this one slice.
```

**This document grants no mutation authority.**
