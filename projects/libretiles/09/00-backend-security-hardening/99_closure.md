Artifact class: **closure record.** Historical evidence for logical whole `backend-security-hardening`
(Meta 09/00). It grants no authority. Task authority comes only from a current authoritative prompt;
protocol meaning from the pinned AP; project truth from the canonical repository.

Filename note: Meta's grammar reserves `NN_<phase>_<idx>.md` for Worker exchanges and `00_handout.md`
for a handout. `99_closure.md` is a deliberate, documented local deviation, requested by the Cooperator,
for the one artifact that is neither. Meta naming is storage policy, not AP meaning.

---

# Closure record — `backend-security-hardening`

## Closure record fields

```text
Declared closure signal: none — Libre Tiles declares no project-level closure-signal string, and one
  must not be invented. Closure is recorded by the field below and nowhere else.
Signal owner: orchestrator
Worker emission of closure signal: prohibited
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete — Libre Tiles declares no AP upgrade ledger, so there is
  nothing to reconcile and nothing was invented.
Active mutation: none
Active Worker: none
Closure actor: ORCHESTRATOR
Phase-qualified result: not-applicable (closure is not a phase result)
Logical-whole closure: closed-by-ORCHESTRATOR
Closing commit: 19cfec9ed27c57e9499b71c55be6c2fb709b0c63
```

## Verified state at the closing commit

Every line below was measured by the Orchestrator at `19cfec9`, not accepted from a Worker report.

```text
HEAD / origin/main   19cfec9ed27c57e9499b71c55be6c2fb709b0c63   equal, published
porcelain            empty
.ap gitlink          9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   unchanged all era
mypy                 Success: no issues found in 80 source files
ruff                 All checks passed!
manage.py check      System check identified no issues (0 silenced)
pytest               328 passed, 4 skipped
npm run typecheck    exit 0        (new gate, added at b5774b2)
npx vitest run       326 passed | 3 skipped
npm run lint         exit 0
npm run build        succeeds; Proxy registered; no middleware deprecation warning
npm audit            3 advisories, all dev-flagged and dispositioned
```

Test progression across the era: 302 → 315 → 322 → 326 → 328 backend passes; the frontend suite grew
to 326 passes. No test was weakened, skipped, xfailed, or deleted at any point.

## Commits

```text
ae574b7  fail closed on insecure Django security defaults
fdfe4a6  require authentication before judge provider calls
7e583aa  throttle auth and AI-context endpoints; enforce password policy
04fe823  revoke tokens on logout and password change
437e20f  make game websocket tickets single-use
445029d  emit security response headers and a strict CSP
bbba2e9  brake brute-force logins and share the throttle cache        (S7a, session 08)
8e82f3b  surface provider, websocket, and API failures                 (S7b, session 09/01)
9ff9ac5  redact provider credentials by value in failure logs          (S7b correction, 09/02)
7a197da  raise django and daphne floors; declare redis directly        (S8a, session 11)
b5774b2  bump next to 16.3.4 and migrate to the proxy convention       (S8b, session 12/02)
19cfec9  key unauthenticated throttles on the socket address           (S9, session 14)
```

## Finding inventory

**32 findings `verified-closed`** — thirty by the comprehensive independent re-audit `audit-03` at
`b5774b2`, two by the bounded independent re-audit `audit-04` at `19cfec9`.

```text
audit-01-F01  unauthenticated /api/ai/judge provider spend
audit-01-F02  fail closed on DJANGO_SECRET_KEY
audit-01-F03  auth stuffing / registration spam / refresh volume bounded per client
audit-01-F04  DEBUG / ALLOWED_HOSTS / CORS / TLS flags
audit-01-F09  websocket ticket replay (replay half)
audit-01-F10  token revocation on logout and password change
audit-01-F11  registration password policy
audit-01-F12  unthrottled AI-route cost channel
orch-01-F17   fail-open DRF default permission class
orch-01-F18   security response headers and enforced CSP
orch-01-F20   Django admin brute-force brake
acc-01-D01    channel-layer diagnosability
acc-01-D02    provider failures unlogged
acc-01-D03    registration validation errors swallowed
acc-01-D04    raw API error strings
acc-01-D05    login throttle window
acc-01-D06    fresh clone cannot boot
acc-01-D07    documentation drift
orch-02-D08   AGENTS.md provider list
orch-02-D09   logout call never made
orch-02-D10   admin-path refresh-token blacklisting
orch-02-D12   middleware in settings.py; dead cache branch
orch-02-D13   every 401 read as invalid credentials
orch-02-F21   log redaction defeated by the project's own fixture
orch-03-G01   sharp in the production optional tree
orch-03-G02   undispositioned Django advisory
orch-04-F22   npm run build could report success with type errors
audit-02-F01  next 16.2.0 advisory cluster
audit-02-F02  Django below patched 5.2.17
audit-02-F03  daphne below patched 4.2.2
audit-02-F04  redis undeclared for RedisCache
audit-03-F01  unauthenticated throttle identity attacker-chosen
```

