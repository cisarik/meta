Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-playable-variant
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice 1 of 4 (engine / lexicon / alphabet / scoring)
Task identity: slice1-per-variant-engine
Task type: feature implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: d34d8b38afa0d1538eb55827554326c6b4588dba
Implementation boundaries: this prompt
Independence required: no

Planning owner: ORCHESTRATOR
Accepted plan: `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/01_report_01.md` Slice 1 contract
Prior result: Slice 0 implementation-PASS at `d34d8b38afa0d1538eb55827554326c6b4588dba` (report `02_report_00.md`). Orchestrator reconciled: 9 allowlist paths, Collins 279497 unchanged, slovak.txt 3_005_250 unique, SSS 100, no CH tile.
Combined implementation envelope: prohibited — implement exactly Slice 1. Do not start Settings/UI or prompts.

Recommended reasoning: High
Recommendation basis: dictionary authority + witness/ranked search + scoring must stay English-correct while becoming Unicode/variant-aware. A leftover `isascii` or global Collins cache would make every Slovak word invalid again.
Escalation or downgrade gate: English tests red; new mypy errors vs 63/17; unkeyed global dict remains; you would need a frontend file.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: d34d8b38afa0d1538eb55827554326c6b4588dba
Baseline subject: feat(variant): add SSS Slovak tile set and hunspell-sk lexicon
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

================================================================
GOAL
================================================================

Make the backend variant-aware so a Slovak session can validate, score, and witness-search using `slovak.txt` and the SSS alphabet — without changing English Collins behavior or any frontend.

After this commit:
- `_word_passes_dictionary` has no `isascii`. English `qi`/`za`/`fe` still pass; `qlet` still fails.
- Dictionary cache is per resolved file path (fastdict already is). Services must not keep an unkeyed module-global Collins singleton as the only cache.
- `create_game` / `join_human_queue` reject unknown slugs with `{ok:false, error, code:"unknown_variant"}` before insert. QueueJoinView returns HTTP 400 when `ok` is false (CreateGameView already maps 400).
- `evaluate_scoring_move` and move search accept variant letters / blank alphabet / tile points. English default remains A–Z + Collins.
- `score_words` is called with `variant=session.variant_slug` (or bag slug) on live paths. Slovak `Á` scores 4, not 0.
- Board/placement ingest is NFC.
- `_build_state` and `get_ai_context` expose `tile_points`, `alphabet` (playable letters, no `?`), `lexicon_id` (`collins2019` | `slovak`).
- `validate_words` `source` is the stem of `dictionary_file`.
- Search node/time caps unchanged.
- Runtime UI still English-only; creating `variant_slug=slovak` via API is allowed and must work.

================================================================
CHANGED-PATH ALLOWLIST
================================================================

Existing:
- backend/game/services.py
- backend/game/serializers.py
- backend/game/views.py
- backend/gamecore/legality.py
- backend/gamecore/move_search.py
- backend/gamecore/scoring.py (only if a call-site type/default must change; prefer not rewriting the function body)
- backend/gamecore/game.py
- backend/gamecore/variant_store.py (`normalise_letter` NFC only)
- backend/tests/test_dictionary_validation.py
- backend/tests/test_move_search.py
- backend/tests/test_api.py
- backend/tests/test_slovak_variant.py (extend)
- backend/tests/test_gamecore.py (only if a tiny scoring/NFC unit is cleaner here)

New tests may live in `backend/tests/test_slovak_variant.py` or `backend/tests/test_slovak_engine.py` (if new, that path is allowed).

If any other path is required, stop BLOCKED.

================================================================
NEGATIVE AUTHORITY
================================================================

- No frontend.
- No `settings.py` / `PRIMARY_DICTIONARY_PATH` swap.
- No `fastdict.py` rewrite.
- No `tiles.py` / `state.py` / `board.py` / `types.py` unless you prove a one-line necessity — prefer NFC in services + `normalise_letter`.
- No `collins2019.txt` / `slovak.txt` / variant JSON edits.
- No catalog migrations, no prompts, no Settings persist.
- Do not edit `test_full_game_simulation.py`. Do not strip `isascii` from English-only helpers in `test_move_search.py` / `test_full_game_simulation.py`.
- Do not change search caps (`DEFAULT_MAX_NODES`, elapsed ms, ranked caps).
- No push. No second commit.
- Do not start Slice 2/3.

================================================================
MANDATORY READING
================================================================

