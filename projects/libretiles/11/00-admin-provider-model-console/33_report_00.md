### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 33
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Task identity: APMC-S8-REAUDIT
Phase: re-audit
Exact baseline: 151e833dd0e78ced075101864cb5f45ee521bebc
Independence required: yes
Evidence posture: independent
Evidence tier: E2
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
```

1. **Identity:** `admin-provider-model-console`, session `33`, exchange `01`.
2. **Status:** `PASS`
3. **Phase-qualified result:** `not-applicable`
4. **Start and end commit:** `151e833dd0e78ced075101864cb5f45ee521bebc` → `151e833dd0e78ced075101864cb5f45ee521bebc` (read-only; no mutation)
5. **Changed files:** none. Inspected correction `8853a29eb5e9f937b3db49236cac6ad876db6469..151e833dd0e78ced075101864cb5f45ee521bebc` on `backend/catalog/admin.py`, `backend/catalog/admin_controls.py`, `backend/tests/test_catalog_admin_controls.py`, plus adjacent catalog admin/probe/seed/sync surfaces.
6. **Tests and validation:**
   - Repository gate: `HEAD` `151e833dd0e78ced075101864cb5f45ee521bebc`; `HEAD:.ap` and `.ap HEAD` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `## main...origin/main`; porcelain empty before and after.
   - Backend (from `backend/`, `env -u APPIMAGE -u ARGV0 -u APPDIR`): pytest **23 passed in 4.76s** (`test_catalog_admin_controls.py`, `test_provider_probe_history.py`, `test_provider_probe_worker.py`, `test_catalog_admin_console_migration.py`); `ruff check .` all passed; `mypy config game gamecore accounts catalog` Success, 99 source files.
   - Frontend: `npm run typecheck` and `npm run lint` passed.
   - Independent contained dynamic checks (synthetic Django TestCase under declared temp root): 3 passed (V-F01 login redirect on all three POSTs for anonymous and non-staff; view-only 403 on review/apply/probe; create `save_model(change=False)` forces `is_active=False`).
7. **Commit and push:** none authorized; none performed.
8. **Deviations / risks / missing evidence:** Prompt citation `INFOSEC.md:154-162` labels section 4.11; pinned `INFOSEC.md` at that range is §4.5, and §4.11 is at `205-210`. Followed the named §4.11 rule, not the mislabeled range. Independent checks lived outside `backend/tests/` and required `DJANGO_SETTINGS_MODULE=config.settings` for collection. Full `test_diagnostic_targets.py` / frontend probe-worker unit tests were outside the authorized command list; V-REG isolation for DiagnosticTarget on this candidate is static plus `test_f19`.
9. **Smallest next step:** Orchestrator records the four `verified-closed` verdicts. Do not implement. Logical whole stays `not-closed`.
10. **Report justification:** `new-evidence`
11. **Authority expiry:** This Worker’s authority ended at submission of this re-audit report. No further action is authorized.

Context pressure: moderate — four named claims plus C4–C8 regression on one candidate, with room left.

Provider calls this session: **ZERO**.

Resolved Execution Issues / Near-Misses: independent pytest initially collected against `/tmp` without Django settings; rerun with `--rootdir` plus `DJANGO_SETTINGS_MODULE=config.settings` (not `PYTHON_DOTENV_DISABLED`). Residual risk: none.

Pre-Existing Failure Classification: none

---

## Security audit report

```text
Security task class: focused defensive re-audit — authN/Z and template safety (INFOSEC 4.11)
Owned/authorized target: Libre Tiles canonical repository, candidate 151e833dd0e78ced075101864cb5f45ee521bebc
Commit under audit: 151e833dd0e78ced075101864cb5f45ee521bebc
Scope: correction diff 8853a29..151e833 (admin.py, admin_controls.py, test_catalog_admin_controls.py) plus adjacent catalog admin, probe history, seed/sync, and DiagnosticTarget isolation on the probe path
Exclusions: live provider calls; host/infrastructure; product UI outside Django admin; DiagnosticTarget admin suite re-execution; frontend probe-worker unit tests (not in the authorized command list)
```

