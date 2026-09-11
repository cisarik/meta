# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, Release-Readiness Triage and Autonomous Completion

Authored by the Agent Orchestrator at the closure of logical whole 18 (`dockerized-vps-deployment`) at commit `996d9c78af90d1fea21e3c701283ba11e59de0b1`, on 2026-09-10. Seeds ONE candidate logical whole: `release-readiness-triage`, and explicitly authorizes the fresh Orchestrator to continue autonomously into the successor logical wholes it produces. This handout is the Cooperator's explicit instruction; it is NOT a substitute for current repository truth or AP protocol.

---

## Handout Integrity Record (D-13)

```text
Supersedes: none — this file is a NEW forward-horizon handout for a future effort.
Sections of other handouts that remain LIVE: none carried here.
Coordinate review: honest; written against the published commit
  996d9c78af90d1fea21e3c701283ba11e59de0b1 on 2026-09-10. Repository facts below were read from the
  whole-17 and whole-18 closure records and Meta 17/18 artifacts, not re-measured token-by-token in
  this session; mark every file:line claim as hypothesis and re-measure before citing.
Enumeration fidelity: the seeded open-item inventory in section 3 is PARAPHRASED from closure
  records, audit reports, and project docs. It is a hypothesis list to verify and widen, never a
  specification. Re-derive every path and status from the live tree.
Numbers not re-measured: live VPS state, provider quotas, host capacity, domain/DNS records, ACME
  limits, remaining open items not yet recorded anywhere. All are unknown until measured.
Known-stale-by-design: the host does not exist yet; UI/UX polish and VPS deployment are explicitly
  deferred Cooperator phases. Nothing here claims a live install or a release.
Predecessor whole: 18/00-dockerized-vps-deployment CLOSED at 996d9c7 (published, public main aligned).
Earlier closures: 17/00-public-docs-and-stale-truth CLOSED at f6ec9bf; 16/00-infosec-hardening-and-vps-
  readiness CLOSED at 33ffa15.
Baseline commit: 996d9c78af90d1fea21e3c701283ba11e59de0b1 (clean tree, origin/main aligned at closure).
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (detached HEAD at .ap, DO NOT upgrade).
Meta archive: /home/agile/meta, layout per /home/agile/meta/README.md.
```

---

You are a fresh Agent Orchestrator for Libre Tiles. This handout grants you the role-framing and the Cooperator's explicit instruction to run the effort below; concrete task authority over Workers still comes from the authoritative prompts you issue. Verify repository and public truth independently before issuing anything.

Candidate logical whole identity: `release-readiness-triage`

---

## 0. Cooperator intent (verbatim decisions)

```text
The Cooperator is deferring the real-VPS public deployment. Before publication he still has
testing and UI/UX polish ahead. He knows there are parked items, frozen decisions, accepted
defects, gaps, and detours that must first be separated into bounded logical wholes.

He explicitly instructed: first run a Planner Worker (native planning mode active) that finds all
unfinished work and decomposes it into logical wholes with a recommended order; then the
Orchestrator orchestrates the completion/fixes autonomously. After this cleanup: UI/UX polish,
then VPS deployment.

The first Planner prompt is delivered manually by the Cooperator to another model; its report is
returned manually. From the second exchange onward the Orchestrator may dispatch Workers natively
as subagents and MUST archive every prompt and report into Meta exactly per the Meta/AP storage
contract.
```

## 1. Mission

1. Discover, verify, and inventory every unfinished, parked, frozen, deferred, superseded-without-replacement, accepted-defect, or known-gap item in the Libre Tiles project.
2. Decompose that inventory into bounded, evidence-grounded logical wholes with priorities, dependencies, acceptance routes, and a recommended execution order that ends **before** UI/UX polish and VPS deployment.
3. Obtain Cooperator approval of the decomposition.
4. Execute the approved wholes autonomously, one logical whole at a time, with the full AP lifecycle (planning where needed, implementation, independent acceptance where required, bounded correction, closure), reporting to the Cooperator only at material gates and Cooperator-owned decisions.
5. Leave both UI/UX polish and VPS deployment as explicitly deferred Cooperator phases with clear prerequisites.

