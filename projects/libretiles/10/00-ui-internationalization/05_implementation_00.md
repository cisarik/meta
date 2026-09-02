You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S4 — the player stops choosing the AI model and the prompt preset
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — a behavioural change across eight files on the AI turn path,
  where one value must be REMOVED FROM THE UI while surviving as a resolved preference. Deleting it
  outright would silently break the fallback queue.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
1. REPOSITORY GATE
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Working-copy topology: canonical checkout.

  git rev-parse HEAD                     -> e0d3b64cbccf1a1d9983ba5c394762f55961325a
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> e0d3b64cbccf1a1d9983ba5c394762f55961325a

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — this Next.js version has breaking changes versus
   your training data. The installed docs ARE present at `frontend/node_modules/next/dist/docs/`.
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/hooks/useGameStore.ts — the two persisted fields and `partialize`
6. frontend/src/lib/ai-fallback.ts lines 80-130 — WHY `selectedModelId` cannot simply be deleted
7. frontend/src/lib/model-catalog.ts — `resolveEligibleModelId`
8. frontend/src/app/settings/page.tsx — in full
9. frontend/src/app/play/page.tsx — in full
10. frontend/src/app/game/[id]/page.tsx lines 455-630, 840-930, 1600-1625, 1795-1825
11. frontend/src/components/game/ScorePanel.tsx lines 255-300 and 410-435
12. backend/game/services.py lines 366-393 — READ ONLY. It is what makes this slice safe.

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
The player no longer chooses the AI model or the prompt preset. A player sees only the model's NAME.
The choice becomes admin-controlled through Django Admin, with no code change and no SSH.

This is the Cooperator's stated single most important product outcome. Treat it as such.

=====================================================================
4. WHY THIS IS SAFE — measured, so you do not have to rediscover it
=====================================================================
The backend already resolves both values when the frontend omits them. Verified by the Orchestrator
against the real source; do not change these files, just rely on them:

    backend/game/services.py:366-384  _resolve_ai_model
        `ai_model_model_id` omitted -> returns `selectable_models[0]`
    backend/game/services.py:386-393  _resolve_ai_prompt
        `ai_prompt_id` omitted      -> returns `selectable_prompts[0]`
    backend/game/serializers.py:174-175   BOTH fields are `required=False`
    backend/catalog/models.py         both catalogs order by ("sort_order", ...)
    backend/catalog/admin.py:43,:113  `sort_order` and `is_active` are `list_editable`

So omitting the fields makes the backend pick catalog row 1, and an administrator changes row 1 by
editing `sort_order` inline in Django Admin. **NO BACKEND CHANGE IS AUTHORIZED OR NEEDED.**

=====================================================================
5. THE TRAP: `selectedModelId` MUST SURVIVE, `selectedPromptId` MUST NOT
=====================================================================
⛔ Read this twice. Deleting `selectedModelId` would silently break the AI turn.

`selectedModelId` is not only a picker value. It is the **preference that becomes attempt 1 of the
provider fallback queue**:

    game/[id]/page.tsx:917   const preferenceModelId = selectedModelId || gameState.ai_model_id || ""
    lib/ai-fallback.ts:90-96 that preference selects the first pair in the queue

It therefore SURVIVES as a resolved value. What disappears is the player's ability to choose it and the
player-initiated write. Concretely:

    KEEP   the `selectedModelId` store field, its persistence, and `setSelectedModelId`
    KEEP   `resolveEligibleModelId(...)` resolution and its repair write-back at
           settings/page.tsx:474, play/page.tsx:123 and app/page.tsx:63. Those are automatic repair of a
           stale id, not the player choosing, and they keep the stored value consistent with the
           live catalog.
    KEEP   `ai_model_model_id: resolved` in the createGame call at play/page.tsx:188. The resolved id
           comes from the admin-set `preferred_ai_model_id` or from catalog row 1 — never from a click.
    REMOVE the selectable rival PANEL in settings, the per-row click handler, `savingModelId`, and the
           player-initiated `api.updateMe(...)` at settings/page.tsx:557.

