### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 12
Worker exchange ordinal: 01

```text
Standard terminal status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: a23b4bc786357da3591a4f75087b7e8a3d50d341
Result evidence: authentic red on opaque readable get; both new regression controls green; focused suite 79 passed; syntax 0; candidate-source provenance under the authorized worktree; read-only candidate status classified both live ahw and NUC as Mullvad with NUC LAN-access false; private confirm root removed
Logical-whole closure: not-closed
Report justification: new-mutation
Authority expiry: all Worker 12 authority expired at this terminal report
```

## Freshness and Native Plan Mode

- Worker session target: `fresh-worker-session` (this conversation started with the complete Worker 12 prompt; no prior Worker 12 authority was inherited).
- Native planning mode: `not-used` (implementation proceeded in Agent mode; Plan Mode was not used).
- Worker session profile: Bounded Correction Worker.
- Evidence posture: non-independent.
- Internal delegation: not-used.
- Publication, host-network mutation, push: none.

## Repository baseline

- Exact worktree: `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2`
- Remote origin: `https://github.com/cisarik/framenest.git`
- Branch: `feat/tailnet-mullvad-egress-recovery-contract`
- Pre-correction HEAD / public `main`: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
- Pre-correction tree: `4c4d09e3d6ed9204c9f26905290cc31397e97d02`
- Pre-correction parent: `20369a197daedac25569fef077400a9754cd1d5f`
- AP pin / `.ap` HEAD: `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`
- Pre-correction worktree and index: clean; untracked files: none
- Public `main` immediately before commit: still `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`

## Recovery classification

```text
Classification unit type: worktree
Classification unit identity: /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2 at 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
Classification accepted-continuation: applicable because new live evidence authorizes one bounded diagnostic correction
Classification unrelated-owner-work: not-applicable if the worktree is clean and exact
Classification stale-clone: not-applicable because local HEAD equals public main
Classification unpublished-candidate: not-applicable before correction
Classification unexplained-divergence: not-applicable only if no material remainder exists
Primary recovery classification: accepted-continuation
Secondary recovery classifications: none
Immediate recovery action: apply only the selected-status classification correction
Publication status: baseline public; correction not yet created
Mutation before classification: none
Destructive recovery operation: none
```

## Changed paths and purpose

Only the three allowlisted paths:

- `scripts/operator/network/framenest_mullvad_egress.sh` — after a successful readable non-empty `get exit-node`, keep unsafe-colon and explicit `.mullvad.ts.net` classification; otherwise, if sanitized status JSON already classified the selected peer as Mullvad, report `mullvad:<sanitized-selected-mullvad-dns>` instead of `non-mullvad`. The opaque preference is never emitted.
- `tests/contract/test_operator_network_scripts.py` — positive and negative regression controls for that reconciliation.
- `docs/OPERATOR_NETWORK.md` — existing installed-command feature-detection/status paragraph now states that readable `get` remains the preference and LAN-access surface, an opaque/non-DNS preference is not itself a provider classification, sanitized status JSON identifies Mullvad vs non-Mullvad, and raw opaque values are not emitted.

Forbidden paths, including both Fish scripts, were not modified.

## Authentic red result

Before the Bash change, only:

```text
tests/contract/test_operator_network_scripts.py::test_readable_opaque_get_reconciles_selected_mullvad_from_status_json
```

Collection succeeded. Exit 1. Failure signature was behavioral: status exit 0 with `client-get: supported` and `exit-node: non-mullvad` instead of `exit-node: mullvad:<synthetic-mullvad-dns>`. Not a syntax, import, collection, interpreter, or harness failure.

## Correction semantics

For a successful readable non-empty `get exit-node` value:

1. colon-containing forms remain `unsafe-non-explicit`;
2. explicit `.mullvad.ts.net` remains Mullvad from that hostname;
3. otherwise the already sanitized selected-peer fields from `tailscale status --json` are consulted;
4. upgrade to `mullvad:<SELECTED_MULLVAD_DNS>` only when `SELECTED_KIND` is `mullvad` and that DNS is non-empty;
5. otherwise retain `non-mullvad`.

Empty readable preference remains `none`. JSON without a selected Mullvad peer cannot upgrade an opaque value. LAN-access, `enable` / `disable` / `verify` / `recover`, mutation arguments, `detect_tailscale_get`, and JSON acquisition were unchanged.

## Regression controls

