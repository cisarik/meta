# Fresh Correction Worker — AP bundle temporary-resource cleanup

You are a genuinely fresh Correction Worker for the canonical Analytic Programming repository.

Logical whole:

`chat-orchestrator-offline-bundle-transport`

Worker session ordinal: `04`  
Worker exchange ordinal: `01`

Persistent role identity: `WORKER`  
Worker session profile: `Correction Worker`  
Worker session target: `fresh-worker-session`  
Native planning mode: `not-used`

This is a narrowly bounded correction after independent Acceptance returned:

`ACCEPTANCE-BLOCKED`

Do not reopen planning.
Do not redesign the bundle transport.
Do not modify its evidence semantics.
Do not make unrelated cleanup improvements.

## Repository

Expected canonical worktree:

```text
/home/agile/Projects/ap
```

Expected baseline HEAD:

```text
717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
```

The implementation candidate is intentionally still an uncommitted dirty worktree on top of that HEAD.

Before mutation verify:

- repository identity;
- exact HEAD;
- current dirty candidate;
- no unexpected changes beyond the known candidate.

Do not require a clean AP worktree because the implementation candidate is intentionally uncommitted.

## Authority

You may edit only the minimum candidate code necessary for this correction.

Expected edited file:

```text
ap
```

Do not edit AP semantics or projections unless the correction genuinely cannot be made without doing so.

Specifically do NOT edit:

```text
AP.md
AP_ORCHESTRATOR.md
PROMPT_CONTRACTS.md
README.md
FAQ.md
GLOSSARY.md
INTEGRATION.md
INTUITION.md
UPDATING.md
CHANGELOG.md
docs/adr/*
consumer repositories
Meta
```

No commit.
No push.
No consumer `.ap` pin update.

## Acceptance blocker

Independent Acceptance found that temporary bundle directories are not actually tracked by the parent shell cleanup logic.

Current pattern includes calls equivalent to:

```sh
bundle_raw=$(bundle_mktemp)/objects
bundle_payload=$(bundle_mktemp)/payload
bundle_zip_repo=$(bundle_mktemp)/zipgit
```

`bundle_mktemp` records its created path through shell state intended for `bundle_cleanup`.

But because it executes inside `$(...)`, those state mutations occur in a subshell.

The parent shell's cleanup list remains unchanged.

Therefore the EXIT/HUP/INT/TERM cleanup trap cannot remove those temporary directories.

Independent Acceptance observed large numbers of leftover:

```text
${TMPDIR:-/tmp}/ap-bundle.*
```

directories containing bundle payloads.

This is acceptance-blocking because offline transport packages can contain complete committed repository history and companion/submodule Git objects.

## Required correction

Refactor temporary-directory allocation so that:

1. every `ap bundle` temporary root is registered in the **parent shell**;
2. no required cleanup state depends on a function side effect occurring inside command substitution;
3. `bundle_cleanup` removes every created `ap-bundle.*` directory;
4. cleanup occurs on:
   - successful export;
   - ordinary command failure;
   - validation failure after one or more temporary directories exist;
   - `EXIT`;
   - `HUP`;
   - `INT`;
   - `TERM`;
5. source repositories and their object databases remain untouched;
6. existing bundle behavior and UX remain unchanged.

Prefer a small explicit shell pattern rather than adding a new abstraction framework.

A technically reasonable shape is to separate:

```text
allocate temp path
register temp path
derive child path
```

in the parent shell.

Do not merely add another trap if the parent still does not know the generated path.

Do not solve this with broad deletion such as:

```sh
rm -rf /tmp/ap-bundle.*
```

Cleanup must be limited to directories created by the current process.

Quote paths safely.

## Preserve current behavior

The correction must NOT alter:

- `ap bundle <project> --initial`;
- cumulative incrementals;
- companion trace;
- `.ap` bundling;
- submodule behavior;
- secret/history scanning;
- chain state;
- output naming;
- ZIP generation;
- evidence classes;
- zero-network behavior;
- existing commands.

No semantic AP documentation change is required for this correction.

## Required independent validation

Use disposable fixtures.

Do not rely only on reading the code.

### 1. Successful export

Record the set of matching temp directories before the test.

Run a successful initial export.

After command termination, verify that no new:

```text
${TMPDIR:-/tmp}/ap-bundle.*
```

directory created by that invocation remains.

The output ZIP must still be valid.

### 2. Failure after temporary allocation

Construct a deterministic failure that occurs after at least one temporary directory has been allocated.

After failure, verify that the invocation leaves no new temp directory.

Do not choose an early argument-validation failure that happens before temp allocation.

### 3. SIGINT

Run an export in a disposable scenario where it can be interrupted after temporary allocation.

Send `SIGINT`.

Verify:

- command terminates appropriately;
- all temporary directories registered by that process are gone;
- no unrelated `/tmp` paths were deleted.

### 4. TERM

If practical, repeat with `SIGTERM`.

At minimum verify the implemented trap path directly and explain evidence.

### 5. Multiple temporary roots

Ensure one invocation that creates all relevant temporary roots cleans all of them:

- object-scan staging;
- payload staging;
- ZIP throwaway Git repository;
- any additional bundle temp root created by current code.

### 6. No regression

Re-run a compact subset sufficient to show the correction did not disturb transport:

- initial bundle creation;
- local reconstruction;
- cumulative incremental;
- companion bundle if straightforward;
- `nothing new to export`;
- ignored `.env` behavior;
- tracked sensitive path refusal.

Do not recreate the entire previous 55-check implementation suite unless needed.

## Security inspection

Before finishing, inspect the corrected cleanup path for:

- command substitution side effects;
- word splitting;
- glob expansion;
- empty-variable `rm -rf`;
- duplicate registration;
- cleanup after partial initialization;
- traps firing more than once;
- cleanup functions returning unexpected status;
- cleanup masking the original command failure;
- unsafe paths outside the current invocation.

The cleanup routine must safely tolerate already-removed or partially-created paths.

## Out-of-scope acceptance observations

Independent Acceptance also mentioned several non-blocking observations:

- ambient `GIT_DIR`;
- IMPORT.md empty-DEST wording;
- POSIX `$'\n'`;
- shared `--allow-path` namespace.

Do **not** address those in this Correction Worker.

They are explicitly outside the smallest accepted correction scope.

## Terminal report

Return one complete report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Include:

- logical whole;
- Worker session ordinal `04`;
- Worker exchange ordinal `01`;
- Worker profile;
- baseline HEAD;
- confirmation that the candidate remained uncommitted;
- exact file(s) modified;
- root cause confirmed or disproven;
- exact correction made;
- explanation of why cleanup state now exists in the parent shell;
- successful-export cleanup result;
- failure-path cleanup result;
- SIGINT result;
- SIGTERM result if tested;
- multiple-temp-root cleanup result;
- compact regression results;
- security review;
- `git diff --stat`;
- `git status --short`;
- confirmation of no commit/push/Meta/consumer mutation;
- recommended next phase.

Do not claim Acceptance PASS.

Recommended next phase is a **fresh independent re-Acceptance Worker**.

Stop after the report.