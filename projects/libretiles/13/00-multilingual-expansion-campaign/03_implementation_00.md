You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Prior logical whole identity: multilingual-expansion
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: MEC-C1a — a multi-code-point tile crosses the wire losslessly. The temporary board adapter and all EIGHT single-code-point guard sites are removed TOGETHER with a new state_schema_version. Dictionary-authority work is a LATER exchange and is NOT in this one.
Phase: Implementation
Implementation authority: explicit
Exact baseline: 8a50ded8b743d0badf7cca7fc3178a11d4b54be1
Changed-path allowlist: backend/game/services.py · backend/game/serializers.py · backend/tests/test_atomic_token_persistence.py · backend/tests/test_api.py · frontend/src/lib/types.ts · frontend/src/components/board/Board.tsx · frontend/src/app/game/[id]/page.tsx · frontend/src/app/api/ai/move/route.ts · frontend/src/hooks/useGameStore.ts
Implementation boundaries: change the WIRE PROJECTION of the board only. NO change to the persisted board_state shape, to any asset, manifest, lexicon or build script, to prompts.ts, or to any provider surface. ONE commit.
Independence required: no
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Evidence tier: E3
Evidence tier basis: a wire-format change to a shipped, playable product with TWELVE variants and live human-vs-human multiplayer. It removes eight guards that currently fail closed, it introduces a schema version the client must honour, and a mistake renders a wrong board rather than raising. Reversible by one revert, but the blast radius is the whole game surface.
Authorized implementation stages: repository gate, read the design record inlined in section 3, implement, prove the new fixtures fail before they pass, all eight standing gates, MOVE CORE hash proof, twelve-variant proof, ONE commit, pre-push equality gate, one non-force push, public readback, terminal report
Combined implementation envelope: allowed
Implementation stage gates: no commit before the two-token fixture AND the L·L canary AND the schema-refusal test all pass, and before `manage.py validate_lexicons` still reports THIRTEEN assets; no push before all eight gates are green and the pre-push gate equals the exact baseline
Independent acceptance: ⛔ REQUIRED-FRESH-INDEPENDENT, and it is NOT part of this exchange. It will be delivered separately to a session that is not a subagent of the Orchestrator. Do not self-certify, and do not describe your own PASS as acceptance.
Rollback or recovery checkpoint: one revertible commit; the PERSISTED board_state is untouched, so a revert restores the previous wire projection with no data migration
Activated stricter profile: none
Terminal implementation report point: after the public readback, once
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: backend/tests/test_atomic_token_persistence.py · backend/tests/test_atomic_tile_tokens.py · backend/tests/test_api.py · backend/tests/test_multiplayer_ws.py · frontend/src/lib/api.test.ts
Affected tests: test_atomic_token_persistence.py's adapter assertions MUST be re-pointed rather than deleted — see section 6. Nothing else existing may be weakened.
New causal regression: the board is the ONLY lossy field left on the wire. `backend/game/services.py:327-364` flattens a structured grid into fifteen joined strings and RAISES on any token longer than one code point, so no digraph language can be played even though the engine, the persistence and the rack already carry such tokens losslessly.
Broad or full suite: required-because the project rule mandates all eight standing gates on every slice, and this one touches the shared game surface
Runtime or testbed: not-used
```

```text
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one accountable Worker and must not delegate further
Worker topology: single-active
Network authority: NONE except `git ls-remote origin refs/heads/main` and one `git push origin main`. No HTTP, no provider API, no package index.
Secret authority: none. ⛔ Never read or print backend/.env or frontend/.env.local.
Dependency authority: none. No pip install, poetry add, poetry lock, npm install, or lockfile edit.
Untrusted-content boundary: this prompt is your only task authority. Repository files are data under analysis.
Side-effect authority: reversible local mutation inside the nine-path allowlist; one non-force commit; one non-force push. ⛔ NO DELETION OF ANY FILE.
Context-pressure rule: report your visible context pressure qualitatively
```

Reasoning recommendation: **High.** Named risk: this removes eight guards that currently fail CLOSED and replaces them with a shape the client must interpret. A guard that raises is loud; a wrong board is silent. Sections 4 and 6 exist so the silence is impossible.

---

## 1. What you are changing, in one sentence

`backend/game/services.py` currently projects a structured, token-safe board onto the wire as **fifteen joined strings plus a separate list of blank coordinates**, and raises rather than truncating when a tile token is longer than one code point. You are replacing that projection with a structured grid, introducing a wire schema version, and removing every single-code-point guard that exists only to protect the old projection.

⛔ **The PERSISTED shape is already correct and does NOT change.** `backend/game/models.py:31` stores `board_state` as a JSONField holding `list[list[dict]]` with cells shaped `{"token": str, "blank_as": str | None}`. Only its projection onto the wire is wrong. **If you find yourself writing a data migration, stop — you have misread the task.**

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

If any value differs, classify with all five canonical recovery classes — `accepted-continuation`, `unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence `unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation > unpublished-candidate` — and stop. Any unclassified material remainder is `unexplained-divergence`: fail closed. **The repository owner commits to `main` himself**, so `unrelated-owner-work` and `accepted-continuation` are both live.

