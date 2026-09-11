# Closure record — logical whole `test-breadth-and-baseline-disposition` (Meta 19/05)

```text
Logical whole identity: test-breadth-and-baseline-disposition
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable (read-only probe)
Result evidence: probe-PARTIAL (01_report_00.md)
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

Probe at 4d33ad6. Cooperator decisions 2026-09-10:

| Item | Disposition |
|---|---|
| Board-defense wide acceptance red (SK winrate 0.45) | ACCEPTED RESIDUAL — known-fail, manual-only, not a CI gate |
| Endgame wide acceptance (green but fragile, +4) | manual-only |
| Postgres parity (`LIBRETILES_TEST_POSTGRES=1`) | deferred to CI (needs synthetic CI password + Postgres service) |
| Nightly CI suites | endgame matrix (106 s), Slovak full-game extra (11 s), 100-seed witness (63 s) — CI candidates; implementation deferred to W-E follow-up |
| Strength-100 (9.5 min) | nightly candidate, not urgent |
| Endgame 100-pair (38 min) | manual-only |
| Board-defense wide (112 min) | manual-only + known-fail |
| Playwright e2e | deferred to D1 (UI/UX) |

Dirty worktree (12 modified + `opt_in.py` overlay — `LIBRETILES_RUN_SIMULATION` gating) is Cooperator in-progress work; not triage scope.