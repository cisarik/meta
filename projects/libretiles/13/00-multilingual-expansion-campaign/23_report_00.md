# MEC-C1 plan — session 23, exchange 01

Delivered by the Cooperator (copy-paste route, per `00_handout.md` §10). Archived verbatim.
Disposition: **ACCEPTED** as the basis for implementation — see `00_notes.md` §61.
Six of the ORCHESTRATOR's claims were refuted; all six independently verified before acceptance.

---

# MEC-C1 — Complete atomic tiles through authority, AI context, and presentation

## 1. Confirm-or-refute measurement

Paths below are repository-relative. Output excerpts retain the relevant printed values; the Python probes executed in memory and created no test files.

| Claim | Finding | Command run and relevant output |
|---|---|---|
| Backend and frontend wire schema are 4 | **Confirmed** | `rg -n 'WIRE_STATE_SCHEMA_VERSION = 4\|return value === WIRE_STATE_SCHEMA_VERSION' backend/game/services.py frontend/src/lib/types.ts` → backend `:321`, frontend `:54`, exact-version check `:57`. |
| Wire board is `BoardCell[][]` | **Confirmed** | `rg -n 'type BoardCell\|board: BoardCell' frontend/src/lib/types.ts` → `BoardCell = { token: string; blank_as: string \| null } \| null`; `board: BoardCell[][]`. |
| Board/bag persistence is structured; model-level blanks column is gone | **Confirmed** | `rg -n 'board_state =\|bag_tiles =\|blanks =' backend/game/models.py` → JSONFields at `:31` and `:36`; no `blanks` field. |
| Migration 0008 exists and refuses populated state in both directions | **Confirmed by inspection** | `cat backend/game/migrations/0008_atomic_token_state_schema.py` and the targeted `RunPython` search → identical refusal callable at both ends of the operations list; `RuntimeError` names `manage.py purge_legacy_game_state`. Migration tests exist; not executed here. |
| F06 counts bag entries rather than code points | **Confirmed** | `rg -n 'return len\(tiles\)\|slot0_wins_starting_draw' backend/game/services.py` → `:318: return len(tiles) if isinstance(tiles, list) else 0`. |
| F07 uses variant starting-draw order | **Confirmed** | Same command → `:544: "slot0_first": variant.slot0_wins_starting_draw(...)`. |
| WordAuthority exists with the named methods | **Confirmed** | `wc -l backend/gamecore/word_authority.py` → `148`; method search found `for_variant`, `from_index`, `route`, `accepts_formed_word`, `is_lexical_word`, and `has_prefix`. |
| Evaluator already accepts optional authority | **Confirmed, with an important limitation** | Authority search → `legality.py:112: authority: WordAuthority \| None = None`. Reading its signature shows the positional `is_word` callable remains mandatory even when authority is supplied. |
| No multigraph guards survive | **Refuted** | `rg -n 'len\(blank\) == 1\|len\(normalized\) == 1\|GRID_ROW =' backend/game/diagnostics.py frontend/src/lib/prompts.ts` → diagnostics `:373–374` retain both one-character checks; prompt `:190` requires exactly 15 letter/dot code points per row. |
| Existing persistence tests prove multigraph transport | **Confirmed as existing coverage** | Read every test in `test_atomic_token_persistence.py`. P3/P4 cover `SZ` and blank `CS`; F1 specifically uses **SZ and DZS**, plus blank SZ. These tests were not rerun. |
| LocalStorage still needs v4 work from the handout | **Refuted as remaining work** | `rg -n 'version: 6\|version < 6\|PREFERENCES only' frontend/src/hooks/useGameStore.ts` → version **6**, with preferences-only persistence. No C1 storage migration is needed. |
| R1: Cell still stores letter/blank flag | **Confirmed** | Read-only `python3 -B` dataclass probe → `Cell storage: ['letter', 'is_blank', 'premium', 'premium_used']`. |
| R2: five production evaluator calls all use the callable | **Confirmed but incomplete inventory** | Evaluator search found services `:866/:1653`, diagnostics `:476`, search `:373/:585`; inspected arguments contain no `authority=`. Additionally, services `:908–909` directly validate joined strings when persisting moves, including human moves. |
| R3: old dictionary helper remains | **Confirmed** | `rg -n '_word_passes_dictionary\|invalid_words =\|is_word = _word_checker' backend/game/services.py backend/game/diagnostics.py` → definition `:209`, service call `:131`, diagnostic calls `:136/:352`, import `:20`. |
| AI projection may still be lossy | **Confirmed, for board and rack** | Read-only `build_ai_state_dict` probe → row `".......SZDZS......"`, row length **18**, rack `"SZDZS?"`; three rack entries have become an ambiguous string. |
| Request serializers and websocket transport still block multigraphs | **No blocker found in those paths** | Read placement/exchange serializers, AI tool schema, consumer and realtime code. Serializers use bounded whole-token validation; websocket state delegates to the structured service projection. Catalog search found no executable tile-length gate. |
| Board/rack/blank/draw rendering is wholly unfinished | **Refuted** | Read the relevant components: they already pass/render whole token strings and derive blanks from physical identity. However, `AIThinkingOverlay.tsx:72` still uses `word.toUpperCase().split("")` to draw candidate “tiles”. |

