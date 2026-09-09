You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AFC-SLICE-5-IMPL — implement Model Analytics Dashboard & VPS Deployment Recommendation (/admin/analytics/ comparison matrix, win rates, spreads, provider authorship %, VPS deployment recommendation, navigation polish, Player 0/1 prompt difficulty sliders, prompt preview modal, and AI judge selection with ⚖️ explanation popup). Land one commit, push, and read back.
Phase: implementation
Exact baseline: f040a644f9f233234ba94ec6f2a620eebc933c39
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: reversible read-only analytics aggregation backend and frontend dashboard, navigation polish, and difficulty/judge UI enhancements. No database migration, no external network, no live provider call.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Implementing Slice 5 delivers the crowning features of the Admin Console for Michal's technical interview: the Model Analytics comparison matrix, VPS deployment recommendation, unified navigation across all 4 admin sections, and the Cooperator's interactive enhancements (prompt strength/difficulty sliders for Player 0 & 1, prompt preview inspection, and game judge selector: Dictionary vs AI Judge with ⚖️ explanation popup).

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:423-453 coordinate consistency and Worker Exchange Identity
AP.md:2453-2454      the CLOSED report-justification enum: `new-mutation`.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md                 the project brief.
/home/agile/Projects/libretiles/frontend/AGENTS.md        Next.js rules.
/home/agile/Projects/libretiles/backend/catalog/selection.py (get_selectable_models)
/home/agile/Projects/libretiles/backend/game/admin_urls.py
/home/agile/Projects/libretiles/frontend/src/app/admin/layout.tsx
/home/agile/Projects/libretiles/frontend/src/components/admin/SimulationSetupForm.tsx
/home/agile/Projects/libretiles/frontend/src/components/admin/ReplayScoreBreakdown.tsx
/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/09_report_00.md the approved technical plan
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be f040a644f9f233234ba94ec6f2a620eebc933c39
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these files:

Backend:
1. `backend/game/analytics.py`
2. `backend/game/analytics_expressions.py`
3. `backend/game/analytics_serializers.py`
4. `backend/game/analytics_views.py`
5. `backend/game/admin_urls.py`
6. `backend/game/simulations.py`
7. `backend/game/simulation_views.py`
8. `backend/game/simulation_serializers.py`
9. `backend/tests/test_admin_analytics_api.py`
10. `backend/tests/test_admin_analytics_aggregation.py`
11. `backend/tests/test_admin_simulation_api.py`

Frontend:
12. `frontend/src/app/admin/analytics/page.tsx`
13. `frontend/src/app/admin/layout.tsx`
14. `frontend/src/lib/api.ts`
15. `frontend/src/lib/types.ts`
16. `frontend/src/lib/admin-analytics.ts`
17. `frontend/src/lib/admin-analytics.test.ts`
18. `frontend/src/components/admin/AdminAnalyticsDashboard.tsx`
19. `frontend/src/components/admin/ModelAnalyticsTable.tsx`
20. `frontend/src/components/admin/PresetAnalyticsCards.tsx`
21. `frontend/src/components/admin/DeploymentRecommendationCard.tsx`
22. `frontend/src/components/admin/SimulationSetupForm.tsx`
23. `frontend/src/components/admin/SimulationSetupForm.test.ts`
24. `frontend/src/components/admin/PromptPreviewModal.tsx`
25. `frontend/src/components/admin/JudgeExplanationModal.tsx`
26. `frontend/src/components/admin/ReplayScoreBreakdown.tsx`
27. `frontend/src/components/admin/ReplayScoreBreakdown.test.ts`
28. `frontend/src/components/admin/AdminNavigation.tsx`
29. `frontend/src/components/admin/AdminNavigation.test.ts`
30. `frontend/src/components/admin/admin.module.css`

