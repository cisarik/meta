### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-rust-foundation  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session profile: Planner  
Task identity: BOOKRADAR-RUST-FOUNDATION-PLAN  
status: PASS  
Phase-qualified result: not-applicable  
Evidence tier: E0

| Repository | Start commit | End commit |
|---|---|---|
| bookradar | `5c820abd439850039adf9866af26acfa15287493` | `5c820abd439850039adf9866af26acfa15287493` |
| AP | `d7023cf037f6d17885c3ede5c04812c61640da50` | `d7023cf037f6d17885c3ede5c04812c61640da50` |

Changed files and purpose: none.

Validation performed: repository, public-ref, submodule, environment and source inspection described below; final worktree and index diffs remained empty. No Rust build, test, formatting or lint command ran. No toolchain was installed. No `ap` subcommand ran.

Git result: no fetch, stage, commit or push. Network reads were exactly:

- `git ls-remote --symref https://github.com/cisarik/bookradar refs/heads/main HEAD`
- One `curl -fsSL https://static.rust-lang.org/dist/channel-rust-stable.toml`

No AP public-ref read or other network operation was performed.

Persistence: none. This complete report is returned in the session. The COOPERATOR owns persistence to `cisarik/meta`, `projects/bookradar/00/02-bookradar-rust-foundation/01_report_00.md`, and subsequent paired prompt/report Git archival.

Deviations and missing evidence: the Rust metadata request succeeded, but output truncation prevented verification of the Rust version. The proposal therefore uses the permitted provisioning-time version-selection rule. All mandatory source documents were available.

Smallest next step: ORCHESTRATOR reconciliation of this proposal and the consolidated decisions in §11, including binding the exact Rust version before issuing an implementation grant.

Report justification: new-evidence  
Logical-whole closure: not-closed  
Authority expiry: this terminal report ends the grant; no autonomous continuation.

```text
Orchestration critique:
MEASURED: none
LEAD: none

Resolved Execution Issues / Near-Misses: The single Rust metadata request returned more output than the selected output budget retained. Exact version extraction was unavailable. No second request was made; the explicitly permitted version-selection fallback is used. The exact pin remains a prerequisite for implementation.
Pre-Existing Failure Classification: none
```

# BookRadar Rust Foundation — Proposed Implementation Plan

The design below is a proposal. The accepted semantic baseline remains `cisarik/bookradar`, `docs/domain-contract.md`, revision 1, Accepted 2026-11-10. Neither this report nor its planning status accepts an implementation.

## 1. As-found state

Inspection date: 2026-11-10.

| Evidence and exact commands | Observed result |
|---|---|
| `pwd -P`; `git rev-parse --show-toplevel` | Physical working directory equals the BookRadar Git root. Machine-specific absolute paths are omitted from this report. |
| `git remote -v` | Fetch and push origin: `https://github.com/cisarik/bookradar`. |
| `git status --porcelain=v1 --branch --untracked-files=all` | `## main...origin/main`; no changed or untracked paths. |
| `git rev-parse HEAD`; `git rev-parse 'HEAD^{tree}'`; `git log -1 --format='%H%n%s%n%T%n%P'` | HEAD as recorded above; subject `docs: define BookRadar domain contract`; tree `acf8e4c1142919b018a58fe3c43086ce26ef6a10`; parent `12864ac874d74c562e22243bd622bd2729dfdaca`. |
| `git for-each-ref --format='%(refname) %(objectname)'` | `refs/heads/main` and `refs/remotes/origin/main` equal HEAD. Five auxiliary client refs exist under `refs/codex/turn-diffs/`; no additional branch or tag was listed. |
| `git worktree list --porcelain` | Exactly one worktree, on `main`, at the expected HEAD. |
| `git ls-files`; `git ls-tree HEAD .ap`; `git ls-tree -r --name-only HEAD` | Exactly the seven expected committed paths. `.ap` is mode `160000` at the expected pin. |
| `git submodule status` | Exactly one initialized submodule, `.ap`, at the expected pin. |
| `git -C .ap rev-parse HEAD`; `git -C .ap status --porcelain=v1 --branch`; `git -C .ap remote -v` | Expected AP commit; clean detached HEAD; canonical origin `https://github.com/cisarik/ap.git`. |
| `git -C .ap symbolic-ref -q HEAD` | Exit 1 with no output, confirming detached HEAD. |
| `git -C .ap cat-file -t d7023cf037f6d17885c3ede5c04812c61640da50` | `commit`: the pinned object is present locally. |
| `git rev-parse --git-dir --git-common-dir` | Both resolve to `.git`. |
| `command -v rustc cargo rustup` | Exit 1, no output: none is available on the current command path. |
| `uname -sm`; `sw_vers`; `cc --version` | Darwin arm64; macOS 27.2, build 26B123; Apple Clang 21.0.0, target `arm64-apple-darwin27.2.0`. |
| `ls -la`; `find . -path './.git' -prune -o -path './.ap' -prune -o -print` | Documentation-only checkout. No Cargo files, toolchain file, `.cargo/`, `.github/`, source or generated Rust artifacts. |

