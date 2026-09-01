
## 1. Repository and AP preflight evidence

Directly observed:

- HEAD: `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd`
- Subject: `fix(ui): explain the starting draw and localize it`
- Repository `.ap` gitlink and submodule HEAD both: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Branch status: `## main...origin/main`
- Public readback from `git ls-remote origin refs/heads/main` matches HEAD.
- The only working-tree changes are the ten expected untracked files:
  `cs.png`, `cz.jpeg`, `en.jpeg`, `en.png`, `hu.jpeg`, `hu.png`, `pl.jpeg`, `pl.png`, `sk.jpeg`, `sk.png`.
- Mandatory root, frontend, AP Worker, prompt-contract, and INFOSEC instructions were read. No repository instruction conflicted with the authoritative prompt.
- No file, database, dependency, provider, test suite, or build was mutated or executed.

The consumer-declared sanitized interpreter route applies to future implementation validation only. It was not used during planning. Ambient `python`, `python3`, and `poetry run` remain prohibited as canonical routes.

## 2. Impact matrix

| Classification | Surfaces | Planning conclusion |
|---|---|---|
| Must change | `variant_store.py`, variant manifests | Remove one-code-point and `isalpha` assumptions; add explicit alphabet order, readiness, two-tile authority, canonical token validation, and optional physical-sequence rules. |
| Must change | `types.py`, `board.py`, `legality.py`, `move_search.py`, `fastdict.py` | Preserve physical token boundaries, attach token sequences to formed words, centralize authority, count tiles rather than code points, and stop filtering lexical entries with `isalpha`. |
| Must change | `models.py`, `services.py`, `serializers.py`, `state.py`, game migrations | Replace joined board/bag/save representations; remove the separate blank-coordinate store; make all human and AI submissions use the same legality evaluator. |
| Must change | REST/websocket serializers and tests | Publish nested board cells and token arrays with schema version 4; retain the websocket envelope but change its state payload identically to REST. |
| Must change | `prompts.ts`, AI move route, stream parser, diagnostics, AI simulation | Accept exact variant tokens, use structured board/rack context, preserve word token arrays, and remove code-point splitting from diagnostics and candidate rendering. |
| Must change | frontend types/store/game board/blank picker/draw/Settings/Play | Replace row strings with `BoardCell[][]`, generalize variant preference to a string slug, dynamically discover readiness, and render multi-codepoint labels as one tile. |
| Already token-safe | `TileBag`, rack lists, DnD rack indices, connectivity/gap rules | These already operate on list items or board coordinates. Preserve their structure and update only misleading names/types. |
| Already token-safe | Scoring coordinate loop, premium consumption, bingo placement count, endgame rack length | One coordinate is already scored once and one placement already counts once. Ensure point lookup uses the physical token and blank score remains zero. |
| Needs proof | Dictionary/prefix lookup | Lexical lookup can remain string-based only after callers also preserve token sequences and the prefix index includes two-tile authority entries. |
| Needs proof | MOVE CORE pin and provider boundary | The English CORE bytes, SHA, version, one route, provider registry, search defaults, and six terminal sources need explicit unchanged regression tests. |
| Unrelated | Account/catalog field lengths, authentication tokens, provider logging limits, UI animation-array lengths | These matches are resource or domain constraints, not tile-count assumptions. |
| Unrelated | Seed-prompt migrations and Slovak lexicon build tooling | Historical prompt text and dictionary-acquisition tooling are outside this implementation; do not mechanically rewrite them. |

Exact negative searches found no existing `/api/game/variants/` route, no REST state schema-version field, and no existing physical token-sequence or lexical/display extension contract.

## 3. Confirmed one-character assumptions and token-safe components

Confirmed defects include:

- Multi-character tokens are silently discarded by the variant loader.
- Declared distribution order is discarded and code-point sorting becomes implicit game order.
- Board rows, bags, racks in save files, and AI racks are concatenated.
- Bag reload splits by character and `bag_remaining` counts serialized characters.
- Formed-word and search completion logic use lexical-string length as tile count.
- Request and Next.js schemas require one Unicode letter.
- Blank fallback alphabets are hardcoded A–Z.
- The store hardcodes an English/Slovak union.
- Diagnostics and the 300-turn frontend simulation reproduce flat-string assumptions.
- `AIThinkingOverlay` splits candidate words by code point.
- Ranked leave quality hardcodes `AEIOU`.

Preserve rather than rewrite:

- Bag and rack lists, rack multiset removal, exchanges, DnD indices, coordinate scans, connectivity, gap detection, premium use, seven-placement bingo logic, and final rack scoring.
- Exact-string tile-point maps and the existing `Tile` component’s ability to render a whole string.
- Text-based dictionary membership and bisect prefix lookup, once detached from physical tile counting.

## 4. Four-concept semantic contract

A. **Atomic tile token**

- Introduce `TileToken = str`.
- One token is one physical bag entry, rack entry, placement, or board cell.
- Canonicalization is `trim → NFC → uppercase → NFC`; runtime input must then match an exact variant token.
- Asset tokens must already be canonical, nonempty, unique, contain no whitespace/control characters, and use no more than 16 Unicode code points. That maximum is a resource bound, never a tile-count rule.
- `?` is reserved exclusively for a physical blank.

B. **Lexical contribution**

- For this cut, every nonblank token contributes its token string, and a blank contributes its `blank_as` target.
- Do not introduce per-tile rich objects or maps yet.
- Add named `VariantDefinition.lexical_contribution(token)` and `tile_display(token)` extension methods, both identity mappings now. Future display or lexical mappings can change behind those interfaces without changing containers.

C. **Container structure**

- Ordered token sequences are always arrays/tuples.
- Empty board cells are `null`; occupied cells are structured objects.
- No persistence, API, websocket, AI context, or save-state path may concatenate tokens and later reverse-tokenize them.

D. **Code-point length**

- Python `len(str)` and JavaScript string length may be used only for normalization/resource limits.
- Physical tile count is always the length of a token container, placement list, or formed-word coordinate/token sequence.

## 5. Selected architecture and rejected alternatives

Selected architecture:

- `Cell` stores `token: TileToken | None` and `blank_as: TileToken | None`.
- A regular cell has `{token: "SZ", blank_as: null}`. A blank representing `CS` has `{token: "?", blank_as: "CS"}`.
- `Cell.realized_token` resolves blank assignment while preserving physical blank identity.
- `WordFound` carries lexical `word`, realized `tokens`, and coordinates. Its physical length is `len(tokens)`.
- Add a pure `gamecore.word_authority` abstraction responsible for normalized dictionary membership, two-tile authority, prefix checks, and optional forbidden physical sequences.
- `evaluate_scoring_move` becomes the sole authoritative legality path for both human and AI submissions.
- Keep the public placement key `letter` because the pinned MOVE CORE uses it. Document it as a legacy wire name containing one atomic token; do not duplicate the schema with a new `token` placement key.
- Variant JSON gains an explicit `alphabet` whose set must equal all nonblank distribution tokens. `playable_letters` returns this order.
- Optional `forbidden_token_sequences: list[list[TileToken]]` is checked against complete formed words. It defaults empty; no Hungarian prohibition is inferred.

Rejected alternatives:

- Flat strings plus longest-match parsing: segmentation is ambiguous and already corrupts bags.
- Grapheme-cluster segmentation: it does not encode game-defined Hungarian digraph tiles.
- Rich token objects everywhere now: no current production variant separates identifier, lexical contribution, and display.
- Locale collation: starting order is a game rule and belongs in variant data.
- Hungarian conditionals: they would prevent future data-only variants.
- A legacy decoder: explicitly unnecessary because game state is expendable.
- Generic substring rejection: it violates the formed-word invariant.
- Language-specific vowel metadata: unsupported complexity for a secondary ranking heuristic; use variant-neutral leave ranking instead.

## 6. Short-word authority decision

Rename the concept everywhere:

- Manifest key: `two_tile_words_file`
- Loader: `load_two_tile_words`
- Existing asset: `slovak_two_tile_words.txt`
- New assets: `czech_two_tile_words.txt`, `polish_two_tile_words.txt`, `hungarian_two_tile_words.txt`

The existing Slovak key and file are migrated atomically with no legacy alias.

Semantic rule:

> For each complete formed word independently, if its physical token count is exactly two, validity is determined by exact normalized lexical membership in the variant’s two-tile authority set. Longer formed words use the main dictionary even if their spelling contains a rejected short string.

Consequences:

- `OSAMENIU` is never rejected because it contains `AM`.
- `Á` + `CS` has two physical tiles despite three code points and therefore uses the two-tile set.
- No scan of lexical substrings or arbitrary board pairs is permitted.
- Optional forbidden physical sequences are a separate rule and inspect preserved token sequences, not lexical substrings.

The main dictionary and prefix index remain normalized-text indexes. Prefix probes use the union of main-dictionary prefixes and all prefixes of two-tile authority words, allowing `ÁCS` to be found without reverse segmentation.

