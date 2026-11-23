# V16 planning — golden meadow accents, tree-shadow detail, and irregular gravel-trail shoulders

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: MEADOW-LIGHT-TRAIL-V16-PLAN — one decision-complete implementation plan for V16 against reference `01.png`
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: coordinating terrain/meadow shader golden accents, tree-shadow fill recovery, and irregular 0.45–0.75 m gravel-trail shoulder geometry/masks inside a 433.6 MiB packed scene without breaking validated V13/V15 support or touching the Cooperator's live Blender GUI
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and isolated-scene-grounded technical planning for V16 (golden slope/meadow accents and micro-contrast, tree-shadow readability between V15 B and C, and irregular 0.45–0.75 m vegetated gravel-trail shoulders) starting from immutable V15 C (`candidate_exterior_v15_tonal.blend`)
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

## Goal and Cooperator-selected scope

Produce one decision-complete, measured implementation plan (no scene save, no
render, no repository or `work/` mutation in this planning exchange) for an
editable V16 candidate under `work/v16/meadow_trail_01/` that converges the
exterior valley scene toward Michal's target reference
`/home/agile/Projects/chata/chatgpt/01.png` across three tightly coupled visual
gaps left open at V15 closure (`15-reference-light-v15/01_closure.md`):

1. **Golden slope accents and meadow micro-variation:** In V15 C
   (`C_tonal960.png`), warm clouds and cottage side-light improved over V14/B,
   but the large valley slopes and foreground meadow still read as too smooth
   and uniformly olive compared with `01.png`. Design a bounded, deterministic
   treatment (combining terrain/substrate shader grazing-angle or slope/wave
   warm golden modulation, meadow blade/tuft tonal variation, and/or subtle
   foreground/midground tuft scale or clump breakup) that creates vivid warm
   golden-green sunlit slope accents and natural meadow texture without losing
   continuous V13 ground coverage.
