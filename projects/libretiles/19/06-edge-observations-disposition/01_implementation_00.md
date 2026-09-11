You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task.

```text
Logical whole identity: edge-observations-disposition
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: EDGE-S1-IMPL — suppress X-Powered-By header on public responses (one nginx template line + two static guards). One commit. Closes L1.
Phase: Implementation
Implementation authority: explicit
Exact baseline: 75f18773f5936517652640503c3b7b5e69e3cb28
Independence required: no
Evidence posture: non-independent
Evidence tier: E1
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/deploy/nginx/nginx.conf.template
  /home/agile/Projects/libretiles/backend/tests/test_docker_deployment.py
  /home/agile/Projects/libretiles/scripts/validate_docker_deployment.sh
```

## Changes

**1. `deploy/nginx/nginx.conf.template`** — add one line in the `http` block, right after `server_tokens off;` (currently line 12):

```
    proxy_hide_header X-Powered-By;
```

This suppresses the `X-Powered-By: Next.js` response header that Next.js standalone emits on every proxied response. It applies to all `proxy_pass` locations (both frontend 127.0.0.1:3000 and backend Unix socket).

**2. `backend/tests/test_docker_deployment.py`** — add a test function verifying the template contains the suppression directive:

```python
def test_nginx_template_suppresses_nextjs_powered_by_header() -> None:
    template = (REPO_ROOT / "deploy/nginx/nginx.conf.template").read_text()
    assert "proxy_hide_header X-Powered-By;" in template, (
        "nginx template must suppress X-Powered-By to avoid "
        "leaking Next.js version on public responses"
    )
```

Place this after the existing template-reading tests. Use the `REPO_ROOT` pattern already established in the file (find one reference and follow it).

**3. `scripts/validate_docker_deployment.sh`** — add one assertion. Find the section with `echo` header-text + assertion lines pattern used elsewhere in the script. Add:

```bash
# L1: suppressed X-Powered-By
if grep -q 'proxy_hide_header X-Powered-By;' deploy/nginx/nginx.conf.template; then
    echo "PASS  nginx template hides X-Powered-By"
else
    echo "FAIL  nginx template must suppress X-Powered-By header" >&2
    status=1
fi
```

## Work sequence

1. Repo gate: `75f18773f5936517652640503c3b7b5e69e3cb28`, AP `9c5cc44f`, clean, `main`.
2. Edit 3 files. `git diff --stat` — 3 files only.
3. Validation:
   - `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py -q` from `backend/` — all must pass
   - `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest -q` (full backend) — green
   - `npm run typecheck && npm run lint && npm run build` from `frontend/` — clean
4. Commit + push: `fix(deploy): suppress Next.js X-Powered-By header on public nginx responses`. `ls-remote` matches.

## Authority

```text
Filesystem: 3 allowlisted files. Temp: /tmp/opencode/edge-s1/.
Git: stage/commit/push non-force. Network: push + ls-remote. No deps, no Docker.
```

## Report contract

`### Report for ORCHESTRATOR_CHAT`. Echo: Logical whole identity: edge-observations-disposition, Worker session ordinal: 01, Worker exchange ordinal: 01. status PASS, Phase-qualified result: implementation-PASS, commit, gates, Report justification: new-mutation, authority expiry.