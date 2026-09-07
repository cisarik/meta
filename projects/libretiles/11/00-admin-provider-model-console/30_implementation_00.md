You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An accepted plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 30
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Implementation Worker
Task identity: APMC-S8-IMPL — probe history child table, bounded Node probe worker (fake default), reviewed fallback ordering / activation controls in Django admin with atomic transaction and zero-selectable refusal, and XSS-safe templates. Provider calls: ZERO.
Phase: implementation
Implementation authority: explicit
Exact baseline: 4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
Changed-path allowlist: exactly the paths in section 4
Implementation boundaries: positive and negative authority in sections 3-5
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: admin-controlled fallback ordering and probe history child table; probe execution reusing existing provider-capability.ts in fake mode; no live provider calls. Independent audit follows landing.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks:
1. **Catalog bricking / zero selectable models**: An admin deactivating all models or all tools-tagged models renders gameplay unplayable. Refusal invariants must hold across both `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` and `true`.
2. **XSS in Django Admin**: Django Admin is session-authenticated and is NOT covered by the Next.js CSP (`proxy.ts`). Persisting model IDs, probe error messages, or provider strings and rendering them with `|safe`, `mark_safe()`, or raw HTML creates stored XSS leading to admin account takeover.
3. **Unbounded probe spend / blocking worker**: A synchronous probe triggering external LLM calls can block workers. Probes must be bounded (20s capability deadline, 22s worker watchdog, 25s subprocess deadline, max 4 outbound HTTP dispatches, 60s global admission throttle, fake-by-default with zero provider calls).
4. **CSRF / AuthN/Z bypass on reorder or probe trigger**: Every state-changing admin action (triggering a probe, altering `sort_order`, toggling `is_active`) must be a POST protected by CSRF and staff + model authorization (`admin_view`).
5. **Race conditions in fallback order updates**: Bulk reordering of `sort_order` across multiple models must execute atomically in a single database transaction with write serialization on `CatalogAdminControl`.
6. **Command execution rule (RF-16)**: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use `.venv/bin/python` and `.venv/bin/pytest`.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
PROMPT_CONTRACTS.md:203     the phase-result enum. Expected Worker result spelling:
                            `implementation-PASS`. Planning uses `not-applicable`; do not invent
                            a third spelling.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading — by symbol; re-measure every symbol before you use it

```text
/home/agile/Projects/libretiles/AGENTS.md
backend/catalog/models.py         AIModel, AIPrompt
backend/catalog/admin.py          AIModelAdmin, sync_models_view
backend/catalog/selection.py      get_selectable_models, is_selectable_model, DIRECT_FREE_RIVAL_PAIRS, FREE_RIVAL_PAIRS
backend/catalog/openrouter_sync.py  sync_openrouter_catalog (preserves sort_order and is_active)
backend/catalog/management/commands/seed_models.py (preserves sort_order and is_active)
frontend/src/lib/provider-capability.ts   probeProviderCapability, PROVIDER_CAPABILITY_STATUSES
frontend/scripts/diagnostic-resolve-hooks.mjs  plain Node import hook for TypeScript
backend/tests/test_admin.py       admin testing pattern
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start and before commit
```

If `main` has advanced past `4c524ec`: re-gate against the THEN-HEAD, state the new baseline in
your report, and continue — your allowlist and claims do not change. Any other divergence:
classify with the five recovery-candidate classes at AP.md:1464-1476 and STOP.

## 2. Goal

Implement Slice 8 as designed in the accepted plan (`APMC-S8-PLAN`):
1. **Capability probe history**: child table `CapabilityProbe` (`catalog_capability_probe`) linked to `AIModel`, tracking status, latency, outbound count, mode (`fake` | `live`), reason code, fixed server summary. Retention bounded to newest 100 observations per `AIModel`, auto-pruned on write. Read-only admin view with clear fake-PASS simulated label.
2. **Dedicated Node probe worker**: `frontend/scripts/probe-worker.mjs` running single-shot IPC calling `probeProviderCapability` via `diagnostic-resolve-hooks.mjs`. Default is `fake` mode (0s, 0 egress, simulated PASS, no subprocess). Explicit `live` mode is gated by `PROVIDER_PROBE_LIVE === "1"` with closed provider credential env whitelist, 20s capability deadline, 22s watchdog, 25s subprocess deadline, max 4 HTTP dispatches.
3. **Reviewed fallback-order and activation controls**:
   - `CatalogAdminControl` singleton coordination model (`revision`, `ordering_reviewed`, `probe_not_before_at`).
   - Two-step reviewed workflow: Review POST computes diff and signed 10-minute token -> Apply POST commits changes in `transaction.atomic()` with write-serialization.
   - Refusal invariants fail closed: refuse leaving zero selectable models under `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` OR `true`; refuse deactivating the last active model with the `"tools"` tag.
   - Direct-edit bypasses closed: remove `list_editable` on `AIModelAdmin`; make activation/sort_order read-only on ordinary changeform.
   - Seed and sync preserve operator `sort_order` and `is_active`.
4. **Template and presentation safety**: Strict HTML escaping in Django admin templates (NO `|safe`, NO `mark_safe()`, NO `autoescape off`). CSRF on all mutation POSTs. Staff and model permissions checked.
5. **Boundary isolation**: Probe history and ordering cover `AIModel` only in this slice. `DiagnosticTarget` and `DiagnosticAllowedHost` remain untouched and isolated.

## 3. Required behaviour & implementation steps

