# BookRadar — `bookradar-review-and-promotion-workflow` — Notes

Orchestrator-authored. Not task authority.

## 2026-11-14 — Stage 1 restoration; handout revalidation; Stage 2 decision gate

- Session identity: fresh per-whole ORCHESTRATOR, direct project checkout
  `/Users/agile/Projects/bookradar`, `Capability profile: Orchestrator`,
  `Orchestrator session scope: logical-whole`. Began read-only.
- Whole opened from the COOPERATOR-delivered provisional handout
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md`
  (SHA-256 `ea5985ff63853098c8f2de5dc59977a30d5374acc0f812f23107e70656e997fd`).
- **Filename exception:** the COOPERATOR expressly requested `00_handout_00.md`
  instead of Meta's usual `00_handout.md`. This is a named opening-handout
  exception, not a Worker exchange and not a change to Meta's naming
  convention. The file is not renamed, no competing `00_handout.md` is created,
  and its handoff-sequence position is `00`; the closing artifact will be
  `01_closure.md` (or the next free handoff prefix if another handout
  intervenes).
- Baseline revalidated read-only on 2026-11-14:
  - Public `refs/heads/main` and local `HEAD`/`main`/`origin/main` all equal
    `2281982f7dae0ef1f582d294592c41281ba11b21`; branch `+0 -0`; worktree clean
    (`git status --porcelain` empty; `target/` ignored).
  - Commit parent `a2182302de73cb345b4b646993a1ad25d602555f`, tree
    `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`, subject
    `feat: add a local read-only UI shell`, date `2026-11-13T18:35:51+01:00`.
  - Public CI run `43485796198`
    (<https://github.com/cisarik/bookradar/actions/runs/43485796198>), workflow
    `verify`, event `push`, head SHA
    `2281982f7dae0ef1f582d294592c41281ba11b21`, status `completed`, conclusion
    `success`, created `2026-11-13T18:46:01Z`, updated `2026-11-13T18:46:39Z`.
  - `.ap` gitlink and detached submodule `HEAD` both
    `d7023cf037f6d17885c3ede5c04812c61640da50`; submodule clean; strict
    `./.ap/ap doctor` PASS; resolved governing variant `stable`.
  - Toolchain verified: `rustc 1.99.1 (58cf8f9c3 2026-10-13)`,
    `cargo 1.99.1 (5f94df478 2026-08-27)`.
  - `bash scripts/verify.sh` executed directly by the Orchestrator: exit 0;
    **94 tests passed** (`17` core in `tests/verification.rs`, `10` store unit in
    `crates/bookradar-store/src/{store,research}.rs` (`7`+`3`), `4` observation
    CLI, `13` history, `6` persistence, `2` research CLI, `5` research contract,
    `20` research ingestion, `3` UI CLI, `6` UI HTTP, `8` UI render; `0`
    doc/bin tests); `fmt`, `clippy -D warnings`, one-line `bookradar-core`
    dependency tree, `git diff --check`, strict `./.ap/ap doctor`, and the
    post-run clean-worktree check all passed.
  - Accepted product contract `docs/domain-contract.md` revision 1 (accepted
    2026-11-10), wire reference `docs/research-input-v1.md`, and ADRs `0001`–`0007`
    verified present. No upgrade ledger is declared in root `AGENTS.md` outside
    the managed AP block.
  - Predecessor closure
    `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_closure.md`
    SHA-256 `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`
    verified; its public commit, CI run, 94-test count, AP pin, and
    `closed-by-ORCHESTRATOR` status match the handout.
  - Activated Meta trace verified through `/Users/agile/meta/README.md`. Meta
    worktree currently contains unrelated owner changes under other projects;
    none were read as authority, modified, staged, or committed. Meta Git
    remains COOPERATOR-owned.
- Handout revalidation record:

```text
Handout revalidation: projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md
Received handout status: provisional
Revalidated against: 2281982f7dae0ef1f582d294592c41281ba11b21; AP d7023cf037f6d17885c3ede5c04812c61640da50; CI run 43485796198; contract revision 1; ADRs 0001–0007; predecessor closure SHA-256 77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f
Usable facts: public/local commit 2281982f7dae0ef1f582d294592c41281ba11b21, parent a2182302de73cb345b4b646993a1ad25d602555f, tree b6e2e169a3670d07a1e16afcaeddd50d368a72d6; public/local branch equality and clean worktree; public CI run 43485796198 conclusion success; 94 passing tests and scripts/verify.sh gate; AP pin d7023cf037f6d17885c3ede5c04812c61640da50, detached clean submodule and strict ap doctor PASS; Rust 1.99.1 toolchain; accepted domain contract revision 1, research-input-v1, and ADRs 0001–0007; Store::append_review present only in library/tests; bookradar-poc four-command fixed-fixture surface and bookradar-research four-command surface; bookradar-ui hardcoded synthetic_offer() while other query flags are configurable; absence of review, reconciliation, promotion, or live-ingestion surfaces
Stale facts and corrections: none
Not revalidated: active external Worker sessions outside this trace (not observable from repository state); COOPERATOR confirmation of the bounded objective and first-Planner delivery route (Stage 2 pending); Meta Git archival timing for this whole (COOPERATOR-owned; inspected read-only only)
Handout disposition: adopted
```

- Stage 2 status: restored state and the review/promotion gap were presented to
  the COOPERATOR. The COOPERATOR selected
  `bookradar-review-and-promotion-workflow` and selected manual delivery for the
  first Planner, with actual Native Plan Mode ON.
- COOPERATOR delivery/persistence decision (explicit, 2026-11-14): the
  Orchestrator is authorized to write every prompt to Meta; copy/paste is not
  the COOPERATOR's preferred workflow. Workers are to be instructed to write
  their own reports directly as Markdown files at the exact Meta report path.
  Manual delivery remains the selected route, but by prompt-file pointer rather
  than full-prompt copy/paste. This decision changes persistence ownership, not
  task authority or native-mode requirements.
- First Planner delivery record updated accordingly: prompt persistence owner
  `ORCHESTRATOR`; report persistence owner `assigned WORKER`; Git publication
  owner `COOPERATOR`; archival `wait-for-report`; the Worker receives
  `Trace persistence: direct-write` authority only for
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_report_00.md`
  and must not write any other Meta path. If native Plan Mode blocks the write,
  the Worker keeps the complete report in the plan output and writes it once the
  client permits within the same unexpired grant; if it remains blocked, the
  report returns in-session with a truthful delivery limitation.
