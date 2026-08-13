### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 09
Worker exchange ordinal: 01

Standard terminal status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
Result evidence: independent identity/allowlist/diff review; syntax-zero; synthetically isolated red-to-green of `test_unreadable_tailscale_get_prefs_fall_back_to_status_json`; candidate suite 77 passed; candidate-source provenance under the exact worktree `src/`; live `ahw` Fish `status` completed with the original unreadable-preference shape; bounded NUC stdin `status` completed with Mullvad nodes unavailable
Logical-whole closure: not-closed
Report justification: final-acceptance
Authority expiry: all Worker 9 authority expired at this terminal report

Acceptance candidate: 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
Acceptance owner map: evaluated against section 8
Acceptance allowlist: evaluated against section 7
Acceptance risk claims: CA-01 through CA-09
Acceptance control matrix: positive and negative controls from section 10
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none

## Independence and routing

Fresh-session confirmation: this conversation opened on this prompt; Native Plan Mode was requested `not-used` and was not observed as active.
Independence confirmation: this session did not implement candidate `4add009e…`, did not perform Worker 7 live preflight, and did not audit or mutate that candidate before this exchange.
Worker session target: `fresh-worker-session`. Worker session profile: Fresh Independent Auditor.

## Capability snapshot

| Row | Requested | Observed | Evidence class |
|---|---|---|---|
| Client/surface | Cursor Worker | Cursor Agent | directly observed |
| Model | Cursor Grok 4.6 | Cursor Grok 4.6 as announced identity | requested; not independently attested |
| Reasoning | High | unknown/not observably exposed | unknown |
| Native planning | not-used | not active | directly observed |
| Filesystem | candidate worktree read-only; private `/tmp/framenest-w9-acceptance.*` | those scopes used | directly observed |
| Git writes | none | none performed | directly observed |
| Public-ref | `git ls-remote origin refs/heads/main` | `20369a197daedac25569fef077400a9754cd1d5f` | directly observed |
| Live status | exact candidate `status` on `ahw` and NUC stdin | both completed | directly observed |

Capability does not grant authority.

Material unknowns: Tailscale client version strings were not collected; NUC admin-console assignment remains outside this audit.

## Candidate identity

Exact existing worktree: `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2`
Remote: `https://github.com/cisarik/framenest.git`
Branch: `feat/tailnet-mullvad-egress-recovery-contract`
HEAD: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
HEAD tree: `4c4d09e3d6ed9204c9f26905290cc31397e97d02`
HEAD parent: `20369a197daedac25569fef077400a9754cd1d5f`
HEAD subject: `fix: fall back from unreadable Tailscale prefs`
HEAD grandparent: `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3`
HEAD great-grandparent: `148b6c2012809944262399c1a166e85082606fbf`
Public `main`: `20369a197daedac25569fef077400a9754cd1d5f`
`.ap` HEAD and gitlink: `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`
Worktree and index before and after: clean
Untracked files before and after: none
Private audit root after cleanup: absent

Commit count above public parent: 1
Changed paths:

```text
M docs/OPERATOR_NETWORK.md
M scripts/operator/network/framenest_mullvad_egress.sh
M tests/contract/test_operator_network_scripts.py
```

Bash implementation mode remains `100755`. Fish wrapper and SSH-gate script are unchanged. `git diff --check` was clean.

## Claims

CA-01 — Candidate identity and scope: **PASS**
CA-02 — Preference readability, not command presence: **PASS**
CA-03 — Safe non-zero fallback: **PASS**
CA-04 — Complete status behavior: **PASS**
CA-05 — Privacy and sanitization: **PASS**
CA-06 — Mutation invariance: **PASS**
CA-07 — Authentic regression test: **PASS**
CA-08 — Red-to-green evidence: **PASS**
CA-09 — Documentation consistency: **PASS**

`detect_tailscale_get` now sets the preference surface usable only when `tailscale get exit-node` exits zero. Any non-zero probe result marks it unusable, discards probe stderr into a scrubbed temp directory, and lets `status` classify selected exit-node from sanitized `tailscale status --json`. LAN-access is `unavailable-without-tailscale-get` whenever that surface is unusable. Mutation subcommands, `tailscale set` arguments, LAN-access-false enable semantics, node validation, privilege behavior, and the standalone Mullvad mutation boundary are unchanged. No retry, sleep, version gate, sudo, `up`/`down`/`login`/`logout`, or operator grant was introduced.

The added test reproduces `get exit-node` non-zero with a short unclassified stderr token, healthy JSON with backend `Running`, no selected exit node, Mullvad nodes available, self not advertising, and standalone Mullvad `Disconnected`. It asserts status completion, sanitized labels, standalone classification, empty set-log, no mutation argv, no probe token, and no fixture secrets.

## Control matrix

Positive controls: **PASS** — readable `get` remains usable; unreadable `get` falls back to sanitized status JSON; backend `Running` is preserved; no selected node becomes `none`; Mullvad availability and self-advertisement remain classified; standalone Mullvad is reached; LAN-access stays explicitly unavailable without usable preference reads; probe stderr is discarded; synthetic status exits zero.

