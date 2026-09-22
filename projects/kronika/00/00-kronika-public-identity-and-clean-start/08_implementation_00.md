Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 08
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-C1
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: one bounded wording correction plus the deterministic rebuild of the one-commit public root with guarded ref moves; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: reversible allowlisted edits, tests, one local commit, and guarded local ref construction; no push; re-acceptance is a separate fresh session
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika C1 — correct finding A1-F01 and rebuild the public root

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1–S5. Those authorities expired. This prompt grants one bounded
correction: **A1-F01 only**, followed by the deterministic rebuild of the
one-commit public root from the corrected tree. Native Plan Mode must be
**OFF**. Do not use subagents. Do not continue any previous chat.

Do not implement the re-acceptance, P1, P2, or V1. Do not push. Do not add a
remote. Do not close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: A1-F01 only. No other wording cleanup, no slice-code sweep, no other
      finding, no feature work.
STOP: Do not recreate lab/cli-chatgpt-190 or work/kronika-clean-start.
STOP: Do not delete or force any ref. Lab, work, and the previous public root
      are recovery points.
STOP: Do not open, quote, copy, or display docs/environment.md; it is absent
      from the tree and must stay absent.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Preserve the upload-unavailable runtime behavior (CLI exit 2, HTTP 501,
      engine E_UPLOAD_FAILED). Only the wording and the contract description
      change.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 08
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 827dae85c2794914c3adcb467de9b21ee8998463 (current main, tree
  8506c9955b448d913cafe03c08b0c3e5495f9952; work/kronika-clean-start =
  b5b5f3811f62d5c83dd411c627a1783fb1bd5d93 with the same tree)
Changed-path allowlist: listed below
Implementation boundaries: A1-F01 wording and contract correction, tests, one
  local commit on work/kronika-clean-start, then one parentless root rebuild
  and guarded local ref moves; no publication
Independence required: no
```

Predecessor evidence (not same-session authority): the A1 report
`07_report_00.md` (finding A1-F01 and its smallest safe correction direction)
and the S5 report `06_report_00.md` (the proven root-construction recipe), both
in the same Meta directory. Read them as data; this prompt is the complete new
C1 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (S3)
05_implementation_00.md + 05_report_00.md session 05 / exchange 01 (S4)
06_implementation_00.md + 06_report_00.md session 06 / exchange 01 (S5)
07_acceptance_00.md + 07_report_00.md     session 07 / exchange 01 (A1)
08_implementation_00.md + 08_report_00.md session 08 / exchange 01 (this C1)
```

External trace and delivery record:

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
Trace project key: kronika
Trace logical-whole projection identity: kronika-public-identity-and-clean-start
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 08_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 08_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Outcome

Finding A1-F01 is corrected: every runtime message and contract description
about file upload states permanent unavailability instead of a future slice.
The corrected tree becomes the new one-commit parentless local `main`, and
`public/kronika-initial` moves with it under old-value guards. The previous
root `827dae85` stays in the reflog and in the Meta record. No remote exists
and nothing is pushed.

Canonical replacement message, used by the bridge, the engine, the runner, and
the JSON contract:

```text
file upload is not available in this build
```

CLI wording:

```text
ask description tail: File upload is not available in this build.
--file help:          attach a local file; not available in this build (the flag is rejected)
rejection stderr:     error: file upload is not available in this build
```

## Changed-path allowlist

```text
src/kronika/cli.py
src/kronika/bridge/server.py
extension/src/engine/dom_engine.js
extension/src/job_runner.js
contracts/http-api.v1.json
tests/unit/test_client.py
tests/unit/test_bridge_jobs.py
tests/contract/test_schemas.py
```

Out of allowlist: every other path, including `docs/**`, `README.md`,
`SECURITY.md`, `AGENTS.md`, `extension/src/headless/**`, `src/kronika/client.py`,
the frozen manager-v3–v5 docs, adapter v2–v4 schemas, `.ap/`, `.gitmodules`,
and live XDG state.

