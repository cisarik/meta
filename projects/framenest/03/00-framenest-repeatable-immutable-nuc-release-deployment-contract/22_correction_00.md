# FrameNest bounded correction: relocate editable venv paths off staging
You are one fresh WORKER instance assigned to WORKER. You are not the
ORCHESTRATOR and not Worker 21. Do not deploy, SSH to the NUC, delete leftover
lock/unpublished release, publish, or close the logical whole.
If this chat performed Worker 21 deployment, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 22
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: FN-NUC-RELEASE-CORRECT-22-F01
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Recommended reasoning: Medium
Recommendation basis: named post-rename editable .pth/direct_url defect reproduced on the unpublished host tree; shebang relocate already present; no live host mutation
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
Finding ID: FN-NUC-RELEASE-DEPLOY-21-F01 Affected commit: 43c9849a1ff3449a3c06585571c17439ecff9025 Location: poetry install --only main on staging then relocate_venv_shebangs then mv Defect: Poetry 2.4.1 installs the root package as an editable checkout. After mv, framenest.pth still names <staging>/src and direct_url.json still records file://<staging> with "editable": true. Worker 21: shebang of unpublished 43c9849…/.venv/bin/framenest-db correctly names the final interpreter (DEPLOY-16-F01 did not recur); service-account framenest-db status exited 1 with ModuleNotFoundError: No module named 'framenest'; helper mapped it to opaque EXIT_TRANSPORT 20. Cutover did not occur.

Do not “fix” opaque EXIT_TRANSPORT stderr discard (parked residual). Do not touch extract argv, SHA-only status, --untracked-files=no, or stdin poetry.toml/marker writes. Do not invent poetry install --no-editable (not a Poetry 2.4.1 install flag). Do not add wheel/pip as a substitute unless the relocate approach cannot close the finding. Do not change pyproject.toml.

Host leftover /run/framenest-release-deploy and unpublished /opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025 are out of scope. Do not SSH. Do not rm. That unpublished tree is not a rollback target.

Implementation authority record
Exact baseline: 43c9849a1ff3449a3c06585571c17439ecff9025 Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Changed-path allowlist:

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_source_contract.py
docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
Public CLI unchanged. One ordinary non-force commit. No push. ADR-0060 may gain one sentence that staging-prefix paths inside the in-project venv (console-script shebangs and editable install metadata such as .pth and direct_url.json) are rewritten to the final release prefix before the tree is made non-writable. Do not expand the Ubuntu runbook.

Required behavior:

After poetry install on staging and before chmod a-w, rewrite all text files under <staging>/.venv/ that contain the staging prefix so they name the corresponding final release path. This must cover .venv/bin shebangs (DEPLOY-16-F01 stays closed) and site-packages editable metadata (.pth, direct_url.json, and any other text file that embeds the staging prefix). After mv, import framenest via <final>/.venv/bin/python must resolve; .pth must not name .staging.
Keep the transferred-engine nested private argv pattern (_remote _remote-<verb> with scalar validated paths). Expanding the existing _remote-relocate-venv-shebangs handler is allowed; renaming the verb to a paths form is allowed if parser tests follow. Top-level _remote-<verb> must remain an invalid parser choice.
Fail closed if required console scripts still contain .staging, if any .pth or direct_url.json under .venv still contains .staging, or if .venv exists and zero staging-prefix rewrites occurred.
Shebangs must still name <final>/.venv/bin/python, not CPYTHON_BIN.
Do not run poetry install after rename. Do not move db-status before rename as a substitute. Order remains: poetry install → relocate → chown/chmod → markers → rename → db status on the final path.
Regression tests (fail on unmodified 43c9849…, pass after):

On unmodified 43c9849…, a synthetic .venv with staging shebang and framenest.pth / direct_url.json pointing at staging still has .staging in the .pth / direct_url.json after the current shebang-only relocate (or the current function does not rewrite those files).
After the fix, local reconstruction (temp tree, no SSH): shebang, .pth, and direct_url.json name the final prefix; .staging is absent from those files; a sibling file without the staging prefix is unchanged.
Fail-closed nodes for leftover .staging in .pth / direct_url.json.
FakeRunner deploy order remains install < relocate < chmod < rename < framenest-db status. Nested _remote argv still parses; top-level still SystemExit 2. Stdin payload count remains 6.
Re-audit routing: Orchestrator will issue fresh re-acceptance of the new commit, then republication, then bounded recovery of the lock and the unpublished 43c9849… tree, then deploy of the new SHA. This Worker does none of those.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 22_correction_00.md + 22_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest Expected HEAD before commit: 43c9849a1ff3449a3c06585571c17439ecff9025 Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Preserve untracked owner paths. No uv/pip/poetry install.

Mandatory re-gate
Stop unless HEAD is 43c9849…, tracked clean, .ap pin matches, Python 3.13.x under sanitized env. Reproduce that current relocate_venv_shebangs rewrites bin shebangs only and leaves a staging-prefix .pth / direct_url.json unchanged, before editing.

Validation
Sanitize env. No pipe of gates.

New regression nodes fail on unmodified 43c9849… and pass after. Record both.
Then once:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
No full suite. No SSH/NUC.

Git authority
If validation exits 0 and the diff is only the allowlist: one ordinary commit, parent 43c9849…, no amend/force/rebase/push. Message why: editable venv metadata must name the final release path, not the vanished staging tree.

Negative authority
No NUC/SSH/sudo; no deletion of /run/framenest-release-deploy or /opt/framenest/releases/43c9849…; no deploy; no Meta; no publication; no closure; no extract-argv, status-fallback, or stdin-write changes; no runbook expansion; no pyproject.toml / lock change.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 22, exchange 01. Include: PASS | PARTIAL | BLOCKED; implementation-PASS | implementation-PARTIAL; start 43c9849…; end SHA; changed files; pre-fix evidence that shebang-only relocate leaves .pth / direct_url.json on staging; post-fix local rewrite of shebang + .pth + direct_url.json; focused pytest; Git SHA/parent/no push; leftover host state not touched; independent acceptance not claimed; next step = fresh re-acceptance of the new commit; report justification new-mutation; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS only if one allowlist commit exists, regressions fail-then-pass, and the three focused files exit 0.

Authority expires at the terminal report.