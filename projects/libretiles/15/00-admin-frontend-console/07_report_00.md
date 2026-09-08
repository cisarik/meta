### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-frontend-console  
Worker session ordinal: 07, Worker exchange ordinal: 01

**Slice 4 technical design: Simulation Playground & Match Launcher**

```text
Status: PASS — repository-grounded advisory planning report
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4
End commit: e2c2549dbbe5b6a2545918cef66d4624a4ceb7d4
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Repository gate: clean `main` at the exact baseline; `.ap` gitlink is `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. Required request, guidance, prior report, and relevant implementation surfaces were inspected. No network, browser navigation, provider call, secret-file access, build, test execution, or mutation occurred. Evidence is E0 and non-independent.

### D1 — Match configuration and setup form

Replace the existing playground placeholder with a client-side `SimulationPlayground` under the current `AdminAccessGate`. Keep the console’s English copy and existing gold/black styling.

Each slot has:

- Category: **AI Model** or **Local Engine CPU**.
- AI Model: searchable live-catalog selector, showing provider and model names; independent Prompt Preset selector.
- CPU: fixed **CPU Master**, identity `engine/engine/cpu` expressed as provider `engine`, model ID `engine/cpu`; preset control disabled with “CPU uses the local search policy.”
- Prompt presets modify an LLM’s strategy; they are not standalone opponents. Load selectable presets from `/api/catalog/prompts/`, preserving customized content.

Fetch models, prompts, and playable variants independently. CPU configuration must remain usable when model or prompt loading fails.

Use `PremiumPicker` for the variant selector. Offer the twelve shipped variants in locale order, with these endonyms:

English, Slovenčina, Čeština, Polski, Deutsch, Português, Íslenska, Italiano, Nederlands, Dansk, Svenska, Afrikaans.

Use an explicit partial slug-to-flag mapping and conditional `flagSrc`, following the existing settings implementation. Only backend-returned playable variants are launchable.

**Defaults and controls**

- CPU Master versus CPU Master; English variant.
- Seed: integer `0…2147483647`. Blank means server-generated; show the resolved seed after launch. “Randomize” fills a seed using browser cryptographic randomness.
- For an LLM slot, default to live catalog row 1 and selectable `Initial`; if `Initial` is unavailable, use prompt row 1. If no presets exist, use the TypeScript CORE alone.
- Snapshot `aiTimeout` and `aiMaxSteps` from Settings into the launch form; show editable advanced controls bounded to existing runtime limits: timeout `1…600` seconds, steps `5…100`.
- Quick presets: CPU/CPU, Gemma 4 31B/CPU, NVIDIA NIM Nemotron/Gemma 4 31B. Disable a model-specific shortcut when its exact pair is unavailable; never silently substitute another model.
- Lock configuration after creation. Starting another configuration requires finishing or stopping the current simulation.

“Start Simulation” creates the match, displays the initial board and both racks, then begins autoplay after the selected inter-turn delay.

### D2 — Backend simulation endpoint and session persistence

**Repository findings**

`create_game()` creates a human slot and one AI slot. `create_diagnostic_game()` creates two AI slots, but also creates a globally constrained `DiagnosticRun`, assigns its reserved service account, and accepts one shared preset. The diagnostic command remains fake-only. Neither creator should be repurposed as the browser launcher.

`engine/cpu` is a synthetic frontend identity; it is not a selectable Django catalog row. Do not create a catalog row merely to launch CPU matches.

**Chosen persistence**

Add `PlaygroundSimulation`, linked one-to-one to `GameSession`, containing:

- Creator, immutable normalized configuration snapshot, and nullable `ended_at`.
- Nullable lease UUID, leased move count, and lease expiry.
- A conditional unique constraint allowing one unfinished playground simulation per creator.

The configuration snapshot records both slot kinds, model/provider/display identities, preset identities, CPU policy where applicable, resolved seed, and turn limits. Existing `PlayerSlot.ai_model` and `.ai_prompt` hold the LLM relationships. CPU slots have null model/prompt relationships and policy `POLICY_RANKED_WITNESS_SAFE` in the simulation configuration.

Create the session transactionally with:

- `game_mode="vs_ai"`, `is_diagnostic=False`.
- Two `is_ai=True` slots, both with `user=None`.
- Null session-level model/prompt, avoiding accidental inheritance across seats.
- Initialization through `_initialize_session()`, preserving the starting draw, seeded bag, and `replay_initial_state`.

