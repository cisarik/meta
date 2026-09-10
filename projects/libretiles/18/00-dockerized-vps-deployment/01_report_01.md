 | Attached only to `edge_egress_net`; owns the shared namespace | Public 80/443, private host-loopback 8443 mapping, loopback callback 8001, loopback Next 3000 |
| `frontend` | `network_mode: service:nginx`; no `networks`, `ports`, `expose`, or Compose hostname | Next binds only `127.0.0.1:3000` |
| `certbot` | Separate `acme_egress_net` | ACME outbound; challenge/certificate sharing occurs through volumes |
| `backend` | Existing isolated data/cache/backend-egress networks | Nginx reaches it only through the shared Unix-socket volume |
| `postgres` | `data_net` only | No nginx/frontend membership |
| `redis` | `cache_net` only | No nginx/frontend membership |

`app_net` and `frontend_egress` from DVP-PLAN-01 are removed. Frontend inherits `edge_egress_net` through nginx’s namespace, which supplies provider egress. Certbot does not need that namespace and remains on a separate outbound network.

Nginx must not join `data_net`, `cache_net`, or `backend_egress`. Network-namespace sharing does not share nginx’s backend-socket mount with frontend, so frontend cannot directly open the Django socket.

## Port Hardening

Sharing nginx’s namespace creates a port-race risk if compromised frontend code can bind an nginx port while nginx is unavailable. Use privileged container ports for host-facing nginx listeners:

| Host | Container namespace | Purpose |
|---|---|---|
| `0.0.0.0:80` | `80` | HTTP redirect and ACME challenge |
| `0.0.0.0:443` | `443` | Public TLS |
| `127.0.0.1:8443` | `444` | Private Django-admin TLS |
| none | `127.0.0.1:8001` | Next-to-Django callback |
| none | `127.0.0.1:3000` | Next standalone |

Set `net.ipv4.ip_unprivileged_port_start=1024` on nginx, drop all capabilities from both services, then add only `NET_BIND_SERVICE` to nginx. Frontend retains no capabilities and cannot bind ports 80, 443, or 444. Both retain `no-new-privileges`.

This narrowly replaces DVP-PLAN-01’s capability-free high-port nginx design. Callback port 8001 remains unprivileged because its exact loopback URL is frozen; it is not host-published.

## Startup And Health

Dependency direction is one-way:

```text
nginx healthy -> frontend starts
```

Frontend uses both the namespace reference and:

```yaml
depends_on:
  nginx:
    condition: service_healthy
```

Nginx must not depend on frontend. Its configuration can load while port 3000 is absent because the upstream is loopback, not a startup-resolved service name.

Expected startup behavior:

1. Nginx starts in TLS bootstrap or full mode.
2. Its own static health endpoint becomes healthy without contacting frontend.
3. Frontend starts in nginx’s namespace.
4. Frontend health probes `http://127.0.0.1:3000`.
5. Next-owned routes may return temporary 502 between steps 2 and 4.
6. Backend routes independently recover when the Django socket appears.

Nginx health must prove nginx only. Frontend health must prove Next separately. A frontend crash therefore leaves nginx healthy but Next routes at 502 while Compose restarts frontend; monitoring must evaluate both services.

Certbot issuance/renewal still depends on nginx’s static challenge health, not frontend health, preventing an application-startup/TLS deadlock.

## Restart And Recreate Contract

- Ordinary nginx process reloads preserve the shared namespace and are preferred for certificate renewal.
- Restart-policy recovery of the same nginx container is expected to preserve the service relationship, but must be dynamically verified.
- Recreating or replacing nginx can create a new namespace while the existing frontend remains attached to the old one.
- Every nginx container recreation must therefore recreate frontend in the same Compose operation.
- Deployment documentation and scripts must forbid nginx-only `--force-recreate`, `up --no-deps nginx`, and equivalent update procedures.
- The supported update operation names both services and verifies namespace equality afterward.
- Compose `restart` does not restart dependents; it must not be presented as sufficient after nginx image/configuration replacement.
- Failure to prove paired recreation and recovery during Docker validation stops implementation.

## Security Trade-Off

Compared with DVP-PLAN-01, nginx and frontend now share:

- Loopback listeners
- Network interfaces and routing
- Provider-capable outbound reachability
- Access to nginx callback and private-admin listeners

They do not share:

- Filesystems or secret mounts
- PID namespaces
- Users or process capabilities
- Backend socket mounts
- PostgreSQL/Redis networks
- Certificate-write authority

A compromised frontend can connect to nginx’s private-admin listener and callback listener, but still lacks Django admin credentials and cannot bypass Django authentication or CSRF. It can also consume shared outbound/network resources or interfere with unprivileged loopback port 8001. These are residual costs of preserving the loopback contract.

The low-port/capability design prevents frontend takeover of host-published public/private listeners if nginx stops. Dynamic validation must prove the frontend process lacks effective `NET_BIND_SERVICE`.

## Alternatives

| Alternative | Cost/reason rejected |
|---|---|
| Combine Next and nginx in one container | Removes namespace lifecycle coupling but also combines filesystems, lifecycle, users, secrets, and process supervision; contradicts separate-service design. |
| Change Next to a container-interface bind | Simpler bridge networking but violates the accepted loopback runtime contract. |
| Add a TCP relay sidecar while Next remains isolated on loopback | Requires another shared namespace or relay mechanism, adds a service and trust boundary, and offers no isolation benefit over sharing nginx’s namespace. |

The proposed topology is therefore the smallest valid option preserving all selected invariants.

## Directly Affected Plan Areas

