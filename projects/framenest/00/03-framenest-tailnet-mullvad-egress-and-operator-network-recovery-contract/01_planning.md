Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 01
Worker exchange ordinal: 01

# Authoritative Prompt for Fresh Worker 1

## FrameNest Tailnet Mullvad Egress and Operator Network Recovery — Read-Only Planning

Persistent role identity: one fresh Worker instance assigned to the WORKER role
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Worker-Executed Preflight
Worker role: read-only network architecture and implementation planner
Phase: Preflight and implementation-planning
Fresh-worker session: required
Evidence posture: independent
Authority renewal: not applicable; this fresh Worker receives authority only from this complete prompt
Reasoning profile requested by Cooperator: Extra High
Internal delegation posture: not-used
Worker topology: single-active

Read this complete prompt before acting.

Your sole objective is to produce a repository-grounded, live-state-informed, decision-complete implementation plan for a stable and lockout-resistant Tailscale Mullvad egress and operator recovery contract for Michal’s CachyOS workstation `ahw` and headless Ubuntu production server `framenest-nuc`.

Do not implement the plan.

## 1. Planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded architecture, current read-only network inventory, smallest repository mutation boundary, one-device-at-a-time implementation sequence, automatic NUC rollback, and final acceptance design
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

Initial planning record:

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Planning authority expires when you submit the terminal report. Native Plan approval, an automatic mode transition, retained context, “Continue,” or equivalent UI action grants no implementation authority.

## 2. Authority

```text
Implementation authority: none
Repository mutation authority: none
FrameNest Git-write authority: none
AP mutation authority: none
Meta mutation authority: none
PC mutation authority: none
NUC mutation authority: none
Tailnet mutation authority: none
Tailscale admin-console mutation authority: none
Mullvad account or entitlement mutation authority: none
Deployment authority: none
Production mutation authority: none
Credential authority: none
Secret-inspection authority: none
Browser or GUI authority: none
```

Authorized effects are limited to:

* read-only inspection of the three declared repositories;
* direct read-only public Git ref verification;
* current official Tailscale/Mullvad documentation research;
* read-only inspection of `ahw`;
* read-only, noninteractive SSH inspection of `framenest-nuc`;
* minimum-necessary sequential public egress/DNS diagnostics when needed to classify current state.

Current-phase evidence tier: E0 read-only evidence collection.

The anticipated future implementation is at least E3 because it will mutate networking preferences on a production host with material availability and recovery consequences. This planning task does not authorize that future envelope.

Do not stage, commit, push, fetch, pull, checkout, switch, reset, clean, stash, create worktrees, edit files, install packages, restart services, alter preferences, or create temporary repository artifacts.

## 3. Communication and ownership

Persistent roles:

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh session
```

The ORCHESTRATOR owns plan acceptance, Worker routing, future implementation authority, acceptance routing, publication, deployment, production acceptance, and logical-whole closure.

Michal owns account-level actions, identity-provider login, material privacy choices, lockout risk, physical-console actions, and acceptance of any residual operational risk.

Write the plan and terminal report in professional English.

Do not emit an Orchestrator closure signal. Use:

```text
Logical-whole closure: not-closed
```

## 4. Verified restoration anchors

The ORCHESTRATOR independently verified these public refs through direct Git transport on 2026-08-13:

```text
FrameNest public main:
148b6c2012809944262399c1a166e85082606fbf

FrameNest tree:
1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366

FrameNest parent:
5fe07b01bdfd587919d38a3d59ddd00e004d7394

FrameNest subject:
fix: restore upload validation layer boundary

FrameNest AP gitlink:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

AP public main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Meta public main:
59e87fa5479844c8c54ed99a93aa06b9ea90a01a
```

Repository identities and normal local locations:

```text
FrameNest:
https://github.com/cisarik/framenest.git
/home/agile/Projects/framenest

AP:
https://github.com/cisarik/ap.git
/home/agile/Projects/ap

Meta:
https://github.com/cisarik/meta.git
/home/agile/meta
```

The preceding logical whole is final:

```text
Logical whole:
framenest-in-process-lifecycle-runtime-contract

Closure:
CLOSED: PASS

Public and production SHA:
148b6c2012809944262399c1a166e85082606fbf

