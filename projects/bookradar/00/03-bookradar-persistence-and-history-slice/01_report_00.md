### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-persistence-and-history-slice  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session profile: Planner  
Task identity: BOOKRADAR-PERSISTENCE-HISTORY-PLAN  
status: PASS  
Phase-qualified result: not-applicable  
Evidence tier: E0

| Repository | Start and end commit, unchanged |
|---|---|
| BookRadar | `bd23b08cd315a7b3c7a549479db59cbe6ad2adce` |
| AP | `d7023cf037f6d17885c3ede5c04812c61640da50` |

Changed files and purpose: none.

Validation performed: repository, public-ref, AP, source, documentation, historical Meta and environment inspection. Final worktree and index diffs were empty in both repositories. **No Rust build, storage implementation, dependency installation or test suite ran. No `ap` subcommand ran.**

Git result: no fetch, stage, commit or push. The only explicit network reads were two executions, at the opening and closing gates, of:

```sh
git ls-remote --symref https://github.com/cisarik/bookradar refs/heads/main HEAD
```

Both returned the expected BookRadar commit for symbolic `HEAD` and `refs/heads/main`.

Persistence: none. This complete report is returned in-session. The COOPERATOR owns persistence as `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_report_00.md` in `cisarik/meta` and subsequent paired prompt/report archival.

Missing evidence: dependency availability, the proposed binding’s compatibility and bundled SQLite build remain unverified. They require later dependency/network authority.

Smallest next step: ORCHESTRATOR reconciliation, followed by the consolidated COOPERATOR decision in §11 and a complete implementation grant if accepted.

Report justification: new-evidence  
Logical-whole closure: not-closed  
Authority expiry: this terminal report ends the grant; no autonomous continuation.

```text
Orchestration critique:
MEASURED: none
LEAD: none

Resolved Execution Issues / Near-Misses: Combined reading output was truncated. Smaller follow-up reads recovered the required material; no missing source was reconstructed from memory.
Pre-Existing Failure Classification: none
```

# BookRadar Persistence and History — Proposed Implementation Plan

This is a bounded implementation proposal. Its defaults are specified below; implementation remains approval-gated.

## 1. As-found state

Inspection date: 2026-11-11.

| Exact commands | Observed result |
|---|---|
| `pwd -P`; `git rev-parse --show-toplevel` | Physical working directory and Git root match the supplied BookRadar checkout. |
| `git remote -v` | Fetch/push origin is `https://github.com/cisarik/bookradar`. |
| `git status --porcelain=v1 --branch --untracked-files=all` | Clean `main`, tracking `origin/main`. |
| `git rev-parse HEAD`; `git rev-parse 'HEAD^{tree}'`; `git log -1 --format='%H%n%s%n%T%n%P'` | Expected commit; subject `feat: add BookRadar verification core`; tree `3298d133bf1cb7d1425c2b712924f94565ffec05`; parent `5c820abd439850039adf9866af26acfa15287493`. |
| `git for-each-ref`; `git worktree list`; `git ls-files`; `git ls-tree -r --name-only HEAD` | One worktree; expected committed files; local/remote-tracking `main` match. Auxiliary client refs exist under `refs/codex/turn-diffs/`. |
| `git submodule status`; `git ls-tree HEAD .ap` | One initialized submodule; gitlink matches the expected AP pin. |
| `git -C .ap rev-parse HEAD`; `git -C .ap status --porcelain=v1 --branch`; `git -C .ap remote -v` | Expected pin, clean detached HEAD, canonical `https://github.com/cisarik/ap.git` origin. |
| `git rev-parse --git-dir --git-common-dir`; operation/lock searches below | Standalone `.git`; no active Git operation or transaction lock. |
| `git diff --exit-code`; `git diff --cached --exit-code`, also inside `.ap` | Empty final worktree/index diffs; all exited 0. |
| Public-ref command above | Expected commit at both opening and closing gates. |

Operation-state inspection used:

```sh
find .git -name '*.lock' -o -name MERGE_HEAD -o -name CHERRY_PICK_HEAD -o -name REVERT_HEAD -o -name rebase-merge -o -name rebase-apply
find .git -type d \( -name rebase-merge -o -name rebase-apply -o -name sequencer \) -print
find .git -type f \( -name MERGE_HEAD -o -name CHERRY_PICK_HEAD -o -name REVERT_HEAD -o -name REBASE_HEAD -o -name index.lock -o -name HEAD.lock -o -name config.lock -o -name packed-refs.lock -o -name shallow.lock \) -print
```

The sole lock-named file was the zero-byte `.git/cursor/crepe/build.lock`, auxiliary editor metadata also documented in predecessor evidence. It was preserved.

Environment checks:

```sh
command -v rustc cargo rustup sqlite3 cc pkg-config
"$HOME/.cargo/bin/rustc" +1.99.1 -Vv
"$HOME/.cargo/bin/cargo" +1.99.1 -V
"$HOME/.cargo/bin/rustup" component list --toolchain 1.99.1 --installed
"$HOME/.cargo/bin/rustup" toolchain list
sqlite3 --version
cc --version
pkg-config --version
uname -sm
sw_vers
```

Observed: Rust/Cargo `1.99.1`, `rustfmt` and `clippy` installed; Rust commands absent from the ordinary PATH. Host: Darwin arm64, macOS 27.2. SQLite command: `3.54.0`; Apple Clang: `21.0.0`; pkg-config: `3.0.10`. SQLite development-library linkability was not tested.

All mandatory project and AP sources were available. The supplied attachment and prepared Meta prompt had identical SHA-256:

```text
9bc76eb4ed0ef158cf0dfe345686baed91bdf420e3c0ce8c84fe65e6aa99f5cf
```

The current whole’s notes, predecessor closure, accepted planning report and implementation report were read as historical evidence. No Meta Git operation or Meta write occurred.

**Accepted core boundary:** `bookradar-core` is dependency-free, unpublished and stateless. Its public checked constructors and getters cover identity, observations, timestamp assertions, evidence and assessment context. `evaluate_verification(target, observation, context, now)` owns eligibility and freshness. The 17 integration tests cover supplied-context policy; their source was inspected, not executed.

**Functional gap:** no durable store, history reader, current-observation resolver, derived conflict/recheck context or runnable persistence demonstration exists.

| Capability | Classification |
|---|---|
| Client/model | Codex client context **inferred**; exact client build/model **unknown/not observably exposed**. |
| Reasoning/context | High and approximately 250k **requested**; effective settings/capacity **unknown/not observably exposed**. |
| Native planning mode | **Directly observed** active through session configuration. |
| Filesystem reads | **Directly observed** for BookRadar, pinned AP, supplied attachment and named Meta context. |
| Shell/Git | Read-only execution **directly observed**. Writes were untested and ungranted. |
| Network | Canonical BookRadar public-ref reads **directly observed**; registry access untested. |
| Toolchain | Version/component reads **directly observed**; compilation untested. |
| SQLite/native build | SQLite command and C compiler **directly observed**; binding/cache/native build compatibility **unknown**. |
| Required planning capability | None missing. No subagents used. |

Capability grants no authority.

## 2. Functional PoC outcome

Provide a small **synthetic-only CLI**, backed by an on-disk store. Each invocation opens and closes the database, proving persistence across processes.

After separately authorized provisioning and build:

```sh
export PATH="$HOME/.cargo/bin:$PATH"
cargo +1.99.1 build --locked --offline -p bookradar-store --bin bookradar-poc

target/debug/bookradar-poc init target/bookradar-poc.sqlite
target/debug/bookradar-poc append-fixture target/bookradar-poc.sqlite available
target/debug/bookradar-poc current target/bookradar-poc.sqlite 1793548800
target/debug/bookradar-poc append-fixture target/bookradar-poc.sqlite blocked
target/debug/bookradar-poc current target/bookradar-poc.sqlite 1793548800
target/debug/bookradar-poc append-fixture target/bookradar-poc.sqlite recovered
target/debug/bookradar-poc append-fixture target/bookradar-poc.sqlite older
target/debug/bookradar-poc current target/bookradar-poc.sqlite 1793548800
target/debug/bookradar-poc history target/bookradar-poc.sqlite
```

`init` prints:

```text
created schema=1 synthetic=true
```

Each append prints `appended observation=N synthetic=true`, using the IDs below.

| Fixture | ID | Observed Unix second | Ingested Unix second | Assertion |
|---|---:|---:|---:|---|
| `available` | 1 | 1793523600 | 1793545201 | Readable, present, available |
| `blocked` | 2 | 1793527200 | 1793545202 | Rate-limited, uncertain listing, unknown availability |
| `recovered` | 3 | 1793534400 | 1793545203 | Readable, present, available |
| `older` | 4 | 1793520000 | 1793545204 | Readable, present, explicitly unavailable |

All use source 1, offer 1, target edition 10. Positive fixtures use synthetic manual evidence, complete claim coverage and attributed supported review. The blocked fixture uses `Observation::failed_check`. Original observation text retains the corresponding `+01:00` fixture timestamp; capture time equals observation time. Evidence/provenance references begin `synthetic:`. No real URL or evidence bytes are involved.

The three `current` calls print, respectively:

```text
synthetic=true latest_attempt=1 access=readable listing=present availability=available
candidate=1 temporal=within-interval conflict=clear recheck=clear verification=eligible
Checked available -- unix:1793523600; expires_unix=1793610000
```