In addition, you have WRITE AUTHORITY to output your complete terminal report file to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/10_report_00.md`

⛔ Any mutation to any file outside this allowlist is strictly unauthorized.

## 3. Detailed Implementation Specifications

Follow the approved technical design from `09_report_00.md` and the Cooperator's interactive enhancements:

### 3.1 Backend: Analytics Aggregation API (`analytics.py`, `analytics_views.py`, `analytics_serializers.py`)

1. In `backend/game/analytics.py`:
   - Compute aggregation metrics across `GameSession`, `PlayerSlot`, `Move`, and `PlaygroundSimulation`:
     * Total games, finished games, total plies, variants breakdown.
     * Per model: games played, completed seats, wins, losses, draws, win rate %, avg score, avg spread differential, total moves, % `provider_candidate` authorship, avg attempt latency (ms), avg requests per turn.
     * Per preset: games played, completed seats, win rate %, avg score.
     * Recommendations derivation:
       - `current_flagship`: from `get_selectable_models()[0]`.
       - `primary_flagship`: top-ranked candidate by Wilson score lower bound / win rate / score.
       - `high_throughput_rival`: candidate with lowest average latency and high tool reliability.
       - `offline_cpu`: `engine/cpu` Master (zero provider requests).
       - `strategic_preset`: highest win-rate preset (e.g. `Grandmaster` or `Fast Search`).
2. In `backend/game/analytics_views.py`:
   - `AdminAnalyticsView`: `GET /api/admin/analytics/` supporting query filters `days` (default 30), `source` (`all`, `gameplay`, `playground`, `diagnostic`), `variant_slug`.
   - Headers: `Cache-Control: private, no-store`, `Vary: Authorization, Cookie`.
   - Permissions: `[IsAuthenticated, IsAdminUser]`.
3. Wire in `backend/game/admin_urls.py`:
   - `path("analytics/", AdminAnalyticsView.as_view(), name="admin-analytics")`

### 3.2 Frontend: Analytics Dashboard & Tables (`AdminAnalyticsDashboard.tsx`, `ModelAnalyticsTable.tsx`, `DeploymentRecommendationCard.tsx`)

1. `AdminAnalyticsDashboard.tsx`:
   - Overview stat cards: Total Games Played, Total Plies Replayed, Top Win-Rate Model, Average Score.
   - Filter bar: Period (`7d`, `30d`, `90d`, `All`), Source filter, Variant filter, and `[Refresh]` button.
2. `ModelAnalyticsTable.tsx`:
   - Sortable columns: Model Name & Provider, Games/Seats, Win Rate (with visual progress bar / badge), Avg Score, Avg Spread, Provider Authorship %, Latency ms, Requests/turn.
   - Distinct highlight for Flagship and CPU Master rows.
3. `PresetAnalyticsCards.tsx`:
   - Cards displaying performance comparison across the 4 strategic prompt presets (`Initial`, `Fast Search`, `Short Hooks`, `Grandmaster`).
4. `DeploymentRecommendationCard.tsx`:
   - Actionable VPS Deployment Recommendation banner for technical interviews:
     * **Primary Flagship**: Recommended free rival.
     * **High-Throughput Rival**: Lowest-latency challenger.
     * **Zero-Cost Offline Fallback**: Local Engine CPU Master (`engine/cpu`).
     * Rationale and reliability notes.

### 3.3 Cooperator Interactive Enhancements: Difficulty Sliders & AI Judge Selector (`SimulationSetupForm.tsx`, `PromptPreviewModal.tsx`, `JudgeExplanationModal.tsx`)

1. In `SimulationSetupForm.tsx`:
   - **Difficulty / Strength Slider for Player 0 and Player 1**:
     * Add an intuitive slider (`<input type="range" min={1} max={4} step={1} />`) with 4 labeled steps:
       - Level 1: `Initial` (Balanced beginner baseline)
       - Level 2: `Fast Search` (Speed & anchor mobility)
       - Level 3: `Short Hooks` (Defensive, hooks, leave balance)
       - Level 4: `Grandmaster` (Deep minimax, endgame tracking, rack equity centipoints)
     * Sliding the slider dynamically updates the selected prompt preset for that player seat!
     * Beside the slider, add a **`[👁 Preview Prompt]`** button!
   - **Prompt Preview Modal (`PromptPreviewModal.tsx`)**:
     * Clicking `[👁 Preview Prompt]` opens a clean modal showing the full instructions, strategic guidance, and core rules for the currently selected preset!
   - **Game Judge Selector**:
     * Add a Judge Selector radio / pill toggle:
       - `📖 Dictionary (Authoritative WordAuthority)` — deterministic backend lexicon lookup.
       - `⚖️ AI Judge (Live Model API)` — with model dropdown selector (selecting from eligible models).
     * Saved in `SimulationConfig` and sent in `createSimulation`.
2. In `ReplayScoreBreakdown.tsx` and `JudgeExplanationModal.tsx`:
   - For moves judged by AI Judge (or when AI Judge is enabled):
     * Render an interactive judge button with emoji: **`[⚖️ AI Judge verdict]`** on the formed words!
     * Clicking it opens `JudgeExplanationModal` displaying the judge's reasoning, lexicon recall rationale, and verdict details.

### 3.4 Navigation Polish (`AdminNavigation.tsx`, `admin/layout.tsx`)

1. `AdminNavigation.tsx`:
   - Replace "Preview" labels; all 4 sections are now fully live:
     * `[Games List]` (`/admin`)
     * `[Simulation Playground]` (`/admin/playground`)
     * `[Model Analytics]` (`/admin/analytics`)
     * `[Replay Studio]` (shows current game ID when on a replay page)
     * `[← Back to Game]` (`/play`)
   - Accessible `aria-current="page"` on the active section, clean gold/black styling.

## 4. Verification Commands

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_admin_analytics_api.py tests/test_admin_analytics_aggregation.py -v
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/lib/admin-analytics.test.ts src/components/admin/AdminNavigation.test.ts src/components/admin/SimulationSetupForm.test.ts src/components/admin/ReplayScoreBreakdown.test.ts
```

