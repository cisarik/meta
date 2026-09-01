Report for ORCHESTRATOR_CHAT
Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 01
Worker exchange ordinal: 01
Status: PASS
Phase-qualified result: planning-complete
Gate and provenance:
- Start commit: 782a23c00553172b6e0c158d4d082f661a28fa6b
- End commit: 782a23c00553172b6e0c158d4d082f661a28fa6b
- Branch: main
- Porcelain: empty before and after inspection/testing.
- .ap gitlink and checkout: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
- origin/main: aa257a7444c8078c57b63b223421e2180a516092; local main is exactly three commits ahead and zero behind. Classified unpublished-candidate, not divergence.
- The [predecessor closure record](/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/99_orchestrator_closure_00.md) confirms mechanical completion, L3 parked, and Slice V not claimed or reopened.
Capability handshake:
Capability	Requested	Directly observed
Native planning mode	Required/on	On
Exact model	No exact model requested	Unknown—not observably exposed
Reasoning	High recommended	Unknown—not observably exposed
Filesystem, shell, tests, Git reads	Required	Available and exercised
Browser/provider/credentials	No authority	Not used or probed
Mutation	Two meta mirrors requested	Effective native Plan Mode prohibited filesystem mutation


Planning Record:
- Planning cycle: initial
- Prior planning report: none
- Targeted revision basis: none
- Changed decision boundary: none
- Preserved unaffected decisions: locked forks; shipped U/L2/L2b/F/T/S; English Collins authority; English CORE bytes/version; SSS-100; one SSE route; L3 parked
- Automatic targeted revisions used: 0
- Plan disposition: approval-gated
- Implementation authority: none
- Implementation in this Worker session: prohibited
Tests and validation actually run:
- Wrapped backend Slice S run: 3 passed. Observed LATINOU 76, OTUPILA 74 at the 750 ms incomplete cap, SOĽNÁ 22, and OSAMENIU 74.
- Wrapped backend stay-green set: 44 passed, 1 expected skip.
- Frontend route/fallback/stream/simulation/prompt set: 126 passed across 5 files.
- Slovak B2 measurement: 103 non-comment entries; ja, ty, my, ex present; ou, am absent.
- pytest-django’s live_server fixture is installed and directly discoverable.
- No tracked artifacts were produced; ignored test caches may have refreshed. Final porcelain remained empty.
- Vite native-config fallback and Node module.register deprecation warnings were informational only.
Commit and push: not authorized and not performed.
Changed files: none. Native Plan Mode prohibited the two user-authorized meta writes, so the complete report and planner artifact are supplied in this exchange for Orchestrator archival. The product tree was not changed.
Deviations, risks, and missing evidence:
- No real provider evidence exists; that is intentionally deferred to the separately granted live annex.
- Exact runtime model and effective reasoning profile were not observably exposed.
- The proposed Django-live-server/Vitest composition is supported by current seams but remains to be proven by Slice T’s causal integration test.
- AGENTS.md omits the shipped backend_ranked_candidate completion source; this is pre-existing doc/code drift and is confined to one sentence in Slice T.
Resolved Execution Issues / Near-Misses: The user-level meta-write allowance conflicted with higher-priority native Plan Mode. The safe resolution was no filesystem mutation and complete in-chat delivery; residual risk is that the Orchestrator must archive the two meta copies.
Pre-Existing Failure Classification:
- Pre-existing claim: asserted
- Comparison baseline commit: 782a23c00553172b6e0c158d4d082f661a28fa6b
- Baseline predates: whole-logical-whole
- Test identity: env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py
- Failure signature:
config/settings.py:89: error: Dict entry 1 has incompatible type "str": "Path"; expected "str": "str"  [dict-item]
game/models.py:93: error: Unused "type: ignore" comment  [unused-ignore]
game/models.py:159: error: Unused "type: ignore" comment  [unused-ignore]
game/realtime.py:6: error: Library stubs not installed for "channels.layers"  [import-untyped]
game/realtime.py:6: note: Hint: "python3 -m pip install types-channels"
game/realtime.py:6: note: (or run "mypy --install-types" to install all missing stub packages)
game/realtime.py:6: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
game/realtime.py:18: error: Missing type parameters for generic type "dict"  [type-arg]
game/realtime.py:46: error: Missing type parameters for generic type "dict"  [type-arg]
gamecore/scoring.py:23: error: Argument 1 to "get_tile_points" has incompatible type "object"; expected "VariantDefinition | str | None"  [arg-type]
gamecore/game.py:35: error: Argument 1 to "get_tile_points" has incompatible type "object"; expected "VariantDefinition | str | None"  [arg-type]
game/services.py:313: error: Unused "type: ignore" comment  [unused-ignore]
game/services.py:315: error: Unused "type: ignore" comment  [unused-ignore]
game/services.py:337: error: Unused "type: ignore" comment  [unused-ignore]
game/services.py:1603: error: Unused "type: ignore" comment  [unused-ignore]
Found 12 errors in 6 files (checked 15 source files)
- Topically related to touched behavior: yes; several errors are in adjacent game/services.py and gamecore modules.
- Superseded by accepted authority: none
- Regression exclusion evidence: immutable start/end baseline, no product diff, focused backend and frontend suites green.
- Closure impact: explicitly-parked; Slice E/T must add no new mypy errors, but this debt does not block the protocol.
One smallest next step: Orchestrator presents the plan to the Cooperator for approval, then issues a fresh Implementation Worker with Native planning mode: not-used.
Report justification: new-evidence
Logical-whole closure: not-closed
Authority expiry: this exchange’s planning authority expires with this terminal report. Retained context, the frozen planner artifact, UI approval, Build, or Continue grants no implementation authority.


