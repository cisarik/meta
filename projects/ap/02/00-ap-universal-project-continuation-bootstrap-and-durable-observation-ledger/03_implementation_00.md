# Fresh Worker 3 — AP continuation bootstrap and durable observation-ledger implementation

Use this text as the **sole authoritative Worker prompt**. Do not prepend the
Planner artifacts, their reports, the prior handout, or any Meta trace. This
prompt already contains the ORCHESTRATOR's decision-complete convergence of the
two independent planning passes.

## 1. Coordinate, route, authority, and evidence record

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 03
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: AP 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Independence required: no
```

- Worker session profile: fresh implementation Worker.
- Task phase: Implementation.
- Evidence tier: E2 — repository-grounded implementation evidence, followed by
  a separately authorized fresh independent acceptance Worker.
- Recommended reasoning effort: High. The change touches the sole normative
  protocol and exact structural spellings, but no executable, schema, security,
  provider, deployment, or production surface.
- Internal delegation: prohibited. One accountable Worker performs this whole
  implementation slice.
- Native planning mode is **off**. Do not create another plan, do not enter a
  client-native planning surface, and do not reinterpret this prompt as
  planning authority. If the client forces planning mode or the task cannot be
  executed without materially replanning it, stop and report `BLOCKED`.
- This grant authorizes only the repository work, local branch/worktree, one
  local commit, validation, and terminal report specified below. It grants no
  publication, consumer update, Meta archival, acceptance, correction,
  deployment, production, or logical-whole closure authority.

## 2. Required outcome

Implement one coherent AP-documentation candidate that:

1. makes project continuation operationally discoverable through a named
   **Continuation Bootstrap** in the already-required
   `AP_ORCHESTRATOR.md`, without adding `CONTINUATION.md`;
2. defines a two-stage continuation rule: first restore and reconcile read-only,
   then select exactly one bounded next logical whole with the COOPERATOR before
   any mutation authority is issued;
3. adds an optional, consumer-owned, explicitly declared, durable storage
   projection for active `upgrade <canonical-repository>` observations while
   preserving RF-09 as the lifecycle semantic owner and preserving the ledger's
   non-authorizing status;
4. prevents structural spellings from being recopied from handouts by routing
   them to `PROMPT_CONTRACTS.md`;
5. handles the newly observed report-completion edge case narrowly: a
   client-native planner artifact without AP's separately required terminal
   Worker report is an incomplete exchange, and a bounded report-format repair
   must not reopen planning or grant implementation authority; and
6. records the decision in ADR-0016 and the explanatory/historical projections,
   with no executable or consumer mutation.

The output is one reviewable local commit whose parent is exactly
`041de310ea33ed1b47dd8f5fbfcc2829d1a32514`.

## 3. Hard baselines and pre-mutation gates

The ORCHESTRATOR reverified these public refs credential-free immediately before
issuing this prompt:

```text
AP public refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
AP tree:
a66b81d75d427a1d465bbfe76a890de1fd16aa52
AP parent:
4e7bfa562c961b33cf835a2e764188b190185209
AP subject:
docs: converge ADR-0014 lifecycle status

FrameNest public refs/heads/main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
FrameNest .ap gitlink at that commit:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before any mutation, independently verify all of the following:

1. `/home/agile/Projects/ap` is the intended AP owner repository and its
   configured canonical origin resolves to the public AP repository.
2. Credential-free `git ls-remote` for AP `refs/heads/main` equals the exact AP
   baseline above.
3. Credential-free `git ls-remote` for FrameNest `refs/heads/main` equals the
   exact FrameNest baseline above.
4. The AP baseline object exists locally and its tree, parent, and subject equal
   the identities above.
5. Commit-bound inspection of FrameNest `230ce43a...`, without reading or
   changing its live dirty worktree, confirms `.ap` is a gitlink to
   `041de310...`. Use only an already-present local object. Do not fetch merely
   to satisfy this check.
6. No unresolved instruction conflict changes the objective, owner map,
   allowlist, or compatibility boundary.

