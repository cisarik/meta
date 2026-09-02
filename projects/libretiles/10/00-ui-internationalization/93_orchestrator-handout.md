Artifact class: **Orchestrator handout.** Second handout for logical whole `ui-internationalization`
(Meta 10/00), written after era 11 delivered playable Czech and Polish and materially changed what
remains here. It grants **no** repository, implementation, deployment, production, account,
external-service, credential, or Git mutation authority by itself. Verify everything yourself.

Filename note: a documented local deviation, consistent with `90_`, `91_`, `92_` in this directory.
Orchestrator-authored non-exchange artifacts here use a `9N_` prefix so they can never collide with a
Worker-session ordinal. `00_handout.md` is the **first** handout and is still valid history; where it and
this file disagree, **this file is later and wins**, and every such disagreement is named in section 4.

Written by the era-11 Orchestrator that closed out the tile-token slices, at the Cooperator's explicit
request, for a fresh Orchestrator running **Claude Opus 5 Thinking with write access to the repository**.
Written to the same model, so section 3 names failure modes that model actually exhibited across eras 10
and 11 rather than generic advice.

---

## Handoff capsule

```text
Objective: finish and close 10/00 ui-internationalization. It is the LARGEST single remaining piece of
           work in the project and the most visible one — the Cooperator is presenting Libre Tiles at a
           job interview and the game screen is still entirely English.

Verified state: main = 2917251aba19706e59aea5d50df8cbf353cea7ad, published, porcelain empty except ten
           deliberately untracked files in frontend/public (five source JPEGs, five normalized PNGs).
           .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
           All EIGHT standing gates measured green at that commit by the era-11 Orchestrator:
           mypy 83 files, ruff, manage.py check, pytest 381 passed / 4 skipped,
           npm run typecheck exit 0, npx vitest run 352 passed / 3 skipped,
           npm run lint exit 0, npm run build exit 0.

Active mutation: none. No Worker is active. Nothing is unpushed.
Next owner and bounded next action: YOU. Verify state, then make the ONE open Cooperator decision in
           section 5 before issuing any prompt.
Repeated blocker: none open.
Planning budget: no planning cycle has been consumed for this whole. The slice plan in
           92_orchestrator-glossary-and-plan.md is Orchestrator-authored, not a Worker planning report.
Audit budget: no audit has been performed for this whole. Its risk profile is mostly R0-R2 with two
           genuine R3 touches named in section 8.
This handoff grants no new mutation authority.
```

---

## 0. Required reading, in this order

1. `/home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md` — **in full, first.** Identity, the
   Cooperator profile and his communication rules, the emoji signals, the eight standing gates, the
   mandatory execution deviation, the eleven locked forks, the formed-word invariant, the central
   product fact, the security state, the instruments, the lessons, the environment traps, and
   **sections 12, 13 and 14** which carry his admin-console intent, the seven `ui-internationalization`
   decisions, and the authoritative alphabet orders.
