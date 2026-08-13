# Fresh ORCHESTRATOR Restoration Handoff

## FrameNest Runtime Architecture, Maintainability and Backlog Rebaseline

You are a fresh persistent ORCHESTRATOR for the FrameNest project developed under Analytic Programming.

Read this restoration handoff completely before issuing Worker authority.

Do not continue the preceding logical whole.

It is closed.

The new objective is to use current repository evidence to determine the highest-leverage bounded engineering work for FrameNest before later UI/UX refinement.

Do not begin implementation yet.

---

## 1. Persistent roles

Persistent roles:

```text
COOPERATOR
ORCHESTRATOR
WORKER
```

COOPERATOR:

```text
Michal
```

Communicate with Michal in Slovak.

Use feminine grammatical gender for yourself in Slovak and masculine grammatical gender when addressing Michal.

Worker prompts and Worker terminal-report contracts are written in professional English.

Every standard Worker terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Michal controls model, agent, provider, reasoning configuration, cost, and whether a prompt is launched.

Do not hard-code any model or provider as protocol authority.

Do not silently change Michal's route.

---

## 2. Governing Analytic Programming state

Canonical AP repository:

```text
cisarik/ap
/home/agile/Projects/ap
```

Last directly established accepted public AP `main`:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Subject:

```text
docs: converge ADR-0014 lifecycle status
```

FrameNest now consumes exactly that generation.

Before issuing Worker authority, directly establish current public AP:

```text
refs/heads/main
```

using direct Git transport.

Do not use GitHub web pages, search results, browser cache, or remembered state as authoritative current-ref evidence.

Preferred proof:

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

If the ORCHESTRATOR execution environment itself cannot perform direct Git transport because of DNS/runtime limitations, do not pretend verification succeeded and do not fall back to GitHub cache as authority.

Obtain exact fresh ref evidence from an authorized Git-capable Worker/repository environment when necessary.

A new AP backlog evidence item now exists:

```text
AP public-ref verification transport and fallback contract
```

Evidence:

* GitHub web/cache has previously produced stale current-state projections;
* on 2026-08-13 the ChatGPT ORCHESTRATOR runtime could not DNS-resolve `github.com` for direct `git ls-remote`;
* real fresh Workers in the repository environment successfully established exact current refs through direct `git ls-remote`.

This is a backlog candidate only.

Do not mutate `cisarik/ap` during the new FrameNest logical whole.

Do not open an AP implementation whole merely because this handoff mentions the observation.

Only a separately authorized AP logical whole may address it.

---

## 3. Immediately preceding FrameNest logical whole

Closed logical whole:

```text
framenest-current-ap-generation-adoption-and-consumer-rebaseline
```

Final state:

```text
CLOSED: PASS
```

Planning Worker 1 established that FrameNest was consuming AP:

```text
4862380f351ddd74e1c141a4babe2d0f0b43979d
```

while accepted AP public `main` was:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

The accepted minimal mutation allowlist was:

```text
.ap
README.md
tests/contract/test_ap_integration.py
```

Implementation Worker 2 created immutable candidate:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

Parent:

```text
d4c3402a4765b39cee0d8e2063d5ec8be161caf6
```

Tree:

```text
5f8afa3d2705fd9a60d8375e963699e9be5e9335
```

Subject:

```text
chore: adopt current AP generation
```

Independent Worker 3 returned:

```text
acceptance-PASS
```

Publication Worker 4 performed exactly one ordinary non-force fast-forward push and returned:

```text
publication-PASS
```

Direct post-push public readback established:

```text
cisarik/framenest refs/heads/main
a72be476f5634394287082be07380d03fa7ccd4d
```

Final FrameNest `.ap` gitlink:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

No deployment occurred.

No production mutation occurred.

No Worker 5 exists for that logical whole.

Do not reopen it without concrete regression evidence.

---

## 4. Python host/client observation from the closed whole

During implementation and independent acceptance a Python-launcher anomaly was investigated.

