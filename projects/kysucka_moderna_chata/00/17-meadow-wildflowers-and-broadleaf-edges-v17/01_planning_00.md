# V17 planning — meadow wildflowers, broadleaf forest-edge groups, and living front-loop trail edges

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: NATURE-DETAIL-V17-PLAN — one decision-complete implementation plan for V17 starting from V16 B (`candidate_exterior_v16.blend`)
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: coordinating multi-layer meadow wildflower/seedhead composition, external/local asset format and KTX2/meshopt import verification in isolated Blender 5.3.0, broadleaf crown placement without sightline/cottage occlusion, and front-loop gravel trail edge/lip/support unification inside a 446.5 MiB packed scene while preserving six `IsViewport` working branches and Michal's live GUI PID 2452
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
Worker planning scope: repository-, scene-, and isolated-probe-grounded technical planning for V17 (meadow botanical layering with curved stems/seedheads/wildflowers, broadleaf beech/birch groups at conifer-meadow transitions, and irregular living front-loop gravel trail edges) starting from immutable V16 B (`work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`)
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

## Goal and Cooperator-selected scope

Produce one decision-complete, measured implementation plan (no scene save in `work/`, no persistent repository or `work/` mutation in this planning exchange) for local candidate **V17** under `work/v17/nature_detail_01/` starting from Michal's selected **V16 B** (`work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`).

V17 must form one coherent natural transition from the close foreground across the front gravel trail loop to the forest edge across three coupled interventions:

