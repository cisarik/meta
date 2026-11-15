# BookRadar — Targeted C16 Browser Evidence Probe — Governed Review and Promotion

Persistent role identity: WORKER
Logical whole identity: bookradar-review-and-promotion-workflow
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: Independent Audit
Task identity: BOOKRADAR-REVIEW-PROMOTION-C16-BROWSER
Delivery route: manual Cooperator delivery (prompt-file pointer)
Reasoning recommendation: Medium — one narrow, deterministic browser-evidence probe with an authorized temporary Playwright adapter; no product code, schema, or repository dependency change.
Recommended context capacity: approximately 250k tokens
Independence required: yes
Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-review-and-promotion-workflow
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_browser_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: one exact temporary probe root under /private/var/folders/93/7fg3d5j17wxdkyh6nlyz239m0000gn/T/opencode/; install only playwright@1.65.1 into that root; optional temporary Chromium download into that root; loopback browser only
Trace persistence: direct-write /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/03_report_00.md

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: C1–C15 and C17 already PASS in `02_report_00.md`; do not re-run the full acceptance matrix
Affected tests: C16 rendered browser evidence only
New causal regression: none — this is the named missing-evidence probe for C16
Broad or full suite: not-used
Runtime or testbed: local loopback Playwright/Chromium browser testbed
Independent acceptance: required-separate-fresh-worker

Repeated-gate or reasoning-loop stop: configured
Broad gate: not-used — targeted C16 only
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes

Development envelope activation: not-used

## Purpose and independence

The independent audit `02_report_00.md` passed C1–C15 and C17 but could not run
C16 because Playwright/Chromium was absent. This is the Orchestrator-authorized,
COOPERATOR-approved targeted probe for that one missing claim. It does not
re-open the other controls and does not perform a new full acceptance.

You are a fresh WORKER in the `Fresh Evidence Probe` profile. Your first input
for this task is this prompt. You did not plan, implement, or correct the
candidate. Do not read or rely on an implementing conversation. The candidate is
frozen; do not modify it. If you have materially participated in the
implementation, stop and report `BLOCKED` rather than claim independence.

This probe is read-only with respect to the repository. Do not edit repository
files, add tests, commit, push, tag, change branches, or add a repository
dependency. The authorized host mutation is limited to the temporary probe root
and the Playwright/Chromium adapter used for C16. If a page assertion fails,
report the finding; do not correct the product.

## Candidate and prerequisite evidence

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Expected branch: `main`
Acceptance candidate: `80b172c2db6fcacc93041d4eb4c246450547f112`
Candidate parent: `69ec45e245108c90e2de4302c03ca72572bf1829`
Candidate tree: `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
Candidate subject: `docs: demonstrate governed conflict resolution`
Public `refs/heads/main`: still `2281982f7dae0ef1f582d294592c41281ba11b21`
Local state: `main` is two commits ahead of `origin/main`; worktree clean; no
push, tags, or extra refs
Governing AP: `.ap` gitlink and detached checkout
`d7023cf037f6d17885c3ede5c04812c61640da50`

Frozen evidence:

- independent audit `02_report_00.md` SHA-256
  `5286deaeb6a28ab5d8d7ab35829eecde21a52f16894b22807e2b017083012f8f`,
  251 lines, `status: BLOCKED`, C1–C15/C17 PASS, C16 NOT-VERIFIED;
- audit prompt `02_acceptance_00.md` SHA-256
  `ffdea5259956cb521dede5b46d04e1138a4fe8faff41934a507797157baebf98`;
- approved plan `01_report_00.md` SHA-256
  `e08189f9534208d4f1dee91d289014d536cad88327236691a9deb8a68e9ecc22`;
- correction report `01_report_02.md` SHA-256
  `f08aee0b9c4da4a1d53c5ddfd0021821db634ed5c88f8efbfef3c9daae6a8108`;
- provisional handout `00_handout_00.md` SHA-256
  `ea5985ff63853098c8f2de5dc59977a30d5374acc0f812f23107e70656e997fd`;
- predecessor closure SHA-256
  `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`.

Before probing, verify HEAD, parent, tree, subject, branch, clean worktree,
`.ap` pin, and strict `./.ap/ap doctor` PASS. If the candidate identity differs,
stop and report; do not probe a different candidate.

## Required reading

- `.ap/AP.md`: RF-05, RF-07, RF-11, RF-18, RF-19; §3; §11 Browser and Rendered
  Acceptance Automation; §12; §18.
- `.ap/AP_WORKER.md`: Session Profile and Independence; Worker Session Target;
  Worker Exchange Coordinates and Trace Boundary; Before Mutation; Validation;
  Reporting; Stopping Conditions.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Fresh Evidence Probe;
  Validation Ladder Record; Browser Stall Guard Contract; Cooperator Delivery
  and Trace Destination Record.
- `02_acceptance_00.md`, `02_report_00.md` (especially C16, the Browser Stall
  Guard record, and the temporary-state section), `01_report_00.md` §11,
  `01_report_02.md`, `README.md` `## Governed review and promotion`, and this
  whole's `00_notes.md`.
