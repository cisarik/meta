# Closure record — logical whole `infosec-hardening-and-vps-readiness` (Meta 16/00)

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: not-applicable
Result artifact or commit: 33ffa150fa520118e67a6670422fe7fae1c98741
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

Closing commit: `33ffa150fa520118e67a6670422fe7fae1c98741`  
AP pin at closure: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Public `refs/heads/main` at closure: `33ffa150fa520118e67a6670422fe7fae1c98741`  
Working tree at closure: `git status --porcelain=v1` EMPTY  
Predecessor whole `admin-frontend-console` (15/00) closed at `a892f740f194af2492c3865a9a1ea6dcf18ed1a7`  
Closed on 2026-09-09 by the Agent Orchestrator.

Artifact class: **closure record — authority for the fact of closure only.** It grants no authority to change the repository, deploy a host, or start a successor whole. Successor work takes authority from its own Orchestrator prompts.

This whole did not upgrade AP. The pin is unchanged. There is no Libre Tiles AP-upgrade ledger mutation to reconcile.

---

## 1. What this whole delivered

Libre Tiles now has staff-surface INFOSEC hardening, PostgreSQL dialect parity for production settings, fail-closed HTTPS/CSRF/proxy-indication controls, repository-owned VPS templates (nginx/systemd/runbook), and a loopback Next.js standalone production launch. Regular player UX was not rewritten. `WordAuthority.accepts_tokens` remains the sole formed-word authority. No live VPS was configured by this whole.

### Slice 1 — INFOSEC admin and simulation (accepted)

End commit: `a33433efe0abec263bc1008d7db46d2b6d13d44f`  
Independent R3: performed (session 03).

Simulation UUID/404 boundaries, replay/simulation projection, Next.js error contract, `authEpoch` refresh ownership (Zustand persist version stayed 6). Staff B GET of Staff A simulation remains 200; mutate remains 404.

### Slice 2 — PostgreSQL dialect parity (accepted)

End commit: `15793bb08f132a1e86e20708d7fa88ae9156df6d`

`CONN_MAX_AGE` default 600 and `CONN_HEALTH_CHECKS` only on the postgresql engine. Fast pytest stays SQLite. Opt-in `LIBRETILES_TEST_POSTGRES=1` uses disposable database `libretiles_pytest`, never compose DB `libretiles`.

### Slice 3 — Production headers, CSRF, throttles (accepted)

End commit: `7ffe0dc4d81b37afb1c22b68b55e7330869c86ef`

`CSRF_TRUSTED_ORIGINS` derived from CORS (optional override), fail-closed origin parse. `SECURE_PROXY_SSL_HEADER` env-gated, default off. Simulation 429 proofs via patched `SimpleRateThrottle.THROTTLE_RATES`. `SECURE_HSTS_PRELOAD` stays unset (Cooperator decision 5; Django `security.W021` still asserted).

### Slice 4 — VPS templates (accepted)

End commit: `2e034d85be72f34b1d967190aa0dd7b03a32dbc0`

`vps_preflight.sh` / `vps_deploy.sh` (`--confirm-vps`, no UFW enable), nginx split (Next AI/admin vs Django API, `/ws/` upgrade, overwrite `X-Forwarded-Proto`, loopback `:8001` callback and `:8443` contrib admin), Daphne + Next systemd units on `127.0.0.1`, `docs/vps_deployment_guide.md`. Isolated static tests: 11 passed at slice acceptance.

### Slice 5 — Next.js standalone production runtime (accepted)

End commit: `33ffa150fa520118e67a6670422fe7fae1c98741`

`output: "standalone"` with `allowedDevOrigins` preserved. Frontend unit runs `server.js` under `/usr/bin/env HOSTNAME=127.0.0.1 PORT=3000` so `EnvironmentFile` cannot bind `0.0.0.0`. Deploy copies `public/.` and `.next/static/.` into the standalone tree. Isolated static tests: 12 passed (Orchestrator re-run 12 passed in 0.10s).

---

## 2. Landed commit lineage

