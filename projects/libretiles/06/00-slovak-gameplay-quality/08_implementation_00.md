Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice S only (Slovak ranked-search CLI fixtures)
Task identity: slice-s-slovak-ranked-search-cli
Task type: test implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: a80d4eb5f80715c31b95a3e38abfd1ac463c2af4
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: Slice S from accepted `05_report_00.md`. F+T are PASS at this baseline. Do not plan. Do not open Plan Mode. Do not implement L3 or V. Do not change production search caps.
Implementation in same Worker session: this IS the implementation session (fresh)
Execution authority event: this prompt (Native planning mode: not-used)
Combined implementation envelope: prohibited — Slice S only.

Continuity (evidence, not your authority):
- T commit `a80d4eb5f80715c31b95a3e38abfd1ac463c2af4` (Unicode rescue + generic-error ranked path)
- Planner measurements: SK empty `AUTOLIN` ranked `found`; blank rack may be `complete=False` at 750ms; still `found`. Do not change `DEFAULT_RANKED_MAX_ELAPSED_MS`.
- B2 is the Slovak two-letter lexicon; `ou`/`am` illegal; `um`/`mi` are in B2

Recommended reasoning: Medium
Recommendation basis: one new pytest file using existing engine APIs. Named risk is silently raising ranked caps to make a fixture green.
Escalation or downgrade gate: stop BLOCKED if `move_search.py` / `services.py` / `slovak.txt` / frontend seem required, if OU/AM would score, or if Plan Mode is on.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER
External trace disposition: not-used

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: a80d4eb5f80715c31b95a3e38abfd1ac463c2af4
Baseline subject: fix(ai): rescue and explain terminal stream failures
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
`origin/main` is behind (local ahead 2). Do not fetch. Do not push.

Canonical Python (RF-16): from `backend/`,

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python
```

Do not use ambient `python` / `python3` / `poetry run` as a parallel route. There is no `ap.project.conf`.

================================================================
GOAL (one primary outcome)
================================================================

Add **one** provider-free pytest module that proves Slovak ranked search:

1. Empty board, racks `AUTOLIN` and `?AUTOLI` → `status == "found"`, non-empty candidates, positive top score. Log `complete`, `nodes`, `elapsed_ms`, top word/score (`pytest -s`). Do **not** require `complete=True`.
2. Midgame: `AUTO` already on row 7 covering center; rack `ĽŤÁSENI` → `found` and at least one candidate with a diacritic placement. `placements_to_dicts` keeps it; every letter is one NFC Unicode letter or `?` with `blank_as` a Unicode letter (Python equivalent of JS `\p{L}`, not `/^[A-Z]$/`).
3. OU/AM traps: a legal B2 main `UM` whose cross is `OU` is `invalid_word` and score 0; same for main `MI` crossing `AM`. Ranked search on a board that offers those hooks never returns a candidate whose `words` include `OU` or `AM`.

Production `move_search` defaults and `_probe_ai_*` kwargs stay unchanged. Hunspell ≥3 junk remaining is L3, not this slice.

English CORE pin (frontend stay-green only): `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` / `pfr-s2-core-1`.

================================================================
CHANGED-PATH ALLOWLIST
================================================================

New:
- backend/tests/test_slovak_ranked_search.py

If `git add` would include any other path, stop BLOCKED.

================================================================
NEGATIVE AUTHORITY
================================================================

- No `move_search.py`, `services.py`, `fastdict.py`, dictionaries, variants, frontend, `test_strength_benchmark.py` helpers.
- No search-cap kwargs changes in production.
- No JULS, no live NIM, no `.env`, no push, no `git add .`.
- Do not rewrite `slovak.txt`. Do not add rejected-word quality exclusions (L3).
- Do not enable `LIBRETILES_RUN_STRENGTH_ACCEPTANCE`.

================================================================
REPAIR SHAPE
================================================================

Mirror `tests/test_slovak_engine.py`: module-scoped `load_prefix_index(load_variant("slovak").dictionary_path)`; `is_word` via `_word_passes_dictionary(..., two_letter_allowlist=load_two_letter_allowlist(variant))`.

`has_prefix`: True if `index.has_prefix(prefix)` else True if NFC-casefold prefix length 2 and in the B2 allowlist (same idea as `_prefix_checker`, without a `GameSession`).

Ranked calls:

```text
find_ranked_scoring_moves(
    board, rack, is_word, has_prefix,
    bag_count=100,
    tile_points=get_tile_points("slovak"),
    blank_letters=variant.playable_letters,
    variant="slovak",
)
```

Use default node/time caps. Print one metric line per ranked case (do not assert on elapsed).

**Unicode predicate** (test helper, do not import frontend):

- NFC + strip + upper
- letter `?` ⇒ `blank_as` present, NFC length 1, `isalpha()`
- else length 1 and `isalpha()`
- reject digits/emoji

**AUTO board:** place `A,U,T,O` on row 7 covering (7,7). Example: cols 5–8.

**OU trap (evaluate_scoring_move):** pre-place `O` at (6,7). Placements `U`(7,7), `M`(7,8). Rack `U,M`. `letters=frozenset(variant.playable_letters)`, `variant="slovak"`, `is_word` as above. Expect `reason_code == REASON_INVALID_WORD`, `total_score == 0`. Confirm `_word_passes_dictionary` UM True, OU False.

**AM trap:** pre-place `A` at (6,7). Placements `M`(7,7), `I`(7,8). MI True, AM False. Same invalid_word / score 0.

**Ranked exclusion:** on a board with that O-hook (and/or A-hook) and a rack that could form UM/OU if OU were legal (e.g. `U,M` plus fillers that do not force a production cap change), assert no ranked candidate `words` contains `OU` or `AM` (casefold). If ranked returns `found` with other words, that is fine. If this fixture cannot run without raising caps, **stop BLOCKED** — do not edit production.

`placements_to_dicts` lives in `gamecore/legality.py`.

pytest-django already sets `DJANGO_SETTINGS_MODULE` in `backend/pyproject.toml`. Do not add a settings hack if `test_slovak_engine.py` already imports `game.services` the same way.

================================================================
TESTS (required)
================================================================

Exact names from the plan (or these plus helpers):

- `test_empty_board_ranked_slovak_returns_found_with_and_without_blank`
- `test_midgame_ranked_slovak_returns_found_with_unicode_candidate`
- `test_slovak_ranked_search_rejects_ou_and_am_crosses_without_scoring`

Stay green:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_slovak_ranked_search.py -q -s
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py
```