Schema:
0028
```

Do not reopen or allocate work to that closed whole.

Its accepted production evidence includes an immutable deployment, verified catalog backup and restore, healthy schema `0028`, graceful live SIGTERM stop in `0.150 s`, no SIGKILL, successful restart, and invalidation of the broad NUC sudo timestamp.

The ORCHESTRATOR’s clean public inspection found:

* no existing `scripts/` tree in FrameNest;
* no FrameNest occurrence of `mullvad`, `connect_via_ahw`, or an `ahw`-advertised exit-node design;
* current network documentation is about Tailscale Serve/MagicDNS ingress and application identity, not public-internet egress;
* relevant durable sources include ADR-0048, `SERVER.md`, `SPEC.md`, `SECURITY.md`, and the Ubuntu NUC deployment runbook.

Treat these as restoration evidence. Independently verify mutable local and live state.

## 5. Accepted objective and topology

Both devices must eventually:

* remain in the same tailnet;
* communicate directly over Tailscale and MagicDNS;
* independently route ordinary public-internet traffic through the purchased Tailscale Mullvad add-on;
* expose Mullvad egress rather than the ISP public IP to ordinary internet destinations;
* preserve reliable noninteractive SSH from `ahw` to the NUC;
* recover safely from authentication, DNS, exit-node, or connectivity failure;
* use lightweight, discoverable, version-controlled operator scripts and documentation;
* preserve intended state across a normal reboot without storing passwords or auth keys.

Preferred topology, unless primary current evidence disproves it:

```text
ahw ---------------- tailnet / MagicDNS / SSH ---------------- framenest-nuc
 |                                                               |
 +----------------> Mullvad exit node                             |
                                                                 |
                         Mullvad exit node <----------------------+
```

Each device selects a Mullvad exit node independently.

Rejected topology:

```text
framenest-nuc -> ahw advertised exit node -> Mullvad exit node
```

Do not advertise `ahw` as an exit node merely to route the NUC through Mullvad. Do not design exit-node chaining unless explicit current upstream support proves that it is a supported native topology.

The closed upstream feature request `tailscale/tailscale#9520` is evidence that chaining was requested; it is not evidence that chaining is supported.

## 6. Privacy and exposure model

Do not promise anonymity or that either device has “no IP.”

The target privacy statement is:

* ordinary internet services observe Mullvad’s public egress IP instead of Michal’s ISP public IP;
* each device retains private Tailscale addressing;
* LAN addressing may continue to exist locally;
* Tailscale remains identity-aware;
* Tailscale can associate a user/device with Mullvad infrastructure;
* traffic content remains protected by WireGuard;
* no public inbound exposure is introduced;
* Tailscale Funnel, public port forwarding, router forwarding, and public FrameNest exposure remain disabled.

MagicDNS provides tailnet name resolution. It does not hide public egress.

Do not include exact public IP addresses, account email addresses, tailnet names, node keys, auth keys, device secrets, private SSH fingerprints, identity-provider data, or policy secrets in the plan or report.

Use classifications such as:

```text
ISP egress
Mullvad egress
same as baseline
different from baseline
MagicDNS address
Tailscale address
LAN address
unknown
```

## 7. Mandatory reading and repository gate

From `/home/agile/Projects/framenest`, read completely where required and inspect relevant sections before drawing conclusions:

```text
AGENTS.md
.ap/AP.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
docs/WORKER_EXECUTION_CONTRACT.md
README.md
SERVER.md
SPEC.md
SECURITY.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/NUC_HOST_BASELINE.md
docs/adr/0048-tailscale-remote-access-and-identity-foundation.md
deploy/ubuntu/README.md
```

Verify without Git writes:

```bash
pwd -P
git status --short --branch
git remote get-url origin
git rev-parse HEAD
git show -s --format='%H%n%T%n%P%n%s' HEAD
git ls-tree HEAD .ap
git submodule status .ap
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote https://github.com/cisarik/ap.git refs/heads/main
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote https://github.com/cisarik/meta.git refs/heads/main
```

Expected FrameNest topology:

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 148b6c2012809944262399c1a166e85082606fbf
Expected origin: cisarik/framenest
Expected porcelain: clean
Expected AP gitlink and submodule HEAD:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Do not fetch or repair a mismatch. Classify any difference using all five AP recovery classes and return evidence. Preserve owner work. An unexplained material divergence is a stopping condition.

