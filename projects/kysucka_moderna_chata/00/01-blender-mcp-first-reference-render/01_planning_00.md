# Plan first useful reference-frame improvement through Blender MCP

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-blender-mcp-first-reference-render
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BLENDER-MCP-FIRST-REFERENCE-RENDER-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded technical planning for one live Blender MCP reference-frame improvement using established Orchestrator grounding
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: concise repository- and live-MCP-grounded technical plan answering the three bounded questions below for read -> change -> readback -> save -> comparable 4:3 before/after renders
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

Produce a concise, decision-complete technical implementation plan for the logical whole `kysucka-moderna-chata-blender-mcp-first-reference-render`.

Accepted Cooperator and project decisions:
- Michal requires tangible visual progress through the already available and functioning **Blender MCP** connected to his live Blender 5.2.3 LTS GUI session, producing:
  1. Actual MCP-tool communication (`read -> authorized change -> readback`).
  2. A saved, reopenable working copy `blender/kysucka_chata_mcp_v01.blend` preserving `blender/kysucka_chata_seed.blend` (`9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`), `reference/kysucka_chata_moderna.png` (`05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`), and any unsaved owner state.
  3. Comparable 4:3 camera renders (`renders/before.png` and `renders/after.png`, target at least `640 x 480` if measured host render time fits cleanly), `renders/render_metadata.json`, and `evidence/mcp_actions.md` in this Meta whole directory.
- Communicate with the Cooperator in Slovak if addressing him directly; write your formal Worker report in English starting with `### Report for ORCHESTRATOR_CHAT`.
- **Important anti-stall constraint**: Do **not** print, quote, propose, or reproduce the project's literal Orchestrator-owned closure signal anywhere in your plan or report. Keep the existing `Closure and Git gates` section of `AGENTS.md` untouched. Do not produce full-file replacement text for documentation files or an exhaustive parameter catalog; keep your plan concise and focused.

## Repository and Environment Prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Baseline: `b47cce6f91ae10a22fb708a8e5220ab27b471aeb` (`docs: initialize pinned AP and external Meta workflow`)
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap` (pinned submodule checkout; detached HEAD equal to gitlink accepted)
Trace repository: `https://github.com/cisarik/meta.git` at `/Users/agile/meta` (HEAD `fe24ef3e3239f79abf05d123b2edf7dd4278643d`; unrelated work in `projects/bookradar/`, `projects/jelena/`, `projects/kronika/`, and `projects/kysucka_moderna_chata/00/00-init/` must remain untouched)

