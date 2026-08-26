### Report for ORCHESTRATOR_CHAT

# FrameNest NUC Push Workflow and Companion Testing

## Executive summary

- **Immediate NUC route:** Michal should run the existing `~/nuc_update.fish` wrapper in a genuine interactive terminal. This is the only zero-work route whose exact schema-jump continuation is already encoded and owner-verified.
- **Do not use a reconstructed direct Orchestrator sequence under standing authority yet.** ADR-0075 authorizes the owner wrapper; the repository runbook still lacks exact exit-13 target probes and recovery-lock cleanup commands.
- **Next repository task:** correct the runbook’s unsafe `/opt/framenest/current` migration example, document the exit-13 continuation, reconcile current NUC terminology, and update documentation contract tests.
- **Companion testing:** remains parked until Michal explicitly reopens it. Once reopened, the NUC, public `main`, and unpacked extension checkout must share one exact SHA.
- **Apply acceptance:** deterministic by default. Current analyzed-history clicks intentionally open hosted Details; there is no normal rendered Apply entry for an analyzed row. Requiring rendered Apply would be a separate product decision.

Current expected release transition, subject to a fresh `status` and `check`:

```text
Target public main: 070681856bc6f14e12da52717dbccefa160554af
Current NUC:        a5487149… / schema 0032
Target schema:      0033
```

## Route comparison

| Route | Executor and sudo lifecycle | Benefits | Principal risks and stop conditions | Recommendation |
|---|---|---|---|---|
| **A. Michal runs the owner wrapper interactively** | Michal prepares SSH and the remote sudo timestamp outside any Worker, verifies `sudo -n` availability, runs the wrapper in a real TTY, completes final `status`, then invalidates the timestamp with `sudo -K`. | Zero repository work; uses the already verified continuation; avoids the failed piped-input and pseudo-TTY paths; expressly covered by ADR-0075. | Stop on non-TTY execution, unexpected initial state or exit, target-tree mismatch, unknown recovery state, migration/cutover failure, or unknown privilege release. Do not repeat unchanged if one genuine-TTY attempt fails at confirmation. | **Immediate default.** |
| **B1. Repository runbook annex plus contract tests** | A fresh Worker edits documentation/tests only; no NUC access. A later authorized operator follows the reviewed sequence. | Smallest durable correction; exposes exact probes and cleanup for review; removes the dangerous `/current` migration example. | Exact cleanup must reject unexpected lock contents. Existing tests assume all service-account examples use `/current`, so test updates are required. | **Recommended next Worker task.** |
| **B2. Tracked noninteractive wrapper** | A later implementation Worker adds a repository wrapper; Michal still prepares sudo, the executor uses only `sudo -n`, and terminal `sudo -K` remains mandatory. | Repeatable agent-compatible operation with fixed phase and exit handling. | Must wrap—not extend—the four public commands. It must never migrate inside `framenest_release.py`, run `sudo -v`, accept passwords/arbitrary remote commands, weaken the public-main gate, or broadly clear recovery state. | Optional successor if frequent agent-run refresh is desired. |
| **C. Orchestrator reconstructs individual commands** | Michal prepares sudo; Orchestrator runs a predeclared fixed sequence and releases sudo at the end. | Avoids interactive stdin without waiting for repository work. | ADR-0075 grants execution of the owner wrapper, not arbitrary reconstructed commands. The current runbook omits exact target verification and lock cleanup. Direct execution therefore exceeds standing routine mechanics even though the high-level outcome is routine. | **Not authorized by standing authority alone; require an exact bounded grant after documentation.** |

### Expected state machine and evidence

The owner wrapper should produce the following sanitized evidence:

1. `status` exits 0 and reports service active, database `0032`, and backup restore-readiness `ready`. If it already reports target SHA/schema `0033`, record completion and do not redeploy.
2. `check --release <T>` exits 0, proving local HEAD, clean tracked worktrees, live public `main`, AP pin, archive hashes, exact tooling, and backup readiness.
3. `deploy --release <T> --yes` normally exits exactly 13 with `migration-required`.
   - Exit 13 occurs after `/opt/framenest/releases/<T>` is atomically published, but before checkpoint, cutover, restart, or cleanup.
   - Exit 0 means direct completion; skip the continuation and verify with `status`.
   - Every other nonzero exit stops the run.