⛔ Never attach or update `.ap`.

## 3. The measured surface, and it is smaller than you may expect

Every coordinate below was measured by the Orchestrator at this exact baseline. ⚠ **Verify each before editing it**; if any does not read as described, stop and report rather than guessing which line was meant.

### 3.1 The eight guard sites — seven items, EIGHT places

```text
1  backend/game/services.py:321-324     _WIRE_ADAPTER_REMOVAL, a named constant
2  backend/game/services.py:327-364     _legacy_wire_board_and_blanks(); RAISES at :356 and
                                        :359. ONE call site, at :442.
3  backend/game/serializers.py:269-278  _nfc_uppercase_letter(value, *, allow_blank) — the
                                        `len(nfc) == 1` test is at :275
4  backend/game/serializers.py:286-290  PlacementSerializer.validate_letter / validate_blank_as
5  frontend/src/app/api/ai/move/route.ts:121-124   letter: z.string().length(1)
6  frontend/src/app/api/ai/move/route.ts:125-129   blank_as: z.string().length(1).optional()
7  frontend/src/app/api/ai/move/route.ts:341       blankAs && blankAs.length === 1
8  frontend/src/app/api/ai/move/route.ts:1002      typeof letter === "string" && letter.length === 1
```

⚠ Site 8 filters `playability.exchange_letters`, which are RACK tokens, not board letters. It is still a single-code-point assumption and still wrong for a digraph rack, so it goes — but note that it is a different code path from the other seven and needs its own thought about what the correct predicate is (a non-empty string).

### 3.2 What is ALREADY lossless — do NOT "fix" these

```text
backend/game/models.py:31        board_state JSONField, structured cells. Correct already.
backend/game/services.py:459     "my_rack": list(my_slot.rack)          — already lossless
frontend/src/lib/types.ts:65     my_rack: string[]                      — already lossless
frontend/src/components/board/Board.tsx, components/game/Tile.tsx, components/game/TileRack.tsx
    contain NO single-character assumption about letters. Every `.length === 1` and `[0]` in
    Board.tsx is TOUCH-EVENT handling at :421-:503. ⛔ Leave all of it alone.
backend/gamecore/legality.py:112 evaluate_scoring_move ALREADY accepts
    `authority: WordAuthority | None = None`. ⛔ THAT IS THE NEXT EXCHANGE, NOT THIS ONE.
```

### 3.3 The board consumers you must update — all of them

```text
frontend/src/lib/types.ts:48       board: string[]
frontend/src/lib/types.ts:49       blanks: { row: number; col: number }[]
frontend/src/components/board/Board.tsx:119   grid = gameState?.board ?? Array(BOARD_SIZE).fill(".".repeat(BOARD_SIZE))
frontend/src/components/board/Board.tsx:120-122  blanks = new Set((gameState?.blanks ?? []).map(...))
frontend/src/components/board/Board.tsx:556     const boardLetter = grid[row]?.[col];
frontend/src/components/board/Board.tsx:597     const boardLetter = grid[row]?.[col] ?? ".";
frontend/src/components/board/Board.tsx:615     isBlank={pending ? pending.letter === "?" : blanks.has(key)}
frontend/src/app/game/[id]/page.tsx:1212        const boardLetter = gameState?.board?.[row]?.[col];
                                                followed by `if (boardLetter && boardLetter !== ".")`
frontend/src/hooks/useGameStore.ts              persist name "libretiles-store", version 5,
                                                migrate chain `< 1` through `< 5` at :273-296
```

## 4. The design — six decisions already taken. Implement them; do not re-decide them.

### D-1 · the wire cell shape

```text
board: BoardCell[][]                     exactly 15 rows of exactly 15 cells
BoardCell = { token: string; blank_as: string | null } | null
empty cell -> null
```

⛔ **`null` for empty, not `{token: ""}`.** `services.py:341-344` already treats any non-dict persisted cell as empty, so `null` is the honest wire spelling of what storage means. Two ways to say "empty" is how a test eventually asserts the wrong one.

