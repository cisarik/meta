# Fresh Orchestrator Handout — FrameNest Tailnet Mullvad Egress and Operator Network Recovery Contract

## Cooperator-facing routing projection

```text
🎛 PROMPT PRE FRESH ORCHESTRATOR
EXTRA HIGH REASONING 🧠🧠🧠

Native Plan Mode for this Orchestrator handout: not-used

Meta archive directory:
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/

Current artifact:
00_handout.md

Next expected artifacts:
01_planning.md
01_report.md
```

Communicate with Michal in Slovak. Address him in masculine grammatical gender. Refer to yourself in feminine grammatical gender. Worker prompts and reports remain professional English.

## Active logical whole

```text
framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
```

This is a new logical whole. Worker numbering resets to Worker 1.

## Previous logical whole closure

The preceding logical whole is final and must not be reopened without concrete regression evidence:

```text
Logical whole:
framenest-in-process-lifecycle-runtime-contract

Closure:
CLOSED: PASS

Public and production SHA:
148b6c2012809944262399c1a166e85082606fbf

Tree:
1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366

AP pin:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Schema:
0028

Production evidence:
verified pre-deployment snapshot;
off-device pull;
disposable restore;
immutable deployment;
health PASS;
database integrity PASS;
live SIGTERM stop 0.150 seconds;
no SIGKILL;
restart PASS;
cached sudo invalidated.
```

Do not allocate another Worker to this closed lifecycle whole.

## Repository identities

```text
FrameNest:
https://github.com/cisarik/framenest
/home/agile/Projects/framenest

AP:
https://github.com/cisarik/ap
/home/agile/Projects/ap

Meta:
https://github.com/cisarik/meta
/home/agile/meta
```

Meta is supporting historical evidence only. It cannot override live state, public Git objects, repository source, or current official Tailscale documentation.

Use direct Git transport such as `git ls-remote`; do not rely on cached GitHub web views.

## Cooperator objective

Michal wants a stable, understandable, lockout-resistant network operating contract for:

```text
ahw:
CachyOS development PC
local user agile

framenest-nuc:
Ubuntu 24.04.4 LTS
headless Intel NUC
operator user michal
production FrameNest server
```

Both devices must:

* remain members of the same tailnet;
* communicate directly through Tailscale/MagicDNS;
* independently route ordinary public internet traffic through the purchased Tailscale Mullvad add-on;
* expose Mullvad egress rather than the ISP public IP to ordinary internet destinations;
* retain reliable noninteractive SSH from `ahw` to the NUC;
* recover safely from authentication, DNS, exit-node, or connectivity failure;
* retain lightweight, discoverable, version-controlled scripts and documentation;
* persist the intended configuration across normal reboot without storing passwords or auth keys in scripts.

## Provisional architecture decision

Treat this as the preferred architecture unless current primary evidence disproves it:

```text
ahw ---------------- tailnet / MagicDNS / SSH ---------------- framenest-nuc
 |                                                               |
 +----------------> Mullvad exit node                             |
                                                                 |
                         Mullvad exit node <----------------------+
```

Each device selects a Mullvad exit node independently.

Do not design:

```text
framenest-nuc -> ahw advertised exit node -> Mullvad exit node
```

Tailscale’s current documentation requires each device to enable an exit node separately. Native exit-node chaining must be treated as unsupported unless the Planner finds explicit current official support proving otherwise.

Do not advertise `ahw` as an exit node merely to route the NUC through Mullvad.

Canonical current sources include:

```text
https://tailscale.com/docs/features/exit-nodes/mullvad-exit-nodes
https://tailscale.com/docs/features/exit-nodes
https://tailscale.com/docs/features/exit-nodes/mandatory-exit-nodes
https://tailscale.com/docs/features/exit-nodes/auto-exit-nodes
https://tailscale.com/docs/reference/tailscale-cli
https://github.com/tailscale/tailscale/issues/9520
```

Technical internet research must prefer current official Tailscale or Mullvad documentation and upstream Tailscale source/issues.

## Privacy model that must remain explicit

Do not promise anonymity or that a device has “no IP.”

The target is:

* internet services observe Mullvad’s public egress IP rather than Michal’s ISP public IP;
* tailnet devices retain private Tailscale addresses;
* LAN addresses may continue to exist locally;
* Tailscale remains identity-aware;
* Tailscale can associate a user/device with Mullvad infrastructure;
* traffic content remains protected by WireGuard;
* no public inbound exposure is introduced;
* Tailscale Funnel, router forwarding, and public port forwarding remain disabled unless separately authorized.

