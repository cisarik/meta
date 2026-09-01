Report for ORCHESTRATOR_CHAT
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 05
Worker exchange ordinal: 01
Status: PARTIAL
Phase-qualified result: planning-partial
Start commit: aa257a7444c8078c57b63b223421e2180a516092
End commit: aa257a7444c8078c57b63b223421e2180a516092
Changed files: none in Libre Tiles; no meta report written.
Commit/push: not authorized and not performed.
Capability handshake: Native Plan Mode was requested and directly observed on. Read-only filesystem, shell, Git inspection, pytest, Vitest, and mypy were directly observed. Provider credentials were not probed; sub-agents were not used.
Repository gate: PASS. Branch main, porcelain empty, HEAD and local origin/main equal the baseline, .ap gitlink and checkout equal 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
Frozen inventory verified:
- U: 2934106db9b37df21b60b6701a4690e78c4fe094 — fix(ai): accept Unicode letters in move placement normalize
- L2: 13da2f97dfbdd64cc430a2be402c8ab089186dff — fix(engine): gate Slovak two-letter words to SSS B2
- L2b: aa257a7444c8078c57b63b223421e2180a516092 — fix(engine): use SSS B2 as Slovak two-letter lexicon
The prior slovak-playable-variant whole remains implementation-complete, liveplay-FAIL, and not closed.
Validation performed:
- Backend focused suite: 43 passed.
- Frontend move/prompt/fallback suite: 102 passed.
- Frontend stream/300-turn simulation suite: 18 passed.
- Mypy: unchanged 12 errors in 6 files.
- Dictionary: 3,005,250 non-comment entries; 269 two-letter entries. loso, miroľa, náhlo, vltavu, ume, ou, and am are present; aj is absent from hunspell and supplied by B2.
- A simple NFC + playable-alphabet + length 3–15 filter retains 2,364,691 entries and all five sampled residuals, so it is not a credible quality filter.
Current search measurements supersede the prompt snapshot:
Case	Witness	Ranked
English AUTOLIN	found, complete, 4ms, OUTLAIN 66	found, complete, 734ms, OUTLAIN 66
Slovak AUTOLIN	found, complete, 1ms, LATINOU 72	found, complete, 272ms, LATINOU 76
Slovak ?AUTOLI	found, complete, 10ms, ITALKOU 70	found, incomplete at 750ms, 18,559 nodes, OTUPILA 74
Slovak ÔŔYÉIST	found, complete, 2ms, ISTÉ 20	found, complete, 23ms, ISTÉ 20
Midgame AUTO + rack ĽŤÁSENI	found, complete, 47ms	found, complete, 356ms, SOĽNÁ 22


Prefix-index load was approximately 237ms English versus 5,484ms Slovak; blank alphabets remain 26 versus 41 letters. Because every measured runtime-ranked case returned found, Slice S should add the missing CLI evidence without changing English or Slovak production caps yet.
Planning Record:
- Planning cycle: initial
- Prior planning report: none
- Targeted revision basis: none
- Changed decision boundary: none
- Preserved unaffected decisions: locked forks; shipped U/L2/L2b; English Collins and CORE bytes; SSS-100; no JULS; no second SSE route
- Automatic targeted revisions used: 0
Deviations, risks, or missing evidence:
- The prompt’s Stage-1 search timings were stale; current measurements are recorded above and remove the basis for an immediate production cap change.
- Deeper inspection found that Judge route comments, its 50-second constant, and tests also encode five lanes. Slice F therefore includes those files rather than changing only ai-fallback.ts.
- L3 is not implementation-grant-ready because the exact licensed source/filter fact is absent. This is the sole reason for planning-partial.
Smallest next step: accept the plan and issue Slice F to a fresh Implementation Worker with Native planning mode not-used, explicit implementation authority, and exact baseline aa257a7444c8078c57b63b223421e2180a516092.
Report justification: new-evidence
Authority-expiry statement: This exchange’s planning authority expires with this terminal report. Plan approval, retained context, or a UI transition grants no implementation authority.
Logical-whole closure: not-closed
Resolved Execution Issues / Near-Misses: The listed five-vs-three drift initially appeared confined to the shared fallback module; inspection found the same stale contract in Judge code/tests. The plan now assigns all related paths to Slice F. The stale Slovak timing premise was resolved through fresh measurements, avoiding an unsupported production cap edit.
Pre-Existing Failure Classification: At baseline aa257a7444c8078c57b63b223421e2180a516092, mypy gamecore game/services.py reports 12 errors in 6 files: config/settings.py dict type, two unused ignores in game/models.py, untyped Channels plus two generic-dict findings in game/realtime.py, variant argument types in gamecore/scoring.py and gamecore/game.py, and four unused ignores in game/services.py. This baseline does not predate the entire logical whole, but the same signature was recorded before this planning exchange in sessions 03–04. Some findings are adjacent to the engine, but no candidate or tracked file was changed here; later grants must allow the identical set and stop on any new error. The debt does not block this planning result and is otherwise parked.


