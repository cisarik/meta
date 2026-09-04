### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 04, Worker exchange ordinal 01

**Status: BLOCKED** — zero mutation. A fifth prompt defect (C-7 below) makes the authorized work un-completable inside the TEN-path allowlist. Stopping condition hit: *"completing the work would require a path outside the TEN-path allowlist"*, and §8's *"If you find a genuine contradiction, stop and report it rather than choosing an interpretation."*

`Phase-qualified result: not-applicable`
`Result artifact or commit: not-applicable — no commit was created`
`Result evidence:` section 3 commands A/B/C/D reproduced verbatim and agreeing with the prompt to the digit; the eight standing gates re-measured green at the unmodified baseline; a read-only in-process probe proving that the §4 D-7 predicate flips two currently-passing assertions in `backend/tests/test_slovak_engine.py`, a file on no list in this prompt.

Start commit `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`
End commit `8a50ded8b743d0badf7cca7fc3178a11d4b54be1` (unchanged)

## Section 2 gate, verbatim

```text
git rev-parse HEAD                    8a50ded8b743d0badf7cca7fc3178a11d4b54be1   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (detached, correct)
git status -sb                        ## main...origin/main                       MATCH
git status --porcelain=v1             <empty>                                     MATCH
git ls-remote origin refs/heads/main  8a50ded8b743d0badf7cca7fc3178a11d4b54be1   MATCH
ss -tlnp | grep -E ':(3000|8000)'     <no output, grep exit 1>                    no listener
ls backend/assets/variants/ | wc -l   12                                          MATCH
```

End-of-task re-confirmation: porcelain empty, `backend/assets/` porcelain empty, `## main...origin/main`, HEAD and public ref both `8a50ded8`, twelve variant manifests, `.ap` never attached or updated.

## Changed files and purpose

**None.** No repository file was created, edited, staged, committed or pushed. The only artifact produced anywhere was one read-only probe script at `/tmp/opencode/mec-c1a2/probe_d7_collision.py`, inside the authorized temp path; it has been removed. Nothing was written under `/home/agile/meta/`.

## Section 3 commands — BEFORE and AFTER (proofs P-C and P-D)

Because there is zero mutation, **AFTER is byte-identical to BEFORE**, and I state plainly that this means **P-C and P-D are NOT satisfied**: the adapter is still present and all seven guard sites still stand. The value here is that the reissue's derivation is confirmed sound.

```text
# A — git grep -n "length(1)\|length === 1" -- frontend/src/app/api/ai/move/route.ts
:123  .length(1)
:127  .length(1)
:341  ...(blankAs && blankAs.length === 1 ? { blank_as: blankAs } : {}),
:1002 typeof letter === "string" && letter.length === 1,
      → FOUR, exactly as stated

# B — git grep -nE '\^\[?\\p\{L\}' -- frontend/src/app/api/ai/move/route.ts
:329  !/^[\p{L}?]$/u.test(letter)
:334  if (letter === "?" && (!blankAs || !/^\p{L}$/u.test(blankAs))) return null;
      → TWO, exactly as stated

# C — git grep -nE "len\(nfc\) == 1" -- backend/game/serializers.py
:275  if len(nfc) == 1 and nfc.isalpha() and nfc == nfc.upper():
      → ONE, exactly as stated

# D — git grep -nE "_WIRE_ADAPTER_REMOVAL|_legacy_wire_board_and_blanks|len\(token\) > 1|len\(realized\) > 1" -- backend/game/services.py
:321 :327 :355 :356 :358 :359 :442
      → SEVEN, exactly as stated
```

Section 6's grep also reproduced **exactly** the eleven lines the prompt names, at the same line numbers. **C-1's correction is sound and the derivation method works** — and it is precisely by extending that method past the prompt's own file scoping that I found C-7 and C-8 below.

## ⛔ C-7 — THE BLOCKER: D-7 + F4 cannot be satisfied inside the allowlist

`backend/tests/test_slovak_engine.py:187-207` contains `test_placement_serializer_accepts_slovak_acute_a`, which currently passes:

```text
:205  assert not PlacementSerializer(data={"row": 7, "col": 7, "letter": "CH"}).is_valid()
:206  assert not PlacementSerializer(data={"row": 7, "col": 7, "letter": ""}).is_valid()
:207  assert not PlacementSerializer(data={"row": 7, "col": 7, "letter": "1"}).is_valid()
```

```text
$ .venv/bin/python -m pytest tests/test_slovak_engine.py::test_placement_serializer_accepts_slovak_acute_a
1 passed in 0.14s
```