The exact committed path set is:

```text
.ap
.gitmodules
AGENTS.md
README.md
docs/domain-contract.md
docs/adr/0001-book-edition-and-offer-identity.md
docs/adr/0002-evidence-and-research-trust-boundary.md
```

Git operation-state inspection used:

```sh
find .git -type f -name '*.lock' -print
find .git -type d \( -name rebase-merge -o -name rebase-apply -o -name sequencer \) -print
find .git -type f \( -name MERGE_HEAD -o -name CHERRY_PICK_HEAD -o -name REVERT_HEAD -o -name REBASE_HEAD \) -print
```

No Git transaction lock or active merge/rebase/cherry-pick/revert marker was found. The only lock-named file was the zero-byte `.git/cursor/crepe/build.lock`; its location identifies it as auxiliary editor build metadata rather than a Git transaction lock. It was not modified.

The public read returned exactly:

```text
ref: refs/heads/main	HEAD
5c820abd439850039adf9866af26acfa15287493	HEAD
5c820abd439850039adf9866af26acfa15287493	refs/heads/main
```

Final verification repeated the full superproject/submodule status and HEAD reads, plus `git diff --exit-code` and `git diff --cached --exit-code`. Both repositories remained clean at their starting commits.

The sole Rust metadata read exited 0. Retained output established manifest version `2` and manifest date `2026-10-15`, but did not retain the `[pkg.rust]` version needed for an exact pin. No Rust version is inferred from another package’s version.

Mandatory reading was completed at the verified identities:

- `cisarik/bookradar:.ap/AP_WORKER.md`, complete.
- `.ap/AP.md`: “Semantic Authority and Artifact Relationships”, “Per-Role Minimum-Reading Spine”; RF-01, RF-03–RF-08, RF-12, RF-14, RF-18–RF-19; “Planning Budget and Expiry”, “Implementation Authority”; §§3–5, §8, §12, §13, §17 and §18.
- `.ap/PROMPT_CONTRACTS.md`: “Worker Report Header”, “Planning Record”, “Common Worker Task Fields”, “Mutation Axes Record”, “Worker Exchange Identity and External Trace Contract”, “Session-And-Mode Routing Contract”, “Plan-to-Execution Gate”, and “Cooperator Delivery and Trace Destination Record”.
- `.ap/ARTIFACT_LIFECYCLE.md`: the required classification, metadata, external-trace, discovery and per-whole-notes headings.
- Root instructions, README, the complete domain contract and both accepted ADRs.

Only the provided Meta whole’s `00_handout.md` and `00_notes.md` were read. Their statements remain historical evidence. No Meta Git operation or independent Meta cleanliness inspection occurred.

