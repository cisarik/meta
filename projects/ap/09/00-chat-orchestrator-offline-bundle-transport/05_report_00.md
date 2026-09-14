### Report for ORCHESTRATOR_CHAT

Logical whole identity: chat-orchestrator-offline-bundle-transport
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Fresh Independent Re-Acceptance
Worker session target: fresh-worker-session
Native planning mode: not-used
Delivery route: manual Cooperator delivery
Phase: Independent Re-Acceptance
status: PASS
Phase-qualified result: Acceptance PASS
Start commit: 717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
End commit: 717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
Report justification: final-acceptance
Logical-whole closure: not-closed

Evidence posture: public branch state not directly observed. This Re-Acceptance Worker used ordinary local Git on the canonical AP checkout and disposable fixtures. No independently observed current public branch evidence is claimed. Exact committed bundle evidence was exercised only inside those fixtures.
Commit authority: not granted; no AP commit or push. Meta Git archival is Cooperator-owned and was not performed in the acceptance grant; this file is a later Cooperator-requested RF-19 report companion. No consumer `.ap` pin was moved.
Requested reasoning: High; effective reasoning/context unknown.

This is a terminal independent-reacceptance report. It does not claim Implementation PASS restatement, publication-PASS, deployment-PASS, production-acceptance-PASS, consumer adoption, or ORCHESTRATOR closure.

Acceptance candidate: uncommitted dirty worktree of `/home/agile/Projects/ap` on `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf`
Acceptance owner map: live semantic owner remains `AP.md`; Session 04 mutated only `ap`; this Worker mutated neither the candidate nor Meta during the audit
Acceptance allowlist: inspect-only
Acceptance risk claims: offline transport temporary directories can contain complete committed repository history and companion/submodule Git objects; they must not outlive the exporting process
Acceptance control matrix: register every `ap-bundle.*` root in the parent shell; cleanup limited to this process's registered paths; no glob deletion of `/tmp/ap-bundle.*`; source repositories and object databases remain untouched; EXIT/HUP/INT/TERM all run owned-path cleanup
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ambient `GIT_DIR`; IMPORT.md empty-DEST wording; POSIX `$'\n'`; shared `--allow-path` namespace

This Meta file is the RF-19 report companion to issued prompt `05_acceptance_00.md` under this whole's activated local grammar (`NN_<phase>_00.md` + `NN_report_00.md` for exchange `01`). It is not a prompt, interruption, or handout.

---

## Independence

Previous reports were read only for provenance. Their harnesses, assertion counts, and verdicts were not used as acceptance evidence. Independent adversarial fixtures ran under isolated `HOME`, `XDG_STATE_HOME`, `XDG_CONFIG_HOME`, `TMPDIR`, and `--output-dir`. A temporary commit of the candidate `ap` existed only inside a disposable exporter clone under `/tmp`. `/home/agile/Projects/ap` was not edited, committed, or pushed during the audit. Disposable fixtures were removed afterwards.

---

## Baseline and candidate worktree

Independently verified before and after the audit:

| Fact | Value |
|---|---|
| Canonical worktree | `/home/agile/Projects/ap` |
| Origin | `https://github.com/cisarik/ap.git` |
| HEAD | `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf` |
| Branch | `feat/ap-practical-workflow-consolidation` |
| State | dirty uncommitted candidate on that HEAD |
| Tracked changes | 13 files |
| Untracked | `docs/adr/0025-chatorchestrator-offline-bundle-transport.md` |
| Diffstat | `13 files changed, 1399 insertions(+), 43 deletions(-)` |
| `ap` | `+1181` lines versus HEAD |
| Commit / push | none |

The real dirty exporter correctly refused export: `exporter AP checkout is dirty`.

```text
 M AP.md
 M AP_ORCHESTRATOR.md
 M CHANGELOG.md
 M FAQ.md
 M GLOSSARY.md
 M INTEGRATION.md
 M INTUITION.md
 M PROMPT_CONTRACTS.md
 M PROMPT_ENGINEERING_PATTERNS.md
 M README.md
 M UPDATING.md
 M ap
 M docs/adr/README.md
?? docs/adr/0025-chatorchestrator-offline-bundle-transport.md
```

