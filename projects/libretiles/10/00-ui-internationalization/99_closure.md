# Closure record — logical whole `ui-internationalization` (Meta 10/00)

**Logical-whole closure: closed-by-ORCHESTRATOR.**

Closing commit: `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`
AP pin at closure: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Public `refs/heads/main` at closure: `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`
Working tree at closure: `git status --porcelain=v1` EMPTY
Closed on 2026-09-03 by the era-10 continuation Orchestrator.

Artifact class: **closure record — authority for the fact of closure only.** It grants no authority to change
anything. Successor wholes take their authority from their own Orchestrator prompts.

---

## 1. What this whole delivered

Libre Tiles ships its interface in **four languages** — English, Slovak, Czech, Polish — from a typed
catalog of **300 keys per locale, 1200 strings**, with three Slavic plural functions and a server-authoritative
locale. The player no longer chooses an AI model or a prompt preset. The product has accessible names, dialog
semantics, a single working live region, and keyboard-operable rack tiles where it previously had nothing. The
last `script-src 'unsafe-inline'` is gone, replaced by a per-request nonce proved on every route.

Eighteen commits from `61c9f09`, in order:

```text
5a96b5e  S3a  server locale authoritative + four interface locales            15 files
e421c66  S3b  board, rack, action buttons and chat in four locales            11 files
e0d3b64  S3c  the game screen, plus uii-01-F08 and uii-01-F09                  8 files
383011b  S4   R6: the player no longer chooses model or prompt         15 files, -460 net
d40b230  S5   the two lobby screens + F10 F11 F12 F14                         11 files
6ca85de  S6   the game header cluster and the AI overlay                       8 files
4bf4365  S7   the settings screen and the overlay stats bar             8 files, 38 keys
d806e31  S8   saved-boards history + half of uii-01-F03                  8 files, 35 keys
8f44022  S9   the profile modal; uii-01-F03 CLOSED                       7 files, 16 keys
c3f75e3  R1   premium searchable pickers with flags                     12 files, +615
e8cc7bb  S11  R12: accessible names, dialog semantics, status regions   16 files, 9 keys
74b5339  R14  one persistent announcer; rack tiles get a role            7 files, 0 keys
f40d8a0  R15  ORCHESTRATOR-AUTHORED: rack keyboard + dead labels         4 files, 0 keys
8f096e1  R7   Django resolves the client locale; F17 end reasons        10 files, 5 keys
8ef5992  R8   ORCHESTRATOR-AUTHORED: Retry-After header over prose       4 files, 0 keys
f983c3d  R9   ORCHESTRATOR-AUTHORED: HSTS includeSubDomains              2 files, 0 keys
cb4efed  R10  per-request nonce CSP; orch-01-F18 corrected               4 files, 0 keys
47ed8bf  R11  unreachable catalog stops reading as an empty one         11 files, 1 key
```

---

## 2. Closure conditions — every one, with its evidence

The conditions are quoted from `93_orchestrator-handout.md` section 11.

| # | Condition | Status | Evidence |
|---|---|---|---|
| 1 | interface localized to Slovak with English retained and switchable, plus the decision-8 locales, and he has accepted the rendered result | **MET** | `en+sk+cs+pl` per decision 8. Accepted across batches B17, B18, B19, B20, B22, B24 and the closing `B25. PASS` |
| 2 | both Settings dropdowns with flags, diacritic-insensitive autocomplete and the arrow, accepted | **MET** | R1 at `c3f75e3`; `B24` 8/8 itemized PASS; re-confirmed under the nonce CSP in `B25` item 5 |
| 3 | the player no longer chooses a model or a prompt preset | **MET** | S4 at `383011b`; Cooperator-verified `B20-5`. Two components deleted, persist 4→5, zero backend change, `selectedModelId` deliberately preserved as fallback attempt 1 |
| 4 | the three routed residuals corrected with evidence or re-recorded with a complete Residual-Risk Decision record including their existing sign-off | **MET** | section 3 below — all three CORRECTED, and every pre-existing sign-off preserved |
| 5 | security headers re-proved on every document route and every `/api/` route after the nonce CSP, by loopback readback, against the audit-03 baseline | **MET** | section 4 below — eleven routes, 114 script tags, eleven distinct nonces |
| 6 | `AC-SEC-1` and `AC-SEC-2` hold in ALL shipped locales | **MET** | `api.test.ts:178` and `:213` iterate en/sk/cs/pl; `11 passed` at `47ed8bf` |
| 7 | all eight standing gates green at the closing commit | **MET** | section 5 below |
| 8 | his acceptance batch run and its results recorded | **MET** | `B25. PASS`, blanket, 2026-09-03, eight items |
| 9 | no active mutation, no active Worker | **MET** | porcelain empty, public readback equal, no Worker session open |
| 10 | Meta archive complete including a closure record | **MET** | 17 Worker sessions archived as `01`–`17`, six `9N_` Orchestrator artifacts, this file |

