Artifact class: **Orchestrator-authored evidence record**, not a Worker exchange and not authority.
It records Stage-1 Continuation Bootstrap restoration for logical whole `ui-internationalization`
(Meta 10/00), performed by the Orchestrator itself. Task authority comes only from a current
authoritative prompt; protocol meaning from the pinned AP; project truth from the canonical repository.

Filename note: a deliberate, documented local deviation. Meta's grammar reserves
`NN_<phase>_<idx>.md` for Worker exchanges with `NN` a contiguous Worker-session ordinal starting at
`01`, and `00_handout.md` for the handout. Orchestrator-authored non-exchange artifacts in this whole
use a `9N_` prefix so they can never collide with a Worker-session ordinal, mirroring the
`99_closure.md` precedent from `09/00-backend-security-hardening`. Meta naming is storage policy, not
AP meaning. Worker-session ordinal `01` remains unused and reserved for the first real Worker session.

---

# Stage 1 — read-only restoration and reconciliation

Logical whole: `ui-internationalization`
Meta directory: `10/00-ui-internationalization/`
Orchestrator: fresh session, Claude Opus 5 Thinking, write access to the repository
Date of measurement: 2026-09-01
Active mutation: none. Active Worker: none. Nothing issued, nothing committed, nothing pushed.

## 1. Canonical repository state — verified, matches the handout exactly

```text
git rev-parse HEAD                    19cfec9ed27c57e9499b71c55be6c2fb709b0c63   as expected
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   as expected
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   equal to the gitlink
git status -sb                        ## main...origin/main                      no divergence marker
git status --porcelain=v1             (empty)
git ls-remote origin refs/heads/main  19cfec9ed27c57e9499b71c55be6c2fb709b0c63   public readback equal
```

`main` has NOT advanced beyond `19cfec9`. No other Orchestrator has been active. `git log --oneline -14`
matches the twelve era-09 commits recorded in `99_closure.md` plus `7a71180` and `b18e50e` beneath them.

## 2. Standing gates — re-measured by the Orchestrator at `19cfec9`

Execution route: `AGENTS.md` documents `poetry run ...`. Per `PROJECT_CONTEXT.md` section 4 that route
is not usable here because the Cursor AppImage environment intercepts `python*` through inherited
`APPIMAGE` / `PYTHONHOME`. Bounded deviation used, exactly as the project rules prescribe:
`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`. Evidence class
`reproduced-dynamic`. No ambient `python`, `python3`, or `poetry run` was presented as a parallel route.

```text
mypy config game gamecore accounts catalog   Success: no issues found in 80 source files   exit 0
ruff check .                                 All checks passed!                            exit 0
manage.py check                              System check identified no issues (0 silenced) exit 0
pytest                                       328 passed, 4 skipped in 191.24s (0:03:11)    exit 0
npm run typecheck                            tsc --noEmit --incremental false              exit 0
npx vitest run                               Test Files 24 passed | 1 skipped (25)
                                             Tests     326 passed | 3 skipped (329)        exit 0
npm run lint                                 eslint                                        exit 0
npm run build                                NOT RUN — see the honest gap in section 3
```

Every number matches the closure record's baseline. `pytest` was invoked as plain `-m pytest` so the
summary line was not suppressed by the `addopts = "-q"` trap, and the summary is quoted verbatim above.
mypy was run on the full documented scope, not a narrowed path set.

## 3. The one gate NOT measured, and why — stated rather than implied

`npm run build` was deliberately **not** run. `ss -tlnp` shows the Cooperator's own live processes:

```text
127.0.0.1:8000   python            pid 88502     (Django development server)
*:3000           next-server       pid 88574     (child of `next dev --webpack`, pid 88562)
```

`next build` and `next dev` share the `frontend/.next` directory. Running the build while his dev
server is live risks corrupting that directory and breaking a server he is using. `PROJECT_CONTEXT.md`
section 3 forbids asking him for destructive actions but explicitly permits asking him to restart a dev
server, so the correct route is to ask. Recorded here as an open gate rather than reported green.

This is also why `pkill`-style cleanup is forbidden in this whole: `PROJECT_CONTEXT.md` records that the
era-09 Orchestrator stopped its own test server with `pkill -f "next-server"`, a pattern that also
matches pid 88574 above. Any server this Orchestrator starts will be stopped by exact PID.

