## Plan: Report for DVP-IMPL-04-F01 (Session 02, Exchange 01)

### Baseline
- HEAD: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
- Branch: `main`
- AP gitlink: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Classification: `accepted-continuation`

### Finding
**DVP-IMPL-04-F01**: nginx container failed binding port 80 because non-root process (UID 10002) had zero effective capabilities despite having `NET_BIND_SERVICE` in bounding set, due to `no-new-privileges` + `cap_drop ALL`.

### Correction Applied
nginx master process runs as root (UID 0) inside container for effective `NET_BIND_SERVICE`; request workers drop to unprivileged `edge` identity (UID 10002/GID 10001) via nginx `user` directive.

### Files Modified
| File | Change |
|------|--------|
| `deploy/nginx/Dockerfile` | Added `USER 0:0` before ENTRYPOINT for master process |
| `deploy/nginx/nginx.conf.template` | Added `user edge libretiles;` directive for worker processes |
| `docker-compose.yml` | Removed `user: "10002:10001"` from nginx service, added master/worker exception comment, fixed tmpfs mode |
| `deploy/nginx/entrypoint.sh` | No changes needed (works correctly as root) |
| `backend/tests/test_docker_deployment.py` | Updated non-root check to exempt nginx; added `test_nginx_master_worker_split` test |
| `scripts/validate_docker_deployment.sh` | Updated static/dynamic checks for master/worker split |
| `AGENTS.md` | Added nginx master/worker exception bullet under Deployment |
| `docs/architecture.md` | Updated Production/Edge bullet with master/worker split description |

### Test Results (focused static)
- `test_docker_deployment.py`: 74/74 pass
- `test_documentation_deployment_claims.py`: pass
- `test_security_settings.py`: pass
- mypy: clean
- ruff: clean
- makemigrations --check --dry-run: clean

### Open Issue
Docker validation failed at runtime: entrypoint `chown` on `/tmp/client-body` etc. fails because `cap_drop: ALL` removes `CAP_CHOWN`.

**Fix required**: Pre-create temp directories in `deploy/nginx/Dockerfile` during build (full root), not at runtime. Add to existing RUN:
```
/tmp/client-body /tmp/proxy /tmp/fastcgi /tmp/uwsgi /tmp/scgi
```
with `chown 10002:10001` on those paths. Then revert entrypoint to simple version (no runtime chown).

### Next Steps (for Orchestrator)
1. Edit `deploy/nginx/Dockerfile` — add temp dir pre-creation with chown
2. Verify `deploy/nginx/entrypoint.sh` is reverted (no runtime chown)
3. Re-run `./scripts/validate_docker_deployment.sh`
4. If Docker passes → run full project gates (pytest, mypy, ruff, frontend typecheck/lint/test/build)
5. Write final report to `/tmp/opencode/libretiles-worker-dispatch/02_report_00.md`