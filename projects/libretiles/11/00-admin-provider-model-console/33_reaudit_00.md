You are a WORKER instance assigned to the persistent AP WORKER role. This is a FRESH INDEPENDENT RE-AUDIT session (INFOSEC 4.11 / P-10). Perform exactly this bounded READ-ONLY re-audit task and stop. ⛔ You have NO implementation authority, NO correction authority, and NO mutation authority of any kind.

⛔ You are the re-auditor. Your first actions are the repository gate, then the test verification in §1, then independent source and dynamic review of V-F01, V-F02, V-F03, and V-REG. Produce the security audit report. ⛔ You audit; you do not correct.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 33
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Task identity: APMC-S8-REAUDIT — independently re-audit the corrected slice-8 candidate (commit 151e833dd0e78ced075101864cb5f45ee521bebc) against findings F01, F02, F03, and regression check V-REG. Verdict per finding: verified-closed | not accepted.
Phase: re-audit
Exact baseline: 151e833dd0e78ced075101864cb5f45ee521bebc
Independence required: yes
Evidence posture: independent
Evidence tier: E2
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Security task class: focused defensive re-audit — authN/Z and template safety (INFOSEC 4.11)
Owned/authorized target: Libre Tiles canonical repository, candidate 151e833dd0e78ced075101864cb5f45ee521bebc
Scope: the correction diff from 8853a29..151e833 (backend/catalog/admin.py, backend/catalog/admin_controls.py, backend/tests/test_catalog_admin_controls.py) plus adjacent catalog surfaces
Canonical repository mutation: none
Correction authority: none
Containment: temporary audit roots per the ledger contract; synthetic evidence only
Evidence classes: reproduced-dynamic | established-static | inferred | hypothesis-unverified
Exploitability cap: evidence class caps the conclusion
Reporting: security audit report contract
Primary route: R3 (re-audit of F02 flag binding and F03 changeform metadata restriction)
Secondary route: R3 (V-REG regression check of C4–C8)
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks:
1. V-F02: Token applied after server dynamic-catalog flag flip must fail closed with HTTP 409 / STALE_REVIEW_MESSAGE.
2. V-F03: Ordinary changeform saves (`AIModelAdmin.save_model`) must use `update_fields` restricted to descriptive metadata, making it impossible to overwrite concurrent reviewed swaps of `is_active` or `sort_order`.
3. V-F01: Confirm non-staff 302 login redirect is standard Django admin_view behavior and unauthorized access remains completely blocked.
4. V-REG: Invariants C4–C8 (probe history immutability, XSS escaping, fake-default node worker, seed/sync preservation, DiagnosticTarget isolation) must not have regressed. Provider calls remain ZERO.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1773-1810      the Defensive-Security Task Anchor — the binding core of your audit
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   your role and authority boundary
INFOSEC.md:144-153   section 4.4 — authN/Z and state-changing admin action audit
INFOSEC.md:154-162   section 4.11 — fresh independent re-audit
INFOSEC.md:220-232   section 5, threat-model requirement
INFOSEC.md:234-248   section 6, finding and evidence contract
PROMPT_CONTRACTS.md:1772-1817  the Security Finding Record fields
PROMPT_CONTRACTS.md:1819-1831  the Threat-Model Fields
PROMPT_CONTRACTS.md:1883-1896  the Security Audit Report contract
PROMPT_CONTRACTS.md:14-41      the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:203       phase-qualified result. This re-audit uses `not-applicable`.
                       ⛔ Do not claim `acceptance-PASS`.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — the candidate diff and surroundings

```text
/home/agile/Projects/libretiles/AGENTS.md
git diff 8853a29eb5e9f937b3db49236cac6ad876db6469..151e833dd0e78ced075101864cb5f45ee521bebc
backend/catalog/admin_controls.py   apply_reviewed_token, load_review_token, current_dynamic_catalog_enabled
backend/catalog/admin.py            AIModelAdmin.save_model
backend/tests/test_catalog_admin_controls.py
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
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_catalog_admin_controls.py tests/test_provider_probe_history.py tests/test_provider_probe_worker.py tests/test_catalog_admin_console_migration.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
```
And frontend verification from `frontend/`:
```bash
npm run typecheck
npm run lint
```

⛔ Command execution rule (RF-16): Never pass or type `PYTHON_DOTENV_DISABLED=1` on shell commands.

## 2. Findings and regression claims to independently verify

Evaluate each with an explicit verdict: `verified-closed` OR `not accepted`.

- **V-F01 (info claim reconciliation)**:
  Confirm that anonymous or non-staff POSTs to `/admin/catalog/aimodel/controls/review/`, `/admin/catalog/aimodel/controls/apply/`, and `/admin/catalog/aimodel/<id>/probe/` are blocked from executing privileged actions by redirecting to `/admin/login/?next=...` (HTTP 302), matching standard Django `admin_view` behavior, and that view-only / unprivileged staff receive HTTP 403.
- **V-F02 (enforce signed flag binding)**:
  Verify dynamically and statically that `apply_reviewed_token` rejects tokens if `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` changed between review and apply (both false→true and true→false), raising `CatalogControlError(STALE_REVIEW_MESSAGE)` and returning HTTP 409 without applying changes.
- **V-F03 (prevent changeform saves from overwriting activation/ordering)**:
  Verify that `AIModelAdmin.save_model` on change updates ONLY the allowed descriptive metadata fields using `obj.save(update_fields=...)`. Verify dynamically that an ordinary changeform save cannot overwrite or revert `is_active` or `sort_order`, and cannot reduce active tools models or selectable models. Verify that creation path still safely defaults `is_active=False`.
- **V-REG (C4–C8 regression check)**:
  Verify that probe history child table (`CapabilityProbe`) remains read-only, retention pruning (newest 100) works, admin templates remain XSS-safe (no `|safe` / `mark_safe`), Node probe worker remains isolated and fake-default, seed and sync continue to preserve operator settings, and DiagnosticTarget remains strictly isolated. Provider calls remain ZERO.

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
Worker session ordinal: 33, Worker exchange ordinal: 01
```
Phase-qualified result: `not-applicable`.
Status: `PASS`, `PARTIAL`, or `BLOCKED`.
Include compact core items 1–11 per `PROMPT_CONTRACTS.md:18-37`.
Include the V-F01, V-F02, V-F03, and V-REG verdict table.
Report justification: new-evidence

⛔ Your authority ends at submitting the re-audit report. Do not modify any file.
