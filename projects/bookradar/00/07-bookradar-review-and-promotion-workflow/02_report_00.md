### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-review-and-promotion-workflow
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: BOOKRADAR-REVIEW-PROMOTION-ACCEPTANCE
status: BLOCKED
Phase-qualified result: not-applicable
Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112
Start commit: 80b172c2db6fcacc93041d4eb4c246450547f112
End commit: 80b172c2db6fcacc93041d4eb4c246450547f112
Changed files: none
Tests and validation: `bash scripts/verify.sh` exit 0, 113 tests, strict `./.ap/ap doctor` PASS, one-line core tree observed separately as `bookradar-core v0.1.0 (/Users/agile/Projects/bookradar)`. Independent CLI, library, SQLite, and loopback HTTP probes passed for C4–C15. C16 rendered Playwright/Chromium session was not run.
Git result: none
Deviations, risks, or missing evidence: Playwright and its Chromium build are not installed. Viewport, console, and browser-network evidence for C16 is absent. Eight local `refs/codex/turn-diffs/checkpoints/*` tree refs exist beside `refs/heads/main` and `refs/remotes/origin/main`; they are not tags, not branch heads, and not on the public remote. The planning sentence that every id rejects 0 is superseded for position 0 by this grant and by ADR 0008; the candidate accepts position 0 and rejects receipt 0.
Smallest next step: Orchestrator decides whether to renew one fresh rendered-browser check once a local Playwright/Chromium adapter already exists. No repository correction is indicated by C1–C15. Do not install Playwright into the repository. Publication and closure are not authorized.
Report justification: final-acceptance
Logical-whole closure: not-closed
Authority expiry: this terminal report ends the audit grant; no autonomous continuation.
Prompt SHA-256: `ffdea5259956cb521dede5b46d04e1138a4fe8faff41934a507797157baebf98`
Orchestration critique:
MEASURED: C16 cannot be completed on this host because Playwright is absent (`npx --no-install` reported missing package `playwright@1.65.1`; Python has no `playwright` module; `~/Library/Caches/ms-playwright` has no Chromium browser directory). Effect: the required 1280×800 and 375×812 rendered session, console, and browser-network observations were not produced. Smallest correction: rerun only that session with an already installed local adapter; do not add a dependency.
LEAD: none
Resolved Execution Issues / Near-Misses: the first dispute probe imported `newer.json` after `partial.json`, so finding F1 stayed `unreviewed` and the probe reported a false miss. Cause: that second file does not create the ledger dispute. Resolution: a second probe imported `conflict.json` and observed `ledger_knowledge=disputed`, promotion exit 0, an unchanged ledger hash, and null copied URLs. The library probe's single failed assertion was the same wrong fixture expectation. Residual risk: none for the disputed-admission claim.
Pre-Existing Failure Classification: none
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Acceptance owner map: `docs/domain-contract.md` (revision 1); `docs/research-input-v1.md`; `docs/adr/0001`–`0008`; `bookradar-core` verification semantics; `crates/bookradar-store` persistence/research/promotion; `crates/bookradar-ui` read-only UI; `README.md`; `scripts/verify.sh` and `.github/workflows/verify.yml`
Acceptance allowlist: README.md, crates/bookradar-store/src/lib.rs, crates/bookradar-store/src/research.rs, crates/bookradar-store/src/promotion.rs, crates/bookradar-store/src/bin/bookradar-review.rs, crates/bookradar-store/tests/promotion.rs, crates/bookradar-store/tests/review_cli.rs, crates/bookradar-ui/src/config.rs, crates/bookradar-ui/src/snapshot.rs, crates/bookradar-ui/src/render.rs, crates/bookradar-ui/tests/cli.rs, crates/bookradar-ui/tests/render.rs, crates/bookradar-ui/tests/common/mod.rs, docs/adr/0008-governed-review-and-promotion.md
Acceptance risk claims: R1–R15 as issued in `02_acceptance_00.md`
Acceptance control matrix: C1–C17 below
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-review-and-promotion-workflow
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the 113-test suite at candidate `80b172c2db6fcacc93041d4eb4c246450547f112`
Affected tests: promotion 12, review_cli 4, plus the preserved suite inside the same gate
New causal regression: independent CLI, library, and HTTP probes of the trust boundary, conflict, idempotency, and UI controls
Broad or full suite: required-because ADR 0006 binds `bash scripts/verify.sh`
Runtime or testbed: local loopback synthetic CLI; Playwright/Chromium unavailable
Independent acceptance: required-separate-fresh-worker