⛔ **A grid, not a sparse list of placed cells.** Both remaining consumers index by coordinate, so a grid keeps that access pattern with a field read instead of a character read. A sparse list would force every consumer to build an index first.

### D-2 · `blanks` is REMOVED from the payload

It is a second source of truth for a fact the cell now carries — `services.py:361` derives it by testing `token == "?"`. Keeping both leaves two representations that can disagree. `Board.tsx:615` becomes a direct cell test.

### D-3 · `state_schema_version: 4` is a NEW field

⛔ **MEASURED: the field does not exist anywhere today.** It appears only inside the adapter's own comment text at `services.py:323` and `:332`, and in one test assertion. So you are INTRODUCING it, not incrementing it.

⛔ **The value is 4 and it is INHERITED, not chosen.** The constant text and the existing test both name 4. Renumbering to 1 would falsify an assertion that already ships.

⛔ **The client must REFUSE a version it does not understand rather than mis-render one.** A wrong board is silent; a refusal is loud. Where and how you surface that refusal is yours to design, but it must not be a console warning that renders anyway.

### D-4 · the client store goes 5 → 6

⛔ **MEASURED: it is already at version 5, not 4.** Bump to 6 and append a `version < 6` branch.

⚠ The store persists **preferences** — token, locale, `selectedVariantSlug`, `aiTimeout`, `aiMaxSteps` — **not game state**. So the v6 branch may have nothing to do. **If it has nothing to do, say so in a comment inside the branch rather than omitting the branch.** A silent gap in a migrate chain is how a stale preference survives a schema change, and the next person cannot tell an intentional no-op from a forgotten one.

### D-5 · dictionary authority is NOT in this exchange

⛔ `_word_passes_dictionary` stays. `evaluate_scoring_move` keeps its current call sites. `backend/game/diagnostics.py` and `backend/gamecore/move_search.py` are NOT on the allowlist. They are the next exchange, deliberately, because they fail for different reasons and a revert must be able to take one without the other.

### D-6 · what must not change

Enumerated in section 8.

## 5. Fixtures — three, and each one catches a different mistake

```text
F1  TWO DIFFERENT MULTI-CHARACTER TOKENS end to end.
    ⛔ NOT only `SZ`. Use `SZ` and one of `DZS` or `LJ`, so an implementation that generalized to
    "exactly two characters" fails. Drive a token from persisted board_state through the wire
    projection and assert BOTH tokens arrive intact, including one placed as a blank
    (`token: "?"`, `blank_as: "SZ"`).
    ⚠ SYNTHETIC TOKENS ARE CORRECT HERE. MEASURED: not one of the twelve shipped variants has a
    digraph tile — which is exactly why they could all ship before this change. Hungarian is the
    first real consumer and it lands AFTER this exchange. Do not wait for a real variant and do
    not add one.
F2  THE L·L SYNTHETIC CANARY still passes.
    backend/tests/test_atomic_tile_tokens.py:240-284 already owns it (`token = "L·L"`, asserting
    `L·LA` reaches legality). ⛔ Do not modify that test. Run it and quote the result. It exists
    to prove the implementation did not generalize only to `len(token) <= 2 && isalpha()` — and
    `L·L` is three code points and contains a MIDDLE DOT, which `isalpha()` rejects.
F3  A PAYLOAD WITH AN UNKNOWN state_schema_version IS REFUSED BY THE CLIENT.
    Assert the refusal, not just the absence of a crash. This is D-3's teeth.
```

Pre-fix capture:

```text
CLASS B  F1 and F3 must each be shown to FAIL against the unmodified code, and the failure text
         quoted. F1 will fail because the adapter RAISES _WIRE_ADAPTER_REMOVAL; quote that. F3
         will fail because no version field exists to disagree with.
         F2 must be shown to PASS both before and after — it is a canary, not a new test, and a
         canary that changes state is not a canary.
```

## 6. `test_atomic_token_persistence.py` — re-point, do NOT delete

```text
:12   imports _WIRE_ADAPTER_REMOVAL by name
:16   imports _legacy_wire_board_and_blanks by name
:264  asserts the raised message EQUALS _WIRE_ADAPTER_REMOVAL
:266  calls the adapter directly
:267  asserts "state_schema_version 4" appears in the message
```

Both symbols are being deleted, so those assertions cannot survive unchanged. ⛔ **Do not delete the test.** It encodes a real invariant — *a multi-code-point token must never be silently truncated on the way out* — and that invariant still holds; only its mechanism changes from "raise" to "carry losslessly". **Re-point it to assert the new behaviour**, and say in the test's own comment what it used to assert and why the replacement is the same invariant. A deleted test is indistinguishable from a lost one.