If either public ref differs, any immutable identity fails, the FrameNest object
needed for the commit-bound check is unavailable, or repository identity is
ambiguous, do not mutate. Return a terminal `BLOCKED` report with
`Report justification: changed-external-state` for a ref change or
`new-material-risk` for another material gate failure.

Meta is outside the implementation boundary and is not a runtime or authority
source. Do not inspect or mutate Meta. Its archival ref may advance while this
task is running and is deliberately not a hard gate.

## 4. Source precedence and fixed convergence

Use this order while editing:

1. this exact implementation grant and its bounded convergence decisions;
2. the verified AP source at `041de310...`, with `AP.md` as sole live semantic
   owner;
3. current commit-bound repository evidence inside that AP baseline;
4. explanatory or historical projections only as subordinate evidence.

Do not inspect prior Planner artifacts or reports to select between alternatives.
The ORCHESTRATOR has selected the following disposition:

- **Disposition B:** extend existing AP projections.
- No new continuation projection file.
- No managed-block pointer or consumer re-init migration.
- No CLI, schema, `ap.project.conf`, or executable validation change.
- No mandatory ledger filename.
- No YAML ledger and no new parser expectation.
- No AP-specific fixed root file such as `AP_UPGRADE_LEDGER.md`.
- No invented regular expression for entry identifiers.
- No `owner/name` normalization rule for canonical repository identity.
- No `AP_WORKER.md` change; its existing terminal-report and authority rules are
  sufficient, and repeating the new mechanism there would create another
  operational owner.
- One optional project-owned Markdown ledger per declared canonical target,
  explicitly discovered through project-owned root `AGENTS.md` text outside the
  AP managed block.
- The absence of a declaration preserves current behavior; it does not assert
  that no unresolved observation exists anywhere.
- Include the bounded planner-artifact-without-report repair because both
  independent planning sessions produced direct evidence of this same
  structural completion failure. Do not make it client-, model-, provider-, or
  IDE-specific.

If implementing these fixed decisions would contradict a stronger invariant in
the exact baseline, stop before mutation and report the contradiction. Do not
silently choose a third architecture.

## 5. Semantic implementation requirements

### 5.1 Continuation Bootstrap

Keep semantic meaning in `AP.md` and operational steps in
`AP_ORCHESTRATOR.md`. Add no new RF family.

The rule must establish two distinct stages after a pause, session rotation, or
minimal resume seed:

**Stage 1 — read-only restoration and reconciliation**

1. Read the consumer root `AGENTS.md` and the immutable AP documents named by
   the managed block.
2. Verify the canonical project repository, governing AP pin, current public or
   external anchors relevant to the task, and current durable project truth.
3. Restore in RF-19/source-precedence order. Optional trace, prior handout,
   conversational memory, and narrative remain subordinate and non-authorizing.
4. Discover only ledgers explicitly declared in project-owned root `AGENTS.md`
   outside the AP managed block. Do not scan the tree for filename guesses.
5. Validate and revalidate active ledger entries against current repository and
   durable external truth before relying on them. A ledger entry never outranks
   repository truth or an explicit current COOPERATOR decision.
6. Surface contradictions, missing evidence, malformed declared storage, and
   stale observations. Read-only restoration may proceed while gathering this
   evidence, but it cannot falsely claim completed reconciliation.

**Stage 2 — select one bounded logical whole**

1. Present the restored state, remaining active observations, material
   uncertainty, and one evidence-backed recommended next logical whole to the
   COOPERATOR.
2. Obtain the COOPERATOR's explicit selection of exactly one bounded next
   logical whole or a decision to gather more evidence.
3. Only after that selection may the ORCHESTRATOR issue a complete, current
   Worker prompt containing its own exact authority record.
4. A seed, handout, planner artifact, stale task grant, ledger state, Meta trace,
   or previous Worker prompt never supplies current mutation authority.

Place an early, clearly named **Continuation Bootstrap** section in
`AP_ORCHESTRATOR.md` so that the existing managed block's required-reading path
finds it without a block change. The section should point to canonical sections
instead of copying large enums or report grammars.