`selectedPromptId` has no fallback-queue role. It is removed outright.

=====================================================================
6. EXACTLY WHAT TO CHANGE
=====================================================================

--- 6.1 settings/page.tsx — the rival panel becomes read-only ---
The selectable panel is the `SettingsPanel` block at roughly lines 668-774. Replace it with a
**read-only display of the active model's `display_name`** in the same panel styling, with no buttons,
no per-row selection, and no `onClick`. Keep the panel title and description keys.

Delete: `savingModelId` state, `handleSelectModel` (the function containing the `api.updateMe` at :557),
the `models.map(...)` selectable rows, and the `"No rival selected"` fallback string.

Keep: the `models` fetch, `resolveEligibleModelId`, `setSelectedModelId(resolved)` at :469, and the
repair `api.updateMe(...)` at :474. If the resolved model is not found in the catalog, show the panel's
empty-catalog wording that already exists in that file rather than inventing new copy.

--- 6.2 play/page.tsx — no "Choose AI" ---
`play/page.tsx:34` `if (!modelId) return "Choose AI";` and the `:69` fallback exist because the player
could have chosen nothing. After this slice the value is always resolved, so a "choose" prompt is wrong.
Show the catalog `display_name`; if the catalog has not loaded yet, show the existing loading wording in
that file. Do not invent new copy and do not add a new catalog key for a state that can no longer occur.

Remove `selectedPromptId` from the component and remove `ai_prompt_id: selectedPromptId ?? undefined`
from the `api.createGame` call at :189, so the backend picks prompt row 1.

--- 6.3 game/[id]/page.tsx — remove the prompt-preset surface ---
Remove: the `selectedPromptId` / `setSelectedPromptId` store reads at :464-465; the prompt-switch effect
at :586-625; `savingPromptId`; `handleOpenPromptsModal` and the `promptsModalOpen` state at :500; the
`promptPreview` state at :501; `effectivePromptId` at :1526; `activePromptLabel`; the
`PromptCatalogModal` and `PromptPreviewModal` imports at :30-31 and their mounts at :1801-1820; and the
`prompts` fetch if it becomes unused after the above.

Keep: everything about `selectedModelId`, including the model-switch effect at :561-583 and
`preferenceModelId` at :917.

⚠ `"Choose rival"` at :1522 and :1524 and `"Initial"` at :1513 are the fallbacks the earlier slice
deliberately left in English for you. `activeHeaderModelName` must now always resolve to a real name, so
the `"Choose rival"` fallback becomes unreachable — remove it rather than translating it. `"Initial"`
disappears with `activePromptLabel`. `"Could not switch AI prompt right now."` at :612 disappears with
the effect.

--- 6.4 ScorePanel.tsx — remove the prompt control ---
Remove the `showPromptPicker`, `promptLabel` and `onOpenPromptPicker` props (declarations at :261-266,
defaults at :282-287) and the control at :418-427 including the `"Prompt presets"` and `Prompt: {label}`
strings. Remove the matching props passed from game/[id]/page.tsx at :1613-1618.
Change NOTHING else in ScorePanel — its remaining copy is slice S5's, not yours.

--- 6.5 Delete the two picker components ---
`frontend/src/components/game/PromptCatalogModal.tsx` and
`frontend/src/components/game/PromptPreviewModal.tsx` are imported from exactly one place,
`game/[id]/page.tsx`, verified by the Orchestrator. Once that mount is gone they are dead code. Delete
both files. Do not leave an unused component in the tree — the project's artifact-hygiene rule is that
the live tree represents current usable knowledge.

--- 6.6 useGameStore.ts — remove `selectedPromptId` only ---
Remove `selectedPromptId` and `setSelectedPromptId` from the interface, the initial state, and
`partialize`. **Bump the persist `version` from 4 to 5** and add a `if (version < 5)` migrate branch that
deletes the stale `selectedPromptId` key from the incoming payload, in the exact style of the existing
branches.

