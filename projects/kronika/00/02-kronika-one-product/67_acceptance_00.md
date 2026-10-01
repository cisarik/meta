# S9-R Bounded Live Proof — Model switch during an active request (Cooperator-executed)

Logical whole identity: kronika-one-product
Worker session ordinal: 67
Worker exchange ordinal: 01
Executor: COOPERATOR (manual, through the deployed workspace UI on the NUC)
Coordinator: ORCHESTRATOR

## Authority record (provider calls)

```text
Provider call authority: authorized for exactly one new Research request and one
  new Search request for this proof only
Numerical call cap: 2 generation submissions; polling and remote-deletion
  calls follow each submission; no retries, no extra quality comparisons
Concurrency: single-call-in-flight
Terminal outcome before next call: required
Reservation bound: research USD 5.00 + search USD 0.50 = USD 5.50 maximum
  against the remaining platform credit (about USD 7.12)
Purpose: prove that an administrator model change reaches only new admissions,
  that an already admitted request keeps its model and pricing, and that
  accounting resolves per admitted model with automatic remote cleanup
Stop conditions: uncontrolled duplication, credential or billing anomaly,
  unexpected admission refusal, unexplained state, any required step missing
Fixture: synthetic, public, non-personal questions only
```

## Preconditions

- NUC serves `2af8edde5faf8967777a68b0a72685cc580c45ea`; database `0035`;
  research enabled; credential present; model currently
  `gpt-5.5-2026-04-23` (restored during rendered acceptance); admin rendered
  acceptance complete.
- Automatic remote cleanup is live in this release.

## Steps (Cooperator)

1. Open the **Research** form and submit exactly one research request:
   “Using official Python documentation, explain how asyncio.TaskGroup handles
   task failures, cancellation, and ExceptionGroup. Include source links.”
   Consent; Submit once.
2. **While that request is still active** (Working… / not yet Saved), open the
   administrator AI dialog → **Research settings**, change the model to
   `gpt-5.6-luna`, confirm, and save. Confirm the “Research settings saved.”
   state. Do not cancel the first request.
3. Wait for the Research request to reach “Saved.” and open its answer.
4. Submit exactly one **Search**:
   “What does the official Python documentation say that asyncio.TaskGroup
   does? Include a source link.”
   Consent; Submit once; wait for “Saved.”; open its answer.
5. Restore the model to `gpt-5.5-2026-04-23` in Research settings, confirm and
   save (“saved” or “unchanged” is fine).
6. On `platform.openai.com` → Usage, note today’s request count and cost.

If the first request completes before the model change is saved, report the
mid-run overlap as unproven; do not add another generation. If any step errors,
stop and report the exact copy; no retries.

## Orchestrator verification afterwards (read-only)

- `research_requests`: the new research row persisted `gpt-5.5-2026-04-23` and
  the new search row persisted `gpt-5.6-luna`, both with configuration version
  `s9r-20260930`; both `saved`, no error codes; `cleanup_state` becomes
  `deleted` through the automatic nudge path.
- `research_budget_holds`: both `reconciled`; the research cost uses the 5.5
  schedule and the search cost the Luna schedule.
- Common records exist for both; render works in the UI (steps 3 and 4).
- Settings restored to the default model; the change itself proved the
  settings save path with a live effect.

## Report

The Orchestrator records the outcome as `67_report_00.md` together with the
Cooperator observations; any failure stops the proof and a new bounded
decision follows. This proof does not close the logical whole and authorizes
no further provider calls.
