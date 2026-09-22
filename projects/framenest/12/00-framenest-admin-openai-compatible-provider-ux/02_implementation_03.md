# Implementation Exchange 03 — Session 02 — Slice 2: Vision Probe (Pong) — Golden Fixture, Judge, Sidecar, CLI, NVIDIA Probe

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (current-session continuation)
Phase: Implementation
Task identity: IMPLEMENT-VISION-PROBE-PONG-SLICE-2
Implementation authority: explicit
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: High — named risk: the judge and fixture become the acceptance surface for the Cooperator's color pong; flaky matching or leaked raw completion text would invalidate the experiment and the privacy boundary
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PASS report for exchange 02
(`/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_02.md`)
and your corrective commit `980db7af33910bb676eef46ed89fd2b453112bb6`. Prior
authority expired at that report. This is a complete renewed grant for slice 2
of the accepted plan. Retained context is convenience, not authority; if it
conflicts with current repository evidence, current repository evidence wins —
stop and report. Evidence in this exchange is non-independent (same session).

## Goal

Implement slice 2 of the accepted plan: the provider-neutral color pong as a
CLI-driven server-side operation — committed golden fixture, bounded color
judge, sanitized sidecar, generic and NVIDIA probe paths, and one new CLI
command. No HTTP routes, no admin UI, no documentation changes in this slice.

## Mandatory reading

- The accepted plan
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report_orchestrator.md`
  §4 (adapter), §6 (capabilities), §7 (ping/pong contract, fixture, judge,
  statuses, persistence, rate limit), §10 (CLI), §13 tests 4, 5, 6, 11, §14
  slice 2.
- Your own slice-1 code: `provider_records.py`, `configuration.py`,
  `registry.py`, `openai_chat_completions.py`, `nvidia_nim.py`,
  `src/framenest/adapters/cli/ai.py`.
- `src/framenest/infrastructure/ai/image_derivative.py` (the deterministic
  PNG-to-JPEG encoder boundary), `transport.py`, and
  `tests/contract/test_web_package_resources.py` (pattern for the wheel
  resource contract).

## Repository gate (before mutation)

Verify: HEAD equals `980db7af33910bb676eef46ed89fd2b453112bb6` (this
exchange's authorized baseline), porcelain clean, branch
`feat/x-meme-browser-companion`, `.ap` gitlink unchanged,
`./.ap/ap ap doctor` PASS. Stop on any unexplained difference.

## Slice 2 deliverables (binding design)

### D1 — Golden fixture (exact bytes)

Create `src/framenest/infrastructure/ai/fixtures/__init__.py` (empty package
marker) and `src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png`
with exactly these bytes, materialized with exactly this authorized command:

```text
printf '%s' 'iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAIAAABLbSncAAAAEUlEQVR42mP4z8CAFTEMLQkAKP8/wc53yE8AAAAASUVORK5CYII=' | base64 -d > src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png
```

The result MUST be 74 bytes with
SHA-256 `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44`
(valid 8x8, 8-bit, color-type 2 PNG, solid RGB(255,0,0)). Verify size and
hash with `stat`/`sha256sum` read-only commands and record them in the report.
Add an explicit include entry for the PNG to `pyproject.toml` alongside the
existing explicit `include` list so the wheel carries it.

### D2 — `src/framenest/infrastructure/ai/vision_probe.py` (new)

- `VISION_PROBE_PROMPT = "What color is this? Answer with one word."` and
  `VISION_PROBE_PROMPT_VERSION = "framenest-vision-probe-v1"`.
- `load_vision_probe_fixture() -> bytes` through `importlib.resources` from
  the `framenest.infrastructure.ai.fixtures` package; no filesystem path
  assumptions.
- `EXPECTED_COLOR = "red"`.
- `match_expected_color(text: str) -> tuple[bool, str | None]`: returns
  `(matched, observed_token)`. Normalization: Unicode lowercase, strip
  control characters, replace punctuation with spaces, collapse whitespace,
  bound the token window to <= 32 characters. `observed_token` is the bounded
  normalized token when the completion is non-empty, else `None`. `matched`
  is true only when the normalization matches the accepted set exactly:
  `red`, `crimson`, `scarlet`, `vermillion`, `červená`, `cervena`,
  `#ff0000`, `ff0000`. No fuzzy matching. Empty, unparseable, or other colors
  (for example `blue`) are a `mismatch`, never an error.
