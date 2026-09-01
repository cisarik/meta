# Orchestrator handout — `ui-internationalization`

Artifact class: **Orchestrator handout.** First handout for this logical whole. It grants **no**
repository, implementation, deployment, production, account, external-service, credential, or Git
mutation authority by itself. Verify everything yourself.

Written by the Orchestrator who closed `backend-security-hardening`, at the Cooperator's explicit
request, for a fresh Orchestrator running **Claude Opus 5 Thinking with write access to the
repository**. That matters: this handout is partly a prompt written to the same model, so section 3
names failure modes that model actually exhibited during the previous era rather than generic advice.

---

## Handoff capsule

```text
Closure candidate: logical whole `ui-internationalization` (Meta 10/00).
Report justification: sequential handoff — the previous whole closed cleanly.
Verified state: main = 19cfec9ed27c57e9499b71c55be6c2fb709b0c63, published, porcelain empty,
                .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
                Gates green at that commit, Orchestrator-measured: mypy 80 files clean, ruff clean,
                manage.py check clean, pytest 328 passed / 4 skipped, npm run typecheck exit 0,
                npx vitest run 326 passed / 3 skipped, npm run lint exit 0, npm run build succeeds.
Active mutation: none. No Worker is active. Nothing is unpushed.
Residual risks / open decisions: `backend-security-hardening` closed with 32 findings verified-closed
                and every residual dispositioned. Three of its residuals are ROUTED HERE — see
                section 5. One is routed to the deployment whole and must not be touched here.
Next owner and bounded next action: YOU. Verify state, then make the two architecture decisions in
                section 4 with the Cooperator before writing any code.
Repeated blocker: none open.
Audit / handoff budget: no audit has been performed for this whole. Its risk profile is mostly R0-R2,
                with two genuine R3 touches named in section 6.
This handoff grants no new mutation authority.
```

## 0. Required reading, in this order

1. `/home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md` — **in full, first.** Identity, the
   Cooperator profile and his communication rules, the emoji signals, the standing gates, the
   execution-route deviation, the eleven locked forks, the formed-word invariant, the central product
   fact, the complete security state, the instruments, the lessons, the environment traps. It exists
   so this handout does not repeat them and so the copies cannot drift.