Additional read-only measurements:

- All twelve manifests have single-code-point playable tokens; none expands under the current NFC/casefold normalization. Only Slovak declares a two-tile list; none declares forbidden sequences.
- Comparing the actual baseline dictionary helper with WordAuthority across **10,457 ordered tile pairs** from all twelve shipped sets produced **zero disagreements**.
- Slovak’s allowlist contains **103 entries**. Its **135 distinct prefixes** produced zero disagreements between the current service prefix predicate and `WordAuthority.has_prefix`.
- Synthetic probes demonstrate real disagreements:

| Case | Old helper | WordAuthority |
|---|---:|---:|
| `Á + CS`, present only in two-tile authority | false | true |
| `Á + CS`, present only in main dictionary | true | false |
| `Á + C + S`, present in main dictionary | true | true |
| One physical `CS` tile with lexical entry `cs` | true | false |
| `L·L + A`, admitted by a custom index | false | true |
| Exact declared forbidden sequence `S + Z` | true | false |

Thus, **verdict equivalence is required over shipped legal tile configurations; universal equivalence would preserve known multigraph defects.**

## 2. Slice decomposition and implementation

### Slice A — Canonical cells and one formed-word authority

**Evidence tier: E3.** This changes every formed-word validation path and the in-memory state used for scoring.

**Ordering:** Implement and validate A first. Its commit retains the existing external AI-context contract and all current game-state formats. It is coherent for all twelve shipped variants, but does not complete C1.

**Exact changed-path allowlist and work:**

| Paths | Changes |
|---|---|
| `backend/gamecore/board.py` | Store `token`, `blank_as`, `premium`, `premium_used`. Make placement, clearing, and word extraction use canonical physical identity and realized tokens. Retain `letter`/`is_blank` as compatibility accessors backed solely by the canonical fields; preserve existing valid assignment idioms. |
| `backend/gamecore/scoring.py` | Score physical blanks as zero; otherwise look up the complete physical token. Preserve premiums, reuse rules, and bingo counting. |
| `backend/gamecore/state.py` | Adapt save-state import/export to canonical cells while retaining the existing save-file schema and external representation. AI projection changes belong to B. |
| `backend/gamecore/types.py` | Require `WordFound.tokens`; enforce matching token/coordinate counts and concatenation matching `word`. Remove the stale transitional promise. |
| `backend/gamecore/word_authority.py` | Own formed-word decisions, exact token-sequence decisions for search, query compatibility, and prefix lookup. Provide `accepts_tokens(tokens)` using the same routing logic as `accepts_formed_word`. Add the variant-derived dictionary-entry handling described below. |
| `backend/gamecore/legality.py` | Require keyword `authority: WordAuthority`; remove the callable argument and fallback branch. Retain complete `WordFound` records in the internal result so diagnostics can inspect physical words after temporary placements are cleared. Preserve existing result strings and scoring semantics. |
| `backend/gamecore/move_search.py` | Require authority in both public search functions and both searchers. Use whole-token authority for cross checks and completed prefixes, `has_prefix` for extension, and the same authority for final certification. Preserve traversal order, ranking, budgets, and cap semantics. |
| `backend/game/services.py` | Resolve one session authority; pass it through both searches and both evaluator calls. Replace the direct persisted-move word loop with `accepts_formed_word`. Delete `_word_passes_dictionary` and obsolete predicate plumbing. Preserve public string-query behavior separately, as specified below. Adapt session restoration to canonical cells. |
| `backend/game/diagnostics.py` | Give probe context one authority. Remove the one-character placement guards; validate normalized complete tokens against the variant tile set. Classify actual formed token sequences, not lexical lengths. Allow token-array racks in diagnostic fixtures while retaining existing single-character fixture strings. |
| `AGENTS.md` | Replace the obsolete requirement to call `_word_passes_dictionary` with the formed-word authority invariant; describe the retained advisory string-query boundary. Do not edit the managed AP block. |

