### Report for ORCHESTRATOR_CHAT

Logical whole identity: nim-fallback-free-rivals
Worker session ordinal: 04
Worker exchange ordinal: 01

- status: **PASS**
- phase-qualified result: **acceptance-complete**
- start commit: `56c5d94875a953f5d4634139cc89691c3549a03b`
- end commit: `56c5d94875a953f5d4634139cc89691c3549a03b` (equal to start; no mutation)
- changed files: none tracked (`git status --porcelain` empty before and after)

Capability handshake (abbreviated; capability does not grant authority):
- Plan Mode: **off** (Native planning mode `not-used`; no mode switch)
- Python: CPython via `backend/.venv` with `env -u APPIMAGE -u ARGV0 -u APPDIR`
- Node: Next.js 16.2.0 on `:3000`; Django on `:8000`
- Git: read-only
- Ports: **started** then **stopped** by this Worker (`./scripts/libretiles.sh`); Redis **not** started
- Browser: cursor-ide-browser; origin `http://localhost:3000`
- Classified key presence only:
  - `NVIDIA_API_KEY: configured`
  - `OPENROUTER_API_KEY: configured`
  - values, lengths, prefixes, and redacted fragments: **not printed**

Acceptance and Correction Record:
```text
Acceptance candidate: 56c5d94875a953f5d4634139cc89691c3549a03b
Acceptance owner map: Slice 2 NIM Chat Completions runtime + nested error classification; Django Collins 2019 remains move validator
Acceptance allowlist: none
Acceptance risk claims: live NIM may 429/401; advertised tools may fail; AI SDK inner retries may exceed one HTTP POST; Settings can confuse NIM vs OpenRouter Nemotron
Acceptance control matrix: one POST, NIM pair only, no OpenRouter, no Slice 3 fallback, no secrets in report, zero app credits, Django persistence required
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

Tests and validation:

| Gate | Result |
|---|---|
| Repository gate | **PASS** — HEAD `56c5d94875a953f5d4634139cc89691c3549a03b`, branch `main`, tracked porcelain empty, `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `./.ap/ap doctor` | **PASS**; governing variant **stable** |
| Secret presence probe | NVIDIA **configured**; OpenRouter **configured**; no values printed |
| Catalog GET `http://localhost:8000/api/catalog/models/` | HTTP 200; includes `{provider:"nvidia-nim", model_id:"nvidia/nemotron-3-super-120b-a12b"}` and the distinct OpenRouter `:free` Nemotron row |
| Browser register | **PASS** — throwaway user `nimhpk4w8`; landed `/play` |
| Settings NIM pair | **PASS** — clicked the card whose description is NVIDIA NIM tool calling, not the OpenRouter `:free` twin; `preferred_ai_model_id` and store `selectedModelId` both `nvidia/nemotron-3-super-120b-a12b` |
| AI game create | **PASS** — draw then `/game/66375b64-6b95-4221-b0c2-2416ac5e4c8f`; AI opened (`current_turn_slot` 1, `my_slot` 0); empty history |
| One AI turn | **PASS** — one user-initiated `POST /api/ai/move`; SSE `done` with `ok: true`; Django persisted AI `pass` |
| Billing | `credit_balance` **10.000000** after the turn (same as before); game `total_cost_usd` **0.000000**; `last_move_billing` null; `POST /api/billing/charge-ai-turn/` HTTP 200 |
| Preference after turn | NIM id **unchanged**; not rewritten to an OpenRouter id |
| Server cleanup | **PASS** — `./scripts/libretiles.sh stop`; both stopped |
| Push | **not performed** |

Persisted game after the stream (authenticated GET `/api/game/{id}/`; token not printed):
- `ai_model_id`: `nvidia/nemotron-3-super-120b-a12b`
- `move_count`: **1**
- last history kind: **`pass`** (AI slot 1)
- `current_turn_slot`: **0** (human)
- overlay candidates: **not used as proof**