## 7. Required proofs beyond the fixtures

```text
P-A  MOVE CORE UNCHANGED. `frontend/src/lib/prompts.test.ts` pins SHA-256
     c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60 and version
     pfr-s2-core-1. prompts.ts is NOT on the allowlist; quote the passing assertion as proof.
P-B  TWELVE VARIANTS STILL PLAYABLE. `manage.py validate_lexicons` must still report THIRTEEN
     assets, 0 failed, and `GET /api/game/variants/` must still return twelve rows all
     `playable` with exactly the four keys {slug, display_name, language_code, readiness}.
     ⛔ `state_schema_version` belongs to the GAME-STATE payload, not to the variant catalog.
     If it appears in a variant row you have broken standing condition 1.
P-C  THE ADAPTER IS GONE. `git grep -n "_legacy_wire_board_and_blanks"` and
     `git grep -in "_WIRE_ADAPTER_REMOVAL"` must both return only what section 6 left behind,
     and you must report both counts. Run BOTH cases; an absence claim with one case is not a
     finding.
P-D  NO SINGLE-CODE-POINT GUARD REMAINS ON A LETTER PATH. Report, per site, the eight
     coordinates from section 3.1 and what each became.
```

## 8. What must not change

```text
⛔ NO change to the persisted board_state shape, and NO Django migration. Storage is correct.
⛔ NO byte under backend/assets/ may change. `git status --porcelain=v1 -- backend/assets/` MUST
   be EMPTY at every point. Twelve variants ship and their behaviour is byte-unchanged.
⛔ NO change to frontend/src/lib/prompts.ts. The MOVE CORE hash and version are proof P-A.
⛔ NO change to backend/game/diagnostics.py, backend/gamecore/move_search.py,
   backend/gamecore/legality.py or backend/gamecore/word_authority.py. Dictionary authority is
   the NEXT exchange, by decision D-5.
⛔ NO deletion of any test file, and no weakening of any existing assertion. Section 6 is the one
   authorized re-pointing.
⛔ NO change to backend/tests/test_atomic_tile_tokens.py. It owns the L·L canary and the canary
   must be observed, not edited.
NO provider list, provider constant, model tuple, provider tier or provider documentation, ANYWHERE.
   A standing decision freezes all of them.
NO new dependency, no lockfile edit, no mypy scope change.
NO reading backend/.env or frontend/.env.local.
NO `git add -A`, no `git add .`, no force, amend, rebase, reset, clean, stash, branch, tag.
NO writing under /home/agile/meta/ and no temporary file outside /tmp/opencode/mec-c1a/.
```

✅ **Cross-check performed when this prompt was written.** Sections 4-7 require edits to exactly the nine allowlisted paths: `services.py` and `serializers.py` (backend guards and the new projection), `test_atomic_token_persistence.py` and `test_api.py` (assertions), and the five frontend files that consume the board or carry a length guard. Section 8 forbids `diagnostics.py`, `move_search.py`, `legality.py`, `word_authority.py`, `prompts.ts`, `test_atomic_tile_tokens.py` and everything under `backend/assets/` — none of which sections 4-7 ask you to touch. Section 6 authorizes re-pointing one test while section 8 forbids weakening assertions; those are compatible because re-pointing preserves the invariant and the section says so explicitly. If you find a genuine contradiction, stop and report it rather than choosing an interpretation.

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
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP AND REPORT. Never
    fall back to ambient `python3` or to `poetry run`.
