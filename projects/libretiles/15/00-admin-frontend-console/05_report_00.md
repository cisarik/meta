### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-frontend-console  
Worker session ordinal: 05, Worker exchange ordinal: 01

# Slice 3 — Deep Move Inspector & Recorded AI Telemetry

**Status: PASS — repository-grounded implementation plan.** This reports planning completion, not implementation or acceptance.

The Cooperator explicitly authorized continued read-only planning after the baseline mismatch and selected **server-side telemetry collection in addition to the frontend inspector**. The accepted planning baseline is `1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a`. The earlier BLOCKED report remains a record of the original failed gate.

```text
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: 1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a
End commit: 1d57ee2927fc0c08c824ab69ac3a8d01f6abb21a
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: baseline mismatch resolved for planning by explicit Cooperator direction
Pre-Existing Failure Classification: original baseline gate mismatch; no runtime failure established
```

```text
Planning cycle: initial
Prior planning report: none — the earlier report stopped at the repository gate
Targeted revision basis: none
Changed decision boundary: Cooperator accepted actual HEAD and expanded scope to telemetry collection
Preserved unaffected decisions: read-only planning; no network, secrets, implementation, or publication
Automatic targeted revisions used: 0
```

Evidence: inspected replay serialization, frontend ingress/types/components, scoring and word authority, AI execution and fallback paths, diagnostic persistence, existing tests, project instructions, and the previous slice report. Working tree remains clean. No tests or browser checks were executed.

## D1 — Drawer & Tabbed Inspection Layout

Replace the expanded content of `ReplayMoveDetails` with a compact move summary and an **Inspect move** disclosure. Add `ReplayMoveInspector` with three tabs:

- **Score & Words**
- **AI Telemetry & Tool Calls**
- **Engine & Search**

At widths **≥1024px**, retain the board in the left column and dual racks above the inspector in the right column. The inspector is a non-modal panel in document flow, with independently scrollable contents capped at `32rem`. Below 1024px, use an inline accordion beneath the racks. Nothing overlays the board or racks; smaller screens scroll naturally.

Behavior:

- Start collapsed, with Score & Words selected.
- Opening the inspector pauses playback. Explicit Play remains available while it is open.
- Preserve open state and selected tab across plies; replace the inspected data and reset its internal scroll and expanded event rows.
- At position zero, show “Initial position”; move-specific inspection is unavailable.
- Keep the existing VCR seek control as the turn selector; no separate history-navigation subsystem.
- Preserve partial-replay board playback restrictions. When the initial board is absent, offer a separate stored-move selector inside the inspector, explicitly labelled as inspecting records while the board shows the final snapshot.

Use proper `tablist`, `tab`, `tabpanel`, `aria-selected`, and disclosure semantics. Tabs support arrow keys and Home/End without triggering replay shortcuts. Escape collapses the inspector and restores focus to its trigger.

Reuse existing gold/black admin styling. Status meaning always includes text; reduced motion removes transitions. Admin copy remains English, matching the existing console.

## D2 — Deep Score & Cross-Word Breakdown

**Compute and capture detailed scores in the backend’s existing scoring path.** Frontend formatters display and reconcile those records; they do not implement another scoring authority.

Extend `ScoreBreakdown` with optional tile details. Add an opt-in keyword to `score_words`, defaulting off, so ranked searches do not allocate inspection records for every candidate. Enable it when persisting a legal placement.

For each word, add an optional versioned `inspection` object inside its existing `Move.words_formed` JSON entry:

- Physical cells: `row`, `col`, `token`, `blank_as`.
- Per-cell `base_points`, `is_new`, premium label, whether it applied, and letter multiplier.
- Word base sum, letter bonus, word multiplier, and total.
- Backend word-authority record described in D5.

Capture these values **before premium consumption**, from the same board and scoring loop that calculate the persisted points. Existing `word`, `score`, `multiplier`, and `coords` remain intact.

Display an equation such as:

`[L(1) + E(1) + A(1) + D(2)] × 2 DW = 10`

Letter multipliers appear inside the sum; word multipliers apply to the entire sum. Assigned blanks retain their displayed letter and contribute zero. A multigraph occupies one tile and uses that tile’s complete token for point lookup.

Classification:

- With multiple placements, the word along their placement axis is primary; orthogonal words are cross-words.
- For a single placement forming two words, use horizontal as the display-primary convention and label both directions explicitly.
- A single resulting word is simply “Formed word”; classification never changes scoring or stored order.

Show a **Bingo +50** badge only when seven physical placements and the stored total reconcile with the summed word scores plus 50.

For both players, show recorded score adjustments using:

`after score − before score − placement points credited to that player`

Use the recorded end reason for context. Without sufficient evidence, label the difference “Recorded score adjustment”; do not invent a specific penalty.

