# BookRadar — Closure: `bookradar-research-ingestion-contract`

**Artifact:** `projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md`
**Kind:** closing continuity and handoff artifact for a completed logical whole. Not a Worker prompt, task authority, implementation plan, acceptance report, publication report, or grant.
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-12.
**Target:** the upstream Master ChatOrchestrator and the next logical-whole selection.
**Capability profile: Orchestrator**
**Orchestrator session scope: logical-whole**
**Closure status:** `closed-by-ORCHESTRATOR`
**Restoration classification:** PASS for selecting and preparing the next logical whole, conditional on the successor revalidating mutable facts. This grants no mutation authority.
**Filename basis:** Meta handoff/closure sequence; next prefix after the opening `00` position, independent of Worker exchange suffixes.

## 1. Closure record

```text
Phase-qualified result: publication-PASS
Result artifact or commit: ed4de54637f22613723bc3df98536a1ac25d0800
Result evidence: exact public commit and tree; direct public ref and symbolic HEAD equality; acceptance-PASS and publication-PASS; unchanged AP pin; 74 tests; workspace build/fmt/clippy/tree and strict ap doctor PASS; clean worktree
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

`publication-PASS` is the final phase result; `acceptance-PASS` preceded it. No upgrade ledger is activated; `Upgrade-ledger reconciliation: complete` records that there was nothing to reconcile.

## 2. Verified result

Canonical repository: `https://github.com/cisarik/bookradar`
Published branch: `main`
Public commit: `ed4de54637f22613723bc3df98536a1ac25d0800`
Public commit URL: <https://github.com/cisarik/bookradar/commit/ed4de54637f22613723bc3df98536a1ac25d0800>
Commit subject: `feat: add versioned research ingestion PoC`
Parent: `c93f5262ca27050922cc658424c298913852eaff`
Tree: `92884838654a0a534d8f3e77120029542adc7f72`
Commit date: 2026-11-12T19:21:28+01:00

The commit changes exactly nineteen paths, adding 5,130 lines and removing 239:

| Path | Purpose |
|---|---|
| `Cargo.lock` | Resolved serde/serde_json graph and pins |
| `README.md` | Status, workspace, research proof, commands and exits |
| `docs/research-input-v1.md` | Versioned wire contract and ledger semantics |
| `docs/adr/0005-versioned-research-admission.md` | Accepted architecture rationale |
| `crates/bookradar-store/Cargo.toml` | Exact serde and serde_json pins |
| `crates/bookradar-store/src/lib.rs` | Research module exports |
| `crates/bookradar-store/src/store.rs` | Shared transaction/insert seams; v1 behavior preserved |
| `crates/bookradar-store/src/history.rs` | Crate-private history seam |
| `crates/bookradar-store/src/research.rs` | Research ledger, admission, replay, projection |
| `crates/bookradar-store/src/research_contract.rs` | Strict JSON v1 decoder and canonicalization |
| `crates/bookradar-store/src/schema_research_v1.sql` | Separate research ledger schema |
| `crates/bookradar-store/src/bin/bookradar-research.rs` | Four-command synthetic CLI |
| `crates/bookradar-store/tests/research_contract.rs` | Contract tests |
| `crates/bookradar-store/tests/research_ingestion.rs` | Admission, replay, conflict and projection tests |
| `crates/bookradar-store/tests/research_cli.rs` | CLI transcript and exit test |
| `crates/bookradar-store/tests/fixtures/research/partial.json` | Synthetic partial-run fixture |
| `crates/bookradar-store/tests/fixtures/research/conflict.json` | Synthetic conflict fixture |
| `crates/bookradar-store/tests/fixtures/research/newer.json` | Synthetic newer-observation fixture |
| `crates/bookradar-store/tests/fixtures/research/older.json` | Synthetic older-import fixture |

The core sources, domain contract, ADRs 0001–0004, `AGENTS.md`, `.gitmodules`, `rust-toolchain.toml`, `schema_v1.sql`, the old `bookradar-poc` binary/fixtures and the existing tests are unchanged.

Public readback:

```text
ref: refs/heads/main HEAD
ed4de54637f22613723bc3df98536a1ac25d0800 HEAD
ed4de54637f22613723bc3df98536a1ac25d0800 refs/heads/main
```

Local `main`, `HEAD` and `origin/main` equal the published commit; the branch is `+0 -0`; the worktree is clean apart from ignored `target/`. The commit parent is the accepted baseline, so publication is a normal fast-forward with no force, rebase, history rewrite or extra ref.

AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`; `.ap` remains detached and clean. Strict `./.ap/ap doctor` PASS.

## 3. Scope completed

- Versioned strict JSON research envelope (`bookradar-research` version 1) with explicit unknown provenance, source/listing/redirect references, timestamps, evidence, uncertainty and producer context.
- Strict decoder behavior: unsupported versions, malformed/UTF-8 input, duplicate keys, unknown fields, input limits and finding/depth limits are quarantined or rejected without guessing.
- Separate SQLite research ledger, application id `0x42525249`, `user_version=1`, with `research_inputs`, `research_runs` and `research_findings`, reusing the v1 observation/review tables without migration.
- Replay identity `(producer_id, run_id, finding_id)` and canonical-byte equality; identical replay is a no-op; changed content under the same identity is retained, quarantined and disputed.
- Partial-run accounting, rejection/quarantine distinction, run-context conflicts, equal-time contradictions, older-import non-rollback and failed-access non-inference.
- Candidate projection only as `Unreviewed`/`Disputed`, with `AgentOnly` application support, no reviewer approval and no promotion to an application store.
- Four-command `bookradar-research` CLI with synthetic fixtures and stable outputs/exits.
- Wire reference `docs/research-input-v1.md`, accepted ADR 0005, updated README, and 74 passing tests.
- No schema v2 migration, no auto-verification, no live research adapter, no UI, no NUC and no deployment.

## 4. Evidence

- 74 tests pass: 17 core, 10 store unit, 6 persistence, 13 history, 2 old CLI, 1 research CLI, 5 research contract, 20 research ingestion.
- Workspace build, test, formatting, clippy `-D warnings`, core dependency tree, `git diff --check`, `git show --check` and strict `ap doctor` pass.
- The exact synthetic demo matches the accepted plan: init exit 0; partial import exit 3; identical replay exit 3; current before conflict exit 0; conflict import exit 3; current after conflict exit 0; inspect output matches. The research ledger reports application id `1112691273` (`0x42525249`), `user_version=1`, the v1 tables plus research tables, empty `editions`, and append-only enforcement.
- Independent acceptance report `04_report_00.md`: SHA-256 `8dac6b2614e4aa54480d0f17ce94aad09a243b176cf98243e9675178f1c1cca6`, `acceptance-PASS` for `ed4de54…`, no push.
- Publication report `05_report_00.md`: SHA-256 `d7f8356f98f3bdd5a61ddd3d0b8d7ddc2eb3c7323271513df364f8c9d775df97`, `publication-PASS`, one normal non-force `git push origin main`, direct readback.
- The acceptance independently verified strict contract behavior, admission/quarantine, replay/conflict, older import, projection without auto-verification, schema/ledger, CLI, documentation, dependency pins and scope. It found no source, test, lockfile or documentation defect.

## 5. Non-achievements and deferrals

Live Hermes/Playwright producers, application-store promotion, reviewer approval/resolution workflow, catalog matching, UI, network ingestion, NUC/SSH/sudo, deployment, screenshots, personal data, accounts, CI release automation and public API stability remain unimplemented. Shipping, fees, totals, ranges, currency conversion and price history are not represented. No license, contribution, privacy, security-response, support or release policy is selected. No schema v2 migration is introduced. The slice does not validate real research, real listings or real stock.

## 6. Residual risks and process/trace defects

- Producer identity, provenance and normalized times are asserted, not authenticated or independently verified.
- Contradiction detection covers explicit comparable facts within exact producer-scoped listing groups; evidence bytes, natural-language truth and cross-producer identity are not assessed.
- Quarantine and disputes persist, but this slice supplies no resolution workflow.
- SQLite recovery evidence covers transaction rollback and second-process reopen, not power-loss or multi-process stress.
- The implementation exchange’s required report was not delivered. `03_report_00.md` is a foreign predecessor BLOCKED report (SHA-256 `4ec92c26…`, logical whole `bookradar-persistence-and-history-slice`, baseline `bd23b08…`) and was rejected as a companion. The candidate was instead verified directly by the Orchestrator and independently accepted from Git, source, tests, documentation and a fresh CLI run. This is a process/trace defect, not a code defect.
- `02_report_00.md` and `03_report_00.md` in this trace are duplicate foreign BLOCKED reports preserved as incident evidence; they are not implementation reports for this whole and must not be reused.
- `00_notes.md` went missing from the working tree and was reconstructed from Orchestrator-authored records; it is marked as a recovery, not claimed byte-identical to the lost file.
- A predecessor acceptance prompt was restored from `03_report_01.md` to its correct `03_acceptance_00.md` name; no Git commit was made.
- Meta Git remains COOPERATOR-owned. The new whole directory is partially untracked/uncommitted; no Meta Git operation was performed by the Orchestrator.
- Untracked `tests/target/` generated build/test artifacts (about 390 MB) were found during the closure check and removed after explicit COOPERATOR authorization; the final BookRadar worktree is clean apart from ignored `target/`.

## 7. Pins and durable owners

- Public BookRadar commit: `ed4de54637f22613723bc3df98536a1ac25d0800`.
- AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Product contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10.
- ADRs: 0001–0004 accepted and unchanged; ADR 0005 accepted 2026-11-12.
- Implementation wire owner: `docs/research-input-v1.md`.
- Current semantic owner remains the domain contract; ADR 0005 is historical rationale.

## 8. Recommended next logical whole(s)

Recommended next whole: `bookradar-test-hardening-and-ci` — add the missing empty-history automated assertion, harden the now-74-test suite around research admission and shared store seams, and add a small CI/quality route. It is the lowest-risk follow-up before live adapters and would also reduce the process/trace and report-delivery friction observed in this whole.

A later candidate: `bookradar-ui-shell` — a small synthetic/store-backed view of the accepted history and research ledger. Live Hermes/Playwright integration, NUC deployment, real retail data and auto-verification remain later, separately secured wholes.

Neither recommendation selects or grants a successor whole.

## 9. Artifact lifecycle and return edge

- **Class:** retained closing continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP and the accepted domain contract.
- **Consumer:** upstream Master ChatOrchestrator, the next per-whole Orchestrator, and later reviewers.
- **Discoverability:** exact Meta location, public commit URL, AP pin, contract revision, acceptance/publication reports and this closure.
- **Retention:** retain through the next selection and archive after closure; material correction after closure is a separately named successor artifact.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup decision.
- **Expected return to Master:** this truthful closure with exact public commit, evidence classification, completed scope, explicit non-achievements, current pins, residual risks, recommended next wholes and no implied successor grant.

**Closure signal:** `closed-by-ORCHESTRATOR`

**Final invariant:** The trust boundary now exists before any live research adapter: one versioned, testable ingestion contract, no auto-verification, synthetic evidence, and no live retail data or host side effects.
