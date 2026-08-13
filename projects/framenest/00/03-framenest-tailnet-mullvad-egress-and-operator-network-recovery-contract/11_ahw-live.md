# Authoritative Prompt for Fresh Worker 11

## Enable and Verify Mullvad Egress on `ahw`

Persistent role identity: one fresh Worker instance assigned to the WORKER role
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Live Network Operator
Phase: Implementation
Implementation authority: explicit for one `ahw` exit-node mutation
Repository mutation authority: none
Publication authority: none
NUC mutation authority: none
Account and admin-console authority: none
Evidence posture: live operational evidence
Worker topology: single-active
Internal delegation posture: not-used
Reasoning recommendation: High

This task must produce the first real Mullvad egress result of this logical whole.

Do not perform another repository audit. Do not inspect or mutate Meta. Do not change the NUC.

Read this complete prompt before acting.

## 1. Current accepted state

Public FrameNest `main` is:

```text
4add009e1f89fcc05b9e8bc306d6ecc8e568547b
```

Tree:

```text
4c4d09e3d6ed9204c9f26905290cc31397e97d02
```

Parent:

```text
20369a197daedac25569fef077400a9754cd1d5f
```

AP pin:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

The published scripts passed independent acceptance.

Accepted live starting state on `ahw`:

```text
backend: Running
client-get: unsupported
exit-node: none
LAN access: unavailable without readable get
Mullvad nodes: available
self advertises exit node: no
standalone Mullvad tunnel: disconnected
valid Mullvad suggestion: available
```

Accepted live state on the NUC:

```text
backend: Running
exit-node: none
LAN access: false
Mullvad nodes: available
self advertises exit node: no
standalone Mullvad tunnel: absent
```

The COOPERATOR has run successfully on `ahw`:

```text
sudo tailscale set --operator=agile
```

The command returned without an error or output. Treat this as Cooperator-authorized operator configuration, but verify the resulting operator state read-only before enabling.

## 2. Exact objective

On `ahw` only:

1. verify the safe starting posture;
2. privately obtain one explicit suggested Mullvad exit-node DNS name;
3. validate that it is an actually available node ending exactly in `.mullvad.ts.net`;
4. enable that exact node using the published Fish wrapper;
5. keep LAN access false;
6. verify Mullvad public egress through the published diagnostic;
7. verify tailnet SSH to the NUC remains functional;
8. verify FrameNest service and Serve/Funnel baseline remain healthy;
9. leave the Mullvad exit node enabled only if every required gate passes;
10. otherwise immediately run the published `recover`.

Do not mutate the NUC.

## 3. Repository identity

Exact published worktree:

```text
/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2
```

Expected branch:

```text
feat/tailnet-mullvad-egress-recovery-contract
```

Expected HEAD and public `main`:

```text
4add009e1f89fcc05b9e8bc306d6ecc8e568547b
```

Expected tree:

```text
4c4d09e3d6ed9204c9f26905290cc31397e97d02
```

Expected AP gitlink:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

The unrelated owner checkout is:

```text
/home/agile/Projects/framenest
```

Do not inspect or mutate it.

## 4. Mandatory reading

From the exact published worktree, read:

```text
AGENTS.md
.ap/AP.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
docs/WORKER_EXECUTION_CONTRACT.md
docs/OPERATOR_NETWORK.md
scripts/operator/network/README.md
scripts/operator/network/framenest_mullvad_egress.sh
scripts/operator/network/framenest_mullvad_egress.fish
scripts/operator/network/framenest_nuc_worker_gate.fish
```

Read only the `Known SSH operator gate` section of:

```text
/home/agile/meta/projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/00_handout.md
```

Use its established NUC target, login, and identity only for post-enable read-only SSH verification.

Do not expose those private parameters.

## 5. Initial immutable repository gate

Run:

```bash
pwd -P
git status --short --branch
git status --porcelain=v1 --untracked-files=all
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD^
git submodule status .ap
git -C .ap rev-parse HEAD
git diff --exit-code
git diff --cached --exit-code
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote origin refs/heads/main
```

Require:

```text
root = exact published worktree
origin = cisarik/framenest
branch = feat/tailnet-mullvad-egress-recovery-contract
HEAD = public main = 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
tree = 4c4d09e3d6ed9204c9f26905290cc31397e97d02
parent = 20369a197daedac25569fef077400a9754cd1d5f
.ap HEAD and gitlink = 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
worktree and index = clean
untracked files = none
```

Run syntax checks:

```bash
bash -n scripts/operator/network/framenest_mullvad_egress.sh
fish -n scripts/operator/network/framenest_mullvad_egress.fish
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish
```

A mismatch stops all live work. Do not repair or fetch into the worktree.

Do not run pytest.

## 6. Private evidence root

Before inspecting live state:

```bash
umask 077
live_root="$(mktemp -d -p /tmp framenest-w11-ahw-live.XXXXXX)"
```

Require:

```text
/tmp/framenest-w11-ahw-live.*
```

Keep raw status, preference, suggestion, diagnostic, SSH, Serve, and Funnel output only below this root.

Do not create a pointer file outside it.

Do not print or report:

* public IP addresses;
* exact Mullvad hostnames or locations;
* tailnet names or suffixes;
* node lists;
* account identity;
* SSH login, identity path, fingerprint, or host key;
* raw JSON;
* raw diagnostic response.

## 7. Environment posture

Unset for every live command:

```text
APPIMAGE
APPDIR
ARGV0
LD_LIBRARY_PATH
LD_PRELOAD
```

Use trusted system executables and the exact published scripts.

Do not invoke Cursor, another AppImage, a GUI, browser, or desktop integration.

## 8. Read-only operator and starting-state gate

Capture privately and parse:

```text
/usr/bin/tailscale debug prefs
```

Require:

```text
operator configured = yes
operator matches current local login = yes
```

Do not report the operator name.

Run the exact published wrapper:

```text
scripts/operator/network/framenest_mullvad_egress.fish status
```

Require:

```text
backend = Running
exit node = none
Mullvad nodes = available
self advertises exit node = no
standalone Mullvad tunnel = disconnected or absent
```

`connected`, `ambiguous`, `NeedsLogin`, an already selected exit node, missing Mullvad availability, self-advertisement, or missing operator rights stops before mutation.

Do not repair any failed precondition.

## 9. Private explicit-node selection

Run read-only:

```text
/usr/bin/tailscale exit-node suggest
```

Capture its complete output privately.

Extract exactly one normalized hostname.

Require that it:

* ends exactly in `.mullvad.ts.net`;
* contains no whitespace;
* is not option-like;
* is not `auto:any`;
* is present as an available Mullvad exit-node option in privately captured `tailscale status --json`;
* is not printed in the report.

If no unique valid Mullvad suggestion can be established, stop before mutation.

Do not choose a city or node manually and do not use a non-Mullvad tailnet exit node.

## 10. Exact authorized mutation

Exactly one enable attempt is authorized through:

```text
scripts/operator/network/framenest_mullvad_egress.fish enable --node <privately-validated-node>
```

The wrapper must cause only:

```text
tailscale set --exit-node=<explicit-mullvad-node> --exit-node-allow-lan-access=false
```

Do not print the exact node.

Do not run:

```text
tailscale up
tailscale down
tailscale login
tailscale logout
sudo
```

No second enable attempt is authorized.

## 11. Immediate post-enable gates

Immediately after successful enablement, capture and sanitize:

```text
scripts/operator/network/framenest_mullvad_egress.fish status
/usr/bin/tailscale debug prefs
```

Require:

```text
backend = Running
selected exit-node class = Mullvad
selected node = the privately validated explicit node
LAN access = false
Mullvad nodes = available
self advertises exit node = no
standalone Mullvad tunnel = disconnected or absent
```

