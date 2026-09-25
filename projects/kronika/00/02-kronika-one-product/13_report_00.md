### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 13
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-LOCK-REACCEPTANCE
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: d63d0b725acedf49d1611224c3b5201a90e7ef90
Result evidence: declared route, unit and CLI inspection, synthetic credential and helper probes
Start commit: d63d0b725acedf49d1611224c3b5201a90e7ef90
End commit: d63d0b725acedf49d1611224c3b5201a90e7ef90
Logical-whole closure: not-closed
Report justification: final-acceptance

Actual independence posture: fresh Worker session. This conversation began with the acceptance prompt. It did not implement S3 and did not correct S3. Prior plans, reports, and the classified host evidence were used as evidence. Verdicts below come from this session's inspection, the declared route, and the synthetic probes. No subagent was used. The NUC was not contacted.

## Compact outcome

The corrected candidate closes the Xvfb lock defect in the deployment sources through the documented `/tmp` fallback and keeps the accepted S3 guarantees that this exchange could re-establish. F-HOST-01 stays closed. No blocking finding remains. This report grants no publication, deployment, or host-retry authority. A live corrected Xvfb under the unit was not run.

Requested reasoning: High. Effective reasoning was a full fresh re-audit of the corrected sources. Model identity was not independently attested.

## Identity gate

Observed before probes:

- Checkout `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`, HEAD `d63d0b725acedf49d1611224c3b5201a90e7ef90`, parent `94e605c17b881461fad3e22fd8c7fca32cb93976`, tree `95862a1e012256829ada49ed780ad665cd2aea18`, subject `fix(capture): let the unprivileged Xvfb create its display lock`.
- Index and worktree clean. No index lock.
- Local `main` and `origin/main` both `94e605c17b881461fad3e22fd8c7fca32cb93976`. Remote URL `https://github.com/cisarik/framenest.git`. Public `refs/heads/main` from `git ls-remote` was `94e605c17b881461fad3e22fd8c7fca32cb93976`.
- Governing AP gitlink and detached `.ap` HEAD `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` was not read.
- Report destination was absent. Its resolved path equals `/home/agile/meta/projects/kronika/00/02-kronika-one-product`.

After probe cleanup, HEAD and tree were unchanged and the worktree was clean.

## Acceptance and Correction Record

```text
Acceptance candidate: d63d0b725acedf49d1611224c3b5201a90e7ef90
  (tree 95862a1e012256829ada49ed780ad665cd2aea18, branch feat/kronika-one-product,
   parent 94e605c17b881461fad3e22fd8c7fca32cb93976)
Acceptance owner map: the S3 slice paths (20 paths, 82a6a598..c975aba); the first
  correction delta (4 paths, c975aba..94e605c); the second correction delta (3 paths,
  94e605c..candidate: kronika-capture-xvfb.service, docs/UBUNTU_NUC_DEPLOYMENT.md,
  tests/contract/test_kronika_capture_services.py); accepted plan sections 7.2-7.3 and
  the S3 row; reports 04_report_00, 08_report_00, 10_report_00, 10_report_01,
  10_report_02, 10_report_03; the classified host evidence in the prompt
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused route; synthetic temporary probe state under /tmp/kronika-one-product-s3-lock-reacceptance;
  this terminal report
Acceptance risk claims: the seven fixed claims; all seven PASS
Acceptance control matrix: completed below, with directly observed results
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 2
Automatic corrections used: 2
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
Acceptance outcome: PASS; no blocking finding remains
```

## Per-claim verdicts

