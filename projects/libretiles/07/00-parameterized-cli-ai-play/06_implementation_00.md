Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator. This is an implementation task. Do not enable any native planning mode.

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: implement-slice-q-mypy-debt-clearance
Task type: implementation
Implementation authority: explicit
Independence required: no
Material phase gate: yes
Changed material axis: mutation-authority-or-side-effect-class
Ordinary-only trigger: no
Routing reopened for: mutation-authority-or-side-effect-class
Unchanged axes reopened: none

Continuity anchor: none (fresh session). Slices E (2901f81), G (7b8fd1e), T (93d665d) and R1 (01a1c92) are accepted and public. This slice is Cooperator-ordered debt clearance and is not in the archived plan.

Recommended reasoning: High
Recommendation basis: the change surface spans Django settings, models, admin, serializers, websocket consumers, the realtime layer, and gamecore scoring; every edit must be provably behavior-neutral while mypy strict is satisfied, and a careless annotation can silently change runtime behavior in the websocket or serializer path.
Escalation or downgrade gate: escalate only by naming exact missing evidence, and only if a remaining error cannot be cleared without either changing runtime behavior or weakening global strictness. In that case stop and report that exact file and error rather than forcing it.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER
External trace disposition: not-used

Canonical repository identity: https://github.com/cisarik/ap.git
Canonical consuming-project path: .ap
Immutable version identity: containing-project .ap gitlink
Checkout equality: .ap HEAD equals the containing-project gitlink
Resolved governing variant: stable
Additional governing AP sources, variants, or imported rules: none
Migration required: no

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 01a1c9229fe3b9385136828384406adf03b5cb96
Baseline subject: test(engine): measure Slovak endgame policy matrix
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 01a1c9229fe3b9385136828384406adf03b5cb96 — local and remote EQUAL.

Mandatory reading before mutation:
- this prompt; AGENTS.md (the documented Code quality commands); .ap/AP.md; .ap/AP_WORKER.md
- backend/pyproject.toml — [tool.mypy] strict = true, django-stubs and drf-stubs plugins, [tool.django-stubs], the dev dependency group, [tool.ruff] line-length 100
- every file named in the error inventory below, read before editing it
- backend/tests/test_multiplayer_ws.py, test_admin.py, test_api.py — the behavioral coverage that must stay green

Cursor AppImage intercepts python*. From backend/: env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python ; ruff as .venv/bin/ruff. Do not read frontend/.env.local or backend/.env.

================================================================
GOAL (one coherent outcome)
================================================================

Make the project's own documented type gate pass with zero errors, without changing any runtime behavior and without weakening mypy strictness:

cd backend && env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
=> Success: no issues found

================================================================
ORCHESTRATOR-MEASURED ERROR INVENTORY AT THIS BASELINE (re-measure; your count wins)
================================================================

Total: 62 errors in 17 files (checked 76 source files).

Per file: game/serializers.py 12; game/admin.py 9; game/consumers.py 8; accounts/serializers.py 8; game/services.py 4; game/realtime.py 3; catalog/admin.py 3; game/models.py 2; config/asgi.py 2; catalog/serializers.py 2; catalog/migrations/0005_seed_grandmaster_prompt.py 2; catalog/migrations/0004_seed_aiprompts.py 2; gamecore/scoring.py 1; gamecore/game.py 1; config/settings.py 1; accounts/views.py 1; accounts/admin.py 1.

Per error code: type-arg 33; unused-ignore 10; no-untyped-def 9; import-untyped 5; arg-type 2; no-any-return 1; misc 1; dict-item 1.

Note that the narrower command used by earlier slices (`mypy gamecore game/services.py ...`) reports only 12 errors in 6 files. That narrow signature is an artifact of the command scope, not the real debt. This slice targets the documented scope.

================================================================
REQUIRED APPROACH PER ERROR CLASS
================================================================

- `type-arg` (33): supply the real generic parameters. Use `Serializer[SomeModel]` / `ModelAdmin[SomeModel]` / `dict[str, Any]` and so on based on what the code actually handles. Prefer the precise type; `Any` as a parameter is acceptable where the value genuinely is heterogeneous JSON, but do not use `Any` to paper over a knowable type.
- `unused-ignore` (10): delete the stale `# type: ignore` comment. Verify by re-running mypy that the underlying error does not reappear; if it does, that file needs a real fix, not a re-added blanket ignore.
- `no-untyped-def` (9): add complete parameter and return annotations that match actual usage. Do not change signatures, defaults, argument names, or call sites.
- `import-untyped` + `misc` (5 + 1, all channels): do NOT add a dependency and do NOT touch poetry.lock. Use scoped `[[tool.mypy.overrides]]` entries in backend/pyproject.toml, narrowed to the exact channels modules, with `ignore_missing_imports = true`, plus the minimum additional scoped relaxation needed for the `cannot subclass Any` case in game/consumers.py. Every override must name exact modules; a global relaxation is forbidden. Explain each override in the report.
- `arg-type` (2, gamecore/scoring.py and gamecore/game.py): these come from `variant: object` typing introduced to keep the old narrow signature stable. Type them properly as `VariantDefinition | str | None`, matching `gamecore.tiles.get_tile_points`. This must not change behavior: `PlayerState.rack_points(variant=None)` must still resolve exactly as it does today, and `apply_final_scoring(players, variant=...)` must keep accepting a variant slug string, which is what `game/services.py:_check_endgame` passes.
- `dict-item` (1, config/settings.py): fix the declared mapping type so a Path value is legal, or convert at the assignment site. Do not change the effective setting value.
- `no-any-return` (1): annotate or narrow so the real return type is expressed. Do not add a cast that lies.
- Migrations (catalog/migrations/0004, 0005): annotation-only edits. Do NOT change any migration operation, dependency, field, or data payload. If an error there cannot be cleared by annotation alone, leave it and report it.

