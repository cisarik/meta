### Report for ORCHESTRATOR_CHAT

Logical whole: kronika-one-product
Worker session ordinal: 60
Worker exchange ordinal: 01
Task identity: KRONIKA-ONE-PRODUCT-S9-P3-F01-CLEANUP
Phase: correction
Worker session profile: Bounded Correction Worker
Delivery route: manual Cooperator delivery
Report justification: new-mutation

## Outcome: PASS

The two research API nudge blocks now call `runtime.release_remote_pending()`
inside their existing `try/except Exception: pass` guards. A causal regression
proves the terminal `saved` + `cleanup_state: pending` request transitions to
`deleted` on a normal API interaction, with the fake provider recording exactly
one release, and with no release attempted for a disabled/absent runtime.

## Baseline verified

- Root: /Users/agile/Projects/framenest
- Branch: feat/kronika-one-product
- HEAD: a3687505eb12359c76f85661e51e36d7e4778fc9
- AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
- Index/worktree clean at start; no divergence observed.

## Changed files (2, exact allowlist)

- `src/framenest/adapters/api/research_api.py`
  - POST `/api/research-requests` successful-admission nudge: added
    `runtime.release_remote_pending()` after `runtime.submit_pending()`.
  - GET `/api/research-requests/{operation_id}` nudge: added
    `runtime.release_remote_pending()` after the `submit_pending()/poll_once()`
    block. Both additions sit inside the pre-existing `try/except Exception:
    pass` guards. `runtime is None` behavior is unchanged.
- `tests/contract/test_research_requests_api.py`
  - `FakeProvider` now records release handles (`self.releases`) and can carry a
    COMPLETE answer.
  - Added `_answer()` helper and regression
    `test_nudge_releases_remote_after_validated_save`.

No other path touched. Response shapes, status codes, capability checks,
admission, polling cadence, cancel semantics, and the loop bound (`limit=20`)
are unchanged.

## Exact commands and evidence

### Red (parent production code, new test present)

Temporarily reverted the two added calls, then:

```text
./.ap/ap exec --root /Users/agile/Projects/framenest --baseline a3687505eb12359c76f85661e51e36d7e4778fc9 --operation test-focus -- tests/contract/test_research_requests_api.py::test_nudge_releases_remote_after_validated_save -q -p no:cacheprovider
```

Result: `1 failed`.

```text
>       assert provider.releases == [HANDLE]
E       AssertionError: assert [] == [ProviderHand...pi-handle-1')]
E         Right contains one more item: ProviderHandle(value='api-handle-1')
tests/contract/test_research_requests_api.py:266: AssertionError
```

### Green (correction restored)

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline a3687505eb12359c76f85661e51e36d7e4778fc9
```

Result: `ap project check --baseline: PASS`

```text
./.ap/ap exec --root /Users/agile/Projects/framenest --baseline a3687505eb12359c76f85661e51e36d7e4778fc9 --operation test-focus -- tests/contract/test_research_requests_api.py tests/contract/test_research_completion.py tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider
```

Result: `20 passed in 7.61s` (exit 0).

Red/Green causal chain: on the parent the GET nudge saved the terminal request
with `cleanup_state=pending` and left it pending (provider release list empty);
after the correction the same GET nudge calls `release_remote_pending()`, the
row becomes `deleted`, and the provider records the handle exactly once.

## Commit result (local only)

- Commit: `3bf424586289b500cf45cb0d49676b50d27328fa`
- Tree: `ee39cdee4cd35d25f39586f681844d9753481a4a`
- Subject: `fix(research): release remote responses on research API nudges`
- Staged by exact path only; worktree clean after commit.
- No push; candidate remains local.

## Deviations

None. No out-of-allowlist change was needed. No subagents, no provider calls,
no credentials, no NUC/SSH/sudo, no publication, no Git remote operations, no
`git add .`/`-A`.

## Smallest next step

An independent verification of commit `3bf424586289b500cf45cb0d49676b50d27328fa`
against the parent, followed by the separate deployment step.

## Critique

- The correction is minimal and matches the accepted design statement ("delete
  the remote response after validated local persistence").
- The POST-handler release runs only on the freshly-admitted (`admitted`) path,
  exactly mirroring the existing nudge placement; an idempotent replay that
  returns an already-terminal row still relies on the GET nudge. This preserves
  current behavior and the authorized scope rather than broadening it.
- The regression asserts both the positive release and the disabled/absent
  no-release case, and checks `cleanup_state` at the store, not only the
  response body.

## Authority expiry

This terminal report ends the S9-P3-F01 correction grant.
