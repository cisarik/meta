# Plan 3D camera perspective calibration through Blender MCP

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-reference-camera-perspective
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BLENDER-MCP-REFERENCE-CAMERA-PERSPECTIVE-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded technical planning for a 3-candidate 3D camera perspective comparison using established Orchestrator MCP grounding
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: concise repository- and live-MCP-grounded technical plan specifying the target perspective discrepancies and comparison controls, at most three purposeful camera candidates, and exact source/scene/checkpoint/output/acceptance scope for v02
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

Produce a concise, decision-complete technical implementation plan for the logical whole `kysucka-moderna-chata-reference-camera-perspective`.

Accepted Cooperator and project decisions:
- Starting from the accepted v01 working scene (`blender/kysucka_chata_mcp_v01.blend` at commit `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`), improve the cottage's **actual 3D camera perspective** (`CAM_A_REFERENCE` location/height, look target/orientation, focal length `lens_mm`, and `shift_y`) against `reference/kysucka_chata_moderna.png`, keeping all building geometry, interior objects, materials, glass, world, lights, and landscape strictly unchanged.
- In `01/02` implementation, the Worker will compare the preserved `v01` baseline (`renders/before.png`) against at most **three** purposeful camera candidates at matched cheap 4:3 Cycles CPU preview settings (`640 × 480`, 32 samples, denoising off, `AgX`, exposure `0.0`, gamma `1.0`), produce a labelled candidate comparison sheet and the chosen camera's final comparison render (`renders/after.png`), save the chosen reopenable scene as `blender/kysucka_chata_mcp_v02.blend`, sync `model/parameters.json` (and narrow v02 references in `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`), and record `evidence/camera_comparison.md` and `renders/render_metadata.json` (plus mechanical persistence of the Master run-map snapshot at `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`).
- Communicate with the Cooperator in Slovak if addressing him directly; write your formal Worker report in English starting with `### Report for ORCHESTRATOR_CHAT`.
- **Important anti-stall constraint**: Do **not** print, quote, propose, or reproduce the project's literal Orchestrator-owned closure signal anywhere in your plan or report. Keep the existing `Closure and Git gates` section of `AGENTS.md` untouched. Do not request full replacement governance text, a broad audit, new infrastructure, or another full-scene inventory.

## Repository and Environment Prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Baseline: `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa` (`feat: create MCP working scene and refine camera framing`)
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap` (pinned submodule checkout; detached HEAD equal to gitlink accepted)
Trace repository: `https://github.com/cisarik/meta.git` at `/Users/agile/meta` (HEAD `4db94c333340c6b77d06701d050de286c701dabc`; preserve all unrelated work and predecessor files untouched)