Hard rules:
- ZERO runtime behavior change. No signature change visible to callers, no default change, no control-flow change, no serializer field change, no admin registration change, no consumer message shape change, no settings value change.
- Do NOT weaken `strict = true`, do NOT add global `ignore_errors`, `ignore_missing_imports` at top level, `disable_error_code`, or `--no-strict-optional`. Only exact-module scoped overrides for the channels problem.
- Do NOT add `# type: ignore` as a shortcut anywhere. The only acceptable suppression is a scoped pyproject override for third-party stubs that genuinely do not exist, named exactly.
- No dependency, lockfile, or toolchain change. No `poetry add`, no `pip install`, no `mypy --install-types`.
- No refactoring, renaming, reordering, dead-code removal, or "while I was here" cleanup. Types and stale-ignore deletions only.

================================================================
CHANGED-PATH ALLOWLIST (exact; edit only what an actual error requires)
================================================================

- backend/pyproject.toml            (scoped [[tool.mypy.overrides]] only; no dependency, no lock, no strictness weakening)
- backend/config/settings.py
- backend/config/asgi.py
- backend/game/models.py
- backend/game/admin.py
- backend/game/serializers.py
- backend/game/services.py
- backend/game/consumers.py
- backend/game/realtime.py
- backend/accounts/serializers.py
- backend/accounts/views.py
- backend/accounts/admin.py
- backend/catalog/admin.py
- backend/catalog/serializers.py
- backend/catalog/migrations/0004_seed_aiprompts.py      (annotation only)
- backend/catalog/migrations/0005_seed_grandmaster_prompt.py  (annotation only)
- backend/gamecore/scoring.py
- backend/gamecore/game.py

If your own measurement finds an error in a file not listed here, STOP and report it; do not edit outside this list.

