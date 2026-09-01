Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator. This is an implementation task on the most sensitive file in the product. Do not enable any native planning mode.

Logical whole identity: slovak-playable-latency
Prior logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: implement-no-provider-progress-deadline
Task type: implementation
Implementation authority: explicit
Independence required: no
Material phase gate: yes
Changed material axis: primary-objective
Ordinary-only trigger: no
Routing reopened for: primary-objective
Unchanged axes reopened: none

This is a NEW logical whole. `parameterized-cli-ai-play` delivered the measurement infrastructure (engine probe, turn CLI, policy matrix, honest live mode) and its live canary produced the evidence that motivates this whole. That prior whole is not closed and is not your concern beyond its shipped tooling, which you will use as your instrument.

Continuity anchor: none (fresh session). All prior reports are subordinate evidence.

Recommended reasoning: High
Recommendation basis: this changes turn finalization inside frontend/src/app/api/ai/move/route.ts, the single file that owns legality-critical commit decisions, the tool-only pipeline, the repair reserve, and completion-source semantics; a careless change could commit an unvalidated move, break the pass/exchange prohibition, or corrupt provider accounting.
Escalation or downgrade gate: escalate only by naming exact missing evidence, and only if the deadline cannot be implemented without weakening backend validation or changing the fallback contract. Do not invent Extra High.
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
Exact baseline: b18e50eb56d90fe65d95670c48b1d32d16bd3721
Baseline subject: fix(diagnostics): honor live runtime mode and count real provider calls
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: b18e50eb56d90fe65d95670c48b1d32d16bd3721 — local and remote EQUAL.

Mandatory reading before mutation:
- this prompt; AGENTS.md; .ap/AP.md; .ap/AP_WORKER.md
- frontend/src/app/api/ai/move/route.ts IN FULL. Specifically: DEFAULT_TIMEOUT_S (41), DEFAULT_MAX_STEPS (42), AUTO_FINALIZE_GRACE_MS (48), AUTO_FINALIZE_VALID_CAP (49), EXTENDED_AUTO_FINALIZE_GRACE_MS (50), EXTENDED_AUTO_FINALIZE_VALID_CAP (51), REPAIR_RESERVE_STEPS (52), REPAIR_MIN_REMAINING_SECONDS (53); the `autoFinalized` / `autoFinalizeTimer` / `abortReason` state (491-496); `rankedCandidatePromise` and its eager backend GET (506-517); the validity-gated auto-finalize block (~576-590); the terminal emit with `timed_out` and `auto_finalized` (~714); `useExtendedSearchBudget` (1106-1110); `commitBestAvailable`; `probeAndResolve` and its `allowProviderRepair`; the generic catch and its bounded `ai_move_internal_error` / `backend_rescue_error`
- frontend/src/lib/ai-fallback.ts — attemptTimeoutSeconds, attemptStepGrant, MIN_ATTEMPT_TIMEOUT_SECONDS, MAX_FALLBACK_ATTEMPTS
- frontend/src/lib/ai-move-stream.ts and types.ts — terminal parsing, AiTurnTelemetry, describeAiMoveFailure
- frontend/src/hooks/useGameStore.ts — aiTimeout 120 / aiMaxSteps 50 defaults and persistence
- frontend/src/app/api/ai/move/route.test.ts — all existing expectations you must keep green
- frontend/src/lib/ai-turn-simulation.test.ts — the 300-turn causal simulation

Cursor AppImage intercepts python*. From backend/: env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python . Frontend uses npx vitest / npm from frontend/. Do not read frontend/.env.local or backend/.env.

================================================================
MEASURED MOTIVATION (Orchestrator-verified; re-verify the code claims)
================================================================

Live acceptance evidence from four completed provider-backed turns against `nvidia/nemotron-3-super-120b-a12b` at this baseline:

- wall-clock per turn: 134 s, 138 s, 124 s, 124 s
- provider requests per turn: 2, 1, 3, 1 — no turn exhausted the 50-step grant
- completion_source: `backend_ranked_candidate` on all four
- `provider_candidate`: ZERO, in Slovak and in English
- persisted words: SČÍTALO 82, OSAMENIU 74, SOĽNÁ 22, OUTLAIN 66; no stale_witness; no generic unchanged-turn; no pass or exchange while probe `found`