That file is **not** among the ten allowlisted paths and is not named in `Existing focused tests`. `"CH"` is structurally indistinguishable from `"SZ"` — two ASCII uppercase letters, NFC, no whitespace, no controls, two code points — so **any** predicate satisfying F4 ("PlacementSerializer must ACCEPT `SZ`, `DZS` and `L·L`") necessarily makes `:205` fail. This is not an implementation-choice hazard; it is arithmetic.

MEASURED, not inferred. In-process probe (monkeypatched `game.serializers._nfc_uppercase_letter` with the exact D-7/D-8 predicate; no repository file touched):

```text
--- BASELINE predicate (len(nfc) == 1 and isalpha and upper) ---
  'CH' False · '' False · '1' False · 'SZ' False · 'DZS' False · 'L·L' False
  'A' True · 'Á' True · 'a' False · 'S Z' False · 17-char False
--- D-7/D-8 predicate ---
  'CH' True  <== FLIPPED
  '1'  True  <== FLIPPED
  'SZ' True  <== FLIPPED
  'DZS' True <== FLIPPED
  'L·L' True <== FLIPPED
  '' False · 'a' False · 'S Z' False · 17-char False
--- test_slovak_engine.py:205-207 re-evaluated ---
  :205 letter='CH' -> FAILS
  :206 letter=''   -> HOLDS
  :207 letter='1'  -> FAILS
```

Every route out is closed by this prompt:

| Route | Verdict |
|---|---|
| re-point `test_slovak_engine.py:205` / `:207` | forbidden — outside the ten-path allowlist |
| implement D-7 so `"CH"` stays invalid | impossible — F4 requires `"SZ"`; the serializer has no variant in scope |
| skip D-7/D-8/F4 | forbidden — no commit before F4 is satisfied; stop on F4 not having teeth |

`:207` is a **second, separable defect**: the D-7 vocabulary as written **accepts the digit `"1"` as a tile letter**. `gamecore/variant_store.py:243 _parse_asset_token` accepts `"1"` too, so mirroring its reasoning faithfully reproduces this. Adding one clause — *contains at least one Unicode letter* — keeps every required token and restores `:207`, measured:

```text
with an added 'contains at least one Unicode letter' clause:
  'CH' True · '1' False · 'SZ' True · 'DZS' True · 'L·L' True · 'Á' True · '·' False
```

I did **not** adopt that clause: §4 says *"Implement them; do not re-decide them."* It is offered as a decision for you, not taken as one. `:205` has no such escape and is the hard blocker.

## Items the report contract requires that a blocked exchange cannot produce

- **New wire payload shape** — not produced. `services.py:449-450` still emits `"board": wire_board, "blanks": wire_blanks`; `state_schema_version` exists nowhere but the adapter's comment text and one test assertion, confirming D-3.
- **Board-consumer diffs** — none. All nine consumer sites stand unmodified.
- **Store migrate branch** — none. `useGameStore.ts:272` remains `version: 5`, chain ends at `version < 5`.
- **New serializer predicate and bound** — designed, probed, not committed. The bound would be `MAX_TILE_TOKEN_CODEPOINTS = 16` at `gamecore/variant_store.py:22`, consumed at `:269`.
- **F1, F3 authoring** — not written. The blocker surfaced during pre-mutation verification, so I stopped before authoring fixtures rather than mutating and reverting.

## Test table

| Fixture | Required | Measured |
|---|---|---|
| F1 two multi-code-point tokens through the wire | fail before, pass after | **not authored** — blocked pre-mutation |
| F2 the `L·L` canary, unmodified | pass before **and** after | **PASS before**: `test_interpunct_token_loads_places_scores_and_validates` → `1 passed in 0.04s`. File never edited. |
| F3 client refuses an unknown `state_schema_version` | fail before, pass after | **not authored**. Confirmed nothing to disagree with: `grep -rn "state_schema" frontend/src frontend/tests` is empty. |
| F4 serializer accepts SZ/DZS/L·L, rejects empty, lowercase, whitespace, 17 code points | fail before, pass after | **not authored as a test**; class-B failure **measured** by probe. |

Defect C-5 made visible, quoted:

```text
  letter='L·L'  is_valid=False        (BASELINE predicate)
$ .venv/bin/python -c "print('L·L'.isalpha(), 'SZ'.isalpha(), 'DZS'.isalpha(), len('L·L'))"
False True True 3
```

C-5 confirmed: dropping only the length test would accept the digraphs and still reject the interpunct canary. Both clauses must go, exactly as D-7 says.

## P-A — MOVE CORE unchanged

