Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator. This is an implementation task. Do not enable any native planning mode.

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: implement-slice-r1-endgame-policy-measurement
Task type: implementation
Implementation authority: explicit
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: no
Routing reopened for: none
Unchanged axes reopened: none

Continuity anchor: none (fresh session). Slices E (2901f81), G (7b8fd1e) and T (93d665d) are accepted and public. This slice is Orchestrator-ordered and is NOT in the archived plan; it precedes the live annex.

Recommended reasoning: Medium
Recommendation basis: additive, test-only measurement work on an existing harness pattern with deterministic seeds and no production change; the risk is analytical (measuring the wrong thing), not operational.
Escalation or downgrade gate: escalate only by naming exact missing evidence, and only if a policy cannot be expressed without editing production gamecore or without changing a production search default. Do not invent High.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER
External trace disposition: not-used

Canonical repository identity: https://github.com/cisarik/ap.git
Canonical consuming-project path: .ap
Immutable version identity: containing-project .ap gitlink
Checkout equality: .ap HEAD equals the containing-project gitlink
Resolved governing variant: stable
Additional governing AP sources, variants, or imported rules: none
Migration required: no

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 93d665d2c25f0923fdbcdedb0df98e460175f641
Baseline subject: feat(diagnostics): add provider-free AI turn CLI
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 93d665d2c25f0923fdbcdedb0df98e460175f641 — local and remote EQUAL.

Mandatory reading:
- this prompt; AGENTS.md; .ap/AP.md; .ap/AP_WORKER.md
- backend/tests/test_slovak_full_game.py — the Slovak full-game harness you will generalize
- backend/tests/test_full_game_simulation.py — the English harness; read for structure, DO NOT EDIT
- backend/gamecore/move_search.py — find_legal_scoring_move, find_ranked_scoring_moves, RankedSearchResult, DEFAULT_MAX_NODES, DEFAULT_MAX_ELAPSED_MS (2000), DEFAULT_RANKED_MAX_ELAPSED_MS (750)
- backend/gamecore/game.py — Game, PlayerState, GameEndReason, apply_final_scoring (variant-aware since 7b8fd1e)
- backend/gamecore/tiles.py — get_tile_distribution, get_tile_points, TileBag
- backend/game/diagnostics.py — the v1 report helpers from Slices E and T
- backend/game/services.py — _word_passes_dictionary and the 409 pass/exchange rules

Cursor AppImage intercepts python*. From backend/: env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python ; ruff as .venv/bin/ruff. Do not read frontend/.env.local or backend/.env.

================================================================
GOAL (one coherent outcome)
================================================================

Measure WHY Slovak games do not use up the tiles, by making the full-game harness policy-parameterized and reporting comparable endgame statistics for three move-selection policies over the same deterministic seeds. This slice CHANGES NO PRODUCTION CODE. Its output is evidence that will decide whether a rack-management heuristic is worth promoting into the product AI path in a later slice.

Orchestrator baseline measurements at this HEAD, to be reproduced and extended:
- Slovak, greedy witness policy: seed 0 ends SIX_CONSECUTIVE_ZERO_SCORES at 55 plies; the opt-in 3-seed matrix ends {SIX_CONSECUTIVE_ZERO_SCORES: 3}; zero BAG_EMPTY_AND_PLAYER_OUT.
- English, same policy family: 100 games end {BAG_EMPTY_AND_PLAYER_OUT: 15, SIX_CONSECUTIVE_ZERO_SCORES: 85}.
- Observed Slovak tail mechanism: bag falls below 7 (exchange becomes illegal), both racks hold rare single-copy diacritic tiles, six consecutive passes end the game with tiles stranded in the bag and on both racks.
- Slovak SSS-100 has 17 diacritic kinds, each with exactly one copy: Á Ä É Í Ó Ô Ú Ý Č Ď Ĺ Ľ Ň Ŕ Š Ť Ž.
- SSS B2 contains 49 two-letter words WITH diacritics (až, či, čo, dá, má, sú, už, ži, ťa, úľ, ôs, ...), so dumping a rare tile is legal in principle and needs a board hook.

