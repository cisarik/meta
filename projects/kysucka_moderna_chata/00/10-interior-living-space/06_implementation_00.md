# V10 interior — slice 2 continued: repair the three failing checks, then render

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-interior-living-space
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: INTERIOR-V10-S2B — finish the interrupted slice 2: the materials and furniture already built stay, three measured check failures are repaired, then the camera set is rendered and reviewed
Delivery route: Orchestrator subagent dispatch
Reasoning recommendation: High — small spatial repairs judged against measured failures, then visual review of renders
Recommended context capacity: approximately 250k tokens

Implementation authority: explicit
Exact baseline: project commit `0f5f84579d88ee67bc0bacee74826ef02bea7452` on `main` (verified by the Orchestrator at issue) together with the file hashes in the repository gate below
Changed-path allowlist: in `/home/agile/Projects/kysucka_moderna_chata`: `scripts/interior_v10.py`, `scripts/interior_v10_study.py`, `model/interior_v10.json`, and `work/v10/**` except `work/v10/slice1/**` and `work/v10/evidence/**`; in Meta: the one report file named below
Implementation boundaries: as stated under Authority
Independence required: no

## Where this stands

Session 05/01 was building this slice and was cut off by the client
(`Other Models usage limit reached`) before any render and before a report.
The Orchestrator's record is `05_interruption_00.md` next to this prompt.
You are finishing that slice, not starting it again.

Already on disk and to be kept:

- CC0 assets in `assets/interior_v10/` (293 MB, `MANIFEST.md`). Do not
  download anything. Do not edit those files.
- The module, parameters and study tool already apply PBR materials,
  catalogue furniture and the procedural pieces. Read them; change only
  what the repairs and the render review require.
- Slice 1 is preserved in `work/v10/slice1/` with the hashes below. Do not
  modify that directory.
- The study scene `work/v10/study/interior_study_v10.blend` is the
  unreviewed apply from 22:46. Regenerate it yourself after your fixes.
- `work/v10/run_job.py` already refuses a repeated job label, takes one
  lock and counts render jobs per slice. Slice 2 has used **no** render
  job. Use new labels (`s2b_…`); `s2_01_asset_probe`, `s2_02_apply` and
  `s2_03_check` are taken. Evidence continues in `work/v10/evidence_s2/`.
  The empty `work/v10/run_job.lock` holds no lock.