Include this compact text only as an explicitly non-normative, vendor-neutral
example seed; adjust line wrapping but not its meaning:

```text
Resume this AP-integrated project.
Read the root AGENTS.md and the pinned AP documents it names.
Begin read-only. Restore canonical state and any declared AP upgrade ledger.
With the COOPERATOR, select exactly one bounded next logical whole before any
mutation authority is issued.
```

The seed is an explanatory pointer, not a durable authority artifact and not
required wording.

### 5.2 Ledger relationship and scope

Extend RF-09 rather than replacing it. Preserve all existing lifecycle states,
transition meanings, terminal removal rules, and exact authority boundary.

The durable storage projection is:

- optional;
- owned by the consuming project;
- committed inside the consumer repository when activated;
- retained, non-authoritative discovery evidence;
- scoped only to improvement observations about one canonical target
  repository;
- never a roadmap, issue tracker, current-task/NEXT file, Worker registry,
  transcript, memory dump, specification, ADR, project-rule substitute, or
  second semantic owner; and
- public-safe by default.

Accepted conclusions continue to move to their existing durable owners:
architecture to ADRs, product behavior to specifications, operating policy to
project rules, deferred work to a roadmap or issue, and security policy to its
security owner. The ledger keeps only active observation lifecycle input.

There is exactly one declared ledger file for one canonical target. Multiple
targets use multiple declaration blocks and multiple files. A presentation
ordinal never identifies a target or entry.

### 5.3 Canonical target identity

Do not introduce a new global canonicalization algorithm. For committed ledger
storage, `<canonical-repository>` is the exact repository identity already
accepted by the consuming project's durable rules. The declaration and file
header must repeat that identity byte-for-byte in:

```text
Upgrade ledger: upgrade <canonical-repository>
```

Do not rewrite it to `owner/name`, a display name, a local path, or a provider-
specific shorthand. If project rules have not established one exact canonical
identity, ledger activation is not ready; reconcile that project-owned identity
first.

### 5.4 Project-rule declaration grammar

`PROMPT_CONTRACTS.md` must own the exact storage/discovery spellings. Define one
repeatable project-owned root `AGENTS.md` declaration block outside the managed
block:

```text
AP upgrade ledger declaration:
Upgrade ledger: upgrade <canonical-repository>
Ledger storage version: 1
Ledger path: <normalized repository-relative Markdown path>
```

Requirements:

- the declared file is committed in the same consumer repository;
- the normalized path is relative to the repository root, ends in `.md`, has no
  `..` segment, and resolves inside the repository without symlink escape;
- target identity and storage version match the file header exactly;
- one target maps to one path and one path maps to one target;
- duplicate target declarations, duplicate path declarations, mismatches, and
  conflict markers are malformed;
- there is no required filename and no tree-scanning discovery fallback; and
- do not change the AP-managed `AGENTS.md` block to advertise this optional
  projection.

### 5.5 Ledger file grammar

Use plain UTF-8 Markdown containing AP-native, line-oriented text records. Do
not use YAML/JSON/TOML, front matter, a new schema file, or executable parser
semantics. The required file header is:

```text
Ledger storage version: 1
Upgrade ledger: upgrade <canonical-repository>
Activation snapshot: <bounded identity of candidate observations at activation>
```

Extend the existing Upgrade Observation Ledger Contract so each committed entry
uses the existing fields plus the minimum storage and staleness fields below:

```text
Entry: <stable non-ordinal identifier unique within this ledger>
Entry state: untriaged | accepted | duplicate | rejected | invalidated | implemented | parked
Entry authority: non-authorizing
Summary: <one public-safe line>
Evidence class: repository | project-rule | cooperator | worker-observed | external | inference
Observed against: <immutable commit or other durable evidence identity> | unknown because <reason>
Last revalidated against: <immutable commit or other durable evidence identity> | none
Implementation task grant: none | exact Orchestrator task <task-id> for <Worker boundary>
Implementation status: not-started | authorized | not-applicable | implemented with <durable evidence>
Disposition evidence: <durable evidence identity> | none
Promotion target: adr | specification | project-rules | roadmap | issue | logical-whole | security-document | none
Closure action: retain-active | remove-from-active-ledger
Historical evidence: <commit, decision, changelog, or closure report holding the provenance> | none
Provenance destroyed: no
```

