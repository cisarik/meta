Logical whole identity: kronika-public-identity-and-clean-start
Worker session ordinal: 07
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-PUBLIC-IDENTITY-CLEAN-START-A1
Native planning mode: not-used
Delivery route: manual Cooperator delivery to a genuinely fresh Worker session that did not implement or plan S1–S5
Reasoning recommendation: Extra High
Reasoning basis: the whole's primary independent acceptance (INFOSEC R4 milestone audit) across security, documentation, state-path, process-boundary, and provenance claims; Extra High is Cooperator-selected for this whole; do not use Max
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Evidence-tier basis: security-boundary and publication-candidate acceptance with a fresh independent audit; publication remains a separate Cooperator grant
Internal delegation: prohibited
Independence required: yes; required-fresh-independent
Evidence posture: independent acceptance evidence

# Kronika A1 — fresh independent acceptance of the public root

You are a genuinely fresh WORKER. You did not plan this whole and you did not
implement S1–S5. This prompt grants one bounded acceptance task: **A1 only**.
Native Plan Mode must be **OFF**. Do not use subagents. Do not continue any
previous chat.

If you took part in planning or implementing any part of this logical whole, or
if this conversation inherits that context, stop and report the conflict
instead of accepting.

You are the whole's primary independent acceptance. You do not correct
findings; you report them. Do not implement corrections, do not push, do not
add a remote, do not construct or move any ref, and do not close the logical
whole.

```text
STOP: Native Plan Mode off. This is acceptance, not planning or implementation.
STOP: A1 only. No corrections, no S1–S5 work, no publication, no P1/P2/V1.
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
Acceptance candidate: 827dae85c2794914c3adcb467de9b21ee8998463
  (tree 8506c9955b448d913cafe03c08b0c3e5495f9952, local main)
Acceptance owner map: the candidate tree's semantic owners - AGENTS.md,
  README.md, SECURITY.md, CONTRIBUTING.md, docs/**, contracts/**,
  src/kronika/**, extension/**, tests/**, .gitmodules, .ap gitlink
Acceptance allowlist: read-only review of the whole candidate tree; declared
  test route; synthetic probes and temporary probe state under one declared
  temporary directory
Acceptance risk claims: the eight fixed claims in "Risk claims" below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

Predecessor evidence (not same-session authority): the A1 section and §5 of
`01_report_00.md`, and the terminal reports `02_report_00.md` through
`06_report_00.md` in the same Meta directory. Read them as data; this prompt is
the complete new A1 grant.

Meta storage:

```text
01_planning_00.md + 01_report_00.md       session 01 / exchange 01 (Planner)
02_implementation_00.md + 02_report_00.md session 02 / exchange 01 (S1)
03_implementation_00.md + 03_report_00.md session 03 / exchange 01 (S2)
04_implementation_00.md + 04_report_00.md session 04 / exchange 01 (S3)
05_implementation_00.md + 05_report_00.md session 05 / exchange 01 (S4)
06_implementation_00.md + 06_report_00.md session 06 / exchange 01 (S5)
07_acceptance_00.md + 07_report_00.md     session 07 / exchange 01 (this A1)
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
Downloadable prompt filename: 07_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start
Report filename: 07_report_00.md
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
- `.ap/INFOSEC.md` §3 risk routing (R4), §4.3 broad milestone audit, §6
  finding record, §7 severity, §8 exploitability, §9 synthetic reproduction,
  §14 residual risk, §15 audit/correction separation, §17 report requirements.
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
HEAD == 827dae85c2794914c3adcb467de9b21ee8998463
main == 827dae85c2794914c3adcb467de9b21ee8998463
git rev-list --count main == 1
git rev-list --parents -n 1 main == 827dae85c2794914c3adcb467de9b21ee8998463
main^{tree} == 8506c9955b448d913cafe03c08b0c3e5495f9952
git merge-base --is-ancestor 2727451d2502925377637e19fa435917c970a996 main  -> exit 1
lab/cli-chatgpt-190 == 2727451d2502925377637e19fa435917c970a996, count 190
work/kronika-clean-start == b5b5f3811f62d5c83dd411c627a1783fb1bd5d93
public/kronika-initial == 827dae85c2794914c3adcb467de9b21ee8998463
no remotes
clean index and worktree
HEAD:.ap == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
.ap HEAD == 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

If any value differs, stop `BLOCKED` and report the exact difference. Do not
repair, switch, reset, clean, stash, or recreate anything.

## Risk claims (fixed; accept or refute each)

1. **Provenance.** Local `main` is one parentless commit whose tree equals the
   accepted cleaned tree; the lab tip is not an ancestor; `lab/cli-chatgpt-190`
   is preserved at `2727451` with exactly 190 commits; the preparation branch
   and `public/kronika-initial` are preserved; no remote exists and nothing was
   pushed.
