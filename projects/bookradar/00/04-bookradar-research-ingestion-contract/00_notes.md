# BookRadar — `bookradar-research-ingestion-contract` — Notes

Orchestrator-authored. Not task authority.

> Recovered 2026-11-12 after the working-tree file went missing. Content reconstructed from Orchestrator-authored records; it is not claimed byte-identical to the lost working-tree file.

## 2026-11-11 — Whole opened; Stage 1 restoration and first Planner prepared

- Stage 2 selection: the COOPERATOR selected `bookradar-research-ingestion-contract` at `projects/bookradar/00/04-bookradar-research-ingestion-contract/`. Objective: establish one minimal, executable, versioned untrusted research-ingestion contract/pipeline that validates structural and invariant requirements, preserves producer/run/finding provenance, quarantines unsupported or malformed input, handles replay and conflicting payloads deterministically, and integrates with the accepted core/store only through explicitly assessed observations or candidates. It must never automatically promote agent output to a verified stock state. Live Hermes/Playwright, UI, NUC, real data, screenshots, accounts, deployment and policy selection remain excluded.
- Orchestrator routing: fresh per-whole Orchestrator (direct project checkout), `Orchestrator session scope: logical-whole`. Fresh Worker session `01`, exchange `01`, `Native planning mode: required`, Worker session profile `Planner`, reasoning recommendation High, approximately 250k context. One accountable Worker workstream; no second implementation worker.
- Delivery routing: the COOPERATOR selected manual delivery. An earlier selection of subagent dispatch was corrected to manual delivery before any prompt was issued; no Worker coordinates were consumed by that correction. The Orchestrator prepared the prompt in Meta; the complete report returns in-session and the COOPERATOR persists it.
- Baseline verified 2026-11-11: public `refs/heads/main` and symbolic `HEAD` = `c93f5262ca27050922cc658424c298913852eaff`; local `main`, `HEAD` and `origin/main` match; worktree clean; parent `bd23b08cd315a7b3c7a549479db59cbe6ad2adce`; tree `b2ad12353723009944521c15ac2016970337c1df`; `.ap` detached and clean at `d7023cf037f6d17885c3ede5c04812c61640da50`; strict `./.ap/ap doctor` PASS; Rust `1.99.1`; 45 tests pass (17 core + 7 store + 6 persistence + 13 history + 2 CLI); `cargo tree -p bookradar-core` contains only `bookradar-core`.
- Handout revalidation record:

```text
Handout revalidation: projects/bookradar/00/04-bookradar-research-ingestion-contract/00_handout.md
Received handout status: provisional
Revalidated against: c93f5262ca27050922cc658424c298913852eaff; AP d7023cf037f6d17885c3ede5c04812c61640da50; contract revision 1; ADRs 0001–0004; predecessor closure SHA-256 4811b847eac398a4ff735a1a54b2ba8fcb5f75fa4ed9868935ef98b2965c0dc9
Usable facts: baseline commit/parent/tree; public/local branch equality; clean worktree; AP pin, detached state and doctor PASS; accepted contract and ADRs; 45 passing tests; Rust 1.99.1; absence of research-envelope/validator/quarantine/replay implementation and research tables in schema v1
Stale facts and corrections: the handout says the late `02_rereport_00.md` remains under the Kronika trace -> no file named `02_rereport_00.md` exists under `/Users/agile/meta`; `projects/bookradar/00/03-bookradar-persistence-and-history-slice/02_report_00.md` now hashes 3d740181c3caacbaba8e09ef3f033a7e4852f80643b771fc0d2092edd4ee514e (the actual implementation report), and the earlier BLOCKED `02_report_00.md` hash 4ec92c2633f98e68f1f3d9439da89bd80741da1de4780bc986bd33ff3250bef7 is not separately present as a file; no file was changed by the Orchestrator
Not revalidated: real-world research or listing behavior and live Hermes/Playwright integration (out of scope for this whole and not claimed); the provenance and intended disposition of uncommitted Meta changes in the predecessor trace and the untracked new whole directory (Meta Git remains COOPERATOR-owned; inspected read-only only)
Handout disposition: adopted-with-corrections
```

