# Implementation 01/03 — Jelena paved access and gravel parking

Delivery marker: **TEN ISTÝ CHAT**
Actual client mode: **Cursor Agent mode; native Plan mode OFF** (`not-used`)
Persistent role identity: WORKER
Worker session profile: Implementation Worker (current-session renewal)
Phase: Implementation
Task identity: `JELENA-ACCESS-PATH-GRAVEL-PARKING-IMPLEMENTATION`
Delivery route: manual Cooperator delivery
Reasoning recommendation: **High** — the execution must build terrain-conforming paving, a road, gravel parking, a grass mask, shared-datablock-safe collection changes and matched renders on an 8 GB machine. The named risks are shared-datablock damage, tree clearance, grass penetration, scene-B drift and render-budget pressure.
Recommended context capacity: approximately 250k tokens — a recommendation, not observed telemetry or a token cap.
Requested model: Michal's current Cursor model selection; routing is Cooperator-owned, and effective model identity and reasoning enforcement are unverified.

Continuity anchor: the accepted plan report `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_01.md` and the frozen planner artifact from Worker exchange `01` under `01_planning_00.md`.
Authority renewal: prior planning and completion authority expired at the terminal `01_report_01.md`; this exchange grants complete bounded implementation authority.
Why current-session reuse: the same healthy session holds the accepted plan, measured scene inventory and preservation context; independence is not required for this reversible visualization.
Retained context: convenience, not authority. Re-gate the repository and live scene from current evidence. Stop on conflict between retained context and current evidence.
Evidence posture: non-independent implementation evidence.

```text
Logical whole identity: jelena-access-path-and-gravel-parking
Worker session ordinal: 01
Worker exchange ordinal: 03
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: commit b70f242169b8173d0af5b660dcf1c9f00181449a; Jelena/Jelena_Realistic_v004.blend SHA-256 00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa
Changed-path allowlist: Jelena/Jelena_Realistic_v005.blend; scripts/access_landscape_v005.py; evidence/access-005/camera-a-before.png; evidence/access-005/camera-a-after.png; evidence/access-005/overview.png; evidence/access-005/camera-a-detail.png; evidence/access-005/camera-a-terrace-detail.png; evidence/access-005/manifest.json; README.md; .local/checkpoints/Jelena_Realistic_v004-before-access.blend (untracked checkpoint, never staged)
Implementation boundaries: one coherent access landscape in scene A only; preserve the accepted cabin, terrace, furniture, steps, Camera A, lighting, trees, scene B and all protected baselines; no tree moves or removals; no whole-scene vegetation regeneration; no external assets
Independence required: no
```

## Accepted plan and corrections

The accepted plan is `01_report_01.md`. Follow it except for the five Orchestrator corrections below. The corrections are mandatory and take precedence over the plan text where they differ.

1. **Tree clearance.** The `0.70 m` trunk-to-edge target applies to the new road, parking and path B. For path A, do not rely on the object origin or a nominal trunk radius. Measure the actual geometry of `Smrek • stredný.021` near the path surface: select its vertices in a z band from the path surface to `+0.30 m` and within the path-A bounding box expanded by `0.10 m`. Assert that no such vertex lies inside the paver footprint and that the minimum horizontal distance from the paver edge to any such vertex is at least `0.10 m`. If the assertion fails, stop and report the exact clearance and vertices; do not move, hide or remove the tree. The reported `0.24 m` edge-to-origin is not accepted as proof of clearance.
2. **Terrace evidence.** The 840 × 560 overview is too wide to judge the `100 mm` terrace riser. Produce a separate `camera-a-terrace-detail.png` framed on the terrace steps and the first `0.6 m` of path B. The riser and paver-to-step contact must be judged on that image, not on the overview alone.
3. **Parking dimensions.** Place the excluded proxy car at `(8.30, -10.65)`, yaw `0`, size `4.50 × 1.80 × 1.50 m`. This gives a `0.55 m` north standing strip and a `0.25 m` south strip. Set the wheel-wear strip centres to `1.50 m` apart, matching the `1.80 m` car body, not `1.35 m`.
4. **Paver edge.** Trim or cut the paver field at both curved path edges, or add a flush border course. No paver may extend outside the path half-width by more than `5 mm`; no gap between the edge pavers and the `Obruba • betón` edge may exceed `5 mm`. The visible edge must be continuous and flush; no raised kerb.
5. **Manifest and side-path ending.** Add SHA-256 for every evidence image to the manifest. The side path must end with a deliberate flush edge or soil/gravel transition, not a raw paver edge in grass. Judge it in the side detail and overview. `README.md` remains the only documentation change.