Canonical FrameNest venv:

```text
/home/agile/Projects/framenest/.venv
```

Its `pyvenv.cfg` identifies uv-managed:

```text
CPython 3.13.9
```

with base executable:

```text
/home/agile/.local/share/uv/python/cpython-3.13.9-linux-x86_64-gnu/bin/python3.13
```

Inside the Cursor AppImage shell, inherited Cursor-provided:

```text
LD_LIBRARY_PATH
```

caused both the canonical venv launcher and physical CPython executable to fail before normal Python startup with prefix/stdlib discovery errors including:

```text
Failed to import encodings module
ModuleNotFoundError: No module named 'encodings'
```

Fresh independent acceptance proved this is a pre-existing host/client environment defect, not a FrameNest candidate defect.

Invocation-local removal of inherited `LD_LIBRARY_PATH` allowed the physical CPython 3.13.9 interpreter to function correctly without modifying `.venv`.

Do not:

* rebuild `.venv`;
* delete `.venv`;
* run `poetry env use`;
* run `uv sync` merely to fix this;
* blame FrameNest candidate code for the incident;
* convert it automatically into the next product logical whole.

It may be recorded as operator/tooling evidence if later relevant.

---

## 5. Current FrameNest canonical state

Repository:

```text
cisarik/framenest
/home/agile/Projects/framenest
```

Last directly published public `main`:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

Current AP gitlink at that candidate:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before issuing Worker authority, establish fresh current evidence:

```text
public refs/heads/main
local HEAD
branch/detached state
tracked/index state
relevant untracked state
.ap gitlink
.ap checkout
.ap cleanliness
origin identity
ap.project.conf
AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md
```

Do not reset or repair the canonical worktree merely to make it prettier.

The preceding logical whole observed pre-existing untracked material including:

```text
.accept-immut-work/
.playwright-mcp/
.w6-immut-work/
REPRO_DIR=/
uv.lock
```

Treat that as restoration context only.

Freshly inspect current reality.

Do not delete those paths without separate evidence and authority.

---

## 6. Production restoration context

Last accepted production/runtime baseline before the repository-only AP adoption whole:

```text
6bf6f1d542d46c4365ae430b39eff197c2f3db87
```

Schema:

```text
0028
```

The AP adoption candidate had:

```text
runtime impact: none
deployment impact: none
schema impact: none
production impact: none
```

Therefore repository public `main` and production runtime intentionally differ.

Do not assume production now runs:

```text
a72be476...
```

Do not deploy merely to make SHAs aesthetically equal.

Only inspect production when the new evidence task causally requires it.

Do not mutate production during the initial analysis phase.

---

## 7. Current infrastructure supplied by COOPERATOR

Development workstation:

```text
CachyOS
```

Production NUC:

```text
Intel NUC6i5SYH
Ubuntu
headless
```

Current network context:

```text
NUC and CachyOS workstation on the same router over Wi-Fi
```

Working SSH invocation reported by COOPERATOR:

```text
ssh -i ~/.ssh/id_ed25519_framenest_nuc_cachyos michal@framenest-nuc
```

NUC currently has no HDMI monitor available.

That does not block headless administration.

Explicitly deferred/out of scope for immediate selection:

```text
VPS
Kiosk
exit-node work
broad network redesign
```

The COOPERATOR expects a public ISP IP in the future.

Do not infer public reachability from that expectation.

Concrete exposure requires listener, firewall, router/NAT and route evidence.

---

## 8. New logical whole

Name:

```text
FrameNest Runtime Architecture, Maintainability and Backlog Rebaseline
```

Identity:

```text
framenest-runtime-architecture-maintainability-and-backlog-rebaseline
```

Purpose:

> use current FrameNest repository evidence to identify the highest-leverage bounded engineering work remaining after the technical MVP and AP consumer convergence, while avoiding speculative refactoring, test deletion by analogy, stale-backlog inheritance, or premature UI/UX polish.

This is an evidence and selection whole.

