### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-cursor-worker-execution-boundary-convergence
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
```

**PASS**  
**implementation-PASS**  
**Logical-whole closure: not-closed**  
**Report justification:** `new-mutation`

```text
Authority expiry: all Worker 01 exchange 01 implementation authority expires
at this terminal report
```

## Result

Cursor Worker Python, NUC SSH, and remote sudo are now bound to the already-owned AP exec envelope, project SSH gate, and Cooperator-timestamp lifecycle. Ambient `.venv` / `poetry run` / reconstructed `gpgconf` are no longer ordinary Worker routes.

## Git

| | |
|---|---|
| Start commit | `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923` |
| End commit | `fc355d6e21d2f2781e0166906b453fa3fa91bdb7` |
| Branch | `fix/cursor-worker-execution-boundary` (local only) |
| Ancestry | direct descendant of `5abb2ad…` (`merge-base --is-ancestor` OK) |
| Local `main` | untouched (`bc15b608…`, still stale) |
| Push | none |

Public `refs/heads/main` remained `5abb2ad…`. AP pin remained `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. `ap.project.conf` was not changed.

## Changed files

| Path | Why necessary |
|---|---|
| `AGENTS.md` | High-priority Cursor/AppImage untrusted-boundary rule: AP exec, SSH gate, sudo lifecycle. Managed AP block unchanged. |
| `docs/WORKER_EXECUTION_CONTRACT.md` | Canonical AP exec **before** raw Python; encodings/SSH/sudo classification; raw `.venv`/`poetry` limited to a clean human development shell never rendered into Cursor Worker prompts. |
| `docs/AP_UPGRADE_OBSERVATIONS.md` | Exactly one untriaged ledger observation. Header/activation snapshot unchanged. |
| `scripts/operator/network/framenest_nuc_worker_gate.fish` | Smallest probe/attach extension of the **same** gate. |
| `tests/contract/test_operator_network_scripts.py` | Behavioral coverage for `--probe` and silent attach. |
| `docs/OPERATOR_NETWORK.md` | Cursor Worker SSH-gate / `gpgconf` / sanitization route (not a second stack). |
| `scripts/operator/network/README.md` | Documents `--probe`. |
| `tests/contract/test_worker_execution_contract.py` | Locks document order, classification owners, and ledger identity. |

## SSH gate: extended (not docs-only)

**Causal gap:** the gate already attached the agent for its own BatchMode SSH child, but it had no idempotent capability probe and a Cursor parent could not attach without reconstructing `gpgconf` or printing the socket.

**Smallest change:** `--probe` (sanitized `ssh-agent: ready` / `ssh-agent: absent`, no SSH, no socket print) plus shared `_attach_agent` used by probe and the existing SSH path. No parallel SSH stack. No GPG/SSH key, rc, Cursor, sudoers, or NUC edits.

This Cursor parent `--probe` returned `ssh-agent: ready` (exit 0) without printing a socket. Live BatchMode `true` was not required and was not run. No `sudo`.

## Python validation (AP exec)

Ambient Cursor classes observed and sanitized by AP (names only): `LD_LIBRARY_PATH`, `APPDIR`, `APPIMAGE`, plus `PATH` / prompt-related classes. No encodings crash this session; no Python inventory; no `.venv` repair.

Before mutation, static red: raw `.venv/bin/python` at lines 76/90/93/155 and `poetry run pytest` at line 148 of `docs/WORKER_EXECUTION_CONTRACT.md`, all **before** the AP exec section (line 231).

| Gate | Baseline | Result |
|---|---|---|
| `./.ap/ap project check` | `5abb2ad…` | PASS (CPython 3.13, encodings OK, `sanitized-v1`) |
| `--operation runtime-info` | `5abb2ad…` | PASS; `.venv/bin/python`; CPython 3.13.9; `framenest.__file__` under `src/` |
| `test-focus` | `5abb2ad…` then `fc355d6…` (execution only, not publication) | **59 passed** (`test_ap_project_contract.py`, `test_worker_execution_contract.py`, `test_operator_network_scripts.py`, `-q -p no:cacheprovider`) |

No full Python suite. No JS suite. No live deploy.

## Fish syntax

`fish -n scripts/operator/network/framenest_nuc_worker_gate.fish` — exit 0.

## Ledger

```text
Entry: consumer-declared-execution-and-capability-route-binding
Entry state: untriaged
```

Non-authorizing. AP does not become a Python, Poetry, GPG, SSH, sudo, Cursor, or deployment manager; exact commands remain consumer-owned.

## Classification owners now

| Rule | Owner |
|---|---|
| Raw encodings startup → ambient-route violation; rerun once via `./.ap/ap exec`; no inventory/rebuild | `docs/WORKER_EXECUTION_CONTRACT.md` (also pointed from `AGENTS.md`) |
| Canonical NUC SSH = project gate; `--probe`; do not reconstruct `gpgconf` | execution contract + `docs/OPERATOR_NETWORK.md` + the gate itself |
| `sudo -K` vs later password-required = expected lifecycle, independent of `SSH_AUTH_SOCK`; Workers must not `sudo -v` | execution contract + `AGENTS.md`; runbook not rewritten |

Secrets omitted: no socket paths, identity paths, env values, or sudoers contents.

## Smallest next step

Independent acceptance of branch `fix/cursor-worker-execution-boundary` at `fc355d6e21d2f2781e0166906b453fa3fa91bdb7` by a fresh Worker that did not implement this change. Not publication, push, or NUC mutation unless later granted.

## Near-Misses

- Docs-only SSH closeout was available; evidence showed a real probe/attach gap, so the same gate was extended instead of adding a second script.
- Optional live BatchMode `true` was not used; `--probe` from this parent plus synthetic attach tests were sufficient.
- Closed NUC-release whole was not reopened; checkout sat on that branch name at the authorized SHA and was left by creating a new branch.
- Owner untracked paths were preserved and not enumerated.

## Pre-Existing Failure Classification

- Local `main` stale versus public `main` (`bc15b608…` vs `5abb2ad…`): expected; left untouched.
- Envelope already expressed in `ap.project.conf`; defect was Worker-route hierarchy and missing SSH probe, not an envelope gap.
- Gate already discovered `gpgconf` for its SSH child; missing piece was parent-usable probe/attach without leaking the socket.