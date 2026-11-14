# BookRadar — Fresh Independent Audit — Minimal Local Read-Only UI Shell

Persistent role identity: WORKER
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: BOOKRADAR-UI-SHELL-ACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — independent verification of a cross-cutting user-visible UI slice, restricted HTTP parser, truth-label invariants, and live local Playwright/Chromium rendered browser evidence.
Recommended context capacity: approximately 250k tokens
Independence required: yes

Acceptance candidate: 2281982f7dae0ef1f582d294592c41281ba11b21
Acceptance owner map: docs/domain-contract.md (revision 1); docs/research-input-v1.md; docs/adr/0001-book-edition-and-offer-identity.md through docs/adr/0007-local-read-only-ui-shell.md; README.md; scripts/verify.sh
Acceptance allowlist: Cargo.toml, Cargo.lock, README.md, crates/bookradar-store/src/history.rs, crates/bookradar-store/src/lib.rs, crates/bookradar-ui/Cargo.toml, crates/bookradar-ui/src/lib.rs, crates/bookradar-ui/src/main.rs, crates/bookradar-ui/src/config.rs, crates/bookradar-ui/src/snapshot.rs, crates/bookradar-ui/src/render.rs, crates/bookradar-ui/src/http.rs, crates/bookradar-ui/src/style.css, crates/bookradar-ui/tests/common/mod.rs, crates/bookradar-ui/tests/render.rs, crates/bookradar-ui/tests/http.rs, crates/bookradar-ui/tests/cli.rs, docs/adr/0007-local-read-only-ui-shell.md
Acceptance risk claims: R1 baseline, parent, tree, and exact 18-path allowlist integrity; R2 zero external dependencies and single-line bookradar-core tree; R3 canonical gate bash scripts/verify.sh PASS with 94 tests (77 preserved + 17 UI); R4 shared render_current_labels with zero CLI transcript or predicate drift; R5 all 13 accepted current truth labels, expiry, and non-guarantee notice; R6 research candidate unreviewed/disputed/agent-only/not-eligible invariants and fail-closed suppression; R7 empty, missing, corrupt, swapped, and unsupported-schema states; R8 HTML escaping of hostile observation and research text; R9 literal 127.0.0.1 binding, GET/HEAD-only routing, header/timeout bounds, Host/Origin/Sec-Fetch-Site checks, and strict CSP/security headers; R10 strict OpenMode::ReadOnly database preservation without writes or file creation; R11 README and ADR 0007 accuracy without domain-contract or ADR 0001-0006 changes; R12 local Playwright/Chromium rendered browser verification in an isolated context
Acceptance control matrix: C1 through C14 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-ui-shell
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_acceptance_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none (read-only audit; ignored `target/` build outputs from `bash scripts/verify.sh` and temporary probe directories created and removed before completion only)
Host/remote mutation: none
Trace persistence: none

## Authority and independence posture

You are a genuinely fresh WORKER in the `Fresh Independent Audit` profile
(`Worker session ordinal: 03`, `Worker exchange ordinal: 01`, `Worker session
target: fresh-worker-session`, `Native planning mode: not-used`). This prompt is
your only task authority.

You must be a separate concrete Worker session that did not participate in
planning or implementing candidate `2281982f7dae0ef1f582d294592c41281ba11b21`
and inherits no parent or implementation conversation. If this session
participated in planning or implementing this logical whole, or if Native Plan
Mode is enabled, stop `BLOCKED` immediately before running any check.

