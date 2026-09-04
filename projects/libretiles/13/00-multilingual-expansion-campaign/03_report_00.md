### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion-campaign, Worker session ordinal 03, Worker exchange ordinal 01

**Status: BLOCKED — stopped before any mutation. Zero files changed, no commit, no push.**

`Phase-qualified result:` not-applicable
`Result artifact or commit:` not-applicable — tree remains at `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`
`Result evidence:` section 2 gate green; all of section 3 verified line by line; full nine-command validation ladder re-measured at baseline and identical to your figures; F2 canary observed passing pre-change; two stopping conditions triggered (details below)

Start commit `8a50ded8b743d0badf7cca7fc3178a11d4b54be1` · End commit `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`

---

## Why I stopped

Two of your own stopping conditions fired. The first is the material one.

### Blocker 1 — F3 cannot be authored inside the nine-path allowlist

F3 requires an executed client-side assertion ("Assert the refusal, not just the absence of a crash"), and stage gate 28 makes it a pre-commit condition ("no commit before the two-token fixture AND the L·L canary AND **the schema-refusal test** all pass").

`frontend/vitest.config.ts` declares no `test.include`, so vitest uses its default `**/*.{test,spec}.?(c|m)[jt]s?(x)`. **None of the nine allowlisted paths matches that glob.** There are 32 collected frontend test files; the natural host — `frontend/src/hooks/useGameStore.test.ts` — exists and is the file that already exercises `useGameStore.persist.getOptions().migrate`, but it is not on the allowlist.

`useGameStore.ts:151` `setGameState` is also the single ingress choke point for *every* game-state payload (REST at `game/[id]/page.tsx:538,911`, `waiting/[id]/page.tsx:40`; move/queue results at `:677,964` and `play/page.tsx:248`; websocket at `:1132` and `waiting/[id]/page.tsx:61`). Two of those ingress files are themselves off-allowlist, which *confirms* the store is the right refusal site — and makes the missing test path the only gap.

Section 11: "completing the work would require a path outside the nine-path allowlist." Section 8 cross-check: "If you find a genuine contradiction, stop and report it rather than choosing an interpretation." I did not write to a non-allowlisted path, and I did not skip F3 to get to a commit.

**Minimal fix: add `frontend/src/hooks/useGameStore.test.ts` as a tenth allowlisted path.** No other gap exists — I verified no off-allowlist frontend test constructs a `GameState` literal, so adding a required `state_schema_version` field and removing `blanks` breaks no other file's typecheck (`ai-fallback.test.ts` / `ai-turn-simulation.test.ts` use the narrow `ReconciliationView` at `ai-fallback.ts:35-41` and a local `board: string[]` harness type at `ai-turn-simulation.test.ts:67,377,463`, not `GameState`).

### Blocker 2 — a section 3.2 coordinate does not read as claimed

You claimed (section 3.2, line 108):

```text
frontend/src/components/board/Board.tsx, components/game/Tile.tsx, components/game/TileRack.tsx
```

Found:

```text
frontend/src/components/board/Board.tsx      ✓ exists, claim holds
frontend/src/components/game/Tile.tsx        ✗ does not exist
frontend/src/components/game/TileRack.tsx    ✗ does not exist
frontend/src/components/tiles/Tile.tsx       ← actual path
frontend/src/components/tiles/TileRack.tsx   ← actual path
```

`frontend/src/components/game/` does exist (it holds `AIThinkingOverlay.tsx`, `ScorePanel.tsx`, `GameControls.tsx`) but contains neither tile component. The **substantive** claim holds at the real paths: `grep -n "length|\[0\]|charAt|slice|substring"` over both files returns only `event.touches[0]` / `changedTouches[0]` and `visibleRack.length === 0`. Both are off-allowlist under either spelling, so this could not have caused a wrong edit — but it is literally a section 3 coordinate that does not read as described, and your delivery boundary said to report claim vs. finding and stop.

Also unnamed in 3.2: `frontend/src/components/board/Cell.tsx` is the actual per-cell renderer that receives `letter`, and it too has no single-code-point assumption (only `event.touches[0]` at `:53,59,68`).

---

## Section 2 gate — verbatim

