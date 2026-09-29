# Kronika one product — worker-gate Darwin agent: focused independent re-audit

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 43
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-WORKER-GATE-DARWIN-AGENT-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — independent focused audit of a security-sensitive operator gate with a strict Darwin trust rule; the Cooperator may override.
Recommended context capacity: approximately 150k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct the
worker-gate change and inherits no implementation reasoning. Declare your
actual independence posture. Prior plans, reports and trace artifacts are
evidence, not authority. You do not correct anything: findings are reported,
never fixed. No subagents. The client must be write-capable (Plan mode OFF)
for report persistence. This is a focused audit: do not run the broad suite,
do not re-run the predecessor's lists, and never re-run an unchanged gate.

## Acceptance record

```text
Acceptance candidate: 665a565bc1279690ce8dacade37103fa3e0aaddc
  (tree 043b811cf82b54cff05026a90b3b15ee46609475, branch feat/kronika-one-product,
   parent 0d0d8c88bf88bf8454751a0205bc8652374796c2)
Acceptance owner map: the correction delta 0d0d8c8..665a565 (five paths below);
  correction grant/report 42_correction_00.md and 42_report_00.md; the blocking
  predecessor 41_report_00.md; gate source and docs in the diff
Acceptance allowlist: read-only review of the candidate, governing AP and named
  evidence; the declared focused route; direct bounded gate invocations; one
  declared temporary probe root under /tmp/kronika-one-product-gate-reaudit
  (mode 0700, synthetic data only)
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: the fixed controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: the live production Darwin probe (claim 3)
Out-of-scope observations: ledger-candidates
```

## Starting state (verified read-only at issuance, 2026-09-28)

- FrameNest checkout `/Users/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `665a565bc1279690ce8dacade37103fa3e0aaddc`, parent
  `0d0d8c88bf88bf8454751a0205bc8652374796c2`, tree
  `043b811cf82b54cff05026a90b3b15ee46609475`, subject
  `fix(operator): discover the macOS launchd ssh agent in the worker gate`;
  clean index and worktree; nothing pushed (local branch is three commits
  ahead of the public feature branch; public `main` is `0d0d8c8…`).
- AP pin `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (gitlink and `.ap` HEAD).
- Correction diff: five paths —
  `scripts/operator/network/framenest_nuc_worker_gate.fish`,
  `scripts/operator/network/README.md`,
  `tests/contract/test_operator_network_scripts.py`,
  `docs/OPERATOR_NETWORK.md`, `docs/WORKER_EXECUTION_CONTRACT.md`.
- Blocking context: `41_report_00.md` recorded `ssh-agent: absent` from the
  gate probe on this MacBook because no `gpgconf` exists while the native
  launchd `ssh-agent` holds the key.
- `private/**` is never read. No host, NUC, SSH session, sudo, service,
  browser, provider or credential action. Never print the socket value, key
  list, hostnames, addresses or other private values.

Required reading: governing WORKER spine; RF-05, RF-07; the Worker Report
Header and Acceptance record in `.ap/PROMPT_CONTRACTS.md`;
`.ap/INFOSEC.md` (R3 route, sections 3 and 4.2/4.4–4.7, finding, containment
and residual-risk rules); `42_correction_00.md` and `42_report_00.md`;
`41_report_00.md`; `docs/OPERATOR_NETWORK.md`; the gate source.

## Fixed claims

1. **Candidate identity and containment.** SHA, parent, tree, subject and the
   five-path `git diff --name-status 0d0d8c8… HEAD` match; no path outside the
   correction allowlist; `.ap`, `AGENTS.md`, packaging, migration history and
   the AP ledger are untouched; the worktree is clean and nothing was pushed;
   the AP pin is unchanged; the diff prints no socket value or key list, adds
   no production dependency on any `FRAMENEST_NETWORK_TEST_*` value, and
   introduces no new dependency. A leak hunt over the diff finds no credential
   or secret-shaped value.
2. **Discovery order and trust rule (code-level).** Read the gate source and
   confirm: trusted `gpgconf` is tried first and is unchanged; a present
   `gpgconf` that yields no usable socket does not fall through to the
   fallback; the fallback activates only when `gpgconf` is absent and the
   trusted-path `uname -s` is exactly `Darwin`; the accepted socket must be
   nonempty, absolute, contain no `..` segment, be a Unix socket, be owned by
   the invoking effective user, and resolve under
   `/private/var/run/com.apple.launchd.` with a nonempty remainder;
   `ssh-add -l` liveness accepts exit 0 or 1 and refuses anything else with
   output discarded; socket mode is not required; success exports the
   validated socket to the SSH child; `--probe` output remains exactly
   `ssh-agent: ready` (exit 0) or `ssh-agent: absent` (exit 1); Linux with
   `gpgconf` missing stays `absent`.
