# Implement first useful reference-frame improvement through Blender MCP

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-blender-mcp-first-reference-render
Worker session ordinal: 01
Worker exchange ordinal: 02
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: BLENDER-MCP-FIRST-REFERENCE-RENDER-IMPL
Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `593f5773a03563dc1e231b0f04431063ac1f322b1925d5c843a87f4e5f5e7065`) from Worker session `01` exchange `01` on baseline `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`
Authority renewal: prior planning authority expired at `01_report_00.md`; this prompt grants complete new bounded implementation, live-MCP execution, Meta artifact persistence, and project Git commit/non-force publication authority
Evidence posture: non-independent
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded execution of the accepted single-variable camera shift correction (`shift_y: 0.17 -> 0.075`), live MCP save/render/readback, and narrow source/doc sync
Recommended context capacity: approximately 250k tokens
Exact baseline: b47cce6f91ae10a22fb708a8e5220ab27b471aeb
Changed-path allowlist: blender/kysucka_chata_mcp_v01.blend, model/parameters.json, AGENTS.md, docs/OPERATIONS.md, README_SK.md
Implementation boundaries: positive authority for the five tracked project paths above, gitignored checkpoints `work/mcp-v01-owner-checkpoint.blend` and `work/mcp-v01-before.blend` (plus Blender automatic `blender/kysucka_chata_mcp_v01.blend1` if created), live Blender MCP scene/camera/viewport/render operations on the running Blender 5.2.3 LTS instance, Meta outputs (`renders/before.png`, `renders/after.png`, `renders/render_metadata.json`, `evidence/mcp_actions.md`, `01_report_01.md`), and one non-force project commit and push to `origin main`; negative authority excludes `blender/kysucka_chata_seed.blend`, `reference/kysucka_chata_moderna.png`, `scripts/build_scene.py`, `scripts/design.py`, `cad/`, `docs/*.pdf`, `previews/`, `manifest/`, `.ap/`, `.gitmodules`, the `Closure and Git gates` section of `AGENTS.md`, and any Git staging/commit/push in `/Users/agile/meta`
Independence required: no

## Goal and Accepted Plan

Execute the accepted `01/01` plan in the healthy current Worker session (`01/02`) with **Native Plan Mode OFF** (`Native planning mode: not-used`):

1. **Preserve live state and create the working `.blend` through Blender MCP**:
   - Confirm that this prompt reached the same `01` Worker session with Native Plan Mode disabled. Retained context from `01/01` is convenience only, not authority; re-verify repository and live MCP state before mutating anything.
   - Communicate with Michal in Slovak if addressing him directly; write all repository documentation updates in their existing language (`README_SK.md` and `docs/OPERATIONS.md` in Slovak, `AGENTS.md` in English) and write your formal terminal report `01_report_01.md` in English starting with `### Report for ORCHESTRATOR_CHAT`.
   - Do **not** quote, print, or reproduce the literal project closure signal from `AGENTS.md` anywhere in your report or changes. Keep the `Closure and Git gates` section of `AGENTS.md` completely untouched.
2. **Deliver the three mandatory outcomes of this whole**:
   - Live MCP read, authorized working-scene change (`CAM_A_REFERENCE.data.shift_y: 0.17 -> 0.075`), and independent MCP readback of the changed property, recorded in `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/evidence/mcp_actions.md`.
   - Saved, reopenable working scene `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend`, with `blender/kysucka_chata_seed.blend` (`9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`) and `reference/kysucka_chata_moderna.png` (`05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`) untouched.
   - Comparable 4:3 Cycles camera renders `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/before.png` (`shift_y = 0.17`) and `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/after.png` (`shift_y = 0.075`) at `640 x 480`, plus `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/render_metadata.json`, visually inspected by you, followed by one clean project commit and non-force push to `https://github.com/cisarik/kysucka_moderna_chata` `main`.

## Repository and Environment Gate

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap`
Trace repository: `https://github.com/cisarik/meta.git` at `/Users/agile/meta`

