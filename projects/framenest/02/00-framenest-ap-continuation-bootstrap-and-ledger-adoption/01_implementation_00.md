# WORKER 01 / EXCHANGE 01 — IMPLEMENTATION

## Role and session contract

You are **Worker session 01, exchange 01** for the FrameNest logical whole:

`framenest-ap-continuation-bootstrap-and-ledger-adoption`

Session target: **fresh-worker-session**
Native planning mode: **not-used**

This is an **implementation Worker**, not an Orchestrator and not a planning Worker.

Work from:

```text
/home/agile/Projects/framenest
```

Begin **strictly read-only**.

Do not inherit mutation assumptions, repository state, unpublished branches, worktrees, conclusions, or authority from any prior Worker session. Reconstruct the relevant state yourself from the repository, the pinned AP generation, and direct public Git evidence.

The Cooperator has selected this logical whole. You have bounded implementation authority only after the mandatory read-only preflight below succeeds.

---

# 1. Governing objective

Adopt the published Analytic Programming generation:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

into FrameNest and make the **smallest project-local activation** necessary to exercise:

1. the new AP **Continuation Bootstrap**, and
2. AP's optional **durable upgrade-ledger storage projection**.

The implementation must leave FrameNest prepared for a later, genuinely fresh Orchestrator restoration test.

That restoration test is **not part of this Worker session**. It will occur only after:

1. this implementation produces an exact candidate,
2. a fresh independent Worker acceptance-PASSes that candidate,
3. a separately authorized Worker publishes it by ordinary non-force push,
4. direct public readback confirms the accepted FrameNest commit.

Do not attempt to simulate, substitute for, or prematurely perform that later fresh-Orchestrator test.

---

# 2. Cooperator-selected authoritative public baseline

The Cooperator independently obtained credential-free direct Git readback establishing:

```text
FrameNest refs/heads/main =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

AP refs/heads/main =
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

The older FrameNest commit:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

is **not** the current FrameNest public-main baseline and MUST NOT be treated as such.

You must independently re-read both public refs before mutation.

Repository identities expected for direct credential-free verification:

```text
https://github.com/cisarik/framenest.git
https://github.com/cisarik/ap.git
```

---

# 3. Governing documents

Before mutation, read and obey the FrameNest root:

```text
AGENTS.md
```

Then inspect the currently pinned `.ap` state and read the governing AP documents required by that generation, including at minimum the applicable forms of:

```text
.ap/AP.md
.ap/AP_ORCHESTRATOR.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
.ap/INTEGRATION.md
```

Read any directly referenced AP document needed to interpret this task correctly.

The existing root `AGENTS.md`, together with the pinned AP documents, governs this Worker until the target AP candidate is inspected.

After the preflight passes and obtaining the target AP object is authorized, inspect the same relevant documents **at exact AP commit**:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

before writing the project-local ledger declaration or ledger file.

Do **not** invent ledger syntax, header fields, activation-snapshot semantics, target identity syntax, or continuation behavior from this prompt when the target AP generation specifies them more precisely.

The exact target AP documents are normative for the new functionality being adopted.

---

# 4. Mandatory fail-closed read-only preflight

No repository mutation of any kind is permitted until this section succeeds.

Inspect the real repository at:

```text
/home/agile/Projects/framenest
```

At minimum establish and record:

* repository root identity;
* current branch or detached-HEAD state;
* exact local `HEAD`;
* `git status --short` / equivalent porcelain state;
* all pre-existing owner changes, including tracked, staged, untracked, ignored-if-material, submodule, or worktree-relevant state;
* whether the working tree is suitable for this bounded implementation without overwriting or contaminating owner work;
* exact `.ap` gitlink recorded by current FrameNest `HEAD`;
* whether `.ap` is initialized;
* exact `.ap` checked-out commit;
* whether `.ap` itself is clean;
* `.gitmodules` identity/configuration relevant to `.ap`;
* current project references to the pinned AP SHA, especially:

  * `README.md`;
  * `tests/contract/test_ap_integration.py`;
* the root `AGENTS.md` managed AP block boundaries and project-owned content around them;
* credential-free direct public `refs/heads/main` for both FrameNest and AP.

Use read-only Git operations for this phase.

Expected public refs are exactly:

```text
FrameNest main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

AP main:
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Determine the actual current FrameNest AP gitlink from the repository rather than assuming it from older reports.

### Fail-closed rule

If there is any **material discrepancy** from the selected logical-whole assumptions, STOP without mutation and report `BLOCKED`.

Material discrepancies include, but are not limited to:

* public FrameNest `main` is no longer `230ce43a...`;
* public AP `main` is no longer `17b7e085...`;
* local FrameNest state cannot be reconciled safely with public `230ce43a...`;
* the current `.ap` gitlink differs materially from the expected adoption starting point;
* `.ap` is uninitialized, corrupted, unexpectedly dirty, or points somewhere inconsistent with project integration;
* owner changes overlap the authorized mutation paths;
* owner changes would be overwritten, staged accidentally, obscured, or made difficult to distinguish from this logical whole;
* root `AGENTS.md` structure differs such that its managed AP block cannot be preserved byte-for-byte;
* project integration has materially changed so that the selected allowlist is no longer sufficient;
* target AP documents materially contradict the selected implementation boundary.

Do not "repair around" a material discrepancy.

Do not silently broaden scope.

Do not reset, stash, clean, checkout over, discard, rewrite, or otherwise alter owner changes.

If unrelated owner changes exist but can demonstrably remain completely untouched and cannot contaminate the candidate, classify them explicitly and proceed only if doing so remains unambiguous and safe under the governing repository/AP rules. Otherwise fail closed.

---

# 5. Mutation authority

Only after the complete preflight passes, implementation mutation authority activates.

The **entire authorized project mutation allowlist** is:

```text
.ap
AGENTS.md
README.md
tests/contract/test_ap_integration.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

No other project path may be modified.

Within `.ap`, the intended change is only adoption of the exact published AP commit through the existing Git-submodule integration. Do not author independent modifications to AP source files.

You may perform the minimum Git operations required to obtain the target AP object, move the existing `.ap` submodule to the exact target commit, inspect it, stage the authorized candidate, validate it, and create one bounded implementation candidate commit if validation passes.

This authority includes **candidate commit creation**.

It does **not** include publication.

Forbidden unless a later Orchestrator explicitly grants separate authority:

* `git push`;
* force push;
* remote branch publication;
* merge;
* rebase;
* squash;
* tag publication;
* deployment;
* production mutation;
* NUC mutation;
* Tailscale/network mutation;
* provider mutation;
* database/schema migration;
* Meta repository mutation.

Do not amend or rewrite unrelated historical commits.

---

# 6. Exact implementation boundary

Implement the smallest coherent adoption slice.

## 6.1 `.ap`

Update the existing FrameNest `.ap` gitlink to exactly:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Requirements:

* use the existing submodule architecture;
* preserve its canonical repository identity unless the current repository evidence proves an authorized convergence is already required;
* do not modify target AP source content;
* do not use an arbitrary branch tip instead of the exact SHA;
* candidate gitlink must resolve exactly to `17b7e085...`.

Do not run a broad or destructive AP reinitialization merely to accomplish the pin update.

In particular, do not use `ap init` merely to activate the optional ledger if the target AP integration contract says project-local activation belongs outside the managed block.

## 6.2 `AGENTS.md`

The current managed AP block in FrameNest root `AGENTS.md` must remain:

**byte-for-byte unchanged.**

Before editing, capture sufficient evidence to prove its exact original byte content and boundaries.

After editing, prove that the managed block is byte-identical.

Outside the managed block, in project-owned content, add only the minimum declaration required by AP `17b7e085...` to activate the optional durable upgrade-ledger projection.

That declaration must identify:

```text
canonical AP target:
https://github.com/cisarik/ap.git
```

and exactly one committed Markdown ledger:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
```

Use the terminology and declaration structure prescribed by the target AP generation.

Do not duplicate rules that already belong to AP.

Do not turn project-owned `AGENTS.md` into an alternate AP specification.

## 6.3 `docs/AP_UPGRADE_OBSERVATIONS.md`