```

⛔ `manage.py check` takes no `-m`. Then from `frontend/`: `npm run typecheck`, `npx vitest run`, `npm run lint`, `npm run build`.

Baseline at `8a50ded8b743d0badf7cca7fc3178a11d4b54be1`, measured by the Orchestrator — re-measure, do not trust:

```text
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       742 passed, 4 skipped in 267.80s
pytest --collect-only                        746 tests collected
manage.py validate_lexicons                  13 asset(s) audited, 0 failed, exit 0
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped (31 files | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

⚠ Counts will MOVE this time, unlike the last several slices: you are adding tests and changing
assertions. Report the new numbers and account for the delta — which tests you added, which you
re-pointed — rather than only quoting a summary. ⚠ Wall-clock times are machine noise; counts and
exit codes are the comparison.

The four standing traps, none optional:

```text
1  backend/pyproject.toml sets addopts = "-q". A second -q SILENTLY suppresses the summary.
2  mypy on the FULL documented scope, never narrowed and never widened.
3  Check `ss -tlnp | grep :3000` before `npm run build`. A listener means STOP. Never pkill.
4  "The build passed" and "the code type-checks" are TWO SEPARATE CLAIMS. State both.
```

## 10. Git authority — one commit

```bash
cd /home/agile/Projects/libretiles
git add <the paths you actually changed, named individually>
git status --porcelain=v1                       # MUST be a subset of the nine-path allowlist
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
the section 2 gate does not match on any line, or backend/assets/variants/ does not hold 12 files
any coordinate in section 3 does not read as described — report both what I claimed and what you
    found, and stop
F1 or F3 PASSES before the change — the fixture has no teeth
F2, the L·L canary, does not pass BEFORE the change — the baseline is not what this prompt
    describes, and you must not proceed on a tree you cannot characterize
F2 stops passing AFTER the change — the implementation generalized to a shape that excludes a
    three-code-point token containing a middle dot; stop, do not weaken the canary
`git status --porcelain=v1 -- backend/assets/` is non-empty at ANY point
`manage.py validate_lexicons` no longer reports 13 assets, 0 failed
the variant catalog stops returning twelve playable rows with exactly its four keys
the MOVE CORE hash assertion fails
completing the work would require a path outside the nine-path allowlist — in particular
    diagnostics.py, move_search.py, legality.py or word_authority.py, which belong to the NEXT
    exchange
you would need a Django migration
`git ls-remote` no longer equals the exact baseline at the pre-push gate
```

Stop normally — success — when the adapter and its constant are gone, all eight guard sites are removed or corrected, the wire carries `board: BoardCell[][]` and `state_schema_version: 4`, `blanks` is gone from the payload and its consumer, the store is at version 6 with an explicit branch, F1 and F3 are proven to fail before and pass after, F2 passes unchanged both times, twelve variants remain playable, the MOVE CORE hash is proved unchanged, all eight gates are green, one commit is pushed non-force, and the public readback equals `git rev-parse HEAD`.

## 12. Report contract

The FIRST CHARACTER of your reply must be `#`, so it begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then, in this order: the coordinate line reading `logical whole multilingual-expansion-campaign, Worker session ordinal 03, Worker exchange ordinal 01`; status; `Phase-qualified result:` one value from the closed enum at `PROMPT_CONTRACTS.md:206`; `Result artifact or commit:`; `Result evidence:`; start and end commit; the section 2 gate values verbatim plus an end-of-task porcelain re-confirmation **including `git status --porcelain=v1 -- backend/assets/` shown empty**; changed files and purpose; **the EIGHT guard sites from section 3.1, each with what it became**; **the new wire payload shape, quoted from the code, including the `state_schema_version` field**; **the exact diff of every frontend board consumer**; **the store migrate branch as committed**; the test table with F1, F2 and F3 and every class B failure quoted verbatim; **proof P-A the MOVE CORE hash assertion passing, quoted**; **proof P-B thirteen lexicon assets and twelve playable variant rows**; **proof P-C both grep counts, case-sensitive and case-insensitive**; **proof P-D the per-site table**; all eight gates each with its own quoted line, the pytest summary verbatim, the `--collect-only` count with the delta accounted for, and the mypy file count; both separate frontend claims; the Git sequence with the pre-push value, the commit SHA, the push result and the readback equality; deviations, risks, missing evidence; `Resolved Execution Issues / Near-Misses:`; `Pre-Existing Failure Classification:`; then:

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
   Two separate labelled lists: MEASURED and LEAD.
   MEASURED means you ran something and it produced that result. LEAD means you suspect it and
   have not proved it. Do not merge them and do not leave an item unlabelled.
   This section has already caught a false premise in one of my prompts and a rule I had scoped
   backwards. It is the highest-value part of your report and I read it first.
   In particular, and it matters for the NEXT exchange: if you can see any OTHER place where a
   letter is assumed to be one code point — in the websocket consumers, the diagnostics harness,
   the move-history serializer, or the draw payload — NAME IT with its file:line. I would rather
   learn it now than after Hungarian ships.
```

then one smallest next step; exactly one report justification from `new-mutation | new-evidence | new-material-risk | changed-external-state | final-acceptance | explicit-closure`; `Logical-whole closure: not-closed`; an authority-expiry statement; and your qualitative context pressure.

⛔ **Your PASS is an implementation PASS and nothing more.** This slice requires fresh independent acceptance from a session that is not a subagent of the Orchestrator, and that is not you. Do not describe your own verification as acceptance.

One value per field. No visible mid-sentence self-corrections. Summarize command output; full output only for failures, unexpected state, or safety-critical evidence.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/
Archival: wait-for-report
```

You do not archive this pair. Your authority expires at your terminal report, and no `PASS` you report closes anything.
