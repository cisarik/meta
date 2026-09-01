### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 03  
Worker exchange ordinal: 01

**status:** PASS

**Phase-qualified result:** Implementation PASS (non-independent). This session implemented the correction and ran same-session gates; it does not certify the correction and does not close the logical whole. Fresh independent re-audit remains mandatory (INFOSEC.md 4.11).

**Start commit:** `ae574b7978afa78386ef31d8648b6c768e703849`  
**End commit:** `fdfe4a67e8598c3580fb1219a224b22615d99f7a`

**Changed paths** (purpose):
- `frontend/src/lib/api-auth.ts` — shared server-side helper: parse `Authorization: Bearer`, verify via Django `GET /api/auth/me/`, branch on `res.status` before any body parse.
- `frontend/src/lib/api-auth.test.ts` — direct unit coverage of header parsing and status-first fail-closed behaviour, including a success-shaped JSON body on HTTP 429/401.
- `frontend/src/app/api/ai/judge/route.ts` — require a valid Django-verified JWT before catalog fetch and before any provider call; cap word count/length after auth; generic bounded error bodies.
- `frontend/src/app/api/ai/judge/route.test.ts` — regression tests 1–8 (fail-before / pass-after) plus existing happy-path/exhaustion/no-fabricate-invalid coverage updated to authenticated fixtures.
- `frontend/src/app/api/ai/move/route.test.ts` — lock-only test 9: Django `ai-context` HTTP 429 ⇒ `generateText` not called. **No change to** `frontend/src/app/api/ai/move/route.ts`.

`git diff --stat ae574b7978afa78386ef31d8648b6c768e703849`:

```text
 frontend/src/app/api/ai/judge/route.test.ts | 284 ++++++++++++++++++++++------
 frontend/src/app/api/ai/judge/route.ts      |  50 +++++
 frontend/src/app/api/ai/move/route.test.ts  |  14 ++
 frontend/src/lib/api-auth.test.ts           | 130 +++++++++++++
 frontend/src/lib/api-auth.ts                |  85 +++++++++
 5 files changed, 507 insertions(+), 56 deletions(-)
```

`git diff --name-only ae574b7978afa78386ef31d8648b6c768e703849`:

```text
frontend/src/app/api/ai/judge/route.test.ts
frontend/src/app/api/ai/judge/route.ts
frontend/src/app/api/ai/move/route.test.ts
frontend/src/lib/api-auth.test.ts
frontend/src/lib/api-auth.ts
```

Nothing outside the allowlist. `backend/**` is untouched (`git diff --name-only ae574b7978afa78386ef31d8648b6c768e703849 -- backend/` was empty).

**Repository gate** (before any edit):
- `git rev-parse HEAD` → `ae574b7978afa78386ef31d8648b6c768e703849`
- `git rev-parse HEAD:.ap` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git -C .ap rev-parse HEAD` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git status -sb` → `## main...origin/main` (no divergence)
- `git status --porcelain=v1` → empty
- `git ls-remote origin refs/heads/main` → `ae574b7978afa78386ef31d8648b6c768e703849`

**Pre-push remote gate:** `git ls-remote origin refs/heads/main` still `ae574b7978afa78386ef31d8648b6c768e703849` immediately before `git push origin main`.

**Capability handshake:**
- Requested: WORKER, Bounded Correction Worker, recommended High reasoning; communication identity Cursor Grok 4.6.
- Directly observed: local git on `main`; frontend `npx`/`npm` (vitest, eslint, `next build`); `LIBRETILES_AI_PLAY_LIVE` unset; no Python, no backend gates, no live provider, no `.env` contents read.
- Inferred: none that expand authority.
- Unknown: serving-model identity is not independently attested.
- Independently attested: none.

---

**audit-01-F01** (implemented in this slice; not self-certified):

`POST /api/ai/judge` now:
1. Rejects missing/malformed `Authorization` with HTTP 401 (no Django call, no catalog, no provider).
2. Calls Django `GET /api/auth/me/` with the Bearer token and **branches on `res.status` first**.
3. Maps 401/403 → HTTP 401, 429 → HTTP 429 (forwards bounded `Retry-After` when Django supplies it), anything else including unreachable/non-JSON/unexpected body → HTTP 503.
4. Only on HTTP 200 with a JSON object body does it parse the judge body, apply input caps, fetch the catalog, and call `generateText`.

