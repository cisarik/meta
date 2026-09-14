# Fresh Implementation Worker - AP ChatOrchestrator offline bundle transport

You are a genuinely fresh Implementation Worker for the canonical Analytic Programming repository.

Implement the approved planning result for:

`chat-orchestrator-offline-bundle-transport`

This is implementation, not a new planning cycle.

## Worker identity

- Persistent role identity: `WORKER`
- Worker session profile: `Implementation Worker`
- Worker session target: `fresh-worker-session`
- Native planning mode: `not-used`
- Recommended reasoning: `High`
- Delivery route: manual Cooperator delivery
- Implementation authority: repository edits and local validation
- Commit authority: **not granted**
- Push authority: **not granted**
- Publication authority: **not granted**

You may use normal Git and GitHub inspection commands because the GitHub restriction being fixed applies only to the `ChatOrchestrator` access profile.

Do not commit.
Do not push.
Do not mutate Meta.
Do not update any consumer `.ap` pin.
Do not modify FrameNest, ContextDesk, LibreTiles, or any other consumer.

Leave the completed AP candidate in the local AP worktree for the Cooperator to review and commit.

## Expected implementation baseline

The approved Planner verified:

```text
repo:   https://github.com/cisarik/ap.git
root:   /home/agile/Projects/ap
HEAD:   717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
public origin/main: same SHA
worktree/index: clean
branch: feat/ap-practical-workflow-consolidation
```

Before editing:

1. verify repository identity;
2. verify exact HEAD;
3. verify worktree/index clean;
4. verify canonical origin;
5. independently verify public `origin/main`;
6. locate and read the archived `01_report_00.md` planning report if present in the active trace.

Do not guess an external trace path.

If the AP repository baseline has unexpectedly moved from the approved planning baseline, stop before editing and report the discrepancy.

The Cooperator may have committed only the planning report in an external trace repository. That does not change the AP product baseline.

## Planning disposition

The Planner result is accepted as:

`planning-PASS`

Implement the approved design, subject to the two Git-level corrections below discovered independently after planning.

Do not reopen architecture merely because another implementation is aesthetically preferable.

If implementation evidence proves a planning assumption technically false, make the smallest necessary correction and document it in the terminal report.

---

# 1. Fundamental scope

This feature exists specifically for the **ChatOrchestrator** access profile.

Do not remove or weaken normal Git/GitHub behavior for:

- full Orchestrators;
- Planners;
- Implementation Workers;
- diagnostic Workers;
- correction Workers;
- independent Acceptance/Audit Workers;
- publication Workers;
- deployment Workers.

Those actors retain ordinary Git access and ordinary GitHub/public-ref verification according to their authority.

The new capability solves one narrow failure:

> A read-only ChatOrchestrator must not lose project continuity merely because its execution container cannot resolve or reach GitHub.

GitHub remains the normal publication and public verification layer.

Offline bundles become an alternative source of **exact committed repository evidence** for ChatOrchestrator orchestration.

---

# 2. Evidence model

Implement the semantic distinction approved by planning.

AP must distinguish:

```text
exact committed bundle evidence
```

from:

```text
independently observed current public branch evidence
```

A valid offline bundle may prove, as applicable:

- exact Git commit SHA;
- commit ancestry represented by the supplied Git objects and prerequisites;
- exact trees/blobs;
- derivable diffs;
- exact `.ap` gitlink;
- exact bundled companion-trace commit.

It must NOT prove:

- current GitHub branch HEAD;
- successful push;
- remote synchronization;
- current remote-tracking state;
- absence of a newer public commit;
- Cooperator uncommitted worktree state;
- sender authenticity merely because Git object hashes are internally valid.

When a ChatOrchestrator has bundle evidence but no independent public observation, the required limitation is:

```text
public branch state not directly observed
```

Do not silently promote bundle evidence into public evidence.

If a future transition genuinely requires publication equality, current public branch state, successful push or another remote claim, a capable Worker/full Orchestrator must perform the normal GitHub/public verification.

