### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 08
Worker exchange ordinal: 01

Standard terminal status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
Logical-whole closure: not-closed
Report justification: new-mutation
Authority expiry: all Worker 8 authority expired at this terminal report

## Session and routing

- Fresh-session confirmation: this exchange was delivered into a new Worker session with `Worker session target: fresh-worker-session`; no prior Worker 8 authority was reused.
- Native Plan Mode confirmation: requested `not-used`; observed Agent/implementation mode, not native planning mode.
- Worker session profile: Bounded Correction Worker.
- Evidence posture: non-independent. This session implemented the correction and cannot certify it.
- Internal delegation: not-used.
- Worker topology: single-active.

## Acceptance and Correction Record

```text
Acceptance candidate: 4add009e1f89fcc05b9e8bc306d6ecc8e568547b
Acceptance owner map: published operator status diagnostic in scripts/operator/network/framenest_mullvad_egress.sh plus matching contract test and OPERATOR_NETWORK feature-detection paragraph
Acceptance allowlist: scripts/operator/network/framenest_mullvad_egress.sh; tests/contract/test_operator_network_scripts.py; docs/OPERATOR_NETWORK.md
Acceptance risk claims: status must distinguish command presence from preference readability; unreadable get must fall back to sanitized status JSON; LAN-access remains unavailable without usable get; standalone Mullvad classification must still run; no raw stderr/JSON/identity leak; mutation subcommands unchanged
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none
```

## Repository identity and gates

| Fact | Value |
|---|---|
| Worktree | `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2` |
| Origin | `https://github.com/cisarik/framenest.git` |
| Branch | `feat/tailnet-mullvad-egress-recovery-contract` |
| Start HEAD | `20369a197daedac25569fef077400a9754cd1d5f` |
| Start tree | `9844fc72275f96ab0edc8f3dc3ae1ae43c8f7488` |
| Start parent | `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3` |
| End HEAD | `4add009e1f89fcc05b9e8bc306d6ecc8e568547b` |
| End tree | `4c4d09e3d6ed9204c9f26905290cc31397e97d02` |
| End parent | `20369a197daedac25569fef077400a9754cd1d5f` |
| End subject | `fix: fall back from unreadable Tailscale prefs` |
| AP pin / `.ap` HEAD | `041de310ea33ed1b47dd8f5fbfcc2829d1a32514` |
| Public `origin/main` before mutation and before commit | `20369a197daedac25569fef077400a9754cd1d5f` |
| Worktree/index after commit | clean; untracked files none |

Repository and public-ref gates passed. Recovery classification was applied before mutation as `accepted-continuation`.

```text
Classification unit type: worktree
Classification unit identity: /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2 at 20369a197daedac25569fef077400a9754cd1d5f
Classification accepted-continuation: applicable because this prompt authorizes one correction based on new live evidence
Classification unrelated-owner-work: not-applicable because the worktree was clean and exact
Classification stale-clone: not-applicable because local HEAD equaled public main
Classification unpublished-candidate: not-applicable before correction
Classification unexplained-divergence: not-applicable because no material remainder existed
Primary recovery classification: accepted-continuation
Secondary recovery classifications: none
Immediate recovery action: apply only the bounded compatibility correction
Publication status: baseline public; correction created locally and not pushed
Mutation before classification: none
Destructive recovery operation: none
```

## Changed paths and purpose

Only the three allowlisted paths changed:

1. `scripts/operator/network/framenest_mullvad_egress.sh` — mark `tailscale get` usable only when the read-only `get exit-node` probe exits zero; any non-zero result treats the preference surface as unavailable and continues through the existing sanitized JSON fallback.
2. `tests/contract/test_operator_network_scripts.py` — synthetic fake-tool state for the live unreadable-preference shape, plus assertions that `status` completes a sanitized matrix without mutation or secret leakage.
3. `docs/OPERATOR_NETWORK.md` — feature-detection paragraph now states readability, not mere command-name presence, and documents JSON fallback plus unavailable LAN-access.

No other tracked or untracked path changed. Push was not performed.

## Defect and fallback semantics

