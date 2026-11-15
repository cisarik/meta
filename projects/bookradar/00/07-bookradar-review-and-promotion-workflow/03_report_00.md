### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-review-and-promotion-workflow
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: Independent Audit
Task identity: BOOKRADAR-REVIEW-PROMOTION-C16-BROWSER
status: PASS
Phase-qualified result: not-applicable
Acceptance candidate: 80b172c2db6fcacc93041d4eb4c246450547f112
Start commit: 80b172c2db6fcacc93041d4eb4c246450547f112
End commit: 80b172c2db6fcacc93041d4eb4c246450547f112
Changed files: none
Tests and validation: C16 rendered Playwright/Chrome evidence for states A–D at 1280×800 and 375×812, plus loopback HTTP controls on each state. Candidate HEAD, parent, tree, subject, branch, clean worktree, local `origin/main`, and the `.ap` pin matched the grant before the probe and again after cleanup. Strict `./.ap/ap doctor` PASS before probing. C1–C15 and C17 were not rerun.
Git result: none
Deviations, risks, or missing evidence: none. The Chromium download fallback was not used. Mobile wrapping and nested table scroll are recorded below and were not failures. No screenshots were written. This Chrome channel evidence does not prove Safari or Firefox.
Smallest next step: Orchestrator combines C1–C15/C17 from 02_report_00.md with C16; COOPERATOR acceptance sign-off; publication separate
Report justification: new-evidence
Logical-whole closure: not-closed
Authority expiry: this terminal report ends the probe grant; no autonomous continuation.
Prompt SHA-256: `5a79fe7c78bcb810edf38058ed392a9ac65f5126b6fa062286edbfd476193fb4`
Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
C16: PASS
Acceptance independence: required-fresh-independent
Temporary root: /private/var/folders/93/7fg3d5j17wxdkyh6nlyz239m0000gn/T/opencode/bookradar-c16-probe.kUMfbg; Cleanup outcome: removed

This session's first task input was `03_browser_00.md`. It did not plan, implement, or correct the candidate. The candidate was not modified. This probe does not close the logical whole and does not authorize publication.

## Candidate identity

Directly observed before probing, and again after cleanup except the public read:

- HEAD `80b172c2db6fcacc93041d4eb4c246450547f112`
- parent `69ec45e245108c90e2de4302c03ca72572bf1829`
- tree `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
- subject `docs: demonstrate governed conflict resolution`
- branch `main`, clean `git status --porcelain`, two commits ahead of `origin/main`
- local `refs/remotes/origin/main` `2281982f7dae0ef1f582d294592c41281ba11b21`
- public `git ls-remote origin refs/heads/main` before probing returned the same SHA
- `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`
- strict `./.ap/ap doctor` printed `ap doctor: PASS` and `OK resolved governing variant: stable`

Existing `target/debug` binaries were used. Cargo was not run. No repository file, dependency, commit, push, tag, or branch change was made. Eight `refs/codex/turn-diffs/checkpoints/*` refs were still present after the probe and were not moved or deleted.

## Adapter and browser

`playwright@1.65.1` was installed only under the temporary root, with `npm_config_cache` and `npm_config_logs_dir` inside that root and `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`. Nothing was installed into the repository.

Launch count: 2. Both used `chromium.launch({ channel: 'chrome', headless: true })`.

1. Channel check. `browser.version()` was `157.0.8103.39`. The browser was closed without opening a page.
2. Scenario launch. `browser.version()` was again `157.0.8103.39`. Eight fresh contexts covered states A–D at both viewports. The browser was closed.

`/Applications/Google Chrome.app` was present. The Playwright Chromium download was not required and was not run.

```text
Failure episode identity: c16-chrome-channel
Prior episode identity: none
Episode relationship: initial
Symptom continuity evidence: none — the Chrome channel launched and all eight rendered contexts completed
Initial verification result: succeeded
Recovery attempts: 0
Recovery attempt 1: not-used because the Chrome channel launched and the scenarios completed
Recovery attempt 2: not-used because recovery attempt 1 was not used
Verification succeeded: yes
Repeated failure remains unresolved: no
Conclusive no-progress evidence: no
Stall guard: not-triggered
Repeated failure evidence: none
Guard rationale: the authorized Chrome channel launched on the first try; the Chromium download fallback was not required
Evidence preserved: yes
Browser repair after trigger: none
Alternative evidence: not-required
Absent verification: none
Cooperator acceptance required: no
Result claimed from missing evidence: none
```

`Cooperator acceptance required: no` applies only to absent browser verification. The combined acceptance sign-off remains a separate COOPERATOR step.

## Synthetic setup

Databases lived under the temporary root. Every command exited 0.

- `bookradar-research init` printed `created research_schema=1`.
- import of `crates/bookradar-store/tests/fixtures/research/newer.json` at `1793545200` printed `run=complete seen=1 admitted=1 replayed=0 rejected=0 quarantined=0 conflicts=0 projected=1`.
- `bookradar-poc init` printed `created schema=1 synthetic=true`.
- first promote printed `promoted source=1 offer=1 observation=1 provenance=research:synthetic:producer/synthetic:run/synthetic:newer@1/0`.
- second promote printed `promoted source=1 offer=1 observation=2 provenance=research:synthetic:producer/synthetic:run/synthetic:newer@1/0`.
- review printed `reviewed source=1 offer=1 observation=2 revision=2`.
- offer-seven promote printed `promoted source=2 offer=7 observation=1 provenance=research:synthetic:producer/synthetic:run/synthetic:newer@1/0`.

Each UI process used `--bind 127.0.0.1:0`, `--now 1793548800`, the temporary store and ledger, and the stated source/offer flags. The probed URL was the printed `listening=` line. Each process was stopped with SIGTERM and reported `closed`. A final `pgrep` found no `bookradar-ui`.

Desktop and mobile DOM extracts were identical in every state. Text below is from the rendered page, not from an HTTP-only substitute.

## State A — first promotion

URL `http://127.0.0.1:52543`. Both viewports.

- Configured offer: `source 1, offer 1`.
- Truth: `Checked available — Unix 1793548100; expires at Unix 1793634500`.
- Current-assessment conflict: `clear`. Verification eligibility: `eligible`. Candidate 1: `eligible`.
- History: observation 1, statement `reviewer:statement`, revision 1 `supported`.
- Research card title `Research candidate — unreviewed`, evidence `agent-only`, eligibility `not-eligible`, statement `synthetic:newer`. The research section did not contain `Checked available`.
- The page contained no `<script` and no `<form`.

## State B — second promotion

URL `http://127.0.0.1:52557`. Both viewports.

- Configured offer: `source 1, offer 1`.
- Truth: `Unverified — unresolved conflict`.
- Current-assessment conflict: `unresolved`. Verification eligibility: `not-eligible`. Candidates 1 and 2: `not-eligible`.
- The page did not contain `Checked available`.
- History kept observation 1 and observation 2. Each had statement `reviewer:statement` and revision 1 `supported`.
- Research card stayed `Research candidate — unreviewed`, `agent-only`, `not-eligible`, and its own conflict field stayed `clear`. It did not contain `Checked available`.
- The page contained no `<script` and no `<form`.

## State C — rejection

URL `http://127.0.0.1:52570`. Both viewports.

- Truth: `Checked available — Unix 1793548100; expires at Unix 1793634500`.
- Current-assessment conflict: `clear`. Verification eligibility: `eligible`. Candidate 1: `eligible`. Candidate 2: `not-eligible`.
- Observation 1: revision 1 `supported`.
- Observation 2: revision 1 `supported` and revision 2 `rejected`.
- Research card remained `unreviewed`, `agent-only`, `not-eligible`, with no `Checked available`.
- The page contained no `<script` and no `<form`.

## State D — non-default offer

URL `http://127.0.0.1:52582`. Desktop 1280×800 and mobile 375×812.

- Configured offer: `source 2, offer 7`.
- The page did not contain `source 1, offer 1` and did not contain `reviewer:statement`.
- History observation 1 statement: `reviewer:offer-seven`.
- Research card statement remained `synthetic:newer`, still `unreviewed`, `agent-only`, and `not-eligible`.
- The page contained no `<script` and no `<form`.

## HTTP controls

Playwright `request.newContext()` called the same loopback URL for every state. Results were the same except the `GET /` body length:

| State | GET / body |
| --- | --- |
| A | 7300 |
| B | 9759 |
| C | 10350 |
| D | 7302 |

On every state:

- `GET /` and `GET /style.css` returned 200. The stylesheet body length was 1302.
- `HEAD /` and `HEAD /style.css` returned 200 with body length 0.
- `POST /` returned 405 with `Allow: GET, HEAD`.
- `GET /api` returned 404.
- `GET /` contained no `<script` and no `<form`.
- Every one of those six responses included `Content-Security-Policy: default-src 'none'; script-src 'none'; style-src 'self'; img-src 'none'; font-src 'none'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'`, `X-Content-Type-Options: nosniff`, `Cache-Control: no-store`, `Referrer-Policy: no-referrer`, and `Cross-Origin-Resource-Policy: same-origin`.

## Console, page errors, and network

Each of the eight page contexts recorded an empty console list and an empty page-error list. Each page made exactly two requests: `GET` of the document and `GET` of `/style.css`, both at `http://127.0.0.1:<port>`. No `data:` URL and no non-loopback URL was requested. The HTTP control calls above were separate loopback API requests to that same origin.

## Responsive check

At 1280×800, document `scrollWidth` equalled `clientWidth` (1280) in every state. No measured heading, truth line, query value, or observation summary was clipped. Both `.table-wrap` boxes were 1112 by 1112.

At 375×812, document `scrollWidth` equalled `clientWidth` (375) in every state. Required headings, the current truth line, query values, and observation summaries had non-zero boxes inside the horizontal viewport. Harmless wrapping was recorded and not failed:

- the store and ledger paths wrapped to about 72px height;
- the checked-available truth line wrapped to about 90px, and the unresolved-conflict line to about 60px;
- `Research current candidates` wrapped to about 72px;
- `Research candidate — unreviewed` wrapped to about 56px.

The research-findings `.table-wrap` had `scrollWidth` 524 and `clientWidth` 295 in every mobile state, so that table scrolls inside its own container. The receipts table fit (295 by 295). This nested scroll did not widen the document and did not clip the required headings. Revision text inside closed `<details>` was checked in the DOM; those collapsed bodies were not painted until disclosure, and their visible summaries were not clipped.

## Temporary state and cleanup

```text
Temporary root: /private/var/folders/93/7fg3d5j17wxdkyh6nlyz239m0000gn/T/opencode/bookradar-c16-probe.kUMfbg
Owner: WORKER (this probe)
Mode: drwx------ (700)
Contents class: synthetic fixtures, temporary Playwright adapter/browser, demo databases
Cleanup owner: WORKER (this probe)
Cleanup outcome: removed
```

The root, including the npm cache, npm logs, Playwright package, probe script, and demo databases, was removed. A following existence check found it absent. No `bookradar-ui` process remained. `git status --porcelain` was empty and HEAD was still `80b172c2db6fcacc93041d4eb4c246450547f112`.

This report records the C16 probe only. It does not close the logical whole, does not publish, and does not authorize publication.