Mandatory reading:
- `.ap/AP.md` (Semantic Authority and WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-04, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#planning-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `docs/VISUAL_BRIEF.md`, `README_SK.md`
- `model/parameters.json`, `scripts/build_scene.py`, `scripts/render_scene.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_notes.md`

## Established Orchestrator MCP Grounding (Reuse, Do Not Re-Inventory Broadly)

The Orchestrator has already verified the repository baseline, `./.ap/ap doctor` (`PASS`), the four protected SHA-256 hashes, and the live Blender session via MCP (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, and `look` in `viewport` and `camera` modes):

1. **Live Blender session state**:
   - Blender `5.2.3 LTS`, MCP addon `[1, 8]` (protocol 15; external asset libraries and generators `off`; `telemetry_consent: false`).
   - Open file: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_seed.blend` (`is_saved: True`, `is_dirty: True`).
   - Scene `'Scene'`: `656` objects (`648` mesh, `6` light, `1` camera, `1` empty), `13,438` total mesh vertices (identical to the seed).
   - Active object: `APPLE_foliage_proxy.022` (42 vertices, location `[0.4291, -3.9701, 3.0752]`), currently in **`EDIT` (`EDIT_MESH`) mode**.
2. **Why the viewport / `00.png` showed green opaque glazing and a flat grey background**:
   - The 3D Viewport area (`1583 x 922`) is in `view_perspective = 'PERSP'` (not `'CAMERA'`), `shading.type = 'MATERIAL'`, `use_scene_lights = False`, `use_scene_world = False`, `studio_light = 'forest.exr'`.
   - `MAT_GLASS` uses `Principled BSDF` (`Base Color = [0.92, 0.97, 0.99, 1.0]`, `Roughness = 0.07`, `IOR = 1.45`, `Transmission Weight = 1.0`, `Alpha = 1.0`, `Thin Wall = False`) with `surface_render_method = 'DITHERED'` and `use_raytrace_refraction = False`.
   - In EEVEE Material Preview (`use_scene_world = False`, `forest.exr`, `use_raytrace_refraction = False`), the glazing does not refract the interior room; it displays the blurred green `forest.exr` studio HDRI over a flat grey background.
   - In a real **Cycles** render (`engine = 'CYCLES'`, `resolution = 1448 x 1086` 4:3, `view_transform = 'AgX'`), `MAT_GLASS` is already transparent and shows the interior (`previews/camera_a_material.png`).
3. **Remaining visual discrepancies in the actual Cycles camera frame (`CAM_A_REFERENCE`) vs `reference/kysucka_chata_moderna.png` (`1448 x 1086`)**:
   - **Camera framing (`CAM_A_REFERENCE`)**: currently at `location = [27.5, -15.5, 1.7]`, target `[7.45, 3.15, 1.7]` (`rotation_euler = [1.5708, 0.0, 0.8216]`), `lens = 50.0` mm, `sensor_width = 36.0` mm, `shift_y = 0.17`. In `previews/camera_a_material.png`, the cottage sits small/low with ~30% empty sky above the ridge, the camera is too far to the right (`X = 27.5`) so the interior fireplace (`X = 11.3, Y = 3.2`) is hidden behind the right gable corner (`X = 14.4, Y = 0.15`), and the foreground fence does not span the lower frame as in the reference.
   - **World / sky / glazing / viewport settings**: `WORLD_procedural_sky` has `Sky Texture` (`SINGLE_SCATTERING`, `sun_elevation = 26°`, `sun_rotation = 228°`) with `Background Strength = 0.26` (dim grey-tan sky compared to the bright daylight sky in the reference); `G01_lower_glass` and `G02_upper_glass` are 2 cm thick solid meshes (`Thin Wall = False`); and the live viewport has `use_scene_lights = False`, `use_scene_world = False`, `view_perspective = 'PERSP'`, and `MAT_GLASS.use_raytrace_refraction = False`.
   - **Compute device**: `scene.cycles.device` is `'CPU'` while `preferences.addons['cycles'].preferences.compute_device_type` is `'METAL'` (actual device behavior/speed in Blender 5.2.3 LTS remains to be measured on a small preview during implementation).

## Questions Your Plan Must Answer (Concise and Decision-Complete)

Perform one brief read-only MCP verification call (`get_scene_info` or a short read-only `execute_blender_code`) to confirm your session's live MCP connection to the cottage scene, then answer **only** these three questions:

1. **Primary obstruction diagnosis**: From the Orchestrator's MCP scene/view observations (and your read-only verification), which single camera/display/glass/world issue most obstructs a useful reference image right now (distinguishing the viewport-only green-glass symptom from the real Cycles camera render comparison against `reference/kysucka_chata_moderna.png`)?
2. **Safe checkpoint + one highest-value correction**:
   - What is the exact safe working-copy/checkpoint sequence that handles `is_dirty == True` and `APPLE_foliage_proxy.022` in `EDIT` mode, preserves any unsaved state and `blender/kysucka_chata_seed.blend` untouched, and opens/saves `blender/kysucka_chata_mcp_v01.blend` as the active live file?
   - What is the **one** highest-value coherent correction to apply via MCP between `renders/before.png` and `renders/after.png` (keeping aspect ratio 4:3, output resolution, and unrelated systems fixed so `before.png` vs `after.png` isolates the improvement cleanly, while also setting the GUI viewport/camera state so Michal sees a proper camera/scene-world view instead of the green `forest.exr` free-perspective view)? Specify the exact property values before and after.
3. **Implementation execution & rollback specification**:
   - What exact project files, Meta output files (`renders/before.png`, `renders/after.png`, `renders/render_metadata.json`, `evidence/mcp_actions.md`), live-scene effects, connection/timeout safeguards (small preview test first, then at least `640 x 480` 4:3 camera render), source/replay capture (`model/parameters.json` and/or `scripts/build_scene.py`, plus narrow `blender-mcp-live-v1` route and working-file updates in `AGENTS.md`, `docs/OPERATIONS.md`, and `README_SK.md` without touching the closure-signal stanza), and rollback steps are needed for `read -> change -> readback -> save -> render`?

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection/render without MCP), which cannot satisfy Michal's explicit requirement for live Blender MCP control of the open GUI scene.
- **Activated route for this task**: `blender-mcp-live-v1` using the session's exposed Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) connected to the running Blender 5.2.3 LTS GUI, supplemented by read-only local Git/file/hash inspection.
- **Evidence class**: directly observed MCP tool receipts and read-only repository/hash checks.
- **Bounded planning authority**: strictly read-only MCP observation and read-only local repository inspection, plus writing your terminal report `01_report_00.md`.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/01-blender-mcp-first-reference-render
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_00.md

Positive authority:
- Read-only inspection of `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta/projects/kysucka_moderna_chata/00/`.
- Read-only Blender MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code` printing JSON/text without modifying `bpy.data` or `bpy.context.scene`, and optional `look`) to verify live MCP connectivity and inspect scene properties.
- Direct creation of the terminal report at `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_00.md` if and only if that file is absent, followed by full readback verification.
- **Client completion route for Native Plan Mode (P4)**: If active Native Plan Mode blocks direct file writes during planning, keep the complete standard terminal report (`### Report for ORCHESTRATOR_CHAT` ...) in your session output and write `01_report_00.md` once the client permits within this same grant without implementing; if the client does not permit the write at all in Plan Mode, return the complete standard report in-session with `status: PARTIAL` (noting only the native Plan Mode write restriction) so the Orchestrator can persist the exact returned bytes to `01_report_00.md` under AP's completion route without another planning cycle.

