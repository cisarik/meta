# FrameNest — Worker 01 implementation: Cursor Worker execution-boundary convergence

🆕 **PROMPT FOR FRESH WORKER 01 • HIGH REASONING**

**Native Plan Mode: OFF.** Work directly. Do not spawn subagents. Do not ask
for another Worker. Do not close the logical whole.

You are one fresh WORKER instance under Analytic Programming. You are not the
ORCHESTRATOR.

The logical whole
`framenest-repeatable-immutable-nuc-release-deployment-contract` is
**CLOSED: PASS**. Do not reopen it. Do not perform production acceptance,
NUC deploy, rollback, or live catalog/service mutation.

```text
Persistent role identity: WORKER
Logical whole identity: framenest-cursor-worker-execution-boundary-convergence
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: FN-CURSOR-WORKER-EXEC-BOUNDARY-01
Reasoning recommendation: High
Recommendation basis: untrusted Cursor/AppImage ambient boundary; three capability routes (Python, SSH-agent, sudo lifecycle) plus one AP ledger observation; must converge existing owners without inventing a new environment manager
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Material phase gate: yes
Changed material axis: Worker execution and capability-route contract
Ordinary-only trigger: no
Routing reopened for: new bounded logical whole
Unchanged axes reopened: none
Evidence tier: E2
Evidence tier basis: repository documentation/contract/test change and at most a small existing SSH-gate extension; reversible; no live NUC mutation, sudoers, AP pin, or production cutover
Combined implementation envelope: allowed
Independent acceptance: recommended-separate-fresh-worker
Rollback or recovery checkpoint: not-applicable
Activated stricter profile: none
Publication authority: none
Deployment authority: none
NUC mutation authority: none
AP-pin / .ap mutation authority: none
Meta write authority: none
Git authority: one normal initial commit on a new clearly named local branch from the authorized baseline; no push; no local main; no amend; no force
```

This identity **supersedes** the unissued narrower proposal
`framenest-cursor-appimage-python-execution-boundary-convergence`. Use only
the identity above.

Read this complete prompt before acting. Do not rewrite or summarize AP.

## 1. Independence and baseline

```text
Repository: /home/agile/Projects/framenest
Public repository: https://github.com/cisarik/framenest.git
Authorized baseline: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Baseline tree: 4f5505c65f883a2eeba10d670e0a76f45c0f1a2a
Baseline parent: f5fbdce5669997f15c28ed6ffdad4cda849df4ee
Required public refs/heads/main: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Required AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/framenest
```

Expected starting checkout is the baseline SHA. Local `main` is stale and
must remain untouched. Preserve owner untracked paths; do not enumerate their
contents.

If this chat implemented the NUC EnvironmentFile deploy (`5abb2ad…`) or was
Worker 28/29 of the closed deploy whole, that retained context is convenience
only and is not this task's authority. Re-gate the repository.

## 2. Protocol and trace

```text
Canonical AP identity: https://github.com/cisarik/ap.git
Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Declared variant: stable
Governing variants in effect: one
Rules from non-governing variants: none
Migration required: no
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/
Trace project key: framenest
Trace logical-whole projection identity: 01-framenest-cursor-worker-execution-boundary-convergence
Trace authority: historical-evidence-only
Trace archival owner: Cooperator Michal; Worker must not archive
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Expected later archival pair after the report exists: 01_implementation_00.md + 01_report_00.md
```

```text
Orchestrator-to-Worker prompt language: professional English
Formal Worker report language: professional English
Required report header: ### Report for ORCHESTRATOR_CHAT
Logical-whole closure: not-closed
```

## 3. Mandatory reading

- root `AGENTS.md`
- `.ap/AP.md`, `.ap/AP_WORKER.md`
- `.ap/PROMPT_CONTRACTS.md` section **Upgrade Observation Ledger Contract**
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `ap.project.conf`
- `tests/contract/test_ap_project_contract.py`
- `scripts/operator/network/framenest_nuc_worker_gate.fish`
- `tests/contract/test_operator_network_scripts.py`
- `docs/OPERATOR_NETWORK.md` (SSH-gate / gpgconf / sanitization only)
- `scripts/operator/network/README.md`
- `docs/AP_UPGRADE_OBSERVATIONS.md`
- `docs/UBUNTU_NUC_DEPLOYMENT.md` same-schema privilege-release paragraph only
  (do not rewrite the runbook)

