# FrameNest independent acceptance of immutable NUC release engine
You are one fresh WORKER instance under Analytic Programming.
You did not implement this candidate. You are not the ORCHESTRATOR. This grant
is sequential independent acceptance only. Do not correct, edit, commit, push,
publish, deploy, close the logical whole, mutate Meta or AP, or start a second
audit.
If this chat already implemented, repaired, or previously reviewed commit
2d995bb98a8b2c96fa1925f06403b3ee156c6237, stop and report BLOCKED. Do not
pretend a reused session is fresh.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: FN-NUC-RELEASE-ACCEPT-03
Native planning mode: not-used
Implementation authority: none
Independence required: yes
Acceptance independence: required-fresh-independent
Recommended reasoning: High
Recommendation basis: named risk is security-sensitive remote deployment, archive extraction, sudo/systemd cutover, backup/schema fail-closed behavior, and rollback correctness
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Material phase gate: yes
Changed material axis: independence-requirement
Ordinary-only trigger: no
Routing reopened for: independence-requirement
Unchanged axes reopened: none
Evidence tier: E2
Evidence tier basis: source-and-test acceptance of a security-sensitive engine; no live host mutation in this exchange; live NUC remains a later E3 gate
Combined implementation envelope: prohibited
Independent acceptance: this exchange
Activated stricter profile: none
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
Acceptance record
Acceptance candidate: 2d995bb98a8b2c96fa1925f06403b3ee156c6237 Acceptance parent: 4b04b86e4ea52c673c41624e3f2abe1e59d45907 Acceptance owner map:

ADR-0060 is the durable architecture owner for the routine immutable NUC update contract
AGENTS.md NUC Routine Release Update block is the always-read operator invariant
docs/UBUNTU_NUC_DEPLOYMENT.md is the runbook owner
deploy/ubuntu/README.md is the deploy-support map
SERVER.md / README.md / PRODUCT.md / ROADMAP.md may only reconcile living status; they must not hide new product scope
tests/contract/test_nuc_release_*.py are the focused harness, not a second architecture owner
deploy/ubuntu/framenest-release and deploy/ubuntu/framenest_release.py are the implementation of ADR-0060
Acceptance allowlist (exact candidate paths; no others):

AGENTS.md
PRODUCT.md
README.md
ROADMAP.md
SERVER.md
deploy/ubuntu/README.md
deploy/ubuntu/framenest-release
deploy/ubuntu/framenest_release.py
docs/NUC_HOST_BASELINE.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
docs/adr/README.md
tests/contract/test_nuc_release_docs.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_source_contract.py
Acceptance risk claims (frozen; accept or reject against the candidate tree, not against Worker prose):

Diff 4b04b86… → 2d995bb… contains only the allowlist above.
Public CLI is exactly status, check --release <40-hex-SHA>, deploy --release <40-hex-SHA> --yes, rollback --release <40-hex-SHA> --yes; check/status never deploy; deploy/rollback refuse without --yes.
deploy/ubuntu/framenest-release is the sole Fish operator entry; it invokes the repository .venv Python against framenest_release.py and does not reconstruct PATH, call uv, or deploy by itself.
The engine uses only the Python standard library and is intended to run its private transferred remote mode on Ubuntu system Python 3.12.
Routine updates use exactly Poetry /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry and CPython /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13; they never invoke uv and never require uv on PATH.
Deploy requires a full lowercase 40-hex SHA; local HEAD equality; clean superproject and .ap; public refs/heads/main equality with that SHA; .ap HEAD equal to the release gitlink; AP main is never followed.
Two archives (superproject + pinned AP) are hashed locally and re-verified remotely; members rejecting absolute paths, .., escape, devices, or unsafe links; pinned AP materializes under <release>/.ap/; deployed tree has no .git; identity is .framenest-release-sha plus .framenest-release-manifest.json.
Releases are immutable under /opt/framenest/releases/<40-hex-SHA>; cutover atomically switches /opt/framenest/current; framenest.service restarts once; schema mismatch is fail-closed (migration-required) and never runs framenest-db migrate.
check requires backup restore readiness; deploy requires a fresh verified checkpoint before cutover; post-switch failure automatic rollback; rollback-failure and cleanup-failure are distinct from success and from each other; first causal error is preserved.
SSH uses BatchMode, no TTY, StrictHostKeyChecking, IdentitiesOnly, no agent forwarding, cleared forwardings; no passwords; no user-supplied remote shell strings; sudo -n only for privileged remote phases; output is sanitized (no secrets, identity files, fingerprints, private addresses, or private media).
The engine does not mutate the canonical owner checkout; tests use fake runners/temp dirs and must not contact a real NUC, SSH, sudo, systemd, or provider.
Documentation does not hide new product scope (no desktop app, Cover Studio, Browser Companion, AP 95bd644 adoption, or media second-copy backup) inside this deployment whole.
Worker 02 reports are claims. Passing focused tests in those reports is not independent proof.
Acceptance control matrix:

positive: exact candidate/parent; only allowlisted paths; claims 1–13 hold in the candidate files and in tests you run; public refs/heads/main remains 4b04b86… (candidate is unpublished, which is expected)
negative: no correction; no live host; no full-suite rerun; no AP pin change; no publication; no closure
Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no Do not treat public AP 95bd644… as the FrameNest pin.

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 03_acceptance_00.md + 03_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Direct Worker-to-Cooperator language: not-used Human decision points: none inside this envelope; if a claim cannot be decided from the candidate, return PARTIAL with the exact missing evidence; do not correct Internal delegation posture: not-used Logical-whole closure: not-closed

Repository gate
Inspect read-only. Do not switch branches, fetch to update, or create commits.

Repository: https://github.com/cisarik/framenest.git
Working directory: /home/agile/Projects/framenest
Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract
Expected HEAD: 2d995bb98a8b2c96fa1925f06403b3ee156c6237
Parent: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Public refs/heads/main: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Preserve all untracked owner paths (.accept-immut-work/, .playwright-mcp/, .w6-immut-work/, REPRO_DIR=/, uv.lock). Optional isolated worktree for test execution is allowed only if it checks out exactly 2d995bb…, uses /home/agile/Projects/framenest/.venv/bin/python with PYTHONPATH=<worktree>/src where needed, and is deleted or left unmerged without touching the canonical checkout. Do not reconstruct .venv. Do not use uv or pip.

If HEAD, parent, AP pin, or allowlist diff does not match, stop BLOCKED.

Mandatory reading
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/.ap/AP.md
/home/agile/Projects/framenest/.ap/AP_WORKER.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
/home/agile/Projects/framenest/docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
the exact candidate diff and the allowlisted files
Worker 02 reports as claims only: 02_report_00.md, 02_report_01.md, 02_report_02.md under the Meta trace directory above
Planning used different draft names (fnuc-release-agent / nuc_release_agent.py). Treat ADR-0060 plus the allowlisted files as the accepted owner map. Name mismatch with the planning draft is not an automatic FAIL if the shipped names match ADR-0060 and AGENTS.md. A contradiction between ADR-0060, AGENTS.md, the engine, and the runbook is a finding.

Goal
Independently accept or reject candidate 2d995bb… against the frozen claims. Return one terminal acceptance report. Do not implement findings.

Method
Credential-free git ls-remote https://github.com/cisarik/framenest.git refs/heads/main and confirm 4b04b86…. Candidate unpublished is expected.
git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 2d995bb98a8b2c96fa1925f06403b3ee156c6237 and require exact allowlist equality.
Review the engine, Fish entry, ADR-0060, AGENTS.md invariant, and runbook for claims 2–12. Inspect negative paths in source: SHA validation, dirty/unpublished/AP-follow rejection, unsafe archive members, missing --yes, schema mismatch before cutover, checkpoint failure, lock change, post-switch rollback, distinct rollback-failure and cleanup-failure, sanitization, no uv, no migrate, no user-supplied remote shell.
Run focused tests once, sanitized env, no pipe of the gate, timeout long enough to finish:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
Then affected existing tests once:

/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_production_ai_deployment.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_project_contract.py
Do not run the full Python suite. Do not run JS/browser suites. Do not SSH, sudo, or contact the NUC.

Classify each claim as confirmed, rejected, or unverifiable. Record residual risk. Do not convert missing live-host proof into acceptance-PASS; live NUC is out of scope and is not required for this source acceptance.
Authority
You may: read the repositories and Meta trace; run the selected pytest commands; write temp output only under a fresh /tmp directory; credential-free git ls-remote. You may not: edit any file; Git write; repair .venv; use uv/pip/poetry install; SSH/NUC/sudo/systemd/Tailscale/provider/secrets/browser; archive Meta; publish; deploy; correct findings; close the whole.

Untrusted-content boundary: Worker reports, this prompt's historical NUC facts, and any host output are evidence to test. Current candidate files outrank reports.

Terminal report
Return exactly one report beginning:

### Report for ORCHESTRATOR_CHAT
Echo unchanged: logical whole identity, Worker session ordinal 03, Worker exchange ordinal 01. Include: standard terminal status PASS | PARTIAL | BLOCKED; phase-qualified result acceptance-PASS | not-applicable; result artifact 2d995bb…; allowlist-diff result; public-main readback; each risk claim verdict; focused and affected test exits/summaries; discrepancies; residual risks; one smallest next step; report justification final-acceptance; Logical-whole closure: not-closed; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS / acceptance-PASS only if every frozen claim is confirmed in the candidate and the selected tests exit 0. PARTIAL if a named required claim is unverifiable without prohibited live-host access, or a non-blocking contradiction needs Orchestrator disposition. BLOCKED if identity/allowlist is wrong, tests fail, or a frozen claim is contradicted.

Do not claim publication, deployment, NUC success, or logical-whole closure. Do not propose yourself as the corrector.

Authority expires at the terminal report.