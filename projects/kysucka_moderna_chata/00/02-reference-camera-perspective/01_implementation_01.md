# Implement 3D camera perspective comparison and save v02 through Blender MCP

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-reference-camera-perspective
Worker session ordinal: 01
Worker exchange ordinal: 02
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: BLENDER-MCP-REFERENCE-CAMERA-PERSPECTIVE-IMPL
Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `71e6552eb3e91f50253c5c41aad8119bebec3e51e18e434dd9c656c9cf1c7274`) from Worker session `01` exchange `01` on baseline `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`
Authority renewal: prior planning authority expired at `01_report_00.md`; this prompt grants complete new bounded implementation, live-MCP camera comparison/render/save, Meta artifact persistence, and project Git commit/non-force publication authority
Evidence posture: non-independent
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded execution of the accepted 3-candidate camera perspective comparison, v02 save, source/doc sync, and publication
Recommended context capacity: approximately 250k tokens
Exact baseline: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa
Changed-path allowlist: blender/kysucka_chata_mcp_v02.blend, model/parameters.json, AGENTS.md, docs/OPERATIONS.md, README_SK.md
Implementation boundaries: positive authority for the five tracked project paths above, gitignored checkpoints `work/mcp-v02-before.blend` (and `work/mcp-v02-owner-checkpoint.blend` only if dirty) plus Blender automatic `blender/kysucka_chata_mcp_v02.blend1` if created, live Blender MCP camera/render/viewport/save operations on the running Blender 5.2.3 LTS instance, Meta outputs (`renders/before.png`, `renders/candidate_01.png`, `renders/candidate_02.png`, `renders/candidate_03.png`, `renders/candidates_sheet.png`, `renders/after.png`, `renders/render_metadata.json`, `evidence/camera_comparison.md`, `01_report_01.md`, and `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`), and one non-force project commit and push to `origin main`; negative authority excludes `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `reference/kysucka_chata_moderna.png`, `model/reference_landmarks.json`, `scripts/build_scene.py`, `scripts/design.py`, `cad/`, `docs/*.pdf`, `previews/`, `manifest/`, `.ap/`, `.gitmodules`, the `Closure and Git gates` section of `AGENTS.md`, and any Git staging/commit/push in `/Users/agile/meta`
Independence required: no

## Goal and Accepted Plan

Execute the accepted `01/01` plan in the healthy current Worker session (`01/02`) with **Native Plan Mode OFF** (`Native planning mode: not-used`):

1. Confirm that this prompt reached the same `01` Worker session with Native Plan Mode disabled. Retained context from `01/01` is convenience only, not authority; re-verify repository and live MCP state before mutating anything.
2. Communicate with Michal in Slovak if addressing him directly; write repository documentation updates in their existing language (`README_SK.md` and `docs/OPERATIONS.md` in Slovak, `AGENTS.md` in English), write `evidence/camera_comparison.md` and `01_report_01.md` in clear technical English (`01_report_01.md` starting with `### Report for ORCHESTRATOR_CHAT`).
3. Do **not** quote, print, or reproduce the literal project closure signal from `AGENTS.md` anywhere in your report, evidence files, or changes. Keep the `Closure and Git gates` section and the managed AP block of `AGENTS.md` completely untouched.

## Repository and Environment Gate

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap`
Trace repository: `https://github.com/cisarik/meta.git` at `/Users/agile/meta`

Mandatory reading:
- `.ap/AP.md` (WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §12 Validation and Public Verification; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#before-mutation`, `#validation`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#implementation-authority-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `model/parameters.json`, `scripts/build_scene.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_notes.md` and `01_report_00.md`

Before any mutation, verify:
1. `/Users/agile/Projects/kysucka_moderna_chata` is on `main` at `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, clean index/worktree, `origin/main` and public `refs/heads/main` equal to `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, `./.ap/ap doctor` exits `0` (`PASS`).
2. Protected and v01 SHA-256 values match `AGENTS.md`:
   - `blender/kysucka_chata_seed.blend`: `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`
   - `blender/kysucka_chata_mcp_v01.blend`: `227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8`
   - `reference/kysucka_chata_moderna.png`: `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`
   - `model/parameters.json`: `90a3bf95c9c51ea407ae1d749b481795733e88c083c07415ed0f58f916c6cc7a`
   - `scripts/build_scene.py`: `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`
3. New target files are absent before starting:
   - `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend` (and `.blend1`)
   - `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v02-before.blend` (and `work/mcp-v02-owner-checkpoint.blend`)
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/before.png`, `candidate_01.png`, `candidate_02.png`, `candidate_03.png`, `candidates_sheet.png`, `after.png`, `render_metadata.json`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/evidence/camera_comparison.md`
   - `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_01.md`

## Execution Route and Mutation Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` (headless CLI-only in `AGENTS.md` and `docs/OPERATIONS.md`), which cannot perform live MCP control of Michal's open Blender GUI session.
- **Activated route for this task**: `blender-mcp-live-v1` (live Blender MCP tool calls against the running Blender 5.2.3 LTS GUI for scene read, checkpoint/v02 save, camera candidate updates, readbacks, comparable 4:3 renders, image inspection, and GUI viewport configuration), supplemented by local CLI for Git, SHA-256 hashing, `./.ap/ap doctor`, macOS `/usr/bin/osascript` (or Python) for composing `renders/candidates_sheet.png`, and read-only cold-reopen verification of the saved `blender/kysucka_chata_mcp_v02.blend` via `scripts/inspect_scene.py`.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/02-reference-camera-perspective
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: blender/kysucka_chata_mcp_v02.blend, model/parameters.json, AGENTS.md, docs/OPERATIONS.md, README_SK.md (plus gitignored work/mcp-v02-before.blend, optional work/mcp-v02-owner-checkpoint.blend if dirty, and blender/kysucka_chata_mcp_v02.blend1)
Host/remote mutation: live Blender 5.2.3 LTS GUI session via local Blender MCP (save work/mcp-v02-before.blend, evaluate CAM_A_REFERENCE baseline and 3 candidates, render 640x480 before/candidate_01..03/after frames, save blender/kysucka_chata_mcp_v02.blend with canonical 1448x1086 settings and CAMERA+RENDERED viewport) and non-force git push of main to https://github.com/cisarik/kysucka_moderna_chata
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_01.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/before.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/candidate_01.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/candidate_02.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/candidate_03.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/candidates_sheet.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/after.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/render_metadata.json, /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/evidence/camera_comparison.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md

## Step-by-Step Implementation Envelope

### Stage 1: Live MCP Read, Baseline Checkpoint, and `renders/before.png`

1. **Initial MCP read and non-camera scene fingerprint**:
   - Via MCP (`get_scene_info` and `execute_blender_code`), verify `bpy.data.filepath` is `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend`, `is_saved == True`, `is_dirty == False`, `mode == 'OBJECT'`, `is_job_running('RENDER') == False`, `objects == 656`, `mesh_vertices == 13438`. (If `is_dirty == True`, save `work/mcp-v02-owner-checkpoint.blend` with `copy=True, compress=True` and stop for reconciliation.)
   - Compute and record compact SHA-256 fingerprints of all non-camera object transforms/mesh geometry, materials, lights, and world nodes so you can prove they remain 100% unchanged after camera updates.
2. **Create output directories and baseline checkpoint**:
   - Create `/Users/agile/Projects/kysucka_moderna_chata/work`, `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders`, and `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/evidence` if absent.
   - Set common 4:3 Cycles CPU comparison render settings (`resolution_x = 640`, `resolution_y = 480`, `resolution_percentage = 100`, `pixel_aspect_x = 1.0`, `pixel_aspect_y = 1.0`, `engine = 'CYCLES'`, `cycles.device = 'CPU'`, `cycles.samples = 32`, `cycles.use_denoising = False`, `cycles.seed = 0`, `cycles.use_animated_seed = False`, `frame_current = 0`, `view_settings.view_transform = 'AgX'`, `look = 'None'`, `exposure = 0.0`, `gamma = 1.0`, `film_transparent = False`).
   - Save `/Users/agile/Projects/kysucka_moderna_chata/work/mcp-v02-before.blend` (`copy=True, compress=True`), record its SHA-256, and verify `blender/kysucka_chata_mcp_v01.blend` and `blender/kysucka_chata_seed.blend` hashes are untouched.
   - Render `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/before.png` from unchanged `v01` (`location = [27.5, -15.5, 1.70]`, `target = [7.45, 3.15, 1.70]`, `lens = 50.0` mm, `shift_x = 0.0`, `shift_y = 0.075`). Verify the PNG decodes as `640 × 480` and matches the predecessor `after.png` (`bf5e95c925446a7c6a317e117f07ce80e4ac28ab79e379976412c8a814017801`) or record its exact SHA-256 and elapsed time.

### Stage 2: Evaluate Three Camera Candidates, Build `renders/candidates_sheet.png`, Select Winner, and Render `renders/after.png`

1. **Evaluate each of the 3 planned candidates via MCP (`read -> change -> separate readback -> projection measurement -> render`)**:
   - For each candidate below, set `cam.location = Vector(loc)`, `cam.rotation_euler = (Vector(tgt) - cam.location).to_track_quat('-Z', 'Y').to_euler()`, `cam.data.lens = lens`, `cam.data.sensor_width = 36.0`, `cam.data.shift_x = 0.0`, `cam.data.shift_y = shift_y` (calling `bpy.context.view_layer.update()`):
     - **`cand_01_35mm_balanced`** -> `renders/candidate_01.png`: `loc = [21.5, -10.0, 1.25]`, `tgt = [8.5, 2.5, 1.25]`, `lens = 35.0`, `shift_y = 0.105`
     - **`cand_02_32mm_wide_low`** -> `renders/candidate_02.png`: `loc = [20.5, -9.0, 1.15]`, `tgt = [8.5, 2.5, 1.15]`, `lens = 32.0`, `shift_y = 0.115`
     - **`cand_03_38mm_parallax`** -> `renders/candidate_03.png`: `loc = [25.5, -9.8, 1.25]`, `tgt = [7.8, 2.5, 1.25]`, `lens = 38.0`, `shift_y = 0.080`
   - For each candidate, perform a separate MCP readback of the camera transform/optics/shift and actual `world_to_camera_view` top-left UV coordinates for the 6 primary landmarks and 3 auxiliary probes, compute `facade_to_gable_ratio`, `eave_dv`, `vertical_envelope_span`, `fireplace_parallax`, `fence_right.u`, and the 5-landmark pixel RMSE `E`, then render its `640 × 480` 32-sample PNG.
2. **Create `renders/candidates_sheet.png` (`1280 × 1024` 2×2 comparison sheet)**:
   - Combine `before.png` (`v01 50mm`), `candidate_01.png` (`C1 35mm`), `candidate_02.png` (`C2 32mm`), and `candidate_03.png` (`C3 38mm parallax`) into a labelled 2×2 PNG at `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/candidates_sheet.png` using `/usr/bin/osascript` (AppKit) or Python.
3. **Apply selection rule and produce `renders/after.png`**:
   - Apply the accepted selection rule from `01_report_00.md` (`cand_01_35mm_balanced` is expected to win with lowest `E = 29.11 px` and closest `facade_to_gable_ratio = 2.2069` vs `2.1818` ref).
   - Set `CAM_A_REFERENCE` in the live scene to the winning candidate, perform a separate MCP readback confirming exact camera properties and unchanged non-camera scene fingerprints, and render `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/after.png` at the identical `640 × 480` 32-sample settings.
   - Inspect `reference/kysucka_chata_moderna.png`, `renders/before.png`, `renders/candidates_sheet.png`, and `renders/after.png` (including via MCP `look(image=...)`).

### Stage 3: Restore Canonical Settings, Save `blender/kysucka_chata_mcp_v02.blend`, and Verify Cold Reopen

1. **Configure GUI viewport and restore canonical render settings**:
   - In the live Blender GUI via MCP:
     - Ensure the Layout 3D Viewport is in `view_perspective = 'CAMERA'` (`CAM_A_REFERENCE`), `shading.type = 'RENDERED'`, `use_scene_lights = True`, `use_scene_world = True`, `use_scene_lights_render = True`, `use_scene_world_render = True`, `cycles.preview_samples = 16`.
     - Restore canonical output settings (`resolution_x = 1448`, `resolution_y = 1086`, `resolution_percentage = 100`, `cycles.samples = 96`, `render.filepath = '//../work/camera_a.png'`).
   - Save `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend` (`copy=False, compress=True`) as the active mainfile. Never overwrite `v01` or `seed`.
2. **Independent MCP readback and cold CLI reopen verification**:
   - Perform a separate MCP readback confirming `filepath` ends with `kysucka_chata_mcp_v02.blend`, `is_saved == True`, `is_dirty == False`, `is_job_running('RENDER') == False`, `objects == 656`, `mesh_vertices == 13438`, non-camera scene fingerprints unchanged, and `CAM_A_REFERENCE` matches the promoted candidate.
   - Run the read-only CLI inspection on the saved `v02` file:
     `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec /Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend --python-exit-code 2 --python /Users/agile/Projects/kysucka_moderna_chata/scripts/inspect_scene.py`
     and confirm exit code `0`, matching camera values, 656 objects, 13,438 vertices, and packed `REF_kysucka_chata_moderna`. Verify live MCP remains connected afterward.

### Stage 4: Source/Doc Sync, Meta Evidence, Run-Map Persistence, and Project Git Publication

1. **Update project files in `/Users/agile/Projects/kysucka_moderna_chata`**:
   - `model/parameters.json`: update only `camera.location`, `camera.target`, `camera.lens_mm`, and `camera.shift_y` to the promoted candidate's exact values (verify that `(Vector(cp['target']) - Vector(cp['location'])).to_track_quat('-Z', 'Y').to_euler()` matches the saved `CAM_A_REFERENCE.rotation_euler` within `1e-5`). Keep `scripts/build_scene.py` untouched (`4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`).
   - `AGENTS.md`:
     - Update the current working candidate description to `blender/kysucka_chata_mcp_v02.blend` (preserving historical initialization and MCP v01 SHA-256 tables and adding the current MCP v02 SHA-256 values for `model/parameters.json` and `blender/kysucka_chata_mcp_v02.blend`).
     - In `### Blender capability route`, note that for `kysucka-moderna-chata-reference-camera-perspective` the task-specific `blender-mcp-live-v1` route updates the working camera scene to `blender/kysucka_chata_mcp_v02.blend` while preserving `seed` and `v01`.
     - **CRITICAL**: Leave the managed AP block and the entire `### Closure and Git gates` section byte-identical.
   - `docs/OPERATIONS.md` and `README_SK.md`: narrowly update the Slovak working-file and camera notes to reference `blender/kysucka_chata_mcp_v02.blend` alongside the preserved `seed` and `v01`.
2. **Write Meta evidence and mechanically persist `00_RUN_MAP.md`**:
   - Write `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/evidence/camera_comparison.md` (in English) documenting baseline and C1/C2/C3 camera parameters, verified landmark UV and control tables, MCP read/change/readback receipts, why the chosen candidate improves perspective, and the measured fixed-geometry residuals (door X-position, eave-vs-transom height, fireplace-under-chimney parallax, fence line).
   - Write `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/renders/render_metadata.json` containing scene/camera identity, world matrix / euler / target, optics/shift, landmark UV and control metrics, render settings and elapsed times, Cycles CPU vs METAL preference classification, non-camera fingerprint hashes, cold-reopen output, and all artifact SHA-256 hashes.
   - Mechanically persist the exact Master-authored run-map snapshot from `00_handout.md` to `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`:
     ```text
     Run map: kysucka-moderna-chata-reference-visualization
     Run objective: converge the editable Blender scene toward reference/kysucka_chata_moderna.png; architectural checking is deferred
     Run map authority: discovery-only
     Run entry: 00 | kysucka-moderna-chata-ap-meta-initialization | closed | depends on: none | handout: projects/kysucka_moderna_chata/00/00-init/00_handout.md | evidence: completed project foundation at b47cce6f91ae10a22fb708a8e5220ab27b471aeb
     Run entry: 01 | kysucka-moderna-chata-blender-mcp-first-reference-render | closed | depends on: kysucka-moderna-chata-ap-meta-initialization | handout: projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_handout.md | evidence: public f0fb0ea25fcd091ff05e5e3717c433c586cac4fa, v01, MCP read/change/readback and supplied matching before/after renders; old archival gaps are classified separately
     Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | provisional | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: vertical framing is improved; Master selects a bounded actual-perspective comparison before changing materials/world
     ```
3. **Validation and Project Git Commit + Non-Force Push**:
   - Run `./.ap/ap doctor` in `/Users/agile/Projects/kysucka_moderna_chata` and confirm `PASS`.
   - Verify `git status --short` shows only the five allowed tracked paths (`AGENTS.md`, `README_SK.md`, `blender/kysucka_chata_mcp_v02.blend`, `docs/OPERATIONS.md`, `model/parameters.json`; `work/` and `*.blend1` remain gitignored).
   - Stage only the exact five paths:
     `git add blender/kysucka_chata_mcp_v02.blend model/parameters.json AGENTS.md docs/OPERATIONS.md README_SK.md`
   - Recheck `git diff --cached --stat` and confirm `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `reference/kysucka_chata_moderna.png`, and `scripts/build_scene.py` are untouched.
   - Commit on `main` (e.g. `feat: calibrate 3D camera perspective in mcp_v02 working scene`) with parent `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`.
   - Recheck `git ls-remote origin refs/heads/main` equals `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, push non-force (`git push origin main`), and verify public `refs/heads/main` equals your new commit SHA via `git ls-remote origin refs/heads/main`.

## Commands, Prohibitions, and Rollback

Commands:
- Blender MCP tools: `get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`.
- Local shell in `/Users/agile/Projects/kysucka_moderna_chata`: file reads/writes on allowed paths, `mkdir -p`, `shasum -a 256`, `/usr/bin/osascript`, `./.ap/ap doctor`, read-only `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec .../blender/kysucka_chata_mcp_v02.blend --python-exit-code 2 --python .../scripts/inspect_scene.py`, and exact-path Git commands (`git status`, `git diff`, `git add <exact-5-paths>`, `git commit`, `git ls-remote`, `git push origin main`).

Negative authority:
- Never modify or overwrite `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `reference/kysucka_chata_moderna.png`, `model/reference_landmarks.json`, `scripts/build_scene.py`, `scripts/design.py`, `cad/`, `docs/*.pdf`, `previews/`, `manifest/`, or `.ap/`.
- Never run `git add .`, `git add -A`, `git push --force`, `git reset --hard`, or `git clean`.
- Never run any Git write command (`git add`, `git commit`, `git push`, `git restore`, `git checkout`) inside `/Users/agile/meta`.
- Never install/update packages or add-ons (`uvx`, `pip`, `poetry`), alter MCP configuration, enable telemetry, or call external 3D/world/asset generators.
- Never quote or emit the literal project closure signal from `AGENTS.md`.

Rollback:
- If any checkpoint or render step fails, ensure no render job is running (`bpy.app.is_job_running('RENDER') == False`), restore `CAM_A_REFERENCE` and canonical `1448 × 1086` settings to `v01` values, preserve all checkpoints and partial evidence, revert uncommitted project edits, and report the exact causal blocker.

## Validation Ladder

Evidence tier: E2
Evidence tier basis: reversible 3-candidate camera perspective comparison, working-scene v02 creation, comparable 4:3 renders, and non-force public Git publication
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor` and read-only `scripts/inspect_scene.py` on `blender/kysucka_chata_mcp_v02.blend`
Affected tests: `./.ap/ap doctor`, `scripts/inspect_scene.py`, generator camera-orientation agreement assertion, and PNG image header/dimension + visual inspection on `before.png`, `candidate_01..03.png`, `candidates_sheet.png`, and `after.png`
New causal regression: none — verified directly via MCP readback, `scripts/inspect_scene.py`, and landmark/image comparison
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (live Blender 5.2.3 LTS GUI via MCP) + `blender-local-v1` read-only cold-reopen check
Independent acceptance: not-required (Orchestrator will independently inspect the live scene via MCP, the saved `v02` `.blend`, the rendered images, and the public Git commit)

## Completion and Report Contract

Write your complete terminal report directly to:
`/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_01.md`
and read back the entire file to verify exact content and first line before sending your short completion notice.

Begin `01_report_01.md` with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-reference-camera-perspective`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 02`

Include:
- `status: PASS` (or `PARTIAL`/`BLOCKED` if any required gate could not complete)
- `Phase-qualified result: implementation-PASS` (and report `publication-PASS` evidence in the publication section)
- `Start commit: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa` and `End commit: <new-40-hex-commit-sha>`
- `Report justification: new-mutation`
- `Logical-whole closure: not-closed`
- Concise summary of changed files, SHA-256 hashes (seed, v01, reference, `scripts/build_scene.py`, updated `model/parameters.json`, new `blender/kysucka_chata_mcp_v02.blend`, checkpoint `work/mcp-v02-before.blend`, `renders/before.png`, `candidate_01..03.png`, `candidates_sheet.png`, `after.png`, `render_metadata.json`, `evidence/camera_comparison.md`, and `00_RUN_MAP.md`), MCP read/change/readback receipts, landmark/ratio comparison table and residuals, `./.ap/ap doctor` and cold-reopen results, and public `origin/main` readback.
- `Orchestration critique` (`MEASURED` and `LEAD`), `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, and `Authority expiry`.