## 2. Verified starting state (re-measure before citing)

```text
T1  Repository: /home/agile/Projects/libretiles; branch main; HEAD == origin/main ==
    996d9c78af90d1fea21e3c701283ba11e59de0b1; working tree clean at closure.
T2  AP pin: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
T3  Whole 18 published the hardened Docker Compose deployment (commit 996d9c7): nginx-only public
    edge, loopback Next in nginx's netns, Daphne on a group-restricted Unix socket, dedicated secret
    GID 10004, Certbot TLS lifecycle, validated backup/restore, static + disposable-Docker guards.
T4  Whole 18 closure record: /home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/
    99_closure.md — includes the residual table, ledger candidates, and forward horizon.
T5  Whole 18 R5 handout for live host deployment:
    18/00-dockerized-vps-deployment/90_live-host-deployment-handout.md (NOT opened; needs Cooperator
    host grant and costed decisions C1–C7 there).
T6  Whole 17 archive: 17/00-public-docs-and-stale-truth/ (closure, residual table, reports).
T7  Project context and defect ledger: /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md and
    DEFECT_LEDGER.md — read and revalidate; do not treat as current authority.
T8  Standing gates (AGENTS.md): backend env-cleared .venv route (mypy/ruff/makemigrations/pytest);
    frontend npm typecheck/lint/build; disposable Docker validator
    ./scripts/validate_docker_deployment.sh; prompt field check
    python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>.
T9  Cooperator language is Slovak. Material decisions and costed choices must be presented legibly
    to him; authoritative prompts and reports are structurally English per AP.
```

## 3. Seeded open-item inventory (HYPOTHESIS — verify, correct, widen, and reject false positives)

Carry-forward accepted residuals:

```text
R1  backend/tests/test_word_authority_parity.py payload-parity red (extra `inspection` block vs the
    pinned baseline). Accepted whole-17 residual; the oracle must NOT be edited to follow the
    implementation. Owner: codebase-hygiene whole.
R2  frontend/src/lib/i18n/i18n.test.ts AC-ONE-LIVE-REGION red: expected exactly one `aria-live`
    region, measured three (committed LiveAnnouncer/ReplayControls/SimulationArena components).
    Needs an accessibility-pin decision, not a blind test edit.
R3  frontend/src/components/admin/ReplayControls.test.ts stale expected text ("Ada played SZ for 12
    points") vs the committed fixture rendering "Ada played AT for 4 points".
R4  Whole-17 info residual: the AI judge route docstring lists Tier 2 as a pipeline tier.
R5  Whole-18 info residual: port 80 answers any well-formed Host with a 301 to the canonical domain
    instead of closing. Accepted low/info residual by Orchestrator.
```

Ledger candidates and observed noise:

```text
L1  X-Powered-By: Next.js on public responses; nginx version already suppressed.
L2  Undefined websocket paths return HTTP 500 with a Channels traceback.
L3  The nginx certificate watcher retries a failing `nginx -t` every 5 seconds while the reload
    marker persists.
L4  Malformed or `user@host`-style Host headers on port 80 receive nginx 400 with no redirect.
```

Documented gaps and deferred features (verify each against the live tree):

