### Report for ORCHESTRATOR_CHAT

Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 05, Worker exchange ordinal: 01.

Terminal status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: uncommitted candidate inventory digest `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900` at HEAD `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`; no commit was authorized or created
Result evidence: an independent fresh audit reproduced the candidate digest and allowlist, ran the exact candidate validator once (exit 0, `Docker deployment validation passed.`), built the five images independently under audit tags, and independently established nginx-only loopback exposure, exact nginx master `0x4c0` / zero-capability workers and services, socket `770 10001:10001`, `0:10004/0440` secret sources and targets with least-scope reads and denials, namespace sharing/non-sharing, TLS bootstrap/full-mode and admin split, forged-header overwrite, paired-recreation identity, backup/restore with all negative guardrails, and read-only filesystems; all project gates match the declared baseline except the whole-17 parity residual and the two declared frontend reds
Logical-whole closure: not-closed

## Repository, Candidate, Digest, And Allowlist Gate

- Repository root/Git directory: `/home/agile/Projects/libretiles`; `.git`; remote `https://github.com/cisarik/libretiles`; branch `main`.
- `HEAD` and `origin/main`: both `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`; AP `.ap` gitlink and checkout: both `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- Index clean (0 staged); 0 unmerged entries; no active Git operation, lock, rebase, merge, cherry-pick, or stash; `ap.project.conf` absent. `FETCH_HEAD`/`ORIG_HEAD` files exist as inert remnants; no operation is in progress.
- Buildx `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`; Docker server `29.7.2`; Compose `5.5.1`.
- Candidate inventory: exactly 45 status paths (14 `M`, 6 `D`, 25 `??`); no path outside the accepted 45-path candidate; the six deletions are exactly the superseded systemd/host-nginx/`vps_*` production owners; the `libretiles.conf` template and `test_vps_templates.py` remain deleted.
- Candidate inventory digest recomputed with the established ordered NUL-delimited `git status --porcelain=v1 --untracked-files=all` record plus present-content SHA-256 or literal `DELETED` marker method: `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900`. Exact match before and after every probe and gate; no canonical repository mutation occurred.
- Candidate secret scan over all present status paths: zero private-key/cloud/JWT-pattern hits; 51 `assigned_secret_16plus` pattern hits were all classified as named synthetic test constants, `your-*` placeholders in committed examples, or validator fixtures; example secret files contain `INVALID-REPLACE-ME`/`replace-me`/`example.invalid` only.

## Coverage Selection

Selected (approved attack-surface map): public edge exposure and routes, private admin, container identity/privilege, frontend/edge coupling, secret delivery, backend runtime/socket, TLS lifecycle, persistence/recovery, image supply chain, documentation/static-guard truth. Excluded: live deployment, host/R5 state, real credentials, real ACME/DNS, provider calls, dependency changes, whole-repository audit, and re-audit of the declared pre-existing baseline residuals.

## Audit Header

- Security task class: broad milestone application audit (INFOSEC R4), fresh independent.
- Owned/authorized target: the local Libre Tiles working tree at `/home/agile/Projects/libretiles`, candidate digest `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900` at HEAD `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`.
- Commit/candidate under audit: uncommitted working-tree candidate (same digest), no commit created.
- Scope: the exact 45-path uncommitted Docker production candidate and its directly claimed controls.
- Exclusions: pre-existing whole-17 parity residual; the two pre-existing frontend reds; host/hardening R5; live deployment, production, real credentials/ACME/DNS; provider calls; dependency changes; correction.
- Source records: no external standard is cited in a finding. Governance references are project-internal: `AGENTS.md`; AP semantic authority `.ap/AP.md` and `PROMPT_CONTRACTS.md`; activated profile `.ap/INFOSEC.md`; all at AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, status pinned to this audit, retrieved 2026-09-10. The prompt's internal `INFOSEC.md` source registry was not used as a requirement catalog and no time-sensitive external claim is made.
- Mutation/correction authority: none; no correction performed.

## Threat Model

- Assets: public availability, private administrative authority, Django/provider credentials, TLS private key, PostgreSQL data and backups, socket access control, image integrity, operator comprehension.
- Trust boundaries: internet to nginx; nginx to Next inside the shared network namespace; nginx to Daphne over the Unix socket; Next to Django callback; services to PostgreSQL/Redis; Certbot to ACME; operator to host secret sources and Compose; image build to runtime.
- Attacker-controlled inputs / local actor: public HTTP/TLS/websocket/SSE input; hostile forwarding headers; a compromised process inside any candidate container; operator configuration mistakes.
- Security properties relied on: nginx-only exposure; loopback-only admin; exact least capability; zero-capability workers/services; group-only socket/secret access; no world-readable secret/key; strict proxy-header overwrite; fail-closed bootstrap; immutable pins; durable rehearsed recovery.
- Abuse cases: direct database/cache/app exposure; public Django admin; forged proxy identity; fourth capability or root service; world-readable secret/key/socket; secret in image/config/log/argument; socket ownership bypass; namespace drift; ACME retry or expiry failure; destructive restore; contradictory documentation.

## Findings

Finding ID: DVP-AUDIT-05-F01
Title: Suspected websocket-edge regression on an undefined path (rejected)
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Affected component and exact location: `deploy/nginx/nginx.conf.template:185` (`location /ws/`) with `backend/game/routing.py:6` (only `^ws/game/(?P<game_id>[^/]+)/$` is routable)
Security property: preserved websocket upgrade behavior
Asset at risk: realtime multiplayer availability
Trust boundary: internet to nginx to Django over the Unix socket
Attacker-controlled input or local actor: unauthenticated HTTP Upgrade request
Reachability: public `443` `/ws/` request path
Preconditions: none
Required privileges: none
Observed or potential impact: an undefined `/ws/` path returns HTTP 500 with a Channels "No route found" traceback and ERROR log; the defined route answers at the application layer
C/I/A effect: no confidentiality/integrity/availability effect established; bounded log noise only
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: audit TLS edge `GET /ws/` returned `HTTP/1.1 500 Internal server error`; `GET /ws/game/123/` with and without `Origin: https://audit.local` returned `HTTP/1.1 403 Access denied` from the proxied Daphne application; backend log showed `ValueError: No route found for path 'ws/'.` plus a disconnect-time `ConnectionError` for a no-ticket handshake
Static evidence: only `backend/game/routing.py`'s `ws/game/<id>/` pattern exists; `GameConsumer.connect` closes before `accept` on missing/absent tickets (`WS_CLOSE_NO_TICKET`/`WS_CLOSE_INVALID_TICKET`); the nginx `/ws/` location forwards `Upgrade $http_upgrade` and `Connection $libretiles_connection_upgrade`
Synthetic containment: `/tmp/opencode/libretiles-audit-05-01`, owner this audit, mode `0700`, synthetic values only, removed
False-positive analysis: the behavior originates in Channels routing for an undefined path and in the consumer's baseline close-before-accept path; both files are unmodified by the candidate and no allowlisted path changes routing or consumers; the intended websocket route is proxied to Daphne and responds at the application layer, so no upgrade-path regression is established
Exploitability conclusion: not applicable
Smallest safe correction direction: optionally map an explicit closed response for undefined websocket paths in a separate hygiene task; out of this candidate
Regression-test requirement: not applicable
Residual risk: low-value error-log noise for undefined websocket paths; pre-existing and candidate-independent
Acceptance-blocking decision: non-blocking