## 4. Goal

Make FrameNest-owned Worker execution and capability routes deterministic
under the untrusted Cursor/AppImage ambient environment, so future Workers
stop rediscovering Python, SSH-agent, and sudo lifecycle facts.

This is **route convergence**, not a new environment manager, Python wrapper,
AP pin change, workstation repair, or NUC change.

## 5. Known red field evidence (do not reproduce unless a named gap remains)

Authentic prior Cursor Worker episodes (treat as red evidence):

1. Raw `.venv/bin/python` / `poetry run` inherited AppImage `LD_LIBRARY_PATH`
   and failed at interpreter startup with `Failed to import encodings` /
   `No module named 'encodings'`. The same canonical interpreter passed
   focused tests when those loader variables were absent. `PYTHONPATH=<repo>/src`
   cannot repair `encodings`.
2. `docs/WORKER_EXECUTION_CONTRACT.md` still presents raw
   `PYTHONPATH=… .venv/bin/python` and `poetry run pytest` **before** the
   stronger `./.ap/ap exec` sanitized-envelope section. Orchestrator prompts
   copied the raw route; Workers bypassed the already-tested envelope.
3. Cursor Worker processes often lack `SSH_AUTH_SOCK` even when another
   terminal has it. Workers rediscovered `gpgconf --list-dirs agent-ssh-socket`
   instead of using `scripts/operator/network/framenest_nuc_worker_gate.fish`,
   which already discovers that socket without printing it. Some prior NUC
   prompts even **forbade** the project-owned gate.
4. Predecessor Workers correctly ran remote `sudo -K` at terminal evidence.
   A successor then saw `sudo -n` password-required and treated it as a broken
   NUC or failed `timestamp_timeout=1440` configuration. The global sudo
   timestamp is independent of local `SSH_AUTH_SOCK`.

Never paste complete environment values, socket paths, identity-file paths,
or sudoers contents into the report.

## 6. Required semantic outcomes

### 6.1 Python / test execution

- Cursor/AppImage ambient execution is untrusted.
- Cursor Workers must not directly invoke `.venv/bin/python`, `python`,
  `python3`, or `poetry run` for Python evidence.
- Canonical Cursor Worker route:
  `./.ap/ap project check` + `./.ap/ap exec` with an exact authorized
  `--baseline`.
- Poetry remains owner of `.venv` / lockfile. CPython 3.13 remains required.
  `ap.project.conf` remains `sanitized-v1` with operations `runtime-info`,
  `test`, `test-focus`. Do not change `ap.project.conf` unless evidence proves
  the existing envelope cannot express the route (current evidence says it can).
- Exact-source provenance comes from the envelope's declared `sourceRoot`,
  not ad-hoc ambient `PYTHONPATH` experimentation.
- Raw `.venv` / Poetry examples, if retained at all, are explicitly limited to
  a separately verified **clean human development shell** and are never to be
  rendered into Cursor Worker prompts.
- Fail-fast classification:
  - raw `encodings` startup signature → ambient-route violation;
  - do not inventory Pythons or rebuild anything;
  - rerun the **same gate once** through the canonical AP operation;
  - if AP exec passes, continue and report the ambient violation briefly;
  - if AP exec itself fails, stop as environment limitation with sanitized
    evidence; no automatic repair loop.

Verify the current CLI before hard-coding. Expected shape at this pin:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation runtime-info
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation test-focus -- <tests> -q -p no:cacheprovider
```

`--baseline` is execution-contract authority. It does not replace worktree
source, grant mutation, or make a local commit canonical.

### 6.2 SSH-agent capability route

Converge on the existing project-owned gate:

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
```

It already unsets AppImage loader classes, optionally discovers the GPG agent
SSH socket via trusted `gpgconf`, sets `SSH_AUTH_SOCK` for its own process
without printing it, and runs BatchMode SSH.

Inspect whether that is sufficient for a Cursor Worker that later runs a
local helper which must **inherit** the agent (for example future
`framenest-release` tasks). Decide the smallest change from evidence:

- If documentation/prompt prohibition was the only defect, document the gate
  as the canonical Cursor Worker SSH route and do not add a second script.