**13 rejected as false positives with disproving evidence**, and re-confirmed by the comprehensive
re-audit: `audit-01-F05`, `F07`, `F08`, `F14`, `F15`, `F16`; `audit-02-F07` through `F12`. Rejecting
nine of twelve dependency signals with reachability evidence was the most valuable output of the
dependency audit. Scanner severity is not derived severity.

## Residual-risk decisions

All complete. `medium` and above carry explicit Cooperator sign-off, per INFOSEC 14.

```text
Finding ID: orch-01-F18 (script-src 'unsafe-inline' in production)
Decision: accepted-residual   Severity: medium   Approver: Cooperator
Rationale: a nonce CSP needs dynamic rendering on /, /play, /settings — the exact pages the UX whole
  rewrites. connect-src still blocks exfiltration of the localStorage tokens.
Regression test: security-headers.test.ts asserts the production policy explicitly
Routed to: ui-internationalization, as the nonce upgrade

Finding ID: audit-02-F05 (no CI, SBOM, signing, or provenance in-tree)
Decision: accepted-residual   Severity: medium   Approver: Cooperator, 2026-09-01
Rationale: no .github directory exists at all. Adding CI is a separate deliberate decision about what
  it should gate and is not fixable inside this whole without expanding its objective.
Regression test: not applicable — absence of a process control, not a code defect

Finding ID: audit-04-F01 / orch-05-D14 (axes lockout degenerates behind a reverse proxy)
Decision: accepted-residual, ROUTED   Severity: medium in the nginx topology; not applicable today
Approver: Cooperator, 2026-09-01, explicitly, with sign-off for the deployed case deferred to the
  deployment whole where it becomes reachable
Rationale: not reachable at this commit — no nginx configuration exists in this repository and the
  product is not publicly deployed. It becomes reachable the moment Django sits behind nginx, which
  the Cooperator has decided it will.
Regression test: required in the deployment whole — a simulated proxied request must yield the real
  peer as the axes client IP, and two real peers must not share a lockout bucket
Routed to: the deployment whole, with the full mechanism and the remedy trap recorded in
  DEFECT_LEDGER.md and PROJECT_CONTEXT.md

Finding ID: audit-01-F13 (duplicate-username registration disclosure)
Decision: accepted-residual   Severity: low   Approver: Cooperator
Rationale: usability for a self-service game; login itself does not differentiate unknown user from
  wrong password. Re-audit confirmed the description still matches and has not widened.

Finding ID: audit-01-F09 (ticket travels in the query string)
Decision: accepted-residual   Severity: low   Approver: Cooperator
Rationale: single-use plus a 10-second TTL minimises the capture window; moving it would change the
  handshake and the frontend client. TTL is tighter than the 60 seconds of the original finding.

Finding ID: audit-01-F06 (public prompt text; swallow-to-HTTP-200 in the catalog proxies)
Decision: accepted-residual   Severity: low   Approver: Orchestrator
Rationale: the catalog endpoints are deliberately public with tests proving exactly what they expose.
Routed to: the UX whole, which touches the catalog surface anyway

Finding ID: orch-01-F18 (style-src 'unsafe-inline')
Decision: accepted-residual   Severity: low   Approver: Orchestrator
Rationale: Framer Motion sets inline style attributes. Inline styles are a far weaker vector than
  inline scripts.

Finding ID: orch-02-D11 (Django HSTS without includeSubDomains or preload)
Decision: accepted-residual, ROUTED   Severity: low   Approver: Orchestrator
Rationale: includeSubDomains interacts with the planned subdomain-locale feature, and preload is
  close to irreversible once submitted. Both are product decisions, not defaults to flip. Note the
  precision the re-audit established: there are TWO HSTS emitters, and this finding is about Django's
  only. The Next.js proxy already emits includeSubDomains.
Routed to: ui-internationalization

Finding ID: audit-02-F06 (no frontend dev-dependency boundary test)
Decision: accepted-residual   Severity: info   Approver: Orchestrator
Rationale: no dev dependency is currently imported by application code; npm ls --omit=dev is clean.

Finding ID: audit-03 diagnostic residuals (provider_transport omits the raw message;
  generate_text over-redacts model identifiers)
Decision: accepted-residual   Severity: low   Approver: Orchestrator
Rationale: phase, status, and error class survive, so acc-01-D02's diagnostic purpose is reduced and
  not destroyed, while orch-02-F21's secret property holds. Redaction erring toward over-redaction is
  the correct direction for a secret control.

Finding ID: LogoutView has no throttle scope
Decision: accepted-residual   Severity: low   Approver: Orchestrator
Rationale: authenticated, so it keys on user.pk; the abuse potential is negligible.

Finding ID: the two NUM_PROXIES regression tests have named coverage gaps
Decision: accepted-residual   Severity: low   Approver: Orchestrator
Rationale: they do not assert api_settings.NUM_PROXIES == 0, do not cover a comma-separated
  nginx-append XFF, and do not vary XFF on refresh. They DO lock the original finding for register and
  login. The identity probe plus the observed cache key close the gap in practice at this commit.
Routed to: the deployment whole, where the proxied XFF shape becomes real
```