2. `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — the running inventory. **Do not re-test what
   is recorded as verified.** Its era-10 section is your defect list; its era-11 sections tell you what
   changed underneath you.
3. `10/00-ui-internationalization/92_orchestrator-glossary-and-plan.md` — **the most important file for
   this whole.** It carries the glossary the Cooperator decided personally, the three-form Slovak plural
   contract, the dictionary type contract, and the slice plan.
4. `10/00-ui-internationalization/91_orchestrator-decisions.md` — the exchange that produced his seven
   decisions, and the record of what he raised unprompted.
5. `10/00-ui-internationalization/90_orchestrator-restoration.md` — Stage-1 evidence, the measured
   Django Slovak-coverage probe, the string inventory method, and the two security acceptance criteria.
6. `10/00-ui-internationalization/00_handout.md` — the first handout. Read it **after** this file and
   treat section 4 below as its correction list.
7. `10/00-ui-internationalization/01_implementation_00.md` and `01_report_00.md` — the S1 exchange that
   built the foundation you are extending.
8. `/home/agile/Projects/libretiles/AGENTS.md` and `frontend/AGENTS.md`.
9. `.ap/AP.md` — RF-01, RF-02, RF-03, RF-04, RF-05, RF-07, RF-08, RF-12, RF-16, RF-18, RF-19, the Finite
   Convergence Contract, the Continuation Bootstrap.
10. `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`.
11. `.ap/PROMPT_CONTRACTS.md` — **read the exact structural section for the exact artifact you are
    issuing, before you write it.** A previous Orchestrator issued a planning prompt missing all six
    `Planning Record` fields at line 89 and a Worker correctly blocked. `PROMPT_CONTRACTS.md` owns exact
    field spellings; `AP_ORCHESTRATOR.md` prose does not.
12. `.ap/INFOSEC.md` sections 3, 4.1, 4.2, 4.4, 4.10, 5, 6, 7, 14 — one slice touches the file that
    emits every security header, and auth error text is security surface, not copy.
13. `.ap/PROMPT_ENGINEERING_PATTERNS.md` sections 3, 4, 5 and P01, P03, P04, P05, P11. Section 5 is a
    list of anti-patterns; check your own prompts against it before issuing them.

⛔ **Do NOT read the handouts in `10/00-product-acceptance-sweep/`, `10/01-player-model-choice-removal/`,
or `11/00-admin-provider-model-console/`.** Explicit Cooperator instruction, to avoid a loop — they are
handout prompts. Everything you need from them is in `PROJECT_CONTEXT.md` sections 12 and 13, the ledger,
and section 6 R6 below.

---

## 1. Stage 1 — verify before you plan

```text
cd /home/agile/Projects/libretiles
git rev-parse HEAD                      -> expect 2917251aba19706e59aea5d50df8cbf353cea7ad
git rev-parse HEAD:.ap                  -> expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               -> expect the same
git status -sb                          -> expect ## main...origin/main
git status --porcelain=v1               -> expect ONLY the ten untracked files below
git ls-remote origin refs/heads/main    -> expect 2917251aba19706e59aea5d50df8cbf353cea7ad
git log --oneline -8
```

Expected untracked, and **none of it is a defect**:

```text
frontend/public/en.jpeg sk.jpeg cz.jpeg hu.jpeg pl.jpeg   Cooperator-supplied flag sources
frontend/public/en.png  sk.png  cs.png  hu.png  pl.png    Orchestrator-normalized, 48x32, 5230 B total
```

They are deliberately uncommitted: committing image assets before the code that uses them would leave
orphans in the tree. **They are YOURS to commit** — they exist for the flag dropdowns in section 6 R1.
`cz.jpeg` became `cs.png` because the selector chooses a LANGUAGE and the Czech language code is `cs`.

Then independently confirm all eight gates. **Do not run `npm run build` without first checking
`ss -tlnp | grep :3000`** — the Cooperator runs a dev server there and `next build` shares
`frontend/.next` with `next dev`. If it is occupied, ask him to stop it. ⛔ **Never** use a broad pattern
kill such as `pkill -f next-server`; that pattern matches his own server and a previous Orchestrator
survived doing it only by luck. Kill only by exact PID, and only a server you started.

If a gate this handout calls green comes back red, that is your first finding: stop, present the
contradiction, and issue nothing.

---

## 2. The objective, and what it is not

Three things, in one whole because they are the same surface:

1. **Localize the interface**, with English retained and switchable, to Slovak — and now also to Czech,
   Polish and Hungarian, because three of those four are playable languages as of `2917251`.
2. **UX fine-tuning and final touch**, so the product is presentable.
3. **Close the three residuals routed here** from the security era.

The purpose is a **job interview**. Presentability and correctness are first-class requirements, not
polish. A control that does nothing, a layout that breaks in Slovak, or a half-translated screen are
serious defects in his frame. He said this whole is what will be most visible.

**What this is NOT:** it is not engine work. Logical whole `11/01 atomic-tile-token-foundation` is still
open and owns the engine, persistence, the wire format and the AI boundary. Do not touch
`backend/gamecore/`, the wire format, or `frontend/src/lib/prompts.ts`. Section 9 lists what belongs to
whom.

---

## 3. You are Claude Opus 5 Thinking. These are your failure modes.

Across eras 10 and 11, **nine times** someone other than the Orchestrator was right about a claim it was
confident in — six Workers, twice the Cooperator, once a Worker again. The pattern is worth more than any
generic caution.

1. **You state conclusions more precisely than your evidence supports.** An Orchestrator predicted a
   guaranteed hydration mismatch and a visible flash of English, "confidence: high", from code reading.
   The Cooperator opened his console and both predictions were false. Before you write "verified", name
   the command and what it would have missed.
2. **You approximate a contract instead of reading it.** A planning prompt went out missing all six
   `Planning Record` fields because the Orchestrator had read the field *table* and the report *header*
   but never opened `PROMPT_CONTRACTS.md:89`. Read the exact structural section for the exact artifact.
3. **A negative grep is not a conclusion.** Four instances: `selection.py` provider constants; the Django
   password validators, which live in `django/contrib/auth/locale/sk/` and not `django/conf/locale/sk/`;
   `rest_framework/locale/sk/`, which ships a compiled `.mo` with no `.po`; and an `aria-label` sweep
   that had to be widened before it could be written as a finding. When a search returns suspiciously
   few results, widen the pattern and **state the exact pattern that failed to match.**
4. **Your allowlists are too narrow, and this has now happened three times.** Era-09 session 12 blocked
   on `npm run build` failing outside its allowlist. Era-11 F2b needed a ninth path because a refusal
   guard broke a migration test's teardown — and the Orchestrator had **measured that exact hazard two
   slices earlier** and still failed to apply it. **Scope by what the GATES will touch, not only what the
   change touches.** For this whole specifically: a new i18n key touches `messages.en.ts`,
   `messages.sk.ts`, `i18n.test.ts`, and every test that asserts rendered copy.
5. **A green gate set is not a correct product.** Eight green gates — typecheck, lint, build, and 337
   frontend tests — coexisted with a document declaring `<html lang="sk">` and a Slovak `<title>` around
   an entirely English body. vitest runs with `environment: "node"` and nothing renders a page. **For
   anything that renders, render it, or do not claim it.** The technique: production build,
   `next start` bound to loopback on a non-default port, probe with an HTTP client, stop the server by
   **exact PID**.
6. **A faithfully executed prompt can still produce a defective product, and then the prompt is the
   defect.** `uii-01-F04` came from the Orchestrator's own contract, which made the client store the
   source of truth for the locale and called the server-readable cookie "a routing hint only". Classify
   that honestly as an Orchestrator design defect, not a Worker execution defect.
7. **You let a shared reference go stale while carefully updating everything else.** Four stale claims
   were found in `PROJECT_CONTEXT.md` in one pass; a fifth was found in era 11. When a fact changes, grep
   the whole file for the old value, not the section you were thinking about.
8. **You will be tempted to make the translation the interesting part.** It is not. The interesting parts
   are the locale-resolution architecture in section 7, the two security properties in section 8, and the
   dropdown UX in R1. Translation is volume work; getting the routing or the security interaction wrong
   is what breaks the product.
9. **A subagent's output is a claim, exactly like a Worker report.** If you delegate three hundred
   translations to subagents and then accept them, you have delegated the judgement too. Section 10
   defines what you must review personally.

---

## 4. What changed since the first handout — its correction list

Read `00_handout.md` with these corrections applied. Every one is measured at `2917251`.

```text
R2 IS DONE. The first handout's R2 — "the game-variant dropdown must read a DYNAMIC installed-variant
   list from Django, not a hardcoded union" — was DELIVERED by era 11 slice A1. There is now
   GET /api/game/variants/ returning {slug, display_name, language_code, readiness}, a
   VariantSummary type, an authenticated getVariants(), and
   frontend/src/components/settings/GameLanguagePanel.tsx consuming the list with `unavailable` rows
   disabled. DO NOT rebuild it. Extend it.

