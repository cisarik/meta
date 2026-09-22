Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 08
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-C1
Native planning mode: not-used
Continuity anchor: your terminal report 08_report_00.md (session 08, exchange 01)
Delivery route: manual Cooperator delivery to the same Worker session
Reasoning recommendation: Extra High
Reasoning basis: completion of the bounded A1-F01 correction and the deterministic root rebuild; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: reversible allowlisted edits already present, tests, one local commit, and guarded local ref construction; no push; re-acceptance is a separate fresh session
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika C1 (exchange 02) — commit the correction and rebuild the public root

You are the same Worker session that produced `08_report_00.md`. Your prior
authority expired at that terminal report. This is a complete renewed grant:
the Orchestrator has decided the open question, and you are authorized to
finish C1 exactly as bounded below. Retained context is convenience, not
authority; re-establish repository evidence and stop on any conflict between
your memory and the current tree.

Confirm you are the session that produced `08_report_00.md`. If this prompt
arrives in a different session, stop and report the mismatch instead of acting.

Native Plan Mode must be **OFF**. Do not use subagents. Do not push, add a
remote, or close the logical whole.

```text
STOP: Native Plan Mode off. This is implementation, not planning.
STOP: Finish C1 only. No new wording edits, no test-isolation fix, no other
      finding, no feature work.
STOP: Do not recreate or delete any branch. Lab, work, and the previous public
      root are recovery points.
STOP: Do not open, quote, copy, or display docs/environment.md.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Preserve the upload-unavailable runtime behavior (CLI exit 2, HTTP 501,
      engine E_UPLOAD_FAILED). Only the wording and the contract description
      change.
STOP: Do not spawn Workers or subagents.
```

## Orchestrator decision on your blocker

Your focused-command failure is classified as a **pre-existing test-isolation
ordering dependency**, not a product defect and not a C1 regression:

- The four quiet-stderr tests fail only when `logging.basicConfig` was never
  installed by `serve()`. In the declared full discover,
  `tests.unit.test_bridge_startup` runs earlier and configures logging, so the
  same four tests pass.
- The Orchestrator re-ran the focused set with
  `tests.unit.test_bridge_startup` included first: 348 tests, OK. The four
  tests and the `configured_job_executor` fallback warning are unchanged from
  `b5b5f381`.
- Decision: park the test-isolation defect as an out-of-scope observation. Do
  **not** fix it in C1. No separate isolation fix is authorized.

The corrected focused command for this completion is:

```bash
python -m unittest tests.unit.test_bridge_startup tests.unit.test_cli \
    tests.unit.test_client tests.unit.test_bridge_jobs \
    tests.contract.test_schemas tests.contract.test_extension_syntax
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 08
Worker exchange ordinal: 02
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: b5b5f3811f62d5c83dd411c627a1783fb1bd5d93 (work branch HEAD;
  tree 8506c9955b448d913cafe03c08b0c3e5495f9952); current main and
  public/kronika-initial = 827dae85c2794914c3adcb467de9b21ee8998463
Changed-path allowlist: the eight uncommitted paths already present
Implementation boundaries: commit the already-reviewed A1-F01 correction, then
  rebuild the one-commit public root and move main and public/kronika-initial
  with old-value guards; no publication
Independence required: no
```

## Repository gate (before mutation)

Working directory: `/home/agile/Tools/cli_chatgpt`

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == work/kronika-clean-start
HEAD == b5b5f3811f62d5c83dd411c627a1783fb1bd5d93
main == public/kronika-initial == 827dae85c2794914c3adcb467de9b21ee8998463
lab/cli-chatgpt-190 == 2727451d2502925377637e19fa435917c970a996, 190 commits
no remotes
HEAD:.ap == .ap HEAD == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
no locks, rebase, cherry-pick, merge, or replace refs
dirty paths == exactly the eight allowlisted files below, no untracked files
```

On any mismatch stop `BLOCKED` and report the difference. Do not repair,
switch, reset, clean, or stash.

## Step 1 — verify the uncommitted correction

The worktree must contain exactly these modified paths and nothing else:

```text
contracts/http-api.v1.json
extension/src/engine/dom_engine.js
extension/src/job_runner.js
src/kronika/bridge/server.py
src/kronika/cli.py
tests/contract/test_schemas.py
tests/unit/test_bridge_jobs.py
tests/unit/test_client.py
```

Verify the diff matches the C1 requirements: the canonical message
`file upload is not available in this build` in the CLI description, `--file`
help, CLI rejection, bridge 501 message, engine comment and message, runner
message; the `GET /v1/files/{fid}` entry with the error-envelope response and
status `[401, 404, 501]`; and the three test updates including the new
`test_file_get_describes_permanent_unavailability`. If anything differs, stop
and report the exact difference.

Note: `src/chatgpt_cli/` does not exist; the predecessor sentence you reported
was in `src/kronika/cli.py` and is already corrected. Do not create any file
under `src/chatgpt_cli/`.

## Step 2 — validation on the exact content to be committed

```bash
bash scripts/dev-setup.sh
python -m unittest tests.unit.test_bridge_startup tests.unit.test_cli \
    tests.unit.test_client tests.unit.test_bridge_jobs \
    tests.contract.test_schemas tests.contract.test_extension_syntax
python -m unittest discover -s tests -t .
```

Use `.venv` Python through a bash child (bare `python` argv is intercepted by
the client appimage and is not product evidence). Disclose any skip. Confirm:

```text
python -m kronika ask -f <path>  -> exit 2, message "error: file upload is not
                                    available in this build", no state created
python -m kronika --version      -> kronika 0.1.0
```

## Step 3 — Stage A commit

Stage exactly the eight reviewed paths (never `git add .` / `git add -A`) and
create one local commit on `work/kronika-clean-start`:

```text
fix(cli): describe file upload as unavailable
```

Read back the commit SHA (`KRONIKA_CLEAN`) and its tree, then confirm
`git status --porcelain` is empty.

## Step 4 — Stage B root rebuild

Only after Stage 3 is green. Re-run the gate, then:

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
git diff --exit-code "$KRONIKA_CLEAN^{tree}" "main^{tree}"
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

No `-p` in `commit-tree`. No push, fetch, remote add, force, branch deletion,
or config write.

## Stop conditions

Any failed gate; any test failure on the corrected commands; a dirty path
outside the eight; the refs not at their expected old values; worktree not
clean after Stage 3 or Stage 4; AP pin mismatch; request to push or add a
remote; any need to open `docs/environment.md`.

Recovery: `work/kronika-clean-start`, `lab/cli-chatgpt-190`, and the previous
root `827dae85` (reflog) remain. Guarded ref updates leave the previous root
as `main` if Stage B fails.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/08_report_01.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 08, exchange 02). Include the
start/end state, confirmation that the committed diff is exactly the eight
reviewed paths, the corrected focused and full suite results with skips, the
behavior checks, the correction commit SHA/tree, the new parentless root
SHA/tree, the previous root SHA, the guarded ref readbacks, the no-ancestry
proof, and:

```text
Logical-whole closure: not-closed
```

`PASS` means A1-F01 is committed and the corrected tree is the new one-commit
local `main`, and the report was saved. Then stop. A fresh independent
re-acceptance is a later grant.