The free-text `validate-words` endpoint remains advisory lexical validation: it checks the main dictionary or exact two-tile asset membership but does not claim a physical classification without a token sequence. Persisted moves always use `WordAuthority.accepts(WordFound)`.

## 7. Persistence, migration, and save-state strategy

Create two migrations after current game leaf `0007`:

1. **`0008_purge_legacy_game_state`**
   - Irreversible `RunPython`.
   - Read a new fail-closed setting `ALLOW_DESTRUCTIVE_GAME_STATE_RESET`, default `false`, documented in `backend/.env.example`.
   - If all named tables are empty, return without requiring the flag.
   - If any row exists and the flag is false, raise before deletion.
   - With explicit opt-in, delete through historical models in this exact order:
     1. `game_chat_message`
     2. `game_move`
     3. `game_player_slot`
     4. `game_session`
     5. `game_consumed_ws_ticket`
   - Record pre/post counts and assert all five are empty.
   - Never touch accounts, JWT blacklist, `catalog_ai_model`, or `catalog_ai_prompt`.
   - Reverse raises `IrreversibleError`.

2. **`0009_atomic_token_state_schema`**
   - Remove `GameSession.blanks`.
   - Remove the text `bag_tiles` field and add `bag_tiles` back as `JSONField(default=list)`; this avoids database-specific text-to-JSON casts.
   - Update `board_state` documentation/default to a 15×15 structured grid.
   - Update rack, placement, and formed-word help text.
   - Structurally reversible only while game tables remain empty.

Canonical DB writes:

- `board_state`: 15×15 `BoardCell | null`
- `bag_tiles`: ordered `string[]`
- `PlayerSlot.rack`: ordered `string[]`
- Move placements retain `{row,col,letter,blank_as}`.
- Move words become `{word,tokens,coords,score,multiplier}`.
- `bag_remaining = len(session.bag_tiles)`.

Save-state becomes schema `"4"` with structured grid, rack arrays, and bag array. Restore accepts only schema 4 and rejects older/missing versions clearly.

Production would require separate production authority, a verified backup and restore rehearsal, a maintenance window, exact pre/post counts, and explicit opt-in. If production game retention were required, a separate non-destructive transform would replace this purge; development consent does not authorize production deletion.

## 8. Migration matrix

| Surface | Legacy | Proposed | Existing-row action | New write | Proof |
|---|---|---|---|---|---|
| Board DB | 15 strings plus `blanks` | 15×15 `BoardCell|null` | Sessions deleted; `blanks` removed | Structured cells | Migration and DB reload with `SZ` and blank→`CS` |
| Bag DB | Joined `TextField` | `JSONField` token array | Sessions deleted; remove/add field | Ordered token array | `SZ` remains one entry and count |
| Player rack | JSON token array | Same | Player slots deleted | Ordered token array | Draw/exchange/reload |
| Move history | Placements plus lexical words | Placements plus lexical word and token array | Moves deleted | Boundary-preserving words | History REST round trip |
| Save grid | Row strings plus blanks | Structured cell grid | Old saves rejected | Schema `"4"` | Save/restore with two multi-token cells |
| Save rack | Joined strings | Token arrays | Old saves rejected | Arrays | Duplicate and blank round trip |
| Save bag | Joined string | Token array | Old saves rejected | Array | No greedy parsing |
| REST state | `board:string[]`, `blanks` | Version 4 structured board | No old game compatibility | Canonical shape | API contract test |
| Websocket state | Same state under envelope | Same v4 state as REST | No old game compatibility | Canonical shape | Initial and refresh frame tests |
| AI context | Row strings, joined rack | Structured board/rack plus alphabet | No compatibility required | Canonical arrays | Mocked route/context test |
| Frontend preferences | Persist v3, slug union | Persist v4, string slug | Django migration has no effect | Syntactic slug retained | Store migration and catalog reconciliation |

Store migration v4 keeps a nonempty syntactically valid slug, resets malformed values to `"english"`, and never decides availability locally. After a successful catalog fetch, stale or unavailable slugs reconcile to the endpoint’s first playable row and are persisted. If no playable row exists or the fetch fails, game creation is blocked rather than silently redirected.

## 9. REST and websocket decision

Canonical wire type:

```text
BoardCell = null | { token: string, blank_as: string | null }
board = BoardCell[15][15]
```

