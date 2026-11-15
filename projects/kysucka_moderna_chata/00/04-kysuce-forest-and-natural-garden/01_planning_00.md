# Plan Kysuce forest and natural garden environment pass (v04)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-kysuce-forest-and-natural-garden
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BLENDER-MCP-KYSUCE-FOREST-AND-NATURAL-GARDEN-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded technical planning for Kysuce hills/forest, near spruces, orchard apple tree, natural front planting, LOD/instance budget, and v04 source-replay synchronization using established Orchestrator MCP grounding
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: concise repository- and live-MCP-grounded technical plan specifying (1) asset availability, acquisition/import strategy, and license/manifest tracking, (2) projected background ridge/forest and near-spruce/orchard/front-planting 3D layout, (3) LOD, collection/mesh instancing, and memory/triangle budget (< 3M unique source triangles, < 90 MiB per tracked file), and (4) exact mutation paths, deterministic scripts/landscape_v04.py hook, semantic source-replay tolerances, and matched 1448x1086 OIDN render acceptance for v04
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

## Goal and Context

Produce a concise, decision-complete technical implementation plan for the logical whole `kysucka-moderna-chata-kysuce-forest-and-natural-garden`.

Accepted Cooperator and project decisions:
- Starting from the accepted `v03` working scene (`blender/kysucka_chata_mcp_v03.blend` at commit `623d12abe0c0eb2742cd02c9962c1712b53437e2`) and keeping its selected camera (`CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35 mm`, `sensor_width = 36 mm`, `shift_x = 0.0`, `shift_y = 0.105`, `clip_end = 500.0`) strictly locked, replace the empty horizon and geometric proxy vegetation with a coherent, realistic **Kysuce setting: rolling forested hills, nearby smaller spruces, an apple-bearing orchard tree in the left garden, and natural front planting** in `blender/kysucka_chata_mcp_v04.blend`, synchronized with `model/parameters.json`, `scripts/landscape_v04.py`, and `scripts/build_scene.py`.
- Preserve `v03` exterior timber and foreground rustic fence (`scripts/timber_fence_v03.py`), building envelope/roof/openings, interior furniture/partitions, chimney/fireplace, paving/steps/bollards, world/lights, glass, reference image, CAD/PDF, and S00/v01/v02/v03 files untouched.
- Communicate with the Cooperator in Slovak if addressing him directly; write your formal Worker report in English starting with `### Report for ORCHESTRATOR_CHAT`.
- **Important anti-stall constraint**: Do **not** print, quote, propose, or reproduce the project's literal Orchestrator-owned closure signal anywhere in your plan or report. Keep the managed AP block and the entire `Closure and Git gates` section of `AGENTS.md` untouched. Do not redesign the workflow or copy the handout into a giant report.

## Repository and Environment Prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Baseline: `623d12abe0c0eb2742cd02c9962c1712b53437e2` (`feat: add PBR exterior timber and reposition foreground rustic fence in v03`)
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap` (pinned submodule checkout; detached HEAD equal to gitlink accepted)
Trace repository: `https://github.com/cisarik/meta` at `/Users/agile/meta` (HEAD `a46e62d7a1876bc04e5af5e7c139d9a9f40d793f`; preserve all unrelated work and predecessor files untouched)

