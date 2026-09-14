### Report for ORCHESTRATOR_CHAT

Logical whole identity: chat-orchestrator-offline-bundle-transport
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Correction Worker
Worker session target: fresh-worker-session
Native planning mode: not-used
Delivery route: manual Cooperator delivery
Phase: Bounded Correction
Task identity: parent-shell registration of `ap bundle` temporary roots after ACCEPTANCE-BLOCKED
status: PASS
Phase-qualified result: not-applicable
Start commit: 717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
End commit: 717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
Report justification: new-mutation
Logical-whole closure: not-closed

Evidence posture: public branch state not directly observed. This Correction Worker used ordinary local Git on the canonical AP checkout. The candidate remained uncommitted. No independently observed current public branch evidence is claimed. Exact committed bundle evidence was exercised only inside disposable fixtures.
Commit authority: not granted; no AP commit or push. Meta Git archival is Cooperator-owned and was not performed. No consumer `.ap` pin was moved.
Requested reasoning: High; effective reasoning/context unknown.

This is a terminal Correction Worker report. It does not claim acceptance-PASS, publication-PASS, deployment-PASS, production-acceptance-PASS, Implementation PASS restatement, consumer adoption, or ORCHESTRATOR closure.

Acceptance candidate: uncommitted dirty worktree of `/home/agile/Projects/ap` on `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf`
Acceptance owner map: live semantic owner remains `AP.md`; this correction mutated only `ap`
Acceptance allowlist: `ap`
Acceptance risk claims: offline transport temporary directories can contain complete committed repository history and companion/submodule Git objects; they must not outlive the exporting process
Acceptance control matrix: register every `ap-bundle.*` root in the parent shell; cleanup limited to this process's registered paths; no glob deletion of `/tmp/ap-bundle.*`; source repositories and object databases remain untouched; EXIT/HUP/INT/TERM all run the same owned-path cleanup
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ambient `GIT_DIR`; IMPORT.md empty-DEST wording; POSIX `$'\n'`; shared `--allow-path` namespace

This Meta file is the RF-19 report companion to issued prompt `04_correction_00.md` under this whole's activated local grammar (`NN_<phase>_00.md` + `NN_report_00.md` for exchange `01`). It is not a prompt, interruption, or handout.

---

## Repository identity

Verified before mutation and after this report's product edits:

| Fact | Value |
|---|---|
| Canonical worktree | `/home/agile/Projects/ap` |
| Origin | `https://github.com/cisarik/ap.git` |
| HEAD | `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf` |
| Branch | `feat/ap-practical-workflow-consolidation` |
| Candidate | intentionally uncommitted dirty worktree on that HEAD |
| Dirty set | unchanged 13 tracked files + untracked `docs/adr/0025-chatorchestrator-offline-bundle-transport.md` |
| File mutated by this Worker | `ap` only |
| `/bin/sh` | bash (`/bin/sh -> bash`) |

No unexpected paths beyond the known implementation candidate. Planning was not reopened. AP semantics and projections were not edited.

---

## Root cause confirmed

Independent Acceptance (`03_report_00.md`) blocked because temporary bundle directories were not tracked by parent-shell cleanup.

The implementation registered paths inside `bundle_mktemp`, then invoked that function only through command substitution:

```sh
bundle_raw=$(bundle_mktemp)/objects
bundle_payload=$(bundle_mktemp)/payload
bundle_zip_repo=$(bundle_mktemp)/zipgit
```

`$(...)` runs in a subshell. Assignments to `bundle_tmp_list` died with that subshell. The parent `trap 'bundle_cleanup' EXIT HUP INT TERM` therefore deleted nothing. Leftover `${TMPDIR:-/tmp}/ap-bundle.*` directories retained bundle payloads.

This Worker confirmed that diagnosis against live `ap` before editing. The cause is confirmed, not disproven.

---

## Exact correction

Edited file: `ap`.

