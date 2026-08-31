### Report for ORCHESTRATOR_CHAT

Logical whole identity: slovak-playable-variant  
Worker session ordinal: 01  
Worker exchange ordinal: 02

**Status:** PASS  
**Phase-qualified result:** planning-complete  

**Start commit:** `30c4d30a97ba797ae77ec05c66187a6a6498279b`  
**End commit:** `30c4d30a97ba797ae77ec05c66187a6a6498279b` (no mutation)  
**Changed files:** none  
**Tests/validation:** inspection only (repository gate, file reads, unauthenticated hunspell/LibreOffice GETs, local `unmunch` probe under `/tmp`). No pytest/Vitest required this exchange.  
**Commit/push:** not authorized  

**Capability handshake (abbreviated):** Native Plan Mode on (directly observed). Provider keys not probed.

**Repository gate:** HEAD `30c4d30a97ba797ae77ec05c66187a6a6498279b`, branch `main`, porcelain empty, `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

**Planning Record:**  
Planning cycle: targeted-revision  
Prior planning report: `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/01_report_00.md`  
Targeted revision basis: newly-identified-material-risk  
Changed decision boundary: slice specification completeness and implementation-grant readiness only  
Preserved unaffected decisions: six locked forks; two-variant architecture; per-path dictionary cache; Settings-only game language; English Collins default; tool-only SSE unforked; live-play design counts; all non-goals  
Automatic targeted revisions used: 1

**Deviations / risks / missing evidence:**  
- `unmunch` stderr prints `parsing line:` for `.aff` comments; stdout is still a full expansion. Slice 0 must not treat that stderr as failure.  
- Expanded unique count on this host: **3_005_250** (raw 7_875_262). Shipped `slovak.txt` will be tens of MB; RAM/load is a residual, not a fork.  
- Exact SHA-256 of the four upstream files was measured against commit `75f5dff8c972fff4a32e4ea8434722c277f02a3f`; Slice 0 re-checks before commit.  
- `hramescrabble.sk` was not re-fetched this exchange (tile table already locked).  
- Catalog SEARCH_PROFILE rows may still mention Collins; no migration in this whole (CORE remains non-overridable).

---

## Full deepened plan body

### Locked decisions (do not reopen)

1. Tile set: official SSS 100. Not 112. Not historical ScrabGPT 108. No CH/DZ/DŽ tiles.  
2. Lexicon: hunspell-sk / LibreOffice `sk_SK` expanded list → `backend/assets/dicts/slovak.txt` + license notice. Do not copy `sk.sorted.txt`. Floor ≥ 80_000 unique NFC alphabetic words length ≥ 2. License/floor failure → Implementation Worker stops.  
3. Human queue uses the same Settings slug.  
4. Slovak blanks: bag letters only (41). No loan Q/W/Ě/Ö/Ř/Ü.  
5. One parameterized CORE. English `MOVE_SYSTEM_PROMPT` byte-identical. SHA-256 `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`. Version `pfr-s2-core-1`.  
6. Judge advisory; Django sole validity authority; exhaustion 503; no false invalids.

Also locked: English chrome; labels English/Slovak; default `english`; never mutate live `GameSession`; `PRIMARY_DICTIONARY_PATH` stays Collins; flagship `nvidia/nemotron-3-super-120b-a12b`; no JULS/ScrabGPT import/second SSE/i18n/third language/production deploy/push unless granted; mypy 63/17 no NEW errors; no catalog prompt migration.

SSS 100 table for `slovak.json` (sum 100):  
0 `?`×2; 1 A×9 O×9 E×8 I×5 N×5 R×4 S×4 T×4 V×4; 2 M×4 D×3 K×3 L×3 P×3; 3 J×2 U×2; 4 B×2 Á×1 C×1 H×1 Y×1 Z×1; 5 Č×1 Í×1 Š×1 Ý×1 Ž×1; 7 É×1 Ľ×1 Ť×1 Ú×1; 8 Ď×1 F×1 G×1 Ň×1 Ô×1; 10 Ä×1 Ĺ×1 Ó×1 Ŕ×1 X×1.

### Architecture (unchanged)

Two variants; required `dictionary_file`; services call `load_prefix_index(path)` (fastdict already per-path). Settings slug only on create/join. Session snapshot owns alphabet, blanks, tile points, prompts. Witness/ranked/playability inherit once legality/search/scoring are variant-aware. English invariants stay (tool-only, ≤3 fallback, `provider_requests_used`, unchanged-turn reconciliation, Collins for `english`, search caps).

### Hunspell procedure (Slice 0 network/tooling — planning, not this session’s fetch grant)

**Pin:** LibreOffice/dictionaries commit `75f5dff8c972fff4a32e4ea8434722c277f02a3f` (2024-09-13, hunspell-sk v2.4.8).  
**Files:** `sk_SK.dic` (160357), `sk_SK.aff`, `LICENSE.txt`, `README_en.txt`.  
**SHA-256:**  
- dic `3e3dbd5c6af8431a3a47652c69692f3f86d0cd82deb4418e49a057a33ef56063`  
- aff `af67bbe8ea9dea74968ec01acd266b3f74177ca087ee6eb7898c576e0aef7a3d`  
- LICENSE `dc06f891b13dcb6fe1ede36c0c9020f0e57e6777aca951ecaceefa95a19d7cfc`  
- README_en `a36af75654ae6e65614f7821b2c401ea1f3b4adfdcba9b59efcb1a06c96df14d`  
**URLs:** `https://raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff8c972fff4a32e4ea8434722c277f02a3f/sk_SK/{sk_SK.dic,sk_SK.aff,LICENSE.txt,README_en.txt}` — unauthenticated, no tokens.  
**License:** GPLv2 / LGPLv2.1 / MPLv1.1 (`README_en.txt`). Ship `backend/assets/dicts/slovak.LICENSE` (upstream LICENSE + attribution). SPDX `GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1`.  
**ONE expander:** host `unmunch` (Hunspell 1.7.x). `unmunch sk_SK.dic sk_SK.aff`. Do not use `wordforms` for bulk. Not a Poetry/npm dependency. Missing binary → stop.  
**Filter:** NFC, casefold, `isalpha`, `len>=2`, unique, `sorted`, UTF-8, `#` header then one word/line.  
**Counts:** unique ≥ 80000 and ≤ 5_000_000; Collins `wc -l` == **279497**.  
**Playable lexicon, not SSS official** (accepted residual). Proper nouns kept; dotted/hyphenated dropped by `isalpha`.