---

## Files inspected

Code: `ap` (`cmd_bundle`, `bundle_alloc_tmp`, `bundle_cleanup`, helper split `require_tool_repository` / `require_context`).

Semantics and projections: `AP.md`, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`, `PROMPT_ENGINEERING_PATTERNS.md`, `GLOSSARY.md`, `FAQ.md`, `INTUITION.md`, `INTEGRATION.md`, `README.md`, `UPDATING.md`, `CHANGELOG.md`, `docs/adr/README.md`, `docs/adr/0025-chatorchestrator-offline-bundle-transport.md`.

Untouched check: `AP_WORKER.md`, `ARTIFACT_LIFECYCLE.md`, `INFOSEC.md`, `ap.project.conf`, historical ADR-0022 and ADR-0023 bodies (empty diff).

Handoff: `01_planning_00.md`, `01_report_00.md`, `02_implementation_00.md`, `02_report_00.md`, `03_acceptance_00.md`, `03_report_00.md`, `04_correction_00.md`, `04_report_00.md`, `05_acceptance_00.md`.

---

## Cleanup success / failure / SIGINT / SIGTERM

Session 03 blocked because `bundle_mktemp` ran only inside `$(...)`, so parent-shell `bundle_tmp_list` never saw allocated roots. This Worker independently inspected the Session 04 correction and exercised it.

Code audit:

- `bundle_mktemp` is gone.
- `bundle_alloc_tmp` is a direct current-shell function: `mktemp -d "${TMPDIR:-/tmp}/ap-bundle.XXXXXX"`, reject unexpected paths, append the root to `bundle_tmp_list`, then derive child paths.
- No `$(bundle_alloc_tmp)` or `$(bundle_mktemp)`.
- No `rm -rf` glob of `/tmp/ap-bundle.*`.
- Cleanup deletes only registered paths matching `*'/ap-bundle.'*` with `rm -rf -- "$bundle_tmp_one"`.
- Empty lines are skipped; paths are quoted.
- Traps: EXIT → `bundle_cleanup`; HUP → cleanup then `exit 129`; INT → cleanup then `exit 130`; TERM → cleanup then `exit 143`.
- Cleanup disarms those traps first. Duplicate cleanup is therefore harmless.
- `sh -n ap` passed.
- Failed `mktemp` is not registered. Partial initialization (invalid project name after traps) left no temps.
- EXIT-trap assignment does not mask the original status (`exit 7` remained 7; tracked-secret and nothing-new paths remained non-zero).
- Source repositories and object databases are not used as temporary storage.

Live results (isolated `TMPDIR`; foreign decoy `$TMPDIR/ap-bundle.foreign-decoy` and an unrelated sentinel retained in every case):

| Scenario | Result |
|---|---|
| Successful initial export (project + `.ap` + companion) | exit 0; valid ZIP; **5** `ap-bundle.*` roots allocated; **no owned temp remained**; decoy and sentinel survived |
| Failure after allocation (tracked `.env`) | non-zero; owned temps gone |
| Failure after allocation (`nothing new to export`) | non-zero; owned temps gone |
| SIGINT after allocation (`timeout --signal=INT` to the process group) | **130**; owned temps gone; decoy survived |
| SIGTERM after allocation | **143**; owned temps gone; decoy survived |
| Multiple roots | five mktemp roots on the companion initial; all gone at EXIT |
| Source repos | consumer and disposable exporter remained clean |

Sending SIGINT only to the parent PID while bash waits for a child is not equivalent to Ctrl+C; bash may defer or discard that INT. Process-group INT (`timeout --signal=INT`) is the contractual interrupt and passed.

The previous temp-cleanup blocker is independently resolved. No unsafe glob deletion of unrelated `/tmp/ap-bundle.*` was observed.

---

## Exact reconstruction

```sh
ap bundle <project> --initial
```

from a disposable clean exporter produced a ZIP containing `project.bundle`, `ap.bundle`, `manifest.conf`, `checksums`, and `IMPORT.md`. Reconstruction:

- reconstructed project HEAD equals source project HEAD;
- reconstructed `.ap` HEAD equals the superproject gitlink equals source `.ap` HEAD;
- no synthesized transport commit in reconstructed project history.

Canonical AP self-bundle (exporter origin set to canonical URL) produced `project.bundle` and no `ap.bundle`; reconstruction matched the disposable exporter HEAD.

---

## Cumulative incremental

Chain `A = initial`, `B = intermediate`, `C = newest`. Package B was not applied.

`initial A + cumulative A..C update` reconstructed C. Intermediate B objects were present in the cumulative update. The `.ap` gitlink was unchanged through A..C.

---

## Missing prerequisites

`git bundle verify` of the cumulative incremental `project.bundle` inside an empty repository failed closed (`Repository lacks these prerequisite commits`). `IMPORT.md` directs ChatOrchestrator to a fresh `--initial`, states `Do not contact GitHub`, and forbids network `git submodule update`.

Non-ancestor / rewritten initial commit: incremental export failed closed (`no longer an ancestor`).

---

## Zero-network

`cmd_bundle` does not call `fetch_remote_main`, `ls-remote`, GitHub API, remote clone, or `submodule update`. A live export under a broken proxy plus a git wrapper that rejects non-bundle fetch / `ls-remote` / remote clone succeeded. This restriction applies only to the bundle exporter / ChatOrchestrator transport workflow. `ap update --check` still fetches canonical origin, as required for that command.

---

## Evidence semantics

Live `AP.md` owns two named classes:

```text
exact committed bundle evidence
independently observed current public branch evidence
```

Required limitation when GitHub has not actually been observed:

```text
public branch state not directly observed
```

Generated `manifest.conf` records `bundle.evidenceClass = exact-committed-bundle-evidence`, `bundle.publicVerification = not-performed`, and `bundle.publicBranchState = not-directly-observed`. Exporter stdout repeats the limitation. `IMPORT.md`, FAQ, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md` restoration, glossary, and ADR-0025 agree. A bundle does not prove current GitHub branch HEAD, push success, remote synchronization, or absence of newer public commits.

