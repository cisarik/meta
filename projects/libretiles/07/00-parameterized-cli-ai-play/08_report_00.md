### Report for ORCHESTRATOR_CHAT

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 08
Worker exchange ordinal: 01

**Status:** PASS
**Phase-qualified result:** implementation-PASS. **publication-PASS** (public `origin/main` readback equals local HEAD).
**Start commit:** `4d60ee42f9b11a75c2464bb41dc674431acd86fa`
**End commit:** `b18e50eb56d90fe65d95670c48b1d32d16bd3721`

**Changed files (property served):**
- `backend/game/diagnostics.py` — A/D/E: runtime helpers, derived executed mode, mismatch reason `runtime_mode_not_honored`, credential/placeholder plumbing, probe env preparation
- `backend/game/management/commands/diagnose_ai_play.py` — A/E: fail-closed live preconditions, named-key forwarding, reconciliation before report/exit
- `backend/tests/diagnostics/test_turn_probe.py` — A: honor `runtime_mode`, preserve sentinel, select driver argv
- `backend/tests/test_ai_play_turn_diagnostic.py` — A/E: named command-level tests
- `backend/assets/diagnostics/ai_play_report_v1.schema.json` — E: `executed_runtime_mode`
- `frontend/src/lib/ai-play-diagnostic.ts` — C/D: parameterized fetch guard, derived invocation count
- `frontend/src/lib/ai-play-diagnostic.test.ts` — C/D/B: guard, derived count, live-driver source assertion
- `frontend/src/lib/ai-play-diagnostic.worker.test.ts` — D: fake driver stays fake; count derived from guard
- `frontend/src/lib/ai-play-diagnostic.live.worker.test.ts` — B: real live driver (no `ai` / `@/lib/ai-runtimes` mocks) plus sentinel-absent refusal

No `ai-play-diagnostic.live.runner.test.ts` (driver fits in the existing live worker node).

**Implementation Authority Record:** explicit implementation; independence required: no; material phase gate: yes; changed material axis: acceptance-owner-or-evidence-class; ordinary-only trigger: no; routing reopened for: acceptance-owner-or-evidence-class; unchanged axes reopened: none; Worker session profile: Bounded Correction Worker; native planning mode: not-used.

**Capability handshake (abbreviated, material rows):**
- Python/pytest/ruff/mypy: observed via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` — Python 3.12.12, pytest 8.4.2, ruff 0.5.7, mypy 1.19.1 (evidence: local sanitized process). Ambient AppImage `PYTHONHOME` hijack is not a usable Python route.
- `npx vitest`: vitest/4.1.11 (local process).
- Git write/push: authorized; observed `4d60ee4..b18e50e main -> main` (public Git).
- `NVIDIA_API_KEY` / `OPENROUTER_API_KEY`: presence-only, both `false` at session start. Values not read for content.
- Provider calls: none (negative observation). Native planning: not used.

**Pre-fix reproduction (misleading live-flag report):**
`LIBRETILES_AI_PLAY_LIVE=1` `diagnose_ai_play --runtime-mode live --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --fixture-id slovak-turn-diacritic-blank` at baseline `4d60ee4`: **exit 0**; persisted a place; `requested.runtime_mode=live`; no `executed_runtime_mode`; `summary.external_provider_invocations=0`; sample `verdict=pass` / `reason_code=ok`. Credentials were absent, so this was fake-path success reported as live.

**A–E and pinning tests:**
- **A.** Handoff already carried `runtime_mode`; command now fail-closes live; probe reads it; `spawn_worker` selects the live vs fake vitest file; `prepare_probe_environment` sets `LIBRETILES_AI_PLAY_LIVE=1` for live and pops it for fake. Pins: `test_handoff_carries_runtime_mode_to_the_probe`, `test_probe_selects_live_driver_for_live_and_fake_driver_for_fake`, `test_probe_preserves_sentinel_for_live_and_omits_it_for_fake`, `test_live_mode_requires_sentinel_and_exits_two_without_it`.
- **B.** Live worker dynamically imports the real route after `BACKEND_URL`, drives `runDiagnosticTurn` → real POST / `orchestrateFallbackTurn` / `consumeAIStream`, and does not mock `ai` or `@/lib/ai-runtimes`. Pins: `test_live_driver_does_not_mock_the_runtime_registry`, `test_live_driver_refuses_without_sentinel`.
- **C.** Guard allows ephemeral backend always; in live, also `https://openrouter.ai` and `https://integrate.api.nvidia.com` (counted); other origins reject hard; fake still blocks provider origins. Pins: `test_fetch_guard_counts_provider_origin_requests`, `test_fetch_guard_blocks_provider_origins_in_fake_mode`, `test_fetch_guard_allows_only_the_two_shipped_provider_bases_in_live_mode`.
- **D.** Both hardcoded `externalProviderInvocations: 0` literals removed; value is `derivedExternalProviderInvocations(providerOrigins)` (guard counter length). Fake remains 0, now derived. Pin: `test_external_provider_invocations_is_derived_not_constant`.
- **E.** Report-level and sample-level `executed_runtime_mode` derived from driver + sentinel (`live` only if driver is live **and** sentinel present). Mismatch → sample `fail` / `runtime_mode_not_honored`. Pins: `test_report_records_executed_runtime_mode`, `test_requested_live_but_executed_fake_is_a_verdict_failure`.