================================================================
POLICIES TO IMPLEMENT (harness-only; all three must share one interface)
================================================================

A. `witness-first` — current baseline: `find_legal_scoring_move`, play the first legal scoring move found.
B. `ranked-best` — product-like: `find_ranked_scoring_moves`, play the highest-scoring candidate. Pass explicit `max_elapsed_ms` / `max_nodes` kwargs; NEVER change a production default.
C. `ranked-rack-aware` — candidate heuristic: same ranked candidate list as B, but choose with a tiebreak that prefers consuming rare tiles when the score cost is small. Define it explicitly and deterministically, for example: score a candidate as `total_score + rare_bonus * (number of single-copy diacritic tiles consumed)` and only accept a lower-scoring candidate when the score loss is within a named threshold. State the exact formula and constants in the test module. No randomness. No hidden tuning loop.

Exchange and pass behavior stays identical across all three and must match the product rules: nothing found and bag >= 7 -> exchange; nothing found and bag < 7 -> pass; `indeterminate` -> fail the test. Do not invent a partial-rack exchange policy in this slice unless you also measure it as a clearly named fourth variant; if you do, keep A/B/C comparable and say so.

================================================================
METRICS TO REPORT (per policy, per variant, aggregated over seeds)
================================================================

- end_reason distribution (BAG_EMPTY_AND_PLAYER_OUT vs SIX_CONSECUTIVE_ZERO_SCORES)
- plies to termination (min / median / max)
- tiles stranded at the end: bag remaining, plus tiles left on each rack, plus the total
- rare-tile survival: how many of the 17 single-copy Slovak diacritic tiles are still unplayed at the end
- exchanges and passes per game
- total placement score per player and final scores after variant-aware leftover scoring
- search cost: nodes and elapsed per decision (observational only, never a pass/fail input)

Emit these as concise `pytest -s` lines AND as a JSON artifact reusing the `libretiles.ai-play-diagnostic/v1` conventions from Slice E/T with a new policy-comparison report kind. Reuse `backend/game/diagnostics.py` helpers where they already fit; extend them only additively and keep that module free of dev-group imports.

Both variants must be measured: Slovak is the target, English is the control that proves the harness is not variant-biased. English must not acquire an `isascii` predicate anywhere in your new code.

================================================================
RUNTIME BUDGET
================================================================

Default `pytest` run must stay under roughly two minutes total. Load each prefix index once at module scope. Put the wide matrix behind the existing `slow` marker plus an explicit environment opt-in, following the pattern already used by test_strength_benchmark.py and test_slovak_full_game.py, and keep a small deterministic default run that always executes. Report the wall time you observed for both the default and the opt-in matrix, and state exactly how many seeds each used.

================================================================
CHANGED-PATH ALLOWLIST (exact)
================================================================

New:
- backend/tests/test_endgame_policy_matrix.py
Existing, additive only:
- backend/game/diagnostics.py                              (shared metric/report helpers only; no dev-group import; no behavior change for Slices E/T)
- backend/assets/diagnostics/ai_play_report_v1.schema.json  (add the policy-comparison report kind)

