### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-nuc-push-workflow-and-companion-testing
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Status: PASS  
Phase-qualified result: implementation-PASS  
Logical-whole closure: not-closed  

Implementation PASS is non-independent. It is not acceptance, publication,
deployment, production acceptance, or ORCHESTRATOR closure.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; directly observed client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Implementation writes available | directly observed |
| Repository | Isolated worktree from exact baseline | Worktree `/home/agile/Projects/framenest-worktrees/framenest-nuc-push-workflow-and-companion-testing-w2`; branch `docs/nuc-dev-test-runbook-annex`; start HEAD `070681856bc6f14e12da52717dbccefa160554af` | directly observed |
| Canonical checkout | Untouched | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; HEAD still `070681856bc6f14e12da52717dbccefa160554af`; tracked-clean | directly observed |
| AP pin | Superproject gitlink | Worktree `.ap` HEAD `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; see Validation | directly observed |
| Network, NUC, SSH, sudo, secrets | None | Unused | directly observed |
| Browser / provider calls | None | Unused | directly observed |
| Git | Local commit in isolated worktree; no push | One commit `91410fe063d9907304cff4550f61d403880a2eeb`; push not performed | directly observed |
| Independence | Not required | Same session implemented the candidate; no self-acceptance | directly observed |

Capability, permission, and client identity did not expand task authority.

Start commit: `070681856bc6f14e12da52717dbccefa160554af`  
End commit: `91410fe063d9907304cff4550f61d403880a2eeb`  
Parent of end commit: `070681856bc6f14e12da52717dbccefa160554af`  
Branch: `docs/nuc-dev-test-runbook-annex`  
End worktree: clean  
Push: not authorized; not performed  

Do not treat `91410fe` as live NUC or public `main`.

## Changed files and purpose

Exactly eight FrameNest repository paths in the one authorized commit:

1. `README.md` — Status section only. Present-tense production-server divergence replaced with development-test NUC routinely targeting the exact public `main` SHA and `framenest-release status` as runtime readback. Dated `aec2f009…` / schema `0028` history retained. Companion review Save does not publish; Apply writes metadata only; administrator `PUT /api/admin/media/{media_id}/content-publication` (including unpublish) is the sole publication path. Local-only `public_published_uds` composition and workspace rollout successors recorded as implemented; public bind/TLS/Funnel remain unshipped.
2. `SERVER.md` — NUC Role present tense: authoritative serving for the disposable development-test instance; exact-main refresh and `framenest-release status` readback. Dated SHA paragraph retained. `owner-authoritative production release` removed from present tense.
3. `docs/INFOSEC.md` — present-tense “serves production over Tailscale” changed to development-test workspace access. Audited checkout SHA `3a21405e…` and findings retained as historical evidence.
4. `docs/ACCEPTANCE_DUAL_AUDIENCE.md` — Part B honesty banner gates on tested public-`main` SHA equal to live `framenest-release status` active release; blocked runs report `BLOCKED: NUC not at tested SHA`. B3 states Apply acceptance is deterministic by owner decision (2026-08-26) and that no rendered Apply entry exists for analyzed rows.
5. `deploy/ubuntu/README.md` — routine-update wording: standing ADR-0075 authority for exact-main refresh; non-routine host work remains separately authorized; schema jumps stop at exit 13 and continue through the runbook section 5 annex, not a fifth helper command.
6. `docs/UBUNTU_NUC_DEPLOYMENT.md` — Status role notes plus section 5. Removed `--chdir=/opt/framenest/current` migrate example. Added exit-13 annex: publish `/opt/framenest/releases/<T>` before checkpoint/cutover; pre-cleanup probes; exact lock cleanup of `ap.tar`, `framenest_release.py`, `superproject.tar` then empty `/run/framenest-release-deploy`; migrate from the new tree; post-migration `current_revision=head_revision=0033`; cutover via `rollback --release <T> --yes`; final `status`; terminal Cooperator `sudo -K`; post-migration cutover failure requires explicit triage.
7. `tests/contract/test_nuc_release_docs.py` — parity assertions for README/SERVER/INFOSEC/acceptance/deploy-README facts and the annex.
8. `tests/contract/test_nuc_operator_runbook.py` — active-tree service-account examples stay on `/opt/framenest/current`; schema-jump continuation examples use `/opt/framenest/releases/<T>`; migrate is forbidden under `/current`.

Meta report (this file; not in the FrameNest commit):

- `/home/agile/meta/projects/framenest/05/00-framenest-nuc-push-workflow-and-companion-testing/02_report_01.md`

No ADR bodies, `SECURITY.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, product code, `deploy/ubuntu/framenest_release.py`, or `docs/X_COMPANION.md` were changed.

## Validation