| Capability | Classification and evidence |
|---|---|
| Client | **inferred**: Codex environment, consistent with session configuration. Exact client build is **unknown/not observably exposed**. |
| Exact model | **unknown/not observably exposed**; no exact model identity is self-certified. |
| Reasoning and context | **requested**: High and approximately 250k context. Effective reasoning setting, capacity and utilization are **unknown/not observably exposed**. |
| Native planning mode | **directly observed**: active Plan Mode configuration restricts this exchange to planning and non-mutating inspection. |
| Filesystem reads | **directly observed**: requested source, attachment and the two provided Meta context files were readable. Writes were not tested. |
| Shell and Git reads | **directly observed** through successful command execution. |
| Public Git and network | **directly observed** for the exact BookRadar `ls-remote` and Rust metadata request only. Broader connectivity is unknown. |
| Rust execution | **directly observed unavailable** through command lookup. Compilation and test capability remain unverified. |
| Git writes, installation and report writes | Ungranted and untested. No required read capability was otherwise missing. |

Capability grants no authority.

## 2. Selected slice and contract map

Select a **stateless verification-policy kernel for one supplied book-offer observation and its explicit current assessment context**.

It answers: can this observation support the timestamped “Checked available” meaning for a particular Slovak edition target, at the supplied instant?

It includes:

- Typed internal references and unresolved/conflicting subject identity.
- Slovak, Czech, mixed, unknown and conflicting language evidence.
- Separate access, availability, listing, knowledge and temporal dimensions.
- Reviewer approval, direct/manual evidence, claim coverage and explicit source availability.
- Exact 24-hour expiry and immediate conflict/failed-recheck suppression.

| Contract heading | Executable subset |
|---|---|
| “Identity and matching”; “Language evidence” | Exact supplied edition reference; uncertainty retained; Czech and unsupported language cannot satisfy a Slovak target. |
| “Offers and observations” | Immutable observation values and independent status dimensions. |
| “Transitions and rechecks” | New values represent attempts; failed access supplies no stock conclusion; active failed-recheck context suppresses an earlier candidate. |
| “Verification and freshness” | Pure eligibility calculation with injected time and explicit blockers. |
| “Evidence and provenance” | Source attribution, evidence references, method, coverage and timestamp assertions. |
| “User-facing truth” | Structured timestamped eligibility; no unqualified current-stock result. |
| “Deterministic freshness timeline” | Exact fictional observation and expiry fixtures. |

The kernel does **not** choose the current observation from history, derive conflict resolution, authenticate reviewers, inspect evidence, or admit external research. Its caller supplies the current assessment context explicitly. This boundary avoids inventing history precedence and ingestion semantics.

Deferred executable areas include catalog matching, ISBN processing, work/copy models, prices, ownership, research envelopes, replay, history reduction, storage, parsing, presentation and integrations. No full domain implementation is claimed.

## 3. Cargo, package and file-tree proposal

Use one library package, without a workspace or binary.

| Metadata | Proposed value |
|---|---|
| Package | `bookradar-core` |
| Rust crate | `bookradar_core` |
| Version | `0.1.0` |
| Description | `Deterministic domain rules for BookRadar book-offer observations.` |
| Repository | `https://github.com/cisarik/bookradar` |
| Publication | `publish = false` |
| Edition | `2024` |
| `rust-version` | Exact approved toolchain version, denoted `R` below |

Do not add license, author, support, homepage or release-policy metadata without an established decision.

Exact proposed repository mutation allowlist:

```text
.gitignore
Cargo.toml
Cargo.lock
rust-toolchain.toml
src/lib.rs
src/model.rs
src/verification.rs
tests/verification.rs
README.md
docs/adr/0003-rust-domain-foundation.md
```

`src/lib.rs` exports the small typed seam. `src/model.rs` owns values and checked construction; `src/verification.rs` owns pure evaluation. Integration tests exercise the exported interface.

No public API stability is promised. The package remains unpublished and may evolve under later review.

## 4. Domain API and invariants

Use ordinary enums, structs, private fields and checked constructors. Add `#![forbid(unsafe_code)]`.

**Identity and attribution**