2. **Private material absent.** The five retired documents, the three
   diagnostics/recovery schemas, `tools/obscura-patches/**`, the old package
   and wrapper paths are absent from the tree; no real host path, credential,
   token, or private household value is present.
3. **Documentation accuracy.** README order and shipped-versus-planned labels
   match the accepted contract; every documented CLI command exists; the
   declared route works; no current operator document advertises a removed
   command or a removed endpoint; documented security boundaries match code.
4. **Security boundaries.** Bridge and manager bind loopback only; per-install
   token; strict Host/Origin; no wildcard CORS; sanitized pages with no
   JavaScript and no external resources; 0700/0600 state; capture does not read
   cookies, storage, other tabs, or history; no external LLM API; no
   recovery-provider loop; file upload unavailable.
5. **State boundary.** The application uses a fresh `kronika` XDG state
   directory; synthetic predecessor `chatgpt-cli` state is untouched; no
   migration, copy, symlink, or fallback exists.
6. **Chromium process boundary.** The probe admits Chromium only; `--engine
   obscura` and `--engine-path` are rejected before profile or process access;
   no host engine install is required or touched; profile and screenshot
   privacy holds.
7. **Local authentication.** Local accounts use salted scrypt hashes and the
   session cookie; manager pages enforce account scope; the bridge render key
   is an installation capability separate from account authorization.
8. **AP integration identity.** The `.ap` gitlink and `.ap` HEAD both equal
   `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; `.gitmodules` and the managed
   AP block are unchanged; no AP upgrade occurred.

## Control matrix (fixed; run each positive and negative control)

Positive controls:

- Declared route on the candidate: `bash scripts/dev-setup.sh` then
  `python -m unittest discover -s tests -t .` with `.venv` Python; report the
  exact count, result, and any skip.
- Synthetic bridge probes through the existing test harnesses (no live
  account): authenticated unknown-route 404 for the removed endpoints,
  unauthenticated rejection, upload 501, wrong render key 404, manager
  session enforcement.
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

- `git grep` for the retired paths and removed command names in the candidate;
  confirm they are absent from current surfaces.
- Privacy scan with filename-only output:

  ```bash
  git grep -I -l -E \
      '/home/|/Users/|[A-Za-z]:\\Users\\|BEGIN [A-Z ]*PRIVATE KEY|https://chatgpt\.com/g/g-p-' \
      HEAD -- . ':(exclude).ap'
  ```

  Classify each match as a synthetic fixture or intentional example without
  printing private values. One known review lead: the shared contract example
  project URL and the unit-test fixture URL. Confirm they are generated
  fixtures and record the classification.
- Confirm `git status --porcelain` is empty after all probes and that no Git
  ref moved; clean the declared temporary probe directory and report the
  cleanup outcome.
- Confirm the candidate tree contains no tracked virtual environment, cache,
  database, profile, export, or temporary evidence.

## Audit route and coverage (INFOSEC R4)

Produce a milestone audit scoped by an attack-surface map: bridge HTTP surface
(auth, routing, render, manager), local authentication and session handling,
the login-wizard exception, the Chromium executor and probe, filesystem and
state handling, the documentation and publication tree, and AP integration
identity. State what was selected, what was excluded, and why. Review `.ap`
only for pin and integration identity, not as a new AP audit.

Findings follow the INFOSEC finding record: evidence class, reachability,
preconditions, required privilege, observed or potential impact, severity, and
confidence. A dangerous API or a test failure is a signal requiring
interpretation, not automatically a reachability claim. Use synthetic
containment only. Do not correct anything; a blocking finding is reported and
routes to a separate correction grant and re-acceptance.

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
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/07_report_00.md
```

only if that path is absent. The chat conclusion is a short 3-line notice with
status, path, and SHA-256. Do not commit Meta. Do not overwrite any earlier
report.

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates exactly once (session 07, exchange 01). Include:

- status `PASS`, `PARTIAL`, or `BLOCKED`, and `Phase-qualified result:
  acceptance-PASS` only when every fixed risk claim is verified;
- the candidate identity and the Acceptance and Correction Record values;
- per-claim verdicts with evidence for all eight risk claims;
- the full control matrix results, including the suite count and skips;
- the audit coverage map with selected and excluded surfaces and reasons;
- findings with severity and confidence, or `none`;
- residual risks and limitations;
- the privacy-scan classification and cleanup outcome;
- confirmation that no ref moved and the worktree is clean;
- one smallest next step or review request; and

```text
Logical-whole closure: not-closed
```

A `PASS` means the candidate is independently accepted as the exact public
root; publication remains a separate Cooperator-owned grant. A blocking
finding keeps the whole open and routes to a bounded correction grant, then a
proportionate fresh re-acceptance. Then stop.
