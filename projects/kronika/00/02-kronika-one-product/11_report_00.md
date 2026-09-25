### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 11
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-REACCEPTANCE
Status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
Result evidence: declared route, unit and CLI inspection, synthetic credential and helper probes
Start commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
End commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
Logical-whole closure: not-closed
Report justification: final-acceptance

Actual independence posture: fresh Worker session. This conversation began with the acceptance prompt. It did not implement S3 and did not correct S3. Prior plans, reports, and the classified host evidence were used as evidence. Verdicts below come from this session's inspection, the declared route, and the synthetic probes. No subagent was used. The NUC was not contacted.

## Compact outcome

The corrected candidate closes F-HOST-01 and F-HOST-02 in the deployment sources and keeps the accepted S3 guarantees that this exchange could re-establish. No blocking finding remains. This report grants no publication, deployment, or host-retry authority. A live corrected Xvfb under the unit was not run.

Requested reasoning: High. Effective reasoning was a full fresh re-audit of the corrected sources. Model identity was not independently attested.

## Identity gate

Observed before probes and again after probe cleanup, before this report was saved:

- Checkout `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`, HEAD `94e605c17b881461fad3e22fd8c7fca32cb93976`, parent `c975aba14840b97944aecc655907e3abc370341d`, tree `4667f47c24e84d80574beb66b71aca533393d994`, subject `fix(capture): accept the capture CLI state directory and skip the Xvfb lock`.
- Index and worktree clean. No index lock.
- Local `main` and `origin/main` both `c975aba14840b97944aecc655907e3abc370341d`. Remote URL `https://github.com/cisarik/framenest.git`. Public `refs/heads/main` was not refreshed with `git ls-remote` in this exchange.
- Governing AP gitlink and detached `.ap` HEAD `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` was not read.
- Report destination was absent. Its resolved path equals `/home/agile/meta/projects/kronika/00/02-kronika-one-product`.

## Acceptance and Correction Record

```text
Acceptance candidate: 94e605c17b881461fad3e22fd8c7fca32cb93976
  (tree 4667f47c24e84d80574beb66b71aca533393d994, branch feat/kronika-one-product,
   parent c975aba14840b97944aecc655907e3abc370341d)
Acceptance owner map: S3 commit paths (20 paths, 82a6a59803ed8830c19e51cd8f9bc1665c28a975..c975aba14840b97944aecc655907e3abc370341d) plus the correction delta (4 paths, c975aba..candidate). The prompt's base 26d28b16..c975aba is 80 paths across five commits; the leak hunt used the 20-path S3 commit. See orchestration critique.
Acceptance allowlist: read-only review of the candidate and governing AP; the declared focused route; synthetic temporary probe state under /tmp/kronika-one-product-s3-reacceptance; this terminal report
Acceptance risk claims: the seven fixed claims; all seven PASS
Acceptance control matrix: completed below, with directly observed results
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
Acceptance outcome: PASS; no blocking finding remains
```

## Per-claim verdicts

