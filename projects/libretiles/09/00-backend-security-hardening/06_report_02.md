### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 06  
Worker exchange ordinal: 03

**Status:** PASS  
**Phase-qualified result:** Implementation PASS (non-independent). Bounded candidate produced and gated; this Worker does not certify the correction, does not close the whole, and does not perform the mandatory fresh independent re-audit.

### Continuity-anchor verification

All five checks matched before mutation:

1. `HEAD` = `04fe823ac2eea6c8398dd9f00830d30d71568e97`; `git ls-remote origin refs/heads/main` = the same SHA.  
2. `.ap` gitlink and `.ap` HEAD = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.  
3. Porcelain was exactly the fourteen named entries.  
4. `game.0007_consumedwsticket` was applied; left applied.  
5. Prior-exchange evidence treated as a claim; every gate in this exchange was re-run.

**Start commit:** `04fe823ac2eea6c8398dd9f00830d30d71568e97`  
**End commit:** `437e20f95a671474074afcb7c412d7733426c72e`

### Changed paths

| Path | Purpose |
|---|---|
| `backend/game/models.py` | `ConsumedWsTicket`: SHA-256 hex unique `ticket_hash`, `expires_at`; never stores the ticket |
| `backend/game/migrations/0007_consumedwsticket.py` | Creates `game_consumed_ws_ticket` |
| `backend/game/services.py` | 10s TTL at call time, per-issue nonce, DB consume via unique insert, bounded cleanup |
| `backend/config/settings.py` | `GAME_WS_TICKET_MAX_AGE_SECONDS` default `10` |
| `backend/tests/test_ws_ticket_single_use.py` | Regression tests 1–11 for audit-01-F09 replay |
| `backend/tests/_migration_restore.py` | Test-only `restore_apps_to_leaf` |
| Six migration-test files | Teardown restores to current app leaf; subjects unchanged |
| `backend/tests/test_multi_provider_catalog_migration.py` | Opening baseline 0011 then 0012 so 0012 data re-runs after flush |
| `README.md`, `backend/.env.example` | Documented TTL default `60` → `10` |

### Evidence

**A. Full suite, default order (this exchange):**

```text
298 passed, 4 skipped in 138.32s (0:02:18)
```

287 baseline + 11 new = 298; zero failures.

**B. Ordering-independence probes (this exchange):**

| Probe | Result |
|---|---|
| creditless + WS | `18 passed` |
| scoreless + WS | `15 passed` |
| openrouter + WS | `19 passed` |

**C. Branch 1 failing-direction probes:**

| Probe | Result |
|---|---|
| `test_dynamic_free_catalog_migration.py` then `test_multi_provider_catalog_migration.py` | `5 passed` |
| `test_multi_provider_catalog_migration.py` **alone** | `3 passed` |

Alone is the real lock: it no longer depends on leftover non-leaf schema.

**D. Assertions unchanged vs `04fe823`.** Only the opening migrate and its comment changed. Before and after, the test still has:

```python
        row = AIModel.objects.get(
            provider=metadata["provider"], model_id=metadata["model_id"]
        )
        ...
            assert row.is_active is False
        ...
            assert row.is_active is False
            assert AIModel.objects.filter(pk=row_id).exists()
```

`finally: call_command("migrate", "catalog", verbosity=0)` is unchanged.

**E. mypy:** `Success: no issues found in 79 source files`  
**F. ruff:** `All checks passed!`  
**G. makemigrations --check --dry-run:** `No changes detected`  
**H. Tests 1–11** (this exchange): `11 passed in 2.26s` — all PASSED.

**I. Diff vs `04fe823`:**