## 8. Repository and Meta investigation

Run the required FrameNest reconnaissance:

```bash
rg -n \
  'tailscale|tailnet|mullvad|exit.node|MagicDNS|framenest-nuc|SSH_AUTH_SOCK|sudo -n' \
  /home/agile/Projects/framenest \
  --glob '!**/.git/**' \
  --glob '!**/.venv/**'

rg --files /home/agile/Projects/framenest \
  | rg '(network|tailscale|tailnet|mullvad|nuc|deploy|recovery)' -i
```

Determine:

* authoritative current scripts and documentation;
* whether relevant material is current, stale, superseded, or unrelated;
* whether any operator tooling is intended for public repository storage;
* which tools currently exist only under operator home directories;
* whether old standalone Mullvad application assumptions survive anywhere relevant;
* whether an old `ahw` exit-node/chained route remains documented;
* the smallest exact documentation and script boundary needed;
* whether the absence of a current `scripts/` tree makes `scripts/operator/network/` appropriate or whether an existing `deploy/ubuntu` convention is better;
* which durable owner should contain the accepted network contract.

Inspect Meta only as supporting historical evidence:

```text
/home/agile/meta/projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/00_handout.md
```

The expected public Meta head is `59e87fa5479844c8c54ed99a93aa06b9ea90a01a`.

Inspect another recent Meta artifact only when a named current question cannot be answered from the active handout, FrameNest repository, live state, or primary upstream documentation. Do not treat Meta as current task authority.

Do not mutate Meta.

## 9. Current official source research

Use current official Tailscale or Mullvad documentation and upstream Tailscale source/issues. Do not rely on cached GitHub branch views, third-party tutorials, forum folklore, or search-result snippets when primary evidence is available.

Minimum sources:

```text
https://tailscale.com/docs/features/exit-nodes/mullvad-exit-nodes
https://tailscale.com/docs/features/exit-nodes
https://tailscale.com/docs/features/exit-nodes/mandatory-exit-nodes
https://tailscale.com/docs/features/exit-nodes/auto-exit-nodes
https://tailscale.com/docs/reference/tailscale-cli
https://github.com/tailscale/tailscale/issues/9520
```

Current Orchestrator findings that you must verify rather than merely repeat:

* every device enables its exit node separately;
* recommended exit-node selection prefers ordinary tailnet exit nodes over Mullvad when ordinary exit nodes are available;
* therefore `auto:any` is not inherently Mullvad-only;
* local LAN access is disabled by default while using an exit node;
* Mullvad documentation warns that enabling LAN access can permit DNS leaks;
* modern supported Tailscale versions no longer require the old Mullvad DNS workaround from versions `1.48.1` and `1.48.2`;
* mandatory exit nodes require system-policy/MDM configuration and can cause service disruption during exit-node failure, captive portals, or authentication;
* `tailscale set --exit-node=<ID-or-name>` changes the selected exit node;
* `tailscale set --exit-node=` disables exit-node use;
* `--operator=<user>` can delegate operation of `tailscaled` on Unix;
* exact persistence and failure behavior must still be verified against the installed versions and live state.

Record source title, owner, last-validated date when exposed, retrieval date, and the exact claim supported. Clearly label inference.

## 10. Safety history and absolute prohibitions

A previous networking attempt caused:

* recursive GUI/Cursor invocation;
* multiple unwanted windows;
* a KDE freeze/crash;
* internet lockout during Mullvad/Tailscale interaction.

Never invoke or mutate:

```text
cursor
code
xdg-open
*.AppImage
recursive shell launchers
GUI automation
browser launch
desktop or KDE restart
NetworkManager
Wi-Fi
router configuration
firewall configuration
iptables or nftables
sysctl forwarding
standalone Mullvad VPN application
tailscale set
tailscale up
tailscale down
tailscale login
tailscale logout
systemctl restart tailscaled
```

Do not advertise an exit node, enable IP forwarding, alter routes, change DNS, assign Mullvad access, modify access controls, edit the tailnet policy, authenticate a device, or change service enablement.

Do not open a browser window automatically.