The exact affected-test allowlist is:

```text
backend/tests/test_atomic_tile_tokens.py
backend/tests/test_atomic_token_persistence.py
backend/tests/test_dictionary_validation.py
backend/tests/test_slovak_engine.py
backend/tests/test_slovak_full_game.py
backend/tests/test_slovak_ranked_search.py
backend/tests/test_czech_polish_variants.py
backend/tests/test_ai_play_engine_diagnostic.py
backend/tests/test_endgame_policy_matrix.py
backend/tests/test_full_game_simulation.py
backend/tests/test_strength_benchmark.py
backend/tests/test_move_search.py
backend/tests/test_gamecore.py
backend/tests/test_api.py
backend/tests/diagnostics/test_turn_probe.py
backend/tests/test_word_authority_parity.py       [new]
backend/tests/test_multigraph_end_to_end.py       [new]
```

Existing tests migrate their callable fixtures and obsolete source assertions without weakening expected outcomes. Diagnostic tests must retain physical words while replaying placements; aggregate lexical strings must never be reverse-segmented to manufacture tile evidence.

**Cell invariant**

| Occupancy | `token` | `blank_as` | `realized_token` | Base points |
|---|---|---|---|---:|
| Empty | `None` | `None` | `None` | 0 |
| Ordinary tile | complete token `T` | `None` | `T` | `tile_points[T]` |
| Assigned blank | `"?"` | complete target `T` | `T` | **0** |

Inversion preserves behavior for valid states, but naïvely swapping field names does not. Restoration, clearing, blank toggling through compatibility accessors, save export, and scoring all require explicit coverage.

Malformed occupied records—particularly `"?"` without an assignment—must fail closed before evaluation, rather than silently becoming empty cells. This is an explicit invalid-state boundary; it is not a change to accepted game rules. Add negative coverage and preserve the existing NFC ingest behavior.

**Authority boundaries**

- Human persistence must switch its **word-verdict loop**. Do not route the entire human move path through the AI evaluator: doing so could change existing human zero-score or error behavior.
- `/validate-words/` accepts strings without physical placement evidence. Preserve its current trimming, normalization, short/nonalphabetic rejection, and lexical two-letter lookup behavior in an explicitly advisory `WordAuthority.accepts_word_query` method. Keep its response shape unchanged. No scoring or search certification may call that method.
- Search must not substitute `is_lexical_word` for final legality dictionary entries such as `AM` that formed-word authority rejects.
- `for_variant` must retain the current `str.isalpha` index behavior for all twelve current tile sets. For a variant declaring nonalphabetic characters inside a token, derive a stable cached entry predicate from those declared characters: require a letter, and permit only letters plus the declared nonletter characters. Keep explicit predicate injection available. This allows the L·L canary through a real temporary dictionary without globally broadening shipped indexes.
- No language-slug branch is needed.

### Slice B — Lossless AI context and truthful candidate presentation

**Evidence tier: E3 for the completed capability.** This closes the provider-input and presentation chain relied upon by C1 acceptance.

**Ordering:** B follows A. Backend AI-context production and frontend consumption change in the **same commit**. Game-state wire version remains 4, localStorage remains 6, and save-file schema remains unchanged.

**Exact changed-path allowlist and work:**