9:01 AM



PlanOpen


Remaining Slovak Gameplay Quality Plan
Summary and interface changes
Implement in the order F → T → S → L3 → V. F restores the documented three-pair queue, giving a preferred 120s/30-step turn an exact 40s/20-step first grant before ordinary request overhead. T makes an unclassified provider/runtime failure use backend-ranked and direct-witness rescue even when the provider produced no valid candidate, while retaining terminal diagnostics through the SSE client and post-turn UI. S adds provider-free Slovak ranked fixtures; current evidence does not justify changing DEFAULT_RANKED_MAX_ELAPSED_MS.
Interface changes are limited to MAX_FALLBACK_ATTEMPTS = 3, Judge’s 30-second overall budget, and transient AiMoveStreamTerminal telemetry. There is no durable schema or endpoint addition. English MOVE_PROMPT_VERSION stays pfr-s2-core-1, and the CORE SHA-256 must remain c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60.
L3 remains evidence-gated. No current lawful mechanical filter removes the demonstrated length-≥3 noise, and no replacement artifact with path, hash, and redistribution license is available.
L3 options
Option	Provenance/license	Gameplay evidence	Recommend?
Keep	Existing pinned hunspell tri-license is recorded	3,005,250 entries; rejected/noisy samples remain eligible	no
Filter	A derivative can retain existing license/attribution, but needs an exact accepted predicate	NFC + alphabet + length 3–15 leaves 2,364,691 entries and retains every sampled residual	no
Replace	Potentially strongest route	No exact artifact path, SHA-256, license, or verified count exists	no