If an admin-console action or identity-provider login is required, stop at a human gate and describe the shortest manual action for Michal. Never request his password, passphrase, session cookie, auth key, recovery code, or browser profile.

Do not fall back from noninteractive BatchMode SSH to interactive authentication.

## 11. Read-only live-state inventory on `ahw`

Before using a Tailscale command, verify its installed help and supported syntax. Do not assume the online documentation exactly matches the installed version.

Collect and safely classify:

* installed Tailscale version;
* `tailscaled` active and boot-enabled state;
* backend/login state, including `NeedsLogin`;
* local device identity and tailnet membership;
* MagicDNS behavior;
* current selected exit node, if any;
* whether `ahw` advertises itself as an exit node;
* Mullvad exit-node availability;
* DNS acceptance and route preferences;
* `--exit-node-allow-lan-access` state;
* whether the standalone Mullvad daemon/application is installed or active;
* bare `framenest-nuc` resolution;
* full MagicDNS name and resolution;
* whether both names resolve to LAN or Tailscale addresses;
* current route class for ordinary internet traffic;
* current egress classification;
* current LAN, tailnet, and internet reachability;
* usable recovery channel if Tailscale becomes unavailable.

Read-only commands may include supported, bounded forms of:

```bash
command -v tailscale
tailscale version
tailscale help
tailscale status --json
tailscale ip
tailscale get
tailscale exit-node list
tailscale exit-node suggest
systemctl is-enabled tailscaled
systemctl is-active tailscaled
systemctl is-active mullvad-daemon.service
resolvectl status
getent ahosts framenest-nuc
ip route get <safe-public-destination>
```

`tailscale status --json` may contain sensitive identifiers. Inspect it locally, extract only the minimum necessary facts, and sanitize the report. Do not copy the raw JSON into Meta or the terminal report.

Do not inspect browser profiles, credential stores, unrelated home-directory files, or enumerate `~/.ssh`.

## 12. Read-only NUC inspection

Use only the existing FrameNest NUC SSH identity declared by the active handout. Do not inspect or print private-key material. Do not print the key fingerprint in the report.

The required SSH posture is:

```bash
env SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)" \
  ssh -T \
  -o BatchMode=yes \
  -o RequestTTY=no \
  -o StrictHostKeyChecking=yes \
  -o IdentitiesOnly=yes \
  -o ForwardAgent=no \
  -o ClearAllForwardings=yes \
  -o ConnectTimeout=10 \
  -o ServerAliveInterval=15 \
  -o ServerAliveCountMax=2 \
  -i /home/agile/.ssh/id_ed25519_framenest_nuc_cachyos \
  michal@framenest-nuc \
  '<one bounded read-only command>'
```

Before treating the bare hostname as canonical:

1. classify how `framenest-nuc` resolves on `ahw`;
2. obtain the NUC’s full MagicDNS name from current Tailscale evidence;
3. verify that the full name resolves to a Tailscale address;
4. verify strict host-key handling without updating `known_hosts`;
5. separately classify which target actually proves tailnet SSH.

Do not use `StrictHostKeyChecking=accept-new`, modify `known_hosts`, add forwarding, request a TTY, forward the agent, or retry interactively.

Worker 8 invalidated the NUC sudo timestamp with `sudo -K`. Do not assume `sudo -n` works and do not request a refresh during planning.

Collect the NUC equivalents of the `ahw` inventory plus:

* FrameNest service active state through an unprivileged read-only query;
* existing Tailscale Serve and Funnel status when readable without privilege;
* whether the NUC advertises an exit node;
* current direct tailnet reachability from `ahw`;
* current non-Tailscale recovery path, if any;
* whether a later exit-node preference change requires sudo or can use an existing configured Tailscale operator.

Do not read production environment contents, private media, database contents, credentials, auth configuration, or unrelated service logs.

## 13. Bounded external diagnostics

Public diagnostics are allowed only when necessary to classify current egress or DNS behavior.

Requirements:

* use an official Mullvad endpoint or another primary/reputable diagnostic source;
* use command-line HTTP only;
* one request at a time;
* no browser;
* no provider credentials;
* do not contact FrameNest’s OpenAI, X, YouTube, NVIDIA, Vercel, or other content providers;
* do not print or archive the exact public IP;
* reduce raw output locally to `Mullvad egress`, `ISP/non-Mullvad egress`, or `unknown`;
* preserve the first causal error if transport, status, parsing, or classification fails;
* do not repeat calls without a concrete evidence-derived reason.

