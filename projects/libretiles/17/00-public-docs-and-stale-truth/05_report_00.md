### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: public-docs-and-stale-truth
Worker session ordinal: 05, Worker exchange ordinal: 01
```

```text
status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: repository gate 5/5 exact (HEAD 4a718b5..., .ap 9c5cc44..., clean tree, main,
  origin readback equal); backend mypy clean (119 files), ruff clean, makemigrations --check
  "No changes detected", pytest 1 pre-existing parity red + 1227 passed + 1 skipped + 27
  deselected (slow/internet/postgres, stated below); frontend typecheck exit 0, lint exit 0;
  10/10 documentation guards green isolated (env flags correctly prefixed). Five
  confirmed-stale findings, all in docs/architecture.md, with exact D2 fixes.
Logical-whole closure: not-closed
Changed files and purpose: none — read-only audit; meta report is the authorized side effect
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: first isolated 10-test invocation collected 0 items
  because PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 / PYTHONDONTWRITEBYTECODE=1 were placed after the
  pytest argv and parsed as paths; rerun with them as env prefix → 10 passed. No other issues.
Pre-Existing Failure Classification: test_word_authority_parity.py parity (pre-existing)
```

Fresh Independent Audit annex:

```text
Audit scope: README.md, AGENTS.md, CONTRIBUTING.md, docs/architecture.md,
  backend/.env.example; libretiles_PRD.md cross-checked only; the 8 deployment guards +
  2 dictionary guards read to know their anchors.
Audit exclusions: product code, templates, live host, AP upgrade, docs/vps_deployment_guide.md
  prose itself (guard-pinned strings verified), .env / .env.local (never opened per A6).
Threat model: not-applicable (documentation truth, not security boundary)
Findings: D1 table + D2 fix proposals (D2 touches docs/architecture.md only)
Limitations: CONTRIBUTING Node "20.19+ or 22.12+" support matrix not verifiable offline
  (no engines field in frontend/package.json; Next docs not fetched — network authority);
  README/CONTRIBUTING "Poetry 2.3.2 or newer" verified only via the poetry.lock generator
  stamp, not a runtime readback.
```

## Repository gate

All five checks exact: `git rev-parse HEAD` = `4a718b5bcf68daed4c0b7ab43ab3261bf026fb10`;
`git rev-parse HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `git status
--porcelain=v1` empty; branch `main`; `git ls-remote origin refs/heads/main` = `4a718b5...`.

## D1 — Findings inventory

Verdict legend: `confirmed-stale` (CS) / `confirmed-correct` (CC) / `hypothesis-unverified` (HU).

