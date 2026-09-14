### Report for ORCHESTRATOR_CHAT

Logical whole identity: `chat-orchestrator-offline-bundle-transport`  
Worker session ordinal: `01`  
Worker exchange ordinal: `01`  
Persistent role identity: WORKER  
Worker session profile: Implementation Worker  
Worker session target: fresh-worker-session  
Native planning mode: not-used  
Delivery route: manual Cooperator delivery  
Commit authority: not granted; no commit or push was performed

This is a terminal implementation report. It does not claim acceptance PASS, publication PASS, deployment PASS, public branch equality after these edits, or consumer adoption.

---

## Baseline and ending worktree

Starting AP HEAD (unchanged): `717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf`  
Branch: `feat/ap-practical-workflow-consolidation`  
Origin: `https://github.com/cisarik/ap.git`  
Public `origin/main` at start of work: same SHA  
Ending HEAD: same SHA (no commit)  
Ending worktree: dirty local candidate, uncommitted

Meta was not mutated. No consumer `.ap` pin was moved.

---

## Exact files changed

Modified:

- `ap`
- `AP.md`
- `AP_ORCHESTRATOR.md`
- `PROMPT_CONTRACTS.md`
- `PROMPT_ENGINEERING_PATTERNS.md`
- `GLOSSARY.md`
- `FAQ.md`
- `INTUITION.md`
- `INTEGRATION.md`
- `README.md`
- `UPDATING.md`
- `CHANGELOG.md`
- `docs/adr/README.md`

Added:

- `docs/adr/0025-chatorchestrator-offline-bundle-transport.md`

Unchanged as planned: `AP_WORKER.md`, `ARTIFACT_LIFECYCLE.md`, `INFOSEC.md`, `ap.project.conf`, historical ADR bodies, consumer repositories.

---

## Concise semantic changes

`AP.md` now owns two named evidence classes: **exact committed bundle evidence** and **independently observed current public branch evidence**. A verified ChatOrchestrator transport may establish the first; it must not be promoted into the second. The required limitation string is `public branch state not directly observed`.

RF-19 retrieval, §3 inspection clones, §12, §14 restoration, and Continuation Bootstrap Stage 1 no longer treat missing ChatOrchestrator GitHub reachability as a hard stop when the claim under decision is exact committed state. Public-ref, publication equality, and remote-sync claims remain unproven until an actor with GitHub capability establishes them.

First-Planner **native planning mode** stays required. **Delivery route** is a separate axis: ChatOrchestrator uses manual Cooperator ferry; a full Orchestrator with authorized functioning dispatch delivers the complete prompt, including the first Planner, unless opt-out, unavailable dispatch, or an independence/external-fresh-session constraint requires manual delivery.

Capsule tokens `ready`, `waiting`, `blocked`, and `partial` are routing presentation, not phase PASS or ORCHESTRATOR closure.

---

## Implemented `ap bundle` CLI

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

Runs from the standalone AP checkout via `require_tool_repository` (extracted from `require_context`). Existing `init`/`doctor`/`project`/`exec`/`update` still use `require_context` and keep their contracts.

Project-name rule: `^[A-Za-z0-9][A-Za-z0-9._-]*$`. Resolution order: `--root`; else stored chain root; else `--projects-root` / `AP_PROJECTS_ROOT` / `bundle.projectsRoot` / `$HOME/Projects/<project>` when that directory exists; else fail and ask for `--root`.

---

## Chain-state location

```text
${XDG_STATE_HOME:-$HOME/.local/state}/ap/bundle/<project>/chain.conf
```

Optional config: `${XDG_CONFIG_HOME:-$HOME/.config}/ap/bundle.conf` (`bundle.projectsRoot`, `bundle.outputDir`). Absolute paths stay user-local. Divergence from the Planner’s `<owner>--<repo>` directory key: the chain is keyed by the validated CLI project name so `ap bundle framenest` can resolve without already knowing origin. Origin identity is stored inside `chain.conf` and must still match on later exports.

---

## Default output behavior

1. `--output-dir` if given (must already be the physical directory)  
2. config `bundle.outputDir`  
3. `$XDG_DOWNLOAD_DIR` or `$HOME/Downloads` if that directory exists  
4. `${XDG_STATE_HOME:-$HOME/.local/state}/ap/bundle/packages/`

ZIP name: `<project>-ap-transport-<initial|update>-<UTC>-<head12>.zip`. Existing paths are refused, never overwritten. Final line: `READY: <absolute-zip-path>`.