### Checklist assignment

**Slice 0:** `variant_store.py`, `english.json`, `test_gamecore.py`, `AGENTS.md`; new `slovak.json`, `slovak.txt`, `slovak.LICENSE`, `test_slovak_variant.py`, `backend/scripts/build_slovak_lexicon.py`.  
**Slice 1:** `services.py`, `serializers.py`, `views.py` (QueueJoinView 400 only), `legality.py`, `move_search.py`, `scoring.py` call sites, `game.py`, `variant_store.py` NFC, `test_dictionary_validation.py`, `test_move_search.py`, `test_api.py`, extend `test_slovak_variant.py`.  
**Slice 2:** `useGameStore.ts` + test, `settings/page.tsx`, `play/page.tsx`, `api.ts`, `types.ts`, `rack.ts`, **`constants.ts`**, `BlankPicker.tsx`, `Tile.tsx`, `AIThinkingOverlay.tsx`, `game/[id]/page.tsx`, `_build_state` if still needed; new `rack.test.ts` as needed.  
**Slice 3:** `prompts.ts` + test, `move/route.ts` + test, `judge/route.ts` + test, `ai-turn-simulation.test.ts`, `get_ai_context` if snapshot still incomplete.  

**Explicitly unchanged this whole:** `collins2019.txt`, `sowpods.txt`, `settings.py`, `fastdict.py`, `tiles.py` / `state.py` / `board.py` / `types.py`, `Cell.tsx` / `Board.tsx` (inspected: they only render `Tile`; 1rem glyphs OK), `draw/[id]/page.tsx` (inspected: `StartTile` at 3rem, no `TILE_POINTS`, no rack regex), migrations 0010/0011/0012, fallback/catalog/NIM routing, playability shape, search caps, `test_full_game_simulation.py` (English-only, no edits).

