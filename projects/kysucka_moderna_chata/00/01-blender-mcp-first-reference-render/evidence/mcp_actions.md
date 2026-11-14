# MCP actions — first reference-frame improvement

Author: assigned WORKER, session 01 / exchange 02. Evidence posture: non-independent.
Project baseline: `b47cce6f91ae10a22fb708a8e5220ab27b471aeb`; AP pin: `d7023cf037f6d17885c3ede5c04812c61640da50`.
Route: task-granted `blender-mcp-live-v1`. Tool `user_prompt` on every call: `Implement first useful reference-frame improvement through Blender MCP`.

## Actual tool receipts

| # | Tool | Observed action/result |
|---|---|---|
| 1 | get_addon_status | Blender 5.2.3 LTS; addon 1.8, protocol 15 / expected 16; native capabilities available; external libraries/generators off; telemetry false. |
| 2 | get_scene_info | Seed active; EDIT_MESH on APPLE_foliage_proxy.022; CAM_A_REFERENCE at (27.5, -15.5, 1.7). |
| 3 | execute_blender_code | initial live snapshot; read-only |
| 4 | execute_blender_code | save live owner checkpoint before mode change |
| 5 | execute_blender_code | flush Edit mesh, verify preservation, save active working file |
| 6 | execute_blender_code | independent working-file readback |
| 7 | execute_blender_code | measured 160x120 CPU probe, no PNG output |
| 8 | execute_blender_code | common 640x480 render settings and immutable baseline checkpoint |
| 9 | execute_blender_code | render comparable baseline before.png |
| 10 | execute_blender_code | authorized single-variable camera correction |
| 11 | execute_blender_code | independent readback of camera correction and unchanged scene invariants |
| 12 | execute_blender_code | save corrected working scene and render after.png |
| 13 | look | inspect actual corrected PNG through MCP |
| 14 | execute_blender_code | configure camera/scene-world GUI, restore canonical render settings, final save |
| 15 | execute_blender_code | independent final saved/live state verification |
| 16 | execute_blender_code | verify live GUI connection survived separate cold-reopen process |

## Read → change → independent readback

- Initial read: seed filepath, saved=true, dirty=true, active `APPLE_foliage_proxy.022` in `EDIT_MESH`; 42 active-mesh vertices; 656 objects / 13,438 mesh vertices.
- Owner checkpoint saved in Edit mode with `copy=True`; original live filepath and mode remained unchanged, and the seed SHA-256 remained unchanged.
- Object-mode conversion preserved the active mesh's coordinates, world bounding box and topology signature; all-scene geometry signature also matched. Save As made v01 the active file; a separate MCP read returned saved=true, dirty=false.
- Before render: 640 × 480, Cycles CPU, 32 samples, denoising=false, seed=0, frame=0, AgX / look=None / exposure=0 / gamma=1.
- Actual camera write: `bpy.data.objects['CAM_A_REFERENCE'].data.shift_y = 0.075` (the executed payload used the equivalent local alias `camera.data.shift_y=0.075`). Observed float values: `0.17000000178813934 → 0.07500000298023224`.
- A separate MCP execution then read the property and compared camera location/rotation/lens/sensor/shift_x, render settings, geometry, materials, lights, glass and world against the baseline. All invariants matched.
- Final read: active v01, saved=true, dirty=false, 656 objects / 13,438 vertices; camera view with RENDERED shading, scene lights/world enabled, preview_samples=16.
- The separate cold CLI check succeeded and a subsequent MCP read confirmed the live GUI connection remained healthy.

## Checkpoints and render receipts

| Artifact | SHA-256 |
|---|---|
| work/mcp-v01-owner-checkpoint.blend | 8ede94f62788f84014e17700e610a59eb41d9c09a4ead3aa699a3fb3c55cde70 |
| work/mcp-v01-before.blend | 24d7219a8440d64ba3eab2831fa5d026f45f1bf4451372069f35c1b5a58aa380 |
| blender/kysucka_chata_mcp_v01.blend | 227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8 |
| renders/before.png | 9a618128cf5e69f7af973a4acffbd036c125de6a5e0b03ce78836d23f05f4436 |
| renders/after.png | bf5e95c925446a7c6a317e117f07ce80e4ac28ab79e379976412c8a814017801 |

Probe: 160 × 120, 8 samples, 0.638998 s. The specified policy selected 32 samples. CPU remained the render device; METAL remained the system preference.
Before: 4.678322 s. After: 5.144120 s. Both synchronous calls returned FINISHED; is_job_running('RENDER') was false afterward.
Both PNGs passed signature, CRC, decompression/scanline-size and 640 × 480 dimension checks, and were visually decoded. No tracking handlers were needed.

## Executed mutation excerpts

These are verbatim operator/property lines from the recorded MCP executions; paths and aliases were asserted in those executions.

```python
result=bpy.ops.wm.save_as_mainfile(filepath=str(target),copy=True,compress=True)
assert 'FINISHED' in bpy.ops.object.mode_set(mode='OBJECT')
result=bpy.ops.wm.save_as_mainfile(filepath=str(target),copy=False,compress=True)
s.render.resolution_x=160;s.render.resolution_y=120;s.render.resolution_percentage=100
s.cycles.samples=8;s.cycles.use_denoising=False
result=bpy.ops.render.render(write_still=False)
s.render.resolution_x=640;s.render.resolution_y=480;s.render.resolution_percentage=100
result=bpy.ops.render.render(write_still=True)
camera.data.shift_y=0.075
space.camera=s.camera
space.region_3d.view_perspective='CAMERA'
space.shading.use_scene_lights=True;space.shading.use_scene_world=True
space.shading.use_scene_lights_render=True;space.shading.use_scene_world_render=True
space.shading.type='RENDERED'
s.cycles.preview_samples=16
s.render.resolution_x=1448;s.render.resolution_y=1086;s.render.resolution_percentage=100
s.cycles.samples=96;s.render.filepath='//../work/camera_a.png'
```

## Visual inspection

The after frame moves the cottage upward by approximately 60.8 pixels at 640x480. The roof ridge and chimney crown retain clear top margins. Both renders show the pendant/dining interior through the gable glazing and a procedural grey-blue sky.
At the unchanged 4:3 aspect, the shift difference predicts 60.8 px upward movement. Read-only projection places the gable peak at top-left UV approximately (0.8611, 0.1249), versus the original 0.2516 vertical coordinate and the approximate reference annotation 0.0875.
This is a vertical-framing improvement only. Proxy geometry/landscape, sky appearance, horizontal framing, fireplace visibility and low-sample noise remain; no visual acceptance is claimed for Michal.

## Replay and rollback

- Replay requires a new complete grant, verified repository/scene identity, collision-free output paths, and preservation of any current owner work.
- Use the immutable before checkpoint as the visual baseline; save a separately granted working copy. Reuse the comparison settings in render_metadata.json, render shift 0.17, apply only shift 0.075 through MCP, perform a separate readback, then render again.
- model/parameters.json now records 0.075 and the unchanged generator already reads that field. Keep live-owner geometry in its checkpoint; regeneration requires explicit reconciliation of accepted scene/source versions.
- Restore canonical 1448 × 1086 / 96-sample output and //../work/camera_a.png before saving a final working scene. GUI uses camera view, rendered Cycles, scene lights/world and 16 preview samples.
- Recovery, only when idle and without intervening owner changes: use the before checkpoint for correction rollback, or the owner checkpoint for the original Edit-mode state. Preserve evidence and checkpoints; never overwrite the seed.

Full measured states, scene fingerprints, file hashes, cold-reopen stdout and PNG validation results are in `../renders/render_metadata.json`.
