# BookRadar — Closure: `bookradar-ui-shell`

**Artifact:** `projects/bookradar/00/06-bookradar-ui-shell/01_closure.md`
**Kind:** closing continuity and handoff artifact for a completed logical whole. Not a Worker prompt, task authority, implementation plan, acceptance report, publication report, or grant.
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-13.
**Target:** the upstream Master ChatOrchestrator and the next logical-whole selection.
**Capability profile: Orchestrator**
**Orchestrator session scope: logical-whole**
**Closure status:** `closed-by-ORCHESTRATOR`
**Restoration classification:** PASS for selecting and preparing the next logical whole, conditional on the successor revalidating mutable facts. This grants no mutation authority.
**Filename basis:** Meta handoff/closure sequence; next prefix after the opening `00` position, independent of Worker exchange suffixes.

## 1. Closure record

```text
Phase-qualified result: publication-PASS
Result artifact or commit: 2281982f7dae0ef1f582d294592c41281ba11b21
Result evidence: exact public ref and symbolic HEAD equality; public commit parent/tree/subject; CI run 43485796198 success; implementation-PASS and acceptance-PASS (with isolated Playwright 1.65.0 / Chrome 157.0.8103.39 rendered browser verification); 94 tests; strict ap doctor PASS; clean worktree
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
Public commit: `2281982f7dae0ef1f582d294592c41281ba11b21`
Public commit URL: <https://github.com/cisarik/bookradar/commit/2281982f7dae0ef1f582d294592c41281ba11b21>
Commit subject: `feat: add a local read-only UI shell`
Parent: `a2182302de73cb345b4b646993a1ad25d602555f`
Tree: `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`
Commit date: `2026-11-13T18:35:51+01:00` (`2026-11-13T17:35:51Z`)

The commit changes exactly eighteen paths, adding 3,354 lines and removing 15:

| Path | Purpose |
|---|---|
| `Cargo.toml` | Adds `crates/bookradar-ui` to workspace `members` and `default-members` |
| `Cargo.lock` | Records local package `bookradar-ui 0.1.0` with path dependencies `bookradar-core` and `bookradar-store` |
| `README.md` | Documents `bookradar-ui`, CLI flags, reproducible synthetic UI demo, and read-only/loopback limits |
| `crates/bookradar-store/src/history.rs` | Exposes `render_current_labels` sharing `human_lines` with `render_current` |
| `crates/bookradar-store/src/lib.rs` | Re-exports `render_current_labels`, `InputView`, and `FindingView` |
| `crates/bookradar-ui/Cargo.toml` | Unpublished `bookradar-ui` crate manifest with path dependencies only |
| `crates/bookradar-ui/src/lib.rs` | Library entrypoint (`#![forbid(unsafe_code)]`) |
| `crates/bookradar-ui/src/main.rs` | `bookradar-ui` CLI binary entrypoint (`#![forbid(unsafe_code)]`) |
| `crates/bookradar-ui/src/config.rs` | Strict CLI flag, timestamp, identifier, edition, and `127.0.0.1:<port>` bind validation before I/O |
| `crates/bookradar-ui/src/snapshot.rs` | Independent `OpenMode::ReadOnly` startup snapshot loader for observation store and research ledger |
| `crates/bookradar-ui/src/render.rs` | Pure deterministic HTML renderer with full HTML escaping, 4 sections, 13 truth labels, and research candidate guards |
| `crates/bookradar-ui/src/http.rs` | Restricted loopback HTTP/1.1 server (`GET`/`HEAD` on `/` and `/style.css`, 8 KiB/64-header cap, 2s timeouts, `Host`/`Origin`/`Sec-Fetch-Site`, strict CSP) |
| `crates/bookradar-ui/src/style.css` | Embedded neutral single-column stylesheet (`72rem` max, skip link, visible focus, no green availability badges) |
| `crates/bookradar-ui/tests/common/mod.rs` | Guarded `TempDir`, child-process kill/wait guard, and synthetic fixture helpers |
| `crates/bookradar-ui/tests/render.rs` | 8 deterministic HTML rendering, truth-label, timestamp/review, escaping, research-outcome, and error-state tests |
| `crates/bookradar-ui/tests/http.rs` | 6 loopback HTTP, `HEAD`, method/target rejection, `Host`/`Origin`/CSP, framing/timeout, and read-only file preservation tests |
| `crates/bookradar-ui/tests/cli.rs` | 3 CLI validation, non-loopback bind rejection, and bind-failure exit tests |
| `docs/adr/0007-local-read-only-ui-shell.md` | Accepted architecture decision record for the local read-only UI shell |