⚠ This is the ONE authorized persist-version bump in this whole. Logical whole `11/01` shares this
store's versioning; a bump is justified here because a removed persisted key is exactly what `migrate`
exists for. Do NOT touch `selectedModelId`, `selectedVariantSlug`, `uiLocale`, or any other field.

--- 6.7 draw/[id]/page.tsx — stop showing a raw model id ---
`draw/[id]/page.tsx:178` renders `{selectedModelId}` in a mono font — an internal id such as
`nvidia/nemotron-3-super-120b-a12b` shown to a player. The Cooperator's decision is that a player sees
only the model's NAME. Render the catalog `display_name` for the resolved id, falling back to
`humanizeModelId(...)` which the project already uses for exactly this purpose. Keep the pill styling.

--- 6.8 THE TWO RIDERS from slice S3c, in files you already touch ---
These are user-facing English strings the previous slice reported and was not authorized to fix.

  RIDER 1  game/[id]/page.tsx:222
             Invalid Word{(toast.words?.length ?? 0) > 1 ? "s" : ""}!
           The big red heading on every invalid-word rejection, with the one-character English "s"
           pluralization. It needs a ONE/OTHER plural per locale, not the three-form helper, because no
           number is displayed. Add ONE parameterized key:

           game.toast.invalidWordHeading   params { count: number }
             en (p) => `Invalid Word${p.count > 1 ? "s" : ""}!`
             sk (p) => p.count > 1 ? "Neplatné slová!" : "Neplatné slovo!"
             cs (p) => p.count > 1 ? "Neplatná slova!" : "Neplatné slovo!"
             pl (p) => p.count > 1 ? "Nieprawidłowe słowa!" : "Nieprawidłowe słowo!"

  RIDER 2  game/[id]/page.tsx lines 90, 93, 98, 99 in `getStreamStartError` — four
           `AI route failed (${response.status})` variants, surfaced to the player through
           "Last error: {aiError}". Add three parameterized keys and one plain one:

           game.ai.routeFailed          params { status: number }
             en (p) => `AI route failed (${p.status}).`
             sk (p) => `Volanie AI zlyhalo (${p.status}).`
             cs (p) => `Volání AI selhalo (${p.status}).`
             pl (p) => `Wywołanie AI nie udało się (${p.status}).`
           game.ai.routeFailedBeforeStream   params { status: number }
             en (p) => `AI route failed (${p.status}) before the stream started.`
             sk (p) => `Volanie AI zlyhalo (${p.status}) ešte pred začiatkom streamu.`
             cs (p) => `Volání AI selhalo (${p.status}) ještě před začátkem streamu.`
             pl (p) => `Wywołanie AI nie udało się (${p.status}) przed rozpoczęciem streamu.`
           game.ai.routeFailedWithPreview    params { status: number; preview: string }
             en (p) => `AI route failed (${p.status}): ${p.preview}`
             sk (p) => `Volanie AI zlyhalo (${p.status}): ${p.preview}`
             cs (p) => `Volání AI selhalo (${p.status}): ${p.preview}`
             pl (p) => `Wywołanie AI nie udało się (${p.status}): ${p.preview}`

           ⚠ `getStreamStartError` is a plain async function outside any component, so it has no hook.
           Pass the resolved locale or the resolved strings in from the caller. Do NOT add a
           module-level mutable locale and do NOT call a hook conditionally. If the cleanest shape is to
           give the function a `locale: Locale` parameter, do that.

  RIDER 3  frontend/src/lib/i18n/messages.en.ts:190-193 — `aiPassBodyKey` declares
           `message?: string` and never reads it. Dead API surface kept only so a test could pass a
           title through, and mildly ironic given that helper exists to STOP keying on `message`.
           Delete the field and adjust the test to stop passing it.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/app/settings/page.tsx
  frontend/src/app/play/page.tsx
  frontend/src/app/game/[id]/page.tsx
  frontend/src/app/draw/[id]/page.tsx
  frontend/src/components/game/ScorePanel.tsx
  frontend/src/hooks/useGameStore.ts
  frontend/src/hooks/useGameStore.test.ts
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts
DELETE:
  frontend/src/components/game/PromptCatalogModal.tsx
  frontend/src/components/game/PromptPreviewModal.tsx

