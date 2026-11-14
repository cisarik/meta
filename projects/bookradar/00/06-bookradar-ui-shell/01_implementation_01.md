# BookRadar — Implementation — Minimal Local Read-Only UI Shell

Persistent role identity: WORKER
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 01
Worker exchange ordinal: 02
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BOOKRADAR-UI-SHELL-IMPLEMENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — the plan is decision-complete; implementation is bounded to one additive read-only store formatter, the dependency-free stdlib `bookradar-ui` crate, 17 focused deterministic tests, README and ADR 0007 updates, and one local commit.
Recommended context capacity: approximately 250k tokens
Exact baseline: a2182302de73cb345b4b646993a1ad25d602555f
Changed-path allowlist: Cargo.toml, Cargo.lock, README.md, crates/bookradar-store/src/history.rs, crates/bookradar-store/src/lib.rs, crates/bookradar-ui/Cargo.toml, crates/bookradar-ui/src/lib.rs, crates/bookradar-ui/src/main.rs, crates/bookradar-ui/src/config.rs, crates/bookradar-ui/src/snapshot.rs, crates/bookradar-ui/src/render.rs, crates/bookradar-ui/src/http.rs, crates/bookradar-ui/src/style.css, crates/bookradar-ui/tests/common/mod.rs, crates/bookradar-ui/tests/render.rs, crates/bookradar-ui/tests/http.rs, crates/bookradar-ui/tests/cli.rs, docs/adr/0007-local-read-only-ui-shell.md
Implementation boundaries: positive and negative authority below
Independence required: no

Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `00c46a0fb52a1657b218439e6b5d2a2dce8c029d2799bb234ed3f85f7aa46ffd`) for task `BOOKRADAR-UI-SHELL-PLAN`, produced in this exact Worker session.
Authority renewal: prior planning authority expired at that terminal report; this exchange grants a new complete bounded implementation grant.
Evidence posture: non-independent. Required fresh independent acceptance (`Fresh Independent Audit` with Playwright/Chromium) is a separate later Worker session and is not performed or self-certified here.
Current-session reuse: the accepted plan is repository-grounded, the session is healthy, assumptions are unchanged, independence is not required for implementation, and retained context reduces implementation error. Retained context is convenience rather than authority; re-gate repository and environment state before mutation and stop on any conflict with current repository evidence.

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
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exact 18 allowlist paths below; ignored build and temporary demo outputs under `target/` and `tests/target/` (any temporary demo directory under `target/` must be cleaned or remain inside ignored `target/`)
Host/remote mutation: none
Trace persistence: none

## Authority and delivery posture

This prompt is your only current task authority. The accepted plan is
`01_report_00.md` (SHA-256 `00c46a0fb52a1657b218439e6b5d2a2dce8c029d2799bb234ed3f85f7aa46ffd`);
this grant binds that plan and records the COOPERATOR's approval of the plan
and all 12 rows of the material decision table on 2026-11-13. If this grant and
the plan differ, this grant controls; stop if a difference is material and
unresolved.

Native Plan Mode must be OFF (`Native planning mode: not-used`) for this
exchange. This prompt must be delivered to the exact current Worker session `01`
that produced `01_report_00.md`, not a different session. If that session is
unavailable, do not execute this prompt in a different session; return for a
fresh-session `02/01` implementation grant instead.

Return the complete terminal implementation report in this session. The
COOPERATOR will persist it at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_01.md`.
The relay basis is the COOPERATOR-selected manual delivery; `Trace persistence:
none` is intentional and grants no Meta write. You may read
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_implementation_01.md`
to verify identity and echo its SHA-256 in your report; do not modify any file
under `/Users/agile/meta`.

## Approved decisions bound in this grant

The COOPERATOR approved all 12 material decisions from `01_report_00.md`:

1. **UI surface & architecture:** One English-language, server-rendered loopback
   HTML/CSS page (`/` and `/style.css`); no JavaScript and no JSON endpoint.
2. **Placement:** New unpublished workspace crate `crates/bookradar-ui`
   (`version = "0.1.0"`, `edition = "2024"`, `rust-version = "1.99.1"`,
   `publish = false`, `#![forbid(unsafe_code)]`).