The plan’s rendering note about the first/last `0.60 m` is accepted as written: the reveal eases from `70 mm` to `12 mm` over the **last** `0.60 m` of path B at the gravel, not the first `0.60 m` at the terrace. The terrace paver top remains `-0.295` against the lower tread `-0.195`, a `100 mm` riser.

## Baseline and live state

Repository identity: `https://github.com/cisarik/jelena`
Working directory: `/Users/agile/Projects/jelena`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `b70f242169b8173d0af5b660dcf1c9f00181449a`
Expected parent: `918d3db6b421048c85b25a7712bd40da6afb0660`
Governing AP: `https://github.com/cisarik/ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`
Public `refs/heads/main`: Orchestrator-observed as `b70f242169b8173d0af5b660dcf1c9f00181449a` on 2026-11-13. Do not fetch before implementation. Post-push readback is authorized below.

Live state at Orchestrator issuance, 2026-11-13 after the Blender freeze and recovery:

- `bpy.data.filepath`: `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v004.blend`
- `bpy.data.is_dirty`: `false`
- Active scene: `A • Chata pri lese`; active camera: `A • Chata pri lese`; frame 1
- Scene A: 923 objects; scene B `B • Zariadená dispozícia`: 308 objects; 1,084 total objects
- Blender `5.2.3 LTS`; addon `MCP for Blender` 1.8; protocol 15; expected protocol 16. Leave the addon untouched.
- `Jelena/Jelena_Realistic_v005.blend` absent; `.local/checkpoints/Jelena_Realistic_v004-before-access.blend` absent
- The three predecessor checkpoints remain untracked: `Jelena_Realistic_v003-before-exterior.blend`, `Jelena_Realistic_v004-before-facade-correction.blend`, `Jelena_Realistic_v004-before-facade-cladding-correction.blend`
- The four v002 checkpoint files are tracked and unmodified; do not stage them.

These are Orchestrator observations, not authority to skip re-gating. Re-verify before any mutation. If the live file is not exactly `v004`, is dirty in an unexplained way, is not scene A with camera A, or the object counts differ, stop and report.

One live Blender instance and one mutating Worker. No background Blender, second instance, process termination, reinstall, addon update or host reconfiguration. Preserve unsaved owner work. The earlier freeze lost no saved state; do not repeat a blocking full-mesh Python loop.

## Goal and one coherent outcome

Build one editable scene-A arrival landscape in `Jelena/Jelena_Realistic_v005.blend`:

```text
forest road -> gravel parking / arrival area -> paved path B -> terrace steps
                                      \-> secondary paved path A -> entry steps
```

The primary pedestrian route is path B from `Schod terasy.003` to the gravel pull-off and road. Path A replaces the existing east side run in place and ends at its last stone; it does not join path B or the road. Both original stone runs are replaced and reversibly excluded. The result must read as a restrained forest-cabin arrival, not a suburban driveway.

This is implementation, not planning. Do not reopen the plan, redesign the layout, move Camera A, move trees, change the cabin/terrace/furniture, or start an interior or tree pass.

## Accepted layout summary

Use the plan’s measured coordinates and the following exact values.

Terrain: `Lesná čistina`, 62 × 58 m, z range about `-0.706..0.024`; metric, scale 1.

Forest road, proposed:

- Centerline: `(-6.3, -10.0)`, `(-3.0, -13.1)`, `(1.0, -13.3)`, `(15.0, -13.3)`, `(17.0, -10.5)`.
- Constant width `3.00 m` from x `1.0` to `15.0`; north edge y `-11.8`, south edge y `-14.8`.
- Outer legs taper to `1.00 m` at the tips. No trunk is moved.
- Road surface follows the terrain with a `12 mm` crust, feathered to `0` at the tips and outer `0.25 m`.

Parking:

- Gravel stall x `5.60..10.60`, y `-11.80..-9.20`; plus `2.4 m` tapers along the road from x `3.20..5.60` and x `10.60..13.00`.
- Stall `5.00 × 2.60 m`; one compact car `4.50 × 1.80 × 1.50 m`.
- Excluded proxy `Proxy • auto` at `(8.30, -10.65)`, yaw `0`; north standing strip `0.55 m`, south strip `0.25 m`.
- Wheel-wear strips `0.28 m` wide with centres `1.50 m` apart; stronger on the stall, faded over the last `3 m` of each tip. No asphalt, paint, gates, fences, sheds, signs or vehicle asset in the final render.

Path B, primary:

- Width `1.20 m`.
- Control points: `(6.20, -2.63)`, `(6.20, -5.70)`, `(6.75, -6.60)`, `(6.40, -8.20)`, `(5.40, -9.20)`.
- Terrace paver top `-0.295` against the lower tread `-0.195`, `100 mm` riser.
- Paver reveal `70 mm` above terrain; the last `0.60 m` eases to `12 mm` at the gravel.
- Keep the built centreline at least `0.35 m` clear of `Kameň • les.001` (AABB x `5.128..5.731`, y `-6.855..-6.226`). Do not move the rock.
- Grades follow the measured terrain; all under `8%` except the existing step risers. No cut or fill deeper than `80 mm`; none on the road.

Path A, secondary:

- Width `0.90 m`; replace the entire existing run A in place. From `Nášľap.006` through `Nášľap.009`, shift the centre about `0.15 m` southeast away from `Smrek • stredný.021`.
- Stops at the last stone. Does not continue to the road, does not join path B.
- Subject to the measured tree-clearance correction above.

Pavers and edge:

- One beveled paver mesh `Dlažba • kus`, `0.198 × 0.098 × 0.060 m`, `1.5 mm` bevel.
- Running bond, `0.200 × 0.100 m` pitch, about `670` instances, realized face count on the order of `20,000`.
- `Lôžko • chodník` under the joints, `40 mm` wider than the pavers, top flush with the paver top, material `Obruba • betón`; continuous flush edge, no raised kerb.
- Edge trimming/border per correction 4.

Materials, procedural only, no images or asset libraries:

- `Dlažba • betón`: warm grey, per-instance base colour about `(0.18, 0.18, 0.17)` to `(0.32, 0.32, 0.30)`, roughness `0.78–0.90`, fine noise bump.
- `Obruba • betón`: darker about `(0.12, 0.12, 0.11)`, roughness `0.85`.
- `Štrk • prístup`: Voronoi scale `18`, noise scale `3`, colours about `(0.22, 0.20, 0.16)` to `(0.38, 0.35, 0.28)`, roughness `0.82`, bump `0.15`.

Collections and objects, scene A only:

- `11 • Prístup • A`: `Chodník • terasa`, `Chodník • vstup`, `Cesta • les`, `Parkovanie • štrk`, `Lôžko • chodník`.
- `11a • Pomocné • A`: `Maska prístupu`, `Proxy • auto`; both hidden from final render. The mask remains available to Geometry Nodes.
- `05b • Nášľap • ponechané`: all 20 original stones, scene A only, excluded from the view layer. Meshes, transforms and `Kameň` unchanged.
- `10a • Vegetácia • mimo prístup`: only non-tree objects whose bounds intersect the expanded mask; scene A only, excluded from the view layer. Likely `Papraď.005`; re-measure at build time.
- `07d • Kamera prístup • A`: `D • Prístup zhora`, location `(7.0, -23.5, 15.5)`, lens `28 mm`, sensor `36 × 24`, aimed at `(6.5, -8.0, -0.4)`. The script may move this camera by at most `2 m` or change the lens by at most `5 mm` if the first overview clips. Camera A never moves.

Grass and ground:

- Add `Maska prístupu` covering the road, stall, tapers and both paths expanded by `0.12 m`.
- In `Pokryv lesa` only, AND the existing point selection with the inverse of a Geometry Proximity test against the mask. The node group has one user and is scene A only. Do not rebuild it; do not rerun `scripts/vegetation_scene_a.py` or `scripts/conifer_detail.py`.
- Pavers and gravel sit on top of `Lesná čistina`; do not boolean or rebuild the terrain.
- Thin soil line at the edge is the intended transition. No grass through the finished surfaces.