| ID | File | Line(s) | Claim class | Current text (≤90 chars) | Verdict | Evidence |
|----|------|---------|-------------|--------------------------|---------|----------|
| F-01 | docs/architecture.md | 183 | Fallback cap | "…buildFallbackQueue, capped at five distinct pairs." | confirmed-stale | frontend/src/lib/ai-fallback.ts:17 `MAX_FALLBACK_ATTEMPTS = 3` (S1 re-verified) |
| F-02 | docs/architecture.md | 184 | Judge attempts/budget | "up to five sequential attempts … 10 seconds per attempt, 50 seconds overall." | confirmed-stale | frontend/src/app/api/ai/judge/route.ts:16-17 "at most three … 30s overall"; route.ts:41 `OVERALL_BUDGET_MS = 30_000` (S2 re-verified) |
| F-03 | docs/architecture.md | 181 | Catalog ordering | "Active direct rows precede the compatibility tail in their fixed canonical order." | confirmed-stale | backend/catalog/admin.py:294-305 `apply_reviewed_token` / "Reviewed catalog activation and fallback order were applied."; admin.py:397 "Review fallback order and activation"; contradicts architecture.md:188 itself (S3 re-verified) |
| F-04 | docs/architecture.md | 394 | Catalog ordering | "Selectable models begin with active exact direct rows in fixed order: Groq …" | confirmed-stale | same evidence as F-03; ordering is reviewed-admin-set, not immutable (widened hit) |
| F-05 | docs/architecture.md | 242-249, 258 | Tier 2 presented as live | "Tier 2: Online API (optional)" pipeline stage; prose omits that it is unimplemented | confirmed-stale | No Tier-2 implementation in backend (rg over backend/game*: zero hits); PRD:69 "Tier 2: Optional online dictionary assistance is planned and not implemented."; AGENTS.md:201 lists Tier 2 under "Not done yet" (widened hit) |
| F-06 | README.md / CONTRIBUTING.md / AGENTS.md | 11 / 104 / 152 | Fallback cap consistency | "at most three distinct pairs" / "capped at three distinct pairs" | confirmed-correct | ai-fallback.ts:17 = 3 |
| F-07 | AGENTS.md | 153 | Judge numbers | "up to three sequential attempts … 10 seconds … 30 seconds overall" | confirmed-correct | judge route.ts:40-41 |
| F-08 | docs/architecture.md | 183 | Defaults "120 seconds and 50 provider steps" | — | confirmed-correct | frontend/src/hooks/useGameStore.ts:248,250 (`aiTimeout: 120`, `aiMaxSteps: 50`) |
| F-09 | docs/architecture.md | 183 | "at least five steps reserved / failed lanes charge at least five" | — | confirmed-correct | ai-fallback.ts:19 `MIN_ATTEMPT_STEPS = 5`; :180-183 reservation; :319 `Math.max(reported, MIN_ATTEMPT_STEPS)` |
| F-10 | docs/architecture.md | 15, 394 | Direct priority order + exact ids | "Groq → Google Gemini → Cloudflare → Mistral → IBM" with 5 exact ids | confirmed-correct | backend/catalog/selection.py:29-66 (sort_order 1-5, ids exact) |
| F-11 | AGENTS.md | 35, 148 | "five-pair bootstrap (4 OpenRouter + 1 NIM)" | — | confirmed-correct | selection.py:106-112 `FREE_RIVAL_PAIRS` (4 openrouter + nvidia-nim) |
| F-12 | docs/architecture.md | 189 | Probe numbers 20s/22s/25s/4/60s | — | confirmed-correct | admin-provider-probe.ts:12 (20s), :11 (4 dispatches); probe-worker.mjs:106 (22s); provider_probes.py:34-35 (60s, 25s) |
| F-13 | README.md / PRD | 18 / 37 | "279,496 words", "thirteen assets" | — | confirmed-correct | english.json entry_count 279496; `validate_lexicons`: "13 asset(s) audited, 0 failed"; `ls backend/assets/dicts/` = 13 .txt (12 variant dicts + slovak_two_tile_words.txt) |
| F-14 | README.md | 20 | "eleven committed scripts" | — | confirmed-correct | `ls backend/scripts/build_*.py | wc -l` = 11 |
| F-15 | README.md / CONTRIBUTING.md / PRD | 187-188 / 9 / 37 | Toolchain versions (3.12 / >=3.11,<3.14 / Next 16 / React 19) | — | confirmed-correct | backend/pyproject.toml:10 `>=3.11,<3.14`; frontend/package.json next 16.3.4, react 19.2.4; poetry.lock "generated by Poetry 2.3.2" |
| F-16 | docs/architecture.md | 185 | Store default resolution | "valid server preference, then valid stored id, then catalog row 1" | confirmed-correct | model-catalog.ts:99-110 `resolveEligibleModelId` |
| F-17 | all five mission files | — | "0.0.0.0", "SOWPODS", bare "DEBUG=true" | none found | confirmed-correct (absence) | `rg` zero hits across the five files; 10/10 guards green |
| F-18 | README:189, architecture:40, CONTRIBUTING:137, AGENTS:198 | — | "Vercel" occurrences | library/historical mentions only | confirmed-correct | No venue claim patterns (guard `test_no_vercel_deployment_venue_claims` green); A3 preserved |
| F-19 | backend/.env.example | 16-94 | Variable defaults vs settings | DJANGO_DEBUG='true', tokens 15000/120, ws-ticket 10, flag false, CORS default | confirmed-correct | config/settings.py:296-298 (CORS default), :445, :452, :455-456, :460-462, :469-470 all match |
| F-20 | AGENTS.md | 7, 199 | "nine providers" / 12 locales/flags | — | confirmed-correct | provider-registry.ts `isKnownProvider` = openrouter + 8 exact = 9; LOCALES 12; 12 messages.*.ts; 12 locale flags under frontend/public/ |
| F-21 | CONTRIBUTING.md | 10 | Node "20.19+ or 22.12+" support matrix | — | hypothesis-unverified | No `engines` field in frontend/package.json; Next 16 support matrix not checkable offline |
| F-22 | PRD | 69, 84, 133, 146, 154, 164, 172 | "planned" statements (Tier 2, Playwright, GH Actions, mobile UX) | — | confirmed-correct | Roadmap statements, mutually consistent with AGENTS.md "Not done yet"; PRD was Slice-edited and is cross-check-only |

