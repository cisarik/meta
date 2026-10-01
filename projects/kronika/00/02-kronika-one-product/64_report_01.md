### Report for ORCHESTRATOR_CHAT

# S9-R bounded correction — close audit findings F-1…F-4

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 64
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S9-R-CORRECTION-AUDIT-FINDINGS
Delivery route: manual Cooperator delivery
Evidence posture: non-independent; the corrector never certifies its own change
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-mutation
Escalation disposition: none
Start commit: e8f1c04b289b7bd694d66edba012d288ee41e610
End commit: 2af8edde5faf8967777a68b0a72685cc580c45ea
```

PASS. All four findings are corrected inside the 7-path allowlist, the focused
route exits 0 with the new regressions present, and one local commit exists.
Closure is not self-certified: the corrected candidate needs a fresh
independent re-audit.

## 1. Re-gate

| Gate | Observed result |
|---|---|
| Branch | `feat/kronika-one-product` |
| HEAD at start | `e8f1c04b289b7bd694d66edba012d288ee41e610` |
| AP gitlink / `.ap` HEAD | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Index and worktree | Clean, including untracked files |
| Continuity anchor | `64_report_00.md` PASS; audit `65_report_00.md` |

No gate conflict. No stopping condition triggered.

## 2. Findings corrected

### F-1 — adapter coverage and the report-attribution defect (guard regression)

**Attribution defect recorded (not edited).** `64_report_00.md` §4 attributed
"strict usage parsing and submit-404 distinction" to
`tests/unit/infrastructure/ai/test_openai_responses_adapter.py`. That file was
unchanged in the `e8f1c04…` delta, so the claim overstated the evidence.
`64_report_00.md` is a historical trace artifact and was deliberately **not**
edited; this section is the correction of record.

**Evidence added** (12 cases in `test_openai_responses_adapter.py`), all passing
against the unchanged `e8f1c04…` production code — `_parse_usage` and
`_submit_status_error_code` were not touched this session, so these are guard
regressions with no expected Red-first:

- reported `cache_write_tokens` parses into `cache_write_input_tokens`, and an
  absent write detail stays `None` rather than becoming `0`;
- missing `usage` yields `answer.usage is None`;
- ten parametrized missing/invalid cases never become a zeroed `ResearchUsage`,
  including a non-dict `input_tokens_details`, a non-list
  `output_tokens_details`, a negative count, a boolean, `R > I` and
  `R + W > I`;
- submit `404` maps to `PROVIDER_UNAVAILABLE` while poll `404` still maps to
  `RESULT_EXPIRED`.

### F-2 — refresh and durable-snapshot regressions (guard regression)

One contract regression added in `test_research_provider_contract.py`
(`test_disabled_start_enables_without_restart_and_keeps_admitted_pricing`). It
runs against unchanged `e8f1c04…` production code, using a real disposable
migrated engine, a mutable `configuration_provider` and a fake transport only:

1. the runtime is built while research is **disabled** and exists;
2. a disabled start refuses admission with `E_DISABLED`;
3. enabling through the same provider admits and completes **without restart**;
4. a later model change reaches only the next admission, while the first
   request keeps its persisted model;
5. after a simulated restart the first request still carries
   `gpt-5.6-luna`, profile `s9r-20260930`, `RECONCILED` accounting, and the
   tuple-resolved schedule, with the day/month totals equal to the Luna cost
   plus the second reservation.

This covers plan §8 `Refresh` and `Snapshot` and the untested
`configuration_provider` composition path.

### F-3 — media half of the shared configuration contract

`app.js` now completes the media side:

- `framenestResponseRevision` parses the strong `ETag`;
  `framenestRevisionHeader` emits `If-Match` **only** when a revision exists, so
  an absent header stays valid server-side;
- the provider-list read records the revision
  (`applyAiProvidersPayload(payload, revision)`);
- `saveAiProviderRecord`, `deleteAiProvider` and `activateAiProvider` send the
  captured `If-Match`, consume the returned ETag via `applyAiProvidersRevision`,
  and on success call `invalidateResearchSettingsRevision()`;
- a successful research save calls `invalidateAiProvidersRevision()`, and a
  research save without a captured revision is refused with the conflict copy
  and `stale` set, so a dirty sibling draft never silently adopts a new
  revision.

Non-mutating `runAiProviderPing` was deliberately left without `If-Match`.
Coverage added to `tests/ai_providers_admin_frontend.test.js` (3 new tests):
`If-Match` sent with the captured revision, header-free behaviour preserved when
no revision was captured, media→research invalidation, and
research→media invalidation.

### F-4 — exact settings response shape

`ResearchSettingsResponse` now carries exactly the seven planned fields;
a new `ResearchSettingsUpdateResponse` adds `changed: boolean` and is the PUT
`response_model`. Before: GET emitted an eighth key `"changed": null`. After:
GET returns exactly the seven keys and PUT returns those seven plus `changed`.
Two key-set assertions added in `test_research_settings_api.py`, including the
six writable settings keys.

## 3. Changed files (6 of the 7 allowlisted paths)

```text
src/framenest/adapters/api/ai_admin_api.py                       (F-4)
src/framenest/adapters/api/web/app.js                            (F-3)
tests/ai_providers_admin_frontend.test.js                        (F-3)
tests/contract/test_research_provider_contract.py                (F-2)
tests/contract/test_research_settings_api.py                    (F-4)
tests/unit/infrastructure/ai/test_openai_responses_adapter.py    (F-1)
```

`tests/contract/test_research_completion.py` was allowlisted but not needed:
F-2 landed entirely in `test_research_provider_contract.py`, which the grant
permitted ("and/or"). No path outside the allowlist was touched.

## 4. Validation evidence

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610
=> ap project check --baseline: PASS

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline e8f1c04b289b7bd694d66edba012d288ee41e610 --operation test-focus -- \
  tests/unit/infrastructure/ai/test_openai_responses_adapter.py \
  tests/contract/test_research_provider_contract.py \
  tests/contract/test_research_completion.py \
  tests/contract/test_research_settings_api.py \
  tests/contract/test_research_requests_api.py \
  tests/unit/application/test_research_coordinator.py -q -p no:cacheprovider
=> 70 passed

node --test tests/ai_providers_admin_frontend.test.js tests/research_settings_admin_frontend.test.js tests/kronika_ui.test.js
=> tests 33 / pass 33 / fail 0

git diff --check
=> clean
```

