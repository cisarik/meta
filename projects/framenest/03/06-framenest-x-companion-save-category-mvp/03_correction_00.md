# Authoritative Prompt for Fresh Worker 03

## FrameNest × X Companion Save Category — Align stale head and AP-pin test literals

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 02 produced a local four-commit candidate at
`16b1727104b4172c72a8b4d21be98dcbfee87df8` and reported **PARTIAL** because the
required full Python suite was not green. That implementation authority is
expired. Do not resume Worker 02. Do not enter Native Plan Mode. Do not reopen
Save UX, the status bridge, photo transport, or Surface B/C.

The ORCHESTRATOR verified the candidate against the repository: four commits
from baseline `226d6e2`, ADR-0061/0062/0063 untouched, schema `0030`, four
Save category radios, honest `reduceXSaveOutcome`, `companion_mutation` still
exactly the two X POST routes, X staging `artifact.bin`, YouTube default
`artifact.mp4`. Causal Node suite 47 passed. Full Python suite: 3117 passed,
10 failed, 8 skipped.

The ten failures are **stale literals**, already wrong on the authorized
Worker 02 baseline (schema head was already `0029`, AP gitlink already
`9c5cc44f…`):

- `tests/contract/test_ap_integration.py` expects AP `17b7e085…`
- nine assertions still expect Alembic `0028` after `upgrade_database_to_head`
  / packaged head in CLI, backup, and production-runtime tests

Worker 02 correctly refused to patch them: they were outside its Section 11
allowlist. This grant exists solely to close that full-suite gate.

If Native Plan Mode is on, stop `BLOCKED`. Medium reasoning is sufficient.
Do not use Extra High or Max.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-save-category-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SAVE-CATEGORY-HEAD-LITERALS-03
Task type: bounded stale-literal correction for required full-suite gate
Native planning mode: not-used
Reasoning recommendation: medium
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 02
Prior authorities: expired
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: no
Changed material axis: none
Routing reopened for: none
Unchanged axes reopened: none
Ordinary-only trigger: yes
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Explore-style task: not-used
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 16b1727104b4172c72a8b4d21be98dcbfee87df8
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: test-literal alignment to already-shipped schema 0030 and governing AP pin; no product, schema, or trust-boundary change
Authorized implementation stages: update the named literals; run the named tests; one local commit; one full Python suite
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit, focused tests, and one full Python suite
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest canonical checkout on feat/x-meme-browser-companion
Declared reversible class: reversible local test literals and one local Git commit
Working-copy topology: canonical-checkout
Topology rationale: correction must sit on Worker 02's four unpublished commits
Irreversible exclusions: secrets, destruction, accounts, public exposure, publication, closure, NUC, push, signed-in X, provider calls, product/schema/extension edits
```

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh bounded correction session
```

Repository artifacts and the terminal report: professional English. Czech
forbidden. Report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Implementation PASS is not acceptance, publication, deployment, or
ORCHESTRATOR closure.

---

## 1. Trace and Meta write

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/06-framenest-x-companion-save-category-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/06-framenest-x-companion-save-category-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_correction_00.md
Destination path: projects/framenest/03/06-framenest-x-companion-save-category-mvp/03_correction_00.md
Archival: wait-for-report
```

You may **read**:

```text
/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/02_implementation_00.md
/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/02_report_00.md
```

You may **write** only:

```text
/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/03_report_00.md
```

Do not stage or commit Meta. If the report path cannot be written, return the
complete report in chat. Do not invent another filename.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Native planning mode `not-used`;
Medium; no Extra High; no Max; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
commit: 16b1727104b4172c72a8b4d21be98dcbfee87df8
parent: b213e5eb7233d9b5e08a2f6eeb382ea2d1f90183
tree: e28e5816c02a4d80f1f7e0726ff9dea502a44223
subject: docs: record X category and photo acquisition contract
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
schema head: Alembic 0030
Working tree: expected clean
Upstream: none configured (expected)
```

If HEAD is not `16b1727…`, stop `BLOCKED` unless the only difference is this
Worker's own later commits. Do not `git fetch`. Do not switch local `main`.
Preserve unrelated dirty state.

Re-verify public refs without fetch:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

Issuance-time expected: FrameNest `045f33b44897a6f3949cc515792336396f1d33a1`,
AP `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. Stop `BLOCKED` only if a new
public commit materially conflicts with this literal-only correction.

---

## 3. Required correction

Update **only** literals that mean “current packaged Alembic head” or
“governing AP gitlink”.

1. `tests/contract/test_ap_integration.py`
   `EXPECTED_AP_COMMIT` must become
   `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