- No Planner prompt had been issued before this decision. The first Planner
  prompt is being prepared as `01_planning_00.md`; no implementation, browser,
  dependency, Git, publication, acceptance, or closure authority is granted.
- Active mutation: none.

## 2026-11-14 — First Planner prompt prepared (`01_planning_00.md`)

- Prompt `01_planning_00.md` prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_planning_00.md`:
  SHA-256 `6547216bbc79798733fc6d4fb67b9bb505eb235cf3a56f828617c5aec9d1e922`;
  666 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `01`, exchange `01`; `fresh-worker-session`; `Native planning mode:
  required`; profile `Planner`; phase `planning`; task identity
  `BOOKRADAR-REVIEW-PROMOTION-PLAN`; reasoning High; approximately 250k
  context; plan disposition `approval-gated`; initial planning cycle; automatic
  targeted revisions used `0`.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR`; archival
  `wait-for-report`; trace persistence `direct-write` only for
  `.../01_report_00.md`. The report destination did not exist at preparation.
- Delivery route: manual, by prompt-file pointer. The COOPERATOR opens a fresh
  session with actual Native Plan Mode ON and points the Worker at the prompt
  file; the full prompt is not copy/pasted. The Worker writes its own report
  directly. If native Plan Mode blocks the report write, the Worker keeps the
  complete report in the plan output and writes it once the client permits
  within the same unexpired grant, or returns it in-session with a truthful
  delivery limitation.
- Authority: read-only planning only. No implementation, browser, dependency,
  Git, publication, acceptance, closure, or Meta Git authority is granted. The
  prompt itself grants no implementation authority.
- Active mutation: none.

## 2026-11-14 — Planner report received; companion integrity PASS; plan reconciled; decision gate

