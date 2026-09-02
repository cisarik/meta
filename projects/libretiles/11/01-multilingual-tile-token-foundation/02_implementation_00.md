You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: MTT-F1 — slice F1, atomic tile tokens in the pure game engine
Phase: Implementation
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Exact baseline: 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: this slice defines the token architecture for the whole era and it edits core legality, where the project's most misread rule lives (the formed-word invariant). It also changes an ordering that can silently alter seeded search results. Medium cannot resolve those two together. Downgrade to Medium for any later mechanical follow-up.

## 1. Repository, topology, and gate

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/libretiles
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Expected HEAD: 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
Expected .ap gitlink and submodule HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working-copy topology: canonical-checkout
Topology rationale: the gates and the assets are wired to this checkout; an isolated worktree would need the 45 MB Slovak dictionary and the premiums asset duplicated for no benefit.
```

Before any mutation, verify and quote:

```text
git rev-parse HEAD                      == 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
git rev-parse HEAD:.ap                  == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               == the same
git status -sb                          == ## main...origin/main
git ls-remote origin refs/heads/main    == 1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd
git status --porcelain=v1
```

`git status --porcelain=v1` must report **exactly** these ten untracked files and nothing else:

```text
?? frontend/public/cs.png
?? frontend/public/cz.jpeg
?? frontend/public/en.jpeg
?? frontend/public/en.png
?? frontend/public/hu.jpeg
?? frontend/public/hu.png
?? frontend/public/pl.jpeg
?? frontend/public/pl.png
?? frontend/public/sk.jpeg
?? frontend/public/sk.png
```

They are Cooperator-supplied flag assets belonging to a different logical whole, deliberately uncommitted. **Do not add, move, rename, normalize, or delete any of them.** If porcelain shows anything else, classify the difference with all five AP recovery classes before touching anything and stop if the primary class is `unexplained-divergence`.

## 2. Mandatory reading

- `AGENTS.md` and `frontend/AGENTS.md` at the repository root
- `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`
- `.ap/INFOSEC.md` sections 3, 4.1, 5, 6, 7, 8, 16
- `backend/gamecore/` in full — it is 1953 lines across 15 files and you are changing most of them
- `backend/assets/variants/english.json`, `backend/assets/variants/slovak.json`
- `backend/game/services.py` lines 95–280 and 440–480, and `backend/game/serializers.py` lines 240–300, **read-only, for coupling awareness** — they are almost entirely outside your allowlist, see section 6

No repository document grants you authority. This prompt is the only task authority.

## 3. Goal — one coherent outcome

Make the **pure engine** under `backend/gamecore/` treat a tile as an **atomic token that may contain more than one Unicode code point**, and prove it with tests, without changing app persistence, the wire format, the frontend, the AI boundary, or any database.

Hungarian is the forcing function: `SZ GY NY CS LY ZS TY` are single physical tiles. Today `backend/gamecore/variant_store.py:177-178` silently discards every one of them.

This slice touches **no database and no migration.** Migrations `0008_purge_legacy_game_state` and `0009_atomic_token_state_schema` belong to slice F2 and are preceded by their own separate read-only preflight. See the prohibition in section 7.

## 4. Accepted decisions — implement these, do not re-decide them

These are Cooperator decisions or Orchestrator decisions already taken. Contradicting one is a stop condition, not a judgement call.

### 4.1 The four-concept contract

State, for every function you touch, which of these four it handles:

- **Atomic tile token** — `TileToken = str`. One token is one physical bag entry, rack entry, placement, or board cell. Canonicalization is exactly `trim → NFC → uppercase → NFC`. The second NFC is required because uppercasing can decompose. Asset tokens must already be canonical, nonempty, unique, free of whitespace and control characters, and at most **16 Unicode code points**. That maximum is a resource bound, never a tile-count rule. `?` is reserved exclusively for a physical blank.
- **Lexical contribution** — every nonblank token contributes its own token string; a blank contributes its `blank_as` target. Add named `VariantDefinition.lexical_contribution(token)` and `VariantDefinition.tile_display(token)` as **identity** methods now. They are extension points, not behaviour. Do not build rich tile objects, per-tile maps, grapheme segmentation, RTL, or CJK support.
- **Container structure** — ordered token sequences are always lists or tuples. No code path may concatenate tokens and later reverse-tokenize them.
- **Code-point length** — `len(str)` is permitted **only** for normalization and resource limits. Physical tile count is always the length of a token container, a placement list, or a formed word's coordinate/token sequence.

### 4.2 `alphabet_order` is declared data, and `letters` is NOT the game order

This is the decision that keeps the slice small, and it comes from the Cooperator himself: `alphabet_order = jazykové poradie tokenov; letters = fyzické Scrabble tiles`.

- Add a **required** manifest key `alphabet_order`: a JSON array of tokens, duplicate-free, NFC, canonical. A manifest without it fails to load. Do not derive it from `letters`.
- **`VariantDefinition.letters` keeps its current construction order — `tuple(sorted(letters, key=lambda lt: lt.letter))` at `variant_store.py:193` stays exactly as it is.** `letters` feeds `distribution`, which is the pre-shuffle tile order consumed by `TileBag` at `backend/gamecore/tiles.py:39-42`. Changing it would change every seeded game in the repository and invalidate pinned expectations in at least `test_slovak_full_game.py`, `test_full_game_simulation.py`, and `test_endgame_policy_matrix.py`. Document `letters` in the source as an internal construction order with **no game meaning**.
- `playable_letters` changes: it returns the **tile tokens only** (blank excluded), ordered by their index in `alphabet_order`. This is the property that carries game meaning.

### 4.3 The alphabet invariant is a SUBSET, not set equality

The accepted planning report asked for set equality. **That is wrong and it would fail on the already-shipped Slovak variant.** Implement it in both directions:

```text
REQUIRED    every non-blank tile token MUST appear exactly once in alphabet_order
FORBIDDEN   requiring the reverse. A letter with no tile is normal and expected.
ALSO        alphabet_order must be duplicate-free, NFC, canonical, and declared rather than derived
```

Slovak has 46 order tokens and 41 non-blank tile kinds; `DZ`, `DŽ`, `CH`, `Q`, and `W` are Slovak alphabet letters that are not tiles in the SSS 100 set. English has 26 and 26.

Consequence you must implement: **blank targets come from the TILE SET ordered by alphabet index, never from `alphabet_order` itself.** Otherwise a Slovak player could assign a blank to `CH`, which is not a tile in that variant.

### 4.4 The authoritative alphabet orders, Cooperator-sourced and Orchestrator-validated

Use these verbatim. Do not reorder, extend, or "correct" them.

```text
english   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

