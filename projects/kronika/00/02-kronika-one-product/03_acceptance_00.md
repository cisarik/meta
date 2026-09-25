# Kronika one product — S2 full fresh independent re-acceptance

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S2-REACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full fresh re-audit of the corrected lifecycle/wire candidate with adversarial re-verification of three closed findings; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement S2 and did not
participate in the correction. Declare your actual independence posture in the
report. The plan, both reports and the first acceptance report are evidence;
inherited implementation or correction reasoning is disqualifying. You do not
correct the candidate; findings are reported, never fixed here.

## Acceptance and Correction Record

```text
Acceptance candidate: 82a6a59803ed8830c19e51cd8f9bc1665c28a975
  (tree 190338dde238c414cf4e80999b29b18797d4f72d, branch feat/kronika-one-product,
   parent 5259b89a9af993e94f00c03e7962681c8ba152a4)
Acceptance owner map: the S2 implementation delta (20 paths, 96ef426..5259b89) plus
  the correction delta (12 paths, 5259b89..candidate); accepted plan 01_report_00.md
  sections 4.1-4.6 S2 subset; S2 report 01_report_03.md; first acceptance
  02_report_00.md; correction report 01_report_04.md
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused routes; synthetic temporary probe state under one declared temporary root
Acceptance risk claims: the eight original claims below plus the three finding-closure
  claims, with the recorded vocabulary scope
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, parent
  `5259b89a9af993e94f00c03e7962681c8ba152a4`, tree
  `190338dde238c414cf4e80999b29b18797d4f72d`, subject
  `fix(capture): correct queued waits and oversized result delivery`; clean
  index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved); no remote branch for
  `feat/kronika-one-product`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Kronika source checkout clean at
  `66c40d43c577276b0ad304a494fbbb1ffb6fc933`; read-only.
- `private/**` contains key material and is never read.

## Goal

Establish whether the corrected candidate fully satisfies the accepted S2
contract: the eight original risk claims, the closure of findings F01, F02 and
F03 from the first acceptance, and the recorded error-vocabulary scope; and
whether the correction weakened any S2 guarantee. This is the one full fresh
correction re-acceptance of this slice. It is not a broad whole-product audit
and grants no S3 authority.

## Fixed risk claims

1. **Browser lifecycle.** One browser process and one owned page across
   ordinary jobs; bridge outage reconnects with capped backoff and never shuts
   the browser down; browser crash blocks readiness with no automatic restart;
   the launch brake enforces at least 300 seconds, rejects backward/
   unverifiable time and does not reclaim a stale lock automatically.
2. **No automatic resend.** Durable single-use send intent before any click;
   no second-click retry; click/confirmation uncertainty, lost association,
   recovery and cancellation/timeout never resend; ambiguous paths end in
   `E_AMBIGUOUS_SEND`.
3. **Journal durability and idempotency.** Admission committed before the
   protocol acknowledgement; identical requests return the original job;
   changed content under one identity returns `E_IDEMPOTENCY_CONFLICT`; 24-hour
   and 256-entry retention without early eviction; recovery reconciliation with
   writer lock and epoch/offer fencing.
4. **Readiness and administration, including F01 closure.** Structural
   readiness only; `needs_admin` retains the single active slot for admitted
   jobs including never-offered queued jobs; administrator waiting is durably
   accounted and excluded from the active-response deadline with an exact
   cumulative 1,800-second limit; explicit resume re-runs readiness before any
   continuation; no send while readiness is blocked; recovery preserves the
   queued phase and fences old epochs.
5. **Authenticated wire, including F03 closure.** Loopback bind; per-install
   token on content/readiness endpoints; exact Host; only an absent or exact
   approved loopback Origin is accepted — a present empty Origin is rejected;
   constant-time comparison; no wildcard CORS; health liveness/protocol only;
   operational status/events expose no prompt, answer, title, source URL or
   staging path.
6. **No profile or credential access.** No `DevToolsActivePort` read; bounded
   in-memory stderr endpoint parsing (at most 64 KiB, bounded lines, loopback
   match); no stealth, no sandbox weakening, no cookie/credential/profile
   content access; unrelated browser stderr not logged.
7. **Typed failures with the reconciled vocabulary, including F02 closure.**
   All S2 codes and HTTP mapping present; an oversized complete result produces
   exactly one engine execution and a durable typed `E_RESULT_TOO_LARGE`
   terminal failure readable through authenticated status; the rejected
   oversized payload is never retried and no second execution occurs;
   `E_ATTACHMENT_INVALID` is deferred to S5 and `E_RESULT_EXPIRED` to the
   application-recovery slice — do not treat that binding deferral as a defect.
8. **Packaging and protected paths.** Wheel contains all 33 capture files with
   both entry points resolving to the same callable; provenance covers exactly
   the 32 upstream-relocated files; `src/framenest/**`, `.ap`, `.gitmodules`,
   `AGENTS.md` (including the managed block), `ap.project.conf`, the upgrade
   ledger, all documentation, `poetry.lock` and `pyproject.toml` unchanged; AP
   pin unchanged.

## Fixed control matrix

Positive controls (run independently from the repository root; report the
counts you actually observe):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 82a6a59803ed8830c19e51cd8f9bc1665c28a975

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 82a6a59803ed8830c19e51cd8f9bc1665c28a975 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

```text
node --test tests/capture_lifecycle.test.js tests/chatgpt_page_protocol.test.js
```

Negative and adversarial controls (bounded synthetic probes under one declared
temporary root, e.g. `/tmp/kronika-one-product-s2-reacceptance`, mode 0700,
cleaned up by you; independently reproduce rather than trusting the reports):

- **F01 reproduction.** The first acceptance's queued-intervention probe
  (synthetic clock: admitted job, timeout 10 s, readiness loss at t=2, watchdog
  at t=10) must now retain the job and slot, exclude the wait, and require a
  successful explicit resume; verify the exact cumulative 1,800-second expiry
  and recovery/epoch fencing.
- **F02 reproduction.** An oversized complete result (including Unicode and
  envelope-overhead cases, exact-limit and one-byte-over) through the real
  loopback bridge with a fake engine: one engine execution, durable
  `E_RESULT_TOO_LARGE`, authenticated HTTP 200 status read, no repeated
  oversized payload, no successful re-execution.
- **F03 reproduction.** Origin matrix: absent, present-empty, exact, literal
  `null`, foreign — with and without token; wildcard CORS absent everywhere.
- **Double-send hunt.** Re-trace every click path and run at least one
  adversarial probe per submission boundary; confirm no path can click twice or
  acknowledge unpersisted work.
- **Journal and retention.** Admission before acknowledgement, replay/conflict,
  256-entry refusal without early eviction, 24-hour boundary, backward clock.
- **Launch brake and readiness.** 299,999 ms refused, exactly 300,000 ms
  allowed, backward/NaN/stale-lock refusal, no automatic relaunch, no profile
  read.
- **Privacy.** Operational status/events carry no prompt, answer, title, source
  URL or staging path.

State the exact observed result for every control. Unverified controls are
reported as unverified, never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate tree and governing
`.ap`; the three declared route commands; creation, use and cleanup of one
declared temporary probe root under `/tmp` (mode 0700, synthetic data only);
and creation of the terminal report. The report write is the only durable
repository-external write.

Commands: bounded read-only inspection; `rg` with private-value-safe output;
read-only Git queries; the declared `./.ap/ap` route; `node --test`/`node
--check`; bounded synthetic probe scripts and loopback HTTP/SQLite probes inside
the temporary root; the native file writer for the report only.

Git authority: read-only. No fetch, branch, switch, stage, commit, push,
remote, reset, clean, stash or config write. Network: loopback synthetic probes
only. Dependency: none. Secrets: none; never read `private/**`, cookies,
tokens, profiles or credentials.

Negative authority: no code, test, documentation, AP, packaging or
configuration edit; no correction of any finding; no push or publication; no
host, NUC, browser or provider execution; no new toolchain; no subagent; no
Meta commit. Stop on any needed forbidden effect.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a required
route that cannot run; a probe exceeding the authorized effects; sensitive
output; or a required control that cannot be established without a forbidden
mutation. Preserve the first causal failure and report the exact missing
evidence. A finding is reported, never corrected. If a new material finding
appears, report it; do not generate a second correction cycle yourself.

## Evidence selection and report delivery

Evidence tier: E3
Evidence tier basis: full fresh independent re-acceptance of a corrected
trust-boundary lifecycle slice with adversarial re-verification
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route and Node suites
Affected tests: the S2 implementation and correction tests
New causal regression: none — this is re-acceptance, not implementation
Broad or full suite: not-used
Runtime or testbed: declared route plus synthetic temporary probes; no real browser
Independent acceptance: required-separate-fresh-worker (this exchange)

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Completion and report contract

`PASS` means every fixed claim and all three finding-closure claims are
independently established with the stated evidence and no blocking finding
remains. `PARTIAL` means useful evidence exists but a claim remains unverified.
`BLOCKED` means the review cannot proceed safely. Use
`Phase-qualified result: acceptance-PASS` only for a PASS. Logical-whole
closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include: the compact core; the
completed Acceptance and Correction Record; per-claim verdicts; explicit F01,
F02 and F03 closure verdicts with the reproduction evidence; the full control
matrix results with your independently observed test counts; adversarial probe
outcomes; findings if any (with the full finding structure used by the
predecessor acceptance reports); the containment ledger and cleanup outcome;
residual risk and limitations; one smallest next step; `Report justification:
final-acceptance` (or `new-evidence` for PARTIAL); authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts. Finalize the
report, save it at the exact destination only if absent, read it back in full,
verify its first line/coordinates/content/path, then send the short separate
completion notice with status, exact path and SHA-256. Terminal report or
cancellation expires this authority.
