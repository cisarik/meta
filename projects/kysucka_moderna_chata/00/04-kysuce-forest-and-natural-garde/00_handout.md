# Kysuce forest and natural garden — logical whole 04

Handout status: provisional
Author: read-only Master Chat Orchestrator
Author session scope: development-run
Development run identity: kysucka-moderna-chata-reference-visualization
Recipient access profile: Orchestrator
Recipient session scope: logical-whole
Logical whole identity: kysucka-moderna-chata-kysuce-forest-and-natural-garden
Destination: cisarik/meta, projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/00_handout.md
Prepared: 2026-11-14, Europe/Bratislava
Artifact lifecycle: provisional operational handoff to this whole's Fresh Orchestrator, linked from the Master run map; freeze on opening, retain as historical evidence; cleanup owner COOPERATOR under an exact grant

🟡 Ready for manual delivery
Capability profile: Orchestrator, fresh session, functioning Blender MCP
Recommendation: Medium reasoning; retain Michal's selected model and manual delivery
Native Plan Mode: OFF for Orchestrator coordination; ON for the first Planner
Archival: handout, not Worker exchange; completed prompt/report pairs wait for the actual report

## One visual outcome

Replace the empty landscape and toy vegetation with a coherent, convincing
**Kysuce setting: forested hills, nearby smaller spruces, an apple-bearing orchard
tree and natural front planting**. Deliver editable v04 and reproducible source.
This is one environment pass, not a whole-house redesign. Keep the selected C1
camera, v03 timber/fence, building and existing lighting.

Michal explicitly asks for real architectural visualization rather than a video-
game appearance. He asks Master to find online tree/plant assets. Master has
researched concrete sources below; their public descriptions are acquisition
evidence, not proof of downloaded files, correct imports or render quality.
You and Workers have functional Blender MCP. Inspect the live scene/reference
yourself, issue a concise Planner prompt, then a separately authorized practical
implementation prompt. Inspect actual pixels yourself at acceptance.

Communicate with Michal in Slovak, masculine address and feminine self-reference.
Worker prompts/reports are English; reports begin `### Report for ORCHESTRATOR_CHAT`.
Master remains read-only. This provisional handout supplies selection/context;
your complete current prompts grant bounded execution authority.

## Verified starting boundary

Master inspected public commit/trees and focused source blobs on 2026-11-14:

| Source | Observed anchor |
|---|---|
| https://github.com/cisarik/kysucka_moderna_chata, main | `623d12abe0c0eb2742cd02c9962c1712b53437e2` |
| Project .ap gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` |
| https://github.com/cisarik/meta, main | `a46e62d7a1876bc04e5af5e7c139d9a9f40d793f` |

Predecessor: `00/03-realistic-timber-and-foreground-fence/01_closure.md`.
The supplied closure is byte-identical to its public Meta blob. Whole 03 is
closed on Orchestrator verification and published project state; preserve the
two historical BLOCKED Worker reports rather than inventing Worker PASS results.
The sky-enum compatibility issue was fixed and semantic replay verified by its
Orchestrator. Do not reopen that whole or initialize AP/MCP again.

- Input: `blender/kysucka_chata_mcp_v03.blend`, recorded SHA-256
  `360c99a107f9bd819e273274e3cd449a5b7666a27fc69c6ee3a51dfa7e120248`.
- `model/parameters.json`: `153437c4a574243240011bb12a34b3597f199b5c18d36b54a8f3e8bcde45ad34`.
- `scripts/build_scene.py`: `baee0b204b17b5e696933ed97a9c915191b6c5b873320651da9cdf59f30288c0`.
- `scripts/timber_fence_v03.py`: `f94dce1b2da5c07d4064f8ac800304ce3e4c04372447eb737ac2a51aa73fcf98`.
- Reference: `reference/kysucka_chata_moderna.png`, 1448 × 1086, SHA-256
  `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`.
- Canonical public v03 `renders/after.png`:
  `3c77ef772bb5578aa54227df98615356cc301c9542fffe982071bed62b0d69d1`.
  Master inspected it. The uploaded preview has tiny RGB differences (maximum
  one 8-bit unit), so do not claim its file hash matches the canonical artifact.

Master also inspected the supplied timber detail sheet. At the observed Meta
commit that sheet and `renders/render_metadata.json` are absent publicly; this
is an archival observation, not model corruption or a reason for a repair whole.
Use the actual local originals where needed; Meta Git belongs to Michal.

Read current AGENTS.md, focused operations/source, pinned AP.md,
AP_ORCHESTRATOR.md, PROMPT_CONTRACTS.md and Meta's storage contract. Verify actual
roots, project origin, baseline, relevant input hashes and owner dirty state.
Protect unsaved GUI work; Master has no current local-state observation.
Renew `blender-mcp-live-v1` explicitly for this whole's authorized environment
changes, imports, checkpoints, renders, packing and saves. Prior grants expired.
No add-on/runtime upgrade is selected; old protocol warnings were non-blocking.

## Composition and required scene changes

Lock `CAM_A_REFERENCE`: location `[21.5,-10.0,1.25]`, target `[8.5,2.5,1.25]`,
35 mm, sensor 36 mm, shift_x 0, shift_y 0.105. Preserve optics and transform.
Use top-left image coordinates `u=x/width, v=y/height` for composition checks.

| Layer | Required visible result |
|---|---|
| Background | Rolling forested hills fill the currently empty left/central distance, with meadow clearings and irregular spruce-dominated forest edges. |
| Near/mid-ground | A few smaller spruces connect the garden to the woodland without blocking the facade or glazing. |
| Left garden | A believable orchard apple tree has branching structure, individual leaves/leaf clusters and visible attached apples. |
| Front garden | The green/purple spheres are replaced by irregular planted groups of shrubs, grasses and modest flowers, with readable ground between them. |

### Hills and forest

The reference skyline is chiefly behind the left/central house, roughly
u=0.00–0.65, v=0.15–0.55 where not occluded by the roof. These are broad visual
bands, not survey points. Build two or three readable terrain layers with meadow
openings and clustered woodland. Do not create a steep green wall immediately
behind the building or merely add trees still hidden behind its roof.

Establish the camera/world directions and project sample ridge points first.
The closure's suggested X/Y ranges are hypotheses; place hills far enough away
and high enough to read as landscape while staying inside the camera clip range.
Use a separate background terrain or a smooth distant deformation. Preserve the
near-ground heights supporting the house, path, steps and v03 fence exactly.

Scatter spruce instances in patches with gaps, varied height/rotation and
plausible upright growth. Tree bases meet the surface; no uniform grid, floating
trees, repeated rows or oversized miniature hills. Use lower detail for distant
canopies and stronger detail on silhouettes. Do not realize thousands of copies
or duplicate materials/images per tree. Far-distance impostors are acceptable
only as a disclosed LOD; retain real 3D terrain and nearer trees. No photographic
wallpaper or generated image substituted for the editable environment.

### Smaller spruces and orchard tree

Place approximately 3–6 smaller conifers near the garden perimeter, as initial
design guidance, with varied roughly 1.5–3.5 m height. Match a young spruce habit;
do not uniformly shrink a broad mature crown and call that a sapling. Keep the
entry, glazing and roof silhouette readable. Final positions follow actual
camera inspection, not a mandatory world-axis recipe.

Replace the `APPLE_*_proxy` tree at approximately `(-0.6,-3.0)` with an orchard
silhouette: a believable textured trunk, branching crown, leaf gaps and readable
red/blushed apples attached by stems. Its exact transform may change within the
left garden to frame the house like the reference. Keep its left-edge crop and
leafy canopy useful; do not let it hide the entrance or occupy most of the sky.
Use plausible fruit size, about 6–9 cm as guidance, and distribution among
supporting twigs. Do not hang apples in empty space or inflate them to make a
failed composition pass. Inspect a native-pixel crown crop and the full frame.

### Planting and ground

Replace visible `SHRUB_proxy*` / `FLOWER_proxy*`, old cone conifers/trunks and
orchard proxies; hiding the precise superseded objects is acceptable if source
replay does it deterministically. Do not hide the whole site collection, which
also contains the retained fence, paving and lights.

Use layered, nonuniform front planting: low foliage, a few airy grass tufts and
small flower accents, leaving the steps/path clear and the bench usable. Do not
replace each sphere with one identical evenly spaced model. Preserve `BED_entry`
footprint; its soil shader may improve. Add restrained grass tufts and surface
variation to visible lawn/fence edges so terrain is no longer a smooth green
sheet. Ground appearance is in scope; nearby ground geometry is protected.
Planters, new paths and full garden redesign are not required.

## Master-researched asset acquisition targets

Use these finite targets first, not an open-ended asset hunt. Public descriptions
were checked on 2026-11-14. Triangle counts are source listings, not measured
Blender evaluated counts. Final suitability requires actual import/test render.

| Role | Concrete source | Observed facts / use decision |
|---|---|---|
| Primary spruce | [Spruce tree — Georgeous](https://sketchfab.com/3d-models/spruce-tree-7a5db417827244d98827459bce0cc944) | Listed as Picea abies, LOD0/LOD1, about 10.4k triangles, bark and branch maps, CC Attribution. Preferred efficient forest/near-tree basis. |
| Spruce fallback | [Realistic HD Norway spruce (3/43) — PlantCatalog](https://sketchfab.com/3d-models/realistic-hd-norway-spruce-343-bf500546e2874f9ea086ba6abb11357e) | Listed Picea abies, adult 9.5 m, LODs, about 143.2k triangles, CC Attribution. Alternative source if the primary fails actual quality/import. |
| Orchard tree | [Apple Tree — rhcreations](https://sketchfab.com/3d-models/apple-tree-e5e1208e7e734f88b02c5f45c70f8db1) | Listed textured, rigged, about 67.6k triangles, created in Blender 2.79b, CC Attribution. Inspect crown/leaves; use a static pose, not an animation/rig project. |
| Fruit detail if needed | [Food Apple 01 — Poly Haven](https://polyhaven.com/a/food_apple_01) | Textured apple, about 7k triangles, CC0. Instance a suitable lower-detail version only if the orchard model lacks usable visible fruit. |
| Lawn/bed grasses | [Grass Medium 01 — Poly Haven](https://polyhaven.com/a/grass_medium_01) | CC0, LODs/Geometry Nodes listed; default page reports a large aggregate. Import a suitable tuft/LOD, not the whole high-density demonstration scatter. |
| Low shrubs | [Shrub 01 — Poly Haven](https://polyhaven.com/a/shrub_01) | CC0, leaf alpha maps and LODs listed. Use selected low-growth clumps at believable scale, not the entire display arrangement repeated. |
| Flower accents | [Periwinkle Plant — Poly Haven](https://polyhaven.com/a/periwinkle_plant) | CC0, opacity/translucency maps, about 67k triangles, LODs. Garden accent, not a claim of lavender or native Kysuce flora. |

Species matters: Poly Haven's `fir_tree_01` / `fir_sapling` are labelled fir,
not a verified spruce substitute. `tree_small_02` is tagged Burkea africana;
do not relabel it an apple tree by attaching fruit. Cheap stylized orchard or
Christmas-tree packs do not answer Michal's request. The listed backup spruce
replaces the primary, not a requirement to import both large libraries.

Important capability limit: Master could inspect indexed source metadata, but
direct Sketchfab page requests returned 403 and binary downloads were not
validated here. Poly Haven API/binary availability was also not established in
this environment. Do not claim assets are attached or already imported.
Use official downloads with existing authorized access. If login or an absent
archive blocks acquisition, name the exact selected missing archive and ask
Michal for that input once; preserve the accepted plan and resume acquisition
afterwards. Do not create accounts, bypass access controls, substitute an
unverified tree, or start an installation/planning loop.

Verify each downloaded archive's actual license/version and complete textures.
CC Attribution is not CC0. Retain creator/title, source URL, exact license URL,
required notices and modifications in `assets/ASSET_MANIFEST.md`, alongside
SHA-256, dimensions, LODs and source-to-derived mapping. Include applicable
credits with distributed project/renders, not only in a private report.
Reference: https://creativecommons.org/licenses/by/4.0/ and
https://polyhaven.com/license . Choose redistribution-compatible data; no paid
purchase or new paid service is selected.

## Finite execution and source boundary

Open `00_notes.md` with handout revalidation. First Planner: fresh session 01,
exchange 01, native Plan Mode required, `01_planning_00.md` → `01_report_00.md`.
Then renew the healthy same Worker for implementation 01/02, Plan Mode not-used,
`01_implementation_01.md` → `01_report_01.md`. Normal Meta suffix is exchange
ordinal minus one. Rotate only for an actual capability/context reason.

The plan answers only asset availability/import strategy, projected ridge and
planting layout, LOD/instance budget, exact mutation paths and acceptance. It
does not redesign the workflow or copy this handout into a giant prompt. Resolve
native Plan Mode's known report-write limitation by naming a capable report
persister and exact relay/writeback route before delivery. Do not replan merely
to persist a complete report. Implementation Worker normally saves its own report.

Implementation milestones within one grant: acquire and test representative
models; build visible hills/forest; replace orchard/near trees/front planting;
then verify and render. Use a small asset test render before large scattering
to check leaf/needle alpha, normals, texture completeness and scale. Limit to
two cheap composition previews and one focused correction for a concrete defect;
do not generate endless alternatives. Missing inputs get an exact disposition,
not a fabricated scene-complete PASS.

Import only required geometry/materials from model files, not their demonstration
worlds, cameras, lights or scatter scenes. Keep imported scripts/auto-run disabled.

Use a shared deterministic `scripts/landscape_v04.py` refinement called through
MCP and after v03 refinement in `scripts/build_scene.py`. Store accepted layout,
asset paths, seeds, densities and LODs in `model/parameters.json`. Preserve
`scripts/timber_fence_v03.py` and its settings. Imported masters and instancing
must be repeatable/idempotent: a second application does not double the forest.
Do not perturb the original generator's global random stream. Test source replay
in a disposable `work/` scene without reopening over live unsaved work.

Grant exact paths for the v04 module/builder/JSON, selected asset libraries/maps,
manifest, v04 scene, temporary staging/replay and Meta evidence. Include network
downloads, live MCP effects and report writes as positive authority. Narrow
documentation updates may cover v04 opening/replay/assets/MCP route only in
AGENTS.md, README_SK.md and docs/OPERATIONS.md. Managed AP block and the entire
`Closure and Git gates` section stay byte-identical; Workers must not reproduce
the literal closure signal in plans/reports.

Keep 1K/2K maps initially; use linked mesh/collection instances, LODs and camera-
aware density. This host was a Mac M1 with limited memory: measure actual memory,
unique/evaluated geometry and render time before increasing density. Aim for
under 3 million unique source triangles initially; this is a budget to validate,
not a claim about hardware capacity. Avoid 4K/8K libraries and destructive
realization as the default. Keep every tracked file below 90 MiB; retain compact
normalized asset libraries if originals are huge. Original download caches can
stay in granted gitignored `work/`; retained derived data must rebuild offline.
Pack used textures in v04 where practical, preserve relative paths and deduplicate
images. No new Git LFS/storage/runtime scheme to solve oversized asset choices.

Unchanged: seed/v01/v02/v03, camera, house/roof, openings, furniture/partitions,
chimney/fireplace, v03 timber/UV/fence, path/steps/bollards, world/lights, glass,
reference, CAD/PDF, AP pin and history. Vegetation may naturally change shadows
and reflections; do not freeze pixels as a preservation test. Preserve actual
unmodified scene data instead. Project publication needs a current explicit
commit/non-force grant against the expected parent; Meta Git remains Michal's.

## Acceptance and return packet

Deliver `blender/kysucka_chata_mcp_v04.blend`, offline-replayable source/assets,
updated manifest/credits and in this Meta whole:

- `renders/before.png` / `renders/after.png`: matched C1, 1448 × 1086, Cycles CPU,
  96 samples, OIDN ON, frame/seed 0, AgX look None, exposure 0, gamma 1 and
  unchanged world/lights. Reuse canonical v03 baseline only after matching its
  exact render profile; otherwise render it fresh. One render job at a time,
  using working MCP submission/polling rather than blindly repeating a timeout.
- `renders/landscape_details.png`: actual native-pixel crops showing ridge/forest,
  smaller spruce, orchard fruit/leaves and front planting; record crop bounds.
- `evidence/landscape_comparison.md`: actual imported sources/licenses, asset
  test, MCP change/separate-readback receipts, projected ridge/layout decisions,
  LOD/instance/memory/timing observations, source replay and remaining limitations.
- `renders/render_metadata.json`: actual scene/camera/render/settings and hashes.
  Notify Michal of this exact ignored JSON path for explicit Meta staging;
  do not rewrite ignore policy or investigate archival history.

You inspect full renders and crops yourself. Required visual checks: hills are
actually visible in the intended background; forest reads as clustered woodland;
near spruces and apple tree have natural silhouettes; apples attach to a leafy
crown; front spheres/cones are gone; ground is not an uninterrupted flat shader;
no black leaf cards, obvious tiling, floating vegetation or blocked entrance.
Confirm v03 timber/fence and locked camera remain intact.

Cold reopen must find all assets. Replay checks meaningful geometry/transforms,
material assignments, instances, textures and deterministic layout with declared
tolerances. **Do not gate on a complete cross-version UI/default-RNA dump**:
this caused the last unnecessary BLOCKED result. Compare semantic scene data in
the actual Blender version; frozen UI caches and .blend binary identity are not
the target. Object counts may legitimately change with replaced vegetation.

Return `01_closure.md` normally, public candidate SHA when publication is granted,
v04 path/hash, images, source/license/performance evidence, actual saved/idle
status, expired grants, and Michal's feedback or NOT TESTED. Technical delivery
does not imply subjective acceptance of the full visualization. Only this whole's
Orchestrator closes it after its gates; Master chooses the next whole.

Carry forward: grey sky/daylight and dark soffit; fireplace visibility/coherent
chimney; Michal's perceived second entrance. Current evidence says only one
exterior `D01_leaf` exists; investigate the ambiguous visible interior slab in a
later interior whole before hiding anything. No automatic deletion or lighting
work is appended here. Architectural checking remains deferred.

## Master run-map snapshot

Mechanically persist this Master-authored snapshot under an exact grant at
`projects/kysucka_moderna_chata/00/00_RUN_MAP.md`; reconcile newer content rather
than blindly overwriting it. Discovery only, no implementation authority.

```text
Run map: kysucka-moderna-chata-reference-visualization
Run objective: converge the editable Blender scene toward reference/kysucka_chata_moderna.png; architectural checking is deferred
Run map authority: discovery-only
Run entry: 00 | kysucka-moderna-chata-ap-meta-initialization | closed | depends on: none | handout: projects/kysucka_moderna_chata/00/00-init/00_handout.md | evidence: project foundation b47cce6f91ae10a22fb708a8e5220ab27b471aeb
Run entry: 01 | kysucka-moderna-chata-blender-mcp-first-reference-render | closed | depends on: kysucka-moderna-chata-ap-meta-initialization | handout: projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_handout.md | evidence: public f0fb0ea25fcd091ff05e5e3717c433c586cac4fa, v01 and MCP framing comparison
Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | closed | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: public d67431d1678de511e06a8ad04cd632ae4899cdc4, v02 C1, comparison and publicly archived closure
Run entry: 03 | kysucka-moderna-chata-realistic-timber-and-foreground-fence | closed | depends on: kysucka-moderna-chata-reference-camera-perspective | handout: projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/00_handout.md | evidence: public 623d12abe0c0eb2742cd02c9962c1712b53437e2, v03 timber/fence, matched render, semantic replay and public closure; some supplemental trace artifacts remain locally supplied
Run entry: 04 | kysucka-moderna-chata-kysuce-forest-and-natural-garden | provisional | depends on: kysucka-moderna-chata-realistic-timber-and-foreground-fence | handout: projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/00_handout.md | evidence: Michal requests forested hills, smaller spruces, an apple-bearing orchard tree and natural planting; Master researched concrete asset targets; acquisition/import/visual acceptance remain to be verified by this whole
```