MagicDNS supplies tailnet name resolution. It does not mask public egress.

## Safety history

A previous networking attempt caused a real workstation incident:

* recursive GUI/Cursor invocation;
* multiple windows;
* KDE freeze/crash;
* internet lockout during Mullvad/Tailscale interaction.

Therefore prohibit Workers from invoking:

```text
cursor
code
xdg-open
*.AppImage
recursive shell launchers
GUI automation
desktop restart
KDE mutation
NetworkManager mutation
Wi-Fi mutation
router mutation
firewall mutation
manual iptables/nftables routing
sysctl forwarding
standalone Mullvad VPN application
tailscale down
blind tailscale up
```

No Worker may open browser windows automatically.

If a Tailscale admin-console action or identity-provider login is necessary, stop at a human gate and give Michal exact short manual steps. Never request his password, passphrase, session cookie, auth key, or recovery code.

## Known SSH operator gate

The NUC key is:

```text
/home/agile/.ssh/id_ed25519_framenest_nuc_cachyos

public fingerprint:
SHA256:FuBY7/UNF4tdQfDkkcQpaJXfsxGZm7RtSk2S1VLRwwQ
```

The gpg-agent socket is:

```bash
gpgconf --list-dirs agent-ssh-socket
```

Required Worker SSH profile:

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
  '<bounded command>'
```

Worker 8 invalidated the broad NUC sudo timestamp using `sudo -K`. Read-only planning must not assume `sudo -n` remains available. If later implementation needs privileged NUC changes, the Cooperator may explicitly refresh the bounded operational gate with `global_sudo.sh`.

Never fall back from BatchMode to interactive authentication.

## First Orchestrator responsibility

Do not mutate FrameNest, either host, or the tailnet.

First:

1. verify current public FrameNest and AP refs;
2. inspect current FrameNest networking documentation and scripts;
3. inspect only relevant recent Meta commits if they prevent repeated work;
4. separate accepted current state from stale network experiments;
5. generate a fresh Worker 1 read-only planning prompt.

Do not perform networking implementation directly from this handout.

## Mandatory Worker 1 routing header

Present the next prompt to Michal with exactly this visual routing information outside the Worker prompt:

```text
🆕 💡 PROMPT PRE FRESH WORKERA S PLAN MODE
EXTRA HIGH REASONING 🧠🧠🧠
```

Then explicitly tell Michal in Slovak:

```text
Najprv zapni Native Plan Mode, až potom vlož prompt.
```

Archive the Worker 1 prompt as:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_planning.md
```

Archive its report as:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/01_report.md
```

## Worker 1 planning envelope

The generated prompt must include:

```text
Logical whole identity:
framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract

Worker session ordinal:
01

Worker exchange ordinal:
01

Worker role:
read-only network architecture and implementation planner

Native planning mode:
required

Maximum plan-only cycles:
1

Fresh-worker session:
required

Reasoning profile requested by Cooperator:
Extra High

Mutation authority:
none

NUC mutation authority:
none

PC mutation authority:
none

Tailnet/admin-console mutation authority:
none

Provider-call authority:
only bounded public egress/DNS diagnostics if explicitly necessary

Evidence posture:
independent
```

## Worker 1 required investigation

The Planner must inspect the repository before proposing new files:

```bash
rg -n \
  'tailscale|tailnet|mullvad|exit.node|MagicDNS|framenest-nuc|SSH_AUTH_SOCK|sudo -n' \
  /home/agile/Projects/framenest \
  --glob '!**/.git/**' \
  --glob '!**/.venv/**'

rg --files /home/agile/Projects/framenest \
  | rg '(network|tailscale|tailnet|mullvad|nuc|deploy|recovery)' -i
