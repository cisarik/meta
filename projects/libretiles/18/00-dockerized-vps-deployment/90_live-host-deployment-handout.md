# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, Live VPS Deployment (Docker, R5)

Authored by the Agent Orchestrator at the closure of logical whole 18 (`dockerized-vps-deployment`) at commit `996d9c78af90d1fea21e3c701283ba11e59de0b1`, on 2026-09-10. Seeds ONE candidate logical whole: `docker-live-host-deployment`. This is a FORWARD-HORIZON handout, not a live grant.

---

## Handout Integrity Record (D-13)

```text
Supersedes: none — this file is a NEW forward-horizon handout for a future whole.
Sections of other handouts that remain LIVE: none carried here (this whole is not open yet).
Coordinate review: honest; written against the published commit 996d9c78af90d1fea21e3c701283ba11e59de0b1
  on 2026-09-10. Repository facts below were read from the whole-18 closure record and Meta 18/00
  reports, not re-measured token-by-token in this session; mark file:line claims as hypothesis and
  re-measure before citing.
Enumeration fidelity: paraphrased from the whole-18 closure record (Meta
  18/00-dockerized-vps-deployment/99_closure.md) and the audit/correction reports; NOT quoted-exactly.
  Re-derive every file path before issuing any Worker prompt.
Numbers not re-measured: live host provider, hardware capacity, provider quotas, current DNS records,
  real ACME rate limits, backup destination, and monitoring channel. All are Cooperator-owned and
  must be decided, not assumed.
Known-stale-by-design: none for the published artifact. The real host state does not exist in this
  repository and is unmeasured by design; nothing below claims a live install.
Predecessor whole: 18/00-dockerized-vps-deployment CLOSED at 996d9c7.
Baseline commit: 996d9c78af90d1fea21e3c701283ba11e59de0b1 (origin/main aligned at closure, clean tree).
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (detached HEAD at .ap, DO NOT upgrade).
```

---

You are a fresh Agent Orchestrator for Libre Tiles. This file grants you NO authority of any kind — not repository, implementation, deployment, production, account, filesystem, Git, browser, credential, provider, host, network, AP-upgrade, or closure authority. Verify repository and public truth independently before issuing any Worker prompt.

Your candidate logical whole identity: `docker-live-host-deployment`

---

## 0. Why this whole exists (Cooperator intent, inherited)

At the end of whole 17 the Cooperator decided on full Docker deployment on the VPS and stated he is a Docker newbie. Whole 18 delivered exactly that as **repository artifacts only**: one hardened Docker Compose topology, published at commit `996d9c7`, independently accepted (R4 + re-audit) with a passing disposable-Docker validator. The live host install was explicitly deferred and needs a separate Cooperator host grant.

This whole would execute and accept that live install on a real VPS: provisioning prerequisites, real secrets, DNS and TLS, firewall/SSH hardening, off-host backups, monitoring, and operational acceptance — with the same defensive-security standard as the rest of the project (`INFOSEC.md`, R5 host-hardening).

It does NOT re-open the published artifact except through a separate bounded correction if live evidence disproves a claim.

---

## 1. Standing product facts from the published artifact (VERIFY before citing)

