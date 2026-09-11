You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task and stop. Your authority expires at your terminal report. A separately authorized fresh independent re-audit follows this exchange.

```text
Logical whole identity: proxied-axes-lockout-correction
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AXES-S1-IMPL — install django-axes[ipware], configure ipware for the nginx overwrite-model X-Forwarded-For topology, add a regression test proving two peers never share a lockout bucket. One commit. Closes audit-04-F01 / orch-05-D14 (medium in deployed topology).
Phase: Implementation
Implementation authority: explicit
Exact baseline: 91a57303b4e4dc05296be87e81be9bce50733d01
Independence required: no
Evidence posture: non-independent
Evidence tier: E3 (authN/authZ boundary touch; separate fresh re-audit follows)
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/backend/pyproject.toml
  /home/agile/Projects/libretiles/backend/config/settings.py
  /home/agile/Projects/libretiles/backend/tests/test_security_settings.py
```

## Background

Current state: nginx template overwrites `X-Forwarded-For` with `$remote_addr` (the real peer). `DJANGO_NUM_PROXIES=1` in `docker-compose.yml`. DRF throttles use the real peer via `_num_proxies()`. But axes (`settings.py:474`) still keys locked on `REMOTE_ADDR` (nginx's socket address = same for every request) because django-axes was installed WITHOUT the ipware extra. Behind nginx, every client shares the same lockout bucket → account-targeted DoS (medium, DEFECT_LEDGER.md:529-543).

The documented trap (DEFECT_LEDGER.md:488-508): installing the ipware extra alone changes nothing; setting precedence without proxy count leaves left-most in force; all three settings must be set together.

## Changes (apply in order)

**1. `backend/pyproject.toml`** — change line ~22:

```
django-axes = "==8.3.1"
→
django-axes = {version = "==8.3.1", extras = ["ipware"]}
```

Then: `poetry lock` + `poetry install` from `backend/`. Use the venv's poetry: `.venv/bin/poetry lock --no-update` then `.venv/bin/poetry install`. The existing lockfile may already contain django-ipware as a transitive; if so, network not needed for resolution. If a resolve is needed, one bounded PyPI request is authorized (no other web).

**2. `backend/config/settings.py`** — two edits:

a) Lines 108-111: update the outdated comment. Replace:
```python
    # django-axes independently keys on REMOTE_ADDR because ipware is not
    # installed. The two brakes must agree: if DRF trusted a client-supplied
    # header while axes used the socket address, a username spray would
    # bypass the unauthenticated throttle.
```
with:
```python
    # django-axes uses ipware (django-ipware) to read the real peer from
    # nginx's X-Forwarded-For overwrite. The two brakes now agree: both DRF
    # throttles and axes lockout key on the real peer IP when
    # DJANGO_NUM_PROXIES > 0.
```

b) After line 476 (`AXES_ENABLE_ADMIN = True`), add:
```python

# ipware reads the real peer through nginx's X-Forwarded-For overwrite model.
# nginx sets X-Forwarded-For to $remote_addr (single element). ipware
# right-most proxy order with count = DJANGO_NUM_PROXIES returns that element
# as the client IP. Must stay in sync: AXES_IPWARE_PROXY_COUNT == DJANGO_NUM_PROXIES.
# Note: DJANGO_NUM_PROXIES=0 (local dev, no proxy) means proxy count=0;
# ipware then falls back to REMOTE_ADDR — the socket address, which IS the
# real peer when no reverse proxy exists. The two setups are symmetric.
AXES_IPWARE_META_PRECEDENCE_ORDER = ("HTTP_X_FORWARDED_FOR", "REMOTE_ADDR")
AXES_IPWARE_PROXY_ORDER = "right-most"
AXES_IPWARE_PROXY_COUNT = _num_proxies()
```

**3. `backend/tests/test_security_settings.py`** — add one test function after the existing `test_axes_middleware_remains_last` (~line 842):