1:21 PM



PlanOpen


Parameterized CLI AI-play diagnostic protocol
Summary
Build a two-layer, browserless diagnostic protocol followed by an optional live-provider annex:
1. Slice E generalizes the existing provider-free engine evidence into a variant-aware CLI and versioned JSON report.
2. Slice T drives independent AI turns through the real TypeScript move route and fallback orchestrator against an isolated live Django test database, with the model call injected in default fake mode.
3. Slice L runs that same CLI against one explicitly authorized live catalog pair, without source changes.
No HTTP API, database model, migration, production search cap, MOVE CORE, prompt version, or second route changes.
Public CLI contract
diagnose_ai_engine accepts:
- --variant-slug SLUG
- exactly one of --fixture-id ID or --seed UINT32
- --probe-count 1..300, default 1
- --output PATH|-, default -
diagnose_ai_play accepts:
- --variant-slug SLUG
- --provider PROVIDER
- --model-id NATIVE_ID
- --runtime-mode fake|live, default fake
- --timeout-seconds 1..600, default 120
- --max-steps 5..100, default 50
- exactly one of --fixture-id ID or --seed UINT32
- --turn-count 1..300, default 1
- --queue-mode selected-only|catalog-fallback, default selected-only
- --output PATH|-
The model ID is opaque and preserved byte-for-byte: no :free suffix is added or removed. Invalid input exits 2 before database or provider work. Completed runs exit 0 for pass/pass-with-telemetry, 1 for any mechanical failure, or 3 for provider/external incompleteness without a mechanical failure. File output is atomic and refuses to overwrite an existing path; JSON goes to stdout when - is selected, while concise metric lines go to stderr.
Seed mode creates deterministic, independent opening-turn sessions with the real variant and TileBag; fixture mode creates independent sessions from the named board/rack state. turn-count counts independent AI-turn samples, not continuous browser games.
Versioned report contract
libretiles.ai-play-diagnostic/v1 is the canonical comparable JSON artifact. It contains:
- Requested parameters, source revision, report kind, fixture/seed, and exact provider/model pair.
- Engine samples: search status, completeness, nodes, elapsed time, ranked top placement, complete formed words, score, and verdict.
- Turn samples: pre-turn found|none|indeterminate and witness; action; placements; complete formed words; score; exact completion source; probe status; repair flag; terminal cause; per-attempt provider/model, effective timeout and step grant; attempt and whole-turn provider-request counts; and Django persistence/state-delta verification.
- Per-sample verdict: pass, pass_with_telemetry, fail, or external_incomplete, with stable reason codes.
- Summary counts, total provider requests, and unresolved/in-flight count.
- No credentials, authorization headers, prompt text, raw provider bodies, or unbounded exception messages.
The completion-source enum is exactly:
provider_candidate
backend_ranked_candidate
repair_candidate
backend_witness_rescue
genuine_no_move_exchange
genuine_no_move_pass
Repository evidence and design decisions
- [Slovak ranked fixtures](/home/agile/Projects/libretiles/backend/tests/test_slovak_ranked_search.py) are provider-free engine probes with four metric lines, Unicode/hook cases, and exact formed-word set checks; they are not model-parameterized AI turns and do not literally assert OSAMENIU.
- [English strength benchmark](/home/agile/Projects/libretiles/backend/tests/test_strength_benchmark.py) is Collins engine-vs-engine evidence. Its local _is_word uses folded.isascii() and must not be copied into variant-neutral or Slovak code.
- [300-turn simulation](/home/agile/Projects/libretiles/frontend/src/lib/ai-turn-simulation.test.ts) uses the real route/orchestrator but mocked generateText and fake in-memory Django, so it does not prove database persistence.
- [Fallback orchestration](/home/agile/Projects/libretiles/frontend/src/lib/ai-fallback.ts) already owns timeout splitting, step grants, reconciliation, and a maximum of three fallback lanes. The diagnostic reuses it and never creates a five-model loop.
- [Move route](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts) owns NFC Unicode normalization, ranked commit, repair, witness rescue, bounded terminal errors, the two-step repair reserve, and the six completion sources. The plan imports its POST handler; it does not fork or edit the route.
- [SSE consumer](/home/agile/Projects/libretiles/frontend/src/lib/ai-move-stream.ts) and [shared types](/home/agile/Projects/libretiles/frontend/src/lib/types.ts) own terminal parsing and transient telemetry. Diagnostic records are external JSON only and never enter the persisted Zustand slice.
- [Backend services](/home/agile/Projects/libretiles/backend/game/services.py) remain the dictionary/playability/candidate authority. [Ranked search](/home/agile/Projects/libretiles/backend/gamecore/move_search.py) retains its 2000 ms general and 750 ms ranked defaults.
- [Slovak B2](/home/agile/Projects/libretiles/backend/assets/dicts/slovak_two_letter.txt) contains 103 entries; the diagnostic evaluates complete formed words against it.
- [Playability URL/view](/home/agile/Projects/libretiles/backend/game/urls.py) and [service-backed view](/home/agile/Projects/libretiles/backend/game/views.py) expose a probe, not a CLI runner.
- [Root launcher](/home/agile/Projects/libretiles/scripts/libretiles.sh), [backend launcher](/home/agile/Projects/libretiles/scripts/start-backend.sh), [frontend launcher](/home/agile/Projects/libretiles/scripts/start-frontend.sh), and [reload script](/home/agile/Projects/libretiles/scripts/reload.sh) start persistent development services and are not reused by the diagnostic.
Design-fork decisions:
1. Use a composition: Django management command → explicitly selected pytest-django worker → Vitest worker importing the real route. Pure engine pytest loses the route/SSE layer; Node-only loses real Django persistence; management-command-only would reimplement TypeScript; persistent dev scripts and browser automation reduce isolation.
2. The command owns an ephemeral pytest test database and live_server; it never requires an existing runserver or next dev. An all-in-one process cannot load both Django and the TypeScript route without replacing one implementation.
3. Keep provider and native model ID as data. Fake mode mocks only getLanguageRuntime/generateText; backend HTTP and catalog revalidation remain real. Live mode uses the production runtime registry and fails before network if the exact tuple is unsupported.
4. Emit both stable JSON and concise metric lines. Lines are useful interactively but insufficient for model comparison; JSON alone hides progress during bounded searches.
5. Leave shipped Slice S unchanged as a focused regression oracle. Slice E adds data-driven equivalents, deterministic seed support, and a new literal OSAMENIU assertion rather than rewriting those tests.
6. Live provider work is an annex in this whole under a separate grant. Default implementation and acceptance are provider-free.
7. Evaluate only complete formed words with a variant-specific predicate. No substring scan or board-wide text search is permitted.
8. Every backend command is invoked through the required AppImage-clean wrapper; frontend checks use existing npx vitest and npm entrypoints.
Mechanical verdict table
Observation	Verdict
Authoritative probe is found; one legal scoring placement persists once	Pass
Probe is found or indeterminate; action is pass/exchange	Fail
SSE says done but no corresponding Move, or state advances more than once	Fail
Generic/no-terminal failure, unchanged state, no coded provider error and no bounded terminal cause	Fail
Move persisted, then terminal delivery was lost but bounded telemetry explains it	Pass with telemetry
Coded provider failure with unchanged state	External incomplete, not a false pass or mechanical defect
NFC Unicode tile/word differs between backend validation, SSE, and persisted Move	Fail
A complete Slovak formed word has length two and is outside the 103-word B2 set	Fail
A complete English formed word has length two and Collins rejects it	Fail
A longer legal word merely contains ja, ty, my, ex, am, or ou	Never a failure
LATINOU or OTUPILA appears from the shipped Slovak lexicon	Not a protocol failure; parked L3 residual