```text
S1  Frontend: Next.js standalone in a separate container with `network_mode: service:nginx`,
    binding only `HOSTNAME=127.0.0.1 PORT=3000`, capability-free, no host port, no independent
    network attachment. Server-only provider credentials; nothing credential-bearing is client-visible.
S2  Backend: Django 5.2 + DRF + Channels (Daphne 4.2.3) serving only a Unix socket
    `/run/libretiles/backend.sock` with `socket 770 10001:10001`, started via
    `exec daphne --endpoint "unix:${socket}:mode=0770" --proxy-headers ...`. No Django TCP bind.
S3  Edge: nginx is the only host-published service — public 80/443 and private host-loopback
    `127.0.0.1:8443` for Django contrib admin. Master `0:10001` with exactly
    `NET_BIND_SERVICE`, `SETGID`, `SETUID`; request workers `10002:10001` with zero effective
    capabilities; every other service non-root and capability-free; `no-new-privileges`;
    read-only root filesystems; no Docker socket.
S4  Secrets: host sources `root:10004` mode `0440` inside an operator-controlled non-world-traversable
    directory; supplemental GID `10004` only on `postgres`, `backend-init`, `backend`, `frontend`,
    `db-tools`; least-scope per-service mounts; no Compose secret target uid/gid/mode; no value in
    image, rendered config, arguments, or logs. Real provisioning and rotation remain host work.
S5  TLS: Certbot HTTP-01 webroot inside Compose; fail-closed challenge-only bootstrap (no plaintext
    application traffic); full mode with canonical-host rejection on 443; port-80 redirect uses the
    literal validated DOMAIN (no request-host reflection); private admin loopback-only.
S6  Routes/streaming: public `/admin` is the Next staff console; `^~ /api/ai/` and
    `/api/admin/simulate/<id>/turn` disable proxy buffering for SSE; `/ws/` upgrades to Daphne;
    unmatched `/api` and `/static` fail closed on the public edge.
S7  Recovery: PostgreSQL 16 durable named volume; validated logical backup and disposable restore
    with migration-count comparison and negative guardrails; Redis non-durable.
S8  Validation truth: `scripts/validate_docker_deployment.sh` passed exit 0 on the published artifact
    (static guards plus disposable-Docker dynamic checks); the ten whole-17 documentation/dictionary
    guards are green.
S9  Known carried residuals (NOT this whole): whole-17 parity-oracle payload test red; two
    pre-existing frontend test reds (`i18n.test.ts` live-region count, `ReplayControls.test.ts`
    stale expectation). Owned by `codebase-hygiene-and-residual-reconciliation`.
```

---

## 2. What the live-host whole must decide and do (NOT accelerate blindly)

### 2.1 Host decisions owed before any install

```text
H1  Provider and host: which VPS, architecture, root/SSH access model, and who holds host authority.
H2  OS baseline and patch posture; disk encryption; swap; locality (EU?) and data-residency intent.
H3  DNS: exact domain and DNS control; who edits records; TTL plan; staging vs production.
H4  TLS: Certbot/Let's Encrypt HTTP-01 through the published Compose path, or an external terminating
    proxy. If external, the published stripping-proxy assumptions must be re-reviewed.
H5  Real secrets: creation method that never places values in shell history, Git, prompts, or logs;
    `root:10004 0440` sources; rotation procedure and its rehearsal.
H6  Off-host encrypted backups: destination, encryption keys, retention (for example 7 daily / 4
    weekly), restore rehearsal cadence, and who owns recovery.
H7  Monitoring and alerting: channel, certificate-expiry alerts, disk/CPU/memory, container health,
    backup success; acceptable downtime and maintenance windows.
H8  Resource sizing: CPU/memory/pids limits, Docker daemon log limits, autostart on boot, and
    image-digest update policy for the five pinned images.
H9  Whether to enable the optional `libretiles-openrouter-catalog-refresh` schedule. Separate
    production authority; not part of the install by default.
```

### 2.2 INFOSEC routing (mandatory posture for this whole)

```text
R5  Pre-deployment application audit is ALREADY done for the artifact (whole-18 R4 + re-audit).
    This whole needs the separate host-hardening audit (INFOSEC 4.9): read-only host inspection,
    deployment architecture, patch posture, reverse proxy/transport, exposure, service sandboxing,
    filesystem ownership, backup/restore evidence, monitoring, secret deployment, update/recovery.
R6  Corrections follow accepted-finding correction + fresh re-audit separation.
NO live SSH, firewall change, DNS change, certbot issuance, or container start on the host
    without an explicit Cooperator host grant (R5 live acceptance). Live acceptance is a
    Cooperator-owned result, not a Worker claim.
```

### 2.3 Deliverables of the whole (suggested slices — Orchestrator refines)

```text
D1  A live-host runbook derived from docs/vps_deployment_guide.md, with provider-specific exact
    commands and rollback, kept newbie-legible.
D2  Provisioning: OS prerequisites, Docker Engine + Compose + Buildx, service user/group (GID 10004),
    secret directory and files, firewall (only 80/443 public), SSH hardening, disk/timezone.
D3  First deployment: build/pull pinned images, first Certbot issuance, start services, verify
    exposure, routes, private admin SSH tunnel, websocket/SSE, and backup/restore rehearsal.
D4  Operations: renewal, monitoring/alerts, backup schedule with off-host copies, image update policy,
    restore rehearsal, maintenance/rollback drill.
D5  Host-hardening audit evidence + Cooperator live acceptance + closure record; any needed
    bounded repository corrections go through a separate correction grant.
```