Exact fact needed to unblock L3: either a curated source path plus SHA-256 and redistribution/derivative license, or an owner-approved deterministic filter specification with expected output count/SHA-256 and accepted keep/drop fixtures.
Already shipped and protected: Unicode normalization in route.ts; SSS B2 asset/config/loader and B2-first service behavior; Slovak engine/variant B2 assertions. Explicitly unchanged: Collins, english.json, PRIMARY_DICTIONARY_PATH, prompts and CORE/version, catalog, tile bag, JULS, move_search.py defaults, and service search caps.
Slice F — Three-lane fallback budget
1. Intent
The shared Play/Judge queue contains at most three distinct provider/model pairs, preserving a valid preference as lane one and untouched catalog order thereafter. With a 120-second/30-step Play turn, lane one receives 40 seconds and 20 steps before request overhead, retaining the two-step route repair reserve. Judge performs at most three ten-second attempts within 30 seconds and still returns 503 on exhaustion. English ranked rescue, unchanged-turn reconciliation, and whole-turn provider accounting remain unchanged.
2. Changed-path allowlist
- Existing: frontend/src/lib/ai-fallback.ts
- Existing: frontend/src/lib/ai-fallback.test.ts
- Existing: frontend/src/lib/ai-turn-simulation.test.ts
- Existing: frontend/src/app/api/ai/judge/route.ts
- Existing: frontend/src/app/api/ai/judge/route.test.ts
AGENTS.md is unchanged because it already specifies three pairs and 30 seconds.
3. Function/symbol edit map
- ai-fallback.ts: set MAX_FALLBACK_ATTEMPTS to 3; retain queue ordering, attemptTimeoutSeconds, attemptStepGrant, accounting, and reconciliation algorithms.
- ai-fallback.test.ts: update five-lane expectations to three and pin attemptTimeoutSeconds(120, 3) === 40 plus attemptStepGrant(30, 3) === 20.
- ai-turn-simulation.test.ts: assert at most three posts/distinct pairs while continuing to exercise all five bootstrap models as preferences.
- Judge route: set OVERALL_BUDGET_MS = 30_000 and correct its contract comment.
- Judge tests: change exhaustion and malformed-output expectations from five calls to three.
4. Data/schema changes
None.
5. Tests to add or update
- caps Play and Judge at three distinct pairs
- grants the preferred 120-second 30-step lane 40 seconds and 20 steps
- defensively caps a raw caller queue at three lanes
- can succeed only on lane three with two reconciliations and one terminal
- pins anti-pass recovery across five bootstrap preferences with at most three lanes
- returns 503 after exhausting three attempts without inventing results
- caps malformed-output retries at three models
Assert preference identity, provider accounting, retry-after aggregation, and no fourth POST.
6. Tests that must stay green
- src/lib/ai-fallback.test.ts
- src/lib/ai-turn-simulation.test.ts
- src/app/api/ai/judge/route.test.ts
- src/app/api/ai/move/route.test.ts
- src/lib/prompts.test.ts
7. Validation commands
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/ai-fallback.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/judge/route.test.ts src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts
npm run lint
npm run build
8. Proposed commit subject
fix(ai): restore three-lane fallback budgets
9. Positive authority / Negative authority
Positive: edit only the five paths above; align shared queue and Judge budgets with the existing documented contract. Negative: no move-route, prompt, catalog, store-default, provider-runtime, backend, or English rescue changes; no provider calls.
10. Stop predicates
Stop if lane one is not the valid preference, 120/30 does not yield 40/20 in deterministic tests, any fourth provider lane opens, Judge synthesizes verdicts on exhaustion, unchanged-turn reconciliation weakens, provider usage is miscounted, or the CORE hash/version changes.
11. Rollback
Revert the single Slice F commit.
12. Residual risks handed to the next slice
A generic/no-terminal failure can still suppress backend rescue and collapse into uninformative UI copy; Slice T owns that path.
Slice T — Backend rescue and terminal error honesty
1. Intent
An unclassified provider/runtime exception no longer requires an earlier provider-valid candidate before backend-ranked rescue is attempted. The route tries ranked candidates, then authoritative playability and direct Unicode witness rescue; it does not call the failed provider again for repair. If the turn still cannot finish, the SSE terminal retains bounded cause/probe metadata and the UI reports that diagnostic instead of bare AI move failed. A lost terminal is reconciled against Django state so an already-persisted move is not shown as a failure.
2. Changed-path allowlist
- Existing: frontend/src/app/api/ai/move/route.ts
- Existing: frontend/src/app/api/ai/move/route.test.ts
- Existing: frontend/src/lib/ai-move-stream.ts
- Existing: frontend/src/lib/ai-move-stream.test.ts
- Existing: frontend/src/lib/types.ts
- Existing: frontend/src/app/game/[id]/page.tsx
- Existing tests only: frontend/src/components/game/AIThinkingOverlay.test.ts
The shipped Unicode predicates in normalizePlacementData are regression-protected, not redesigned.
3. Function/symbol edit map
- Route terminal helpers: make commitBestAvailable and probeAndResolve callable from the generic-exception path.
- probeAndResolve: accept allowProviderRepair; normal completion passes true, failed-runtime recovery passes false, while direct witness/exchange/pass remain available.
- Generic catch: always try backend-ranked choices even with zero provider candidates; then probe. Successful ranked recovery keeps generic_error_fallback; an unrecoverable internal rescue failure emits bounded code ai_move_internal_error and cause backend_rescue_error, never raw exception text.
- Classified provider failures remain coded and eligible for outer fallback.
- AiMoveStreamTerminal: attach optional transient AiTurnTelemetry to coded/generic/no-terminal results and retain the last bounded telemetry when the stream ends without a terminal.
- Export describeAiMoveFailure, producing specific post-turn copy with cause/probe when available.
- describeAiTurnTelemetry: render a concise failure state inside the existing attempt-progress surface.
- triggerAIMove: reconcile generic/no-terminal results before displaying failure; suppress the error if the exact anchored turn already advanced, otherwise use describeAiMoveFailure.
4. Data/schema changes
The client-side terminal union gains optional transient telemetry. SSE fields already exist; no endpoint, database, localStorage, or persisted metadata schema changes.
5. Tests to add or update
- Reverse the existing guard into rescues a generic runtime error with a backend-ranked candidate without a tracked provider candidate.
- rescues a generic runtime error with a Slovak Unicode witness when ranked candidates are empty.
- emits stage-specific terminal telemetry when backend rescue itself fails.
- preserves error terminal cause and probe status.
- returns no_terminal with the last bounded telemetry.
- describes unchanged-turn failures without bare AI move failed.
- renders backend rescue failure telemetry inside the attempt progress surface.
Assertions include no second generateText call after runtime failure, no stale_witness, no pass/exchange while probe is found, no raw provider/backend body leakage, and unchanged provider-request accounting.
6. Tests that must stay green
- Unicode ranked/witness cases in route.test.ts
- ai-move-stream.test.ts
- ai-turn-simulation.test.ts
- Slice F fallback and Judge tests
- AIThinkingOverlay.test.ts
- prompts.test.ts CORE pin
7. Validation commands
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/lib/ai-fallback.test.ts src/components/game/AIThinkingOverlay.test.ts src/lib/prompts.test.ts
npm run lint
npm run build
8. Proposed commit subject
fix(ai): rescue and explain terminal stream failures
9. Positive authority / Negative authority
Positive: mocked, provider-free repair of route finalization, SSE terminal telemetry, and page error reconciliation. Negative: no live provider calls, no fallback-cap change, no second SSE route, no CORE/version/catalog change, no persistence of telemetry, and no weakening of Django legality.
10. Stop predicates
Stop if coded provider errors cease to be fallback-eligible, generic recovery calls the failed provider again, a Unicode witness becomes stale_witness, a found probe can pass/exchange, a terminal can expose raw exception/private payloads, a lost-stream reconciliation can retry after state changed, or English CORE/ranked rescue regresses.
11. Rollback
Revert the Slice T commit; no durable migration exists.
12. Residual risks handed to the next slice
Slovak ranked behavior still lacks a dedicated provider-free CLI fixture, and the length-≥3 lexicon remains noisy.
Slice S — Slovak ranked-search CLI fixtures
1. Intent
A dedicated pytest file exercises Slovak ranked search without Django HTTP or a model provider. It covers empty-board racks with and without a blank, a Unicode midgame, and explicit OU/AM cross traps. It logs status, completion, nodes, elapsed time, top words, and score under pytest -s. Current runtime defaults remain unchanged because measured cases return found, including the cap-bound blank case.
2. Changed-path allowlist
- New: backend/tests/test_slovak_ranked_search.py
No production Python or existing test file changes.
3. Function/symbol edit map
Add test-only helpers for:
- module-scoped Slovak index/word/prefix predicates using the B2-aware service helpers;
- deterministic board construction;
- one-line ranked metric output;
- NFC Unicode-category validation equivalent to JavaScript \p{L};
- canonical placement comparison for illegal cross traps.
4. Data/schema changes
None.
5. Tests to add
- test_empty_board_ranked_slovak_returns_found_with_and_without_blank
  - Racks AUTOLIN and ?AUTOLI
  - status == "found", candidates non-empty, positive top score
  - report complete, nodes, elapsed, top word/score; do not require complete=True
