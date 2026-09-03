# Libre Tiles — shared project context for Orchestrators

Artifact class: **shared reference, not authority.** Referenced by every Orchestrator handout under
`projects/libretiles/*/*/00_handout*.md` so that project truth is stated ONCE instead of being
copied into each handout, where the copies would drift apart.

This file grants no authority. Task authority comes only from the current authoritative prompt.
Protocol meaning comes from the pinned AP. Project truth comes from the canonical repository —
if this file and the repository disagree, **the repository wins and this file needs correcting.**

**Logical whole `backend-security-hardening` is CLOSED** at
`19cfec9ed27c57e9499b71c55be6c2fb709b0c63`; the closure record is
`09/00-backend-security-hardening/99_closure.md`. 32 findings `verified-closed`, 13 rejected as false
positives, all residuals dispositioned with sign-off where required.

**Two logical wholes are OPEN.** `ui-internationalization` (Meta 10/00) is roughly 60 percent done with
no active mutation. `multilingual-tile-token-foundation` (Meta 11/01) holds an accepted `planning-PASS`
and is ready for slice F1. `czech-polish-hungarian-variant-activation` (Meta 11/02) is NOT STARTED and
is blocked on Cooperator-supplied dictionaries. Execution order is `10/00`, then `11/01`, then `11/02`,
then `11/00`. The 10/00 opening Cooperator decisions are in section 13; the 11/01 alphabet data is in
section 14.

Three slices of `10/00` have landed and were Cooperator-accepted in his own browser:
`a5aff1214d97d28f2d27e55de5de19f09faf9c0e` (S1 — the typed two-locale message system and the localized
landing/auth page), `f26e92a61c65269c4d7d5a620665040e65466e59` (the game-variant description removal),
and `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd` (the starting-draw screen, plus a latent `tf()` contract
fix). `uii-01-F04` is owned by slice **S3a**, not S2 — Cooperator decision 7 cancelled S2 altogether by
removing URL locale prefixes. An earlier version of this paragraph said S2 and was stale.

`main` is now `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`. Porcelain is EMPTY — the ten
deliberately untracked `frontend/public` flag files are gone. The **Cooperator himself** committed the
five normalized 48x32 PNGs at `61c9f09` on 2026-09-02 (`feat(images): add new language icons for Czech,
English, Hungarian, Polish, and Slovak`, 5 files, 5230 B total, byte sizes identical to the
Orchestrator-normalized assets recorded in `DEFECT_LEDGER.md`). The five source JPEGs **never entered Git
history** and are gone from the working tree, so nothing is orphaned. Any handout or record that still
expects "ten deliberately untracked files in `frontend/public`" describes an earlier state; that
obligation is **discharged** and `10/00` R1 can reference `/en.png`, `/sk.png`, `/cs.png`, `/hu.png`,
`/pl.png` immediately. Full RF-12 classification of that commit (`unrelated-owner-work`, secondary
`accepted-continuation`) is in `10/00-ui-internationalization/94_orchestrator-restoration.md` section 1.

⛔ **THREE OF THE FOUR VISEGRÁD LANGUAGES ARE PLAYABLE: Slovak, Czech, Polish.** Czech and Polish landed
at `2917251` with real inflected lexicons from LibreOffice hunspell — 3 930 497 and 3 721 704 words,
licensed, provenance-pinned to one commit, Orchestrator-verified by hash and by membership probe.
**Hungarian is NOT playable and is blocked on a real inflection lexicon**, not on tile data: `unmunch`
cannot expand `hu_HU` because Magyar Ispell alias-compresses it and `unmunch` implements no `AF`
handling and no two-level suffixation. The accepted route is to keep the pinned source and replace the
expander with Spylls, which is a **candidate and not yet verified**. The full acceptance gate for that
work is in `DEFECT_LEDGER.md`.

Commit lineage of era 11, all Orchestrator-verified:

    9f0c5b8  F1   atomic tile tokens in the pure engine                     26 files
    3fd1a81  F2a  fail-closed command to purge legacy development state      4 files
    8c00a33  F2b  token-shaped persistence, uii-01-F06 and uii-01-F07        9 files
    2917251  A1   Czech and Polish activated as playable variants           22 files
    61c9f09  --   the five 48x32 flag PNGs, committed by the COOPERATOR      5 files
    5a96b5e  S3a  server locale authoritative + four interface locales      15 files
    e421c66  S3b  board, rack, action buttons and chat in four locales      11 files
    e0d3b64  S3c  the game screen, plus uii-01-F08 and uii-01-F09 fixed      8 files
    383011b  S4   R6: the player no longer chooses model or prompt   15 files, -460 net
    d40b230  S5   the two lobby screens + F10 F11 F12 F14 corrected   11 files
    6ca85de  S6   the game header cluster and the AI overlay           8 files
    4bf4365  S7   the settings screen and the overlay stats bar         8 files, 38 keys
    d806e31  S8   saved-boards history + half of uii-01-F03 (dates)     8 files, 35 keys
    8f44022  S9   the profile modal; uii-01-F03 CLOSED                   7 files, 16 keys
    c3f75e3  R1   premium searchable pickers with flags (closure cond. 2) 12 files, +615
    e8cc7bb  S11  R12: accessible names, dialog semantics, status regions 16 files, 9 keys
    74b5339  R14  one persistent announcer; rack tiles get a role       7 files, 0 keys
    f40d8a0  R15  ORCHESTRATOR-AUTHORED: rack keyboard + dead labels    4 files, 0 keys
    8f096e1  R7   Django resolves the client locale; F17 end reasons     10 files, 5 keys
    8ef5992  R8   ORCHESTRATOR-AUTHORED: Retry-After header over prose     4 files, 0 keys
    f983c3d  R9   ORCHESTRATOR-AUTHORED: HSTS includeSubDomains          2 files, 0 keys
    cb4efed  R10  per-request nonce CSP; orch-01-F18 corrected            4 files, 0 keys
    47ed8bf  R11  unreachable catalog stops reading as an empty one      11 files, 1 key

Anything below that speaks of `19cfec9`, `f26e92a`, `1b7b05d`, `9f0c5b8`, `3fd1a81`, `8c00a33`,
`2917251`, `61c9f09`, `5a96b5e`, `e421c66`, `e0d3b64`, `383011b`, `d40b230`, `6ca85de`, `4bf4365`, `d806e31`, `8f44022`, `c3f75e3`, `e8cc7bb`, `74b5339`, `f40d8a0`, `8f096e1`, `8ef5992`, `f983c3d` or `cb4efed`
as "current" describes an earlier commit and is history.

⛔ **THE FRONTEND SURFACE OF `10/00` IS COMPLETE AT `e8cc7bb`** — copy (S1–S9), function (S4), presentation
(R1) and accessibility attributes (S11). `R14` at `74b5339` then corrected S11's own three defects.
Everything remaining in this whole is **backend and security**, plus one 10-line frontend correction:
R15 (`uii-01-F24` + `uii-01-F23`), R7 Django i18n + `uii-01-F17`, R8 `Retry-After`, R9 HSTS
`includeSubDomains`, R10 nonce CSP, R11 catalog proxies + `uii-01-F13`, then the final acceptance batch.

✅ **`R14` IS DONE at `74b5339`.** It fixed `uii-01-F21` (a `role="status"` container enclosing a per-second
countdown, re-announcing the whole overlay atomically once a second), `uii-01-F22` (live regions that mount
with their content and so may never announce), `uii-01-F20` (`aria-label` on a role-less rack tile), and the
vacuous `aria-live` count assertion. `role="status"` and `aria-live` each went 8 -> 1. The emitted
`.sr-only` rule was read from the built CSS and is the correct clipped pattern, not `display:none`.

⛔ **BUT R14 PRODUCED TWO MORE, AND THE PATTERN IS NOW THE FINDING.** Both are corrected at `f40d8a0`:

    uii-01-F24  REGRESSION, corrected at f40d8a0. {...attributes} brings dnd-kit's role="button" and
                tabIndex={selectEnabled ? 0 : -1} makes it 0 whenever the tile is clickable — but
                DraggableTile had onClick and NO onKeyDown, and page.tsx:535-539 configures no
                KeyboardSensor. So every desktop rack tile became a dead Tab stop that no key could
                activate: worse than at e8cc7bb, where they were not focusable at all. Wider than the
                Worker reported — selectEnabled is true on a normal turn, not only in exchange mode.
                Fixed with an Enter/Space onKeyDown mirroring TapSelectableTile:147-151, declared BEFORE
                the listeners spread so a future KeyboardSensor would win on a draggable turn.
    uii-01-F23  corrected at f40d8a0. Six aria-label={t("a11y.status.turn")} sat on role-less toast
                motion.divs, because the R14 prompt authorized removing role and aria-live and said
                nothing about aria-label. Same class as F20. Deleted; a11y.status.turn stays in use on
                LiveAnnouncer, so no key went dead.

⛔ **TWO HANDOUT CORRECTIONS MEASURED WHILE SCOPING R7, both worth carrying forward:**

    R8 is NOT urgent   The handout says R7 "makes the coupling live" for the 429 wait-time parse and that
                       Slovak is safe "by luck". Measured: the msgids 'Expected available in {wait}
                       second(s).' (rest_framework/exceptions.py:229-230) are ABSENT from the sk, cs AND pl
                       catalogs, and exceptions.py:238-243 calls ngettext on an ALREADY-FORMATTED string,
                       so the lookup key carries the literal number and can never match a msgid. The
                       suffix stays English structurally, in every locale. api.ts:129's
                       /(\d+)\s+seconds/i matched 3300 in all four locales under USE_I18N=True.
    uii-01-F25         DOWNGRADED after R7 measured it: UNREACHABLE through any shipped endpoint. Both
                       password fields carry min_length=8 (accounts/serializers.py:17 and :62), so DRF's
                       own field validation rejects a short password BEFORE validate_password runs
                       MinimumLengthValidator — and that DRF message IS translated in all four locales.
                       Latent upstream curiosity, reachable only if someone removes min_length.
                       Original cause, still accurate: Czech does not translate MinimumLengthValidator:
                       django/contrib/auth/password_validation.py:118-119 uses msgid "... at least %d
                       character.", but django-5.2.17's cs catalog still carries the OLD
                       "%(min_length)d" form. sk and pl were updated, cs was not. The Czech string exists
                       and is unreachable. Fixing it needs a project-level backend/locale/cs/ override
                       plus compilemessages — out of scope, recorded so nobody reads it as our bug.
    uii-01-F26         NEW accepted residual, found while measuring F25. The Slovak DRF min_length
                       translation is SEMANTICALLY WRONG: "Uistite sa, že toto pole má viac ako 8 znakov"
                       says MORE THAN 8, but the constraint is AT LEAST 8 — an 8-character password
                       satisfies the rule while the message says it must exceed it. Czech `alespoň` and
                       Polish `co najmniej` are correct. Upstream djangorestframework-3.17.0 sk catalog,
                       not our string, and now visible to every Slovak player who types a short password.
                       Same blocked fix route as F25. Owner: a later whole.

⚠ Re-probing was CORRECT, not disobedient. The handout says "Do not re-run that probe; it is recorded as
verified" — but that recording covered **Slovak only**, and cs/pl were added by decision 8 afterwards.
Re-measuring what a recording never covered is not re-running it. Apply the same test to every other
"already verified" claim inherited from a handout written before decision 8.

⚠ **The ONLY outstanding evidence for F24 is one Cooperator keyboard observation**: Tab onto a rack tile,
press Enter, the tile is selected. `AC-RACK-KEYBOARD` asserts the handler and its declaration order from
SOURCE, because React does not serialize event handlers into static markup. Unlike F21 and F22, this one is
genuinely observable by him.

⛔ **FOUR A11Y DEFECTS FROM FOUR A11Y INSTRUCTIONS, ALL THE SAME ERROR.** F21: specified `role="status"`
without modelling `aria-atomic` plus a ticking timer. F20: specified `aria-label` without modelling where
the role comes from. F24: specified `tabIndex=0` without modelling what activates the control. F23:
specified removing two attributes without noticing the third became invalid. Lesson 14 in section 9 already
named this after F21/F22 and R14 repeated it anyway, so the lesson was not operational enough. The rule now
reads: **for every ARIA attribute added or removed, write down what the user does, what the technology
announces, and which key activates it. If nothing activates it, that is the defect.**

