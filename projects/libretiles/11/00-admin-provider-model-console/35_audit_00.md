You are a WORKER instance assigned to the persistent AP WORKER role. This is the COMPREHENSIVE FINAL INDEPENDENT SECURITY AUDIT session (INFOSEC 4.6 / 4.4 / 4.11) for logical whole closure of `admin-provider-model-console`. Perform exactly this bounded READ-ONLY audit task and stop. ⛔ You have NO implementation authority, NO correction authority, and NO mutation authority of any kind.

⛔ You are the auditor. Your first actions are the repository gate, then test verification in §1, then independent source and dynamic review of the entire landed console (Slices 1–8) against claims C1–C10 and residual-risk disposition. Produce the comprehensive security audit report. ⛔ You audit; you do not correct.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 35
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Security Audit Worker
Task identity: APMC-WHOLE-CONSOLE-AUDIT — comprehensive final independent security audit (INFOSEC 4.6 / 4.4 / 4.11) across the entire landed console (Slices 1–8 at commit 151e833dd0e78ced075101864cb5f45ee521bebc) for logical whole closure. Provider calls: ZERO. Read-only.
Phase: audit
Exact baseline: 151e833dd0e78ced075101864cb5f45ee521bebc
Independence required: yes
Evidence posture: independent
Evidence tier: E3
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Security task class: comprehensive logical-whole closure audit — AI/provider-boundary (INFOSEC 4.6) + authN/Z (INFOSEC 4.4)
Owned/authorized target: Libre Tiles canonical repository, candidate 151e833dd0e78ced075101864cb5f45ee521bebc
Scope: the complete landed admin-provider-model-console implementation across Slices 1–8
Canonical repository mutation: none
Correction authority: none
Containment: temporary audit roots per the ledger contract; synthetic evidence only
Evidence classes: reproduced-dynamic | established-static | inferred | hypothesis-unverified
Exploitability cap: evidence class caps the conclusion
Reporting: security audit report contract
Primary route: R3 (comprehensive provider-boundary, SSRF, credential isolation, and runner safety)
Secondary route: R3 (authN/Z, CSRF, template safety, and catalog integrity invariants)
Logical-whole closure: closure-audit
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks across the landed whole:
1. Provider API keys / secrets at rest: verify that R2=A holds everywhere (keys live only in server environment, never stored in DB, never logged, never rendered in admin HTML or reports).
2. Outbound SSRF & Destination controls: verify that DiagnosticAllowedHost and DiagnosticTarget enforce strict HTTPS, hostname allowlist, DNS re-validation with private IP refusal, and bound `node:https` adapter without redirects.
3. Seam isolation: verify that player gameplay (`getLanguageRuntime`, `isValidRuntimePair`) cannot reach `DiagnosticTarget` or custom URLs, and that the single move route `/api/ai/move` strictly gates target seats behind `diagnostic_target_seat === true`.
4. Diagnostic runner & service account safety: verify that the runner mints only access-bound service tokens, passes them via whitelisted env to Node worker, refuses product matchmaking/games, and cannot execute live provider calls without explicit gates.
5. Catalog fallback order and activation safety: verify that `controls/apply/` enforces atomic write-locking, refuses zero selectable models and last tools-model deactivation, and that changeform saves cannot overwrite activation/ordering.
6. Template safety & XSS: verify that no `|safe` or `mark_safe()` vulnerability exists in any added admin template.
7. Provider calls during this audit: ZERO.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1773-1810      the Defensive-Security Task Anchor — the binding core of your audit
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
INFOSEC.md:163-171   section 4.6, AI/provider-boundary specialization
INFOSEC.md:144-153   section 4.4, authN/Z and state-changing action audit
INFOSEC.md:220-232   section 5, threat-model requirement
INFOSEC.md:234-248   section 6, finding and evidence contract
PROMPT_CONTRACTS.md:1772-1817  the Security Finding Record fields
PROMPT_CONTRACTS.md:1819-1831  the Threat-Model Fields
PROMPT_CONTRACTS.md:1883-1896  the Security Audit Report contract
PROMPT_CONTRACTS.md:14-41      the report contract and coordinate fields you echo
PROMPT_CONTRACTS.md:203       phase-qualified result (`not-applicable` for audit)
AP.md:2452-2454      the CLOSED report-justification enum (`final-acceptance` or `new-evidence`).
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — key components of the landed console

```text
/home/agile/Projects/libretiles/AGENTS.md
backend/game/models.py               DiagnosticSession, DiagnosticRun, DiagnosticPly, DiagnosticTarget, DiagnosticAllowedHost
backend/game/services.py             ensure_diagnostic_service_user, create_diagnostic_game, get_ai_context, abort_diagnostic_run
backend/game/admin.py                DiagnosticRunAdmin, DiagnosticTargetAdmin, DiagnosticAllowedHostAdmin
backend/game/diagnostic_targets.py   URL policy, DNS getaddrinfo validation, target freezing
frontend/src/lib/diagnostic-target-fetch.ts   bound node:https adapter, custom lookup, private IP refusal
frontend/src/lib/diagnostic-target-runtime.ts parseDiagnosticRuntimeSpec, getDiagnosticLanguageRuntime
frontend/src/app/api/ai/move/route.ts         diagnosticTargetSeat branch
backend/catalog/models.py            AIModel, AIPrompt, CapabilityProbe, CatalogAdminControl
backend/catalog/admin.py             AIModelAdmin, controls_view, probe_model_view, save_model
backend/catalog/admin_controls.py    CatalogControlsService, apply_reviewed_token
backend/catalog/provider_probes.py   probe execution, subprocess management
backend/catalog/selection.py         get_selectable_models, is_selectable_model
frontend/scripts/diagnostic-worker.mjs
frontend/scripts/probe-worker.mjs
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 151e833dd0e78ced075101864cb5f45ee521bebc
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start
```