- The current `bookradar-ui` config/render/http code and tests, the promotion
  and review CLI, and the fixture `crates/bookradar-store/tests/fixtures/research/newer.json`.

## Authorized temporary adapter

The COOPERATOR has explicitly authorized a local Playwright adapter outside the
repository. Use one exact temporary root under:

```text
/private/var/folders/93/7fg3d5j17wxdkyh6nlyz239m0000gn/T/opencode/bookradar-c16-probe.XXXXXX
```

Create it with `mktemp -d` and record the exact path. Keep the npm cache, npm
logs, Playwright package, optional browsers, demo databases, and the probe script
inside that root. Remove the entire root at the end and report the cleanup
outcome.

Install only this package:

```bash
export npm_config_cache="$root/npm-cache"
export npm_config_logs_dir="$root/npm-logs"
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
npm install --prefix "$root" playwright@1.65.1
```

First try the installed Chrome channel:

```js
const { chromium } = require('playwright');
const browser = await chromium.launch({ channel: 'chrome', headless: true });
```

`/Applications/Google Chrome.app` is present. Record `browser.version()`.
If the Chrome channel cannot launch, set:

```bash
export PLAYWRIGHT_BROWSERS_PATH="$root/browsers"
unset PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD
"$root/node_modules/.bin/playwright" install chromium
```

and use `chromium.launch({ headless: true })`. The fallback download is
authorized into the temporary root only. Do not install Playwright or Chromium
into the repository, do not change `Cargo.toml`/`Cargo.lock`, and do not add a
package manifest to the project. Network authority is limited to the npm
registry for `playwright@1.65.1` and, only if needed, the Playwright Chromium
download; loopback UI traffic; no other network.

If the adapter cannot be installed or launched even after the fallback, stop
`BLOCKED` with the exact adapter failure and cleanup. Do not substitute the
existing `browser` tool or a non-Playwright check for C16.

## Synthetic data setup

Use the existing built binaries under `target/debug` if present; otherwise build
with:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
cargo +1.99.1 build --locked --offline \
  -p bookradar-store --bin bookradar-research --bin bookradar-review --bin bookradar-poc \
  -p bookradar-ui --bin bookradar-ui
```

Create the demo databases under `$root/data` and use the README sequence:

1. `bookradar-research init` and import
   `crates/bookradar-store/tests/fixtures/research/newer.json` at `1793545200`.
2. `bookradar-poc init` the observation store.
3. Promote observation 1: source 1, offer 1, observation 1, edition 10,
   observed `1793548100`, offset `3600`, ingested/assessed/recorded
   `1793548700`, `manual` evidence, reviewer statement/reference/approval/
   assessor/rationale as in the README.
4. Start the UI for state A, verify, stop it.
5. Promote observation 2: same finding, source 1, offer 1, observation 2,
   edition 11, same observed `1793548100`, same timestamps and attestation.
   Start the UI for state B, verify, stop it.
6. Append `bookradar-review review` on observation 2 with
   `--expected-revision 1 --knowledge rejected --assessed-at 1793548750
   --recorded-at 1793548750`, assessor `reviewer:assessor`, rationale
   `reviewer:reject-conflicting-edition`. Start the UI for state C, verify, stop
   it.
7. Promote the same finding again: source 2, offer 7, observation 1, edition 10,
   same observed instant and timestamps, `--source-statement reviewer:offer-seven`.
   Start the UI with `--source-id 2 --offer-id 7` for state D, verify, stop it.

For each UI start use `--bind 127.0.0.1:0`, `--now 1793548800`, the exact
`--store` and `--research-ledger`, and the configured source/offer flags. Read
the printed `listening=http://127.0.0.1:<port>` line; use that exact URL. The UI
is a startup snapshot, so restart it after each database change. Do not leave a
listener or process running.

## C16 browser scenarios and assertions

Use a fresh browser context per viewport and scenario. Verify both
`1280×800` and `375×812` for states A, B, and C; state D may use the desktop
viewport plus a mobile layout check.

**State A — after the first promotion.** The page must show
`source 1, offer 1`; `Checked available — Unix 1793548100; expires at Unix
1793634500`; conflict `clear`; candidate 1 eligible; the research section must
show the research candidate as `unreviewed`, `agent-only`, `not-eligible` and
must not turn it into verified stock.

**State B — after the second promotion.** The page must show the configured
offer; `Unverified — unresolved conflict`; conflict `unresolved`; no
`Checked available`; both observations remain in history. The research card
stays unreviewed/agent-only/not-eligible.

