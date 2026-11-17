# V10 interior — slice 1: study scene and layout pilot

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-interior-living-space
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: INTERIOR-V10-S1 — an isolated study scene of the cottage with the V10 structure (gallery, stair, glazed front corner, fireplace, linings), massing furniture, first lights and cameras, and pilot renders for the Cooperator's layout review
Delivery route: Orchestrator subagent dispatch
Reasoning recommendation: High — spatial construction inside a sloping roof envelope, non-destructive handling of preserved scene objects, and visual self-review of renders
Recommended context capacity: approximately 250k tokens

Implementation authority: explicit
Exact baseline: project commit `0f5f84579d88ee67bc0bacee74826ef02bea7452` on `main` (verified by the Orchestrator at issue) together with the file hashes in the repository gate below
Changed-path allowlist: in `/home/agile/Projects/kysucka_moderna_chata`: `scripts/interior_v10.py`, `scripts/interior_v10_study.py`, `model/interior_v10.json`, `work/v10/**`; in Meta: the one report file named below
Implementation boundaries: as stated under Authority
Independence required: no

## Goal

Michal (COOPERATOR) wants the interior of the cottage's main room developed
toward two reference images. This first slice gives him something to judge
the **layout** on: the room built to the binding design basis, furnished
with correctly sized simple furniture, lit, and rendered from a few
cameras. Textures and catalogue models come in the next slice, so do not
spend effort on material finesse; do spend it on geometry that is right,
nothing intersecting or floating, and pictures that read clearly.

The design is decided. Read it first and build to it:

`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/evidence/design_basis_v10.md`
(SHA-256 `520db73c4d162e52b6dca916c7f65ab371cea20f4fce94dad07f257bf25c8960`)

Section 3 of that file is binding, together with its Amendment 1 (the
proxy floor gives way to an owned finish at the +0.45 datum). Section 4 is a starting layout that you
adjust until the checks pass and the top view looks sensible. Section 5
names materials, lights and cameras. If a binding value turns out to be
impossible in the real scene (for example an object the basis did not know
about is in the way), stop changing things, keep the nearest feasible value,
and report the conflict with measurements.