- Add numeric `state_schema_version: 4` to REST and websocket game state.
- Remove `blanks`; blank identity is inside each board cell.
- Add `variant_display_name`, ordered `alphabet`, `blank_tile_count`, and exact `tile_points`.
- Add `tokens: string[]` to each formed-word payload.
- Preserve placement key `letter` for request and move-history compatibility.
- Placement and exchange validators canonicalize bounded strings, reject unknown fields, and rely on the session variant for exact membership.
- Known-but-unready variants return `variant_unavailable`; unknown slugs return `unknown_variant`.
- REST and websocket use the same `_build_state`; websocket event names/envelopes remain unchanged.
- No mixed state-version reader is introduced.

## 10. Frontend state and rendering decision

- Define `BoardCell` and change `GameState.board` to `BoardCell[][]`; remove `blanks`.
- Change `SelectedVariantSlug` to `string` and persist version to 4.
- Board rendering indexes nested arrays, uses `blank_as` as the visible token for blanks, and never indexes token strings.
- Pending placements remain coordinate/rack-index objects with the legacy `letter` field.
- `Tile`, draw tiles, `MiniTile`, and blank-picker buttons render the whole token in one DOM tile. Add adaptive typography classes for one, two, and three-or-more code points without splitting graphemes.
- `isPlausibleRack` requires server alphabet and `blank_tile_count`; remove the Unicode-one-letter fallback and hardcoded two-blank rule.
- BlankPicker uses only the ordered session alphabet. If absent, it fails closed instead of falling back to A–Z.
- Starting-draw UI displays whole tokens and trusts server `human_first`; it performs no local ordering.
- Candidate UI consumes backend `wordTokens`; it does not call `split("")`.
- DnD, exchanges, bingo indicators, and rack counts continue using array indices.
- Settings and Play consume variant display names from the catalog. Interface translations and flag assets remain outside this whole.

## 11. AI tool schema and AI context decision

Lock handling:

- **Lock A:** no provider registry, runtime constructor, catalog tuple, or provider documentation changes.
- **Lock B:** keep one `moveSystemPromptFor`, one SSE route, `MOVE_PROMPT_VERSION = "pfr-s2-core-1"`, and English CORE SHA-256 `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`.
- **Lock C:** leave 2000 ms witness and 750 ms ranked defaults unchanged.
- **Lock D:** retain exactly the six current completion sources.

The pinned system CORE text need not change:

- Its 15-character board description remains true for a 15-character occupancy grid using `.` and `#`.
- Atomic-token semantics are added to the structured user context and route-local tool description.
- Variant prompt examples and authority labels become strictly validated manifest data passed through the existing parameterized factory.
- English prompt bytes and version remain pinned; tests prove the hash.

AI context:

- Backend returns `ai_state.board: BoardCell[][]`, `ai_rack: string[]`, scores, alphabet, points, and bounded move/judge prompt specs.
- Next.js renders 15 fixed-width occupancy rows plus a sparse exact map such as `(07,08)=SZ` or `(08,08)=?→CS`.
- Rack and token alphabet are rendered as explicit JSON/space-delimited token lists.
- This preserves coordinates without repeating 225 potentially long labels.

Tool boundary:

- Construct Zod schemas only after trusted backend context is loaded.
- `letter` is an enum of `["?", ...alphabet]`; `blank_as` is an alphabet enum.
- A refinement requires `blank_as` only for `?`.
- Route normalization mirrors backend canonicalization and then checks exact set membership.
- Ranked, witness, repair, and exchange payload normalization uses arrays and never a one-letter regex.
- Backend final validation remains authoritative for all provider candidates.
- Candidate SSE events carry `word_tokens` and token arrays for all formed words.
- Unknown variant prompt specs fail closed; they never fall back to English.
- Judge lexical-length caps become named resource limits based on the 15-tile maximum, not assertions that a word has at most 15 code points.
- All AI tests use mocked generation/backend calls; no live provider probe is authorized.

## 12. Installed-variant discovery decision

Add public read-only `GET /api/game/variants/` returning only:

```text
{ slug, display_name, language_code, readiness }
```

where readiness is exactly `"playable"` or `"unavailable"`.

Implementation rules:

- Split structural manifest parsing from playable loading.
- A structurally valid manifest remains discoverable if a referenced dictionary or two-tile file is absent.
- A malformed manifest is omitted and logged.
- `playable` requires valid token metadata, alphabet-set equality, readable referenced resources, and complete bounded AI prompt metadata.
- File paths, filenames, dictionary contents, filesystem metadata, and readiness reasons are never returned.
- Canonical order is default `english` first, then stable display-name/slug order.
- Settings disables unavailable rows.
- Create and queue paths recheck readiness server-side and never fall back.
- The route is uncached or explicitly revalidated; the installed Next 16 route-handler documentation confirms GET handlers are not cached by default, but this endpoint is implemented in Django.