slovak    A Á Ä B C Č D Ď DZ DŽ E É F G H CH I Í J K L Ĺ Ľ M N Ň O Ó Ô P Q R Ŕ
          S Š T Ť U Ú V W X Y Ý Z Ž
```

Sources: *Pravidlá slovenského pravopisu* (JÚĽŠ SAV), which states that `DZ`, `DŽ`, and `CH` are separate letters. Czech, Polish, and Hungarian orders exist and are **not** part of this slice.

Document in the source that `alphabet_order` is a deterministic total order for the **engine** — tile order, starting draw, blank picker — and is not a dictionary collation. Nobody may later reuse it as a universal word sorter.

### 4.5 Central word authority, and the formed-word invariant

Create `backend/gamecore/word_authority.py`: one pure abstraction owning normalized dictionary membership, two-tile authority, prefix probes, and optional forbidden physical sequences.

⛔ **The formed-word invariant is the single most misread rule in this project. Read this twice.**

```text
A move is illegal iff a COMPLETE formed dictionary-word produced by the placement has a PHYSICAL
LENGTH of exactly two tiles and is outside the variant's two-tile lexicon.
It is NEVER illegal because a LONGER formed word CONTAINS a two-letter string.
```

`OSAMENIU` is legal even though it contains `AM`. `ja`, `ty`, `my`, `si`, `to` are legal Slovak two-letter plays and the Cooperator wants them legal. If any line you write implies `"am" not in word`, scans the board for a letter pair, or enumerates pairs to reject a longer word, **you have failed the slice.** The only lawful shape is set membership over the list of complete formed words. Reference implementation of the correct shape: `backend/tests/test_slovak_ranked_search.py`, `_REJECTED_CROSSES` and `isdisjoint`.

The physical-length generalization is where this rule is easiest to break. Today `backend/game/services.py:209-222` `_word_passes_dictionary` keys the two-letter rule on **lexical code-point length** (`len(w) == 2`). That is a defect: a Hungarian `SZ`+`A` word is two physical tiles and three code points, and a Slovak-style `Á`+`CS` word is two tiles and three code points. Your authority must key on **physical token count**, which is `len(word.tokens)` and equals `len(word.letters)` — the coordinate list already counts tiles correctly at `backend/gamecore/board.py:89,96`.

Prefix probes must cover the **union** of main-dictionary prefixes and all prefixes of two-tile authority words, so a word like `ÁCS` is reachable with no reverse segmentation anywhere.

Optional `forbidden_token_sequences: list[list[TileToken]]`, checked against the token sequence of **complete** formed words only, defaulting to empty. **No prohibition is inferred for any language without evidence — Hungarian stays empty.**

### 4.6 `evaluate_scoring_move` gains the authority as an OPTIONAL parameter

`backend/gamecore/legality.py:100-108` currently takes `is_word: Callable[[str], bool]`. Add an optional `authority: WordAuthority | None = None`. When supplied it decides word legality over `WordFound` objects, including physical length. When absent, the existing `is_word` path behaves exactly as today.

Both `backend/game/services.py:30` and `backend/game/diagnostics.py:24` import and call this function and are outside your allowlist, so the existing signature must keep working unchanged. **F2 re-points them at the authority and deletes `_word_passes_dictionary`.** Record that removal obligation in your report so it cannot be lost. Do not leave a permanent second authority path.

Also fix `backend/gamecore/legality.py:24`: `LETTERS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")` is an ASCII default that is wrong for every non-English variant. Keep the default behaviour for callers that pass no `letters`, but make the reason it exists explicit in a comment.

