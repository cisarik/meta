Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 02
Worker exchange ordinal: 01

# Authoritative Prompt for Fresh Worker 2

## Implement the Repository-Native Mullvad Egress and Network Recovery Contract

Persistent role identity: one fresh Worker instance assigned to the WORKER role
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Evidence posture: non-independent
Implementation authority: explicit
Fresh-worker session: required
Worker topology: single-active
Internal delegation posture: not-used
Reasoning recommendation: High

High reasoning is recommended because this repository-only slice creates future operator controls for two Linux hosts and must encode fail-closed validation, shell safety, privacy sanitization, version skew, noninteractive SSH, and headless recovery without executing any live networking change.

Read this complete prompt before acting.

## 1. Continuity and accepted planning decision

Worker 1 completed the only initial planning cycle and returned a terminal `PARTIAL` report. All Worker 1 authority expired.

The ORCHESTRATOR accepts that plan for this repository implementation phase without a targeted revision.

The `PARTIAL` status arose because `/home/agile/Projects/framenest` is an old, dirty owner checkout on another branch. It does not invalidate the architecture or block an isolated worktree created from the verified public baseline.

Do not reuse Worker 1’s session. Do not repeat its live inventory.

Accepted current facts:

* both devices are healthy members of one tailnet;
* SSH from `ahw` to `framenest-nuc` currently uses Tailscale;
* neither device currently uses or advertises an exit node;
* both currently expose ISP/non-Mullvad egress;
* `ahw` has Mullvad exit nodes available;
* the NUC currently lacks Mullvad access;
* `ahw` runs Tailscale `1.98.10` and lacks `tailscale get`;
* the NUC runs Tailscale `1.102.2` and supports `tailscale get`;
* the standalone Mullvad daemon is installed and active on `ahw`;
* FrameNest Serve remains tailnet-only through its protected Unix socket;
* the selected architecture is independent explicit Mullvad exit-node selection on each device;
* chained routing through `ahw`, `auto:any`, mandatory exit-node policy, LAN access by default, custom boot units, and public exposure are rejected.

This prompt authorizes source implementation only. It does not authorize any host or network action.

## 2. Verified public anchors

The ORCHESTRATOR directly reverified these refs:

```text
FrameNest public main:
148b6c2012809944262399c1a166e85082606fbf

FrameNest tree:
1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366

FrameNest parent:
5fe07b01bdfd587919d38a3d59ddd00e004d7394

AP public main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

FrameNest AP gitlink:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Meta public main:
dae7715ddec0810cab2ed5ba4adfbdcfd6459048
```

Meta commit `dae7715d…` atomically added:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_planning.md
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_report.md
```

Meta is historical evidence only.

## 3. Repository identities and working locations

```text
Canonical FrameNest repository:
https://github.com/cisarik/framenest.git

Owner checkout:
 /home/agile/Projects/framenest

Authorized isolated worktree:
 /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2

Authorized branch:
feat/tailnet-mullvad-egress-recovery-contract

Exact baseline:
148b6c2012809944262399c1a166e85082606fbf
```

The owner checkout contains unrelated owner work and untracked files. Preserve it exactly.

Do not modify, clean, reset, stash, checkout, switch, stage, or commit in the owner checkout.

## 4. Mandatory reading

Before mutation, read:

```text
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/.ap/AP.md
/home/agile/Projects/framenest/.ap/AP_WORKER.md
/home/agile/Projects/framenest/.ap/PROMPT_CONTRACTS.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
```

After creating the exact worktree, inspect the baseline versions of:

```text
README.md
SERVER.md
SECURITY.md
docs/UBUNTU_NUC_DEPLOYMENT.md
deploy/ubuntu/README.md
docs/adr/README.md
docs/adr/0048-tailscale-remote-access-and-identity-foundation.md
docs/adr/0047-operator-cli-configuration-and-working-directory-hygiene.md
docs/adr/0057-operator-workstation-pull-based-catalog-snapshot.md
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_ap_integration.py
```

ADR number `0058` is currently unused on the accepted baseline.

## 5. Repository and recovery gate

From the owner checkout, perform read-only checks first:

```bash
pwd -P
git status --short --branch
git remote get-url origin
git rev-parse HEAD
git worktree list --porcelain
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote origin refs/heads/main
```

Expected public `main` is exactly:

```text
148b6c2012809944262399c1a166e85082606fbf
```

Confirm the authorized worktree path does not exist and the authorized branch name is unused.

Do not delete, reuse, overwrite, or repair an existing path or branch. If either already exists, stop and report the evidence.

If the exact baseline object is absent locally, the only authorized fetch is:

```bash
env GIT_TERMINAL_PROMPT=0 \
  git fetch --no-tags origin \
  148b6c2012809944262399c1a166e85082606fbf
