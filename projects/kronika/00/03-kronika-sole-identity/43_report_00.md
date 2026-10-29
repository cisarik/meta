### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 43
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6COMP
status: PASS
Phase-qualified result: not-applicable
Start commit: e9413dff98605443e7d17557f498c87433c93e92
End commit: e9413dff98605443e7d17557f498c87433c93e92
Report justification: new-evidence
Logical-whole closure: not-closed

Changed files: none. This session did not edit the repository. The candidate under review is the existing local commit named below.
Validation: gates re-derived; ingress and environment matrices reviewed against the candidate source; mutation demonstrations re-executed; focused module, retention module, and full suite re-run through the declared AP route.
Git result: no fetch, stage, commit, push, checkout, or other Git write. End HEAD equals start HEAD. Working tree clean at start and after the suites.
Deviations, risks, missing evidence: no blocking finding. Non-blocking residuals are in section 7. The parent-suite count was not re-executed.
Smallest next step: under a separate grant, archive the failed C6 journal and close C6. This audit does not authorize that archive, a push, or host contact.

## 1. Identity, scope, and gate verification

Candidate commit `e9413dff98605443e7d17557f498c87433c93e92`, parent `fcde631047650d1ff0a84b84bf185b54d6d11ba5`, subject `Fix C6 ingress spelling and environment permission parity`. Standalone checkout at `/home/agile/Projects/kronika` (`.git` is a directory). Branch `main`. `origin` is `https://github.com/cisarik/kronika`. Local `origin/main` is the parent, so this checkout is one commit ahead. That difference is the unpublished candidate named by the prompt. Working tree clean (`git status --porcelain=v1` empty) at the start and after the suites.

Containing-repository `.ap` gitlink and `.ap` HEAD are both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `./.ap/ap doctor` returned `ap doctor: PASS` and `resolved governing variant: stable`. `./.ap/ap project check --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5` returned `ap project check --baseline: PASS` on CPython 3.13.

The commit touches exactly two paths:

- `deploy/ubuntu/kronika_release.py` (+106/−24 in the combined stat, 551 insertions and 24 deletions across both files)
- `tests/contract/test_kronika_identity_migration.py` (464 insertions, 5 deletions)

No documentation, configuration, dependency, lockfile, Alembic revision, AP gitlink, or retention-ledger path is in the commit. The five deleted test lines replace a fixed `READONLY_ENVIRONMENT` return with `self.environment_raw`, and replace a `chown root:root` simulator branch with a general `sudo -n chown <owner>:<group>` branch. No test function was removed.

The engine diff is confined to the evidence field on `MigrationObservation` and `MigrationPlan`, `parse_environment_file_evidence`, `environment_file_ownership`, plan-digest binding, the post-move `chown`/`chmod`/verify in `transform_environment`, the two-spelling guard and mirrored replacement, the verifier’s use of `tailscale_unix_targets`, the classifier’s use of that same helper, and the observation read that hashes the raw file. `MIGRATION_PHASES`, `_MIGRATION_PHASE_METHODS`, `migration_journal_payload`, `recover_pre_write`, `recover_post_write`, `cmd_remote_tailscale_replace`, `cmd_remote_rename_group`, `MIGRATION_PLAN_VERSION`, and `MIGRATION_JOURNAL_VERSION` do not appear in the diff. Phase order, phase names, the method map, journal and receipt shapes, and recovery semantics are unchanged. The correction prompt’s negative authority (no other path, no document, no dependency, no publication) is honored by the commit contents.

The parent full-suite figure of 4901 was not re-executed. Checking out the parent is outside this grant. `ap project check --baseline` validates the execution contract at that commit; it does not replay the suite. The candidate results in section 6 match the claimed candidate gates. The 54-test increase from 4901 to 4955 equals the new `test_c6_completion_*` parametrization, and the diff removes no test function.

## 2. Ingress spelling and refusal matrix

`tailscale_unix_targets` is the single ordered pair `(unix+http://<socket>, unix:<socket>)`. The classifier, the replace guard, and the verifier all use it.