Because the `ahw` client cannot read the required `tailscale get` preferences, use private `debug prefs` evidence to establish that LAN access remains false.

Do not report the selected hostname or raw preferences.

If any required post-enable state is not proven, immediately execute recovery under section 14.

## 12. Mullvad egress verification

Run exactly once:

```text
scripts/operator/network/framenest_mullvad_egress.fish verify
```

This authorizes one HTTPS request only to:

```text
https://am.i.mullvad.net/json
```

Require:

```text
Mullvad egress
```

Do not perform another public IP diagnostic and do not report an IP address.

A transport failure, parse failure, HTTP failure, `non-Mullvad egress`, or unknown result triggers immediate recovery.

## 13. Tailnet and FrameNest preservation gates

After Mullvad egress is proven, use only the published strict SSH gate and established handout parameters.

Run a bounded NUC command:

```text
/usr/bin/true
```

Require strict SSH success over MagicDNS.

Then collect read-only NUC facts through separate bounded commands:

```text
/usr/bin/systemctl is-active framenest.service
/usr/bin/tailscale serve status --json
/usr/bin/tailscale funnel status
```

Report only:

```text
strict MagicDNS SSH = PASS
framenest.service = active
Serve handlers = exactly-one
Serve target = protected-unix-socket
Funnel = unconfigured
public inbound exposure = none-proven
```

Do not report the hostname, tailnet suffix, socket details, addresses, or raw output.

Any failure in strict SSH, service state, Serve baseline, Funnel baseline, or private-output containment triggers immediate recovery.

Do not execute any NUC mutation.

## 14. Mandatory recovery boundary

If enablement succeeded but any later required gate fails, immediately run exactly once:

```text
scripts/operator/network/framenest_mullvad_egress.fish recover
```

Then run:

```text
scripts/operator/network/framenest_mullvad_egress.fish status
```

Require the selected exit node to be cleared.

Preserve and report the first causal failure. A later recovery or status failure must not replace it.

If the Worker loses connectivity and cannot continue, the COOPERATOR has a separate local terminal prepared to run the same published `recover` command.

Do not retry enablement after recovery.

## 15. Successful terminal state

Leave the Mullvad exit node enabled only if all of these pass:

* operator state is configured;
* safe starting status passes;
* one explicit Mullvad node is privately validated;
* one enable attempt succeeds;
* post-enable state proves a Mullvad exit node;
* LAN access is false;
* published `verify` reports `Mullvad egress`;
* strict MagicDNS SSH to the NUC succeeds;
* FrameNest service remains active;
* Serve remains exactly one protected Unix-socket handler;
* Funnel remains unconfigured;
* repository state remains immutable;
* private evidence is removed.

Do not run `disable` or `recover` after a successful result.

## 16. Allowed live effects

Authorized live effects are limited to:

* read-only local Tailscale state and suggestion inspection;
* the Cooperator-configured operator readback;
* exactly one `ahw` exit-node enable attempt;
* LAN-access false as part of that enablement;
* exactly one Mullvad diagnostic request through the published verifier;
* read-only strict SSH and NUC service/Serve/Funnel checks;
* immediate `recover` only after a failed post-enable gate;
* private temporary evidence;
* exact cleanup.

## 17. Forbidden actions

Do not:

* mutate the NUC;
* configure another operator;
* invoke sudo;
* change DNS, `accept-dns`, routes other than the selected exit node, firewall, Wi-Fi, NetworkManager, forwarding, or sysctl;
* change Serve or Funnel;
* use `auto:any`;
* enable LAN access;
* activate standalone Mullvad;
* contact another diagnostic endpoint;
* print a public IP;
* restart Tailscale, FrameNest, systemd services, or either host;
* reboot either device;
* open the admin console or any browser;
* inspect credentials or private-key contents;
* modify or publish repository content;
* mutate AP or Meta;
* deploy FrameNest;
* claim NUC egress or logical-whole closure.

## 18. Cleanup

