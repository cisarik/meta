You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 04
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S3c — localize the game screen, correct two defects it exposes, and finish the board
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis unchanged — the largest file in this whole and two behavioural
  corrections rather than pure string extraction.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
0. CONTINUITY, AUTHORITY RENEWAL, AND WHY THIS EXCHANGE EXISTS
=====================================================================
Continuity anchor: your terminal BLOCKED report for Worker session 04, exchange 01, which returned
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` because TCP port 3000 was held by
  `next-server (v16.3.4)` pid 67401.

Prior authority: EXPIRED with that report. This prompt grants complete new bounded authority. Retained
context from exchange 01 is convenience, not authority. Evidence from this session is
NON-INDEPENDENT.

**You blocked correctly and this exchange exists because the Orchestrator's prompt was wrong, not
because your judgement was.** Verified independently: pid 67401 was a child of
`next dev --webpack` pid 67389, alive 41 minutes, alongside Django on port 8000 pid 67368 — both the
Cooperator's own processes. He had started them because the Orchestrator asked him to run an acceptance
batch in the product, and the Orchestrator then issued an implementation slice that forbids exactly that
state without asking him to stop first. That is an Orchestrator sequencing defect. Your working copy was
left byte-clean at the baseline, which the Orchestrator confirmed: HEAD, `ls-remote`, and an empty
porcelain all match.

TWO THINGS CHANGE IN THIS EXCHANGE. Everything else is reaffirmed unchanged.

  CHANGE 1  The port-3000 condition is now SCOPED TO THE BUILD GATE ONLY. It is no longer a preflight
            stop condition. Do the implementation and every gate that does not touch `frontend/.next`
            regardless of what is listening on 3000.
  CHANGE 2  A PRE-AUTHORIZED FALLBACK now exists for the case where the port is still occupied when you
            reach the build gate, so this slice cannot consume a third exchange doing nothing. See
            section 3.

The Cooperator has been asked to stop his dev server. Verify the port yourself rather than assuming he
did; both outcomes are now handled.

=====================================================================
1. REPOSITORY GATE — unchanged, re-run it
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main

  git rev-parse HEAD                     -> e421c6690f091203a60636b3aebaeec71e7fba69
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> e421c6690f091203a60636b3aebaeec71e7fba69

STOP if any value disagrees. A non-empty porcelain now would mean something mutated the tree between
your two exchanges and must be classified before any edit, not cleaned.

=====================================================================
2. CONTINUITY VERIFICATION — three exact strings, and STOP if you cannot produce them
=====================================================================
The complete authored string table is section 7 of your exchange-01 prompt and is UNCHANGED. It remains
authoritative for this exchange. Because a compaction could have dropped it from your context, prove you
still hold it by echoing these three values verbatim in your report before you begin:

  1. the Czech value of `game.lexicon.czech`
  2. the Polish value of `game.toast.aiExchanged`
  3. the Slovak value of `game.status.yourTurn`

If you cannot reproduce all three exactly from your retained context, STOP and report that the string
table is no longer available. The Orchestrator will reissue it in full. Do NOT reconstruct, re-translate,
or approximate a single string — translation is Orchestrator work in this project by Cooperator decision
and an invented Slavic string would be a silent product defect.

=====================================================================
3. THE BUILD GATE, AND THE PRE-AUTHORIZED FALLBACK
=====================================================================
`npm run build` and `npm run dev` share `frontend/.next`. Running the build while a dev server is live
risks corrupting that directory and breaking a server the Cooperator is using.

Immediately before `npm run build`, and not before:

    ss -tlnp | grep :3000

PRIMARY ROUTE — nothing is listening. Run `npm run build`, complete all eight gates, then commit and
push under section 6.

PRE-AUTHORIZED FALLBACK ROUTE — something is still listening. Take this route WITHOUT stopping and
WITHOUT asking:
  - do NOT kill the process, do NOT run `npm run build`, do NOT touch `frontend/.next`;
  - run and report the other SEVEN gates, all of which are safe with a dev server live:
      backend mypy, ruff, manage.py check, pytest; frontend typecheck, vitest, lint;
  - leave the completed candidate UNCOMMITTED in the working copy. Do not commit and do not push,
    because the standing rule is that all eight gates must be green before the commit;
  - report `status: PARTIAL`, list every changed path, and quote the exact `ss` output naming the PID
    and the process that held the port;
  - state explicitly that the candidate is uncommitted and that the only remaining action is the build
    gate plus the commit.

⛔ NEVER use a broad pattern kill such as `pkill -f next-server` or `pkill -f next`, on either route.
That pattern matches the Cooperator's own development server. A previous Orchestrator did it and
survived by luck alone. You may kill nothing at all in this exchange.

Either way, name the route you took and quote the `ss` output that decided it.

=====================================================================
4. THE TASK — reaffirmed unchanged from exchange 01
=====================================================================
Every one of the following remains exactly as granted in exchange 01. Re-read your exchange-01 prompt
for the detail; this section is the binding restatement, not a summary you may reinterpret.

GOAL. Route every user-facing string on the game screen through the four-locale catalog, correct the two
named defects rather than translating around them, and localize the one word left behind in `Board.tsx`.

THE TWO DEFECTS, both mandatory:
  uii-01-F08  `page.tsx:231-233` selects the lexicon message with a two-value test
              `lexiconId === "slovak" ? ... : "Not in Collins Scrabble Words 2019"`. Measured through
              the real loader, `gameState.lexicon_id` takes FOUR values — `collins2019`, `slovak`,
              `czech`, `polish` — so a Czech or Polish player is told their word is not in an English
              dictionary. That message is FALSE, not merely untranslated. Correct it with the five
              complete `game.lexicon.*` messages plus the unknown-id fallback. Do NOT build one
              parameterized `Not in ${lexicon}` sentence: Slovak and Czech need the locative case and
              Polish its own oblique form, which a single nominative label cannot supply.
  uii-01-F09  `page.tsx:1033-1054` gives pass and exchange the SAME toast type, and `page.tsx:305`
              distinguishes them with `toast.message.toLowerCase().includes("exchanged")`. Once that
              message is Slovak the substring is gone and an exchange is explained as "Couldn't find a
              valid move". Carry the discriminator in the toast DATA, not its prose. Choose the smaller
              change for this file and say which you chose and why. Afterwards no localized string may
              be load-bearing.

DO NOT TOUCH these three, because slice S4 deletes them:
  `"Choose rival"` at page.tsx:1502 and :1504 · `"Initial"` at :1513 ·
  `"Could not switch AI prompt right now."` at :606

`Board.tsx:689` `<span className="text-white/34">zoom</span>` becomes `{t("board.zoomNoun")}` and
NOTHING else changes in that 692-line file.

POSITIVE AUTHORITY — exact paths, unchanged:
  frontend/src/lib/i18n/messages.en.ts · messages.sk.ts · messages.cs.ts · messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md · i18n.test.ts
  frontend/src/app/game/[id]/page.tsx
  frontend/src/components/board/Board.tsx        (one word only)
No file is created. If a gate fails in a file NOT on this list, STOP and report rather than editing it.

NEGATIVE AUTHORITY — unchanged and still absolute. ScorePanel, GameHistoryPanel, GameHistoryModal,
ProfileModal, PromptCatalogModal, PromptPreviewModal, AIThinkingOverlay, play/page.tsx,
waiting/[id]/page.tsx, settings/page.tsx, lib/types.ts, lib/ai-move-stream.ts, lib/constants.ts
(its TW/DW/TL/DL literals are the BOARD, not copy), lib/api.ts (its 401 branch is a security property),
the five i18n machinery files, proxy.ts, security-headers.ts, anything under backend/ including
services.py, package.json and package-lock.json, the frozen provider files, prompts.ts and the AI
routes. SVG `path d`, `Content-Type`, toast ids and the LayoutGroup id are not copy. The `" vs "`
separator at :1709 stays English by glossary decision; only the `"Waiting"` fallback inside it is
localized. No Intl locale, no aria-label, no role, no alt. No reformatting or import reordering beyond
the named edits.

EXECUTION ROUTE — the bounded deviation is unchanged and mandatory, from backend/:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
Declared route that could not be used: `poetry run ...`, because the Cursor AppImage environment
intercepts `python*` through inherited APPIMAGE / ARGV0 / APPDIR / PYTHONHOME. Evidence class
reproduced-dynamic. Bounded authority: these four commands only. If the alternate also fails to resolve
the in-project virtualenv, STOP; do not substitute ambient python, python3, or poetry run.
`addopts = "-q"` is set — do NOT pass another `-q`, and quote the pytest summary verbatim. Run mypy on
the FULL documented scope.

Secret authority NONE. Dependency authority NONE. Browser authority none. Network authority: the two
`git ls-remote` reads only. This prompt is the only source of task authority.

=====================================================================
5. VALIDATION — unchanged
=====================================================================
Evidence tier: E2. Combined implementation envelope: allowed. Independent acceptance: not-required.
Validation ladder: selected · inspection and provenance required · existing focused tests
`frontend/src/lib/i18n/i18n.test.ts` · new causal regression = the two defect corrections · broad suite
required-because a project standing rule requires all eight gates · runtime or testbed not-used.

Gate baselines: mypy `Success: no issues found in 83 source files` · ruff `All checks passed!` ·
check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped` ·
typecheck exit 0 · vitest at least `369 passed | 3 skipped` plus your new tests · lint exit 0 ·
build exit 0 with EVERY route `ƒ` and ZERO `○` static routes.

