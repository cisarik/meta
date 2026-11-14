# Planner — Jelena grass and ground-cover realism (`v006`)

Persistent role identity: WORKER
Logical whole identity: jelena-grass-and-ground-cover-realism
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: Planning
Task identity: JELENA-GRASS-AND-GROUND-COVER-REALISM-PLANNING
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — whole-scene grass clump/blade geometry, shader, distribution, lateral mask clearance, and 8 GB performance budgeting across an uncommitted 1.72M-instance live worktree state and the committed `c83e2ba` baseline.
Independence required: no

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and scene-grounded technical planning for realistic, varied grass and ground cover (~10x baseline density target where grass is eligible) in scene A of candidate Jelena_Realistic_v006.blend, including baseline/worktree reconciliation, clump/blade geometry, material/shader, access-mask lateral clearance, patch-first prototyping, 8 GB performance budget, evidence recipe, and narrow README update. Planning only; no implementation.
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

## 1. Goal and Accepted Constraints

Design one decision-complete, repository- and scene-grounded technical implementation plan for `Jelena/Jelena_Realistic_v006.blend` that achieves Michal's explicit artistic objective: **approximately 10× more grass where grass already exists, varied sizes, and substantially greater realism**, without damaging the accepted cabin, horizontal timber main walls, vertical-board gable, dark anthracite shingle roof, glossy glazing, terrace, furniture, steps, paved access paths A and B, dark gravel apron and parking, light forest road, trees, cameras, lighting, or scene B (`B • Zariadená dispozícia`).

Michal explicitly noted that the current grass spoils the impression of the visualization. Merely multiplying the existing upright rectangular/trapezoidal star strips (`Karta trávy A` and `Karta trávy B`) is inadequate and visually rejected. Quality of blade taper, gentle curvature/bend, clump structure, scale coherence in metres relative to the 60–70 mm pavers and 100 mm step riser, natural green root-to-tip variation, and clean path/gravel edge clearance matters as much as raw count.

Accepted boundaries that must not be reopened:

- **Trees**: tree silhouettes, floating foliage, and crown saturation remain explicitly deferred. Do not repair, move, or regenerate trees.
- **Hidden vegetation and stones**: preserve excluded collections `01a • Fasáda • pôvodné latky` (210 battens), `02a • Strecha • pôvodné falce` (38 ribs), `05a • Les • nahradené` (171 old vegetation objects including `Tráva • čistina`), `05b • Nášľap • ponechané` (20 stepping stones), `05c • Vegetácia • odstránená pre prístup` (`Smrek • stredný.021`, `Smrek • vysoký.015`, `Ker.003`), `06 • Terasa`, `07b • Svetlá exteriér`, `09 • Prototypy vegetácie`, and `10a • Vegetácia • mimo prístup` (`Papraď.005`, `Kameň • les.001`). Never create a new view layer that would accidentally un-exclude these collections.
- **Paving pattern artifacts**: triangular/pattern artifacts visible on curved paving are recorded as a deferred access-surface observation. Do not diagnose or edit paving geometry under the grass grant, and do not conceal paving with over-hanging grass.
- **Scripts**: do not run full entrypoints of `scripts/vegetation_scene_a.py`, `scripts/conifer_detail.py`, or `scripts/access_landscape_v005.py`. Plan a dedicated, idempotent grass-only script `scripts/grass_ground_cover_v006.py`.

Communication routing:

- Communicate with the Cooperator (Michal) in Slovak if direct user text is emitted outside the report; write the formal terminal report in English.
- Start the formal report with `### Report for ORCHESTRATOR_CHAT` on line 1.
- Use fish-compatible shell examples and verified Slovak Blender UI labels (`Súbor`, `Otvoriť`, `Uložiť ako...`, `Navrátiť`, `Prekreslenie → Render Image`).

## 2. Sources, Baseline, and Critical Worktree Revalidation Context