### Verdict table

| Claim | Verdict | Evidence class |
|---|---|---|
| V-F01 | **verified-closed** | reproduced-dynamic + established-static |
| V-F02 | **verified-closed** | reproduced-dynamic + established-static |
| V-F03 | **verified-closed** | reproduced-dynamic + established-static |
| V-REG (C4–C8) | **verified-closed** | reproduced-dynamic + established-static |

---

### Threat model

```text
Assets: catalog activation (`is_active`), fallback order (`sort_order`), selectable free-rival set, signed review tokens, probe history integrity, admin session, DiagnosticTarget isolation, provider credentials / outbound provider calls
Trust boundaries: unauthenticated HTTP → Django admin; non-staff user → staff admin; view-only staff → change/probe privileged actions; ordinary AIModel changeform → reviewed activation/order writes; review token (signed, 600s) → apply; process setting DYNAMIC_FREE_MODEL_CATALOG_ENABLED → apply; Node probe worker → Django process; catalog rows → DiagnosticTarget seats
Attacker-controlled inputs: anonymous/non-staff POST bodies to /admin/catalog/aimodel/controls/review/, /controls/apply/, /<id>/probe/; CSRF-bearing staff POSTs; review_token; changeform fields including is_active/sort_order/provider/model_id; probe mode and extra keys (diagnostic_target_id, base_url); hostile display_name/summary strings
Security properties: privileged catalog mutation requires staff + change permission; apply fails closed on actor/revision/fingerprint/flag mismatch; ordinary changeform cannot write activation/order; probe history immutable; XSS-escaped admin templates; fake-default probe with zero provider calls unless live sentinel; seed/sync must not revive operator kill-switch/order; DiagnosticTarget stays off the catalog probe path
Abuse cases: replay a reviewed token after a dynamic-catalog flag flip; POST a stale changeform to undo a concurrent reviewed swap; unauthenticated POST hoping for 200 apply; view-only staff invoking review/apply/probe; changeform mass-assignment of identity/activation; XSS via model/probe strings; probe POST smuggling a diagnostic target URL
Attacker profile: unauthenticated internet client; authenticated non-staff user; view-only staff; change-capable staff acting on a stale form or token; local concurrent admin sessions
Attack surface: Django admin custom URLs wrapped by admin_view; AIModelAdmin.save_model; apply_reviewed_token; CapabilityProbe admin; catalog templates; seed_models / sync_openrouter_models
Threat condition: deployed Django admin reachable by the attacker class; DYNAMIC_FREE_MODEL_CATALOG_ENABLED may change between review and apply (restart / override); concurrent reviewed apply vs changeform save
Technical mechanism: Django 5.2.17 AdminSite.admin_view (is_active ∧ is_staff else redirect_to_login); PermissionDenied → 403; signed payload field dynamic_enabled compared to current_dynamic_catalog_enabled(); Model.save(update_fields=CHANGEFORM_METADATA_FIELDS)
Blast radius: empty or inverted selectable catalog; last tools-capable model dropped; operator kill-switch reverted; XSS in staff browser; accidental live provider call (not observed)
Verification strategy: repository gate; authorized pytest/ruff/mypy/typecheck/lint; independent TestCase for login Location and create-path is_active=False; static read of admin_view, save_model, apply_reviewed_token, seed/sync, templates, probe worker
Residual risk: AIModel.is_active model default remains True if save_model is bypassed (ORM/seed create); Django csrf_protect may 403 an anonymous POST before the 302 login redirect — still fail-closed; flag check is process settings, not a DB lock
```

---

### Source records

```text
Title: CWE List
Owner: MITRE
Version: 4.17
Status: taxonomy
Retrieval date: 2026-09-07
AP concept supported: finding CWE mapping
Refresh: recheck before time-sensitive audits

Title: Django AdminSite.admin_view / has_permission (local installed source)
Owner: Django Software Foundation
Version: 5.2.17 (backend/.venv)
Status: tooling
Retrieval date: 2026-09-07
AP concept supported: V-F01 standard login-redirect behavior
Refresh: recheck if Django version changes

Title: OWASP Application Security Verification Standard
Owner: OWASP
Version: 5.0
Status: final
Retrieval date: not re-fetched this session
AP concept supported: ASVS mapping
Refresh: exact V-requirement IDs not asserted (ASVS mapping: none)
```