| Input | Result |
| --- | --- |
| `unix:<old>` | Classified former. One `sudo -n tailscale serve --bg unix:<new>`. Return `{"replaced": 1, "handler_count": 2}` with the unrelated HTTP handler preserved. No `reset`. Verifier accepts. |
| `unix+http://<old>` | Same shape, mirrored to `unix+http://<new>`. |
| Foreign HTTP, foreign socket, empty proxy, `unix://<old>`, `unix:<old>.other`, `unix+http://<old>/child`, and the same near-misses on the new socket | `old_handlers == []`. Replace raises `existing ingress handler is not uniquely identifiable`, `EXIT_MIGRATION`. No `--bg`. Verifier raises `ingress replacement did not verify`. |
| Mixed duplicate `unix:<old>` and `unix+http://<old>` | `old_handlers == [0, 1]`. Same unique-handler refusal. No `--bg`. |
| Zero handlers | `{"replaced": 0, "handler_count": 0}`. No `--bg`. With plan count 0, verify runs the health command and does not query Serve. |
| Forged `old_handlers: [0]` whose target is `unix:/foreign.sock` | Guard raises `existing ingress handler target is unexpected`, `EXIT_MIGRATION`, before any SSH call. |
| Mounts `…:443/other`, `…:80/`, and empty | `cmd_remote_tailscale_replace` still raises `ingress handler mount is not the documented default`, `EXIT_MIGRATION`. That builder is unchanged and still emits only `tailscale serve --bg <target>`. |

Return shapes `{"replaced": 0, "handler_count": 0}` and `{"replaced": 1, "handler_count": <count>}` are unchanged.

Places the three sites can disagree:

- The verifier accepts either new spelling. The guard emits exactly the mirrored one. A host that ended on the other new spelling would still verify. That is the specified verifier rule. `fixed-replacement` is caught by the command assertion, which the re-run printed as `exact mirrored target assertion failed`.
- The classifier matches `OLD_WEB_LAYOUT.socket_path`. The guard matches `plan.old_layout.socket_path`. `select_web_layout` returns the layout object from `WEB_LAYOUTS`, so a production observation uses the same socket. A constructed plan whose old socket differs fails closed: the live former socket is either an unexpected target or not classified as the single former handler.
- `verify_ingress` returns immediately when `plan.tailscale_handler_count == 0` and does not read Serve. `replace_tailscale_handler` ignores that stored count and acts on a fresh read. If the plan recorded zero handlers and, later in the apply, Serve has exactly one former handler, the guard issues one `--bg` and the verifier does not read the result back. The command’s non-zero exit still raises. The live-empty read remains a no-op. This is non-blocking: it needs the ingress set to change after the apply-start digest gate, and the live host’s plan count was not zero.

An out-of-range forged index is not a parser output. `targets[index]` would raise `IndexError`, and `run_migration_apply` catches `ReleaseError` only. Untested, non-blocking.

## 3. Environment parity, evidence binding, and fail-closed behavior

Live shape `root:<former group>:640`, `root:root:640`, and `operator:operators:600` install with the observed owner, group, and mode. The old file is unchanged. The staged path is removed by the atomic move. Command order is write, canonical assertion, `mv -T`, `chown`, `chmod`, then `stat`/`sha256sum`. Non-account groups stay on those names through `rename_account`. Mode `600` stays `600`.

Fail-closed, all `EXIT_MIGRATION`, and the content read is not issued when parsing fails first:

- `absent`, `unsafe` → `former environment file is absent|unsafe`
- `query-failed` → `former environment file could not be queried`
- empty, non-octal mode, missing digest, extra trailing text, and owner or group exactly `UNKNOWN` → `former environment file evidence is malformed`

Installed owner, group, mode, or digest mismatch, and installed `absent` / `unsafe` / `query-failed` / empty evidence, raise `installed environment file did not verify` or the malformed-evidence error, after the verify command has run. A file that disappears or whose read returns `query-failed` after a valid evidence line raises before a plan exists.

Staged-write failure and atomic-move failure leave the previous destination bytes in place and issue no `chown` or `chmod`. A canonical-assertion failure does the same and raises `installed environment still carries retired assignments`.

Binding, end to end: `read_migration_observation` stores the evidence string; `build_migration_plan` puts that string in the digest payload; `MigrationPlan.payload()` repeats it; `migration_plan_digest` matches `plan.plan_digest`. Changing owner, group, mode, or the 64-hex digest produces a different digest (five distinct digests in the binding test). Apply rebuilds the observation and refuses with `preflight digest does not match the current migration plan` when the evidence string drifts. The source digest is `sha256(environment_source)`, the SSH return of `sudo -n cat` before `_require_query_result` strips it. Appending a newline to the runner’s file body raises `former environment file content did not verify`. The real-shell evidence script, against `b"synthetic\n"`, parses mode `640` and the SHA-256 of those bytes, including the newline.

