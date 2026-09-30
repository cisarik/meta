### Report for ORCHESTRATOR_CHAT

Logical whole: kronika-one-product
Worker session ordinal: 61
Worker exchange ordinal: 01
Task identity: KRONIKA-ONE-PRODUCT-S9-P3-F01-VERIFY
Phase: acceptance
Worker session profile: Fresh Independent Re-Audit
Delivery route: manual Cooperator delivery
Phase-qualified result: acceptance-PASS
Logical-whole closure: not-closed
Report justification: final-acceptance

## Acceptance record (echo)

```text
Acceptance candidate: 3bf424586289b500cf45cb0d49676b50d27328fa
  (tree ee39cdee4cd35d25f39586f681844d9753481a4a, branch feat/kronika-one-product,
   parent a3687505eb12359c76f85661e51e36d7e4778fc9)
Acceptance owner map: delta a3687505eb12359c76f85661e51e36d7e4778fc9..3bf424586289b500cf45cb0d49676b50d27328fa
  (one commit, 2 paths); 60_correction_00.md and 60_report_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused route; no
  temporary root is required and none is granted; no mutation
Acceptance risk claims: V1–V5
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: scoped
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

This session did not implement or correct the audited change. The correction
report was treated as a claim and verified read-only against repository and
public evidence. No correction authority was used.

## Per-claim verdicts

### V1 — Candidate identity and containment: VERIFIED

- `git rev-parse HEAD 'HEAD^{tree}' HEAD^` →
  `3bf424586289b500cf45cb0d49676b50d27328fa`,
  `ee39cdee4cd35d25f39586f681844d9753481a4a`,
  `a3687505eb12359c76f85661e51e36d7e4778fc9`. HEAD, tree and parent match the
  candidate exactly.
- `git status --porcelain --untracked-files=all` → empty (branch clean including
  untracked files). Branch is `feat/kronika-one-product`.
- `git diff --name-status a3687505eb12359c76f85661e51e36d7e4778fc9..HEAD` → exactly:
  `M src/framenest/adapters/api/research_api.py` and
  `M tests/contract/test_research_requests_api.py`. No other behavior-bearing
  file changed.
- `git show --stat 3bf424586289b500cf45cb0d49676b50d27328fa` → one commit, 2 paths,
  68 insertions(+), 1 deletion(-). `git rev-list --count a368750..HEAD` → `1`,
  single parent.
- No push: `GIT_TERMINAL_PROMPT=0 git ls-remote origin refs/heads/main
  refs/heads/feat/kronika-one-product` →
  `a3687505eb12359c76f85661e51e36d7e4778fc9 refs/heads/feat/kronika-one-product`
  and `a3687505eb12359c76f85661e51e36d7e4778fc9 refs/heads/main`. Both public
  refs still point at the parent.
- AP pin: `git ls-files -s .ap` → `160000 73e20ef80b88700d5fcbc397cd8edd4fc425869f 0 .ap`;
  `git -C .ap rev-parse HEAD` → `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Gitlink
  and `.ap` HEAD agree.

### V2 — Correction shape: VERIFIED

`git show 3bf4245:src/framenest/adapters/api/research_api.py`:

- POST `/api/research-requests` successful-admission nudge (lines 260–265):
  `if row.record.state.value == "admitted": try: runtime.submit_pending();
  runtime.release_remote_pending() except Exception: pass`. The new call is the
  only added statement and sits inside the pre-existing `try/except Exception:
  pass` guard, after `submit_pending()`.
- GET `/api/research-requests/{operation_id}` nudge (lines 283–289):
  `if runtime is not None: try: if runtime.submit_pending() is None:
  runtime.poll_once(); runtime.release_remote_pending() except Exception: pass`.
  The new call is inside the pre-existing guard, after the
  `submit_pending()/poll_once()` block.
- The disabled/absent-runtime path is unchanged: the GET handler still returns
  via `runtime is not None` before the guard, and the POST handler's
  disabled runtime refuses earlier with `E_DISABLED`.
- Diff shape: exactly two added lines in production code (no deletions, no
  signature/response/status changes). Response shapes, status codes, capability
  checks, admission, polling cadence, cancel semantics and the cleanup loop bound
  (`release_remote_pending(limit=20)`) are untouched.
- New production callers confirmed: `grep release_remote_pending src` finds only
  the definition (`application/research.py:555`) and the two new calls
  (`research_api.py:263`, `research_api.py:287`). The previously workerless
  `release_remote_pending()` now has exactly the two intended call sites.

### V3 — Causal evidence: VERIFIED