Mandatory reading:
- `.ap/AP.md` (Semantic Authority and WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-04, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#planning-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `model/parameters.json`, `model/reference_landmarks.json`, `scripts/build_scene.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/01_closure.md`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md` and `00_notes.md`

## Established Orchestrator MCP & Projective Grounding (Reuse Directly)

The Orchestrator has already verified the repository baseline (`f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`), `./.ap/ap doctor` (`PASS`), all protected S00 and v01 SHA-256 hashes, and the live Blender 5.2.3 LTS session via MCP (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, and `look(mode="camera", shading="solid", max_size=640)`):

1. **Live Blender session state**:
   - Open file: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend` (`is_saved: True`, `is_dirty: False`, `is_job_running('RENDER'): False`).
   - Scene `'Scene'`: `656` objects, `13,438` mesh vertices, active object `APPLE_foliage_proxy.022` in `OBJECT` mode.
   - `CAM_A_REFERENCE`: `location = [27.5, -15.5, 1.7]`, `target = [7.45, 3.15, 1.7]` (`rotation_euler = [1.570796, -0.0, 0.821558]`), `lens = 50.0` mm, `sensor_width = 36.0` mm, `shift_x = 0.0`, `shift_y = 0.075`.
   - Note on `look`: the active Layout viewport is in `RENDERED` shading with Cycles; if calling `look(mode="camera")`, pass `shading="solid"` (or `image=...`) because `look` cannot capture Cycles `RENDERED` viewport shading directly.
2. **Projective analysis of `v01` vs `reference/kysucka_chata_moderna.png` (top-left UV `u = x/width, v = 1 - y/height`)**:
   - **Telephoto vertical & depth compression (`50 mm` at `~25 m` distance, `Z_cam = 1.70 m`)**:
     - In `v01`, `left_front_eave` `(-0.55, -0.85, 2.40)` projects to `(0.1187, 0.5575)` (2.8% higher than reference `(0.1195, 0.5856)`), while `gable_peak` `(14.95, 4.20, 7.45)` projects to `(0.8611, 0.1290)` (4.2% lower than reference `(0.8605, 0.0875)`). Thus the vertical span `left_front_eave.v - gable_peak.v` is only `0.4285` in `v01` vs **`0.4981`** in the reference—a perspective depth ratio difference that vertical shift (`shift_y`) alone cannot solve.
     - Similarly, the long front roof eave (`Z = 2.40 m`) is only `0.70 m` above `Z_cam = 1.70 m`, yielding a nearly flat upward slope from left to right (`eave_dv = left_front_eave.v - gable_front_eave.v = +0.0252` in `v01`), whereas moving closer (`~12–15 m`) with a wider lens (`32–40 mm`) and lower camera height (`Z_cam = 1.15–1.30 m`, keeping `target.z = location.z` so verticals remain strictly upright) increases `eave_dv` by **2.2x to 3.3x** (`+0.055` to `+0.083`) and expands the near gable vertically so `left_front_eave.v` (`~0.57–0.58`) and `gable_peak.v` (`~0.085–0.095`) match the reference simultaneously.
   - **Entrance facade vs glazed gable apparent width ratio**:
     - In `v01`, `gable_near_base` `(14.4, 0.15, 0.45)` is at `u = 0.6740` (vs `0.6996` in reference), giving `facade_u_span = 0.5553`, `gable_u_span = 0.2824`, and `facade_to_gable_ratio = 1.966` (vs **`2.184`** in the reference where `facade_u_span = 0.5801` and `gable_u_span = 0.2659`). Adjusting the camera azimuth slightly toward the entrance facade brings `gable_near_base.u` to `~0.692–0.700` and `facade_to_gable_ratio` to `~2.12–2.27`.
   - **Interior fireplace parallax vs facade/gable ratio trade-off**:
     - In the fixed S00 geometry, `FIREPLACE_stone` `(11.3, 3.2, 1.7)` is vertically aligned under `CHIMNEY_shaft` (`X = 11.3, Y = 3.2`), which is `3.1 m` left of the glazed gable plane (`X = 14.4`) and behind the solid front wall (`Y = 0..0.3`).
     - In `v01`, `fireplace_front_center` `(11.3, 2.8, 1.4)` projects to `u = 0.6351`, which is `0.0418` left of `mullion_0.15` (`u = 0.6769`) behind the solid front wall.
     - For a camera ray from `(xc, yc)` to `(11.3, 2.8)` to pass to the right of `(14.4, 0.15)` into the glazed gable, `(xc - 14.4) / (0.15 - yc)` must exceed `3.1 / 2.65 = 1.17` (or `> 1.02` for `(11.3, 3.2)`), which requires swinging the camera toward `+X` (e.g. `loc ~ [25.5, -9.8, 1.25]`), shifting `gable_near_base.u` left to `~0.63` and reducing `facade_to_gable_ratio` to `~1.30`.
   - **Fixed-model geometry residuals (must not be overfitted or blamed on camera)**:
     - In S00, the 45° roof continues over a `0.85 m` eave overhang to `Z = 2.40 m`, whereas `GABLE_horizontal_transom` is at `Z = 3.18 m`; in the reference image the eave soffit meets the gable near the transom height (`v = 0.4392`).
     - In S00, `D01` is at `X = 7.875 m` (`54.7%` of `14.4 m`), which under perspective foreshortening always projects around `u ~ 0.37–0.41` rather than the reference's `u = 0.493`.
     - In S00, the foreground fence runs along `Y = -5.78` from `X = -1.5` to `X = 16.8`.

## Questions Your Plan Must Answer (Concise and Decision-Complete)

Perform one brief read-only MCP verification call (`get_scene_info` or a short read-only `execute_blender_code`) to confirm your session's live MCP connection to `blender/kysucka_chata_mcp_v01.blend`, then answer **only** these three questions:

1. **Target perspective discrepancies & comparison controls**:
   - Define the exact verified landmark set (`6–8` 3D points with normalized top-left `(u, v)`) and the `4` key perspective/ratio controls (`facade_to_gable_ratio`, `eave_dv = left_front_eave.v - gable_front_eave.v`, `vertical_envelope_span = left_front_eave.v - gable_peak.v`, and `fireplace_parallax = fireplace_front_center.u - mullion_0.15.u` plus `fence_right.u`) that will score the baseline and candidates, explicitly distinguishing camera-solvable perspective relationships from fixed S00 geometry hypotheses.
2. **At most three purposeful camera candidates & selection rule**:
   - Specify the exact parameters (`location`, `target` with `target.z = location.z`, `lens_mm`, `sensor_width_mm = 36.0`, `shift_x = 0.0`, `shift_y`) and analytic `(u, v)` / ratio predictions for **three** purposeful camera candidates to render at matched `640 × 480` 32-sample Cycles CPU preview settings alongside `v01` (`renders/before.png`), e.g.:
     - **Candidate 1 (`cand_01_35mm_balanced`)**: `35 mm` closer/lower architectural view (`loc = [21.5, -10.0, 1.25]`, `tgt = [8.5, 2.5, 1.25]`, `shift_y = 0.105`) balancing the outer envelope (`left_front_eave`, `gable_near_base`, `gable_far_base`, `gable_peak`, `chimney_top`), `facade_to_gable_ratio ~ 2.21` (ref `2.18`), `vertical_envelope_span ~ 0.485` (ref `0.498`), and `eave_dv ~ +0.068` (2.7x v01).
     - **Candidate 2 (`cand_02_32mm_wide_low`)**: `32 mm` wider/lower view (`loc = [20.5, -9.0, 1.15]`, `tgt = [8.5, 2.5, 1.15]`, `shift_y = 0.115`) maximizing eave convergence (`eave_dv ~ +0.083`, 3.3x v01) and matching `vertical_envelope_span = 0.497` (ref `0.498`).
     - **Candidate 3 (`cand_03_40mm_moderate` or `cand_03_38mm_parallax`)**: either a `40 mm` moderate perspective (`loc = [23.25, -11.75, 1.30]`, `tgt = [8.25, 2.5, 1.30]`, `shift_y = 0.095`) or a `38 mm` gable-parallax test (`loc = [25.5, -9.8, 1.25]`, `tgt = [7.8, 2.5, 1.25]`, `shift_y = 0.080`) testing the fireplace-parallax vs facade-ratio trade-off.
   - State the exact selection rule for promoting one candidate to `renders/after.png` and `blender/kysucka_chata_mcp_v02.blend` (and the stop/decision rule if no candidate improves on `v01`).
3. **Exact source, scene, checkpoint, output, and acceptance scope**:
   - Specify the exact project changed-path allowlist (`blender/kysucka_chata_mcp_v02.blend`, `model/parameters.json`, `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`), gitignored checkpoints in `work/` (`work/mcp-v02-before.blend`, plus `work/mcp-v02-owner-checkpoint.blend` if dirty), Meta outputs in `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/` (`renders/before.png`, `renders/after.png`, `renders/candidates_sheet.png` and/or `renders/candidate_01.png`..`03.png`, `renders/render_metadata.json`, `evidence/camera_comparison.md`, `01_report_01.md`, plus `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`), generator agreement check (`scripts/build_scene.py` camera orientation formula `(Vector(cp['target']) - cam.location).to_track_quat('-Z', 'Y').to_euler()`), canonical scene restoration (`1448 × 1086`, 96 samples, `//../work/camera_a.png`, `CAMERA` + `RENDERED` 16-sample viewport), cold CLI reopen check, and rollback steps.

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection without MCP), which cannot perform live MCP inspection/control of the open Blender 5.2.3 LTS GUI session required by this logical whole.
- **Activated route for this task**: `blender-mcp-live-v1` using the session's exposed Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) connected to the running Blender 5.2.3 LTS GUI, supplemented by read-only local Git/file/hash inspection.
- **Evidence class**: directly observed MCP tool receipts and read-only repository/hash checks.
- **Bounded planning authority**: strictly read-only MCP observation and read-only local repository inspection, plus writing your terminal report `01_report_00.md`.

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
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md