2. `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — the running defect inventory, current at
   `19cfec9`. **Do not re-test what is recorded as verified.**
3. `/home/agile/meta/projects/libretiles/09/00-backend-security-hardening/99_closure.md` — what the
   previous era established, what it deliberately left, and its seven lessons.
4. `/home/agile/Projects/libretiles/AGENTS.md` and `frontend/AGENTS.md`
5. `.ap/AP.md` — at minimum RF-01, RF-02, RF-03, RF-08, RF-12, RF-16, RF-18, RF-19, the Continuation
   Bootstrap, and the Defensive-Security Task Anchor
6. `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`
7. `.ap/INFOSEC.md` sections 3, 4.1, 4.2, 4.10, 5, 6, 7, 14 — you will touch the file that emits every
   security header, so the profile activates
8. `.ap/PROMPT_ENGINEERING_PATTERNS.md` sections 3, 4, 5, and P01, P03, P04, P05, P11. Section 5 is a
   list of anti-patterns; check your own prompts against it before issuing them.

## 1. Stage 1 — verify before you plan

```text
cd /home/agile/Projects/libretiles
git rev-parse HEAD                      -> expect 19cfec9ed27c57e9499b71c55be6c2fb709b0c63
git rev-parse HEAD:.ap                  -> expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               -> expect the same
git status -sb                          -> expect ## main...origin/main
git status --porcelain=v1               -> expect empty
git ls-remote origin refs/heads/main    -> expect 19cfec9ed27c57e9499b71c55be6c2fb709b0c63
git log --oneline -14
```

Then independently confirm the standing gates from `PROJECT_CONTEXT.md` section 4, **including the new
`npm run typecheck`**. If a gate this handout calls green comes back red, that is your first finding:
stop, present the contradiction, and issue nothing.

If `main` has advanced beyond `19cfec9`, another Orchestrator has been active. Establish who and what
before issuing any mutating prompt. Exactly one Orchestrator is active at a time.

## 2. The objective, and what it is not

Three things, in one whole because they are the same surface:

1. **Localize the user interface to Slovak**, with English retained and switchable.
2. **UX fine-tuning and final touch**, so the product is presentable.
3. **Close the three residuals routed here** from the security era.

The purpose is a **job interview**. The Cooperator will present Libre Tiles as evidence that he can
integrate AI into a real product. Presentability and correctness are first-class requirements, not
polish. A control that does nothing, a layout that breaks in Slovak, or a half-translated screen are
serious defects in his frame.

**What this is NOT:** it is not enabling Slovak *gameplay*. `AGENTS.md` records that the Slovak assets
ship but that Settings/engine/prompt wiring belongs to later slices of `slovak-playable-variant`
(Meta 05/00), and that live Slovak play is not enabled until those land. **Localizing the interface
chrome and enabling the Slovak lexicon are two different axes and conflating them is the single
easiest way to break this whole.** See section 4.2.

## 3. You are Claude Opus 5 Thinking. These are your failure modes.

The previous Orchestrator was the same model. Five times a Worker contradicted it with evidence and
five times the Worker was right. The pattern in those five is worth more to you than any generic
caution:

1. **You state conclusions more precisely than your evidence supports.** It reported "gates green" at
   five commits while `npm run build`'s typecheck was partly served from an incremental cache. It was
   not lying; it just did not distinguish "the command exited 0" from "the check actually ran". Before
   you write "verified", name the command and what it would have missed.
2. **You treat a negative grep as a conclusion.** It grepped `selection.py` for `*_PROVIDER =`
   constants, found two, and wrote in two durable files that the backend knew about two providers. All
   nine were there as string literals. **When a search returns suspiciously few results, widen the
   pattern before writing a finding, and state the exact pattern that failed to match.**
3. **You write allowlists that are too narrow and then a Worker blocks.** Session 12 stopped because
   `npm run build` failed on two files outside its allowlist. The Worker was right; the allowlist was
   wrong. When you scope a slice, ask what the *gates* will touch, not only what the *change* touches.
4. **You propose remedies without reading the defaults.** It recommended installing
   `django-axes[ipware]` to fix a proxy-identity problem. The package's defaults would have made that
   remedy a no-op, and one plausible half-step would have converted a denial-of-service weakness into
   a full authentication-brake bypass. **Read the installed `conf.py` before you name a fix.**
5. **You let a shared reference go stale while carefully updating everything else.** It updated the
   gate, dependency, and security sections of `PROJECT_CONTEXT.md` and left section 1 describing the
   wrong Next.js version, the wrong Django version, and a file that no longer existed. A re-auditor
   caught it. **When a fact changes, grep the whole file for the old value, not the section you were
   thinking about.**
6. **You use broad patterns for destructive operations.** It stopped a test server with
   `pkill -f "next-server"`, a pattern that also matched the Cooperator's own development server. It
   survived by luck. Kill by exact PID.

Two more that matter specifically for **this** whole, because you will use subagents:

7. **A subagent's output is a claim, exactly like a Worker report.** The previous era's core discipline
   was re-verifying every material Worker claim. If you delegate three hundred translations to
   subagents and then accept them, you have delegated the judgement too. Section 7 defines what you
   must review personally and what you may delegate.
8. **You will be tempted to make the translation the interesting part.** It is not. The interesting
   part is the two architecture decisions in section 4 and the security surfaces in section 6.
   Translation is volume work; getting the routing and the security interaction wrong is what breaks
   the product.

## 4. Two architecture decisions, before any code

Both are **Cooperator decisions** under RF-01 because they are product and irreversibility trade-offs.
Present them with a recommendation and evidence; do not decide them yourself.

### 4.1 Locale routing: path prefix or subdomain?

The original era-09 handout named "the subdomain-locale feature" as part of this whole. **Before
implementing it, put the following in front of the Cooperator**, because it was written before the
security era and the security era changed what a subdomain costs.

`sk.example.com` / `en.example.com` touches **five** surfaces that the previous era just finished
hardening:

- **CSP `connect-src` is request-derived.** `frontend/src/lib/security-headers.ts` builds it from the
  request hostname, mirroring `resolveApiBase()`. Every locale subdomain gets its own policy and each
  must still permit the API origin and the websocket origin. Verified working for one host; never for
  several.
- **HSTS `includeSubDomains`.** This is exactly `orch-02-D11`, routed here. Django currently sends HSTS
  with neither flag; the Next.js proxy sends `includeSubDomains` already. A subdomain-per-locale layout
  makes that flag consequential rather than theoretical.
- **`ALLOWED_HOSTS`** must list every locale host, and it rejects wildcards when `DEBUG` is false by
  design (`audit-01-F04`).
- **`CORS_ALLOWED_ORIGINS`** likewise.
- **The Django admin session cookie** is a real credential (`PROJECT_CONTEXT.md` section 7). Cookie
  domain scope across subdomains is a decision, not a default.

A path prefix — `/sk/...` and `/en/...` — costs **none** of those. Same origin, one CSP, one host, one
cookie scope.

**Recommendation to put to him: path prefix now; subdomain as a separate later decision if he ever
wants it for SEO or for a marketing reason.** The interview does not need subdomains and they convert
a UI task into a five-surface security task. Say that plainly, and say that you are recommending
against something an earlier handout named, and why.

### 4.2 Two independent axes, and the UX defect that proves they are confused today

`frontend/src/app/settings/page.tsx` has `GameLanguagePanel` at line 315. It selects the **game
variant** — tiles, bag, and lexicon — and its own description says: *"Tiles, bag, and lexicon for new
games. The interface stays English."*

That sentence becomes false in this whole, and it is your anchor. There are **two axes**:

```text
game variant     english tiles + Collins 2019   |   slovak tiles + SSS lexicon
interface locale English chrome                 |   Slovak chrome
```

Four combinations, all legitimate. A Slovak-speaking user playing English Scrabble with a Slovak
interface is a normal case.

The defect ledger records a known UX defect the Cooperator reported: **"Settings appearing to change
the language during a game."** That is almost certainly this confusion — a control labelled "Game
language" reads as an interface-language switch. Fixing the labelling and separating the two controls
visually is probably the single highest-value UX change in this whole, and it costs almost nothing.

Present to the Cooperator: does he want an interface-language switch in Settings, browser-language
detection, or both? And confirm that changing the game variant mid-game must remain impossible —
`PROJECT_CONTEXT.md` records that `variant_slug` is only ever set at game creation and that a running
game's variant cannot be swapped. That is a *verified non-issue* and must stay one.

## 5. The three residuals routed here

Read each one's full record in the ledger before acting. None may be closed by assertion; each needs
its own evidence.

**`orch-01-F18` — `script-src 'unsafe-inline'` in production, accepted `medium` with Cooperator
sign-off, nonce upgrade routed here.** The reason it was routed here is exact: a nonce CSP needs
dynamic rendering on `/`, `/play`, and `/settings` — the pages this whole rewrites anyway. If you
implement it, `style-src 'unsafe-inline'` is a separate lower-value question because Framer Motion sets
inline `style` attributes. **If you do not implement it, say so explicitly and leave the residual and
its sign-off intact.** Do not silently drop a routed item.

**`orch-02-D11` — Django HSTS without `includeSubDomains` or `preload`, accepted `low`, routed here.**
It is routed here because `includeSubDomains` interacts with 4.1. Note the precision the re-audit
established: there are **two** HSTS emitters and this finding is about Django's only. `preload` is close
to irreversible once submitted to the browser preload list and is its own Cooperator decision.

**`audit-01-F06` — public prompt text and swallow-to-HTTP-200 in the catalog proxies, accepted `low`.**
`frontend/src/app/api/models/route.ts` and `.../prompts/route.ts` return
`NextResponse.json([], { status: 200 })` when Django fails. A caller cannot distinguish "no models" from
"the backend is down", which is a UX defect as much as a disclosure one. This whole touches that surface.

## 6. The security surfaces this whole will touch — treat them as R3

The previous era spent five slices and four audits on these. Do not undo it. `INFOSEC.md` activates
here; select the route per section 3 of that document and record it.

**`frontend/src/proxy.ts` is the collision point, and you must reopen a constraint deliberately.**
That file emits every security header. The S7b prompt explicitly forbade putting redirect or rewrite
logic in it: *"It sets headers and nothing else."* Locale routing needs exactly that logic, in exactly
that file. So:

- reopen that constraint **explicitly, in writing, with the reason**, rather than letting it erode;
- keep header emission and locale routing separable and separately tested;
- **re-prove the headers afterwards.** The technique now exists and is cheap: build, `next start` bound
  to loopback on a free non-default port — 3000 and 8000 are the Cooperator's — then read the headers
  with an HTTP client on `/`, `/play`, `/settings`, `/game/{id}`, `/waiting/{id}`, and the `/api/`
  routes, and compare directive by directive against `buildSecurityHeaders`. The `audit-03` re-auditor
  established the full-route baseline; match it or explain every difference. Kill the server by exact
  PID.
- `axes.middleware.AxesMiddleware` must remain **last** in Django's `MIDDLEWARE` with
  `config.middleware.AxesDrfLockoutFlagMiddleware` immediately before it. If you add Django's
  `LocaleMiddleware` (see below) it goes after `SessionMiddleware` and before `CommonMiddleware`, and
  `backend/tests/test_admin_login_brake.py` asserts the axes ordering. Run it.

**Error messages are security surface, not copy.** The previous era ended with a deliberate map in
`frontend/src/lib/api.ts` `humanMessageForStatus`. Two properties must survive translation:

- **401 without a token must not differentiate an unknown user from a wrong password.** English says
  "Invalid username or password". A Slovak translation that says *"Toto meno neexistuje"* would create
  a user-enumeration disclosure that the English original does not have. `audit-01-F13` accepts
  duplicate-username disclosure at *registration*; that acceptance does not extend to login.
- **401 with a token says the session expired, not that credentials are wrong** (`orch-02-D13`). Keep
  the two distinct in Slovak too.

Write those two as explicit acceptance criteria and check every translated auth string against them
personally. This is not delegable.

**Do not touch, at all:** the nine AI providers or any provider list, constant, tier, model tuple, or
provider documentation — standing Cooperator decision, `PROJECT_CONTEXT.md` locked fork 11. The
`MOVE CORE` prompt and its pinned SHA-256, `MOVE_PROMPT_VERSION` `pfr-s2-core-1`, and the single SSE
route — locked fork 2. The search caps in `backend/gamecore/move_search.py` — locked fork 9. The six
`completion_source` values — locked fork 10. `audit-04-F01` / `orch-05-D14`, which is routed to the
deployment whole. And the formed-word invariant, which is the most misread rule in the project and is
stated in `PROJECT_CONTEXT.md` section 5.

## 7. How to do the translation, since you do it yourself

The Cooperator has decided explicitly: **you translate, using your own subagents. No Worker performs
translation.** He wants the model that understands the product doing the language work, not a fresh
session guessing at tone.

Rough scale, measured at `19cfec9`: about 156 capitalized user-facing string literals under
`frontend/src/app` and `frontend/src/components` alone, plus more in `frontend/src/lib`. Expect several
hundred strings across roughly forty files, including thirteen components under
`frontend/src/components/game/`.

**No new dependency, and here is why that is a decision rather than laziness.** There is no i18n
library in `package.json` today. `audit-02` — the first dependency audit this project ever had — found
three high findings in the dependency tree, and `next-intl` would also want middleware, which collides
with `proxy.ts` (section 6). A typed dictionary module with two locales and a compile-time
exhaustiveness check gives you missing-key detection from TypeScript itself, adds zero supply-chain
surface, and is entirely proportionate for two languages. If you disagree, make it a Cooperator
decision with the audit history on the table; do not add a dependency quietly.

**What you must do personally, not delegate:**

- the two architecture decisions in section 4;
- every string in `frontend/src/lib/api.ts` and every auth or error message, against the two security
  properties in section 6;
- the dictionary's type contract and the missing-key mechanism;
- reviewing every subagent batch against a written checklist before it enters the tree.

**What a subagent may do:** produce candidate Slovak for a bounded batch of non-security strings, with
the source file and line for each, and a note wherever the English is ambiguous. Give each subagent the
same glossary and tone rules so batches do not drift apart.

**The glossary is the thing that decides whether this reads professional.** Write it before the first
batch and keep it in the repository next to the dictionary. Decide once, then never vary: how to
address the user (Slovak `vy` versus `ty` — this is a game, and the Cooperator's own register is
informal, but ask him), what a "tile", a "rack", a "blank", an "exchange", a "pass", a "bag", a "score"
and a "premium square" are called in Slovak Scrabble usage, and whether AI-domain terms like "provider",
"model", "fallback", and "prompt" are translated or kept. Slovak Scrabble has established vocabulary;
use it rather than inventing.

**Verify these, because they are the concrete traps:**

- **Slovak text is typically 10-20 percent longer than English.** Buttons, badges, and the score panel
  will break before the prose does. The Cooperator's own acceptance list already includes "layout at a
  smaller window". Check the longest strings against the tightest containers.
- **Diacritic rendering.** `frontend/src/app/globals.css` sets the display font stack to
  `"Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif` with
  `-webkit-background-clip: text` and `color: transparent`. On Linux the first three are absent, so the
  gold-gradient text falls back to Georgia or a system serif. `ľ`, `ť`, `ď`, `ĺ`, `ŕ`, `ô`, `ä` are
  Latin Extended-A and should be covered — but a clipped-background gradient on a fallback glyph is
  exactly where rendering surprises live. **Verify visually, and ask the Cooperator to confirm on his
  own machine.** He is the acceptance owner for rendered output.