Structural and lifecycle rules:

- `Entry` is an opaque, public-safe, non-empty, single-line identifier. It is
  immutable after first commit and unique within that ledger. Do not impose an
  AP-wide regex. A collision or reuse is malformed until reconciled.
- Existing RF-09 owns the seven states and transitions; this storage grammar
  does not redefine them.
- `Entry authority: non-authorizing` and `Provenance destroyed: no` remain the
  only valid values.
- `Summary`, evidence identity, and all stored content are public-safe. Do not
  store secrets, credentials, private host/path/media identifiers, full
  transcripts, hidden reasoning, or unnecessary production details.
- A new observation begins `untriaged`. `Disposition evidence: none` is valid
  only while no disposition has occurred. Any later state names bounded durable
  disposition evidence.
- `Observed against` records what was actually observed. `unknown because
  <reason>` is allowed only to preserve a candidate safely; it cannot support a
  mutation decision until revalidated.
- `Last revalidated against: none` is valid before the first revalidation.
  After a pause, every active entry is revalidated against current truth before
  Stage 2 relies on it. Contradiction by stronger evidence moves the entry to
  `invalidated` with disposition evidence.
- `accepted` records validity only. It never grants implementation authority.
  Any recorded task grant is current only inside the exact original Worker
  boundary and expires with that authority; it remains historical evidence and
  cannot be resumed as authority.
- `Promotion target` prevents the ledger from becoming a substitute for an
  existing durable owner. Promotion does not by itself authorize work.
- Active states (`untriaged`, `accepted`, `parked`) use
  `retain-active`. Terminal states (`implemented`, `rejected`, `duplicate`,
  `invalidated`) use `remove-from-active-ledger` and require non-`none`
  historical evidence before removal.
- Terminal reconciliation removes terminal entries from the live file only
  after immutable provenance is named. Git history and the named durable owner
  retain the record; do not create a second growing archive file.
- Entry ordering is deterministic by stable identifier. Ordering is
  presentation only and changes only in an authorized reconciliation commit.

### 5.6 Absence, empty, malformed, stale, and conflicted behavior

Define these cases precisely without adding runtime validation:

- **No declaration:** valid compatibility behavior. No AP-contracted durable
  ledger has been activated. Continue with existing canonical sources and
  COOPERATOR reconciliation. Do not infer that the universe contains zero
  unresolved observations.
- **Valid declared file with no entries:** zero active ledger entries for that
  declared target.
- **Undeclared lookalike file:** ordinary project content, not an AP ledger.
- **Declared missing file, empty file without the required header, target/path/
  version mismatch, duplicate target/path/id, unknown version, invalid record,
  or conflict markers:** malformed, non-authorizing evidence. Read-only
  restoration may continue, but the ORCHESTRATOR cannot claim ledger
  reconciliation complete or issue mutation authority that relies on it. Route
  a bounded reconciliation/repair decision to the COOPERATOR.
- **Stale but structurally valid entry:** not automatically malformed. Preserve
  it as non-authoritative evidence, revalidate it, and disposition it from
  current truth.
- **Repository contradiction:** repository/current durable truth wins; record
  `invalidated` with evidence.
- **Public AP main ahead of a consumer pin:** the pin governs that consumer. An
  update is a separate explicit task.

### 5.7 Planner artifact without terminal report

Add one narrow clarification at the semantic, structural, Orchestrator, and P11
projection surfaces:

- A client-native planner artifact does not replace the required standard
  terminal Worker report.
- If an otherwise healthy planning exchange yields a frozen decision-complete
  artifact but no separate AP terminal report, the exchange is structurally
  incomplete and cannot be treated as planning PASS.
- The ORCHESTRATOR may issue the same healthy Worker session a complete next-
  exchange, report-rendering-only repair grant with the next exchange ordinal,
  `Native planning mode: not-used`, the frozen artifact as continuity anchor,
  and explicit prohibitions on re-planning, implementation, mutation,
  acceptance, publication, and closure.