Outer ZIP is built in a throwaway Git repo with `git archive --format=zip` (no `zip(1)`). Payload files only; `.gitattributes` used during packing is not included.

---

## Initial algorithm

Fail-closed preconditions: physical worktree root; HEAD is a commit; non-shallow; no `refs/replace`; clean index/worktree including untracked; local `remote.origin.url`; no Git LFS; exporter AP checkout clean and running `ap` matches `HEAD:ap`; no source mutation.

Consumers require initialized `.ap` gitlink, `.ap HEAD` equals gitlink, clean `.ap`, canonical AP identity. Canonical AP self-bundle (`ap bundle ap --initial`) omits `.ap`.

Creates `project.bundle` from `HEAD` (and the current branch ref when attached), plus `ap.bundle` from the `.ap` checkout `HEAD` after gitlink equality, plus companion/submodule bundles when configured. Records chain state. Manifest sets `publicVerification=not-performed`, `evidenceClass=exact-committed-bundle-evidence`, `publicBranchState=not-directly-observed`.

---

## Cumulative incremental algorithm

Current HEAD must have the recorded initial commit as ancestor (`merge-base --is-ancestor`). Same independently for `.ap` and companion.

```text
update = <initial>..HEAD
```

not adjacent `B..C`. Newest update applies onto the original initial snapshot. Unchanged components are omitted and marked `omitted-unchanged-from-initial`. If nothing relevant changed: `nothing new to export`. Non-ancestor history: fail and require `--initial --replace-chain`.

---

## `.ap` handling

Required for non-canonical consumers. Bundled from the `.ap` checkout using `HEAD` after verifying HEAD equals the superproject gitlink. Incremental: `initialAp..HEAD` when the gitlink moved forward.

---

## Companion trace

Explicit `--companion-trace <physical-git-root>` on `--initial` only. Stored in chain state. Later `ap bundle <project>` includes a cumulative companion bundle automatically when companion HEAD changed. An update containing only companion change is valid. Unconfigured siblings, including Meta, are never guessed. No hardcoded `cisarik/meta`.

---

## Other submodules

Default fail-closed: unexpected HEAD gitlinks abort export with the path list. `--include-submodule <relpath>` includes that gitlink’s local checkout at the exact gitlink SHA. Filename `submodule-<path-with-slashes-as-double-dash>.bundle`. No network fill.

---

## Tracked/history secret handling

Scan of `git rev-list --objects` for the exported range (initial: ancestors of HEAD; incremental: `initial..HEAD`). Conservative names include `.env` / `.env.*` except `.env.example`, private key basenames, `*.pem`/`*.p12`/`*.pfx`/`*.key`/`*.keystore`/`*.jks`, `credentials.json`, `secrets.json`, `secrets.yaml`, `.netrc`, `.pypirc`. Hit: print paths, refuse, no package. `--allow-path` is an exact exception recorded in the manifest. No `--force`. Filename scanning is not claimed to prove absence of secrets. Objects are never stripped.

---

## Two post-planning Git corrections

1. **Do not `git bundle create` from a raw unreferenced gitlink SHA.** Implementation bundles `.ap` and included submodules from the checkout `HEAD` after verifying HEAD equals the gitlink.

2. **`git bundle verify` for incremental packages runs in the reconstructed repository** so prerequisites are checked. Initial packages use a throwaway `git init --bare` verification repo (always valid). On this host Git 2.55 also verifies an initial bundle outside a repository; IMPORT.md does not treat that as public evidence and still documents the bare-repo method. Incremental `git fetch` of a superproject bundle uses `--no-recurse-submodules` so Git does not try to fill gitlinks from the network.

---

## Disposable validation (55 PASS / 0 FAIL)

One-shot fixtures under `/tmp/ap-bundle-smoke.*` (not committed). Real `git bundle` create/verify/clone/fetch.