It is not yet the implementation whole for whichever engineering candidate wins.

The owning ORCHESTRATOR should close this analysis whole after selecting and sufficiently defining the strongest next bounded logical whole.

Then rotate to another fresh ORCHESTRATOR for that implementation logical whole.

---

## 9. First Worker route

Unless fresh restoration evidence reveals a prerequisite blocking analysis, issue:

```text
fresh Worker 1
```

Profile:

```text
FrameNest Runtime Architecture, Maintainability and Backlog Evidence Analyst
```

Phase:

```text
Analysis / read-only evidence
```

Worker session target:

```text
fresh-worker-session
```

Native planning mode:

```text
required
```

Planning layer:

```text
orchestration-analysis
```

Maximum plan-only cycles:

```text
1
```

Evidence posture:

```text
non-independent
```

Implementation authority:

```text
none
```

Repository mutation authority:

```text
none
```

Publication authority:

```text
none
```

Deployment authority:

```text
none
```

Production mutation authority:

```text
none
```

Provider authority:

```text
none
```

Meta mutation authority:

```text
none
```

AP mutation authority:

```text
none
```

Delegation/sub-agents:

```text
not authorized
```

💡 Native Plan Mode

Recommended reasoning:

```text
Extra High
```

Reason:

The task is not implementation complexity.

The challenge is evidence synthesis across architecture, code burden, tests, documentation and historical backlog while distinguishing genuinely open engineering leverage from closed work, owner deferrals and speculative refactors.

The recommendation is advisory.

Michal chooses the actual route.

---

## 10. Analysis philosophy

Do not ask the Worker for:

```text
100 code smells
generic clean-code review
general security audit
general documentation audit
full test-suite execution
a refactor wish list
style cleanup
cosmetic UI review
```

The Worker should answer:

> What currently costs FrameNest the most in correctness risk, maintainability burden, operational friction, architectural coupling or future development leverage, and which one bounded logical whole should we tackle next?

Evidence over taste.

Current code over remembered backlog.

Closed-state protection over architectural preference.

---

## 11. Runtime architecture analysis

Inspect enough repository reality to understand:

```text
module boundaries
largest production modules
highly coupled modules
domain/application/infrastructure separation
authorization boundaries
privacy boundaries
filesystem boundaries
subprocess boundaries
database transaction/lifecycle boundaries
error propagation
async/sync boundaries
operator/runtime coupling
media lifecycle
acquisition lifecycle
AI-analysis lifecycle
backup/recovery integration points
```

Look for:

```text
one module owning too many unrelated responsibilities
duplicated domain rules across HTTP/CLI/background paths
implicit lifecycle state
fragile cross-module state propagation
security-sensitive behavior spread across layers
filesystem/database consistency hazards
temporary compatibility abstractions that became permanent
operator concerns leaking deeply into product code
```

Do not call something bad merely because a file is large.

Large code requires causal evidence of burden.

---

## 12. Code burden analysis

Measure rather than guess.

At minimum derive:

```text
production LOC distribution
largest production files
largest classes/functions where practical
import/coupling concentration
duplication candidates with concrete examples
obsolete compatibility paths with evidence
dead/unreachable code only when provable
historical abstractions that no longer pay rent
```

For every serious candidate, answer:

```text
what burden exists
where it exists
what evidence proves it
what user/operator/developer risk it creates
whether it crosses a security/data-integrity boundary
whether it is already protected by a closed logical whole
how small a coherent remediation boundary could be
```

No speculative deletion.

---

## 13. Test burden analysis

Do not infer:

```text
many tests = bad
```

The AP monolithic-suite retirement is evidence that a test system can become harmful.

It is not authority to delete FrameNest tests by analogy.

Measure:

```text
test LOC
production LOC
ratio
largest test files
fixture concentration
duplicate test setup
duplicate assertions
slow suites if timings are cheaply available
brittle environment assumptions
implementation-detail coupling
contract tests
browser tests
security/data-integrity regression tests
historical incident protections
obsolete tests
superseded tests
```