### 4.7 `Cell` and `WordFound` change ADDITIVELY in this slice

`backend/game/services.py:238,240,817` and `backend/game/diagnostics.py:390` both **read and write** `Cell.letter` and `Cell.is_blank`, and mypy covers `backend/game/`. Restructuring `Cell`'s fields now would force this slice to rewrite the persistence paths, which is F2's entire objective.

So:

- `Cell` keeps `letter` and `is_blank` as its dataclass **fields**, unchanged and still writable.
- `Cell` gains **read-only derived properties**: `token` (`"?"` when `is_blank`, else `letter`), `blank_as` (`letter` when `is_blank`, else `None`), and `realized_token` (`letter`). These are the faithful mapping F2 will invert.
- `WordFound` gains `tokens: list[TileToken]` as a **third field with a default**, so the positional constructions at `board.py:91,98` keep working. Populate it with the realized token at each coordinate.
- Mark both additions in the source as a deliberate two-step whose second half is F2.

### 4.8 The two-tile rename, with no alias

Manifest key, loader, dataclass field, path property, and the shipped asset all rename together:

```text
manifest key        two_letter_allowlist_file   ->  two_tile_words_file
dataclass field     two_letter_allowlist_file   ->  two_tile_words_file
path property       two_letter_allowlist_path   ->  two_tile_words_path
loader function     load_two_letter_allowlist   ->  load_two_tile_words
shipped asset       backend/assets/dicts/slovak_two_letter.txt
                ->  backend/assets/dicts/slovak_two_tile_words.txt
```

No alias, no deprecation shim, no backward-compatible key. The old name encodes the wrong semantics.

