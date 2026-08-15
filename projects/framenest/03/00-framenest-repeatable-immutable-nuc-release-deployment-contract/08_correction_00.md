# FrameNest bounded correction: first-cutover status of a pre-manifest NUC tree
You are one fresh WORKER instance assigned to WORKER. You are not the
ORCHESTRATOR and not Worker 07. Do not deploy, SSH to the NUC, write host
markers, publish, or close the logical whole.
If this chat performed Worker 07 deployment, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: FN-NUC-RELEASE-CORRECT-08-F01
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Recommended reasoning: Medium
Recommendation basis: named helper compatibility defect with a reproduced missing-manifest status failure; no live host mutation
Automatic model selection: off
Sub-agents/internal delegation: not-used
Worker topology: single-active
Material phase gate: yes
Changed material axis: mutation-authority-or-side-effect-class
Ordinary-only trigger: no
Routing reopened for: mutation-authority-or-side-effect-class
Unchanged axes reopened: none
Evidence tier: E1
Combined implementation envelope: allowed
Independent acceptance: not-required
Activated stricter profile: none
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Accepted findings (Orchestrator-confirmed)
Finding ID: FN-NUC-RELEASE-DEPLOY-07-F01 Affected commit: 011823a9dcb3d2a51e684fefd5083970f3610701 Location: read_current_release / cmd_remote_read_manifest Defect: status, check, and deploy all sudo -n cat .framenest-release-manifest.json. Worker 07 reproduced EXIT_TRANSPORT 20 on the live tree 148b6c2012809944262399c1a166e85082606fbf, which has .framenest-release-sha and no manifest. That blocks the mandated status-before-deploy sequence. Do not write a synthetic manifest onto the immutable host release.

Finding ID: FN-NUC-RELEASE-DEPLOY-07-F02 (authorized adjacent) Location: verify_clean_worktrees Defect: git status --porcelain treats owner ?? paths as dirty. This operator checkout must preserve those untracked paths; git archive does not include them. check/deploy would fail next.

Audit authority: none. Do not self-certify independent acceptance. Do not deploy.

Implementation authority record
Exact baseline: 011823a9dcb3d2a51e684fefd5083970f3610701 Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Changed-path allowlist:

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_source_contract.py
docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
Public CLI unchanged. No NUC/SSH. No second extract-argv change. No parked sanitizer/--yes residuals.

Required behavior:

If the current release manifest is absent and .framenest-release-sha is a full lowercase 40-hex SHA, read_current_release succeeds using that SHA only. Do not invent ap_gitlink or archive hashes. status must print active_release from that SHA and a sanitized indication that the manifest is absent. check/deploy may use current_path for backup/rollback without a manifest.
If both markers are absent, or the SHA is invalid, fail closed with a distinct sanitized error (not opaque command failed if you can name the missing marker).
New ADR-0060 releases still write both markers. Do not weaken archive validation or private _remote _remote-extract.
verify_clean_worktrees must ignore untracked (--untracked-files=no or equivalent). Tracked dirty still fails EXIT_SOURCE_GATE.
ADR-0060: one short clause that a pre-manifest production tree is observed via .framenest-release-sha only; synthesizing a manifest on an old immutable tree is forbidden. Keep Status Accepted.
Regression tests (fail on unmodified 011823a9…, pass after):

FakeRunner status when manifest cat/test -e is missing and SHA file returns a valid 40-hex → exit 0, active_release printed, no invented hashes.
Same setup: check still reaches backup-readiness using current_path (manifest not required).
Missing SHA and missing manifest → non-zero.
verify_clean_worktrees accepts ?? owner-untracked and still rejects M AGENTS.md.
Re-audit routing: Orchestrator will issue a separate fresh Worker full-fresh re-acceptance of the new commit, then republication, then deploy. This Worker does none of those.

Commits: exactly one ordinary non-force commit. No push.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 08_correction_00.md + 08_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Direct Worker-to-Cooperator language: not-used Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest Expected HEAD before commit: 011823a9dcb3d2a51e684fefd5083970f3610701 Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Preserve untracked owner paths. Do not use uv/pip/poetry install.

Mandatory reading
AGENTS.md, WORKER_EXECUTION_CONTRACT.md, .ap/AP.md, .ap/AP_WORKER.md
read_current_release, _cmd_status, _cmd_check, verify_clean_worktrees, cmd_remote_read_release_sha
Worker 07 report as the finding claim only
Mandatory re-gate
Stop unless HEAD is 011823a9…, tracked clean, no active Git op, .ap pin matches, Python 3.13.x under sanitized env. Reproduce F01 on unmodified code (status path requires manifest) before editing.

Validation
Sanitize env. No pipe of gates.

New regression nodes fail on unmodified 011823a9… and pass after the edit. Record both.
Then once:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
Do not run the full suite. Do not SSH/NUC.

Git authority
If validation exits 0 and the diff is only the allowlist: one ordinary commit, parent 011823a9…, no amend/force/rebase/push. Message why: first routine update must status/check a pre-manifest production tree without forging host markers.

Negative authority
No NUC/SSH/sudo; no host marker write; no deploy; no Meta; no publication; no closure; no AP pin change; no extra docs outside the allowlist.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 08, exchange 01. Include: PASS | PARTIAL | BLOCKED; implementation-PASS | implementation-PARTIAL | not-applicable; start 011823a9…; end SHA; changed files; pre-fix vs post-fix evidence for F01 and F02; focused pytest; Git SHA/parent/no push; independent acceptance not claimed; next step = fresh re-acceptance of the new commit; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS only if one allowlist commit exists, regressions fail-then-pass, and the three focused files exit 0. Do not claim acceptance-PASS, publication, or deployment.

Authority expires at the terminal report.