3. **Dependencies:** Only workspace path dependencies `bookradar-core` and
   `bookradar-store`; zero new external crates (`Cargo.lock` gains only the
   local `bookradar-ui` package entry; `bookradar-core` dependency tree remains
   1 line).
4. **Minimal slice & snapshot model:** Both stores and all four sections
   (**Current assessment**, **Observation history**, **Research ledger**,
   **Research current candidates**) on one page; CLI-configured query and
   required `--now`; immutable startup snapshot opened via literal
   `OpenMode::ReadOnly`, with database connections closed before serving.
5. **Read-model helper:** Expose `pub fn render_current_labels(view: &CurrentView, target: EditionId, now: SystemTime) -> Vec<String>`
   in `crates/bookradar-store/src/history.rs` and re-export it from
   `crates/bookradar-store/src/lib.rs`, sharing `human_lines` with
   `render_current` so CLI output bytes and selection predicates remain
   unchanged. (You may also re-export `InputView` and `FindingView` in
   `crates/bookradar-store/src/lib.rs` if convenient for typed snapshot
   conversion, without changing their semantics.)
6. **Language & wording:** English UI; exact existing truth meanings from
   `render_current_labels` with presentation-only typography substitutions
   (` -- ` -> ` — `, `unix:` -> `Unix `, `; expires_unix=` -> `; expires at Unix `),
   plus the explicit disclaimer:
   `"Verification describes an evidenced source observation, not a guarantee that a purchase will succeed."`
7. **Visual & accessibility design:** Single-column neutral layout (`72rem`
   max), system fonts, native `<details>` disclosures, skip link, logical
   headings, visible keyboard focus, labelled tables, no green availability
   badges, colour never the sole carrier of meaning.
8. **Local HTTP security controls:** Literal IPv4 `127.0.0.1` only (default
   `127.0.0.1:0`, printing and flushing `listening=http://127.0.0.1:<actual-port>`);
   `GET` and `HEAD` only on `/` and `/style.css` (`include_str!`); origin-form
   HTTP/1.1 only; 8 KiB / 64 header cap; 2s header-read deadline and 2s write
   timeout; one request per connection (`Connection: close`); `Host` required
   to match `127.0.0.1:<actual-port>`; foreign `Origin` or cross-site
   `Sec-Fetch-Site` rejected (`403`); strict security headers (`Content-Security-Policy`,
   `X-Content-Type-Options: nosniff`, `Cache-Control: no-store`,
   `Referrer-Policy: no-referrer`, `Cross-Origin-Resource-Policy: same-origin`);
   full HTML-escaping (`&`, `<`, `>`, `"`, `'`) on all displayed strings.
9. **Tests & verification gate:** Preserve all 77 existing tests and add the 17
   focused tests in `crates/bookradar-ui/tests/{render,http,cli}.rs` (94 total);
   keep `scripts/verify.sh` and `.github/workflows/verify.yml` unchanged.
10. **Documentation & ADR:** Update `README.md` with the workspace/binary
    summary, reproducible synthetic UI demo, and boundaries; add
    `docs/adr/0007-local-read-only-ui-shell.md` (`Status: Accepted 2026-11-13`,
    `Date: 2026-11-13`, `Decision owner: COOPERATOR`). Leave
    `docs/domain-contract.md`, `docs/research-input-v1.md`, and
    `docs/adr/0001`–`0006` untouched.
11. **Evidence tier & acceptance route:** `E2` with separate fresh independent
    acceptance (`Fresh Independent Audit` in a separate fresh Worker session)
    and COOPERATOR rendered acceptance.
12. **Git & publication boundary:** Exact 18-path allowlist; one local commit
    with subject `feat: add a local read-only UI shell`; `bash scripts/verify.sh`
    run on the clean committed candidate; no push in this grant.

