# V07 implementation — forest age variation and connected gravel trail

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-forest-age-variation-and-gravel-trail
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (same-session continuation of Planner 01/01)
Phase: implementation
Task identity: FOREST-TRAIL-V07-IMPL — one bounded editable v07 candidate with validated evidence
Delivery route: manual Cooperator delivery
Continuity anchor: terminal planning report `01_report_00.md` (SHA-256 `63b42bcc2b3c6865d844570d1185dc929ddc9f0886319f1a1c0c5043de6a8a5e`) for FOREST-TRAIL-V07-PLAN, exchange 01/01, accepted by this whole's ORCHESTRATOR on 2026-11-17 (record in `00_notes.md`)
Authority renewal: prior planning authority expired at that terminal report; this prompt grants complete new bounded implementation authority. Retained context is convenience, not authority. Re-gate repository and environment yourself; stop on any conflict between retained context and current evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: live mutation of a 152 MiB packed instanced scene, idempotent selective transforms, finite-boundary route geometry, serialized resource-bounded renders
Recommended context capacity: approximately 250k tokens

## Binding specification and goal

The accepted plan `01_report_00.md` at the exact hash above is the binding
technical specification; re-read it fully before mutation. This prompt
controls authority; where it differs from the plan, this prompt wins.
Implement exactly its §§2–5 within the boundaries below.

One coherent outcome: editable `blender/kysucka_chata_mcp_v07.blend` with
(a) 649 uniform-0.5 half-size replacements inside a final forest population
of 12,977 (12,833 existing + 144 crest additions), including the eleven
reserved route-clearance replacements; (b) restrained mature-canopy
variation and ≤384 edge MARIANA→ABIES prototype swaps; (c) irregular crest
completion with two glades and an open near valley; (d) one continuous
gate→north-terrain-boundary gravel trail with the disclosed threshold
transition, gravel material, footprint-accurate clearance and soft
shoulders; (e) owned V07 terrain derivatives limited to the declared
corridor; (f) recovery packet, pilots, one complete candidate, at most one
focused correction, source replay + idempotence + cold proof; (g) the
required native evidence and a clean saved C1/P0 idle final state.

Accepted decisions (do not reopen): exterior 0.5 compression is part of v06
— never reapply/undo; C1 optics and P0 profile exact (Cycles CPU, FIXED 8
threads, 96 samples, OIDN Accurate/High, adaptive 0.01/min 0, frame/seed 0,
AgX/None, exposure 0, gamma 1, 1448×1086@100%); preserve reference/S00/
v01–v06, house/roof/openings, glazing/fireplace/interior, world/lights,
garden polygon/fence/gate position except the exact threshold transition,
original paving, v03 timber, orchard/fruit, prior credits, all 18 existing
JSON sections and v03/v04/v05/v06 modules; no new tree pack/mesh/material
for trees; no realization, no global orphan purge, no V06 meadow
regeneration for previews; one continuous route (no fork requirement); no
GPU/P1 attempt, no driver/preference changes, serialize heavy jobs; fish
for project-authored Linux shell scripts; managed AP block and entire
Closure and Git gates section of AGENTS.md byte-identical; no CAD/PDF; no
Git write of any kind; Worker never emits the literal project closure
signal; visual acceptance belongs to ORCHESTRATOR image inspection and
COOPERATOR feedback, not to this grant.

## Repository gate and exact baseline

Working directory R = `/home/agile/Projects/kysucka_moderna_chata`;
trace T = `/home/agile/meta/projects/kysucka_moderna_chata/00/07-forest-age-variation-and-gravel-trail`.
Project origin `https://github.com/cisarik/kysucka_moderna_chata.git`,
branch main, expected HEAD `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`
(public main equal at planning). Expected differences: modified tracked
`AGENTS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`,
`docs/OPERATIONS.md`, `model/parameters.json`, `scripts/build_scene.py`;
untracked `assets/textures/grass/`, `blender/kysucka_chata_mcp_v05.blend`,
`blender/kysucka_chata_mcp_v06.blend`, `scripts/site_v05.py`,
`scripts/vegetation_v06.py` (accepted-continuation / unpublished-candidate
owner work). Meta origin `https://github.com/cisarik/meta.git`, HEAD
`bb274bdd179e1038da0d3679fea214dd81128fe4`; its modified run map and
untracked whole-05/06/07 + `projects/kronika/` are preserved owner work.
AP gitlink = checkout `d7023cf037f6d17885c3ede5c04812c61640da50`.

