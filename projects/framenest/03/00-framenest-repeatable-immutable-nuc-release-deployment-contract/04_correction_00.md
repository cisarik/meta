# FrameNest bounded correction: remote extract private argv
You are one fresh WORKER instance assigned to WORKER. You are not the
ORCHESTRATOR and not the Worker 03 auditor. Do not close the logical whole.
If this chat performed the Worker 03 independent acceptance of 2d995bb…, stop
and report BLOCKED. Do not correct in the auditor session.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: FN-NUC-RELEASE-CORRECT-04-F01
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Recommended reasoning: Medium
Recommendation basis: one named argv wiring defect with a failing parse probe and a required regression test; no design reopen
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
Out-of-scope observations: ledger-candidates only
Accepted finding (Orchestrator-confirmed)
Finding ID: FN-NUC-RELEASE-ACCEPT-03-F01 Status: open → correct in this exchange Affected commit: 2d995bb98a8b2c96fa1925f06403b3ee156c6237 Exact location: deploy/ubuntu/framenest_release.py cmd_remote_extract Defect: emitted remote command is sudo -n python3 <engine> _remote-extract --archive … --destination … Parser private mode is nested _remote _remote-extract. Direct parse of the emitted argv is invalid choice: '_remote-extract' / SystemExit 2. Local extract_validated_archive therefore cannot run on the transferred-engine path required by ADR-0060. Focused tests match substring _remote-extract in a fake SSH string and never parse engine argv. Audit authority: none. Do not re-audit unrelated claims. Do not certify your own correction as independent acceptance.

Implementation authority record
Exact baseline: 2d995bb98a8b2c96fa1925f06403b3ee156c6237 Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Changed-path allowlist:

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
Implementation boundaries: make cmd_remote_extract invoke the argv the parser already accepts; add a contract test that fails on the baseline and passes after the fix. No other findings, no ADR rewrite, no runbook/product edits, no public CLI change, no live NUC.

Regression test (must fail on 2d995bb… before the engine edit, pass after):

Build cmd_remote_extract(...).
shlex.split the command, drop sudo -n python3 <engine>, and feed the remaining argv to engine._build_parser().parse_args.
Assert command == "_remote", remote_command == "_remote-extract", and archive/destination match the inputs.
Call engine.main with that private argv (no SSH) against a temporary safe archive and a destination under /tmp or pytest tmp_path, and assert a safe member is extracted via the private mode (this is the path deploy currently cannot enter).
Assert top-level ["_remote-extract", ...] still fails to parse (SystemExit or parser error). That keeps the trap visible.
Re-audit routing: Orchestrator will issue a separate fresh Worker 05 full-fresh re-acceptance of the new commit. This Worker must not perform it.

Commits: exactly one ordinary non-force commit on the expected branch. No push.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no Do not treat public AP 95bd644… as the FrameNest pin.

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 04_correction_00.md + 04_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Direct Worker-to-Cooperator language: not-used Human decision points: none inside this envelope Internal delegation posture: not-used Logical-whole closure: not-closed

Repository identities
Repository checkout topology: standalone checkout Repository identity: https://github.com/cisarik/framenest.git Working directory: /home/agile/Projects/framenest Expected HEAD before commit: 2d995bb98a8b2c96fa1925f06403b3ee156c6237 Parent of baseline: 4b04b86e4ea52c673c41624e3f2abe1e59d45907 Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Do not use uv, pip, poetry install, or ./framenest setup.

Mandatory reading
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
/home/agile/Projects/framenest/.ap/AP.md
/home/agile/Projects/framenest/.ap/AP_WORKER.md
deploy/ubuntu/framenest_release.py functions cmd_remote_extract, _build_parser, _cmd_remote, remote_extract
tests/contract/test_nuc_release_remote_contract.py
Worker 03 report as the finding claim only
Goal
On baseline 2d995bb…, correct only FN-NUC-RELEASE-ACCEPT-03-F01 so the transferred-engine extract command is the nested private mode the parser accepts, with a causal regression test. One commit. Honest implementation-PASS only if tests prove the parser accepts the emitted argv and private-mode extract runs. Do not self-certify independent acceptance.

Mandatory re-gate
Stop unless:

HEAD == 2d995bb98a8b2c96fa1925f06403b3ee156c6237 on the expected branch;
zero tracked changes; no active Git operation; preserve all untracked owner paths (.accept-immut-work/, .playwright-mcp/, .w6-immut-work/, REPRO_DIR=/, uv.lock);
.ap gitlink and HEAD == 17b7e085139e9bcbb0e4953d26aef9b6687d541c;
canonical interpreter is Python 3.13.x (sanitize AppImage/LD_LIBRARY_PATH / PYTHONHOME per WORKER_EXECUTION_CONTRACT).
Reproduce the defect before editing the engine: parse the current cmd_remote_extract argv and record SystemExit 2. Then add the regression test so it fails on the baseline, then fix cmd_remote_extract only.

Authorized change
In cmd_remote_extract, emit _remote _remote-extract after the quoted engine path. Keep sudo -n python3, --archive, --destination, and shlex.quote. Do not add a second top-level _remote-extract parser. Do not change public CLI (status / check / deploy / rollback). Do not expand FakeRunner except as needed for the new test. Do not “fix” parked residuals: log-sanitizer token list, rollback-failure stderr phrasing, or a new deploy without --yes test.

Validation
Sanitize env. Do not pipe gates through tail/grep. Timeout long enough.

The new regression node(s) in tests/contract/test_nuc_release_remote_contract.py must fail on unmodified 2d995bb… and pass after the engine edit. Record both.
Then once:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
Do not run the full suite. Do not SSH, sudo, or contact the NUC.

Git authority
If validation exits 0 and the diff is only the allowlist:

stage only those two paths;
one ordinary commit on the current branch; parent must be 2d995bb…;
no amend, force, rebase, merge, stash, reset, clean, or push;
do not touch untracked owner files;
commit message in the repository style, focused on why: the transferred engine must invoke nested _remote _remote-extract so archive validation actually runs.
If the diff escapes the allowlist or tests fail, do not commit; report PARTIAL or BLOCKED.

Negative authority
No source/docs outside the allowlist; no .ap / lock / .venv mutation; no uv/pip/poetry install; no NUC/SSH/sudo/provider/browser/secrets; no Meta archive; no publication; no deployment; no logical-whole closure; no second finding correction.

Terminal report
Return exactly one report beginning:

### Report for ORCHESTRATOR_CHAT
Echo unchanged: logical whole identity, Worker session ordinal 04, Worker exchange ordinal 01. Include: standard terminal status PASS | PARTIAL | BLOCKED; phase-qualified result implementation-PASS | implementation-PARTIAL | not-applicable; start commit 2d995bb…; end commit (new SHA or unchanged); changed files; pre-fix parse failure evidence; post-fix parse and private-mode extract evidence; focused pytest exit and summary; Git commit result (SHA, parent, no push); finding ID FN-NUC-RELEASE-ACCEPT-03-F01; statement that independent acceptance is not claimed; residual parked items untouched; one smallest next step (fresh re-acceptance of the new commit); report justification new-mutation; Logical-whole closure: not-closed;
Resolved Execution Issues / Near-Misses
; Pre-Existing Failure Classification; authority expiry.

PASS / implementation-PASS only if the one commit exists, parent is 2d995bb…, allowlist-only diff, regression fails before and passes after, and the three focused files exit 0. Do not claim acceptance-PASS, publication, deployment, or closure.

Authority expires at the terminal report.