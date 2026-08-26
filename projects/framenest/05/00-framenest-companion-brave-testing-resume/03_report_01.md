### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 03
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-HISTIMPL-01
```

Status: **PASS**  
Phase-qualified result: `implementation-PASS`  
Logical-whole closure: not-closed  

Implementation PASS is non-independent. It is not acceptance, publication,
deployment, production acceptance, NUC refresh, rendered re-test, or
ORCHESTRATOR closure.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Implementation writes available (Plan Mode off) | directly observed |
| Permission mode | not named | unknown/not observably exposed; allowlisted writes and one local commit succeeded | unknown |
| Context pressure | not named | Elevated after mid-task restoration; remaining work completed from repository evidence | inferred |
| Repository | Isolated worktree from exact baseline `91410fe…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3`; branch `feat/companion-history-r1-r3prime`; start HEAD `91410fe063d9907304cff4550f61d403880a2eeb` | directly observed |
| Canonical checkout | Untouched | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; HEAD still `91410fe063d9907304cff4550f61d403880a2eeb`; tracked-clean | directly observed |
| AP pin | Superproject gitlink `9c5cc44…` | Worktree `.ap` HEAD `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; see Validation (worktree `--root` topology classified) | directly observed |
| Network, NUC, SSH, sudo, secrets | None | Unused | directly observed |
| Browser / provider calls | None | Unused | directly observed |
| Git | One local commit in isolated worktree; no push | Commit `977a7af80afed16745adb0ef8e939555e5e21cce`; push not performed | directly observed |
| Independence | Not required | Same session implemented the candidate; no self-acceptance | directly observed |

Capability, permission, client identity, and context pressure did not expand
task authority.

Start commit: `91410fe063d9907304cff4550f61d403880a2eeb`  
End commit: `977a7af80afed16745adb0ef8e939555e5e21cce`  
Parent of end commit: `91410fe063d9907304cff4550f61d403880a2eeb`  
Branch: `feat/companion-history-r1-r3prime`  
End worktree: clean  
Push: not authorized; not performed  

Do not treat `977a7af80afed16745adb0ef8e939555e5e21cce` as live NUC or public
`main`.

## Changed files and purpose

Exactly 21 FrameNest repository paths in the one authorized commit:

1. `extension/ui/sidebar.js` — R1: every history row `open_details` / hosted Details; analyzed click POSTs opened without gating the iframe; pending never POSTs opened; ordinary compact is newest five of any state.
2. `extension/background/service_worker.js` — Identity-based history routing (inbox vs hardcoded `GET /api/companion/own-history`); ordinary badge uses own-history `limit=1`; `fetchJson` path override; `history_source` on the list result.
3. `src/framenest/adapters/api/companion_review_api.py` — `GET /api/companion/own-history` (`x.request`); opened identity `x.request` with `require_owner` when the caller lacks `media.workflow.read`.
4. `src/framenest/adapters/api/tailscale_ingress.py` — Own-history GET `x.request`, not `companion_mutation`; opened capability `x.request`; still exactly four mutation routes.
5. `src/framenest/application/companion_review.py` — `ListCompanionReviewInbox.execute(..., own_history=)` dispatches via `getattr(list_own_history)`; `MarkCompanionReviewOpened.execute(..., require_owner=)` passes the repository kwarg only when true.
6. `src/framenest/infrastructure/persistence/companion_review_repository.py` — Analyzed-only admin inbox; `list_own_history`; own-analyzed `unopened_count`; `mark_opened(..., require_owner=)` ownership 404.
7. `src/framenest/adapters/api/web/app.js` — Hosted Details hide Analyze by AI and Load AI suggestion; standalone unchanged.
8. `docs/X_COMPANION.md` — History section rewrite (hosted click, analyzed-only admin inbox, ordinary own-history, no 0034).
9. `docs/adr/0076-companion-history-hosted-click-admin-analyzed-inbox-and-ordinary-own-history.md` — New successor ADR.
10. `docs/adr/README.md` — 0076 index row; 0067/0073 successor notes only (bodies untouched).
11. `SPEC.md`, `PRODUCT.md`, `README.md` — Surgical present-tense R1–R3′ sentences.
12. Tests: `tests/companion_review_extension.test.js`, `tests/companion_web_bridge.test.js`, `tests/tailscale_identity_frontend.test.js`, `tests/contract/test_companion_review_api.py`, `tests/contract/test_adr_0073.py`, `tests/contract/test_x_route_policy.py`, `tests/contract/test_tailscale_ingress_security.py`, `tests/unit/infrastructure/persistence/test_companion_review_repository.py`.