Use `git mv` for the asset so Git records a rename, and **assert in a test that the normalized content is unchanged** — compute and report the SHA-256 of the file before and after. It is 586 B, 106 lines, 3 comment lines plus 103 entries, and it is the SSS Príloha B2 intersection filter. Its content must not change by one byte.

### 4.9 Optional variant `vowels`, defaulting to `"AEIOU"` — and deliberately NOT declared for Slovak

`backend/gamecore/move_search.py:536,540` hardcodes `"AEIOU"` inside ranked leave quality. Make it read an optional variant `vowels` field that **defaults to `"AEIOU"`**, threaded through the `variant: object = None` parameter that `find_ranked_scoring_moves` already accepts at line 110. No signature change.

⛔ **Do NOT add a `vowels` key to `slovak.json` or `english.json` in this slice.** This is deliberate, not an omission. The engine authors every move in this product — across a dozen counted live provider invocations the free LLM authored zero backend-valid placements and every completed live turn used `completion_source: backend_ranked_candidate`. The measured Slovak engine numbers (520–560 points per side, ~29 plies, all 17 single-copy diacritic tiles consumed) were produced under the current ranking. Changing shipped Slovak AI behaviour to fix a problem that only exists for new languages needs its own measured decision. Leaving en/sk on the default is what makes this change byte-identical for both shipped variants.

Prove the mechanism with a **synthetic** variant that declares `vowels`, and record the Slovak vowel misclassification as a named residual in your report.

### 4.10 Save state becomes schema `"4"`

`backend/gamecore/state.py:116` writes `schema_version="3"` and **nothing anywhere validates it** — there is no `get("schema_version")` read in the entire backend. `build_save_state_dict` and `restore_board_from_save` have **zero call sites**; only `build_ai_state_dict`, `restore_bag_from_save`, and `read_consecutive_scoreless_turns` are live. You are therefore adding a check that has never existed, and your tests are the only proof it works.

- `build_save_state_dict` writes `schema_version="4"` with a structured 15×15 cell grid, rack token arrays, and a bag token array. No joined strings.
- `restore_board_from_save` and `restore_bag_from_save` accept **only** schema `"4"` and reject `"2"`, `"3"`, absent, and malformed versions with a clear error. Drop the greedy longest-symbol bag parser at `state.py:165-186`; a token array needs no parsing.
- ⛔ **`build_ai_state_dict` keeps its current emitted shape byte-for-byte.** It is live at `backend/game/services.py:1529` and its structure is owned by slice F3. Changing it here breaks the AI boundary outside your allowlist.

### 4.11 The `isalpha` lexical filter must become injectable, with today's behaviour as the default

`backend/gamecore/fastdict.py:32` drops every dictionary line where `normalized.isalpha()` is false. `"L·L".isalpha()` is `False`, so the Catalan interpunct case is silently unplayable. That is the architecture counterexample this slice must survive.

Make the entry predicate injectable, **defaulting to exactly today's `isalpha()` behaviour** so the English and Slovak indexes stay byte-identical — `test_slovak_variant.py:18,73` pins the Collins line count at `279497` and it must not move.

⚠ `_INDEX_CACHE` at `fastdict.py:58` is keyed by `(resolved_path, normalize.__name__)`. If you add a predicate parameter without adding its identity to that cache key, two different predicates over one path will silently share an index. Include it, and test the collision.

### 4.12 A pure draw-order helper now; the wiring is F2

`uii-01-F07` is live in production today: `backend/game/services.py:453-464` decides who opens the board with `slot0_value <= slot1_value` on raw tile strings, so `('Á' <= 'Z')` is `False` — code points 193 versus 90. All seventeen single-copy Slovak diacritic tiles sort after `Z`, and a player who draws `Á` is treated as further from A than one who draws `Z`. In the Slovak alphabet `Á` is second.

`_perform_starting_draw(bag: TileBag)` has **no variant handle at all**, so the fix needs a signature change in `backend/game/services.py`, which is outside your allowlist.