| Claim | Verdict | Observed |
| --- | --- | --- |
| 1. Unit directives | PASS | All five units parsed. None contain `PartOf=`, `BindsTo=`, `ConsistsOf=`, or `PropagatesStopTo=`. Xvfb and runner `Restart=no`. Bridge `Restart=on-failure`. Runner `Requires=` is only `kronika-capture-xvfb.service`. Xvfb `ExecStart` is `/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -nolock -auth /run/kronika-capture/Xauthority`; the exec tokens do not contain `-ac`. VNC is `-localhost` on port 5900. noVNC is `127.0.0.1:6080` to `127.0.0.1:5900`. Both view units set `RuntimeMaxSec=1800`, `Restart=no`, and have no `[Install]`. Bridge and runner `StateDirectoryMode=0700`. Xvfb `RuntimeDirectoryMode=0700`. Runner `ExecStartPre` creates profile and staging with mode 0700. All five units set `UMask=0077`. Bridge and runner `LoadCredential=` is unchanged. Bridge and runner place `--state-dir` before the subcommand, and those argument lists parse. Xvfb, VNC, and noVNC do not invoke `kronika-capture`. |
| 2. F-HOST-01 closure | PASS | Corrected bridge and runner argument lists parse with `kronika_capture.cli.build_parser()`. The parent order, option after the subcommand, exits 2 for both. The regression test passes on the candidate units and raises `AssertionError` on the parent unit text. |
| 3. F-HOST-02 closure | PASS | The Xvfb command contains `-nolock`, matching the classified command and the classified `-help` wording that `-nolock` disables locking. `ReadWritePaths=/tmp/.X11-unix /run/kronika-capture` is unchanged from the parent. Xvfb and runner do not set `PrivateTmp`. A live corrected Xvfb was not started. |
| 4. Credential boundary | PASS | `paths.py`, `bridge/auth.py`, and `cli.py` have an empty diff from the parent. Credential-wins, unset-directory fallback, missing-directory mint (mode 0600, length 43, parent 0700), empty/spaces/4097/non-UTF-8/NUL/newline rejection without minting, a 4096-byte accept, symlink refusal, and directory-symlink use of the regular target all matched. Absent Origin 200; empty and foreign Origin 403; exact loopback Origin 200 with the origin echoed; wrong Host 403; wrong token and empty expected token 401. Comparison in `check_request` is `hmac.compare_digest`. Launcher argv contained the credential directory and the explicit Chromium path, and did not contain the synthetic marker, `--no-sandbox`, or `--stealth`. A relative Chromium path is rejected. |
| 5. Release helper | PASS | `framenest_release.py` has an empty diff from the parent. Candidate and parent capture code trees match, runtime-contract hashes match, and unit-contract hashes differ (`c2f31eac9c042e23ac9beebb8af648baaf16ef94e6f5106924591110cb88abaa` versus `4d4566c13a23f6dd642931f7cd9a2e618726a5a8a84fcc097daf99b459b66759`). Protocol remains `1`. A manifest carrying the parent unit hash is refused with exit 3 before any restart. Activate and rollback-capture keep verify, drain, refuse, brake, one atomic capture switch, one runner restart, and no second restart. Web rollback restarts only `framenest.service` and reports `capture_release: absent`. Deploy with revisions 0028 and 0029 exits 13 with `migration-required` before either pointer switch or either restart. |
| 6. Correction containment | PASS | `git diff --name-only` from the parent to the candidate is exactly the four allowed paths. Capture source, helper, AP, and documentation diffs against those owners are empty. The declared route passed. The new regression fails on the reconstructed parent order and passes on the candidate. The leak hunt found no secret value. |
| 7. Evidence consistency | PASS | The corrected ExecStart lines are the classified corrected commands. The parent ExecStart lines are the classified failing order and the Xvfb command without `-nolock`. Both observed failures are explained by those parent lines and are absent from the candidate. The live corrected Xvfb under the unit remains unobserved. |

## F-HOST closure

F-HOST-01: verified-closed on the candidate sources. Parser exit for the old order is 2. Parser acceptance of the corrected order was observed for both units. The regression test is causal: it passes against the candidate files and fails against the parent files reconstructed under the temporary root.

F-HOST-02: verified-closed as a source strategy. The unit uses `-nolock`, keeps the narrow `ReadWritePaths`, and does not set `PrivateTmp` on Xvfb or the runner. Closure of the live process under systemd is not claimed.

## Control matrix

