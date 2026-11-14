# Realistic timber and foreground fence — logical whole 03

Handout status: provisional
Author: read-only Master Chat Orchestrator
Author session scope: development-run
Development run identity: kysucka-moderna-chata-reference-visualization
Recipient access profile: Orchestrator
Recipient session scope: logical-whole
Logical whole identity: kysucka-moderna-chata-realistic-timber-and-foreground-fence
Destination: cisarik/meta, projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/00_handout.md
Prepared: 2026-11-14, Europe/Bratislava
Artifact lifecycle: provisional operational handoff, linked from the Master run map; freeze when this whole opens and retain as historical evidence; consumer this whole's Fresh Orchestrator; cleanup owner COOPERATOR under an exact grant

🟡 Ready for manual delivery
Capability profile: Orchestrator, fresh session, functioning Blender MCP
Recommendation: Medium reasoning; enough context for the pinned AP spine and this bounded whole
Native Plan Mode: OFF for Orchestrator coordination; ON for the first Planner exchange
Archival: this is a handout, not a Worker exchange; prompt/report pairs wait for the actual report

## Outcome and operating posture

Produce a visibly better **timber facade and rustic foreground fence**, starting
from v02 and keeping its selected camera. The fence must also occupy the lower
foreground like the reference. Deliver editable v03, reproducible source changes,
portable textures and matched renders. This is one exterior-timber whole, with
material appearance and fence placement both required; neither is a vague optional
follow-up. Overall photorealism and architectural verification are later concerns.

You generate task-specific English prompts for a short Planner exchange and an
implementation Worker. You and the Workers have functioning Blender MCP. Inspect
the actual active file and reference yourself through MCP before delegation;
inspect the saved result and rendered pixels yourself at acceptance. Master
remains read-only and supplies context, not executable Worker authority.

Communicate with Michal in Slovak, masculine address and feminine self-reference.
Reports are English and start `### Report for ORCHESTRATOR_CHAT`. Keep manual
Cooperator delivery and his selected model. Do not turn this into AP setup, MCP
installation, asset-library research, a broad audit or repeated planning.

## Evidence and accepted boundary

Master checked public project commit/tree and focused source blobs on 2026-11-14:

| Source | Anchor |
|---|---|
| Project https://github.com/cisarik/kysucka_moderna_chata, main | `d67431d1678de511e06a8ad04cd632ae4899cdc4` |
| Project .ap gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` |
| Meta https://github.com/cisarik/meta, main | `4db94c333340c6b77d06701d050de286c701dabc` |

The returned `02-reference-camera-perspective/01_closure.md` closes that camera
whole on the published project commit. Master read the supplied closure,
`camera_comparison.md`, `cooperator_residuals.md`, candidate sheet and renders,
and compared the images to the original reference. The whole-02 packet is not
yet in the inspected public Meta tree. Use Michal's exact supplied files/local
trace as predecessor evidence; do not call them publicly archived. This archival
gap does not invalidate the public project or justify a repair whole. Meta Git
archival remains Cooperator-owned; preserve historical reports unchanged.

Start scene: `blender/kysucka_chata_mcp_v02.blend`; closure-recorded SHA-256
`010f47a81a4fde2e936f401e87b8bc11af76a8e72d71811d68dd910da0b27249`.
Reference: `reference/kysucka_chata_moderna.png`, 1448 × 1086, SHA-256
`05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`.
Current `model/parameters.json` SHA-256:
`2d441b08d658e4aa4c8fccc5e71c76eb16666deeb4401cdd0b973c379901cada`.
Current `scripts/build_scene.py` SHA-256:
`4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`.

Lock `CAM_A_REFERENCE`: location `[21.5,-10.0,1.25]`, target `[8.5,2.5,1.25]`,
35 mm lens, 36 mm sensor, shift_x 0, shift_y 0.105. C1 improved the approximate
envelope score from 32.70 to 29.11 reference pixels and facade/gable ratio from
1.9661 to 2.2069 against 2.1818. These support a bounded camera choice, not exact
physical reconstruction or Michal's acceptance of the overall visualization.

Read current project AGENTS.md, focused operations/source, pinned AP.md,
AP_ORCHESTRATOR.md and PROMPT_CONTRACTS.md, and Meta's naming contract. Reconcile
actual physical roots, origin, commit, dirty state and input hashes. The current
local GUI state is unknown to Master. Preserve unsaved owner work before opening
or modifying anything. Use new checkpoints and v03; never resave seed/v01/v02.

Renew `blender-mcp-live-v1` explicitly in current prompts for this whole's live
reads, authorized timber/fence changes, checkpoints, saves, renders and readback.
Whole-02 authority expired. Existing protocol-version warnings were non-blocking;
they do not select an upgrade. CLI supports source work, hashing, Git and cold
verification, while actual scene control and acceptance inspection use MCP.

## Cooperator priorities and deferred observations

The closure records Michal's priority verbatim:

> report vygenerovany, dalsi do residual moj brainstorming: plot je inak umiestneny ako na predlohe prvej chcem realisticke drevo aj drevo fasady potrebujem realisticke drevo.

The supplied residuals additionally say the current trees look unrealistic and
the desired result is a convincing architectural visualization without a video-
game appearance; complete photorealism is not required. He wants a recognizable
fireplace with visible fire, and notes the chimney is questionable even in the
original AI image. He did **not** prescribe moving the chimney/fireplace.

Record vegetation, sky/daylight, fireplace visibility and coherent chimney design
as future-scope observations. Do not solve them in this whole or erase them from
closeout. Transparent glass already works in Cycles; its earlier green Material
Preview issue is resolved. Do not compensate for fireplace occlusion with another
camera search, glass replacement or stronger emission.

## Visual specification

### Facade, gable timber and soffit

The reference has warm honey/brown exterior boards with long grain, occasional
knots, restrained differences between boards, readable seams and soft edge
highlights. Aim for that natural timber character. Existing boards already have
geometry and bevels; changing tint or adding more high-frequency noise is not
enough. Avoid plastic gloss, uniformly orange surfaces, deep black grooves,
identical repeating knots, oversized grain and exaggerated bump.

Upgrade visible `CLADDING_front*`, corresponding rear cladding for consistency,
`GABLE_timber*`, `SOFFIT_wood*` and `WOOD_BAY_post*`. Preserve their dimensions,
openings and silhouettes; UVs, material slots and timber shader data may change.
Keep the existing board joints; do not overlay a second texture grid of boards.
Keep other wooden objects outside scope unless explicitly included below.

Source facts worth giving the Planner:

- Existing cladding rows are approximately 0.205 m tall at 0.22 m pitch with
  0.007 m bevels. Use physically plausible grain scale along these boards.
- `MAT_WOOD_H` and `MAT_WOOD_V` are shared with tables, chairs, tree trunks,
  branches and decorative objects. Make dedicated exterior/fence materials and
  reassign exact consumers; do not globally replace the shared materials.
- `beam()` builds members with length along local Z before object rotation.
  Grain must follow each member's actual long axis: facade horizontal, gable
  upright, posts upright, rails longitudinal, soffit within its sloped plane.
  A material named H/V or a global-coordinate stretch does not prove orientation.

Use coherent base color, roughness and normal/bump detail with restrained
per-board variation. Define mapping in real units with stable deterministic
offsets. Color textures use an appropriate color interpretation; data maps use
Non-Color, with the normal convention verified. Avoid heavy displacement and
large subdivision. Preserve believable small-scale relief and edge light.

### Fence appearance and placement

Current `FENCE_post_proxy*` / `FENCE_rail_proxy*` form a straight strip near
Y=-5.8, X≈-1.5..16.8. In C1 it stops near u=0.467, so much of the lower-right
foreground has no fence. This is a geometry/layout residual, not another lens
problem.

Reposition/extend or replace only this fence group as a coherent rustic boundary
in front of the garden. In the reference, its main run crosses the lower frame
from the bottom-left toward the right edge at a higher image position. Using
top-left normalized coordinates, aim broadly for left-edge crossing in the lower
fifth and right-edge crossing in the lower 20–40% band; inspect the actual
reference before fixing anchors. These are composition guides, not surveyed
coordinates. Do not fit isolated stakes at the expense of a sensible 3D line.

Use weathered grey/brown split stakes, mildly irregular tops/spacing/lean and
continuous timber rails with plausible attachments. Grain follows each member;
fence wood is rougher and less saturated than the maintained facade. Keep subtle
edge wear and end grain where visible. Avoid toy-perfect square pickets, extreme
distortion or a bulky barrier covering the entrance, bench and glass. Fence feet
must meet terrain and rails/posts must actually connect. Do not move the house,
path, terrain or camera to make it fit. Inspect endpoint projections and the
whole frame; allow at most two purposeful placement trials before selecting one.

## Assets and source ownership

This handout selects a small PBR-wood route rather than another generic noise
shader. The implementation grant should authorize downloading **at most two
appropriate wood texture sets**, initially 2K, from official Poly Haven or
ambientCG pages after checking each asset/license. Choose surface wood whose
grain works on existing boards, not floorboards with unwanted nails or duplicate
seams. One set may support both finishes if it looks convincing.

Official starting points: https://polyhaven.com/textures and
https://polyhaven.com/license ; https://ambientcg.com and
https://docs.ambientcg.com/license/ . Verify the actual selected asset, map files,
license and mapping scale; these links are discovery, not a preselected asset.
No paid assets, accounts, executables, add-on installation or external generator.
If downloads are unavailable, disclose the missing input and return the exact
decision needed; do not silently substitute another placeholder as success.

Keep the used maps under a small exact `assets/textures/wood/` allowlist, with an
`assets/ASSET_MANIFEST.md` recording asset/page/license URLs, downloaded filenames,
map roles, resolution, physical scale if known, SHA-256 and all modifications.
Pack used images into v03 and retain portable relative source paths. Aim for
total new assets plus v03 below 80 MiB and every tracked file below 90 MiB; select
smaller maps if needed, rather than introducing Git LFS or another storage system.

Synchronize the accepted result with `model/parameters.json` and the procedural
source. Store timber/mapping targets and fence geometry parameters explicitly.
Use a small reusable refinement function/module if helpful; invoke the same logic
through MCP and from `scripts/build_scene.py`. Grant its exact path before work.
No manual-only final scene, duplicate cumulative fence or auto-run handler.
Use local deterministic variation: inserting random draws in the generator's
global stream would otherwise change the later trees, which are outside scope.

Verify a source replay into a disposable `work/` scene for the modified groups,
without replacing the active owner scene. Require material assignments, mapping,
texture availability and fence transforms to agree within stated tolerances;
binary .blend identity is unnecessary. Do not regenerate CAD/PDF or redesign the
building. Protect unrelated groups from source-replay drift.

## Finite delegation and mutation boundary

Open `00_notes.md` with handout revalidation. Use normal coordinates:

| Role / session / exchange | Prompt | Report |
|---|---|---|
| Planner, fresh 01/01, native Plan Mode required | `01_planning_00.md` | `01_report_00.md` |
| Implementation, healthy same session 01/02, Plan Mode not-used | `01_implementation_01.md` | `01_report_01.md` |

The Planner answers only: selected wood assets/mapping and exact consumers; one
fence layout method; minimal source/output allowlist; preservation and acceptance.
Reuse your MCP observations. One concise decision-complete plan, then a complete
implementation grant. A fresh Worker is needed only for a real continuity or
capability reason; do not create an audit chain for this reversible slice.

The prior native Plan Mode could not write the report file. Select a satisfiable
completion route **before delivery**: ordinarily relay the complete Planner
report in-session to the explicitly named capable Fresh Orchestrator persister
on that demonstrated client limitation. Grant exact persistence/readback and
keep status truthful. Do not bypass native restrictions or launch another planning
cycle merely to save an already complete plan. Implementation Worker normally
persists its own report under an exact grant.

Issue coherent positive authority for all three mutation axes: exact project
source/assets/v03 paths; live Blender timber/fence/checkpoint/render effects;
exact Meta reports/evidence/run-map writes. Downloads and any temporary replay
scene need explicit inclusion. Potential ancillary documentation changes are
only current-file, source-replay, asset and MCP-route sections of AGENTS.md,
docs/OPERATIONS.md and README_SK.md. Keep the managed AP block and entire
`Closure and Git gates` section byte-identical. Do not ask Workers to reproduce
the literal closure signal in a report, plan or replacement governance text.

Preserve camera, building/openings, roof, chimney/fireplace, furniture, lights,
world, glass, vegetation, terrain, path and other materials, plus reference,
seed/v01/v02, .ap pin and historical artifacts. Scope project commit/non-force
publication explicitly against the verified expected parent; no blanket staging.
Meta prompts/notes are Orchestrator-authored, reports retain actual authorship,
Meta Git belongs to Michal, and completed prompt/report pairs are first-added
together. No history rewriting or unrelated configuration repair.

## Required evidence, acceptance and closeout

Deliver `blender/kysucka_chata_mcp_v03.blend`, synchronized source/assets, and in
this Meta whole:

- `renders/before.png` and `renders/after.png`: matched C1, 1448 × 1086, Cycles
  CPU, 96 samples, denoising ON for both, fixed frame/seed and identical AgX look,
  exposure, lights/world and other sampling settings. Baseline is freshly rendered
  v02 under that same profile; do not compare a noisy 640 px predecessor to a
  denoised larger final. Cheap working previews are allowed. Use one render job
  at a time and the known working MCP submission/poll route if a render outlasts
  a tool call; never resubmit blindly after a timeout.
- `renders/timber_details.png`: labelled before/after facade and fence crops
  from those actual renders, with crop coordinates recorded; no AI retouching.
- `evidence/timber_fence_comparison.md`: actual MCP read/change/separate readback,
  selected asset/mapping explanation, reference comparison, fence world endpoints
  and projections, source-replay result and honest residuals.
- `renders/render_metadata.json`: actual scene/camera/render identities, settings,
  device, file hashes and relevant preservation observations. Meta ignores JSON;
  notify Cooperator that this exact evidence file needs explicit forced inclusion
  when he stages the completed archive, not a broad ignore-rule change.

Judge actual pixels: grain/knots and board variation should be readable at facade
and fence scale, without stretching, obvious repetitions or plastic highlights.
Fence placement must improve the reference composition with connected geometry
and grounded stakes. A texture-load receipt or node graph alone is not success.

You inspect MCP output yourself, verify locked camera and non-target state, cold
reopen v03 with textures present, verify source replay and record exact published
candidate when publication is granted. Do not call same-session checks an
independent Worker audit. Permit one focused correction for a concrete defect;
do not append trees, sky or fireplace work to consume remaining context.

Return normally `01_closure.md`, project SHA, v03 path/hash, comparison images,
asset/source evidence, expired grants and saved/idle status, plus Michal's actual
feedback or NOT TESTED. Distinguish technical delivery from subjective visual
acceptance. Only this whole's Orchestrator closes this whole after its gates;
Master then selects the next scope from the packet and Cooperator feedback.

## Master run-map snapshot

Under an explicit exact-path grant, mechanically persist the following at
`projects/kysucka_moderna_chata/00/00_RUN_MAP.md`, reconciling any newer content
instead of overwriting it blindly. This Master-authored map is discovery-only;
it neither issues Worker authority nor rewrites predecessor records.

```text
Run map: kysucka-moderna-chata-reference-visualization
Run objective: converge the editable Blender scene toward reference/kysucka_chata_moderna.png; architectural checking is deferred
Run map authority: discovery-only
Run entry: 00 | kysucka-moderna-chata-ap-meta-initialization | closed | depends on: none | handout: projects/kysucka_moderna_chata/00/00-init/00_handout.md | evidence: project foundation at b47cce6f91ae10a22fb708a8e5220ab27b471aeb
Run entry: 01 | kysucka-moderna-chata-blender-mcp-first-reference-render | closed | depends on: kysucka-moderna-chata-ap-meta-initialization | handout: projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_handout.md | evidence: public f0fb0ea25fcd091ff05e5e3717c433c586cac4fa, v01, MCP scene control and framing comparison
Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | closed | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: public project d67431d1678de511e06a8ad04cd632ae4899cdc4, v02 C1 35 mm, supplied closure and three-candidate comparison; public Meta archival pending at Master's observation
Run entry: 03 | kysucka-moderna-chata-realistic-timber-and-foreground-fence | provisional | depends on: kysucka-moderna-chata-reference-camera-perspective | handout: projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/00_handout.md | evidence: Michal prioritizes realistic facade/fence wood and observes fence placement mismatch; Master selects a bounded timber/fence whole with camera locked; vegetation and fireplace remain recorded residuals
```
