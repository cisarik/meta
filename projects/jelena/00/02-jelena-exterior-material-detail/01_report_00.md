### Report for ORCHESTRATOR_CHAT

Logical whole identity: `jelena-exterior-material-detail`
Worker session ordinal: `01`
Worker exchange ordinal: `01`
Persistent role identity: WORKER
Worker session target: `fresh-worker-session`
Native planning mode: `required`
Worker session profile: Planner
Phase: Planning
Task identity: `JELENA-EXTERIOR-MATERIAL-DETAIL-PLAN`
status: PASS
Phase-qualified result: not-applicable
Start commit: `918d3db6b421048c85b25a7712bd40da6afb0660`
End commit: `918d3db6b421048c85b25a7712bd40da6afb0660`
Report justification: new-evidence
Logical-whole closure: not-closed

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and scene-grounded technical planning for exterior material and craft detail of the existing cabin and terrace
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with `Native planning mode: not-used`
Post-plan implementation session: `current-worker-session`
Maximum plan-only cycles: 1

No repository, host, Blender, or Git mutation was performed. Every path, setting, and sequence below is proposed, not performed. Cursor plan approval, Build, or a mode switch does not authorize implementation.

Delivery limitation: native Plan mode blocks the granted write of `/Users/agile/meta/projects/jelena/00/02-jelena-exterior-material-detail/01_report_00.md`. This text is the complete report. The file was absent at planning time. It was not written, and no other path was used.

## Repository gate

- Branch `main`. HEAD, parent, and tree match the grant: `918d3db6b421048c85b25a7712bd40da6afb0660`, parent `9d75587e39a97e4f26b106ef2d48a141515401dd`, tree `246bfc2a9aef98578a6950c7c722e2ec9cc78c20`.
- Index and worktree clean. Local `origin/main` is the same commit. Public `refs/heads/main` was not fetched; it remains the Orchestrator observation of `918d3db6b421048c85b25a7712bd40da6afb0660` on 2026-11-13.
- AP gitlink `.ap` = `d7023cf037f6d17885c3ede5c04812c61640da50`.
- Protected hashes rechecked and matched, including `Jelena/Jelena_Realistic_v003.blend` `e97fe7d745e2b5b0f8ce69ab85d8fc449dbd929e277ebc0bd566582844fedf3b` and `.local/renders/smreky-camera-a.png` `3956952b86a6b6a2246a13426949245aa9f6555c06901b148f356781881799e3`.
- `Jelena/Jelena_Realistic_v004.blend` is absent. Proposed working deliverable: that exact path.
- Run map `/Users/agile/meta/projects/jelena/00/00_RUN_MAP.md` is absent. Persistence limitation only. Do not create it.
- README SHA-256 `9130f50a439fba34ac39b087e72e1eed8528f01aa51097fa750534a173fb5f22`. Quick Start step 1 still says to open v001. Confirmed.

## Live scene identity

Cursor MCP `user-blender`, read-only, one successful connection. Addon `MCP for Blender` 1.8, protocol 15, Blender 5.2.3 LTS. The MCP server reports expected protocol 16 and says trajectory still works via fallbacks. Recorded, not changed. Libraries and generators are off. Telemetry consent false.

In-memory scene and the saved file agree:

- `bpy.data.filepath`: `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v003.blend`
- `is_dirty` false, `is_saved` true, mode OBJECT, frame 1
- Active scene `A • Chata pri lese`, active camera `A • Chata pri lese`, lens 46 mm, sensor fit AUTO, 36 × 24 mm, shift 0, clip 0.1–1000
- Camera world location `(13.9, -16.4, 6.35)`, rotation Euler XYZ `(1.390952, 0.0, 0.477129)` radians, scale 1. This matches `evidence/foundation-001/manifest.json` within the manifest's float noise.
- Scenes: A 870 objects, B `B • Zariadená dispozícia` 308 objects, 1031 unique objects, 147 shared, 723 only in A, 161 only in B
- 30 materials, 5 lights, 3 cameras, 931 meshes, no libraries, no image textures except viewer `Render Result`
- Saved render: Cycles, CPU, 1260 × 840, 100%, 80 samples, adaptive on, threshold 0.01, min samples 0, denoise off, denoiser OPENIMAGEDENOISE present but unused, seed 0, AgX, look None, exposure 0, gamma 1, display sRGB, film transparent off, PNG RGBA 8-bit, output `/tmp/`
- The historic PNG is 840 × 560, frame 1, 16 samples. It is context, not the new before image. Color management and device are not in that PNG.
- Idle sampled RSS of Blender PID 3187: 34064 KiB (0.03 GiB). This is not peak memory and not a render sample.
- The accepted PNG was inspected. At ordinary size the cabin reads as one orange timber color, the roof as a dark sheet, the terrace doors as washed glass, and the deck as a flat warm plane. Trees and saturated foliage stay out of scope.

Camera A is also linked into scene B. Do not move it.

## Ranked defects and ownership

The flat look has a measured cause. Facade and terrace shaders sample Texture Coordinate Object, multiply it, and run one FBM noise (scale 1, detail 3.4) through a narrow color ramp. The multiply on the facade is Object × `(10, 10, 0.47)`. Roughness is a constant 0.5. Bump strength is 0.13 and bump distance is 0.028 m. There is no per-object offset. Separate boards with the same local shape therefore repeat the same soft cloud. Across a 44 mm batten, Object × 10 spans only about 0.44 noise units, so the cloud never becomes grain.

1. Facade, largest impact. South face toward the camera: wall panels such as `Exterior_S_000` occupy Y `0.0–0.24`. Battens `Fasádna lata` sit proud of that face, Y `-0.0245–0.0005`, so they project about 24 mm. Pitch is 0.160 m, batten width 0.044 m, clear gap about 0.116 m. A 1.6 m pitch jump is the opening, not a missing board. Both the battens and the panels use `Fasáda • termodrevo`, so the gap does not read.
   - Battens: 210 in collection `01 • Import 3D | pôvodná geometria` plus 102 in `02 • Strecha a štíty`. Almost all are 25 × 44 mm in cross-section. Long local axis is Z on 219 of the collection-01 facade objects and on 102 gable battens. A minority of collection-01 pieces are long on X (8) or Y (4): horizontal trim.
   - Backing: about 21 larger `Exterior_*` meshes in collection 01, plus `Gable_S_029` and `Gable_N_030` (each 8.4 × 0.24 × 2.058 m, 6 vertices) in collection 02. These are single boxes or a gable slab, not individual boards.
   - Material users 491, fake user off, library none, one slot, scale 1, no modifiers. 453 meshes have `UVMap`; 38 have no UV. UVs are unused by the shader. Each mesh has one user.
   - Scene split of this material: 231 objects only in collection 01, 104 only in collection 02, 156 only in `08 • Len pre rez` (scene B). No facade object is in both scenes.
   - Class: shader-only. Do not split the gable, do not add boards, do not bevel the 8-vertex wall boxes.

2. Glazing, second. `Sklo • priehľadné` mixes a Principled BSDF (transmission weight 0, roughness 0.11, IOR 1.5, cyan-gray base) with a Transparent BSDF at factor 0.14. The mix is mostly transparent, so the pane has neither real transmission nor a readable reflection. Nine panes in `03 • Okná a dvere` are scene A only, 18 mm thick, no modifiers: `Terrace_glazing.006/.007/.008` (1.133 × 2.23 m at Y 0.108), `Bedroom_window.004`, `Kitchen_window.005/.006`, `Living_window.005/.006`, `Bathroom_window.004`. `Sprchová zástena` is in shared collection `04 • Nábytok a vybavenie` and is in both scenes. Leave it on the original material.
   - Class: shader-only, on the nine exterior panes.

