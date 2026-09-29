### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 42
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT
status: PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation

Start commit: `0d0d8c88bf88bf8454751a0205bc8652374796c2`
End commit: `665a565bc1279690ce8dacade37103fa3e0aaddc`
Changed files: five allowlisted paths; the NUC worker gate accepts a validated macOS launchd agent only when `gpgconf` is unavailable
Commit and push: one local commit; no push

## Repository re-gate

Verified before any edit. The issuance checkout matched.

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     0d0d8c88bf88bf8454751a0205bc8652374796c2
parent   5843486ddeae13ec5b331f102c5cb595bfa6e386
tree     96adead05beb58f2e282ff77b9e6d29bff2c8298
subject  fix(kronika): serve approved projections on household reads
status   empty (git status --porcelain=v1 --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
```

`42_report_00.md` was absent. Public `main` was not re-queried in this exchange.

Host facts checked without printing the socket or any identity: `gpgconf` is not on `PATH`; `pgrep -x gpg-agent` found no process; `SSH_AUTH_SOCK` is nonempty, absolute, has no `..` segment, is a Unix socket, uid 501, euid 501, mode `0o666`, and `realpath` places it under `/private/var/run/com.apple.launchd.`. `realpath` is `/bin/realpath`, `ssh-add` is `/usr/bin/ssh-add`, and `fish` is `/opt/homebrew/bin/fish`.

## Validation

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2
```

Exit 0 before editing, and exit 0 again before the commit.

Declared route, same baseline:

```text
./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2 --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider
```

Red, unfixed gate, after the tests existed. Exit 1. `3 failed, 57 passed` in 20.78s. The causal test `test_ssh_gate_probe_accepts_validated_darwin_launchd_agent` ran the gate and got stdout `ssh-agent: absent`, return code 1, against expected `ssh-agent: ready` and return code 0. The same absent result failed `test_ssh_gate_probe_accepts_darwin_agent_with_no_identities`. `test_ssh_gate_darwin_fallback_sets_socket_for_ssh_child` saw `SSH_AUTH_SOCK_SET=0`. Negative Darwin cases, the Linux non-activation case, the gpgconf-failure case, and the gpgconf-preferred case already returned the expected absent or ready lines on the unfixed gate.

Green, same command, corrected gate. Exit 0. `60 passed` in 21.35s. One earlier green of the same file, before a quote-only change on the production socket operands, was also `60 passed`. The final run is the committed file.

`git diff --cached --check` produced no whitespace errors. Cached `--stat` was the five paths below. The broad suite was not run. Mullvad egress scripts were not run again as a separate target; they remain covered by this same contract file, which passed.

## Discovery order and validation

`_attach_agent` still calls trusted `gpgconf` first, through the existing `_optional_gpgconf` path. A found `gpgconf` that does not yield a nonempty socket returns absent and does not fall through. The Darwin fallback runs only when that lookup finds no `gpgconf`, and only when `uname -s` from `/usr/sbin:/usr/bin:/sbin:/bin` is exactly `Darwin`. Any other platform, including Linux with `gpgconf` missing, stays `ssh-agent: absent`.

On Darwin the ambient socket is accepted only when all of these hold: `SSH_AUTH_SOCK` is nonempty and absolute, no path segment is `..`, `test -S` says it is a Unix socket, `stat -f %u` matches `id -u`, and `realpath` lies under `/private/var/run/com.apple.launchd.` with a nonempty remainder. `ssh-add -l` runs with stdout and stderr discarded; exit 0 or 1 is a working agent and any other status is refusal. Socket mode is not checked. Success exports that socket on the gate process, which the SSH child inherits, and the probe still prints only `ssh-agent: ready` or `ssh-agent: absent`.

Test hooks are read only when `FRAMENEST_NETWORK_TEST_HOOKS=1`: `FRAMENEST_NETWORK_TEST_UNAME`, `FRAMENEST_NETWORK_TEST_SSH_AUTH_SOCK`, `FRAMENEST_NETWORK_TEST_AGENT_IS_SOCKET`, `FRAMENEST_NETWORK_TEST_AGENT_OWNER_MATCH`, `FRAMENEST_NETWORK_TEST_AGENT_RESOLVED`, and `FRAMENEST_NETWORK_TEST_SSH_ADD_STATUS`. With hooks on and no Darwin values, the platform hook is empty, so the fallback stays inert and does not read the process socket. The production branch does not read those hook names.

## Tests

New or updated cases in `tests/contract/test_operator_network_scripts.py`:

- `test_ssh_gate_probe_accepts_validated_darwin_launchd_agent` — causal regression; failed on the unfixed gate; passed after the fix
- `test_ssh_gate_probe_accepts_darwin_agent_with_no_identities` — `ssh-add -l` status 1 is ready; failed unfixed; passed after
- `test_ssh_gate_probe_rejects_invalid_darwin_agent` — relative path, `..` segment, non-socket, foreign owner, path outside the launchd prefix, `ssh-add` status 2, empty value; each is `ssh-agent: absent` exit 1
- `test_ssh_gate_probe_ignores_darwin_fallback_on_linux`
- `test_ssh_gate_probe_does_not_fall_back_when_gpgconf_fails`
- `test_ssh_gate_probe_prefers_present_gpgconf_over_darwin_fallback`
- `test_ssh_gate_probe_darwin_fallback_inert_without_hook_values`
- `test_ssh_gate_darwin_fallback_sets_socket_for_ssh_child` — child log is `SSH_AUTH_SOCK_SET=1` and the fixture path is absent from output
- `test_ssh_gate_rejects_missing_required_values` — parameterized target, user, identity, and command; the only missing-value case in this file

Final file result: `60 passed`, exit 0. Probe assertions reject any stdout other than the two sanitized status lines before comparing them, so a leaked socket is not echoed as the assertion diff.

## Changed paths

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
scripts/operator/network/README.md
tests/contract/test_operator_network_scripts.py
docs/OPERATOR_NETWORK.md
docs/WORKER_EXECUTION_CONTRACT.md
```

## Commit

```text
SHA      665a565bc1279690ce8dacade37103fa3e0aaddc
parent   0d0d8c88bf88bf8454751a0205bc8652374796c2
tree     043b811cf82b54cff05026a90b3b15ee46609475
subject  fix(operator): discover the macOS launchd ssh agent in the worker gate
status   empty (git status --porcelain=v1 --untracked-files=all)
```

No push, fetch, tag, merge, rebase, reset, restore, checkout, switch, stash, clean, or config write.

## Deviations, risks, and missing evidence

The contract tests simulate Darwin outcomes through hooks. The declared route strips `SSH_AUTH_SOCK` before pytest, so those tests do not open the Cooperator's live agent. `stat -f %u` on a temporary socket matched the euid, and `realpath /var/run` resolved to `/private/var/run`; that check did not use the live socket. This session does not certify the correction and did not run `--probe` against the live agent after the commit.

Requested reasoning: High. Effective reasoning and context capacity were not independently attested.

## Parked-failure classification for the MacBook ambient names

`FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER`, and `FRAMENEST_NUC_SSH_IDENTITY` were nonempty in the operator environment; `FRAMENEST_NUC_SSH_COMMAND` was empty. Classification: test-isolation interference, not a production gate defect. `test_ssh_gate_rejects_missing_required_values` is the only parameterized missing-value case in this file. It now clears those four names on the gate process and expects exit 2 plus the gate's own missing-value line, so an exported operator environment cannot satisfy the omitted argument. Production behavior for present values is unchanged. That removes the ambient-default interference for this file.

The exchange 41 probe result `ssh-agent: absent` is the defect this commit corrects. It is not left parked.

## Smallest next step

A separate fresh focused re-audit of the corrected exact SHA `665a565bc1279690ce8dacade37103fa3e0aaddc`, then publication, then the renewed NUC deployment grant.

## Resolved Execution Issues / Near-Misses

The first declared test run exited 1 with `25 failed, 35 passed` because `ap exec` sets `PATH=/usr/bin:/bin` and `shutil.which("fish")` did not see `/opt/homebrew/bin/fish`. Every Fish test failed before the gate ran. The test helper now tries `PATH` and then `/usr/bin/fish`, `/bin/fish`, `/usr/local/bin/fish`, and `/opt/homebrew/bin/fish`. The causal red above is the run after that lookup. The production shebang is unchanged.

Fish 4 treats `?` as a literal in `string match`. A first prefix pattern using `?` matched nothing, including a valid launchd path. The check is a full-string prefix match on `/private/var/run/com.apple.launchd.` plus a nonempty remainder. That correction landed before the green run.

## Pre-Existing Failure Classification

```text
Pre-existing claim: MacBook ambient FRAMENEST_NUC_SSH_* values can satisfy omitted gate arguments inside test_ssh_gate_rejects_missing_required_values
Class: test-isolation interference
Evidence: operator environment had nonempty TARGET, USER, and IDENTITY; COMMAND empty
Resolution in this commit: that parameterized test clears the four names for the invoked gate process and asserts the missing-value refusal
Production behavior: unchanged
Residual risk: other test files that inherit those names were not in this allowlist and were not retargeted
```

## Orchestration critique

```text
Orchestration critique:
MEASURED: none
LEAD: the production Darwin branch is not executed by the contract tests, because the declared route strips SSH_AUTH_SOCK; cheapest useful check is the fresh re-audit's read of that branch against the stated checks, without printing the socket
```

## Authority expiry

This terminal report ends the grant. No further edit, test, commit, push, or probe is authorized by this exchange.