- **Repository identity**: `https://github.com/cisarik/jelena` at `/Users/agile/Projects/jelena`
- **Repository checkout topology**: standalone checkout with pinned submodule `.ap`
- **Expected branch and HEAD**: `main` at `c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e` (public `refs/heads/main` verified equal by Orchestrator on 2026-11-13)
- **Containing-repository `.ap` gitlink and `.ap` HEAD**: `d7023cf037f6d17885c3ede5c04812c61640da50` (`./.ap/ap doctor` PASS, variant `stable`)
- **Trace repository**: `https://github.com/cisarik/meta` at `/Users/agile/meta` (`HEAD` `2786ed5c911e5ef99bc7b56086e4edc8a6606d6c`)

### Critical Revalidation Fact — Committed `c83e2ba` vs Uncommitted Local Worktree (`followup_without_grant`)

The Orchestrator's read-only restoration established that `/Users/agile/Projects/jelena` has an uncommitted post-closure worktree state that **must be preserved untouched during planning**:

1. **Committed `c83e2ba` baseline** (in Git `HEAD` and preserved byte-for-byte on disk at `.local/checkpoints/Jelena_Realistic_v005-before-edge-grass.blend`):
   - `Jelena/Jelena_Realistic_v005.blend` SHA-256: `2399ce17ff1c332e7302bc5d623d687655eb2b72bc225fa2be88b0834583ddf8`.
   - `Pokryv lesa` has base density without the `14×` `Matematika.001` multiplier (`~122,895` instances of `Karta trávy A`/`B`).
2. **Uncommitted local worktree state** (currently on disk at `Jelena/Jelena_Realistic_v005.blend`, SHA-256 `892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4`, and currently open in live Blender with `is_dirty = false`):
   - Documented in working-tree `evidence/access-005/manifest.json` under `"followup_without_grant"` (`"not_committed": true`).
   - Extended `Cesta • les` to the terrain edges (`x: [-26.0, 35.65]`), rebuilt `Prechod • štrk` as `"junction": "solid-bay"` (`396` vertices), and inserted `Matematika.001` (`MULTIPLY` by `14.0`) into `Pokryv lesa` (`1,720,525` instances of the old 5-strip star cards `Karta trávy A`/`B`, random scale `0.35..1.90`).
   - Working-tree modified paths: `Jelena/Jelena_Realistic_v005.blend`, `evidence/access-005/overview.png`, `evidence/access-005/top-view.png`, `evidence/access-005/connection-detail.png`, `evidence/access-005/manifest.json`, `scripts/access_landscape_v005.py`.
   - Six untracked checkpoints in `.local/checkpoints/`: `Jelena_Realistic_v003-before-exterior.blend`, `Jelena_Realistic_v004-before-access.blend`, `Jelena_Realistic_v004-before-facade-cladding-correction.blend`, `Jelena_Realistic_v004-before-facade-correction.blend`, `Jelena_Realistic_v005-before-edge-grass.blend`, `Jelena_Realistic_v005-before-owner-correction.blend`.

Do **not** stop or report `BLOCKED` because of this known worktree diff, and do **not** revert, stage, or overwrite any worktree file. Classify it under RF-12 (`unrelated-owner-work` primary, `unpublished-candidate` secondary) and design the `v006` plan so that:

- Quantitative `1×` baseline vs `~10×` target is measured relative to the **pre-14× `v005` grass baseline** (`~122,895` instances of 5-strip cards = `~614,475` upright strip quads, where `Matematika.001` = 1.0 or absent), while also reporting the comparison against the rejected `14×` spike state (`1,720,525` instances).
- The plan supports building `Jelena/Jelena_Realistic_v006.blend` cleanly from whichever `v005` starting state Michal selects before execution:
  - **Option A (default if approved by Michal)**: start from the current worktree `v005` (`892d930b...`, keeping the terrain-edge road and `solid-bay` gravel junction) and remove/replace `Matematika.001` + old cards with the new `v006` grass system; or
  - **Option B**: start from the committed `c83e2ba` `v005` (`2399ce17...` via `.local/checkpoints/Jelena_Realistic_v005-before-edge-grass.blend`) and apply the new `v006` grass system.