Your job in F1 is the **pure** half: a variant-aware ordering key in `gamecore` — blank lowest, then tile tokens by `alphabet_order` index, ties resolved to slot 0 — with unit tests including `Á` beating `Z` in Slovak and English ordering unchanged. **F2 wires it into `_perform_starting_draw`.** Say so in your report; do not claim `uii-01-F07` is corrected.

Note the instructive asymmetry worth a source comment: naive code-point order happens to place the Hungarian **digraphs** correctly (`SZ` < `T`, `CS` < `D`, `GY` < `H`, `ZS` > `Z`) while being wrong for **every accented vowel** in all four non-English languages. A fix that only thinks about digraphs misses the real defect.

## 5. Positive authority — the exact changed-path allowlist

```text
backend/gamecore/word_authority.py            NEW FILE
backend/gamecore/variant_store.py
backend/gamecore/types.py
backend/gamecore/board.py
backend/gamecore/rules.py
backend/gamecore/legality.py
backend/gamecore/move_search.py
backend/gamecore/fastdict.py
backend/gamecore/scoring.py
backend/gamecore/state.py
backend/gamecore/tiles.py
backend/gamecore/game.py
backend/gamecore/rack.py

backend/assets/variants/english.json
backend/assets/variants/slovak.json
backend/assets/dicts/slovak_two_letter.txt  ->  backend/assets/dicts/slovak_two_tile_words.txt   (git mv, content unchanged)

backend/tests/test_atomic_tile_tokens.py      NEW FILE
backend/tests/test_slovak_variant.py
backend/tests/test_gamecore.py
backend/tests/test_move_search.py
backend/tests/test_dictionary_validation.py
backend/tests/test_slovak_engine.py
backend/tests/test_slovak_ranked_search.py
backend/tests/test_slovak_full_game.py
backend/tests/test_endgame_policy_matrix.py
backend/tests/test_full_game_simulation.py
backend/tests/test_strength_benchmark.py
backend/tests/test_ai_play_engine_diagnostic.py
```

Plus a **narrowly bounded** entry, granted only because decision 4.8 forbids an alias:

```text
backend/game/services.py       ONLY the import at line 52 and the two call sites at lines 128 and 138
backend/game/diagnostics.py    ONLY the import at line 31 and the call site at line 331
```

In those two files you may rename references to `load_two_letter_allowlist` and nothing else. Any other edit to them — one line, one character, one import reordering — is out of scope and must stop the slice with an escalation. State in your report exactly which lines you changed there.

## 6. Coupling you must be aware of and must NOT fix

Read these; leave them alone. They are F2's objective and knowing them stops you from "helpfully" widening the slice:

```text
backend/game/serializers.py:275   len(nfc) == 1 and nfc.isalpha() and nfc == nfc.upper()
                                  A multi-character tile is a 400 before it reaches the engine.
                                  Pinned by test_slovak_engine.py:206, which asserts "CH" is rejected.
                                  That assertion stays TRUE and must keep passing — CH is not a
                                  Slovak tile. Precision that matters: "SZ".isalpha() is True, so
                                  what blocks Hungarian is the len(nfc) == 1 half, not isalpha().
backend/game/services.py:228-236  _board_from_session indexes row[c] per code point
backend/game/services.py:263-272  _persist_board joins with "" — lossy for any digraph
backend/game/services.py:248      tiles=list(session.bag_tiles) — CHARACTER split
backend/game/services.py:372,558  bag_remaining = len(session.bag_tiles) — a COUNT from a string
                                  LENGTH. This is uii-01-F06. One SZ would store fine, restore as
                                  S + Z, and count as two tiles. BAG_EMPTY_AND_PLAYER_OUT reads it.
backend/game/services.py:167      "alphabet": list(variant.playable_letters) — a pure pass-through.
                                  Your reordering propagates here with zero source change, which is
                                  intended. No backend test asserts alphabet order.
backend/game/diagnostics.py:373-374, 789   further one-code-point and isalpha assumptions
```

## 7. Negative authority — prohibited without exception