**Input caps** (module constants in `route.ts`; not exported — Next.js 16 typed routes reject extra route exports):
- `MAX_JUDGE_WORDS = 12`
- `MAX_JUDGE_WORD_LENGTH = 15`

Reasoning: a 15×15 placement forms at most eight words, each at most 15 letters. 12 words is modest headroom for a real turn and hostile to prompt stuffing. 15 is the board-length ceiling.

Error bodies are generic (`Authentication required`, `Too many requests`, `Too many words`, `Word too long`, `AI judge failed`) and do not echo the token, `Authorization`, provider keys, Django `detail`, or stack traces.

| Test | Pre-fix (unmodified route) | Post-fix |
|---|---|---|
| 1. No `Authorization` | HTTP **503**; `generateText` called (exhaustion path) | HTTP **401**; `generateText` 0; no `/api/auth/me/`; no catalog |
| 2. Malformed `Authorization` (`Token not-a-bearer`) | HTTP **503** | HTTP **401**; `generateText` 0; no Django call |
| 3. Django `/api/auth/me/` HTTP 401 | HTTP **503**; catalog path used; `generateText` called | HTTP **401**; `generateText` 0; catalog not fetched |
| 4. Django HTTP 429 + `Retry-After: 12` | HTTP **503** | HTTP **429**; `Retry-After: 12`; `generateText` 0; catalog not fetched |
| 5. Django fetch rejects | `generateText` **called** (catalog still reachable; exhaustion 503) | HTTP **503**; `generateText` 0 |
| 5b. Django 200 with unexpected array body | `generateText` **called** | HTTP **503**; `generateText` 0; catalog not fetched |
| 6. 13-word array | HTTP **503** (`generateText` called) | HTTP **400**; `generateText` 0; `getLanguageRuntime` 0; catalog not fetched |
| 7. Word length 16 | HTTP **503** | HTTP **400**; `generateText` 0; `getLanguageRuntime` 0; catalog not fetched |
| 8. Valid token + valid input | `/api/auth/me/` **not called** (`meIndex === -1`); existing happy path otherwise | HTTP **200**; Django verification **precedes** catalog and `generateText`; existing exhaustion still **503** with no `results`; malformed model output still does not fabricate `invalid` |

---

**audit-01-F12** (partial; remains OPEN):

| Test | Pre-fix | Post-fix |
|---|---|---|
| 9. Move route: Django `ai-context` HTTP 429 (`{detail: "Request was throttled."}`) | **PASS** — `generateText` not called, `getLanguageRuntime` not called, SSE error emitted | **PASS** (lock only; move route source unchanged) |

**audit-01-F12 remains OPEN after this slice and closes in S3 (Django DRF throttles).** This slice only makes the pre-provider Django call non-bypassable on the judge path (unconditional `/api/auth/me/` before catalog/provider) and locks the existing move-route `ai-context` 429 ⇒ no `generateText` behaviour. No in-memory Next.js limiter was added.

Residual (not a finding, not corrected here): the move route still uses `parseBackendJson`, which ignores HTTP status. Test 9 passes because a typical DRF 429 body has no `compact_state`. A 429 body that included `compact_state` would not be locked by that test. Enforcing 429 at Django, then treating status as authoritative, is S3.

---

**Verification helper branches on `res.status`:** confirmed. `verifyUserBearerToken` reads `res.status` before `res.json()`. HTTP 401/403/429 never inspect the body for success shape. Unit test: a user-profile-shaped JSON body with status 429 returns `{ ok: false, status: 429 }`, not success. This is the opposite of `parseBackendJson` in the move route.