- The repair renders the missing report prospectively. It never overwrites the
  earlier exchange, changes the frozen plan, retroactively grants authority, or
  consumes a second planning cycle.
- `Native planning mode: not-used` is a client-mode routing declaration, not
  implementation authority. Execution still requires a separate complete
  Implementation Authority Record.
- Keep all wording vendor-, model-, client-, provider-, IDE-, and memory-system
  neutral. Do not create new statuses, phase results, report justifications, or
  exchange filename rules.

This is a bounded completion branch of the existing report-format repair and
P11 session/mode routing rules, not a new role, phase, lifecycle, or artifact.

## 6. Exact changed-path allowlist

Change **all and only** these 12 paths:

| Path | Required purpose |
|---|---|
| `AP.md` | Sole semantic owner: two-stage continuation, optional ledger storage/discovery semantics, and bounded planner-artifact/report-completion rule under existing rule families |
| `PROMPT_CONTRACTS.md` | Exact declaration, header, entry, absence/malformed/staleness, and report-repair structural spellings |
| `AP_ORCHESTRATOR.md` | Early named Continuation Bootstrap checklist, seed example, and operational report-repair route |
| `PROMPT_ENGINEERING_PATTERNS.md` | Extend P11 only with the client-native artifact-without-report completion branch |
| `ARTIFACT_LIFECYCLE.md` | Classify the optional consumer ledger, active/terminal retention, removal, and historical provenance |
| `INTEGRATION.md` | Explain the optional project-owned root `AGENTS.md` declaration outside the unchanged managed block |
| `README.md` | Minimal reading/discovery pointer to the named Continuation Bootstrap and ledger contract |
| `FAQ.md` | Concise continuation-after-pause and optional-ledger guidance, with canonical links |
| `GLOSSARY.md` | Define Continuation Bootstrap and the durable upgrade-ledger storage projection without creating semantic ownership |
| `CHANGELOG.md` | One Unreleased historical delivery entry with compatibility boundary |
| `docs/adr/README.md` | Index ADR-0016 and state its relationship |
| `docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md` | Historical ADR recording the converged decision and rejected alternatives |

The new ADR is the only new file. Keep artifact-relationship labels consistent
with ADR-0013: `AP.md` alone owns live semantics; contracts are structural;
role/lifecycle/integration documents are operational; README/FAQ/GLOSSARY are
explanatory; ADR and changelog are historical.

ADR-0016 must record at least:

- the proven narrow gaps and rejected overbroad framing;
- disposition B and the two-stage bootstrap;
- optional explicit project-rule declaration;
- one Markdown ledger per canonical target with no fixed filename;
- non-authority, staleness, privacy, terminal reconciliation, and safe absence/
  malformed behavior;
- the bounded planner-artifact-without-report repair evidence;
- rejection of `CONTINUATION.md`, a managed-block change, YAML, fixed
  `AP_UPGRADE_LEDGER.md`, `owner/name` normalization, ID regex, CLI/schema/
  `extension.*.*`, executable validation, Meta-as-runtime, and FrameNest
  mutation; and
- compatibility: existing consumers remain unchanged until an explicit AP pin
  update and optional project-local adoption.

## 7. Explicitly unchanged and prohibited surfaces

Do not change, create, delete, rename, stage, or commit anything outside the
allowlist. In particular:

- no `CONTINUATION.md`, `MEMORY.md`, BOOT/NEXT/session-state file, ledger
  template, example consumer ledger, or schema file;
- no `AP_WORKER.md`, `UPDATING.md`, `INFOSEC.md`, `AGENTS.md`, managed block,
  `ap`, `ap.project.conf`, tests, fixtures, CI, or dependency files;
- no schema-v1 change, `extension.*.*` protocol use, CLI command, doctor rule,
  parser, validator, conformance suite, or executable check;
- no FrameNest, Meta, remote ref, release, issue, pull request, account, host,
  service, provider, deployment, or production mutation;