```

It must identify:

* authoritative current scripts and documentation;
* stale or contradictory material;
* scripts intended for public repository storage;
* scripts currently expected only under the operator’s home directory;
* whether older Mullvad-app assumptions remain;
* whether an earlier `ahw` exit-node design remains documented;
* exact smallest cleanup and implementation boundary.

## Read-only live-state inventory

Worker 1 may perform safe read-only inspection of `ahw` and the NUC.

It must determine, without exposing secrets:

* installed Tailscale version on both devices;
* `tailscaled` service state and boot enablement;
* logged-in/NeedsLogin/backend state;
* tailnet and device identities;
* current MagicDNS behavior;
* whether both devices are in the same tailnet;
* whether Mullvad access is assigned to both devices;
* currently selected exit node, if any;
* whether either device advertises itself as an exit node;
* current DNS acceptance and route preferences;
* `--exit-node-allow-lan-access` state;
* whether bare `framenest-nuc` resolves to a LAN or Tailscale address;
* whether the full MagicDNS name should become the canonical SSH target;
* current ISP egress versus Mullvad egress classification;
* current LAN, tailnet, and internet reachability;
* current recovery path when Tailscale is unavailable.

Do not include exact public IPs, account email addresses, node keys, auth keys, device secrets, or tailnet policy secrets in the report. Use classifications such as:

```text
ISP egress
Mullvad egress
same as baseline
different from baseline
MagicDNS address
LAN address
```

Read-only commands may include carefully bounded forms of:

```text
tailscale version
tailscale status --json
tailscale ip
tailscale get
tailscale exit-node list
tailscale exit-node suggest
systemctl is-enabled tailscaled
systemctl is-active tailscaled
resolvectl status
getent ahosts <hostname>
ip route get <safe target>
```

The Planner must verify exact supported commands from the installed version before using them.

It must not run:

```text
tailscale set
tailscale up
tailscale down
tailscale login
tailscale logout
systemctl restart tailscaled
```

during planning.

## Required architecture adjudication

The plan must answer explicitly:

1. Why direct Mullvad selection on both devices is preferable to chaining through `ahw`.
2. Whether both devices can use the paid Mullvad entitlement concurrently.
3. Whether explicit Mullvad node selection or suggested selection is safer.
4. Whether `auto:any` could select a non-Mullvad exit node.
5. Whether LAN access is actually needed when SSH uses MagicDNS.
6. DNS-leak implications of `--exit-node-allow-lan-access=true`.
7. Whether the ordinary persisted Tailscale preference survives reboot.
8. Whether custom boot scripts or systemd units are unnecessary.
9. What failure mode occurs if the chosen Mullvad exit node is unavailable.
10. Why mandatory exit-node policy is or is not suitable after the earlier lockout.
11. Which actions require Michal in the admin console.
12. Which actions require sudo and which can use a configured Tailscale operator.
13. How the PC and headless NUC can be changed one at a time while retaining a recovery channel.

Do not silently turn the privacy goal into a hard fail-closed guarantee. If hard fail-closed behavior requires MDM or additional policy, identify it as a separate decision and risk boundary.

## Lightweight script objective

Prefer a small number of discoverable scripts with subcommands over many one-purpose scripts.

The Planner should evaluate a structure similar to:

```text
scripts/operator/network/
  framenest_nuc_worker_gate.fish
  framenest_mullvad_egress.fish
  framenest_mullvad_egress.sh
  README.md