```

Do not fetch another ref or update `origin/main`.

Verify the fetched or existing object:

```bash
git cat-file -e \
  148b6c2012809944262399c1a166e85082606fbf^{commit}

git show -s \
  --format='%H%n%T%n%P%n%s' \
  148b6c2012809944262399c1a166e85082606fbf
```

Authorized worktree creation:

```bash
git worktree add \
  -b feat/tailnet-mullvad-egress-recovery-contract \
  /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2 \
  148b6c2012809944262399c1a166e85082606fbf
```

Inside the new worktree, initialize only the pinned AP submodule when necessary:

```bash
git submodule update --init .ap
```

Expected `.ap` HEAD and containing-repository gitlink:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Submodule initialization is setup authority, not AP mutation authority.

After setup, require:

```text
worktree HEAD = 148b6c2012809944262399c1a166e85082606fbf
worktree branch = feat/tailnet-mullvad-egress-recovery-contract
worktree porcelain = clean
origin = cisarik/framenest
.ap HEAD = containing-repository gitlink
```

Any unexplained divergence stops mutation.

## 6. Exact changed-path allowlist

You may create or modify only:

```text
docs/adr/0058-independent-mullvad-egress-and-operator-network-recovery.md
docs/adr/README.md
docs/OPERATOR_NETWORK.md
scripts/operator/network/README.md
scripts/operator/network/framenest_mullvad_egress.sh
scripts/operator/network/framenest_mullvad_egress.fish
scripts/operator/network/framenest_nuc_worker_gate.fish
tests/contract/test_operator_network_scripts.py
README.md
SERVER.md
SECURITY.md
docs/UBUNTU_NUC_DEPLOYMENT.md
deploy/ubuntu/README.md
```

No other tracked path may change.

Explicitly forbidden:

```text
.ap
.gitmodules
ap.project.conf
pyproject.toml
poetry.lock
uv.lock
src/**
migrations/**
deploy/systemd/**
docs/NUC_HOST_BASELINE.md
PRODUCT.md
SPEC.md
ROADMAP.md
```

Do not change dependencies, schemas, application behavior, systemd units, deployment code, Tailscale Serve configuration, or AP integration.

## 7. Primary implementation outcome

Produce one coherent repository-native operator foundation that:

* records the accepted independent Mullvad egress architecture;
* distinguishes Tailscale Serve ingress from public-internet egress;
* provides public-safe operator documentation;
* provides a Bash implementation shared by CachyOS and Ubuntu;
* provides a thin Fish wrapper for `ahw`;
* provides a strict noninteractive Fish SSH gate for the NUC;
* supports `status`, `enable`, `disable`, `verify`, and `recover`;
* detects installed-client feature differences;
* refuses unsafe or ambiguous states;
* never embeds secrets or host-private values;
* is behaviorally tested using synthetic fake tools;
* performs no real networking or host mutation during this Worker task.

## 8. ADR-0058 contract

Create:

```text
docs/adr/0058-independent-mullvad-egress-and-operator-network-recovery.md
```

Title:

```text
ADR-0058: Independent Mullvad Egress and Operator Network Recovery
```

Status:

```text
Accepted
```

Decision date:

```text
2026-08-13
```

The ADR must establish:

* `ahw` and `framenest-nuc` select Mullvad exit nodes independently;
* direct tailnet/MagicDNS communication remains overlay traffic;
* Tailscale Serve ingress remains unchanged and tailnet-only;
* FrameNest gains no public listener or inbound exposure;
* `ahw` is not advertised as an exit node;
* exit-node chaining is unsupported and rejected;
* `auto:any` is rejected because it may select a non-Mullvad exit node;
* an explicit verified `*.mullvad.ts.net` node is required;
* `--exit-node-allow-lan-access=false` is the default;
* standalone Mullvad routing must not compete with Tailscale Mullvad egress;
* mandatory exit-node/MDM policy is rejected for this owner-operated Linux setup;
* persisted Tailscale preferences are preferred over custom boot services;
* no firewall, NetworkManager, Wi-Fi, router, manual-route, forwarding, or sysctl change belongs to this contract;
* host mutations remain separately authorized;
* the headless NUC requires an automatic transient rollback before exit-node mutation;
* the privacy goal is Mullvad public egress, not anonymity;
* Tailscale remains identity-aware;
* public verification must sanitize IPs, tailnet identity, account data, and node metadata.

Do not encode an exact city, Mullvad hostname, tailnet name, IP address, local username, account email, key path, fingerprint, or private host fact.

Update the ADR index with one exact row.

## 9. Operator documentation contract

Create:

```text
docs/OPERATOR_NETWORK.md
```

It must be the durable operator contract and contain:

* artifact classification, consumers, retention, and inbound links;
* accepted topology;
* rejected topology;
* privacy limitations;
* installed-command feature detection;
* the five script subcommands;
* `ahw` sequence;
* NUC sequence;
* human admin-console gate;
* `NeedsLogin` stop behavior;
* standalone Mullvad conflict handling;
* full MagicDNS recommendation without a real tailnet suffix;
* explicit-node validation;
* LAN-access/DNS posture;
* optional future `--operator` decision;
* transient NUC rollback design;
* one-device-at-a-time reboot acceptance;
* disable and recovery procedures;
* output sanitization;
* no public inbound exposure;
* no credential storage.

Use placeholders such as:

```text
<operator-user>
<nuc-magicdns-name>
<identity-file>
<mullvad-node>.mullvad.ts.net
```

Do not include the real SSH identity filename, local absolute home paths, fingerprint, account identifiers, exact tailnet suffix, public IP, or exact current Mullvad suggestion.

The document may describe the future admin-console action, but must make clear that repository presence grants no account or host authority.

Add concise discoverability links in the other allowed documentation paths. Avoid copying the full operator contract into each file.

Do not change stale production SHA claims unrelated to this network whole.

## 10. Bash script interface

Create executable:

```text
scripts/operator/network/framenest_mullvad_egress.sh
```

Public interface:

```text
framenest_mullvad_egress.sh status
framenest_mullvad_egress.sh enable --node <verified-mullvad-dns-name>
framenest_mullvad_egress.sh disable
framenest_mullvad_egress.sh verify
framenest_mullvad_egress.sh recover
```

The implementation must:

* use Bash with strict error handling;
* avoid `eval`;
* avoid constructed shell source;
* avoid broad globs;
* validate every argument before invoking a tool;
* reject unknown flags and extra operands;
* reject empty, whitespace-containing, option-like, non-DNS, or non-Mullvad node values;
* accept only a normalized hostname ending exactly in `.mullvad.ts.net`;
* never use `auto:any`;
* never invoke `tailscale up`, `tailscale down`, `tailscale login`, or `tailscale logout`;
* never advertise an exit node;
* never change accepted routes, DNS, Serve, Funnel, SSH, firewall, routes, Wi-Fi, NetworkManager, forwarding, or sysctl state;
* set an explicit Mullvad exit node only through `tailscale set`;
* set LAN access false on enable;
* clear the selected exit node on disable and recover;
* preserve and report the first causal error;
* distinguish tool failure from non-Mullvad egress;
* sanitize public diagnostic output;
* never print an exact public IP;
* never print raw `tailscale status --json`;
* stop on `NeedsLogin`;
* stop when Mullvad nodes are unavailable;
* stop when the device advertises itself as an exit node;
* stop if competing standalone Mullvad routing is positively detected;
* treat active Mullvad daemon presence separately from proof of an active Mullvad tunnel;
* handle the absence of `tailscale get`;
* use a read-only fallback supported by the observed older client when needed;
* avoid assuming the two machines expose identical CLI surfaces;
* never configure `--operator`;
* never invoke `sudo` automatically;
* provide an exact, short permission-denied explanation when a configured operator or separately authorized sudo action is needed;
* make `status` non-mutating;
* make `verify` contact only the documented Mullvad diagnostic endpoint when explicitly invoked by an operator;
* reduce the endpoint response to `Mullvad egress`, `non-Mullvad egress`, or `unknown`;
* use one sequential diagnostic call;
* fail when transport, status, or parsing cannot establish the fact;
* scrub AppImage/Cursor pollution before invoking operating-system tools.

At minimum, scrub these inherited variables for child tools:

```text
APPIMAGE
APPDIR
ARGV0
LD_LIBRARY_PATH
LD_PRELOAD
```

Use a bounded trusted executable search strategy. Tests may inject fake absolute tool paths through an explicit test-only or validated command-resolution mechanism, but production behavior must not silently execute a repository-local or current-directory binary.

The implementation must not perform a real Tailscale or Mullvad command during this task.

## 11. Fish wrapper

Create executable:

```text
scripts/operator/network/framenest_mullvad_egress.fish
```

It must:

* be a thin wrapper around the adjacent Bash implementation;
* resolve its own directory safely;
* avoid recursive shell or GUI launch;
* remove the same AppImage/Cursor environment variables;
* preserve arguments without string concatenation or `eval`;
* return the Bash script’s exact exit status;
* contain no networking logic duplicated from Bash.

## 12. NUC SSH gate

Create executable:

```text
scripts/operator/network/framenest_nuc_worker_gate.fish
```

It must provide the strict operator transport without hardcoding private values.

Require explicit values through arguments or public-safe environment variables for:

```text
remote target
remote user
identity file
bounded remote command
```

Do not hardcode:

```text
michal
agile
/home/agile
a real identity filename
a real fingerprint
a real tailnet suffix
an IP address
```

Required SSH properties:

```text
BatchMode=yes
RequestTTY=no
StrictHostKeyChecking=yes
IdentitiesOnly=yes
ForwardAgent=no
ClearAllForwardings=yes
ConnectTimeout=10
ServerAliveInterval=15
ServerAliveCountMax=2
```

When `gpgconf --list-dirs agent-ssh-socket` succeeds, use that socket without printing it. Do not enumerate SSH keys or print fingerprints.

Use Fish arrays. Do not use `eval`, `sh -c`, constructed quoting, forwarding, TTY fallback, `accept-new`, interactive password fallback, or automatic `known_hosts` mutation.

The script must transmit only the explicitly supplied bounded command.

## 13. Synthetic behavioral tests

Create:

```text
tests/contract/test_operator_network_scripts.py
```

Tests must not contact a real network or real host.

Use temporary synthetic fake executables and fixtures to test behavior. Exact temporary roots belong to pytest-managed `tmp_path`; report cleanup outcome.

Test at least:

1. all expected files exist and executable modes are correct;
2. Bash and Fish surfaces expose only the intended interface;
3. unknown subcommand fails without invoking fake `tailscale`;
4. `enable` without `--node` fails;
5. option-like, whitespace-containing, malformed, and non-Mullvad node names fail;
6. a valid explicit Mullvad hostname produces exactly the expected fake `tailscale set` arguments;
7. enable includes LAN access false;
8. no command uses `auto:any`;
9. disable clears only the selected exit node;
10. recover clears only the selected exit node and preserves the first failure;
11. `NeedsLogin` blocks mutation;
12. missing Mullvad availability blocks mutation;
13. self-advertised exit-node state blocks mutation;
14. a positively detected competing standalone Mullvad tunnel blocks mutation;
15. an active daemon without proof of a tunnel is not silently called connected;
16. absence of `tailscale get` uses the bounded read-only fallback or returns a precise unsupported-state error;
17. diagnostic transport failure yields `unknown`/failure and does not claim non-Mullvad egress;
18. Mullvad and non-Mullvad diagnostic fixtures are classified without printing fixture IPs;
19. raw status JSON is not emitted;
20. AppImage/Cursor variables do not reach fake child tools;
21. the Fish wrapper preserves arguments and exit status;
22. the SSH gate includes every required option;
23. the SSH gate rejects missing target/user/identity/command;
24. the SSH gate contains no private values;
25. no script contains forbidden GUI, networking, forwarding, or destructive commands;
26. no script configures `--operator` or invokes `sudo`;
27. documentation contains no real IP, tailnet suffix, fingerprint, account email, or private absolute home path.

You may adjust exact test mechanics to fit repository conventions, but do not weaken the behavioral claims.

## 14. Validation environment

Do not create, delete, move, copy, symlink, or reconstruct any `.venv`.

Do not run:

```text
poetry env use
uv sync
uv lock
pip install
poetry install
```

Use the canonical CPython 3.13 interpreter:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

For candidate-source tests, set:

```text
PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src
```

Before trusting Python evidence, prove:

```python
import framenest
print(framenest.__file__)
```

It must resolve below the exact worktree’s `src/`.

Clear only interfering AppImage variables for execution. Do not reconstruct the environment.

Required validation:

```bash
bash -n scripts/operator/network/framenest_mullvad_egress.sh
fish -n scripts/operator/network/framenest_mullvad_egress.fish
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish
```

If Fish is unexpectedly unavailable, classify that as an environment limitation. Do not install it.

Run focused candidate tests through the canonical interpreter:

```bash
PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src \
  /home/agile/Projects/framenest/.venv/bin/python \
  -m pytest \
  tests/contract/test_operator_network_scripts.py \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_integration.py
```

Also require:

```bash
git diff --check
git status --short
```

Inspect the complete diff and confirm only allowlisted paths changed.

No real invocation of these commands is allowed during validation:

```text
tailscale
mullvad
ssh
sudo
systemctl
systemd-run
curl to a live endpoint
```

Synthetic fake executables in pytest are allowed.

## 15. Git authority

Authorized Git writes are limited to:

* the exact isolated worktree creation above;
* initialization of the pinned `.ap` checkout;
* creation of the exact authorized branch;
* staging only the exact changed-path allowlist;
* one implementation commit.

Before staging or committing, re-run:

```bash
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote origin refs/heads/main
```

It must still equal:

```text
148b6c2012809944262399c1a166e85082606fbf
```

If public `main` advanced, stop before commit and report the exact divergence. Do not merge, rebase, cherry-pick, or silently rebaseline.

Do not use:

```text
git add .
git add -A
git commit -a
git push
git merge
git rebase
git stash
git reset
git clean
git checkout
git switch
git tag
```

Stage only explicit allowlisted paths.

Authorized commit subject:

```text
feat: add Mullvad egress recovery controls
```

Exactly one commit.

No push or publication authority exists.

After commit, verify:

```bash
git status --short
git show --stat --oneline HEAD
git diff --check HEAD^ HEAD
git diff --name-status HEAD^ HEAD
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD^
```

The worktree must be clean. Preserve the candidate for independent acceptance.

## 16. Negative authority

Do not:

* connect or disconnect a real exit node;
* run any real Tailscale CLI command beyond the initial public Git work;
* run the standalone Mullvad CLI;
* inspect or alter the Mullvad daemon;
* SSH to the NUC;
* invoke sudo;
* invoke systemctl or systemd-run;
* contact an egress/DNS diagnostic endpoint;
* open the Tailscale admin console;
* assign Mullvad access;
* configure a Tailscale operator;
* mutate DNS, routes, firewall, Wi-Fi, NetworkManager, router, KDE, forwarding, or sysctl;
* restart or reboot anything;
* deploy FrameNest;
* alter Tailscale Serve or Funnel;
* inspect credentials, SSH keys, browser state, environment secrets, private media, or production data;
* publish or push;
* mutate AP or Meta;
* fix unrelated stale production SHA documentation;
* rewrite `NUC_HOST_BASELINE.md`;
* add boot services or systemd units;
* add `connect_via_ahw.sh`;
* add an exact Mullvad city or node default;
* implement automatic live NUC rollback in this repository task;
* begin live acceptance.

Available credentials or connectivity are capability context, not authority.

## 17. Completion criteria

Implementation may report `PASS` only when:

* the exact isolated worktree began at `148b6c201…`;
* only allowlisted files changed;
* ADR-0058 records the accepted architecture;
* the operator document is public-safe and decision-complete;
* all three scripts follow the exact authority and privacy boundary;
* behavioral tests use only synthetic tools;
* Bash and Fish syntax checks exit zero;
* the focused pytest invocation exits zero;
* provenance resolves to candidate source;
* `git diff --check` exits zero;
* direct public `main` recheck still equals the baseline;
* exactly one authorized commit exists;
* the worktree is clean;
* no real host, network, provider, admin-console, publication, deployment, AP, or Meta mutation occurred.

A non-zero required command, traceback, real-tool invocation, forbidden path change, baseline mismatch, or unexplained divergence forbids PASS.

Correct defects inside the exact allowlist when possible before the single commit. Stop when correction would require another path or authority class.

## 18. Report contract

The terminal report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

```text
Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Include:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact candidate SHA or not-applicable>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk
Authority expiry: all Worker 2 authority expired at this terminal report
```

Also report:

* fresh-session and Native Plan Mode confirmation;
* start commit, end commit, tree, and parent;
* isolated worktree and branch;
* repository and public-ref gates;
* exact changed files and purpose;
* executable modes;
* syntax checks;
* exact test command and exit status;
* candidate-source provenance;
* Git diff and cleanliness evidence;
* whether any live networking command ran;
* whether any host, NUC, provider, sudo, account, publication, deployment, AP, or Meta mutation occurred;
* deviations, limitations, or residual risks;
* `Resolved Execution Issues / Near-Misses`;
* `Pre-Existing Failure Classification`;
* one smallest next step.

Do not claim independent acceptance, publication, deployment, production acceptance, or closure.

The expected next route after an implementation PASS is a fresh Worker 3 independent repository acceptance of the exact candidate. That statement grants no Worker 3 authority.

## 19. External trace lifecycle

```text
External trace disposition: configured
Trace discovery: projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/
Trace project key: framenest
Trace logical-whole projection identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Trace authority: historical-evidence-only
Trace archival owner: separately authorized archive workflow after the terminal outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

This exact prompt is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/02_implementation.md
```

The actual terminal report is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/02_report.md
```

Do not write either Meta file. They may be archived together only after the report exists by a separately authorized archival owner.

## 20. Stop conditions

Stop and report honestly if:

* this is not a fresh Worker session;
* Native Plan Mode is active;
* the owner checkout would need mutation;
* the exact worktree path or branch already exists;
* repository identity fails;
* the exact baseline object cannot be verified;
* public `main` differs from the expected baseline;
* `.ap` differs from the expected gitlink;
* owner work would be overwritten or exposed;
* required files outside the allowlist must change;
* a private value would need to enter committed content;
* a real network or host command would be needed;
* a required test fails and cannot be corrected inside authority;
* Fish or the canonical CPython environment is unusable;
* validation imports non-candidate source;
* a second commit would be required;
* implementation and the single authorized commit are complete.

At the terminal report, all Worker 2 authority expires.