---

### Findings

```text
Finding ID: APMC-S8-F01
Title: Anonymous/non-staff privileged POSTs redirect to admin login (info reconciliation)
Status: verified-closed
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 151e833dd0e78ced075101864cb5f45ee521bebc
Affected component and exact location: backend/catalog/admin.py:90-116 (admin_view wrappers); Django AdminSite.admin_view 5.2.17 sites.py:209-254
Security property: unauthenticated and non-staff actors cannot execute review/apply/probe
Asset at risk: catalog controls and probe admission
Trust boundary: unauthenticated/non-staff HTTP → Django admin
Attacker-controlled input or local actor: POST to controls/review/, controls/apply/, <id>/probe/
Reachability: established — those three URLs are registered and wrapped with admin_site.admin_view
Preconditions: Django admin enabled; CsrfViewMiddleware on
Required privileges: none (anonymous) or ordinary user (is_staff=False)
Observed or potential impact: HTTP 302 to /admin/login/?next=<path>; privileged view body does not run. View-only staff: HTTP 403. CSRF-enforced anonymous POST: 403 or 302, still no apply.
C/I/A effect: none remaining on this claim
CWE mapping: none
ASVS mapping: none
Source-standard references: Django 5.2.17 AdminSite.has_permission / admin_view / redirect_to_login, local venv, 2026-09-07
Dynamic reproduction evidence: test_f13_methods_csrf_and_permissions (anon apply 302; view-only review/probe 403; CSRF staff review 403; GET 405). Independent IndependentReauditChecks: anonymous and is_staff=False POST on all three URLs 302 with Location starting /admin/login/ and containing next= plus the path; view-only POST apply also 403; CSRF-enforced anonymous POST blocked (302 or 403).
Static evidence: has_permission = request.user.is_active and request.user.is_staff; else redirect_to_login(request.get_full_path(), reverse("admin:login")); csrf_protect wraps inner. controls_review_view / controls_apply_view / probe_view raise PermissionDenied without change/probe permission.
Synthetic containment: /tmp/apmc-s8-reaudit-33 (mode 0700, synthetic TestCase only, removed)
False-positive analysis: a 302 is Django’s documented staff gate, not an authorization bypass. Disproof would be a 200/302-to-success apply without staff+change permission.
Exploitability conclusion: not applicable
Smallest safe correction direction: none
Regression-test requirement: retain test_f13 plus login Location coverage on review/apply/probe
Residual risk: csrf_protect may return 403 before login redirect; privileged action remains unexecuted
Acceptance-blocking decision: non-blocking — info claim reconciled, access blocked
Redaction requirements: none beyond ordinary admin URLs
```