- `01_report_00.md` received at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_report_00.md`:
  SHA-256 `e08189f9534208d4f1dee91d289014d536cad88327236691a9deb8a68e9ecc22`;
  323 lines. Header exact; coordinates `01/01`; `status: PASS`;
  `Phase-qualified result: not-applicable`; start/end commit
  `2281982f7dae0ef1f582d294592c41281ba11b21`; changed repository files `none`;
  `Report justification: new-evidence`; `Logical-whole closure: not-closed`.
  It echoes prompt SHA-256 `6547216b…`, handout SHA-256 `ea5985ff…`, and
  predecessor closure SHA-256 `77332b58…`; all match. Native planning mode was
  observed active at start. Repository remains clean at `2281982f…`.
- Companion integrity: PASS. The report records that its own file readback
  occurred only after native Plan Mode permitted the write, so the report text
  pre-dates its self-readback. The Orchestrator has now read the complete saved
  file and verified its first line, coordinates, status, and SHA-256. Delivery
  is verified at the Orchestrator boundary; this is a delivery-order note, not a
  content defect.
- Plan summary: add `bookradar-review` in `bookradar-store` with exactly
  `show`, `promote`, and `review`; add `ResearchStore::candidate` and
  `promotion.rs`; keep both schemas, `bookradar-core`, both existing CLIs, and
  `Cargo.toml`/`Cargo.lock` unchanged; promote only fully reviewer-attested
  positive claims with `DirectBrowser` or `Manual` evidence; use
  `research:<producer>/<run>/<finding>@<receipt>/<position>` provenance; append
  human review revisions only to `0x42524452`; add UI `--source-id`/`--offer-id`
  defaulting to `1/1`; 17 proposed new tests (expected 111 total, not claimed
  until run); E2 with separate fresh independent audit; 14-path allowlist;
  ADR 0008 and README; one local commit
  `feat: add a governed research review and promotion path`.
- Reconciliation: plan accepted as decision-ready; no targeted revision is
  needed for the plan's core. The following carry-forward corrections must be
  encoded in any implementation grant:
  1. §11 says "six decision cells" while the table has nine. The COOPERATOR
     decision gate covers all nine rows.
  2. `incomplete_attestation_writes_nothing` includes a stale-timestamp case
     that is expected to write a historical row. Split or rename it so the
     writes-nothing test covers only refusal cases and the stale case is named
     truthfully (for example `stale_observation_is_stored_but_not_eligible`).
  3. Add a trust-boundary test for the handout's "promotion/review" wording:
     a `Supported` review revision on an `AgentOnly` application observation
     must remain `NotEligible`; the kernel already enforces this, but the plan's
     proposed tests cover only promotion refusal.
  4. ADR 0008's `Status`/`Date` must reflect the COOPERATOR's actual decision
     date; do not pre-date acceptance.
  5. The recommended `promote` command records only reviewer-attested positive
     claims (`readable`, `present`, `available`, Slovak, resolved edition). It
     does not add a reviewer-attested negative/unavailable or AgentOnly
     historical promotion path; a stale positive claim is stored as historical
     but not eligible. This scope must be explicit in the COOPERATOR decision.
- Material decision table: nine rows, each with a recommendation and a blank
  COOPERATOR cell. Presented to the COOPERATOR; no implementation authority is
  granted. If the COOPERATOR selects an option other than the recommendation
  for a row that changes the designed surface, the one permitted targeted
  revision may be required before implementation.
- Active mutation: none.

## 2026-11-14 — COOPERATOR approved all nine; implementation grant prepared (`01_implementation_01.md`)

- COOPERATOR decision: approved all nine recommended rows and authorized
  preparation of the implementation grant. Implementation itself remains a
  separate Worker exchange and requires delivery to the exact current session.
- Implementation prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_implementation_01.md`:
  SHA-256 `04747fbabb2d9d7973943b7be3a419fdb54af735d4eda60eb73cf86dc3957926`;
  416 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `01`, exchange `02`; `current-worker-session`; `Native planning mode:
  not-used`; profile `Implementation Worker`; phase `implementation`; task
  identity `BOOKRADAR-REVIEW-PROMOTION-IMPLEMENT`; reasoning High; approximately
  250k context; exact baseline `2281982f…`; 14-path allowlist; one local commit;
  19 new tests expected (113 total, not claimed until run).
- Approved decisions bound: new `bookradar-review` with `show`/`promote`/`review`;
  full positive attestation only; research ledger read-only with `candidate`;
  caller-supplied observation ids; UI `--source-id`/`--offer-id` default 1/1 and
  poc unchanged; E2 with separate fresh audit and browser verification;
  disputed admitted findings allowed; same finding with a new observation id
  allowed; policy refusals exit 1 with stable categories.