## Exact filesystem scope

Candidate: `Jelena/Jelena_Realistic_v005.blend`
Checkpoint: `.local/checkpoints/Jelena_Realistic_v004-before-access.blend`
Script: `scripts/access_landscape_v005.py`
Evidence directory: `evidence/access-005/`

Evidence files, all required:

- `evidence/access-005/camera-a-before.png`
- `evidence/access-005/camera-a-after.png`
- `evidence/access-005/overview.png`
- `evidence/access-005/camera-a-detail.png` — side-path joints
- `evidence/access-005/camera-a-terrace-detail.png` — terrace riser and path B start
- `evidence/access-005/manifest.json`

README: one minimal line under `## Súbory`, stating that `Jelena/Jelena_Realistic_v005.blend` is the access candidate and that `v004` remains the accepted exterior until this whole is accepted. No other documentation change.

Do not write any other repository path. Do not stage any `.local` checkpoint. Do not touch `Jelena/Jelena_Realistic_v004.blend`, `v003`, `v002`, `v001`, `Jelena.blend`, the protected evidence or the AP submodule.

## Checkpoint and recovery

Before any render-setting change or scene edit:

```fish
cp Jelena/Jelena_Realistic_v004.blend .local/checkpoints/Jelena_Realistic_v004-before-access.blend
shasum -a 256 Jelena/Jelena_Realistic_v004.blend .local/checkpoints/Jelena_Realistic_v004-before-access.blend
```

Both hashes must equal `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`. If the checkpoint path already exists, stop. If the copy or hash fails, stop.

Recovery:

- `Súbor → Navrátiť` reloads the current filepath. Before Save As, that is `v004`; after Save As, it reloads `v005`.
- To recover from a bad `v005`, open the checkpoint and Save As `v005` only under this grant. Never save onto `v004`.
- The checkpoint is untracked and must never be staged or committed.

## Render evidence and budget

Matched Camera A before/after:

- Camera `A • Chata pri lese`, frame 1, Cycles CPU, `840 × 560`, `32` samples, adaptive on, threshold `0.01`, min samples `0`, OpenImageDenoise on, seed `0`, AgX, look `None`, exposure `0`, gamma `1`, display sRGB, PNG RGB 8-bit, transparent off, border off.
- Render the before fresh from `v004` before Save As. Do not reuse `evidence/exterior-004-correction-02/camera-a-after.png`.
- After building, render the after from `v005` with identical settings.

Overview:

- Camera `D • Prístup zhora`, frame 1, Cycles CPU, `840 × 560`, `32` samples, same adaptive/denoise/seed/colour settings.
- One optional `16`-sample overview test is allowed before the final overview.
- It must show road, parking, path and steps together.

Side detail:

- Camera A, `1260 × 840` render setting, border `(0.64, 0.995, 0.00, 0.28)`, `32` samples, OpenImageDenoise on, same colour settings.
- Purpose: side-path joints and edge contact.

Terrace detail:

- Camera A, `1260 × 840` render setting, border `(0.28, 0.72, 0.00, 0.38)`, `32` samples, OpenImageDenoise on, same colour settings.
- Purpose: `100 mm` terrace riser and paver-to-step contact.
- If the first crop clips the junction, adjust the border by at most `0.05` in each direction and record the final border. Do not change Camera A.

After all renders, restore the saved `1260 × 840 / 80 samples / denoise off / RGBA` settings and save `v005` once more.

Budget:

- First pass: at most six stills, including the optional 16-sample overview test.
- One bounded correction: at most two additional stills.
- Hard cap: eight stills total; cumulative render wall-clock at most `15` minutes; no animation.
- Sampled process RSS: stop and simplify if a sample reaches `4.5 GiB`; never continue past `6.0 GiB`. Record sampled RSS in KiB and state that it is not peak memory.
- If a required view cannot render inside the budget, report `PARTIAL`; do not drop a required view silently.

Manifest fields:

`camera`, `frame`, resolution, samples, engine, device, adaptive sampling, threshold, min samples, denoising, denoiser, seed, view transform, look, exposure, gamma, display, file format, colour mode, depth, border, seconds, blend path and SHA-256, checkpoint path and SHA-256, script path and SHA-256, each evidence image path and SHA-256, scene-B object count, Camera A matrix/lens/sensor/shift, `Kameň` user count, tree-location check, proxy exclusion, visual review, known limitations, sampled RSS in KiB (not peak), total render seconds.