Run required backend verification from `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_catalog_admin_controls.py tests/test_provider_probe_history.py tests/test_provider_probe_worker.py tests/test_catalog_admin_console_migration.py tests/test_diagnostic_targets.py tests/test_diagnostic_runner.py -k "not test_f_v and not test_f_w"
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
```
And frontend verification from `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/diagnostic-target-fetch.test.ts src/lib/diagnostic-target-runtime.test.ts src/lib/admin-provider-probe.test.ts src/lib/provider-capability.test.ts
```

⛔ Command execution rule (RF-16): Never pass or type `PYTHON_DOTENV_DISABLED=1` on shell commands.

## 2. Whole-Console Claims to evaluate (C1–C10)

Evaluate each claim with an explicit verdict: `verified-closed` OR `not accepted`.

- **C1: R2=A Credential Isolation**: No provider API keys, tokens, or plaintext secrets are stored in the database, logged to files, echoed in diagnostic reports, or rendered in admin HTML. The database stores ONLY the environment variable name (closed allowlist `credential_env_name`).
- **C2: Outbound SSRF & Network Protection**: `DiagnosticAllowedHost` and `DiagnosticTarget` enforce HTTPS, reject private/loopback/link-local/multicast IP ranges at save-time DNS and at request-time (`node:https` custom DNS lookup), follow zero redirects, and reject invalid hostname forms.
- **C3: Sibling Runtime Seam & Player Route Isolation**: Custom endpoints are available exclusively via `getDiagnosticLanguageRuntime`. Player routes (`getLanguageRuntime`, `isValidRuntimePair`) remain untouched and hardcoded. Target seats are strictly isolated behind `diagnostic_target_seat === true`.
- **C4: Diagnostic Service Account Security**: `ensure_diagnostic_service_user` creates an unusable-password managed user flagged with `is_service_account=True`. The service bearer is blocked from creating product games, joining matchmaking, or renaming its account.
- **C5: Diagnostic Runner Bounds & Resource Containment**: The background runner enforces wall-clock timeouts, turn timeouts, max provider request caps, heartbeat monitoring, and cancellation handling. Provider calls in fake mode remain ZERO.
- **C6: Probe History & Worker Isolation**: `CapabilityProbe` history is read-only in admin, capped at newest 100 per model, distinguishes fake vs live execution, and uses dedicated isolated single-shot Node worker.
- **C7: Fallback Order & Catalog Invariants**: Reviewed fallback order update (`controls/apply/`) executes in `transaction.atomic()` with coordination write-locking, refusing any update that produces zero selectable models under either flag state or removes the last tools-capable model.
- **C8: Changeform Save Isolation**: Ordinary AIModel changeform saves update only allowed descriptive metadata fields via `update_fields`, completely preventing overwrite or reversion of `is_active` or `sort_order`.
- **C9: Django Admin Template XSS Prevention**: All added admin templates (`change_list.html`, `change_form.html`, `controls.html`, `live_view.html`, `comparison.html`) use standard auto-escaping. No `|safe` or `mark_safe()` vulnerability exists.
- **C10: Operational Honesty & Metrics Separation**: Model metrics (`completion_source`, requests used, latency) are cleanly separated from engine metrics (score). Fake runs clearly record `executed_runtime_mode=fake` and simulated status.

## 3. Residual-Risk Disposition

Independently review and disposition the established accepted residuals:
1. **APMC-S7-IA-F05**: Key-to-host delegation (admin pairs allowlisted host + existing env name). Accepted fake-only residual; live credential/destination binding decision owed at a future live target grant.
2. **APMC-S5-IA-F01–F03**: Wildcard ALLOWED_HOSTS only when DEBUG=true; access token lifetime; local-actor test override.
3. **Slice 3b fill honesty**: `_model_position_samples` records generic_unchanged for unmeasured plies.
4. **Slice 6 compare-table UX**: `run_id_short` rendered as text rather than link.
5. **K1 calibration residual**: Requests-per-ply calibrated at 1.0 (rescue floor); subcaps remain provisional (`subcaps_provisional=true`), safely bounded by run default 200 and admin max 1000 (R4).

## 4. Threat-model fields to echo

Include the threat-model fields table per `PROMPT_CONTRACTS.md:1819-1831`:
- Assets
- Trust boundaries
- Attacker-controlled inputs
- Security properties
- Abuse cases
- Attacker profile
- Attack surface
- Threat condition
- Technical mechanism
- Blast radius
- Verification strategy
- Residual risk

## 5. Report format and stopping conditions

Submit exactly ONE standard AP terminal report beginning with:
```text
### Report for ORCHESTRATOR_CHAT
```
Echo coordinates:
```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 35, Worker exchange ordinal: 01
```
Phase-qualified result: `not-applicable`.
Status: `PASS`, `PARTIAL`, or `BLOCKED`.
Include compact core items 1–11 per `PROMPT_CONTRACTS.md:18-37`.
Include C1–C10 verdict table and the residual-risk disposition table.
Report justification: final-acceptance

⛔ Your authority ends at submitting the audit report. Do not modify any file.
