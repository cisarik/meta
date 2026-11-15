# BookRadar — Closure: `bookradar-review-and-promotion-workflow`

**Artifact:** `projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_closure.md`
**Kind:** closing continuity and handoff artifact for a completed logical whole. Not a Worker prompt, task authority, implementation plan, acceptance report, publication report, or grant.
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-14.
**Target:** the upstream Master ChatOrchestrator and the next logical-whole selection.
**Capability profile: Orchestrator**
**Orchestrator session scope: logical-whole**
**Closure status:** `closed-by-ORCHESTRATOR`
**Restoration classification:** PASS for selecting and preparing the next logical whole, conditional on the successor revalidating mutable facts. This grants no mutation authority.
**Filename basis:** Meta handoff/closure sequence; next prefix after the COOPERATOR-requested `00_handout_00.md` opening position, independent of Worker exchange suffixes. No competing `00_handout.md` was created.

## 1. Closure record

```text
Phase-qualified result: publication-PASS
Result artifact or commit: 80b172c2db6fcacc93041d4eb4c246450547f112
Result evidence: exact public ref and symbolic HEAD equality; public commit parent/tree/subject; CI run 43600404485 success; implementation-PASS and acceptance-PASS with C1–C15/C17 independent audit plus C16 Playwright/Chrome proof; 113 tests; strict ap doctor PASS; clean worktree
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

`publication-PASS` is the final phase result; `acceptance-PASS` and
`implementation-PASS` preceded it. No deployment or production acceptance
applies. No upgrade ledger is activated; `Upgrade-ledger reconciliation:
complete` records that there was nothing to reconcile.

## 2. Verified result

Canonical repository: `https://github.com/cisarik/bookradar`
Published branch: `main`
Public commit: `80b172c2db6fcacc93041d4eb4c246450547f112`
Public commit URL: <https://github.com/cisarik/bookradar/commit/80b172c2db6fcacc93041d4eb4c246450547f112>
Commit subject: `docs: demonstrate governed conflict resolution`
Parent: `69ec45e245108c90e2de4302c03ca72572bf1829`
Tree: `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
Commit date: `2026-11-14T12:17:44+01:00` (`2026-11-14T11:17:44Z`)

The publication is one normal non-force fast-forward from the observed public
base `2281982f7dae0ef1f582d294592c41281ba11b21` to
`80b172c2db6fcacc93041d4eb4c246450547f112`. The two pushed commits are:

- `69ec45e245108c90e2de4302c03ca72572bf1829`
  `feat: add a governed research review and promotion path`
- `80b172c2db6fcacc93041d4eb4c246450547f112`
  `docs: demonstrate governed conflict resolution`

Direct public readback independently observed:

```text
ref: refs/heads/main	HEAD
80b172c2db6fcacc93041d4eb4c246450547f112	HEAD
80b172c2db6fcacc93041d4eb4c246450547f112	refs/heads/main
```

The public commit API independently confirms the parent
`69ec45e245108c90e2de4302c03ca72572bf1829`, tree
`578fbe8f958b17230ccdc5e1f13476c5e23c84f3`, and subject above. The authorized
push printed `2281982..80b172c  HEAD -> main`; no fetch, tag, force, rebase,
history rewrite, or extra ref occurred. `refs/codex/turn-diffs/checkpoints/*`
was not pushed.

CI evidence, independently observed through the GitHub API:

```text
Workflow: verify
Run: 43600404485
URL: https://github.com/cisarik/bookradar/actions/runs/43600404485
Event: push
Head SHA: 80b172c2db6fcacc93041d4eb4c246450547f112
Status: completed
Conclusion: success
Created: 2026-11-14T13:34:00Z
Updated: 2026-11-14T13:34:43Z
```

The single job `132463717503` (`verify`) and its `Verify` step completed
`success`. Local `main`, `HEAD`, and `origin/main` equal the public commit and
the worktree is clean apart from ignored `target/`.

AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`; `.ap` remains detached and
clean. Strict `./.ap/ap doctor` PASS. The domain contract remains revision 1.
ADR 0008 is accepted 2026-11-14; ADRs 0001–0007 are unchanged.

### Changed paths

The final diff from baseline `2281982f…` changes exactly fourteen paths:

| Path | Purpose |
|---|---|
| `README.md` | Documents the governed review/promotion surface, offer flags, and synthetic conflict-clearing demo |
| `crates/bookradar-store/src/bin/bookradar-review.rs` | New `show`, `promote`, and `review` command surface |
| `crates/bookradar-store/src/lib.rs` | Exposes the candidate and promotion APIs |
| `crates/bookradar-store/src/promotion.rs` | Reviewer-attested promotion and application-review wrapper |
| `crates/bookradar-store/src/research.rs` | Adds the read-only `ResearchStore::candidate` lookup |
| `crates/bookradar-store/tests/promotion.rs` | Twelve library promotion/review/trust-boundary tests |
| `crates/bookradar-store/tests/review_cli.rs` | Four `bookradar-review` process tests |
| `crates/bookradar-ui/src/config.rs` | Optional `--source-id` and `--offer-id`, default `1`/`1` |
| `crates/bookradar-ui/src/snapshot.rs` | Loads the configured `OfferRef` read-only |
| `crates/bookradar-ui/src/render.rs` | Displays the configured offer |
| `crates/bookradar-ui/tests/cli.rs` | Invalid offer-id rejection before I/O |
| `crates/bookradar-ui/tests/render.rs` | Non-default offer and promoted checked-available rendering |
| `crates/bookradar-ui/tests/common/mod.rs` | Existing UI config defaults remain `1`/`1` |
| `docs/adr/0008-governed-review-and-promotion.md` | Accepted ADR recording the nine approved decisions |

`bookradar-core` sources, the two schemas, `Cargo.toml`, `Cargo.lock`,
`docs/domain-contract.md`, `docs/research-input-v1.md`, ADRs `0001`–`0007`,
`scripts/verify.sh`, `.github/workflows/verify.yml`, `rust-toolchain.toml`,
`.gitignore`, both pre-existing binaries, and the `.ap` gitlink are unchanged.

## 3. Scope completed

- Added `bookradar-review` in `bookradar-store` with exactly three commands:
  `show`, `promote`, and `review`. `bookradar-poc` stays four commands on source
  `1`, offer `1`; `bookradar-research` is unchanged.
- Added an additive, read-only candidate lookup in the research ledger. There is
  no research-ledger `append_review`; human reviews are appended only in the
  application store (`0x42524452`).
- Implemented reviewer-attested **positive-only** promotion from an `admitted`
  research finding into the application store:
  - explicit resolved edition, Slovak, readable, present, available, all three
    claim covers, `direct-browser` or `manual` evidence, nonempty evidence
    reference/source statement/assessor/rationale, and reviewer approval;
  - caller-supplied instants and `(source_id, offer_id, observation_id)`;
  - one application-store `append` transaction, after candidate and attestation
    checks;
  - exact provenance `research:<producer>/<run>/<finding>@<receipt>/<position>`.
- Enforced fail-closed promotion:
  - `AgentOnly` is refused even with approval;
  - rejected, quarantined, replayed, unknown, or incomplete inputs write nothing;
  - `duplicate-key` rolls back the append without partial registry/observation
    writes;
  - the same finding may be cited under a new observation id; disputed admitted
    findings may be promoted while their ledger dispute remains visible.
- Exposed attributed application-review revisions through `review`, preserving
  `expected_revision` optimistic concurrency and the non-regressing
  `assessed_at` guard. Equal-time conflict rejection and disputed-to-supported
  supersession preserve all prior revisions.
- Added optional `bookradar-ui --source-id` and `--offer-id` flags, defaulting to
  `1` and `1`. Invalid ids exit `2` before database or socket I/O. The UI remains
  read-only and supports only `GET`/`HEAD` on `/` and `/style.css`.
- Preserved all 94 pre-existing tests and added 19 focused tests, bringing the
  total to **113 passing tests**. The new coverage includes promotion,
  refusal-before-I/O, `AgentOnly` promotion and `Supported`-review invariants,
  duplicate rollback, ledger-byte preservation, conflict clearing, review
  concurrency/time regression, non-default offers, and UI invalid-id rejection.
- Updated `README.md` with the runnable synthetic end-to-end demo, including a
  second same-time observation and the `Rejected` revision that clears the
  conflict, and added accepted `docs/adr/0008-governed-review-and-promotion.md`
  with the nine approved decisions.
- Completed E2 evidence: an independent audit (C1–C15, C17) plus a targeted C16
  Playwright `1.65.1` / headless Chrome `157.0.8103.39` probe covering the
  promoted, conflicted, rejected, and non-default states at `1280×800` and
  `375×812`, clean console/network, HTTP security controls, and cleanup.
- Published the accepted candidate on `origin/main` with direct public readback
  and observed the successful public `verify` run `43600404485`.

## 4. Evidence

- **113 tests pass** in `bash scripts/verify.sh` and public CI run
  `43600404485`: 17 core, 10 store unit, 4 observation CLI, 13 history, 6
  persistence, 12 promotion, 2 research CLI, 5 research contract, 20 research
  ingestion, 4 review CLI, 4 UI CLI, 6 UI HTTP, and 10 UI render; 0 doc/bin
  tests. That's 94 preserved tests plus 19 new tests.
- Opening provisional handout `00_handout_00.md` SHA-256
  `ea5985ff63853098c8f2de5dc59977a30d5374acc0f812f23107e70656e997fd`
  (COOPERATOR-requested filename exception; no competing `00_handout.md`).
- Predecessor closure `06-bookradar-ui-shell/01_closure.md` SHA-256
  `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`.
- Planning prompt `01_planning_00.md` SHA-256
  `6547216bbc79798733fc6d4fb67b9bb505eb235cf3a56f828617c5aec9d1e922`;
  planning report `01_report_00.md` SHA-256
  `e08189f9534208d4f1dee91d289014d536cad88327236691a9deb8a68e9ecc22`.
- Implementation prompt `01_implementation_01.md` SHA-256
  `04747fbabb2d9d7973943b7be3a419fdb54af735d4eda60eb73cf86dc3957926`;
  implementation report `01_report_01.md` SHA-256
  `030f8955a7a2b116a647ed6d47489ddf59bde23483b3f6e0e0a459e21642bf8c`.
- Documentation-correction prompt `01_correction_02.md` SHA-256
  `2f921c3b3c945a84221d2c8de481fa577e86860a62af0338a37cbc2bef49d559`;
  correction report `01_report_02.md` SHA-256
  `f08aee0b9c4da4a1d53c5ddfd0021821db634ed5c88f8efbfef3c9daae6a8108`.
- Independent audit prompt `02_acceptance_00.md` SHA-256
  `ffdea5259956cb521dede5b46d04e1138a4fe8faff41934a507797157baebf98`;
  independent audit report `02_report_00.md` SHA-256
  `5286deaeb6a28ab5d8d7ab35829eecde21a52f16894b22807e2b017083012f8f`
  (C1–C15 and C17 PASS).
- C16 fresh probe prompt `03_browser_00.md` SHA-256
  `5a79fe7c78bcb810edf38058ed392a9ac65f5126b6fa062286edbfd476193fb4`;
  C16 probe report `03_report_00.md` SHA-256
  `2f1d3df2a889e6d00b1d4daaaf7131cb94e886be4353ff1e0ccaca4342047743`
  (C16 PASS).
- Publication prompt `04_publication_00.md` SHA-256
  `9be324491b72c10e499a32894a57a55fca461e539d4a6be52856f7077c9163c4`;
  final publication report `04_report_00.md` SHA-256
  `f12f4bdaa751195e2ef03208277f1705d53bb575e8fb99fa9b389fe6693c2066`
  (`publication-PASS`, public readback, and CI run `43600404485`).

## 5. Non-achievements and deferrals

- No live Hermes/Playwright adapter, scraping, external API, external network in
  the implemented workflow, MCP, real retail data, personal state, watchlists,
  accounts, authentication, NUC, SSH, sudo, services, deployment, or releases.
- No negative/unavailable or `AgentOnly` historical promotion path. This whole
  deliberately implements only a complete positive reviewer attestation. A stale
  positive row is stored as historical, not eligible.
- No research-ledger dispute-resolution command and no human review write to the
  research ledger. Research candidates remain untrusted evidence.
- No UI writes, forms, JSON endpoints, JavaScript, non-loopback binds, or running
  monitor. The UI is an immutable local startup snapshot at a caller-supplied
  `--now` instant.
- No `bookradar-core` behavior change, no schema v2, no research wire change, no
  domain-contract change, and no ADR 0001–0007 edit.
- No new external crate, new workspace crate, dependency, toolchain, AP update,
  committed screenshot, license, contribution policy, privacy policy, or release
  process.

## 6. Residual risks and process/trace notes

- Positive `Checked available` lines are decisions about explicitly
  reviewer-typed synthetic observations. They are not guarantees of current real
  retail stock or successful future purchase. Reviewer approval is attribution,
  not authentication.
- C16 was first BLOCKED because no Playwright adapter existed. With explicit
  COOPERATOR provisioning authority, a fresh targeted probe installed only
  `playwright@1.65.1` under a declared temporary root, used the installed Chrome
  channel `157.0.8103.39`, completed C16 on the first attempt, and removed the
  root. Browser evidence is Chrome-only; it does not establish Safari/Firefox
  behavior. The mobile `.table-wrap` nested scroll did not widen the document or
  clip key text.
- A later `Supported` review cannot make an `AgentOnly` observation eligible;
  the kernel decides eligibility from the immutable evidence method.
- Observation ids are caller-allocated. Duplicate keys fail closed, while the
  same research finding may intentionally be cited by multiple observation ids.
- Eight local `refs/codex/turn-diffs/checkpoints/*` tree refs remain harness state;
  they were neither deleted nor published. They are not part of the candidate or
  public branch identity.
- The final publication artifact was read fully and hashed at
  `f12f4bda751195e2ef03208277f1705d53bb575e8fb99fa9b389fe6693c2066`. It and
  the independently observed public CI API agree on run `43600404485`; this
  final hash is the closure evidence.
- Meta Git remains COOPERATOR-owned. The Orchestrator wrote only this whole's
  prompts, notes, and closure artifact into Meta; no Meta commit, branch, tag, or
  push was performed. Notes are frozen at closure.

## 7. Pins and durable owners

- Public BookRadar commit: `80b172c2db6fcacc93041d4eb4c246450547f112` on `main`.
- Public CI run: `43600404485`, workflow `verify`, conclusion `success`.
- AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Product contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10.
- Wire reference: `docs/research-input-v1.md`.
- ADRs 0001–0007 accepted and unchanged; ADR 0008 accepted 2026-11-14.
- Verification owners: `scripts/verify.sh`, `.github/workflows/verify.yml`,
  `README.md`, ADR 0006, and ADR 0008.
- No active upgrade ledger.

## 8. Recommended next logical whole(s)

For COOPERATOR selection, in no priority order:

1. A bounded **synthetic producer-adapter contract rehearsal**, producing
  untrusted `bookradar-research` v1 without live network so the
  validate -> review -> promote -> inspect workflow can be rehearsed at larger
  synthetic coverage.
2. A bounded **live Hermes/Playwright research-adapter slice**, only with new
  explicit network, untrusted-content, real-data, rate-limit, and host-security
  decisions. Its output must remain untrusted and pass the same governed review
  boundary.
3. A bounded **reviewer-attested negative/historical observation** or expanded
  catalog-navigation whole, if the COOPERATOR explicitly wants to reopen the
  positive-only promotion scope.

Deployment, NUC operations, personal state/accounts, and policy selection remain
later separately authorized wholes. Neither recommendation selects or grants a
successor whole.

## 9. Artifact lifecycle and return edge

- **Class:** retained closing continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to the governing
  immutable AP and the accepted domain contract.
- **Consumer:** upstream Master ChatOrchestrator, the next per-whole
  Orchestrator, and later reviewers.
- **Discoverability:** exact Meta location, public commit URL, CI run URL, AP pin,
  ADR 0008, frozen prompt/report hashes, and the notes.
- **Retention:** retain through the next selection and archive after closure; a
  material correction after closure is a separately named successor artifact, not
  an in-place edit. `00_handout_00.md` stays frozen.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup
  decision.
- **Expected return to Master:** this truthful closure with the exact public
  commit, CLI/UI/CI evidence, completed scope, explicit non-achievements, current
  contract/AP pin, residual risks, recommended next wholes, and no implied
  successor grant.

**Closure signal:** `closed-by-ORCHESTRATOR`

**Final invariant:** research and curated application truth are bridged only by
complete, attributed human review. Zero automatic verification, immutable
append-only SQLite, deterministic caller-supplied times, zero new external
dependencies, and no live network or real retail data.