3. Terrace and steps, third, and in the same pass because they are the foreground of camera A and share the same shader bug. Collection `06 • Terasa` is linked to both scenes. Its 51 objects are the same datablocks in A and B. Sixteen `Terasová doska` planks are 4.98 × 0.122 × 0.056 m at pitch 0.130 m, so the clear gap is 8 mm. They already have Bevel 0.004 m, 2 segments, and Weighted Normal. `Schod terasy` and `Schod terasy.001` are 2.4 × 0.28 × 0.11 m with bevel 0.01 m. `Vstupný schod` pair is on the far side. `Terasový stôl` and four legs use the same terrace material. `Rám terasy` is Antracit, 4.98 × 2.08 × 0.25 m. Chairs use `Interiér • prírodný dub`. One `Keramická miska.002` uses `Terakota`.
   - Material `Terasa • smrekovec`: same graph as the facade, ramp slightly lighter, users 25, all 25 objects in both scenes.
   - Class: shader-only on duplicated scene-A objects. No new plank geometry.

4. Roof, included because it is the remaining large surface and it is scene-A-only. `Strecha • falcovaný plech`: flat Principled, base `(0.033, 0.045, 0.046)`, metallic 0.62, roughness 0.36, no textures, 45 single-user meshes in collection 02. Geometry already exists: `Roof_031` and `Roof_032` sheets, 38 `Strešný falc` ribs about 33 × 29 mm × 5.03 m, 4 `Lem strechy`, 1 `Hrebeňáč`. Long local axis is X on 42 of 45. The uniform look is the shader, not missing seams.
   - Class: shader-only, in place, because scene B does not use this material.

Deferred, with reasons:

- Antracit frames, chimney (`Dymovod`, `Hlavica komína`), cables, and `Rám terasy`. Frames in collection 03 already have bevels about 8 mm and read as dark metal. The material is shared with the stove, tap, cabinet pulls, and four objects that also sit in collection 08. Editing it would change scene B.
- Terrace chairs and all `Interiér • prírodný dub`. Shared with the interior. Not required for the exterior gain.
- `Slab_027` (`Kameň`, 8.40 × 5.80 × 0.283 m) and `Floor_028`. Both are in scene A and scene B.
- Vegetation collections `05`, `05a`, `09`, `10`, node group `Pokryv lesa`, worlds, and all five lights.
- Tree errors, floating foliage, foliage saturation, and tree generation. Known limitations. They do not fail this whole.

## Recommended coherent scope

One pass, four shader targets, one object-duplication set:

- `Fasáda • lata • A` on scene-A objects named `Fasádna lata*`.
- `Fasáda • podklad • A` on scene-A `Exterior_*` and `Gable_*` that currently use `Fasáda • termodrevo`.
- `Sklo • exteriér A` on the nine collection-03 panes only.
- `Terasa • smrekovec • A` on the duplicated deck, steps, table, and table legs only.
- In-place roughness variation on `Strecha • falcovaný plech`.

Do not add geometry nodes, image textures, bevels, or new meshes in the first pass. The 24 mm batten projection and the 8 mm deck gaps are already the edges. A bevel is only the defined second refinement, and only on scene-A `Fasádna lata` objects, width 0.0008 m, segments 1, angle above 40 degrees. Never bevel `Exterior_*`, `Gable_*`, or the 29 mm standing-seam ribs.

First-pass shader targets, adjustable only inside these ranges during the two refinements:

- Batten grain: Object coordinate × a per-object vector. Short axes start at 90 (allowed 60–140). Long axis starts at 0.45 (allowed 0.25–0.80). The script sets custom property `grain_mul` from the longest local mesh axis so the 12 non-Z battens are not striped across their length. Object Info Random × 17 (allowed 8–30) is added as an offset. Roughness from the same noise, 0.42–0.70. Bump distance starts at 0.002 m (allowed 0.0015–0.004), strength 0.12 (allowed 0.08–0.16). Color stays inside the current ramp, from about `(0.115, 0.043, 0.018)` to `(0.37, 0.177, 0.074)`, with only that random offset. No stains, no second albedo pattern.
- Backing: constant color `(0.09, 0.035, 0.015)`, roughness 0.72, bump strength 0.04, distance 0.002 m. Darker and quieter than the battens so the existing 116 mm gaps read. No fake boards on the gable slab.
- Glass: one Principled BSDF, base `(0.85, 0.92, 0.90)`, metallic 0, roughness 0.04 (allowed 0.03–0.12), IOR 1.5, transmission weight 1, specular IOR level 0.5, coat 0. No Transparent mix. Meshes stay. Thickness is already 18 mm, so do not enable Thin Wall.
- Roof: keep base color. Metallic 0.72. Roughness from a broad Object-space noise between 0.32 and 0.48. No anisotropy unless refinement 1 shows the sheet is still a single value. Do not add ribs.
- Terrace copy: same grain method as the battens, using each duplicate's long local axis. Deck color stays in the current terrace ramp, from `(0.19, 0.088, 0.036)` to `(0.46, 0.247, 0.106)`. Existing bevels stay untouched.

If a refinement would need to leave these ranges or add geometry beyond the one defined bevel, stop and report.

## Scene B and baseline protection

Shared collections, measured: `04 • Nábytok a vybavenie` (84), `06 • Terasa` (51), `07 • Svetlá a kamery` (4), `07b • Svetlá exteriér` (2). Scene B also has `08 • Len pre rez` (167), which scene A does not.

Shared lights, not to be edited: `Popoludňajšie slnko` energy 2.2, angle 0.13, in both scenes; `Mäkké svetlo z čistiny` energy 610, size 8, in both scenes; `Svetlo v interiéri` energy 65. Scene A only: `Popoludňajšie slnko • A` energy 6.5 and `Mäkké svetlo z čistiny • A` energy 40. World A is `Obloha nad lesom • A`, background strength 0.5. World B is `Obloha nad lesom`, strength 0.48. No node groups are shared onto the facade.

Preservation method:

- Never edit the node trees of `Fasáda • termodrevo`, `Terasa • smrekovec`, `Sklo • priehľadné`, `Antracit`, or `Interiér • prírodný dub`.
- New facade and glass materials are assigned only to scene-A objects listed above. The 156 collection-08 objects and `Sprchová zástena` keep the originals.
- For the terrace, duplicate all 51 objects and their meshes into a new collection `06b • Terasa • scéna A`, linked only to scene A. Then exclude `06 • Terasa` on scene A's view layer only. Scene B keeps the original collection included. Duplicated chairs, the bowl, and `Rám terasy` keep their original materials. Only deck, steps, table, and table legs on the duplicates receive `Terasa • smrekovec • A`.
- Do not duplicate vegetation. Do not touch collections `05`, `05a`, `09`, `10`, cameras, lights, or worlds.
- Do not save over v003, v001, or `Jelena.blend`.

Pre-change and post-change readback, all must match before any commit:

- On-disk v003 SHA-256 still `e97fe7d745e2b5b0f8ce69ab85d8fc449dbd929e277ebc0bd566582844fedf3b`.
- Scene B object count 308. Scene B view layer still includes `06 • Terasa`. Scene A view layer excludes it and includes `06b • Terasa • scéna A`.
- Camera A location, rotation, lens, sensor, and shift as measured above. Camera B location `(12, -12, 13)`, lens 40. Camera C location `(7.67, 4.63, 1.55)`, lens 19.
- `Sprchová zástena` still uses `Sklo • priehľadné`. Collection 08 still uses `Fasáda • termodrevo`. `Slab_027` still uses `Kameň`.
- Light energies and world strengths unchanged. Collection `10 • Vegetácia scéna A` still has 93 objects.
- No new image datablocks. No library links.