## 13. Czech, Polish, and Hungarian integration route

After the generic foundation:

- Add manifests at `backend/assets/variants/czech.json`, `polish.json`, and `hungarian.json`.
- Manually supplied dictionaries land as `backend/assets/dicts/czech.txt`, `polish.txt`, and `hungarian.txt`.
- Short authorities use the three `*_two_tile_words.txt` names.
- Every manifest supplies an owner-approved game alphabet independent of distribution order, plus the same bounded move/judge prompt-spec fields used by English and Slovak.
- Czech and Polish must activate without code changes, proving ordinary data integration.
- Hungarian metadata must load all seven multi-character kinds (`SZ`, `GY`, `NY`, `CS`, `LY`, `ZS`, `TY`), all nine copies, all 100 tiles, and both blanks.
- No rule forbidding `S` + `Z` is added for Hungarian without explicit evidence. The generic `forbidden_token_sequences` field remains empty.
- A manifest with missing dictionary or short authority appears unavailable, cannot create or queue a game, and never borrows English or Slovak resources.
- No dummy dictionary, download, scrape, UI translation, or flag-dropdown work is included.

## 14. Provenance and licensing gate for short-word assets

Before any short-word file enters a public commit, require:

- Source title, owner/publisher, authoritative URL, edition/version/date, and access date.
- License identifier or full license text proving redistribution and modification rights.
- Required attribution and notices in `<slug>_two_tile_words.LICENSE`.
- A `<slug>_two_tile_words.PROVENANCE.json` recording acquisition by the Cooperator, transformation/selection rules, UTF-8/NFC/case policy, original and normalized SHA-256, entry counts, duplicate/comment removals, and review date.
- A declaration that the file represents complete lexical words permitted when formed from exactly two physical tiles.
- Reviewer attestation that the content was supplied manually and was not scraped or synthesized by the Worker.
- Stop before commit if redistribution rights, origin, or derivation are unclear.

Full-dictionary acquisition remains outside scope, but activation likewise requires its independently supplied licensing evidence.

## 15. English and Slovak gameplay compatibility

- Preserve both 100-tile distributions, point values, dictionary identities, blank behavior, and rack/bag semantics.
- Rename the Slovak two-tile asset without changing its normalized contents.
- Add explicit English and Slovak game alphabets. The Slovak order fixes `uii-01-F07`; English ordering remains unchanged.
- English and Slovak words still have one token per code point, so the new physical rule produces their existing legality outcomes.
- Keep one-cell premium scoring, seven-placement bingo, rack-out, exchange, and six-scoreless-turn behavior.
- Replace the `AEIOU` imbalance component with variant-neutral point burden and duplicate-excess ranking. Legal results and deterministic ordering remain required, but exact legacy candidate preference is not treated as a contract.
- Preserve the English MOVE CORE hash/version and reproduce current English/Slovak prompt specs through manifest data.
- Preserve search defaults, completion-source values, provider tuples, and fallback behavior.
- Deleted games and old save states are intentionally not backward-compatible; gameplay code is.

## 16. Implementation slice order

### Slice F1 — token semantics and pure engine

- **Objective:** establish canonical tokens, explicit alphabets, word authority, physical word sequences, variant-neutral search, and save schema 4.
- **Paths:** `backend/gamecore/{variant_store,word_authority,types,board,legality,move_search,fastdict,scoring,state}.py`, English/Slovak manifests and short asset, related backend tests.
- **Schemas:** variant manifest contract, `Cell`, `WordFound`, `WordAuthority`, save schema `"4"`.
- **Tests:** loader negatives, L·L canary, Slovak short invariant, Hungarian synthetic engine/search/scoring, draw order, v4 save round trip, old-save rejection.
- **Focused command from `backend/`:**  
  `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_atomic_tile_tokens.py tests/test_gamecore.py tests/test_move_search.py tests/test_slovak_variant.py tests/test_slovak_engine.py tests/test_slovak_ranked_search.py`
- **Rollback:** revert code/assets; no DB effect.
- **Dependency:** none.
- **Negative scope:** no app persistence, frontend, provider, dictionary acquisition, or default-cap changes.

### Slice F2 — destructive cutover, DB, REST/websocket, and frontend state

