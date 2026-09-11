You are a WORKER instance. Perform exactly this bounded diagnostic task and stop. This is a DISPOSITION report, not a fix.

```text
Logical whole identity: test-breadth-and-baseline-disposition
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Task identity: TB-PROBE-01 — run every opt-in test suite once and record each result for disposition. No fixes, no correction, read-only on the repo.
Phase: Diagnostic Closeout
Exact baseline: 4d33ad618dc131662193078f183e0b78a94c18f1
Evidence tier: E1
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

## Task

Run each opt-in backend test suite at HEAD, record the outcome and runtime, and produce a disposition table. **You fix nothing.** Test failures or anomalies are evidence, not your job to correct.

## Suites to run

**1. Postgres parity** (needs docker-compose.dev.yml Postgres):
- `docker compose -f docker-compose.dev.yml up -d postgres`
- `env -u APPIMAGE -u ARGV0 -u APPDIR LIBRETILES_TEST_POSTGRES=1 .venv/bin/pytest tests/test_postgres_dialect_parity.py -v`
- Record: tests passed/failed, runtime
- `docker compose -f docker-compose.dev.yml down` (cleanup)

**2. Slow benchmarks** (`LIBRETILES_RUN_BENCHMARKS=1`):
- `env -u APPIMAGE -u ARGV0 -u APPDIR LIBRETILES_RUN_BENCHMARKS=1 .venv/bin/pytest tests/test_board_defense_benchmark.py tests/test_endgame_benchmark.py tests/test_endgame_policy_matrix.py -m slow -q`
- Record: passed/failed, runtime
- (other slow-marked tests like `test_slovak_full_game.py`, `test_full_game_simulation.py`, `test_slovak_strength.py`, `test_strength_benchmark.py` — if they have env gates, try running them with their documented env var; if no gate, just `-m slow`)

**3. All env-gated vitest suites** (no provider call — read-only markers):
- `PROVIDER_PROBE_LIVE=1 npx vitest run src/lib/provider-capability.live.test.ts` — skip if it needs provider calls (sentinel-gated — check)
- List any sentinel-skipped vitest files with their gate names

**4. Playwright/e2e** — search for any Playwright configs or e2e directories. Record presence/absence. (Expected: none — PRD planned.)

## Disposition table (output this in your report)

| Suite | Ran? | Passed/Failed | Runtime | Disposition (recommend) |
|---|---|---|---|---|
| Postgres parity | yes/no | N | Xs | CI candidate / manual-only / not-runnable |
| Slow benchmarks | yes/no | N | Xs | CI candidate / manual-only |
| ... (each env-gated suite) | | | | |
| Playwright e2e | N/A | — | — | deferred to D1 (UI/UX) |

## Authority

```text
Filesystem: read-only on repo. Temp: /tmp/opencode/tb-probe/.
Docker: authorized — docker compose -f docker-compose.dev.yml up/down postgres only.
  No other services, no production compose, no swarm, no image push/pull beyond the
  already-pinned postgres:16.15-alpine3.24. Docker network: local only.
Git: read-only. No commit, push, fetch.
Network: no web, no provider calls, no npm registry, no PyPI.
  Docker image pull if needed for the pinned postgres SHA is authorized.
Secrets: LIBRETILES_DEV_POSTGRES_PASSWORD from the Cooperator's host env (docker compose reads it).
  Never print, hash, or log it.
```

## Report

Begin `### Report for ORCHESTRATOR_CHAT`. Echo coordinates. Disposition table. Cleanup of docker compose resources. Authority expiry. Context pressure. Report justification: new-evidence.