- **`<html lang="en">` is hardcoded** at `frontend/src/app/layout.tsx:15`. It must become dynamic.
  `layout.tsx` has a wide blast radius and slice 07 deliberately avoided it; treat it as a real change.
- **Backend-produced strings.** `USE_I18N = False` and `LANGUAGE_CODE = "en-us"` in
  `backend/config/settings.py`. But Django produces user-visible text that the frontend now
  deliberately surfaces: `validate_password` messages such as "This password is entirely numeric.",
  `ChangePasswordSerializer`'s "Current password is incorrect.", the DRF throttle message, and the axes
  lockout message. **The `acc-01-D03` fix deliberately shows the server's own field text on the
  registration form** — so a Slovak interface with English password errors is half-localized in the
  most visible place a new user reaches.
  There are two ways out. Turning on Django's `USE_I18N` with `LocaleMiddleware` and a Slovak locale
  gets Django's own bundled Slovak translations for the auth validators **for free**, which is elegant
  and cheap; it costs one middleware entry whose ordering you must reconcile with section 6. Or map
  known messages on the frontend, which is fragile string matching and is precisely the anti-pattern
  the previous era removed when it replaced `err.message.includes("401")` with a numeric status.
  **Recommendation: Django `USE_I18N`.** Verify the bundled Slovak coverage yourself before committing
  to it; do not assume it from this handout.

