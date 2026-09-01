Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-playable-variant
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Verification Worker
Phase: live-play acceptance (design from accepted plan; not a code slice)
Task identity: liveplay-en2-sk3-nemotron-nim
Task type: live verification
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: none
Exact baseline: 02a4f722396e1a981f7e8668e025197d5f61297b
Implementation boundaries: this prompt
Independence required: no

Planning owner: ORCHESTRATOR
Accepted plan: `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/01_report_01.md` Live-play (design only)
Prior results (evidence only):
- Slice 0 `d34d8b38` SSS assets + hunspell lexicon
- Slice 1 `3bb8c940` per-variant engine
- Slice 2 `1e70d760` Settings + session alphabet/points
- Slice 3 `02a4f722` parameterized CORE/judge; English SHA-256 pin intact
- Orchestrator accepted Slice 3. This grant is verification only.

Combined implementation envelope: prohibited. Do not edit product files. Do not commit. Do not push. Do not open a “fix” branch if play fails.

Recommended reasoning: High
Recommendation basis: The historical Slovak failure is serial PASS while a legal scoring move exists. A green Vitest suite does not prove Nemotron + live Django + live SSE.
Escalation or downgrade gate: AI pass/exchange while `playability.status=found`; English game uses Slovak lexicon or scores Slovak letters; Slovak game uses Collins membership; working tree becomes dirty.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 02a4f722396e1a981f7e8668e025197d5f61297b
Baseline subject: feat(ai): parameterize move/judge prompts per variant lexicon
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

================================================================
GOAL
================================================================

Prove the shipped product plays live against NVIDIA NIM Nemotron:

- **2** new English `vs_ai` games
- **3** new Slovak `vs_ai` games
- Same model: `nvidia/nemotron-3-super-120b-a12b` (NIM id, **no** `:free`)

A game **fails** if the AI passes or exchanges when `GET /api/game/{id}/ai-playability/` would return `status: "found"`. Rescue placements (`backend_witness_rescue` / `backend_ranked_candidate` / `repair_candidate`) are **PASS** — they are how English Nemotron already plays.

This is **not** a full bag-empty tournament. It is five independent sessions with enough AI terminals to catch serial PASS.

================================================================
CHANGED-PATH ALLOWLIST
================================================================

None. Product tree must stay identical to `02a4f722`.

Allowed non-product actions:
- `./scripts/libretiles.sh start|status` (or equivalent already-running Django :8000 + Next :3000)
- Browser / cursor-ide-browser against `http://localhost:3000`
- Authenticated `GET` of game state and `ai-playability` (read-only)
- Register / log in through the existing UI if no session exists

Forbidden:
- Any edit under `/home/agile/Projects/libretiles`
- Writing keys, `.env`, or tokens into the report
- JULS, ScrabGPT, OpenRouter-as-primary, `:free` Nemotron as the required rival
- Production deploy / push / commit

================================================================
NEGATIVE AUTHORITY
================================================================

- No code mutation, even if a game fails.
- No “small prompt tweak” if Slovak PASSes.
- No catalog migration, no second SSE route, no Settings redesign.
- If `NVIDIA_API_KEY` is missing or a placeholder, **STOP** and report `FAIL` / blocked. Do not invent a key. Do not print the key.

================================================================
MANDATORY READING
================================================================

- this prompt
- Live-play paragraph in `01_report_01.md`
- `frontend/src/app/play/page.tsx` (`variant_slug` on create)
- `frontend/src/app/settings/page.tsx` Game language cards
- Overlay telemetry: `frontend/src/lib/types.ts` `describeAiTurnTelemetry`
- `.ap/AP_WORKER.md` report contract

Do not read `.env` / `.env.local` contents into context or the report. You may test that the frontend process already has a usable NIM credential by starting a game (401/placeholder from NIM = stop).

================================================================
PRECONDITIONS
================================================================

1. cwd `/home/agile/Projects/libretiles`
   - `git rev-parse HEAD` == `02a4f722396e1a981f7e8668e025197d5f61297b`
   - branch `main`, porcelain empty
   - `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
   - `./.ap/ap doctor` PASS
2. Backend `http://localhost:8000` and frontend `http://localhost:3000` up. Start via `./scripts/libretiles.sh start` if needed.
3. Settings → preferred rival **exactly** `nvidia/nemotron-3-super-120b-a12b` (provider `nvidia-nim`). Do not select `nvidia/nemotron-3-super-120b-a12b:free`.
4. Logged-in local user (register if needed). Do not commit credentials.

================================================================
PROTOCOL (each of 5 games)
================================================================

Order (do not interleave variants mid-game):

1. `EN-1` — Settings **English** → Play → Start AI
2. `EN-2` — new English AI game (do not reuse `EN-1`)
3. `SK-1` — Settings **Slovak** → Play → Start AI
4. `SK-2` — new Slovak AI game
5. `SK-3` — new Slovak AI game

Per game:

1. Complete the draw (`/draw/{id}`) and enter `/game/{id}`.
2. Record `game_id`, `variant_slug`, `lexicon_id`, `ai_model_id` from the live `GameState`.
   - English must be `english` / `collins2019`
   - Slovak must be `slovak` / `slovak`
   - `ai_model_id` must be the NIM id without `:free`