Finding ID: DVP-AUDIT-05-F02
Title: Full-mode HTTP redirect reflects the request Host value
Status: open
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Affected component and exact location: `deploy/nginx/entrypoint.sh:54` (`return 301 https://$host$request_uri`) with the port-80 `default_server` in `deploy/nginx/nginx.conf.template:30-49`
Security property: canonical-host rejection / redirect-target integrity
Asset at risk: user trust in the operator's redirect
Trust boundary: internet to nginx over plaintext HTTP
Attacker-controlled input or local actor: the `Host` request header on host port 80
Reachability: public TCP 80 after TLS exists (full mode); bootstrap mode returns 503 and is unaffected
Preconditions: a certificate is present so the entrypoint renders the 301 fallback
Required privileges: none
Observed or potential impact: `Host: evil.local` on port 80 receives `Location: https://evil.local/some/path`; browsers derive `Host` from the URL authority, so redirection of a browser victim to an unrelated third-party domain was not established
C/I/A effect: no confidentiality/integrity/availability effect demonstrated
CWE mapping: CWE-601 (taxonomy signal only; usefulness depends on the unproven browser path)
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: independent full-mode audit edge: correct Host returned `301` with `Location: https://audit.local/some/path?q=1`; `Host: evil.local` returned `301` with `Location: https://evil.local/some/path`
Static evidence: the entrypoint substitutes `__HTTP_FALLBACK__` with `301 https://$host$request_uri`; the port-80 server is `default_server` and serves any well-formed Host; the `443` server separately enforces `if ($host != __DOMAIN__) return 444;` (independently observed as connection reset/`000`)
Synthetic containment: `/tmp/opencode/libretiles-audit-05-01`, owner this audit, mode `0700`, synthetic values only, removed
False-positive analysis: nginx constrains `$host` to a normalized valid hostname and rejects malformed Host headers, so header/CRLF injection is not possible; a browser sending an attacker-controlled `Host` is not a normal navigation mode; no cache-poisoning or cross-domain browser redirection path was established
Exploitability conclusion: plausible but unproven
Smallest safe correction direction: substitute the literal configured domain in the full-mode redirect instead of `$host` in a separately authorized template change
Regression-test requirement: a focused guard that a non-canonical Host on host port 80 in full mode redirects to the canonical domain
Residual risk: low; the TLS edge already rejects non-canonical hosts, and bootstrap fails closed
Acceptance-blocking decision: non-blocking