- no copying provisional `CONT-001` labels into AP as normative identities;
- no legitimizing or reproducing the drifted structural values
  `planning-PASS`, `planning-PARTIAL`, `planning-BLOCKED`, `no-new-material`,
  `invariant-failure`, or `public-ref-mutation` as valid AP fields;
- no model, provider, client, IDE, emoji, hidden-reasoning, or trace-as-authority
  semantics; and
- no reopening the closed project-local prompt-archive or sidecar logical
  wholes.

A future `ap doctor` ledger-shape check and a future FrameNest adoption/pin
update remain separate logical wholes requiring separate evidence and authority.

## 8. Repository, worktree, and Git authority

Preferred owner repository:

```text
/home/agile/Projects/ap
```

Use an isolated new worktree and branch:

```text
Branch: feat/universal-continuation-observation-ledger
Worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w3
Base: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before creation, inspect the owner repository, existing worktrees, branch ref,
and exact target path read-only. Do not clean, stash, reset, switch, or otherwise
modify the owner worktree or any unrelated user state. Owner-worktree dirtiness
is not permission to touch it; if isolation remains safe, create the new
worktree directly from the exact baseline object. If the named branch or target
path already exists, stop `BLOCKED` rather than deleting, reusing, or
overwriting it.

Authorized Git mutations are limited to:

1. creating that one local branch and isolated worktree from the exact baseline;
2. editing the allowlisted paths;
3. staging only those paths; and
4. creating one new local commit with exact subject:

```text
docs: define continuation bootstrap and observation ledgers
```

The commit must have exactly one parent, the AP baseline above. Do not amend,
merge, rebase, cherry-pick, tag, fetch, push, force, delete refs/worktrees, or
change local/global Git configuration. If signing or another repository policy
prevents the commit, do not weaken configuration; report the blocker.

No temporary clone is authorized or needed. Leave the implementation worktree
and branch intact for fresh acceptance. Do not clean them up at task end.

## 9. Implementation method

1. Re-read the complete exact-baseline versions of every allowlisted existing
   file and the directly linked owner sections before editing.
2. Map each statement to its semantic owner/projection class. Avoid duplicated
   normative prose and prefer canonical links for long existing rules.
3. Implement the semantic owner first, then exact structural contract, then
   operational, explanatory, and historical projections.
4. Preserve established headings and style; keep changes narrow and readable.
5. Use repository-native editing. Do not run formatters that can rewrite
   unrelated content.
6. Review the staged diff as a single coherent protocol change before commit.

Do not merely paste this prompt's prose into every file. Compact it according to
each artifact's relationship while preserving every fixed decision and exact
structural spelling.

## 10. Required validation before commit

Documentation-first proportional validation per ADR-0015 is mandatory. At
minimum:

1. inspect the full unstaged and staged diffs;
2. prove the changed-path set is exactly the 12-path allowlist and no other path
   changed in the isolated worktree;
3. run `git diff --check` before commit and the equivalent commit-range
   whitespace check after commit;
4. verify all relative Markdown links and referenced local paths resolve;
5. verify fenced code blocks are balanced;
6. compare every new exact field and allowed value directly against the final
   `PROMPT_CONTRACTS.md` text;
7. verify `AP.md` is the sole live semantic owner and projections do not create
   a competing owner;
8. verify `AP_WORKER.md`, `ap`, `ap.project.conf`, the managed block, schema v1,
   tests, FrameNest, and Meta are byte-untouched by this task;
9. search the candidate for accidental normative use of the prohibited drifted
   spellings listed in section 7; their appearance in ADR rationale is allowed
   only when clearly quoted as rejected evidence, never as a valid value;
10. verify the declaration and file-header target/version match rules, absence
    behavior, malformed behavior, authority expiry, and terminal-removal
    behavior are consistent across all projections;
11. verify README, FAQ, GLOSSARY, CHANGELOG, and ADR links point to the canonical
    owner rather than restating it as authority;
12. verify the new ADR filename, index entry, number, title, status, and
    relationship agree;
13. after commit, prove:
    - commit parent is exactly `041de310...`;
    - commit subject is exact;
    - commit changed only the allowlist;
    - the worktree is clean; and
    - no push occurred.

Do not recreate the retired monolithic suite and do not add protocol-mirroring
tests. If a small read-only script is used only to inspect links, fences, paths,
or diffs, report it; do not commit it.

## 11. Acceptance criteria for implementation PASS

Report `PASS` only if all are true:

- both hard public baselines and immutable identities matched before mutation;
- the candidate implements every fixed requirement in sections 5 and 6;
- exactly the 12 allowlisted paths changed, with only ADR-0016 newly created;
- no prohibited surface changed;
- semantic ownership and structural spellings are internally consistent;
- no current authority can arise from a seed, ledger, planner artifact, old task
  grant, or report repair;
- missing declaration remains backward-compatible, while malformed declared
  storage fails closed before mutation relying on it;
- the managed block, CLI, schema, executable, tests, consumers, and Meta remain
  unchanged;
- all required validation passes;
- one local commit with the exact parent and subject exists; and
- the implementation worktree is clean and unpushed.

The implementation Worker is not independent acceptance. Do not claim
architecture acceptance, publication, consumer adoption, or logical-whole
closure. A fresh independent Worker will review the exact candidate under a
separate prompt.

## 12. Stop and escalation conditions

Stop before further mutation and report `PARTIAL` or `BLOCKED` when any of these
occurs:

- a hard baseline or repository identity differs;
- branch/worktree collision or protected user state prevents safe isolation;
- a stronger baseline invariant materially contradicts the fixed convergence;
- a required change falls outside the allowlist;
- a fixed decision would require executable/schema/managed-block/consumer
  mutation;
- exact structural consistency cannot be achieved without a new decision;
- required validation cannot be run or gives unresolved material failure;
- commit creation fails under existing repository policy; or
- any credential, secret, private path/media detail, or unrelated user change
  would be exposed or overwritten.

Do not broaden authority, improvise a replacement architecture, perform an
automatic correction cycle, or create a Worker 4 prompt. Preserve evidence and
name the smallest decision or authority expansion needed.

## 13. Mandatory terminal report

Return exactly one standard terminal report in the **same response** as the end
of the implementation work. It must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Its metadata must contain exactly one occurrence of:

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 03
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact local commit SHA or not-applicable>
Result evidence: <bounded exact evidence>
Logical-whole closure: not-closed
Report justification: <one canonical allowed value>
Authority expiry: all Worker 3 implementation authority expired at this terminal report
```

