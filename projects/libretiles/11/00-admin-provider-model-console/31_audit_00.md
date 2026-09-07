You are a WORKER instance assigned to the persistent AP WORKER role. This is a FRESH INDEPENDENT AUDIT session. Perform exactly this bounded READ-ONLY audit task and stop. ⛔ You have NO implementation authority, NO correction authority, and NO mutation authority of any kind.

⛔ You are the auditor. Your first actions are the repository gate, then the test verification in §1, then independent source and dynamic review of C1–C8. Produce the security audit report. ⛔ You audit; you do not correct.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 31
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Task identity: APMC-S8-AUDIT — independently audit the landed slice-8 candidate (commit 8853a29eb5e9f937b3db49236cac6ad876db6469) against the accepted threat model: fallback order and activation controls in Django admin, CSRF/permission enforcement, token signing and replay prevention, zero-selectable and last-tools refusal invariants, probe history child table integrity and pruning, template escaping without |safe/mark_safe, and Node probe worker isolation (fake mode default, zero provider calls). Verdict per claim: verified-closed | not accepted.
Phase: audit
Exact baseline: 8853a29eb5e9f937b3db49236cac6ad876db6469
Independence required: yes
Evidence posture: independent
Evidence tier: E2
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Security task class: focused defensive audit — authN/Z and template safety (INFOSEC 4.4) + provider capability probe boundary
Owned/authorized target: Libre Tiles canonical repository, candidate 8853a29eb5e9f937b3db49236cac6ad876db6469
Scope: the slice-8 candidate diff (24 allowlisted paths from 4c524ec..8853a29) plus adjacent catalog and admin surfaces
Canonical repository mutation: none
Correction authority: none
Containment: temporary audit roots per the ledger contract; synthetic evidence only
Evidence classes: reproduced-dynamic | established-static | inferred | hypothesis-unverified
Exploitability cap: evidence class caps the conclusion
Reporting: security audit report contract
Primary route: R3 (authN/Z on the sort_order / probe POSTs and CSRF)
Secondary route: R3 (template XSS safety and history integrity)
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks:
1. CSRF bypass or missing staff/model permission checks on `controls/review/`, `controls/apply/`, or `aimodel/<id>/probe/`.
2. Signed token forgery, replay, or parameter tampering bypassing the review step to alter ordering or de-activate models directly.
3. Concurrency / write skew bypassing the refusal invariants and deactivating all models or all tools-capable models.
4. Stored XSS in Django Admin templates via unescaped model IDs, provider names, probe summaries, or error messages.
5. Probe worker executing live provider calls or leaking process environment / Django secrets. Provider calls this session must be ZERO.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1773-1810      the Defensive-Security Task Anchor — the binding core of your audit
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   your role and authority boundary
INFOSEC.md:144-153   section 4.4 — authN/Z and state-changing admin action audit
INFOSEC.md:220-232   section 5, threat-model requirement
INFOSEC.md:234-248   section 6, finding and evidence contract
PROMPT_CONTRACTS.md:1772-1817  the Security Finding Record fields — every finding uses them
PROMPT_CONTRACTS.md:1819-1831  the Threat-Model Fields
PROMPT_CONTRACTS.md:1883-1896  the Security Audit Report contract
PROMPT_CONTRACTS.md:14-41      the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:203       phase-qualified result. This audit uses `not-applicable`.
                       ⛔ Do not claim `acceptance-PASS`.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — the candidate diff and its surroundings

```text
/home/agile/Projects/libretiles/AGENTS.md
git diff 4c524ec3020bbd2f27f2ce32ac160d2c40469c0e..8853a29eb5e9f937b3db49236cac6ad876db6469
backend/catalog/models.py         CapabilityProbe, CatalogAdminControl
backend/catalog/admin.py          AIModelAdmin, controls_view, probe_model_view
backend/catalog/admin_controls.py CatalogControlsService, review/apply logic, tokens
backend/catalog/provider_probes.py probe execution service, subprocess management
backend/catalog/selection.py      get_selectable_models, is_selectable_model
frontend/scripts/probe-worker.mjs probe worker script
frontend/src/lib/admin-provider-probe.ts probe worker client
backend/catalog/templates/admin/catalog/aimodel/controls.html
backend/catalog/templates/admin/catalog/aimodel/change_form.html
backend/catalog/templates/admin/catalog/aimodel/change_list.html
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 8853a29eb5e9f937b3db49236cac6ad876db6469
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start
```

