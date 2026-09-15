# Fresh Publication Worker — FrameNest web-client contract and testability convergence

## AP coordinates

```text
Logical whole identity: framenest-web-client-contract-and-testability-convergence
Worker role: WORKER
Worker profile: Fresh Publication Worker
Worker session target: fresh-worker-session
Worker session ordinal: 05
Worker exchange ordinal: 00
Native planning mode: not-required
Reasoning expectation: High

Publication authority: granted, strictly bounded by this prompt
Implementation authority: NOT granted
Source mutation authority: NOT granted
New commit authority: NOT granted
Force-push authority: NOT granted
Deployment authority: NOT granted
Meta mutation authority: NOT granted
```

You are a genuinely fresh Publication Worker.

The candidate has already passed independent acceptance.

Your sole job is to publish the **exact accepted FrameNest candidate** to the canonical public `main` branch without changing its tree, commit identity, history, AP pin, or source.

Do not implement anything.

Do not amend, rebase, merge, squash, cherry-pick, regenerate, format, or otherwise transform the accepted candidate.

Publication must preserve exact commit identity.

---

# 1. Exact accepted candidate

Accepted FrameNest commit:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Expected accepted commit chain:

```text
0f4500ad7463d7428f377097aea224a268b321e2
Rebaseline FrameNest AP integration pin

6371bc00cb686c80e735330b308494ba552b94bc
Align metadata client-server validation contracts

1f355a8433331beef3410bf807b247a5b8155919
Replace metadata source assertions with behavior tests

fe5e38b8bfb986e68a9714d709267e3d19be1575
Retire test-only frontend artifacts

33946e08447dc92621ed6844b4b5d13a19ec29f1
Remove unreachable legacy library browser client
```

Logical-whole baseline:

```text
8c7858b62beca3c4ee92bb8f1f095b98063e2c94
```

Expected AP gitlink:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

Expected repository:

```text
/home/agile/Projects/framenest
```

Canonical origin:

```text
https://github.com/cisarik/framenest.git
```

These coordinates are orientation only.

Verify them independently before publication.

---

# 2. Accepted evidence

Read the governing repository `AGENTS.md` and pinned AP documents.

Read the complete logical-whole Meta trace:

```text
/home/agile/meta/projects/framenest/11/01/
```

At minimum:

```text
01_planning_00.md
01_report_00.md

02_implementation_00.md
02_report_00.md

03_implementation_00.md
03_report_00.md

04_acceptance_00.md
04_report_00.md

05_publication_00.md
```

Do not modify Meta.

The accepted Acceptance Worker verdict is:

```text
acceptance-PASS
```

for exact candidate:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Do not reinterpret or extend the accepted implementation scope.

---

# 3. Expected public state before publication

The fresh Acceptance Worker independently observed:

```text
origin/feat/x-meme-browser-companion
= 33946e08447dc92621ed6844b4b5d13a19ec29f1

origin/main
= a4193d4f520a30aafa333987f2e6b846a5425d27
```

Therefore the exact accepted candidate is already publicly reachable through the feature branch, while canonical `main` is behind.

These values MUST be independently refreshed.

Do not rely on stale remote-tracking refs.

Use direct canonical public evidence such as:

```text
git ls-remote origin refs/heads/main refs/heads/feat/x-meme-browser-companion
```

or AP-governed equivalent.

---

# 4. Pre-publication gates

Before any push, independently verify all of the following.

## Repository identity

```text
git rev-parse --show-toplevel
git remote get-url origin
```

Required repository root:

```text
/home/agile/Projects/framenest
```

Required canonical origin identity:

```text
github.com/cisarik/framenest
```

---

## Candidate identity

Verify:

```text
git rev-parse HEAD
```

is exactly:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Verify:

```text
git status --short
```

is empty.

Verify exact `.ap` gitlink:

```text
git rev-parse HEAD:.ap
```

equals:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

and:

```text
git -C .ap rev-parse HEAD
```

matches it.

Run:

```text
./.ap/ap doctor
```

Required:

```text
PASS
```

---

## Accepted commit identity

Verify candidate history contains the accepted chain.

At minimum:

```text
git log --format='%H %P %s' -6
```

and appropriate ancestry checks.

Do not create a new publication commit.

Publication target must remain:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

---

# 5. Public ancestry safety gate

Refresh direct public state immediately before the push.

Determine exact current:

```text
refs/heads/main
refs/heads/feat/x-meme-browser-companion
```

Required conditions:

1. Public feature branch must still identify the accepted candidate, or any difference must be fully explained and must not invalidate candidate identity.
2. Current public `main` must be an ancestor of accepted candidate `33946e08447d...`.
3. Publishing the candidate to `main` must therefore be a normal fast-forward.
4. No force push may be needed.
5. There must be no unknown public-main commit requiring integration.

