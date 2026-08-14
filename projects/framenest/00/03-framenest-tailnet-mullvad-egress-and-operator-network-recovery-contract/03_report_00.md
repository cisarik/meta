### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 03
Worker exchange ordinal: 01

Standard terminal status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: f2a98a17ce7f4c82f33e0492870f11c02f4af0b3
Result evidence: independent read-only audit of exact candidate `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3` in `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2`; allowlist, syntax, provenance, and focused pytest 75 passed; AC-11 fails because the documented NUC rollback has no ten-minute duration
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: all Worker 3 authority expired at this terminal report

Acceptance candidate: f2a98a17ce7f4c82f33e0492870f11c02f4af0b3
Acceptance owner map: evaluated against section 9
Acceptance allowlist: evaluated against section 8
Acceptance risk claims: AC-01 through AC-14
Acceptance control matrix: positive and negative controls from section 11
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none

## Routing and independence

- Fresh-session confirmation: this conversation began with this prompt; Worker session target `fresh-worker-session`; exchange `01`.
- Native Plan Mode confirmation: requested `not-used`; observed not in native planning mode; no plan-to-execution transition occurred.
- Independence from Worker 2 implementation: this session did not implement, correct, or previously audit `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3`. Worker 2’s report was treated as a claim only and was not used as proof of behavior.

## Directly observed capabilities

| Row | Requested | Observed | Evidence class |
|---|---|---|---|
| Client/surface | Cursor Worker | Cursor agent session | directly observed |
| Model | Cursor Grok 4.6 (system-stated) | not independently attested | unknown/not observably exposed |
| Reasoning | High | not independently enforced | unknown/not observably exposed |
| Native planning | not-used | not active | directly observed |
| Internal delegation | not-used | not used | directly observed |
| Filesystem | candidate worktree read | exact worktree readable | directly observed |
| Canonical interpreter | owner `.venv` | `/home/agile/Projects/framenest/.venv/bin/python` | directly observed |
| Public-ref verification | `git ls-remote` | succeeded | directly observed |
| Live host/network tools | forbidden | not invoked | directly observed |

Capability does not grant authority. Unknown: provider quota, exact context window, independent model attestation.

## Repository identity

Start commit: `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3`
End commit: `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3` (no mutation)

| Gate | Required | Observed |
|---|---|---|
| root | `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2` | match (`pwd -P`) |
| origin | `cisarik/framenest` | `https://github.com/cisarik/framenest.git` |
| branch | `feat/tailnet-mullvad-egress-recovery-contract` | match |
| HEAD | `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3` | match before and after |
| tree | `db23a95acc9decc22672b785227cd9d47ce23b42` | match before and after |
| parent | `148b6c2012809944262399c1a166e85082606fbf` | single parent, match |
| subject | `feat: add Mullvad egress recovery controls` | match |
| `.ap` gitlink and HEAD | `041de310ea33ed1b47dd8f5fbfcc2829d1a32514` | match |
| public `main` | `148b6c2012809944262399c1a166e85082606fbf` | match before and after via `git ls-remote` |
| worktree/index | clean, untracked none | clean before and after (`git status --porcelain=v1 --untracked-files=all`; `git diff` / `git diff --cached` exit 0) |

Commit count parent..candidate: `1`.

## Allowlist and modes

Changed paths (exact, all inside the allowlist):

```text
M README.md
M SECURITY.md
M SERVER.md
M deploy/ubuntu/README.md
A docs/OPERATOR_NETWORK.md
M docs/UBUNTU_NUC_DEPLOYMENT.md
A docs/adr/0058-independent-mullvad-egress-and-operator-network-recovery.md
M docs/adr/README.md
A scripts/operator/network/README.md
A scripts/operator/network/framenest_mullvad_egress.fish
A scripts/operator/network/framenest_mullvad_egress.sh
A scripts/operator/network/framenest_nuc_worker_gate.fish
A tests/contract/test_operator_network_scripts.py
```

`git diff --check` exit 0. Forbidden paths unchanged. Executable modes:

```text
100755 scripts/operator/network/framenest_mullvad_egress.sh
100755 scripts/operator/network/framenest_mullvad_egress.fish
100755 scripts/operator/network/framenest_nuc_worker_gate.fish
```

## Owner-map consistency

Evaluated against section 9: **consistent**.