Follow the accepted sequence:
1. **Failing tests first**: Create test files covering F01–F19 from the plan before modifying production code.
2. **Schema & Migration**: Add `CapabilityProbe` and `CatalogAdminControl` to `backend/catalog/models.py`. Create migration `0013_admin_provider_model_console.py` depending on `0012_multi_provider_free_rivals` and the swappable user model.
3. **Selection helper & Preview**: Update `backend/catalog/selection.py` / `admin_controls.py` to support reviewed ordering (respecting direct rivals sort_order, compatibility segment sort_order, dynamic OpenRouter freshness, NIM last, `ordering_reviewed` toggle). Implement refusal invariant validators.
4. **Admin review workflow**: Implement `controls/` review and apply endpoints in `backend/catalog/admin.py` with signed tokens and CSRF. Create templates in `backend/catalog/templates/admin/catalog/aimodel/`.
5. **Probe worker & Subprocess**: Create `frontend/scripts/probe-worker.mjs` and `frontend/src/lib/admin-provider-probe.ts`. Wire Python subprocess caller in `backend/catalog/provider_probes.py`.
6. **Admin probe action**: Add POST `/admin/catalog/aimodel/<id>/probe/` action and changelist/changeform integration.
7. **Verification**: Run all focused tests, regressions, type checks, and linters.

## 4. File allowlist

You may create or edit ONLY these paths:

```text
backend/catalog/models.py
backend/catalog/admin.py
backend/catalog/selection.py
backend/catalog/admin_controls.py
backend/catalog/provider_probes.py
backend/catalog/openrouter_sync.py
backend/catalog/management/commands/seed_models.py
backend/catalog/migrations/0013_admin_provider_model_console.py
backend/catalog/templates/admin/catalog/aimodel/change_list.html
backend/catalog/templates/admin/catalog/aimodel/change_form.html
backend/catalog/templates/admin/catalog/aimodel/controls.html
backend/tests/test_catalog_admin_controls.py
backend/tests/test_provider_probe_history.py
backend/tests/test_provider_probe_worker.py
backend/tests/test_catalog_admin_console_migration.py
frontend/scripts/probe-worker.mjs
frontend/src/lib/admin-provider-probe.ts
frontend/src/lib/admin-provider-probe.test.ts
frontend/src/lib/admin-provider-probe.worker.test.ts
frontend/src/lib/provider-capability.ts
frontend/src/lib/provider-capability.test.ts
backend/.env.example
README.md
docs/architecture.md
```

Existing files outside this list are read-only. In particular: do NOT touch `.ap/`, `backend/game/**`, existing migrations `0001`–`0012`, `frontend/src/app/**`, lockfiles, or package manifests.

## 5. Invariants you must not break

1. **Provider calls: ZERO during tests/implementation.** Default mode is `fake`. `PROVIDER_PROBE_LIVE` must NOT be set in automated tests.
2. **Template safety: NO `|safe`, NO `mark_safe()`, NO raw HTML injection.** Every model ID, provider, summary, and message is auto-escaped.
3. **Zero-selectable refusal:** Refuse any review that leaves 0 selectable models under either `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` or `true`.
4. **Last tools-model refusal:** Refuse deactivating the last active model carrying the `"tools"` tag.
5. **Atomic review & write lock:** Fallback order updates must run in `transaction.atomic()` with serialization via `CatalogAdminControl`.
6. **Seed and sync preservation:** `seed_models` and `sync_openrouter_models` must NOT overwrite operator `sort_order` or `is_active` on existing rows.
7. **DiagnosticTarget isolation:** No FK from `CapabilityProbe` to `DiagnosticTarget`. No crossover into `backend/game/**`.
8. **No secret materialization (R2=A):** Never write credentials to the database, logs, or reports.
9. **No full Provider entity:** Do not invent a Provider model.
10. **RF-16 environment rule:** Never pass or type `PYTHON_DOTENV_DISABLED=1` on your shell commands. Use `.venv/bin/python` from `backend/`.

## 6. Validation sequence

Execute from `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_catalog_admin_controls.py tests/test_provider_probe_history.py tests/test_provider_probe_worker.py tests/test_catalog_admin_console_migration.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

Execute from `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-provider-probe.test.ts src/lib/provider-capability.test.ts
```

## 7. Git commit and push

When all tests and checks pass:
1. Stage ONLY the allowlisted files touched using explicit paths:
   ```bash
   git add <explicit path 1> <explicit path 2> ...
   ```
2. Verify staged diff and status:
   ```bash
   git diff --staged
   git status --porcelain=v1
   ```
3. Commit with a concise message:
   ```bash
   git commit -m "feat(catalog): add capability probe history and reviewed fallback order controls"
   ```
4. Verify remote baseline equality before push:
   ```bash
   test "$(git ls-remote origin refs/heads/main | cut -f1)" = "4c524ec3020bbd2f27f2ce32ac160d2c40469c0e"
   ```
5. Push fast-forward:
   ```bash
   git push origin main
   ```
6. Verify public readback:
   ```bash
   test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
   ```

## 8. Report format and stopping conditions

Submit exactly ONE standard AP terminal report beginning with:
```text
### Report for ORCHESTRATOR_CHAT
```
Echo coordinates:
```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 30, Worker exchange ordinal: 01
```
Phase-qualified result: `implementation-PASS`.
Status: `PASS`, `PARTIAL`, or `BLOCKED`.
Include compact core items 1–11 per `PROMPT_CONTRACTS.md:18-37`.
Report justification: new-mutation

⛔ Your authority ends at pushing the commit and submitting the report. Do not start re-audit, K1, slice 8 acceptance, or 14/00.
