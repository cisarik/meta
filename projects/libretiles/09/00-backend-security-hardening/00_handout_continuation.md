# Continuation handout — finish `backend-security-hardening`

Artifact class: **Orchestrator handout.** Second handout into this logical whole; `00_handout.md` in
this same directory is the original restoration that opened it. Meta's filename grammar reserves
`00_handout.md` for one handout per whole, so this continuation uses an explicit descriptive name.
That is a deliberate, documented local deviation; Meta naming is storage policy, not AP meaning.

This handout grants **no** repository, implementation, deployment, production, account, filesystem,
external-service, Git, browser, or credential mutation authority. Verify everything yourself.

---

## Handoff capsule

```text
Closure candidate: logical whole `backend-security-hardening` (Meta 09/00).
Report justification: rotation — the outgoing Orchestrator's session ended by Cooperator decision
                      while implementation and audit work remained.
Verified state: main = 445029d35474cba9f363734c19cf969226fbe5ed, published, porcelain empty,
                .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.
                Gates green at that commit: mypy 79 files clean, ruff clean,
                pytest 302 passed / 4 skipped, frontend lint clean, build succeeds.
Active mutation: none. No Worker is active. Nothing is unpushed.
Residual risks / open decisions: five accepted residuals with recorded Cooperator sign-off, and
                seven open defects — see DEFECT_LEDGER.md. Three of the twelve original audit
                findings are corrected but NOT yet verified-closed.
Next owner and bounded next action: YOU. Verify state, then issue slice S7 (section 3).
Repeated blocker: none open. One earlier blocker recurred twice inside slice S5 and was resolved
                with a pre-authorized fallback branch; that technique is recorded in
                PROJECT_CONTEXT.md lesson 7.
Audit / handoff budget: one comprehensive fresh independent re-audit and one dependency audit
                remain justified. No further handoff is justified before closure.
This handoff grants no new mutation authority.
```

## 0. Required reading, in this order