This audit is **read-only** with respect to the repository and Meta trace. Do
not modify any tracked file, create any untracked repository file that remains
after your audit, run any Git write (`commit`, `amend`, `reset`, `clean`,
`stash`, `checkout`, `push`, `fetch`), or write to `/Users/agile/meta`. Return
the complete terminal report in this session; the COOPERATOR will persist it at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/03_report_00.md`.
You may read `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/03_acceptance_00.md`
to verify identity and echo its SHA-256 in your report.

Note on trace history: the implementation commit
`2281982f7dae0ef1f582d294592c41281ba11b21` was produced under grant
`01_implementation_01.md`, while `01_report_01.md` and `02_report_00.md` record
pre-mutation `BLOCKED` stops from other sessions. Do not rely on any
implementation report; audit the committed repository state
`2281982f7dae0ef1f582d294592c41281ba11b21` directly against the accepted plan
`01_report_00.md` and the domain contract.

## Repository and candidate gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected candidate HEAD: `2281982f7dae0ef1f582d294592c41281ba11b21`
Expected parent (public baseline): `a2182302de73cb345b4b646993a1ad25d602555f`
Expected candidate tree: `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`
Expected commit subject: `feat: add a local read-only UI shell`
Expected public `origin/main` and remote `refs/heads/main`: `a2182302de73cb345b4b646993a1ad25d602555f` (local `main` is ahead 1, unpublished)
Expected worktree: clean (`git status --porcelain` empty; `target/` ignored by `/target/`)
Governing AP: `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`

Execution route (RF-16): no `ap.project.conf` is declared in this repository.
The canonical project verification gate is `bash scripts/verify.sh` (per
`README.md` and `docs/adr/0006-verification-gate-and-ci.md`), and the protocol
integration check is `./.ap/ap doctor`. Run `bash scripts/verify.sh` as the
canonical build/test/fmt/clippy/core-tree/doctor/clean-worktree gate.

## Mandatory reading

- `.ap/AP.md` (WORKER spine; RF-03, RF-05, RF-06, RF-07, RF-08, RF-11, RF-12,
  RF-16, RF-18, RF-19; Acceptance, Correction, and Escalation; §8; §11 Browser
  and Rendered Acceptance Automation and Browser Verification Stall Guard; §12
  Validation; §18 Stopping Conditions).
- `.ap/AP_WORKER.md` and `.ap/PROMPT_CONTRACTS.md` (Worker Report Header;
  Acceptance and Correction Record; Validation Ladder Record; Browser Stall
  Guard Contract).
- `AGENTS.md`, `README.md`, `Cargo.toml`, `Cargo.lock`, `scripts/verify.sh`,
  `.github/workflows/verify.yml`.
- `docs/domain-contract.md`, `docs/research-input-v1.md`, and `docs/adr/0001`–`0007`.
- Accepted plan `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_00.md`
  (SHA-256 `00c46a0fb52a1657b218439e6b5d2a2dce8c029d2799bb234ed3f85f7aa46ffd`).
- All 18 changed/added files in `2281982f7dae0ef1f582d294592c41281ba11b21`:
  `Cargo.toml`, `Cargo.lock`, `README.md`,
  `crates/bookradar-store/src/history.rs`, `crates/bookradar-store/src/lib.rs`,
  `crates/bookradar-ui/Cargo.toml`, `crates/bookradar-ui/src/lib.rs`,
  `crates/bookradar-ui/src/main.rs`, `crates/bookradar-ui/src/config.rs`,
  `crates/bookradar-ui/src/snapshot.rs`, `crates/bookradar-ui/src/render.rs`,
  `crates/bookradar-ui/src/http.rs`, `crates/bookradar-ui/src/style.css`,
  `crates/bookradar-ui/tests/common/mod.rs`,
  `crates/bookradar-ui/tests/render.rs`, `crates/bookradar-ui/tests/http.rs`,
  `crates/bookradar-ui/tests/cli.rs`, and
  `docs/adr/0007-local-read-only-ui-shell.md`.

## Fixed acceptance control matrix (C1–C14)

Verify every positive and negative control below with direct evidence:

- **C1 — Candidate & allowlist integrity:** `HEAD` is
  `2281982f7dae0ef1f582d294592c41281ba11b21`, parent is
  `a2182302de73cb345b4b646993a1ad25d602555f`, tree is
  `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`, subject is
  `feat: add a local read-only UI shell`; `git diff --name-status a2182302de73cb345b4b646993a1ad25d602555f..2281982f7dae0ef1f582d294592c41281ba11b21`
  lists the exact 18 allowlist paths and nothing else; public `refs/heads/main`
  is still `a2182302de73cb345b4b646993a1ad25d602555f` (no premature push); `.ap`
  is detached and clean at `d7023cf037f6d17885c3ede5c04812c61640da50`.
- **C2 — Dependency & safety invariants:** `crates/bookradar-ui/Cargo.toml`
  depends only on path dependencies `bookradar-core` and `bookradar-store`
  (`publish = false`, `edition = "2024"`, `rust-version = "1.99.1"`,
  `#![forbid(unsafe_code)]` in library, binary, and test targets); `Cargo.lock`
  adds only `bookradar-ui 0.1.0` with zero new external crates or feature
  changes; `cargo +1.99.1 tree --locked --offline -p bookradar-core` is 1 line.
- **C3 — Canonical verification gate (`bash scripts/verify.sh`):** Exits `0`;
  runs all **94 tests** (`17` core, `10` store unit, `4` old CLI, `13` history,
  `6` persistence, `2` research CLI, `5` research contract, `20` research
  ingestion, `3` UI CLI, `6` UI HTTP, `8` UI render; `0` doc/bin unit tests);
  passes `fmt`, `clippy -D warnings`, `git diff --check`, strict `./.ap/ap doctor`,
  and leaves `git status --porcelain` empty.