## Repository and baseline gate

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Expected subject: `fix: restore target ignore and run the gates in CI`
Expected worktree: clean (`git status --porcelain` empty; `target/` ignored by `/target/`)
Governing AP: `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1
Accepted ADRs: `docs/adr/0001`–`0006`

Before any edit, independently re-verify the physical root, remote, branch,
HEAD, parent, tree, clean worktree, `.ap` pin and cleanliness, strict
`./.ap/ap doctor` PASS, and Rust `1.99.1` / C compiler availability. If the
baseline differs or the worktree is dirty, stop and report under RF-12; do not
reset, clean, stash, or switch branches.

Execution route (RF-16): no `ap.project.conf` is declared in this repository.
The canonical project verification gate is `bash scripts/verify.sh` (per
`README.md` and `docs/adr/0006-verification-gate-and-ci.md`), and the protocol
integration check is `./.ap/ap doctor`. Because `bash scripts/verify.sh`
refuses a dirty worktree at startup, during Stage 3–4 development before the
local commit you are explicitly authorized to run focused `cargo +1.99.1`
commands (`cargo +1.99.1 test`, `cargo +1.99.1 build`, `cargo +1.99.1 fmt`,
`cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D warnings`,
`cargo +1.99.1 tree --locked --offline -p bookradar-core`) with
`$HOME/.cargo/bin` prepended in-process if needed. After creating the single
local commit in Stage 5, you **must** execute the canonical gate
`bash scripts/verify.sh` on the clean committed candidate and require exit `0`.

## Mandatory reading

Read or re-verify as needed:
- `.ap/AP.md` (WORKER spine, RF-03, RF-06, RF-12, RF-16, RF-18, RF-19,
  Implementation Authority, §8, §12, §18), `.ap/AP_WORKER.md`, and
  `.ap/PROMPT_CONTRACTS.md` (Worker Report Header, Implementation Authority
  Record, Validation Ladder Record).
- `AGENTS.md`, `README.md`, `Cargo.toml`, `Cargo.lock`, `scripts/verify.sh`,
  `docs/domain-contract.md`, `docs/research-input-v1.md`, `docs/adr/0004-local-persistence-and-history.md`,
  `docs/adr/0005-versioned-research-admission.md`, `docs/adr/0006-verification-gate-and-ci.md`.
- `crates/bookradar-store/src/lib.rs`, `crates/bookradar-store/src/history.rs`,
  `crates/bookradar-store/src/store.rs`, `crates/bookradar-store/src/research.rs`,
  `crates/bookradar-store/src/fixtures.rs`.
- Your accepted plan `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_00.md`.

## Exact changed-path allowlist (18 paths)

Only these 18 repository-relative paths may be modified or created:

1. `Cargo.toml`
2. `Cargo.lock`
3. `README.md`
4. `crates/bookradar-store/src/history.rs`
5. `crates/bookradar-store/src/lib.rs`
6. `crates/bookradar-ui/Cargo.toml`
7. `crates/bookradar-ui/src/lib.rs`
8. `crates/bookradar-ui/src/main.rs`
9. `crates/bookradar-ui/src/config.rs`
10. `crates/bookradar-ui/src/snapshot.rs`
11. `crates/bookradar-ui/src/render.rs`
12. `crates/bookradar-ui/src/http.rs`
13. `crates/bookradar-ui/src/style.css`
14. `crates/bookradar-ui/tests/common/mod.rs`
15. `crates/bookradar-ui/tests/render.rs`
16. `crates/bookradar-ui/tests/http.rs`
17. `crates/bookradar-ui/tests/cli.rs`
18. `docs/adr/0007-local-read-only-ui-shell.md`

No other tracked or untracked repository file may remain at completion.

## Ordered implementation stages and gates

1. **Stage 1 — Baseline re-gate:** Verify repo root, remote, `main` / `HEAD` /
   `origin/main` at `a2182302de73cb345b4b646993a1ad25d602555f`, parent
   `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`, tree
   `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`, clean worktree, `.ap` detached
   and clean at `d7023cf037f6d17885c3ede5c04812c61640da50`, strict
   `./.ap/ap doctor` PASS, and Rust `1.99.1`.
2. **Stage 2 — Store label helper & workspace manifest:**
   - In `crates/bookradar-store/src/history.rs`, expose
     `pub fn render_current_labels(view: &CurrentView, target: EditionId, now: SystemTime) -> Vec<String>`
     returning `Vec::new()` when `view.is_empty()` and `human_lines(view, target, now)`
     otherwise, and route `render_current` through it so existing CLI outputs
     and predicates are unchanged.
   - Re-export `render_current_labels` in `crates/bookradar-store/src/lib.rs`
     (plus `FindingView, InputView` if desired).
   - Add `"crates/bookradar-ui"` to `members` and `default-members` in root
     `Cargo.toml` and create `crates/bookradar-ui/Cargo.toml` depending only on
     `bookradar-core = { path = "../.." }` and
     `bookradar-store = { path = "../bookradar-store" }`. Verify `Cargo.lock`
     changes only by adding the local `bookradar-ui` package entry.
3. **Stage 3 — Implement `bookradar-ui` modules (`config`, `snapshot`, `render`, `http`, `style.css`, `lib`, `main`):**
   - Implement exact CLI parsing and validation before any file or socket I/O
     as specified in Section 2 & Section 3 of `01_report_00.md`.
   - Implement independent `OpenMode::ReadOnly` startup snapshot loading (closing
     both connections before serving), preserving exact error categories/reasons
     (`not-found`, `unsupported-schema: corrupt-database`,
     `unsupported-schema: application-id`, `unsupported-schema: user-version`,
     etc.) and healthy-slot independence.
   - Implement pure deterministic HTML rendering with full HTML escaping, the
     four anchored sections, all 13 current truth label families, the
     non-guarantee notice, full timestamp/offset/instant/nanosecond/pre-epoch
     details, review revisions, research counts/receipts/findings, research
     candidate cards (`Research candidate — unreviewed` / `Research candidate — disputed`,
     `Unverified`, `agent-only`, `not-eligible`, and fail-closed suppression on
     unexpected research states), and embedded accessible CSS (`include_str!("style.css")`).
   - Implement the restricted loopback HTTP/1.1 server (`127.0.0.1` literal
     only, `GET`/`HEAD` on `/` and `/style.css`, origin-form only, 8 KiB / 64
     headers max, 2s read deadline / 2s write timeout, `Connection: close`,
     exact `Host: 127.0.0.1:<port>` check, `Origin` / `Sec-Fetch-Site` check,
     and strict security headers).
4. **Stage 4 — Implement the 17 focused UI tests, `README.md`, and `docs/adr/0007-local-read-only-ui-shell.md`:**
   - Implement `crates/bookradar-ui/tests/common/mod.rs` (guarded `TempDir`,
     child-process kill/wait guard, fixture helpers) and the 17 exact tests in
     `tests/render.rs` (8 tests), `tests/http.rs` (6 tests), and `tests/cli.rs`
     (3 tests).
   - Update `README.md` and create `docs/adr/0007-local-read-only-ui-shell.md`
     as specified in Section 4 of `01_report_00.md`.
   - Run focused `cargo +1.99.1 fmt --all --check`, `cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D warnings`,
     and `cargo +1.99.1 test --workspace --locked --offline` to confirm all 94
     tests pass (77 existing + 17 new).
5. **Stage 5 — Review, stage exact allowlist, and create one local commit:**
   - Verify `git status --porcelain` shows only the 18 allowlist paths.
   - Stage only the 18 allowlist paths (never `git add .` or `git add -A`),
     inspect `git diff --cached --check` and `git diff --cached --stat`, and
     create one local commit with exact subject:
     `feat: add a local read-only UI shell`
   - Do not amend, rebase, tag, or push.
6. **Stage 6 — Canonical post-commit verification gate and local synthetic demo:**
   - Run `bash scripts/verify.sh` on the clean committed candidate; require exit
     `0`, all 94 tests passing, 1-line `bookradar-core` tree, `git diff --check`,
     strict `./.ap/ap doctor` PASS, and empty `git status --porcelain`.
   - Run the bounded synthetic demonstration against `127.0.0.1:0` (creating the
     demo stores inside ignored `target/`, starting `bookradar-ui`, reading back
     `/` and `/style.css` over loopback, stopping the child process cleanly, and
     removing the temporary demo directory under `target/`). Confirm
     `git status --porcelain` remains empty.

## Validation ladder and implementation envelope

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: preserve all 77 accepted tests across bookradar-core and bookradar-store
Affected tests: crates/bookradar-store/tests/cli.rs, crates/bookradar-store/tests/research_cli.rs, and the 17 new tests in crates/bookradar-ui/tests/{render,http,cli}.rs
New causal regression: 17 focused UI tests covering all 13 truth labels, timestamp/review/uncertainty rendering, HTML escaping of hostile observation and research text, research outcomes without candidate promotion, empty/missing/corrupt/swapped/unsupported-schema states, byte-identical deterministic rendering, loopback GET/HEAD, method/target/framing/Host/Origin/CSP enforcement, read-only database preservation, and CLI/bind validation
Broad or full suite: required-because ADR 0006 binds bash scripts/verify.sh as the canonical repository gate
Runtime or testbed: local loopback synthetic demonstration on 127.0.0.1:0
Independent acceptance: required-separate-fresh-worker
```