If the current decision needs only exact committed state, a valid bundle is sufficient and lack of ChatOrchestrator GitHub connectivity must not block ordinary routing.

---

# 3. Fix the current semantic conflict

Audit and update the live semantic owner and projections identified by the Planner.

In particular correct the conflict between:

- phase-specific public gates applying when the claim/authority actually requires them;
- capability-adaptive public verification;
- RF-19 manual retrieval currently demanding canonical public commit verification;
- restoration language currently requiring public truth before continuation;
- Continuation Bootstrap public/external anchors;
- inspection clone language describing only verified published state.

A manually relayed or bundled exact commit does not become public state merely because it has a SHA.

RF-19 must allow a ChatOrchestrator to reconcile an exact report/repository state using authorized bundle evidence when current public state is not the claim under decision.

Fresh ChatOrchestrator restoration from an initial package must be lawful.

Fresh full Orchestrator restoration with GitHub access keeps normal independent public verification.

---

# 4. Delivery-route correction

Correct the currently fused concepts:

- first Planner;
- native planning mode;
- manual delivery;
- full Orchestrator dispatch.

Target semantics:

### ChatOrchestrator

Manual Cooperator ferry is the normal prompt/result delivery route.

### Full Orchestrator with authorized functioning dispatch

Direct dispatch of the complete Worker prompt is the normal route, including the first Planner of a new logical whole.

The Cooperator must not be forced to copy/paste the first Planner merely because it is the first Planner.

### Full Orchestrator without dispatch

Manual Cooperator delivery is the fallback.

### Independence / external fresh-session requirement

Existing independence rules still apply and may require a genuinely external/manual fresh Worker.

### Native planning mode

The first Planner still requires actual native planning mode where current AP requires it.

Native planning mode and delivery route are separate axes.

GitHub access and dispatch capability are also separate axes.

Preserve explicit Cooperator opt-out and sovereignty.

Do not rewrite historical ADR-0022 or ADR-0023 bodies.

Create the new prospective ADR planned as ADR-0025 if that number remains free. If another ADR now occupies 0025, use the next available number and document the discrepancy.

---

# 5. Implement `ap bundle`

Add a new executable command to the existing POSIX `/bin/sh` `ap` tool.

Primary UX:

```sh
~/Projects/ap/ap bundle framenest --initial
```

then later:

```sh
~/Projects/ap/ap bundle framenest
```

This command is intentionally invoked from the **standalone AP checkout**.

It must not require the executable to be running as the target project's `.ap` submodule.

Preserve existing behavior of:

```text
ap init
ap doctor
ap project
ap exec
ap update
```

The Planner identified `require_context` as being submodule-specific.

Perform the smallest sensible helper split, such as extracting a tool-repository check from consumer-context validation, rather than building a new framework.

Remain POSIX `/bin/sh`.

Do not add a package/runtime dependency merely for this feature.

---

# 6. CLI surface

Implement at minimum:

```text
ap bundle <project> --initial
    [--root <physical-git-root>]
    [--projects-root <physical-directory>]
    [--companion-trace <physical-git-root>]
    [--include-submodule <project-relative-path>]...
    [--allow-path <project-relative-path>]...
    [--output-dir <absolute-directory>]
    [--replace-chain]

ap bundle <project>
    [--root <physical-git-root>]
    [--include-submodule <project-relative-path>]...
    [--allow-path <project-relative-path>]...
    [--output-dir <absolute-directory>]

ap bundle --help
```

The simple form is the primary UX.

Do not require `--root` for the Cooperator's normal layout.

Safe project-name rule should reject slashes, traversal and ambiguous names.

Preferred resolution:

1. explicit `--root`;
2. stored chain mapping after initial export;
3. explicit/configured projects root;
4. `$HOME/Projects/<project>` only as a convenience fallback when `$HOME/Projects` exists;
5. otherwise fail and tell the user to provide `--root`.

Never recursively scan sibling repositories or guess names.