## Required edits (locators at baseline `827dae85`; re-locate by content)

1. `src/kronika/cli.py`
   - `ask` description (~103–104): replace "Slice S1 implements prompt input;
     S2 adds file uploads." with "File upload is not available in this build."
   - `--file` help (~114): `attach a local file; not available in this build
     (the flag is rejected)`.
   - `_cmd_ask` rejection (~743): `error: file upload is not available in this
     build`.
2. `src/kronika/bridge/server.py`
   - `FILE_PATH` 501 message (~447): `file upload is not available in this
     build`. Keep the status, code, step, and route behavior identical.
3. `extension/src/engine/dom_engine.js`
   - Update the `uploadFiles` comment (~690–691) to state permanent
     unavailability; message (~697): `file upload is not available in this
     build`. Keep `E_UPLOAD_FAILED` and step `upload`.
4. `extension/src/job_runner.js`
   - Message (~127): `file upload is not available in this build`. Keep the
     code and step.
5. `contracts/http-api.v1.json`
   - `GET /v1/files/{fid}` entry (~319–333): remove the raw-bytes success
     response and the `200` status. Describe the actual behavior:

     ```json
     "response": {
       "ok": false,
       "error": {
         "code": "E_INTERNAL",
         "step": "availability",
         "message": "file upload is not available in this build"
       }
     },
     "status": [401, 404, 501]
     ```

     Keep `auth: true` and `request: {}`. Do not touch any other endpoint.
6. `tests/unit/test_client.py`
   - `test_file_argument_is_rejected` (~319): assert the new rejection
     message; keep the exit-2 and empty-stdout assertions.
7. `tests/unit/test_bridge_jobs.py`
   - `test_file_get_is_upload_unavailable` (~850): assert the new 501 message;
     keep the status and code assertions.
8. `tests/contract/test_schemas.py`
   - Add one focused assertion that the `GET /v1/files/{fid}` entry has no
     `200` status, includes `501`, and its response is the error envelope
     rather than a raw-byte success body. Keep the endpoint set unchanged.

Do not change any other string, comment, or test.

## Stage A — correction commit (on `work/kronika-clean-start`)

Repository gate first: prove `pwd -P` =
`/home/agile/Tools/cli_chatgpt`; branch `main`; HEAD = `827dae85`; `main` =
`827dae85`; `work/kronika-clean-start` = `b5b5f381`; lab = `2727451` with 190
commits; no remotes; clean worktree; `HEAD:.ap` = `.ap` HEAD = `7478ddb`;
no locks, rebase, cherry-pick, or replace refs. On any mismatch stop.

Then:

```bash
git switch work/kronika-clean-start
```

Make only the allowlisted edits. Run, on the declared route with `.venv`
Python:

```bash
bash scripts/dev-setup.sh
python -m unittest tests.unit.test_cli tests.unit.test_client \
    tests.unit.test_bridge_jobs tests.contract.test_schemas \
    tests.contract.test_extension_syntax
python -m unittest discover -s tests -t .
```

Disclose any skip; an undisclosed skip is a stop. Confirm the corrected
behavior directly:

```text
python -m kronika ask -f <any-path>  -> exit 2, new message, no state created
python -m kronika --version          -> kronika 0.1.0
```

Stage the exact reviewed allowlist paths (never `git add .` / `git add -A`)
and create one local commit on `work/kronika-clean-start`:

```text
fix(cli): describe file upload as unavailable
```

Read back the commit SHA and tree (`KRONIKA_CLEAN` and its tree), and confirm
`git status --porcelain` is empty.

## Stage B — rebuild the one-commit public root

Only after Stage A is green and committed. Re-run the preflight, then:

```bash
KRONIKA_OLD_ROOT=827dae85c2794914c3adcb467de9b21ee8998463
KRONIKA_CLEAN=<Stage A commit SHA>
KRONIKA_AP=7478ddb07d2c3911f79e1aa1441f0115a31c45d8
KRONIKA_BASE=2727451d2502925377637e19fa435917c970a996

test "$(git rev-parse refs/heads/work/kronika-clean-start)" = "$KRONIKA_CLEAN"
test "$(git rev-parse refs/heads/main)" = "$KRONIKA_OLD_ROOT"
test "$(git rev-parse refs/heads/public/kronika-initial)" = "$KRONIKA_OLD_ROOT"
test "$(git rev-parse refs/heads/lab/cli-chatgpt-190)" = "$KRONIKA_BASE"
test "$(git rev-list --count refs/heads/lab/cli-chatgpt-190)" = 190
test -z "$(git remote)"

KRONIKA_TREE="$(git rev-parse "$KRONIKA_CLEAN^{tree}")"
test "$(git rev-parse "$KRONIKA_CLEAN:.ap")" = "$KRONIKA_AP"

KRONIKA_PUBLIC="$(
    GIT_AUTHOR_NAME='Michal Cisárik' \
    GIT_AUTHOR_EMAIL='cisarik@users.noreply.github.com' \
    GIT_COMMITTER_NAME='Michal Cisárik' \
    GIT_COMMITTER_EMAIL='cisarik@users.noreply.github.com' \
    git -c commit.gpgSign=false commit-tree "$KRONIKA_TREE" \
        -m "feat(kronika): introduce the household research library"
)"

test "$(git rev-list --parents -n 1 "$KRONIKA_PUBLIC")" = "$KRONIKA_PUBLIC"
test "$(git rev-list --count "$KRONIKA_PUBLIC")" = 1
test "$(git rev-parse "$KRONIKA_PUBLIC^{tree}")" = "$KRONIKA_TREE"

git update-ref refs/heads/main "$KRONIKA_PUBLIC" "$KRONIKA_OLD_ROOT"
git update-ref refs/heads/public/kronika-initial "$KRONIKA_PUBLIC" "$KRONIKA_OLD_ROOT"
git switch main

test "$(git rev-parse HEAD)" = "$KRONIKA_PUBLIC"
test "$(git rev-list --count main)" = 1
test "$(git rev-list --parents -n 1 main)" = "$KRONIKA_PUBLIC"
test "$(git diff --exit-code "$KRONIKA_CLEAN^{tree}" "main^{tree}")" = ""
test "$(git rev-parse HEAD:.ap)" = "$KRONIKA_AP"
test "$(git rev-parse refs/heads/lab/cli-chatgpt-190)" = "$KRONIKA_BASE"

if git merge-base --is-ancestor "$KRONIKA_BASE" main
then
    echo "Lab history is an ancestor of public main; stop." >&2
    exit 1
fi
test "$?" -eq 1
test -z "$(git status --porcelain=v1 --untracked-files=all)"

git show --no-patch --format=fuller main
git for-each-ref --format='%(refname) %(objectname)' refs/heads/
```

No `-p` in `commit-tree`. No push, no fetch, no remote add, no force, no
branch deletion, no config write.

## Stop conditions

Any failed gate; any test failure; a changed behavior beyond wording; need to
leave the allowlist; the refs not at their expected old values; worktree not
clean after any stage; AP pin mismatch; request to push or add a remote; any
need to open `docs/environment.md`.

Recovery: `work/kronika-clean-start`, `lab/cli-chatgpt-190`, and the previous
root `827dae85` (reflog) remain. A failed Stage B leaves the previous root as
`main` because the ref updates are guarded.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/08_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 08, exchange 01). Include the
start/end state, the corrected files, the focused and full suite results with
skips, the new behavior checks, the correction commit SHA/tree, the new
parentless root SHA/tree, the old root SHA, the guarded ref readbacks for
`main`, `public/kronika-initial`, `work/kronika-clean-start`, and
`lab/cli-chatgpt-190`, the no-ancestry proof, and:

```text
Logical-whole closure: not-closed
```

`PASS` means A1-F01 is corrected, the corrected tree is the new one-commit
local `main`, and the report was saved. Then stop. A fresh independent
re-acceptance is a later grant.