Consequence for later work: "the build passed" and "the code type-checks" remain two separate claims
(`orch-04-F22`). `npm run typecheck` is measured green above; `npm run build` is unmeasured.

## 4. Reconciliation of the handout against measured truth

| Handout claim | Verdict |
|---|---|
| `main = 19cfec9`, published, porcelain empty, `.ap` gitlink `9c5cc44` | confirmed |
| mypy 80 files, ruff, `manage.py check`, pytest 328/4 | confirmed, re-measured |
| typecheck exit 0, vitest 326/3, lint exit 0 | confirmed, re-measured |
| `npm run build` succeeds | **not re-measured** — see section 3 |
| no active mutation, no active Worker | confirmed |
| three residuals routed here (`orch-01-F18`, `orch-02-D11`, `audit-01-F06`) | confirmed against the ledger and `99_closure.md` |
| `audit-04-F01` / `orch-05-D14` routed to the deployment whole, not here | confirmed; will not be touched |

One drafting defect in the handout itself, recorded because a later reader will hit it: section 4.2
contains a corrupted sentence — *"That is almost certaitrol labelled \"Game language\" reads as an
interface-language switch"* — and section 8 contains a second one — *" not a command runner"*. Both are
recoverable from context and neither changes any instruction. The same class of truncation artifact was
recorded in `DEFECT_LEDGER.md` for the `audit-02` report.

## 5. Evidence gathered for the two architecture decisions

### 5.1 Locale routing (handout 4.1) — the five surfaces are real

Read directly, not inferred:

- `frontend/src/lib/security-headers.ts:70-100` — `connect-src` really is request-derived through
  `resolveConnectApiBase(configuredApiUrl, requestHostname)`, which rewrites a loopback configured host
  to the request hostname. One CSP per locale host would follow, each needing the API origin and the
  websocket origin.
- `frontend/src/lib/security-headers.ts:109-112` — the Next.js proxy emits
  `Strict-Transport-Security: max-age=31536000; includeSubDomains` already, in production only. This is
  the second of the two HSTS emitters; `orch-02-D11` is about Django's, which sets neither flag
  (`backend/config/settings.py:238`, `SECURE_HSTS_SECONDS` only).
- `backend/config/settings.py:101-119` — `ALLOWED_HOSTS` is built from `DJANGO_ALLOWED_HOSTS` and
  rejects wildcards when `DEBUG` is false, by design (`audit-01-F04`). Every locale host must be listed.
- `backend/config/settings.py:226-232` — `CORS_ALLOWED_ORIGINS` likewise, from an explicit env list.
- `frontend/src/proxy.ts` is 29 lines and does exactly one thing: build headers, set them on
  `NextResponse.next()`, and declare a matcher. There is no redirect or rewrite logic in it today.

### 5.2 Two axes (handout 4.2) — confirmed, and the false sentence located

`frontend/src/app/settings/page.tsx:315-378` is `GameLanguagePanel`. Line 341 is the title
`"Game language"`; line 342 is the description
`"Tiles, bag, and lexicon for new games. The interface stays English."` That sentence becomes false in
this whole. The control writes `selectedVariantSlug` (`"english" | "slovak"`) in the Zustand store, i.e.
the game variant, not the interface locale.

### 5.3 Django `USE_I18N` — measured, not assumed

`backend/config/settings.py:216,218` — `LANGUAGE_CODE = "en-us"`, `USE_I18N = False`.

`frontend/src/lib/api.ts:145-171` `humanMessageForStatus` returns Django's OWN field text for HTTP 400
and 409 (`fieldMessage ?? ...`), which is the `acc-01-D03` behaviour. So Django-produced strings really
do reach the user.

A first probe using `override_settings(USE_I18N=True)` inside an already-booted process gave a MIXED
result — `ngettext` translated, `gettext` did not. That probe was **invalid**, not a finding:
`django.utils.translation._trans` is a `Trans` object that resolves and then caches per attribute name
on first access, so attributes touched during `django.setup()` stayed bound to `trans_null`. Recorded
because it is exactly the shape of a false conclusion this project has been bitten by before.

The valid probe set `USE_I18N=True` and `LANGUAGE_CODE="sk"` from process start, through a settings
module outside the repository (`/tmp/opencode/i18nprobe/sk_settings.py`, importing `config.settings`).
Evidence class `reproduced-dynamic`. Repository unmodified. Observed:

```text
COVERED IN SLOVAK BY BUNDLED CATALOGS, at no cost
  This password is too common.        -> Toto heslo je používané príliš často.
  This password is entirely numeric.  -> Toto heslo pozostáva iba z číslic.
  too short (ngettext, min 8)         -> Toto heslo je príliš krátke. Musí obsahovať aspoň 8 znakov.
  username uniqueness                -> Používateľ s takým používateľským menom už existuje.
  Enter a valid email address.        -> Vložte správnu emailovú adresu.
  DRF This field is required.         -> Toto pole je povinné.
  DRF NotAuthenticated                -> Prihlasovacie údaje neboli zadané.
  DRF PermissionDenied                -> K danej akcii nemáte oprávnenie.
  DRF NotFound                        -> Nebolo nájdené.
  auth "Please enter a correct ..."   -> Zadajte prosím správne %(username)s a heslo. ...

NOT COVERED — stays English, because no `sk` catalog ships
  simplejwt  "Token is invalid or expired"     rest_framework_simplejwt/locale/ has no sk
  django-axes lockout text                     axes/locale/ has ar de fa fr id pl ru tr — no sk
  DRF throttle SECOND sentence                 see the finding below

PARTIAL, and it matters
  Throttled(wait=3274).detail ->
    "Požiadavok bol obmedzený, z dôvodu prekročenia limitu. Expected available in 3274 seconds."
```

The `django/contrib/auth/locale/sk/` catalog is where the password validators live, NOT
`django/conf/locale/sk/`. A search of only `django/conf/locale/sk/LC_MESSAGES/django.po` reports all
four password messages MISSING, which is a false negative. Exact patterns that produced that false
negative: `msgid "This password is entirely numeric."`, `msgid "This password is too common."`,
`msgid "The password is too similar to the %(verbose_name)s."` against that one file. The same msgids
are present in `django/contrib/auth/locale/sk/LC_MESSAGES/django.po`. `rest_framework/locale/sk/` ships
a compiled `django.mo` with no `.po`, so a `.po`-only search reports DRF Slovak as absent — also false.

**Candidate finding, needs its own record before any correction.** `frontend/src/lib/api.ts:122-132`
`parseRetryAfterSeconds` extracts the wait time by matching `/(\d+)\s+seconds/i` against Django's 429
body. That depends on the English word "seconds" surviving in the response. It survives today only
because the Slovak DRF catalog leaves that particular fragment untranslated. If `USE_I18N` is enabled
and that fragment is ever translated, `formatThrottleWait` silently degrades from
"Too many requests. Try again in about 55 minutes." to the generic
"Too many requests. Please wait and try again." — a UX regression with no test to catch it. DRF's own
`exception_handler` sets a `Retry-After` response header from `exc.wait`, which is a numeric,
locale-independent source. Classification: product-defect (localization fragility), severity `low`,
confidence `high`, evidence class `established-static` for the coupling plus `reproduced-dynamic` for
the current Slovak string. Not corrected; recorded.

**Design consequence, not yet a decision.** If Django serves Slovak, the locale must be chosen by the
UI, not by the browser. `Accept-Language` is the natural carrier and `LocaleMiddleware` reads it
natively. `CORS_ALLOW_HEADERS` is not set in `backend/config/settings.py`, so `django-cors-headers`
uses its defaults, verified from the installed package as
`('accept', 'authorization', 'content-type', 'user-agent', 'x-csrftoken', 'x-requested-with')` —
`accept-language` is NOT in that list. `Accept-Language` is a CORS-safelisted request header, so it
should not need to appear there; that expectation is **inferred and unverified in a browser** and must
be tested rather than assumed. A custom header such as `X-Locale` would definitely require the CORS
change and is the worse option for that reason.

`backend/config/settings.py:141-153` — current `MIDDLEWARE` order, confirmed:

```text
corsheaders.middleware.CorsMiddleware
django.middleware.security.SecurityMiddleware
django.contrib.sessions.middleware.SessionMiddleware      <- LocaleMiddleware goes after this
django.middleware.common.CommonMiddleware                 <- and before this
django.middleware.csrf.CsrfViewMiddleware
django.contrib.auth.middleware.AuthenticationMiddleware
django.contrib.messages.middleware.MessageMiddleware
django.middleware.clickjacking.XFrameOptionsMiddleware
config.middleware.AxesDrfLockoutFlagMiddleware            <- must stay immediately before
axes.middleware.AxesMiddleware                            <- must stay LAST (axes.W002)
```