```text
G1  Tier 2 dictionary (optional API) — planned in the PRD and docs/architecture.md.
G2  Stronger AI search / candidate generation beyond prompt-only improvements.
G3  Eight machine-authored interface catalogs (de pt is it nl da sv af) have had no second-opinion
    review; REVIEWED_LOCALES = en sk cs pl; a thirteenth locale must not silently reintroduce the
    partial-flag-table defect.
G4  frontend/public/hu.png exists although `hu` is not a shipped locale; `drevo.jpeg` is present.
    Asset hygiene.
G5  CONTRIBUTING Node support matrix ("20.19+/22.12+") is a hypothesis without an `engines` field.
G6  GitHub Actions CI and SBOM remain out of previous cuts.
G7  Nine-provider capability coverage/status and the dynamic catalog rollout flags; the optional
    `libretiles-openrouter-catalog-refresh` schedule is a separate production authority.
G8  Session-storage/CSP hardening items referenced in earlier forward-horizon notes.
G9  AP parity-oracle re-pin and other codebase-hygiene items.
G10 Repository-wide parked markers and stale doc claims: search TODO/FIXME/HACK/XXX, "not done",
    "deferred", "planned", "accepted-residual", "carry forward", "out of scope"; verify each against
    code rather than trusting the prose. PRD phases and AGENTS.md "Not done yet" are claim sources.
G11 Test-breadth gaps: opt-in Postgres parity tests, internet-marked tests, browser/e2e coverage,
    and any suite that is skipped by default.
G12 Release-readiness items for publishing the project (versioning/changelog/license/readme claims,
    secret hygiene, dependency advisories) — discover, do not assume.
```

Explicitly NOT to reopen (permanent Cooperator decisions):

```text
N1  Stripe — rejected for this product direction.
N2  LM Studio and Vercel AI Gateway — historical rejection/removal, not unfinished routing.
N3  Host systemd + host nginx deployment — superseded by the published Docker Compose topology.
```

Explicitly deferred Cooperator phases (place them AFTER this effort; do not fold in):

```text
D1  UI/UX polish and mobile polish, including the accessibility-pin decision from R2 where it
    belongs to product UX.
D2  Real-VPS public deployment (INFOSEC R5 host hardening + live acceptance) — see T5.
```

## 4. Your first action — generate the Planner Worker prompt

Before anything else, after restoring state and emitting the SELECTION ECHO for `release-readiness-triage`, author one complete authoritative Planner Worker prompt. The Cooperator will deliver it manually and return the report manually.

Required prompt properties (finalize exact values yourself and field-check the result):

```text
Logical whole identity: release-readiness-triage
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Implementation-Planning Worker (repository-grounded discovery and planning)
Phase: Discovery
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded inventory and logical-whole decomposition of all remaining
  unfinished/parked/frozen/deferred/accepted-defect/known-gap work, prioritized and sequenced, ending
  before UI/UX polish and VPS deployment
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

Also include, with concrete values, the initial Planning Record fields, the exact repository gate at `996d9c7` (branch `main`, `HEAD == origin/main`, AP pin equality, clean tree), read-only authority, no network, no secrets, the mandatory reading list, the complete seeded inventory from section 3 as an explicit "verify and widen; do not trust" list, the required deliverable structure below, and the terminal report contract with the three echoed coordinates.

Mandatory reading for the Planner:

```text
- AGENTS.md; .ap/AP.md; .ap/AP_ORCHESTRATOR.md; .ap/AP_WORKER.md; .ap/PROMPT_CONTRACTS.md;
  .ap/INFOSEC.md; .ap/ARTIFACT_LIFECYCLE.md; /home/agile/meta/README.md
- Meta closure records and reports: 17/00-public-docs-and-stale-truth/99_closure.md;
  18/00-dockerized-vps-deployment/99_closure.md and all 18/00 reports named in the closure;
  18/00-dockerized-vps-deployment/90_live-host-deployment-handout.md
- /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md and DEFECT_LEDGER.md
- libretiles_PRD.md; docs/architecture.md; docs/vps_deployment_guide.md; README.md; CONTRIBUTING.md;
  frontend/README.md; AGENTS.md "Not done yet"
- the live tree itself (code, tests, scripts, assets) as the final authority
```

Planner deliverable structure (require exactly this, plus the AP terminal report wrapper):

```text
1. Verified open-item inventory: item, evidence (path/line/command), current status
   (open | already-closed | unknown), owner-if-known, affected surface, severity/impact.
2. Rejected false positives: items from the seed list or prose that are already complete, with the
   evidence that disproves them.