## 8. UX fine-tuning, and the Cooperator-executed acceptance this whole inherits

`product-acceptance-sweep` as a standalone whole is superseded; its remaining items are UI observations
and belong here. The full list is in the ledger under "Not yet covered by manual acceptance". Plus
three behaviours from the security era that could not be automated and were explicitly deferred:

```text
1  registering with an all-numeric password shows the server's password error and issues NO login
2  logout still clears local state and redirects when the logout request fails
3  an ordinary websocket close shows no error toast; close code 4503 shows a realtime-unavailable message
```

And two known UX defects the Cooperator reported himself:

```text
the new-game modal does not appear after "Play the house"
Settings appears to change the language during a game    <- almost certainly section 4.2
```

**He is the acceptance owner for everything rendered.** Browser MCP is a locked fork by his explicit
decision — prefer CLI, HTTP readbacks, and direct database inspection, which in this project have
produced more evidence than a browser would. Asking him to look at the UI himself is ordinary
Cooperator-executed acceptance and is the right tool for UI work.

When you give him a manual batch: **label every step with a batch prefix** (`B1-1`, `B1-2`, …). Plain
`1.)` collides with your own numbered action list and has already caused a round of confusion. Ask for
`PASS` / `FAIL` / `PARTIAL` per item. Give him **one** batch, not a trickle — he is not a command
runner, and the previous era deliberately held its manual items back so he would walk through the
product once rather than five times.