Focused route on the corrected candidate (exit 0):

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa
→ ap project check --baseline: PASS

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 3bf424586289b500cf45cb0d49676b50d27328fa --operation test-focus -- tests/contract/test_research_requests_api.py tests/contract/test_research_completion.py tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider
→ 20 passed in 7.84s
```

The exec run reported `OK execution trust: baseline 3bf4245...`, i.e. it ran the
exact candidate. The named regression was collected and run in isolation:

```text
tests/contract/test_research_requests_api.py::test_nudge_releases_remote_after_validated_save PASSED [100%]
```

Causality for the missing cleanup, established from code and the parent diff:

- The regression sets `poll_kind = COMPLETE` and drives `coordinator.poll_once()`
  directly. It asserts the request reaches `saved` while
  `cleanup_state == "pending"` and `provider.releases == []`, proving the
  completion path itself does not release the remote handle.
- A disabled client (`runtime=None`) GET returns 200 and leaves
  `cleanup_state == "pending"` with `releases == []`, proving the absent-runtime
  path performs no release.
- The enabled client GET then drives the nudge and asserts
  `provider.releases == [HANDLE]` and `cleanup_state == "deleted"`, i.e. exactly
  one recorded release and the terminal transition.
- The parent (`a368750`) has no `release_remote_pending` reference at all:
  `git show a368750:src/framenest/adapters/api/research_api.py | grep -n ...`
  shows only `submit_pending()` (line 262) and `submit_pending()/poll_once()`
  (lines 284–285). With the two added statements absent, the same GET nudge
  cannot release; `provider.releases` stays `[]` and `cleanup_state` stays
  `pending`, failing the added assertions. The new test is therefore causal for
  the correction, exactly as the correction report's Red evidence recorded
  (`assert [] == [ProviderHandle(value='api-handle-1')]`). The regression drives
  only the repository's existing fake-transport harness; no new files were
  created and the repository was not mutated.

### V4 — No live side effects: VERIFIED

- No provider call: both focused suites inject `FakeProvider` and the coordinator
  is constructed directly with that fake; no real provider/transport is selected.
- No credential or secret read: the test settings carry only
  `database_path` and a synthetic `identity_map`; no API key is loaded or
  accessed.
- No NUC/SSH/sudo and no remote Git write: the only network operation was a
  read-only `git ls-remote`.
- Repository clean after the run: `git status --porcelain
  --untracked-files=all` is empty; HEAD/tree and AP pin unchanged.
- No scope enablement: the diff changes only the two API nudge blocks and one
  test file; it does not enable research, change budgets/limits, migrations,
  configuration or dependencies. The changes are inert when `runtime is None`.

### V5 — Finding disposition

`KRONIKA-ONE-PRODUCT-S9-P3-F01` → **verified-closed**.

V1–V4 are all established on the corrected candidate
`3bf424586289b500cf45cb0d49676b50d27328fa`: identity/containment holds, the
correction is exactly the two guarded `release_remote_pending()` calls, the
focused route passes on the exact candidate, the new regression is causal and
Red on the parent, and there are no live side effects. The earlier defect — the
implemented-but-uncalled automatic cleanup — is now closed by an automatic call
on both nudge paths.

## Control matrix results

| Control | Result |
| --- | --- |
| `git rev-parse HEAD 'HEAD^{tree}' HEAD^`; `git status --porcelain -uall` | HEAD/tree/parent exact; clean tree |
| `git diff --name-status a368750..HEAD` | exactly the two allowlisted paths |
| `git show 3bf4245` | one commit, 2 paths, +68/-1 |
| `GIT_TERMINAL_PROMPT=0 git ls-remote origin ...` | both refs = a368750 (no push) |
| AP gitlink / `.ap` HEAD | `73e20ef8…` both |
| `./.ap/ap project check --baseline 3bf4245` | PASS |
| `./.ap/ap exec ... test-focus ...` | 20 passed in 7.84s (exit 0) |
| named regression in isolation | 1 passed |

## Limitations

- Causality was established from the source diff and the regression's own
  assertions, not by running the new test against a checked-out parent tree; the
  grant allowed no temporary root and no mutation, so no worktree/checkout was
  created.
- The broad Python suite, JS/browser suites, NUC access and any live provider
  behavior were out of scope and were not exercised.
- Only the declared focused route and the exact control matrix were run; no
  unknown-unknown audit was attempted.

## Residual risk

- Low. The change adds two statements inside pre-existing
  `try/except Exception: pass` guards; a failure in `release_remote_pending()`
  is swallowed exactly like the existing nudge calls and cannot alter response
  shape or status. The GET path now performs up to `limit=20` idempotent release
  attempts per detail read; this is pre-existing loop behavior, already bounded
  and per-row fault-tolerant. No new failure mode reaches the client.

## Out-of-scope observations (non-authorizing ledger candidates)

1. The POST-handler release runs only on the freshly-`admitted` path, so an
   idempotent replay that returns an already-terminal row still depends on a
   later GET nudge for cleanup. This is scope-preserving, not a defect, and is
   noted only as a possible future review item.
2. `release_remote_pending()` leaves a row `pending` indefinitely when the
   provider raises on `release_remote` (per-row `except Exception: continue`).
   This is pre-existing and unchanged; a persistent provider-side delete failure
   would keep being retried each nudge up to the bound.
3. Cleanup release is triggered on every detail read, which may be more frequent
   than strictly required; still bounded by `limit=20` and only pending rows.

These are non-authorizing observations for a future explicit decision; they
grant no work.

## Critique

- The correction is minimal, matches the accepted design statement ("delete the
  remote response after validated local persistence"), and reuses the existing
  guard and helper rather than adding new control flow.
- The regression is well-placed: it asserts the store-level `cleanup_state`
  transition (not just the response body), the positive release count
  (`[HANDLE]`), and that the disabled/absent-runtime path performs no release —
  which is why it cleanly distinguishes parent from candidate.
- The audit remained within its declared controls and did not mutate the
  repository.

## Authority expiry

This terminal report ends the S9-P3-F01 verification exchange.