For Slovak, ja, ty, my, ex, on, si, to, um, mi, aj, and ak remain legal complete two-letter words. ou and am are rejected only when they are themselves complete two-letter formed words. OSAMENIU remains legal even though its longer spelling contains AM.
Explicit non-goals
1. No Slovak bag other than SSS 100; no 100+2 or English bag reuse.
2. No UI localization; English remains default chrome and Settings language.
3. No MOVE CORE byte change, second CORE, route fork, or version bump from pfr-s2-core-1 / SHA-256 c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60.
4. No Judge authority change: exhaustion stays HTTP 503, malformed output never becomes false invalid, Collins remains English authority, and Slovak assistance cannot override Django.
5. No JULS, sk.sorted.txt, unofficial SSS dump, slovak_no_license.txt, paid tier, Stripe, or payment work.
6. NVIDIA NIM remains exactly nvidia/nemotron-3-super-120b-a12b; it is a default parameter, not protocol identity. No FrameNest Omni/VLM.
7. No substring-based two-letter rejection; legality is over complete formed words and the selected variant lexicon.
8. No L3 unpark, Hunspell filtering, lexicon replacement, or treatment of the named residual words as failures.
9. No browser, MCP browser adapter, Playwright, or five-game snapshot script.
10. No second engine or parallel test-Scrabble implementation.
Slice E — Parameterized provider-free engine probe
1. Intent
   HEAD gains a variant-aware engine diagnostic command backed by the real gamecore and backend dictionary predicates. Existing Slice S remains untouched and green. Named JSON fixtures and seeded opening racks produce a versioned report plus metric lines without changing production search caps. A new regression literally pins OSAMENIU legality.