`bookradar-core` sources, `bookradar-store` storage/research logic and schemas,
the 77 existing tests, `docs/domain-contract.md`, `docs/research-input-v1.md`,
`docs/adr/0001`–`0006`, `scripts/verify.sh`, `.github/workflows/verify.yml`,
`rust-toolchain.toml`, `.gitignore`, and the `.ap` gitlink are unchanged.

Direct public readback:

```text
ref: refs/heads/main	HEAD
2281982f7dae0ef1f582d294592c41281ba11b21	HEAD
2281982f7dae0ef1f582d294592c41281ba11b21	refs/heads/main
```

Local `main` equals `origin/main` and `HEAD`; the branch is `+0 -0`; the
worktree is clean apart from ignored `target/`. The push was one normal
non-force fast-forward `a218230..2281982 HEAD -> main`. Public commit metadata
shows the expected parent, tree, and subject.

CI evidence, independently observed by the Orchestrator:

```text
Workflow: verify
Run: 43485796198
URL: https://github.com/cisarik/bookradar/actions/runs/43485796198
Event: push
Head SHA: 2281982f7dae0ef1f582d294592c41281ba11b21
Status: completed
Conclusion: success
Created: 2026-11-13T18:46:01Z
Updated: 2026-11-13T18:46:39Z
```

AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`; `.ap` remains detached and
clean. Strict `./.ap/ap doctor` PASS. The domain contract remains revision 1.
ADR 0007 is accepted; ADRs 0001–0006 are unchanged.

## 3. Scope completed

- Added `crates/bookradar-ui` (`0.1.0`, `edition = "2024"`, `rust-version = "1.99.1"`,
  `publish = false`, `#![forbid(unsafe_code)]`) with path dependencies on
  `bookradar-core` and `bookradar-store` only, adding zero external registry
  crates.
- Exposed `pub fn render_current_labels(view: &CurrentView, target: EditionId, now: SystemTime) -> Vec<String>`
  in `bookradar-store` and routed `render_current` through it so the UI and CLI
  share the exact truth-label selection predicates without CLI drift.
- Implemented `bookradar-ui` startup snapshot loading using `OpenMode::ReadOnly`
  and a caller-supplied `--now <unix-seconds>` instant, closing both SQLite
  connections before serving an immutable HTML snapshot (`/`) and embedded
  stylesheet (`/style.css`).
- Rendered all four sections (**Current assessment**, **Observation history**,
  **Research ledger**, **Research current candidates**), all 13 accepted current
  truth label families, the explicit non-guarantee notice, full timestamp
  assertions (original text, offset state, Unix instant, signed seconds,
  nanoseconds including pre-epoch, and ingestion time), review revisions,
  research counts/receipts/findings, research candidates strictly as
  `Research candidate — unreviewed` / `disputed` (`Unverified`, `agent-only`,
  `not-eligible`, with fail-closed suppression on unexpected states), and
  distinct empty, missing (`not-found`), and corrupt/swapped/unsupported-schema
  (`unsupported-schema: ...`) states.
- Implemented strict loopback security controls: literal `127.0.0.1` IPv4 bind
  only, `GET`/`HEAD` on `/` and `/style.css` only, origin-form HTTP/1.1 only,
  8 KiB / 64 header cap, 2-second read/write deadlines, one request per
  connection (`Connection: close`), `Host`/`Origin`/`Sec-Fetch-Site` validation,
  strict `Content-Security-Policy` and security headers, and full HTML escaping
  of all displayed strings.
