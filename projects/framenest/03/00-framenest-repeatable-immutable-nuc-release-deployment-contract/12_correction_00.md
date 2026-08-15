# FrameNest bounded correction: remote poetry.toml / marker writes
You are one fresh WORKER instance assigned to WORKER. You are not the
ORCHESTRATOR and not Worker 11. Do not deploy, SSH to the NUC, delete the
leftover lock/staging, publish, or close the logical whole.
If this chat performed Worker 11 deployment, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: FN-NUC-RELEASE-CORRECT-12-F01
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Recommended reasoning: Medium
Recommendation basis: named nested-quote defect reproduced on the live staging tree and in the engine string; no live host mutation in this exchange
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
Accepted findings
Finding ID: FN-NUC-RELEASE-DEPLOY-11-F01 Affected commit: de580f6f9d18cddbc4ad7894d163a361b30ef05f Location: cmd_remote_write_poetry_toml Defect: POETRY_TOML ([virtualenvs]\nin-project = true\n) is shlex.quoted inside an already single-quoted sudo -n sh -c '…'. The remote shell splits; poetry.toml is never written. Worker 11: deploy EXIT_TRANSPORT 20 before cutover; staging lacks poetry.toml. Orchestrator confirmed the emitted string is quote-broken.

Finding ID: FN-NUC-RELEASE-DEPLOY-11-F02 (authorized adjacent, same class) Location: cmd_remote_write_markers Same nested-quote construction for manifest JSON and SHA. Not reached on the host because F01 failed first. Correct it in this same commit so the next deploy does not fail one step later.

Do not change cmd_remote_write_file unless required to reuse its stdin pattern. Do not “fix” opaque EXIT_TRANSPORT stderr discard (parked residual). Do not touch extract argv, SHA-only status, or --untracked-files=no.

Host leftover /run/framenest-release-deploy and /opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging are out of scope. Do not SSH. Do not rm.

Implementation authority record
Exact baseline: de580f6f9d18cddbc4ad7894d163a361b30ef05f Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Changed-path allowlist:

deploy/ubuntu/framenest_release.py
tests/contract/test_nuc_release_remote_contract.py
Public CLI unchanged. One ordinary non-force commit. No push.

Required behavior:

Remote writes of poetry.toml, .framenest-release-manifest.json, and .framenest-release-sha must not embed payload bytes inside nested single-quoted sh -c strings. Prefer the proven stdin/cat pattern used by cmd_remote_write_file (payload as input_bytes, path shlex.quoted only). Exact POETRY_TOML bytes and exact marker bytes must land in the destination files.
Wire _cmd_deploy to pass those payloads as stdin (or equivalent safe transfer). Do not leave builders that still emit the broken quote pattern.
New releases still write both markers and in-project = true poetry.toml.
Regression tests (fail on unmodified de580f6f…, pass after):

The string from cmd_remote_write_poetry_toml must not be a quote-broken sh -c that would run in-project as a command. After the fix, a local reconstruction (FakeRunner capturing stdin, or equivalent) must write exact POETRY_TOML bytes to the destination path.
Same for cmd_remote_write_markers (manifest JSON + SHA file with trailing newline as the engine already intends).
Happy-path FakeRunner deploy still reaches poetry.toml write and marker write; adjust FakeRunner matchers only as needed for the new transfer shape.
Re-audit routing: Orchestrator will issue fresh re-acceptance of the new commit, then republication, then bounded lock/staging recovery plus deploy. This Worker does none of those.

Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 12_correction_00.md + 12_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest Expected HEAD before commit: de580f6f9d18cddbc4ad7894d163a361b30ef05f Required AP pin/HEAD: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Canonical interpreter: /home/agile/Projects/framenest/.venv/bin/python Preserve untracked owner paths. No uv/pip/poetry install.

Mandatory re-gate
Stop unless HEAD is de580f6f…, tracked clean, .ap pin matches, Python 3.13.x under sanitized env. Reproduce the broken cmd_remote_write_poetry_toml string before editing.

Validation
Sanitize env. No pipe of gates.

New regression nodes fail on unmodified de580f6f… and pass after. Record both.
Then once:
/home/agile/Projects/framenest/.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
No full suite. No SSH/NUC.

Git authority
If validation exits 0 and the diff is only the allowlist: one ordinary commit, parent de580f6f…, no amend/force/rebase/push. Message why: remote poetry.toml and marker writes must use stdin-safe transfer, not nested shlex quotes.

Negative authority
No NUC/SSH/sudo; no deletion of /run/framenest-release-deploy or .staging; no deploy; no Meta; no publication; no closure; no extra docs; no extract-argv or status-fallback changes.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 12, exchange 01. Include: PASS | PARTIAL | BLOCKED; implementation-PASS | implementation-PARTIAL; start de580f6f…; end SHA; changed files; pre-fix broken command string; post-fix stdin/write evidence for poetry.toml and markers; focused pytest; Git SHA/parent/no push; leftover host state not touched; independent acceptance not claimed; next step = fresh re-acceptance of the new commit; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

PASS only if one allowlist commit exists, regressions fail-then-pass, and the three focused files exit 0.

Authority expires at the terminal report.