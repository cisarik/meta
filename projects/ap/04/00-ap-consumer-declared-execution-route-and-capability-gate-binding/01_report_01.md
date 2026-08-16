### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Standard terminal status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: all Worker 01 exchange 02 report-rendering authority expires at this terminal report
```

## 1. Repair identity

Frozen native planner artifact:

```text
Name: Route Binding Plan
Cursor plan file: route_binding_plan_a0714043.plan.md
Logical whole: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session: 01
Producing exchange: 01
This exchange: 02 (Planner Artifact Report Completion)
```

Session-continuity gate: this is the same concrete Worker 01 session that produced `Route Binding Plan`; the frozen artifact remains available without reconstruction; Native Plan Mode is disabled (`not-used`); no implementation or repository mutation occurred after the artifact froze; this exchange rendered the missing terminal report without commands or modifications.

Substantive frozen decisions were not changed. This exchange performed no re-planning, no plan amendment, and no new semantic, path, validator, or authority decision. Material omitted from the compact planner artifact below is report rendering of exchange-01 evidence and classifications, not a new plan.

## 2. Repository and evidence reconciliation from exchange 01

Inspection in exchange 01 used read-only Git/filesystem methods and credential-free `git ls-remote` of the three canonical public refs. Public objects for AP `95bd6448…` were already present locally (`git cat-file` / `git show`); no fetch, checkout, or other Git write was used.

### AP owner checkout

| Item | Exchange-01 observation |
|---|---|
| Physical root | `/home/agile/Projects/ap` |
| Origin fetch/push | `https://github.com/cisarik/ap.git` |
| Local `HEAD` | `041de310ea33ed1b47dd8f5fbfcc2829d1a32514` (`docs: converge ADR-0014 lifecycle status`) |
| Local tree | `a66b81d75d427a1d465bbfe76a890de1fd16aa52` |
| Branch | `refactor/retire-monolithic-ap-test-suite` (no upstream) |
| Tracked tree | clean |
| Root `AGENTS.md` | absent at local `HEAD` and at public `95bd6448…` (`AP.md` remains sole live semantic owner) |
| Classification vs public `main` | **behind**, not unpublished-ahead; merge-base with public is local `HEAD` |
| Public `refs/heads/main` | `95bd644829d48dcd188627f3e495e649df577eca` |
| Public tree | `9b895a1eaa95293f14964a756fa9f873e8c48a80` |
| Public subject | `docs: mark ADR-0017 accepted` |
| Commits on public not in local `HEAD` | `a1b04ff` continuation ledger; `17b7e08` ADR-0016 accepted; `1cd2783` cost-proportional grants; `95bd644` ADR-0017 accepted |
| Active rebase/merge/cherry-pick/revert/bisect/sequencer | none (`git status` clean; no `rebase-merge` / `rebase-apply`) |
| Stale leftover | `.git/REBASE_HEAD` dated 2026-07-28 pointing at `573975cffc5ce94c481553168abc040d4ad39557`; classified as leftover, not an active mutation |
| Unpublished overlapping owner work on candidate AP owners | none; local branch is an ancestor of public `main` |
| Planning inspection basis | public AP objects at `95bd6448…`, not the behind working tree |

### FrameNest consumer checkout

| Item | Exchange-01 observation |
|---|---|
| Physical root | `/home/agile/Projects/framenest` |
| Origin fetch/push | `https://github.com/cisarik/framenest.git` |
| Local `HEAD` / public `main` | `fc355d6e21d2f2781e0166906b453fa3fa91bdb7` (equal) |
| Tree | `00704b16a308ace5e349db1582691876e26dd613` |
| Parent | `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923` |
| Subject | `fix: bind Cursor Workers to declared AP exec and capability routes` |
| Branch | `fix/cursor-worker-execution-boundary` (no upstream) |
| Tracked tree | clean |
| Active Git mutation | none |
| Governing AP gitlink / `.ap` `HEAD` | `17b7e085139e9bcbb0e4953d26aef9b6687d541c` |
| Untracked remainder | owner untracked paths present; preserved; not enumerated |

