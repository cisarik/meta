### Report for ORCHESTRATOR_CHAT

Logical whole identity: release-readiness-triage
Worker session ordinal: 01, Worker exchange ordinal: 01

status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates no Libre Tiles file and no Meta file
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: R1 (parity payload pin), R2 (aria-live count), R3 (ReplayControls stale string) — all three re-measured red by this Worker at `996d9c7`, all pre-existing, none caused by this exchange.

Planning Record:

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Repository gate: HEAD = origin/main = `996d9c78af90d1fea21e3c701283ba11e59de0b1`; `.ap` gitlink and checkout = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `git status --porcelain=v1` empty; branch `main`. All mandatory-reading files present and read.

---

## D1 — Verified open-item inventory

Every evidence cell below is my own measurement at `996d9c7` (focused-test runs through the RF-16 env-cleared route; greps/reads against the live tree). Full-suite counts for un-re-run gates are carried from `18/00/07_report_00.md` and labelled as carried.

| Item | Evidence (path/line/command) | Current status | Owner-if-known | Affected surface | Severity/impact |
|---|---|---|---|---|---|
| R1 parity payload pin red | Re-run: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_word_authority_parity.py::PersistedPayloadParityTests::test_human_persisted_move_payload_matches_the_pinned_baseline` → FAILED at `backend/tests/test_word_authority_parity.py:1049`; persisted `words_formed` carries an extra `inspection` block. Cause: commit `e2c2549` added `capture_move_inspection` (`backend/game/services.py:75,992,1020`, `backend/game/inspection.py`) for the admin deep move inspector — a deliberate feature. The three protected oracle-guard tests (`-k "pinned_digest or byte_identical or baseline_helper_executed"`) pass (3 passed); `ORACLE_SOURCE_SHA256=260bfe15…` (test file :22) and the frozen `_word_passes_dictionary` segment (b50f84a, lines 209–222) are untouched. The stale pin is the payload literal at :1049–1056, NOT the protected oracle. | open | W-B (codebase-hygiene) slice S1 | backend test file | medium (suite-red, sign-off record exists; oldest carried residual) |
| R2 aria-live count red | Re-run: `npx vitest run src/lib/i18n/i18n.test.ts` → 1 failed, 82 passed; `AC-ONE-LIVE-REGION` (describe at `i18n.test.ts:829`) fails at `:839`, measured `aria-live` 3, expected 1. The three sites (all measured): `frontend/src/components/game/LiveAnnouncer.tsx:25`, `frontend/src/components/admin/ReplayControls.tsx:19`, `frontend/src/components/admin/SimulationArena.tsx:39`. | open | accessibility-pin decision → deferred D1 (P4); test stays red until then | frontend test + 2 admin components | low (quality/a11y pin) |
| R3 ReplayControls stale expectation | Re-run: `npx vitest run src/components/admin/ReplayControls.test.ts` → 1 failed; test expects "Ada played SZ for 12 points" (`ReplayControls.test.ts:9`), component renders "Ada played AT for 4 points" from the committed fixture. Truth chain measured: `admin-replay.fixtures.ts:19` has `words_formed:[{word:"AT",score:4}]`, `points:4`; `ReplayControls.tsx:12` renders `words_formed` + `move.points`; git shows `a7f9960` (fixture+test with SZ/12) then `e2c2549` (fixture rewritten to AT/4 with `inspection`, test not updated). Additional measured drift: the fixture's `placements`/`board_delta`/`finalBoard` still tell the SZ story while `words_formed`/`inspection`/cumulative scores tell AT — the fixture is internally inconsistent at HEAD. | open | W-B slice S2 | frontend fixture + test | low (suite-red) |
| R4 judge docstring Tier-2 claim | `frontend/src/app/api/ai/judge/route.ts:11` "Tier 2: Online dictionary API (optional) — Django" inside the validation-pipeline list. Repo-wide "Tier" scan: only other site is `frontend/src/lib/provider-registry.ts:34` (`ProviderCatalogTier` — a different concept). Docs are correct: `docs/architecture.md:242,258`, `libretiles_PRD.md:70-72,163` mark Tier 2 planned/not implemented. | open | W-B slice S3 | frontend docstring | info |
| R5 port-80 canonical redirect for any Host | `deploy/nginx/nginx.conf.template:28-46`: port-80 `default_server` has no Host conditional; `deploy/nginx/entrypoint.sh:54` full mode renders `301 https://${DOMAIN}$request_uri` (literal, no reflection), `:58` bootstrap renders `503`; 443 rejects non-canonical hosts (`if ($host != __DOMAIN__) return 444;`). Guarded by `scripts/validate_docker_deployment.sh:388-394` and `backend/tests/test_docker_deployment.py:522-526`. | open (accepted residual, info) | Cooperator decision in W-D (keep vs close-connection) | deploy template | info |
| L1 X-Powered-By | `deploy/nginx/nginx.conf.template:12` has `server_tokens off;`; `rg proxy_hide_header/X-Powered-By deploy/` → zero hits. Audit-05 reproduced `X-Powered-By: Next.js` on public responses. | open | W-D | deploy template | info |
| L2 undefined ws path → 500 traceback | `backend/game/routing.py:6` has only `^ws/game/(?P<game_id>[^/]+)/$`; `nginx.conf.template:185` proxies every `/ws/` path to Daphne; Channels "No route found" → HTTP 500 + ERROR traceback (reproduced-dynamic in `18/00/05_report_00.md` finding DVP-AUDIT-05-F01, static-verified by me). | open (decision: code fix / nginx guard / accept) | W-D, Cooperator decision | Channels routing + nginx | low/info |
| L3 5-second `nginx -t` retry | `deploy/nginx/entrypoint.sh:65-74`: `while sleep 5; do` … marker-gated; on failing `nginx -t` the marker persists and the loop retries every 5 s (log noise via stderr; last-good config keeps serving). | open (decision) | W-D, Cooperator decision | nginx entrypoint | info/low |
| L4 malformed/user@host Host on 80 → nginx 400 | Port-80 server performs no Host inspection; nginx core rejects malformed Host headers with 400 (dynamic observation in `18/00/07_report_00.md`; static template evidence above). No redirect, no reflection. | already-closed (never a defect; accepted residual) | — | nginx core | info |
| G1 Tier 2 dictionary | Same evidence as R4; planned product work, documented. | open (roadmap — NOT a triage whole) | post-release roadmap | docs/backend | roadmap |
| G2 stronger AI search | `AGENTS.md:206` lists it under "Not done yet"; `backend/gamecore/move_search.py` exists and ships ranked candidates (`DEFAULT_MAX_ELAPSED_MS`/`DEFAULT_RANKED_MAX_ELAPSED_MS` per `PROJECT_CONTEXT.md` lock 9), so the claim is partially satisfied; `docs/architecture.md:467-478` names the remaining (anchor/lane generation, persisted diagnostics). | open (roadmap, partially implemented) | roadmap | gamecore/frontend | roadmap |
| G3 eight catalogs unreviewed | `REVIEWED_LOCALES=["en","sk","cs","pl"]` at `frontend/src/lib/i18n/i18n.test.ts:63`; `LOCALE_FLAG_SRC` = `Partial<Record<Locale,string>>` with 12 entries at `frontend/src/app/settings/page.tsx:358-372` (conditional spread at :403); `VARIANT_FLAG_SRC` with 12 slugs at `frontend/src/components/settings/GameLanguagePanel.tsx:30-44` (conditional spread at :70). PARTIAL-by-design invariant documented in both files. | open (documented gap) | W-G, Cooperator decision | frontend i18n | quality |
| G4 hu.png / drevo.jpeg | `frontend/public/` = 12 locale flags + `hu.png` + `drevo.jpeg`. Measured: `drevo.jpeg` IS referenced 3× (`frontend/src/app/globals.css:109,151,213`); `hu.png` is deliberately unreferenced (comment `settings/page.tsx:356-357`; Cooperator decision 8 in `PROJECT_CONTEXT.md:1046-1047`). | already-closed (never a defect) | — | assets | none |
| G5 Node support matrix | No `engines` field in `frontend/package.json` (rg exit 1); `CONTRIBUTING.md:10` claims "Node 20.19+ or 22.12+". | open | W-B slice S3 | docs/package.json | info |
| G6 CI/SBOM | No `.github` directory (measured); `libretiles_PRD.md:147` "GitHub Actions workflows remain planned"; `audit-02-F05` medium accepted-residual with Cooperator sign-off 2026-09-01 (`DEFECT_LEDGER.md:545-557`). | open (decision) | W-E, Cooperator decision | repo meta/CI | medium (sign-off exists) |
| G7 catalog flags/schedule | `backend/config/settings.py:500-501` `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` default "false"; schedule documented only (`docs/architecture.md:333-346`, `docs/vps_deployment_guide.md:257-263`) under separate production authority. No defect measured. | already-closed (documented; D2-adjacent production authority) | — | config/docs | none |
| G8 session-storage/CSP hardening | `frontend/src/lib/security-headers.ts:97-98`: nonce + `'strict-dynamic'` script-src (closed at cb4efed); `style-src 'unsafe-inline'` = accepted low residual with sign-off; JWT in localStorage = accepted low residual (no XSS sink). **But the DEFECT_LEDGER carry list contains one still-open medium: audit-04-F01/orch-05-D14 — see N6.** | mostly already-closed; N6 open | N6 → W-C | settings/headers | N6 = medium in deployed topology |
| G9 hygiene umbrella | Whole-17/18 forward horizons both name `codebase-hygiene-and-residual-reconciliation` (measured in `17/00/99_closure.md:87`, `18/00/99_closure.md:102`). Overlaps R1/R3/R4/G5; G4 disproven. | open (umbrella) → W-B | W-B | multi | — |
| G10 marker sweep | Repo-wide `TODO|FIXME|HACK|XXX` (case-insensitive, excluding node_modules/.venv/.next/__pycache__/.git/.ap/locks/binaries): ZERO code hits; the only matches are dictionary words (`backend/assets/dicts/*.txt`: "hack", "xxx", "todo"). Prose sweep (`not done|not yet|not implemented|deferred|accepted-residual|carry forward|out of scope`, markdown only): 9 hits, all classified — PRD Tier-2/planned UI items (:70,:163,:164,:165), `AGENTS.md:198`, `docs/architecture.md:258`, `docs/vps_deployment_guide.md:249`, `GLOSSARY.md:101` (plural-helper param rename deferred), `GLOSSARY.md:133` (focus trap out of scope by design). | already-closed (sweep run, nothing new in code) | — | repo | none |
| G11 test-breadth gaps | `backend/pyproject.toml:73-78`: `addopts=-q`, markers `slow`, `postgres`; postgres parity opt-in `LIBRETILES_TEST_POSTGRES=1` (`backend/tests/test_postgres_dialect_parity.py:40-44`, 6 marked tests); 18 `slow` tests env-gated per file (e.g. `test_slovak_full_game.py:360`, endgame matrix, strength/benchmark skipifs). Vitest: `provider-capability.live.test.ts` sentinel-gated, `ai-play-diagnostic.live.worker.test.ts`/`.worker.test.ts` skipIf-gated, `plural.test.ts:190` conditional skip; no Playwright anywhere (no e2e dir, no config; PRD:134,155 planned). Baseline full-suite counts carried from `18/00/07_report_00.md`: pytest 1 failed/1242 passed/27 skipped, npm test 2 failed/718 passed/3 skipped. Seed's "4 skipped" is the stale era-10 number. | open (decisions) | W-F, Cooperator decisions | tests | quality |
| G12 release-readiness | **New from my sweep: no LICENSE file at repo root** while `README.md:205-207` says "License: MIT" and PRD NFR-04 claims MIT. No CHANGELOG. `frontend/package.json` name "frontend" version 0.1.0; `backend/pyproject.toml` name "libretiles-backend" version 0.1.0, no license field. Lockfiles present; `env -u APPIMAGE -u ARGV0 -u APPDIR ~/.local/bin/poetry check --lock` → exit 0 (backend lock consistent, offline). npm lockfile drift unverifiable offline; advisories need network. | open | W-A (license) + W-H (deps) | packaging | blocker (licensd Docker topology** |
| N6 proxied-axes lockout | New from my widening of G8: `backend/config/settings.py:473-475` unchanged (`AXES_LOCKOUT_PARAMETERS=[["username","ip_address"]]`, no ipware); `backend/pyproject.toml:22` `django-axes==8.3.1` (no ipware extra); `docker-compose.yml:19` sets `DJANGO_NUM_PROXIES="1"` (fixes the DRF-throttle half only); template sets `X-Forwarded-For $remote_addr` (overwrite). Behind nginx, axes keys on REMOTE_ADDR = nginx's address → (username, nginx) global lockout bucket → account-targeted DoS, extendable indefinitely (`AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT` default true). Residual record `DEFECT_LEDGER.md:529-543` mandates the regression test "in the deployment whole"; no test covers a proxied axes IP (measured: only `test_security_settings.py:835-842` middleware ordering, `test_docker_deployment.py:487` XFF-presence). Whole-18 fixed DRF but not axes, and its closure residual table does not list it. | open — pre-deployment blocker | W-C | backend settings + Docker topology | medium in deployed topology (sign-off for residual exists; correction is the trap-documented one — precedence order + proxy order right-most + proxy count must be set together, `DEFECT_LEDGER.md:488-508`) |
| N7 Bulgarian lexicon licence blocker (mec-13-D04) | No `bg`/`bulgarian` anywhere in `backend/assets/` (12 variant manifests measured). Unshipped language; ledger row open. | open (roadmap for a not-shipped 13th language) | roadmap | assets | roadmap |

## D2 — Rejected false positives (measured disproof, not doc claims)

- **G4 is not a defect.** `drevo.jpeg` is actively used (`globals.css:109,151,213`); `hu.png` is deliberately unreferenced and documented as such (`settings/page.tsx:356-357`; Cooperator decision 8). No deletion, no "asset hygiene" whole.
- **L4 is not a defect.** Malformed Host → nginx core 400 with no Location is correct default behavior; the reflection was already removed by the whole-18 correction.
- **G7 is not a defect.** Flag default false, rollout/rollback documented; the schedule is a documented D2 production-authority item.
- **The frozen parity oracle is NOT the failing part of R1.** The three oracle-guard tests pass (3 passed, 47 deselected); `ORACLE_SOURCE_SHA256=260bfe15…` holds. What is stale is the persisted-payload literal at `test_word_authority_parity.py:1049`, a different pin added by the same file — this distinction is the entire basis for the S1 re-pin route.
- **Seed count corrections:** "pytest skipped 4" is the era-10 number (27 at baseline, carried from 07_report); seed's R2 line "i18n.test.ts:829" is the describe line (assertion at :839 — both exist); `PROJECT_CONTEXT.md:63-64` ("Flags exist for four locales") is a stale Meta claim — the tree ships all twelve flags; per P6 it is evidence, not ours to rewrite.
- Everything else in the seed list (R1, R2, R3, R4, R5, L1, L2, L3, G1, G2, G3, G5, G6, G8→N6, G9, G10, G11, G12) checks out as measured above. If "the seed list is correct on all counts" were the claim, this D2 says: correct except G4, L4, G7, and the three citation corrections.

## D3 — Logical-whole decomposition

```text
W-A  release-license-and-packaging                                        [bucket A]
     Objective: make the repository's MIT claim concrete and its release metadata legible.
     In scope: add root LICENSE (MIT text), align README.md:205-207 + PRD NFR-04, add a minimal
       CHANGELOG.md, decide package naming/versioning (frontend "frontend" → libretiles-frontend or
       leave; versions 0.1.0 both sides), optional pyproject license field.
     Out of scope: any code/test change; CI; docs claims beyond license/version.
     Evidence basis: G12 (LICENSE absent), D1 N2.
     Slices: S1 license + claims; S2 changelog skeleton + naming/version decision (Cooperator).
     Route: R0 (documentation/metadata only). Network: none.
     Dependencies: none. Acceptance: LICENSE file exists and is the exact MIT text; README/PRD claims
       match; gates green; fresh-acceptor diff review.

W-B  codebase-hygiene-and-residual-reconciliation                          [bucket A (S1), B (S2,S3)]
     Objective: close every carried code/test-truth residual so the standing gate set is green except
       the D1-owned R2 red.
     In scope: backend/tests/test_word_authority_parity.py (payload pin only), frontend
       admin-replay.fixtures.ts + ReplayControls.test.ts, judge/route.ts docstring, package.json
       engines + CONTRIBUTING.md prose.
     Out of scope: the frozen oracle segment + its digest constant (protected, P3); any production
       gamecode/ file; i18n.test.ts:829-841 and the three aria-live sites (P4); new features.
     Evidence basis: R1, R3, R4, G5.
     Slices (in order):
       S1 parity-payload re-pin (approval-gated): exact edit pre-approved by the Orchestrator as a
         bounded evidence decision — update the payload literal at test_word_authority_parity.py:1049
         to the canonical e2c2549 shape (assert stable fields word/score/multiplier/coords exactly and
         pin the inspection block shape/digest separately), add provenance comment; forbid touching
         ORACLE_SOURCE_SHA256, BASELINE_COMMIT, or the frozen source; causal check: a synthetic tree
         with `include_inspection=False` must make the re-pinned test fail; the three oracle guards
         must stay green.
       S2 replay truth: decide fixture story by evidence (the AT/4 story is the one consistent with the
         committed inspection block and the backend parity fixture); reconcile placements/board_delta/
         finalBoard/scores to one coherent story; update ReplayControls.test.ts:9 expectation. Pre-fix
         capture of the current red.
       S3 docstring + engines: judge/route.ts:11 lists Tier 2 as planned/not-implemented (or removes
         the pipeline tier listing); add engines to package.json (>=20.19) and align CONTRIBUTING.md:10
         or soften prose — small Cooperator decision on which.
     Route: R0 (tests/docs/metadata only; no executable path change); S1 additionally approval-gated
       because of the standing oracle rule.
     Dependencies: none external. Acceptance: pytest fully green; npm test = 1 failed (R2 only, declared
       carry); typecheck/lint/build green; S1 oracle-guard subset green and digest unchanged.

W-C  proxied-axes-lockout-correction                                      [bucket A]
     Objective: correct django-axes client-IP identity for the shipped nginx topology and prove two
       real peers never share a lockout bucket.
     In scope: backend/pyproject.toml (django-axes[ipware] extra), backend/config/settings.py axes
       block (AXES_IPWARE_META_PRECEDENCE_ORDER + right-most proxy order + AXES_IPWARE_PROXY_COUNT set
       together, per DEFECT_LEDGER.md:488-508 trap), the mandated regression test (simulated proxied
       request yields the real peer; two peers do not share a bucket), docker topology assertion.
     Out of scope: DRF NUM_PROXIES (already correct), host/R5, UI.
     Evidence basis: N6 (audit-04-F01/orch-05-D14).
     Slices: S1 implementation with pre-fix failure capture; S2 fresh independent re-audit (INFOSEC 15
       mandates re-audit for authN/authZ/crypto touches).
     Route: R3 during implementation + mandatory fresh independent re-audit; E3.
     Dependencies: none (repository-only); hard prerequisite for D2.
     Acceptance: regression test fails pre-fix/passes post-fix; re-audit verdict verified-closed;
       Cooperator informed (medium, sign-off for the residual already exists; closing it is recorded).

W-D  edge-observations-disposition                                        [bucket C]
     Objective: disposition every deployment-artifact observation carried from whole-18 with one
       Cooperator decision per item.
     In scope: L1 (one-line `proxy_hide_header X-Powered-By;` in the http block or frontend proxy
       locations + validator assertion + test_docker_deployment guard); L2 (decision among: Channels
       catch-all close route / nginx explicit non-matching `/ws` guard / accept as residual);
       L3 (decision among: accept / bounded backoff / log-rate-limit); R5 (keep accepted residual, or
       optional close-connection variant if the Cooperator wants it); L4 (record as accepted).
     Out of scope: product code outside deploy/ + backend routing as needed; D2 host work.
     Evidence basis: R5, L1, L2, L3, L4.
     Slices: S1 L1 deterministic fix + validator; S2 decision-first disposition of L2/L3/R5 (costed
       2-4 option packages); S3 any chosen corrections with regression guards.
     Route: R0/R1; L1 changes need the disposable-Docker validator run (Docker authority, no network).
     Dependencies: none. Acceptance: decisions recorded with sign-off where required; validator exit 0
       on the final artifact.

W-E  github-actions-ci-and-sbom                                            [bucket B/C, decision-gated]
     Objective: create the CI/SBOM pipeline the Cooperator chooses, gating the green suite with the
       R2 red explicitly allowlisted until D1.
     In scope: .github/workflows (ruff+mypy+pytest backend; eslint+tsc+vitest frontend; build), SBOM
       generation route, the R2-red allowlist decision, audit-02-F05 closure record.
     Out of scope: host deployment automation; changing gates themselves.
     Evidence basis: G6. Material Cooperator decision: what CI gates, SBOM tooling, and whether CI is
       even wanted pre-release (he may defer; audit-02-F05 sign-off exists).
     Route: R0 for workflow files; R3 dependency audit if SBOM tooling is added; network authority
       needed for SBOM tool pulls — the whole must carry it explicitly.
     Dependencies: W-A (license for CI checks) and W-B (green gates at CI creation).

W-F  test-breadth-and-baseline-disposition                                 [bucket B/C]
     Objective: run every opt-in suite once at a clean baseline and record each gap's disposition.
     In scope: postgres parity run (LIBRETILES_TEST_POSTGRES=1 against docker-compose.dev.yml Postgres —
       Docker authority required), the 18 slow/env-gated backend matrices (one run each), the live-probe
       naming (sentinel-gated, no provider call without explicit authority), Playwright e2e decision
       (recommended placement: inside D1, since UI polish is deferred — Cooperator decision).
     Out of scope: new tests beyond gap-closing; provider calls.
     Evidence basis: G11. Dependencies: W-B (clean baseline to compare against); W-E (CI wiring of any
       opt-in suite is a W-E follow-up).

W-G  i18n-catalog-second-opinion-review                                    [bucket B, decision-gated]
     Objective: produce second-opinion review evidence for the eight machine-authored catalogs or
       obtain an explicit disclose-and-ship decision.
     In scope: a structured review batch (Cooperator-executed, per PROJECT_CONTEXT decision-10 ceiling)
       or a Worker-structured diff of the eight catalogs against REVIEWED_LOCALES wording patterns,
       plus any Cooperator-approved wording corrections; update REVIEWED_LOCALES only with sign-off.
     Out of scope: the PARTIAL flag-table shape (stays by design); catalog key counts (enforced by tsc).
     Evidence basis: G3. Route: R0. Dependencies: none. Acceptance: per-catalog review verdicts
       recorded, or a signed disclose-and-ship residual.

W-H  dependency-posture-reverify                                           [bucket C, network-required]
     Objective: refresh the 2026-09-01 dependency posture against current advisories and lockfiles.
     In scope: npm audit + OSV.dev + poetry audit re-run (network authority explicit), npm lockfile
       drift check (`npm ci` in a disposable root), bump decisions only with route-A-style sign-off;
       the two tripwire tests (test_czech_minimum_length_validator_catalog_mismatch,
       test_drf_throttle_wait_suffix_stays_english) are expected casualties on bump (lesson 19).
     Out of scope: provider-catalog calls; adding dependencies beyond advisory-driven bumps.
     Evidence basis: G12 (backend lock verified consistent offline at 996d9c7; npm unverified).
     Dependencies: none; sequence last so the freshest posture precedes D2.

NOT wholes: G1, G2, N7 (roadmap); R2 (D1-owned pin decision); Stripe/LM Studio/Gateway/systemd (N1-N3,
permanent); the AP pin (P2).
```

## D4 — Priority buckets and recommended sequence

- **A (release blockers):** W-A license (a repo claiming MIT with no LICENSE file); W-B S1 parity re-pin (only medium open, carried through two closures); W-C axes correction (medium open in the only production topology).
- **B (pre-release quality/testing):** W-B S2/S3; W-E CI/SBOM (decision); W-G catalog review (decision); W-F postgres/slow matrix runs.
- **C (hygiene/tech debt):** W-D edge observations; W-F remaining decisions; W-H dependency reverify.
- **D (post-release operations):** catalog-refresh schedule, monitoring, backups — all under D2 (real-VPS), none here.

Ordering with reasons:
1. **W-B S1 before any later whole's acceptance**, because every green-gate claim since whole-17 has been conditional on the parity red; closing it restores honest full-gate evidence (Z).
2. **W-A before W-E** because CI license checks need the LICENSE file (X before Y because Y's gate content depends on X).
3. **W-B (all slices) before W-E/W-F** because CI/test-breadth baselines must be measured on a green gate set.
4. **W-C independent of W-B but sequenced before D2** (it is a D2 hard prerequisite; security routing keeps it separate from the hygiene whole).
5. **W-D before D2** (deployment-artifact hygiene the R5 host audit will want decided).
6. **W-H last** (freshest dependency posture immediately before deployment decisions).
7. **W-G anywhere pre-D1, but recommended before D1** (a review outcome may feed polish).

Recommended end-to-end sequence: W-A → W-B(S1→S2→S3) → W-C → W-E → W-F → W-D → W-G → W-H, then **stop before** D1 and D2.

## D5 — Deferred phases placement

Both deferred phases sit AFTER the sequence above:

- **UI/UX polish (deferred Cooperator phase D1)** — begins after W-B closes R3 (so its baseline has one declared red, the R2 pin, not three). Its first act is the **accessibility-pin decision** on R2 (product UX owns it; this triage places it, does not design it): whether "exactly one persistent announcer" is a product invariant (then `ReplayControls.tsx:19` and `SimulationArena.tsx:39` must route announcements through `LiveAnnouncer` or the sweep scope changes) or a game-surface-only rule (then the test scope narrows). D1 also carries the PRD-planned UI items measured in G10 (`libretiles_PRD.md:164-165,173`: move timeline, mobile bottom-sheet/pinch-zoom, AI thinking particles) and the Playwright e2e decision from W-F.
- **Real-VPS deployment (deferred Cooperator phase D2, `18/00/…/90_live-host-deployment-handout.md`, C1–C7 + R5 route)** — its concrete prerequisites produced by the wholes above: W-B green gates (a D2 acceptance run must not carry three reds); **W-C closed with the fresh re-audit** (the axes medium must not be deployed); W-D chosen dispositions (X-Powered-By, ws-500, watcher, port-80 residual recorded); W-H fresh dependency posture; W-E artifact provenance if chosen; W-A license present; and the R2 pin decided in D1 (R5 host audit reads the accessibility posture as accepted-residuals-with-sign-off, not as an unexplained red).

## D6 — Unknowns needing one bounded evidence probe each

1. **npm lockfile drift** — probe: `npm ci` into a disposable root + `npm ls` (needs network or cache authority). Unlocks: whether G12 has lockfile drift to fix. Network: yes → carried by W-H explicitly.
2. **Node 20.19+/22.12+ truth** — probe: run `npm ci`/build under Node 20 and 22 in disposable environments (network/nvm). Unlocks: engines-vs-prose decision in W-B S3. Network: yes → W-B S3 either softens prose (no network) or carries a bounded verification authority.
3. **Postgres parity suite result** — probe: `LIBRETILES_TEST_POSTGRES=1 pytest tests/test_postgres_dialect_parity.py` against `docker-compose.dev.yml` Postgres. Unlocks: W-F disposition and W-E CI wiring. Needs Docker authority, no network beyond local images.
4. **Slow-matrix runtimes/verdicts** — probe: one run of each env-gated backend matrix at a clean baseline. Unlocks: whether they belong in CI or stay manual. No network; time-cost only → W-F.
5. **L2 dynamic shape at HEAD** — already reproduced-dynamic in audit-05 (not unknown); what is missing is the Cooperator decision, not evidence. No probe needed.

## D7 — Recommended first successor whole and why

**W-B `codebase-hygiene-and-residual-reconciliation`, slice S1 first.** Rationale: highest priority open item (the only medium-severity residual, carried through two closures) × lowest external dependency (one backend test file, no network, no Docker, no provider) × highest measurable-evidence yield (restores the fully-green pytest gate that every subsequent whole's acceptance depends on), while the approval-gated evidence decision keeps the standing oracle protection (P3) intact — the re-pin touches only the payload literal at `test_word_authority_parity.py:1049`, never the frozen oracle, whose three guard tests and digest stay green. Expected first Worker exchange shape: a bounded backend test-file slice that re-pins the persisted-payload expectation to the canonical e2c2549 `inspection` payload, records provenance, proves the causal check (stripping inspection re-breaks it), and verifies the oracle guards and `ORACLE_SOURCE_SHA256` unchanged, with the exact edit pre-approved by the Orchestrator. I do not author that prompt.

---

Orchestration critique:
- MEASURED: seed path/line citations match the real tree (R1 :1049, R2 describe :829/assert :839, R3 :9, R4 judge/route.ts:11, L1 template:12, L3 entrypoint.sh:66, G1 architecture.md:258 + PRD:70-72, G3 i18n.test.ts:63, G4 both files, G5 no engines, G6 no .github, G7 settings.py:500-501) with two exceptions: G4's framing is wrong (measured disproven, D2) and the seed's pytest-skip "4" is the era-10 number (27 at baseline, carried from 07_report).
- MEASURED (scope gaps the seed missed, found by my widening): **N6 — the axes proxied-lockout medium (audit-04-F01/orch-05-D14) is open in the published Docker topology** (DRF half fixed by `docker-compose.yml:19`, axes half untouched at `settings.py:473-475`, no ipware, no regression test); **G12 — the repo has no LICENSE file despite README/PRD MIT claims**; and the R3 fixture's internal story drift (placements/board_delta vs words_formed).
- LEAD: none — every claim I make above is measured, or explicitly labelled carried-from-07_report.

Enumeration widened: the Orchestrator's partial sweep was widened to a repo-wide, case-insensitive marker sweep excluding .git/node_modules/.venv/.next/__pycache__/.ap/locks/binaries (zero code hits; dictionary-word noise only), a markdown prose sweep (9 hits, all classified), a pytest mark/skipif enumeration (79 django_db, 18 slow, 12 skipif, 6 postgres, plus per-file env gates), a vitest skip/gate enumeration (sentinel and skipIf-gated live/worker tests), a frontend-source `aria-live`/`role="status"` site enumeration (3/1), a repo-wide "Tier" scan, a public-asset reference scan, lockfile consistency (`poetry check --lock` exit 0, offline), and focused red-test re-runs for R1 (plus its 3 oracle guards), R2, and R3. Sites this prompt's commands could not reach: npm-lockfile drift and advisory freshness (network banned — routed to W-H), postgres parity and the disposable-Docker validator (Docker banned — routed to W-F/W-D), live provider probes (P7 — none run).

Report justification: new-evidence

Planning authority granted by exchange 01 expires at this terminal report. No implementation authority was granted and none is implied.

Smallest next step for the Orchestrator: reconcile this plan against repository evidence, present the costed successor-whole package to the Cooperator, and on approval close release-readiness-triage and issue the first successor implementation prompt (`codebase-hygiene-and-residual-reconciliation`, slice S1, approval-gated) with Native planning mode: not-used.

Context pressure: high-but-manageable — full mandatory reading set plus ~30 focused evidence commands consumed; no truncation affected any decision-critical output.