Finding ID: DVP-AUDIT-05-F03
Title: Validation helper runs as container root with CHOWN over synthetic secret sources (rejected)
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Affected component and exact location: `scripts/validate_docker_deployment.sh:279-302`
Security property: no unnecessary privilege in validation
Asset at risk: host files under the disposable audit root only
Trust boundary: container root/CHOWN to host bind source
Attacker-controlled input or local actor: local operator running the validator
Reachability: validation-only path, never part of a production service
Preconditions: a disposable audit root being provisioned
Required privileges: local operator
Observed or potential impact: none demonstrated; the helper modifies ownership/mode of synthetic fixtures only inside the audit root during a bounded `0701` window
C/I/A effect: none
CWE mapping: none
ASVS mapping: none
Source-standard references: none
Dynamic reproduction evidence: independent helper run emitted `CapPrm=CapEff=CapBnd 0000000000000001`, `CapAmb 0000000000000000`, `NoNewPrivs 1`, with `--network none --read-only --cap-drop ALL --cap-add CHOWN`; sources became `regular file 0:10004 440`; the helper was absent afterward and the directory was restored to `0700`
Static evidence: the helper mount is the single audit secrets directory; it is `--rm`; production secret provisioning is a separate R5 host operation
False-positive analysis: the helper exists only to reproduce the production host metadata contract locally, affects synthetic evidence only, and creates no production capability, account, or ownership; it does not weaken any accepted control
Exploitability conclusion: not applicable
Smallest safe correction direction: none required
Regression-test requirement: not applicable
Residual risk: none accepted; validation-time convenience only
Acceptance-blocking decision: non-blocking

## Independent Validator Assessment

- The exact candidate validator `scripts/validate_docker_deployment.sh` was run once, unmodified, from the repository root. Result: exit 0 and final line `Docker deployment validation passed.` with `VALIDATOR_EXIT=0`; under `set -euo pipefail` and the exit trap, reaching that line means every assertion passed.
- Independent inspection of all 590 lines found no tautological, self-referential, or always-true assertions. Assertions read real runtime state through `docker inspect`, `docker exec`, `stat`, `curl`, process `/proc` files, TCP probes, and Compose results; no assertion compares a value with itself and no assertion is conditioned on its own expected value. The synthetic secrets are created by the validator before use, which is standard fixture design, not circular verification.
- The only self-origin values are the declared synthetic fixtures (three source files, expected metadata `0:10004/0440`, domain `test.local`), which the validator then proves are absent from image history, rendered configuration, and logs; this is the intended evidence method.
- Weaknesses noted (none acceptance-blocking): the helper's `/proc` capability lines are printed but not asserted by the script (the independent helper run observed the expected `0x1`/`0`/`1` mask); the validator does not exercise canonical-Host rejection, TLS protocol versions, exact `/api`+`/api/`, private `/static`, websocket upgrades, or a non-canonical port-80 Host (all covered independently below); the final pytest-style count line is not part of its scope.
- The previously corrected defects were independently re-observed: socket `socket 770 10001:10001`; anchored worker probe returned exactly one worker (UID 10002/GID 10001/CapEff 0); paired recreation produced new container IDs while the recycled netns inode stayed identical (`net:[4026532749]`), confirming that container identity plus `NetworkMode` is the valid replacement signal.
- Assessment: the validator's PASS is supporting evidence only, consistent with the independent probes; it is not treated as independent proof.