### Meta selective checkout

| Item | Exchange-01 observation |
|---|---|
| Physical root | `/home/agile/meta` |
| Origin fetch/push | `https://github.com/cisarik/meta.git` |
| Local `HEAD` / public `main` | `dcba662e8aa7944df02bae6f057d472ddb05e036` (equal; `feat: add handout for consumer-declared execution-route and capability gate binding in AP`) |
| Orchestrator snapshot cited | `d316b675f761e3cad15a005140a5365dc36b9213` — one commit behind then-current public; local equalled current public |
| Named chain | all seven FrameNest execution-boundary files present |
| Worker Meta write | none |

### Ledger (discovered only from FrameNest root `AGENTS.md`)

```text
Upgrade ledger: upgrade https://github.com/cisarik/ap.git
Ledger storage version: 1
Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md
Activation snapshot: zero candidate observations at 17b7e085139e9bcbb0e4953d26aef9b6687d541c

Entry: consumer-declared-execution-and-capability-route-binding
Entry state: untriaged
Entry authority: non-authorizing
Summary: Consumer-declared AP exec and project SSH/sudo gates were bypassed by ambient raw Cursor Worker routes.
Evidence class: worker-observed
Observed against: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Last revalidated against: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Implementation task grant: none
Implementation status: not-started
Disposition evidence: none
Promotion target: none
Closure action: retain-active
Historical evidence: none
Provenance destroyed: no
```

Uniqueness: exactly one `Entry:` in the declared file. Required fields present once. Header matches the FrameNest `AGENTS.md` declaration. Not mutated.

### Evidence limitations (exchange 01)

- Non-independent planning evidence; no tests, `ap`, Python, NUC, or prompt-parser execution.
- Ledger `Last revalidated against` remained `5abb2adf…`; planning inspected later public AP/FrameNest identities without rewriting the ledger.
- Local AP checkout was behind public `main`; public meaning was taken from already-present objects at `95bd6448…`.
- Stale `REBASE_HEAD` leftover classified; not treated as an active rebase.
- Meta Orchestrator snapshot was stale by one public commit; named chain was still inspectable.
- Worker 01 did not inspect the entire Meta archive and did not treat Meta as live semantic authority.

## 3. Frozen verdict

```text
AP change required
```

Ledger mapping (recommendation only; ledger not mutated): the unique entry remains `untriaged` / `non-authorizing` until a separately authorized FrameNest task. After an authorized AP implementation and durable public AP evidence, the later consumer disposition is `accepted` then `implemented`. Not `duplicate`, `invalidated`, `parked`, or `rejected`.

**Why ADR-0017 is only partial overlap.** Public AP `95bd6448…` / `1cd2783…` added cost-proportional Worker grants, optional Development Envelope Activation (`not-used` \| `activated`), “reference declared project tooling or envelopes instead of recopying,” and compact-catalog anti-patterns. ADR-0017 explicitly rejected a FrameNest envelope in that whole, rejected executable/`ap`/schema change, and left envelope activation optional. It does not require the Orchestrator to resolve an applicable consumer-declared execution operation or capability gate before prompt issuance, does not forbid an equivalent-looking ambient raw command beside a declared route, and does not define bounded deviation lifecycle for that contradiction.

**Why not duplicate / invalidated / parked / rejected.** FrameNest public `fc355d6…` closed the consumer execution-boundary whole and left this observation `untriaged` as AP discovery input. Pin `17b7e085…` lacked even the ADR-0017 tooling-reference language. Current public AP still lets Common Worker Task Fields `Commands` authorize a raw interpreter/shell/SSH route; `ap exec` observes a declared operation only after the Worker actually invokes it. The observation remains a portable prompt-construction gap, not a FrameNest-only product rule, and Shape A stays inside the Complexity Budget.

## 4. Frozen semantic-owner map

`AP.md` remains the sole live semantic owner. No new RF family.