- ADR-0058 owns accepted/rejected topology.
- `docs/OPERATOR_NETWORK.md` owns the operator contract and recovery sequence.
- Bash script owns shared behavior; Fish egress wrapper only resolves the adjacent Bash script and forwards `$argv`; SSH gate owns strict noninteractive SSH.
- Contract tests own synthetic evidence.
- Script README is discoverability only.
- ADR index is a single 0058 row.
- README, SERVER, SECURITY, UBUNTU NUC runbook, and `deploy/ubuntu/README.md` add inbound links only; the production SHA `aec2f0091c10aed2fc2033dac154a0d9651b2b6d` in the NUC runbook is unchanged. No competing operational procedure was introduced in those inbound files.

## Acceptance risk claims

| Claim | Result |
|---|---|
| AC-01 Architecture integrity | PASS |
| AC-02 Public and private data boundary | PASS |
| AC-03 Bash interface and parsing | PASS |
| AC-04 Mutation boundary | PASS |
| AC-05 Fail-closed preconditions | PASS |
| AC-06 Failure and recovery behavior | PASS |
| AC-07 Diagnostic privacy | PASS |
| AC-08 Environment hygiene and executable resolution | PASS |
| AC-09 Fish wrapper | PASS |
| AC-10 NUC SSH gate | PASS |
| AC-11 Headless recovery documentation | FAIL |
| AC-12 Test authenticity | PASS |
| AC-13 Test coverage | PASS |
| AC-14 Documentation consistency | PASS |

### AC-11 FAIL (acceptance-blocking)

The NUC procedure documents a separately authorized transient rollback, cancel-after-successful-`verify`, one-device-at-a-time reboot, and that repository presence grants no host/account/Tailscale authority. Scripts contain no `systemd-run` / `systemctl` timer activation.

The fixed claim also requires a **ten-minute** rollback duration. Neither `docs/OPERATOR_NETWORK.md` nor ADR-0058 states any duration. That is a concrete omission in the recovery-sequence owner, not a live-host defect.

### Claim notes (non-blocking)

- AC-02: test fixtures use documentation-reserved TEST-NET IPs (`203.0.113.10`, `198.51.100.20`) and do not appear in script output. Valid-node fixture `se-got-wg-001.mullvad.ts.net` is a public-style Mullvad DNS name, not a private FrameNest identity; operator docs use placeholders.
- AC-05: daemon-present/unproven Mullvad CLI text classifies as `ambiguous` and blocks mutation; it is not labeled `connected`. Established by inspection of `classify_mullvad_cli` / `preflight_mutation`.
- AC-07: HTTP non-200 and parse failure report `unknown`, not `non-Mullvad egress`. Established by inspection of `cmd_verify`; committed tests cover transport failure and Mullvad/non-Mullvad classification.
- AC-13: committed tests materially cover the named requirement list. Harness fixtures exist for `curl_mode=http-error`, `curl_mode=invalid`, and `mullvad_mode=daemon-only` but are not invoked; those modes remain inspection-backed, not test-backed.

## Control matrix

Positive controls:

| Control | Result |
|---|---|
| exact valid Mullvad DNS node | PASS (`se-got-wg-001.mullvad.ts.net` enable) |
| enable produces exact `tailscale set` arguments | PASS (`set --exit-node=se-got-wg-001.mullvad.ts.net --exit-node-allow-lan-access=false`) |
| LAN access false | PASS |
| disable clears exit node | PASS (`set --exit-node=`) |
| recover clears exit node | PASS |
| Mullvad diagnostic fixture | PASS (`Mullvad egress`) |
| non-Mullvad diagnostic fixture | PASS (`non-Mullvad egress`, non-zero) |
| disconnected standalone Mullvad not treated as connected | PASS |
| daemon-present but tunnel-unproven distinguished | PASS by inspection (`ambiguous`, not `connected`) |
| Fish wrapper preserves arguments and exit | PASS |
| SSH gate exact strict option vector | PASS (all eight `-o` options logged) |

Negative controls:

| Control | Result |
|---|---|
| missing `--node` | PASS |
| empty or option-like node | PASS (missing `--node`; `--evil.mullvad.ts.net`; empty `--node=` rejected in source) |
| whitespace and shell-metacharacter node | PASS (whitespace tested; metacharacters rejected by DNS regex before tool use) |
| suffix-confusion and non-Mullvad node | PASS |
| unknown subcommand, flag, or operand | PASS (unknown subcommand tested; flag/operand rejected in `cmd_enable` / `main`) |
| `NeedsLogin` | PASS |
| unavailable Mullvad nodes | PASS |
| self-advertised exit node | PASS |
| positively detected standalone Mullvad tunnel | PASS |
| unsupported/ambiguous client state | PASS (non-Running backend refused; ambiguous Mullvad CLI refused) |
| diagnostic transport, HTTP, or parsing failure | PASS (transport tested; HTTP/parse by inspection → `unknown`) |
| no public IP or raw JSON output | PASS |
| no `auto:any` | PASS |
| no `tailscale up/down/login/logout` | PASS |
| no implicit `sudo` or `--operator` | PASS |
| no environment-variable leakage to child tools | PASS |
| no real tool fallback | PASS (see harness isolation) |
| no SSH interactive fallback, forwarding, `accept-new`, or private hardcoding | PASS |
| no public inbound, firewall, routing, DNS, Wi-Fi, NetworkManager, sysctl, Serve, Funnel, or systemd mutation | PASS |

## Syntax

```text
bash -n scripts/operator/network/framenest_mullvad_egress.sh  -> exit 0
fish -n scripts/operator/network/framenest_mullvad_egress.fish -> exit 0
fish -n scripts/operator/network/framenest_nuc_worker_gate.fish -> exit 0
fish present: /usr/bin/fish
```

## Pytest

Exact command:

```bash
env \
  -u APPIMAGE \
  -u APPDIR \
  -u ARGV0 \
  -u LD_LIBRARY_PATH \
  -u LD_PRELOAD \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src \
  /home/agile/Projects/framenest/.venv/bin/python \
  -m pytest \
  -p no:cacheprovider \
  tests/contract/test_operator_network_scripts.py \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_integration.py
```

Exit status: `0`
Test count: `75 passed` in 1.32s (collected 75). Operator-network file contributed 37 of those items.

## Candidate-source provenance

```text
/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py
```

Resolves under the exact candidate `src/` as required.

## Synthetic-tool isolation

Before pytest: with `FRAMENEST_NETWORK_TEST_HOOKS=1`, `resolve_required_tool` / `_resolve_tool` accept only an absolute override and exit otherwise; they never search `PATH`. Optional `mullvad` likewise does not fall back to a real binary. Production resolution uses `PATH=/usr/sbin:/usr/bin:/sbin:/bin` only when the hook is unset. All subprocess tests set the hook and pytest-managed fake executables. A cwd `tailscale` trap is installed; unknown-subcommand leaves it uninvoked. `python3` may be resolved from the trusted path for JSON parsing; that is not a forbidden live network tool. Pre-existing contract tests invoke `fish --no-execute` and `./.ap/ap doctor` only.

## Live / forbidden actions

No real `tailscale`, `mullvad`, `ssh`, `sudo`, `systemctl`, `systemd-run`, `curl`, `wget`, `ping`, `ip`, `resolvectl`, `networkctl`, or `nmcli` was executed. No Mullvad diagnostic endpoint or host was contacted. The only network operation was `git ls-remote origin refs/heads/main`. No browser, GUI, credential, publication, deployment, AP mutation, or Meta write occurred. Canonical repository mutation: none.

## Discrepancies, missing evidence, residual risks

1. **Acceptance-blocking:** AC-11 omits the required ten-minute rollback duration from the operator contract and ADR.
2. Residual: HTTP-error, parse-failure, and daemon-only harness branches are unimplemented as tests.
3. Residual: ignored `__pycache__` files existed before this session (mtime 2026-08-13 19:53–19:54 +0200); git status without `--ignored` remained clean; this audit did not create or delete them.
4. This is repository acceptance only. It is not live-host, account, publication, or production acceptance.

Resolved Execution Issues / Near-Misses: pre-existing gitignored `tests/contract/__pycache__/*.pyc` from an earlier session was observed after pytest; `PYTHONDONTWRITEBYTECODE=1` prevented new bytecode in this audit; files were not deleted because this task has no cleanup authority. Residual risk: none to candidate Git identity.

Pre-Existing Failure Classification: none

## Smallest next step

Separately authorize a Bounded Correction Worker to add the missing **ten-minute** transient-rollback duration to `docs/OPERATOR_NETWORK.md` (recovery-sequence owner) and the matching sentence in `docs/adr/0058-independent-mullvad-egress-and-operator-network-recovery.md`, plus a documentation assertion in `tests/contract/test_operator_network_scripts.py` if that remains in the correction allowlist. Then route a fresh independent re-audit of the corrected unpublished candidate. This grants no publication, host, sudo, account, or timer-install authority.