- Isolated worktree created from exact baseline `070681856bc6f14e12da52717dbccefa160554af`; canonical checkout remained on `feat/x-meme-browser-companion` at that SHA, tracked-clean.
- `git diff --cached --check` on the staged eight-file set: clean.
- Focused link review: new/used targets `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md` and `docs/adr/0075-nuc-development-test-target-and-routine-release-refresh.md` exist; deploy README relative link `../../docs/adr/0075-…` resolves. Runbook contains no `/home/`, `chmod`, `chown`, or `/opt/framenest/current/.venv/bin/framenest-db migrate`. The only documented migrate command is `/opt/framenest/releases/<T>/.venv/bin/framenest-db migrate`.
- Helper contract unchanged by inspection of the unedited engine: still four public commands; `framenest-db migrate` is absent from `framenest_release.py`; `EXIT_MIGRATION_REQUIRED = 13` still occurs after atomic publish and before checkpoint/cutover.

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 070681856bc6f14e12da52717dbccefa160554af
```

Outcome: `ap project check --baseline: PASS` (also `WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH`; CPython 3.13).

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-nuc-push-workflow-and-companion-testing-w2 \
  --baseline 070681856bc6f14e12da52717dbccefa160554af
```

Outcome: FAIL `declared CPython executable does not exist`. Classification: expected isolated-worktree environment limitation (no worktree `.venv`). Not repaired. Canonical `.venv` was not copied, symlinked, or reconstructed.

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 070681856bc6f14e12da52717dbccefa160554af \
  --operation runtime-info
```

Outcome: PASS. Provenance: `/home/agile/Projects/framenest/.venv/bin/python`; CPython 3.13.9; `framenest.__file__` = `/home/agile/Projects/framenest/src/framenest/__init__.py`. Documentation tests do not import product code for their assertions; they read files from `Path(__file__).resolve().parents[2]`.

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 070681856bc6f14e12da52717dbccefa160554af \
  --operation test-focus -- \
  /home/agile/Projects/framenest-worktrees/framenest-nuc-push-workflow-and-companion-testing-w2/tests/contract/test_nuc_release_docs.py \
  /home/agile/Projects/framenest-worktrees/framenest-nuc-push-workflow-and-companion-testing-w2/tests/contract/test_nuc_operator_runbook.py \
  -q -p no:cacheprovider
```

Outcome after the wrapping fix below: **35 passed in 0.10s**. Exact-source for these suites is the worktree test paths (`__file__` → worktree root). `--root` remains the canonical checkout solely because the worktree has no declared interpreter.

## Git result

One local commit on `docs/nuc-dev-test-runbook-annex` in the isolated worktree:

`91410fe063d9907304cff4550f61d403880a2eeb`

No fetch, merge, rebase, reset, tag, or push. Canonical checkout was not switched, committed, or dirtied.

## Boundary-compliance confirmation

- Allowlist: exactly the eight named paths.
- `framenest-release` still has exactly four public commands; engine untouched and migration-free; no fifth helper command.
- No global replacement of “production”, `/opt/framenest/current`, or historical SHAs. Dated `aec2f009…` / `0028` sentences retained. Active-tree operator examples still use `/opt/framenest/current`.
- No NUC access, SSH, sudo, wrapper execution, provider calls, browser use, or publication.
- Closed logical wholes were not reopened (`docs/X_COMPANION.md`, companion product code, ADR bodies).

## Deviations, risks, or missing evidence

Deviation (environment, not candidate): isolated worktree has no `.venv`. `ap project check --root <worktree>` therefore cannot pass. Tests were run through the canonical envelope with absolute worktree test paths so documentation assertions read candidate files. A Worker must not treat `runtime-info` provenance (`…/framenest/src/…`) as proof of candidate product code; this task did not change product code.

Residual editorial debt outside this allowlist (not acted on):

- Runbook `## Current Target` still says `personal production server`.
- Routine section still describes the helper as same-schema-only internally (accurate for the engine; the annex is the operator continuation).
- Later README sections still use “personal production server” (Status-only edit authority).
- `SECURITY.md` left unchanged as required.

No deviation request. None of the residual debt blocked this slice.

Resolved Execution Issues / Near-Misses: first focused run failed one assertion because “Never improvise a downgrade or catalog restore” wraps across two runbook lines. The test now flattens whitespace. Residual risk: none; the annex wording is unchanged.

Pre-Existing Failure Classification: none.

## Smallest next step

Orchestrator verifies `91410fe063d9907304cff4550f61d403880a2eeb` against repository evidence, then handles publication to public `main` and the NUC refresh (expected schema jump `0032 → 0033`) under standing ADR-0075 authority. This Worker has no follow-on authority.

Report justification: new-mutation

Authority expiry: this implementation authority expires with submission of this terminal report. No further commits, revisions, publication, deployment, push, NUC access, or logical-whole closure are authorized.
