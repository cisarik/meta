# Kronika one product — S4-D: durable documentation of modular research and the administrator-curated timeline

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 26
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S4-D-SUPERSEDING-DOCUMENTATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: a documentation slice that supersedes part of the accepted architecture and records a deliberate administrator-access change, requiring an exact contradiction review; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository baseline from Step 0 before mutation.
The plan and decisions below are input; verify the named sources yourself.
Documentation only: no code, tests, schema, configuration, AP, host or
provider action. No subagents.

## Current Cooperator decisions to record (authority for this slice)

These are the current strategic authority. They were made by the Cooperator
during the modular-provider planning exchange and supersede conflicting
earlier wording.

1. Kronika keeps MEME and Movie and adds Search and Research through a
   **modular, provider-neutral application boundary**; chatgpt.com capture
   remains one currently parked module.
2. The first provider is the **OpenAI Responses API with a fixed model
   configuration** (`gpt-5.5-2026-04-23`), native provider-managed research,
   no automatic fallback. FrameNest supervises the lifecycle.
3. **Personal history**: Kronika stores questions and their answers, including
   complete Research reports.
4. **Administrator access**: an authenticated application administrator can
   read all product records, including private and unfinished work. This
   supersedes the earlier "administrator status alone never permits reading
   another owner's private content" wording. Administrator access concerns
   application content only; it grants no access to provider secrets, browser
   credentials or host administration.
5. **Shared publication**: administrators approve completed question/answer
   records and successfully analyzed media for the shared page. Owners do not
   publish directly to that page.
6. **Main page**: the Timeline contains only administrator-approved records;
   personal history is a separate view; Gallery remains a working view.
7. **Audience**: the shared page is for verified household members only;
   internet publication remains disabled.
8. **Budget**: application thresholds Search USD 0.50, Research USD 5, daily
   USD 10, monthly USD 30; a provider monthly hard limit of USD 30; delayed
   enforcement and possible overshoot were explicitly accepted.
9. **External retention**: the standard provider retention, including possible
   security retention after deletion of the retrieved response, was accepted;
   ZDR is not required.
10. The end goal remains transforming FrameNest into public Kronika (S10).