Historical ADR-0022 / ADR-0023 bodies remain historical. ADR-0025 records prospective supersession of ADR-0023's first-manual Planner *delivery* rule only. That is not a live contradiction.

ChatOrchestrator may perform ordinary routing from valid bundle evidence when public state is not the claim being decided. Publication / public-ref claims still require independent public evidence.

---

## Delivery semantics

Access profile, GitHub capability, dispatch capability, native planning mode, freshness/independence, and delivery route remain separate axes.

- ChatOrchestrator → manual Cooperator ferry normally.
- Full Orchestrator with authorized functioning dispatch → direct complete-prompt dispatch normally, including the first Planner.
- Native planning mode for the first Planner remains `required`.
- Independence / required-external-fresh-session constraints remain separate and still require manual or external fresh delivery.
- Cooperator opt-out / failed / unavailable dispatch remains a manual fallback.

---

## Companion

```sh
ap bundle <project> --initial --companion-trace <repo>
```

included `companion-trace.bundle` at the exact companion HEAD.

A later `ap bundle <project>` after only the companion trace changed produced a useful update: `companion-trace.bundle` present, `projectBundle = omitted-unchanged-from-initial`. No hardcoded Meta path, no sibling scan, no automatic inclusion of private repositories.

---

## Secrets and ignored files

- Ignored `.env` does not dirty porcelain; export succeeds; `.env` is absent from ZIP names.
- Tracked `.env` refuses.
- Historically tracked then deleted `.env` refuses.
- Explicit exact `--allow-path .env` exports and records the path in the manifest.

Filename scanning does not prove absence of secrets. The exporter states that limitation.

---

## Other submodules

- An unexpected extra gitlink fails closed without `--include-submodule`.
- `--include-submodule lib` bundled the checkout at its exact gitlink; reconstruction matched.
- Missing submodule content was not fetched from the network.

---

## Existing-command regression