- `test_readable_opaque_get_reconciles_selected_mullvad_from_status_json`: opaque readable get + selected Mullvad peer in JSON → `exit-node: mullvad:<synthetic-mullvad-dns>`; LAN `false`; client-get `supported`; no opaque token, JSON, or fixture secrets; no mutation command. Passed after the correction.
- `test_readable_opaque_get_keeps_selected_non_mullvad_from_status_json`: opaque readable get + selected non-Mullvad exit-node option → `exit-node: non-mullvad`; no Mullvad upgrade; opaque token not emitted; no mutation. Passed.

Harness inspection: tests set `FRAMENEST_NETWORK_TEST_HOOKS=1` and absolute fake tool paths only. Production trusted-PATH resolution is not used. No real `tailscale`, `curl`, SSH, or network contact.

## Syntax, provenance, and focused suite

```text
bash -n scripts/operator/network/framenest_mullvad_egress.sh  → 0
fish -n scripts/operator/network/framenest_mullvad_egress.fish → 0
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish → 0
```

Provenance command printed:

```text
/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py
```

That path is under the exact authorized worktree `src/`.

Focused pytest (canonical interpreter, candidate `PYTHONPATH`, AppImage scrub, `-p no:cacheprovider`):

```text
tests/contract/test_operator_network_scripts.py
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_integration.py
```

Exit 0. `collected 79 items` / `79 passed`.

## Sanitized live candidate-status matrices

Read-only candidate `status` only. No `enable`, `disable`, `verify`, `recover`, `tailscale set`, public diagnostic, sudo, or timer.

**ahw** (`framenest_mullvad_egress.fish status`, candidate wrapper):

| Field | Result |
|---|---|
| exit | 0 |
| backend | Running |
| client-get | unsupported |
| selected exit-node class | Mullvad |
| lan-access | unavailable-without-tailscale-get |
| mullvad-nodes | available |
| self-advertises-exit-node | no |
| standalone-mullvad-tunnel | disconnected |

**NUC** (strict SSH gate; remote `/usr/bin/bash -s -- status`; candidate Bash on stdin; not installed):

| Field | Result |
|---|---|
| exit | 0 |
| backend | Running |
| client-get | supported |
| selected exit-node class | Mullvad |
| lan-access | false |
| mullvad-nodes | available |
| self-advertises-exit-node | no |
| standalone-mullvad-tunnel | absent |

Exact selected hostnames and any opaque preference remained in the private capture only and are not reported.

Live exit nodes changed: **no**. Both already-active Mullvad exit nodes were left untouched.

## Private-root class and cleanup

- Root class: `/tmp/framenest-w12-status-confirm.*`
- Capture mode: `umask 077` / files `0600`
- Cleanup: `rm -rf -- "$live_root"` after the class-prefix check
- Outcome: removed; `test ! -e "$live_root"` succeeded; no matching confirm roots remained
- No external pointer file; no other path deleted

## Commit and final cleanliness

- Commit: `a23b4bc786357da3591a4f75087b7e8a3d50d341`
- Tree: `a1ea29c5fa7e6878670b243ef34b8b0b31084829`
- Parent: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
- Subject: `fix: reconcile selected Mullvad status`
- Commits above `4add009…`: exactly 1
- Worktree and index: clean
- Untracked files: none
- Push: **none**

## Forbidden effects

No push, public diagnostic, sudo, timer, host mutation, account access, deployment, AP mutation, or Meta write occurred. Meta files `12_correction.md` / `12_report.md` were not written.

## Deviations, limitations, residual risks, missing evidence

- This evidence is non-independent. The corrector does not certify the candidate.
- Live confirmation is one read-only candidate `status` on each device; public egress was not re-verified, by design.
- `ahw` still lacks readable `tailscale get`; LAN-access there remains `unavailable-without-tailscale-get`. That is unchanged and expected.
- Residual risk: a future opaque preference paired with JSON that does not positively select a Mullvad peer must remain `non-mullvad` (covered by the negative control). No version-specific client check was added.

## Resolved Execution Issues / Near-Misses

The private `live_root` shell variable did not persist into the next shell invocation, so the NUC capture aborted once locally with exit 90 before any remote command. The already-created `/tmp/framenest-w12-status-confirm.*` directory from this session was relocated and reused; NUC `status` then succeeded. Residual risk: none after capture and exact cleanup.

## Pre-Existing Failure Classification: none

## Smallest next step

One fresh independent acceptance of exact commit `a23b4bc786357da3591a4f75087b7e8a3d50d341`. That next task grants no publication or live-host authority.