Explicitly verify the current public-main SHA is an ancestor of the candidate.

If `main` moved to a commit not contained in the accepted candidate:

```text
STOP
publication-BLOCKED
```

Do not merge or rebase.

Such integration requires a new candidate and renewed acceptance.

---

# 6. Publication operation

Only after every pre-publication gate passes, perform exactly one ordinary non-force publication of the accepted commit to canonical `main`.

Preferred identity-explicit form:

```text
git push origin \
  33946e08447dc92621ed6844b4b5d13a19ec29f1:refs/heads/main
```

Equivalent AP-governed ordinary push is acceptable if it preserves the exact source and destination identities.

Forbidden:

```text
--force
--force-with-lease
merge commits
rebases
amends
cherry-picks
new source commits
tag mutation
deployment
```

Capture the exact push command and exit status.

Required:

```text
exit 0
```

One successful ordinary push is enough.

Do not repeatedly mutate the remote.

---

# 7. Independent public readback

After the push, independently query canonical public state again.

Required exact result:

```text
refs/heads/main
= 33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Also verify the accepted candidate remains publicly available.

Use direct public evidence, not merely:

```text
origin/main
```

from a preexisting local remote-tracking ref.

Compare:

```text
accepted candidate
local HEAD
public main
```

All must equal:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

---

# 8. Post-publication repository integrity

After publication verify:

```text
git rev-parse HEAD
git status --short
git rev-parse HEAD:.ap
git -C .ap rev-parse HEAD
./.ap/ap doctor
```

Required:

```text
HEAD unchanged at 33946e08447d...
worktree/index clean
AP unchanged at 7478ddb...
ap doctor PASS
```

Publication itself must not mutate the accepted local tree.

---

# 9. No deployment

This task does NOT authorize:

```text
NUC refresh
systemd changes
database migration execution
service restart
media operations
VPS operations
Tailscale changes
deployment testing
```

Do not touch the NUC.

Do not run deployment scripts.

The Cooperator deliberately wants additional engineering work before final UI/UX polish and NUC testing.

---

# 10. Known residuals are not publication blockers

Independent acceptance classified the following as non-blocking residuals:

```text
R1 catalog-card-preview cluster
R2 metadataDurableAnalysis.result
R3 previewObjectUrls / revokePreviewObjectUrls
R4 legacy .library-* CSS
```

Do not modify them.

Do not reopen acceptance.

Publication means publishing the exact already-accepted candidate, not polishing residuals.

R1 may become a subsequent bounded logical whole.

---

# 11. Stop conditions

Return `publication-BLOCKED` without any push if:

```text
local HEAD != accepted candidate
worktree/index is dirty
.ap gitlink/check-out mismatch exists
ap doctor fails materially
canonical origin identity is wrong
public main moved outside accepted candidate ancestry
feature/public evidence contradicts candidate identity
ordinary fast-forward publication is impossible
publication would require force
publication would require merge/rebase/cherry-pick/new commit
```

Do not repair these conditions under publication authority.

Report exact evidence.

---

# 12. Terminal report

Return a complete report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

No preamble before this heading.

The Cooperator will archive the complete response as:

```text
05_report_00.md
```

Include:

```text
Logical whole identity
Worker session ordinal
Worker exchange ordinal
Worker session target
Native planning mode
Standard terminal status
Phase-qualified result
Accepted candidate
Published public commit
Logical-whole closure
Report justification
Authority expiry
```

Then include these sections.

## Verified pre-publication state

Report exact:

```text
repository root
branch
HEAD
worktree/index
origin identity
.ap gitlink
.ap checkout
ap doctor
public main before
public feature branch before
```

## Ancestry/publication safety

Provide exact evidence proving:

```text
public main before ⊆ accepted candidate history
```

and that publication is a normal non-force fast-forward.

## Publication operation

Provide:

```text
exact push command
exit status
remote response summary
```

Explicitly state whether exactly one mutation push was performed.

## Independent public readback

Report direct post-push public values for:

```text
refs/heads/main
refs/heads/feat/x-meme-browser-companion
```

and show equality with the accepted candidate.

## Post-publication integrity

Report:

```text
local HEAD
git status --short
.ap gitlink
.ap HEAD
ap doctor
```

## Non-actions

State explicitly:

```text
no source implementation performed
no new commit created
no rebase/merge/amend performed
no force push performed
Meta was not mutated
no deployment performed
NUC was not touched
```

## Publication verdict

End with exactly one:

```text
publication-PASS
publication-BLOCKED
```

For `publication-PASS`, required meaning is:

```text
canonical public main equals exact accepted candidate
```

The logical whole remains:

```text
not-closed
```

until ORCHESTRATOR_CHAT performs final closure/reconciliation after receiving this publication report.

All Publication Worker authority expires at the terminal report.