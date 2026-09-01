Artifact class: **Orchestrator acceptance record** for Worker session 01, exchange 02 of logical whole
`multilingual-tile-token-foundation` (Meta 11/01). Not authority. Filename deviation as in
`10/00-ui-internationalization/90_orchestrator-restoration.md`.

✅ **ARCHIVE COMPLETE, corrected 2026-09-01.** An earlier version of this note said the verbatim
exchange-02 prompt and report were not stored here. That was true when it was written and is no longer
true. The Cooperator archived all four files at 18:29–18:30:

```text
01_plan_00.md   01_report_00.md    Worker session 01, exchange 01 — the BLOCKED planning exchange
01_plan_01.md   01_report_01.md    Worker session 01, exchange 02 — the accepted plan
```

A duplicate misfiled set under `10/02-ui-locales-visegrad/` was verified content-identical and deleted at
his instruction. See section 9 of `00_handout.md` for the two recorded report deviations. This file
records the acceptance decision and the independently verified evidence; the four files above are the
primary historical record.

---

# Acceptance of the planning report — 2026-09-01

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 01
Worker exchange ordinal: 02   (exchange 01 returned planning-BLOCKED; see DEFECT_LEDGER.md)
Baseline observed by the Worker: 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
Orchestrator verdict: planning-PASS, ACCEPTED with three corrections and one named dependency
Planning cycle consumed: the initial cycle. One targeted revision remains available.
Evidence independence: non-independent (current-session continuation) — labelled as such by the Worker
```

Report-shape gap, noted and not treated as a violation: the pasted report did not include the
`### Report for ORCHESTRATOR_CHAT` header, the coordinate echo, `status:`, `phase-qualified result:`,
or `report justification:`. It began at section 1. Exchange 01's report DID carry all of them, so this is
most likely a paste boundary rather than a Worker omission. Confirmed with the Cooperator rather than
assumed.

Three truncation artifacts appear in the report text — `**Obestablish canonical tokens`,
`1ays and sparse AI coordinate map`, and a bare `o`` for the bag_tiles row. Content is recoverable from
context. The same artifact class was recorded for the `audit-02` report and for the era-10 handout.

## What the Orchestrator independently verified

Every load-bearing claim was checked in the repository rather than accepted:

```text
MOVE CORE pinned hash        the quoted c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60
                             is REAL — frontend/src/lib/prompts.test.ts:22-23, asserted at :81 over
                             MOVE_SYSTEM_PROMPT. The Worker did not invent it.
MOVE_PROMPT_VERSION          "pfr-s2-core-1" at prompts.ts:12                          CONFIRMED
game migration leaf          0007_consumedwsticket, so 0008/0009 are the correct next   CONFIRMED
GameSession.blanks           models.py:30 JSONField, read/written at services.py
                             237, 258, 267, 274, 370, 482, 497                          CONFIRMED
                             *** The Orchestrator's own reconnaissance MISSED this field. The Worker
                             found a whole persistence surface the prompt never named. ***
AEIOU hardcoded              move_search.py:536 and :540, in ranked leave quality       CONFIRMED
overlay code-point split     AIThinkingOverlay.tsx:70 word.toUpperCase().split("")      CONFIRMED
five db_table names          game_session, game_player_slot, game_move,
                             game_chat_message, game_consumed_ws_ticket                 CONFIRMED
isPlausibleRack              lib/rack.ts, called at game/[id]/page.tsx:541 and :1541    CONFIRMED
```

## Correction 1 — the `.` / `#` occupancy grid collides with an existing validator

The report proposes rendering the AI board context as fifteen fixed-width occupancy rows using `.` and
`#`, arguing the pinned CORE's "15 zero-based rows" description stays true.

Measured: `frontend/src/lib/prompts.ts:190` is `const GRID_ROW = /^[\p{L}.]{15}$/u`. An occupied cell
must match `\p{L}`. `#` would be REJECTED. And `prompts.ts:136` tells the model the board renders as
`row 00 |...............| through row 14`, i.e. dots and letters.

`GRID_ROW` is not part of the hashed bytes — the hash is over `MOVE_SYSTEM_PROMPT`, which is
`moveSystemPromptFor(englishMoveSpec)` — so widening it would not break Lock B. But it would leave the
CORE telling the model one thing while the runtime sends another, which is the report's own risk 13.

**Orchestrator direction, better than both options:** render an occupied cell as the FIRST CODE POINT of
its token. That is a letter, so `GRID_ROW` still matches unchanged, the CORE prose stays literally true,
and the row stays exactly fifteen characters. The full token lives only in the sparse exact map the
report already designs — `(07,08)=SZ`, `(08,08)=?→CS`. Ambiguity between `S` and `SZ` in the grid is
resolved by the sparse map, which is authoritative. Zero tension with Lock B, no validator change, no
new marker character the model was never told about.

## Correction 2 — do NOT delete the `AEIOU` leave term; make it variant data with an English default

The report recommends removing the vowel-imbalance component of ranked leave quality rather than adding
variant vowel metadata, calling the latter "unsupported complexity".

