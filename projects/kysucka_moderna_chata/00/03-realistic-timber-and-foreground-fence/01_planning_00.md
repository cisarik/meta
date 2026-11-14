# Plan realistic exterior timber and foreground rustic fence (v03)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-realistic-timber-and-foreground-fence
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BLENDER-MCP-REALISTIC-TIMBER-AND-FOREGROUND-FENCE-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded technical planning for PBR exterior/fence wood materials, explicit metric UVs, foreground fence placement, and source-replay synchronization using established Orchestrator MCP grounding
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: concise repository- and live-MCP-grounded technical plan specifying (1) selected CC0 wood texture sets, shader/UV mapping, and exact consumers, (2) foreground rustic fence 3D layout/geometry method and placement trials, (3) minimal source/asset/output allowlist and local deterministic RNG isolation, and (4) preservation, matched 1448x1086 denoised render comparison, source-replay verification, and rollback for v03
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

Produce a concise, decision-complete technical implementation plan for the logical whole `kysucka-moderna-chata-realistic-timber-and-foreground-fence`.

Accepted Cooperator and project decisions:
- Starting from the accepted v02 working scene (`blender/kysucka_chata_mcp_v02.blend` at commit `d67431d1678de511e06a8ad04cd632ae4899cdc4`) and keeping its selected camera (`CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35 mm`, `sensor_width = 36 mm`, `shift_x = 0.0`, `shift_y = 0.105`) strictly locked, deliver a visibly better **exterior timber facade/gable/soffit/bay-post material** and a **rustic foreground fence** (both weathered timber appearance and lower-foreground placement matching `reference/kysucka_chata_moderna.png`) in `blender/kysucka_chata_mcp_v03.blend`, synchronized with `model/parameters.json` and procedural source (`scripts/build_scene.py`).
- Vegetation/shrubs (`SHRUB_proxy*`, `FLOWER_proxy*`, `APPLE_*`, `CONIFER_*`), sky/daylight (`WORLD_procedural_sky`), fireplace/chimney position, interior partitions/doors, roof, stone, glass, terrain, and path remain strictly preserved in this logical whole and are recorded as future-scope observations.
- Communicate with the Cooperator in Slovak if addressing him directly; write your formal Worker report in English starting with `### Report for ORCHESTRATOR_CHAT`.
- **Important anti-stall constraint**: Do **not** print, quote, propose, or reproduce the project's literal Orchestrator-owned closure signal anywhere in your plan or report. Keep the managed AP block and the entire `Closure and Git gates` section of `AGENTS.md` untouched. Do not turn this into asset-library research, a broad audit, or repeated planning.

## Repository and Environment Prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Baseline: `d67431d1678de511e06a8ad04cd632ae4899cdc4` (`feat: calibrate 3D camera perspective in mcp_v02 working scene`)
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap` (pinned submodule checkout; detached HEAD equal to gitlink accepted)
Trace repository: `https://github.com/cisarik/meta` at `/Users/agile/meta` (HEAD `4db94c333340c6b77d06701d050de286c701dabc`; preserve all unrelated work and predecessor files untouched)