## Independence

This session's first input was `02_acceptance_00.md`. It did not plan, implement, or correct the candidate and did not read an implementing conversation. The plan, implementation report, and correction report were read as claims and checked against the candidate. Frozen evidence hashes matched the grant: plan `01_report_00.md` `e08189f9534208d4f1dee91d289014d536cad88327236691a9deb8a68e9ecc22` (323 lines); implementation prompt `04747fbabb2d9d7973943b7be3a419fdb54af735d4eda60eb73cf86dc3957926`; implementation report `030f8955a7a2b116a647ed6d47489ddf59bde23483b3f6e0e0a459e21642bf8c` (35 lines); correction prompt `2f921c3b3c945a84221d2c8de481fa577e86860a62af0338a37cbc2bef49d559`; correction report `f08aee0b9c4da4a1d53c5ddfd0021821db634ed5c88f8efbfef3c9daae6a8108` (39 lines); handout `ea5985ff63853098c8f2de5dc59977a30d5374acc0f812f23107e70656e997fd`; predecessor closure `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`. Native Plan Mode was not used. No repository file was edited.

This report does not close the logical whole.

## C1 — Candidate identity and public separation — PASS

Directly observed:

- HEAD `80b172c2db6fcacc93041d4eb4c246450547f112`
- parent `69ec45e245108c90e2de4302c03ca72572bf1829`
- tree `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
- subject `docs: demonstrate governed conflict resolution`
- `main` is ahead of `origin/main` by 2 (`git rev-list --left-right --count` printed `0 2`)
- `git ls-remote origin refs/heads/main` and local `origin/main` are `2281982f7dae0ef1f582d294592c41281ba11b21`
- `git status --porcelain` empty before the gate, after the gate, and after temporary-root cleanup
- `.ap` gitlink and detached HEAD `d7023cf037f6d17885c3ede5c04812c61640da50`
- strict `./.ap/ap doctor` printed `ap doctor: PASS`
- `git tag --list` empty; branches are only `main` and `remotes/origin/main`
- HEAD was still `80b172c…` after cleanup

Also directly observed, and not treated as a candidate or publication ref: eight local `refs/codex/turn-diffs/checkpoints/*` objects of type `tree`. `git ls-remote` did not advertise them. This audit did not create, move, or delete refs.

## C2 — Exact changed-path allowlist — PASS

`git diff --name-status 2281982f7dae0ef1f582d294592c41281ba11b21..HEAD` is exactly the 14 allowlist paths: `README.md`; `crates/bookradar-store/src/bin/bookradar-review.rs`; `crates/bookradar-store/src/lib.rs`; `crates/bookradar-store/src/promotion.rs`; `crates/bookradar-store/src/research.rs`; `crates/bookradar-store/tests/promotion.rs`; `crates/bookradar-store/tests/review_cli.rs`; `crates/bookradar-ui/src/config.rs`; `crates/bookradar-ui/src/render.rs`; `crates/bookradar-ui/src/snapshot.rs`; `crates/bookradar-ui/tests/cli.rs`; `crates/bookradar-ui/tests/common/mod.rs`; `crates/bookradar-ui/tests/render.rs`; `docs/adr/0008-governed-review-and-promotion.md`.

`git diff --name-status 69ec45e… ..HEAD` is `M README.md` only. `git diff 2281982f… ..HEAD -- Cargo.toml Cargo.lock` is empty. The full name-status does not include `src/**`, either SQL schema, `docs/domain-contract.md`, `docs/research-input-v1.md`, ADRs 0001–0007, `scripts/verify.sh`, `.github/workflows/verify.yml`, `rust-toolchain.toml`, `.gitignore`, `.ap`, `bookradar-poc`, or `bookradar-research`.

## C3 — Canonical gate — PASS

`bash scripts/verify.sh` on the clean candidate exited 0. `rustc 1.99.1 (58cf8f9c3 2026-10-13)`. The script's `set -euo pipefail` order is fetch, build, test, `fmt --all --check`, `clippy -D warnings`, the one-line core-tree check, `git diff --check`, strict `./.ap/ap doctor`, then a clean-worktree check. Doctor output was printed and the process then exited 0, so the preceding checks passed. A later read-only `cargo +1.99.1 tree --locked --offline -p bookradar-core` printed exactly `bookradar-core v0.1.0 (/Users/agile/Projects/bookradar)`.

Test split, 113 passed, 0 failed:

- `tests/verification.rs` 17
- store lib 10
- `bookradar-poc`, `bookradar-research`, and `bookradar-review` bins 0
- store `tests/cli.rs` 4
- `tests/history.rs` 13
- `tests/persistence.rs` 6
- `tests/promotion.rs` 12
- `tests/research_cli.rs` 2
- `tests/research_contract.rs` 5
- `tests/research_ingestion.rs` 20
- `tests/review_cli.rs` 4
- UI lib and main 0
- UI `tests/cli.rs` 4
- UI `tests/http.rs` 6
- UI `tests/render.rs` 10
- doc-tests 0

`git diff -U0 2281982f… ..HEAD` adds 19 `#[test]` attributes. 94 preserved plus 19 new is 113. The plan's pre-implementation estimate of 111 was not a gate. The worktree was empty after the gate.

## C4 — Positive promotion path — PASS

The README command sequence was run as written under ignored `target/review-promotion`, then removed. `newer.json` imported at `1793545200` (exit 0). `show` exited 0 with `outcome=admitted`, `position=0`, and `ledger_knowledge=unreviewed`. `promote` onto source 1, offer 1, observation 1, edition 10 exited 0 and printed `provenance=research:synthetic:producer/synthetic:run/synthetic:newer@1/0`. Ledger SHA-256 was unchanged across show and promote. `bookradar-poc current` at `1793548800` printed `conflict=clear`, `verification=eligible`, and `Checked available -- unix:1793548100; expires_unix=1793634500`. `history` printed `count=1` and `review=supported`.

SQLite on that store: observation `(1,1,1)`, edition 10, method `manual`, provenance as above, and `requested_url`, `resolved_url`, and `redirect_reference` all null. The ledger row count stayed one finding. The same absence of URLs was observed from the library probe on a `newer.json` promotion. A separate promotion of admitted F1, whose canonical JSON contains `synthetic:requested` and `synthetic:resolved`, also stored null URLs and `source_statement=reviewer:statement`.

## C5 — AgentOnly never eligible — PASS

Library `promote` with `EvidenceMethod::AgentOnly` returned `agent-only-evidence`, did not create an absent store, and left an existing store's bytes and the ledger bytes unchanged. CLI `--evidence-method agent-only` exited 2 with a `usage:` prefix and created neither the missing ledger nor the missing store.

A library-built application observation with `AgentOnly` evidence, followed by a `Supported` review with approval at `expected_revision` 0, stayed `NotEligible`. Its labels did not contain `Checked available`. Eligibility still comes from `evaluate_verification`: `EvidenceMethod::AgentOnly` returns false in `policy_matches` (`src/verification.rs`). The new layer does not replace that function.

## C6 — Incomplete attestation and stale history — PASS

Library refusals, each with no store file created: missing approval, missing coverage, Czech language, unresolved subject, empty statement, empty reference, empty assessor, empty rationale, and offset `64801`. Every category was `incomplete-attestation`.

CLI invalid offset `64801` exited 2 before creating a store. That is the usage gate in front of the library refusal.

A positive row observed at `1793548100` and evaluated at `1793634500` was retained and was `verification=not-eligible`, with no `Checked available` label, both through `bookradar-poc current` and through `Store::current`.

## C7 — Closed ledger outcomes — PASS

Import of `partial.json` (CLI exit 3, committed), `newer.json` (exit 0), and the same envelope with `reported_run_outcome` changed from `succeeded` to `failed` (exit 0) produced:

- receipt 1 position 0 `F1` `admitted` `unreviewed`
- receipt 1 position 1 finding id absent, `rejected`, `missing-finding-id`
- receipt 1 position 2 `F3` `quarantined` `invalid-availability`
- receipt 2 position 0 `synthetic:newer` `admitted`
- receipt 3 position 0 `synthetic:newer` `replayed`

CLI promote results, each exit 1, no store created, ledger hash unchanged: F1 position 1 `unknown-finding`; F3 position 2 `not-admitted`; replayed receipt 3 `not-admitted`; missing finding `unknown-finding`. The rejected row has no finding id, so the matching refusal is `unknown-finding`, which ADR 0008 records.

Disputed path, corrected probe: `partial.json` then `conflict.json`. Inspect showed F1 `admitted` `knowledge=disputed`. `show` printed `ledger_knowledge=disputed`. Promote exited 0 with provenance `research:synthetic:producer/synthetic:run/F1@1/0`. Ledger hash was unchanged and a later `show` still printed `disputed`.

## C8 — Idempotency, ids, and provenance — PASS

A second CLI promote of observation 1 exited 1 with `duplicate-key:`. The side store then had one observation for source 1 offer 1. A following promote with `--source-id 2 --offer-id 7 --observation-id 1` exited 0. SQLite showed exactly `(1,1,1)` and `(2,7,1)`, both with the same `research:…newer@1/0` provenance, and review count 2. The library probe likewise kept one row after `duplicate-key` and allowed observation 2 for the same finding.

Position 0 was accepted by `show` and `promote`. Receipt 0 on `show` exited 2 and did not create the ledger file. No allocator assigned an id other than the caller-supplied id.

## C9 — Review revisions and conflicts — PASS

The second README promote, observation 2 edition 11 at the same `1793548100`, made `bookradar-poc current` print `latest_attempts=1,2`, `candidates=1,2 conflict=unresolved recheck=clear verification=not-eligible`, and `Unverified -- unresolved conflict`, with no `Checked available`. `review --knowledge rejected --expected-revision 1` printed `reviewed source=1 offer=1 observation=2 revision=2`. The following current printed `conflict=clear`, `verification=eligible`, and `Checked available -- unix:1793548100; expires_unix=1793634500`.

SQLite reviews after that rejection: observation 1 revision 1 `supported`; observation 2 revision 1 `supported` and revision 2 `rejected` with rationale `reviewer:reject-conflicting-edition`. The library probe observed the same pair of immutable revisions and a cleared conflict. A separate library path appended `Supported` after `Disputed` on one observation; revision 1 stayed `Disputed`, revision 2 was `Supported`, and the later view was eligible with conflict clear.

## C10 — Concurrency and time guards — PASS

On the conflicted store, `--expected-revision 0` exited 1 with `review-conflict:` and the store SHA-256 did not change. `--expected-revision 1` with `--assessed-at 1793548699` (before the initial `1793548700` assessment) exited 1 with `storage:` and `assessment-time-regressed`, and the store hash stayed the same. The library probe returned the same two categories and the same unchanged bytes, with the review count still 1.

## C11 — Ledger and UI read-only integrity — PASS

`research.rs` has no `append_review`. `append_review` exists on the application `Store` only. `show` and `promote` open the ledger with `OpenMode::ReadOnly` before any store open, and policy refusal happens before `Store::open`. Ledger file hashes and `research_inputs` / `research_runs` / `research_findings` row dumps were identical before and after show, promote, and review.

`bookradar-ui` `load_observations` and `load_research` open both databases `OpenMode::ReadOnly` and drop them before `serve`. `http.rs` accepts only `GET` and `HEAD`, and only `/` and `/style.css`. Serving the three stage databases and the two-offer database left both file hashes unchanged. Invalid UI arguments exited 2 without creating the named database files.

## C12 — UI offer selection — PASS

Invalid `--source-id` / `--offer-id` values `0`, `-1`, `abc`, and `9223372036854775808`, plus `--offer-id 0`, a duplicate `--source-id`, and a missing value, each exited 2 and created no database.

The page served with no offer flags and the page served with `--source-id 1 --offer-id 1` were byte-identical. Both named `source 1, offer 1`. `--source-id 2 --offer-id 7` named `source 2, offer 7`, contained `reviewer:offer-seven`, and did not contain `reviewer:statement` or `source 1, offer 1`. The rendered HTML has no `<script` and no `<form`. No write method or JSON route was added; `POST /` returned `405` and `/api` returned `404`.

## C13 — CLI exit and error contract — PASS

Observed exits: `2` for missing command, `agent-only`, receipt `0`, invalid offset, and `bookradar-poc fifth`; `1` for `unknown-finding`, `not-admitted`, `duplicate-key`, `review-conflict`, and `storage` / `assessment-time-regressed`. Stderr prefixes matched those categories or `usage:`. No probed command exited 4. The review and UI sources contain no `ExitCode::from(4)`.

`bookradar-poc fifth` exited 2 with `expected init, append-fixture, current, or history`. `bookradar-research.rs` is outside the diff. `bookradar-poc.rs` still matches only those four commands and still uses `synthetic_offer()`.

## C14 — No new dependencies, crates, or unsafe code — PASS

`Cargo.toml` and `Cargo.lock` are unchanged. Workspace members remain `.`, `crates/bookradar-store`, and `crates/bookradar-ui`. The core tree is one line. New files `promotion.rs`, `bookradar-review.rs`, `tests/promotion.rs`, and `tests/review_cli.rs` each contain `#![forbid(unsafe_code)]`. No external crate was added.

## C15 — Documentation and ADR accuracy — PASS

The README commands, run from the repository root with `cargo +1.99.1 build --locked --offline` exit 0, produced the first checked-available current, the unresolved equal-time conflict, the rejected revision, and the cleared checked-available current described above. The rendered page for that end state shows `Checked available — Unix 1793548100; expires at Unix 1793634500`, conflict `clear`, and the notice `not a guarantee that a purchase will succeed`. Defaults are source 1 and offer 1. The non-default pair is documented as query-only and was exercised on a separate row.

ADR 0008, read in full, has `Status: Accepted 2026-11-14`, `Date: 2026-11-14`, `Decision owner: COOPERATOR`, the nine approved cells, positive-only scope, alternatives, consequences, and limitations. `docs/domain-contract.md`, `docs/research-input-v1.md`, and ADRs 0001–0007 are outside the diff.

The plan's recommended `promote(&mut ResearchStore, &mut Store, …)` signature is not the candidate's signature. The candidate opens the store path internally after the refusal checks. That matches this grant's "refusal does not create the store" rule. It is not a control failure.

## C16 — Rendered browser verification — NOT-VERIFIED

Playwright/Chromium was unavailable. `npx --no-install playwright --version` stopped with missing package `playwright@1.65.1`. Python found no `playwright` module. `~/Library/Caches/ms-playwright` contains cursor browser metadata and `ffmpeg-1013`, not a Playwright Chromium directory. `/Applications/Google Chrome.app` is present and was not used as a substitute. Nothing was installed and no dependency was added. Browser launch count: 0. Viewports `1280×800` and `375×812` were not opened. Console, page errors, and browser-observed network requests were not collected.

Loopback HTTP against the same synthetic pages was directly observed, with `Host: 127.0.0.1:<port>` on an ephemeral bind. It does not replace the rendered session.

- After the first promotion: `source 1, offer 1`; `Checked available — Unix 1793548100; expires at Unix 1793634500`; application conflict `clear`; research card `Research candidate — unreviewed`, evidence `agent-only`, verification `not-eligible`.
- After the second promotion: `Unverified — unresolved conflict`; application conflict `unresolved`; configured offer `source 1, offer 1`; no `Checked available`. The research card stayed `unreviewed` / `agent-only` / `not-eligible`, and its own conflict field stayed `clear`.
- After the rejection: checked-available sentence restored; application conflict `clear`; observation history contains knowledge `supported` and `rejected`; `Revision 1` and `Revision 2` are both present. The research card was still not promoted to verified stock.
- `GET` and `HEAD` on `/` and `/style.css` returned `200`. `HEAD` bodies were empty. `POST /` returned `405` with `Allow: GET, HEAD`. `GET /api` returned `404`.
- Response headers included `Content-Security-Policy: default-src 'none'`, `X-Content-Type-Options: nosniff`, `Cache-Control: no-store`, `Referrer-Policy: no-referrer`, and `Cross-Origin-Resource-Policy: same-origin`.
- Database hashes were unchanged. No screenshot was written. Each UI process was stopped. `pgrep` found no `bookradar-ui` or review binary afterward.

```text
Failure episode identity: playwright-adapter-absent
Prior episode identity: none
Episode relationship: initial
Symptom continuity evidence: npx --no-install reported missing package playwright@1.65.1; Python found no playwright module; ~/Library/Caches/ms-playwright had no Chromium browser directory
Initial verification result: failed-conclusive
Recovery attempts: 0
Recovery attempt 1: not-used because installing Playwright or fetching Chromium is outside this grant
Recovery attempt 2: not-used because another lookup would not create the adapter
Verification succeeded: no
Repeated failure remains unresolved: yes
Conclusive no-progress evidence: yes
Stall guard: triggered
Repeated failure evidence: none
Guard rationale: the adapter is absent before any launch; a further attempt is not meaningful without an install this grant forbids
Evidence preserved: yes
Browser repair after trigger: none
Alternative evidence: loopback HTTP text and header checks recorded above
Absent verification: Playwright-driven Chromium at 1280×800 and 375×812, including console, page errors, and browser-observed network
Cooperator acceptance required: yes
Result claimed from missing evidence: none
```

## C17 — Independence and evidence classification — PASS

This is a fresh session with no material implementation participation and no inherited parent conversation. The candidate was not corrected. Classifications:

- Directly observed: git identity, public `refs/heads/main`, doctor, diff, gate exit and per-suite counts, core tree line, library probe, CLI transcripts, SQLite rows, and loopback HTTP pages.
- Inferred: `fmt --check`, clippy, and `git diff --check` succeeded because `verify.sh` exits on their failure and then printed a passing doctor. The tree line itself was also printed by a separate locked offline `cargo tree`.
- Not verified: Playwright viewport, console, and browser-network evidence. No product behavior is claimed from that absence.

## Findings

1. Control C16. Evidence: Playwright/Chromium is not installed, as recorded above. Affected behavior: the rendered two-viewport acceptance session. Severity: missing required acceptance evidence. No product defect was observed in the HTTP checks of the same pages. Smallest correction direction: rerun C16 with an already installed local Playwright/Chromium adapter. Do not add a repository dependency and do not treat the HTTP checks as the rendered session.

No other finding. C1–C15 and C17 passed on the observed evidence.

## Temporary state and cleanup

Owned roots: `target/acceptance-review-promotion.HmnW8o` and `target/review-promotion`. Both were removed. A following `git status --porcelain` was empty and HEAD was still `80b172c2db6fcacc93041d4eb4c246450547f112`. No listener was left.

One `npx --no-install` lookup reported the missing Playwright package and wrote an npm log under the user npm cache. It did not install a package and did not change the repository.

This report records an audit result only. It does not close the logical whole, does not publish, and does not authorize a correction.
