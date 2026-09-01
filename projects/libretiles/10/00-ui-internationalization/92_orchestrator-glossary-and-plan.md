Artifact class: **Orchestrator-authored design and plan record**, not a Worker exchange and not
authority. Logical whole `ui-internationalization` (Meta 10/00). Filename deviation is explained in
`90_orchestrator-restoration.md`.

This file carries the two things the handout reserves to the Orchestrator personally: the dictionary's
type contract with its missing-key mechanism, and the glossary. It also carries the slice plan. The
glossary's durable home is the repository (`frontend/src/lib/i18n/GLOSSARY.md`); this copy is the design
record and the source the first Worker prompt quotes.

---

# 1. Terminology, fixed by the Cooperator on 2026-09-01

Register: **tykanie** (informal `ty`). Fixed for the entire product, including error messages.

He decided three terms personally, and one of them overturned both options the Orchestrator offered:

```text
tile   -> písmeno      NOT kameň, NOT dlaždica. His words: "nechce ani kamen ani dlazdica chcem
                       'písmeno' ako slovenska scrabble terminologia za 'tile'". Recorded as his
                       decision, not as a recommendation the Orchestrator made.
rack   -> zásobník
blank  -> žolík
```

AI-domain terms stay **untranslated**, by his decision: `provider`, `model`, `prompt`, `fallback`.
Extended by the Orchestrator for consistency, as minor wording inside the same decision: `token`,
`chat`, `API`.

## Consequence of `tile -> písmeno` that has to be handled, not assumed away

A **žolík** has no letter until it is resolved, so it must never be called a *písmeno* in copy. The
`BlankPicker` heading becomes "Vyber písmeno pre žolíka" — which reads correctly precisely because the
two words are distinct. Anywhere the product counts rack contents it counts *písmená*, and a resolved
blank counts as one.

## Slovak needs THREE plural forms, not two — this is the main mechanical trap

English pluralization in this codebase is a one-character `"s"` suffix
(`GameControls.tsx:79`, `app/game/[id]/page.tsx:215`). Slovak cannot do that:

```text
n == 1        nominative singular    1 písmeno    1 bod     1 slovo    1 ťah
n in 2..4     nominative plural      2 písmená    2 body    2 slová    2 ťahy
n == 0, n>=5  genitive plural        5 písmen     5 bodov   5 slov     5 ťahov
                                     0 písmen     0 bodov   0 slov     0 ťahov
```

A naive one/other implementation produces "2 písmen" or "2 písmeno", both of which read as broken
Slovak to a native speaker. The dictionary contract therefore carries a three-form helper and every
counted noun goes through it.

Layout mitigation that is also a correctness mitigation: abbreviate points as **`b.`** rather than
spelling `bodov`. `10 b.` is shorter than `10 pts`, which helps the score panel, and it sidesteps the
three-form problem in the tightest container in the product.

## Glossary, as it will be committed

```text
UI CHROME
  Settings              Nastavenia
  Account / Profile     Účet / Profil
  Sign in / Log in      Prihlásiť sa
  Log out               Odhlásiť sa
  Create account        Vytvoriť účet
  Username              Používateľské meno
  Password              Heslo
  Close                 Zavrieť
  Send                  Poslať
  Chat                  Chat
  History               História
  Saved boards          Uložené partie
  Loading / Starting    Načítavam / Spúšťam

GAME OBJECTS
  tile                  písmeno            (1 písmeno / 2 písmená / 5 písmen)
  blank                 žolík
  rack                  zásobník
  board (playing area)  hracia plocha
  board (a saved match) partia
  bag                   vrecko
  premium square        prémiové pole
  word                  slovo              (1 slovo / 2 slová / 5 slov)
  score                 skóre
  point                 bod, abbreviated b. (1 bod / 2 body / 5 bodov)
  move / turn           ťah                (1 ťah / 2 ťahy / 5 ťahov)
  lexicon               lexikón
  dictionary            slovník

GAME ACTIONS
  Your turn             Tvoj ťah
  Place / Submit        Zahrať
  Exchange              Vymeniť        (noun: výmena)
  Pass                  Vynechať       (noun: vynechanie ťahu)
  Shuffle rack          Premiešať
  Recall tiles          Vrátiť písmená
  Give up / Resign      Vzdať sa
  New game              Nová partia
  Play the house        Hrať proti AI
  Join queue            Pripojiť sa do frontu
  Waiting room          Čakárňa
  Victory! / Draw!      Vyhral si! / Remíza!
  Game Over             Koniec partie

OPPONENT
  rival / opponent      súper
  free rival            súper            ("free" is dropped: Libre Tiles is free-only, so the word
                                          adds nothing for a player and costs layout width)
  Choose rival          Vyber súpera
  vs                    vs               (kept; universally understood and the container is 2ch wide)

NOT TRANSLATED, by Cooperator decision
  provider, model, prompt, fallback, token, chat, API
```