MANDATORY NEW TESTS, unchanged. Each must FAIL before your implementation and PASS after, with the exact
pre-fix failure text reported.
  AC-LEX-4       all four `lexicon_id` values x all four locales select the right message. Assert that
                 `lexicon_id: "czech"` does NOT contain "Collins" and `"collins2019"` DOES. This is the
                 uii-01-F08 regression test and must fail against the current ternary.
  AC-LEX-UNK     an unrecognised `lexicon_id` selects `game.lexicon.unknown` and does not throw.
  AC-TOAST-DISC  the uii-01-F09 regression test. An EXCHANGE toast selects the exchange subtitle in
                 Slovak, whose message contains no English word; a PASS toast selects the pass subtitle.
                 Must fail while the substring check exists.
  AC-EXHAUST4    ALREADY EXISTS and must keep passing with every new key. Do not weaken it.
  AC-GAME-TERM   Czech `game.status.selectExchange` contains `kameny` and NOT `písmen`; Polish contains
                 `płytki`.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
6. GIT AUTHORITY — only on the primary route
=====================================================================
On the PRIMARY route, after all eight gates are green: exactly one commit and exactly one push.
On the FALLBACK route: NO commit, NO push, candidate left uncommitted.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the game screen and fix the lexicon and toast defects
     Body: the two corrected defects by ID, which discriminator shape you chose for uii-01-F09 and why,
     and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     e421c6690f091203a60636b3aebaeec71e7fba69. If it advanced, STOP and escalate; do not merge, rebase,
     or pull.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