---

# 7. Source repository preconditions

Export must be fail-closed.

Verify at least:

- physical Git worktree root;
- HEAD resolves to a commit;
- non-shallow repository;
- no `refs/replace`;
- clean index/worktree for non-ignored state;
- configured `remote.origin.url`;
- no mutation needed to make the export succeed;
- exporter AP checkout itself is clean;
- running `ap` corresponds to the exporter AP checkout;
- no unsupported Git LFS transport condition;
- project identity matches stored chain state.

For ordinary consumer repositories also require:

- initialized `.ap`;
- `.ap` is a gitlink/submodule;
- `.ap HEAD` exactly equals superproject gitlink;
- `.ap` worktree clean;
- canonical AP identity consistent with AP expectations.

Canonical AP itself is a special case:

```sh
ap bundle ap --initial
```

must be possible even though AP does not contain itself as `.ap`.

No source mutation.

Specifically no:

- commit;
- fetch;
- push;
- remote mutation;
- source ref mutation;
- checkout;
- submodule update;
- `.ap` pin update.

Temporary repositories/directories outside source repos are allowed and should be securely cleaned.

---

# 8. Package must contain Git objects, not working-tree ZIP

Do NOT ZIP the project's filesystem tree.

The outer ZIP is only an attachment container.

Payload is Git-native.

Therefore untracked or ignored local files such as:

```text
.env
.venv/
node_modules/
build/
dist/
cache/
editor state
local generated binaries
```

must not enter the transport merely because they are present on disk.

Do not manually reproduce `.gitignore` filtering over the filesystem.

Use Git objects as the transport source.

Tracked content necessarily remains part of the exact commit.

Do not silently strip legitimate tracked binaries, because that would change commit identity.

---

# 9. Package structure

Produce a uniquely named ZIP such as:

```text
<project>-ap-transport-<initial|update>-<UTC>-<head12>.zip
```

Never silently overwrite an existing package.

Contents should follow the approved plan:

```text
manifest.conf
IMPORT.md
checksums
project.bundle
ap.bundle
companion-trace.bundle
```

where optional files are omitted when not applicable.

Other explicitly included submodules may have clearly named bundle payloads.

`manifest.conf` should use a parser already available through Git, for example git-config syntax.

Do not add `jq` or a JSON runtime solely for this.

Record enough information to reconstruct and classify the package, including at least:

- schema version;
- transport kind;
- initial/update package kind;
- project name/identity;
- configured origin;
- exact project HEAD;
- original chain initial commit;
- branch or detached status;
- exact `.ap` gitlink or canonical-AP special case;
- exporter AP commit;
- UTC creation time;
- included companion repositories;
- included explicit submodules;
- payload integrity hashes;
- `publicVerification=not-performed`;
- evidence class;
- `publicBranchState=not-directly-observed`;
- explicit allowed-path exceptions if any.

Generated `IMPORT.md` is operational guidance, not a competing protocol owner.

---

# 10. Outer ZIP implementation

The Planner observed that `zip(1)` is not installed while Git supports archive ZIP.

Do not introduce a `zip(1)` dependency.

A valid implementation is:

1. assemble payload files in a private temporary directory;
2. create a throwaway temporary Git repository;
3. add/commit only those package payload files inside that throwaway repository;
4. use:

```sh
git archive --format=zip
```

to create the attachment ZIP.

Do not write temporary packaging objects into the source project's object database.

Ensure binary `.bundle` bytes survive packaging exactly.

Verify the payload checksums after round-trip extraction in smoke validation.

---

# 11. IMPORTANT Git correction discovered after planning

Do not implement this Planner pseudocode literally:

```sh
git bundle create ap.bundle <raw-gitlink-SHA>
```

It is technically wrong.

Independent Git testing showed that creating a bundle from an otherwise unreferenced raw commit SHA can fail with:

```text
fatal: Refusing to create empty bundle.
```

You already have a stronger precondition:

```text
.ap HEAD == superproject .ap gitlink
```