Two Orchestrator changes to its own earlier suggestions, recorded rather than quietly swapped:

1. In the decision message the Orchestrator wrote `pass = pas` and said it would decide it alone.
   `pas` is a card-game term. Slovak Scrabble usage is *vynechať ťah*. Changed to **Vynechať**.
2. `free rival -> voľný/bezplatný súper` was considered and dropped. "Bezplatný súper" is clumsy, and
   `PROJECT_CONTEXT.md` section 6 records that Libre Tiles is free-only as a product fact, so a player
   never needs the word. English copy keeps "free rival" where it already exists; Slovak says `súper`.

# 2. Dictionary type contract and missing-key mechanism

Non-delegable Orchestrator design. **No new dependency.** Rationale, which is a decision rather than
laziness: `audit-02` found three high findings in the dependency tree the first time anyone looked, and
`next-intl` would additionally want middleware, colliding with `proxy.ts`. Two locales do not justify
new supply-chain surface.

The missing-key mechanism is **the TypeScript compiler**, gated by the already-standing
`npm run typecheck`. No runtime check, no lint rule, no test enumerating keys.

```ts
// frontend/src/lib/i18n/locales.ts
export const LOCALES = ["en", "sk"] as const;
export type Locale = (typeof LOCALES)[number];
export const DEFAULT_LOCALE: Locale = "en";
export function isLocale(value: unknown): value is Locale { ... }
```

```ts
// frontend/src/lib/i18n/messages.en.ts   — English is the SHAPE-DEFINING catalog
export const enText = {
  "auth.signIn": "Sign in",
  "game.yourTurn": "Your turn",
} as const;

export const enFn = {
  "controls.tilesSelected": (p: { count: number }) =>
    `${p.count} tile${p.count !== 1 ? "s" : ""} selected`,
  "game.aiPlayedFor": (p: { score: number }) => `AI played for ${p.score} pts`,
} as const;

export type TextKey = keyof typeof enText;
export type FnKey = keyof typeof enFn;
```

```ts
// frontend/src/lib/i18n/messages.sk.ts
import type { TextKey, FnKey } from "./messages.en";
import { enFn } from "./messages.en";
import { pluralSk } from "./plural";

export const skText: Record<TextKey, string> = { ... };

export const skFn: { [K in FnKey]: (typeof enFn)[K] } = {
  "controls.tilesSelected": (p) =>
    `Vybrané ${p.count} ${pluralSk(p.count, "písmeno", "písmená", "písmen")}`,
  "game.aiPlayedFor": (p) => `AI zahralo za ${p.score} b.`,
};
```

Why this shape gives exactly what is needed:

- `Record<TextKey, string>` makes a **missing** Slovak key a `tsc` error and an **extra** Slovak key a
  `tsc` error. Both directions, at compile time, with no library.
- `{ [K in FnKey]: (typeof enFn)[K] }` forces every Slovak function to have the **identical parameter
  type** as its English counterpart. A Slovak string cannot silently start needing a different
  parameter, and a renamed parameter is a compile error rather than an `undefined` in rendered copy.