Positive controls, from `/home/agile/Projects/framenest`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976
```

Result: exit 0. `ap project check --baseline: PASS`. Non-failing warning that inherited environment classes were sanitized (`LD_LIBRARY_PATH`, `SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PROMPT_COMMAND`, `APPDIR`, `APPIMAGE`, `PATH`).

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Result: exit 0. `197 passed in 4.64s`.

Negative and adversarial controls used one temporary root, `/tmp/kronika-one-product-s3-reacceptance`, mode 0700, not a symlink. The probe imported the candidate. SSH was not executed. `git ls-remote` was not executed. The deploy probe returned a local string for that argv so the helper could reach the schema gate; that string is not evidence of public `main`. Gate scripts were the production `python3 -c` sources with the hardcoded capture paths replaced by paths inside the temporary root. The readiness script's `subprocess.run` was replaced by a stub that returned a chosen `ActiveState`. `systemctl` was not executed.

Unit directive matrix:

| Unit | Restart | Requires | LoadCredential | PrivateTmp | Install | Other required property |
| --- | --- | --- | --- | --- | --- | --- |
| xvfb | no | none | none | absent | yes | `-nolisten tcp`, `-nolock`, `-auth`, runtime mode 0700, no `-ac` token |
| bridge | on-failure | none | token absolute path | true | yes | state mode 0700, `--state-dir` before `bridge run`, port 8765 |
| runner | no | xvfb only | token absolute path | absent | yes | state mode 0700, profile and staging mode 0700, `--state-dir` before `runner run` |
| vnc | no | xvfb | none | absent | no | `-localhost`, port 5900, `RuntimeMaxSec=1800` |
| view | no | none | none | absent | no | `127.0.0.1:6080` to `127.0.0.1:5900`, `RuntimeMaxSec=1800` |

CLI-parse matrix: bridge and runner corrected argv parse with `state_dir=/var/lib/kronika-capture`, command `bridge` or `runner`, port 8765, runner `headed=true`. Old argv exit codes are 2 and 2. No other capture `ExecStart` invokes the `kronika-capture` executable.

Credential probes, synthetic files only: credential-wins with no state file; unset directory returns the state token; missing directory mints mode 0600 length 43; empty, spaces, 4097 bytes, non-UTF-8, NUL, and internal newline return empty and do not mint; 4096 bytes is accepted; a `token` symlink is ignored; a `token` symlink with no state token then mints; a symlink `CREDENTIALS_DIRECTORY` uses the regular file inside the target. Auth results are those in claim 4. Launcher argv has the credential directory and the Chromium path, and lacks the marker.

Helper probes, one fake runner, no network:

| Case | Exit | Runner restarts | Order observed |
| --- | --- | --- | --- |
| activate, idle, ready | 0 | 1 | work, brake, switch, restart, readiness; both SHAs |
| rollback-capture, idle, ready | 0 | 1 | same; no web restart; no web switch |
| live | 22 | 0 | work only |
| paused | 22 | 0 | work only |
| queued, queued, then clear | 0 | 1 | three work polls, then brake, switch, one restart |
| queued and drain deadline 0 | 22 | 0 | work only |
| brake refuse | 23 | 0 | work, brake; no switch |
| protocol 9 on the current capture manifest | 3 | 0 | no work and no restart |
| installed SHA mismatch | 3 | 0 | no restart |
| manifest tree mismatch | 3 | 0 | no restart |
| manifest parent unit hash | 3 | 0 | no work and no restart |
| readiness failed, browser_unavailable, or needs_admin | 16 | 1 | one restart, one readiness poll, both SHAs |
| readiness starting then ready | 0 | 1 | two readiness polls, one restart |
| restart command fails | 15 | 1 | one restart, no readiness poll, both SHAs |
| web rollback | 0 | 0 | one `framenest.service` restart; capture switch absent; `capture_release: absent` |
| status, capture link absent | 0 | 0 | `capture_release: absent` and the web SHA |
| deploy, revisions 0028 and 0029 | 13 | 0 | `migration-required`; no web switch, no capture switch, no restart |

Work-gate classifications, synthetic SQLite journals: absent `none`; offered, running, and queued-plus-running `live`; needs_admin job and needs_admin service `paused`; queued `queued`; done `none`; symlink to a real journal `unverifiable`.

Brake-gate classifications: missing directory `ok`; directory without metadata, elapsed about 299 seconds, future timestamp, boolean, missing field, oversized metadata, and a metadata symlink `refuse`; elapsed 300000 ms and about 301 seconds `ok`. The comparison is strict `< 300000`.

Readiness-script classifications with a stubbed active state: failed unit `failed`; active plus ready `ready`; needs_admin `needs_admin`; browser_unavailable `browser_unavailable`; active plus missing journal `starting`; activating `starting`.

Leak hunt across the 20 S3 paths and the four correction paths: no private-key block and no secret value. Matches for `Bearer `, `0.0.0.0`, `PartOf=`, `password=`, `api_key=`, `--no-sandbox`, and `--stealth` are the log denylist, prohibition text, or negative assertions in `framenest_release.py`, `docs/UBUNTU_NUC_DEPLOYMENT.md`, `test_kronika_capture_services.py`, and `test_systemd_credentials.py`.

## Findings

Findings: none.

## Containment and cleanup

```text
Temporary root: /tmp/kronika-one-product-s3-reacceptance
Owner: this Worker
Mode: 0700
Contents class: synthetic probe script, JSON summary, disposable credential files, SQLite journals, brake metadata, reconstructed parent unit text
Cleanup owner: this Worker
Cleanup outcome: removed
```

Hashes recorded before removal:

```text
probe.py       36adc6666863bd51c86e395cf276980a4d68dbf1417f9114703f7d2901bf7396
probe-out.json 74a8d6b0c515809e7641ead8eee72bf081d079b289fbf03bc6a1be2303a5645f
```

The repository index remained clean after removal. HEAD remained the candidate. No release directory, credential, or host path outside the temporary root was created. No fetch, stage, commit, or push was performed. Meta was not committed by this Worker; this report is the authorized trace write.

## Residual risk and limitations

- A live corrected Xvfb under `kronika-capture-xvfb.service` was not started. The host retry remains the check for that process. The `-nolock` meaning used here is the classified host `-help` evidence.
- Public `refs/heads/main` was not re-read from the network. Local `main` and `origin/main` match the stated parent. The deploy probe's `ls-remote` result was a local stub.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` still does not name `-nolock`. That file is outside the correction delta. The sentence that Xvfb does not disable access control remains true because the unit does not use `-ac`. Recorded as a ledger candidate, not a failed claim.
- The first probe run failed before JSON output because an inherited `LD_LIBRARY_PATH` broke the venv interpreter, and a later run failed on a probe defect that treated the Xauthority path as a CLI invocation. Both were corrected in the probe and rerun. See near-misses.