If a gate fails in a file NOT on this list, STOP and report it rather than editing that file.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
⛔ NO DATABASE CHANGE AND NO BACKEND CHANGE OF ANY KIND. This is an explicit Cooperator decision and it
is the load-bearing constraint of this slice. Specifically KEEP, untouched:
  `accounts.User.preferred_ai_model_id` and its migrations
  its Django admin field
  its `is_selectable_model` validation in `accounts/serializers.py:52-55`
  `backend/game/serializers.py` and `backend/game/services.py`
  `backend/catalog/` in its entirety
  `api.updateMe` in `frontend/src/lib/api.ts` and the `preferred_ai_model_id` field on `UserProfile`
The field becomes admin-settable-only by ceasing to be WRITTEN from a player click. It is not removed.

- Do NOT remove `selectedModelId` from the store, from `ai-fallback.ts`, or from
  `game/[id]/page.tsx:917`. Section 5 explains why. Removing it breaks the AI turn.
- Do NOT touch `frontend/src/lib/ai-fallback.ts`, `model-catalog.ts`, `ai-move-stream.ts`,
  `ai-runtimes.ts`, or any file under `frontend/src/app/api/`.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md. This slice does
  NOT add, remove, rename, or reorder any provider or model. Verify that and say so in the report.
- frontend/src/lib/prompts.ts, its pinned SHA-256, MOVE_PROMPT_VERSION, and the AI move and judge
  routes. Locked fork 2. Removing the player's PROMPT PICKER does not touch the MOVE CORE prompt; those
  are different things and must not be confused.
- frontend/src/lib/constants.ts — TW/DW/TL/DL is the BOARD, not copy.
- frontend/src/lib/api.ts. Its 401 branch is a security property.
- frontend/src/proxy.ts, security-headers.ts. The nonce CSP is a later slice.
- frontend/src/lib/i18n/locales.ts, plural.ts, translate.ts, LocaleProvider.tsx, index.ts.
- ScorePanel's remaining copy, GameHistoryPanel, GameHistoryModal, ProfileModal, AIThinkingOverlay,
  and the settings copy remainder. Slice S5 owns all of it. You remove the prompt CONTROL from
  ScorePanel and nothing else.
- Do NOT add a locale to any Intl.DateTimeFormat call, and do NOT add aria-label, role, or alt.
- frontend/package.json and package-lock.json. NO new dependency.
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits.

=====================================================================
9. COMMANDS AND EXECUTION ROUTE
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build.
Allowed, from backend/: the four gates below, ONLY via the bounded deviation, to prove you did not break
  the backend. You are NOT authorized to change any backend file.

BOUNDED EXECUTION DEVIATION, mandatory and task-specific.
  Declared route that could NOT be used: `poetry run ...`, as documented in AGENTS.md.
  Why: the Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
  Exact alternate, from backend/:
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
  Evidence class: reproduced-dynamic. Bounded authority: these four commands only.
  Stopping condition: if the alternate route also fails to resolve the in-project virtualenv, STOP and
    report; do not substitute ambient python, python3, or poetry run.

TRAP: `addopts = "-q"` is set. Do NOT pass another `-q`; use plain `-m pytest` and quote the summary.
TRAP: run mypy on the FULL documented scope.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. `npm run build` and `npm run dev` share
`frontend/.next`. Immediately before `npm run build`, and not before, run `ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, which are all safe with a dev server live. Leave the completed candidate
    UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss` output with the PID, and state that the
    only remaining action is the build gate plus the commit.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`. That pattern matches the Cooperator's
  own development server. You may kill nothing in this slice.
Name the route you took and quote the `ss` output that decided it.

Forbidden commands: any git write beyond section 11, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote`
  reads, any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: cross-cutting reversible change across eight files on the AI turn path, user-visible,
  removes a player capability, bumps a shared persisted schema version; no trust boundary, no durable
  server data, no credential, no production effect. Rollback is `git revert` of one commit plus a
  localStorage migration that already tolerates the old shape.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned and the Orchestrator will request it as batch B20.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/hooks/useGameStore.test.ts, frontend/src/lib/i18n/i18n.test.ts
