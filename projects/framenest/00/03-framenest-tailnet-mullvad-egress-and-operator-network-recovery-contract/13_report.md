### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract
Worker session ordinal: 13
Worker exchange ordinal: 01

Standard terminal status: PASS
Phase-qualified result: publication-PASS
Acceptance disposition: acceptance-PASS
Publication disposition: publication-PASS
Result artifact or commit: a23b4bc786357da3591a4f75087b7e8a3d50d341
Logical-whole closure: not-closed
Report justification: new-mutation

## Freshness, Native Plan Mode, and independence

This was a genuinely fresh Worker session. This instance did not implement candidate `a23b4bc786357da3591a4f75087b7e8a3d50d341`, did not participate in Worker 12, had not previously inspected this candidate, and had not received an earlier Worker 13 prompt.

Native planning mode: requested `not-used`; observed disabled/absent (Agent/implementation surface). No Plan-mode work was performed.

Independence: required-fresh-independent; satisfied. Evidence posture is independent of the implementing Worker.

Internal delegation: not-used. Worker topology: single-active.

Requested reasoning: High. Observed model: Cursor Grok 4.6; identity is not independently attested beyond client selection.

## Candidate / public identities and cleanliness

Worktree: `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2`
Origin: `https://github.com/cisarik/framenest.git`
Branch: `feat/tailnet-mullvad-egress-recovery-contract`
HEAD: `a23b4bc786357da3591a4f75087b7e8a3d50d341`
Tree: `a1ea29c5fa7e6878670b243ef34b8b0b31084829`
Parent: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
Subject: `fix: reconcile selected Mullvad status`
AP gitlink and `.ap` HEAD: `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`
Commit count parent..candidate: `1`
Worktree and index: clean before and after; untracked files: none
This Worker changed no repository paths.

Public `main` before publication: `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`
Public `main` after publication and final readback: `a23b4bc786357da3591a4f75087b7e8a3d50d341`

## Recovery classification

Classification unit type: worktree
Classification unit identity: `/home/agile/Projects/framenest-worktrees/framenest-tailnet-mullvad-egress-w2` at `a23b4bc786357da3591a4f75087b7e8a3d50d341`
Classification accepted-continuation: applicable for fresh acceptance of the exact correction
Classification unrelated-owner-work: not-applicable; clean
Classification stale-clone: not-applicable; candidate descends directly from public main
Classification unpublished-candidate: applicable before the authorized push
Classification unexplained-divergence: not-applicable
Primary recovery classification: accepted-continuation
Secondary recovery classifications: unpublished-candidate
Immediate recovery action: independently accept first; publish only after all acceptance gates pass
Publication status: unpublished at classification; published after acceptance
Mutation before classification: none
Destructive recovery operation: none

## Exact diff and modes

Parent-to-candidate `name-status` is exactly:

```text
M	docs/OPERATOR_NETWORK.md
M	scripts/operator/network/framenest_mullvad_egress.sh
M	tests/contract/test_operator_network_scripts.py
```

`git diff --check` clean. `git diff --summary` empty (no mode/create/delete). Bash script mode remains `100755` on parent and candidate (`cdcfb15f48d49eee83ca74372e2726eaecd5d21a` on candidate). Fish wrapper and SSH gate blobs are unchanged. `.ap` gitlink unchanged. No other path changed.

The Bash delta is a two-line insertion in `print_status`: after the explicit readable `.mullvad.ts.net` branch, a successful non-empty opaque/non-DNS `tailscale get` value is classified `mullvad:<sanitized-selected-peer-dns>` only when `SELECTED_KIND=mullvad` and `SELECTED_MULLVAD_DNS` is non-empty; otherwise it remains `non-mullvad`. Empty, colon/`unsafe-non-explicit`, explicit-suffix, unreadable/unsupported-get JSON fallback, mutation, and `verify` paths are unchanged.

Parent unconditionally classified that opaque readable branch as `non-mullvad`. The positive regression reaches that same branch. The candidate adds selected-Mullvad JSON reconciliation. The negative control keeps a selected non-Mullvad peer as `non-mullvad` even when other Mullvad options exist.

