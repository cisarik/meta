# BookRadar — Fresh Independent Audit — Governed Review and Promotion

Persistent role identity: WORKER
Logical whole identity: bookradar-review-and-promotion-workflow
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: BOOKRADAR-REVIEW-PROMOTION-ACCEPTANCE
Delivery route: manual Cooperator delivery (prompt-file pointer)
Reasoning recommendation: High — independent acceptance of a trust-boundary change spanning two SQLite databases, append-only history, optimistic review concurrency, a new CLI, additive read APIs, UI query selection, and rendered browser evidence.
Recommended context capacity: approximately 250k tokens
Independence required: yes

Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112
Acceptance owner map: `docs/domain-contract.md` (revision 1); `docs/research-input-v1.md`; `docs/adr/0001`–`0008`; `bookradar-core` verification semantics; `crates/bookradar-store` persistence/research/promotion; `crates/bookradar-ui` read-only UI; `README.md`; `scripts/verify.sh` and `.github/workflows/verify.yml`
Acceptance allowlist: README.md, crates/bookradar-store/src/lib.rs, crates/bookradar-store/src/research.rs, crates/bookradar-store/src/promotion.rs, crates/bookradar-store/src/bin/bookradar-review.rs, crates/bookradar-store/tests/promotion.rs, crates/bookradar-store/tests/review_cli.rs, crates/bookradar-ui/src/config.rs, crates/bookradar-ui/src/snapshot.rs, crates/bookradar-ui/src/render.rs, crates/bookradar-ui/tests/cli.rs, crates/bookradar-ui/tests/render.rs, crates/bookradar-ui/tests/common/mod.rs, docs/adr/0008-governed-review-and-promotion.md
Acceptance risk claims: R1 candidate identity, ancestry, tree, local/public separation, no push; R2 exact 14-path allowlist and no core/schema/domain-contract/research-input/ADRs 0001–0007/scripts/Cargo/.ap change; R3 canonical gate `bash scripts/verify.sh` PASS with 113 tests and one-line core tree; R4 no automatic promotion of AgentOnly evidence in promotion or review; R5 complete and explicit positive reviewer attestation; R6 rejected/quarantined/replayed/unknown findings fail closed without store writes or ledger mutation; R7 one-transaction promotion with exact `research:` provenance; R8 caller-supplied id collisions fail closed and same-finding/new-observation is allowed; R9 review concurrency, time regression, equal-time conflict clearing, and disputed supersession preserve prior revisions; R10 research ledger read-only and no ledger `append_review`; R11 UI flags default 1/1, non-default selection, invalid ids exit before I/O, UI remains read-only; R12 no external dependency, no new crate, `#![forbid(unsafe_code)]`; R13 README end-to-end demo includes conflict clearing and ADR 0008 records the nine approved cells; R14 local Playwright/Chromium rendered browser verification under the Browser Stall Guard Contract; R15 independent session and no self-certification
Acceptance control matrix: C1 through C17 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-review-and-promotion-workflow
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_acceptance_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow
Report filename: 02_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/02_report_00.md

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the accepted 113-test suite at candidate `80b172c…`
Affected tests: all new promotion/review/UI tests plus the preserved 94; rerun the canonical gate
New causal regression: independent acceptance of the trust-boundary, conflict, idempotency, and UI controls
Broad or full suite: required-because ADR 0006 binds `bash scripts/verify.sh` as the canonical repository gate and this is a trust-boundary acceptance
Runtime or testbed: local loopback synthetic CLI and Playwright/Chromium browser testbed
Independent acceptance: required-separate-fresh-worker

Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes

Development envelope activation: not-used

## Independence and authority posture

You are a fresh WORKER in the `Fresh Independent Audit` profile. You did not
participate in the planning, implementation, or README correction. Your first
input for this task is this prompt. Do not read or rely on the implementing
session's conversation; read the frozen candidate, the approved plan, the
implementation and correction reports, the repository evidence, and this grant.
Independence is a required property, not a label: if you have materially
implemented this candidate or inherited the implementing session's reasoning,
stop and report `BLOCKED` rather than claim independence.

