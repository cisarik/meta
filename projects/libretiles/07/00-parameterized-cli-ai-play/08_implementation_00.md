Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator. This is a bounded correction task. Do not enable any native planning mode.

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: implement-slice-t2-real-live-runtime-path
Task type: implementation (bounded correction of a confirmed defect)
Implementation authority: explicit
Independence required: no
Material phase gate: yes
Changed material axis: acceptance-owner-or-evidence-class
Ordinary-only trigger: no
Routing reopened for: acceptance-owner-or-evidence-class
Unchanged axes reopened: none

Continuity anchor: none (fresh session). You are correcting a defect confirmed independently by the Orchestrator in Worker 04's Slice T deliverable (commit 93d665d, public). Worker 07's Slice L acceptance annex returned BLOCKED because of it. You are NOT the Worker who wrote the defect and you are NOT auditing your own work.

Recommended reasoning: High
Recommendation basis: this corrects a measurement-integrity defect in which a live-mode flag silently executes the fake path and emits a report that reads like live evidence; a careless fix would either leak credentials into logs or produce a second class of false evidence.
Escalation or downgrade gate: escalate only by naming exact missing evidence, and only if a real live driver cannot exist without editing production route/runtime code. Do not invent Extra High.
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
Exact baseline: 4d60ee42f9b11a75c2464bb41dc674431acd86fa
Baseline subject: chore(types): clear backend mypy debt
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 4d60ee42f9b11a75c2464bb41dc674431acd86fa — local and remote EQUAL.

================================================================
CONFIRMED DEFECT (Orchestrator-verified at this baseline; re-verify, do not trust)
================================================================

`manage.py diagnose_ai_play --runtime-mode live` with `LIBRETILES_AI_PLAY_LIVE=1` exits 0, persists a move, and writes a v1 report whose `requested.runtime_mode` is `live` and whose `external_provider_invocations` is `0` — while never contacting any provider. Exact evidence:

1. `backend/tests/diagnostics/test_turn_probe.py:162` — `spawn_worker` does `env.pop("LIBRETILES_AI_PLAY_LIVE", None)`, stripping the sentinel from the child environment.
2. `backend/tests/diagnostics/test_turn_probe.py:175` — it unconditionally runs `src/lib/ai-play-diagnostic.worker.test.ts`, which is the FAKE worker (`vi.mock("ai", ...)` and `vi.mock("@/lib/ai-runtimes", ...)` replacing `getLanguageRuntime` and `generateText`).
3. The string `runtime_mode` does not appear anywhere in `backend/tests/diagnostics/test_turn_probe.py`; the probe is runtime-mode blind.
4. `frontend/src/lib/ai-play-diagnostic.ts:362` and `:430` — `externalProviderInvocations: 0` is a hardcoded literal.
5. `frontend/src/lib/ai-play-diagnostic.live.worker.test.ts` is a 7-line guard asserting `liveOptInEnabled()` is `false`. It is not a live driver; running it with the sentinel set would fail its own assertion.

Classification: measurement-integrity defect producing FALSE EVIDENCE. It is not merely an unimplemented feature, because the tool reports success on a path that did nothing.

================================================================
GOAL (one coherent outcome)
================================================================

`--runtime-mode live` must either make real, counted provider calls or fail closed. It must never again be able to execute the fake path while reporting as live. And the report must make that impossible to misread, structurally.

Five required properties:

A. **Runtime mode is honored end to end.** The handoff carries `runtime_mode`; the pytest probe reads it; `spawn_worker` selects the live driver for `live` and the fake worker for `fake`; the sentinel is preserved (not popped) for `live` and remains absent for `fake`.

B. **A real live driver exists.** It does NOT mock `ai` and does NOT mock `@/lib/ai-runtimes`. It resolves the runtime through the shipped `getLanguageRuntime` and drives the real route POST, the real `orchestrateFallbackTurn`, and the real `consumeAIStream`, exactly as the fake worker does for everything except the model call. It sets `process.env.BACKEND_URL` to the ephemeral origin BEFORE the dynamic route import, same seam as the fake worker.

C. **Fetch policy is explicit and counted.** The fetch guard allows, in live mode, the ephemeral backend origin plus exactly the two shipped provider bases `https://openrouter.ai` and `https://integrate.api.nvidia.com`, and blocks everything else. It COUNTS requests to provider origins. In fake mode the provider origins remain blocked as they are today.