- Sidecar state: path `<config_path.parent>/vision-probe-state.json`, body
  `{schema_version, provider_id, model_id, status, matched, observed_color,
  probed_at_ms}` with `schema_version = 1`; `observed_color` only the bounded
  token or `null`; atomic write, 0600, symlink refusal, reuse the existing
  config write helpers' posture (a small local helper is fine). Reading is
  fail-safe: malformed or mismatched provider/model state is treated as
  absent, never as a crash.
- Statuses: `success`, `mismatch`, `authentication_failed`,
  `rate_limited_or_quota_exhausted`, `model_unavailable`,
  `provider_unreachable`, `invalid_response`, `provider_error`.
- Raw completion text is NEVER persisted, logged, or printed; only the
  bounded token.

### D3 — `src/framenest/infrastructure/ai/activity_lock.py` (new)

Small shared helper wrapping the existing `.test.lock` pattern (exclusive
`O_CREAT|O_EXCL` create, 0600, explicit release and unlink). Binding decision:
`ai test` keeps the `.test.lock` path and behavior (refactored through the
helper); `ai vision-probe` uses `.vision-probe.lock`. Busy -> sanitized
failure (CLI exit 2, message `Another AI provider operation is already
running.`). Admin-side mutual exclusion is a slice-4 concern.

### D4 — Generic adapter probe path

In `src/framenest/infrastructure/ai/openai_chat_completions.py`:

- `build_chat_completions_vision_probe_body(*, model_id, prompt, image)` —
  one image as an `image_url` JPEG data URL (encode the PNG fixture through
  the existing `PillowVlmImageDerivativeEncoder.encode_png_bytes`), the fixed
  prompt as the text part, `stream: false`, `temperature: 0`, small
  `max_tokens`, no `response_format`.
- `OpenAiChatCompletionsMediaSuggestionProvider.probe_vision(*, prompt,
  image_png) -> str` reusing the existing bounded single-call and error
  mapping (`403 -> MediaSuggestionProviderAuthError`, and so on).

### D5 — NVIDIA probe path

Add `probe_vision(*, prompt, image_png) -> str` to
`NvidiaNimMediaSuggestionProvider` using the shared probe body and its
existing decode path, with the same error mapping as its `test_connection`.
`nvidia_nim.py` is allowlisted only for this addition; do not alter its
suggestion, polling, or movie-identification behavior.

### D6 — CLI `vision-probe`

In `src/framenest/adapters/cli/ai.py`:

```text
framenest-ai vision-probe [--confirm-cloud-upload]
```

Flow: require `--confirm-cloud-upload` (else `AI vision probe:
confirmation_required`, exit 2); resolve the active provider; refuse a
selected model whose declared capabilities lack `vision_input` (sanitized
`AI vision probe: unsupported_model_capability`, exit 2); acquire
`.vision-probe.lock`; load the fixture; call the provider's `probe_vision`;
judge; persist the sidecar; print sanitized lines only (`AI vision probe:
success|mismatch|...`, `Expected color: red`, `Observed color: <bounded
token or none>`); exit 0 on `success`, 2 otherwise. If the provider is
unconfigured or the credential is unavailable, use the existing sanitized
messages and exit 2. No key, Authorization header, base64 payload, raw
completion, absolute path, or database path may appear in output.

## Binding synthesis decisions

1. Per-operation locks (`.test.lock` for test/ping, `.vision-probe.lock` for
   pong) via the shared helper; UI-level mutual exclusion lands in slice 4.
2. The judge accepts Slovak tokens; the prompt stays English.
3. `observed_color` stores the bounded normalized token (<= 32 chars) or
   `null` — never raw completion text.

## Exact changed-path allowlist