This is a read-only acceptance task with respect to the repository. Do not edit
repository files, add tests, correct defects, stage, commit, push, tag, change
branches, or rewrite history. Do not write any Meta file except the exact report
destination above. If you find a concrete defect, report it with evidence and
stop; the Orchestrator will decide a bounded correction.

The COOPERATOR has selected direct Worker report persistence. Write the complete
terminal report to the exact report path above, read it back fully, and send a
short completion notice with its SHA-256. If the client blocks the write, return
the complete report in the session and report the delivery limitation; do not
create a placeholder or write any other Meta file.

Native Plan Mode must be OFF. This prompt targets a genuinely fresh Worker
session `02`; if the selected session is not fresh, stop and report the routing
defect.

## Candidate and baseline

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Expected branch: `main`
Acceptance candidate: `80b172c2db6fcacc93041d4eb4c246450547f112`
Candidate parent: `69ec45e245108c90e2de4302c03ca72572bf1829`
Candidate tree: `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
Candidate subject: `docs: demonstrate governed conflict resolution`
Implementation commit: `69ec45e245108c90e2de4302c03ca72572bf1829`
Implementation parent/baseline: `2281982f7dae0ef1f582d294592c41281ba11b21`
Public `refs/heads/main` at audit time: still `2281982f7dae0ef1f582d294592c41281ba11b21`
Local state: `main` is two commits ahead of `origin/main`; worktree clean; no
push, tags, or extra refs
Governing AP: `.ap` gitlink and detached checkout
`d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1; `docs/research-input-v1.md`
Accepted ADRs: `docs/adr/0001`–`0008`
Verification gate: `bash scripts/verify.sh`, `.github/workflows/verify.yml`,
`README.md`, `docs/adr/0006-verification-gate-and-ci.md`

Frozen evidence to verify, not trust:

- approved plan `01_report_00.md` SHA-256
  `e08189f9534208d4f1dee91d289014d536cad88327236691a9deb8a68e9ecc22`
  (323 lines);
- implementation prompt `01_implementation_01.md` SHA-256
  `04747fbabb2d9d7973943b7be3a419fdb54af735d4eda60eb73cf86dc3957926`;
- implementation report `01_report_01.md` SHA-256
  `030f8955a7a2b116a647ed6d47489ddf59bde23483b3f6e0e0a459e21642bf8c`
  (35 lines);
- correction prompt `01_correction_02.md` SHA-256
  `2f921c3b3c945a84221d2c8de481fa577e86860a62af0338a37cbc2bef49d559`;
- correction report `01_report_02.md` SHA-256
  `f08aee0b9c4da4a1d53c5ddfd0021821db634ed5c88f8efbfef3c9daae6a8108`
  (39 lines);
- provisional handout `00_handout_00.md` SHA-256
  `ea5985ff63853098c8f2de5dc59977a30d5374acc0f812f23107e70656e997fd`;
- predecessor closure `06-bookradar-ui-shell/01_closure.md` SHA-256
  `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`.

The plan, prompts, and reports are claims/evidence, not proof. Verify the
candidate directly. If a reported fact differs from the candidate, report the
difference.

## Required reading

Read the WORKER minimum-reading spine and task-relevant anchors:

- `.ap/AP.md`: RF-02, RF-05, RF-07, RF-11, RF-12, RF-16, RF-18, RF-19; §3
  Worker Session Target; §5; §7; §8; §11 Browser and Rendered Acceptance
  Automation; §12 Validation; §13; §18 Stopping Conditions.
- `.ap/AP_WORKER.md`: Session Profile and Independence; Worker Session Target;
  Worker Exchange Coordinates and Trace Boundary; Before Mutation; Validation;
  Reporting; Stopping Conditions.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Acceptance and Correction
  Record; Worker Exchange Identity and External Trace Contract; Validation
  Ladder Record; Browser Stall Guard Contract; Amended Expectation Contract;
  Fresh Independent Audit; Cooperator Delivery and Trace Destination Record.
- Project root `AGENTS.md`, `README.md`, `.gitignore`, `Cargo.toml`,
  `Cargo.lock`, `rust-toolchain.toml`, `scripts/verify.sh`,
  `.github/workflows/verify.yml`.
