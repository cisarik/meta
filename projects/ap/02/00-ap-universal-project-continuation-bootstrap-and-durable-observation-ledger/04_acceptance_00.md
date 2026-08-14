# Fresh Worker 4 — independent acceptance of AP continuation bootstrap and durable observation-ledger storage

Use this text as the **sole authoritative Worker prompt**. Do not prepend the
implementation prompt, either Planner artifact, prior reports, the original
handout, or any Meta trace. They are claims or history, not acceptance
authority. Accept or reject the exact candidate from its Git objects and its
committed content.

## 1. Coordinate, route, authority, and independence record

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Task phase: Acceptance
Acceptance authority: explicit-read-only
Independence required: yes
```

```text
Acceptance candidate: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Acceptance owner map: AP.md sole semantic owner under ADR-0013; PROMPT_CONTRACTS.md exact structural owner; role/lifecycle/integration documents operational projections; README/FAQ/GLOSSARY explanatory; ADR/CHANGELOG historical
Acceptance allowlist: AP.md; PROMPT_CONTRACTS.md; AP_ORCHESTRATOR.md; PROMPT_ENGINEERING_PATTERNS.md; ARTIFACT_LIFECYCLE.md; INTEGRATION.md; README.md; FAQ.md; GLOSSARY.md; CHANGELOG.md; docs/adr/README.md; docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
Acceptance risk claims: semantic-owner integrity; cold-start discoverability; two-stage authority separation; optional-ledger storage/discovery correctness; absence/malformed/stale fail-closed behavior; report-repair non-authority; backward compatibility
Acceptance control matrix: exact Git identity; exact path set; positive semantic scenarios; negative authority scenarios; structural spelling consistency; link/fence/path integrity; unchanged executable/schema/managed-block/consumer surfaces
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

- Worker session profile: Fresh Independent Acceptance Worker.
- Evidence tier: E2 repository-grounded independent documentation acceptance.
- Reasoning recommendation: High, advisory only. Do not encode a model,
  provider, client, or IDE into the result.
- Internal delegation: prohibited. One fresh accountable Worker performs the
  complete acceptance.
- Evidence posture: independent. Do not contact, reuse, or continue Worker 3.
- Native planning mode is off. Do not produce another plan or modify the
  client-native planner surface.
- This grant authorizes credential-free public-ref reads, read-only repository
  and Git-object inspection, and disposable uncommitted validation material
  under `/tmp` only. It grants no source, index, branch, worktree, configuration,
  remote-ref, AP, FrameNest, Meta, account, service, or external mutation.
- No correction is authorized. A defect produces evidence for a later separate
  correction prompt; do not edit the candidate.

## 2. Exact candidate and hard gates

The implementation claim to verify independently is:

```text
Candidate: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Parent: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Tree: 7b53c74b7bfa183e490a0d81581a9f3db45c99d3
Subject: docs: define continuation bootstrap and observation ledgers
Branch: feat/universal-continuation-observation-ledger
Candidate worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w3
Owner repository: /home/agile/Projects/ap
```

The ORCHESTRATOR reverified these credential-free public refs immediately
before issuing this prompt:

```text
AP public refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

FrameNest public refs/heads/main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

FrameNest .ap gitlink at that commit:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before substantive review, independently prove:

1. `/home/agile/Projects/ap` is the intended AP owner repository and resolves
   to the canonical public AP repository.
2. Credential-free AP `refs/heads/main` still equals `041de310...`.
3. Credential-free FrameNest `refs/heads/main` still equals `230ce43a...`.
4. The candidate object exists locally, is a commit, has exactly the stated
   parent, tree, and subject, and is not a merge.
5. The candidate worktree is at the exact candidate and clean before review.
6. Commit-bound FrameNest inspection, without reading or changing its live
   worktree, confirms the `.ap` gitlink claimed above.
7. The candidate is not already present at public AP `main`; publication has
   not occurred.

If a public hard gate differs, stop with terminal `BLOCKED` and
`Report justification: changed-external-state`. If the local candidate identity,
cleanliness, ancestry, or repository identity differs, stop with `BLOCKED` and
the canonical justification supported by the evidence. Do not repair or
normalize anything.

Meta is outside this acceptance boundary. Do not inspect or mutate it, and do
not use its current ref as a gate. The implementation report is also not a
substitute for direct evidence.

## 3. Acceptance objective

Determine whether exact candidate `a1b04ffc...` is safe to publish unchanged as
one coherent AP documentation change.

Acceptance PASS requires proving all of the following:

1. `AP.md` remains the sole live semantic owner.
2. A fresh Orchestrator can discover a named Continuation Bootstrap through the
   existing required-reading path without `CONTINUATION.md` or a managed-block
   change.
3. Continuation separates read-only restoration/reconciliation from the later
   COOPERATOR selection of exactly one bounded logical whole and from any
   subsequent mutation authority.
4. Optional durable upgrade-ledger storage is consumer-owned,
   explicitly declared, one Markdown file per canonical target, and always
   non-authorizing.
5. Declaration, header, entry, staleness, absence, malformed, conflict,
   reconciliation, retention, and privacy behavior have one exact structural
   owner and consistent projections.
6. A client-native planner artifact without a separate standard terminal report
   cannot be treated as PASS or execution authority, while the bounded
   same-session report repair remains finite and non-authorizing.
7. Existing consumers remain compatible until an explicit pin update and
   optional consumer adoption.
8. The candidate changes exactly its declared documentation boundary and no
   executable, schema, managed-block, test, AP_WORKER, FrameNest, or Meta
   surface.

Do not evaluate whether a different architecture would be preferable in the
abstract. Falsify the candidate against current AP invariants and the fixed
acceptance controls below.

## 4. Exact diff and artifact-boundary controls

Compare the exact candidate directly with parent `041de310...`.

The changed path set must be **exactly** these 12 paths:

```text
AP.md
PROMPT_CONTRACTS.md
AP_ORCHESTRATOR.md
PROMPT_ENGINEERING_PATTERNS.md
ARTIFACT_LIFECYCLE.md
INTEGRATION.md
README.md
FAQ.md
GLOSSARY.md
CHANGELOG.md
docs/adr/README.md
docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
```

Required negative controls:

- ADR-0016 is the only added file; there are no deletions or renames.
- `AP_WORKER.md`, `ap`, `ap.project.conf`, `UPDATING.md`, `INFOSEC.md`, tests,
  fixtures, CI, dependencies, and all existing ADR bodies are byte-identical to
  the parent.
- The AP-managed consumer `AGENTS.md` block generated by `ap` is byte-identical.
- There is no new `CONTINUATION.md`, ledger template, example consumer ledger,
  schema file, parser, validator, CLI command, doctor rule, or conformance test.
- No FrameNest or Meta content is part of the candidate.
- The candidate contains no merge, fixup, unrelated cleanup, generated debris,
  temporary validation script, or private path/host/media detail.

Run and report bounded Git-object evidence for modes, additions, deletions,
path set, parent, tree, and subject. Run the exact two-commit equivalent of
`git diff --check <parent> <candidate>`. Do not alter the index or worktree.

## 5. Semantic-owner and projection acceptance

Read the complete candidate versions of all 12 changed files and the directly
linked unchanged owner sections needed to interpret them. Do not assess only
diff snippets.

Prove:

1. `AP.md` owns every new semantic statement: two-stage continuation,
   declaration/storage meaning, authority/staleness/absence behavior, and the
   planner-artifact/report-completion rule.
2. `PROMPT_CONTRACTS.md` owns exact field names, allowed values, record shapes,
   and repair structure without becoming a second semantic protocol.
3. `AP_ORCHESTRATOR.md`, `ARTIFACT_LIFECYCLE.md`, `INTEGRATION.md`, and P11 are
   operational/advisory projections that point back to the semantic owner.
4. README, FAQ, and GLOSSARY explain and link; they do not silently add stronger
   requirements, additional discovery behavior, or different enum values.
5. CHANGELOG and ADR-0016 are historical records, do not claim acceptance,
   publication, FrameNest adoption, or closure, and do not become live owners.
6. ADR-0016's status and index relationship match the repository's current ADR
   lifecycle conventions for an unaccepted local candidate.
7. No new RF family or duplicate lifecycle owner was created.

Any semantic rule that exists only in a projection, any conflicting owner, or
any exact field with multiple structural owners is material and forbids PASS.

## 6. Continuation-bootstrap falsification scenarios

Trace each scenario from the committed candidate. Record PASS or a concrete
failure with exact source locations.

### C1 — Minimal seed, no prior conversation

Starting only from the candidate's non-normative minimal seed and a hypothetical
AP-integrated consumer root `AGENTS.md`, prove that a fresh Orchestrator is
directed through the unchanged managed block to the pinned AP documents and can
discover the named Continuation Bootstrap in `AP_ORCHESTRATOR.md`.

It must not require:

- an outgoing Orchestrator;
- a handcrafted restoration handout;
- Meta or another external trace;
- private/conversational memory;
- a vendor, model, client, IDE, or emoji convention; or
- a new AP file or managed-block pointer.

### C2 — Stage separation

Prove Stage 1 is read-only restoration and reconciliation, while Stage 2 obtains
the COOPERATOR's explicit selection of exactly one bounded logical whole. No
mutation authority exists until a later complete current Worker prompt is
issued.

The algorithm must restore governing pin, repository/external truth, durable
decisions, optional trace, and tentative narrative in the correct precedence
without treating a stale proposed next step as current authority.

### C3 — Missing outgoing Orchestrator and stale handout

Prove ordinary continuation still works when no outgoing Orchestrator or handout
is available. If an old handout exists, it remains subordinate evidence and
cannot freeze the next whole across a pause.

### C4 — Discovery terminates

Prove the discovery path is finite:

```text
minimal seed -> root AGENTS.md -> pinned AP_ORCHESTRATOR.md -> read-only restore
-> declared ledger reconciliation if any -> COOPERATOR selects one whole
-> separate complete Worker prompt
```

There must be no cyclic requirement to create or read a continuation file before
the bootstrap can be found.

## 7. Ledger-storage falsification scenarios

### L1 — No declaration

Prove a consumer with no ledger declaration remains valid and follows existing
canonical sources and COOPERATOR reconciliation. Absence must mean that no
AP-contracted durable ledger storage is activated, **not** that every possible
observation in the universe is resolved.

### L2 — Valid empty declared ledger

From the exact declaration and header grammar, prove a committed declared file
with a valid header and no entry records means zero active ledger entries for
that one declared target.

### L3 — Explicit discovery only

Prove the root project-owned `AGENTS.md` declaration sits outside the unchanged
managed block, uses one target-to-one-path mapping, and is the only discovery
mechanism. An undeclared lookalike file must remain ordinary project content.
There is no mandatory filename or tree scan.

### L4 — Canonical identity portability

Prove the contract reuses the exact canonical repository identity already
accepted by project rules and repeats it byte-for-byte in declaration and file
header. It must not impose GitHub, `owner/name`, a display name, a local path,
or another new universal canonicalization algorithm.

### L5 — Path containment and collision

Prove the declared path is normalized, repository-relative Markdown, has no
`..`, remains inside the consumer repository without symlink escape, and cannot
collide with another target or declaration. Duplicate target/path/id and
conflict-marker behavior must fail closed.

### L6 — Exact record and lifecycle

Prove the file header and 14-field entry record occur in the structural owner
with exact allowed values. RF-09 must still own the seven lifecycle states and
transitions. Entry identity is stable, opaque, public-safe, non-ordinal, unique
within the ledger, and has no invented AP-wide regex.

### L7 — Accepted but unauthorized

Trace an `accepted` observation whose old `Implementation task grant` names an
expired Worker boundary. It must remain non-authorizing; neither `accepted`,
the stored grant, nor `Implementation status: authorized` can resume mutation
authority after report/session expiry.

### L8 — Stale or unknown evidence

Trace active entries with `Last revalidated against: none` and with
`Observed against: unknown because <reason>`. They may be preserved as
non-authoritative candidates, but Stage 2 cannot rely on them for mutation
until current truth revalidates them.

### L9 — Repository contradiction

Prove current repository/durable truth outranks the ledger. A contradicted entry
moves to `invalidated` with disposition evidence; the ledger cannot override
the repository.

### L10 — Malformed declared storage

Trace a declared missing file, empty file without the required header,
target/version mismatch, unknown version, duplicate declaration/id, invalid
record, and conflict markers. Read-only restoration may gather evidence, but
ledger reconciliation cannot be claimed complete and mutation relying on it
must stop for a bounded COOPERATOR reconciliation/repair decision.

### L11 — Terminal reconciliation

Prove terminal entries leave the live ledger only after immutable historical
evidence is named. Git history and the promoted durable owner preserve
provenance; no second growing archive file is created. Active states remain
active and ordering never becomes identity.

### L12 — Scope and privacy

Prove the ledger cannot become a roadmap, issue tracker, NEXT/session-state
file, Worker registry, transcript, specification, ADR, or second protocol.
Check public-safe exclusions for secrets, credentials, private paths/media,
full transcripts, hidden reasoning, and unnecessary production detail.

## 8. Planner-artifact/report-repair falsification scenarios

### R1 — Artifact alone

Prove a client-native planner artifact without AP's separately required
standard terminal Worker report is structurally incomplete and cannot be
classified as planning PASS.

### R2 — Bounded same-session repair

Prove the ORCHESTRATOR may issue only a complete next-exchange,
report-rendering-only repair to the same healthy session, with:

- the next exchange ordinal;
- `Native planning mode: not-used`;
- the frozen artifact as continuity anchor; and
- explicit prohibitions on re-planning, implementation, mutation, acceptance,
  publication, and closure.

The repair must render the missing report prospectively without overwriting the
earlier exchange, changing the plan, consuming another planning cycle, or
granting execution authority.

### R3 — Mode is not authority

Prove `Native planning mode: not-used` remains only a client-mode routing fact.
Implementation still requires a separate complete Implementation Authority
Record. No new status, phase result, report justification, filename convention,
role, or lifecycle may have been invented.

### R4 — Existing Worker contract remains sufficient

Prove leaving `AP_WORKER.md` unchanged creates no missing obligation: its
existing terminal-report and authority-expiry rules already cover the Worker,
while the new completion branch belongs to the semantic, structural,
Orchestrator, and P11 projections.

## 9. Cross-projection and documentation validation

Perform proportional documentation-first validation under ADR-0015:

1. verify every relative Markdown link and local path in all 12 changed files;
2. verify every referenced heading/anchor exists in the candidate;
3. verify fenced code blocks are balanced;
4. compare every new field name and allowed value against
   `PROMPT_CONTRACTS.md` and detect spelling/order/value drift;
5. verify each declaration/header/entry fixture has one canonical structural
   definition and projections use links or compact exact references;
6. search for accidental validation of `planning-PASS`, `planning-PARTIAL`,
   `planning-BLOCKED`, `no-new-material`, `invariant-failure`, or
   `public-ref-mutation`; quoted historical rejection is allowed only when it
   cannot be mistaken for a valid value;
7. check artifact-relationship labels and owner links across AP, role,
   lifecycle, integration, explanatory, changelog, and ADR projections;
8. verify ADR-0016 filename, number, title, status, index row, and relationship;
9. verify compatibility claims do not imply that unpublished AP governs the
   currently pinned FrameNest consumer; and
10. verify no text claims executable enforcement, conformance testing,
    FrameNest adoption, public acceptance, publication, or closure.

A small read-only validation script may be created only under `/tmp`, must not
touch either repository, must be reported, and must be removed before the
terminal report. Do not install dependencies or create/rebuild a virtual
environment. Do not run or recreate the retired monolithic AP suite.

## 10. Acceptance decision rules

Return `PASS` only when every positive scenario and negative control above is
proved from the exact candidate and no material contradiction remains.

Return `PARTIAL` when the candidate is useful but one material claim lacks
evidence or one bounded correction is required before publication.

Return `BLOCKED` when a hard gate differs, candidate identity is invalid,
independence is compromised, or the candidate cannot be safely assessed without
new authority.

Any defect affecting a semantic owner, authority/routing/convergence rule,
exact structural field, compatibility boundary, or privacy/fail-closed behavior
requires a separate correction followed by **full fresh re-acceptance**. Do not
recommend scoped re-acceptance for such defects.

Do not mark stylistic preference as a material defect. Do record genuinely
adjacent protocol observations as non-authorizing ledger candidates without
expanding this whole.

## 11. Explicit prohibitions

- No source, index, worktree, branch, ref, configuration, dependency, host,
  account, service, provider, or external mutation.
- No edits, formatting, automatic fixes, commits, amendments, merges, rebases,
  cherry-picks, tags, fetches, pushes, releases, pull requests, or issues.
- No publication, FrameNest pin update, ledger adoption, deployment, production
  acceptance, Meta archival, or logical-whole closure.
- No use of prior Planner conclusions as proof.
- No consultation with Worker 3 and no same-session correction.
- No Worker 5/publication prompt generation.
- No model/provider/client/IDE requirement.
- No secret, credential, private path/media, transcript, or hidden-reasoning
  disclosure.

Leave the retained candidate branch and worktree unchanged for the later
publication Worker. Clean only disposable acceptance material created under
`/tmp`.

## 12. Mandatory terminal report

Return exactly one standard terminal report in the same response as the end of
acceptance. It must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Its metadata must contain exactly one occurrence of:

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 04
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: acceptance-PASS | not-applicable
Result artifact or commit: a1b04ffcebda197bfe25c4258d9e6d96328d36b1 | not-applicable
Result evidence: <bounded independent evidence>
Logical-whole closure: not-closed
Report justification: final-acceptance | new-evidence | new-material-risk | changed-external-state
Authority expiry: all Worker 4 acceptance authority expired at this terminal report
```