Input SHA-256 (re-verify before mutation and before reporting):

| File | SHA-256 |
|---|---|
| blender/kysucka_chata_mcp_v06.blend | `059eaa947d64ecb1a0e3b15c2a380f800b827c54d4a1a7dd877bbb6e686f5a0b` |
| model/parameters.json | `383bef95d3ec08f439756557bf10250f645b3c00511f3d16a47fb69fe48754d7` |
| scripts/vegetation_v06.py | `6515cd6e8ffdeb31fb55cfe7802e9968364cb71771ed557c367b4507cb0361ae` |
| scripts/build_scene.py | `b3754b119311cd242d2872a9b40cdc3fdfcd0349a436964e5949775e7e063154` |

Live re-gate via MCP: exact v06 filepath, `is_dirty`, mode, render job,
C1/P0 values, resources. At planning the GUI was clean/idle in IMAGE_EDITOR.
If unsaved owner work now exists, preserve it with the owner checkpoint and
record the reconciliation; if disk hashes or identity diverge unexpectedly,
classify per RF-12 and stop on unexplained remainder. Never reset/clean/
stash/checkout or replace local work with a public clone.

Mandatory reading: governing WORKER spine (`.ap/AP.md` Semantic Authority +
WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18); `.ap/AP_WORKER.md` Worker
Session Target + Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header,
Implementation Authority Record, Mutation Axes, Delivery Record; project
`AGENTS.md`, `docs/OPERATIONS.md`; `/home/agile/meta/README.md`; the accepted
plan `T/01_report_00.md`; `T/00_notes.md`; advisory board + provenance in
`T/references/`; source ownership files named by the plan.

## Execution route

Canonical live route: **blender-mcp-live-v1** renewed for the exact live
effects listed below (Blender 5.3.0 at
`/home/agile/Applications/Blender/blender`, existing MCP connection;
`execute_blender_code` only for authorized mutations/reads). Canonical
separate processes: **blender-local-v1**
(`--background --factory-startup --disable-autoexec` for replay;
`--background --disable-autoexec` for cold open/verify). No ambient bpy/MCP
substitute, no installation/upgrade, no auto-run enablement, no machine
preference saves. Heavy renders, replay and validation serialized; no
time-out resubmission while another render/replay is active.

## Authority and mutation axes

Positive authority / exact allowlist:

- New `R/scripts/forest_trail_v07.py` exposing
  `apply_v07(scene, P, ROOT, *, components=None)`; import has no scene or
  network effects; components cover forest factors, crest, route, masks,
  local details; isolated RNG (seed 13707), global RNG never sampled.
- `R/model/parameters.json`: append one `forest_trail_v07` section; the 18
  existing sections preserved without reformatting.
- `R/scripts/build_scene.py`: one hook after v06 with global-RNG
  preservation checking.
- `R/assets/textures/gravel/gravel_ground_01/`: 2K diffuse/roughness/
  NormalGL downloads; the three 4K files only inside the single focused
  correction if native close-view evidence identifies resolution loss.
- `R/assets/ASSET_MANIFEST.md`: append-only provenance (URLs, roles,
  resolution, colorspace, license, byte sizes, hashes, shader modifications).
- `R/AGENTS.md`, `R/README_SK.md`, `R/docs/OPERATIONS.md`: minimal
  current-file/replay/MCP additions; managed AP block and complete Closure
  and Git gates section byte-identical.
