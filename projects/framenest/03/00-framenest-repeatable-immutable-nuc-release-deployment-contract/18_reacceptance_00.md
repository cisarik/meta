# FrameNest full-fresh re-acceptance of venv shebang relocation
You are one fresh WORKER instance under Analytic Programming.
You did not implement this candidate and you did not perform Worker 03–17
work on it. You are not the ORCHESTRATOR. Sequential independent
re-acceptance only. Do not correct, edit, commit, push, publish, deploy,
SSH to the NUC, delete leftover lock/unpublished release, write host markers,
mutate Meta or AP, or close the whole.
If this chat implemented, corrected, accepted, published, recovered leftover
state, or deployed 2d995bb…, 011823a9…, de580f6f…, d963df7…, or 43c9849…,
stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 18
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: FN-NUC-RELEASE-REACCEPT-18
Native planning mode: not-used
Implementation authority: none
Correction authority: none
Independence required: yes
Independent of the correction: yes
Acceptance independence: required-fresh-independent
Recommended reasoning: High
Recommendation basis: full-fresh re-acceptance after runtime change that rewrites staging-prefix venv shebangs to the final release path before chmod
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
If staging-prefix shebangs still survive until framenest-db status, rewrite runs after chmod, shebangs are retargeted at CPYTHON_BIN, or nested _remote argv is missing, keep PARTIAL/BLOCKED and set Escalation disposition: NEEDS_ORCHESTRATOR_DECISION. Do not propose yourself as the corrector.

Acceptance record
Acceptance candidate: 43c9849a1ff3449a3c06585571c17439ecff9025 Accepted tree: df98c395cc4d88cd8b37a92f854f79a245b0facd Correction parent: d963df7dfc7d56c75f3696e8bc3830ee81a98534 Whole-logical-whole parent: 4b04b86e4ea52c673c41624e3f2abe1e59d45907 Public refs/heads/main (unpublished successor expected): d963df7dfc7d56c75f3696e8bc3830ee81a98534 Required AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c

Prior closed findings (must remain closed):

FN-NUC-RELEASE-ACCEPT-03-F01 nested _remote _remote-extract
FN-NUC-RELEASE-DEPLOY-07-F01 SHA-only status / no forged host manifest
FN-NUC-RELEASE-DEPLOY-07-F02 --untracked-files=no
FN-NUC-RELEASE-DEPLOY-11-F01 poetry.toml stdin write
FN-NUC-RELEASE-DEPLOY-11-F02 marker stdin write
Finding under re-acceptance:

FN-NUC-RELEASE-DEPLOY-16-F01 staging-path Poetry shebangs after mv
Acceptance owner map: unchanged (ADR-0060, AGENTS.md NUC block, runbook, tests, engine).

Allowlist vs 4b04b86… (exact; same 15 paths):

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
Correction allowlist vs d963df7… (must equal exactly):

deploy/ubuntu/framenest_release.py
docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_source_contract.py
Frozen claims (candidate files outrank Worker 17 prose):