## 3. Mandatory Reading

1. AP Worker spine: `/Users/agile/Projects/jelena/.ap/AP.md` (`Semantic Authority and Artifact Relationships`, `Per-Role Minimum-Reading Spine`, `RF-03`, `RF-04`, `RF-06`, `RF-08`, `RF-12`, `RF-18`, `RF-19`, `§8 Worker Responsibilities`, `§18 Stopping Conditions`); `/Users/agile/Projects/jelena/.ap/AP_WORKER.md` (`Worker Session Target`, `Reporting`); `/Users/agile/Projects/jelena/.ap/PROMPT_CONTRACTS.md` (`Worker Report Header`, `Planning Record`, `Plan-to-Execution Gate`, `Mutation Axes Record`, `Cooperator Delivery and Trace Destination Record`).
2. Project rules and docs: `/Users/agile/Projects/jelena/AGENTS.md`, `/Users/agile/Projects/jelena/README.md`.
3. Existing scripts (for read-only inspection of grass/mask structure only): `/Users/agile/Projects/jelena/scripts/access_landscape_v005.py`, `/Users/agile/Projects/jelena/scripts/vegetation_scene_a.py`.
4. Trace context: `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/00_handout_00.md`, `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/00_notes.md`, `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/00_trace_reconciliation.md`, and `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/02_closure.md`.

## 4. Authority, Execution Route, and Trace Persistence

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Trace project key: jelena
Trace logical-whole projection identity: jelena-grass-and-ground-cover-realism
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md
```

- **Execution route**: local read-only file/Git inspection in `/Users/agile/Projects/jelena` and `/Users/agile/meta`, plus bounded read-only MCP queries to the live Blender instance via `blender` (`get_addon_status`, `get_scene_info`, and strictly read-only `execute_blender_code` queries using `numpy`/`foreach_get` or aggregate node inspection). Never dump raw vertex arrays to chat.
- **Positive authority**:
  - Read-only inspection of `/Users/agile/Projects/jelena`, `.ap/`, `/Users/agile/meta/projects/jelena/00/`, and the live Blender session (`Jelena_Realistic_v005.blend`).
  - Direct creation of the complete terminal report at `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md` if and only if that file is absent, followed by full readback and SHA-256 verification.
- **Client completion route under `Native planning mode: required` (P4)**:
  - If your client's native Plan mode permits writing `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md` directly (or once the plan is finalized within this same unexpired grant without executing any implementation step), write the complete standard terminal report starting with `### Report for ORCHESTRATOR_CHAT` to that exact path and read it back.
  - If native Plan mode blocks writing `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md`, **do not** bypass the control, **do not** copy `00_handout_00.md` or `01_planning_00.md` to `01_report_00.md`, and **do not** start implementation. Instead, output the complete standard terminal report (beginning with `### Report for ORCHESTRATOR_CHAT` and containing the full plan) in the session output so the Orchestrator can persist it or issue the bounded report-completion exchange.
- **Commands**: read-only Git/file/hash/process checks (`git status`, `git rev-parse`, `git diff`, `shasum -a 256`, `ps`, `stat`, `rg`) and read-only Blender MCP inspection.
- **Git authority**: strictly read-only in Jelena, `.ap`, and Meta. No `git fetch`, `git add`, `git commit`, `git push`, `git checkout`, `git restore`, `git reset`, or `git clean`.
- **Dependency, network, browser, and secret authority**: none. Do not install packages (including Pillow), do not access the network, do not enable external asset libraries or generators, and do not read credentials.
- **Negative authority**: no Blender scene mutation, no modifier/node/material edit, no `Save` or `Save As`, no file reload, no rendering, no viewport screenshot that mutates state, no creation of `Jelena_Realistic_v006.blend` or `scripts/grass_ground_cover_v006.py`, and no edits to `00_handout_00.md`, `00_notes.md`, `00_trace_reconciliation.md`, or `00_RUN_MAP.md`.

