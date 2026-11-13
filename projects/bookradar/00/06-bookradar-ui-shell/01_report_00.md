### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BOOKRADAR-UI-SHELL-PLAN
Planning cycle: initial
Automatic targeted revisions used: 0

status: PASS
Phase-qualified result: not-applicable
Start commit: a2182302de73cb345b4b646993a1ad25d602555f
End commit: a2182302de73cb345b4b646993a1ad25d602555f
Changed files: none
Tests and validation: read-only repository, source, fixture, protocol, toolchain, public-ref and CI inspection; strict ./.ap/ap doctor PASS; no builds or tests run.
Git result: none; no fetch, stage, commit or push.
Deviations, risks, or missing evidence: no planning blocker; runtime and rendered evidence intentionally deferred. This session lacks Playwright; the COOPERATOR selected a provisioned fresh acceptance Worker.
Smallest next step: ORCHESTRATOR presents the proposed decisions below for COOPERATOR approval.
Report justification: new-evidence
Logical-whole closure: not-closed
```

Persisted prompt SHA-256: `f38aa7decb5b26efa06b6e463ae560b8944f96a91aea13749dd47714438d40e4`.

Received attachment SHA-256: `b2ac54f00bc9b8aaf9c605c981abf449df882b0802b11149798a6575bd52d9e3`.

The persisted prompt adds one final newline; its content otherwise matches the attachment. The handout and predecessor closure hashes match those declared in the prompt. Both were treated as historical evidence.

Report delivery is this complete session response, for COOPERATOR persistence at `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_00.md`. That file was absent when checked. No report or other trace file was written.

## BookRadar — Minimal local read-only UI shell

Implement one English-language, server-rendered page in a new unpublished workspace crate, `bookradar-ui`. It will display observation history/current assessment and research-ledger/current-candidate information together. Use the Rust standard library for a deliberately restricted loopback HTTP surface and add no external dependencies.

Capture both read models at startup using an explicitly supplied evaluation instant, close the database connections, and serve an immutable HTML snapshot plus embedded CSS. Restarting the process changes the query, evaluation instant, or loaded data. This is a synthetic local demonstration, with no continuous monitoring or automatic rechecking.

The recommendations below form one complete proposed implementation route. They remain approval-gated; the provisioned browser-acceptance Worker route was selected by the COOPERATOR during this exchange.

## 1. Verified baseline and functional gap

| Check | Direct observation |
|---|---|
| Physical checkout/topology | `/Users/agile/Projects/bookradar`; standalone checkout; `.git` is its Git directory |
| Remote | `origin` fetch/push: `https://github.com/cisarik/bookradar` |
| Branch and HEAD | `main`, `a2182302de73cb345b4b646993a1ad25d602555f` |
| Parent | `d7d49ab6df2d2fd063644700095d5e55a94e4ae1` |
| Tree | `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7` |
| Subject | `fix: restore target ignore and run the gates in CI` |
| Local tracking state | `origin/main` matches HEAD; ahead/behind counts `0/0` |
| Public refs | Read-only `git ls-remote --symref` confirmed symbolic HEAD and `refs/heads/main` at the expected SHA |
| Cleanliness | Empty porcelain status and diff at final inspection |
| Ignore rules | Exact `/target/` and `/tests/target/` matches confirmed |
| AP | Gitlink and detached, clean checkout at `d7023cf037f6d17885c3ede5c04812c61640da50`; strict doctor PASS |
| Toolchain | Rust and Cargo `1.99.1`; Apple Clang `21.0.0` available |
| Execution contract | No `ap.project.conf`; canonical project gate is `bash scripts/verify.sh` |
| Public CI | `verify`, push to `main`, completed/success, expected head SHA: [run 43438422059](https://github.com/cisarik/bookradar/actions/runs/43438422059) |

Read-only inspection covered the governing AP anchors, root instructions, manifests/lockfile, README, gate/workflow, contract revision 1, research-input v1, ADRs 0001–0006, core/store APIs and implementations, CLI implementations, test inventory, shared fixture helpers, and relevant test assertions. No nested crate instructions were found.

The source inventory matches **77 tests**: 17 core, 10 store unit, 4 observation CLI, 13 history, 6 persistence, 2 research CLI, 5 research-contract, and 20 research-ingestion tests. This is a static inventory; no local test execution is claimed.

The core already provides typed identity, timestamp, evidence and assessment dimensions, plus pure verification with the accepted 24-hour rule. The store provides append-only observation/review persistence, deterministic history/current selection, and a separate research ledger with replay, quarantine, conflict retention and unreviewed/disputed projections. The two existing binaries expose synthetic demonstrations through text transcripts.

The UI gaps are:

1. No rendered observation history or current assessment.
2. No rendered ledger, research candidates, quarantine or conflicts.
3. No consistent UI treatment of empty, missing, corrupt or unsupported databases.
4. No repeatable local UI demonstration.
5. No UI rendering/HTTP tests, browser acceptance or UI documentation.

## 2. Proposed surface, data interfaces and exact presentation

### Architecture choices

| Choice | Cost, footprint and acceptance implications | Recommendation |
|---|---|---|
| Server-rendered loopback HTML/CSS | Small Rust implementation; semantic HTML supports keyboard and browser inspection. Adds an inbound HTTP parsing boundary that requires the controls below. | **Select.** |
| Static page plus JSON endpoint | Adds a wire interface, JavaScript, client state and more CSP/testing decisions. | Defer. |
| TUI | A basic ANSI presentation can be small; robust terminal interaction/accessibility introduces additional implementation or toolkit work. Requires terminal-specific rendered acceptance. | Defer. |
| Native desktop shell | Adds framework, platform, packaging and acceptance work beyond the four read-only sections. | Defer. |

| Placement/dependency option | Tradeoff | Recommendation |
|---|---|---|
| New `crates/bookradar-ui` | Separates HTTP/presentation from persistence. Adds workspace membership and one local lockfile package entry. | **Select.** |
| Another store binary with private UI modules | Avoids workspace/lockfile changes, but places application HTTP code inside the persistence package. | Valid smaller alternative, not selected. |
| Standard-library HTTP/HTML | No additional registry graph, features or runtime. Maintainers own the restricted parser. | **Select**, bounded to this local shell. |
| External HTTP/TUI framework | Provides reusable infrastructure but adds dependency, feature, lockfile and provisioning decisions. | No dependency proposed. |

The new crate uses edition 2024, Rust `1.99.1`, version `0.1.0`, `publish = false`, and `#![forbid(unsafe_code)]`. Its only dependencies are paths to `bookradar-core` and `bookradar-store`; no dev dependencies are needed. Add it to workspace members and default members.

Keep every existing registry version, checksum and feature unchanged. The lockfile addition is only the local UI package and its two path dependencies. Compile-time impact is additional local Rust code; no timing estimate is claimed because builds were prohibited.

### CLI and snapshot behavior

```text
bookradar-ui
  --store <existing-observation-database>
  --research-ledger <existing-research-database>
  --now <signed-integer-unix-seconds>
  [--bind 127.0.0.1:<port>]
  [--producer <identifier>]
  [--source-ref <identifier>]
  [--listing-ref <identifier>]
  [--listing-generation <identifier>]
  [--target-edition <positive-integer>]
```

Defaults:

- Bind: `127.0.0.1:0`; print and flush `listening=http://127.0.0.1:<actual-port>`.
- Observation offer: `synthetic_offer()` — source `1`, offer `1`.
- Target: `synthetic_target()` — edition `10`; an explicit target applies to both assessments.
- Research key: `synthetic:producer`, `synthetic:source`, `OFFER-A`, `generation-1`.
- Evaluation instant: required, without a wall-clock default.
- Queries are supplied through CLI arguments and displayed on the page. There are no query forms or URL parameters.

Validate all arguments before database or socket I/O. Reject missing/duplicate/unknown options, invalid identifiers, invalid targets, unrepresentable times and disallowed binds with exit `2` and a stable `usage:` message. Use checked timestamp arithmetic. `--help` exits `0` without opening files or a listener.

Load each database independently through literal `OpenMode::ReadOnly`. A failed slot becomes an error panel while the other slot remains usable. Database errors do not prevent the diagnostic page from being served. Listener/startup transport failure exits `1`; there is no address fallback or browser auto-launch.

The prepared fixtures must be closed before launch. These are independent startup reads, with no cross-database transaction or concurrent-writer consistency claim.

### API audit and the one additive helper

| Existing interface | UI use and exposure finding |
|---|---|
| `Store::open`, `history`, `current` | Open read-only; load the selected offer’s history and accepted current assessment. |
| `HistoryEntry` | `record()` and `reviews()` already expose the required data. |
| `ObservationRecord`, `ReviewRevision` | Existing getters cover provenance, timestamps, evidence and every requested review field. |
| `CurrentView` | Existing getters expose attempts, unorderable records, candidates, historical claims, conflict and recheck. Private `observation_count` needs no getter: use history length and `is_empty()`. |
| `CandidateAssessment`, `StockClaim` | Existing getters expose record/context/assessment and dated historical claims. Eligibility already includes the authoritative expiry instant. |
| `ResearchStore::open`, `inspect`, `current` | Open read-only; obtain the transactional ledger snapshot and accepted candidate assessment. |
| `ResearchSnapshot`, `InputView`, `FindingView` | Required fields are public. The latter two names are not re-exported, but their vectors can be traversed through `ResearchSnapshot` without naming those types. No re-export is required. |
| `ResearchOfferKey` | Fields are private; validate using `try_new`. Retain the four operator-supplied strings for display, so no getter is needed. |
| `synthetic_offer`, `synthetic_target` | Supply the fixed observation query and target default. |
| Existing transcript renderers | Preserve `render_current`, `render_history`, `render_inspect` and `render_research_current` unchanged in observable output. Do not parse their transcripts into a UI model. |

Current truth-label selection is private in `history.rs`. Expose one read-only formatter:

```rust
pub fn render_current_labels(
    view: &CurrentView,
    target: EditionId,
    now: SystemTime,
) -> Vec<String>;
```

Reuse the existing `human_lines` implementation and route `render_current` through that shared implementation. Return no labels for an empty view. Preserve existing CLI bytes and all selection predicates. Export the helper from the store library.

The UI applies only presentation substitutions to generated labels: ` -- ` becomes ` — `, `unix:` becomes `Unix `, and `; expires_unix=` becomes `; expires at Unix `. This introduces no freshness or selection logic.

The UI contains **no SQL**, JSON admission parser, freshness interval, conflict reducer, recheck reducer or verification-policy implementation. Its loader creates owned presentation data; its renderer performs no I/O.

### Page structure and visual defaults

Use one page titled **BookRadar**, with four anchored sections in this order:

1. **Current assessment**
2. **Observation history**
3. **Research ledger**
4. **Research current candidates**

Show **“Synthetic data · Local · Read-only”** and **“Evaluation instant — Unix …”** above the sections. Explain that the snapshot and evaluation instant remain fixed until restart.

Use English, system fonts, a single-column layout up to `72rem`, white panels on a light neutral background, dark text and blue focus/link accents. Use a 16px base size and 1.5 line height. Truth labels are prominent text, without green availability badges. Provide a skip link, logical headings, visible keyboard focus, native `<details>` disclosures, labelled tables and contained table overflow on narrow screens. Long stored text wraps and preserves whitespace. No images, remote assets, animation or design-system framework.

### Exact truth and state presentation

| Area | Required presentation |
|---|---|
| Observation history | Observation/source/offer IDs; subject state and resolved edition when present; language; access; listing disposition; **Source-reported availability**; attributed source statement; evidence method/reference and separate subject/language/availability coverage; requested/resolved URLs and redirect reference; provenance and uncertainty. |
| Timestamps | For observed and captured times, show original text, offset as known with seconds east of UTC or `unknown`, and the supplied Unix instant or `unknown`. Show ingestion time separately. Preserve nanoseconds and represent pre-epoch instants with explicit signed seconds and nanoseconds. Do not parse original timestamp text or apply its offset again. |
| Reviews | Show every revision in existing order, with revision number, knowledge, approval reference or `not recorded`, assessor reference, rationale, assessed time and recorded time. An observation without reviews says **“No review recorded.”** |
| Current assessment | Show all candidate IDs, latest attempts, unorderable observations, temporal assessment (`within-interval`, `stale`, `unknown`), conflict (`clear`, `unresolved`, `unknown`), recheck (`clear`, `failed`, `unknown`) and verification eligibility (`eligible`, `not-eligible`). Use returned expiry values. |
| Research ledger | Show envelope/run/finding/projected-observation/review counts, plus edition count if useful for demonstrating the existing zero-edition projection. Receipt rows show receipt ID, disposition and reported outcome or `unknown`. Finding rows show receipt/position, `admitted`/`replayed`/`rejected`/`quarantined`, reason, knowledge when recorded, and projected observation ID or `not projected`. |
| Research candidates | Display the complete queried key, operator-supplied target and evaluation instant. Label cards **“Research candidate — unreviewed”** or **“Research candidate — disputed”**, with **“Unverified”**, application evidence method `agent-only`, approval absence, temporal/conflict/recheck fields and `not-eligible`. Display source assertions as attributed data. |

The observation current section uses exactly these generated label families:

- **Checked available — [time]; expires at [time]**
- **Last observed available — [time]**
- **Last observed reserved — [time]**
- **Last observed unavailable — [time]**
- **Could not recheck — [time]**
- **Listing removed — [time]**
- **Unverified — unresolved conflict**
- **Unverified — observation order unknown**
- **Unverified — observation time in future**
- **Unverified — observation offset unknown**
- **Unverified — observation time unknown**
- **Unverified — source availability unknown**
- **Unverified — insufficient support**

Preserve the existing formatter’s precedence and supplementary historical/access lines. Show candidate facets alongside generic insufficient-support wording; do not invent detailed eligibility reasons that the API does not return.

Include: **“Verification describes an evidenced source observation, not a guarantee that a purchase will succeed.”**

Research rendering never generates a positive verification label. If a loaded research assessment violates the expected unreviewed/disputed, agent-only, not-eligible invariants, show **“Unexpected research assessment — verification display suppressed”** as a UI error rather than promoting it.

Identical replay creates no new receipt. Display `replayed` only when a stored finding row actually has that outcome. Do not fabricate import activity. Raw/canonical research payloads are not rendered or reinterpreted; opaque quarantine retains its receipt disposition without invented per-finding reasons.

| Empty/error condition | Exact treatment |
|---|---|
| No observation history | **“No observations for this offer.”** No positive current label. |
| Empty research ledger | **“Research ledger is empty.”** Show zero counts. |
| No research candidate for a valid query | **“No research candidates for this query.”** Preserve any ledger rows. |
| Missing path | **“Database not found (not-found).”** Do not create it. |
| Corrupt database | **“Unsupported database (unsupported-schema: corrupt-database).”** |
| Wrong application ID, including swapped slots | Same category with `application-id`. |
| Unsupported schema version | Same category with `user-version`. Preserve other existing format-reason codes. |
| Other read failures | Stable `filesystem` or `storage` category and a controlled message; no OS/SQLite-dependent text is required for rendering. |
| Invalid operator input | CLI `usage:` error and exit `2`, before I/O. URL query strings are not accepted. |

Text, timestamps and explicit unknown/not-recorded values carry every meaning. The UI generates no **“Sold out”**, **“In stock”**, unqualified green **“Available”**, or automatically promoted **“Verified”** status. Stored source wording remains attributed, escaped data.

## 3. Local security and deterministic tests

### HTTP boundary

- Accept only a literal IPv4 socket address whose IP is exactly `127.0.0.1`. Default to an ephemeral port. Reject `0.0.0.0`, other addresses, hostnames and IPv6 before opening databases.
- Serve only `GET`/`HEAD` for `/` and `/style.css`. CSS comes from `include_str!`; there is no runtime asset directory. Other methods return `405` with `Allow: GET, HEAD`; other targets return `404`.
- Accept only origin-form HTTP/1.1 requests. Reject absolute URLs, query strings, traversal forms and malformed framing; do not decode paths into filesystem names.
- Bound headers to 8 KiB and 64 fields. Use a two-second total header-read deadline and two-second write timeout. Monotonic time may enforce transport deadlines; `SystemTime::now()` is forbidden for UI/domain evaluation.
- Handle one request per connection and send `Connection: close`. Reject transfer encoding, duplicate framing headers and nonzero content length. Do not process pipelined requests.
- Require one `Host` matching `127.0.0.1:<actual-port>`. Reject foreign hosts/origins and explicit cross-site fetches. Do not enable CORS.
- Escape `&`, `<`, `>`, `"`, and `'` in every displayed operator/stored string. Keep stored URLs/references as plain text, with no navigation, command execution or file opening.
- Apply security headers to normal and error responses:

```text
Content-Security-Policy: default-src 'none'; script-src 'none'; style-src 'self'; img-src 'none'; font-src 'none'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'
X-Content-Type-Options: nosniff
Cache-Control: no-store
Referrer-Policy: no-referrer
Cross-Origin-Resource-Policy: same-origin
```

Use explicit UTF-8 HTML/CSS content types and byte-accurate content lengths. `HEAD` returns the corresponding headers without a body. Avoid a variable wall-clock response header.

There are no database writes, creation, migrations, imports, reviews, promotions, repairs, outbound connections, external assets, telemetry, credentials, accounts or personal-state features.

### Test infrastructure

Add **17 focused tests**, preserving all 77 existing tests and assertions. Reuse the existing guarded `TempDir` and synthetic sample helpers through the new UI test-support module. Prepare fixtures before calling production read-only loading. Schema-error fixtures may alter copied database headers using standard-library file I/O strictly inside their temporary directory; production UI code performs no such inspection or mutation.

Pure rendering takes an already loaded snapshot. Process tests use the actual UI binary, `127.0.0.1:0`, bounded socket/startup waits, and a child guard that kills and waits for its exact process on success or panic. No fixed ports, wall-clock domain values, credentials, browser framework or network other than loopback.

All paths in the following tables are relative to `crates/bookradar-ui/`.

| File and test function | Setup | Expected result and regression covered |
|---|---|---|
| `tests/render.rs` — `renders_both_stores_and_pinned_context` | Four observation fixtures and partial/replay/conflict research imports at fixed instants. | Four sections, configured identities/time, observation candidate 3 and research counts `2/1/4/1/2`; closes the absent combined presentation path. |
| `tests/render.rs` — `renders_every_current_truth_label` | Table of qualifying fresh/expired, reserved, unavailable, blocked, removed, conflicting and unsupported observations using accepted sample APIs. Include exact expiry and the immediately preceding instant. | Correct generated wording/expiry and suppression; no forbidden generated stock labels. Catches UI overrides of accepted assessment results. |
| `tests/render.rs` — `preserves_unknown_time_identity_language_and_review_details` | Samples with absent/unknown-offset/future timestamps, nanoseconds and pre-epoch time; unresolved/conflicting subjects, Czech/unknown language, incomplete evidence and multiple reviews. | Every requested field remains distinct and visible, including original text and all revisions; catches flattening or omitted uncertainty. |
| `tests/render.rs` — `escapes_hostile_observation_and_research_text` | Put HTML/script fragments, quotes, ampersands and embedded command text into observation fields and a valid synthetic research finding. | Escaped text, no active markup or executable/navigation sink; covers both untrusted data sources. |
| `tests/render.rs` — `renders_research_outcomes_without_promoting_candidates` | Partial import, identical replay, changed reported outcome to retain replay rows, then conflicting F1. Include an unexpected presentation-state fixture. | All four finding outcomes, receipt outcomes, absent projections and unreviewed/disputed states; always no positive research label, with unexpected states suppressed. |
| `tests/render.rs` — `distinguishes_empty_missing_and_no_candidate_states` | Empty compatible stores, missing paths, and a populated ledger queried with an unknown valid key. | Distinct messages, retained healthy-slot content, and no missing-file creation; prevents empty/error conflation. |
| `tests/render.rs` — `renders_corrupt_swapped_and_unsupported_schema_errors` | Corrupt bytes, version 0/2 copies, wrong application ID and swapped database slots. | Stable `unsupported-schema` reasons, unchanged input bytes and no repair/fallback. |
| `tests/render.rs` — `rendering_is_byte_identical_for_identical_inputs` | Render the same loaded snapshot repeatedly. | Byte-identical HTML and stable ordering, independent of wall time or listener port. |
| `tests/http.rs` — `serves_loopback_dashboard_and_embedded_stylesheet` | Start actual binary with populated fixtures and ephemeral binding. | Printed nonzero loopback port; `/` and CSS return correct types/content; no external resources or runtime file serving. |
| `tests/http.rs` — `head_returns_get_headers_without_bodies` | GET and HEAD both routes. | Matching status/content metadata, correct content length, empty HEAD body. |
| `tests/http.rs` — `rejects_mutating_methods_and_non_allowlisted_targets` | Send POST/PUT/DELETE/OPTIONS and unknown, traversal, encoded traversal, query and absolute-form targets. | Appropriate `405`, `404` or malformed-request `400`; no file content or mutation. |
| `tests/http.rs` — `enforces_host_origin_and_response_headers` | Valid requests, foreign/missing/duplicate Host, foreign Origin and cross-site metadata. | Valid requests succeed; foreign-origin cases return `403`, missing/duplicate Host returns `400`; required headers on all responses, no CORS permission. |
| `tests/http.rs` — `bounds_requests_and_rejects_ambiguous_framing` | Oversized/many headers, malformed requests, body lengths, transfer encoding, incomplete headers and pipelining. | `431` for header limits, `400` for invalid framing, `408` for incomplete-header timeout, one response per connection; subsequent valid requests still work. |
| `tests/http.rs` — `serving_never_changes_databases_or_creates_missing_files` | Record database bytes/directory entries, serve repeated requests, then exercise missing-path startup. | Files remain byte-identical, no sidecars/created databases, missing paths stay absent. |
| `tests/cli.rs` — `invalid_operator_arguments_exit_before_database_or_socket_io` | Missing `--now`, malformed/range-invalid times/targets/keys, duplicate/unknown flags; help case. | Usage failures exit `2` without listener or file creation; help exits `0` without I/O. |
| `tests/cli.rs` — `non_loopback_binds_are_rejected` | Wildcard, external and other IPs, hostnames, IPv6 and invalid ports. | Exit `2` before file/socket I/O; no DNS resolution or fallback. |
| `tests/cli.rs` — `bind_failure_exits_without_address_fallback` | Reserve an ephemeral loopback port, then request that port in the UI child. | Exit `1` with stable bind-failure category and no alternative listener. |

The existing tests establish kernel/store behavior; these additions establish its presentation and the new HTTP boundary.

## 4. Runnable demonstration, documentation and CI

### Proposed README demonstration

Run from the repository root after implementation. The canonical gate builds the binaries. The import wrapper requires the existing expected partial/quarantine exit `3`.

```bash
bash <<'SH'
set -euo pipefail
export PATH="$HOME/.cargo/bin:$PATH"
bash scripts/verify.sh

ui_demo_dir=$(mktemp -d "$PWD/target/bookradar-ui-demo.XXXXXX")

target/debug/bookradar-poc init "$ui_demo_dir/observations.sqlite"
for ui_fixture in available blocked recovered older; do
  target/debug/bookradar-poc append-fixture \
    "$ui_demo_dir/observations.sqlite" "$ui_fixture"
done

target/debug/bookradar-research init "$ui_demo_dir/research.sqlite"

ui_expect_partial() {
  local ui_import_status=0
  "$@" || ui_import_status=$?
  test "$ui_import_status" -eq 3
}

ui_expect_partial target/debug/bookradar-research import \
  "$ui_demo_dir/research.sqlite" \
  crates/bookradar-store/tests/fixtures/research/partial.json 1793545201

ui_expect_partial target/debug/bookradar-research import \
  "$ui_demo_dir/research.sqlite" \
  crates/bookradar-store/tests/fixtures/research/partial.json 1793545202

ui_expect_partial target/debug/bookradar-research import \
  "$ui_demo_dir/research.sqlite" \
  crates/bookradar-store/tests/fixtures/research/conflict.json 1793545203

target/debug/bookradar-ui \
  --store "$ui_demo_dir/observations.sqlite" \
  --research-ledger "$ui_demo_dir/research.sqlite" \
  --now 1793548800 \
  --bind 127.0.0.1:0 \
  --producer synthetic:producer \
  --source-ref synthetic:source \
  --listing-ref OFFER-A \
  --listing-generation generation-1 \
  --target-edition 10
SH
```

Open the printed loopback URL manually; stop with Ctrl-C. The UI performs none of the fixture-writing commands.

Expected main demo: observation history IDs `[4,1,2,3]`, current candidate `3`, checked-available expiry Unix `1793620800`; research counts `2/1/4/1/2`, disputed candidate, unresolved conflict and `not-eligible`.

Document restarting with `--now 1793620800` to demonstrate expiry. Document preparing an additional store containing only `available` and `blocked` for failed-recheck acceptance. Empty databases come from the existing `init` commands; errors use explicitly separate missing/corrupt/swapped test paths. Do not overwrite existing stores to repeat a demonstration.

### Documentation and gate impact

Update README status/workspace diagrams, describe the new binary and arguments, add the exact demo, explain fixed-time snapshots, and state the loopback/read-only/synthetic boundaries. Retain the distinction between a UI shell and a running monitor.

Add `docs/adr/0007-local-read-only-ui-shell.md` after approval, recording the selected surface, crate placement, zero external dependencies, restricted HTTP model, shared label formatter, fixed evaluation time, tests and acceptance limitations. Record COOPERATOR ownership and the actual approval date. Product semantics remain owned by the existing domain contract.

Leave `docs/domain-contract.md`, `docs/research-input-v1.md`, ADRs 0001–0006, schemas, toolchain and existing store behavior untouched.

**No changes to `scripts/verify.sh` or `.github/workflows/verify.yml` are proposed.** Workspace build/test/fmt/clippy already cover the new crate, binary and tests. The canonical gate continues to require the one-line core dependency tree, locked fetch followed by offline execution, diff checks, strict AP doctor and clean state. CI gains no browser download, Node/Python dependency, secret or additional workflow.

Dependency provisioning remains the gate’s existing locked-fetch step. The UI, synthetic fixture operations, tests and browser flows require no external network.

## 5. Implementation stages, acceptance and delivery boundary

### Ordered stages and gates

1. **Approve and renew authority.** Reconcile this report and record the decision table. Issue a complete `current-worker-session` implementation prompt with native planning disabled, continuity anchor, unchanged baseline, exact allowlist and permissions. Plan approval alone grants no execution.
2. **Revalidate before edits.** Recheck checkout/public baseline, clean state, AP pin/doctor and toolchain. Stop and classify unexpected differences under RF-12.
3. **Add the shared label formatter and UI crate.** Preserve predicates and CLI output. Add only the local lockfile package; stop on registry graph/feature drift.
4. **Implement snapshot loading, rendering and restricted HTTP.** Complete the named focused tests and allowed-file formatting during development. Use focused checks for diagnosis; they do not replace the canonical gate.
5. **Review and commit once.** Inspect exact changed paths, diff and staged content; verify the public parent remains the expected baseline. Create one local commit with subject **`feat: add a local read-only UI shell`**.
6. **Verify the committed candidate.** Because the gate refuses dirty state, run **`bash scripts/verify.sh` after the local commit**. Require all existing/new tests, core-tree invariant, AP doctor and clean-state checks to pass. A failure stops publication; do not amend, weaken the gate or repeat it unchanged.
7. **Demonstrate locally and report implementation evidence.** Record fixed inputs, actual loopback origin, observed states and exact candidate SHA. This evidence is non-independent.
8. **Obtain separate independent and COOPERATOR acceptance.** Freeze the candidate throughout acceptance. Any correction requires renewed bounded authority and appropriate fresh re-acceptance.
9. **Publish only under a separate grant.** Follow the publication boundary below.

### Exact proposed changed-path allowlist

```text
Cargo.toml
Cargo.lock
README.md
crates/bookradar-store/src/history.rs
crates/bookradar-store/src/lib.rs
crates/bookradar-ui/Cargo.toml
crates/bookradar-ui/src/lib.rs
crates/bookradar-ui/src/main.rs
crates/bookradar-ui/src/config.rs
crates/bookradar-ui/src/snapshot.rs
crates/bookradar-ui/src/render.rs
crates/bookradar-ui/src/http.rs
crates/bookradar-ui/src/style.css
crates/bookradar-ui/tests/common/mod.rs
crates/bookradar-ui/tests/render.rs
crates/bookradar-ui/tests/http.rs
crates/bookradar-ui/tests/cli.rs
docs/adr/0007-local-read-only-ui-shell.md
```

Root manifest edits are limited to workspace membership/default membership. Store edits are limited to the additive formatter and export. Existing tests, store manifest, core sources, schemas, contracts, accepted ADRs, gate/workflow and `.ap` are outside the mutation boundary.

### Evidence and browser acceptance

```text
Evidence tier: E2
Evidence tier basis: reversible change across presentation, read interfaces and a local development HTTP surface; synthetic inputs, no durable writes, privileges, accounts or production effects.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: preserve all 77 accepted tests
Affected tests: existing CLI transcripts plus the 17 listed UI cases
New causal regression: rendered truth/uncertainty, escaping, read-only file preservation and restricted loopback HTTP behavior
Broad or full suite: required-because ADR 0006 binds bash scripts/verify.sh
Runtime or testbed: fixed-time synthetic demonstration on 127.0.0.1
Independent acceptance: required-separate-fresh-worker
```

The COOPERATOR selected a **provisioned fresh Worker** with existing Playwright/Chromium. No tooling installation is part of this task. Before issuing acceptance authority, the ORCHESTRATOR must establish that Worker’s usable adapter/runtime. This session’s installed Chrome `157.0.8103.39` is installation metadata, not rendered or automation evidence.

The fresh **Fresh Independent Audit** receives the exact candidate and acceptance package, without material implementation participation or inherited implementation reasoning. It reruns the canonical gate and verifies:

- Fresh, expired, failed-recheck and removed-listing observation states.
- Unreviewed/disputed candidates, replay/quarantine/conflict rows.
- Empty, missing, corrupt, unsupported and swapped-slot states.
- Hostile text as inert rendered content.
- Keyboard operation and desktop/narrow layouts.

Browser authority is limited to a clean isolated context and the actual `http://127.0.0.1:<port>` origin. Block requests outside that origin; use synthetic fixtures only. Do not inspect personal profiles, unrelated tabs, accounts or storage. Record the Playwright and Chromium versions, candidate SHA, origin, query, evaluation instant, viewport and exercised states.

Screenshots are optional temporary acceptance artifacts in one expressly owned temporary directory. Do not commit them, retain real data or infer screenshot redistribution rights. Close the context/server and clean only exact owned temporary artifacts.

Apply the AP Browser Stall Guard: preserve one identified failure episode, use at most two meaningful recovery attempts, and stop browser repair on repeated or conclusive no-progress. Report absent browser evidence explicitly; tests or HTTP checks do not turn missing rendered evidence into acceptance PASS.

### Numbered COOPERATOR rendered acceptance

Each item receives `PASS`, `FAIL` or `NOT TESTED`, optionally with commentary.

1. The page clearly identifies synthetic/local/read-only operation, the fixed evaluation instant and all four sections.
2. Fresh supported observations show checked-available wording and expiry; exact expiry removes the positive label.
3. Failed rechecks and removed listings retain dated history without implying stock exhaustion.
4. Original timestamps, offset uncertainty, edition/language distinctions, evidence coverage, provenance and every review revision are understandable.
5. Research outcomes, quarantine and disputes are legible; candidates remain unreviewed/disputed, agent-only and not eligible.
6. Empty, missing and unsupported/corrupt/swapped databases have distinct messages, with healthy independent content retained.
7. Keyboard focus, disclosures, text wrapping and narrow/desktop layouts are usable; meaning remains clear without colour.
8. Hostile text is inert; the page has no remote links/assets or write/import/review actions.
9. Invalid operator arguments produce clear usage feedback before a server starts.

The ORCHESTRATOR classifies feedback as accepted behavior, concrete defect, missing evidence, product decision or adjacent scope. Subjective sign-off remains COOPERATOR-owned.

### Publication and rollback

Publication requires independent **acceptance-PASS**, COOPERATOR rendered sign-off and a separate exact-SHA publication grant. Recheck that public `main` still equals the accepted parent and that the candidate is clean and unchanged. Use one normal, non-force, single-ref push, with tag following disabled:

```text
git push --no-follow-tags origin HEAD:refs/heads/main
```

Then directly verify public ref equality, commit/parent/tree/changed paths, and observe a separate `verify` push run on `main` for that exact SHA through completion. Do not infer CI success from workflow existence. Remote drift stops publication for RF-12 reconciliation.

No extra refs, tags, rebase, amend, force push, deployment, release or Meta Git operation is proposed.

Rollback first stops the UI process; databases require no rollback because the UI never writes them. Preserve rejected/unpublished candidates and owner work. Code rollback uses a separately authorized normal revert of the exact UI commit, followed by the canonical gate. Do not reset, clean, stash or rewrite history.

### Material decision record

| Decision | Proposed route | Disposition |
|---|---|---|
| UI surface/architecture | One server-rendered loopback HTML/CSS page; no JavaScript/JSON endpoint | COOPERATOR approval required |
| Placement | New unpublished `bookradar-ui` workspace crate | COOPERATOR approval required |
| Dependencies | Two existing path dependencies; zero new external dependencies | COOPERATOR approval required |
| Minimal slice/query | Both stores and all four sections; CLI-configured query; immutable startup snapshot | COOPERATOR approval required |
| Language/wording | English; exact existing truth meanings with presentation-only typography | COOPERATOR approval required |
| Visual design | Small neutral semantic layout, system fonts, native disclosures, explicit text states | COOPERATOR approval required |
| Local security | Exact loopback binding, bounded read-only HTTP subset, escaping and strict headers above | COOPERATOR approval required |
| Browser capability route | Separate provisioned fresh Playwright/Chromium Worker; no installation here | **Selected by COOPERATOR** |
| Browser/screenshot scope | Isolated exact-origin acceptance; optional temporary synthetic captures; none committed | COOPERATOR approval required |
| ADR 0007 | Add the selected UI architecture record after approval | COOPERATOR approval required |
| Evidence/independence | E2 with mandatory separate fresh acceptance and COOPERATOR rendered review | COOPERATOR approval required |
| Commit/publication | One local commit, canonical clean-candidate gate, separate acceptance-gated publication grant | COOPERATOR approval required |

Residual limits are explicit: the custom HTTP subset is for this local synthetic shell; displayed assessments are tied to the supplied instant; browser evidence covers only the recorded engine/environment; no live monitor, data ingestion, account system or production readiness is established.

```text
Orchestration critique:
MEASURED: none
LEAD: none

Resolved Execution Issues / Near-Misses: initial sandbox GitHub DNS/API reads failed; permitted read-only network execution subsequently verified the public refs and CI run. No repository fetch or environment repair occurred; no residual evidence gap.
Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the planning grant; no autonomous continuation.
```