```python
def test_axes_ipware_returns_real_peer_in_proxied_topology() -> None:
    """Two proxied peers must not share a lockout bucket (gard-04-F01)."""
    from axes.helpers import get_client_ip_address
    from django.test import override_settings

    peer_a = "203.0.113.10"
    peer_b = "198.51.100.7"
    proxy_addr = "10.0.0.1"

    def _req(peer: str):
        return type("req", (), {
            "META": {
                "REMOTE_ADDR": proxy_addr,
                "HTTP_X_FORWARDED_FOR": peer,
            },
            "axes_locked_out": False,
        })()

    with override_settings(
        AXES_IPWARE_META_PRECEDENCE_ORDER=("HTTP_X_FORWARDED_FOR", "REMOTE_ADDR"),
        AXES_IPWARE_PROXY_ORDER="right-most",
        AXES_IPWARE_PROXY_COUNT=1,
    ):
        ip_a = get_client_ip_address(_req(peer_a))
        ip_b = get_client_ip_address(_req(peer_b))
        assert ip_a == peer_a, f"expected {peer_a}, got {ip_a}"
        assert ip_b == peer_b, f"expected {peer_b}, got {ip_b}"
        assert ip_a != ip_b, "different peers must not share a lockout bucket"
```

The `override_settings` forces the deployed topology (proxy count 1). In local dev (NUM_PROXIES=0), this test still passes because it overrides the settings explicitly.

## Work sequence

1. Repository gate: `91a57303b4e4dc05296be87e81be9bce50733d01`, AP `9c5cc44f`, clean, `main`.

2. **Pre-fix capture.** Run the NEW test (step 3's test body, placed in the file but with `import pytest; pytest.skip("ipware not yet installed")` or simply not committed yet — run it from a scratch file at `/tmp/opencode/axes-s1/prefix_test.py` using `backend/.venv/bin/python` with `DJANGO_SETTINGS_MODULE=config.settings` and `django.setup()` BEFORE the ipware install. It should fail with an AttributeError or return REMOTE_ADDR not the peer. Record.

3. Edit the three files. Run `poetry lock --no-update` and `poetry install`.

4. Run validation:
   - New test: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_security_settings.py::test_axes_ipware_returns_real_peer_in_proxied_topology -v` — must PASS
   - Existing axes test at line ~835 — must still PASS
   - Full backend pytest — must be green (1243+ passed), no NEW failures
   - mypy/ruff/makemigrations — clean

5. Commit + non-force push. Message: `fix(axes): install ipware and key lockout on real peer behind nginx`. Push. Verify `ls-remote`.

## Authority

```text
Filesystem: write the 3 allowlisted files. Temp: /tmp/opencode/axes-s1/.
Git: stage/commit/push non-force only.
Network: poetry lock resolution if needed (bounded PyPI); push + ls-remote. No other.
Secrets: none. Docker: none.
Dependencies: poetry lock + poetry install authorized.
```

## Stopping conditions

Stop if: the existing axes test breaks; any new pytest failure outside the new test; mypy/ruff/makemigrations fail; push fails; `IPWARE_INSTALLED` is still False after install; `get_client_ip_address` returns the proxy address instead of the peer.

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo:

```text
Logical whole identity: proxied-axes-lockout-correction
Worker session ordinal: 01, Worker exchange ordinal: 01
```

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS
Result artifact or commit: <pushed SHA> | not-applicable
Result evidence: <gates>
Logical-whole closure: not-closed
Changed files and purpose: pyproject.toml (ipware extra), settings.py (axes ipware config), test_security_settings.py (regression test)
Commit/push result: <sha, push, ls-remote>
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: none
Report justification: new-mutation
```

Then: pre-fix evidence, diff verbatim, validation table, an explicit `get_client_ip_address` probe (run from a scratch shell showing it returns the peer not the proxy), cleanup, deviations, authority expiry, context pressure.