Mandatory reading:
- `.ap/AP.md` (Semantic Authority and WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-04, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#planning-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `model/parameters.json`, `scripts/build_scene.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_closure.md`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/00_handout.md` and `00_notes.md`

## Established Orchestrator MCP, Geometry, and Asset Grounding (Reuse Directly)

The Orchestrator has already verified the repository baseline (`d67431d1678de511e06a8ad04cd632ae4899cdc4`), `./.ap/ap doctor` (`PASS`), all protected S00, v01, and v02 SHA-256 hashes, the live Blender 5.2.3 LTS session via MCP, and the official Poly Haven CC0 wood texture manifests:

1. **Live Blender 5.2.3 LTS state**:
   - Open file: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend` (`is_saved: True`, `is_dirty: False`, `is_job_running('RENDER'): False`, `mode: OBJECT`, `656` objects, `13,438` mesh vertices).
   - Locked camera `CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]` (`rotation_euler = [1.570796, -0.0, 0.805004]`), `lens = 35.0` mm, `sensor_width = 36.0` mm, `shift_x = 0.0`, `shift_y = 0.105`.
   - Note on `look`: the active Layout viewport is in `RENDERED` shading with Cycles; if calling `look(mode="camera")`, pass `shading="solid"` (or `image=...`) so it does not fail on Cycles viewport capture.
2. **Material sharing & exact consumer boundaries in `v02`**:
   - `MAT_WOOD_H` (`102` objects) is shared between `CLADDING_front*` (`35`), `CLADDING_rear*` (`33`), `FENCE_rail_proxy*` (`2`), and **out-of-scope** `COFFEE_table` (`1`), `DINING_table` (`1`), `CHAIR_seat*` (`6`), `APPLE_trunk_proxy` (`1`), `APPLE_branch_proxy*` (`23`).
   - `MAT_WOOD_V` (`92` objects) is shared between `GABLE_timber*` (`16`), `SOFFIT_wood*` (`2`), `WOOD_BAY_post*` (`2`), `GABLE_other_proposed` (`1`), `FENCE_post_proxy*` (`26`), and **out-of-scope** `WALL_DECOR_proxy` (`1`), `CHAIR_back*` (`6`), `TREE_trunk_proxy*` (`38`).
   - Therefore, `MAT_WOOD_H` and `MAT_WOOD_V` must remain untouched on all out-of-scope objects (`32` + `45` = `77` objects). Dedicated PBR materials (e.g. `MAT_TIMBER_EXTERIOR` for facade/gable/soffit/bay-posts and `MAT_TIMBER_FENCE` for fence stakes/rails) must be created and assigned only to the exact target consumers.
3. **Target mesh local axes and UV layer facts**:
   - `CLADDING_front_*` (`35` objects) and `CLADDING_rear_*` (`33` objects): `cube()` meshes, rotation `[0,0,0]`, board thickness `Y = 0.060 m`, row height `Z <= 0.205 m` (`0.22 m` pitch), bevel `0.007 m` (`2` segments) + `WEIGHTED_NORMAL`. Long axis is local `X`. Their existing `UVMap` is unscaled default unit-cube UV (stretched up to `28.8×`).
   - `GABLE_timber_*` (`16` objects), `GABLE_other_proposed` (`1` object), and `SOFFIT_wood_0` / `SOFFIT_wood_1` (`2` objects): created via `from_pydata`, so they currently have **no UV layer (`uv_layers = []`)**! Without a valid `UVMap`, tangent-space normal maps (`ShaderNodeNormalMap`) have undefined tangents.
   - `WOOD_BAY_post` and `WOOD_BAY_post.001` (`2` objects, `dim = [0.18, 0.20, 2.80]`): upright long axis is local `Z`.
   - `beam()` builds members with length along **local `Z`** before quaternion rotation.
   - Writing explicit metric UVs (`UVMap`) on every target mesh — where `u` is distance in metres along the member's actual long axis (`X` for horizontal cladding and soffit span; `Z` for upright gable boards, wood-bay posts, fence stakes, and `beam()` fence rails) and `v` is distance in metres across the grain (`Z`/`Y` for cladding, `Y` for gable boards, sloped rake `(0, ±1, ±1)/sqrt(2)` for soffits, `X`/`Y` perimeter for posts/stakes/rails), plus a deterministic per-object offset `(du, dv)` derived from `hashlib.sha256(obj.name.encode())` — guarantees physically plausible real-unit mapping, valid tangent-space normals, and per-board variation without repeating aligned knots.
   - In the shader, deterministic per-object tone/roughness micro-variation can be driven cleanly via `ShaderNodeObjectInfo.outputs['Random']` (or deterministic UV offsets) so boards have restrained warm honey/brown variation without uniform orange tint or plastic gloss.
4. **Verified CC0 2K PBR Wood Texture Sets on Poly Haven (`https://polyhaven.com/license`)**:
   - **Set 1 — Exterior Timber (`coated_pine_02` or `teak_veneer` or `fine_grained_wood`)**:
     - `coated_pine_02` (`https://polyhaven.com/a/coated_pine_02`, real scale `1.05 × 1.05 m`, continuous knotty pine surface without plank seams or nails):
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_diff_2k.jpg` (`2,985,006` bytes, MD5 `9d2bb5797918490d00743efe737c1471`)
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_rough_2k.jpg` (`620,683` bytes, MD5 `44dd138d932b3f966e4be7ae21f81030`)
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_nor_gl_2k.jpg` (`1,418,403` bytes, MD5 `e4ca3043d18d35aee836fc26cfc3ac1e`)
       - *(Note: `coated_pine_02` has natural pine grain and knots matching the reference's honey-brown knotty timber; in the exterior shader, remap its roughness through a ColorRamp/Map Range to `0.42–0.58` so it has a soft natural exterior finish rather than indoor gloss, and warm-grade its base color to match the reference honey-brown tone).*
     - *(Alternative Set 1 if needed: `teak_veneer`, `1.00 × 1.00 m`, `teak_veneer_diff_2k.jpg` + `teak_veneer_rough_2k.jpg` + `teak_veneer_nor_gl_2k.jpg`, `7.62 MB`, or `fine_grained_wood`, `0.60 × 0.60 m`, `3.06 MB`).*
   - **Set 2 — Weathered Rustic Fence Timber (`rough_wood`)**:
     - `rough_wood` (`https://polyhaven.com/a/rough_wood`, real scale `0.50 × 0.50 m`, weathered cracked rough wood surface without plank seams or nails):
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_diff_2k.jpg` (`2,223,327` bytes, MD5 `f5f9c55696f047ceaa49dc97c5aa5526`)
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_rough_2k.jpg` (`810,338` bytes, MD5 `832d6d549a8e76c16b9af2586f429d6c`)
       - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_nor_gl_2k.jpg` (`2,520,021` bytes, MD5 `62594f2d00eb246581b9d4fde30209f1`)
       - *(Total for both 2K sets = `6` files, `10.58 MB`, leaving `assets/` + `v03.blend` well below `25 MiB` vs the `80 MiB` cap).*
5. **Foreground fence 3D placement geometry in `v02` camera**:
   - In `v02`, `SITE_terrain_proxy` is flat at `Z = -0.055 m` everywhere in the foreground (`Y < 12 m`).
   - Current fence (`Y = -5.80, X = -1.5..16.8`) projects from `u = -0.143, v = 0.685` down to `u = 0.4668, v = 0.780`, leaving `u = 0.47..1.00` empty.
   - A 3D foreground boundary line running across the front meadow from `P_start ≈ (16.60, -8.62)` to `P_end ≈ (18.25, +1.00)` (length `9.76 m`, stake feet embedded at `Z_foot = -0.075 m` into `Z_terrain = -0.055 m`, nominal stake top `Z_top ≈ 0.58–0.60 m` with deterministic irregular top/spacing/lean variation, continuous lower/upper rails at `Z ≈ 0.19 m` and `Z ≈ 0.43 m`, and a prominent anchor post near `t ≈ 0.14` / `u ≈ 0.21`) projects to:
     - Left frame crossing (`u = 0.00`): `v_top ≈ 0.83, v_foot ≈ 1.01` (inside the **lower fifth** `[0.80, 1.00]`),
     - Right frame crossing (`u = 1.00`): `v_top ≈ 0.725, v_foot ≈ 0.81` (inside the **lower 20–40% band** `[0.60, 0.80]`),
     - Mid-frame (`u = 0.34`): `v_top ≈ 0.80` (cleanly below `ENTRY_step_1` at `v = 0.733`, garden bed at `v = 0.72..0.75`, bench at `v = 0.67`, and glazed gable base at `v = 0.698..0.725`).

## Questions Your Plan Must Answer (Concise and Decision-Complete)

Perform one brief read-only MCP verification call (`get_scene_info` or a short read-only `execute_blender_code`) to confirm your session's live MCP connection to `blender/kysucka_chata_mcp_v02.blend`, then answer **only** these four questions:

1. **Selected wood assets, shader/UV mapping, and exact consumers**:
   - Confirm the exact 2K CC0 Poly Haven texture sets and files to download in `01/02` under `assets/textures/wood/` (e.g., `coated_pine_02` + `rough_wood`, 6 JPG files totaling `~10.6 MB`), their color spaces (`sRGB` for base color, `Non-Color` for roughness and OpenGL normal `nor_gl`), shader graph structure (restrained per-board color/roughness variation via `Object Info -> Random`, matte/satin exterior roughness `0.42–0.58` vs rougher desaturated weathered fence `0.72–0.88`, verified OpenGL normal strength + subtle bump, no heavy displacement or subdivision), real-metre UV projection formula (`u` along each member's actual long axis, `v` across grain, deterministic per-object hash offset `(du, dv)`), and the exact consumer object lists for `MAT_TIMBER_EXTERIOR` (`CLADDING_front*` 35, `CLADDING_rear*` 33, `GABLE_timber*` 16, `SOFFIT_wood*` 2, `WOOD_BAY_post*` 2, plus `GABLE_other_proposed` 1 = 89 objects) and `MAT_TIMBER_FENCE` (`FENCE_post_proxy*`, `FENCE_rail_proxy*`), while preserving `MAT_WOOD_H` and `MAT_WOOD_V` on all 77 out-of-scope furniture/tree/decor objects.
2. **Foreground rustic fence layout method and placement trials**:
   - Specify the exact parametric 3D fence layout (at most two purposeful placement trials in `01/02` before selecting one, e.g., Trial 1 straight boundary `(16.60, -8.62) -> (18.25, 1.00)` vs Trial 2 slight corner bend at `u ≈ 0.21` `(16.75, -8.70) -> (17.05, -7.20) -> (18.25, 1.00)`), stake count (~24–28 split/irregular stakes with bevels, subtle width/thickness/height variation `Z_top ≈ 0.58 ± 0.04 m`, mild lean `±1.5°–2.5°`, feet grounded at `Z = -0.075 m <= -0.055 m` terrain, plus a slightly thicker corner/anchor post near `u ≈ 0.21`), continuous lower/upper rails (`Z ≈ 0.19 m` and `Z ≈ 0.43 m`) physically intersecting/connecting to the stakes, and the deterministic local RNG (`random.Random(13703)` or SHA-256 hash) so the global `random.seed(137)` stream in `scripts/build_scene.py` for later trees (`TREE_trunk_proxy*`, `CONIFER_proxy*`, `APPLE_*`) remains 100% unchanged.
3. **Minimal source, asset, checkpoint, and output allowlist**:
   - Specify the exact reusable refinement module path (e.g., `scripts/timber_fence_v03.py` invoked identically through live MCP on `v02` and from `scripts/build_scene.py`), exact `model/parameters.json` additions/updates (`exterior_timber`, `fence_timber`, and `foreground_fence` parameters), `assets/ASSET_MANIFEST.md`, `assets/textures/wood/*`, `blender/kysucka_chata_mcp_v03.blend` (with used textures packed and relative paths `//../assets/textures/wood/...` retained), narrow documentation updates (`AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`), disposable `work/` checkpoints/replay scene (`work/mcp-v03-before.blend`, `work/v03_source_replay.blend`), and Meta outputs in `/Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/` (`renders/before.png`, `renders/after.png`, `renders/timber_details.png`, `renders/render_metadata.json`, `evidence/timber_fence_comparison.md`, `01_report_01.md`, plus `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`).
4. **Preservation, matched render comparison, source-replay verification, and rollback**:
   - Specify the matched full-resolution render profile required by `00_handout.md` for **both** `renders/before.png` (freshly rendered from unchanged `v02` before timber/fence changes) and `renders/after.png` (`v03`): **`1448 × 1086` at `100%`, Cycles CPU, `96` samples, `use_denoising = True` (OpenImageDenoise) for both, frame `0`, seed `0`, `AgX`, look `None`, exposure `0.0`, gamma `1.0`**, using one render job at a time and safe polling if a render outlasts a tool call; plus `renders/timber_details.png` (labelled before/after crops of facade cladding, gable/soffit timber, and foreground fence from those exact `1448 × 1086` renders with crop coordinates recorded), non-target fingerprint preservation (camera, building/openings, roof, chimney/fireplace, furniture, lights, world, glass, vegetation, terrain, path, and tree RNG stream), cold CLI reopen of `v03` (`scripts/inspect_scene.py`), disposable source-replay check into `work/v03_source_replay.blend`, and rollback steps.

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection without MCP), which cannot perform live MCP inspection/control of the open Blender 5.2.3 LTS GUI session required by this logical whole.
- **Activated route for this task**: `blender-mcp-live-v1` using the session's exposed Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) connected to the running Blender 5.2.3 LTS GUI, supplemented by read-only local Git/file/hash inspection.
- **Evidence class**: directly observed MCP tool receipts and read-only repository/hash checks.
- **Bounded planning authority**: strictly read-only MCP observation and read-only local repository inspection. No file writes, downloads, or scene mutations are authorized during planning.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/03-realistic-timber-and-foreground-fence
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: none

Positive authority:
- Read-only inspection of `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta/projects/kysucka_moderna_chata/00/`.
- Read-only Blender MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code` printing JSON/text without modifying `bpy.data` or `bpy.context.scene`, and optional `look` with `shading="solid"` or `image=...`).
- **Satisfiable completion route for Native Plan Mode (`P2` / `00_handout.md`)**: Because the Worker client's Native Plan Mode blocks direct file writes (demonstrated in predecessor `02-reference-camera-perspective/01_report_00.md`), `Report persistence owner` is set to `ORCHESTRATOR` with `Trace persistence: none` for the Worker. Return your complete standard terminal report (`### Report for ORCHESTRATOR_CHAT` ...) directly in the session output (`status: PASS` once your read-only checks and technical plan are complete); do not attempt file writes in Native Plan Mode. The Fresh Orchestrator will persist your exact returned report bytes to `/Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/01_report_00.md` and read it back completely.

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
Evidence tier basis: cross-cutting reversible live-scene material/UV/fence refinement, CC0 PBR asset integration, source-replay verification, and matched 1448x1086 denoised Cycles visual comparison
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: none (read-only planning phase)
New causal regression: none — planning phase specifies the bounded timber/fence refinement, source-replay check, and matched render comparison
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (read-only observation in planning)
Independent acceptance: not-required

Validation in this planning task:
1. Verify repository root, branch `main`, HEAD `d67431d1678de511e06a8ad04cd632ae4899cdc4`, clean status, `./.ap/ap doctor`, and the protected S00, v01, and v02 SHA-256 hashes.
2. Perform at least one read-only Blender MCP tool call confirming live connection to the open `kysucka_chata_mcp_v02.blend` scene (`CAM_A_REFERENCE` locked at `[21.5, -10.0, 1.25]`, `35 mm`, `shift_y = 0.105`) without changing `bpy.data.is_dirty` (`False`) or scene objects.
3. Verify that your plan answers all four required questions concisely and names exact asset files/URLs, UV/shader rules, fence parameters, allowlist paths, mutation axes, source-replay checks, and rollback for implementation.

Stopping conditions:
- Stop immediately if repository identity, baseline commit, or source hashes disagree with this grant.
- Stop and report `BLOCKED` if Blender MCP tools are unavailable in your session (do not substitute headless CLI or attempt installation/reconfiguration).
- Stop after submitting your terminal planning report in-session; planning authority expires at the report (`Plan-to-Execution Gate`).

## Completion and Report Contract

Begin your in-session report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-realistic-timber-and-foreground-fence`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 01`

Include the compact core (`status: PASS` once read-only verification and the four-part plan are complete; `Phase-qualified result: not-applicable`; `Start commit` and `End commit`: `d67431d1678de511e06a8ad04cd632ae4899cdc4`; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`). Keep the report concise (under ~220 lines) and decision-complete.