4. Before cleanup, verify the current symlink/service remain on the old release, target markers and executables identify `T`, target-tree database status is `0032 → 0033`, and the lock contains only the known pre-schema-gate artifacts.
5. Remove only those exact artifacts and then the empty `/run/framenest-release-deploy`. Unexpected contents stop the run.
6. Migrate using `/opt/framenest/releases/<T>` as both working directory and executable tree—not `/opt/framenest/current`—with the configured EnvironmentFile. Require new-tree status `current_revision=head_revision=0033`.
7. Complete cutover through `rollback --release <T> --yes`; here `rollback` is the supported switch to an already complete target tree.
8. Final `status` must report exact target SHA/path, active service, database `0033`, and restore-readiness `ready`.
9. Only after final status, invalidate sudo. If the session disappears first, privilege release is `unknown`, not assumed.

Evidence classes are:

- source/public provenance: `check`;
- before/after runtime state: `status`;
- schema transition: exit 13 plus target-tree database status and migration result;
- cutover/readiness: rollback completion and final status;
- privilege lifecycle: noninteractive readiness and terminal invalidation, recorded separately.

A post-migration cutover failure must not trigger an improvised downgrade or catalog restore. Migration `0033` is additive, but recovery still requires explicit triage.

## Documentation triage

| Statement area | Classification | Treatment |
|---|---|---|
| README’s old `aec2f009…` / schema `0028` release | **Stale but explicitly historical.** | Retain as dated history; never replace it with a mutable “current SHA” snapshot. |
| README present-tense “personal production server” and ordinary main/release divergence | **Misleading after ADR-0075.** | Describe a development-test NUC routinely targeting exact public `main`; keep `status` as runtime evidence. |
| README claim that companion review Save may publish | **Genuinely false after ADR-0074 implementation.** | State that Apply writes metadata only and administrator Publish is the sole future publication path. |
| README claim that `public_published_uds` and all rollout successors are unshipped | **Genuinely false.** | Record that the local-only composition and workspace successors are implemented, while public bind/TLS/Funnel remain unshipped. |
| SECURITY current support status | **Substantially coherent.** | No required edit: dev/test role, historical release, and current Tailscale/Funnel boundaries are honest. |
| SERVER NUC role opening | **Current and coherent.** | Retain. |
| SERVER “owner-authoritative production release” and normal divergence language | **Misleading present tense.** | Replace with authoritative serving for the disposable test instance and exact-main refresh/readback wording; retain the dated SHA paragraph. |
| INFOSEC “today serves production over Tailscale” | **Misleading present tense.** | Change only to development-test workspace access; retain the audited-checkout SHA and findings as historical evidence. |
| Runbook title/status/current target and blanket separately-authorized wording | **Legacy framing with operational consequences.** | Distinguish standing routine refresh authority from non-routine host work; do not globally replace generic production terminology. |
| Runbook section 5 migration from `/current` | **Operationally dangerous and directly contradicted by ADR-0075.** | Document the new release tree, exact exit-13 verification/cleanup, migration, rollback-cutover, final status, and sudo lifecycle. |
| Acceptance Part B old-release honesty banner | **Actively false.** | Gate on tested public-main SHA equalling `framenest-release status`; report `BLOCKED: NUC not at tested SHA` rather than “release not deployed.” |
| Acceptance Part B/B3 “Apply from the side panel” | **Unavailable in the current rendered flow.** | Assign Apply to deterministic evidence unless Michal chooses a new rendered entry. |
| Worker execution contract | **Coherent.** | Do not weaken Worker SSH, Python, or deployment-authority boundaries. |
| `docs/X_COMPANION.md` “fade by position” | **Misleading but belongs to the parked companion backlog.** | Correct only after Michal accepts the outline chrome; do not fold it into ADR-0075 editorial work. |

### Bounded editorial task