The Orchestrator disagrees, and the reason is a project fact the Worker could not know: `PROJECT_CONTEXT`
section 6 records that **the engine authors every move in this product** — across a dozen counted live
provider invocations the free LLM authored zero backend-valid placements, and every completed live turn
used `completion_source: backend_ranked_candidate`. Ranked candidate ordering is therefore not a
secondary heuristic. It is what the player actually sees the AI play, and the measured engine numbers
(520–560 per side, ~29 plies, all 17 single-copy diacritic tiles consumed) were produced under the
current ranking.

Deleting the term changes shipped English and Slovak AI behaviour to fix a problem that only exists for
Czech, Polish, and Hungarian. Adding an optional variant `vowels` field that DEFAULTS to `"AEIOU"` is
strictly less risky: byte-identical behaviour for English and Slovak, correct behaviour for the new
variants, one field, no deletion. Adopt that instead.

## Named dependency the plan creates and cannot satisfy itself

Decision 3 makes an explicit official game alphabet a REQUIRED manifest field for all five variants. The
Orchestrator does not hold authoritative alphabet orders for Czech, Polish, or Hungarian, and Slovak's
correct order is only partly recorded (`PROJECT_CONTEXT` locked fork 1 records the tile SET, not the
collation). Getting this wrong silently reintroduces `uii-01-F07` in a new language.

This is a data-sourcing dependency of the same class as the dictionaries: it belongs with the Cooperator,
who has already used ChatGPT with web search successfully for the distributions. It must be supplied and
recorded with provenance before the second whole activates, and English and Slovak orders must be
supplied before the FIRST whole can add the field at all.

## The eight decisions from report section 21

All eight are Orchestrator-owned routing, schema, and sequencing decisions rather than Cooperator
material decisions, except where noted.

```text
1  two-whole split                     ACCEPTED. atomic-tile-token-foundation first, then
                                       czech-polish-hungarian-variant-activation. The boundary is the
                                       dictionary dependency, which is real and external.
2  ALLOW_DESTRUCTIVE_GAME_STATE_RESET   ACCEPTED, default false, fail-closed, abort on non-empty tables
   fail-closed, irreversible purge      without explicit opt-in, five named tables, no blanket flush,
                                        no-op on an empty database. The Cooperator authorized DELETION
                                        of development game state; he did not authorize a broad flush,
                                        and this design is what keeps those two apart.
3  explicit alphabets in manifests      ACCEPTED as a schema decision, BLOCKED on the data dependency
                                        above. English and Slovak orders must be supplied first.
4  two_letter -> two_tile_words rename   ACCEPTED, no alias. The old name encodes the wrong semantics and
   including the Slovak file rename      no external contract depends on it. Note it renames a SHIPPED
                                        asset, so the rename and its content hash must be asserted.
5  optional forbidden_token_sequences   ACCEPTED, empty for Hungarian. Locating the rule without
                                        inventing the language's behaviour is exactly right.
6  remove the AEIOU leave term          REJECTED. See correction 2. Variant `vowels` field defaulting to
                                        "AEIOU" instead.
7  Lock B stays closed                  ACCEPTED, with correction 1 applied so it stays closed without
                                        the CORE text becoming misleading.
8  production activation blocked until   ACCEPTED. No dummy dictionaries, no silent fallback to English
   dictionaries + licensing present      or Slovak, readiness computed and re-checked server-side.
```

## What the report got right that is worth preserving verbatim into the implementation prompt

```text
- the four-concept contract (atomic token / lexical contribution / container / code-point length) and
  the decision to keep lexical_contribution() and tile_display() as IDENTITY extension points rather
  than building rich tile objects now
- Cell = {token, blank_as} with realized_token, which keeps the physical blank identity while resolving
  its assignment, and which incidentally removes the separate GameSession.blanks store
- WordFound carrying lexical word AND realized tokens AND coordinates, so physical length is len(tokens)
  and never a string length
- one central gamecore.word_authority, and evaluate_scoring_move as the SOLE legality path for both
  human and AI submissions
- keeping the wire placement key `letter` as a documented legacy name rather than duplicating the schema
- prefix probes over the union of main-dictionary prefixes and all prefixes of two-tile authority words,
  which lets ÁCS be found with no reverse segmentation at all
- the readiness split between structural manifest parsing and playable loading
- the E4 classification of the destructive migration, and the R4 audit recommendation
- retiring persisted-game corruption from the risk register while naming wrong-table deletion as the
  new governing risk
```

## Next step

The plan is decision-complete. The next artifact is an implementation grant scoped ONLY to
`atomic-tile-token-foundation`, fresh Worker session, whose first action is the read-only
destructive-migration preflight and NOT migration execution.

The Orchestrator holding this context is deep into its window and will not write a five-slice E4
implementation grant to the standard this plan deserves. The proportionate route is a fresh Orchestrator
with a complete handout. That is a routing recommendation put to the Cooperator, not a decision taken
for him.
