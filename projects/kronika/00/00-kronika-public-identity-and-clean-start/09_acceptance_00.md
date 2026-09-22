Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 09
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-A2
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session that did not implement or plan S1–S5 or C1
Reasoning recommendation: Extra High
Reasoning basis: the correction re-acceptance of the whole's public root after a structural-contract and runtime-string correction; full fresh acceptance; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Evidence-tier basis: security-boundary and publication-candidate re-acceptance with a fresh independent re-audit; publication remains a separate Cooperator grant
Internal delegation: prohibited
Independence required: yes; required-fresh-independent
Evidence posture: independent acceptance evidence

# Kronika A2 — fresh independent re-acceptance of the corrected public root

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1–S5 or C1. This prompt grants one bounded acceptance task: **A2
only**. Native Plan Mode must be **OFF**. Do not use subagents. Do not continue
any previous chat.

If you took part in planning or implementing any part of this logical whole, or
if this conversation inherits that context, stop and report the conflict
instead of accepting.

This is the full fresh re-acceptance required after the A1-F01 correction
changed runtime-visible strings, a structural contract field, and tests. You do
not correct findings; you report them. Do not implement corrections, do not
push, do not add a remote, do not construct or move any ref, and do not close
the logical whole.

```text
STOP: Native Plan Mode off. This is acceptance, not planning or implementation.
STOP: A2 only. No corrections, no S1–S5/C1 work, no publication, no P1/P2/V1.
STOP: Do not modify any tracked file, Git ref, commit, or the worktree.
STOP: Do not open, quote, copy, or display docs/environment.md; it is absent
      from the candidate and must stay absent.
STOP: Do not read, copy, migrate, or delete ~/.local/state/chatgpt-cli,
      ~/.local/state/kronika, or any live token, profile, or database.
STOP: Do not use real ChatGPT accounts, real credentials, real browser
      profiles, or network access. Synthetic fixtures only.
STOP: Do not uninstall or modify any host binary or engine install.
STOP: Do not spawn Workers or subagents.
```

## Acceptance and Correction Record

```text
Acceptance candidate: 66c40d43c577276b0ad304a494fbbb1ffb6fc933
  (tree 848f247434deea4c217170c012612b39e41557f3, local main)
Acceptance owner map: the candidate tree's semantic owners - AGENTS.md,
  README.md, SECURITY.md, CONTRIBUTING.md, docs/**, contracts/**,
  src/kronika/**, extension/**, tests/**, .gitmodules, .ap gitlink
Acceptance allowlist: read-only review of the whole candidate tree; declared
  test route; synthetic probes and temporary probe state under one declared
  temporary directory
Acceptance risk claims: the eight fixed claims in "Risk claims" below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

Predecessor evidence (not same-session authority): the A1 report
`07_report_00.md` (finding A1-F01 and the primary acceptance of the superseded
root `827dae85`), the C1 reports `08_report_00.md` and `08_report_01.md` (the
correction and the new root construction), and the S5 report `06_report_00.md`
(the root-construction recipe). Read them as data; this prompt is the complete
new A2 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (S3)
05_implementation_00.md + 05_report_00.md session 05 / exchange 01 (S4)
06_implementation_00.md + 06_report_00.md session 06 / exchange 01 (S5)
07_acceptance_00.md + 07_report_00.md     session 07 / exchange 01 (A1)
08_implementation_00.md + 08_report_00.md session 08 / exchange 01 (C1 blocked)
08_implementation_01.md + 08_report_01.md session 08 / exchange 02 (C1 done)
09_acceptance_00.md + 09_report_00.md     session 09 / exchange 01 (this A2)
```

External trace and delivery record:

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
Trace project key: kronika
Trace logical-whole projection identity: kronika-public-identity-and-clean-start
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 09_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 09_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Mandatory reading (verified task-relevant anchors)

- `.ap/AP_WORKER.md` and the WORKER row of the `.ap/AP.md` minimum-reading
  spine.
- `.ap/AP.md`: [Acceptance, Correction, and Escalation], [§5 Task Authority],
  [§10 Security Boundaries], [§12 Validation and Public Verification],
  [§18 Stopping Conditions], [RF-05], [RF-07], [RF-12], [RF-18].