- **Objective:** execute the guarded purge and make token arrays canonical end to end.
- **Paths:** game models/migrations/services/serializers/views/consumers; frontend types/API/store/game board/tile/blank/draw components.
- **Schemas:** migrations 0008/0009, REST/websocket v4, localStorage v4.
- **Tests:** destructive flag, protected-table preservation, empty no-op, schema rollback on empty DB, DB reload, REST/websocket parity, rack/exchange/endgame, frontend coordinates and rendering.
- **Focused commands:**  
  Backend: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_atomic_token_migration.py tests/test_api.py tests/test_multiplayer_ws.py tests/test_gamecore.py`  
  Frontend: `npx vitest run src/hooks/useGameStore.test.ts src/lib/rack.test.ts src/lib/draw-result.test.ts`
- **Rollback:** 0008 deletion cannot restore data; restore only from the preflight backup. On an empty database, reverse 0009 and revert code. Stop if post-cutover games exist.
- **Dependency:** F1 accepted.
- **Negative scope:** no accounts, JWT, catalog, deployment, or untracked image changes.

### Slice F3 — AI and diagnostics boundary

- **Objective:** make AI context, schemas, ranked candidates, SSE, diagnostics, and simulations token-aware while preserving all four locks.
- **Paths:** backend AI-context services and diagnostics; `prompts.ts`, AI move/judge routes, stream parser, overlay, diagnostic fixtures, 300-turn simulation.
- **Schemas:** structured AI context, validated manifest prompt specs, `word_tokens` SSE fields.
- **Tests:** exact MOVE hash/version, dynamic token enum, mocked `SZ`/`GY` candidate path, malformed/split candidate rejection, backend revalidation, diagnostic arrays, Hungarian causal simulation.
- **Focused commands:**  
  Backend: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/diagnostics tests/test_ai_play_engine_diagnostic.py tests/test_ai_play_turn_diagnostic.py`  
  Frontend: `npx vitest run src/lib/prompts.test.ts src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts src/lib/ai-move-stream.test.ts src/components/game/AIThinkingOverlay.test.ts src/lib/ai-turn-simulation.test.ts`
- **Rollback:** revert AI/diagnostic changes; F1/F2 token state remains valid.
- **Dependency:** F2.
- **Negative scope:** no live provider calls, provider files, prompt version bump, new completion source, or search-cap change.

### Slice F4 — readiness discovery

- **Objective:** expose the narrow catalog and remove frontend variant hardcoding.
- **Paths:** variant loader/catalog, game views/URLs/serializers, frontend API/store/Settings/Play.
- **Schemas:** four-field variant endpoint and playable/unavailable errors.
- **Tests:** absent-resource readiness, response redaction, stale preference reconciliation, unavailable selection disabled, server-side race rejection.
- **Focused commands:**  
  Backend: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_variant_catalog.py tests/test_api.py`  
  Frontend: `npx vitest run src/hooks/useGameStore.test.ts src/lib/api.test.ts`
- **Rollback:** revert endpoint/UI; existing English/Slovak game state remains valid.
- **Dependency:** F2; F3 before activating new AI-playable variants.
- **Negative scope:** no interface-locale or flag work.

### Slice A1 — Central European data activation

- **Objective:** activate Czech, Polish, and Hungarian only after all manual resource and provenance gates pass.
- **Paths:** three variant manifests, dictionaries, two-tile files, license/provenance companions, data-driven tests.
- **Schemas:** no executable schema changes.
- **Tests:** exact distributions/orders, readiness, lexical and two-tile authority, data-only Czech/Polish, full Hungarian acceptance fixture.
- **Focused command:**  
  `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_central_european_variants.py tests/test_atomic_tile_tokens.py tests/test_slovak_full_game.py`
- **Rollback:** revert activation assets; do not claim compatibility for games created under removed assets.
- **Dependency:** accepted foundation and manually supplied licensed resources.
- **Negative scope:** no downloading, scraping, translations, flags, deployment, or provider work.

At each coherent logical-whole candidate, run the complete canonical gates once:

Backend:

- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog`
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .`
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check`
- `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest`

Frontend:

- `npm run typecheck`
- `npx vitest run`
- `npm run lint`
- Run `ss -tlnp | grep :3000`; if any listener is reported, stop and do not build or kill it.
- Otherwise run `npm run build`.

## 17. Full test matrix