⛔ Do NOT run package installers (`npm install`, `poetry add`, etc.).

## 5. Git Commit and Push Sequence

Stage ONLY allowlisted files by explicit paths:
```bash
git add backend/game/analytics.py backend/game/analytics_expressions.py backend/game/analytics_serializers.py backend/game/analytics_views.py backend/game/admin_urls.py backend/game/simulations.py backend/game/simulation_views.py backend/game/simulation_serializers.py backend/tests/test_admin_analytics_api.py backend/tests/test_admin_analytics_aggregation.py backend/tests/test_admin_simulation_api.py frontend/src/app/admin/analytics/page.tsx frontend/src/app/admin/layout.tsx frontend/src/lib/api.ts frontend/src/lib/types.ts frontend/src/lib/admin-analytics.ts frontend/src/lib/admin-analytics.test.ts frontend/src/components/admin/AdminAnalyticsDashboard.tsx frontend/src/components/admin/ModelAnalyticsTable.tsx frontend/src/components/admin/PresetAnalyticsCards.tsx frontend/src/components/admin/DeploymentRecommendationCard.tsx frontend/src/components/admin/SimulationSetupForm.tsx frontend/src/components/admin/SimulationSetupForm.test.ts frontend/src/components/admin/PromptPreviewModal.tsx frontend/src/components/admin/JudgeExplanationModal.tsx frontend/src/components/admin/ReplayScoreBreakdown.tsx frontend/src/components/admin/ReplayScoreBreakdown.test.ts frontend/src/components/admin/AdminNavigation.tsx frontend/src/components/admin/AdminNavigation.test.ts frontend/src/components/admin/admin.module.css
git diff --staged --stat
```

Commit with message:
```bash
git commit -m "feat(admin): implement model analytics dashboard, difficulty sliders, and judge inspection"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "f040a644f9f233234ba94ec6f2a620eebc933c39"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Any test or gate failure cannot be resolved within the allowlisted files.
- Pre-push verification reveals that `origin/main` has diverged from the baseline.

## 7. Report Contract

IMPORTANT: Write your complete terminal report directly to:
`/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/10_report_00.md`

The report content must begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 10, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `f040a644f9f233234ba94ec6f2a620eebc933c39`
- End commit: `<exact SHA>`
- Changed files and purpose
- Tests and validation summaries (verbatim tool outputs)
- Commit and push result (SHA and readback check)
- Deviations, risks, or missing evidence: none | <details>
- One smallest next step
- Report justification: `new-mutation`
- Explicit authority-expiry statement

Plus the two analytical fields:
```text
Orchestration critique: none | <findings> (labelled MEASURED and LEAD)
Enumeration widened: none | <surfaces not reached>
```

In your final chat message, emit a concise 3-line notification confirming that the report has been written to disk at `/home/agile/meta/projects/libretiles/15/00-admin-frontend-console/10_report_00.md`.