| Paths | Changes |
|---|---|
| `backend/gamecore/state.py` | Change AI state to a 15×15 structured cell grid and an ordered rack-token array. Carry blank identity inside cells; remove the AI-state blank sidecar. |
| `backend/game/services.py` | Produce that structured AI state. Preserve existing `compact_state` bytes for single-code-point states. For multigraph states, serialize the structured AI state as JSON, preserving cells, blanks, and rack boundaries. |
| `frontend/src/lib/prompts.ts` | Consume structured cells and rack tokens directly. Compute anchors by cell coordinates. Render multigraph board rows as token arrays with explicit blank information and format racks with spaces between complete tokens. Preserve current single-code-point prompt output and CORE bytes. |
| `frontend/src/components/game/AIThinkingOverlay.tsx` | For a tile alphabet containing multigraphs, render candidate words as lexical text with the authoritative total score. Do not infer physical tiles or per-tile values by splitting the word. Retain current single-code-point presentation. |
| `backend/tests/test_api.py` | Assert the updated AI-context contract and unchanged ordinary game-state payloads. |
| `backend/tests/test_multigraph_end_to_end.py` | Extend the synthetic service fixture through AI context after persistence and reload. |
| `backend/tests/test_atomic_ai_context.py` **[new]** | Cover structured projection, blank identity, distinct ambiguous segmentations, and unchanged single-code-point compact output. |
| `frontend/src/lib/prompts.test.ts` | Cover structured racks, exact board coordinates, anchors, blanks, multigraph formatting, and byte parity for existing prompts. |
| `frontend/src/app/api/ai/move/route.test.ts` | Exercise the new context with existing whole-token tool validation and a fake provider. |
| `frontend/src/lib/ai-turn-simulation.test.ts` | Update fake context production to the structured contract; preserve the simulation’s behavioral assertions. |
| `frontend/src/components/game/AIThinkingOverlay.test.ts` | Assert truthful multigraph candidate text and unchanged ordinary presentation. |
| `frontend/src/hooks/useGameStore.test.ts` | Extend v4 fixtures with distinct multigraphs and assigned blanks; retain version-6 persistence assertions. |
| `frontend/src/lib/atomic-tiles.test.ts` **[new]** | Render board/rack/blank-picker/draw fixtures to verify complete token labels and physical blank identity. |

**Compatibility decision:** The frontend prompt context temporarily accepts the old single-character AI shape as well as the structured shape. The legacy parser is used only for legacy contexts. If the supplied tile snapshot contains multigraphs, an unstructured context is rejected rather than reverse-segmented. Modern contexts always use arrays.

This preserves coherent commits and permits frontend-first deployment of B if deployment is later separately authorized. No deployment is part of C1 implementation authority.

**Meaning of “together” now:** There is no remaining v3/v4 game-state transition to coordinate. In A, all authoritative backend callers and search certification switch together. In B, AI-context production and consumption switch together. Neither commit claims that the entire capability is complete in isolation.

Rollback is code-only: revert B as a complete backend/frontend pair, then A if necessary. Do not reverse migration 0008 or purge game state.

## 3. Verdict-equivalence proof and acceptance fixtures

### Differential mechanism

Create `test_word_authority_parity.py` **before deleting the old helper**.

1. Freeze the exact baseline helper as a clearly labelled test-only legacy oracle. Record its source provenance and source digest.
2. While the production helper still exists, verify that the frozen oracle agrees with it.
3. Compare the oracle against WordAuthority using actual shipped dictionary loading and actual `WordFound` token sequences.
4. After deletion, retain the frozen oracle and the differential tests. The independent acceptor compares its source with the baseline Git object; it is not allowed to drift with the implementation.

The comparison corpus comprises:

- All ordered two- and three-tile sequences from each shipped tile set.
- Every dictionary/allowlist entry realizable by that shipped set within a board line.
- Existing English and Slovak locks, plus Czech and Polish accepted/rejected examples.
- Case and NFC/NFD query variants, surrounding whitespace, empty/one-character input, punctuation, and nonwords.
- Deterministic move fixtures comparing validity, reasons, scores, premium consumption, blanks, rack/bag state, and persisted payloads. Compare deterministic search outputs under a controlled clock so elapsed-time noise cannot hide a behavior change.