```text
$ npx vitest run src/lib/prompts.test.ts --reporter=verbose
 ✓ MOVE_SYSTEM_PROMPT > exports MOVE_PROMPT_VERSION and pins the CORE snapshot hash 1ms
 Test Files  1 passed (1) · Tests  29 passed (29)
```

`prompts.test.ts:79-84` asserts `pfr-s2-core-1` and `sha256(MOVE_SYSTEM_PROMPT) === c7acc270…`. `prompts.ts` never opened for writing.

## P-B — twelve variants still playable

```text
validate_lexicons: 13 asset(s) audited, 0 failed          (exit 0)
tests/test_czech_polish_variants.py                        14 passed in 15.57s
ls backend/assets/variants/ | wc -l                        12
git status --porcelain=v1 -- backend/assets/               <empty>
```

## All eight standing gates — re-measured at the unmodified baseline

Baseline attestation, not validation of a change. Every value reproduces the prompt's table to the digit, independently of the previous Worker.

```text
1  mypy                    Success: no issues found in 85 source files
2  ruff check .            All checks passed!
3  manage.py check         System check identified no issues (0 silenced).
4  pytest                  742 passed, 4 skipped in 295.12s
   --collect-only          746 tests collected in 6.78s        delta +0
5  validate_lexicons       13 asset(s) audited, 0 failed       exit 0
6  npm run typecheck       exit 0
7  npx vitest run          Test Files 31 passed | 1 skipped (32) · Tests 450 passed | 3 skipped (453)
8  npm run lint            exit 0
   npm run build           exit 0, ELEVEN ƒ routes, ZERO static
```

Four traps: no second `-q`; mypy full scope; `ss -tlnp` re-checked immediately before build, nothing running, nothing killed; and the two frontend claims stated separately — **the code type-checks** and **the build passed**. RF-16 route used as declared, no `-m` on `manage.py check`, no fallback to ambient `python3` or `poetry run`.

## Git sequence

Nothing staged, committed or pushed. `git add` never invoked. Pre-push gate never reached; public ref still `8a50ded8`, equal to HEAD. No force, amend, rebase, reset, clean, stash, branch or tag. No `.ap` change. No file deleted.

## Deviations, risks, missing evidence

- **Deviation:** none from the authorized route. No implementation was attempted, which is the stopping condition rather than a choice.
- **Risk left standing:** the C1a wire defect is unfixed. `services.py:355-359` still raises on any token longer than one code point, so no digraph language can be played. Hungarian remains blocked behind this exchange.
- **Missing evidence:** F1's and F3's class-B failure text does not exist. F4's class-B evidence exists only as a probe. No "after" measurement exists for anything.
- **Not verified:** whether the twelve shipped variants tolerate the new payload at runtime — no runtime exercised, no listener started.

`Resolved Execution Issues / Near-Misses:`

- **Near-miss avoided.** My first instinct on `:207` was to add the "contains at least one letter" clause and proceed — which would have kept `:207` green, left `:205` red, and produced a report claiming partial success on a task that cannot be completed. "Do not re-decide them" plus "stop and report rather than choosing an interpretation" caught it. I measured the alternative and handed you the measurement instead of the decision.
- **Near-miss avoided.** Section 6's grep returns eleven lines and I nearly trusted that as complete. It is short by one — see MEASURED-1.
- **Resolved:** `diagnostics.py:308` matches `item.get("board")` but parses a *fixture* list of `{row,col,letter}` objects, unrelated to the wire payload.
- **Resolved:** `serializers.py:58` `"board"` is a forbidden-AI-metadata key name, not a wire field.
- **Confirmed clean:** `git grep -n "board\|blanks" -- backend/game/consumers.py` is empty. Multiplayer really would come along for free.
- **Confirmed clean:** `_build_state` (`services.py:429`) is the single producer; `get_game_state_for_user` (`:1125-1127`) its only caller, reached from `views.py` ×8 and `consumers.py` ×2. No second projection to keep in sync.
- **Confirmed clean:** no frontend file outside the allowlist consumes `GameState.board` or `.blanks`. `play/page.tsx` and `waiting/[id]/page.tsx` contain zero `board`/`blanks` references, so the store-level refusal covers both without editing them.

`Pre-Existing Failure Classification:` **none.** All eight gates green at `8a50ded8`, including `test_slovak_engine.py`. C-7 is a *prospective* regression introduced by the authorized design, not a pre-existing failure — which is why it blocks rather than being waivable.

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED**

1. **`test_atomic_token_persistence.py:251` — the re-pointing list is short by one.** `assert state["blanks"] == [{"row": 7, "col": 7}]`, inside the same test as five of the eleven. D-2 removes `blanks` from the payload, so this must be re-pointed too — **twelve, not eleven**. Section 6's grep cannot see it: the pattern searches `state\["board"\]` and the two adapter names, never `state\["blanks"\]`. Not a blocker (allowlisted file), but a Worker who trusts the count leaves a `KeyError`.