Run required backend verification from `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_catalog_admin_controls.py tests/test_provider_probe_history.py tests/test_provider_probe_worker.py tests/test_catalog_admin_console_migration.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
```
And frontend verification from `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-provider-probe.test.ts src/lib/provider-capability.test.ts
```

⛔ Command execution rule (RF-16): Never pass or type `PYTHON_DOTENV_DISABLED=1` on shell commands.

## 2. Claims to independently evaluate (C1–C8)

Evaluate each claim with an explicit verdict: `verified-closed` OR `not accepted`. If `not accepted`, provide a full Security Finding Record (ID, severity, title, threat condition, technical mechanism, blast radius, verification evidence, remediation recommendation).

- **C1: AuthN/Z and CSRF enforcement on action endpoints**
  `POST /admin/catalog/aimodel/controls/review/`, `POST /admin/catalog/aimodel/controls/apply/`, and `POST /admin/catalog/aimodel/<id>/probe/` are wrapped in `admin_view`, enforce CSRF checks, require staff access and explicit model permissions (`catalog.change_aimodel` and `catalog.probe_aimodel`). GET requests to these action endpoints are refused with HTTP 405. Anonymous access redirects to login (302). Non-staff and view-only users are refused (403).
- **C2: Signed review token integrity and anti-replay**
  The confirmation token generated by `controls/review/` is cryptographically signed (via Django's `TimestampSigner`), bound to the actor's user ID, catalog revision, flag state, and the exact diff. Tokens expired (>10 minutes), tampered, replayed against a modified catalog, or submitted by a different user are rejected fail-closed with HTTP 409 / error message. No editable values passed alongside the token are honored.
- **C3: Safety invariants and bricking refusal**
  The apply endpoint executes in `transaction.atomic()` with serialization write-lock on `CatalogAdminControl`. Any change that leaves zero selectable models under either `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` or `true` is rejected fail-closed with HTTP 409. Any change that deactivates the last active model with the `"tools"` tag is rejected fail-closed. On refusal, zero database mutations survive.
- **C4: Probe history integrity and read-only administration**
  `CapabilityProbe` (`catalog_capability_probe`) records are read-only in Django admin (add/change/delete disabled). Auto-retention prunes records beyond the newest 100 per `AIModel` atomically on write. Display prominently separates simulated `fake` PASS ("Simulated PASS — capability unverified") from genuine live observations.
- **C5: Template safety and XSS prevention**
  All added Django admin templates (`controls.html`, `change_form.html`, `change_list.html`) use standard auto-escaping. Untrusted strings (model IDs, provider names, summaries, reason codes, status labels) are never rendered with `|safe`, `mark_safe()`, or raw HTML concatenation.
- **C6: Node probe worker isolation and fake default**
  The probe worker `frontend/scripts/probe-worker.mjs` runs single-shot with bounded timeouts (20s capability, 22s watchdog, 25s subprocess). Default execution is `fake` mode (0s, 0 egress, simulated PASS, no subprocess). `PROVIDER_PROBE_LIVE === "1"` is strictly required for live probes. The worker environment forwards only the specific provider's credential env name, never Django secrets, JWTs, or full process environment. Provider calls during test/audit remain ZERO.
- **C7: Seed and sync preservation of operator choices**
  `seed_models` and `sync_openrouter_models` preserve existing operator-set `sort_order` and `is_active` values and advance `CatalogAdminControl.revision` without overwriting concurrent admin decisions.
- **C8: Boundary isolation (DiagnosticTarget untouched)**
  `CapabilityProbe` has no FK to `DiagnosticTarget`. No catalog probe or fallback ordering endpoint affects `DiagnosticTarget` or `DiagnosticAllowedHost`. No secret materialization (R2=A).

## 3. Threat-model fields to echo

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

## 4. Report format and stopping conditions

Submit exactly ONE standard AP terminal report beginning with:
```text
### Report for ORCHESTRATOR_CHAT
```
Echo coordinates:
```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 31, Worker exchange ordinal: 01
```
Phase-qualified result: `not-applicable`.
Status: `PASS`, `PARTIAL`, or `BLOCKED`.
Include compact core items 1–11 per `PROMPT_CONTRACTS.md:18-37`.
Include the C1–C8 verdict table and any finding records.
Report justification: new-evidence

⛔ Your authority ends at submitting the audit report. Do not modify any file. Do not start corrections.