- this prompt
- accepted Slice 1 contract in `01_report_01.md` (engine section)
- `backend/game/services.py`: `_get_prefix_index` `:100`, `_word_passes_dictionary` `:139`, `_board_from_session` `:148`, `_build_state` `:272`, `_probe_ai_playability` `:522`, `_probe_ai_ranked_candidates` `:624`, `_submit_move_locked` `score_words` `:747`, `create_game` `:904`, `join_human_queue` `:1162`, `evaluate_scoring_move` call sites `:703` / `:1439`, `validate_words` `:1469`, `get_ai_context` `:1390`
- `backend/gamecore/legality.py` `LETTERS` `:24`, `evaluate_scoring_move` `:100`–`:179`
- `backend/gamecore/move_search.py` `_BLANK_LETTERS` `:33`, `_plays` `:314`, `find_legal_scoring_move` / `find_ranked_scoring_moves`
- `backend/gamecore/game.py` `:135`
- `backend/game/views.py` `CreateGameView` `:59` vs `QueueJoinView` `:72` (always 200 today)
- `backend/game/serializers.py` `CreateGameSerializer` / `QueueJoinSerializer`
- `backend/tests/test_dictionary_validation.py`, `test_move_search.py`, `test_api.py` create/queue tests
- `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` implementation report

Do not read `.env` files.

================================================================
D1 — Per-path dictionary in services
================================================================

Replace the unkeyed globals.

Recommended shape:
- cache key = resolved `Path` of the variant's `dictionary_path` (string)
- `_get_prefix_index(session)` → `load_prefix_index(load_variant(session.variant_slug).dictionary_path)`
- `_get_dictionary(session)` / `_is_word(session, word)` use that index
- every current `_get_prefix_index()` / `_get_dictionary()` / `_is_word` call site must pass the session (playability, ranked, validate, submit, validate_words)

Do not change `PRIMARY_DICTIONARY_PATH`. English sessions resolve through `english.json` → `collins2019.txt` (same file the env default points at). That is the lock.

`validate_words` source = `Path(variant.dictionary_file).stem` (`collins2019` or `slovak`).

Loading `slovak.txt` (~3.0M words, ~43 MiB) on first Slovak request is an accepted residual. Do not add a new cache library.

================================================================
D2 — Unicode membership
================================================================

`_word_passes_dictionary`:
- NFC then casefold (or casefold then NFC — pick one and test both `škola` and a combining-mark equivalent)
- `len >= 2`
- `isalpha()` (Unicode)
- `contains(w)`
- NO `isascii`

English Collins tests must stay: `qi`/`za`/`fe` true, `qlet` false.

Slovak: a diacritic word in `slovak.txt` (e.g. `škola`) is true only when the contains fn is the Slovak index; it is false on Collins.

Short and non-alpha still false.

================================================================
D3 — Slug gate
================================================================

Installed slugs = `{v.slug for v in list_installed_variants()}`.

`create_game` and `join_human_queue`: if slug not installed, return
`{"ok": False, "error": "<brief>", "code": "unknown_variant"}`
BEFORE `GameSession.objects.create`.

Serializers: `validate_variant_slug` on both Create and QueueJoin (DRF ValidationError is also acceptable for unknown slugs; then also keep the service guard so internal callers cannot insert junk). Prefer one consistent API: HTTP 400 + `code` visible to the client.

`QueueJoinView.post`: `return Response(result, status=200 if result.get("ok", True) else 400)` — same pattern as CreateGameView.

================================================================
D4 — Legality + search + scoring thread the variant
================================================================

`evaluate_scoring_move(..., letters=None, variant=None)`:
- `letters` default `LETTERS` (English A–Z) so existing English tests need no alphabet argument
- when `letters` is provided (session playable letters as a frozenset), use it for letter + `blank_as` checks
- `score_words(..., variant=variant)` when variant is not None; English default stays `get_tile_points(None)` → english

`find_legal_scoring_move` / `find_ranked_scoring_moves` / `_Searcher` / `_RankedSearcher`:
- add `blank_letters` (default `_BLANK_LETTERS`) and `variant` (default None)
- `_plays` iterates `blank_letters`, not the module constant alone
- ranked already receives `tile_points=get_tile_points(session.variant_slug)` from services — keep that; also pass `variant` into `evaluate_scoring_move` inside the searcher so certification uses Slovak points/letters

Services probes and `evaluate_scoring_move` call sites must pass:
- `letters=frozenset(load_variant(session.variant_slug).playable_letters)`
- `variant=session.variant_slug`
- `blank_letters` = playable letters (41 for Slovak, 26 for English)

`game.py` `:135` → `score_words(..., variant=self.bag.variant_slug)`