Render one actual value, never the literal alternatives. Use
`Phase-qualified result: acceptance-PASS`, the exact candidate identity, and
`Report justification: final-acceptance` only with terminal `PASS`. Use
`not-applicable` for a terminal `PARTIAL` or `BLOCKED` and select the one
canonical justification actually supported.

The report must include:

1. fresh-session, independence, native-mode, capability, delegation, evidence,
   and authority confirmation;
2. AP/FrameNest public gates and exact candidate identity/ancestry/tree/subject/
   cleanliness evidence;
3. exact changed-path and unchanged-surface controls;
4. a numbered C1-C4, L1-L12, and R1-R4 acceptance matrix with PASS or exact
   defect evidence;
5. semantic-owner/projection verdict;
6. structural-field and cross-projection verdict;
7. link, anchor, path, fence, whitespace, privacy, and compatibility results;
8. commands or probes summarized with full output only for failure or unexpected
   state;
9. deviations, risks, missing evidence, and non-authorizing out-of-scope ledger
   candidates;
10. `Resolved Execution Issues / Near-Misses: none` or a complete bounded
    record;
11. `Pre-Existing Failure Classification: none` or a complete applicable
    classification;
12. temporary material and cleanup evidence;
13. explicit confirmation that no mutation or push occurred; and
14. one smallest next step: publication of the exact accepted candidate if PASS,
    otherwise the smallest separate correction or decision required.

Do not substitute an acceptance plan, progress summary, client-native artifact,
or informal review for the terminal report. Stop autonomous work immediately
after it; all Worker 4 authority expires regardless of context health.