```text
synthetic=true latest_attempt=2 access=rate-limited listing=uncertain availability=unknown
candidate=1 temporal=within-interval conflict=clear recheck=failed verification=not-eligible
Could not recheck -- unix:1793527200
Last observed available -- unix:1793523600
```

```text
synthetic=true latest_attempt=3 access=readable listing=present availability=available
candidate=3 temporal=within-interval conflict=clear recheck=clear verification=eligible
Checked available -- unix:1793534400; expires_unix=1793620800
```

`history` prints:

```text
synthetic=true offer=1/1 count=4
4 observed=1793520000 ingested=1793545204 access=readable listing=present availability=unavailable review=supported
1 observed=1793523600 ingested=1793545201 access=readable listing=present availability=available review=supported
2 observed=1793527200 ingested=1793545202 access=rate-limited listing=uncertain availability=unknown review=supported
3 observed=1793534400 ingested=1793545203 access=readable listing=present availability=available review=supported
```

The CLI has exactly four commands: `init`, `append-fixture`, `current`, `history`; exactly the four fixture names above; fixed synthetic identities; and no general input/import framework. `current` requires explicit integer Unix seconds. Conflict resolution and richer inputs are exercised through the library tests.

Exit behavior:

- `0`: successful operation, including empty history or non-eligibility.
- `2`: invalid arguments, fixture name or supplied time.
- `1`: filesystem, SQLite, unsupported schema, duplicate key or storage-range error.
- Errors go to stderr with a stable application error category. Non-eligibility is ordinary output.
- `init` refuses any existing path; other commands refuse missing databases without creating them.
- Empty current output is exactly `synthetic=true offer=1/1 target=10 status=empty`.

## 3. Architecture, crate and file tree

Retain the root package and add a workspace containing it and one dependent package:

```toml
[workspace]
members = [".", "crates/bookradar-store"]
default-members = [".", "crates/bookradar-store"]
resolver = "3"
```

`bookradar-store` is version `0.1.0`, edition 2024, `rust-version = "1.99.1"`, `publish = false`. It contains the store library and `bookradar-poc` binary.

Dependency direction:

```text
bookradar-poc → bookradar-store → bookradar-core
                              → rusqlite / bundled SQLite
```

The root package gains no dependency. Existing core sources and tests remain unchanged.

Proposed store API:

- `Store::create(path)` and `Store::open(path, ReadOnly | ReadWrite)`.
- `append(record, optional_initial_review)` atomically appends an observation and explicitly supplied initial review.
- `append_review(observation_ref, expected_revision, draft)` appends an attributed assessment revision.
- `history(offer_ref)` returns immutable observations, provenance and all review revisions.
- `current(offer_ref, target, now)` returns latest attempt set, candidate set, historical source claims, conflict/uncertainty details, constructed contexts and kernel assessments.

Use concrete types and ordinary errors, without a repository trait, async runtime, ORM or public SQL interface. `CurrentView` preserves sets where timestamps tie. No public API stability is promised.

`ObservationRecord` carries the core observation plus ingestion time, capture timestamp assertion, optional requested/resolved URLs and redirect reference, required provenance reference, and optional uncertainty rationale. `ReviewDraft` carries knowledge, optional approval, assessor reference, rationale, assessment time and recording time.

All repository-owned Rust uses `#![forbid(unsafe_code)]`. This does not describe the implementation of SQLite or third-party dependencies.

## 4. Storage decision and schema/format

| Option | Dependencies/native build | Migration, recovery and isolation | Portability and lock-in |
|---|---|---|---|
| In-memory only | Standard library | Easy isolated tests; no reopen durability | Portable, but fails the requested outcome |
| Versioned append-only file | Custom codec, or serialization dependencies | Must define framing, torn-tail handling, atomicity, locking and version changes; isolated temporary files | Portable; substantial custom format/recovery ownership |
| Pure-Rust embedded database, e.g. `redb` | Rust dependency graph; no SQLite C build | Transactions help recovery; application still owns encoding/schema upgrades; temporary database per test | Plausible macOS/Linux route, untested here; engine-specific file format |
| SQLite with system binding | Rust binding plus compatible system development library | Transactions, constraints and standard inspection tools; explicit schema versions; temporary files | Ubuntu/macOS viable, but system linking/version prerequisites differ |
| **SQLite with bundled binding** | Rust binding/transitives and bundled C compilation | Same transactional model with a reproducible engine source dependency | **Recommended**; avoids system SQLite linking prerequisites. Native build and schema ownership remain |

Use **bundled SQLite through `rusqlite`**, synchronous local operations, rollback journal mode `DELETE`, `synchronous=FULL`, foreign keys enabled, and immediate busy errors. No WAL, connection pool or concurrency service.

