# ContextDesk — reconcile durable M2/G4 documentation after the first physical slice

## Identity and one outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 17
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Documentation Implementation Worker — M2/G4 state reconciliation
Phase: implementation
Task identity: CONTEXTDESK-DOCS-RECONCILE-G4-SLICE
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E2
Evidence tier basis: public safety documentation and durable product-state reconciliation; no runtime behavior change
```

Use a fresh Worker session. Do not dispatch subagents. Worker 16's authority expired. Speak Slovak to the Cooperator; write repository documentation and the terminal report in English. Your one outcome is a narrow, public-safe documentation reconciliation after the verified deployment and the named physical acceptance slice. Do not change C++/QML/scripts/packaging, host state, AP, or META Git.

The exact code candidate remains `cb72ae0388307b514182efc6936712e3da42cda4`. Worker 14 established deployment-PASS for that candidate while inactive. Worker 16, after an independently demonstrated SSH recovery path, established `acceptance-PASS` for one named slice: explicit authenticated ARM, sampled G213 pass-through, matching-invocation 45-second cutoff death, and G213 typing after descriptor close. Full G4 remains open for watchdog/hang, held-modifier-at-death, LED return, all-control fidelity, and production/autostart readiness. Do not promote this slice to full G4 or closure.

This task exists because the durable product documents still describe the pre-install/pre-ARM state and one recovery sentence still says a second keyboard or SSH is optional. For any live G4 grab on this project, an independently verified second physical keyboard or SSH from another device is a mandatory safety precondition. A cutoff timer is additional evidence and is never a replacement for that path. Device-free S3 procedures may remain keyboard-free.

## Verified baseline and source routing

Canonical product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; expected starting `HEAD` and code candidate `cb72ae0388307b514182efc6936712e3da42cda4`. Required AP gitlink/checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` must pass.

META is historical evidence and remains Cooperator-owned for archival. The exact 14/15/16 prompt/report pairs are under `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`; public META currently contains Worker 16 report in commit `c06a4004ae06c9395c68c7919f331aab8b6be460` or a later ref verified at start. Read the exact reports, not conversation summaries. Their evidence is immutable history. Do not modify META.

Read applicable `AGENTS.md`, the pinned AP Worker/report contracts, and only the current versions of:

- `README.md`
- `ROADMAP.md`
- `AGENTS.md`
- `docs/operations.md`
- `docs/testing-m2.md`
- `docs/architecture.md`

Inspect `docs/specification.md` only if a concrete recovery/G4 contradiction is found there. `handout.md` is historical and must not be rewritten. Do not read or copy local host paths, event-node numbers, serials, raw input, credentials, or private network data into public documentation.

## Gates and authority

Before editing, verify repository root, remote, branch, exact starting HEAD, clean worktree apart from ignored build output, no active Git operation, `.ap` identity, and AP doctor. If the code candidate or AP pin differs, or unexplained user work is present, stop and report without editing. A read-only `git fetch origin main` is allowed if needed; do not reset, clean, stash, switch, rebase, amend, or discard work.

The changed-path allowlist is exactly:

```text
README.md
ROADMAP.md
AGENTS.md
docs/operations.md
docs/testing-m2.md
docs/architecture.md
```

No other product path may change. Do not update the pinned `.ap` submodule, generated build output, user profiles, host units, udev/ACL policy, service state, OpenRGB/KWin/input-remapper, or any product code. No physical trial is authorized. The report file under META is the sole explicit persistence exception described below; META Git operations remain forbidden.

## Required semantic reconciliation

Keep the current owners and public-document style. Make the smallest coherent edits that make these claims consistent everywhere they are stated:

1. **Current M2 status.** Planning and production implementation are complete enough for deployment. The exact candidate was installed and verified on the reference host while the broker remained inactive. One fresh-independent physical slice passed: external SSH recovery proof, explicit ARM, sampled pass-through, matching-invocation cutoff recovery, and post-death G213 typing. State the evidence scope without embedding private machine details or pretending that a documentation commit itself reran hardware acceptance.
2. **Full G4 remains open.** Explicitly retain open watchdog/hang recovery, held-modifier-at-death, LED-return behavior, all-control fidelity, input-remapper coexistence beyond the sampled trial, and production/autostart readiness as applicable to the current document. Do not write “G4 passed”, “production ready”, “safe to enable”, or “logical whole closed”. Keep the broker disabled/static and no-autostart rules visible.
3. **Recovery prerequisite.** In live G4/physical-grab procedures, say that a second physical keyboard or SSH from another device must be independently verified before the broker is started or ARM is attempted and must remain available through the trial. The cutoff helper is invocation-bound supplemental recovery evidence, not a substitute. Do not require both routes; either one is sufficient. Do not impose this requirement on device-free S3 tests.
4. **Deployment versus acceptance.** Preserve the distinction between repository packaging, host installation, deployment-PASS, named physical acceptance-PASS, full G4, production acceptance, and closure. A public document may point readers to the META trace directory and exact report identities, but must not include Cooperator local paths, passwords, addresses, serials, raw logs, or typed samples.
5. **Next route.** Replace stale “next unresolved work is a recovery-design decision before any live grab” language with a truthful bounded next route: the named slice is accepted, and a separately authorized fresh task remains for watchdog/hang, held-modifier-at-death, LED return/all-control fidelity, or an explicitly chosen documentation/decision step. Do not invent a new task queue or claim the next choice is already accepted.
6. **Historical integrity.** Do not rewrite `handout.md`, old reports, old prompts, or old commits. Do not relabel Worker 16's `acceptance-PASS` as full G4. Preserve historical statements that were true at their time when adding a clear current-state paragraph.

Use exact public-safe wording appropriate to each owner. `README.md` should remain concise and user-facing; `ROADMAP.md` remains the plan of record; `AGENTS.md` carries current execution constraints; operations/testing carry executable safety procedures; architecture carries stable boundaries. Do not copy a long report into all six files. If an old sentence is a procedure-specific contradiction, fix the sentence at its owner rather than adding a disclaimer elsewhere.

## Validation and Git

Because this is documentation-only, do not rerun CTest or any live operation. Run:

```sh
git diff --check
rg -n "G4|second keyboard|SSH|optional|cutoff|autostart|deployment-PASS|acceptance-PASS|not-closed" README.md ROADMAP.md AGENTS.md docs/operations.md docs/testing-m2.md docs/architecture.md
```

Review the complete diff for:

- no remaining statement that makes the independent recovery path optional for live G4;
- no claim that Worker 16 or a documentation commit closed full G4;
- no private host data, raw keyboard data, credentials, or unbounded transcript;
- no altered code, packaging, AP pin, or unrelated roadmap feature;
- no contradiction between `docs/operations.md`, `docs/testing-m2.md`, and `docs/architecture.md`;
- no accidental rewrite of historical handout/report language.

After review, create one ordinary local commit containing only the allowlisted documentation changes. Push that commit to `origin main` only if the starting baseline and diff remain exactly within this prompt; otherwise report the prepared diff and stop before publication. Record the full pushed commit and public branch readback. Do not modify META or push any META commit. A docs-only commit changes the product tree identity; state that prior physical evidence remains attributed to code candidate `cb72ae0` and that no runtime behavior was changed by this slice.

## Exact report persistence

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 17_implementation_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 17_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR for META; this WORKER may publish the allowlisted product documentation commit
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/17_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is exact report-file preparation only; no META add/commit/push. Verify the real destination, parents, symlinks, and collision. Preserve any existing/nonidentical report and never choose an alternate filename. If persistence fails, state it and provide the complete report as fallback; never claim saved bytes without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, contain one coordinate set echoing this prompt, status and `implementation-PASS` or `not-applicable`, exact starting/ending product commits, AP pin, changed-path diff, public push/readback result, validation commands and outcomes, Worker-versus-Cooperator evidence attribution, unchanged runtime/host statement, one smallest next step, exactly one report justification (`new-mutation` for the docs commit or `new-evidence` if no commit), compact `Orchestration critique` with `MEASURED`/`LEAD`, resolved/pre-existing issues, `Logical-whole closure: not-closed`, and authority expiry. Do not include private host details or raw input. Read the report back completely before notifying the Cooperator. The Cooperator archives this exact prompt/report pair after the report exists.