```

Possible subcommands:

```text
status
enable
disable
verify
recover
```

The exact paths and names must follow existing repository conventions found during inspection.

The repository must remain the public source of truth. If Michal wants convenient home-directory commands, plan a documented copy or symlink into:

```text
~/.local/bin/
```

No secret may be embedded in a repository script or home wrapper.

Scripts must:

* use `tailscale set`, not blind `tailscale up`;
* validate installed commands and versions;
* record or display safe current state before mutation;
* select an explicit verified Mullvad node unless a better bounded mechanism is proven;
* fail closed at the script level when prerequisites are absent;
* include `status`, `verify`, and recovery operations;
* never alter firewall, routes, NetworkManager, Wi-Fi, or KDE;
* avoid GUI or recursive process invocation;
* never contain passwords, auth keys, cookies, or passphrases;
* give concise, comprehensible operator output;
* preserve tailnet SSH;
* avoid printing exact public IPs in archived reports.

Use minimal comments. Follow repository language conventions for public code and documentation; operator-facing messages may be Slovak when that materially helps Michal.

Do not create `connect_via_ahw.sh`. That name encodes the rejected chained-exit topology.

## Startup and authentication model

The plan should prefer:

* `tailscaled` managed by the existing systemd service;
* persisted Tailscale preferences;
* manual scripts for status, controlled changes, verification, and recovery;
* no new boot service unless live evidence proves one is required.

No password should be stored or entered on every boot.

If either device is `NeedsLogin`, the script must stop and provide a human authentication instruction. Authentication must happen through Tailscale’s supported identity flow, not through credentials in a script.

If the Tailscale admin console has not granted Mullvad access to both `ahw` and `framenest-nuc`, the workflow must pause and give Michal the minimal manual console steps. Do not automate or scrape the authenticated console.

## Future implementation safety plan

Worker 1 must design implementation and live acceptance so that later Workers change only one device at a time.

Required sequence to evaluate:

1. preserve read-only baseline evidence;
2. create exact recovery commands before mutation;
3. validate canonical tailnet SSH independently of LAN routing;
4. configure and verify `ahw` locally while Michal retains local console access;
5. verify internet, DNS, tailnet, and NUC SSH;
6. configure the NUC through tailnet SSH with a bounded automatic rollback mechanism;
7. verify NUC Mullvad egress without exposing its exact public IP;
8. verify NUC remains reachable over tailnet;
9. verify FrameNest service and health are unaffected;
10. test persistence one device at a time;
11. retain an explicit `disable`/`recover` path;
12. avoid rebooting both devices in the same evidence step.

Before any headless NUC network mutation, the future implementation plan must define a transient rollback that automatically restores the previous exit-node preference unless explicitly cancelled after successful verification.

Do not invent manual firewall rules to recover from an unsupported topology.

## Live acceptance requirements

The final logical whole must eventually prove:

* both devices are in the intended tailnet;
* both independently use a Mullvad exit node;
* internet destinations do not see the ISP egress during the accepted state;
* DNS behavior matches the selected privacy posture;
* PC-to-NUC SSH works through the canonical tailnet name;
* FrameNest health remains available;
* ordinary reboot preserves the intended state;
* scripts can display status and safely disable/recover;
* no standalone Mullvad app is competing with Tailscale;
* no chained exit node is used;
* no device advertises an unintended exit route;
* no public inbound exposure was added;
* no firewall, router, Wi-Fi, KDE, or unrelated service mutation occurred.

External checks must be bounded to official or reputable egress/DNS verification endpoints. Do not invoke FrameNest’s X, YouTube, OpenAI, or other content providers for network acceptance.

## Planner artifact format

Worker 1’s planning artifact must begin with concise YAML front matter rather than a decorative “REPORT FOR ORCHESTRATOR” preamble:

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

The body must then provide:

1. observed current state;
2. authoritative source findings;
3. chosen topology and rejected alternatives;
4. exact repository mutation proposal;
5. exact script interface;
6. PC and NUC operational sequencing;
7. human admin-console gates;
8. rollback and lockout prevention;
9. test and acceptance matrix;
10. security/privacy limitations;
11. smallest Worker 2 implementation authority;
12. unresolved decisions requiring Cooperator input;
13. AP empirical observations;
14. FrameNest ledger observations.

Planning must not mutate anything.

## Orchestrator routing after Worker 1

After receiving Worker 1’s report:

* independently classify its observed state and chosen topology;
* ask Michal only for a genuinely material missing choice;
* do not begin another planning cycle unless the single allowed plan requires correction;
* generate a fresh Worker 2 implementation prompt with an exact allowlist;
* separate repository implementation from live PC/NUC mutation if that improves recoverability;
* require independent acceptance before declaring the logical whole closed.

Use the agreed visual routing headers on every handoff.

## Non-authorizing ledgers

Retain without implementing during this networking whole:

```text
AP candidate:
cooperator-facing-routing-header-and-meta-destination-projection

FrameNest candidate:
relocatable-immutable-release-build-contract
```

The AP candidate should eventually formalize Cooperator-visible role, reasoning, Native Plan Mode, Meta directory, and artifact-name projection.

The FrameNest candidate comes from the production observation that a Poetry `.venv` created under a staging directory retained 32 absolute staging references after the release directory was renamed.

Neither candidate authorizes AP or unrelated FrameNest mutation in this logical whole.

## Stop condition

This handout ends after producing the expert Worker 1 planning prompt.

Do not:

* mutate either host;
* modify the tailnet;
* change Mullvad access;
* alter FrameNest source;
* deploy;
* reopen the closed lifecycle whole;
* begin Worker 1’s work yourself.