Therefore use a named/adverstised revision such as:

### Initial `.ap`

```sh
git -C <ap-checkout> bundle create <out>/ap.bundle HEAD
```

after verifying `HEAD == gitlink`.

### Incremental `.ap`

```sh
git -C <ap-checkout> bundle create <out>/ap.bundle <initialApCommit>..HEAD
```

after verifying current `.ap HEAD == current superproject gitlink`.

Use the analogous method for explicitly included submodules and companions.

Do not mutate source refs merely to create a bundle.

If some implementation case requires an exact commit that is not current `HEAD`, construct a temporary local Git repository/ref outside the source repo rather than updating source refs.

---

# 12. Initial project bundle

For the consumer project initial package, bundle only history reachable from the committed current state required for reconstruction.

Do not indiscriminately use `--all`, which could pull unrelated stale branches and objects into the attachment.

A valid shape is:

```sh
git bundle create project.bundle HEAD
```

Optionally advertise the current local branch ref as well if doing so materially improves reconstruction and remains exact.

Detached inspection checkout is acceptable for ChatOrchestrator. Exact committed content matters more than manufacturing a branch.

Record branch/detached identity in the manifest.

---

# 13. Cumulative incremental algorithm

This is an important UX property.

Suppose:

```text
initial = A
first update = B
second update = C
third update = D
```

Generate:

```text
update1 = A..B
update2 = A..C
update3 = A..D
```

not:

```text
A..B
B..C
C..D
```

Thus the Cooperator can send the newest update directly to a ChatOrchestrator that still has the original initial state.

Missing update1/update2 must not break update3.

For project:

```sh
git bundle create project.bundle <initialCommit>..HEAD
```

after verifying:

```sh
git merge-base --is-ancestor <initialCommit> HEAD
```

If the initial baseline is no longer an ancestor, fail and instruct the user to establish a new chain using an explicit initial-reset operation.

Do not silently change the baseline.

Apply the same cumulative principle independently to:

- `.ap`;
- companion trace;
- explicitly included submodules.

If a component has not changed since the initial package, omission is acceptable if the manifest makes this explicit.

If nothing has changed anywhere relevant, return a clear "nothing new to export" result instead of manufacturing a meaningless package.

---

# 14. Chain state

Do not store generated transport state inside the consumer repository.

Use XDG-style user state, for example:

```text
${XDG_STATE_HOME:-$HOME/.local/state}/ap/bundle/
```

Use an identity-safe chain directory/key.

Store at least:

- project name;
- physical project root;
- origin identity;
- initial project commit;
- initial `.ap` commit;
- companion identity/root/initial commit if configured;
- explicitly included submodules;
- chain creation metadata.

Optional user configuration may live under:

```text
${XDG_CONFIG_HOME:-$HOME/.config}/ap/
```

for convenience settings such as:

- projects root;
- output directory.

Absolute local paths must remain user-local state.

Never commit them into AP consumers.

---

# 15. Output location

Primary UX should make attaching the resulting file easy.

Prefer:

1. explicit `--output-dir`;
2. configured output directory;
3. user's Downloads directory when safely discoverable/existing;
4. XDG AP state package directory fallback.

Always print the final **absolute ZIP path** prominently.

The Cooperator should finish with something visually obvious such as:

```text
READY: /home/agile/Downloads/framenest-ap-transport-update-....zip
```

Do not make the emoji authoritative.

---

# 16. Sensitive tracked/history paths

This is security-sensitive.

`.gitignore` is not a secret sanitizer.

Initial bundles can contain historical objects no longer present at current HEAD.

Implement a conservative pathname scan over the Git history/object range actually being exported.

At minimum detect obvious risky paths/names such as:

```text
.env
.env.*
id_rsa
id_dsa
id_ecdsa
id_ed25519
*.pem
*.p12
*.pfx
*.key
*.keystore
*.jks
credentials.json
secrets.json
secrets.yaml
.netrc
.pypirc
```