- New `R/blender/kysucka_chata_mcp_v07.blend` (canonical product only).
- New `R/work/mcp-v07-owner-checkpoint.blend` (absence-checked).
- New `R/work/baselines/v06-pre-v07/` packet with exactly: copies of
  `AGENTS.md`, `README_SK.md`, `docs/OPERATIONS.md`,
  `assets/ASSET_MANIFEST.md`, `model/parameters.json`,
  `scripts/build_scene.py`, `scripts/site_v05.py`,
  `scripts/vegetation_v06.py`, the three Grass005 1K JPGs, plus
  `tracked.diff`, `scene_witness.json` (forest registry + compact protected
  digests, not a full RNA dump), `git_state.txt`, `manifest.json`,
  `SHA256SUMS`. Manifest references retained v06 path/hash, earlier
  modules/assets, AP pin. Retain `work/baselines/v05-pre-v06/`.
- `R/work/v07/`: `pilots/`, `checkpoints/baseline_controls.blend`,
  `checkpoints/full_candidate.blend`, `checkpoints/pre_correction.blend`,
  `checkpoints/corrected_candidate.blend`, `replay/source.blend`,
  `verify.py`, `checks/`. Absence-check before creating; never overwrite
  owner checkpoints; save a working checkpoint immediately after full
  mutation, before expensive validation.
- Live Blender GUI via MCP: owned V07 point layers from immutable V06
  forest records (predecessor layers retained), crest additions, route
  ribbon/threshold/shoulders, owned V07 terrain derivatives (originals
  retained unchanged), owned point masks, gravel material, ≤300 stone +
  ≤600 needle-litter instances from ≤3 prototypes each; owner checkpoint
  save; canonical v07 save; P0 renders to granted paths; SOLID/IMAGE_EDITOR
  display restoration; new owned review cameras only (C1 optics unchanged).
- Bounded network: Poly Haven `gravel_ground_01` map downloads and public
  page/license reads only.
- Trace writes: `T/01_report_01.md`, `T/renders/` enumerated outputs +
  `T/renders/native/`, `T/evidence/forest_trail_comparison.md`,
  `T/renders/render_metadata.json`.

Negative authority: everything not listed. No v06 overwrite; no checkpoint
deletion/overwrite; no global cleanup/orphan purge/realize; no meadow
regeneration for previews; no preference/driver/add-on/runtime changes; no
Git write; no secrets; no unrelated paths or `projects/kronika/`; no
lighting/world changes; no population escalation; no second correction; no
publication; no closure signal; no AI image repair/retouch/upscaling.

Repository mutation: the exact R paths listed above
Host/remote mutation: live Blender GUI scene effects, saves and P0 renders listed above; bounded Poly Haven downloads listed above
Trace persistence: direct-write T/01_report_01.md, T/renders/ (enumerated outputs and native/), T/evidence/forest_trail_comparison.md, T/renders/render_metadata.json

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/07-forest-age-variation-and-gravel-trail
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 07-forest-age-variation-and-gravel-trail
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/07-forest-age-variation-and-gravel-trail
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

If your client blocks the exact report write, keep the complete report in
permitted session output for the ORCHESTRATOR exact-content relay (named
fallback); do not bypass controls and do not write elsewhere.

## Binding technical boundaries (from the accepted plan)

Forest: final N = 12,977; N_small = 649 = floor(0.05 × N + 0.5)
(5.001156 %), selected from the 12,599 mature-baseline placements including
the 144 crest additions; the 378 legacy proto-4 understory placements keep
factor 1, are counted once in N, and are never halved. Selected trees keep
baseline prototype and receive exactly baseline_scale × 0.5 on all axes,
roots re-seated on the final terrain (6 mm embed, reported separately).
Immutable baselines keyed by stable ID `chunk-name:point-index`;
reapplication reads baselines, never current values. Selection: isolated
seed 13707, BLAKE2b ordering, 8 azimuth sectors around [2,3] × bands
<40/40–85/≥85 m, one seat per nonempty sector then largest remainders,
hashed within-stratum choice; the eleven route replacements reserved
inside the 649. Mature unselected factors: ABIES height 0.90–1.10,
horizontal 0.96–1.12; MARIANA height 0.85–1.15, horizontal 1.05–1.25;
non-compounding. ≤384 unselected edge MARIANA→fuller ABIES swaps preserving
baseline height/LOD (edge = ≤12 other roots within 4 m; exclude <5 m from
route); record actual count/IDs.