```text
Evidence tier: E2
Evidence tier basis: reversible cross-cutting addition of a user-visible local read-only UI crate, shared store label helper, and loopback HTTP surface using synthetic fixtures only; no external network, credentials, durable schema migration, or production deployment
Authorized implementation stages: baseline gate; store helper and workspace manifest; bookradar-ui implementation; 17 focused tests + README + ADR 0007; one local commit; post-commit bash scripts/verify.sh + synthetic loopback demonstration; terminal report
Combined implementation envelope: allowed
Implementation stage gates: each stage must pass before proceeding; no product-semantics change; no external dependencies; no push
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: baseline a2182302de73cb345b4b646993a1ad25d602555f; before commit stop and report; after commit do not reset, amend, or force
Activated stricter profile: none
Terminal implementation report point: after the one local commit, bash scripts/verify.sh PASS, and clean synthetic loopback demonstration
```

## Authority boundaries

- **Positive authority:** Read/write only the 18 allowlist paths; create
  `crates/bookradar-ui/` and `crates/bookradar-ui/src/`, `crates/bookradar-ui/tests/`,
  `crates/bookradar-ui/tests/common/` for those exact files; create ignored
  build/demo outputs under `target/` (cleaning temporary demo directories before
  completion); run `cargo +1.99.1` build/test/fmt/clippy/tree/fetch (`--locked`),
  `bash scripts/verify.sh`, bounded loopback HTTP checks on `127.0.0.1`,
  read-only `git` inspection, explicit staging of the 18 allowlist paths, and
  one local `git commit` with subject `feat: add a local read-only UI shell`.