Mandatory reading:
- `.ap/AP.md` (Semantic Authority and WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-04, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#planning-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`, `model/parameters.json`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/01_closure.md`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/00_handout.md` and `00_notes.md`

## Established Orchestrator MCP, Projective Geometry, and Asset Grounding (Reuse Directly)

The Orchestrator has already verified the repository baseline (`623d12abe0c0eb2742cd02c9962c1712b53437e2`), `./.ap/ap doctor` (`PASS`), all protected S00, v01, v02, and v03 SHA-256 hashes, the live Blender 5.2.3 LTS session via MCP, 3D-to-camera-UV ridge/garden projections, and the Poly Haven / Sketchfab APIs:

1. **Live Blender 5.2.3 LTS state**:
   - Open file: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v03.blend` (`is_saved: True`, `is_dirty: False`, `is_job_running('RENDER'): False`, `mode: OBJECT`, `656` objects).
   - Locked camera `CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35.0` mm, `sensor_width = 36.0` mm, `shift_x = 0.0`, `shift_y = 0.105`, `clip_end = 500.0`.
   - Note on `look`: the active Layout viewport is in `RENDERED` shading with Cycles; if calling `look(mode="camera")`, pass `shading="solid"` (or `image=...`) so it does not fail on Cycles viewport capture.
2. **Projective 3D-to-camera-UV (`u = x/width` left-to-right, `v = y/height` top-to-bottom) facts**:
   - Camera forward direction in XY is `(-0.7208, +0.6931, 0.0)` (looking toward **negative X and positive Y**).
   - `SITE_terrain_proxy` (`x ∈ [-45, +65], y ∈ [-18, +104.4], z ∈ [-1.35, +11.24]`, flat `z = -0.055 m` for `Y < 12 m`) ends at `X = -45 m` and only rises for `Y > 12 m`. Consequently, for `u ∈ [0.00, 0.40]` its skyline sits at `v = 0.659..0.589` (`Z = 0.3..3.8 m`), and for `u ∈ [0.40, 0.65]` it stays hidden behind the house roof (`roof_ridge_left` at `u = 0.3093, v = 0.3277`, `roof_ridge_right` at `u = 0.8802, v = 0.0881`, `roof_eave_front_left` at `u = 0.1202, v = 0.5730`).
   - **Exact world `(X, Y, Z)` coordinates that project into the required Kysuce skyline band (`u = 0.00–0.65, v = 0.15–0.55`)**:
     - **Layer 1 (`D ≈ 70 m`, nearer wooded slope / meadow clearings)**:
       `u = 0.00, v = 0.20 -> (-42.70, 9.21, 21.48)`; `u = 0.15, v = 0.22 -> (-39.63, 17.32, 21.66)`; `u = 0.30, v = 0.24 -> (-35.17, 25.76, 21.50)`; `u = 0.45, v = 0.21 -> (-28.70, 33.54, 23.26)`; `u = 0.60, v = 0.23 -> (-21.64, 40.96, 22.26)`.
     - **Layer 2 (`D ≈ 110 m`, main rolling forested ridge)**:
       `u = 0.00, v = 0.20 -> (-79.39, 20.19, 33.04)`; `u = 0.15, v = 0.22 -> (-74.56, 32.93, 33.33)`; `u = 0.30, v = 0.24 -> (-67.55, 46.19, 33.07)`; `u = 0.45, v = 0.21 -> (-57.39, 58.41, 35.84)`; `u = 0.60, v = 0.23 -> (-46.30, 70.08, 34.26)`.
     - **Layer 3 (`D ≈ 160 m`, distant ridge, well inside `clip_end = 500 m`)**:
       `u = 0.00, v = 0.20 -> (-125.24, 33.92, 47.49)` through `u = 0.60, v = 0.23 -> (-77.12, 106.49, 49.27)`.
     - **Right-side hillside / mid-ground beyond glazed gable (`u = 0.90–1.00, v = 0.35–0.70`, `gable_right_corner` at `u = 0.9538, v = 0.6980`)**:
       At `D = 25 m`, `u = 0.98, v = 0.55 -> (13.03, 13.47, 2.80)`; at `D = 40 m`, `u = 0.92, v = 0.45 -> (6.16, 26.56, 6.58)`.
   - **Near-ground preservation**: Keep `SITE_terrain_proxy` near-ground heights (`Z = -0.055 m` supporting the house, path, steps, and `v03` fence) untouched; create dedicated background hill mesh layers (e.g. `LANDSCAPE_hills_v04` in `70_SITE` or `95_LANDSCAPE_V04`) and upgrade visible ground/lawn/soil shaders and edge grass tufts without altering near-ground vertex heights.
   - **Existing proxy objects in `90_VEGETATION_PROXY` (`263` objects) to replace/hide deterministically**:
     `SHRUB_proxy*` (`19`), `FLOWER_proxy*` (`7`), `TREE_trunk_proxy*` (`38`), `CONIFER_proxy*` (`152`), `APPLE_trunk_proxy` (`1`), `APPLE_branch_proxy*` (`23`), `APPLE_foliage_proxy*` (`23`).
3. **Asset acquisition targets and verified access**:
   - **Poly Haven CC0 (`https://polyhaven.com/license`) — direct unauthenticated HTTP download verified via `api.polyhaven.com/files/<id>`**:
     - `food_apple_01` (`https://polyhaven.com/a/food_apple_01`): `food_apple_01_1k.blend` (`445,545` B) / `.gltf` + 1K JPG maps (`diff`, `rough`, `nor_gl`).
     - `grass_medium_01` (`https://polyhaven.com/a/grass_medium_01`): `grass_medium_01_1k.blend` (`1,832,028` B) / `2k` + 1K/2K maps (`diff`, `alpha`, `nor_gl`, `rough`). Import selected tuft/clump meshes, not the high-density demo scatter plane.
     - `shrub_01` (`https://polyhaven.com/a/shrub_01`): `shrub_01_1k.blend` (`6,535,174` B) / `2k` + 1K/2K maps (`diff`, `alpha`, `nor_gl`, `rough`). Import selected low-growth clumps.
     - `periwinkle_plant` (`https://polyhaven.com/a/periwinkle_plant`): `periwinkle_plant_1k.blend` (`1,680,482` B) / `2k` + 1K/2K maps (`diff`, `opacity`, `translucency`, `nor_gl`, `rough`). Import selected flowering clumps/LODs.
   - **Sketchfab CC-BY-4.0 (`https://creativecommons.org/licenses/by/4.0/`) — metadata verified via `api.sketchfab.com/v3/models/<uid>`; `/download` endpoint returns `401 Unauthorized` without logged-in user session**:
     - Primary spruce: **Spruce tree** by **Georgeous** (`intice184`), `https://sketchfab.com/3d-models/spruce-tree-7a5db417827244d98827459bce0cc944` (`10,387` faces, LOD0/LOD1, bark + branch maps, CC-BY-4.0).
     - Spruce fallback (only if primary fails quality/import): **Realistic HD Norway spruce (3/43)** by **PlantCatalog**, `https://sketchfab.com/3d-models/realistic-hd-norway-spruce-343-bf500546e2874f9ea086ba6abb11357e` (`143,190` faces, LODs, 9.5 m, CC-BY-4.0).
     - Orchard tree: **Apple Tree** by **rhcreations**, `https://sketchfab.com/3d-models/apple-tree-e5e1208e7e734f88b02c5f45c70f8db1` (`67,563` faces, Blender 2.79b rigged tree — import static mesh pose only, CC-BY-4.0).
     - The Orchestrator is asking Michal once alongside this planning prompt to place the downloaded Sketchfab archives into `/Users/agile/Downloads/` (or `work/downloads/`) for `01/02` implementation.

## Questions Your Plan Must Answer (Concise and Decision-Complete)

Perform one brief read-only MCP verification call (`get_scene_info` or a short read-only `execute_blender_code`) to confirm your session's live MCP connection to `blender/kysucka_chata_mcp_v03.blend`, then answer **only** these four questions:

1. **Asset availability, acquisition/import strategy, and license/manifest tracking**:
   - Specify how `01/02` will acquire the 4 Poly Haven CC0 models (`food_apple_01`, `grass_medium_01`, `shrub_01`, `periwinkle_plant` via direct HTTP from `dl.polyhaven.org` with MD5/SHA-256 verification into `work/downloads/`) and ingest the Sketchfab CC-BY-4.0 archives (`Spruce tree — Georgeous` `7a5db417827244d98827459bce0cc944` [or fallback `bf500546e2874f9ea086ba6abb11357e`] and `Apple Tree — rhcreations` `e5e1208e7e734f88b02c5f45c70f8db1` from `/Users/agile/Downloads/` or `work/downloads/`, stopping cleanly to report the exact missing filename if absent).
   - Specify how normalized static master meshes/LODs and 1K/2K textures will be extracted into tracked `assets/models/<asset_id>/` (stripping rigs/armatures, cameras, lights, worlds, and demo scatter planes, keeping auto-run disabled, verifying alpha/normal/translucency shader nodes in a small asset test render before scattering), and how CC-BY-4.0 and CC0 credits, creator names, source URLs, license URLs, SHA-256 hashes, dimensions, LODs, and modifications will be recorded in `assets/ASSET_MANIFEST.md` and `README_SK.md`.
2. **Projected ridge/forest and near-spruce/orchard/front-planting 3D layout**:
   - Specify the parametric 2–3 layer background terrain (`LANDSCAPE_hills_v04`) and spruce forest patch scatter covering `u = 0.00–0.65, v = 0.15–0.55` (plus right-side hillside continuity near `u = 0.90–1.00`) with meadow clearings, irregular forest edges, upright trees grounded on the surface, and varied height/rotation.
   - Specify the placement of `3–6` smaller young-habit spruces (`1.5–3.5 m` height) near the garden perimeter (left behind orchard/wood-bay and right beyond the glazed gable), keeping the entry, glazing, and roof silhouette clear.
   - Specify the left-garden orchard apple tree replacement around `(-0.6, -3.0)` (static crown framing left edge `u ≈ 0.00–0.22` without blocking the entrance or sky, plus attached `6–9 cm` `food_apple_01` instances on upper/outer twigs if the imported tree lacks usable visible apples).
   - Specify the irregular layered front planting in `BED_entry` (`shrub_01` low clumps, `grass_medium_01` airy tufts, `periwinkle_plant` flower accents, keeping the entry steps `X = 6.5..9.2` and bench `X = 10.2..12.4` clear), restrained grass tufts along visible lawn/fence edges, improved soil/lawn ground shaders (preserving near-ground `SITE_terrain_proxy` geometry), and deterministic hiding/removal of the 263 superseded proxy objects in `90_VEGETATION_PROXY`.
3. **LOD, instancing, memory, and file-size budget**:
   - Specify how master assets are stored and instanced (linked mesh data / collection instances sharing single materials and packed 1K/2K images, LOD0 for near/silhouette trees and LOD1 for distant forest canopies, no destructive realization of thousands of copies), how unique source triangles stay well below `3,000,000` and each tracked file stays below `90 MiB`, and how `01/02` will measure actual memory, unique/evaluated triangle counts, and render time.
4. **Exact mutation paths, deterministic `scripts/landscape_v04.py` hook, semantic replay, and acceptance**:
   - Specify the exact allowlist for `01/02` (`scripts/landscape_v04.py`, `scripts/build_scene.py`, `model/parameters.json`, `assets/ASSET_MANIFEST.md`, normalized `assets/models/...`, `blender/kysucka_chata_mcp_v04.blend`, `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, gitignored `work/` checkpoints/replay/downloads, and Meta deliverables `renders/before.png`, `renders/after.png`, `renders/landscape_details.png`, `renders/render_metadata.json`, `evidence/landscape_comparison.md`, `01_report_01.md`, `../00_RUN_MAP.md`).
   - Specify how `apply_v04(scene, P, ROOT)` in `scripts/landscape_v04.py` uses isolated `random.Random(13704)` after `apply_v03` so `random.getstate()` and `v03` timber/fence are preserved and idempotent on a second call, and how cold CLI reopen and disposable source replay (`work/v04_source_replay.blend`) will verify semantic scene data (object/instance counts, transforms, bounding boxes, material assignments, packed textures, and preserved `v03` non-vegetation fingerprint within declared tolerances — **without** gating on a cross-version UI/default-RNA dump).

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection without MCP), which cannot perform live MCP inspection/control of the open Blender 5.2.3 LTS GUI session required by this logical whole.
- **Activated route for this task**: `blender-mcp-live-v1` using the session's exposed Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) connected to the running Blender 5.2.3 LTS GUI, supplemented by read-only local Git/file/hash inspection.
- **Evidence class**: directly observed MCP tool receipts and read-only repository/hash checks.
- **Bounded planning authority**: strictly read-only MCP observation and read-only local repository inspection. No file writes, downloads, or scene mutations are authorized during planning.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/04-kysuce-forest-and-natural-garden
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: none

Positive authority:
- Read-only inspection of `/Users/agile/Projects/kysucka_moderna_chata`, `/Users/agile/Downloads`, and `/Users/agile/meta/projects/kysucka_moderna_chata/00/`.
- Read-only Blender MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code` printing JSON/text without modifying `bpy.data` or `bpy.context.scene`, and optional `look` with `shading="solid"` or `image=...`).
- **Satisfiable completion route for Native Plan Mode (`P2` / `00_handout.md`)**: Because the Worker client's Native Plan Mode blocks direct file writes, `Report persistence owner` is set to `ORCHESTRATOR` with `Trace persistence: none` for the Worker. Return your complete standard terminal report (`### Report for ORCHESTRATOR_CHAT` ...) directly in the session output (`status: PASS` once your read-only checks and technical plan are complete); do not attempt file writes in Native Plan Mode. The Fresh Orchestrator will persist your exact returned report bytes to `/Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/01_report_00.md` and read it back completely.

Commands:
- Read-only file reads, `git status`, `git rev-parse`, `shasum -a 256`, `./.ap/ap doctor`.
- Read-only Blender MCP tool calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, `look`).