- Reconciliation corrections bound: nine decision rows, split
  `incomplete_attestation_writes_nothing` from the stale-timestamp write, add
  `supported_review_keeps_agent_only_not_eligible`, ADR 0008 dated 2026-11-14,
  and the positive-only scope.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR`; archival
  `wait-for-report`; trace persistence `direct-write` only for
  `.../01_report_01.md`. The report destination did not exist at preparation.
- Delivery route: manual, by prompt-file pointer, to the exact current Worker
  session `01` with Native Plan Mode OFF. If that session is unavailable, do not
  deliver this grant elsewhere; a fresh-session `02/01` implementation grant is
  required.
- Authority: one local commit `feat: add a governed research review and
  promotion path`; no push; no browser; no acceptance; no publication; no Meta
  Git. The Worker writes only the exact report path in Meta.
- Active mutation: none until the implementation Worker begins.

## 2026-11-14 — Implementation report received; direct verification; one documentation correction

- `01_report_01.md` received at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_report_01.md`:
  SHA-256 `030f8955a7a2b116a647ed6d47489ddf59bde23483b3f6e0e0a459e21642bf8c`;
  35 lines. Header exact; coordinates `01/02`; `status: PASS`;
  `Phase-qualified result: implementation-PASS`; start commit `2281982f…`; end
  commit `69ec45e245108c90e2de4302c03ca72572bf1829`; prompt SHA-256
  `04747fba…` matches; `Git result: one local commit ... no push`;
  `Logical-whole closure: not-closed`. Native Plan Mode was not-used.
- Direct Orchestrator verification of candidate `69ec45e…`:
  - `bash scripts/verify.sh` exit `0`; `cargo test` sum **113 passed, 0
    failed**; `cargo tree -p bookradar-core` is one line; strict
    `./.ap/ap doctor` PASS; clean worktree.
  - The commit changes exactly the 14 allowlist paths; `Cargo.toml`,
    `Cargo.lock`, `src/**`, both schemas, `docs/domain-contract.md`,
    `docs/research-input-v1.md`, ADRs `0001`–`0007`, `scripts/verify.sh`,
    the workflow, `rust-toolchain.toml`, `.gitignore`, and `.ap` are unchanged.
  - Local `main` is one commit ahead of `origin/main`; public
    `refs/heads/main` is still `2281982f…`; no push, tags, or extra refs.
  - Source spot-check: `promotion.rs` refuses `AgentOnly` with
    `agent-only-evidence`, requires the full positive attestation, opens the
    application store only after candidate/attestation success, writes one
    `Store::append` transaction, and uses
    `research:<producer>/<run>/<finding>@<receipt>/<position>` provenance.
    `ResearchStore` gains only a read-only `candidate` query; `review` appends
    only to the application store; UI flags keep `OpenMode::ReadOnly`. The
    `supported_review_keeps_agent_only_not_eligible`, stale-row split, and
    conflict-clearing tests are present. ADR 0008 records the nine approved
    cells, accepted 2026-11-14, positive-only scope.
- Reconciliation: non-independent `implementation-PASS` is accepted for the
  code and gate evidence. One **documentation deviation** remains: the README's
  "Governed review and promotion" demo imports, shows, promotes, appends a
  `disputed` review, and opens the UI, but it does not demonstrate the
  approved plan §10 sequence "a second observation used only to show `review`
  clearing a conflict." The library test
  `rejected_revision_clears_equal_time_conflict` covers the behavior, but the
  README does not. The `--position 0`/receipt `0` note is a correct
  clarification of the plan's imprecise identifier sentence, not a defect.
- Smallest correction: one README-only exchange (`01/03`) adding the second
  observation and the `review --knowledge rejected` conflict-clearing sequence,
  then one local commit on top of `69ec45e…`. This is documentation-only inside
  the original allowlist; the primary independent audit will target the
  corrected candidate. If the COOPERATOR prefers to accept the README
  limitation and audit `69ec45e…` directly, record that decision and add the
  limitation to the acceptance and closure records.
- Audit remains separate: `Fresh Independent Audit`, fresh session `02`,
  exchange `01`, Playwright/Chromium for the UI, E2. No acceptance,
  publication, or closure authority is granted.
- Active mutation: local candidate `69ec45e245108c90e2de4302c03ca72572bf1829`
  only; no push.

## 2026-11-14 — README correction prompt prepared (`01_correction_02.md`)

- Orchestrator preflight of the proposed conflict-clearing sequence on candidate
  `69ec45e…`: imported `newer.json`; promoted observation `1` edition `10` at
  `1793548100`; promoted the same finding as observation `2` edition `11` at the
  same instant; `bookradar-poc current 1793548800` reported
  `conflict=unresolved` / `Unverified -- unresolved conflict`; `bookradar-review
  review` on observation `2` with `--knowledge rejected --expected-revision 1`
  at `1793548750` returned revision `2`; the next `current` reported
  `conflict=clear` / `Checked available -- unix:1793548100;
  expires_unix=1793634500`; history showed observation `1` supported and
  observation `2` rejected. The sequence is feasible with the approved CLI and
  does not require a code or policy change.