- Added 17 focused UI tests (`8` in `tests/render.rs`, `6` in `tests/http.rs`,
  `3` in `tests/cli.rs`), bringing the workspace test suite from 77 to **94
  passing tests** under `bash scripts/verify.sh`.
- Updated `README.md` with the reproducible synthetic UI demo and accepted
  `docs/adr/0007-local-read-only-ui-shell.md`.
- Verified the candidate via a fresh independent audit (`03_report_00.md`)
  including live isolated Playwright `1.65.0` / headless Google Chrome
  `157.0.8103.39` browser rendering across 6 loopback scenarios, obtained
  COOPERATOR acceptance sign-off, published to `origin/main`, and observed a
  successful public CI run (`43485796198`).

## 4. Evidence

- **94 tests pass** in `bash scripts/verify.sh` and in public CI run
  `43485796198`: 17 core, 10 store unit, 4 observation CLI, 13 history, 6
  persistence, 2 research CLI, 5 research contract, 20 research ingestion, 3 UI
  CLI, 6 UI HTTP, and 8 UI render (`0` doc/bin unit tests).
- Planning prompt `01_planning_00.md` SHA-256
  `f38aa7decb5b26efa06b6e463ae560b8944f96a91aea13749dd47714438d40e4`;
  planning report `01_report_00.md` SHA-256
  `00c46a0fb52a1657b218439e6b5d2a2dce8c029d2799bb234ed3f85f7aa46ffd`.
- Implementation prompt `01_implementation_01.md` SHA-256
  `a0ee71de454f000796030092f01c64e132f76ce363cb8ea3db3611e2968e5fdb` (which
  produced candidate `2281982f7dae0ef1f582d294592c41281ba11b21`, directly
  verified by the Orchestrator as `implementation-PASS`). Consumed pre-mutation
  `BLOCKED` reports in the trace: `01_report_01.md` SHA-256
  `a680fa633ae9b071af0aab5096dcaee877d669b5c143b1b92b6469a79b72b714` and
  `02_report_00.md` SHA-256
  `0db26b4caecd225973092a44e41e4f69ba4afbc9f965d2b4c645be532eb48046` (for
  `02_implementation_00.md` SHA-256
  `0599376692af4cd94949b3b2ae239c5cf7d2855f6c71d93a19c1c527c3a5962a`).
- Independent acceptance prompt `03_acceptance_00.md` SHA-256
  `a83c2318e48b740a1af59fd532738b5897ddd6efe99c658bade84e9623fc5f54`;
  independent acceptance report `03_report_00.md` SHA-256
  `525afe9783b7c2656b0aeb2ec2f60b31d6a5e25b7d6417db892027b659b5c563`
  (`acceptance-PASS` for `2281982f7dae0ef1f582d294592c41281ba11b21`; all C1–C14
  controls and Playwright/Chromium browser verification passed).
- Publication prompt `04_publication_00.md` SHA-256
  `8c71ebf1958f5f30d21b02b9629e4b3474c25ca78bd530ff266fbb1f688a730b`;
  publication report `04_report_00.md` SHA-256
  `e8eaf475aceeba28886f74fb04c2b4db7335ceb2b3253450c1553717df1b2a89`
  (`publication-PASS` for `2281982f7dae0ef1f582d294592c41281ba11b21`).
- Public CI run `43485796198`, workflow `verify`, conclusion `success`, head SHA
  `2281982f7dae0ef1f582d294592c41281ba11b21`, observed directly after
  publication.

## 5. Non-achievements and deferrals

- No live Hermes/Playwright research adapter, scraping, external API, MCP, real
  retail data, screenshots committed to the repository, personal data,
  watchlists/library, accounts, authentication, NUC, SSH, sudo, services,
  deployment, release, or production hosting.