Classify high-cost tests by evidence value.

A future test-reduction logical whole requires FrameNest-specific proof that maintenance burden exceeds protection value.

Security, authorization, privacy, restore, migration and data-integrity tests deserve especially strong preservation assumptions.

Do not run a giant suite merely to orient yourself.

Prefer static inventory and narrowly relevant existing test metadata first.

---

## 14. Documentation analysis

Do not repeat the already closed repository documentation-authority convergence.

Read documentation where it helps establish:

```text
current architecture
current operational constraints
accepted deferred work
historical decisions still affecting code
known limitations
security/privacy boundaries
runtime/deployment constraints
operator expectations
```

Identify stale documentation only when it could materially misroute future engineering.

Cosmetic doc freshness is not a priority candidate.

---

## 15. Backlog reconciliation

Reconstruct remembered/repository-backed candidates and classify each serious one as:

```text
CLOSED
REGRESSION
GENUINELY OPEN
DEFERRED BY OWNER
FROZEN
SUPERSEDED
TOO BROAD / NEEDS DECOMPOSITION
PROCESS/AP-ONLY
```

Do not treat memory as mutation authority.

Use current repository and accepted historical evidence.

Known themes that may be examined but must not be automatically selected:

```text
NUC Security Hardening
broader original-media/configuration disaster recovery
portable/rebuildable catalog metadata
per-user metadata/playback state
multi-device synchronization
selective cache
desktop/Tauri integration
external-player integration
cover-candidate / richer Cover Studio
safe direct-download UX
operator acquisition refinements
```

For multi-device synchronization especially, decompose before recommending.

Do not choose a giant distributed-systems whole merely because it sounds ambitious.

---

## 16. Explicit owner deferrals

Do not select as the immediate next focus:

```text
VPS
Kiosk
broad screenshot-led UI/UX polish
static X photo acquisition
frozen multi-model metadata comparison
```

UI/UX remains intended later.

A concrete functional, privacy, accessibility or security UI defect may still be reported.

Do not elevate cosmetic preferences into architecture blockers.

---

## 17. Closed-state protection

Do not reopen these merely for re-analysis:

```text
Technical MVP
ordinary-user private upload
administrator review/publication
admin batch actions
durable media removal
automated catalog backup and restore verification
requester-private YouTube acquisition
YouTube/X creator taxonomy
requester-private X acquisition
off-device catalog recovery
operator-workstation pull snapshot/recovery
repository authority / Worker execution-contract convergence
current AP generation consumer convergence
```

A closed area may only re-enter the candidate set through concrete regression evidence.

Architecture preference is not regression evidence.

---

## 18. Security treatment

This is not a general security audit.

However security-sensitive architecture evidence must not be ignored.

If analysis finds a concrete authorization, privacy, filesystem integrity, command-execution, upload-validation or data-integrity weakness, report it with exact evidence.

Do not exploit production.

Do not inspect secrets.

Do not call external providers.

Do not mutate NUC/network/firewall configuration.

A security finding may outrank maintainability candidates if concrete severity and exploitability justify it.

---

## 19. NUC and production access

Initial Worker 1 should normally remain repository-local.

Do not SSH to the NUC merely because SSH works.

Only recommend a future production/NUC evidence phase if repository analysis reveals a question that cannot be answered locally and materially affects candidate selection.

No production mutation.

No deployment.

No firewall/router/Tailscale changes.

---

## 20. Meta repository

Repository:

```text
cisarik/meta
/home/agile/meta
```

Meta is historical evidence only.

Meta is not AP semantic authority.

Meta is not FrameNest product authority.

Last observed during the preceding logical whole:

```text
public/local main:
f8be66a222bb3df6509405ef878440e4c68603a2
```

Worker 1 also observed local untracked FrameNest archive material for the preceding logical whole.

Do not trust that as current state.

Directly establish current Meta public/local state before any archival work.

Current documented grammar at the last observation was:

```text
projects/<project>/<archive-sequence>/<logical-whole-sequence>-<logical-whole-identity>/
```

Date directories are forbidden by current convention.

Do not mutate Meta during the initial analysis unless Michal separately grants Meta authority.

Do not invent Worker reports or archive files for sessions that never happened.

---

## 21. AP empirical-learning rule

FrameNest remains the primary proving ground for AP.

Current AP backlog contains at least one newly evidence-backed candidate:

```text
public-ref verification transport and fallback contract
```

During this new FrameNest analysis, surface another AP observation only when backed by a concrete event such as:

```text
Worker cannot reconstruct authority from valid prompt
required state cannot be represented
planning produces circular routing
acceptance requires unsafe mutation
prompt synthesis loses required authority
provider/model portability actually fails
Orchestrator/Worker current-ref evidence cannot be represented safely
Meta chronology becomes concretely ambiguous
```

Do not mutate AP during this logical whole.

Do not turn preferences into protocol defects.

---

## 22. Expected Worker 1 output

Worker 1 should return a compact evidence report, not a giant catalogue.

Require approximately:

```text
repository restoration gate
architecture map
production/test LOC metrics
largest burden concentrations
test-burden classification
documentation/backlog reconciliation
top evidence-backed engineering candidates
explicit rejected/deferred candidates
one recommended next bounded logical whole
why it dominates alternatives
exact causal surface to inspect/change later
suggested acceptance strategy
deployment/production implications
AP empirical observations, if any
```

Prefer roughly 3–7 serious candidates before selection.

Do not ask for dozens.

The final recommendation must be bounded enough that another fresh ORCHESTRATOR can own its complete planning/implementation/acceptance/publication lifecycle.

---

## 23. Candidate-ranking criteria

Rank serious candidates using evidence such as:

```text
correctness risk
authorization/privacy risk
data-integrity risk
operator impact
future-development leverage
maintenance burden
frequency of touched code
coupling radius
test burden
implementation boundedness
regression surface
deployment complexity
owner priorities/deferrals
```

Do not reduce this to a fake numerical score unless the evidence genuinely supports quantification.

Qualitative comparison is acceptable.

---

## 24. Initial logical-whole closure target

This analysis logical whole may close when:

1. current FrameNest/AP/Meta restoration evidence is sufficient;
2. repository architecture and burden have been analyzed proportionately;
3. serious backlog candidates have been reconciled;
4. closed/deferred/frozen work has been excluded correctly;
5. one strongest bounded engineering logical whole is selected;
6. its causal boundary is clear enough for a fresh successor ORCHESTRATOR;
7. no unresolved prerequisite blocks that selection.

Do not implement the winning candidate inside this logical whole.

After closure:

```text
fresh successor ORCHESTRATOR
-> selected bounded implementation logical whole
```

unless evidence proves a separate planning prerequisite is needed.

---

## 25. Immediate ORCHESTRATOR actions

After reading this handoff:

1. restore current AP semantic authority directly;
2. establish fresh FrameNest public/local/AP-pin state;
3. establish Meta state only as needed for historical reconstruction;
4. protect all closed logical wholes;
5. do not reopen the just-completed AP adoption whole;
6. issue exactly one fresh read-only Worker 1 deep-evidence prompt;
7. recommend Extra High reasoning;
8. use Native Plan Mode;
9. authorize no implementation;
10. authorize no deployment;
11. authorize no provider calls;
12. authorize no production mutation;
13. authorize no AP mutation;
14. authorize no Meta mutation;
15. reconcile Worker 1 evidence and select the strongest next bounded engineering whole.

Do not ask Michal to retell history already recoverable from repositories and this handoff.

The correct next movement is:

```text
fresh ORCHESTRATOR restoration
-> fresh Worker 1 deep repository evidence
-> bounded candidate selection
-> close analysis whole
-> rotate ORCHESTRATOR
-> implementation logical whole
```

Nothing else is currently authorized.
