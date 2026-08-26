# FrameNest — Implementation Worker prompt

Logical whole identity: framenest-nuc-push-workflow-and-companion-testing
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh implementation Worker, isolated worktree, exact-source evidence
Phase: implementation
Reasoning recommendation: High (documentation parity tests are strict; wording precision matters)
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-nuc-push-workflow-and-companion-testing/
Trace project key: framenest
Trace logical-whole projection identity: framenest-nuc-push-workflow-and-companion-testing
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

## Mission

Documentation-coherence and exit-13 runbook annex task following accepted
ADR-0075 (NUC as development-test target with routine release refresh) and the
session-01 Planner synthesis. You align remaining misleading present-tense
statements with shipped reality and document the safe schema-jump continuation
for `deploy/ubuntu/framenest-release`, including contract-test parity.

Exact baseline (also current public `main`):
`070681856bc6f14e12da52717dbccefa160554af`

## Edit authority — exact allowlist

You may modify ONLY these eight paths:

1. `README.md` — Status section only.
2. `SERVER.md` — NUC role/status present-tense statements only.
3. `docs/INFOSEC.md` — only present-tense "serves production" style statements.
4. `docs/ACCEPTANCE_DUAL_AUDIENCE.md` — Part B honesty banner and B3 Apply framing only.
5. `deploy/ubuntu/README.md` — routine-update wording only.
6. `docs/UBUNTU_NUC_DEPLOYMENT.md` — section 5 migration annex plus role notes; no other rewrites.
7. `tests/contract/test_nuc_release_docs.py`
8. `tests/contract/test_nuc_operator_runbook.py`

Everything else is read-only. In particular you must NOT touch:
accepted ADR bodies (`docs/adr/*.md` except reading them), `SECURITY.md`,
`docs/WORKER_EXECUTION_CONTRACT.md`, any Python product code,
`deploy/ubuntu/framenest_release.py`, `docs/X_COMPANION.md`.

## Required content changes

1. **README Status:** replace present-tense production-server divergence
   wording with the development-test NUC routinely targeting the exact public
   `main` SHA, `framenest-release status` as runtime readback; keep dated
   history sentences intact. Correct two factually false claims:
   - companion review Save does NOT publish; Apply writes metadata only and
     the administrator publication PUT (including unpublish on the same PUT)
     is the sole publication path ([ADR-0074]);
   - the local-only `public_published_uds` composition and workspace rollout
     successors ARE implemented at this baseline; public bind/TLS/Funnel
     remain unshipped ([ADR-0074]).
2. **SERVER.md:** replace "owner-authoritative production release" present
   tense with authoritative serving for the disposable development-test
   instance plus exact-main refresh/readback wording; retain the dated SHA
   paragraph as history.
3. **docs/INFOSEC.md:** change only present-tense "serves production over
   Tailscale" statements to development-test workspace access; keep audited
   checkout SHA and findings as historical evidence.
4. **Runbook section 5 + new exit-13 annex:** remove the dangerous
   `--chdir=/opt/framenest/current` schema-jump example. Document instead:
   - `deploy --yes` exits exactly 13 (`migration-required`) AFTER atomically
     publishing `/opt/framenest/releases/<T>` and BEFORE checkpoint/cutover;
   - verification before cleanup: current symlink/service unchanged on the old
     release; target `.framenest-release-sha` equals `<T>`;
     `.venv/bin/framenest-db` executable in the target tree; target-tree
     `framenest-db status` shows `current_revision=0032`,
     `head_revision=0033`; lock dir contains only known pre-schema-gate
     artifacts;
   - exact lock cleanup removing only those artifacts then the empty
     `/run/framenest-release-deploy`; unexpected contents stop the run;
   - explicit `framenest-db migrate` from the NEW release tree under the
     operator command execution contract (`sudo -u framenest --chdir=/opt/
     framenest/releases/<T> env FRAMENEST_ENV_FILE=/etc/framenest/
     framenest.env ...`), requiring post-migration status
     `current_revision=head_revision=0033`;
   - cutover completion via `rollback --release <T> --yes` (documented switch
     to an already-complete target tree);
   - final `status` evidence (exact SHA, active service, schema `0033`,
     backup ready) and terminal Cooperator `sudo -K`;
   - a post-migration cutover failure requires explicit triage, never an
     improvised downgrade or catalog restore.
5. **Acceptance guide Part B banner:** gate on tested public-`main` SHA equal
   to live `framenest-release status` active release; blocked runs report
   `BLOCKED: NUC not at tested SHA`. B3 Apply acceptance is deterministic by
   owner decision (2026-08-26); no rendered Apply entry exists for analyzed
   rows — say so plainly instead of implying one.
6. **Contract tests:** adapt both suites so service-account examples under
   active-tree sections use `/opt/framenest/current` while the documented
   schema-jump continuation examples use `/opt/framenest/releases/<T>`; add
   parity assertions for the new annex facts above.

## Hard boundaries

- `framenest-release` keeps exactly four public commands; the engine stays
  migration-free; no fifth helper command.
- No global replacement of "production", `/opt/framenest/current`, or
  historical SHAs; do not reopen closed logical wholes; stale-but-historical
  text stays historical.
- No NUC access, no SSH, no sudo, no wrapper execution, no provider calls, no
  browser use, no push/publication.

## Execution and validation

- Isolated worktree from exact baseline `0706818…`; canonical checkout stays
  untouched.
- All Python evidence ONLY through `./.ap/ap project check` and
  `./.ap/ap exec` with exact `--baseline 070681856bc6f14e12da52717dbccefa160554af`.
- Minimum evidence: the two updated documentation contract suites green at the
  exact baseline, plus a focused link/diff review statement.
- Commit locally inside your isolated worktree; report the commit SHA. No push.

## Output

Write `02_report_01.md` in the trace discovery path, professional English,
beginning exactly:

### Report for ORCHESTRATOR_CHAT

Include: changed-file list with per-file intent summary, exact commit SHA,
test invocation lines with outcomes, boundary-compliance confirmation, and any
deviation requests (never self-granted).

## Transition owner

ORCHESTRATOR verifies your claims against repository evidence, then handles
publication and NUC refresh sequencing. You have no follow-on authority.

## Stopping rule

Stop after a complete verified implementation within the allowlist, or request
direction through your report when an allowlisted change proves impossible
without crossing a boundary.
