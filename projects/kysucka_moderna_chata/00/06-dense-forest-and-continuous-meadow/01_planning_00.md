# Dense forest and continuous meadow — implementation plan

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-dense-forest-and-continuous-meadow
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: V06-VEGETATION-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — coverage/canopy morphology, linked LOD, real render-device evidence and protected local-source recovery must form one bounded design
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Worker topology: single-active

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and live-scene-grounded vegetation, review-camera, replay and render-profile design
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

## Outcome and preservation

Produce one concise, decision-complete implementation plan for local v06. The
selected result is visibly layered connected forest including the far ridge,
continuous natural meadow lower/mid cover, and believable bent short lawn on the
preserved v05 spatial foundation. Do not turn this into architectural, glass,
lighting, entry or interior work. Do not inherit v05 as a visual PASS.

Current Coordinate/Surface selections are fixed: manual delivery; fresh Planner
01/01 with actual native Plan Mode ON; then, after an accepted plan, one complete
new 01/02 implementation grant to the same healthy session with Plan Mode OFF.
Verify this really is a fresh session and actual Plan Mode is ON. Read-only work
and plan preparation are the only substantive authorities here. Do not implement,
save/render/reopen a scene, alter its viewport/material/UI state, download assets,
change hardware preferences or install/update anything.

Cooperator-facing chat is Slovak, masculine address; prompt/report are English.
The standard report begins `### Report for ORCHESTRATOR_CHAT`. Do not reproduce
the project's literal closure signal.

## Verified anchors

Working directory: /home/agile/Projects/kysucka_moderna_chata
Repository identity: https://github.com/cisarik/kysucka_moderna_chata.git
Repository checkout topology: standalone checkout, main
HEAD and independently read public main: f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50, .ap checkout equals gitlink
Trace: https://github.com/cisarik/meta.git at /home/agile/meta, HEAD/public main bb274bdd179e1038da0d3679fea214dd81128fe4
Orchestrator notes: /home/agile/meta/projects/kysucka_moderna_chata/00/06-dense-forest-and-continuous-meadow/00_notes.md
Previous technical evidence: /home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/

Public main is v04, not the v06 input. Intentional local v05 changes/untracked
inputs are `AGENTS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`,
`docs/OPERATIONS.md`, `model/parameters.json`, `scripts/build_scene.py`,
`scripts/site_v05.py`, three `assets/textures/grass/Grass005/Grass005_1K-JPG_*.jpg`
and `blender/kysucka_chata_mcp_v05.blend`. Preserve them all; do not require a
clean tree. The project index is empty. Unrelated Meta `projects/kronika/` and
all other owner work remain untouched.

Required exact input hashes:

- `blender/kysucka_chata_mcp_v05.blend`: c3bd3d5e847c52d33a60f3f89cf4392da85a24df96fe7774a25a37bd39d8fafe
- `model/parameters.json`: 66ed4d7246ca211a55d3067a4b14f50e8af706efc669c4dd4911c7c0c1d2d664
- `scripts/build_scene.py`: 9c7863c125c74f2894529ad247f8d5eb8f9b756f3f1af26dd8be094ebd7a8c6b
- `scripts/site_v05.py`: f6f122dbacb293bb8a90f748583555516c8d57344112c47a62eba172afb821aa
- `scripts/landscape_v04.py`: 950d23c79bc50b26a1c606cff36605923a1c172b660f15945f58faf9beceb723
- `scripts/timber_fence_v03.py`: f94dce1b2da5c07d4064f8ac800304ce3e4c04372447eb737ac2a51aa73fcf98
- `assets/ASSET_MANIFEST.md`: b332a064bf63c62d2458fa79208402d4ba760e46768e4287e405d4f22c0ff584
- `reference/kysucka_chata_moderna.png`: 05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96

`./.ap/ap doctor` directly passes. Current Blender is 5.3.0 at
`/home/agile/Applications/Blender/blender`; existing MCP at 127.0.0.1:9876 is
reachable and reads v05 successfully (4,166 objects, saved and not dirty,
C1 active). No render job is active. Current RAM availability at the latest
snapshot is about 18.7 GiB (not a reserved budget). RTX 3080 is 10,240 MiB
with ordinary desktop/Blender occupancy. Device preference entries are
localhost observations only, not proof of GPU rendering.

## Mandatory reading and inspection

Read the governing WORKER spine in `.ap/AP.md` (authority capsule anchors),
`.ap/AP_WORKER.md` Worker Session Target and Reporting, and
`.ap/PROMPT_CONTRACTS.md` Worker Report Header, Plan-to-Execution Gate and
trace destination/delivery contracts. Read current `AGENTS.md` and focused
`docs/OPERATIONS.md` v05/CachyOS sections, the Orchestrator notes, the relevant
v05 implementation detector/helpers in `scripts/site_v05.py`, builder ordering in
`scripts/build_scene.py`, and normalized library/credit entries in
`assets/ASSET_MANIFEST.md`. Read the preserved reference and existing whole-05
render images/metadata relevant to forest, meadow/lawn, orbit and valley.