Test counts moved 58→70 Python (six new tests plus the parametrized adapter
cases) and 29→33 JavaScript.

One narrow extra run, for the changed `ai_admin_api.py` and its shell callers
outside the granted route: `test_ai_provider_admin_api.py`,
`test_ai_configuration_storage.py`, `test_ai_cli.py`,
`test_kronika_access_inventory.py` → **268 passed**. No broad suite was run.

**Red/green record.** F-1 and F-2 are guard regressions: they pass against
`e8f1c04…` production code, and no production behavior was reverted, so no
Red-first was expected or observed. F-3 and F-4 are before/after client and
response changes:

| Assertion | Before | After |
|---|---|---|
| GET settings key set | 7 fields + `"changed": null` | exactly 7 fields |
| PUT settings key set | 7 fields + `changed` | 7 fields + `changed` (unchanged) |
| media record write headers | no `If-Match` | `If-Match: "<captured revision>"` when captured |
| media write with no captured revision | n/a | no `If-Match` (still valid) |
| media success → research revision | untouched | dropped and marked `stale` |
| research success → media revision | untouched | dropped |
| research save with no captured revision | sent `If-Match: ""` | refused with the conflict copy |

## 5. Commit result (local only)

```text
commit:  2af8edde5faf8967777a68b0a72685cc580c45ea
tree:    3f6367cf2da9224eebefb7659ca0efb8ae7d54e0
parent:  e8f1c04b289b7bd694d66edba012d288ee41e610
subject: fix(research): close the S9-R audit findings
```

No push, merge, rebase, reset, branch change, NUC access, provider call or
credential inspection occurred. No subagents, dependencies, migrations or AP
changes.

## 6. Deviations and near-misses

- **`tests/contract/test_research_completion.py` untouched** — permitted by the
  "and/or" wording; no loss of coverage, since F-2 is fully covered in the
  provider-contract file.
- **Near-miss, self-corrected before commit.** Two `app.js` edits landed on the
  wrong function while implementing F-3: a headers edit corrupted
  `runAiProviderPing` (changing its request body and error copy), and an
  identifier edit left `activateAiProvider` referencing undefined
  `selectedProviderId`/`selectedModelId`, which its `try` would have swallowed
  into an "unreachable" message. Both were caught by the pre-existing
  `ping and pong run only on explicit actions…` test and are fixed; the
  corrected diff is reviewed above and the full JS route passes. Recording it
  because a mis-targeted edit in a 14k-line untyped shell is a real residual
  risk that the next audit should re-check.
- Media `If-Match` remains optional server-side, as recorded in the
  implementation report; this correction adds the shell half without changing
  that server-side compatibility.
- Ledger candidates L-1…L-4 from `65_report_00.md` remain out of scope and
  unaddressed.

## 7. Smallest next step

Issue the fresh independent re-audit grant against
`2af8edde5faf8967777a68b0a72685cc580c45ea`, explicitly asking it to (a) verify
the four corrections, (b) re-check the `app.js` mutation callers for
mis-targeted edits of the kind recorded in §6, and (c) state whether L-1…L-4
remain acceptable. Publication, NUC refresh and rendered acceptance stay
separate.

## 8. Critique

- **MEASURED:** F-1's untested behaviors and F-2's untested composition path
  now have causal regressions; both pass on the current production code.
- **MEASURED:** F-4 removes the extra `changed: null` key, and the key set is
  asserted.
- **MEASURED:** F-3 is now symmetric, and the absent-`If-Match` path stays
  valid.
- **LEAD:** the F-3 mis-targeted-edit near-miss shows the shell needs the same
  scrutiny as Python; the re-audit should read those four mutation functions
  closely rather than trusting the green suite.

```text
External trace disposition: configured
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Prompt filename: 64_correction_01.md
Report filename: 64_report_01.md
Destination: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Git publication owner: COOPERATOR
```

**Authority expiry:** this terminal report ends the correction grant for
`kronika-one-product` session 64, exchange 02. No publication, NUC refresh or
rendered acceptance follows from it.