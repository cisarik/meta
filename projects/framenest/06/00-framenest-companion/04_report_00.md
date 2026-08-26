### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 04
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-HISTACC-01
```

Status: **PASS**  
Phase-qualified result: `acceptance-PASS`  
Logical-whole closure: not-closed  

This session did not implement `977a7af80afed16745adb0ef8e939555e5e21cce`.
Independence conflict: none. Prior session-03 authority is treated as expired;
`03_report_01.md` was verified as a claim against the candidate object, not
believed.

Implementation-PASS is not emitted. Publication, NUC refresh, rendered re-test,
and logical-whole closure remain inactive.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; only authorized report + temporary probe writes | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Context pressure | not named | unknown/not observably exposed | unknown |
| Repository | Fresh isolated checkout of `977a7af…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w4`; detached `977a7af…` | directly observed |
| Canonical checkout | Read-only at public main | `/home/agile/Projects/framenest`; `feat/x-meme-browser-companion`; HEAD `91410fe063d9907304cff4550f61d403880a2eeb`; tracked-clean after worktree add and after tests | directly observed |
| Session-03 worktree | Untouched | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w3` still `977a7af…` tracked-clean | directly observed |
| AP pin | Superproject gitlink `9c5cc44…` | Canonical and w4 gitlink + `.ap` HEAD `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; worktree `--root` miss classified; canonical `--root` plus pytest `pythonpath` / `--rootdir` | directly observed |
| Network, NUC, SSH, sudo, secrets | Credential-free `ls-remote` only | Two public `main` refs; no NUC/SSH/sudo/providers | directly observed |
| Browser / provider calls | None | Unused | directly observed |
| Git | Worktree add + worktree-local `.ap` init only | No commits, no `git add`, no push | directly observed |
| Independence | Required fresh independent | This session did not author `977a7af…` | directly observed |

Capability, permission, and client identity did not expand task authority.

## Fresh checkout and provenance

| Fact | Observed |
|---|---|
| Fresh-checkout path | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w4` |
| Candidate SHA | `977a7af80afed16745adb0ef8e939555e5e21cce` |
| Parent SHA | `91410fe063d9907304cff4550f61d403880a2eeb` |
| `merge-base --is-ancestor` parent→candidate | succeeds |
| Canonical after worktree add | still `91410fe…` on `feat/x-meme-browser-companion`, tracked-clean |
| AP pin (gitlink and w4 `.ap` HEAD) | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Public `refs/heads/main` (`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`) | `91410fe063d9907304cff4550f61d403880a2eeb` |
| Public `cisarik/ap` `main` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (same as pin) |
| Session-03 worktree | untouched at `977a7af…`, tracked-clean |
| w4 porcelain after submodule init | empty (worktree-local `.ap` checkout only) |

## Diff path set

Exactly 21 paths vs parent `91410fe…` (`+1128 / −177`):

1. `PRODUCT.md`
2. `README.md`
3. `SPEC.md`
4. `docs/X_COMPANION.md`
5. `docs/adr/0076-companion-history-hosted-click-admin-analyzed-inbox-and-ordinary-own-history.md`
6. `docs/adr/README.md`
7. `extension/background/service_worker.js`
8. `extension/ui/sidebar.js`
9. `src/framenest/adapters/api/companion_review_api.py`
10. `src/framenest/adapters/api/tailscale_ingress.py`
11. `src/framenest/adapters/api/web/app.js`
12. `src/framenest/application/companion_review.py`
13. `src/framenest/infrastructure/persistence/companion_review_repository.py`
14. `tests/companion_review_extension.test.js`
15. `tests/companion_web_bridge.test.js`
16. `tests/contract/test_adr_0073.py`
17. `tests/contract/test_companion_review_api.py`
18. `tests/contract/test_tailscale_ingress_security.py`
19. `tests/contract/test_x_route_policy.py`
20. `tests/tailscale_identity_frontend.test.js`
21. `tests/unit/infrastructure/persistence/test_companion_review_repository.py`

Forbidden-path absence (empty diffs vs parent):