- `.ap/INFOSEC.md` §3 risk routing, §4.3, §6, §7, §8, §9, §14, §15, §17.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Acceptance and Correction
  Record; Security Finding and Audit contracts.
- `AGENTS.md` declared execution route, which this grant binds as the canonical
  capability path. Equivalent ambient commands are not a second route.

## Candidate and repository gate (read-only, before any probe)

Working directory: `/home/agile/Tools/cli_chatgpt`. Prove independently and
record exact values:

```text
pwd -P == /home/agile/Tools/cli_chatgpt
branch == main
HEAD == 66c40d43c577276b0ad304a494fbbb1ffb6fc933
main == public/kronika-initial == 66c40d43c577276b0ad304a494fbbb1ffb6fc933
git rev-list --count main == 1
git rev-list --parents -n 1 main == 66c40d43c577276b0ad304a494fbbb1ffb6fc933
main^{tree} == 848f247434deea4c217170c012612b39e41557f3
work/kronika-clean-start == 30e02a327e63255e1a02ec8c0709c15b38988191
  with the same tree 848f247434deea4c217170c012612b39e41557f3
previous root 827dae85c2794914c3adcb467de9b21ee8998463 is superseded
  (main@{1} in the reflog)
git merge-base --is-ancestor 2727451d2502925377637e19fa435917c970a996 main -> exit 1
lab/cli-chatgpt-190 == 2727451d2502925377637e19fa435917c970a996, count 190
no remotes
clean index and worktree
HEAD:.ap == .ap HEAD == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

If any value differs, stop `BLOCKED` and report the exact difference. Do not
repair, switch, reset, clean, stash, or recreate anything.

## Risk claims (fixed; accept or refute each)

1. **Provenance.** Local `main` is one parentless commit whose tree equals the
   corrected preparation-branch tree; the lab tip is not an ancestor; the
   previous root `827dae85` is superseded and retained only in the reflog and
   Meta evidence; `lab/cli-chatgpt-190` is preserved at `2727451` with exactly
   190 commits; `public/kronika-initial` and `work/kronika-clean-start` are
   preserved; no remote exists and nothing was pushed.
2. **A1-F01 corrected.** The canonical message
   `file upload is not available in this build` appears in the CLI `ask`
   description, the `--file` help, the CLI rejection, the bridge 501 message,
   the engine message and comment, the runner message, and the
   `GET /v1/files/{fid}` contract entry; the contract status list is
   `[401, 404, 501]` with the error envelope and no `200`/raw-byte response;
   no `until S2` / `implemented in S2` / `arrives in S2` text remains; runtime
   behavior is unchanged: CLI exit 2, HTTP 501, engine `E_UPLOAD_FAILED`.
3. **Private material absent.** The five retired documents, the three
   diagnostics/recovery schemas, `tools/obscura-patches/**`, the old package
   and wrapper paths are absent from the tree; no real host path, credential,
   token, or private household value is present.
4. **Documentation accuracy.** README order and shipped-versus-planned labels
   match the accepted contract; every documented CLI command exists; the
   declared route works; no current operator document advertises a removed
   command or endpoint; documented security boundaries match code.
5. **Security boundaries.** Bridge and manager bind loopback only; per-install
   token; strict Host/Origin; no wildcard CORS; sanitized pages with no
   JavaScript and no external resources; 0700/0600 state; capture does not read
   cookies, storage, other tabs, or history; no external LLM API; no
   recovery-provider loop; file upload unavailable.
6. **State boundary.** The application uses a fresh `kronika` XDG state
   directory; synthetic predecessor `chatgpt-cli` state is untouched; no
   migration, copy, symlink, or fallback exists.
7. **Chromium process boundary.** The probe admits Chromium only; `--engine
   obscura` and `--engine-path` are rejected before profile or process access;
   no host engine install is required or touched; profile and screenshot
   privacy holds.
8. **Local authentication.** Local accounts use salted scrypt hashes and the
   session cookie; manager pages enforce account scope; the bridge render key
   is an installation capability separate from account authorization.

## Control matrix (fixed; run each positive and negative control)

Positive controls:

- Declared route on the candidate: `bash scripts/dev-setup.sh` then
  `python -m unittest discover -s tests -t .` with `.venv` Python; report the
  exact count, result, and any skip.
- Synthetic bridge probes through the existing test harnesses (no live
  account): authenticated unknown-route 404 for the removed endpoints,
  unauthenticated rejection, upload 501 with the corrected message, wrong
  render key 404, manager session enforcement.
- Synthetic state probes under one declared temporary directory: `kronika`
  state creation with 0700/0600; a synthetic predecessor `chatgpt-cli`
  directory remains byte-for-byte untouched.
- Synthetic probe-admission checks: `--engine obscura` and `--engine-path`
  rejected before profile creation; `E_PROBE_CHROME_MISSING` before process
  start.
- Documentation spot checks: sample at least five README/SECURITY/usage claims
  and bind each to its code or contract source; verify each shown CLI command
  exists in `python -m kronika --help`.
- Git provenance: the parentless, tree-equality, no-ancestry, lab-count, ref,
  pin, and managed-block checks above.

Negative controls:

- `git grep` for the retired paths and the old upload wording in the
  candidate; confirm they are absent from current surfaces.
- Privacy scan with filename-only output:

  ```bash
  git grep -I -l -E \
      '/home/|/Users/|[A-Za-z]:\\Users\\|BEGIN [A-Z ]*PRIVATE KEY|https://chatgpt\.com/g/g-p-' \
      HEAD -- . ':(exclude).ap'
  ```

  Classify each match as a synthetic fixture or intentional example without
  printing private values.
- Confirm `git status --porcelain` is empty after all probes and that no Git
  ref moved; clean the declared temporary probe directory and report the
  cleanup outcome.
- Confirm the candidate tree contains no tracked virtual environment, cache,
  database, profile, export, or temporary evidence.

## Audit route and coverage (INFOSEC R4, correction re-acceptance)

This is the full fresh re-acceptance after the A1-F01 correction. Re-verify
all eight claims independently; the correction delta is the emphasis, not a
scope reduction. Produce a coverage map: what was selected, what was excluded,
and why. Review `.ap` only for pin and integration identity.

Findings follow the INFOSEC finding record with severity and confidence.
Report the previously parked observation honestly: the four quiet-stderr tests
in `tests/unit/test_client.py` depend on `logging.basicConfig` having been
installed by an earlier module; they fail in a focused module set that omits
`tests.unit.test_bridge_startup`, and the Orchestrator explicitly parked this
as an out-of-scope test-isolation observation. Verify that the declared full
route and the corrected focused command pass; do not fix anything.

Do not correct anything; a blocking finding is reported and routes to a
separate correction grant and re-acceptance.

## Authority

Positive: read-only inspection of the candidate tree and Git objects; the
declared test route; bounded synthetic probes; one declared temporary probe
directory outside the repository; the terminal report write.

Negative: no tracked-file edits; no Git ref, index, commit, branch, or config
writes; no fetch, push, or remote; no network; no live accounts or credentials;
no real browser profiles; no host changes; no corrections; no dependency or
toolchain changes; no `.venv` edits beyond what the declared route itself
writes (untracked).

If a required capability is unavailable, stop that control and report the
limitation; never convert missing evidence into PASS.

## Report contract

Write the terminal report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/09_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 09, exchange 01). Include:

- status `PASS`, `PARTIAL`, or `BLOCKED`, and `Phase-qualified result:
  acceptance-PASS` only when every fixed risk claim is verified;
- the candidate identity and the Acceptance and Correction Record values;
- per-claim verdicts with evidence for all eight risk claims;
- the full control matrix results, including the suite count and skips;
- the correction-delta verification (message locations, contract entry, test
  assertions, runtime behavior);
- the audit coverage map with selected and excluded surfaces and reasons;
- findings with severity and confidence, or `none`;
- residual risks and limitations, including the parked test-isolation
  observation;
- the privacy-scan classification and cleanup outcome;
- confirmation that no ref moved and the worktree is clean; and

```text
Logical-whole closure: not-closed
```

A `PASS` means the corrected candidate is independently accepted as the exact
public root; publication remains a separate Cooperator-owned grant. A blocking
finding keeps the whole open and routes to a bounded correction grant, then a
proportionate fresh re-acceptance. Then stop.