- No database write, creation, migration, import, review, promotion, or repair
  from the UI; `bookradar-ui` is a fixed local read-only snapshot, not a running
  monitor.
- No change to product semantics, `bookradar-core` behavior, schema v1, the
  research ledger or wire contract, `docs/domain-contract.md`, or ADRs 0001–0006.
- No new external crate dependency, toolchain change, or AP update.
- No license, contribution, privacy, security-response, support, or release
  policy.

## 6. Residual risks and process/trace notes

- The custom HTTP/1.1 subset in `bookradar-ui` is intentionally restricted to
  loopback (`127.0.0.1`) and synthetic local inspection (`GET`/`HEAD` on `/` and
  `/style.css`). Any future LAN, remote, or hosted surface requires a separate
  security and architecture decision.
- Displayed assessments are evaluated at the caller-supplied `--now` instant at
  process startup and remain fixed until restart.
- Browser acceptance evidence covers Playwright `1.65.0` driving headless Google
  Chrome `157.0.8103.39` on macOS (`1280×800` and `375×812` viewports).
- Trace note: the session that committed `2281982f7dae0ef1f582d294592c41281ba11b21`
  under `01_implementation_01.md` did not have its text report saved in the
  trace because `01_report_01.md` recorded a pre-mutation `BLOCKED` stop from a
  different chat window and `02_report_00.md` recorded the pre-mutation
  `BLOCKED` stop of session `02` after `2281982f…` already existed. Both the
  Orchestrator and the fresh independent auditor (`03_report_00.md`) verified
  the committed tree directly against the accepted plan and all 94 tests.
- Meta Git remains COOPERATOR-owned; no Meta Git operation was performed.

## 7. Pins and durable owners

- Public BookRadar commit: `2281982f7dae0ef1f582d294592c41281ba11b21`.
- Public CI run: `43485796198`, `verify`, conclusion `success`, head SHA
  `2281982f7dae0ef1f582d294592c41281ba11b21`.
- AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Product contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10.
- ADRs 0001–0006 accepted and unchanged; ADR 0007 accepted 2026-11-13.
- Verification owners: `scripts/verify.sh`, `.github/workflows/verify.yml`,
  `README.md`, ADR 0006, ADR 0007.
- No active upgrade ledger.

## 8. Recommended next logical whole(s)

Recommended next whole candidates (for COOPERATOR selection):
1. A bounded **research-producer / adapter contract rehearsal or live Hermes/Playwright
   research adapter slice** (requires explicit network, untrusted-content,
   real-data, and host security boundaries).
2. A bounded **multi-offer catalog / reviewer-workflow slice** over the local
   store and research ledger (such as explicit attributed review/reconciliation
   or multi-offer listing navigation), if the COOPERATOR prefers expanding local
   domain workflows before live network ingestion.

Deployment, NUC operations, personal state/accounts, and policy selection remain
later separately authorized wholes. Neither recommendation selects or grants a
successor whole.

## 9. Artifact lifecycle and return edge

- **Class:** retained closing continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP
  and the accepted domain contract.
- **Consumer:** upstream Master ChatOrchestrator, the next per-whole
  Orchestrator, and later reviewers.
- **Discoverability:** exact Meta location, public commit URL, CI run URL, AP
  pin, contract revision, ADR 0007, and the Worker exchange reports.
- **Retention:** retain through the next selection and archive after closure;
  material correction after closure is a separately named successor artifact.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup
  decision.
- **Expected return to Master:** this truthful closure with exact public commit,
  UI run/demo and CI evidence, completed scope, explicit non-achievements,
  current contract/AP pin, residual risks, recommended next logical wholes, and
  no implied successor grant.

**Closure signal:** `closed-by-ORCHESTRATOR`

**Final invariant:** The accepted truth is now visible locally without changing
its meaning: one dependency-free standard-library loopback UI shell, 94 passing
tests, independent Playwright/Chromium browser verification, one green public CI
run, zero external dependencies added, no product-semantics change, no live
network or real data, and no deployment.
