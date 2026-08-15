# FrameNest bounded correction: relocate venv shebangs off the staging path
You are one fresh WORKER instance assigned to WORKER. You are not the
ORCHESTRATOR and not Worker 16. Do not deploy, SSH to the NUC, delete leftover
lock/unpublished release, publish, or close the logical whole.
If this chat performed Worker 16 deployment, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 17
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: FN-NUC-RELEASE-CORRECT-17-F01
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Recommended reasoning: Medium
Recommendation basis: named post-rename shebang defect reproduced on the unpublished host tree and in the engine sequence; no live host mutation in this exchange
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
Accepted finding
Finding ID: FN-NUC-RELEASE-DEPLOY-16-F01 Affected commit: d963df7dfc7d56c75f3696e8bc3830ee81a98534 Location: _cmd_deploy poetry install on staging_dir then cmd_remote_rename_staging then cmd_remote_db_status(target) Defect: Poetry console scripts bake absolute shebangs to <staging>/.venv/bin/python. After mv to the final release directory that interpreter path is gone. Worker 16: first line of unpublished /opt/framenest/releases/d963df7…/.venv/bin/framenest-db was #!/opt/framenest/releases/d963df7….staging/.venv/bin/python; that path test -e exit 1; service-account framenest-db status exit 127; helper mapped it to opaque EXIT_TRANSPORT 20. Cutover did not occur. Orchestrator confirmed the engine sequence: install on staging, chmod a-w, markers, rename, then db status on the final path.

Do not “fix” opaque EXIT_TRANSPORT stderr discard (parked residual). Do not touch extract argv, SHA-only status, --untracked-files=no, or stdin poetry.toml/marker writes.

Host leftover /run/framenest-release-deploy and unpublished /opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534 are out of scope. Do not SSH. Do not rm. That unpublished tree is not a rollback target.

Implementation authority record
Exact baseline: d963df7dfc7d56c75f3696e8bc3830ee81a98534 Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Changed-path allowlist:

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_source_contract.py
docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
Public CLI unchanged. One ordinary non-force commit. No push. ADR-0060 may gain one preparation sentence that console-script shebangs are rewritten from the staging prefix to the final release prefix before the tree is made non-writable. Do not expand the Ubuntu runbook.

Required behavior:

After poetry install on the staging tree and before chmod a-w, rewrite text shebangs under <staging>/.venv/bin/ that contain the staging prefix so they name the corresponding path under the final release directory (/opt/framenest/releases/<40-hex>/…). After mv, framenest-db and framenest-backup must invoke <final>/.venv/bin/python, which remains the in-project venv interpreter (do not retarget shebangs at CPYTHON_BIN; that would skip venv site-packages).
Prefer the transferred-engine nested private argv pattern already used by extract (_remote _remote-<verb> with scalar validated paths). Do not embed file payloads inside nested shlex.quote / sh -c strings. Top-level _remote-<verb> must remain an invalid parser choice (ACCEPT-03-F01 stays closed).
Fail closed if .venv/bin exists and zero shebangs were rewritten, or if framenest-db / framenest-backup still contain .staging after rewrite.
Do not run poetry install after rename (do not mutate the published name to regenerate scripts). Do not move db-status before rename as a substitute for shebang relocation.
Wire _cmd_deploy so order is: poetry install → shebang rewrite → chown/chmod → markers → rename → db status on the final path.
Regression tests (fail on unmodified d963df7…, pass after):

Deploy sequence on unmodified d963df7… has no shebang-rewrite remote command between install and db status.
After the fix, FakeRunner deploy order is install < rewrite < chmod < rename < framenest-db status.
Local reconstruction (temp tree, no SSH): a synthetic framenest-db whose first line is #!<staging>/.venv/bin/python becomes #!<final>/.venv/bin/python; a sibling framenest-backup likewise; .staging is absent from those files after rewrite; a file that did not contain the staging prefix is unchanged.
Nested _remote _remote-<verb> parses; top-level _remote-<verb> still SystemExit 2.
Happy-path FakeRunner deploy still reaches poetry.toml, markers, rename, and db status; stdin payload count remains 6.
Re-audit routing: Orchestrator will issue fresh re-acceptance of the new commit, then republication, then bounded recovery of the lock and the unpublished d963df7… tree, then deploy of the new SHA. This Worker does none of those.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 17_correction_00.md + 17_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest Expected HEAD before commit: d963df7dfc7d56c75f3696e8bc3830ee81a98534 Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Preserve untracked owner paths. No uv/pip/poetry install.

Mandatory re-gate
Stop unless HEAD is d963df7…, tracked clean, .ap pin matches, Python 3.13.x under sanitized env. Reproduce that _cmd_deploy installs on staging then renames then runs framenest-db on the final path, with no shebang rewrite, before editing.

Validation
Sanitize env. No pipe of gates.

New regression nodes fail on unmodified d963df7… and pass after. Record both.
Then once:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
No full suite. No SSH/NUC.

Git authority
If validation exits 0 and the diff is only the allowlist: one ordinary commit, parent d963df7…, no amend/force/rebase/push. Message why: venv console-script shebangs must name the final release interpreter, not the vanished staging path.

Negative authority
No NUC/SSH/sudo; no deletion of /run/framenest-release-deploy or /opt/framenest/releases/d963df7…; no deploy; no Meta; no publication; no closure; no extract-argv, status-fallback, or stdin-write changes; no runbook expansion.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 17, exchange 01. Include: PASS | PARTIAL | BLOCKED; implementation-PASS | implementation-PARTIAL; start d963df7…; end SHA; changed files; pre-fix sequence evidence (install → rename → db status, no rewrite); post-fix nested _remote argv and local shebang rewrite evidence; focused pytest; Git SHA/parent/no push; leftover host state not touched; independent acceptance not claimed; next step = fresh re-acceptance of the new commit; report justification new-mutation; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS only if one allowlist commit exists, regressions fail-then-pass, and the three focused files exit 0.

Authority expires at the terminal report.