- Correction prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_correction_02.md`:
  SHA-256 `2f921c3b3c945a84221d2c8de481fa577e86860a62af0338a37cbc2bef49d559`;
  274 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `01`, exchange `03`; `current-worker-session`; `Native planning mode:
  not-used`; profile `Bounded Correction Worker`; phase `correction`; task
  identity `BOOKRADAR-REVIEW-PROMOTION-README-CORRECTION`; reasoning Medium;
  exact baseline `69ec45e…`; `README.md` only; one local corrective commit
  `docs: demonstrate governed conflict resolution`; no push; 113-test gate on the
  clean committed candidate.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR`; archival
  `wait-for-report`; trace persistence `direct-write` only for
  `.../01_report_02.md`. The report destination did not exist at preparation.
- Delivery route: manual, by prompt-file pointer, to the exact current Worker
  session `01` with Native Plan Mode OFF. If that session is unavailable, do not
  deliver elsewhere; a fresh correction grant is required.
- After the correction, the primary fresh independent audit remains `02/01` on
  the corrected candidate tip. If the COOPERATOR instead accepts the README
  limitation and audits `69ec45e…` directly, that limitation must be recorded in
  the acceptance and closure records.
- Active mutation: local candidate `69ec45e…` only; no push.

## 2026-11-14 — Correction report received; direct verification; fresh audit prepared

- `01_report_02.md` received at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_report_02.md`:
  SHA-256 `f08aee0b9c4da4a1d53c5ddfd0021821db634ed5c88f8efbfef3c9daae6a8108`;
  39 lines. Header exact; coordinates `01/03`; `status: PASS`;
  `Phase-qualified result: implementation-PASS`; start commit `69ec45e…`; end
  commit `80b172c2db6fcacc93041d4eb4c246450547f112`; changed files `README.md`
  only; prompt SHA-256 `2f921c3b…` matches; `Git result: one local corrective
  commit ... no push`; `Logical-whole closure: not-closed`.
- Direct Orchestrator verification of candidate `80b172c…`:
  - `bash scripts/verify.sh` exit `0`; `cargo test` sum **113 passed, 0
    failed**; strict `./.ap/ap doctor` PASS; clean worktree.
  - The correction commit `80b172c…` changes only `README.md` (49 insertions,
    10 deletions). The final diff from baseline `2281982f…` remains exactly the
    14 approved paths.
  - Local `main` is two commits ahead of `origin/main`; public
    `refs/heads/main` is still `2281982f…`; no push, tags, or extra refs.
  - README now demonstrates the second promotion (same finding, observation 2,
    edition 11, same observed instant), the unresolved conflict, the
    `review --knowledge rejected --expected-revision 1` revision, the cleared
    conflict, and the checked-available UI state. The previous disputed review
    on observation 1 was removed so the demo ends resolved.
- Reconciliation: the documentation finding is resolved. Candidate
  `80b172c2db6fcacc93041d4eb4c246450547f112` is the frozen acceptance candidate.
- Next: fresh independent audit `02/01`, `Fresh Independent Audit`, independent
  session `02`, `Native planning mode: not-used`, candidate `80b172c…`,
  Playwright/Chromium for the UI, report `02_report_00.md`. No acceptance,
  publication, or closure authority is granted yet.
- Active mutation: local candidate `80b172c…` only; no push.

## 2026-11-14 — Fresh independent audit prompt prepared (`02_acceptance_00.md`)

- Audit prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/02_acceptance_00.md`:
  SHA-256 `ffdea5259956cb521dede5b46d04e1138a4fe8faff41934a507797157baebf98`;
  398 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `02`, exchange `01`; `fresh-worker-session`; `Native planning mode:
  not-used`; profile `Fresh Independent Audit`; phase `Independent Audit`; task
  identity `BOOKRADAR-REVIEW-PROMOTION-ACCEPTANCE`; reasoning High; approximately
  250k context; independence required `yes`; acceptance candidate
  `80b172c2db6fcacc93041d4eb4c246450547f112`; 14-path acceptance allowlist;
  control matrix C1–C17; Playwright/Chromium browser controls for `1280×800` and
  `375×812`.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR`; archival
  `wait-for-report`; trace persistence `direct-write` only for
  `.../02_report_00.md`. The report destination did not exist at preparation.
- Independence: the audit must be a genuinely fresh session, with this grant as
  its first input, no implementation participation, and no inherited parent
  conversation. The candidate is frozen; the auditor must not correct or
  self-certify a correction.
- Authority: read-only repository; loopback CLI/browser probes and exact
  temporary roots under ignored `target/`; no commit, push, dependency, external
  network, or Meta write outside the report.
- Active mutation: local candidate `80b172c2db6fcacc93041d4eb4c246450547f112`
  only; no push.

## 2026-11-14 — Independent audit received; C1–C15/C17 PASS; C16 blocked; COOPERATOR decision

- `02_report_00.md` received at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/02_report_00.md`:
  SHA-256 `5286deaeb6a28ab5d8d7ab35829eecde21a52f16894b22807e2b017083012f8f`;
  251 lines. Header exact; coordinates `02/01`; `status: BLOCKED`;
  `Phase-qualified result: not-applicable`; acceptance candidate
  `80b172c…`; start/end commit `80b172c…`; prompt SHA-256 `ffdea525…` matches;
  independence attested; `Logical-whole closure: not-closed`.