SSE (redacted to type/code/provider_path/runtime_model/done-vs-error):
- types observed: `thinking`, `thinking`, `tool_use`, `tool_result`, `candidate`, `tool_use`, `tool_result`, `done`
- `thinking`: `provider_path: "nvidia-nim"`, `runtime_model: "nvidia/nemotron-3-super-120b-a12b"`
- `done`: `ok: true`, `action: "pass"`, `provider_path: "nvidia-nim"`, `runtime_model: "nvidia/nemotron-3-super-120b-a12b"`
- no `provider_rate_limited` / `provider_auth_failed` / `provider_unavailable`

This-session Next.js log (after `===== 2026-08-24 20:42:20 :: frontend start =====`):
- `POST /api/ai/move 200 in 61s`
- **zero** `openrouter.ai` lines
- **zero** `integrate.api.nvidia.com` lines (SDK did not print the outbound host on the successful stream)

Django this-turn (hosts only): `POST .../ai-pass/` 200; `POST /api/billing/charge-ai-turn/` 200; tool `validate-move` / `validate-words` 200. Redis was not started; realtime publish logged connection refused to `127.0.0.1:6379` (expected for AI-only).

Provider call authority: authorized for one direct NIM Chat Completions tool-calling turn through Next.js `POST /api/ai/move` using pair `nvidia-nim` / `nvidia/nemotron-3-super-120b-a12b`
Numerical call cap: 1 Worker-originated `POST /api/ai/move` because NVIDIA trial/quota and AI-SDK inner retries can multiply HTTP
Unlimited call authority: no
Concurrency: single-call-in-flight
Terminal outcome before next call: required
Additional call purpose: not applicable unless the single authorized extra POST below
Retry inventory requirement: not-required-inside-authorized-loop
Stop conditions: uncontrolled duplication, credential exposure, unexpected billing, destructive risk, unexplained unrelated mutation, material scope expansion, loss of fixture or privacy guarantee

```text
Provider accounting record: activated
Task or acceptance scope: Slice 2 direct NIM tool turn; throwaway vs-AI game 66375b64-6b95-4221-b0c2-2416ac5e4c8f
Bounded time window: supervisor start 20:42:20 through POST /api/ai/move 61s and supervisor stop
Subject identity: throwaway user nimhpk4w8; local game 66375b64-6b95-4221-b0c2-2416ac5e4c8f
Run or correlation boundary: one POST /api/ai/move SSE from the AI Play prompt
Evidence source: SSE metadata capture (type/code/provider_path/runtime_model/ok/action only); Django GET /api/game/{id}/ and /api/auth/me/; this-session Next.js and Django logs
Evidence freshness: current for this bounded time window
Reconciliation status: open
Accounting authority effect: none
Intended UI submissions: 1
Intended UI submissions relationship: independently varying metric because AI SDK inner NVIDIA HTTP is not one-to-one with the UI click
Actual external provider invocations: unknown because this-session Next.js logs did not print integrate.api.nvidia.com request lines
Actual external provider invocations relationship: not applicable because the NVIDIA HTTP count is missing
Retry attempts: unknown because inner SDK retries were not logged
Retry attempts relationship: not applicable because the NVIDIA HTTP count is missing
Defect-driven duplicate invocations: 0
Defect-driven duplicate invocations relationship: subset of actual external provider invocations
Retry/duplicate overlap: 0
Terminal outcomes: completed=1 failed=0 refused=0 cancelled=0
Terminal outcomes relationship: one-to-one with Worker-originated POST /api/ai/move streams (not proven one-to-one with inner NVIDIA HTTP)
In-flight invocations: 0
Unresolved invocations: 0
Durable provider-submission rows: 1
Durable provider-submission rows relationship: independently varying metric because Django persisted one AI pass after the SSE done; inner NVIDIA HTTP may differ
Analysis-run rows: 0
Analysis-run rows relationship: independently varying metric because Libre Tiles has no analysis-run table for this SSE
Security-audit events: 0
Security-audit events relationship: independently varying metric because no security-audit event is written for this path
Canonical save events: 0
Canonical save events relationship: independently varying metric because no catalog save is part of /api/ai/move
Count divergence: UI submissions 1 versus unknown NVIDIA HTTP because the SDK may retry inside one authorized stream; durable Django row 1 because one pass persisted
Unknown closure for Actual external provider invocations: accepted by acceptance owner for billing because app credits stayed 10.000000 with total_cost_usd 0.000000 and the Worker stayed inside the one-POST cap
Unknown closure for Retry attempts: accepted by acceptance owner for billing because no second Worker POST was sent
```