```text
src/framenest/infrastructure/ai/vision_probe.py (new)
src/framenest/infrastructure/ai/activity_lock.py (new)
src/framenest/infrastructure/ai/fixtures/__init__.py (new)
src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png (new, exact bytes)
src/framenest/infrastructure/ai/openai_chat_completions.py
src/framenest/infrastructure/ai/nvidia_nim.py
src/framenest/adapters/cli/ai.py
pyproject.toml
tests/unit/infrastructure/ai/test_vision_probe.py (new)
tests/unit/infrastructure/ai/test_openai_chat_completions.py
tests/unit/infrastructure/ai/test_nvidia_nim.py
tests/unit/adapters/cli/test_ai_cli.py
tests/contract/test_ai_package_resources.py (new)
```

No other file may be created, edited, deleted, or moved.

## Tests

1. `test_vision_probe.py` (new): judge table (`red`, `Crimson.`, `scarlet`,
   `vermillion`, `červená`, `cervena`, `#ff0000`, `ff0000` -> matched;
   `blue`, `not sure`, empty, oversized/injection-ish text -> not matched,
   bounded token or None); fixture presence, 74-byte size, dimensions, and
   pinned SHA-256; sidecar round-trip, atomically written, provider/model
   filtering, malformed-state fail-safe.
2. `test_openai_chat_completions.py` (edit): probe request body (single image
   data URL, fixed prompt, temperature 0, no `response_format`), error
   mapping for probe, one call per invocation.
3. `test_nvidia_nim.py` (edit): one focused `probe_vision` test with the fake
   transport; do not weaken existing tests.
4. `test_ai_cli.py` (edit): `vision-probe` confirmation required, success,
   mismatch, unsupported-model capability refusal, busy lock, unconfigured
   provider, and sanitized output (no raw completion).
5. `test_ai_package_resources.py` (new): the fixture is loadable through
   `importlib.resources` and present in a built wheel, modeled on
   `tests/contract/test_web_package_resources.py`.

Validation ladder:

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the named suites above
Affected tests: tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py
New causal regression: the fixture/judge/sidecar/probe path has no prior coverage; the CLI pong has no prior coverage
Broad or full suite: not-used — no project rule or named decision risk requires it for this slice
Runtime or testbed: not-used
Independent acceptance: not-required
```

## Commands (canonical execution route — binding)

```text
./.ap/ap ap project check --root /home/agile/Projects/framenest --baseline 980db7af33910bb676eef46ed89fd2b453112bb6
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline 980db7af33910bb676eef46ed89fd2b453112bb6 --operation runtime-info
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline 980db7af33910bb676eef46ed89fd2b453112bb6 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_package_resources.py -q -p no:cacheprovider
```

Plus the one exact fixture-materialization command in D1 and read-only
`stat`/`sha256sum` verification of it.

## Authority

Positive: edit/create only the allowlisted paths; the exact fixture command;
the declared AP route; read-only Git; stage exactly the allowlisted paths;
one local commit with subject
`Add vision probe fixture, judge, and CLI pong`; no push; the single Meta
report below.

Negative: everything outside the allowlist; any HTTP route, `application.py`,
UI/frontend, extension, or documentation change; any other Git write; any
provider/network call; NUC/SSH/sudo/browser/GUI; ambient Python, `poetry run`,
`pip`, `uv`, environment reconstruction; secret access; `git add .`/`-A`; no
weakening or deleting existing tests.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_03.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 02`, `Worker exchange ordinal: 03`); compact
core: status; phase-qualified result `implementation-PASS` on PASS else
`not-applicable`; start commit `980db7a…`; end commit; changed files; tests
and validation with exact counts; fixture size and SHA-256; commit result;
deviations/risks; one smallest next step; `Report justification: new-mutation`;
authority-expiry statement; `Orchestration critique` (MEASURED/LEAD);
Resolved Execution Issues / Near-Misses and Pre-Existing Failure
Classification; `Logical-whole closure: not-closed`. Save, read back fully,
verify identity, then a short separate completion notice with location and
SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails unclassifiably, a needed
change exceeds the allowlist, the fixture bytes cannot be reproduced exactly,
an existing test contract must be weakened, the execution route is unusable,
the Meta destination is occupied or unsafe, or retained context conflicts
with repository evidence.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.