2. Changed-path allowlist
   - New: backend/assets/diagnostics/ai_play_report_v1.schema.json
   - New: backend/assets/diagnostics/ai_play_scenarios_v1.json
   - New: backend/game/diagnostics.py
   - New: backend/game/management/__init__.py
   - New: backend/game/management/commands/__init__.py
   - New: backend/game/management/commands/diagnose_ai_engine.py
   - New: backend/tests/test_ai_play_engine_diagnostic.py
   - Deferred to Slice T: Django live testbed, TypeScript worker, model injection, persistence checks, AGENTS.md sentence.
   - Must not change: Slice S, dictionaries, variants, tile bag, move-search defaults, frontend route/prompts.
3. Function/symbol edit map
   - game/diagnostics.py: DiagnosticScenario, EngineSample, DiagnosticVerdict, load_diagnostic_scenario, build_seeded_scenario, run_engine_probe, classify_complete_formed_words, build_diagnostic_report, write_diagnostic_report.
   - diagnose_ai_engine.py: Command.add_arguments, Command.handle.
   - Scenario asset: named equivalents for AUTOLIN, ?AUTOLI, Unicode midgame, hook/UMENASI, plus an English Collins fixture.
4. Data/schema changes
   No Django migration or persisted product data. Add report schema v1 and versioned diagnostic scenarios. Engine samples populate engine fields; turn fields are nullable/absent under the schema’s engine branch.
