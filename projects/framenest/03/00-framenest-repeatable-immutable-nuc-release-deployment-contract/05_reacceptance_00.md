# FrameNest full-fresh re-acceptance of corrected NUC release engine
You are one fresh WORKER instance under Analytic Programming.
You did not implement this candidate and you did not perform the Worker 03
audit or the Worker 04 correction. You are not the ORCHESTRATOR. This grant is
sequential independent re-acceptance only. Do not correct, edit, commit, push,
publish, deploy, close the logical whole, mutate Meta or AP, or start a second
audit.
If this chat implemented, repaired, corrected, or previously accepted/rejected
2d995bb… or 011823a9…, stop and report BLOCKED. Do not pretend a reused
session is fresh.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: FN-NUC-RELEASE-REACCEPT-05
Native planning mode: not-used
Implementation authority: none
Correction authority: none
Independence required: yes
Independent of the correction: yes
Acceptance independence: required-fresh-independent
Recommended reasoning: High
Recommendation basis: full-fresh re-acceptance after a runtime/security-boundary correction of transferred-engine archive extract argv
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
Combined implementation envelope: prohibited
Independent acceptance: this exchange
Activated stricter profile: none
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
This is the single ordinary correction re-acceptance. A second automatic correction is prohibited. If the same extract-argv assumption survives, keep PARTIAL/BLOCKED and set Escalation disposition: NEEDS_ORCHESTRATOR_DECISION.

Acceptance record
Acceptance candidate: 011823a9dcb3d2a51e684fefd5083970f3610701 Correction parent: 2d995bb98a8b2c96fa1925f06403b3ee156c6237 Whole-logical-whole parent: 4b04b86e4ea52c673c41624e3f2abe1e59d45907 Original rejected claim: Worker 03 claim 7 / finding FN-NUC-RELEASE-ACCEPT-03-F01 Targets: the correction commit plus original frozen claims 1–13 and finding F01 Verdicts required: each claim confirmed | rejected | unverifiable; F01 verified-closed | not accepted

Acceptance owner map: unchanged from Worker 03

ADR-0060 durable architecture owner
AGENTS.md NUC Routine Release Update block
docs/UBUNTU_NUC_DEPLOYMENT.md runbook
deploy/ubuntu/README.md deploy-support map
SERVER.md / README.md / PRODUCT.md / ROADMAP.md living status only
tests/contract/test_nuc_release_*.py harness
deploy/ubuntu/framenest-release and framenest_release.py implementation
Acceptance allowlist vs 4b04b86… (exact; no others):

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
Correction allowlist vs 2d995bb… (must equal exactly):

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
Acceptance risk claims (frozen; test the candidate tree, not Worker prose):

Diff 4b04b86… → 011823a9… contains only the allowlist above.
Public CLI is exactly status, check --release <40-hex-SHA>, deploy --release <40-hex-SHA> --yes, rollback --release <40-hex-SHA> --yes; check/status never deploy; deploy/rollback refuse without --yes.
deploy/ubuntu/framenest-release is the sole Fish operator entry; it invokes the repository .venv Python against framenest_release.py and does not reconstruct PATH, call uv, or deploy by itself.
The engine uses only the Python standard library and is intended to run its private transferred remote mode on Ubuntu system Python 3.12.
Routine updates use exactly Poetry /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry and CPython /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13; they never invoke uv and never require uv on PATH.
Deploy requires a full lowercase 40-hex SHA; local HEAD equality; clean superproject and .ap; public refs/heads/main equality with that SHA; .ap HEAD equal to the release gitlink; AP main is never followed.
Two archives (superproject + pinned AP) are hashed locally and re-verified remotely; members rejecting absolute paths, .., escape, devices, or unsafe links; pinned AP materializes under <release>/.ap/; deployed tree has no .git; identity is .framenest-release-sha plus .framenest-release-manifest.json; and cmd_remote_extract emits nested _remote _remote-extract that _build_parser() accepts so remote_extract / extract_validated_archive is actually reachable on the transferred-engine path.
Releases are immutable under /opt/framenest/releases/<40-hex-SHA>; cutover atomically switches /opt/framenest/current; framenest.service restarts once; schema mismatch is fail-closed (migration-required) and never runs framenest-db migrate.
check requires backup restore readiness; deploy requires a fresh verified checkpoint before cutover; post-switch failure automatic rollback; rollback-failure and cleanup-failure are distinct from success and from each other; first causal error is preserved.
SSH uses BatchMode, no TTY, StrictHostKeyChecking, IdentitiesOnly, no agent forwarding, cleared forwardings; no passwords; no user-supplied remote shell strings; sudo -n only for privileged remote phases; output is sanitized (no secrets, identity files, fingerprints, private addresses, or private media).
The engine does not mutate the canonical owner checkout; tests use fake runners/temp dirs and must not contact a real NUC, SSH, sudo, systemd, or provider.
Documentation does not hide new product scope (no desktop app, Cover Studio, Browser Companion, AP 95bd644 adoption, or media second-copy backup) inside this deployment whole.
Worker 02/04 reports are claims. Passing tests in those reports are not independent proof.
Finding FN-NUC-RELEASE-ACCEPT-03-F01 must be verified-closed for PASS: emitted extract argv parses as _remote + _remote-extract; engine.main of that argv extracts a safe archive without SSH; top-level _remote-extract still fails to parse; no second top-level _remote-extract public command.