---

### Slice 0 — assets + English lock

**1. Intent.** Two variant JSONs. `english.json` has required `dictionary_file: "collins2019.txt"`. `slovak.json` is SSS 100 + `slovak.txt`. Collins line count unchanged. No UI/services resolver/prompts.

**2. Allowlist.** Slice 0 checklist. Deferred 1–3. Do not touch Collins/sowpods/services/frontend.

**3. Symbols.** `VariantDefinition.dictionary_file` required; `dictionary_path`; `playable_letters`; loader rejects missing/path-escaping `dictionary_file`. Script: sha256, `unmunch`, filter, write. `AGENTS.md` one sentence: English Tier 1 remains Collins; Slovak ships as `backend/assets/dicts/slovak.txt`.

**4. Data.** Required JSON field `dictionary_file`. No HTTP/persist/migration.

**5. Tests.** `test_slovak_bag_is_official_sss_100`; `test_english_dictionary_file_is_collins`; `test_slovak_lexicon_meets_floor` (≥80000, `auto`/`hra`/diacritic); `test_collins_line_count_unchanged` (279497).

**6. Stay green.** `test_dictionary_validation.py`, `test_gamecore.py`, `test_move_search.py`.

**7. Commands** (cwd `backend/`):

```bash
poetry run pytest tests/test_dictionary_validation.py tests/test_gamecore.py tests/test_slovak_variant.py -q
python -c "from pathlib import Path; print(sum(1 for _ in Path('assets/dicts/collins2019.txt').open()))"
which unmunch
poetry run mypy gamecore
```

**8. Commit.** `feat(variant): add SSS Slovak tile set and hunspell-sk lexicon`

**9. Authority.** Positive: named GETs, host `unmunch`, listed paths. Negative: no JULS, no `sk.sorted.txt`, no UI, no resolver, no prompt edits, no catalog migration, no Poetry hunspell.

**10. Stop.** `unmunch` missing/nonzero/empty stdout; SHA mismatch; README missing GPL+LGPL+MPL; unique &lt;80000 or &gt;5000000; Collins lines ≠ 279497; Slovak tiles ≠ 100; `CH` as a tile.

**11. Rollback.** Delete Slovak assets/script; revert `english.json`/`variant_store.py`.

**12. Next-slice residual.** Global Collins singleton, `isascii`, A–Z legality, English default scoring, UI A–Z remain.

---

### Slice 1 — engine

**1. Intent.** Per-path cache; unknown slug `{ok:false, error, code:"unknown_variant"}` HTTP 400; Unicode membership; variant alphabet/blanks/points; NFC 15-char rows; English `qi`/`za` pass, `qlet` fail; search caps unchanged.

**2. Allowlist.** Slice 1 checklist. Snapshot keys `tile_points`, `alphabet`, `lexicon_id` (`collins2019`|`slovak`) on `_build_state` and `get_ai_context`.

**3. Symbols.** `_get_prefix_index(session)` via `load_prefix_index(path)`; drop module-global unkeyed cache. `_word_passes_dictionary`: drop `isascii`; NFC+casefold; `len>=2`; `isalpha`; `contains`. `_board_from_session` / `_placements_from_data` NFC. `create_game`/`join_human_queue` reject unknown before insert. Serializers `validate_variant_slug`. `QueueJoinView` 400 when `ok` is false (CreateGameView already maps). `evaluate_scoring_move(..., letters=None, variant=None)` default `LETTERS`; `score_words(..., variant=)`. `_Searcher.blank_letters`; `find_legal_scoring_move`/`find_ranked_scoring_moves` gain `blank_letters`/`variant`. `game.py` `score_words(..., variant=self.bag.variant_slug)`. `normalise_letter` NFC. `validate_words` source stem of `dictionary_file`.

