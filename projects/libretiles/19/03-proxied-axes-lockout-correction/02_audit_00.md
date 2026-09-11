You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded READ-ONLY independent re-audit and stop. You did NOT implement the correction and you may NOT correct anything.

```text
Logical whole identity: proxied-axes-lockout-correction
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Security task class: fresh independent re-audit
Task identity: AXES-RAUDIT-01 — independently re-audit commit 75f1877 against the original risk claim audit-04-F01 / orch-05-D14. Verdicts: verified-closed or not accepted per finding, with evidence.
Phase: Independent Audit
Exact baseline: 75f18773f5936517652640503c3b7b5e69e3cb28
Independence required: yes — this session did NOT implement the correction
Independent of the correction: yes
Evidence posture: independent
Evidence tier: E3 (authN/authZ re-audit)
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

## Original risk claim

```text
Finding ID: audit-04-F01 / orch-05-D14
Status before S1: open — behind nginx, axes keys on REMOTE_ADDR (nginx's address
  for every request) because ipware is absent, so AXES_LOCKOUT_PARAMETERS=[["username","ip_address"]]
  degenerates to one global bucket per account → targeted account DoS, extendable indefinitely
  (AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT default true).
Durable evidence: DEFECT_LEDGER.md:529-543
```

## Correction under audit

Commit `75f18773f5936517652640503c3b7b5e69e3cb28` (parent `91a5730`), message `fix(axes): install ipware and key lockout on real peer behind nginx`. The rectification:

1. **`backend/pyproject.toml`** — `django-axes = {version = "==8.3.1", extras = ["ipware"]}`
2. **`backend/config/settings.py`** — three ipware settings set together:
   - `AXES_IPWARE_META_PRECEDENCE_ORDER = ("HTTP_X_FORWARDED_FOR", "REMOTE_ADDR")`
   - `AXES_IPWARE_PROXY_ORDER = "right-most"`
   - `AXES_IPWARE_PROXY_COUNT = 0` (intentionally NOT `_num_proxies()` — the DRF vs ipware integer mismatch is documented in the comment at lines 478-488)
3. **`backend/tests/test_security_settings.py`** — regression test `test_axes_ipware_returns_real_peer_in_proxied_topology` (line 845): two different synthetic peers behind a proxy must yield distinct client IPs.
4. **`backend/poetry.lock`** — `django-ipware 7.0.1` + `python-ipware 3.0.0` newly locked.

## The trap (DEFECT_LEDGER.md:488-508)

The following half-measures each silently fail and must be REJECTED:

```text
T1  Installing the ipware extra alone — nothing changes (default precedence is ("REMOTE_ADDR",))
T2  Adding HTTP_X_FORWARDED_FOR to precedence WITHOUT setting proxy_count — left-most is the client-supplied
    portion of $proxy_add_x_forwarded_for, attacker-chosen → worse than pre-fix
T3  Setting AXES_IPWARE_PROXY_COUNT = _num_proxies() (=1 in docker-compose) — strict mode requires
    len(ips) - 1 == count → overwrite has one element → count=1 requires two elements → returns None
    (shared empty bucket = still broken)
```

The shipped correction (precedence "HTTP_X_FORWARDED_FOR, REMOTE_ADDR" + right-most + count=0) succeeds because nginx overwrite produces exactly one element; count=0 with strict=True requires len(ips) == 1 → client IP returned. Every half-measure above returns the wrong identity or None.

## What you verify (all remotely, from the committed source)

1. Repository gate: HEAD = `75f18773f5936517652640503c3b7b5e69e3cb28`, porcelain empty.

2. **Source audit (static):**
   - grep for any OTHER `AXES_IPWARE_` or `IPWARE_` constant set elsewhere → must be exactly the three in settings.py
   - confirm `AXES_LOCKOUT_PARAMETERS` unchanged (still `[["username", "ip_address"]]`)
   - confirm `AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT` is the default (True, no override)
   - confirm no other settings.py change between lines 101-500 beyond the ipware block + comment update

3. **Dynamic probe: `get_client_ip_address` in the overwrite topology.** Run a scratch `.py` under `/tmp/opencode/axes-raudit/` using `backend/.venv/bin/python`, `DJANGO_SETTINGS_MODULE=config.settings`, `django.setup()`. Import `axes.helpers.get_client_ip_address`, `axes.conf.settings as axes_conf`. Probe:

| Scenario | REMOTE_ADDR | XFF | COUNT | Override? | Expected IP |
|---|---|---|---|---|---|
| overwrite, two peers | 10.0.0.1 | 203.0.113.10 | 0 | no | 203.0.113.10 |
| overwrite, second peer | 10.0.0.1 | 198.51.100.7 | 0 | no | 198.51.100.7 (≠ first) |
| local dev, no XFF | 127.0.0.1 | absent | 0 | no | 127.0.0.1 |
| trap T3: count=1 overwrite | 10.0.0.1 | 203.0.113.10 | 1 | yes | None |

If `get_client_ip_address` returns `None` in the trap-T3 probe with count=1, that confirms the comment is correct and count=0 is deliberate. If it returns the peer (false positive), the count=0 assumption is wrong.

4. **Dependency audit (static).** `git diff 91a5730..75f1877 backend/poetry.lock` — only `django-ipware 7.0.1` and `python-ipware 3.0.0` may be new. No unrelated version bumps. Verify via: list all packages whose version changed between the two lockfile states.

5. **Regression test verification:**
   - Run `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_security_settings.py::test_axes_ipware_returns_real_peer_in_proxied_topology -v` — must PASS.
   - Read the test: it uses `override_settings(AXES_IPWARE_PROXY_COUNT=0, AXES_IPWARE_META_PRECEDENCE_ORDER=..., AXES_IPWARE_PROXY_ORDER="right-most")` and constructs two synthetic requests. Verify the two peers differ.
   - The test does NOT prove the pre-fix state was wrong (it uses override_settings). That is acceptable: the pre-fix proof came from the implementation probe (IPWARE_INSTALLED=False, both returned REMOTE_ADDR). Your audit records whether this is sufficient.

6. **Full gate re-run:**
   - `pytest tests/test_security_settings.py` — all 58 must pass.
   - `pytest` (full backend) — must be green (1244+ passed).

## Authority

```text
Filesystem: read-only on the repo. Temp: /tmp/opencode/axes-raudit/ (create, use, delete).
Git: read-only. No stage, commit, push, checkout, reset.
Network: NONE. No push, no fetch, no web, no provider, no registry.
Correction authority: NONE. Do NOT mutate any file.
Secrets: none. Dependencies: none. Docker: none.
```

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo coordinates:

```text
Logical whole identity: proxied-axes-lockout-correction
Worker session ordinal: 02, Worker exchange ordinal: 01
```

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: acceptance-PASS | not-applicable
Result artifact or commit: 75f18773f5936517652640503c3b7b5e69e3cb28
Result evidence: <verdict per finding with evidence>
Logical-whole closure: not-closed
```

Per finding verdict: `verified-closed` or `not accepted`, with the evidence for each. Report the dynamic probe results as a table, the lockfile diff summary, the test outcome, any discrepancy from the implementation report. Include: the trap verification (did T3 return None as documented?), the DEFECT_LEDGER protection summary (no half-measure present), cleanup, authority expiry, context pressure.