The `require_tool_repository` / `require_context` split is an extraction. `init`, `doctor`, `project`, `exec`, and `update` contracts are unchanged.

- Throwaway-consumer `ap init` and `ap doctor`: PASS.
- Throwaway contract `ap project check --baseline` and `ap exec`: PASS.
- Canonical AP `ap project check --candidate`: missing `.venv` — environment-dependent, not a command regression.
- `ap update --check` still fetches origin. On the disposable exporter HEAD (ahead of `origin/main`) it correctly refused `canonical origin/main is behind the current AP commit`. No `--apply` and no publication were performed.

---

## Coordinate finding

Live AP (RF-19) progression for this whole:

```text
01 Planner
02 Implementation
03 Acceptance
04 Correction
05 Re-Acceptance
```

This Worker used session `05`, exchange `01`. The Implementation report historically restates `01` / `01` for a `fresh-worker-session`; the Implementation prompt lacks Worker session/exchange ordinal fields even though Meta-local grammar already uses `02_`. Classification remains a **non-blocking** documentation / report-coordinate defect plus an issuance defect. Historical reports were not rewritten. The product candidate is independently inspectable.

---

## Non-blocking observations disposition

Session 03 listed these outside Session 04's correction scope. Independent re-evaluation: none is a material correctness, portability, privacy, security, or continuity failure of the supported contract on this host. They do not block.

| Observation | Disposition |
|---|---|
| Ambient `GIT_DIR` | Fail-closed (`the ap tool must live inside a Git worktree`); no temp leak |
| IMPORT.md empty-DEST wording | `extractall DEST` still lacks “new empty DEST”; reconstruction instructions otherwise fail-closed |
| POSIX `$'\n'` | Bashism in `#!/bin/sh`; this host's `/bin/sh` is bash, so newline rejection works; dash is not present here |
| Shared `--allow-path` namespace | One allow list across project / `.ap` / companion / submodule; operator-explicit and recorded in the manifest |

---

## Security findings

1. **Resolved blocker:** parent-shell registration now tracks every `ap-bundle.*` root; EXIT/HUP/INT/TERM delete only those owned paths. Successful export, post-allocation failure, process-group SIGINT, and SIGTERM leave no owned temps. Foreign decoys survive. No glob deletion of `/tmp/ap-bundle.*`.
2. Filename scanning still does not prove absence of secrets.
3. No new material security blocker.

---

## Overall

```text
ACCEPTANCE-PASS
```

PASS requires, and this Worker independently confirmed: previous temp-cleanup blocker resolved; no new material blocker; exact offline reconstruction works; cumulative incremental works; ChatOrchestrator evidence semantics remain correct; no accidental GitHub dependency in `ap bundle`; no material regression in the AP executable.

---

## Next recommended phase

1. Cooperator commit of the candidate.
2. Push canonical AP.
3. Verify publication.
4. Then consumer `.ap` pin adoption as a separate step.

This Worker did not perform those actions.

---

## Mutations

The candidate was not edited, committed, or pushed. HEAD remains `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf` with the same dirty set. Consumer `.ap` pins were not moved. Product Meta was not mutated during the audit. Persistence of this companion file is a Cooperator-requested reporting write after the Re-Acceptance Worker had already stopped product work.

---

Orchestration critique:
MEASURED: parent-shell `bundle_alloc_tmp` plus owned-path cleanup; process-group SIGINT 130; SIGTERM 143; exact A reconstruction; cumulative A..C without package B; missing-prerequisite fail-closed; companion-only update omits unchanged project payload.
LEAD: none.
Resolved Execution Issues / Near-Misses: an audit git wrapper first blocked `git config` origin URL strings; SIGINT against the parent PID alone is not Ctrl+C — retested with `timeout --signal=INT`.
Pre-Existing Failure Classification: missing `.venv` on canonical `project check`; `update --check` behind-main on the disposable exporter HEAD.
Authority expiry: this terminal report ends the Re-Acceptance grant; no autonomous continuation. Persistence of this companion file was a later Cooperator-requested reporting write, not a new mutation grant over `ap`.