- `docs/domain-contract.md` (especially *Trust and research ingestion*,
  *Verification and freshness*, *Admission, replay, and correction*, *Never
  automatically accepted*, *Personal state*), `docs/research-input-v1.md`, and
  `docs/adr/0001`–`0008`.
- `src/model.rs`, `src/verification.rs`, `tests/verification.rs`.
- `crates/bookradar-store/src/{lib,store,history,research,research_contract,fixtures,promotion}.rs`,
  both SQL schemas, `src/bin/bookradar-review.rs`, `src/bin/bookradar-poc.rs`,
  `src/bin/bookradar-research.rs`, and the store/UI tests.
- `crates/bookradar-ui/src/{config,snapshot,render,http,main}.rs` and its tests.
- The approved plan, implementation prompt/report, correction prompt/report,
  and this whole's `00_notes.md`.

## Acceptance control matrix

Record every control as PASS, FAIL, or NOT-VERIFIED with exact evidence. A FAIL
or material NOT-VERIFIED blocks `acceptance-PASS`.

**C1 — Candidate identity and public separation.** Verify HEAD equals
`80b172c…`, parent `69ec45e…`, tree `578fbe8…`, subject
`docs: demonstrate governed conflict resolution`; local `main` is two commits
ahead of `origin/main`; public `refs/heads/main` is still `2281982f…`; worktree
clean; `.ap` gitlink and detached HEAD equal
`d7023cf…`; strict `./.ap/ap doctor` PASS; no tags or extra refs.

**C2 — Exact changed-path allowlist.** `git diff --name-status
2281982f7dae0ef1f582d294592c41281ba11b21..HEAD` must equal the 14 acceptance
paths. Confirm `Cargo.toml`, `Cargo.lock`, `src/**`, both schemas,
`docs/domain-contract.md`, `docs/research-input-v1.md`, ADRs `0001`–`0007`,
`scripts/verify.sh`, `.github/workflows/verify.yml`, `rust-toolchain.toml`,
`.gitignore`, and `.ap` are unchanged. Confirm the correction commit changes
`README.md` only.

**C3 — Canonical gate.** Run `bash scripts/verify.sh` on the clean candidate.
Require exit `0`, 113 tests, `fmt --all --check`, clippy `-D warnings`, one-line
`bookradar-core` tree, `git diff --check`, strict `./.ap/ap doctor` PASS, and
clean worktree after the gate. Record the exact test split.

**C4 — Positive promotion path.** Use a fresh temp ledger and store. Import
`crates/bookradar-store/tests/fixtures/research/newer.json` at a caller-supplied
instant; `show` the finding; `promote` it onto source 1, offer 1, observation 1,
edition 10, with complete reviewer attestation; require exit 0. Verify
`history` and `current` show one supported observation and
`Checked available — Unix …; expires at Unix …`; verify provenance
`research:synthetic:producer/synthetic:run/synthetic:newer@1/0`; verify requested
URL/resolved URL/redirect are absent; verify the ledger was opened read-only.

**C5 — AgentOnly never eligible.** Direct library `promote` with
`EvidenceMethod::AgentOnly` must return `agent-only-evidence` and must not create
or change the store. CLI `--evidence-method agent-only` must exit `2` before
I/O. Append a `Supported` review with approval to an application observation
that has `AgentOnly` evidence; `Store::current` must remain `NotEligible` and
must not render `Checked available`. Confirm the kernel, not the new layer, is
the eligibility authority.

**C6 — Incomplete attestation and stale history.** Exercise missing approval,
missing coverage, non-Slovak, unresolved subject, empty statement/reference/
assessor/rationale, and an invalid offset. Refusals must be
`incomplete-attestation` and must not create/change the store. A stale positive
observation may be stored but must remain `NotEligible`/historical, not
`Checked available`.

**C7 — Closed ledger outcomes.** Exercise a rejected, quarantined, replayed, and
unknown finding. Require `not-admitted` or `unknown-finding`, exit `1`, no
application store creation/write, and byte-identical ledger/file rows. Confirm a
disputed admitted finding may be promoted under complete attestation and `show`
still prints the dispute.

**C8 — Idempotency, ids, and provenance.** A duplicate
`(source_id, offer_id, observation_id)` must return `duplicate-key`, roll back
registry inserts, and leave observation/review counts unchanged. The same
finding under a new observation id must be allowed. Position `0` is valid;
receipt `0` is usage. Source/offer/observation ids are caller-supplied; no
automatic allocation.

