You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task and stop.

```text
Logical whole identity: github-actions-ci-and-sbom
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: CI-S1-IMPL — create GitHub Actions CI workflow (backend + frontend gates) and SBOM generation workflow. Two files, one commit. Closes G6 / audit-02-F05 (medium, Cooperator sign-off 2026-09-01, approved pre-release 2026-09-10).
Phase: Implementation
Implementation authority: explicit
Exact baseline: a9491081733cfa05e439845e78f26191f15f0abe
Independence required: no
Evidence posture: non-independent
Evidence tier: E0
Evidence tier basis: new YAML files only; no executable code, no test, no production path; CI runs only when GitHub Actions processes them (external).
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/.github/workflows/ci.yml      (NEW)
  /home/agile/Projects/libretiles/.github/workflows/sbom.yml     (NEW)
```

## Goal

Create two GitHub Actions workflow files that gate the standing quality checks on push and pull request to `main`, and produce explicit CycloneDX SBOM artifacts. The R2 pre-existing red (i18n aria-live count) is explicitly allowlisted so unexpected new failures still block CI. audit-02-F05 (no CI/SBOM) is closed by this.

## Changes

### `.github/workflows/ci.yml` (new file)

One workflow with two jobs — `backend` and `frontend` — that both run on `push` and `pull_request` to `main`. Use `ubuntu-24.04`.

**Backend job:**
- Python 3.12 (actions/setup-python)
- Install Poetry via pip, then `poetry install` in `backend/`
- Steps (each a separate step with a name):
  1. `mypy config game gamecore accounts catalog` (from `backend/`)
  2. `ruff check .` (from `backend/`)
  3. `python manage.py makemigrations --check --dry-run` (from `backend/`)
  4. `pytest` (from `backend/`; expect green — 1244+ passed, 0 failed, exit 0)

**Frontend job:**
- Node 24 (actions/setup-node)
- `npm ci` in `frontend/`
- Steps:
  1. `npm run typecheck`
  2. `npm run lint`
  3. `npm run build`
  4. `npx vitest run` — the i18n aria-live test (`AC-ONE-LIVE-REGION` describe in `src/lib/i18n/i18n.test.ts`) is a known pre-existing red (expects 1 live region, measures 3; owned by deferred UI/UX). The vitest step must NOT fail the workflow because of this ONE known test. Technique: run vitest, capture the list of failed test files, assert that the only failure is `i18n.test.ts`. If any OTHER test fails, the step exits non-zero. If zero tests fail, exit 0. Example shell logic:
   ```yaml
   - name: Run tests
     run: npx vitest run --reporter=json > vitest-results.json; EXIT=$?
   - name: Allowlist R2 only
     run: |
       FAILURES=$(jq -r '.testResults[] | select(.status=="failed") | .name' vitest-results.json)
       OK="i18n.test.ts"
       for f in $FAILURES; do
         case "$f" in *"$OK"*) continue ;; *)
           echo "UNEXPECTED FAILURE: $f" >&2; exit 1 ;;
         esac
       done
       echo "All failures are allowlisted (R2 aria-live in i18n.test.ts)"
   ```

Use `jq` (pre-installed on ubuntu-24.04 runners).

### `.github/workflows/sbom.yml` (new file)

One job that runs on `push` to `main` (not PR — SBOMs on merge only) and generates two CycloneDX SBOM artifacts:

**Backend SBOM:** `poetry export -f requirements.txt -o /tmp/requirements.txt` from `backend/`, then use `cyclonedx-py` or `pip install cyclonedx-bom && cyclonedx-py -r -i /tmp/requirements.txt -o backend-sbom.json`. Simpler: use `pipdeptree` + `cyclonedx-bom`. Even simpler: `pip install cyclonedx-bom && cyclonedx-bom -r -i <(poetry export -f requirements.txt) -o backend-sbom.xml` (CycloneDX XML). Use whatever toolchain produces valid CycloneDX with minimal dependencies.

**Frontend SBOM:** `npm sbom --sbom-format cyclonedx > frontend-sbom.json` from `frontend/` (npm 10 ships with `npm sbom`; Node 24 includes npm 10).

Upload both as workflow artifacts: `actions/upload-artifact`.

## Work sequence

1. Repo gate: `a9491081733cfa05e439845e78f26191f15f0abe`, AP `9c5cc44f`, clean, `main`.
2. Create `.github/` and `.github/workflows/` directories. Write both files.
3. Verify YAML validity: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml')); yaml.safe_load(open('.github/workflows/sbom.yml')); print('YAML valid')"` (PyYAML is in the venv).
4. `git diff --stat` — 2 files only.
5. Validation: backend pytest (green), frontend gates (typecheck/lint/build/vitest — 1 expected red). Since you've added no code, these should be unchanged from baseline.
6. Commit + push: `ci: add GitHub Actions workflow and CycloneDX SBOM generation`. `ls-remote` matches.

## Authority

```text
Filesystem: create .github/workflows/ + 2 YAML files. Temp: /tmp/opencode/ci-s1/.
Git: stage/commit/push non-force. Network: push + ls-remote only. No deps, Docker, secrets.
```

## Report contract

`### Report for ORCHESTRATOR_CHAT`. Echo: Logical whole identity: github-actions-ci-and-sbom, Worker session ordinal: 01, Worker exchange ordinal: 01. status PASS, Phase-qualified result: implementation-PASS, commit, gates (backend pytest green, frontend unchanged), 2 files, Report justification: new-mutation, authority expiry.