| Layer | Required evidence |
|---|---|
| Variant unit | Canonical NFC tokens; duplicates, noncanonical case, whitespace/control, `?` misuse, alphabet mismatch, bad counts, missing resources; L·L accepted as one non-`isalpha` token. |
| Word authority | `OSAMENIU` remains legal despite `AM`; complete rejected two-token word fails; `Á`+`CS` uses short authority; atomic `SZ` is distinct from `S`,`Z`; optional physical rule tested synthetically. |
| Engine | `SZ` and `GY` each draw, exchange, place, score, consume premiums, and remain single rack/board entries. Seven placements including them earn one bingo. |
| Search | Multi-token prefixes, blank targets, cross-checks, witness and ranked results; default 2000/750 ms constants unchanged; variant alphabet controls deterministic traversal. |
| Starting draw | Blank lowest, equal token gives slot 0 the tie, English unchanged, and Slovak `Á` beats `Z`. |
| Persistence/save | Structured cell with `SZ`; blank physical `?`→`CS`; ordered bag/racks; schema 4 round trip; schema 2/3 rejection; no reverse tokenization. |
| Migration | Nonempty+flag false aborts atomically; empty+false no-op; explicit opt-in deletes exactly five tables; accounts/JWT/catalog survive; 0009 forward/reverse tested empty. |
| API | Multi-token placement/exchange, token normalization, invalid/overlong/unavailable rejection, bag count, words with tokens, REST schema 4, human/AI parity. |
| Realtime | Initial and refresh websocket state equal REST shape and preserve `SZ`, `GY`, and blank assignment coordinates. |
| AI without provider | Dynamic schema accepts exact Hungarian tokens, rejects split or non-alphabet values, preserves sparse coordinates, emits token arrays, and revalidates through Django. |
| Frontend | One DOM tile per multi-token value, adaptive typography, zero-point blank, DnD/exchange by rack index, dynamic blank picker, store v4, unavailable catalog handling. |
| Regression | English and Slovak full-game/search/dictionary suites; Slovak two-tile behavior; prompt hash/version; six completion sources; provider-registry tests. |
| Causal simulation | Existing 300-turn invariants plus a Hungarian fixture using at least `SZ` and `GY`; no false pass/exchange when a move exists. |
| Provenance | Machine tests verify referenced license/provenance companions and recorded normalized hashes/counts. |

The Hungarian acceptance fixture must prove all 100 tiles and nine multi-character copies load, two distinct multi-token kinds survive every persistence/wire/AI/frontend round trip, configured points and premiums apply once per cell, seven physical placements trigger bingo, and no round trip produces `S`+`Z`.

## 18. Ranked risk register

Evidence labels: D = directly observed; S = supplied by prompt; I = inference.

| Rank | Risk | Consequence | Mitigation | Evidence |
|---:|---|---|---|---|
| 1 | Destructive migration targets wrong DB/tables | Irrecoverable unrelated data loss | E4 separation, backup/count checkpoint, opt-in flag, historical named models, protected-table assertions | S/D |
| 2 | Token boundaries lost | Ambiguous or corrupt board/bag/rack state | Arrays and structured cells everywhere; no reverse tokenization | D |
| 3 | Short authority regresses to substring logic | Valid longer words rejected | Central `WordAuthority`, complete `WordFound` tests including `OSAMENIU` | S/D |
| 4 | Tile count still uses lexical length | `Á`+`CS`, bingo, and search fail | Carry tokens/coords and count containers only | D |
| 5 | AI normalization drops candidates | False no-move pass/exchange | Variant enum, token arrays, mocked route test, final Django validation | D |
| 6 | Frontend coordinate drift | Tiles render in wrong cells | 15×15 nested arrays and sparse AI coordinate map | D/I |
| 7 | Bag/rack count corruption | Incorrect draws and endgame | JSON arrays and `len(array)` only | D |
| 8 | Blank physical identity lost | Wrong points/history/round trip | `{token:"?",blank_as}` in cell and word tokens | D |
| 9 | Python/JavaScript normalization differs | Valid token rejected at one boundary | Shared documented canonical order and cross-language fixtures | I |
| 10 | Physical digraph composition rule omitted or invented | Language rules silently wrong | Optional data rule, central enforcement, Hungarian default empty | S |
| 11 | Incomplete variant appears playable | Game creation fails after selection | Computed readiness and server-side recheck | S/D |
| 12 | English/Slovak behavior regresses | Shipped gameplay breaks | Full regression suites, explicit alphabet assets, pinned prompt | D |
| 13 | Prompt remains ambiguous for small models | Model proposes split tokens | Explicit atomic-token list, dynamic enums, examples, sparse map | I |
| 14 | Asset license is insufficient | Public redistribution exposure | Mandatory license/provenance gate and hashes | S |
| 15 | Overengineering | Unreviewable Unicode/plugin framework | Identity lexical/display methods only; no grapheme, RTL, CJK, or plugin framework | S |

Persisted legacy-game corruption is retired by the authorized purge; wrong-database or over-broad deletion remains the governing risk.

## 19. Recommended acceptance route