**C9 — Review revisions and conflicts.** Create an equal-time edition conflict
by promoting the same finding as observation 2 with edition 11 at the same
observed instant. Require `conflict=unresolved` / `Unverified -- unresolved
conflict`. Append `review --knowledge rejected --expected-revision 1` to
observation 2; require `conflict=clear` and the remaining checked-available
observation. Confirm both review revisions remain visible and immutable. Repeat
the disputed-to-supported supersession path and confirm prior revisions remain.

**C10 — Concurrency and time guards.** A wrong `expected_revision` must return
`review-conflict` and write nothing. A regressed `assessed_at` must return a
`storage` failure containing `assessment-time-regressed` and write nothing.

**C11 — Ledger and UI read-only integrity.** Confirm `ResearchStore` has no
`append_review`; `show` and `promote` open the ledger `ReadOnly`; promotion
writes only the application store; the research ledger file bytes and
`research_inputs`/`research_runs`/`research_findings` rows unchanged. Confirm
`bookradar-ui` opens both databases `OpenMode::ReadOnly`, supports only
`GET`/`HEAD` on `/` and `/style.css`, and creates no file on a read.

**C12 — UI offer selection.** Default `--source-id 1 --offer-id 1` must preserve
the existing page. `--source-id 2 --offer-id 7` must render that configured
query and its own state without falling back to `1/1`. Reject `0`, negative,
non-numeric, overflow, duplicate, and missing values with exit `2` before
database or socket I/O. Confirm no write, POST, form, JavaScript, or JSON
endpoint was added.

**C13 — CLI exit and error contract.** Confirm exit `2` usage before I/O; exit
`1` for `unknown-finding`, `not-admitted`, `agent-only-evidence`,
`incomplete-attestation`, storage, filesystem, `duplicate-key`, and
`review-conflict` as applicable; no exit `4`; stable stderr prefixes. Confirm
`bookradar-poc` remains four commands on source 1, offer 1 and
`bookradar-research` remains unchanged.

**C14 — No new dependencies, crates, or unsafe code.** Confirm `Cargo.lock` is
unchanged, `cargo tree -p bookradar-core` is one line, no external crate was
added, no new crate/workspace member was added, and every new source/test file
has `#![forbid(unsafe_code)]`.

**C15 — Documentation and ADR accuracy.** Verify the README end-to-end synthetic
demo now includes the second promotion, unresolved conflict, rejected revision,
cleared conflict, checked-available UI, defaults `1/1`, and the non-guarantee
notice. Verify the README commands actually run as written in a clean temp
directory. Verify ADR 0008 has `Status: Accepted 2026-11-14`,
`Date: 2026-11-14`, `Decision owner: COOPERATOR`, the nine approved cells, the
positive-only scope, alternatives, consequences, and limitations. Confirm
`docs/domain-contract.md`, `docs/research-input-v1.md`, and ADRs `0001`–`0007`
are unchanged.

**C16 — Rendered browser verification.** Use an isolated local Playwright/
Chromium session against the audit's synthetic databases. Start `bookradar-ui`
with `--bind 127.0.0.1:0`, read the printed loopback URL, and use the exact
`Host: 127.0.0.1:<port>` for HTTP checks. Verify in both `1280×800` and
`375×812` viewports:
  - default source 1 / offer 1 after the first promotion shows
    `Checked available — Unix 1793548100; expires at Unix 1793634500`;
  - after the second promotion the page shows the unresolved equal-time
    edition conflict and the configured offer;
  - after the rejection the page shows `conflict` clear, the checked-available
    observation, and observation 2's preserved supported+rejected revisions;
  - the research section still shows the candidate as `unreviewed`/`agent-only`/
    `not-eligible`, never promoted to verified stock;
  - `GET` and `HEAD` on `/` and `/style.css` succeed; a mutating method and a
    non-allowlisted target are rejected; required security headers are present;
  - no console/page errors, no external network requests, no committed
    screenshots, and no writable UI behavior.
  Record Playwright and Chromium versions, browser launch count, viewports,
  page/console/network observations, the Browser Stall Guard state, any failure
  episode and recovery attempts (one episode, at most two meaningful recovery
  attempts), and cleanup (UI process stopped, temp roots removed). If
  Playwright/Chromium is unavailable, stop `BLOCKED`; do not install it into the
  repository or add a dependency.