A safe documented example file such as `.env.example` may be treated separately if the implementation can do so without weakening detection of real `.env` files.

On a suspicious hit:

- print the offending tracked/historical path;
- refuse export;
- make no package;
- do not pretend filename scanning proves absence of secrets.

If implementing the planned explicit:

```text
--allow-path <relpath>
```

exception:

- require exact explicit paths;
- record exceptions in the manifest;
- do not create a global `--force`;
- do not silently whitelist;
- never describe the result as "secret-free".

Do not strip Git objects to sanitize the package.

That would invalidate exact commit identity.

---

# 17. Other submodules

Superproject Git bundles contain gitlinks, not submodule content.

`.ap` is specially required and included.

For every other submodule:

- default to fail-closed;
- identify it explicitly;
- tell the user it was not included;
- allow explicit local inclusion with `--include-submodule <path>`;
- require the local checkout to contain exactly the referenced gitlink commit;
- do not contact the network to fill it;
- bundle that exact committed state;
- describe it in manifest/import instructions.

Never label an export a complete snapshot while silently omitting required gitlink content.

---

# 18. Companion analytic trace

Do not hardcode `cisarik/meta`.

Do not scan for `meta`.

Do not assume a sibling directory.

The approved v1 model is explicit opt-in during initial chain creation, for example:

```sh
~/Projects/ap/ap bundle framenest --initial \
    --companion-trace /home/agile/meta
```

The initial command records that mapping in user-level chain state.

Thereafter:

```sh
~/Projects/ap/ap bundle framenest
```

must automatically include the configured companion's newest cumulative committed state when it changed.

This is important because a Planner/Worker report may be committed only in the external analytic trace while the product repository has not changed.

An update package containing only a changed companion trace is valid and useful.

The companion must satisfy equivalent strictness:

- physical Git root;
- clean;
- exact committed HEAD;
- configured identity/origin;
- initial companion commit remains ancestor for cumulative incremental transport;
- suspicious history handling;
- no network use.

Private traces must never be included merely because they exist.

Only explicit configuration authorizes inclusion.

RF-19 remains the semantic owner of analytic trace/report exchange.

The bundle transport is only a storage/transport mechanism.

---

# 19. ChatOrchestrator reconstruction semantics

Generated `IMPORT.md` and live AP projections must teach this workflow.

## Initial

1. unpack ZIP to a private inspection area;
2. parse manifest;
3. verify payload checksums;
4. locally validate the bundle(s);
5. reconstruct project;
6. reconstruct exact `.ap`;
7. reconstruct configured companion/submodules if included;
8. verify reconstructed SHAs against manifest;
9. verify `.ap HEAD` equals the project's gitlink;
10. configure canonical origin URLs only as identity/reference if desired;
11. do **not fetch** those remotes;
12. classify evidence as bundle evidence;
13. state:

```text
public branch state not directly observed
```

14. continue ordinary ChatOrchestrator routing when public evidence is not required.

The inspection checkout is ephemeral cache.

It is not durable project storage.

Conversational context is not a substitute for Git objects.

---

# 20. IMPORTANT second Git correction discovered after planning

Do not blindly implement the planned sequence:

```text
unpack
git bundle verify project.bundle
clone
```

from an arbitrary non-repository directory.

`git bundle verify` requires Git repository context.

Independent testing confirmed an invocation outside a Git repository fails with:

```text
error: need a repository to verify a bundle
```

For an initial bundle with no prerequisites, use one of the technically correct approaches, for example:

```sh
git init --bare <temporary-verification-repo>
git -C <temporary-verification-repo> bundle verify <absolute-bundle-path>
```

then locally clone/reconstruct,

or perform another equivalently strong Git-native validation sequence.

For incremental packages, run `git bundle verify` in the corresponding already-reconstructed repository so prerequisite objects are actually checked:

```sh
git -C <inspection-project> bundle verify <update-bundle>
```

The implementation and generated `IMPORT.md` must get this detail right.

Do not present a command sequence that fails outside a repository.

