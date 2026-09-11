# Closure record — logical whole `dockerized-vps-deployment` (Meta 18/00)

```text
Logical whole identity: dockerized-vps-deployment
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: not-applicable
Result artifact or commit: 996d9c78af90d1fea21e3c701283ba11e59de0b1
Result evidence: implementation-PASS (06_report_00), acceptance-PASS (05_report_00 on d554d11b; 07_report_00 on c2d08f48 with DVP-AUDIT-05-F02 verified-closed), publication-PASS (08_report_00)
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

Publishing commit: `996d9c78af90d1fea21e3c701283ba11e59de0b1` (parent `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`)  
AP pin at closure: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Public `refs/heads/main` at closure: `996d9c78af90d1fea21e3c701283ba11e59de0b1`  
Working tree at closure: `git status --porcelain=v1` EMPTY  
Predecessor whole `public-docs-and-stale-truth` (17/00) closed at `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`  
Closed on 2026-09-10 by the Agent Orchestrator.

Artifact class: **closure record — authority for the fact of closure only.** It grants no authority to change the repository, deploy a host, issue certificates, configure a schedule, or start a successor whole. Successor work takes authority from its own Orchestrator prompts.

This whole did not upgrade AP. The pin is unchanged and no Libre Tiles AP-upgrade ledger is declared in project rules, so there is no ledger mutation to reconcile.

---

## 1. What this whole delivered

The production deployment ownership moved from systemd/host-nginx to one hardened Docker Compose topology, validated statically and dynamically on the exact published artifact.

Published commit `996d9c7` contains exactly the accepted 45-path candidate:

- **Topology** (`docker-compose.yml`): `postgres`, `redis`, one-shot `backend-init`, `backend` (Daphne), `nginx`, `frontend`, profile-gated `certbot` and `db-tools`; nginx is the only host-published service (public 80/443, private host-loopback 8443); internal data/cache networks; named durable volumes.
- **Backend runtime**: Daphne on a group-restricted Unix socket `socket 770 10001:10001` via `--endpoint "unix:${socket}:mode=0770"`; `/app/.venv` built at its exact runtime path; ASGI initializes Django settings before importing Channels/game routing.
- **Frontend runtime**: Next standalone at `127.0.0.1:3000` inside nginx's network namespace (`network_mode: service:nginx`), capability-free, no independent network or host port; closed-key secret-file loader.
- **Edge/TLS** (`deploy/nginx/*`, `deploy/certbot/*`): fail-closed challenge bootstrap, full-mode TLS with literal-domain redirect target, canonical-host rejection on 443, proxy-header overwrite, SSE/websocket behavior preserved, private Django admin only on host loopback.
- **Secrets**: dedicated reader GID `10004`; host sources `0:10004/0440`; `group_add` only on `postgres`, `backend-init`, `backend`, `frontend`, `db-tools`; least-scope mounts; no Compose secret target metadata; no world-readable value.
- **Recovery** (`deploy/postgres/*`): validated logical backup, disposable restore, migration-count comparison, negative guardrails.
- **Truth guards**: `backend/tests/test_docker_deployment.py` plus the extended `scripts/validate_docker_deployment.sh`; the ten whole-17 documentation/dictionary guards remain green.
- **Owner migration**: systemd units, host-nginx template, `vps_preflight.sh`, `vps_deploy.sh`, and `test_vps_templates.py` deleted; public docs document the Docker deployment and local development remains non-production.

## 2. Phase results

| Result | Status | Evidence |
|---|---|---|
| Implementation PASS | MET | `01_report_03.md` candidate, completed through corrections to `06_report_00.md` (`implementation-PASS`) |
| Acceptance PASS | MET | `05_report_00.md` (`acceptance-PASS`, digest `d554d11b…`, no blocking findings); `07_report_00.md` (`acceptance-PASS`, corrected digest `c2d08f48…`, DVP-AUDIT-05-F02 `verified-closed`) |
| Publication PASS | MET | `08_report_00.md`; commit `996d9c78af90d1fea21e3c701283ba11e59de0b1` equals public `refs/heads/main` by direct `git ls-remote` readback |
| Deployment PASS | NOT APPLICABLE | artifact-only whole; live-host install was explicitly out of scope (R5 deferred) |
| Production acceptance | NOT APPLICABLE | no production system touched |
| ORCHESTRATOR closure | MET | this record |

## 3. Correction lineage (all on top of the accepted plan DVP-PLAN-01/02)

- nginx master/worker split: master `0:10001` with exactly `NET_BIND_SERVICE`, `SETGID`, `SETUID`; workers `10002:10001` zero capabilities; explicit worker-owned temp tmpfs; no runtime `chown`.
- Certificate link/target/directory semantics: targets `0640 10002:10001`, directories `0750 10002:10001`, relative live symlinks.
- Secret delivery: dedicated GID `10004`, `0:10004/0440` sources and targets, trapped `0701` validation-only helper window.
- Backend runtime: `/app/.venv` path-preserving console scripts; ASGI settings-initialization order.
- Unix socket: Twisted endpoint `mode=0770` restoring `socket 770 10001:10001`.
- Validator measurement fixes: anchored nginx-worker probe; container-identity paired-recreation check; canonical port-80 redirect assertions.
- Edge redirect: full-mode port-80 fallback uses the literal validated `DOMAIN`, removing request-host reflection.

## 4. Closure conditions

| Condition | Status | Evidence |
|---|---|---|
| Accepted candidate is the published commit | **MET** | `996d9c7` public `main`; tree/path set equals the 45-path candidate |
| Independent acceptance performed | **MET** | `05_report_00.md`, `07_report_00.md` (fresh sessions 05 and 07) |
| No active mutation | **MET** | `git status --porcelain=v1` empty; index clean; no lock/operation |
| AP pin unchanged | **MET** | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Host/deployment not claimed | **MET** | no host, certificate, DNS, or production action in any exchange |
| Public documentation truth | **MET** | deployment docs updated; whole-17 guards green; systemd production owners removed |
| Docker validator PASS on final artifact | **MET** | `06_report_00.md` and `07_report_00.md` exact exit-0 runs |
| Backend gates | **MET with declared residual** | mypy/ruff/migrations clean; pytest `1242 passed` except the whole-17 parity-oracle red |
| Frontend gates | **MET with declared residuals** | typecheck/lint/build clean; two pre-existing test reds |

## 5. Residual-risk disposition at closure

| Item | Severity | Decision | Approver | Rationale |
|---|---|---|---|---|
| Port 80 answers any well-formed `Host` with `301` to the literal canonical domain instead of closing | info | accepted-residual | Orchestrator | Non-blocking; the reflection is removed; 443 already rejects non-canonical hosts; bootstrap fails closed |
| Whole-17 parity-oracle payload test red (`inspection` block vs pinned baseline) | medium (suite-red, not a security defect) | accepted-residual, carry forward | Orchestrator + Cooperator (whole-17) | Pre-existed at `33ffa15`; oracle must not be edited to follow implementation; owned by `codebase-hygiene-and-residual-reconciliation` |
| `frontend/src/lib/i18n/i18n.test.ts` live-region count red | low (quality/accessibility pin) | accepted-residual, carry forward | Orchestrator | Pre-existing committed `aria-live` attributes; candidate touches no non-test frontend source; owned by the hygiene whole |
| `frontend/src/components/admin/ReplayControls.test.ts` stale expectation | low (quality) | accepted-residual, carry forward | Orchestrator | Committed fixture renders `AT for 4 points`; candidate-independent; owned by the hygiene whole |
| R5 host hardening, real ACME/DNS/TLS issuance, off-host backup transport, monitoring/alerts, catalog-refresh schedule | deferred | not assessed | — | Explicitly outside this whole; require a separate Cooperator host grant |

Accepted R4 finding set: `DVP-AUDIT-05-F01` and `DVP-AUDIT-05-F03` rejected as false positives; `DVP-AUDIT-05-F02` corrected and independently `verified-closed`. No medium-or-higher finding remains open from this whole.

## 6. Out-of-scope observations (ledger candidates, non-authorizing)

- `X-Powered-By: Next.js` on public responses; `server_tokens off` already suppresses the nginx version.
- Undefined websocket paths return HTTP 500 with a Channels traceback (baseline behavior, unmodified files).
- The nginx certificate watcher retries a failing `nginx -t` every 5 seconds while the reload marker persists.
- Malformed or `user@host`-style `Host` headers on port 80 receive nginx `400` with no `Location`.

## 7. Forward horizon (not authority)

1. **Live host deployment (R5)** — install the published Compose topology on a real VPS under a separate Cooperator host grant, including host hardening, firewall, DNS, real ACME issuance, off-host encrypted backups, and monitoring. Needs the Cooperator's provider/host and domain decisions.
2. **`codebase-hygiene-and-residual-reconciliation`** — carry the parity-oracle re-pin, the two frontend test reds, and the ledger candidates above.
3. **Optional catalog-refresh schedule** — configure `libretiles-openrouter-catalog-refresh` only under separate production authority.

No successor whole is opened by this record. A fresh Orchestrator restores from canonical repository, this closure record, and the Meta 18/00 exchange history, then asks the Cooperator to select exactly one next bounded logical whole.