**All eight standing gates measured green at `47ed8bf` by the era-10 continuation Orchestrator**,
independently. At `47ed8bf` the FULL closure-condition-5 loopback re-proof was also run on port 3211 over all
seven document routes and all four /api routes: 114 script tags every one carrying its own response nonce,
and ELEVEN DISTINCT NONCES ACROSS ELEVEN REQUESTS. ⚠ THREE commits in this whole have NON-INDEPENDENT evidence because
the Orchestrator authored them: `f40d8a0` (R15), `8ef5992` (R8) and `f983c3d` (R9). For those, only the
mechanical gates corroborate the judgement calls. Every other commit is Worker work independently
re-measured. Do not read them as equally verified:

    mypy config game gamecore accounts catalog   Success: no issues found in 83 source files
    ruff check .                                 All checks passed!
    manage.py check                              System check identified no issues (0 silenced).
    pytest                                       390 passed, 4 skipped in 220.32s
    npm run typecheck                            exit 0
    npx vitest run                               450 passed | 3 skipped  (31 files passed | 1 skipped)
    npm run lint                                 exit 0
    npm run build                                exit 0, EVERY route ƒ, zero static, no deprecation warning
    grep -c sr-only .next/static/css/*.css       1, and the rule is clip-path:inset(50%), not display:none

Catalog size is unchanged by R14: **294 keys per catalog x 4 languages = 1176 strings**, of which 20 per
catalog are parameterized functions. Parity exact in all four, re-derived from source rather than read off a
report. `280 -> 285` (R1) `-> 294` (S11) `-> 294` (R14 adds none); the arithmetic closes at every step.

The earlier `c3f75e3` and `e8cc7bb` measurements — pytest 220.68s / 218.61s, vitest 405 and 414 — are
history. `414 -> 418` is `+6 -2`: six new tests minus the two `AC-STATUS-NOT-DIALOG` cases that R14's one
authorized inversion replaced. At `c3f75e3` `mypy --no-incremental` was also run as a ninth check and
returned the identical clean result.

✅ **The open mypy question in section 4 is now ANSWERED with evidence: mypy's incremental cache does
NOT share the `orch-04-F22` weakness at this commit.** Section 4 asked whether a cached mypy success
could hide errors the way `npm run build` hid two type errors behind `tsconfig.json`
`"incremental": true`. Measured at `61c9f09`: the cached and `--no-incremental` runs return the
identical `83 source files` clean result. That caution no longer needs to be carried forward.

The same gate set was measured green at `2917251` and `61c9f09` with vitest at 352/3; `5a96b5e` adds ten
frontend tests and every addition is accounted for. Zero `○` static routes is the REQUIRED outcome, not
a coincidence: a static route would mean the locale cookie is no longer read.

**The game surface is now localizing, area by area.** At `e421c66` the five surfaces a player touches on
every turn are in all four locales: the action buttons (`Zahrať / Vynechať / Vymeniť`,
`Zahrát / Vzdát tah / Vyměnit`, `Zagraj / Pauza / Wymiana`), the blank picker, the rack empty state, the
board hints and points abbreviation (`b.` / `b.` / `pkt`), and the chat panel. All three plural functions
are live at one call site and were read back through the real `tf()` against the shipped catalogs:

    sk  Výber: 1 písmeno · 2 písmená · 5 písmen · 22 písmen
    cs  Výběr: 1 kámen   · 2 kameny  · 5 kamenů · 22 kamenů
    pl  Wybrane: 1 płytka · 2 płytki · 5 płytek · 22 PŁYTKI   <- Polish diverges at 22, by design

⚠ **Two traps this produced, both worth carrying forward.** Polish genitive plural inserts an epenthetic
`e`, so `płytek` does NOT contain the stem `płytk` and a naive stem glob in a test gives a false
failure — assert the actual catalog forms. And a counted noun in a Slavic locale should be written as a
grammatically inert colon-label (`Výber: 2 písmená`) rather than a participle sentence, because the
participle would have to agree in both number and case across the one/few/many forms.

⛔ **One visible half-localized string is open at `e421c66`:** `Board.tsx:689` renders a dim English
`zoom` next to the localized `board.reset`, so the control reads "Reset zoom" in every locale. Cause is
an Orchestrator allowlist gap — the broad inventory counted six text nodes in that file and the prompt
authorized five. Routed to slice S3c with the key `board.zoomNoun`.

⛔ **`uii-01-F04` IS CORRECTED at `5a96b5e`, and the interface now ships in FOUR locales.** Server HTML,
`<html lang>`, `<title>` and the visible body share one locale, because `layout.tsx` reads the cookie and
feeds it to a client `LocaleProvider` that `useLocale()` prefers over the store. The store keeps
persistence and first-visit detection and stops being the rendering source. Reproduced independently by
the Orchestrator on a different loopback port than the Worker used:

    cookie=sk -> lang=sk, "Sign In" x0, "Prihlásiť sa" x1     (was x1 / x0 — that WAS the defect)
    cookie=cs -> lang=cs, "Přihlásit se" x1
    cookie=pl -> lang=pl, "Zaloguj się" x1
    cookie=fr | cz | hu | SK | empty -> lang=en, English body

The U+00A0 thousands separator was verified end to end for the first time, read as raw bytes from the
server HTML: `32 37 39 c2 a0 34 39 36` in sk / cs / pl versus `279,496` in en.

The frontend suite sat at 342 for four consecutive slices, which was the standing proof that no frontend
file had been touched; `A1` is the first slice to change it, deliberately, and every added test is
accounted for.

⚠ **Two era-11 deviations from accepted plan decisions, both deliberate and both evidence-backed.** The
development-state purge is a **management command**, not migration `0008`, because a fail-closed
irreversible migration is hostile to Django's own test harness in two measured directions and would make
`manage.py migrate` destructive. Consequently the schema migration is `0008_atomic_token_state_schema`,
**not `0009`** — there is no gap. Full reasoning in `DEFECT_LEDGER.md`.

⚠ **Czech and Polish receive the ENGLISH MOVE/JUDGE prompt CORE.** `MovePromptLexiconId` is
`"collins2019" | "slovak"` and anything else falls through to English, so the free LLM is primed on
Collins while the engine scores Czech or Polish. Bounded by the central product fact in section 6 — the
engine authors every move — so it degrades prompt quality, not playability. Recorded, not fixed.

**All eight standing gates were also green at `9f0c5b8`**, Orchestrator-measured: mypy 81 files, ruff,
`manage.py check`, pytest `352 passed, 4 skipped`, typecheck exit 0, vitest `342 passed | 3 skipped`,
lint exit 0, build exit 0. The frontend suite has been unchanged at 342 across both slices, which is
itself the evidence that neither touched a frontend file.

Last reconciled against `main` at commit `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd` by the era-11
`multilingual-tile-token-foundation` Orchestrator, with porcelain carrying only the ten deliberately
untracked `frontend/public` flag files, public readback equal, and no uncommitted tracked state.
**All eight standing gates were re-measured green at that commit** by that Orchestrator itself rather
than accepted from a handout:

    mypy config game gamecore accounts catalog   Success: no issues found in 80 source files
    ruff check .                                 All checks passed!
    manage.py check                              System check identified no issues (0 silenced).
    pytest                                       328 passed, 4 skipped in 189.67s
    npm run typecheck                            exit 0   (tsc --noEmit --incremental false)
    npx vitest run                               342 passed | 3 skipped  (26 files passed | 1 skipped)
    npm run lint                                 exit 0
    npm run build                                exit 0

They were also green at `f26e92a` (frontend suite `337 passed | 3 skipped`), at `a5aff12`, and at
`19cfec9` (`326 passed | 3 skipped`). Re-verify before relying on any of this.

**The `npm run build` route table is now ALL dynamic, and that changes a Cooperator-facing cost claim.**
Every route reports `ƒ` at `1b7b05d` — `/`, `/play`, and `/settings` included — because `layout.tsx`
reads the locale cookie. That is the expected, documented cost of decision 2 and is NOT a regression;
`92_orchestrator-glossary-and-plan.md` section 3 predicted it in writing. The consequence for decision 4
is worth stating loudly: the nonce CSP was costed to the Cooperator as "three product routes lose static
prerendering", and those three routes are **already** dynamic, so the nonce now costs **zero** additional
static prerendering. That estimate has now been revised down twice. The decision itself does not change.

⛔ **A green gate set did NOT mean a correct product at `a5aff12`.** `uii-01-F04`: the server renders
the page body in English while `<html lang>` and `<title>` follow the Slovak cookie. No gate can see
it, because vitest runs with environment `node` and nothing renders a page. It was found by
`next start` on a loopback port plus curl. Generalise the era-09 lesson: **for anything that renders,
render it, or do not claim it.**

**One commit in this era was authored by the ORCHESTRATOR rather than a Worker:** `f26e92a`, fourteen
lines of Cooperator-requested UI copy removal. It used the standing delegated slice git pattern
(explicit-path staging, pre-push `ls-remote` equality gate, one non-force push, public readback) and
passed all eight gates, but its evidence is explicitly **non-independent** — the Orchestrator was both
implementer and verifier. That is proportionate for R1 cosmetic work with no trust boundary and is
recorded rather than left implicit. Do not use it as precedent for anything larger.

---

## 1. Identity and topology

- Product: **Libre Tiles**, a standalone Next.js + Django Scrabble-like web app.
- Canonical repo `https://github.com/cisarik/libretiles`, working copy `/home/agile/Projects/libretiles`.
- Frontend: Next.js **16.3.4** App Router (bumped from 16.2.0 at `b5774b2`), React 19.2.4, Tailwind, Framer Motion, Zustand (persisted), DnD Kit. The request-interception file is **`frontend/src/proxy.ts`** exporting `proxy`; `middleware.ts` is gone and that convention is deprecated.
- Backend: Django + DRF. `backend/pyproject.toml` pins `django = "^5.2.17"` and the installed version is **5.2.17**; `daphne` is `^4.2.2` at **4.2.3**; `redis` is a **declared direct** dependency at `^7.3.0`. Write feature checks against Django 5.2. Pure game logic in `backend/gamecore/`.
- Realtime: Django Channels + Redis. **Redis is required ONLY for human-vs-human websockets, NOT for AI-only local boot.** That promise is in `AGENTS.md` and constrains where a shared cache or job queue may live.
- English validator: Collins 2019. Slovak: a hunspell-sk expansion (playable, not SSS-official) with SSS Príloha **B2** as the authoritative two-letter lexicon.
- AI-vs-house runs through **one** Next.js SSE route `/api/ai/move`. Free-only, but **nine** provider constants ship in `frontend/src/lib/provider-registry.ts`: `openrouter`, `nvidia-nim`, `groq`, `google-gemini`, `cloudflare-workers-ai`, `mistral`, `ibm-watsonx`, `aion`, `huggingface`. Eight route through the shared OpenAI-compatible transport in `frontend/src/lib/openai-compatible.ts`; `ibm-watsonx` has its own IAM path in `frontend/src/lib/ibm-watsonx.ts`. `backend/catalog/selection.py` **does** already carry all nine — the seven extra ones are string literals inside `DIRECT_FREE_RIVALS` / `WATCHLIST_FREE_RIVALS`, not module-level `*_PROVIDER` constants, so a constant-only grep misses them. `README.md` was already accurate. Only `AGENTS.md` was stale; corrected at `bbba2e9` as `orch-02-D08`.
- AP is pinned at the `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. A sibling checkout at `/home/agile/Projects/ap` may be newer; **the pin governs.** Do not upgrade AP.
- Libre Tiles declares **no** project-level `ap.project.conf`, **no** AP upgrade ledger, **no** closure-signal string. `.ap/ap.project.conf` belongs to the AP repository itself (`projectId = cisarik/ap`) and declares no route here. Do not invent any of those.

## 2. The Cooperator

Cooperator: **Michal.** Address him in **Slovak**, masculine grammatical forms. Orchestrator
self-reference is **feminine**. Worker prompts and Worker reports are professional **English**, and
every terminal Worker report begins exactly `### Report for ORCHESTRATOR_CHAT`.

His role, in his own words: he brainstorms, he intervenes when development heads the wrong way, he
answers questions, and he tests and gives feedback. He is not a file clerk and not a command runner.
He will happily be a courier when it genuinely helps, but do not make him one for work you can do.

His stake is material: he is preparing to present Libre Tiles at a **job interview** as evidence
that he can integrate AI into a real product. Presentability and correctness are first-class
requirements. A fresh clone that crashes, a control that does nothing, or a dashboard whose numbers
do not mean what they claim are serious defects in his frame.

He has granted full trust and asks for initiative. His replies are terse — `A`, `Pokracuj`, `ano`,
`Fixnute`. One one-word reply was once misread and cost an entire Worker session, so **confirm an
ambiguous one-word instruction in one line** before spending a session on it.

Do not encode "make no mistakes" as an acceptance criterion for him or for a Worker. It is not a
testable condition. Make his steps unambiguous instead.

### Emoji signals he asked for

Begin every message to him with the signal that tells him what to do:

    🧠 fresh Worker session, Plan mode ON (Planner Worker)
    🔨 fresh Worker session, Plan mode OFF (implementation or correction)
    🔍 fresh Worker session, Plan mode OFF (read-only audit or evidence probe)
    🧭 fresh Orchestrator session (handout)
    🧪 a manual test batch for him, answered with labelled PASS/FAIL/PARTIAL
    ❓ a question, you are waiting on an answer
    ✅ verified by you, nothing for him to do
    🐞 a classified defect going into the ledger
    ⛔ a blocker, or do-not-deploy
    📁 you wrote something to meta

**End every message with an explicit, emoji-annotated block of what he must do**: what to paste
where, what to test, what feedback you need, which question blocks you. Never bury his action in prose.

**Label manual test steps with a batch prefix** (`B3-1`, `B3-2`, …). Plain `1.)` collides with your
own numbered action list and has already caused one round of confusion.

## 3. Never do this

- Never read or print `frontend/.env.local` or `backend/.env`. Ask him yes/no questions about
  whether a variable is set. Never ask him to paste either file.
- Never let a credential value, prefix, length, or hash reach chat, a report, or a Meta file.
- Never create permanent `BOOT_*`, `NEXT_*`, `WORKERS.md`, or `ORCHESTRATOR_HANDOFF.md` files in
  the repository. A repository handoff is not the live model.
- Never ask him for a destructive action: no `git reset`, `git clean`, force push, database drop or
  reset, deleting his `.env` files, or deploying. Asking him to restart a dev server, create a test
  account, or play a game is fine and expected.

## 4. Standing quality gates

Every implementation prompt must require all of these and stop on any regression:

    cd backend
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    cd frontend
    npx vitest run <focused set>   ;   npm run typecheck   ;   npm run lint   ;   npm run build

Baselines at commit `19cfec9ed27c57e9499b71c55be6c2fb709b0c63` — **re-measure, do not trust**: mypy
`Success: no issues found in 80 source files`; ruff `All checks passed!`; `manage.py check`
`System check identified no issues (0 silenced).`; pytest `328 passed, 4 skipped`; the ten authorized
vitest files `199 passed (10 files)`; lint exit 0; build succeeds with one known deprecation warning
about the `middleware` file convention. Progression: `445029d` 302 passed, `bbba2e9` 315 (+13 from
S7a), `8e82f3b` 322 (+7 from S7b), `9ff9ac5` 322 unchanged (that correction added 6 frontend tests only), `7a197da` 326 (+4 dependency-floor tests), `b5774b2` 326 unchanged (frontend-only), `19cfec9` 328 (+2 throttle-identity tests).

### Execution route, and the mandatory bounded deviation

`AGENTS.md` documents backend commands as `poetry run ...`. **That route is NOT usable in a Worker
boundary**: the Cursor AppImage environment intercepts `python*` through inherited `APPIMAGE` /
`PYTHONHOME` variables. Per AP RF-16, every prompt must express the alternate as an explicit bounded
deviation naming the declared route that could not be used, the exact alternate
(`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`), the rationale, the evidence
class, and the stopping condition. Never present ambient `python`, `python3`, or `poetry run` as a
parallel canonical route.

**`poetry` itself IS usable once the same variables are unset.** Verified read-only at `445029d`:
`env -u APPIMAGE -u ARGV0 -u APPDIR poetry env info` resolves the in-project virtualenv at
`backend/.venv` (Poetry 2.3.2 at `~/.local/bin/poetry`, `virtualenvs.in-project = true`). There is no
`poetry` binary inside `.venv/bin`. So a dependency change is done with
`env -u APPIMAGE -u ARGV0 -u APPDIR poetry add ...`, while test and type-check runs still go through
`.venv/bin/python` directly. Confirm the resolved virtualenv path before any `poetry add`.

**`npm run typecheck` is a NEW and mandatory gate, added at `b5774b2`.** It runs
`tsc --noEmit --incremental false`. It exists because `frontend/tsconfig.json` sets
`"incremental": true` and `next build` reuses that cache, so `npm run build` reported SUCCESS at
`9ff9ac5` and `7a197da` while two type errors existed in the tree — finding `orch-04-F22`. Every
"build succeeds" claim in this era, including the Orchestrator's own re-measurements, was weaker than
stated. "The build passed" and "the code type-checks" are now two separate claims and both must be
said. **The parallel mypy question is now ANSWERED rather than open:** measured at `61c9f09`, the
cached mypy run and `mypy --no-incremental` over the documented scope both return
`Success: no issues found in 83 source files`, so mypy's cache does not share the `orch-04-F22`
weakness at that commit. Re-check it after any dependency or stub change, but stop carrying it as an
unknown.

### Two traps that have already cost real Worker sessions

- `backend/pyproject.toml` sets `addopts = "-q"`. Passing another `-q` **silently suppresses the
  pytest summary count line**. Require plain `-m pytest` and require the summary quoted verbatim.
- Running mypy on a **narrowed** path set once hid 62 real errors behind a reported 12 for six
  consecutive Worker sessions. Always require the documented scope. Never let a "parked error count"
  travel between prompts unchallenged.

### Git pattern, delegated by the Cooperator

One commit per slice, staged by **explicit path** (never `git add -A` or `git add .`), an explicit
pre-push `git ls-remote origin refs/heads/main` equality gate against the exact baseline, one
non-force fast-forward `git push origin main`, and a public readback comparing `git ls-remote` with
`git rev-parse HEAD`. Never force, amend, rebase, reset, clean, stash, branch, or tag. If the remote
advanced, stop and escalate.

**Exactly one Orchestrator is active at a time**, because all of them push to `main` and each one's
pre-push gate demands exact equality.

## 5. Locked forks — do not reopen without contradictory evidence plus a Cooperator decision

1. SSS **100** Slovak tiles. Not 112, not 108. No CH/DZ/DŽ tiles. 42 tile kinds, of which **17 diacritic kinds have exactly one copy each**, so running out of a specific diacritic tile is normal.
2. **One** parameterized MOVE CORE with a pinned SHA-256, version `pfr-s2-core-1`, in `frontend/src/lib/prompts.ts`. **One** SSE route. Do not fork a second one and do not bump the version.
3. Judge (`/api/ai/judge`) is advisory Tier-3 assistance; Django is the sole authority; HTTP 503 on exhaustion; never synthesize a false `invalid`. It currently has **no caller** in the frontend.
4. No JULS, no `sk.sorted.txt`, no unofficial SSS dump, **no paid catalog tier**, no Stripe, no LM Studio, no Vercel AI Gateway. Libre Tiles is **free-only**: no money, credits, balances, token prices, or per-game charges.
5. Slovak two-letter legality = SSS B2 membership of **complete formed words**. Never a substring test.
6. Slovak lexicon quality is **PARKED** by Cooperator decision. hunspell junk (`loso`, `náhlo`, `vltavu`) is accepted residual and must never fail a diagnostic.
7. **Browser MCP is forbidden as a diagnostic driver** — explicit Cooperator decision, made because browser-driven diagnosis was too slow. He has since said it may be used if genuinely necessary; prefer CLI, raw sockets, and direct database inspection, which in practice have produced *more* evidence than a browser would. Asking the Cooperator to look at the UI himself is ordinary Cooperator-executed acceptance and is the right tool for UI work.
8. `MAX_FALLBACK_ATTEMPTS = 3` in `frontend/src/lib/ai-fallback.ts`.
9. Production search caps `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` in `backend/gamecore/move_search.py`. Any variant-specific bound is an explicit call kwarg, never a changed default.
10. Exactly six `completion_source` values: `provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_exchange`, `genuine_no_move_pass`. Do not add a seventh.
11. **The nine AI providers are FROZEN pending their own logical whole.** Explicit Cooperator decision, 2026-08-31: he will run a dedicated whole to stop hardcoding providers. Until that whole runs, **no change to any provider list, provider constant, provider tier, exact model tuple, or provider documentation is authorized anywhere** — not `frontend/src/lib/provider-registry.ts`, not `frontend/src/lib/openai-compatible.ts`, not `backend/catalog/selection.py`, not `README.md`, not `AGENTS.md`. Reading those files is fine. The AGENTS.md accuracy fix that landed at `bbba2e9` (defect `orch-02-D08`) predates this decision and stands; do not revert it and do not extend it.

### The formed-word invariant — the single most misread rule in this project

    Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2
    and is outside the variant two-letter lexicon.
    NEVER illegal because a longer formed word CONTAINS a two-letter string.

`OSAMENIU` is legal even though it contains `AM`. `ja`, `ty`, `my`, `si`, `to` are legal Slovak
two-letter plays and the Cooperator wants them legal. If any Worker writes `assert "am" not in word`,
greps the board for a letter pair, or enumerates pairs to reject a longer word, **that Worker has
failed.** The only lawful shape is set membership over the list of complete formed words. Reference
implementation: `backend/tests/test_slovak_ranked_search.py` (`_REJECTED_CROSSES`, `isdisjoint`).

## 6. The central product fact

Across roughly a dozen counted live provider invocations in five independent sessions, the free LLM
authored **zero** backend-valid placements. Every completed live turn used
`completion_source: backend_ranked_candidate`. **The engine authors every move.** The LLM is an
unreliable component behind an authoritative engine.

This is the architecture working as designed and it is the honest framing for the interview. Never
let a Worker "improve" the AI by weakening backend validation.

Measured live on 2026-08-31 in the Cooperator's own browser, from persisted `ai_metadata`:

| observation | value |
|---|---|
| with an expired provider key | `terminal_cause = generic_error_fallback`, ~5 s per AI turn |
| with a fresh provider key | `terminal_cause = no_provider_progress_deadline`, ~21 s per AI turn |
| both cases | `provider_requests_used = 1`, `valid_candidate_count = 0` |

The ~21 s is the ~20 s no-provider-progress deadline aborting a silent model, after which the engine
commits a ranked candidate. Before that deadline existed, an AI turn took 124–138 s. **That
mechanism is observable working in production and is one of the better things to demonstrate.**

Engine strength, measured provider-free: under the product-like `ranked-best` policy a Slovak game
finishes in ~29 plies via `BAG_EMPTY_AND_PLAYER_OUT`, consumes all 17 single-copy diacritic tiles,
plays zero passes, and scores 520–560 per side. **Those are engine numbers, identical whichever
model is plugged in.** Any "how good is this model at Scrabble" metric must therefore be built on
the `completion_source` distribution and the `provider_candidate` rate, never on final score.

**Provider failures are now logged, bounded and redacted.** `frontend/src/lib/provider-logging.ts`
emits `{provider, phase, status, errorClass, message}` to `process.stderr.write`, message capped at
200 characters, from `createTrackedProviderFetch` in `openai-compatible.ts`, from `trackedFetch` in
`ibm-watsonx.ts`, from the outer catch in the move route, and from the two judge catches. The sink is
`process.stderr.write` rather than `console.error` because Vitest's console wrapper consumed a
`Date.now` mock and broke the judge timing tests — a real near-miss the Worker reported honestly. All
routes are Node runtime (`export const runtime` appears nowhere), so `process.stderr` exists.
**The redaction was the fragile part** — finding `orch-02-F21`, corrected at `9ff9ac5`. A pattern
denylist could not hold; the project's own `ibm-watsonx.test.ts` fixture defeated the first version.
The rule is now: redact by VALUE against the twelve credential environment variables the process
actually holds (literal replace, longest first, minimum length 8, placeholders skipped, no cache so a
rotated credential is matched on the next failure); keep the pattern denylist as defence in depth with
`Bearer[\s:_-]+` and a 16-character entropy floor; and for the `provider_transport` phase omit the raw
provider message entirely, keeping only error class and status, because the watsonx IAM request carries
the API key in its body. Never log request headers, the
request body, the response body, or a stack trace.

## 7. Security state — do not regress it

**`audit-03-F01` is `verified-closed`** by the bounded independent re-audit `audit-04` at `19cfec9`.
`DJANGO_NUM_PROXIES` defaults to `0`, is validated fail-closed, and binds `get_ident` to `REMOTE_ADDR`.
Orchestrator-verified dynamically: a spoofed `X-Forwarded-For` no longer changes the throttle bucket.
The history below is kept because the mechanism matters for any future rate limit.

⛔ **THE HISTORY OF THAT FINDING.** `audit-03-F01`, found by the independent re-audit at `b5774b2` and
independently confirmed by the Orchestrator from the installed DRF source: **DRF's unauthenticated
throttle identity is attacker-chosen.** `rest_framework/throttling.py` `BaseThrottle.get_ident` ends
with `return ''.join(xff.split()) if xff else remote_addr`, and that final line is reached whenever
`NUM_PROXIES` is `None` — which is the DRF default and is not overridden in `backend/config/settings.py`.
So every distinct `X-Forwarded-For` value WAS a fresh throttle bucket until `19cfec9`. `django-axes` is NOT affected,
because `ipware` is not installed and `axes/helpers.py` falls back to `REMOTE_ADDR`. The two brakes
therefore key on different identities. The consequence was that `auth_register` and `auth_refresh` had no
effective IP brake, and a **credential spray across many usernames** from one address was unbounded —
the DRF limit bypassed and axes never firing, because its key is (username, IP) and each username saw
only one failure. **Any future rate limit in this project must state which identity it keys on, and it
must agree with axes.**

### The nginx deployment fact, and the trap inside it

Cooperator decision 2026-09-01: Django will be deployed **behind nginx, and only behind nginx**.
Therefore `DJANGO_NUM_PROXIES` must be **1** in production, and nginx must set
`proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;`, which appends the real peer LAST — DRF
with `NUM_PROXIES=1` reads `addrs[-1]`, so that composition is not spoofable. `NUM_PROXIES=1` with nginx
NOT setting the header re-opens the bypass silently.

**The trap:** behind nginx, `django-axes` still keys on `REMOTE_ADDR` — nginx's address for every
request — because `ipware` is absent and `axes/helpers.py` only honours `AXES_IPWARE_*` when
`IPWARE_INSTALLED` is true. The lockout key `(username, ip_address)` then collapses to one global bucket
per account, turning an account lockout into a **targeted denial of service**. The very setting chosen in
S7a to avoid NAT-wide lockouts stops protecting anything once every request appears to come from one
address. Recorded as `orch-05-D14`, independently confirmed as
`audit-04-F01`, routed to the deployment whole.

⛔ **AND THE OBVIOUS REMEDY IS A TRAP.** The Orchestrator first wrote "install `django-axes[ipware]` and
set the trusted-proxy count". Verified against the installed `axes/conf.py`, that is wrong in a dangerous
direction:

    AXES_IPWARE_META_PRECEDENCE_ORDER  default ("REMOTE_ADDR",)   <- XFF is never consulted
    AXES_IPWARE_PROXY_ORDER            default "left-most"
    AXES_IPWARE_PROXY_COUNT            default None

Installing the extra and stopping there changes NOTHING. Adding `HTTP_X_FORWARDED_FOR` to the precedence
order without also setting the proxy count leaves `left-most` in force — and the left-most element of
`$proxy_add_x_forwarded_for` is the part the CLIENT sent. That would give axes an attacker-chosen
identity, turning a denial-of-service weakness into a full lockout-and-throttle bypass. **The half-measure
is worse than the current state.** Precedence order, proxy order (right-most, to match nginx's append),
and proxy count must be set together and tested as one unit. Also note the DRF dual: a `NUM_PROXIES`
value GREATER than the real hop count reads a leftward, attacker-chosen element. Too high is as dangerous
as too low.



Corrections landed across commits `ae574b7`, `fdfe4a6`, `7e583aa`, `04fe823`, `437e20f`, `445029d`,
`bbba2e9`, `8e82f3b`, `9ff9ac5`, `7a197da`, `b5774b2`, `19cfec9`. Verify current state yourself; this is the summary.

- Django **refuses to start** without a strong explicit `DJANGO_SECRET_KEY` (rejects absent, empty, whitespace, the old public fallback literal, keys under 50 characters or with fewer than 5 unique characters, and the `django-insecure-` prefix). `DEBUG` defaults to **false**. `ALLOWED_HOSTS` has no wildcard default and rejects `*` when DEBUG is false. `CORS_ALLOW_ALL_ORIGINS` is only ever true in DEBUG. HTTPS cookie, HSTS, and SSL-redirect flags follow `not DEBUG`. Tests in `backend/tests/test_security_settings.py`.
- DRF `DEFAULT_PERMISSION_CLASSES` is `IsAuthenticated` — **fail-closed**. Any DRF view you add is authenticated unless it explicitly declares otherwise. A deliberately public endpoint must declare `AllowAny`, justify it, and carry a test proving exactly what it exposes.
- `/api/ai/judge` requires a Django-verified Bearer token **before** any catalog fetch or provider call, and caps input size (12 words, 15 characters each). The shared helper is `frontend/src/lib/api-auth.ts`; it branches on `res.status` **before** parsing the body. **Any route that can cause provider spend must use that helper and that ordering.** Never copy the older `parseBackendJson` pattern in the move route, which ignores HTTP status.
- DRF scoped throttles exist. The scope **strings are load-bearing for tests**: `auth_register`, `auth_login`, `auth_refresh`, `auth_change_password`, `auth_me`, `ai_context`. Adding a scope is cheap; renaming one breaks tests. Rates at `bbba2e9`: register **20/h**, login **60/h**, refresh 60/h, change-password 5/h, me 200/h, ai-context 200/h. Login and register are **IP-keyed**, so all browsers on one machine share the budget — the derivation is `ScopedRateThrottle.get_cache_key`, which uses `user.pk` when authenticated and otherwise `get_ident(request)`. `LogoutView` has **no** throttle scope. In DEBUG the throttle cache is `LocMemCache` and therefore **per-process**, so restarting Django clears all counters — that is the reset button during manual testing.
- **Per-account brute-force brake: `django-axes==8.3.1`**, exactly pinned, the only dependency addition in this era. `AXES_FAILURE_LIMIT = 8`, `AXES_COOLOFF_TIME = 30 minutes`, `AXES_RESET_ON_SUCCESS = True`, `AXES_HTTP_RESPONSE_CODE = 429`, and — critically — `AXES_LOCKOUT_PARAMETERS = [["username", "ip_address"]]`, overriding the 8.3.1 default of IP-only, which would let one wrong-password user lock out everybody behind a NAT including the presenter. axes compares with `>=`, so the **8th** response is the lockout, not the 9th. `AUTHENTICATION_BACKENDS` is now explicit: `axes.backends.AxesStandaloneBackend` first (a lockout gate that does not authenticate), then `ModelBackend`. Enforcement is in the backend chain — `AxesStandaloneBackend.authenticate` raises `AxesBackendPermissionDenied` — so it does **not** depend on the DRF glue middleware. Covers both `POST /admin/login/` and `POST /api/auth/login/`; SimpleJWT does pass `request` into `authenticate()`, which is what makes the API path covered. `AccessAttempt` in Django admin is the failure audit trail; `AXES_ENABLE_ACCESS_FAILURE_LOG` is left false. Axes 8 ≪ login 60/h is deliberate: a single targeted account locks long before the coarse IP budget.
- **Throttle cache fails closed in production.** DEBUG true keeps `LocMemCache`, so Redis is still not required for AI-only local boot. DEBUG false resolves `DJANGO_THROTTLE_CACHE_URL`, else `REDIS_URL`, else raises `ImproperlyConfigured`; a non-`redis://`/`rediss://` value also raises. `django.core.cache.backends.redis.RedisCache` needs no new dependency, but the `redis` client is a **transitive** dependency of `channels-redis` rather than a declared direct one — a standing residual for the dependency audit.
- Password policy: registration runs `validate_password`, minimum length 8, and four Django validators (`UserAttributeSimilarity`, `MinimumLength`, `CommonPassword`, `NumericPassword`).
- JWT lifecycle: `token_blacklist` enabled, `ROTATE_REFRESH_TOKENS`, `BLACKLIST_AFTER_ROTATION`, `POST /api/auth/logout/`, a `password_changed_at` field on `accounts.User`, and a `PasswordAwareJWTAuthentication` subclass rejecting any token whose `iat` predates the password change. Missing or non-numeric `iat` **fails closed**. Verified live: after a password change the old session yields `Session expired`.
- Websocket tickets are **single-use**, enforced by a unique constraint on a SHA-256 hash in `game_consumed_ws_ticket` (a DB constraint, visible to every worker, deliberately not the per-process cache). The signed payload carries a `nonce` because Django's `TimestampSigner` is deterministic within one second for an identical payload, and without the nonce two fetches in the same second would collide and look like "one connection per game forever". Bounded cleanup of expired rows, no scheduled job, no Redis.
- Security response headers and an **enforced** CSP are emitted from `frontend/src/proxy.ts` via the pure builder in `frontend/src/lib/security-headers.ts`. Independently re-audited at `b5774b2`: the headers reach **every** document route and Next `/api/` route — `/`, `/play`, `/settings`, `/game/[id]`, `/waiting/[id]`, `/draw/[id]`, `/api/models`, `/api/prompts`, `/api/ai/move` — and are correctly absent on `favicon.ico`, `/_next/static/**`, and prefetch-marked requests. `connect-src` is **request-derived**, mirroring `resolveApiBase()` including its loopback-to-current-hostname rewrite. A static `connect-src 'self'` would break both the Django API and the game websocket.

### Dependency posture — established 2026-09-01, and it blocks deployment

The first dependency and supply-chain audit in this project's history (`audit-02`, INFOSEC 4.7 profile
P-4) found **three high findings on the deployed surface**, all independently re-confirmed by the
Orchestrator with `npm audit` and OSV.dev rather than accepted from the report:

| Package | Was | Now | Status |
|---|---|---|---|
| `django` | 5.2.12, 33 OSV records | **5.2.17**, OSV **0** | corrected at `7a197da`; constraint floor `^5.2.17` |
| `daphne` | 4.2.1, 4 OSV records | **4.2.3**, OSV **0** | corrected at `7a197da`; constraint floor `^4.2.2` |
| `redis` | undeclared transitive of `channels-redis` | declared `^7.3.0` direct | corrected at `7a197da` |
| `next` | 16.2.0, 23 advisories | **16.3.4**, left the advisory set | corrected at `b5774b2`; also closed `sharp` 0.34.5 -> 0.35.4 and nested `postcss` |

The `next` bump was the dangerous one and is why it was a separate slice: `orch-01-F18`'s accepted residual
records that `frontend/src/middleware.ts` works only because Next 16 renamed the convention and the
old name still executes with a deprecation warning. A minor bump could drop that support and silently
stop emitting the CSP and every other security header. Anyone bumping `next` must prove the headers
are still emitted afterwards.

One medium finding is not fixable inside that whole and was dispositioned rather than corrected:
`audit-02-F05` — there is no CI, SBOM, signing, or provenance in-tree attesting the artifact a browser
executes. No `.github` directory exists at all. Adding CI is a separate deliberate decision about what
it gates.

`npm audit` went from 7 advisories to **3**, and all three remaining are `dev`-flagged and already
dispositioned as `rejected-false-positive` in `audit-02-F07`.

`audit-02-F05` — no CI, SBOM, signing, or provenance in-tree — is an **accepted residual with explicit
Cooperator sign-off given 2026-09-01**. The complete Residual-Risk Decision record is in the ledger.

⛔ **The do-not-deploy stands, but for one specific named reason rather than precautionarily.** All 32
corrected findings ARE `verified-closed` — thirty by `audit-03` at `b5774b2`, two by `audit-04` at
`19cfec9`. What blocks public exposure is `audit-04-F01` / `orch-05-D14`, which becomes reachable the
moment Django sits behind nginx, plus the unresolved deployment items in section 11. The deployment
whole must correct it before public exposure.

### Runtime evidence for the CSP now exists, and one gap in it

The enforced CSP was built in slice 07, which had to state honestly that runtime validation was not
performed because Browser MCP is a locked fork. At `b5774b2` that gap is partly closed: a production
`next start` bound to loopback, probed with an HTTP client, returns the full header set on `GET /`. The
implementing Worker did it on port 3100 and the Orchestrator independently reproduced it on 3200 with
byte-identical output. A production server plus an HTTP client is not a browser and is a legitimate
technique here.

**That gap is now CLOSED.** The P-10 re-auditor probed `/`, `/play`, `/settings`, `/game/{id}`,
`/waiting/{id}`, `/draw/{id}`, `/api/models`, `/api/prompts`, and `GET /api/ai/move` on its own loopback
server and got the identical header set on every one, with the exclusions behaving exactly as
`proxy.ts` declares. The CSP is not decorative on the page where a user plays. This was the
Orchestrator's own named weak spot and handing it to the re-auditor is what resolved it.

### Migrating the proxy convention is not safe to do gradually

Next 16.2.0 **hard-fails** when both `src/middleware.ts` and `src/proxy.ts` exist, with an
`unhandledRejection` rather than a graceful message — observed by the Cooperator in his own
`npm run dev` during the migration window. There is no safe intermediate state, a running dev server
will break during the transition, and that crash is not a product defect. Migrate as a single rename and
restart the dev server afterwards.

Reusable lesson from this audit: the deployed surface here is `next`, `django`, `daphne`, `channels`,
`channels-redis`, `redis`, `psycopg`, `httpx`, `djangorestframework`, `djangorestframework-simplejwt`,
`django-cors-headers`, `django-axes`, `python-dotenv`, `ai`, `@ai-sdk/openai`, `react`, `react-dom`,
`zod`, `zustand`, `framer-motion`, `@dnd-kit/*`, `canvas-confetti`. Everything else in either lockfile
is dev-only, and an advisory against a dev-only package is not a production finding. `poetry.lock`
carries group markers and `package-lock.json` carries `dev: true`; use them before promoting a scanner
line into a finding. Note that `optional: true` is NOT `dev` — `sharp` is in the production optional
tree, which is how `orch-03-G01` was missed the first time.

### Accepted residuals with recorded Cooperator sign-off

| Finding | Decision | Severity | Rationale |
|---|---|---|---|
| `audit-01-F13` duplicate-username registration error stays explicit | accepted-residual | low | usability for a self-service game; login itself does not differentiate unknown user from wrong password |
| `audit-01-F09` websocket ticket travels in the query string | accepted-residual | low | single-use plus a short TTL minimises the capture window; moving it would require changing the handshake and the frontend client |
| `orch-01-F18` `script-src 'unsafe-inline'` in production | accepted-residual | medium | nonce CSP needs dynamic rendering on `/`, `/play`, `/settings` — the exact pages the UX whole rewrites. `connect-src` still blocks exfiltration of the localStorage tokens. **Upgrade to nonce CSP is routed to the UX/i18n Orchestrator.** |
| `style-src 'unsafe-inline'` | accepted-residual | low | Framer Motion sets inline `style` attributes |
| ~~`frontend/src/middleware.ts` instead of `proxy.ts`~~ | **CLOSED at `b5774b2`** | — | migrated to `proxy.ts`; this residual no longer exists and must not be carried forward |

### Verified non-issues — do not re-litigate without contrary evidence

Object-level authorization is sound (`services._load_session_for_user` filters on `slots__user_id`,
outsiders get 404, the acting slot is server-derived, and `variant_slug` is only ever set at game
creation so a running game's variant cannot be swapped). `dangerouslySetInnerHTML` appears nowhere
in `frontend/src`; chat renders as a React text node. No secret is tracked in Git or in reachable
history. Model output cannot choose `game_id`, slot, or pass/exchange/place, because `game_id` and
the token are closures over the HTTP request body. `AllowedHostsOriginValidator` permits the browser
origin (`ALLOWED_HOSTS` contains `*` in the Cooperator's dev environment; the validator honours it).

### Two standing facts that constrain every UI change

1. The access token **and** the refresh token are persisted in `localStorage` through the Zustand store (`frontend/src/hooks/useGameStore.ts`). That is an accepted residual only because no XSS sink exists. No `dangerouslySetInnerHTML`, no `innerHTML`, no untrusted HTML, no casually added third-party script. Render model-produced and user-produced text as text nodes. **One XSS sink converts an accepted residual into full account takeover.**
2. Django admin is **session**-authenticated while the API is JWT-authenticated, so admin cookies are real and `SESSION_COOKIE_SECURE` / `CSRF_COOKIE_SECURE` matter. The Django admin login form is **not** a DRF view, so the DRF throttles do not protect it.

## 8. Instruments you inherit — use them, do not rebuild them

    manage.py diagnose_ai_engine   variant-aware PROVIDER-FREE engine probe; fixtures or a deterministic seed; versioned JSON report `libretiles.ai-play-diagnostic/v1`; exit 0/1/2
    manage.py diagnose_ai_play     drives a real AI turn through the real /api/ai/move POST, the real fallback orchestrator, the real SSE consumer, and an ephemeral pytest-django live_server with a real DB; --runtime-mode fake|live; live is hard-gated on LIBRETILES_AI_PLAY_LIVE=1 plus a present provider key and fails closed with a redacted message otherwise; supports --turn-count 1..300 although only 1 was ever run live
    manage.py seed_models          offline bootstrap catalog; must keep working for local boot — never make `sync` a startup requirement
    backend/tests/test_endgame_policy_matrix.py   three move-selection policies x both variants x deterministic seeds; wide matrix behind `slow` + LIBRETILES_RUN_ENDGAME_MATRIX=1
    backend/tests/test_slovak_full_game.py        Slovak full game to a legitimate end reason with tile conservation; wide matrix behind LIBRETILES_RUN_SLOVAK_FULL_GAME=1
    backend/tests/test_slovak_ranked_search.py    provider-free Slovak ranked oracle; the OU/AM formed-word traps
    backend/tests/test_full_game_simulation.py    English engine-vs-engine full games. Its local _is_word uses folded.isascii() — NEVER copy that onto Slovak
    backend/tests/test_multiplayer_ws.py          websocket coverage
    backend/tests/test_admin.py                   admin coverage; the house style for admin tests
    backend/tests/test_game_app_has_no_dev_imports.py   AST guard: no pytest/pytest_django/ruff/mypy import under backend/game/**
    frontend/src/lib/ai-turn-simulation.test.ts   300-turn causal simulation with an injectable model

Two ORCHESTRATOR instruments, both validated against known-bad inputs before being trusted. Neither lives in
the repository; recreate them from these descriptions if `/tmp/opencode` is gone:

    /tmp/opencode/jsxsweep.py        v2 sweep over JSX text nodes. Regex inventory of JSX is unreliable, so
                                     this walks text nodes structurally. Validated against four historical
                                     Orchestrator inventory errors.
    /tmp/opencode/apfieldcheck.py    ⛔ AP STRUCTURAL FIELD CHECKER. Extracts the spec blocks from the pinned
                                     .ap — Plan-to-Execution PROMPT_CONTRACTS.md:716-728, Planning Record
                                     :89-101, justification enum AP.md:2452-2454, result enum :203 — and
                                     diffs EVERY field value in a Worker prompt against them.
                                     `python3 apfieldcheck.py <prompt.md>`; exit 1 on any defect.
                                     Written after Worker session 15 returned BLOCKED TWICE on protocol
                                     conformance: three invalid fields in exchange 01, then a FOURTH that the
                                     Orchestrator introduced while hand-fixing the first three.
                                     Validated: exchange-01 prompt -> 1 defect + 4 warnings (reproduces all
                                     three findings), exchange-02 prompt -> 1 defect (reproduces the fourth),
                                     exchange-03 prompt -> clean. Two bugs were found in the tool during that
                                     validation, which is the argument for doing it.
                                     Honest limits, emitted as WARNINGS not skipped: it cannot judge
                                     `Native planning mode: required` (that depends on the Cooperator's
                                     client, not on a value), and it catches invented result values such as
                                     `planning-PASS` only by prose scan.
                                     It ALSO checks COORDINATE CONSISTENCY: the header's session/exchange
                                     ordinals must equal what the report-format section tells the Worker to
                                     echo (PROMPT_CONTRACTS.md:38-41). Added after defect five, which the
                                     field checker could not see because the ordinal occurs in two textual
                                     forms and a patch on one silently left the other.
                                     ⚠ RUN IT ON EVERY PROMPT BEFORE ISSUING. Lesson 17 said "read the enum,
                                     do not recall it" and was written in the very session that then
                                     hand-edited a field without re-reading its spec line.
                                     ⛔ AND DO NOT BUILD A PROMPT BY STRING-PATCHING THE PREVIOUS ONE. Three
                                     of the five structural defects in Worker session 15 were introduced BY
                                     THE REPAIR of an earlier one.

Two structural patterns worth reusing rather than reinventing:

- **`executed_runtime_mode`.** The v1 report records what **actually executed**, separately from what was requested, and a mismatch is a sample **failure** with reason `runtime_mode_not_honored`. This exists because `--runtime-mode live` once accepted the flag, silently ran the fake path, and reported `exit 0 / verdict pass`. Apply "record what happened, not what was asked" to anything you build, and make sure any dashboard can say **"I did not measure."**
- **Derived counters.** `external_provider_invocations` comes from the fetch guard that decides which origins are allowed, not from a literal. It was previously a hardcoded `0`.

## 9. Lessons that cost real Worker sessions

1. Provider-free tests hid two live-only defects: whether live mode was implemented at all, and that every AI turn burned 120 seconds. **For anything the model touches: measure live, or do not claim it.**
2. A test that proves only the guard can hide an unimplemented feature. An Orchestrator once accepted "live mode implemented and hard-refused" after verifying only the refusal path; the enabled branch did not exist. **When you accept a feature that has a guard, exercise the positive path too.**
3. **Worker reports are claims.** Re-verify every material one yourself: read the diff, run the gates, check the exact line references, reproduce the load-bearing behaviour. This practice has caught a garbled finding that hid a real fact, an entirely missed finding, and a line-number claim that pointed at a lazily-invoked closure rather than a sequential call. It is not distrust; it is the protocol.
4. **A tool that measures must be able to say "I did not measure."** A Worker could once have written "live run, exit 0, verdict pass" and nobody would have noticed; it wrote BLOCKED and cited five lines of code instead. Demand that shape explicitly.
5. **Negative results are results.** A rare-tile-dumping heuristic was designed, measured, and rejected because it made one seed worse. Write completion contracts that say a negative result is an acceptable PASS.
6. **Require a pre-fix / post-fix table for every regression test**, with the exact pre-fix failure. A test that passes before the change locks nothing. One Worker caught its own too-weak assertion this way and strengthened it before implementing.
7. **An authorized correction can expose a pre-existing defect outside its allowlist, twice in a row.** When that happens, do not keep growing the slice. Give the Worker a decision rule with a pre-authorized bounded fallback so the work converges in at most one more exchange, and route the root cause as its own whole.
8. **Your own prediction can be wrong and the Worker's measurement can be right.** An Orchestrator claimed a third test file would break a probe; the Worker measured `19 passed` and explained why. Say so plainly when it happens; that is what keeps Workers reporting honestly.
9. **Diagnose the environment before blaming the product.** A websocket failure that looked like a product defect was a Tailscale exit node routing the entire Docker bridge range into the tunnel. Check reachability, routes, and services first.
10. **A negative grep is not a conclusion.** The era-09 continuation Orchestrator grepped `backend/catalog/selection.py` for `*_PROVIDER =` constants, found two, and recorded in this file and in the ledger that the backend knew about only two providers. All nine were there as string literals inside `DIRECT_FREE_RIVALS` / `WATCHLIST_FREE_RIVALS`. The Worker measured it, contradicted the Orchestrator, and was right. When a grep returns *few* results, widen the pattern before writing a finding — a finding built on the absence of a match must state the exact pattern that failed to match. Two more instances landed in era 10 on one afternoon: the Django password validators live in `django/contrib/auth/locale/sk/`, not `django/conf/locale/sk/`, and `rest_framework/locale/sk/` ships a compiled `.mo` with no `.po`, so a `.po`-only search reports both as absent.
11. **For anything that renders, render it, or do not claim it.** Era 10, `uii-01-F04`. Eight green gates — including `typecheck`, `lint`, `build`, and 337 frontend tests — coexisted with a document that declared `<html lang="sk">` and a Slovak `<title>` around an entirely English body. vitest runs with environment `node` and nothing in the suite renders a page, so the whole gate set was structurally blind. The technique that found it is the one the era-09 re-auditor established for CSP headers: production build, `next start` bound to loopback on a non-default port, probe with an HTTP client, stop the server **by exact PID**. Reuse it for every rendered claim in this project.
12. **A faithfully executed prompt can still produce a defective product, and then the prompt is the defect.** `uii-01-F04` came from the Orchestrator's own section-5 contract, which made the client store the source of truth for the locale and called the server-readable cookie "a routing hint only". In a server-rendered application, whatever the server can read must be authoritative for rendered output, or SSR and hydration cannot agree. The Worker implemented the contract exactly, its gates were genuinely green, and it honestly reported the adjacent limitation it did find. Classify this as an Orchestrator design defect, not a Worker execution defect, and say so in the record.
13. **Do not state an inventory more precisely than the measurement that produced it.** Lesson 10 is about negative greps; this is its positive twin. At `c3f75e3` the Orchestrator wrote that `AIThinkingOverlay` "already has `aria-live` in two places". The measurement actually run counted `aria-label`, `role`, `alt`, `htmlFor`, `tabIndex`, `aria-modal` and `sr-only` — **never `aria-live`**. There were two occurrences repo-wide, in two different files, and the Worker read the source, found one in the named file, said so, and resolved both. Two consecutive slices now end with a Worker correcting an Orchestrator claim on evidence (R1's `alt=""`, S11's `aria-live`). Both times the prompt's own permission-to-overrule is what surfaced it. Write the count, or write "unmeasured".
14. **An accessibility attribute is a behavioural change, so reason about the behaviour, not the attribute.** ⛔ THIS LESSON WAS WRITTEN AFTER TWO DEFECTS AND THEN REPEATED TWICE MORE, so it now carries an operational rule instead of an observation. Four defects, one error: `uii-01-F21` specified `role="status"` on a `fixed inset-0` container without modelling that `role="status"` implies `aria-atomic="true"` and that the container held a per-second countdown, so an assistive technology re-read the whole overlay once a second. `uii-01-F22` specified live regions that mount together with their text, which frequently never announce at all. `uii-01-F20` specified `aria-label` without modelling that the role it needs comes from a conditionally spread dnd-kit `attributes` object. `uii-01-F24` specified `tabIndex={0}` without modelling that a `div[role=button]` does not synthesize a click from Enter or Space, turning every desktop rack tile into a dead Tab stop — a regression against the commit before it. THE RULE: for every ARIA attribute you add or remove, write down (a) what the user does, (b) what the technology announces, (c) which key activates it. If the answer to (c) is "nothing", that is the defect and not a detail. None of these four is visible to `typecheck`, `lint`, `build`, or a node-environment vitest suite; all four are visible by reading the semantics before writing the prompt.
15. **A remediation slice can produce its own remediation, and that is a signal to change method rather than iterate.** S11 produced F20/F21/F22; R14 fixed those three and produced F23/F24. Both Workers executed their prompts faithfully and reported the new problems themselves, in the report field that asks what they can still see — which is the only reason the chain was visible at all. Keep that field in every prompt. But when the second slice in a domain also generates defects, the Orchestrator's model of that domain is the fault, not the slice size: stop writing another confident prompt and write down the interaction model first.
16. **After writing the negative authority, re-read the mandated tests and ask whether you just forbade one of them.** Worker session 14: section 7 said `CREATE: nothing` and "`backend/tests/` is NOT on this list", while section 10 mandated three BACKEND tests. Both cannot hold. What was MEANT was "do not edit an existing backend test to make it pass"; what was WRITTEN also banned adding one. The Worker caught it by reading the two sections against each other, created a new file, edited nothing existing, and disclosed it — the best available outcome. Prohibitions and obligations get drafted in separate passes and are never cross-checked, so make the cross-check explicit: for every artifact section 10 requires, confirm section 8 permits it.
17. **⛔ VERIFY THE PROMPT'S OWN AP FIELD VALUES AGAINST THE PINNED ENUMS, NOT JUST ITS `file:line` CLAIMS.** Worker session 15 exchange 01 returned BLOCKED because one prompt carried THREE invalid protocol fields at once. Its technical content was fine — nine `file:line` claims mechanically checked, zero misses — while the frame was structurally invalid. The gap is exact: `file:line` claims get verified every time, AP field VALUES never did. **The three closed enums, written here so the check takes seconds:**

    ```text
    Report justification            AP.md:2452-2454
      new-mutation | new-evidence | new-material-risk | changed-external-state | final-acceptance |
      explicit-closure                                  <- there is NO `new-analysis`
    Phase-qualified result          PROMPT_CONTRACTS.md:203
      implementation-PASS | acceptance-PASS | publication-PASS | deployment-PASS |
      production-acceptance-PASS | not-applicable       <- planning uses `not-applicable`, NOT `planning-PASS`
    Native planning mode            PROMPT_CONTRACTS.md:695-698
      `required` means the client MUST have the mode enabled before delivery. If it does not, the prompt
      MUST NOT BE PASTED; reissue as `not-used` with explicit prompt-level read-only planning authority.
    Plan-to-Execution fields        PROMPT_CONTRACTS.md:716-728    Planning Record  :89-101
    current-worker-session needs    :359-365 — continuity anchor · prior-authority expiry · complete new
      bounded grant · reuse rationale · preserved WORKER role · repository re-gating · retained context as
      CONVENIENCE NOT AUTHORITY · non-independent posture · stop on conflict · new terminal report
    ```

    Read the enum, do not recall it. All three defects were confident inventions that read plausibly.

    ⛔ **AND THEN THE REPAIR ITSELF ADDED A FOURTH.** Exchange 02 was rejected for
    `Execution authority event`, which `PROMPT_CONTRACTS.md:725` fixes as a CLOSED LITERAL. Because the
    planner prompt now carried `Native planning mode: not-used`, the required value read as
    self-contradictory to me, so I "improved" it. The spec block has three kinds of entry and I collapsed
    two: `<angle brackets>` is a fill-in, `a | b` is an enum, **a bare string is a literal to be copied
    byte-for-byte.** This lesson existed already when I made that edit, which is the proof that a lesson
    saying "be careful" does not survive contact with a hand edit. The operational form is a TOOL:
    `/tmp/opencode/apfieldcheck.py`, section 8, run on every prompt before issuing.

    ⛔ **AND THEN THE PATCH FOR THAT REPAIR ADDED A FIFTH.** Exchange 03 declared
    `Worker exchange ordinal: 03` in its header while section 9 still instructed the Worker to echo `02`;
    `PROMPT_CONTRACTS.md:38-41` requires the report to echo the authoritative coordinates UNCHANGED. Cause:
    the ordinal occurs in two textual forms — `ordinal: NN` in the header, `ordinal NN` in the report
    instructions — and a string patch matched only the first.

    ⛔ **THE REAL LESSON IS NOT ABOUT FIELDS AT ALL: DO NOT BUILD A PROMPT BY STRING-PATCHING THE PREVIOUS
    PROMPT.** Five structural defects in Worker session 15, and THREE of them were introduced by the repair
    of an earlier one. Regenerate the whole coordinate-bearing region, then let the tool check it. The tool
    now covers coordinate consistency as well — extended twice, each time after a defect it could not see,
    each time validated against the failing artifact before being trusted. A checker never anticipates a
    class it has not been burned by, so growing it after each miss is the method, not an admission.
18. **A NUMBER YOU DID NOT COUNT YOURSELF IS NOT A MEASUREMENT, WHATEVER PRODUCED IT.** Lesson 13 was written after an inventory stated from recollection. Worker session 16 found the same failure with a different source: the R10 implementation prompt said `security-headers.test.ts` had "nine existing `it` blocks" when it had ELEVEN. The number came from an explore subagent's report and was repeated without counting — and the `12 call sites` figure in the same sentence WAS correct, which is exactly what made the wrong number look checked. One layer down, the same prompt claimed `constructRequest` was available from `next/experimental/testing/server`; it is declared in the internal `utils.d.ts` but the public barrel re-exports only `getRedirectUrl`, `getRewrittenUrl` and `isRewrite`. **Reading the file that DECLARES a symbol is not reading the file that EXPORTS it.** Subagent output is evidence to verify, not a measurement to quote.
19. **A test that pins a known-broken UPSTREAM state is a tripwire, not a regression test, and it must be labelled as one.** R7 added `test_czech_minimum_length_validator_catalog_mismatch` and `test_drf_throttle_wait_suffix_stays_english`, both asserting that a Django/DRF translation gap still exists. They are useful — they fire the moment upstream fixes it — but the next dependency bump will break the suite with a failure that looks like a regression and is actually good news. Both carry explanatory docstrings. `audit-02` established a standing upgrade posture, so whoever performs the next bump must be told these two are expected casualties.

## 10. Known environment traps on the Cooperator's machine

- `backend/.env` must set `DJANGO_DEBUG=true`, otherwise `SECURE_SSL_REDIRECT` and the secure-cookie and HSTS flags switch on and local plain HTTP misbehaves in ways that look like product bugs. Since `bbba2e9` there is a second consequence: with `DJANGO_DEBUG=false` Django now **refuses to start** unless `DJANGO_THROTTLE_CACHE_URL` or `REDIS_URL` names a `redis://` / `rediss://` URL. That is deliberate fail-closed behaviour, not a regression.
- `scripts/libretiles.sh` now generates a strong `DJANGO_SECRET_KEY` into a **freshly created** `backend/.env` using `python3 -c` / `secrets.token_hex(32)`. It returns early and touches nothing when `backend/.env` already exists, so the Cooperator's existing file is safe. It requires `python3` on PATH and fails closed if absent.
- `.env` values **override** code defaults and are read at process start. Changing `.env` requires restarting the affected server. This is how `GAME_WS_TICKET_MAX_AGE_SECONDS='60'` silently kept the old TTL after the code default became 10.
- **The documented Django start command binds every interface.** `README.md:56`, `README.md:180`, and `AGENTS.md:32` all say `runserver 0.0.0.0:8000`. The Cooperator's live listener happens to be `127.0.0.1:8000` (verified with `ss`), but anyone following the documentation is reachable from their whole LAN. Any "not reachable today" claim must say which of the two it means. Found by the session-15 re-auditor.
- `frontend/.env.local` is read by the Next.js server at startup; a new provider key needs `npm run dev` restarted.
- ⛔ **An App Router page module may export ONLY the enumerated Next.js set.** Discovered and reproduced
  at `4bf4365`. `frontend/.next/types/app/<route>/page.ts` contains a
  `checkFields<Diff<{ default: Function; config?: {}; generateStaticParams?: Function; metadata?: any;
  generateMetadata?: Function; revalidate?; dynamic?; ... }, TEntry, ''>>()` assertion, so ANY other named
  export from a `page.tsx` is a `tsc` error:

      error TS2344: ... does not satisfy the constraint '{ [x: string]: never; }'.
        Property 'TIMEOUT_CHOICES' is incompatible with index signature.

  Consequence for prompts: never instruct a Worker to "export it for the test" from a page file. Either
  authorize a separate module in the allowlist, or accept a static property on the default export.
  `frontend/AGENTS.md` warns that this is not the Next.js you know; this is a concrete instance of it.
- Login and register throttles are IP-keyed and shared across browser profiles. At `bbba2e9` login is 60/hour and register 20/hour, sized for a same-NAT demo of roughly 16 logins and 12 registrations. **Restarting Django clears the counters** in DEBUG, because the cache is per-process LocMem. A single account is separately locked by `django-axes` after 8 failures for 30 minutes, and that lockout lives in the **database**, so a Django restart does NOT clear it — delete the `AccessAttempt` row in Django admin instead.
- Multiplayer needs Redis (`docker compose up -d redis`; only the redis service — the project uses SQLite in dev). **Tailscale with an exit node can route the Docker bridge range into the tunnel**, making Redis unreachable from the host while healthy inside the container. Symptom: `docker exec … redis-cli PING` returns `PONG` but a host connection times out. Check with `ip route get 172.18.0.2` — it must show `dev br-…`, not `dev tailscale0`. Fix with `sudo tailscale set --exit-node-allow-lan-access=true`.
- Two browser profiles are required for multiplayer. Two tabs in one profile share `localStorage` and the second login overwrites the first.
- An AI turn takes ~21 seconds with a working key. That is expected, not a timeout.

## 11. Carried-forward obligations: THREE handouts are owed, none written

Recorded here, not only in a handout, so they cannot be lost when a session ends.

### 11.1 An expert Orchestrator handout for `10/00 ui-internationalization` — WRITTEN, 2026-09-01

✅ **Delivered.** `10/00-ui-internationalization/93_orchestrator-handout.md`, 41 783 B, written by the
era-11 Orchestrator at his explicit request. It is the second handout for that whole; where it and
`00_handout.md` disagree, `93_` is later and wins, and every disagreement is named in its section 4.

Cooperator decision, his own initiative, that produced it: finishing the localization deserves its own
fresh Orchestrator that understands exactly how to complete it, because it is an enormous chunk and will
consume very many tokens. In his words: `10/00 by bolo najrozumnejsie riesit novym fresh Agent
Orchestratorom ktory bude presne rozumiet ako dokoncit lokalizaciu ta je predsa ohromne velky zarez`.
Sequencing he set: written after `11/01`'s slices, not interleaved with them.

He also observed, correctly, that **Slovak itself is not finished.** Re-measured at `61c9f09`: **57 keys**
are localized — `enText` holds exactly **55** plain keys and `enFn` holds exactly **2** parameterized
ones — across six areas (draw 13, landing 11, error 11, settings 10, auth 10, meta 2, which sums to 57).
An earlier version of this paragraph and `93_orchestrator-handout.md` both say "55 keys across six areas"
while listing a histogram that sums to 57; both numbers are real and the sentence conflated the `enText`
half with the total. A key-set diff of the two catalogs returns zero missing and zero extra keys, so the
`Record<TextKey, string>` contract is holding. The entire game surface is still English —
`game/[id]/page.tsx` alone holds ~70 user-facing literals across 1822 lines, and JSX text nodes between
tags are invisible to a quoted-literal grep, so the true figure is higher.

What that handout carries, so nobody reconstructs it: the corrected residual list R1–R13 with **R2 marked
DONE** because era 11 slice A1 delivered the dynamic variant list; the measured per-file remaining scope
**with the warning that a raw grep over-counts** locked and non-user-facing literals in
`provider-registry.ts`, `prompts.ts`, `security-headers.ts` and the AI routes; the glossary and his
personal `písmeno` / `zásobník` / `žolík` decisions; the three-form Slovak plural contract; the
`Record<TextKey, string>` type contract; AC-SEC-1 and AC-SEC-2 as non-delegable; the one open Cooperator
decision on which locales to ship; unverified candidate terminology for Polish and Hungarian clearly
labelled as candidates; the boundary table against the still-open `11/01`; and the nine failure modes
this model has actually exhibited.

### 11.2 An expert Orchestrator handout for the VPS deployment whole — STILL OWED

Asked for three times and still not written. He describes himself as a complete novice at operations and
named Prometheus and Grafana specifically as things he does not understand. The complete fact set —
the Docker-Compose-plus-host-nginx topology decision, the exact `DJANGO_NUM_PROXIES=1` and
`$proxy_add_x_forwarded_for` arithmetic with both silent misconfigurations, `audit-04-F01` and the trap
in its obvious remedy, the `NEXT_PUBLIC_*` build-time inlining trap, and the monitoring assessment — is
written out in `10/00-ui-internationalization/00_handout.md` section 10. **Copy it from there; do not
reconstruct it from memory.**

### 11.3 A prompt for a read-only Research Worker — STILL OWED

He has ChatGPT Deep Research and wants it used for current VPS-hardening practice on Ubuntu Server
24.04. The prompt must demand versions and retrieval dates rather than unsourced "best practices", and
must be framed so the researcher can honestly answer "this is disproportionate for a single demo VPS",
particularly about Prometheus and Grafana.

**That route is now proven to work.** Era 11 used it for the Hungarian lexicon question with the brief at
`11/02/90_hungarian-lexicon-research-brief.md` and got back a precise, source-cited report that correctly
returned a **negative** answer on nine of nine candidates rather than an optimistic pointer. Reuse that
brief's shape: two independent questions, hard disqualifying constraints, required per-candidate fields,
and an explicit instruction that a well-evidenced negative is a fully successful outcome.

Topology decision already made at his explicit request: **Docker Compose for the application and Redis;
nginx and certbot on the host.** Reasons and the rejected systemd alternative are in that same section.
Deployment happens after the UI/UX work, by his decision 6.

### His stated goal, and the honest distance to it

On 2026-09-01 he named the goal: localization plus **play in the Visegrád Four languages**. The honest
path, with nothing hidden:

```text
11/01  F2b -> F2c -> F3 -> F4, then the R4 independent audit, then closure
11/02  czech-polish-hungarian-variant-activation — BLOCKED on three things HE must supply:
       czech.txt, polish.txt, hungarian.txt with licensing and provenance evidence.
       Sourcing those is the single highest-value thing he can do in parallel, because it is the
       only blocker nobody else can clear. No scraping, no synthesis, no substitutes.
10/00  the ~330 remaining strings plus cs/pl/hu UI translations, under its own fresh Orchestrator
```

`11/02` needs `11/01` closed **and** the dictionaries. `10/00` R4 (cs/pl/hu UI) is additive and
independent of the engine. Neither is reachable in one sitting, and saying otherwise would be dishonest.


## 12. Cooperator product intent for the admin provider/model console

Recorded **verbatim in substance** on 2026-09-01, in this durable file rather than only in a handout,
because the Cooperator asked whether this brainstorming had been lost. It had not been lost as a
*decision* — locked fork 11 and the ledger both record the provider freeze — but the *detail* below was
nowhere in this file. It is now. This section is product intent and constrains successor wholes; it is
not authority to implement anything today.

He stated, in his own words and his own priority ordering:

- **The single most important thing for him** is being able to add new providers and new models, and set
  the default, **from the Django admin interface, without an SSH connection**. That is the acceptance
  condition for the `admin-provider-model-console` whole, and it is what "the models must not be
  hardcoded" means operationally.
- He wants **AI-vs-AI diagnostics inside that admin surface, in both the English and the Slovak
  variant**, going beyond the existing ping→pong tile.
- In future he intends to configure **OpenAI-compatible models** there, and he wants to **test a model's
  strength before promoting it to default**. The engine numbers in section 6 constrain how such a test
  must be built: final score is an engine number and is identical whichever model is plugged in, so a
  strength metric must rest on the `completion_source` distribution and the `provider_candidate` rate.
- **"It was bad UX to leave that decision to the user."** The player should not choose the model. He
  believes the frontend may already reflect this and asked; see the correction below.
- The player **should only ever see the model's name**, not provider internals, tiers, or tuples.

✅ **RESOLVED at `383011b` (slice S4 / R6).** The paragraph below was true at `19cfec9` and is now
history. The player no longer chooses the AI model or the prompt preset: the settings rival panel is
a read-only display name, the prompt-preset picker and both of its components are deleted,
`selectedPromptId` is gone from the store with a persist 4->5 migration, and `ai_prompt_id` is no
longer sent at game creation so the backend picks catalog row 1. `preferred_ai_model_id`, its
migrations, its admin field and its `is_selectable_model` validation are untouched, which is what
makes it admin-settable only. ZERO backend change was needed: `_resolve_ai_model` and
`_resolve_ai_prompt` already return row 1 when the field is omitted, and `sort_order` plus
`is_active` are `list_editable` in Django Admin — so an administrator sets the default with no SSH,
while `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` stays `false`.

The original correction, kept as history:

⛔ **Factual correction the Orchestrator owed him, verified in the repository at `19cfec9`, not
inferred.** The frontend had **NOT** yet been changed. The player still chose:

```text
frontend/src/app/settings/page.tsx:656-712   a selectable rival panel over the live catalog, with
                                             display_name, description, and per-row selection
frontend/src/app/settings/page.tsx:664       "No rival selected" fallback
frontend/src/app/play/page.tsx:31,65         "Choose AI"
frontend/src/hooks/useGameStore.ts:30,129    persisted `selectedModelId`, default ""
frontend/src/hooks/useGameStore.ts:32,131    persisted `selectedPromptId` — the player also chooses the
                                             PROMPT PRESET, through PromptCatalogModal and the
                                             "Prompt presets" control in ScorePanel.tsx:425
```

So there are **two** player-facing internals to remove, not one: the model choice and the prompt-preset
choice. The prompt-preset choice arguably leaks more product internals to a player than the model choice
does. `10/01-player-model-choice-removal` is therefore genuine outstanding work, not already-landed work.

Note the overlap, because it affects sequencing: removing the player's model and prompt choice rewrites
`frontend/src/app/settings/page.tsx`, which is the same file the `ui-internationalization` whole rewrites
for the interface-locale switch. Two wholes rewriting one 803-line file in sequence is avoidable churn.
Whether to fold that removal into the current whole is a Cooperator scope decision and has not been made.

## 13. Decisions taken at the opening of `ui-internationalization`

All six are **Cooperator decisions**, given on 2026-09-01 in reply to a decision package that carried a
recommendation and the supporting evidence for each. He selected option A for the first five.

```text
1  LOCALE ROUTING: **SUPERSEDED on 2026-09-01 by decision 7 below — there are no URL locale
   prefixes at all.** The original decision was a path prefix `/sk/...` and `/en/...`, with
   subdomain-per-locale rejected. The subdomain rejection STANDS and is permanent for this cut.
   Rationale he was shown for rejecting subdomains: a subdomain layout touches five surfaces the
   security era just hardened — request-derived `connect-src`, HSTS `includeSubDomains`,
   `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, and the Django admin session-cookie domain scope. This
   superseded the "subdomain-locale feature" named in the era-09 handout, deliberately and with his
   agreement.

2  INTERFACE LOCALE SWITCH: a switch in Settings, PLUS browser-language detection on the FIRST visit
   only. Not detection alone, and not a switch alone.

3  SLOVAK REGISTER: informal `ty` (tykanie). "Tvoj rad", not "Váš rad". Fixed for the whole product,
   including error messages. Do not vary it.

4  NONCE CSP: implement it. `orch-01-F18` (`script-src 'unsafe-inline'`, medium, previously an accepted
   residual with his sign-off) moves from accepted to being corrected in this whole. `style-src
   'unsafe-inline'` REMAINS an accepted low residual because Framer Motion sets inline `style`
   attributes.
   ORCHESTRATOR SELF-CORRECTION, measured at the `npm run build` run on 2026-09-01: the cost he was
   shown was overstated. The Orchestrator wrote that "all six page files under `frontend/src/app` carry
   `use client` and are prerendered as static shells", so a nonce would convert six routes to dynamic.
   The `"use client"` half is correct; the prerendering half was not. The build route table shows only
   THREE product pages prerendered static — `○ /`, `○ /play`, `○ /settings` (plus `○ /_not-found`) —
   while `ƒ /draw/[id]`, `ƒ /game/[id]`, `ƒ /waiting/[id]` and every `/api/` route are ALREADY
   server-rendered on demand. So the nonce costs static prerendering on three routes, not six. That is
   exactly what the `orch-01-F18` residual record itself said — "a nonce CSP needs dynamic rendering on
   `/`, `/play`, `/settings`" — and the residual was more precise than the Orchestrator restating it.
   The decision does not change; the cost is smaller than presented and he was told so.

5  DJANGO HSTS: add `SECURE_HSTS_INCLUDE_SUBDOMAINS`. Do NOT add `SECURE_HSTS_PRELOAD`. `orch-02-D11`
   is corrected in this whole for the includeSubDomains half; `preload` stays a separate explicit future
   decision because submission to the browser preload list is close to irreversible. Remember there are
   TWO HSTS emitters and this concerns Django's only — `frontend/src/lib/security-headers.ts:109-112`
   already sends `includeSubDomains` from the Next.js proxy in production.
   NOTE after decision 7: the only reason `orch-02-D11` was routed to this whole was that
   `includeSubDomains` interacted with a subdomain-locale design. With no subdomains and no prefixes
   that interaction no longer exists, so this is now a plain one-line settings addition with an explicit
   test in `test_security_settings.py`. The decision stands; the coupling is gone.

6  SEQUENCING: localization and the UI/UX work come FIRST. The VPS deployment itself happens only after
   the UI/UX changes. BOTH deployment artifacts are still owed and are NOT cancelled — the expert
   Orchestrator handout for the deployment whole, and the read-only Research Worker prompt for ChatGPT
   Deep Research. He confirmed both are needed; he simply is not deploying yet.

7  NO URL LOCALE PREFIXES AT ALL. Decided 2026-09-01, superseding decision 1. `/` and every existing
   path stay exactly as they are. There is no `/en/...`, no `/sk/...`, and no subdomain. His reasoning,
   in his own words: "ked mam v localstorage ulozeny jazyk interface ... ma to zmysel a je to
   jednoduchsie".
   THE ORCHESTRATOR RECOMMENDED THE PREFIX AND HE WAS RIGHT TO OVERRIDE IT. What the prefixes would
   have bought — shareable language-bearing links, per-language SEO, and a path the server can read
   without a cookie — is worth nothing to this product. It is an interview demo of AI integration, not
   a content site; there is no public content to rank, and every page except `/` is behind login.
   What they would have cost is concrete:
     - redirect or rewrite logic inside `frontend/src/proxy.ts`, the file that emits EVERY security
       header, whose slice-07 prompt said in terms "it sets headers and nothing else"
     - either an `app/[locale]/` restructure that moves every page file, or a proxy rewrite
     - every internal `router.push(...)` and `<Link>` made locale-aware, across dozens of call sites
     - a third source of locale truth (URL) needing reconciliation against the cookie and the store

   CONSEQUENCE WORTH STATING LOUDLY: with no prefixes, `proxy.ts` is now touched exactly ONCE in this
   whole — in the nonce-CSP slice, which is a header concern. **The era-09 constraint that `proxy.ts`
   sets headers and nothing else is therefore never reopened.** The Orchestrator had planned to reopen
   it in writing; his decision made that unnecessary. The highest-risk touch in the whole is gone.

   One factual correction to his premise, made because a wrong premise should not survive even when it
   leads to the right answer: URL prefixes would NOT have required a backend change. They are frontend
   routes. What they would have changed is `proxy.ts` and every internal navigation call. Django
   localization (`USE_I18N`, slice S5) is a separate matter, is unaffected by this decision, and is
   still going ahead — the registration form shows Django's own password-validator text and that text
   must be Slovak.

   Accepted residual that follows: on the very first document request from a brand-new visitor there is
   no locale cookie, so the server renders `lang="en"` and English metadata even for a Slovak browser.
   The client detects, writes the cookie, and every later document is correct. He measured the visible
   effect himself and reported "bez bliku" and "konzola cista". Recorded as `uii-01-F05`, accepted, low.

8  INTERFACE LOCALES: **en + sk + cs + pl.** Decided 2026-09-02, his answer verbatim `1. B`, in reply to
   a three-option package (A `en+sk`; B `en+sk+cs+pl`, recommended; C all five including `hu`) that
   carried the honest cost — roughly triple the translation volume, near-zero architecture cost because
   each locale is one `messages.<locale>.ts` typed `Record<TextKey, string>` and `tsc` names every
   missing key. So the `Locale` union grows from `["en","sk"]` to `["en","sk","cs","pl"]`.
   HUNGARIAN INTERFACE IS NOT SHIPPED, consistent with Hungarian gameplay being blocked on a real
   inflection lexicon. `frontend/public/hu.png` is committed and deliberately UNREFERENCED until
   `11/02`; that is not a defect and must not be "fixed".
   Interface locale and game variant remain TWO INDEPENDENT AXES. B makes them coincide in extent, not
   in meaning: a Slovak speaker playing the Czech variant with a Slovak interface is a normal case.
```

⛔ **TERMINOLOGY: the Cooperator's Czech assumption was WRONG, corrected on primary-source evidence.**
Full record with verbatim quotations and retrieval dates in
`10/00-ui-internationalization/95_orchestrator-terminology.md`. He said Czech `písmeno` is "clearly right
just as in Slovak". The Česká asociace Scrabble rules (`https://scrabble.hrejsi.cz/pravidla`, retrieved
2026-09-02) use **`kámen`** for the physical tile throughout and reserve **`písmeno`** for the letter
printed on it — the two words do different jobs inside one sentence. Czech therefore ships `kámen`.

Conversely his **Slovak** decision is now PROVEN right rather than merely accepted: `sk.wikipedia`'s
Scrabble article uses `písmen*` 29 times and `kameň` **zero** times, so his override of the
Orchestrator's `kameň` / `dlaždica` suggestions matched the actual national convention. Fourth time his
answer beat the Orchestrator's recommendation, first time with a primary source to prove why.

```text
              tile      letter    rack        blank    bag        board          pass        points
en            tile      letter    rack        blank    bag        board          Pass        pts
sk  DECIDED   písmeno   písmeno   zásobník    žolík    vrecko     hracia plocha  Vynechať    b.
cs  EVIDENCED kámen     písmeno   zásobník    žolík    sáček      hrací deska    Vzdát tah   b.
pl  EVIDENCED płytka    litera    stojak      blank    woreczek   plansza        Pauza       pkt
```

Polish is sourced from the Polska Federacja Scrabble regulations (`https://pfs.org.pl/regulaminy.php`,
retrieved 2026-09-02): `płytka` 62, `stojak` 28, `blank` 24, `woreczek` 26. All three handout candidates
were correct. ⚠ **Polish `pass` is `Pauza`, not `Pas`** — `pas` appears ZERO times in those regulations
while `pauza` has its own numbered section 3.4 and 3.4.2 states the player says „pauza". The
Orchestrator's instinct was `Pas` and checking prevented shipping the wrong verb on a primary button.

⚠ **Polish needs a THIRD plural function.** `pluralSk(n, one, few, many)` implements `1 / 2..4 /
otherwise`, which is correct for Slovak **and Czech** (`22 minút`, `22 minut`) but WRONG for Polish,
which keys on the last digit with a 12–14 exception (`22 minuty`, not `22 minut`). A separate `pluralPl`
is required; `pluralSk` is reused verbatim for Czech behind an exported `pluralCs` alias. Points also
abbreviate differently — `pkt` is one character wider than `b.` in the tightest container in the product.

Backend localization route, following from decision 2 and measured rather than assumed: Django
`USE_I18N = True` with a Slovak `LANGUAGE_CODE` supplies bundled Slovak for all four password
validators, username uniqueness, the email validator, and four DRF exception messages. It does NOT
cover `rest_framework_simplejwt` or `django-axes`, neither of which ships an `sk` catalog. The full
probe output is in `10/00-ui-internationalization/90_orchestrator-restoration.md` section 5.3, together
with a recorded candidate finding: `frontend/src/lib/api.ts:122-132` parses the 429 wait time with
`/(\d+)\s+seconds/i` against Django's English body, and should read the numeric `Retry-After` header
instead.

9  ADMIN VERIFICATION LEAVES `ui-internationalization`. Decided 2026-09-02. Acceptance batch B21,
   which would have had him reorder catalog rows in Django admin and inspect GameSession rows, is
   **FROZEN with every item NOT TESTED**, and all admin work belongs to `11/00`. His words: *"admin bola
   odbocka, je to najdolezitejsie pre mna okrem hry proti AI a lokalizacia + UI/UX perfektne.. Toto sa
   ale netyka tvojho logickeho celku prosim Freeze B21"*.

   HE WAS RIGHT AND THE ORCHESTRATOR WAS DRIFTING. Removing the player-facing picker is `10/00` work;
   verifying the admin surface that now owns the setting is not. The Orchestrator had followed the
   evidence across a whole boundary instead of depositing it and stopping.

   His priority order, stated in the same message: **game-vs-AI first, then localization plus UI/UX
   "perfektne", then admin.**

   All measured admin-surface evidence is deposited in
   `11/00-admin-provider-model-console/90_admin_surface_evidence_from_era10.md`, written blind to that
   directory's own `00_handout.md` per his standing do-not-read instruction, and stating that the handout
   wins on any overlap.

   CONSEQUENCE FOR CLOSURE: `10/00` closure condition "the player no longer chooses a model or a prompt
   preset" is **MET** at `383011b` and Cooperator-verified by `B20-5`. It does not require the admin side
   to be demonstrated, and after this decision it must not.

10 NO SCREEN READER, AND HE WILL NOT INSTALL ONE. Decided 2026-09-02 in reply to a direct question, his
   answer: *"Nemám a nechcem ju inštalovať"*. Consequence, and it is a **hard evidence ceiling on every
   accessibility claim this whole makes**:

   ```text
   VERIFIABLE by him, keyboard only   initial focus into the four dialogs · Escape closes each ·
                                      Tab never becomes unescapable · focus NOT restored on close
                                      (uii-01-F19, expected)
   NOT VERIFIABLE by observation      whether the rack tile announces "Písmeno A, 1 bod" · whether the
                                      turn banner, toasts and AI overlay announce AT ALL (uii-01-F22) ·
                                      whether the AI overlay re-reads itself every second (uii-01-F21)
   ```

   So `uii-01-F20`, `uii-01-F21` and `uii-01-F22` are **closed by inspection only**, and any closure
   record must say exactly that instead of implying an observed pass. Do not quietly ask him again, and do
   not let a later session write "accessibility verified" over this. The same discipline the S11 report
   applied to its own node-only suite applies to the whole slice: attributes are present in the markup;
   rendered assistive-technology behaviour is unaudited in this project, by his decision, permanently.

   ⚠ This also retires one line from the ledger's manual-acceptance list: "modal focus trap and ESC" —
   ESC is observable, the focus trap does not exist by design, and the announcement half cannot be
   observed at all.

11 REMEDIATION BEFORE BACKEND. Decided 2026-09-02, his answer to the ordering question: keep the
   Orchestrator's order. Sequence for the rest of `10/00`:

   ```text
   R14  DONE at 74b5339 — uii-01-F21, F22, F20 and the vacuous assertion
   R15  DONE at f40d8a0, ORCHESTRATOR-AUTHORED per decision 12 — uii-01-F24 and uii-01-F23
   R7   DONE at 8f096e1 — USE_I18N, LANGUAGES restricted to the four shipped locales, LocaleMiddleware at
        index 3, api.ts sends Accept-Language parsed from the locale COOKIE, plus uii-01-F17 as a
        FRONTEND-ONLY mapping. It does NOT wrap the ~70 hardcoded backend strings; that stays a residual
        because legality.py:31-46 already exposes REASON_* codes and the frontend catalog is the right
        place to translate them.
        ⛔ HAND-OFF TO R10, CORRECTED: LocaleMiddleware adds `Vary: Accept-Language` and `Content-Language`
        to **Django** responses only. The audit-03 baseline at DEFECT_LEDGER.md:141-153 is the **Next.js**
        loopback readback, which Django middleware cannot touch — so R10's frontend re-probe should differ
        ONLY by what R10 itself changes. An earlier version of this note said otherwise and was wrong.
   R8   DONE at 8ef5992, ORCHESTRATOR-AUTHORED — and it needed TWO halves, not one. Reading the header in
        api.ts alone would have REGRESSED it: Retry-After is not CORS-safelisted, corsheaders emits
        Access-Control-Expose-Headers only when CORS_EXPOSE_HEADERS is non-empty, and it was unset, so
        res.headers.get() would have returned null while every gate stayed green. Prose fallbacks KEPT
        behind the header, deliberately.
   R9   DONE at f983c3d, ORCHESTRATOR-AUTHORED — security.W005 closed, security.W021 (no preload) kept
        standing and PINNED BY TEST as an accepted residual. ⛔ Deployment checklist item: includeSubDomains
        forces HTTPS on every subdomain for a year and is slow to undo.
   R10  DONE at cb4efed — per-request nonce, 'strict-dynamic', 'self' kept as the CSP2 fallback, matcher
        UNCHANGED with conditional /api request propagation. Orchestrator reproduced the loopback proof on
        port 3208: ALL 15/15 <script> tags carried that response's nonce, four distinct nonces across two
        ports, audit-03 diff shows exactly ONE changed directive.
        ⛔ orch-01-F18 is `corrected`, NOT `verified-closed` — that needs the Cooperator's browser.
   R11  ISSUED at cb4efed, Worker session 17 — and the measurement MOVED the defect. Both proxy routes have
        ZERO callers; the app reaches Django directly via api.ts:356/:412. The user-visible swallow is in the
        PAGES: play/page.tsx:104 `.catch(() => [])` then :147/:164 render "the catalog is empty", and
        settings/page.tsx:426 already tracks `ok: false` but :477 ignores it. A slice fixing only the routes
        would have closed audit-01-F06 on paper with every symptom intact.
        uii-01-F13 DECIDED as keep-and-record: four documents describe /api/models, two of them
        (README.md, AGENTS.md) are frozen, and whole 11/00 will need the proxy. Build must still show
        ELEVEN dynamic routes.
        One new key `play.error.catalogUnavailable` in four locales; informal `ty` because this sentence
        addresses the player, deliberately unlike the impersonal history.endReason.* strings.
   B25+ the final acceptance batch, then the residual signatures and 99_closure.md
   ```

   R14 went first deliberately: it fixed a regression S11 itself introduced, and doing it while the
   accessibility markup was fresh was cheaper than closing the whole over a known-wrong announcement
   design. R15 followed for the same reason — `uii-01-F24` is a keyboard regression against `e8cc7bb`, and
   unlike the announcement findings it IS observable by the Cooperator without a screen reader.

12 THE ORCHESTRATOR MAY IMPLEMENT A TEN-LINE CORRECTION OF ITS OWN DEFECT. Decided 2026-09-02 in reply to
   a direct question about who should implement `R15`, his answer: *"Oprav to sama"*. Precedent is
   `f26e92a` in this same whole. The argument he accepted: a 500-line Worker prompt for a ten-line fix is
   disproportionate, and every line of it would have been the Orchestrator dictating the exact edit anyway.

   ⛔ THE COST, AND IT MUST NOT BE FORGOTTEN: **evidence for `f40d8a0` is NON-INDEPENDENT.** For every
   Worker slice the Orchestrator re-measured another agent's work, and twice a Worker corrected an
   Orchestrator claim on evidence — which is precisely the check that an Orchestrator-authored commit does
   not have. Only the mechanical gates corroborate `f40d8a0`; none of its judgement calls do. The
   discipline applied to compensate, and the minimum bar for any future use of this authority:

   ```text
   pre-fix failures CAPTURED, not asserted   the two source files were checked out back to the parent
                                             commit, the focused suite run, the exact failure text
                                             recorded, then the edits restored from a backup and porcelain
                                             re-verified clean
   the one test that did NOT fail pre-fix    named as a test-strength improvement rather than dressed up
                                             as a regression test
   all eight gates                           run in full, not just the focused suite
   the evidence ceiling                      written down: source-asserted handlers are not dispatched
                                             handlers
   ```

   This authority is for correcting the Orchestrator's OWN defect at this scale. It is not a general
   licence to skip Workers, and it does not extend to backend, security, or anything with a trust boundary.

   ⚠ **SUPERSEDED IN PART by decision 13 below.** That last sentence no longer holds: R9 was a security
   setting and was performed by the Orchestrator under decision 13. What survives from decision 12 is the
   EVIDENCE caveat and the four-item discipline, which now apply to every Orchestrator-authored commit.

13 EASY TASKS DO NOT GET WORKERS. Decided 2026-09-03, his words: *"Na easy ulohy nevytvaraj Workerov ale
   ries ich sam"*. A general broadening of decision 12 from "the Orchestrator's own defect" to "anything
   easy", explicitly including backend and security work — R8 and R9 landed under it at `8ef5992` and
   `f983c3d`.

   ⛔ WHAT "EASY" MUST NOT BE ALLOWED TO MEAN: *looks* like one line. R8 looked like one line in `api.ts`
   and was a REGRESSION as one line, because `Retry-After` is not CORS-safelisted and `CORS_EXPOSE_HEADERS`
   was unset, so the new read returned null while every gate stayed green. The measurement that caught it
   took longer than the fix.

   ```text
   THE BAR FOR SELF-IMPLEMENTING, and R8 is why each line is here
   1  measure the whole path before writing, not just the file that obviously changes
   2  capture pre-fix failures by checking the touched files back out to the parent commit, then restore
      from a backup and re-verify porcelain clean
   3  name any test that did NOT fail pre-fix as documentation rather than dressing it up as a regression
      test
   4  run all eight gates, and say plainly if they were run once across several commits
   5  write the evidence ceiling and the NON-INDEPENDENCE into the record every time
   ```

   If a task fails bar 1 — if measuring reveals a second file, a trust boundary, or a design choice — it was
   not easy, and it goes back to a Worker.

14 INFOSEC AND LARGE OR COMPLEX CUTS GET A PLANNER WORKER FIRST. Decided 2026-09-03, his words: *"R10 Ano
   vygeneruj expertny prompt aj pre Planner Workera nie obycajneho Workera a ten budes nasledne
   schvalovat, takto postupujeme pri infosec zalezitostiach a velkych rezoch resp. komplexnych rezoch"*.

   The flow, and it is the counterweight to decision 13 rather than a contradiction of it:

   ```text
   1  Orchestrator writes a PLAN-ONLY prompt, read-only, `Native planning mode: required`
   2  Cooperator delivers it to a fresh Worker session
   3  Planner returns a terminal planning report; planning authority EXPIRES with it
   4  Orchestrator APPROVES, revises once, or rejects with a concrete reason
   5  a separate implementation prompt, `Native planning mode: not-used`, in a FRESH session
   ```

   Contract fields come from `.ap/PROMPT_CONTRACTS.md:716-728` plus the Planning Record at `:89-101`. First
   use: R10, Worker session 15, at `f983c3d`.

   ⛔ `Post-plan implementation session: fresh-worker-session` and `Implementation in same Worker session:
   prohibited` are the right defaults for infosec work, because INFOSEC 4.10 says the corrector never
   self-certifies — a planner implementing its own plan is the closest thing to that this flow allows.
   `Approve`, `Yes`, `Build` or an accepted plan grant NO implementation authority.

   ✅ **FIRST USE COMPLETED, and the planning exchange earned its keep.** Session 15 needed four exchanges
   because of Orchestrator structural defects, but exchange 04's plan delivered three things the Orchestrator
   did not have: `next/experimental/testing/server` exposes `unstable_doesMiddlewareMatch`, which makes the
   first ever test of `proxy.ts` possible; the prerendered `_global-error` document contains a native
   `<form>` + `<button type="submit">`, which narrows that residual to LOW because reload does not need
   JavaScript; and the conditional `/api` propagation decision, which preserves the response headers
   `audit-03` verified while refusing to forward a randomized CSP into route handlers. It also caught an
   Orchestrator error — the audit-03 baseline lives in Meta, OUTSIDE the checkout, so a Worker cannot compare
   against it. ⛔ NEVER point a Worker at `/home/agile/meta/...` as though it were repository evidence;
   inline the evidence into the prompt.

   ⚠ "Called complex is not enough" — `.ap/PROMPT_CONTRACTS.md:711-714` routes to implementation planning
   only when reconnaissance or unresolved alternatives, architecture, migration, security, rollback, or
   cross-layer impact materially affect safe implementation. R10 qualified on three of those, and the
   measurement proved it: Next reads the nonce from REQUEST headers while `proxy.ts:12` only sets the
   response, so the obvious one-file change would have produced a correct-looking header and no nonce
   anywhere.

## 14. Authoritative game alphabet orders — Cooperator-sourced 2026-09-01, Orchestrator-validated

`alphabet_order` is a DECLARED language order for game purposes: tile order, the starting draw, and the
blank picker. It is never derived from `letters[]` and never derived from Unicode collation.

```text
en  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
sk  A Á Ä B C Č D Ď DZ DŽ E É F G H CH I Í J K L Ĺ Ľ M N Ň O Ó Ô P Q R Ŕ S Š T Ť U Ú V W X Y Ý Z Ž
cs  A Á B C Č D Ď E É Ě F G H CH I Í J K L M N Ň O Ó P Q R Ř S Š T Ť U Ú Ů V W X Y Ý Z Ž
pl  A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P R S Ś T U W Y Z Ź Ż
hu  A Á B C CS D DZ DZS E É F G GY H I Í J K L LY M N NY O Ó Ö Ő P Q R S SZ T TY U Ú Ü Ű V W X Y Z ZS
```

Sources he supplied: JÚĽŠ SAV *Pravidlá slovenského pravopisu* (sk, which also states that `DZ`, `DŽ`,
and `CH` are separate letters); Ústav pro jazyk český AV ČR (cs, `CH` between H and I); Rada Języka
Polskiego PAN (pl, 32 letters, `Q V X` explicitly NOT part of the alphabet); MTA *A magyar helyesírás
szabályai* (hu, 40 native letters, eight two-character letters and the three-character `DZS`).

**THE INVARIANT IS A SUBSET, NOT SET EQUALITY.** Measured by the Orchestrator against the real assets:

```text
locale  order tokens   non-blank tile kinds   tiles missing from order   letters with no tile
en          26                26                    none                (0)  —
sk          46                41                    none                (5)  DZ DŽ CH Q W
cs          42                39                    none                (3)  CH Q W
pl          32                32                    none                (0)  —
hu          44                38                    none                (6)  DZ DZS Q W X Y
```

Every non-blank tile token MUST appear exactly once in `alphabet_order`. Requiring the reverse is WRONG
and would fail on the already-shipped Slovak variant, because locked fork 1 states outright that the
Slovak set has no CH/DZ/DŽ tiles. `alphabet_order` must be duplicate-free and NFC.

Consequence: **blank targets come from the TILE SET ordered by alphabet index, not from
`alphabet_order`.** Otherwise a Slovak player could assign a blank to `CH`, which is not a tile in that
variant. `playable_letters` and the BlankPicker both use tile tokens sorted by alphabet position.

Czech caveat he flagged: this array is a deterministic total order for the ENGINE. Normed Czech
dictionary collation per ČSN 97 6030 treats `Á Ď É Ě Í Ň Ó Ť Ú Ů Ý` as their base letter at the primary
level, with diacritics deciding only secondarily. Document `alphabet_order` so nobody later reuses it as
a universal word sorter. Czech is the only one of the five where that confusion is possible.

## 15. Related artifacts

- `/home/agile/meta/README.md` — the Meta storage contract
- `/home/agile/meta/projects/libretiles/09/00-backend-security-hardening/` — the CLOSED security era: the original audit `01_report_00.md`, four audit reports, and the closure record `99_closure.md`
- `/home/agile/meta/projects/libretiles/10/00-ui-internationalization/00_handout.md` — the current whole, and the only place the deployment fact set is written out
- `/home/agile/meta/projects/libretiles/10/00-ui-internationalization/90_orchestrator-restoration.md` — Stage-1 restoration evidence for the current whole, including the measured Django Slovak-coverage probe and the string inventory
- `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — open defects found by Cooperator-executed acceptance
- `/home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/00_handout.md` — the handout for the fresh Orchestrator holding `ui-internationalization` and `atomic-tile-token-foundation`
- `/home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/90_orchestrator-plan-acceptance.md` — the accepted tile-token plan, its three corrections, and the eight decisions
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/INFOSEC.md`, `.ap/PROMPT_ENGINEERING_PATTERNS.md`