FOUR VARIANTS EXIST, NOT TWO. english, czech, polish, slovak. Czech and Polish are PLAYABLE with real
   inflected lexicons (3 930 497 and 3 721 704 words). Hungarian is deliberately absent — its lexicon
   is blocked. So the variant list is no longer hypothetical and R4's cs/pl UI translations now serve
   real playable languages.

SelectedVariantSlug IS NOW `string`, persist version 4, with fetch-time reconciliation to the first
   playable row. The old plan assumed a two-value union. Do not narrow it again.

THE NONCE CSP NOW COSTS ZERO ADDITIONAL STATIC PRERENDERING. The first handout and decision 4 costed it
   as "three product routes lose static prerendering". Measured at 2917251: EVERY route is already
   `ƒ` (server-rendered on demand), because layout.tsx reads the locale cookie. That estimate has been
   revised down twice and is now zero. The decision does not change; the cost argument is gone.

GameLanguagePanel IS ALREADY EXTRACTED from settings/page.tsx into its own component with its own test.
   The "two wholes rewriting one 803-line file" worry in 91_orchestrator-decisions.md is partly
   resolved. settings/page.tsx is 813 lines.

THE i18n KEY PATTERN IS PROVEN. Era 11 added czech/polish variant-name keys to both catalogs and the
   `Record<TextKey, string>` contract caught the one-sided case as a tsc error, exactly as designed.
   You are extending a mechanism that has been exercised, not adopting an untested one.

THE BASELINE MOVED. Not 19cfec9 and not 1b7b05d. It is 2917251, with mypy 83 files, pytest 381/4,
   vitest 352/3.
```

---

## 5. The ONE open Cooperator decision — settle it before issuing anything

Everything else is decided. This is not.

**Which locales does the interface ship in, and in what order?**

The `Locale` union is still `["en", "sk"]` at `frontend/src/lib/i18n/locales.ts`. Czech and Polish are
now playable *game* languages, but the *interface* is English or Slovak only. Those are two independent
axes and conflating them is the single easiest way to break this whole — a Slovak speaker playing Czech
Scrabble with a Slovak interface is a normal case.

Put this to him with a recommendation and the cost of each option:

```text
A  en + sk only. Finish Slovak completely, ship, and treat cs/pl/hu interface locales as a later whole.
   Cheapest, lowest risk, and it makes the interview demo fully coherent in two languages.