## Verified starting state (verified read-only at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd` (parent
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`); clean index and worktree;
  local `main` = `origin/main` = public `refs/heads/main` = `fd277a9…`;
  AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- No `docs/adr/0083-…` file exists; the current migration head is `0033`.
- The accepted planning input is the session-delivered Planner report
  (session 25 / exchange 01, status PASS); its architecture and revised slice
  order are accepted by the Orchestrator. The capture host remains parked; no
  host action is authorized.
- `private/**` is never read. Do not print host values, private network
  values, credentials or Meta paths in repository documents.

## Goal

Record the revised architecture and the decisions above in the durable
document owners; mark ADR-0082 as partially superseded with an exact link and
retained-history explanation; perform the contradiction search; create one
documentation commit. Nothing executable changes.

## Exact mutation allowlist

```text
AGENTS.md
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SERVER.md
SECURITY.md
DEVELOPMENT.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/adr/README.md
docs/adr/0082-kronika-one-product-and-private-records.md
docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md
```

## Required documentation content

| Owner document | Required update |
|---|---|
| ADR-0083 (new) | Provider-neutral research boundary and placement; native execution of the model/search loop at the provider with local supervision; selected first provider and fixed configuration; application budgets and accepted enforcement/retention limitations; question/answer history; administrator read-all and administrator-curated household publication; shared-only Timeline and separate personal history. |
| ADR-0082 | Partial-supersession notice with an exact link to ADR-0083 for capture-only research, owner-only private reading, direct owner sharing and completion-triggered Timeline entry; preserve the historical reasoning. |
| ROADMAP | Revised rows and order S4-D → S4-A → S6 → S4-B → S7-P → S8 → S9 → S10; parked capture work (S3 host remainder, capture-mode S4, S5 ZIP activation, S7-C) and the separate acceptance/host grants. |
| PRODUCT | Personal question/answer history; shared-only Timeline with administrator approval; administrator access; household-only publication; capture parked. |
| SPEC | Research/provider contracts and resource limits; ownership and administrator approval; completion and error rules; no automatic fallback; safe rendering. |
| SERVER | Local supervisory runtime versus hosted research loop; configuration and credential boundaries; no second server or deployment system. |
| SECURITY | Revised administrator privilege; permitted text egress only; untrusted output; spend controls; retention and audit routes. This is a deliberate Cooperator-owned change: replace the conflicting current sentences and keep the exact supersession trace in ADR-0082/ADR-0083. |
| AGENTS.md | Project-specific product/security guidance matching the new decisions, outside the managed AP block; the managed block stays byte-identical. |
| README | Accepted target versus implemented state, with capture explicitly parked. |
| DEVELOPMENT.md | Fake-provider route, disabled-by-default research configuration, declared test commands. |
| docs/UBUNTU_NUC_DEPLOYMENT.md | Future credential-provisioning and native-provider gates; preserve the existing release helper and the parked capture state. |
| docs/adr/README.md | Add ADR-0083 and its partial-supersession relationship to ADR-0082. |

## Required contradiction search

Search all current authoritative repository wording for: capture-only
Search/Research providers; excluded external providers; the
administrator-private-content denial; owner direct sharing; Timeline entry on
completion; obsolete S3/S5 dependencies. Classify each occurrence as current
normative text (update), historical rationale (preserve with link), or
irrelevant. Known starting conflicts to resolve or explicitly preserve:
`AGENTS.md` administrator-privacy sentence, `PRODUCT.md` Timeline/Search
wording, `ROADMAP.md` S8 wording, and the capture-only provider passages in
`SPEC.md`/`SERVER.md`/`SECURITY.md`. Do not rewrite historical ADRs or history.

## Step 0 — preconditions (fail closed)

- Verify physical root, branch, HEAD, parent, clean index and worktree, local
  `main` = `origin/main` = `fd277a9…`, public `refs/heads/main` via
  `git ls-remote`, and the AP pin `7478ddb0…` (gitlink and `.ap` HEAD).
- Confirm `docs/adr/0083-…` is absent and the migration head is still `0033`.
- Classify any divergence with RF-12; stop on unexplained remainder.

## Declared execution route

From the repository root with the exact baseline:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline fd277a9a64a6965df76127dbec5b1735d2fb3cdd

./.ap/ap exec --root /home/agile/Projects/framenest --baseline fd277a9a64a6965df76127dbec5b1735d2fb3cdd --operation test-focus -- tests/contract/test_nuc_release_docs.py -q -p no:cacheprovider
```

JavaScript tests: not-used — no JavaScript change. No new tests are required
for this documentation slice; use direct semantic and link review plus the
contradiction search. No ambient Python or environment reconstruction.

## Git and commit rules

Stage only the twelve allowlisted paths after reviewing the complete diff.
Inspect `git diff --cached --name-only`, `git diff --cached --check` and the
full staged diff. Verify the `.ap` gitlink, managed AP block and
`docs/AP_UPGRADE_OBSERVATIONS.md` are unchanged. Create exactly one local
commit:

```text
docs(kronika): define modular research and administrator-curated timeline
```

Do not push, fetch, tag, merge or rebase. Do not commit Meta artifacts. Public
documents stay public-safe: no private paths, trace text, host values or
credentials.

## Authority and containment

Positive authority: read-only repository inspection; edits to exactly the
twelve allowed paths; the declared route commands; one local commit; the
terminal report write at the exact destination below when absent; full
readback of the saved report.

Negative authority: no executable code, test, dependency, lockfile, schema,
migration, configuration, AP, packaging or ledger change; no source-Kronika
mutation; no host, SSH, gate, sudo, service, account, browser, credential or
provider action; no `private/**`; no push/publication/deployment; no
subagents; no ambient execution route.

## Stopping conditions

Stop and report on: baseline or topology drift; an unexpected existing
ADR-0083; an out-of-allowlist change; an unusable declared route; a failed
required validation; an unresolved normative contradiction that would require
rewriting history; sensitive evidence exposure; or any need for host/provider
activity. Do not repair unrelated failures.

## Validation

Validation ladder: selected.
Inspection and provenance: required — repository gate and exact diff.
Existing focused tests: `tests/contract/test_nuc_release_docs.py`.
Affected tests: the same contract plus direct documentation review.
New causal regression: none — documentation slice.
Broad or full suite: not-used.
Runtime or testbed: not-used.
Independent acceptance: not-required for the documentation slice; the later
S4-A/S6/S4-B code slices carry their own acceptance classes.

## Completion and report contract

`PASS` means the twelve-path documentation change is committed with the
declared route passing, the contradiction search reported, the AP pin and
managed block unchanged and the worktree clean. `PARTIAL`/`BLOCKED`
otherwise. Use `Phase-qualified result: implementation-PASS` for PASS,
otherwise `not-applicable`, and `Logical-whole closure: not-closed`.
`Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the exact
changed paths; a per-document summary of the recorded decisions; the
contradiction-search results with each conflict's disposition; the route
results; the commit SHA, parent, tree and subject; post-commit status; the
unchanged AP pin/managed block/ledger; deviations, risks and missing evidence;
one smallest next step (S4-A provider contracts and configuration); authority
expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; the short completion notice to the
Cooperator is in Slovak, masculine address. Finalize the report, save it at
the exact destination, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Do not run `sudo -v` or `sudo -K`. Terminal
report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 26_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 26_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