**4. Data.** Error `unknown_variant`. Snapshot keys above. No DB migration.

**5. Tests.** English still qi/za/qlet; Slovak diacritic only on Slovak dict; nonalpha/short rejected; create/queue 400 `unknown_variant`; Slovak blank `Á`; `Á` scores &gt;0 on slovak; NFC combining ingest. Do not strip `isascii` from English test helpers in `test_move_search.py` / `test_full_game_simulation.py`.

**6. Stay green.** Those files plus `test_api.py`, `test_gamecore.py`. `test_full_game_simulation.py` untouched.

**7. Commands** (cwd `backend/`):

```bash
poetry run pytest -m "not internet and not slow" -q
poetry run mypy config game gamecore accounts catalog
```

**8. Commit.** `fix(engine): per-variant lexicon, alphabet, and scoring`

**9. Authority.** Engine/API/tests only. No Settings/UI, no prompt hash change, no cap change, no fastdict rewrite.

**10. Stop.** English tests red; unkeyed global dict remains; `isascii` still in `_word_passes_dictionary`; legality still hard `LETTERS` with no override; `_submit_move_locked` still `score_words` without `variant=session.variant_slug`; new mypy errors.

**11. Rollback.** Revert commit. Collins path never moved.

**12. Next-slice residual.** Frontend A–Z rack/picker/points; play page omits slug (backend defaults english).

---

### Slice 2 — Settings / UI / persist

**1. Intent.** Premium English/Slovak control. Persist version **2**. Migrate rewrite (not `if (version >= 1) return`). Create/join send slug. In-game alphabet/points from **session**. No live PATCH.

**2. Allowlist.** Includes `constants.ts`. Not Cell/Board/draw unless Tile clipping is proven (not expected).

**3. Symbols.** `selectedVariantSlug`; partialize it. Exact migrate:

```ts
migrate: (persistedState, version) => {
  const incoming = { ...((persistedState ?? {}) as Record<string, unknown>) };
  if (version < 1) {
    delete incoming.localAIContextLength;
    delete incoming.localAIReloadAfterTurn;
  }
  if (version < 2) {
    if (incoming.selectedVariantSlug !== "english" && incoming.selectedVariantSlug !== "slovak") {
      incoming.selectedVariantSlug = "english";
    }
  }
  return incoming as unknown as GameStore;
}
```

Settings panel “Game language”. `createGame` `variant_slug`. Play page stops hardcoding queue `"english"`. `GameState` snapshot fields. `isPlausibleRack(rack, alphabet?)`: 1–7, ≤2 blanks, membership in alphabet or Unicode letter fallback `/^[\p{L}?]$/u` — never Settings. BlankPicker from `gameState.alphabet`, 7 columns, English title. `TILE_POINTS` remains English fallback; `Tile`/`AIThinkingOverlay` prefer `tile_points`. Invalid-word copy parameterized by `lexicon_id`.

**4. Data.** localStorage version 2. HTTP `variant_slug`.

**5. Tests.** migrate v1 → english slug, keep budgets, no revived local-AI keys; keep explicit slovak if present; rack accepts `Á` with alphabet; rejects emoji.

**6. Stay green.** Existing `useGameStore.test.ts` fallback-progress tests.

**7. Commands** (cwd `frontend/`):

```bash
npx vitest run src/hooks/useGameStore.test.ts src/lib/rack.test.ts
npm run lint
```

**8. Commit.** `feat(ui): persist game language and variant tile alphabet`

**9. Authority.** No chrome i18n; no in-game language switch; no CORE edit.

**10. Stop.** migrate still short-circuits `version >= 1`; queue still hardcoded english; rack still A–Z only; BlankPicker A–Z despite 41-letter alphabet; `Á` still shows 0 points when snapshot has 4.

**11. Rollback.** Revert slice.

**12. Next-slice residual.** CORE/judge still Collins-shaped; `GRID_ROW` still ASCII.

---

### Slice 3 — prompts / judge / pipeline