```text
Finding ID: APMC-S8-F02
Title: Signed review token must bind DYNAMIC_FREE_MODEL_CATALOG_ENABLED
Status: verified-closed
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 151e833dd0e78ced075101864cb5f45ee521bebc
Affected component and exact location: backend/catalog/admin_controls.py:222-236 apply_reviewed_token / current_dynamic_catalog_enabled()
Security property: apply fails closed if the dynamic-catalog flag changed after review
Asset at risk: selectable catalog under flag-off vs flag-on invariants
Trust boundary: signed review token → apply
Attacker-controlled input or local actor: review_token issued under one flag value, applied after server flag flip
Reachability: established — apply_reviewed_token is the apply POST path
Preconditions: valid signature, matching actor_id, token age ≤ 600s; settings flag differs from payload["dynamic_enabled"]
Required privileges: staff with catalog change permission
Observed or potential impact: CatalogControlError(STALE_REVIEW_MESSAGE, status=409); HTTP 409; is_active/sort_order unchanged
C/I/A effect: integrity preserved (no apply)
CWE mapping: CWE-345 (CWE List 4.17)
ASVS mapping: none
Source-standard references: CWE List 4.17, MITRE, taxonomy, 2026-09-07
Dynamic reproduction evidence: test_f02_apply_rejects_token_when_dynamic_flag_changes — false→true and true→false; exception message STALE_REVIEW_MESSAGE and status 409; client POST 409 with message in body; row is_active/sort_order unchanged
Static evidence: after actor_id check, `if payload.get("dynamic_enabled") != current_dynamic_catalog_enabled(): raise CatalogControlError(STALE_REVIEW_MESSAGE)` before parsing changes or apply_reviewed_changes. Missing payload key fails closed (None != bool).
Synthetic containment: Django TestCase database only
False-positive analysis: a silent apply after override_settings flip would disprove closure
Exploitability conclusion: not demonstrated (correction holds)
Smallest safe correction direction: none
Regression-test requirement: keep test_f02_apply_rejects_token_when_dynamic_flag_changes
Residual risk: flag is process settings, read outside the catalog write lock; a mid-request in-process settings mutation after the check is not a realistic Django threat
Acceptance-blocking decision: non-blocking — verified-closed
Redaction requirements: none
```

```text
Finding ID: APMC-S8-F03
Title: Ordinary changeform save must not write is_active or sort_order
Status: verified-closed
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 151e833dd0e78ced075101864cb5f45ee521bebc
Affected component and exact location: backend/catalog/admin.py:52-59 CHANGEFORM_METADATA_FIELDS; 131-142 AIModelAdmin.save_model
Security property: reviewed activation/order survive ordinary and concurrent changeform saves
Asset at risk: is_active, sort_order, selectable set, last tools-capable language model
Trust boundary: changeform POST / in-memory ModelAdmin.save_model vs reviewed apply
Attacker-controlled input or local actor: changeform POST with is_active/sort_order; poisoned in-memory instance; concurrent DB update of sort_order
Reachability: established — admin change URL calls save_model(change=True)
Preconditions: staff with change permission; existing AIModel row
Required privileges: admin (staff + change_aimodel)
Observed or potential impact: metadata (display_name, description, …) updates; is_active/sort_order unchanged; tools/selectable counts not reduced; UPDATE SQL omits is_active and sort_order. Create path forces is_active=False despite in-memory True.
C/I/A effect: integrity of activation/order preserved on this path
CWE mapping: CWE-915; CWE-362 (CWE List 4.17)
ASVS mapping: none
Source-standard references: CWE List 4.17, MITRE, taxonomy, 2026-09-07
Dynamic reproduction evidence: test_f03_changeform_save_cannot_overwrite_reviewed_activation (HTTP POST plus RequestFactory save_model with patched get); test_f12_ordinary_admin_saves_cannot_bypass_review; independent save_model(change=False) with is_active=True persisted False; CHANGEFORM_METADATA_FIELDS has neither is_active nor sort_order
Static evidence: change branch is only `obj.save(update_fields=list(CHANGEFORM_METADATA_FIELDS))` with fields display_name, description, quality_tier, context_window, max_tokens, updated_at. Create branch sets obj.is_active=False then super().save_model. IDENTITY_READONLY still includes is_active/sort_order. actions = None.
Synthetic containment: Django TestCase database; /tmp/apmc-s8-reaudit-33 removed
False-positive analysis: an UPDATE including is_active/sort_order, or selectable/tools count drop after the posted save, would reopen the finding
Exploitability conclusion: not demonstrated (correction holds)
Smallest safe correction direction: none
Regression-test requirement: keep test_f03_changeform_save_cannot_overwrite_reviewed_activation
Residual risk: model field default is_active=True if AIModel is created outside save_model (seed/ORM). Intended for seed create; admin add is forced inactive.
Acceptance-blocking decision: non-blocking — verified-closed
Redaction requirements: none
```

