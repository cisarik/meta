### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`  
Worker session ordinal: `41`  
Worker exchange ordinal: `01`  
Persistent role identity: `WORKER`  
Worker session target: `fresh-worker-session`  
Native planning mode: `not-used`  
Worker session profile: Fresh Independent Audit, read-only  
Task identity: `KSI-AUDIT-C6PS`  
status: **PASS**  
Phase-qualified result: `not-applicable`  
Logical-whole closure: `not-closed`  
Report justification: `new-evidence`  
Start commit: `fcde631047650d1ff0a84b84bf185b54d6d11ba5`  
End commit: `fcde631047650d1ff0a84b84bf185b54d6d11ba5`

The candidate makes absence, presence, and query failure three distinguishable outcomes. No blocking finding. Escalation condition: not triggered.

## 1. Identity, scope, and gates

Standalone checkout `/home/agile/Projects/kronika`, branch `main`, HEAD `fcde631047650d1ff0a84b84bf185b54d6d11ba5`, parent `980041cf13dd427e77263f573694aed7c1a54018`. Working tree clean at start and at close. Local `origin/main` is the parent; this checkout is ahead by 1. No fetch was performed.

`.ap` gitlink and submodule HEAD are both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap doctor`: PASS, governing variant stable. `ap project check --baseline fcde631…`: PASS. `runtime-info`: CPython 3.13.9, `.venv/bin/python`, provenance module `kronika`.

The commit changes exactly two paths:

```text
 deploy/ubuntu/kronika_release.py                  |  20 +-
 tests/contract/test_kronika_identity_migration.py | 217 +++++++++++++++++++++-
 2 files changed, 224 insertions(+), 13 deletions(-)
```

The engine hunk is only `cmd_remote_account_processes_absent`, including its docstring. Every other byte of `deploy/ubuntu/kronika_release.py` matches the parent. `assert_no_legacy_writers` is outside that hunk. Its comparisons, the messages `former web account process state is unverifiable` and `a process still runs as the former web account`, and `EXIT_MIGRATION = 27` are the parent text. The retention file is not in the commit.

This audit changed no repository file, commit, or branch. Temporary probe state under `/tmp/ksi-audit-41` was removed; the directory is absent.

## 2. Three-outcome matrix

The repository matrix executes the real builder through `RemoteBoundary.account_process_query`. An independent `/bin/sh` probe ran the same transcribed body with synthetic `id` and `ps`. Both agreed.

| Condition | Token | Caller |
|---|---|---|
| Valid account, zero processes, decoys `0`, `11001`, `10010` present | `0` (1 byte) | pass |
| One spaced UID line | `1` | `a process still runs as the former web account`, exit 27 |
| Four spaced UID lines, same decoys | `4` | same refusal, exit 27 |
| Unknown account | `query-failed` | `former web account process state is unverifiable`, exit 27 |
| `ps` returns 1 immediately | `query-failed` | unverifiable, exit 27 |
| `ps` returns 127 | `query-failed` | unverifiable, exit 27 |
| `ps` prints a target UID and then returns 1 | `query-failed` | unverifiable, exit 27 |
| Empty, malformed, or multiline UID; `id` returns 0 with empty stdout; `id` returns 1 after printing a UID | `query-failed` | unverifiable, exit 27 |
| Empty, blank, header, or extra-column snapshot | `query-failed` | unverifiable, exit 27 |
| Counter returns 2, or `awk` is absent from `PATH` | `query-failed` | unverifiable, exit 27 |

Account `worker' $(printf unsafe)` is passed as one literal argument. The independent probe recorded that exact byte string, created no side file from the substitution, and counted `2`. The repository test also returned `2`.

A zero-padded field `01001` against UID `1001` produces token `1`. That is numeric equality. The caller then refuses with the positive-count message. It does not become `0`.

## 3. Caller contract, quiesce, and recovery

`0` passes `assert_no_legacy_writers`. Any other token except `query-failed` raises the positive-count refusal. `query-failed` raises the unverifiable refusal. Both use exit 27. The repository cases assert those exact strings.

`quiesce` order is observe, stop writers, assert, capture. The passing order test records admission, then the timer, then the job, then `ps -e -o uid=`, then the capture snapshot.

A process refusal raises inside `quiesce` after `writers_stopped` is recorded and before `_capture_before` exists. `recover_pre_write` then restores the observed unit records, including the active state that `stop` had changed. Both the positive-count refusal and the `query-failed` refusal passed that test.

`run_migration_apply` still selects `recover_pre_write` when `writes_possible` is false. That flag is set only on entry to `start-service`, which follows `quiesce`. The simulated-host failure injection covers a failure at every phase index, including the first, and selects pre-write recovery before cutover. A non-zero remote exit still becomes `ReleaseError("command failed", EXIT_TRANSPORT)` with exit 20, because `subprocess_runner` is unchanged and the corrected script exits 0 so the token can be read.

## 4. Mutation probes

Each mutation was applied in the independent shell probe and, separately, by the repository test to the real builder. Repository results below are the test’s own printed observation plus the caller assertion that passed with it.