A diagnostic-method failure leaves the intended fact unknown unless prior valid evidence proves it.

## 14. Required architecture adjudication

The plan must answer explicitly:

1. Why independent Mullvad selection on both devices is preferable to chaining the NUC through `ahw`.
2. Whether the purchased entitlement currently permits both devices to use Mullvad concurrently.
3. Whether account access is already assigned to both devices or requires a Michal admin-console gate.
4. Whether explicit verified Mullvad node selection or suggested selection is safer for this use case.
5. Why `auto:any` is or is not acceptable given that Tailscale can prefer a non-Mullvad exit node.
6. Whether direct LAN access is needed when operator SSH uses a verified MagicDNS target.
7. DNS privacy and leak implications of `--exit-node-allow-lan-access=true`.
8. Whether `--exit-node-allow-lan-access=false` should be the default.
9. Whether ordinary persisted Tailscale preferences survive reboot on both installed clients.
10. Whether custom boot scripts or new systemd units are unnecessary.
11. What happens when the selected Mullvad exit node becomes unavailable.
12. Whether the client fails closed, fails open, automatically switches, or leaves the outcome version-dependent.
13. Why mandatory exit-node policy is or is not suitable after the prior workstation lockout.
14. Which actions require Michal in the Tailscale admin console.
15. Which future commands require sudo and which can use a configured Tailscale operator.
16. Whether configuring `--operator=agile` or `--operator=michal` is desirable, already present, or an unnecessary authority expansion.
17. How each device can be changed separately while preserving a verified recovery channel.
18. Whether the full MagicDNS name should replace the bare hostname as the canonical SSH target.
19. How Tailscale Serve ingress and Mullvad public egress coexist without changing FrameNest’s loopback/Unix-socket trust boundary.
20. Which claims remain unproven until future live mutation and reboot acceptance.

Do not silently reinterpret the privacy goal as a hard fail-closed guarantee. If hard fail-closed behavior requires MDM, mandatory policy, or another control, identify it as a separate material decision with its disruption risk.

## 15. Smallest repository mutation proposal

Plan, but do not create, the smallest coherent public repository surface.

Evaluate a structure similar to:

```text
scripts/operator/network/
  framenest_nuc_worker_gate.fish
  framenest_mullvad_egress.fish
  framenest_mullvad_egress.sh
  README.md
```

This is a proposal, not an accepted path. Reconcile it with the observed fact that FrameNest currently has no `scripts/` directory and already keeps Ubuntu operator tooling under `deploy/ubuntu/`.

Prefer a small number of discoverable scripts with subcommands over many one-purpose files.

Evaluate this interface:

```text
status
enable
disable
verify
recover
```

For every proposed file, specify:

* exact path;
* purpose and consumer;
* shell and operating-system scope;
* public-safe content boundary;
* whether executable mode is required;
* exact tests or static validation;
* documentation owner;
* lifecycle and removal trigger.

The public repository remains the source of truth. If convenient commands under `~/.local/bin/` are useful, plan only a documented copy or symlink installed during a separately authorized implementation. Do not embed secrets or private host values.

Do not create or propose `connect_via_ahw.sh`.

Planned scripts must:

* use `tailscale set`, never blind `tailscale up`;
* detect the installed command and supported flags;
* show sanitized state before mutation;
* stop on `NeedsLogin`;
* stop if Mullvad access is absent;
* select an explicit verified Mullvad node unless a better bounded mechanism is proven;
* avoid `auto:any` when it cannot guarantee Mullvad;
* provide safe `status`, `verify`, `disable`, and `recover`;
* preserve tailnet SSH;
* never change firewall, manual routes, NetworkManager, Wi-Fi, KDE, router, or sysctl state;
* never contain passwords, auth keys, cookies, recovery codes, private keys, or passphrases;
* avoid printing exact public IPs;
* avoid recursive process or GUI invocation;
* fail closed at the script level when prerequisites are missing;
* distinguish “command failed” from “egress is not Mullvad”;
* preserve the first causal error;
* produce concise operator-facing output.

