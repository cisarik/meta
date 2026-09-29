# Kronika one product — worker-gate F01: scoped independent re-audit

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 45
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-WORKER-GATE-F01-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — scoped independent closure audit of a low-severity security finding with a live production non-regression probe; the Cooperator may override.
Recommended context capacity: approximately 120k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

Genuinely fresh session that did not implement or correct the worker-gate change
and inherits no implementation reasoning. Prior reports are evidence, not
authority. You do not correct anything. No subagents. Write-capable client,
Plan mode OFF. This is a scoped audit: only the controls and claims below; no
broad suite, no re-run of the full claim set from `43_report_00.md`.

## Acceptance record

```text
Acceptance candidate: 89a402981a9eac83646199c77984c3fc21c0744d
  (tree 27cf6ba02e9c08f27151976aa2b259bea0d60dcb, branch feat/kronika-one-product,
   parent 665a565bc1279690ce8dacade37103fa3e0aaddc)
Acceptance owner map: the F01 correction delta 665a565..89a4029 (two paths);
  correction grant/report 44_correction_00.md and 44_report_00.md; finding
  KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT-REAUDIT-F01 in 43_report_00.md
Acceptance allowlist: read-only review of the candidate, governing AP and named
  evidence; the declared focused route; direct bounded gate invocations; one
  declared temporary probe root under /tmp/kronika-one-product-gate-f01-reaudit
  (mode 0700, synthetic data only)
Acceptance risk claims: the five fixed claims below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1 (the F01 correction under audit)
Correction re-acceptance: scoped
Named missing-evidence probe: live production probe non-regression (claim 5)
Out-of-scope observations: ledger-candidates
```

## Starting state (verified read-only at issuance, 2026-09-28)

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     89a402981a9eac83646199c77984c3fc21c0744d
parent   665a565bc1279690ce8dacade37103fa3e0aaddc
tree     27cf6ba02e9c08f27151976aa2b259bea0d60dcb
subject  fix(operator): follow symlinks in the gate agent ownership check
status   empty (git status --porcelain --untracked-files=all)
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
public   main 0d0d8c8…; feature branch 38e7bee…
```

Correction diff: exactly
`scripts/operator/network/framenest_nuc_worker_gate.fish` and
`tests/contract/test_operator_network_scripts.py`; 34 insertions, 1 deletion.
Line 192 of the gate changes from `$stat_bin -f %u "$sock"` (parent) to
`$stat_bin -L -f %u "$sock"` (candidate).

`private/**` is never read. No NUC contact, no SSH session, no sudo, no host
service, browser, provider or credential action. Never print the socket value,
key list, hostnames, addresses or other private values.

Required reading: governing WORKER spine; RF-05, RF-07;
`.ap/INFOSEC.md` (R3 route); `43_report_00.md` (finding F01); the correction
grant/report `44_correction_00.md` and `44_report_00.md`; the candidate diff
and gate source.

## Fixed claims

1. **Candidate identity and containment.** SHA, parent, tree and subject match;
   `git diff --name-status 665a565… HEAD` is exactly the two named paths; no
   protected path changed; the worktree is clean; nothing was pushed; the AP
   pin is unchanged; a leak hunt over the small diff finds no private value.
2. **F01 closed (code-level and causal).** The candidate's Darwin ownership
   comparison follows the final symlink and compares the socket inode's uid
   (`stat -L -f %u`), while the parent at the same location lacks `-L`; no
   other trust check changed. The regression
   `test_ssh_gate_darwin_ownership_follows_final_symlink` exists, asserts the
   follow-mode ownership read, and could not pass on the parent.
3. **No other behavior change.** Diff review confirms the gate change is the
   single ownership-line change; every other check, the `--probe` output
   contract, the hook branch, the SSH options, loader unsets and sanitized PATH
   are unchanged; the docs were not touched and remain truthful.
4. **Targeted suite non-regression.** Through the declared route,

   ```text
   ./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 89a402981a9eac83646199c77984c3fc21c0744d --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider
   ```

   exits 0 (the correction reports `61 passed`).
5. **Live production non-regression.** From the repository root with
   `FRAMENEST_NETWORK_TEST_HOOKS` unset:
   `./scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
   exactly `ssh-agent: ready`, exit 0; and with a synthetic regular file under
   the declared probe root as `SSH_AUTH_SOCK`, the same probe prints exactly
   `ssh-agent: absent`, exit 1, without echoing the path. The probe opens no
   SSH session.

## Fixed controls

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status 665a565bc1279690ce8dacade37103fa3e0aaddc HEAD
git show 665a565bc1279690ce8dacade37103fa3e0aaddc:scripts/operator/network/framenest_nuc_worker_gate.fish
git status --porcelain --untracked-files=all

./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 89a402981a9eac83646199c77984c3fc21c0744d

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 89a402981a9eac83646199c77984c3fc21c0744d --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider

./scripts/operator/network/framenest_nuc_worker_gate.fish --probe

env SSH_AUTH_SOCK=<synthetic regular file under the declared probe root> ./scripts/operator/network/framenest_nuc_worker_gate.fish --probe
```

Findings use the full INFOSEC finding structure; unverified controls are never
PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate, governing `.ap` and
the named evidence; the declared focused route; direct bounded gate probe
invocations; one declared temporary probe root under `/tmp` (0700, synthetic);
the terminal report write.

Negative authority: no product, test, documentation, configuration, AP,
packaging or migration edit; no correction; no NUC contact, SSH session, sudo,
host service, browser, provider or credential action; no push; no subagent;
no `private/**`; no Meta commit.

## Stopping conditions

Stop with `PARTIAL`/`BLOCKED` on identity or git-state mismatch, an unusable
route, a probe exceeding authorized effects, sensitive output, or a control
that cannot be established without a forbidden mutation. Missing evidence is
never PASS.

## Evidence selection

```text
Evidence tier: E3
Evidence tier basis: security/trust boundary (agent-socket ownership check); scoped closure audit with live production probe
Activated stricter profile: INFOSEC.md — R3 route
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/contract/test_operator_network_scripts.py
Affected tests: the two-path correction delta
New causal regression: none — this is acceptance
Broad or full suite: not-used — do not run
Runtime or testbed: declared route plus direct gate probes under the declared synthetic root; no NUC
Independent acceptance: required-separate-fresh-worker (this exchange)
```

## Completion and report contract

`PASS` means all five claims are independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a PASS;
otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: final-acceptance`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 45, exchange 01) exactly once. Include the
completed acceptance record; per-claim verdicts with exact evidence; the
control matrix with counts and exit codes; any finding with the full structure;
containment and cleanup; residual risk; one smallest next step (a separate
Cooperator publication grant for the accepted corrected candidate, then the
renewed NUC deployment grant); the critique block; and the authority-expiry
statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Terminal report or cancellation expires this
authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 45_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 45_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
