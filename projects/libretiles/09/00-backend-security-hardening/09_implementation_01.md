Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator, not the Cooperator, and not an auditor. You have implementation authority for an exact allowlist and nothing else. You have NO audit authority and you never certify your own correction. Do not enable any native planning mode.

Logical whole identity: backend-security-hardening
Worker session ordinal: 09
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: hold-the-log-redaction-and-name-an-expired-session
Task type: bounded correction of two concrete findings against your own previous candidate
Security task class: accepted-finding correction (INFOSEC.md 4.10)
INFOSEC route: R3 — this correction touches secret handling, so INFOSEC.md section 15 makes a fresh independent re-audit mandatory. It is already scheduled and you do not perform it.

Continuity anchor: your terminal implementation-PASS report for Worker session 09, exchange 01, task `make-failures-legible`, ending at commit `8e82f3bda67751a74746ef15a634514609e3886f`.
Authority renewal: the authority from exchange 01 EXPIRED with that report. This prompt grants complete new bounded authority for exactly the two findings in section 1 and nothing else. Retained context from exchange 01 is convenience, not authority.
Why this session: you wrote the redaction rule and the error mapping, so you hold the most accurate model of both. Independence is not required here — this is a correction, not an acceptance. Your evidence remains NON-INDEPENDENT.
Re-gate before you touch anything: repository state, environment, and the gates below must be re-established from scratch. If any current repository evidence conflicts with what you remember from exchange 01, STOP and report the conflict rather than trusting memory.