Use professional English for public repository documentation and code comments. Operator-facing output may use Slovak only when it materially improves Michal’s operation.

## 16. Startup and authentication model

Prefer, unless evidence disproves it:

* the existing systemd-managed `tailscaled`;
* persisted Tailscale preferences;
* manual scripts for status, controlled change, verification, disable, and recovery;
* no custom boot service;
* no password or auth key stored in a script;
* no authentication prompt on every normal reboot.

If a device is `NeedsLogin`, the future script must stop and give Michal a short supported human authentication instruction.

If both devices do not currently have Mullvad access, plan the minimal admin-console gate:

```text
General settings
→ Mullvad VPN
→ Configure
→ Add devices
→ select ahw and framenest-nuc
→ Save
```

Do not assume this exact UI remains current; verify it from official documentation and label any account-specific state that only Michal can confirm.

Do not automate or scrape the authenticated admin console.

## 17. Future one-device-at-a-time implementation sequence

Design a future implementation route that evaluates this order:

1. capture sanitized, read-only baseline evidence;
2. prepare exact disable/recovery commands before mutation;
3. verify canonical Tailscale/MagicDNS SSH independently of LAN routing;
4. verify Michal retains local console access to `ahw`;
5. configure only `ahw`;
6. verify `ahw` internet, DNS, Mullvad egress, tailnet reachability, and NUC SSH;
7. test `ahw` persistence separately;
8. return `ahw` to a known accepted state;
9. establish an automatic rollback for the headless NUC;
10. configure only the NUC over verified tailnet SSH;
11. verify NUC Mullvad egress without printing its public IP;
12. verify `ahw` can still reach the NUC over the canonical tailnet name;
13. verify FrameNest health and Tailscale Serve remain unaffected;
14. cancel the automatic rollback only after all required checks pass;
15. test NUC persistence separately;
16. retain explicit `disable` and `recover` paths;
17. never reboot both devices in the same evidence step.

Before any future NUC network mutation, specify a transient automatic rollback that restores the exact previous exit-node preference unless successful verification explicitly cancels it.

The plan must identify:

* rollback scheduler/mechanism;
* exact captured prior preferences;
* timeout rationale;
* cancellation evidence;
* behavior if SSH disconnects;
* behavior if the Worker process dies;
* whether privilege is required;
* cleanup owner and exact cleanup paths;
* how the rollback avoids altering Tailscale Serve or unrelated preferences.

Do not invent firewall rules to recover from an unsupported topology.

## 18. Future acceptance matrix

The final logical whole must eventually prove:

* both devices remain in the intended tailnet;
* both independently use Mullvad exit nodes;
* ordinary internet destinations observe Mullvad rather than ISP egress;
* DNS behavior matches the explicitly selected privacy posture;
* canonical PC-to-NUC SSH works over Tailscale;
* bare versus full hostname behavior is understood;
* FrameNest service and health remain available;
* Tailscale Serve remains tailnet-only;
* Funnel remains disabled;
* normal reboot preserves the intended state on each device;
* scripts safely report status;
* scripts safely disable and recover;
* no standalone Mullvad application competes with Tailscale;
* no chained exit node is used;
* neither device advertises an unintended exit route;
* no public inbound exposure was added;
* no firewall, router, Wi-Fi, KDE, NetworkManager, sysctl, or unrelated service mutation occurred.

For every acceptance row, define:

* target device;
* precondition;
* exact observable;
* positive expectation;
* negative control;
* evidence source;
* sanitization;
* rollback trigger;
* acceptance owner;
* whether fresh independent evidence is required.

Require a fresh independent acceptance Worker after implementation because future host/network mutation is E3 and affects production availability and recovery.

## 19. Human gates and unresolved choices

Identify only genuinely material choices requiring Michal.

At minimum classify whether these are decisions, observations, or recommendations:

* preferred Mullvad country/city versus lowest-latency node;
* whether LAN access is needed for any real local service;
* whether hard fail-closed internet behavior is desired despite lockout risk;
* whether both Mullvad device assignments already exist;
* whether `ahw` has a reliable physical/local recovery console;
* whether the NUC has any recovery path when Tailscale fails, given that it is headless;
* whether configuring a Tailscale operator is acceptable;
* whether canonical SSH should use the full MagicDNS name.