IDs occupy positive SQLite `INTEGER` values, therefore `1..=i64::MAX`. Larger valid core IDs return `OutOfStorageRange`; they are never truncated. Offer identity remains `(source_id, offer_id)`, with each offer key identifying one caller-selected generation. URLs are provenance, not identity.

Time encoding is `(signed Unix seconds, nanoseconds 0..999999999)`, with seconds rounded downward for pre-epoch instants. Nullable pairs represent absent instants. A nullable offset means explicitly unknown; retain the original representation separately. Convert with checked arithmetic. Ingestion/review times are caller-supplied normalized instants and never replace observation time.

The exact proposed initial DDL is:

```sql
CREATE TABLE sources (
    id INTEGER PRIMARY KEY CHECK (id > 0)
) STRICT;

CREATE TABLE editions (
    id INTEGER PRIMARY KEY CHECK (id > 0)
) STRICT;

CREATE TABLE offers (
    source_id INTEGER NOT NULL REFERENCES sources(id),
    id INTEGER NOT NULL CHECK (id > 0),
    PRIMARY KEY (source_id, id)
) STRICT;

CREATE TABLE observations (
    source_id INTEGER NOT NULL,
    offer_id INTEGER NOT NULL,
    id INTEGER NOT NULL CHECK (id > 0),

    subject TEXT NOT NULL
        CHECK (subject IN ('resolved','unresolved','conflicting')),
    edition_id INTEGER REFERENCES editions(id),
    language TEXT NOT NULL
        CHECK (language IN ('slovak','czech','mixed','unknown','conflicting')),

    observed_original TEXT,
    observed_offset INTEGER CHECK (observed_offset BETWEEN -64800 AND 64800),
    observed_s INTEGER,
    observed_ns INTEGER CHECK (observed_ns BETWEEN 0 AND 999999999),

    captured_original TEXT,
    captured_offset INTEGER CHECK (captured_offset BETWEEN -64800 AND 64800),
    captured_s INTEGER,
    captured_ns INTEGER CHECK (captured_ns BETWEEN 0 AND 999999999),

    ingested_s INTEGER NOT NULL,
    ingested_ns INTEGER NOT NULL CHECK (ingested_ns BETWEEN 0 AND 999999999),

    access TEXT NOT NULL CHECK (access IN (
        'readable','rate-limited','captcha','authentication-blocked',
        'timeout','transport-error','page-gone'
    )),
    listing TEXT NOT NULL CHECK (listing IN ('present','removed','uncertain')),
    availability TEXT NOT NULL
        CHECK (availability IN ('available','reserved','unavailable','unknown')),
    source_statement TEXT,

    evidence_method TEXT
        CHECK (evidence_method IN ('direct-browser','manual','agent-only')),
    evidence_reference TEXT,
    subject_covered INTEGER CHECK (subject_covered IN (0,1)),
    language_covered INTEGER CHECK (language_covered IN (0,1)),
    availability_covered INTEGER CHECK (availability_covered IN (0,1)),

    requested_url TEXT,
    resolved_url TEXT,
    redirect_reference TEXT,
    provenance_reference TEXT NOT NULL,
    uncertainty_rationale TEXT,

    PRIMARY KEY (source_id, offer_id, id),
    FOREIGN KEY (source_id, offer_id) REFERENCES offers(source_id, id),

    CHECK (
        (subject = 'resolved' AND edition_id IS NOT NULL)
        OR (subject IN ('unresolved','conflicting') AND edition_id IS NULL)
    ),
    CHECK ((observed_s IS NULL) = (observed_ns IS NULL)),
    CHECK (observed_offset IS NULL OR observed_s IS NOT NULL),
    CHECK ((captured_s IS NULL) = (captured_ns IS NULL)),
    CHECK (captured_offset IS NULL OR captured_s IS NOT NULL),
    CHECK (
        (evidence_method IS NULL AND evidence_reference IS NULL
            AND subject_covered IS NULL AND language_covered IS NULL
            AND availability_covered IS NULL)
        OR
        (evidence_method IS NOT NULL AND subject_covered IS NOT NULL
            AND language_covered IS NOT NULL
            AND availability_covered IS NOT NULL)
    )
) STRICT;

CREATE TABLE reviews (
    source_id INTEGER NOT NULL,
    offer_id INTEGER NOT NULL,
    observation_id INTEGER NOT NULL,
    revision INTEGER NOT NULL CHECK (revision > 0),
    assessed_s INTEGER NOT NULL,
    assessed_ns INTEGER NOT NULL CHECK (assessed_ns BETWEEN 0 AND 999999999),
    recorded_s INTEGER NOT NULL,
    recorded_ns INTEGER NOT NULL CHECK (recorded_ns BETWEEN 0 AND 999999999),
    knowledge TEXT NOT NULL
        CHECK (knowledge IN ('unreviewed','supported','disputed','rejected')),
    reviewer_approval TEXT,
    assessor_reference TEXT NOT NULL,
    rationale TEXT NOT NULL,
    PRIMARY KEY (source_id, offer_id, observation_id, revision),
    FOREIGN KEY (source_id, offer_id, observation_id)
        REFERENCES observations(source_id, offer_id, id)
) STRICT;

CREATE INDEX observations_by_time
    ON observations(source_id, offer_id, observed_s, observed_ns, id);

CREATE TRIGGER observations_no_update BEFORE UPDATE ON observations
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER observations_no_delete BEFORE DELETE ON observations
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER reviews_no_update BEFORE UPDATE ON reviews
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER reviews_no_delete BEFORE DELETE ON reviews
BEGIN SELECT RAISE(ABORT, 'append-only'); END;
```

