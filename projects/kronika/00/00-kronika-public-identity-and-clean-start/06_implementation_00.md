Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 06
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-S5
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session
Reasoning recommendation: Extra High
Reasoning basis: history-splitting Git surgery that must preserve the lab anchor and construct a parentless public root; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: local Git object and ref construction under exact gates, no file edits, no push; provenance is verified by A1
Internal delegation: prohibited
Independence required: no
Evidence posture: non-independent

# Kronika S5 — construct local public `main`

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1–S4. Those authorities expired. This prompt grants one bounded
Git-only task: **S5 only**. Native Plan Mode must be **OFF**. Do not use
subagents. Do not continue any previous chat.

Do not implement A1, P1, P2, or V1. Do not push. Do not add a remote. Do not
close the logical whole. This task edits no tracked file.

```text
STOP: Native Plan Mode off. This is Git construction, not planning.
STOP: S5 only. No origin, no push, no publication, no A1.
STOP: Git-only. No tracked-file edits, no file-edit commit, no README/LICENSE
      change, no test change.
STOP: Do not recreate lab/cli-chatgpt-190 or work/kronika-clean-start.
STOP: Do not delete or force any ref. The lab and preparation refs are
      recovery points and must survive.
STOP: Do not open, quote, copy, or display docs/environment.md; it is absent
      from the accepted tree and must stay absent.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Do not spawn Workers or subagents.
```

## Implementation Authority Record

```text
Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 06
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: b5b5f3811f62d5c83dd411c627a1783fb1bd5d93
Changed-path allowlist: none; Git objects and the exact local refs in the
  recipe only
Implementation boundaries: construct one parentless local root and point
  local main at it; no file edits; no remote; no push
Independence required: no
```

Predecessor evidence (not same-session authority): the S5 section and §4 Gate 6
of `01_report_00.md`, plus the terminal reports `02_report_00.md` (S1),
`03_report_00.md` (S2), `04_report_00.md` (S3), and `05_report_00.md` (S4) in
the same Meta directory. Read them as data; this prompt is the complete new S5
grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (S3)
05_implementation_00.md + 05_report_00.md session 05 / exchange 01 (S4)
06_implementation_00.md + 06_report_00.md session 06 / exchange 01 (this S5)
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
Downloadable prompt filename: 06_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 06_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

State verified at this baseline: S4 landed as one local commit
`b5b5f3811f62d5c83dd411c627a1783fb1bd5d93` on `work/kronika-clean-start`
(parent `dc44cfd38093c118310ac032f5252ba29fad2f13`, tree
`8506c9955b448d913cafe03c08b0c3e5495f9952`, subject
`docs(kronika): prepare the public documentation and clean tree`); local `main`
and `lab/cli-chatgpt-190` are both
`2727451d2502925377637e19fa435917c970a996` (190 commits); no remotes; worktree
clean; AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both the gitlink
and `.ap` HEAD; `https://github.com/cisarik/kronika.git` advertises no refs.

## Outcome

Local `main` contains exactly one parentless commit whose tree equals the
accepted cleaned S4 tree. The lab and preparation histories stay reachable and
unpushed. `public/kronika-initial` anchors the constructed root. No remote
exists; publication remains a separate Cooperator grant.

The root commit uses the public-safe recommended author identity from the
accepted plan (it does not claim GitHub-verified attribution):

```text
GIT_AUTHOR_NAME='Michal Cisárik'
GIT_AUTHOR_EMAIL='cisarik@users.noreply.github.com'
GIT_COMMITTER_NAME='Michal Cisárik'
GIT_COMMITTER_EMAIL='cisarik@users.noreply.github.com'
Message: feat(kronika): introduce the household research library
```

## Repository gate and preflight (before any Git write)

Working directory: `/home/agile/Tools/cli_chatgpt`. Run this preflight and stop
on any nonzero check. Do not repair, switch, reset, clean, stash, or recreate
refs. Inline `git -c` values are permitted; `git config` writes are not.