7. STOPPING CONDITIONS
=====================================================================
Stop and report if: a section 1 gate value disagrees, including a non-empty porcelain; you cannot
reproduce the three section 2 strings; a gate fails in a file outside the section 4 allowlist; you cannot
localize a string without a structural change beyond the two authorized corrections; a hook would have to
be called conditionally; you conclude a new dependency is required; the backend gates fail;
`git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or
observed repository truth; or you find yourself weakening, skipping, xfailing, or deleting an existing
test.

**Port 3000 being occupied is NO LONGER a stopping condition.** It selects the section 3 fallback route.

If you do stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal
blocker, the smallest authority expansion that would resolve it, and the exact first error text.

=====================================================================
8. TERMINAL REPORT
=====================================================================
Begin with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 04, Worker exchange ordinal 02
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. the three section 2 continuity strings, echoed verbatim
 6. WHICH SECTION 3 ROUTE you took, with the exact `ss -tlnp | grep :3000` output that decided it
 7. changed files with the purpose of each, and the exact count of strings routed through the catalog in
    `page.tsx`
 8. the uii-01-F09 decision: which discriminator shape, why it is the smaller change, and the exact
    proof that no localized string is load-bearing any more
 9. the uii-01-F08 correction: how the five messages are selected and what happens for an unknown id
10. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
11. gate results — eight on the primary route, seven plus a named omission on the fallback route — with
    the pytest summary quoted verbatim and the vitest counts
12. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
13. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it
14. ANY user-facing English string still left in `page.tsx` after your work, other than the three that
    slice S4 deletes. List them exactly. The previous slice left one word behind because an Orchestrator
    allowlist was one item short, and this report is where that gets caught.
15. deviations, risks, or missing evidence
16. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
17. Pre-Existing Failure Classification: none | <complete classification>
18. one smallest next step or review request
19. report justification: new-mutation
20. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.