Update only the active role/status sections of `README.md`, `SERVER.md`, `docs/INFOSEC.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `deploy/ubuntu/README.md`, and `docs/UBUNTU_NUC_DEPLOYMENT.md`. Adapt `tests/contract/test_nuc_release_docs.py` and `tests/contract/test_nuc_operator_runbook.py` to distinguish active-tree commands from the target-release migration continuation.

Keep these interfaces unchanged:

- `framenest-release` retains exactly `status`, `check`, `deploy`, and `rollback`;
- `framenest_release.py` remains migration-free;
- no fifth helper command;
- no changes to accepted ADR bodies, `SECURITY.md`, or `docs/WORKER_EXECUTION_CONTRACT.md`;
- no global replacement of “production,” `/opt/framenest/current`, or historical SHAs.

Validation is a focused diff/link review plus the two documentation contract suites through the exact-baseline AP route.

## Companion Brave testing procedure

1. **Require explicit unpark authority and pin target `T`.**
   - Record the full current public-main SHA containing `37da5f2`.
   - Require canonical checkout HEAD `T`, clean tracked state, and matching AP pin.
   - Do not trust the local `origin/main` tracking ref alone; current inspection found it stale at `06af60a…`. The release helper’s live `check --release T` is authoritative.

2. **Prove the NUC serves `T`.**
   - Require post-refresh `active_release=T`, release path ending in `T`, service active, schema `0033`, and backup readiness `ready`.
   - Reduce one HTTPS audience-bootstrap response to booleans proving `tailscale_workspace`, mapped administrator identity, and required workflow capabilities.
   - Stop on any mismatch. Never ask Michal to test another SHA.

3. **Run a quiet extension-origin allowlist gate.**
   - Inspect only the assignment for `FRAMENEST_COMPANION_EXTENSION_ORIGINS`; never print the file or right-hand side.
   - Emit only assignment count, JSON-array validity, entry count, exact-format validity, uniqueness, and loaded-extension membership as PASS/FAIL.
   - Accepted structure remains zero to four unique exact `chrome-extension://[a-p]{32}` entries; live acceptance requires the manifest-pinned extension origin to be present.
   - GET history visibility is not proof: GET routes can work with an empty allowlist while four mutations remain denied.
   - Absence, malformed data, duplication, or mismatch stops testing. Any EnvironmentFile correction/restart is a separate task.

4. **Run deterministic evidence at `T` before using Michal’s time.**
   - Run `./.ap/ap project check` with exact baseline `T`.
   - Through `./.ap/ap exec --operation test-focus`, run the configuration, route-policy, Tailscale-ingress, companion application/tag, repository, API, X companion, and companion migration tests.
   - Run Node’s built-in runner over `tests/x_companion_extension.test.js`, `tests/companion_review_extension.test.js`, and `tests/companion_web_bridge.test.js`.
   - These suites own non-v1 list inclusion, corrupt JSON not breaking the mixed page, omitted-category pending rows, badge math, protocol/target-origin pinning, frame survival, 403 behavior, tag union and 409 overflow, Apply not publishing, movie exclusion, Settings state, stale-context handling, and minimized manifest permissions.
   - Gated synthetic browser evidence is optional only under a separately authorized browser-evidence task; a skip is not PASS.

5. **Inventory usable live data without disclosing it.**
   - Report aggregate counts only: analyzed, pending, unopened, and whether six analyzed rows exist.
   - Reuse existing non-movie rows. Do not mutate the live database to create corrupt JSON, non-v1 suggestions, 32-tag overflow, identities, or styling fixtures.
   - Do not enable automatic analysis or contact a provider merely to seed acceptance.

6. **Load the exact extension and connect.**
   - Load `extension/` from checkout `T`, privately verify the Brave ID, refresh existing X tabs, and reopen the side panel.
   - Begin disconnected and use the Tailscale HTTPS workspace origin. Loopback and the future public-origin companion are outside this backlog.
   - Michal verifies that Connect opens Settings, Save is below the origin and enabled only when dirty, equivalent/trailing-slash forms canonicalize, only the requested tailnet host permission is granted, successful status is blank, and the hosted frame loads.