## Acceptance record

```text
Acceptance candidate: a23b4bc786357da3591a4f75087b7e8a3d50d341
Acceptance owner map: section 10
Acceptance allowlist: section 9
Acceptance risk claims: SC-01 through SC-09
Acceptance control matrix: section 12
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none
```

## SC-01 through SC-09

| Claim | Result |
|---|---|
| SC-01 Candidate identity | PASS |
| SC-02 Positive opaque reconciliation | PASS |
| SC-03 Negative reconciliation | PASS |
| SC-04 Existing classifications | PASS |
| SC-05 Privacy | PASS |
| SC-06 Mutation invariance | PASS |
| SC-07 Test authenticity | PASS |
| SC-08 Documentation | PASS |
| SC-09 Live read-only classification | PASS |

SC-02: JSON extractor marks a selected peer Mullvad when `ExitNode` is true and DNS ends in `.mullvad.ts.net`; the fixture peer also has `ExitNodeOption=true`. Output uses sanitized selected-peer DNS, never the opaque preference.

SC-03: opaque preference plus selected non-Mullvad peer remains `non-mullvad`; available Mullvad peers alone do not upgrade.

SC-04: empty, explicit Mullvad suffix, unsafe `*:`, selected non-Mullvad, and unreadable/unsupported-get fallback branches are unmodified versus parent; existing tests still cover fallback and mutation guards.

SC-06: `enable`, `disable`, `verify`, `recover`, node validation, preflight, `tailscale set` arguments, LAN-access false, trusted executable resolution, temp cleanup, and first-error behavior are outside the two-line status insertion.

## Positive and negative controls

Positive: PASS — explicit readable Mullvad DNS branch unchanged; opaque readable preference plus selected Mullvad peer (new test); unreadable/unsupported preference plus selected Mullvad peer (existing fallback test); NUC LAN false (live); live sanitized Mullvad classification on both devices.

Negative: PASS — opaque plus selected non-Mullvad; opaque without selected Mullvad peer remains the else/`non-mullvad` path; empty preference unchanged; unsafe non-explicit unchanged; no raw opaque value in synthetic or live captured operator output; no raw JSON or fixture secrets; status invokes no mutation; test hooks use pytest-managed absolute fakes plus a cwd trap; no mutation-subcommand change; no live mutation and no public egress diagnostic.

## Syntax, provenance, and tests

Syntax: PASS (`bash -n` on the Bash implementation; `fish -n` on the unchanged Fish wrapper and SSH gate).

Provenance: exact. Canonical interpreter `/home/agile/Projects/framenest/.venv/bin/python` with candidate `PYTHONPATH` imported `.../framenest-tailnet-mullvad-egress-w2/src/framenest/__init__.py`. No `.venv` reconstruction.

Tests: `79 passed`, exit 0, `-p no:cacheprovider`, AppImage/`LD_*` unset.

## Synthetic-isolation evidence

Harness inspected before execution. Tests set `FRAMENEST_NETWORK_TEST_HOOKS=1` and absolute fake `tailscale`/`curl`/`ssh`/`gpgconf`/`mullvad` under pytest `tmp_path`. Production trusted-PATH lookup is skipped. Unexpected fake `tailscale` invocations fail closed. A cwd `tailscale` trap is installed and unused. Status tests assert empty `set` logs and no `up`/`down`/`login`/`logout`. Fake curl bodies are local files; status does not contact the network. Opaque token `fnOpaqueSelectedPref` is asserted absent from combined output.

## Sanitized live status

Private capture used `/tmp/framenest-w13-final.*` only. No host mutation. No `enable`/`disable`/`verify`/`recover`, curl, sudo, systemctl, or systemd-run.

ahw (`framenest_mullvad_egress.fish status`, exit 0): backend Running; client-get unsupported; exit-node class Mullvad; LAN-access unavailable-without-tailscale-get (no usable `get`; not treated as LAN false); Mullvad nodes available; self-advertisement no; standalone Mullvad disconnected. No braces, IPv4, or node-key material in captured operator output.