5. Tests or CLI entrypoints to add
   - test_engine_cli_writes_v1_json_for_named_fixture
   - test_seeded_engine_probe_is_repeatable
   - test_formed_word_policy_checks_complete_words_not_substrings
   - test_slovak_hook_fixture_keeps_osameniu_legal — new literal assertion that OSAMENIU is among the legal ranked formed words with score 74; this is not an assertion in current Slice S.
   - test_slovak_b2_accepts_named_legal_complete_words
   - test_slovak_b2_rejects_complete_ou_and_am
   - test_english_two_letter_policy_delegates_to_collins
   - test_engine_cli_rejects_unknown_variant_or_fixture_before_search
   - Assert timing/node variance is recorded but never a verdict input.
6. Tests that must stay green
   - Backend: test_slovak_ranked_search.py, test_dictionary_validation.py, test_slovak_engine.py, test_slovak_variant.py, test_move_search.py, test_strength_benchmark.py.
   - Frontend: prompts.test.ts, route.test.ts.
   - No variant-neutral predicate may acquire the benchmark’s English-only isascii() restriction.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_engine --variant-slug slovak --fixture-id slovak-hooks-umenasi --probe-count 1 --output -
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_ai_play_engine_diagnostic.py tests/test_slovak_ranked_search.py tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q -s
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check game/diagnostics.py game/management/commands/diagnose_ai_engine.py tests/test_ai_play_engine_diagnostic.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py game/diagnostics.py game/management/commands/diagnose_ai_engine.py
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/prompts.test.ts src/app/api/ai/move/route.test.ts
   The mypy command may reproduce the classified 12-error baseline, but must add no new diagnostic-file error.
8. Proposed commit subject
   feat(diagnostics): add parameterized engine probe
9. Positive authority / Negative authority
   Positive: add only the listed diagnostic assets, command, helper, and tests. Reuse gamecore, variant assets, _word_passes_dictionary, prefix checking, and ranked-search defaults.
   Negative: no production-cap, dictionary, tile-bag, service/API, prompt, route, catalog, provider, or existing Slice S mutation.
10. Stop predicates
   Stop if the implementation requires changing either production search cap, copying the English isascii() predicate, scanning substrings, rejecting OSAMENIU, changing a variant asset, or writing outside the requested output path and ordinary test caches.
11. Rollback
   Revert the single slice commit; there is no migration or product data to restore.
12. Residual risks and provider annex
   Engine evidence does not prove SSE behavior, fallback accounting, or Django persistence; Slice T owns those. Later provider annex needed: yes, but only after Slice T.
Slice T — Provider-free real-turn CLI
1. Intent
   HEAD gains the public diagnose_ai_play command. It launches one explicit pytest-django worker, which owns an isolated test database and ephemeral live_server, then launches a Vitest worker that imports the real move-route POST, orchestrateFallbackTurn, and consumeAIStream. Fake mode injects only the model/runtime response while every Django request, legality decision, SSE terminal, reconciliation, and Move persistence check remains real. No persistent Next or Django development server is required.
2. Changed-path allowlist
   - Existing: backend/assets/diagnostics/ai_play_scenarios_v1.json
   - Existing: backend/game/diagnostics.py
   - New: backend/game/diagnostic_testbed.py
   - New: backend/game/management/commands/diagnose_ai_play.py
   - New: backend/tests/test_ai_play_turn_diagnostic.py
   - New: frontend/src/lib/ai-play-diagnostic.ts
   - New: frontend/src/lib/ai-play-diagnostic.test.ts
   - New: frontend/src/lib/ai-play-diagnostic.worker.test.ts
   - New: frontend/src/lib/ai-play-diagnostic.live.worker.test.ts
   - Existing: AGENTS.md — exactly one sentence/list correction adding backend_ranked_candidate.
   - Must not change: route.ts, ai-fallback.ts, ai-move-stream.ts, types.ts, prompts, store persistence, backend service endpoints, catalog selection, DB models/migrations.