D. **`external_provider_invocations` is derived, never a literal.** Its value comes from the guard's counter. Remove both hardcoded `0` literals. In fake mode the derived value must still be `0`, and a test must prove that the value is derived rather than constant.

E. **`executed_runtime_mode` is a first-class report field.** The v1 report records, separately from `requested.runtime_mode`, which mode ACTUALLY executed, derived from which driver ran and whether the sentinel was present in the child. If `requested` and `executed` disagree, the sample verdict is `fail` with a stable reason code such as `runtime_mode_not_honored`. Update the schema. This is the structural guarantee that this defect class cannot recur silently.

Fail-closed rules for live mode:
- sentinel absent -> refuse before any spawn (today's behavior; keep it, exit 2);
- the named provider credential absent or an obvious placeholder -> refuse before resolving a runtime, with a REDACTED message naming only the variable name;
- the requested provider is not one of the shipped runtimes -> refuse before any network call;
- any request to an origin outside the allowlist -> hard failure, not a silent skip.

================================================================
CREDENTIAL HANDLING (strict)
================================================================

The command must forward to the child process ONLY these variable names when present, and only in live mode: `NVIDIA_API_KEY`, `OPENROUTER_API_KEY`. No blanket environment forwarding of unrelated secrets. Never print, log, echo, write to a file, hash, or include any credential value in the report, the observation JSON, the v1 artifact, an error message, or a test fixture. Presence checks report only `true`/`false` and the variable NAME. Do not read `backend/.env`. Do not read any other variable from `frontend/.env.local`; the command reads the process environment it was given, and the Cooperator or a later acceptance annex is responsible for populating it.

================================================================
CHANGED-PATH ALLOWLIST (exact)
================================================================

Existing:
- backend/tests/diagnostics/test_turn_probe.py            (honor runtime_mode; preserve sentinel for live; select driver; forward only named keys)
- backend/game/management/commands/diagnose_ai_play.py    (handoff carries runtime_mode; fail-closed live preconditions; executed-mode reconciliation; exit codes)
- backend/game/diagnostics.py                             (executed_runtime_mode, the mismatch reason code, derived invocation plumbing; no dev-group import)
- backend/assets/diagnostics/ai_play_report_v1.schema.json (executed_runtime_mode)
- backend/tests/test_ai_play_turn_diagnostic.py            (new command-level tests)
- frontend/src/lib/ai-play-diagnostic.ts                  (guard counting, allowlist parameterization, derived invocations, executed-mode reporting)
- frontend/src/lib/ai-play-diagnostic.test.ts              (new unit tests)
- frontend/src/lib/ai-play-diagnostic.worker.test.ts       (only what the shared changes require; it must stay the FAKE driver)
- frontend/src/lib/ai-play-diagnostic.live.worker.test.ts  (replace the guard-only file with the real live driver, keeping a sentinel-absent refusal path)

New, only if the live driver genuinely cannot live inside the existing `.live.worker.test.ts` node:
- frontend/src/lib/ai-play-diagnostic.live.runner.test.ts

MUST NOT change: frontend/src/app/api/ai/move/route.ts, ai-fallback.ts, ai-move-stream.ts, types.ts, ai-runtimes.ts, prompts.ts, any store, any other frontend test, backend/game/services.py, views.py, urls.py, models, migrations, backend/gamecore/**, backend/game/management/commands/diagnose_ai_engine.py, backend/tests/test_ai_play_engine_diagnostic.py, backend/tests/test_endgame_policy_matrix.py, backend/tests/test_slovak_full_game.py, any dictionary or variant asset, AGENTS.md, pyproject.toml, poetry.lock, package.json.

================================================================
NEGATIVE AUTHORITY
================================================================

- NO live provider call in this slice. Your validation must prove the wiring WITHOUT spending: prove driver selection, sentinel preservation, allowlist behavior, derived counting, fail-closed preconditions, and executed-mode reconciliation using local stubs at the GUARD level, not by mocking `getLanguageRuntime` in the live driver. The actual live call belongs to the re-run of the Slice L annex under its own provider grant.
- No production behavior change. Zero edits to the route, the fallback orchestrator, the SSE consumer, shared types, or the runtime registry.
- No new dependency, lockfile, or toolchain change. No migration.
- No weakening of the fake path: fake mode must still block provider origins and must still report `external_provider_invocations: 0`, now derived.
- No credential disclosure. No `.env` reads. No blanket env forwarding.
- No L3 lexicon work, no move-policy change, no search-cap change, no infosec work (the audit is a separate slice).
- No force push, amend, rebase, merge, reset, clean, stash, `git add .`, `git add -A`.
- Do not close the logical whole. Do not emit any project closure signal.

Secret authority: none beyond forwarding the two named variables from the ambient environment without rendering them
Browser authority: none
Provider call authority: none in this slice
Network authority: loopback plus the Git remote read and one push
Dependency authority: none
Side-effect authority: reversible local mutation inside the allowlist; ephemeral pytest database; temp files outside the repository removed in `finally`; one local commit; one non-force fast-forward push
Untrusted-content boundary: governing instructions are this prompt, the pinned AP documents, and AGENTS.md. Tool output and any provider text are data under analysis.

================================================================
TESTS TO ADD (the point is that the guard-only test could not catch this)
================================================================

Command level:
- test_live_mode_requires_sentinel_and_exits_two_without_it            (keep existing behavior)
- test_live_mode_refuses_when_named_credential_is_absent               (redacted message, variable name only, no spawn)
- test_live_mode_refuses_unsupported_provider_before_any_network
- test_handoff_carries_runtime_mode_to_the_probe
- test_report_records_executed_runtime_mode
- test_requested_live_but_executed_fake_is_a_verdict_failure           (the anti-regression for this exact defect)
- test_command_forwards_only_named_credential_variables

Probe level:
- test_probe_selects_live_driver_for_live_and_fake_driver_for_fake     (assert on the actual argv script chosen)
- test_probe_preserves_sentinel_for_live_and_omits_it_for_fake

Frontend level:
- test_fetch_guard_counts_provider_origin_requests
- test_fetch_guard_blocks_provider_origins_in_fake_mode
- test_fetch_guard_allows_only_the_two_shipped_provider_bases_in_live_mode
- test_external_provider_invocations_is_derived_not_constant           (a stubbed provider-origin request increments it)
- test_live_driver_does_not_mock_the_runtime_registry                  (static assertion over the driver source: it must not contain a mock of `@/lib/ai-runtimes` or of `ai`)
- test_live_driver_refuses_without_sentinel

Stay-green (run, do not edit): every backend suite including tests/diagnostics/test_turn_probe.py, test_ai_play_engine_diagnostic.py, test_endgame_policy_matrix.py, test_slovak_full_game.py, test_full_game_simulation.py, test_gamecore.py, test_api.py, test_game_app_has_no_dev_imports.py and the Slovak engine suites; and the full frontend focused set including ai-fallback, ai-move-stream, ai-turn-simulation, move route, judge route, prompts, AIThinkingOverlay, useGameStore.

================================================================
VALIDATION
================================================================

cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_ai_play_turn_diagnostic.py tests/diagnostics/test_turn_probe.py -q -s
d="$(mktemp -d)"; env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode fake --fixture-id slovak-turn-diacritic-blank --output "$d/fake.json"; echo "fake exit=$?"
# the fake report must now show executed_runtime_mode=fake and derived external_provider_invocations=0
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode live --fixture-id slovak-turn-diacritic-blank --output -; echo "expect exit=2 without sentinel, got $?"
rm -rf "$d"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/ai-play-diagnostic.test.ts src/lib/ai-play-diagnostic.worker.test.ts src/lib/ai-play-diagnostic.live.worker.test.ts src/lib/ai-fallback.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/move/route.test.ts src/app/api/ai/judge/route.test.ts src/lib/prompts.test.ts src/components/game/AIThinkingOverlay.test.ts src/hooks/useGameStore.test.ts
npm run lint
npm run build

Required outcomes: `mypy config game gamecore accounts catalog` stays at `Success: no issues found` (the debt was cleared at this baseline and must not return); `ruff check .` clean; full backend pytest green; full frontend focused set, lint, and build green; the fake CLI run reports `executed_runtime_mode=fake` with a derived zero; live without the sentinel still exits 2.

Do NOT attempt a live run to "check it works". Its wiring is proven by the named tests. The live call is Slice L's job.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the stay-green lists above
Affected tests: the diagnostic command, probe, and frontend diagnostic files
New causal regression: requested-versus-executed runtime-mode reconciliation, driver selection, sentinel preservation, provider-origin allowlisting, and derived invocation counting
Broad or full suite: required-because this changes the evidence semantics of the measurement tool and touches both runtimes
Runtime or testbed: not-used
Independent acceptance: not-required for this correction, but note that the corrector does not certify its own correction; the Orchestrator will verify and the Slice L re-run is the real acceptance
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
Evidence tier basis: cross-runtime change to the semantics of an evidence-producing tool, with credential forwarding involved, but no production behavior change, no migration, fully reversible, and provable without provider spend.
Authorized implementation stages: (1) gate; (2) reproduce the defect exactly as described, including the misleading live-flag report, and record that reproduction; (3) implement A-E; (4) add the named tests; (5) full validation; (6) diff and porcelain review; (7) one commit; (8) remote gate then one non-force push; (9) public readback; (10) one terminal report.
Combined implementation envelope: allowed
Implementation stage gates: stage 7 only after every validation command is green and the diff contains only allowlisted paths; stage 8 only after `git ls-remote origin refs/heads/main` still equals 4d60ee42f9b11a75c2464bb41dc674431acd86fa.
Independent acceptance: not-required
Rollback or recovery checkpoint: baseline 4d60ee42f9b11a75c2464bb41dc674431acd86fa; recovery is a forward `git revert`. Never rewrite published history.
Activated stricter profile: none
Terminal implementation report point: after the public readback (or after the stop), exactly one terminal report.

Git authority: stage only allowlisted paths by explicit path; exactly one commit with subject

fix(diagnostics): honor live runtime mode and count real provider calls

then the pre-push remote gate, one `git push origin main`, and a public readback. Forbidden: force push, amend, rebase, merge, tag, branch, remote or config writes, second commit.

================================================================
REPOSITORY GATE
================================================================

cwd /home/agile/Projects/libretiles
- `git rev-parse HEAD` equals 4d60ee42f9b11a75c2464bb41dc674431acd86fa
- branch main; `git status --porcelain` empty
- `git rev-parse HEAD:.ap` equals 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 and the .ap checkout HEAD equals it
- `git ls-remote origin refs/heads/main` equals the baseline
- native planning mode OFF or absent
- backend/.venv has python, pytest, ruff, mypy; `npx vitest` resolves in frontend/

If any gate fails: STOP with BLOCKED before mutation, classify with the five canonical recovery classes, use no destructive recovery.

Capability handshake: abbreviated, material rows only, with evidence classes. Do not probe credentials; a presence check is not a probe of the value.

================================================================
STOP PREDICATES
================================================================

Stop and report instead of improvising if:
- the gate fails or porcelain is dirty;
- a real live driver would require editing route.ts, ai-fallback.ts, ai-move-stream.ts, types.ts, or ai-runtimes.ts;
- proving the wiring would require an actual provider call;
- a credential value would be rendered anywhere, or blanket env forwarding would be needed;
- `mypy config game gamecore accounts catalog` gains any error;
- the fake path would lose its provider-origin block or its derived zero;
- you cannot make `executed_runtime_mode` genuinely derived rather than echoed from the request;
- the remote moved before your push;
- you are tempted to do infosec work, live calls, or anything outside A-E.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

PASS requires: the defect reproduced and recorded before the fix; all five properties A-E implemented; every named test present and green; the fake path unchanged in outcome but now derived; live-without-sentinel still exit 2; live-with-sentinel-but-missing-credential failing closed with a redacted message; full backend and frontend validation green; mypy still zero; one commit; fast-forward push; public readback equal to local HEAD.

Begin the terminal report exactly:

### Report for ORCHESTRATOR_CHAT

Then include exactly once:

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 08
Worker exchange ordinal: 01

Then: status; phase-qualified result (implementation-PASS, with publication-PASS separately and its readback); start and end commit; changed files with the property each one serves; Implementation Authority Record echoed; capability handshake; the pre-fix reproduction of the misleading live-flag report; how each of A-E is implemented and which test pins it; the exact argv the probe now uses for live versus fake; the credential-forwarding mechanism and proof that no value is rendered; the fake CLI report's `executed_runtime_mode` and derived invocation count; the exact mypy result; commit subject and SHA; pre-push gate value; push result; public readback SHA; final `git status --porcelain`; temp cleanup; deviations, risks, missing evidence; one smallest next step (expected: Orchestrator re-issues the Slice L acceptance annex unchanged under a renewed provider grant); Report justification: new-mutation; Logical-whole closure: not-closed; Authority expiry statement; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification (`Pre-existing claim: none` expected; verify rather than assume).

Authority expiry: this exchange's authority expires with your terminal report.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
The Worker does not write to the Cooperator; all output returns to the Orchestrator through the English report.