1. **Meadow botanical composition and wildflowers:**
   - Select three concrete zones in `CAM_V11_VALLEY_REVIEW`: (a) close foreground (bottom fourth of the frame), (b) the meadow side of the front trail loop below the garden fence, and (c) one forest-to-meadow transition zone. Design a representative pilot sector first that reads clearly both in a fixed low ground-level witness camera and in `CAM_V11_VALLEY_REVIEW`.
   - In the foreground, layer the existing low green cover with basal leaf rosettes/distinct low clusters, arching grass stems with brownish/golden sunlit seedheads, and sparse, irregular clusters of small flower heads (at least one light/white flower form and one restrained yellow form). Determine real centimetre dimensions from the actual meshes. Warm golden accents must come primarily from drier seedheads/stems catching the existing V16 B light (never from V16 c01's large yellow slope blotches). Distant slopes read through vegetation layers without individual flower heads.
   - Replace part of the uniform foreground/sector cover or add small irregular clusters with varied density, gaps, height, tilt, and hue so no regular bands, repeated identical flower stamps, uniform stem tilts, or artificial yellow masks appear. In a 1:1 foreground crop, actual flower heads and seedheads must be distinguishable from random bright noise specks.
2. **Broadleaf tree groups at conifer edges (Kysuce mosaic):**
   - Design several asymmetric broadleaf groups along sunlit conifer margins (plus one readable group or specimen on a more open slope if the composition carries it) so rounded/layered deciduous crowns (`Fagus sylvatica` beech and airy `Betula pendula` birch profiles, or one high-quality broadleaf model across varied growth scales if superior to multiple weak models) soften the spruce-to-meadow boundary in `CAM_V11_VALLEY_REVIEW`.
   - Inspect and record the actual conifer age/height stratification in V16 B (including small trees from earlier wholes). Preserve the dark spruce valley frame, open valley floor axis, cottage silhouette, fence, garden, apple tree, glazing sightlines, and trail clearance. Account for actual crown diameters (not just trunk centers), ground root bases on evaluated terrain, and prefer local replacement of specific edge spruces over adding crown count where density would crowd the frame.
3. **Living front-loop gravel trail surface and edges:**
   - Start with the front trail loop directly in front of the garden fence. Measure why V16 B (`meadow_trail_v16.py`) still renders as a smooth ribbon in `CAM_V11_VALLEY_REVIEW` and compare how V16 c01 (`meadow_trail_v16_c01.py`) softened the upper trail edge (using c01's edge/lip technique only as an edge reference; c01's slope color patches are rejected).
   - Design an irregular, bilaterally asymmetric transition from the compact central gravel track through a thin crushed-fines/loam zone into low leaves and grass, with occasional small stones and thin blades encroaching into the immediate edge across the 15 mm trail lip while keeping the central walkable track clear and continuous to the gate and north boundary. The same boundary field must drive both the shader transition (on trail and terrain) and the surface-supported instance mask.

## Candidate assets and isolated Blender 5.3.0 import/format check

Evaluate local assets first (`assets/models/periwinkle_plant`, `grass_medium_01`, `shrub_01`, `sketchfab_7df0631398f443379fa4541e9efc2343`, and existing V04–V16 masters in `candidate_exterior_v16.blend`), together with the handout's external CC0/CC-BY candidates:
- Mixed low meadow vegetation: `tevy Wildflower Patch v1` (`https://tevy.dev/models/wildflower-patch`, CC0)
- Distinct yellow form: `Poly Haven Dandelion 01` (`https://polyhaven.com/a/dandelion_01`, CC0, Blend format)
- Broadleaf trees: `tevy European Beech v1` (`https://tevy.dev/models/european-beech`, CC0, GLB 3 LODs) and `tevy Silver Birch v1` (`https://tevy.dev/models/silver-birch`, CC0, GLB 3 LODs)
- Backup broadleaf: `Beech tree by evolveduk` (`https://sketchfab.com/3d-models/beech-tree-0983d8933531491f9be71c669e8a907b`, CC-BY) or local/Poly Haven compatible assets.

Because tevy GLB files note `meshopt` compression and `KTX2` textures:
- If your client environment in Native Plan Mode permits outbound HTTPS fetches into `/tmp/opencode/v17_plan_inspect`, run one bounded import & tiny reference-render test in isolated headless Blender 5.3.0 inside `/tmp/opencode/v17_plan_inspect` to verify unpacked geometry, alpha, colors, and KTX2/meshopt support before cleaning `/tmp/opencode/v17_plan_inspect`.
- If Native Plan Mode restricts network access or if tevy KTX2/meshopt fails in stock Blender 5.3.0 glTF importer (modifying Blender's importer is out of scope), record that exact observation and specify the deterministic Stage-0 asset verification/conversion or compatible Poly Haven / local asset fallback in your plan. Every asset used in V17 must be packed/local for offline replay and documented with author, URL, license, version, SHA-256, and modifications.

## Sources, identity, and repository gate

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17`

Repository identity and baseline:
- Project checkout: standalone checkout at `R`, branch `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5` (tracked working tree and index clean; untracked owner file `reference/01.png` with SHA-256 `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` is classified under RF-12 as `unrelated-owner-work` and must remain untouched).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `abfb0ea0226dab1db554abcd47b4cc0a3fc289c1`.

Verified immutable input hashes:
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `work/v16/meadow_trail_01/source/meadow_trail_v16.py`: `16bde4cf14182b99ae4467cdf4f052ab9067c7a2b46613648140775a4f09266e`
- `work/v16/meadow_trail_01/source/meadow_trail_v16.json`: `1298218692c8fe88f27008df9eab287b2f5c3e7bb62866f762df883e748243fb`
- `work/v16/meadow_trail_01/renders/B_v16_960.png`: `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`
- `work/v16/meadow_trail_01/source/meadow_trail_v16_c01.py`: `4e1645e6f7b74ba1295ff357208c842fc4c6fdfd3e0c7812a496a4baa565fd11`
- `work/v16/meadow_trail_01/renders/C_v16_c01_960.png`: `62f4f5afc34f246f125c4da7d22bdb331fde96ac7713b59e6d31420aa196b317`
- Local AI concept reference `reference/01.png` (= `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/references/00.png` = `/home/agile/Projects/chata/chatgpt/01.png`, 1672 × 941): `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- Isolated MCP-disabled preferences `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`

Mandatory reading:
- Governing WORKER spine: `.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18; `.ap/AP_WORKER.md` Worker Session Target and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Planning Record, Plan-to-Execution Gate, Worker Exchange Identity, Mutation Axes Record, Cooperator Delivery and Trace Destination Record.
- Project `AGENTS.md`, `assets/ASSET_MANIFEST.md`, `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_closure.md`, `T/00_handout.md`, and `T/00_notes.md`.
- Visual inputs (inspect actual images): `work/v16/meadow_trail_01/renders/B_v16_960.png`, `work/v16/meadow_trail_01/renders/C_v16_c01_960.png`, and `reference/01.png`.
- Existing source scripts: `work/v16/meadow_trail_01/source/meadow_trail_v16.py`, `work/v16/meadow_trail_01/source/meadow_trail_v16_c01.py`, `work/v14/native_02/source/exterior_light_v14.py`, `work/v13/meadow/correction_01/source/meadow_v13.py`, and `scripts/forest_trail_v07.py`.

## Execution route for isolated headless Blender 5.3.0 probe

Canonical inspection route: **isolated headless Blender 5.3.0 CLI probe** (explicit bounded task route because Michal's live GUI `PID 2452`, `start_ticks 12233` is protected owner work and live MCP `tools.blender.*` is prohibited):
- Verify first that no foreign background Blender is running (only GUI PID 2452 may exist) and available system RAM is ≥12 GiB.
- Run `/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4` with `nice -n 10` and isolated environment (`BLENDER_USER_CONFIG`, `TMPDIR`, `TMP`, `TEMP`) inside `/tmp/opencode/v17_plan_inspect` initialized with a copy of `work/v12/profile_03/isolated_config/userpref.blend`.
- Never write into `R/` or `R/work/`; remove `/tmp/opencode/v17_plan_inspect` completely before submitting your report and verify that `candidate_exterior_v16.blend` SHA-256 and global `/home/agile/.config/blender/5.3/config/userpref.blend` are unchanged.

## Planning deliverables required in `01_report_00.md`

1. **V16 B scene & asset audit:** exact collections, objects, shaders, 6 `IsViewport` working branches (`V12_WORK_CORE_LAWN`, `V12_WORK_CORE_MEADOW`, `V12_WORK_EXTERIOR_MEADOW`, `V12_WORK_FOREST`, `V13_MASTER_MEADOW_WORK`, `V16_MASTER_SHOULDER_WORK`), current conifer age/scale distribution, front-loop trail stations/coordinates (`s`, `lateral`, `half_width`, triangle density), and results of your local/external asset & glTF/Blend import probe.
2. **Three target zones & pilot design:** exact world XY / station coordinates for (a) close foreground sector, (b) meadow side of the front trail loop, and (c) forest-to-meadow transition; pilot sector boundary and fixed low ground-level witness camera pose (`CAM_V17_LOW_DETAIL`) that simultaneously views wildflowers/stems, the front-loop gravel edge transition, and the broadleaf forest margin.
3. **Botanical meadow & wildflower specification:** exact assets/meshes, centimetre dimensions, shader adjustments, density/clustering math, seedhead golden light response under `V16_WORLD_MEADOW_BALANCE`, replacement/addition rules over `V13_MEADOW_CLOUD_*`, and lightweight `IsViewport` working-branch representation.
4. **Broadleaf group specification:** exact species/models (`European Beech`, `Silver Birch`, or verified fallback), LOD/triangle budget, working-branch proxy, exact XY coordinates/scales/rotations, which specific edge conifers are replaced vs complemented, root grounding on evaluated terrain, and crown-diameter clearance proofs for cottage, trail, garden, apple tree, and valley axis.
5. **Front-loop trail edge & shoulder unification:** exact mathematical and shader/geometry formulation combining V16 B's clean slope palette with an asymmetric, irregular front-loop gravel-to-loam-to-grass/leaf transition across the 15 mm lip, scattered edge pebbles/blades, and surface-supported instance masks (`exposure ≤ 1 mm`, `burial ≤ 18 mm`, protected central core).
6. **Implementation workflow, render pairs, and allowlist:**
   - Pilot execution and check (full frame + low ground view) before full V17 expansion, followed by one full candidate `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend`, recipe `work/v17/nature_detail_01/source/nature_detail_v17.py` (+ JSON config and asset manifest), and at most one targeted correction if needed.
   - Matched render suite (serialized one-by-one on CachyOS, CPU4 / 96 samples / OIDN Accurate/High, measuring wall time and peak RSS): (i) `CAM_V11_VALLEY_REVIEW` 960 × 540 pair against V16 B `B_v16_960.png`, (ii) higher-resolution / 1:1 foreground comparison crop from `CAM_V11_VALLEY_REVIEW` sufficient to resolve flower heads, stems, and trail shoulders, and (iii) fixed low ground-level witness render (`CAM_V17_LOW_DETAIL`).
   - Exact file allowlist under `work/v17/nature_detail_01/**`, idempotence, fresh-input replay, cold reopen with offline packed assets, and support/collision gates.

## Authority and mutation axes

Positive authority: read-only inspection of `R`, `R/work/v07`–`R/work/v16`, `/home/agile/meta/projects/kysucka_moderna_chata/00/**`, and `reference/01.png`; bounded isolated headless Blender 5.3.0 probe and optional candidate-asset import test strictly inside temporary `/tmp/opencode/v17_plan_inspect` (cleaned before report); return the complete terminal report in session output for Orchestrator persistence.

Negative authority: no writes to tracked repository files, `R/work/**`, or `/home/agile/meta/**`; no scene save in `R/work/**`; no live MCP calls (`tools.blender.*` prohibited); no touching or signalling Michal's GUI PID 2452; no Blender importer modifications; no package/runtime installation; no Git writes in any repository; no closure signal emission.

Repository mutation: none
Host/remote mutation: bounded temporary `/tmp/opencode/v17_plan_inspect` directory for isolated headless Blender 5.3.0 inspection and asset import probe only (must be removed before report; zero persistent host change)
Trace persistence: none

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 17-meadow-wildflowers-and-broadleaf-edges-v17
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — named exact-content relay because Native Plan Mode blocks direct file writes
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E0
Evidence tier basis: read-only technical planning and isolated temporary headless Blender probe with full cleanup
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: failed repository/hash gate; unexplained divergence; foreign background Blender process; temporary directory cleanup failure; instruction conflict. Stop at the terminal planning report; planning authority expires there.

Completion and report contract: begin the report on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17`, `01`, `01`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: not-applicable`, `Start commit` / `End commit`, changed files = none, validation summary including `/tmp/opencode/v17_plan_inspect` cleanup and unchanged V16 B SHA-256, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-evidence`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Output the complete report text in the session so the Orchestrator can persist it to `T/01_report_00.md`, then stop.

Authority expiry: this terminal planning report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.
