Ordering probe je zelený; plný suite padá na `test_multi_provider_catalog_migration.py`, ktorý nie je v allowliste. Commit nespúšťam.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 06  
Worker exchange ordinal: 02

**Status:** BLOCKED  
**Phase-qualified result:** Implementation BLOCKED (non-independent). Game-app leaf restore and the three ordering probes are green. Catalog leaf restore, which this grant required, exposed a fourth pre-existing coupling outside the allowlist. No commit, no push, no self-certification.  
**Escalation disposition: NEEDS_ORCHESTRATOR_DECISION**

### Continuity-anchor verification

All five checks matched before mutation:

1. `HEAD` = `04fe823ac2eea6c8398dd9f00830d30d71568e97`; `git ls-remote origin refs/heads/main` = the same SHA.  
2. Porcelain was exactly the five exchange-01 entries.  
3. `game.0007_consumedwsticket` was applied (`[X] 0007_consumedwsticket`). Left applied.  
4. `.ap` gitlink and `.ap` HEAD = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.  
5. Exchange-01 evidence treated as a claim; every gate in this exchange was re-run.

Prior-authority expiry: exchange 01 expired with its terminal report. This prompt was the only current grant.

**Start commit:** `04fe823ac2eea6c8398dd9f00830d30d71568e97`  
**End commit:** unchanged; no corrective commit

### Changed paths (uncommitted; allowlist only)

| Path | Purpose |
|---|---|
| Carried: `backend/game/models.py`, `0007_consumedwsticket.py`, `services.py`, `config/settings.py`, `test_ws_ticket_single_use.py` | Exchange-01 single-use candidate, unchanged in intent |
| `backend/tests/_migration_restore.py` | New test-only helper: `restore_apps_to_leaf(*app_labels)` → `call_command("migrate", app, verbosity=0)` (current leaf, no pinned name) |
| `backend/tests/test_creditless_migration.py` | `finally` restore catalog+game via helper; subject reverse targets 0007/0004 unchanged |
| `backend/tests/test_scoreless_turns_migration.py` | Separate `finally` restore via helper; `migrate_from` / `migrate_to` unchanged |
| `backend/tests/test_openrouter_catalog_migration.py` | `try`/`finally` restores catalog+game+accounts; subject 0007/0004/accounts-0002 unchanged |
| `backend/tests/test_dynamic_free_catalog_migration.py` | `finally` catalog leaf restore; subject 0008/0009 unchanged |
| `backend/tests/test_playable_seeded_prompts_migration.py` | `finally` catalog leaf restore; subject 0010 and in-test forward unchanged |
| `backend/tests/test_refresh_seeded_prompts_migration.py` | `finally` catalog leaf restore; subject 0009/0010 unchanged |
| `backend/.env.example`, `README.md` | Documented TTL default `60` → `10` only |

### Evidence

**A. Full suite, default order** (re-run this exchange):

```text
1 failed, 297 passed, 4 skipped in 138.79s (0:02:18)
```

Expected: 287 + 11 new = 298 passed, 4 skipped, zero failures.  
Actual: the 11 new tests passed; one **existing** test failed:

`tests/test_multi_provider_catalog_migration.py::MultiProviderCatalogMigrateCommandTests::test_backward_and_forward_preserve_rows_and_do_not_reactivate`  
`catalog.models.AIModel.DoesNotExist` for `PREPARED_MODELS[0]` (`provider=groq`, `model_id=openai/gpt-oss-120b`) after `call_command("migrate", "catalog", "0012_multi_provider_free_rivals")`.

Cause: that test is not in the allowlist. It assumes some earlier file left `catalog` **behind** 0012 so that `migrate catalog 0012` re-runs the 0012 data step after `TransactionTestCase` flush. `test_dynamic_free_catalog_migration.py` previously left schema at 0009 (that was the accidental feeder). This grant required a catalog **leaf** restore there; after flush the schema is already 0012, the opening migrate is a no-op, and the prepared rows are gone. `test_multi_provider_catalog_migration.py` already has a lawful `finally: call_command("migrate", "catalog", verbosity=0)` — the defect is the opening baseline, not teardown.

**B. Ordering-independence probes**

Pre-fix (this exchange, before editing the six test files):

| Probe | Result |
|---|---|
| creditless + WS | `4 failed, 14 passed` — `OperationalError: no such table: game_consumed_ws_ticket` on the four connect tests |
| scoreless + WS | `4 failed, 11 passed` — same `no such table` |
| openrouter + WS | `19 passed` — **did not fail**. That file already ends with `call_command("migrate")` (all apps), which re-applies `0007` before WS tests. The 0004 subject still unapplies `0007` mid-test; restore was accidental, not a `finally`. |

Post-fix:

| Probe | Result |
|---|---|
| creditless + WS | `18 passed` |
| scoreless + WS | `15 passed` |
| openrouter + WS | `19 passed` |