- test_midgame_ranked_slovak_returns_found_with_unicode_candidate
  - Board AUTO across row 7, rack ĽŤÁSENI
  - found result and at least one candidate containing a diacritic placement
  - placements_to_dicts preserves it and every letter passes the duplicated NFC/Unicode-letter predicate
- test_slovak_ranked_search_rejects_ou_and_am_crosses_without_scoring
  - Legal B2 main UM crossing illegal OU
  - Legal B2 main MI crossing illegal AM
  - legality is invalid_word, total score zero; ranked candidates never contain or reproduce those rejected crosses
6. Tests that must stay green
- tests/test_dictionary_validation.py
- tests/test_slovak_engine.py
- tests/test_slovak_variant.py
- tests/test_move_search.py
- Default four-game tests/test_strength_benchmark.py
- Frontend Unicode route tests
The opt-in 100-game English matrix remains skipped unless explicitly enabled.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_slovak_ranked_search.py -q -s
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts
8. Proposed commit subject
test(engine): add Slovak ranked-search CLI fixtures
9. Positive authority / Negative authority
Positive: add the one test file and use committed Slovak/SSS assets. Negative: no move_search.py, services, search-cap, dictionary, frontend, benchmark-helper, dependency, or provider change.
10. Stop predicates
Stop if any required rack/midgame result is not found, Unicode serialization fails, OU/AM can score, English strength/search tests regress, or satisfying the tests would require a production cap change. Record variable elapsed/completion values; do not convert timing variation alone into a code edit.
11. Rollback
Remove the new test file by reverting the Slice S commit.
12. Residual risks handed to the next slice
The CLI establishes mechanics and budgets, not SSS lexical quality; current top candidates still come from the 3M-word hunspell expansion.
Slice L3 — Length-≥3 Slovak lexicon quality
1. Intent
This slice cannot receive implementation authority until the exact source/filter gate above is satisfied. Once selected by the Cooperator and encoded in the Orchestrator grant, slovak.txt becomes a deterministic, licensed length-≥3 lexicon while B2 remains the sole two-letter authority. The build records the source identity, expected SHA-256/count, attribution, and accepted keep/drop fixtures. Ranked Slovak fixtures must no longer return the specifically rejected words as candidates.
2. Changed-path allowlist
After the missing gate is supplied:
- Existing: backend/assets/dicts/slovak.txt
- Existing: backend/assets/dicts/slovak.LICENSE
- Existing: backend/scripts/build_slovak_lexicon.py
- New: backend/tests/test_slovak_lexicon_quality.py
- Existing from Slice S: backend/tests/test_slovak_ranked_search.py
- Existing: AGENTS.md, limited to the exact lexicon provenance/quality sentence
3. Function/symbol edit map
- Build script: one selected source route only; verify source SHA-256/license, normalize NFC/casefold, retain only alphabetic playable-letter words of length ≥3, sort uniquely, and assert the grant-pinned output count/hash.
- License asset: identify the source, selected license, modification/filter notice, and attribution.
- Quality tests: stream the committed output without loading it into a second production index.
- Ranked tests: add the exact rejected-word exclusion set.
No implementation Worker chooses filter versus replacement.
4. Data/schema changes
Replace the committed length-≥3 dictionary contents and provenance. No database/API schema change. slovak_two_letter.txt remains the independent 103-word B2 lexicon.
5. Tests to add
- test_slovak_long_lexicon_matches_authorized_hash_count_and_provenance
- test_slovak_long_lexicon_is_nfc_sorted_unique_and_playable
- test_slovak_long_lexicon_contains_no_two_letter_rows
- test_slovak_long_lexicon_keeps_owner_acceptance_fixture
  - Keep: auto, hra, škola, úpis, isté