`hide_render` must not be used on the original terrace objects, because that flag is global and would hide them in scene B. View-layer exclude is the scene-local gate.

## Paths, script, evidence, Git

Proposed paths:

- Working file: `Jelena/Jelena_Realistic_v004.blend`
- Pre-mutation checkpoint, filesystem copy of the clean saved v003, not a second Blender: `.local/checkpoints/Jelena_Realistic_v003-before-exterior.blend`. Verify its SHA-256 equals the v003 hash before any render setting change. No second checkpoint is required; the first risky stage is the in-memory material pass, and recovery before Save As is Navrátiť.
- Script: `scripts/exterior_material_v004.py`. One-shot. It must refuse to run unless the open file is v003 or, after Save As, v004; the active scene and camera are A; scene B has 308 objects; camera A matches the measured transform within 0.0001; and collection `06b • Terasa • scéna A` does not already exist. It is not safely rerunnable. Review is the diff in the later commit. Inline MCP code may call this script; the script is the reviewed source.
- Evidence directory: `evidence/exterior-004/`
  - `camera-a-before.png`
  - `camera-a-after.png`
  - `camera-a-detail.png`
  - `manifest.json`
  - `camera-a-presentation.png` only if the presentation condition below is met
- Iteration renders stay in `/tmp/` or are overwritten by the retained after image. Do not stage them.

`.gitignore` does not ignore `.local/`. The later grant must `git add` explicit paths only. Never `git add -A` and never add the checkpoint.

Manifest fields: camera, frame, resolution, samples, engine, device, adaptive sampling, threshold, min samples, denoise, denoiser, seed, view transform, look, exposure, gamma, display device, file format, color mode, depth, film transparent, output path, blend path, blend SHA-256, before/after/detail SHA-256, render duration, scene-B object count, collection-06 exclude state per scene, camera A/B/C transforms, light energies, world names and strengths, preservation checks, visual review, known limitations, sampled RSS, and a statement that sampled RSS is not peak memory.

Retained in Git after Michal accepts the images: v004, the script, the evidence directory files that were actually produced, and the README edit. The checkpoint and `/tmp` output are not retained. v003 and older evidence stay as they are.

README minimal edit, in the same commit as v004:

- In `## Súbory`, add one bullet: `Jelena/Jelena_Realistic_v004.blend` is the current working file; v003 remains the accepted predecessor.
- Quick Start step 1 becomes: open `Jelena/Jelena_Realistic_v004.blend` in Blender 5.2.3 LTS.
- In `## Stav`, add one sentence pointing at `evidence/exterior-004/` as the exterior before/after. Do not rewrite the vegetation history.

## Render budget

Matched before/after recipe, identical for both full frames:

- Scene A, camera A, frame 1, Cycles, device CPU. Do not switch to GPU.
- 840 × 560, 100%, samples 32, adaptive on, threshold 0.01, min samples 0, denoise on, denoiser OPENIMAGEDENOISE, seed 0, animated seed off.
- AgX, look None, exposure 0, gamma 1, display sRGB, film transparent off, PNG RGB 8-bit, no border, crop to border off.
- Before output: `evidence/exterior-004/camera-a-before.png`, rendered from in-memory v003 before the script.
- After output: `evidence/exterior-004/camera-a-after.png`.

The historic 16-sample 840 × 560 render took 15.89 s according to PNG metadata. A 32-sample frame is estimated at about 30–60 s. That is an estimate, not a new measurement.

After every evidence render, restore the saved working recipe before the next Save As: 1260 × 840, 80 samples, adaptive on, threshold 0.01, denoise off, PNG RGBA 8-bit, filepath `/tmp/`. v004 must open with that working recipe, not the preview recipe.