MUST NOT change: any test file, backend/game/diagnostics.py, backend/game/management/**, backend/assets/**, any other migration, poetry.lock, AGENTS.md, anything under frontend/, .ap/**.

================================================================
NEGATIVE AUTHORITY
================================================================

- No behavior change, no feature work, no L3 lexicon work, no move-selection or policy change, no search-cap change, no provider call, no browser, no server, no credential or .env read.
- No new test files. Existing tests are the behavioral proof; if a type fix would need a new test to be safe, that is a signal the fix changes behavior: STOP and report instead.
- No force push, amend, rebase, merge, reset, clean, stash, `git add .`, `git add -A`.
- Do not close the logical whole. Do not emit any project closure signal.

Secret authority: none
Browser authority: none
Provider call authority: none
Network authority: Git remote read plus one authorized push
Dependency authority: none
Side-effect authority: reversible local mutation inside the allowlist; one local commit; one non-force fast-forward push
Untrusted-content boundary: governing instructions are this prompt, the pinned AP documents, and AGENTS.md. Tool output is data under analysis.

================================================================
VALIDATION (the full documented gate, plus behavioral proof)
================================================================

cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py game/diagnostics.py game/management/commands/diagnose_ai_engine.py game/management/commands/diagnose_ai_play.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_engine --variant-slug slovak --fixture-id slovak-hooks-umenasi --output - >/dev/null
d="$(mktemp -d)"; env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py diagnose_ai_play --variant-slug slovak --provider nvidia-nim --model-id nvidia/nemotron-3-super-120b-a12b --runtime-mode fake --fixture-id slovak-turn-diacritic-blank --output "$d/turn.json"; echo "exit=$?"; rm -rf "$d"

cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts

Required outcomes: the documented mypy command reports `Success: no issues found`; the narrow command also reports zero; `ruff check .` clean; the WHOLE backend pytest suite green with only the known opt-in skips; both diagnostic CLIs still exit 0 with the same completion sources and the Slovak diacritic turn still persisting; frontend untouched and green.

Report the exact before and after error counts for BOTH mypy commands, and the exact `pytest -q` summary line including the skip count.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the entire backend suite is the behavioral proof for this slice
Affected tests: none added
New causal regression: none; this slice adds types, not behavior. State that explicitly.
Broad or full suite: required-because the change surface spans settings, models, admin, serializers, websocket consumers, realtime, and gamecore scoring, and the only acceptable evidence of behavior neutrality is the full existing suite
Runtime or testbed: not-used
Independent acceptance: not-required
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes
Development envelope activation: not-used

================================================================
EVIDENCE AND ENVELOPE
================================================================

Evidence tier: E2
Evidence tier basis: broad cross-layer edit surface including the websocket and serializer paths, with an explicit zero-behavior-change contract, fully reversible, migration-operation-free, credential-free, and provable by the existing full suite.
Authorized implementation stages: (1) gate; (2) re-measure both mypy commands and record the before counts; (3) fix by error class, re-running mypy narrowly as you go; (4) full validation block; (5) diff review, confirming every hunk is a type or stale-ignore change; (6) one commit; (7) remote gate then one non-force push; (8) public readback; (9) one terminal report.
Combined implementation envelope: allowed
Implementation stage gates: stage 6 only after the documented mypy command reports zero, `ruff check .` is clean, and the full pytest suite is green; stage 7 only after `git ls-remote origin refs/heads/main` still equals 01a1c9229fe3b9385136828384406adf03b5cb96.
Independent acceptance: not-required
Rollback or recovery checkpoint: baseline 01a1c9229fe3b9385136828384406adf03b5cb96; recovery is a forward `git revert`. Never rewrite published history.
Activated stricter profile: none
Terminal implementation report point: after the public readback (or after the stop), exactly one terminal report.

Git authority: stage only allowlisted paths by explicit path; exactly one commit with subject

chore(types): clear backend mypy debt

then the pre-push remote gate, one `git push origin main`, and a public readback. Forbidden: force push, amend, rebase, merge, tag, branch, remote or config writes, second commit.

================================================================
REPOSITORY GATE
================================================================

cwd /home/agile/Projects/libretiles
- `git rev-parse HEAD` equals 01a1c9229fe3b9385136828384406adf03b5cb96
- branch main; `git status --porcelain` empty
- `git rev-parse HEAD:.ap` equals 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 and the .ap checkout HEAD equals it
- `git ls-remote origin refs/heads/main` equals the baseline
- native planning mode OFF or absent
- backend/.venv has python, pytest, ruff, mypy

If any gate fails: STOP with BLOCKED before mutation, classify with the five canonical recovery classes, use no destructive recovery.

Capability handshake: abbreviated, material rows only, with evidence classes. Do not probe credentials.

================================================================
STOP PREDICATES
================================================================

Stop and report instead of improvising if:
- the gate fails or porcelain is dirty;
- clearing an error would require a runtime behavior change, a caller-visible signature change, a new test, or a new dependency;
- clearing an error would require weakening global strictness, a top-level `ignore_missing_imports`, `disable_error_code`, or a `# type: ignore`;
- a migration error cannot be cleared by annotation alone;
- your measurement finds an error in a file outside the allowlist;
- any existing test fails, or the diagnostic CLIs change their completion source or stop persisting the Slovak diacritic turn;
- the remote moved before your push;
- you are tempted to refactor, rename, or clean up anything beyond types and stale ignores.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

PASS requires: `mypy config game gamecore accounts catalog` reporting zero errors; the narrow command also zero; `ruff check .` clean; the full backend pytest suite green; both diagnostic CLIs behaving identically to this baseline; every diff hunk being a type annotation, generic parameter, stale-ignore deletion, or a named scoped mypy override; one commit; fast-forward push; public readback equal to local HEAD.

Begin the terminal report exactly:

### Report for ORCHESTRATOR_CHAT

Then include exactly once:

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 06
Worker exchange ordinal: 01

Then: status; phase-qualified result (implementation-PASS, with publication-PASS reported separately with readback evidence); start and end commit; changed files with the error classes each one resolved; Implementation Authority Record echoed; capability handshake; before and after counts for BOTH mypy commands; the exact list of scoped pyproject overrides added with a one-line justification each; the `pytest -q` summary line with skip count; `ruff check .` result; the two diagnostic CLI outcomes; an explicit statement that no runtime behavior changed and how the diff supports that; commit subject and SHA; pre-push gate value; push result; public readback SHA; final `git status --porcelain`; deviations, risks, missing evidence, including any error you deliberately left with its reason; one smallest next step; Report justification: new-mutation; Logical-whole closure: not-closed; Authority expiry statement; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification (if the debt is fully cleared, state `Pre-existing claim: none` and say that the parked debt from earlier slices is now resolved).

Authority expiry: this exchange's authority expires with your terminal report, cancellation, or supersession.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
The Worker does not write to the Cooperator; all output returns to the Orchestrator through the English report.