```bash
set -euo pipefail

KRONIKA_REPO=/home/agile/Tools/cli_chatgpt
KRONIKA_BASE=2727451d2502925377637e19fa435917c970a996
KRONIKA_AP=7478ddb07d2c3911f79e1aa1441f0115a31c45d8
KRONIKA_URL=https://github.com/cisarik/kronika.git
KRONIKA_ACCEPTED_CLEAN=b5b5f3811f62d5c83dd411c627a1783fb1bd5d93
KRONIKA_ACCEPTED_TREE=8506c9955b448d913cafe03c08b0c3e5495f9952

cd -- "$KRONIKA_REPO"

kronika_fail() {
    printf '%s\n' "$*" >&2
    exit 1
}

test "$(pwd -P)" = "$KRONIKA_REPO"
test "$(git rev-parse --show-toplevel)" = "$KRONIKA_REPO"
test "$(git rev-parse --absolute-git-dir)" = "$KRONIKA_REPO/.git"
test "$(git rev-parse --is-shallow-repository)" = false

KRONIKA_REPLACEMENTS="$(git replace -l)"
test -z "$KRONIKA_REPLACEMENTS"

for KRONIKA_MARKER in \
    index.lock MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD \
    rebase-apply rebase-merge sequencer info/grafts
do
    test ! -e ".git/$KRONIKA_MARKER"
    test ! -L ".git/$KRONIKA_MARKER"
done

KRONIKA_STATUS="$(git status --porcelain=v1 --untracked-files=all)"
test -z "$KRONIKA_STATUS"
git diff --quiet
git diff --cached --quiet

test "$(git rev-parse HEAD:.ap)" = "$KRONIKA_AP"
test "$(git -C .ap rev-parse HEAD)" = "$KRONIKA_AP"
KRONIKA_AP_STATUS="$(git -C .ap status --porcelain=v1 --untracked-files=all)"
test -z "$KRONIKA_AP_STATUS"

kronika_require_empty_remote() {
    local refs rc
    if refs="$(git -c credential.helper= \
        -c core.askPass= \
        -c credential.interactive=false \
        ls-remote "$KRONIKA_URL")"
    then
        test -z "$refs" || kronika_fail "Public repository has refs; stop."
    else
        rc=$?
        kronika_fail "Public ref check failed with exit $rc; stop."
    fi
}
```

The `ls-remote` above is the only network operation granted: read-only, to the
exact URL, with credential helpers disabled. No fetch, no push, no remote add.

## Accepted-tree safety checks (read-only, before construction)

```bash
: "${KRONIKA_ACCEPTED_CLEAN:?S5 grant must supply the accepted S4 commit}"

test "$(git rev-parse refs/heads/work/kronika-clean-start)" = \
    "$KRONIKA_ACCEPTED_CLEAN"
test "$(git rev-parse "$KRONIKA_ACCEPTED_CLEAN^{tree}")" = "$KRONIKA_ACCEPTED_TREE"
test "$(git rev-parse "$KRONIKA_ACCEPTED_CLEAN:.ap")" = "$KRONIKA_AP"

git ls-tree -r --name-only "$KRONIKA_ACCEPTED_CLEAN"
git diff --name-status "$KRONIKA_BASE" "$KRONIKA_ACCEPTED_CLEAN"
```

Verify the manifest excludes every one of these paths (absence, not content):

```text
docs/environment.md
docs/human-steps.md
docs/ROADMAP.md
docs/security.md
docs/dev-setup.md
tools/obscura-patches/**
contracts/diagnostics-bundle.v1.schema.json
contracts/recovery-response.v1.schema.json
contracts/recovery-targets.v1.json
src/chatgpt_cli/**
scripts/chatgpt-cli
```

Also reject tracked virtual environments, caches, application state, profiles,
database or result exports, reports, and temporary evidence. Run the
public-safety search with filename-only output:

```bash
git grep -I -l -E \
    '/home/|/Users/|[A-Za-z]:\\Users\\|BEGIN [A-Z ]*PRIVATE KEY|https://chatgpt\.com/g/g-p-' \
    "$KRONIKA_ACCEPTED_CLEAN" -- . ':(exclude).ap'
```