- English is the shape-defining catalog, so adding an English string without its Slovak counterpart
  fails the gate. That is the correct direction: the gate should block half-localized additions.

```ts
// frontend/src/lib/i18n/plural.ts
export function pluralSk(n: number, one: string, few: string, many: string): string {
  const abs = Math.abs(Math.trunc(n));
  if (abs === 1) return one;
  if (abs >= 2 && abs <= 4) return few;
  return many;
}
export function pluralEn(n: number, one: string, other: string): string {
  return Math.abs(n) === 1 ? one : other;
}
```

```ts
// frontend/src/lib/i18n/index.ts
export function t(locale: Locale, key: TextKey): string;
export function tf<K extends FnKey>(
  locale: Locale, key: K, params: Parameters<(typeof enFn)[K]>[0],
): string;
```

Server surfaces — the SSE move route, the judge route, the catalog proxies, `layout.tsx` — have no
store and therefore take `locale` explicitly. There is no ambient locale on the server.

Key naming: `area.thing`, lowercase-dot, area first, so the catalog sorts into the same groups the UI
has. Areas: `auth`, `landing`, `play`, `queue`, `draw`, `game`, `controls`, `board`, `overlay`, `chat`,
`history`, `profile`, `prompt`, `settings`, `error`, `a11y`, `meta`.

The `a11y` area exists because `uii-01-F02` found the product has **zero** `aria-label`, `role`, `alt`,
`tabIndex`, and `sr-only` occurrences. Accessible names are translatable strings that do not exist yet,
so authoring them inside the dictionary now costs one pass instead of two.

# 3. Locale persistence and resolution

Cooperator decision B2-3: persisted **on the device**, not on the account.

```text
Source of truth        `uiLocale` in the persisted Zustand store (localStorage), like
                       `selectedVariantSlug` already is
First visit            navigator.language is consulted ONCE, when `uiLocale` has never been set.
                       `sk*` -> "sk", anything else -> "en". Never re-consulted afterwards, so an
                       explicit choice is never overridden by a browser setting.
Routing mirror         a non-httpOnly cookie `libretiles_locale` mirrors the store. Its ONLY consumer
                       is `proxy.ts`, which cannot read localStorage, and `layout.tsx`, which needs the
                       locale before any client code runs. It is a routing hint, carries no personal
                       data, and is never authority for anything.
Server-side reads      `layout.tsx` reads the cookie for `<html lang>` and `metadata`
Django                 the API client sends `Accept-Language` derived from `uiLocale`
```

Accepted and named consequence: `layout.tsx` reading a cookie makes `/`, `/play`, and `/settings`
server-rendered on demand instead of prerendered static. That is the SAME cost decision 4 (nonce CSP)
already accepts, so it is paid once rather than twice. **A Worker must be told this is expected**,
otherwise the changed `npm run build` route table looks like a regression and the slice blocks.

# 4. Slice plan

**REVISED 2026-09-01 after Cooperator decision 7 (no URL locale prefixes at all).** The original plan
is kept below the revision so the change is legible rather than silently swapped.

Ordered by risk and by reviewability, not by convenience. `PROMPT_ENGINEERING_PATTERNS` P05 and the
era-09 lesson that one allowlist covering a dependency addition, an authentication change, a
fail-closed guard, four frontend changes, a shell script, and three documents produces a diff nobody
can review honestly.

## Current plan