No `DiagnosticRun`, `DiagnosticPly`, service-user token, subprocess, or background worker is created.

**Public Django interfaces**

| Endpoint | Contract |
|---|---|
| `POST /api/admin/simulate/` | Accept `slot0`, `slot1`, `variant_slug`, optional `seed`, `ai_timeout`, `ai_max_steps`; return HTTP 201 with complete initial simulation state. |
| `GET /api/admin/simulate/<game_id>/` | Return current authoritative state for staff viewing and reconciliation. |
| `POST /api/admin/simulate/<game_id>/step/` | Accept `expected_move_count`; execute one CPU turn or grant one LLM turn lease. |
| `POST /api/admin/simulate/<game_id>/action/` | Closed, lease-bound LLM execution adapter described in D3. |
| `POST /api/admin/simulate/<game_id>/stop/` | Idempotently stop the simulation and revoke its lease. |

A slot request is either `{kind:"cpu"}` or `{kind:"llm", provider, model_id, prompt_id}`. Reject unknown fields, diagnostic target IDs, runtime URLs, credentials, invalid/inactive model pairs, unavailable presets, and non-playable variants. Invalid explicit choices never fall back during creation.

All endpoints use the existing password-aware JWT/session authentication, `IsAuthenticated`, and `IsAdminUser`. Any staff member can inspect; only the creator can advance or stop. Ordinary gameplay endpoints remain membership-gated, and neither simulation seat supplies that membership.

Return a versioned `SimulationState` containing game ID, resolved configuration, move count, current slot, board, premiums used, both racks, scores, bag count, player labels, terminal fields, in-flight status, latest committed move, and replay URL. Never return bag order, provider configuration, or leases from the public state endpoint.

A conflicting unfinished simulation returns 409 with its game ID so the UI can reopen it.

### D3 — Turn advancement and execution pipeline

Use **Option A as the execution primitive, with Option B as its browser controller**. Each request advances at most one turn; autoplay schedules those requests sequentially. This provides visible progress and pause/step controls without requiring a persistent runner.

**CPU turn**

The Django step service:

1. Verifies staff ownership, active status, expected move count, and absence of an active lease.
2. Derives the acting slot from `current_turn_slot`.
3. Searches with `_probe_ai_ranked_candidates()` and takes the first ranked candidate.
4. If ranking supplies none, uses `_probe_ai_playability()`: place its witness when found; exchange/pass only on certified `none`; return `playability_unknown` without mutation on `indeterminate`.
5. Rechecks the lease and turn under lock, then commits through existing `_submit_*_locked()` services.

This implements `POLICY_RANKED_WITNESS_SAFE` semantics using the existing persisted-game search adapters. Do not run `simulate_engine_game()` and later copy its result into Django.

Search runs outside long database transactions against the claimed position. Commit revalidation remains authoritative. CPU metadata records zero provider requests and the applicable existing completion source.

**LLM turn**

Add one browser-facing Next.js endpoint:

`POST /api/admin/simulate/[id]/turn/`

It accepts a staff bearer token and `{expected_move_count}`. Both CPU and LLM turns use this entrypoint, returning a consistent progress stream.

For an LLM:

- Next calls Django `step/`, which atomically grants a lease and returns the acting seat’s authorized context, immutable preference, preset, and limits.
- Extract the existing AI move executor into a server module with an injected backend transport. Keep `/api/ai/move` as a thin wrapper using its existing transport and behavior.
- The simulation transport maps context, candidates, playability, validation, and terminal commits to the lease-bound admin adapter. It cannot call arbitrary paths or patch the selected model.
- Run the existing `buildFallbackQueue()` and `orchestrateFallbackTurn()` on the server. Preference is attempt 1; remaining eligible pairs keep catalog order; maximum three attempts share one timeout and provider-request budget.
- Forward candidate/tool/attempt progress. Emit the outer successful terminal only after Django state confirms a committed move.

The admin `action/` endpoint accepts a closed operation enum: `candidates`, `playability`, `validate`, `place`, `exchange`, `pass`, `release`. Every operation verifies creator, simulation, lease, expiry, and unchanged move count. Placement and exchange payloads reuse existing serializers and metadata sanitization.