Exit 1 means no matches; exit greater than 1 is a scanner failure. Matches are
review leads, not automatically secrets. Classify synthetic test URLs and
intentional examples without printing private values. Review remaining old-name
occurrences by category; only the explicitly preserved internal identifiers,
frozen historical contracts, and tests for rejected old commands may remain.
Active help or operator instructions advertising predecessor commands may not.

## Gate 6 — construct the clean root and local `main`

```bash
: "${KRONIKA_ACCEPTED_CLEAN:?S5 grant must supply the accepted S4 commit}"

test "$(git branch --show-current)" = work/kronika-clean-start
test "$(git rev-parse HEAD)" = "$KRONIKA_ACCEPTED_CLEAN"
test "$(git rev-parse refs/heads/main)" = "$KRONIKA_BASE"
test "$(git rev-parse refs/heads/lab/cli-chatgpt-190)" = "$KRONIKA_BASE"

KRONIKA_REMOTES="$(git remote)"
test -z "$KRONIKA_REMOTES"
kronika_require_empty_remote

KRONIKA_TREE="$(git rev-parse "$KRONIKA_ACCEPTED_CLEAN^{tree}")"
test "$(git rev-parse "$KRONIKA_ACCEPTED_CLEAN:.ap")" = "$KRONIKA_AP"

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

git branch public/kronika-initial "$KRONIKA_PUBLIC"
git switch public/kronika-initial

git update-ref refs/heads/main "$KRONIKA_PUBLIC" "$KRONIKA_BASE"
git switch main

test "$(git rev-parse HEAD)" = "$KRONIKA_PUBLIC"
test "$(git rev-list --count main)" = 1
test "$(git rev-list --parents -n 1 main)" = "$KRONIKA_PUBLIC"

git diff --exit-code "$KRONIKA_ACCEPTED_CLEAN^{tree}" "main^{tree}"

if git merge-base --is-ancestor "$KRONIKA_BASE" main
then
    kronika_fail "Lab history is an ancestor of public main."
else
    KRONIKA_ANCESTRY_STATUS=$?
    test "$KRONIKA_ANCESTRY_STATUS" -eq 1
fi

test "$(git rev-parse refs/heads/lab/cli-chatgpt-190)" = "$KRONIKA_BASE"
test "$(git rev-list --count refs/heads/lab/cli-chatgpt-190)" = 190
test "$(git rev-parse HEAD:.ap)" = "$KRONIKA_AP"

git show --no-patch --format=fuller main
git log --oneline main
git ls-tree main .ap .gitmodules
git for-each-ref --format='%(refname) %(objectname)' refs/heads/

KRONIKA_STATUS="$(git status --porcelain=v1 --untracked-files=all)"
test -z "$KRONIKA_STATUS"
```

`commit-tree` receives no `-p`, so it creates a new root from the already
reviewed tree. Stop after the readbacks. Do not create `origin`, do not push,
do not run a test suite (the tree is unchanged), and do not delete the lab or
preparation refs.

## Stop conditions

Any nonzero gate; public repository has refs or is unreachable; `main` is not
at `$KRONIKA_BASE` before the update; ancestry check shows lab history as an
ancestor; worktree not clean; AP pin mismatch; a ref would be overwritten or
deleted; need for any file edit; need to leave this recipe; branch/HEAD
mismatch; request to push or add a remote.

Recovery: the lab ref, the preparation branch, and `public/kronika-initial`
all remain. A failed gate leaves them intact. No automatic reset, clean,
branch deletion, or force operation.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/06_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 06, exchange 01). Include the
start/end state, the constructed root SHA and tree, commit metadata, the
parentless and tree-equality proofs, the no-ancestry proof, ref readbacks for
`main`, `lab/cli-chatgpt-190`, `public/kronika-initial`, and
`work/kronika-clean-start`, the privacy manifest result, proof that no remote
exists and no push occurred, and:

```text
Logical-whole closure: not-closed
```

`PASS` means local `main` is the one parentless commit of the accepted cleaned
tree, all readbacks match, the report was saved, and no push occurred. Then
stop. A1 is a later grant.