Commands:
- Read-only file reads, `git status`, `git rev-parse`, `shasum -a 256`, `./.ap/ap doctor`.
- Read-only Blender MCP tool calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, `look`).
- Native file write for `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_00.md` only.

Git authority:
- Read-only in both `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta`. No `git fetch`, `git add`, `git commit`, `git push`, `git checkout`, `git reset`, or `git clean`.

Dependency, network, and secret authority:
- Dependency authority: none (no package, add-on, `uvx`, `pip`, or runtime installation/update).
- Network authority: localhost Blender MCP socket only; no external network, asset downloads, or paid generators.
- Secret authority: none.
- Side-effect authority: read-only inspection of repository and live Blender MCP state, plus direct write of `01_report_00.md`.

Negative authority:
- Do NOT mutate any file in `/Users/agile/Projects/kysucka_moderna_chata` during planning.
- Do NOT mutate the live Blender scene, switch object mode, change camera/material/world values, save `.blend` files, or trigger `bpy.ops.render.render()` during planning.
- Do NOT install or update `mcp-for-blender` (`uvx mcp-for-blender install-addon` is forbidden), modify client MCP config, change telemetry settings, or call `generate_3d` / `generate_gaussian_world` / `import_asset`.
- Do NOT quote, print, or reproduce the literal project closure signal from `AGENTS.md`.
- Do NOT touch unrelated files in `/Users/agile/meta`.

## Validation and Stopping Conditions

Evidence tier: E2
Evidence tier basis: cross-cutting reversible live-scene and repository workflow with explicit MCP read/change/readback and visual render artifacts
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: none (read-only planning phase)
New causal regression: none — planning phase produces a technical plan and verifies read-only MCP connectivity
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (read-only observation in planning)
Independent acceptance: not-required

Validation in this planning task:
1. Verify repository root, branch `main`, HEAD `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`, clean status, and the four protected SHA-256 hashes.
2. Perform at least one read-only Blender MCP tool call confirming live connection to the open `kysucka_chata_seed.blend` scene without changing `bpy.data.is_dirty` or scene objects.
3. Verify that your plan answers all three required questions concisely and names exact paths, property values, mutation axes, and rollback for implementation.
4. If direct write is permitted by your client, verify `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_00.md` is absent before writing, write the complete report, and read it back completely.

Stopping conditions:
- Stop immediately if repository identity, baseline commit, or protected source hashes disagree with this grant.
- Stop and report `BLOCKED` if Blender MCP tools are unavailable in your session (do not substitute headless CLI or attempt installation/reconfiguration).
- Stop after submitting your terminal planning report; planning authority expires at the report (`Plan-to-Execution Gate`).

## Completion and Report Contract

Begin your report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-blender-mcp-first-reference-render`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 01`

Include the compact core (`status: PASS` if plan + direct write succeed, or `status: PARTIAL` if the plan is complete and only Native Plan Mode blocked the file write; `Phase-qualified result: not-applicable`; `Start commit` and `End commit`: `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`). Keep the report concise (under ~200 lines) and decision-complete.