- test_slovak_long_lexicon_drops_owner_rejected_fixture
  - Drop: loso, miroľa, náhlo, vltavu
- Extend ranked CLI with test_ranked_slovak_candidates_exclude_owner_rejected_words
- Existing B2 test continues to prove aj/ak/či legal and ou/am illegal.
6. Tests that must stay green
All Slice S tests, Slovak engine/variant/dictionary suites, English move-search and default strength benchmark, frontend Unicode route tests, and the CORE hash test.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_slovak_lexicon_quality.py tests/test_slovak_ranked_search.py -q -s
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py
sha256sum assets/dicts/slovak.txt assets/dicts/slovak.LICENSE

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts
The eventual grant must add the exact source/build command and expected hashes before implementation begins.
8. Proposed commit subject
fix(lexicon): curate Slovak words for gameplay quality
9. Positive authority / Negative authority
Positive only after the source gate: use the selected licensed source/filter and the six paths above. Negative: no mystery home-directory search, JULS, sk.sorted.txt, slovak_no_license.txt, B2 edits, Collins/English edits, service-rule changes, source substitution, or silent reuse of the old ≥80k expansion floor.
10. Stop predicates
Stop before mutation if source path/hash/license or exact filter specification is missing. During implementation, stop on source/output hash mismatch, unmet license obligations, non-NFC/unsorted/duplicate output, rejected fixtures surviving, keep fixtures disappearing, output count differing from the grant, B2 behavior changing, English regression, or any need for a forbidden source.
11. Rollback
Revert the L3 commit, restoring the prior hunspell asset while leaving B2 untouched.
12. Residual risks handed to the next slice
Automated fixtures cannot prove subjective tournament feel; final evidence remains the five-game live-play protocol.
Slice V — Live-play acceptance
1. Intent
After F, T, S, and authorized L3 are accepted, run two fresh English and three fresh Slovak vs-AI games against exact NIM nvidia/nemotron-3-super-120b-a12b. Each game records at least two persisted AI terminals unless an owner stop is explicitly classified incomplete. The protocol proves that three-lane budgeting, ranked/witness rescue, Unicode persistence, B2, and lexicon quality hold together. This is live acceptance, not a replacement for pytest/Vitest.
2. Changed-path allowlist
None. Product repository mutation and commits are prohibited; evidence is returned in the Worker report.
3. Function/symbol edit map
None. Observe the existing UI, SSE telemetry, Django state, and persisted moves.
4. Data/schema changes
No schema changes. Record per turn: game/variant/lexicon, pre-turn playability, action, words/score, completion source, probe status, repair flag, terminal cause, attempt timeout/max steps, provider-request usage, and persistence result.
5. Tests/scenarios
- EN-1 and EN-2: at least two persisted AI terminals each; each game must demonstrate ranked or witness rescue.
- SK-1 through SK-3: at least two persisted AI terminals each.
- At least one Slovak persisted terminal must be backend_ranked_candidate or backend_witness_rescue; a provided diacritic witness must persist without stale_witness.
- Preferred NIM lane under 120s/30 steps must show queue length ≤3, max_steps=20, and at least 30 seconds of timeout.
- Pass/exchange is valid only when pre-turn playability is none; found or indeterminate is a failure.
- ou/am must never score; L3 rejected words must not persist.
- Bare Last error: AI move failed is a failure unless Django already persisted the terminal or the UI shows a coded provider error with terminal diagnostics.
6. Tests that must stay green before live play
All F/T/S/L3 focused suites and the English CORE pin. No live call begins after a CLI failure.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_slovak_ranked_search.py tests/test_slovak_lexicon_quality.py tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/ai-fallback.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts src/lib/prompts.test.ts
After these pass, the Cooperator performs the five UI games. No command or report reads or prints API keys.
8. Proposed commit subject
Not applicable; acceptance-only slice with no commit.
9. Positive authority / Negative authority
Positive: exact five-game protocol and exact NIM provider calls under a separately activated provider/browser grant. Negative: no OpenRouter substitution for the named evidence, no secret inspection, production/deploy/push, database editing, source mutation, extra games without evidence-derived purpose, or treating owner stop as PASS.
10. Stop predicates
Stop and report FAIL/incomplete on any stated scenario failure, provider/accounting anomaly, credential exposure, unexpected mutation, changed baseline, owner stop, or missing terminal evidence. Do not repair during acceptance.
11. Rollback
Acceptance mutates no source; stop the run and preserve the bounded game/report evidence.
12. Residual risks
Provider availability and model behavior remain external. Passing live play establishes the tested five games, not universal Slovak tournament strength.
Sequencing recommendation
1. Implement F from exact baseline aa257a7444c8078c57b63b223421e2180a516092.
2. Implement T from the accepted F commit.
3. Add S from the accepted T commit and preserve its measurements as the pre-L3 baseline.
4. Obtain the exact L3 Cooperator source/filter fact, then issue the completed L3 grant. Do not let the implementer choose the lexicon route.
5. Run V only after all applicable CLI suites pass; if L3 remains blocked, any live run is diagnostic and cannot be final gameplay-quality acceptance.