```text
Fixture identity: throwaway user nimhpk4w8 / vs-AI game 66375b64-6b95-4221-b0c2-2416ac5e4c8f
Prior values proven: yes
Mutation authority: reversible local servers, one throwaway user, one vs-AI game, NVIDIA quota for the authorized stream
Write mode: fail-closed-transactional
Affected rows: one user, one game, one AI pass, one zero-charge billing POST
Postconditions verified: yes
Unrelated state preserved: verified
Counted as provider call: no
Manual repair after provider result: none
New logical whole required: no
```

Browser Stall Guard:
```text
Failure episode identity: home-blank-then-loaded
Prior episode identity: none
Episode relationship: initial
Symptom continuity evidence: first navigate snapshot was about:blank; curl already returned home 200; second snapshot showed Register/Sign In
Initial verification result: succeeded
Recovery attempts: 0
Recovery attempt 1: not-used because the home page loaded without a second navigation
Recovery attempt 2: not-used because verification succeeded
Verification succeeded: yes
Repeated failure remains unresolved: no
Conclusive no-progress evidence: no
Stall guard: not-triggered
Repeated failure evidence: none
Guard rationale: the blank document was a race with Next hydration, not a repeated no-progress failure
Evidence preserved: yes
Browser repair after trigger: none
Alternative evidence: not-required
Absent verification: none
Cooperator acceptance required: no
Result claimed from missing evidence: none
```

Deviations, risks, missing evidence:
1. Next.js did not print `integrate.api.nvidia.com` for the successful stream. Runtime identity is from SSE `provider_path` / `runtime_model` plus the catalog pair and Django persist. This-session logs after the 20:42:20 start header contain **no** `openrouter.ai`.
2. Older frontend.log lines before that start header contain leftover OpenRouter 429 traces from a prior supervisor run; they are not this turn.
3. `last_move_billing` on GET game was null; zero incremental cost is shown by unchanged `credit_balance` 10.000000 and `total_cost_usd` 0.000000 plus `charge-ai-turn` HTTP 200.
4. Default AI thinking time stayed 30s; the authorized stream ran ~61s (route timeout / auto-finalize). Django still persisted `pass`.
5. Password and JWT were never reported. Overlay candidate text was not quoted.

One smallest next step: issue Slice 3 (one-turn, three-model fallback, including OpenRouter-429→NIM) to a **fresh** Worker. Do **not** retry this NIM happy-path. Do **not** close the logical whole. Do **not** push.

Native planning mode: **not-used**
Report justification: **new-evidence**
Authority-expiry statement: this acceptance authority expires when this terminal report is submitted. A UI approval or retained plan grants no extra authority.
Logical-whole closure: **not-closed**

Resolved Execution Issues / Near-Misses:
- Settings lists two Nemotron cards with the same display name. The NIM card was selected by description (`NVIDIA NIM chat rival with tool calling`) and confirmed via GET `/api/auth/me/` before Play. The OpenRouter `:free` card was not clicked.
- First home snapshot was `about:blank`; recovered by waiting, not by a second navigation.
- Fill-tool output included the password; it is omitted from this report.
- Did not start Redis, a second game, `/api/ai/judge`, or OpenRouter.

Pre-Existing Failure Classification:
- Leftover OpenRouter 429 stack traces in `frontend.log` **before** this session’s start header: prior-run residue, not this turn.
- Redis absent by authority; Channels publish to `127.0.0.1:6379` failed with connection refused. Expected for AI-only; the vs-AI pass still persisted.