```text
NO database work of any kind: no migration file, no model change, no manage.py migrate,
   no manage.py makemigrations, no DB write, no sqlite file touched.
   Migrations 0008 and 0009 belong to slice F2 and are preceded by their own read-only preflight.
NO change to backend/game/ beyond the five lines named in section 5.
NO change to backend/config/, backend/accounts/, backend/catalog/, backend/billing/.
NO change anywhere under frontend/. Not one file, including the ten untracked images.
NO new variant manifest. Czech, Polish, and Hungarian assets belong to slice A1 and are blocked on
   Cooperator-supplied dictionaries. Hungarian in this slice is a SYNTHETIC test fixture only.
NO dictionary acquisition, download, scraping, or synthesis. Ever.
NO dependency, lockfile, runtime, or toolchain change. Do not run pip, poetry add, or npm install.
NO change to README.md, AGENTS.md, or any documentation file.
NO deletion of backend/assets/dicts/sowpods.txt even though nothing references it.
NO live provider call, no network access except the one authorized git ls-remote and git push.
NO reading or printing of backend/.env or frontend/.env.local.
```

Four standing Cooperator locks. Breaking one is a stop condition:

```text
LOCK A  The nine AI providers are FROZEN. No change to any provider list, constant, tier, exact model
        tuple, or provider documentation, anywhere.
LOCK B  ONE parameterized MOVE CORE with pinned SHA-256
        c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60, version pfr-s2-core-1, and
        ONE SSE route. This slice touches no prompt file at all.
LOCK C  DEFAULT_MAX_ELAPSED_MS = 2000 at move_search.py:24 and DEFAULT_RANKED_MAX_ELAPSED_MS = 750 at
        move_search.py:28 are unchanged. ⚠ The 2000 constant is pinned by NO test — repo-wide it
        appears only at move_search.py:24 and :79 — so no gate would catch a change to it. Add the
        missing assertion (section 9, test 10).
LOCK D  Exactly six completion_source values. No seventh. This slice adds none.
```

## 8. Execution route — mandatory bounded deviation under RF-16

`AGENTS.md` documents backend commands as `poetry run ...`. **That declared route is not usable in this Worker boundary**: the Cursor AppImage environment intercepts `python*` through inherited `APPIMAGE` / `ARGV0` / `APPDIR` / `PYTHONHOME` variables. This is an explicit bounded deviation, not a parallel canonical route.

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md "Code quality"
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m <tool>
Rationale:                              inherited AppImage variables hijack the interpreter
Evidence class:                         reproduced-dynamic, established repeatedly in this project
Bounded authority:                      this task only; it never becomes a second canonical route
Stopping condition:                     if .venv/bin/python is absent or the deviation fails, STOP and
                                        report. Do not fall back to ambient python, python3, or
                                        poetry run, and do not repair the environment.
```

Never present ambient `python`, `python3`, or `poetry run` as an equivalent alternative anywhere in your report.

## 9. Validation

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the twelve backend test files named in section 5
Affected tests: same
New causal regression: required — see the ten items below
Broad or full suite: required-because the project's standing gate contract requires all eight gates at
  every commit, and this slice changes core legality
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one fresh independent R4
  application audit after slice F3
Evidence tier: E2
Evidence tier basis: multiple pure-engine layers, fully reversible, no database, no trust boundary, no
  credential, no provider, no production surface. The E4 classification of this logical whole attaches
  to F2's irreversible migration, not to F1.
Activated stricter profile: INFOSEC.md at R1 + R2
Combined implementation envelope: allowed — code, assets, tests, one commit, one non-force push
Terminal implementation report point: after the public readback
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
```

### The ten required new regression tests

For **every** one of these, supply a **pre-fix / post-fix table** with the exact pre-fix failure output. A test that passes before your change locks nothing, and the Orchestrator will check this.