```text
git rev-parse HEAD                    8a50ded8b743d0badf7cca7fc3178a11d4b54be1     ✓
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656     ✓
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656     ✓ (detached, equal)
git status -sb                        ## main...origin/main                        ✓
git status --porcelain=v1             <empty>                                      ✓
git ls-remote origin refs/heads/main  8a50ded8b743d0badf7cca7fc3178a11d4b54be1	refs/heads/main   ✓
ss -tlnp | grep -E ':(3000|8000)'     <no output, exit 1>                          ✓
ls backend/assets/variants/ | wc -l   12                                           ✓
```

End-of-task re-confirmation:

```text
git status --porcelain=v1                     <empty>
git status --porcelain=v1 -- backend/assets/  <empty>
git rev-parse HEAD                            8a50ded8b743d0badf7cca7fc3178a11d4b54be1
git status -sb                                ## main...origin/main
```

`.ap` was neither attached nor updated.

## Changed files and purpose

**None.** No file inside or outside the allowlist was created, modified, or deleted. No temporary file was created; `/tmp/opencode/mec-c1a/` was never needed. `npm run build` wrote `frontend/.next/`, which is gitignored (`.gitignore:51`, `frontend/.gitignore:17`) and leaves porcelain empty, as shown above.

## The eight guard sites — all verified as described; none changed

| # | Coordinate | Reads as claimed? | Current text | What it *would* become (not applied) |
|---|---|---|---|---|
| 1 | `services.py:321-324` | ✓ | `_WIRE_ADAPTER_REMOVAL = (...)` constant | deleted |
| 2 | `services.py:327-364` | ✓ raises at `:356` and `:359`; sole call site `:442` | `_legacy_wire_board_and_blanks()` | deleted; replaced by a structured-grid projection |
| 3 | `serializers.py:269-278` | ✓ `len(nfc) == 1` at `:275` | `if len(nfc) == 1 and nfc.isalpha() and nfc == nfc.upper():` | length test dropped; non-empty NFC-uppercase token |
| 4 | `serializers.py:286-290` | ✓ | `validate_letter` / `validate_blank_as` | unchanged call shape, relaxed predicate via site 3 |
| 5 | `route.ts:121-124` | ✓ | `letter: z.string().length(1)` | `z.string().min(1)` |
| 6 | `route.ts:125-129` | ✓ | `blank_as: z.string().length(1).optional()` | `z.string().min(1).optional()` |
| 7 | `route.ts:341` | ✓ | `...(blankAs && blankAs.length === 1 ? …)` | `...(blankAs ? …)` |
| 8 | `route.ts:1002` | ✓ | `typeof letter === "string" && letter.length === 1` | `typeof letter === "string" && letter.length > 0` — and yes, these are RACK tokens from `playability.exchange_letters`, a different path from the other seven |

**Your count of eight is short by two, and both are inside the allowlist.** In the same function as site 7:

```text
9   route.ts:329   !/^[\p{L}?]$/u.test(letter)      ← rejects any multi-code-point letter
10  route.ts:334   letter === "?" && (!blankAs || !/^\p{L}$/u.test(blankAs))
```

`^…$` with a single `\p{L}` matches exactly one code point. Removing site 7 while leaving `:329`/`:334` in place is a **no-op**: `normalizePlacementData` would still return `null` for `SZ`, so the AI could never place a digraph. Proof P-D as written ("NO SINGLE-CODE-POINT GUARD REMAINS ON A LETTER PATH… the eight coordinates") would have been a false absence claim. Please restate 3.1 as ten places across seven items.

## New wire payload shape

Not implemented, so I cannot quote it from committed code. Current code, unchanged:

```python
# backend/game/services.py:442,449-450
wire_board, wire_blanks = _legacy_wire_board_and_blanks(session.board_state)
...
"board": wire_board,
"blanks": wire_blanks,
```

`state_schema_version` still does not exist as a field anywhere. **D-3 confirmed MEASURED** — the only three occurrences in the repository are prose:

```text
backend/game/services.py:323                    "…moves to state_schema_version 4"
backend/game/services.py:332                    Deleted when the wire format moves to state_schema_version 4.
backend/tests/test_atomic_token_persistence.py:267   assert "state_schema_version 4" in str(…)
```

`4` is therefore inherited, not chosen, exactly as you stated. Design accepted unchanged (D-1 `BoardCell[][]`, `null` for empty, D-2 `blanks` removed, D-3 version 4 + loud refusal, D-4 store 5 → 6 with an explicit commented no-op branch).

## Frontend board consumers — exact diff

**Empty.** No diff exists. Baseline text of every consumer, re-verified:

```text
types.ts:48        board: string[];
types.ts:49        blanks: { row: number; col: number }[];
Board.tsx:119      const grid = gameState?.board ?? Array(BOARD_SIZE).fill(".".repeat(BOARD_SIZE));
Board.tsx:120-122  const blanks = new Set((gameState?.blanks ?? []).map((b) => `${b.row}-${b.col}`));
Board.tsx:556      const boardLetter = grid[row]?.[col];
Board.tsx:597      const boardLetter = grid[row]?.[col] ?? ".";
Board.tsx:615      isBlank={pending ? pending.letter === "?" : blanks.has(key)}
page.tsx:1212      const boardLetter = gameState?.board?.[row]?.[col];
page.tsx:1213      if (boardLetter && boardLetter !== ".") return null;
```

Those are the only two files that read `GameState.board` and the only one that reads `GameState.blanks`, repository-wide.

## Store migrate branch as committed

No branch was committed. Baseline, verified: `useGameStore.ts:271-272` `name: "libretiles-store"`, `version: 5`; chain `< 1` (`:275`), `< 2` (`:279`), `< 3` (`:284`), `< 4` (`:289`), `< 5` (`:294`). **D-4 confirmed MEASURED at 5**, so 5 → 6 is correct.

## Test table

| Fixture | Required | Observed |
|---|---|---|
| **F1** two distinct multi-char tokens end to end | fail before, pass after | **not authored** — blocked upstream of F1 by Blocker 1; no class B capture |
| **F2** L·L canary, unmodified | pass before **and** after | **PASS before.** `tests/test_atomic_tile_tokens.py::test_interpunct_token_loads_places_scores_and_validates` → `1 passed in 0.03s`. File untouched. Body verified at `:243-284` (`token = "L·L"`, `assert token.isalpha() is False`, `assert len(token) == 3`, `assert words[0].word == "L·LA"`, `assert legality.ok`) |
| **F3** unknown `state_schema_version` refused by client | fail before, pass after | **not authored** — Blocker 1; no class B capture |

**Class B failure text: none to quote.** I authored neither F1 nor F3, so nothing failed. I am not reporting an unrun capture as satisfied. F2's pre-change PASS is real and quoted; the stopping condition "F2 does not pass BEFORE the change" did **not** fire.

## Proof P-A — MOVE CORE hash

`frontend/src/lib/prompts.ts` untouched. `npx vitest run src/lib/prompts.test.ts` → `Test Files 1 passed (1) · Tests 29 passed (29)`, including:

```typescript
// frontend/src/lib/prompts.test.ts:22-23, 79-84
const CORE_SHA256 =
  "c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60";
...
it("exports MOVE_PROMPT_VERSION and pins the CORE snapshot hash", () => {
  expect(MOVE_PROMPT_VERSION).toBe("pfr-s2-core-1");
  expect(createHash("sha256").update(MOVE_SYSTEM_PROMPT).digest("hex")).toBe(
    CORE_SHA256,
  );
});
```

## Proof P-B — thirteen lexicon assets, twelve playable variants

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons
…
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
swedish dictionary ok reason=ok words=822919 duplicates=0 non_nfc=0
validate_lexicons: 13 asset(s) audited, 0 failed        exit 0
```

Twelve manifests present: `afrikaans czech danish dutch english german icelandic italian polish portuguese slovak swedish`.

The catalog contract is guarded by `backend/tests/test_czech_polish_variants.py`, which passed inside the 742. It asserts the exact ordered twelve-slug list (`:131-143`), `set(row.keys()) == _SUMMARY_KEYS` where `_SUMMARY_KEYS = frozenset({"slug","display_name","language_code","readiness"})` (`:18`, `:146`), and `row["readiness"] == "playable"` for every row (`:147`). That file is off-allowlist and needs no change — it is exactly the standing guard that would catch `state_schema_version` leaking into a variant row. I did not hit `GET /api/game/variants/` over HTTP: no server is running, and starting one is outside my authority.

## Proof P-C — adapter grep counts (baseline: adapter still present)

```text
git grep -n  "_legacy_wire_board_and_blanks"   → 4 matches
  backend/game/services.py:327  (def)
  backend/game/services.py:442  (sole call site)
  backend/tests/test_atomic_token_persistence.py:16   (import)
  backend/tests/test_atomic_token_persistence.py:266  (direct call)