2. **`backend/game/serializers.py:248` — an EIGHTH single-code-point guard on a letter path, invisible to command C.** `ExchangeSerializer.letters` is `child=serializers.CharField(max_length=1)`. `views.py:304` and `views.py:475` show **both** `/api/game/{id}/exchange/` (human) and `/api/game/{id}/ai-exchange/` (AI) use it. So relaxing A:1002 moves the failure one hop downstream: the route would forward `SZ` and the backend would answer HTTP 400. **The exchange path stays closed to every digraph language after this slice ships.** Command C searched only for `len(nfc) == 1`; this guard is spelled `max_length=1`. C-1 recurring one file to the left, and it is in an already-allowlisted file.

3. **`frontend/src/lib/rack.ts:1` and `:23` — a single-code-point regex on the rack path.** `const UNICODE_TILE = /^[\p{L}?]$/u;` rejects `SZ` and `L·L` when `isPlausibleRack` is called without an alphabet. Mitigated: all call sites pass `gameState?.alphabet` and `services.py:163-169` always ships it, so the regex branch is reached only when `gameState` is null. Latent, off-allowlist, worth an explicit decision rather than a discovery.

4. **C1b is larger than `gamecore/state.py`, and its second locus is in the hash-frozen file.** `gamecore/state.py:44` `grid.append("".join(row_chars))` is the site you own. But `prompts.ts:190` declares `GRID_ROW = /^[\p{L}.]{15}$/u`, and `extractGridRows` (`:227-236`, called at `:314`) keeps only lines matching it. A digraph row is sixteen code points, so it is not misaligned — it is **silently dropped**, and `rows.slice(0, 15)` returns a short board. Two mitigating facts: the P-A hash covers only `MOVE_SYSTEM_PROMPT`, not the parser, so C1b can repair `extractGridRows` without moving the CORE hash; and `gamecore/state.py:63` / `:104-125` already carry a structured `grid: list[list[str | None]]` for the save file, so the token-preserving projection C1b needs already exists next to the lossy one.

5. **`route.ts` does not consume the wire board at all.** Only `compact_state` and prose. C1a and C1b touch disjoint code, and this slice cannot regress the AI's view.

6. **The whole wire-board surface really is confined to the allowlist**, `:251` aside.

**LEAD**

1. Once D-8 bounds `PlacementSerializer` at 16, `SubmitMoveSerializer` (`serializers.py:241-243`) still declares `placements` as a bare `ListField(child=DictField())` and never runs `PlacementSerializer` — the human move path. `services.py:183-196 _placements_from_data` normalises through `normalise_letter` with no length or shape bound at all. I did not probe whether an adversarial long token reaches scoring through `/api/game/{id}/move/`, so I do not claim it does; but the human path visibly does not share the guard D-8 is about to add to the AI path.
2. `_variant_snapshot_fields` ships `tile_points` as `dict(variant.tile_points)` and `alphabet` as a list of tokens, both already token-shaped. If a later slice keys tile points by rendered character anywhere in the UI, a digraph would miss its score. I did not trace the `TILE_POINTS` consumer in `components/tiles/TileRack.tsx:9`.

## One smallest next step

Reissue with **`backend/tests/test_slovak_engine.py` as an eleventh allowlisted path**, authorizing exactly two re-pointings with their invariant restated in a comment: `:205` becomes "shape-valid, engine-rejected" — `PlacementSerializer` accepts `CH` because a serializer has no variant in scope, while `CH` stays unplayable in Slovak at the engine layer, which the same file already asserts at `:237` (`"CH" not in variant.playable_letters`) — and `:207` resolved by whichever way you decide the digit question. In the same pass: correct ELEVEN to **TWELVE** to include `test_atomic_token_persistence.py:251`, and decide MEASURED-2 (`ExchangeSerializer` `max_length=1`) either into this slice or into a named successor, because leaving it silently makes C1a's own exchange path a no-op for digraph languages.

`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`

Report justification: `new-material-risk`

`Logical-whole closure: not-closed`

**Authority expiry.** My authority expires with this terminal report. No mutation was made and nothing is left half-applied; the tree is at the exact baseline and the public ref is unchanged. I will take no further autonomous action on this task, and this `BLOCKED` closes nothing — MEC-C1a still requires a corrected prompt, implementation, and the separate fresh independent acceptance that is not me.

**Context pressure:** low-to-moderate. Roughly a third of the window is in use.