S1/S2/S3 from the handout §Hypothesis: all three re-verified and confirmed-stale (F-01, F-02,
F-03); F-04 and F-05 are new widened hits.

## D2 — Fix proposals (exact old→new)

All five fixes are inside `docs/architecture.md`. None is ambiguous; no
`NEEDS_ORCHESTRATOR_DECISION` items.

**F-01** (line 183) — reason: code cap is 3 (`ai-fallback.ts:17`); matches README/AGENTS/CONTRIBUTING.

- OLD: `- **Fallback**: Play and Judge call the same \`buildFallbackQueue\`, capped at five distinct pairs.`
- NEW: `- **Fallback**: Play and Judge call the same \`buildFallbackQueue\`, capped at three distinct pairs.`

**F-02** (line 184) — reason: judge budget is 3 attempts / 30 s (`judge/route.ts:17,41`); matches AGENTS.md:153.

- OLD: `- **Judge**: up to five sequential attempts, AI SDK \`maxRetries: 0\`, 10 seconds per attempt, 50 seconds overall.`
- NEW: `- **Judge**: up to three sequential attempts, AI SDK \`maxRetries: 0\`, 10 seconds per attempt, 30 seconds overall.`

**F-03** (line 181, sentence at end of the **Catalog activation** bullet) — reason: ordering is
set through the reviewed Admin workflow (admin.py:294-305, :397) and line 188 of the same file
already states this correctly; "fixed canonical order" contradicts both.

- OLD: `Seed/migration never flips an existing Admin kill switch. Active direct rows precede the compatibility tail in their fixed canonical order.`
- NEW: `Seed/migration never flips an existing Admin kill switch. Active direct rows precede the compatibility tail in the ordering set through the reviewed Django Admin workflow.`

**F-04** (line 394, first sentence) — reason: same reviewed-ordering truth as F-03; the five
seeded rows and their initial order are correct and stay.

- OLD: `- Selectable models begin with active exact direct rows in fixed order: Groq \`openai/gpt-oss-120b\`, Gemini \`gemini-3.7-flash\`, Cloudflare \`@cf/zai-org/glm-4.7-flash\`, Mistral \`mistral-small-2603\`, IBM \`ibm/granite-4-h-small\`.`
- NEW: `- Selectable models begin with active exact direct rows in seeded order, reviewable through the Django Admin ordering workflow: Groq \`openai/gpt-oss-120b\`, Gemini \`gemini-3.7-flash\`, Cloudflare \`@cf/zai-org/glm-4.7-flash\`, Mistral \`mistral-small-2603\`, IBM \`ibm/granite-4-h-small\`.`

**F-05** (line 258, prose below the pipeline diagram) — reason: Tier 2 is planned and not
implemented (PRD:69, AGENTS.md:201); today's pipeline is Tier 1 with advisory Tier 3. The
diagram's "optional" label may stay; this prose fix removes the implication that the stage is
live without touching ASCII box art.