Factor context construction and placement validation into helpers accepting an already-authorized session and acting slot. Existing gameplay callers retain their current authorization loaders.

**Concurrency and recovery**

- Lease identity binds the original move count; a late request cannot act for the next AI seat.
- Lease expiry is the granted turn timeout plus 15 seconds for completion/reconciliation.
- Claim, commit, stop, and release use short atomic transactions with consistent simulation-then-session locking.
- Successful commit clears the lease atomically. Release only clears the matching lease. Expired leases permit recovery; their old callbacks cannot commit.
- Stale counts, duplicate requests, and occupied leases return 409 before provider execution.
- Disconnects and missing SSE terminals trigger state reconciliation, never a blind repeat. A committed turn is recovered from Django; an unresolved turn remains paused until its lease clears/expires.

**Browser controller**

States: configuring, starting, running, pausing, paused, stepping, stopping, finished, stopped, error.

Autoplay uses a completion-based timer with delays of 0.5, 1, or 2 seconds; default 1 second. Never use an overlapping interval. Pause stops scheduling and lets the current turn settle. Step performs exactly one turn and stays paused. Reloading `/admin/playground?game=<id>` restores the simulation paused.

Unmount cancels timers and requests. Propagate simulation cancellation into the executor and suppress repair/rescue work after cancellation; backend lease checks remain the final protection against late commits.

### D4 — Live arena board and dual racks

Reuse `ReplayBoard`, `DualRackVisualizer`, `Tile`, and the admin CSS.

Add backward-compatible presentation props:

- `ReplayBoard`: accessible label defaults to “Replay board”; playground supplies “Live simulation board.”
- `DualRackVisualizer`: live mode labels the current slot “Thinking” or “Next to play,” preserving existing replay wording by default.

Render committed state only. Provider candidates appear in the thinking/progress surface and never populate the board.

- Animate the latest committed placement delta using move count as `frameKey`.
- Replace both racks and scores together from one authoritative snapshot.
- Preserve atomic tile tokens, blank assignments, and zero blank values.
- Show a green/blue score differential indicator with numerical scores and signed spread; handle ties and negative scores without dividing by total score.
- Maintain a bounded ticker of the latest 50 committed moves, deduplicated by sequence. Build commentary from persisted words, acting slot, runtime identity when available, and points.
- Distinguish pass, exchange, and final rack adjustments from word scores.
- Use restrained `aria-live` announcements for completed turns. Respect reduced motion and Premium Look off.

Desktop places the board beside the racks/progress/ticker; narrow screens stack them. Controls remain keyboard-operable.

### D5 — Endgame and Replay Studio transition

Normal completion uses `_check_endgame()` and its existing rack adjustments, winner calculation, and persisted terminal snapshots.

Display:

- Winner or draw, both final scores, and signed spread.
- Actual game-end reason.
- **Open in Replay Studio →**, linking directly to `/admin/replay/<game_id>`.

Stopping is an administrative interruption, not a player resignation:

- Under lock, revoke the lease and set `game_over=True`, `status="abandoned"`, `game_end_reason="simulation_stopped"`, `winner_slot=None`, `current_turn_slot=None`, and finish timestamps.
- Preserve scores, board, racks, and all existing moves.
- Do not invent a `give_up` move or apply normal endgame deductions.
- Show “Simulation stopped” and the replay button, without a victory claim.

Finish `PlaygroundSimulation.ended_at` in the same transaction as any terminal transition.

Use existing replay capture for every committed action. Extend replay/admin player identity projection to use the simulation configuration snapshot, ensuring CPU Master and deleted/renamed LLM identities remain understandable. Reuse one projection helper across replay and game-list serialization.

A stopped match remains fully captured up to its last committed turn. `replay_status="complete"` describes capture completeness, not natural game completion. Keep `diagnostic_ply=null`; do not fabricate diagnostic evidence.

### D6 — Security, performance, and resource boundaries