B  en + sk + cs + pl. Matches the playable game languages. Each added locale is one
   messages.<locale>.ts typed Record<TextKey, string>, and `tsc` names every missing key — so the
   marginal cost per locale is real translation work but near-zero architecture work.
C  all five, including hu. Hungarian interface without Hungarian gameplay is defensible but odd.
```

**Recommendation to put to him: B.** Reasons, and give him all of them: the two playable new languages
deserve their own interface; the type contract makes each additional locale mechanical rather than
architectural; and shipping a Czech-playable game with no Czech interface is exactly the half-localized
tell he would notice. Against B: it roughly triples the translation volume, and he has to live with that.

⛔ **Do not decide this yourself.** It is scope and cost, which RF-01 reserves to him. He has explicitly
asked to be asked LESS, so ask this **once**, with the three options and the recommendation, in one
message — and then do not re-open it.

### The terminology problem he handed to you explicitly

He said, in his own words, that for Czech `písmeno` is clearly right just as in Slovak, but that he does
not know for Polish and Hungarian, and that **you must solve it yourself** and he will report bugs on
the fly.

Take that seriously but not carelessly. The method that produced the correct Slovak answer is recorded in
`92_orchestrator-glossary-and-plan.md`: the Orchestrator offered two options with evidence, and the
Cooperator **overruled both** and chose `písmeno` himself, and he was right. So the method is: research
actual Scrabble usage in that language, present a short evidenced recommendation, and let him overrule.

⚠️ **These are unverified candidates, not decisions. Do not ship them without evidence.** They are here
so you start from something rather than nothing:

```text                tile            rack           blank
Slovak  (DECIDED)      písmeno         zásobník       žolík
Czech   (likely)       písmeno         zásobník       žolík        <- he confirmed písmeno himself
Polish  (UNVERIFIED)   płytka?         stojak?        blank?
Hungarian (UNVERIFIED) betű?           tartó?         joker?
```

Verify Polish against the Polska Federacja Scrabble and Hungarian against an actual Hungarian Scrabble
source before committing either. A wrong core noun appears on every screen.

---

## 6. The remaining work — measured, not estimated

### What is already localized: 55 keys across six areas

```text
draw 13   landing 11   error 11   settings 10   auth 10   meta 2
```

Landed at `a5aff12` (the typed two-locale system, the landing/auth page, the `api.ts` error map, an
Interface language panel, and the Game variant panel relabelled), `f26e92a` (button descriptions
removed at his request), `1b7b05d` (the starting-draw screen), and extended by era 11 with the
czech/polish variant names.

He verified in his own browser: the whole logged-out landing/auth page in Slovak, all seven items
individually; diacritics `ľ ť í ž` render correctly in the gold gradient; console clean after a hard
reload; no flash of English.

### What is NOT localized — the game surface, measured per file at `2917251`

```text
frontend/src/app/game/[id]/page.tsx          70 literals   1822 lines   <- the big one
frontend/src/app/settings/page.tsx           41            813 lines    (only 10 keys done so far)
frontend/src/lib/api.ts                      25            partly done — see the WARNING below
frontend/src/components/game/GameHistoryPanel.tsx  18
frontend/src/components/game/ScorePanel.tsx  15
frontend/src/components/game/ProfileModal.tsx 15
frontend/src/app/play/page.tsx               11
frontend/src/app/waiting/[id]/page.tsx        6
frontend/src/components/game/PromptPreviewModal.tsx  3
```

Fourteen files live under `frontend/src/components/game/`: `AIThinkingOverlay`, `BlankPicker`,
`ChatPanel`, `GameControls`, `GameHistoryModal`, `GameHistoryPanel`, `LuxeHoverText`, `ProfileModal`,
`PromptCatalogModal`, `PromptPreviewModal`, `ScorePanel`, `TurnStatusNotice` plus two test files. The
grep above only counts quoted capitalized literals — **JSX text nodes between tags are invisible to it**,
which is why the era-10 subagent inventory found ~125 more that way. Expect the true figure to be
meaningfully higher than the sum above.

⚠️ **The raw grep OVER-counts too, and this matters.** These files contain capitalized literals that are
**not user-facing copy** and several are under standing locks:

```text
frontend/src/lib/provider-registry.ts     17   LOCK A — providers are FROZEN, do not touch
frontend/src/lib/prompts.ts               13   LOCK B — pinned MOVE CORE hash, do not touch
frontend/src/app/api/ai/move/route.ts     37   mostly tool descriptions and telemetry, not UI copy
frontend/src/app/api/ai/judge/route.ts    12   same
frontend/src/lib/security-headers.ts       8   CSP directive strings
plus provider-capability, ibm-watsonx, ai-move-stream, openai-compatible, ai-runtimes,
    ai-play-diagnostic                        internal, not UI copy