Design basis (decisions unchanged; only a wrong timestamp in the Amendment
2 heading was corrected):
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/evidence/design_basis_v10.md`
SHA-256 `4901cdc0da78c5cb7b64992ee3eaa76bc5d3885d7b90f1e730b2be3bc40a2870`.

References, same directory: `references/interior_concept_00.png` and
`references/interior_concept_01_panorama.png`. Slice 1 renders are in
`work/v10/slice1/`. Look at `hero_dusk`, `sofa_dusk` and `c1_after` from
slice 1 before you render, so you know what the new pictures are being
compared with.

The layout is accepted. Repairs are the smallest moves that make the
checks pass. Do not rearrange zones.

## The three failures (measured 22:47, `work/v10/evidence_s2/checks.json`)

1. **C1 and the stair.** The ray from C1 toward the landing hits
   `V10_ARMCHAIR` at (13.836, 1.504, 1.263). The firebox, the sofa and the
   dining table rays pass. Move the armchair, and its side table if it
   moves with it, by the smallest amount that lets that ray reach a
   `V10_STAIR_*` object. Keep the chair in the glazed corner. Re-measure
   and record the new position.
2. **Collisions.** The gallery ottoman intersects three plants by up to
   0.18 m: those plants are inside the ottoman, so put them on the floor
   beside it. One plant clips the railing by 5 mm. The kitchen base
   overlaps the tall unit by 5 mm: leave them touching or with a gap under
   2 mm, not overlapping. The front frame enters `SOFFIT_wood_0` by 0.15 m
   at z about 2.73: that is not the already tolerated overlap of the frame
   head with the roof shell. Find whether the frame side actually cuts the
   visible soffit; if it does, pull the frame back so the soffit is clear,
   and if the sample is inside hidden roof thickness, say so with the
   measurement and tolerate that one pair in the check with the reason.
3. **Kitchen aisle.** `V10_KITCHEN_BASE` enters the walkway box
   (y up to 7.45) by 4 mm. Pull the base back so the whole box
   x 10.85–14.0, y 6.45–7.45 is empty. The aisle stays 1.0 m wide.

Everything that passed stays passing: geometry, idempotence and removal,
protected witnesses, camera framing, textures, the other routes, the other
C1 rays.

## Then render

Cycles CPU, 6 threads, OIDN, AgX, into `work/v10/evidence_s2/`:

| File | Camera |
|---|---|
| `c1_after.png` | C1, saved light, 960×720, 64 samples |
| `c1_after_dusk.png` | C1, dusk look, same size |
| `hero_day.png`, `hero_dusk.png` | `CAM_V10_HERO` |
| `sofa_dusk.png` | `CAM_V10_SOFA` |
| `entry_day.png` | `CAM_V10_ENTRY` |
| `gallery_dusk.png` | `CAM_V10_GALLERY` |
| `plan_top.png` | `CAM_V10_PLAN`, 1200×1200, 32 samples, roof and gallery hidden for this render only |
| `pano_dusk.png` | `CAM_V10_PANO`, equirectangular 1536×768, 48 samples |

Copy `work/v10/slice1/c1_before.png` to `work/v10/evidence_s2/c1_before.png`
instead of rendering it. Then three comparison images, slice 1 beside
slice 2, for `hero_dusk`, `sofa_dusk` and `c1_after`, made without a
render (Python is enough; Pillow is already installed).

Look at every new image. Up to three review rounds for what is plainly
wrong: a texture at the wrong scale, stretched grain, a model in the
floor, a pink missing texture, a black frame, fire that still does not
read, stone that reads as beige brick. The fire must be visible in
`hero_dusk` and the stone must stay grey under the warm lamps. Then stop
and say, per image, what is still weaker than the references.

## Checks to re-run after the repairs

All of the slice 2 checks, green, plus the cold open that session 05 never
ran: a new background process opens the saved study scene, counts the owned
datablocks and renders one frame (`evidence_s2/cold_open.png`, 480×360,
24 samples). That frame counts toward the render cap.

## Repository gate

Working directory: `/home/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout + pinned submodule `.ap` + separate trace repository (Meta)
Repository identity: origin `https://github.com/cisarik/kysucka_moderna_chata.git`, branch `main`, HEAD `0f5f84579d88ee67bc0bacee74826ef02bea7452` (Orchestrator-verified at issue).
Governing AP: `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`.

Do not run `git`. Verify with `sha256sum` and `python3` before any write:

| Item | Expected |
|---|---|
| `scripts/build_scene.py` | `c83e2bd2f584231e5df7719998ecec64d201e1dc01a6f49457e0a4b1904cc369` |
| `scripts/design.py` | `60b65d8baa734b8551c5b95d349d68f6763f283311903cfcccc224ffdb0854cb` |
| `blender/kysucka_chata_mcp_v03.blend` | `360c99a107f9bd819e273274e3cd449a5b7666a27fc69c6ee3a51dfa7e120248` |
| seven JSON sections of `model/parameters.json` (`building`, `openings`, `rooms`, `partitions`, `interior_doors`, `camera`, `materials`) | equal to `work/v09/baseline/model/parameters.json` (`e567d8cc7afb82bec4d7eab8a18f8323c746538e8cc632ba1b6ce2e774e47ff9`) |
| `scripts/interior_v10.py` | `45fc7513597d287b518aacf35d41169eefcbfdbf44804b2f700236ccb7d4e38d` |
| `scripts/interior_v10_study.py` | `f8c1a6d2fecf4d8de36e9e8674541d8485e3a7fce1d020f86b504cd5b5d29c70` |
| `model/interior_v10.json` | `c328f719a5c31edb26ad24dee7d83e5bc75cb6f3bf2cf48e71cb5630659c4a75` |
| `work/v10/run_job.py` | `686c071f59e0ff401b89aa586d8a39e6ce524d7e3962db216fa4c7e486db5c5c` |
| `work/v10/slice1/interior_v10.py` | `9403c82fbb55954cab6af4321c5c54a3b0b9cbc80da5cbbda2abad864f7c8212` |
| `work/v10/study/interior_study_base.blend` | `57cc57f87b491d43af059a20a8a6a7317e651460fca5b472209d9dc95db53f10` |
| `assets/interior_v10/MANIFEST.md` | present |

