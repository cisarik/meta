### Report for ORCHESTRATOR_CHAT

Logical whole identity: parameterized-cli-ai-play  
Worker session ordinal: 09  
Worker exchange ordinal: 01

Status: **PASS**  
Phase-qualified result: not-applicable (this is neither implementation nor publication; it is bounded acceptance evidence).

Start commit: `b18e50eb56d90fe65d95670c48b1d32d16bd3721`  
End commit: `b18e50eb56d90fe65d95670c48b1d32d16bd3721`  
Changed files: none  
Git: branch `main`; porcelain empty before and after; `HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `origin/main` = `b18e50eb56d90fe65d95670c48b1d32d16bd3721`. No commit, push, or source edit.

---

### Stage 0 gate evidence

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `b18e50eb56d90fe65d95670c48b1d32d16bd3721` |
| `git status --porcelain` | empty |
| `git rev-parse HEAD:.ap` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `git ls-remote origin refs/heads/main` | `b18e50eb56d90fe65d95670c48b1d32d16bd3721` |
| pytest (`test_ai_play_turn_diagnostic.py`, `test_turn_probe.py`, `test_ai_play_engine_diagnostic.py`, `test_slovak_ranked_search.py`) | exit 0; `s....................................` (started `2026-08-30T17:25:23Z`, ~25s) |
| fake `diagnose_ai_play` slovak / NIM / `slovak-turn-diacritic-blank` | exit 0 |

Fake run: `requested.runtime_mode=fake`, **`executed_runtime_mode=fake`**, `external_provider_invocations=0`, `turn_provider_requests_used=0`, action=`place`, `completion_source=backend_ranked_candidate`, word=`SČÍTALO`, score=82, verdict=`pass`. This is not live evidence.

Credential present: `NVIDIA_API_KEY` = **yes** (dotenv) / **no** (ambient)  
Credential present: `OPENROUTER_API_KEY` = **yes** (dotenv) / **no** (ambient)  
Mechanism: subshell `set +x; set -a; . frontend/.env.local; set +a; export LIBRETILES_AI_PLAY_LIVE=1` then `manage.py`. Values were never printed, hashed, or copied. `backend/.env` was not read. Leak scans of stdout/stderr/JSON for assignment/Authorization/Bearer needles: no.

---

### Stage-by-stage narrative

**Stage 1 — purpose:** first live Slovak canary against flagship NIM `nvidia/nemotron-3-super-120b-a12b`, selected-only, fixture `slovak-turn-diacritic-blank`, sentinel set, credentials in the parent environment.  
Window: `2026-08-30T17:26:57Z`–`2026-08-30T17:29:11Z` (~134s). Exit 0.  
`executed_runtime_mode=live`, `external_provider_invocations=2` (≥1). Classified before any further call: legal place persisted, **engine-rescued** (`backend_ranked_candidate`), not a mechanical product failure. Continue.

**Stage 2a — purpose:** Stage 1 was engine-rescued on an empty-board diacritic-blank rack; sample a different geometry (`slovak-hooks-umenasi`, midgame OA, rack `UMENASI`) so the completion-source distribution is not a single-position artifact.  
Window: `2026-08-30T17:29:51Z`–`2026-08-30T17:32:09Z` (~138s). Exit 0. Live, 1 invocation, again `backend_ranked_candidate`.

**Stage 2b — purpose:** two engine rescues so far; sample a third distinct board/rack (`slovak-midgame-auto-ltaseni`, AUTO stem, diacritic rack `ĽŤÁSENI`).  
Window: `2026-08-30T17:32:29Z`–`2026-08-30T17:34:33Z` (~124s). Exit 0. Live, 3 invocations, again `backend_ranked_candidate`. Unicode `Ľ`/`Á` persisted.

**Stage 3 — purpose:** all three Slovak turns were engine-rescued; one English empty-board `AUTOLIN` control (`english-empty-autolin`) to separate “cannot do Slovak” from “cannot invent a backend-valid placement at all”. Dead-rack `english-turn-dead-qqq` was not used because it cannot answer that question.  
Window: `2026-08-30T17:35:02Z`–`2026-08-30T17:37:06Z` (~124s). Exit 0. Live, 1 invocation, again `backend_ranked_candidate` (`OUTLAIN`/66, same word and score as the witness, different axis).

**Stage 4 — purpose (optional):** NIM produced 0 `provider_candidate` in either language; one OpenRouter catalog-row-1 control (`google/gemma-4-31b-it:free`) on the same Slovak diacritic-blank fixture, to test whether engine rescue is NIM-specific or the live-path default. Cap before this call: 7 used, 5 remaining.  
Window: `2026-08-30T17:37:43Z`–`2026-08-30T17:38:00Z` (~17s). Exit 3 (live `external_incomplete`). Live mode honored, 1 invocation, `terminal_kind=coded_provider_error`, `reason_code=coded_provider_unchanged`. **This is a coded provider failure, not a product defect.** Selected-only queue: no shipped fallback remaining. Stopped; no retry.

---

### Result table (live turns)

**Stage 1** — slovak / nvidia-nim / `nvidia/nemotron-3-super-120b-a12b`  
requested `live` / executed **`live`**. Playability `found`, witness present (`LOSÍČAT`/74). Action `place`. Placement letters `S,Č,?,T,A,L,O` with blank_as `Í`. Complete formed words: **`SČÍTALO`**. Score **82**. `completion_source=backend_ranked_candidate`. Probe `found`. Repair `false`. Terminal cause `backend_ranked_candidate`. Attempts 1 (nvidia-nim, timeout 119s of 120, step grant 50, provider_requests_used 2). Turn provider requests 2. External invocations **2**. Wall-clock ~134s. Persistence: move_id 1, move-count Δ1, state-version Δ1, SSE/DB action/words/score all match. Verdict `pass` / `ok`. Foreign origins none.

**Stage 2a** — slovak / nvidia-nim / `nvidia/nemotron-3-super-120b-a12b`  
requested `live` / executed **`live`**. Playability `found`, witness present (`NEMUSIA`/12). Action `place`. Placement letters `S,A,M,E,N,I,U`. Complete formed words: **`OSAMENIU`**. Score **74**. `completion_source=backend_ranked_candidate`. Probe `found`. Repair `false`. Terminal cause `backend_ranked_candidate`. Attempts 1 (timeout 120, step grant 50, requests 1). External invocations **1**. Wall-clock ~138s. Persistence: move_id 1, Δ1/Δ1, SSE/DB agree. Verdict `pass` / `ok`. Foreign origins none.

**Stage 2b** — slovak / nvidia-nim / `nvidia/nemotron-3-super-120b-a12b`  
requested `live` / executed **`live`**. Playability `found`, witness present (`NESIAŤ`/14). Action `place`. Placement letters `S,Ľ,N,Á`. Complete formed words: **`SOĽNÁ`**. Score **22**. `completion_source=backend_ranked_candidate`. Probe `found`. Repair `false`. Terminal cause `backend_ranked_candidate`. Attempts 1 (timeout 120, step grant 50, requests 3). External invocations **3**. Wall-clock ~124s. Persistence: move_id 1, Δ1/Δ1, SSE/DB agree. Verdict `pass` / `ok`. Foreign origins none. Diacritics `Ľ`/`Á` preserved end to end.

**Stage 3** — english / nvidia-nim / `nvidia/nemotron-3-super-120b-a12b`  
requested `live` / executed **`live`**. Playability `found`, witness present (`OUTLAIN`/66). Action `place`. Placement letters `O,U,T,L,A,I,N`. Complete formed words: **`OUTLAIN`**. Score **66**. `completion_source=backend_ranked_candidate`. Probe `found`. Repair `false`. Terminal cause `backend_ranked_candidate`. Attempts 1 (timeout 120, step grant 50, requests 1). External invocations **1**. Wall-clock ~124s. Persistence: move_id 1, Δ1/Δ1, SSE/DB agree. Verdict `pass` / `ok`. Foreign origins none.

**Stage 4** — slovak / openrouter / `google/gemma-4-31b-it:free`  
requested `live` / executed **`live`**. Playability `found`, witness present (`LOSÍČAT`/74). Action none. Placements none. Formed words none. Score 0. `completion_source=null`. Probe `found`. Repair `false`. Terminal cause `provider_error`. Attempts 1 (timeout 120, step grant 50, requests 1). External invocations **1**. Wall-clock ~17s. Persistence: move_id null, Δ0/Δ0. Verdict **`external_incomplete`** / `coded_provider_unchanged`. Foreign origins none. No pass/exchange while probe `found` (no action persisted).

---

### Headline aggregate

- **Slovak (NIM):** 3 live turns. Completion-source distribution: `backend_ranked_candidate` 3; `provider_candidate` **0**; `repair_candidate` 0; `backend_witness_rescue` 0; `genuine_no_move_exchange` 0; `genuine_no_move_pass` 0.
- **English (NIM):** 1 live turn. Completion-source distribution: `backend_ranked_candidate` 1; `provider_candidate` **0**.
- **OpenRouter control:** 1 live invocation, no completion source (provider error before a move). Not NIM evidence.

**Did the live model ever produce a backend-valid placement on its own, in either language? No. Every completed live turn was engine-rescued (`backend_ranked_candidate`).** That is an acceptable PASS for this annex: the product finished and persisted legal Slovak and English turns; this free NIM model did not author those placements.

Observed model/product behaviour (evidence, not opinion):
- No sample timed out or exhausted the 50-step grant (requests used 1–3).
- `repair_attempted=false` on every sample.
- No `stale_witness`, no generic unchanged-turn, no `sse_done_without_matching_move`.
- Overlay illegal-word *attempts* are not in the v1 turn report (missing evidence below). Terminals that persisted were lexicon-legal.

Product-rule check under real latency:
- Never pass or exchange while probe `found`.
- Queue length 1 on every turn (≤ `MAX_FALLBACK_ATTEMPTS` 3).
- Granted timeout ~119–120s and step grant 50 honored; `turn_provider_requests_used` matched `external_provider_invocations` on every sample.
- Unicode preserved (`SČÍTALO`, `SOĽNÁ`, blank_as `Í`).
- Fetch guard: no foreign origins; provider hits were the shipped NIM/OpenRouter bases.
- Complete two-letter formed words outside the variant lexicon: **none**. Complete formed words were `SČÍTALO`, `OSAMENIU`, `SOĽNÁ`, `OUTLAIN`; all `two_letter_policy.rejected` arrays empty.

---

### Provider accounting record

Provider accounting record: activated  
Task or acceptance scope: Slice L live-provider canary rerun — NIM Slovak/English legal-turn measurement plus optional OpenRouter catalog-row-1 control, cap 12  
Bounded time window: `2026-08-30T17:25:23Z`–`2026-08-30T17:39:06Z`  
Subject identity: `slovak-turn-diacritic-blank`, `slovak-hooks-umenasi`, `slovak-midgame-auto-ltaseni`, `english-empty-autolin`  
Run or correlation boundary: ephemeral dir `/tmp/libretiles-ai-play-live-pCTOlk` (removed); report `generated_at` `2026-08-30T17:29:10Z`, `17:32:08Z`, `17:34:32Z`, `17:37:06Z`, `17:37:59Z`; source_revision `b18e50eb56d90fe65d95670c48b1d32d16bd3721`  
Evidence source: the v1 JSON reports plus CLI stderr metric lines  
Evidence freshness: current for `2026-08-30T17:25:23Z`–`2026-08-30T17:39:06Z`  
Reconciliation status: fully-reconciled  
Accounting authority effect: none

Intended UI submissions: not applicable because this is a CLI acceptance, no UI was used  
Actual external provider invocations: **8** (derived: 2+1+3+1+1)  
Actual external provider invocations relationship: total  
Retry attempts: **0** ; relationship: subset of actual external provider invocations  
Defect-driven duplicate invocations: **0** ; relationship: subset or overlapping subset  
Retry/duplicate overlap: **0**  
Terminal outcomes (turn samples): completed=4 failed=0 refused=0 cancelled=0 external_incomplete=1 ; relationship: turn-level, not one-to-one with the 8 invocations  
In-flight invocations: 0  
Unresolved invocations: 0  
Durable provider-submission rows: not applicable because the harness uses an ephemeral pytest database and does not write a product provider-submission ledger  
Analysis-run rows: not applicable because this diagnostic does not persist analysis-run rows  
Security-audit events: not applicable because no security-audit event store is written by this command  
Canonical save events: not applicable because reports were ephemeral temp JSON removed at cleanup; game rows lived only in the pytest DB  
Count divergence: 8 fetch-guard provider HTTP hits versus 5 turn samples, because a successful tool-loop turn can emit multiple provider calls (Stage 1: 2, Stage 2b: 3)

Unknown closure for per-HTTP-call terminal outcome: accepted by ORCHESTRATOR for acceptance because the shipped v1 report classifies terminals per turn sample, not per HTTP call  
Unknown closure for OpenRouter error subclass (auth vs quota vs policy vs 5xx): accepted by ORCHESTRATOR for acceptance because the v1 sample exposes `coded_provider_error` / `provider_error` / `coded_provider_unchanged` only, and further log mining risked credential exposure

Fake Stage 0 contributed 0 invocations and is excluded from the 8.

---

### Temp cleanup outcome

Removed exact owned directory `/tmp/libretiles-ai-play-live-pCTOlk`. No leftover `/tmp/libretiles-ai-play-live-*`. Repository tree untouched.

---

### Deviations, risks, missing evidence

Deviations (inside the grant):
- Stage 2 used two other named Slovak fixtures rather than `--turn-count 3` on one fixture, because independent positions exist and the prompt preferred that.
- Stage 3 used `english-empty-autolin` rather than `english-turn-dead-qqq`, because a dead rack cannot test whether the model can invent placements.
- Stage 4 optional OpenRouter control was executed, then stopped on `external_incomplete` with no retry.

Risks:
- Four completed NIM turns is a small sample; `provider_candidate=0` is still the truthful measurement for this annex.
- OpenRouter catalog-row-1 competence remains unknown (provider blocked that optional control).

Missing evidence:
- Overlay/invalid candidate attempts (not in v1 samples).
- OpenRouter HTTP status / error subclass.
- Per-HTTP-call terminal classification.

---

### One smallest next step

Treat this annex as live-canary PASS: the corrected tool honors `--runtime-mode live`, counts real provider calls, and persists legal Slovak and English NIM turns without `stale_witness` or generic unchanged-turn. Record as first-class product fact that **this NIM free model did not author a backend-valid placement in four completed live turns; the engine did**. Do not retry OpenRouter under this expired grant. Do not close the logical whole. Any further live spend needs a new complete prompt.

Report justification: new-evidence  
Logical-whole closure: not-closed

Authority expiry statement: this exchange’s authority, including the provider grant, expires with this terminal report. Retained context is not a renewal. No further provider call will be made.

Resolved Execution Issues / Near-Misses: ambient `NVIDIA_API_KEY` and `OPENROUTER_API_KEY` were absent (same class of observation as Worker 08). Cause: keys live in `frontend/.env.local`, not the parent shell. Resolution: subshell dotenv load of those two names only, never rendered. Residual risk: none in this process; ambient shell still lacks the keys.

Pre-Existing Failure Classification: none