- no `alembic_environment/versions/0034*` (versions dir is `0001`–`0033` plus `__init__.py`)
- no ADR-0073 body edit
- no ADR-0067 body edit
- no `SECURITY.md` change
- no `application.py` change
- no `application/ports/companion_review_repository.py` change
- no `extension/shared/messages.js` change

## Validation

### Worktree `--root` (declared route first)

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w4 \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb
```

Outcome: FAIL `declared CPython executable does not exist`. Classification:
**environment limitation** (isolated worktree has no launch-path `.venv`).
Not repaired. Candidate not failed for this miss.

Worktree `--root` `runtime-info` was not re-attempted after that classified
miss; the prompt’s declared first route was proven unusable.

### Classified deviation (canonical `--root`)

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
envelope proof only, not candidate evidence).

### Provenance probe

Temporary file `/tmp/framenest-histacc-04-provenance.py` (outside both git
checkouts). First pytest collection of a module with only top-level statements
reported `no tests ran` (exit 5). Rewritten as one collectable
`test_candidate_src_provenance` that prints `framenest.__file__` and asserts
the path is under the fresh checkout `src/framenest/`. Re-run through the
authorized `test-focus` envelope with `--rootdir` / `pythonpath` on w4:

Printed path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w4/src/framenest/__init__.py
```

Outcome: `1 passed in 0.01s`. Probe deleted. Cleanup: `PROBE_GONE` (file
absent). Not left in any FrameNest worktree.

### Python test-focus matrix

Same classified envelope (canonical `--root`, candidate `--rootdir` and
`pythonpath`):

```text
tests/contract/test_companion_review_api.py
tests/contract/test_adr_0073.py
tests/contract/test_x_route_policy.py
tests/contract/test_tailscale_ingress_security.py
tests/unit/infrastructure/persistence/test_companion_review_repository.py
tests/contract/test_analysis_proposal.py
tests/contract/test_automatic_analysis_privacy_contract.py
tests/integration/persistence/test_analysis_proposal_migration.py
tests/integration/test_persistence_migrations.py
```

Outcome: **151 passed in 70.68s**. No failed suite. Ambient encodings signature
not observed.

### Node tests

From the fresh checkout root (not canonical):

```text
node --test tests/x_companion_extension.test.js tests/companion_review_extension.test.js tests/companion_web_bridge.test.js tests/tailscale_identity_frontend.test.js
```

Outcome: **107 passed**, 0 failed, 0 skipped. Duration 167 ms.

## Per-rule map

| Rule | Owning tests executed or inspected | Result |
|---|---|---|
| R1 hosted click | `analyzed history click posts opened then open_details; pending is hosted without opened` (asserts `historyClickKind` is `open_details` for analyzed and pending; `v: "framenest.companion.web.v1"`; `postToFrame(message, storedOrigin)`; `openHostedDetails` never `openReviewOverlay`; `openedIndex > hostedIndex`); `web and shell share the companion web protocol and never use a wildcard target`; `open_details opens hosted media-details from the pinned extension only`; `hosted Details hide Analyze by AI and Load AI suggestion; standalone keeps them`; duplicate hide assertion in `tests/tailscale_identity_frontend.test.js` | proven, not inverted |
| R2 admin analyzed-only inbox | `test_admin_list_and_detail_are_no_store_and_ordinary_is_forbidden` (admin items `[GENERIC]` only); `test_mixed_inbox_includes_only_owned_pending_and_analyzed_wins` (historical name; body: `PENDING not in` `list_inbox` ids, `PENDING in` admin `list_own_history`); `test_suggestion_ready_lists_without_v1_schema_and_survives_decode_failure`; `test_corrupt_result_json_does_not_drop_inbox_page` | proven, not inverted |
| R3′ listing | ordinary empty own-history 200 in `test_admin_list_and_detail_are_no_store_and_ordinary_is_forbidden`; `test_own_history_opened_alice_bob_admin_isolation` (Alice ⊈ Bob; movies excluded in repository mixed-inbox/own-history asserts); `ordinary own-history compact is newest five of any state`; `ordinary badge refresh uses own-history limit=1 and does not call inbox`; ordinary still 403 on inbox list/detail | proven, not inverted |
| R3′ opened + isolation | `test_own_history_opened_alice_bob_admin_isolation` (Alice POST 200; Bob count unchanged; admin global unopened unchanged until admin opens; admin POST does not re-unopen Alice; Alice on Bob’s id or unknown → 404 `MEDIA_NOT_FOUND`; Alice apply 403); `test_own_history_opened_isolation_does_not_use_global_unopened_count`; `test_opened_and_apply_contracts` (ordinary opened on admin GENERIC → 404 `MEDIA_NOT_FOUND`; apply 403; apply `publication.status == not_ready` / unpublished); retained `test_actor_opened_rows_are_isolated` | proven, not inverted |
| Ingress / four mutations | `test_only_companion_mutations_are_companion_flagged` (exactly four flagged routes; opened capability `x.request`; GET own-history not flagged, capability `x.request`); `test_empty_companion_allowlist_rejects_extension_origin` (opened/apply 403 `MUTATION_ORIGIN_FORBIDDEN`; GET own-history 200) | proven |
| No 0034 / head 0033 | `test_current_schema_head_is_0033`; `test_adr_0076_is_accepted_and_indexed`; `tests/integration/test_persistence_migrations.py`; `tests/integration/persistence/test_analysis_proposal_migration.py`; versions dir inspection | proven |
| Retention | `test_adr_0073_is_accepted_and_indexed` (body unedited vs parent); movie detail 409 `COMPANION_REVIEW_MOVIE_EXCLUDED` and movie apply 409; `mark_opened` still calls `_require_non_movie_media`; analysis-proposal and automatic-analysis privacy contracts in the executed matrix | proven |