| Scenario | Result |
|---|---|
| initial export | PASS |
| unzip/readback and sha256 checksums | PASS |
| exact reconstruction without network | PASS |
| initial verify in repo context | PASS |
| cumulative incremental export/import | PASS |
| skip intermediate update (initial+C ⇒ C) | PASS |
| dirty project refusal | PASS |
| non-ancestor initial refusal | PASS |
| missing `.ap` refusal | PASS |
| mismatched `.ap HEAD` vs gitlink | PASS |
| ignored `.env` absent from bundle | PASS |
| tracked `.env` refusal | PASS |
| `--allow-path .env` recorded | PASS |
| changed `.ap` pin forward + reconstruct | PASS |
| lost prerequisite ⇒ new `--initial` | PASS |
| unexpected extra submodule refusal | PASS |
| explicit `--include-submodule` | PASS |
| configured companion included | PASS |
| companion-only useful update | PASS |
| unconfigured sibling/Meta not guessed | PASS |
| export with invalid HTTP proxy | PASS (first export) |
| no `ls-remote`/`fetch` in export path | PASS |
| canonical AP self-bundle, no `ap.bundle` | PASS |
| `zip(1)` not required | PASS |
| `init` / `doctor` | PASS |
| `project check --candidate/--baseline` | PASS |
| `exec` runtime-info | PASS |
| `update` still requires `--check`/`--apply` | PASS |
| unique ZIP / no overwrite / nothing-new | PASS |
| slash and `..` project names refused | PASS |

`update --check` was not executed against GitHub (it still fetches origin main by design). Argv/contract of `update` is unchanged.

---

## Security review findings

- No `eval`. User values quoted. `--` used before `git archive` pathspecs.  
- Project names reject slashes/traversal. `--root` and other roots must already be physical paths; `..` components refused.  
- Gitlink paths with whitespace refused. Ambient `GIT_DIR`/`GIT_WORK_TREE` unset for export Git.  
- Temps via `mktemp -d …/ap-bundle.XXXXXX`, cleaned on EXIT. Throwaway zip repo is not the source object DB.  
- Export does not `fetch`/`ls-remote`/clone remotes. Ignored worktree files cannot enter (Git objects only).  
- Companion inclusion is explicit. Chain origin/root/name must match. Checksums use `sha256  <hex>  <filename>` with space-free names; manifest is `git config -f` syntax.  
- Residual: filename scanning is incomplete by design; `--allow-path` is an explicit hole recorded in the ZIP; huge histories may exceed ChatGPT attach limits (operational, not solved here).

---

## Known limitations

- ChatGPT attachment size is a Cooperator operational limit.  
- Incremental verify/fetch requires the same-chain inspection checkout.  
- Once a suspicious path is in exported history, later incrementals covering that range still fail unless `--allow-path` is repeated or a new history without that path is used.  
- `ap bundle` requires a clean exporter AP checkout matching `HEAD:ap`.  
- Git LFS, shallow clones, and `refs/replace` are refused.

---

## Divergence from the approved Planner design

1. Chain directory keyed by project name, not `<owner>--<repo>`, so name-only incremental lookup works; origin identity is still enforced.  
2. Incremental bundles use only `<initial>..HEAD` (no extra branch ref) so Git does not union full branch history into an incremental package.  
3. Manifest payload hashes use `bundle.hash-<sanitized-filename>` because `git config` keys cannot contain `_`.  
4. IMPORT.md incremental fetch documents `--no-recurse-submodules`.  
5. IMPORT.md does not claim that every Git version refuses `git bundle verify` outside a repository (Git 2.55 does not).

---

## `git diff --stat`

```text
 AP.md                          |  150 +++++-
 AP_ORCHESTRATOR.md             |   19 +-
 CHANGELOG.md                   |   11 +
 FAQ.md                         |   16 +-
 GLOSSARY.md                    |    7 +-
 INTEGRATION.md                 |   10 +-
 INTUITION.md                   |    4 +-
 PROMPT_CONTRACTS.md            |   22 +-
 PROMPT_ENGINEERING_PATTERNS.md |    4 +-
 README.md                      |    6 +
 UPDATING.md                    |    3 +
 ap                             | 1165 +++++++++++++++++++++++++++++++++++++++-
 docs/adr/README.md             |    9 +
 13 files changed, 1383 insertions(+), 43 deletions(-)
```

Untracked: `docs/adr/0025-chatorchestrator-offline-bundle-transport.md`

## `git status --short`

```text
 M AP.md
 M AP_ORCHESTRATOR.md
 M CHANGELOG.md
 M FAQ.md
 M GLOSSARY.md
 M INTEGRATION.md
 M INTUITION.md
 M PROMPT_CONTRACTS.md
 M PROMPT_ENGINEERING_PATTERNS.md
 M README.md
 M UPDATING.md
 M ap
 M docs/adr/README.md
?? docs/adr/0025-chatorchestrator-offline-bundle-transport.md
```

---

## Recommended next AP phase

Independent Acceptance / Audit of this local AP candidate by a fresh Worker, then Cooperator-controlled commit if accepted. Consumer pin adoption remains a later explicit step. This Worker does not commit or push.