Before deciding widths, stand coverage or memory, measure the actual reusable
master meshes/collection sources and live bounds using read-only local file and
non-mutating MCP inspection. Use the existing `blender-mcp-live-v1` capability
path solely for bounded read-only inspection in this exchange; do not create
saves, preferences or scene mutations. No installation audit is required.
Inspect actual original Grass005 2K map bytes, licences and paths under
`work/downloads/Grass005/`; no download or promotion to an asset path is granted.
Cite actual code and measured bounds, not just historical counts.

## Decisions the plan must settle

Select one coherent option for each item, with compact numeric reasoning and
explicit trade-offs. Keep the design implementable without a second Planner.

1. **Forest/stand coverage and ownership.** Reuse the existing normalized
   Picea abies and Picea mariana libraries. Fuller abies should support near
   woodland edges/valley flanks; mariana can support dense rear layers.
   Populate the visible far ridge around X=240..320 while keeping the +X valley
   corridor open, avoiding a uniform ring, rows, needle-like foreground or a
   solid wall across the valley. Specify irregular stand envelopes, crown-width
   driven overlap/density, measured heights/width variation, young/understorey
   transitions, intentional glades and sector-aware LOD. Say exactly how existing
   V04/V05 forest/populations are reused, hidden, re-grounded or superseded so
   reapplication cannot duplicate vegetation or change global RNG.

   Only if necessary for visible composition, declare a minimal distant terrain
   relief zone outside the protected terrace/enclosure and its exact owned
   terrain data support. Default to preserving the current terrain/service
   except for that precise, declared exception. Every affected tree/grass root
   on modified terrain must sample the resulting actual surface. Do not remodel
   garden/access/global topology.

2. **Continuous meadow design.** Replace center-distance bands, far-half-density
   and the parcel-halo tuft look with deterministic world-space irregular
   ecological patches and gradual forest/slope transitions. Detail a linked,
   reusable set of low/intermediate cover masters plus varied taller stems/seed
   heads (roughly 25–65 cm tallest tips), using existing grass_medium_01
   sources without new asset shopping. State how actual geometry and shaded
   ground base will read as overlapping cover from C1, native low-eye witnesses
   and all four orbits—not merely many isolated tufts. Include green/olive/dry
   variation, sparse meaningful clearings, retained hard-surface clearances,
   normal ray/root-grounding on slopes, and a practical sector LOD approach.

3. **Natural short-lawn masters and ground transition.** Specify bent/tapered
   blades with several lengthwise segments, restrained folded/midrib
   cross-section, twist, varied lean/horizontal growth and lower thatch while
   keeping 4–10 cm scale. Explain root-to-tip color/material/roughness/
   translucency and real micro-shadow variation without emission, lighting
   changes or generalized realization. Preserve opening/step/path/gate clearances
   and make the planting-edge transition soft where appropriate. New V06-owned
   materials/meshes/masters must not alter shared house or source-library data.

4. **Representative trials and actual-scale views.** Choose one small forest/
   meadow/lawn pilot sector and its low-eye/detail cameras, at actual viewing
   scale. Define two purposeful sector/composition trials first, then full-site
   propagation, and one focused correction after full-frame review. State precise
   visual evidence and stop conditions; do not substitute root counts or a
   triangle target for acceptance. Give a new NW/SZ candidate outside crowns or
   higher, with cottage/site readability and no forest hiding. Keep C1 and
   inside-valley camera/optics unchanged. Add an outside-glass diagnostic just
   beyond the glazing with comparable direction/FOV, clearly non-interior.

5. **Render/resource profile and texture decision.** Keep P0 CPU/OIDN as a
   preserved control. Plan one small matched CPU/GPU bridge on a representative
   v05 crop under the existing MCP route. Prefer P1 OPTIX/RTX 3080 with scene
   GPU Compute, initially 96 samples, 1448×1086, OIDN, frame/seed 0, AgX/None,
   exposure 0 and gamma 1; document the bounded departure from inherited CPU-only
   comparisons. Specify verification of selected preferences/devices, actual
   scene device, render/device/monitor logs and RAM/VRAM/timing, with no saved
   preferences. When P1 works, use the same P1 for fresh v05 before and v06
   after. State the bounded fallback to matched CPU only if the existing GPU
   route actually fails—no installs or repeated blind retries. Separate warm GUI
   and cold-process resources; query live availability rather than reserving the
   old 3 GiB. Keep unique and instance-expanded geometry separate.

   Inspect actual Grass005 2K originals. Compare 1K/2K only with identical
   UV/scale/camera/density and current backend. Do not assume 2K improves the
   picture; if selected, specify honest new V06-resolved asset paths and packed
   relative paths, without renaming/rewriting prior assets. State actual RAM/VRAM
   headroom and file-packaging concerns separately; no Git LFS.

6. **Source/replay/acceptance package.** Specify a small deterministic
   `scripts/vegetation_v06.py::apply_v06(scene,P,ROOT)` using isolated RNG,
   idempotent owned data, one call after apply_v03/v04/v05 in
   `scripts/build_scene.py` before pack/save, and the same call from live MCP.
   Source replay is from the preserved v05 source packet; semantic layout,
   materials/instances and tolerances must match, without binary/complete-RNA
   comparisons. Cold reopen must resolve all assets. Define positive/negative
   protected witnesses (C1, architecture, glass/world/lights/interior, v03
   timber, enclosure/gate/paving, orchard, seed/v01-v05/reference/AP).
   Restored saved scene must be C1, saved, clean and idle.