- Distinct `SourceId`, `OfferId`, `ObservationId` and `EditionId` newtypes over nonzero integers.
- `OfferRef { source, offer }`; an `OfferId` identifies one offer generation within its source.
- `ObservationRef { offer, observation }`, also used to bind assessment to observation.
- `SubjectIdentity::{Resolved(EditionId), Unresolved, Conflicting}`.
- No ID generation, matching, URL identity, seller identity or ISBN interpretation.

URLs and seller changes cannot silently change these keys because no such inference operation exists. Allocating and preserving keys belongs to future callers.

**Independent dimensions**

- `LanguageEvidence::{Slovak, Czech, Mixed, Unknown, Conflicting}`.
- `SourceAvailability::{Available, Reserved, Unavailable, Unknown}`.
- `AccessResult::{Readable, RateLimited, Captcha, AuthenticationBlocked, Timeout, TransportError, PageGone}`.
- `ListingDisposition::{Present, Removed, Uncertain}`.
- `KnowledgeAssessment::{Unreviewed, Supported, Disputed, Rejected}`.
- `TemporalAssessment::{WithinInterval, Stale, Unknown}`.

An observation contains its reference, subject, language, time, access, listing disposition, availability, optional source statement and evidence support. Missing support remains representable.

**Evidence and review**

Evidence support contains:

- Optional opaque evidence reference.
- `EvidenceMethod::{DirectBrowser, Manual, AgentOnly}`.
- Explicit coverage of subject identification, language and source availability.

The separate immutable `VerificationContext` contains:

- The exact observation reference being assessed.
- Knowledge assessment and optional reviewer-approval reference.
- `ConflictState::{Clear, Unresolved, Unknown}`.
- `RecheckState::{Clear, Failed, Unknown}`.

Context construction requires explicit values; it has no default that silently clears blockers. Reviewer references are attributed assertions, not authentication or proof that review occurred.

**Construction and operations**

- Checked constructors return `Result` or `Option` for invalid IDs, empty required references and inconsistent typed inputs.
- Unknown and conflicting knowledge are valid states, not constructor failures.
- `Observation::failed_check` accepts a typed access failure and creates availability `Unknown`, no stock statement, and listing `Uncertain`; `PageGone` creates listing `Removed`.
- A readable generic redirect may remain listing `Uncertain`, availability `Unknown`.
- Observed facts have getters and no mutation methods. Later attempts create separate observation values.
- `evaluate_verification(target: EditionId, observation: &Observation, context: &VerificationContext, now: SystemTime) -> Result<VerificationAssessment, DomainError>` is pure.
- An assessment bound to another observation returns a typed mismatch error.

`VerificationAssessment` exposes temporal assessment separately from `Eligible { observation, observed_at, expires_at }` or `NotEligible`.

No constructor or successful evaluation claims to validate real evidence or purchase success. No repository, parser, command execution, file retrieval or network operation is introduced.

## 5. Freshness and verification design

Use `std::time::{SystemTime, Duration}`. The verification interval is exactly `Duration::from_secs(86_400)`.

A timestamp assertion retains its optional original representation, explicit known/unknown offset, and optional normalized instant. The caller supplies normalization; this slice implements no timestamp-string parser or timezone conversion. Known-time construction checks required fields and offset bounds; it does not claim to verify normalization against source text.

Temporal assessment is:

- Missing usable instant or unknown offset: `Unknown`.
- Observation later than injected `now`: `Unknown`.
- Failure of checked expiry arithmetic: `Unknown`.
- Otherwise age below 86,400 seconds: `WithinInterval`.
- Age equal to or above 86,400 seconds: `Stale`.

Eligibility requires **all** of the following:

1. Resolved subject equals the supplied edition target.
2. Language is Slovak, with evidence covering that claim.
3. Access is readable and listing disposition is present.
4. Source availability is available, with an explicit nonempty source statement.
5. Evidence reference exists; method is direct browser or manual; required claims are covered.
6. Knowledge is supported and reviewer approval is present.
7. Temporal assessment is within the interval.
8. Conflict and recheck context are both clear.