Click order in source is hosted `openHostedDetails` first, then POST opened.
That matches the plan’s “do not gate the iframe on opened HTTP.” The test title
phrase “opened then open_details” is satisfied as both occurring
(`openedIndex > hostedIndex`).

## Trust-boundary confirmation

| Claim | Evidence |
|---|---|
| Ordinary opened on foreign/unknown id → 404 `MEDIA_NOT_FOUND` | `test_opened_and_apply_contracts`; `test_own_history_opened_alice_bob_admin_isolation` (Bob’s id and `MISSING`) |
| Ordinary Apply still 403 | same two tests (`CAPABILITY_DENIED`) |
| Ordinary inbox list/detail still 403 | `test_admin_list_and_detail_are_no_store_and_ordinary_is_forbidden`; Alice inbox 403 in isolation test |
| Exactly four `companion_mutation` | `test_only_companion_mutations_are_companion_flagged` equality on flagged `(method, pattern)` set |
| Empty-allowlist mutations fail-closed | `test_empty_companion_allowlist_rejects_extension_origin` (opened and apply 403 `MUTATION_ORIGIN_FORBIDDEN`) |
| GET `/api/companion/own-history` readable under `x.request`; not a mutation | route policy + empty-allowlist GET 200 |
| Own-history `unopened_count` is own-analyzed, not the global latest subquery | `list_own_history` uses `_own_analyzed_latest`; `test_own_history_opened_isolation_does_not_use_global_unopened_count` |
| Alice ⊈ Bob ⊈ admin open-state | isolation API + repository tests |
| Movie 409 retained | detail GET 409; apply POST 409; movies absent from inbox and own-history lists |
| Hosted click never uses `ui/review.html` for this path | `historyClickKind` always `open_details`; `openHostedDetails` does not call `openReviewOverlay` |

No named trust-boundary claim is unproven.

## Classification of the five named deviations

1. **`getattr(self.repository, "list_own_history", None)`** — **accepted-continuation inside the original allowlist.** The port was not allowlisted. Missing method raises `CompanionReviewQueryError` (fail-closed listing, not a leak). Production repository implements `list_own_history`. Not a Protocol hole that grants ordinary inbox/Apply/foreign-open.

2. **`require_owner` passed to the repository only when true** — **accepted-continuation inside the original allowlist.** API sets `require_owner=not identity.has_capability(media.workflow.read)`. Ordinary path still passes `require_owner=True` into the concrete repository, which 404s non-owners before the eligible-run check. Omitting the kwarg on the admin path keeps Protocol fakes without that argument type-checkable. A Protocol-only fake receiving the kwarg would `TypeError`, not silently skip ownership.

