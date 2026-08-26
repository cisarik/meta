# FrameNest — Deterministic Companion Acceptance completion (exchange 02)

Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe (bounded continuation)
Phase: acceptance (deterministic portion)
Reasoning recommendation: Medium (same familiar suites; one command plus short report)
Task identity: FRAMENEST-COMPANIE-DETACC-02
Continuity anchor: your terminal PASS report for FRAMENEST-COMPANIE-DETACC-01, archived as `/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/01_report_00.md`
Authority renewal: prior authority expired at that terminal report. This exchange grants one new bounded read/test-only task to the exact same healthy session. Retained context is convenience, never authority. Re-gate repository state before execution. Evidence remains non-independent. Stop on any conflict between retained context and current repository evidence.
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

## Mission

Close the three coverage gaps you honestly recorded under “Missing evidence”
in exchange 01. Execute exactly ONE additional `test-focus` invocation over
exactly TWO files that own them, then write one short terminal report.
Everything else from exchange 01 (boundaries, sanitization, canonical route,
classification discipline) carries over unchanged.

Exact baseline unchanged (= public `main`):
`91410fe063d9907304cff4550f61d403880a2eeb`

## Re-gate (fail-closed, before execution)

- `git rev-parse HEAD` equals `91410fe063d9907304cff4550f61d403880a2eeb`;
- branch `feat/x-meme-browser-companion`;
- `git status --porcelain=v1` empty;
- `.ap` HEAD equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

Any difference stops you; classify per RF-12, mutate nothing, return evidence.

## Command (exact; no additions, no widening)

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 91410fe063d9907304cff4550f61d403880a2eeb \
  --operation test-focus -- \
  tests/unit/infrastructure/persistence/test_companion_review_repository.py \
  tests/integration/persistence/test_analysis_proposal_migration.py \
  -q -p no:cacheprovider
```

If output truncates, split into two invocations over the same two files —
never add other paths.

## Coverage this closes (cite executed test ids in your report)

1. Suggestion-ready analyzed rows listed without requiring suggestion payload
   `result_schema_version == v1`, surviving undecodable JSON rows
   (`test_suggestion_ready_lists_without_v1_schema_and_survives_decode_failure`).
2. One corrupt suggestion JSON does not drop or 500 the mixed inbox page
   (`test_corrupt_result_json_does_not_drop_inbox_page`).
3. Omitted-category own-saves appear in the merged pending history as owned
   GENERAL rows (`test_mixed_inbox_includes_omitted_category_owned_general_saves`).
4. Successful preserve-and-append Apply unions stored keys with submitted
   mapped AI keys while preserving unselected fields
   (`test_apply_review_preserves_unselected_fields_and_unions_tags` and its
   sibling union tests in that file).
5. Migration `0033` additive proposals table: create at head, `0032`
   downgrade restores prior shape, re-upgrade stable
   (`tests/integration/persistence/test_analysis_proposal_migration.py`).

## Hard boundaries

Read/test-only. No edits, no commits, no push, no NUC/SSH/sudo, no providers,
no browser, no EnvironmentFile access, no dependency changes. A failing test
is classified (candidate / harness / ambient-route / environment /
pre-existing-with-full-record), never repaired. Preserve the first causal
error. Same ambient-route rule: rerun once through the identical `ap exec`
operation if the encodings signature appears.

## Output

Write exactly one file:

```text
/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/01_report_01.md
```

Professional English, beginning exactly:

### Report for ORCHESTRATOR_CHAT

Required content: coordinate echo (session `01`, exchange `02`); status plus
phase-qualified result — `acceptance-PASS` only when the re-gate holds AND
both files pass completely, otherwise PARTIAL/BLOCKED with sanitized failure
classes; one-line gate echo; the exact invocation line(s) and pass/fail
counts; per-gap citation of the executed owning test ids (items 1–5 above);
sanitization compliance statement;
Resolved Execution Issues / Near-Misses and Pre-Existing Failure
Classification (`none` expected);
deviations/risks if any; Report justification: new-evidence; authority-expiry
statement terminating even this renewal.

Abbreviated capability recheck suffices: material changes since the exchange-01
handshake (expected: none).

## Stopping rule

Stop after the terminal report, or earlier as BLOCKED when the re-gate fails,
a required capability is unavailable, or a failure cannot be classified
inside your authority.

## Transition owner

ORCHESTRATOR reconciles this report, then sequences the Cooperator rendered
Brave pass against the same SHA using the NOT-RUN-here list from exchange 01.
You have no follow-on authority.