- Classify the destructive, irreversible data migration as **E4**, despite the expendable development data.
- Use strict stage separation: fresh preflight and backup/count evidence; bounded implementation; explicit migration execution on the named development database; implementation report; then fresh independent acceptance.
- INFOSEC route: inline **R1** validation checks during implementation and a fresh **R4** application audit because the base R3 AI/provider-boundary change is combined with an irreversible migration. The audit may remain static/synthetic and must not call providers.
- Audit focus: destructive-table containment, request normalization, malformed/oversized values, model-output validation, prompt-context injection boundaries, egress/provider files remaining unchanged, and secret/logging containment.
- A material correction to the provider boundary requires an **R6** correction plus fresh independent re-audit loop.
- Fresh independent acceptance is mandatory because persistence, migrations, wire format, request validation, core legality, and AI tool invocation all change.
- The Cooperator should separately render-check single-letter, `SZ`, `GY`, `L·L`, and blank→`CS` tiles on board, rack, draw, blank picker, and AI candidate surfaces.
- No live provider, deployment, production, or publication action is part of this acceptance plan.

## 20. Logical-whole split

Split sequentially:

1. `atomic-tile-token-foundation`
2. `czech-polish-hungarian-variant-activation`

The first owns the generic engine, migration, wire, AI, frontend, readiness, English/Slovak conversion, and synthetic canaries. The second is blocked only on manually supplied dictionaries, short authorities, official alphabet approval, and provenance. This boundary reduces migration review size, permits independent foundation acceptance, and proves production variants are data-only.

## 21. Material decisions required before implementation

1. **Should the Orchestrator adopt the two-whole split above?**  
   Recommendation: yes; authorize only `atomic-tile-token-foundation` first.

2. **Should the one-time development purge use `ALLOW_DESTRUCTIVE_GAME_STATE_RESET=false` by default and abort on nonempty game tables without explicit opt-in?**  
   Recommendation: yes; retain E4 separation and an irreversible migration.

3. **Should explicit official game alphabets and bounded move/judge prompt specs become required variant-manifest data?**  
   Recommendation: yes; the implementation prompt must supply or confirm the exact Czech, Polish, Hungarian, English, and Slovak orders.

4. **Should `two_letter_allowlist_file` be replaced without an alias by `two_tile_words_file`, including the Slovak filename rename?**  
   Recommendation: yes; the old name encodes the wrong semantics and no external plugin contract was found.

5. **Should physical composition use optional `forbidden_token_sequences`, empty for Hungarian until evidence says otherwise?**  
   Recommendation: yes; this locates the rule correctly without inventing Hungarian behavior.

6. **Should the `AEIOU` leave-imbalance term be removed instead of adding variant-specific vowel metadata?**  
   Recommendation: yes; preserve point burden and duplicate excess and accept deterministic ranking changes.

7. **Should Lock B remain closed, with atomic semantics confined to user context/tool schemas and no CORE byte or version change?**  
   Recommendation: yes; enforce the existing hash in acceptance.

8. **Should production activation remain blocked until all three dictionaries, short assets, alphabet orders, and redistribution evidence are present?**  
   Recommendation: yes; never use dummy or fallback resources.

## 22. Resolved Execution Issues / Near-Misses

- The first read-only lookup used an obsolete installed Next.js documentation path. Cause: Next 16 reorganized the local documentation tree. Resolution: the correct route-handler guide was found at `frontend/node_modules/next/dist/docs/01-app/01-getting-started/15-route-handlers.md` and inspected. Residual: none.
- A broad initial assumption search produced truncated output. Cause: too many repository-wide matches. Resolution: rerun as classified path-family searches and targeted source reads. Residual: none.
- The initial architecture temptation to treat the migration as E3 was rejected after reading the pinned E4 definition: irreversible destructive data is E4 even when bounded and development-only.

## 23. Pre-Existing Failure Classification

none

No implementation gates were run during planning, so no claim is made that the current suites pass. The ten untracked image files are authorized pre-existing state, not failures.

## 24. Smallest next step

The Orchestrator should approve the recommended decisions and issue a fresh-worker-session implementation grant scoped only to `atomic-tile-token-foundation`, with E4 preflight requirements and no production-variant assets or live provider calls. The first implementation action must be the read-only destructive-migration preflight, not migration execution.

## 25. Authority-expiry statement

This terminal planning report consumes the authorized initial planning cycle. All Worker planning authority for session 01, exchange 02 expires now. It grants no implementation, migration, database, Git, provider, deployment, acceptance, publication, or logical-whole closure authority.