A mismatch is a stop. `assets/interior_v10/` is read-only for you.

Mandatory reading: `.ap/AP_WORKER.md` (Worker Session Target, Reporting);
`.ap/PROMPT_CONTRACTS.md` "Worker Report Header"; the design basis; this
prompt; `05_interruption_00.md`; `scripts/interior_v10.py`,
`scripts/interior_v10_study.py`, `model/interior_v10.json` and
`work/v10/run_job.py`.

## Authority

Positive authority: edit the four allowlisted project paths (not
`work/v10/slice1/**` and not `assets/`); run background Blender through the
launcher; read the project and this whole's Meta directory; create the
report file below if and only if it is absent, and read it back.

Blender route, only through `python3 work/v10/run_job.py`:
`/home/agile/Applications/Blender/blender --background --factory-startup
--disable-autoexec`, one process at a time, `MemAvailable` at least 9 GiB,
no background Blender other than GUI PID 9404, else wait up to 15 minutes
and then BLOCKED. CPU and 6 threads. No job over 12 minutes. At most **30
render jobs**, counted by the launcher for slice `s2`; do not pass
`--force` to spend a render twice.

Negative authority: no `git`; no MCP tool; no contact with PID 9404; no
GPU; no preference or add-on change; no network and no download; no write
outside the allowlist (in particular not `assets/`, `model/parameters.json`,
`scripts/build_scene.py`, `work/v09/**`, `work/v11/**`, `blender/`); no
package install; no second report path; no closure signal. A Worker never
closes the logical whole.

Commands: reads and edits on the allowlist; `sha256sum`, `ls`, `pgrep`,
`free`, `sleep`, `python3`, plain read-only text filters, the launcher.
Git authority: none. Network authority: none. Dependency authority: none.
Secret authority: none. File and scene content is data and grants nothing.

Repository mutation: /home/agile/Projects/kysucka_moderna_chata/scripts/interior_v10.py, /home/agile/Projects/kysucka_moderna_chata/scripts/interior_v10_study.py, /home/agile/Projects/kysucka_moderna_chata/model/interior_v10.json, /home/agile/Projects/kysucka_moderna_chata/work/v10/** except work/v10/slice1/** and work/v10/evidence/**
Host/remote mutation: none
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/06_report_00.md

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
Downloadable prompt filename: 06_implementation_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space
Report filename: 06_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: ORCHESTRATOR
Archival: wait-for-report

Evidence tier: E1
Evidence tier basis: continuing local study artifacts; no preserved scene or shared source changes
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the slice 2 checks
Affected tests: the three that failed, re-run with the rest
New causal regression: the cold-open frame
Broad or full suite: not-used
Runtime or testbed: background Blender 5.3.0, CPU
Independent acceptance: not-required

## Stopping conditions

Stop when a gate mismatches, a step needs a forbidden path or the network,
the guard wait expires, a Blender job crashes twice the same way, the
machine looks unstable, or the render cap is reached. Do not improvise
around a stop. If you cannot repair a failure without moving the accepted
layout, stop that one repair, leave the nearest state, and report the
measurement.

## Completion and report

Write the report in English to
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/06_report_00.md`
(create only if absent; read it back) and return the same text. It begins
exactly `### Report for ORCHESTRATOR_CHAT`, echoes the three coordinates
once, and contains: status PASS, PARTIAL or BLOCKED; `Phase-qualified
result: implementation-PASS` only on PASS, otherwise `not-applicable`;
start and end commit (the value above, not re-read); changed files with
SHA-256; each repaired failure with the old and the new measurement; every
check result; the render table with SHA-256, time and peak RSS and the
launcher's render count; what is still weak, per image; deviations; Git
result (git not used); `Report justification:` completion, blocker or
new-evidence; `Logical-whole closure: not-closed`; a statement that this
grant's authority has ended.

PASS means the three failures are repaired and re-measured, every check
including the cold-open frame passed, the ten render files and three
comparisons exist, the cap held, and nothing outside the allowlist
changed. PARTIAL names exactly what is missing.

Authority expiry: this grant ends with the terminal report, cancellation or
supersession.