- OLD: `Tier 1 covers the shipped Collins 2019 word list and handles nearly all cases. Tier 3 provides a fallback for edge cases using AI language understanding.`
- NEW: `Tier 1 covers the shipped Collins 2019 word list and handles nearly all cases. Tier 2 (an optional online API) is planned and not yet implemented; the live pipeline is Tier 1 with advisory Tier 3. Tier 3 provides a fallback for edge cases using AI language understanding.`

## D3 — Static-guard reconciliation

All ten guards stay green after D2. Checked against each anchor:

1. `test_no_documented_django_wildcard_bind` — scans architecture.md for `0.0.0.0:8000`; D2 adds none. GREEN.
2. `test_documented_backend_commands_use_loopback` — counts `runserver 127.0.0.1:8000` in README(2)/AGENTS(1)/CONTRIBUTING(1); architecture.md not counted; D2 touches neither. GREEN.
3. `test_backend_launch_scripts_use_loopback` — scripts only; untouched. GREEN.
4. `test_no_vercel_deployment_venue_claims` — D2 introduces no "Vercel" text. GREEN.
5. `test_authoritative_deployment_descriptions_are_present` — requires `"Vercel AI SDK"`? No — requires "self-hosted VPS"/"standalone"/"127.0.0.1:3000"/"nginx"/PRD phase-7 strings/settings CORS comment; D2 leaves all untouched. GREEN.
6. `test_prd_phase_seven_names_standalone_vps_deployment` — PRD untouched. GREEN.
7. `test_vercel_ai_sdk_library_references_are_preserved` — requires `"Vercel AI SDK"` present in PRD (≥2) and architecture.md; F-01..F-05 do not touch line 40 or any Vercel text. GREEN.
8. `test_throttle_prose_names_django_debug` — README/`.env.example` anchors untouched. GREEN.
9. `test_d1_prd_never_names_a_dictionary_the_product_does_not_ship` — PRD untouched. GREEN.
10. `test_d2_prd_word_count_equals_the_english_manifest_entry_count` — PRD untouched. GREEN.

No D2 change would affect any guard; no test edit is required (A4 satisfied without exception).

## D4 — Path allowlist + implementation gate sketch

Allowlist for the later implementation exchange (expected evidence tier E1):

```text
docs/architecture.md    (all five D2 fixes — the ONLY file D1 found stale)
```

No other mission file qualifies: README, AGENTS, CONTRIBUTING, backend/.env.example, and
libretiles_PRD.md produced zero confirmed-stale findings. The implementer must NOT touch
gamecore/game/accounts/catalog/views/models/migrations/serializers/player UX, nginx/systemd/
vps scripts, next.config, package.json, any test module, or the parity oracle.

Ordered implementation steps:

1. Repository gate (same five checks as this audit).
2. Verify OLD strings from D2 exist verbatim in docs/architecture.md (each exactly once; F-03's
   OLD sentence is unique to line 181 — assert single match before edit).
3. Apply the five edits exactly.
4. Focused 10-test run: from `backend/`, the exact isolated invocation used here
   (`env … PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/pytest
   tests/test_documentation_deployment_claims.py tests/test_documentation_dictionary_claims.py
   -c /dev/null -p no:cacheprovider`) → expect 10/10.
5. Standing gates once: mypy (clean), ruff (clean), makemigrations --check --dry-run ("No
   changes detected"), pytest (`not internet and not postgres and not slow` — expect only the
   pre-existing parity red), frontend `npm run typecheck` + `npm run lint` (exit 0).
6. `git diff --check` clean.
7. One commit (docs-only, message per repo style).
8. Pre-push verification, push, `git ls-remote` readback equals new HEAD.

## D5 — Residuals and out-of-scope

