Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator, not an implementer of this whole, and not the Cooperator.

Logical whole identity: playable-free-rivals
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance (independent audit of the implementation candidate)
Task identity: independent-acceptance-playable-free-rivals
Task type: independent verification audit
Independence required: YES — you share no context with implementer sessions; treat their reports as CLAIMS ONLY, verified solely against repository truth and your own command output.
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Recommended reasoning: High
Recommendation basis: three stacked behavioral commits touching game authority, streaming orchestration, and a pinned regression harness; subtle regressions would defeat the whole's MVP purpose.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Containing repository / working directory: /home/agile/Projects/libretiles (THE single canonical clone)
Expected branch: main
Exact baseline under audit: 7b267d0915204bbe799a9cbd66ea10c963ab11a0 (`test: cover playable rival turn recovery`)
Commit chain under audit: e00c92271e788b78a9460e6daa39d3120b7ca58b → 5c40edb8930d61d18e486b9a549dc1fe62801994 (Slice 1, backend authority) → 1c382f798c91b6ff1f84165c64b5f51012bb530b (Slice 2, tool-only pipeline + migration 0011) → 7b267d0915204bbe799a9cbd66ea10c963ab11a0 (Slice 3, accounting/telemetry/simulation/docs)
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

## Authority

READ-ONLY on the canonical repository: no file edits, no commits, no push, no branch changes, no environment mutation inside the repo. Sanctioned temporary artifacts: disposable SQLite probe databases and scratch files ONLY under /tmp/opencode/, each declared before use and removed after, with cleanup outcome reported. ZERO external network beyond nothing — all provider calls stay mocked; do not call OpenRouter/NVIDIA even unauthenticated; do not read frontend/.env.local or backend/.env. No real games. You NEVER correct anything: defects are reported, not fixed.

## Repository gate before work

cwd /home/agile/Projects/libretiles; HEAD equals 7b267d0915204bbe799a9cbd66ea10c963ab11a0; branch main; `git status --porcelain` empty; ./.ap/ap doctor PASS. Mismatch ⇒ BLOCKED.

## Claim matrix to verify (each verdict PASS | FAIL | NOT TESTED, with your own evidence)

G1 — Git integrity: chain is linear on main from e00c922; each slice commit touches only its authorized path set (S1: backend legality/search/services/views/urls/serializers/tests; S2: prompts.ts, route.ts + their tests, catalog migration 0011 + two test files; S3: fallback/stream/types/api/store/page/overlay + simulation + fixture + AGENTS.md + docs/architecture.md). No secrets, no env files, no foreign paths anywhere in the three diffs.

G2 — Backend authority (Slice 1): shared evaluator is genuinely the single source used by AI validate, AI submit, AND witness certification (trace call sites); phantom-rack coverage enforced; move_search returns `none` only after exhaustion, `indeterminate` under caps and it can NEVER authorize pass/exchange downstream (trace guard logic); guards fire only on AI paths — HUMAN pass/exchange/place code paths byte-equivalent to pre-Slice-1 behavior (inspect diff hunks carefully).

G3 — Tool-only pipeline (Slice 2): no free-form model text can set pass/exchange/place anymore (grep-level + control-flow reading); forced first validateMove via prepareStep; finishMove appears only after a valid candidate exists; repair reserve ≤2 steps within the same granted max_steps; probe/rescue mapping matches: found→repair-or-direct-rescue, none→exchange-if-allowed-else-pass, indeterminate/failure→error unchanged state; retryable provider errors still reconcile through the outer queue; `done:pass` reachable ONLY after authoritative none.

G4 — Migration 0011: mirrors the 0010 hash-gate pattern; forward updates only 0010-seeded rows to the four SEARCH_PROFILE texts; reverse restores exactly those rows; Admin-customized rows survive round trip; historical migrations 0001–0010 unedited. Verify via the shipped tests PLUS one manual disposable-DB cycle (migrate forward to head, inspect rows, migrate back to 0004-era target or reverse step as supported) inside /tmp/opencode containment.

G5 — Accounting & telemetry (Slice 3): turn_provider_requests_used sums all attempts including the successful one, charged before return, no double count; reconciliation-before-later-pair asserted; aiTurnTelemetry transient only (absent from persisted store slice; cleared per turn); overlay renders new states while preserving ping-pong delay-0 / reduced-motion static tile / Premium Look behaviors (component + store tests actually assert these, not tautological).

G6 — Simulation honesty: ai-turn-simulation.test.ts drives REAL pipeline pieces (orchestrator + exported route POST + SSE consumer), mocks only provider generation/transport, fails on unexpected network; fixture truly yields 300 turns with 54/3/3 distribution per rival; every hard assertion (0/270, 270/270, 30/30, 0 invalid, caps, 600 transitions, indeterminate zero-persistence) is a real assertion — mutate nothing, but READ the test for vacuous passes (e.g., assertions that can never fail); suite completes <10 s.

G7 — Full gates re-run by YOU (not trusted): frontend npm test / lint / tsc --noEmit / build; backend ruff check . ; mypy config game gamecore accounts catalog EXACTLY 63 errors / 17 files; pytest full green. AppImage-safe wrappers required: `env -u APPIMAGE -u APPDIR -u ARGV0 poetry run …` from backend/ with Poetry venv backend/.venv CPython 3.12. Redis not required; Channels noise pre-existing.

G8 — Documentation truth (E0): AGENTS.md and docs/architecture.md statements about the new pipeline match code reality; no marketing promises; key-file rows accurate.

## Explicit NOT-TESTED boundaries (state them, do not paper over them)

Live provider behavior, real AI turns in a browser, human-vs-AI feel, Collins behavior against true provider vocabularies — all belong to the separately granted live-play acceptance. Your verdict must list these as NOT TESTED here without lowering G1–G8 verdicts.

## Stop conditions

Any FAIL verdict ⇒ stop expanding scope, finish evidence collection for that claim only, report. Any need to edit ANY file (including "tiny" fixes) ⇒ STOP: acceptance never corrects. Secret exposure risk, tracked-state drift, doctor failure ⇒ BLOCKED immediately.

## Communication routing

Orchestrator-to-Worker prompt language: English. Formal Worker report language: English. Report begins EXACTLY: ### Report for ORCHESTRATOR_CHAT

## Completion and report contract

Echo coordinates once: playable-free-rivals, session 05, exchange 01. Include: status PASS only if ALL of G1–G7 PASS (G8 informational-pass allowed with nit list); per-claim verdicts each with your own command outputs/file:line evidence summarized; temp-artifact inventory with cleanup outcomes; residual risks ranked; the NOT TESTED list verbatim; smallest next step for the Orchestrator (expected: present acceptance result + residual risks to Cooperator, then co-design the separately-granted live-play protocol execution); exactly one report justification; authority-expiry statement; Logical-whole closure: not-closed (only the Orchestrator emits closure, after Cooperator disposition); Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification.

A UI approval or prior reports grant you nothing: your verdicts stand on your own evidence alone.