New causal regression: the persist migration and the two riders
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `374 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

⚠ The vitest count may LEGITIMATELY DROP if a deleted component had its own tests. If it drops, state
exactly which tests were removed and why, and confirm that no surviving test was weakened. A drop with an
accounting is fine; a drop without one is not.

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-PERSIST-5   A persisted v4 payload containing `selectedPromptId` migrates to v5 with that key
                 ABSENT, and `selectedModelId`, `selectedVariantSlug` and `uiLocale` all preserved
                 unchanged. This is the regression test for the one authorized version bump.
  AC-MODEL-KEPT  `selectedModelId` is still a persisted field and still round-trips. Assert it
                 explicitly, because the whole risk of this slice is deleting it by accident.
  AC-HEADING-4   `game.toast.invalidWordHeading` renders the singular form at count 1 and the plural
                 form at counts 2 and 5, in all four locales. Assert the exact Slovak strings
                 "Neplatné slovo!" and "Neplatné slová!".
  AC-ROUTEFAIL-4 The three `game.ai.routeFailed*` keys render with a status interpolated, in all four
                 locales, and none of them contains the English words "route failed" in sk, cs or pl.
  AC-EXHAUST4    ALREADY EXISTS and must keep passing. Do not weaken it.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, EXCEPT for tests of a
component this slice deletes. If you remove a test file, it must be only because its subject no longer
exists, and you must say so explicitly.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and exactly one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only, including the two deletions. `git add -A` and `git add .` are
     FORBIDDEN. Use `git rm` for the two deleted files.
  2. Commit message, first line exactly:
       feat(ui): the player no longer chooses the AI model or the prompt preset
     Body: that the model and prompt defaults now come from Django Admin catalog row 1 with no backend
     change, that `selectedModelId` survives as the resolved fallback preference, that
     `preferred_ai_model_id` and its validation are untouched, the persist bump 4 -> 5, and that no
     dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     e0d3b64cbccf1a1d9983ba5c394762f55961325a. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; removing the prompt surface appears to require a backend change; you conclude
`selectedModelId` must be removed; you cannot bump the persist version without touching another field;
`getStreamStartError` cannot receive a locale without a module-level mutable or a conditional hook; you
conclude a new dependency is required; the backend gates fail; `git ls-remote` shows main advanced; any
instruction here conflicts with AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself
weakening a test whose subject still exists.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 05, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the two deleted files
 7. AN EXPLICIT AUDIT that `selectedModelId` survives: quote the store field, the `partialize` entry,
    `game/[id]/page.tsx:917`, and confirm `ai-fallback.ts` is untouched
 8. AN EXPLICIT AUDIT that no backend file, no migration, no `preferred_ai_model_id` declaration, and no
    `is_selectable_model` validation changed. Quote `git diff --name-only` scoped to `backend/` as proof
    that it is empty.
 9. AN EXPLICIT LOCKED-FORK STATEMENT: confirm that no provider or model was added, removed, renamed, or
    reordered anywhere, and that prompts.ts and its pinned hash are untouched
10. the persist migration: the new branch, and what a stored v4 payload becomes
11. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
12. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts. If the vitest count dropped, account for every
    removed test.
13. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
14. ANY user-facing English string still left in the files you touched. List them exactly. Two previous
    slices left strings behind because an Orchestrator inventory was incomplete, and this report field is
    the structural defence that caught it both times.
15. deviations, risks, or missing evidence — including anything you noticed but were not authorized to
    fix. Name it; do not fix it.
16. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
17. Pre-Existing Failure Classification: none | <complete classification>
18. one smallest next step or review request
19. report justification: new-mutation
20. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.
