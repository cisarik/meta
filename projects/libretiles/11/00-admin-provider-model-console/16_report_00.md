All evidence collected and containment cleaned. Rendering the report.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 16, Worker exchange ordinal: 01
```

**Security task class:** focused defensive audit — authN/Z specialization (INFOSEC 4.4)
**Owned/authorized target:** Libre Tiles canonical repository, candidate a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
**Commit under audit:** a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20 (start = end; no mutation)
**Scope:** the slice-5 candidate diff (exactly 14 paths measured in `git diff --stat f17a8ba..a17cdf4`) plus the authN/Z surfaces it touches: JWT mint, admin launcher, Node worker env/IPC, DiagnosticPly persistence, parameters_json, `backend/var/` artifacts
**Exclusions:** INFOSEC 4.6 provider boundary (not triggered — zero provider calls made, none required); K1 live NIM; slices 3b/6/7/8; APMC-S4-IA-F05/F06 (no reopen trigger measured — see findings)
**Threat model:** §2 of the prompt, audited as given. Measured delta: the Host-header binding (C6) is posture-dependent — `config/settings.py:100-114` enforces explicit, wildcard-free `ALLOWED_HOSTS` only when `DEBUG=false` (and refuses to boot otherwise, reproduced dynamically), while the local dev `.env` on this machine runs `DJANGO_DEBUG=true` with a wildcard host list, under which an arbitrary Host is accepted. This delta is recorded as finding F01 (accepted-residual, local-actor). No other deltas to the accepted threat model were measured.
**Source records:** OWASP Application Security Verification Standard (ASVS) 5.0.0, OWASP Foundation, official release, retrieved 2026-09-06; MITRE CWE, version 4.16, MITRE Corporation, retrieved 2026-09-06.
**Findings:** APMC-S5-IA-F01, F02, F03 (accepted-residual, full records below); APMC-S4-IA-F04 re-disposition (verified-closed); F05/F06 unchanged; two audit-internal rejected-false-positive results (probe artifacts, disproven, recorded in the findings section).
**Containment ledger:**

| Root | Owner | Mode | Contents | Cleanup owner | Outcome |
|---|---|---|---|---|---|
| `/tmp/opencode/s5-ia/` | agile (worker-16/ex01) | 0755→chmod 0700 before token-bearing probes | probe scripts, gate logs, stub worker, synthetic-credential env dump (never printed), launch-response HTML, redirected runner `var/` output | worker-16/ex01 | removed (`rm -rf /tmp/opencode/s5-ia`), verified absent |
| Django throwaway test DB (DiscoverRunner `setup_databases`/`teardown_databases`, all probes) | worker-16/ex01 | n/a | synthetic accounts/runs only; dev DB untouched | DiscoverRunner teardown | destroyed each run; no dev-DB writes |
| `backend/var/` (residue) | worker-16/ex01 | gitignored | 20 stub-worker log/report files created by the mandated full-pytest re-run (implementer's suite writes there); my own runner probes redirected output to `/tmp/opencode/s5-ia/vard` and never wrote here | worker-16/ex01 | removed as single declared path; porcelain still 0 |

No network targets. No wildcards. `git status --porcelain=v1` = empty before and after; reflog lineage clean (f17a8ba → a17cdf4).

**Limitations:** (1) frontend typecheck/lint/build not re-run — optional per prompt, no frontend mutation this session; implementer's vitest number not copied as mine. (2) Fetch-guard egress blocking (`ai-play-diagnostic.ts:157-175`) is established-static: the shipped generic_unchanged path makes zero fetch calls (proven dynamically), and the audit constraint forbids any live egress test; the worker-error `scrub()` (diagnostic-worker.mjs:36-40) and runner `_log` scrub (run_diagnostic_match.py:178-186) are likewise code-measured, not provoked dynamically. (3) Admin-HTML no-echo is proven structurally — the token is never persisted anywhere (C1 + full sweep of every persistence surface), so no admin page can render it. (4) F05/F06 re-dispositioned without their original finding text in this session's material.

**Residual-risk summary:** three accepted-residuals (F01-F03), all local-actor or dev-posture, none reachable in the deployed (DEBUG=false) posture, none blocking. The minted service JWT is a real credential (stated in C4): ≤6 h lifetime, revocation-resistant until expiry (F02). Acceptance decision can proceed on these dispositions.

---

**Compact core**

1. Coordinates: echoed above.
2. **Status: PASS** (audit completed per §3; all claims dispositioned; no repository mutation).
3. Phase-qualified result: **not-applicable** (audit exchange; `acceptance-PASS` is not mine to claim).
4. Start/end commit: a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20 / a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20.
5. Changed files: **none** (repository gate: HEAD, `.ap` gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656, empty porcelain — all verified twice).
6. Tests and validation — gates re-run verbatim: mypy `Success: no issues found in 93 source files`; ruff `All checks passed!`; pytest `898 passed, 4 skipped in 551.84s (0:09:11)`. Proven **dynamically** (throwaway test-DB probes + real runner + real Node worker): C1, C2, C3, C4, C5, C6 (production posture), C7, C9, C10 (incl. migration 0011 un-apply/re-apply), C11 (sentinel refusal), C13, C14. Proven **statically**: C8 (abort byte-identity via git extraction diff; cancel/authorship code order), C11's fetch-guard egress subclaim, C12 (byte-diffs), C2's error-scrub subclaim, plus C3's single-caller grep.
7. Commit/push result: not-applicable (no Git authority exercised).
8. Deviations, risks, missing evidence: `backend/var/` residue from the mandated pytest re-run removed (ledger); my probes had two instrumented-and-corrected probe bugs (rejected-false-positive in findings); C13 has no separate header in §3 — its text is folded into C12's block after "SIMPLE_JWT ds." (numbering artifact); no evidence missing beyond the static-only subclaims listed under Limitations.
9. One smallest next step: none required from this audit — ORCHESTRATOR dispositions F01–F03 and the F04 closure.
10. Report justification: **new-evidence**.
11. Authority-expiry: this Worker's authority expires upon rendering this report; it extended only to read-only audit, throwaway test-DB probes, and the declared `/tmp/opencode/s5-ia` root; no closure signal is emitted.

```text
Resolved Execution Issues / Near-Misses: none (product-side). Probe-side near-misses: placeholder seat ids caused a misleading C5 failure and the C6 probe initially ran under the dev-posture wildcard env producing misleading FAILs — both instrumented, root-caused as probe artifacts, and corrected; no canonical repo state was touched.
Pre-Existing Failure Classification: none new. F02's revocation gap is inherent to the access-only mint policy that the APMC-S4-IA-F04 disposition deliberately chose; it landed with this slice and is dispositioned as accepted-residual, not a new failure.
Orchestration critique: MEASURED, lead item first — (1) claim C13 exists only as a truncated fragment folded into C12's block ("SIMPLE_JWT ds." is mid-sentence cut); I audited its content as its own row; future prompts should renumber. (2) C6 was the right question and got adequate weight; its honest answer splits by posture, which the threat model's single sentence did not signal — the production guarantee is real and settings-enforced (wildcard refuses to boot at DEBUG=false), the dev .env wildcard is the delta. (3) No contradiction found between this prompt's instructions after the assumed-contradiction check: containment (temp roots) vs. read-only repo are consistent; the runner's var/ output was redirected rather than suppressed, which honors both. (4) The claim list's evidence discipline ("implementer's report is a CLAIM") was honored; nothing in C1-C14 was the wrong question.
Enumeration widened: middleware/axes chain, `CORS_ALLOW_ALL_ORIGINS = DEBUG` (pre-existing dev-only posture, not this diff), PasswordAwareJWTAuthentication iat/password_changed_at handling for the service token (password_changed_at None → normal auth, no bypass found), admin `readonly_fields` completeness (every DiagnosticRun field readonly), spawn-env set-equality check, reflog lineage, `.gitignore` backend/var entry.
```

---

### Per-claim verdict table

| Claim | Verdict | Evidence class | One-line evidence pointer |
|---|---|---|---|
| C1 access-only mint | **verified-closed** | reproduced-dynamic | `AccessToken` MRO `['AccessToken','Token','object']` (no BlacklistMixin; RefreshToken contrast persists OutstandingToken); mint left OutstandingToken 0→0; payload exp−iat=1200 (per-token `set_exp`, services.py:1512); SIMPLE_JWT 2 h unchanged; F04 row below |
| C2 no echo | **verified-closed** | reproduced-dynamic | End-to-end run: minted JWT absent from Node argv/env-dump, IPC lines, log (`Bearer` absent), report, DiagnosticPly blob, parameters_json; real worker outbound observation has no token key/JWT substring; scrubs static at diagnostic-worker.mjs:36-40, run_diagnostic_match.py:178-186 |
| C3 mint callers | **verified-closed** | reproduced-dynamic | Sole caller run_diagnostic_match.py:769-771 (grep), mint at services.py:1512; mint occurs at :251-255 after claim; spawn argv exactly `[python, manage.py, run_diagnostic_match, --run-id, <uuid>]`, env = os.environ − APPIMAGE/ARGV0/APPDIR, no JWT, `start_new_session`+DEVNULL; no `call_command` in admin.py |
| C4 stolen-JWT capability | **verified-closed** | reproduced-dynamic | Service JWT: own diagnostic session 200 (slot0 = service user), product game 404 (`services.py:484` membership), login 401 (unusable password), `/api/auth/me` rename 400 (`accounts/serializers.py:53-61`), create_game/join queue refused 400 (`services.py:1083-1101`), admin 302 (not a Bearer surface); residual = F02 |
| C5 launcher authz | **verified-closed** | reproduced-dynamic | admin.py:433 guard + :461 `admin_view`: anon 302, no-perm staff 403, CSRF-missing POST 403, valid launch 302→changelist with 1 spawn, created_by=request.user, second in-flight 302 message (no 500), configure-failure row aborted `failed/launch_configuration_invalid` (not stuck queued), no base_url field |
| C6 django_origin / Host | **verified-closed** (production posture; residual F01) | reproduced-dynamic | Sole writer admin.py:607 `build_absolute_uri("/")`; DEBUG=false: evil Host → 400 on admin+API, wildcard+DEBUG=false refuses to boot (ImproperlyConfigured); DEBUG=true + dev `.env` wildcard: Host accepted — F01 accepted-residual |
| C7 Node env / worker path | **verified-closed** (residual F03) | reproduced-dynamic | `_worker_env_whitelist` (run_diagnostic_match.py:87-102): Django env had DJANGO_SECRET_KEY/DATABASE_URL/NVIDIA_API_KEY/OPENROUTER_API_KEY — all absent from dumped Node env; JWT only as `LIBRETILES_AI_PLAY_JWT`; fragment-offender keys none (STUB_* only under override); argv `[node, worker]` |
| C8 cancel ≠ abort | **verified-closed** | reproduced-dynamic + established-static | abort_diagnostic_run byte-identical to f17a8ba (git extraction diff, 0 changed lines); cancel sets cancelled/cancelled, session abandoned, empty game_end_reason, no Move creation; authorship abort ordered after `_persist_ply` (:660 → :666-672); runner observes cancelled → `_finish(0)` no abort (:622-624) |
| C9 in-flight unique | **verified-closed** | reproduced-dynamic | `unique_inflight_diagnostic_run` IntegrityError fired on second create; stale flip `max(300, 2·max_wall_clock)` → abandoned/stale_heartbeat; never-claimed queued (no heartbeat) untouched; zero cap refused by configure; launcher + runner double refusal |
| C10 DiagnosticPly secrets | **verified-closed** | reproduced-dynamic | Mechanical scan: 0 of 25 column names contain any SECRET_KEY_FRAGMENTS substring; ply blob and JSON carry no JWT; migration 0011 = reversible CreateModel on 0010 — un-applied (table dropped) and re-applied dynamically; models.py diff append-only (no DiagnosticRun field added) |
| C11 fake-mode containment | **verified-closed** (egress subclaim static) | reproduced-dynamic + established-static | `LIBRETILES_AI_PLAY_LIVE=1` → CommandError refusal before claim/mint; launcher hardcodes script `generic_unchanged`/`selected-only` (parameters_json evidence); `executed_runtime_mode=fake`; worker guard `installFetchGuard(backendOrigin, {mode:"fake"})` blocks every non-backend origin (ai-play-diagnostic.ts:157-175, static); zero provider calls made; no base_url |
| C12 formed-word/scoring invariants | **verified-closed** | established-static | `git diff f17a8ba..a17cdf4` over `backend/gamecore/`, `backend/game/position_sets.py`, `backend/game/diagnostics.py`, `frontend/package.json` = 0 lines; `_reject_ai_nonscoring` (services.py:717) outside the additions-only hunk; package.json has no `"type"` key; settings.py not in diff (SIMPLE_JWT byte-unchanged) |
| C13 parameters_json credential rejection | **verified-closed** | reproduced-dynamic | `_reject_credential_parameters` (services.py:1399-1412): fragment key rejected, JWT-like value rejected, benign `django_origin` accepted; header absent from §3 (folded into C12) — content audited as its own row |
| C14 IPC contract | **verified-closed** | reproduced-dynamic | Captured runner→Node lines: run_turn keys exactly `{ai_slot, cmd, game_id, max_steps, model_id, provider, queue_mode, script, seq, timeout_seconds}`, plus `{cmd:"shutdown"}`; no token field, no JWT substring; Node reads JWT from env only (diagnostic-worker.mjs:20-22); outbound observation keys measured, no token key |
| **APMC-S4-IA-F04 re-disposition** | **verified-closed** | reproduced-dynamic | Owed disposition delivered: mint is AccessToken-only (`for_user` + `set_exp`), no RefreshToken on runner/admin path (single-caller grep + OutstandingToken unchanged across a full admin launch), lifetime override per-token (exp−iat measured), SIMPLE_JWT default untouched, never echoed (C2 sweep), token-blacklist admin has nothing to display (never persisted) |

### Findings (Security Finding Record shape)

**Finding ID:** APMC-S5-IA-F01
**Title:** Dev-posture wildcard ALLOWED_HOSTS makes django_origin Host-controllable when DEBUG=true
**Status:** accepted-residual · **Severity:** low · **Confidence:** high
**Evidence class:** reproduced-dynamic
**Affected commit:** a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
**Affected component and exact location:** backend/config/settings.py:100-114 (`_allowed_hosts`); consumption at backend/game/admin.py:607 and run_diagnostic_match.py:257-263
**Security property:** django_origin bound to operator-declared hosts
**Asset at risk:** service JWT (minted post-launch, sent as Bearer to django_origin)
**Trust boundary:** Node worker → Django HTTP (BACKEND_URL + Bearer)
**Attacker-controlled input or local actor:** Host header of the launch request, under a DEBUG=true host whose `DJANGO_ALLOWED_HOSTS` is wildcard (this machine's dev .env)
**Reachability:** established only when the server runs DEBUG=true AND the operator env sets a wildcard host list; production posture (DEBUG=false) returns 400 for evil Hosts and refuses wildcard configs at boot (both reproduced dynamically). Deployment docs configure DEBUG=false.
**Preconditions:** dev server with DEBUG=true + wildcard env; admin logged in; attacker achieves same-origin view of the admin (e.g. DNS rebinding on the dev host) to obtain the CSRF token and POST launch.
**Required privileges:** local/network-adjacent attacker plus an authenticated admin session on a DEBUG=true host
**Observed or potential impact:** minted runner JWT delivered as Bearer to an attacker-chosen origin.
**C/I/A effect:** confidentiality of the ≤6 h service credential; no integrity/availability effect on game rows.
**CWE mapping:** CWE-346 (Origin Validation Error), CWE 4.16 · **ASVS mapping:** ASVS 5.0.0 chapter V3 (session/token handling) host-binding expectation
**Source-standard references:** OWASP ASVS 5.0.0, retrieved 2026-09-06; MITRE CWE 4.16, retrieved 2026-09-06
**Dynamic reproduction evidence:** probe with `DJANGO_DEBUG=false DJANGO_ALLOWED_HOSTS=testserver` → evil Host 400 on admin+API; `DJANGO_ALLOWED_HOSTS='*'` + DEBUG=false → `ImproperlyConfigured: ... without wildcards when DEBUG is false`; dev .env posture measured `ALLOWED_HOSTS ['*','testserver'], DEBUG True` with evil-Host requests accepted.
**Static evidence:** settings.py:100-114 enforces the guarantee exactly when DEBUG=false; candidate code does not weaken it.
**Synthetic containment:** throwaway test DBs; containment root removed.
**False-positive analysis:** would be disproven if a production path could run DEBUG=true with wildcard hosts, or if django_origin had a second writer (grep: none).
**Exploitability conclusion:** plausible but unproven (dev-host local actor; no demonstrated attack)
**Smallest safe correction direction:** none required in the candidate; optionally document that the dev env must pin DJANGO_ALLOWED_HOSTS (operator guidance, not code).
**Regression-test requirement:** keep a settings-level test that DEBUG=false + wildcard raises ImproperlyConfigured (exists in suite behavior; the negative-path lock should remain).
**Residual risk:** a developer running DEBUG=true wildcard locally accepts the same exfil chain against their local-only synthetic credentials.
**Acceptance-blocking decision:** non-blocking — local-actor residual outside the deployed posture; the settings code actively forbids the dangerous production configuration.
**Redaction requirements:** never print JWT strings or .env contents; report posture facts only.

**Finding ID:** APMC-S5-IA-F02
**Title:** Minted access-only runner JWT is revocation-resistant until expiry (inherent to the chosen F04 policy)
**Status:** accepted-residual · **Severity:** low · **Confidence:** high
**Evidence class:** reproduced-dynamic (lifetime) + established-static (no revocation path)
**Affected commit:** a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
**Affected component and exact location:** backend/game/services.py:1512-1532 (mint, lifetime = min(max_wall_clock_seconds + 600, 6 h), run_diagnostic_match.py:252-255)
**Security property:** credential lifecycle / revocability
**Asset at risk:** service JWT (gameplay authority on the diagnostic session)
**Trust boundary:** runner → Node env → Django HTTP
**Attacker-controlled input or local actor:** local reader of the Node process env or log/report surfaces (all measured clean — see C2)
**Reachability:** not established for theft (C2 disproved every echo surface); the property measured is that once minted, the token cannot be blacklisted (AccessToken is not persisted; `blacklist_outstanding_refresh_tokens` covers refresh tokens only) and `password_changed_at`-iat rejection cannot apply (service account has an unusable, never-changed password).
**Preconditions:** credential obtained via some out-of-band local compromise
**Required privileges:** local
**Observed or potential impact:** stolen token remains valid up to 6 h against the diagnostic session it owns; product-game access stays 404 (C4) and profile/queue/refusals hold.
**C/I/A effect:** confidentiality (bounded, scoped)
**CWE mapping:** CWE-613 (Insufficient Session Expiration), CWE 4.16 · **ASVS mapping:** ASVS 5.0.0 V3 token-invalidation expectation
**Source-standard references:** as above, retrieved 2026-09-06
**Dynamic reproduction evidence:** minted token payload exp−iat honored per-token; no OutstandingToken written (nothing to blacklist); C4 capability sweep.
**Static evidence:** `AccessToken` MRO lacks BlacklistMixin; no revocation call exists on the runner path.
**Synthetic containment:** throwaway test DBs; synthetic mint inside contained root.
**False-positive analysis:** would be disproven if simplejwt exposed an un-persisted access-token blacklist (installed version: no).
**Exploitability conclusion:** not demonstrated (no echo surface found; C2)
**Smallest safe correction direction:** none for this slice; if shorter blast radius is later wanted, cap `_TOKEN_MAX_LIFETIME_SECONDS` below 6 h — a policy choice, not a defect fix.
**Regression-test requirement:** keep the OutstandingToken-count-zero mint regression (present in implementer suite; re-run here as gate).
**Residual risk:** ≤6 h scoped credential window after a hypothetical local compromise.
**Acceptance-blocking decision:** non-blocking — this is the credential-retention policy the F04 disposition selected; the trade was explicit.
**Redaction requirements:** never print the token.

**Finding ID:** APMC-S5-IA-F03
**Title:** LIBRETILES_DIAGNOSTIC_WORKER allows an arbitrary worker executable; STUB_* forwarding only under that override
**Status:** accepted-residual · **Severity:** info · **Confidence:** high
**Evidence class:** established-static + reproduced-dynamic (override honored, whitelist identical)
**Affected commit:** a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
**Affected component and exact location:** run_diagnostic_match.py:76-84 (`_worker_path`), :87-102 (whitelist), :95-101 (STUB_* branch)
**Security property:** process-spawn integrity (worker script fixed by default)
**Asset at risk:** runner process integrity; by extension the JWT it mints
**Trust boundary:** Django host env → runner → child process spawn
**Attacker-controlled input or local actor:** local actor who can set the Django host process env — who can already execute code in that trust domain
**Reachability:** production default (override unset) hits the committed `frontend/scripts/diagnostic-worker.mjs`; a missing worker fails closed (`_RunnerFailure`). The override is a documented test harness; STUB_* names reached the Node env only because I set the override (measured).
**Preconditions:** control of the server process env
**Required privileges:** local (server-operator class)
**Observed or potential impact:** arbitrary executable spawned as "worker" — equivalent to local code execution the actor already has
**C/I/A effect:** none beyond the local actor's existing power
**CWE mapping:** CWE-15 (External Control of System or Configuration Setting), CWE 4.16 · **ASVS mapping:** none specific (configuration surface)
**Source-standard references:** MITRE CWE 4.16, retrieved 2026-09-06
**Dynamic reproduction evidence:** stub run with override set — STUB names present, forbidden names absent, argv `[node, <override path>]`
**Static evidence:** `_worker_path()` reads env; default is the committed script
**Synthetic containment:** contained root, removed
**False-positive analysis:** would be a real finding if the override were settable by a remote request (it is not; no HTTP/IPC writer)
**Exploitability conclusion:** not applicable (local-actor tautology)
**Smallest safe correction direction:** none required; optionally log the worker path at spawn (name only) for forensics
**Regression-test requirement:** none (behavior is intended test-harness surface)
**Residual risk:** accepted local-actor residual
**Acceptance-blocking decision:** non-blocking
**Redaction requirements:** none

**Rejected-false-positive results (audit-internal, disproven):**
1. "Valid launch POST returned 200 with unknown error" — disproven: my probe's form dict still carried placeholder seat ids; the isolated clean-state probe shows 302→changelist with one correct spawn. Not a product defect.
2. "Evil Host accepted on launch POST (potential JWT exfil)" as a candidate-code claim — disproven for the deployed posture: the settings module returns 400 and refuses wildcard configs at DEBUG=false; the accepted portion is recorded as F01 (operator dev posture).

**APMC-S4-IA-F05/F06:** unchanged, remain `rejected-false-positive` from slice 4-IA. Reopen trigger measured: none — this diff does not touch a surface in a way that reintroduces those patterns per the material available to this session; no new evidence was produced against them.

**APMC-S4-IA-F04 (owed disposition):** **verified-closed** — see table row; the smallest-safe-correction question ("choose token type/lifetime and storage/admin exposure policy before the runner mints") was answered in code exactly as claimed and re-measured independently.

Context pressure: moderate — comfortably sufficient for the full audit; no truncation of required reading.

**Explicit authority-expiry statement:** This Worker session's authority is exhausted upon submission of this report. I performed no implementation, correction, or mutation of the canonical repository, emitted no closure signal, and will not begin K1, slice 3b, or any correction. Disposition of F01–F03, F04, and acceptance of a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20 rest with the ORCHESTRATOR.