- Audit result: C1–C15 and C17 PASS on directly observed evidence. The canonical
  gate exited 0 with **113 tests**, one-line core tree, strict `ap doctor` PASS,
  and clean worktree. The CLI/library/SQLite/loopback-HTTP probes covered the
  trust boundary, closed outcomes, disputed admission, duplicate rollback,
  same-finding/new-observation, conflict clearing, review concurrency, UI
  flags, exit codes, and read-only integrity. C16 is **NOT-VERIFIED**:
  Playwright/Chromium is absent (`npx --no-install` missing
  `playwright@1.65.1`; Python has no `playwright` module; the Playwright cache
  has no Chromium browser directory). Browser launch count 0; no viewport,
  console, or browser-network evidence. Loopback HTTP text/header checks were
  recorded but do not replace the rendered session. The Browser Stall Guard
  triggered with a conclusive adapter-absent failure; the audit correctly did
  not claim acceptance PASS.
- Independent verification of the blocker: `node`/`npm`/`npx` are present;
  `playwright` is not installed; `~/Library/Caches/ms-playwright` has no
  Chromium browser directory; `/Applications/Google Chrome.app` is present but
  was not used as a substitute. Installing Playwright or fetching Chromium is
  outside the audit grant.
- Extra local refs: eight `refs/codex/turn-diffs/checkpoints/*` tree refs from
  the Codex harness exist beside `refs/heads/main` and
  `refs/remotes/origin/main`. They are not tags, branches, or remote refs, and
  are not part of the acceptance candidate. Do not delete, move, or publish
  them without exact authority; a normal publication pushes only
  `HEAD:refs/heads/main`.
- Reconciliation: `BLOCKED` is correct. The Orchestrator accepts C1–C15/C17 as
  independent evidence but cannot accept the missing C16. No product defect or
  repository correction is indicated by the audit. The only routes are:
  1. provision a local Playwright/Chromium adapter outside the repository and
     run one targeted fresh browser-only probe for C16 (`03/01`);
  2. obtain an explicit COOPERATOR amendment of the frozen browser expectation
     and record C16 as a named acceptance limitation; or
  3. defer acceptance/publication until an adapter is available.
- No acceptance, publication, or closure authority is granted. Active mutation:
  local candidate `80b172c…` only; no push.

## 2026-11-14 — COOPERATOR authorized Playwright provisioning; C16 probe prepared

- COOPERATOR decision: provision the Playwright adapter in a temporary
  environment outside the repository and run one targeted fresh browser-only
  probe for C16. No repository dependency, no code change, candidate remains
  `80b172c2db6fcacc93041d4eb4c246450547f112`.
- Probe prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/03_browser_00.md`:
  fresh Worker session `03`, exchange `01`, `fresh-worker-session`,
  `Native planning mode: not-used`, profile `Fresh Evidence Probe`, phase
  `Independent Audit`, task identity `BOOKRADAR-REVIEW-PROMOTION-C16-BROWSER`,
  reasoning Medium, candidate `80b172c…`, report `03_report_00.md`.
- Authorized host mutation: one exact temporary root under the approved temp
  directory; install only `playwright@1.65.1` via npm; use the installed Chrome
  channel first, with a temp Chromium fallback if needed; loopback browser only.
  No repository dependency, no repository edit, no commit, no push.
- The probe re-verifies candidate identity and produces C16 only; C1–C15/C17
  remain the accepted independent audit evidence from `02_report_00.md`. The
  final acceptance verdict remains Orchestrator/COOPERATOR.
- Active mutation: local candidate `80b172c…` only; no push.

## 2026-11-14 — C16 browser probe prompt prepared (`03_browser_00.md`)

- Probe prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/03_browser_00.md`:
  SHA-256 `5a79fe7c78bcb810edf38058ed392a9ac65f5126b6fa062286edbfd476193fb4`;
  355 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `03`, exchange `01`; `fresh-worker-session`; `Native planning mode:
  not-used`; profile `Fresh Evidence Probe`; phase `Independent Audit`; task
  identity `BOOKRADAR-REVIEW-PROMOTION-C16-BROWSER`; reasoning Medium; candidate
  `80b172c…`; report `03_report_00.md`.