Positive authority:
- Read-only inspection of `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta/projects/kysucka_moderna_chata/00/`.
- Read-only Blender MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code` printing JSON/text without modifying `bpy.data` or `bpy.context.scene`, and optional `look` with `shading="solid"` or `image=...`).
- Direct creation of the terminal report at `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md` if and only if that file is absent, followed by full readback verification.
- **Client completion route for Native Plan Mode (P4)**: If active Native Plan Mode blocks direct file writes during planning, keep the complete standard terminal report (`### Report for ORCHESTRATOR_CHAT` ...) in your session output and write `01_report_00.md` once the client permits within this same grant without implementing; if the client does not permit the write at all in Plan Mode, return the complete standard report in-session with `status: PARTIAL` (noting only the native Plan Mode write restriction) so the Orchestrator can persist the exact returned bytes to `01_report_00.md` under AP's completion route without another planning cycle.

Commands:
- Read-only file reads, `git status`, `git rev-parse`, `shasum -a 256`, `./.ap/ap doctor`.
- Read-only Blender MCP tool calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, `look`).
- Native file write for `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md` only.

Git authority:
- Read-only in both `/Users/agile/Projects/kysucka_moderna_chata` and `/Users/agile/meta`. No `git fetch`, `git add`, `git commit`, `git push`, `git checkout`, `git reset`, or `git clean`.