`backend/tests/test_admin_login_brake.py` asserts the axes ordering and must be run after any
`MIDDLEWARE` edit.

### 5.4 String inventory — delegated to a read-only subagent, reviewed by the Orchestrator

A subagent produced a file-by-file inventory. Treated as a claim. Its headline numbers:

```text
~411  distinct user-facing literals summed per file
~360  globally distinct after cross-file dedup
 ~48  cross-file repeats, dominated by the three provider-blocker messages (4 files each)
      and six telemetry human-states duplicated between lib/types.ts and api/ai/move/route.ts
~125-130  English text nodes in JSX (between tags), which a quoted-literal grep misses entirely
```

The handout's estimate was "about 156 capitalized user-facing string literals under
`frontend/src/app` and `frontend/src/components`, plus more in `frontend/src/lib`" and "several hundred
strings across roughly forty files". The subagent's ~360 is consistent with the handout's own upper
framing, and its method note explains the gap: a `^[A-Z]` anchored grep rejects lowercase-initial text
nodes (`vs`, `pts`, `zoom`, `human and AI.`), text mixed with `{...}` on one line, and one-character
pluralization suffixes.

Largest files by string count: `app/game/[id]/page.tsx` ~75, `app/settings/page.tsx` ~64,
`components/game/GameHistoryPanel.tsx` ~35, `components/game/ProfileModal.tsx` ~26,
`app/page.tsx` ~23, `app/play/page.tsx` ~23.

Orchestrator spot-verification of the claims that matter most, read directly:

- `frontend/src/app/layout.tsx:15` really is `<html lang="en" className="dark">`, and lines 4-7 really
  are the only `metadata` export in the tree. Confirmed.
- `frontend/src/lib/api.ts:145-171` really is a `switch (status)` with eight messages, and case 401
  really does branch on `requestCarriedToken`. Confirmed — that is the `orch-02-D13` correction and it
  must survive translation.
- `frontend/src/app/settings/page.tsx:341-342` really carries the "The interface stays English"
  sentence. Confirmed.

Two claims from the subagent that are themselves useful findings and that I have not yet independently
re-run:

1. `grep -rn 'aria-label' frontend/src --include=*.tsx --include=*.ts` returned **nothing**, and
   `grep -rn '\balt=' frontend/src --include=*.tsx` returned nothing. If that holds, the product has no
   `aria-label` anywhere, which bears directly on the "accessibility basics: keyboard reachability,
   focus states" item still open in the ledger. To be re-verified with a widened pattern before it is
   written as a finding — a negative grep is not a conclusion.
2. `Intl.DateTimeFormat` is called with a hardcoded `"en-US"` in exactly two places,
   `components/game/GameHistoryPanel.tsx:73` and `components/game/ProfileModal.tsx:22`. Dates will stay
   American in a Slovak interface unless those take the locale.

No i18n library is present. Verified independently: `grep -rniE 'i18n|intl|locale|translat|lingui|polyglot|globalize'`
over `frontend/package.json` and `frontend/package-lock.json` returns exit 1.

### 5.5 Diacritic rendering — measured on this machine

`frontend/src/app/globals.css:34-38` sets the display font stack to
`"Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif` with
`-webkit-background-clip: text`, `background-clip: text`, `color: transparent`, and
`-webkit-text-fill-color: transparent`.

```text
fc-list | grep -icE "Iowan Old Style|Palatino Linotype|Book Antiqua"   0
fc-match Georgia                                                       NotoSerif-Regular.ttf "Noto Serif"
fc-match serif                                                         NotoSerif-Regular.ttf "Noto Serif"
```

So all four named families are absent and the gradient display text resolves to **Noto Serif**, which
has complete Latin Extended-A coverage. `ľ ť ď ĺ ŕ ô ä č š ž` should therefore render. This lowers the
risk the handout flagged but does not close it: a clipped-background gradient over a fallback glyph is
a rendering question, and the Cooperator is the acceptance owner for rendered output. Browser MCP
remains a locked fork; his own eyes are the right instrument.

