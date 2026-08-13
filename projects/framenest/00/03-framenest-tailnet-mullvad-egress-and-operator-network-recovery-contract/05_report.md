### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract  
Worker session ordinal: 05  
Worker exchange ordinal: 01

Standard terminal status: PASS  
Phase-qualified result: acceptance-PASS  
Result artifact or commit: 20369a197daedac25569fef077400a9754cd1d5f  
Result evidence: independent static inspection of the unpublished candidate plus the authorized synthetic pytest suite (76 passed); worktree remained clean; public `main` remained `148b6c2012809944262399c1a166e85082606fbf`  
Logical-whole closure: not-closed  
Report justification: final-acceptance  
Authority expiry: all Worker 5 authority expired at this terminal report

Acceptance candidate: 20369a197daedac25569fef077400a9754cd1d5f  
Acceptance owner map: evaluated against section 8  
Acceptance allowlist: evaluated against section 7  
Acceptance risk claims: AC-01 through AC-14  
Acceptance control matrix: positive and negative controls from section 10  
Acceptance independence: required-fresh-independent  
Primary fresh acceptances used: 1  
Automatic corrections used: 1  
Correction re-acceptance: full-fresh  
Named missing-evidence probe: none  
Out-of-scope observations: none

## Freshness, routing, and independence

This was a genuine fresh Worker session. Native Plan Mode was not active. This session did not implement `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3`, did not perform Worker 3’s audit, and did not author corrective commit `20369a197daedac25569fef077400a9754cd1d5f`. Prior reports were treated as claims only. No internal delegation was used.

## Observed capabilities and unknowns

Directly observed: read-only Git, filesystem inspection of the named worktree, canonical interpreter `/home/agile/Projects/framenest/.venv/bin/python` (CPython 3.13.9), `bash -n`, `fish -n`, pytest 9.1.1, and one `git ls-remote` of `origin`.  
Unknown / not independently attested: model identity.  
Not used: live Tailscale, Mullvad, SSH, sudo, systemd, host mutation, diagnostic HTTP, provider accounts, Meta, publication, or repository writes.

## Immutable candidate identity

| Gate | Observed |
|---|---|
| Physical root | `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2` |
| Origin | `https://github.com/cisarik/framenest.git` |
| Branch | `feat/tailnet-mullvad-egress-recovery-contract` |
| HEAD / start / end commit | `20369a197daedac25569fef077400a9754cd1d5f` |
| HEAD tree | `9844fc72275f96ab0edc8f3dc3ae1ae43c8f7488` |
| HEAD parent | `f2a98a17ce7f4c82f33e0492870f11c02f4af0b3` |
| HEAD subject | `fix: specify NUC rollback duration` |
| HEAD grandparent / public main | `148b6c2012809944262399c1a166e85082606fbf` |
| HEAD^ tree | `db23a95acc9decc22672b785227cd9d47ce23b42` |
| HEAD^ subject | `feat: add Mullvad egress recovery controls` |
| Commits above public baseline | 2 |
| Corrective commits above `f2a98a…` | 1 |
| `.ap` gitlink and checkout | `041de310ea33ed1b47dd8f5fbfcc2829d1a32514` |
| Cleanliness before | clean; untracked none |
| Cleanliness after | clean; untracked none |
| Public `main` (`git ls-remote`) | `148b6c2012809944262399c1a166e85082606fbf` |

## Allowlists, modes, and unchanged paths

Complete candidate vs public baseline (exact allowlist, 13 paths):

- `M` `README.md`, `SECURITY.md`, `SERVER.md`, `deploy/ubuntu/README.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/adr/README.md`
- `A` `docs/OPERATOR_NETWORK.md`, `docs/adr/0058-independent-mullvad-egress-and-operator-network-recovery.md`, `scripts/operator/network/README.md`, `scripts/operator/network/framenest_mullvad_egress.sh`, `scripts/operator/network/framenest_mullvad_egress.fish`, `scripts/operator/network/framenest_nuc_worker_gate.fish`, `tests/contract/test_operator_network_scripts.py`

Correction vs `f2a98a…` (exact correction allowlist only):

- `M` `docs/OPERATOR_NETWORK.md`
- `M` `tests/contract/test_operator_network_scripts.py`

Executable modes at HEAD: all three scripts `100755`. `git diff --check` was clean for both the full and corrective diffs.

Unchanged from public baseline as required: `.ap`, `.gitmodules`, `ap.project.conf`, `pyproject.toml`, `poetry.lock`, `uv.lock`, `src/**`, `migrations/**`, `deploy/systemd/**`, `docs/NUC_HOST_BASELINE.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`. Unrelated production SHA `aec2f0091c10aed2fc2033dac154a0d9651b2b6d` in the Ubuntu NUC runbook is unchanged.

## Owner-map verdict

PASS. ADR-0058 owns architecture and rejected alternatives and does not state the ten-minute duration. `docs/OPERATOR_NETWORK.md` owns topology, sequence, transient rollback, verification, recovery, privacy, and authority, including the exact `10 minutes` delay. The Bash script owns shared behavior; the Fish wrapper is thin invocation only; the SSH gate owns strict transport only; the contract test owns synthetic evidence; script README and ADR index are discoverability/index only; inbound documents are concise links. Worker 4 did not duplicate the duration into ADR-0058 or inbound-link documents. Repository-wide, `10 minutes` appears only in the operational rollback section and in the test that reads that section.

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
| AC-11 Corrected headless recovery contract | PASS |
| AC-12 Test authenticity | PASS |
| AC-13 Test coverage | PASS |
| AC-14 Documentation consistency | PASS |