7. **Establish hosted-frame and Attach baseline.**
   - With a controlled reply composer and an existing published non-movie test item, verify Attach succeeds without posting.
   - If no safe published item exists, mark this evidence unavailable; do not publish ad hoc.
   - An empty ordinary Gallery after a new unpublished Save is expected.

8. **Exercise Save and pending history.**
   - With one owner-approved public X test item, verify Title → Tags → Description → Save, no category radios, no Analyze, and one preselected `x`/𝕏 seed.
   - Submit once; verify the omitted-category/GENERAL Save appears as a pending own-save under All.
   - Pending must not increment the badge.
   - Opening the pending row shows waiting copy, sends no opened/apply mutation, and never removes the row.
   - Closing it leaves the hosted frame mounted and Attach functional.

9. **Exercise merged history, chrome, and badge.**
   - Verify one title-bar history and no `#review-inbox`.
   - Compact history is newest analyzed first, capped at five; All adds pending and older analyzed rows.
   - Title bar, rows, and All use dark/outline language rather than solid neon fills; pending is muted and the newest unopened analyzed row may have stronger accent.
   - Clicking never removes rows, and the badge equals API `unopened_count`, not visible-row count.
   - If fewer than six analyzed items exist, combine available rendered evidence with deterministic coverage rather than manufacturing data.

10. **Exercise the analyzed click path.**
    - An analyzed click must open hosted Details inside the surviving `#frame`, not `ui/review.html`.
    - Close Details and confirm the row, frame, and Attach remain.
    - Deterministic evidence—not a deliberately broken live origin—owns message version, `{mediaId}` payload, exact stored target origin, absence of wildcard target, and no review-overlay fallback on handshake failure.

11. **Exercise ordinary 403 conditionally.**
    - If an existing mapped ordinary profile is available, confirm history/badge hide, collapse, and disable while the hosted iframe and Attach remain.
    - Do not edit the identity map for this test. Otherwise record live evidence as NOT RUN and retain deterministic coverage.

12. **Exercise stale context last, then disconnect.**
    - Reload the unpacked extension while an X tab/surface remains open.
    - First stale interaction must show the specific recovery copy, remove partial hosts, and disable affected controls.
    - Refresh/reopen and confirm recovery.
    - Disconnect must clear stored origin, granted host permission, alarm/badge, and in-flight state.

13. **Report sanitized outcomes.**
    - Report `T`, schema, boolean/scalar preflight results, deterministic test totals, and scenario PASS/FAIL/NOT RUN.
    - Never report hostnames, allowlist values, extension-origin values, X URLs, titles, UUIDs, cookies, headers, identity-map entries, or raw journals.

### Evidence ownership

| Evidence | Owner |
|---|---|
| Exact public-main/NUC SHA, schema, service, backup, and audience | Orchestrator/release operator |
| Allowlist presence/format/membership booleans | Explicitly authorized read-only NUC preflight or Michal |
| Rendered chrome, Settings, Save, pending flow, hosted Details, Attach continuity, and stale-copy UX | Michal |
| Listing resilience, badge math, route/manifest contracts, protocol pinning, Apply union/409/no-publication, and movie exclusion | Deterministic evidence Worker |
| Trust-boundary severity | Independent INFOSEC audit Worker |
| Remediation slicing, publication, NUC refresh, and retest ordering | Orchestrator |

### INFOSEC finding route

1. Stop the affected mutation path; do not improvise CORS, identity, allowlist, or EnvironmentFile changes.
2. Capture only target SHA, scenario ID, bounded timestamp, status/error class, and a sanitized chrome-only screenshot if useful.
3. Issue an independent read-only audit covering origin admission, mutation proof, capabilities, audit-before-execute, message pinning, content-script isolation, publication, movie exclusion, and leakage.
4. Orchestrator classifies expected behavior, configuration, UX defect, companion security defect, or frozen public-net concern.
5. Issue one bounded remediation Worker per defect.
6. Run focused Python evidence through `./.ap/ap exec` plus the relevant Node suite.
7. Independently verify, publish to public `main`, refresh the NUC to that exact SHA, and ask Michal to rerun only the failed scenario and adjacent regression.