3. **Service worker hardcodes `path: "/api/companion/own-history"`** — **accepted-continuation inside the original allowlist.** `messages.js` / `pathFor` was not allowlisted; `pathFor("ownHistory")` would return empty and `fetchJson` would `invalid_path`. The override is a compile-time GET constant, used only on the identity-routed history list (default GET). Mutation routes still use `pathFor` (`reviewInboxOpened` / `reviewInboxApply`) with UUID fail-closed. This is not a hole that lets ordinary callers construct fail-open mutation paths.

4. **Historical `test_mixed_inbox_…` names** — **accepted-continuation.** Bodies assert analyzed-only admin inbox (`PENDING not in ids`) plus pending on admin own-history. Not inverted relative to `02_report_01.md`.

5. **`SECURITY.md` unchanged** — **publication-flag, not a blocking present-tense contradiction.** See next section.

## `SECURITY.md` present-tense judgement

Inspected companion paragraphs (canonical = candidate; file not in the diff).
They still correctly name exactly four `companion_mutation` routes including
opened, empty-allowlist fail-closed for those mutations, GET inbox readability
without the allowlist, and no CORS. They do **not** claim opened is
administrator-only, do **not** claim ordinary 403 hides history, and do **not**
deny own-history. They omit own-history GET and opened-for-owners-with-404.

Judgement: **publication-flag** for a later publication allowlist (surgical
sentence naming ADR-0076 / own-history GET / owner 404). **Not** a
present-tense contradiction that blocks close of this acceptance. This Worker
did not rewrite `SECURITY.md`.

Candidate `docs/X_COMPANION.md` history section is present-tense for R1–R3′
(hosted click, analyzed-only admin inbox, ordinary own-history, four mutations,
empty-allowlist GET).

## Sanitization compliance

No credentials, tokens, cookies, private keys, private media filenames,
host-specific identifiers, disk serials, SSH fingerprints, Tailscale hostnames,
identity-map values, live titles, tweet URLs, companion PEM, or EnvironmentFile
values in this report. Synthetic UUIDs and example logins only. Probe lived
under `/tmp` and was deleted.

## Resolved Execution Issues / Near-Misses

1. Isolated-worktree `ap project check --root <w4>` cannot launch relative
   `.venv/bin/python`. Classified environment limitation. Not repaired.
2. Provenance probe as a pytest module without a `test_*` function collected
   zero tests. Rewritten as one collectable test; printed candidate
   `__file__`; deleted. Not a candidate defect.
3. Trailing `-s` was added on the successful provenance re-run so the printed
   `__file__` was visible under `-q`. Matrix run used the prompt’s `-q -p
   no:cacheprovider` only.

## Pre-Existing Failure Classification

None in the executed Python or Node gates. The worktree AP `.venv` miss is the
known isolated-worktree topology limitation, not a candidate defect.

## Deviations, residual risk, missing evidence

- Exact-source Python provenance is via pytest `pythonpath` under `ap exec`,
  not via `ap exec --root <worktree>` (unusable without unauthorized `.venv`
  topology). Candidate `framenest.__file__` under w4 `src/` is proven.
- Port Protocol still omits `list_own_history` and `require_owner`; honesty
  gap is allowlist-constrained, fail-closed, not a trust-boundary fail-open.
- `pathFor` still lacks `ownHistory`; hardcoded GET override is bounded.
- `SECURITY.md` omission remains a publication-flag.
- Rendered Brave companion, NUC SHA, and live identity mapping were out of
  authority (not missing evidence for this deterministic acceptance).

No named plan test is absent or inverted. No fifth `companion_mutation`. No
Alembic 0034.

## One smallest next step

ORCHESTRATOR: **accept**. Then sequence an explicit Cooperator publication
grant for exact SHA `977a7af80afed16745adb0ef8e939555e5e21cce` (optional
surgical `SECURITY.md` sentence on that grant’s allowlist), public
`ls-remote` equality, routine NUC `framenest-release` to that public SHA, and
rendered R1–R3′ re-test. This Worker does not close, publish, or deploy.

Report justification: `new-evidence`

Authority expiry: all Worker 04 / exchange 01 authority expired at this
terminal report. No follow-on implementation, Git write, push, publication,
NUC access, provider call, product edit, or logical-whole closure is
authorized.