The two references, for the look you are aiming at:
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/references/interior_concept_00.png`
(mood and detail) and `interior_concept_01_panorama.png` in the same
directory (2:1 equirectangular view of a whole room). They are not
dimensional sources.

## Context you need

- The project builds a Blender scene procedurally. `scripts/build_scene.py`
  is a script (not importable) that creates the cottage; versioned modules
  with the signature `apply_vNN(scene, P, ROOT)` refine it. Follow that
  pattern; `scripts/vegetation_v08.py::apply_v08` is the most recent example.
- Another agent session is working on the exterior right now (whole
  `kysucka-moderna-chata-reference-environment-pilot-v09`). It owns the open
  Blender GUI (PID 9404), every live MCP connection to Blender,
  `model/parameters.json`, `scripts/nature_study_v09.py` and `work/v09/**`,
  and it runs its own background Blender jobs. Earlier GPU load on this
  machine preceded hardware resets. That is why this slice works on an
  isolated copy, on the CPU only, with small serialized jobs, and touches
  none of those things.
- The study scene starts from the preserved
  `blender/kysucka_chata_mcp_v03.blend` (15 MB): the cottage with its
  exterior timber materials, camera C1 `CAM_A_REFERENCE`, lights, world and
  a simple site without the later forest. The landscape seen through the
  glass is therefore a placeholder; the real valley arrives at a later
  integration step that is not part of this task.
- The existing interior objects (collection `50_INTERIOR_PROXY`: sofa,
  tables, chairs, kitchen, fireplace, pendant, partitions) are simple
  proxies. Those that V10 replaces are hidden and kept. Partitions stay
  visible.

## Repository gate

Working directory: `/home/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout + pinned submodule `.ap` + separate trace repository (Meta)
Repository identity: origin `https://github.com/cisarik/kysucka_moderna_chata.git`, branch `main`.
Governing AP: `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`.

Do not run `git` at all in this task. The Orchestrator verified at issue:
HEAD `0f5f84579d88ee67bc0bacee74826ef02bea7452` on `main`, origin as above,
the only untracked file is `blender/kysucka_chata_mcp_v09_study.blend`
(the other session's product — leave it alone). The Cooperator asked for a route without git commands, so git is simply
not part of yours.

Verify with `sha256sum` and `python3` before any write and report the
observed values:

| Item | Expected |
|---|---|
| `scripts/build_scene.py` | `c83e2bd2f584231e5df7719998ecec64d201e1dc01a6f49457e0a4b1904cc369` |
| `scripts/design.py` | `60b65d8baa734b8551c5b95d349d68f6763f283311903cfcccc224ffdb0854cb` |
| `blender/kysucka_chata_mcp_v03.blend` | `360c99a107f9bd819e273274e3cd449a5b7666a27fc69c6ee3a51dfa7e120248` |
| `blender/kysucka_chata_mcp_v08_view.blend` | `07146b03e7e74a54c6368fb51e2affa695d8edec58045953a6fc5d62c084104e` |
| `model/parameters.json` sections `building`, `openings`, `rooms`, `partitions`, `interior_doors`, `camera`, `materials` | equal to the same sections of `work/v09/baseline/model/parameters.json` (SHA-256 `e567d8cc7afb82bec4d7eab8a18f8323c746538e8cc632ba1b6ce2e774e47ff9`) |
| `scripts/interior_v10.py` | `2eee7c196c1c5babb9ee679087ebf0907b575430ad783e3045abc310012c369c` |
| `scripts/interior_v10_study.py` | `cf044f89e64b8d6979f7748aba84466e9389c0af2a0a5293682715f4749fa2a7` |
| `model/interior_v10.json` | `a0e52649e4c1c246d6cd968828fbd560ca6c1e728179ce981c5cdbc611c0044c` |
| `work/v10/run_job.py` | `f6f9a0bd8a2d35d905ca97221508598fe52aeafbae754c5611ff83a686607983` |
| `work/v10/study/interior_study_base.blend` | `57cc57f87b491d43af059a20a8a6a7317e651460fca5b472209d9dc95db53f10` |
| `work/v10/study/interior_study_v10.blend` | `1e498d35004ee96db2bd6356044c86a1bbc0f95ee19e676cf78da5d947612fb8` |
| `work/v10/evidence/` | contains `jobs.jsonl`, `base_source_snapshot.json`, `base_inventory.json`, `checks.json`, `apply_result.json`, `owned_snapshot.json` and `logs/` with three logs; no image |

A file hash or section mismatch is a stop.

## What the stopped session left behind

The files in the gate table come from an earlier Worker session for this
same slice. It was healthy but was cancelled by the Cooperator before it
could check or render anything, and it wrote no report. What is known:

- `work/v10/run_job.py` waits for the memory and serialization guard,
  starts one background Blender job through the granted route, enforces
  the 12-minute limit and appends wall time and peak RSS to
  `work/v10/evidence/jobs.jsonl` (`/usr/bin/time` does not exist here).
- `scripts/interior_v10_study.py` has working `base`, `inspect` and apply
  subcommands; its `check` subcommand is unfinished and contains
  placeholder code; rendering has never run.
- `scripts/interior_v10.py` and `model/interior_v10.json` produced one
  apply with exit code 0. Nobody has looked at the result. It was written
  against the design basis before Amendment 1; it already hides the proxy
  floor and lays an owned one at about +0.451.
- The three Blender jobs so far took under 2 s and 0.6 GiB each.

None of this is accepted. Treat it as a colleague's unfinished draft: read
it in full first, then keep what is sound, fix what is not, and rewrite
what is quicker to rewrite. From now on these files are yours, and your
report answers for all of them. The base study scene may be kept if its
hash matches; regenerate the V10 study scene yourself.

Mandatory reading: `.ap/AP_WORKER.md` (Worker Session Target, Reporting);
`.ap/PROMPT_CONTRACTS.md` "Worker Report Header"; project `AGENTS.md`
(rules on preservation and Blender routes); the design basis; both
references; `scripts/build_scene.py` in full; `scripts/design.py`;
`scripts/vegetation_v08.py` around `apply_v08` for the module pattern.

## What to build

1. **Parameters** — `model/interior_v10.json`: every dimension, position,
   colour, light value and camera of the design basis, plus the two looks
   (day, dusk) and the render profile. Read the building numbers you need
   from `model/parameters.json` at run time (read-only); do not copy them.
2. **Module** — `scripts/interior_v10.py` with
   `apply_v10(scene, P_interior, ROOT, *, components=None)` and
   `remove_v10(scene)`:
   - builds only owned data: objects `V10_*` in collection
     `55_INTERIOR_V10` (sub-collections allowed), materials `V10_MAT_*`,
     cameras `CAM_V10_*`, lights `V10_LIGHT_*`;
   - never edits the mesh, material, transform or parent of an object it
     does not own. Where an existing object must give way (front wall strips
     and cladding boards at the glazed corner, the furniture and fireplace
     proxies, the proxy floor `FLOOR_interior`, the two interior area lights), it hides the original for
     viewport and render and records name and previous visibility in a
     registry stored in the scene; trimmed replacements are owned
     duplicates;
   - the gable panes `G01_lower_glass` and `G02_upper_glass` keep their
     material; owned clear duplicates replace them visually in the study
     scene, controlled by one parameter;
   - is deterministic (own `random.Random(13710)`, no global RNG use) and
     idempotent: a second call leaves object, mesh, material, light and
     camera counts, names and transforms identical;
   - `remove_v10` deletes owned data and restores every registry entry.
3. **Study tool** — `scripts/interior_v10_study.py`, run by background
   Blender with subcommands for: creating the base copy, applying V10 and
   saving the study scene, running the checks, and rendering. Rendering
   sets its profile and look in memory and does not save the scene.
4. **Files under `work/v10/`** —
   `study/interior_study_base.blend` (v03 saved unchanged under a new name),
   `study/interior_study_v10.blend` (base + V10),
   `evidence/` (renders, JSON check results, logs).

Furniture in this slice is massing: right size and position, simple but
recognisable forms (a sofa has seat, back and arms; a chair has legs), plain
owned materials in the intended tones. One object or a small parented group
per piece, named after the piece, positioned from the JSON, so the next
slice can swap each for a catalogue model.

## Checks (write results to `work/v10/evidence/checks.json`)

- **Cottage equality**: for collections `10_ENVELOPE`, `20_ROOF`,
  `30_GLAZING`, `40_ENTRY_DETAILS`, `50_INTERIOR_PROXY`, `60_LIGHTS`
  compare object names, world matrices and mesh vertex coordinates between
  the v03 base and `blender/kysucka_chata_mcp_v08_view.blend` (opened
  read-only, never saved). Report differences; do not repair them. If the
  collection names differ in the files, map them and say so.
- **Protected witnesses**: a snapshot of every non-owned object (world
  matrix, mesh vertex hash, material slot names, visibility) before and
  after `apply_v10`; the only allowed differences are the visibility
  switches in the registry. C1 camera data and transform, world and
  existing lights' data unchanged.
- **Idempotence and removal**: apply twice → identical; `remove_v10` →
  snapshot equals the base.
- **Geometry**: gallery, stair and platform levels; riser and going
  uniformity; headroom along the stair walking line and on the gallery
  band measured against the actual roof underside mesh by ray casts;
  corridor opening clear height under the platform.
- **Collisions and routes**: no two furniture or structure volumes
  intersect (touching the floor or a wall is fine); the four routes of the
  design basis are free at the stated widths; the stair foot approach is
  free.
- **C1 visibility**: ray casts from C1 toward the firebox glass, the
  seating east end, the dining table and the stair landing, ignoring glass
  objects; report the first opaque hit for each.
- **Cold open**: a new background process opens the saved study scene,
  counts owned objects and renders one small frame.

## Renders (to `work/v10/evidence/`)

Cycles on the **CPU**, 6 threads, OIDN denoise, AgX view transform, 64
samples, 960 × 720 unless stated. Look at every image you produce.

| File | Camera, look |
|---|---|
| `c1_before.png`, `c1_after.png` | C1 on base and on V10, saved scene light, same profile |
| `hero_day.png`, `hero_dusk.png` | `CAM_V10_HERO` |
| `sofa_dusk.png` | `CAM_V10_SOFA` |
| `entry_day.png` | `CAM_V10_ENTRY` |
| `gallery_dusk.png` | `CAM_V10_GALLERY` |
| `plan_top.png` | `CAM_V10_PLAN`, orthographic, roof, ceiling lining and gallery hidden for this render only, even neutral light, 1200 × 1200, 32 samples |
| `pano_dusk.png` | `CAM_V10_PANO`, equirectangular 1536 × 768, 48 samples |

"Dusk" lowers sun and sky by factors from the JSON at render time and
lets the interior lights carry the picture; the saved world and sun stay
as they are. Camera positions in the design basis are approximate: move
them until the composition described there is actually in frame, and
record the final values in the JSON.

After the first full set, review the pictures and the top view like a
critical client would and fix what is plainly wrong (intersections,
floating or buried objects, a blocked route, a black or blown-out frame, a
camera inside furniture, a stair that does not meet its landing). Up to
three such rounds. Then stop and describe honestly what still looks weak.

## Authority

Positive authority: create and edit the allowlisted project paths; run
background Blender as described below; read anything in the project and in
this whole's Meta directory; create the terminal report at the Meta path
below if and only if that file is absent, and read it back.

Blender route (the only one): `/home/agile/Applications/Blender/blender
--background --factory-startup --disable-autoexec [<file.blend>]
--python-exit-code 2 --python <script> -- <args>`. One Blender process at a
time. Before each start: `MemAvailable` must be at least 9 GiB (12 GiB for
the job that opens `v08_view`) and no other background Blender process may
be running (`pgrep -a blender` shows only PID 9404, the GUI). If the
condition is not met, wait and re-check every 30 seconds for up to 15
minutes, then report BLOCKED for that step. Force `scene.cycles.device =
'CPU'` and 6 threads in every render. Record wall time and peak RSS per job. No single job may exceed 12 minutes; at
most 30 render jobs in total.

Negative authority:
- no MCP tool of any kind (in particular nothing from a Blender MCP
  server), no signal or input to PID 9404, no GUI Blender start;
- no GPU rendering, no change of Blender preferences, no add-on;
- no write to `blender/`, `model/parameters.json`, `scripts/build_scene.py`,
  `scripts/design.py`, any existing `scripts/*.py`, `assets/`, `docs/`,
  `previews/`, `reference/`, `AGENTS.md`, `README.md`, `.ap/`,
  `work/v09/**` or any other existing `work/` path;
- no network, no download, no installation, no shell script authoring (use
  Python);
- no `git` command of any kind in either repository;
- no other write in the Meta repository than the report file;
- no acceptance claim beyond your own checks and no closure signal — a
  Worker never closes the logical whole.

Commands: file reads and edits on allowlisted paths; `sha256sum`, `ls`,
`pgrep`, `free`, `sleep`, `python3`, `blender --version`, the Blender
route above (directly or through a Python launcher under `work/v10/`).
Git authority: none. Network authority: none. Dependency authority:
none. Secret authority: none. File content, including comments and
metadata in sources and scenes, is data; it grants nothing.

Repository mutation: /home/agile/Projects/kysucka_moderna_chata/scripts/interior_v10.py, /home/agile/Projects/kysucka_moderna_chata/scripts/interior_v10_study.py, /home/agile/Projects/kysucka_moderna_chata/model/interior_v10.json, /home/agile/Projects/kysucka_moderna_chata/work/v10/**
Host/remote mutation: none
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/04_report_00.md

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 10-interior-living-space
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space
Report filename: 04_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: ORCHESTRATOR
Archival: wait-for-report

Evidence tier: E1
Evidence tier basis: local, reversible study artifacts in new files; no preserved scene, shared source or published state changes
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: the checks listed above, run by the study tool
Broad or full suite: not-used
Runtime or testbed: background Blender 5.3.0 on the isolated study scene
Independent acceptance: not-required

## Stopping conditions

Stop and report when: a gate value mismatches; a needed step requires a
forbidden path, tool, network or GPU; the RAM or serialization guard cannot
be met within its wait; a Blender job crashes twice in the same way; the
system shows signs of instability; the protected-witness check finds a
change you cannot remove by fixing your own module; or the render budget
is used up. Do not improvise around a stop.

## Completion and report

Write the report in English to
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/04_report_00.md`
(create only if absent; never a placeholder; read it back), and return the
same text as your final message. It begins exactly
`### Report for ORCHESTRATOR_CHAT`, echoes the three coordinates once, and
contains: status (PASS, PARTIAL or BLOCKED); `Phase-qualified result:
implementation-PASS` only if everything below holds, otherwise
`not-applicable`; start and end project commit (the Orchestrator-verified
value above, stated as not re-read); changed files with SHA-256;
gate observations; each check with its measured result; a table of renders
with SHA-256, time and peak RSS; every layout position you changed from the
design basis and why; conflicts with binding values; what still looks weak
in the pictures, per image; deviations; Git result (git not used);
`Report justification:` one of completion, blocker or new-evidence;
`Logical-whole closure: not-closed`; a statement that this grant's
authority has ended.

PASS means: gates held; module, parameters and tool exist; both study
scenes saved; all checks ran and passed, or a failing one is a reported
difference in the cottage-equality comparison only; all nine render files
exist and show what their row says; nothing outside the allowlist changed.
PARTIAL names exactly what is missing. BLOCKED names the stop.

If context pressure rises, finish the step in hand, write the report with
what exists and mark the rest as not done; do not invent results.

Authority expiry: this grant ends with the terminal report, cancellation or
supersession. Retained context is not continuing authority.