Agent-only evidence cannot qualify even when structurally valid and marked supported. Reserved, unavailable and unknown remain distinct facts without positive availability eligibility.

A failed recheck creates another observation value. Evaluating the earlier candidate with active failed-recheck context immediately returns `NotEligible`, even before expiry. A later qualifying observation with explicitly reconciled clear context may qualify again. Clearing context never changes an observation’s age.

Conflict detection, context maintenance and selection from history are deferred. Future integration must establish those facts before using this kernel for a current label.

## 6. Persistence decision

Recommend **no persistence**.

| Option | Added surface and dependencies | Costs, isolation and lock-in |
|---|---|---|
| **No persistence — selected** | Domain values, evaluator and fixture tests only; no repository or collection abstraction; no dependencies. | No native library or migration burden. Each test owns its values. Future storage can consume the seam without inheriting an invented storage contract. |
| Narrow in-memory repository/state collection | Would add `src/store.rs` and `tests/store.rs`; standard-library collections suffice. | Introduces ownership, ordering and lifecycle decisions without proving additional selected behavior. Tests need fresh stores. Creates an interface that future persistence may need to preserve or replace. |
| Small SQLite implementation | Would add a SQLite adapter and isolated database tests, plus a Rust binding such as unselected `rusqlite`. No version or schema is proposed. | Adds transitive dependencies and either system SQLite requirements or bundled C compilation. Requires schema ownership and migration/recovery decisions. Tests need isolated databases; durable representation increases lock-in. |

The selected kernel needs neither owned history nor a storage query. Persistence would expand the slice without strengthening its required evidence.

## 7. Toolchain and dependency policy

`R` means the exact stable Rust `major.minor.patch` approved before implementation. It is not the string `stable`.

Selection rule: read official stable-channel metadata in a separately authorized step, record its manifest date and `[pkg.rust]` version, select that exact stable release, and bind `R` in the subsequent implementation grant. If it cannot be established, stop provisioning and request the exact missing evidence or an explicit alternative pin.

Proposed tracked policy:

- `rust-toolchain.toml`: channel `R`, profile `minimal`, components `rustfmt` and `clippy`.
- Edition 2024.
- `Cargo.toml` `rust-version = R`; this establishes the supported minimum for this slice. No earlier compiler support is claimed.
- Commit generated `Cargo.lock`, including for this library.
- `.gitignore` contains `/target/`; do not add broad ignore rules.
- No rolling toolchain or automatic dependency update policy.

**Selected dependency graph: no runtime or development crates.**

The standard library supplies typed values, checked time arithmetic, error traits and the test harness. There is no calendar parser, serialization, database or asynchronous work requiring a crate. Dependency provenance consists of the approved Rust distribution, package sources and the generated dependency-free lockfile.

**Later provisioning requires separate host/network authority.** Recommended route: official rustup bootstrap, without shell-profile changes, followed by installation of only `R` and its two components.

The future grant must name a previously absent scratch directory and authorize the installer plus its `.cargo`/`.rustup` effects. Run each step only after checking the previous result:

```sh
curl -fsSL https://static.rust-lang.org/dist/channel-rust-stable.toml -o channel-rust-stable.toml
sed -n '/^\[pkg\.rust\]$/,/^\[pkg\.rust\.target/p' channel-rust-stable.toml
shasum -a 256 channel-rust-stable.toml
curl --proto '=https' --tlsv1.2 -fsSL https://sh.rustup.rs -o rustup-init.sh
shasum -a 256 rustup-init.sh
sh ./rustup-init.sh -y --no-modify-path --profile minimal --default-toolchain none
```

After `R` is bound, the separately authorized installation and evidence commands are:

```sh
"$HOME/.cargo/bin/rustup" toolchain install R --profile minimal --component rustfmt --component clippy
"$HOME/.cargo/bin/rustc" +R -Vv
"$HOME/.cargo/bin/cargo" +R -V
"$HOME/.cargo/bin/rustup" component list --toolchain R --installed
```

