Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice U only (Unicode SSE placement normalize)
Task identity: slice-u-unicode-sse-placement-normalize
Task type: bugfix implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: 02a4f722396e1a981f7e8668e025197d5f61297b
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: not-used — Slice U repair shape is already specified in `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/07_diagnosis_00.md` Defect A. AP RF-04: no remaining architecture uncertainty for this slice. Do not plan. Do not open Plan Mode.
Implementation in same Worker session: this IS the implementation session (fresh)
Planning stop event: not-used
Execution authority event: this prompt (Native planning mode: not-used)
Post-plan implementation session: this session
Combined implementation envelope: prohibited — implement exactly Slice U. Not lexicon. Not JULS. Not live-play protocol.

Prior Worker session 01 exchange 01: research BLOCKED on dirty porcelain (`01_report_00.md`). That report grants nothing. Porcelain is now empty; do not re-run research.

Continuity (evidence only, not your authority):
- Live-play FAIL: `05/00-slovak-playable-variant/06_report_00.md` (SK-2 `stale_witness` on OSĽAŤA)
- Diagnosis: `07_diagnosis_00.md` Defect A
- Cooperator (2026-08-30): deleted untracked `slovak_no_license.txt`; parked JULS and lexicon; asked to unstick via the known code bug

Recommended reasoning: Medium
Recommendation basis: localized regex + NFC + existing Vitest route suite. Named risk is English ranked-rescue regression, covered by stay-green tests, not by Extra High reasoning.
Escalation or downgrade gate: stop BLOCKED if English A–Z rescue tests go red, if CORE hash/version would need to change, if a second SSE route seems required, or if a path outside the allowlist seems required.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

External trace disposition: not-used

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 02a4f722396e1a981f7e8668e025197d5f61297b
Baseline subject: feat(ai): parameterize move/judge prompts per variant lexicon
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: local main ahead 4. Do not push. Do not treat GitHub main as HEAD.

================================================================
GOAL (one primary outcome)
================================================================

Slovak diacritic placements survive the Next.js SSE normalize path the same way English A–Z already does.

After this commit:

- `normalizePlacementData` accepts one NFC Unicode letter or `?`.
- `blank_as` accepts one NFC Unicode letter (not A–Z only).
- `normalizeRankedChoices` no longer drops a whole candidate solely because a placement letter is `Ľ` / `Ť` / `Á`.
- A playability witness with `?` as `Ľ` and letter `Ť` is not stripped to empty → no `stale_witness` from ASCII filter.
- English A–Z ranked rescue and existing `route.test.ts` cases stay green.
- `MOVE_PROMPT_VERSION` remains `pfr-s2-core-1`.
- English CORE SHA-256 remains `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`.
- Hunspell `slovak.txt` is untouched. OU/AM can still score. That is an accepted residual of this slice, not a fail.

This is Defect A only. It is why English rescue looks brilliant and Slovak rescue looks random or crashes.

================================================================
CHANGED-PATH ALLOWLIST (nothing else may change)
================================================================

Existing:
- frontend/src/app/api/ai/move/route.ts
- frontend/src/app/api/ai/move/route.test.ts

If git add would include any other path, stop and report BLOCKED.
Do not “while we’re here” edit `prompts.ts`, judge route, Django, or AGENTS.md.

================================================================
NEGATIVE AUTHORITY
================================================================

- No `backend/` files. No `slovak.txt`. No lexicon filter. No 2-letter allowlist.
- No JULS. No httpx scrape of slovnik.juls.savba.sk. No ScrabGPT import.
- No `sk.sorted.txt` / `slovak_no_license.txt` (deleted; do not recreate).
- No second `/api/ai/move` route. No CORE / version bump. No catalog migration.
- No LM Studio. No paid models. No Stripe. No production. No push.
- No live provider inference. No `.env` reads.
- No chrome i18n. No tile-bag change. No CH tile.
- No git fetch/switch/stash/clean. One local commit only, after tests pass.

================================================================
MANDATORY READING (deep)
================================================================

- this prompt
- frontend/src/app/api/ai/move/route.ts — `placementSchema` (~113), `normalizePlacementData` (~276), `normalizePlacementArray`, `normalizeRankedChoices` (drops candidate when `placements.length !== raw.placements.length`), witness rescue ~1138
- frontend/src/app/api/ai/move/route.test.ts — `rankedPayload`, `WITNESS`, “falls through a stale ranked candidate to the old playability witness”
- /home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/07_diagnosis_00.md Defect A
- /home/agile/Projects/libretiles/.ap/AP.md, .ap/AP_WORKER.md, .ap/PROMPT_CONTRACTS.md (Implementation Authority + standard report)

Do not read `.env` / `.env.local`.
Do not read scrabgpt / scrabgpt_sk.