NUC (published Fish SSH gate; remote `/usr/bin/bash -s -- status`; stdin candidate Bash; exit 0): backend Running; client-get supported; exit-node class Mullvad; LAN access false; Mullvad nodes available; self-advertisement no; standalone Mullvad absent. No braces, IPv4, or node-key material in captured operator output.

Exact nodes, opaque preferences, hostnames, suffixes, IPs, login, and raw output are not reported.

## Acceptance decision before publication

```text
SC-01 through SC-09 = PASS
positive and negative controls = PASS
syntax = PASS
79 passed
provenance = exact
live ahw status = Mullvad
live NUC status = Mullvad
NUC LAN access = false
candidate worktree = clean
public main = parent
private evidence contained
Acceptance disposition: acceptance-PASS
```

Publication stage gate passed. No candidate correction was made or attempted.

## Route and push

Pre-push recheck: clean worktree/index; HEAD/tree/parent/AP pin unchanged; public `main` still `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`.

Route A. Exactly one ordinary non-force push:

```text
git push --porcelain origin a23b4bc786357da3591a4f75087b7e8a3d50d341:refs/heads/main
```

Result: porcelain fast-forward `4add009..a23b4bc`, `Done`, exit 0. Push attempts: 1. No retry. No fetch/pull/merge/rebase/force/switch/checkout/reset/clean/add/commit/tag, and no other ref push. Feature branch was not published.

## Public readback and disposable verification

`git ls-remote origin refs/heads/main` = `a23b4bc786357da3591a4f75087b7e8a3d50d341`.

Disposable `/tmp/framenest-w13-public.*`: `git init` then depth-2 fetch of `refs/heads/main` from `https://github.com/cisarik/framenest.git` (not into the candidate worktree).

Fetched object facts: commit `a23b4bc786357da3591a4f75087b7e8a3d50d341`; tree `a1ea29c5fa7e6878670b243ef34b8b0b31084829`; parent `4add009e1f89fcc05b9e8bc306d6ecc8e568547b`; subject `fix: reconcile selected Mullvad status`; count above parent `1`; changed paths the exact three-path allowlist; diff check clean; Bash mode `100755`; AP pin `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`.

## Cleanup

Both exact roots matched `/tmp/framenest-w13-final.*` and `/tmp/framenest-w13-public.*`, were removed, and are absent. Two Worker-created path-pointer files under `/tmp` were also removed. Candidate worktree remains clean. Final HEAD and public `main` both equal `a23b4bc786357da3591a4f75087b7e8a3d50d341`.

## Host mutation / public egress diagnostic

None. Neither exit node nor LAN access was changed. `verify` was not run. Funnel/Serve/systemd/firewall/DNS/routes were not touched. FrameNest was not deployed. Credentials and private-key contents were not inspected (identity path existence only). AP and Meta were not mutated. Logical whole is not closed.

## Deviations and residual risks

No acceptance or publication deviation.

Residual risks: `status` classification is not a public-egress proof; `verify` remains the owner of actual Mullvad-egress classification. Readable opaque `get` representations can still exist; they must keep being reconciled from sanitized selected-peer JSON and must not be emitted. ahw still lacks a usable `tailscale get`, so its LAN line remains `unavailable-without-tailscale-get`. This slice does not claim reboot persistence, Serve/Funnel, or logical-whole closure.

Meta archival of `13_acceptance-publication.md` / `13_report.md` was not performed; that remains a separately authorized archive workflow.

## Resolved Execution Issues / Near-Misses

Issue: two extra `/tmp` pointer files were used to retain audit/verify root paths.
Cause: `mktemp` identities were not otherwise kept in the report.
Resolution: pointers were removed with the authorized roots; no private operator output left the audit root.
Residual risk: none material.

## Pre-Existing Failure Classification: none

## Smallest next step

Fresh ORCHESTRATOR restoration and deterministic closure. No additional Worker belongs to this logical whole.

## External trace

```text
External trace disposition: configured
Trace discovery: projects/framenest/00/03-framenest-tailnet-mullvad-egress-and-operator-network-recovery-contract/
Trace authority: historical-evidence-only
Trace archival owner: separately authorized archive workflow after the report exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

```text
all Worker 13 authority expired at this terminal report
```