Immediate security stops include accepting an unallowlisted origin or missing mutation header, ordinary-user admin access, wildcard messaging, new CORS, content-script server fetches, Apply creating publication, companion movie inclusion, or private data in evidence.

### Preserved invariants

- The backlog tests the Tailscale administrator loop; public-origin reconnect remains rollout step 7 and a separate whole.
- The extension checkout, public main, and NUC active release share one exact SHA.
- Loopback-first composition, Tailscale-only workspace access, no public listener, Funnel, router forwarding, or CORS.
- Exactly four `companion_mutation` routes.
- Apply writes metadata only and never publishes; administrator PUT is the sole publication route.
- Movies remain excluded from companion workflows.
- Automatic analysis remains false in tracked files; live enablement is a separate owner decision.
- No `notifications` permission.
- The hosted frame remains mounted and Attach survives history interactions.
- No live database fixture edits, identity-map changes, provider calls, or automatic-analysis enablement without separate authority.

## Open questions for Michal

1. Is one genuine interactive owner-wrapper run acceptable now? **Default: yes; route A.**
2. Is the 03/10 Brave backlog explicitly reopened, or should the plan remain queued after NUC refresh? **Default: remain parked until an explicit message.**
3. Is deterministic Apply evidence sufficient, or is a new rendered Apply entry required? **Default: deterministic-only; a rendered entry is a separate product whole.**
4. Which disposable public X item may be used, and is real acquisition explicitly authorized? **Default: one owner-selected item, never identified in evidence.**
5. Are existing analyzed rows and a mapped ordinary profile available? **Default: reuse existing data/profile; otherwise mark the dependent live case NOT RUN.**
6. If the quiet allowlist gate fails, may a separate EnvironmentFile/restart task be issued? **Default: stop and request that task.**
7. Must the exact five-plus-remainder history be rendered if six analyzed rows are unavailable? **Default: no synthetic live-data mutation; combine rendered and deterministic evidence.**

## Proposed next-task coordinates

These are proposals only and grant no authority.

1. **Worker session 02 / exchange 01 — documentation coherence and exit-13 runbook annex**
   - Documentation plus the two parity-test files only.
   - No NUC, deployment, wrapper-home-file inspection, or product code.
   - Validate through focused AP contract tests.

2. **Worker session 03 / exchange 01 — optional tracked noninteractive wrapper**
   - Issue only if Michal selects repository automation after the annex.
   - Keep the four-command helper interface and migration-free engine.
   - Test exit 0/13/all-other handling, exact lock cleanup, target migration, cutover, final status, and terminal sudo release.

3. **Worker session 04 / exchange 01 — deterministic companion acceptance**
   - Requires explicit unpark and exact baseline `T`.
   - Read/test only; no provider, NUC mutation, or fixture injection.
   - Produce a sanitized evidence matrix for Michal’s rendered pass.

4. **Worker session 05 / exchange 01 — independent INFOSEC audit**
   - Issue only for a concrete security finding.
   - Read-only, finding-specific, no remediation.

5. **Worker session 06 / exchange 01 — bounded remediation**
   - One finding per Worker; exact path/test allowlist.
   - Publication and NUC refresh remain separate follow-on authority.

6. **Worker session 07 / exchange 01 — companion documentation closeout**
   - Only after Michal resolves outline chrome and rendered-Apply expectations.
   - Correct “fade by position” and acceptance prose without reopening product code.

## Evidence limits and defaults

- No test, browser, provider, SSH, sudo, wrapper, or NUC command was executed.
- No wrapper internals were inspected; route A relies on the Orchestrator-verified facts in the issued prompt.
- Local checkout was clean at HEAD `0706818…`; its local `origin/main` tracking ref was stale at `06af60a…`. Public-main equality comes from the issued verified facts and must be re-proved by `check` at execution.
- No claim is made that the live allowlist, test identities, or required media fixtures are present.
- Native Plan Mode prohibited filesystem mutation, so `01_report.md` was not created. This block is the decision-ready report content to persist only under an execution-authorized turn.