Write/read validation additionally rejects empty present reference strings through core constructors and equivalent checks for store provenance. It preserves whitespace and opaque text; this is not an external-input validator.

Create the schema and set `application_id = 0x42524452` and `user_version = 1` in one transaction. Identity registries contain only asserted keys and are inserted transactionally with observations; no catalog descriptions or matching are introduced.

**Version/recovery policy:**

- Creation reserves a previously absent file exclusively. Existing files, including empty ones, are refused.
- Open validates application ID, version, expected journal mode, SQLite `quick_check` and foreign-key consistency.
- Only version 1 is supported. Existing version 0, unknown versions, malformed rows and corrupt databases fail closed.
- There is no automatic migration, reset, repair, row skipping or alternate-format fallback.
- SQLite provides transaction rollback/recovery. A read-only command never retries with write access when recovery needs it.
- Any later format change requires separately authorized migration design and preservation of existing data. No destructive synthetic-data cleanup is implied.
- These tables contain no work/author/copy, price, owner, research-run, screenshot or authentication schema.

## 5. History/current interpretation

Read one offer’s observations and reviews in a single SQLite read transaction. Never filter observations to the requested edition before selection: a newer different/unresolved subject must not revive an older matching offer.

1. **Preserve events.** Every attempt has a new observation key. Duplicate keys fail; no upsert or mutation is available. A duplicate-key error is not an implementation of research replay/quarantine.
2. **Order by normalized observation instant.** Compare seconds/nanoseconds, regardless of ingestion order. Original text and unknown offset remain intact. An unknown offset with a supplied normalized instant permits ordering, but the kernel still assesses its freshness as `Unknown`.
3. **Retain ties as sets.** History sorts known instants ascending, then observation ID for display; absent instants appear afterward by ID. IDs never adjudicate incompatible claims.
4. **Choose candidate content.** Use the maximal-time set of readable observations. If none exists, use the maximal-time attempt set. Do not fall back to an older eligible record when newer readable content is unavailable, unreviewed, rejected, Czech or otherwise unsuitable.
5. **Keep access separate.** Latest attempts and the latest explicit historical source-claim set remain separate outputs. A failed attempt does not acquire the previous availability.
6. **Derive failed recheck.** Any non-readable attempt at or after the candidate content time sets `RecheckState::Failed`, including equal-time success/failure ties. A strictly later readable candidate moves past earlier failures; only a qualifying kernel result can restore a positive label. Rejected review does not erase an access attempt or clear this chronology.
7. **Detect explicit equal-time incompatibility.** Within each exact-time group, compare differing resolved editions, explicit language claims, explicit availability statements and definite present/removed listing claims. Unknown/uncertain values supply no contrary claim; different evidence references or wording alone do not establish contradiction. Readable versus timeout alone is an access issue.
8. **Keep conflicts active until explicit assessment.** Any incompatible pair among non-rejected claims, intrinsic conflicting subject/language assertion, or active disputed review yields `ConflictState::Unresolved`. This applies across retained history. A newer observation alone does not clear it.
9. **Resolve without rewriting.** Append an attributed review rejecting the erroneous observation claim, with rationale. A pair ceases blocking only when at least one member is explicitly rejected; all remaining incompatible pairs still block. The original claims and review revisions remain visible. A later review can explicitly revise a disputed assessment.
10. **Handle unorderable events conservatively.** Any observation lacking a normalized instant prevents a positive current interpretation: use unknown context where no definite conflict/failure is established. Do not substitute ingestion time. Rejection of a claim does not invent its missing attempt time; repairing such chronology is deferred.
11. **Evaluate through the kernel.** Construct each candidate’s own context and call `evaluate_verification`. A positive result requires at least one `Eligibility::Eligible` candidate under the derived blockers. For compatible qualifying ties, display the lowest eligible observation ID and expose the complete candidate set. This is display selection, not claim priority.
12. **Separate evaluation time from historical queries.** `now` controls kernel freshness only. It does not hide future observations or simulate what had been ingested at a past instant. Future candidates therefore remain `Unknown` and non-eligible.