**State C — after the rejection.** The page must show `Checked available — Unix
1793548100; expires at Unix 1793634500`; conflict `clear`; observation 1
supported; observation 2 has both `Revision 1` supported and `Revision 2`
rejected; the research card remains not eligible.

**State D — non-default offer.** The page must show `source 2, offer 7` and
`reviewer:offer-seven`; it must not fall back to `source 1, offer 1` or show
`reviewer:statement` as the configured offer row.

**HTTP controls on each state.** Using Playwright request contexts with the
exact loopback URL:
- `GET /` and `GET /style.css` return `200`;
- `HEAD /` and `HEAD /style.css` return `200` with empty bodies;
- `POST /` returns `405` with `Allow: GET, HEAD`;
- `GET /api` returns `404`;
- response headers include `Content-Security-Policy: default-src 'none'`,
  `X-Content-Type-Options: nosniff`, `Cache-Control: no-store`,
  `Referrer-Policy: no-referrer`, and
  `Cross-Origin-Resource-Policy: same-origin`;
- no `<script` or `<form>` in the page.

**Browser observations.** Collect `console` messages, `pageerror`, and every
request URL. Require no console errors and no page errors; all requests must be
loopback `http://127.0.0.1:<port>` (plus any `data:` or same-origin stylesheet).
Record request counts and any non-loopback attempt as a finding. Do not commit
or write screenshots outside the temporary root; DOM/text/console/network
evidence is preferred.

**Responsive check.** At `375×812`, the configured query, current assessment,
history, and research headings/text must remain visible; record any horizontal
overflow or clipped key text. Do not fail on harmless wrapping, but record it.

**Browser Stall Guard.** Record the exact adapter and browser versions, launch
count, viewports, state/scenario results, console/page/network observations,
failure episode, recovery attempts (at most two meaningful attempts), and
cleanup. If the adapter is absent and cannot be installed, or the browser cannot
launch after the fallback, stop `BLOCKED` with the guard record. Missing
evidence never becomes PASS.

## Temporary state and cleanup

Declare and report:

```text
Temporary root: <exact absolute path>
Owner: WORKER (this probe)
Mode: <permission mode>
Contents class: synthetic fixtures, temporary Playwright adapter/browser, demo databases
Cleanup owner: WORKER (this probe)
Cleanup outcome: removed | retained-with-reason
```

Stop every `bookradar-ui` child, close every browser/context, remove `$root`,
and verify `git status --porcelain` is empty and HEAD is still
`80b172c2db6fcacc93041d4eb4c246450547f112`. Do not delete or move the
`refs/codex/turn-diffs/checkpoints/*` harness refs.

## Report contract

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the prompt's coordinate values exactly once at the top of the report
metadata, then the routing fields. Include:

- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: not-applicable`
- `Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `Start commit: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `End commit: 80b172c2db6fcacc93041d4eb4c246450547f112`
- `Changed files: none`
- `Tests and validation: <C16 evidence; candidate identity; no full gate rerun>`
- `Git result: none`
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: Orchestrator combines C1–C15/C17 from 02_report_00.md with C16; COOPERATOR acceptance sign-off; publication separate`
- `Report justification: new-evidence`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the probe grant; no autonomous continuation.`
- Echo the SHA-256 of `03_browser_00.md`.
- `Orchestration critique:` with exactly `MEASURED:` and `LEAD:` lines.
- `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>`
- `Pre-Existing Failure Classification: none | <complete classification>`
- `C16: PASS | FAIL | BLOCKED` with the exact evidence.
- `Acceptance independence: required-fresh-independent`
- `Temporary root: <path>; Cleanup outcome: removed`.

The body must include the adapter versions, launch count, viewports, state A–D
results, HTTP/header results, console/pageerror/network observations, Browser
Stall Guard record, temporary-state cleanup, and an explicit statement that this
probe does not close the whole or authorize publication.

## Stopping conditions

Stop and report without improvisation if:

- the candidate, parent, tree, branch, cleanliness, `.ap` pin, or `ap doctor`
  differs from the declared state;
- this is not a genuinely fresh session or independence is compromised;
- Native Plan Mode is enabled;
- the Playwright adapter cannot be installed or launched after the authorized
  Chrome-channel attempt and one Chromium fallback;
- a browser or HTTP assertion fails;
- a console error, page error, or non-loopback request is observed;
- the repository becomes dirty, or a repo edit/dependency/commit/push would be
  required;
- context pressure makes the probe unreliable.

Do not correct the product, add a test, change the README, or install anything
into the repository. Report the exact blocker and preserved evidence.

## What happens next

The Orchestrator will combine the independent C1–C15/C17 evidence with this C16
probe, decide whether the acceptance package is complete, and present the
COOPERATOR acceptance sign-off. Publication remains a separate authority.