================================================================
REPAIR SHAPE
================================================================

In `normalizePlacementData`:

1. If `letter` / `blank_as` are strings, NFC-normalize then trim then uppercase (`letter.normalize("NFC")` before length/regex). Combining marks must not sneak through as length>1.
2. Letter must match `/^[\p{L}?]$/u` (one Unicode letter or `?`). Not `/^[A-Z?]$/`.
3. If letter is `?`, `blank_as` must match `/^\p{L}$/u`. Not `/^[A-Z]$/`.
4. Keep 15×15 integer bounds and the existing `letter !== "?" && blankAs !== null` reject.
5. Still reject digits, emoji, empty, multi-character strings after NFC.
6. Update `placementSchema` **description** so the tool text does not say “A-Z only”. Do not change English CORE bytes. Zod `.length(1)` may remain if NFC guarantees one char; if a test needs `.min(1)` after NFC, keep it strict (exactly one letter).

`toUpperCase()` is correct for `ľ` → `Ľ`. The bug is the ASCII regex, not casing.

Do not invent a session-alphabet allowlist in this slice unless you can do it with data already on the request context **without** new backend fields. Prefer `\p{L}`. Backend already rejects letters outside the variant alphabet on persist.

================================================================
TESTS (required)
================================================================

Add in `route.test.ts` (same helpers: `rankedPayload`, `mockBackend`, `runRoute`):

1. **Ranked diacritic candidate survives.** Ranked payload placements include `Ľ` and `Á` (and/or `Ť`). Expect `completion_source === "backend_ranked_candidate"` and the POST `/ai-move/` body to still contain those letters (not stripped).
2. **Diacritic witness rescue.** Playability witness like SK-2: at least one `letter: "?"` with `blank_as: "Ľ"` and one `letter: "Ť"`. Ranked path stale or unused as needed so witness rescue runs. Expect `completion_source === "backend_witness_rescue"`, **not** SSE error `stale_witness` / empty witness. English `WITNESS` RATE fixture must still pass.
3. **Negative:** a placement letter `"1"` or `"😀"` is still dropped / candidate skipped.

Stay green: existing English ranked + witness tests in this file.

Commands (cwd `frontend/`):

```bash
npx vitest run src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts
```

`prompts.test.ts` is the CORE hash/version pin — must still pass without editing `prompts.ts`.

================================================================
GIT
================================================================

Git authority: **one** local commit after tests pass. No push. No `--no-verify`. No amend. No `git add .`.

Stage only the two allowlisted files.

Subject:

```text
fix(ai): accept Unicode letters in move placement normalize
```

Body: one or two sentences on SK-2 `stale_witness` / ranked drop. Do not claim SSS lexicon quality.

================================================================
REPOSITORY GATE (before mutation)
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD equals `02a4f722396e1a981f7e8668e025197d5f61297b`
- branch `main`
- `git status --porcelain` empty
- `HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native Plan Mode **off**

If dirty or HEAD moved: BLOCKED, no edits.

Independently confirm `/^[A-Z?]$/` is still in `normalizePlacementData` before patching.

Capability handshake: abbreviated. Plan Mode off. Do not probe keys.

Cursor AppImage: if you need Python, wrap `env -u APPIMAGE -u ARGV0 -u APPDIR`. This slice should not need Python.

================================================================
EVIDENCE / VALIDATION
================================================================

Evidence tier: E2 for this slice (targeted Vitest + inspect diff). No Django pytest required. No live NIM. No browser annex.

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure.
- English route tests red.
- CORE hash or `MOVE_PROMPT_VERSION` change.
- Second SSE route.
- JULS / lexicon / backend edits.
- Second commit or push.
- Plan Mode on.

================================================================
COMPLETION AND REPORT
================================================================

Status PASS only if: allowlisted diff + tests named above pass + one local commit + no push + English CORE pin unchanged.
PARTIAL if tests pass but commit was not made because of a named git blocker.
BLOCKED on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-blocked`

Report justification: `new-mutation`

Logical-whole closure: `not-closed`

Standard terminal report begins exactly:

### Report for ORCHESTRATOR_CHAT

Then exactly once:
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 02
Worker exchange ordinal: 01

Then: status; phase-qualified result; start commit (baseline) and end commit (new SHA); changed files; vitest evidence; commit result (SHA + subject); push: not authorized / not performed; deviations; one smallest next step (expected: Orchestrator tells Michal Slice U is in; OU/AM residual remains; live-play later; no JULS); authority-expiry; Logical-whole closure: not-closed; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification.

Optional: copy the same report to `/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/02_report_00.md` (meta only, no git).

Authority expires with the terminal report. Retained context is not a renewal.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