Code mechanism, Orchestrator-observed at this baseline: auto-finalize is gated behind the MODEL producing backend-valid candidates. `validCount >= autoFinalizeValidCap` or the grace timer both require at least one valid provider candidate first. When the model never produces one, no auto-finalize fires and the attempt burns its entire granted timeout before the route commits the ranked candidate that was already fetched eagerly. Ranked search itself costs on the order of 150 ms.

Consequence for the product: with the shipped defaults (aiTimeout 120, aiMaxSteps 50, which also force `useExtendedSearchBudget`), every AI turn costs roughly the full timeout. A 29-ply Slovak game means about fifteen AI turns, so roughly half an hour of dead waiting. The game is legally correct and practically unplayable.

================================================================
GOAL (one coherent outcome)
================================================================

An AI turn must stop paying for a model that is making no progress, while keeping every legality and authority guarantee exactly as it is today.

Introduce a NO-PROVIDER-PROGRESS DEADLINE with these semantics:

1. Start a deadline when the attempt begins.
2. If, at deadline expiry, the model has produced ZERO backend-valid candidates for this attempt AND a backend-valid ranked candidate is available, finalize the turn immediately with that ranked candidate.
3. If the model has produced at least one backend-valid candidate, the deadline does not fire; the existing auto-finalize logic (valid-count cap and grace timer) continues to own that path unchanged.
4. If no ranked candidate is available at expiry, the deadline does NOT fire; the attempt continues under the existing timeout so the existing playability/witness/exchange/pass resolution can still run. Never turn a no-progress deadline into a pass, an exchange, or an unvalidated commit.
5. The existing `aiTimeout` remains the hard upper bound. The deadline can only make a turn finish sooner, never later.

Parameterization:
- A named constant with a default. Recommended default: 20 seconds. Justify whatever you choose against the live evidence (the model used 1-3 requests over ~130 s, so a first valid candidate would have to arrive within a few tens of seconds to be useful).
- Overridable per request through the existing request body, clamped to a sane range, in the same style as `timeout` and `max_steps` are handled today. Do not add a new endpoint or a new SSE event type.
- Scale it sensibly relative to the granted attempt timeout: the deadline must never exceed the attempt's own timeout, and must leave the repair reserve and `REPAIR_MIN_REMAINING_SECONDS` intact.

Observability, required:
- The SSE terminal must carry a truthful `terminal_cause` distinguishing this path, for example `no_provider_progress_deadline`, while `completion_source` stays `backend_ranked_candidate` because that is factually what was committed.
- The transient telemetry the overlay already renders must be able to explain it in human terms. Keep it transient; never persist telemetry to localStorage or any store.
- Provider accounting must stay exact: requests actually made are still counted; an aborted in-flight model call must not be counted as a successful request and must not be double counted.

================================================================
HARD INVARIANTS (any violation is a stop)
================================================================

- Nothing is ever committed without backend validation. The tool-only pipeline stands: free-form model text still has no authority over place, pass, or exchange.
- Pass or exchange remains impossible while authoritative playability is `found` or `indeterminate`. The backend 409 contract (`legal_scoring_move_exists`, `playability_unknown`, `exchange_required`) is untouched.
- `MAX_FALLBACK_ATTEMPTS` stays 3. Retryable-failure semantics, unchanged-turn reconciliation, and the whole-turn provider budget stay as they are.
- The six `completion_source` values are unchanged. Do not add a seventh.
- English behavior must not regress. Collins path, ranked rescue, and the CORE pin stay identical: SHA-256 c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60, version pfr-s2-core-1. Do not touch prompts.ts. Do not bump MOVE_PROMPT_VERSION.
- No second SSE route. No production search-cap change. No backend change of any kind.
- Unicode NFC handling in `normalizePlacementData` is untouched.
- No credential read, no provider call in your validation, no browser, no server.

================================================================
CHANGED-PATH ALLOWLIST (exact)
================================================================

