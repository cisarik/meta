### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-REPO
status: PASS
Phase-qualified result: implementation candidate committed
Start commit: 82a6a59803ed8830c19e51cd8f9bc1665c28a975
End commit: c975aba14840b97944aecc655907e3abc370341d
Report justification: new-mutation
Logical-whole closure: not-closed

Session posture: this was a fresh session. It did not implement or correct S2. Prior plans and reports were read as evidence only. Independence required: no. This result is non-independent implementation evidence.

Requested reasoning: High. Effective reasoning was ordinary implementation depth on the granted files. Model identity was not independently attested.

## Changed files and purpose

Branch `feat/kronika-one-product`. Parent of the new commit is the baseline. Tree `a80ab53cf5ee19ffe0af46de4e015519cd97d941`. Worktree clean after the commit. No push.

| Path | Purpose |
|---|---|
| `deploy/systemd/kronika-capture-xvfb.service` | Virtual display `:99`, restricted Xauthority, no auto-restart, shared `/tmp/.X11-unix`. |
| `deploy/systemd/kronika-capture-bridge.service` | Loopback bridge; may restart on failure; systemd credential `token`. |
| `deploy/systemd/kronika-capture-runner.service` | Headed runner; no auto-restart; same credential and display; explicit profile. |
| `deploy/systemd/kronika-capture-vnc.service` | Loopback VNC, normally not installed, 1800 s limit. |
| `deploy/systemd/kronika-capture-view.service` | Loopback noVNC, normally not installed, 1800 s limit. |
| `deploy/systemd/kronika-capture.env.example` | Non-secret Chromium path and documented contract paths. No secret. |
| `deploy/ubuntu/framenest_release.py` | Capture identity in the manifest; `activate-capture` and `rollback-capture`. |
| `deploy/ubuntu/framenest-release` | Still the sole entry point; capture subcommands are forwarded unchanged. |
| `deploy/ubuntu/README.md` | Capture commands and the web/capture split. Does not claim deployment. |
| `docs/UBUNTU_NUC_DEPLOYMENT.md` | Units, paths, credentials, view procedure, activation rules. Not deployed. |
| `src/kronika_capture/config.py` | Credential name and the 300000 ms brake constant. |
| `src/kronika_capture/paths.py` | Systemd credential file lookup and token-path fallback. |
| `src/kronika_capture/bridge/auth.py` | Credential token wins; unusable credential does not mint a replacement. |
| `src/kronika_capture/cli.py` | `runner run` launcher. Token bytes are not command arguments. |
| `tests/contract/test_nuc_release_source_contract.py` | Manifest now includes the capture identity fields. |
| `tests/contract/test_nuc_release_docs.py` | Docs name activation and say capture is not deployed. |
| `tests/contract/test_nuc_release_remote_contract.py` | Existing deploy/rollback fakes; web rollback leaves capture untouched. |
| `tests/contract/test_nuc_operator_runbook.py` | Runbook capture section stays inside the existing hygiene contract. |
| `tests/contract/test_kronika_capture_services.py` | Unit directives, env template, activation behavior, web/capture split. |
| `tests/unit/chatgpt_page/test_systemd_credentials.py` | Credential present, fallback, empty credential, auth semantics, launcher argv. |

`git diff --name-status 82a6a59803ed8830c19e51cd8f9bc1665c28a975..HEAD` is those 20 paths. No path outside the allowlist. `tests/unit/chatgpt_page/**` is the new credential test only.

## Unit and helper design

Persistent units are `kronika-capture-xvfb.service`, `kronika-capture-bridge.service`, and `kronika-capture-runner.service`, each with `[Install]`. VNC and noVNC have no `[Install]`.

- Xvfb and the runner set `Restart=no`. The bridge sets `Restart=on-failure`.
- No capture unit contains `PartOf=framenest.service`.
- The runner `Requires=` Xvfb and is ordered `After=` the bridge. It does not `Requires=` the bridge, so a bridge restart does not stop the browser.
- Xvfb and the runner omit `PrivateTmp`, share `/tmp/.X11-unix` and `/run/kronika-capture/Xauthority`, and Xvfb uses `-auth` plus `-nolisten tcp`. It does not use `-ac`.
- Bridge and runner `LoadCredential=token:/etc/kronika-capture/credentials/kronika-bridge-token`.
- Bridge listen address stays `127.0.0.1` in the existing server. The unit passes `--port 8765`.
- VNC uses `-localhost` and `-rfbport 5900`. noVNC binds `127.0.0.1:6080` to `127.0.0.1:5900`. Both set `RuntimeMaxSec=1800`.
- State directories use `StateDirectoryMode=0700`. The runner creates `profile` and `staging` at mode 0700 as the capture user.
- Contract paths are `/var/lib/kronika-capture`, `profile`, `capture-journal.sqlite3`, `staging`, `/run/kronika-capture`, `/etc/kronika-capture/capture.env`, and `/opt/framenest/capture-current`.

Release helper (`deploy/ubuntu/framenest_release.py`):

- `make_manifest` (line 178) adds `capture_code_tree`, `capture_runtime_contract_sha256`, `capture_unit_contract_sha256`, and `capture_bridge_protocol`.
- `capture_runtime_identity` (line 756) derives those from the git tree `src/kronika_capture`, a fixed node-stdlib runtime contract, and the six capture unit/template sources. Protocol is `1`.
- Web `deploy` and `rollback` still switch only `/opt/framenest/current` and restart only `framenest.service`. They print `web_release` and `capture_release`. They do not delete a release directory.
- `activate-capture` and `rollback-capture` share `_cmd_capture_transition` (line 1630): verify the installed SHA, manifest identity, and protocol `1`; drain queued journal work; refuse `offered`/`running` or `needs_admin`; enforce the 300000 ms brake from `profile.capture-launch/last-start.json`; `cmd_remote_atomic_switch_capture` (line 553); exactly one `systemctl restart kronika-capture-runner.service`; poll readiness and do not restart again on `failed`, `browser_unavailable`, or `needs_admin`.
- A missing capture pointer is `capture_release: absent`. An existing capture pointer with a different protocol is refused before restart.
- `migration-required` on web deploy is unchanged. Capture activation does not call `framenest-db` or migrate.