Detail view, one border render of the after state, same samples and color management, resolution 1260 × 840, `use_border` on, `use_crop_to_border` on, border `(min_x, max_x, min_y, max_y) = (0.28, 0.74, 0.02, 0.64)`. Those bounds cover the south battens, the three terrace panes, and the deck in camera-A NDC. Purpose: show grain, glass, and plank gaps at a larger pixel size. Restore border and resolution afterward. Output: `evidence/exterior-004/camera-a-detail.png`.

Presentation, optional, only if the after image passes the technical checks, sampled RSS stayed under 5.0 GiB, and fewer than two refinements were used. One render: camera A, 1260 × 840, 64 samples, adaptive on, denoise on, seed 0, same color management. Output: `evidence/exterior-004/camera-a-presentation.png`. It is not part of the matched pair.

Budget: one first pass and at most two targeted refinements. Maximum 6 renders: before, after, detail, refinement full frame, second refinement full frame, optional presentation. Wall-clock ceiling 25 minutes of render time. Do not start a render if sampled Blender RSS is already at or above 4.5 GiB. Stop the render sequence if a sample during or immediately after a render reaches 6.0 GiB. Sampled RSS is not peak memory. If the ceiling or the memory gate trips, keep the last complete matched pair and skip presentation.

## Acceptance

The matched pair demonstrates the same camera, light, and color management, with a fresher reading of timber, glass, deck, and roof. The detail crop shows batten-versus-backing contrast, glass that reflects and transmits, and deck gaps that already exist in the mesh.

Technical validation, separate from Michal's taste: visible difference at 840 × 560; grain running along battens and planks rather than a repeated cloud; backing visibly darker in the existing gaps; glass readable as glass on the three terrace doors; no new intersections, floating pieces, or obvious seams; camera A, vegetation, and scene B readback passed; sampled RSS stayed under 6.0 GiB; v004 saved and v003 hash unchanged.

Independent acceptance is not required. This is a reversible art change on a new file, with the original v003 and a checkpoint kept.

Numbered request for Michal, after the images exist:

1. Je fasáda na pohľade z kamery A presvedčivejšia ako jeden oranžový povrch, pri zachovanej skladbe latiek?
2. Čítajú sa terasové dvere ako sklo, nie ako vyblednutá fólia?
3. Majú dosky terasy a plech strechy dosť materiálu, bez novej výzdoby a bez zmeny lesa?
4. Môže ostať táto podoba ako `Jelena_Realistic_v004.blend`?

## Implementation sequence for the later grant

The later prompt must set `Native planning mode: not-used`, name this report as the continuity anchor, and grant checkpoint copy, temporary render-setting override, Save As to v004, the script, the evidence writes, the README edit, one ordinary commit, and one ordinary non-force push. Planning does not grant those actions.

1. Re-check the live file, dirty flag, scene, camera, and v003 hash. Stop if the session is dirty or is not v003 / scene A / camera A.
2. Copy the saved blend to the checkpoint path and verify the hash. Do not open a second Blender.
3. Apply the matched recipe, render the before image, restore the working recipe, and verify the on-disk v003 hash is unchanged. The memory image may now be dirty. Do not save v003.
4. Run the script. Read back scene B and the camera before Save As.
5. Save As `Jelena/Jelena_Realistic_v004.blend`. Confirm v003 on disk is unchanged.
6. Render the after image and the detail crop. Restore the working recipe and save v004 again.
7. Inspect the three images. At most two numeric refinements inside the ranges above, then re-render the after image. The bevel refinement is allowed only as refinement 2 and only if edges still fail.
8. Optional presentation under its condition.
9. Write the manifest from measured values. Stop if any preservation check fails; do not commit.
10. Show Michal the four numbered questions. Commit only after technical validation and his acceptance.

Changed-path allowlist for that commit:

- `Jelena/Jelena_Realistic_v004.blend`
- `scripts/exterior_material_v004.py`
- `evidence/exterior-004/camera-a-before.png`
- `evidence/exterior-004/camera-a-after.png`
- `evidence/exterior-004/camera-a-detail.png`
- `evidence/exterior-004/manifest.json`
- `evidence/exterior-004/camera-a-presentation.png` only if it exists
- `README.md`

Git scope to state in the later grant: one commit of those paths on `main`, then one ordinary non-force push, consistent with the standing Cooperator authorization. No fetch is required before the commit. Do not force-push, rewrite history, add LFS, or untrack `.local`.

Stop conditions for the later grant: dirty or wrong file at start; checkpoint hash mismatch; v003 hash changes; scene B count, shared materials, cameras, lights, or vegetation count drift; a render hits the memory or time ceiling; the script finds `06b` already present; an image shows new intersections or a broken silhouette. Terminal report after the commit and push, or earlier if a gate stops the work.

## Recovery

`Súbor → Navrátiť` reloads the current filepath. It does not open the checkpoint. Verified Slovak labels in this Blender locale `sk_SK`: Súbor, Otvoriť, Uložiť ako..., Navrátiť. `Render Image` stayed English in `pgettext`.

- Before Save As, if the script is wrong: `Súbor → Navrátiť`. That reloads v003 from disk. Then stop.
- After a bad v004 exists and v003's hash is still good: `Súbor → Otvoriť`, choose the checkpoint `.local/checkpoints/Jelena_Realistic_v003-before-exterior.blend`, then `Súbor → Uložiť ako...` only under a new grant if a replacement v004 is required. Do not Save over v003.
- If v003's hash changes, stop immediately. Do not continue, commit, or push. Recovery is a new grant that opens the checkpoint and writes it back only with an explicit overwrite decision.

## Risks

- Shared terrace objects: mitigated by duplication plus view-layer exclude. Detect by scene B still showing the old terrace material and by scene B count 308.
- Scene B facade drift: mitigated by never editing the original facade material. Detect by collection 08 still assigned to `Fasáda • termodrevo`.
- Glass too dark or mirror-like: refinement 1 may move roughness only inside 0.03–0.12. If that is not enough, stop.
- Grain scale wrong on horizontal battens: `grain_mul` is set from the measured long axis. Detect in the detail crop.
- Double terrace if exclude fails: detect by a z-fighting deck in the after image, then Navrátiť or reopen the checkpoint.
- Memory: idle RSS is not a forecast. The 4.5 / 6.0 GiB sampled gates are the control.
- Dirty live file or accidental save of v003: the hash gate stops the grant.
- Checkpoint accidentally committed: prevented by an explicit path allowlist.

## Editability

New materials are local procedural node trees, named as above. Duplicates stay as separate meshes with the existing bevels. No joins, no booleans, no baked maps, no absolute texture paths, no paid addon. The script is the reproducible source. Custom property `grain_mul` is visible on the batten objects.

Orchestration critique:
MEASURED: the connected MCP server expects addon protocol 16 while the live addon is 1.8 / protocol 15; scene queries still succeeded through the server's stated fallback. Effect: none on this plan. Smallest correction: do not update or reinstall the addon inside this whole.
MEASURED: `.gitignore` does not exclude `.local/`, while existing checkpoints are tracked by a prior decision. Effect: a broad `git add` would publish the new checkpoint. Smallest correction: the implementation grant must add explicit paths only.
LEAD: idle RSS of 0.03 GiB may under-represent render memory because of compression or an idle process. Cheapest check: sample RSS before and after the before-render, then apply the 4.5 / 6.0 GiB gates.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Changed files: none. The report file was not written.
Validation: repository hashes, cleanliness, and live read-only scene inspection. No render, save, or scene edit.
Git result: no fetch, stage, commit, or push.
Smallest next step: Orchestrator accepts or corrects this plan, then issues a separate implementation prompt with `Native planning mode: not-used`.
Authority expiry: this terminal report ends the planning grant. No autonomous continuation and no implementation follows from plan approval.