| Mutation | Test | Observed token | Caller outcome |
|---|---|---|---|
| `old-selection-guard`: restore `if ! ps -u … -o pid=` | zero processes, synthetic `ps -u` exits 1; one process exits 0 | `query-failed`; the one-process control returned `1` | unverifiable, exit 27 |
| `unchecked-ps`: drop the `ps` exit check | failing `ps` leaves unrelated UID lines | `0` | caller passes |
| `unguarded-uid`: drop the `id` failure branch and the digit guard | unknown account, snapshot still contains UID `0` | `0` | caller passes |

The corrected builder, before each mutation, produced the safe token: `0`, `query-failed`, and `query-failed` respectively. The same shell body under `set -euo pipefail` on this bash `/bin/sh` kept those outcomes.

## 5. Boundary fidelity

`account_process_query` prepends shell functions and runs the production body with `/bin/sh -c`. On this machine `/bin/sh` is bash and `awk` is GNU Awk 5.4.1. The functions return 97 for an unsupported invocation and do not call through to the binary. Unsupported `id` and unsupported `ps` both produced `query-failed`, with the reject marker set.

With the functions defined and decoy binaries first on `PATH`, the token was `0` and those binaries were not executed. With the functions removed and the same decoy binaries present, the binaries were executed and the token was `0`. The harness always defines the functions. A positive `0` for the fixture account also depends on them here: local `id -u framenest` exits 1, so the success cases fail if the synthetic UID is not supplied.

The removed parent branch returned a stored count whenever the command text contained `ps -u ` and the fake flags looked healthy. It did not run the shell and did not model procps exit 1 on an empty selection. The new executor runs the body. An unhandled remote command still raises in `_dispatch`.

Branches the boundary does not reach:

- dash and mawk, because neither is installed here
- a production `run_migration_apply` driven by this specific refusal; the production test calls `recover_pre_write` directly, and the dispatcher test uses the simulated host
- an injected unsupported-argv case inside the repository suite; the independent probe reached that harness return
- procps-ng 4.0.4 on the NUC

## 6. Checks and Part A / Part B

| Check | Result |
|---|---|
| Migration module | 231 passed, 1.23 s |
| Retention module | 15 passed, 0.37 s |
| Named process, mutation, quiesce, and recovery cases | 26 passed, 205 deselected |
| Full Python suite | **4901 passed, 8 skipped, 3 warnings, 0 failed**, 695.03 s, operation exit 0 |

Difference from `4901/8/3/0`: none. The three warnings are `PydanticJsonSchemaWarning` on the two health OpenAPI contract tests and `test_database_path_absent_from_settings_repr_logs_api_and_openapi`. The eight skips are the existing real-tool and live-provider skips.

Part A pins are unchanged in the commit. The pin file contains 86 document keys and 36 Alembic keys. The retention tests passed, so the on-disk bytes match those pins and the Alembic key set matches the version directory. Part B is the 20-path basename set; its exact-membership test passed.

## 7. Findings and untested sites

No blocking finding.

Non-blocking:

- Numeric `==` counts a zero-padded field as the canonical UID. The required prefix and suffix cases (`11001`, `10010`, `0`) stay exact. The extra match refuses the migration. Local procps output contained no zero-padded UID field.
- Failure-expected cases could pass for the wrong reason if the synthetic functions were omitted and local `id` failed. The success cases cannot, and the executor always installs the functions.

Untested sites: NUC procps-ng 4.0.4 `ps -e -o uid=` exit status and column shape; dash; mawk; one production `run_migration_apply` call that carries this refusal into the dispatcher; the transport exit-20 path, which this diff does not touch.

## 8. Deviations, risks, and next step

The implementation counts one checked `ps -e -o uid=` snapshot. That satisfies the required matrix. A failed snapshot is discarded, including one that already printed the target UID.

Local procps-ng 4.0.7, which is not the NUC, exits 0 for `ps -e -o uid=`, exits 1 for an unknown-user `ps -u` selection, and exits 0 for `ps -u root`. Its 388 UID lines were all single numeric fields, with no leading-zero field. The production body, a numeric awk count, a string awk count, and the `ps -u` line count agreed. No NUC, SSH, provider, browser, capture, publication, or deployment contact occurred.

Repository commands were read-only Git inspection, `ap doctor`, `ap project check`, and `ap exec` for `runtime-info`, `test-focus`, and `test`. The shell probes and the local `ps`/`id` format read were outside the repository and were removed.

Smallest next step: under separate authority, publish `fcde631047650d1ff0a84b84bf185b54d6d11ba5`, archive the failed journal, run a fresh preflight, and retry the apply.

**Resolved Execution Issues / Near-Misses**

The first fallthrough probe set `PATH` to the decoy directory only, so `awk` was missing and both the function-present and function-absent runs returned `query-failed`. That was probe construction. The rerun with `awk` on `PATH` is the evidence above. No product file was changed.

**Pre-Existing Failure Classification**

none

Authority expiry: this terminal report ends the grant. No implementation, correction, commit, push, publication, host contact, or later cut is authorized. The report was delivered here only; no report file was written.

Orchestration critique:  
MEASURED: none  
LEAD: the corrected `ps -e -o uid=` form was not executed on procps-ng 4.0.4; local 4.0.7 output was accepted. Cheapest useful check: the already required apply retry, which fails closed on `query-failed`.