- frontend/src/app/api/ai/move/route.ts          (the deadline, its wiring, the terminal cause)
- frontend/src/app/api/ai/move/route.test.ts     (new deterministic tests)
- frontend/src/lib/types.ts                      (only if a terminal-cause copy string is needed for the overlay; no new completion source, no persisted field)
- frontend/src/lib/ai-move-stream.ts             (only if the terminal cause needs to be surfaced; no schema break)
- frontend/src/lib/ai-move-stream.test.ts        (coverage for the above)
- frontend/src/lib/ai-turn-simulation.test.ts    (extend the causal simulation to cover a no-progress model)
- AGENTS.md                                      (at most two sentences documenting the deadline and its default)

MUST NOT change: frontend/src/lib/prompts.ts, ai-fallback.ts, ai-runtimes.ts, useGameStore.ts, any component, any backend file, any asset, any diagnostic file under backend/game/diagnostics.py or backend/tests/**, pyproject.toml, package.json.

If you conclude the store default `aiTimeout` should also change, do NOT change it. Report it as a recommendation; that is a Cooperator-owned product decision.

================================================================
TESTS TO ADD (deterministic, provider-free)
================================================================

- test_no_progress_deadline_commits_ranked_candidate_when_model_produces_nothing
- test_deadline_does_not_fire_when_model_produced_a_valid_candidate
- test_deadline_does_not_fire_without_a_ranked_candidate
- test_deadline_never_causes_pass_or_exchange_while_probe_found
- test_deadline_terminal_reports_backend_ranked_candidate_with_no_progress_cause
- test_deadline_respects_repair_reserve_and_hard_timeout
- test_deadline_is_clamped_and_never_exceeds_attempt_timeout
- test_provider_accounting_is_exact_when_an_in_flight_call_is_abandoned
- test_english_ranked_rescue_behaviour_is_unchanged_by_the_deadline
- extend ai-turn-simulation.test.ts with a model that never returns a valid candidate, asserting the turn still completes legally, never passes while found, and stays within three lanes

Use fake timers or an injectable clock rather than real waiting; the suite must stay fast. Do not sleep for 20 seconds in a test.

Stay-green (run, do not edit beyond the allowlist): route.test.ts existing cases, ai-fallback.test.ts, ai-move-stream.test.ts, ai-turn-simulation.test.ts, judge/route.test.ts, prompts.test.ts, AIThinkingOverlay.test.ts, useGameStore.test.ts, and the full backend suite including the diagnostics CLIs.

================================================================
VALIDATION
================================================================

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/lib/ai-fallback.test.ts src/app/api/ai/judge/route.test.ts src/lib/prompts.test.ts src/components/game/AIThinkingOverlay.test.ts src/hooks/useGameStore.test.ts
npm run lint
npm run build

cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
d="$(mktemp -d)"; env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode fake --fixture-id slovak-turn-diacritic-blank --output "$d/turn.json"; echo "exit=$?"; rm -rf "$d"

Required: all green; mypy stays `Success: no issues found`; the fake diagnostic CLI still exits 0 with `executed_runtime_mode=fake`, `completion_source=backend_ranked_candidate`, and the Slovak diacritic turn still persisting; the CORE pin test still green.

Do NOT make a live provider call. The real latency win will be confirmed by a separately granted live re-measurement.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the stay-green list above
Affected tests: route.test.ts, ai-move-stream.test.ts, ai-turn-simulation.test.ts
New causal regression: a model that produces no backend-valid candidate must finalize from the ranked candidate before the hard timeout, without pass, exchange, or unvalidated commit
Broad or full suite: required-because this changes turn finalization in the legality-critical route and must be shown not to regress English, the fallback contract, or the diagnostics
Runtime or testbed: not-used
Independent acceptance: recommended — the Orchestrator will verify, and a separately granted live re-measurement is the real acceptance
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

Evidence tier: E2
Evidence tier basis: user-visible behavioral change inside the legality-critical SSE route, reversible, migration-free, credential-free, provable by deterministic provider-free tests plus the existing 300-turn causal simulation.
Authorized implementation stages: (1) gate; (2) read route.ts in full and confirm the validity-gated auto-finalize mechanism yourself; (3) implement the deadline; (4) tests; (5) full validation; (6) diff review; (7) one commit; (8) remote gate then one non-force push; (9) public readback; (10) one terminal report.
Combined implementation envelope: allowed
Implementation stage gates: stage 7 only after all validation is green and the diff is inside the allowlist; stage 8 only after `git ls-remote origin refs/heads/main` still equals b18e50eb56d90fe65d95670c48b1d32d16bd3721.
Independent acceptance: recommended
Rollback or recovery checkpoint: baseline b18e50eb56d90fe65d95670c48b1d32d16bd3721; recovery is a forward `git revert`. Never rewrite published history.
Activated stricter profile: none
Terminal implementation report point: after the public readback (or after the stop), exactly one terminal report.

Git authority: stage only allowlisted paths by explicit path; exactly one commit with subject

feat(ai): finalize turns when the model makes no progress

then the pre-push remote gate, one `git push origin main`, and a public readback. Forbidden: force push, amend, rebase, merge, tag, branch, remote or config writes, second commit.

================================================================
REPOSITORY GATE
================================================================

cwd /home/agile/Projects/libretiles
- `git rev-parse HEAD` equals b18e50eb56d90fe65d95670c48b1d32d16bd3721
- branch main; `git status --porcelain` empty
- `git rev-parse HEAD:.ap` equals 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 and the .ap checkout HEAD equals it
- `git ls-remote origin refs/heads/main` equals the baseline
- native planning mode OFF or absent
- backend/.venv has python, pytest, ruff, mypy; `npx vitest` resolves in frontend/

If any gate fails: STOP with BLOCKED before mutation, classify with the five canonical recovery classes, use no destructive recovery.

Capability handshake: abbreviated, material rows only, with evidence classes. Do not probe credentials.

================================================================
STOP PREDICATES
================================================================

Stop and report instead of improvising if:
- the gate fails or porcelain is dirty;
- the deadline cannot be implemented without weakening backend validation, the tool-only pipeline, or the pass/exchange prohibition;
- it would require changing ai-fallback.ts, prompts.ts, the store, or any backend file;
- a seventh completion source or a new SSE event type would be needed;
- provider accounting could double count or lose an in-flight abandoned call;
- the CORE hash or MOVE_PROMPT_VERSION would change;
- a test would need real 20-second waiting;
- any stay-green suite fails, or mypy or lint or build regresses;
- the remote moved before your push;
- you are tempted to change the store default aiTimeout, make a live call, or touch anything outside the allowlist.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

PASS requires: the mechanism confirmed by your own reading before the change; the deadline implemented with all five semantics and all hard invariants intact; every named test present and green; the full frontend and backend validation green; mypy still zero; the CORE pin unchanged; the fake diagnostic CLI unchanged in outcome; one commit; fast-forward push; public readback equal to local HEAD.

Begin the terminal report exactly:

### Report for ORCHESTRATOR_CHAT

Then include exactly once:

Logical whole identity: slovak-playable-latency
Worker session ordinal: 01
Worker exchange ordinal: 01

Then: status; phase-qualified result (implementation-PASS, publication-PASS separately with readback); start and end commit; changed files with purpose; Implementation Authority Record echoed; capability handshake; your own confirmation of the validity-gated auto-finalize mechanism with exact line references; the chosen deadline default and its justification against the live evidence; how each of the five semantics and each hard invariant is pinned by a named test; the exact terminal cause string introduced; how provider accounting stays exact when an in-flight call is abandoned; validation results including lint, build, backend suite, and mypy; the fake diagnostic CLI outcome; commit subject and SHA; pre-push gate value; push result; public readback SHA; final `git status --porcelain`; deviations, risks, missing evidence, including any recommendation you are NOT authorized to implement such as the store default; one smallest next step (expected: Orchestrator grants a bounded live re-measurement to confirm the latency win, then routes the infosec audit); Report justification: new-mutation; Logical-whole closure: not-closed; Authority expiry statement; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification.

Authority expiry: this exchange's authority expires with your terminal report.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
The Worker does not write to the Cooperator; all output returns to the Orchestrator through the English report.