## Independent Probe Evidence

Image build and supply chain (audit tags `libretiles-audit-05-01-a05-*`):

- Five images built from the exact working tree: backend `66fc3bf01988...`, frontend `922f8e3d6b86...`, nginx `2b5036c03b1c...`, certbot `cc5ac03503b4...`, postgres `fb51f20ad526...`.
- Runtime users: backend `10001:10001`; frontend `10003:10003`; nginx `0:10001`; certbot `10002:10001`; postgres `70:70`.
- `FROM` pins verified as exact version tags plus multi-architecture manifest-list digests with no `latest`: nginx `1.30.4-alpine3.24@sha256:dc5069ad...`, certbot `v5.8.0@sha256:f70ad0ad...`, node `24.21.0-bookworm-slim@sha256:2fe369e9...`, python `3.12.14-slim-bookworm@sha256:782412e8...`, postgres `16.15-alpine3.24@sha256:cf78e766...`; all five base images resolve locally to those exact digests.
- Image configs and full `docker history` scans for the declared synthetic values and API-key/token assignments: clean for all five; no secret is present in image environment or layers. The only grep noise was the literal filename `load-secrets.cjs` in the frontend `NODE_OPTIONS`, which is not a value.

Exposure and ports:

- Only `libretiles-audit-05-01-nginx-1` has `HostConfig.PortBindings`: `443/tcp→127.0.0.1:28443`, `444/tcp→127.0.0.1:28444`, `80/tcp→127.0.0.1:28080`; backend, backend-init, frontend, postgres, redis all report `{}`.
- Host `ss -ltn` shows only the three audit loopback listeners. Production defaults in the candidate bind `80/443` publicly and `127.0.0.1:8443` privately; loopback publication of all three was used only to keep the audit local.

Identities and capabilities (independent `/proc` and `docker inspect`):

- nginx master PID 1: `comm=nginx`, `uid=0 gid=10001 groups=10001`, `CapPrm=CapEff=CapBnd=00000000000004c0`, `CapAmb=0`; the certificate-watch child holds the same container capability set, constrained by the read-only rootfs.
- nginx worker: UID 10002, GID 10001, `CapEff=0`; worker can write all five `/var/cache/nginx/*` tmpfs paths (`770 10002:10001`) and is denied write on the master runtime tmpfs.
- frontend PID 1 `docker-init` and `next-server` PID 7: `10003:10003`, `CapEff=0`; runtime env `HOSTNAME=127.0.0.1 PORT=3000 NODE_ENV=production`.
- backend `daphne` PID 7: `10001:10001`, `CapEff=0`; postgres processes `70:70`, `CapEff=0`; redis `redis-server` `999:1000`, `CapEff=0`; certbot one-off `10002:10001`, `CapEff=0`, no GID 10004.
- All tested services: `ReadonlyRootfs=true`, `Privileged=false`, `CapDrop=["ALL"]`, `no-new-privileges:true`; nginx is the only service with `CapAdd` (`CAP_NET_BIND_SERVICE`, `CAP_SETGID`, `CAP_SETUID`).
- frontend low-port bind to port 80/445 denied; a normal high port bind succeeded.

Socket and secrets:

- Backend socket `socket 770 10001:10001`; containing directory `directory 770 10001:10001` (independently; the validator asserted the same); nginx sees the same socket and can stat it as `10002:10001`; frontend has no socket path and no socket volume.
- Secret sources: all three synthetic sources `regular file 0:10004 440`; targets independently `regular file 0:10004 440` for postgres/backend/frontend (and validator-asserted for backend-init/db-tools). Mounts are read-only binds (`RW=false`) to the exact per-service source.
- Intended reads succeed for postgres (`postgres_password`), backend (`django_secret_key`, `postgres_password`), frontend (`frontend_credentials`), backend-init, and db-tools. Unrelated secret paths are absent for every service that lacks them; redis/nginx/certbot have neither GID 10004 nor any application-secret path.
- Write attempts to read-only secret targets by backend and postgres, and a socket write attempt by the nginx worker, were denied.
- Rendered Compose config, container `inspect`, container logs, and per-process environments/cmdlines contained zero occurrences of the synthetic secret values (counts only; values never emitted).
- Missing-secret startup fails closed: a fresh `docker compose up -d postgres` with an absent source path exits 1 with `bind source path does not exist` (two occurrences) and creates no container.

Namespaces and coupling:

- nginx and frontend share `net:[4026532749]` before and after recreation; backend `net:[4026533198]`, postgres `net:[4026533128]`, redis `net:[4026533065]` are distinct; frontend `NetworkMode` resolves to the nginx container ID.
- frontend and nginx cannot reach `postgres:5432` by IP; frontend has no PostgreSQL/Redis network membership and no backend socket.
- Paired `up -d --force-recreate nginx frontend` replaced both containers (distinct IDs), preserved the shared namespace, resolved `NetworkMode` to the new nginx ID, and both services returned healthy with catalog/root 200 afterward.

Routes, admin, TLS, proxy:

- Bootstrap: `/healthz` 200, plaintext application 503, `nginx -t` gated config; full mode: pre-frontend `502` only, then frontend 200.
- Public TLS edge (`audit.local:28443`): `/` 200, `/api/catalog/models/` 200, `/api/models` 200, `/api/prompts` 200, `/api/admin/` 404 (Django no-route), `/api/game/unknown/` 401, `/api/auth/me/` 401, `/api/unknown/` 404, `/api` 404, `/api/` 404, `/static/admin/css/base.css` 404, `/admin` 200 (Next staff console), `/admin/` 308 (Next), simulate-turn 405 (Next).
- Canonical-host rejection: `Host: evil.local` (including a forged `Host` over a valid SNI connection) closed with `000` (nginx 444); forged `X-Forwarded-Proto: http`, `X-Forwarded-For`, `Forwarded`, and `X-Real-IP` still returned 200 on the catalog route, demonstrating nginx overwrite; `Server: nginx` carries no version.
- Private admin listener (`audit.local:28444`): `/admin/` 302 (Django login), `/static/admin/css/base.css` 200 from collected files, `/api/game/x/` 404, `/` 404, `/admin` 301.
- Callback listener from the frontend network namespace (`127.0.0.1:8001`): `/api/catalog/models/` 200, `/api/auth/me/` 401, `/api/ai/move` 404, `/admin/` 404, `/` 404.
- TLS: `ssl_protocols TLSv1.2 TLSv1.3`; TLSv1.2 and TLSv1.3 handshakes succeeded (TLSv1.3 via `-brief`); TLSv1.1/TLSv1.0 could not be negotiated because the audit host's OpenSSL 3.6.4 client offers no legacy protocols (client limitation, static config is the evidence).
- Certificate material: links `777 10002:10001` to targets `640 10002:10001`; directories `750 10002:10001`; issue-style and renewal-style reload markers were consumed by nginx through group access.
- Websocket and SSE: the defined `/ws/game/<id>/` route reached Daphne and returned an application-level 403 for unauthorized handshakes; an undefined `/ws/` path returned a Channels 500 (F01). `/api/ai/move` GET 405 and POST 200 reached the Next SSE route; `proxy_buffering off`/`proxy_request_buffering off`/`gzip off` and 660s read/send timeouts are present for the SSE locations.

Persistence and recovery:

- `db-tools backup audit05.dump` and `verify` exited 0; the file is `regular file 70:70 600` inside `directory 70:70 700` `/backups`.
- Disposable restore into a fresh `restore-postgres` succeeded: `restore completed into disposable target: audit05.dump`; migration counts `source=73 restore=73`.
- Negative guardrails: duplicate destination exit 1; traversal-style name exit 2; missing `--confirm-disposable` exit 2; missing `RESTORE_DISPOSABLE=1` exit 1; restore target host equal to source exit 1; restore into a non-empty target exit 1.
- Read-only root filesystem verified for postgres, redis, backend, nginx, frontend; postgres data volume is a named durable volume; Redis runs `--save "" --appendonly no` on tmpfs.