## 5. Required Technical Plan Contents

Your report must distinguish **directly observed facts** from **engineering estimates** and cover:

1. **Live Scene & Grass Inventory**:
   - Exact readback of `Pôda • pokryv`, modifier `Pokryv lesa`, its Geometry Nodes graph (eligible area bounds, upward normal check, cabin/terrace keep-out boxes, 20 legacy stone disks, distance falloff `Rozsah mapovania` / `Matematika`, `Matematika.001` 14× multiplier in the worktree file, `Maska prístupu` raycast exclusion, instance pick/rotation/scale nodes).
   - Exact measurements of `Karta trávy A` and `Karta trávy B` (vertex/triangle counts, bounding boxes, why 5 flat vertical trapezoids read as rigid spikes), `Tráva • pokryv` shader nodes, and `Lesná pôda` shader nodes.
   - Verification of datablock users and Scene B (`B • Zariadená dispozícia`, 308 objects) isolation.
2. **Quantitative `10×` Target & Density Architecture**:
   - Explicit definition of `1×` baseline vs `~10×` target on the same eligible area:
     - Pre-14× `v005` baseline (`Matematika.001` absent / `1.0`): `~122,895` clump/card instances × `5` strips (`10` triangles) = `~614,475` strips (`~1,228,950` triangles).
     - Worktree `14×` spike state: `1,720,525` instances (`~8,602,625` strips, `~17.2M` triangles).
   - How `v006` achieves **~10× effective blade density** (e.g., `~5M–6.5M` rendered tapered blades across the eligible clearing, or a clearly justified instanced clump count × blades-per-clump product) with multi-blade clump prototypes so instance count stays practical for Blender depsgraph evaluation while rendered blade density and visual ground cover reach the ~10× target.
   - How distance/camera-frustum density gradation or layered clump scales (e.g., hero/mid/fill clumps) keep memory and render time well within the 8 GB machine's budget without thinning visible areas in Camera A, Overview (Camera D), or review cameras.
3. **Blade & Clump Geometry + Shader Realism**:
   - Exact procedural `bmesh` construction for new grass clump prototypes in a scene-A-only prototype collection (preserving `Karta trávy A`/`B` hidden and unedited for rollback safety):
     - Number of clump variants (e.g., short/dense tuft, medium arched clump, taller accent tuft), blades per clump, segments per blade (e.g., 3–4 vertical segments with quadratic bend/arch, taper to a fine tip, slight V-fold or normal curvature, varied azimuth/pitch/length/width).
     - Physical dimensions in metres coherent with the `60 mm` paver thickness, `70 mm` reveal, and `100 mm` terrace step riser (e.g., short base layer `45–85 mm`, main meadow/forest-clearing layer `90–160 mm`, sparse taller accents `170–230 mm`).
   - Patchy, natural distribution: how noise/clump modulation leaves subtle, irregular readings of `Lesná pôda` soil between richer tufts rather than a uniform green carpet or regular grid.
   - Upgraded grass material (`Tráva • pokryv • A` or updated scene-A-only material): root-to-tip colour/value gradient (darker earthy base, varied olive/forest-green mid-blade, warm sunlit tip), per-instance random hue/value variation via `Object Info -> Random`, appropriate roughness and subtle translucent/subsurface leaf response under existing sunny lighting without neon or plastic highlights.
4. **Access & Clearance Mask Strategy**:
   - Why root-point exclusion (`0.12 m` margin on `Maska prístupu`) still allowed bent/scaled blades to cross outer gravel edges.
   - Exact lateral-reach calculation: `max_clump_radius × max_xy_scale` (e.g., if a clump reaches `0.10–0.14 m` laterally at max scale, what mask margin or secondary edge-scale tapering is required at Path A, Path B, terrace steps, `Prechod • štrk`, `Parkovanie • štrk`, and `Cesta • les` so zero blades cross finished paving/gravel while avoiding an artificial bare moat).
   - Handling of the 20 legacy stepping-stone disk exclusions in `Pokryv lesa`: whether they should remain or be superseded by the actual Path A / Path B ribbon masks so old stone positions outside the shifted Path A do not leave round bald spots.