Dependency, network, and secret authority:
- Dependency authority: none (no package, add-on, `uvx`, `pip`, or runtime installation/update).
- Network authority: localhost Blender MCP socket only; no external network, asset downloads, or paid generators.
- Secret authority: none.
- Side-effect authority: read-only inspection of repository and live Blender MCP state, plus direct write of `01_report_00.md`.

Negative authority:
- Do NOT mutate any file in `/Users/agile/Projects/kysucka_moderna_chata` during planning.
- Do NOT mutate the live Blender scene, change camera/material/world values, save `.blend` files, or trigger `bpy.ops.render.render()` during planning.
- Do NOT install or update `mcp-for-blender`, modify client MCP config, change telemetry settings, or call `generate_3d` / `generate_gaussian_world` / `import_asset`.
- Do NOT quote, print, or reproduce the literal project closure signal from `AGENTS.md`.
- Do NOT touch unrelated files in `/Users/agile/meta`.

## Validation and Stopping Conditions

Evidence tier: E2
Evidence tier basis: cross-cutting reversible live-scene camera comparison and repository workflow with MCP read/change/readback and visual render artifacts
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: none (read-only planning phase)
New causal regression: none — planning phase specifies the bounded 3-candidate camera comparison and verifies read-only MCP connectivity
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (read-only observation in planning)
Independent acceptance: not-required

Validation in this planning task:
1. Verify repository root, branch `main`, HEAD `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, clean status, and the protected S00 and v01 SHA-256 hashes.
2. Perform at least one read-only Blender MCP tool call confirming live connection to the open `kysucka_chata_mcp_v01.blend` scene without changing `bpy.data.is_dirty` (`False`) or scene objects.
3. Verify that your plan answers all three required questions concisely and names exact paths, candidate camera parameters, mutation axes, and rollback for implementation.
4. If direct write is permitted by your client, verify `/Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md` is absent before writing, write the complete report, and read it back completely.

Stopping conditions:
- Stop immediately if repository identity, baseline commit, or source hashes disagree with this grant.
- Stop and report `BLOCKED` if Blender MCP tools are unavailable in your session (do not substitute headless CLI or attempt installation/reconfiguration).
- Stop after submitting your terminal planning report; planning authority expires at the report (`Plan-to-Execution Gate`).

## Completion and Report Contract

Begin your report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-reference-camera-perspective`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 01`

Include the compact core (`status: PASS` if plan + direct write succeed, or `status: PARTIAL` if the plan is complete and only Native Plan Mode blocked the file write; `Phase-qualified result: not-applicable`; `Start commit` and `End commit`: `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`). Keep the report concise (under ~200 lines) and decision-complete.
