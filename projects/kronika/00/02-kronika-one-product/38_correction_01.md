# KRONIKA-ONE-PRODUCT-S6-A35-F01-CORRECTION — renewal (session 38 / exchange 02)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 38
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S6-A35-F01-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — same security-relevant correction as the predecessor grant; only the environment blocker is resolved. The Cooperator may override.
Independence required: no — the separate fresh E3/R3 re-audit follows after the corrected commit.

## Continuity and renewal

Continuity anchor: your own terminal report `38_report_00.md`, SHA-256
`86a0eda29de487ace60c40c8282fde2f4c2d489c829859648307b64686f738e1` (status
BLOCKED; no edits; no commit). That authority expired with the report. This
renewal re-grants the same bounded correction. The predecessor grant
`38_correction_00.md`, SHA-256
`f5c3af564f74a7e8df9c99783e4cadaf841e8d19ccb6788e7a478213df62e199`, remains
the binding requirements document: R1–R10, its validation, git and stop
conditions stay in force, with the two adjustments in this renewal. Where this
renewal and the predecessor differ, this renewal governs.

Blocker resolved: the pinned AP tool could not run on this macOS host because
BSD `/usr/bin/awk` does not implement a NUL record separator (`RS="\0"`), and
the sanitized stage fixes `PATH=/usr/bin:/bin`. Upstream AP `main` now carries
the one-line portable fix (AP commit
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`), and this repository adopted it in
commit `5843486ddeae13ec5b331f102c5cb595bfa6e386` on
`feat/kronika-one-product`. The canonical route is verified on this host:
`project check --baseline 5843486…` PASS, `exec runtime-info` PASS
(exact-source `.venv` provenance), focused tests PASS. No product source file
changed; the S6 candidate under correction remains
`38e7beeb3921d7c0fd8e717e480754fbd18130c9`.

## Updated starting state (verify independently before any edit; fail closed)

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     5843486ddeae13ec5b331f102c5cb595bfa6e386
parent   38e7beeb3921d7c0fd8e717e480754fbd18130c9
tree     863c0411f4be0e3d2389890aa8952862399ee51a
subject  chore: adopt AP pin 73e20ef80b88700d5fcbc397cd8edd4fc425869f
status   empty (git status --porcelain --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
main     40e51cb2d061ead96850c9c94aa59de54d5e1310
origin/main 40e51cb2d061ead96850c9c94aa59de54d5e1310
```

Baseline for every declared AP command in this exchange:
`5843486ddeae13ec5b331f102c5cb595bfa6e386` (replaces the predecessor's
`40e51cb2…`). The previously failing `project check` must now exit 0 before any
edit — that is the first proof that exchange 01's blocker is resolved.

Report destination: `38_report_01.md` (absent at issuance). `38_report_00.md`
is your predecessor's terminal report; never write to it.

## Allowlist adjustment (binding)

One path in the predecessor grant's additional-production list —
`src/framenest/application/ports/media_cover_repository.py` — is NOT part of
the whole's effective S6 allowlist (the 176-path union of `33_report_00.md`
section 6 plus `tests/support/youtube_fake_demo.py` and
`tests/contract/test_youtube_fake_demo.py`). Do not edit it. If the correction
genuinely requires a change to that port, stop and report the exact need; do
not expand any allowlist yourself. Every other predecessor allowlist path
remains authorized unchanged.

## Required behavior, validation and git

R1–R10 of the predecessor grant apply unchanged, including: decision-based
reads; R2 detail; R3 metadata; R4 gallery membership and member filters without
a publication row; R5 content/download `404` for non-approved locations; R6
approved cover digest only; R7 analysis/suggestions including the acceptance
LEAD reproduction; R8 gallery preview; R9 no weakening and no expansion; R10
the required regression in `tests/contract/test_kronika_approved_projection.py`
(Red first on the unfixed candidate, then Green).

Validation: targeted only; no full suite; no rerun of an unchanged gate. Use
the same declared route and the same targeted set as the predecessor grant,
with `--baseline 5843486ddeae13ec5b331f102c5cb595bfa6e386` substituted in every
command. The four parked pre-existing failures stay unrepaired and un-run.

Git: exactly one local commit with the predecessor subject
`fix(kronika): serve approved projections on household reads`; stage by
explicit allowlisted path list; `git diff --cached --check` exit 0; report SHA,
parent (`5843486ddeae13ec5b331f102c5cb595bfa6e386`), tree, subject and changed
paths; post-commit status empty; no push, fetch, tag, merge, rebase, reset,
restore, checkout, switch, stash, clean or config write.

Stops, evidence envelope and no-self-audit rules: as issued in the predecessor
grant.

## Completion and report contract

`PASS` means: the regression scenario fails first and passes after the fix; the
targeted set exits 0; R2–R8 behavior holds within the effective allowlist; and
one local commit exists with a clean post-commit worktree and no push. Use
`Phase-qualified result: implementation-PASS` only for that result; otherwise
`not-applicable` and a truthful `PARTIAL`/`BLOCKED`. `Logical-whole closure:
not-closed`. `Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
renewal's coordinates (session 38, exchange 02) exactly once. Include: the
re-gate values with the new HEAD and pin; the Red/Green regression evidence; the
exact commands and exit statuses; the changed-path list; the commit
SHA/parent/tree/subject and post-commit status; the R2–R8 implementation
summary including any surface not dynamically exercised; the R7 LEAD check
result; deviations, risks and missing evidence; one smallest next step (the
fresh independent E3/R3 re-audit of the corrected exact SHA); the compact
critique block; and the authority-expiry statement. Classify any pre-existing
failure you encounter; do not repair it.

Finalize the report, save it at the exact destination below only if absent, read
it back in full, verify its first line, coordinates, content and path, then send
the separate short completion notice in Slovak (masculine address) with status,
path and SHA-256. Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 38_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 38_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