The plan digest binds the raw evidence string and the transformed-body hash. That covers owner, group, mode spelling, and the raw source digest. It correctly does not bind the post-rename group name: preflight requires the canonical account, user and group, to be absent, so that name is not an observable input. It does not bind ACLs or xattrs. It does not bind ingress target spellings, only the two handler counts; socket identity is re-checked at replace time.

## 4. D-3 phase-order verdicts

`MIGRATION_PHASES` places `transform-environment` before `preserve-ancillary`, `prepare-release-environment`, and `rename-account`. `rename_account` runs `sudo -n groupmod -n kronika framenest` and then `usermod -l`. `groupmod -n` changes the name and keeps the GID. The simulator does the same, and rewrites stored group names that still say `framenest`. `cmd_remote_assert_account_renamed` checks that the UID and primary GID are the planned values.

Preflight refuses when `getent` shows the canonical user or group already present (`canonical web account already exists`). `chown root:kronika` inside `transform_environment` cannot succeed on a host that passed that gate. Applying the observed group name, then letting `groupmod` canonicalize it, is the sequence that can run.

Dispositions:

- Live shape `root:framenest:640`. No parity gap. The file is installed `root:framenest:640` and, after the GID-preserving rename, reads as `root:kronika:640`. Mode `640` keeps the group-read bit. The default account’s primary GID is that group’s GID, so the renamed service account can read it. The separate primary-GID test shows a file grouped on the account group stays on that GID when the user’s primary GID is something else; membership follows the GID `groupmod` preserves.
- Non-account groups. No parity gap. `root:root:640` and `operator:operators:600` are copied exactly. The rename rewrites only the former account group name. Access is not widened.
- Former-account-owned file. Fail-closed-correct. `environment_file_ownership` raises `environment file owner cannot be preserved`, `EXIT_MIGRATION`, during plan build, before a write. The observed owner name cannot remain after `usermod -l`; accepting it would make the renamed service account the owner. That is a different permission outcome from the operator-owned `/etc/framenest` contract. The live file was root-owned. This is not a legitimate shape the migration has to carry.

The phase-order interpretation is confirmed. It does not remain an open design assumption.

## 5. Mutation-probe results

`test_c6_completion_mutation_demonstrations` compiles one altered method with `exec` into a scratch module and patches `RemoteMigrationHost`. It reads `kronika_release.py` and does not write it. The tree was clean after the run. Re-run: 5 passed in 0.60s. Printed outcomes:

| Mutation | Test | Observed outcome |
| --- | --- | --- |
| `old-only-guard` | `test_c6_completion_ingress_round_trip("unix:")` | `spurious refusal, EXIT_MIGRATION`; regression detected |
| `fixed-replacement` | same | `exact mirrored target assertion failed`; regression detected |
| `no-ownership` | `_assert_environment_parity` | `installed metadata mismatch, EXIT_MIGRATION`; regression detected |
| `no-mode` | same | `installed metadata mismatch, EXIT_MIGRATION`; regression detected |
| `no-verification` | `test_c6_completion_environment_installed_mismatch_refuses("unsafe")` | `unsafe installed evidence accepted; DID NOT RAISE`; regression detected |

Additional probe, static, not executed. A new in-memory mutation cannot be compiled through `test` or `test-focus` without a repository edit or a Python invocation outside those operations. Traced input: plan handler count 0, live Serve status one `unix:` former handler. `replace_tailscale_handler` returns `{"replaced": 1, ...}` and issues one `--bg unix:<new>`. `verify_ingress` returns at `if self.plan.tailscale_handler_count == 0` without a Serve read. This is the disagreement in section 2, not a failed named mutation.

## 6. Checks and Part A / Part B / Part C

All three runs used `./.ap/ap exec --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5`.

| Check | Result | Elapsed |
| --- | --- | --- |
| `test-focus -- tests/contract/test_kronika_identity_migration.py -q -p no:cacheprovider --tb=line` | 285 passed, 0 failed | 1.46s |
| `test-focus -- tests/contract/test_kronika_identity_retention.py -q -p no:cacheprovider --tb=line` | 15 passed, 0 failed | 0.35s |
| operation `test` | 4955 passed, 8 skipped, 3 warnings, 0 failed | 689.12s |

No difference from the claimed candidate gates 285, 15, and 4955/8/3/0. The 8 skips are the real-tool cover workflow (5), real-tool media analysis (2), and the live NVIDIA smoke test (1). The 3 warnings are `PydanticJsonSchemaWarning` on the two health OpenAPI tests and `test_database_path_absent_from_settings_repr_logs_api_and_openapi`.