Fail-closed also pinned: missing named credential (redacted message, variable name only, no spawn) — `test_live_mode_refuses_when_named_credential_is_absent`; unsupported provider before network — `test_live_mode_refuses_unsupported_provider_before_any_network`.

**Exact probe argv:**
- live: `npx vitest run src/lib/ai-play-diagnostic.live.worker.test.ts`
- fake: `npx vitest run src/lib/ai-play-diagnostic.worker.test.ts`

**Credential forwarding:** `prepare_probe_environment` always drops `NVIDIA_API_KEY` and `OPENROUTER_API_KEY`, then re-adds those two names only in live when present in the parent process. Handoff JSON does not include them. Errors name only the variable. Pin: `test_command_forwards_only_named_credential_variables` (values asserted absent from report and handoff).

**Fake CLI after fix:** `executed_runtime_mode=fake`; derived `external_provider_invocations=0`; exit 0. Live without sentinel: **exit 2** (`--runtime-mode live requires LIBRETILES_AI_PLAY_LIVE=1`). No live-with-sentinel run (no provider spend).

**mypy:** `Success: no issues found in 76 source files`. `ruff check .` clean. Full backend pytest green. Frontend focused set 172 passed / 2 skipped (worker-only cases); lint and build green.

**Commit:** `fix(diagnostics): honor live runtime mode and count real provider calls` — `b18e50eb56d90fe65d95670c48b1d32d16bd3721`
**Pre-push gate:** `origin/main` still `4d60ee42f9b11a75c2464bb41dc674431acd86fa`
**Push:** fast-forward `4d60ee4..b18e50e  main -> main` (non-force)
**Public readback:** `b18e50eb56d90fe65d95670c48b1d32d16bd3721` equals local HEAD
**Final porcelain:** empty
**Temp cleanup:** fake CLI temp dir and pre-fix repro dir removed

**Deviations / risks / missing evidence:** None material. Live wiring is proven by driver selection, sentinel preservation, allowlist stubs, derived counting, fail-closed preconditions, and requested-vs-executed reconciliation — not by a provider call. The corrector does not certify its own correction.

**One smallest next step:** Orchestrator re-issues the Slice L acceptance annex unchanged under a renewed provider grant.

Report justification: new-mutation
Logical-whole closure: not-closed
Authority expiry statement: this exchange's authority expires with this terminal report.
Resolved Execution Issues / Near-Misses: unsanitized `.venv` Python is AppImage-hijacked; authorized `env -u APPIMAGE -u ARGV0 -u APPDIR` route was used. Ambient provider keys were absent (`present=false`); live-with-sentinel was still not attempted.
Pre-Existing Failure Classification: `Pre-existing claim: none`