Mandatory reading:
- `.ap/AP.md` (WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §12 Validation and Public Verification; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#before-mutation`, `#validation`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#implementation-authority-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `model/parameters.json`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_notes.md` and `01_report_00.md`

Before any mutation, verify:
1. `/Users/agile/Projects/kysucka_moderna_chata` is on `main` at `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`, clean index/worktree, `origin/main` and public `refs/heads/main` equal to `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`, `./.ap/ap doctor` exits `0` (`PASS`).
2. All four protected SHA-256 values match `AGENTS.md`:
   - `blender/kysucka_chata_seed.blend`: `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`
   - `reference/kysucka_chata_moderna.png`: `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`
   - `model/parameters.json`: `00b97dd1adc1b82a19685454d4ab40dfb60332c90c7ad2ad165eb9e73e39a162`
   - `scripts/build_scene.py`: `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`
3. New target files are absent before starting:
   - `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend` (and `.blend1`)
   - `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v01-owner-checkpoint.blend`
   - `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v01-before.blend`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/before.png`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/after.png`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/render_metadata.json`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/evidence/mcp_actions.md`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_01.md`

## Execution Route and Mutation Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` (headless CLI-only in `AGENTS.md` and `docs/OPERATIONS.md`), which cannot perform live MCP control of Michal's open Blender GUI session.
- **Activated route for this task**: `blender-mcp-live-v1` (live Blender MCP tool calls against the running Blender 5.2.3 LTS GUI for scene read, checkpoint/working-copy save, camera `shift_y` update, readback, comparable 4:3 renders, and GUI viewport configuration), supplemented by local CLI only for Git, SHA-256 hashing, `./.ap/ap doctor`, and optional non-disruptive cold-reopen verification of the saved `blender/kysucka_chata_mcp_v01.blend` via `scripts/inspect_scene.py`.

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
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: blender/kysucka_chata_mcp_v01.blend, model/parameters.json, AGENTS.md, docs/OPERATIONS.md, README_SK.md (plus gitignored work/mcp-v01-owner-checkpoint.blend, work/mcp-v01-before.blend, and blender/kysucka_chata_mcp_v01.blend1)
Host/remote mutation: live Blender 5.2.3 LTS GUI session via local Blender MCP (mode switch EDIT -> OBJECT, save checkpoints and blender/kysucka_chata_mcp_v01.blend, update CAM_A_REFERENCE.data.shift_y 0.17 -> 0.075, render 640x480 before/after frames, configure 3D viewport to CAMERA + scene lights/world) and non-force git push of main to https://github.com/cisarik/kysucka_moderna_chata
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_01.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/before.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/after.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/render_metadata.json, /Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/evidence/mcp_actions.md

## Step-by-Step Implementation Envelope

### Stage 1: Live MCP Read, Owner Checkpoint, and Working Copy (`kysucka_chata_mcp_v01.blend`)

1. **Initial MCP read**:
   - Using Blender MCP (`get_scene_info` and `execute_blender_code`), read and record the live state: `bpy.data.filepath`, `bpy.data.is_dirty`, `bpy.data.is_saved`, `bpy.app.version_string`, active object (`APPLE_foliage_proxy.022`) and mode (`EDIT`), vertex count/bounding box of `APPLE_foliage_proxy.022` (using `bmesh.from_edit_mesh` while in Edit Mode) and total scene mesh vertices (`13438`), `CAM_A_REFERENCE` transform/lens/sensor/`shift_x`/`shift_y` (`0.17`), render settings, color management (`AgX`), `WORLD_procedural_sky`, `MAT_GLASS`, and 3D Viewport settings.
2. **Owner checkpoint before mode switch**:
   - Create `/Users/agile/Projects/kysucka_moderna_chata/work` if absent.
   - While still in the initial mode, save `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v01-owner-checkpoint.blend` via `bpy.ops.wm.save_as_mainfile(filepath="/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v01-owner-checkpoint.blend", copy=True, compress=True)`.
   - Verify the checkpoint file exists, is non-empty, record its SHA-256, and verify `blender/kysucka_chata_seed.blend` still has SHA-256 `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`.
3. **Switch to Object Mode and save active working scene**:
   - In `execute_blender_code`, switch from `EDIT` to `OBJECT` mode (`bpy.ops.object.mode_set(mode='OBJECT')`), verify `APPLE_foliage_proxy.022` vertex count (`42`) and world coordinates/bounding box are unchanged, and save the working copy as active mainfile:
     `bpy.ops.wm.save_as_mainfile(filepath="/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend", copy=False, compress=True)`
   - Read back `bpy.data.filepath` via MCP and confirm it is `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend`.

### Stage 2: Measured Render Probe, `before.png`, Single-Variable MCP Change, Readback, and `after.png`

1. **Create Meta output directories**:
   - Create `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders` and `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/evidence` if absent.
2. **Small measured preview probe (`160 x 120`, 8 samples)**:
   - Measure render speed on the working scene (`CYCLES`, `CPU`, `use_denoising = False`, `160 x 120`, `100%`, `8` samples) and record elapsed wall time `t`.
   - Select the common sample count deterministically per the accepted plan: `32` if `64 * t <= 90 s`; else `16` if `32 * t <= 90 s`; else `8` if `16 * t <= 90 s`.
   - **Render execution note**: When `640 x 480` at the selected sample count completes well within the MCP call timeout (e.g., `<= 45 s`), you may use either synchronous `bpy.ops.render.render(write_still=True)` or the `INVOKE_DEFAULT` job-polling route from your plan—choose whichever reliably writes the PNG file on this Blender 5.2.3 LTS instance without hanging or losing window context. Ensure only one render runs at a time and verify `bpy.app.is_job_running('RENDER') == False` after completion.
3. **Baseline checkpoint and `renders/before.png` (`shift_y = 0.17`)**:
   - Set common comparison render settings (`resolution_x = 640`, `resolution_y = 480`, `resolution_percentage = 100`, `pixel_aspect_x = 1.0`, `pixel_aspect_y = 1.0`, `cycles.samples = <selected>`, `cycles.use_denoising = False`, `cycles.seed = 0`, `cycles.use_animated_seed = False`, `view_settings.view_transform = 'AgX'`, `exposure = 0.0`, `gamma = 1.0`, `film_transparent = False`).
   - Save `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v01-before.blend` (`copy=True, compress=True`) and record its SHA-256.
   - Confirm `CAM_A_REFERENCE.data.shift_y == 0.17` and render `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/before.png`. Verify the PNG exists, decodes as `640 x 480`, and record its SHA-256 and elapsed time.
4. **Apply single highest-value correction via MCP (`shift_y: 0.17 -> 0.075`), read back, and render `renders/after.png`**:
   - Via MCP `execute_blender_code`, set `bpy.data.objects['CAM_A_REFERENCE'].data.shift_y = 0.075` (keeping location `[27.5, -15.5, 1.7]`, rotation, 50 mm lens, 36 mm sensor, `shift_x = 0.0`, and all geometry, materials, lights, world, and render settings identical).
   - Perform a separate MCP readback call confirming `round(bpy.data.objects['CAM_A_REFERENCE'].data.shift_y, 6) == 0.075` and that all other camera/render/material/world settings are unchanged.
   - Render `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/after.png` at the exact same `640 x 480` comparison settings. Verify the PNG exists, decodes as `640 x 480`, and record its SHA-256 and elapsed time.
   - Visually inspect `reference/kysucka_chata_moderna.png`, `renders/before.png`, and `renders/after.png` (using your image reader and/or `look`) to verify that:
     - both renders show transparent glazing with readable interior and procedural sky (confirming the green opaque glazing in `00.png` was a Material Preview `forest.exr` viewport artifact, not a Cycles glass shader failure), and
     - `after.png` shifts the cottage upward in the 4:3 frame closer to the reference while keeping the roof ridge and chimney crown cleanly inside the top margin.

### Stage 3: Configure GUI Viewport, Finalize and Verify `blender/kysucka_chata_mcp_v01.blend`

1. **Configure live 3D Viewport and canonical scene properties before final save**:
   - In the live Blender GUI via MCP:
     - Set the 3D Viewport to camera view (`region_3d.view_perspective = 'CAMERA'`).
     - Enable `use_scene_lights = True` and `use_scene_world = True` for Material Preview, set `use_scene_lights_render = True` and `use_scene_world_render = True`, set `scene.cycles.preview_samples = 16`, and set `shading.type = 'RENDERED'` (so Michal immediately sees the Cycles camera view with transparent glass and scene world in his open Blender window).
     - Remove any temporary Python handlers if you registered any during render tracking (`load_post`, `save_pre`, `render_pre`, `render_complete`, `render_cancel`).
     - Restore canonical output resolution on the saved scene (`scene.render.resolution_x = 1448`, `scene.render.resolution_y = 1086`, `scene.render.resolution_percentage = 100`, `scene.cycles.samples = 96`, `scene.render.filepath = '//../work/camera_a.png'`) so the saved `.blend` matches `model/parameters.json` and does not retain a hardcoded Meta output path.
   - Save `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend` (`copy=False, compress=True`).
2. **Verify saved `.blend` both live via MCP and on disk**:
   - Via MCP, read back `bpy.data.filepath`, `bpy.data.is_saved == True`, `bpy.data.is_dirty == False`, `CAM_A_REFERENCE.data.shift_y == 0.075`, object count `656`, mesh vertices `13438`, and the 3D Viewport state.
   - To verify cold reopenability from disk without risking resetting the live GUI's MCP timer, run the read-only CLI inspection against the newly saved working copy:
     `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec /Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend --python-exit-code 2 --python /Users/agile/Projects/kysucka_moderna_chata/scripts/inspect_scene.py`
     (and/or `wm.open_mainfile(filepath=..., use_scripts=False)` only if you verify MCP remains connected afterward) and confirm `shift_y = 0.075`, 656 objects, 13,438 vertices, and packed `REF_kysucka_chata_moderna`. Record the final SHA-256 of `blender/kysucka_chata_mcp_v01.blend`.

### Stage 4: Source/Documentation Sync, Meta Evidence Files, and Project Git Publication

1. **Source & documentation updates in `/Users/agile/Projects/kysucka_moderna_chata`**:
   - `model/parameters.json`: update only `"shift_y": 0.17` to `"shift_y": 0.075` under `"camera"`. (`scripts/build_scene.py` already reads `cp.get('shift_y', 0)` and stays untouched with its protected SHA-256 `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`).
   - `AGENTS.md`:
     - Update the `model/parameters.json` hash in the protected-hashes table (or list both the S00 initialization hash and the updated current hash for `model/parameters.json` plus the new `blender/kysucka_chata_mcp_v01.blend` working-copy hash, while keeping `blender/kysucka_chata_seed.blend`, `reference/kysucka_chata_moderna.png`, and `scripts/build_scene.py` hashes unchanged).
     - In `### Blender capability route`, add the task-granted `blender-mcp-live-v1` live Blender MCP route alongside `blender-local-v1` and identify `blender/kysucka_chata_mcp_v01.blend` as the current working scene copy derived from the preserved `blender/kysucka_chata_seed.blend`.
     - **CRITICAL**: Do NOT touch the `<!-- BEGIN MANAGED AP INTEGRATION --> ... <!-- END MANAGED AP INTEGRATION -->` block and do NOT touch or edit anything inside `### Closure and Git gates`.
   - `docs/OPERATIONS.md`: add a concise Slovak section describing `blender-mcp-live-v1` (live MCP control of the open GUI scene, checkpoint before mode/scene changes, and working copy `blender/kysucka_chata_mcp_v01.blend`).
   - `README_SK.md`: update the table and opening notes in Slovak to mention `blender/kysucka_chata_mcp_v01.blend` (current MCP working copy with adjusted `CAM_A_REFERENCE` `shift_y = 0.075` and camera/rendered viewport) alongside the preserved `blender/kysucka_chata_seed.blend`.
2. **Meta evidence files in `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/`**:
   - Write `renders/render_metadata.json` containing: scene/working-file identity and SHA-256, preserved seed/reference/script and updated `model/parameters.json` SHA-256 values, `work/mcp-v01-owner-checkpoint.blend` and `work/mcp-v01-before.blend` SHA-256 values, `renders/before.png` and `renders/after.png` SHA-256 values and pixel dimensions (`640 x 480`), camera transform/lens/sensor/`shift_x`/`shift_y` (`0.17` before -> `0.075` after), engine (`CYCLES`), actual rendered device (`CPU`) and configured system preference (`METAL`), color management (`AgX`, exposure `0.0`, gamma `1.0`), sample count, denoising (`false`), probe and render elapsed times, and cold-reopen verification output.
   - Write `evidence/mcp_actions.md` containing compact, public-safe receipts of the actual MCP tool calls (`get_scene_info`, `execute_blender_code`, `look`), observed pre-change state, checkpoint creation, `shift_y` change (`0.17 -> 0.075`), MCP readback, viewport configuration, and replay instructions.
3. **Validation and Project Git Commit + Non-Force Push**:
   - Run `./.ap/ap doctor` in `/Users/agile/Projects/kysucka_moderna_chata` and confirm `PASS`.
   - Verify `git status --short` shows only the five allowed tracked paths (`AGENTS.md`, `README_SK.md`, `blender/kysucka_chata_mcp_v01.blend`, `docs/OPERATIONS.md`, `model/parameters.json`; `work/` and `*.blend1` must remain gitignored/untracked).
   - Stage only the exact five paths:
     `git add blender/kysucka_chata_mcp_v01.blend model/parameters.json AGENTS.md docs/OPERATIONS.md README_SK.md`
   - Recheck `git diff --cached --stat` and confirm `blender/kysucka_chata_seed.blend`, `reference/kysucka_chata_moderna.png`, and `scripts/build_scene.py` are untouched.
   - Commit on `main` (e.g. `feat: create mcp_v01 working scene and refine camera vertical shift`) with parent `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`.
   - Recheck `git ls-remote origin refs/heads/main` equals `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`, push non-force (`git push origin main`), and verify public `refs/heads/main` equals your new commit SHA via `git ls-remote origin refs/heads/main`.

## Commands, Prohibitions, and Rollback

Commands:
- Blender MCP tools: `get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`.
- Local shell in `/Users/agile/Projects/kysucka_moderna_chata`: file reads/writes on allowed paths, `mkdir -p`, `shasum -a 256`, `./.ap/ap doctor`, read-only `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec .../blender/kysucka_chata_mcp_v01.blend --python-exit-code 2 --python .../scripts/inspect_scene.py`, and exact-path Git commands (`git status`, `git diff`, `git add <exact-5-paths>`, `git commit`, `git ls-remote`, `git push origin main`).

Negative authority:
- Never modify or overwrite `blender/kysucka_chata_seed.blend`, `reference/kysucka_chata_moderna.png`, `scripts/build_scene.py`, `scripts/design.py`, `cad/`, `docs/*.pdf`, `previews/`, `manifest/`, or `.ap/`.
- Never run `git add .`, `git add -A`, `git push --force`, `git reset --hard`, or `git clean`.
- Never run any Git write command (`git add`, `git commit`, `git push`, `git restore`, `git checkout`) inside `/Users/agile/meta`.
- Never install/update packages or add-ons (`uvx`, `pip`, `poetry`), alter MCP configuration, enable telemetry, or call external 3D/world/asset generators.
- Never quote or emit the literal project closure signal from `AGENTS.md`.

Rollback:
- If any checkpoint fails before mutation, stop immediately with zero changes.
- If a live scene or render step fails after `work/mcp-v01-owner-checkpoint.blend` is saved, ensure no render job is running (`bpy.app.is_job_running('RENDER') == False`), preserve all checkpoints and partial evidence, restore `model/parameters.json` and doc edits if uncommitted, and report the exact causal blocker.

## Validation Ladder and Publication Annex

Evidence tier: E2
Evidence tier basis: reversible working-scene creation, single-parameter camera framing update, comparable 4:3 renders, and non-force public Git publication
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor` and read-only `scripts/inspect_scene.py` on `blender/kysucka_chata_mcp_v01.blend`
Affected tests: `./.ap/ap doctor`, `scripts/inspect_scene.py`, and PNG image header/dimension + visual inspection on `renders/before.png` and `renders/after.png`
New causal regression: none — verified directly via MCP readback, `scripts/inspect_scene.py`, and `before.png`/`after.png` comparison
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (live Blender 5.2.3 LTS GUI via MCP) + `blender-local-v1` read-only cold-reopen check
Independent acceptance: not-required (Orchestrator will independently inspect the live scene via MCP, the saved `.blend`, the rendered images, and the public Git commit)

## Completion and Report Contract

Write your complete terminal report directly to:
`/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_report_01.md`
and read back the entire file to verify exact content and first line before sending your short completion notice.

Begin `01_report_01.md` with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-blender-mcp-first-reference-render`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 02`

Include:
- `status: PASS` (or `PARTIAL`/`BLOCKED` if any required gate could not complete)
- `Phase-qualified result: implementation-PASS` (and report `publication-PASS` evidence in the publication section)
- `Start commit: b47cce6f91ae10a22fb708a8e5220ab27b471aeb` and `End commit: <new-40-hex-commit-sha>`
- `Report justification: new-mutation`
- `Logical-whole closure: not-closed`
- Concise summary of changed files, SHA-256 hashes (seed, reference, `scripts/build_scene.py`, updated `model/parameters.json`, new `blender/kysucka_chata_mcp_v01.blend`, checkpoints, `renders/before.png`, `renders/after.png`, `renders/render_metadata.json`, `evidence/mcp_actions.md`), MCP read -> change (`shift_y: 0.17 -> 0.075`) -> readback receipts, visual comparison of `before.png` vs `after.png` against `reference/kysucka_chata_moderna.png`, `./.ap/ap doctor` and cold-reopen results, and public `origin/main` readback.
- `Orchestration critique` (`MEASURED` and `LEAD`), `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, and `Authority expiry`.