3. **End-to-end production probe (named missing evidence).** From the
   repository root, with `FRAMENEST_NETWORK_TEST_HOOKS` unset, run
   `./scripts/operator/network/framenest_nuc_worker_gate.fish --probe`
   directly (not through `ap exec`, whose envelope strips `SSH_AUTH_SOCK`).
   Expected: exactly `ssh-agent: ready`, exit 0, no other output, no socket
   value. This probe opens no SSH session. If the environment lacks
   `SSH_AUTH_SOCK`, report that exact environment fact (names only) and
   classify it as an environment limitation rather than a silent PASS or a
   candidate defect.
4. **Negative production behavior.** Under the declared probe root, create a
   regular file and run the same probe with `env SSH_AUTH_SOCK=<that file>`;
   also run it with `SSH_AUTH_SOCK` unset. Each must print exactly
   `ssh-agent: absent`, exit 1, with no other output and no echo of the
   synthetic path.
5. **Targeted contract suite.** Through the declared route,

   ```text
   ./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 665a565bc1279690ce8dacade37103fa3e0aaddc --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider
   ```

   exits 0 (the correction reports `60 passed`). Confirm the new causal tests
   exist and assert the specified positive and negative cases, and that the
   parameterized missing-value test isolates the ambient `FRAMENEST_NUC_SSH_*`
   names for the invoked gate process while production behavior for present
   values is unchanged.
6. **Non-weakening and documentation truthfulness.** The SSH child options
   (`BatchMode`, `StrictHostKeyChecking=yes`, `IdentitiesOnly=yes`,
   `ClearAllForwardings=yes`, timeouts), loader unsets and sanitized PATH are
   unchanged; no parallel SSH or agent stack was introduced; the docs describe
   the discovery order and validation truthfully and contain no private value.

## Fixed controls

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status 0d0d8c88bf88bf8454751a0205bc8652374796c2 HEAD
git status --porcelain --untracked-files=all
git log --oneline -3

./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 665a565bc1279690ce8dacade37103fa3e0aaddc

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 665a565bc1279690ce8dacade37103fa3e0aaddc --operation test-focus -- tests/contract/test_operator_network_scripts.py -q -p no:cacheprovider

./scripts/operator/network/framenest_nuc_worker_gate.fish --probe

env SSH_AUTH_SOCK=<synthetic regular file under the declared probe root> ./scripts/operator/network/framenest_nuc_worker_gate.fish --probe

env -u SSH_AUTH_SOCK ./scripts/operator/network/framenest_nuc_worker_gate.fish --probe
```

State every observed result with exact evidence; unverified controls are
reported as unverified, never as PASS. Findings use the full INFOSEC finding
structure (evidence class, reachability, preconditions, privilege, impact,
containment, residual risk).

## Authority and containment

Positive authority: read-only inspection of the candidate, governing `.ap` and
the named trace evidence; the declared focused route; direct bounded
invocations of the gate probe and its documented environment overrides;
creation, use and cleanup of one declared temporary probe root under `/tmp`
(mode 0700, synthetic data only); the terminal report write at the exact
destination when absent, with full readback.

Negative authority: no product, test, documentation, configuration, AP,
packaging or migration edit; no correction; no NUC contact, no SSH session, no
`sudo`, no host service, browser, provider or credential action; no push; no
new dependency; no subagent; no `private/**`; no Meta commit.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity, candidate or git-state mismatch;
an unusable declared route; a probe exceeding the authorized effects; sensitive
output; or a required control that cannot be established without a forbidden
mutation. Preserve the first causal failure; missing evidence is never PASS.

## Evidence selection

```text
Evidence tier: E3
Evidence tier basis: security/trust boundary (worker agent-socket selection for the NUC gate); live production probe plus simulated negative cases
Activated stricter profile: INFOSEC.md — R3 route (fresh focused audit)
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/contract/test_operator_network_scripts.py
Affected tests: the five-path correction delta
New causal regression: none — this is acceptance
Broad or full suite: not-used — do not run
Runtime or testbed: declared route plus direct gate probes under the declared synthetic root; no NUC
Independent acceptance: required-separate-fresh-worker (this exchange)
```

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a PASS;
otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: final-acceptance`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 43, exchange 01) exactly once. Include the
compact core; the completed acceptance record; per-claim verdicts with exact
evidence; the control matrix with observed counts and exit codes; findings with
the full structure; containment and probe cleanup; residual risk and
limitations; one smallest next step (a separate Cooperator publication grant
for the accepted corrected candidate, then the renewed NUC deployment grant);
the critique block; and the authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. If the report write is blocked by the client,
preserve the complete content in the client output and report the missing
delivery truthfully. Terminal report or cancellation expires this authority.

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
Downloadable prompt filename: 43_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 43_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