1. **Loader positives and negatives** in `test_atomic_tile_tokens.py`: a multi-code-point token like `SZ` loads as one tile; whitespace, control characters, a non-canonical case, a duplicate token, a token over 16 code points, and a non-`?` token that tries to mean blank are each rejected with a distinguishable error. A manifest missing `alphabet_order` fails to load. An `alphabet_order` with a duplicate, or non-NFC, fails.
2. **The subset invariant in both directions**: a tile token absent from `alphabet_order` is rejected; a letter in `alphabet_order` with **no** tile is **accepted**. Prove it against real Slovak, where `DZ`, `DŽ`, `CH`, `Q`, `W` have no tiles.
3. **The `L·L` canary**: a synthetic variant with a three-code-point, non-`isalpha` token loads, places, scores, and validates. This test is what proves the implementation did not generalize only to `len(token) <= 2 && isalpha()`.
4. **The Slovak two-tile invariant**: `OSAMENIU` stays legal even though it contains `AM`; a complete two-token word outside the B2 set is rejected; and a synthetic physical-2 / lexical-3 word (the `Á`+`CS` shape) is routed to the two-tile authority and **not** to the main dictionary. Assert the routing, not just the verdict.
5. **Hungarian synthetic engine, search, and scoring**: `SZ` and `GY` each draw, exchange, place, score, consume a premium exactly once, and remain one rack entry and one board cell. Seven physical placements including them earn exactly one 50-point bingo. No round trip anywhere produces `S` + `Z`.
6. **Draw ordering**: blank lowest; Slovak `Á` beats `Z`; English ordering unchanged; two equal tokens give slot 0 the tie.
7. **Save schema 4**: a round trip preserving two multi-token cells, a blank realized as a two-code-point token, ordered racks, and an ordered bag; plus explicit rejection of schema `"2"`, `"3"`, absent, and malformed. Also assert that `build_ai_state_dict`'s emitted shape is **unchanged**.
8. **The seeded-bag promise**: a seeded `TileBag` for English and for Slovak produces the **identical** first twenty draws as at baseline `1b7b05d`. Capture the baseline values before you change anything. This test is what makes decision 4.2 verifiable instead of merely asserted.
9. **The two-tile asset rename**: the new filename resolves, the old one does not, the entry count is still 103, every entry is still two characters, and the normalized SHA-256 is identical to baseline. Report both hashes.
10. **The frozen search caps**: assert `DEFAULT_MAX_ELAPSED_MS == 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS == 750` explicitly. The second is already pinned at `test_move_search.py:369`; the first is pinned nowhere and this closes that hole.

### Expected churn you must disclose rather than silently absorb

Reordering `playable_letters` changes the **order** in which blank targets are enumerated, because `backend/game/services.py:623,721` pass `blank_letters=variant.playable_letters` into the searchers. For English nothing moves — code-point order and alphabet order are identical. For Slovak the enumeration order changes, so a ranked or witness candidate that previously won a tie may now lose it.

If any pinned expected value changes — a score, a candidate, a word choice — you must:

- report the exact pre and post values;
- state the causal reason;
- state whether the change is a **rule** difference (a defect) or a **tie-break / traversal-order** difference (expected);
- and never edit a pinned value without that disclosure.

Silently updating an expected number is how a real regression gets buried. A negative result here is an acceptable and useful outcome.

### The eight standing gates, all required at the commit