## Preservation checks

- `v004` SHA-256 unchanged before and after; never save the `v004` path.
- Protected `Jelena.blend`, `v001`, `v002`, `v003` hashes unchanged.
- Camera A matrix, lens `46 mm`, sensor `36 × 24`, shift `0/0` unchanged.
- Scene B remains `308` objects; no new collection, object, material, node group or image is linked into scene B.
- `Kameň` remains `25` users; its node tree untouched.
- Every `Smrek` location and scale unchanged; no tree moved, hidden or removed.
- The 20 original stones remain in the file, in `05b`, with unchanged meshes, transforms and material; excluded from scene A render.
- New collections/objects/materials are scene-A-only.
- Lighting, world and colour management unchanged.
- No whole-scene vegetation generator rerun; only the local `Pokryv lesa` mask.
- Proxy car hidden from every final render.
- No external assets, paid services, uploads or credential changes.

## Implementation sequence

1. **Preflight.** Verify repository identity, branch, HEAD, AP pin, clean tracked worktree apart from the three known untracked checkpoints, `v004` hash, `v005` absent, checkpoint absent, evidence directory absent, report path absent, live filepath, `is_dirty false`, scene A, camera A, frame 1, scene counts `923`/`308`, and Camera A values. Stop on any material difference.
2. **Checkpoint.** Create and hash the checkpoint copy as above. Do not stage it.
3. **Script.** Write `scripts/access_landscape_v005.py`. It must:
   - refuse unless `bpy.data.filepath` ends with `Jelena_Realistic_v005.blend`, scene is `A • Chata pri lese`, camera is `A • Chata pri lese`, scene B has `308` objects, Camera A matches within `0.0001`, and the new collections/objects are absent;
   - build the scene per the accepted plan and the five corrections;
   - measure path-A tree geometry as specified; assert road/parking/path-B trunk clearance `>= 0.70 m`; assert the rock clearance `>= 0.35 m`;
   - assert scene B, `Kameň`, Camera A, tree transforms and shared datablocks are preserved;
   - print a compact measured report of object counts, bounds, clearances and created datablocks;
   - never render, never save, never delete shared datablocks, never move trees.
4. **Before render.** Set the matched recipe, render `camera-a-before.png`, restore the saved settings. Do not save `v004`. Stop without saving if object counts changed.
5. **Save As.** Save As `Jelena/Jelena_Realistic_v005.blend`. Use the verified Slovak `Súbor → Uložiť ako...` flow or an exact `bpy.ops.wm.save_as_mainfile(filepath=...)`; verify the resulting filepath. Never overwrite `v004`.
6. **Build.** Run the script through the current MCP session. If any assertion fails, stop; do not save a failed candidate.
7. **Save and render.** Save `v005`, then render the after, overview, side detail and terrace detail. Inspect the actual images.
8. **One bounded correction.** If a visible defect is inside the plan and corrections, adjust only the affected part: mask margin, edge blend/border, material variation or detail framing. Do not change the layout, move Camera A, move trees or expand scope. Re-render at most two stills. If the defect requires a layout or tree change, stop and report `PARTIAL` with the exact finding.
9. **Final save.** Restore the saved `1260 × 840 / 80 samples / denoise off / RGBA` settings, save `v005`, hash it, read back the filepath and settings.
10. **Manifest and README.** Write the manifest and the one minimal README line. Do not touch other documentation.
11. **Final preservation readback.** Re-hash `v004`; verify scene B, Camera A, `Kameň`, stones, trees, collections and proxy exclusion. Stop on any failure.
12. **Git.** Stage only the exact commit paths below, make one commit, push ordinarily non-force, and verify the public ref.
13. **Terminal report.** Write `01_report_02.md` at the exact Meta path.

## Git authority

Phase: Implementation. Michal’s standing authorization covers this ordinary non-force project commit and push.

Stage only these exact paths:

```text
Jelena/Jelena_Realistic_v005.blend
scripts/access_landscape_v005.py
evidence/access-005/camera-a-before.png
evidence/access-005/camera-a-after.png
evidence/access-005/overview.png
evidence/access-005/camera-a-detail.png
evidence/access-005/camera-a-terrace-detail.png
evidence/access-005/manifest.json
README.md
```

Never use `git add .` or `git add -A`. Never stage `.local/checkpoints`, `01_report_02.md`, the Meta trace, the AP submodule or any other path.

One commit, exact message:

```text
Add the forest access path, gravel pull-off and road as v005.

The accepted v004 exterior stays unchanged so the arrival can be reviewed beside it.
```

One ordinary non-force `git push origin HEAD`. No fetch/pull, no force, no LFS, no history rewrite, no remote rewrite, no tag. After push, verify `git ls-remote origin refs/heads/main` equals the new commit and `git status` shows only the expected untracked checkpoints. If the push is rejected or would require force, stop and report.

Meta Git remains COOPERATOR-owned. The Worker writes only its own terminal report in the Meta trace.

## Authority

Positive authority:

- read-only inspection of the repository, AP, Meta evidence and live scene;
- exact local filesystem writes in the changed-path allowlist;
- scene-A mutation in the live Blender instance exactly as specified;
- checkpoint copy, Save As `v005`, script execution, renders, evidence writes, manifest, minimal README edit;
- one commit and one ordinary non-force push to `origin` `main` with the exact paths and message above;
- direct write of the terminal report at the exact Meta path.

Negative authority:

- no writes outside the changed-path allowlist;
- no scene B edits; no shared collection `04`, `06`, `07`, `07b` edits; no `Kameň` edit;
- no cabin, terrace, furniture, steps, Camera A, light, world or colour-management changes;
- no tree moves, hides, removals or tree-generation work;
- no whole-scene vegetation regeneration;
- no external assets, paid services, network except the authorized Git push/readback, uploads, credentials, accounts or host configuration;
- no addon update, reinstall, second Blender instance, background Blender or process termination;
- no Meta Git operation, no acceptance claim, no publication PASS, no logical-whole closure;
- no subagents, internal delegation or parallel work.

Commands: read-only shell, `cp`, `shasum`, the exact script, Blender MCP calls, `git add` with explicit paths, `git commit`, `git push origin HEAD`, `git ls-remote origin refs/heads/main`, `git status`, `shasum`, `stat`, `rg`, `cat`. Fish-compatible presentation for owner steps.

Repository checkout topology: standalone checkout
Working-copy topology: canonical checkout, single mutating Worker.

Repository mutation: `Jelena/Jelena_Realistic_v005.blend`; `scripts/access_landscape_v005.py`; `evidence/access-005/camera-a-before.png`; `evidence/access-005/camera-a-after.png`; `evidence/access-005/overview.png`; `evidence/access-005/camera-a-detail.png`; `evidence/access-005/camera-a-terrace-detail.png`; `evidence/access-005/manifest.json`; `README.md`; `.local/checkpoints/Jelena_Realistic_v004-before-access.blend` (untracked, never staged)
Host/remote mutation: ordinary non-force push to `origin` `refs/heads/main` at `https://github.com/cisarik/jelena`; no other host/remote effect
Trace persistence: direct-write `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_02.md`