---

## 3. Condition 4 — the three routed residuals, and every preserved sign-off

All three were **corrected with evidence**, so the accepted-residual branch of condition 4 does not apply to
them. The routing recorded against each is discharged.

```text
orch-01-F18  script-src 'unsafe-inline' in production
             CORRECTED at cb4efed by R10. Per-request nonce + 'strict-dynamic', 'self' retained as the CSP2
             fallback. Proved on eleven routes at 47ed8bf. The PROJECT_CONTEXT section 7 row is struck
             through and marked corrected rather than deleted, so the routing history survives.
orch-02-D11  HSTS without includeSubDomains or preload
             CORRECTED at f983c3d by R9. security.W005 closed; security.W021 (no preload) KEPT and PINNED
             BY TEST as an accepted residual per Cooperator decision 5.
audit-01-F06 catalog proxies swallow every failure into an empty HTTP 200
             CORRECTED at 47ed8bf by R11, in both halves — the two proxy routes now report the upstream
             status or 502 without leaking Django's body, and the user-visible collapse in the page call
             sites now distinguishes "empty" from "unreachable".
```

⛔ **Sign-offs preserved, none lost.** Condition 4 says losing one at closure is a closure failure.

```text
audit-01-F13  duplicate-username registration error stays explicit    accepted, era-09 sign-off, UNCHANGED
audit-01-F09  websocket ticket in the query string                    accepted, era-09 sign-off, UNCHANGED
audit-02-F05  no CI, SBOM, signing or provenance                      accepted, Cooperator 2026-09-01
style-src 'unsafe-inline'                                             accepted, era-09 sign-off, CARRIED
              FORWARD UNCHANGED — 33 `style=` props plus imperative style.setProperty writes are style
              ATTRIBUTES, and a nonce covers <style> ELEMENTS only. R10 could not have fixed it and
              deliberately did not touch security-headers.ts:98.
uii-01-F05    first-visit detection cannot be flash-free on the client  accepted
uii-01-F18    five PremiumPicker behaviours                            accepted, Cooperator `nevadi`, B24-2
```

### Residuals this whole created or inherited and now signs off