Review/ingestion never changes observation age. Exact expiry, stale/unknown boundaries and overflow handling remain entirely in the accepted kernel.

A single older import adds history without selecting an older current candidate. If an import reveals a previously unknown same-time contradiction, it may suppress verification through a newly established conflict; it still does not select the older state.

For the §2 timeline: observation 1 qualifies; attempt 2 suppresses its label while its temporal assessment remains within interval; observation 3 can qualify with its own expiry; importing observation 4 leaves candidate 3 unchanged.

Deferred: natural-language contradiction analysis, automatic reconciliation, external replay, missing-time repair, historical “as known then” queries, catalog identity reconciliation and full event sourcing.

## 6. Core integration and review state

Serialize through existing getters and reconstruct through existing checked constructors:

| Stored representation | Core reconstruction |
|---|---|
| Positive IDs and composite keys | `SourceId`, `OfferId`, `ObservationId`, `EditionId`, `OfferRef`, `ObservationRef` |
| Subject tag and optional edition | `SubjectIdentity` |
| Observed original/offset/instant | `TimestampAssertion::known` or `with_unknown_offset` |
| Separate dimension tags | Corresponding core enums |
| Optional statement/evidence fields | `SourceStatement`, `EvidenceReference`, `ClaimCoverage`, `EvidenceSupport` |
| Latest explicit review revision | `KnowledgeAssessment`, optional `ReviewerApproval` |
| Derived blockers and exact observation reference | `VerificationContext::new` |
| Candidate, target, context, injected time | `evaluate_verification` |

Absent evidence and present evidence with a missing reference remain different. Unknown offset with a present instant also round-trips distinctly from absent time.

No additive core API is necessary. No private-field access, serde derivation, SQLite dependency or duplicate 24-hour/eligibility implementation enters the core.

Review revisions form an explicit per-observation decision sequence. `expected_revision` must match the current revision inside an immediate write transaction; otherwise return `ReviewRevisionConflict`. Revision 1 requires no predecessor. Subsequent assessment times must not precede their predecessor. Missing review means unreviewed with no approval.

The revision sequence represents explicit assessment supersession, not observation-arrival priority. Adding an older observation cannot alter another observation’s review. There is no offer-wide mutable status or automatic approval propagation.

## 7. Test matrix

Use fresh owned temporary directories, close connections before reopen/cleanup, and inject every domain timestamp. A standard-library helper uses exclusive directory creation with process ID and an atomic counter; it uses no clock or random dependency.

Let `T0 = 1793523600` and `T1 = T0 + 86400`.

| Scenario | Exact expected result |
|---|---|
| Round-trip/reopen | All observation, provenance, optional evidence and timestamp fields compare equal; history/current results match before and after reopen. |
| Atomic append failure | Invalid initial review or duplicate observation rolls back the entire append; no partial observation/review/registry additions. |
| Append-only constraints | Update/delete attempts on observation/review tables fail; existing rows remain unchanged. |
| Schema identity/version | Fresh create opens as version 1; existing path, wrong application ID, version 0/2, corrupt file and foreign-key violation return errors without reset. |
| Transaction rollback | Dropping an uncommitted write leaves previously committed history unchanged after reopen. No power-loss guarantee is claimed. |
| Observation versus arrival order | Every insertion permutation of §2 observations selects candidate 3; displayed history IDs are `4,1,2,3`. |
| Newer negative/unsuitable content | Newer unavailable/reserved/unknown, Czech, different edition, unreviewed or rejected content prevents fallback to an older positive candidate. |
| Same-time incompatible claims | Supported available/unavailable pair yields unresolved conflict and no positive result, independent of insertion order. |
| Explicit conflict resolution | Newer qualifying evidence alone remains blocked. Attributed rejection of the erroneous claim clears that pair; all raw/review history remains. A third unresolved pair still blocks. |
| Compatible ties | Candidate sets remain intact; a compatible qualifying candidate can support eligibility; display ID does not resolve contrary claims. |
| 429/CAPTCHA/timeout/auth/transport | New attempt has unknown availability, uncertain listing and no source statement; earlier candidate becomes non-eligible without changing its observation time. |
| 404/disappearance/redirect | Page-gone is removed with unknown stock; generic readable redirect can remain uncertain/unknown. Neither reports a sale. |
| Failure then recovery | Failure at `T0+3600`: candidate at T0 remains `WithinInterval` but non-eligible. Qualifying recovery at `T0+10800`: eligible, expiry `T0+97200`. |
| Exact freshness | At `T1−1ns`: eligible. At `T1` and `T1+1ns`: stale/non-eligible. Later review and ingestion do not move T1. |
| Unknown/future time | Unknown instant or current unknown-offset assertion: `Unknown`, non-eligible. Future candidate: `Unknown`, no older fallback. Unorderable history blocks a known candidate through context without changing that candidate’s age. |
| Evidence/reviewer failures | Agent-only method; missing evidence/reference/statement/approval; each missing coverage field; disputed/rejected/unreviewed review: persisted and non-eligible as applicable. |
| Codec boundaries | Pre-epoch fractional time and nanoseconds round-trip; unknown-offset-plus-instant preserved; oversized ID or unrepresentable time errors without truncation. |
| Review revisions | Stale expected revision and backward assessment time fail; another observation’s newer review remains unchanged by older imports. |
| CLI process tests | Exact §2 transcript and exit codes; every invocation reopens storage; missing/existing paths and repeated fixture append fail without unintended changes. |