```

Classify before you translate. A "localized" CSP directive or a translated tool name is a defect.

### The residual list, corrected

```text
R1  the two "fancy" Settings dropdowns he described in detail: a flag image left of the language name,
    a search input with diacritic-insensitive autocomplete ("cestina" must match "Čeština"), and an
    arrow at the input edge that opens the dropdown. TWO of them — one for the interface locale, one
    for the game variant. He wants them eye candy, matching the existing premium chrome, not a plain
    white input. The five 48x32 PNGs are ready and untracked and are yours to commit.
    ⚠️ The game-variant one now wraps the EXISTING GameLanguagePanel + VariantSummary list. Extend it.
R2  DONE by era 11 slice A1. Delete it from your plan.
R3  the remaining strings above, extracted into the en catalog with their counterparts. Areas still to
    create: play, queue, waiting, game, controls, board, overlay, chat, history, profile, prompt, a11y.
R4  cs, pl, hu UI translations, subject to the section 5 decision. Additive: one messages.<locale>.ts
    per locale typed Record<TextKey, string>, and `tsc` names every missing key. The Locale union grows.
R5  the LocaleProvider for uii-01-F04. VERIFIED STILL OPEN at 2917251: no LocaleProvider exists
    anywhere in frontend/src, and layout.tsx:12-37 reads the cookie server-side for <html lang> while
    the body renders from the client store. Severity is LOW today (he measured no console error and no
    flash) but it GROWS with R3: after R3 the entire server HTML would be English inside lang="sk".
    It is a prerequisite for R3, not a bug fix. Its correction direction is in the ledger.
R6  remove the player-facing model picker AND the prompt-preset picker, so a player sees only a model
    name. NO database change: leave accounts.User.preferred_ai_model_id, its migrations, its admin
    field, and its is_selectable_model validation, and simply stop writing it from the player UI. That
    makes it admin-settable only, in the direction he wants. Locked fork 11 is NOT engaged — verify
    that yourself before acting, the reasoning is in 91_orchestrator-decisions.md.
R7  backend localization: Django USE_I18N + LocaleMiddleware after SessionMiddleware and before
    CommonMiddleware, axes ordering preserved and test_admin_login_brake.py re-run, Accept-Language
    sent by the API client from the store. The measured Slovak coverage probe is in
    90_orchestrator-restoration.md section 5.3 — bundled Slovak covers all four password validators,
    username uniqueness, the email validator and four DRF messages; it does NOT cover simplejwt or
    django-axes. Do not re-run that probe; it is recorded as verified.
R8  uii-01-F01 — read the numeric Retry-After header instead of parsing "seconds" out of Django's
    English 429 body. It works today only by luck: the Slovak DRF catalog happens to leave that
    fragment untranslated. R7 makes the coupling live.
R9  orch-02-D11 — add SECURE_HSTS_INCLUDE_SUBDOMAINS, do NOT add SECURE_HSTS_PRELOAD.
R10 orch-01-F18 — the nonce CSP. The ONLY remaining proxy.ts touch in this whole, and it is a header
    concern, so the slice-07 constraint "it sets headers and nothing else" is NEVER reopened. Full
    loopback header re-proof afterwards against the audit-03 baseline. Now costs ZERO static
    prerendering — see section 4.
R11 audit-01-F06 — the catalog proxies stop swallowing failures into an empty HTTP 200.
R12 uii-01-F02 accessible names (the product has ZERO aria-label, role, alt, tabIndex, sr-only) and
    uii-01-F03 dates taking the active locale instead of a hardcoded "en-US".
    ⚠️ a11y strings are translatable strings that do not exist yet. Authoring them inside the
    dictionary now costs one pass instead of two. This is the cheapest moment in the project's life.
R13 his acceptance batch, including the three deferred S7b behaviours and the new-game-modal defect.
```

**There are NO URL locale prefixes.** Cooperator decision 7, 2026-09-01, permanent: no `/sk/`, no
`/en/`, no subdomain, not now and not later. He reasoned it himself and he was right — the full cost
analysis is in `PROJECT_CONTEXT.md` section 13. That decision is what keeps `proxy.ts` touched exactly
once in this whole.

---

## 7. The architecture you inherit — use it, do not redesign it

All of this is decided and partly built. `92_orchestrator-glossary-and-plan.md` is the authority.

```text
Register: TYKANIE, informal `ty`. "Tvoj rad", not "Váš rad". Fixed for the whole product including
          error messages. Do not vary it.

Terminology, HIS decisions, not recommendations:
          tile -> písmeno   (NOT kameň, NOT dlaždica — he overruled both)
          rack -> zásobník      blank -> žolík
          provider, model, prompt, fallback, token, chat, API stay UNTRANSLATED
Consequence: a žolík has no letter until resolved, so it must never be called a písmeno in copy. The
          BlankPicker heading is "Vyber písmeno pre žolíka", which reads correctly precisely because
          the two words are distinct.

