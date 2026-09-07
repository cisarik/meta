### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 34
Worker exchange ordinal: 01
```

**Status:** `PARTIAL`  
**Phase-qualified result:** `not-applicable`  
**Report justification:** `new-evidence`

Context pressure: moderate; the live window and accounting fit in one exchange.

---

### 1. Coordinates

Logical whole identity: `admin-provider-model-console`  
Worker session ordinal: 34, Worker exchange ordinal: 01  
Task identity: APMC-K1  
Worker session target: `fresh-worker-session`

### 2. Status

`PARTIAL` — the authorized live measurement ran and is fully accounted, but NVIDIA NIM did not author a candidate. Subcaps cannot leave `provisional` on authorship-path cost.

### 3. Phase-qualified result

`not-applicable` (calibration measurement)

### 4. Start and end commit

Start: `151e833dd0e78ced075101864cb5f45ee521bebc`  
End: `151e833dd0e78ced075101864cb5f45ee521bebc`  
AP pin: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (detached `.ap` HEAD, correct)  
Branch: `## main...origin/main`  
Working tree: empty before and after (`git status --porcelain=v1` empty)

### 5. Changed files and purpose

None. Read-only measurement; no repository mutation.

### 6. Tests and validation

**Credential:** `credential present: yes (NVIDIA_API_KEY)` (loaded from `frontend/.env.local` into the parent shell via `set -a; . frontend/.env.local; set +a`; value never printed). Process environment was empty until that load.

**Fake (0 provider calls)** — prompt omitted `--fixture-id`/`--seed`; the CLI refuses with exit 2 (`exactly one of --fixture-id or --seed is required`). Re-ran with the shipped Slovak turn fixture `slovak-turn-diacritic-blank`:

```text
slovak turn slovak-turn-diacritic-blank action=place source=backend_ranked_candidate score=82 words=SČÍTALO persisted=1 verdict=pass
slovak turn slovak-turn-diacritic-blank action=place source=backend_ranked_candidate score=82 words=SČÍTALO persisted=1 verdict=pass
```

Exit 0. `executed_runtime_mode=fake`. `summary.external_provider_invocations=0`. `source_revision=151e833dd0e78ced075101864cb5f45ee521bebc`. Wall ~21.4 s for two independent turns.

**Live capability probe (1 call):**

```text
{"provider":"nvidia-nim","model":"nvidia/nemotron-3-super-120b-a12b","status":"unknown","latency_ms":1506,"outbound_count":1}
```

Vitest exit 1 (`expected 'pass'`). Log: `nvidia-nim provider_http 500`. Not auth failure (not 401/403). Classified `unknown` because HTTP 500 is outside the named status list.

**Live turn diagnostic (3 sequential plies, 1 call in flight, `--turn-count 1` each to keep the session cap stoppable):**

```text
slovak turn slovak-turn-diacritic-blank action=place source=backend_ranked_candidate score=82 words=SČÍTALO persisted=1 verdict=pass
```

(same metric line on all three live plies)

| Ply | `provider_requests_used` | `external_provider_invocations` | `completion_source` | `terminal_cause` | action | score | wall |
|---|---|---|---|---|---|---|---|
| Live 1 | 1 | 1 | `backend_ranked_candidate` | `generic_error_fallback` | place | 82 | ~20.2 s |
| Live 2 | 1 | 1 | `backend_ranked_candidate` | `no_provider_progress_deadline` | place | 82 | 40 s |
| Live 3 | 1 | 1 | `backend_ranked_candidate` | `no_provider_progress_deadline` | place | 82 | 39 s |

All three: `executed_runtime_mode=live`, `verdict=pass`, `reason_code=ok`, `repair_attempted=false`, `unresolved_in_flight=0`, queue length 1, persisted `SČÍTALO`. Score 82 is an **engine** metric (identical to fake). RF-16: `.venv/bin/python` only; `PYTHON_DOTENV_DISABLED` never set.

### 7. Commit and push result

Not authorized. None.

### 8. Deviations, risks, missing evidence

1. Prompt commands omitted the required `--fixture-id`/`--seed` axis. Used shipped fixture `slovak-turn-diacritic-blank` (the historical NIM turn fixture). Literal prompt commands exit 2.
2. Live ran as three sequential `--turn-count 1` invocations instead of one `--turn-count 3`, so the 12-call stop could fire between plies.
3. **NIM did not complete a model-authored move.** Probe HTTP 500; live ply 1 `generic_error_fallback`; plies 2–3 `no_provider_progress_deadline`. Distribution is 100% engine rescue.
4. Requests-per-ply is therefore the **rescue floor** (one failed/silent provider call, then `backend_ranked_candidate`), not a healthy tool-loop ceiling. `max_steps=15` was not consumed.
5. Position set is a single known-legal fixture repeated, not seeds 300/301/302.

### 9. Smallest next step

Do **not** clear `subcaps_provisional` on this evidence. Either (a) keep provisional and take K1 as rescue-floor = 1 request/ply, or (b) issue a follow-up live grant when `probe:provider` returns `status=pass`, then re-measure authorship-path `provider_requests_used`. Whole-closure INFOSEC 4.6 may proceed with that residual named.

### 10. Report justification

`new-evidence`

### 11. Authority expiry

Worker authority for session 34 exchange 01 ends upon this report. No whole-closure, no 14/00, no further provider calls.

---

## Provider Accounting Contract