1. Removed `bundle_mktemp`.
2. Added `bundle_alloc_tmp`, which must be called as a direct function in the current shell: `mktemp -d "${TMPDIR:-/tmp}/ap-bundle.XXXXXX"`, reject unexpected paths, append the created root to `bundle_tmp_list`, leave the root in `bundle_tmp`.
3. Derived child paths only after registration: `$bundle_tmp/objects`, `$bundle_tmp/payload`, `$bundle_tmp/zipgit`. Call sites: `bundle_scan_secrets`, payload staging in `cmd_bundle`, ZIP throwaway Git repository in `cmd_bundle`.
4. Split traps so signals terminate after cleanup:
   - `EXIT` → `bundle_cleanup`
   - `HUP` → `bundle_cleanup; exit 129`
   - `INT` → `bundle_cleanup; exit 130`
   - `TERM` → `bundle_cleanup; exit 143`
5. `bundle_cleanup` disarms those traps first, deletes only registered paths matching `*'/ap-bundle.'*` with `rm -rf --`, ignores already-removed paths (`|| true`), then clears `bundle_tmp_list`.

Why cleanup state now exists in the parent shell: registration is no longer a function side effect executed inside `$(...)`. `bundle_alloc_tmp` mutates `bundle_tmp_list` in the same shell that installed the traps. EXIT/HUP/INT/TERM therefore see every root created by that invocation.

No `rm -rf /tmp/ap-bundle.*`. Cleanup is limited to directories created and registered by the current process.

`sh -n ap` passed. There is no remaining `$(bundle_mktemp)` or `$(bundle_alloc_tmp)`.

---

## Independent validation

Disposable fixtures only. Isolated `HOME`, `XDG_STATE_HOME`, `XDG_CONFIG_HOME`, `TMPDIR`. The canonical dirty exporter correctly cannot export (`running ap` would not match `HEAD:ap` and the worktree is dirty). Tests used a disposable clone with a temporary commit of the corrected `ap` solely inside `/tmp`; that commit was not applied to `/home/agile/Projects/ap`. A decoy `$TMPDIR/ap-bundle.foreign-decoy` and an unrelated sentinel were retained across every scenario. 30/30 PASS. Fixtures were removed after the run.

### Successful export

Recorded matching temp directories before the run. Initial `ap bundle cons1 --initial` with `--companion-trace` exited 0, printed `READY:`, and produced a ZIP that `zipfile.testzip` accepted, containing `project.bundle`, `ap.bundle`, and `companion-trace.bundle`. After termination, no new `ap-bundle.*` directory from that invocation remained.

### Failure after temporary allocation

Tracked `.env` refused after `bundle_scan_secrets` had allocated a temp root. Non-zero exit; no leftover owned temps. A second failure after payload allocation (`nothing new to export`) also left no owned temps.

### SIGINT

Export held after allocation (`rev-list` wrapper). `timeout --signal=INT` terminated with status **130** (INT trap `exit 130`). Owned temps gone. Decoy retained. Unrelated `/tmp` paths were not deleted (isolated `TMPDIR` plus decoy/sentinel checks).

### SIGTERM

Same hold-after-allocation setup. `timeout --signal=TERM` terminated with status **143** (TERM trap `exit 143`). Owned temps gone. Decoy retained. This exercises the implemented TERM trap path, not merely default termination.

### Multiple temporary roots

One successful consumer+companion invocation created **5** `ap-bundle.*` mktemp roots: object-scan staging for project, `.ap`, and companion; payload staging; ZIP throwaway Git repository. All were gone after EXIT. Source repositories were untouched.

### Compact transport regression

- initial bundle creation
- local reconstruction: `git clone project.bundle` HEAD equals project HEAD
- cumulative incremental export and reconstruction to latest HEAD without the intermediate package
- companion payload present in the initial ZIP
- `nothing new to export`
- ignored `.env` does not dirty porcelain, export succeeds, `.env` absent from ZIP names
- tracked sensitive path refusal
- canonical AP self-bundle

Existing `ap bundle` UX and transport semantics were not redesigned.

---

## Security review of the cleanup path