| Concern | Canonical owner | Structural | Operational | Advisory | Executable | Consumer | Historical |
|---|---|---|---|---|---|---|---|
| Capability vs authority vs ambient convenience | RF-06 in `AP.md` | capability handshake / side-effect fields already in `PROMPT_CONTRACTS.md` | `AP_ORCHESTRATOR.md`, `AP_WORKER.md` | P08 | none for prompt binding | project gates in consumer rules | ADR-0009 |
| Baseline-declared operations | RF-16 in `AP.md` | `ap.project.conf` schema v1 (unchanged) | `AP_ORCHESTRATOR.md` command authority | P08 tooling reference | `ap project check` / `ap exec` after invocation only | consumer `ap.project.conf` values | ADR-0012 |
| Prompt construction / command contradiction | RF-06 + RF-16 clarifications | existing `Commands`, positive/negative authority; **no new record** | Orchestrator prompt construction; Worker stop | P08 fixtures | none | `AGENTS.md` / project contracts name exact routes | ADR-0018 (proposed historical) |
| Optional development envelope | RF-06 / §5 (already) | Development Envelope Activation Record | `INTEGRATION.md` (default untouched) | P08 | none | optional `AGENTS.md` declaration | ADR-0017 |
| Protocol variant / consumer rules | RF-15 (unchanged; not retargeted) | managed block (forbidden to change) | `INTEGRATION.md` | — | `ap doctor` / `init` (forbidden to change) | consumer rules outside managed block | ADR-0013 |
| Docs-first validation | RF-07 / §12 | Validation Ladder (unchanged) | Worker validation | — | no AP suite | consumer tests remain consumer-owned | ADR-0015 |

**Contradictions and duplication risks established in exchange 01**

- Development envelope and `ap.project.conf` are separate: envelope is optional, prompt-activated, project-owned tooling/topology/reversible class; `ap.project.conf` is the closed schema-v1 operation/runtime contract enforced only when `ap exec` runs. Merging them would be a semantic error (Shape B risk).
- `AP.md` §5 makes the current prompt the only concrete task authority; consumer `AGENTS.md` is required reading and authoritative in its scope. An issued prompt can therefore silently authorize an ambient equivalent of a declared route unless prompt construction forbids it.
- Compact communication already says to reference declared tooling; that is permission/ergonomics, not a canonical-route or contradiction rule.
- `ap` does not construct or validate Worker prompts. Claiming executable enforcement without a prompt surface would violate “documentation must not claim enforcement that no validator observes.”
- Natural-language capability gates (SSH/sudo) are outside ADR-0012’s `ap.project.conf` scope; AP must not invent a schema for them.

## 5. Frozen implementation-shape decision

**Shape A selected:** refine existing RF-06/RF-16, Orchestrator prompt construction, command authority, and capability-gate guidance. Existing fields can express route identity and purpose (`Commands` / required reading), canonical use, contradictory-route prohibition (`Negative authority`), explicit bounded deviation in the prompt, and compatibility when no route exists.

**Shape B rejected:** a new structural record would duplicate Development Envelope Activation, `Commands`, side-effect authority, and capability-handshake fields; it is not required for decision-completeness.

**Shape C rejected:** current public AP does not own the complete invariant; FrameNest consumer docs do not make it universal; ADR-0017 is partial overlap only. Parking or rejecting would ignore still-open prompt-construction failure.

```text
Docs/projection only
```

No executable `ap` change; no new executable/conformance surface; no claim that `ap` will observe prompt contradiction.

## 6. Frozen implementation semantics