Part A. The retention ledger is not in the candidate diff. An awk count of the pinned hashes in `tests/contract/test_kronika_identity_retention.py` is 86 `FROZEN_DOCUMENT_SHA256` entries and 36 `FROZEN_ALEMBIC_SHA256` entries. The green retention run executes `test_frozen_adr_and_host_document_bytes_are_unchanged`, `test_frozen_adr_and_host_document_set_is_complete`, `test_frozen_alembic_revision_bytes_are_unchanged`, and `test_frozen_alembic_revision_set_is_complete`, so those pins match the tree bytes and the on-disk sets.

Part B. The basename frozenset lists 20 paths, from `deploy/systemd/framenest-ai-credential-nvidia-nim.conf` through `scripts/operator/network/framenest_nuc_worker_gate.fish`. The green run executes `test_framenest_basename_path_ledger_matches_exactly`.

Part C. The candidate diff’s added and removed lines contain no case-insensitive `framenest` literal (`NO_FRAMENEST_LITERAL_LINES`). No path was added or removed. The retention file itself is unmodified, so its Part C scalars are the same pins. The green run executes the per-tree file counts, per-tree occurrence counts, content-path membership, environment-prefix counts, bare-prefix counts, and console-script count. A green result against an unmodified ledger, plus a zero literal delta in the only two changed paths, is the no-movement measurement.

## 7. Findings and untested sites

No blocking finding.

Non-blocking:

- Verifier accepts either new spelling; the guard is scheme-exact. Specified.
- Plan count 0 skips ingress readback even if a former handler appears after the apply-start observation. Concurrent change only. Command failure still aborts.
- `cmd_remote_root_file_evidence` decides `absent` and `unsafe` with unprivileged `[ -e ]`, `[ -L ]`, and `[ -f ]`, then reads owner and digest through `sudo`. A parent directory the SSH user cannot search is reported as `absent`. A mode `0640` file in a searchable directory is still visible to `[ -f ]`; the content read is sudo. Outcome is a false refusal, `EXIT_MIGRATION`, not a wrong install. Directory mode was not measured; this grant has no host contact.
- `chown` or `chmod` failure after `mv -T` leaves the new path in place. Write, assertion, and move failures preserve the previous destination. Pre-write recovery does not delete the new environment file. The new service has not started, and the former file is untouched.
- ACLs and xattrs are not copied. The parity contract is owner, group, and mode.
- `read_migration_observation` still stores the stripped body as `environment_text`, as the parent did. The new digest check hashes the unstripped cat stdout. A trailing newline is included in that check and is not passed into the transformer.

Untested, all non-blocking:

- Live Tailscale and a live `chown`/`chmod` on the NUC. Excluded by authority. The host was already completed manually.
- One shell that pairs the evidence script and `cat` on a root-owned `0640` file. The real-shell test covers the evidence script on a user-owned temporary file, with a local `sudo` function. The observation pairing is covered by the in-memory runner.
- Out-of-range `old_handlers` index (`IndexError` outside `ReleaseError`).
- The plan-count-zero readback case, traced statically and not executed.
- Parent-suite execution at `fcde631`.
- Post-move `chown` rollback, ACLs, and an unsearchable parent directory.

## 8. Deviations, risks, missing evidence, and one smallest next step

Deviation: the first focused-suite wrapper exited 1 after pytest had already printed `285 passed in 1.46s`, because the wrapper assigned to zsh’s read-only `status`. The pytest summary is the test result. Later commands used a different variable. No repository change followed.

Risk: the residuals in section 7. None of them reopens the live `unix:` refusal, the `unix+http://` replacement spelling, or the `0600 root:root` install for the live `root:framenest:640` shape.

Missing evidence: no NUC contact, by the grant. Parent suite not re-run. The additional probe was a static trace.

Smallest next step: a separate bounded grant may archive the failed C6 journal and close C6. This report does not perform either.

Resolved Execution Issues / Near-Misses: the focused-suite timing wrapper assigned zsh’s read-only `status` after pytest had printed `285 passed in 1.46s`, so the wrapper exited 1. Cause: `status` is read-only in zsh. Resolution: the pytest line is the module result; retention and the full suite were timed with a different variable and exited 0. Residual risk: none for the recorded counts.

Pre-Existing Failure Classification: none

Orchestration critique:
MEASURED: none
LEAD: `verify_ingress` skips Serve readback when the stored handler count is 0, while `replace_tailscale_handler` will still replace one later live former handler; cheapest useful check is one in-memory case with plan count 0 and a single live `unix:` former handler.

Authority expiry: this terminal report ends the grant. No implementation, correction, commit, push, publication, host contact, or later cut is authorized.