## 9. Closure conditions

You may emit ORCHESTRATOR closure for this whole only when all of these hold:

1. the interface is localized to Slovak with English retained and switchable, and the Cooperator has
   accepted the rendered result;
2. the two architecture decisions in section 4 are recorded as Cooperator decisions with their
   rationale;
3. the three routed residuals in section 5 are each either corrected with evidence or re-recorded as
   accepted residuals with a complete Residual-Risk Decision record — including their existing
   Cooperator sign-off where one exists. **Losing a sign-off at closure is a closure failure.**
4. the security headers are re-proved on every document route and `/api/` route after the `proxy.ts`
   change, by the loopback readback technique;
5. the two auth-message security properties in section 6 hold in both languages;
6. the standing gates are green at the closing commit, including `npm run typecheck`;
7. the Cooperator-executed acceptance batch has been run and its results recorded;
8. no active mutation and no active Worker;
9. the Meta archive for this whole is complete, including a closure record.

## 10. What comes after you

```text
YOU    ui-internationalization + UX fine-tuning and final touch   10/00
then   VPS deployment behind nginx, Ubuntu Server 24.04           handout NOT YET WRITTEN — see below
later  admin-provider-model-console                               11/00
later  de-hardcoding the nine AI providers                        Cooperator-declared future whole
```

