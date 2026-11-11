# Publication — Jelena foundation baseline candidate

Persistent role identity: WORKER
Logical whole identity: jelena-foundation-and-blender-connection
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Publication Worker
Phase: publication
Task identity: JELENA-FOUNDATION-PUBLISH-003
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — bounded deterministic non-force push and direct public readback; no design ambiguity.
Recommended context capacity: approximately 250k tokens (recommendation, not observed capacity)
Requested model: Grok 4.7 High, or the Cooperator-selected Cursor model. Report the observed model if exposed, otherwise unknown.
Independence required: no

## Publication record

Publication authority: explicit
Exact publication candidate: `cf73239f3142fc1b3b05ea6743b8b3e6ccb60c47`
Candidate parent: `989da45c055a99971c8a7fa897e07bf7f23da2c1`
Candidate tree: `5f20b1cac7f9fecced4ca8a1774a9e26855e0d40`
Candidate subject: `evidence: retain foundation baseline render`
Expected public pre-state: `989da45c055a99971c8a7fa897e07bf7f23da2c1` on `refs/heads/main`
Publication target: `https://github.com/cisarik/jelena.git` `refs/heads/main`
Publication operation: one normal non-force `git push origin HEAD:main`
Publication completion evidence: direct `git ls-remote` readback equals the candidate

## Goal

Independently verify and publish the exact accepted baseline candidate `cf73239f3142fc1b3b05ea6743b8b3e6ccb60c47` to `cisarik/jelena` `main` with one normal non-force push, then prove direct public equality.

This is one bounded publication. It creates no new commit and changes no file.

## Context

The baseline candidate was produced by `05_report_00.md`, SHA-256 `3fea5b99a5a2d19572ed0a3fbb737a26508fa320729bc4fa7cfb543e9a1a711a`, status `PASS`, with `implementation-PASS`.

The Orchestrator inspected the actual PNG and manifest and accepted the baseline as proportionate E1 additive evidence. The Cooperator's visual checklist returned PASS for the correct camera-A view, readable materials and framing, and suitability as a comparison baseline.

The candidate adds only:

- `README.md` update;
- `evidence/foundation-001/camera-a.png`;
- `evidence/foundation-001/manifest.json`.

The previous foundation commit `989da45` is already public. This publication adds the baseline evidence on top of it.

## Repository gate

Repository identity: https://github.com/cisarik/jelena (origin https://github.com/cisarik/jelena)
Working directory: /Users/agile/Projects/jelena
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: `cf73239f3142fc1b3b05ea6743b8b3e6ccb60c47`
Expected parent: `989da45c055a99971c8a7fa897e07bf7f23da2c1`
Expected tree: `5f20b1cac7f9fecced4ca8a1774a9e26855e0d40`
Expected index/worktree: clean
Expected public pre-state: `989da45c055a99971c8a7fa897e07bf7f23da2c1`

Before mutation, verify:

```fish
git status --porcelain=v1 -b
git rev-parse HEAD
git rev-parse HEAD^
git rev-parse HEAD^{tree}
git show --stat --oneline HEAD
git submodule status
git -C .ap rev-parse HEAD
git -C .ap status --porcelain=v1
./.ap/ap doctor
git ls-remote origin refs/heads/main
shasum -a 256 evidence/foundation-001/camera-a.png evidence/foundation-001/manifest.json
```

Interpretation:

- If local HEAD, parent, tree, branch or cleanliness differ, stop and report.
- If `.ap` is not clean at `d7023cf037f6d17885c3ede5c04812c61640da50` or `ap doctor` is not PASS, stop and report.
- If the PNG or manifest hash differs from the report (`PNG` `db1386a24a00765c976eb8c216f1936f91ccbeb6eb4c8b9bb7da5b7b24a5cd8f`), stop and report.
- If public `refs/heads/main` equals the candidate already, do not push; report that publication appears already complete and request reconciliation.
- If public `refs/heads/main` is not the expected parent and is not the candidate, stop and report divergence. Do not force or reconcile.

## Publication sequence

Only after all preconditions pass:

```fish
git push origin HEAD:main
```

This must be a normal fast-forward push of the accepted candidate. Do not use `--force`, `--force-with-lease`, `+`, a different refspec, tags, or any additional remote operation.

Immediately after the push, perform direct public readback:

```fish
git ls-remote origin refs/heads/main
git rev-parse HEAD
git status --porcelain=v1 -b
```

The direct `ls-remote` result must equal:

```text
cf73239f3142fc1b3b05ea6743b8b3e6ccb60c47	refs/heads/main
```

If the push is rejected, non-fast-forward, authentication fails, or the public ref does not equal the candidate, stop and report. Do not force, retry with different credentials, create a commit, or reconcile automatically.

## Negative authority

Do not edit, stage, commit, amend, rebase, tag, delete, force, fetch, pull, open Blender, use MCP, change Cursor configuration, install anything, access secrets, modify AP or Meta, or perform any operation other than the single push and read-only checks above.

Repository mutation: none
Host/remote mutation: one normal non-force push to `https://github.com/cisarik/jelena.git` `refs/heads/main`
Trace persistence: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 06_publication_00.md
Destination path: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Report filename: 06_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Trace project key: jelena
Trace logical-whole projection identity: jelena-foundation-and-blender-connection
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

## Mandatory reading

- Governing WORKER spine: AP.md Semantic Authority; Per-Role Minimum-Reading Spine (WORKER row); RF-03, RF-05, RF-06, RF-12, RF-13, RF-18; §8; §18.
- AP.md `Publication PASS` meaning; Git and Remote Safety; Validation and Public Verification.
- AP_WORKER.md Reporting.
- PROMPT_CONTRACTS.md Worker Report Header; Phase Result and Closure Record.
- The baseline report `05_report_00.md` and manifest.

## Report contract

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo these coordinates once: logical whole identity `jelena-foundation-and-blender-connection`; Worker session `06`; Worker exchange `01`.

Include:

- Status: PASS, PARTIAL or BLOCKED.
- Exact candidate commit, parent, tree and subject.
- Pre-push public ref and local HEAD.
- Exact push command and result.
- Post-push direct `git ls-remote` output.
- Local HEAD, branch and cleanliness after publication.
- PNG and manifest hashes observed before push.
- Confirmation that no file, AP, Blender, MCP, Cursor, Meta or additional Git mutation occurred.
- Any divergence, authentication failure or residual risk.
- Orchestration critique: MEASURED findings and LEAD possibilities; either may be none.
- Phase-qualified result: publication-PASS | not-applicable
- Logical-whole closure: not-closed
- Report justification: new-mutation

PASS means the accepted candidate is the public `refs/heads/main` and direct readback matches. Publication PASS is not whole closure. Do not claim acceptance, deployment or closure.

Authority expires at the terminal report, cancellation or supersession.