Retain the existing 17 core tests unchanged. New tests address storage integrity and resolver behavior absent from that suite.

Deferred: network, real evidence inspection, authentication, multi-process stress, actual crash/power-loss testing, Ubuntu execution and external-format migrations.

## 8. Toolchain, dependencies and gates

Keep Rust `1.99.1` and the existing toolchain file. Use `$HOME/.cargo/bin` explicitly or prepend it only for the current session.

Proposed manifest dependencies:

```toml
bookradar-core = { path = "../.." }
rusqlite = { version = "=0.37.0", default-features = false, features = ["bundled"] }
```

`0.37.0` is a **proposed fixed pin**, not a claim about the latest release, cache presence, security status or verified compatibility. No additional runtime/development crate is proposed. Bundled SQLite requires the observed C compiler; no system SQLite installation or pkg-config linking is selected.

Later provisioning must explicitly authorize:

- Registry/index/archive access needed by Cargo, bounded to crates.io infrastructure.
- Cargo registry cache writes and regeneration of the workspace `Cargo.lock`.
- Resolution of the pinned binding’s transitive graph and bundled native build artifacts.
- Inspection/reporting of exact resolved versions, checksums and compiled SQLite version.

Run dependency resolution/fetch only under that later grant, then validate offline. If the pin cannot resolve or build, stop with the causal evidence; do not silently change versions, use system SQLite or install host packages.

Commit the complete workspace lockfile. No automatic updates, vendoring, toolchain installation or host configuration changes are included.

Later canonical gates:

```sh
cargo +1.99.1 build --workspace --all-targets --locked --offline
cargo +1.99.1 test --workspace --locked --offline
cargo +1.99.1 fmt --all --check
cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D warnings
cargo +1.99.1 tree --locked --offline -p bookradar-core
git diff --check
./.ap/ap doctor
```

The core dependency tree must contain only `bookradar-core`. Strict `ap doctor` is proposed later integration evidence; its strict default was inspected in `.ap/ap`, and it was not executed here.

Use automated temporary-file/reopen tests plus the §2 transcript against a previously absent store. This satisfies fresh-store evidence without another clone or additional Git transport authority. CI remains deferred.

Proposed implementation evidence tier: **E2**, reflecting a local durable format and native dependency. Include one focused fresh read-only acceptance of schema/history behavior after implementation because this introduces a durable-data boundary. It is separate from implementation self-review; no recursive audit sequence is proposed.

## 9. README, ADR and lifecycle

Update `README.md` to document:

- The workspace and dependency-free core boundary.
- Bundled SQLite/C compiler prerequisites and authorized dependency provisioning.
- Offline workspace gates and the exact synthetic CLI transcript.
- Caller-selected database path; use under existing ignored `target/` for the example.
- Version-1-only opening, no automatic migration/reset, and error behavior.
- Synthetic evidence, injected time, historical labels and current limitations.

Add only `docs/adr/0004-local-persistence-and-history.md`. Record storage alternatives, bundled dependency choice, workspace boundary, schema/version policy, immutable observations/reviews, deterministic selection and conservative conflict handling.

Create ADR 0004 as Accepted only when the later grant records the COOPERATOR’s approval and date. This planning report does not assign that status.

Lifecycle: durable historical architecture rationale; product semantics remain owned by the accepted domain contract; implementation is owned by store code/schema and Cargo files. Discover through README. Retain while relevant; supersession updates links; cleanup belongs to the COOPERATOR under separate authority.

Do not modify the contract, ADRs 0001–0003, AP pin, managed instructions or toolchain. Select no license, contribution, privacy, security-response, support or release policy.

## 10. Ordered implementation sketch

Exact proposed source allowlist:

```text
Cargo.toml
Cargo.lock
README.md
docs/adr/0004-local-persistence-and-history.md
crates/bookradar-store/Cargo.toml
crates/bookradar-store/src/lib.rs
crates/bookradar-store/src/store.rs
crates/bookradar-store/src/history.rs
crates/bookradar-store/src/fixtures.rs
crates/bookradar-store/src/schema_v1.sql
crates/bookradar-store/src/bin/bookradar-poc.rs
crates/bookradar-store/tests/persistence.rs
crates/bookradar-store/tests/history.rs
crates/bookradar-store/tests/cli.rs
crates/bookradar-store/tests/common/mod.rs
```

No `.gitignore` change is needed: `/target/` is already ignored.

1. **Re-gate.** Verify complete renewed authority, exact baseline, clean checkout/AP, public refs and toolchain. Same-session implementation is suitable only if continuity remains healthy.
2. **Provision dependencies under explicit authority.** Add workspace/store manifest, resolve the proposed pin, generate/fetch the lockfile and inspect the graph. Stop on unexpected native/provisioning requirements.
3. **Implement storage.** Add schema, checked encoding, exclusive creation, validated opening, transactional append/review operations and round-trip/recovery tests.
4. **Implement interpretation.** Add snapshot reads, chronological sets, conflict/recheck derivation, kernel integration and the §7 history cases.
5. **Add the bounded CLI.** Implement four commands and synthetic fixtures; verify complete process output and failures.
6. **Complete documentation.** Add the ratified ADR and truthful README. Review all changed paths and claims.
7. **Validate.** Run §8 gates once for the completed candidate and capture the fresh-store transcript. Diagnose any failure narrowly before repeating broad gates.
8. **Report candidate.** Return exact diff/path list, dependency/native versions, command results, persistence/reopen and negative-path evidence, unchanged core/AP identity, and limitations.
9. **Acceptance/publication remain separate.** ORCHESTRATOR routes the focused fresh acceptance. Commit, stage or normal push occurs only if the subsequent grant expressly authorizes it and specifies its sequencing.

Rollback: preserve owner work on failure; never reset/clean automatically. A committed change is undone only by a separately authorized revert. Existing databases are never deleted or downgraded by rollback. Tests clean only their exact newly created temporary stores; the CLI demonstration database is retained unless exact cleanup is authorized.

The later report must distinguish implementation evidence, independent acceptance, Git publication and logical-whole closure. No NUC, live data, deployment or production claim follows from these checks.

## 11. Risks and Cooperator decisions

One consolidated decision point remains after ORCHESTRATOR reconciliation:

| Decision | Specified recommendation/default | Consequence / alternative |
|---|---|---|
| Durable engine and native dependency | Bundled SQLite with proposed exact `rusqlite =0.37.0` pin | Authorize bounded registry/cache/native-build effects. System linking changes prerequisites; a file or pure-Rust engine changes storage design. |
| Package/binary topology | Root core plus one dependent store crate containing the small CLI | Keeps native dependencies outside the accepted core; a separate CLI crate adds unnecessary packaging for this slice. |
| Format and migration boundary | Exact schema v1 above; checked signed storage ranges; reject unsupported existing formats | No data deletion or automatic migration. Broader compatibility requires another authorized boundary. |
| Current/review/unknown-time rules | §5–6, including explicit review revisions, observation-time selection and conservative unorderable-history blocking | No ingestion-order priority, automatic conflict repair or fallback to older eligible content. |
| Conflict lifetime | **Selected by COOPERATOR during this exchange:** explicit attributed resolution required | Newer successful evidence alone cannot clear an unresolved conflict. Implement through attributed rejection of erroneous claims. |
| Runnable proof | Four-command synthetic CLI and fixed fixtures | Proves durability without selecting a research input format, general application or UI. |
| ADR, validation and CI | Ratify ADR 0004; E2 local gates, fresh-store proof and one focused fresh acceptance; defer CI | Establishes durable/native-boundary evidence without release infrastructure. |
| Later authority | Complete same-session implementation renewal if healthy, with the allowlist and bounded dependency effects | Current report grants no execution, Meta write, Git publication or closure authority. |

Residual risks:

- Typed assertions and reviewer references remain caller-supplied; no evidence inspection or authentication exists.
- Bundled compilation and the proposed dependency graph remain unverified.
- An unorderable attempt conservatively blocks positive interpretation; chronology repair is deferred.
- A newly discovered historical contradiction can suppress a current label until explicit resolution.
- Native power-loss behavior, simultaneous-process stress and Ubuntu execution are not proved by the proposed local tests.
- Public refs are point-in-time evidence and must be rechecked before implementation/publication.

Stop later implementation on baseline/AP divergence, unavailable mandatory gates, incompatible dependency/native requirements, unexpected existing data, need for migration or semantic-owner changes, missing material approval, or any out-of-allowlist/network/host requirement. Preserve evidence and return the smallest exact decision needed.