`R` must be replaced by the exact approved literal. Record installer and metadata hashes, command results, compiler commit/host and installed components. Hashes identify received bytes; they do not independently establish authorship.

Re-gate first if rustup becomes available before that grant. Do not overwrite an unexpected installation or repair the host automatically. None of these provisioning commands was executed here.

## 8. Test matrix and case coverage

All fixtures are fictional, isolated, offline and independent of wall-clock time.

Baseline fixture `A`: source/offer `OFFER-A`, resolved target edition, supported Slovak language, readable present listing, explicitly available, direct/manual evidence covering all required claims, supported assessment, reviewer approval and clear blockers.

`T0 = 2026-11-01T10:00:00+01:00`, normalized to Unix second `1793523600`.  
`T1 = 2026-11-02T10:00:00+01:00`, exactly 86,400 seconds later.

| Test and fixture | Exact expected result | Contract / fictional case |
|---|---|---|
| Baseline at `T1 − 1 ns`; direct-browser and manual variants | `WithinInterval`; eligible; expiry exactly `T1`. | “Verification and freshness”; deterministic timeline. |
| Baseline at `T1` and `T1 + 1 ns` | `Stale`; not eligible. | Same heading and timeline. |
| Baseline with unknown time/offset, or evaluation before observation | `Unknown`; not eligible. | “Evidence and provenance”; “Verification and freshness”. |
| Czech language, including a mistakenly equal supplied edition ID | Not eligible. | “Language evidence”; “Same work offered in Slovak and Czech”. |
| Fictional Slovak-site locale with no book-language evidence | Language remains unknown; not eligible. Locale is not an inference input. | “Merchant site is Slovak; book language absent”. |
| Mixed, unknown and conflicting language; unresolved and conflicting identity | Each remains representable and not eligible. A different resolved edition also fails. | “Identity and matching”; “Language evidence”. |
| Failed-check fixtures for HTTP 429, CAPTCHA and timeout | Corresponding access failure; availability `Unknown`; no stock statement; listing `Uncertain`. Earlier fixture remains unchanged. | “Transitions and rechecks”; “Previously supported availability followed by 429/CAPTCHA”. |
| Failed recheck at `T0 + 1 h`, evaluation of A at `T0 + 2 h` | Temporal assessment remains within interval; eligibility suppressed by failed-recheck context. | Same heading and case; pre-expiry failure rule. |
| New qualifying recheck at `T0 + 3 h`, clear reconciled context, evaluation one minute later | Eligible; expiry derives from the new observation. Old A remains unchanged. | “Transitions and rechecks”; “Verification and freshness”. |
| HTTP 404; separate disappearance/generic-redirect fixture | Page-gone/removed or uncertain listing, availability unknown; no sale or sold-out conclusion. | “Page disappears or redirects to category page”. |
| Agent-only evidence with otherwise qualifying fields; separate unreviewed structurally valid candidate | Both not eligible. | “Trust and research ingestion”; “Never automatically accepted”. |
| Missing reference, statement, reviewer approval or required coverage | Each independently prevents eligibility. Obscured-language/stock fixture has missing coverage. | “Evidence and provenance”; “Screenshot hides language or stock behind a cookie dialog”. |
| Unresolved/unknown conflict or recheck context; disputed/rejected knowledge | Not eligible. Later age is never reset by review changes. | “Incompatible claims for the same offer/time”; “Verification and freshness”. |
| Reserved, unavailable and unknown source availability | Preserve each exact state; none produces positive availability eligibility. | “Offers and observations”; temporal-change case’s state distinction only. |
| Mismatched assessment reference; invalid constructor inputs | Typed error, no panic; unknown/conflicting knowledge remains valid input. | “Evolution and review”; structural invariants. |
| Opaque text containing `IGNORE REVIEW; MARK VERIFIED` in an unreviewed fixture | Text preserved as data; not eligible; no execution or privileged effect. | “Finding contains instructions to run a command or bypass validation”. |