Slovak needs THREE plural forms and this is the main mechanical trap:
          n == 1        1 písmeno   1 bod    1 slovo   1 ťah
          n in 2..4     2 písmená   2 body   2 slová   2 ťahy
          n == 0, >=5   5 písmen    5 bodov  5 slov    5 ťahov
          A naive one/other implementation produces "2 písmen", which reads as broken Slovak.
          pluralSk(n, one, few, many) exists at frontend/src/lib/i18n/plural.ts. Every counted noun
          goes through it. Points abbreviate to `b.` — shorter than "pts", which helps the score panel
          and sidesteps three forms in the tightest container in the product.

Type contract, and the missing-key mechanism is the TypeScript compiler:
          messages.en.ts is the SHAPE-DEFINING catalog. `Record<TextKey, string>` makes a MISSING
          Slovak key a tsc error AND an EXTRA one a tsc error. `{ [K in FnKey]: (typeof enFn)[K] }`
          forces every parameterized Slovak string to take the identical parameter type. No runtime
          check, no lint rule, no test enumerating keys. Gated by the standing `npm run typecheck`.
          NO NEW DEPENDENCY. That is a decision, not laziness: audit-02 found three high findings in
          the dependency tree the first time anyone looked, and next-intl would want middleware, which
          collides with proxy.ts. If you disagree, make it a Cooperator decision with the audit
          history on the table.

Key naming: area.thing, lowercase-dot. Areas: auth, landing, play, queue, draw, game, controls, board,
          overlay, chat, history, profile, prompt, settings, error, a11y, meta.

Locale resolution, Cooperator decision B2-3 — persisted ON THE DEVICE, not the account:
          source of truth  uiLocale in the persisted Zustand store
          first visit      navigator.language consulted ONCE, never again, so an explicit choice is
                           never overridden by a browser setting
          routing mirror   a non-httpOnly cookie libretiles_locale, consumed by layout.tsx
          server reads     layout.tsx for <html lang> and generateMetadata
          Django           the API client sends Accept-Language derived from uiLocale (R7)
Accepted consequence: layout.tsx reading a cookie makes routes server-rendered rather than prerendered.
          That has ALREADY happened — every route is `ƒ` at 2917251. A Worker must be told this is
          expected, otherwise the build route table looks like a regression and the slice blocks.
```

---

## 8. Security surfaces — treat them as R3, and two things are non-delegable

`INFOSEC.md` activates for this whole. Primary route **R1 + R2** for the bulk of translation and UX,
escalating to **R3** for two bounded surfaces.

**`frontend/src/proxy.ts` is touched exactly once**, for the nonce CSP (R10). It emits every security
header. Re-prove them afterwards by the loopback readback technique: build, `next start` bound to
loopback on a free non-default port — 3000 and 8000 are the Cooperator's — read the headers on `/`,
`/play`, `/settings`, `/game/{id}`, `/waiting/{id}`, `/draw/{id}`, `/api/models`, `/api/prompts`,
`GET /api/ai/move`, and compare directive by directive against the `audit-03` baseline. Stop the server
by exact PID. If you add Django's `LocaleMiddleware` (R7) it goes after `SessionMiddleware` and before
`CommonMiddleware`, `axes.middleware.AxesMiddleware` must remain **last** with
`config.middleware.AxesDrfLockoutFlagMiddleware` immediately before it, and
`backend/tests/test_admin_login_brake.py` asserts that ordering — run it.

**Error messages are security surface, not copy.** Two properties must survive translation into every
locale you ship. Check every translated auth string against them **personally**. This is not delegable.

```text
AC-SEC-1  A 401 WITHOUT a bearer token renders the same message whether the username exists or not, in
          EVERY locale. Slovak must not say anything of the shape "toto meno neexistuje". The English
          original is "Invalid username or password". audit-01-F13 accepts duplicate-username
          disclosure at REGISTRATION only; that acceptance does not extend to login.
AC-SEC-2  A 401 WITH a bearer token renders session-expired wording, distinct from AC-SEC-1, in every
          locale. That is the orch-02-D13 correction and translation must not flatten it.
```

`frontend/src/lib/api.ts` `humanMessageForStatus` is a `switch (status)` whose case 401 branches on
`requestCarriedToken`. That branch **is** AC-SEC-2. Preserve it.

**Do not touch, at all:** the nine AI providers or any provider list, constant, tier, model tuple, or
provider documentation (LOCK A). The MOVE CORE prompt, its pinned SHA-256
`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`, version `pfr-s2-core-1`, and the
single SSE route (LOCK B). The search caps `DEFAULT_MAX_ELAPSED_MS = 2000` and
`DEFAULT_RANKED_MAX_ELAPSED_MS = 750` (LOCK C) — note the first is pinned by a test only since era 11.
The six `completion_source` values (LOCK D). `audit-04-F01` / `orch-05-D14`, routed to the deployment
whole. And the formed-word invariant, the most misread rule in the project.

---

## 9. Boundaries with the open engine whole

`11/01 atomic-tile-token-foundation` is **still open** and owns things that look adjacent to yours.

```text
YOURS          all of frontend/src except prompts.ts and provider files; backend/config/settings.py for
               USE_I18N and HSTS; the catalog proxy routes; proxy.ts once