## Audits performed

```text
audit-01  original independent application audit          (pre-era, session 01)
audit-02  dependency and supply-chain audit, P-4          (session 10, first ever in this project)
audit-03  comprehensive fresh independent re-audit, P-10  (session 13)
audit-04  bounded fresh independent re-audit, P-10        (session 15)
```

The auditor never corrected, the correctors never self-certified, and no re-auditor audited its own
work. `audit-02` had never been performed in this project and was a genuine deploy-readiness gate:
it found three high findings that every application-level audit had missed, because they were in the
dependency tree rather than in the code.

## What was gained beyond closed findings

- **The CSP has runtime evidence for the first time.** Slice 07 built an enforced policy and had to
  state honestly that it could not validate it, because Browser MCP is a locked fork. A production
  `next start` bound to loopback, probed with an HTTP client, is not a browser — and it established
  the headers on every document route and every Next `/api/` route.
- **`npm run typecheck` exists**, because `npm run build` was found to report success while type
  errors sat in the tree. "The build passed" and "the code type-checks" are now two separate claims.
- **A fresh clone boots.** `scripts/libretiles.sh` generates a strong key into a newly created `.env`
  and never touches an existing one.
- **Provider failures are legible.** An expired credential is no longer indistinguishable from a
  silent model, and the log cannot carry a credential the process holds.
- **The dependency surface is known**, with the deployed set enumerated and the dev-only set excluded
  from finding status.

## Lessons this era produced

Each cost something real. They are recorded in `PROJECT_CONTEXT.md` for reuse; the era-specific ones:

1. **A negative grep is not a conclusion.** The Orchestrator recorded that `selection.py` knew only
   two providers because a constant-only pattern found two. All nine were there as string literals.
2. **A test written by the author of a rule tests what the author thought of.** The mandatory
   redaction test passed while the redaction leaked, because the implementer picked a sentinel its own
   regex caught. The fix was to use the sentinel the project already declared sensitive.
3. **A green gate can be a cached gate.** `npm run build` reported success with two type errors for
   two commits.
4. **The obvious remedy can be worse than the defect.** Installing `django-axes[ipware]` and stopping
   there changes nothing; adding XFF to the precedence order without the proxy count hands axes an
   attacker-chosen identity. A half-measure on a security control is not half a fix.
5. **Too high is as dangerous as too low.** A `NUM_PROXIES` above the real hop count reads a
   client-supplied element, exactly like `None` did.
6. **Name your own weak spots in the audit prompt.** The Orchestrator listed nine thin spots for the
   re-auditor. The most valuable finding of the whole era came out of the one it could not resolve
   itself, and the second-most out of the one the re-auditor disproved.
7. **A blocked report is a good report.** Session 12 stopped rather than touch two files outside its
   allowlist, and the blocker was the Orchestrator's allowlist, not the Worker's work.

Five times a Worker contradicted the Orchestrator with evidence. Five times the Worker was right.
That is the protocol working, and it only works if the corrections are recorded rather than smoothed.

## Deployment posture at closure

⛔ **Not deployed, and not yet safe to deploy publicly** — but for a reason that is now specific rather
than precautionary. `audit-04-F01` becomes reachable the moment Django sits behind nginx, which is the
Cooperator's stated plan. The deployment whole must correct it before public exposure.

Also unresolved for deployment, all recorded: no CI or provenance (`audit-02-F05`, accepted);
`DJANGO_NUM_PROXIES` must be `1` behind one nginx hop with `$proxy_add_x_forwarded_for`; the documented
`runserver 0.0.0.0:8000` binds every interface; Django HSTS lacks `includeSubDomains`.

## What the next Orchestrator inherits

Read `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` first; both are current at `19cfec9`. The execution
order the Cooperator has now chosen:

```text
next   ui-internationalization + UX fine-tuning and final touch   10/00
then   VPS deployment behind nginx on Ubuntu Server 24.04         separate whole, handout to follow
later  admin-provider-model-console                               11/00
later  de-hardcoding the nine AI providers                        Cooperator-declared future whole
```

`product-acceptance-sweep` as a standalone whole is superseded: its remaining items are UI
observations and fold into the UX whole, together with the three S7b behaviours that could not be
automated (registration error rendering, logout tolerating a failed request, websocket close toasts).

Standing Cooperator decisions that constrain every successor: the nine AI providers are frozen; Stripe,
LM Studio, and Vercel AI Gateway are rejected; Browser MCP is not a diagnostic driver; the Slovak
lexicon quality is parked. All are in `PROJECT_CONTEXT.md` section 5.