`10/01-player-model-choice-removal/` has a pre-existing handout from an earlier plan; revalidate it
against current truth before treating it as live.

### The deployment whole needs a handout that does not exist yet, and the Cooperator has asked for it twice

This is a **carried-forward obligation**, recorded here so it cannot be lost. The Cooperator asked for
it explicitly and reminded the previous Orchestrator to make sure it was not forgotten. It was not
written before that Orchestrator's session ended.

He needs **two artifacts**, and he asked for them to be as professional as possible:

1. **An expert Orchestrator handout for the deployment whole**, which must lead him step by step to a
   finished, hardened deployment. He describes himself as a complete novice at operations and named
   Prometheus and Grafana specifically as things he does not understand. He wants an Orchestrator that
   explains as it goes, not one that assumes.
2. **A prompt for a read-only Research Worker** — he has ChatGPT Deep Research available and wants to
   use it for current VPS-hardening practice on Ubuntu Server 24.04. That prompt must be detailed,
   demand versions and retrieval dates rather than unsourced "best practices", and be framed so the
   researcher can answer "this is disproportionate for a single demo VPS" where that is the honest
   answer — particularly about Prometheus and Grafana, which the previous Orchestrator assessed as a
   poor trade for one VPS before an interview.

The facts that handout must carry, all established during the security era:

```text
Target        Ubuntu Server 24.04, one VPS, behind nginx and ONLY behind nginx (Cooperator decision)
Topology      DECIDED by the previous Orchestrator at the Cooperator's request:
              Docker Compose for the application and Redis; nginx and certbot ON THE HOST.
              Reasons, in order: Node 26.4 is not in Ubuntu 24.04 repositories, so a host install
              means a third-party apt repo and version drift, while Docker pins a base image; image
              tags make rollback a 30-second operation, which matters before a fixed interview date;
              a committed compose file plus Dockerfile plus nginx config is the reviewable deployment
              description that `audit-02-F05` says is missing; and Redis comes correctly isolated on
              an internal network with no published port. nginx stays on the host because certbot
              renewal is far simpler there and nginx must survive container restarts.
              Rejected alternative, and say so honestly: systemd units plus a host nginx. systemd's
              hardening primitives (ProtectSystem=strict, NoNewPrivileges, SystemCallFilter,
              MemoryMax) are excellent and often better than default Docker isolation, and the Docker
              daemon itself runs as root and is attack surface. The Node availability problem is what
              decided it.
DJANGO_NUM_PROXIES must be 1 behind one nginx hop, NOT the shipped default of 0.
              nginx must set: proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              That expands to "$http_x_forwarded_for, $remote_addr", appending the real peer LAST.
              DRF with NUM_PROXIES=1 reads addrs[-min(1,len(addrs))] = addrs[-1] = the appended peer.
              That composition is NOT spoofable. Verified against installed DRF 3.17.0.
              TWO dangerous misconfigurations, both silent:
                NUM_PROXIES=1 with nginx NOT setting the header -> last element is attacker-chosen
                NUM_PROXIES greater than the real hop count     -> reads a leftward attacker element
audit-04-F01  MUST be corrected before public exposure. Behind nginx, django-axes still keys on
              REMOTE_ADDR (nginx's address) because ipware is absent, so the lockout key
              (username, ip_address) collapses to one global bucket per account and an account
              lockout becomes a targeted denial of service. Accepted as a routed residual with
              Cooperator sign-off, 2026-09-01, deferred to that whole.
              AND THE OBVIOUS REMEDY IS A TRAP. Installing django-axes[ipware] and stopping there
              changes nothing: AXES_IPWARE_META_PRECEDENCE_ORDER defaults to ("REMOTE_ADDR",), so XFF
              is never consulted. Adding XFF to that order WITHOUT setting AXES_IPWARE_PROXY_COUNT
              leaves AXES_IPWARE_PROXY_ORDER at "left-most", and the left-most element of
              $proxy_add_x_forwarded_for is what the CLIENT sent — handing axes an attacker-chosen
              identity and converting a DoS weakness into a full lockout-and-throttle bypass.
              Precedence order, proxy order (right-most), and proxy count must be set together and
              tested as one unit.
NEXT_PUBLIC_* are inlined at BUILD time, not read at runtime. NEXT_PUBLIC_API_URL must be correct
              when `docker build` runs, or the image points at localhost:8000 forever. Put a build
              check that FAILS the production build if the localhost default is still in place.
              This is the most common cause of "it worked locally".
Also unresolved for deployment: no CI, SBOM, signing, or provenance in-tree (audit-02-F05, accepted
              residual with Cooperator sign-off); Django HSTS lacks includeSubDomains and preload
              (orch-02-D11, may be resolved by whoever holds it); the documented start command
              `runserver 0.0.0.0:8000` in README.md:56, README.md:180, and AGENTS.md:32 binds every
              interface, which matters for any reachability claim; websockets through nginx need
              explicit upgrade headers; `sharp` needs matching platform binaries in the image.
Monitoring    The previous Orchestrator's assessment, to be tested by the research rather than
              inherited: for one VPS before an interview, Prometheus plus Grafana is a large surface
              for little benefit and another port to secure. What is actually needed is readable
              structured logs — the LOGGING configuration already landed in the security era —
              plus journalctl, plus possibly an external uptime check. Metrics as an interview story
              are legitimate but belong in their own whole after the deployment works.
```