### AC-11 wording and test enforcement

`docs/OPERATOR_NETWORK.md` section `## Transient NUC rollback design` now states that rollback is armed before changing the NUC exit-node preference, the delay is exactly `10 minutes`, and the timer remains able to fire if SSH disconnects or the Worker terminates. Cancellation is only after SSH, Mullvad-egress, FrameNest-health, and Serve/Funnel gates. Reboot acceptance is one host at a time. Repository presence grants no timer, sudo, host, Tailscale, or account authority. Scripts contain no `systemd-run` / `systemctl` timer activation.

Worker 4 changed only the operational owner and its test. Added test `test_operator_network_doc_requires_ten_minute_nuc_rollback` splits on `## Transient NUC rollback design` and asserts `10 minutes` in that window. The phrase is not present in earlier OPERATOR_NETWORK prose, ADR-0058, or inbound-link documents, so the assertion is not satisfied by unrelated owners. Residual tightness: the split is heading-to-EOF rather than heading-to-next-heading; on this candidate the unique documentation occurrence is still the rollback paragraph itself.

## Control matrix

Positive controls satisfied: valid explicit Mullvad DNS node; exact `tailscale set --exit-node=<node> --exit-node-allow-lan-access=false`; disable/recover `set --exit-node=`; Mullvad and non-Mullvad diagnostic labels; disconnected standalone Mullvad allowed; daemon-present-without-Connected is not treated as a competing tunnel; Fish argument and exit preservation; exact SSH option vector; rollback section states `10 minutes`; rollback-duration test reads that section.

Negative controls satisfied by static inspection plus the suite: missing/empty/option-like/whitespace/suffix-confused/non-Mullvad nodes; unknown subcommand; `NeedsLogin`; missing Mullvad availability; self-advertisement; connected standalone Mullvad; ambiguous Mullvad CLI and non-Running backend; diagnostic transport failure reported as `unknown` not `non-Mullvad egress`; no public IPs or raw JSON in operator output; no `auto:any`; no `tailscale up/down/login/logout`; no `sudo` or `--operator`; AppImage/library variables scrubbed from children; test hooks fail closed without real-tool fallback; no SSH `accept-new`, forwarding, interaction, or hardcoded private identity; no firewall/routing/DNS/Wi-Fi/NetworkManager/sysctl/Serve/Funnel/systemd mutation; no rollback-duration duplication into ADR-0058 or inbound links.

Dedicated HTTP-error, invalid-JSON, and daemon-only test functions remain absent. Implementation handles those states fail-closed. Per the prompt they are not new blocking scope.

## Validation

Syntax:

- `bash -n scripts/operator/network/framenest_mullvad_egress.sh` — exit 0
- `fish -n scripts/operator/network/framenest_mullvad_egress.fish` — exit 0
- `fish -n scripts/operator/network/framenest_nuc_worker_gate.fish` — exit 0

Candidate-source provenance under the required scrubbed invocation:

```text
/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py
```

Exact pytest command (cwd = candidate worktree):

```text
env -u APPIMAGE -u APPDIR -u ARGV0 -u LD_LIBRARY_PATH -u LD_PRELOAD \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2/src \
  /home/agile/Projects/framenest/.venv/bin/python -m pytest -p no:cacheprovider \
  tests/contract/test_operator_network_scripts.py \
  tests/contract/test_nuc_operator_runbook.py \
  tests/contract/test_fedora_systemd_service.py \
  tests/contract/test_ap_integration.py
```

Exit status: 0. Result: `76 passed` in 1.35s. No skips.

Synthetic isolation: harness inspected before execution. Behavioral tests install pytest `tmp_path` fake executables and set `FRAMENEST_NETWORK_TEST_HOOKS=1`. Required tools do not fall back to PATH when hooks are on. A cwd `tailscale` trap is present and was not invoked on the unknown-subcommand path. Fixture IPs and leak tokens are documentation-reserved and asserted absent from operator output. No real Tailscale, Mullvad, SSH, systemd, sudo, host, or diagnostic endpoint was contacted.

## Forbidden actions

No real networking other than the authorized `git ls-remote`. No SSH, sudo, systemd, host, provider, account, publication, deployment, AP mutation, or Meta inspection/write. No Git writes. No `.venv` reconstruction.

## Discrepancies, limitations, residual risks

None that falsify a fixed claim. Residual non-blocking tightness: the ten-minute documentation test window continues past the next heading; the NUC sequence still says cancel after a successful `verify` while the rollback-design owner lists the fuller gate set and is the section the sequence points to. These do not remove the corrected duration or the owner-map placement.

## Resolved Execution Issues / Near-Misses

An extra interpreter probe without unsetting `LD_LIBRARY_PATH` failed because the Cursor AppImage environment pollutes library paths. Authorized provenance and pytest commands already scrub those variables and succeeded. Cause: host session pollution, not candidate defect. Residual risk: none for this audit.

## Pre-Existing Failure Classification

none

## Smallest next step

Separately authorized publication of the exact accepted commit `20369a197daedac25569fef077400a9754cd1d5f`. That statement grants no publication, deployment, account, host, or live-network authority.

Authority expiry: all Worker 5 authority expired at this terminal report.