Create exactly one durable project-local ledger file:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
```

Its initial state must:

* satisfy the exact durable-ledger storage contract of AP `17b7e085...`;
* contain the required valid header;
* identify the canonical target correctly;
* contain the required activation snapshot;
* start with **zero synthetic upgrade observations/entries**;
* not invent backlog work merely to populate the file;
* not resurrect previously exhausted AP backlog items;
* not claim a protocol defect that has not actually been observed;
* remain a lightweight Markdown projection, not a database or executable subsystem.

The storage mechanism is being activated now; no artificial AP problem is being manufactured.

If the target AP contract permits or requires an explicit empty active-observation representation, use that exact representation.

## 6.4 `README.md`

Make only the minimal convergence required so FrameNest documentation reflects the exact adopted AP pin:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Do not opportunistically rewrite unrelated README content.

## 6.5 `tests/contract/test_ap_integration.py`

Update only what is required for the existing AP integration contract to recognize the new exact pin.

The expected AP commit must become:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Preserve the existing test philosophy.

Do not build a new ledger parser, ledger schema validator, Continuation Bootstrap executor, or large test harness unless the existing narrow integration test absolutely requires a tiny compatibility adjustment within this same file.

The selected design intentionally does **not** introduce executable ledger validation.

---

# 7. Explicitly forbidden scope

Do not create or modify any of the following as part of this logical whole:

* a new FrameNest ADR;
* `00_handout.md`;
* any continuation file;
* any handoff file;
* any `NEXT`, `BOOT`, restoration, resume, or generated-state document;
* any executable ledger parser;
* any executable ledger validator;
* any synthetic AP backlog entry;
* any unrelated test;
* any production configuration;
* any NUC state;
* any deployment artifact;
* any schema migration;
* any provider configuration;
* any Meta repository artifact;
* any generated prompt archive inside FrameNest;
* `.gitmodules`, unless an unexpected material inconsistency forces a fail-closed stop rather than scope expansion;
* `ap.project.conf`, unless the target AP itself proves the selected design impossible, in which case stop rather than expanding scope.

Do not implement the future fresh-Orchestrator restoration acceptance in this session.

---

# 8. Continuation Bootstrap intent

The purpose of this adoption is not to create another permanent handoff mechanism.

The target AP generation's Continuation Bootstrap should allow a later fresh Orchestrator to reconstruct state from ordinary durable project authority and evidence.

Therefore:

* do not create a special continuation-state document;
* do not encode a "next task" into the ledger merely so the later test has something to find;
* do not preload an outgoing Orchestrator handout;
* do not manufacture conversational-memory substitutes.

This logical whole explicitly has **no outgoing Orchestrator handout**.

There must be no:

```text
00_handout.md
```

for this logical whole.

A later fresh-Orchestrator restoration test will begin from a genuine minimal seed after publication and public readback.

---

# 9. Validation requirements

Validation must be proportional but strong enough to prove the AP adoption and ledger activation.

Use the target AP's own documented integration/update/doctor workflow where applicable. Do not invent commands when the repository provides the authoritative form.

At minimum establish all of the following before PASS.

## 9.1 Exact diff boundary

Prove that project changes are confined to:

```text
.ap
AGENTS.md
README.md
tests/contract/test_ap_integration.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

No other path may be part of the candidate commit.

Review both unstaged and staged state.

## 9.2 AP pin

Prove:

* candidate FrameNest gitlink for `.ap` is exactly `17b7e085...`;
* checked-out `.ap` HEAD is exactly `17b7e085...`;
* target commit object is authentic from canonical AP history/repository evidence;
* no local AP content modification exists beneath the submodule.

## 9.3 Managed block integrity

Prove the managed AP block in root `AGENTS.md` is byte-for-byte identical before and after the implementation.

A semantic eyeball check is insufficient.

Use a deterministic comparison or equivalent exact-byte evidence.

## 9.4 Ledger projection

Validate directly against the target AP normative text that:

* project-owned `AGENTS.md` explicitly declares the ledger;
* the canonical target is exactly:
  `https://github.com/cisarik/ap.git`;
* declaration points to exactly:
  `docs/AP_UPGRADE_OBSERVATIONS.md`;
* the file is committed project-owned Markdown;
* header conforms;
* activation snapshot conforms;
* there are zero synthetic entries;
* nothing creates an executable ledger requirement absent from AP.

## 9.5 Existing project integration test

Run the focused AP integration contract test containing:

```text
tests/contract/test_ap_integration.py
```

Use the repository-prescribed Python/tooling environment.

Do not casually substitute system Python for the project environment.

A non-zero result cannot support PASS.

## 9.6 AP candidate/doctor validation

Run the applicable target-AP-supported candidate/update/doctor validation needed for an existing consumer moving its pin.

Where the target AP documentation distinguishes candidate checks from staged/current integration checks, follow that distinction correctly.

The final staged/candidate state must pass the applicable strict doctor/integration gate.

A non-zero exit cannot support PASS.

Do not "explain away" a failing gate.

## 9.7 Text/diff hygiene

Run:

```text
git diff --check
```

or the correct equivalent against the candidate.

Inspect the complete diff manually.

Confirm no accidental formatting churn, unrelated prose rewrite, generated noise, or owner-change contamination.

## 9.8 Candidate object integrity

If all implementation and validation gates pass, create exactly one bounded implementation candidate commit.

Then record:

* exact candidate commit SHA;
* parent SHA;
* tree SHA;
* commit subject;
* exact changed paths;
* clean/dirty state after commit;
* exact `.ap` gitlink in the committed tree.

Do not push it.

If the surrounding repository workflow uses a dedicated task branch/worktree, preserve that model. Do not publish or merge it.

---

# 10. Candidate quality requirements

The candidate should be reviewable as one coherent logical change:

> FrameNest adopts AP `17b7e085...`, updates its existing exact-pin projections, and opts into the AP-defined project-local durable upgrade-ledger storage with an empty activation snapshot, without adding a parallel continuation mechanism or executable ledger subsystem.

Do not bundle unrelated cleanup.

Prefer the smallest semantically complete diff over cosmetic improvement.

---

# 11. Independent acceptance boundary

This Worker may validate its own implementation sufficiently to decide whether an implementation candidate is internally ready.

This Worker may **not** perform the independent acceptance role.

After your terminal report, all Worker 01 authority expires.

If you PASS, the Orchestrator is expected to create a **fresh independent acceptance Worker** against the exact candidate object.

That future Worker must not inherit implementation authority.

Publication is also separately authorized later.

---

# 12. Archive identity

Do not write Meta or archive files yourself.

The Cooperator/Orchestrator will archive the exact prompt and your actual resulting report externally using:

```text
01_implementation_00.md
01_report_00.md
```

Do not create those files in FrameNest.

Do not generate a substitute handoff.

---

# 13. Terminal-status rules

Your terminal standard status must be one of the governing AP statuses, with phase qualification appropriate to an implementation Worker.

Use:

```text
PASS
```

only if:

* preflight reconciled successfully;
* implementation remained entirely inside authority;
* all required validation gates exited successfully;
* the exact candidate commit exists;
* candidate evidence is internally consistent;
* no unresolved material discrepancy remains.

Expected phase-qualified successful result:

```text
implementation-PASS
```

If a material preflight discrepancy exists, stop **before mutation** and report the appropriate blocked result.

If implementation begins but validation reveals a defect you cannot safely correct inside the existing authority, stop without broadening scope and report the governing non-PASS status.

Never turn a non-zero required gate into PASS through prose.

---

# 14. Required terminal report

Return one detailed English report for `ORCHESTRATOR_CHAT`.

Begin with this exact structured header shape, filling real values:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-ap-continuation-bootstrap-and-ledger-adoption
Worker session ordinal: 01
Worker exchange ordinal: 01
Standard terminal status: <PASS|BLOCKED|PARTIAL|FAIL or exact AP-governed status>
Phase-qualified result: <implementation-PASS or appropriate non-PASS result>
Result artifact or commit: <exact candidate SHA or not-applicable>
Result evidence: <compact strongest evidence summary>
Logical-whole closure: not-closed
Report justification: <new-mutation|blocked-before-mutation|appropriate classification>
Authority expiry: all Worker 01 authority expired at this terminal report
```

Then report, with exact evidence rather than unsupported conclusions:

1. **Fresh-session confirmation**

   * fresh Worker status;
   * Native Plan Mode not used;
   * governing files read.

2. **Read-only preflight**

   * local FrameNest HEAD/branch/status;
   * owner-change classification;
   * `.ap` pre-adoption gitlink and checked-out state;
   * public FrameNest `main`;
   * public AP `main`;
   * whether all preconditions matched.

3. **Target AP interpretation**

   * exact target SHA;
   * which target AP documents governed Continuation Bootstrap and ledger activation;
   * concise statement of the project-local ledger contract actually implemented.

4. **Implementation**

   * exact change to `.ap`;
   * exact project-owned `AGENTS.md` activation;
   * exact ledger file semantics;
   * README convergence;
   * integration-test pin convergence.

5. **Managed-block proof**

   * method and result proving byte-for-byte preservation.

6. **Ledger proof**

   * canonical target;
   * declared path;
   * header/activation snapshot;
   * explicit confirmation of zero synthetic entries.

7. **Validation**

   * exact commands/gates that materially matter;
   * exit statuses;
   * focused test result;
   * AP doctor/candidate result;
   * `git diff --check`;
   * any other narrow evidence used.

8. **Candidate Git object**

   * commit SHA;
   * parent;
   * tree;
   * subject;
   * changed paths;
   * final working-tree status;
   * committed `.ap` gitlink.

9. **Authority accounting**
   Explicitly confirm that you did not:

   * push;
   * publish;
   * deploy;
   * modify production/NUC/network/provider state;
   * mutate Meta;
   * create ADR/handoff/continuation artifacts;
   * create executable ledger tooling;
   * invent ledger backlog.

10. **Next authority boundary**
    State that:

    * this implementation does not close the logical whole;
    * a fresh independent acceptance Worker is required next if implementation-PASS;
    * publication remains separately unauthorized;
    * the genuine minimal-seed fresh-Orchestrator restoration test is deferred until after publication and direct public readback.

Do not provide an outgoing Orchestrator handout.

Do not propose a second logical whole.

Do not perform publication.

Execute only this selected bounded implementation.