- Trace: provisional handout SHA-256 `316ca28a302479db22f95c78f22f3ea467339a13f9b11aa26ceabb63e8e54ee2`. First planning prompt is `01_planning_00.md`, SHA-256 `e90d78c5913941523d523d9ee053cb4ec28b620eb674e4ed5021179b5593128b`; report returns in-session as `01_report_00.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner: COOPERATOR. Archival: wait-for-report. No Meta Git operation is authorized.
- Trace residual: the predecessor duplicate-report incident is preserved as historical evidence but its current file placement differs from the handout's description; do not rewrite or relocate it without a separate COOPERATOR decision. The new whole directory was untracked at opening; Meta Git remains COOPERATOR-owned.
- Planned boundary for the Planner: one minimal executable, versioned untrusted research-ingestion contract/pipeline with synthetic fixtures; explicit format, persistence/migration, replay-identity, dependency, core/store-integration and acceptance decisions surfaced to the COOPERATOR; no implementation in the planning exchange; no live Hermes/Playwright, UI, NUC, real data, screenshots, accounts, deployment or policy selection; no auto-promotion to verified stock.
- No implementation, dependency, Git, publication, acceptance or closure authority is granted by the opening or the planning prompt.
- Active mutation: none.

## 2026-11-11 — Planner report received; plan reconciliation and decision gate

- `01_report_00.md` received and read: status `PASS`, SHA-256 `4577cac5064c6a92e76ae55998f6679f95aeec2b1cae46ec72d932f54ab970c5`, 575 lines. Coordinates `01/01` and task identity match; it echoes the prompt hash `e90d78c5…` and handout hash `316ca28a…`. It is a plan artifact, not acceptance.
- Plan summary: strict JSON contract v1; separate SQLite research ledger (application id `0x42525249`, `user_version=1`); extend `bookradar-store` with `ResearchStore`/research modules; no new crate, no core dependency, no schema v2/migration; exact replay identity `(producer_id, run_id, finding_id)` plus canonical content bytes; ledger-local candidates only, no catalog resolution or application-store promotion; four commands and four fixtures; proposed serde `1.0.228` / serde_json `1.0.145`; E2 with fresh independent acceptance; one local candidate commit only when granted, no push before acceptance and a separate publication grant.
- The report claims two Cooperator selections made during planning: strict JSON and a separate SQLite research ledger. These remain pending explicit confirmation in the Orchestrator reconciliation before the plan is accepted.
- Proposed rows requiring Cooperator decision: extend `bookradar-store`; exact identity plus canonical-bytes replay; ledger-local candidates only; exact serde pins and later provisioning; four commands/four fixtures; wire reference plus ADR 0005; E2 plus fresh independent acceptance; local candidate/commit boundary.
- Minor plan clarifications to bind in the implementation grant if accepted: add `source_provenance` to the exact finding field list; map “unassessed coverage” to exact `ClaimCoverage` `Covered`/`Missing` values; state that price is asking price only and defer shipping/fees/total/ranges; clarify the agent-only test fixture; clarify `reported_run_outcome` and the `research_inputs` canonical content key; state that the target `EditionId` is operator-supplied and not inferred from research.
- Process near-miss: the report self-discloses an initial filename search over broader Projects/Meta roots before the grant was fully parsed; it requested filenames only and used no unrelated contents. Recorded as a measured read-scope deviation; no plan defect or corrective write.
- Meta state: HEAD `ae7cbf2` contains the predecessor report fix (`02_report_00.md` updated, `02_rereport_00.md` deleted), confirming the handout’s stale placement narrative. The new whole directory and `01_report_00.md` remain untracked; no Meta Git operation was performed.
- No implementation, dependency, Git, publication, acceptance or closure authority is granted.
- Active mutation: none.

## 2026-11-12 — Plan accepted; implementation grant prepared

- COOPERATOR decision: the accepted plan `01_report_00.md` is approved, including strict JSON, the separate SQLite research ledger and all proposed rows: extend `bookradar-store`; exact identity plus canonical-bytes replay; ledger-local candidates only; exact serde `1.0.228` / serde_json `1.0.145` pins; four commands/four fixtures; wire reference plus ADR 0005; E2 plus fresh independent acceptance; one local candidate commit and no push.
- The six minor clarifications from the prior entry are binding in the implementation grant, not a new planning cycle. ADR 0005 records the Cooperator’s 2026-11-12 acceptance.
- Implementation grant: `01_implementation_01.md`, SHA-256 `3254e88614bc5870182cc2dbaf5e28db6ceffefbc5c5cd111adf4867def579a9`. Same Worker session `01`, exchange `02`, `current-worker-session`, `Native planning mode: not-used`, exact baseline `c93f526…`, eighteen-path allowlist, one local commit with subject `feat: add versioned research ingestion PoC`; no push.
- Delivery: manual COOPERATOR ferry to the exact Planner session. The report returns in-session as `01_report_01.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner: COOPERATOR. Archival: wait-for-report.
- If the Planner session is unavailable, this current-session grant must not be pasted into a different session; a fresh-session `02/01` grant is required instead.
- Plan acceptance is not implementation acceptance. Fresh independent acceptance, publication and closure remain separate.
- Active mutation: none until the Worker begins; no push is authorized.