| Prior slice | Revision |
|---|---|
| Runtime images | Frontend final command and environment must enforce `HOSTNAME=127.0.0.1 PORT=3000`; its healthcheck targets loopback. |
| Compose platform | Add namespace sharing and one-way dependency; remove frontend/app networks; give nginx only the edge network and one narrowly scoped capability. |
| Nginx configuration | Restore frontend upstream and callback to loopback; use ports 80, 443, and 444 plus callback 8001. |
| Static truth guards | Assert exact namespace, environment, command, network, capability, sysctl, dependency, and loopback proxy invariants. |
| Docker harness | Prove namespace equality, listener isolation, paired recreation, health independence, and recovery from temporary 502. |
| Documentation | Preserve frontend loopback wording and document paired nginx/frontend recreation. |

Directly affected implementation paths:

```text
docker-compose.yml
frontend/Dockerfile
frontend/docker/healthcheck.cjs
deploy/nginx/Dockerfile
deploy/nginx/nginx.conf.template
deploy/nginx/entrypoint.sh
backend/tests/test_docker_deployment.py
scripts/validate_docker_deployment.sh
AGENTS.md
README.md
CONTRIBUTING.md
libretiles_PRD.md
docs/architecture.md
docs/vps_deployment_guide.md
backend/tests/test_documentation_deployment_claims.py
```

The remaining DVP-PLAN-01 allowlist and decisions are unchanged.

## Revised Stop Conditions

Stop implementation if any of these occurs:

- Compose rejects the service namespace reference or explicit dependency combination.
- Frontend receives a separate network endpoint or host port.
- Next does not bind exactly to loopback.
- Nginx gains database/cache network membership.
- Frontend can access the backend Unix socket.
- Nginx requires frontend readiness to start or serve ACME challenges.
- Paired nginx/frontend recreation does not re-establish one namespace.
- Restart-policy behavior strands either service.
- Frontend can bind a protected low port.
- Nginx cannot run non-root with only `NET_BIND_SERVICE`.
- Callback routing or forwarding-header overwrite changes.
- A proposed recovery requires changing the loopback invariant.

## Validation Changes

Static Compose/config checks must assert:

- `frontend.network_mode == "service:nginx"`.
- Frontend has no `networks`, `ports`, `expose`, or Compose `hostname`.
- Frontend environment and command both force `HOSTNAME=127.0.0.1` and `PORT=3000`.
- Frontend depends on healthy nginx.
- Nginx does not depend on frontend.
- Nginx belongs only to `edge_egress_net`.
- Nginx has `cap_drop: [ALL]`, only `cap_add: [NET_BIND_SERVICE]`, and the unprivileged-port sysctl.
- Frontend drops all capabilities and adds none.
- Only nginx publishes ports.
- Public/private mappings target nginx ports 80, 443, and 444.
- Nginx proxies Next and callback traffic through loopback.
- Nginx has no PostgreSQL/Redis network or TCP upstream.
- Certbot uses only its separate ACME egress network.

Docker smoke checks must prove:

1. Nginx starts and becomes healthy without frontend.
2. A Next-owned route returns bounded 502 before frontend starts.
3. Frontend starts only after nginx health and becomes healthy on loopback.
4. The route recovers through nginx without a frontend host port.
5. `docker inspect` shows frontend network mode resolving to nginx’s container.
6. `/proc/1/ns/net` identity matches between nginx and frontend but differs from backend and Certbot.
7. Frontend has no independent Docker network attachment.
8. Nginx/frontend cannot reach PostgreSQL or Redis network addresses.
9. Frontend cannot see or open the backend socket path.
10. Frontend cannot bind an unused port below 1024.
11. Nginx has only effective bind-service capability.
12. Certbot reaches the ACME challenge volume without sharing nginx’s namespace.
13. Paired nginx/frontend recreation produces a new shared namespace and restores routes.
14. Certificate-triggered `nginx -s reload` leaves frontend healthy in the same namespace.
15. No host port 3000, 8000, 8001, 5432, or 6379 is created.

No live provider or external ACME call is needed for these tests.

## INFOSEC Boundary

Security route remains R1 implementation review followed by fresh independent R4 broad milestone audit; R5 host review remains deferred.

New material risks:

- Shared network reachability between public edge and provider-facing Next.
- Namespace donor recreation can strand frontend.
- Frontend can reach callback/private-admin listeners.
- Nginx now needs one capability.
- Frontend and nginx share egress capacity and network-level availability.

Mitigations:

- No data/cache network membership.
- Backend reachable only through an nginx-only socket mount.
- Separate filesystems, secrets, PID namespaces, users, and capability sets.
- Low protected edge ports plus explicit unprivileged-port sysctl.
- Paired-recreation contract and dynamic namespace proof.
- Exact callback allowlist and forwarding-header overwrite.
- Independent service health and bounded 502 behavior.

Residual R5 concerns include host firewall enforcement, Docker daemon authority, egress monitoring, namespace behavior under the deployed Docker/Compose versions, and operational compliance with paired recreation.

## Deviations And Missing Evidence

- No Docker/Compose command was authorized, so namespace, capability, restart, and recreate behavior remains planned implementation evidence.
- No tests were run.
- No files changed.
- No second revision remains available automatically.
- The changed topology adds the narrowly scoped nginx capability described above; this is required to prevent a shared-namespace frontend from racing host-published listeners.

Smallest next step: accept this targeted revision and issue one complete current-session implementation prompt using the unchanged baseline and DVP-PLAN-01 allowlist, with these revised frontend/nginx invariants made mandatory.

Report justification: new-material-risk

Authority expiry: the sole targeted planning revision expired at submission of this report; no implementation, further planning revision, acceptance, publication, deployment, production, or closure authority remains.