- **C4 — Store seam & CLI compatibility:** `render_current_labels` in
  `crates/bookradar-store/src/history.rs` reuses `human_lines` and
  `render_current` routes through it without altering any selection predicate,
  store behavior, schema, or CLI output bytes. `bookradar-ui` contains no SQL,
  no JSON admission parser, and no freshness/conflict/recheck/eligibility
  reimplementation.
- **C5 — Current assessment & all 13 truth labels:** Renders all 13 accepted
  truth label families (`Checked available — Unix …; expires at Unix …`,
  `Last observed available — Unix …`, `Last observed reserved — Unix …`,
  `Last observed unavailable — Unix …`, `Could not recheck — Unix …`,
  `Listing removed — Unix …`, and the 7 `Unverified — …` reasons), the
  mandatory notice `"Verification describes an evidenced source observation, not a guarantee that a purchase will succeed."`,
  candidate facets, and never generates `"Sold out"`, `"In stock"`, or an
  unqualified green `"Available"` badge.
- **C6 — Observation history, timestamps, and reviews:** Preserves observation,
  source, offer, subject/edition, language, access, listing disposition,
  `Source-reported availability`, source statement, evidence method/reference
  and 3 claim-coverage bits, URLs/redirect/provenance/uncertainty, full
  timestamp assertions (original text, known offset or `unknown`, Unix instant,
  signed seconds, nanoseconds including pre-epoch, and separate ingestion time),
  and all review revisions (`No review recorded.` when empty).
- **C7 — Research ledger & candidate invariants:** Renders envelope, run,
  finding, projected-observation, review, and edition counts, receipt table, and
  finding table (`admitted`, `replayed`, `rejected`, `quarantined`, reasons,
  knowledge, projected observation ID or `not projected`). Research current
  candidates are strictly labelled `Research candidate — unreviewed` or
  `Research candidate — disputed`, with `Unverified`, `agent-only`, `not recorded`
  approval, and `not-eligible`, plus fail-closed suppression
  (`Unexpected research assessment — verification display suppressed`) if an
  unexpected state is supplied.
- **C8 — Empty, missing, corrupt, swapped, and unsupported-schema states:**
  Distinct messages for empty observation offer (`No observations for this offer.`),
  empty research ledger (`Research ledger is empty.`), no candidate for query
  (`No research candidates for this query.`), missing file
  (`Database not found (not-found).`), corrupt file
  (`Unsupported database (unsupported-schema: corrupt-database).`), wrong
  application ID / swapped slots (`unsupported-schema: application-id`), and
  unsupported version (`unsupported-schema: user-version`), while a healthy
  independent slot still renders.
- **C9 — HTML escaping & untrusted-content containment:** Escapes `&`, `<`,
  `>`, `"`, and `'` across all displayed operator, observation, review, and
  research strings; renders URLs and evidence references as plain text rather
  than active links, scripts, images, or executable sinks.
- **C10 — Local HTTP & CLI security boundary:** Rejects non-loopback `--bind`
  values (`0.0.0.0`, external IPs, `localhost`, IPv6, invalid ports) and invalid
  CLI flags with exit `2` before any database or socket I/O; `--help` exits `0`
  without I/O; bind failure exits `1` without fallback; serves only `GET` and
  `HEAD` on `/` and `/style.css` (`405` with `Allow: GET, HEAD` on other
  methods, `404` on other paths, `400` on query/traversal/absolute targets or
  framing errors, `431` on oversized/excess headers, `408` on header-read
  timeout, `403` on foreign `Host`/`Origin` or cross-site `Sec-Fetch-Site`);
  sends `Connection: close` and all 5 required security headers without CORS or
  a wall-clock `Date` header.
- **C11 — Read-only database preservation:** Opens both databases strictly with
  `OpenMode::ReadOnly`, closes connections before serving, never modifies
  database bytes, never creates missing files or sidecars.
- **C12 — Documentation & ADR 0007:** `README.md` accurately documents
  `bookradar-ui`, its flags, the reproducible synthetic demo, and boundaries;
  `docs/adr/0007-local-read-only-ui-shell.md` is complete (`Accepted 2026-11-13`,
  owner `COOPERATOR`); `docs/domain-contract.md`, `docs/research-input-v1.md`,
  `docs/adr/0001`–`0006`, `scripts/verify.sh`, and `.github/workflows/verify.yml`
  are unchanged.