---

# 21. Incremental reconstruction

For an incremental package:

1. confirm chain/project identity;
2. verify checksums;
3. verify bundle prerequisites against the existing reconstructed repo;
4. fetch from the local bundle, not GitHub;
5. move the inspection checkout to the exact advertised commit;
6. do the same for changed `.ap`, companion and explicit submodules;
7. verify final SHAs and gitlinks;
8. retain:

```text
public branch state not directly observed
```

unless separate real public evidence exists.

If prerequisite objects or the inspection checkout are gone:

**do not recover by contacting GitHub.**

Tell the Cooperator to generate and provide a new:

```sh
ap bundle <project> --initial
```

A new initial snapshot after days or weeks is normal.

Do not require replaying a long series of incremental attachments.

---

# 22. ChatOrchestrator must not depend on GitHub recovery

For this transport profile, do not prescribe:

- retry GitHub;
- GitHub mirror;
- reverse proxy;
- DNS pinning;
- hardcoded GitHub IP;
- alternate public clone;
- guessed cache recovery.

The entire purpose is deterministic Cooperator-mediated continuity when ChatOrchestrator network access is unreliable.

A full Orchestrator/Worker remains free to use normal GitHub as usual.

---

# 23. Presentation-state clarification

Make the small approved clarification without turning AP into a global emoji palette.

Keep project-owned emoji/localization.

Clarify textual routing states such as:

```text
ready
waiting
blocked
partial
```

These indicate routing/presentation state.

They are not equivalent to:

- implementation PASS;
- acceptance PASS;
- publication PASS;
- deployment PASS;
- ORCHESTRATOR closure.

An emoji must never independently convey authority or closure.

Avoid broad redesign of communication presentation.

---

# 24. ADR

Create the prospective ADR approved by the Planner.

It should record at least:

- the observed ChatOrchestrator GitHub/DNS failure class;
- offline exact committed bundle evidence;
- separation from public branch evidence;
- ChatOrchestrator-only offline transport scope;
- normal Git/GitHub retention for other AP actors;
- ephemeral inspection checkout;
- cumulative incremental bundle design;
- explicit companion trace;
- first-Planner delivery correction for full Orchestrators;
- preservation of native planning mode;
- partial supersession relationship with ADR-0023;
- rejection of worktree ZIPs;
- rejection of GitHub mirrors as continuity requirement;
- rejection of making conversational context the repository;
- security limitation around tracked/historical secrets.

Do not rewrite historical ADR bodies.

Update the ADR index/relationship text.

---

# 25. Expected documentation/projection scope

Use `AP.md` as sole live semantic owner.

Inspect and update only where required.

Planner expected changes in:

```text
AP.md
ap
docs/adr/<new ADR>
docs/adr/README.md
AP_ORCHESTRATOR.md
PROMPT_CONTRACTS.md
GLOSSARY.md
FAQ.md
INTUITION.md
INTEGRATION.md
README.md
UPDATING.md
CHANGELOG.md
PROMPT_ENGINEERING_PATTERNS.md
```

Do not mechanically touch every file.

For each modified projection, ensure it remains a projection rather than a competing semantic owner.

Expected unchanged unless implementation proves otherwise:

```text
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
INFOSEC.md
ap.project.conf
historical ADR bodies
consumer repositories
```

Do not change schema v1 merely to store bundle machine-local configuration.

---

# 26. Practical validation

ADR-0015 retired the monolithic protocol-mirroring test suite.

Do not resurrect one.

Use disposable temporary Git repositories and one-shot smoke validation.

Do not commit a large permanent `tests/` framework solely for this feature.

Validate at least:

1. successful initial export;
2. package unzip/readback;
3. checksum validation;
4. exact reconstruction without network;
5. initial bundle Git validation using valid repository context;
6. cumulative incremental export;
7. cumulative incremental import;
8. skip intermediate update and still reconstruct latest state;
9. dirty project refusal;
10. rewritten/non-ancestor initial baseline refusal;
11. missing `.ap` refusal;
12. mismatched `.ap HEAD` vs gitlink refusal;
13. ignored `.env` absent;
14. tracked `.env`/suspicious historical path refusal;
15. explicit allow-path behavior if implemented;
16. changed `.ap` pin forward and reconstruct exact new gitlink;
17. lost prerequisite/inspection checkout causes request for new initial;
18. unexpected other submodule refusal;
19. explicit included submodule success;
20. configured companion trace included;
21. companion-only change can produce useful update;
22. unconfigured sibling/Meta is never guessed;
23. source export performs no GitHub/network operation;
24. invalid HTTP proxy/network still permits export;
25. canonical AP self-bundle works without `.ap`;
26. `zip(1)` is not required;
27. existing `init` behavior unchanged;
28. existing `doctor` behavior unchanged;
29. existing `project` behavior unchanged;
30. existing `exec` behavior unchanged;
31. existing `update` behavior unchanged;
32. output package is unique and not silently overwritten.

Use real `git bundle` inspection/reconstruction in the fixtures, not merely textual assertions.

---

# 27. Security review before completion

Before terminal report, inspect the implementation specifically for:

- shell quoting;
- whitespace in paths;
- `..` traversal;
- option injection;
- symlink/physical-path confusion;
- unsafe `eval`;
- temporary-file cleanup;
- predictable temp files;
- source object DB mutation;
- accidental network commands;
- accidental inclusion of ignored working-tree content;
- accidental inclusion of unconfigured private repositories;
- stale chain-state confusion;
- malicious or malformed project names;
- checksum parser ambiguity;
- manifest parser ambiguity.

Preserve POSIX shell portability.

Fail closed rather than guessing.

---

# 28. Human UX acceptance target

The normal Cooperator experience should ultimately be this simple:

First package for FrameNest:

```sh
~/Projects/ap/ap bundle framenest --initial \
    --companion-trace /home/agile/meta
```

The command prints one clear final ZIP path.

The Cooperator attaches that ZIP to a fresh ChatOrchestrator.

Later, after committing either:

- product changes;
- AP pin changes;
- Planner/Worker reports in the configured trace;
- or some combination,

the Cooperator runs only:

```sh
~/Projects/ap/ap bundle framenest
```

and attaches the newly generated ZIP.

No GitHub access is required by ChatOrchestrator.

No manual diff construction is required.

No per-project bundle script is required.

No project repository contains local bundle state.

After a long break or lost ChatOrchestrator inspection cache:

```sh
~/Projects/ap/ap bundle framenest --initial --replace-chain
```

creates a new starting package.

Do not sacrifice this UX without a concrete safety reason.

---

# 29. No consumer adoption in this Worker

Do not update:

```text
framenest/.ap
libretiles/.ap
contextdesk/.ap
```

or any other consumer.

First complete the AP implementation candidate and validation.

Consumer adoption is a later explicit Cooperator-controlled step.

---

# 30. Terminal report

Return one complete terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Include:

- logical whole: `chat-orchestrator-offline-bundle-transport`;
- Worker profile and session freshness;
- starting AP HEAD;
- ending AP worktree state;
- confirmation that no commit/push occurred;
- exact files changed;
- concise semantic changes;
- exact implemented `ap bundle` CLI;
- exact chain-state location;
- exact default output behavior;
- initial algorithm;
- cumulative incremental algorithm;
- `.ap` handling;
- companion trace handling;
- other-submodule handling;
- tracked/history secret handling;
- the two post-planning Git corrections and how implemented;
- disposable validation scenarios and exact results;
- existing-command regression results;
- security review findings;
- known limitations;
- any divergence from the approved Planner design and why;
- `git diff --stat`;
- `git status --short`;
- recommended next AP phase.

Do not claim:

- acceptance PASS;
- publication PASS;
- deployment PASS;
- public branch equality after your edits;
- consumer adoption.

Stop after the terminal report.

Do not commit.
Do not push.