- **Parity red test (classified pre-existing)**: `backend/tests/test_word_authority_parity.py::PersistedPayloadParityTests::test_human_persisted_move_payload_matches_the_pinned_baseline`
  fails at line 1049 (persisted `words_formed` now carries an extra `inspection` block vs the
  pinned baseline). Unchanged by this whole: the five audit files are documentation; no slice
  touched game code; the test does not import any of them. Per A5, classify only — forward-horizon
  owner: Orchestrator (a future whole that pins or updates the baseline).
- **Out of this whole's file scope, with owners**:
  - `frontend/src/app/api/ai/judge/route.ts:10-12` docstring still lists "Tier 2: Online
    dictionary API (optional) — Django" as a pipeline tier — same Tier-2 truth as F-05, but
    frontend source is outside the docs allowlist (A1). Owner: a future frontend-docs/comment
    slice.
  - `frontend/public/hu.png` and `frontend/public/drevo.jpeg` are present but `hu` is not a
    shipped locale; not a documentation claim, no doc impact. Owner: future frontend asset
    hygiene slice.
  - CONTRIBUTING Node support matrix (F-21) — no action proposed; verification requires network.
    Owner: Orchestrator if a network-capable whole opens.
- **Explicit exclusions**: gamecore/game/accounts/catalog code, nginx/systemd/vps scripts,
  next.config/package.json, live host, AP upgrade, logical-whole closure (ORCHESTRATOR-only),
  all A5 carry residuals (IHR-S1-F01, IHR-S2-R01, HSTS W021, billing orphan, throttle scopes,
  JWT storage, CSP), and all A3-protected mentions.

## Gate run record (exactly what ran)

- `backend`: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` (3.12.12);
  `.venv/bin/mypy config game gamecore accounts catalog` → "Success: no issues found in 119
  source files"; `.venv/bin/ruff check .` → "All checks passed!";
  `.venv/bin/python manage.py makemigrations --check --dry-run` → "No changes detected";
  `.venv/bin/pytest -m "not internet and not postgres and not slow" -p no:cacheprovider`
  → 1 failed (parity, pre-existing), 1227 passed, 1 skipped, 27 deselected, 699 s.
  Slow/internet/postgres marks were deselected per the Slice-1/Slice-2 precedent.
- `frontend`: `npm run typecheck` → exit 0; `npm run lint` → exit 0. No build, no dev, no
  installs, no provider calls.
- Extra read-only evidence commands: `manage.py validate_lexicons` → "13 asset(s) audited,
  0 failed"; file reads and `rg`/`ls`/`sed` over the repository only.

## Orchestration critique

none (measured). The §Hypothesis S1/S2/S3 all verified accurate; the mission-file split in the
handout matched reality — docs/architecture.md held every stale claim found.

Enumeration widened:

- F-04: a second "fixed order" occurrence at architecture.md:394 (the handout only named :181
  and :394 for "fixed canonical"/"fixed order" — :394 confirmed and given its own D2 fix).
- F-05: the Word Validation Pipeline presents Tier 2 as a live stage without the "planned, not
  implemented" truth carried by PRD and AGENTS.md; prose fix proposed.
- Positive widenings recorded as confirmed-correct: F-08/F-09 (120 s / 50 steps / 5-step
  reservation and failed-lane charge), F-12 (probe timing numbers), F-13 ("thirteen assets"
  is real, not an off-by-one), F-19 (`.env.example` values all match settings defaults),
  F-20 (nine-provider and twelve-locale claims exact).

```text
Report justification: new-evidence
```

Authority expiry: this Worker exchange's read-only audit authority is fully spent upon
delivery of this report; no further repository access is authorized for this ordinal.

Smallest next step: Orchestrator issues the Slice-3 implementation exchange against the D4
allowlist (`docs/architecture.md` only), or resolves any D2 point it disagrees with before
doing so (none are flagged NEEDS_ORCHESTRATOR_DECISION).

Context pressure: comfortable — roughly one-third of visible context consumed; no truncation
risk encountered.