git grep -in "_WIRE_ADAPTER_REMOVAL"           → 5 matches
  backend/game/services.py:321  (definition)
  backend/game/services.py:356  (raise)
  backend/game/services.py:359  (raise)
  backend/tests/test_atomic_token_persistence.py:12   (import)
  backend/tests/test_atomic_token_persistence.py:264  (equality assert)
```

Both cases run. Case-insensitive found no extra spelling. Post-change these must fall to what section 6 leaves behind; neither is 0 yet because nothing was changed.

## Proof P-D — per-site table

See the eight-site table above. Every one of the eight verified as described, **none changed**, plus two unenumerated sites 9 and 10.

## The eight standing gates — all green at baseline, re-measured

| Gate | Claimed | Measured | Exit |
|---|---|---|---|
| mypy `config game gamecore accounts catalog` | 85 files | `Success: no issues found in 85 source files` | 0 |
| ruff `check .` | pass | `All checks passed!` | 0 |
| `manage.py check` | 0 issues | `System check identified no issues (0 silenced).` | 0 |
| pytest | 742/4 | `742 passed, 4 skipped in 271.43s (0:04:31)` | 0 |
| `npm run typecheck` | exit 0 | exit 0 | 0 |
| `npx vitest run` | 450/3 | `Test Files 31 passed \| 1 skipped (32)` · `Tests 450 passed \| 3 skipped (453)` | 0 |
| `npm run lint` | exit 0 | exit 0 | 0 |
| `npm run build` | 11 dynamic / 0 static | `✓ Compiled successfully` · 11 `ƒ` routes, 0 `○` | 0 |

`pytest --collect-only` → `746 tests collected in 7.40s`. **Delta accounted for: zero.** No test was added, removed, or re-pointed, so 746/742/4 must and do match your figures exactly. mypy file count is 85, unchanged. The eleven dynamic routes are `/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`.

**Two separate frontend claims, stated separately as required:** (1) the code type-checks — `npm run typecheck` (`tsc --noEmit --incremental false`) exited 0; (2) the production build passed — `npm run build` exited 0 and emitted eleven dynamic routes and zero static routes. Trap 1 avoided: no second `-q` was passed, and the pytest summary line is present. Trap 3 satisfied: `ss -tlnp | grep -E ':(3000|8000)'` re-checked immediately before `npm run build` → `no listener on 3000/8000`. Nothing was killed.

RF-16 route binding used exactly as granted: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …` and `.venv/bin/ruff`. `.venv/bin/python` is present (symlink → `python3.12`). No `poetry run`, no ambient `python3`. `manage.py check` was invoked without `-m`.

## Git sequence

None performed, by design. Nothing staged, no commit created, pre-push gate never reached, no push, no readback. `git ls-remote origin refs/heads/main` still equals the exact baseline. No force, amend, rebase, reset, clean, stash, branch, or tag was run at any point.

## Deviations, risks, missing evidence

- **Deviation:** none from the granted route. The stop itself is the prescribed behaviour, not a deviation.
- **Risk retired by stopping:** shipping proof P-D as an eight-site absence claim while sites 9 and 10 silently keep rejecting every digraph placement. That would have produced a green eight-gate run, a passing F1 at the `_build_state` layer, and an AI that still cannot place `SZ` — a false PASS on a shipped multiplayer product.
- **Missing evidence, named:** (a) F1 and F3 pre-fix class B captures — unobtainable without the allowlist amendment; (b) live `GET /api/game/variants/` over HTTP — no server, no authority to start one; the Django-level guard test is quoted instead; (c) post-change values for every gate — nothing changed.
- **Not read:** `backend/.env`, `frontend/.env.local`. No secret was read or printed. No network call beyond the one authorized `git ls-remote`. No dependency, lockfile, or migration touched. No provider surface, prompt, asset, manifest, or lexicon touched. Nothing under `/home/agile/meta/` was read beyond the single delivery file, listed, searched, or written.

`Resolved Execution Issues / Near-Misses:`