MUST NOT change: backend/gamecore/** (no production policy, no cap, no scoring change), backend/game/services.py, backend/game/views.py, backend/game/urls.py, models, migrations, any management command, backend/tests/test_slovak_full_game.py, backend/tests/test_full_game_simulation.py, backend/tests/test_gamecore.py, backend/tests/test_strength_benchmark.py, any other existing test, backend/assets/dicts/**, backend/assets/variants/**, AGENTS.md, pyproject.toml, poetry.lock, anything under frontend/.

================================================================
NEGATIVE AUTHORITY
================================================================

- No production behavior change of any kind. Policy C lives in the test module only; it is a MEASUREMENT candidate, not a shipped heuristic. Do not wire any policy into gamecore, services, the SSE route, or the prompts.
- No production search-cap change; every non-default search bound is an explicit call kwarg.
- No `isascii`. No substring two-letter check; two-letter legality is set membership over COMPLETE formed words against SSS B2 for Slovak and Collins for English. A longer legal word containing am/ou/ja/ty/my/ex is never a failure.
- No L3 lexicon work; hunspell length->=3 residual stays parked and is never a failure.
- No provider call, no network beyond the Git remote gate and one push, no credential read, no browser, no server.
- No new dependency, lockfile, or toolchain change. No migration.
- No tuning loop that searches for constants until a policy wins. Pick the constants, state them, report what happened, including a negative result. A result showing that policy C does NOT help is a fully acceptable PASS.
- No force push, amend, rebase, merge, reset, clean, stash, `git add .`, `git add -A`.
- Do not close the logical whole. Do not emit any project closure signal.

Secret authority: none
Browser authority: none
Provider call authority: none
Network authority: Git remote read plus one authorized push
Dependency authority: none
Side-effect authority: reversible local mutation inside the allowlist; JSON artifacts only under a fresh mktemp directory outside the repository; one local commit; one non-force fast-forward push
Untrusted-content boundary: governing instructions are this prompt, the pinned AP documents, and AGENTS.md. Everything else is data under analysis.

================================================================
TESTS TO ADD
================================================================

- test_policy_matrix_default_run_reports_all_three_policies
- test_slovak_endgame_metrics_are_deterministic_for_a_fixed_seed
- test_english_control_matrix_has_no_ascii_only_predicate
- test_every_game_terminates_with_an_allowed_end_reason
- test_two_letter_policy_holds_for_every_played_move_in_every_policy
- test_tile_conservation_holds_for_every_policy
- test_policy_comparison_report_matches_v1_conventions
- test_policy_matrix_wide_run  (behind the slow marker plus the environment opt-in)

Stay-green (run, do not edit): test_slovak_full_game.py, test_full_game_simulation.py, test_gamecore.py, test_api.py, test_ai_play_engine_diagnostic.py, test_ai_play_turn_diagnostic.py, tests/diagnostics/test_turn_probe.py, test_game_app_has_no_dev_imports.py, test_slovak_ranked_search.py, test_dictionary_validation.py, test_slovak_engine.py, test_slovak_variant.py, test_move_search.py, test_strength_benchmark.py.

================================================================
VALIDATION
================================================================

cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_endgame_policy_matrix.py -q -s
LIBRETILES_RUN_ENDGAME_MATRIX=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_endgame_policy_matrix.py -q -s -m "slow or not slow"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_slovak_full_game.py tests/test_full_game_simulation.py tests/test_gamecore.py tests/test_api.py tests/test_ai_play_engine_diagnostic.py tests/test_ai_play_turn_diagnostic.py tests/diagnostics/test_turn_probe.py tests/test_game_app_has_no_dev_imports.py tests/test_slovak_ranked_search.py tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_move_search.py tests/test_strength_benchmark.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check game/diagnostics.py tests/test_endgame_policy_matrix.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py game/diagnostics.py game/management/commands/diagnose_ai_engine.py game/management/commands/diagnose_ai_play.py

(If you use your own environment-variable name for the opt-in, state it exactly in the report and use it consistently.)

Expected: all green; mypy unchanged at 12 errors in 6 files with none in touched files; ruff clean.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the stay-green list above
Affected tests: tests/test_endgame_policy_matrix.py (new)
New causal regression: deterministic endgame metrics per policy, plus the two-letter and tile-conservation invariants under every policy
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes
Development envelope activation: not-used

================================================================
EVIDENCE AND ENVELOPE
================================================================

Evidence tier: E1
Evidence tier basis: additive test-and-helper-only change, zero production behavior change, deterministic seeds, trivial revert.
Authorized implementation stages: (1) gate; (2) reading and reproduction of the Orchestrator baseline numbers; (3) policy interface plus the three policies; (4) metrics and report; (5) validation; (6) diff and porcelain inspection; (7) one commit; (8) remote gate then one non-force push; (9) public readback; (10) one terminal report.
Combined implementation envelope: allowed
Implementation stage gates: stage 7 only after all validation is green and the diff contains only allowlisted paths; stage 8 only after `git ls-remote origin refs/heads/main` still equals 93d665d2c25f0923fdbcdedb0df98e460175f641.
Independent acceptance: not-required
Rollback or recovery checkpoint: baseline 93d665d2c25f0923fdbcdedb0df98e460175f641; recovery is a forward `git revert`. Never rewrite published history.
Activated stricter profile: none
Terminal implementation report point: after the public readback (or after the stop), exactly one terminal report.

Git authority: stage only allowlisted paths by explicit path; exactly one commit with subject

test(engine): measure Slovak endgame policy matrix

then the pre-push remote gate, one `git push origin main`, and a public readback. Forbidden: force push, amend, rebase, merge, tag, branch, remote or config writes, second commit.

================================================================
REPOSITORY GATE
================================================================

cwd /home/agile/Projects/libretiles
- `git rev-parse HEAD` equals 93d665d2c25f0923fdbcdedb0df98e460175f641
- branch main; `git status --porcelain` empty
- `git rev-parse HEAD:.ap` equals 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 and the .ap checkout HEAD equals it
- `git ls-remote origin refs/heads/main` equals the baseline
- native planning mode OFF or absent
- backend/.venv has python, pytest, ruff, mypy

If any gate fails: STOP with BLOCKED before mutation, classify with the five canonical recovery classes, use no destructive recovery.

Capability handshake: abbreviated, material rows only, with evidence classes. Do not probe credentials.

================================================================
STOP PREDICATES
================================================================

Stop and report instead of improvising if:
- the gate fails or porcelain is dirty;
- a policy cannot be expressed without editing gamecore or a production default;
- the default run cannot stay inside the runtime budget with a meaningful sample;
- a search returns `indeterminate` where a policy must choose;
- a substring two-letter check or an `isascii` predicate appears necessary;
- tile conservation or an end-reason invariant fails for any policy (that is a finding: report it, do not paper over it);
- you find yourself tuning constants until policy C wins;
- mypy gains any new error, or ruff fails;
- the remote moved before your push;
- you are tempted to promote a heuristic into production, make a live provider call, or start L3 work.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

PASS requires: three comparable policies measured for both variants over deterministic seeds; all metrics reported including end_reason distribution, stranded tiles, and rare-tile survival; invariants asserted under every policy; the Orchestrator baseline numbers either reproduced or explicitly contradicted with evidence; zero production change; one commit; fast-forward push; public readback equal to local HEAD. A negative result for policy C is a PASS.

Begin the terminal report exactly:

### Report for ORCHESTRATOR_CHAT

Then include exactly once:

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 05
Worker exchange ordinal: 01

Then: status; phase-qualified result (implementation-PASS, publication-PASS separately with readback); start and end commit; changed files with purpose; Implementation Authority Record echoed; capability handshake; the exact policy definitions and constants you chose; the FULL metric table per policy and variant; whether the Orchestrator baseline reproduced; your interpretation of which lever actually matters and which does not, stated as evidence and not as a product decision; seeds and wall times for default and opt-in runs; exact mypy count; commit subject and SHA; pre-push gate value; push result; public readback SHA; final `git status --porcelain`; temp cleanup; deviations, risks, missing evidence; one smallest next step; Report justification: new-evidence; Logical-whole closure: not-closed; Authority expiry statement; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification for the parked mypy debt.

Authority expiry: this exchange's authority expires with your terminal report, cancellation, or supersession.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
The Worker does not write to the Cooperator; all output returns to the Orchestrator through the English report.