```text
a33433e  fix(security): harden simulation IDs, refresh session ownership, and admin payloads
15793bb  fix(db): persist PostgreSQL connections and prove dialect parity
7ffe0dc  fix(security): derive CSRF origins and gate proxy SSL indication
2e034d8  feat(ops): add VPS nginx, systemd, and deploy templates
33ffa15  feat(frontend): run production Next as a standalone server
```

Cosmetic residual in the Slice 5 commit body: `EnvironmentFileoverrides` (missing space). Amendment was prohibited; product/security impact none.

---

## 3. Closure conditions

| Condition | Status | Evidence |
|---|---|---|
| Slices 1–5 implemented and Orchestrator-accepted | **MET** | notes §1–§18; public `main` at `33ffa15` |
| Staff gate remains `IsAdminUser`; player UX not rewritten | **MET** | A1/A2 held; no gameplay page redesign in this whole |
| `WordAuthority.accepts_tokens` unchanged | **MET** | A3; gamecore not in later-slice allowlists |
| Proxy SSL default false until stripping nginx exists | **MET** | Slice 3 gate + Slice 4 nginx overwrite + runbook enablement |
| Standalone production bind is loopback | **MET** | unit ExecStart env prefix; tests forbid `0.0.0.0` |
| Fast default pytest remains SQLite | **MET** | A7; Postgres opt-in only |
| AP pin unchanged | **MET** | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Meta archive | **MET** | sessions 01–11 prompts/reports; append-only `00_notes.md` |
| Live VPS / R5 host gate | **not this whole** | templates and runbook only; operator-owned later |

---

## 4. Residual-risk disposition at closure

| Finding / residual | Severity | Decision | Approver | Rationale |
|---|---|---|---|---|
| IHR-S1-F01 simulation `pass` writes unsanitized `ai_metadata`; reads sanitize | low | accepted-residual | Orchestrator + Cooperator (Slice 1) | Staff-creator only; not mixed into later slices |
| IHR-S2-R01 `game.0008` count guard uses default alias | low | accepted-residual | Orchestrator | Trap for `migrate --database=<other>`; not Slice 2/4/5 scope |
| `SECURE_HSTS_PRELOAD` unset; `security.W021` asserted | info | accepted-residual | Cooperator decision 5 | Do not add preload |
| Leftover `backend/billing/migrations/` not in `INSTALLED_APPS` | info | accepted-residual | A4 | Do not revive billing |
| `DJANGO_SECURE_PROXY_SSL_HEADER` default false | info | accepted-residual / operational | Slice 3+4 | Safe only off, or behind installed stripping nginx |
| Unbound throttle scopes (state GET, stop, admin list/replay/analytics) | info | product-choice | Slice 3 | Not expanded in Slices 4–5 |
| `AGENTS.md` still says frontend deploy on Vercel | info | accepted-residual | Orchestrator | Out of Slice 4/5 allowlists; architecture Production corrected |
| README throttle-row prose still says `DEBUG=true` | info | accepted-residual | Orchestrator | Env-table key is `DJANGO_DEBUG` |
| Slice 5 commit body `EnvironmentFileoverrides` | info | accepted-residual | Orchestrator | Cosmetic; no amend |
| JWT in `localStorage`; `style-src 'unsafe-inline'`; no CI/SBOM | info | out-of-whole | prior product | Not this whole’s slices |
| Standalone tree exists only after operator `npm run build` on a VPS | info | operational | Slice 5 | Static tests do not certify generated `.next/standalone` |
| Live nginx/systemd/TLS/SSE/websocket on a named host | n/a | deferred | INFOSEC R5 later | No host was named; no R5 grant |

---

## 5. Logical whole closure declaration

Logical whole `infosec-hardening-and-vps-readiness` (Meta 16/00) is **CLOSED**.

The five tactical slices are accepted on public `main` at `33ffa150fa520118e67a6670422fe7fae1c98741`. Installing those templates on a VPS, obtaining certificates, and INFOSEC R5 host acceptance remain separate production authority.

A post-whole deep audit prompt (fresh Worker, large context) is recorded in notes §13 as successor Orchestrator work. It is not part of this closed whole and is not started by this record.