| Claim | Verdict | Observed |
| --- | --- | --- |
| 1. Unit directives | PASS | All five units parsed. None contain `PartOf=`, `BindsTo=`, `ConsistsOf=`, or `PropagatesStopTo=`. Xvfb and runner `Restart=no`. Bridge `Restart=on-failure`. Runner `Requires=` is only `kronika-capture-xvfb.service`. Xvfb `ExecStart` is `/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -auth /run/kronika-capture/Xauthority`. The exec tokens contain `-nolisten tcp` and `-auth`, and contain neither `-nolock` nor `-ac`. `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture` with `ProtectSystem=strict`. Xvfb and runner have no `PrivateTmp` key. VNC is `-localhost` on port 5900. noVNC is `127.0.0.1:6080` to `127.0.0.1:5900`. Both view units set `RuntimeMaxSec=1800`, `Restart=no`, and have no `[Install]`. Bridge and runner `StateDirectoryMode=0700`. Xvfb `RuntimeDirectoryMode=0700`. Runner `ExecStartPre` creates profile and staging with mode 0700. All five units set `UMask=0077`. Bridge and runner `LoadCredential=` is `token:/etc/kronika-capture/credentials/kronika-bridge-token`. Bridge and runner place `--state-dir` before the subcommand, and those argument lists parse. |
| 2. F-HOST-01 closure | PASS | Corrected bridge and runner argument lists parse with `kronika_capture.cli.build_parser()`. The old order exits 2 for both. The grandparent unit order, option after the subcommand, also exits 2 for both. The regression test passes on the candidate. |
| 3. F-HOST-02 fallback | PASS | `-nolock` is absent from the Xvfb `ExecStart`. The parent `ReadWritePaths` list is `/tmp/.X11-unix /run/kronika-capture`. The candidate list adds only `/tmp` and removes nothing. `ProtectSystem=strict` remains. Xvfb and the runner do not gain `PrivateTmp`. `-auth` remains. `-ac` remains absent. A live corrected Xvfb was not started. |
| 4. Credential boundary | PASS | `src/kronika_capture` has an empty diff from the parent. Credential-wins, unset-directory fallback, missing-directory mint (mode 0600, length 43, parent 0700), empty/spaces/4097/non-UTF-8/NUL/newline rejection without minting, a 4096-byte accept (length 4096, state file not created), symlink refusal, and directory-symlink use of the regular target all matched. Absent Origin with the synthetic token is 200. Empty and foreign Origin are 403. Exact loopback Origin is 200 and the origin is echoed. Wrong Host is 403. Wrong token and empty expected token are 401. `check_request` uses `hmac.compare_digest`. Launcher argv contained the credential directory and the explicit Chromium path, and did not contain the synthetic marker, `--no-sandbox`, or `--stealth`. A relative Chromium path is rejected. |
| 5. Release helper | PASS | `deploy/ubuntu/framenest_release.py` has an empty diff from the parent. Candidate and parent capture code trees match (`977465503254fe6cdf31673b7e107b9e0487ffe2`). Runtime-contract hashes match (`691500d51dc9a2f3966de144c3592b0b984e8b2753cca4d599aee3793ee35e6b`). Unit-contract hashes differ (`e61dc70a80fef5df8fce6b8bd922656585e22aafabef8d4cc9a216042b680bb5` versus `c2f31eac9c042e23ac9beebb8af648baaf16ef94e6f5106924591110cb88abaa`). Protocol remains `1`. A manifest carrying the parent unit hash is refused with exit 3 before any work gate or restart. Activate and rollback-capture keep verify, drain, refuse, brake, one atomic capture switch, one runner restart, and no second restart. Web rollback restarts only `framenest.service` and reports `capture_release: absent`. Deploy with revisions 0028 and 0029 exits 13 with `migration-required` before either pointer switch or either restart. |
| 6. Correction containment | PASS | `git diff --name-only` from the parent to the candidate is exactly the three allowed paths. Capture source, helper, and AP diffs against those owners are empty. The declared route passed, 197 tests. The updated lock assertion fails on the reconstructed parent unit and passes on the candidate. The CLI-parse regression fails on the old order and passes on the candidate order. The documentation sentence is present, and the access-control sentence remains. The leak hunt found no secret value. |
| 7. Evidence consistency | PASS | The candidate Xvfb command is the command recorded in `10_report_03`. The parent command still contains `-nolock` and the narrower `ReadWritePaths`. The grandparent bridge and runner commands still place `--state-dir` after the subcommand and still exit 2. Both classified failures are explained by those earlier lines and are absent from the candidate. The live corrected Xvfb under the unit remains unobserved. |