## 6. Residuals routed here — read, not yet acted on

```text
orch-01-F18  script-src 'unsafe-inline' in production, accepted-residual medium, Cooperator sign-off,
             nonce upgrade routed here. Feasibility input measured: all six page files under
             frontend/src/app carry "use client" (page.tsx, play, settings, game/[id], draw/[id],
             waiting/[id]), so they are prerendered as static shells today. A nonce is per-request, so
             adopting it converts those routes to dynamic rendering. That is precisely the cost the
             residual records. Not yet decided; the sign-off stays intact either way.
orch-02-D11  Django HSTS without includeSubDomains or preload, accepted-residual low, routed here
             because includeSubDomains interacts with the locale-routing decision. Two emitters
             confirmed; this is Django's only. preload is close to irreversible and is its own
             Cooperator decision.
audit-01-F06 public prompt text and swallow-to-HTTP-200 in the catalog proxies, accepted-residual low.
             Confirmed at frontend/src/app/api/models/route.ts:20 and :26 —
             NextResponse.json([], { status: 200 }) on both the !res.ok branch and the catch branch,
             so "no models" and "the backend is down" are indistinguishable to the caller. The same
             shape is expected in .../prompts/route.ts. That is a UX defect as much as a disclosure one
             and this whole touches the surface.
```

Not touched, and must not be: `audit-04-F01` / `orch-05-D14`, routed to the deployment whole.

## 7. Security route selection under `INFOSEC.md`

`INFOSEC.md` activates for this whole because `frontend/src/proxy.ts` — the file that emits every
security header — is the collision point for locale routing, and because auth error text is security
surface.

Primary route selected: **R1 + R2** for the bulk of the translation and UX work (ordinary reversible
slices, no attacker-controlled input, no boundary or secret delta), escalating to **R3** for two
bounded surfaces under INFOSEC 4.2:

1. any change to `frontend/src/proxy.ts` or `frontend/src/lib/security-headers.ts`, because it is a
   trust-boundary emitter — with the loopback header readback re-proved on `/`, `/play`, `/settings`,
   `/game/{id}`, `/waiting/{id}`, `/draw/{id}`, and the `/api/` routes against the `audit-03` baseline;
2. any change to auth or error message text, under INFOSEC 4.4, because the two properties below are
   authentication-disclosure properties rather than copy.

Threat model for the security-touching part of this whole, per INFOSEC 5:

```text
Assets              the localStorage access and refresh tokens; the Django admin session cookie;
                    account existence information
Trust boundaries    browser to Next.js server (proxy header emission); browser to Django API
                    (error text); Next.js server to Django (catalog proxies)
Attacker inputs     request hostname (feeds connect-src), Accept-Language if adopted, submitted
                    username and password
Properties relied on  connect-src blocks exfiltration of the localStorage tokens; a 401 without a
                    token does not differentiate an unknown user from a wrong password; a 401 with a
                    token says the session expired
Abuse cases         user enumeration through a translated login error; header loss through a proxy.ts
                    edit that silently stops emitting the CSP
```

Two acceptance criteria written now, to be checked personally and not delegated:

```text
AC-SEC-1  A 401 WITHOUT a bearer token renders the same message whether the username exists or not,
          in English and in Slovak. Slovak must not say anything of the shape "this name does not
          exist" / "toto meno neexistuje". The English original is "Invalid username or password".
          audit-01-F13 accepts duplicate-username disclosure at REGISTRATION only; that acceptance
          does not extend to login.
AC-SEC-2  A 401 WITH a bearer token renders session-expired wording, distinct from AC-SEC-1, in both
          languages. That is the orch-02-D13 correction and it must not be flattened by translation.
```

## 8. Open at the end of Stage 1

```text
1  npm run build is unmeasured; it needs the Cooperator's dev server (pid 88562 / 88574) stopped
2  the two architecture decisions in handout section 4 are Cooperator decisions and are unmade
3  Slovak register (vy / ty) and the glossary are unset; the glossary must exist before batch 1
4  the aria-label / alt absence needs a widened re-grep before it becomes a finding
5  the throttle-wait "seconds" coupling is recorded as a candidate finding, not corrected
6  the deployment-whole handout and Research-Worker prompt remain a carried-forward obligation
```

No mutation has been performed. No Worker prompt has been issued. Worker-session ordinal `01` is
unused.