- **Applicability.** A consuming project has a usable declared route for the current task: a baseline-declared `ap.project.conf` operation, and/or a project-owned capability gate named in project rules. Absence of both is valid compatibility.
- **Pre-issuance resolution.** The Orchestrator resolves the governing AP baseline and any applicable consumer-declared route before issuing the prompt. Referencing is not enough when a usable route exists.
- **Canonical prompt behavior.** When that route exists and is usable, the prompt names it and treats it as canonical. Copied raw interpreter, shell, SSH, or reconstructed ambient commands must not appear as an equivalent parallel route.
- **Contradiction.** `Commands` / allowed-command examples cannot authorize a raw ambient equivalent beside the declared route unless an explicit bounded deviation is recorded.
- **Deviation.** Lawful only when the declared route is unavailable or unsuitable. The prompt records the declared route, exact alternate path, rationale, evidence class, bounded authority, and stop condition. A deviation is not a second standing canonical route.
- **Unusable/missing route.** Stop or use exact project-owned guidance. AP does not invent a toolchain.
- **Ambient state.** IDE, terminal, login shell, inherited variable, retained socket, editor, or prior Worker session is convenience state, not authority or guaranteed capability.
- **Separation.** Role, capability, credentials, privilege, technical reachability, task authority, containment, and evidence remain separate (RF-06). An ambient-environment failure is classified before remediation; when a declared sanitized route applies, one focused reproduction through it is preferred; environment repair or substitution needs separate authority.
- **Documented-only / no-route consumers.** Remain compatible. Fallback is exact project-owned guidance, not AP-invented operations or an implied development envelope.
- **Historical pins.** Existing pins and historical prompts retain original meaning. Consumer adoption of newer AP remains a separate task. FrameNest continues under `17b7e085…` until a later pin-adoption whole.
- **Stopping.** Worker stops on unresolved prompt-versus-declared-route contradiction; on missing required capability after classification; and does not reconstruct an ambient route to force PASS.

Development Envelope Activation may remain `not-used` when a usable machine-readable `ap.project.conf` route exists: they are different declarations. Envelope `not-used` does not waive RF-16 operation binding or a project-owned capability gate.

## 7. Exact proposed implementation allowlist and forbidden paths

Preserve the frozen allowlist. Do not enlarge it.

**Semantic owner (1)**

- `AP.md` — RF-06, RF-16, §5, prompt-synthesis readiness, Compact Communication, stopping conditions, anti-patterns

**Operational/structural projections (4)**

- `AP_ORCHESTRATOR.md` — prompt construction and command authority
- `AP_WORKER.md` — contradiction stop and ambient classification
- `PROMPT_CONTRACTS.md` — `Commands` / positive/negative authority purpose text only; no new record
- `PROMPT_ENGINEERING_PATTERNS.md` — P08 generic positive example and parallel-raw negative fixture; no FrameNest names

**Historical**

- `CHANGELOG.md`
- new `docs/adr/0018-consumer-declared-execution-route-binding.md`
- `docs/adr/README.md`

**Default-untouched projections** (do not edit unless a later independent review proves inconsistency; frozen default is untouched): `INTEGRATION.md`, `README.md`, `FAQ.md`, `GLOSSARY.md`, `ARTIFACT_LIFECYCLE.md`, `INFOSEC.md`, `UPDATING.md`.

**Forbidden**

- executable `ap`
- `ap.project.conf` / schema version
- managed `AGENTS.md` block
- new RF family, new universal command, new structural annex/record
- AP `tests/` or any new conformance/CI suite
- FrameNest, Meta, consumer pin, NUC, credentials, environment repair, product work

## 8. Verification and lifecycle

Later implementation verification (docs/projection only; no AP suite):

| Changed owner | Direct semantic review | Projection/relationship | Structural spelling | Examples |
|---|---|---|---|---|
| `AP.md` RF-06/RF-16 | required | map vs projections | no new fields | positive canonical route; parallel-raw negative; explicit deviation; no-route compatibility |
| `AP_ORCHESTRATOR.md` | required | prompt-construction duty | n/a | pre-issuance resolution |
| `AP_WORKER.md` | required | stop/classify | n/a | ambient failure then one declared-route rerun |
| `PROMPT_CONTRACTS.md` | required | `Commands` purpose only | exact existing field names unchanged as identifiers | contradiction prohibition in purpose text |
| P08 | advisory review | must not become a second owner | fixture shape | generic negative parallel-raw |
| ADR-0018 / CHANGELOG / adr README | historical consistency | non-retroactivity | n/a | pin `17b7e085…` retains original meaning |