## 2026-11-12 — Fresh implementation session selected; current-session grant undelivered

- The COOPERATOR reports that the Planner session which produced `01_report_00.md` is no longer available. The current-session implementation grant `01_implementation_01.md` (SHA-256 `3254e88614bc5870182cc2dbaf5e28db6ceffefbc5c5cd111adf4867def579a9`) could not be delivered. It remains in the trace as historical/undelivered evidence and grants no authority here. Coordinates `01/02` are consumed but were not delivered.
- Fresh routing: Worker session `02`, exchange `01`, `fresh-worker-session`, `Native planning mode: not-used`, Worker session profile `Fresh Implementation Worker`. This is a routing departure from the plan’s current-session preference because the session is unavailable; freshness is not an independence claim. The accepted plan and every technical decision are unchanged.
- Fresh grant: `02_implementation_00.md`, SHA-256 `4b56f9f589bbf87807294655acac1379de4578d2399ae0d6df6e93739a5f4bfd`.
- Delivery: manual COOPERATOR ferry to a genuinely fresh session with Native Plan Mode OFF. The report returns in-session as `02_report_00.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner: COOPERATOR. Archival: wait-for-report.
- The grant authorizes the same eighteen paths, exact serde pins, one authorized `cargo fetch`, the full gates, and one local commit with subject `feat: add versioned research ingestion PoC`; no push, no Meta writes, no acceptance, publication or closure.
- Active mutation: none until the fresh Worker begins; no push is authorized.

## 2026-11-12 — Second foreign report at `03_report_00.md`; delivery blocker

- `03_report_00.md` is byte-identical to the predecessor BLOCKED report: SHA-256 `4ec92c2633f98e68f1f3d9439da89bd80741da1de4780bc986bd33ff3250bef7`, logical whole `bookradar-persistence-and-history-slice`, task `BOOKRADAR-PERSISTENCE-HISTORY-IMPLEMENTATION`, baseline `bd23b08…`, status `BLOCKED`.
- BookRadar remains at `c93f5262ca27050922cc658424c298913852eaff`, clean; reflog shows no new commit; no research source or binary. The implementation candidate does not exist.
- The same foreign report has now been saved for both `02/01` and `03/01`. This is a report-delivery/persistence failure, not an implementation outcome. `03/01` is not accepted.
- Stop issuing new implementation grants until the causal delivery problem is resolved. The smallest correction is for the COOPERATOR to paste the complete actual report text from the `03` session, or to confirm that the `03` session never ran and re-deliver `03_implementation_00.md` to a genuinely new session without first creating a report file.
- Do not overwrite the two foreign report files; they are preserved as trace/incident evidence. A `04/01` grant is not authorized yet.
- No implementation, acceptance, publication or closure authority is granted.
- Active mutation: none.

## 2026-11-12 — File-naming correction; implementation session outcome still unknown

- The COOPERATOR clarified that the misnamed `03_acceptance_00.md` was the predecessor `bookradar-persistence-and-history-slice` acceptance prompt, not a report for this whole. It is now present in the predecessor trace as `03_acceptance_00.md` (SHA-256 `6895c3258f2770991de57414d53ec6f101312dcd5574e8124b78a4d607692f51`); that is historical evidence and Meta Git remains COOPERATOR-owned.
- `03_report_00.md` in this whole remains the predecessor BLOCKED report (`4ec92c26…`), not a new implementation report.
- It is still unknown whether a genuinely new session received and ran `03_implementation_00.md`. If it did not run, the existing `03/01` prompt can be delivered now without a new grant; if it ran, its actual terminal report must be supplied. No `04/01` grant is authorized until that fact is established.
- BookRadar remains at `c93f526…`, clean, with no implementation commit, research source or binary.
- No implementation, acceptance, publication or closure authority is granted.
- Active mutation: none.

## 2026-11-12 — Trace naming audit; predecessor acceptance prompt restored

- Inspected the beginnings of every file in `projects/jelena/00/01-jelena-vegetation-detail/`. All headers match their filenames and ordinals; no rename is needed there.
- Found one unambiguous misnamed file in the predecessor BookRadar trace: `03_report_01.md` was the acceptance prompt for session `03`, exchange `01`, not a report. Renamed it to `03_acceptance_00.md`; SHA-256 `6895c3258f2770991de57414d53ec6f101312dcd5574e8124b78a4d607692f51`. This restores the tracked file; no Git commit was made.
- The current whole’s `02_report_00.md` and `03_report_00.md` are still copies of the predecessor BLOCKED report. They cannot be corrected by renaming because the content belongs to a different whole, task and baseline.
- Searched the Meta `projects` tree for the new whole identity and `BOOKRADAR-RESEARCH-INGESTION-IMPLEMENT`; only the prompts and notes contain them. No new implementation report exists anywhere in Meta.
- The `03/01` implementation session outcome therefore remains unknown: it either did not run or its report was never saved. No new grant is authorized until that fact is established.
- Active mutation: none.

## 2026-11-12 — Implementation candidate found and directly verified; report still missing

- BookRadar now has a real local implementation commit: `ed4de54637f22613723bc3df98536a1ac25d0800`, subject `feat: add versioned research ingestion PoC`, parent `c93f5262ca27050922cc658424c298913852eaff`, tree `92884838654a0a534d8f3e77120029542adc7f72`.
- The commit changes exactly the nineteen enumerated allowlist paths. The implementation prompt said “eighteen” while enumerating nineteen; that count was an Orchestrator prompt defect, not a Worker scope expansion. No root manifest, core source, `schema_v1.sql`, old CLI/fixtures, existing tests, contract, ADRs 0001–0004 or `.ap` changed.
- Direct Orchestrator verification on 2026-11-12: worktree clean, local `main` ahead 1, no push; 74 tests pass (17 core + 10 store unit + 6 persistence + 13 history + 2 CLI + 1 research CLI + 5 research contract + 20 research ingestion); build, fmt, clippy `-D warnings`, core tree, `git diff --check`, `git show --check` and strict `ap doctor` PASS.
- The synthetic demo matches the accepted plan exactly: init exit 0; partial import exit 3; identical replay exit 3; current before conflict exit 0; conflict import exit 3; current after conflict exit 0; inspect output matches. Research ledger reports application id `1112691273` (`0x42525249`), `user_version=1`, and the v1 plus research tables.
- The wire reference includes `source_provenance`, exact coverage values, asking-price scope, receipt-level `reported_run_outcome`, canonical-byte equality, operator-supplied target edition and producer identity. ADR 0005 is `Accepted 2026-11-12`.
- `03_report_00.md` is still the predecessor BLOCKED report (`4ec92c26…`); the actual implementation report has not been delivered. The report-delivery defect remains, but it does not invalidate the directly verified code candidate.
- Next decision: either proceed to a fresh independent acceptance with the missing report recorded as a process/trace defect, or wait for the actual implementation report. No acceptance, publication or closure is granted yet.
- Active mutation: local candidate commit only; no push.

## 2026-11-12 — Fresh independent acceptance prepared against `ed4de54`

- Implementation report `03_report_00.md` remains missing/foreign; the code candidate is real and directly verified. The COOPERATOR approved the plan’s E2 fresh-acceptance route. The missing report is recorded as a process/trace defect, not a code defect.
- Acceptance grant: `04_acceptance_00.md`, SHA-256 `78b65f3b236b22c152f28f8307491aa38cc7a672e5fa8b048e13632db231207a`. Fresh Worker session `04`, exchange `01`, `fresh-worker-session`, `Native planning mode: not-used`, Worker session profile `Fresh Independent Audit`, independence required.
- Candidate `ed4de54637f22613723bc3df98536a1ac25d0800`; parent `c93f5262ca27050922cc658424c298913852eaff`; tree `92884838654a0a534d8f3e77120029542adc7f72`; nineteen-path allowlist; public `main` remains `c93f526…`.
- The acceptance is read-only: no source, dependency, Git or Meta mutation and no push. Report returns in-session as `04_report_00.md` and is persisted by the COOPERATOR.
- The acceptance must independently verify the 74 tests, gates, exact demo, schema, replay/quarantine/projection and documentation; it must not rely on the missing implementation report.
- No publication or closure is granted.
- Active mutation: local candidate only; no push.

## 2026-11-12 — Acceptance report received; `acceptance-PASS`

- `04_report_00.md` received and read: SHA-256 `8dac6b2614e4aa54480d0f17ce94aad09a243b176cf98243e9675178f1c1cca6`, 147 lines. Coordinates `04/01`, candidate `ed4de54…`, `status: PASS`, `Phase-qualified result: acceptance-PASS`, changed files none, `Logical-whole closure: not-closed`. It is consistent with the Orchestrator’s direct candidate verification.
- The independent acceptance ran the 74 tests, full gates, exact CLI demo, fresh-ledger probes, schema/trigger checks, replay/conflict/older-import/partial-run cases and documentation review. It found no source, test, lockfile or documentation defect.
- It recorded the missing implementation report (`03_report_00.md` is the foreign predecessor BLOCKED report, SHA-256 `4ec92c26…`) as a process/trace defect, not a code defect. The acceptance was performed directly against Git, source, tests and a fresh CLI run.
- Acceptance PASS is accepted by the Orchestrator for candidate `ed4de54637f22613723bc3df98536a1ac25d0800`. Publication remains a separate Cooperator decision and is not authorized by this acceptance.
- Public `main` remains `c93f526…`; local `main` is one commit ahead; no push occurred.
- Active mutation: local candidate only; no push.

## 2026-11-12 — Publication grant prepared

- `acceptance-PASS` is accepted for `ed4de54637f22613723bc3df98536a1ac25d0800`; the COOPERATOR approved a separate publication grant.
- Publication grant: `05_publication_00.md`, SHA-256 `16d461b54a513043b643f28728056c02d16f9c8c62a7612764750df6d4f36db0`. Fresh Worker session `05`, exchange `01`, `fresh-worker-session`, `Native planning mode: not-used`, Worker session profile `Publication Worker`.
- Exact accepted candidate `ed4de54…`, parent `c93f526…`, tree `928848…`; expected public baseline `c93f526…`; one normal non-force `git push origin main`; direct public readback. No new commit, source change, force, rebase, Meta write or other ref.
- The grant requires the exact `04_report_00.md` acceptance identity (SHA-256 `8dac6b26…`) and stops if the candidate, acceptance or remote baseline differs.
- Report returns in-session as `05_report_00.md` and is persisted by the COOPERATOR. Prompt persistence owner: ORCHESTRATOR. Report persistence owner: COOPERATOR. Git publication owner: COOPERATOR. Archival: wait-for-report.
- No publication PASS or closure is granted yet. Remote `main` remains `c93f526…` until the Worker pushes.
- Active mutation: local candidate only; no push until the publication Worker begins.

## 2026-11-12 — Publication PASS; untracked `tests/target/` blocks a clean closure

- `05_report_00.md` received and read: SHA-256 `d7f8356f98f3bdd5a61ddd3d0b8d7ddc2eb3c7323271513df364f8c9d775df97`. Coordinates `05/01`, `status: PASS`, `publication-PASS`, candidate `ed4de54…`, changed files none, closure not-closed.
- Direct Orchestrator readback confirms public symbolic `HEAD` and `refs/heads/main` are `ed4de54637f22613723bc3df98536a1ac25d0800`; local `HEAD`, `main` and `origin/main` match; parent `c93f526…`, tree `928848…`; branch is `+0 -0`.
- Acceptance `04_report_00.md` SHA-256 `8dac6b26…`; publication `05_report_00.md` SHA-256 `d7f8356f…`.
- Closure check found an untracked `tests/target/` directory (about 390 MB) containing Cargo build outputs and synthetic SQLite demo stores. It is not part of the commit and is not covered by the current `.gitignore`. The acceptance/publication reports did not record it, so their clean-worktree claim is incomplete for that path.
- The directory appears to be generated acceptance/test output, not owner source. Removing it is a destructive local action and requires a Cooperator decision; it is not authorized by the acceptance or publication grants.
- No closure is emitted until this artifact’s disposition is recorded and the worktree state is honestly classified.
- No source, commit, public-ref or other mutation changed. Active mutation: none; one untracked generated artifact directory remains.

## 2026-11-12 — Whole closed

- The COOPERATOR authorized removal of the untracked `tests/target/` build/test artifact directory. It was removed; BookRadar `git status` is clean apart from ignored `target/`.
- `01_closure.md` authored: SHA-256 `d8c62fb1fef6f1c33d9d9e71e4a6986c90812362e3e0809ae1d9c08fc78d9584`.
- Final result: `publication-PASS`; `Logical-whole closure: closed-by-ORCHESTRATOR`.
- Public commit `ed4de54637f22613723bc3df98536a1ac25d0800`; parent `c93f5262ca27050922cc658424c298913852eaff`; tree `92884838654a0a534d8f3e77120029542adc7f72`; public `refs/heads/main` and symbolic `HEAD` match; local `main`/`HEAD`/`origin/main` match; `+0 -0`; AP pin `d7023cf…`; strict `ap doctor` PASS.
- Evidence: 74 tests pass; build/fmt/clippy/tree/diff checks pass; exact synthetic demo; acceptance `04_report_00.md` SHA-256 `8dac6b26…`; publication `05_report_00.md` SHA-256 `d7f8356f…`.
- Residual process/trace defects: implementation report missing; `03_report_00.md` and `02_report_00.md` are foreign predecessor BLOCKED reports; `00_notes.md` recovered from Orchestrator records; predecessor acceptance prompt filename restored; Meta Git remains COOPERATOR-owned and partially untracked. These do not change the public commit.
- Recommended next whole: `bookradar-test-hardening-and-ci`; later `bookradar-ui-shell`; live Hermes/Playwright and NUC remain separately secured. No successor grant implied.
- These notes are frozen at closure. Meta Git archival remains COOPERATOR-owned.
- Active mutation: none.