Implementation authority: explicit
Audit authority: none
Accepted finding IDs: orch-02-F21 and orch-02-D13 only
Exact baseline: 8e82f3bda67751a74746ef15a634514609e3886f
Changed-path allowlist: exactly the paths listed in section 4 and no others
Exact path allowlist: see section 4
Implementation boundaries: positive authority is section 2; negative authority is section 4's exclusion list and section 6 in full
Regression test: the numbered set in section 5; each must fail before your change and pass after
Commits: one corrective commit, explicitly authorized in section 7
Independence required: no
Evidence tier: E2
Evidence tier basis: reversible and narrow, but it changes a secret-handling control, which is why the general tier does not lower the activated INFOSEC requirements.
Combined implementation envelope: allowed — inspection, implementation, tests, one commit, one non-force push, one public readback, one terminal report.
Independent acceptance: required-separate-fresh-worker.
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: full-fresh — because this correction changes a security boundary, scoped re-acceptance is not valid. The scheduled comprehensive fresh independent re-audit is that full fresh acceptance.
Rollback or recovery checkpoint: the start commit above. `git revert` of your single commit fully restores it.
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none
Worker topology: single-active
Accountable Worker: one WORKER
Sub-agents/internal delegation: not-used
External trace disposition: not-used; do not write to /home/agile/meta/** or any archive location
Provider call authority: none. No live provider call. LIBRETILES_AI_PLAY_LIVE stays unset.
Secret authority: you may READ the NAMES of provider credential environment variables from source, and you may compare a log message against `process.env` values AT RUNTIME inside the redaction function. You must never print, echo, log, hash, measure the length of, or report any such value, and you must never read `frontend/.env.local` or `backend/.env` yourself.
Network authority: none beyond the authorized `git ls-remote origin refs/heads/main` gate and one `git push`.
Side-effect authority: reversible local mutation of the allowlisted paths; one remote non-force fast-forward push to main. No dependency change, no migration.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: src/lib/provider-logging.test.ts, src/lib/ibm-watsonx.test.ts, src/lib/api.test.ts, src/lib/openai-compatible.test.ts, src/app/api/ai/judge/route.test.ts, src/app/api/ai/move/route.test.ts
Affected tests: the same set
New causal regression: a provider-failure log record that provably cannot carry the account values this project's own fixture already declares sensitive, and an expired session that is not reported as a wrong password
Broad or full suite: required-because AGENTS.md makes `npm run lint`, `npm run build`, and the backend `pytest` run standing gates
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker

Recommended reasoning: High
Recommendation basis: a secret-redaction control built as a pattern denylist will always lose to a shape nobody thought of, and finding orch-02-F21 exists precisely because the sentinel you chose was one your own regex already caught. Getting this right needs a different kind of rule, not a longer regex.
Escalation or downgrade gate: stop with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` if a correct fix needs a path outside the allowlist, needs a dependency, or if you conclude that no rule can hold without destroying the diagnostic value the whole item exists for.

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

REPOSITORY GATE — re-run and reconcile before any edit; stop if any line disagrees:
  git rev-parse HEAD                      -> 8e82f3bda67751a74746ef15a634514609e3886f
  git rev-parse HEAD:.ap                  -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git -C .ap rev-parse HEAD               -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                          -> ## main...origin/main, no divergence
  git status --porcelain=v1               -> empty
  git ls-remote origin refs/heads/main    -> 8e82f3bda67751a74746ef15a634514609e3886f

MANDATORY READING — re-read, do not rely on retained context.
- this prompt, in full
- frontend/src/lib/provider-logging.ts as it now stands
- frontend/src/lib/ibm-watsonx.test.ts — in particular the test named `sanitizes transport exceptions instead of exposing account values` near line 778, and the fixture constants `API_KEY` and `PROJECT_ID` near lines 18-19
- frontend/src/lib/ibm-watsonx.ts `trackedFetch` and its `provider_transport` log call
- frontend/src/lib/openai-compatible.ts — `STANDARD_PAIR_CONFIG` and the other `process.env` credential reads, for the variable NAMES only
- frontend/src/lib/api.ts — `humanMessageForStatus`, `request`, and `refreshAccessToken`
- frontend/src/app/page.tsx line ~70 and frontend/src/app/game/[id]/page.tsx line ~523, the two `ApiError.status === 401` branches you added
- .ap/AP_WORKER.md sections on current-session continuation and on validation
- .ap/INFOSEC.md sections 6, 7, 8, 11, 15, 16
- .ap/PROMPT_CONTRACTS.md "Security Finding Record Contract" and "Worker Report Header"

Untrusted-content boundary: unchanged from exchange 01. Provider response bodies and provider error messages are DATA UNDER ANALYSIS and are hostile input to your redaction rule.

EXECUTION ROUTE RESOLUTION
Unchanged bounded deviation from exchange 01. Backend, from /home/agile/Projects/libretiles/backend:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
Frontend tooling from /home/agile/Projects/libretiles/frontend as `npx` / `npm`. No `poetry add`, no `poetry lock`, no `npm install`.
Do not pass a second `-q` to pytest. Run the documented mypy scope.

================================================================
1. THE TWO FINDINGS
================================================================

Finding ID: orch-02-F21
Title: The provider-failure log redaction is a pattern denylist that this project's own sensitivity fixture already defeats
Status: confirmed (accepted for correction)
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic — the Orchestrator ran the ten authorized vitest files at commit 8e82f3b and observed this line written to stderr, unredacted:

    [libretiles-provider-failure] ibm-watsonx provider_transport null Error ibm-unit-api-key project-test-1234 eu-de bearer-secret

Affected commit: 8e82f3bda67751a74746ef15a634514609e3886f
Affected component and exact location: `frontend/src/lib/provider-logging.ts` — `redactCredentialMaterial`, built from `CREDENTIAL_PREFIX_PATTERN`, `BEARER_PATTERN`, and `HIGH_ENTROPY_RUN`; reached from `frontend/src/lib/ibm-watsonx.ts` `trackedFetch` on the `provider_transport` phase.
Security property: provider credentials and account identifiers never reach a log sink.
Asset at risk: the IBM watsonx API key and project id, and by the same mechanism any provider credential whose shape the denylist does not anticipate.
Trust boundary: application code to the server log sink — a new egress path that exchange 01 introduced.
Attacker-controlled input: the provider error message. A provider is untrusted and can put anything in it, including material you sent it. The watsonx IAM token request carries the API key in its request BODY, so an error that echoes the request can carry the key.
Reachability: established. Every watsonx transport failure reaches `recordProviderFailure`, and `process.stderr.write` emits the message.
Preconditions: none beyond a transport failure.
Required privileges: none for the failure to occur; reading a server log for the consequence.
Observed or potential impact: credential and account material in operator-visible logs and in any aggregator they ship to.
C/I/A effect: confidentiality of provider credentials.
CWE mapping: CWE-532 (Insertion of Sensitive Information into Log File), MITRE CWE corpus per the version-qualified registry in .ap/INFOSEC.md section 19.
Why the three patterns missed it: `bearer-secret` is hyphen-joined so `/Bearer\s+\S+/` never matches; `ibm-unit-api-key` is 16 characters and `project-test-1234` is 17, both below the `{24,}` floor of `HIGH_ENTROPY_RUN`; neither carries a listed prefix.
Exploitability conclusion: **not demonstrated** for a real credential. The values that leaked are synthetic fixtures, and a realistic 44-character IBM key or 36-character project UUID would in fact be caught by the entropy rule. The finding is that the CONTROL cannot be relied on, not that a real secret is known to have leaked. Do not overstate it and do not understate it.
Why it is still medium: `frontend/src/lib/ibm-watsonx.test.ts` contains a test literally named `sanitizes transport exceptions instead of exposing account values`. This project already decided those values are sensitive. That test asserts only the THROWN error and passes, while a second egress path that it does not check emits them. A control that the project's own sensitivity test defeats is not a control, and the blast radius of a credential in an aggregated log is high.
Smallest safe correction direction: stop relying on guessing the shape of a secret. Redact by VALUE against the credentials the process actually holds, keep the pattern denylist as defence in depth only, and reconsider whether the raw provider message belongs in the highest-risk phase at all.
Regression-test requirement: the existing watsonx sanitisation test must also assert the LOG record, using its own existing fixture constants as the sentinels.
Acceptance-blocking decision: blocking — a secret-handling control must hold before this whole closes.
Redaction requirements: your report must not reproduce any real credential value, prefix, or length. The four synthetic fixture strings above are already in the repository's test file and may be named.

Finding ID: orch-02-D13
Title: Every HTTP 401 renders "Invalid username or password", including an expired session on an authenticated request
Status: confirmed (accepted for correction)
Severity: low
Confidence: high
Evidence class: established-static
Affected commit: 8e82f3bda67751a74746ef15a634514609e3886f
Affected component and exact location: `frontend/src/lib/api.ts` — `humanMessageForStatus`, `case 401`, returns that string unconditionally.
Observed: `request()` retries once through `refreshAccessToken()` when `opts.token` is present. When the refresh fails, `clearAuth()` runs and the original 401 propagates to the caller. Roughly fourteen call sites render `err.message` directly, so a mid-game expiry on loading game history, submitting a move, exchanging, passing, giving up, starting a new game, joining the queue, or changing a password now tells the user their username or password is wrong.
Impact: the worst case is the profile modal: a user types the correct current password, the access token has expired, and the product tells them their credentials are wrong. That is actively misleading, and misleading error text is exactly what finding acc-01-D04 existed to remove. Before exchange 01 the text was ugly (`API error 401: {...}`) but not untrue.
Reachability: established. The pre-existing acceptance sweep already recorded a real observation of an expired session being surfaced, so this path is exercised in ordinary use.
Exploitability conclusion: not applicable — this is a correctness and UX defect, not a vulnerability.
Smallest safe correction direction: distinguish a 401 on an authenticated request from a 401 on an unauthenticated one at the single place the mapping lives.
Regression-test requirement: a 401 on a request carrying a token renders session-expired wording; a 401 on a request carrying no token renders invalid-credentials wording.
Acceptance-blocking decision: non-blocking, but it is cheap and it is in the same file you are already opening.

================================================================
2. WHAT TO IMPLEMENT
================================================================

--- ITEM A: make the redaction hold (orch-02-F21) ---

1. **Redact by value, not only by shape.** Inside the redaction step, compare the message against the credential values the server process actually holds, read from `process.env` at call time, and replace any occurrence. The variable names are discoverable from `frontend/src/lib/openai-compatible.ts` `STANDARD_PAIR_CONFIG`, from `openrouter.ts`, `nvidia-nim.ts`, and from `ibm-watsonx.ts`. This is strictly stronger than any pattern guess: if the process sent the value, the process can recognise it coming back, whatever its shape.

   Guard rails, all mandatory:
   - never log, print, hash, measure, report, or return any of those values;
   - skip any value that is absent, empty, whitespace, a placeholder (`openai-compatible.ts` already has `isPlaceholder`), or shorter than a stated minimum. Pick the minimum and justify it: redacting a 3-character value would blank out ordinary words and destroy the diagnostic value the whole item exists for;
   - the comparison must not be vulnerable to the value containing regular-expression metacharacters. Use a literal replace, or escape properly, and say which;
   - state explicitly whether you read the environment once per call or cache it, and what that means if a credential is rotated while the server runs.

2. **Keep the pattern denylist as defence in depth**, and close the two holes the finding names: `Bearer` followed by a non-space separator, and credential-shaped runs below the 24-character floor. Lower or supplement the floor deliberately.

3. **Reconsider the highest-risk phase.** For `provider_transport` on watsonx — a failure of `fetch` itself, where the diagnostic value of the free-form message is lowest and the risk is highest because the IAM request body carries the key — decide whether the raw message belongs in the record at all, or whether the error class and status alone are enough. Either choice is acceptable; make it deliberately and justify it in one or two sentences. Do not silently leave it as it is.

4. **Prove you did not over-redact.** The benign records the suite already emits must stay readable and diagnostic. These exact lines were observed at the start commit and their message text must survive your change:

       [libretiles-provider-failure] openrouter generate_text null Error generic SDK failure
       [libretiles-provider-failure] openrouter generate_text null Error rate limited
       [libretiles-provider-failure] ibm-watsonx provider_http 503 Error HTTP 503

   A redaction rule that blanks out `rate limited` or `HTTP 503` has destroyed the reason acc-01-D02 was filed. Report the before and after of at least these three.

--- ITEM B: name an expired session correctly (orch-02-D13) ---

In `frontend/src/lib/api.ts`, distinguish the two kinds of 401 at the single place the mapping lives.

Preferred shape, and the reason: branch on whether the request carried a bearer token. A 401 on a request that carried a token means the session is no longer valid; a 401 on a request that carried none means the submitted credentials were rejected. Deciding it at the source is more robust than relying on each call site to override, and there are roughly fourteen call sites.

  - authenticated 401: wording that says the session expired and that the user should sign in again.
  - unauthenticated 401: keep the existing invalid-credentials wording. Do not differentiate an unknown user from a wrong password — that non-disclosure is deliberate.
  - do not weaken the transparent single-retry refresh in `request()`, and do not change `refreshAccessToken()`.
  - check both `ApiError.status === 401` branches you added in exchange 01 — `frontend/src/app/page.tsx` and `frontend/src/app/game/[id]/page.tsx` — and confirm each still behaves correctly. The login page override may now be redundant; leave it if it is harmless and say so, or remove it if it is dead.
  - the rendered message must still contain neither `API error` nor a JSON brace.

================================================================
3. WHAT NOT TO REDESIGN
================================================================

Everything else from exchange 01 stands and was verified by the Orchestrator at 8e82f3b. Do not revisit it:
the 4401 / 4403 / 4503 close codes and the consumer logging; the `LOGGING` dict; `config/middleware.py` and the axes middleware ordering; the deleted dead cache branch; the `process.stderr.write` sink and the `Date.now` near-miss that justified it; the record shape `{provider, phase, status, errorClass, message}`; the 200-character bound; the four call sites plus watsonx; the `ApiError` class shape and every status mapping other than 401; the 429 wording; the registration fall-through removal; the logout wiring; the client-import guard.

The Orchestrator independently re-measured all of these at 8e82f3b: mypy `Success: no issues found in 80 source files`, ruff clean, `manage.py check` clean, pytest `322 passed, 4 skipped`, the ten vitest files `193 passed`, lint exit 0, build succeeding. Those are your baselines.

Do not touch, reopen, or re-litigate: audit-01-F13, audit-01-F09 (transport accepted, replay corrected — the single-use ticket must not regress), orch-01-F18, audit-01-F06, audit-01-F05/F07/F08/F14/F15/F16, orch-01-F20 and every axes value, any throttle rate, orch-02-D11 (HSTS, routed to a later whole), and orch-02-D12 (already corrected at 8e82f3b).

**A NEW STANDING COOPERATOR DECISION, effective now:** the nine AI providers are to be de-hardcoded in their own future logical whole. Until then, **no change to provider lists, provider constants, provider tiers, or provider documentation is authorized anywhere** — not in `provider-registry.ts`, not in `openai-compatible.ts`, not in `backend/catalog/selection.py`, not in `README.md`, not in `AGENTS.md`. You may READ `openai-compatible.ts` for credential variable names, and you must not edit it.

================================================================
4. EXACT PATH ALLOWLIST — nothing outside this list may change
================================================================

  frontend/src/lib/provider-logging.ts          (Item A)
  frontend/src/lib/provider-logging.test.ts     (Item A tests)
  frontend/src/lib/ibm-watsonx.ts               (Item A step 3, ONLY if your decision requires it)
  frontend/src/lib/ibm-watsonx.test.ts          (Item A test 3 — strengthen the existing sanitisation test)
  frontend/src/lib/api.ts                       (Item B)
  frontend/src/lib/api.test.ts                  (Item B tests)
  frontend/src/app/page.tsx                     (ONLY if the 401 branch is now dead and you remove it)
  frontend/src/app/game/[id]/page.tsx           (ONLY if the 401 branch needs adjusting; it probably does not)

Do not touch anything else. In particular: no backend file, no `openai-compatible.ts`, no `provider-registry.ts`, no `openrouter.ts`, no `nvidia-nim.ts`, no route file, no `package.json`, no lockfile, no README, no AGENTS.md, no `.ap/**`.

Choose the SMALLEST set that does the job. Prove the boundary with `git diff --stat` and `git diff --name-only`.

================================================================
5. REGRESSION TESTS — each must fail before your change and pass after
================================================================

Record the exact pre-fix result for each. Test 3 is the one that matters most and it WILL fail before your change — the Orchestrator already observed the leak, so a "passes before" result there means your test is not asserting the right thing.

  1. In `provider-logging.test.ts`: a message containing a value taken from a stubbed provider credential environment variable is redacted. Stub the environment inside the test; never touch a real `.env`.
  2. In `provider-logging.test.ts`: `bearer-secret`, `Bearer:token`, and `bearer_token` style separators are redacted, and a credential-shaped run below the previous 24-character floor is redacted.
  3. In `ibm-watsonx.test.ts`, STRENGTHEN the existing test `sanitizes transport exceptions instead of exposing account values`: it must now assert that the emitted LOG RECORD, as well as the thrown error, contains none of its own `API_KEY`, `PROJECT_ID`, `"eu-de"`, or `"bearer-secret"` fixture values. Keep every assertion that test already makes. Capture the sink rather than scraping terminal output.
  4. In `provider-logging.test.ts`: the three benign messages named in section 2 item A step 4 survive redaction with their diagnostic text intact.
  5. In `provider-logging.test.ts`: an absent, empty, whitespace, placeholder, or below-minimum-length credential variable causes NO redaction, so a stray short value cannot blank an ordinary message.
  6. In `api.test.ts`: a 401 on a request carrying a token renders session-expired wording, and does NOT contain `Invalid username or password`.
  7. In `api.test.ts`: a 401 on a request carrying no token still renders the invalid-credentials wording.
  8. In `api.test.ts`: both messages contain neither `API error` nor a JSON brace, and `ApiError.status` is still numerically 401 in both cases.

Do not weaken, skip, mark xfail, or delete any existing test. Every one of the 193 vitest tests and 322 backend tests must still pass.

================================================================
6. NEGATIVE AUTHORITY
================================================================

- Change only the allowlisted paths. Preserve unrelated work.
- No dependency change, no lockfile edit, no migration, no backend change.
- No provider list, provider constant, provider tier, or provider documentation change anywhere — standing Cooperator decision, section 3.
- Never print, log, echo, hash, measure, or report a real credential value, prefix, or length. Do not read `frontend/.env.local` or `backend/.env`.
- Do not weaken the transparent refresh retry in `request()`.
- Do not change any SSE field, `terminal_cause`, `completion_source`, `ai_metadata` field, or the judge status contract.
- Do not change the record shape, the sink, or the 200-character bound.
- Do not weaken, delete, skip, or xfail any existing test.
- Do not differentiate an unknown user from a wrong password.
- No live provider call. `LIBRETILES_AI_PLAY_LIVE` stays unset.
- No `git add -A`, no `git add .`, no force push, no amend, no rebase, no reset, no clean, no stash, no branch, no tag.
- Do not audit your own correction beyond the required gates. You do not certify it, you do not close the logical whole, and you emit no closure signal. If the same assumption survives this correction and its recheck, stop and return `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` rather than attempting a second automatic correction.

================================================================
7. GIT AUTHORITY
================================================================

One corrective commit, then one non-force fast-forward push to main, then a public readback.
- Stage exactly your allowlisted changed paths by EXPLICIT PATH.
- Review the FULL staged diff before committing.
- Suggested message: `fix(security): redact provider credentials by value in failure logs`. The body names orch-02-F21 and orch-02-D13.
- PRE-PUSH GATE, mandatory: `git ls-remote origin refs/heads/main` must still equal `8e82f3bda67751a74746ef15a634514609e3886f`. If it advanced, STOP and escalate.
- Push `git push origin main` only, no flags. READBACK `git ls-remote origin refs/heads/main` and `git rev-parse HEAD`; they must be equal and be your new commit. Porcelain empty afterwards.

================================================================
8. GATES AND REPORT CONTRACT
================================================================

Gates, all green at your terminal report:
  backend: mypy `Success: no issues found in 80 source files`; ruff `All checks passed!`; pytest `322 passed, 4 skipped` unchanged, summary quoted verbatim
  frontend: `npx vitest run` over the same ten files from exchange 01 — expect 193 plus your new tests, no failures; `npm run lint` exit 0; `npm run build` succeeds

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Then exactly once:

Logical whole identity: backend-security-hardening
Worker session ordinal: 09
Worker exchange ordinal: 02

Then, in this order:
- status; Phase-qualified result, labelled NON-INDEPENDENT
- the continuity anchor you verified and confirmation that the re-gate matched, or the exact conflict if it did not
- start and end commit; `git diff --stat` and `git diff --name-only`; which allowlisted paths you did not need
- repository gate and pre-push gate evidence
- capability recheck: material changes since the continuity anchor, required capabilities still observed, unknown or degraded capabilities, and the statement that capability does not grant authority
- Item A: the value-based redaction rule; the exact environment variable NAMES you match against, with NO values; the minimum length you chose and why; how you handled regex metacharacters; read-per-call versus cached and what that means for rotation; what you did about the `provider_transport` phase and why; and the before/after of the three benign messages
- Item B: the two 401 messages, and whether the login page override is now dead
- the before/after table for tests 1-8 with exact pre-fix results, with test 3 called out explicitly
- all gate output, with the pytest summary quoted verbatim
- an explicit statement that no real credential value, prefix, or length appears anywhere in this report, in a test, or in a committed file
- explicit statement that nothing was observed in a browser and that all provider failures were synthetic
- residuals, including any credential shape you believe could still escape and why you judge that acceptable
- authorized Git result with public readback and post-push porcelain
- deviations, risks, missing evidence
- out-of-scope observations, labelled as observations
- one smallest next step (expected: the Orchestrator issues the fresh independent dependency and supply-chain audit, INFOSEC 4.7 profile P-4, then the comprehensive fresh independent re-audit, INFOSEC 4.11 profile P-10)
- Report justification: new-mutation
- Logical-whole closure: not-closed
- Authority expiry statement
- Resolved Execution Issues / Near-Misses
- Pre-Existing Failure Classification

Stop conditions: repository gate failure; dirty porcelain; remote main advanced; a fix needing a non-allowlisted path or a dependency; any need to change a provider list; any risk of a real credential value reaching a report, a test, or a commit; any existing test regressing; a second automatic correction attempt for the same surviving assumption.

Authority expiry: this exchange's authority expires with your terminal report. Retained context is not a renewal.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