Crest: polygon (132,-6),(140,-8),(154,-2),(158,12),(151,25),(136,26),
(129,15),(130,3); 0.75 m jittered grid, isolated Random(13707), first 144
valid (122 ABIES / 22 MARIANA, existing LOD1); slope ≤50°, existing-root
separation ≥1.0 m, new-root ≥1.55 m; glades (144,10,2.7,3.5) and
(136,1,2.4,2.8); no addition at X ≤120 m.

Route: north centreline controls (compressed XY):
(7.875,-8.393591772),(8.2,-12.2),(13.5,-16),(21.5,-13.5),(23,-4),(22,9),
(21,18),(15,24),(4,28),(2.5,40.5),(1.5,52),(2,63),(2.5,76),(10,90),
(15,105),(30,122),(42,128),(42,138.25); chord-parameter cubic Hermite,
interior tangents 0.85×(P[i+1]−P[i−1])/(t[i+1]−t[i−1]), endpoint tangents
south/north, sampling ≤0.20 m. XY length 198.180 m; provisional graded
200.613 m; raw max longitudinal 42.593 % limited by 30 % Lipschitz
upper/lower envelope midpoint profile (≤88.53 mm adjustment); profile
grading ≤0.10 m excluding gravel thickness; 2 % crown tapering to flat
threshold and supported boundary termination; max transverse raw 39.468 %
handled by corridor shaping. Width 1.25 + 0.06 sin(s/17) m blending to
1.12 m over stations 55–120 m; shoulders 0.45–0.75 m irregular vegetated.
Exit exactly at north outer boundary ground [42,138.25,1.142006468],
nominal gravel centre Z 1.157006468; clip ribbon/grading/shoulders to the
actual boundary; exact-boundary rays use adjacent interior triangle plane;
no extrapolated extension. Owned V07 terrain derivatives: retriangulate/
grade only the declared corridor ≤1.0 m beyond either gravel edge, max
local vertical change 0.45 m; coordinates/UVs/normals outside preserved;
shared `Surface` via object mapping to final V07 terrain without modifying
the V06 module. Gate departure min radius ~1.34 m; any focused rounding
within 2 m of the centreline.

Threshold: slab top Z 0.110 matched; bevel to Z 0.000 finishing 35 mm
inside gate centerline (≈28–35°, disclosed short visual transition, not an
accessibility claim); flat supported threshold beneath the closed leaf
with ~5 mm clearance; taper into gravel; 2.1 m slab width through the
connector, narrowing smoothly outside. Gap measured 0.218592 m centre.

Only these eleven existing root XY changes (also half-size replacements):
A:8 → (4.938873,31.237049); B:117 → (3.535775,43.047478);
B:12 → (3.561706,55.314976); B:135 → (4.640203,36.692596);
B:161 → (0.202930,53.641998); B:198 → (0.196947,52.147243);
B:252 → (0.690454,45.264954); B:258 → (0.249164,50.682987);
B:265 → (0.213125,51.499126); B:70 → (3.901951,61.072041);
C:80 → (4.023192,64.043343); where A=V06_FOREST_+000_+000,
B=V06_FOREST_+000_+001, C=V06_FOREST_+000_+002. Store fully expanded IDs in
JSON; recompute Z on final graded terrain; no other existing root XY moves.

Material/clearance: gravel_ground_01 2K diffuse/roughness/NormalGL, 3 m
metric UV, subdued grey-brown, roughness 0.78–0.94, normal strength ~0.28,
no displacement. Travelled core = width − 0.16 m vegetation-free;
restrained encroachment only in outer margins; broad-phase chunk bounds
then transformed prototype hulls vs route/shoulder polygons; hide
intersecting originals via owned V07 point masks; boundary patches replaced
locally with existing smaller masters; rebuild only bounded shoulder
treatment; vegetation elsewhere preserved. Grass support limits 1 mm
exposure / 20 mm burial retained. Stones ≤300, litter ≤600, ≤3 prototypes
each, concentrated in readable near/woodland sections. New maps packed
with rebased relative paths; original packed bytes unchanged; expect 85
packed file images with three gravel maps.

