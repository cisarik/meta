# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, Dockerized VPS Deployment

Authored by the Agent Orchestrator at the closure of logical whole 17 (`public-docs-and-stale-truth`) at commit `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`, on 2026-09-09. Seeds ONE candidate logical whole: `dockerized-vps-deployment`. This is a FORWARD-HORIZON handout, not a live grant.

---

## Handout Integrity Record (D-13)

```text
Supersedes: none — this file is a NEW forward-horizon handout for a future whole.
Sections of other handouts that remain LIVE: none carried here (this whole is not open yet).
Coordinate review: honest; written against commit f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
  on 2026-09-09. Repository facts below were read from the whole-16/17 artifacts, not re-measured
  token-by-token in this session; mark file:line claims as hypothesis and re-measure before citing.
Enumeration fidelity: paraphrased from whole-16 closure record and whole-17 closure record;
  NOT quoted-exactly. Re-derive every file path before issuing any Worker prompt.
Numbers not re-measured: live Docker images, registry names, exact container memory/CPU limits,
  compose network topology. All are to be designed, not assumed.
Known-stale-by-design: whole-16 landed systemd+daphne+nginx non-Docker templates; this handout
  describes a DOCKERIZED replacement that does NOT exist in the tree yet. Do not cite these as
  current truth.
Predecessor whole: 17/00-public-docs-and-stale-truth CLOSED at f6ec9bf.
Baseline commit: f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 (origin/main aligned at closure).
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (detached HEAD at .ap, DO NOT upgrade).
```

---

You are a fresh Agent Orchestrator for Libre Tiles. This file grants you NO authority of any kind — not repository, implementation, deployment, production, account, filesystem, Git, browser, credential, provider, host, AP-upgrade, or closure authority. Verify repository and public truth independently before issuing any Worker prompt.

Your candidate logical whole identity: `dockerized-vps-deployment`

---

## 0. Why this whole exists (Cooperator decision, verbatim intent)

At the end of Whole 17 the Cooperator stated, in Slovak, that he has decided on **full Docker deployment on the VPS** and that he is a **newbie** to this. His exact requirements:
- Docker on the VPS, not the whole-16 systemd+daphne+nginx-process model.
- **INFOSEC-critical**: deployment must be reviewed to the same defensive-security standard as the rest of the project (the `.ap/INFOSEC.md` profile, risk-weighted routing R0–R6).
- He explicitly accepts that he is new to Docker: the eventual public documentation must stay readable for a non-Docker-expert operator AND for an LLM coding agent.

---

## 1. Standing product facts (inherited from 16/00 and 17/00 — VERIFY before citing)

```text
P1  Frontend: Next.js 16.3 (React 19), production build `output:"standalone"`, runs
    server.js on 127.0.0.1:3000 behind nginx. Nine AI providers, server-only credentials.
P2  Backend: Django 5.x + DRF + Channels (Daphne/ASGI), loopback 127.0.0.1:8000,
    PostgreSQL (prod) / SQLite (dev), Redis for Channels + shared throttle cache.
P3  Whole 16 landed non-Docker templates: backend/scripts/nginx/libretiles.conf,
    backend/scripts/systemd/libretiles-{backend,frontend}.service,
    scripts/vps_preflight.sh, scripts/vps_deploy.sh, docs/vps_deployment_guide.md.
    These remain the ONLY shipped deployment artifacts. NB: vps_preflight.sh pins
    python3.12/poetry2.3.2/node{20.19+,22.12+,24}/systemd checks; a Docker whole must
    reconcile or supersede these, not silently leave both true.
P4  golden hardening invariants (must hold in any containerized form):
    - Django binds loopback inside the container; nginx is the only public listener.
    - No 0.0.0.0 for Django. (Whole 17 froze this with static tests: any new
      documentation or config that reintroduces it will trip
      backend/tests/test_documentation_deployment_claims.py.)
    - Standalone frontend must run with HOSTNAME=127.0.0.1 PORT=3000 logic preserved
      wherever the runtime still reads env.
    - SECURE_PROXY_SSL_HEADER only behind a stripping TLS proxy; HSTS preload stays unset.
    - Credentials server-only, never in NEXT_PUBLIC_, never committed.
P5  Whole 17 now owns a static truth-guard: test_documentation_deployment_claims.py
    (8 guards) + test_documentation_dictionary_claims.py (2). Any deployment doc change
    that reassigns bind addresses or hosting names must keep these 10 green.
```

---

## 2. What the Dockerized whole must decide and build (NOT accelerate blindly)

### 2.1 Architecture questions to resolve BEFORE any host work

```text
Q1  One container vs n services: frontend + backend + nginx + postgres + redis + certbot.
    Recommend: separate images, one compose project, nginx as the single public edge.
Q2  Do NOT ship a database password in the image or in a committed compose/env file.
    Secrets: Docker secrets, a .env gitignored, or runtime env injection. Pick one and
    document it. INFOSEC 4.6 secret minimization applies.
Q3  Backup/restore for PostgreSQL volume: no container is durable without a documented
    volume + backup story. A newbie operator WILL lose data without this.
Q4  Nginx inside Docker terminating TLS (certbot sidecar with volume for certs) vs
    host nginx. Decision must preserve the whole-16 route split (Next owns /api/ai/*,
    /api/models, /api/prompts, /api/admin/simulate/<id>/turn, /admin; Django owns the
    rest of /api/ and /ws/; private admin loopback).
Q5  The private Django contrib-admin listener (whole 16 used 127.0.0.1:8443) — replicate
    or replace with a loopback-only container port. Public 443 must NOT expose /admin.
```