Render one actual value, never the literal alternatives. Use
`Phase-qualified result: implementation-PASS` only with terminal `PASS`; use
`not-applicable` for `PARTIAL` or `BLOCKED`. A successful committed candidate
normally uses `Report justification: new-mutation`; a hard public-ref mismatch
uses `changed-external-state`; another material stop normally uses
`new-material-risk` or `new-evidence` as actually supported.

The report must also state, evidence-densely:

1. route, fresh-session status, native mode observed, capabilities used,
   delegation status, evidence posture, and authority boundary;
2. exact AP and FrameNest pre-mutation gate results;
3. owner repository and isolated branch/worktree handling, including preserved
   pre-existing user state;
4. start commit, end commit, parent, tree, subject, and clean status;
5. changed files with one-line purpose each;
6. semantic-owner and projection review result;
7. exact structural grammar and cross-projection consistency result;
8. validation commands and bounded results;
9. commit result and explicit `Push: not-authorized, not-performed`;
10. deviations, risks, missing evidence, and out-of-scope observations;
11. `Resolved Execution Issues / Near-Misses: none` or a complete bounded
    record;
12. `Pre-Existing Failure Classification: none` or a complete applicable
    classification;
13. temporary artifacts and cleanup status, while retaining the authorized
    implementation worktree for acceptance; and
14. the single smallest next step: fresh independent acceptance of the exact
    candidate commit.

Do not substitute a client-native completion artifact, plan, summary, or
progress update for this report. Stop autonomous work immediately after the
terminal report; all authority expires regardless of context health.