```text
Provider call authority: authorized for measuring requests-per-ply on nvidia-nim to calibrate position-set instrument subcaps
Numerical call cap: 12 because bounded budget to prevent unexpected billing and noise floor
Unlimited call authority: no
Concurrency: single-call-in-flight
Terminal outcome before next call: required
Additional call purpose: calibration of subcap defaults
Retry inventory requirement: not-required-inside-authorized-loop
Stop conditions: uncontrolled duplication, credential exposure, unexpected billing, destructive risk, unexplained unrelated mutation, material scope expansion, loss of fixture or privacy guarantee
```

```text
Provider accounting record: activated
Task or acceptance scope: APMC-K1 live NVIDIA NIM requests-per-ply calibration (slovak / nvidia-nim / nvidia/nemotron-3-super-120b-a12b)
Bounded time window: 2026-09-07T15:18:10Z through 2026-09-07T15:21:04Z
Subject identity: fixture slovak-turn-diacritic-blank (variant slovak)
Run or correlation boundary: Worker session 34 exchange 01; fake diagnose_ai_play + vitest probe:provider + three live diagnose_ai_play --turn-count 1
Evidence source: diagnose_ai_play JSON summaries (external_provider_invocations, turn_provider_requests_used, completion_source); probe JSON outbound_count/status/latency_ms; git rev-parse
Evidence freshness: current for 2026-09-07T15:18:10Z–15:21:04Z
Reconciliation status: fully-reconciled
Accounting authority effect: none
```

```text
Intended UI submissions: not applicable because this was CLI/vitest diagnostic, not an admin or game UI submission
Intended UI submissions relationship: not applicable because CLI/vitest diagnostic
Actual external provider invocations: 4
Actual external provider invocations relationship: total
Retry attempts: 0
Retry attempts relationship: subset of actual external provider invocations
Defect-driven duplicate invocations: 0
Defect-driven duplicate invocations relationship: subset of actual external provider invocations
Retry/duplicate overlap: 0
Terminal outcomes: completed=0 failed=2 cancelled=2 refused=0
Terminal outcomes relationship: one-to-one with actual external provider invocations
In-flight invocations: 0
Unresolved invocations: 0
Durable provider-submission rows: 0
Durable provider-submission rows relationship: not applicable because diagnose_ai_play uses an ephemeral pytest-django database that is destroyed after the command; no DiagnosticPly/DiagnosticRun rows retained
Analysis-run rows: 0
Analysis-run rows relationship: not applicable because this session did not launch the diagnostic match runner
Security-audit events: 0
Security-audit events relationship: not applicable because no security-audit sink was in the authorized path
Canonical save events: 0
Canonical save events relationship: independently varying metric because each live ply persisted a move into an ephemeral test DB that was then deleted; those saves are not durable provider-submission rows
Count divergence: none
```

Terminal-class map (one class per invocation):

- Probe: **failed** (HTTP 500, `status=unknown`, `outbound_count=1`)
- Live ply 1: **failed** (`generic_error_fallback` after `provider_requests_used=1`)
- Live ply 2: **cancelled** (`no_provider_progress_deadline` after `provider_requests_used=1`)
- Live ply 3: **cancelled** (`no_provider_progress_deadline` after `provider_requests_used=1`)

Turn `verdict=pass` is independently varying: the engine rescued after the provider invocation terminated. Fake mode added 0 invocations.

---

## Empirical Calibration Table

| Sample | External calls | `provider_requests_used` | `completion_source` | Model vs engine | Wall |
|---|---|---|---|---|---|
| Fake ply 1 | 0 | 0 | `backend_ranked_candidate` | engine (fake) | ~21.4 s pair |
| Fake ply 2 | 0 | 0 | `backend_ranked_candidate` | engine (fake) | (same pair) |
| Probe | 1 | 1 (`outbound_count`) | n/a | provider HTTP 500 | 1506 ms |
| Live ply 1 | 1 | 1 | `backend_ranked_candidate` | engine rescue | ~20.2 s |
| Live ply 2 | 1 | 1 | `backend_ranked_candidate` | engine rescue | 40 s |
| Live ply 3 | 1 | 1 | `backend_ranked_candidate` | engine rescue | 39 s |
| **Session total** | **4** | | | | |

Live plies n=3:

- Mean `provider_requests_used` per ply: **1.0**
- Max `provider_requests_used` per ply: **1**
- Model-authored (`provider_candidate` + `repair_candidate`): **0 / 3 = 0%**
- Engine rescue (`backend_ranked_candidate`): **3 / 3 = 100%**
- Score on every ply: 82 (`SČÍTALO`) — engine metric, identical to fake

### Derived subcap arithmetic (from observed max = 1)

- Position-set instrument (24 positions × max requests/ply): **24**
- Game instrument using the prompt’s example (30 plies × max): **30**
- Game instrument using shipped `DIAGNOSTIC_MAX_PLIES_DEFAULT=60`: **60**
- Shipped run default `DIAGNOSTIC_MAX_PROVIDER_REQUESTS_DEFAULT=200` still bounds all of the above

**Calibration verdict:** 24 coincidentally matches a 1:1 rescue floor. It is **not** a measured authorship-path ceiling. A later passing NIM tool-loop could consume several requests per ply (grant was `max_steps=15`). Keep `parameters_json.subcaps_provisional=true` until a `probe:provider` `pass` plus at least one `provider_candidate` / `repair_candidate` ply is measured.

```text
Resolved Execution Issues / Near-Misses: prompt diagnose_ai_play lines missing required --fixture-id|--seed (exit 2); resolved by shipped fixture slovak-turn-diacritic-blank, residual = Orchestrator should name fixture or seed in any reissue. zsh read-only $status after live ply 1 hid the epoch footer; manage.py had already printed a complete pass JSON; residual = none. NIM HTTP 500 / silent-model deadline: no Worker retry loop started.
Pre-Existing Failure Classification: none
```

Authority ended.