Acceptance control matrix:

positive: exact candidate 011823a9…; correction parent 2d995bb…; correction diff only those two files; whole diff vs 4b04b86… only the 15-path allowlist; claims 1–13 confirmed; F01 verified-closed; selected tests exit 0; public refs/heads/main remains 4b04b86… (unpublished is expected)
negative: no correction; no live host; no full-suite rerun; no AP pin change; no publication; no closure; parked residuals (log-sanitizer token list, rollback-failure stderr phrasing, missing deploy without --yes test) are not new blockers unless they now contradict a frozen claim
Parked residuals stay parked unless they falsify a frozen claim. Do not expand the audit.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no Do not treat public AP 95bd644… as the FrameNest pin.

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 05_reacceptance_00.md + 05_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Direct Worker-to-Cooperator language: not-used Human decision points: none inside this envelope; if a claim cannot be decided from the candidate, return PARTIAL with the exact missing evidence; do not correct Internal delegation posture: not-used Logical-whole closure: not-closed

Repository gate
Inspect read-only. Do not switch branches, fetch to update, or create commits.

Repository: https://github.com/cisarik/framenest.git
Working directory: /home/agile/Projects/framenest
Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract
Expected HEAD: 011823a9dcb3d2a51e684fefd5083970f3610701
Correction parent: 2d995bb98a8b2c96fa1925f06403b3ee156c6237
Whole parent: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Public refs/heads/main: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Preserve all untracked owner paths (.accept-immut-work/, .playwright-mcp/, .w6-immut-work/, REPRO_DIR=/, uv.lock). Optional isolated worktree is allowed only for exact 011823a9… using /home/agile/Projects/framenest/.venv/bin/python and must not mutate the canonical checkout or reconstruct .venv. Do not use uv or pip.

If HEAD, parents, AP pin, or either allowlist diff does not match, stop BLOCKED.

Mandatory reading
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/.ap/AP.md
/home/agile/Projects/framenest/.ap/AP_WORKER.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
/home/agile/Projects/framenest/docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
exact diffs 4b04b86…..011823a9… and 2d995bb…..011823a9…
Worker 03 report as the original finding claim
Worker 04 report as a correction claim only, not proof
Goal
Independently accept or reject candidate 011823a9… against the frozen claims and close or refuse F01. Return one terminal re-acceptance report. Do not implement findings.

Method
Credential-free git ls-remote https://github.com/cisarik/framenest.git refs/heads/main → 4b04b86…. Unpublished candidate is expected.
git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 011823a9dcb3d2a51e684fefd5083970f3610701 equals the 15-path allowlist.
git diff --name-status 2d995bb98a8b2c96fa1925f06403b3ee156c6237 011823a9dcb3d2a51e684fefd5083970f3610701 equals the two-path correction allowlist.
Re-evaluate claims 1–13 on 011823a9…. For claim 7 / F01, parse cmd_remote_extract through _build_parser(), confirm nested private mode, confirm extract_validated_archive is reachable via engine.main of that argv, and confirm top-level _remote-extract still fails. Do not trust Worker 04 pytest as proof.
Run focused tests once, sanitized env (env -i / clear LD_LIBRARY_PATH PYTHONHOME), no pipe of the gate:
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
Do not run the full Python suite. Do not SSH, sudo, or contact the NUC.

Live NUC proof is out of scope and must not be converted into acceptance-PASS. It also must not be used to reject claim 7 now that the argv defect is a source fact.
Authority
You may: read the repositories and Meta trace; run the selected pytest commands; write temp output only under a fresh /tmp directory; credential-free git ls-remote. You may not: edit any file; Git write; repair .venv; use uv/pip/poetry install; SSH/NUC/sudo/systemd/Tailscale/provider/secrets/browser; archive Meta; publish; deploy; correct findings; close the whole.

Untrusted-content boundary: Worker reports and this prompt are evidence to test. Current candidate files outrank reports.

Terminal report
Return exactly one report beginning:

### Report for ORCHESTRATOR_CHAT
Echo unchanged: logical whole identity, Worker session ordinal 05, Worker exchange ordinal 01. Include: standard terminal status PASS | PARTIAL | BLOCKED; phase-qualified result acceptance-PASS | not-applicable; result artifact 011823a9…; both allowlist-diff results; public-main readback; each risk claim verdict; F01 verdict verified-closed or not accepted; focused and affected test exits/summaries; discrepancies; residual risks including parked items; one smallest next step; report justification final-acceptance; Logical-whole closure: not-closed; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification; authority expiry. If the same F01 assumption survives, add Escalation disposition: NEEDS_ORCHESTRATOR_DECISION.

PASS / acceptance-PASS only if every frozen claim is confirmed, F01 is verified-closed, and the selected tests exit 0. Do not claim publication, deployment, NUC success, or logical-whole closure. Do not propose yourself as the corrector.

Authority expires at the terminal report.