Recommend defaults where evidence permits. Do not ask Michal to choose matters that can be resolved deterministically from current evidence.

## 20. Non-authorizing observations

Retain without implementing:

```text
AP candidate:
cooperator-facing-routing-header-and-meta-destination-projection

FrameNest candidate:
relocatable-immutable-release-build-contract
```

The AP candidate concerns Cooperator-visible role, reasoning, Native Plan Mode, Meta directory, and artifact-name projection.

The FrameNest candidate concerns the observed absolute staging references retained in a Poetry `.venv` after an immutable release-directory rename.

Neither observation authorizes AP or unrelated FrameNest mutation.

Record any genuinely new AP or FrameNest ledger observation separately. Do not invent upgrades and do not reopen the exhausted AP backlog without concrete practical evidence.

## 21. Required planning artifact

Return two consecutive deliverables in one response.

### Deliverable A — planning artifact

Begin exactly with this YAML front matter:

```yaml
---
name: Tailnet Mullvad Egress and Operator Network Recovery
overview: Establish independent Mullvad egress for ahw and framenest-nuc while preserving direct tailnet SSH, reboot persistence, lightweight operator controls, and lockout-safe recovery.
logical_whole: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
phase: planning
worker: 01
maximum_plan_only_cycles: 1
---
```

Then provide these sections:

1. Observed current state
2. Evidence limitations and sanitization
3. Authoritative source findings
4. Chosen topology and rejected alternatives
5. DNS, LAN-access, privacy, and failure semantics
6. Exact repository mutation proposal
7. Exact script interface and behavior
8. PC operational sequence
9. Headless NUC operational sequence
10. Human admin-console and privilege gates
11. Automatic rollback and lockout prevention
12. Test and acceptance matrix
13. Security and privacy limitations
14. Smallest Worker 2 implementation authority
15. Unresolved Cooperator decisions
16. AP empirical observations
17. FrameNest ledger observations

The Worker 2 authority proposal must specify exact paths, exact baseline, implementation stages, privileges, host targets, rollback, tests, Git authority, publication separation, and fresh independent acceptance routing. It remains a proposal and grants no authority.

### Deliverable B — terminal report

After the planning artifact, begin the terminal report exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo these coordinates exactly once in the report metadata:

```text
Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 01
Worker exchange ordinal: 01
```

Include:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
```

Also report:

* start and end FrameNest commit;
* public FrameNest, AP, and Meta ref verification;
* repository cleanliness and AP pin;
* read-only commands performed;
* PC and NUC inspection coverage;
* external diagnostic endpoints contacted or none;
* sanitized observed state;
* unresolved evidence;
* deviations and risks;
* `Resolved Execution Issues / Near-Misses`;
* `Pre-Existing Failure Classification`;
* one smallest next step;
* explicit authority expiry.

A non-zero command, authentication failure, unsupported installed command, missing live evidence, unexpected repository state, or inability to establish safe NUC reachability forbids an unqualified PASS. Classify the causal limitation honestly.

## 22. External trace lifecycle

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

This prompt is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_planning.md
```

The actual terminal outcome is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_report.md
```

Do not write either file. The prompt and actual report may be archived together only after the report exists and only by a separately authorized archival owner.

## 23. Stop conditions

Stop and report `PARTIAL` or `BLOCKED` when appropriate if:

* the prompt did not reach a genuinely fresh Worker session;
* Native Plan Mode is not active;
* repository identity, baseline, cleanliness, or AP pin is contradictory;
* public refs cannot be verified;
* live inspection would require mutation;
* SSH requires interactive authentication;
* strict host-key verification fails;
* required current state needs sudo during planning;
* a command would expose secrets or prohibited identifiers;
* an admin-console action is required;
* either device is `NeedsLogin`;
* Mullvad entitlement cannot be classified safely;
* the selected topology depends on unsupported exit-node chaining;
* exact rollback cannot be designed for the headless NUC;
* a material conclusion would rely only on stale Meta history or third-party documentation;
* implementation would be needed to answer the planning question;
* the planning artifact and terminal report are complete.

At the terminal report, all Worker 1 authority expires.