**C. Subject preservation (MISS 1)**

`test_scoreless_turns_migration.py` still has:

```python
    migrate_from = [("game", "0005_remove_money_state")]
    migrate_to = [("game", "0006_rename_consecutive_scoreless_turns")]
```

Unchanged from `04fe823`. The body still migrates `migrate_from` → `migrate_to` → `migrate_from`. The `finally` now calls `restore_apps_to_leaf("game")` instead of `executor.migrate(self.migrate_to)`.

**D. mypy** (this exchange): `Success: no issues found in 79 source files`  
**E. ruff:** `All checks passed!`  
**F. makemigrations --check --dry-run:** `No changes detected`

**G. Tests 1–11** (re-run this exchange, not copied from 01): `11 passed in 2.30s`

| # | Result this exchange |
|---|---|
| 1–11 | all PASSED |

**H. Allowlist diff vs `04fe823`**

```text
git diff --name-only 04fe823…:
README.md
backend/.env.example
backend/config/settings.py
backend/game/models.py
backend/game/services.py
backend/tests/test_creditless_migration.py
backend/tests/test_dynamic_free_catalog_migration.py
backend/tests/test_openrouter_catalog_migration.py
backend/tests/test_playable_seeded_prompts_migration.py
backend/tests/test_refresh_seeded_prompts_migration.py
backend/tests/test_scoreless_turns_migration.py

untracked:
backend/game/migrations/0007_consumedwsticket.py
backend/tests/_migration_restore.py
backend/tests/test_ws_ticket_single_use.py
```

`backend/game/consumers.py` and `frontend/**` are absent. `backend/db.sqlite3` is gitignored and not in porcelain.

### Confirmations

- `migrate_from` / `migrate_to` in `test_scoreless_turns_migration.py` are unchanged.  
- No existing test was weakened, skipped, xfailed, deleted, or reordered. No pytest plugin.  
- No `OperationalError` (or other missing-table) swallow was added to `backend/game/services.py`. Consume still raises `IntegrityError` → `GameNotFoundError` only.  
- Ticket-to-user, ticket-to-game, and `_load_session_for_user` still run **before** consume.  
- **Query-string transport remains** as a Cooperator-accepted residual of audit-01-F09. `consumers.py` `connect()` was not touched.

### Authorized Git result

Not performed. Standing full-suite pytest is not green. origin `main` remains `04fe823ac2eea6c8398dd9f00830d30d71568e97`. Porcelain is dirty with the allowlisted candidate.

### Deviations, risks, missing evidence

- Full-suite gate red on one existing test outside the allowlist (see A).  
- Openrouter pre-fix probe was green; the game-app pin was real mid-test but masked by a terminal untargeted `migrate`. A `finally` was still added so restore does not depend on that last line.  
- Human-vs-human multiplayer was **not** exercised manually in a browser.  
- No live provider call; no `.env` / `.env.local` read; no ticket/secret printed.  
- Correction remains non-independent. Fresh independent re-audit is still mandatory after a green commit.

### Out-of-scope observations (not findings)

- `test_multi_provider_catalog_migration.py` opening `migrate catalog 0012` is not self-contained at a flushed leaf. Not modified.  
- Catalog HEAD is still `0012_multi_provider_free_rivals`; creditless’s old hardcoded catalog restore was already the leaf.

### Smallest next step

Expand the allowlist by **one file**: `backend/tests/test_multi_provider_catalog_migration.py`. Make the opening baseline self-contained so 0012 **data** re-applies after a flushed leaf, for example migrate `catalog` to `0011_playable_seeded_prompts` then to `0012_multi_provider_free_rivals` (the same pair the test body already uses), without changing what it asserts. Then current-worker-session re-runs A–H, one commit, push, and the Orchestrator routes the mandatory re-audit. Do not route S6 until this slice is committed.

**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  
**Authority expiry:** this exchange’s authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** Continuity porcelain matched. Did not change `migrate_to` in the scoreless test (MISS 1). Did not treat openrouter’s assertRaises 0004 call as a restore target; wrapped it with a separate `finally`. Did not swallow missing-table errors. Catalog leaf restore in `test_dynamic_free_catalog_migration.py` was applied as granted and is what surfaced the multi_provider coupling; that file was not reverted. Residual risk: dirty tree plus applied `0007` on the development DB.

**Pre-Existing Failure Classification:** `MultiProviderCatalogMigrateCommandTests.test_backward_and_forward_preserve_rows_and_do_not_reactivate` depends on some earlier test leaving `catalog` schema behind 0012 so the opening `migrate catalog 0012` re-runs `prepare_free_rivals` after flush. That coupling was latent at the start commit (fed by dynamic leaving 0009). It is a test-harness isolation defect, not a product defect and not evidence against single-use. Exposed by the authorized catalog leaf restore. Not repaired: file is outside the allowlist.