```text
uii-01-F13  callerless /api/prompts and api.getPrompts        DECIDED keep-and-record, low.
            Four documents describe /api/models — README.md:291, frontend/README.md:45,
            docs/architecture.md:38, CONTRIBUTING.md:91 — and README.md is under the standing Cooperator
            freeze. Whole 11/00 will need a server-side catalog proxy. Deleting would have required editing
            a frozen file to keep the documentation true.
uii-01-F15  slug fallback in the variant picker                accepted, low
uii-01-F16  static properties on a page component              accepted, low. A consequence of the Next.js
            App Router export restriction recorded in PROJECT_CONTEXT section 10.
uii-01-F19  no focus trap and no focus restoration in the four dialogs   accepted, low, DELIBERATE.
            A subtly wrong trap strands a keyboard user with no way out; aria-modal plus Escape plus initial
            focus delivers most of the value at a fraction of the risk. `activeElement` is 0 by design.
uii-01-F25  Czech MinimumLengthValidator untranslated          accepted, INFO — UNREACHABLE. Both password
            fields carry min_length=8, so DRF rejects a short password with its OWN translated message
            before validate_password ever runs. Upstream django-5.2.17 cs catalog carries the stale
            %(min_length)d msgid. Reachable only if someone removes min_length.
uii-01-F26  Slovak DRF min_length translation is semantically wrong   accepted, low. "má viac ako 8 znakov"
            says MORE THAN 8 where the rule is AT LEAST 8. Upstream djangorestframework-3.17.0 sk catalog.
            Visible to every Slovak player who types a short password. Fixing it needs a project-level
            backend/locale/sk override plus compilemessages.
uii-01-F27  settings rival PANEL still says "seed the catalog" on an outage   accepted, low, NEW at 47ed8bf.
            The notice above it is now correct; the panel needs one piece of persisted reachability state
            that R11's grant forbade. Two messages disagreeing beats one message lying, but it is not done.
_global-error does not hydrate under the nonce CSP           accepted, low. It is prerendered, so no nonce
            can be injected. It still renders styled error text and a NATIVE <form> + <button type="submit">
            Reload, so recovery does not depend on JavaScript. The ordinary-page policy was deliberately NOT
            weakened to accommodate it.
{humanState} in AIThinkingOverlay stays English              accepted, deferred to an enum-keyed telemetry
            slice. Guarded by AC-NO-TELEMETRY-KEY so it cannot be localized by accident.
```

---

## 4. Condition 5 — the full loopback re-proof at `47ed8bf`

Production build, `next start` bound to `127.0.0.1:3211`, PID-exact stop, port released.

```text
path              code  CSP  nonce  no-unsafe-inline  style-src ok  5 headers  HSTS  scripts nonced
/                 200    Y     Y           Y                Y           Y        Y      15/15
/play             200    Y     Y           Y                Y           Y        Y      17/17
/settings         200    Y     Y           Y                Y           Y        Y      16/16
/draw/abc123      200    Y     Y           Y                Y           Y        Y      18/18
/game/abc123      200    Y     Y           Y                Y           Y        Y      20/20
/waiting/abc123   200    Y     Y           Y                Y           Y        Y      16/16
/nope-404         404    Y     Y           Y                Y           Y        Y      12/12
/api/models       200    Y     Y           Y                Y           Y        Y       n/a
/api/prompts      200    Y     Y           Y                Y           Y        Y       n/a
/api/ai/move      405    Y     Y           Y                Y           Y        Y       n/a
/api/ai/judge     405    Y     Y           Y                Y           Y        Y       n/a
```

**114 script tags across seven document routes, every one carrying its own response's nonce. Eleven distinct
nonces across eleven requests.**

audit-03 byte comparison, nonce canonicalized: 11 directives base, 11 observed, identical order and values,
**exactly one authorized difference** —

```text
base      script-src 'self' 'unsafe-inline'
observed  script-src 'self' 'nonce-PLACEHOLDER' 'strict-dynamic'
```

All six constant security headers byte-identical to the baseline. `Vary: Accept-Language` and
`Content-Language` correctly ABSENT — they are Django response headers from R7's `LocaleMiddleware` and
cannot appear on a Next.js response.

---

## 5. Condition 7 — the eight gates at the closing commit

```text
mypy config game gamecore accounts catalog   Success: no issues found in 83 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       390 passed, 4 skipped in 220.32s
npm run typecheck                            exit 0
npx vitest run                                450 passed | 3 skipped  (31 files passed | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

Standing invariants at closure: `aria-live` 1, `role="status"` 1, `role="dialog"` 4, `aria-modal` 4,
`role="group"` 1, `htmlFor` 0, `tabIndex` 5, `activeElement` 0. Catalog parity 300 keys in each of four
locales, 20 of them parameterized.

Backend growth across the whole: pytest `381 → 390`. Frontend: vitest `374 → 450`.

---

## 6. What this whole is honest about NOT having proven

⛔ **Rendered assistive-technology behaviour is unaudited, permanently, by Cooperator decision 10** — he has
no screen reader and will not install one. `uii-01-F20`, `F21`, `F22` are closed **by inspection only**:
attributes present in markup, asserted by string tests, plus his keyboard observation. No later session may
summarize this whole as "accessibility verified". What he DID observe is keyboard: initial dialog focus,
Escape dismissal, Tab reaching a rack tile and Enter selecting it.

Browser CSP enforcement, hydration and Fast Refresh are covered by `B25` items 1–3 and by nothing else. The
node-environment vitest suite renders no page and enforces no policy.

Three commits — `f40d8a0` (R15), `8ef5992` (R8), `f983c3d` (R9) — are **ORCHESTRATOR-AUTHORED and their
evidence is NON-INDEPENDENT.** Only the mechanical gates corroborate their judgement calls; there is no
second agent's reading. Every other commit is Worker work that the Orchestrator re-measured.

---

## 7. Routed onward — not this whole's work

```text
11/00 admin-provider-model-console  the whole admin surface. Cooperator decision 9 froze acceptance batch
                                    B21 with every item NOT TESTED and moved admin work out of this whole.
                                    Measured evidence is deposited in
                                    11/00-.../90_admin_surface_evidence_from_era10.md, written blind to that
                                    directory's own handout. It will need the /api/models proxy uii-01-F13
                                    deliberately kept alive.
