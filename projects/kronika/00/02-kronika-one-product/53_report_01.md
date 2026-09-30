### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 53
Worker exchange ordinal: 02

Status: PASS

Phase-qualified result: implementation-PASS

Start commit: `7f7aae9012d35671b062c8731e9009169501d4d0`
End commit: `ef9920333013f3f70bf5e3443be2e51814f6b9c3`
End tree: `e4338c2f31e8aff2829351ec107e2d75a165a473`
Branch: `feat/kronika-one-product` (ahead of origin by 2; not pushed)
AP pin: `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (unchanged)

F01 is corrected inside the allowlist. Closure of F01 is not self-certified. A fresh independent re-audit of the corrected candidate is required next. This is not acceptance, publication, or deployment.

## Changed files

```text
src/framenest/adapters/api/web/app.js
tests/kronika_ui.test.js
```

`kronikaFreezeAttempt` now recomputes the SHA-256 fingerprint over the current login, kind, exact prompt, and `kronika-research-v1`. It reuses the stored `client_request_id` only when that fingerprint is non-empty and equals the stored fingerprint. A mismatch, a missing or empty stored fingerprint, or no `crypto.subtle` mints a new id. The prompt stays out of storage. Recovery still restores the id and the same recovery copy, and it does not submit. `kronikaRetrySubmission` still posts the frozen attempt.

## Tests

Repository gate, before editing, exit 0:

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 7f7aae9012d35671b062c8731e9009169501d4d0
```

Red, on parent `7f7aae9…`, before the production change. Command:

```text
node --test --test-name-pattern "reload recovery reuses" tests/kronika_ui.test.js
```

Result: 1 failed, 0 passed. Exact assertion at `tests/kronika_ui.test.js:665`:

```text
assert.equal(same.bodies[0].client_request_id, bodiesA[0].client_request_id);
```

`AssertionError` `strictEqual`. Expected `8575462f-cd60-4191-9d69-225c06681420`. Actual `8b243e1a-e463-4b3f-80a6-d5af64b605e6`. Those ids are from that run only. The failure is that the reloaded submit minted a different `client_request_id`.

Green, after the correction:

```text
node --test tests/kronika_ui.test.js
```

Result: 12 passed, 0 failed. The existing same-page retry test stayed green and was not edited.

Bounded run, exit 0:

```text
node --test tests/kronika_ui.test.js tests/gallery_details_playback_handoff.test.js tests/tailscale_identity_frontend.test.js tests/metadata_form_contract.test.js
```

Result: 76 passed, 0 failed, 0 skipped.

No Python run. No browser, NUC, sudo, or provider call.

## Commit

Local only. Subject: `fix(kronika): reuse the frozen request id across reload recovery`. No push, fetch, merge, or branch change.

## Deviations and missing evidence

None in scope. The harness gained a `storage` and `login` option in test code only. Rendered browser evidence and an independent re-audit of this commit are still absent.

## Smallest next step

A fresh independent re-audit of `ef9920333013f3f70bf5e3443be2e51814f6b9c3`. F01 closure is not claimed by this correction.

Report justification: new-mutation

```text
Orchestration critique:
MEASURED: none
LEAD: none

Issues: none

Logical-whole closure: not-closed
```

Authority expiry: this terminal report ends the correction grant. No publication or deployment is authorized.
