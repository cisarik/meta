# Spatial site, valley vista and grass — logical whole 05

Handout status: provisional
Author: read-only Master Chat Orchestrator
Author session scope: development-run
Development run identity: kysucka-moderna-chata-reference-visualization
Recipient access profile: Orchestrator
Recipient session scope: logical-whole
Logical whole identity: kysucka-moderna-chata-spatial-site-valley-and-grass
Destination: cisarik/meta, projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/00_handout.md
Prepared: 2026-11-15, Europe/Bratislava
Artifact lifecycle: provisional operational handoff to this whole's Fresh Orchestrator, linked from the Master run map; freeze on opening, retain as historical evidence; cleanup owner COOPERATOR under an exact grant

🟡 Ready for manual delivery
Capability profile: Orchestrator, fresh session, functioning Blender MCP
Recommendation: Medium reasoning; retain Michal's selected model and manual delivery
Native Plan Mode: OFF for Orchestrator coordination; ON for the first Planner
Archival: handout, not Worker exchange; completed prompt/report pairs wait for the actual report

## Selected outcome

Turn v04's primarily camera-composed environment into a **coherent mountain
property that works in 3D**: surrounding forest/meadow context, an open valley
view from the glazed gable, a fully enclosed generous garden, and visibly
different short lawn and tall meadow grass. Deliver editable, offline-replayable
v05. These are connected site changes: define terrain and enclosure first, then
scatter the two ground-cover zones against those same boundaries.

This selects Michal's reported next-step vision from the returned whole-04
closure. It does not select lighting/interior work or more fruit-tree shopping.
The reference remains the appearance target; the accepted brief now also includes
orbiting the scene and looking out from inside. A single attractive front render
cannot demonstrate this whole's spatial outcome.

You and Workers have functioning Blender MCP. Inspect the live scene and
reference yourself, delegate one concise Planner and a separately authorized
implementation, then inspect actual saved scene/render evidence yourself.
Master remains read-only and supplies context, not executable Worker authority.
Communicate with Michal in Slovak, masculine address and feminine self-reference.
Worker prompts/reports are English; reports begin `### Report for ORCHESTRATOR_CHAT`.

## Starting evidence and restoration

Master independently checked public commit/trees and focused source blobs on
2026-11-15:

| Source | Observed anchor |
|---|---|
| https://github.com/cisarik/kysucka_moderna_chata, main | `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` |
| Project .ap gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` |
| https://github.com/cisarik/meta, main | `2f1b70dfb4b402b5e5df6351a6d2ec0b00fedc9c` |

Predecessor: `00/04-kysuce-forest-and-natural-garden/01_closure.md`, supplied to
Master as `Pasted text(4).txt`, plus the supplied v04 after image. The closure
records Michal's acceptance, project publication and expired authority. At the
observed Meta commit, whole-04 closure/notes/comparison are not yet public; do
not describe them as publicly archived. Use exact supplied/local predecessor
evidence. This is an archival observation, not a new repair whole.

- Input `blender/kysucka_chata_mcp_v04.blend`, closure-recorded SHA-256:
  `c19b37cf75037969d2608677d276880d46e9ae7afc31aa11a78c340241fa3d43`.
- `model/parameters.json`:
  `a2239cd2ef6b75545e9f0a8ca750c11553678674c8ee1fde11818cb77d40ba77`.
- `scripts/landscape_v04.py`:
  `950d23c79bc50b26a1c606cff36605923a1c172b660f15945f58faf9beceb723`.
- `scripts/build_scene.py`:
  `8dfe65695ad99e25fad53d465fd8d79e4f6f5a7f7e8f1ef780ad9385ac08ce15`.
- Preserved reference `reference/kysucka_chata_moderna.png`, 1448 × 1086:
  `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`.

V04 already provides seven normalized local asset libraries and credits, 1,200
linked forest placements, four young spruces, the orchard tree/28 apples, natural
front planting and edge grass. Reuse those assets. Picea mariana was Michal's
selected visual forest asset; do not reopen species selection or claim native
botanical accuracy. V04 measured about 446,545 unique evaluated triangles,
27.83 million instance-expanded triangles, 1.43 GiB process RSS high-water and
219 seconds for the final CPU render on the 8 GiB M1 host. These are observations,
not future performance guarantees.

Read current AGENTS.md, focused operations/source, governing pinned AP.md,
AP_ORCHESTRATOR.md, PROMPT_CONTRACTS.md and Meta's storage contract. Verify actual
roots, origin, HEAD, working-tree state and input scene through MCP. Renew
`blender-mcp-live-v1` explicitly for this whole's permitted scene changes,
checkpoints, renders, imports, packing and saves. Prior grants expired; no AP/MCP
installation or upgrade is selected.

Avoid the predecessor's preventable viewport-save block: inspect hashes and
owner changes **before issuing** the Worker grant. A saved viewport can change
.blend bytes without changing model semantics. Preserve any owner state in a
unique checkpoint, reconcile an actual hash mismatch with available semantic
evidence and record the current input truthfully. Do not falsely label a changed
file byte-identical, reset it, or repeat planning. Record permissible unrelated
owner changes explicitly and exclude them from staging. Unexplained material
scene changes need reconciliation; a stale expected hash is not task design.

## Cooperator intent and site specification

The closure records Michal asking for more forest with meadow edges, landscape
around the entire cottage, a view from the glazing into a distant valley, a large
enclosed garden reserved for later orchard additions, realistic lawn instead of
uniform green ground, and tall grass on the meadows. He accepted v04 for closure.
Master selects the following reversible visualization realization. Proposed
parcel dimensions/topography are scene hypotheses, not surveyed site data.

### 1. Continuous setting with an open valley axis

World axes are model axes: X runs from the wood bay to the glazed gable, Y from
entrance to rear, Z upward. The main glass is at approximately X=14.4 and faces
outward toward +X. Establish an open view generally along +X, with forested side
ridges, descending meadow foreground and receding distant horizons. Do not put
an immediate tree wall across the principal living-room view.

Build a gentle garden terrace and a believable transition to descending ground
outside it. Forested hills should embrace the other sectors and continue around
the valley flanks; 360-degree context does not mean a uniform ring of dense trees.
Use irregular meadow/woodland edges, glades and two or three readable depth layers.
There is no requirement for a river, road, village or another building.

Source fact: v04 `_hill()` derives terrain from the main camera's projected u/v
profiles. Extending those same strips around the house blindly will not create a
coherent valley. Introduce world-space terrain/layout parameters and a common
surface-height query for ground, tree roots, fence and grass. Existing distant
hill/forest groups may be extended, selectively replaced or hidden as required;
preserve their local assets and broadly retain the accepted front composition.
Do not leave overlapping flat terrain covering the valley floor, exposed sheet
backs, holes, abrupt platform edges or a near-cottage cliff.

Preserve ground support beneath the house, existing path/steps/bed, orchard and
accepted foreground fence. Unlike whole 04, **distant SITE_terrain_proxy geometry
is now allowed to change or be replaced** outside a declared protected terrace.
Define that protected zone and contact-height witnesses before mutation. Outside
it, reconnect the terrain smoothly. Keep retained vegetation grounded; any needed
vertical re-grounding must identify exact groups in the current grant.

Choose a bounded terrain extent sufficient for the review views, not an infinite
world. Background distance can increase where useful. Main camera transform,
lens and shifts stay fixed; increasing only camera/viewport far clipping is
allowed if required for the newly extended landscape, with before/after recorded.
Do not move the house or camera to manufacture a valley view.

### 2. A complete garden enclosure

Define one non-self-intersecting garden polygon containing the cottage, orchard,
front path and usable open lawn. An initial envelope roughly 30–40 m across is
a visualization proposal; choose/report a coherent footprint and area rather
than treating that range as an approved boundary. Reserve generous unobstructed
interior space for later fruit trees. Do not add those trees now.

Keep the accepted foreground segment `(16.60,-8.62) → (18.25,1.00)` and its
26 stakes/two rails intact. Continue its ends into the enclosure with credible
corners and anchor posts. Reuse MAT_TIMBER_FENCE, dimensions and rustic character.
New sections follow terrain, connect physically and avoid duplicate corner posts
or rails hanging in air. Use V05-owned extension names so v03's existing fence
ownership/counts remain valid.

Include one simple, closed gate aligned with the existing entrance approach,
with a plausible clear opening, frame and posts. No gate animation is needed.
Align the access route without moving existing slabs; a modest continuation to
the gate is allowed if necessary and explicitly granted. No driveway redesign.
The enclosure must read as a complete property in an overhead/oblique review,
not four disconnected foreground props. Do not force the existing segment into
an inaccurate axis-aligned rectangle.

### 3. Short lawn and tall meadow as distinct systems

Inside the enclosure: maintained lawn, mainly 4–10 cm blades, real short-grass
geometry over a PBR turf/thatch base. It must improve the large exposed ground
areas, not merely add more isolated weeds along the fence. Use restrained green,
olive and dry/thatch variation, bent/tapered blades, irregular density and real
micro-shadows. Avoid neon green, thick spikes, obvious tile borders and noisy
displacement pretending to be grass.

Outside the garden and on forest-edge/valley meadows: unmown grass around
25–65 cm with finer stems and occasional seed heads/dry strands. Meadow edges
and tree-group gaps should be visibly different from the maintained garden.
Retain the garden's front ornamental bed. No dense meadow on the path, steps,
paving, gate swing/access, under the house or through fence posts.

Use the same garden polygon and terrain surface to derive lawn/meadow/clearance
masks. Ground vegetation everywhere on its actual supporting surface. Keep
some geometric coverage throughout the garden and review sectors; do not make
the opposite side bare because CAM_A_REFERENCE cannot see it. Use spatial chunks,
linked low-detail patches or Geometry Nodes instances, not one object per blade
or realized copies across the whole landscape. Higher detail can be concentrated
near observers; disclose quality controls so orbiting remains usable.

Reuse `grass_medium_01` masters/maps for suitable meadow clumps. For short turf,
derive appropriate fine-blade patches or select/rework a suitable existing tuft;
do not squash a bush uniformly into a rubber mat. Keep green/dry material variants
on dedicated V05 materials so existing front planting does not change globally.

## Small, concrete new asset input

Master checked [ambientCG Grass005](https://ambientcg.com/view?id=Grass005) and
its [official license](https://docs.ambientcg.com/license/) on 2026-11-15. It is
listed as a short clean-lawn PBR material, created procedurally with bitmap
elements, under CC0; do not call it a verified photoscan. Select its 1K/2K JPG
maps initially as the turf base, then verify actual scale and appearance locally.
Retain only the required color, roughness and appropriate normal maps; large
displacement maps and 4K/8K sets are unnecessary. A PBR base alone is insufficient:
the accepted outcome also needs real blades.

Use the current official asset/download metadata rather than guessing archive
members or CDN paths. Master has not downloaded/imported this set. One targeted
fallback to [Grass001](https://ambientcg.com/view?id=Grass001) is allowed if the
selected turf is unavailable or visually unsuitable. No open-ended library hunt,
new tree purchases, accounts, add-ons or runtime installation. Document a real
missing input once instead of repeatedly retrying it.

Add exact asset paths/URLs, license, map interpretation, scale, hashes and any
derivation to assets/ASSET_MANIFEST.md. Preserve current CC-BY credits for tree
assets and redistribution notices. Keep used maps portable and packed in v05
where practical, with reproducible relative source paths. New raw download caches
may remain in granted gitignored work/; retained project data must rebuild offline.

## Finite delegation and source ownership

Open 00_notes.md with handout revalidation. Normal initial coordinates:

| Task | Prompt | Report |
|---|---|---|
| Planner: fresh 01/01, native Plan Mode required | 01_planning_00.md | 01_report_00.md |
| Implementation: healthy same Worker 01/02, Plan Mode not-used | 01_implementation_01.md | 01_report_01.md |

Keep actual consumed coordinates; extra exchanges never overwrite an outcome.
The concise plan answers: protected terrace and world-space valley layout;
garden polygon/gate; grass masks/LOD and budget; exact source/output scope and
review poses. It should use your MCP observations and existing local asset
inventory, not repeat the previous discovery. Resolve the known native Plan
Mode report-write limitation by naming a capable exact-content persister/relay
before delivery. A completed plan does not need another planning cycle to save it.

One implementation stream, with finite milestones: (1) low-detail terrain,
enclosure and sightline; (2) forest extension and grass zones at measured density;
(3) verification and evidence. Permit two cheap composition/performance previews
and one focused correction for a concrete defect. No separate repeated audit or
unbounded scattering/density escalation.

Use a reusable deterministic `scripts/site_v05.py` refinement and a `site_v05`
JSON section for terrain extent/valley axis, protected terrace, garden boundary,
gate, masks, seeds, LOD and review cameras. Invoke the same refinement through
MCP and after v03/v04 in scripts/build_scene.py, before packing/saving. Preserve
scripts/timber_fence_v03.py and scripts/landscape_v04.py and normalized v04
libraries. Own V05 outputs explicitly; reapplying the refinement must not duplicate
fence, grass or trees or perturb the generator's global random stream.

Grant exact project paths for module/builder/JSON, selected maps/manifest, v05
scene and temporary checkpoints/replay; exact live MCP effects; and exact Meta
report/evidence/run-map writes. Auxiliary review cameras and a necessary gate
approach extension require explicit inclusion. Narrow current-file/replay/MCP
documentation updates may touch AGENTS.md, README_SK.md and docs/OPERATIONS.md;
the managed AP block and entire Closure and Git gates section stay byte-identical.
Do not ask Workers to repeat the literal closure signal in plans/reports.

Protect seed/v01/v02/v03/v04, reference, architecture/roof/openings, furniture,
chimney/fireplace, glazing, lights/world, accepted timber/UVs, original foreground
fence and AP pin/history. Unrelated owner work is not staged or reset. Project
commit/non-force publication must be covered by current explicit authority and
expected parent; Meta Git belongs to Michal and completed pairs are first-added
together. Project-authored Linux shell scripts use fish.

## Verification and practical budget

Retain C1 at `[21.5,-10.0,1.25]`, target `[8.5,2.5,1.25]`, 35 mm, 36 mm sensor,
shift_x 0, shift_y 0.105. Auxiliary cameras do not replace it. Restore it active
for the saved final project; any far-clipping-only change is disclosed.

Measure a small grass patch and representative terrain sector before multiplying
density. Reuse meshes/materials and avoid realizing the forest/grass. Keep unique
evaluated geometry below the existing 3-million ceiling and every tracked file
below 90 MiB. Aim to stay below roughly 3 GiB render-process RSS on the observed
8 GiB M1; measure actual behavior and reduce distant density/LOD if necessary.
These are working budgets, not a hardware capability claim. Do not solve density
problems with new storage/toolchains or maximum-resolution textures.

Required deliverables in addition to project `blender/kysucka_chata_mcp_v05.blend`
and its source/assets, under this Meta whole:

- `renders/before.png` / `renders/after.png`: matched C1 1448 × 1086, Cycles CPU,
  96 samples, OIDN ON, frame/seed 0, AgX look None, exposure 0, gamma 1 and unchanged
  lighting/world. Reuse predecessor baseline only after verifying actual profile;
  otherwise render it fresh. Do not claim uploaded chat bytes match archive hashes.
- `renders/site_overview.png`: an oblique/overhead view proving the entire fence,
  gate, garden, grass zones and transition toward the valley; label/reproduce pose.
- `renders/valley_from_inside.png`: eye-level view from inside the living/dining
  space through unchanged glass toward +X, with actual sloping foreground, side
  ridges and distant depth. Camera origin must really be inside, around floor
  level plus normal eye height; do not hide glass/partitions or use an exterior
  camera to fake the result. Record pose, lens and eye height.
- `renders/orbit_sheet.png`: four labelled inexpensive exterior views covering
  different sides, sufficient to reveal missing terrain, forest seams or a fence
  that fails to enclose the property. Final-quality rendering of every orbit view
  is unnecessary; fix common settings and record poses.
- `renders/grass_details.png`: native-pixel short-lawn and tall-meadow evidence,
  with source views/crop bounds. At least the main render must visibly improve;
  a close-up alone cannot establish lawn realism across the property.
- `evidence/site_comparison.md` and `renders/render_metadata.json`: actual MCP
  change/separate-readback receipts, geometry/mask/clearance and sightline checks,
  asset credits, budgets/timings, source replay, hashes and honest limitations.

Meta ignores JSON by default. Tell Michal the exact new metadata path requiring
explicit forced staging with the completed archive; no ignore-policy change or
historical archival investigation is needed.

You inspect the saved scene and images through MCP yourself. Check grounded
stakes/rails and physically connected enclosure/gate, no boundary self-crossing,
clear approach, usable empty future-orchard space, terrace contact preservation,
unblocked valley view, no grass on hard surfaces and no flat-color blanket lawn.
Vegetation may change shadows/reflections naturally; unchanged-data checks do
not mean identical pixels.

Cold reopen must resolve all data. Factory-startup replay into disposable work/
must reproduce the new semantic layout/materials, terrain support, masks and
instances within declared scale-appropriate tolerances; a second application
must be idempotent. Do not gate on binary .blend identity or full cross-version
UI/default-RNA dumps. Preserve actual unmodified scene data, not obsolete global
object counts. One render job at a time; use working MCP submission/polling if
a render exceeds a tool call, never blindly resubmit after a timeout.

Closeout normally returns 01_closure.md, exact candidate SHA when publication is
granted, v05 path/hash, review images/poses, source/license/performance evidence,
saved/idle status, expired grants and Michal's actual feedback or NOT TESTED.
Technical delivery and subjective acceptance remain distinct. Only this whole's
Orchestrator closes it; Master then selects the next whole. Carry forward the
grey sky/daylight/dark soffit, visible fireplace/coherent chimney and ambiguous
interior slab. Only one exterior D01_leaf exists; do not delete a supposed second
door in this site whole. Architectural checking remains deferred.

## Master run-map snapshot

Mechanically persist this Master-authored snapshot under an exact grant at
projects/kysucka_moderna_chata/00/00_RUN_MAP.md, reconciling newer content instead
of overwriting blindly. Discovery only; it grants no execution authority.

```text
Run map: kysucka-moderna-chata-reference-visualization
Run objective: converge the editable scene toward reference/kysucka_chata_moderna.png and Michal's selected spatial garden/valley vision; architectural checking is deferred
Run map authority: discovery-only
Run entry: 00 | kysucka-moderna-chata-ap-meta-initialization | closed | depends on: none | handout: projects/kysucka_moderna_chata/00/00-init/00_handout.md | evidence: project foundation b47cce6f91ae10a22fb708a8e5220ab27b471aeb
Run entry: 01 | kysucka-moderna-chata-blender-mcp-first-reference-render | closed | depends on: kysucka-moderna-chata-ap-meta-initialization | handout: projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_handout.md | evidence: public f0fb0ea25fcd091ff05e5e3717c433c586cac4fa, v01 and MCP framing comparison
Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | closed | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: public d67431d1678de511e06a8ad04cd632ae4899cdc4, v02 C1 and camera comparison
Run entry: 03 | kysucka-moderna-chata-realistic-timber-and-foreground-fence | closed | depends on: kysucka-moderna-chata-reference-camera-perspective | handout: projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/00_handout.md | evidence: public 623d12abe0c0eb2742cd02c9962c1712b53437e2, v03 timber/fence and semantic replay
Run entry: 04 | kysucka-moderna-chata-kysuce-forest-and-natural-garden | closed | depends on: kysucka-moderna-chata-realistic-timber-and-foreground-fence | handout: projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/00_handout.md | evidence: public f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c, v04, supplied closure/acceptance and forest/orchard/planting result; closure trace not yet public at Master's observation
Run entry: 05 | kysucka-moderna-chata-spatial-site-valley-and-grass | provisional | depends on: kysucka-moderna-chata-kysuce-forest-and-natural-garden | handout: projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/00_handout.md | evidence: Michal requests all-around terrain/forest with meadow edges, valley vista from glass, enclosed large garden, realistic short lawn and tall meadow grass; Master selects their coherent site realization with multiple-view verification
```