1. `/home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md` — **read this first and in full.** It holds the project identity, the Cooperator profile and communication rules, the emoji signals, the standing gates, the execution-route deviation, the locked forks, the formed-word invariant, the central product fact, the complete security state with accepted residuals, the instruments, the lessons, and the environment traps. It exists so that this handout does not repeat them and so the copies cannot drift.
2. `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — the seven open defects and the complete list of what manual acceptance already verified. **Do not re-test what is recorded as verified.**
3. `/home/agile/Projects/libretiles/AGENTS.md` and `/home/agile/Projects/libretiles/frontend/AGENTS.md`
4. `.ap/AP.md` — at minimum RF-01, RF-02, RF-03, RF-08, RF-12, RF-16, RF-18, RF-19, the Continuation Bootstrap, and the Defensive-Security Task Anchor
5. `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`
6. `.ap/PROMPT_CONTRACTS.md` — the Accepted-Finding Correction, Fresh Independent Re-Audit, Security Audit Prompt, Security Finding Record, and Residual-Risk Decision contracts
7. `.ap/INFOSEC.md` in full — you will close an activated security whole, so you need sections 4.7, 4.10, 4.11, 14, 15, and 17
8. `.ap/PROMPT_ENGINEERING_PATTERNS.md` — sections 3, 4, 5, P01, P02, P03, P04, P11. Section 5 is a list of anti-patterns; check your own prompts against it before issuing them.
9. `09/00-backend-security-hardening/01_report_00.md` — the original independent audit, which is the authority on what was found and why
10. The rest of this directory in session order: `00_handout.md`, then `01`…`07` prompt/report pairs

## 1. Stage 1 — verify before you plan

```text
cd /home/agile/Projects/libretiles
git rev-parse HEAD                      -> expect 445029d35474cba9f363734c19cf969226fbe5ed
git rev-parse HEAD:.ap                  -> expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               -> expect the same
git status -sb                          -> expect ## main...origin/main
git status --porcelain=v1               -> expect empty
git ls-remote origin refs/heads/main    -> expect 445029d35474cba9f363734c19cf969226fbe5ed
git log --oneline -12
```

Then independently confirm the standing gates from PROJECT_CONTEXT.md section 4. If a gate that this
handout calls green comes back red, that is your first finding: stop, present the contradiction, and
issue nothing.

If `main` has advanced beyond `445029d`, another Orchestrator has been active. Establish who and what
before issuing any mutating prompt. Exactly one Orchestrator is active at a time.

## 2. Finding status — what is corrected, what is not

Twelve findings came out of the independent audit (`01_report_00.md`) plus two established by the
outgoing Orchestrator. Current disposition:

| Finding | Substance | Status |
|---|---|---|
| audit-01-F02 | fail closed on `DJANGO_SECRET_KEY` | corrected, **not** verified-closed |
| audit-01-F04 | DEBUG / ALLOWED_HOSTS / CORS / TLS flags | corrected, **not** verified-closed |
| orch-01-F17 | fail-open DRF default permission class | corrected, **not** verified-closed |
| audit-01-F01 | unauthenticated `/api/ai/judge` provider spend | corrected, **not** verified-closed |
| audit-01-F03 | no auth throttling | corrected, **not** verified-closed |
| audit-01-F11 | registration password policy | corrected, **not** verified-closed |
| audit-01-F12 | unthrottled AI-route cost channel | corrected, **not** verified-closed |
| audit-01-F10 | token revocation on logout and password change | corrected, **not** verified-closed |
| audit-01-F09 | websocket ticket replay | replay part corrected; transport part accepted-residual with Cooperator sign-off |
| orch-01-F18 | security response headers and CSP | corrected; `script-src 'unsafe-inline'` in production accepted-residual `medium` with Cooperator sign-off, nonce upgrade routed to the UX/i18n whole |
| **orch-01-F20** | **Django admin login has no brute-force brake; DRF throttles do not cover it** | **OPEN — slice S7** |
| audit-01-F13 | duplicate-username registration error | accepted-residual, Cooperator sign-off |
| audit-01-F05, F07, F08, F14, F15, F16 | six hypotheses | rejected-false-positive with disproving evidence; do not re-litigate |
| audit-01-F06 | public prompt text and swallow-to-HTTP-200 in the catalog proxies | accepted-residual `low`; the swallow-to-200 is a candidate for the UX whole, which touches the catalog surface anyway |

`corrected` means an implementation slice landed with pre-fix/post-fix regression evidence.
`verified-closed` requires the fresh independent re-audit in section 4. **Do not tell the Cooperator
the whole is secure before that re-audit returns per-finding verdicts.**

## 3. Slice S7 — the remaining correction

One coherent slice, or two if it grows past a reviewable diff. It is the last implementation work in
this whole. Scope, with owners already established in the ledger:

1. **orch-01-F20 — Django admin login brake.** The Cooperator has explicitly **approved adding `django-axes`** as a pinned dependency, chosen over a reverse-proxy rate limit because it also gives an audit trail of failed admin logins, which he will want once the admin console exists. This is the only dependency addition authorized in this whole. Pin it exactly, review the lockfile diff, and keep the AST guard in `backend/tests/test_game_app_has_no_dev_imports.py` green.
2. **acc-01-D05 — throttle-rate tuning.** Raise the IP-keyed `auth_login` rate so a realistic demo cannot lock the presenter out for most of an hour, and let `django-axes` provide the per-account lockout. Require the Worker to state the arithmetic for a realistic session. **The throttle scope strings are load-bearing for existing tests — do not rename them.**
3. **Shared throttle cache when `DEBUG` is false.** `LocMemCache` is per-process, so the brake on a multi-worker deployment is `workers × rate`. Django 5.1 ships `django.core.cache.backends.redis.RedisCache`, so this needs **no new dependency**. But `AGENTS.md` promises Redis is not required for AI-only local boot — so keep LocMem in DEBUG and **require** a shared cache when DEBUG is false, failing closed in the same style as the `SECRET_KEY` guard. Do not make Redis a requirement for local play.
4. **acc-01-D03 — surface registration validation errors.** The highest-value UX item in the slice and a direct consequence of this whole's own password policy. See the ledger for the exact mechanism and file lines.
5. **acc-01-D04 — human error messages.** Map known statuses at one place in the API client. The change-password path already does this well and is the model to follow.
6. **acc-01-D01 — channel-layer failure diagnosability.** Wrap `group_add` / `accept`, close with a distinct code, log the cause, and decide deliberately whether the ticket is consumed before or after the connection is established.
7. **acc-01-D02 — log provider exceptions**, bounded and redacted: class, HTTP status when present, truncated message. Never the key, never the request body. This is the gap that made an expired credential indistinguishable from a silent model.
8. **acc-01-D06 — onboarding.** Have `scripts/libretiles.sh` generate a strong key into a freshly created `backend/.env`, and correct the onboarding paragraphs in `README.md` and `AGENTS.md`.
9. **acc-01-D07 — documentation drift.** The judge attempt count, and a note that pre-existing `.env` files override new code defaults and must be reviewed after a settings change.
10. **Wire the frontend logout call.** `POST /api/auth/logout/` exists and blacklists the presented refresh token, but no client calls it — `handleLogout` in `frontend/src/app/game/[id]/page.tsx` only clears local state. Until something calls it, refresh-token theft is mitigated only by a password change.
11. **Admin-path refresh-token blacklisting.** A password change made through Django admin sets `password_changed_at` via `User.set_password`, but only `ChangePasswordSerializer.save()` also blacklists that user's outstanding refresh tokens. `low`, and it belongs here rather than anywhere else.

Judgement to exercise: items 1–3 are backend configuration and dependency work; items 4, 5, and 10
are frontend; items 6, 7, 9 are docs and logging. If one allowlist covering all of that produces a
diff you cannot review honestly, split it. Prefer two clean slices over one unreviewable one — see
`PROMPT_ENGINEERING_PATTERNS.md` P05.

## 4. The two audits, then closure

**🔍 P-4 dependency and supply-chain audit** (INFOSEC 4.7, structural profile P-4). Never performed
in this project, explicitly excluded from the original audit, and a genuine deploy-readiness gate. It
becomes more relevant because S7 adds `django-axes`. Scope: manifest and lockfile consistency for
both `backend/pyproject.toml` + `poetry.lock` and `frontend/package.json` + `package-lock.json`;
known-vulnerability signals **with reachability analysis**, because a CVE is a signal and not a
finding; typosquatting and dependency-confusion signals; abandonment signals; build provenance. Tool
output is evidence requiring interpretation. Fresh independent session, read-only.

**🔍 Comprehensive fresh independent re-audit** (INFOSEC 4.11, structural profile P-10). Mandatory,
because the corrections touched authentication, authorization, and secret handling. Requirements:

- the re-auditor must not have implemented any of it, and must not correct what it audits;
- targets are every correction slice **plus the original risk claim** behind each finding;
- verdict per finding is exactly `verified-closed` or `not accepted`, with evidence;
- it must re-verify the accepted residuals are still accurately described, not silently widened;
- it should be given the ledger and told that manual acceptance already confirmed the live behaviour of token revocation, single-use tickets, CSP, and multiplayer, so it can spend its effort on what is not yet established.

**Closure conditions.** You may emit ORCHESTRATOR closure for this whole only when all of these hold:

1. every finding is `verified-closed`, or `accepted-residual` with a complete Residual-Risk Decision record;
2. every residual of severity `medium` or higher carries the Cooperator's explicit sign-off — four such records already exist, do not lose them;
3. P-4 has run and its findings are dispositioned;
4. the standing gates are green at the closing commit;
5. no active mutation and no active Worker;
6. the Meta archive for this whole is complete.

Then, and only then, tell the Cooperator the whole is closed — which is also the gate that releases
the next Orchestrator in the sequence.

## 5. Deployment posture

⛔ **Do not deploy to a public address, and do not let anyone else, until this whole is closed.** At
the time of writing: `orch-01-F20` is open, the throttle cache is per-process, the dependency audit
has never run, and no finding is `verified-closed`. Local play is fine and has been extensively
exercised. The Cooperator knows this and agrees.

## 6. What comes after you

Execution order, with Meta archive numbers matching it. Exactly one Orchestrator active at a time.

| | Whole | Meta |
|---|---|---|
| **YOU** | finish `backend-security-hardening` | `09/00-backend-security-hardening/` |
| next | `product-acceptance-sweep` — the human-only observations still uncovered | `10/00-product-acceptance-sweep/` |
| then | `player-model-choice-removal` | `10/01-player-model-choice-removal/` |
| then | `ui-internationalization`, including the subdomain-locale feature and the nonce-CSP upgrade | `10/02-ui-internationalization/` |
| then | `admin-provider-model-console` | `11/00-admin-provider-model-console/` |

Each of those has its own handout already written, in its own directory. You do not need to write
them. Your final act is to write and archive a short closure record for this whole and to tell the
Cooperator which handout to open next.

## 7. Meta duties

You have write access to `/home/agile/meta`. The Cooperator commits Meta himself; write files, do not
commit or push Meta. Follow `/home/agile/meta/README.md` exactly: one directory per logical whole for
its entire lifecycle, filenames `<worker-session>_<phase>_<meta-exchange-index>.md` and
`<worker-session>_report_<meta-exchange-index>.md`, Meta exchange index = AP exchange ordinal − 1,
`<phase>` lowercase kebab-case and never `report`. Archive a prompt/report pair only after the report
exists. Contents are exact historical evidence — never edit a report to read better.

Sessions `01` through `07` are already archived in this directory. **Your first Worker session in
this whole is `08`.**

Keep `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` current as you go. They are the reason the three
downstream handouts do not each carry a drifting copy of the same facts.