**1. Intent.** English CORE bytes + hash unchanged. Version stays `pfr-s2-core-1`. Slovak uses factory (lexicon name, tile values from snapshot, shed X/10-point tiles, exemplars `AUTO` opening + rejection-pivot, no Q/W). Judge uses `judgeSystemPromptFor` (replace inline Collins string in `judge/route.ts`). `GRID_ROW` `/^[\p{L}.]{15}$/u`. Slovak turn: legal move exists ⇒ not PASS. SSE not forked.

**2. Allowlist.** Slice 3 checklist. No catalog migration.

**3. Symbols.** `moveSystemPromptFor`; `MOVE_SYSTEM_PROMPT = moveSystemPromptFor(englishMoveSpec)` identity. `buildMoveUserPrompt` tile values from context. Judge factory; English `JUDGE_SYSTEM_PROMPT` export stays Collins text. Move route passes spec from context.

**4. Data.** Optional judge `lexicon_id`. No durable schema.

**5. Tests.** Hash gate exact hex above; Slovak CORE must not name Collins as lexicon; `extractGridRows` keeps `Á`; judge English Collins / Slovak not Collins / 503 no synthetic invalids; `slovak found rack does not complete with genuine_no_move_pass`.

**6. Stay green.** `prompts.test.ts` hash, English 300-turn sim, move/judge route tests.

**7. Commands** (cwd `frontend/`):

```bash
npx vitest run src/lib/prompts.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/judge/route.test.ts src/app/api/ai/move/route.test.ts
```

**8. Commit.** `feat(ai): parameterize move/judge prompts per variant lexicon`

**9. Authority.** No second route; no version bump; no prompt DB migration; no paid models.

**10. Stop.** SHA-256 ≠ quoted hex; version ≠ `pfr-s2-core-1`; Slovak CORE treats Collins as authority; judge synthesizes invalid; PASS while `legalMoves.length > 0`.

**11. Rollback.** Revert slice.

**12. Residual.** Live-play later; hunspell ≠ tournament; SEARCH_PROFILE may still say Collins; 3M-word RAM; blank fanout 41 inside existing caps.

### Live-play (design only)

2 English + 3 Slovak vs NIM `nvidia/nemotron-3-super-120b-a12b`. Fail on pass/exchange when `playability.status=found`. Telemetry: `variant_slug`, `completion_source`, `probe_status`, `repair_attempted`, `terminal_cause`, `provider_requests_used`.

### Non-goals

UI i18n; third language; JULS; ScrabGPT import; CH tile; replacing Collins; paid models; Stripe; LM Studio; Vercel AI Gateway; closing prior wholes; production deploy; push unless granted; loan-letter blanks; 112-tile; catalog prompt migration; heavy runtime deps.

---

**Smallest next step:** Orchestrator presents this deepened plan to Michal for approval, then issues Slice 0 to a **fresh** Implementation Worker with `Native planning mode: not-used`, the Slice 0 twelve-part contract, named hunspell URLs/SHA-256/`unmunch` host tool, Collins `wc -l` 279497, and no implementation authority leaking from this report.

**Report justification:** `new-evidence`

**Authority-expiry statement:** This exchange’s planning authority expires with this terminal report. Plan UI approval, retained context, and this report grant no implementation authority. A second automatic targeted revision is prohibited.

**Logical-whole closure:** not-closed

**Resolved Execution Issues / Near-Misses:** Exchange 01 underspecified hunspell expansion, persist migrate (`if (version >= 1) return`), NFC slice ownership, `constants.ts` allowlist, and the English AP report. This exchange specified `unmunch` (verified 3_005_250 unique words), SHA-256 pins, migrate rewrite, NFC ingest points (Slice 1 board/placements; `normalise_letter` NFC), and assigned every checklist path. Residual: `unmunch` comment-parse stderr is noisy but non-fatal.

**Pre-Existing Failure Classification:** none in repository HEAD (no new product defect opened). Exchange 01 process gap (missing AP terminal report) is closed by this report; it is not a code defect on `30c4d30`.