uii-01-F27                          one piece of persisted reachability state for the settings rival panel
uii-01-F25, uii-01-F26              two upstream catalog defects needing a project-level backend/locale
                                    override plus compilemessages
{humanState} telemetry              an enum-keyed slice, guarded by AC-NO-TELEMETRY-KEY
slovak-playable-variant             Settings/engine/prompt wiring for live Slovak play
Tier 2 dictionary                   optional API
deployment whole                    ⛔ ITS CHECKLIST MUST CARRY: SECURE_HSTS_INCLUDE_SUBDOMAINS forces HTTPS
                                    on EVERY subdomain for a year and is slow to undo. Confirm every
                                    subdomain is HTTPS before the first production response.
dependency bump                     ⛔ two tripwire tests assert that an UPSTREAM gap still exists —
                                    test_czech_minimum_length_validator_catalog_mismatch and
                                    test_drf_throttle_wait_suffix_stays_english. A Django or DRF upgrade that
                                    fixes upstream will break them, and that is good news wearing the costume
                                    of a regression.
```

---

## 8. What this whole cost, and what it taught

Seventeen Worker sessions, eighteen commits, twenty-seven `uii-01-F*` findings, nine acceptance batches.

**Nine of those findings were caused by Orchestrator prompts**, not Worker error: four accessibility
instructions that specified an ARIA attribute without modelling the interaction it implies (`F20`, `F21`,
`F23`, `F24`), one prompt whose negative authority forbade a test its own section 10 required, and five
protocol-conformance defects across four planner prompts — three of which were introduced by the repair of an
earlier one.

**A Worker caught every single one before it reached code.** Twice a Worker overruled an Orchestrator claim on
evidence and was right. Three times a Worker refused to work at all rather than proceed under an invalid
grant, and each refusal cited exact protocol lines. That is the protocol functioning exactly as designed, and
the report field that asks "what can you still see that this prompt did not anticipate" is what made it
visible — eight findings arrived through that field.

The durable lessons are in `PROJECT_CONTEXT.md` section 9, numbers 13 through 19. Two are worth restating
here because they cost the most:

```text
A number you did not count yourself is not a measurement, whatever produced it — including a subagent.
Do not build a prompt by string-patching the previous prompt. Regenerate and run apfieldcheck.py.
```

`apfieldcheck.py` — in this directory's parent as `apfieldcheck.py` — mechanically diffs a prompt's AP field
values and coordinate consistency against the pinned `.ap`. It was extended twice, each time after a defect
it could not see, each time validated against the failing artifact first. It caught two defects in the very
next prompt written after it.

---

## 9. Successor obligations

This closure does not discharge:

- the VPS deployment handout, still owed (`PROJECT_CONTEXT.md` section 11.2)
- the read-only Research Worker prompt, still owed (section 11.3)
- `libretiles-openrouter-catalog-refresh` scheduling, which is separate production authority

`DEFECT_LEDGER.md` stays live as the project's running inventory. `PROJECT_CONTEXT.md` stays the standing
brief. Both were updated through `47ed8bf` before this record was written.

**Logical-whole closure: closed-by-ORCHESTRATOR.**
