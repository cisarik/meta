### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 08
Worker exchange ordinal: 01

Persistent role identity: WORKER
Task identity: KRONIKA-ONE-PRODUCT-S3-ACCEPTANCE
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Native planning mode: not-used
Phase: acceptance
Status: PASS
Phase-qualified result: acceptance-PASS
Start commit: c975aba14840b97944aecc655907e3abc370341d
End commit: c975aba14840b97944aecc655907e3abc370341d
Report justification: final-acceptance
Logical-whole closure: not-closed

The S3 candidate is safe and correct to deploy within the six fixed claims. Unit directives, the in-process credential boundary, and the capture transition behave as specified. No blocking finding was established. This report grants no host setup, publication, or deployment authority.

Changed candidate files: none. The only durable write by this Worker is this report. Commit and push were not authorized and were not performed.

Smallest next step: the Orchestrator reconciles this report and records the S3 acceptance decision. Host setup remains a separate grant.

#### Independence, authority and verified state

Actual independence posture: fresh Worker session. This conversation did not implement S3 and did not participate in its implementation. No predecessor conversation was inherited as reasoning. The accepted plan sections 7.2-7.3 and the S3 row, and the S3 implementation report, were available as historical evidence; verdicts below come from this session's inspection, the declared route, and the synthetic probes. No subagents were used.

Requested reasoning recommendation: High. This session does not independently attest a model identity.

The governing AP Worker spine, AP_WORKER.md session-target and reporting sections, the Worker report header, and the FrameNest project rules were read. The authoritative task remained this acceptance prompt.

Observed at start and rechecked after probe cleanup, before this report was saved:

- Physical target: /home/agile/Projects/framenest. Standalone checkout. Git directory /home/agile/Projects/framenest/.git. Not a submodule worktree.
- Branch: feat/kronika-one-product.
- HEAD: c975aba14840b97944aecc655907e3abc370341d.
- Parent: 82a6a59803ed8830c19e51cd8f9bc1665c28a975.
- Tree: a80ab53cf5ee19ffe0af46de4e015519cd97d941.
- Subject: feat(capture): supervise capture separately from web deploys.
- Index and worktree clean. No merge, rebase, cherry-pick, or revert marker. No index or HEAD lock.
- Local main and origin/main both 26d28b16c08a5e7e0179a32c16646bfdc1009c81. No remote-tracking ref for feat/kronika-one-product. No fetch and no remote contact. Public branch state not directly observed.
- AP gitlink and detached .ap HEAD both 7478ddb07d2c3911f79e1aa1441f0115a31c45d8. Submodule porcelain empty.
- Diff against the parent is exactly the 20 paths named in the prompt: 6 added unit/template files, 3 release-helper paths, the deployment document, 4 capture sources, and 6 test paths. 1483 insertions, 9 deletions.
- private/** was not read. The NUC, SSH, and systemd on the host were not contacted.
- The report destination was absent. Its parent path contained no symlinks.

#### Acceptance and Correction Record

```text
Acceptance candidate: c975aba14840b97944aecc655907e3abc370341d
Acceptance tree: a80ab53cf5ee19ffe0af46de4e015519cd97d941
Acceptance branch: feat/kronika-one-product
Acceptance parent: 82a6a59803ed8830c19e51cd8f9bc1665c28a975
Acceptance owner map: the 20 S3 paths listed in the issued prompt; accepted plan 01_report_00.md sections 7.2-7.3 and the S3 row; S3 report 04_report_00.md; the classified preflight facts in the issued prompt
Acceptance allowlist: read-only review of the candidate and governing AP; the declared focused routes; synthetic temporary probe state under /tmp/kronika-one-product-s3-acceptance; this terminal report
Acceptance risk claims: the six fixed claims in the issued prompt
Acceptance control matrix: completed below, with directly observed results
Acceptance independence: required-fresh-independent; satisfied by this session's actual separation
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
Acceptance outcome: PASS; no blocking finding remains within this slice
Result artifact or commit: this report against the frozen candidate
Result evidence: declared route, unit inspection, synthetic credential and helper probes
Logical-whole closure: not-closed
```

#### Evidence selection and per-claim verdicts

Evidence tier: E3
Evidence tier basis: fresh independent review of deployment tooling and a credential boundary before host installation
Validation ladder: selected
Inspection and provenance: completed
Existing focused tests: completed, 195 passed
Affected tests: included in the declared route
New causal regression: none; temporary probes only
Broad or full suite: not-used
Runtime or testbed: declared route plus synthetic temporary probes; no host
Independent acceptance: required-separate-fresh-worker; this exchange

| Fixed claim | Verdict | Independently established evidence |
| --- | --- | --- |
| 1. Unit directives | PASS | All five units parsed. No `PartOf=`, `BindsTo=`, `ConsistsOf=`, or `PropagatesStopTo=`. Xvfb and runner `Restart=no`. Bridge `Restart=on-failure`. Runner `Requires=` only `kronika-capture-xvfb.service` and does not require the bridge. Xvfb uses `-nolisten tcp` and `-auth`; the exec tokens do not contain `-ac`. Xvfb and runner do not set `PrivateTmp` and both name `/tmp/.X11-unix` and `/run/kronika-capture/Xauthority`. VNC uses `-localhost` and port 5900. noVNC listens on `127.0.0.1:6080` and targets `127.0.0.1:5900`. Both view units set `RuntimeMaxSec=1800`, `Restart=no`, and have no `[Install]`. Bridge and runner `StateDirectoryMode=0700`. Xvfb `RuntimeDirectoryMode=0700`. Runner `ExecStartPre` creates profile and staging with mode 0700. All five units set `UMask=0077` and `User=kronika-capture`. Bridge debugging in the unchanged launcher is `--remote-debugging-address=127.0.0.1`. |
| 2. Credential boundary | PASS | Bridge and runner units contain `LoadCredential=token:/etc/kronika-capture/credentials/kronika-bridge-token`. A regular credential file wins and does not create a state token. Unset `CREDENTIALS_DIRECTORY` keeps the state token. A missing credential directory mints through the existing writer: mode 0600, `TOKEN_BYTES` 32, recorded length 43, value not recorded. Empty, whitespace, 4097-byte, non-UTF-8, NUL, and internal-newline credentials return an empty token and do not mint. A 4096-byte credential is accepted. A symlink credential file is ignored. Host, Origin, and token results match the existing comparison, including empty Origin rejected with 403. `hmac.compare_digest` is the comparison. Launcher argv contained the credential directory and the explicit Chromium path, and did not contain the synthetic marker, `--no-sandbox`, or `--stealth`. A relative Chromium path is rejected. `deploy/systemd/framenest.service` is unchanged, has `User=framenest` and `Group=framenest`, and names neither the capture profile nor `LoadCredential`. |
| 3. Release helper | PASS | Manifest identity keys are `capture_code_tree`, `capture_runtime_contract_sha256`, `capture_unit_contract_sha256`, and `capture_bridge_protocol` `1`. Fake-runner `activate-capture` and `rollback-capture` verified the installed SHA and manifest, refused a mismatched SHA, tree, and protocol before any restart, drained two queued polls then continued, refused live and paused work, refused the brake, switched `capture-current` with one command, restarted `kronika-capture-runner.service` once, and did not restart it again after failed, unavailable, or needs_admin readiness or after a failed restart. Success and failure reports named web `82a6a59803ed8830c19e51cd8f9bc1665c28a975` and capture `c975aba14840b97944aecc655907e3abc370341d`. Web rollback restarted only `framenest.service`, left capture unswitched, and reported `capture_release: absent`. Status did the same. Deploy with unequal revisions exited 13 with `migration-required` before either pointer switch or either restart, and issued no migrate or delete command. |
| 4. Documentation and tests | PASS | `docs/UBUNTU_NUC_DEPLOYMENT.md` states that the capture units and helper do not record a completed capture deployment. The deploy README says nothing in that directory is evidence that capture is already deployed. The declared suite passed, including the new service contract and credential tests. The leak hunt found no secret, token value, private address, or private key in the 20 changed paths. Matches for `PartOf=`, `0.0.0.0`, `Bearer `, `password=`, `api_key=`, and `--no-sandbox` are prohibition text in docs, the log denylist, or negative assertions. |
| 5. Capture semantics preserved | PASS | `git diff` against the parent is empty for `errors.py`, `jobs.py`, `journal.py`, `server.py`, `protocol.js`, `driver.mjs`, `runner.mjs`, and `framenest.service`. `PROTO_VERSION` is 1 and equals the helper protocol. The unchanged driver still refuses a launch when elapsed time is below 300000 ms. `TOKEN_BYTES` remains 32. Wire comparison and the empty-Origin rejection are unchanged. The credential branch returns before minting and does not alter `rotate_token`. |
| 6. Preflight consistency | PASS | No classified fact contradicts the units, the template, or the plan's deployment design. Unverified items are named in the preflight section and were not assumed. |

#### Control matrix

Positive controls, run from `/home/agile/Projects/framenest` through `./.ap/ap`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d
```

Result: exit 0. `ap project check --baseline: PASS`. It reported a non-failing warning that inherited environment classes were sanitized (`LD_LIBRARY_PATH`, `SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PROMPT_COMMAND`, `APPDIR`, `APPIMAGE`, `PATH`).

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d --operation test-focus -- tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/contract/test_kronika_capture_services.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Result: exit 0. `195 passed in 4.55s`. No failures and no skips were printed. The same non-failing environment-sanitization warning was printed. Ambient pytest was not used.

Negative and adversarial controls used one temporary root, `/tmp/kronika-one-product-s3-acceptance`, mode 0700, not a symlink. The probe imported the candidate. SSH was intercepted inside the fake runner and was not executed. `git ls-remote` was not executed. The deploy probe returned a local string for that argv so the helper could reach the schema gate; that string is not evidence of public `main`.

Gate scripts were the production `python3 -c` sources with only the hardcoded `/var/lib/kronika-capture/...` path replaced by a path inside the temporary root. The readiness script's `subprocess.run` was replaced by a stub that returned a chosen `ActiveState`. `systemctl` was not executed.

Unit directive matrix, from an independent parser plus the file text:

| Unit | Restart | Requires | LoadCredential | PrivateTmp | Install | Other required property |
| --- | --- | --- | --- | --- | --- | --- |
| xvfb | no | none | none | absent | yes | `-nolisten tcp`, `-auth`, runtime mode 0700, no `-ac` |
| bridge | on-failure | none | token absolute path | true | yes | state mode 0700, port 8765, no `0.0.0.0` |
| runner | no | xvfb only | token absolute path | absent | yes | state mode 0700, profile and staging created mode 0700, `/tmp/.X11-unix` |
| vnc | no | xvfb | none | absent | no | `-localhost`, port 5900, `RuntimeMaxSec=1800` |
| view | no | none | none | absent | no | `127.0.0.1:6080` to `127.0.0.1:5900`, `RuntimeMaxSec=1800` |

No capture unit contains a coupling that would stop the runner when the bridge restarts. No view unit lacks its time limit. No capture unit lacks the credential where the claim requires it: bridge and runner have it; xvfb, vnc, and view do not.

Credential probes, synthetic files only:

| Case | Observed |
| --- | --- |
| Regular credential and a different state file | credential value returned; state file not created |
| `CREDENTIALS_DIRECTORY` unset | existing state token returned |
| Credential directory missing | state token minted, mode 0600, length 43 |
| Empty, spaces, 4097 bytes, non-UTF-8, NUL, internal newline | empty result; no state file |
| Exactly 4096 bytes | that value used; no state file |
| Symlink named `token` | path rejected; existing state token kept |
| Symlink named `token`, no state token | ignored, then the previous mint path runs |
| `CREDENTIALS_DIRECTORY` itself is a directory symlink | the regular file inside the target is used |
| Absent Origin | accepted, 200 |
| Empty Origin | rejected, 403 |
| Foreign Origin | rejected, 403 |
| Exact loopback Origin | accepted, 200, allow-origin echoed |
| Wrong Host | rejected, 403 |
| Wrong token | rejected, 401 |
| Empty expected token | rejected, 401 |
| Runner argv | credential directory present; synthetic marker absent from argv and environ |

Helper probes, one fake runner, no network:

| Case | Exit | Runner restarts | Order observed |
| --- | --- | --- | --- |
| activate, idle, ready | 0 | 1 | work, brake, switch, restart, readiness |
| rollback-capture, idle, ready | 0 | 1 | same, no web restart, no web switch |
| live | 22 | 0 | work only |
| paused | 22 | 0 | work only |
| queued, queued, then clear | 0 | 1 | three work polls, then brake, switch, one restart |
| queued and drain deadline 0 | 22 | 0 | work only |
| brake refuse | 23 | 0 | work, brake |
| protocol 9 on the current capture manifest | 3 | 0 | no work and no restart |
| installed SHA mismatch | 3 | 0 | no restart |
| manifest tree mismatch | 3 | 0 | no restart |
| readiness failed, browser_unavailable, or needs_admin | 16 | 1 | one restart, one readiness poll, both SHAs printed |
| readiness starting then ready | 0 | 1 | two readiness polls, one restart |
| restart command fails | 15 | 1 | switch, one restart, no readiness poll, both SHAs printed |
| web rollback | 0 | 0 | one `framenest.service` restart; capture switch absent; `capture_release: absent` |
| status, capture link absent | 0 | 0 | `capture_release: absent` and the web SHA |
| deploy, revisions 0028 and 0029 | 13 | 0 | `migration-required`; no web switch, no capture switch, no restart |

Work-gate classifications, synthetic SQLite journals: absent `none`; offered, running, and queued-plus-running `live`; needs_admin job and needs_admin service `paused`; queued `queued`; done `none`; symlink to a real journal `unverifiable`.

Brake-gate classifications: missing directory `ok`; directory without metadata, elapsed about 299 seconds, future timestamp, boolean, missing field, oversized metadata, and a metadata symlink `refuse`; elapsed about 301 seconds `ok`. The comparison is strict `< 300000`.

Readiness-script classifications with a stubbed active state: failed unit `failed`; active plus ready `ready`; needs_admin `needs_admin`; browser_unavailable `browser_unavailable`; active plus missing journal `starting`; activating `starting`.

Leak hunt: no `-ac` exec token, no private-network address, and no private-key block in the 20 paths. The capture profile path appears only as the planned path in the runner unit, env template, helper, deployment doc, and service test. It does not appear in `framenest.service`.

#### Findings

Findings: none.

#### Preflight consistency

Consistent with the units and template: systemd 255 with `LoadCredential` supported; capture account and capture paths absent before setup; `/tmp/.X11-unix` mode 1777 with no `:99` lock; `/usr/bin/chromium` matches `KRONIKA_CHROMIUM_PATH`; Xvfb, x11vnc, websockify, install, xauth, mcookie, and node are present; ports 8765, 5900, and 6080 are the unit ports and are free; the web unit's existing AI credential line is a different credential namespace from `/etc/kronika-capture/credentials/kronika-bridge-token`.

Named and not assumed:

- The preflight states that `node`, `xauth`, and `mcookie` are present. It does not state their paths. The Xvfb unit invokes `xauth` and `mcookie` through `PATH`, and the launcher invokes bare `node`.
- The userns restriction value is 1 and an AppArmor userns profile is present. Whether that profile lets Chrome for Testing 154.0.8037.57 start with the sandbox unchanged was not tested. No browser was launched. The units do not add a sandbox-weakening flag.
- Host systemd was not asked to start a unit whose absolute credential file is missing. This workstation's `systemd.exec` text says a missing credential is non-fatal when the path is omitted or is a credential identifier. These units use an absolute path and do not prefix it with `-`. The in-process fallback was executed. The host start failure for a missing source file was not.

#### Containment, provenance and cleanup

```text
Temporary root: /tmp/kronika-one-product-s3-acceptance
Owner: assigned acceptance WORKER
Mode: 0700, verified before removal
Symlink: no
Contents class: one synthetic probe script, its JSON summary, disposable credential files, SQLite journals, and brake metadata
Network targets: none
Cleanup owner: assigned acceptance WORKER
Cleanup outcome: removed; exact path absence verified
```

Removed-script SHA-256 before cleanup:

```text
probe.py      31a097a9dc129f3f42456c916250fc12da3b09e194fa1848959cb51465c334d0
probe-out.json 65c803dfa75bb41f5fe7ffa75c5d64433259de353c779bfa812545c1cc9f778d
```

The repository index remained clean after removal. No release directory, credential, or host path outside the temporary root was created.

#### Residual risk and ledger candidate

- Plan 7.2 says to deliver the per-install token to the web, the bridge, and the runner. Fixed claim 2 and this slice cover the bridge and runner. `framenest.service` is outside the S3 allowlist and was not changed. The deployment doc defers a one-line web drop-in to a later host grant and says that drop-in must not add the web account to the capture account or open the profile. Ledger candidate only. It does not fail the fixed claim.
- A symlink at the credential file is ignored. A symlink used as `CREDENTIALS_DIRECTORY` is followed when the final `token` file is regular. systemd's own credential directory is normally a real directory. This was not treated as a failed claim.
- The work gate reports a dangling journal symlink as `blocked=none`, the same result as a missing journal, because `Path.exists()` is false before the symlink check. A symlink to an existing journal is `unverifiable`. The capture account owns that path and can also unlink the journal. Absent journal is the specified first-install result. Not a failed ordinary live/paused control.
- `retained_release_paths` is not called by deploy or rollback. Retention holds because those commands remove only `/run/framenest-release-deploy` temporaries, which the probes did not see applied to `/opt/framenest/releases/`.
- VNC uses `-nopw` together with `-localhost`. While an operator has started the view units, another local user can open the loopback ports. That matches the loopback and SSH-tunnel design. The units are not installed by default and stop after 1800 seconds.
- The X cookie is expanded by `mcookie` inside the Xvfb `ExecStartPre` shell. That can place the cookie in the `xauth` argument list. It is not the bridge token. The bridge token was absent from the launcher argv.

#### Orchestration critique

```text
Orchestration critique:
MEASURED: none
LEAD: host PATH entries for node, xauth, and mcookie, and whether the existing AppArmor userns profile permits this Chrome build without sandbox weakening; cheapest useful check is the separate host-setup grant, not another repository review
Resolved Execution Issues / Near-Misses: the first helper fake returned the capture manifest for the web pointer, so both printed SHAs were the candidate. The probe was corrected and rerun. The second run printed web 82a6a59803ed8830c19e51cd8f9bc1665c28a975 and capture c975aba14840b97944aecc655907e3abc370341d. No candidate file changed.
Pre-existing Failure Classification: none
```

Authority expiry: this terminal report ends the grant. No autonomous continuation, correction, deployment, or publication follows from it.
