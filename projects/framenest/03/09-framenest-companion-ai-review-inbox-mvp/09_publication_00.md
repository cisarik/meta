# Authoritative Prompt for Fresh Worker 09

## FrameNest Companion AI Review Inbox — publish candidate to public main

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

The COOPERATOR accepted living docs and now needs this SHA on the Ubuntu NUC
so he can test the review inbox. ADR-0060 will deploy only a SHA whose public
`refs/heads/main` equals it. This session publishes that SHA. It does **not**
deploy, migrate, enable automatic analysis, or close the logical whole.

Do not enter Native Plan Mode. Do not use Max. Medium is enough; if Extra High
is the only offered high-reasoning SKU, you may use it. If Native Plan Mode is
on, stop `BLOCKED`.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-save-category-mvp
  framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: FN-COMPANION-AI-REVIEW-INBOX-PUB-09
Task type: bounded publication
Native planning mode: not-used
Reasoning recommendation: medium
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Prior implementation report: Worker 07 / exchange 01 implementation-PASS at 6e20fc12; living-docs Cooperator PASS 2026-08-23
Continuity anchor: none — do not resume Worker 07
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
Exact published object: 6e20fc12f145286e474294b79cbd120df6e38e56
Independence required: no
```

```text
Evidence tier: E2
Evidence tier basis: reviewable non-force fast-forward of the accepted unpublished candidate onto public FrameNest main; no production host
Authorized implementation stages: one push, then credential-free ls-remote
Combined implementation envelope: prohibited
Independent acceptance: not-required (this session)
Rollback or recovery checkpoint: ordinary Git revert of public main later; no force-push
Activated annex: publication
Terminal publication report point: after public main equals the candidate SHA
```

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh publication session
```

Internal delegation, sub-agents, parallel Workers, Explore tasks, and hidden
secondary workstreams are not authorized.

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
Trace discovery: cisarik/meta repository path projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/09-framenest-companion-ai-review-inbox-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Downloadable prompt filename: 09_publication_00.md
Destination path: projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/09_publication_00.md
Archival: wait-for-report
```

You may **read** (historical):

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/07_report_00.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/08_cooperator_acceptance_00.md
```

You may **write** only:

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/09_report_00.md
```

Do not alter any other Meta path. Do not stage or commit Meta.

---

## 2. Frozen published object

```text
Repository: https://github.com/cisarik/framenest.git
Working directory: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Accepted commit: 6e20fc12f145286e474294b79cbd120df6e38e56
Accepted tree: 950d6eeb0a78ad7f2b143ead724e01ccc0bc6788
Accepted subject: docs: record companion review inbox in living product status
Required AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Expected public ref before publication: refs/heads/main = 045f33b44897a6f3949cc515792336396f1d33a1
Expected public ref after publication: refs/heads/main = 6e20fc12f145286e474294b79cbd120df6e38e56
Push mode: one ordinary non-force fast-forward push of the exact accepted commit to origin refs/heads/main
```

Public `main` `045f33b4` is an ancestor of `6e20fc12`. The fast-forward contains
**29** commits (X Save overlay, schema `0030`/`0031`, companion review inbox,
living docs). Do not create a merge, squash, rebase, or any new Git object.
Do not check out local `main`. Publish by SHA.

Local `main` may be stale. Ignore it.

---

## 3. Read-only preflight (stop `BLOCKED` on mismatch)

From `/home/agile/Projects/framenest`, no fetch that rewrites:

1. `origin` fetch/push URL is `https://github.com/cisarik/framenest.git`.
2. Credential-free:

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

   must equal `045f33b44897a6f3949cc515792336396f1d33a1`. If it differs, do
   not push and do not invent a merge.
3. Local `HEAD` is exactly `6e20fc12f145286e474294b79cbd120df6e38e56`.
   Tree `950d6eeb0a78ad7f2b143ead724e01ccc0bc6788`. Tracked tree clean.
   No active Git operation. Untracked owner paths may exist; do not delete them.
4. `.ap` gitlink equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
5. `git merge-base --is-ancestor 045f33b44897a6f3949cc515792336396f1d33a1 6e20fc12f145286e474294b79cbd120df6e38e56` succeeds.
6. `git rev-list --count 045f33b44897a6f3949cc515792336396f1d33a1..6e20fc12f145286e474294b79cbd120df6e38e56` equals **29**.

Do not run tests. Do not use `uv`, `pip`, or `poetry install`. Do not SSH.

---

## 4. Push and public readback

One non-force push:

```text
git push origin 6e20fc12f145286e474294b79cbd120df6e38e56:refs/heads/main
```

Then credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
must equal `6e20fc12f145286e474294b79cbd120df6e38e56`.

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

---

## 6. Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

```text
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
```

Include: PASS | PARTIAL | BLOCKED; `publication-PASS` or not; before/after
ls-remote SHAs; push command used (no `--force`); AP pin; next step =
Orchestrator issues Worker 10 deploy after Cooperator `sudo -v` on the NUC.
Report justification: `changed-external-state`.
`Logical-whole closure: not-closed`.

Write only the Meta path in Section 1.

---

## 7. Stop

After the terminal report, stop. Do not deploy.