3. Function/symbol edit map
   - game/diagnostics.py: TurnSample, AttemptSample, PersistenceEvidence, classify_turn_outcome, merge_worker_observation, summarize_report.
   - game/diagnostic_testbed.py: DiagnosticTestbed, build_isolated_games, seed_diagnostic_catalog, run_vitest_worker, verify_persisted_move, teardown_testbed.
   - Management command: argument validation, temporary config creation, explicit pytest node invocation via sys.executable, exit-code mapping, atomic final report.
   - ai-play-diagnostic.ts: buildDiagnosticQueue, fetchPreTurnProbe, runDiagnosticTurn, serializeTerminalObservation, guardNetworkTargets.
   - Fake worker: hoisted mocks for getLanguageRuntime and generateText; real backend fetch.
   - Live worker: no runtime mock; hard guard requiring LIBRETILES_AI_PLAY_LIVE=1 before route import or provider resolution.
4. Data/schema changes
   No product database schema or durable rows. The testbed creates and tears down a pytest test database, users, catalog rows, sessions, slots, and moves. Scenario data gains deterministic fake-response scripts. Report output follows v1; raw temporary config and worker output are removed in finally, while the requested report remains.
5. Tests or CLI entrypoints to add
   - test_diagnose_ai_play_preserves_all_axes_and_native_model_id
   - test_diagnostic_worker_uses_isolated_live_server_and_persists_one_move
   - test_selected_only_queue_runs_exact_requested_pair
   - test_catalog_fallback_uses_preference_first_and_at_most_three_pairs
   - test_fake_mode_rejects_every_non_backend_network_target
   - test_found_or_indeterminate_probe_never_accepts_pass_or_exchange
   - test_generic_unchanged_turn_is_mechanical_failure
   - test_persist_then_explain_is_pass_with_telemetry
   - test_unicode_round_trips_nfc_from_backend_through_sse_to_move
   - test_turn_report_accepts_exact_six_completion_sources
   - test_report_contains_request_accounting_and_redacts_secrets
   - test_live_worker_exits_before_runtime_without_opt_in_sentinel
   - test_existing_output_path_is_not_overwritten
   - Integration assertions query the actual new Move, compare action/words/score/ai_metadata, and require exactly one state-version/move-count advance.
6. Tests that must stay green
   - Backend Slice E/S, dictionary, Slovak engine/variant, move search, English strength benchmark, and test_api.py playability/candidates/pass-exchange/persistence coverage.
   - Frontend route, fallback, SSE stream, 300-turn simulation, Judge route, prompts hash, AI runtimes, and useGameStore.test.ts.
   - Judge remains 503-on-exhaustion; telemetry remains absent from localStorage.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
diagnostic_fake_dir="$(mktemp -d)"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode fake --timeout-seconds 60 --max-steps 30 --fixture-id slovak-hooks-umenasi --turn-count 1 --queue-mode selected-only --output "$diagnostic_fake_dir/report.json"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_ai_play_turn_diagnostic.py tests/test_ai_play_engine_diagnostic.py tests/test_slovak_ranked_search.py tests/test_api.py tests/test_strength_benchmark.py -q -s
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check game/diagnostics.py game/diagnostic_testbed.py game/management/commands/diagnose_ai_play.py tests/test_ai_play_turn_diagnostic.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py game/diagnostics.py game/diagnostic_testbed.py game/management/commands/diagnose_ai_play.py
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/ai-play-diagnostic.test.ts src/lib/ai-play-diagnostic.worker.test.ts src/lib/ai-play-diagnostic.live.worker.test.ts src/lib/ai-fallback.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts src/lib/prompts.test.ts src/hooks/useGameStore.test.ts
npm run lint
npm run build
8. Proposed commit subject
   feat(diagnostics): add provider-free AI turn CLI
9. Positive authority / Negative authority
   Positive: add the isolated pytest/Vitest composition, fake injection, exact catalog-pair validation, versioned turn evidence, tests, and the one-sentence completion-source documentation repair.
   Negative: no real provider request, credential read, persistent database mutation, already-running server requirement, browser, route/core/prompt edit, fallback-budget edit, fourth lane, localStorage telemetry, or production catalog/cap change.
10. Stop predicates
   Stop if fake mode reaches a provider origin; the harness touches the configured development/production database; direct route import requires a second route or production route mutation; fallback exceeds three pairs; requested IDs are normalized; state/SSE/Move evidence cannot be reconciled; any Unicode or complete-formed-word invariant fails; or the mypy signature gains a new error.
