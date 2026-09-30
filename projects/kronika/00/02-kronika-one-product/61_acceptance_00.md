# S9-P3-F01 Scoped Fresh Verification — Automatic cleanup correction (kronika-one-product, session 61)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 61
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S9-P3-F01-VERIFY
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — independent scoped verification of a provider-boundary behavior correction
Recommended context capacity: approximately 250k tokens
Independence required: yes

## Acceptance and Correction Record

```text
Acceptance candidate: 3bf424586289b500cf45cb0d49676b50d27328fa
  (tree ee39cdee4cd35d25f39586f681844d9753481a4a, branch feat/kronika-one-product,
   parent a3687505eb12359c76f85661e51e36d7e4778fc9)
Acceptance owner map: delta a3687505eb12359c76f85661e51e36d7e4778fc9..3bf424586289b500cf45cb0d49676b50d27328fa
  (one commit, 2 paths); 60_correction_00.md and 60_report_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused route; no
  temporary root is required and none is granted; no mutation
Acceptance risk claims: V1–V5 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: scoped
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

This session did not implement or correct the audited change. The correction
report is a claim; verify it. No correction authority is granted.

## Verified claims and required verdicts

**V1 — Candidate identity and containment.** HEAD `3bf4245…`, tree
`ee39cdee…`, parent `a368750…`, branch clean including untracked files; the
delta is exactly the two allowlisted paths
(`src/framenest/adapters/api/research_api.py`,
`tests/contract/test_research_requests_api.py`); no push (public `main` and
feature branch still `a368750…`); AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`; no other behavior-bearing file
changed.

**V2 — Correction shape.** Both research API nudge blocks now call
`runtime.release_remote_pending()` inside their pre-existing
`try/except Exception: pass` guards (POST successful-admission path after
`submit_pending()`; GET detail after `submit_pending()/poll_once()`); the
disabled/absent-runtime path is unchanged; no response-shape, status-code,
capability, admission, polling, cancel or loop-bound change is present in the
diff.

**V3 — Causal evidence.** Independently run the focused route on the corrected
candidate and record the totals:
`tests/contract/test_research_requests_api.py`,
`tests/contract/test_research_completion.py`,
`tests/unit/application/test_research_coordinator.py`, plus
`./.ap/ap project check` with baseline `3bf4245…`. Independently inspect the
new regression `test_nudge_releases_remote_after_validated_save` and confirm
from the code and the parent diff that it is causal for the missing cleanup
(on the parent the nudge leaves the terminal row `pending` and records no
release; after the correction the row becomes `deleted` with exactly one
recorded release). An independent synthetic probe through the API harness is
welcome but must stay within the repository's test code — do not create new
files outside the traced candidate; do not mutate the repository.

**V4 — No live side effects.** No provider call was made (tests use fake
transports); no credential or secret read; no NUC/SSH/sudo; repository clean
after the run; the correction does not enable research or change budgets.

**V5 — Finding disposition.** State the verdict for
`KRONIKA-ONE-PRODUCT-S9-P3-F01` (`verified-closed` only if V1–V4 are
established on the corrected candidate; otherwise `not accepted` with the
evidence). Out-of-scope observations become non-authorizing ledger candidates.

## Controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}' HEAD^; git status --porcelain --untracked-files=all
git diff --name-status a3687505eb12359c76f85661e51e36d7e4778fc9..HEAD; git show 3bf424586289b500cf45cb0d49676b50d27328fa
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main refs/heads/feat/kronika-one-product
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa --operation test-focus -- tests/contract/test_research_requests_api.py tests/contract/test_research_completion.py tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider
```

The broad Python suite, JS tests, browser suites, NUC access and provider calls
are not part of this verification. No dependencies, lockfiles, configuration,
migrations or AP changes.

## Report contract

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 61, 01), and includes the Acceptance
record, per-claim verdicts V1–V5 with evidence, the control matrix results,
the finding verdict, limitations, residual risk, critique and authority
expiry. Use `Phase-qualified result: acceptance-PASS | not-applicable`,
`Logical-whole closure: not-closed`, `Report justification: final-acceptance`.
Save the report exactly at `61_report_00.md` if the client permits; read back
the full content; otherwise preserve it in chat and mark delivery PARTIAL.

## Delivery record

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
Downloadable prompt filename: 61_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 61_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed gate, unseen divergence, any need to
mutate the repository, or a claim that cannot be established read-only. Do
not expand into an unknown-unknown audit.

Authority expiry: the terminal report ends this verification exchange.