- **Negative authority:** All other file writes, paths outside the 18-path
  allowlist, external crate dependencies, `bookradar-core` edits, schema or
  research wire-contract edits, `docs/domain-contract.md` or `docs/adr/0001`–`0006`
  edits, `scripts/verify.sh` or `.github/workflows/verify.yml` edits, browser
  downloads/installations, external network requests (beyond `cargo fetch --locked`
  inside `scripts/verify.sh`, which is a no-op since no registry crate is added),
  non-loopback binds (`0.0.0.0`), `git add .` / `git add -A`, `git push`,
  `git reset`, `git clean`, `git stash`, `git commit --amend`, rebasing, tags,
  secrets, Meta writes, self-certified acceptance, publication, and closure are
  strictly prohibited.

## Report contract

Return the complete terminal report in this session; the COOPERATOR will save
it at `/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_01.md`.
Begin the report with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinates once at the top of the report metadata:

```text
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 01
Worker exchange ordinal: 02
```

Include the compact core:
- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: implementation-PASS` (or `not-applicable` if not PASS)
- `Start commit: a2182302de73cb345b4b646993a1ad25d602555f`
- `End commit: <new-local-commit-sha>`
- `Changed files: <exact 18 paths and purpose>`
- `Tests and validation: <94 tests breakdown, bash scripts/verify.sh result, core-tree check, ap doctor, and synthetic loopback demo summary>`
- `Git result: one local commit on main (<sha>, parent a2182302de73cb345b4b646993a1ad25d602555f, tree <tree-sha>); no push`
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: Fresh Independent Audit (02/01) on candidate <sha>`
- `Report justification: new-mutation`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the implementation grant; no autonomous continuation.`
- Echo the SHA-256 of `01_implementation_01.md` and include:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>
Pre-Existing Failure Classification: none | <complete classification per the contract>
```

## Stopping conditions

Stop and report without improvisation if:
- the baseline commit, parent, tree, branch, cleanliness, `.ap` pin, or
  `ap doctor` state differs from the declared state;
- this prompt is not running in the exact Worker session `01` that produced
  `01_report_00.md`, or Native Plan Mode is still enabled;
- any required change would touch a path outside the 18-path allowlist, add an
  external crate dependency, or alter accepted domain/store semantics or CLI
  transcripts;
- `bash scripts/verify.sh` fails on the committed candidate;
- a Git operation fails or recovery would require reset, amend, clean, stash, or
  force.