1. **Near-miss — sites 9/10.** I nearly fixed `route.ts:329`/`:334` under the reasoning that they sit in site 7's own function, are inside the allowlist, and are required for P-D to be true. I did not, because your count of eight is a load-bearing premise of P-D's report contract and silently reporting ten under an eight-row heading would corrupt the acceptance record. Escalated instead.
2. **Near-miss — F3 host.** `frontend/src/hooks/useGameStore.test.ts` already exists and is the obvious host. Writing to it would have produced a complete, green, pushable slice. It is not on the allowlist, so I did not touch it. Omitted permission is not permission.
3. **Resolved — false alarm on `backend/gamecore/state.py:167`.** `for pos in state.get("blanks", [])` looked like a second `blanks` consumer. It is the **save-file** schema-4 shape (`grid` + `blanks`), unrelated to the wire payload, pinned by the forbidden `test_atomic_tile_tokens.py:531`. No conflict; nothing to change.
4. **Resolved — false alarm on `serializers.py:58` and `diagnostics.py:308`.** `"board"` at `serializers.py:58` is a `FORBIDDEN_AI_METADATA_KEYS` member. `diagnostics.py:308` reads a *fixture asset* board of `{row, col, letter}` objects (`_board_letters_from_payload`, `:264-286`), never the wire payload. Neither blocks the wire change.
5. **Resolved — `backend/tests/diagnostics/test_turn_probe.py:110` `session.blanks = []`** sets a dead Python attribute; the model field was dropped in migration `0008`. Harmless, off-allowlist, no action.

`Pre-Existing Failure Classification:` **No pre-existing failures.** All nine ladder commands exited 0 at the exact baseline and every count matches your measurement to the digit. The `[libretiles-provider-failure] openrouter … rate limit` and `No endpoints found for stealth/example:free` lines in the vitest output are deliberate stderr from passing negative-path fixtures, not failures — `450 passed | 3 skipped`, exit 0. The three vitest skips and one skipped file are the live-probe suites (`provider-capability.live`, `ai-play-diagnostic.live.worker`), gated off without `PROVIDER_PROBE_LIVE=1`. The 4 pytest skips are pre-existing and unchanged.