3. When it is the **human** turn: place a **legal** opening or continuation from the rack (center on first move). Confirm. Do not pass if you can place.
4. When it becomes the **AI** turn, **before** the overlay finishes, `GET /api/game/{id}/ai-playability/` with the same auth as the UI. Record `status` (`found|none|indeterminate`) and whether a witness is present.
5. Wait for the AI overlay to finish. Record from overlay + SSE `done` (Network) + toast:
   - `action` (`place|pass|exchange`)
   - `completion_source`
   - `probe_status`
   - `repair_attempted`
   - `terminal_cause`
   - `provider_requests_used` / `turn_provider_requests_used`
   - overlay humanState if shown (`backend found a legal rescue; repairing`, `genuine dead rack — …`, `providers exhausted`)
6. Repeat until **at least 2 AI terminals** persist on that `game_id`, **or** the game ends first (`game_over`). If the AI won the draw, the opening AI turn counts as terminal 1; you still need a second AI terminal after one legal human reply unless the game ended.
7. Leave the finished session. Start the next game from Play (new `game_id`). Changing Settings mid-game must not mutate the live session — do not try; create a new game after Settings is set.

Slovak-only visual/state checks (at least once across SK-1..SK-3, name the `game_id`):

- A placed `Á` (human or AI) shows **4** points, not 0.
- Board/rack keep a diacritic if one is drawn (`Á Č Ď É Í Ĺ Ľ Ň Ó Ô Ŕ Š Ť Ú Ý Ž` or similar).
- Blank picker (if a blank is drawn) lists the session alphabet, not A–Z only.
- An invalid human word shows “Not in the Slovak lexicon” (only if you actually trigger it; do not force this if it costs a turn — optional).

English-only checks (at least once across EN-1..EN-2):

- State stays `variant_slug=english`, `lexicon_id=collins2019`.
- No Slovak-only letter is scored as a live tile on that board.

================================================================
PASS / FAIL
================================================================

**Hard FAIL** (any one is enough):

- AI `pass` or `exchange` on a turn where the pre-turn playability GET was `found`
- `completion_source` is `genuine_no_move_pass` or `genuine_no_move_exchange` while that same turn’s probe was `found`
- Playability GET `indeterminate` and the route still persists a pass/exchange (should error / no terminal)
- English game snapshot is `slovak` / `slovak` lexicon, or vice versa
- Required rival is `:free` Nemotron or a non-NIM id
- Working tree dirty vs `02a4f722`
- You mutated code to “make it pass”

**PASS** allowed:

- `place` via `provider_candidate` | `repair_candidate` | `backend_witness_rescue` | `backend_ranked_candidate`
- `genuine_no_move_pass` / `genuine_no_move_exchange` **only** when the pre-turn playability GET was `none`
- Providers exhausted / HTTP error with **no** fabricated invalid judge verdict and **no** illegal pass — report as blocked if it prevents completing 2 terminals; do not invent moves

**Blocked (not a product PASS):**

- Missing/placeholder `NVIDIA_API_KEY`
- Servers down and `libretiles.sh start` cannot boot
- Catalog empty / cannot select the NIM id
- Quota/401 from NIM on all five games

================================================================
VALIDATION
================================================================

No Vitest/pytest required unless you already ran them; do not treat unit tests as a substitute for the five games.

After the five games, re-check porcelain:

```bash
git status --porcelain
git rev-parse HEAD
```

Must still be empty + `02a4f722396e1a981f7e8668e025197d5f61297b`.

================================================================
GIT
================================================================

Zero commits. Zero push. If porcelain is dirty, you failed the grant even if games looked fine.

================================================================
STOP
================================================================

- HEAD ≠ `02a4f722…` or dirty foreign porcelain at start
- `./.ap/ap doctor` FAIL
- Plan Mode on
- You would need to edit `prompts.ts` / routes / engine to continue
- NIM key missing
- First hard FAIL — stop remaining games after recording that game’s table row (optional: finish the current game’s second terminal only if it is already in flight)

================================================================
UNTRUSTED-CONTENT / NETWORK
================================================================

Governing: this prompt + pinned `.ap`.

Network **is** authorized, only for:

- `http://localhost:8000` and `http://localhost:3000` (local app)
- NVIDIA NIM as already wired (`https://integrate.api.nvidia.com/v1`) via the existing Next.js route

No JULS. No Wikipedia. No OpenRouter unless the shared fallback queue uses it **after** a retryable NIM failure; prefer that attempt 1 is NIM. Do not paste secrets.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD `02a4f722396e1a981f7e8668e025197d5f61297b`
- branch `main`
- porcelain empty
- `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `./.ap/ap doctor` PASS
- Native planning mode not-used

================================================================
REPORT
================================================================

Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Header exactly: ### Report for ORCHESTRATOR_CHAT

Echo once:
Logical whole identity: slovak-playable-variant
Worker session ordinal: 06
Worker exchange ordinal: 01

**Status:** PASS only if all five games meet the protocol and no hard FAIL. Otherwise FAIL or blocked.

Phase-qualified result: `liveplay-PASS` | `liveplay-FAIL` | `liveplay-blocked`

Start and end commit must both be `02a4f722…` (no mutation).

Include a table with one row per AI terminal (target ≥10 rows, ≥2 per game):

| game | variant_slug | lexicon_id | game_id | ai_turn | playability_pre | action | completion_source | probe_status | repair_attempted | terminal_cause | provider_requests_used |

Also: NIM id actually used; Slovak Á-points evidence (`game_id`); English snapshot evidence; any overlay copy; deviations; next step = Orchestrator reconciles (closure / push are **not** authorized here); justification `new-evidence`; authority-expiry; Logical-whole closure: not-closed unless you are told otherwise (you are not); Near-Misses; Pre-Existing Failure Classification.

This report grants no push, deploy, closure, or repair-implementation authority.