- Preserve existing staff authentication and CSRF behavior. New mutation views explicitly permit POST; the existing `_AdminAPIView` currently allows only GET/HEAD/OPTIONS.
- Recheck authorization at Django execution endpoints; the frontend gate is presentation only.
- Retain private/no-store responses and `Vary: Authorization, Cookie`.
- Add scoped throttles: creation `10/hour`, turn claims `120/minute` per authenticated user. Do not put model tool requests under the existing `ai_context` rate intended for normal gameplay.
- One unfinished simulation per creator and one lease per simulation bound concurrency.
- Bound simulations to 300 committed plies. If the match has not naturally ended, stop with `simulation_ply_limit`, preserving the replay and showing no winner.
- Reuse existing bounded ranked/witness searches, including `indeterminate` handling. CPU Master is a bounded strategic engine, not a guarantee of optimal play.
- Enforce the granted provider-request ceiling in the request tracker immediately before outbound provider/IAM calls. Add an optional limit to runtime construction; preserve unlimited/default behavior for existing callers. This prevents HTTP accounting from exceeding `aiMaxSteps` through setup calls.
- Preserve `maxRetries:0`, sequential fallback, repair reserves, request accounting, and existing provider Retry-After handling. Exhaustion pauses the browser; it must not synthesize a move.
- CPU execution never constructs an AI runtime or fetches an external catalog. Skip websocket publication for playground sessions; browser HTTP/SSE supplies updates.
- CPU/CPU means **zero external provider calls**. Local browser/server HTTP and CPU search still have latency.
- No new dependencies, provider URLs, credentials, diagnostic targets, catalog changes, schedules, or deployment configuration belong to this slice.

### D7 — Unit, integration, and Playwright verification

**Django**

Add focused tests covering:

- Anonymous/non-staff denial, creator-only mutation, session CSRF, and unchanged ordinary-game access.
- CPU/CPU, CPU/LLM, and LLM/LLM creation; separate presets; all twelve variants; reproducible initial state for a fixed seed.
- Strict invalid-pair/preset/seed/config rejection with no partial records.
- CPU ranked placement, witness rescue, genuine no-move exchange/pass, and indeterminate refusal.
- Duplicate/stale claims, competing tabs, expired leases, stop/commit races, and late callbacks after slot changes.
- Natural final scoring, stopped games, 300-ply termination, and complete replay capture.
- Correct CPU/model labels without diagnostic records.

Use transaction-aware concurrency tests against the intended database behavior; mocked request order alone is insufficient evidence.

**Vitest**

Use the repository’s existing Node environment, pure controller tests, fake timers, and static React rendering:

- Form defaults, category transitions, independent presets, unavailable shortcuts, seed validation, and flags.
- Sequential scheduling; pause during a turn; one-step behavior; cleanup; stale responses; lost-terminal reconciliation.
- Arena blanks/multigraphs, placement highlights, dual-rack updates, negative scores, ties, ticker deduplication, and terminal copy.
- Next turn route authorization failures, CPU short-circuit, immutable seat preference, bounded fallback, cancellation, and no provider calls after failed claims.
- Provider/IAM request-limit enforcement.
- Existing move route, fallback, stream, diagnostic-target, 300-turn simulation, replay, and inspector regressions.

Run backend Ruff/mypy and affected pytest suites; frontend typecheck/lint and affected Vitest suites. Any build belongs only to later explicit execution authority.

**Playwright acceptance**

The session exposes Playwright browser tools; the repository has no committed Playwright harness. Use those tools in a separately authorized acceptance session without installing a package.

Use isolated synthetic staff/non-staff accounts and disposable local services/database, with external egress denied.

1. Verify login redirect and non-staff denial.
2. Open `/admin/playground`; confirm twelve variants and independent slot controls.
3. Start English CPU/CPU with seed `0`; verify the initial racks and server-selected starting slot.
4. Observe several committed placements, rack replacements, score changes, ticker entries, and placement highlights.
5. Pause and confirm no further turns after the in-flight turn settles; step once; resume at different delays.
6. Allow the unmocked match to reach natural completion and verify final scores and winner/draw.
7. Open Replay Studio, seek to the final ply, and compare its board, racks, scores, and game ID with the arena.
8. Launch a second match and stop during execution; verify the stopped banner, stable state, and replay link.
9. Check narrow layout, keyboard access, reduced motion, Premium Look off, console errors, and missing flags.

A seed-0 run that stalls or reaches the cap is not natural-completion PASS. Report it directly; do not substitute a mocked victory. CPU route/runtime tests plus denied server egress establish zero provider calls—browser request logs alone cannot prove that.

### D8 — Implementation sequence, path allowlist, and evidence tier