**Judge 503-on-exhaustion and never-fabricate-invalid:** still hold. Evidence after the fix:
- `returns 503 after exhausting attempts without inventing results` — HTTP 503, `payload.results` undefined, `generateText` ×3
- `caps malformed-output retries at three models` — HTTP 503, `generateText` ×3
- `returns three-lane 503 accounting without synthesizing invalid verdicts`
- `advances past malformed output and never synthesizes invalid verdicts` — third model’s strict payload, no fabricated invalids
- `returns 503 without fabricating invalids for a slovak lexicon request`
- New happy-path test asserts the 200 payload is the model’s actual `valid: true` results, not a synthesized invalid

`MAX_FALLBACK_ATTEMPTS` in `ai-fallback.ts` was not changed.

---

**Standing gates** (from `frontend/`; `LIBRETILES_AI_PLAY_LIVE` unset):

Exact prompt command:

```text
npx vitest run src/app/api/ai/judge/route.test.ts src/app/api/ai/move/route.test.ts src/lib/ai-fallback.test.ts src/lib/ai-move-stream.test.ts
→ Test Files  4 passed (4)
→ Tests  125 passed (125)
```

Per-file in that set: `judge/route.test.ts` 21, `move/route.test.ts` 52, `ai-fallback.test.ts` + `ai-move-stream.test.ts` the remaining 52.

Allowlisted extra: `src/lib/api-auth.test.ts` — 6 passed (5 files / 131 when included).

`npm run lint` → no errors (eslint exit 0, empty diagnostics).

`npm run build` → succeeds (`Next.js 16.2.0`, TypeScript finished, `/api/ai/judge` and `/api/ai/move` present as dynamic routes).

Backend baseline (not re-run): mypy 76 files clean, ruff clean, pytest 260 passed / 4 skipped at the start commit.

---

**Authorized Git result:**
- One commit: `fdfe4a67e8598c3580fb1219a224b22615d99f7a` — `fix(ai): require authentication before judge provider calls`
- Staged by explicit path only (no `git add -A` / `git add .`)
- Pre-push remote `main` still `ae574b7978afa78386ef31d8648b6c768e703849`
- `git push origin main` (no flags) → `ae574b7..fdfe4a6  main -> main`
- Readback: `git ls-remote origin refs/heads/main` = `fdfe4a67e8598c3580fb1219a224b22615d99f7a` = `git rev-parse HEAD`
- Working tree: `## main...origin/main`, clean

---

**Deviations, risks, missing evidence:**
- Caps are **module** constants, not exported from `route.ts`. Next.js 16 typed routes reject extra route exports (`"MAX_JUDGE_WORDS" is not a valid Route export field`). Tests duplicate `12` / `15` with a comment to keep them aligned.
- `Retry-After` is copied from the Django **header** when present and ≤64 characters; a missing header is not invented.
- No live Django, no live provider, no serverless multi-instance observation. In-memory limiter was correctly not built; real 429 enforcement is S3.
- Move-route 429 lock depends on a 429 body without `compact_state` (see F12 residual above).
- `npm run build` loads the Next.js env files internally; this Worker did not read `frontend/.env.local` or `backend/.env`.

**Out-of-scope observations (not findings):**
- `README.md` still says the judge makes “up to five attempts” while `AGENTS.md` and the code use three. Documentation drift, unchanged as instructed.
- `/api/ai/judge` still has no in-repo client caller; requiring `Authorization` therefore does not break an existing frontend contract.

**One smallest next step:** Orchestrator routes S3 — Django DRF throttling plus register password policy — which closes audit-01-F12, audit-01-F03, and audit-01-F11. Separately, a fresh independent re-audit of this correction is mandatory before treating F01 as verified-closed.

**Report justification:** new-evidence

**Logical-whole closure:** not-closed

**Authority expiry:** this exchange’s authority expires with this terminal report. Retained context is not a renewal. Autonomous work stops here.

**Resolved Execution Issues / Near-Misses:** first `npm run build` failed because `export const MAX_JUDGE_WORDS` is not a valid Next.js Route export. Cause: Next.js 16 typed `route.ts` surface. Resolution: drop the export, keep module-level constants, duplicate the numbers in the test file. Residual: two copies of `12`/`15` can drift if only one is edited.

**Pre-Existing Failure Classification:** none