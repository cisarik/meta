You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded correction task and stop. This prompt is the ONLY source of your task authority.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 32
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: APMC-S8-CORR — correct F02 (enforce signed dynamic_enabled flag binding during token apply) and F03 (prevent ordinary changeform saves from overwriting is_active or sort_order, using update_fields for descriptive metadata only). Provider calls: ZERO.
Phase: correction
Implementation authority: explicit
Exact baseline: 8853a29eb5e9f937b3db49236cac6ad876db6469
Changed-path allowlist: exactly the paths in section 4
Implementation boundaries: positive and negative authority in sections 3-5
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: bounded correction of audit findings F02 and F03 in catalog admin and controls; provider calls ZERO.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks:
1. Breaking existing ordinary changeform editing of AIModel metadata (display_name, description, quality_tier, etc.).
2. F02: `apply_reviewed_token` must strictly verify `payload.get("dynamic_enabled") == current_dynamic_catalog_enabled()` and raise `CatalogControlError(STALE_REVIEW_MESSAGE)` on mismatch.
3. F03: `AIModelAdmin.save_model` on change must never write `is_active` or `sort_order` to the database. Restrict `obj.save(update_fields=...)` to editable descriptive metadata fields so concurrent or stale changeform saves cannot overwrite reviewed activation or ordering.
4. RF-16: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
PROMPT_CONTRACTS.md:203     the phase-result enum. Expected Worker result spelling:
                            `implementation-PASS`.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — by symbol

```text
/home/agile/Projects/libretiles/AGENTS.md
backend/catalog/admin_controls.py   apply_reviewed_token, load_review_token, current_dynamic_catalog_enabled
backend/catalog/admin.py            AIModelAdmin.save_model
backend/tests/test_catalog_admin_controls.py
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

## 2. Findings to correct

### Finding F02 (Low): Signed review token survives dynamic-catalog flag change
- **Problem**: `apply_reviewed_token` loads the token payload (which includes `"dynamic_enabled"`), but does not verify whether `current_dynamic_catalog_enabled()` matches the signed value.
- **Fix**: In `backend/catalog/admin_controls.py`, `apply_reviewed_token`:
  ```python
  if payload.get("dynamic_enabled") != current_dynamic_catalog_enabled():
      raise CatalogControlError(STALE_REVIEW_MESSAGE)
  ```
- **Regression test**: Test that applying a token when the flag has changed (false→true or true→false) raises `CatalogControlError(STALE_REVIEW_MESSAGE)` and returns HTTP 409 on the apply endpoint without persisting changes.

### Finding F03 (Medium): Ordinary admin save can overwrite reviewed activation/ordering
- **Problem**: In `backend/catalog/admin.py`, `AIModelAdmin.save_model` on change does a full `obj.save()` after copying values from `AIModel.objects.get(pk=obj.pk)`. If `save_model` runs concurrently with or after a reviewed swap, it writes `is_active` and `sort_order` back to the database, potentially restoring stale inactive values and violating the non-empty / tools invariants.
- **Fix**:
  1. On change, `AIModelAdmin.save_model` must NOT write `is_active` or `sort_order`.
  2. Use `update_fields` on `obj.save(update_fields=...)` containing ONLY the allowed descriptive metadata fields:
     `["display_name", "description", "quality_tier", "context_window", "max_tokens", "updated_at"]`.
  3. This ensures SQL executes an `UPDATE` only for descriptive metadata, completely preventing ordinary changeform saves from touching or reverting `is_active`, `sort_order`, `provider`, or `model_id`.
  4. On creation (`not change`), new rows continue to be created with `is_active=False`.
- **Regression test**: Test that saving an AIModel via changeform updates descriptive fields (e.g. `display_name`, `description`) while strictly preserving any concurrent change to `is_active` or `sort_order`, and cannot reduce active tools models or selectable models.

## 3. Required behaviour

1. Add reproduction/regression tests in `backend/tests/test_catalog_admin_controls.py` proving both defects fail before the fix.
2. Apply the fixes in `backend/catalog/admin_controls.py` and `backend/catalog/admin.py`.
3. Verify that all catalog tests, admin tests, ruff, and mypy pass.

## 4. File allowlist

You may edit ONLY these paths:

```text
backend/catalog/admin.py
backend/catalog/admin_controls.py
backend/tests/test_catalog_admin_controls.py
```

## 5. Invariants

1. Provider calls: ZERO. No outbound HTTP calls.
2. Invariants preserved: zero selectable models refused; last tools model refusal holds.
3. No secret materialization.
4. RF-16: Never pass `PYTHON_DOTENV_DISABLED=1` on shell commands.

## 6. Validation sequence

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_catalog_admin_controls.py tests/test_provider_probe_history.py tests/test_provider_probe_worker.py tests/test_catalog_admin_console_migration.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
```
From `frontend/`:
```bash
npm run typecheck
npm run lint
```

## 7. Git commit and push

When all tests pass:
1. Stage ONLY the allowlisted files:
   ```bash
   git add backend/catalog/admin.py backend/catalog/admin_controls.py backend/tests/test_catalog_admin_controls.py
   ```
2. Commit with message:
   ```bash
   git commit -m "fix(catalog): enforce signed flag binding and restrict changeform saves to metadata"
   ```
3. Pre-push check:
   ```bash
   test "$(git ls-remote origin refs/heads/main | cut -f1)" = "8853a29eb5e9f937b3db49236cac6ad876db6469"
   ```
4. Push:
   ```bash
   git push origin main
   ```
5. Readback verification:
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
Worker session ordinal: 32, Worker exchange ordinal: 01
```
Phase-qualified result: `implementation-PASS`.
Status: `PASS`, `PARTIAL`, or `BLOCKED`.
Include compact core items 1–11 per `PROMPT_CONTRACTS.md:18-37`.
Report justification: new-mutation

⛔ Your authority ends at pushing the commit and submitting the report. Do not start re-audit.