| Risk | Disposition |
|---|---|
| Command-substitution side effects | Required cleanup state no longer depends on them |
| Word splitting | Heredoc reader with `IFS=` and quoted `"$bundle_tmp_one"` |
| Glob expansion | No `rm -rf .../ap-bundle.*`; `case` pattern is not a filename glob |
| Empty-variable `rm -rf` | Empty lines skipped; `rm -rf --` only on a non-empty `/ap-bundle.` path |
| Duplicate registration | `mktemp -d` yields unique roots; a duplicate `rm -rf` would still be safe |
| Cleanup after partial initialization | Failed `mktemp` is not registered; later `fail`/`exit` still runs EXIT cleanup |
| Traps firing more than once | `trap - EXIT HUP INT TERM` at the start of cleanup |
| Unexpected cleanup status | `rm ... \|\| true`; cleanup does not `exit` on the EXIT path |
| Masking the original failure | Tracked-secret and nothing-new paths remained non-zero |
| Unsafe paths outside this invocation | Only the current process list; foreign decoy survived |
| Already-removed or partial paths | Tolerated |

Out-of-scope Acceptance observations were not addressed.

---

## Changed files and purpose

Product (this Correction Worker):

- `ap` — parent-shell temporary-root allocation and owned-path cleanup so offline transport Git objects cannot remain in `${TMPDIR:-/tmp}` after the exporter exits.

Unchanged by this Worker (still part of the uncommitted implementation candidate):

- `AP.md`, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`, `PROMPT_ENGINEERING_PATTERNS.md`, `GLOSSARY.md`, `FAQ.md`, `INTUITION.md`, `INTEGRATION.md`, `README.md`, `UPDATING.md`, `CHANGELOG.md`, `docs/adr/README.md`, `docs/adr/0025-chatorchestrator-offline-bundle-transport.md`

Trace persistence (this file, Cooperator-requested after the Correction Worker had already stopped product work):

- `projects/ap/09/00-chat-orchestrator-offline-bundle-transport/04_report_00.md`

---

## `git diff --stat`

Whole uncommitted candidate, including the prior implementation plus this correction (`ap` grew from the implementation-era +1165 to +1180 lines vs HEAD):

```text
 AP.md                          |  150 ++++-
 AP_ORCHESTRATOR.md             |   19 +-
 CHANGELOG.md                   |   11 +
 FAQ.md                         |   16 +-
 GLOSSARY.md                    |    7 +-
 INTEGRATION.md                 |   10 +-
 INTUITION.md                   |    4 +-
 PROMPT_CONTRACTS.md            |   22 +-
 PROMPT_ENGINEERING_PATTERNS.md |    4 +-
 README.md                      |    6 +
 UPDATING.md                    |    3 +
 ap                             | 1181 +++++++++++++++++++++++++++++++++++++++-
 docs/adr/README.md             |    9 +
 13 files changed, 1399 insertions(+), 43 deletions(-)
```

Untracked: `docs/adr/0025-chatorchestrator-offline-bundle-transport.md`

## `git status --short`

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

Git result: no fetch, stage, commit, or push in the AP repository. No Meta commit or push. No consumer repository mutation.

---

## Deviations, risks, missing evidence

- This Worker does not independently certify the rest of the transport beyond the compact regression subset required by the correction prompt.
- Historical leftover `${TMPDIR:-/tmp}/ap-bundle.*` directories from earlier Implementation/Acceptance runs on the host, if any still exist outside this Worker's isolated `TMPDIR`, were not glob-deleted (that would violate owned-path cleanup). They are not evidence that the corrected path still leaks.
- `Correction re-acceptance: full-fresh` because the change is runtime cleanup of directories that can hold complete Git history: scoped re-acceptance would be invalid for a security-boundary/runtime-behavior correction.
- No independently observed current public branch evidence.

---

## Smallest next step

Issue a fresh independent re-Acceptance Worker (`fresh-worker-session`) against the same uncommitted candidate. That Worker must independently re-check temporary-root cleanup (success, failure after allocation, SIGINT/SIGTERM, multiple roots) and that transport semantics are unchanged. Do not treat this report as acceptance-PASS.

Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: the disposable SIGINT/SIGTERM harness first wrote a git wrapper that was not named `git` on `PATH`; renamed before those signal tests ran. Product `ap` was unaffected.
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the Correction Worker grant; no autonomous continuation. Persistence of this companion file was a later Cooperator-requested reporting write, not a new mutation grant over `ap`.