Git authority:
- Read-only in both `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta`. No `git fetch`, `git add`, `git commit`, `git push`, `git checkout`, `git reset`, or `git clean`.

Dependency, network, and secret authority:
- Dependency authority: none (no package, add-on, `uvx`, `pip`, or runtime installation/update).
- Network authority: localhost Blender MCP socket only during planning; external asset downloads are reserved for `01/02` implementation.
- Secret authority: none.
- Side-effect authority: strictly read-only inspection of repository and live Blender MCP state.

Negative authority:
- Do NOT mutate any file in `/Users/agile/Projects/kysucka_moderna_chata` or `/Users/agile/meta` during planning.
- Do NOT mutate the live Blender scene, download assets, change camera/material/mesh values, save `.blend` files, or trigger `bpy.ops.render.render()` during planning.
- Do NOT install or update `mcp-for-blender`, modify client MCP config, change telemetry settings, or call `generate_3d` / `generate_gaussian_world` / `import_asset`.
- Do NOT quote, print, or reproduce the literal project closure signal from `AGENTS.md`.

## Validation and Stopping Conditions

Evidence tier: E2
Evidence tier basis: cross-cutting reversible live-scene environment/vegetation refinement, CC0 and CC-BY-4.0 3D asset integration, semantic source-replay verification, and matched 1448x1086 denoised Cycles visual comparison
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: none (read-only planning phase)
New causal regression: none — planning phase specifies the bounded Kysuce environment refinement, semantic source-replay check, and matched render comparison
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (read-only observation in planning)
Independent acceptance: not-required