THEIRS         backend/gamecore/ entirely; the REST and websocket state shape and
               state_schema_version; frontend/src/lib/prompts.ts; the AI move and judge routes;
               frontend/src/lib/types.ts `board` shape; the board/tile/blank-picker RENDERING contract
SHARED, CARE   frontend/src/hooks/useGameStore.ts — they own selectedVariantSlug and persist versioning,
               you own uiLocale. Coordinate the persist version if you both need to bump it.
               frontend/src/components/game/BlankPicker.tsx — they own which tokens it offers, you own
               its heading and accessible names.
```

⛔ **Exactly one Orchestrator is active at a time**, because both push to `main` and each one's pre-push
`ls-remote` equality gate demands exact equality. If `11/01` is mid-slice, coordinate through the
Cooperator rather than racing. A temporary wire adapter exists in `backend/game/services.py`
(`_legacy_wire_board_and_blanks`) that their next slice deletes — do not touch it.

---

## 10. How to do the translation, and what you must not delegate

The Cooperator decided explicitly: **you translate, using your own subagents. No Worker performs
translation.** He wants the model that understands the product doing the language work.

**Personally, not delegated:**

- the section 5 locale decision, put to him once;
- every string in `frontend/src/lib/api.ts` and every auth or error message, against AC-SEC-1 and
  AC-SEC-2;
- the terminology for any new locale, with evidence;
- reviewing every subagent batch against a written checklist before it enters the tree.

**A subagent may** produce candidate translations for a bounded batch of non-security strings, with the
source file and line for each, and a note wherever the English is ambiguous. Give every subagent the same
glossary and the same register rule so batches do not drift apart.

**Concrete traps, all measured:**

- **Slovak text is typically 10-20 percent longer than English.** Buttons, badges and the score panel
  break before prose does. Check the longest strings against the tightest containers, and at a smaller
  window — that is already on his acceptance list.
- **Diacritic rendering is measured and lower-risk than it looks.** `globals.css` sets the display stack
  to `"Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif` with
  `-webkit-background-clip: text`. On this machine all four are absent and it resolves to **Noto Serif**,
  which has complete Latin Extended-A coverage. He has already confirmed `ľ ť í ž` render correctly in
  the gold gradient. Polish `ł ą ę ś ź ż` and Hungarian `ő ű` are the same block; Hungarian `ő`/`ű` are
  Latin Extended-A too. Verify, but do not treat it as an open risk.
- **`<html lang>` is already dynamic** at `layout.tsx:37`. Do not re-do it.
- **Backend-produced strings reach the user deliberately.** The `acc-01-D03` fix shows Django's own field
  text on the registration form, so a Slovak interface with English password errors is half-localized in
  the most visible place a new user reaches. R7 is the fix and its coverage is already measured.

---

## 11. Closure conditions

You may emit ORCHESTRATOR closure for this whole only when all of these hold:

```text
1  the interface is localized to Slovak with English retained and switchable, and to whichever
   additional locales the section 5 decision selected, and he has accepted the rendered result
2  both Settings dropdowns exist with flags, diacritic-insensitive autocomplete and the arrow, and he
   has accepted them
3  the player no longer chooses a model or a prompt preset
4  the three routed residuals are each corrected with evidence or re-recorded as accepted residuals
   with a complete Residual-Risk Decision record INCLUDING their existing Cooperator sign-off.
   Losing a sign-off at closure is a closure failure.
5  the security headers are re-proved on every document route and /api/ route after the nonce CSP
   change, by the loopback readback technique, against the audit-03 baseline
6  AC-SEC-1 and AC-SEC-2 hold in ALL shipped locales
7  all eight standing gates green at the closing commit
8  his acceptance batch has been run and its results recorded
9  no active mutation, no active Worker
10 the Meta archive is complete, including a closure record
```

---

## 12. The Cooperator

Read `PROJECT_CONTEXT.md` section 2 in full. The short version, because it changes how you write:

Address **Michal** in **Slovak**, masculine forms; refer to yourself in **feminine** forms. Worker
prompts and reports are professional **English**. Begin every message with the emoji signal that tells
him what to do, and **end every message with an explicit, emoji-annotated block of what he must do** —
never bury his action in prose. Label manual test steps with a batch prefix (`B17-1`, `B17-2`, …); plain
`1.)` collides with your own numbered list and has caused confusion. The last batch used was `B16`.