2. Replace current-head Alembic `0028` with `0030` in:

```text
tests/contract/test_persistence_cli.py
tests/unit/infrastructure/backup/test_catalog_backup.py
tests/unit/infrastructure/runtime/test_production_runtime.py
```

Those `0028` strings are expectations after `upgrade_database_to_head` or
packaged `head_revision`, not historical backup fixtures of an old release.
Do not invent a dual-head matrix. Do not change CLI, backup, or runtime
**product** code to emit `0028`.

Do not touch `index.html` cockpit copy. That residual stays parked.

Do not amend, squash, or rewrite Worker 02's four commits.

---

## 4. Out of scope

- Save popup, status bridge, photo transport, category API, migration `0030`
  body, extension JS beyond leaving it untouched
- Surface B/C, Analyze execution, origins, `x_acquisition_root`
- ADR-0061/0062/0063/0064 body edits
- Dependency or AP submodule mutation
- Independent INFOSEC R3, push, NUC, Brave Reload

---

## 5. Negative authority

You must not:

- push, fetch, switch branch, merge, rebase, stash, reset, clean, amend, tag,
  or update submodules;
- edit any path outside Section 7;
- change product behavior so stale tests pass;
- contact X or `pbs.twimg.com`;
- use sudo, SSH, or Michal's Brave profile;
- close the logical whole or claim independent acceptance.

---

## 6. Canonical execution routes

Cursor/AppImage ambient Python is untrusted. Do not invoke raw
`.venv/bin/python`, `python`, `python3`, or `poetry run` for Python evidence.

Until the first authorized local commit exists, `--baseline` is
`16b1727104b4172c72a8b4d21be98dcbfee87df8`. After the authorized commit,
subsequent `ap project check` / `ap exec` uses that new SHA.

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>

./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation runtime-info

./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation test-focus -- \
  tests/contract/test_ap_integration.py \
  tests/contract/test_persistence_cli.py \
  tests/unit/infrastructure/backup/test_catalog_backup.py \
  tests/unit/infrastructure/runtime/test_production_runtime.py \
  -q -p no:cacheprovider
```

After focused success and the local commit, run **once**:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation test
```

Then:

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

PASS of this correction requires the full Python suite green (exit 0) and
those two Node files green. Do not loop an unchanged failing full suite.
Do not hide non-zero exits.

NUC gate: not activated.

---

## 7. Changed-path allowlist

```text
tests/contract/test_ap_integration.py
tests/contract/test_persistence_cli.py
tests/unit/infrastructure/backup/test_catalog_backup.py
tests/unit/infrastructure/runtime/test_production_runtime.py
```

---

## 8. Git authority

```text
Fetch: forbidden
Worktree/clone creation: forbidden
Branch: stay on existing feat/x-meme-browser-companion
Stage: exact allowlisted paths only; never git add . or git add -A
Commit: one local commit after focused tests pass
Amend: forbidden
Push: forbidden
Tags: forbidden
```

Suggested subject:

```text
test: align schema-head and AP pin assertions with 0030 and 9c5cc44
```

Do not commit secrets, media bytes, or Meta files.

---

## 9. Completion, report, and expiry

Write `/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/03_report_00.md`.

Begin exactly with `### Report for ORCHESTRATOR_CHAT` and echo once:

```text
Logical whole identity: framenest-x-companion-save-category-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
```

Include terminal status; `Phase-qualified result: implementation-PASS` only
if the full Python suite exits 0; `Logical-whole closure: not-closed`;
capability handshake; baseline and final HEAD/parent/tree/subject; exact
changed paths; commands with `--baseline` and exit codes; proof no product
path changed; `Resolved Execution Issues / Near-Misses`; `Pre-Existing
Failure Classification`; justification `new-mutation`; authority expiry; one
smallest next step (Orchestrator: Michal Reload-unpacked Save look, then
later independent R3).

PASS requires: the four files updated only as specified; focused tests green;
full Python suite exit 0; Node pair green; one commit; no push; Worker 02
commits remain ancestors.

PARTIAL if a named allowlisted assertion was not a current-head literal and
you stopped rather than guessing. BLOCKED on baseline contradiction.

After the terminal report, stop. Plan UI or chat `Continue` does not renew
this authority.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 03 • Medium
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 03_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/03_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/03_report_00.md
✅ Archival: wait-for-report
```