```text
S1  i18n foundation                         Worker 01   R1   LANDED a5aff12, accepted
      dictionary contract, plural helpers, glossary, locale store + cookie mirror + first-visit
      detection, dynamic <html lang> and generateMetadata, and the auth + landing proving area plus
      the api.ts error map. Followed by the Orchestrator-authored copy removal at f26e92a.

S2  locale path-prefix routing              CANCELLED by Cooperator decision 7
      There are no /sk/ or /en/ prefixes. proxy.ts is not touched for routing. The era-09 constraint
      "it sets headers and nothing else" is therefore NEVER reopened in this whole.

S3a play, queue, draw, waiting  + LocaleProvider     Worker   R1
      The uii-01-F04 LocaleProvider moves here rather than into a dedicated correction slice, because
      a provider without localized pages cannot be meaningfully tested. Carries the SSR regression
      test uii-01-F04 needs: request `/` from a production `next start` with the sk cookie and assert
      Slovak copy in the server HTML.
S3b game, controls, board, overlay, chat              Worker   R1
S3c history, profile, prompt, settings, error, a11y   Worker   R1

S4  remove the player-facing pickers        Worker   R1
      Model picker and prompt-preset picker removed so a player sees only a model name. NO database
      change: accounts.User.preferred_ai_model_id stays, keeps its migrations, its admin field, and
      its is_selectable_model validation, and simply stops being written from the player UI — which
      makes it admin-settable only, in the direction the Cooperator wants. Locked fork 11 verified NOT
      engaged: none of the five frozen files is touched and no provider is added, removed, or renamed.
      Be precise: this delivers "the player does not choose". It does NOT deliver "the admin sets the
      GLOBAL default", which is still catalog row 1 determined in code and belongs to the
      admin-console whole.

S5  backend localization                    Worker   R1+R2
      Django USE_I18N + LocaleMiddleware after SessionMiddleware and before CommonMiddleware; axes
      ordering preserved and test_admin_login_brake.py re-run; Accept-Language sent by the API client
      from the store; uii-01-F01 corrected by reading the numeric Retry-After header; orch-02-D11
      includeSubDomains added, preload NOT added.

S6  nonce CSP                               Worker   R3
      orch-01-F18. The ONLY proxy.ts touch in this whole, and it is a header concern, so the slice-07
      constraint holds rather than being reopened. Full loopback header re-proof on /, /play,
      /settings, /game/{id}, /waiting/{id}, /draw/{id}, /api/models, /api/prompts, GET /api/ai/move
      against the audit-03 baseline. Server stopped by exact PID.

S7  diagnosability and polish                Worker   R1
      audit-01-F06 catalog proxies stop swallowing failures into an empty 200; uii-01-F02 accessible
      names; uii-01-F03 dates take the active locale; the longest-string layout pass at a smaller
      window.

S8  Cooperator-executed acceptance          Cooperator
      batch-prefixed PASS/FAIL/PARTIAL, including the three deferred S7b behaviours and the two known
      UX defects.
```

Deployment artifacts remain owed and are scheduled between S7 and S8, per his item-6 qualification:
the expert Orchestrator handout for the VPS deployment whole, and the read-only Research Worker prompt
for ChatGPT Deep Research.

## What the revision changed, and why it is an improvement

```text
before  8 slices, TWO proxy.ts touches (S2 routing at R3, S6 nonce at R3), the "headers and nothing
        else" constraint reopened in writing, every internal router.push and <Link> made
        locale-aware, and a third source of locale truth (URL) to reconcile
after   the same 8 slices minus S2, ONE proxy.ts touch (S6, headers only), the constraint intact,
        no navigation changes, and two sources of locale truth (cookie for the server, store for
        persistence) with the provider making them agree
```

The Orchestrator recommended the prefix. The Cooperator overrode it after thinking about it and was
right. Recorded as such.

# 5. What the Orchestrator does not delegate

Per the handout and re-affirmed here:

```text
the two architecture decisions                          done, section 13 of PROJECT_CONTEXT.md
every string in frontend/src/lib/api.ts and every auth or error message, checked against AC-SEC-1
  and AC-SEC-2 in 90_orchestrator-restoration.md section 7
the dictionary type contract and the missing-key mechanism                 section 2 above
the glossary                                                              section 1 above
review of every subagent batch against a written checklist before it enters the tree
```

A subagent may produce candidate Slovak for a bounded batch of non-security strings, with file and line
for each and a note wherever the English is ambiguous. Every subagent receives the same glossary and the
same register rule so batches do not drift.