---

## 3. Cooperator decisions owed (his, not yours)

```text
C1  Provider/host and who executes privileged host steps (independent of EU data-residency needs?). Cost: recurring VPS spend + his time.
C2  Exact domain + DNS control path. Cost: DNS propagation + a short issuance window.
C3  TLS route: published Certbot Compose path vs external proxy. Cost: external proxy adds a trust boundary and header-stripping review.
C4  Off-host backup destination + encryption + retention, and who holds the recovery keys. Cost: storage + key-loss risk.
C5  Monitoring/alert channel and who responds. Cost: a new external service or self-hosted stack.
C6  Acceptance window/maintenance allowance for first install and any restart.
C7  Whether to enable the optional catalog-refresh schedule. Cost: a scheduled external request under separate authority.
```

Present these as costed 2-4-option choices, cost stated first.

---

## 4. Terse-handling rules the fresh Orchestrator must obey (D-14)

```text
- A terse Cooperator reply (A, ano, ok, Pokracuj) CONTINUES the selected scope; it never selects a
  new whole or slice.
- Before beginning this whole (or any slice), emit a one-line SELECTION ECHO and act on the next reply.
- Present Cooperator-owned decisions as costed 2–4-option choices, cost stated first.
```

---

## 5. Standing quality gates (from AGENTS.md — the fresh Orchestrator re-verifies)

```text
Backend (from backend/, RF-16 env-cleared route):
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
Frontend (from frontend/):
  npm run typecheck
  npm run lint
  npm run build
Never ambient python/python3/poetry run. Never PYTHON_DOTENV_DISABLED=1.
Field-check every Worker prompt with:
  python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>
```

Repository corrections, if any, still run the disposable-Docker validator:
`./scripts/validate_docker_deployment.sh`.

---

## 6. Forward-horizon note (do NOT fold into this whole)

```text
This whole does NOT own: parity-oracle re-pin or the two frontend test reds (codebase-hygiene whole),
GitHub Actions CI/SBOM, nine-provider unfreeze, session-storage/CSP hardening, or UI/mobile polish.
Deployment of the published artifact is this whole; changing the published artifact is a separate
corrective grant with its own acceptance route.
```

---

## 7. Your exact first bounded step

```text
1. Inspect repository state at 996d9c7 (HEAD == origin/main, AP pin 9c5cc44, clean tree) and confirm
   the published commit is still the public refs/heads/main by direct readback.
2. Read .ap/AP.md (RF-01/RF-02/RF-03/RF-07/RF-12/RF-13/RF-16/RF-18), .ap/INFOSEC.md 4.8+4.9 and the
   host-hardening profile, AP_ORCHESTRATOR.md, AGENTS.md, the whole-18 closure record
   (meta/projects/libretiles/18/00-dockerized-vps-deployment/99_closure.md), and the published
   docs/vps_deployment_guide.md.
3. Verify S1–S8 against the live tree; correct any stale fact before issuing anything.
4. Present the Cooperator a SELECTION ECHO + the C1–C7 costed choices and the host-grant request.
   Do NOT begin any host or slice work until he selects this whole, answers the choices, and grants
   explicit host authority.
```

---

## Restoration Readiness Review

```text
Restoration Classification: PASS (forward-horizon handout)
Contradiction review: clean — this handout seeds a future whole; it does not contradict the closed
  whole-18 record at 996d9c7.
Omission review: clean — D-13 fields, D-14 rules, INFOSEC R5 posture, standing gates, and Cooperator
  decisions are present.
Stale-state review: honest — the published artifact exists; the live host state is prospective and
  unmeasured; this is flagged Known-stale-by-design (host state only).
Authority review: clean — grants NO authority; task authority comes from future Orchestrator prompts
  and a separate Cooperator host grant.
Active-mutation review: clean — no active mutation at closure commit 996d9c7.
Active-Worker review: clean — no Worker active.
Security-boundary review: clean — no secret, no live host, no public exposure in this handout.
Strategic-direction review: clean — aligned with the Cooperator's Docker-on-VPS intent.
Next-step executability review: clean — step 1 re-measures and waits for Cooperator selection.
```