Legacy records retain stored scores and coordinates. Missing detailed evidence displays “Per-tile breakdown was not recorded.” Malformed or inconsistent new details produce a reconciliation warning and fall back to stored totals.

## D3 — Tool-Call Execution & Candidates Viewer

**Measured gap:** `sanitize_ai_metadata` currently strips tool arguments, and the diagnostic runner does not populate a structured `ai_trace`. Existing data cannot supply the requested execution history.

Add a strictly typed, versioned `ai_metadata.inspection_trace` envelope. Keep existing forbidden raw-output fields forbidden. No database migration is needed.

The envelope contains:

| Record | Required behavior |
|---|---|
| Version and turn anchor | Version `1`; game ID, pre-move count, acting slot |
| Attempts | Ordered records, maximum three; zero-based attempt index, provider/model identifiers |
| Timing and accounting | Attempt elapsed time to submission, reported provider requests, outcome |
| Events | Ordered `validateMove`, `finishMove`, and repair-start records |
| Search summary | Only observed strategy mode and ranked/playability summary fields |
| Completeness | Explicit truncation, incomplete-call, and missing-attempt indicators |

A tool event contains a local ordinal, elapsed milliseconds, search/repair phase, tool name, sanitized parameters, and its result:

- `validateMove`: up to seven placements; returned word verdicts, score, and stable rejection code.
- `finishMove`: `{ready:true}` and its returned acknowledgement.
- Repair-start: an explicit phase marker; do not infer repair merely from a later valid proposal.

Record calls in the existing tool execution callbacks. Record invalid proposals as well as valid ones. Allocate the event ordinal at invocation so concurrent completions cannot reorder the history. A pending call at terminal capture is labelled incomplete. Freeze the persisted snapshot against late callbacks.

**Collection limits:** maximum 64 event records per attempt, 32 KiB serialized per attempt, and 96 KiB per turn. Retain earliest complete records plus the final event when it fits; report omitted counts. Bound word arrays to eight formed words and each word to the board’s maximum physical span times the existing token code-point limit. Validate coordinates, tokens, enums, booleans, and finite nonnegative counters. Do not retain prompts, reasoning text, arbitrary response bodies, exception messages, headers, credentials, or runtime configuration.

Apply equivalent explicit projection in TypeScript and Django. Unknown fields are dropped. Invalid inspection metadata must not make an otherwise legal move fail.

**Fallback data flow:**

1. The route emits its bounded attempt observation in terminal SSE.
2. `consumeAIStream` preserves that observation separately from transient overlay state.
3. `orchestrateFallbackTurn` carries previous observations into the next authorized attempt.
4. `aiMoveRequestBody` forwards the bounded history and turn anchor from both gameplay and the diagnostic harness.
5. The successful route attaches prior attempts plus its current observation to the existing move/pass/exchange submission.

Expose the authoritative anchor through `get_ai_context`; discard mismatched carried history. Observation fields never control model selection, retries, budgets, legality, or action choice. Earlier browser-forwarded observations remain explicitly **reported telemetry**, not authenticated execution proof.

The viewer renders chronological events, proposed coordinates, accepted/rejected word verdicts, rejection explanations from stable codes, and expandable **Sanitized parameters** JSON. Backend rescue without a model tool call must not fabricate a `finishMove` event.

Old or missing traces show “Tool-call history was not recorded.” A failed turn without a persisted move creates no replay ply.

## D4 — Telemetry Badges & Completion Sources

Implement `CompletionSourceBadge` using the existing canonical completion-source type:

| Source | Style and label |
|---|---|
| `provider_candidate` | Emerald — Provider candidate |
| `backend_ranked_candidate` | Amber — Backend ranked candidate |
| `repair_candidate` | Indigo — Repair candidate |
| `backend_witness_rescue` | Blue — Backend legal rescue |
| `genuine_no_move_exchange` | Stone — No legal move: exchange |
| `genuine_no_move_pass` | Stone — No legal move: pass |

Unknown values receive neutral “Unknown source” styling. Do not introduce `witness_rescue` as an alias or infer authorship from the selected player model.

Chips show:

- **Attempt 1**, **Attempt 2**, etc.; convert stored zero-based indices only for presentation.
- Actual recorded runtime provider/model.
- Attempt request count and whole-turn reported request count separately.
- **Time to submission**, measured before the successful backend POST.
- Diagnostic **runner wall time** separately when available.

Preserve zero values. Missing values remain “Not recorded”. Incomplete attempt history means request totals are labelled partial; budget charges are never presented as measured provider requests.

Source precedence is explicit: use the new trace for its own attempt data, existing move metadata for legacy runtime/completion summaries, and labelled `DiagnosticPly` fields for diagnostic measurements. Show conflicting recorded values rather than silently reconciling them.