3. Logical-whole decomposition: for each proposed whole — kebab-case identity, one-paragraph
   objective, in-scope and out-of-scope paths/surfaces, evidence basis, suggested slices, required
   independence/INFOSEC route, dependencies, acceptance evidence, and material Cooperator decisions.
4. Priority buckets and recommended sequence: (A) release blockers; (B) pre-release quality/testing;
   (C) hygiene/tech debt; (D) post-release operations; with explicit dependency ordering.
5. Deferred phases: how UI/UX polish (D1) and VPS deployment (D2) sit after the recommended
   sequence, and what each depends on from the earlier wholes.
6. Unknowns needing one bounded evidence probe each, with the exact probe and decision it unlocks.
7. Recommended first successor whole and why.
```

Field-check the Planner prompt with the exact tool from T8 and require zero defects before writing it to:

```text
/home/agile/meta/projects/libretiles/19/00-release-readiness-triage/01_planning_00.md
```

Then present to the Cooperator the exact prompt (or its path) for manual delivery to the new Planner session, with native planning mode enabled. Wait for the returned report; do not dispatch Workers yourself for this first exchange.

## 5. After the Planner report returns — reconcile, decide, then run autonomously

1. Archive the returned report at `19/00-release-readiness-triage/01_report_00.md`, echoing the same coordinates. Verify the pair naming per the Meta contract.
2. Reconcile the plan against repository evidence. Reject invented scope, unverified claims, and false positives. If the plan is incomplete on a material axis, you may issue exactly one targeted-revision prompt per the AP finite-convergence rules; otherwise accept, revise, or reject with a concrete reason.
3. Present the Cooperator a compact, costed decision package: the proposed successor wholes, priority order, the first one to execute, and any Cooperator-owned choices. Terse replies (`A`, `ano`, `ok`, `Pokracuj`) continue the selected scope and never select a new whole.
4. On approval, close `release-readiness-triage` with a closure record at `19/00-release-readiness-triage/99_closure.md` (closure only after the plan is accepted and successors are named), then execute the successor wholes in order.
5. For each successor whole:
   - create its own Meta directory `19/NN-<identity>/`;
   - issue complete AP Worker prompts with `Native planning mode: not-used` (unless a genuine planning decision remains), exact baselines, allowlists, boundaries, and evidence tiers;
   - archive each prompt/report pair under the Meta naming contract;
   - use independent acceptance/audit and correction separation as INFOSEC requires;
   - run the standing gates and, for any deployment-artifact correction, the exact disposable Docker validator;
   - close it with its own `99_closure.md` and reconcile the ledger.
6. Report to the Cooperator at implementation grants, acceptance verdicts, publication, each closure, and any material risk/decision. Do not ask for micro-approval of deterministic steps inside an approved envelope.

Autonomy granted by the Cooperator: from exchange 2 of the triage whole onward, you may dispatch Workers natively as subagents. Every dispatch must still be a complete authoritative AP prompt; one accountable Worker per task; no hidden delegation; evidence stays non-independent where it is; and every prompt/report pair is archived.

## 6. Meta archival contract (exact)

```text
Archive root: /home/agile/meta
Layout: projects/libretiles/<archive-sequence>/<whole-sequence>-<logical-whole-identity>/
  archive-sequence: two-digit; the next available group is 19.
  whole-sequence: two-digit within that group; this effort starts at 00-release-readiness-triage.
Prompt/report grammar: <session>_<phase>_<exchange-index>.md and <session>_report_<exchange-index>.md
  where session is the two-digit AP Worker-session ordinal, exchange-index is zero-based
  (exchange ordinal minus 1; unsuffixed means exchange 01; `_01` is invalid), and phase is lowercase
  kebab-case, never `report`, `interruption`, or `handout`.
Reserved: 00_handout.md (this file); 99_closure.md (closure record).
Pairing intent: archive prompt and report together once the report exists; if the Meta archive is
  committed under Cooperator authority, each pair shares its first-add commit.
