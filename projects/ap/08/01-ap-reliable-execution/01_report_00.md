### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-update
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Task identity: AP-RELIABLE-EXECUTION-INITIAL-PLAN
Worker session target: fresh-worker-session
Worker session profile: Planner
Native planning mode: required
Phase: Discovery / implementation-planning
status: PARTIAL
Phase-qualified result: not-applicable
Planning cycle: initial
Automatic targeted revisions used: 0
Plan disposition: approval-gated
Report justification: new-evidence
Logical-whole closure: not-closed
Start AP commit: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
End AP commit: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
```

# AP — Reliable Execution and Cooperator Experience: Initial Planning Report

The recommended design is one bounded documentation change: simplify task composition, make action and completion authority internally consistent, bind acceptance values to their actual objects, and place complete finishing examples beside the existing contracts. Preserve AP’s semantic owner, structural owner, roles, finite authority, independent acceptance, manual delivery, executable interfaces, and consumer pins.

The design is decision-ready. **PARTIAL describes missing file delivery:** native Plan Mode prohibits filesystem writes in this session. Neither required output file was created. This complete report is frozen through the permitted client output; implementation and design adoption remain unauthorized.

| Report core | Actual outcome |
|---|---|
| Changed files and purposes | None |
| Required opening notes | `/home/agile/meta/projects/ap/08/01-ap-reliable-execution/00_notes.md` remains absent |
| Required planning report | `/home/agile/meta/projects/ap/08/01-ap-reliable-execution/01_report_00.md` remains absent |
| Validation performed | Source inspection, immutable-object comparison, direct public-ref checks, input hashes, path/collision inspection, and disposition/owner/scenario coverage review |
| Saved-output readback | Not performed: saving is prohibited |
| Git result | No Git writes, fetches, staging, commits, or pushes |
| Runtime/build/test execution | None; unnecessary for this planning result |
| Main limitation | Documentary design evidence does not establish improved client performance |
| Recommended next step | One separately authorized completion-only exchange to persist the exact frozen report and supplied opening notes, with its own completion report |
| Authority expiry | This exchange’s authority expires upon submission of this terminal report |

## 1. Evidence reconciliation and D2 dispositions

### Environment and capability observations

Inspection on 2026-09-12 established:

- AP’s physical root is `/home/agile/Projects/ap`, with Git directory `/home/agile/Projects/ap/.git` and canonical remote `https://github.com/cisarik/ap.git`.
- AP HEAD is the governing commit above; its parent is `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`. The observed branch is `feat/ap-practical-workflow-consolidation`. Its name is not a baseline failure.
- AP’s index and worktree are clean. No relevant AP untracked files or checked Git-operation markers were found.
- META’s physical root is `/home/agile/meta`, with canonical remote `https://github.com/cisarik/meta.git`, branch `main`, and HEAD `1bf6a913e21c309d78eff8d742f19be678731d8f`. Its tracked worktree and index are unchanged.
- Direct `git ls-remote origin refs/heads/main`, repeated at the final repository recheck, returned the pinned AP and META commits.
- Both required output paths are absent. Their parent directories resolve inside the verified META tree; no destination symlink or collision was observed.
- No applicable `AGENTS.md` was found in the inspected AP/META ancestor and task-directory locations. ContextDesk’s historical consumer instructions were treated solely as evidence.
- All required immutable objects were already available. ContextDesk’s root and remote were verified, then only exact historical Git objects were inspected.

The visible conversation contains no preceding Worker task. The current trace contains its discovery, handout, and the matching initial prompt, with no report or additional exchange observed. External session-creation telemetry is not exposed.

| Capability | Requested versus observed |
|---|---|
| Native planning | Required; active Plan Mode is explicitly supplied by the client instructions |
| File preparation | Authorized by the task, prohibited by the higher-priority active mode; no write was attempted |
| Source and public-ref inspection | Available and exercised successfully |
| High reasoning | Requested; effective enforcement is not independently exposed |
| Approximately 250k context | Recommendation only; effective capacity and usage telemetry are unknown |
| Model/provider identity | No independently attested identity obtained |
| Permissions | Client configuration exposes unrestricted filesystem access and approval policy `never`; these do not override Plan Mode or task authority |
| Delegation | Prohibited and unused |
| Configuration changes | None |

The native-mode restriction is a client-policy observation, not a measured failed filesystem operation. The task anticipated this route, so it does not prevent responsible planning.

### RF-12 disposition of local differences

All five canonical recovery classes were considered for each relevant difference:

| Classification unit | Primary disposition | Other class assessment and action |
|---|---|---|
| Current untracked `01_planning_00.md` | `accepted-continuation` | Byte-identical prepared input for this exchange. No stale-clone, unpublished-candidate, unrelated-owner-work, or unexplained-divergence evidence; preserve it |
| ContextDesk `20_implementation_00.md` and `20_report_00.md` in META | `unrelated-owner-work` | Outside this whole; inspected as path names only. No other class established; preserve without investigating their current product outcome |
| AP branch name versus public `main` | No content divergence requiring recovery | HEAD and public main agree; no switch or cleanup is needed |

The current prompt and attachment both hash to:

`fb86bbaa6b04a99c067879ac3a04e1ecd0b504d7b65b118cf77b91a17df25685`

The discovery’s working and committed bytes match:

`aceaf2fe5d469d675f41a831d0cbb9056216c2715c258cd786ec4c0cc2739788`

The historical handout destination remains provenance. New output routing uses `01-ap-reliable-execution`; the logical identity remains `ap-update`.

### Source anchors and evidentiary limits

The governing [AP semantic owner](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md), its selected role projections, structural contracts, lifecycle guidance, executable command boundary, and project configuration were inspected. The complete current discovery and handout and the predecessor closure were read. The predecessor planning report was consulted for its native-mode persistence failure and accepted design only.

