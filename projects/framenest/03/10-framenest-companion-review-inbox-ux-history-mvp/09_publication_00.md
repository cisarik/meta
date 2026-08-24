# AUTHORITATIVE PROMPT FOR FRESH WORKER 09

## FrameNest companion review-inbox UX/history — publish candidate to public main

You are a Worker assigned to WORKER. Read this whole prompt before acting.

The Orchestrator accepted implementation through Settings Save
(`0eeaf350801e181025b271676d8f2fbb487db3d8`). Public `main` is still
`6e20fc12f145286e474294b79cbd120df6e38e56`. Home wrappers
(`nuc_update.fish`, `framenest_routine.fish`) deploy only a SHA that equals
public `refs/heads/main`. This session **publishes** that SHA. It does **not**
deploy, migrate, enable automatic analysis, or close the logical whole.

Do not enter Native Plan Mode. Do not use Max. Medium is enough; Extra High is
allowed if it is the only high-reasoning SKU offered. If Native Plan Mode is
on, stop `BLOCKED`.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-save-category-mvp
  framenest-x-save-overlay-edit-subset-mvp
  framenest-companion-ai-review-inbox-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: FN-COMPANION-REVIEW-INBOX-UX-PUB-09
Task type: bounded publication
Native planning mode: not-used
Reasoning recommendation: medium
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Prior implementation report: Worker 08 / exchange 01 implementation-PASS at
  0eeaf350801e181025b271676d8f2fbb487db3d8
Continuity anchor: none — do not resume Worker 08
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: production-external-service-credential-or-account-boundary
Routing reopened for: production-external-service-credential-or-account-boundary
Unchanged axes reopened: none
Ordinary-only trigger: no
Automatic model selection: off
Enhanced/maximum mode: not requested
```

```text
Publication authority: explicit
Implementation authority: none
Deployment authority: none
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact published object: 0eeaf350801e181025b271676d8f2fbb487db3d8
Independence required: no
```

```text
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of the accepted
  unpublished candidate onto public FrameNest main; no production host
Authorized implementation stages: one push, then credential-free ls-remote
Combined implementation envelope: prohibited
Independent acceptance: not-required (this session)
Rollback or recovery checkpoint: ordinary Git revert of public main later; no force-push
Activated annex: publication
Terminal publication report point: after public main equals the candidate SHA
```

Repository documentation, commit subjects, and the terminal Worker report must
use professional English. Czech is forbidden. The terminal report must begin
exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Publication PASS is not deployment, UX acceptance, or closure.
`Logical-whole closure: not-closed`.

Protocol-variant selection:

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

---

## 1. External trace and Meta write boundary

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/10-framenest-companion-review-inbox-ux-history-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Downloadable prompt filename: 09_publication_00.md
Destination path: projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/09_publication_00.md
Archival: wait-for-report
```

You may **read** (historical):

```text
/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/08_report_00.md
```

You may **write** only:

```text
/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/09_report_00.md
```

Do not alter any other Meta path. Do not stage or commit Meta.

---

## 2. Frozen published object

```text
Repository: https://github.com/cisarik/framenest.git
Working directory: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Accepted commit: 0eeaf350801e181025b271676d8f2fbb487db3d8
Accepted tree: be9d83da50f9d44356f65f2a632d5f2ff20b9422
Accepted subject: fix: use Save under companion origin settings
Required AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Expected public ref before publication: refs/heads/main = 6e20fc12f145286e474294b79cbd120df6e38e56
Expected public ref after publication: refs/heads/main = 0eeaf350801e181025b271676d8f2fbb487db3d8
Push mode: one ordinary non-force fast-forward push of the exact accepted commit to origin refs/heads/main
```

Public `main` `6e20fc12` is an ancestor of `0eeaf350`. The fast-forward contains
**7** commits (unread/history chrome, stale-context guard, merged history,
X seed, preserving Apply, ADR-0073 living docs, Settings Save). Do not create
a merge, squash, rebase, or any new Git object. Do not check out local `main`.
Publish by SHA.

Local `main` may be stale. Ignore it.

---

## 3. Read-only preflight (stop `BLOCKED` on mismatch)

From `/home/agile/Projects/framenest`, no fetch that rewrites:

1. `origin` fetch/push URL is `https://github.com/cisarik/framenest.git`.
2. Credential-free:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

   must equal `6e20fc12f145286e474294b79cbd120df6e38e56`. If it differs, do
   not push and do not invent a merge.
3. Local `HEAD` is exactly `0eeaf350801e181025b271676d8f2fbb487db3d8`.
   Tree `be9d83da50f9d44356f65f2a632d5f2ff20b9422`. Tracked tree clean.
   No active Git operation. Untracked owner paths may exist; do not delete them.
4. `.ap` gitlink equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
5. `git merge-base --is-ancestor 6e20fc12f145286e474294b79cbd120df6e38e56 0eeaf350801e181025b271676d8f2fbb487db3d8` succeeds.
6. `git rev-list --count 6e20fc12f145286e474294b79cbd120df6e38e56..0eeaf350801e181025b271676d8f2fbb487db3d8` equals **7**.

Do not run product test suites. Do not use `uv`, `pip`, or `poetry install`.
Do not SSH. Do not invoke `framenest-release`.

---

## 4. Push and public readback

One non-force push:

```text
git push origin 0eeaf350801e181025b271676d8f2fbb487db3d8:refs/heads/main
```

Then credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
must equal `0eeaf350801e181025b271676d8f2fbb487db3d8`.

If the push is rejected or is not a fast-forward, stop `BLOCKED`. No
`--force`. No tags. No PR.

---

## 5. Negative authority

- Native Plan Mode, Max, sub-agents
- NUC, sudo, `framenest-release`, migrate, `/etc/framenest/framenest.env`
- Enabling `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`
- Source edits, new commits, rebase, reset, stash, clean
- Force-push
- Closure, UX, INFOSEC R3
- Generating an Orchestrator restoration prompt
- Editing `~/nuc_update.fish` or `~/framenest_routine.fish`

---

## 6. Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

```text
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
```

Include: PASS | PARTIAL | BLOCKED; `publication-PASS` or not; before/after
ls-remote SHAs; push command used (no `--force`); AP pin; next step =
Cooperator may run the usual NUC routine against public main
`0eeaf350801e181025b271676d8f2fbb487db3d8`. Same-schema deploy will stop at
`migration-required` because NUC catalog is `0031` and this SHA packages
`0032`. That migrate is a later exact grant, not this session.
Report justification: `changed-external-state`.
`Logical-whole closure: not-closed`.

Write only the Meta path in Section 1.

Planning-mode note: native Plan Mode must be OFF. If it cannot be disabled,
STOP without mutating and report BLOCKED.