- Authorized adapter: one exact temp root under
  `/private/var/folders/93/7fg3d5j17wxdkyh6nlyz239m0000gn/T/opencode/`; only
  `playwright@1.65.1` installed there; installed Chrome channel first; optional
  temporary Chromium fallback into the same root; loopback browser only; full
  cleanup. No repository dependency, edit, commit, or push.
- Scope: C16 only, states A–D (first promotion, conflict, rejection, non-default
  offer), both viewports, HTTP/headers, console/pageerror/network, Browser Stall
  Guard, cleanup. C1–C15/C17 are not re-audited.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR`; archival
  `wait-for-report`; trace persistence `direct-write` only for
  `.../03_report_00.md`. The report destination did not exist at preparation.
- After the probe: Orchestrator combines C1–C15/C17 with C16 and presents the
  acceptance sign-off. Publication remains a separate authority.
- Active mutation: local candidate `80b172c…` only; no push.

## 2026-11-14 — C16 probe PASS; acceptance package complete; COOPERATOR sign-off

- `03_report_00.md` received at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/03_report_00.md`:
  SHA-256 `2f1d3df2a889e6d00b1d4daaaf7131cb94e886be4353ff1e0ccaca4342047743`;
  199 lines. Header exact; coordinates `03/01`; `status: PASS`;
  `C16: PASS`; candidate `80b172c…`; start/end commit `80b172c…`; prompt
  SHA-256 `5a79fe7c…` matches; independence attested; temporary root removed;
  `Logical-whole closure: not-closed`.
- C16 evidence: Playwright `1.65.1` installed only in the temporary root; Chrome
  channel `157.0.8103.39`; 2 browser launches; 8 contexts covering states A–D at
  `1280×800` and `375×812`. State A checked-available; state B unresolved
  conflict; state C rejection and cleared conflict with both revisions; state D
  `source 2, offer 7`. Each state showed the research candidate as
  `unreviewed`/`agent-only`/`not-eligible`. HTTP controls: GET/HEAD 200 on `/`
  and `/style.css`, POST 405, `/api` 404, required security headers present.
  Empty console and page-error lists; exactly two loopback requests per page; no
  external network; no `<script`/`<form>`; no screenshots. Mobile nested table
  scroll was contained and did not widen the document. Browser Stall Guard:
  not-triggered.
- Combined acceptance: C1–C15/C17 PASS in `02_report_00.md` plus C16 PASS in
  `03_report_00.md`; no findings. Recommendation: `acceptance-PASS` for candidate
  `80b172c…` with `Named missing-evidence probe: C16 rendered browser evidence`
  completed. Residual notes: browser evidence is Chrome-only, not Safari/Firefox;
  eight Codex checkpoint tree refs remain harness-local and are not part of the
  candidate or public refs; Meta Git remains COOPERATOR-owned.
- COOPERATOR acceptance sign-off is pending. Publication is a separate authority
  and is not granted. Active mutation: local candidate `80b172c…` only; no push.

## 2026-11-14 — COOPERATOR acceptance sign-off; publication grant prepared (`04_publication_00.md`)

- COOPERATOR decision: accepted candidate
  `80b172c2db6fcacc93041d4eb4c246450547f112` as `acceptance-PASS` and authorized
  preparation of a separate publication grant. Publication still requires its
  own delivery and execution.
- Acceptance record: C1–C15 and C17 PASS in independent audit `02_report_00.md`;
  C16 PASS in fresh probe `03_report_00.md`; no findings; `acceptance-PASS` for
  `80b172c…`; named missing-evidence probe completed; primary fresh acceptance
  used `1`; automatic corrections used `0`; correction re-acceptance
  `not-applicable`. Residual notes: browser evidence is Chrome-only, not
  Safari/Firefox; eight Codex checkpoint tree refs are harness-local and not part
  of the candidate or public refs; Meta Git remains COOPERATOR-owned.