The predecessor [closure](https://github.com/cisarik/meta/blob/1bf6a913e21c309d78eff8d742f19be678731d8f/projects/ap/08/00-ap-practical-workflow-consolidation/03_closure.md) records documentary acceptance and publication of the consolidation. That result remains valid within its stated limits; it did not claim measured client efficiency.

For the disposition table:

- **12 grant/report** means [12_implementation_02.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/12_implementation_02.md) and [12_report_02.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/12_report_02.md).
- **13 grant/report** means [13_acceptance_00.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/13_acceptance_00.md) and [13_report_00.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/13_report_00.md).
- **Product** means ContextDesk commit `cb72ae0388307b514182efc6936712e3da42cda4`.

Both archived prompt hashes reproduce the discovery’s values. Git history also confirms that the 13 prompt/report pair was first added together at `d00fa3ba2256c985c3c828ad88ea6ee143d8f57f`.

Reading an archived report directly establishes what the Worker reported. It does not convert its host observations or test results into this Planner’s direct runtime evidence.

### Compact disposition table

| Finding | Reproduced evidence and class | Governing owner | Classification | Likely cause and uncertainty | Disposition and smallest affected projection | Observable validation |
|---|---|---|---|---|---|---|
| **D2-01** | 13 grant prohibits META/persistent writes without an exact exception; 13 report says no file was saved. Documentary and Worker-reported evidence; human transcription remains Cooperator evidence | AP RF-19; Planning Budget and Expiry | Orchestration application defect; projection/usability defect | Persister naming was mistaken for permission, and file preparation was conflated with Git archival. 12’s reported save does not prove its grant was fully conforming | **Fix** the delivery example and Worker finishing sequence. Include a positive path grant, all terminal statuses, collision checks, readback, and separate Git ownership | V1–V2: authorized save succeeds; any existing report is preserved; no transcription obligation |
| **D2-02** | Discovery documents a conversation-only unsupported-source incident. Its underlying failed reads and subsequent responses were not independently reproduced | AP RF-19; §14; Orchestrator Intent and Evidence Reconciliation | Reported orchestration application defect; projection/usability lead. Direct telemetry claim unsupported | Narrative apparently replaced unavailable report bytes. Exact incident causality remains attributed | **Fix** the operational unavailable-source example; do not add another provenance register | V3: unavailable exact report produces an explicit evidence gap, never an invented verdict |
| **D2-03** | 13 Gate 0 assigns `0755` to the service file; product operations installs it with `0644`; unit property is `RuntimeDirectoryMode=0755` | AP §12 and §7; product operations/service owners | Orchestration application defect; projection/usability defect | Expected value lost its object/property binding. Broader propagation through earlier conversations is not independently established | **Fix** object-bound gate construction using existing validation content; no universal Linux modes | V5: service file, runtime property, and executable are evaluated separately |
| **D2-04** | 12 combines R1/R2, rehearsal, tests and two commits; 13 combines installation prerequisites, static review and multiple physical claims. Compaction frequency is Cooperator evidence | AP §14–§15; §17; reading spine | Orchestration application defect; projection/usability defect | Deliverables and context signals were insufficiently reflected in routing. No token/compaction telemetry reproduced | **Fix** outcome-sized routing example and common-contract selection; no universal context limit or mandatory per-commit rotation | V4: one independently useful outcome, relevant reading and a bounded report point |
| **D2-05** | 12 report explicitly says the unit was not reinstalled; 13 assumes installation complete but forbids it. Installed binary/unit mismatch is 13 Worker evidence | AP §7; RF-07/RF-08; §15 | Orchestration application defect | A known unmet dependency was routed into a host-dependent acceptance task. The stale binary was established later, not by the earlier unit statement alone | **Fix** prerequisite routing in Prompt Construction; product installation remains separately owned | V4: route a prerequisite or useful source review; do not repeat a predictably blocked broad audit |
| **D2-06** | 13 prohibits persistent files while requiring build output; permits one start while later demanding a new invocation. Gate 0’s exact stop wording is narrower than discovery’s characterization | AP §5, §7, §18; structural authority/envelope fields | Orchestration application defect; projection/usability defect; partially unsupported discovery interpretation | Independently composed clauses conflict. Whether the Gate 0 wording permitted later static work is ambiguous; it does not unambiguously order immediate terminal submission | **Fix** action/count/stop consistency and explicit residual-work boundaries. Reject the stronger unsupported stop claim | V5: every required action fits its grant and count; failed-gate continuation is explicit or absent |
| **D2-07** | 12 accepts one-keyboard cutoff recovery. Product operations and 13 Gate 4.4 preserve it; 13 Gate 4.5 retains separate watchdog evidence. Testing documentation requires an external signal/recovery path for its hang harness | AP RF-01/RF-07; §7; product operations/testing owners | Orchestration scope/usability defect; consumer documentation ambiguity | Bundling different claims changes what the requested trial can complete. A watchdog safety requirement is not disproved by cutoff success | **Fix** outcome separation and accepted-constraint carry-forward. **Defer** consumer procedure reconciliation; reject weakening watchdog evidence | V6: cutoff can reach its bounded result while watchdog and overall G4 remain open |
| **D2-08** | 13 report starts with Slovak prose and uses `BLOCKED` as phase result; its prompt offered that invalid value. Prompt templates and 12 report duplicate coordinates | AP RF-19; §17; Worker Report Header; Phase Result and Closure Record | Orchestration application defect; report-output defect; projection/usability defect | Report instructions and copied templates drifted. Useful observations remain attributable despite malformed packaging | **Fix** one blocked-report example and single-coordinate composition. Preserve historical bytes; no new enum or cosmetic repair exchange by default | V7: exact first line, one coordinate set, valid status/result, distinct interruption identity |
| **D2-09** | 13 reports failed `sudo -n` and an unperformed broker-identity check. The grant offers no complete owner-authenticated execution route | AP RF-13; Owner-Executed Commands and Privileged Sessions; Owner-Executed Command Contract | Orchestration application defect; projection/usability defect | Authentication was treated as ambient client capability. Availability in another terminal was not proof for this process | **Fix** operational owner-session routing example. No passwordless-sudo prerequisite; no host change here | V6: authentication, privileged operation and release belong to the actual named owner session |
| **D2-10** | Product AGENTS and ROADMAP still identify recovery design/safety gaps as next work, while code and technical docs contain R1/R2. 12 explicitly excluded root-document changes | AP RF-14/RF-19; §7/§13; product documentation owners | Consumer defect; orchestration follow-through defect | No bounded reconciliation of stale durable summaries. README is broadly accurate about uncompleted G4, so blanket staleness is overstated | **Fix** AP’s operational routing example; **defer** product repairs to its owner. Do not add a second state file | V4/V8: fresh restoration distinguishes implemented, reviewed, installed and physically accepted |

### Corrections that materially affect the design

**The previous successful save is not an ideal authority example.** The 12 grant permits preparation when a report is “absent or empty,” while governing RF-19 protects any existing terminal report. It also contains broad META-prohibition language. The replacement example must use an absent destination and an explicit exception; copying that historical grant would reproduce another defect.

**D2-06 has two definite contradictions and one interpretation dispute.** Gate 0 ends with “report `BLOCKED`, and stop before any live trial.” It establishes a live-transition stop, but does not clearly settle the timing of the report versus subsequent device-free checks. The Worker’s continuation is therefore not evidence of disobeying an unambiguous immediate-terminal instruction. Nevertheless, generated build output still lacks a coherent positive exception.

The opening acceptance claim is candidate-qualified. The four inspected exchange artifacts do not establish a complete earlier acceptance-budget ledger. No retrospective audit count is invented. Future issuance must reconcile the prior acceptance boundary and justify any additional claim-specific evidence.

**Expected values need distinct owners.** At the product pin:

| Object/property | Supported expectation or observation | Owner/evidence |
|---|---|---|
| Installed service file | File installation mode `0644`; content matches candidate unit | [Operations §9](https://github.com/cisarik/contextdesk/blob/cb72ae0388307b514182efc6936712e3da42cda4/docs/operations.md#9-install-the-broker-binary-s5--cooperator-run) |
| Service `RuntimeDirectoryMode` | `0755` | [Service unit](https://github.com/cisarik/contextdesk/blob/cb72ae0388307b514182efc6936712e3da42cda4/packaging/systemd/contextdeck-broker.service) |
| Installed broker binary | Operations requires existence and executability; 13 reports observed mode `755` | Operations §9 and attributed Worker readback |

The binary’s observed mode must not silently become a stronger acceptance requirement than its owner specifies.

**Recovery documentation is claim-dependent.** Operations permits the one-keyboard cutoff demonstration; the [production hang harness](https://github.com/cisarik/contextdesk/blob/cb72ae0388307b514182efc6936712e3da42cda4/docs/testing-m2.md#production-hang-harness-g4-only) needs an externally delivered signal and recovery route. Some surrounding general wording needs consumer reconciliation, but this does not establish that every watchdog test is safe without that route.

Targeted code inspection corroborated the presence of sink-error handling, capability measurement before virtual creation/grab, LED feedback handling, the narrow session lookup fallback, and invocation checks in the cutoff helper. This supports “implemented in the historical tree,” not runtime correctness or present host acceptance.

## 2. Recommended design and affected owners

### A. Make task composition smaller and internally executable

Reorganize `PROMPT_CONTRACTS.md` **Common Worker Task Fields** into a compact composition entrypoint followed by the existing task-triggered catalog. Preserve existing field spellings and activation semantics.

Use these content groups, without introducing new mandatory field names:

1. **Identity and route:** role, coordinates, task/phase/profile, session target and native mode.
2. **Outcome and accepted constraints:** one coherent result and its completion criteria.
3. **Sources and prerequisites:** applicable repository/artifact identity, baseline, required reading and gates.
4. **Authority:** positive effects, exclusions, commands and Git boundary.
5. **Evidence:** selected validation, applicable independence and missing-evidence handling.
6. **Finish:** stop conditions, complete report, activated persistence and expiry.

Reasoning and context recommendations remain recommendations. Current-session renewal, planning history, trace delivery, owner privilege, browser/provider activity, deployment and other annexes activate only when applicable. An inactive field’s omission never supplies permission.

This is an organization of existing required content, not a new fixed giant template. Exact task authority stays self-contained; stable protocol meaning remains linked. Do not add an authority register, prompt-size limit, telemetry requirement or symbolic notation.

Replace the repeated long composition inventory in `AP_ORCHESTRATOR.md` **Prompt Construction** with the operational sequence:

- Establish the exact sources, retained decisions and one useful outcome.
- Resolve known prerequisites and the applicable execution route.
- Compose the common contract and activated detail.
- Check required actions, effects, quantities, failure paths and output preparation against the same grant.
- Deliver through the already selected route with a viable completion path.

The consistency review belongs to prompt preparation. It need not produce another permanent checklist or attestation.

### B. Make three narrow normative clarifications

Most D2 incidents violate existing protections. Three refinements are justified because the current text leaves consequential relationships too easy to compose ambiguously.

| Amendment | Exact AP owner | Required behavior | Detection surface/class |
|---|---|---|---|
| **Issuance consistency** | `AP.md` **§7 Orchestrator Responsibilities**, replacing the current undifferentiated readiness-review paragraph | Before issue, each required action—including validation output, report preparation and recovery—must fit the positive authority, exclusions, prerequisites and action budget. A known unmet prerequisite must be routed to its owner or excluded from a narrower useful outcome; it must not be presented as already satisfied | **Artifact-detectable:** issued prompt, cited prerequisite evidence, allowed effects and action counts |
| **Object-bound expectations** | `AP.md` **§12 Validation and Public Verification** | When an exact expected value determines a gate, identify its object/property, authoritative source and readback method in the task’s existing validation content. Resolve material source conflicts prospectively; do not silently substitute another object or expectation | **Artifact-detectable:** gate specification, source citation and reported readback |
| **Stop and finishing scope** | `AP.md` **§18 Stopping Conditions** | A failed prerequisite stops substantive work by default. Only explicitly granted, unaffected residual checks may continue after that failure. Report preparation and necessary cleanup remain limited by their own positive authority and verified gates; a terminal stop permits no further substantive work | **Artifact-detectable:** stop clause, residual-work grant, execution/report evidence and saved-output evidence |

These amendments do not grant new effects. In particular, the stop clarification does not let a Worker decide that an ungranted continuation is “useful” or bypass a failed capability boundary.

Use a short pointer from **§5 Task Authority** to the stop owner where needed. Preserve RF-19’s existing persistence semantics and **Planning Budget and Expiry**’s completion recovery. Projections link to these owners rather than introducing parallel normative statements.

### C. Put the complete finishing route where it is used

In `PROMPT_CONTRACTS.md` **Cooperator Delivery and Trace Destination Record**, add one complete source-review example using manual delivery and native mode `not-used`. It is a later bounded review example, not a substitute for the initial native Planner.

The example must demonstrate:

- A resolved repository/baseline and one read-only source-review outcome.
- Source-read-only scope with an explicit positive exception for the exact report file.
- Assigned Worker authorship/persistence and Cooperator-owned META Git.
- Physical root, parent, symlink and destination checks before substantive work.
- No overwrite or append to any existing report, including an empty file.
- Complete report creation for PASS, PARTIAL or BLOCKED; full readback before terminal notification.
- Archival waiting until the report exists; no Worker Git archival authority.
- A task-specific failed-source route that still permits report preparation when its independent path/capability gates pass.

The example is a complete parameterized model. Before issuance, the Orchestrator resolves every placeholder and includes identity coordinates only once; the report instruction refers to those coordinates instead of copying a second metadata block.

In **Worker Report Header**, add a standalone blocked-report example with the exact first line, one coordinate block, `status: BLOCKED`, `Phase-qualified result: not-applicable`, compact evidence, persistence outcome, critique, next step and expiry. Use `none` for absent near-misses. Keep informal localized notices outside the report artifact.

In **Planner-Artifact Report Completion Repair**, organize the already supported choices explicitly:

1. Frozen plan lacks its standard report: separately authorized rendering.
2. Complete report lacks file delivery: exact persistence of supplied content.
3. Neither route can access exact predecessor content: report the source gap.

Each renewed Worker exchange uses actual next coordinates and its own report. It preserves the predecessor’s original status and never reopens planning or implements the design.

In `AP_WORKER.md`:

- **Worker Exchange Coordinates and Trace Boundary** performs early delivery/path feasibility checks and links to RF-19.
- **Reporting** presents one finishing sequence: finalize content → authorized save → complete readback/identity check → terminal notice → expiry.
- **Stopping Conditions** points to the clarified stop owner.
- Remove duplicated persistence/recovery explanations from these sections once the single operational sequence and owner links cover them.

In `ARTIFACT_LIFECYCLE.md` **External Analytic Development Trace**, consolidate repeated preparation instructions into links to RF-19 and Worker Reporting. Preserve authorship, retention, interruption and after-outcome archival responsibilities.

### D. Keep source claims, accepted constraints and sequencing near decisions

Update these `AP_ORCHESTRATOR.md` sections:

| Heading | Operational change |
|---|---|
| **Intent and Evidence Reconciliation** | Add a short unavailable-report example. Name the expected immutable commit/path and unresolved claim; distinguish Worker, Cooperator and direct observations. A narrative retrieval may locate evidence but cannot replace the requested source |
| **Worker Exchange Coordinates and Optional Trace** | Make this the single Orchestrator entrypoint for report retrieval and delivery failure. Link to the finishing/completion contracts rather than restating them |
| **Planning Ownership and Plan-to-Execution** | Point to the two completion cases; retain expiry, renewed authority and native-mode boundaries |
| **Prompt Construction** | Add one outcome-sized sequencing example: production candidate; device-free recovery mechanism; independent review; owner installation/identity; one physical trial. Preserve accepted constraints and expose prerequisites beside the affected stage |
| **Validation, Results, and Closure** | Show how implemented, reviewed, installed and physically accepted states remain separate. Route stale durable summaries to their existing owners under a bounded allowlist |

The sequencing example is operational/advisory guidance, not a mandatory five-Worker pipeline. Related implementation and documentation can stay together when they serve one outcome and context remains healthy.

The owner-command example links to the existing **Owner-Executed Command Contract** and demonstrates authentication and authorized privileged effects in the same owner terminal, bounded output capture and release. It introduces no passwordless-sudo requirement, keep-alive, credential exchange or new privilege mechanism.

ChatOrchestrator and inspection-clone support already exist. The improvement is a clearer evidence and delivery route for that access profile; no role or access-profile feature is missing.

### E. Record the design without creating another live database

The proposed AP change boundary is:

- `AP.md`
- `PROMPT_CONTRACTS.md`
- `AP_ORCHESTRATOR.md`
- `AP_WORKER.md`
- `ARTIFACT_LIFECYCLE.md`
- `docs/adr/0024-reliable-execution-and-cooperator-experience.md`
- `docs/adr/README.md`
- `CHANGELOG.md`

Preserve existing anchors and unaffected requirements. No general documentation cleanup is included.

The sole proposed new repository artifact is ADR-0024. The existing ADR index requires a new record when an accepted decision changes; rewriting accepted ADR-0023 would corrupt historical rationale. ADR-0024 records these refinements, rejected alternatives, compatibility and evidence limits. It is historical retained evidence for maintainers, discoverable through the index, and removable only under later explicit lifecycle authority. It is not a second protocol or D2 database.

The D2 disposition and validation matrix stay in this report and subsequent acceptance evidence. Existing advisory patterns remain available selectively; no new pattern library, README workflow duplicate or permanent state file is needed.

## 3. Compatibility, alternatives and assumptions

The public structural interface remains stable:

- Same three roles, coordinates, session targets and native-mode values.
- Same report header, terminal statuses, phase-result enum and report justification values.
- Same planning/revision/correction budgets and required independent acceptance.
- Same optional trace activation and distinction between AP’s default filenames and META’s local suffix arithmetic.
- Same prompt/report authorship, file preparation and separate Cooperator Git ownership.

No change is proposed to executable `ap`, schema-v1 `ap.project.conf`, CPython/runtime policy, managed integration block, stable distribution tuple, integration/update commands or consumer pins. The declared `runtime-info` operation is irrelevant to this task and was not run. `ap doctor` validates integration; its inspected command boundary does not validate Worker grants or prove model conduct.

Migration is prospective: newly issued prompts under an adopted revision use the reorganized contract and clarified rules. Historical prompts/reports retain their original bytes and governing pins. An ongoing planned whole does not repeat its initial planning.

| Material alternative | Assessment |
|---|---|
| **Examples only, with no owner clarification** | Lower semantic-change cost, but leaves stop scope and object-bound gate construction less explicit. Retain the examples and adopt the three narrow owner refinements |
| **Full protocol rewrite or new compact DSL** | Larger migration and interpretation risk; the evidence does not establish a need to replace AP’s ownership model. Reject for this whole |
| **Mandatory checker or prompt compiler** | Could catch a small structural subset, but cannot establish action authority, factual correctness, actual reading, independence or usability. Reject as the default |
| **Automatic persistence rights or mode switching** | Conflicts with bounded authority and actual client controls. Reject |
| **Consumer fixes bundled with AP** | Couples protocol design to product/host operations and current state not inspected here. Defer to separately owned tasks |

No new checker is recommended. Header/enum/coordinate checks are suitable for bounded direct artifact inspection. A later tool proposal would require a distinct demonstrated mechanical defect, false-positive analysis, maintained integration boundary and focused behavioral tests.

Rollback is a separately authorized coherent documentation reversal, preserving the historical ADR and reports. Consumer rollback or adoption remains an independent pin-update task.

## 4. Fixed validation scenarios and practical-use proposal

The following eight scenarios are the complete initial acceptance matrix. They are **designed here, not executed against a changed candidate**.

“Generated artifact” means an actual constructed prompt/report specimen. It does not mean that a Worker performed its described actions.

| Scenario and input | Observable positive result | Negative result that must be prevented | Evidence owner/class | Proposed change tested |
|---|---|---|---|---|
| **V1 — Successful finishing:** source-read-only review, exact absent report destination, capable permitted writer, manual delivery | Complete report is saved and read back before notice; source remains unchanged; Cooperator handles only subsequent Git archival | Transcription assignment, premature terminal notice, ungranted META Git, incomplete report presented as saved | Worker tools: observed client/filesystem evidence; Cooperator: archival/effort feedback | Finishing example and Worker Reporting |
| **V2 — Unavailable delivery:** missing write grant, existing report including empty file, unsafe resolved destination, or native write prohibition | Preserve existing state and complete available content; report missing delivery honestly; route exact completion under renewed authority when required | Overwrite, alternate unauthorized path, permission bypass, reconstructed “exact” predecessor, second planning cycle | Reviewer: documentary/generated cases; actual client evidence only where observed | Early delivery checks, RF-19 projection and completion repair |
| **V3 — Source and validator limits:** report-ready notice without accessible exact bytes; valid doctor result paired with defective task authority | Reconciliation names the missing report claim; doctor evidence is confined to integration; useful work uses verified sources | Invented report verdict, memory substituted as source, integration PASS promoted to task compliance | Orchestrator: generated reconciliation; reviewer: exact source and CLI inspection | Evidence-reconciliation example |
| **V4 — Scope and prerequisites:** oversized assignment, reported context pressure, known missing installation, stale durable summary | Next grant has one useful outcome, justified reading, preserved accepted decisions and a satisfiable prerequisite route; state repair belongs to its existing owner | Another predictably blocked full audit, fabricated telemetry, restored planning budget, unauthorized documentation edits | Orchestrator: generated grant; reviewer: documentary/source comparison | Common composition contract, issuance consistency and slicing |
| **V5 — Action and expectation coherence:** one-start budget with required second invocation; build under blanket no-write prohibition; ambiguous stop; detached numeric value | Contradictions are corrected before issue; generated output scope is explicit; residual work is expressly bounded; expected values bind to object/source/readback | Silent reinterpretation, inferred additional invocation, build/report writes without authority, chmod to satisfy a wrong object | Reviewer: documentary and generated grant inspection | All three normative refinements |
| **V6 — Owner and recovery boundaries:** owner terminal can authenticate but Worker terminal cannot; accepted cutoff trial coexists with missing watchdog evidence | Privileged operation remains in the authorized owner session with complete output and release evidence; cutoff result preserves its accepted scope; watchdog stays open | Password sharing, assumed cross-session timestamp, passwordless-sudo prerequisite, cutoff promoted to watchdog PASS, optional hardware imposed on all progress | Product owner/Cooperator own actual operation evidence; AP acceptance checks generated routes and attributed source evidence | Owner-command routing and constraint-preserving examples |
| **V7 — Report identity:** BLOCKED/PARTIAL, duplicated coordinates, informal prefix, native fragment, interruption or late report | Standard report has the exact first line, one coordinate set, valid result spelling and honest delivery state; interruption stays distinct and separately owned | `BLOCKED`/`PARTIAL` used as phase-result enum, forged Worker report, history rewritten or companion silently replaced | Reviewer: generated artifact/readback inspection; Orchestrator: reconciliation | Report example and completion/identity projections |
| **V8 — Acceptance and publication:** exact candidate, fresh reviewer, later publication and stale product-state claims | Independence is established from actual separation; accepted commit is frozen; publication readback matches it; adoption and physical acceptance remain separate | Self-certification, accepting a changed artifact, automatic consumer update, implementation/test PASS promoted to installed or physical PASS | Fresh reviewer: acceptance evidence; publication Worker and Orchestrator: direct Git evidence | Preserved acceptance contracts and state-reconciliation example |

### Bounded observed use before practical-improvement claims

Include one harmless finishing rehearsal in the later fresh acceptance grant, using the acceptance exchange’s own actual terminal report as the observed successful delivery. This avoids a ceremonial Worker whose only purpose is copying a report.

Future fixture scope:

- Exact temporary directory: `/tmp/ap-reliable-execution-finishing-01`.
- Exact fixture files:
  - `input.md`, UTF-8/LF content: `AP finishing fixture v1\n`
  - `occupied-report.md`, UTF-8/LF content: `Preserve this existing fixture.\n`
- Require the directory to be absent and its physical parent verified before exclusive creation. A pre-existing directory blocks fixture creation; do not choose another path automatically.
- After preparation, treat `input.md` as immutable source. Record its hash before and after the read-only fixture task.
- Use `occupied-report.md` for the collision scenario; preserve its exact bytes. Generated negative-case decisions remain separately labelled from an actual client run.
- Remove only these two owned fixture files and the empty owned directory after evidence capture, before terminal reporting. Stop cleanup on unexpected replacement or additional entries; no recursive or wildcard deletion.
- The real acceptance report is written only to the exact META destination named by that future grant, after its separate identity/path/collision checks. It is retained and is not part of fixture cleanup.
- No services, devices, privileged commands, dependencies, provider calls, other projects or ContextDesk host operations are involved.

The future grant must explicitly authorize both fixture creation/cleanup and its real report preparation. Current governing AP and that grant supply authority; the candidate under review does not authorize its own use.

Practical evidence consists of the actual save operation, complete readback, source preservation, cleanup result and terminal receipt. Cooperator feedback should establish whether he had to transcribe the report or resolve an avoidable permission loop. One success supports only “the finishing route worked in this observed client/configuration.” It does not establish a failure-rate reduction, universal compatibility or time/token savings.

Native-mode blocking and missing-authority cases may remain documentary/generated evidence unless actually exercised under a separately valid route. Do not manufacture client observations to complete the matrix.

## 5. Bounded delivery and implementation slices

These are prospective boundaries, not current grants.

| Slice | Main result and exact owners | Dependencies | Acceptance evidence and stopping boundary |
|---|---|---|---|
| **0 — Complete this exchange’s file delivery** | Persist the exact supplied opening notes and this frozen report at the two named META paths; produce the completion exchange’s own report | Actual native mode OFF, complete renewed grant, available exact predecessor content, fresh path/collision checks | Exact full readback and hashes; preserve this report’s PARTIAL status. Stop after completion reporting; no replanning or AP edits |
| **1 — Produce one coherent AP documentation candidate** | Change only the eight AP paths listed in §2E; implement the three owner refinements, reorganized composition, operational examples and historical rationale | Orchestrator reconciliation, Michal’s design decision, explicit implementation grant, revalidated AP baseline and local state | Direct semantic/ownership review, V1–V8 documentary coverage, generated prompt/report specimens, changed-link/anchor inspection, whitespace/diff/allowlist checks; one reviewable candidate commit, no publication |
| **2 — Fresh independent acceptance** | Review the exact candidate and fixed owner/matrix package; include the explicitly granted harmless finishing rehearsal | Frozen candidate; genuinely fresh reviewer with no material implementation participation or inherited implementation conversation/reasoning | One primary acceptance; validate positive/negative cases and evidence-class separation. Stop with actual acceptance status; no corrective edits or publication |
| **3 — Publish the accepted artifact** | Publish exactly the accepted AP commit through a separately authorized normal fast-forward route | Independent acceptance, reconciled limitations, explicit publication authority and verified expected public parent | Direct public ref, commit/tree and content identity; stop at publication report. Consumer adoption and Orchestrator closure remain separate |

Slice 1 is cross-projection reversible documentation work, proposed as E2 with embedded preflight. Fresh independent acceptance is mandatory under AP’s semantic/structural-change rule regardless of the general tier. Expansion into privilege, runtime or broader authority changes ends this scope and requires a new risk decision.

Use the verified canonical AP checkout if it remains non-overlapping and clean. Do not require a worktree, branch switch or baseline cleanup merely for presentation.

A healthy current planning session may perform completion and later implementation under separate complete grants. Recommend reuse only while source provenance, accepted decisions and current state remain reconstructable. Rotate on actual context degradation or material assumption changes. Acceptance always uses the required fresh independent route.

For the next healthy same-session completion exchange, the expected routing is exchange 02 with META’s `_01` suffix; actual continuity and occupancy must be verified before issuance. Later coordinates follow real session transitions rather than being reserved by this plan.

If acceptance finds a concrete defect, use the existing one-correction boundary. A correction affecting semantic owners, authority/routing/convergence or exact structural fields requires full fresh acceptance. No audit-of-audit or automatic third equivalent blocker cycle is created.

## 6. Remaining decisions, limitations and frozen delivery

### Material decision

Michal’s remaining design choice is whether to adopt the recommended compact consolidation with three narrow normative clarifications, or restrict the change to examples alone.

**Recommendation:** adopt the consolidation. The additional precision targets reproduced ambiguity while retaining existing interfaces and authority boundaries. A full rewrite, checker, delivery change and consumer migration are outside the recommendation.

The design itself leaves no unresolved implementation alternative. Future grants must resolve mutable facts—actual session continuity, candidate identity, destination occupancy and client permission—at issuance.

### Exact completion requirements

The two missing predecessor artifacts remain:

1. `/home/agile/meta/projects/ap/08/01-ap-reliable-execution/00_notes.md`
2. `/home/agile/meta/projects/ap/08/01-ap-reliable-execution/01_report_00.md`

The opening-notes source is the exact fenced payload in the verified local `01_planning_00.md`, whose hash is recorded above. Its author remains ChatOrchestrator. A future persister must extract that payload without rewriting its conclusions, using UTF-8, LF and one final newline.

This complete standard report is the frozen report content within the client’s presentation wrapper. The wrapper itself is not report-file content. No stable downloadable artifact identifier is exposed, and no saved-report SHA-256 can truthfully be supplied.

A future completion grant must provide access to the exact terminal content, authorize the two predecessor files plus its own completion report, and prohibit replanning and implementation. If the exact terminal content cannot be recovered, preserve that limitation instead of reconstructing it as exact. The Cooperator is not assigned transcription.

A byte-identical prepared notes file may be reused after verification. Different notes require reconciliation. Any existing predecessor report blocks ordinary overwrite or append, even if empty. Completion does not retroactively change this report’s status.

### Validation limits and orchestration critique

This exchange establishes repository-grounded dispositions and an implementable proposal. It does not establish candidate acceptance, practical improvement, ContextDesk’s present state, deployment, publication, consumer adoption or closure.

D2-02’s underlying conversation and D2-04’s compaction observations remain attributed evidence. Historical host results remain Worker observations. No broad AP history audit, product certification, build, test suite or live fixture was performed.

```text
Orchestration critique:
MEASURED: Active native Plan Mode prohibits the task’s two requested file writes. The prompt correctly supplies a completion fallback. Effect: useful planning can finish, but direct file delivery cannot. Smallest completion action: one separately authorized persistence-only exchange with actual native mode OFF and exact predecessor content.
LEAD: Moving complete examples beside task composition and finishing may reduce grant omissions and Cooperator effort. This is unmeasured. Cheapest useful check: the fixed generated-artifact cases plus one bounded observed finishing run.
```

**Resolved Execution Issues / Near-Misses:** Some batched tool output was truncated; decision-relevant source sections were subsequently inspected in bounded excerpts. An initial filename query covered more META paths than necessary; subsequent content inspection remained restricted to the named causal sources. No historical commands were executed and no unrelated owner content was modified.

**Pre-Existing Failure Classification:** None claimed for runtime or test failures in this exchange; no such checks were run. Historical defects are attributed and dispositioned above rather than relabelled as newly observed failures.

The plan and standard report are complete in the permitted client output. Required file delivery remains incomplete. **This terminal report expires the current authority.**