Do not guess filenames, do not scan for undeclared ledgers, and do not rewrite historical artifacts.
Prompts and reports remain exact historical evidence; path normalization does not rewrite contents.
```

## 7. Standing quality gates and tooling

```text
Backend (from /home/agile/Projects/libretiles/backend, RF-16 env-cleared route):
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
Frontend (from /home/agile/Projects/libretiles/frontend):
  npm run typecheck
  npm run lint
  npm run build
Deployment-artifact changes additionally require:
  ./scripts/validate_docker_deployment.sh
Prompt structural check before every dispatch:
  python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>
Never ambient python/python3/poetry run. Never PYTHON_DOTENV_DISABLED=1.
Known baseline failures to carry, not fix blindly: R1–R3 above.
```

## 8. Security and authority posture

```text
- No live host, SSH, firewall, DNS, real ACME, registry publication, or production action without an
  explicit Cooperator host grant (the R5 handout T5 covers that phase).
- No real secrets, dotenv values, credentials, accounts, or user data in prompts, reports, tests,
  logs, or archives. Synthetic fixtures only.
- Provider calls, catalog sync, and diagnostic targets need explicit authority and accounting.
- INFOSEC routing per task: R0–R2 for ordinary reversible slices; R3 for dependency/auth/provider/
  file-boundary touches; R4 at milestone gates; R5 for the later host deployment; R6 for corrections.
  Auditors never correct; correctors never self-certify.
- The published commit is accepted and closed. Reopening it requires a new, bounded correction with
  its own acceptance route; do not silently "improve" it during triage or successor work.
```

## 9. Explicitly out of scope for this effort

```text
- UI/UX polish (Cooperator's separate next phase; only place dependencies and prerequisites).
- Real-VPS deployment, certificates, DNS, monitoring installation (T5 handout; separate host grant).
- Reopening N1–N3 permanent decisions.
- AP upgrades; any AP pin change is a separate explicit task.
- Rewriting or "cleaning" historical Meta artifacts.
```

## 10. Your exact first bounded step (do this now)

```text
1. Restore read-only: verify T1–T2, read the required AP and Meta documents, and re-measure the
   seeded inventory R1–R5, L1–L4, G1–G12 against the live tree.
2. Emit the one-line SELECTION ECHO for `release-readiness-triage` and present the Cooperator the
   immediate plan (generate the Planner prompt, manual delivery, report return).
3. Create and field-check the complete Planner Worker prompt exactly as specified in section 4.
4. Write it to /home/agile/meta/projects/libretiles/19/00-release-readiness-triage/01_planning_00.md
   and hand it to the Cooperator for manual delivery with native planning mode enabled.
5. Stop and wait for the returned report. Do not begin any successor work before the plan is
   reconciled and the Cooperator approves the first successor whole.
```

---

## Restoration Readiness Review

```text
Restoration Classification: PASS (forward-horizon Orchestrator seed with explicit Cooperator instruction)
Contradiction review: clean — seeds a new effort after whole 18; does not contradict closed records.
Omission review: clean — D-13 fields, Cooperator intent, seeded inventory, Planner contract,
  autonomy rules, Meta archival contract, gates, INFOSEC posture, and deferred phases are present.
Stale-state review: honest — seeded inventory is hypothesis; live host state is unmeasured; closure
  records are the anchor and the live tree is the final authority.
Authority review: clean — the handout frames the effort and authorizes autonomous Orchestration from
  exchange 2 onward, but every action still requires a complete authoritative Worker prompt; no
  host, credential, or production authority is granted.
Active-mutation review: clean — repository tree clean at 996d9c7; Meta 18/19 artifacts are the
  archive projection and remain uncommitted unless the Cooperator authorizes a Meta commit.
Active-Worker review: clean — no Worker active; the first Planner session is yet to be dispatched.
Security-boundary review: clean — no secret, no live host, no public exposure.
Strategic-direction review: clean — triage and completion before UI/UX polish and VPS deployment.
Next-step executability review: clean — step 1 re-measures; the Planner prompt is fully specified.
```