2. **Tree-shadow detail recovery (balancing V15 B and V15 C):** V15 C darkened
   the fill (`0.73` vs B's `1.14`), which improved cottage shadow contrast but
   lost branch and trunk detail in the dark forest stands on the left. Design a
   lighting/shader balance that keeps C's warm clouds, warm key light, and
   readable cottage shadow contrast while restoring subtle shadow detail in the
   conifer canopy and trunks as seen in `01.png` and B.
3. **Irregular gravel-trail width and soft vegetated shoulders (`0.45–0.75 m`):**
   Resolve the deferred V07/V13/V15 trail-edge gap. In V15 B/C, the gravel trail
   curving around the garden and up the right valley slope has a sharp, uniform
   ribbon appearance. On `01.png`, the path has a naturally irregular width and
   soft, organically encroaching grass shoulders with subtle worn edge blending.
   Inspect how the trail mesh, terrain substrate blend, and V11/V13 grass masks
   are stored in `candidate_exterior_v15_tonal.blend`, and design a concrete,
   support-verified irregular edge and shoulder treatment (`0.45–0.75 m` zone)
   that softens the path borders without floating geometry, terrain gaps, or
   grass growing through the travelled gravel core.

Accepted constraints you must preserve (do not reopen):

- **Starting scene:** exact immutable V15 C
  `work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend`
  (433,603,200 bytes, SHA-256
  `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2`).
- **Comparison camera and render profile:** `CAM_V11_VALLEY_REVIEW` with exact
  saved pose and optics; matched native Cycles `CPU`, 4 threads (`--threads 4`),
  96 samples, `960 × 540`, CPU OpenImageDenoise `Accurate` / `High` (GPU
  denoising off), adaptive threshold `0.01`, frame/seed `0`, `AgX` / `None`,
  exposure `0`, gamma `1`. Target native render time stays bounded near the
  established ~105 s baseline (<1.5×). No 4K/UHD render in the initial
  implementation slice (UHD is a separate later decision after 960×540 visual
  inspection).
- **Preserved elements:** cottage architecture, roof, chimney, openings, glass,
  interior V10 objects/lights, enclosed garden polygon, fence, gate, internal
  paving slabs, orchard tree/fruit, 6,200 forest placements, and all 87 packed
  images (exact byte hashes, colorspaces, and target-preserving relative paths,
  including `//../../../v14/assets/qwantani_sunset_puresky_2k.hdr` resolving to
  `work/v14/assets/qwantani_sunset_puresky_2k.hdr`).
- **Working-view branch integrity:** preserve the V12/V13 `IsViewport`
  lightweight working-branch contract (`_working_branch` in
  `work/v14/native_02/source/exterior_light_v14.py`) so Solid orbit performance
  (~30–40 FPS at 1440×900) is not degraded by unswitched high-poly geometry.
- **No live MCP and no interference with Michal's GUI:** Michal's live Blender
  GUI (`PID 2452`, `start_ticks 12233`) is protected owner work. Never call
  `tools.blender.*` MCP tools, never signal or touch PID 2452, and never read
  or modify global Blender user preferences.

## Sources, identity and repository gate

Repository checkout topology: standalone checkout (project) + pinned submodule
`.ap` + separate trace repository (Meta).
Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16`

Project repository identity:
- Local backup origin: `/home/agile/backups/git/kysucka_moderna_chata.git`
- Canonical GitHub URL: `https://github.com/cisarik/kysucka_moderna_chata.git`
- Branch: `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5`,
  clean tracked working tree and empty index (`git status --porcelain=v1`
  empty; ignored `work/` holds the V05–V15 local checkpoints and evidence).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap`
  (gitlink = submodule HEAD, clean detached HEAD).

Exact immutable input hashes (verified by Orchestrator on 2026-11-19; re-verify
before planning reads):

| Input | SHA-256 |
|---|---|
| `work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend` | `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2` |
| `work/v15/reference_01/renders/C_tonal960.png` | `3110941602665c563dfbe9bfe4ce9f118fb4d11dcb2fbc14ffeff15b3b8704d2` |
| `work/v15/reference_01/renders/B_reference960.png` | `1315bb7a50528ca7d77b41527dbf080e3a30bb93805569f351e9ae09751c9cb5` |
| `work/v14/native_02/renders/B_final960.png` | `334bc640d65490dfee64cfe7768daaf85d2bcdbf64f70264420537cadeb72c05` |
| `/home/agile/Projects/chata/chatgpt/01.png` | `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` |
| `work/v15/reference_01/source/reference_light_v15.py` | `40e71376d5b08490c5545eb15fd42c45887ce26714cf2e4ef06549becc5bd57c` |
| `work/v15/reference_01/source/tonal_reference_v15.py` | `72c1cea50d82d95f0a4384d8fe048fb9b19a4905edeff88c32c92c1c6ae52220` |
| `work/v13/meadow/correction_01/source/meadow_v13.py` | `6bf2b052b04101348dbc8167a86335391af7e26383e49bcdd8e348baefc79993` |
| `work/v12/profile_03/isolated_config/userpref.blend` | `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561` |

Mandatory reading:
- Governing WORKER spine: `.ap/AP.md` Semantic Authority + WORKER row,
  RF-03/RF-06/RF-12/RF-18, §8, §18; `.ap/AP_WORKER.md` Worker Session Target
  and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Planning
  Record, Plan-to-Execution Gate, Worker Exchange Identity, Mutation Axes
  Record, Cooperator Delivery and Trace Destination Record.
- Project `AGENTS.md`, `/home/agile/meta/README.md`,
  `/home/agile/meta/projects/kysucka_moderna_chata/00/15-reference-light-v15/01_closure.md`,
  and this whole's `T/00_notes.md`.
- Visual inputs (inspect the actual images): `C_tonal960.png`,
  `B_reference960.png`, `B_final960.png`, and target reference
  `/home/agile/Projects/chata/chatgpt/01.png`.
- Existing recipes and reports:
  `work/v15/reference_01/report_01.md`, `work/v15/reference_01/report_02.md`,
  `work/v15/reference_01/source/reference_light_v15.py`,
  `work/v15/reference_01/source/tonal_reference_v15.py`,
  `work/v14/native_02/source/exterior_light_v14.py`,
  `work/v13/meadow/correction_01/source/meadow_v13.py`, and relevant V11/V07
  trail/terrain scripts (`scripts/forest_trail_v07.py` and `work/v11/source/`).

## Execution route for read-only scene inspection

Canonical inspection route for this planning task: **isolated headless
Blender 5.3.0 CLI read-only probe** (explicit bounded task route because live
GUI PID 2452 is owned by Michal and live MCP is prohibited for exterior V16).
If you run a read-only Python inspection script on
`work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend`:

- Check first that no foreign background Blender is running (only owner GUI
  PID 2452 / start_ticks 12233 may exist) and system available RAM is ≥12 GiB.
- Use `/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`
  with `nice -n 10` and isolated environment variables
  (`BLENDER_USER_CONFIG`, `TMPDIR`, `TMP`, `TEMP`) pointing inside a temporary
  directory `/tmp/opencode/v16_plan_inspect` containing a copy of the
  MCP-disabled `work/v12/profile_03/isolated_config/userpref.blend`.
- Perform strictly read-only inspection (print JSON/observations to stdout;
  never save any `.blend`, never render, never write into `R/` or `R/work/`).
- Remove `/tmp/opencode/v16_plan_inspect` completely before submitting your
  report and verify that global preference witnesses and `candidate_exterior_v15_tonal.blend`
  SHA-256 remain unchanged.

## Planning questions to answer (decision-complete, measured)

Answer these five technical questions with concrete, measured values from the
scene and sources:

1. **Scene & shader inventory of V15 C (`candidate_exterior_v15_tonal.blend`):**
   - What exact objects, meshes, materials, and Geometry Nodes modifiers own:
     (a) the valley terrain and its substrate shader zones (core, trail halo,
     far slopes), (b) the gravel trail ribbon, threshold, and any existing
     shoulder/detail layers, (c) the 29,000 exterior meadow points and their
     blade/clump master materials, and (d) the V15 world
     (`V15_WORLD_REFERENCE_LIGHT`) and sun (`V15_SUN_REFERENCE_KEY`)?
2. **Golden slope accents and meadow micro-contrast design:**
   - How will V16 produce the warm golden-green sunlit slope accents and
     local meadow micro-variation seen in `01.png`? Specify exact shader node
     additions/adjustments (e.g., slope/normal/sun-facing grazing warm golden
     tint, dual-scale macro/micro noise modulation on terrain and meadow master
     materials, and/or bounded tuft height/scale/color variation) and exact
     parameter ranges.
3. **Tree-shadow detail and lighting balance (between B and C):**
   - How will V16 recover readable branch/bark detail in the shaded left forest
     stands while keeping C's warm clouds, warm key light on the cottage, and
     distinct cottage shadow? Specify exact proposed world/fill/key/material
     values and why they avoid both B's flat olive slopes and C's crushed tree
     shadows.
4. **Irregular gravel-trail width and soft vegetated shoulders (`0.45–0.75 m`):**
   - How is the trail geometry and meadow clearance mask currently constructed
     in V15 C? Propose a concrete, deterministic mechanism to give the visible
     trail an organic, subtly irregular effective width and soft, grass-encroached
     `0.45–0.75 m` shoulders (e.g., procedural edge-displacement/alpha or
     vertex/shader irregular gravel-to-loam-to-grass border transition plus
     bounded low-tuft shoulder encroachment with actual terrain/gravel surface
     support and zero core-path intrusion). State how actual support and
     clearance tolerances will be verified.
5. **Implementation architecture, validation, and resource envelope:**
   - Specify the exact allowlist under `work/v16/meadow_trail_01/`
     (`source/meadow_trail_v16.py`, `source/meadow_trail_v16.json`,
     `checkpoints/candidate_exterior_v16.blend`,
     `renders/B_v16_960.png`, `worker/`, `proofs/`, `runtime/`, and
     one-correction paths if needed).
   - Define the staged preservation proof, cold reopen & semantic/portability
     verification (87 packed images, target-preserving relative paths,
     `_working_branch` IsViewport integrity), crop metrics comparing V16
     against V15 C, V15 B, and `01.png` (front meadow, sunlit right/left slopes,
     shaded left forest, cottage shadow, sky, and trail shoulder crops), and
     the single-child CPU4 resource guards (start ≥12 GiB available RAM, own
     RSS ≤8 GiB, system available ≥6 GiB).

## Authority and mutation axes

Positive authority: read-only inspection of the repository, `work/v07`–`work/v15`,
Meta trace files, and `/home/agile/Projects/chata/chatgpt/01.png`; read-only
Git status/log/hash checks; one isolated read-only headless Blender inspection
process using temporary `/tmp/opencode/v16_plan_inspect` (cleaned before
completion). Prepare the complete terminal planning report in your session
output for the named relay.

Negative authority: no writes to tracked repository files or `R/work/`; no
scene save; no render; no live MCP calls (`tools.blender.*` prohibited); no
touching or signalling Michal's GUI PID 2452; no network downloads; no
package/runtime installation; no Git writes in any repository; no closure
signal emission.

Repository mutation: none
Host/remote mutation: bounded temporary `/tmp/opencode/v16_plan_inspect` directory for isolated read-only headless Blender inspection only (must be removed before report; zero persistent host change)
Trace persistence: none

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 16-meadow-light-and-trail-shoulders-v16
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — named exact-content relay because Native Plan Mode blocks direct file writes
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E0
Evidence tier basis: read-only technical planning and isolated headless scene inspection with temporary directory cleanup
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: failed repository/hash gate; unexplained divergence;
foreign background Blender running that does not clear; temporary inspection
cleanup failure; instruction conflict. Stop at the terminal planning report;
planning authority expires there.

Completion and report contract: begin the report exactly
`### Report for ORCHESTRATOR_CHAT`; echo this prompt's three coordinates
(`kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16`, `01`, `01`)
once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`,
`Phase-qualified result: not-applicable`, `Start commit` / `End commit`,
changed files = none, validation summary including cleanup of
`/tmp/opencode/v16_plan_inspect` and unchanged V15 C SHA-256, Git result = no
writes, deviations/risks, one smallest next step, `Report justification: new-evidence`,
authority-expiry statement, compact `Orchestration critique` `MEASURED` /
`LEAD`, `Resolved Execution Issues / Near-Misses`, and
`Pre-Existing Failure Classification`). `Logical-whole closure: not-closed`.
Return the complete report text in session output for exact persistence to
`T/01_report_00.md`, then stop.

Authority expiry: this terminal planning report, cancellation, or supersession
ends this grant; retained context is convenience, not continuing authority.