```text
Finding ID: APMC-S8-REG
Title: C4–C8 regression check after F02/F03 correction
Status: verified-closed
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 151e833dd0e78ced075101864cb5f45ee521bebc
Affected component and exact location: CapabilityProbeAdmin; catalog templates; provider_probes.run_aimodel_probe; seed_models; openrouter_sync; CapabilityProbe fields
Security property: probe history immutability; XSS escaping; fake-default isolated worker; seed/sync preserve operator settings; DiagnosticTarget isolation; ZERO provider calls
Asset at risk: probe history, staff browser, provider credentials, catalog operator settings, diagnostic seats
Trust boundary: catalog admin vs probe worker vs DiagnosticTarget
Attacker-controlled input or local actor: probe POST extras; hostile summary/display_name; seed/sync reruns
Reachability: established for catalog admin probe/history; DiagnosticTarget models not in the correction diff
Preconditions: staff probe/view permissions as in tests
Required privileges: admin
Observed or potential impact: none of C4–C8 regressed on this candidate
C/I/A effect: none observed
CWE mapping: none
ASVS mapping: none
Source-standard references: CWE List 4.17 (taxonomy only; no new CWE opened)
Dynamic reproduction evidence:
  C4 immutability/retention: test_f18_retention_keeps_newest_100_and_history_is_read_only (count 100; add/delete 403); CapabilityProbeAdmin has_add/change/delete False
  C5 XSS: test_f14_hostile_text_is_escaped_in_changeform_and_history; catalog templates have no |safe / autoescape off; admin.py has no mark_safe; change_form.html autoescapes probe.summary
  C6 fake-default worker: probe_view defaults mode to fake; run_aimodel_probe treats non-live as fake and never calls _spawn_worker; test_f01/f02 history (spawn.assert_not_called, outbound_count 0); live tests mock spawn; test_f06 env whitelist (no DJANGO_SECRET_KEY/NODE_OPTIONS)
  C7 seed/sync: test_f17_seed_and_sync_preserve_operator_priority_and_activation; seed updates existing rows without is_active/sort_order; sync update_fields omit them
  C8 DiagnosticTarget: test_f19_probe_path_has_no_diagnostic_target_fk; extra POST keys ignored; fake still binds ai_model only
  Provider calls: authorized suite 4.76s, live spawn mocked or not called
Static evidence: correction diff does not touch diagnostic models, templates, or probe worker; _spawn_worker is live-only
Synthetic containment: Django TestCase only
False-positive analysis: a live _spawn_worker call in fake tests, |safe in catalog templates, or seed rewriting is_active would reopen V-REG
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none
Regression-test requirement: keep the four authorized test modules
Residual risk: DiagnosticTarget admin suite and frontend probe-worker.mjs unit tests were not re-executed this session
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

---

### Containment ledger

```text
Temporary root: /tmp/apmc-s8-reaudit-33
Owner: Worker session 33 exchange 01
Mode: 0700
Contents class: synthetic pytest module and pytest cache only
Cleanup owner: this Worker
Cleanup outcome: removed (file, __pycache__, .pytest_cache, then directory; path absent)
```

No other temporary roots, accounts, or network targets were created. Pytest used the isolated Django test database.

---

### Limitations

- Live provider and live Node worker were not invoked (in scope: ZERO).
- `test_diagnostic_targets.py` / diagnostic admin tests were not in the authorized pytest list.
- Frontend `admin-provider-probe*.test.ts` / `probe-worker.mjs` unit tests were not run; fake-default isolation was taken from backend tests plus static `admin.py` / `provider_probes.py`.
- Exact OWASP ASVS 5.0 requirement IDs were not re-fetched; mappings recorded as `none`.

---

### Residual-risk summary

No open security findings on F01–F03 or C4–C8 for candidate `151e833dd0e78ced075101864cb5f45ee521bebc`. Remaining residuals are proportionate: CSRF may 403 before login redirect; `AIModel.is_active` defaults True outside admin `save_model`; dynamic-flag compare is process settings. None of these reopen the named claims.

This Worker does not claim `acceptance-PASS` and does not close the logical whole.