**Sequence**

1. Add simulation persistence, strict request/state contracts, and creation.
2. Add lease-bound CPU stepping, stop behavior, and replay identity projection.
3. Extract the shared AI executor while preserving existing route behavior; run its regression suite.
4. Add the admin transport, server fallback orchestration, and provider-request ceiling.
5. Implement the form, browser controller, arena, and replay transition.
6. Run focused positive/negative checks, then separately authorized browser acceptance and independent review.

**Exact proposed path allowlist**

Existing backend files:

```text
backend/config/settings.py
backend/game/models.py
backend/game/services.py
backend/game/admin_urls.py
backend/game/admin_serializers.py
backend/game/replay.py
backend/game/realtime.py
backend/tests/test_admin_replay_api.py
```

New backend files:

```text
backend/game/migrations/0014_playground_simulation.py
backend/game/simulations.py
backend/game/simulation_views.py
backend/game/simulation_serializers.py
backend/tests/test_admin_simulation_api.py
backend/tests/test_simulation_services.py
backend/tests/test_simulation_concurrency.py
```

Existing frontend files:

```text
frontend/src/app/admin/playground/page.tsx
frontend/src/app/admin/layout.tsx
frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
frontend/src/components/admin/ReplayBoard.tsx
frontend/src/components/admin/ReplayBoard.test.ts
frontend/src/components/admin/DualRackVisualizer.tsx
frontend/src/components/admin/DualRackVisualizer.test.ts
frontend/src/components/admin/admin.module.css
frontend/src/lib/api.ts
frontend/src/lib/ai-runtimes.ts
frontend/src/lib/openai-compatible.ts
```

New frontend files:

```text
frontend/src/app/api/admin/simulate/[id]/turn/route.ts
frontend/src/app/api/admin/simulate/[id]/turn/route.test.ts
frontend/src/lib/ai-move-execution.ts
frontend/src/lib/admin-simulation.ts
frontend/src/lib/admin-simulation.test.ts
frontend/src/lib/admin-simulation-server.ts
frontend/src/lib/provider-request-limit.test.ts
frontend/src/hooks/useSimulationRunner.ts
frontend/src/hooks/useSimulationRunner.test.ts
frontend/src/components/admin/SimulationPlayground.tsx
frontend/src/components/admin/SimulationSetupForm.tsx
frontend/src/components/admin/SimulationArena.tsx
frontend/src/components/admin/SimulationPlayground.test.ts
```

Keep simulation types and parsers in `admin-simulation.ts`; existing replay interfaces remain compatible. No package/lockfile, lexicon, prompt, catalog, diagnostic-runner, secret, or `.ap` modifications are proposed.

**Evidence-tier disposition**

E2 was requested. **Recommend E3 for the complete implementation** because the selected design adds durable simulation persistence and a new privileged execution path with lease-authorized commits. The cited AP tier rules require separate preflight, checkpoint/rollback evidence, negative-path checks, and fresh independent review before final acceptance. The current planning exchange remains E0.

Rollback should disable launcher/execution routes and restore prior application behavior while retaining simulation records and replay data. Reversing the migration after use would discard simulation ownership/configuration; it is not the default rollback. Production migration, provider execution, publication, and deployment require their own explicit authority.

```text
Orchestration critique:
MEASURED — ordinary creation supports one AI; diagnostic creation uses a
reserved service account, a global in-flight constraint, and a fake-only runner.
MEASURED — CPU identity is synthetic in the frontend, and existing admin views
are read-only. Both require explicit implementation treatment.
MEASURED — the requested E2 designation is below the cited AP triggers for the
proposed durable persistence and privileged execution boundary.
LEAD — browser-only duplicate suppression would permit stale LLM callbacks to
act for the next AI seat; backend lease validation is necessary.

Enumeration widened:
Replay/admin identity projection, realtime publication, provider-request
tracking, and shared executor extraction are included in the allowlist because
they are required consumers of the design. No broader audit is claimed.

Visible context pressure: moderate; sufficient for the bounded design and report.

Report justification: new-evidence
```

Authority expiry: AFC-SLICE-4-PLAN planning authority expires with this report; implementation in this Worker session remains prohibited.

Smallest next step: ORCHESTRATOR reviews the E3 designation and issues the bounded fresh-session preflight for this technical design.