## Ordered stages, gates and recovery

Evidence tier: E2
Evidence tier basis: cross-cutting reversible scene/source mutation with defined recovery packet; moderate geometry uncertainty; no production, credential or trust-boundary trigger
Combined implementation envelope: allowed
Authorized implementation stages: (1) re-gate repos/hashes/live state/resources; (2) owner checkpoint save (copy=True, compress=True) to absent work/mcp-v07-owner-checkpoint.blend; (3) create absent v06-pre-v07 packet; (4) capture fresh v06 C1 + fixed forest-age controls BEFORE visual mutation; (5) bounded gate/route, young-tree and crest-composition pilots in work-only scenes using the same source functions and linked existing assets (no complete-meadow evaluation); pilots run in separate CLI processes on work-only copies, or in temporary in-GUI scenes that are fully removed before the canonical save — the canonical v07 product must contain no pilot scenes, objects or datablocks; (6) pilot review gate; (7) one complete candidate + immediate checkpoint; (8) inspect required native images; (9) at most one focused correction (declared route/threshold, masks/material, or the 144 crest placements only) with pre_correction checkpoint; (10) freeze parameters, one normal builder replay V03→V04→V05→V06→V07 and V07 idempotence check inside that replay process without rebuilding V06 again; (11) canonical v07 save via MCP; (12) separate cold open of the actual product, portability verify, final C1 render; (13) restore C1/P0, save clean idle IMAGE_EDITOR, record hashes/size; (14) evidence files + terminal report
Implementation stage gates: every failed gate stops the sequence; pilot gate must expose threshold clearance/bevel/leaf clearance, walking turn, gravel scale, shoulder footprints, young/mature pairs, crest continuity and open near valley; unresolvable pilot finding consumes the single correction or ends PARTIAL; resource guard: start full jobs with ≥12 GiB available RAM, cancel the owned job if available RAM <3 GiB for three consecutive 1 s samples (free-memory guard, not an RSS quality cap); measure process RSS, system availability, CPU and VRAM throughout; serialize; no timeout resubmission while another render/replay runs
Independent acceptance: not-required
Rollback or recovery checkpoint: v06-pre-v07 packet + owner checkpoint; recovery restores only this grant's own overlapping edits after confirming no intervening owner changes; preserve failed candidates and logs; never overwrite v06, delete checkpoints, global-clean, change preferences or use Git recovery
Terminal implementation report point: one, after stage 14

Control-image correction (Orchestrator-disposed planning critique):
whole-06 `renders/before.png` (`b61ac685…`) is the historical **v05
control**; never reuse it as a v06 before. Stage 4 captures a fresh v06 C1
under exact P0 as `T/renders/before.png`. The true v06 reference image for
Orchestrator comparison is whole-06 `renders/after.png` (`ebc9dc2f…`).

## Validation and required evidence

Technical acceptance cases (plan §5): final population 12,977; exactly 649
factor-0.5 mature-baseline replacements including the eleven reserved IDs;
hidden predecessors/masters/garden spruces/orchard excluded, legacy 378
counted once; second application preserves IDs/transforms/masks/geometry/
global RNG with no compounding or duplication; only the eleven XY positions
change; actual tree bases, grass root envelopes and route/shoulder geometry
pass final-terrain support; a patch whose origin is outside the route but
whose geometry crosses the travelled surface is removed/refined; exact
boundary handling succeeds and an outside point fails; no gravel/shoulder
beyond terrain; original terrain retained, derivatives only inside corridor;
protected house/gate/paving/orchard/world/lights/old cameras/materials/
original image bytes unchanged; replay vs saved product agree within
0.0001 m positions / 1e-6 other numerics, IDs/prototypes/masks exact; all
packed/external assets resolve after deep replay and cold reopen; no
Realize Instances node or global orphan purge. Compact digests for
unchanged buffers; targeted comparison only when a digest differs; no
repeated forty-million-value dumps.