Validate:

```bash
case "$live_root" in
  /tmp/framenest-w11-ahw-live.*)
    ;;
  *)
    printf '%s\n' 'Unsafe live cleanup target' >&2
    exit 90
    ;;
esac
```

Remove only:

```bash
rm -rf -- "$live_root"
```

Verify:

```bash
test ! -e "$live_root"
```

Cleanup failure must not overwrite the first live result.

## 19. Final repository gate

Repeat:

```bash
git status --porcelain=v1 --untracked-files=all
git diff --exit-code
git diff --cached --exit-code
git rev-parse HEAD
git rev-parse HEAD^{tree}
git -C .ap rev-parse HEAD
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote origin refs/heads/main
```

Require:

```text
local HEAD = public main = 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
tree = 4c4d09e3d6ed9204c9f26905290cc31397e97d02
.ap = 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
worktree and index = clean
untracked files = none
```

## 20. Verdict rules

Report `PASS` only when the successful terminal state in section 15 is fully proven and the Mullvad exit node remains enabled.

For `PASS`, use:

```text
Phase-qualified result: implementation-PASS
Result artifact or commit: 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
Report justification: new-mutation
Live ahw egress: Mullvad
Recovery executed: no
```

Report `PARTIAL` when useful evidence exists but enablement was recovered after a failed post-enable gate.

Report `BLOCKED` when a pre-mutation identity, operator, starting-state, explicit-node, private-evidence, or authority gate fails.

A failed mutation must not be retried.

## 21. Terminal report contract

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Immediately echo exactly once:

```text
Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 11
Worker exchange ordinal: 01
```

Include:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: 4add009e1f89fcc05b9e8bc306d6ecc8e568547b | not-applicable
Result evidence: <sanitized live evidence or not-applicable>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk | changed-external-state
Authority expiry: all Worker 11 authority expired at this terminal report
```

Also report:

* fresh-session and Native Plan Mode confirmation;
* repository and public identity;
* operator configured/not-configured without naming it;
* sanitized starting-state matrix;
* valid explicit Mullvad suggestion available or unavailable, without its hostname or location;
* number and class of enable attempts;
* sanitized post-enable matrix;
* LAN-access evidence;
* exact diagnostic command class and `Mullvad egress` result;
* strict MagicDNS SSH result;
* FrameNest service, Serve, Funnel, and public-inbound classifications;
* whether the exit node remains enabled;
* whether recovery ran and its result;
* private temporary root class and cleanup;
* final immutable repository state;
* whether sudo, NUC mutation, DNS/firewall/Serve/Funnel changes, restart, reboot, deployment, AP, or Meta mutation occurred;
* deviations, missing evidence, limitations, and residual risks;
* `Resolved Execution Issues / Near-Misses`;
* `Pre-Existing Failure Classification: none`;
* one smallest next step.

For `PASS`, the smallest next step is a separately authorized NUC-only live implementation with the exact ten-minute transient rollback armed before mutation.

That statement grants no NUC, sudo, timer, account, reboot, deployment, or closure authority.

Do not report exact IP addresses, hostnames, tailnet suffixes, Mullvad nodes, account identities, or key information.

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

This exact prompt is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/11_ahw-live.md
```

The actual terminal report is intended for:

```text
projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/11_report.md
```

Do not write either Meta file.

## 23. Stop conditions

Stop and report honestly if:

* this is not a fresh Worker session;
* Native Plan Mode is active;
* repository, public commit, AP pin, cleanliness, or script identity differs;
* operator configuration is not proven;
* the safe starting state differs;
* no unique explicit Mullvad suggestion can be privately validated;
* a private value cannot be contained;
* mutation would require sudo or another authority class;
* enablement fails;
* a required post-enable gate fails and recovery completes;
* recovery fails;
* repository, NUC, AP, or Meta mutation would be required;
* the successful live state and cleanup are complete.

At the terminal report, all Worker 11 authority expires.