### 2.2 Deliverables of the whole (suggested slices — Orchestrator refines)

```text
D1  docker-compose.yml + per-service Dockerfiles (frontend standalone, backend ASGI,
    nginx TLS edge, postgres, redis), non-root users, no default creds, healthchecks.
D2  Secret + env strategy; .dockerignore; .env.docker.example (gitignored .env.docker).
D3  docs/docker_deployment_guide.md — newbie-legible, INFOSEC-annotated, and kept
    consistent with docs/vps_deployment_guide.md (which may be re-pointed or retired).
D4  Static guard extension: a test that forbids 0.0.0.0 / default credentials in the new
    Docker artifacts, matching the whole-17 guard style; 10 existing guards stay green.
D5  Optional CI-friendly image build check (no live host needed) — belongs here or in the
    github-actions-ci-and-sbom whole; decide.
```

---

## 3. INFOSEC routing (mandatory posture for this whole)

```text
R4  Broad milestone application audit at the deployment gate, plus
R5-subset  host/hardening review when a real host is named.
R1  Inline secure-implementation checks during each slice.
NO live host SSH, certbot issuance, UFW/tarn changes, or systemd reconfiguration without
  a separately authorized Cooperator host grant (INFOSEC R5 live acceptance).
The concrete choice: this whole produces container artifacts + documentation and static
  proofs. It does NOT own a live host install until the Cooperator grants one.
```

---

## 4. Cooperator decisions owed (his, not yours)

```text
C1  Confirm the non-Docker whole-16 systemd templates are to be SUPERSEDED by Docker
    (documented as such) vs kept as an alternative. Two live deployment directories
    contradict each other (D-15-style two owners); resolve explicitly.
C2  Confirm hosting provider / whether a real host grant exists now or later.
C3  Confirm he wants the private Django admin exposed at all, and how (loopback container
    port vs disabled entirely).
C4  Confirm the domain and whether TLS is certbot (Let's Encrypt) or external.
```

---

## 5. Terse-handling rules the fresh Orchestrator must obey (D-14)

```text
- A terse Cooperator reply (A, ano, ok, Pokracuj) CONTINUES the selected scope; it never
  selects a new whole or slice.
- Before beginning this whole (or any slice), emit a one-line SELECTION ECHO and act on the
  next reply.
- Present Cooperator-owned decisions as costed 2–4-option choices, cost stated first.
```

---

## 6. Standing quality gates (from AGENTS.md — the fresh Orchestrator re-verifies)

```text
Backend (from backend/, RF-16 env-cleared route):
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
Frontend (from frontend/):
  npm run typecheck
  npm run lint
Never ambient python/python3/poetry run. Never PYTHON_DOTENV_DISABLED=1.
Field-check every Worker prompt with:
  python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>
```

---

## 7. Forward-horizon note (do NOT fold into this whole)

```text
This whole does NOT own: parity-oracle re-pin (codebase-hygiene whole), GitHub Actions
CI/SBOM, nine-provider unfreeze, session-storage/CSP hardening, live-host R5 acceptance
(separate grant), or UI/mobile polish.
```

---

## 8. Your exact first bounded step

```text
1. Inspect repository state at f6ec9bf (HEAD == origin/main, AP pin 9c5cc44, clean tree).
2. Re-read .ap/AP.md RF-01/RF-02/RF-07/RF-12/RF-16/RF-18, .ap/INFOSEC.md 4.6+4.8,
   AP_ORCHESTRATOR.md, and AGENTS.md deployment sections.
3. Verify P1–P5 against the live tree; correct any stale fact before issuing anything.
4. Present the Cooperator a SELECTION ECHO + the C1–C4 costed choices. Do NOT begin D1
   until he selects this whole and answers C1–C4.
```

---

## Restoration Readiness Review

```text
Restoration Classification: PASS (forward-horizon handout)
Contradiction review: clean — this handout seeds a future whole; it does not contradict
  the closed whole-17 record.
Omission review: clean — D-13 fields, D-14 rules, INFOSEC posture, standing gates, and
  Cooperator decisions present.
Stale-state review: honest — whole-16 systemd templates are live; the Docker whole is
  prospective; this is flagged Known-stale-by-design.
Authority review: clean — grants NO authority; task authority from future Orchestrator prompts.
Active-mutation review: clean — no active mutation at closure commit f6ec9bf.
Active-Worker review: clean — no Worker active.
Security-boundary review: clean — no secret, no live host, no public exposure.
Strategic-direction review: clean — aligned with Cooperator Docker intent.
Next-step executability review: clean — step 1 re-measures and waits for Cooperator selection.
```