Validation in this planning task:
1. Verify repository root, branch `main`, HEAD `623d12abe0c0eb2742cd02c9962c1712b53437e2`, clean status, `./.ap/ap doctor`, and the protected S00, v01, v02, and v03 SHA-256 hashes.
2. Perform at least one read-only Blender MCP tool call confirming live connection to the open `kysucka_chata_mcp_v03.blend` scene (`CAM_A_REFERENCE` locked at `[21.5, -10.0, 1.25]`, `35 mm`, `shift_y = 0.105`) without changing `bpy.data.is_dirty` (`False`) or scene objects.
3. Verify that your plan answers all four required questions concisely and names exact asset files/URLs, license/manifest rules, projected 3D ridge/garden layout, LOD/instancing budget, allowlist paths, mutation axes, semantic source-replay tolerances, and rollback for implementation.

Stopping conditions:
- Stop immediately if repository identity, baseline commit, or source hashes disagree with this grant.
- Stop and report `BLOCKED` if Blender MCP tools are unavailable in your session (do not substitute headless CLI or attempt installation/reconfiguration).
- Stop after submitting your terminal planning report in-session; planning authority expires at the report (`Plan-to-Execution Gate`).

## Completion and Report Contract

Begin your in-session report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-kysuce-forest-and-natural-garden`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 01`

Include the compact core (`status: PASS` once read-only verification and the four-part plan are complete; `Phase-qualified result: not-applicable`; `Start commit` and `End commit`: `623d12abe0c0eb2742cd02c9962c1712b53437e2`; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`). Keep the report concise (under ~220 lines) and decision-complete.