A minimax/out-play description requires an observed strategic search marker. `backend_ranked_candidate` alone does not prove minimax or optimality. Distinguish `exact`, `bounded`, `pre_endgame`, and `board_control`.

## D5 — Word Authority & Lexicon Inspection

Capture the backend certification while persisting each accepted word:

- Authority name: `WordAuthority`.
- `valid: true`, taken from the existing successful authority verdict.
- Physical tile count and `authority.route(word)` result.
- Main lexicon identifier from the dictionary filename stem.
- Selected two-tile lexicon identifier when that route applies.
- Human-readable lexicon source from the variant manifest.

This records the authority used at move time, without re-running dictionary lookup when replay opens. Frontend cannot supply or override this certification.

The UI distinguishes:

- **Persisted move:** backend-certified formed word.
- **Candidate event:** recorded validation response for a proposed move.
- **Legacy record:** stored accepted move; detailed certification unavailable.

Use physical tile count, never string length, when explaining two-tile routing.

**AI Judge boundary:** the current placement pipeline does not invoke the standalone Judge route, and its responses have no persisted move association. New move-pipeline observations may explicitly report “AI Judge not consulted by this pipeline”; legacy records say “Judge consultation was not recorded.”

This slice adds no automatic Judge calls and no invented verdict or rationale. Linking independently requested Judge consultations to moves requires a separate product flow; the conditional Judge-verdict display has no current producer.

## D6 — Diagnostic Ply Integration

Use the already serialized `diagnostic_ply` directly in Engine & Search:

- `model_authored`
- `first_validate_valid`
- `valid_candidate_count`
- `model_legal_score` versus `ranked_best_score`
- `ranked_search_complete`
- `playability_status`
- Assist mode, score authority, runtime mode, terminal cause, and runner timing

Display null as **Not measured**, false as **No**, and zero numerically. The current runner deliberately leaves several fields null; UI work must not turn those into measured outcomes.

Keep diagnostic observations separate from metrics derived from the new tool trace. Do not backfill `DiagnosticPly` columns or duplicate the new trace into its arbitrary `ai_trace` field.

The backend currently returns a diagnostic ply only when exactly one is associated with the move. For null, say “No unambiguous diagnostic ply attached”; do not choose an arbitrary record.

Keep fake-runtime labels visible. A fake run is not evidence of a live provider invocation.

## D7 — Component Testing & Verification

**Backend tests**

- Score snapshots: DL/TL, multiple word multipliers, consumed premiums, main plus cross-words, blanks, multigraphs, and seven-tile bingo.
- Equality between captured equations and existing scorer totals; default search scoring avoids detail allocation.
- Certification routing through existing authority, including Slovak two-tile rejection and longer-word acceptance. Preserve the frozen parity oracle unchanged.
- Metadata projection: forbidden fields, oversized traces, invalid tokens/coordinates, truncation, legacy payloads, and malformed telemetry accompanying a legal move.
- Persistence for AI placement/pass/exchange and human word details.
- Replay remains staff-only, with old payloads and ambiguous diagnostic associations covered.

**Vitest**

Use the existing Node environment and server-render component-test pattern; add no testing dependency.

- Pure score-formatting and reconciliation tests.
- Every completion badge, unknown values, null/false/zero metrics, and conflicting sources.
- Accepted/rejected candidates, repair markers, sanitized JSON escaping, truncated/incomplete traces.
- New and legacy replay parsing; invalid optional details must not discard the whole replay.
- Route collection with fake models: success, rejected-then-valid, repair, backend rescue, engine-only completion, timeout, and late callbacks.
- Multi-attempt carry-forward, anchor mismatch, aggregate request accounting, and unchanged fallback budget/reconciliation behavior.
- Existing AI stream, fallback, route, diagnostic, admin replay, replay-engine, and 300-turn simulation suites.

**Playwright acceptance**

Use the available Playwright browser tools against an isolated local verification copy, existing dependencies, synthetic Django data, and fake provider execution. No package installation or external provider calls.

The implementation/acceptance prompt must explicitly include temporary verification files, local servers, test database, synthetic accounts, browser storage, screenshots, and cleanup. Exclude real `.env` files from the copy; Next.js and Django automatically load them.

Verify the actual `/admin/replay/[id]/` route at 1440×900, 1024×768, and 390×844:

- Staff access, real API loading, seek/open/tab switching, pause behavior, and keyboard focus.
- Board and racks remain unobscured; no horizontal page overflow.
- A backend-created scoring fixture agrees with the displayed equation.
- A fake recorded AI turn shows rejected/accepted proposals and completion source.
- Legacy, partial replay, null diagnostic metrics, reduced motion, and Premium Look off.
- No provider request occurs during replay inspection.