**C17 — Independence and evidence classification.** Attest that this is a fresh
session with no material implementation participation and no inherited parent
conversation. Keep the candidate frozen; do not correct. Classify every claim as
directly observed, inferred, or not verified. A finding must include the exact
control, evidence, affected path/behavior, severity, and smallest correction
direction (not an implementation). Do not emit a project closure signal.

## Browser and temporary-state contract

- **Browser adapter/origin:** local Playwright driving headless Chromium against
  literal loopback `http://127.0.0.1:<ephemeral>/`; no external origin, no
  account, no storage state, no remote host.
- **Temporary root:** an exact directory under ignored `target/` (for example
  `target/acceptance-review-promotion.XXXXXX`), created by you, synthetic
  contents only, removed by you. Report the exact path and cleanup outcome.
- **UI process:** one process per scenario, bind `127.0.0.1:0`, capture the
  printed URL, stop it cleanly after the scenario. Do not leave a listener.
- **Failure episode:** if the first browser launch fails, record the failure,
  use at most two meaningful recovery attempts, and apply the Browser Stall
  Guard Contract; do not loop or install dependencies.
- **Screenshots:** do not commit or write screenshots outside the temporary
  root; prefer DOM/text assertions and console/network evidence.
- **Network:** loopback only. Do not fetch external URLs, GitHub, registries, or
  providers. `bash scripts/verify.sh` may use its existing `cargo fetch
  --locked` behavior; no dependency is added.

## Acceptance report contract

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the prompt's coordinate values exactly once at the top of the report
metadata, then the routing fields. Include:

- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: acceptance-PASS` (or `not-applicable` if not PASS)
- `Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `Start commit: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `End commit: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `Changed files: none` (the audit is read-only)
- `Tests and validation: <gate result, CLI transcript, browser evidence, control matrix>`
- `Git result: none` (no fetch, stage, commit, push, tag, or ref change)
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: COOPERATOR acceptance sign-off and separate publication decision`
- `Report justification: final-acceptance`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the audit grant; no autonomous continuation.`
- Echo the SHA-256 of `02_acceptance_00.md`.
- `Orchestration critique:` with exactly `MEASURED:` and `LEAD:` lines.
- `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>`
- `Pre-Existing Failure Classification: none | <complete classification>`
- `Acceptance independence: required-fresh-independent`
- `Primary fresh acceptances used: 1`
- `Automatic corrections used: 0`
- `Correction re-acceptance: not-applicable`
- `Named missing-evidence probe: none`
- `Out-of-scope observations: ledger-candidates`

The body must include the C1–C17 matrix with evidence, findings (or `none`), the
browser evidence, the exact candidate identity, and an explicit statement that
the report does not close the whole. If any control fails, use `PARTIAL` or
`BLOCKED` with the exact finding and do not propose a correction as if
authorized.

## Stopping conditions

Stop and report without improvisation if:

- the candidate, parent, tree, branch, cleanliness, `.ap` pin, or `ap doctor`
  differs from the declared state;
- the session is not genuinely fresh or independence is compromised;
- Native Plan Mode is enabled;
- the repository is dirty before or after the gate, or the gate fails;
- a required read-only capability or Playwright/Chromium is unavailable;
- a browser or CLI probe needs a repository write, a new dependency, an
  external origin, a credential, a host/remote mutation, or a Meta write outside
  the report path;
- the evidence cannot distinguish PASS from a material NOT-VERIFIED;
- context pressure makes the audit unreliable; report the preserved evidence
  and limitation.

Do not correct, repair, reset, clean, stash, commit, push, or accept your own
work. The Orchestrator owns the accept/correct/escalate decision.

## What happens next

The Orchestrator will reconcile this audit report, present the acceptance verdict
and residual risks to the COOPERATOR, and decide whether a bounded correction or
a separate publication grant is appropriate. Publication, deployment, and
closure remain separate and are not authorized here.
