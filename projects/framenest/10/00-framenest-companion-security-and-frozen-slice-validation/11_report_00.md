### Report for ORCHESTRATOR_CHAT

**Coordinates:** framenest-companion-security-and-frozen-slice-validation; Worker session 11; exchange 01.
**Status:** complete — implementation-PASS. Start commit `ba54cfa7eb107efaf62c94ba76e895842ee35065`; end commit `3acd06daaedadd4bb67c7cc808123715b142b28a` (branch `feat/x-meme-browser-companion`, porcelain clean, no push).

**Changed files and purpose (all within the exact allowlist):**

1. `src/framenest/application/x_acquisition.py` — Finding 1. Added four typed subclasses, named consistently with the existing family and mirroring S4's YouTube pattern:
   - `XAcquisitionNotRetryableError(XAcquisitionStateConflictError)`
   - `XAcquisitionNoRetryableAssetsError(XAcquisitionStateConflictError)`
   - `XAcquisitionInvalidCursorError(XAcquisitionInvalidRequestError)`
   - `XAcquisitionInvalidRequesterIdentityError(XAcquisitionInvalidRequestError)`
   Raiser sites converted with IDENTICAL messages: `list_owned` cursor parse (`x_acquisition.py:419`, was :403, kept `from None`); `retry` state gate (`:456`, was :440); `retry` no-retryable-assets gate (`:470`, was :454); `_normalize_requester` identity (`:1451`, was :1435, kept `from exc`).
2. `src/framenest/adapters/api/x_request_api.py` — Finding 1. The two `str(exc)` passthroughs became static literals: list route now catches `XAcquisitionInvalidCursorError` → 422 `X_REQUEST_INVALID_URL` "Invalid X request cursor." and `XAcquisitionInvalidRequesterIdentityError` → 422 "Invalid requester identity."; retry route catches `XAcquisitionNotRetryableError` → 409 `X_REQUEST_STATE_CONFLICT` "X claim is not retryable in its current state." and `XAcquisitionNoRetryableAssetsError` → 409 "X claim has no retryable assets."; the now-unreachable generic-class catches were removed and the unused `XAcquisitionStateConflictError` import dropped. No `str(exc)` remains in the file — B3 is complete for X.
3. `src/framenest/application/companion_review.py` — Finding 2. `_parse_analysis_run_id` return annotation corrected `MediaId` → `MediaAnalysisRunId` plus a TYPE_CHECKING-only import (annotation-only; runtime-inert under `from __future__ import annotations`). Verified before changing: both call sites (`:657`, `:695`) flow the value into `analysis_run_id=` parameters, and the function's name, error type (`CompanionReviewAnalysisRunNotFoundError`), and message are unambiguously run-identity purpose — the stop condition (a genuine `MediaId` for a non-run purpose) does not apply.
4. `tests/contract/test_library_api.py` — Finding 3. Renamed to `test_malformed_library_id_uses_uniform_validation_contract` and realigned to the accepted 460b37b contract: 422; body exactly `{"error":{"code":"VALIDATION_FAILED","message":"Request validation failed."}}`; no `detail`; no echo of `not-a-uuid`; `Cache-Control: no-store`. Rest of the module untouched.
5. `tests/contract/test_x_request_api.py` — two route-level discriminator-pair tests (one per pair), asserting exact bodies and that the hostile cursor is not echoed; no other changes.

**Byte-identity basis:** complete raiser inventory verified — the only raisers of `XAcquisitionInvalidRequestError`/`XAcquisitionStateConflictError` in `src/` are the four now-typed sites; the submit route's `(XAcquisitionInvalidRequestError, FrameNestXUrlError)` tuple catch still matches the subclasses, so all caller-observable statuses, codes, and messages are unchanged.

**Tests and validation (exact):**
- `./.ap/ap project check --baseline ba54cfa…` → PASS (baseline contract, CPython 3.13 runtime, schema 1, sanitized-v1).
- `./.ap/ap exec … --operation test-focus -- tests/contract/test_x_request_api.py tests/contract/test_library_api.py tests/contract/test_x_companion_api.py tests/contract/test_x_route_policy.py -q -p no:cacheprovider` → **42 passed in 4.40s**, including the previously failing library test now realigned and the two new discriminator tests.

**Commit result:** exactly one commit `3acd06d` (`refactor: typed X invalid-request and state-conflict discriminators, realign library 422 test`), staged by exact path, no push, no force. Subject justification: the production change is externally byte-identical typed-discriminator hardening (refactor), while the commit also adds discriminator-path tests and realigns the stale library 422 assertion to the independently accepted 460b37b contract.

**Deviations/risks/missing evidence:** one documented interpretation — the prompt's "catch the subclasses BEFORE the generic branches" was implemented by replacing the two generic `str(exc)` catches with the typed static-literal catches (the stated end state is incompatible with retaining them as dead fallbacks); the remaining generic branches (NotFound/Infrastructure) sit after the typed catches, and removal is byte-identical under the verified raiser inventory. Residual risk: a future untyped raiser of either parent class reaching these routes would surface as 500 rather than 422/409 until typed. Validation was executed pre-commit at the exact baseline (RF-16 baseline-bound execution); the commit is byte-identical to the validated state. No missing evidence.

**Smallest next step:** dispatch the required fresh independent acceptance Worker for the Finding 3 validator-semantics realignment and the whole candidate.

**Report justification:** `new-mutation`.
**Authority expiry:** this report terminates my authority; no further action is taken or authorized beyond it.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: `test_malformed_library_id_uses_fastapi_validation` failed at baseline — superseded-by-accepted-authority (commit 460b37b changed the workspace validation contract; the test's assertion shape was the stale party); baseline predates: latest-correction-only; regression exclusion evidence: focused suite green post-realignment, all other module tests untouched and passing.
