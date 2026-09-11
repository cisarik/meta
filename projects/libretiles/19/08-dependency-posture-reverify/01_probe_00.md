You are a WORKER instance. Perform exactly this bounded diagnostic task and stop. This is a RE-VERIFY report, not a fix.

```text
Logical whole identity: dependency-posture-reverify
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Task identity: DEP-PROBE-01 — re-verify the 2026-09-01 dependency posture against current advisories and lockfiles. No bumping, no installs, read-only on lockfiles.
Phase: Diagnostic Closeout
Exact baseline: 4d33ad618dc131662193078f183e0b78a94c18f1
Evidence tier: E1
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

## Task

Check the current dependency posture at HEAD and report the result. You do NOT bump anything — you report what advisories exist and whether a bump is warranted, for a later Cooperator decision.

## Checks

**1. Backend — audit lockfile for known vulnerabilities:**
```bash
cd backend
pip install pip-audit  # one-time, into venv or temp
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pip-audit -r <(env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/poetry export -f requirements.txt --without-hashes)
```
Or: `poetry show --outdated` + manually check OSV.dev for the Django/daphne/redis/django-axes versions currently locked.

**2. Frontend — `npm audit`:** `npm audit --audit-level=high` from `frontend/`. Record every HIGH or CRITICAL advisory with its fix version.

**3. Frontend — lockfile drift:**
- `npm ci --dry-run` or `npm install --package-lock-only --dry-run` to check if lockfile is stale against package.json.
- If drift exists, record the list of packages that would change.

**4. Tripwire tests** (these assert English strings; a locale/i18n bump may break them — expected casualties):
- `test_czech_minimum_length_validator_catalog_mismatch` in `backend/tests/test_locale_resolution.py:95`
- `test_drf_throttle_wait_suffix_stays_english` in `backend/tests/test_locale_resolution.py:112`
- Record their current status at HEAD (should be green — run just those two).

## Disposition table

| Package | Current | Latest safe | Advisories | Action |
|---|---|---|---|---|
| django | X | Y | N | bump / none |
| daphne | X | Y | N | bump / none |
| next | X | Y | N | bump / none |
| ... | | | | |
| Tripwire: czech_minimum_length | PASS/FAIL | — | — | expected casualty / survived |
| Tripwire: drf_throttle_wait_suffix | PASS/FAIL | — | — | expected casualty / survived |
| Lockfile drift (npm) | yes/no | — | — | list drifted packages |

## Pre-existing baseline

The last full dependency audit was at commit `19cfec9` / `7a197da` (2026-09-01), recorded in DEFECT_LEDGER.md. At that time: django 5.2.17 (OSV 0), daphne 4.2.3 (OSV 0), next 16.3.4, django-axes 8.3.1 (OSV 0). The Cooperator approved route-A bumps on 2026-09-01.

## Authority

```text
Filesystem: read-only on repo. Temp: /tmp/opencode/dep-probe/.
Network: authorized for npm audit, PyPI (pip-audit / pip install pip-audit), OSV.dev,
  and npm registry (npm audit). No provider calls, no web beyond audit tooling.
Dependencies: pip-audit one-time install OK; no lockfile writes.
Git: read-only. No commit, push, fetch.
Secrets: none.
Docker: none.
```

## Report

Begin `### Report for ORCHESTRATOR_CHAT`. Echo coordinates. Disposition table, tripwire status, lockfile drift, any NEW advisories vs the 2026-09-01 baseline. Authority expiry. Report justification: new-evidence.