Diff 4b04b86… → 43c9849… contains only the 15-path allowlist.
Diff d963df7… → 43c9849… contains only the four-path correction allowlist.
Public CLI remains status / check --release <40-hex> / deploy --release <40-hex> --yes / rollback --release <40-hex> --yes; check/status never deploy; deploy/rollback refuse without --yes.
framenest-release is the sole Fish entry; no uv on the routine path; stdlib engine; exact NUC Poetry/CPython paths unchanged.
Nested private extract remains _remote _remote-extract; top-level _remote-extract still fails to parse (ACCEPT-03-F01 stays verified-closed).
DEPLOY-07-F01 stays verified-closed: SHA-only current tree is readable; helper does not synthesize a host manifest on an old tree. New releases still write both markers.
DEPLOY-07-F02 stays verified-closed: verify_clean_worktrees uses --untracked-files=no; tracked dirty still EXIT_SOURCE_GATE. ADR silence on untracked remains residual.
DEPLOY-11-F01/F02 stay verified-closed: poetry.toml and markers remain stdin cat; payloads are not nested inside shlex.quote/sh -c; _cmd_deploy still passes six stdin payloads (engine, two archives, poetry.toml, manifest, SHA).
DEPLOY-16-F01 verified-closed only if:
_cmd_deploy order is poetry install → shebang relocate → chown/chmod → markers → rename → framenest-db status on the final path;
relocate uses nested sudo -n python3 <engine> _remote _remote-relocate-venv-shebangs --staging … --final …;
top-level _remote-relocate-venv-shebangs is still an invalid parser choice;
relocate_venv_shebangs rewrites text shebangs under <staging>/.venv/bin/ from the staging prefix to the final release prefix;
framenest-db and framenest-backup first lines become #!<final>/.venv/bin/python (not CPYTHON_BIN); .staging is absent from those files afterward;
fail-closed if .venv/bin exists and zero shebangs are rewritten, or if required console scripts still contain .staging;
poetry install is not run after rename; db-status is not moved before rename as a substitute.
ADR-0060 states that console-script shebangs are rewritten from the staging prefix to the final release prefix before the tree is made non-writable. Ubuntu runbook was not required to expand.
SHA/public-main/AP-pin/archive-member/immutable-release/atomic-cutover/same-schema/no-migrate/backup-checkpoint/rollback-distinct/SSH-options/sanitized-output/no-canonical-checkout-mutation/no-hidden-product-scope claims from Worker 05 remain true on this successor except where claims 8–10 explicitly change remote write/shebang preparation.
Worker 17 tests and local reconstruction are claims, not independent proof. Live NUC leftover /run/framenest-release-deploy and unpublished /opt/framenest/releases/d963df7… are out of scope, are not a rollback target, and must not be converted into acceptance-PASS or deleted.
Control matrix:

positive: exact candidate/parents/tree; both allowlists; claims 1–12; DEPLOY-16-F01 verified-closed; prior closed findings still closed; selected tests exit 0
negative: no correction; no NUC; no full suite; no publication; no closure; parked residuals (EXIT_TRANSPORT stderr discard, log-sanitizer tokens, rollback stderr phrasing, missing deploy-without---yes pytest, ADR silence on untracked) stay parked unless they falsify a frozen claim
Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 18_reacceptance_00.md + 18_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Logical-whole closure: not-closed

Repository gate
Working directory: /home/agile/Projects/framenest Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Expected HEAD: 43c9849a1ff3449a3c06585571c17439ecff9025 Preserve untracked owner paths. Git write: none. If HEAD/parents/AP pin/allowlists mismatch, BLOCKED.

Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Sanitize Cursor/AppImage LD_LIBRARY_PATH/PYTHONHOME. Do not reconstruct .venv. No uv.

Mandatory reading
AGENTS.md, .ap/AP.md, .ap/AP_WORKER.md, docs/WORKER_EXECUTION_CONTRACT.md, ADR-0060, diffs 4b04b86…..43c9849… and d963df7…..43c9849…, Worker 16 as host finding, Worker 17 as correction claim only.

Method
Credential-free git ls-remote https://github.com/cisarik/framenest.git refs/heads/main → d963df7….
Both name-status diffs equal the frozen allowlists. Confirm tree df98c395cc4d88cd8b37a92f854f79a245b0facd.
Independently probe builders, _cmd_deploy order, nested relocate argv, local relocate_venv_shebangs on a temp tree, stdin poetry/marker writes, nested extract, SHA-only status, and --untracked-files=no. Do not trust Worker 17 pytest as proof.
Focused tests once, sanitized env, no pipe of gates:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
Then affected once:

/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_production_ai_deployment.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_project_contract.py
No full suite. No SSH/NUC.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 18, exchange 01. Include: PASS | PARTIAL | BLOCKED; acceptance-PASS | not-applicable; artifact 43c9849…; tree; both allowlist diffs; public-main readback; each claim verdict; ACCEPT-03-F01, DEPLOY-07-F01/F02, DEPLOY-11-F01/F02, and DEPLOY-16-F01 verdicts; independent shebang-rewrite evidence; test exits; residuals; next step = republication of this SHA (not deploy, not lock/unpublished-tree recovery yet); report justification final-acceptance only if acceptance-PASS, else new-evidence; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS / acceptance-PASS only if every frozen claim is confirmed, DEPLOY-16-F01 is verified-closed, prior closed findings remain closed, and selected tests exit 0. Do not claim publication, deployment, recovery, or closure.

Authority expires at the terminal report.