Plan the exact changed paths and temporary outputs. In particular:
`work/baselines/v05-pre-v06/` is the protected compact recovery packet, whose
manifest/hashes/relevant tracked diff must be captured before overlapping edits.
Original `blender/kysucka_chata_mcp_v05.blend` stays byte-identical and is hashed,
not overwritten or archived with unrelated files. Worker never cleans this
packet. The only scene product is `blender/kysucka_chata_mcp_v06.blend`.
Use a separately granted owner-state checkpoint and bounded temporary paths in
`work/`; do not claim those paths exist yet.

The required later Meta package is this whole's `renders/before.png`, `after.png`,
`vegetation_details.png`, `orbit_sheet.png`, `site_overview.png`,
`valley_from_inside.png`, `valley_exterior_diagnostic.png`,
`renders/render_metadata.json`, and `evidence/vegetation_comparison.md`.
Native before/after details must witness blades/thatch, meadow lower/mid cover,
forest edge and far canopy with crop/source provenance and no retouching or AI
repair. `AGENTS.md`, `README_SK.md` and `docs/OPERATIONS.md` may receive only
minimal current-v06/profile documentation later; the managed AP block and the
entire Closure and Git gates section remain byte-identical. No CAD/PDF work.
The metadata JSON will later need explicit Cooperator forced staging; do not
alter ignore rules or perform Git now.

## Authority and execution gates

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/06-dense-forest-and-continuous-meadow/01_planning_00.md only if byte-identical to the received prompt and absent of any mismatch; never overwrite it

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/06-dense-forest-and-continuous-meadow
Trace project key: projects/kysucka_moderna_chata
Trace logical-whole projection identity: 06-dense-forest-and-continuous-meadow
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/06-dense-forest-and-continuous-meadow
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — exact-content relay because the native Plan Mode report-write limitation is anticipated
Git publication owner: COOPERATOR
Archival: wait-for-report

Positive authority: read-only source/repository/asset inspection, read-only Git,
hardware/process queries, and bounded read-only live MCP. Verify physical roots,
canonical origins, exact HEAD/public state, AP pin, source/input hashes, permitted
dirty/untracked state, current v05 path and saved/not-dirty state. Classify the
intentional local changes as accepted-continuation plus unpublished-candidate;
unrelated owner work stays outside scope. A changed prerequisite stops the plan.

Git authority: read-only; no fetch, stage, commit, push, submodule update, stash,
reset, restore, checkout mutation or clean. Network authority: no downloads,
research or provider calls. Secrets: none. No subagents, temporary scene copies,
checkpoint/baseline-packet creation, source writes, renders, image generation or
scene reopen/manipulation. No new cameras or new maps. No scene pref/user-pref or
host configuration writes. All other filesystem writes are prohibited; the
report returns in-session instead of violating Plan Mode restrictions.

The live route is read-only in this exchange. Already observed v05 state: C1
location [21.5,-10,1.25], lens 35 mm, sensor 36 mm, shift 0/0.105, clip_end
500; Cycles CPU/OIDN, 96 samples, 1448×1086, frame/seed 0, AgX/None. Glass
roughness 0.07/transmission 1/IOR 1.45, world/lights/fireplace/interior are
protected even though the interior camera remains blurred. Do not hide panes,
alter glass/fire/reflections or lighting.

Evidence tier: E0
Evidence tier basis: read-only technical plan and exact prompt evidence
Independent acceptance: not-required
Implementation authority: not granted

## Finishing and report

Recheck current prerequisites before terminal output. Return PASS only if every
numbered decision has a concrete coherent answer plus exact proposed allowlist,
checkpoints, validation/stop conditions, and a feasible same-session 01/02
implementation route. Return PARTIAL or BLOCKED for missing evidence; this
prompt never grants authority to fill gaps by mutation. Preserve the first
causal failure.

Required terminal status: report exactly one actual outcome — PASS, PARTIAL or BLOCKED
Phase-qualified result: not-applicable
Report justification: new-evidence
Logical-whole closure: not-closed

Return the complete standard terminal report in-session. Include coordinates
once, target/mode/profile/task identity, start/end commit, no changed source,
inspection/hash evidence, the selected plan with actual numeric rationale,
remaining risks/novel questions/rejected alternatives, required validation,
one smallest next step, real issues/near-misses or none, pre-existing failure
classification, and a complete compact Orchestration critique. State explicitly
that no implementation or visual acceptance is claimed. Because the ORCHESTRATOR
is the named exact-content report relay, provide the complete report text ready
for byte-exact persistence, not a native-plan fragment. The relay preserves
Worker authorship and will not replan to save it. If full output cannot be
returned, state that limitation; do not use another tool to bypass Plan Mode.

Authority expiry: terminal report, cancellation or supersession ends this grant;
no autonomous continuation, implementation, acceptance, publication or closure.