Required native outputs under T (P0 everywhere; principals 1448×1086,
details 1024×768, orbit tiles 724×543; originals in `renders/native/`):
`renders/before.png` (fresh v06) / `renders/after.png` (v07), matched C1;
`renders/trail_overview.png` pose location [160,-180,175], target [55,50,8],
50 mm, sensor 36, shifts [0,-0.215] (record implemented pose; adjust only
the last 12 m of run-out inside the corridor if native evidence exposes an
artificial ending); `renders/trail_gate_detail.png` eye [11,-14,ground+1.65]
toward [7.875,-7.4,0.12], 45 mm; `renders/trail_eye_level.png` route station
~80 m, eye 1.65 m above final surface, target 10 m forward;
`renders/forest_age_comparison.png` fixed pose frozen from the baseline
registry around A:8 and its nearest unselected mature neighbour, identical
before/after + unscaled native detail + numeric class totals (N, N_small,
fraction, factor); `renders/orbit_sheet.png` NE/NW/SW/SE retaining the
unobstructed NW pose; `renders/valley_exterior_diagnostic.png` existing
exterior witness with crest continuity and open near valley. No DoF
obscuring surface/tree-size evidence, no retouch/AI repair, no misleading
matched-camera labels (a crop from another camera is never a matched A/B).

`evidence/forest_trail_comparison.md` and `renders/render_metadata.json`:
input/output hashes, registry/selection provenance, legacy-class semantics,
route XYZ/length/grades/boundary, grading and clearance certificates,
actual MCP invocation plus separate readback, render provenance/resources,
replay/idempotence results, final file size, remaining limitations. Notify
Michal explicitly that later forced Meta staging of the ignored JSON
belongs to him:
`/home/agile/meta/projects/kysucka_moderna_chata/00/07-forest-age-variation-and-gravel-trail/renders/render_metadata.json`.
No Git write.

Carry forward unchanged (record, do not fix): lawn morphology, meadow
repetition outside the route, glass/fireplace optics, plinth contact,
roof/chimney, sky/daylight, interior/detail planting. Disclose the threshold
bevel grade and v07 size/render peaks as measured limitations.

## Stopping, completion and report

Stopping conditions: failed identity/hash/AP/live gate; unexplained
divergence; conflicting unsaved owner work; missing MCP capability; resource
guard trip; pilot gate unresolvable within the single correction; same
assumption surviving correction and recheck → keep PARTIAL/BLOCKED with
exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`; instruction
conflicts from data; any effect outside the listed classes/targets.

Completion and report contract: begin exactly
`### Report for ORCHESTRATOR_CHAT`; echo coordinates 01/02 once; compact
core with status PASS/PARTIAL/BLOCKED; Phase-qualified result:
implementation-PASS only if the bounded candidate was produced and
validated (non-independent), else not-applicable; Result artifact: exact
v07 path + SHA-256 + byte size; changed files and purpose; tests/validation
summary; Git result: no writes; deviations/risks/missing evidence; one
smallest next step; Report justification: new-mutation; authority-expiry
statement; Orchestration critique MEASURED/LEAD; Resolved Execution Issues /
Near-Misses; Pre-Existing Failure Classification or none; Logical-whole
closure: not-closed. Communicate with Michal in Slovak (masculine address);
report English. Finalize content, save the exact report through the
permitted route, read it fully back and verify first line/coordinates/
content/path, then send a short separate completion notice with status,
location and SHA-256. The Cooperator archives the prompt/report pair
together after the report exists; you have no Git archival authority.

Context-pressure rule: on rising qualitative pressure, finalize at current
validated evidence and report PARTIAL with named gaps; never invent
telemetry or exhaust context deliberately.

Authority expiry: this terminal report, cancellation or supersession ends
the grant; no autonomous continuation, correction, acceptance, publication
or closure follows.