Mypy: no **new** errors. Pre-existing 12 in 6 files (sessions 03–04) is allowed if the signature is unchanged.

```text
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts
```

Do not start Django/Next as a product server. Do not call providers.

================================================================
MANDATORY READING
================================================================

- this prompt
- `05_report_00.md` Slice S
- `backend/tests/test_slovak_engine.py` (fixtures, B2 `is_word`, empty-board witness)
- `backend/gamecore/move_search.py` `find_ranked_scoring_moves` signature
- `backend/gamecore/legality.py` `placements_to_dicts`, `REASON_INVALID_WORD`, `evaluate_scoring_move`
- `backend/game/services.py` `_word_passes_dictionary` / `_prefix_checker` (read, do not edit)
- `.ap/AP_WORKER.md` report header

Do not read `.env`. Do not read scrabgpt.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`

- HEAD equals `a80d4eb5f80715c31b95a3e38abfd1ac463c2af4`
- branch `main`
- porcelain empty
- `HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native planning mode **off** / absent

If any fails: **BLOCKED**.

Independently confirm `_word_passes_dictionary` rejects `ou`/`am` and accepts `um`/`mi` on Slovak before writing traps.

Capability handshake: abbreviated. Plan Mode off. Do not probe API keys.

================================================================
GIT
================================================================

One local commit. Stage only the new test file. No push. No amend.

Subject:

```text
test(engine): add Slovak ranked-search CLI fixtures
```

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure. Plan Mode on. Second path needed.
- Required rack/midgame not `found`.
- Unicode dicts fail `\p{L}`-equivalent check.
- OU/AM can score.
- English strength/search tests regress.
- Satisfying tests would require a production cap change.
- Live provider calls. L3 lexicon rewrite.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

**PASS** if: new tests green under `-s`; stay-green pytest + mypy (no new errors) + Vitest Unicode route; one local commit of only the new file; no push; no production cap change. Include the printed ranked metric lines in the report (summarize).

**BLOCKED** on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-partial` | `implementation-blocked`
Report justification: `new-mutation`
Logical-whole closure: `not-closed`

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo:
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 08
Worker exchange ordinal: 01

Then: status; phase result; start/end commit; paths; tests (including metric lines); commit; push not authorized; residuals (L3 still gated); smallest next step (Orchestrator: L3 remains blocked unless Cooperator supplies path+SHA-256+license or an approved filter spec; otherwise diagnostic-only live play is not V); expiry; closure not-closed; Near-Misses; Pre-Existing Failure Classification (mypy 12/6 if still present).

================================================================
AUTHORITY EXPIRY
================================================================

Expires with the terminal report. Retained context is not a renewal.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
Cooperator address (Orchestrator only): Slovak.