- **C13 — Local Playwright/Chromium rendered browser verification:** Using an
  isolated temporary directory (removed before completion), prepare synthetic
  stores and verify the live local server `http://127.0.0.1:<port>` in a clean
  isolated Playwright/Chromium browser context (blocking any non-loopback
  origin):
  1. Main populated demo at `--now 1793548800`: verify page title `BookRadar`,
     banner `Synthetic data · Local · Read-only`, `Evaluation instant — Unix 1793548800`,
     all 4 section headings, `Checked available — Unix 1793534400; expires at Unix 1793620800`,
     non-guarantee notice, observation `<details>` disclosures (`Observation 4`,
     `Observation 1`, `Observation 2`, `Observation 3`), research ledger counts
     (`2`, `1`, `4`, `1`, `2`, `0`) and tables, and `Research candidate — disputed`
     (`Unverified`, `agent-only`, `not-eligible`).
  2. Expiry demo on the same files restarted with `--now 1793620800`: verify
     `Checked available` is replaced by `Last observed available — Unix 1793534400`
     and `stale` temporal assessment.
  3. Failed-recheck demo (observation store with `available` + `blocked` at
     `--now 1793548800`): verify `Could not recheck — Unix 1793527200` alongside
     `Last observed available — Unix 1793523600`, with no `"Sold out"` claim.
  4. Missing/swapped database error state: verify `Database not found (not-found).`
     and `Unsupported database (unsupported-schema: application-id).` render as
     visible error text while a healthy slot still renders.
  5. Layout, accessibility, and styling: verify `/style.css` loads (`200`),
     skip-link and `<details>` keyboard operation work, both desktop (e.g.
     `1280x800`) and narrow (e.g. `375x812`) viewports render cleanly without
     broken layout, and zero console errors or external network requests occur.
- **C14 — Post-audit cleanliness:** Stop any started `bookradar-ui` and browser
  processes, remove all audit-created temporary directories/files, and confirm
  `git status --porcelain` is empty and `HEAD` is still
  `2281982f7dae0ef1f582d294592c41281ba11b21`.

## Browser authority and Browser Stall Guard Contract

Browser authority is limited to a clean, isolated local Playwright/Chromium
context accessing only `http://127.0.0.1:<port>` for the local `bookradar-ui`
process started from synthetic fixtures in an audit-owned temporary directory.
Do not access any external URL, user browser profile, cookies, extensions, or
unrelated tabs. Do not commit any screenshot to the repository; if temporary
screenshots are captured in the audit-owned temporary directory for inspection,
delete them during cleanup and report their cleanup outcome.

Include the complete **Browser Stall Guard Contract** record from
`.ap/PROMPT_CONTRACTS.md#browser-stall-guard-contract` in your report (`Failure
episode identity`, `Prior episode identity`, `Episode relationship`, `Symptom
continuity evidence`, `Initial verification result`, `Recovery attempts`,
`Recovery attempt 1`, `Recovery attempt 2`, `Verification succeeded`, `Repeated
failure remains unresolved`, `Conclusive no-progress evidence`, `Stall guard`,
`Repeated failure evidence`, `Guard rationale`, `Evidence preserved`, `Browser
repair after trigger`, `Alternative evidence`, `Absent verification`,
`Cooperator acceptance required`, `Result claimed from missing evidence`). Remember
that missing browser evidence never becomes `acceptance-PASS`.

## Validation ladder

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: 77 preserved core and store tests
Affected tests: 17 bookradar-ui tests (render, http, cli) plus store CLI tests
New causal regression: none — read-only independent audit of committed candidate 2281982f7dae0ef1f582d294592c41281ba11b21
Broad or full suite: required-because ADR 0006 binds bash scripts/verify.sh as the canonical gate
Runtime or testbed: local loopback bookradar-ui + Playwright/Chromium isolated browser verification
Independent acceptance: required-separate-fresh-worker
```

## Report contract

Return the complete terminal report in this session; the COOPERATOR will save
it at `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/03_report_00.md`.
Begin the report with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinates once at the top of the report metadata:

```text
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 03
Worker exchange ordinal: 01
```

Include:
- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: acceptance-PASS` (only if all C1–C14 including rendered browser verification pass; otherwise `not-applicable`)
- `Start commit: 2281982f7dae0ef1f582d294592c41281ba11b21`
- `End commit: 2281982f7dae0ef1f582d294592c41281ba11b21`
- `Changed files: none`
- The Acceptance and Correction Record, the C1–C14 control results, the Browser
  Stall Guard Contract record (with observed Playwright/Chromium versions,
  origins, viewports, and cleanup verification), and `bash scripts/verify.sh`
  evidence.
- `Git result: read-only; no stage, commit, or push`
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: COOPERATOR rendered acceptance checklist and separate publication decision for 2281982f7dae0ef1f582d294592c41281ba11b21`
- `Report justification: final-acceptance`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the audit grant; no autonomous continuation.`
- Echo the SHA-256 of `03_acceptance_00.md` and include:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>
Pre-Existing Failure Classification: none | <complete classification per the contract>
```