On baseline, `detect_tailscale_get` treated any non-unknown-command stderr as usable `get` support. A client where `get` exists but `get exit-node` returns unclassified non-zero then made `print_status` call `read_exit_node_from_get`, abort, and skip the sanitized matrix and standalone Mullvad classification.

After correction:

- usable preference reads require probe exit status 0;
- any non-zero probe result sets `HAVE_TAILSCALE_GET=no` for this invocation;
- `status` falls back to sanitized `tailscale status --json` for selected-exit-node classification;
- LAN-access remains `unavailable-without-tailscale-get`;
- `classify_mullvad_cli` still runs;
- failed-probe stderr is captured and discarded, not printed;
- `enable` / `disable` / `recover` mutation boundaries and `tailscale set` semantics are unchanged.

## Red-to-green regression evidence

Synthetic fixture:

- `tailscale get exit-node` non-zero with unclassified stderr token `fn-unreadable-pref-token`;
- `tailscale status --json` Running, no selected exit node, Mullvad nodes available, self not advertising;
- standalone `mullvad status` Disconnected.

Against baseline `20369a197daedac25569fef077400a9754cd1d5f` (script unfixed, test already present):

```text
FAILED test_unreadable_tailscale_get_prefs_fall_back_to_status_json
AssertionError: tailscale get is present but could not read the selected exit node.
assert 1 == 0
```

After the script correction, the same test passed: exit 0; `backend: Running`; `client-get: unsupported`; `exit-node: none`; `lan-access: unavailable-without-tailscale-get`; Mullvad nodes available; self-advertisement `no`; standalone Mullvad `disconnected`; no fake `set`/`up`/`down`/`login`/`logout`; no raw fake stderr, JSON, IP, or fixture token.

## Validation

Syntax:

```text
bash -n scripts/operator/network/framenest_mullvad_egress.sh  -> 0
fish -n scripts/operator/network/framenest_mullvad_egress.fish -> 0
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish -> 0
```

Candidate provenance under the required interpreter:

```text
PYTHONPATH=<worktree>/src
/home/agile/Projects/framenest/.venv/bin/python -c 'import framenest; print(framenest.__file__)'
-> /home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py
```

Focused pytest (exit 0, 77 passed = prior 76 plus one regression):

```text
env -u APPIMAGE -u APPDIR -u ARGV0 -u LD_LIBRARY_PATH -u LD_PRELOAD \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src \
  /home/agile/Projects/framenest/.venv/bin/python -m pytest -p no:cacheprovider \
  tests/contract/test_operator_network_scripts.py \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_integration.py
============================== 77 passed in 1.40s ==============================
```

`git diff --check` passed before commit. After commit, worktree and index are clean. `git show --name-only` lists only the three allowlisted paths.

## Side-effect and prohibition evidence

- Real `tailscale`, `mullvad`, `ssh`, `sudo`, `systemctl`, `systemd-run`, `curl`, `wget`, `ping`, `ip`, `resolvectl`, `networkctl`, and `nmcli` were not executed. Only pytest-managed fake executables were used by the suite.
- No host, Tailscale account, Mullvad, route, DNS, firewall, Wi-Fi, NetworkManager, Serve, Funnel, FrameNest production, AP, or Meta mutation occurred.
- No browser, GUI, AppImage, credential store, private key, or production data was opened.
- No `.venv` reconstruction, Poetry/uv install, fetch, merge, rebase, push, or publication occurred.
- Meta files `08_correction.md` / `08_report.md` were not written.

## Deviations, missing evidence, limitations, residual risks

- Evidence is synthetic and non-independent. The original live `ahw` unreadable-`get` shape was reproduced only by fake tools.
- Separate live findings remain unaddressed by design: NUC Mullvad nodes unavailable; NUC has no valid Mullvad suggestion; standalone Mullvad on `ahw` was unknown because live `status` aborted; neither device has a configured Tailscale operator.
- This correction does not prove live-host recovery. Publication and live use remain unauthorized.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

## Smallest next step

One fresh independent acceptance of candidate `4add009e1f89fcc05b9e8bc306d6ecc8e568547b` against the original live unreadable-`get` failure claim. That grant does not include publication or live-host authority.