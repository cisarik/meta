### Report for ORCHESTRATOR_CHAT

**Coordinates:** logical whole `framenest-companion-security-and-frozen-slice-validation`; Worker session ordinal `05`; Worker exchange ordinal `01`.
**Status:** BLOCKED — the pre-declared compatibility stopping condition was hit with static and dynamic evidence.
**Phase-qualified result:** not-applicable (no implementation-PASS candidate was produced).
**Start commit:** `6cdbe6f14f31fabc011a316a52026b3800f4e180` (branch `feat/x-meme-browser-companion`, porcelain empty, AP gitlink == `.ap` HEAD == `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` — gate verified before mutation). **End commit:** none made; repository end state is the exact start baseline (porcelain empty, HEAD unchanged, `ap project check` PASS re-verified at close-out).

**Why BLOCKED — requirement 3 compatibility gate fails (do-not-loosen condition):**

1. **Static evidence.** Installed pinned uvicorn 0.49.0 (`pyproject.toml` `uvicorn (>=0.49.0,<0.50.0)`; poetry.lock 0.49.0) hardcodes a post-bind permission widening: `Server.startup()` sets `uds_perms = 0o666` for a fresh socket and runs `os.chmod(config.uds, uds_perms)` immediately after `loop.create_unix_server(...)` (`.venv/lib/python3.13/site-packages/uvicorn/server.py:156-167`); the same `0o666` chmod exists in `Config.bind_socket()` (`uvicorn/config.py:540-546`). There is no configuration knob to suppress it. A pre-existing socket file's mode is preserved (`uds_perms = os.stat(config.uds).st_mode`), but the documented posture never pre-creates the socket: `deploy/systemd/framenest.service` creates only the empty `RuntimeDirectory=framenest` at boot and its single `ExecStartPre` is `check-database-ready`.
2. **Dynamic evidence** (run through `./.ap/ap exec --operation test-focus`, probe placed transiently on the allowlisted `tests/contract/test_uvicorn_runtime.py`): a real uvicorn 0.49.0 UDS bind under `umask 0o077` (documented posture: fresh `RuntimeDirectory` + `UMask=0077`, socket absent at bind) produced `PROBE ... mode=0o666 uid=1000 euid=1000 owner_only=False`. The required assertion (`S_ISSOCK`, `mode & 0o077 == 0`, `st_uid == os.geteuid()`) would fail on the mode condition on every first boot → CRITICAL log + fail-closed exit → systemd `Restart=on-failure` would loop forever. The documented posture cannot produce the assumed "bound socket mode 0700".
3. **Complementary dynamic evidence:** a socket file pre-created with mode `0700` is preserved through uvicorn's bind (observed post-bind `mode=0o700`), so the required check would pass if the socket were pre-created owner-only (e.g. `ExecStartPre` step or a `systemd.socket` unit).
4. The finding itself is thereby statically confirmed as worse than "plausible": today's documented deployment binds a group-and-world-connectable socket (0666) while `Tailscale-User-*` header trust is bound to that socket.

**Decision compliance:** per the task's stopping condition ("the check would break the documented systemd posture — report BLOCKED, do not loosen") I stopped: no loosened check, no unauthorized remediation-by-chmod inside `server.py` (it would add a socket-hardening behavior change beyond the accepted slice), no deployment-file change (outside allowlist), no commit. The transient probe was reverted via `git restore -- tests/contract/test_uvicorn_runtime.py` (the only path touched; rollback checkpoint "pre-edit state is the exact baseline" applied).

**Uvicorn-seam decision (designed, not landed):** a `uvicorn.Server` subclass overriding `async startup()` — `await super().startup(...)` then a synchronous, await-free check of the configured `uds_path`, raising `SystemExit(1)` after emitting CRITICAL through `framenest.structured_logging` (`get_logger("server")`, event `uds_permission_assertion_failed`, UPPER_SNAKE `error_code`, no path in the record). Ordering guarantee in 0.49.0: after `super().startup()` binds, its remaining body is synchronous; the check runs with no intervening event-loop yield, so on failure `main_loop()` is never entered and the exception propagates through `serve()`/`asyncio_run` to a non-zero exit — no request can be served by a permissive socket (connections at most sit in the kernel backlog, never accepted). Post-bind-only was sufficient because ordering is guaranteed; no pre-bind check needed.

**Tests and validation (exact commands/outcomes):**
- `./.ap/ap project check --root /home/agile/Projects/framenest --baseline 6cdbe6f…` → PASS (pre-mutation and at close-out).
- Prescribed focused suite at the exact baseline: test-focus over tests/unit/test_server_runtime.py, tests/contract/test_uvicorn_runtime.py, tests/contract/test_tailscale_ingress_security.py → **107 passed in 47.06s**.
- Probe runs (transient probe test, since reverted): fresh-bind probe → FAILED with `documented posture yielded mode 0o666 uid 1000, required check would fail` (this failure is the BLOCKED evidence, not a regression); pre-created-0700 probe → PASSED (`mode=0o700`); pre-existing contract test in the same file passed alongside (`1 failed, 1 passed`).

**Commit result:** no commit, no push, no force; nothing staged.

**Changed files and purpose:** none retained (probe reverted; end state is the exact baseline).

**Deviations / risks / missing evidence:** no NUC observation was authorized, so live-socket mode on the NUC remains unproven dynamically (static code path says 0666 after first bind there too); the acceptance-doc A9 "no world bits" diagnostic has apparently never been run against the live socket. Test-design notes for the eventual slice: the foreign-owner fail case can be expressed portably by monkeypatching `os.geteuid`; `test_importing_server_module_has_no_runtime_side_effects` will need its `uvicorn.Server` MagicMock replaced by a raising stub class, because the module-level subclass definition requires a real class base.

**Smallest next step:** Orchestrator decision on remediation authority — either authorize a bounded follow-up slice adding a post-bind owner-only chmod inside the same `server.py` seam immediately before the accepted assertion, or authorize a deployment slice pre-creating the socket mode 0700 (e.g. `ExecStartPre` or `systemd.socket`), after which the accepted fail-closed assertion applies unchanged. No loosening is required in either route.

**Report justification:** new-mutation.
**Authority expiry:** this terminal report expires my authority; no continuing work, retained context, or self-granted follow-up is authorized.

Resolved Execution Issues / Near-Misses: two probe-harness corrections (lifespan setup for direct `startup()` invocation) before evidence was produced; no production path was touched at any point.
Pre-Existing Failure Classification: none (focused suite fully green at baseline: 107 passed).