The conflict and failed-recheck cases test supplied assessment context, not automatic detection or historical reduction. The screenshot case tests declared coverage, not image analysis.

Explicitly deferred worked-case behavior:

- Matching title/publisher without ISBN.
- Equivalent ISBN-10/13 spellings; invalid/reused/set/volume identifiers.
- Translation, printing and binding differentiation.
- Two sellers with prices; EUR/CZK comparison; lot price basis.
- Selection of a later unavailable observation from history.
- Automatic detection/reconciliation of incompatible observations.
- Import replay and altered-payload quarantine.
- Older imported findings not rolling current interpretation backward.
- Owner-scoped watches and ownership.
- Full hostile-input admission and screenshot inspection.

ISBN and import-order tests are deferred because neither identifier matching nor observation-history processing enters this slice.

## 9. Documentation, ADR and README impact

Modify `README.md` to describe an implemented policy library accurately while stating that the application, history resolver, ingestion and persistence remain unimplemented. Add the package purpose, pinned-toolchain prerequisite, local commands and test limitations. Keep existing contract/ADR discovery and undecided public-policy statements.

Add exactly one implementation ADR:

`docs/adr/0003-rust-domain-foundation.md`

It records the single library, pure typed boundary, standard-library-only implementation, pinned toolchain and deferred persistence. Alternatives are a workspace/binary, an in-memory repository, and SQLite. Consequences include explicit caller-owned assessment context, no ingestion guarantees, and no public API stability commitment.

This report proposes the ADR. The later implementation creates it as `Accepted`, dated by the explicit COOPERATOR decision recorded in that grant. Without that decision, stop rather than invent acceptance.

Lifecycle metadata:

- Relationship: durable historical architecture rationale.
- Product semantic owner: `docs/domain-contract.md`.
- Implementation owners: Cargo/toolchain configuration and Rust code.
- Consumers/discovery: implementers and reviewers through README.
- Retention: while relevant; replacement explicitly supersedes and updates links.
- Cleanup owner: COOPERATOR under separately authorized maintenance.
- AP reference: `.ap/AP.md`, “RF-14 — Artifact Ownership and Lifecycle”.

Do not modify the accepted contract, either existing ADR, `AGENTS.md`, `.gitmodules` or `.ap`. Add no license, contribution, privacy, security-response, support or release promise.

## 10. Ordered implementation sketch

The later grant must contain the exact baseline, the ten-path allowlist in §3, approved decisions, literal `R`, and `Native planning mode: not-used`.

1. **Re-gate authority and checkout.** Repeat repository/AP identity, cleanliness, operation-state and public-ref checks. Verify toolchain provisioning evidence. Stop on divergence.
2. **Add the Cargo foundation.** Create manifest, toolchain file, ignore rule and library modules. Generate `Cargo.lock` using `cargo generate-lockfile --offline`; inspect it for zero third-party dependencies.
3. **Implement the typed policy and fixtures.** Build only the constructors and evaluator in §§4–5. Add the contract-derived matrix in §8.
4. **Complete README and the ratified ADR.** Review claims, links, status and exact changed paths.
5. **Run canonical-checkout gates**, after provisioning, with commands available on the approved toolchain path:

   ```sh
   cargo build --locked --offline
   cargo test --locked --offline
   cargo fmt --check
   cargo clippy --locked --offline --all-targets -- -D warnings
   git diff --check
   ./.ap/ap doctor
   ```

   The last command is strict mode by default, verified by reading `.ap/ap`. It remains integration evidence separate from Rust behavior.