## Project Gates

Backend from `backend/` using the env-cleared `.venv/bin/...` route:

- `mypy config game gamecore accounts catalog`: PASS, `Success: no issues found in 119 source files`.
- `ruff check .`: PASS, `All checks passed!`.
- `makemigrations --check --dry-run`: PASS, `No changes detected`.
- `pytest -q`: `1 failed, 1241 passed, 27 skipped` (counts independently derived from the 1269 progress markers because the captured log's final count line was not emitted). Sole failure: `tests/test_word_authority_parity.py::PersistedPayloadParityTests::test_human_persisted_move_payload_matches_the_pinned_baseline`, with a strictly additive `inspection` block versus the pinned baseline — the exact whole-17 accepted residual.

Frontend from `frontend/`:

- `npm run typecheck`: PASS. `npm run lint`: PASS. `npm run build`: PASS (Next build completed; all routes emitted).
- `npm test`: `2 failed, 718 passed, 3 skipped` — exactly the two declared pre-existing reds in non-allowlisted files: `src/lib/i18n/i18n.test.ts` (expected 1 `aria-live`, measured 3) and `src/components/admin/ReplayControls.test.ts` (stale expected text). Independence re-checked: `aria-live` occurs in committed `LiveAnnouncer.tsx`, `ReplayControls.tsx`, and `SimulationArena.tsx`; no candidate path overlaps either red-test file.
- Focused candidate guards `tests/test_docker_deployment.py` + `tests/test_documentation_deployment_claims.py`: 28 passed; the whole-17 documentation/dictionary guards are green inside the full run.

The residuals above are restated, not re-labelled; this Worker does not accept or close them.

## Containment Ledger

- Declared root `/tmp/libretiles-audit-05-01`: unavailable to this session because the client permission policy denies writes outside its allowed roots; deviation recorded below.
- Temporary root `/tmp/opencode/libretiles-audit-05-01`: owner this audit, mode `0700`, synthetic fixtures only, cleanup owner this audit; used for two declared probe windows; removed (`rm -rf` exit 0; path absent).
- Exact validator internal temporary root `/tmp/libretiles-docker-impl-01`: created and removed by the candidate validator's own trap; independently verified absent; no retained artifacts.
- Exact validator Compose project `libretiles-dvp-impl-01` and image prefix `libretiles-dvp-impl-01-`: transient validator-owned identities; independently verified zero containers, networks, volumes, and images afterward.
- Audit Compose project `libretiles-audit-05-01`, image prefix `libretiles-audit-05-01-`, volumes certified after `down --volumes --remove-orphans`: zero containers, networks, volumes, images.
- Missing-secret probe project `libretiles-audit-05-01-miss`: created only for the fail-closed check; zero containers, networks, volumes after cleanup.
- Helper container `libretiles-audit-05-01-secret-helper`: `--rm`, `--network none`, `--read-only`, `--cap-drop ALL --cap-add CHOWN`, `no-new-privileges`, single-directory bind, CHOWN-only mask `0x1`; absent after use.
- Synthetic secret sources: `django`, `postgres`, `frontend.json` as `0:10004 0440` inside the audit root; deleted with the root; values never emitted.
- Diagnostic one-off containers (`certbot-run-*`, `db-tools-run-*`, `backend-init-run-*`, `restore-postgres-1`): all removed by the exact cleanup.
- Retained as authorized: shared official base-image layers and BuildKit/package caches. Untouched: pre-existing `libretiles-postgres-1` (`4091e825c32f`), `libretiles-redis-1` (`9039e197c971`), `recursing_engelbart` (`5362d3e0e06c`), `pochop-dev` (`e191c6cf8421`), volume `libretiles_pgdata`, anonymous volume `bd4e7383892e...`, networks `libretiles_default`, `pochop-private_default`, `bridge`, `host`, `none`; verified by ID before and after.
- Network endpoint classes observed: Docker Hub official registry/CDN and local caches only; the audit build used warm cached layers; no provider, catalog, ACME, DNS, VPS, SSH, browser, or host-service endpoint was contacted. No packet-level accounting is claimed.

## Limitations And Unverifiable Items

- Declared audit root `/tmp/libretiles-audit-05-01` was rejected by the client permission policy; the equivalent audit-owned root `/tmp/opencode/libretiles-audit-05-01` (`0700`, synthetic, cleaned) was used. Docker identities remain the declared `libretiles-audit-05-01`.
- The exact validator's temporary root, Compose project, and image prefix are hardcoded in the candidate script (`libretiles-dvp-impl-01`, `/tmp/libretiles-docker-impl-01`); the run therefore used those internal identities rather than the audit project name. Everything was transient and verified clean; no candidate file was modified.
- TLSv1.1/TLSv1.0 rejection is not dynamically proven because the audit host's OpenSSL 3.6.4 client offers no legacy protocols; the server's `ssl_protocols TLSv1.2 TLSv1.3;` is established-static.
- A websocket `101 Switching Protocols` was not demonstrated end-to-end because no synthetic authenticated ticket/game state was created; the defined route was proven to reach Daphne (application-level 403), with static upgrade-header evidence.
- `X-Forwarded-For`/`Forwarded` overwrite was proven indirectly through the `X-Forwarded-Proto` overwrite effect; no endpoint echoes the client-IP value.
- `exec daphne` signal semantics and graceful shutdown were verified statically and through restart/recreation health, not through a dedicated stop/signal rehearsal.
- Secret host provisioning (`0:10004/0440` under a root-owned `0700` directory) is an R5 host operation; the audit reproduced the metadata contract with a bounded synthetic helper, not with real host state.
- The captured backend pytest log did not include the terminal count line; the `1241 passed / 1 failed / 27 skipped` counts were derived from the run's 1269 progress markers and match the declared baseline exactly.
- The two frontend reds and the whole-17 parity residual remain open by design and were not re-audited as candidate findings.

## Residual-Risk Summary

- No `medium` or higher finding; no acceptance-blocking finding; the fixed control matrix passes on the exact candidate.
- DVP-AUDIT-05-F02 (`info`, open): the port-80 full-mode redirect reflects the request Host. Non-blocking; Orchestrator may accept as documented residual or route a one-line hygiene correction plus a focused test.
- DVP-AUDIT-05-F01 and DVP-AUDIT-05-F03: rejected false positives; no residual action required.
- Pre-existing baseline residuals carried forward unchanged: whole-17 parity-oracle backend test red; `i18n.test.ts` live-region count red; `ReplayControls.test.ts` stale expectation red.
- Deferred by scope: R5 host hardening, real ACME/DNS/TLS issuance, off-host backup storage, monitoring/alerts, and the optional catalog-refresh schedule.

## Out-Of-Scope Observations (Ledger Candidates)

- `X-Powered-By: Next.js` is present on public responses; `server_tokens off` already suppresses the nginx version. Informational; Next default.
- Undefined websocket paths return 500 with an ERROR traceback (DVP-AUDIT-05-F01); no-ticket handshakes log a disconnect-time `ConnectionError`. Baseline behavior in unmodified files.
- The nginx certificate watcher retries a failing `nginx -t` every 5 seconds while the reload marker persists; operational noise consideration only.
- The port-80 `$host` redirect reflection (DVP-AUDIT-05-F02) if the Orchestrator prefers not to accept it as residual.
- Pre-existing unrelated `libretiles-postgres-1`, `libretiles-redis-1`, and `libretiles_pgdata` objects are not part of this candidate and were explicitly not inspected beyond identity preservation.

## Smallest Next Step

The Orchestrator should record the R4 outcome as `acceptance-PASS` for digest `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900`, decide DVP-AUDIT-05-F02 as accepted residual or as a separately authorized one-line template hygiene correction with its regression test, and leave the declared whole-17/frontend baseline residuals to their existing disposition. No candidate correction is required for acceptance.

Report justification: new-evidence

Authority expiry: audit authority expires when this report is written; no correction, acceptance disposition beyond the reported verdict, Git write, publication, deployment, production, or closure authority remains.