Changed files: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/11_report_00.md` only, containing this report. The candidate tree is unchanged.

Git result: no fetch, stage, commit, or push.

Smallest next step: publish the corrected commit `94e605c17b881461fad3e22fd8c7fca32cb93976`, then run the host retry of the corrected units.

```text
Orchestration critique:
MEASURED: the owner map calls 26d28b16..c975aba a 20-path range; git diff --name-only on that range is 80 paths across five commits. The 20-path S3 diff is 82a6a59803ed8830c19e51cd8f9bc1665c28a975..c975aba14840b97944aecc655907e3abc370341d. Effect: none on this verdict; the leak hunt used the 20-path commit. Smallest correction: cite 82a6a598 as the S3 parent in the owner map.
LEAD: the deployment doc does not name -nolock; cheapest useful check is an Orchestrator decision, before the host retry, on whether one sentence is required.
Resolved Execution Issues / Near-Misses: three probe-side misses, repository unchanged. Inherited LD_LIBRARY_PATH made .venv/bin/python fail while importing encodings; the probe was rerun with that variable unset. The first CLI scan matched the substring kronika-capture inside the Xauthority path and aborted on Xvfb; the scan was limited to an executable token and rerun. The readiness stub was inserted at the wrong indentation and raised IndentationError; the stub was moved above the script and rerun. The saved JSON is from that successful run.
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
```