## Delivery and trace

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_implementation_02.md`
Destination path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Report filename: `01_report_02.md`
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR (Meta Git); project Git push is separately authorized above
Archival: wait-for-report

External trace disposition: configured
Trace discovery: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Trace project key: `jelena`
Trace logical-whole projection identity: `jelena-access-path-and-gravel-parking`
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

The exact report write is the sole Meta write. Create `01_report_02.md` if and only if it is absent; read it back fully and verify path, identity and SHA-256. Do not touch `01_report_00.md`, `01_report_01.md` or any earlier trace artifact.

## Validation and acceptance

Technical validation, non-independent:

- script assertions and readbacks pass;
- `v004`, protected baselines, Camera A, scene B, `Kameň`, trees and stones preserved;
- both paths replace both stone runs; stones are present but excluded;
- road, parking and path form a continuous, grounded sequence;
- parking fits one car with the corrected `0.55 m` north standing strip and a plausible approach;
- no tree moved; path-A clearance measured or reported as a specific conflict;
- no grass penetration, floating edge, buried edge or unsupported level change in the inspected images;
- paver edges are trimmed/bordered with no gaps or overlaps;
- the terrace riser is readable in `camera-a-terrace-detail.png`;
- the overview shows road, parking, path and steps together;
- manifest hashes and settings are complete;
- performance is inside the budget and the result is editable.

Owner acceptance is separate. Do not claim it. Provide a short numbered acceptance request for Michal in the terminal report, based on the plan’s four questions, updated to mention both paths, the overview, the parking approach and the terrace junction.

Independence is not required for this reversible visualization. The implementation evidence is non-independent.

## Stopping conditions

Stop and report without improvising if:

- repository identity, branch, HEAD, AP pin or a protected hash differs materially;
- the live file is not exactly `Jelena_Realistic_v004.blend`, is dirty in an unexplained way, or is not scene A with camera A;
- `v005`, the checkpoint, the evidence directory or `01_report_02.md` already exists;
- the checkpoint copy or hash fails;
- a script assertion fails, including any tree, rock, scene-B, `Kameň`, Camera A or shared-datablock check;
- a required change would move/remove a tree, edit a shared collection, change Camera A or expand scope;
- MCP fails after two bounded attempts; do not restart Blender, update the addon or bypass the MCP path;
- a render would exceed the still-count, wall-clock or RSS gate;
- an inspected image shows a defect that requires a layout change rather than a bounded correction;
- Git would require force, a non-fast-forward recovery, LFS or a path outside the allowlist;
- the task would require external assets, paid services, uploads, credentials or host changes.

Do not save a failed candidate, do not overwrite `v004`, do not emit the closure signal and do not close the logical whole.

## Report contract

The terminal report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo exactly once:

- `Logical whole identity: jelena-access-path-and-gravel-parking`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 03`

Include:

- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: implementation-PASS | not-applicable`
- `Start commit:` `b70f242169b8173d0af5b660dcf1c9f00181449a`
- `End commit:` the new commit, or the unchanged commit if no commit was made
- `Report justification: new-mutation`
- `Logical-whole closure: not-closed`
- Changed files and purpose.
- Candidate path, SHA-256, and the exact checkpoint hash.
- Script path and SHA-256.
- Evidence image paths, dimensions, SHA-256, settings and render seconds.
- Manifest path and SHA-256.
- Preservation results: `v004`, protected baselines, Camera A, scene B, `Kameň`, trees, stones, collections, proxy.
- Layout dimensions and assumptions actually built.
- Path-A tree-clearance measurement and result, or the exact conflict.
- Performance: total render seconds, sampled RSS in KiB (not peak), any budget pressure.
- Git commit and push result; public-ref readback; any limitation.
- Image inspection findings and the bounded correction, if used.
- Risks, deviations, missing evidence and known limitations.
- One smallest next step: Orchestrator evidence review and Michal’s visual acceptance.
- `Orchestration critique:` with `MEASURED` and `LEAD`; either may be `none`.
- `Resolved Execution Issues / Near-Misses:` none or complete.
- `Pre-Existing Failure Classification:` none or complete.
- A clear statement that the Worker did not claim acceptance, publication PASS or closure.
- `Authority expiry:` this terminal report ends the grant; no autonomous continuation.

PASS means the candidate and required evidence were produced and validated inside the grant, with all preservation and performance checks passing. PARTIAL means a useful candidate or evidence exists but a named required check or image is missing. BLOCKED means a prerequisite or authority boundary prevented the implementation.

## Context and MCP safety

The earlier read-only Orchestrator query over a 569k-vertex tree mesh froze the addon bridge. Do not repeat that pattern:

- use `numpy` and `vertices.foreach_get` for large mesh reads, not per-vertex Python loops;
- keep each MCP call bounded; split long inspections from renders;
- if a call times out, do not restart Blender, do not kill processes and do not bypass the MCP path; report the exact state;
- one live Blender instance; no background/second instance;
- protocol 15 is behind expected 16; leave it untouched unless a later call fails.

If your context degrades or you lose track of the accepted decisions, stop at a coherent boundary and report `PARTIAL`/`BLOCKED` with the exact limitation. Do not invent telemetry. A terminal report ends this grant.

Authority expires at the terminal report, cancellation or supersession.