`_submit_move_locked` `:747` → `score_words(..., variant=session.variant_slug)`

Search caps: do not change defaults.

================================================================
D5 — NFC ingest
================================================================

- `normalise_letter` in `variant_store.py`: NFC before upper (Slice 1 owns this; Slice 0 left it)
- `_placements_from_data`: NFC `letter` and `blank_as`
- `_board_from_session`: NFC each row string before indexing cells, so combining marks cannot expand a 15-cell row

Do not change Board storage format.

================================================================
D6 — Snapshot fields
================================================================

On `_build_state` and `get_ai_context`:
- `tile_points`: dict from `load_variant(session.variant_slug).tile_points`
- `alphabet`: list/tuple of `playable_letters`
- `lexicon_id`: stem of `dictionary_file`

Frontend is not wired yet; still add the keys so Slice 2/3 do not invent them.

================================================================
TESTS TO ADD
================================================================

English lock (keep/adjust existing, do not weaken):
- `qi`/`za`/`fe` pass, `qlet` fail
- existing move_search / api English games

New (names may be adjusted, assertions must exist):
- Slovak diacritic membership only on Slovak path
- non-alpha / len-1 rejected without `isascii`
- `POST /api/game/create/` `variant_slug=klingon` → 400 `unknown_variant`
- `POST /api/game/queue/join/` unknown slug → 400 `unknown_variant`
- `POST /api/game/create/` `variant_slug=slovak` → 201/ok; state has `variant_slug=slovak`, `lexicon_id=slovak`, `alphabet` includes `Á`, `tile_points.Á == 4`
- default create (no slug) still english + `lexicon_id=collins2019`
- `validate_words` on a Slovak game returns `source: slovak`
- witness/search: empty board + a rack that can play a Slovak lexicon word through center finds status `found` (use a tiny fixture rack you know is playable, e.g. letters of `AUTO` plus extras — `auto` is in slovak.txt)
- blank `?` assigned `Á` is not `invalid_blank` on Slovak letters
- `Á` placement scores > 0 with slovak variant
- combining-character letter NFC-equivalent is accepted as the composed letter

Do not mark the whole suite as requiring live network.

================================================================
VALIDATION
================================================================

cwd `backend/`:

```bash
poetry run pytest -m "not internet and not slow" -q
poetry run ruff check game gamecore tests/test_slovak_variant.py tests/test_slovak_engine.py tests/test_dictionary_validation.py tests/test_move_search.py tests/test_api.py tests/test_gamecore.py
poetry run mypy config game gamecore accounts catalog
```

mypy must stay **exactly 63 errors / 17 files** (or the current documented baseline if you re-count at HEAD and it is still 63/17). Zero NEW diagnostics. If mypy exits 1, run pytest separately afterward (known pattern).

================================================================
GIT
================================================================

Exactly ONE local commit on `main`.
Subject: `fix(engine): per-variant lexicon, alphabet, and scoring`
No push. Allowlist only.

================================================================
STOP
================================================================

- HEAD ≠ `d34d8b38afa0d1538eb55827554326c6b4588dba` or dirty foreign porcelain
- `./.ap/ap doctor` FAIL
- Plan Mode on
- English dictionary tests red
- `_word_passes_dictionary` still has `isascii`
- unkeyed `_prefix_index` global remains as the only cache
- `LETTERS` still the only alphabet in `evaluate_scoring_move` with no override
- `_submit_move_locked` still `score_words` without variant
- search caps changed
- new mypy errors
- frontend touched
- Collins or slovak asset files modified

================================================================
UNTRUSTED-CONTENT / NETWORK
================================================================

Governing: this prompt + pinned `.ap`. Zero provider HTTP. No JULS. No `.env`.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD `d34d8b38afa0d1538eb55827554326c6b4588dba`
- branch `main`
- porcelain empty
- `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `./.ap/ap doctor` PASS
- Native planning mode not-used

================================================================
REPORT
================================================================

Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Header exactly: ### Report for ORCHESTRATOR_CHAT

Echo once:
Logical whole identity: slovak-playable-variant
Worker session ordinal: 03
Worker exchange ordinal: 01

PASS only if D1–D6 + tests + one commit. Phase-qualified result: implementation-PASS.
Start commit `d34d8b38…`; end commit new SHA; changed files vs allowlist; pytest totals; mypy 63/17; ruff; deviations; next step = Orchestrator reconciles then issues Slice 2 to a FRESH Worker; justification `new-mutation`; authority-expiry; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification.

This report grants no Slice 2 authority.