## 11. Meta duties

You have write access to `/home/agile/meta`. **The Cooperator commits Meta himself; write files, do
not commit or push Meta.** Follow `/home/agile/meta/README.md` exactly: one directory per logical whole
for its entire lifecycle, filenames `<worker-session>_<phase>_<meta-exchange-index>.md` and
`<worker-session>_report_<meta-exchange-index>.md`, Meta exchange index = AP exchange ordinal − 1,
`<phase>` lowercase kebab-case and never `report`. Archive a prompt/report pair only after the report
exists. Contents are exact historical evidence — **never edit a report to read better.**

This directory is `10/00-ui-internationalization/`. **Your first Worker session in this whole is `01`.**
If you do the translation yourself with subagents rather than through a Worker, there is no Worker
exchange to archive for that part; record your own decisions and evidence in a phase file instead, and
say plainly in it that subagents were used and how their output was reviewed.

Keep `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` current as you go. They are the reason the downstream
handouts do not each carry a drifting copy of the same facts — and the previous era proved they rot
quietly if you only update the section you are thinking about.

## 12. The Cooperator

Read `PROJECT_CONTEXT.md` section 2 in full. The short version, because it changes how you write:

Address **Michal** in **Slovak**, masculine forms; refer to yourself in **feminine** forms. Worker
prompts and reports are professional **English**. Begin every message with the emoji signal that tells
him what to do, and **end every message with an explicit, emoji-annotated block of what he must do** —
never bury his action in prose.

He has granted full trust and asks for initiative. He is also emphatic that he is not the expert. Both
are true, and neither transfers authority: RF-01 still reserves material product, cost,
irreversibility, and residual-risk decisions to him. When he says "decide for me", decide — and then
show the reasoning so he can overrule it. When something is a genuine trade-off he has to live with,
put it in front of him even if he has said he trusts you. The previous era's most valuable moments came
from him mentioning something in passing: a `npm run dev` error message he pasted is now recorded as an
operational trap, and his one-line answer about nginx unlocked a `medium` finding nobody had considered.

His replies are terse — `A`, `Pokracuj`, `ano`, `hotovo`. One one-word reply was once misread and cost
an entire Worker session, so **confirm an ambiguous short instruction in one line** before spending a
session on it.