- If a real gap exists (no idempotent capability probe; parent Worker process
  cannot attach the agent without printing the socket or reconstructing
  `gpgconf`), extend **this same gate** with the smallest probe/attach
  behavior. Do not create a parallel SSH stack.

Canonical behavior after the change:

- idempotent GPG-agent socket discovery;
- capability validation without exposing the socket value;
- bounded BatchMode SSH proof **when a later task actually grants NUC access**;
- this task does **not** grant live NUC mutation; do not deploy, sudo, or
  run `framenest-release`.

Do not modify private keys, GPG configuration, Cursor installation, desktop
entries, or user shell startup files.

### 6.3 Remote sudo lifecycle

Document in the Worker execution contract (not in sudoers, not on the NUC):

- remote global sudo timestamp state is independent of local `SSH_AUTH_SOCK`;
- `sudo -K` intentionally invalidates the global timestamp for later Workers,
  even when `timestamp_timeout=1440`;
- each privileged Worker releases sudo at its terminal report;
- the Cooperator re-establishes the timestamp (`sudo -v`, then `sudo -n true`)
  **outside** the next privileged Worker;
- a successor seeing password-required after predecessor `sudo -K` classifies
  it as **expected lifecycle state**, not a broken NUC or failed global-sudo
  configuration;
- Workers must not run `sudo -v` or handle a password.

Do not modify `/etc/sudoers`, the timeout, live NUC files, or deployment
helpers unless a separately surfaced contradiction requires returning to the
Orchestrator. Prefer not to rewrite `docs/UBUNTU_NUC_DEPLOYMENT.md`; a single
cross-link is allowed only if leaving it would keep two equal Worker routes.

This Worker must not use `sudo`.

### 6.4 Universal AP field observation

Write **exactly one** bounded candidate observation into
`docs/AP_UPGRADE_OBSERVATIONS.md`. Do not mutate `.ap` or `cisarik/ap`.

Keep the required file header. Do not change the activation snapshot line
except if the current header is malformed (it is not). Append one record
using every ledger field exactly once:

```text
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

You may tighten `Summary` to one public-safe line if the line above is too
long, but keep the `Entry` identity byte-for-byte.

Field evidence to reflect (do not paste secrets or full transcripts):

FrameNest already declared a sanitized AP execution envelope and a
project-owned NUC SSH gate, but project guidance and authoritative Worker
prompts still offered or reconstructed ambient raw routes. That repeatedly
caused Cursor AppImage Python loader failure and repeated SSH-agent discovery.

Potential universal AP gap:

When a consuming project declares an execution operation or capability gate,
AP Orchestrator prompt construction may not bind Workers strongly enough to
that declared route or detect contradictory parallel ambient instructions.

Desired AP-level outcome:

A current Worker prompt uses the consumer-declared route by default. Any
deviation is explicit and justified. Ambient environment inheritance is never
assumed across Orchestrator, IDE, terminal, script, and Worker process
boundaries.

Non-goals (must appear in spirit in the summary/report, not as AP mutation):
AP does not become a Python, Poetry, uv, virtualenv, GPG, SSH, sudo, Cursor,
workstation, or deployment manager. Exact commands remain consumer-owned.

## 7. Allowlist

Derive the final used set from inspection. Do not exceed:

**Always in scope**

```text
AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md
tests/contract/test_ap_project_contract.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