Not modified (forbidden / unused): ADR-0073 and ADR-0067 bodies, `SECURITY.md`,
any `alembic_environment/versions/` file, `application.py`,
`application/ports/companion_review_repository.py`, `extension/shared/messages.js`,
publication/upload APIs, `deploy/ubuntu/*`, `.venv`, dependency manifests.

## Validation

Worktree `.ap` pin after `git submodule update --init .ap` (worktree-local
checkout only; gitlink unchanged): `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3 \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb
```

Outcome: FAIL `declared CPython executable does not exist`. Classification:
isolated-worktree environment limitation (no worktree `.venv`). Not repaired.
Canonical `.venv` was not copied, symlinked, or reconstructed.

```text
./.ap/ap exec --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3 \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb --operation runtime-info
```

Outcome: same FAIL. Same classification.

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb
```

Outcome: `ap project check --baseline: PASS`. WARN sanitized inherited
environment classes: `LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT
PROMPT_COMMAND APPDIR APPIMAGE PATH`. CPython 3.13.

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb --operation runtime-info
```

Outcome: PASS. Interpreter `/home/agile/Projects/framenest/.venv/bin/python`;
CPython 3.13.9; `framenest.__file__` =
`/home/agile/Projects/framenest/src/framenest/__init__.py` (canonical source;
not used as candidate evidence).

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb \
  --operation test-focus -- \
  --rootdir /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3 \
  -o pythonpath=/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/src \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_companion_review_api.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_adr_0073.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_x_route_policy.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_tailscale_ingress_security.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/unit/infrastructure/persistence/test_companion_review_repository.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_analysis_proposal.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/contract/test_automatic_analysis_privacy_contract.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/integration/persistence/test_analysis_proposal_migration.py \
  /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3/tests/integration/test_persistence_migrations.py \
  -q -p no:cacheprovider
