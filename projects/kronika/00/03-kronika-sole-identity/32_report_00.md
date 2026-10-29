### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `32` |
| Worker exchange ordinal | `01` |
| Task identity | `KSI-IMPL-COPS` |
| Persistent role | `WORKER` |
| Status | **PASS** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| NUC contact | `none` |
| Start commit | `a3977755b6d20a369f1a5c75e39bbcacd88de5c6` |
| Commit | `b8ec042b5bf1835df77c81341abc75e9cf8ab059` (`feat(operator): add the five canonical operator-script counterparts`) |
| Push / publication / deployment | none |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (unmoved; submodule clean) |

The five canonical counterparts exist, are executable, carry the established dual-prefix contract, and preserve every check, ordering, refusal, timeout and exit code of the old scripts. The old files are byte-untouched. One local commit; nothing published.

---

## 1. Canonical scripts, modes, old-file proof

New files, all mode `755` (verified `stat -c '%a'` and commit `create mode 100755`):

| Path | SHA-256 |
|---|---|
| `scripts/operator/infosec/kronika_log_triage.sh` | `261397a6850a336a5e0d9501474f42ae62fe38a43a5d7890e1145735abed9e1d` |
| `scripts/operator/infosec/kronika_public_surface_check.sh` | `fdabff7bfd21d47eb0dbe64754db0231f642470f69dcf4a45b5fcba7d68b7082` |
| `scripts/operator/infosec/kronika_socket_permissions_check.sh` | `54256110d43a43909304f4273ec1af62e123e4a0c083223b9c2fd6a21d222a97` |
| `scripts/operator/network/kronika_mullvad_egress.sh` | `c0e9569a3bf6fc91f8e8b3fb09088b59c4a8d120a3210b7b550970794698a736` |
| `scripts/operator/network/kronika_mullvad_egress.fish` | `7fb4ef2746422d262fd383c4a2649fb36003bf4a28cbfa83bbf8bc3377655851` |

Old files, hashes measured before any edit and re-measured after the commit — identical both times:

| Path | SHA-256 |
|---|---|
| `framenest_log_triage.sh` | `51191023e12547448ee41aa43df91d4368bf1b5614828d4465b386df1af4a9e9` |
| `framenest_public_surface_check.sh` | `8e67976250155d7f95785e3cd4e7c1f237d893af90fe7f8c7812ac24f67e7868` |
| `framenest_socket_permissions_check.sh` | `af1389ef6094676453e600df8086076e34be38b92367e759c659f8033c2406a5` |
| `framenest_mullvad_egress.sh` | `72fb5c929a398c93caf5890c526ccb7d1c397071cf1056d2da6357164e750bf1` |
| `framenest_mullvad_egress.fish` | `72de8e05e1f6dd57d7dcfb954438c09ba183ba35570552835fb4a3b5f27debe1` |

No old `framenest_*` operator script appears in the commit diff.

## 2. Derived variable suffix set and dual-prefix semantics

Derivation: I parsed every variable read and every `FRAMENEST_` literal in the five old scripts, then cross-checked against the gate's hook list. The complete suffix set is exactly the prompt's known set — no further operator variable exists. `TMPDIR` (ambient `mktemp` base), internal `PATH` pinning and the constants `MULLVAD_SUFFIX`/`DIAGNOSTIC_URL` are not operator variables.

| Family | Accepted suffixes (`KRONIKA_<S>` preferred, `FRAMENEST_<S>` retained) |
|---|---|
| log triage | `LOG_UNIT`, `LOG_SINCE`, `SPIKE_THRESHOLD`, `JOURNALCTL_BIN` |
| public surface | `PUBLIC_BASE_URL`, `CURL_BIN`, `SURFACE_CHECK_TIMEOUT` |
| socket permissions | `SOCKET_PATHS`, `EXPECTED_OWNER_PATTERN`, `STAT_BIN` |
| Mullvad hooks | `NETWORK_TEST_HOOKS`, `NETWORK_TEST_PYTHON`, `NETWORK_TEST_TAILSCALE`, `NETWORK_TEST_CURL`, `NETWORK_TEST_MULLVAD` |

Semantics, copied from `kronika_nuc_worker_gate.fish` `_resolve_env` and implemented identically in Bash:

- empty value counts as unset; only-canonical present → canonical; only-retained present → retained (empty primary falls back);
- both present and equal → accepted;
- both present and different non-empty → **exit 2**, stderr exactly `Conflicting environment variables <KRONIKA_NAME> and <FRAMENEST_NAME> are set to different values` — only the two names, never a value; neither value is used;
- resolution for **every** variable/hook happens before any logic, so a conflicting pair refuses even for `--help` or a subcommand that would not read it (the gate's established eagerness);
- empty + default → default (`kronika.service`, `50`, `journalctl`, `curl`, `10`, the canonical socket pair, `^(root|kronika)$`, `stat`); empty + required (`PUBLIC_BASE_URL`) → exit 64; empty hook with hooks enabled → exit 1 "not provided through the test hook".

The external facts `.mullvad.ts.net` and `https://am.i.mullvad.net/json` were not renamed.

## 3. Line-by-line logic diff classification

`diff -u` per pair; a mechanical residual scan (`grep` of all `+`/`-` lines excluding identity words, the resolution block, `TEST_*`/`override_*` plumbing and comments) returned only dual-prefix helper/default-application lines plus the identity strings below. Classification of every difference:

| Family | Hunks | Changes | Classes |
|---|---|---|---|
| `kronika_log_triage.sh` | 4 | 69 changed lines | header/usage/`SCRIPT_NAME` strings; default unit `framenest.service`→`kronika.service`; message `FRAMENEST_SPIKE_THRESHOLD`→`KRONIKA_SPIKE_THRESHOLD`; dual-prefix helper + resolution lines |
| `kronika_public_surface_check.sh` | 5 | 66 | banner `FrameNest`→`Kronika`; required/usage strings; FAIL messages name canonical variable; dual-prefix helper |
| `kronika_socket_permissions_check.sh` | 3 | 71 | defaults `/run/framenest/...`→`/run/kronika/...`, `^(root|framenest)$`→`^(root|kronika)$`; usage/messages; helper |
| `kronika_mullvad_egress.sh` | 8 | 57 | compatibility header comment; helper + five up-front hook resolutions; `resolve_required_tool`/`resolve_optional_tool` take the resolved value instead of an indirect variable name (same trust checks, same messages); `ensure_python`, `ensure_tailscale`, `ensure_curl`, `print_status`, `preflight_mutation` read resolved values |
| `kronika_mullvad_egress.fish` | 1 | 5 | comment; `bash_impl` names `kronika_mullvad_egress.sh` |

No check, comparison, ordering, refusal, timeout, option list or numeric exit code text differs. The helper/default lines shown by the residual scan are the mandated dual-prefix resolution (e.g. `UNIT="${UNIT:-kronika.service}"` replaces the old `:-` default at the read site; behavior identical for single-prefix environments).

## 4. Hermetic matrix results per family

All exercised through fake binaries only (`journalctl`, `curl`, `stat`, `tailscale`, `mullvad`) plus `fish --no-config`; no real journal, origin, socket, network or privilege use.

| Family | Canonical-only | Old-only | Equal dual | Conflict | Empty semantics | Missing required / tool | Preserved codes |
|---|---|---|---|---|---|---|---|
| log triage | exit 0 CLEAN, argv `-u kronika.service --no-pager -o cat` | identical | accepted | exit 2, names only, no value, journalctl not invoked | canonical-empty falls back to retained; per-variable mixing honored (`--since 24h ago` + threshold 2) | no `JOURNALCTL_BIN` → 64; failing tool → 1 with first stderr preserved | 0 clean / 1 spike (`SPIKE(>50)`, 60 lines) / 64 bad threshold |
| public surface | exit 0 PASS, 8 fetches, both banner and probes | identical | accepted | exit 2, names only, curl not invoked | canonical-empty falls back to retained | no URL → 64; bad scheme → 64; no `CURL_BIN` → 64 | 0 pass / 1 body DIFFERS / 1 header MISSING / 1 code mismatch / 1 ref empty / 1 transport |
| socket | exit 0 PASS both rows | identical | accepted | exit 2, names only, stat not invoked | canonical-empty falls back to retained | no `STAT_BIN` → 64; `::` → 64 "resolved to no paths" | 0 conform / 1 world bits / 1 not-a-socket / 1 owner mismatch / 1 retired owner `framenest` rejected by canonical default / 1 missing / 1 invalid ERE fails closed |
| Mullvad (bash + fish) | `enable --node` → exact `set --exit-node=... --exit-node-allow-lan-access=false`; `status` 0 | identical | accepted | exit 2 names only; no tool invoked | both empty + hooks → exit 1 "not provided through the test hook"; non-executable override → exit 1 | override `/nonexistent` → 1 "not a trusted absolute executable" | 0 success/verify-mullvad / 1 transport / 2 usage+invalid node / 3 NeedsLogin refusal / 4 non-Mullvad egress |

Focused modules: `test_operator_infosec_scripts.py` (43 collected) and `test_operator_network_scripts.py` (91 collected) — 134 combined, all green; plus retention 15 green.

## 5. Wrapper identity and environment-sanitization evidence

- **Reachability (behavioral, not textual):** the canonical Fish wrapper was driven with every fake tool present through the retained prefix and a conflicting canonical `KRONIKA_NETWORK_TEST_TAILSCALE` value. It exited 2 with the conflict message and invoked no tool. The retained Bash implementation ignores the canonical spelling and would have succeeded; the observed exit 2 can only come from the canonical implementation. Source confirmation: the wrapper's `bash_impl` names `kronika_mullvad_egress.sh`.
- **Sanitization:** through the wrapper with `APPIMAGE=/tmp/Cursor.AppImage`, `APPDIR`, `ARGV0`, `LD_LIBRARY_PATH`, `LD_PRELOAD` polluted, `status` succeeded and the fake child saw `APPIMAGE=` (empty) and none of the polluted values. Both the Fish `set -e ...` pre-clean and the Bash `unset`/`env -u` layers are in place.
- **Absence guard:** a wrapper copy run where no `kronika_mullvad_egress.sh` exists exits `127` with the sanitized message "Shared Bash implementation is missing." and runs no tool.
- Argument pass-through and exit-status forwarding are asserted by the new suite and by the existing retained-wrapper test.

## 6. Mutation demonstrations

Each guard was demonstrated load-bearing by running a mutated copy in `/tmp/opencode` (never in the repository) against the same fixture environment:

| Guard | Named mutation | Observed canonical | Observed mutant |
|---|---|---|---|
| log triage conflict | helper's conflict condition replaced by `if [[ 1 == 1 ]]` (silently prefer canonical) | exit 2, names only | exit 0, silently used `alpha-host` (fake argv recorded `-u alpha-host`) |
| public surface conflict | same mutation | exit 2, names only | exit 0, ran probes against `http://alpha.invalid` |
| socket conflict | same mutation | exit 2, names only | exit 0, `RESULT: PASS` on the canonical path |
| Mullvad conflict | same mutation | exit 2, names only | exit 0, ran `status` through the canonical fake, printed `backend: Running` |
| fish wrapper existence | guard block removed | exit 127, sanitized message | exit 127, raw `/bin/bash: ...: No such file or directory` (the message assertion fails) |

Absent-input proofs (no mutation): missing required URL → 64; missing tool binaries → 64; missing journalctl → 64; absent stat path → `FAIL(missing)` exit 1; absent bash implementation → 127; absent hook override → exit 1; unknown subcommand → 2; invalid threshold → 64 — all listed in section 4 and covered by named tests.

## 7. Operator documents updated; derivation differences

- `docs/OPERATOR_NETWORK.md`: subcommands, `ahw` sequence, NUC sequence (`KRONIKA_NUC_SSH_*`, `kronika_mullvad_egress.sh status`, canonical gate) and the Cursor Worker gate section now name the canonical scripts; compatibility notes keep the retained spellings truthful.
- `docs/INFOSEC.md`: §4.1, §4.6, §4.8, §5.1, §5.6 and the §7 table now name `kronika_*`; §7 adds the compatibility statement.
- `docs/ACCEPTANCE_DUAL_AUDIENCE.md`: A7/A9/B4 command blocks and the annex paragraph now use canonical scripts/variables (B4 keeps the actual live unit value `framenest.service` with a note that the unit name follows the host until C6-H); one compatibility note added near the introduction.

Derivation difference: `scripts/operator/network/README.md` still names the retained `framenest_mullvad_egress.*` entry points and `FRAMENEST_NETWORK_TEST_HOOKS`; it is outside the prompt's named positive authority, so it was left unchanged and is reported here. `docs/adr/0058` is frozen and speaks generically; `AGENTS.md` and `docs/WORKER_EXECUTION_CONTRACT.md` already carry canonical gate references and needed no edit.

## 8. Counts, elapsed time, baseline difference

| Run | Result | Time |
|---|---|---|
| Focused modules (infosec + network + retention) | **149 passed**, 0 failed | 3.64 s (process real 4.22 s) |
| Retention module alone | **15 passed** (unchanged count) | 0.34 s |
| Full declared Python suite (`ap exec --operation test`) | **4828 passed, 8 skipped, 3 warnings, 0 failed** | 692.43 s (11:32) |
| Baseline at `a397775` | 4773 passed, 8 skipped, 3 warnings, 0 failed | — |

Difference: **+55 passed** = +43 (new `test_operator_infosec_scripts.py`) + 12 (canonical Mullvad additions to `test_operator_network_scripts.py`). Skipped and warnings counts identical. Retention stayed 15 because it re-pins scalars without adding tests.

## 9. Commit, diff stat, Part A/B/C evidence

```text
git show --stat b8ec042:
 docs/ACCEPTANCE_DUAL_AUDIENCE.md                   |  30 +-
 docs/INFOSEC.md                                    |  20 +-
 docs/OPERATOR_NETWORK.md                           |  52 +-
 scripts/operator/infosec/kronika_log_triage.sh     | 148 ++++
 scripts/operator/infosec/kronika_public_surface_check.sh | 193 +++++
 scripts/operator/infosec/kronika_socket_permissions_check.sh | 153 ++++
 scripts/operator/network/kronika_mullvad_egress.fish |  16 +
 scripts/operator/network/kronika_mullvad_egress.sh | 770 ++++++++++++++++++++
 tests/contract/test_kronika_identity_retention.py  | 114 ++-
 tests/contract/test_operator_infosec_scripts.py    | 787 +++++++++++++++++++++
 tests/contract/test_operator_network_scripts.py    | 342 ++++++++-
 11 files changed, 2561 insertions(+), 64 deletions(-)
```

- Commit SHA `b8ec042b5bf1835df77c81341abc75e9cf8ab059`, parent `a3977755…`, working tree clean, no branch/tag/push. Exactly one `git add` of the 11 exact paths and one commit.
- **Part A unmoved:** no frozen path in the diff; `test_frozen_adr_and_host_document_bytes_are_unchanged` and the Alembic byte/complete-set tests all pass. `FROZEN_ALEMBIC_SHA256` computed from the tree: **36** keys (extraction + completeness test).
- **Part B still 20:** `EXPECTED_FRAMENEST_BASENAME_PATHS` measured 20 and the ledger test passes; all five new basenames contain `kronika`, not `framenest`.
- **Part C movement, re-pinned from my own measurement** (temp probe over tracked ∪ this cut's untracked additions, then confirmed green by the real ledger after staging):

| Pin | Before → After | Cause |
|---|---|---|
| `tests` occurrences | 2214 → **2251** (+37) | +7 network module edits, +30 new infosec module |
| `scripts` occurrences | 86 → **98** (+12) | 4 canonical Bash scripts × 3 (helper `FRAMENEST_`, header note, usage note); canonical Fish adds 0 |
| `docs` occurrences | 1231 → **1206** (−25) | OPERATOR_NETWORK −12, INFOSEC −7, ACCEPTANCE −6 (repointed commands; compatibility notes partially restore) |
| content-path membership | +5, −0 | the 4 Bash scripts + infosec test module; canonical Fish deliberately absent |
| `scripts` file count | 7 → **11**; `tests` 185 → **186** | same causes; docs/deploy/src/extension file counts unmoved |
| env tokens | 695 → **699** (+4) | infosec module +10, network module +1, docs −7; distinct names unmoved at **112** |
| bare `FRAMENEST_` | 29 → **53** (+24) | scripts +11, infosec module +7, network module +5, OPERATOR_NETWORK +1 |
| capitalized | 2772/398 → **2773/399** (+1/+1) | one verbatim retained-banner assertion in the infosec module |
| mutation header / host paths / unit accounts / consoles | unmoved | no touches |

## 10. Sites no test exercises

- Retained infosec scripts' refusal and edge branches (only success sanity + byte-identity are exercised; intentional).
- Canonical Mullvad branches not re-executed against the canonical copy: unreadable `get` preference fallback, opaque selected-preference reconciliation, `unsafe-non-explicit`, `recover` first-error ordering, self-advertised-exit-node refusal, competing/ambiguous-tunnel refusals, LAN-access unavailability. These are exercised for the retained script by the existing suite; canonical equivalence rests on the classified diff plus the shared body, not re-execution.
- Non-hook production tool resolution (`resolve_from_trusted_path`, trusted-PATH rejection) for all four Bash scripts — unchanged limitation of the harness.
- The new document compatibility prose is not pinned by a doc-content test.
- `scripts/operator/network/README.md` retains old-name references with no test pinning them.

## 11. Deviations, risks, missing evidence, smallest next step

- **Deviations:** none within scope. The README difference in section 7 is the only found-but-not-granted reference. No publication, push, host, NUC, network, journal or provider contact; no dependency/pyproject/AP change.
- **Risks:** a single-name message (e.g. the threshold FAIL) names the canonical variable only, which an old-spelling operator may find surprising; the conflict message and both usage texts name both spellings. Conflict resolution is eager for all variables, matching the gate.
- **Missing evidence:** none material to this cut; host/rendered evidence is intentionally out of scope.
- **Smallest next step:** Orchestrator independent acceptance, then publication of `a397775` + `b8ec042` followed by the planned `C6-H` window.

### Resolved Execution Issues / Near-Misses

- The shell policy rejected one compound smoke command containing recursive cleanup; fixtures were rebuilt with the file tools and plain commands. No repository impact.
- First focused run: 3 of 134 failed, all defects in my new test expectations, not candidates — a mode-`644` fixture correctly produced `FAIL(multiple)` because the world-read bit also fires, so the isolation fixture uses `600`; the retained socket script's retained default owner pattern correctly rejects the `kronika` owner, so the retained regression uses a `framenest` owner/path; and one assertion compared against the wrong side of an accumulating fake log. Fixed before staging.
- A temporary fake `tailscale` initially lacked the executable bit; the mutated Mullvad demo refused with exit 1 "not a trusted absolute executable" — itself confirming the override trust check — before `chmod` and the intended silent-pick demonstration.
- One mutation-demo pipeline (`| head -2`) produced exit 141 by SIGPIPE; rerun without the pipeline showed the true exit 0.

### Pre-Existing Failure Classification

**None.** The `a397775` baseline's 4773/8/3/0 was reproduced as 4828/8/3/0 with the delta fully attributed to this cut's added tests; no failure, skip-set or warning movement predates or accompanies the cut.

```text
Orchestration critique:
MEASURED: The remaining Mullvad branch matrix (unreadable get fallback, opaque preference reconciliation, recover ordering, self-advertised and competing-tunnel refusals, LAN-access unavailability) is executed only against the retained framenest_mullvad_egress.sh; the canonical copy's equivalence for those branches rests on the classified diff. Evidence: grep shows no module runs those cases against kronika_mullvad_egress.sh. Effect: "every preserved check and exit code" for those branches is proven by equivalence, not re-execution, before C7-B deletes the old files. Smallest correction: one bounded independent-acceptance harness run that re-points the existing matrix at the canonical script (no repository change).
LEAD: docs/ACCEPTANCE_DUAL_AUDIENCE.md A7 composes its own inline UDS wrapper reading `FRAMENEST_UDS_PATH`, an operator scratch variable outside the five scripts' variable families; unverified whether C7-B intends to include that inline spelling. Cheapest useful check: read A7 when planning C7-B and decide its scope then.
```

All authority under this Worker prompt expires on submission of this report. No further implementation, second commit, push, publication, host contact or later cut is authorized by it.