# Fresh Independent Re-Acceptance Worker

You are a genuinely fresh independent Acceptance/Audit Worker for the canonical Analytic Programming repository.

Logical whole:

`chat-orchestrator-offline-bundle-transport`

Worker session ordinal: `05`  
Worker exchange ordinal: `01`

Persistent role identity: `WORKER`  
Worker session profile: `Fresh Independent Re-Acceptance`  
Worker session target: `fresh-worker-session`  
Native planning mode: `not-used`

Phase: Independent Re-Acceptance

## Repository

Expected canonical worktree:

```text
/home/agile/Projects/ap
```

Expected unchanged product HEAD:

```text
717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
```

The complete candidate is intentionally still **uncommitted and dirty** on top of that HEAD.

No commit or push has yet occurred.

Independently verify repository identity, HEAD and candidate diff before relying on previous reports.

## Independence

This must be a genuinely fresh acceptance.

You may read previous reports for provenance, but do not simply inherit their conclusions.

Previous phase history:

- Session 01: Planner
- Session 02: Implementation
- Session 03: Independent Acceptance → `ACCEPTANCE-BLOCKED`
- Session 04: bounded Correction Worker → correction PASS
- Session 05: **you**

Do not implement corrections.
Do not edit the candidate.
Do not commit.
Do not push.
Do not mutate Meta.
Do not update consumer `.ap` pins.

## Previous blocker

Session 03 found one acceptance-blocking defect.

Temporary directories created by `ap bundle` were allocated through command substitution:

```sh
bundle_raw=$(bundle_mktemp)/objects
bundle_payload=$(bundle_mktemp)/payload
bundle_zip_repo=$(bundle_mktemp)/zipgit
```

The cleanup list was therefore mutated only inside subshells and the parent cleanup trap could not see those paths.

Bundle payloads containing repository history remained under:

```text
${TMPDIR:-/tmp}/ap-bundle.*
```

Session 04 corrected only `ap`.

The reported correction:

- removed `bundle_mktemp`;
- added direct parent-shell `bundle_alloc_tmp`;
- registers every created root in `bundle_tmp_list`;
- derives child paths only after registration;
- EXIT/HUP/INT/TERM invoke owned-path cleanup;
- signal exits are 129/130/143 as applicable;
- cleanup removes only paths registered by that process;
- no wildcard deletion of unrelated `/tmp/ap-bundle.*`.

Do not accept this description without independently inspecting and exercising it.

---

# 1. Re-test the blocker independently

This is mandatory.

Create your own disposable fixtures.

Verify cleanup after:

### Successful export

Run a real successful initial bundle export.

After process exit:

- generated ZIP still exists and is valid;
- no temp root created by the process remains.

### Failure after allocation

Cause a deterministic failure only **after** one or more bundle temp roots have been created.

After failure:

- correct non-zero status;
- no owned bundle temp root remains.

### SIGINT

Interrupt a live export after temp allocation.

Verify:

- exit status/termination is appropriate;
- all process-owned temp roots are gone;
- unrelated decoy temp paths survive.

### SIGTERM

Repeat independently for TERM.

### Multiple roots

Use an invocation exercising several temporary areas, preferably:

- project secret scan;
- `.ap` scan;
- companion scan;
- payload staging;
- ZIP staging.

All process-owned roots must be gone at exit.

Check that cleanup cannot expand into:

```sh
rm -rf /tmp/ap-bundle.*
```

or equivalent unsafe behavior.

---

# 2. Inspect the correction itself

Read the relevant `ap` code.

Specifically audit:

- temp allocation executes in parent shell;
- no cleanup-state mutation depends on `$(...)`;
- empty or malformed paths cannot reach `rm -rf`;
- paths are quoted;
- cleanup only removes current invocation's registered paths;
- duplicate cleanup is harmless;
- traps are disarmed appropriately;
- cleanup does not mask original command failure;
- partial initialization is safe;
- source repository/object database is not used as temporary storage.

No blocker may remain here.

---

# 3. Reconfirm complete transport semantics

Because Session 04 intentionally tested only a compact regression subset, independently verify enough of the complete candidate to issue final acceptance.

At minimum confirm:

## Initial bundle

```sh
ap bundle <project> --initial
```

produces a package from which an exact committed project checkout can be reconstructed offline.

Verify:

- exact project HEAD;
- exact `.ap` gitlink;
- reconstructed `.ap HEAD == project gitlink`;
- no synthesized commits.

## Cumulative incremental

Test:

```text
A = initial
B = intermediate
C = newest
```

Confirm:

```text
initial A + cumulative A..C update
```

reconstructs C without B.

## Missing prerequisites

Applying the incremental to a checkout without the required initial objects must fail closed and direct the ChatOrchestrator toward a fresh `--initial`, not GitHub recovery.

## Non-ancestor chain

