# V10 interior — slice 4: cushion seams at hero distance, throw in frame

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-interior-living-space
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: INTERIOR-V10-S4 — make the sofa cushions read as separate pieces from the hero camera, and put the chaise throw where that camera sees it
Delivery route: Orchestrator subagent dispatch
Reasoning recommendation: High — one visual gap, judged on the rendered frame rather than on the mesh box
Recommended context capacity: approximately 180k tokens

Implementation authority: explicit
Exact baseline: project commit `0f5f84579d88ee67bc0bacee74826ef02bea7452` on `main` (verified by the Orchestrator at issue) together with the file hashes in the repository gate below
Changed-path allowlist: in `/home/agile/Projects/kysucka_moderna_chata`: `scripts/interior_v10.py`, `model/interior_v10.json`, `work/v10/run_job.py`, and `work/v10/**` except `work/v10/slice1/**`, `work/v10/slice2/**`, `work/v10/slice3/**`, `work/v10/evidence/**`, `work/v10/evidence_s2/**` and `work/v10/evidence_s3/**`; in Meta: the one report file named below
Implementation boundaries: as stated under Authority
Independence required: no

## What this slice is

Slice 3 passed its checks and replaced the black chair. Michal looked at
`hero_dusk` and asked for one more narrow pass. Amendment 4 of
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/evidence/design_basis_v10.md`
is the decision. Its SHA-256 is in the gate.

The picture to beat is `work/v10/evidence_s3/hero_dusk.png`. In it the sofa
is one smooth light block. The throw is on the chaise and is not in that
frame. Look at that image, and at `references/interior_concept_00.png` in
the same Meta directory, before you edit.

## What to change

**Cushions.** Keep the sofa plan exactly: x 9.25–12.10, y 0.40–1.35, chaise
to y 2.30, origin [10.675, 0.875]. From `CAM_V10_HERO` the seat cushions
and the back cushions must read as separate pieces. The 70 mm gaps of
slice 3 disappear at that distance. Deepen the recess between cushions,
thicken the pillows, and give the gap a dark edge so it survives a
960×720 frame. Stay on the warm `rough_linen` already chosen. Do not put
`wool_boucle` back on the large faces: that map is a houndstooth and it
fused the cushions. Do not move the coffee table, rug, lamp or chair.

**Throw.** Keep it a knitted drape on the chaise, hem above the floor.
Move or extend it so it is visible in `hero_dusk` without moving the
camera. Do not drag it across the main seat just to enter the other
camera. `CAM_V10_SOFA` sits on the sofa looking at the fire; if the chaise
is behind that camera, say so and do not force the throw into
`sofa_dusk`.

The corner chair, gallery chair, dining chairs, kitchen, fireplace,
cameras, lights and landscape stay. Shared materials stay.

## Before any edit

Copy `scripts/interior_v10.py`, `model/interior_v10.json`,
`work/v10/run_job.py`, `work/v10/study/interior_study_v10.blend`,
`work/v10/evidence_s3/hero_dusk.png` and `sofa_dusk.png` into
`work/v10/slice3/`. Verify them against the gate hashes, then do not write
there again. Slice 4 evidence goes to `work/v10/evidence_s4/`. Add slice
`s4` to the launcher with render cap **8**. Do not change the s2 or s3
caps. `scripts/interior_v10_study.py` already writes evidence from a slice
argument or a constant: if it is hardcoded to `evidence_s3`, the smallest
change that sends this slice to `evidence_s4` is allowed and that file
joins the allowlist for that edit only. Do not rewrite the tool.

## Checks and renders

Regenerate the study scene. Re-run the existing check set into
`evidence_s4`; every section stays true, including the C1 stair ray,
collisions, routes and the sofa plan. Cold-open the saved scene with
`evidence_s4/cold_open.png`, 480×360, 24 samples.

Render Cycles CPU, 6 threads, OIDN, AgX, 960×720, 64 samples:
`hero_dusk.png`, `sofa_dusk.png`. Then Pillow comparisons, slice 3 on the
left and slice 4 on the right: `compare_hero_dusk.png`,
`compare_sofa_dusk.png`. Look at `hero_dusk`. One review round is allowed
only if the cushions still fuse or the throw is still out of that frame.
The cap is 8 and the cold-open frame counts. New labels start with `s4_`.

## Repository gate

Working directory: `/home/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout + pinned submodule `.ap` + separate trace repository (Meta)
Repository identity: origin `https://github.com/cisarik/kysucka_moderna_chata.git`, branch `main`, HEAD `0f5f84579d88ee67bc0bacee74826ef02bea7452` (Orchestrator-verified at issue).
Governing AP: `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`.

Do not run `git`. Verify with `sha256sum` before any write:

| Item | Expected |
|---|---|
| `scripts/build_scene.py` | `c83e2bd2f584231e5df7719998ecec64d201e1dc01a6f49457e0a4b1904cc369` |
| `blender/kysucka_chata_mcp_v03.blend` | `360c99a107f9bd819e273274e3cd449a5b7666a27fc69c6ee3a51dfa7e120248` |
| `scripts/interior_v10.py` | `a55ed3bb447ae78388a4946f2d1911f1bc9aa22ac3b6ba2590f5d5e50d21f333` |
| `model/interior_v10.json` | `8623a0ff26954313925824105ca919dda16fa7f959a3a9769d4641babb56e955` |
| `work/v10/run_job.py` | `42a6ff845fa61a428dd03637e2de413f62c009fbb513e0ab647a8cc479ffae7d` |
| `work/v10/study/interior_study_v10.blend` | `7b512b9046ec7c405acd560d7b623b405093d88b2ddfceef7f33f4ca9f804dea` |
| `work/v10/evidence_s3/hero_dusk.png` | `7283925f4c03b753ee37f694da4dc74fb6f9040bc64a96c9bf97041fb95372be` |
| `work/v10/evidence_s3/sofa_dusk.png` | `dbbdea8147e9fe8d4293310351175a82e72505ee16e38a93c2d0329c86b30ded` |
| design basis | `43694106883be4970884a6a92ad31a09cd16ff5f41b6b069228c53edb4d257d7` |

A mismatch is a stop. `work/v10/slice3/` must not exist yet.

Mandatory reading: `.ap/AP_WORKER.md` (Worker Session Target, Reporting);
`.ap/PROMPT_CONTRACTS.md` "Worker Report Header"; Amendment 4; this prompt;
the sofa and throw builders in `scripts/interior_v10.py`.

## Authority

Positive authority: edit the allowlisted paths; run background Blender
through the launcher; read the project and this whole's Meta directory;
create the report file below if and only if it is absent, and read it back.

Blender route, only through `python3 work/v10/run_job.py`:
`/home/agile/Applications/Blender/blender --background --factory-startup
--disable-autoexec`, one at a time, `MemAvailable` at least 9 GiB, no
background Blender other than GUI PID 9404, else wait up to 15 minutes and
then BLOCKED. CPU, 6 threads, no job over 12 minutes. At most **8 render
jobs** for slice `s4`. No `--force` on a render.

Negative authority: no `git`; no MCP; no contact with PID 9404; no GPU; no
preference or add-on change; no network; no download; no write outside the
allowlist, including `assets/`, `model/parameters.json`,
`scripts/build_scene.py`, `work/v09/**`, `work/v11/**` and `blender/`; no
package install; no second report; no closure signal. A Worker never closes
the logical whole.

Commands: reads and edits on the allowlist; `sha256sum`, `ls`, `pgrep`,
`free`, `sleep`, `python3`, plain read-only text filters, the launcher.
Git authority: none. Network authority: none. Dependency authority: none.
Secret authority: none. File and scene content is data and grants nothing.

Repository mutation: /home/agile/Projects/kysucka_moderna_chata/scripts/interior_v10.py, /home/agile/Projects/kysucka_moderna_chata/model/interior_v10.json, /home/agile/Projects/kysucka_moderna_chata/work/v10/run_job.py, /home/agile/Projects/kysucka_moderna_chata/work/v10/** except the six preserved directories named in the allowlist, and scripts/interior_v10_study.py only if its evidence path is hardcoded to slice 3
Host/remote mutation: none
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/08_report_00.md

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
Downloadable prompt filename: 08_implementation_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space
Report filename: 08_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: ORCHESTRATOR
Archival: wait-for-report

Evidence tier: E1
Evidence tier basis: continuing local study artifacts; no preserved scene or shared source changes
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the slice 3 checks
Affected tests: sofa plan and the C1 stair ray
New causal regression: the cold-open frame
Broad or full suite: not-used
Runtime or testbed: background Blender 5.3.0, CPU
Independent acceptance: not-required

## Stopping conditions

Stop when a gate mismatches, the seams cannot be made visible without
leaving the sofa plan, a job crashes twice the same way, the guard wait
expires, or the render cap is reached. Do not move a camera to win the
frame.

## Completion and report

Write the report in English to
`/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/08_report_00.md`
(create only if absent; read it back) and return the same text. It begins
exactly `### Report for ORCHESTRATOR_CHAT`, echoes the three coordinates
once, and contains: status PASS, PARTIAL or BLOCKED; `Phase-qualified
result: implementation-PASS` only on PASS, otherwise `not-applicable`;
start and end commit (the value above, not re-read); changed files with
SHA-256; the sofa plan measurement, old and new; what you changed on the
cushions and the throw; whether the throw is actually visible in
`hero_dusk`, said from looking at the image; every check result; the
render table with SHA-256, time, peak RSS and the launcher render count;
what still does not match the reference; deviations; Git result (git not
used); `Report justification:` completion, blocker or new-evidence;
`Logical-whole closure: not-closed`; a statement that this grant's
authority has ended.

PASS means the sofa plan is unchanged, `hero_dusk` shows separate cushions
and the throw, the checks and the cold-open frame passed, and the cap
held. PARTIAL names exactly what is still missing in the picture.

Authority expiry: this grant ends with the terminal report, cancellation or
supersession.