The analytical argument is stronger than a passing corpus alone: for all twelve current sets, normalized lexical length equals physical length, generated words contain only letters, forbidden sequences are absent, and both paths consult the same main index or Slovak list. This establishes equality for all valid formed words constructed from those sets.

### Exhaustive disagreement categories to cover

| Difference source | Required disposition |
|---|---|
| Two physical tiles but more than two lexical code points | Route by physical count. Test both directions of disagreement: allowlist-only and main-only membership. |
| Fewer than two physical tiles despite a longer lexical string | Reject as a formed word; retain the board’s minimum two-cell extraction rule. |
| Nonalphabetic characters inside valid declared tokens | Admit only through the declared-token dictionary predicate; prove L·L with a real temporary index. |
| Exact forbidden token sequence | Reject that complete sequence only. Do not reject another segmentation or a longer containing word. |
| `None` versus empty two-tile list | `None` uses main membership; an empty list rejects every physical two-tile word. |
| Whitespace, short input, or punctuation in string queries | Preserve the existing public query verdict; never treat string queries as placement evidence. |
| NFC/casefold expansion or a custom index normalizer | Test explicitly with synthetic indexes. Keep production normalization unchanged and never accent-fold A into Á. |
| Missing/mismatched tokens, coordinates, or lexical text | Reject malformed `WordFound` construction; never infer missing tokens from strings. |
| Search membership/prefix shortcuts | Use exact token authority for complete main/cross words and union prefixes only for exploration. Test that an allowlist-only multigraph word remains reachable. |

Every observed difference must be either a named synthetic correction above or a failure. **Any shipped formed-word verdict difference blocks A.** Public-query differences also block A.

### Existing inherited fixtures

The required multi-token condition is already represented by:

- `test_f1_two_multicodepoint_tokens_cross_the_wire_losslessly` — **SZ and DZS**, plus blank SZ.
- `test_hungarian_synthetic_draw_exchange_place_score_bingo_no_split` — **SZ and GY**.
- `test_p4_blank_realized_as_multicodepoint_keeps_blank_identity_and_scores_zero` — blank **CS**.

The L·L condition is already represented by:

- `test_interpunct_token_loads_places_scores_and_validates`.

These are existing tests, not newly established passing results. Strengthen them to use the required authority path.

The new end-to-end fixture uses a temporary synthetic variant with `A`, `Á`, `CS`, `SZ`, `DZS`, `L·L`, and `?`, a temporary dictionary, and explicit points/order. Patch only variant/asset resolution; do not mock validation, scoring, search, persistence, or transport.

It must cover drawing, exchange, duplicate rack entries, placement, crossing words, blank targets, scoring, premium reuse, seven-**tile** bingo counting, database reload, game-state wire projection, websocket refresh, AI context, and prompt construction. Include two different segmentations of the same lexical string to prove boundaries are preserved.

## 4. Gates and fresh independent acceptance

### Implementation gates

Before source changes, run the four inherited focused files and establish the differential oracle against the baseline. Do not run a redundant full baseline suite.

After **A**, run its focused parity, service, search, diagnostics, and multigraph tests, then these five backend gates:

```bash
poetry run ruff check .
poetry run mypy config game gamecore accounts catalog
poetry run python manage.py check
poetry run python manage.py makemigrations --check --dry-run
poetry run pytest -m "not internet"
```

The full backend suite is justified by changes to the cell representation and the authoritative path used by scoring moves, including simulation, endgame, diagnostics, and persistence.

After **B**, run its focused backend/frontend tests, then the backend gates again and all four frontend gates:

```bash
npm run typecheck
npm run lint
npm test
npm run build
```

B changes both backend context production and frontend consumption, so backend repetition and the frontend suite/build establish new evidence.

Use installed dependencies and isolated test databases. Disable dotenv loading for backend checks with the supported `PYTHON_DOTENV_DISABLED=1`; supply synthetic test settings. Run frontend gates in an isolated source snapshot containing no private env files. Do not install dependencies, contact providers, run catalog sync, or operate on the local game database.

### Independent-acceptance procedure

A **fresh separately launched session**, which implemented neither slice and is **not the Orchestrator’s subagent**, receives the exact A/B candidate identities and this plan.