From `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

From `frontend/`:

```bash
npm run typecheck
npx vitest run
npm run lint
# THEN, and only after the port check below:
npm run build
```

Baseline at `1b7b05d`, Orchestrator-measured — **match or exceed every one**:

```text
mypy               Success: no issues found in 80 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             328 passed, 4 skipped in 189.67s
npm run typecheck  exit 0
npx vitest run     342 passed | 3 skipped   (26 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0, every route ƒ, Proxy registered, no deprecation warning
```

Four traps that have each cost a real session in this project:

1. `backend/pyproject.toml` sets `addopts = "-q"`. **Passing another `-q` silently suppresses the pytest summary count line.** Run plain `-m pytest` and quote the summary line verbatim.
2. Running mypy on a **narrowed** path set once hid 62 real errors behind a reported 12 for six consecutive Worker sessions. Always use the full documented scope above.
3. `npm run build` and `npm run dev` share `frontend/.next`. **Run `ss -tlnp | grep :3000` first. If any listener is reported, STOP and report — do not build and do not kill it.** ⛔ Never use a broad pattern kill such as `pkill -f next-server`; that pattern matches the Cooperator's own development server and a previous session survived doing it only by luck. Kill only by exact PID, and only a server you started.
4. `npm run build` can report success while type errors exist, because `tsconfig.json` sets `incremental: true`. **"The build passed" and "the code type-checks" are two separate claims. State both separately.**

The frontend gates must be run even though you change no frontend file: they prove you changed none.

## 10. Git authority

```text
Authorized:  git status, git diff, git log, git show, git rev-parse, git ls-remote,
             git mv (for the one asset rename only),
             git add <explicit paths>, git commit, one git push origin main
Forbidden:   git add -A, git add ., force push, amend, rebase, reset, revert, clean, stash,
             branch, tag, checkout of another ref, any remote or config modification
```

Sequence, in this exact order:

1. stage by **explicit path only** — every path you list must appear in section 5;
2. `git status --porcelain=v1` again and confirm the ten untracked flag images are still untracked and unstaged;
3. review the full staged diff before committing;
4. commit with subject `feat(engine): make tile tokens atomic in the pure game engine`;
5. pre-push gate: `git ls-remote origin refs/heads/main` **must still equal** `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd`. If it has advanced, another actor is active — **stop, push nothing, and report**;
6. one non-force `git push origin main`;
7. public readback: `git ls-remote origin refs/heads/main` compared with `git rev-parse HEAD`. Quote both.

## 11. Stopping conditions

Stop, preserve state, mutate nothing further, and report:

- any repository or baseline gate fails, or porcelain shows anything beyond the ten flag images;
- the work would require any path outside section 5, including the two narrowly bounded `backend/game/` files beyond their named lines;
- the work would require a migration, a model change, or any database access;
- any of the four locks would be touched;
- a gate regresses below the baseline and cannot be fixed inside this allowlist;
- port 3000 has a listener at build time;
- the pre-push `ls-remote` gate does not equal the baseline;
- the `.venv` execution route is unavailable;
- you find a pre-existing defect outside this allowlist — **record it, do not fix it**;
- the same failing gate survives one correction attempt with an unchanged hypothesis and candidate. Then report `PARTIAL` or `BLOCKED` with exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## 12. Report contract

Begin the report **exactly**:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once, unchanged: logical whole `multilingual-tile-token-foundation`, Worker session `02`, Worker exchange `01`.

Then include:

1. status: `PASS`, `PARTIAL`, or `BLOCKED`;
2. `Phase-qualified result: implementation-PASS` or `not-applicable`;
3. start and end commit;
4. every changed path with its purpose, and the exact lines changed in the two `backend/game/` files;
5. all eight gate results with the pytest and vitest summary lines quoted verbatim, and "the build passed" stated separately from "the code type-checks";
6. the **pre-fix / post-fix table** for all ten regression tests, with exact pre-fix failure output;
7. every changed pinned expectation with pre value, post value, causal reason, and rule-versus-tie-break classification — or an explicit `none`;
8. the two-tile asset SHA-256 before and after;
9. the F2 obligations you are handing forward: delete `_word_passes_dictionary`, re-point `evaluate_scoring_move` callers at the authority, invert the `Cell` storage and remove the derived properties, wire the draw-order helper into `_perform_starting_draw`, and correct `uii-01-F06`;
10. the Slovak vowel-classification residual from decision 4.9;
11. deviations, risks, and missing evidence — honestly, including anything you could not verify;
12. `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>`;
13. `Pre-Existing Failure Classification: none | <the complete contract record>`;
14. commit and push result with the public readback;
15. one smallest next step;
16. `Report justification: new-mutation`;
17. `Logical-whole closure: not-closed`;
18. an explicit authority-expiry statement.

⛔ You must **not** emit any logical-whole closure signal. Closure belongs to the Orchestrator alone. Your evidence is **non-independent** — say so.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