Negative controls: **PASS** — no command-presence-only success inference; no raw stderr/JSON/IP/identity/node/fixture-token leakage in synthetic or live sanitized matrices; no LAN-access guess; standalone Mullvad not skipped; pytest harness resolves only pytest-managed absolute fakes under `FRAMENEST_NETWORK_TEST_HOOKS=1` and does not fall back to trusted PATH for required tools; no fake `set`/`up`/`down`/`login`/`logout` on the regression path; no mutation-subcommand change; no retry/sleep/version/sudo/repair; no unrelated repository change.

## Red-to-green

Harness isolation: `_run_bash` sets `FRAMENEST_NETWORK_TEST_HOOKS=1` and absolute fake executables under pytest `tmp_path`. Production resolution uses those overrides only when the hook is set and otherwise searches a trusted PATH; the regression never reaches a real `tailscale`/`mullvad`.

Throwaway parent snapshot from `git archive 20369a197daedac25569fef077400a9754cd1d5f` below `/tmp/framenest-w9-acceptance.*`, with only the candidate test file copied in.

Parent result: `test_unreadable_tailscale_get_prefs_fall_back_to_status_json` non-zero (`rc=1`); sanitized first causal assertion: `assert result.returncode == 0`; abort class: `tailscale get is present but could not read`.
Candidate result: same test `1 passed` (`rc=0`).
Candidate worktree/index/refs remained unchanged.

## Validation

Syntax:

```text
bash -n scripts/operator/network/framenest_mullvad_egress.sh -> 0
fish -n scripts/operator/network/framenest_mullvad_egress.fish -> 0
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish -> 0
```

Provenance:

```text
framenest.__file__ = /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py
```

Exact candidate pytest (scrubbed env, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `PYTHONPATH=<candidate>/src`):

```text
tests/contract/test_operator_network_scripts.py
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_integration.py
exit 0
77 passed
```

## Live `ahw` status

Command: exact candidate `scripts/operator/network/framenest_mullvad_egress.fish status`
Exit: 0
Original unreadable-preference shape: still present (not `changed-external-state`)

Sanitized `ahw` matrix:

```text
backend: Running
client-get: unsupported
selected exit-node class: none
LAN access: unavailable-without-tailscale-get
mullvad-nodes: available
self-advertises-exit-node: no
standalone-mullvad-tunnel: disconnected
```

Standalone Mullvad readiness: `disconnected` — safe for a later separately authorized enablement slice on `ahw`. No raw stderr, JSON, IPs, node names, or identity were reported.

## NUC assignment readback

Transport: exact candidate `framenest_nuc_worker_gate.fish` with required SSH posture; candidate Bash script fed on stdin to `/usr/bin/bash -s -- status`. Strict SSH succeeded.

Sanitized NUC matrix:

```text
backend: Running
client-get: supported
selected exit-node class: none
LAN access: false
mullvad-nodes: unavailable
self-advertises-exit-node: no
standalone-mullvad-tunnel: absent
operator configured: not provided by status output
```

NUC Mullvad nodes = unavailable
Operational readiness = not-ready
Reason: NUC assignment has not propagated to device-visible Mullvad availability
Standalone Mullvad on NUC: `absent`

This operational observation coexists with repository `acceptance-PASS`. No live enablement should be authorized until a later read-only device-side check proves NUC Mullvad availability.

## Containment and mutations

Private temporary root class: `/tmp/framenest-w9-acceptance.*` mode `700`; captured files mode `0600`.
Cleanup: exact `rm -rf -- "$audit_root"` after case-guard; `test ! -e "$audit_root"` succeeded.
Real mutation, sudo, account action, provider action, deployment, publication, AP mutation, Meta mutation: none.
Forbidden network diagnostics (`curl`, `ping`, `ip`, direct `/usr/bin/mullvad`, `tailscale set`/`up`/`down`/`login`/`logout`): none.

## Deviations, limitations, residual risks

Independent red-to-green required a throwaway parent snapshot; the first two pytest attempts used the wrong working directory and were discarded. Final parent-red and candidate-green evidence was obtained from the correct trees.
Live `ahw` still exhibits the original unreadable-preference shape; synthetic red-to-green remains the acceptance control for that defect.
NUC preference reads succeed, so the live NUC path did not re-exercise the unreadable-`get` fallback. That does not weaken CA-08.
Gitignored `.pytest_cache` / `__pycache__` objects were present in the candidate worktree; Git porcelain remained clean and the candidate was not mutated.
Residual operational risk: NUC Mullvad nodes remain unavailable, so later enablement would fail preflight even after this correction is published.

Resolved Execution Issues / Near-Misses: initial parent pytest was invoked from the candidate worktree and from `/tmp` rather than the throwaway snapshot; a later `--override-ini cache_dir` option aborted collection; a zsh-quoting error delayed the first `ahw` status invocation. Cause: command-cwd and quoting mistakes. Resolution: re-ran from the snapshot and candidate roots with private capture and AppImage-variable scrubbing. Residual risk: none for the accepted evidence set.
Pre-Existing Failure Classification: none

## Smallest next step

Separately authorized publication of exact accepted candidate `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`. That statement grants no publication, deployment, account, privilege, rollback-timer, host-mutation, or live-egress authority. No live enablement should be authorized until a later read-only device-side check proves NUC Mullvad availability.

External trace disposition: configured
Trace discovery: projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/
Trace project key: framenest
Trace logical-whole projection identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Trace authority: historical-evidence-only
Trace archival owner: separately authorized archive workflow after the terminal outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none