Also: link/path/Git evidence on the allowlist; historical pin/non-retroactivity check; no focused executable AP evidence because executable behavior does not change.

**Lifecycle after plan approval (no authority now)**

1. New complete implementation prompt with `Native planning mode: not-used`.
2. One fresh Implementation Worker and one initial implementation attempt on the frozen allowlist.
3. Bounded correction only for one concrete classified defect.
4. Fresh independent acceptance.
5. Correction re-acceptance only if needed under existing scoped-reacceptance rules.
6. Explicit AP publication gate and credential-free public `refs/heads/main` readback.
7. **AP closure after publication and required acceptance**, with no FrameNest mutation in the AP whole (matches ADR-0016/0017: consumer adoption and AP logical-whole closure remain separate).
8. Later separately authorized FrameNest ledger transition to `implemented` using the durable public AP SHA as disposition evidence.
9. Later separate FrameNest AP-pin adoption whole only if the Cooperator selects it.
10. No automatic NUC deployment or product work.

## 9. Rollback, residual risks, and Complexity Budget

Frozen posture is docs/projection only, so rollback is Git-level revert of the published documentation commit on AP; no runtime, schema, or consumer pin to roll back. Projection inconsistency is recovered by reconciling subordinates to `AP.md`, not by adding a validator. Historical prompts and non-adopting consumers keep pin meaning.

Residual risks already classified in exchange 01 (not new decisions):

- Documentation-only enforcement cannot mechanically stop a Worker who follows an issued contradictory prompt; the contract binds Orchestrator construction and Worker stop rules.
- Executable prompt validation would parse wording and was rejected (ADR-0015; no prompt surface on `ap`).
- Natural-language capability gates remain project-owned and can stay ambiguous if the consumer does not name them.
- Poorly written deviation text could become a standing second route; the frozen anti-pattern is that a deviation must not become permanently canonical.
- Overfitting to FrameNest is avoided by generic route/gate language and by forbidding FrameNest examples in AP files.

```text
Canonical semantic owner files: 1
Existing RF families touched: at most 2
Operational/structural projection files: at most 4
New ADRs: at most 1
Executable surfaces changed: 0
New executable/conformance mechanisms: 0
Consumer repositories changed: 0
Managed blocks changed: 0
Schema versions changed: 0
New universal commands: 0
Plan-only cycles: exactly 1
Implementation attempts before classified correction: 1
Fresh independent acceptance Workers after implementation: 1
```

## 10. Mutation statement

Worker 01 exchange 01 performed read-only inspection and created the native planner artifact `Route Binding Plan` (Cursor plan file `route_binding_plan_a0714043.plan.md`). It did not modify AP, FrameNest, or Meta repository files, indexes, refs, the FrameNest ledger, the AP pin, environment, credentials, host, NUC, or production state.

Worker 01 exchange 02 performed no commands and no writes. The frozen artifact was not amended.

No file, index, ref, repository, ledger, Meta artifact, pin, environment, credential, host, NUC, or production state was changed by this Worker during exchanges 01–02 in AP, FrameNest, or Meta.

## 11. Smallest next step

Orchestrator review of the frozen `Route Binding Plan` and this terminal report.

Plan acceptance would still grant **no implementation authority**. Implementation requires a new complete Orchestrator prompt with `Native planning mode: not-used`, a fresh Worker session, and explicit implementation authority.

Near-miss / pre-existing classification from exchange 01: stale AP `.git/REBASE_HEAD` leftover (not an active rebase); local AP checkout behind public `main` with public objects still inspectable; Meta public one commit newer than the Orchestrator snapshot; FrameNest owner untracked paths preserved and not enumerated. None required a planning `BLOCKED`.

```text
Authority expiry: all Worker 01 exchange 02 report-rendering authority expires at this terminal report
```