---

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
```

**MEASURED** — each of these I ran or read directly.

1. **`route.ts:329` and `route.ts:334` are guard sites 9 and 10.** `!/^[\p{L}?]$/u.test(letter)` and `!/^\p{L}$/u.test(blankAs)`. Same function as site 7; removing site 7 alone changes nothing. 3.1 must become ten places / seven items.
2. **The board is *not* the only lossy field left — `backend/gamecore/state.py:33-44` is worse, and it feeds the AI's own eyes.** `build_ai_state_dict` does `row_chars.append(cell.letter)` then `grid.append("".join(row_chars))`. A single `SZ` makes that row **16 characters**, silently shifting every column to its right. `:48` `ai_rack="".join(ai_rack)` collapses a digraph rack into an ambiguous character run. This flows through `services.py:1611-1618` `compact_state` into `prompts.ts:314` `extractGridRows` / `renderLabeledBoard(gridRows)` / `listAnchorSquares(gridRows)`. After your wire change the *human* sees `SZ` correctly and the *model* sees a corrupted, off-by-one grid — a silent wrong board of exactly the kind D-3 exists to prevent, just one layer inward. `gamecore/state.py` is neither allowlisted nor listed in section 8; `prompts.ts` is frozen by P-A and `test_atomic_tile_tokens.py:531` pins `["grid","blanks","ai_rack",…]` and is forbidden. **This needs its own exchange and probably its own MOVE CORE hash re-pin.** I rate it higher-risk than the dictionary-authority work you scheduled next.
3. **`backend/game/diagnostics.py` holds four more single-code-point letter guards** — `:373` `len(blank) == 1 and blank.isalpha() and blank in playable`, `:374` `len(normalized) == 1 and normalized.isalpha()`, `:782` `_ascii_letter` `len(ch) == 1`, `:789` `is_diacritic_letter` `len(folded) == 1`. Forbidden here by D-5, correctly. Note `.isalpha()` also rejects `L·L`, so the canary's shape breaks these twice over.
4. **`serializers.py:275` fails the canary twice too.** `nfc.isalpha()` is `False` for `L·L`. Dropping only `len(nfc) == 1` leaves the digraph accepted but the interpunct rejected. F2 is a *backend-legality* canary today and does not traverse `PlacementSerializer`; it will not catch this. Your replacement predicate needs to drop `.isalpha()` or delegate to the variant's playable set — worth naming explicitly in the next prompt.
5. **Section 6 undercounts the re-pointing, and section 8 contradicts the allowlist about it.** Beyond `:12/:16/:264/:266/:267`, `test_atomic_token_persistence.py::test_p7_adapter_is_lossless_for_english_blank_board` at **`:233-253`** asserts the *old* wire shape outright — `len(state["board"]) == 15`, `all(isinstance(row, str) and len(row) == 15 …)`, `state["board"][7][7] == "A"`, `state["blanks"] == [{"row": 7, "col": 7}]`, `state["board"][7] == "." * 7 + "A" + "T" + "." * 6`. Its invariant survives; its shape cannot. Also **`test_api.py:1078`** `data["state"]["board"][7][7:9] == "AT"` and **`test_api.py:1324`** `data["state"]["board"][7][7:10] == "JOE"`. All three are inside the allowlist, so authorized — but section 8's "Section 6 is the one authorized re-pointing" reads as forbidding them. Please widen section 6 to name all five.
6. **Section 3.2's tile-component paths are wrong** — `components/tiles/`, not `components/game/`. Substantive claim holds. `components/board/Cell.tsx` belongs on that list too.
7. **Websocket consumers carry no independent assumption.** `consumers.py:41,135,143` forward `services.get_game_state_for_user` verbatim; `git grep board -- backend/game/consumers.py` is empty. Multiplayer is covered for free by the `_build_state` change — but the client refusal must therefore also cover the `game_state` / `match_found` websocket frames at `page.tsx:1132` and `waiting/[id]/page.tsx:61`, and the latter is off-allowlist. Another reason the refusal belongs in `setGameState`.
8. **Move-history serializer and draw payload are already lossless.** `services.py:96-110` passes `move.placements` / `move.words_formed` through untouched from JSONFields. `services.py:525-531` `_serialize_ai_starting_draw` emits whole tokens (`"human_tile": draw["slot0_tile"]`), consumed as plain strings at `types.ts:78-79` and `draw/[id]/page.tsx:135-136`. Neither needs work in any exchange. Rule scoped correctly.
9. **`gamecore/state.py:79` already calls its save format "schema 4"** (`_require_schema_4`). Your inherited wire value `4` will collide *nominally* with an unrelated versioning axis. Not a defect, but `state_schema_version` and the save `schema_version` will be two different 4s, and someone will eventually conflate them.

**LEAD** — suspected, not proved.

1. `Board.tsx:597-602` builds `letter` as `pending ? (pending.blank_as || pending.letter) : boardLetter !== "." ? boardLetter : null`. Under D-1 the `"."` sentinel disappears entirely and `Cell` receives `string | null`. I expect that to be a clean simplification, but I have not typechecked it. Watch for `Cell.tsx` prop narrowing.
2. `Board.tsx:119`'s fallback `Array(BOARD_SIZE).fill(".".repeat(BOARD_SIZE))` becomes an empty-grid constructor. `Array(15).fill(...)` with a shared inner array would alias all fifteen rows; the current string version cannot alias. A careless port could.
3. I suspect no server-side zod/schema validation of the inbound game state exists anywhere in the client — `api.getGameState` appears to cast (`page.tsx:538` `as GameState`). If so, D-3's refusal is the *first* runtime validation the payload ever receives, which raises its importance and argues for refusing loudly rather than degrading.
4. Once sites 3/4 relax, `PlacementSerializer` will accept any non-empty token. I suspect nothing downstream bounds token length, so an adversarial 10 000-character `letter` may reach the board/scoring path. `_bounded_ident` at `serializers.py:71-79` caps at `_IDENT_MAX = 200` but is used for ai_metadata, not placements. Worth a bound in the same exchange that removes the guards.

---

**Smallest next step:** reissue this exchange with `frontend/src/hooks/useGameStore.test.ts` added as a tenth allowlisted path, section 3.1 restated as ten places across seven items (adding `route.ts:329` and `:334`), section 6 widened to name `test_atomic_token_persistence.py:233-253` plus `test_api.py:1078` and `:1324`, and section 3.2's tile paths corrected to `frontend/src/components/tiles/`. Nothing else in the prompt needs to change — the design (D-1…D-6), the baseline, and every other coordinate are sound and re-verified.

Report justification: `new-evidence`
`Logical-whole closure: not-closed`

**Authority expiry:** my authority under `03_implementation_00.md` expires with this terminal report. I hold no implementation, Git, or network authority beyond it, and I will take no further action on this task without a new complete authoritative prompt. This is a BLOCKED implementation report, not acceptance — the required fresh independent acceptance is still outstanding and is not mine to give.

**Context pressure:** low. Roughly a fifth of the window used; no compaction occurred. Read-only investigation and one full ladder run were inexpensive, and I stopped before the edit phase that would have consumed the most.