## Credential integration

Choice: systemd's `CREDENTIALS_DIRECTORY` file named `token`, which is the name the existing node runner already reads as `<state-dir>/token`.

- `paths.systemd_bridge_token_path` (line 43) accepts only an absolute directory and a regular file. Symlinks are ignored.
- `paths.read_systemd_bridge_token` (line 69) returns `None` when systemd did not provide the file, and `""` when the file is present but empty, oversized, or not a single UTF-8 line. It does not log the value.
- `auth.load_or_create_token` (line 44) returns that credential and does not mint a second token. With no credential file, the state-directory token is reused or created as before (`secrets.token_urlsafe`, mode `0600`).
- The bridge server already calls `load_or_create_token`, so it picks up the credential without a server change.
- `cli.build_runner_argv` (line 294) passes the credentials directory as `--state-dir` when the credential file exists, plus an explicit `--profile` and `--chrome-path`. The token value is not an argument. `configured_chromium` (line 263) requires an absolute executable from `--chrome-path` or `KRONIKA_CHROMIUM_PATH`. It does not search `PATH` and does not add sandbox or stealth flags.
- Without the credential, the launcher keeps the explicit state directory and the existing token file.

Test evidence in `tests/unit/chatgpt_page/test_systemd_credentials.py`: credential used and state token not created; `build_state` uses the credential; missing directory and missing variable fall back, including a minted token; empty credential does not mint; symlink ignored; Host/Origin/token results stay 200/403/401; runner argv contains the credential directory and the synthetic value does not appear, and `--no-sandbox` / `--stealth` are absent.

The web unit was not edited. `docs/UBUNTU_NUC_DEPLOYMENT.md` records the two-line `LoadCredential=token:...` drop-in for a later host grant. This slice does not add the web account to the capture account.

## Validation

1. `./.ap/ap project check --root /home/agile/Projects/framenest --baseline 82a6a59803ed8830c19e51cd8f9bc1665c28a975` PASS before mutation and PASS after the commit.
2. Declared `./.ap/ap exec --operation test-focus` on the granted test paths: `195 passed` in 4.59s. The pytest summary listed no failures. No Node suite was run; no JavaScript path changed.
3. `tests/contract/test_kronika_capture_services.py` covers unit directives, the env template, activation order, live/paused refusal, queued drain, brake refusal, exactly one runner restart, no second restart after `browser_unavailable`, protocol refusal, capture rollback, and web rollback leaving capture untouched. Both pointer SHAs are printed.
4. Credential tests above.
5. Name-status against the baseline is the 20 paths above. Clean worktree. One commit. Branch `feat/kronika-one-product`. HEAD `c975aba14840b97944aecc655907e3abc370341d`, parent `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, tree `a80ab53cf5ee19ffe0af46de4e015519cd97d941`.
6. AP gitlink and detached `.ap` HEAD remain `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. `main` and `origin/main` remain `26d28b16c08a5e7e0179a32c16646bfdc1009c81`. No diff in `pyproject.toml`, `poetry.lock`, `AGENTS.md`, `src/framenest`, `.gitmodules`, or `ap.project.conf`.
7. New and changed sources, templates, tests, and docs were scanned for password assignments, private-key blocks, bearer tokens, and non-loopback private addresses. None were added. Loopback `127.0.0.1` remains the bind contract. Tests use the synthetic string `synthetic-bridge-token`.

No host, NUC, SSH, browser, login, or real token operation was performed. Capture is not deployed. Host preflight is not claimed to have passed.

## Deviations, risks, missing evidence

- `deploy/systemd/framenest.service` is outside the allowlist, so the web credential drop-in is documented rather than added to the unit. Bridge and runner units load it.
- Xvfb, `xauth`, `mcookie`, `x11vnc`, and `websockify` paths are repository assumptions. The NUC was not contacted, so those binaries, ports 5900/6080/8765, the account, and AppArmor/sandbox behavior are unverified.
- Capture activation refuses an already installed release whose manifest lacks the new identity fields. Releases deployed by the previous helper cannot be activated until a release built with this helper is installed.
- Failed capture readiness does not switch the pointer back and does not restart the runner again. The new pointer remains; a later `rollback-capture` is the deliberate reversal, subject to the same brake.

## Smallest next step

Read-only NUC preflight of the capture account, paths, loopback ports, Node/Chromium/Xvfb/VNC binaries, and release pointers. Do not install units in that preflight.

Orchestration critique:
MEASURED: the accepted plan requires systemd credential delivery to the web as well as the bridge and runner, while `deploy/systemd/framenest.service` is outside this grant's allowlist (`04_implementation_00.md` changed-path allowlist; `git diff --name-status` does not include that unit). Effect: bridge and runner load `token`; the web unit does not. Smallest correction: a later grant that adds one web drop-in path and no profile access for the web account.
LEAD: conventional binary paths in the new units may not match the NUC; the cheapest check is the read-only preflight above, without starting the units.
Resolved Execution Issues / Near-Misses: the runner-argv test first placed `--state-dir` after the subcommand; argparse rejected it. The test now passes `--state-dir` on the parent parser. Fixed before commit. No residual product defect.
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