- Publication prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/04_publication_00.md`:
  fresh Worker session `04`, exchange `01`, `fresh-worker-session`,
  `Native planning mode: not-used`, profile `Fresh Publication Worker`, phase
  `publication`, candidate `80b172c…`, one normal non-force fast-forward push of
  `refs/heads/main`, direct public readback, and CI observation; report
  `04_report_00.md`.
- Publication scope: no file edit, no rebase, no force, no tags, no extra refs,
  no `.ap` update; push only `HEAD:refs/heads/main`; do not push the
  `refs/codex/turn-diffs/checkpoints/*` refs. No closure authority.
- Active mutation: local candidate `80b172c…`; public `main` still
  `2281982f…`; no push yet.

## 2026-11-14 — Publication prompt prepared (`04_publication_00.md`)

- Publication prompt prepared at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/04_publication_00.md`:
  SHA-256 `9be324491b72c10e499a32894a57a55fca461e539d4a6be52856f7077c9163c4`;
  244 lines.
- Coordinates: logical whole `bookradar-review-and-promotion-workflow`, Worker
  session `04`, exchange `01`; `fresh-worker-session`; `Native planning mode:
  not-used`; profile `Fresh Publication Worker`; phase `publication`; task
  identity `BOOKRADAR-REVIEW-PROMOTION-PUBLISH`; reasoning Medium; publication
  candidate `80b172c…`; expected public base `2281982f…`; report
  `04_report_00.md`.
- Authority: exactly one normal non-force fast-forward push
  `git push --no-follow-tags origin HEAD:refs/heads/main` from `2281982f…` to
  `80b172c…`; direct public readback; read-only CI observation. No file edit,
  commit, amend, rebase, force, tags, extra refs, `.ap` update, or closure.
  The `refs/codex/turn-diffs/checkpoints/*` harness refs are not pushed.
- Delivery record: prompt persistence owner `ORCHESTRATOR`; report persistence
  owner `assigned WORKER`; Git publication owner `COOPERATOR` (trace Git);
  archival `wait-for-report`; trace persistence `direct-write` only for
  `.../04_report_00.md`. The report destination did not exist at preparation.
- After publication: Orchestrator reconciles the public readback and CI run, then
  decides whether closure prerequisites are satisfied. Closure is separate.
- Active mutation: local candidate `80b172c…`; public `main` `2281982f…`; no push
  yet.

## 2026-11-14 — Publication PASS; closure authored and notes frozen

- Final publication report `04_report_00.md` received and fully re-read at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/04_report_00.md`:
  SHA-256 `f12f4bdaa751195e2ef03208277f1705d53bb575e8fb99fa9b389fe6693c2066`;
  128 lines. Coordinates `04/01`; `status: PASS`;
  `Phase-qualified result: publication-PASS`; candidate `80b172c…`; prompt
  SHA-256 `9be32449…` matches; one normal non-force fast-forward push
  `2281982..80b172c`, no tags, no extra refs; `Logical-whole closure:
  not-closed`. The final saved file and the public API agree on CI run
  `43600404485`; an intermediate first-read artifact differed and was not used
  for the closure verdict. The Orchestrator did not edit the Worker report.
- Direct public readback, independently verified: `refs/heads/main` and symbolic
  `HEAD` both `80b172c2db6fcacc93041d4eb4c246450547f112`; public commit parent
  `69ec45e…`, tree `578fbe8…`, subject `docs: demonstrate governed conflict
  resolution`. Local `HEAD`, `main`, and `origin/main` agree, `+0 -0`, worktree
  clean. The authorized push updated the local remote-tracking ref; the candidate
  was not modified.
- Independent CI readback through GitHub API: run `43600404485`
  (<https://github.com/cisarik/bookradar/actions/runs/43600404485>), workflow
  `verify`, event `push`, head SHA `80b172c…`, status `completed`, conclusion
  `success`, created `2026-11-14T13:34:00Z`, updated `2026-11-14T13:34:43Z`; job
  `132463717503` also completed `success`.
- Closure prerequisites reconciled: `implementation-PASS`, `acceptance-PASS`
  (C1–C15/C17 plus the named C16 fresh probe), `publication-PASS`; COOPERATOR
  objective/nine-cell/acceptance/publication/C16-provisioning decisions complete;
  residual-risk disposition complete; no active upgrade ledger; no active
  mutation. The required phase results precede closure.
- Closure `01_closure.md` authored at
  `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_closure.md`:
  SHA-256 `dc19ca8972d158345ddbf149f9f9978d982b6951b88394e4aa94ddb9787d73a2`;
  306 lines. Closure signal `closed-by-ORCHESTRATOR`. The opening filename
  exception `00_handout_00.md` is preserved and no competing `00_handout.md`
  was created.
- Notes are frozen at closure. No successor logical-whole grant exists; the next
  whole requires COOPERATOR selection and revalidation of mutable facts.
- Active mutation: none. Meta Git remains COOPERATOR-owned.