**In scope only if §6.2 proves a real gate gap**

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
tests/contract/test_operator_network_scripts.py
docs/OPERATOR_NETWORK.md
scripts/operator/network/README.md
```

**Optional new focused test owner if cleaner than overloading the AP contract**

```text
tests/contract/test_worker_execution_contract.py
```

Out of scope: `.ap/`, `ap.project.conf` unless proven necessary, `deploy/`,
live NUC, sudoers, Poetry/uv lockfiles, product UI, Brave/X, closed deploy
whole, Meta.

`AGENTS.md` needs a short high-priority rule: Cursor/AppImage is untrusted;
Python/tests go through `./.ap/ap exec`; NUC SSH goes through the project
gate; sudo lifecycle is Cooperator-timestamp plus Worker `sudo -K`; do not
duplicate universal AP protocol.

## 8. Positive / negative authority

You may:

- inspect the owners above;
- edit only allowlisted paths;
- create one clearly named local branch from `5abb2ad…`;
- create **one** normal initial commit if the semantic outcomes are met;
- run the validation ladder in §9;
- optionally run **one** read-only BatchMode connectivity probe through the
  canonical gate with remote command equivalent to `true` only if §6.2
  requires proving attach from this Cursor parent. No other remote command.

You may not:

- push, publish, deploy, roll back, migrate, restore, or restart services;
- run `sudo`, `sudo -v`, or `sudo -K`;
- change `.ap`, the AP pin, `cisarik/ap`, or adopt a newer AP;
- repair `.venv`, run `uv sync` / `uv lock` / `pip install` / `poetry install`
  / `poetry env use`;
- change CPython 3.13 support or use global Python 3.14;
- set `PYTHONPATH` to repair `encodings`;
- search `/opt/*` or the filesystem for a replacement interpreter;
- modify shell rc files, Cursor settings, desktop entries, GPG/SSH keys;
- write Meta;
- close the logical whole;
- reopen the closed NUC-release whole.

## 9. Validation ladder (proportional)

Dogfood the Python route. After the first docs/contract edit, **all** Python
evidence in this session uses `./.ap/ap exec` with
`--baseline 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923` until you create the
implementation commit; after that commit, use that new SHA as `--baseline`
only for executing tests, not as publication authority.

1. Treat §5 as red field evidence. Do not spend the session reproducing the
   fatal encodings crash unless a named causal gap remains.
2. One narrow static red **before** mutation proving the ambiguous raw Worker
   command hierarchy still exists (raw `.venv` / `poetry run pytest` presented
   as an ordinary Worker route).
3. `./.ap/ap project check` against the authorized baseline, then
   `--operation runtime-info` from this actual Cursor parent.
4. `test-focus` on `tests/contract/test_ap_project_contract.py` and any new
   focused Worker-execution contract tests, `-q -p no:cacheprovider`.
5. Focused `tests/contract/test_operator_network_scripts.py` **only if** the
   gate or its tests change.
6. `fish -n` (or equivalent no-execute syntax check) for any changed fish
   script.
7. Direct semantic review of AGENTS.md, the execution contract, and the
   ledger entry against §6.
8. No full Python suite. No JS suite. No live deploy.

If a raw Python invocation is accidentally used and emits the encodings
signature, classify and rerun once through AP exec. Do not inventory Pythons.

## 10. Git

- Create a clearly named local branch from `5abb2ad…`.
- One normal commit. Message focuses on why: Cursor Workers must use declared
  AP exec / SSH-gate / sudo-lifecycle routes instead of ambient reconstruction.
- Do not touch local `main`.
- Do not push.
- Show the commit is a direct descendant of `5abb2ad…`.

## 11. Hard stop

Stop without improvising if:

- public `main` is no longer `5abb2ad…` and is not a descendant you may use
  as baseline without a new Orchestrator grant;
- the existing AP envelope cannot run `runtime-info` from this Cursor parent
  even after one encodings→AP-exec reroute;
- making the SSH route work would require editing GPG/SSH keys, shell rc,
  Cursor, sudoers, or the live NUC;
- the ledger header/declaration is malformed in a way that needs a separate
  reconciliation grant;
- the change wants to mutate `.ap` or `ap.project.conf` without a proven
  envelope gap.

## 12. Report contract

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo unchanged: logical whole identity, session 01, exchange 01, fresh-worker-session,
Native planning mode `not-used`.

Include:

- `PASS` | `PARTIAL` | `BLOCKED`;
- phase-qualified result `implementation-PASS` | `not-applicable`;
- `Logical-whole closure: not-closed`;
- start/end commit; changed files and why each is necessary;
- whether the SSH gate was extended or docs-only, with the causal gap;
- Python validation via AP exec (runtime-info + focused tests);
- fish syntax check if applicable;
- ledger entry identity and state `untriaged`;
- encodings/SSH/sudo classification rules now owned where;
- secrets omitted;
- one smallest next step (independent acceptance of this branch, not
  publication unless later granted);
- report justification `new-mutation` if you committed, else `new-evidence`;
- authority expiry;
- Near-Misses; Pre-Existing Failure Classification.

`PASS` / `implementation-PASS` only if §6 outcomes are in the commit (or you
honestly report that no commit was required because the repository already
satisfied them, which current evidence contradicts).

```text
Authority expiry: all Worker 01 exchange 01 implementation authority expires
at this terminal report
```