Run project quality checks in that isolated copy, including frontend typecheck/lint/build and backend Ruff/mypy/pytest. The build remains prohibited during this planning exchange. Record browser evidence separately from unit-test evidence.

## D8 — Implementation Order, Allowlists & Evidence Tier

**Ordered slices**

1. Add shared inspection contracts and bounded TypeScript/Python projection tests.
2. Capture opt-in scoring details and word certification during existing move persistence.
3. Collect tool events and search summaries; carry bounded observations across fallback attempts.
4. Extend replay parsing and implement inspector tabs, equations, badges, and diagnostics.
5. Run automated checks and isolated Playwright acceptance.
6. Review the exact diff, compatibility, trace limits, and cleanup evidence before reporting implementation completion.

**Frontend allowlist — exact proposed files**

```text
frontend/src/lib/types.ts
frontend/src/lib/admin-replay.ts
frontend/src/lib/admin-replay.test.ts
frontend/src/lib/admin-replay.fixtures.ts
frontend/src/lib/admin-move-inspection.ts
frontend/src/lib/admin-move-inspection.test.ts
frontend/src/lib/ai-inspection-trace.ts
frontend/src/lib/ai-inspection-trace.test.ts
frontend/src/lib/ai-fallback.ts
frontend/src/lib/ai-fallback.test.ts
frontend/src/lib/ai-move-stream.ts
frontend/src/lib/ai-move-stream.test.ts
frontend/src/lib/ai-play-diagnostic.ts
frontend/src/lib/ai-play-diagnostic.test.ts
frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
frontend/src/app/game/[id]/page.tsx
frontend/src/components/admin/ReplayStudio.tsx
frontend/src/components/admin/ReplayMoveDetails.tsx
frontend/src/components/admin/ReplayMoveDetails.test.ts
frontend/src/components/admin/ReplayMoveInspector.tsx
frontend/src/components/admin/ReplayMoveInspector.test.ts
frontend/src/components/admin/ReplayScoreBreakdown.tsx
frontend/src/components/admin/ReplayScoreBreakdown.test.ts
frontend/src/components/admin/ReplayToolTimeline.tsx
frontend/src/components/admin/ReplayToolTimeline.test.ts
frontend/src/components/admin/ReplayEngineDetails.tsx
frontend/src/components/admin/ReplayEngineDetails.test.ts
frontend/src/components/admin/CompletionSourceBadge.tsx
frontend/src/components/admin/CompletionSourceBadge.test.ts
frontend/src/components/admin/admin.module.css
```

**Backend allowlist — required by the Cooperator’s expanded scope**

```text
backend/gamecore/types.py
backend/gamecore/scoring.py
backend/game/services.py
backend/game/serializers.py
backend/game/replay.py
backend/game/inspection.py
backend/tests/test_move_inspection.py
backend/tests/test_admin_replay_api.py
backend/tests/test_api.py
```

Additive optional fields retain replay schema version `1`. Existing JSON columns hold the new evidence; no model migration, historical rewrite, dependency change, provider enablement, dictionary change, or Judge integration is required.

Deploy backend support before frontend collection. Old clients ignore additional fields; new clients tolerate missing inspection records. Roll back the frontend collector/UI first and backend support second. Retained JSON is ignored by older code; no destructive cleanup is needed.

**Evidence tier:** E0 for this read-only planning exchange. **Proposed E2 for implementation:** reversible changes across backend persistence, AI orchestration, and UI, with bounded observational data and unchanged legality/access decisions. Review trace projection and staff-only replay exposure explicitly. Any implementation that grants telemetry authority, exposes it to new audiences, or requires privileged infrastructure changes must return for reassessment.

**Orchestration critique**

- **MEASURED:** the original full baseline SHA differed from HEAD; continued planning now rests on explicit Cooperator authorization.
- **MEASURED:** complete tool history requires collection changes beyond the original frontend allowlist; the Cooperator selected that expansion.
- **MEASURED:** existing diagnostic metrics contain deliberate nulls; no persisted Judge association exists.
- **MEASURED:** prior slice browser evidence was absent. This plan specifies the temporary environment and acceptance authority needed to close that gap.

Enumeration widened: scoring capture, AI metadata sanitization, SSE terminal parsing, fallback carry-forward, and the diagnostic frontend harness. Standalone Judge association and diagnostic-runner metric enrichment remain outside this slice.

Visible context pressure: moderate; sufficient for the completed design.

Report justification: new-evidence

Authority expiry: this report ends the renewed read-only planning work. It grants no implementation, mutation, network, or publication authority.

Smallest next step: ORCHESTRATOR reviews this expanded plan and issues a fresh implementation-worker prompt against the accepted full SHA, using these allowlists and the isolated verification envelope.
