# Targeted Planning Revision — Portable Media Sidecar Determinism

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 01
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: required

Persistent role identity: the exact current Worker 1 session
Worker session profile: Repository-Grounded Implementation Planning Worker
Phase: Discovery
Task type: read-only targeted implementation-plan revision
Reasoning recommendation: High — this is a bounded revision, but it governs durable serialized data, deterministic export, idempotent replacement, and machine-readable comparison semantics
Evidence posture: non-independent
Worker topology: single-active
Internal delegation posture: not-used

Authority renewal: complete; all exchange-02 authority expired at its terminal report
Continuity anchor: Worker 1 exchange 02 planning PASS for this exact logical whole, based on the contained clone at `/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02`
Retained context: convenience only, never authority
Implementation authority: none
Repository mutation authority: none
Host mutation authority: none
Meta mutation authority: none
Git mutation authority: none
Publication authority: none
Deployment authority: none
Production authority: none

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: targeted correction of the deterministic sidecar serialization, repeat-export, and compare-result boundary only
Plan disposition: advisory
Implementation in same Worker session: prohibited
Planning stop event: terminal targeted-revision report submitted
Execution authority event: later explicit ORCHESTRATOR implementation prompt with Native planning mode set to not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: targeted-revision
Prior planning report: Worker 1 session 01 exchange 02 terminal planning PASS
Targeted revision basis: newly-identified-material-risk
Changed decision boundary: deterministic and idempotent v1 sidecar encoding plus canonical compare-result semantics
Preserved unaffected decisions: explicit `framenest-sidecar` CLI; catalog-to-sidecar projection only; no import or rebuild; `{media_filename}.framenest.json`; one explicit `--location-id`; catalog remains authoritative; sidecar never overwrites catalog; atomic same-directory replacement; final mode `0644`; no migration; no new dependency; existing allowlist and exclusions except where this revision explicitly changes a field or validation test
Automatic targeted revisions used: 1

## 1. Repository gate

Use only the existing contained clone:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02
```

Do not inspect or modify the owner checkout at:

```text
/home/agile/Projects/framenest
```

Expected origin:

```text
https://github.com/cisarik/framenest.git
```

Expected detached HEAD and public `main`:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Expected AP gitlink and initialized submodule HEAD:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before analysis, run read-only gates:

```bash
cd /home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02
pwd -P
git status --short --branch
git status --porcelain=v1 --untracked-files=all
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git rev-parse HEAD^{tree}
git submodule status .ap
git -C .ap rev-parse HEAD
git diff --exit-code
git diff --cached --exit-code
env GIT_TERMINAL_PROMPT=0 git ls-remote origin refs/heads/main
```

Require the exact contained clone, origin, detached baseline, public ref, AP pin, clean index/worktree, no untracked paths, and no active Git operation.

If a gate fails, perform no restoration, clone, checkout, fetch, reset, clean, stash, submodule update, or mutation. Return `BLOCKED` with only the exact mismatch.

## 2. Material contradiction to resolve

The exchange-02 plan simultaneously proposed:

```text
sidecar_written_at_ms = wall-clock projection time
```

and:

```text
a second export of unchanged catalog state is byte-identical
```

Those properties conflict when the timestamp changes.

The revised v1 plan must preserve deterministic byte-for-byte export. A wall-clock write timestamp must not appear in canonical v1 serialized bytes. Remove `sidecar_written_at_ms` unless current source proves a deterministic, product-meaningful value; no such proof is presently accepted.

Catalog-owned `created_at_ms` and `updated_at_ms` may remain if their exact current semantics are verified from source.

For an existing valid same-identity sidecar whose bytes already equal the intended deterministic encoding, recommend a successful no-op without `os.replace`. For changed same-identity content, retain validated atomic replacement. Malformed, unsupported, special-file, symlink, or foreign-identity targets must not be destroyed.

## 3. Canonical comparison vocabulary

The exchange-02 plan used both `missing` and `not_exported`. Produce one canonical public result vocabulary.

Unless current source proves a contradiction, use:

```text
match
stale
mismatch
missing
```

Validation failures such as malformed JSON, duplicate keys, unsupported version, oversize input, unsafe path, or unreadable file are errors, not additional successful compare states.

Define deterministic precedence for at least:

1. sidecar path absent;
2. valid sidecar with exact projected fields;
3. valid differing sidecar whose catalog revision field is older than current catalog truth;
4. valid differing sidecar with equal or newer revision field;
5. valid sidecar with foreign media or location identity;
6. malformed or unsupported sidecar;
7. existing symlink, directory, socket, FIFO, or other non-regular target.

Clarify whether exact field equality returns `match` even when historical timestamps would otherwise suggest staleness. Avoid silently treating timestamps as stronger than actual content comparison.

Specify stable machine-readable result codes and the success/non-success exit-code classes needed by CLI contract tests. Do not invent an HTTP surface.

## 4. Required revised output

Return only a targeted revision, not a full unrelated re-planning exercise.

The report must include:

* the exact repository gate result;
* the revised v1 field table, showing removal or justified deterministic treatment of `sidecar_written_at_ms`;
* exact repeated-export/no-op semantics;
* the single canonical compare-result vocabulary;
* the comparison/error precedence table;
* any changed atomic-write or target-safety requirement;
* exact tests added to the future validation matrix;
* confirmation that all unaffected exchange-02 decisions remain preserved;
* any changed likely paths, or `none`;
* one smallest implementation step;
* no Worker 2 prompt.

Do not implement, create plan files, edit source, edit Meta, commit, push, deploy, or access production.

## 5. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo:

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 01
Worker exchange ordinal: 03
```

Use:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: planning-PASS | planning-PARTIAL | planning-BLOCKED
Report justification: new-material-risk
```

State start/end commit, changed repository paths (`none` required), tests or read-only checks performed, deviations, remaining risks, and the smallest next step.

If this single targeted revision cannot become decision-ready, return `PARTIAL` with:

```text
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION
```

Do not propose another automatic planning cycle.

All exchange-03 authority expires at the terminal report.