## Xvfb lock strategy closure

F-HOST-01 remains verified-closed on the candidate sources. Parser exit for the old order is 2. Parser acceptance of the corrected order was observed for both units. The regression test passes against the candidate files.

F-HOST-02 is verified-closed as a source strategy. The unit no longer depends on `-nolock`. The lock path named by the classified host evidence, `/tmp/.tX99-lock`, sits under `/tmp`, and `/tmp` is now the only path added to `ReadWritePaths`. `ProtectSystem=strict` remains, so the rest of the hierarchy stays read-only except the pre-existing writable entries and the API filesystems that `ProtectSystem=strict` already leaves outside that mount. `-auth` still names the Xauthority file. `-ac` is absent. Closure of the live process under systemd is not claimed.

The documentation sentence is present: Xvfb writes its display lock under `/tmp`, so the unit keeps `/tmp` writable while the rest of the filesystem stays read-only. The sentence that Xvfb does not disable access control remains. The deployment doc does not name `-nolock`.

## Control matrix

Positive controls, from `/home/agile/Projects/framenest`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90
```

Result: exit 0. `ap project check --baseline: PASS`. Non-failing warning that inherited environment classes were sanitized (`LD_LIBRARY_PATH`, `SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PROMPT_COMMAND`, `APPDIR`, `APPIMAGE`, `PATH`).

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Result: exit 0. `197 passed in 4.56s`.

Negative and adversarial controls used one temporary root, `/tmp/kronika-one-product-s3-lock-reacceptance`, mode 0700, not a symlink. The probe imported the candidate. SSH was not executed. `systemctl` was not executed. Gate scripts were the production `python3 -c` sources with the hardcoded capture paths replaced by paths inside the temporary root. The readiness script's `subprocess.run` was replaced by a stub that returned a chosen `ActiveState`. The deploy, web-rollback, and status probes returned a local string for `git ls-remote`; that string is not evidence of public `main`. Public `main` was read separately, as recorded in the identity gate.

Unit directive matrix:

| Unit | Restart | Requires | LoadCredential | PrivateTmp | Install | Other required property |
| --- | --- | --- | --- | --- | --- | --- |
| xvfb | no | none | none | key absent | yes | `-nolisten tcp`, `-auth`, no `-nolock`, no `-ac`, runtime mode 0700, `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture`, `ProtectSystem=strict` |
| bridge | on-failure | none | token absolute path | true | yes | state mode 0700, `--state-dir` before `bridge run`, port 8765 |
| runner | no | xvfb only | token absolute path | key absent | yes | state mode 0700, profile and staging mode 0700, `--state-dir` before `runner run` |
| vnc | no | xvfb | none | key absent | no | `-localhost`, port 5900, `RuntimeMaxSec=1800` |
| view | no | none | none | key absent | no | `127.0.0.1:6080` to `127.0.0.1:5900`, `RuntimeMaxSec=1800` |

Xvfb strategy: candidate assertion passed. The same assertion raised `AssertionError` on the parent unit text reconstructed with `git show`. The parent list differs by the absence of `/tmp` only. Parent `ExecStart` still contains `-nolock`.

CLI-parse matrix: bridge and runner corrected argv parse with `state_dir=/var/lib/kronika-capture`, command `bridge` or `runner`, port 8765, runner `headed=true`. Old argv exit codes are 2 and 2. Grandparent unit argv exit codes are 2 and 2. Xvfb, VNC, and noVNC do not invoke the `kronika-capture` executable. The regression test passed.

Credential probes, synthetic files only: results are those in claim 4. The 4096-byte accept was confirmed in a second measurement after the saved JSON: read length 4096, loaded length 4096, state file absent.

Helper probes, one fake runner for capture transitions, with real read-only `git` for capture identity, and the existing contract fake runner for web rollback, status, and deploy. No network from those runners.

| Case | Exit | Runner restarts | Order observed |
| --- | --- | --- | --- |
| activate, idle, ready | 0 | 1 | work, brake, switch, restart, readiness; both SHAs |
| rollback-capture, idle, ready | 0 | 1 | same; no web restart; no web switch |
| live | 22 | 0 | work only |
| paused | 22 | 0 | work only |
| queued, queued, queued, then clear | 0 | 1 | three work polls, then brake, switch, one restart |
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

Brake-gate classifications: missing directory `ok`; directory without metadata, elapsed 299 seconds, future timestamp, boolean, missing field, oversized metadata, and a metadata symlink `refuse`; elapsed 300000 ms and 301 seconds `ok`. The comparison in the gate source is `(now - started) < limit` with limit 300000.

Readiness-script classifications with a stubbed active state: failed unit `failed`; active plus ready `ready`; needs_admin `needs_admin`; browser_unavailable `browser_unavailable`; active plus missing journal `starting`; activating `starting`.

Leak hunt across the union of the S3 slice and both correction deltas, 20 paths: no private-key block and no secret value. Matches for `Bearer `, `0.0.0.0`, `PartOf=`, `password=`, `api_key=`, `--no-sandbox`, `--stealth`, and `-nolock` are the log denylist, prohibition text, or negative assertions in `framenest_release.py`, `docs/UBUNTU_NUC_DEPLOYMENT.md`, `test_kronika_capture_services.py`, and `test_systemd_credentials.py`.

## Findings

Findings: none.

## Containment and cleanup

```text
Temporary root: /tmp/kronika-one-product-s3-lock-reacceptance
Owner: this Worker
Mode: 0700
Contents class: synthetic probe script, JSON summary, disposable credential files, SQLite journals, brake metadata, reconstructed parent unit text used only in memory
Cleanup owner: this Worker
Cleanup outcome: removed
```

Hashes recorded before removal:

```text
probe.py       bba8537ec7e52a1aea8f96f6ca0e2c74f773129923a696509ef23d55953e3bb0
probe-out.json 1db2a5dd662e313fa25ecb4c672f7e388f81459a54f79416071323ad91d3cd88
```

The repository index remained clean after removal. HEAD remained the candidate. Tree remained `95862a1e012256829ada49ed780ad665cd2aea18`. No release directory, credential, or host path outside the temporary root was left behind. No fetch, stage, commit, or push was performed. Meta was not committed by this Worker; this report is the authorized trace write.

## Residual risk and limitations

- A live corrected Xvfb under `kronika-capture-xvfb.service` was not started. The host retry remains the check for that process. The lock path under `/tmp` is taken from the classified host evidence and from the unit's new `ReadWritePaths` entry.
- `ProtectSystem=strict` still leaves `/dev`, `/proc`, and `/sys` outside the read-only mount, and the parent unit already allowed `/run/kronika-capture`. The second correction adds `/tmp` only.
- The deploy, web-rollback, and status probes stub `git ls-remote`. Public `refs/heads/main` was read directly and matches the parent. The second correction is not on public `main`.
- The saved probe JSON records the first absent-Origin call, which omitted the token header. The claim uses the corrected call. See near-misses.

Changed files: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/13_report_00.md` only, containing this report. The candidate tree is unchanged.

Git result: no fetch, stage, commit, or push.

Smallest next step: publish the corrected commit `d63d0b725acedf49d1611224c3b5201a90e7ef90`, then run the host retry of the corrected units.

```text
Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: two probe-side misses, repository unchanged. Inherited LD_LIBRARY_PATH made .venv/bin/python fail while importing encodings; the probe was rerun with that variable unset. The declared route had already sanitized that variable. The first absent-Origin call passed an empty header map, so the token was missing and the status was 401; a second call with the synthetic token and origin omitted returned 200. The saved JSON keeps the first call. The claim uses the second observation.
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
```