His stake is material: a **job interview**, with Libre Tiles as evidence that he can integrate AI into a
real product.

He has granted full trust and asks for initiative. He is also emphatic that he is not the expert. Neither
transfers authority: RF-01 still reserves material product, cost, irreversibility and residual-risk
decisions to him. **He has explicitly asked to be asked LESS** — do not ask him to approve wording or
small choices, decide and show the reasoning. He remains the acceptance owner for rendered output, and
because Browser MCP is a locked fork **his eyes are the only instrument for rendered acceptance**, so
asking him to look is the right tool, not a burden.

His replies are terse — `A`, `ano`, `hotovo`, `PASS`, `obetovatelne`. One one-word reply was once
misread and cost an entire Worker session, so **confirm an ambiguous short instruction in one line**
before spending a session on it. A blanket `PASS` on a multi-item batch means all items passed; record it
as a blanket pass rather than as itemized evidence.

Every time he has been asked a sharp, well-evidenced question he has answered fast and well, and **three
times his answer was better than the Orchestrator's recommendation**: he rejected URL locale prefixes, he
supplied the `alphabet_order` / `letters` separation the engine now rests on, and he was right that the
LibreOffice dictionaries could be re-sourced when an Orchestrator had recorded them as a manual blocker.

### Two artifacts still owed to him, carried across three eras

```text
1  an expert Orchestrator handout for the VPS deployment whole, leading him step by step to a finished
   hardened deployment. He is a self-described complete novice at operations and named Prometheus and
   Grafana specifically as things he does not understand.
2  a prompt for a read-only Research Worker — he has ChatGPT Deep Research — for current VPS-hardening
   practice on Ubuntu Server 24.04, demanding versions and retrieval dates rather than unsourced "best
   practices", and framed so the researcher can honestly answer "this is disproportionate for a single
   demo VPS", particularly about Prometheus and Grafana.
```

The complete fact set those must carry is written out in `00_handout.md` section 10 and summarized in
`PROJECT_CONTEXT.md` section 11. **Copy it from there; do not reconstruct it from memory.** Deployment
happens after the UI/UX work, by his decision 6. The Deep Research route works — era 11 used it
successfully for the Hungarian lexicon question and got a precise, honest, negative-where-warranted
answer.

---

## 13. Meta duties

You have write access to `/home/agile/meta`. **The Cooperator commits Meta himself; write files, do not
commit or push Meta.** Follow `/home/agile/meta/README.md` exactly: filenames
`<worker-session>_<phase>_<meta-exchange-index>.md` and `<worker-session>_report_<meta-exchange-index>.md`,
Meta exchange index = AP exchange ordinal − 1, `<phase>` lowercase kebab-case and never `report`.
Archive a prompt/report pair only **after** the report exists. Contents are exact historical evidence —
**never edit a report to read better.**

This directory is `10/00-ui-internationalization/`. **Worker session `01` is USED** — it built S1.
Your first Worker session in this whole is `02`. Orchestrator-authored non-exchange artifacts use the
`9N_` prefix; `90`, `91`, `92` and this file at `93` are taken, so start at `94`.

Keep `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` current as you go. They are why downstream handouts do
not each carry a drifting copy of the same facts, and they rot quietly if you only update the section you
are thinking about.

---

## 14. What comes after you

```text
YOU    10/00  ui-internationalization  finish and close
       (in parallel, different Orchestrator) 11/01 atomic-tile-token-foundation, still open
then   11/02  Hungarian activation — BLOCKED on a real inflection lexicon. The route is decided:
              keep the pinned LibreOffice/Magyar Ispell source and replace `unmunch` with Spylls,
              which resolves AF aliases and follows suffix continuation flags. It is a CANDIDATE, not
              verified. The full acceptance gate is in DEFECT_LEDGER.md.
then   the deployment whole    handout and Research prompt STILL OWED — section 12
later  11/00  admin-provider-model-console   his stated single most important outcome: add providers
              and models and set the default from Django admin, with NO SSH, plus AI-vs-AI diagnostics
              in every variant and strength testing before promotion. PROJECT_CONTEXT.md section 12
              carries his intent verbatim, including the constraint that a strength metric must rest on
              the completion_source distribution and the provider_candidate rate, NEVER on final score,
              because final score is an engine number and is identical whichever model is plugged in.
later  de-hardcoding the nine AI providers   his declared future whole; LOCK A holds until then
```

Sequencing recommendation, not a decision: land **R5 the LocaleProvider first**, before any bulk
translation. It is the prerequisite that makes the rest correct rather than a bug fix, and every string
you add before it exists makes the `lang="sk"`-around-English-body inconsistency larger. Then R3 in
area-sized slices, then R1, then the security residuals, then his acceptance batch.