11. Rollback
   Revert the slice commit; its isolated test database and temporary worker files are already teardown-owned, and no migration exists.
12. Residual risks and provider annex
   Fake execution proves mechanics, not provider capability, quota, latency, or model quality. Later provider annex needed: yes, as Slice L under a separate exact-call grant.
Slice L — Separately granted live-provider annex
1. Intent
   Run the shipped Slice T CLI against one exact approved provider/model pair without modifying source. Start with one selected-only canary turn and reconcile every terminal, provider-request count, and Django move before authorizing a larger sample. Produce the same v1 artifact used by fake and future model comparisons.
2. Changed-path allowlist
   None. Only an explicitly requested report under a fresh temporary directory and normal ephemeral test artifacts may be created.
3. Function/symbol edit map
   None; reuse diagnose_ai_play, the live Vitest worker, production runtime resolver, route, fallback orchestrator, SSE parser, and Django verifier.
4. Data/schema changes
   None. The pytest database remains ephemeral. The final JSON report is the sole retained annex artifact.
5. Tests or CLI entrypoints to add
   No additions. Invoke diagnose_ai_play --runtime-mode live with the sentinel and exact granted tuple. Use selected-only; cross-model fallback requires its own explicit multi-provider grant.
6. Tests that must stay green
   Slice E/T’s full provider-free backend and frontend validation remains the preflight gate. A live outcome never replaces those mechanical tests.
7. Validation commands
cd /home/agile/Projects/libretiles/backend
diagnostic_live_dir="$(mktemp -d)"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_ai_play_turn_diagnostic.py tests/test_ai_play_engine_diagnostic.py tests/test_slovak_ranked_search.py -q
LIBRETILES_AI_PLAY_LIVE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode live --timeout-seconds 120 --max-steps 50 --fixture-id slovak-hooks-umenasi --turn-count 1 --queue-mode selected-only --output "$diagnostic_live_dir/report.json"
git status --porcelain
   The future grant must explicitly authorize the chosen provider, exact model, one turn, 120-second deadline, and at most 50 tracked provider requests. It must supply credentials externally without printing, reading, or copying them into reports.
8. Proposed commit subject
   N/A — acceptance-only annex; no source commit.
9. Positive authority / Negative authority
   Positive: one sequential selected-only live turn for the exact granted tuple, bounded by the declared timeout/step budget, with one report.
   Negative: no other provider/model, fallback lane, parallel request, browser, credential probe, source edit, deployment, catalog sync, retry expansion, or additional turn without new authority.
10. Stop predicates
   Stop before traffic if the sentinel, exact tuple, credential authority, clean provider-free preflight, or output path is missing. Stop during execution on an unexpected origin/model, request count above the grant, concurrent or unresolved call, credential exposure, generic unchanged-turn failure, persistence mismatch, unbounded terminal, or inability to classify every request. A coded provider failure is external_incomplete, not a mechanical failure or false pass.
11. Rollback
   Terminate the annex, allow finally teardown of the testbed, and retain the report; no source or product data rollback is required.
12. Residual risks and provider annex
   One canary is causal safety evidence, not a statistically strong model ranking. Further providers, models, fixtures, or turn counts require separately bounded provider grants. Later provider annex needed: no for this slice’s exact canary; broader comparisons remain separately authorized work.
Sequencing and assumptions
- Sequence strictly E → T → L. Accept and commit E before T; run L only after T’s provider-free evidence is accepted.
- Default to fake, selected-only, one independent turn, 120 seconds, and 50 steps.
- catalog-fallback preserves preference-first canonical order and uses buildFallbackQueue, capped at three distinct pairs.
- The exact NIM tuple is an example/default parameter only; schema and CLI model fields are unenumerated strings.
- Search timing and node counts are observational. They do not fail a run unless search itself violates the defined mechanical invariants.
- Existing 12-error mypy output is parked; any additional error is a slice stop.
- The smallest Orchestrator action is to present this plan for Cooperator approval and, if approved, grant Slice E alone to a fresh Implementation Worker with native planning mode off.