5. **Patch-First Prototyping, Performance Budget & Render Recipe**:
   - Step-by-step execution sequence for the later implementation grant:
     1. Pre-mutation verification and checkpoint `.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend`.
     2. `Save As` to `Jelena/Jelena_Realistic_v006.blend` (preserving `v005` and all prior `.blend` files byte-for-byte).
     3. Small representative patch test (including the Camera A terrace/path edge or path-to-gravel junction) to measure instance count, triangle count, render time, and sampled `ps` RSS before full-clearing rollout.
     4. Hard performance gates on this 8 GB Mac: sampled `ps` RSS working ceiling `<= 5.0 GiB` (simplify if sampled RSS exceeds `4.2 GiB`; pause/stop before `5.0 GiB`), single-still sequential renders (never batch 8 renders in one MCP call), and bounded `foreach_get` checks.
   - Exact matched before/after evidence package under `evidence/grass-006/`:
     - `camera-a-before.png` & `camera-a-after.png` (`840 × 560`, 32 samples, Cycles CPU, OIDN, AgX, frame 1)
     - `overview-before.png` & `overview-after.png` (`840 × 560`, 32 samples, Camera D)
     - `grass-detail-before.png` & `grass-detail-after.png` (dedicated scene-A review camera `J • Tráva • detail` or reproducible border crop showing blade taper, arch, root-to-tip shading, and path/step edge clearance)
     - `access-clearance.png` (from `G • Napojenie • detail` or `I • Chodník A • detail` if needed to prove gravel/paver margin cleanliness)
     - `manifest.json` (hashes, timings, sampled RSS in KiB with non-peak note, quantitative density table: clumps/m², blades/clump, total rendered blades, achieved ratio vs `1×` baseline, preservation readbacks).
6. **Changed-Path Allowlist, Narrow `README.md` Update, and Recovery**:
   - Exact allowlist for the later implementation grant (`Jelena/Jelena_Realistic_v006.blend`, `scripts/grass_ground_cover_v006.py`, `evidence/grass-006/**`, `README.md`, plus untracked local checkpoint `.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend` never staged).
   - Exact narrow `README.md` text update: identify `v005` as the accepted access baseline and `v006` as the grass candidate until owner acceptance.
   - Rollback procedure (`Súbor → Navrátiť` / checkpoint reload) and Slovak owner acceptance checklist preview.

## 6. Validation, Stopping Conditions, and Report Contract

```text
Evidence tier: E1
Evidence tier basis: read-only technical planning with direct trace report persistence
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: none — read-only planning exchange; script assertions are planned for the execution grant
Broad or full suite: not-used
Runtime or testbed: local Blender MCP read-only inspection
Independent acceptance: not-required
```

Stopping conditions:

- Stop and report `BLOCKED` if the live Blender file is not `Jelena_Realistic_v005.blend`, active scene is not `A • Chata pri lese`, Scene B does not have `308` objects, or MCP is unreachable after two bounded attempts.
- Stop if `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md` already exists.
- Do not mutate any repository file or Blender datablock.

Completion and report contract:

- Begin the report with `### Report for ORCHESTRATOR_CHAT` and echo the three coordinate fields (`Logical whole identity: jelena-grass-and-ground-cover-realism`, `Worker session ordinal: 01`, `Worker exchange ordinal: 01`) once.
- Include the compact core (`status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: not-applicable`, `Start commit` and `End commit` = `c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e`, `Report justification: new-evidence`, `Logical-whole closure: not-closed`), the `Planning Record`, the full technical plan (sections 1–6 above), `Orchestration critique` (`MEASURED` and `LEAD`), `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, and the `Authority expiry` statement.
- Persist the report to `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md` if permitted by the client, read back its full content, and return the status, path, and SHA-256 in a short completion notice.
- Authority expires upon submission of the terminal planning report.