History rewrite/non-ancestor initial commit must fail closed.

---

# 4. Zero-network property

Independently confirm `ap bundle` performs no network operation.

It must not require:

- fetch;
- pull;
- ls-remote;
- GitHub API;
- remote clone;
- submodule update.

Use a broken proxy or isolated network environment where useful.

This restriction applies only to the bundle exporter / ChatOrchestrator transport workflow.

Normal GitHub behavior of other AP actors remains intact.

---

# 5. Evidence semantics

Reconfirm live documentation remains coherent after the correction.

The candidate must distinguish:

```text
exact committed bundle evidence
```

from:

```text
independently observed current public branch evidence
```

A bundle must not prove current GitHub state.

Required limitation when GitHub has not actually been observed:

```text
public branch state not directly observed
```

ChatOrchestrator may perform ordinary routing from valid bundle evidence when public state is not the claim being decided.

Publication/public-ref claims still require appropriate independent public evidence.

Search live projections for contradictions.

Historical ADR text is not a contradiction.

---

# 6. Delivery semantics

Confirm final candidate still says:

- ChatOrchestrator → manual Cooperator ferry normally;
- full Orchestrator with authorized working dispatch → direct complete-prompt dispatch normally, including first Planner;
- native planning mode remains a separate requirement;
- independence/fresh-session constraints remain separate;
- Cooperator opt-out/manual fallback remains available.

Do not allow GitHub capability, dispatch capability and access profile to become conflated.

---

# 7. Companion trace

Verify explicit companion configuration still works:

```sh
ap bundle <project> --initial --companion-trace <repo>
```

and subsequent:

```sh
ap bundle <project>
```

can produce a useful update when only the companion trace changed.

No hardcoded Meta.
No sibling scan.
No automatic inclusion of private repos.

---

# 8. Secrets and ignored files

Independently spot-check:

- ignored `.env` does not enter;
- tracked `.env` refuses;
- historically tracked then deleted `.env` refuses;
- explicit exact `--allow-path` behaves as documented.

Do not claim pathname scanning proves absence of secrets.

---

# 9. Other submodules

Spot-check:

- unexpected submodule fails closed;
- explicitly included local submodule can be bundled at its exact gitlink;
- no missing submodule content is fetched from network.

---

# 10. Existing command regression

Verify the helper refactor did not materially alter existing commands:

```text
init
doctor
project
exec
update
```

Environment-dependent failures such as a deliberately absent project `.venv` must be classified separately from regressions.

Do not perform unauthorized publication or mutation.

---

# 11. Review previous coordinate defect

Session 03 classified the Session-02 report-coordinate problem as non-blocking provenance/documentation defect.

Verify current trace now has coherent progression:

```text
01 Planner
02 Implementation
03 Acceptance
04 Correction
05 Re-Acceptance
```

Do not retroactively rewrite historical reports merely to beautify them.

State whether this remains non-blocking.

---

# 12. Non-blocking observations

Previous Acceptance identified these optional observations:

- ambient `GIT_DIR`;
- IMPORT.md empty-DEST wording;
- POSIX `$'\n'`;
- shared `--allow-path` namespace.

They were explicitly outside Session-04 correction scope.

Re-evaluate their severity.

Do **not** block merely because they were not cleaned up.

Block only if your independent analysis shows one creates a material correctness, portability, privacy, security or continuity failure in the supported contract.

Do not fix them yourself.

---

# 13. Final decision

Return exactly one overall result:

```text
ACCEPTANCE-PASS
```

or:

```text
ACCEPTANCE-BLOCKED
```

PASS requires:

- previous temp-cleanup blocker independently resolved;
- no new material blocker;
- exact offline reconstruction works;
- cumulative incremental works;
- ChatOrchestrator evidence semantics remain correct;
- no accidental GitHub dependency in `ap bundle`;
- no material regression in the AP executable.

If BLOCKED, provide the smallest bounded Correction Worker scope.

If PASS, recommend:

1. Cooperator commit;
2. push canonical AP;
3. verify publication;
4. then consumer `.ap` pin adoption as a separate step.

Do not perform those actions yourself.

## Terminal report

Return one report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Include:

- logical whole;
- session `05`;
- exchange `01`;
- independent-reacceptance statement;
- baseline HEAD;
- candidate worktree state;
- cleanup success/failure/SIGINT/SIGTERM results;
- exact reconstruction result;
- cumulative incremental result;
- missing-prerequisite result;
- zero-network result;
- evidence-semantics result;
- delivery-semantics result;
- companion result;
- secret/history result;
- submodule result;
- existing-command regression result;
- coordinate finding;
- non-blocking observations disposition;
- security findings;
- overall `ACCEPTANCE-PASS` or `ACCEPTANCE-BLOCKED`;
- next recommended phase;
- confirmation of no candidate mutation/commit/push.

Stop after the terminal report.