1. **Gate identity and independence.** Verify the original baseline, AP pin, clean candidate state, sequential A→B ancestry, and the acceptor’s independence. Stop on divergence.
2. **Check each allowlist separately.** Compare baseline→A and A→B changed paths. Verify no changes to assets, manifests, dependencies, lockfiles, migrations, `.ap`, localization catalogs, or queued language work.
3. **Verify the oracle independently.** Read `_word_passes_dictionary` from the original baseline using `git show`; compare it with the frozen test oracle. Reject changed expectations or an oracle reconstructed from the new implementation.
4. **Inspect authoritative coverage.** Confirm the callable evaluator branch is gone; all five named calls, the human persisted-word loop, both searchers, and diagnostics use the same authority. Confirm the query compatibility method cannot authorize a scoring move.
5. **Inspect canonical cells.** Confirm dataclass storage contains token/assignment fields and no stored letter/blank flag. Check empty, ordinary, assigned-blank, clearing, and malformed-state cases.
6. **Check A independently.** In a disposable A checkout, run the focused parity, atomic-token, persistence, Slovak, and diagnostic tests. Inspect A’s recorded full backend gate results.
7. **Check B independently.** In a disposable B checkout, run the final focused fixtures and all backend/frontend gates listed above. The acceptor records their own command outputs.
8. **Verify transport and UI evidence.** Confirm distinct multigraphs occupy exactly one cell/rack entry each; blank CS stays physical `?` and scores zero; websocket and AI projections retain boundaries; anchors use physical coordinates; candidate text does not invent S/Z tiles. Verify full labels remain readable in narrow and desktop rendering using an authorized local browser. Missing browser capability is an evidence gap, not a passing visual check.
9. **Verify preservation.** Require zero unexplained shipped verdict differences, unchanged Slovak A/Á distinction and 103-entry list, unchanged seeded draw/search expectations, unchanged existing prompt bytes, and unchanged wire/store/save versions.
10. **Report acceptance separately.** PASS only when all required evidence is present. Findings return for one bounded correction; the acceptor does not fix its own findings. C1 and campaign closure remain Orchestrator decisions.

## 5. Limits, assumptions, and orchestration critique

**C1 does not make Hungarian or Croatian playable.** Both still need sourced tile distributions. Hungarian also needs a verified lexicon-generation solution: the stated `unmunch` limitation and unverified Spylls candidate remain separate work. C1 adds no language, asset, dependency, or slug branch.

The queued localization-shape problems, glossary rows, `hu.png`, and prompt lexicon literal unions remain outside both allowlists.

**What this exchange could not determine**

- Current full-suite health: running tests/builds was prohibited.
- Full-corpus verdict parity and deterministic move parity: this exchange measured all two-tile pairs and Slovak allowlist prefixes, not the complete implementation acceptance corpus.
- Actual browser fit of three-code-point labels: source rendering was inspected; no browser was used.
- Production deployment topology, live database contents, or private configuration: not inspected and not needed for this plan.
- The historical identities of all seven F2b guards: the external defect ledger was not read. The plan relies on current executable paths.
- The Hungarian/Croatian sourcing claims were supplied constraints; no network or external research was authorized.

**Orchestration critique**

**MEASURED**

- R1–R3 are correct but incomplete. The additional remainder includes diagnostic guards and the AI context/prompt/presentation chain.
- Five evaluator call sites do not cover persisted human word validation or search pruning.
- F1 uses SZ/DZS, not CS/SZ; the broader persistence file covers CS separately.
- The L·L canary currently bypasses service dictionary authority through an injected callable.
- Game-state wire version 4, save schema `"4"`, and localStorage version 6 are distinct formats.
- The cited AP line ranges for E3/independence are stale at the pinned revision. The governing E3 and fresh-acceptance provisions were located; no substantive conflict was found.

**LEAD**

- Existing multigraph labels may need visual sizing work; no clipping defect was measured. Do not expand production UI paths without evidence and renewed authority.
- A future language may require a lexical-contribution policy beyond identity token concatenation. C1 does not infer such rules.
- Production rollout sequencing must be established under separate deployment authority; the compatibility path above makes frontend-first rollout possible.