```

Outcome: **151 passed in 71.50s**. Declared AP envelope (canonical `--root`
because the worktree has no launch path). Trailing pytest `pythonpath` is the
candidate `src/` so `import framenest` cannot be the baseline tree: baseline
`91410fe…` has no `list_own_history`, and those tests passed. No `.venv`
reconstruction.

```text
node --test tests/x_companion_extension.test.js tests/companion_review_extension.test.js tests/companion_web_bridge.test.js tests/tailscale_identity_frontend.test.js
```

From the isolated worktree root. Outcome: **107 passed**, 0 failed.

Schema files under
`src/framenest/infrastructure/persistence/alembic_environment/versions/`:
`0030`–`0033` only. No `0034_*.py`. `git diff --check` clean.

## Per-rule confirmation

| Rule | Owning tests |
|---|---|
| R1 hosted click | `tests/companion_review_extension.test.js` (`analyzed history click posts opened then open_details; pending is hosted without opened`; compact/All); `tests/companion_web_bridge.test.js` (`open_details` / `storedOrigin` / never `*`); hosted hide Analyze + Load AI suggestion in that file and `tests/tailscale_identity_frontend.test.js` |
| R2 admin analyzed-only inbox | `test_admin_list_and_detail_are_no_store_and_ordinary_is_forbidden` (admin items `[GENERIC]` only); `test_mixed_inbox_includes_only_owned_pending_and_analyzed_wins` (PENDING absent from `list_inbox`, present on admin `list_own_history`); `test_suggestion_ready_lists_without_v1_schema_and_survives_decode_failure`; `test_corrupt_result_json_does_not_drop_inbox_page` |
| R3′ listing | `test_admin_list_and_detail_are_no_store_and_ordinary_is_forbidden` (ordinary own-history 200 empty; inbox/detail 403); `test_own_history_opened_alice_bob_admin_isolation`; `ordinary own-history compact is newest five of any state`; `ordinary badge refresh uses own-history limit=1 and does not call inbox` |
| R3′ opened + Alice/Bob/admin | `test_own_history_opened_alice_bob_admin_isolation`; `test_own_history_opened_isolation_does_not_use_global_unopened_count`; `test_opened_and_apply_contracts` (ordinary opened on admin GENERIC → 404 `MEDIA_NOT_FOUND`; apply still 403); retained `test_actor_opened_rows_are_isolated` |
| Ingress / four mutations | `test_only_companion_mutations_are_companion_flagged` (opened capability `x.request`; own-history not flagged; exactly four `companion_mutation`); `tests/contract/test_tailscale_ingress_security.py` (opened still allowlist+header fail-closed; GET own-history 200 with empty allowlist) |
| No 0034 / head 0033 | `test_current_schema_head_is_0033`; `tests/integration/test_persistence_migrations.py`; `tests/integration/persistence/test_analysis_proposal_migration.py`; `test_adr_0076_is_accepted_and_indexed` |
| Retention | `test_adr_0073_is_accepted_and_indexed` (body unedited); analysis-proposal and automatic-analysis privacy contracts; apply never publishes / movie 409 / empty-allowlist mutations in the ingress and API suites above |

## Security-invariant confirmation

- Exactly four `companion_mutation` routes (submit, retry, same opened, apply).
- Opened allowlist + `X-FrameNest-Request: 1` + Origin rules unchanged.
- Empty-allowlist mutations remain fail-closed; GET own-history is not a mutation.
- Ordinary gains only `GET /api/companion/own-history` and opened-POST on owned items (uniform 404 otherwise).
- Inbox list/detail/apply remain admin-only 403 for ordinary.
- Apply never publishes; administrator PUT remains sole writer including unpublish.
- Movie exclusion retained.
- Schema head remains `0033`; no migration `0034`.
- Header rules and empty-allowlist fail-closed behavior unchanged for the four mutation routes.

## Sanitization compliance

No credentials, tokens, cookies, private keys, private media filenames,
host-specific identifiers, disk serials, SSH fingerprints, or private network
values in the candidate diff or this report. Synthetic UUIDs and example logins
only.

## Resolved Execution Issues / Near-Misses

1. Isolated-worktree `ap project check` / `ap exec --root <worktree>` cannot
   launch relative `.venv/bin/python`. Classified as environment limitation.
   Not repaired. Python evidence used the declared `ap exec` envelope with
   canonical `--root` plus trailing pytest `pythonpath` / `--rootdir` on the
   candidate worktree (see Validation).
2. Two Node pagination tests failed once (`fetchCalls.length` 3 !== 2) after
   `reviewInbox()` started with `GET /api/identity/me`. Fixed in
   `tests/companion_review_extension.test.js` by counting only
   `/api/companion/review-inbox` list calls. Re-run: 107 passed.
3. Worktree `.ap/` was empty until `git submodule update --init .ap` (pin
   `9c5cc44…`). Superproject gitlink unchanged. Python exec used canonical
   `/home/agile/Projects/framenest/.ap/ap`.
4. Port and `messages.js` were not allowlisted. Own-history is dispatched
   through the existing `ListCompanionReviewInbox` use case (`getattr
   list_own_history`). Opened `require_owner` is omitted on the admin call so
   Protocol fakes without that kwarg still type-check. Service worker uses a
   hardcoded `/api/companion/own-history` path override instead of `pathFor`.

## Pre-Existing Failure Classification

None. The Node pagination failures were introduced by this session’s identity
prefetch and were corrected on the test allowlist. The worktree AP `.venv` miss
is the known isolated-worktree topology limitation, not a candidate defect.

## Deviations, risks, or missing evidence

- Click order is hosted `openHostedDetails` first, then POST opened (iframe is
  not gated). The plan’s test-title phrase “opened then open_details” is
  satisfied as both occurring; source order matches “do not gate on opened
  HTTP” (`openedIndex > hostedIndex`).
- Two repository tests retain historical names
  (`test_mixed_inbox_includes_only_owned_pending_and_analyzed_wins`,
  `test_mixed_inbox_includes_omitted_category_owned_general_saves`); bodies
  assert analyzed-only admin inbox plus own-history pending.
- Exact-source Python provenance is via pytest `pythonpath` under `ap exec`,
  not via `ap exec --root <worktree>` (unusable without unauthorized `.venv`
  topology).
- Rendered Brave companion and NUC refresh were out of authority.

## One smallest next step

ORCHESTRATOR verifies this candidate against repository evidence, then
sequences Cooperator publication grant, routine NUC `framenest-release` refresh
to the published SHA, and rendered admin/ordinary companion re-test.

Report justification: new-mutation

Authority expiry: all Worker 03 / exchange 01 authority expired at this
terminal report. No follow-on implementation, Git write, push, publication,
NUC access, provider call, or logical-whole closure is authorized.