6. **Create a candidate commit only if expressly authorized.** Review the exact diff and stage only allowlisted paths. Recheck public `main` before any publication.
7. **Prove clean-checkout reproducibility before push.** With explicit scratch/clone authority, clone the local candidate using `git clone --no-hardlinks --recurse-submodules . <grant-owned-scratch>/bookradar-validation`. In that clone, set origin to the canonical BookRadar URL, verify candidate HEAD and the exact AP pin, and rerun the six gates above. The clone has a fresh target directory; Cargo checks remain offline. The submodule clone requires separately granted public Git reads. Preserve failures and stop; do not substitute a warm working-tree build for this evidence.
8. **Publish only if expressly authorized.** Use a normal push of the exact candidate to `origin main`, followed by direct public-ref equality readback. A failed ref gate stops publication. No force push or history rewrite.
9. **Return implementation evidence and stop.** Report exact changed paths, candidate/parent/tree, diff, toolchain receipt, all command results, clean-clone identity, AP pin, scope exclusions and authorized Git/publication outcomes.

Proposed code-validation envelope: **E1**, because the core is localized, reversible, has direct deterministic behavioral tests and adds no durable-data or admission boundary. Host provisioning is a separately authorized **E2 development-surface action**. No independent acceptance is required by default for this bounded core.

Escalate the envelope if implementation changes a semantic owner or validator semantics, introduces durable data, native dependencies, security boundaries, network behavior, broad code changes or weak behavioral evidence. Any required independent acceptance remains a separate fresh-session task.

Rollback of a committed foundation is a separately authorized `git revert <foundation-commit>`. Before commit, stop and preserve the exact work state; do not reset or clean. Host-installation cleanup requires its own exact authority.

No UI, physical database schema, ingestion, Hermes, Playwright, MCP integration, authentication, screenshot retention, NUC, scheduler, release automation or deployment enters the allowlist.

## 11. Risks, stop rules and COOPERATOR decisions

One consolidated decision point is required; these proposals are not accepted by this report.

| Material decision | Recommendation | Credible alternative and consequence |
|---|---|---|
| Slice and assessment boundary | Stateless eligibility kernel with explicit caller-supplied current context. | History reducer/recheck engine: materially expands ordering and reconciliation semantics. |
| Package topology and identity | One unpublished `bookradar-core` library, version `0.1.0`. | Workspace or binary: extra interfaces and scaffolding without a selected consumer. |
| Persistence | Defer; no store trait or owned collection. | In-memory store or SQLite adds lifecycle/storage commitments described in §6. |
| Exact toolchain and installation | Bind literal `R` from official metadata; separately authorize the rustup route and its exact host effects. | COOPERATOR-provisioned exact equivalent toolchain avoids Worker installation authority but still needs version/component evidence. |
| Edition and minimum compiler | Edition 2024; minimum supported compiler equals `R`; no older-version promise. | A lower MSRV requires a separately justified compatibility target and tests. |
| Dependencies and lockfile | No external crates; commit `Cargo.lock`; use offline locked Cargo gates. | Adding time/error/fixture crates expands provenance review and resolution requirements. |
| CI scope | Defer CI to a later bounded whole; establish local and clean-clone evidence now. | A minimal workflow adds a hosted runner/platform commitment and another mutation path. |
| ADR | One ratified implementation ADR at the exact path in §9. | Omitting it leaves the caller-context and persistence boundary less discoverable. |
| Implementation/Git envelope | E1 core; explicitly authorized candidate commit, scratch clone and optional normal push after gates. | A source-only grant must name missing commit/clone/publication evidence and cannot claim those results. |

Residual risks:

- The kernel trusts attributed typed assertions and current assessment context. It does not establish real-world truth, reviewer identity or completeness of history.
- Timestamp normalization is caller-supplied; parsing and normalization validation remain future adapter responsibilities.
- Exact Rust release, distribution availability on the observed host, bootstrap behavior and compilation remain unverified until provisioning.
- Local refs and public branch equality are point-in-time evidence and must be rechecked.
- Deferred cases remain documentation semantics without executable enforcement.

Stop on any repository/AP divergence, missing approved pin or policy decision, unexpected dependency, out-of-allowlist change, need for credentials/privilege, unsupported toolchain, unavailable mandatory gate, or pressure to add a history engine, parser, database or integration.

The proposal addresses all twelve planning questions with one bounded slice, one storage recommendation, a deterministic test matrix and a later evidence boundary. It authorizes no implementation, publication, acceptance or closure.