```text
git diff --stat 04fe823..437e20f
 README.md                                          |   2 +-
 backend/.env.example                               |   2 +-
 backend/config/settings.py                         |   2 +-
 backend/game/migrations/0007_consumedwsticket.py   |  25 +++
 backend/game/models.py                             |  18 ++
 backend/game/services.py                           |  54 ++++-
 backend/tests/_migration_restore.py                |  15 ++
 backend/tests/test_creditless_migration.py         |   4 +-
 backend/tests/test_dynamic_free_catalog_migration.py |  30 +--
 backend/tests/test_multi_provider_catalog_migration.py |  11 +-
 backend/tests/test_openrouter_catalog_migration.py |  66 +++---
 backend/tests/test_playable_seeded_prompts_migration.py |  34 +--
 backend/tests/test_refresh_seeded_prompts_migration.py |  38 ++--
 backend/tests/test_scoreless_turns_migration.py    |   5 +-
 backend/tests/test_ws_ticket_single_use.py         | 250 +++++++++++++++++++++
 15 files changed, 465 insertions(+), 91 deletions(-)
```

`backend/game/consumers.py` and `frontend/**` are absent. `backend/db.sqlite3` was not staged (`*.sqlite3` gitignored).

**J. Branch taken:** **Branch 1 (primary).** After the 0011→0012 opening baseline, the full suite was green (298 passed, 4 skipped). Branch 2 was not used.

### Confirmations

- No existing test was weakened, skipped, xfailed, deleted, or reordered. No assertion text was changed.  
- No missing-table / `OperationalError` swallow exists in `backend/game/services.py`. Consume raises `IntegrityError` → `GameNotFoundError` only.  
- Ticket-to-user, ticket-to-game, and `_load_session_for_user` still run **before** consume.  
- **Query-string transport remains** as a Cooperator-accepted residual of audit-01-F09. `consumers.py` `connect()` was not touched.

### Authorized Git result

- Commit: `437e20f95a671474074afcb7c412d7733426c72e` — `fix(ws): make game websocket tickets single-use`  
- Pre-push gate: `git ls-remote origin refs/heads/main` was still `04fe823ac2eea6c8398dd9f00830d30d71568e97`  
- Push: `git push origin main` → `04fe823..437e20f  main -> main`  
- Public readback: `git ls-remote origin refs/heads/main` = `437e20f95a671474074afcb7c412d7733426c72e`; `git rev-parse HEAD` = the same SHA  
- Post-push porcelain: empty; `## main...origin/main`

### Deviations, risks, missing evidence

- Human-vs-human multiplayer was **not** exercised manually in a browser. Coverage is the synthetic WS harness (tests 6, 7, 11 and `test_multiplayer_ws.py`).  
- No live provider call; no `.env` / `.env.local` read; no ticket/secret printed.  
- Query-string ticket remains capturable within the 10s TTL (accepted residual).  
- This correction is non-independent. Fresh independent re-audit (INFOSEC.md 4.11, P-10) is still mandatory.

### Out-of-scope observations (not findings)

- Exchange-02 measurement stands: openrouter’s pre-fix WS probe was genuinely `19 passed` because of its terminal untargeted `migrate`; the explicit `finally` is still present.  
- Catalog-app leaf restores from exchange 02 were **kept** (Branch 1 succeeded). The suite is less dependent on leftover catalog schema than at `04fe823`; remaining catalog tests that still pin named subject targets are unchanged by design.

### Smallest next step

Orchestrator routes the mandatory **fresh independent re-audit** of this correction plus the original audit-01-F09 replay claim. After that, S6 (security response headers and CSP).

**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  
**Authority expiry:** this exchange’s authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** Continuity porcelain matched. Branch 1 applied without touching assertions. Did not take Branch 2. AppImage Python intercept classified; used the authorized `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/...` route. Residual risk: none from a fourth coupling in this run.

**Pre-Existing Failure Classification:** The `MultiProviderCatalogMigrateCommandTests` opening `migrate catalog 0012` was a no-op at a flushed leaf; it only passed when another test left catalog behind 0012. That isolation defect is repaired in this commit (0011 then 0012, with a comment that `TransactionTestCase` flushes migration-inserted data). Not a product defect.